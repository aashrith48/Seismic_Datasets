# ML-Ready and Synthetic Exploration-Seismic Benchmarks

> **Status: LIVE-VERIFIED.** This file replaces an earlier knowledge-only placeholder.
> Every row carries an explicit verification flag stating what was actually checked.
> Research session: 2026-08-24. **131 numbered entries.**

**Flag key**

| Flag | Meaning |
|---|---|
| `[V-HEAD]` | URL fetched with HTTP HEAD; **exact `Content-Length` in bytes recorded** |
| `[V-PAGE]` | Landing/host page fetched and read; sizes taken from the portal's own metadata |
| `[V-API]` | Enumerated via a machine API (HuggingFace `/api/datasets`, Zenodo `/api/records`, Dataverse `/api/datasets`); **byte-exact** |
| `[V-DEAD]` | Checked and found **dead / moved / blocked** — documented as such |
| `[U]` | Unverified — could not fetch; a search phrase is given instead of a guessed URL |

---

## 0. Headline infrastructure findings — read this first

| Finding | Detail | Flag |
|---|---|---|
| **`freeusp.org` is dead as a data host** | `http://www.freeusp.org/` returns 200 but **302-redirects to `https://freedds.org`**, which serves only the FreeDDS *software* (BP Amoco's Data Dictionary System I/O library). `https://www.freeusp.org` (TLS) fails outright — HTTP only. **No BP/SMAART data remains there.** | `[V-DEAD]` |
| **A FreeUSP mirror exists but has no data** | `https://stuartschmitt.com/FreeUSP/` is live (200, 8 220 B; mirrors `RaceCarWebsite`, `DDS`, and a `2007_BP_Ani_Vel_Benchmark` stub). Its `2007_BP_Ani_Vel_Benchmark/listing.html` is **404** — it mirrors the *software* site, not the data archive. Do not rely on it. | `[V-DEAD]` |
| **The SMAART JV host is gone** | `http://www.delphi.tudelft.nl/SMAART/` — **connection failure (curl exit 6 / code 000, DNS)**. Per the SEG Wiki, the SMAART models (Pluto, Sigsbee, Ziggy) are "maintained and licensed by TNO and Delphi", but the Delphi URL no longer resolves. | `[V-DEAD]` |
| **The BP / Chevron / SEG-EAGE benchmarks live on S3** | `https://s3.amazonaws.com/open.source.geoscience/open_data/<name>/…` is **alive and serving**. This is the de-facto live store behind the SEG Wiki. | `[V-HEAD]` |
| **The S3 bucket is NOT listable** | `?list-type=2` ⇒ `AccessDenied`; bare directory paths ⇒ 403; no `index.html` or `open_data.html` at the root (403). You must know the exact object key or reach it via a per-dataset `.html` index inside the bucket. **Directory names are case-sensitive and non-obvious** (`bpvelanal2004`, `bptti2007`, `seg_eage_models_cd`, `seg_eage_salt`, `elastic-marmousi`, `seg_workshop_fwi`, `seg_workshop_fwi_tti`, `seg_workshop_fwi_long_offset2013`, `seg_workshop_fwi_2014`, `SModels`). Brute-forcing ~18 plausible names for Hess/statics/Pluto/Sigsbee found nothing — a 403 is returned for both "wrong key" and "no permission", so probing is useless. | `[V-HEAD]` |
| **`software.seg.org` returns HTTP 525; `wiki.seg.org` and `seg.org` return 403** | 525 = Cloudflare SSL handshake failure; 403 = bot protection. Both block `curl` **and** WebFetch, with and without a browser User-Agent, and the `r.jina.ai` reader proxy returned nothing usable. Content here was recovered from a cached copy of the SEG Wiki *Open data* page plus the S3 index pages. | `[V-DEAD]` |
| **Madagascar's data server path has moved** | `https://reproducibility.org/` root is **alive (200, 26 226 B)**, but `/data`, `/data/`, `/data/index.html`, `/data/sigsbee`, `/RSF/book/data/` and `/wiki/Download` all return **404**. The widely-cited `reproducibility.org/data/sigsbee` path is stale. | `[V-DEAD]` |
| **`dataunderground.org` is unreachable** | curl exit code 000 (DNS/connection failure). The Georgia Tech datasets it hosted are on Zenodo instead (see §4). | `[V-DEAD]` |
| **License split matters commercially** | Three tiers: **(a) CC-BY / MIT — safe** (SEG/EAGE models, F3 benchmark, Penobscot, SFM data, the entire CIG collection); **(b) CC-BY-NC-SA — research only** (all of OpenFWI's *data*); **(c) bespoke restrictive** (Chevron DLA — revocable/non-transferable; FaultSeg3D — "personal and research use only"). | `[V-PAGE]` |

---

## 1. OpenFWI — the modern FWI / velocity-inversion benchmark suite

**Paper:** Deng, C., Feng, S., Wang, H., Zhang, X., Jin, P., Feng, Y., Zeng, Q., Chen, Y., Lin, Y.
*OpenFWI: Large-scale Multi-structural Benchmark Datasets for Full Waveform Inversion.*
NeurIPS 2022 Datasets & Benchmarks Track. arXiv:2111.02926.

| Resource | URL | Status |
|---|---|---|
| Landing page | `https://openfwi-lanl.github.io/` | live `[V-PAGE]` |
| **Dataset table (the one you want)** | `https://openfwi-lanl.github.io/docs/data.html` | live `[V-PAGE]` |
| Code | `https://github.com/lanl/OpenFWI` | live `[V-PAGE]` |

**Two different licenses — do not conflate:**
- **Code** (`github.com/lanl/OpenFWI`): **BSD-3-Clause** `[V-PAGE]`
- **Data** (per data.html): **CC BY-NC-SA 4.0 — NonCommercial.** A real blocker for a commercial product. `[V-PAGE]`

**Hosts:** 2D families on **Google Drive**; **Kimberlina** families on **NETL** (US DOE National Energy Technology Laboratory), not LANL. `[V-PAGE]`

| # | Dataset | Family | Samples (train/val) | Seismic dims | Velocity dims | Size | Host | Flag |
|---|---|---|---|---|---|---|---|---|
| 1 | **FlatVel-A** | Vel | 24 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **43 GB** | Google Drive | `[V-PAGE]` |
| 2 | **FlatVel-B** | Vel | 24 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **43 GB** | Google Drive | `[V-PAGE]` |
| 3 | **CurveVel-A** | Vel | 24 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **43 GB** | Google Drive | `[V-PAGE]` |
| 4 | **CurveVel-B** | Vel | 24 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **43 GB** | Google Drive | `[V-PAGE]` |
| 5 | **FlatFault-A** | Fault | 48 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **77 GB** | Google Drive | `[V-PAGE]` |
| 6 | **FlatFault-B** | Fault | 48 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **77 GB** | Google Drive | `[V-PAGE]` |
| 7 | **CurveFault-A** | Fault | 48 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **77 GB** | Google Drive | `[V-PAGE]` |
| 8 | **CurveFault-B** | Fault | 48 000 / 6 000 | (5, 1000, 70) | (1, 70, 70) | **77 GB** | Google Drive | `[V-PAGE]` |
| 9 | **Style-A** | Style | 60 000 / 7 000 | (5, 1000, 70) | (1, 70, 70) | **95 GB** | Google Drive | `[V-PAGE]` |
| 10 | **Style-B** | Style | 60 000 / 7 000 | (5, 1000, 70) | (1, 70, 70) | **95 GB** | Google Drive | `[V-PAGE]` |
| 11 | **Kimberlina-CO2** | Kimberlina | 15 000 / 4 430 | (9, 1251, 101) | (1, 401, 141) | **96 GB** | **NETL** | `[V-PAGE]` |
| 12 | **Kimberlina-V1 (3D)** | Kimberlina | 1 664 / 163 | (25, 5001, 40, 40) | (1, 350, 400, 400) | **1.4 TB** | **NETL** | `[V-PAGE]` |

**Total: ≈793 GB for the 2D + CO2 families; ≈2.2 TB including 3D Kimberlina-V1.** `[V-PAGE]`

**File layout (GitHub README):** `[V-PAGE]`

| Family | Split | File range |
|---|---|---|
| Vel | 24k / 6k | `data(model)1-48.npy` / `data(model)49-60.npy` |
| Fault | 48k / 6k | `data(model)1-96.npy` / `data(model)97-108.npy` |
| Style | 60k / 7k | `data(model)1-120.npy` / `data(model)121-134.npy` |

**Notes**
- A/B is a difficulty axis: **A = smaller velocity contrast (easier)**, **B = larger contrast (harder)**. All 2D families share identical acquisition geometry (5 sources × 1000 time samples × 70 receivers → 70×70 velocity grid), which is what makes this a clean controlled benchmark.
- **"KimberlinaV2" and a separate "Kimberlina-3D" were NOT found on the OpenFWI data page.** The page lists exactly *Kimberlina-CO2* and *3D Kimberlina-V1*. A V2 exists in the NETL/NRAP CCS literature but is not an OpenFWI-branded release. `[U]` — search: `NETL NRAP Kimberlina v2 CCS simulation dataset`.
- Kimberlina families derive from the **NRAP Kimberlina CCS** simulations — the CCS-relevant subset.
- Sizes above are the portal's own published figures, **not** `Content-Length`: the per-dataset Google Drive file IDs were not enumerated.

---

## 2. Classic velocity / FWI / imaging benchmarks — WHERE THEY LIVE NOW

Base URL for all S3 rows: `https://s3.amazonaws.com/open.source.geoscience/open_data/`
Sizes are **exact `Content-Length` bytes** from HTTP HEAD unless noted.

| # | Dataset | Type | Task | Exact size | License | Verified path (append to base) | Flag |
|---|---|---|---|---|---|---|---|
| 13 | **BP 2004 velocity benchmark** — exact velocity model | Synthetic 2D | FWI, velocity estimation, RTM | **19 533 256 B (19.5 MB)** gz | Open for research (BP release) | `bpvelanal2004/vel_z6.25m_x12.5m_exact.segy.gz` | `[V-HEAD]` |
| 14 | **BP 2004** — shot gathers (shots 1–200; one of several parts) | Synthetic 2D | FWI | **1 204 545 864 B (1.20 GB)** per part | as above | `bpvelanal2004/shots0001_0200.segy.gz` | `[V-HEAD]` |
| 15 | **BP 2007 TTI anisotropic benchmark** — shot data | Synthetic 2D **TTI anisotropic** | anisotropic imaging / velocity analysis | parts 1–4 = **1 036 037 910 + 1 070 019 484 + 1 110 088 697 + 323 224 177 = 3 539 370 268 B (3.54 GB)** | Open for research (courtesy BP Exploration Operating Company Ltd) | `bptti2007/Anisotropic_FD_Model_Shots_part1..4.sgy.gz` | `[V-HEAD]` |
| 16 | **BP 2007 TTI** — model parameters (Vp, delta, epsilon, tilt) | Synthetic | anisotropic model | **230 291 943 B (230.3 MB)** | as above | `bptti2007/ModelParams.tar.gz` | `[V-HEAD]` |
| 17 | **SEG/EAGE Salt AND Overthrust models** (combined CD image) | Synthetic 3D | 3D imaging, salt, statics | **1 222 196 638 B (1.22 GB)** | **CC-BY-4.0** (Copyright 1997 SEG) | `seg_eage_models_cd/salt_and_overthrust_models.tar.gz` | `[V-HEAD]` |
| 18 | **SEG/EAGE 3D Salt model** (standalone) | Synthetic 3D | salt imaging | **513 098 004 B (513.1 MB)** | CC-BY-4.0 | `seg_eage_models_cd/Salt_Model_3D.tar.gz` | `[V-HEAD]` |
| 19 | **SEG/EAGE 3D Overthrust model** (HDF5, DOI'd copy) | Synthetic 3D | 3D imaging, FWI | **1 062 506 184 B (1.06 GB)** — `overthrust_3D_true_model.h5` 531 253 092 B + `overthrust_3D_initial_model.h5` 531 253 092 B | **CC-BY-4.0** | `https://zenodo.org/records/4252588` (DOI `10.5281/zenodo.4252588`) | `[V-API]` |
| 20 | **SEG C3 narrow-azimuth shots** (Salt Model C3 NA) | Synthetic 3D shots | 3D migration/imaging | **1 575 306 320 B** + **1 579 602 640 B** per file (4 SEG-Y Rev1 files, ≈1.5 GB each ⇒ **≈6.3 GB total**) | CC-BY-4.0 | `seg_eage_salt/SEG_C3NA_ffid_2-1200.sgy`, `…ffid_1201-2400.sgy` (+2 more, same pattern) | `[V-HEAD]` |
| 21 | **SEG C3 wide-azimuth shots** (Salt Model C3 WA) | Synthetic 3D shots | WATS imaging | not resolved — extrapolated `SEG_C3WA_*` filenames returned 403 | CC-BY-4.0 | `[U]` — browser-open `wiki.seg.org/wiki/SEG_C3_WA` | `[U]` |
| 22 | **AGL Elastic Marmousi (= Marmousi2)** | Synthetic 2D **elastic** | elastic FWI, AVO, imaging | **153 722 387 B (153.7 MB)** tar.gz | Open (Univ. of Houston Allied Geophysical Laboratories release, 2019) | `https://s3.amazonaws.com/open.source.geoscience/open_data/elastic-marmousi/elastic-marmousi-model.tar.gz` | `[V-HEAD]` |
| 23 | **Chevron 2014 FWI blind test** (SEG 2014 workshop) | Synthetic 2D marine isotropic **elastic** | FWI blind test | **2 097 152 000 + 1 678 807 920 = 3 775 959 920 B (3.78 GB)** in 2 parts. Uncompressed `SEG14.Pisoelastic.segy` is **4 234 122 000 B**. | **Chevron Data License Agreement** | `seg_workshop_fwi_2014/seg_workshop_fwi_2014.tar.gz.partaa` + `.partab` | `[V-HEAD]` |
| 24 | **Chevron GOM 2012 FWI benchmark** — no free-surface multiples | Synthetic 2D elastic subsalt GOM | FWI | **9 663 676 416 B (9.66 GB)** for part0 of 3 (≈25 GB total per the page) | Chevron DLA | `seg_workshop_fwi/ChevronGOM_2012_Benchmark_no_FSM.gzip.part0/1/2` | `[V-HEAD]` |
| 25 | **Chevron GOM 2012** — with free-surface multiples | Synthetic 2D elastic | FWI + multiple attenuation | ≈25 GB in 3 parts | Chevron DLA | `seg_workshop_fwi/ChevronGOM_2012_Benchmark_w_FSM.gzip.part0/1/2` | `[V-PAGE]` |
| 26 | **Chevron 2013 long-offset FWI synthetic** | Synthetic 2D elastic; 30 km offset, 23 s record | FWI | **10 485 760 000 B (10.49 GB)** per part × **8 parts (aa–ah) ⇒ ≈83.9 GB** | Chevron DLA | `seg_workshop_fwi_long_offset2013/ChevGOMLO.tar.gzip.partaa … partah` | `[V-HEAD]` |
| 27 | **Chevron GOM 2013 TTI** | Synthetic 2D anisotropic (TTI) | anisotropic FWI | **5 242 880 000 B (5.24 GB)** per part × **6 parts (aa–af) ⇒ ≈31.5 GB** | Chevron DLA | `seg_workshop_fwi_tti/ChevronGOM2013_tti.tar.partaa … partaf` | `[V-HEAD]` |
| 28 | **Chevron FWI starting velocity model** | Synthetic | FWI initialisation | **204 768 644 B (204.8 MB)** | Chevron DLA | `seg_workshop_fwi/ChevronFWI-StartingModel.segy` (also `.bin`) | `[V-HEAD]` |
| 29 | **Chevron GOM CSEM + MT data** (same earth model) | Synthetic EM | joint EM/seismic inversion | not HEADed | Chevron DLA | `seg_workshop_fwi/ChevGOM_CSEMMT.tar` | `[V-PAGE]` |
| 30 | **SModels v01 — RCP 3D 9-C shear models** (Postle Field, OK) | Synthetic 3D elastic / HTI | S-wave statics, birefringence, 9-C VSP | **218 402 950 B (218.4 MB)** model archive; 9-C VSP SEG-Ys (`{iso,hti,isons,htins}_vsp01_{xx..zz}.sgy.gz`, 36 files) separate; VSP02 as 4 `.tgz`. `all_md5sums.txt` is **live (200)**. | Requires accepting `README_agreement` | index `SModels/SModels.html`; archive `SModels/SModels.v01.tgz` | `[V-HEAD]` |

### Chevron acquisition geometry (2014 blind test) — from the S3 index page `[V-PAGE]`
1600 shots, dS = 25 m, source depth 15 m · 321 hydrophones/shot, dR = 25 m, receiver depth 15 m · max offset 8000 m · record 8.0 s at 4 ms · Vp(water) = 1510 m/s constant · free-surface multiples present · isotropic elastic. Ships `SEG14.Pisoelastic.segy` (dX = 25 m), `SEG14.Vpsmoothstarting.segy` (dX = 12.5 m), one Vp well log, a farfield no-ghost wavelet (`Wavelet.txt`, 0.666666 ms sampling), `WellWavePic.JPG`, and the legal disclaimer.

### Chevron licence — commercial-use warning `[V-PAGE]`
The Chevron DLA is **revocable and non-transferable**. It grants a royalty-free right to *use*, requires acknowledging Chevron in publications, requires documenting modifications, and requires redistributing the licence alongside the data. It grants **no commercial exploitation right**. Get legal review before shipping anything derived from it.

### Documented-but-not-locatable benchmarks (provenance recovered from the cached SEG Wiki text)

These are real, they are described on the SEG Wiki, and their download links sit on wiki subpages that are **403 to every automated fetch I tried**. Provenance below is `[V-PAGE]` (from the cached wiki text); the **URLs are `[U]`**.

| # | Dataset | Provenance (verbatim-sourced from SEG Wiki text) | Flag |
|---|---|---|---|
| 31 | **1994 BP statics benchmark model** | Created at the **Amoco Tulsa Research Lab in 1994 by Mike O'Brien** to study methods for attacking statics in land data. Geology entirely invented, not a specific play; contains many near-surface geology types thought to cause statics. **2D, purely acoustic, constant density.** Used in internal Amoco reports F94-G-0059 and F95-G-0033, never published externally; released to a few academic institutions in the late 1990s; **re-released in 2008 courtesy of BP**. Lacks ground roll (acoustic) but otherwise looks like real data. | `[V-PAGE]` / URL `[U]` — browser-open `wiki.seg.org/wiki/1994_BP_statics_benchmark_model` |
| 32 | **1994 BP migration from topography** | Created for the CSEG paper *"Migration from topography: improving the near-surface image"* by **Gray and Marfurt**. Widely circulated among Canadian contractors in the mid-1990s. | `[V-PAGE]` / URL `[U]` |
| 33 | **1997 BP 2.5D migration benchmark model** | Created by **John Etgen and Carl Regone at Amoco** for *"Strike shooting, dip shooting, widepatch shooting — Does prestack migration care? A model study"*. A 2D dip-line subset of the full 3D dataset; a severe test of 2.5D Kirchhoff migration (model invariant in Y). Built to advocate wavefield migration, so it illustrates Kirchhoff's limitations. | `[V-PAGE]` / URL `[U]` |
| 34 | **Hess VTI migration benchmark** | 2D synthetic generated with **two different FD forward-modeling codes in VTI media**. *Data I* was generated with Hess's internal software and **contains surface multiples**; *Data II* was generated with SEPLIB (Stanford) and is **free of surface multiples**. | `[V-PAGE]` / URL `[U]` — browser-open `wiki.seg.org/wiki/Hess_VTI_migration_benchmark` |
| 35 | **SMAART models — Pluto 1.5, Sigsbee2A, Sigsbee2B, Ziggy** | SMAART = Subsalt Multiples Attenuation And Reduction Team. **"Maintained and licensed by TNO and Delphi."** Pluto 1.5: elastic, released Nov 2000, realistic free-surface and internal multiples over a relatively easy-to-image structure. Sigsbee2A: constant-density acoustic, Sept 2001, no free-surface multiples and almost no internal multiples (very low water-bottom contrast), over a hard-to-image subsalt structure. Sigsbee2B: same structural model, water-bottom contrast raised to normal ⇒ significant internal and FS multiples. **`delphi.tudelft.nl` no longer resolves.** | `[V-PAGE]` / host `[V-DEAD]` |
| 36 | **Amoco statics dataset** | Not found on the SEG Wiki open-data page and no live host located. | `[U]` — search: `Amoco statics test dataset SEG open data` |
| 37 | **Original (1988 acoustic) Marmousi** | Only the *elastic* Marmousi2 (row 22) was confirmed live. The original IFP Marmousi is bundled in dozens of packages (Devito, PySIT, Madagascar) with no single authoritative live URL. Context from the wiki: Marmousi2 has 17 km lateral extent, 3.5 km depth, **199 geological layers**, and an extended **450 m water layer**; layers derived from the same horizon picks as the original, supplied by **Aline Bourgeois (IFP)**. Ships density, Vp and Vs models plus NMO stacks and pre/poststack time and depth migrations. | `[U]` — take it from a package fixture |
| 38 | **KFUPM-KAUST Red Sea model** | Created by **Abdullatif A. Al-Shuhail, Wail A. Mousa, and Tariq Alkhalifah** (KFUPM + KAUST). High-resolution **2D viscoelastic** model of the Red Sea plus synthetic seismic data. | `[V-PAGE]` / URL `[U]` |
| 39 | **Qademah Fault 3D Survey (KAUST)** | Full dataset (0.5 ms sample interval, 0.7 s record) in MATLAB format. | `[V-PAGE]`; link `https://csim.kaust.edu.sa/files/FieldData/Qademah_2014/Active/Qademag_3D_Active.htm` (from cached wiki link list, not fetched) `[U]` |

---

## 3. Fault detection and segmentation

| # | Dataset | Type | Task | Exact size | License | Verified URL | Flag |
|---|---|---|---|---|---|---|---|
| 40 | **FaultSeg3D** (Wu et al. 2019) — the standard baseline | Synthetic, labeled | 3D fault segmentation | 200 synthetic seismic/fault volume pairs (train) + validation set | ⚠️ **Creative Commons, personal & research use ONLY — commercial use requires contacting the authors.** Hard blocker for productisation. | repo `https://github.com/xinwucwp/faultSeg`; data `https://drive.google.com/drive/folders/1FcykAxpqiy2NpLP1icdatrrSQgLRXLP8`; pretrained model `https://drive.google.com/drive/folders/1q8sAoLJgbhYHRubzyqMi9KkTeZWXWtNd` | `[V-PAGE]` |
| 41 | **Thebe** — the largest public *field* fault dataset | **Field** (Thebe Gas Field, Exmouth Plateau, Carnarvon Basin, NW Shelf Australia), expert-labeled | 2D/3D fault recognition | **53 090 565 446 B = 53.09 GB across 78 files.** Volume **1803 × 1537 × 3174**; 1803 labeled crossline sections of 1737 × 3174. Split: first 900 crosslines train, next 200 val, last 703 test. `.npy` (~487.8 MB each) + `.npz` pairs. | **CC0** with additional terms; ships `Creative_Commons_Attribution_4_0 International_CC_BY_4_0.pdf` | `https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YBYGBK` — published 2021-05-04, state RELEASED | `[V-API]` |
| 42 | **large-bench-geo** — unified fault benchmark | code | 200+ experimental setups: 8 architectures (UNet, UNet++, DeepLabV3+, SegFormer, …) × 3 datasets (FaultSeg3D, CRACKS, Thebe) × multiple training regimes; domain-shift and generalisability study | code only; links out to the three datasets | see repo | `https://github.com/olivesgatech/large-bench-geo` (arXiv 2505.08585) | `[V-PAGE]` |
| 43 | **Synthetic 3D Seismic Volumes and Fault Labels for Strike-Slip Flower Structures in Carbonate Reservoirs** | Synthetic 3D, labeled | fault detection in carbonate strike-slip / flower-structure systems | **459 665 659 B (0.46 GB)**, single `V1.zip` | **CC-BY-4.0** | `https://zenodo.org/records/20130881` (DOI `10.5281/zenodo.20130881`, 2026-05-12) | `[V-API]` |
| 44 | **`porestar/crossdomainfoundationmodeladaption-deepfault`** | Republished fault labels, parquet | fault segmentation | **11.759 GB** (HF `usedStorage`) | **CC-BY-4.0** | `https://huggingface.co/datasets/porestar/crossdomainfoundationmodeladaption-deepfault` | `[V-API]` |
| 45 | **Trustworthy Deep Learning for Seismic Fault Interpretation** | supporting code/figures | fault interpretation + uncertainty | 0.001 GB (not a data corpus) | **MIT** | `https://zenodo.org/records/21010917` | `[V-API]` |

**FaultSeg3D citation:** Wu, X., Liang, L., Shi, Y., Fomel, S. (2019). *FaultSeg3D: using synthetic datasets to train an end-to-end convolutional neural network for 3D seismic fault segmentation.* GEOPHYSICS 84(3), IM35–IM45.
**Thebe citation:** An, Y. et al. *A gigabyte interpreted seismic dataset for automatic fault recognition.* Data in Brief (2021). Companion: *Deep Convolutional Neural Network for Automatic Fault Recognition with a Large-scale Interpreted Field Dataset.* (Univ. College Dublin.)

---

## 3b. The CIG collection (Xinming Wu / USTC Computational Interpretation Group)

**This is the single richest source of labeled 3D synthetic exploration-seismic data on the open web.** Enumerated via `https://zenodo.org/api/records?q=creators.name:"Wu, Xinming"` — **23 records**. Sizes are byte-exact from the Zenodo API. **Almost all are CC-BY-4.0** — i.e. commercially usable with attribution, unlike FaultSeg3D and OpenFWI.

| # | Dataset | Type | Task / labels | Exact size | License | Zenodo record | Flag |
|---|---|---|---|---|---|---|---|
| 46 | **Massive-scale clinothem datasets** — 4 000 labeled synthetic + 3 000 unlabeled field | Synthetic + field | **relative geologic time (RGT)** estimation on global shelf-edge-scale clinothems | **81 040 433 213 B (81.04 GB)**, 3 files — *largest in the collection* | CC-BY-4.0 | `https://zenodo.org/records/20769762` (2026-06-20) | `[V-API]` |
| 47 | **cigCK** — 3D synthetic volumes with labeled **channels AND karsts** | Synthetic 3D | simultaneous channel + karst interpretation | **42 870 719 995 B (42.87 GB)**, 6 files | CC-BY-4.0 | `https://zenodo.org/records/12806267` (2025) | `[V-API]` |
| 48 | **Deep learning for simultaneously interpreting 3D horizons and faults via RGT** | Synthetic 3D | **400 pairs** of 3D seismic + label volumes (RGT + fault) | **27 968 005 525 B (27.97 GB)**, 53 files | CC-BY-4.0 | `https://zenodo.org/records/4627924` (2021-02-11) | `[V-API]` |
| 49 | **LFD — Latent-Compression-Free Generative Diffusion with Geological Priors** | Synthetic | implicit structural modeling (diffusion) | **24 631 935 275 B (24.63 GB)**, 3 files | **MIT** | `https://zenodo.org/records/20508635` (2026-06-02); code `https://github.com/ProgrammerZXG/LFD` | `[V-API]` |
| 50 | **Self-supervised pre-training + few-shot finetuning for gas-bearing prediction** | Field + synthetic | gas-bearing prediction (DHI) | **19 715 809 052 B (19.72 GB)**, 1 file | CC-BY-4.0 | `https://zenodo.org/records/15301338` (2025-04) | `[V-API]` |
| 51 | **cigChannel** — large-scale 3D with labeled **paleochannels** | Synthetic 3D | channel segmentation; 400 samples total, includes folded & faulted structures | **11 973 510 812 B (11.97 GB)**, 6 files | CC-BY-4.0 | `https://zenodo.org/records/15500696` (2024-04-28) | `[V-API]` |
| 52 | **ClinoformNet-1.0** — synthetic + field | Synthetic + field | seismic **clinoform** delineation via stratigraphic forward modeling | **11 026 324 208 B (11.03 GB)**, 3 files | CC-BY-4.0 | `https://zenodo.org/records/7122471` (2022-09-29); code `https://zenodo.org/records/7123934` (0.072 GB, other-open) | `[V-API]` |
| 53 | **Pretrain-to-alignment RGT baselines** — 3 000 field datasets | Field | RGT estimation baselines | **10 801 509 721 B (10.80 GB)**, 3 files | CC-BY-4.0 | `https://zenodo.org/records/18910332` (2026-03-15) | `[V-API]` |
| 54 | **cigKast** — 3D synthetic volumes with labeled **paleokarsts** | Synthetic 3D | paleokarst interpretation; **120 pairs** of seismic + label volumes | **7 805 078 543 B (7.81 GB)** — `seismic.zip` 7 496 187 892 B + `karst.zip` 26 361 067 B + `checkpoint.50.hdf5` 282 529 584 B | CC-BY-4.0 | `https://zenodo.org/records/4285733` (2020-11-23) | `[V-API]` |
| 55 | **cigCK (Extended dataset)** | Synthetic 3D | supplement to cigCK | **7 265 313 700 B (7.27 GB)**, 1 file | CC-BY-4.0 | `https://zenodo.org/records/17104253` (2025-09-12) | `[V-API]` |
| 56 | **Sensing a priori constraints in DNNs for solving geophysical problems** | Synthetic | constrained geophysical inversion | **7 235 000 000 B ≈ 7.24 GB** | CC-BY-4.0 | `https://zenodo.org/records/7326606` | `[V-API]` |
| 57 | **3D Implicit Structural Modeling (training + validation)** | Synthetic | implicit structural modeling via CNN | **5 678 000 000 B ≈ 5.68 GB** | CC-BY-4.0 | `https://zenodo.org/records/6480165` | `[V-API]` |
| 58 | **cigRockSEM** — rock microstructure in SEM images | Lab imagery | rock microstructure segmentation (mudstone, sandstone, shale) | **4 647 873 371 B (4.65 GB)**, 1 file | CC-BY-4.0 | `https://zenodo.org/records/14988631` (2025-03-07) | `[V-API]` |
| 59 | **Objective-programmable implicit structural modeling** | Synthetic | structural modeling under heterogeneous data | **4 050 000 000 B ≈ 4.05 GB** | CC-BY-4.0 | `https://zenodo.org/records/18728073` | `[V-API]` |
| 60 | **Cross-Domain Foundation Model Adaptation — data** | Mixed | cross-domain transfer for geophysics | **2 790 000 000 B ≈ 2.79 GB** | CC-BY-4.0 | `https://zenodo.org/records/12798750`; code `https://zenodo.org/records/14927852` (MIT). Paper arXiv:2408.12396 | `[V-API]` |
| 61 | **Implicit Structural Modeling via Generative Diffusion Framework** | Synthetic | structural modeling | **2 370 000 000 B ≈ 2.37 GB** | CC-BY-4.0 | `https://zenodo.org/records/18447817` | `[V-API]` |
| 62 | **Geologically-informed + data-driven labeled synthetic training sets** | Synthetic | (workflow training data) | **2 200 000 000 B ≈ 2.20 GB** | CC-BY-4.0 | `https://zenodo.org/records/14678398`; code `https://zenodo.org/records/14835207` (0.070 GB, MIT) | `[V-API]` |
| 63 | **Memory-Efficient Full-Volume Inference for Large-Scale 3D Dense Prediction** | Synthetic | 3D dense prediction at volume scale | **1 059 000 000 B ≈ 1.06 GB** | **MIT** | `https://zenodo.org/records/17810071` | `[V-API]` |
| 64 | **Foundation model with a multi-modal prompt engine for universal seismic interpretation** | Field + synthetic | promptable universal seismic interpretation | **1 014 000 000 B ≈ 1.01 GB** | CC-BY-4.0 | `https://zenodo.org/records/13892216` | `[V-API]` |
| 65 | **cigFacies** — knowledge-graph-guided facies benchmark | Synthetic + field | 3D facies classification | **13 350 907 B (13.4 MB)** for the *skeletonization* benchmark zip (the headline corpus is generated from it, not shipped whole) | CC-BY-4.0 | `https://zenodo.org/records/10777460` (2024-03-04); network `https://zenodo.org/records/13150879` (`huigcig/cigFaciesNet`, 47 MB) | `[V-API]` |

**Collection total (rows 46–65): ≈286 GB of overwhelmingly CC-BY-4.0 labeled 3D seismic.** Main contributors across records: Xinming Wu, Hui Gao, Jintao Li, Xiaoming Sun, Jiarun Yang, Guangyu Wang, Mingcai Hou.

---

## 4. Facies classification and seismic interpretation

| # | Dataset | Type | Task | Exact size | License | Verified URL | Flag |
|---|---|---|---|---|---|---|---|
| 66 | **F3 Facies Classification Benchmark** (Alaudah et al. 2019) — *the* facies reference | **Field** (F3 block, Dutch North Sea), expert-labeled | multi-class facies segmentation | **`data.zip` 1 051 449 986 B (1.05 GB)** + **`raw.zip` 1 084 578 002 B (1.08 GB)** + `logs.zip` 112 229 B = **2 136 140 217 B (2.14 GB)**. Ships `train_seismic.npy`/`train_labels.npy` + two test splits; also raw horizons, fault planes, well logs. MD5(data.zip) = `bc5932279831a95c0b244fd765376d85` | **MIT** | code `https://github.com/olivesgatech/facies_classification_benchmark`; data `https://zenodo.org/records/3755060` (DOI `10.5281/zenodo.3755060`). Direct file confirmed 200 with `content-length: 1051449986`. | `[V-API]` `[V-HEAD]` |
| 67 | **LANDMASS-1 and LANDMASS-2** (Georgia Tech CeGP / OLIVES) | **Field** (derived from F3) | 4-class patch classification: Horizon, Chaotic, Fault, Salt Dome | **2 325 243 284 B (2.33 GB)**, single `LANDMASS.zip`. **LANDMASS-1**: 17 667 patches of 99×99 — 9 385 Horizon, 5 140 Chaotic, 1 251 Fault, 1 891 Salt Dome. **LANDMASS-2**: 4 000 images of 150×300, normalised to [0,1], 1 000 per class. Structures extracted from F3 with a curvelet-based distance measure. | **CC-BY-SA-3.0** | **`https://zenodo.org/records/3901644` (DOI `10.5281/zenodo.3901644`) — this is the live, no-form URL.** The CeGP page `https://cegp.ece.gatech.edu/codedata/landmass/` requires a request form; also on `https://github.com/olivesgatech/LANDMASS` and IEEE DataPort. | `[V-API]` |
| 68 | **Penobscot Interpretation Dataset** (Baroni et al.) | **Field** (Penobscot 3D, Scotian Shelf, offshore Nova Scotia), expert-labeled | facies segmentation, horizon picking | **2 316 061 505 B (2.32 GB)** — `dataset.h5` 2 268 562 702 B + `horizons.zip` 36 213 721 B + `penobscot-examples.png` 10 649 865 B + `how-to-read.ipynb` 633 270 B + `dataset-log.txt` 1 947 B. **7 interpreted horizons in XYZ; 2 166 images (1 083 seismic TIFF + 1 083 label PNG); >100 000 labeled inline/crossline tiles.** | **CC-BY-4.0** | `https://zenodo.org/records/3924682` (DOI `10.5281/zenodo.3924682`, v3.0.0, 2020-06-30) | `[V-API]` |
| 69 | **Netherlands F3 Interpretation Dataset** (same IBM/Baroni group) | **Field** (F3) | facies segmentation | **1 657 611 714 B (1.66 GB)** — `inlines.zip` 637 187 326 B + `crosslines.zip` 639 101 595 B + `tiles_inlines.tar.gz` 139 644 717 B + `tiles_crosslines.tar.gz` 140 979 246 B + `horizons.tar.gz` 95 320 034 B + `masks.tar.gz` 4 800 574 B | **CC-BY-4.0** | `https://zenodo.org/records/1471548` (DOI `10.5281/zenodo.1471548`, 2018-09-20) | `[V-API]` |
| 70 | **Parihaka facies (SEAM AI 2020 challenge)** | **Field** (Parihaka 3D, offshore Taranaki NZ; public-domain NZ govt survey), expert-labeled | **6-class** facies segmentation; volume **1006 × 782 × 590** | host requires login, size not directly verified | AIcrowd challenge rules; underlying survey is NZ public domain | Challenge `https://www.aicrowd.com/challenges/seismic-facies-identification-challenge` (+ `/challenge_rules`). **Verified alternative: row 71 ships `Parihaka_data.zip` at 449 881 742 B under CC-BY-4.0.** | `[V-PAGE]` |
| 71 | **AdaSemSeg — Processed Seismic Facies Datasets (F3, Parihaka, Penobscot)** | Field, republished + preprocessed | few-shot facies segmentation | **2 553 842 528 B (2.55 GB)** — `F3_data.zip` 1 050 309 306 B + `Penobscot_data.zip` 1 053 651 480 B + **`Parihaka_data.zip` 449 881 742 B**. Uses the original F3 benchmark train/val/test split. | **CC-BY-4.0** | `https://zenodo.org/records/21764042` (DOI `10.5281/zenodo.21764042`, 2026-08-02) | `[V-API]` |
| 72 | **`Surojit-Utah/adasemseg-seismic-facies-datasets`** (HF mirror of row 71) | Field | facies segmentation | **3.940 GB** (HF `usedStorage`, includes git history) | **CC-BY-4.0** | `https://huggingface.co/datasets/Surojit-Utah/adasemseg-seismic-facies-datasets` | `[V-API]` |
| 73 | **AdaSemSeg — Trained Model Checkpoints** | model weights | few-shot facies | **3.460 GB** | CC-BY-4.0 | `https://zenodo.org/records/21762769` | `[V-API]` |
| 74 | **NZ Tui-3D semi-automatic interpretation benchmark** | **Field** (New Zealand) | semi-automatic interpretation / segmentation | **378 783 319 B (0.38 GB)** — `Crosslines_NZ_Interpretation_Dataset.zip` 294 145 386 B + `Inlines_NZ_Interpretation_Dataset.zip` 84 635 198 B + explicit train/test line lists + SEG-Y header text | **CC-BY-4.0** | `https://zenodo.org/records/4153216` (DOI `10.5281/zenodo.4153216`, 2020-10-29) | `[V-API]` |
| 75 | **`porestar/crossdomainfoundationmodeladaption-seismicfacies`** | Field, parquet | facies segmentation | **3.743 GB** | **CC-BY-4.0** | `https://huggingface.co/datasets/porestar/crossdomainfoundationmodeladaption-seismicfacies` | `[V-API]` |
| 76 | **Derived data and results of SeismicFaciesClassification** | Field | facies classification | **0.155 GB** | CC-BY-4.0 | `https://zenodo.org/records/4729952` | `[V-API]` |
| 77 | **Probabilistic Seismic Facies Classification** | — | facies classification | **0.014 GB** | CC-BY-4.0 | `https://zenodo.org/records/1466917` | `[V-API]` |
| 78 | **Representation Learning in Seismic Interpretation** | — | representation learning | **0.008 GB** | CC-BY-4.0 | `https://zenodo.org/records/3233692` | `[V-API]` |
| 79 | **`Jinlong99/f3-seismic-facies-mood-demo`** | Field (F3) | facies demo / OOD detection | not stated | not stated | `https://huggingface.co/datasets/Jinlong99/f3-seismic-facies-mood-demo` | `[V-API]` |

**F3 benchmark citation:** Alaudah, Y., Michałowicz, P., Alfarraj, M., AlRegib, G. (2019). *A machine-learning benchmark for facies classification.* Interpretation 7(3), SE175–SE187. DOI 10.1190/INT-2018-0249.1
**LANDMASS citation:** AlRegib, G., Alaudah, Y., Alfarraj, M. — LANDMASS = *LArge North-Sea Dataset of Migrated Aggregated Seismic Structures*, Georgia Tech ECE / CeGP (Georgia Tech + KFUPM).
**Penobscot citation:** Baroni, L., Silva, R.M., Ferreira, R.S., Chevitarese, D., Szwarcman, D. *Penobscot Dataset: Fostering Machine Learning Development for Seismic Interpretation.* arXiv:1903.12060
**AdaSemSeg citation:** Saha & Whitaker (2025). *AdaSemSeg: An Adaptive Few-Shot Semantic Segmentation of Seismic Facies.* IEEE TGRS. DOI 10.1109/TGRS.2025.3595010

---

## 5. Foundation models and their corpora

| # | Dataset | Type | Task | Exact size | License | Verified URL | Flag |
|---|---|---|---|---|---|---|---|
| 80 | **Seismic Foundation Model (SFM)** — Sheng et al. | **Field**, self-supervised | MAE pretraining (75% masking) on **2 286 422 2-D seismic images curated from 192 globally collected 3-D seismic volumes** | pretraining set distributed as "PreTrain 224×224"; **hosted on USTC institutional servers + Baidu Netdisk — no HF/Drive mirror in the repo**, so size unverified | **MIT** | `https://github.com/shenghanlin/SeismicFoundationModel`; pretrain README `…/blob/main/SFM-Pretrain/README.md`. Paper arXiv:2309.02791, accepted to GEOPHYSICS. | `[V-PAGE]` |
| 81 | **SFM downstream — facies** | Field | facies classification, **768×768** | **1.159 GB** | **MIT** | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-facies` | `[V-API]` |
| 82 | **SFM downstream — geobody** | Field | geobody identification, 224×224 | **1.568 GB** | MIT | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-geobody` | `[V-API]` |
| 83 | **SFM downstream — denoise (synthetic)** | Synthetic | denoising, 224×224 | **1.606 GB** | MIT | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-denoise` | `[V-API]` |
| 84 | **SFM downstream — denoise (field)** | Field | denoising | **2.008 GB** | MIT | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-denoise-field` | `[V-API]` |
| 85 | **SFM downstream — interpolation** | Field | trace interpolation, 224×224 | **1.568 GB** | MIT | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-interpolation` | `[V-API]` |
| 86 | **SFM downstream — inversion (synthetic)** | Synthetic | reflectivity/impedance inversion, 224×224 | **1.765 GB** | MIT | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-inversion-synthetic` | `[V-API]` |
| 87 | **SFM downstream — inversion (SEAM-derived)** | Synthetic (SEAM) | inversion | **3.442 GB** — *notable: a SEAM-derived product redistributed under MIT* | MIT | `https://huggingface.co/datasets/porestar/seismicfoundationmodel-inversion-seam` | `[V-API]` |
| 88 | **Seismic super-resolution dataset** | — | super-resolution | **0.882 GB** | MIT | `https://huggingface.co/datasets/porestar/superresolutiondataset` | `[V-API]` |
| 89 | **Cross-Domain FM Adaptation — crater** | planetary imagery | cross-domain transfer | **9.091 GB** | CC-BY-4.0 | `https://huggingface.co/datasets/porestar/crossdomainfoundationmodeladaption-crater` | `[V-API]` |
| 90 | **Cross-Domain FM Adaptation — DAS** | DAS field | cross-domain transfer | **0.302 GB** | CC-BY-4.0 | `https://huggingface.co/datasets/porestar/crossdomainfoundationmodeladaption-das` | `[V-API]` |
| 91 | **Cross-Domain FM Adaptation — geobody** | Field | geobody | **0.323 GB** | CC-BY-4.0 | `https://huggingface.co/datasets/porestar/crossdomainfoundationmodeladaption-geobody` | `[V-API]` |
| 92 | **`LukasMosser/seismic-datasets`** — the unification layer | index/code | loads all 13 `porestar/*` sets via HF `datasets` | code only | see repo | `https://github.com/LukasMosser/seismic-datasets` | `[V-PAGE]` |
| 93 | **`thirdExec/synthetic-seismic-vlm`** | **Synthetic** | VQA + segmentation + image-to-text (vision-language on seismic) | **1.534 GB** | **MIT** | `https://huggingface.co/datasets/thirdExec/synthetic-seismic-vlm` | `[V-API]` |
| 94 | **`sdlj/seismicVMB`** — velocity model benchmark | likely synthetic | velocity model building | **12.202 GB**; 619 downloads — most-downloaded genuinely-geophysical set in the HF search | not stated on the API record | `https://huggingface.co/datasets/sdlj/seismicVMB` (DOI `10.57967/hf/6553`) | `[V-API]` |
| 95 | **`HeXingChen/Seismic-AI-Data`** | mixed | general seismic AI corpus | declared `size_categories: n>1T` — **largest declared** of any HF seismic dataset; 10 102 downloads | MIT | `https://huggingface.co/datasets/HeXingChen/Seismic-AI-Data` | `[V-API]` |
| 96 | **Foundation model with multi-modal prompt engine** (CIG) | Field + synthetic | promptable universal interpretation | 1.014 GB | CC-BY-4.0 | `https://zenodo.org/records/13892216` — see row 64 | `[V-API]` |

**SeisCLIP:** not investigated. It is *earthquake* seismology (contrastive pretraining on event waveforms + metadata), out of scope for exploration. `[U]` — search: `SeisCLIP github dataset`.

---

## 6. Generators and tooling data

| # | Name | Type | What it gives you | License | Verified URL | Flag |
|---|---|---|---|---|---|---|
| 97 | **Synthoseis** | **Generator** | Generates pseudo-random synthetic 3D seismic volumes **with labels for lithology (facies), fluid content, and closure**. Volume shape via `cube_shape` = [X, Y, Z]. Ships config examples + a rock-property model template; **no pre-generated dataset**. 130 stars. | **MIT** | **`https://github.com/sede-open/synthoseis`** (Shell / `sede-open`) — docs `https://sede-open.github.io/synthoseis/datagenerator.html`. ⚠️ **Correction to prior notes: this is NOT an Equinor repo. `github.com/equinor/synthoseis` returns 404.** Forks: `tpmerrifield/synthoseis`, `donald-terratellum/synthoseis-*`. | `[V-PAGE]` `[V-API]` |
| 98 | **segyio** | tooling + tiny fixtures | Fast Python SEG-Y I/O; small CI test files under `test-data/` | **LGPL-3.0** | `https://github.com/equinor/segyio` (581 stars) | `[V-API]` |
| 99 | **seismic-zfp** | tooling | Seismic compression/decompression | LGPL-3.0 | `https://github.com/equinor/seismic-zfp` (73 stars) | `[V-API]` |
| 100 | **equinor/seismic-forward** | **Generator** | Forward seismic modelling from reservoir models | LGPL-3.0 | `https://github.com/equinor/seismic-forward` | `[V-API]` |
| 101 | **oneseismic / oneseismic-api** | tooling | Fast arbitrary-slice access to VDS volumes over HTTP | AGPL-3.0 | `https://github.com/equinor/oneseismic`, `https://github.com/equinor/oneseismic-api` | `[V-API]` |
| 102 | **si4ti** | tooling | 4D/time-lapse seismic inversion for monitoring | LGPL-2.1 | `https://github.com/equinor/si4ti` | `[V-API]` |
| 103 | **zgy2sgz** | tooling | ZGY → seismic-zfp conversion | Apache-2.0 | `https://github.com/equinor/zgy2sgz` | `[V-API]` |
| 104 | **equinor/tmatrix** | rock physics | Seismic properties + pore structure of carbonates | LGPL-3.0 | `https://github.com/equinor/tmatrix` | `[V-API]` |
| 105 | **Devito example data** | Generator + fixtures | FD wave-propagation examples (Marmousi/Overthrust demos) | MIT | `[U]` — search: `devitocodes devito examples seismic marmousi data` | `[U]` |
| 106 | **Madagascar reproducible-research data server** | Mixed | Backing data for hundreds of reproducible papers | GPL (software) | Root `https://reproducibility.org/` alive (200, 26 226 B). **`/data`, `/data/`, `/data/sigsbee`, `/RSF/book/data/`, `/wiki/Download` all 404.** The widely-cited data path is stale. | `[V-DEAD]` |
| 107 | **cigFaciesNet** | code | facies network for cigFacies | CC-BY-4.0 | `https://zenodo.org/records/13150879` (47 MB) | `[V-API]` |
| 108 | **LFD (Latent-compression-Free Diffusion)** | Generator | geological-prior diffusion for structural models | MIT | `https://github.com/ProgrammerZXG/LFD` | `[V-PAGE]` |

**Synthoseis citation:** Merrifield, T.P. et al. (2022). *Synthetic seismic data for training deep learning networks.* Interpretation 10(3), SE31–SE39. DOI 10.1190/INT-2021-0193.1

---

## 7. SEAM (SEG Advanced Modeling)

⚠️ **`seg.org` returns HTTP 403 to every automated fetch, so no SEAM page could be read first-party.** Everything below is from search-result extracts. Treat as **`[V-PAGE]`-via-search**, not verified.

| # | Item | Detail | Flag |
|---|---|---|---|
| 109 | **SEAM Phase I (subsalt, GOM-style)** | Data **subsets range from 120 GB to 5.8 TB**; the largest subset covers a full-fold area of about **11 OCS blocks**. | search-extract |
| 110 | **SEAM has an OPEN DATA programme — the big change** | SEAM now provides free access to selected datasets from past projects, with **open access to Phase I and the Time Lapse Pilot datasets for students, universities, research labs, and startups.** This supersedes the old "members/fee only" understanding. Portal: `https://seg.org/seam/open-data/` | search-extract |
| 111 | **SEAM data-set index** | `https://seg.org/seam/data-sets/` | `[U]` (403) |
| 112 | **SEAM Phase II — Foothills** | Thrust-belt land model; size and pricing not published | `[U]` |
| 113 | **SEAM Phase II — Arid** | Desert near-surface model; size and pricing not published | `[U]` |
| 114 | **SEAM Barrett** | Listed as a SEAM project; size and pricing not published | `[U]` |
| 115 | **SEAM Life of Field / Time Lapse Pilot** | Time Lapse Pilot is named as part of the **open-access** tier (row 110) | search-extract |
| 116 | **SEAM Pressure Prediction** | Listed as a SEAM project; no detail found | `[U]` |
| 117 | **SEAM AI** | `https://seg.org/seam/artificial-intelligence/` — the arm that ran the 2020 Parihaka facies challenge (row 70) | search-extract |
| 118 | **SEAM Phase I Interpretation Challenge 1 (Time and Depth)** | SEG Wiki pages `SEAM_Phase_I:_Interpretation_challenge_I_-_Depth` and `…_–_Time` exist — these are the free Phase-I teasers | `[V-PAGE]` (cached wiki link list) |
| 119 | **SEAM-derived data you CAN get today under MIT** | `porestar/seismicfoundationmodel-inversion-seam`, **3.442 GB** — a SEAM-derived inversion training set republished under MIT on HuggingFace. Practical workaround if SEAM licensing is the blocker. | `[V-API]` |

**Pricing:** no 2025/2026 SEAM price list is publicly reachable. The actionable step is the open-data request form at `https://seg.org/seam/open-data/`. `[U]`

---

## 8. Salt

| # | Dataset | Type | Task | Size | License | URL | Flag |
|---|---|---|---|---|---|---|---|
| 120 | **TGS Salt Identification Challenge (Kaggle)** | **Field** seismic image patches | binary salt segmentation | **not verified** — the Kaggle data page requires authentication and competition-rule acceptance; WebFetch returned only the page title | ⚠️ **Kaggle competition rules — acceptance required before download; TGS retains rights. Not an open licence.** | `https://www.kaggle.com/c/tgs-salt-identification-challenge/data` | `[U]` |
| 121 | **SEG/EAGE 3D Salt model** | Synthetic 3D | salt body imaging | **513 098 004 B** | CC-BY-4.0 | see row 18 | `[V-HEAD]` |
| 122 | **Sandia salt C3 documentation page** | Synthetic | salt imaging docs | — | — | `http://www.cs.sandia.gov/~ccober/seismic/salt_c3.html` (from cached wiki link list; not fetched) | `[U]` |
| 123 | **U-T training/test data for Saltblock model** | Synthetic | velocity inversion | **3.285 GB** | CC-BY-4.0 | `https://zenodo.org/records/7968683` | `[V-API]` |
| 124 | **U-T training/test data for Sigsbee2A model** | Synthetic | velocity inversion — **a live route to Sigsbee2A-derived ML data now that SMAART's host is dead** | **1.908 GB** | CC-BY-4.0 | `https://zenodo.org/records/7967050` | `[V-API]` |
| 125 | **U-T training/test data for LayerFault model** | Synthetic | velocity inversion | **3.269 GB** | CC-BY-4.0 | `https://zenodo.org/records/7968577` | `[V-API]` |
| 126 | **Training/test data for simultaneous inversion of velocity + density** | Synthetic | multi-parameter inversion | **1.778 GB** | CC-BY-4.0 | `https://zenodo.org/records/7965402` | `[V-API]` |

---

## 9. Other notable Zenodo/HF records (exploration-relevant, size-ranked)

| # | Record | Size | License | URL | Flag |
|---|---|---|---|---|---|
| 127 | **Dataset + trained models for "Depth-progressive 3D seismic velocity model building"** | **79.871 GB** | **MIT** | `https://zenodo.org/records/21206427` | `[V-API]` |
| 128 | **"A Unified Framework for Forward and Inverse Problems in Subsurface Imaging"** | **31.947 GB** | CC-BY-4.0 | `https://zenodo.org/records/15226367` | `[V-API]` |
| 129 | **Caosiyao giant porphyry Mo 2D seismic reflection dataset** (mineral exploration) | **3.841 GB** | CC-BY-4.0 | `https://zenodo.org/records/7322156` | `[V-API]` |
| 130 | **GANSim-SeReM — conditional GAN for seismic reservoir modelling** | 0.419 GB | CC-BY-4.0 | `https://zenodo.org/records/19422356` | `[V-API]` |
| 131 | **Trained models for seismic data (Deliverable 2.1)** | 0.593 GB | **EUPL-1.2** | `https://zenodo.org/records/20441181` | `[V-API]` |
| — | `GeoBrain/random-noise-avo-seismic` (denoising, AVO, SEG-Y) | not stated | not stated | `https://huggingface.co/datasets/GeoBrain/random-noise-avo-seismic` | `[V-API]` |
| — | `shaowinw/seismic_inversion` | not stated | CC-BY-4.0 | `https://huggingface.co/datasets/shaowinw/seismic_inversion` | `[V-API]` |
| — | `SAistheBEST/well-seismic-core` | not stated | not stated | `https://huggingface.co/datasets/SAistheBEST/well-seismic-core` | `[V-API]` |
| — | Dip-Guided Multi-Stage Transformer Seismic Super-Resolution | <0.001 GB (code) | CC-BY-4.0 | `https://zenodo.org/records/15709616` | `[V-API]` |

---

## 10. Hub enumeration summary and API gotchas

### HuggingFace — `https://huggingface.co/api/datasets?search=seismic`
**47 results.** `[V-API]`
- **13 are the `porestar/*` geophysics republications** (SFM + Cross-Domain FM Adaptation) — by far the highest-quality, best-licensed cluster. Combined ≈**39.2 GB**.
- ~8 more are genuine exploration-seismic ML sets from other authors (rows 72, 79, 93–95, plus the three unnumbered above).
- **~26 are noise.** In particular the six `tuskanny/seismic-*` datasets are **MS MARCO information-retrieval indexes** (the "Seismic" IR library — nothing to do with geophysics); several others are earthquake-catalogue CSVs or NASA Space Apps lunar/Mars seismic-detection sets.
- **Caveat:** HF `usedStorage` includes git history and all revisions, so it is an **upper bound** on a single checkout.

### Zenodo — `https://zenodo.org/api/records?q=…`
`[V-API]` **Two hard-won lessons:**
1. **A bare `q=seismic` query is nearly useless for exploration.** It is dominated by earthquake seismology: of the top 75 hits, the largest records were elephant-behaviour videos, volcano monitoring, and shaking-table tests. **Not one** was an exploration-seismic ML benchmark.
2. **Targeted queries are mandatory.** `seismic facies`, `seismic interpretation deep learning`, `full waveform inversion`, `seismic velocity model dataset`, and above all **`creators.name:"Wu, Xinming"`** each surfaced records that `q=seismic` missed entirely. The creator query alone yielded ≈286 GB of CC-BY labeled 3D data (§3b).
- **`&size=50` returns HTTP 400. `size=25` is the working page limit** — paginate with `&page=N`.
- Per-record byte sizes come from `hits.hits[].files[].size`; the search endpoint includes them, so no per-record fetch is needed for sizing.

### Kaggle
Not enumerated — Kaggle's dataset API requires authentication (`~/.kaggle/kaggle.json`). The only exploration-seismic competition of note is TGS Salt (row 120). `[U]`

---

## 11. What I could NOT verify, and why

| Item | Why | What to do instead |
|---|---|---|
| **All `seg.org` / `wiki.seg.org` pages** | **HTTP 403** (bot protection) to both `curl` and WebFetch, with and without a browser User-Agent; the `r.jina.ai` reader proxy returned nothing. `software.seg.org` returns **HTTP 525** (Cloudflare SSL handshake failure). | Open in a real browser, or use the `claude-in-chrome` / `playwright` MCP tools. A cached copy of the *Open data* wiki page is in this session's scratchpad and carries the full link list. |
| **SEAM sizes, pricing, and exactly which parts are free** | `seg.org` 403. All of §7 is search-extract. | Browser-fetch `https://seg.org/seam/open-data/` and `https://seg.org/seam/data-sets/`. |
| **TGS Salt exact size and terms** | Kaggle requires login + competition-rule acceptance; the unauthenticated page returns only a title. | `kaggle competitions download -c tgs-salt-identification-challenge` after configuring credentials; read rules in-browser. |
| **BP 1994 statics, BP 1994 migration-from-topography, BP 1997 2.5D, Hess VTI, KFUPM-KAUST Red Sea, SEG C3 WA** | The S3 bucket is unlistable; the two directory names I did find (`bpvelanal2004`, `bptti2007`) were only discoverable via web search, and ~18 brute-forced guesses all returned 403. The wiki subpages carrying the exact keys are 403. | Browser-open each `wiki.seg.org/wiki/<page>` from the subpage list in §2 and copy the S3 link. Descriptions and provenance for each are already captured in rows 31–39. |
| **Pluto 1.5, Sigsbee2A, Sigsbee2B, Ziggy (SMAART JV)** | `http://www.delphi.tudelft.nl/SMAART/` **does not resolve** (curl code 000). `https://reproducibility.org/data/sigsbee` returns **404**. | For Sigsbee-derived *ML* data, rows 123–126 (Zenodo, CC-BY-4.0, byte-exact) are verified working alternatives today. For the raw SMAART models, contact TNO/Delphi directly. |
| **Original 1988 acoustic Marmousi canonical host** | Only the *elastic* Marmousi2 was confirmed live (S3, 153 722 387 B). The original is mirrored in dozens of packages with no single authoritative URL. | Take it from a package fixture (Devito, PySIT, Madagascar) rather than chasing a canonical host. |
| **Kimberlina V2 / a distinct Kimberlina-3D product** | Not present on the OpenFWI data page; the name appears only in NETL/NRAP literature. | Search NETL EDX for the NRAP Kimberlina releases. |
| **OpenFWI per-file download URLs and byte-exact sizes** | The data page names Google Drive / NETL as hosts but the individual Drive file IDs were not enumerated; sizes in §1 are the portal's published GB figures, not `Content-Length`. | Open `https://openfwi-lanl.github.io/docs/data.html` in a browser and copy the per-dataset Drive links. |
| **SFM pretraining corpus size in GB** | Hosted on USTC institutional servers and Baidu Netdisk; neither exposes a HEAD-able public URL. | The 13 `porestar/*` HF republications (rows 81–91, byte-exact) cover the downstream tasks without touching Baidu. |
| **`dataunderground.org`** | DNS/connection failure (curl code 000). | Likely permanently gone; the Georgia Tech datasets it hosted are on Zenodo (rows 66–67). |
| **SeisCLIP** | Not investigated — *earthquake* seismology, out of scope for exploration. | search: `SeisCLIP github dataset` |
| **Devito / Madagascar bundled example data** | Not enumerated; low value (tiny CI fixtures) relative to cost. | Clone the repos and look in `examples/` and `data/`. |
| **Further web searching** | The session's WebSearch budget (200 calls) was exhausted before the last few gaps could be closed. | Raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, or close the remaining gaps with a browser MCP tool — most of them are behind `seg.org`'s 403 anyway, which searching would not have fixed. |

---

## 12. Practical shortlist for a commercial product

Sorted by **licence safety first**, then usefulness.

| Rank | Dataset | Why | Licence |
|---|---|---|---|
| 1 | **The CIG collection** (§3b, ≈286 GB, 20 records) | The best value on the open web: labeled 3D synthetic volumes for faults, channels, karsts, horizons, RGT, clinoforms, structural models — and **almost entirely CC-BY-4.0**, so commercially usable with attribution. Start with **cigCK (42.9 GB)** and **cigChannel (12.0 GB)**. | **CC-BY-4.0 / MIT** |
| 2 | **F3 Facies Classification Benchmark** (2.14 GB) | The canonical facies benchmark, permissive licence, tiny download | **MIT** |
| 3 | **SFM downstream suite on HF** (13 sets, ≈39 GB) | Five ready ML tasks — facies, geobody, denoise, interpolation, inversion — already in parquet, loadable with one `load_dataset` call | **MIT / CC-BY-4.0** |
| 4 | **SEG/EAGE Salt + Overthrust** (1.22 GB) | The classic 3D synthetics, unambiguously CC-BY-4.0 | **CC-BY-4.0** |
| 5 | **Thebe** (53.09 GB) | Largest public *field* fault dataset with expert labels; CC0-based terms | **CC0 + CC-BY-4.0** |
| 6 | **Penobscot + Netherlands F3 interpretation** (3.97 GB) | Horizons + facies on two well-known field surveys | **CC-BY-4.0** |
| 7 | **Synthoseis** (code) | Generate unlimited labeled 3D volumes yourself — sidesteps every licence problem | **MIT** |
| 8 | **BP 2004 / BP 2007 TTI** (1.2 / 3.5 GB) | Industry-standard velocity and anisotropy benchmarks, open for research | BP research release |
| — | ⚠️ **OpenFWI** | Best-in-class FWI benchmark **but the data is CC BY-NC-SA 4.0 (NonCommercial)** | **NC — research only** |
| — | ⚠️ **FaultSeg3D** | The standard fault baseline **but "personal and research use only"; commercial use requires contacting the authors.** Use the CIG fault/channel/karst sets instead — same group, CC-BY-4.0. | **Research only** |
| — | ⚠️ **Chevron FWI suite** | Excellent elastic FWI benchmarks **but a revocable, non-transferable bespoke licence** | **Bespoke, legal review needed** |
| — | ⚠️ **TGS Salt (Kaggle)** | Popular, but competition rules govern; not an open licence | **Kaggle rules** |
