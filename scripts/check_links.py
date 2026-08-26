#!/usr/bin/env python3
"""Verify every URL in the catalog and report exact sizes where servers tell us.

Costs nothing but bandwidth — no LLM involved. Use it to check the entries that
were written from knowledge rather than live research.

    python scripts/check_links.py                 # check everything
    python scripts/check_links.py --only nz,au    # filter by country
    python scripts/check_links.py --unverified    # only entries with verified: false
    python scripts/check_links.py --downloads     # only concrete download URIs
    python scripts/check_links.py --write-sizes   # patch size_bytes from Content-Length
    python scripts/check_links.py --json report.json

Exit code is 1 if anything looks broken, so it works as a CI gate.
"""
from __future__ import annotations

import argparse
import json
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml is required:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "datasets.yaml"

TIMEOUT = 30
WORKERS = 8
# Plain urllib gets blocked by a lot of government portals; a browser UA gets
# through most of them. Cloudflare-protected hosts (SEG wiki) will still 403 —
# that is not the same as the link being dead.
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
# Hosts known to refuse automated requests. A failure here is inconclusive, not a
# broken link, so we label it rather than crying wolf.
BOT_HOSTILE = (
    "wiki.seg.org",
    "walrus.wr.usgs.gov",
    "sodir.no",
    "cmgds.marine.usgs.gov",
    "terranubis.com",
    "nzpam.govt.nz",
    "energymining.sa.gov.au",
    "petroleumagencysa.com",
    "digital.csic.es",
)


@dataclass
class Result:
    entry_id: str
    label: str
    url: str
    status: str          # ok | redirect | client-error | server-error | dead | blocked
    code: int | None
    content_length: int | None
    final_url: str | None
    detail: str


def human(n: int | None) -> str:
    if n is None:
        return "—"
    x = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if abs(x) < 1000:
            return f"{x:.0f} {unit}" if unit == "B" else f"{x:.1f} {unit}"
        x /= 1000
    return f"{x:.1f} EB"


def probe(entry_id: str, label: str, url: str) -> Result:
    """HEAD first; fall back to a 1-byte ranged GET for servers that reject HEAD."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # several government portals have broken chains

    def attempt(method: str, extra: dict[str, str] | None = None) -> Result:
        headers = {"User-Agent": UA, "Accept": "*/*"}
        if extra:
            headers.update(extra)
        req = urllib.request.Request(url, method=method, headers=headers)
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            raw = resp.headers.get("Content-Length")
            # A ranged GET reports the slice length, so prefer Content-Range's total.
            crange = resp.headers.get("Content-Range")
            total = None
            if crange and "/" in crange:
                tail = crange.rsplit("/", 1)[-1].strip()
                if tail.isdigit():
                    total = int(tail)
            length = total if total is not None else (int(raw) if raw and raw.isdigit() else None)
            final = resp.geturl()
            return Result(
                entry_id, label, url,
                "redirect" if final.rstrip("/") != url.rstrip("/") else "ok",
                resp.status, length, final if final != url else None,
                resp.headers.get("Content-Type", "") or "",
            )

    blocked = any(h in url for h in BOT_HOSTILE)
    try:
        return attempt("HEAD")
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 501):
            try:
                return attempt("GET", {"Range": "bytes=0-0"})
            except Exception as e2:
                status = "blocked" if blocked else "client-error"
                return Result(entry_id, label, url, status, e.code, None, None,
                              f"HEAD {e.code}, ranged GET failed: {type(e2).__name__}")
        status = "blocked" if blocked and e.code in (401, 403, 429) else (
            "client-error" if 400 <= e.code < 500 else "server-error")
        return Result(entry_id, label, url, status, e.code, None, None, str(e.reason))
    except urllib.error.URLError as e:
        return Result(entry_id, label, url,
                      "blocked" if blocked else "dead",
                      None, None, None, f"{type(e.reason).__name__}: {e.reason}")
    except Exception as e:
        return Result(entry_id, label, url,
                      "blocked" if blocked else "dead",
                      None, None, None, f"{type(e).__name__}: {e}")


def collect(entries: list[dict], args) -> list[tuple[str, str, str]]:
    jobs: list[tuple[str, str, str]] = []
    countries = (
        {c.strip().upper() for c in args.only.split(",")} if args.only else None
    )
    for e in entries:
        if countries and (e.get("country") or "").upper() not in countries:
            continue
        if args.unverified and e.get("verified"):
            continue
        if not args.downloads and e.get("url"):
            jobs.append((e["id"], "landing", e["url"]))
        for d in e.get("download") or []:
            uri = d.get("uri", "")
            # ftp:// and s3:// need different clients; skip rather than false-fail
            if uri.startswith(("http://", "https://")):
                jobs.append((e["id"], d.get("kind", "download"), uri))
    return jobs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="comma-separated country codes (e.g. NZ,AU)")
    ap.add_argument("--unverified", action="store_true",
                    help="only entries with verified: false")
    ap.add_argument("--downloads", action="store_true",
                    help="only concrete download URIs, skip landing pages")
    ap.add_argument("--write-sizes", action="store_true",
                    help="patch size_bytes in the catalog from Content-Length")
    ap.add_argument("--json", metavar="PATH", help="write a full JSON report")
    ap.add_argument("--workers", type=int, default=WORKERS)
    args = ap.parse_args()

    entries = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    jobs = collect(entries, args)
    if not jobs:
        print("nothing to check with those filters")
        return 0

    print(f"probing {len(jobs)} URL(s) with {args.workers} workers...\n")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda j: probe(*j), jobs))

    order = {"dead": 0, "server-error": 1, "client-error": 2,
             "blocked": 3, "redirect": 4, "ok": 5}
    results.sort(key=lambda r: (order.get(r.status, 9), r.entry_id))

    icon = {"ok": "  ok", "redirect": "  ->", "blocked": " blk",
            "client-error": " ERR", "server-error": " ERR", "dead": "DEAD"}
    for r in results:
        code = f"{r.code}" if r.code else "---"
        print(f"[{icon.get(r.status,'  ?')}] {code:>4}  {r.entry_id}/{r.label}"
              f"  {human(r.content_length):>10}  {r.url}")
        if r.final_url:
            print(f"                 redirects to: {r.final_url}")
        if r.status in ("dead", "client-error", "server-error"):
            print(f"                 {r.detail}")

    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    print("\n" + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    if args.json:
        Path(args.json).write_text(
            json.dumps([asdict(r) for r in results], indent=2), encoding="utf-8")
        print(f"report written to {args.json}")

    if args.write_sizes:
        # Only fill in sizes for single-file downloads; a landing page's
        # Content-Length is the size of the HTML, which would be nonsense.
        sized = {r.entry_id: r.content_length for r in results
                 if r.label != "landing" and r.content_length
                 and r.content_length > 10_000_000}
        patched = 0
        for e in entries:
            n = sized.get(e["id"])
            if n and not isinstance(e.get("size_bytes"), int):
                e["size_bytes"] = n
                patched += 1
        if patched:
            CATALOG.write_text(
                yaml.safe_dump(entries, sort_keys=False, allow_unicode=True,
                               width=100),
                encoding="utf-8")
            print(f"patched size_bytes on {patched} entry(ies) "
                  f"— review the diff, formatting will have been normalised")

    broken = sum(counts.get(k, 0) for k in ("dead", "client-error", "server-error"))
    if broken:
        print(f"\n{broken} URL(s) need attention "
              f"(blocked = bot-hostile host, usually still fine)")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
