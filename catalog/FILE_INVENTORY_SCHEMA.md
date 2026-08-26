# Per-file inventory schema

`catalog/file_inventory.csv` is the file-level companion to `catalog/datasets.yaml`.
Where the YAML catalogue answers *"what datasets exist"*, this answers
*"exactly what will land on my disk, how big is it, and does it come with labels"*.

One row per downloadable artefact. A 3D survey with four angle stacks, a velocity
volume and a well set is **six or more rows**, not one.

## Columns

| Column | Meaning | Example |
|---|---|---|
| `dataset_id` | Matches `id` in `datasets.yaml` — the join key | `parihaka-3d` |
| `dataset_name` | Human name of the parent survey/collection | `Parihaka 3D` |
| `country` | ISO-3166 alpha-2, or `GLOBAL` / `MULTI` / `SYNTHETIC` | `NZ` |
| `basin` | Basin or field | `Taranaki` |
| `product` | What this artefact *is* — see Product vocabulary | `angle stack (near)` |
| `domain` | `post-stack` \| `pre-stack` \| `synthetic` \| `non-seismic` | `post-stack` |
| `migration` | `PSTM` \| `PSDM` \| `time` \| `depth` \| `unmigrated` \| `n/a` | `PSTM` |
| `file_name` | Actual filename, or a glob for multi-file products | `Parihaka_PSTM_near_stack.sgy` |
| `format` | `SEG-Y` \| `HDF5` \| `npy` \| `LAS` \| `zarr/MDIO` \| `ZIP` \| … | `SEG-Y` |
| `size_bytes` | **Exact** byte count, or empty if not measured | `5099504464` |
| `size_human` | Rendered size | `5.10 GB` |
| `size_method` | `HEAD` \| `api` \| `listing` \| `published` \| `estimate` | `HEAD` |
| `n_files` | File count when the row covers many (else `1`) | `1` |
| `dims` | Inline/crossline/sample geometry where known | `1287 x 1000 x 1501` |
| `sample_rate_ms` | Sample interval in ms | `4` |
| `has_labels` | `yes` \| `no` \| `partial` | `yes` |
| `label_type` | `fault` \| `facies` \| `salt` \| `horizon` \| `channel` \| `RGT` \| … | `fault; facies` |
| `label_format` | How labels ship | `PNG masks`, `npy`, `OpendTect horizons` |
| `label_source` | Who produced them + where | `AICrowd 2020 challenge` |
| `ancillary` | Wells/logs/velocities bundled with this artefact | `4 wells; 8 horizons` |
| `license` | Licence string | `CC BY 4.0` |
| `license_spdx` | SPDX id where it maps cleanly | `CC-BY-4.0` |
| `commercial_ok` | `yes` \| `no` \| `unclear` — NC licences block commercial use | `no` |
| `redistribution_ok` | `yes` \| `no` \| `unclear` — may you re-host the data yourself? | `yes` |
| `attribution_required` | `yes` \| `no` \| `unclear` — must you credit the holder? | `yes` |
| `share_alike` | `yes` \| `no` \| `unclear` — must derivatives keep the same licence? | `yes` |
| `ml_training_ok` | `yes` \| `no` \| `unclear` — does the licence permit ML/AI training? | `yes` |
| `usage_basis` | `spdx` \| `licence-text` \| `per-dataset` \| `unstated` — where the answer came from | `spdx` |
| `access` | `open-download` \| `open-registration` \| `open-request` \| `academic-free` \| `fee` | `open-download` |
| `url` | Direct download URL, or the landing page if no direct link | `http://s3.amazonaws.com/...` |
| `verified` | `yes` \| `no` — was this URL/size checked directly | `yes` |
| `ml_ready` | `1`–`5`, see ML-readiness scale | `5` |
| `notes` | Anything a user needs before downloading | `bucket listing denied; key must be exact` |

## Product vocabulary

Use these exact strings so the sheet can be filtered:

`full stack` · `angle stack (near)` · `angle stack (mid)` · `angle stack (far)` ·
`pre-stack gather (CIP)` · `pre-stack gather (shot)` · `pre-stack gather (CDP)` ·
`velocity volume` · `velocity model` · `attribute volume` · `impedance volume` ·
`horizon set` · `fault labels` · `facies labels` · `salt labels` ·
`well logs` · `checkshot` · `VSP` · `navigation` · `report` · `project bundle` ·
`shot gathers (synthetic)` · `4D vintage` · `DAS` · `nodal`

## ML-readiness scale

This is the column that answers "where do I start". It is deliberately opinionated.

| Score | Meaning |
|---|---|
| **5** | Labeled, permissively licensed, direct download, no account. Train today. |
| **4** | Direct download and permissive, but unlabeled — good for pretraining or self-supervision. |
| **3** | Free but needs an account, an order form, or format wrangling before use. |
| **2** | Academic-only, NonCommercial, or awkward bulk access. |
| **1** | Fee-gated, request-only, or effectively closed. Catalogued for completeness. |

## Rules

- **Exact bytes or empty.** Never round into `size_bytes`. `size_human` carries the
  friendly form. An invented byte count is worse than a blank.
- **One row per artefact.** Resist collapsing a survey into a single row — the whole
  point is knowing that Parihaka is 4 × 5.1 GB and not one 20 GB blob.
- **`commercial_ok` is human-curated and authoritative.** It is never overwritten by
  the licence-text derivation used to populate the other usage columns. Where the two
  disagreed during the audit, the curated value won — e.g. the Equinor Open Data Licence
  rows, whose text appends "OSDU repo tooling itself is Apache-2.0"; the *data* is
  academic-use-only even though a *software* licence is named in the same string.
- **The five usage columns mirror `usage:` in `catalog/datasets.yaml`.** See the
  "Usage rights" section of [SCHEMA.md](SCHEMA.md) for the derivation rules and the
  standing caveat that these flags are a research aid, not legal advice. Cost of access
  is recorded in `access`, never as `commercial_ok: no`.
- **`commercial_ok` is load-bearing.** OpenFWI's data is CC BY-NC-SA while its code is
  BSD-3; that distinction decides whether a dataset is usable in a commercial setting,
  so record it per-artefact rather than per-project.
- **Never invent a URL.** Blank plus a note beats a plausible guess.
