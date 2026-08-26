# Seismic Datasets

**A verified, machine-readable index of open seismic data worldwide** — where it is,
how big it actually is, what licence it carries, and whether you can train on it.

[![catalogue](https://img.shields.io/badge/datasets-78-1f3864)](CATALOG.md)
[![artefacts](https://img.shields.io/badge/files_inventoried-239-1f3864)](catalog/file_inventory_field.csv)
[![measured](https://img.shields.io/badge/measured-50.75_TB-1f3864)](catalog/seismic_datasets.xlsx)
[![docs](https://img.shields.io/badge/research_rows-2789-555)](docs/)

---

## Why this exists

Open seismic data is scattered across national regulators, academic archives, cloud
buckets and paper supplements. Finding it is hard. Finding out *how big it is*, *what
you may do with it*, and *whether the link still works* is harder.

A survey of the existing landscape (documented in [`docs/prior-art-and-hubs.md`](docs/prior-art-and-hubs.md))
found something worth stating plainly:

> **No maintained, seismic-focused, machine-readable index of open seismic datasets
> carrying sizes and licences currently exists — and the niche is emptying, not filling.**

Six index nodes have died since 2022: `dataunderground.org` (domain gone),
Agile Scientific (company closed), Papers With Code (shut down), the SEG Wiki's
Open Data page (bot-inaccessible, and **19 of its 69 external links are dead — 28%**,
including the access routes for Teapot Dome, Volve and SMAART), **CWP Colorado School
of Mines** (`www.cwp.mines.edu` — DNS failure) and **Michigan Tech's public seismic
data list** (`geo.mtu.edu/spot/SeismicData/` — redirected to a generic page).
The last two were still linked from the SEG Wiki as live routes when they were checked.

What survives splits into two halves that never meet: **exploration seismic**
(SEG wiki, TerraNubis) and **earthquake seismology** (SeisBench, FDSN). Nothing spans
both. Nothing publishes structured sizes or licences.

## What makes this different

**Sizes are measured, not quoted.** Published figures in this field are frequently
wrong — sometimes catastrophically. Verified during this work:

| Claim | Reality | Error |
|---|---|---|
| An FDSN network DOI declaring 685 TB | ~1.49 TB by actual data rate | **~460x** |
| Poseidon MDIO bucket "~40–50 GB" | 202.11 GB (56,465 objects) | ~4x |
| PoroTomo 187 TB gross | ~52 TB unique (3.5x format redundancy) | 3.5x |
| PubDAS "~90 TB" | 76.6 TB, and it hosts **zero** PoroTomo bytes | — |
| Chevron 2013 TTI "~31.5 GB" | 28,640,141,824 B exactly | — |
| HuggingFace reporting SubsurfaceGen at 1.62 TB | 11.92 TB by tree enumeration | **7.35x — the other way** |

Most errors point the *same* direction — the published number is larger than the truth.
But not all: HuggingFace's `usedStorage` under-reported SubsurfaceGen by **7.35x**,
making the largest open exploration-seismic ML dataset on the Hub look like the second
largest. The rule is not "assume published figures are inflated"; it is **measure**.
So `size_bytes` here is either an exact measured count or **empty** — never a rounded
guess. `size_confidence: official` means *"the holder published this"*, not
*"this is true"*.

**Licensing is answered, not just cited.** Every entry carries five machine-readable
usage axes — `commercial`, `redistribution`, `attribution_required`, `share_alike`,
`ml_training` — plus `usage_basis` recording where the answer came from. Silence is
recorded as `unclear`, never as permission.

The honest headline: **34 entries are commercially usable, 6 are not, and 38 are
unclear.** That last number is the data holders' silence, faithfully recorded.

**Dead ends are recorded too.** Knowing that `freeusp.org` is gone, that Kansas
Geological Survey has never published a single `.sgy` file, or that Azure hosts zero
seismic data saves you the search.

---

## Start here

### I want to train a model today

Open [`catalog/seismic_datasets.xlsx`](catalog/seismic_datasets.xlsx) → **Start Here**
tab. It lists the 139 artefacts that are permissively licensed and directly
downloadable, with 77 of them carrying labels.

Or grab the no-account datasets straight away:

```bash
./scripts/fetch.sh list          # see what needs no account
./scripts/fetch.sh all-nz        # Parihaka + Opunake + Kerry, ~32 GB
./scripts/fetch.sh poseidon-mdio # Poseidon 3D, CC BY 4.0
```

**A suggested first corpus for interpretation ML** (all permissive, no account):

| Dataset | Size | Labels |
|---|---|---|
| [Thebe](CATALOG.md) | 53.09 GB | fault — **CC0**, largest open *field* fault set |
| CIG clinothems | 81.04 GB | RGT — CC BY 4.0 |
| cigCK channels + karsts | 42.87 GB | channel, karst — CC BY 4.0 |
| Parihaka 3D (4 angle stacks) | 20.4 GB | facies |
| F3 facies benchmark | 1.05 GB | facies — MIT, published train/test split |
| Penobscot interpretation | 2.27 GB | horizons — CC BY 4.0 |
| Hardpicks (4 surveys) | 23.79 GB | **first-break picks on real field data** — CC BY 4.0 / OGL-Canada |

For velocity/FWI work the largest permissive option is **SubsurfaceGen field-scale**
(11.92 TB, CC BY 4.0) — start from its 2.81 GB preview repo rather than the full pull.

### I want the big archives

The petabyte-scale national repositories are in [`docs/government-portals.md`](docs/government-portals.md)
(115 portals, every continent). The largest genuinely-free ones with pre-stack data:
**Australia NOPIMS** (~3–4 PB), **Norway Diskos** (>22 PB stored), **UK NDR** (~1 PB),
**Netherlands NLOG** (no registration at all).

### I want to know what's in a specific region

Browse [`CATALOG.md`](CATALOG.md), or the topic documents in [`docs/`](docs/).

---

## Repository layout

```
catalog/
  datasets.yaml              Source of truth — 78 structured entries
  file_inventory_field.csv   105 per-file rows: field surveys
  file_inventory_ml.csv      134 per-file rows: ML + synthetic
  seismic_datasets.xlsx      6-tab workbook built from the CSVs
  SCHEMA.md                  Entry schema + the standing size warning
  FILE_INVENTORY_SCHEMA.md   Per-file schema + ML-readiness scale
CATALOG.md                   Generated from datasets.yaml — do not edit by hand
docs/                        12 research documents, 2,789 catalogued rows
scripts/                     Build and verification tooling
```

### The research documents

| Document | Covers |
|---|---|
| [`government-portals.md`](docs/government-portals.md) | 115 national regulators, every continent |
| [`prior-art-and-hubs.md`](docs/prior-art-and-hubs.md) | Existing indexes, Zenodo/HF/Kaggle/AWS/GCP/Azure |
| [`deep-crustal-refraction.md`](docs/deep-crustal-refraction.md) | COCORP, LITHOPROBE, FIRE, DEKORP, INDEPTH… |
| [`ccs-geothermal-mining.md`](docs/ccs-geothermal-mining.md) | CCS 4D, geothermal DAS, mining, induced seismicity |
| [`cryosphere-polar-seismic.md`](docs/cryosphere-polar-seismic.md) | Antarctic, Greenland, glaciers, icequakes |
| [`das-gaps-and-reconciliation.md`](docs/das-gaps-and-reconciliation.md) | DAS archives + the PubDAS/PoroTomo reconciliation |
| [`ml-synthetic-benchmarks.md`](docs/ml-synthetic-benchmarks.md) | OpenFWI, SEAM, BP/Chevron, fault/facies/salt labels |
| [`earthquake-das-planetary.md`](docs/earthquake-das-planetary.md) | FDSN archives, strong motion, Mars and Moon |
| [`field-volumes-global.md`](docs/field-volumes-global.md) | F3, Volve, Penobscot, Teapot Dome, Stratton… |
| [`field-volumes-nz-au.md`](docs/field-volumes-nz-au.md) | Parihaka, Opunake, Kerry, Poseidon, NOPIMS |
| [`academic-marine-archives.md`](docs/academic-marine-archives.md) | MGDS, NAMSS, PANGAEA, JAMSTEC, SDLS |
| [`us-state-canada-surveys.md`](docs/us-state-canada-surveys.md) | 35 US states, 13 Canadian jurisdictions |

---

## Tooling

```bash
pip install pyyaml pandas openpyxl

python scripts/build_readme.py     # regenerate CATALOG.md from datasets.yaml
python scripts/build_workbook.py   # rebuild the xlsx from the CSVs
python scripts/check_usage.py      # validate usage/licence/size consistency
python scripts/check_links.py      # re-verify every URL (free, no API keys)
```

`check_links.py` exits non-zero on dead links, so it works as a CI gate. Given the 28%
rot measured on the SEG wiki, running it on a schedule matters more than adding entries.

```bash
python scripts/check_links.py --unverified    # only unverified entries
python scripts/check_links.py --downloads     # skip landing pages
python scripts/check_links.py --json report.json
```

---

## Notable finds

Things this survey turned up that appear in no other index:

- **COCORP is openly downloadable and undocumented.** Cornell's server is an
  unauthenticated directory index holding **780 pre-stack land shot gathers (~122 GiB)**.
  No FDSN code, no mirror, unmaintained — **at risk**.
- **The EarthScope "assembled datasets" archive is invisible to FDSN queries** — 852
  datasets, 12.775 TiB, reachable only via an undocumented `?json` endpoint. It holds
  CD-ROM, Deep Probe, SNORCLE, INDEPTH and the Russian PNE profiles, all widely
  described as lost.
- **`gs://noaa-deep-sea-minerals`** — 24.9 TB, CC0, including **998 GiB of SEG-Y**
  across 15,903 files. Absent from Google's own public-datasets documentation.
- **FIRE (Finland)** — 1.147 TB, CC BY 4.0, **with raw field data**. The largest open
  deep-crustal dataset anywhere.
- **OSDU's test bucket is public and anonymous** — including a
  20,311,496,528-byte pre-stack CIP gather. Probably the easiest open pre-stack 3D there is.
- **Kevin Dome, Montana** — ~589 GB of free **nine-component** 3D, supporting
  converted-wave work almost no other open dataset allows.
- **Teal South is 4D *and* 4C, and appears in no index.** 15,326,377,125 B across 38
  files on an unindexed host — an ocean-bottom-cable survey shot twice (1997 baseline,
  1999 monitor) with P-Z *and* P-S converted-wave gathers, plus wells, a VSP,
  directional surveys and observer notes. Time-lapse **and** multicomponent **and**
  pre-stack **and** with wells is a combination nothing else here offers.
- **HuggingFace under-reports its own largest seismic dataset by 7.35x.**
  `subsurfacegen/field-scale-dataset` reports 1.62 TB via `usedStorage`; enumerating the
  tree API gives **11,923,346,031,911 B across 47,084 files**, confirmed by HTTP HEAD.
  It is CC BY 4.0, and it is four times the size of the next largest.
- **Hardpicks: labelled *real field* data for a *processing* task.** 23.79 GB of
  hardrock shot gathers from four Canadian mines with expert first-break picks in the
  trace headers and a cross-survey generalisation split. Every other labelled field
  dataset here is an interpretation task.
- **QuakeFlow DAS ships three subsets its own dataset card never mentions** — including
  a 45.63 GB first-motion **polarity** set.

## Known limits

- **36 entries have `commercial: unclear`.** The holders did not say. Verify before
  relying on it — and always verify before commercial use regardless.
- **55 of 239 artefacts have no measured size.** Mostly session-gated portals. Left
  blank deliberately rather than estimated.
- **The HuggingFace byte figures in `docs/prior-art-and-hubs.md` §b.2 are provisional.**
  They come from HF's `usedStorage`, which this sweep proved unreliable in both
  directions (see §b.6.5). Only the entries re-measured against the tree API are
  trustworthy; the remaining ~300 have not been redone.
- Coverage is deepest for exploration seismic, national archives and ML benchmarks;
  thinner for non-English-language regional portals.
- Sizes and links were verified as of the survey date. Re-run `check_links.py`.

## Contributing

Add or correct entries in [`catalog/datasets.yaml`](catalog/datasets.yaml), then run
`build_readme.py` and `check_usage.py`. Corrections with measured byte counts are
especially welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Catalogue and documentation: **CC BY 4.0**. Tooling: **MIT**. See [LICENSE](LICENSE).

**This repository indexes data; it does not host or redistribute it.** Each dataset
remains under its own licence. The usage flags are a research aid summarising published
licence text — **not legal advice.**
