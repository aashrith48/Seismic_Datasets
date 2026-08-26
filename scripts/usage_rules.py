"""Derive structured usage rights from licence text.

Principles:
  1. Cost of ACCESS is not a restriction on USE. A media/handling fee is recorded in
     `access`, never as commercial: no.
  2. 'unclear' is the default. Only assert a right the licence text actually grants.
  3. US-Government public domain is NOT CC0. Leave spdx null; the usage profile is
     still accurately (commercial yes / redistribute yes / no attribution required).
"""
import re


def _u(c, r, a, s, m, spdx, basis):
    return dict(spdx=spdx, commercial=c, redistribution=r,
                attribution_required=a, share_alike=s, ml_training=m, basis=basis)


def derive(lic: str, access: str, entry_id: str = ""):
    low = (lic or "").strip().lower()

    # ---- Hub / aggregator: terms are delegated to each dataset -------------
    if ("per-dataset" in low or "per source licence" in low
            or "keep their own" in low or "datasets keep their own terms" in low):
        return _u("unclear", "unclear", "unclear", "unclear", "unclear", None, "per-dataset")

    # ---- Bespoke restrictive data licences: test FIRST ---------------------
    # These strings often append a SOFTWARE licence ("code is Apache-2.0") that
    # must not be mistaken for the DATA licence.
    if "equinor open data licence" in low:
        # Data is limited to study/research/development by academia.
        return _u("no", "unclear", "yes", "unclear", "unclear", None, "licence-text")
    if "chevron data license agreement" in low:
        return _u("unclear", "unclear", "yes", "unclear", "unclear", None, "unstated")
    if "research-use-only" in low or "research use only" in low:
        return _u("no", "unclear", "yes", "unclear", "unclear", None, "licence-text")
    if "business use licence" in low or "business use license" in low:
        return _u("no", "unclear", "yes", "unclear", "unclear", None, "licence-text")

    # ---- A CC licence that covers only the METADATA is not the data licence -
    if re.search(r"metadata\s+cc[ -]by", low):
        return _u("unclear", "unclear", "yes", "unclear", "unclear", None, "licence-text")

    # ---- Hedged wording: rights are indicative, no hard SPDX id ------------
    # "Mostly CC BY 4.0", "CC-BY-style terms" etc. describe a licence family, not a
    # specific licence. Record the likely rights, but never assert an SPDX id.
    if re.search(r"\bmostly\b|-style\b|\bsimilar to\b", low):
        return _u("yes", "yes", "yes", "unclear", "yes", None, "licence-text")

    # ---- CC0 / explicit public-domain dedication --------------------------
    if "cc0" in low or "public domain dedication" in low:
        return _u("yes", "yes", "no", "no", "yes", "CC0-1.0", "spdx")

    # ---- Government public domain (US / NASA / DOE) -----------------------
    # Accurate usage profile, but NOT CC0 — no SPDX id exists for this.
    if "public domain" in low:
        return _u("yes", "yes", "no", "no", "yes", None, "licence-text")

    # ---- Creative Commons, most restrictive variant first -----------------
    if "cc by-nc-sa 3.0" in low:
        return _u("no", "yes", "yes", "yes", "unclear", "CC-BY-NC-SA-3.0", "spdx")
    if "cc by-nc-sa" in low:
        return _u("no", "yes", "yes", "yes", "unclear", "CC-BY-NC-SA-4.0", "spdx")
    if "cc by-nc 4.0" in low or "cc by-nc" in low:
        return _u("no", "yes", "yes", "no", "unclear", "CC-BY-NC-4.0", "spdx")
    if "cc by-sa" in low:
        return _u("yes", "yes", "yes", "yes", "yes", "CC-BY-SA-3.0", "spdx")
    if "cc by 3.0 nz" in low:
        return _u("yes", "yes", "yes", "no", "yes", "CC-BY-3.0-NZ", "spdx")
    if "cc-by 4.0" in low or "cc by 4.0" in low:
        return _u("yes", "yes", "yes", "no", "yes", "CC-BY-4.0", "spdx")
    if "cc by" in low or "cc-by-style" in low:
        return _u("yes", "yes", "yes", "no", "yes", "CC-BY-4.0", "licence-text")

    # ---- Open Government Licence: jurisdiction matters --------------------
    if "open government licence" in low:
        if "canada" in low:
            return _u("yes", "yes", "yes", "no", "yes", "OGL-Canada-2.0", "licence-text")
        return _u("yes", "yes", "yes", "no", "yes", "OGL-UK-3.0", "licence-text")

    # ---- Software licences (tooling entries) ------------------------------
    if re.search(r"\bmit\b", low) and "permit" not in low:
        return _u("yes", "yes", "yes", "no", "yes", "MIT", "spdx")
    if "bsd-3" in low and "data" not in low:
        return _u("yes", "yes", "yes", "no", "yes", "BSD-3-Clause", "spdx")
    if "apache-2.0" in low:
        return _u("yes", "yes", "yes", "no", "yes", "Apache-2.0", "spdx")
    if "gpl-3.0" in low:
        return _u("yes", "yes", "yes", "yes", "yes", "GPL-3.0-only", "spdx")

    # ---- Genuine USE restrictions (not cost) ------------------------------
    if "non-commercial" in low:
        return _u("no", "unclear", "yes", "unclear", "unclear", None, "licence-text")
    if "no redistribution" in low:
        return _u("unclear", "no", "yes", "unclear", "unclear", None, "licence-text")
    # Industry must pay/licence separately => commercial use is gated.
    if ("fee for industry" in low or "free for academia" in low
            or "free for universities" in low or "public data free for universities" in low):
        return _u("no", "unclear", "yes", "unclear", "unclear", None, "licence-text")

    # ---- Attribution stated, everything else silent -----------------------
    if "acknowledge" in low or low.startswith("cite ") or "; cite" in low:
        return _u("unclear", "unclear", "yes", "unclear", "unclear", None, "licence-text")

    # ---- Everything else: fee-to-obtain, "Free", "Open", unstated ---------
    # NOTE: fee/registration entries land here deliberately. Cost is in `access`.
    return _u("unclear", "unclear", "unclear", "unclear", "unclear", None, "unstated")
