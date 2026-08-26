# DAS Datasets — Gap Fill and Size Reconciliation

Research pass date: **2026-08-24**. All sizes measured or quoted from primary sources on that date.
Status flags: **VERIFIED** = URL fetched / S3 prefix measured live in this pass. **UNVERIFIED** = quoted from a
primary document but the endpoint itself was not exercised this pass.

Units convention used below: **TB = decimal (10^12 B)**, **TiB = binary (2^40 B)**. This distinction turns out to be
load-bearing (see §1.4).

---

## 1. PRIORITY 1 — The PubDAS "~90 TB" vs PoroTomo "172.15 TB" reconciliation

### 1.1 Verdict (short form)

**The two figures are not in conflict, because they describe entirely disjoint things.**

> **PubDAS does not host PoroTomo at all — not the full archive, and not a curated subset.**

- The **~90 TB** is the total of the **eight datasets curated onto the PubDAS Globus endpoint at the University of
  Michigan**. PoroTomo is not one of them. Those eight are: Fairbanks, FORESEE, FOSSA, LaFarge-Conco, Stanford-1,
  Stanford-2, Stanford-3, Valencia.
- **PoroTomo is listed in the PubDAS paper's Table 3**, which is explicitly captioned as a *"Non-exhaustive list of
  other DAS datasets available for download on **other platforms**"*. There it is given as **~81,000 GB (~81 TB)**,
  located at Brady Hot Springs NV, 15 days, access `doi:10.15121/1778858` — i.e. the DOE GDR / OEDI submission, **not**
  PubDAS.
- So the prior note that "PubDAS = ~90 TB across 8 datasets" and the separate measurement "PoroTomo = 172.15 TB on
  GDR/AWS" were **both right**; they were simply never measuring the same archive. There is no overlap to subtract.

### 1.2 (a) What exactly the PubDAS ~90 TB figure covers

Source: Spica, Z. J., Ajo-Franklin, J., Beroza, G. C., Biondi, B., Cheng, F., Gaite, B., Luo, B., Martin, E., Shen, J.,
Thurber, C., Viens, L., Wang, H., Wuestefeld, A., Xiao, H., Zhu, T. (2023), *"PubDAS: A PUBlic Distributed Acoustic
Sensing Datasets Repository for Geosciences"*, **Seismological Research Letters 94(2A), 983–998**,
DOI [10.1785/0220220279](https://doi.org/10.1785/0220220279).

**Pages/APIs actually used (the publisher page is paywalled/403):**

| What | URL | Result |
|---|---|---|
| DOI resolution | `https://doi.org/10.1785/0220220279` | 302 → `pubs.geoscienceworld.org/srl/article/94/2A/983/619682/...` then **HTTP 403** (paywall) — VERIFIED as inaccessible |
| OpenAlex record | `https://api.openalex.org/works/doi:10.1785/0220220279` | `is_oa: true`, `oa_status: green`, `oa_url: https://www.osti.gov/servlets/purl/1957924` — **VERIFIED** |
| Semantic Scholar | `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1785/0220220279?fields=title,abstract,openAccessPdf` | returned the **published abstract verbatim** — **VERIFIED** |
| Green OA full text (LANL accepted manuscript, LA-UR-22-29228) | `https://www.osti.gov/servlets/purl/1957924` | 40-page PDF retrieved and text-extracted — **VERIFIED** |
| OSTI landing page | `https://www.osti.gov/biblio/1957924` | — |

**The published (SRL) abstract, verbatim, via the Semantic Scholar API:**

> "PubDAS currently hosts eight datasets covering a variety of geological settings (e.g., urban centers, underground
> mines, and seafloor), spanning from several days to several years, offering both continuous and triggered active
> source recordings, and **totaling up to ~90 TB of data**."

The same figure recurs twice more in the accepted manuscript body:

> Introduction: "we introduce PubDAS, a public repository **presently hosting 8 DAS datasets, for a total of ~90 Tb**."
>
> Conclusions: "Currently, **~90TB of DAS data are hosted at the University of Michigan**, and there are plans to add
> new datasets upon the conclusion of some experiments and publication embargoes. The PubDAS team has secured support
> **through the end of 2026**."

So the ~90 TB is: *eight curated datasets, on one Globus endpoint, at the University of Michigan.* It is a
**repository-holdings** figure, not an experiment figure.

**Caveat worth flagging (VERIFIED arithmetic):** the paper's own Table 1 volumes sum to **76,604 GB ≈ 76.6 TB**, not 90 TB.
The abstract hedges with *"up to ~90 TB"*. The 13 TB gap is unexplained in the text — most likely headroom/rounding, an
earlier snapshot, or inclusion of ancillary geophone/metadata products. **Treat 76.6 TB as the defensible sum of the
enumerated holdings and ~90 TB as the authors' headline figure.**

### 1.3 (b) Does PubDAS host a curated subset of PoroTomo? — **No.**

This is the crux, and the paper is unambiguous. PoroTomo appears **only** in Table 3, and §8 of the paper
("Public DAS Data Beyond PubDAS") introduces that table like this:

> "the Department of Energy's GDR hosts two frequently cited DAS datasets – **PoroTomo** (University of Wisconsin, 2016)
> and **FORGE 2C** (University of Utah Seismograph Stations, 2022). ... In an effort to centralize the available datasets
> online and acknowledge the work of our peers, **we summarize their availability in Table 3**."

Table 3's caption: *"Non-exhaustive list of other DAS datasets available for download on other platforms."*

Neither PoroTomo nor FORGE 2C is in Table 1 (the PubDAS holdings). **PubDAS mirrors zero bytes of PoroTomo.** The full
PoroTomo archive lives on DOE GDR / OEDI / AWS Open Data and always has.

*(Note the one dataset that legitimately appears in BOTH tables: **FORESEE**. Table 1 = the PubDAS-hosted, 125 Hz
downsampled, 365-day copy at 29,338 GB. Table 3 = the separate Penn State DataCommons copy at 28,670 GB / 180 d. Same
experiment, two independent distributions — see §3.)*

### 1.4 (c) Current authoritative size of each

#### PubDAS — the eight Table 1 datasets

Total of enumerated holdings: **76,604 GB = 76.6 TB**. Headline figure in the paper: **~90 TB**.
Access: Globus only (see §2).

#### PoroTomo — measured live on AWS this pass

`aws s3 ls --no-sign-request --recursive --summarize s3://nrel-pds-porotomo/DAS/...` executed 2026-08-24:

| Prefix | Objects | Bytes | Decimal TB | Binary TiB |
|---|---:|---:|---:|---:|
| `DAS/SEG-Y/DASH/` | 81,424 | 51,014,450,198,036 | 51.01 | **46.40** |
| `DAS/SEG-Y/DASV/` | 22,826 | 1,052,714,801,119 | 1.05 | 0.96 (980.4 GiB) |
| `DAS/SEG-Y/DASH_NV-test-site-explosion/` | 285 | 106,727,757,760 | 0.107 | 0.097 |
| `DAS/H5/DASH/` | 40,632 | 89,296,445,626,120 | 89.30 | **81.21** |
| `DAS/H5/DASV/` | 15,174 | 1,474,257,452,440 | 1.47 | **1.34** |
| `DAS/H5/DASH_NV-test-site-explosion_standardized/` | 284 | 106,587,753,520 | 0.107 | 0.097 |
| `DAS/H5-standardized/DASH/` | 40,782 | 42,753,472,676,848 | 42.75 | 38.88 |
| `DAS/H5-standardized/DASV/` | 22,798 | 1,056,549,612,608 | 1.06 | 0.96 |
| **TOTAL `DAS/`** | **224,205** | **186,861,205,878,451** | **186.86** | **169.94** |

**This resolves the "172.15" number precisely.** The GDR submission page states per-resource sizes of
"DASH SEG-Y 46.4 TB", "DASH HDF5 81.21 TB", "DASV SEG-Y 980.42 GB", "DASV HDF5 1.34 TB". Those match my measured
byte counts **exactly when converted to binary units** (51,014,450,198,036 B ÷ 2^40 = 46.40; 89,296,445,626,120 B ÷ 2^40
= 81.21; 1,052,714,801,119 B ÷ 2^30 = 980.4; 1,474,257,452,440 B ÷ 2^40 = 1.34).

> **Therefore: GDR labels binary units as "TB". The "172.15 TB" figure is really ~172 TiB ≈ 189 decimal TB.**
> My independent measurement of the live bucket gives 169.94 TiB / 186.86 decimal TB — consistent to ~1%.

#### The second, larger point about PoroTomo: **~3.5x of it is format redundancy**

The bucket stores the *same underlying recordings* three times over:

- **SEG-Y** (original interrogator output) — 52.17 TB
- **H5** (HDF5 conversion) — 90.88 TB
- **H5-standardized** (DAS-RCN-style standardized HDF5) — 43.81 TB

The unique scientific content is roughly **one copy ≈ 52 TB** (SEG-Y, DASH + DASV + the NV test-site explosion), covering
~18 days of recording (DASH 8–26 Mar 2016 trenched horizontal fibre; DASV 17–28 Mar 2016 vertical fibre through 363 m of
a well). The HDF5 copy being *larger* than the SEG-Y copy (89.3 vs 51.0 TB for DASH) is consistent with a wider sample
dtype / uncompressed chunking, not with additional data.

So: **PubDAS ~90 TB (8 datasets, no PoroTomo) and PoroTomo ~187 TB decimal / ~170 TiB (one experiment, stored in three
formats) are entirely independent, and the PubDAS paper's own Table 3 quotes PoroTomo at ~81 TB — its size at the
2022 time of writing, before the H5-standardized conversion was added.**

### 1.5 PoroTomo — authoritative record

| Field | Value |
|---|---|
| Name | PoroTomo Natural Laboratory Horizontal and Vertical Distributed Acoustic Sensing Data |
| Institution | University of Wisconsin–Madison (PoroTomo project); hosted by NREL/OEDI for DOE GTO |
| Location | Brady Hot Springs, Nevada, USA |
| Duration | DASH 8–26 Mar 2016 (trenched horizontal); DASV 17–28 Mar 2016 (vertical, 363 m of well) |
| Size | **186.86 TB decimal / 169.94 TiB measured**; GDR page states 172.15 (binary) |
| Objects | 224,205 (30-second files organised by day) |
| Format | SEG-Y, HDF5, standardized HDF5 |
| Licence | **CC-BY-4.0** |
| DOI | `https://doi.org/10.15121/1778858` |
| GDR landing page | `https://gdr.openei.org/submissions/980` — **VERIFIED** |
| S3 | `s3://nrel-pds-porotomo/DAS/` (no-sign-request) — **VERIFIED, measured** |
| OEDI viewer | `https://data.openei.org/s3_viewer?bucket=nrel-pds-porotomo` |
| Note | awesome-das points at `https://gdr.openei.org/submissions/849` for PoroTomo; submission **980** is the DAS-specific record carrying the 172.15 figure |

---

## 2. PubDAS — full holdings (Table 1 of Spica et al. 2023)

**Access method for all eight: Globus only.** No HTTP/S3 mirror exists.

- Globus endpoint / collection UUID: **`706e304c-5def-11ec-9b5c-f9dfb1abb183`**
- File manager link (from the paper's Data & Resources section):
  `https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2F`
- **A free Globus account is required.** Globus Connect Personal is the client.
- Host: Advanced Research Computing, University of Michigan. Funding: Air Force Research Laboratory grant
  FA9453-21-2-0018. Support secured **through end of 2026**.
- ⚠️ **The old PubDAS web front-end is DEAD.** `http://piweb.ess.washington.edu/pubdas/` fails DNS resolution
  (`ENOTFOUND`) as of 2026-08-24. `pubdas.org`, `www.pubdas.org`, `pubdas.ess.washington.edu` and `pubdas.umich.edu` all
  fail to connect. **VERIFIED DEAD.** The Globus UUID above is the only surviving access path found.

| # | Dataset | Location | Interrogator | Span (d) | Format | Sps (Hz) | Vol. (GB) | GL (m) | Cable (m) | Ch. spacing (m) | Units | Flag |
|---|---|---|---|---|---|---|---:|---|---:|---|---|---|
| 1 | **Fairbanks** Permafrost Experiment Array | Farmer's Loop, Fairbanks, AK (USACE CRREL) | Silixa iDAS-v2 | 59 (active src) | TDMS | 1,000 | 10,441 | 10 | 4,000 | 1 | strain rate | VERIFIED (paper) |
| 2 | **FORESEE** | State College, PA (Penn State campus) | Silixa iDAS-v2 | 365 | HDF5 | 125 (÷ from 500) | **29,338** | 10 | 4,900 | 2 | strain rate | VERIFIED (paper) |
| 3 | **FOSSA** | W. Sacramento → Woodland, CA (DOE ESnet dark fibre) | Silixa iDAS-v2 | 7 | TDMS | 500 | 11,680 | 10 | 23,300 | 2 | strain rate | VERIFIED (paper) |
| 4 | **LaFarge-Conco Mine** | North Aurora, IL (limestone/dolomite mine) | Silixa iDAS | 2 (active src) | SEG-Y | 1,000 | 45 | 10 | 1,120 | 1 | strain rate | VERIFIED (paper) |
| 5 | **Stanford-1** (Campus Array) | Stanford, CA | OptaSense ODH3 | **940** | SEG-Y | 50 | 18,908 | 7.14 | 2,500 | 8.16 | strain | VERIFIED (paper) |
| 6 | **Stanford-2** (Sandhill Road) | Palo Alto, CA | OptaSense ODH3 | 14 | SEG-Y | 250 | 2,887 | 20 | 10,200 | 8.16 | strain | VERIFIED (paper) |
| 7 | **Stanford-3** (dual-IU campus) | Stanford, CA | OptaSense ODH4 (+ODH3) | 6 | SEG-Y | ~ | 92 | ~ | 2,500 | 8.16 | strain | VERIFIED (paper) |
| 8 | **Valencia** (Valencia–IslaLink) | Valencia → Palma de Mallorca, Spain (submarine) | Febus Optics A1-R | 7 | HDF5 | 250 (÷ from 1,000) | 3,213 | 30.4 | 50,000 | 16.8 | strain rate | VERIFIED (paper) |
| | **TOTAL** | | | | | | **76,604 GB = 76.6 TB** | | | | | computed |

`÷` = downsampled with anti-aliasing low-pass. Only FORESEE and Valencia are pre-processed; the other six are raw
interrogator output.

### 2.1 Per-dataset notes (from the paper body)

**Fairbanks** — 2D grid of hybrid tactical fibre in trenches 20–40 cm deep, monitoring an *in-ground heating experiment
thawing a section of permafrost*. Four road-parallel lines (A–D, ~180 m each) crossing the heater, plus five
perpendicular lines (1–5). PubDAS hosts the **active-source** portion: sequential shots from a single Surface Orbital
Vibrator (SOV) swept nightly for time-lapse monitoring. **Co-located geophone recordings of the SOV sweeps are archived
too** (useful for deconvolution).

**FOSSA** — 27 km of DOE ESnet dark telecom fibre; usable quality on ~23.3 km = **11,648 channels at 2 m**. Recorded
28 Jul 2017 – 18 Jan 2018 at 500 Hz, generating **210 TB of raw uncompressed data** — of which PubDAS publishes **one
week** (11,680 GB). Cable mostly in conduit 1–1.5 m deep in soil; some sections in shallow horizontal boreholes 3–4 m
under roads/railways.

**LaFarge-Conco** — room-and-pillar mine, ~1,500 × 500 m, four levels to ~80 m depth. ~1,120 m of tactical cable in an
L-shaped loop over three layers: Loop 1 cemented into a saw-cut floor groove (sharpest P arrivals), Loop 2 covered with
rock powder, Loop 3 loose (poorest arrivals). Sources: 23 kg / 208 J weight drops, plus two mine blasts at ~200 m and
~450 m.

**Stanford-1** — fibre loosely deployed in air-filled ~12 cm PVC conduit; coupling by gravity/friction only. **626
channels**, continuous 2 Sep 2016 – 31 Mar 2019. **Longest time span in PubDAS at 940 days.** Tap-test calibrated.

**Stanford-2** — citywide Palo Alto extension of Stanford-1. **1,250 channels**, 10.2 km, write rate **~101 GB/day**.
PubDAS hosts two full weeks, 1–14 Mar 2020, all channels at native 250 Hz. Channels 400–750 (Sandhill Road, Stanford
Hospital → SLAC) have the highest SNR; located by driving a car at constant velocity along the fibre at night.

**Stanford-3** — temporary dual-interrogator experiment 5–13 Oct 2017 on the *same* Stanford-1 cable loop. An OptaSense
**ODH-4** was attached alongside the running ODH-3 with identical acquisition parameters for three days, then various
gauge lengths and sample rates were tested on the ODH-4 alone. **ODH-4 showed better data quality than ODH-3.** Three
USGS broadband seismometers were installed in building basements inside the loop for comparison.

**Valencia** — pre-installed IslaLink Holding Iberia S.L. telecom cable, Spanish peninsula → Mallorca. Febus Optics A1-R
on the Valencia end sampling the first **50 km**: first **9,189 m on land** (confirmed by traffic noise), remaining
**40,811 m buried ~1 m below the Mediterranean seabed** (confirmed by marine gravity waves and secondary microseism).
Native 1,000 Hz, 30 m gauge length, 16.8 m spatial resolution → **2,977 channels**. Downsampled to 250 Hz with a
10th-order Chebyshev low-pass below 125 Hz, and hour-long files truncated to 10-minute files. **Only 1–7 Sep 2020 is
published** — the second week had too many recording gaps.

---

## 3. Ridgecrest DAS (SCEDC / Caltech) — MEASURED

**S3 prefix measured live: `aws s3 ls --no-sign-request --recursive --summarize s3://scedc-pds/Ridgecrest_DAS/`**

| Field | Value | Flag |
|---|---|---|
| Name | Ridgecrest DAS (Ridgecrest–Inyokern airport dark fibre) | |
| Institution | Southern California Earthquake Data Center (SCEDC), Caltech | |
| Location | Between Ridgecrest and Inyokern airport, California, USA | |
| **Total size** | **4,090,776,008,465 bytes = 4.09 TB (3.72 TiB)** | **VERIFIED (measured)** |
| Objects | **911** total = 909 hourly SEG-Y + `das_info.csv` + `README_citation.txt` | **VERIFIED** |
| File cadence | Hourly SEG-Y, each exactly **4,500,303,600 bytes** | **VERIFIED** |
| Coverage | Files span `2020062000` → `2020072923` (UTC hour-stamped). README states recording 2020/06/23–2020/07/29. 909 of a possible 960 hours ⇒ ~51 hours of gaps | **VERIFIED** |
| Channels | **1,250 traces** (derived exactly from file size: 1,250 × 900,000 samples × 4 B + 1,250 × 240 B trace headers + 3,600 B textual/binary header = 4,500,303,600 B). `das_info.csv` geolocates **1,150** of them (index 25–1174, columns `index,latitude,longitude,elevation_m`) | **VERIFIED (derived + measured)** |
| Sample rate | **250 Hz** (900,000 samples/hour ÷ 3,600 s) | **VERIFIED (derived)** |
| Format | **SEG-Y**, 4-byte samples | **VERIFIED** |
| Licence | Not stated in-bucket; SCEDC open data. Citation required (see below) | UNVERIFIED (licence text) |
| Access | AWS Open Data, anonymous S3, no credentials | **VERIFIED** |

**Verified URLs**
- `s3://scedc-pds/Ridgecrest_DAS/SEG-Y/hourly/YYYYMMDDHH.segy`
- `https://scedc-pds.s3.amazonaws.com/Ridgecrest_DAS/das_info.csv` — **VERIFIED, 1,151 lines**
- `https://scedc-pds.s3.amazonaws.com/Ridgecrest_DAS/README_citation.txt` — **VERIFIED**
- Bucket root listing: `https://scedc-pds.s3.amazonaws.com/?list-type=2&delimiter=/` — **VERIFIED**

**Required citations (verbatim from `README_citation.txt`):**
- Li et al. 2021 — `https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021AV000395`
- SCEDC (2013): Southern California Earthquake Center. Caltech. Dataset. `doi:10.7909/C3WD3xH1`

**Sibling prefixes discovered in the same bucket** (VERIFIED to exist): `Malibu_Nodal/`, `continuous_waveforms/`,
`event_waveforms/`, `event_phases/`, `earthquake_catalogs/`, `FDSNstationXML/`, `indexmap/`.

---

## 4. DAS-RCN `awesome-das` — full repository enumeration

Source: `https://raw.githubusercontent.com/DAS-RCN/awesome-das/main/README.md` — **VERIFIED fetched**.
Repo metadata via `https://api.github.com/repos/DAS-RCN/awesome-das` (HTTP 200) — **VERIFIED**.

The list contains **10 entries** in two sections. Every URL below was present in the README verbatim.

### 4.1 General DAS Data Repositories (7)

| # | Name | URL (verbatim from README) | Notes |
|---|---|---|---|
| 1 | PoroTomo Experiment at Brady Hot Springs | `https://gdr.openei.org/submissions/849` | See §1.5 — the DAS-specific record is submission **980**, ~187 TB |
| 2 | FORGE Phase 2C | `https://gdr.openei.org/submissions/1185` | Utah FORGE, already catalogued elsewhere |
| 3 | Garner Valley | `https://gdr.openei.org/submissions/614` | ~165 GB, 1 day, active source (per PubDAS Table 3, `doi:10.15121/1261941`) |
| 4 | Belgium DAS | `https://data.caltech.edu/records/1296` | ~1.3 GB, Zeebrugge, 1 day (`doi:10.22002/D1.1296`) |
| 5 | Monterey Bay Dark Fiber | `https://github.com/njlindsey/Photonic-seismology-in-Monterey-Bay-Dark-fiber1DAS-illuminates-offshore-faults-and-coastal-ocean` | ~0.565 GB, Moss Landing CA, 4 days |
| 6 | RCA Shore Station, Cascadia Margin (OOI) | `https://oceanobservatories.org/2022/02/distributed-acoustic-sensing-lays-groundwork-for-earthquake-tsunami-warnings-and-more/` | Announcement page, FTP access. Data host `piweb.ooirsn.uw.edu/das/`, ~26 TB, 5 days ("RAPID") |
| 7 | **PubDAS** | `https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2F` | The Globus endpoint — see §2 |

### 4.2 Earthquake-Specific Datasets (3)

| # | Name | URL (verbatim) | Notes |
|---|---|---|---|
| 8 | SAFOD DAS Array | `https://github.com/ariellellouch/DASDetection` | ~1.54 GB, San Andreas Fault CA |
| 9 | Stanford Phase 1 Experiment | `https://github.com/eileenrmartin/FiberOpticEarthquakes` | Small event extracts, not the full Stanford-1 archive |
| 10 | Fairbanks Farmers Loop | `https://github.com/eileenrmartin/FiberOpticEarthquakes` | Same repo as #9 |

**Caveat:** the awesome-das list is a *pointer list*, not a size catalogue — it carries **no sizes at all**. The sizes in
the tables above come from PubDAS Table 3 and from my own measurements, not from awesome-das.

### 4.3 Other DAS-RCN GitHub repositories (VERIFIED via `https://api.github.com/orgs/DAS-RCN/repos`)

Software, not data, but relevant tooling:

| Repo | Description |
|---|---|
| `DAS-RCN/IntroToDASData` | "a friendly introduction to reading and working with DAS data" |
| `DAS-RCN/Vertical-DAS-Processing` | "Various methods for handling data from vertical DAS arrays" |
| `DAS-RCN/continuous_data_handling` | "Methods for handling continuous DAS data (loading, buffering, data processing...)" |
| `DAS-RCN/jDAS` | "Coherence-based Deep Learning denoising of DAS data" |
| `DAS-RCN/DAS_metadata` | "Tools for standardizing Distributed Acoustic Sensing (DAS) metadata" |
| `DAS-RCN/RCN_DASformat` | The standardized DAS format effort (relates to PoroTomo's `H5-standardized/`) |
| `DAS-RCN/mldas` | ML on DAS |
| `DAS-RCN/awesome-das` | The curated list above |
| `DAS-RCN/DAS-RCN` | Org profile |

⚠️ `das-rcn.org` and `dasrcn.org` **both fail to connect** (VERIFIED DEAD as of 2026-08-24). The GitHub org is the live
presence.

---

## 5. Other DAS datasets catalogued in PubDAS Table 3 (external platforms)

Verbatim from Table 3 of Spica et al. 2023. Sizes are the authors' 2022 figures unless I re-measured (flagged).
`⋆` = contains active sources.

| Short name | Approx. vol. (GB) | Location | Span (d) | Access (verbatim) | Flag |
|---|---:|---|---:|---|---|
| DAS4Microseism | 182 | Svalbard, Norway | 42 | `doi:10.18710/VPRD2H` | UNVERIFIED |
| DAS4Whale | 37.6 | Svalbard, Norway | 2 | `doi:10.5281/zenodo.5823343` | UNVERIFIED |
| RAPID (OOI RCA) | 26,000 | Offshore Pacific City, OR | 5 | `piweb.ooirsn.uw.edu/das/` | UNVERIFIED |
| **PoroTomo** ⋆ | 81,000 (2022) | Brady Hot Springs, NV | 15 | `doi:10.15121/1778858` | **RE-MEASURED: 186.86 TB — see §1.4** |
| FORGE 2C ⋆ | ~ | Milford, Utah | ~ | resolves to `https://constantine.seis.utah.edu/datasets.html` | **URL VERIFIED (redirect resolved)** |
| Marcellus ⋆ | ~ | Morgantown, WV | ~ | `https://www.mseel.org/` | UNVERIFIED |
| Garner Valley ⋆ | 165 | California | 1 | `doi:10.15121/1261941` | UNVERIFIED |
| Levee Workshop ⋆ | 0.741 | Black Hawk, LA | 1 | `doi:10.17603/ds2-c96x-pg70` | UNVERIFIED |
| Belgium | 1.3 | Zeebrugge, Belgium | 1 | `doi:10.22002/D1.1296` | UNVERIFIED |
| Monterey Bay | 0.565 | Moss Landing, CA | 4 | resolves to `https://github.com/njlindsey/Photonic-seismology-in-Monterey-Bay-Dark-fiber1DAS-illuminates-offshore-faults-and-coastal-ocean` | **URL VERIFIED (redirect resolved)** |
| SAFOD | 1.54 | San Andreas Fault, CA | ~ | resolves to `http://github.com/ariellellouch/DASDetection` | **URL VERIFIED (redirect resolved)** |
| **FORESEE** | 28,670 | State College, PA | 180 | resolves to `http://www.datacommons.psu.edu/commonswizard/MetadataDisplay.aspx?Dataset=6290` | **URL VERIFIED (redirect resolved)** |

**Short-URL resolutions performed this pass** (the paper cites tinyurls, which are fragile — resolved and recorded here
so they survive link rot):

| tinyurl in paper | Resolves to | Flag |
|---|---|---|
| `tinyurl.com/499mn4pa` | `http://www.datacommons.psu.edu/commonswizard/MetadataDisplay.aspx?Dataset=6290` | **VERIFIED (301)** |
| `tinyurl.com/2p8epnn5` | `https://constantine.seis.utah.edu/datasets.html` | **VERIFIED (301)** |
| `tinyurl.com/ynab86bc` | `https://github.com/njlindsey/Photonic-seismology-in-Monterey-Bay-Dark-fiber1DAS-illuminates-offshore-faults-and-coastal-ocean` | **VERIFIED (301)** |
| `tinyurl.com/yc49swp4` | `http://github.com/ariellellouch/DASDetection` | **VERIFIED (301)** |

---

## 6. FORESEE (Penn State) — consolidated

FORESEE = **F**iber-**O**ptic fo**R** **E**nvironment **SE**ns**E**ing. It is the **largest single dataset on PubDAS**.

| Field | Value | Flag |
|---|---|---|
| Name | FORESEE — Fiber-Optic foR Environment SEnsEing Array | |
| Institution | **Penn State University** (Tieyuan Zhu, Junzhu Shen — Dept. of Geosciences) | VERIFIED (paper) |
| Location | Penn State campus, **State College, central Pennsylvania**, Valley & Ridge Appalachians | VERIFIED |
| Fibre | **~5 km** single-mode **dark fibre** beneath campus, in buried concrete conduit **1–10 m deep**. Two individual fibres spliced together around **channel 1340** | VERIFIED |
| Channels | **2,137 channels accurately located by tap test**; 2 m channel spacing; 10 m gauge length. Channels 1–604 = quiet off-campus; remainder = main campus with strong anthropogenic noise | VERIFIED |
| Interrogator | Silixa iDAS-v2 | VERIFIED |
| Native sample rate | **500 Hz** | VERIFIED |
| Full experiment duration | **5 Apr 2019 → 4 Oct 2022 (~3.5 yr continuous strain-rate)** | VERIFIED (paper) |
| **PubDAS portion** | **First year only: 5 Apr 2019 – 14 Mar 2020**, downsampled 500 → **125 Hz**, **HDF5**, **29,338 GB (29.3 TB)**. Recordings interrupted several times by power outages; files rewritten for HDF5 consistency during preprocessing | VERIFIED |
| **Penn State portion** | Separate distribution: **28,670 GB, 180 days**, at `http://www.datacommons.psu.edu/commonswizard/MetadataDisplay.aspx?Dataset=6290` | URL VERIFIED (resolved); size UNVERIFIED |
| Access | PubDAS copy: **Globus** (UUID `706e304c-5def-11ec-9b5c-f9dfb1abb183`). PSU copy: PSU DataCommons web | VERIFIED |
| Licence | Not stated in the paper | UNVERIFIED |
| Signals recorded | Global & regional earthquakes, **thunderquakes** (Zhu & Stensrud 2019; Hone & Zhu 2021), mining blasts (Zhu et al. 2021), cars, footsteps, **live music events** (Shen & Zhu 2021b), seasonal environmental variation | VERIFIED |
| Calibration | Zhu et al. (2021) describe calibrating DAS to particle velocity using earthquake waveforms from a nearby broadband seismometer | VERIFIED |

---

## 7. Stanford DAS Array (SDASA / Stanford Fiber Optic Seismic Observatory) — consolidated

Three distinct Stanford deployments are on PubDAS. **All three are on PubDAS in curated form**; the GitHub repo
`eileenrmartin/FiberOpticEarthquakes` holds only small earthquake extracts, not the archives.

| | **Stanford-1** (Campus Array) | **Stanford-2** (Sandhill Road) | **Stanford-3** (dual-IU) |
|---|---|---|---|
| Location | Stanford campus, CA | Palo Alto citywide, CA | Stanford campus (same loop as S-1) |
| Interrogator | OptaSense **ODH-3** | OptaSense **ODH3** | OptaSense **ODH-4** alongside ODH-3 |
| Dates | **2 Sep 2016 – 31 Mar 2019** | **1–14 Mar 2020** (from Dec 2019 deployment) | **5–13 Oct 2017** |
| Span on PubDAS | **940 d** (longest in PubDAS) | 14 d | 6 d |
| Channels | **626** | **1,250** | (same loop as S-1) |
| Cable length | 2,500 m | **10,200 m** | 2,500 m |
| Channel spacing | 8.16 m | 8.16 m | 8.16 m |
| Gauge length | 7.14 m | 20 m | varied (tested) |
| Sample rate | **50 Hz** | **250 Hz** (native) | varied (tested) |
| Format | SEG-Y | SEG-Y | SEG-Y |
| Units | strain | strain | strain |
| **Size on PubDAS** | **18,908 GB (18.9 TB)** | **2,887 GB (2.9 TB)** | **92 GB** |
| Write rate | — | **~101 GB/day** | — |
| Deployment | Loose in air-filled ~12 cm PVC conduit; coupling by gravity/friction; 45 m spooled & wall-strapped at two manholes | Citywide extension; ch. 400–750 (Stanford Hospital→SLAC) highest SNR | ODH-4 gave **better data quality** than ODH-3 |
| Calibration | Tap tests (E. Martin et al. 2017) | Car driven at constant velocity along fibre at night (Yuan et al. 2020) | identical params to ODH-3 for first 3 days |
| Ancillary | — | — | **3 USGS broadband seismometers** in building basements within the loop |
| Access | Globus `706e304c-5def-11ec-9b5c-f9dfb1abb183` | same | same |
| Flag | VERIFIED (paper) | VERIFIED (paper) | VERIFIED (paper) |

**Total Stanford on PubDAS: 21,887 GB ≈ 21.9 TB** across the three arrays.

---

## 8. InterPACIFIC — clarification (it is **NOT** a DAS dataset)

**Confirmed: InterPACIFIC has nothing to do with distributed acoustic sensing.** The name is an acronym for
**"Inter**comparison of methods for site **PA**rameter and velocity **P**rofile **C**haracterization"
(styled *InterPACIFIC*). It is a **blind benchmarking exercise** comparing *invasive* (borehole) against
*non-invasive* (surface-wave / seismic-noise) methods for measuring shear-wave velocity profiles and Vs30 at test sites.
It predates the DAS era in seismology and used conventional geophones, borehole receivers and suspension logging.

**Primary references (VERIFIED via OpenAlex, all open access):**

| Paper | Year | DOI | OA full text |
|---|---|---|---|
| "InterPACIFIC project: Comparison of invasive and non-invasive methods for seismic site characterization. **Part I: Intra-comparison of surface wave methods**" (Soil Dynamics and Earthquake Engineering) | 2016 | `10.1016/j.soildyn.2015.12.010` | `http://porto.polito.it/2636786/1/Interpacific_part1_postprint.pdf` — **VERIFIED OA** |
| "InterPACIFIC project: Comparison of invasive and non-invasive methods for seismic site characterization. **Part II: Inter-comparison between surface-wave and borehole methods**" | 2016 | `10.1016/j.soildyn.2015.12.009` | `https://www.osti.gov/biblio/2279732` — **VERIFIED OA** |
| "**Guidelines for the good practice of surface wave analysis**: a product of the InterPACIFIC project" (Bull. Earthquake Eng.) | 2017 | `10.1007/s10518-017-0206-7` | `https://link.springer.com/content/pdf/10.1007%2Fs10518-017-0206-7.pdf` — **VERIFIED OA** |
| "The InterPACIFIC Project — A Cooperative Exercise for Assessing Reliability and Accuracy of Seismic Methods" (EAGE extended abstract) | 2014 | `10.3997/2214-4609.20140535` | `https://zenodo.org/records/14354351` — **VERIFIED** |
| "Reliability and accuracy assessment of invasive and non-invasive seismic methods for site characterization: feedback from the InterPACIFIC project" (16WCEE) | 2025 | `10.71846/16-wcee-1457` | `https://hal.science/hal-01461225` — **VERIFIED OA** |

**Is the data open?** **No — not as a downloadable waveform archive.** What is open is the *scientific product*: the
comparison results, the inverted Vs profiles from each participating team, and the practice guidelines, all published in
the open-access papers above. The raw field recordings from the three test sites were distributed **privately to the
participating teams** as part of the blind-test protocol and were never released as a public repository. **Flag:
UNVERIFIED that any raw-data archive exists; VERIFIED that no public dataset DOI is discoverable via Zenodo, DataCite or
OpenAlex.**

**Recommendation for the catalogue: file InterPACIFIC under *benchmark studies / Vs30 method comparison*, not under DAS.**
It is a useful reference for *validating* velocity-inversion workflows, which is probably why it drifted onto the DAS
list in the first place.

---

## 9. OOI Regional Cabled Array DAS — cross-check and a **major 2025–26 update**

The prior catalogue entry covers the **2021 "RAPID" experiment**. That is correct but is now only half the story: **a
second, larger OOI DAS experiment ran November 2025 – January 2026** and is separately published.

### 9.1 The 2021 experiment (OOI RCN 2001 DAS/DTS) — VERIFIED, host is LIVE

⚠️ Correction to note: the host serves **HTTP only** — `https://piweb.ooirsn.uw.edu/` **fails to connect**;
`http://piweb.ooirsn.uw.edu/das/` returns **HTTP 200** with a browsable directory index. **VERIFIED 2026-08-24.**

| Field | Value | Flag |
|---|---|---|
| Name | OOI RCN 2001 DAS/DTS experiment (a.k.a. **RAPID**) | |
| Institution | University of Washington / Ocean Observatories Initiative Regional Cabled Array | |
| Location | Two submarine cables off **Pacific City, Oregon** (Cascadia margin). North cable ~480 km toward Axial Seamount; South cable ~350 km across the continental shelf | VERIFIED |
| Dates | **1–5 November 2021** | VERIFIED |
| Interrogators | **2 × OptaSense QuantX** (north + south cables); **1 × Silixa iDASv3**; **1 × Silixa ULTIMA SM** (DTS) | VERIFIED (readme) |
| Format | **HDF5** (OptaSense), **TDMS** (Silixa DAS), **XML→CSV** (Silixa DTS) | VERIFIED |
| **Total size** | **~25.3 TB summed from the official readme volumes** (OptaSense ~18.5 T; Silixa ~6.8 T). Cross-checks against PubDAS Table 3's "RAPID 26,000 GB" | **VERIFIED (readme arithmetic)** |
| Root URL | `http://piweb.ooirsn.uw.edu/das/` | **VERIFIED (200)** |
| Readme | `http://piweb.ooirsn.uw.edu/das/processed/metadata/readme.pdf` (4 pp, version 3/23/22) | **VERIFIED (downloaded)** |
| Changes log | `http://piweb.ooirsn.uw.edu/das/processed/metadata/changes.pdf` | VERIFIED (exists) |
| Access | Plain HTTP directory browsing — **no account, no Globus, no S3** | **VERIFIED** |
| Licence | Not stated on the server | UNVERIFIED |

**Directory tree (VERIFIED by crawling):**
```
/das/data/Optasense/{NorthCable,SouthCable}/{ReceiveFiber,TransmitFiber}/<config>_<timestamp>/
/das/data/Optasense/NorthCable/TransmitFiber/ShortDuration/<config>_<timestamp>/
/das/data/Silixa/DAS/{North65km,South90km}/{acquisition,noisecheck}/
/das/data/Silixa/DTS/{Fiber001on65km,Fiber002on90km}/   (369 XML entries in Fiber001)
/das/processed/metadata/{Geometry,Optasense,Silixa}/ + readme.pdf + changes.pdf
```

**Directory names encode the acquisition parameters** (`P`=pulse rate, `GL`=gauge length, `Sp`=channel spacing,
`FS`=sample rate). Per-configuration volumes, **quoted verbatim from the readme**:

| Configuration | Volume |
|---|---:|
| `North-C1-LR-P1kHz-GL50m-Sp2m-FS200Hz_2021-11-03` (TransmitFiber) | 1.8 T |
| `North-C2-HF-P1kHz-GL30m-Sp2m-FS500Hz_2021-11-02` | 2.6 T |
| `North-C3-HF-P1kHz-GL30m-Sp2m_2021-11-01` | **5.3 T** |
| `North-C1-LR-...-ReceiveFiber_2021-11-05` | 114 G |
| `South-C1-LR-95km-P1kHz-GL50m-SP2m-FS200Hz_2021-11-01` | **4.4 T** |
| `South-C1-...-2021-11-04_part1` / `part2` | 804 G / 597 G |
| `South-C1-...-ReceiveFiber_2021-11-05` | 180 G |
| North ShortDuration (10 gauge-length/spacing tests, GL 14–200 m, Sp 1–2 m) | ~1.44 T total |
| South ShortDuration (13 tests, GL 14–200 m, FS 200/1000 Hz) | ~1.22 T total |
| `Silixa/DAS/North65km/acquisition` + noisecheck P7/P9 | 79 G + 2.0 G + 376 M |
| `Silixa/DAS/South90km/` 2021-11-01 … 11-05 | 723 G, 1.3 T, 1.3 T, **2.3 T**, 1.1 T |
| `Silixa/DTS/` | 634 M |

**Ancillary metadata (VERIFIED to exist):**
- OptaSense acquisition report: `Summary-UW-OOI-QuantX-DataAcquisition-October2021 - Issue 2.pdf`
- Jupyter notebook for reading OptaSense HDF5, by **Ethan Williams (Caltech)** — also a GitHub Gist:
  `https://gist.github.com/ethanfwilliams/c7c952220ac329db48f8ef159f0b169f`
- Silixa: `OOIdelivery.pdf`, `readTDMS.py`, `TDMS_Adv_Read.m`, `OOIDASacqnotes.xlsx`
- Cable geometry: `RCA_RPL (Segment S1 and S5).xlsx` (S1 = southern cable, S5 = northern)
- `OOI_RCA_DAS_channel_location/` — channel locations at 2 m spacing (derived by Ethan Williams)
- `OOI_RCA_DAS_channel_location_with_depth/` — same, with GMRT bathymetry depths added

### 9.2 The **2025–26 multi-span experiment** — NEW, not in the prior catalogue

This is the significant new find. Nokia Bell Labs' **multi-span DAS** uses the high-loss loopback couplers inside optical
repeaters to push DAS measurement **past the repeaters, along the entire seafloor cable** — i.e. hundreds of km rather
than the ~95 km first span.

| Field | Nokia Bell Labs Multi-span | Alcatel Subsea Networks OptoDAS |
|---|---|---|
| Zenodo record | `https://zenodo.org/records/19930402` | `https://zenodo.org/records/19930457` |
| DOI | `10.5281/zenodo.19930402` | `10.5281/zenodo.19930457` |
| Institution | Nokia Bell Labs + University of Washington | Alcatel Subsea Networks + University of Washington |
| Creators | Mazur, M.; Fontaine, N.; Krauss, Z.; Wilcock, W. | Dienstfrey, W.; Lipovsky, B.; Wilcock, W.; Krauss, Z. |
| Cables | **Both** OOI cables (north ~480 km, south ~350 km) | **First span of south cable only (~95 km)** |
| Dates | Nov 2025 – Jan 2026 (3 months) | **12 Nov 2025 – 28 Jan 2026**, outage 27 Nov – 5 Dec |
| Sample rate | 8 Hz (low-rate product) | 8 Hz (low-rate product); spatial/temporal rates varied periodically |
| **Size** | **3.9 TB** | **1.2 TB** |
| Format | **binary** (data arrays + metadata in one file) | **HDF5** (same layout as the 2024 OOI DAS experiment) |
| Licence | **CC-BY-4.0** | **CC-BY-4.0** |
| Data URL | `http://piweb.ooirsn.uw.edu/das25/data/MultiDAS/` | `http://piweb.ooirsn.uw.edu/das25/data/OptoDAS/` |
| Reader code | `https://github.com/uwfiberlab/OOI_DAS_2025` | same |
| Flag | **VERIFIED** (Zenodo record + directory listing 200) | **VERIFIED** |

⚠️ **Important quality caveat, verbatim from the OOI_DAS_2025 README:** *"the OptoDAS interrogator experienced significant
calibration issues during the experiment, leading to overall poorer data quality, especially for smaller gauge lengths."*

The Zenodo records themselves hold **only the readme PDFs** (0.1 MB and 1.0 MB); the bulk data is on the UW HTTP server.
Directory layout: `das25/data/{MultiDAS,OptoDAS}/` then sorted by year / month / date / cable — **VERIFIED by crawling.**

There is also a **2024** OOI DAS experiment with reader code at `https://github.com/uwfiberlab/OOI_DAS_2024`
("OOI DAS data examples and cable information") — **VERIFIED repo exists.**

---

## 10. Rutford Ice Stream, Antarctica — cross-check (VERIFIED, size confirmed)

| Field | Value | Flag |
|---|---|---|
| Name | Seismic noise interferometry and DAS: firn layer S-velocity structure on Rutford Ice Stream | |
| Institution | University of Bristol + **British Antarctic Survey** + Silixa | VERIFIED |
| Creators | Zhou, Wen; Butcher, Antony; **Brisbourne, Alex**; Kufner, Sofia-Katerina; Kendall, J-Michael; **Stork, Anna** | VERIFIED |
| Location | Rutford Ice Stream, West Antarctica | VERIFIED |
| Date | **14 January 2020** (7 hours continuous) | VERIFIED |
| Channels | Offsets **0 → 1,210 m in 10 m steps** (≈122 channels), filenames `...offset_XXXX.mseed` | VERIFIED |
| Sample rate | **100 Hz** | VERIFIED |
| **Size** | **4.976 GB across 122 files** (each ~40.9 MB) | **VERIFIED (measured via Zenodo API)** |
| Format | **miniSEED** (`.mseed`) | VERIFIED |
| Licence | **CC-BY-4.0** | VERIFIED |
| DOI / URL | `10.5281/zenodo.7064405` — `https://zenodo.org/records/7064405` | **VERIFIED** |
| Access | Direct HTTPS download from Zenodo, no account | VERIFIED |
| Extras | Co-located **vertical-component geophone A000** (at DAS channel offset 570 m) for the same 7 hours; **refracted P-wave travel times** from a geophone refraction survey | VERIFIED |

Related: **"Open-access data for 'Fibre-optic exploration of the cryosphere'"** — `10.5281/zenodo.12623160`,
1.642 GB / 8 files, CC-BY-4.0, `https://zenodo.org/records/12623160` — **VERIFIED**. A cryosphere-DAS compilation worth
cataloguing alongside Rutford.

---

## 11. Mount Meager, British Columbia — volcano-glacial DAS (VERIFIED)

| Field | Value | Flag |
|---|---|---|
| Name | Distributed Acoustic Sensing in Volcano-Glacial Environments — Mount Meager, British Columbia | |
| Institution | **ETH Zurich** (Sara Klaasen) | VERIFIED |
| Location | Mount Meager volcanic complex, British Columbia, Canada (on-glacier fibre) | VERIFIED |
| Dates | **October 2019** (files stamped `UTC20191007`, `UTC20191008`, …) | VERIFIED |
| **Size** | **8.848 GB across 5,420 files** | **VERIFIED (Zenodo API)** |
| Format | **HDF5** (`.h5`) + `catalog.csv` | VERIFIED |
| Processing | Linear detrend, 0.01 taper, **bandpass 5–45 Hz**, decimated to **100 Hz** | VERIFIED |
| Contents | `UTC*.h5` preprocessed high-frequency event windows; `stack*.h5` stack; `catalog.csv` catalogue of all high-frequency events | VERIFIED |
| Licence | **CC-BY-4.0** | VERIFIED |
| DOI / URL | `10.5281/zenodo.4728303` — `https://zenodo.org/records/4728303` | **VERIFIED** |
| Companion | Supplementary Information record: `10.5281/zenodo.4723795` — 0.373 GB / 7 files (event animation, cable-deployment video, notebooks) — `https://zenodo.org/records/4723795` | **VERIFIED** |

⚠️ **Caveat:** this is a **preprocessed event-window** release (bandpassed and decimated), not the raw continuous archive.

---

## 12. Chile / Valparaíso submarine DAS (VERIFIED — but small, derived products only)

Two records from Géoazur / Observatoire de la Côte d'Azur (Vernet, Rivet, Trabattoni, Baillet, van den Ende):

| Name | DOI / URL | Size | Format | Licence | Flag |
|---|---|---:|---|---|---|
| Imaging the sediment cover offshore central Chile with surface-wave dispersion and P-wave conversion using DAS | `10.5281/zenodo.15100337` — `https://zenodo.org/records/15100337` | **1.742 GB / 40 files** | csv, h5, ipynb, nc, txt | **CC-BY-4.0** | **VERIFIED** |
| Shallow crustal imaging with distributed acoustic sensing offshore central Chile | `10.5281/zenodo.18607487` — `https://zenodo.org/records/18607487` | **0.597 GB / 28 files** | csv, nc | **CC-BY-4.0** | **VERIFIED** |

Companion paper for the first: `https://doi.org/10.1029/2024JB030507` (JGR Solid Earth, 2025).
Station codes visible in the file names (`SERN`, `SERS`, `CCNN`) indicate the cable segments.

⚠️ **These are figure-reproduction packages (dispersion curves, Vs models, cross-correlations, PSDs), NOT the raw DAS
waveform archive.** The underlying Chilean submarine-cable DAS recordings do **not** appear to be openly released.
**Flag: no open raw Chile/Valparaíso DAS archive located.**

---

## 13. Whidbey Island / Seattle fibre (UW Fiber Lab) — code is open, bulk data is NOT

`https://api.github.com/orgs/uwfiberlab/repos` — **VERIFIED, 17 repositories.** This is Brad Lipovsky's group at the
University of Washington, and it is the home of the Whidbey Island and Seattle urban-fibre DAS work.

| Repo | Description (verbatim) | Last push | Relevance |
|---|---|---|---|
| `uwfiberlab/WhidbeyDAS` | "Collection of scripts for analysis of DAS data in Whidbey Island" | 2023-11-17 | **Whidbey Island — analysis scripts only, no data** |
| `bradlipovsky/whidbey-surface-waves` | MCMC inversion of dispersion curves to Vs profiles (referenced from `psf_dasnoisepy`) | — | Whidbey surface-wave inversion |
| `uwfiberlab/psf_dasnoisepy` | "software and workflows for ambient-noise analysis of the PSF DAS data. From Onyx acquisition to dispersion and monitoring analysis" | 2023-03-18 | Puget Sound fibre workflow |
| `uwfiberlab/sz4d_das_workshop` | "SZ4D Open DAS Data for Subduction Zone Environments Mini-workshop 2025" | 2025-12-26 | **Best open-DAS index for this region** |
| `uwfiberlab/OOI_DAS_2025` / `OOI_DAS_2024` | OOI readers + docs | 2026-05-07 | see §9 |
| `uwfiberlab/MTRainier` | "Collection of scripts and data files for DAS on Mt Rainier" | 2025-01-30 | Mount Rainier DAS |
| `uwfiberlab/curatedDAS` | "Building an AI-ready curated data set for DAS" | 2025-03-06 | **Watch this — an ML-ready DAS corpus in progress** |
| `uwfiberlab/FM_Denoising_DAS`, `FM_Segmentation_DAS` | Foundation-model denoiser / segmentation for DAS | 2025-06/07 | ML models |
| `uwfiberlab/alaska_event_reports` | Daily automated earthquake reports from Alaska DAS arrays (cron, QuakeML + 2-min HDF5 per array, e.g. `KKFLS.h5`) | 2024-11-20 | **Alaska DAS is operational — see §14** |
| `uwfiberlab/field_das`, `fast_beamforming`, `fiber_response`, `segDAS`, `DAS_spectra`, `das-stuff` | tooling | — | |

⚠️ **Verdict: no open bulk Whidbey Island or Seattle DAS archive was located.** The repositories publish *scripts*, and
the workshop publishes *notebooks against hosted data*, but there is no public download endpoint for the Whidbey or
Seattle (`SeaDAS-N`) waveform archives comparable to PubDAS or the OOI HTTP server. **Flag: UNVERIFIED / likely not
openly released as of 2026-08-24.**

### 13.1 The SZ4D DAS workshop — a curated index of open subduction-zone DAS

`https://github.com/uwfiberlab/sz4d_das_workshop` (**VERIFIED**), workshop page
`https://www.sz4d.org/events/agu-mini-workshop-das-subduction-zones`. It names **four** open DAS datasets by hands-on
session, which is effectively a peer-curated shortlist:

| Session | Dataset | Setting | Lead |
|---|---|---|---|
| 1–2 | **Cook Inlet, AK DAS** (`cidas`) | Subduction-zone forearc basin | Zoe Krauss / Yiyu Ni (UW) |
| 3 | **Mount Rainier, WA DAS** (`moradas`) | Subduction-zone volcano | Verónica Gaete-Elgueta (UW) |
| 4–5 | **OOI Regional Cabled Array, OR** | Accretionary prism | Ethan Williams (UCSC) / Qibin Shi (Rice) |
| 6 | **Seattle, WA urban DAS** (`seadasn`) | Urban subduction-zone setting | Manuela Köpfli (UW) |

⚠️ **Access caveat:** the workshop runs on **EarthScope GeoLab** (`https://www.earthscope.org/data/geolab/`), a hosted
JupyterHub — sign-up required, ≥7 GB RAM allocation. The Cook Inlet, Mt Rainier and Seattle data are reachable *inside
GeoLab*; **no direct public download URL was found for them.** This is the most promising route to the Seattle/Whidbey
and Alaska DAS data. **Flag: access path VERIFIED, bulk-download URLs UNVERIFIED.**

---

## 14. Iceland — Grímsvötn (NOT Reykjanes) — VERIFIED, with a serious caveat

No open **Reykjanes** DAS dataset was located. What exists for Iceland is **Grímsvötn**:

| Field | Value | Flag |
|---|---|---|
| Name | Images of DAS recordings from Grímsvötn | |
| Institution | **ETH Zurich** + **Icelandic Meteorological Office** | VERIFIED |
| Creators | Thrastarson, Sölvi; Klaasen, Sara; Cubuk-Sabuncu, Yeşim; Jónsdóttir, Kristín; Fichtner, Andreas | VERIFIED |
| Location | **Grímsvötn volcano, Vatnajökull, Iceland** — a **12 km fibre-optic cable trenched into the ice on top of the volcano** | VERIFIED |
| Date | **2021** (archive named `Grimsvotn_050721.zip` ⇒ 5 July 2021) | VERIFIED |
| **Size** | **9.364 GB** in a single ZIP | **VERIFIED (Zenodo API)** |
| Format | ⚠️ **IMAGES of seismic recordings — not waveform data** | **VERIFIED** |
| Licence | **CC-BY-4.0** | VERIFIED |
| DOI / URL | `10.5281/zenodo.5769827` — `https://zenodo.org/records/5769827` | **VERIFIED** |

⚠️ **Do not catalogue this as a usable waveform archive.** The record's own description says it "contains **images** of
seismic recordings done with Distributed Acoustic Sensing". It is useful for visual/ML-on-images work, not for signal
processing. **Flag: no open Icelandic DAS *waveform* archive located; Reykjanes DAS not found as open data.**

---

## 15. Grimsel, Bern, Athens — NEGATIVE RESULTS (searched, nothing open found)

Honest reporting: I could not find open DAS datasets for these. Recording what was searched so the next pass doesn't
repeat it.

| Target | What was searched | Outcome |
|---|---|---|
| **Grimsel Test Site** (Switzerland, underground rock lab) | Zenodo full-text + OpenAlex | **No open DAS dataset.** Relevant literature only: *"The seismo-hydromechanical behavior during deep geothermal reservoir stimulations"* (Solid Earth 2018, `10.5194/se-9-115-2018`), *"Influence of reservoir geology on seismic response during decameter-scale hydraulic stimulations in crystalline rock"* (Solid Earth 2020, `10.5194/se-11-627-2020`), *"Frequency-dependent seismic attenuation and velocity dispersion in crystalline rocks: insights from the Grimsel test site"* (GJI 2025, `10.1093/gji/ggaf188`), and a 2024 book chapter on DAS/DSS for geomechanical characterization (`10.1002/9781394179275.ch30`). All OA papers; **no data DOI**. |
| **Bern urban DAS** | Zenodo + OpenAlex | **No dataset found.** |
| **Athens urban DAS** | Zenodo + OpenAlex | **No Athens dataset.** The Greek DAS data that *does* exist is **Kefalonia Island** — see §16. |
| **Reykjanes DAS** | Zenodo + OpenAlex | **No dataset found** (Grímsvötn is what exists — §14). |
| **SISSLE** | Zenodo (1 irrelevant hit — a Coleoptera paper) + OpenAlex (0 hits) | **Not resolvable as a DAS experiment name.** Either a mis-transcription or an unpublished/internal project. **Recommend dropping from the target list unless a citation surfaces.** |

---

## 16. Alaska / Quintillion submarine — NOT openly released, but evidence it exists

No public Alaska submarine DAS archive was found. However, two independent traces show Alaskan DAS data is real and has
moved into the PubDAS orbit:

1. **PubDAS Table 2** (the Globus transfer-benchmark table) lists a transfer origin **"CTC: Cordova Telephone
   Cooperative, Alaska, USA" → University of Michigan: 8,868 files, 2.91 TB, 21.74 MB/s, 1 d 13 h 17 m 27 s.**
   **VERIFIED from the paper.** Cordova Telephone Cooperative is the Alaskan operator connected to the **Quintillion**
   subsea fibre system. So ~2.9 TB of Alaskan DAS was transferred to the PubDAS host — **but it is not among the eight
   Table 1 datasets.** It is most likely a pending addition held under embargo (the paper explicitly says "there are
   plans to add new datasets upon the conclusion of some experiments and publication embargoes").
2. **`https://github.com/uwfiberlab/alaska_event_reports`** — **VERIFIED repo.** Operational cron-driven daily
   earthquake reporting from Alaska DAS arrays, storing per-event directories with a QuakeML file (`event.qml`) and
   **2-minute HDF5 files per array** (example array code `KKFLS.h5`). This is a live monitoring pipeline, confirming
   ongoing Alaskan DAS acquisition. **No public data endpoint is exposed by the repo.**

**Flag: UNVERIFIED / not openly downloadable as of 2026-08-24. Recommend re-checking the PubDAS Globus endpoint for a
Cordova/Alaska folder — it is the single most likely near-term addition.**

**Also note the PubDAS Fairbanks dataset (§2) is Alaskan** — but it is a *terrestrial permafrost* experiment at Farmer's
Loop, not the Quintillion submarine cable.

---

## 17. HuggingFace — VERIFIED NEGATIVE (zero DAS datasets)

Queried the HuggingFace Hub API directly:

| Query | Endpoint | Result |
|---|---|---|
| `distributed acoustic sensing` | `https://huggingface.co/api/datasets?search=distributed+acoustic+sensing` | **`[]` — zero datasets** |
| `distributed acoustic sensing` | `https://huggingface.co/api/models?search=distributed+acoustic+sensing` | **`[]` — zero models** |
| `DAS` | `https://huggingface.co/api/datasets?search=DAS&limit=25` | 25 hits, **all unrelated name collisions** (`daspartho/*`, `dasago78/*`, `DasanCallDial`, `roots_*_book_dash_books`, …) |
| `fiber optic` | `https://huggingface.co/api/datasets?search=fiber+optic` | 3 hits, all unrelated (`fiber-optic-faults`, `fiber-optic-drones`) |
| `earthquake` | `https://huggingface.co/api/datasets?search=earthquake&limit=25` | 25 hits, **all catalogue/tabular/news data — no DAS, no waveform arrays** |

> **Conclusion: there is no DAS data on HuggingFace.** DAS remains entirely in the Globus / S3 / Zenodo / institutional-HTTP
> world. If an AI-ready DAS corpus is wanted, `https://github.com/uwfiberlab/curatedDAS` ("Building an AI-ready curated
> data set for DAS") is the effort to track.

---

## 18. Zenodo DAS catalogue — systematic sweep

**Method (VERIFIED, reproducible):** `https://zenodo.org/api/records?q=%22distributed%20acoustic%20sensing%22&size=25&page=N`
for N = 1…10. Zenodo caps anonymous page size at 25 ("Page size cannot be greater than 25. Please use authenticated
requests to increase the limit to 100"). **Total hits: 230. Records parsed: 225. Records ≥30 MB: 123.**

### 18.1 Largest open DAS records on Zenodo (all sizes computed from the API file manifests)

| Size (GB) | Name | DOI | Licence | Formats | URL | Flag |
|---:|---|---|---|---|---|---|
| **102.168** | DASGAS borehole data | `10.5281/zenodo.21193610` | CC-BY-4.0 | zip | `https://zenodo.org/records/21193610` | VERIFIED |
| **83.154** | Fault-Controlled Thaw in Degrading Permafrost on the Qinghai–Tibet Plateau Resolved by Traffic-Enhanced DAS | `10.5281/zenodo.19369569` | CC-BY-4.0 | mat, txt, zip | `https://zenodo.org/records/19369569` | VERIFIED |
| **72.556** | Calving-driven fjord dynamics resolved by seafloor fibre sensing | `10.5281/zenodo.15353304` | CC-BY-4.0 | zip | `https://zenodo.org/records/15353304` | VERIFIED |
| **63.507** | **Trondheimsfjord DAS** — Tracking ships with submarine cables | `10.5281/zenodo.18851481` | CC-BY-4.0 | 7z | `https://zenodo.org/records/18851481` | VERIFIED |
| **48.638** | NCF data — atmosphere-groundwater modulated seismic velocity variations by DAS | `10.5281/zenodo.21275599` | CC-BY-4.0 | dat, py, tar, xlsx | `https://zenodo.org/records/21275599` | VERIFIED |
| **48.557 / 46.604 / 44.275** | DASGAS surface data parts 1 / 3 / 2 | `…21208202` / `…21208335` / `…21208303` | CC-BY-4.0 | zip | `https://zenodo.org/records/21208202` etc. | VERIFIED |
| **44.272 / 41.903** | Self-Supervised Coherence-Based Denoising on Cryoseismological DAS (two versions) | `10.5281/zenodo.13868934` / `…14998653` | CC-BY-4.0 | zip | `https://zenodo.org/records/13868934` | VERIFIED |
| **37.625** | **DAS4Whale** — Svalbard DAS for baleen whale monitoring | `10.5281/zenodo.5823343` | CC-BY-4.0 | mat (11 files) | `https://zenodo.org/records/5823343` | VERIFIED |
| **37.164** | Rhonegletscher DAS Cryoseismic Training Dataset, Features and Catalog | `10.5281/zenodo.17555409` | CC-BY-4.0 | md, zip | `https://zenodo.org/records/17555409` | VERIFIED |
| **36.365** | DAS Earthquake Waveforms Recorded During the **NEREIDS** Experiment | `10.5281/zenodo.20614142` | CC-BY-4.0 | png, zip | `https://zenodo.org/records/20614142` | VERIFIED |
| **30.150** | Enhancing On-Site Earthquake Early Warning with DAS | `10.5281/zenodo.15171557` | **CC0** | gz, txt | `https://zenodo.org/records/15171557` | VERIFIED |
| **25.188** | Tailings dam monitoring — coda wave interferometry + DAS | `10.5281/zenodo.11069095` | CC-BY-4.0 | **h5** | `https://zenodo.org/records/11069095` | VERIFIED |
| **23.422** | Seismic Slope Instability Monitoring: Fibre-Optic (Seismica) | `10.5281/zenodo.17095556` | CC-BY-4.0 | txt, zip | `https://zenodo.org/records/17095556` | VERIFIED |
| **22.224** | DAS at Milun Campus, Donghua University (2024 Hualien earthquake) | `10.5281/zenodo.13318497` | CC-BY-4.0 | pdf, zip | `https://zenodo.org/records/13318497` | VERIFIED |
| **21.870** | Ocean observations, 29-km submarine cable, northern South China Sea | `10.5281/zenodo.15508784` | CC-BY-4.0 | mat, txt, zip | `https://zenodo.org/records/15508784` | VERIFIED |
| **21.421** | Magnitude Estimation of Low-yield Mining Blasts Using DAS | `10.5281/zenodo.17573175` | CC-BY-4.0 | zip | `https://zenodo.org/records/17573175` | VERIFIED |
| **21.080** | Harnessing converted phases for rapid magnitude estimation / EEW with DAS | `10.5281/zenodo.17422886` | CC-BY-4.0 | **csv, nc** (75 files) | `https://zenodo.org/records/17422886` | VERIFIED |
| **20.442** | Secondary microseisms — joint DAS observations + full waveform modelling | `10.5281/zenodo.20668434` | CC-BY-4.0 | txt, zip | `https://zenodo.org/records/20668434` | VERIFIED |
| **20.133** | Deformation-rate DAS: filtering and coupling considerations | `10.5061/dryad.ksn02v756` | **CC0** | zip | `https://zenodo.org/records/5728129` | VERIFIED |
| **19.342** | DAS + hydrophone arrays for locating underwater sounds | `10.5281/zenodo.7886409` | CC-BY-4.0 | **h5**, pdf, zip | `https://zenodo.org/records/7886409` | VERIFIED |
| **18.588** | Multiconfiguration **borehole** DAS at the **PITOP** test site | `10.5281/zenodo.19001579` | CC-BY-4.0 | 7z | `https://zenodo.org/records/19001579` | VERIFIED |
| **15.741** | DAS Phase Pick Quality for Operational Earthquake Monitoring | `10.5281/zenodo.17983113` | CC-BY-4.0 | csv, zip | `https://zenodo.org/records/17983113` | VERIFIED |
| **14.116** | **Marlinks-NS** — vessel detection, Zeebrugge North Sea | `10.5281/zenodo.15611778` | CC-BY-4.0 | **h5** | `https://zenodo.org/records/15611778` | VERIFIED |
| **14.033** | DAS Ambient-Noise Processing Using Existing Telecom Fibre | `10.5281/zenodo.21828754` | CC-BY-4.0 | zip | `https://zenodo.org/records/21828754` | VERIFIED |
| **12.674** | DAS data products from **Mt. Zugspitze** (German/Austrian Alps) | `10.5281/zenodo.19226183` | CC-BY-4.0 | py, zip | `https://zenodo.org/records/19226183` | VERIFIED |
| **9.364** | **Grímsvötn** DAS recordings (images) | `10.5281/zenodo.5769827` | CC-BY-4.0 | zip | `https://zenodo.org/records/5769827` | VERIFIED (§14) |
| **8.848** | **Mount Meager** volcano-glacial DAS | `10.5281/zenodo.4728303` | CC-BY-4.0 | **h5** (5,420 files) | `https://zenodo.org/records/4728303` | VERIFIED (§11) |
| **7.489** | Selected Original and Compressed Data from the **Taiwan MiDAS** Project | `10.5281/zenodo.15241981` | CC-BY-4.0 | **h5**, zip | `https://zenodo.org/records/15241981` | VERIFIED |
| **6.564** | **RNN-DAS** — volcano-tectonic event detection | `10.5281/zenodo.15105596` | CC-BY-4.0 | zip | `https://zenodo.org/records/15105596` | VERIFIED |
| **6.232** | Cross-spectra, S-wave structure off **Sanriku, Japan** | `10.5281/zenodo.5904941` | CC-BY-4.0 | zip | `https://zenodo.org/records/5904941` | VERIFIED |
| **4.976** | **Rutford Ice Stream, Antarctica** | `10.5281/zenodo.7064405` | CC-BY-4.0 | **mseed** | `https://zenodo.org/records/7064405` | VERIFIED (§10) |
| **4.647** | Source Parameters from DAS, Central Shikoku, Japan | `10.5281/zenodo.18613984` | CC-BY-4.0 | dat, gz | `https://zenodo.org/records/18613984` | VERIFIED |
| **3.823** | **DAS Urban Mobility Patterns Database** (Univ. Granada) | `10.5281/zenodo.8068609` | CC-BY-4.0 | rar→**MINIDAS/HDF5** | `https://zenodo.org/records/8068608` | VERIFIED |
| **2.725** | Shallow tremor + DAS data off **Cape Muroto**, SW Japan | `10.5281/zenodo.7935235` | CC-BY-4.0 | txt, zip | `https://zenodo.org/records/7935235` | VERIFIED |
| **1.742** | Sediment cover offshore **central Chile** | `10.5281/zenodo.15100337` | CC-BY-4.0 | csv, h5, nc | `https://zenodo.org/records/15100337` | VERIFIED (§12) |
| **1.642** | **Fibre-optic exploration of the cryosphere** (8-dataset compilation) | `10.5281/zenodo.12623160` | CC-BY-4.0 | zip | `https://zenodo.org/records/12623160` | VERIFIED (§18.3) |
| **1.567** | DAS at **Ruapehu Volcano**, New Zealand (2023) | `10.5281/zenodo.20789299` | CC-BY-4.0 | zip (27 files) | `https://zenodo.org/records/20789299` | VERIFIED |
| **1.537** | Urban **rat** dynamics via dark-fibre DAS | `10.5281/zenodo.17175393` | CC-BY-4.0 | md, zip | `https://zenodo.org/records/17175393` | VERIFIED |
| **1.159** | Nearshore ocean currents from submarine-cable DAS | `10.5281/zenodo.13133835` | CC-BY-4.0 | npy, npz | `https://zenodo.org/records/13133835` | VERIFIED |
| **0.597** | Shallow crustal imaging offshore **central Chile** | `10.5281/zenodo.18607487` | CC-BY-4.0 | csv, nc | `https://zenodo.org/records/18607487` | VERIFIED (§12) |
| **0.362** | **Kefalonia Island DAS** — codes + catalogue | `10.5281/zenodo.20558686` | CC-BY-4.0 | zip | `https://zenodo.org/records/20558686` | VERIFIED (§18.4) |

⚠️ **Read the format column carefully.** Many of these are **figure-reproduction packages** (cross-correlations, Vs
models, dispersion curves) rather than raw waveforms. The ones that genuinely ship waveform-like arrays are flagged with
**h5 / mseed / MINIDAS / nc** above.

### 18.2 Two notable "processed only" traps

- **Marlinks-NS** (`10.5281/zenodo.15611778`, 14.116 GB, CC-BY-4.0): 10 days of DAS over a **2,553 m segment of a 28 km
  ocean-bottom cable offshore Zeebrugge, Belgium**, 16–25 June 2023, **OptoDAS interrogator, 3,125 Hz, gauge length and
  channel spacing both 10.21 m**. But — verbatim — *"The original DAS time-series signals are **not** publicly
  distributed because of data-owner confidentiality and critical-infrastructure restrictions."* What ships is
  **250×100×250 spectral-energy feature matrices** per 10 s window plus AIS vessel labels. Excellent for ML vessel
  detection, useless for seismology.
- **DAS Urban Mobility Pattern Database**: the original record `10.5281/zenodo.8046236` is marked
  **"DISCONTINUED!!!!"** — **use `10.5281/zenodo.8068609` (`https://zenodo.org/records/8068608`, 3.823 GB) instead.**
  Notable for using the **IRIS/DAS-RCN MINIDAS HDF5 format** (`https://github.com/DAS-RCN/RCN_DASformat`).

### 18.3 "Fibre-optic exploration of the cryosphere" — an 8-dataset cryo-DAS bundle

`10.5281/zenodo.12623160` (1.642 GB, 8 ZIPs, CC-BY-4.0). Creators: Fichtner, A.; Walter, F.; Brisbourne, A.; Booth, A.;
Kendall, M.; Hudson, T. (ETH Zurich / WSL / BAS / Leeds). **VERIFIED.** Contents:

| # | Sub-dataset | Content |
|---|---|---|
| 1 | Store Glacier (Booth et al., 2020) | Active-shot VSP |
| 2 | Rhone Glacier (Walter et al., 2020) | Basal strike-slip + surface crevassing events |
| 3 | **Rutford Ice Stream** (Hudson et al., 2021) — 188.9 MB | Ice quakes |
| 4 | EastGRIP cascades (Fichtner et al., 2025) — 779.9 MB | Englacial ice-quake cascades from borehole |
| 5 | Vallée de la Sionne (Paitz et al., 2023) | **Snow avalanches** |
| 6 | EastGRIP touch down (Fichtner et al., 2023) — 68.9 MB | Airplane landing |
| 7 | Gorner Glacier (Hudson et al., 2025) | Crevassing events |
| 8 | Skytrain VSP (Brisbourne et al., 2021) — 72.1 MB | Active-source VSP, Skytrain Ice Rise |

This is the single most efficient cryosphere-DAS starting point — eight settings, one download, CC-BY.

---

### 18.4 Kefalonia Island, Greece — the real "Greek urban/island DAS"

| Field | Value | Flag |
|---|---|---|
| Name | Earthquake Catalog and Continuous Waveforms From a Two-week DAS Experiment On Kefalonia Island, Greece | |
| Institution | **Ruhr University Bochum** (Bocchini, G. M.; Roth, M.; Harrington, R. M.) | VERIFIED |
| Location | Kefalonia Island, Greece | VERIFIED |
| Dates | **23:00 on 1 Aug 2024 → 23:00 on 15 Aug 2024** (two weeks) | VERIFIED |
| Catalogue | **356 earthquakes** with absolute locations, from DAS + seismic stations | VERIFIED |
| Codes/support pkg | **0.362 GB**, `10.5281/zenodo.20558686`, CC-BY-4.0 — cable geometry (`das_channels.csv` with coordinates + segment ids), catalogues, P/S picks, cross-correlation tables | **VERIFIED** |
| **Continuous waveforms** | Separate repository: **`10.60517/cv43p1601`** → resolves (302, **VERIFIED**) to `https://reseed.ruhr-uni-bochum.de/concern/datasets/da6dedc6-2fa8-454c-a6f7-ad05a84d1fee` | **URL VERIFIED via DOI redirect; page itself UNREACHABLE from this network (connection reset) — size/format UNVERIFIED** |
| Mirror | `https://gitlab.ruhr-uni-bochum.de/bocchgxw/das-kefalonia` | UNVERIFIED |
| Paper | Bocchini et al., in review at **Earth System Science Data (ESSD)** | VERIFIED |

**This is a genuinely open two-week continuous DAS waveform release** and is a strong candidate for the catalogue —
worth re-verifying the RESEED endpoint from a different network.

---

## 19. Summary of what changed vs. the prior catalogue

| Item | Prior belief | Corrected finding |
|---|---|---|
| PubDAS vs PoroTomo | Assumed conflict between 90 TB and 172.15 TB | **No conflict — disjoint archives. PubDAS hosts zero PoroTomo bytes.** |
| PoroTomo size | 172.15 TB | **172.15 *TiB* (GDR mislabels binary units). Measured live: 186.86 decimal TB / 169.94 TiB, 224,205 objects.** |
| PoroTomo uniqueness | Implicitly one dataset | **~3.5× format redundancy — SEG-Y + H5 + H5-standardized. Unique content ≈ 52 TB.** |
| PubDAS total | ~90 TB | **~90 TB is the authors' headline; the enumerated Table 1 holdings sum to 76.6 TB.** |
| PubDAS web front-end | Assumed live | **DEAD (`piweb.ess.washington.edu` fails DNS). Globus UUID is the only access path.** |
| Ridgecrest DAS | Size unknown | **Measured: 4.09 TB, 911 objects, 909 hourly SEG-Y, 1,250 channels @ 250 Hz.** |
| OOI RCA DAS | 2021 RAPID only, ~26 TB | **Confirmed ~25.3 TB; plus a NEW 2025–26 multi-span experiment (Nokia 3.9 TB + OptoDAS 1.2 TB) not previously catalogued.** |
| DAS-RCN | "~10 entries, zero dead links" | **10 entries enumerated. But `das-rcn.org` itself is dead, and the list carries no sizes.** |
| InterPACIFIC | Ambiguous | **Not DAS at all — a blind Vs-method comparison. No open raw data.** |
| HuggingFace | Unknown | **VERIFIED ZERO DAS datasets and zero DAS models.** |
| Whidbey / Seattle / Alaska | Expected open data | **Code is open; bulk data is not. Access likely via EarthScope GeoLab.** |

---

*(Final save — 2026-08-24. Sections 1–19 complete.)*
