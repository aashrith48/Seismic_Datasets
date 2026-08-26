#!/usr/bin/env python3
"""Validate the usage/licence/size marking across the catalog.

    python scripts/check_usage.py

Exits non-zero if anything is malformed or if a derived commercial-use flag
contradicts a human-curated one in the file inventories.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    import yaml
except ImportError:
    sys.exit("pyyaml is required:  pip install pyyaml")

from usage_rules import derive
from size_rules import parse as parse_size

ROOT = Path(__file__).resolve().parent.parent
AXES = ("commercial", "redistribution", "attribution_required",
        "share_alike", "ml_training")
TRISTATE = {"yes", "no", "unclear"}
BASES = {"spdx", "licence-text", "per-dataset", "unstated"}


def main() -> int:
    errors: list[str] = []
    entries = yaml.safe_load((ROOT / "catalog" / "datasets.yaml").read_text("utf-8"))

    for e in entries:
        eid = e.get("id", "?")
        usage = e.get("usage")
        if not isinstance(usage, dict):
            errors.append(f"{eid}: missing usage block")
        else:
            for axis in AXES:
                if usage.get(axis) not in TRISTATE:
                    errors.append(f"{eid}: usage.{axis} = {usage.get(axis)!r}")
        if e.get("usage_basis") not in BASES:
            errors.append(f"{eid}: usage_basis = {e.get('usage_basis')!r}")

        lo, hi = e.get("size_bytes_min"), e.get("size_bytes_max")
        if lo and hi and lo > hi:
            errors.append(f"{eid}: size_bytes_min > size_bytes_max")
        if e.get("size_bytes") and (lo or hi):
            errors.append(f"{eid}: has both an exact size_bytes and bounds")
        if e.get("license_spdx") and e.get("usage_basis") == "unstated":
            errors.append(f"{eid}: SPDX id set but usage_basis is 'unstated'")

        # The recorded usage must still match what the rules derive.
        want = derive(e.get("license", ""), e.get("access", ""), eid)
        if isinstance(usage, dict):
            for axis in AXES:
                if usage.get(axis) != want[axis]:
                    errors.append(
                        f"{eid}: usage.{axis} is {usage.get(axis)!r} but the rules "
                        f"derive {want[axis]!r} — re-run the refresh or fix the rule")

    # File inventories: curated commercial_ok must never be contradicted.
    for name in ("file_inventory_ml.csv", "file_inventory_field.csv"):
        path = ROOT / "catalog" / name
        if not path.exists():
            continue
        with path.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                want = derive(row.get("license", ""), row.get("access", ""))
                cur = (row.get("commercial_ok") or "").strip().lower()
                if cur not in TRISTATE:
                    errors.append(f"{name}: commercial_ok = {cur!r}")
                if (want["commercial"] != "unclear" and cur in ("yes", "no")
                        and want["commercial"] != cur):
                    errors.append(
                        f"{name}: curated commercial_ok={cur} contradicts derived "
                        f"{want['commercial']} for {row.get('license','')[:60]!r}")
                if (row.get("usage_basis") or "") not in BASES:
                    errors.append(f"{name}: usage_basis = {row.get('usage_basis')!r}")

    n = len(entries)
    sized = sum(1 for e in entries
                if e.get("size_bytes") or e.get("size_bytes_min") or e.get("size_bytes_max"))
    print(f"{n} catalog entries")
    print(f"  usage rights recorded : {sum(1 for e in entries if e.get('usage'))}/{n}")
    print(f"  usage basis stated    : "
          f"{sum(1 for e in entries if e.get('usage_basis') != 'unstated')}/{n}")
    print(f"  size machine-readable : {sized}/{n}")
    print(f"  license_spdx          : "
          f"{sum(1 for e in entries if e.get('license_spdx'))}/{n}")
    for axis in AXES:
        c = Counter(e["usage"][axis] for e in entries if e.get("usage"))
        print(f"  {axis:<21} yes={c['yes']:<4} no={c['no']:<4} unclear={c['unclear']}")

    if errors:
        print(f"\n{len(errors)} PROBLEM(S):")
        for x in errors:
            print("  -", x)
        return 1
    print("\nOK — usage, licence and size marking is internally consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
