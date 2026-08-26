#!/usr/bin/env python3
"""Generate CATALOG.md from catalog/datasets.yaml.

The YAML catalog is the single source of truth. Run this after editing it:

    python scripts/build_readme.py

Requires: pyyaml
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml is required:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "datasets.yaml"
OUT = ROOT / "CATALOG.md"

CATEGORY_ORDER = [
    ("field-3d", "Named 3D field surveys"),
    ("field-2d", "Named 2D surveys and line sets"),
    ("national-archive", "National / regulator archives"),
    ("academic-archive", "Academic and research archives"),
    ("ml-benchmark", "ML-ready and labeled datasets"),
    ("synthetic", "Synthetic models and benchmarks"),
    ("passive-waveform", "Earthquake / passive waveform archives"),
    ("das", "Distributed acoustic sensing (DAS)"),
    ("strong-motion", "Strong-motion databases"),
    ("planetary", "Planetary and ocean-bottom"),
    ("hub", "Hubs, registries, and curated lists"),
]

ACCESS_BADGE = {
    "open-download": "🟢 open",
    "open-registration": "🟡 free acct",
    "open-request": "🟡 request",
    "academic-free": "🟡 academic",
    "fee": "🟠 fee",
    "closed": "🔴 closed",
}

CONFIDENCE_MARK = {
    "verified": "",           # trusted, no annotation needed
    "official": "",
    "estimate": " *(est.)*",
    "unknown": "",
}

REQUIRED_FIELDS = ("id", "name", "category", "region", "size_display", "access", "url",
                   "usage", "usage_basis")


@dataclass
class Issue:
    entry_id: str
    message: str


def load(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, list):
        sys.exit(f"{path}: expected a top-level list of entries")
    return data


def validate(entries: Iterable[dict[str, Any]]) -> list[Issue]:
    """Catch the mistakes that actually bite: dupes, missing fields, bad enums."""
    issues: list[Issue] = []
    seen: set[str] = set()
    valid_categories = {c for c, _ in CATEGORY_ORDER}

    for entry in entries:
        eid = entry.get("id", "<no id>")
        for field in REQUIRED_FIELDS:
            if not entry.get(field):
                issues.append(Issue(eid, f"missing required field '{field}'"))
        if eid in seen:
            issues.append(Issue(eid, "duplicate id"))
        seen.add(eid)
        if entry.get("category") not in valid_categories:
            issues.append(Issue(eid, f"unknown category {entry.get('category')!r}"))
        if entry.get("access") not in ACCESS_BADGE:
            issues.append(Issue(eid, f"unknown access {entry.get('access')!r}"))
        if entry.get("size_confidence") not in CONFIDENCE_MARK:
            issues.append(
                Issue(eid, f"unknown size_confidence {entry.get('size_confidence')!r}")
            )
    return issues


def md_escape(text: str) -> str:
    """Pipes inside a cell would break the table."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def link(entry: dict[str, Any]) -> str:
    url = entry.get("url")
    name = md_escape(entry["name"])
    return f"[{name}]({url})" if url else name


def size_cell(entry: dict[str, Any]) -> str:
    display = md_escape(entry.get("size_display") or "unknown")
    return display + CONFIDENCE_MARK.get(entry.get("size_confidence"), "")


def download_cell(entry: dict[str, Any]) -> str:
    targets = entry.get("download") or []
    if not targets:
        return md_escape(entry.get("bulk_method") or "—")
    parts = []
    for t in targets:
        kind = t.get("kind", "link")
        uri = t.get("uri", "")
        parts.append(f"`{kind}`" if not uri else f"[{kind}]({uri})")
    return " · ".join(parts)


def human_bytes(n: int) -> str:
    step = 1000.0
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if abs(n) < step:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= step
    return f"{n:.1f} EB"


def usage_cell(entry: dict[str, Any]) -> str:
    """Compact encoding of what you are allowed to DO with the data."""
    u = entry.get("usage") or {}
    if not u:
        return "?"
    parts = []
    com = u.get("commercial")
    if com == "yes":
        parts.append("COM")
    elif com == "no":
        parts.append("**NC**")
    else:
        parts.append("COM?")
    if u.get("attribution_required") == "yes":
        parts.append("BY")
    if u.get("share_alike") == "yes":
        parts.append("SA")
    if u.get("redistribution") == "no":
        parts.append("**no-redist**")
    if u.get("ml_training") == "yes":
        parts.append("ML")
    return " ".join(parts)


def render_table(entries: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| Dataset | Region | Type | Size | Access | License | Use | Get it |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for e in sorted(entries, key=lambda x: (x.get("country") or "", x["name"])):
        lines.append(
            "| {name} | {region} | {dtype} | {size} | {access} | {lic} | {use} | {dl} |".format(
                name=link(e),
                region=md_escape(e.get("region", "")),
                dtype=md_escape(", ".join(e.get("data_type") or [])),
                size=size_cell(e),
                access=ACCESS_BADGE.get(e.get("access"), e.get("access", "")),
                lic=md_escape(e.get("license") or "—"),
                use=usage_cell(e),
                dl=download_cell(e),
            )
        )
    return lines


def render_summary(entries: list[dict[str, Any]]) -> list[str]:
    by_cat = Counter(e.get("category") for e in entries)
    by_access = Counter(e.get("access") for e in entries)
    known = [e["size_bytes"] for e in entries if isinstance(e.get("size_bytes"), int)]

    lines = ["## At a glance", ""]
    lines.append(f"- **{len(entries)}** catalogued entries across "
                 f"**{len({e.get('country') for e in entries})}** countries/regions")
    if known:
        lines.append(
            f"- **{human_bytes(sum(known))}** of directly-downloadable data with "
            f"exact byte counts ({len(known)} entries measured)"
        )
    openish = sum(by_access[k] for k in ("open-download", "open-registration"))
    lines.append(f"- **{openish}** entries are free to download "
                 f"({by_access['open-download']} with no account at all)")
    lines.append("")
    lines.append("| Category | Entries |")
    lines.append("|---|---|")
    for cat, title in CATEGORY_ORDER:
        if by_cat[cat]:
            lines.append(f"| [{title}](#{slug(title)}) | {by_cat[cat]} |")
    lines.append("")
    return lines


def slug(title: str) -> str:
    return (
        title.lower()
        .replace(" / ", "-")
        .replace(" ", "-")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
    )


def render(entries: list[dict[str, Any]]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in entries:
        grouped[e.get("category")].append(e)

    out: list[str] = []
    out.append("<!-- GENERATED FILE — edit catalog/datasets.yaml, then run "
               "scripts/build_readme.py -->")
    out.append("")
    out.append("# Catalogue")
    out.append("")
    out.append(
        "A catalog of open, public, and potentially accessible seismic datasets "
        "worldwide — exploration reflection seismic, national archives, earthquake "
        "waveforms, DAS, and ML benchmarks."
    )
    out.append("")
    out.extend(render_summary(entries))
    out.append("### Legend")
    out.append("")
    out.append("| Badge | Meaning |")
    out.append("|---|---|")
    for value, badge in ACCESS_BADGE.items():
        out.append(f"| {badge} | `{value}` |")
    out.append("")
    out.append("**\"Use\" column — what you are permitted to DO with the data:**")
    out.append("")
    out.append("| Token | Meaning |")
    out.append("|---|---|")
    out.append("| `COM` | Commercial use permitted |")
    out.append("| `COM?` | Commercial use **not stated** — assume you must ask |")
    out.append("| **`NC`** | Commercial use **excluded** (non-commercial only, "
               "or industry must pay a separate licence) |")
    out.append("| `BY` | Attribution required |")
    out.append("| `SA` | Share-alike — derivatives must carry the same licence |")
    out.append("| **`no-redist`** | You may not redistribute the data |")
    out.append("| `ML` | Licence permits ML/AI training use |")
    out.append("")
    out.append(
        "> **These flags are a research aid, not legal advice.** They are derived "
        "from each holder's published licence text and recorded in `usage_basis` as "
        "`spdx` (a recognised SPDX licence), `licence-text` (stated in prose), "
        "`per-dataset` (a hub — terms vary per dataset), or `unstated` (the holder "
        "publishes no usage terms). **Anything marked `COM?` or `unclear` means the "
        "holder did not say — verify before commercial use.**"
    )
    out.append("")
    out.append(
        "Sizes marked *(est.)* are derived from line-km or survey counts and can be "
        "off by a factor of a few. Machine-readable bounds live in `size_bytes`, or "
        "`size_bytes_min`/`size_bytes_max` where the holder publishes only a range. "
        "See [catalog/SCHEMA.md](catalog/SCHEMA.md)."
    )
    out.append("")

    for cat, title in CATEGORY_ORDER:
        if not grouped.get(cat):
            continue
        out.append(f"## {title}")
        out.append("")
        out.extend(render_table(grouped[cat]))
        out.append("")

    out.append("## Contributing")
    out.append("")
    out.append(
        "Add or correct an entry in [`catalog/datasets.yaml`](catalog/datasets.yaml) "
        "and run `python scripts/build_readme.py`. See "
        "[CONTRIBUTING.md](CONTRIBUTING.md)."
    )
    out.append("")
    return "\n".join(out)


def main() -> int:
    entries = load(CATALOG)
    issues = validate(entries)
    if issues:
        for issue in issues:
            print(f"  {issue.entry_id}: {issue.message}", file=sys.stderr)
        print(f"\n{len(issues)} validation issue(s); README not written.",
              file=sys.stderr)
        return 1
    OUT.write_text(render(entries), encoding="utf-8")
    print(f"Wrote {OUT} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
