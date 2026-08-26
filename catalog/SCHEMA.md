# Catalog schema

The source of truth for this repo is `catalog/datasets.yaml`. The README and any
derived tables are generated from it by `scripts/build_readme.py` — edit the YAML,
never the generated Markdown.

Each entry is one dataset, archive, or portal:

```yaml
- id: parihaka-3d                  # kebab-case, unique, stable (used as anchor)
  name: Parihaka 3D                # display name
  category: field-3d               # see Categories below
  region: New Zealand — Taranaki Basin
  country: NZ                      # ISO-3166 alpha-2, or "GLOBAL" / "MULTI"
  data_type:                       # free-form tags
    - 3D post-stack
    - angle stacks
  ancillary:                       # what ships alongside (optional)
    - none
  size_bytes: 20397919536          # exact when known, else null
  size_bytes_min: null             # lower bound when the holder publishes a range
  size_bytes_max: null             # upper bound when the holder publishes a range
  size_display: "~20.4 GB"         # human string, always present
  size_confidence: verified        # verified | official | estimate | unknown
  license: "Free; acknowledge NZ Petroleum & Minerals"
  license_spdx: null               # SPDX id when it maps cleanly (CC-BY-4.0 etc.)
  usage:                           # WHAT YOU MAY DO WITH IT — see Usage below
    commercial: "unclear"          # yes | no | unclear
    redistribution: "unclear"      # yes | no | unclear
    attribution_required: "yes"    # yes | no | unclear
    share_alike: "unclear"         # yes | no | unclear
    ml_training: "unclear"         # yes | no | unclear
  usage_basis: licence-text        # spdx | licence-text | per-dataset | unstated
  access: open-download            # see Access below
  url: https://wiki.seg.org/wiki/Parihaka-3D
  download:                        # zero or more concrete fetch targets
    - kind: https
      uri: http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/...
  bulk_method: "per-file HTTPS"
  notes: "Classic ML benchmark (SEG/AICrowd fault-ID challenge)."
  verified: true                   # was the URL/size checked directly?
  tags: [ml-benchmark, fault, segy]
```

## Categories

| value | meaning |
|---|---|
| `field-3d` | Named, individually downloadable 3D field survey |
| `field-2d` | Named 2D survey or line set |
| `national-archive` | Government/regulator repository (many surveys) |
| `academic-archive` | University/research-institution repository |
| `ml-benchmark` | Labeled or ML-ready derived dataset |
| `synthetic` | Synthetic/model-based dataset or velocity model |
| `passive-waveform` | Earthquake/passive seismology waveform archive |
| `das` | Distributed acoustic sensing |
| `strong-motion` | Engineering strong-motion database |
| `planetary` | Non-terrestrial seismic |
| `hub` | Aggregator, registry, or curated list |

## Access

| value | meaning |
|---|---|
| `open-download` | Direct download, no account |
| `open-registration` | Free, account required |
| `open-request` | Free, but you must email/order |
| `academic-free` | Free for academia, fee for industry |
| `fee` | Paid, cost-recovery, or licensed |
| `closed` | Not publicly obtainable |

## Usage rights — what the data can be used for

`license` is prose and `license_spdx` is often null, so neither answers the question
people actually have: **may I use this?** The `usage` block answers it in five
machine-readable axes. Every value is `yes`, `no`, or `unclear` — quoted, so YAML
does not coerce them to booleans.

| Field | Question it answers |
|---|---|
| `commercial` | May I use this in commercial work / a commercial product? |
| `redistribution` | May I re-host or redistribute the data myself? |
| `attribution_required` | Must I credit the holder? |
| `share_alike` | Must derivatives carry the same licence? |
| `ml_training` | May I train an ML/AI model on it? |

`usage_basis` records **where the answer came from**, so a reader can weigh it:

| value | meaning |
|---|---|
| `spdx` | The licence is a recognised SPDX licence; the rights follow from it |
| `licence-text` | The holder states the terms in prose, and they were read |
| `per-dataset` | A hub or registry — terms vary per dataset, so nothing is asserted |
| `unstated` | The holder publishes no usage terms at all |

### Rules this catalogue follows

1. **`unclear` is the default.** A right is only asserted when the holder's text
   actually grants it. Silence is recorded as silence, never as permission.
2. **Cost of access is not a restriction on use.** A media or handling fee is an
   `access` property (`fee`, `open-request`, `academic-free`). It never sets
   `commercial: "no"` on its own. `commercial: "no"` is used only where the holder
   genuinely gates commercial or industry use — e.g. an NC licence, an explicit
   "non-commercial" condition, or "free for academia, fee for industry".
3. **US-Government public domain is not CC0.** No SPDX id is asserted for it, but the
   usage profile (commercial yes / redistribute yes / no attribution required) is
   recorded, because that much *is* accurate.
4. **Open Government Licence is jurisdiction-specific.** `OGL-UK-3.0` and
   `OGL-Canada-2.0` are distinct and are not interchanged.
5. **Hubs delegate.** Aggregators (SEG wiki, TerraNubis, AWS Registry, CO2DataShare)
   get `usage_basis: per-dataset` and assert nothing, because their entries carry
   different licences from one another.

### Reproducing and checking the marking

The derivation is not hand-waved — it lives in code and is re-runnable:

| Script | Purpose |
|---|---|
| `scripts/usage_rules.py` | The licence-text -> usage-rights rules, in priority order |
| `scripts/size_rules.py` | Parses `size_display` prose into `size_bytes_min`/`max` |
| `scripts/check_usage.py` | Validates every entry and fails on any contradiction |

Run `python scripts/check_usage.py` after editing the catalog. It exits non-zero if a
usage value is malformed, if an SPDX id is claimed on an `unstated` basis, if size
bounds are inverted, or if a recorded value no longer matches what the rules derive.
It also guards the file inventories: `commercial_ok` there is **human-curated and
authoritative**, and the check fails loudly if the derivation would contradict it.

> **These flags are a research aid, not legal advice.** They summarise published
> licence text as of the survey date. Anything marked `unclear` means the holder did
> not say — verify directly before relying on it, and always verify before commercial
> use regardless of what is recorded here.

## Size bounds

Many holders publish only a range ("~3–4 PB") or a bound (">600 TB"). Those cannot go
in `size_bytes` without inventing precision, so they are captured as:

- `size_bytes_min` — lower bound, or `null` if only an upper bound is published
- `size_bytes_max` — upper bound, or `null` if only a lower bound is published

When an exact figure is known, `size_bytes` is set and both bounds stay absent. When
the holder publishes nothing numeric ("100s of TB", "multi-TB", a record count), all
three stay null and `size_display` carries the prose. Decimal units (GB/TB/PB) and
binary units (GiB/TiB) are parsed distinctly — they are not treated as equivalent.

## Size confidence

- `verified` — byte count from HTTP HEAD, S3 listing, or file inspection
- `official` — a figure published by the data holder
- `estimate` — derived from line-km / survey counts; treat as ±3x
- `unknown` — not published and not estimable

## Size figures: a standing warning

**Published sizes in this domain are frequently wrong, sometimes by orders of
magnitude.** Verified during this research:

- **FDSN network DOIs are registration-time ESTIMATES, not measurements.** Their
  DataCite `sizes` fields total 1.56 PB across the federation, but the largest
  single entry declares 685 TB while its actual data rate implies ~1.49 TB — an
  error of roughly **460x**. Never propagate an FDSN DOI size as fact.
- **DOE GDR labels binary units as "TB"** — its published figures are really TiB.
- **PoroTomo is ~3.5x redundant**: the same ~18 days stored as SEG-Y, H5 and
  H5-standardized. 187 TB gross, ~52 TB unique.
- **PubDAS's "~90 TB"** is a headline figure; its Table 1 holdings sum to 76.6 TB,
  and it hosts no PoroTomo bytes at all.
- **Poseidon's MDIO bucket** is 202.11 GB, not the "~40-50 GB" widely repeated.
- **Chevron 2013 TTI** is 28,640,141,824 B, not "~31.5 GB".

Therefore: `size_confidence: official` means *"the holder published this"*, NOT
*"this is true"*. Only `verified` means measured. When the two disagree, measure.

## Conventions

- Never invent a URL. If the exact path is unknown, point at the canonical landing
  page and put the search phrase in `notes`.
- Prefer exact byte counts. A wrong TB figure is worse than `unknown`.
- Sizes for archives are *released/accessible* volume, not total holdings; note the
  distinction in `notes` when they differ materially.
