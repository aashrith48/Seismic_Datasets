# Named Open Seismic Field Volumes — Global (excluding New Zealand & Australia)

> New Zealand and Australia are covered separately in `field-volumes-nz-au.md`.
> This document covers the rest of the world.
>
> **This file replaces an earlier unverified placeholder.** Every row carries a flag:
>
> * `[V]` — URL fetched, and/or byte count read from an HTTP `Content-Length` header or an
>   authoritative repository API field, during this research pass.
> * `[P]` — partially verified: authoritative page reached, size as published by the portal
>   rather than measured.
> * `[U]` — unverified. Do not trust the size, and re-check the URL before using it.
>
> **Never cite a URL from this file that is not marked `[V]` or `[P]` without re-checking.**

---

## How the sizes here were obtained

* HTTP `Content-Length` via `curl -sI <url>` for every direct-file entry.
* TerraNubis publishes both a *download* (zip) size and an *uncompressed* size; both are
  recorded, because the difference decides your disk budget. TerraNubis download URLs sit
  behind a session gate (`.../download/X.zip/2` returns a 96-byte stub to `curl`), so the
  portal-published figures are used rather than measured ones.
* MGDS sizes come from its own `FileServer` API fields `data_file_size` (bytes) and
  `uncompressed_file_size`.
* S3-hosted corpora were enumerated with `?list-type=2` where listing is permitted.

### Host quirks worth knowing before you script anything

| Host | Behaviour | Workaround |
|---|---|---|
| `wiki.seg.org` | Cloudflare-blocked to automation — 403 to WebFetch, to `curl` with a browser UA, **and to `api.php?action=parse`** | Read it through the Wayback Machine: `http://web.archive.org/web/2024/https://wiki.seg.org/wiki/<Page>`. That is how the SEG catalogue below was recovered. |
| `open.source.geoscience` S3 | **Bucket listing denied** — `https://s3.amazonaws.com/open.source.geoscience/?list-type=2` → `<Error><Code>AccessDenied</Code>`. Objects themselves are public. | Keys must come from documentation. Full recovered key list is in the Aggregators section. |
| `osdu-seismic-test-data` S3 | **Listing permitted, no credentials needed** | `https://s3.amazonaws.com/osdu-seismic-test-data/?list-type=2&max-keys=1000` + continuation tokens. Fully enumerated below. |
| `dataunderground.org` | **DEAD** — DNS does not resolve (`getaddrinfo ENOTFOUND`) | None. Content survives only in Wayback and search indexes. |
| `www.rmotc.doe.gov` | **DEAD** (SEG Wiki itself says so) | Teapot Dome now lives on two public S3 buckets — see below. |
| `www.opendtect.org/osr/...` | Legacy dGB Open Seismic Repository links now **redirect to TerraNubis** | Use the TerraNubis `datainfo` pages. |
| `marine-geo.org` `FileDownloadServer` | Documented in the WADL and returned by the API, but **301s to `api.marine-geo.org` then 404s** (verified on three uids) | Use the `download.php` terms-accept flow described in the MGDS section. |
| `geofizyka.pl/2D_Land_vibro_data_2ms.tgz` | **404** | Use the `ftps.geofizyka.pl` weblink (host is up; the weblink token was not exercised). |

---

## Netherlands

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **F3 Demo 2023** (F3 Block) | Dutch North Sea, block F3. Acq. 1987, value-add 2023. **386.92 km²**; inline 100–750 step 1, crossline 300–1250 step 1, Z 0–1.848 s at 4 ms, 25 m × 25 m bins | 3D post-stack + **10 lines of 2D**; 15 3D volumes total: original seismic, two steering cubes, dip-steered median filter, ChimneyCube, 2 acoustic-impedance cubes, porosity cube, gamma cube, 4 similarity/fault-enhancement volumes, **interval and RMS velocity models** | **4 vertical wells** F02-1, F03-2, F03-4, F06-1, each with density, sonic, gamma ray, porosity, P-impedance (abs + rel), Vp, Vp_BLI, Vs_BLI, Density_BLI, litholog; **8 interpreted horizons** (FS4, MFS4, FS6, Top_Foresets, Truncation, FS7, FS8, Shallow) | **4.5 GB download / 7.6 GB uncompressed** | Creative Commons 3.0 (CC BY-SA); acknowledge dGB Earth Sciences via TerraNubis. Original seismic NAM, source NLOG. | `https://terranubis.com/datainfo/F3-Demo-2023` → `https://terranubis.com/download/F3_Demo_2023.zip/2` | The world's default open 3D. Sequence stratigraphy (textbook downlap/toplap/onlap/truncation), channels, bright spots from biogenic gas, gas chimneys, polygonal dewatering faults, Zechstein salt. OpendTect Pro and commercial plugins run on it **without licence keys**. | [V] |
| 2 | **F3 Block — legacy dGB OSR packagings** | as above | "F3 Complete" and "F3 Seismic Only" | wells + horizons in Complete only | **~4 GB** (Complete) / **494 MB** (Seismic Only) — sizes are embedded in the legacy URL names | CC BY-SA | `http://www.opendtect.org/osr/Main/NetherlandsOffshoreF3BlockComplete4GB` and `.../NetherlandsOffshoreF3BlockSeismicOnly494MB` — **both now redirect to the TerraNubis F3 Demo 2023 page** (verified 200 + redirect) | The 494 MB "Seismic Only" figure is the useful fact: an F3 cube alone is under half a gigabyte. Export to SEG-Y from OpendTect. | [P] |
| 3 | **F3 full survey / original SEG-Y** | as above | the full un-cropped 3D survey as released by the Dutch state | navigation | not published as a figure | Free, no registration | via the NLOG interactive map / data centre, `https://www.nlog.nl/en/seismic-data` | Use when the demo subset's 386.92 km² / 1.848 s window is too small. | [U] |
| 4 | **Delft** | West Netherlands Basin, 84.6 km², onshore | 3D post-stack (acq. 1985, reprocessed 2011) + **Thinned Fault Likelihood** volume + steering cube with planarity | wells with logs; interpreted horizons | **2.8 GB download / 5.4 GB uncompressed** | CC BY-SA 3.0 (dGB value-add); original from NAM via NLOG | `https://terranubis.com/datainfo/Delft` → `https://terranubis.com/download/Delft.zip/2` | Onshore geothermal and fault imaging. Small enough to iterate on. | [V] |
| 5 | **NLOG released Dutch surveys** (whole national archive) | Dutch on- and offshore | 2D + 3D **post-stack** SEG-Y | navigation; well data via the same portal | archive-scale (tens of TB) | Free, **no registration**, for released post-stack | `https://www.nlog.nl/en/seismic-data` — interactive map or data centre | Largest no-registration national archive in Europe. **Important split: post-stack is genuinely free; pre-stack 3D is a fee-bearing TNO retrieval request** (see the "Fees TNO Seismic Data Requests" PDF on that page). | [V] |
| 6 | **SCAN programme regional 2D** (*Seismische Campagne Aardwarmte Nederland*; TNO + EBN, since 2018) | onshore Netherlands, geothermal screening | 2D, **newly acquired long-offset** (offsets to 29 km) + reprocessed legacy. Includes **PreSDM/RTM** products. | processed sections, **velocity models**, processing reports and appendices | **73 newly acquired lines (2019–2025)** + **4 "widelines"** + **6 cross-spread pseudo-3D products** + **11 reprocessing packages covering ~6,700 km** of 1970s–90s data. Test line Utrecht–Almere: 1,355 shots × 5,817 channels. **Measured: 98 unique `.zip` downloads on the page; 97 returned a size; total 234,647,068,060 bytes = 234.65 GB.** Largest single file `SCAN002_PreSDM_RTM.zip` = 12,633,310,523 B (11.8 GiB). | Free via NLOG; **no explicit licence text is published on the page** | `https://www.nlog.nl/en/scan-2d-seismic-data`. Direct pattern: `https://www.nlog.nl/sites/default/files/big_files/<NAME>.zip`, e.g. `L2EBN2019ASCAN001.zip`, `L2EBN2021ASCAN020.zip` (8.26 GB), `GTO-19-C032-01_Zeeland_NAM.zip` (11.59 GB), `Lines11-46_Processingreport+appendices.zip` (6.63 GB). Lines 68–73 are reached via the interactive map instead. | Genuinely *new* state-funded 2D released open, with long offsets and released velocity models — unusually good for velocity/FWI work. Raw field data is a fee-bearing NLOG Servicedesk request. | [V] |
| 7 | **Groningen 3D** | Groningen gas field, onshore NL | 3D post-stack | wells via NLOG | not measured | Free via NLOG | via `https://www.nlog.nl/en/seismic-data` interactive map | Pairs with KNMI induced-seismicity waveforms — the best open reservoir-scale induced-seismicity setting. | [U] |

---

## Norway and the North Sea

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 8 | **Volve — full release** | Norwegian North Sea, block 15/9 (produced 2008–2016) | 3D + 4D, **pre- and post-stack**, VSP | **~40,000 files**: petrophysical and drilling logs, production data, well and completion-string design, geology/stratigraphy, **static and dynamic (Eclipse) models**, surface and grid data, reports | **~5 TB total**, ~40,000 files | **Equinor Open Data Licence** — academic institutions, students and researchers may use it for study, research and development with no further written permission | `https://www.equinor.com/energy/volve-data-sharing` → "Access open data". Historically an Azure Blob container pulled with Azure Storage Explorer; the page now also routes via **Databricks Marketplace**. User guide: `https://equinoropendata.blob.core.windows.net/userguides/Equinor%20open%20data%20-%20User%20Guide.pdf` | The most complete open field-lifecycle dataset in existence, and the only realistic basis for an end-to-end integrated demo. | [V] |
| 9 | **Volve seismic subset — via the OSDU open test-data S3 bucket** | as above | **This is the practical way to get Volve seismic without Azure.** Anonymous HTTPS, listable, exact sizes. | see the detailed table in the Aggregators section | **volve/ prefix total 22,637,514,545 B (22.64 GB), 109 objects**, of which `volve/seismic` = **22,413,469,774 B (22.41 GB) across 49 files**. The prize: `volve/seismic/st0202/prestacks/ST0202R08_PZ_PrSDM_CIP_gathers_in_PP_Time.segy` = **20,311,496,528 B (18.92 GiB) of pre-stack CIP gathers** | Apache 2.0 on the OSDU repo tooling; the underlying Volve data remains under the **Equinor Open Data Licence** | Repo `https://community.opengroup.org/osdu/platform/data-flow/data-loading/open-test-data` · bucket `s3://osdu-seismic-test-data/` (`aws s3 ls s3://osdu-seismic-test-data/ --no-sign-request`) · plain HTTPS also works: `https://s3.amazonaws.com/osdu-seismic-test-data/<key>` (HEAD verified `200`, `Content-Length: 20311496528`) | **The single best open pre-stack 3D that you can `curl` in one command.** Gathers + PSDM stacks + a TTI velocity volume + LAS logs + horizons + faults + checkshots, all in one bucket. | [V] |
| 10 | **Sleipner 4D Seismic Dataset** | Norwegian North Sea, Utsira Fm | **4D** time-lapse post-stack, **12 processed cubes across 7 vintages, 1994–2010**, baseline pre-injection | pairs with #11 | 1994: 94p01 2.2 GiB, 94p07 1.5 GiB, 94p08 2 GiB, 94p10 2 GiB · 1999: 99p01 2.2 GiB · 2001: 01p01 2.2 GiB, 01p07 1.5 GiB · 2004: 04p07 1.5 GiB · 2006: 06p07 1.5 GiB · 2008: 08p08 2 GiB · 2010: 10p10 2 GiB, 10p11 3.2 GiB. **Total ≈ 24.6 GiB.** | **Sleipner CO2 Reference Dataset Licence** (open access, licence acceptance required) | `https://co2datashare.org/dataset/sleipner-4d-seismic-dataset` — individual ZIP per vintage/processing | The canonical open CCS time-lapse volume — 16 years of CO2 plume growth. ~20,000 downloads since Jan 2020. The reference dataset for 4D CO2 monitoring. | [V] |
| 11 | **Sleipner 2019 Benchmark Model** | as above | static reference/benchmark model (not seismic) | model grids | ZIP | Sleipner CO2 Reference Dataset Licence | `https://co2datashare.org/dataset` | The model half of the Sleipner pair — forward modelling and inversion benchmarks against #10. | [V] |
| 12 | **Smeaheia Dataset** | Horda Platform, Norwegian North Sea | **Seismic 3D surveys (TNE01 and GN1101) 1.7 GiB** and **Seismic 2D lines (BPN88 1988, GSB-85R97 1985) 2.5 GiB** — 4.2 GiB of seismic in total | wells 32/2-1 and 32/4-1 logs (1.6 MiB); geomechanical stress/temperature/pressure (329.6 KiB); Triassic–Jurassic fault sticks (552.5 KiB); depth-converted surfaces (15.2 MiB); reports incl. Troll Kystnær subsurface report (16.9 MiB); extracted interval velocity maps (21.9 MiB); well reports (31.2 MiB); Equinor + other simulation grids (49.6 MiB); pre-feasibility horizons (203.7 MiB) — **11 components** | **~4.4 GiB total** | **Smeaheia Dataset Licence** (open access) | `https://co2datashare.org/dataset/smeaheia-dataset` | CO2 storage-site characterisation with a genuinely complete ancillary suite; the Northern Lights alternative site. ~20,300 downloads since Feb 2021. | [V] |
| 13 | **The Johansen Dataset** | offshore Norway | geological model of a candidate CO2 store | model | ZIP | listed under the Sleipner CO2 Reference Dataset Licence | `https://co2datashare.org/dataset` | Classic CO2 reservoir-simulation benchmark. | [V] |
| 14 | **Northern Lights — Eos well 31/5-7 rock mechanics** (2 datasets: core; thermo-mechanical response) | Horda Platform | **not seismic** — rock-mechanical lab testing from a CCS exploration well | core test results | ZIP | Northern Lights Eos 31/5-7 Rock Mechanical Data Licence | `https://co2datashare.org/dataset` | Rock-physics calibration for CCS seismic modelling. **There is no Northern Lights *seismic* volume on CO2DataShare** — treat "Northern Lights seismic" claims with suspicion. | [V] |
| 15 | **Svelvik CO2 Field Lab cross-well data 2019** | Svelvik ridge, Norway | **cross-well seismic** plus other CO2 monitoring methods | monitoring suite | ZIP | Svelvik 2019 Dataset Licence | `https://co2datashare.org/dataset` | Shallow controlled-injection cross-well seismic — rare open cross-well data. | [V] |
| 16 | **Norne field** (E-segment, and whole field) | Norwegian Sea | **4D**: 2001 base + 2003 and 2004 monitors, **full / mid / near / far offset** stacks on inline and crossline sections | **Eclipse reservoir simulation model**; all E-segment wells with logs; per-well oil/water/gas rates; production history to 2004; interpreted horizons incl. **oil–water contacts for 2001/2003/2004**; faults | not published as a single figure | **Attribution, non-commercial** (NTNU licence page) | Case 1 (1997–2004, E-segment) `http://www.ipt.ntnu.no/~norne/wiki/doku.php?id=english:nornebenchmarkcase1` · Case 2 (1997–2006, whole field) `...:nornebenchmarkcase2` · Licence `...:english:license` | The best open **4D + history-matching** pairing anywhere: time-lapse seismic *and* the matching simulation model. Statoil/Equinor with ENI and Petoro; hosted by NTNU. | [P] |
| 17 | **Diskos / Sodir released Norwegian cubes** | Norwegian Continental Shelf | 2D/3D post-stack, some pre-stack | velocities, navigation | archive-scale | free to access; media/handling cost may apply | `https://www.sodir.no/en/diskos/seismic/` | Europe's largest national archive. Named cubes must be picked off the Diskos map — **no per-cube inventory was verified here**. | [U] |

---

## United Kingdom

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 18 | **OGA Mid North Sea High (MNSH) 2016** | UK North Sea, Mid North Sea High | 2D — **260 lines** | **98 wells** with logs and checkshots; interpreted horizons (water bottom, Chalk, Permian); **18 fault stick sets**; gravity and magnetics | **11 GB download / 12 GB uncompressed** | **Open Government Licence v3.0** | `https://terranubis.com/datainfo/OGA-MNSH` → `https://terranubis.com/download/MNSH_OGA_2016_v1.zip/2` | Released to stimulate the UK 29th Offshore Licensing Round. Best open *2D + many wells* package for regional interpretation and well ties. | [V] |
| 19 | **OGA Rockall Trough 2016** | UK Atlantic Margin | 2D — 77 lines with **near / mid / far / ultra-far angle stacks**, 10 reprocessed legacy lines, 71 further legacy lines | **20 wells** with logs and checkshots; 4 horizons; 2 fault stick sets; gravity and magnetics | **11 GB download / 12 GB uncompressed**; individual angle stacks are separate downloads of **3.9–6 GB each** | **Open Government Licence v3.0** | `https://terranubis.com/datainfo/OGA-Rockall-Trough` → `https://terranubis.com/download/Rockall_Trough_OGA_2016_v1.zip/2` | One of very few open datasets shipping **angle stacks** — AVO/AVA without needing pre-stack. | [V] |
| 20 | **OGA/NSTA South-West of Britain & East Shetland Platform 2D** | UK offshore | 2D | wells | not measured | Open Government Licence v3.0 | catalogued on SEG Wiki; primary host UKOGL / `https://www.ukoilandgasdata.com/` | Companion release to #18/#19. | [U] |

---

## Canada

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 21 | **Penobscot 3D** (TerraNubis packaging) | Scotian Shelf, offshore Nova Scotia | 3D **and** 2D, PSTM stack **plus pre-stack**: NMO-migrated gathers and **conditioned angle gathers** | **stacking velocities**; wells **B-41** and **L-30** with logs, markers and time-depth models; 5 interpreted horizons; dip-steering volumes | **8.7 GB download / 12.4 GB uncompressed** | CC BY-SA 3.0 | `https://terranubis.com/datainfo/Penobscot` | The best F3 alternative, and strictly better than F3 for pre-stack — one of very few open 3Ds shipping migrated gathers *and* angle gathers *and* velocities *and* wells. | [V] |
| 22 | **Penobscot 3D — full pre-stack (legacy dGB OSR)** | as above | 3D **pre-stack** | as above | **101 GB** | CC BY-SA | `http://www.opendtect.org/osr/Main/PENOBSCOT3DSABLEISLAND` (legacy OSR links now redirect to TerraNubis) | The full pre-stack volume, if the 8.7 GB conditioned subset is not enough. | [P] |
| 23 | **Penobscot Interpretation Dataset** (Baroni, Silva, Ferreira, Chevitarese, Szwarcman & Vital Brazil, 2020, v3.0.0) | as above | **ML labels** derived from Penobscot; 7 facies classes | `dataset.h5` **2.3 GB** (>100,000 labelled images); `horizons.zip` **36.2 MB** (7 reinterpreted horizons); `how-to-read.ipynb` 633.3 kB; `penobscot-examples.png` 10.6 MB; `dataset-log.txt` 1.9 kB. Splits: crosslines 289 train / 192 test slices (16,706 / 1,000 records per class); inlines 358 train / 238 test slices (14,988 / 1,000 per class) | **~2.35 GB** | **CC BY 4.0** | **DOI `10.5281/zenodo.3924682`** → `https://zenodo.org/records/3924682` | The reference *labelled* companion to Penobscot. Use with #21 for supervised facies segmentation. Reference implementation: IBM `rockml`. | [V] |
| 24 | **Laurentian Basin — Complete** | Laurentian Deep rift basin, between Newfoundland and Nova Scotia, ~67,016 km² | 2D — **29 lines**, full stack after PSTM | background steering cube, dip-steered median filter, fault-enhancement filter | **2.0 GB download / 3.6 GB uncompressed** | CC BY-SA 3.0 on dGB derived attributes; **original seismic © Natural Resources Canada, Geogratis licence** | `https://terranubis.com/download/NRCAN_Laurentian_Basin_v6.zip/2` | Regional frontier 2D at low disk cost; large-scale structural and attribute work. | [V] |
| 25 | **Nova Scotia Play Fairway Analysis** | Scotian Basin | 2D/3D + full basin-analysis reports | wells | not measured | Free | CNSOER, `https://www.cnsoer.ca` (the regulator renamed from CNSOPB) | An entire regulator-funded basin study released free. | [U] |
| 26 | **LITHOPROBE** | Canada-wide transects | deep crustal 2D reflection | magnetotellurics, refraction | archive-scale | Open Government Licence – Canada | `https://open.canada.ca` (search "Lithoprobe"); NRCan `https://www.nrcan.gc.ca/earth-sciences/science/geology/energy-geoscience/10890` | The great deep-crustal reflection programme; each transect is its own record. | [U] |

---

## United States

### 27. Teapot Dome / RMOTC — where it lives now

`http://www.rmotc.doe.gov/datasets.html` is **dead** ("The old RMOTC web sites no longer
work" — SEG Wiki). The data survives on **two** public S3 buckets, needs no account, and is
**not** on NETL EDX (an EDX search for "teapot dome" returns only unrelated NETL reports).
All byte counts exact.

| File | What it is | Exact bytes | Human | URL |
|---|---|---|---|---|
| `filt_mig.sgy` | 3D filtered post-stack migration volume | 404,989,440 | 386.2 MiB | `https://s3.amazonaws.com/teapot/filt_mig.sgy` — mirrored at `https://s3.amazonaws.com/open.source.geoscience/open_data/teapot/filt_mig.sgy` (identical size) |
| `npr3_gathers.sgy` | **pre-stack** preprocessed CMP gathers at smooth surface | 6,107,591,676 | 5.69 GiB | `https://s3.amazonaws.com/teapot/npr3_gathers.sgy` |
| `npr3_field.sgy` | **pre-stack** unprocessed shot gathers (raw field data) | 6,107,591,676 | 5.69 GiB | `https://s3.amazonaws.com/teapot/npr3_field.sgy` — **reports the same `Content-Length` as the gathers file; compare ETags before assuming they differ** |
| `npr3_dmo.vel` | DMO velocity field, text | 27,944 | 27 KiB | `https://s3.amazonaws.com/teapot/npr3_dmo.vel` |
| `rmotc.tar` | RMOTC support bundle — LAS well logs, formation tops, production history, GIS, 3D corner-point coordinates, processing-sequence documents, horizons | 1,777,994,752 | 1.66 GiB | `https://s3.amazonaws.com/open.source.geoscience/open_data/teapot/rmotc.tar` |

**Total ≈ 14.4 GB.** Wyoming (Powder River Basin), land 3D. Public domain (US DOE / RMOTC);
SEG Wiki records no usage constraint. The reference **US onshore integrated** dataset:
post-stack + two pre-stack volumes + logs + tops + production. Flag `[V]`.

### 28. Stratton 3D (Bureau of Economic Geology, UT Austin) — full file inventory

South Texas land 3D. Base
`https://s3.amazonaws.com/open.source.geoscience/open_data/stratton/`. All sizes exact.

| File | What it is | Exact bytes | Human |
|---|---|---|---|
| `segy/processed/Stratton3D_32bit.sgy` | final migrated image, 32-bit | 443,764,680 | 423.2 MiB |
| `segy/cdp_gathers/cdpgathers_2-80.sgy` | **pre-stack** CMP gathers with NMO | 875,441,520 | 834.9 MiB |
| `segy/cdp_gathers/cdpgathers_82-140.sgy` | pre-stack CMP gathers | 758,730,600 | 723.6 MiB |
| `segy/cdp_gathers/cdpgathers_142-200.sgy` | pre-stack CMP gathers | 776,357,280 | 740.4 MiB |
| `segy/cdp_gathers/cdpgathers_202-290.sgy` | pre-stack CMP gathers | 1,181,982,960 | 1.10 GiB |
| `segy/cdp_gathers/cdpgathers_290-310.sgy` | pre-stack CMP gathers | 243,849,600 | 232.6 MiB |
| `segy/cdp_gathers/cdpgathers_601-630.sgy` | pre-stack CMP gathers | 460,554,480 | 439.2 MiB |
| `segy/navmerged/swath_1_geometry.sgy` | **unprocessed shot gathers with geometry in trace headers** | 1,671,130,800 | 1.56 GiB |
| `segy/navmerged/swath_2_geometry.sgy` | as above | 1,636,369,200 | 1.52 GiB |
| `segy/navmerged/swath_3_geometry.sgy` | as above | 1,697,373,360 | 1.58 GiB |
| `segy/navmerged/swath_4_geometry.sgy` | as above | 1,602,048,240 | 1.49 GiB |
| `segy/VSP/NVSP1.SGY` · `NVSP2.SGY` | **VSP** | 596,880 · 183,118 | |
| `segy/VSP/WVSP1.SGY` · `WVSP2.SGY` | VSP (SEG Wiki flags these as possible repeats of NVSP1/2 — the byte counts are identical, which supports that) | 596,880 · 183,118 | |
| `segy/VSP/TABLE3.TXT` · `VSP_9.TXT` | VSP tables (SEG Wiki asks whether TABLE3 is the corridor stack) | 14,777 · 27,039 | |
| `Stratton_wells.zip` | **well logs** | 1,076,309 | 1.03 MiB |
| `Stratton_Achieve_Log.pdf` | well-log description | 4,598,806 | 4.4 MiB |
| `stratton_acqui_proc.pdf` | acquisition & processing report | 1,416,031 | 1.35 MiB |

**Totals: pre-stack CMP gathers 4,296,916,440 B (4.00 GiB) · unprocessed shot gathers
6,606,921,600 B (6.15 GiB) · everything 11,356,295,678 B ≈ 10.58 GiB.** Flag `[V]`.
License: distribution authorised in 2014 by Bob Hardage (PI) and Scott Tinker (Director,
BEG / State Geologist of Texas), conditional on the acknowledgement *"the data were
collected and made available for worldwide education and training by the Bureau of Economic
Geology at the University of Texas at Austin."* The dataset also includes inversion results
per SEG Wiki. Use: the smallest complete **3D land** package with raw shots + gathers +
final image + VSP + logs.

### Other United States entries

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 29 | **Blake Ridge Hydrates 3D** | offshore South Carolina, 348.93 km² / 164 blocks | 3D PSTM stack **+ conditioned PSTM angle gathers**; detailed and background steering cubes | — | **914 MB download / 1.94 GB uncompressed** | CC BY-SA 3.0 on derived attributes; original seismic released under **NSF award 99190966** | `https://terranubis.com/download/Blake_Ridge_Hydrates_3D.zip/2` | The classic gas-hydrate BSR dataset — and it ships angle gathers, so you can do AVO on a BSR. | [V] |
| 30 | **USGS Central Alaska (NPRA)** | National Petroleum Reserve Alaska, ~14,292 km²; NPRA blocks 2-L-\*\*\*, 2008-L-\*\*\*, 991-L-\*\*\* | 2D — 16–17 lines | — | **160 MB download / 173 MB uncompressed** | CC BY-SA 3.0 (dGB value-add on USGS public-domain original) | `https://terranubis.com/datainfo/USGS-Central-Alaska-2023` → `https://terranubis.com/download/USGS_Central_Alaska_2023.zip/2` | Tiny, fast Arctic onshore 2D. Good smoke-test corpus. | [V] |
| 31 | **USGS Beaufort Sea — Arctic Alaska** | Beaufort Sea shelf near Prudhoe Bay, 18,730.51 km²; acq. 1978, value-add 2023 | 2D — **119 lines** | interpreted horizons (top Ellesmerian, Prodelta); **3D gridded horizons built from the 2D interpretation**; **26 well locations** | **516 MB download / 1.2 GB uncompressed** | Creative Commons 3.0 | `https://terranubis.com/datainfo/USGS-Beaufort-Sea-Arctic-Alaska-2023` → `https://terranubis.com/download/USGS-BeaufortSea-Shallow_water-2023.zip/2` | Arctic shelf 2D with gridded horizons — good for 2D-to-3D horizon workflows. **The slug needs the `-2023` suffix; the bare slug 404s.** | [V] |
| 32 | **Alaska 2D land line 31-81** (NPRA) | NPRA, Alaska | 2D **pre-stack** land: unprocessed prestack data, final stack, images of previous stack | Seismic Unix processing scripts **plus su 43R1 Linux executables** (useful if su is not installed); observer's and surveyor's logs via USGS | `alaska31-81.tar.gz` = **38,138,509 B (36.4 MiB)** | Public domain; credit USGS | `https://s3.amazonaws.com/open.source.geoscience/open_data/alaska/alaska31-81.tar.gz` | The best "hello world" for a complete 2D land processing sequence: download → reformat → header load → gain → prestack f-k filter → brute velocities → brute stack → residual statics → final velocity analysis → final stack → phase-shift **and** Kirchhoff migration. Short line, small statics. | [V] |
| 33 | **Alaska 2D land line 16-81** (NPRA) | NPRA, Alaska; crosses line 31-81 | 2D pre-stack land, same processing sequence as 31-81 | Seismic Unix scripts; research poster (R. Zavala, U. Houston) | `alaska16-81.tar.gz` = **5,480,496 B (5.2 MiB)** | Public domain; credit USGS | `https://s3.amazonaws.com/open.source.geoscience/open_data/alaska/alaska16-81.tar.gz` | Sister line to 31-81 — weaker ground roll, fewer noise bursts, **larger statics problem**, more structure between 1 and 2 s. Use the pair for statics experiments. | [V] |
| 34 | **USGS NPRA seismic data archive (full)** | Arctic Alaska | 2D SEG-Y: **raw field data and processed stacks**, acquired 1974–1981 | observer's logs, surveyor's logs, scanned stack images | archive-scale | Public domain; credit USGS | legacy entry point `http://energy.usgs.gov/GeochemistryGeophysics/SeismicDataProcessingInterpretation/NPRASeismicDataArchive.aspx` — **stale**, see "Couldn't verify" | ~15,000 line-miles of legacy Arctic 2D **with raw shot data** — arguably the largest open raw-prestack 2D land archive anywhere. | [P] |
| 35 | **Mobil AVO Viking Graben Line 12** | North Viking Graben, North Sea (US-released) | 2D **pre-stack** marine, unprocessed field data | **two well logs**; a basic Seismic Unix script | `seismic.segy` = **749,552,400 B (714.8 MiB)** | **Public domain** — Keys & Foster: *"Since the workshop data set is in the public domain, readers can apply their own methods to the data."* | `https://s3.amazonaws.com/open.source.geoscience/open_data/Mobil_Avo_Viking_Graben_Line_12/seismic.segy` · landing page `.../Mobil_Avo_Viking_Graben_Line_12/mobil_avo.html` | The reference open **pre-stack AVO / seismic-inversion** line, from the 1994 SEG inversion workshop (Keys & Foster, *Comparison of Seismic Inversion Methods on a Single Real Data Set*; also Madiba & McMechan 2003). | [V] |
| 36 | **US east coast deep water line 32** | Southern Atlantic Margin | 2D marine: **unprocessed field data + processed stack**, SEG-Y | observer's logs; final report with interpretation (USGS OFR 1995-0027) | not measured (Dropbox host) | Public domain; credit USGS (confirmed by USGS Woods Hole email quoted on the wiki page) | scripts tar `https://www.dropbox.com/s/xa5c8t6h0lyz57d/eastcoast32.tar?dl=0`; data at the **USGS Woods Hole datastore** `https://woodshole.er.usgs.gov/operations/ia/public_ds_info.php?fa=1978-015-FA` | Deep-water margin 2D with raw field data. The Woods Hole datastore is the real prize — **many** lines, not just 32. | [P] |
| 37 | **PGS Simultaneous Source (blended) Marine Line** | marine, PGS | 2D **blended / simultaneous-source** shot data — a 2768 × 256 × 256 (ntime, nreceiver, nshot) MATLAB array at 4 ms | 256 × 256 array of inter-shot time delays; a Jupyter notebook that reads the `.mat` into numpy; a summary PDF. **No geometry information at all.** | `blended_data.mat` **788,684,435 B (752.2 MiB)** · `time_delay_in_ms.mat` **1,580 B** · `reading_blended_data.ipynb` **1,444,421 B** · `2017_SeismicDeblendingSummary_Final.pdf` **897,361 B** | Provided by PGS for the 2017 IEEE signal-processing competition (Tokyo); acknowledge PGS in any use | `https://s3.amazonaws.com/open.source.geoscience/open_data/pgsblended/blended_data.mat` and siblings | The only open **deblending** benchmark, and it arrives ML-ready (MATLAB → numpy) rather than as SEG-Y. | [V] |
| 38 | **2010 BP 3D Tiber WATS** | Northern Keathley Canyon, deep-water Gulf of Mexico; full-fold area ≈ 11 OCS blocks; Tiber is a Paleogene deep-water oil field | 3D **wide-azimuth towed-streamer**, pre-stack, 5 subsets | **anisotropic velocity model (36 GB)**; geological information, technical overview, file lists, copyright — 19 MB of documents | raw large-area **5.8 TB** · raw small-area **1.0 TB** · decimated small-area **130 GB** · preprocessed (regularized, migration-ready) large-area **725 GB** · preprocessed small-area **120 GB** · velocity model **36 GB** | **CC BY-NC-SA 4.0** (released 2020); redistribution explicitly permitted | **No public online copy exists.** Distributed on media to universities 2021–22: CSM, UT Austin, U. Houston, UT Dallas, MIT, Princeton, Rice, Stanford, Calgary, Memorial, Alberta, Imperial, Leeds, Edinburgh, Durham, Bristol, ETH Zürich, NTNU, Curtin, ANU, KAUST, CICESE. | The largest openly-licensed **pre-stack WATS 3D** in existence — sub-salt imaging and FWI at industrial scale. Acquired by CGGVeritas for bp. | [V] on sizes and licence. **No download URL exists — do not invent one.** |
| 39 | **NAMSS — USGS National Archive of Marine Seismic Surveys** | US Exclusive Economic Zone: Gulf of Mexico, Atlantic, Pacific, Alaska (incl. North Slope), offshore Diablo Canyon | 2D lines and 3D post-stack volumes in SEG-Y, plus navigation; some surveys hold only PDF images | navigation | archive-scale. **>300,000 km transferred by WesternGeco and Chevron alone (2005)**, plus USGS OCS/EEZ 1975–mid-1990s, plus BP North Slope, PG&E Diablo Canyon, and BOEM releases since 2011 | **Public domain, no restrictions on usage or publication.** (BOEM G&G data is releasable after the 25-year proprietary term, 30 CFR 551 & 580.) Cite Triezenberg, Hart & Childs 2016, **doi:10.5066/F7930R7P**, and Kluesner, Hart, Snyder & Triezenberg 2024, **doi:10.1029/2023CN000229** | Portal `https://walrus.wr.usgs.gov/namss/` (map + filters). **A WMS service exists**: `https://walrus.wr.usgs.gov/namss/wms?request=GetCapabilities&service=WMS&version=1.1.1` (EPSG:3857; GetCapabilities / GetMap / GetFeatureInfo; a `FILTERS` parameter supports `identifier`, `data-type`, `year` (with `..` ranges), `contributor`, each OR-able, e.g. `FILTERS=identifier;F-2-86-BS OR L87-056 OR G3D1106-001`) | No account, no registration — the easiest large US archive to script against. **The WMS is the only machine-readable index found; there is no file-listing API, so per-survey sizes must be harvested from the map UI.** | [V] on portal, licence, citations and WMS; `[U]` on named 3D volumes and their sizes |
| 40 | **Kansas Geological Survey 3D/4D** (Dickman, Wellington CCUS, Cutter) | Kansas, US midcontinent | 3D SEG-Y; the 4D CO2-injection monitoring project ran a **baseline plus six monitor 3D surveys**, Nov 2003 – Jul 2005 | Dickman: **3.3 sq mi of 3D, 142 wells with logs, core, and oil/water production data**. Wellington: multicomponent 3D, CO2-EOR/CCUS, Sumner County (acquisition/analysis by Paragon Geophysical) | not measured | Free | `https://www.kgs.ku.edu/Geophysics/` resolves; **`https://www.kgs.ku.edu/Geophysics/4Dseismic/` is a project website of site-visit reports, progress reports and processing updates — no SEG-Y download links were found on it.** | Small, clean CCS/4D method-development targets. | **`[U]` — no working SEG-Y download path was established. Do not cite a KGS download URL from memory; contact Rick Miller (project investigator) instead.** |
| 41 | **Illinois Basin — Decatur Project (IBDP)** | Illinois Basin, USA | CO2 injection reference package: subsurface, monitoring and geomechanical data, including seismic monitoring products | monitoring wells | ZIP; per-file sizes require opening the dataset page | **Illinois Basin – Decatur Project CO2 Injection Datasets Licence** (open access) | `https://co2datashare.org/dataset` → "Illinois Basin - Decatur Project Dataset" | A major US CCS demonstration with time-lapse monitoring — and CO2DataShare is a much easier host to reach than NETL EDX. | [V] on listing and licence |

---

## Japan

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 42 | **Kumano 3D — Nankai Trough (NanTroSEIZE site survey)** | Kumano Basin, central Nankai Trough, off the Kii Peninsula. Acquired April–May 2006 by M/V *Nordic Explorer* (PGS Geophysical) for JAMSTEC — the first 3D site survey run with a commercial seismic vessel. Survey ~12 km (strike) × 56 km (dip). | **3D migration volume**, SEG-Y. The public file covers inlines 2130–2750, CMPs 3720–7230; bounds 136.460–136.818 °E, 33.012–33.476 °N | in MGDS entry `Nankai:Moore`: survey location map `Nankai_3D_survey.pdf` (305 KB) and science report `2006020_NOR_Jamstec.pdf` (9.0 MB) — that entry's own MCS is marked "Data not online", but the migration volume below **is** online under entry `KUMANO3D` | `ar55.4495.kumano3d.2130_2750.3dmigration.segy` = **27,697,960,040 bytes (25.8 GB)**, exact, from the MGDS `FileServer` API | Access status **PUBLIC**, release date **2020-05-24**. MGDS site licence CC BY-NC-SA 3.0; users must cite contributing scientists and MGDS. *A Business Use License may be required for marine seismic data* — `techventures@columbia.edu`. | MGDS entry `KUMANO3D`, `data_uid=1464342`, `data_set_uid=28541`. Retrieve through the MGDS download flow described below. | **This answers "is the Nankai 3D open?" — yes.** A 25.8 GB migrated 3D volume across the seismogenic zone is public, but through MGDS rather than JAMSTEC's own portal. Subduction-zone imaging, IODP borehole ties. | [V] |

---

## Academic marine MCS via MGDS (marine-geo.org)

MGDS is the **Marine Geoscience Data System**, run at Lamont-Doherty Earth Observatory /
Columbia and funded by NSF. It holds the US academic multichannel-seismic archive and is by
far the largest source of open, named, *academic* field seismic outside the national
regulators.

### 43. Verified recipe: enumerating and sizing MGDS holdings

**Step 1 — list files with sizes.** The `FileServer` REST service:

```
https://www.marine-geo.org/services/FileServer
    ?data_type=Seismic:Reflection:MCS
    &file_format=SEGY
    &minlongitude=<W>&maxlongitude=<E>&minlatitude=<S>&maxlatitude=<N>
    &format=full_info
```

`format=full_info` returns per file: `data_uid`, `data_set_uid`, `entry_id` (cruise ID),
`<file_name>`, **`data_file_size` in bytes**, `uncompressed_file_size`,
`<access release_date="…">PUBLIC</access>`, start/stop time and lat/lon, the associated line
`event`, and `<segy start_cmp stop_cmp has_hist>`. `format=summary` gives name + `data_uid`
+ a download link; `format=data_set` and `format=geoms` also exist. Additional filters:
`platform`, `platform_type`, `event`, `starttime`, `endtime`. Latitude/longitude parameters
also accept the aliases `north`, `south`, `east`, `west`.

Controlled vocabularies: `https://www.marine-geo.org/services/VocabServer/data_type`,
`.../file_format_id`, `.../platform_id`, `.../platform_type`, `.../event`.
The seismic `data_type` terms are: `Seismic:Reflection:MCS`, `Seismic:Reflection:SCS`,
`Seismic:WideAngle` (+`:OBS`, `:OBH`, `:ESPs`), `Seismic:Passive` (+`:OBS`, `:OBH`,
`:Compliance`), `Seismic:Active:Subbottom`, `Seismic:Active:OBS:TravelTimePicks`,
`Seismic:Velocity:Model`, `Seismic:Navigation` (+`:ShotTime`), `Seismic:SegyHistory:MCS|SCS`,
`Seismic:ShotTimesStatus`, `Seismic:ReceiverFunction`, `Seismic:Ancillary`.
Relevant `file_format` terms: `SEGY`, `SEGD`.

Per-cruise line geometry and acquisition parameters come from a second service:
`https://www.marine-geo.org/services/seismicxml/xml?id=<CRUISE>` (e.g. `?id=MGL2104`,
`?id=EW0207`). Note this endpoint emits PHP warnings before the XML for some IDs — parse
defensively.

**A whole-globe query (`-180…180 / -90…90`) returns `count=0`.** The service needs a real
bounding box, so enumerate region by region.

**Step 2 — download.** The `download=` attribute the API returns points at
`.../services/FileDownloadServer?data_uid=NNN`, but **that endpoint 301s to
`api.marine-geo.org` and then 404s** (verified on three separate uids). The working route is:

```
https://www.marine-geo.org/services/download/download.php
    ?data_uids=<comma-separated data_uids>&data_set_uid=<data_set_uid>
```

That returns a **terms-acceptance page** which states the bundle size — for CASIE21
MGL2104 it reads *"Archive Download is 227.1MB (269.0MB uncompressed)"* — and posts to
`https://api.marine-geo.org/services/download/download_accept.php` with an "intended use"
field (Educational / Research / Personal Interest / Commercial / Other).
**There is no anonymous direct-file URL.** Bulk retrieval means scripting that accept POST,
or using the site's "Download Selected File(s)" / "Request Selected File(s)" (DVD or FTP
session) buttons. Dataset landing pages are
`https://www.marine-geo.org/tools/files/<data_set_uid>`; cruise pages are
`https://www.marine-geo.org/tools/search/entry.php?id=<CRUISE>`. Documents attach via
`https://api.marine-geo.org/services/download/Document_Accept.php?client=DataLink&doc_uid=<n>&entry_id=<CRUISE>`.

**Step 3 — terms.** Site licence **CC BY-NC-SA 3.0 (US)**. Users must cite the contributing
scientists and MGDS, and are encouraged to contact the original investigators and consider
co-authorship. Datasets carry their own DOIs. Flag `[V]`.

### 44. Verified regional inventories (MCS, SEG-Y, `data_file_size` summed)

| Region (bounding box used) | Files | Total size | Principal cruises (by file count) | Flag |
|---|---|---|---|---|
| **Cascadia** (128–123 °W, 42–50 °N) | 722 | **384.22 GB** | TN112, EW0208, GT8909, **MGL2104 (CASIE21)**, RR1718, W0709A, MGL1212, MGL1211 | [V] |
| **Costa Rica / CRISP** (88–83 °W, 7.5–10.5 °N) | 676 | **1,471.14 GB (1.47 TB)** | IG2402, FM3502, EW0104, IG2903, MGL0807, EW0005, EW0412, IG2403 | [V] |
| **ENAM — Eastern North American Margin** (78–70 °W, 31–39 °N) | 1,510 | **1,421.19 GB (1.42 TB)** | FM0802, FM1001, IG1502, EW0008, MGL1408, EW9009, EN555, IG1501 | [V] |
| **Alaska / Aleutians** (172–140 °W, 50–62 °N) | 462 | **1,082.52 GB (1.08 TB)** | AG1608, EW0408, EW9409, MGL0814, EW9410, MGL1109, MGL1110, GT8907 | [V] |
| **Gulf of Corinth** (21.0–23.8 °E, 37.7–38.7 °N) | 163 | **110.89 GB** | EW0108 | [V] |
| **Nankai Trough** (134–139 °E, 31–35 °N) | 156 | **959.94 GB** | EW9907, EW9908, FM3506, **KUMANO3D** | [V] |
| **Gulf of Mexico** (98–82 °W, 18–31 °N) | 2,600 | **884.69 GB** | FM0301, FM0702, EW0501, FM0901, FM1501, IG2801, MNT1301, FM1801 | [V] |
| **Mid-Atlantic Ridge** (46–40 °W, 20–32 °N) | 64 | **90.58 GB** | EW0102, FM1002, RC3001 | [V] |

*(Hikurangi NZ3D falls in the New Zealand file. CRISP, ENAM, Cascadia, Alaska/Aleutians and
Gulf of Corinth are all confirmed present and sized above; the cruise IDs are the handles to
filter on.)*

### 45. CASIE21 — Cascadia Seismic Imaging Experiment 2021 (named highlight)

* Cruise **MGL2104**, R/V *Marcus G. Langseth*, June 2021. **18 primary margin-crossing
  lines and 6 margin-parallel lines**, ~42–50 °N — the whole Cascadia subduction zone.
* PIs Suzanne Carbotte, Shuoshuo Han, Brian Boston, Juan Pablo Canales
  (NSF OCE18-27363 / OCE18-27452 / OCE18-29113).
* **39 SEG-Y files of pre-stack depth-migrated Kirchhoff stacks, totalling
  10,337,499,324 bytes (10.34 GB)** — exact, summed from the API. Individual lines run
  51 MB to 788 MB; largest is `MGL2104PS01ACD_psdm_kir_stk_20220802.sgy` at 788,107,320 B.
* Naming: `MGL2104{PDnn|PSnn|TDnn}_psdm_kir_stk_20220802.sgy` — PD = margin-perpendicular
  dip lines, PS = strike lines, TD = tie lines. `data_uid` runs 2839302–2839342.
* Companion datasets: **navigation (P1)** DOI `10.26022/IEDA/330901`;
  **shot data (SEG-D)** DOI `10.26022/IEDA/330905`; **interpretation (NetCDF grids)**
  DOI `10.60521/331666`. Processed stacks DOI `10.26022/IEDA/331274`
  (`https://www.marine-geo.org/tools/files/31274`, `data_set_uid=31274`).
* Documents bundle 71.4 MB: final cruise report (10.4 MB) and the MGL2104/MGL1211
  Cascadia 2D PSDM processing report (61.0 MB).
* Use: a modern, high-quality PSDM of an entire active margin, with **shot gathers available
  separately** — the best open academic **pre-stack + PSDM pair**. Flag `[V]`.

---

## Poland

| # | Dataset | Basin / area | Type | Ancillary | Size | License | Verified download | Typical use | Flag |
|---|---|---|---|---|---|---|---|---|---|
| 46 | **Poland 2D Vibroseis Line 001** | Poland, onshore | 2D **pre-stack land vibroseis**. 25 m receiver / 50 m source interval; SP stations 701–1201; live stations 561–1342; SM-4 10 Hz geophones, 24 per group in a 25 m linear array; sweep 8–95 Hz, UP +3 dB/oct; reference velocity 1900 m/s | **complete SPS geometry**: `Line_001.SPS` (source, 21,951 B), `Line_001.RPS` (receiver, 64,962 B), `Line_001.XPS` (relational, 21,951 B), `Line_001.TXT` acquisition parameters (866 B) | `Line_001.sgy` = **445,100,896 bytes (424.5 MiB)**; tar ≈ 445 MB | **Donated to the public domain** by Geofizyka Toruń Sp. z o.o. | **`http://www.geofizyka.pl/2D_Land_vibro_data_2ms.tgz` returns 404 (verified).** The FTPS host is up (`https://ftps.geofizyka.pl/` → 200); the documented weblink form is `https://ftps.geofizyka.pl/main.html?download&weblink=973286ef2a219064126f69fd6b8f77c6&realfilename=2D_Land_vibro_data_2ms.tgz`. Originally posted on FreeUSP 2005-02-20. | The standard open **land pre-stack + complete SPS geometry** line. Used by Liu, Fomel & Liu (2015) *Geophysics* 80(6):WD117 for velocity-dependent seislet denoising; Madagascar ships a full processing tutorial on it. | [P] — inventory and byte counts from the SEG Wiki file table; **the plain HTTP URL is confirmed dead** |

---

## Aggregators and inventories

### 47. TerraNubis (dGB Earth Sciences) — complete free list, all 12 slugs verified

`https://terranubis.com/datalist/free`. Info page `https://terranubis.com/datainfo/<Slug>`;
download `https://terranubis.com/download/<File>.zip/2` (session-gated).

| Project | Slug | Download / uncompressed | Covered at |
|---|---|---|---|
| F3 Demo 2023 | `F3-Demo-2023` | 4.5 GB / 7.6 GB | NL #1 |
| Delft | `Delft` | 2.8 GB / 5.4 GB | NL #4 |
| Penobscot | `Penobscot` | 8.7 GB / 12.4 GB | Canada #21 |
| FORCE ML Competition 2020 | `FORCE-ML-Competition-2020` | **7.3 GB / 7.9 GB** — Ichthys 3D, offshore **Australia**, 563.05 km², UTM 51S/WGS84. Fault-interpretation ML target (polygonal + planar faults). Organised by FORCE (NPD); original seismic from Geoscience Australia; project by dGB. **CC BY-SA 4.0.** `https://terranubis.com/download/FORCE_ML_Competition_2020.zip/2` | AU — cross-ref `field-volumes-nz-au.md` |
| FORCE ML Competition 2020 Synthetic Models and Wells | `FORCE-ML-Competition-2020-Synthetic-Models-and-Wells` | not measured | synthetic — ML doc |
| Blake Ridge Hydrates 3D | `Blake-Ridge-Hydrates-3D` | 914 MB / 1.94 GB | US #29 |
| Laurentian Basin – Complete | `Laurentian-Basin-Complete` | 2.0 GB / 3.6 GB | Canada #24 |
| NW Shelf Australia – Poseidon 3D | `NW-Shelf-Australia-Poseidon-3D` | not measured | AU file |
| OGA MNSH | `OGA-MNSH` | 11 GB / 12 GB | UK #18 |
| OGA Rockall Trough | `OGA-Rockall-Trough` | 11 GB / 12 GB | UK #19 |
| USGS Beaufort Sea – Arctic Alaska | `USGS-Beaufort-Sea-Arctic-Alaska-2023` | 516 MB / 1.2 GB | US #31 |
| USGS Central Alaska | `USGS-Central-Alaska-2023` | 160 MB / 173 MB | US #30 |

The first five run without an OpendTect licence key. Flag `[V]`.

### 48. OSDU Open Test Data — fully enumerated

Repo: `https://community.opengroup.org/osdu/platform/data-flow/data-loading/open-test-data`
(Apache 2.0, est. Feb 2020). Data lives in a **public, listable** S3 bucket:

```
aws s3 ls s3://osdu-seismic-test-data/ --no-sign-request
aws s3 cp s3://osdu-seismic-test-data/<key> <target> --no-sign-request
# plain HTTPS works too:
https://s3.amazonaws.com/osdu-seismic-test-data/<key>
https://s3.amazonaws.com/osdu-seismic-test-data/?list-type=2&max-keys=1000   # listing OK
```

**Whole bucket: 19,092 objects, 23,769,977,002 bytes (23.77 GB).** Flag `[V]`.

| Prefix | Files | Bytes | Contents |
|---|---|---|---|
| `volve/` | 109 | 22,637,514,545 (22.64 GB) | see below |
| `r1/data/provided/` | 12,790 | 1,050,851,514 (1.05 GB) | R1 reference set: USGS documents (PDFs), markers, and assorted per-well CSVs |
| `tno/trajectories_1_1_0/` | 6,192 | 76,566,587 | TNO well trajectories (CSV) |
| `nopims/seismic/` | 1 | 5,044,356 | `CVX_Acme-1_upp.sgy` |

**`volve/` breakdown** — `seismic` 49 files / 22,413,469,774 B (22.41 GB) · `horizons`
7 / 102,484,196 B · `welllogs` 28 / 99,320,744 B (LAS) · `documents` 6 / 21,244,348 B ·
`faults` 2 / 824,056 B · `checkshots` 7 / 71,498 B · `trajectories` 2 · `markers` 7.

**`volve/seismic/st0202/` (the 3D survey), exact sizes:**

| Key | Bytes | What |
|---|---|---|
| `prestacks/ST0202R08_PZ_PrSDM_CIP_gathers_in_PP_Time.segy` | 20,311,496,528 | **pre-stack CIP gathers, PP time** |
| `stacks/ST0202R08-PS_PSDM_FULL_OFFSET_DEPTH.MIG_FIN.POST_Stack.3D.JS-017534.segy` | 895,367,300 | full-offset PSDM post-stack, depth |
| `velocities/TTI_model_2011/ST10010ZC11_MIG_VEL.MIG_VEL.VELOCITY.3D.JS-017527.segy` | 479,335,024 | **TTI migration velocity volume** |
| `stacks/ST0202R08_PS_PSDM_RAW_PP_TIME.MIG_RAW.POST_Stack.3D.JS-017534.segy` | 277,427,976 | raw PSDM stack, PP time |
| `bingrids/*.sgp` (2 files) | 14,674,588 + 3,684,484 | bin grids |
| `stacks/SeismicOrderSummary+Header.txt`, `velocities/SeismicOrderSummary+Headers.txt` | 446,268 + 99,234 | order summaries |

`volve/seismic/st0299/` holds **40 migrated 2D lines** (`ST0299-*+MIG_FIN.segy`, ~12–19 MB
each, 430,938,372 B total). Horizons are `.dat` picks on ST0202R08 PSDM (BCU, Balder Fm,
Hod Fm, Ty Fm Top, Shetland Gp) plus Hugin Fm top/base in depth.

### 49. `open.source.geoscience` S3 bucket — verified key inventory

Listing **denied**; objects public. Base
`https://s3.amazonaws.com/open.source.geoscience/open_data/`.

| Key | Bytes |
|---|---|
| `teapot/filt_mig.sgy` | 404,989,440 |
| `teapot/rmotc.tar` | 1,777,994,752 |
| `stratton/…` (21 objects) | 11,356,295,678 total — full table above |
| `Mobil_Avo_Viking_Graben_Line_12/seismic.segy` | 749,552,400 |
| `alaska/alaska31-81.tar.gz` | 38,138,509 |
| `alaska/alaska16-81.tar.gz` | 5,480,496 |
| `pgsblended/blended_data.mat` | 788,684,435 |
| `pgsblended/time_delay_in_ms.mat` | 1,580 |
| `pgsblended/reading_blended_data.ipynb` | 1,444,421 |
| `pgsblended/2017_SeismicDeblendingSummary_Final.pdf` | 897,361 |
| `elastic-marmousi/elastic-marmousi-model.tar.gz` | 153,722,387 (synthetic) |

Landing pages under the bucket: `SModels/SModels.html`,
`seg_workshop_fwi/seg_workshop_fwi.html`,
`seg_workshop_fwi_2014/seg_workshop_fwi_2014.html`,
`Mobil_Avo_Viking_Graben_Line_12/mobil_avo.html`.

Documented keys that return **403** (they do not exist under those names):
`open_data/teapot/npr3_field.sgy`, `open_data/teapot/npr3_gathers.sgy`,
`open_data/stratton/stratton.sgy` — the Teapot pre-stack files live in the **separate
`teapot` bucket**. Flag `[V]`.

### 50. SEG Wiki Open Data

Cloudflare-blocked to automation; read through Wayback
(`http://web.archive.org/web/2024/https://wiki.seg.org/wiki/Open_data`). Field-data sections:
2D land (Poland 001) · 2D marine (US east coast line 32, USGS marine/NAMSS, Mobil AVO Viking
Graben line 12, PGS simultaneous source, UK MNSH & Rockall, UK SW Britain & East Shetland) ·
3D land (**Teapot Dome, Stratton**) · 3D marine (F3, Poseidon, Penobscot, Blake Ridge,
**Norne**, Volve, **BP Tiber WATS**) · NPRA Alaska (lines 31-81, 16-81) · Qademah Fault 3D
(KAUST, `https://csim.kaust.edu.sa/files/FieldData/Qademah_2014/Active/Qademag_3D_Active.htm`)
· New Zealand 3D (Opunake, Parihaka, Kahu, Kerry, Tui, Waihapa, Waipuku, Waka — NZ file) ·
NRCan · BGS OpenGeoscience · NPD/Sodir · SEAM (Google Drive-hosted) and the synthetic model
collection · SEG/DMEC reference mineral exploration data · the SEG 2020 ML blind-test
challenge (3D volume + 6-class facies label volume, both SEG-Y). Flag `[V]` for the
catalogue structure.

### 51. Data Underground (`dataunderground.org`)

**DEAD.** DNS does not resolve. Verified this pass. Do not cite it as a host; its Teapot
Dome and `?tags=3D+seismic` pages survive only in search indexes and Wayback.

---

## Best starting corpus (shortlist)

A compact, fully-verified, legally-clean corpus spanning post-stack, pre-stack, 4D,
ML labels, VSP and ancillary data — in roughly build order:

| Rank | Dataset | Size | Why it earns the disk |
|---|---|---|---|
| 1 | **F3 Demo 2023** | 4.5 GB | The lingua franca. 4 wells, 8 horizons, AI cubes, velocity models, no licence key. |
| 2 | **Penobscot** + **Penobscot Interpretation Dataset** | 8.7 GB + 2.35 GB | The only clean *seismic + published labels + angle gathers + velocities + wells* stack. CC BY-SA / CC BY 4.0. |
| 3 | **Volve seismic via the OSDU S3 bucket** | 22.4 GB | **Anonymous, listable, `curl`-able pre-stack CIP gathers (18.9 GiB) + PSDM stacks + a TTI velocity volume + LAS + horizons.** By far the highest value-per-GB open pre-stack 3D. |
| 4 | **Teapot Dome** | ~14.4 GB | US onshore, raw shots *and* CMP gathers *and* final image *and* logs *and* production. Public domain. |
| 5 | **Stratton 3D** | ~10.6 GB | The second land 3D, and it has **VSP**. Pairs with Teapot for land-processing method work. |
| 6 | **Mobil AVO Viking Graben Line 12** | 715 MiB | The pre-stack AVO reference line. Public domain, tiny. |
| 7 | **Alaska lines 31-81 + 16-81** | 41.6 MiB combined | Complete reproducible 2D land processing sequences with scripts and binaries. Effectively free to store. |
| 8 | **OGA Rockall Trough** | 11 GB | **Angle stacks** plus 20 wells, OGL v3.0. |
| 9 | **Sleipner 4D** (+ 2019 Benchmark Model) | ~24.6 GiB | The CCS time-lapse reference: 12 cubes, 7 vintages, 1994–2010. |
| 10 | **CASIE21 / MGL2104 PSDM stacks** | 10.34 GB | A modern whole-margin academic PSDM, with SEG-D shot data available separately. |
| 11 | **Norne** | — | The 4D-plus-Eclipse-model pairing; nothing else gives you seismic and a history-matched simulation together. |
| 12 | **Kumano 3D** | 25.8 GB | The open subduction-zone 3D. |

Items 1–10 come to roughly **110 GB** and already cover post-stack, pre-stack gathers, shot
gathers, angle stacks, VSP, 4D, velocity models, wells, production and ML labels.

**If you need bulk instead of breadth**, the verified archive-scale options are, in order of
ease: NLOG (no registration, tens of TB), the SCAN programme (98 direct zips, 234.65 GB),
NAMSS (public domain, no account), MGDS by region (the eight boxes above total ~6.4 TB), and
Volve in full (~5 TB).

---

## What could not be verified

* **Kansas Geological Survey** (Dickman, Wellington CCUS 3D+4D, Cutter). The project facts
  are documented — Dickman is 3.3 sq mi of 3D with 142 wells (logs, core, production);
  Wellington is multicomponent 3D CO2-EOR in Sumner County; the 4D project ran a baseline
  plus six monitor surveys 2003–2005 — but `kgs.ku.edu/Geophysics/4Dseismic/` is a website of
  reports, **not a data download page**, and no SEG-Y path was found. Flagged `[U]`.
* **NAMSS named 3D volumes and per-survey sizes.** The WMS is the only machine-readable
  index; there is no file-listing API. Host, licence, citation DOIs and WMS parameters are
  verified; the named 3D inventory is not.
* **USGS NPRA archive current URL.** The `energy.usgs.gov/…NPRASeismicDataArchive.aspx`
  entry point on SEG Wiki is stale; the live replacement (likely ScienceBase or a USGS Alaska
  Science Center page) was not confirmed.
* **Groningen 3D**, **Diskos/Sodir named cubes**, **Nova Scotia Play Fairway**,
  **LITHOPROBE**, **UK SW Britain & East Shetland Platform** — hosts named, not fetched.
* **Volve's per-subset breakdown in the *official* release.** Equinor publishes only the
  ~5 TB / ~40,000-file totals. The 22.4 GB OSDU mirror is a *curated subset*, not the whole
  seismic holding — do not conflate them.
* **Most CO2DataShare ZIP sizes** other than Sleipner 4D and Smeaheia, which were opened
  individually. The catalogue page lists format and licence but not size.
* **TerraNubis measured byte counts** — downloads are session-gated, so the portal's own GB
  figures were used.
* **Geofizyka Toruń weblink token** for Poland Line 001 — the host is up and the plain HTTP
  `.tgz` URL is confirmed **404**; the FTPS weblink was not exercised.
* **BP Tiber WATS** — confirmed to have **no online copy at all**. Sizes and licence are
  verified; there is no URL to give, and none should be invented.
* **`open.source.geoscience` complete key list** — the bucket denies listing, so the
  inventory above is only what documentation revealed. There are almost certainly more keys.
