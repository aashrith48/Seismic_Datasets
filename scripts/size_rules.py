"""Parse size_display strings into machine-readable byte bounds.

Returns (min_bytes, max_bytes) or (None, None) when not parseable.
Ranges ('~3-4 PB') become distinct bounds. A single value becomes min == max.
Decimal units (GB/TB/PB) and binary units (GiB/TiB) are honoured separately.
"""
import re

DEC = {"b":1,"kb":10**3,"mb":10**6,"gb":10**9,"tb":10**12,"pb":10**15}
BIN = {"kib":2**10,"mib":2**20,"gib":2**30,"tib":2**40,"pib":2**50}
UNITS = {**DEC, **BIN}

# normalise the various dashes used for ranges
DASHES = "\u2010\u2011\u2012\u2013\u2014\u2212"

NUM = r"(\d[\d,]*(?:\.\d+)?)"


def _v(num, unit):
    return int(float(num.replace(",", "")) * UNITS[unit.lower()])


def parse(display: str):
    if not display:
        return None, None
    s = display.strip()
    for d in DASHES:
        s = s.replace(d, "-")
    low = s.lower()

    # Explicitly non-numeric hedges
    if re.search(r"\bmulti-tb\b|\btens? to\b|\b10s of\b|\b100s of\b|\bdozens\b", low):
        # try "<1 TB (dozens of GB)" style upper bound
        m = re.search(r"<\s*" + NUM + r"\s*(pb|tb|gb|mb|kb|b|pib|tib|gib|mib|kib)\b", low)
        if m:
            return None, _v(m.group(1), m.group(2))
        return None, None

    # Range: "3-4 PB" / "5-15 TB" / "184-190 TB"
    m = re.search(NUM + r"\s*-\s*" + NUM + r"\s*(pb|tb|gb|mb|kb|b|pib|tib|gib|mib|kib)\b", low)
    if m:
        return _v(m.group(1), m.group(3)), _v(m.group(2), m.group(3))

    # Range with units on both sides: "600 TB - 1 PB"
    m = re.search(NUM + r"\s*(pb|tb|gb|mb|kb|pib|tib|gib|mib|kib)\s*-\s*" + NUM
                  + r"\s*(pb|tb|gb|mb|kb|pib|tib|gib|mib|kib)\b", low)
    if m:
        return _v(m.group(1), m.group(2)), _v(m.group(3), m.group(4))

    # Lower bound only: ">600 TB", ">22 PB", ">50 TB"
    m = re.search(r">\s*" + NUM + r"\s*(pb|tb|gb|mb|kb|b|pib|tib|gib|mib|kib)\b", low)
    if m:
        return _v(m.group(1), m.group(2)), None

    # Upper bound only: "<1 TB"
    m = re.search(r"<\s*" + NUM + r"\s*(pb|tb|gb|mb|kb|b|pib|tib|gib|mib|kib)\b", low)
    if m:
        return None, _v(m.group(1), m.group(2))

    # Trailing '+' means a lower bound: "~1 PB+"
    m = re.search(r"~?\s*" + NUM + r"\s*(pb|tb|gb|mb|kb|pib|tib|gib|mib|kib)\s*\+", low)
    if m:
        return _v(m.group(1), m.group(2)), None

    # Single value, possibly with ~ prefix: "14.4 GB", "~150 TB", "202.11 GB ..."
    m = re.search(r"~?\s*" + NUM + r"\s*(pb|tb|gb|mb|kb|pib|tib|gib|mib|kib)\b", low)
    if m:
        v = _v(m.group(1), m.group(2))
        return v, v

    return None, None
