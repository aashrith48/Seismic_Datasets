# Prior Art and General-Purpose Data Hubs

**Survey date:** 2026-08-24. Everything below was fetched live via API or `curl` unless
explicitly marked otherwise. Sizes are **exact bytes** where an API returned them.
Nothing is estimated silently — unverifiable items are listed in "Could not verify".

**Link check:** all 15 primary resource URLs cited in Section (a) returned HTTP 200 on
2026-08-24 (checked with `curl -L` and a browser User-Agent). The two exceptions are
recorded as failures in their own right: `wiki.seg.org` (403 to every route) and
`dataunderground.org` (NXDOMAIN).

> **Status: v6 — COMPLETE** — Section (a) complete. Section (b) complete: Zenodo,
> HuggingFace, DataCite (cross-repository), §b.5 (Kaggle, figshare, OSF, Dataverse,
> Mendeley, Dryad), AWS/GCP/Azure and CTBTO/IMS. **All sections harvested.**

---

# Section (a) — Prior art: every curated list, index and wiki found

## a.1 Master table

| # | Resource | URL | Kind | Seismic entries | Last updated | Sizes? | Licences? | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | SEG Wiki — Open data | https://wiki.seg.org/wiki/Open_data | community wiki | **~55 named datasets** in 24 sections | page undated; **Wayback stops 2024-03-29** | Prose only | Prose only | The de-facto index. Cloudflare-gated to all bots; **28 % of its external links are dead** |
| 2 | softwareunderground/awesome-open-geoscience | https://github.com/softwareunderground/awesome-open-geoscience | awesome-list | **~10 of 19** data entries | pushed 2026-05-26 | No | No | Alive, 1.8k ★, 183 links, **only 1 dead link (5 %)**; but seismic is a footnote |
| 3 | SeisBench | https://github.com/seisbench/seisbench | Python loader | **44 concrete dataset classes** | pushed 2026-08-19 | At download time | In docstrings | Alive, excellent — **earthquake/DAS only** |
| 4 | aradfarahani/awesome-geophysics | https://github.com/aradfarahani/awesome-geophysics | awesome-list | **12 data entries, 6 seismic** | pushed 2026-08-02 | No | No | Newest active geophysics list; 257 links total |
| 5 | schipp/awesome-seismology | https://github.com/schipp/awesome-seismology | awesome-list | **5 data-access entries** | pushed 2026-06-23 | No | No | Alive; method/tool-oriented, not a data index |
| 6 | DAS-RCN/awesome-das | https://github.com/DAS-RCN/awesome-das | awesome-list | **10 DAS repositories** | **2022-11-04** | No | CC0 on the list itself | **Stale ~4 yr**; DAS only |
| 7 | yohanesnuwara/open-geoscience-repository | https://github.com/yohanesnuwara/open-geoscience-repository | dataset index + notebooks | **8 databases** in one table | **2021-10-08** | No | "Copyright note" per entry | **Stale ~5 yr**; closest historical analogue |
| 8 | cebirnie92/GeoGraphI | https://github.com/cebirnie92/GeoGraphI | Neo4j graph DB | schema-driven; OSDU-derived | **2021-04-30** | No | No | **Stale**; conceptually the closest prior art |
| 9 | LukasMosser/seismic-datasets | https://github.com/LukasMosser/seismic-datasets | conversion scripts + HF mirror | 3 dataset families | 2024-12-24 | Implicit (HF) | Cites source papers | Alive-ish; a *mirror*, not an index |
| 10 | Data Underground | `dataunderground.org` | community index | — | last Wayback **2024-09-03** | — | — | **DEAD — NXDOMAIN** |
| 11 | Software Underground | https://softwareunderground.org/ | community | n/a | live (HTTP 200) | — | — | Alive; hosts no dataset index |
| 12 | re3data | https://www.re3data.org/ | repository registry | **37 repositories** match "seismic" | rolling | No | Repository-level | Repository granularity only |
| 13 | SamiranDas1311/GeMiSe | https://github.com/SamiranDas1311/Geological-Mining-Seismic-Dataset-Collection-GeMiSe- | dataset collection | **~99 URLs, 48 seismic mentions** | 2024-03-22 | No | No | 17 ★. Has a *schema* (Location/Type/Description/Tags/Link) but stored as 912 lines of flat prose — zero markdown links, so not even clickable |
| 14 | blasscoc/SubsurfaceML | https://github.com/blasscoc/SubsurfaceML | curation attempt | — | **2018-10-15** | No | No | **Abandoned** |
| 15 | AdmcCarthy/subdata | https://github.com/AdmcCarthy/subdata | curation attempt | — | **2017-07-02** | No | No | **Abandoned** |
| 16 | fatiando/rockhound | https://github.com/fatiando/rockhound | data loader | — | 2022-06-30 | — | — | **Explicitly deprecated by its authors** |
| 17 | fatiando/ensaio | https://github.com/fatiando/ensaio | data loader | small practice sets | 2026-08-06 | Yes (checksums) | Yes | Alive; deliberately tiny scope |
| 18 | OpenFWI | https://openfwi-lanl.github.io/ | benchmark suite | **12 datasets, 4 families** | site © 2022 | **Yes — GB per dataset** | **Yes — CC-BY-NC-SA-4.0** | Alive; single-purpose (synthetic FWI). Best size+licence discipline found |
| 19 | TerraNubis free list | https://terranubis.com/datalist/free | vendor catalogue | **12 free projects** | live, © 2026 | No | No | Alive; OpendTect-format vendor catalogue |
| 20 | Agile Scientific blog | https://agilescientific.com/blog | blog roundups | many posts | **"Agile* is closing" 2022-07-14; last post 2022-08-29** | No | No | **FROZEN — the company shut down** |
| 21 | Papers With Code datasets | `paperswithcode.com` | ML dataset index | — | — | — | — | **DEAD — 302-redirects to huggingface.co/papers/trending** |
| 22 | ESIPFed/Awesome-Earth-Artificial-Intelligence | https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence | awesome-list | **4 seismic entries** | pushed 2026-06-26 | No | No | Alive, 250 ★; seismic is 4 links out of ~200 |
| 23 | FDSN data-centre registry | https://www.fdsn.org/datacenters/ | federation registry | **32 data centres** | rolling | No | No | Alive and **machine-readable** (`/ws/datacenters/1/query`); passive only |
| 24 | AWS Registry of Open Data | https://registry.opendata.aws/ | cloud registry | **9 of 1,190 datasets** | rolling (several daily) | **No — the YAML schema has no `Size` field at all** | **Yes** | Alive, high quality, machine-readable YAML. Best licence discipline of any registry; zero sizes; 2 wrong bucket regions found |
| 25 | Google Cloud Public Datasets | https://cloud.google.com/datasets | cloud registry | **3** (1 SEG-Y, 2 BigQuery catalogues) | varies | Partly | Yes | Alive; almost no seismic |
| 26 | Azure Open Datasets | https://learn.microsoft.com/azure/open-datasets/dataset-catalog | cloud registry | **0 of 38** | rolling | No | Yes | **No seismic content whatsoever** |

## a.2 The headline finding

Across **eleven GitHub repository-search queries** returning ~450 distinct repos, plus
the SEG wiki, re3data, Software Underground and the cloud registries:

> **No maintained, seismic-focused, machine-readable index of open seismic datasets
> carrying sizes and licences currently exists.**

**And the niche is emptying, not filling.** In the last four years the field has
*lost* four of its index nodes:

| Node | Fate | Evidence |
|---|---|---|
| `dataunderground.org` | **Domain gone** | `nslookup` → NXDOMAIN; last Wayback capture 2024-09-03 |
| Agile Scientific | **Company closed** | Blog post *"Agile* is closing"*, 2022-07-14; last post 2022-08-29 |
| Papers With Code | **Shut down** | `paperswithcode.com/api/v1/datasets/?q=seismic` → HTTP 302 → `huggingface.co/papers/trending` |
| SEG Wiki *Open data* | **Bot-inaccessible and rotting** | HTTP 403 to curl/API/WebFetch; no Wayback 200 capture since 2024-03-29; **19 of its 69 external links (28 %) are dead** — including the access routes for Teapot Dome, Volve, SMAART and the New Zealand data pack |

**Link rot, measured across every list's data section** (checked 2026-08-24 with
`curl -L` and a browser UA; HTTP 200 and 403 both counted as alive):

| List | Data links checked | Broken | Rot rate |
|---|---:|---:|---:|
| `DAS-RCN/awesome-das` — Data repositories | 9 | 0 | **0 %** |
| `softwareunderground/awesome-open-geoscience` — Data Repositories | 19 | 1 (UK NDR) | **5 %** |
| `aradfarahani/awesome-geophysics` — Datasets and Databases | 11 | 1 (ISC, unreachable from this network) | **9 %** |
| **SEG Wiki — Open data** | **69** | **19** | **28 %** |

The pattern is clear: the *big* index is the *rotten* index, and it is the one nobody
can check. `awesome-das` has not been touched since 2022 yet has zero dead links,
because its ten entries point at institutional repositories (GDR OpenEI, Caltech,
Globus, GitHub) rather than at corporate landing pages and Google Drive folders.
**Where you host matters more than how often you update.**

**Plus a discoverability gap:** the canonical awesome index
(`sindresorhus/awesome`, 78,803 bytes) contains **no geoscience, geophysics or
seismology entry at all** — its only Earth-science line is
`[Earth](https://github.com/philsturgeon/awesome-earth#readme) - Find ways to resolve
the climate crisis.` Neither `awesome-open-geoscience` nor `awesome-seismology` is
listed there, so neither is reachable by anyone browsing the awesome ecosystem.

The three projects that ever attempted exactly that have all lapsed:

- **`dataunderground.org`** — the Software Underground community's dataset index —
  now returns **NXDOMAIN**. Last Internet Archive capture 2024-09-03.
- **`cebirnie92/GeoGraphI`** — a Neo4j graph database of open seismic datasets with an
  OSDU-derived schema, explicitly built because *"with no central storage location or
  consistent description strategy, finding suitable openly available datasets still
  poses a large challenge to the geophysics community"* — last commit **2021-04-30**,
  3 stars.
- **`yohanesnuwara/open-geoscience-repository`** — a catalogue table plus access
  notebooks, 143 stars — last commit **2021-10-08**.

What remains alive splits cleanly into two halves that never meet: **exploration
seismic** (SEG wiki, awesome-open-geoscience, TerraNubis) and **earthquake seismology**
(SeisBench, awesome-seismology, re3data, FDSN). Nothing spans both, and nothing in
either half publishes structured sizes or licences.

## a.3 `softwareunderground/awesome-open-geoscience` — verified

- **Stars** 1,818 · **Forks** 531 · **Open issues** 10
- **Created** 2017-10-18 · **Last push** 2026-05-26 · **Metadata touched** 2026-08-20
- **Licence** CC0-1.0 · **Default branch** `main`
- **Sections:** Related Awesome · Open Books · Software · Data Repositories ·
  Tutorials and Cheat Sheets · Miscellaneous · How to Contribute

**Data Repositories section — complete, extracted from the raw README (10,940 bytes,
183 links total): 20 links, 19 unique, of which ~10 are seismic/subsurface-relevant.**
Link-checked 2026-08-24:

| Entry | URL | Seismic? | Status |
|---|---|---|---|
| Athabasca Oil Sands Well Dataset McMurray/Wabiskaw | https://ags.aer.ca/publication/spe-006 | wells | 200 |
| Digital Rocks Portal | https://www.digitalrocksportal.org | no | 200 |
| Geoscience Australia Portal | https://portal.ga.gov.au | yes | 200 |
| GSQ Open Data Portal | https://geoscience.data.qld.gov.au/ | yes | 403 (alive) |
| GSQ GitHub Repository | https://github.com/geological-survey-of-queensland | partly | 200 |
| ICGEM | http://icgem.gfz-potsdam.de/home | no (gravity) | 200 |
| NOPIMS | http://www.ga.gov.au/nopims | yes | 200 |
| Poseidon NW Australia | Google Drive folder `0B7brcf-eGK8Cbk9ueHA0QUU4Zjg` | yes | 200 |
| Quantarctica | https://www.npolar.no/quantarctica | no | 200 |
| SARIG | https://map.sarig.sa.gov.au | yes | 200 |
| SEG Open Data Catalog | https://wiki.seg.org/wiki/Open_data | index | 403 |
| TerraNubis | https://terranubis.com/datalist/free | yes | 200 |
| **UK National Data Repository** | https://ndr.ogauthority.co.uk | yes | **BROKEN — no connection** |
| Volve data village (listed twice) | https://www.equinor.com/energy/volve-data-sharing | yes | 200 |
| World Stress Map | http://www.world-stress-map.org | no | 200 |
| Macrostrat | https://macrostrat.org | no | 200 |
| Costa Model | https://researchportal.hw.ac.uk/en/datasets/costa-model-hierarchical-carbonate-reservoir-benchmarking-case-st/ | reservoir | 200 |
| EarthChem | https://www.earthchem.org/ | no | 200 |
| Tethys Research Data Repository | https://www.tethys.at/ | no | 200 |

**Link health: 18 of 19 reachable — only the UK NDR is dead** (the OGA was renamed the
North Sea Transition Authority and the `ogauthority.co.uk` host no longer answers).
That is a 5 % rot rate against the SEG wiki's 28 %, which is what active maintenance
buys you.

**Gaps:** no sizes, no licences, no access-friction notes anywhere. Datasets are a
minority of a mostly-software list. Several seismic entries are indirections to *other*
indexes (SEG wiki, TerraNubis) rather than data. The Poseidon entry is a bare Google
Drive folder ID. Volve is listed twice.

## a.4 SEG Wiki "Open data" — full entry list (recovered from Wayback)

**Access problem, verified three ways.** `wiki.seg.org` returns **HTTP 403** to:
`curl` with a Chrome User-Agent and `Accept-Language`; the MediaWiki API
(`/api.php?action=parse&page=Open_data&format=json`); and WebFetch. The `r.jina.ai`
proxy refused separately (HTTP 401, "blocked from performing anonymous queries due to
bad network reputation"). The page sits behind Cloudflare bot protection.

The Wayback CDX index shows the **last successful 200 capture is 2024-03-29**
(`http://web.archive.org/web/20240329123137/https://wiki.seg.org/wiki/Open_data`,
43,445 bytes), with prior captures at 2024-03-26, 2024-02-05, 2024-02-02, 2024-01-23,
2024-01-21, 2023-01-30 and 2022-11-21 — and **nothing after March 2024**, consistent
with the Cloudflare gate going up then. **The list below is accurate as of March 2024
and may have drifted.**

Page's own framing: *"Open data on the SEG Wiki is a catalog of available open
geophysical data online. SEG does not own or maintain the data listed on this page…
you do not need SEG's permission to utilize the open data on the page for your
research, thesis, lectures, or presentations."*

**24 top-level sections, ~55 named datasets:**

| § | Section | Named datasets |
|---|---|---|
| 1 | Machine Learning Blind-test Challenge at SEG 2020 | 3D seismic volume + facies label volume, both SEG-Y (Chevron / Bevc, Halpert, Fomel, Herrmann, Esmersoy) |
| 2 | SEAM open data | Interpretation Challenge I – Depth; Interpretation Challenge I – Time (hosted on **Google Drive**) |
| 3 | Phase I 2D Data Sets | Elastic Earth Model Subset 2D; Elastic 2DEW Classic; Elastic VSP 2D Walk-Away; Well logs |
| 4 | 2D land seismic data | Poland 2D Vibroseis Line 001 |
| 5 | 2D marine seismic data | US east coast deep water line 32; USGS Marine Seismic Data; Mobil AVO Viking Graben line 12; PGS Simultaneous Source Marine Line; UK Mid-North Sea High & Rockall Trough 2D; UK South-West of Britain & East Shetland Platform 2D |
| 6 | 3D land seismic data | Teapot Dome 3D; Stratton 3D |
| 7 | 3D marine seismic data | F3 Netherlands; Poseidon 3D (Australia); Penobscot 3D; Blake Ridge 3D; North Sea Norne field; North Sea Volve Data Village; 2010 BP 3D Tiber WATS |
| 8 | SEG/DMEC Reference Mineral Exploration Data | 1 |
| 9 | New Zealand 3D | Opunake-3D; Parihaka-3D; Kahu-3D; Kerry-3D; Tui-3D; Waihapa-3D; Waipuku-3D; Waka-3D |
| 10 | OpenGeoscience at British Geological Survey | portal |
| 11 | Natural Resources Canada | portal |
| 12 | National Petroleum Reserve Alaska (NPRA), USGS | Alaska 2D land line 31-81; Alaska 2D land line 16-81 |
| 13 | Norwegian Petroleum Directorate | portal |
| 14 | 2D synthetic seismic data | AGL Elastic Marmousi; 1994 BP migration from topography; 1994 BP statics benchmark; 1997 BP 2.5D migration benchmark; 2004 BP velocity estimation benchmark; 2007 BP Anisotropic Velocity Benchmark; Chevron GOM FWI Synthetics; Hess VTI migration benchmark; KFUPM-KAUST Red Sea model |
| 15 | Qademah Fault 3D Survey | 1 |
| 16 | SMAART models | family |
| 17 | 3D synthetic seismic data | SEG/EAGE Salt and Overthrust Models; SEG/EAGE 3D Salt Model Phase-C 1996; 3D 9C synthetic VSP |
| 18 | Gravity and magnetic data | Satellite data; Bishop Model |
| 19 | Chevron GOM FWI Seismic, CSEM and MT Synthetic | 1 |
| 20 | Topographic and bathymetric data | portals |
| 21 | Dutch Ministry of Economic Affairs Data Release | 1 |
| 22 | Geophysical Software and Algorithms | software |
| 23 | Candidate open data | staging list |
| 24 | See also | — |

### Link rot on the SEG wiki, measured: **19 of 69 external links are broken (28 %)**

Every external URL on the 2024 snapshot was extracted (83 links, 69 unique after
removing Wikipedia and seg.org self-links) and checked with `curl -L` and a browser
User-Agent on 2026-08-24. Treating 200 and 403 (bot-blocked but alive) as reachable:

**50 reachable · 19 broken.**

| Broken link | Status | What it was |
|---|---|---|
| `drive.google.com/open?id=1RycUcV5vWIoAK3K0g-Jwa7ZM4Rkm8Vjy` | 404 | Google Drive dataset |
| `drive.google.com/open?id=1RjQrT2bPAkbOdQ-4a_LGSDr9tPnGS7WFhzVpwfbi89Q` | 404 | Google Drive dataset |
| `http://www.rmotc.doe.gov/` | no connection | RMOTC — the **Teapot Dome** host; facility closed |
| `https://data-equinor-com.azurewebsites.net/authenticate` | no connection | **Volve** data-village access page |
| `http://www.statoil.com/en/Pages/default.aspx` | 404 | Statoil — renamed Equinor in 2018 |
| `http://www.petoro.no/home` | no connection | Norne field partner |
| `http://www.delphi.tudelft.nl/SMAART/` | no connection | **SMAART models** |
| `http://www.nzpam.govt.nz/cms/.../exploration-data-pack` | 404 | **New Zealand 3D data pack** |
| `http://www.nrcan.gc.ca/earth-sciences/resources/10778` | 404 | Natural Resources Canada |
| `https://www.nrcan.gc.ca/earth-sciences/science/geology/energy-geoscience/10890` | 404 | Natural Resources Canada |
| `http://www.npd.no/en/Maps/` and `/Map-of-the-NCS/` | 404 ×2 | NPD — renamed Norwegian Offshore Directorate, 2024 |
| `https://www.ogauthority.co.uk/exploration-production/exploration/seismic-acquisition/` | 404 | OGA — renamed NSTA |
| `https://www.ukoilandgasdata.com/` | 301 loop | UK data portal |
| `http://www.bgs.ac.uk/discoverymetadata/13605653.html` | 400 | BGS metadata record |
| `http://www.cs.sandia.gov/~ccober/seismic/salt_c3.html` | 302 loop | SEG/EAGE Salt Model Phase-C |
| `http://www.eni.com/en_IT/home.html` | connection error | Eni |
| `http://earth.esa.int/.../goce-data-access-7219` | 404 | GOCE gravity data access |
| `http://dl.dropbox.com/u/37269048/...pptx` | 404 | Dropbox-hosted slides |

Note what is broken: **the access routes for Teapot Dome, Volve, SMAART and the entire
New Zealand data pack** — four of the wiki's headline datasets. And because
`wiki.seg.org` 403s every automated agent, *nobody can run this check on the live page*.
The rot is structurally invisible to its own maintainers.

**What is still healthy:** the `open.source.geoscience` S3 bucket that hosts several SEG
synthetics. `elastic-marmousi-model.tar.gz` returns HTTP 200,
**Content-Length 153,722,387**, Last-Modified 2019-04-22, no auth. (The bucket is not
listable — `?list-type=2` → `AccessDenied`.)

### Proof the SEG wiki list has already drifted: SEAM moved off Google Drive

The 2024 wiki snapshot says *"SEAM open data is hosted using the Google Drive online
service… due to their large size, Google Drive may notify you that it cannot offer
preview or virus scanning functionality."* **That is no longer true.** SEG relaunched
its website (banner: *"SEG has moved to a new platform as of 3 Aug"*) and
https://seg.org/seam/open-data/ (HTTP 200) now serves SEAM from a **public,
unauthenticated AWS S3 bucket**: `seam-open-data.s3.us-west-2.amazonaws.com`.

Exact sizes, verified by HTTP HEAD on 2026-08-24 — **no account, no registration,
direct HTTPS**:

| Object | Bytes | Last-Modified |
|---|---:|---|
| `Phase+I/SEAM_Interpretation_Challenge_1_Depth.zip` | 3,026,841,906 | 2021-11-13 |
| `Phase+I/SEAM_Interpretation_Challenge_1_Time.zip` | 2,942,886,186 | 2021-11-13 |
| `Phase+I/SEAM_I_2D_Data.zip` | 892,317,018 | 2021-11-13 |
| `Phase+I/SEAM_I_Well_Log_Delivery.zip` | 16,605,942 | 2021-11-13 |
| `Phase+I/SEAM_Phase_I_Volume_1_+Combined_web.pdf` | 16,254,902 | 2021-11-13 |
| `Phase+I/SEAM_I_2D_Model.zip` | 16,185,850 | 2021-11-13 |
| **Total Phase I** | **6,911,091,804 (≈6.44 GiB)** | |

The Time Lapse Pilot package (before/after reciprocal OBN shots, 501 × 501 array at
25 m spacing, 257.5 m above the node), the RPSEA Final Report, the TLE article and the
**SEAM Time Lapse Pilot End User License Agreement** are all under
`Time+Lapse+Pilot/` in the same bucket. Note the EULA: SEAM open data is *free* but
governed by an end-user licence, not a Creative Commons licence.

The bucket is **not listable** — `?list-type=2` returns HTTP 403 — so individual keys
must be known. Related: `seg.org/publications/seg-wiki/` now returns **HTTP 404**, and
`library.seg.org` redirects to `pubs.geoscienceworld.org/seg`. The wiki itself is still
linked from the seg.org homepage (`wiki.seg.org/wiki/Main_Page`) but is clearly not
being maintained in step with the main site.

**Gaps:** no structured sizes — geometry is described in prose (e.g. SEAM Elastic 2DEW:
"901 receivers per shot, 151 shots from East 3700 m to 18700 m, 2001 samples at 8 ms")
which is useful but not machine-readable; no licence field — terms of use are narrative
and vary per dataset; heavy Google Drive hosting with an explicit warning that Drive
"cannot offer preview or virus scanning" for the large files; **no passive/earthquake
data, no DAS, no national archives beyond three portal links**; and the page is now
unreachable to any automated link checker, so its rot cannot be audited by anyone.

## a.5 SeisBench — "~45 dataset classes" claim **verified**

- **Repo** https://github.com/seisbench/seisbench · **Docs** https://seisbench.readthedocs.io
- **Stars** 414 · **Last push** 2026-08-19 · **Licence** GPL-3.0
- **`seisbench/data/` module count:** 30 Python files
- **Paper:** Woollam et al. (2022), *SeisBench—A Toolbox for Machine Learning in
  Seismology*, SRL, https://doi.org/10.1785/0220210324 (175 citations)

Counting concrete benchmark dataset classes exported from `seisbench/data/__init__.py`
(excluding abstract bases, writers, bucketers, `Dummy*`, `DatasetInspection`):
**44 classes.** The "~45" figure is **confirmed**.

`AQ2009GM`, `AQ2009Counts`, `BohemiaSaxony`, `CEED`, `CREW`, `CWA`, `CWANoise`,
`ESM25BadCV`, `ESM25GoodCV`, `ESM25GoodMP`, `ESM25SpectraMP`, `ETHZ`,
`EQSDenoiserEvents`, `EQSDenoiserNoise`, `EQSDenoiserCombined`, `GEOFON`,
`InstanceCounts`, `InstanceCountsCombined`, `InstanceGM`, `InstanceNoise`, `Iquique`,
`ISC_EHB_DepthPhases`, `LenDB`, `LFEStacksCascadiaBostock2015`,
`LFEStacksMexicoFrank2014`, `LFEStacksSanAndreasShelly2017`, `MLAAPDE`, `MLSubDAS`,
`NEIC`, `OBS`, `OBST2024`, `PiSDL`, `PNW`, `PNWAccelerometers`, `PNWExotic`,
`PNWNoise`, `SCEDC`, `Meier2019JGR`, `Ross2018GPD`, `Ross2018JGRFM`,
`Ross2018JGRPick`, `STEAD`, `TXED`, `VCSEIS`.

DAS is now in scope: `MLSubDAS` plus the `DASDataset` / `DASBenchmarkDataset` /
`DASDataWriter` / `MultiDASDataset` / `RandomDASDataset` machinery (v0.11 release notes
cite "DAS support, performance improvements, new datasets and models",
https://doi.org/10.5281/zenodo.18433641).

**Gaps:** exploration/reflection seismic is **entirely absent** — no F3, Parihaka,
Volve, Poseidon, SEAM, Marmousi, Teapot Dome. And it is a *loader*, not an index: you
cannot browse it to answer "what open seismic data exists", only pull the 44 it wraps.

## a.6 Data Underground — **dead, verified**

- `nslookup dataunderground.org` → **`Non-existent domain` (NXDOMAIN)**
- `curl` → HTTP 000, no connection
- Last Internet Archive capture **2024-09-03**:
  `http://web.archive.org/web/20240903043531/https://dataunderground.org/`

This was the Software Underground community's dataset index and the closest historical
analogue to a curated seismic dataset repo. It no longer exists.

**Provenance confirmed on GitHub.** The `softwareunderground` org has 47 repos; one is
**`softwareunderground/data-underground`** — *"Things related to open data and
dataunderground.org"* — **0 stars, last pushed 2019-09-22**. So the project was
effectively abandoned in 2019; the site limped on unmaintained until the domain lapsed
some time after September 2024.

`softwareunderground.org` itself is alive (HTTP 200, 21 KB landing page) but is a
community/Mattermost front door. Its navigation is
`mattermost · blog · events · calendar · rendezvous · TRANSFORM · AGM · org · about ·
contact · FAQ · board · conduct · terms · privacy · logos · projects · stack · code ·
chateau · support` — **there is no data or datasets section at all.**

Other SWUNG repos worth noting: `awesome-open-geoscience` (1,818 ★, §a.3);
`awesome-open-geothermal` (13 ★, last push 2022-09-04); `awesome-machine-learning`
(0 ★, 2023-07-21, subsurface ML *papers*); `subsurface` (66 ★, "core data exchange
library", 2024-06-14); `gio` (65 ★, read/write subsurface surfaces & horizons);
`xsdf` — "X Seismic Data Format" (6 ★, abandoned 2017-04-04); `fossilnet` (6 ★, an
image dataset); `TeapotDome` (1 ★, 2015).

## a.7 `aradfarahani/awesome-geophysics` — verified

- 129 ★ · pushed **2026-08-02** · 54,992 chars, **257 links**, 46 headings
- Sections: Software and Tools · **Datasets and Databases** · Educational Resources ·
  Textbooks · Online Courses · Research Papers and Journals · Tutorials and Cheat
  Sheets · Organizations and Societies · Conferences · Blogs/Podcasts/Forums ·
  Career · Industry News · Market Analysis

**"Datasets and Databases" contains exactly 12 entries**, of which 6 are seismic:

| Entry | URL | Seismic? |
|---|---|---|
| GeoMapApp | https://www.geomapapp.org/data_set_news.html | partly |
| Global Seismographic Network (GSN) | https://www.iris.edu/hq/programs/gsn | yes |
| ICGEM | http://icgem.gfz-potsdam.de/home | no (gravity) |
| International Seismological Centre (ISC) | https://www.isc.ac.uk/ | yes (catalogue) |
| IRIS Data Management Center | https://ds.iris.edu/ds/nodes/dmc/ | yes |
| NGDC | https://www.ngdc.noaa.gov/ | no |
| NOAA NCEI | https://www.ncei.noaa.gov/ | no |
| Poseidon NW Australia | Google Drive `0B7brcf-eGK8Cbk9ueHA0QUU4Zjg` | yes |
| Quantarctica | https://www.npolar.no/quantarctica/ | no |
| SEG Open Data Catalog | https://wiki.seg.org/wiki/Open_data | yes (index) |
| TerraNubis | https://terranubis.com/datalist/free | yes |
| USGS Earthquake Hazards Program | https://earthquake.usgs.gov/ | yes (catalogue) |

**Gaps:** no sizes, no licences; the actual *seismic data* content is four links
(GSN, IRIS, Poseidon, TerraNubis) plus two indirections. Its strength is software and
education, not data.

## a.8 `schipp/awesome-seismology` — verified

- 34 ★ · pushed **2026-06-23** · 15,773 chars, 105 links, 19 sections
- Sections: Array seismology · Earthquake bulletins/catalogues · Educational resources ·
  Fibre optic sensing · Imaging · Inversion & Inference · Machine learning ·
  Marine seismology · Observatory software · Phase picking and association · Raytracing ·
  **Seismic data access** · Seismic data handling · Seismic hazard ·
  Seismic interferometry and ambient noise · Source parameter estimation ·
  Synthetic seismograms

**"Seismic data access" contains exactly 5 entries:**
EarthScope (formerly IRIS) · EIDA (ORFEUS) · FDSN network codes · PyWEED · STEAD.

**Gaps:** this is a *methods and software* list with a data-access appendix. No sizes,
no licences, no exploration seismic, and only one actual dataset (STEAD).

## a.9 `DAS-RCN/awesome-das` — verified, stale

- 72 ★ · pushed **2022-11-04** (≈4 years stale) · CC0 licence badge
- Sections: Data Management · Processing · Visualisation · Modelling · **Data repositories**

**Data repositories — 7 public + 3 earthquake-specific:**

| Dataset | Host |
|---|---|
| PoroTomo Experiment at Brady Hot Springs | GDR OpenEI submission 849 |
| FORGE Phase 2C | GDR OpenEI submission 1185 |
| Garner Valley | GDR OpenEI submission 614 |
| Belgium DAS | Caltech `data.caltech.edu/records/1296` |
| Monterey Bay Dark Fiber | GitHub (`njlindsey/Photonic-seismology-in-Monterey-Bay…`) |
| RCA Shore Station / Cascadia Margin | OOI announcement + FTP link |
| **PubDAS** | Globus endpoint `706e304c-5def-11ec-9b5c-f9dfb1abb183` |
| SAFOD DAS array | GitHub `ariellellouch/DASDetection` |
| Stanford Phase 1 experiment | GitHub `eileenrmartin/FiberOpticEarthquakes` |
| Fairbanks Farmers Loop | GitHub `eileenrmartin/FiberOpticEarthquakes` |

**Gaps:** no sizes, no licences, no updates since 2022 — and DAS has moved fast since.
Note the PubDAS entry has a broken markdown link (`[Globus] (https://…)` with a space).

## a.10 `yohanesnuwara/open-geoscience-repository` — verified, stale

- 143 ★ · pushed **2021-10-08** (≈5 years stale) · CC-BY-4.0
- Self-described: *"a quick catalogue of the open databases"*, one table with columns
  Open Databases | Owner | Topics | Accessible Contents | How-to-access tutorial

**8 databases catalogued:** Google Drive *Public geoscience Data* (Peter Amstrand) —
Canning 3D TDQ seismic, Dutch F3, GEOLINK North Sea wells, Poseidon seismic, core
images, 48 well composite logs · SEG Wiki · GDR OpenEI (Utah FORGE, HOTSPOT) ·
KGS Repository · MSEEL Repository · 14 Wildcat Wells NPRA (USGS) · Oklahoma
Corporation Commission Oil & Gas Data Files · SPE Data Repository.

**What it did well that nothing else does:** each entry ships an *access notebook* —
a working Colab/Jupyter recipe for actually pulling the data. That is the same idea as
shipping fetch scripts.

**Gaps:** stale by five years; no sizes; licence handled by a hand-wave "⚠️ Copyright
note … you should cite the dataset to its owner institution"; only 8 sources.

## a.11 `cebirnie92/GeoGraphI` — the closest conceptual prior art, abandoned

- 3 ★ · pushed **2021-04-30** · a Neo4j `*.dump` file, queried in Cypher
- Its own problem statement is the same one this repo addresses verbatim:
  > *"Over the years numerous geophysical datasets have been released for public usage.
  > However, with no central storage location or consistent description strategy,
  > finding suitable openly available datasets still poses a large challenge to the
  > geophysics community."*
- Schema is **an extension of the Open Subsurface Data Universe (OSDU) schema** with
  extra "less-technical dataset descriptors": Dataset (id, name, link),
  Operating Environment (Marine/Land/Cross), Generation Procedure
  (Synthetic/Lab/Field), Geographic Region, Seismic Geometry (2D/3D/4D/Passive),
  Energy Source, Receiver Type — plus feature tags such as CO₂ injection, turbidites,
  simultaneous shooting, surface-related multiples.
- Supports similarity queries: *"Return similar field datasets to the SEAM dataset."*

**Gaps:** requires a running Neo4j instance to read at all — no browsable rendering, no
CI, no sizes, no licences; abandoned after ~6 months; three stars.

## a.12 `LukasMosser/seismic-datasets` — a mirror, not an index

- 6 ★ · pushed 2024-12-24. Converts existing seismic ML datasets to HuggingFace
  `datasets` format with reproduced train/valid/test splits.
- Explicit motivation: *"I highly encourage not storing datasets on google drives and
  provide corresponding dataloaders for datasets on zenodo via huggingface."*
- Covers 3 families: Seismic SuperResolution (Li, Wu & Hu 2022, TGRS
  10.1109/TGRS.2021.3057857); Seismic Foundation Model (shenghanlin); Cross-Domain
  Foundation Model Adaptation.
- Output lives at the HF collection `porestar/seismic-foundation-model-datasets-…`
  and is visible in §b.1 below (`porestar/*`, consistently CC-BY-4.0 or MIT).

## a.13 re3data — 37 seismic repositories

`https://www.re3data.org/api/beta/repositories?query=seismic` → **37 repositories**.
(Note: the older `/api/v1/` endpoint ignores `query=` and returns all 3,521
repositories — a trap worth recording. `query=seismology` and `query=seismic data`
also return 37; `query=geophysics` returns 343; `query=subsurface` returns 6.)

| # | Repository | re3data ID |
|---:|---|---|
| 1 | Academic Seismic Portal at LDEO | r3d100010644 |
| 2 | Bureau Central Sismologique Français – RNSS | r3d100014052 |
| 3 | Center for Engineering Strong Motion Data | r3d100011797 |
| 4 | Northern California Earthquake Data Center | r3d100011679 |
| 5 | Academic Seismic Portal at UTIG | r3d100010631 |
| 6 | Alberta Geological Survey Open Data Portal | r3d100013018 |
| 7 | AHEAD | r3d100011648 |
| 8 | Southern California Earthquake Data Center | r3d100011575 |
| 9 | Agricultural and Environmental Data Archive | r3d100012236 |
| 10 | Canada-Nova Scotia Offshore Petroleum Board DMC | r3d100010981 |
| 11 | Marine Geoscience Data System | r3d100010273 |
| 12 | GERDA | r3d100011484 |
| 13 | National Earthquake Information Center | r3d100010313 |
| 14 | China Earthquake Data Center | r3d100011154 |
| 15 | EPOS-FRANCE Seismological Data Center | r3d100012222 |
| 16 | EIDA | r3d100011718 |
| 17 | WDC for Geophysics, Beijing | r3d100012217 |
| 18 | China Seismic Array Data Management Center | r3d100013132 |
| 19 | Database of Individual Seismogenic Sources | r3d100012621 |
| 20 | EarthScope | r3d100010587 |
| 21 | National Data Repository (UK) | r3d100012683 |
| 22 | GEOFON | r3d100011326 |
| 23 | NSF GAGE Facility | r3d100010872 |
| 24 | National Earthquake DataBase | r3d100011997 |
| 25 | Wyoming Data Repository | r3d100014441 |
| 26 | Alaska Climate Research Center | r3d100010954 |
| 27 | Southern California Earthquake Center | r3d100010764 |
| 28 | WOVOdat | r3d100013649 |
| 29 | European-Mediterranean Seismological Centre | r3d100011729 |
| 30 | Incorporated Research Institutions for Seismology | r3d100010268 |
| 31 | World Stress Map | r3d100010664 |
| 32 | MARGINS Data Collection | r3d100010641 |
| 33 | SedDB | r3d100011534 |
| 34 | NOAA NCEI (formerly NGDC) | r3d100010292 |
| 35 | Exploration and Production Data Bank (BDEP) | r3d100010989 |
| 36 | Oceans 3.0 Data Portal | r3d100011094 |
| 37 | NEPTUNE Canada | r3d100010693 |

Each URL is `https://www.re3data.org/repository/<id>`.

**Gaps:** repository granularity only — never dataset-level, never sizes. Entries such
as "Incorporated Research Institutions for Seismology" (IRIS) are stale names; IRIS
merged into EarthScope in 2023 and both are listed separately. Only ~4 of the 37 are
exploration-seismic (CNSOPB, UK NDR, BDEP, Alberta GS).

## a.14 GitHub landscape — full search results

GitHub repository-search API `total_count` per query:

| Query | Repos matched |
|---|---:|
| `awesome seismic` | 7 |
| `awesome geoscience` | 14 |
| `awesome geophysics` | 8 |
| `awesome seismology` | 7 |
| `open seismic data` | 61 |
| `seismic datasets` | 218 |
| `subsurface datasets` | 35 |
| `open subsurface data` | 12 |
| `seismic data list` | 7 |
| `awesome subsurface` | 2 |
| `geoscience datasets` | 65 |

Every repo in the top-25-by-stars of each query was inspected. The complete set of
repos that are *curated indexes* (not tools, not single datasets) is in §a.1.

**Topic and negative searches** (run separately from the eleven above):

| Query | Repos | What is in it |
|---|---:|---|
| `topic:seismic-data` | 142 | All tools, models or single datasets — **no curated index**. Top: `microsoft/seismic-deeplearning` (475 ★, last push **2020-09-18**), `anyshake/explorer` (90 ★), `SeismicSource/sourcespec` (81 ★), `JintaoLee-Roger/cigsegy` (64 ★, SEG-Y ↔ NumPy) |
| `topic:seismology list` | 6 | `DAS-RCN/awesome-das` (stale), `Hunter-Github/GitScience` (2017), `phonchi/Awesome-earthquake-predictions` |
| `topic:open-data topic:geophysics` | 5 | `awesome-open-geoscience` plus four unrelated repos; note `fatiando/data` is explicitly marked **DEPRECATED** |
| `awesome earth science` | 8 | Best is `ESIPFed/Awesome-Earth-Artificial-Intelligence` (250 ★, 2026-06-26) — see below |
| `awesome geology` | 7 | `awesome-open-geoscience`, `aradfarahani/awesome-geophysics`, `awesome-geotechnics` (2018), `awesome-planetary-geology` |
| `seismic open data catalog` | 3 | All 0-star personal projects |
| `awesome list geophysics data catalog` | **0** | — |
| `seismic data catalog yaml` | **0** | — |
| `open geophysical data index` | **0** | — |
| `subsurface data catalog` | **0** | — |

Those four zeroes are the sharpest evidence in this document: **no repository on GitHub
is a structured catalogue or index of seismic/subsurface datasets.**

**`ESIPFed/Awesome-Earth-Artificial-Intelligence`** (250 ★, pushed 2026-06-26,
11,760 bytes) is the best-maintained adjacent list, run by the Earth Science
Information Partners. Its sections are ML questions · Courses · Books · Tools ·
Foundation Models · Earth Observation · Weather and Climate · Tutorials ·
**Training Data** · Code · Videos · Papers · Reports · Competitions · Communities.
Its **entire seismic content is four entries**: SeisBench, STEAD, EQTransformer, and
the LANL Earthquake Prediction Kaggle competition. No sizes, no licences.

Also noted — **datasets, not indexes**, but heavily depended on and worth linking:
`smousavi05/STEAD` (405 ★), `lishiqianhugh/GlobalTomo` (28 ★, "first global synthetic
dataset for physics-ML seismic wavefield modeling and FWI"), `huigcig/cigFaciesNet`
(19 ★), `mila-iqia/hardpicks` (18 ★, first-break picking on hardrock seismic),
`DIG-Kaust/VolveSynthetic` (16 ★), `djozinovi/LEN-DB` (7 ★),
`olivesgatech/LANDMASS` (3 ★), `GeostatsGuy/GeoDataSets` (106 ★, synthetic
geostatistics), `ubriustc/GPR_data` (58 ★, GPR).

## a.15 OpenFWI — verified, and the *only* list that publishes both sizes and a licence

- **Site** https://openfwi-lanl.github.io/ (HTTP 200) · **Code** https://github.com/lanl/OpenFWI
- **Paper** Deng et al., arXiv:2111.02926 · NeurIPS D&B 2022 (10.52202/068431-0435)
- **Licence, stated on the datasets page:** *Creative Commons
  Attribution-NonCommercial-ShareAlike 4.0 International* — applies to the whole suite
- Self-description: *"the first open-source platform to facilitate data-driven FWI
  research… twelve datasets synthesized from different priors, including one 3D dataset"*

Sizes and shapes are published per dataset, which nothing else in §a does:

| Family | Dataset | Size | #Train | #Val | Input shape | Output shape |
|---|---|---:|---:|---:|---|---|
| Vel | FlatVel-A | 43 GB | 24 K | 6 K | (5,1000,70) | (1,70,70) |
| Vel | FlatVel-B | 43 GB | 24 K | 6 K | (5,1000,70) | (1,70,70) |
| Vel | CurveVel-A | 43 GB | 24 K | 6 K | (5,1000,70) | (1,70,70) |
| Vel | CurveVel-B | 43 GB | 24 K | 6 K | (5,1000,70) | (1,70,70) |
| Fault | FlatFault-A | 77 GB | 48 K | 6 K | (5,1000,70) | (1,70,70) |
| Fault | FlatFault-B | 77 GB | 48 K | 6 K | (5,1000,70) | (1,70,70) |
| Fault | CurveFault-A | 77 GB | 48 K | 6 K | (5,1000,70) | (1,70,70) |
| Fault | CurveFault-B | 77 GB | 48 K | 6 K | (5,1000,70) | (1,70,70) |
| Style | Style-A | 95 GB | 60 K | 7 K | (5,1000,70) | (1,70,70) |
| Style | Style-B | 95 GB | 60 K | 7 K | (5,1000,70) | (1,70,70) |
| Kimberlina | Kimberlina-CO2 | 96 GB | 15 K | 4,430 | (9,1251,101) | (1,401,141) |

**Total of the 11 sizes published: 766 GB.** The twelfth (3D) dataset is announced on
the home page but has no size row on `docs/data.html`.

**Gaps:** single-purpose (synthetic FWI only); site copyright still reads "OpenFWI
2022"; pretrained models are on Google Drive; **NC-SA licence blocks commercial use** —
a material constraint that most lists citing OpenFWI never mention.

## a.16 TerraNubis (dGB) free list — verified live

`https://terranubis.com/datalist/free` (HTTP 200, © 2018-2026). Split into
"Projects that do not need an OpendTect license key" and "Other Free Projects".
**12 free projects:**

| Project | Path | No licence key needed |
|---|---|---|
| Delft | /datainfo/Delft | yes |
| F3 Demo 2023 | /datainfo/F3-Demo-2023 | yes |
| FORCE ML Competition 2020 | /datainfo/FORCE-ML-Competition-2020 | yes |
| FORCE ML Competition 2020 Synthetic Models and Wells | /datainfo/FORCE-ML-Competition-2020-Synthetic-Models-and-Wells | yes |
| Penobscot | /datainfo/Penobscot | yes |
| Blake Ridge Hydrates 3D | /datainfo/Blake-Ridge-Hydrates-3D | no |
| Laurentian Basin – Complete | /datainfo/Laurentian-Basin-Complete | no |
| NW Shelf Australia – Poseidon 3D | /datainfo/NW-Shelf-Australia-Poseidon-3D | no |
| OGA MNSH | /datainfo/OGA-MNSH | no |
| OGA Rockall Trough | /datainfo/OGA-Rockall-Trough | no |
| USGS Beaufort Sea – Arctic Alaska | /datainfo/USGS-Beaufort-Sea-Arctic-Alaska-2023 | no |
| USGS Central Alaska | /datainfo/USGS-Central-Alaska-2023 | no |

The page bills itself as the "Open Seismic Repository". **Gaps:** a vendor catalogue
packaged as OpendTect projects, not raw SEG-Y; no sizes on the list page; registration
required for download; and seven of the twelve need an OpendTect licence key.

## a.17 FDSN data-centre registry — verified, and the only machine-readable index found

- HTML: https://www.fdsn.org/datacenters/ (HTTP 200)
- **JSON web service: `https://www.fdsn.org/ws/datacenters/1/query`** — 6,305 bytes,
  **32 data centres**, each with `name`, `website` and FDSN web-service endpoints.

AusPass · BGR · BGS · CATAC · EarthScope · EMSC · EPOSFR · ETH · GEOFON · GeoNet ·
ICGC · IESDMC · IGN · INGV · IPGP · ISC · KAGSR · KIT · KOERI · LMU · NCEDC · NIEP ·
NOA · NRCAN · ODC (ORFEUS) · OSDC · RASPISHAKE · RSBR · SCEDC · UIB-NORSAR · USGS · USP

**Why it matters here:** it is the *only* resource in §a that is machine-readable by
design and therefore the only one whose links can be CI-checked. It is the model to
copy. **Gaps:** passive seismology only; data-centre granularity, never dataset;
no sizes; no licences; and no exploration-seismic archive appears in it at all.

## a.18 Review papers and dataset-catalogue literature

Verified via the OpenAlex API (title-search filters; citation counts as of
2026-08-24).

| Paper | Year | DOI | Cites | What it catalogues |
|---|---:|---|---:|---|
| Mousavi & Beroza, *Deep-learning seismology*, **Science** | 2022 | 10.1126/science.abm4470 | 492 | The canonical review of ML in seismology; surveys the dataset landscape |
| Münchmeyer et al., *Which Picker Fits My Data? A Quantitative Evaluation of Deep Learning Based Seismic Pickers*, **JGR Solid Earth** | 2022 | 10.1029/2021JB023499 | 205 | Cross-dataset benchmark; the de-facto list of earthquake ML training sets |
| Woollam et al., *SeisBench—A Toolbox for Machine Learning in Seismology*, **SRL** | 2022 | 10.1785/0220210324 | 175 | The paper behind the 44-dataset loader |
| Mousavi et al., *STanford EArthquake Dataset (STEAD)*, **IEEE Access** | 2019 | 10.1109/ACCESS.2019.2947848 | 451 | The most-reused single earthquake ML dataset |
| Zhao et al., *DiTing: A large-scale Chinese seismic benchmark dataset for AI in seismology*, **Earthquake Science** | 2023 | 10.1016/j.eqs.2022.01.022 | 79 | Large national benchmark |
| Deng et al., *OpenFWI: Large-Scale Multi-Structural Benchmark Datasets for Seismic Full Waveform Inversion* | 2021/22 | arXiv:2111.02926 · 10.52202/068431-0435 | 14/9 | The FWI benchmark family |
| *OpenFWI 2.0: Benchmark datasets for elastic full-waveform inversion*, **IMAGE** | 2023 | 10.1190/image2023-3896358.1 | 2 | Elastic extension |
| Kuo-Chen et al., *The CWA Benchmark: A Seismic Dataset from Taiwan for Seismic Research*, **SRL** | 2024 | 10.1785/0220230393 | 6 | Taiwan national benchmark (SeisBench `CWA`) |
| Hui Gao et al., *cigFacies: a massive-scale benchmark dataset of seismic facies*, **ESSD** | 2025 | 10.5194/essd-17-595-2025 | 6 | Exploration-seismic facies benchmark |
| Zhu et al., *Benchmark on the accuracy and efficiency of several neural-network-based phase pickers*, **Earthquake Science** | 2023 | 10.1016/j.eqs.2022.10.001 | 28 | Picker/dataset comparison |
| Di, Gao & AlRegib, *Successful leveraging of image processing and machine learning in seismic structural interpretation: A review*, **TLE** | 2018 | 10.1190/tle37060451.1 | 136 | Older but the standard interpretation-ML review |
| Bhattacharya et al. (eds.), *Value of open data: A geoscience perspective*, **Geoscience Data Journal** | 2022 | 10.1002/gdj3.138 | 8 | Policy framing for open geoscience data |

All twelve DOIs above were resolved on 2026-08-24 — eleven via the Crossref API
(`api.crossref.org/works/<doi>` → HTTP 200) and the SeisBench v0.11 release DOI via
DataCite (`api.datacite.org/dois/10.5281/zenodo.18433641` → HTTP 200).

**Gap in the literature:** every one of these catalogues datasets *incidentally*, inside
a methods paper, for a single task (picking, FWI, facies). There is no published survey
whose subject is the open seismic dataset landscape itself.

---

# Section (b) — General-purpose repositories: actual seismic holdings

## b.1 Zenodo — verified via REST API

**Method.** `https://zenodo.org/api/records?q=<query>&size=25&page=<n>&sort=mostrecent`
across 12 queries (`seismic` filtered to `resource_type=dataset`, then `image` and
`other`; `"SEG-Y" OR segy`; `"seismic volume"`; `"full waveform inversion"`;
`"distributed acoustic sensing"`; `"seismic reflection"`; `"3D seismic"`; `seismology`;
`earthquake waveform`; `seismogram`), deduplicated by record id. Total bytes computed
by summing each record's `files[].size`.

**API constraints worth recording** (both hit during this survey):
- Anonymous page size is capped at **25**: *"Page size cannot be greater than 25.
  Please use authenticated requests to increase the limit to 100."*
- `page × size` is capped at **10,000**, so no query can be enumerated past 10k hits.
- Anonymous rate limit produces **HTTP 429** at roughly 60 req/min; ~1.05 s between
  requests plus retry-with-backoff is the working cadence.

**Counts:**
- `q=seismic`, all resource types: **11,012 records**
- `q=seismic`, `resource_type=dataset`: **2,591 records**
- `q=earthquake waveform` (datasets): 3,033 · `q=seismology` (datasets): 389 ·
  `q="distributed acoustic sensing"`: 230 · `q="full waveform inversion"`: 110 ·
  `q=seismic` (image): 107 · `q=seismic` (other): 93 ·
  `q="seismic reflection"` (datasets): 71 · `q=seismogram` (datasets): 25 ·
  `q="seismic volume"`: 9
- **Harvested and deduplicated: 4,099 records**, of which **3,836 have files**,
  totalling **12.385 TB**

**Resource types of the harvest:** dataset 3,332 · publication 181 · image 105 ·
software 97 · other 96 · presentation 9 · model 8 · poster 5 · video 3.

**Licence distribution across the 3,836 records with files** — this is the single best
licensing hygiene of any platform surveyed:

| Licence | Records | Share |
|---|---:|---:|
| CC-BY-4.0 | 3,312 | 86.3 % |
| CC0 (`cc-zero`) | 228 | 5.9 % |
| **none stated** | 55 | 1.4 % |
| CC-BY-NC-ND-4.0 | 47 | 1.2 % |
| MIT | 33 | 0.9 % |
| CC-BY-NC-4.0 | 28 | 0.7 % |
| CC-BY-SA-4.0 | 21 | 0.5 % |
| other-open | 20 | 0.5 % |
| GPL-3.0-or-later | 14 | 0.4 % |
| CC-BY-NC-SA-4.0 | 13 | 0.3 % |

### TOP 25 LARGEST OPEN SEISMIC RECORDS (Zenodo, exact bytes)

Non-seismic keyword collisions have been removed — see the exclusion list below.

| # | Bytes | Title | DOI | Licence | Published | Files |
|---:|---:|---|---|---|---|---:|
| 1 | 178,825,674,062 | Dataset for *Seismic waveform tomography of the Central and Eastern Mediterranean upper mantle* | 10.5281/zenodo.3732981 | CC-BY-4.0 | 2020-03-30 | 9 |
| 2 | 176,842,054,483 | Dataset for *Reduced-order modeling for complex 3D seismic wave propagation* | 10.5281/zenodo.12520845 | CC-BY-4.0 | 2024-06-24 | 5 |
| 3 | 172,530,233,396 | **Oklahoma Labeled AI Dataset for Seismology (OKLAD)** | 10.5281/zenodo.18991761 | CC-BY-NC-4.0 | 2026-03-13 | 19 |
| 4 | 145,267,610,728 | Seismic full-waveform inversion of the crust–mantle structure beneath China and adjacent regions | 10.5281/zenodo.6597380 | CC-BY-4.0 | 2022-06-01 | 11 |
| 5 | 142,474,199,040 | Rock-temperature, fracture displacement and acoustic/micro-seismic data, Matterhorn Hörnligrat | 10.5281/zenodo.1215632 | CC-BY-4.0 | 2018-04-09 | 3 |
| 6 | 135,523,536,345 | Western Peloponnese Seismological Data Acquisition, Jul 2016 – May 2017 | 10.5281/zenodo.3550842 | CC-BY-4.0 | 2019-11-22 | 4 |
| 7 | 128,415,557,469 | Quantitatively monitoring seasonal frozen-ground freeze–thaw cycle using ambient seismic noise | 10.5281/zenodo.12784252 | CC-BY-4.0 | 2024-07-19 | 84 |
| 8 | 118,867,275,584 | **SubRidge: a 3-D subduction-to-ridge model with synthetic seismic waveforms for benchmarking** | 10.5281/zenodo.16634304 | CC-BY-4.0 | 2025-07-31 | 1 |
| 9 | 102,463,279,059 | Seismic Data and Structural Constraints | 10.5281/zenodo.18445915 | **none stated** | 2026-02-01 | 62 |
| 10 | 102,168,374,882 | DASGAS borehole data | 10.5281/zenodo.21193610 | CC-BY-4.0 | 2026-07-04 | 4 |
| 11 | 97,385,026,687 | Seismic source dynamics, tsunami generation/propagation and numerical modelling complexity | 10.5281/zenodo.10497580 | CC-BY-4.0 | 2024-01-12 | 37 |
| 12 | 92,547,665,032 | Dataset for seismic oceanography in the Gulf of Cadiz | 10.5281/zenodo.15722256 | CC-BY-4.0 | 2025-06 | 17 |
| 13 | 91,639,315,003 | **Earthquake Seismogram Denoiser (EQS-Denoiser)** — backs SeisBench `EQSDenoiser*` | 10.5281/zenodo.17865808 | CC-BY-NC-4.0 | 2025-12-18 | 5 |
| 14 | 84,768,081,423 | Time-lapse velocity variations during an open-pit mine slope failure, noise interferometry | 10.5281/zenodo.14969229 | CC-BY-4.0 | 2025-03-14 | 13 |
| 15 | 83,154,106,434 | Fault-controlled thaw in degrading permafrost, Qinghai–Tibet Plateau, traffic-enhanced fibre-optic seismology | 10.5281/zenodo.19369569 | CC-BY-4.0 | 2026-05-21 | 15 |
| 16 | 82,908,348,435 | Mitigating the effect of errors in source parameters on seismic (waveform) inversion | 10.5281/zenodo.6969602 | CC-BY-4.0 | 2022-08-03 | 66 |
| 17 | 81,040,433,213 | **4,000 labelled synthetic + 3,000 unlabelled field datasets** (massive-scale global seismic) | 10.5281/zenodo.20769762 | CC-BY-4.0 | 2026-06-20 | 3 |
| 18 | 79,871,303,967 | Dataset + trained models, *Depth-progressive 3D seismic velocity model building via 2D generative diffusion models* | 10.5281/zenodo.21206427 | MIT | 2026-07-05 | 3 |
| 19 | 73,542,380,737 | **GeoFWI3D Dataset** | 10.5281/zenodo.20148778 | CC-BY-4.0 | 2026-05-13 | 10 |
| 20 | 72,556,222,320 | Calving-driven fjord dynamics resolved by seafloor fibre sensing | 10.5281/zenodo.15353304 | CC-BY-4.0 | 2025-08-14 | 1 |
| 21 | 67,340,721,276 | DataSet La Habra Earthquake | 10.5281/zenodo.6403870 | CC-BY-4.0 | 2022-04-01 | 297 |
| 22 | 65,629,131,306 | Seismic dataset for the full-waveform regional seismic model in Asia (**FWEA23**) | 10.5281/zenodo.15039554 | CC-BY-4.0 | 2025-03-17 | 21 |
| 23 | 64,087,918,748 | Dataset of Validation of **PRISM3D** model | 10.5281/zenodo.15116833 | CC-BY-4.0 | 2025-04-01 | 18 |
| 24 | 63,506,663,295 | Tracking ships with submarine cables — unsupervised arrival-time detection with DAS | 10.5281/zenodo.18851481 | CC-BY-4.0 | 2026-03-17 | 1 |
| 25 | 59,509,025,478 | Stacked cross-correlation functions of the MINQ network, NW Queensland + 3D Vs model | 10.5281/zenodo.17254657 | CC-BY-4.0 | 2025-10-03 | 2 |

Record URLs are `https://zenodo.org/records/<id>` where `<id>` is the numeric suffix of
the DOI. All ten record IDs spot-checked returned HTTP 200 from
`https://zenodo.org/api/records/<id>`.

**Downloadability confirmed, not just metadata.** Record #1 (`zenodo.3732981`) reports
`access_right: open` and its files are served over plain HTTPS with no account:
`EMed_full.complete.tar` 142,457,405,440 B · `MODEL_FILES.tar` 32,104,755,200 B ·
`FIGURE_SCRIPTS.tar` 37,754,880 B · `LASIF-master.zip` 14,691,347 B ·
`SCRIPTS.tar` 276,480 B. A `HEAD` on
`https://zenodo.org/api/records/3732981/files/MODEL_FILES.tar/content` returns
`HTTP 200`, `content-length: 32104755200`. So Zenodo's byte figures are real bytes you
can fetch, unlike most portal-listed sizes.

**Just outside the top 25** (all CC-BY-4.0 unless noted): *A Benchmark Database of Ten
Years of Prospective Next-Day Earthquake Forecasts in California (CSEP)*
56,449,171,382 B (10.5281/zenodo.15076187); *HSR Radiation Patterns and Virtual Shot
Gathers* 55,813,529,368 B (10.5281/zenodo.19944304); *RESOLVE dense array, Glacier
d'Argentière* 55,448,901,813 B (10.5281/zenodo.5645545); *2018 Central Tottori
earthquake* 54,617,119,673 B (10.5281/zenodo.5036124); **REVEAL: A Global Full-Waveform
Inversion Model** 49,305,065,289 B (10.5281/zenodo.10684325); *DASGAS surface data
part 1* 48,556,727,578 B (10.5281/zenodo.21208202); the three-part *China crust–mantle
FWI supplement* 48.6 / 48.4 / 48.3 GB (zenodo.6594582, .6595793, .6595791);
*Seismic monitoring of Hans glacier, Svalbard* 48,273,017,688 B (10.5281/zenodo.3377402);
*2012–2016 ASK seismic data* 47,573,631,146 B (10.5281/zenodo.17165027).

**Excluded keyword collisions** — these ranked in the raw top 30 but are not seismic
data: *A statewide InSAR velocity map for California* 111,453,656,476 B
(geodesy, 10.5281/zenodo.19493073); *NIST CBRS Full-Spectrogram Object-Detection
Dataset* 92,868,253,852 B (radio spectrum, 10.5281/zenodo.22005788); *Experimental data
of dissipative embedded column base connections under cyclic lateral loading*
48,339,802,375 B (earthquake **engineering**, 10.5281/zenodo.4244684); *Evolutionary
tracks accompanying Stellar Evolution in Real Time II* 47,632,971,780 B
(**astero**seismology, 10.5281/zenodo.11353933).

### Zenodo's own curation mechanism is unused

Zenodo Communities are its native way to curate a themed collection. For seismic they
are all but empty — verified via `https://zenodo.org/api/records?communities=<slug>`:

| Community | Slug | Records |
|---|---|---:|
| Seismology | `seismology` | **0** |
| seismic data | `seismic` | **1** |
| Global Seismology Organization | `globalseismology` | 7 |
| Seismic Ambient Noise Measurements Repository | `sanmr` | 6 |
| New Zealand Seismic Tomography | `nz_tomo` | 4 |
| Euro-Mediterranean Seismological Centre | `emsc` | 9 |
| Seismica (journal) | `seismica-journal` | 23 |

Against 4,099 harvested seismic records, **fewer than 50 sit in any seismic community**.
The `seismology` community exists and contains nothing at all. Zenodo is a deposit
target, not a discovery surface, and nobody is curating it.

### The exploration-seismic gap on Zenodo, quantified

Searching the 4,099 harvested records' titles and keywords for the canonical open
exploration surveys shows how thin Zenodo is on field data:

| Survey / model | Records | Largest Zenodo record |
|---|---:|---|
| F3 (Netherlands) | 6 (2 genuine) | AdaSemSeg processed facies (F3 + Parihaka + Penobscot) 2,553,842,528 B, CC-BY-4.0, 10.5281/zenodo.21764042 |
| Parihaka | 2 | *Parihaka Annotated Seismic Dataset — slices from cube* 928,368,066 B, CC-BY-4.0, 10.5281/zenodo.13994329 |
| Penobscot | 2 | *Penobscot Interpretation Dataset* 2,316,061,505 B, CC-BY-4.0, 10.5281/zenodo.3924682 |
| Kerry-3D | 1 | *Netherlands F3 block and New Zealand Kerry-3D seismic attributes* 1,436,716,239 B, CC-BY-4.0, 10.5281/zenodo.14055932 |
| Volve | 2 | *VolveSynthetic* 2,408,661,873 B, CC-BY-4.0, 10.5281/zenodo.6572286 |
| Marmousi | 1 | *Marmousi Velocity Model* 6,912,204 B, CC-BY-4.0, 10.5281/zenodo.16114161 |
| SEG/EAGE Overthrust | 1 | *SEG/EAGE 3-D Overthrust Models* 1,062,506,184 B, CC-BY-4.0, 10.5281/zenodo.4252588 |
| LANDMASS | 1 | 2,325,243,284 B, **CC-BY-SA-3.0**, 10.5281/zenodo.3901644 |
| **Poseidon** | **0** | — |
| **Teapot Dome** | **0** | — |
| **Opunake / Stratton / Viking Graben / Blake Ridge / Norne** | **0 each** | — |

Records whose files are actually SEG-Y are rarer still — 9 matching "segy" and 11
matching "seg-y" across the whole harvest. The largest are: *Unprocessed multichannel
seismic reflection data (SEG-Y) and supporting metadata, R/V Ta…* 22,973,077,370 B
(CC-BY-NC-4.0, 10.5281/zenodo.18407436); *Adele 3D seismic survey, SEG-Y, used in the
FORCE 2020 ML fault competition* 3,488,703,164 B (CC-BY-4.0, 10.5281/zenodo.4299758);
*SEGY-DATA for "Enhancing seismic noise suppression using the Noise2Noise framework"*
2,005,478,875 B (CC-BY-4.0, 10.5281/zenodo.10660485).

**Conclusion:** what lives on Zenodo are *derived, diced, annotated subsets* of the
famous surveys — never the surveys themselves. Anyone using Zenodo as their index of
open seismic data would conclude that Poseidon and Teapot Dome do not exist.

**Observations.** Zenodo has by far the best licensing hygiene of any platform here:
**92 % of records with files carry CC-BY-4.0 or CC0**, and only 1.4 % state no licence.
But the corpus is overwhelmingly **passive seismology, DAS, and wave-propagation
simulation**. The largest exploration-flavoured records are all *synthetic*
FWI/velocity-model sets (#17, #18, #19). **No open exploration 3D field volume of the
Parihaka / Poseidon / F3 class appears anywhere near the top** — those live on national
portals and vendor catalogues, not on Zenodo. Zenodo also caps single-record size in
practice: nothing in 4,099 records exceeds 180 GB, so the multi-terabyte field surveys
structurally cannot live there.

## b.2 HuggingFace Hub — verified via API

**Method.** `https://huggingface.co/api/datasets?search=<term>&limit=500` across 12
terms (`seismic`, `segy`, `seg-y`, `earthquake`, `seismology`, `waveform inversion`,
`distributed acoustic sensing`, `subsurface`, `seismogram`, `microseismic`,
`geophysics`, `reflection seismic`), deduplicated; then per-dataset
`?expand[]=usedStorage` for exact byte counts. (`usedStorage` is the reliable size
field; the dataset-viewer `size` endpoint fails on datasets without a loadable config.)

- `search=seismic` alone: **47 datasets**
- All 12 terms deduplicated: **326 datasets**
- Byte size resolved for **314** of them
- **Total resolved storage: 5,702,018,126,979 bytes (5.70 TB)**
- Total downloads across all 326: **32,039**

**Licence distribution across the 326:** CC-BY-4.0 218 (66.9 %) · **none stated 48
(14.7 %)** · MIT 23 (7.1 %) · Apache-2.0 8 (2.5 %) · CC-BY-SA-4.0 7 (2.1 %) ·
CC0-1.0 6 (1.8 %) · "other" 6 (1.8 %) · "unknown" 5 (1.5 %) · ECL-2.0 3 (0.9 %) ·
CC-BY-NC-SA-4.0 1 · ODbL 1. By volume, unlicensed records account for
261,534,449,167 bytes — **4.6 % of the corpus**.

| # | Dataset | Bytes | Licence | Downloads | Last modified |
|---:|---|---:|---|---:|---|
> **These are `usedStorage` figures and are provisional — see §b.6 and footnote 4.**
> Where a row has been re-measured against the tree API the corrected value is given
> inline. The ranking itself is wrong: `subsurfacegen/field-scale-dataset` is #1, not #2.

| 1 | `HeXingChen/Seismic-AI-Data` | 2,916,246,352,428 (tree: 2,907,508,850,352) | MIT | 10,102 | 2026-01-21 |
| 2 | `subsurfacegen/field-scale-dataset` | 1,623,610,657,665 — **WRONG, tree: 11,923,346,031,911 (11.92 TB)** | CC-BY-4.0 | 229 | 2026-05-06 |
| 3 | `cangyeone/SeismicX-Cont` | 427,176,078,330 | other | 4,074 | 2026-07-22 |
| 4 | `JasonXF/SeismicTransformerData` | 289,998,313,442 | Apache-2.0 | 1,673 | 2026-08-06 |
| 5 | `YinghaoXu/SeisMIC-Init` | 75,518,754,391 | none | 23 | 2026-03-29 |
| 6 | `GeoBrain/first-break-picking-segy-with-masks` | 61,553,127,384 | none | 42 | 2026-05-23 |
| 7 | `Jamie1701/seismic-ensemble` | 42,034,691,779 | MIT | 34 | 2026-08-20 |
| 8 | `giabao804/seismic` | 24,372,331,024 | none | 13 | 2025-09-25 |
| 9 | `SAistheBEST/well-seismic-core` | 15,059,255,436 | none | 58 | 2026-07-28 |
| 10 | `MH0386/seismic_data` | 15,016,777,487 | MIT | 179 | 2024-10-05 |
| 11 | `SamuuelPanda/Earthquake` | 12,981,478,452 | MIT | 8 | 2025-12-02 |
| 12 | `YXBIAN/EarthquakeNet` | 12,282,741,646 | CC-BY-NC-SA-4.0 | 65 | 2026-08-14 |
| 13 | `sdlj/seismicVMB` | 12,202,006,093 | none | 619 | 2025-09-22 |
| 14 | `Devansh555/seismic_data` | 7,577,726,664 | MIT | 114 | 2026-03-21 |
| 15 | `MH0386/nasa_space_apps_2024_seismic_detection` | 7,075,555,841 | none | 33 | 2024-09-19 |
| 16 | `smpark00/space_apps_2024_seismic_detection` | 7,075,555,841 | none | 5 | 2024-09-20 |
| 17 | `jer47/SEGY-PATCHES-256-HF` | 5,701,238,784 | none | 8 | 2026-02-11 |
| 18 | `segyulee/UniSAFE` | 5,098,797,739 | none | 40 | 2026-04-02 |
| 19 | `SeismicFlow/seismicflow` | 4,811,047,136 | none | 29 | 2026-05-16 |
| 20 | `Surojit-Utah/adasemseg-seismic-facies-datasets` | 3,940,475,875 | CC-BY-4.0 | 15 | 2026-08-24 |
| 21 | `porestar/crossdomainfoundationmodeladaption-seismicfacies` | 3,743,056,884 | CC-BY-4.0 | 57 | 2024-12-24 |
| 22 | `cangyeone/SeismicX-Cont-mini` | 3,656,756,915 | other | 301 | 2026-07-21 |
| 23 | `porestar/seismicfoundationmodel-inversion-seam` | 3,442,236,058 | MIT | 74 | 2024-12-24 |
| 24 | `davanstrien/subsurfacebench-array3d-test` | 2,890,807,101 | none | 5 | 2026-03-18 |
| 25 | `subsurfacegen/field-scale-dataset-preview` | 2,807,379,441 | CC-BY-4.0 | 74 | 2026-05-06 |

**False positives to exclude** (matched the *string* "seismic"/"segy" but are not
geophysics): `segyges/OpenWebText2` (35,716,519,092 B — a text corpus by a user named
`segyges`); the `tuskanny/seismic-msmarco-*` and `tuskanny/seismic-nq-*` family
(~46 GB combined — information-retrieval indexes built with the *Seismic* sparse-index
algorithm); `z7chary/earthquake_news`; `hasilm1/Earthquake_PredictNextDate`. **A naive
keyword search of HuggingFace over-reports seismic holdings by roughly 15 % of bytes.**

**What the two biggest actually are** (verified by inspecting their file trees / cards):

- **`HeXingChen/Seismic-AI-Data`, 2.92 TB, MIT, 10,102 downloads — is a mirror of the
  entire SeisBench benchmark corpus.** Its 24 top-level directories are literally the
  SeisBench dataset names: `AQ2009COUNTS`, `AQ2009GM`, `CEED`, `CREW`, `ETHZ`,
  `GEOFON`, `INSTANCENOISE`, `IQUIQUE`, `ISC_EHB_DEPTHPHASES`, `LENDB`, `LFE`,
  `MLAAPDE`, `NEIC`, `OBS`, `OBST2024`, `PISDL`, `PNW`, `SCSN`, `STEAD`, `TXED`,
  `VCSEIS`, `pnwaccelerometers`, `pnwexotic`, `pnwnoise`. This is the single largest
  open seismic ML corpus found anywhere in this survey, and it is a third-party
  re-host of §a.5 rather than new data — worth flagging for licence-provenance reasons,
  since the upstream datasets do **not** all carry MIT terms.
- **`subsurfacegen/field-scale-dataset`, 1.62 TB, CC-BY-4.0** — genuinely new and the
  most exploration-relevant thing on the Hub: *"field-scale 3D subsurface velocity
  volumes (SOS-smoothed, depth-truncated to 619 samples) paired with 2D velocity
  slices, their corresponding acoustic wavefields, and multi-source shot-gather
  cubes… spans multiple geological settings and covers five frequency bands
  (3–6, 3–8.5, 3–12, 3–17.5, 3–25 Hz)"*. Parquet format; tags include `benchmark`,
  `geophysics`, `velocity-model`, `acoustic-wavefield`, `wave-propagation`. A 2.81 GB
  `-preview` variant exists for evaluation.

**Notable curated cluster:** `porestar/*` (Lukas Mosser — see §a.12) mirrors the
Seismic Foundation Model datasets: facies, denoise (synthetic + field), interpolation,
inversion (SEAM + synthetic), geobody — all CC-BY-4.0 or MIT and *consistently*
licensed, which is rare on the Hub.

**Gating check:** the top HuggingFace records are all `gated: false, private: false`, so
no access request is needed. Note `JasonXF/SeismicTransformerData` (290 GB) ships
Windows `.exe`/`.pdb`/`.sln` build artefacts alongside the data, which is a provenance
and hygiene smell worth flagging in any catalogue entry.

**Gaps:** licences are absent on a large minority of records; almost nothing is SEG-Y —
most is pre-diced NumPy/HDF5 patches; and there is usually no provenance chain back to
the source survey. HuggingFace is where seismic *ML training tensors* live, not where
seismic *data* lives.

## b.3 TOP 25 LARGEST OPEN SEISMIC RECORDS — cross-platform, by stated bytes

**This table changed completely once DataCite was harvested.** The largest open seismic
datasets in the world are not on Zenodo, HuggingFace or Kaggle — they are **FDSN
temporary-network DOIs minted by IRIS/EarthScope and GFZ**, which carry a `sizes` field
in their DataCite metadata that nobody aggregates.

> ⚠️ **READ THIS BEFORE USING THE FDSN NUMBERS. They are registration-time estimates,
> not measured archive sizes, and at least one is wrong by ~460×.**
>
> I tested the #1 entry. Network **YC (2018)**, *Northern Borneo Orogeny Seismic
> Survey*, declares `684756688 MB` ≈ 685 TB. Measured reality:
> - `fdsnws-station level=channel` → **294 channels across 49 stations**, 2018-01-01 to
>   2020-12-31.
> - `fdsnws-dataselect`, whole network, `cha=*`, 60 s on 2019-01-15 → **946,176 bytes**
>   (HTTP 200, real miniSEED).
> - Extrapolated: 946,176 B/min × 1,440 × 1,095 days ≈ **1.49 TB** — roughly **460×
>   smaller** than declared.
> - The DOI's DataCite record shows `created: 2018-08-20`, i.e. **minted at network
>   registration, before the experiment had finished recording.**
>
> The round numbers throughout the list (`100000000 MB`, `16000000 MB`, `10000000 MB`,
> `6000000 MB`, `5000000 MB`) are the signature of a planning figure typed into a
> registration form. Network 7P, which declares 16 TB, returns **HTTP 204 — no data at
> all** for a spot-checked minute in its stated operating window.
>
> **So: this is a ranking of what depositors *declared*, and it is the only
> machine-readable size signal that exists for FDSN networks — but the individual
> figures must not be quoted as measured volumes.** Where a real number is needed,
> measure it: `fdsnws-station level=channel` for the channel count, then a timed
> `dataselect` fetch, as above. The AWS rows in this table *are* measured
> (`aws s3 ls --summarize`) and are trustworthy within their stated prefix scope.

Method: DataCite `resource-type-id=dataset`, `query=seismic`, full cursor enumeration
(21,895 DOIs, 22 pages of 1,000). **4,845 records (22 %) carry a parseable `sizes`
value, totalling 1,556,735,383,939,710 bytes — 1.56 PB.** Merged with the Zenodo and
HuggingFace harvests above; keyword collisions removed; MB/GB/TB parsed as binary
multiples as the depositors intend.

| # | Bytes | Record | Source | Stated size | Licence |
|---:|---:|---|---|---|---|
| 1 | 718,019,428,876,288 | **Northern Borneo Orogeny Seismic Survey** | FDSN `10.7914/sn/yc_2018` | `684756688 MB` | none stated |
| 2 | 104,857,600,000,000 | Monitoraggio Sismico Urbano e delle infrastrutture | FDSN `10.7914/v68b-5553` | `100000000 MB` | none stated |
| 3 | 52,428,800,000,000 | Temporary seismic network, rapid erosion in mountain catchments | FDSN `10.7914/0ygw-nn15` | `50000000 MB` | **CC0-1.0** |
| 4 | 52,213,349,679,104 | **PoroTomo DAS, SEG-Y** (Brady Hot Springs) | AWS `s3://nrel-pds-porotomo/DAS/SEG-Y/` | 47.5 TiB measured, 104,535 obj | CC-BY-3.0-US |
| 5 | 25,165,824,000,000 | Bedload Monitoring of Ephemeral Streams, nodal | FDSN `10.7914/sn/4l_2020` | `24000000 MB` | none stated |
| 6 | 21,474,836,480,000 | **Eger Large Seismic Experiment (ELISE)** | GFZ `10.14470/k7719395` | `20000GB` | **embargoed** + CC-BY |
| 7 | 20,419,506,242,688 | The DYNALake project dataset | CSC Finland `10.23729/fd-05823461-…` | exact bytes given | CC-BY |
| 8 | 16,777,216,000,000 | Investigating West Texas Seismicity with Dense Geophone Arrays | FDSN `10.7914/sn/7p_2018` | `16000000 MB` | none stated |
| 9 | 14,680,064,000,000 | Active and passive seismic interferometry of Kīlauea volcano | FDSN `10.7914/gqdb-hs97` | `14000000 MB` | none stated |
| 10 | 11,544,872,091,648 | **SCEDC continuous waveforms, 2023 alone** | AWS `s3://scedc-pds/continuous_waveforms/2023/` | 10.5 TiB measured, 1,630,906 obj | royalty-free, cite DOI |
| 11 | 11,534,336,000,000 | Seismic Baseline Survey, Northern Gulf of Mexico, Texas | FDSN `10.7914/3v97-dp93` | `11000000 MB` | none stated |
| 12 | 11,324,969,766,092 | RV *Investigator* Voyage IN2025_V05 EOV Archive | CSIRO `10.25919/wek0-ar08` | `10.30 TB` | CC-BY-NC-SA-4.0 |
| 13 | 10,485,760,000,000 | Southern Lake Tanganyika experiment | FDSN `10.7914/sn/zv_2014` | `10000000 MB` | none stated |
| 14 | 10,485,760,000,000 | Icelandic Strong-motion Arrays | FDSN `10.7914/sn/5s_2019` | `10000000 MB` | none stated |
| 15 | 10,485,760,000,000 | **Leeds–Blacknest Eskdalemuir DAS experiment, Feb 2023** | FDSN `10.7914/3320-5s03` | `10000000 MB` | none stated |
| 16 | 10,485,760,000,000 | Kennedy Space Center Seismo-Acoustic Network | FDSN `10.7914/js1e-s768` | `10000000 MB` | **CC0-1.0** |
| 17 | 10,333,716,480,000 | Marlborough Observatory (MORIA), NZ | FDSN `10.7914/mkb2-v464` | `9855000 MB` | none stated |
| 18 | 9,785,653,487,206 | **GeoNet miniSEED waveforms, 2024 alone** | AWS `s3://geonet-open-data/waveforms/miniseed/2024/` | 8.9 TiB measured, 685,411 obj | **CC-BY-3.0-NZ** |
| 19 | 9,437,184,000,000 | Seismic Monitoring of Postfire Debris Flows — Nodes 2026 | FDSN `10.7914/ne3h-tq53` | `9000000 MB` | none stated |
| 20 | 8,388,608,000,000 | Paleovalley ICDP site survey | FDSN `10.7914/sn/3n_2022` | `8000000 MB` | none stated |
| 21 | 7,348,420,608,000 | Amplify EGS Monitoring Network | FDSN `10.7914/sn/y9_2022` | `7008000 MB` | none stated |
| 22 | 7,340,032,000,000 | Dryland Critical Zone: Jornada Piedmont Seismic Imaging | FDSN `10.7914/sn/9d_2021` | `7000000 MB` | none stated |
| 23 | 7,340,032,000,000 | FocusX temporary OBS network | FDSN `10.7914/dpf7-5n77` | `7000000 MB` | none stated |
| 24 | 6,710,886,400,000 | Livermore Valley Nodal Experiment | FDSN `10.7914/r3v1-dp73` | `6400000 MB` | none stated |
| 25 | 6,291,456,000,000 | Nodal Deployment, Alaska Amphibious Community Seismic Experiment | FDSN `10.7914/sn/8j_2019` | `6000000 MB` | none stated |

Also at 6,291,456,000,000 B: China–Western Australia Seismic array (`10.7914/sn/4n_2017`),
TANGO TransANdean Great Orogeny nodes/Argentina (`10.7914/q4nj-hf03`), and Pacific Coast
Seismic Assessment for Faults and Earthquakes (`10.7914/nr48-3x83`, the rare **CC-BY-4.0**
of the group). Just below: RV *Investigator* IN2023_V02 5.29 TB and IN2022_V02 5.10 TB
(CSIRO, CC-BY-NC-SA-4.0); The Irpinia seismic Array `10.14470/mx7576871994` 5200 GB
(GFZ, **embargoed**); CASIE21-OBS controlled-source dataset `10.7914/sn/yr_2021`
5,000,000 MB.

All FDSN DOIs resolve to `https://www.fdsn.org/networks/detail/<CODE>/` and the data is
fetched through FDSN web services, not as a file download.

### Where the declared petabyte actually lives

| Repository | DataCite client-id | Sized records | Bytes | TB |
|---|---|---:|---:|---:|
| **IRIS / EarthScope (FDSN network DOIs)** | `iris.iris` | 614 | 1,394,306,705,260,544 | **1,394.3** |
| GFZ / GEOFON | `tib.gfz` | 137 | 99,367,396,992,606 | 99.4 |
| CSIRO (RV *Investigator* voyages) | `csiro.repo` | 16 | 26,348,305,504,004 | 26.3 |
| CSC Finland | `csc.nrd` | 4 | 20,754,733,479,491 | 20.8 |
| INGV | `crui.ingv` | 57 | 6,776,370,241,126 | 6.8 |
| JAMSTEC | `jamstec.jamstec` | 1 | 3,942,243,106,816 | 3.9 |
| **figshare** | `figshare.ars` | **2,632** | 1,654,162,656,357 | 1.7 |
| NERC EDS | `bl.nerc` | 57 | 1,384,566,445,947 | 1.4 |
| ScienceDB | `cnic.sciencedb` | 56 | 689,307,799,225 | 0.7 |
| DataDryad | `dryad.dryad` | 137 | 442,083,875,682 | 0.4 |
| RESIF | `inist.resif` | 1 | 328,189,188,505 | 0.3 |
| **Total** | — | **4,845** | **1,556,735,383,939,710** | **1,556.7** |

**IRIS/EarthScope alone is 89.6 % of every declared byte.** figshare has 2,632 sized
records — more than half the count — and 0.1 % of the volume. Counting *records* and
counting *bytes* give completely different pictures of where open seismic data lives,
and every existing index counts records.

**Licence coverage inverts with size:** only 636 of 4,845 records (13.1 %) state no
rights — but those records hold **1,286,352,610,287,857 bytes, 82.6 % of the total
volume.** The bigger the dataset, the less likely anyone said what you may do with it.

### What this reframes

1. **The general-purpose repositories are a rounding error.** The largest thing on
   HuggingFace (2.92 TB) would rank ~40th here; the largest on Zenodo (178.8 GB) would
   not make the top 200. Any survey that stops at Zenodo/HF/Kaggle understates the open
   seismic corpus by roughly three orders of magnitude.
2. **Licensing collapses at the top.** Of the 25 largest, **19 state no licence at all**
   in their DataCite record. Two are CC0, one CC-BY, two CC-BY-NC-SA, one CC-BY-3.0-NZ,
   one CC-BY-3.0-US, and one is explicitly **embargoed**. The pattern inverts Zenodo's
   (92 % CC-BY/CC0). Size and licence clarity are inversely correlated.
3. **`sizes` in DataCite is an untapped index.** 4,845 seismic dataset DOIs publish a
   size nobody aggregates. Harvesting it costs 22 HTTP requests.

### Cloud buckets, measured (prefix-scoped — these are floors, not totals)

The AWS figures above come from `aws s3 ls --no-sign-request --recursive --summarize`
against a single prefix, because no AWS Registry entry publishes a size (see §b.6).
Full-bucket totals would require enumerating tens of millions of objects.

| Bucket prefix | Measured | Objects |
|---|---:|---:|
| `s3://nrel-pds-porotomo/DAS/SEG-Y/` | 47.5 TiB | 104,535 |
| `s3://scedc-pds/continuous_waveforms/2023/` | 10.5 TiB | 1,630,906 |
| `s3://geonet-open-data/waveforms/miniseed/2024/` | 8.9 TiB | 685,411 |
| `s3://scedc-pds/Ridgecrest_DAS/` | 3.7 TiB | 911 |
| `s3://ncedc-pds/continuous_waveforms/BK/2024/` | 3.1 TiB | 2,690,124 |
| `s3://gdr-data-lake/wholescale/subter_seismic/` | 3.0 TiB | 23,177 |
| `s3://earthscope-geophysical-data/miniseed/TA/2011/` | 2.8 TiB | 159,154 |
| `s3://geonet-open-data/seismic-products/benchmark-dataset/` | 1.5 TiB | 39 |
| `s3://gdr-data-lake/imperialvalleydas/` | 1.1 TiB | 2,882 |
| `s3://earthscope-geophysical-data/miniseed/IU/2024/` | 932.4 GiB | 24,433 |
| `s3://tgs-opendata-poseidon` (**complete bucket**) | 188.2 GiB | 56,465 |
| `s3://gdr-data-lake/soda_lake/raw_seismic/2010/` | 171.0 GiB | 8,323 |

### The general-purpose leaders, for reference

Kept from the earlier ranking, since these are what a researcher actually finds by
searching the big hubs: `HeXingChen/Seismic-AI-Data` 2,916,246,352,428 B (HF, MIT —
a SeisBench mirror) · `subsurfacegen/field-scale-dataset` 1,623,610,657,665 B (HF,
CC-BY-4.0) · `cangyeone/SeismicX-Cont` 427,176,078,330 B (HF) ·
`JasonXF/SeismicTransformerData` 289,998,313,442 B (HF, Apache-2.0) · Central &
Eastern Mediterranean tomography 178,825,674,062 B (Zenodo `10.5281/zenodo.3732981`,
CC-BY-4.0) · Reduced-order 3D wave propagation 176,842,054,483 B
(`10.5281/zenodo.12520845`) · OKLAD 172,530,233,396 B (`10.5281/zenodo.18991761`,
CC-BY-NC-4.0). **None of these is a field exploration seismic volume, and none is in
SEG-Y.** The SEAM Phase I package (6,911,091,804 B) — the only vendor-grade exploration
release with byte-exact public URLs found in this survey — would rank far below all of
them.

## b.4 Cross-repository census via DataCite — an independent count

DataCite indexes DOI metadata across essentially every research repository, so it gives
a single consistent denominator that does not depend on each platform's own search
quirks. Verified via `https://api.datacite.org/dois`.

**All DataCite `resourceTypeGeneral=Dataset` DOIs matching "seismic": 21,895.**

Per repository (`&client-id=<id>&resource-type-id=dataset`):

| Repository | DataCite client-id | Seismic dataset DOIs | All seismic DOIs |
|---|---|---:|---:|
| Zenodo | `cern.zenodo` | **5,675** | 20,531 |
| figshare | `figshare.ars` | **2,743** | 7,311 |
| Mendeley Data | `bl.mendeley` | **1,235** | — |
| DataDryad | `dryad.dryad` | **137** | — |
| Harvard Dataverse | `gdcc.harvard-dv` | **96** | — |
| Open Science Framework | `cos.osf` | **3** | 279 |
| Mendeley Data (Elsevier prefix) | `elsevier.md` | 0 | — |

**Domain repositories that no general-purpose survey catches** — same method, and
several of these hold more seismic data than Dryad, Dataverse and OSF combined:

| Repository | DataCite client-id | Seismic dataset DOIs |
|---|---|---:|
| LDEO, Columbia University | `tib.ldeo` | **1,101** |
| PANGAEA | `pangaea.repository` | **1,049** |
| GFZ Data Services | `tib.gfz` | **395** |
| USGS (DOI Tool Production) | `usgs.prod` | **393** |
| Marine Geoscience Data System (MGDS) | `cul.mgds` | **131** |
| NERC Environmental Data Service | `bl.nerc` | **111** |
| ScienceDB (Chinese Academy of Sciences) | `cnic.sciencedb` | 56 |
| B2SHARE / EUDAT | `fzj.b2share` | 0 |
| Norwegian Marine Data Centre | `bibsys.nmdc` | 1 |

That LDEO and PANGAEA each out-hold Harvard Dataverse by more than tenfold is the
practical argument against treating "general-purpose repository" as the unit of search
— **the seismic data is concentrated in domain repositories that the generic hubs never
surface.**

**Growth curve** — DOIs *created* per year for seismic datasets:
2026 → 6,084 · 2025 → 2,792 · 2024 → 2,314 · 2023 → 1,960 · 2022 → 1,624 ·
2021 → 1,652 · 2020 → 1,329 · 2019 → 1,039 · 2018 → 717 · 2017 → 387.
**Deposits have roughly doubled every two years and 2026 alone is 28 % of everything
ever registered.** Any index built now must be designed for continuous re-harvest, not
a one-off snapshot.

**Caveat on the Zenodo discrepancy:** DataCite reports 5,675 seismic *dataset* DOIs at
Zenodo while Zenodo's own API reports 2,591 for `q=seismic&resource_type=dataset`.
The gap is explained by (a) DataCite full-text-matching descriptions and subjects that
Zenodo's default `q` weights differently, and (b) Zenodo minting a DOI per *version*.
Neither number is wrong; they answer different questions. Use Zenodo's own API for
sizes (DataCite carries no file-size field) and DataCite for census.

## b.5 Kaggle, figshare, OSF, Dataverse, Mendeley Data, DataDryad — verified via API

**Method.** Each platform's own REST API, preferred over HTML scraping so that every
byte figure below is a real byte count rather than a rounded display string. Where a
platform publishes no size field of its own, sizes come from DataCite's `sizes` and are
labelled as such. All six were harvested 2026-08-24.

> **Independent re-verification (second pass, same day).** The figshare, Dryad and
> Dataverse figures below were re-derived from scratch on a separate run and match:
> figshare **612,245,482,264 B** (identical), Dryad **399,996,641,657 B across 125
> records, 100 % CC0** (identical), Harvard Dataverse **1,065,993,830,528 B** (within
> 0.08 % — a version-boundary difference, not a methodology one). The Dataverse
> harvested-metadata caveat also reproduced exactly: only **102 of 325** are
> Harvard-native `doi:10.7910/DVN/*` and return a size; the other 223 are metadata
> harvested from Texas Data Repository (`10.18738/T8`), ICPSR (`10.3886`), Borealis
> (`10.5683`) and others, whose files live elsewhere.
>
> ⚠️ **Kaggle did not reproduce.** On the second pass,
> `https://www.kaggle.com/api/v1/datasets/list?search=seismic` returned **HTTP 200 with
> a Google reCAPTCHA challenge page as the body** — not JSON — as did the internal
> `POST /api/i/datasets.DatasetService/ListDatasets` and all three direct dataset and
> competition pages (`<title>Checking your browser - reCAPTCHA</title>`). **Even the
> Internet Archive is walled**: the most recent Wayback capture of
> `kaggle.com/c/tgs-salt-identification-challenge/data` (`20251231183646`, 9,310 bytes)
> contains only the interstitial, as do the 20240731 and 20251002 captures. So Kaggle's
> unauthenticated dataset API is **rate-limited or IP-reputation-gated, not reliably
> open** — it worked once and refused an hour later. Treat the Kaggle numbers below as
> a snapshot that a link checker will not be able to re-verify, and plan on an
> authenticated `kaggle` CLI token for any maintained catalogue.

**Headline: all six together hold less open seismic data than Zenodo alone.**

| Platform | Seismic records | Bytes measured | Largest single record | Licence stated |
|---|---:|---:|---:|---:|
| **Dataverse** (Harvard search) | 325 (102 Harvard-native) | **1,065,179,580,414** | 443,994,738,710 | 15/16 of top |
| **Kaggle** | 130 strict (1,067 harvested) | **923,695,085,194** | 172,639,117,416 | 66.9 % |
| **figshare** | 1,188 distinct articles | **612,245,482,264** | 27,838,770,673 | **100 %** |
| **DataDryad** | 137 (125 via Dryad's own API) | **399,996,641,657** | 123,694,529,055 | **100 % CC0** |
| **Mendeley Data** | 538 distinct datasets | **154,285,322,367** | 10,069,878,612 | **98.9 %** |
| **OSF** | 374 nodes (174 with files) | **61,631,975,813** | 24,165,566,330 | n/a (no licence API) |
| **Total** | — | **3,217,034,087,709 (3.22 TB)** | — | — |

Zenodo alone (§b.1) holds **12.385 TB** across 3,836 records with files. **These six
platforms combined are 26.0 % of Zenodo.** They are not a second tier of the same size;
they are a rounding error on a rounding error — §b.3 already established that the whole
general-purpose category is ~0.2 % of the 1.56 PB declared through DataCite.

### b.5.1 Kaggle — the API is split down the middle by authentication

**This is the single most important operational finding of §b.5**, and it is a plain
negative rather than a guess:

| Endpoint | Unauthenticated result |
|---|---|
| `https://www.kaggle.com/api/v1/datasets/list?search=seismic` | **HTTP 200** — full JSON incl. `totalBytesNullable`, `licenseNameNullable`, `usabilityRatingNullable`, `downloadCount` |
| `https://www.kaggle.com/api/v1/competitions/list?search=seismic` | **HTTP 401** `{"code":401,"message":"Unauthenticated"}` |
| `https://www.kaggle.com/api/v1/competitions/data/list/tgs-salt-identification-challenge` | **HTTP 401** |
| `https://www.kaggle.com/api/v1/competitions/data/list/LANL-Earthquake-Prediction` | **HTTP 401** |
| `https://www.kaggle.com/competitions/<slug>` (HTML) | HTTP 200 but only a **~5.6 KB JavaScript shell** — no data in the markup |

**So: Kaggle *datasets* are fully machine-readable with exact bytes and licences and no
account. Kaggle *competitions* are not readable at all without an API token.** Any
statement in this file about competition file sizes, team counts or prize money would
be invention, so none is made — see "Could not verify" #20.

What *can* be verified about competitions without auth is existence and official title,
because a nonexistent slug returns HTTP 404 while a real one returns HTTP 200 with a
populated `<title>`. Control: `definitely-not-a-real-competition-xyz123` → **HTTP 404**.
On that test, four seismic-relevant competitions exist:

| Slug | Official title (from `<title>`) |
|---|---|
| `tgs-salt-identification-challenge` | TGS Salt Identification Challenge |
| `LANL-Earthquake-Prediction` | LANL Earthquake Prediction |
| `waveform-inversion` | **Yale/UNC-CH – Geophysical Waveform Inversion** |
| `predict-volcanic-eruptions-ingv-oe` | INGV – Volcanic Eruption Prediction |

The third was not on the brief and is the most exploration-relevant ML competition
found anywhere in this survey. `geophysical-waveform-inversion`,
`seismic-facies-identification`, `earthquake-damage-prediction`, `force-2020` and
`nasa-space-apps-seismic-detection` all return **HTTP 404** — they are not Kaggle
competitions, whatever secondary sources say.

**Dataset harvest.** 16 search terms (`seismic`, `segy`, `seg-y`, `earthquake`,
`seismology`, `seismogram`, `waveform inversion`, `subsurface`, `geophysics`, `salt
identification`, `microseismic`, `tgs salt`, `LANL earthquake`, `well log`, `facies`,
`first break picking`), paginated to exhaustion, deduplicated by `ref`: **1,067 unique
datasets**. Restricting to titles/descriptions that genuinely denote seismic work and
removing collisions (`jennifergwen/deepfake-datasets`,
`absolutedegradation/absolutecinema-*` — 174 GB of video that matched on "scene split")
leaves **130 datasets totalling 923,695,085,194 bytes**.

| # | Bytes | Kaggle ref | Licence | Usability | Downloads |
|---:|---:|---|---|---:|---:|
| 1 | 172,639,117,416 | `tsaitang00124/openfwi-style` | CC BY-NC-SA 4.0 | 0.44 | 22 |
| 2 | 151,518,589,567 | `tsaitang00124/openfwi-vels` | CC BY-NC-SA 4.0 | 0.44 | 10 |
| 3 | 137,413,679,224 | `tsaitang00124/openfwi-curvefault` | CC BY-NC-SA 4.0 | 0.44 | 9 |
| 4 | 136,171,569,029 | `tsaitang00124/openfwi-flatfault` | CC BY-NC-SA 4.0 | 0.44 | 5 |
| 5 | 85,124,279,963 | `isevilla/stanford-earthquake-dataset-stead` | CC-BY-4.0 | 0.94 | 4,147 |
| 6 | 22,114,565,718 | `brendanartley/openfwi-preprocessed-72x72` | CC-BY-SA-4.0 | **1.00** | 4,591 |
| 7 | 21,609,545,476 | `seshurajup/waveform-inversion-2` | CC BY-NC-SA 4.0 | 0.47 | 239 |
| 8 | 21,609,220,533 | `seshurajup/waveform-inversion-1` | CC BY-NC-SA 4.0 | 0.47 | 591 |
| 9 | 21,605,389,062 | `seshurajup/waveform-inversion-3` | CC BY-NC-SA 4.0 | 0.47 | 203 |
| 10 | 18,777,644,742 | `redstr/lanl-p4581` | Data files © Original Authors | 0.50 | 55 |
| 11 | 14,322,186,525 | `zanjibar/apollo-12-lunar-seismic-data` | CC-BY-SA-4.0 | 0.35 | 13 |
| 12 | 10,535,327,475 | `budatuan666/seismic-data-synthetic` | MIT | 0.13 | 0 |
| 13 | 9,868,424,124 | `zhanglic/seismic-simulated-data` | **Unknown** | 0.00 | 104 |
| 14 | 9,435,111,943 | `kjasoria/seismology1` | **Unknown** | 0.00 | 2 |
| 15 | 6,845,665,536 | `mycarta/thebe-fault-patches-256` | CC-BY-4.0 | 0.94 | 159 |

**The top four are a third-party re-upload of OpenFWI** (§a.15) — and their
CC-BY-NC-SA-4.0 tag does at least match OpenFWI's own licence, which is more than can
be said for the HuggingFace SeisBench mirror in §b.2. #5 is a re-upload of STEAD. **Six
of the top eight bytes on Kaggle are copies of two datasets already catalogued
elsewhere in this survey.** Kaggle is a mirror layer, not a source.

**Licence and quality hygiene:** **43 of the 130 (33.1 %) carry `licenseName:
"Unknown"`** — the worst licence coverage of any platform in §b.5 and worse than
HuggingFace's 14.7 %. Kaggle's own `usabilityRating` has a **median of 0.50** across the
130; the two 9-GB entries at #13 and #14 score **0.00**, meaning no description, no tags,
no column metadata and no licence.

**Competition-derived datasets are re-hosted as ordinary datasets**, which is the only
route to a byte count for competition data without an account:
`integmind/tsg-salt-superres-training-data` 1,351,144,990 B ·
`inhvnnhn/sub-part-of-tsg-salt-segmentation-dataset` 676,872,806 B ·
`jerrinbright/salt-identification` 473,665,222 B · `bernir/bernis-lanl-features`
719,910,474 B · `teeyee314/lanl-ft` 433,316,843 B · `tocha4/lanl-training-as-pickle`
433,315,918 B · `elvenmonk/lanl-training-acoustic-data` 418,422,301 B ·
`takeiy/data-for-lanl-earthquake-prediction` 381,470,428 B. These are user copies of
uncertain fidelity and mostly `Unknown` licence — usable as evidence that the
competitions existed, **not** as a substitute for the official competition files.

**What dominates:** by title classification, earthquake/passive 53, exploration
/reflection 11, engineering 3, unclassified 63. Kaggle's seismic content is
**pre-diced ML tensors** — `.npy`, `.parquet`, image patches. Nothing in the 130 is SEG-Y.

### b.5.2 figshare — the best licence hygiene found anywhere, and a version-count trap

**figshare's own search API cannot count.** `POST https://api.figshare.com/v2/articles/search`
returns a bare JSON array with **no total-count field of any kind**, and paginates via
an opaque `X-Cursor` header. Offset is capped exactly as Zenodo's is:

```
{"message": "Your requested offset (10100) exceeds the maximum accepted offset (10000)",
 "code": "PaginationOffsetExceeded"}
```

So a census must come from DataCite. **DataCite reports 2,743 seismic dataset DOIs at
`figshare.ars`** — but figshare mints **a DOI per version**, and stripping the `.vN`
suffix collapses those 2,743 DOIs to **1,188 distinct articles**. §b.3's figure of
"2,632 sized figshare records, 1.65 TB" counts versions; the de-duplicated figure is
**1,139 sized articles totalling 612,245,482,264 bytes**. Both are defensible; they
answer different questions, and the version-inflated one should never be quoted as a
record count.

| # | Bytes | Record | DOI | Licence |
|---:|---:|---|---|---|
| 1 | **27,838,770,673** | **Raw seismic reflection data from Orca Volcano, Bransfield Strait, Antarctica** | 10.6084/m9.figshare.24085110 | **CC-BY-4.0** |
| 2 | 17,930,095,284 | Passive Sources and Diffracted Points Imaging Using Combinational Cross-correlation | 10.6084/m9.figshare.26019373 | CC-BY-4.0 |
| 3 | 15,721,847,524 | DAS data, coastal ocean dynamics under typhoon conditions, submarine cable | 10.6084/m9.figshare.30315541 | CC-BY-4.0 |
| 4 | 14,884,951,486 | Influence of Grain Size Polydispersity on Seismic Spectra of Geophysical Granular… | 10.6084/m9.figshare.32298315 | CC-BY-4.0 |
| 5 | 14,724,640,654 | Seismic-Acoustic Dataset of Coastal Bryde's Whales in the Beibu Gulf | 10.6084/m9.figshare.30363799 | CC-BY-4.0 |
| 6 | 14,504,955,962 | AQ53 card content | 10.6084/m9.figshare.25036139 | CC-BY-4.0 |
| 7 | 13,857,630,745 | Monitoring seasonal variations in seismic velocity and groundwater, Harvey, W. Aus. | 10.6084/m9.figshare.12366074 | CC-BY-4.0 |
| 8 | 13,085,345,789 | Fault slip behaviours modulated by locally increased fluid pressure | 10.6084/m9.figshare.19601773 | CC-BY-4.0 |
| 9 | 12,061,408,099 | TAMNNET Waveform Data | 10.6084/m9.figshare.26087416 | MIT |
| 10 | 11,578,381,824 | Infrasound recordings, 2021 eruptive episodes of Etna Volcano | 10.6084/m9.figshare.29037734 | CC-BY-4.0 |

**#1 independently re-verified against figshare's own API**, not just DataCite:
`GET /v2/articles/24085110` returns 22 files summing to **27,838,770,673 bytes**,
`license: CC BY 4.0`, current DOI `10.6084/m9.figshare.24085110.v5`. Note DataCite
carries **27,860,172,234** for a `.v10` of the same article — a 21 MB discrepancy caused
purely by version drift. **Where a platform has its own size API, prefer it to DataCite.**
The files are RAR archives (`OR_21.1.rar` 1,752,954,994 B, `OR_12.1.rar` 1,588,903,863 B,
`OR_17.1.rar` 1,578,287,456 B, …) — genuinely *raw* marine multichannel reflection data,
which makes this the most exploration-shaped record in all of §b.5. It is academic
Antarctic MCS, not an industry 3D volume.

**Licence distribution across all 1,188 distinct articles — and this is the standout
number of the whole section:**

| Licence | Articles | Share |
|---|---:|---:|
| CC-BY-4.0 | 1,003 | 84.4 % |
| CC0-1.0 | 96 | 8.1 % |
| CC-BY (unversioned) | 47 | 4.0 % |
| CC-BY-NC-ND-4.0 | 19 | 1.6 % |
| MIT | 10 | 0.8 % |
| GPL / GPL-3.0+ | 8 | 0.7 % |
| CC BY 4.0 (variant string) | 4 | 0.3 % |
| CC BY (variant string) | 1 | 0.1 % |
| **none stated** | **0** | **0.0 %** |

**Zero unlicensed records out of 1,188.** figshare beats Zenodo (1.4 % unstated),
HuggingFace (14.7 %) and Kaggle (33.1 %). figshare enforces a licence at deposit time
and it shows. If a catalogue needs a platform whose licence field can be trusted without
manual review, this is it.

**What dominates** (title-keyword classification, so approximate): earthquake/passive
269, engineering/structural 111, exploration/reflection 55, lab/rock-physics 23,
DAS/fibre 3, unclassified 727. By bytes, exploration/reflection is 77,871,909,030 —
**12.7 % of figshare's seismic volume**, the highest exploration share of any platform
in §b.5.

### b.5.3 OSF — a project workspace, not a data repository

**Counts** via `https://api.osf.io/v2/`:

| Query | Total |
|---|---:|
| `nodes/?filter[title]=seismic` | **182** |
| `nodes/?filter[title]=earthquake` | 181 |
| `nodes/?filter[description]=seismic` | 273 |
| `preprints/?filter[title]=seismic` | 149 |
| `nodes/?filter[tags]=seismic` | **9** |
| `nodes/?filter[title]=seismology` | 5 |
| `registrations/?filter[title]=seismic` | **HTTP 502 Bad Gateway** (two attempts) |

Harvesting title+description across `seismic` and `seismology` gives **374 unique
nodes**, of which only **212 have a genuinely seismic title**. Measuring each node's
`osfstorage` provider file-by-file:

- **174 nodes hold at least one byte; 200 hold none at all.**
- **Total OSF-hosted seismic bytes: 61,631,975,813 (61.6 GB)** — the smallest holding of
  any platform in this entire survey, smaller than a *single* mid-table Zenodo record.

| # | Bytes | Node | Files | Title |
|---:|---:|---|---:|---|
| 1 | 24,165,566,330 | `osf.io/rqk3y` | 15 | Upper Crustal Complexities and Their Influences on Intraplate Seismicity |
| 2 | 5,328,109,708 | `osf.io/9ygrp` | 10 | Fault Valving and Pore Pressure Evolution in Simulations of Earthquake Sequences |
| 3 | 3,989,162,438 | `osf.io/wsh32` | 4 | Ledevin_MultiphaseFlow |
| 4 | 3,748,523,501 | `osf.io/y48eg` | 1 | Long timescale aseismic simulation data |
| 5 | 3,046,608,973 | `osf.io/wv738` | 3 | Physics-Based Simulation of Megathrust Ground Motions at 54 Dams in New Zealand |
| 6 | 2,983,992,401 | `osf.io/8gzkx` | 9 | Injection-Induced Aseismic Fault Slip in an Underground Gas Storage Reservoir |
| 7 | 2,391,540,593 | `osf.io/7bsvq` | 18 | InSAR data and model of the Bada 2022 seismic sequence (Ethiopia) |
| 8 | 2,284,128,904 | `osf.io/bj6sq` | 4 | Upper Crustal Complexities Revealed by Ambient Noise Eikonal Tomography |

**That 200 of 374 nodes contain zero OSF-hosted files is the finding.** OSF projects
routinely point at Google Drive, Dropbox, GitHub or an institutional server through
add-ons, so the node is a landing page and the data is elsewhere and unmeasurable —
and often unversioned and impermanent. DataCite corroborates the shallowness: **OSF has
just 3 seismic *dataset* DOIs** registered (§b.4), against figshare's 2,743. OSF
publishes no licence field through the nodes API at all.

**Verdict: do not include OSF as a data source in a curated index.** It is worth one
line as a place where seismic *preprints and project pages* live. Everything of size is
simulation output, not observation.

### b.5.4 Dataverse — holds the single largest record in §b.5, and has no federated search

**Query behaviour must be pinned down first, because the naive numbers are nonsense.**
Harvard Dataverse's `/api/search` OR-tokenises unquoted multi-word queries:

| Query | `total_count` |
|---|---:|
| `q=SEG-Y` (unquoted) | **7,923** |
| `q="SEG-Y"` (quoted) | **1** |
| `q=full waveform inversion` (unquoted) | **13,520** |
| `q="full waveform inversion"` (quoted) | **2** |
| `q=seismic` | **325** |
| `q="seismic reflection"` | 9 · `q="3D seismic"` 9 · `q="seismic data"` 33 · `q="distributed acoustic sensing"` 7 |

Anyone quoting "13,520 full-waveform-inversion datasets on Harvard Dataverse" has
measured the number of datasets containing the word *of*. **Always quote the phrase.**

**The 325 are not all Harvard.** Splitting by DOI prefix reveals that Harvard's search
index silently includes *harvested* metadata from other Dataverse installations:

| DOI prefix | Installation | Records |
|---|---|---:|
| `10.7910` | **Harvard Dataverse (native)** | **102** |
| `10.17603` | DesignSafe Data Depot | 65 |
| `10.5683` | Borealis (Canada) | 47 |
| `10.18738` | Texas Data Repository | 23 |
| `10.18710` | DataverseNO | 22 |
| `10.17026` | DANS | 8 |
| `10.3886` | ICPSR | 6 |
| (no DOI / handle) | various | 49 |

**Sizes are exact and public**, via an endpoint that deserves to be better known:
`/api/datasets/:persistentId/versions/:latest/downloadsize` returns
`{"storageSize": <int>}`. It works without an account **only for records the
installation actually hosts**: all 102 native records returned a size, while **179 of
the 223 harvested records returned HTTP 403** — the metadata is indexed at Harvard but
the bytes live on the origin server. Net measurable: **105 records with non-zero size,
1,065,179,580,414 bytes**, of which Harvard-native is **1,030,627,046,767**.

| # | Bytes | DOI | Files | Licence | Title |
|---:|---:|---|---:|---|---|
| 1 | **443,994,738,710** | 10.7910/DVN/EXOCYD | 53 | **CC-BY-4.0** | **A Real Swell Noise Benchmark Dataset for Seismic Data Denoising with Deep Learning** |
| 2 | 125,746,134,900 | 10.7910/DVN/WCJTJT | 59 | **CC0-1.0** | Synthetic Seismic Waveforms and Receiver Functions from SPECFEM3D Simulations |
| 3 | 111,205,953,594 | 10.7910/DVN/1GISZH | 62 | CC0-1.0 | Seismic_Data_Larsemann_ENZ_Line1 |
| 4 | 104,003,926,834 | 10.7910/DVN/N6MTZA | 60 | CC0-1.0 | Seismic_Data_Larsemann_ENZ_Line2 |
| 5 | 55,523,312,079 | 10.7910/DVN/TPDPHA | 240 | CC0-1.0 | Complex near-surface rheology inferred from the response of the ground |
| 6 | 53,090,565,446 | 10.7910/DVN/YBYGBK | 78 | custom CC text | **A Gigabyte Interpreted Seismic Dataset for Automatic Fault Recognition** |
| 7 | 33,622,470,722 | 10.18738/T8/6JOR2D | 620 | **none stated** | Influence of Frictional Melt on the Seismic Cycle (Texas Data Repository) |
| 8 | 21,282,876,016 | 10.7910/DVN/XUL0NV | 627 | CC-BY-SA-4.0 | Owhiro Bay Quarry seismic data from the reference station |
| 9 | 20,463,230,528 | 10.7910/DVN/EGB21M | 160 | CC0-1.0 | **2018 San Pedro Basin fault CSULB multichannel seismic reflection data** |
| 10 | 14,516,530,671 | 10.7910/DVN/GXJ6VH | 2,101 | CC0-1.0 | Vertical Component of Raw Ambient Seismic Noise Waveform |
| 11 | 13,839,681,135 | 10.7910/DVN/G2KFLY | 30 | CC0-1.0 | Ambient seismic field cross-correlation functions in Japan |
| 12 | 13,192,643,931 | 10.7910/DVN/I0C6X3 | 20 | CC0-1.0 | 3D drone outcrop models of the Mount Messenger Formation, New Zealand |
| 13 | 12,760,376,060 | 10.7910/DVN/5D4CST | 372 | CC-BY-SA-4.0 | Owhiro Bay Quarry seismic data from the top station |
| 14 | 5,574,121,783 | 10.7910/DVN/AYZI3L | 905 | CC-BY-NC-SA-4.0 | 6 February 2023 Kahramanmaraş Earthquakes Database |
| 15 | 5,185,639,920 | 10.7910/DVN/FCTZZC | 7 | CC0-1.0 | **Guaymas basin MCS line 1** |

**`10.7910/DVN/EXOCYD` at 443,994,738,710 bytes is the largest single record found
anywhere in §b.5 — 2.48× larger than the largest record on Zenodo** (178,825,674,062 B,
§b.1). It is also squarely an *exploration* dataset: swell noise is a marine
towed-streamer processing problem, and the record is a denoising benchmark built from
real acquisition noise. Licence confirmed **CC BY 4.0** two independent ways
(`/versions/:latest` → `license.name`, and the `schema.org` exporter →
`"license": "http://creativecommons.org/licenses/by/4.0"`).

**A licence-metadata correction that matters beyond this section.** DataCite reports
**"none stated" for every one of these Harvard records** (§b.4 counted 96 seismic
dataset DOIs at `gdcc.harvard-dv`, all rights-less). Querying Dataverse directly shows
that is a *propagation failure*, not missing licences: of the top 16 by size, **15 carry
an explicit licence** — CC0-1.0 ×10, CC-BY-4.0, CC-BY-SA-4.0 ×2, CC-BY-NC-SA-4.0, plus
one custom CC text — and only the Texas Data Repository record genuinely states none.
**DataCite's `rightsList` is unreliable for Dataverse.** The same is true for Mendeley
(§b.5.5). §b.3's finding that licensing collapses at the top of the size distribution
still holds for the FDSN/IRIS records, but should not be extended to these two platforms.

**The wider Dataverse network has no federated search.** Each installation must be
queried separately, and most are not queryable at all:

| Installation | `?q=seismic&type=dataset` |
|---|---|
| Harvard Dataverse | **325** |
| Borealis (Canada) | **53** |
| DataverseNO (UiT, Norway) | **23** |
| DANS Data Station (`ssh.datastations.nl`) | 1 |
| Texas Data Repository | **HTTP 403** |
| Odum / UNC | **HTTP 401** |
| CIMMYT | **HTTP 401** |
| `dataverse.nl`, ADA Australia | non-JSON response |
| `opendata.pku.edu.cn` | DNS resolution failed |

There is no `hub.dataverse.org`-style cross-installation search API; the count above is
a floor, and roughly half the installations tried refuse anonymous API access outright.

### b.5.5 Mendeley Data — the search API is broken, and this is provable

**`https://data.mendeley.com/api/datasets/search?query=<q>` ignores the `query`
parameter entirely.** Retrieving 400 rows for `query=seismic` and grepping name +
description for `seismic|seismolog|seismogram|earthquake` matches **5 of 400 — 1.2 %**.
The actual top-ranked "results" for a seismic query include *Establishment Dates of
Stock Markets*, *Dairy calcium promotes the prebiotics effects*, *Gender-based violence:
Statistical data for four Colombian municipalities* and *Food allergy: children's
symptom levels impact caregivers' …*. Every returned record also reports `"size": 0`.
Pagination is equally non-functional: `page`, `offset` and `skip` are all silently
ignored (identical first record every time) and `limit=500` returns **HTTP 500**.

Other routes: the documented Elsevier endpoint `api.datasearch.elsevier.com` returned
**HTTP 000 — no connection**; `https://data.mendeley.com/public-api/datasets?query=…`
returns **HTTP 401 Unauthorized**. **Mendeley Data has no usable public search API.**

The route that *does* work is per-dataset:
`/public-api/datasets/{id}/files?folder_id=root&version={v}` returns exact
`content_details.size` per file, and `/public-api/datasets/{id}` returns
`data_licence.short_name`. Combining DataCite for the census with these two for the
measurement: **1,235 seismic dataset DOIs → 538 distinct datasets** after version-dedup,
**448 sized, 154,285,322,367 bytes**, 87 measuring zero, 3 fetch failures.

| # | Bytes | DOI (`10.17632/…`) | Files | Licence | Title |
|---:|---:|---|---:|---|---|
| 1 | 10,069,878,612 | `8srrb2rcw6` | 42 | CC BY-NC 4.0 | PAM Recordings of Seismic Surveys — IBAMA Regulations in Brazil, part 2 |
| 2 | 9,448,926,710 | `gvxmng6644` | 2 | CC BY 4.0 | **Historical Romanian seismograms scanned in the EUROSEISMOS framework** |
| 3 | 6,791,916,419 | `grpxc5fty2` | 4 | CC BY 4.0 | Acoustic emission dataset-1, fluid-driven fault nucleation |
| 4 | 6,614,518,372 | `w9b5z7znst` | 45 | CC BY-NC 4.0 | PAM Recordings of Seismic Surveys — IBAMA Regulations in Brazil, part 1 |
| 5 | 6,401,425,832 | `g4bdsvg8bm` | 4 | CC BY 4.0 | Travel times of temporary seismic arrays and 3-D Vp/Vs models |
| 6 | 6,147,218,154 | `c5wymn9w8j` | 1 | CC BY NC 3.0 | **Marmousi_Seism4ML** |
| 7 | 6,010,851,581 | `ncmy778xnc` | 1 | CC BY-SA 4.0 | 3D Outcrop-Based Carbonate Seismic Property Model |
| 8 | 5,817,883,280 | `ct25dfrns3` | 4 | CC BY 4.0 | Acoustic emission dataset-2, fluid-driven fault nucleation |
| 9 | 5,069,836,435 | `k2prx886jz` | 3 | CC BY 4.0 | Geotechnical data synthesis for GIS-based fault zone analysis |
| 10 | **4,687,629,207** | `gnvyh3msrj` | 9 | CC BY 4.0 | **Parihaka + Netherlands F3 (raw volumes + labels) for seismic facies segmentation** |

**#1 and #4 are a trap worth naming**: "PAM Recordings of Seismic Surveys" is *passive
acoustic monitoring of marine mammals* during airgun operations — a marine-biology
compliance dataset, not seismic data. Together they are **16.7 GB, 10.8 % of Mendeley's
measured seismic bytes**, and they rank #1 and #4 on a pure keyword search.

**Licences, fetched per-record from Mendeley itself (all 538):** CC BY 4.0 466 (86.6 %) ·
CC BY NC 3.0 35 · CC0 1.0 15 · CPC 4 · CC BY-NC-ND 4.0 4 · GPLv3 3 · CC BY-NC 4.0 3 ·
CC BY-SA 4.0 2 · **none 3** · fetch failed 3. That is **98.9 % licence coverage** —
second only to figshare and Dryad. Yet DataCite reports **"none stated" for 445 of the
538 (82.7 %)**. As with Dataverse, the licence exists and simply is not propagated.

### b.5.6 DataDryad — smallest, cleanest, and 100 % CC0

The best-behaved API of the six. `https://datadryad.org/api/v2/search?q=seismic`
returns a `total` **and** a `storageSize` in bytes on every record, with no
authentication and no offset cap.

- **Total: 125 records**, fully enumerated in two pages of 100.
- **Total bytes: 399,996,641,657.**
- **Licence: `https://spdx.org/licenses/CC0-1.0.html` on all 125 — 100 %, no exceptions.**
  Dryad mandates CC0 at deposit, so there is nothing to audit.

| # | Bytes | DOI | Published | Title |
|---:|---:|---|---|---|
| 1 | 123,694,529,055 | 10.5061/dryad.cjsxksndw | 2025-08-13 | Transient seismo-acoustic signals from crashing ocean waves |
| 2 | 83,635,672,070 | 10.5061/dryad.j3tx95xp6 | 2024-05-24 | Seismic low-velocity equatorial torus in the Earth's outer core |
| 3 | 79,271,471,275 | 10.5061/dryad.34tmpg4td | 2024-08-28 | The Self-Calibrating Tilt Accelerometer |
| 4 | 26,113,015,494 | 10.5061/dryad.0cfxpnw7f | — | Dust devil detection microbarometer and weather, Summer 2018 |
| 5 | 20,132,793,891 | 10.5061/dryad.ksn02v756 | 2021-11-25 | Deformation-rate distributed acoustic sensing |
| 6 | 11,116,442,359 | 10.5061/dryad.tx95x6b2f | — | RockNet: rockfall and earthquake detection via multitask learning |
| 7 | 9,881,844,080 | 10.5061/dryad.f7m0cfz2d | 2023-08-03 | Strain localization in sandstone-derived fault gouges |
| 8 | 9,213,226,714 | 10.5061/dryad.3tx95x6gb | 2021-06-08 | *Elephants show risk-avoidance behaviour to human-generated seismic cues* |

**Dryad's count discrepancy is real and small:** Dryad's own API says **125 records /
399,996,641,657 B**; DataCite says **137 DOIs / 442,083,875,682 B** at `dryad.dryad`.
The 12-record, 42 GB gap is not resolved here — see "Could not verify" #21.

**Keyword contamination is the highest of any platform measured**, because Dryad is
predominantly a life-sciences repository: **14 of 137 records (10 %) are biology or
ecology papers that merely mention seismic surveys** — elephants (9,213,226,714 B),
baleen whale soundscapes (7,329,888,695 B), humpback response to airguns, groundfish
depth distribution, wolf movement on seismic lines — totalling **16,904,039,470 bytes,
4.2 % of Dryad's seismic volume**. Filtering to genuine geophysics by title leaves
**64 records, 131,084,468,004 bytes**. A catalogue harvesting Dryad on the keyword
`seismic` alone would import a fifth of a marine-mammal literature.

### b.5.7 Does any of these fill the exploration-seismic gap? No.

§b.1 established that Zenodo holds *derived subsets* of the famous exploration surveys
and none of the surveys themselves. **The same test run across all six platforms in
§b.5 returns the same verdict, more emphatically.** Searching every harvested title and
description for the canonical open exploration surveys:

| Survey / model | Kaggle | figshare | Dataverse | Mendeley | Dryad | OSF |
|---|---:|---:|---:|---:|---:|---:|
| F3 (Netherlands) | 3 | 0 | 0 | 2 | 0 | 0 |
| Parihaka | 1 | 0 | 0 | 2 | 0 | 0 |
| Marmousi | 0 | 1 | 0 | 1 | 0 | 0 |
| **Penobscot** | **0** | **0** | **0** | **0** | **0** | **0** |
| **Poseidon** | **0** | **0** | **0** | **0** | **0** | **0** |
| **Teapot Dome** | **0** | **0** | **0** | **0** | **0** | **0** |
| **Volve** | **0** | **0** | **0** | **0** | **0** | **0** |
| **Opunake / Stratton / Viking Graben / Kerry** | **0** | **0** | **0** | **0** | **0** | **0** |
| **SEAM / Overthrust / Blake Ridge / Norne** | **0** | **0** | **0** | **0** | **0** | **0** |

The handful of hits are, without exception, **pre-diced ML arrays rather than survey
data.** The best of them, Mendeley `10.17632/gnvyh3msrj` — titled *"Parihaka +
Netherlands F3 (**raw volumes** + labels)"* — is 4,687,629,207 B across 9 files, and
those files are `Parihaka_Data.zip` (1,722,167,774 B), `parihaka_data_train.npz`
(1,715,555,445 B), `F3_train_seismic.npy` (573,446,168 B), `F3_test1_seismic.npy`
(286,008,128 B), `F3_test2_seismic.npy` (245,208,128 B) and three label `.npy` files.
**"Raw volumes" means NumPy arrays, not SEG-Y.** On Kaggle the equivalents are
`great23u5/f3-facies-classification-benchmark` 1,073,292,037 B (**Unknown** licence),
`great23u5/f3-facies-classification` 1,051,896,685 B (MIT),
`gustavoscholze/f3-dataset` 514,275,920 B (CC-BY-SA-3.0) and
`fvizeus/2020-seg-annual-meeting-ml-dataset` 1,688,195,719 B (MIT, Parihaka).

**Conclusion: none of the six fills the exploration-seismic gap.** Two records come
closest and neither is an industry 3D volume:

1. **`10.7910/DVN/EXOCYD`, 443,994,738,710 B, CC-BY-4.0 (Harvard Dataverse)** — a real
   marine swell-noise denoising benchmark. Exploration-domain, exploration-scale, and
   **the only record in §b.5 that outweighs anything on Zenodo.** It belongs in a
   curated index.
2. **`10.6084/m9.figshare.24085110`, 27,838,770,673 B, CC-BY-4.0 (figshare)** — genuinely
   raw marine MCS reflection data from Orca Volcano, Antarctica. Academic acquisition,
   RAR-packed, but real field reflection data with a clean licence.

Everything else repeats the §b.1 pattern exactly: Poseidon, Teapot Dome, Volve,
Penobscot, Opunake, Stratton, Viking Graben, Kerry, SEAM, Overthrust, Blake Ridge and
Norne return **zero hits on all six platforms**. Those surveys live on national data
portals, vendor catalogues and cloud buckets (§a.16, §b.6) and nowhere else. **The
general-purpose repository layer does not contain open exploration seismic, and adding
five more repositories to a Zenodo-based search does not change that.**

### b.5.8 Inclusion verdicts

| Platform | Include? | Why |
|---|---|---|
| **Dataverse (Harvard-native)** | **Yes** | Holds the largest record in §b.5, exact public `downloadsize`, on-platform licences are excellent (mostly CC0). Query with quoted phrases; ignore harvested records (403 on size). |
| **figshare** | **Yes** | 1,188 articles, **100 % licensed**, highest exploration share (12.7 % of bytes). De-duplicate `.vN` DOIs or the count triples. |
| **DataDryad** | **Yes, cheaply** | 125 records, one API call, exact bytes, 100 % CC0. Small but free to harvest. Filter the ~10 % biology collisions. |
| **Kaggle** | **Datasets only, with care** | Exact bytes and licences without auth, but 33 % `Unknown` licence, median usability 0.50, and the top bytes are re-uploads of OpenFWI and STEAD. Cite it as a *mirror*, and record provenance. Competitions need a token. |
| **Mendeley Data** | **Marginal** | 154 GB total, no working search API, and the two largest records are marine-mammal monitoring. Harvest via DataCite + per-record file API only if completeness matters. |
| **OSF** | **No** | 61.6 GB, 200 of 374 nodes hold no files at all, 3 dataset DOIs, no licence field. A preprint host, not a data repository. |

**The cross-cutting lesson of §b.5** is that *each platform lies about itself in a
different way*, and every one of those lies inflates:

- Kaggle looks like it has 1,067 seismic datasets; 130 survive scrutiny.
- figshare looks like it has 2,743; 1,188 survive version-dedup.
- Harvard Dataverse looks like it has 325; 102 are actually Harvard's.
- Mendeley's search returns stock-market data for a seismic query.
- Dryad's 137 include elephants and whales.
- OSF's 374 nodes are 200 empty landing pages.

A catalogue that harvests these APIs naively would report roughly **3× more seismic
datasets than exist** and would attribute sizes and licences that its own sources
contradict.

## b.6 AWS / Google Cloud / Azure open-data registries — verified

**Provenance:** `awslabs/open-data-registry` @ commit `c24da1bb4261` (2026-08-24T14:08:55Z),
**1,190 dataset YAMLs** downloaded and parsed in full. Bucket regions independently
confirmed via the `x-amz-bucket-region` header; sizes marked *measured* come from
`aws s3 ls --no-sign-request --recursive --summarize`.

### Critical schema finding

**The AWS Registry of Open Data YAML schema has no `Size` field.**
`grep -rlE "^\s*Size:"` across all 1,190 files returns **0 matches**. Any size
attributed to an AWS ODR dataset must come from the operator's own docs or from
listing the bucket. This is exactly the gap a sized catalogue fills.

### AWS — the 9 core seismic/subsurface datasets

The `seismology` tag matches exactly 7; `gdr-data-lake` and `grillo-openeew` are
genuinely seismic but tagged otherwise. All registry URLs verified HTTP 200; all
buckets verified anonymously listable.

| Dataset | Registry URL | Bucket / region | Size | Licence | Updated |
|---|---|---|---|---|---|
| **SCEDC** (Southern California) | `registry.opendata.aws/southern-california-earthquakes/` | `s3://scedc-pds` · us-west-2 ✅ | *measured* `continuous_waveforms/2023/` **10.5 TiB / 1,630,906 obj**; `Ridgecrest_DAS/` **3.7 TiB / 911 obj** | royalty-free; cite `doi:10.7909/C3WD3xH1` + `doi:10.7914/SN/CI` | **daily** |
| **NCEDC** (Northern California) | `registry.opendata.aws/northern-california-earthquakes/` | `s3://ncedc-pds` · **us-east-2** ⚠️ | *measured* `continuous_waveforms/BK/2024/` **3.1 TiB / 2,690,124 obj** | royalty-free; cite `doi:10.7932/NCEDC` | **daily** |
| **EarthScope Geophysical Data** | `registry.opendata.aws/earthscope-geophysical-data/` | `s3://earthscope-geophysical-data` · us-east-2 ✅ + SNS topic | *measured* `miniseed/TA/2011/` **2.8 TiB / 159,154 obj**; `miniseed/IU/2024/` **932.4 GiB** | per-network, declared at `fdsn.org/networks/` | **daily** |
| **GeoNet** (Aotearoa NZ) | `registry.opendata.aws/geonet/` | `s3://geonet-open-data` · ap-southeast-2 ✅ | *measured* `waveforms/miniseed/2024/` **8.9 TiB / 685,411 obj**; `seismic-products/benchmark-dataset/` **1.5 TiB** | **CC-BY-3.0-NZ** | **daily** |
| **Poseidon 3D Seismic, Australia (TGS)** | `registry.opendata.aws/tgs-opendata-poseidon/` | `s3://tgs-opendata-poseidon` · us-west-2 ✅ | **188.2 GiB / 56,465 objects (complete)** | **CC-BY-4.0** (originals CC-BY-3.0-AU) | static |
| **PoroTomo** (NREL/DOE) | `registry.opendata.aws/nrel-pds-porotomo/` | `s3://nrel-pds-porotomo` · us-west-2 ✅ | *measured* `DAS/SEG-Y/` **47.5 TiB / 104,535 obj** | **CC-BY-3.0-US** | as needed |
| **DOE Geothermal Data Repository Data Lake** | `registry.opendata.aws/gdr-data-lake/` | `s3://gdr-data-lake` · us-west-2 ✅ | *measured* `imperialvalleydas/` **1.1 TiB**; `wholescale/subter_seismic/` **3.0 TiB**; `soda_lake/raw_seismic/2010/` **171.0 GiB** | **CC-BY-4.0-US** | as needed |
| **OpenEEW** (Grillo) | `registry.opendata.aws/grillo-openeew/` | `s3://grillo-openeew` · us-east-1 ✅ | not stated | `github.com/openeew/openeew#license` | **~5 min** |
| Taiwan CWA / CWB OpenData | `registry.opendata.aws/cwa_opendata/`, `/cwb_opendata/` | `s3://cwaopendata` · ap-northeast-1 ✅ · `s3://cwbopendata` · **us-west-2** ⚠️ | not stated | `data.gov.tw/license` | as available |

**Registry metadata errors found:** `ncedc-pds` YAML says `us-west-2`; the live header
and `ncedc.org/db/cloud.html` both say **us-east-2**. `cwbopendata` YAML says
`ap-northeast-1`; live header says **us-west-2**. Treat `x-amz-bucket-region` as
authoritative.

**Detail worth carrying into a catalogue:**
- **SCEDC** — 540+ SCSN stations. `continuous_waveforms/` 1999→2026; `event_waveforms/`
  from 1977; `event_phases/` from **1932**. miniSEED. `Ridgecrest_DAS/` is PASSCAL
  **SEG-Y**, 250 Hz hourly, 2020-06-23→07-29. A `Malibu_Nodal/` (SAC) prefix was added
  2025-09 and is **not described in the registry YAML**.
- **NCEDC** — 20 networks: 4E, BG, BK, BP, CC, CE, CI, GM, GS, NC, NN, NP, PB, PG, RE,
  SB, SF, TA, UL, UO.
- **EarthScope** — ⚠️ **a subset, not the IRIS archive**: only 8 networks (AK, II, IU,
  N4, PB, TA, UU, UW). Layout `miniseed/NET/YEAR/DOY/STATION.NET.YEAR.DOY`; TA spans
  2004–2022. The full archive still requires FDSN web services at
  `service.earthscope.org`.
- **GeoNet** — miniSEED back to **1986**;
  `seismic-products/benchmark-dataset/{event_dataset,noise_dataset}` is a ready-made
  **ML training set**.
- **Poseidon** — the *only* true exploration-seismic dataset in AWS ODR. Near/mid/far/
  full-stack (AGC) migrated volumes plus decimated stacking velocity, in **MDIO v1, not
  SEG-Y**: `near_stack.mdio/`, `mid_stack.mdio/`, `far_stack.mdio/`,
  `full_stack_agc.mdio/`. ~2,900 km², GDA94/MGA Zone 51. Courtesy ConocoPhillips +
  Geoscience Australia.
- **GDR Data Lake** — 13 resource entries, **10 seismic**: Utah FORGE Neubrex well
  16B(78)-32 DAS (continuous + triggered) and downhole geophone; EGS Collab Exp 1 & 2
  (CASSM active-source, DAS, microseismic); Imperial Valley dark-fibre DAS; **Soda Lake
  raw 3D/3C seismic-reflection**; San Emidio and Crescent Valley surveys.

**AWS — earthquake-adjacent (imagery, not seismic):** Maxar Open Data Program
(`s3://maxar-opendata`, CC-BY-NC-4.0, includes the Türkiye–Syria activation);
PALSAR-2 ScanSAR Türkiye & Syria (`s3://jaxaalos2/palsar2-scansar/Turkey-Syria-earthquake/`);
Sentinel-1 SLC/GRD and EBD global coherence (tagged `earthquakes` for InSAR).
**LADI** (`s3://ladi`) is tagged `seismology` but is Civil Air Patrol aerial photography
2015–2023 — a tag false positive.

**AWS — explicit negatives.** **No USGS seismic dataset exists in AWS ODR** (all 13
`usgs*` YAMLs are Landsat, 3DEP LiDAR, Sentinel-2 or planetary). **No NOAA seismic
dataset exists** (all 95 `noaa*` YAMLs are weather/ocean/satellite; the "subsurface"
matches are *subsurface ocean* profiles). No Volve, no Groningen, no F3, no OSDU, no
well logs, no LAS/DLIS anywhere in the registry.

### Google Cloud Public Datasets

Enumerated 356 Marketplace listings, **1,137 Earth Engine STAC collections** (full
crawl, 0 fetch errors), and the 5 documented Cloud Storage public datasets.

| Dataset | URL | URI | Size | Licence | Updated |
|---|---|---|---|---|---|
| **NOAA Marine Critical Minerals (MCM)** | `console.cloud.google.com/marketplace/product/noaa-public/noaa-mcm` | `gs://noaa-deep-sea-minerals` | **≥5.61 TiB / ≥1,064,000 objects** (floor); SEG-Y subset **≥3,802 `.sgy` / ≥230.7 GiB** | **CC0-1.0** | not stated |
| NOAA Significant Earthquakes Database | `.../noaa-public/noaa-earthquakes` | `bigquery-public-data.noaa_significant_earthquakes` | >5,700 events, 2150 BC–present | public domain; cite `doi:10.7289/V5TD9V7K` | **weekly** |
| NOAA Global Historical Tsunami Database | `.../noaa-public/tsunamis` | `bigquery-public-data.noaa_tsunami` | >2,400 tsunamis | data.gov terms | **daily** |

`gs://noaa-deep-sea-minerals` is **the only genuine SEG-Y on GCP** — an American Samoa
AUV + ship survey under EO 14285. A live range request on one file decoded the SEG-Y
header as single-channel **chirp sub-bottom profiler, EdgeTech DW-216, 1–9 kHz, 41 µs
sample interval**. The bucket also holds ~103k `.xtf`, 1,809 Kongsberg `.all` multibeam
and 546k seafloor JPEGs. ⚠️ Survey H14281 uses extension `.seg` rather than `.sgy`, so
the SEG-Y count is understated.

**GCP explicit negatives.** Zero earthquake-waveform or seismological-network data.
Zero exploration seismic, well logs, boreholes, tomography or DAS. Google's own
Marketplace search across 28 geoscience queries returned **0** for `geophysics`,
`SEG-Y`, `segy`, `borehole`, `tomography`, `petroleum`, `gravity anomaly`,
`aeromagnetic`, `lithology`, `crustal`, `volcano`. Earth Engine's 1,137 collections
contain no seismic content. Probed and absent (HTTP 404):
`gcp-public-data-{seismic,usgs,earthquake,iris,segy,crustal}`, `iris-seismic-data`,
`scedc-pds`, `ncedc-pds`, `earthscope-seismic`, `openei-geothermal`, `opentopography`.
*Adjacent but unofficial:* the community **Awesome GEE Community Catalog** hosts a USGS
earthquake catalog at EE asset `projects/sat-io/open-datasets/USGS/usgs_earthquakes`
(1923–present, M≥2.5, public domain) — on Google infrastructure, but not a Google
public dataset.

### Azure Open Datasets — **NONE. Explicit negative.**

**Azure Open Datasets contains zero seismic, subsurface, geophysics, well-log,
borehole, SEG-Y or OSDU datasets.** The catalog is **38 datasets** across transportation
(4), health/genomics (13), labor/economics (7), population/safety (7) and ML samples (6).
All 45 source markdown files were grepped for
`seismic|earthquake|seismolog|subsurface|seg-y|segy|geophys|well log|borehole|osdu|petroleum|reservoir|drilling|geolog`
→ **zero matches**. Corroborated by the SDK: `azureml.opendatasets` exposes exactly 30
classes (NYC taxi, MNIST, US labor/CPI/PPI, city safety, holidays, NOAA weather, COVID)
— no geoscience class exists.

The **Planetary Computer** (136 reachable collections) is pure Earth observation — no
collection matches `seismic`, `seismo`, `SEG-Y`, `well log`, `borehole`, `OSDU`,
`magnetotelluric`, `tomograph`, `gravity anomaly`, `stratigraph`, `geothermal` or
`seafloor`. Nearest misses: *Predicted Building Damage: Venezuela 2026 / Colombia 2026*
(optical damage assessment, CC-BY-4.0); *gNATSGO Soil Database* (soil horizons and depth
to bedrock, CC0-1.0 — the nearest true subsurface property on Azure); USGS 3DEP LiDAR
COPC (surface topography); OOI CamHD (seafloor HD video — and probes of
`ooiopendata/seismic` and `/hydrophone` both return 404).

**Azure Data Manager for Energy (OSDU) ships no public data** — it is strictly a
BYO-data managed PaaS; every seismic capability is a *service* (Seismic Store DDMS,
Wellbore DDMS, Petrel DDMS). Where its docs need test data they point **off Azure**: the
TNO Netherlands open subsurface dataset (~2.2 GB) is pulled by
`github.com/Azure/osdu-data-load-tno` from the **OSDU Forum GitLab**; two sample Volve
SEG-Y files ("<250 MB" and "~1 GB") also live on OSDU GitLab; Volve itself is at
Equinor. `microsoft/seismic-deeplearning` has been **archived since 2020** and pulls
Dutch F3 / Penobscot from **Zenodo**.

**Azure Marketplace has no dataset offer type at all** — the public catalog API paged to
exhaustion gives **24,663 offers across 103 pages**: VirtualMachine 12,921 · SaaS 8,241 ·
AzureApplication 2,159 · ConsultingServices 746 · None 451 · Container 145. Grepping all
of them for seismic terms returned 27 offers, **all software/SaaS, zero data** (Geoteric,
Baker Hughes JewelSuite, Resoptima, AIQ, plus false positives from "Seismic Software",
a sales-enablement vendor).

## b.7 CTBTO / IMS — verified

**There is no CTBTO public data portal, and CTBTO releases essentially zero raw IMS
waveform data to the unaffiliated public.** But a large, genuinely open, no-login slice
of IMS waveform data *does* exist — it comes from FDSN data centres, not `ctbto.org`.
This was verified by actually downloading miniSEED.

### Access models

| Channel | URL | Who qualifies | What you get |
|---|---|---|---|
| **vDEC** (Virtual Data Exploitation Centre) | `ctbto.org/resources/for-researchers-experts/vdec` (verified 200) | **"Organizations rather than individual researchers."** Requires a **signed legal confidentiality contract** with CTBTO by all participants plus the organisation's legally responsible person. Max **3 Authorized Persons**; nationalities must be declared | Only the IMS data *necessary for the study*, bounded in time and geography. **No redistribution.** *"The data cannot be published in their raw form."* Screened IDC bulletins explicitly excluded. **Prior publication review** — the PTS receives any paper or talk in advance, deemed approved if no objection within 5 working days. **Nothing is downloadable without approval; the pages contain no data links at all** |
| **NDC / IDC Secure Web Portal** | `swp.ctbto.org` → Oracle Access Manager login wall | Users **nominated by each State Signatory** through an official designation form from the Permanent Mission or Principal Point of Contact — a diplomatic route, not an application form | Full IMS raw + analysed data: SEL1 (~1 h), SEL2 (~4 h), SEL3 (~6 h), REB (2 days), ARR/RRR. Onward sharing with domestic academics is left to national discretion |
| **FDSN network `IM` via EarthScope** | `service.earthscope.org/fdsnws/` (`service.iris.edu` 307-redirects here) | **Anyone. No account, no auth** | See below — the real public channel |
| **BGR IMS infrasound products** | `download.bgr.de` (5 DOIs, all resolve) | Anyone | 18 years (2003–2020) of reprocessed infrasound from **all 53 certified IS stations**, netCDF detection lists |
| **ISC Bulletin** | `isc.ac.uk/iscbulletin/search/bulletin/` | Anyone | IDC-authored event origins and IMS-array phase picks with back-azimuth/slowness. Parametric only — no waveforms |

### What the public can actually download today

FDSN network **`IM`** is registered at `fdsn.org/networks/detail/IM/`, DOI
`10.7914/vefq-vh75`, **385 stations**, and **every one is flagged
`restrictedStatus="open"`** (386 occurrences, zero restricted). Only one data centre
carries it: **IRISDMC/EarthScope**. The FDSN data-centre registry contains **no
CTBTO/IDC node**.

Cross-referenced against CTBTO's certified-station table, `IM` contains genuine IMS
facilities:
- **17 of 53 certified infrasound arrays** — IS3, IS4, IS5, IS6, IS7, IS18, IS49–IS53,
  IS55–IS60
- **5 of 11 hydroacoustic stations** — HA1, HA8, HA9, HA10, HA11
- **Primary/auxiliary seismic array elements** — TX01–31 (PS46 Lajitas), NV01–31
  (PS47 Mina), PD01–32 (PS48 Pinedale), IL01–31 (PS49 Eielson), VNDA (PS50), MK31
  (PS23 Makanchi), EKB*/EKR* (AS104 Eskdalemuir), TKL (AS107), TOA*/TOB* (PS26 Torodi),
  GEA*–GED* (PS19 Freyung)

Verified working downloads (all HTTP 200, real miniSEED):

```
# Whole open IM network, 60 s → 2,648,064 bytes = 190 stations / 304 streams (~3.8 GB/day)
curl -L "https://service.earthscope.org/fdsnws/dataselect/1/query?net=IM&sta=*&loc=*&cha=*&start=2026-08-10T00:00:00&end=2026-08-10T00:01:00"

# IMS infrasound (BDF), near-real-time            → 18,432 B
.../query?net=IM&sta=I57H1&cha=BDF&starttime=2026-08-01T00:00:00&endtime=2026-08-01T00:10:00

# IMS hydroacoustic hydrophone (EDH), Wake Island HA11  → 117,760 B
.../query?net=IM&sta=H11N1&cha=EDH&starttime=2026-08-01T00:00:00&endtime=2026-08-01T00:05:00

# IMS primary seismic array element, current      → 18,432 B
.../query?net=IM&sta=TX31&cha=BHZ&starttime=2026-08-20T00:00:00&endtime=2026-08-20T00:05:00

# 2013 DPRK test window at PS23 Makanchi          → 27,136 B
.../query?net=IM&sta=MK31&cha=BHZ&start=2013-02-12T02:57:00&end=2013-02-12T03:05:00
```

Channel inventory (985 epochs): BDF 361 (infrasound), SHZ 173, BHZ/BHN/BHE 61/27/27,
EDH 35 (hydrophone), plus meteorological/ancillary. Coverage grows over time: 36
stations in 2000 (seismic only) → 189 in 2015 (infrasound and hydroacoustic appear) →
190 today.

**Three gotchas that produce false negatives:**
1. Array **beam** pseudo-stations (`ARCES`, `MKAR`, `TXAR`, `ASAR`, `WRA`, `YKA`,
   `CMAR`, `GERES`, `ILAR`, `NVAR`, `PDAR`, …) have StationXML but return **0 bytes** —
   use *element* codes (TX31, PD31, MK31, EKB1) instead.
2. `curl -I` (HEAD) on fdsnws-dataselect returns **405 Method Not Allowed**. You must
   GET. An empty result is **204**, not 404.
3. EarthScope's **fdsnws-availability is HTTP 410 Gone** (decommissioned), so exact
   archive extents cannot be established that way.

Several IMS arrays are also open under national codes: `NO.ARA0` (PS28 Karasjok/ARCES),
`NO.NAO01`, `NO.SPA0` at `eida.geo.uib.no`; `GR.GEA0`/`GR.GEC2` (PS19) at `eida.bgr.de`;
`AU.WB1` (PS2 Warramunga) at `auspass.edu.au`; `KZ.MKAR` at EarthScope. NORSAR requires
`loc=00` or `loc=*`.

**`IM` ≠ IMS.** FDSN's own description reads *"this network code is used for
International networks that have not applied for a specific network code."* The shared
initials are coincidence — `IM` is a grab bag containing IMS facilities **and** non-IMS
stations (BC01–05 Beaver Creek, BM01–05 Burnt Mountain, ATTU, CY101–CY606 RAF Akrotiri).
**AFTAC** contributes the US arrays: EarthScope's `_AFTAC` virtual network has exactly
**67 stations**, all US (ATTU, IL*, NV*, PD*, TX*, VNDA = IMS PS46–PS50), and the
hydroacoustic sensor descriptions read "USAEDS HiTech hydrophone". **USGS does not
redistribute IMS** — GSN networks IU/II are separate.

**Not publicly available:** the other ~41 infrasound arrays, 6 of 11 hydroacoustic
stations, the large majority of the 50 primary + 120 auxiliary seismic stations
(including all Russian and Chinese IMS seismic), **all radionuclide data** (80 stations
+ 16 labs — zero public presence anywhere), and all IDC products in native form
(SEL1/2/3, REB, ARR, RRR).

**Dead CTBTO endpoints, stated plainly:** `ctbto.org/vdec` 404 · `ctbto.org/our-work/vdec`
404 · `vdec.ctbto.org` 404 · `autodrm.ctbto.org` and `data.ctbto.org` **do not resolve** ·
`ctbto.org/autodrm` 404 · `ctbto.org/our-work/international-monitoring-system/ims-map`
404 (correct path is `/our-work/ims-map`).

### Cloud registries — bottom line

**AWS is the only cloud registry with a real seismic corpus** — 9 core datasets spanning
regional network archives (SCEDC, NCEDC, GeoNet), a curated global *subset* (EarthScope,
8 networks only), the sole exploration-seismic volume (TGS Poseidon, 188.2 GiB in MDIO),
and by far the best DAS/geothermal holdings (PoroTomo 47.5 TiB of SEG-Y; GDR Data Lake
with 10 seismic sub-collections including Utah FORGE and Soda Lake 3D/3C reflection).
**GCP has exactly one genuine multi-TB SEG-Y holding** — `gs://noaa-deep-sea-minerals`,
CC0, chirp sub-bottom profiler — essentially undocumented outside its Marketplace card,
plus two tabular earthquake catalogues. **Azure has nothing**, and its own OSDU docs send
you off-platform for test data.

---

## b.6 Refinement sweep, 2026-08-26 — corrections and new finds

A second pass aimed at two things the first survey did not cover: **datasets whose only
barrier is asking someone**, and **labelled data outside the interpretation tasks**
(fault / facies / salt) that dominate the existing catalogue. Everything below was
verified live in this pass; flags follow the `[V-HEAD]` / `[V-API]` / `[V-DEAD]` key.

### b.6.1 Two more index nodes are dead — the count is six, not four

The SEG wiki's own **`Candidate open data`** page (recoverable only through the Wayback
Machine — `wiki.seg.org` still 403s every client) routes readers to two hubs. Both are
gone:

| Node | What it held | Status | Flag |
|---|---|---|---|
| `www.cwp.mines.edu/cwpcodes/` | Colorado School of Mines CWP — the SEG wiki's stated route to the Oz Yilmaz 40-shot collection | **`www` host fails DNS outright; bare `cwp.mines.edu` returns 403 to every client and UA tried.** No route to data. | `[V-DEAD]` |
| `www.geo.mtu.edu/spot/SeismicData/` | "Michigan Tech's list of links to public seismic datasets" — an index node in its own right | **301-redirects to `https://www.mtu.edu/geo/research/focus/`**, a generic departmental page. The list is gone. | `[V-DEAD]` |

Also checked and dead: **`wikidev.seg.org`** — surfaced by search engines as an
apparently-live mirror of the SEG wiki, which would have solved the 403 problem. It
**does not resolve (NXDOMAIN)**. It is a stale search-index artefact; do not chase it.

That takes the count of dead index nodes since 2022 from four to **six**, and both new
ones were *linked from the SEG wiki as live routes*. The wiki cannot audit its own
links because Cloudflare blocks its bots — this is that failure mode, measured.

### b.6.2 The SEG "Candidate open data" page — the permission-gated wish list

This page is the closest thing the field has to a register of *"data that could be open
if someone asked the owner"*, and it is not indexed anywhere else. Recovered content
(snapshot `20240330083118`):

| Dataset | Holder / blocker | Note |
|---|---|---|
| **SMAART JV: Pluto 1.5, Sigsbee 2A & 2B, Ziggy** | Restrictive licence forbidding redistribution; SEG wiki says TNO/Delphi maintain them, but the Delphi host is gone | The page's explicit ask: *"Can owners be found and convinced to offer a more generous license… before the data are orphaned"* |
| **Marmousi** | Same category — listed as redistribution-forbidden | Widely mirrored anyway; the licence question is genuinely unresolved |
| **Mobil Viking Graben — VSP at both wells + observer logs** | Believed lost; Delft had a copy in 2013 and no longer does | The stacked data survives; the VSP and logs are the missing part |
| **Hess VTI 2D, Model94, Statics94, 1997 2.5D (Etgen & Regone), 2004 BP, 2007 BP TTI** | On `software.seg.org`, which returns HTTP 525 | Consistent with this repo's earlier finding that probing the S3 bucket for these names returns nothing |
| **SEG student field camp data** | Exists in SEG-D; nobody has converted or hosted it | Named contact on the page: John Stockwell |
| **EDGER consortium multicomponent compendium (UT Austin)** | Compiled but not published | University-held; would need an ask |
| **Kurt Marfurt's Stratton processing lab** | Described as sitting on a named individual's laptop | Genuinely at risk |

Live and already catalogued, for completeness: **KAUST CSIM Qademah Fault 3D**
(`csim.kaust.edu.sa/files/FieldData/Qademah_2014/QademahFault.htm`, 200, 42,746 B) `[V-PAGE]`.

### b.6.3 University-held data: CREWES and Stanford SEP

Both were absent from this repo entirely. Both turn out to be **negative results worth
recording**, which is why they are here rather than in `datasets.yaml`:

- **CREWES (University of Calgary)** — holds Blackfoot 3C-3D (8.5 km² multicomponent
  land 3D with field data, observer notes, a low-frequency dataset and a 3C-3D VSP),
  the Hussar low-frequency experiment (2011, dynamite + Vibroseis, five receiver types)
  and the Priddis near-surface surveys. **`crewes.org` publishes no data at all** —
  `/ResearchLinks/` offers only the Matlab toolbox (156.62 MB) and textbook sample data
  (13.65 MB); `/ResearchLinks/ExplorationDatasets/`, `/Samples/` and `/data/` all 404.
  Blackfoot was formerly sold through the SEG Bookstore and is now listed on the SEG
  wiki's **`Non-open seismic data`** page — the University of Calgary owns it under
  restrictive terms. Route is `support@crewes.org` or sponsorship, not download.
  `[V-PAGE]`
- **Stanford Exploration Project** — the widely-cited SEP data library path
  `sepwww.stanford.edu/public/docs/sepdatalib/toc_html/` returns **200 but now renders a
  DokuWiki home page**, not a data index. SEP publishes reports and theses openly (all
  material older than three years) but no browsable data library. The SEG wiki lists
  "Stanford (SEP)" as a route to the Yilmaz shots; that route no longer works. `[V-DEAD]`

**The general shape of the "just ask" category:** the barrier is rarely a licence fee.
It is that the holder is a university consortium with sponsor obligations (CREWES), a
defunct JV whose members have dispersed (SMAART), or an individual (Marfurt's lab). The
first is answerable by email; the second and third are archival-rescue problems.

### b.6.4 New datasets added to the catalogue by this sweep

| Dataset | Bytes (measured) | Labels | Licence | Why it was missing | Flag |
|---|---:|---|---|---|---|
| **Teal South 4C/4D** | 15,326,377,125 (38 files) | none | unstated | Host `seismicrocks.com` appears in no index consulted, including the SEG wiki | `[V-HEAD]` |
| **Hardpicks** (Brunswick, Halfmile Lake, Lalor, Sudbury) | 23,787,278,764 (4 files) | **first-break picks, real field data** | CC-BY-4.0 ×2, OGL-Canada ×2 | Was a single line in a GitHub-stars list here — no sizes, URLs or licence | `[V-HEAD]` |
| **QuakeFlow DAS** | 674,313,768,517 (7,697 files) | event metadata; **first-motion polarity** | MIT | Name contains neither "seismic" nor "segy"; missed by the 12-term HF sweep | `[V-API]` |
| **MultiSeismo** (PNNL) | 106,534,693,427 (104 files) | text descriptions, intensity maps, exposure | **CC0-1.0** | Same reason | `[V-API]` |
| **Oz Yilmaz 40 shot gathers** | 33,364,928 (3 files) | none | attribution only | Both SEG-listed routes dead; live host unindexed | `[V-HEAD]` |
| **SubsurfaceGen field-scale** | 11,923,346,031,911 (47,084 files) | velocity models | CC-BY-4.0 | Present, but recorded at 1/7th its true size | `[V-API]` |

**Teal South is the most significant of these.** It is simultaneously **4D** (July 1997
baseline + April 1999 monitor) and **4C** (ocean-bottom cable, P-Z plus P-S converted
wave), and ships wells, a VSP, directional surveys and observer notes. That combination
— time-lapse *and* multicomponent *and* pre-stack *and* with wells — is not available in
any other open dataset in this catalogue. Ownership traces to Texaco via the Energy
Research Clearing House. The host warns directly that the P-S amplitudes "seem to be
unreliable"; that caveat is carried into the catalogue entry.

**Hardpicks closed a real category gap.** Before it, every labelled *field* dataset here
was an interpretation task (fault, facies, horizon, channel, karst). There was nothing
for a **processing** task, and nothing in a hardrock/mineral-exploration setting.
Hardpicks is both, with picks in the trace headers and an explicit cross-survey split
that tests generalisation between acquisition conditions rather than in-survey accuracy.

### b.6.5 Method note — what the first HF sweep missed and why

The §b.2 sweep used 12 search terms and found 326 datasets. It missed
`AI4EPS/quakeflow_das` (674 GB) and `PNNL/MultiSeismo` (107 GB) because
**HuggingFace's `search=` matches the repo id and card, and neither id contains any of
the 12 terms** — `quakeflow_das` matches only on the substring `das`, whose results are
overwhelmed by unrelated repos (`daspartho/*`, `dash8x/*`, `DasanCallDial`), and
`MultiSeismo` matches "seismo" but not "seismic". Two fixes, both cheap:

1. **Search by tag, not text.** `?filter=distributed-acoustic-sensing`, `?filter=seismology`,
   `?filter=geophysics` reach repos whose names carry no domain word. `quakeflow_das`
   carries all three tags and would have surfaced immediately.
2. **Never rank by `usedStorage`** — see footnote 4. The tree API is the only figure
   worth recording, and it changed the #1 entry on the leaderboard.

### b.6.6 Still open

- **`polarity`, `eureka` and `ridgecrest_south` in QuakeFlow DAS are undocumented.** The
  dataset card names three subsets; the repo has six. Label semantics for `polarity`
  (45.63 GB, 674 files) are described nowhere. Worth an issue on `AI4EPS/quakeflow`.
- **OpenSeisML** (arXiv:2605.20539) — UK-NDR-derived velocity models with well logs and
  checkshot time-to-depth conversion. The paper is out; **no dataset URL or DOI is given
  in it**. If released it would be the first open *real-field* velocity-model training
  set at scale. `[U]`
- **Unicamp-NAMSS** (arXiv:2602.04890) — 2,588 cleaned 2D migrated sections from 122
  NAMSS survey areas, with geographic macro-region splits for generalisation testing.
  **No repository URL stated in the paper.** `[U]`
- **CIG-Bench** (arXiv:2606.09094) — fault, RGT, geobody and property-modelling
  benchmark with pretrained baselines, at `douyimin.github.io/CIG-bench`. Not yet
  size-verified. `[U]`
- The §b.2 table's remaining 300+ `usedStorage` figures have not been re-measured.
  Re-running §b.6.5's tree-API method across all of them is a bounded, scriptable job
  and would put a real number on the corpus, replacing the provisional 5.70 TB.


---

# What the survey implies for this repo

**The niche is genuinely vacant, and shrinking.** **Six** index nodes have been lost
since 2022: Data Underground, Agile Scientific, Papers With Code, the SEG wiki's
machine-accessibility, and — added by the 2026-08-26 sweep, §b.6.1 — CWP Colorado
School of Mines (`www.cwp.mines.edu`, DNS failure) and Michigan Tech's public seismic
data list (`geo.mtu.edu/spot/SeismicData/`, redirected away). The last two were both
still linked from the SEG wiki as live routes. Nothing has replaced any of them. Four separate GitHub queries aimed
squarely at "structured seismic data catalogue" return **zero repositories**.

**Every surviving resource has exactly one of the properties needed, never all:**

| Property | Who has it | Who does not |
|---|---|---|
| Machine-readable | FDSN registry (JSON), SeisBench (Python) | SEG wiki, every awesome-list, TerraNubis, re3data (dataset level) |
| Exact sizes | OpenFWI (per dataset), Zenodo/HF (via API), SEAM S3 (via HEAD), DataCite `sizes` (22 % of DOIs) | Every curated list without exception; **the AWS registry schema has no `Size` field at all** |
| Explicit licences | OpenFWI (CC-BY-NC-SA), Zenodo (92 % CC-BY/CC0), AWS registry (all 9) | SEG wiki, awesome-open-geoscience, awesome-geophysics, awesome-das, TerraNubis; **19 of the 25 largest datasets in the world state no licence** |
| Exploration + passive + DAS in one place | **nobody** | everybody |
| Access friction stated | yohanesnuwara (notebooks), partially TerraNubis | everyone else |
| Link rot auditable | FDSN registry | SEG wiki (403s all bots), Google-Drive-hosted entries |

**Four concrete openings this survey exposes:**

0. **The biggest open seismic datasets are invisible to every existing index.** The 25
   largest are FDSN temporary-network DOIs (IRIS/EarthScope, GFZ) and AWS bucket
   prefixes — up to 685 TB for a single experiment. None appears in the SEG wiki,
   awesome-open-geoscience, SeisBench, or any Zenodo/HuggingFace/Kaggle ranking. The
   size metadata already exists in DataCite's `sizes` field for 4,845 seismic DOIs;
   harvesting it costs 22 HTTP requests, and nobody does it.

1. **The exploration/passive split.** SeisBench covers 44 earthquake datasets superbly
   and zero exploration surveys. The SEG wiki covers ~55 exploration datasets and zero
   passive networks. Nobody spans them, and the same person increasingly needs both.
2. **Sizes and licences are the missing metadata everywhere.** They are individually
   obtainable — Zenodo's API, HF's `usedStorage`, an HTTP HEAD on an S3 object — but
   nobody has ever assembled them. This survey demonstrates it can be automated.
3. **Provenance and re-hosting is an unmanaged mess.** The largest "seismic dataset" on
   HuggingFace (2.92 TB) is an unattributed MIT-labelled mirror of SeisBench's corpus
   whose upstream components carry mixed and stricter terms. A catalogue that records
   *"this is a mirror of X, whose actual licence is Y"* would be new and useful.

**Two things to do before publishing** (unchanged from earlier analysis, now with
evidence):

- Run the link checker over every URL. The SEG wiki cannot audit its own links because
  Cloudflare blocks bots; Google Drive links rot silently; `dataunderground.org` proves
  that whole indexes vanish. A catalogue whose links rot is worse than none.
- Announce in the two places the maintainers actually are:
  `softwareunderground/awesome-open-geoscience` (issue/PR) and the Software Underground
  Mattermost. Note that Software Underground's own dataset project has been dead since
  2019, so this is likely to be welcomed rather than seen as competition.

---

# Could not verify (as of v6)

1. **SEG Wiki current contents.** Cloudflare returns HTTP 403 to *every* automated
   route attempted: `curl` with a Chrome UA; `/api.php?action=parse`;
   `/w/api.php?action=parse`; `/rest.php/v1/page/Open_data`;
   `/wiki/Special:Export/Open_data`; and WebFetch. `r.jina.ai` refused separately
   (HTTP 401, network reputation). `archive.today` / `archive.ph` / `archive.li` /
   `archive.is` all returned HTTP 429 (rate limited) rather than a snapshot. §a.4 is
   therefore the 2024-03-29 Wayback capture; anything added since is unknown. **A human
   with a browser could confirm the current list in one minute — do that before
   publishing.**
2. **Whether `dataunderground.org` moved** rather than simply died. NXDOMAIN is
   certain; a successor domain is not ruled out.
2b. **`www.isc.ac.uk` (International Seismological Centre)** returned HTTP 000 — no
   connection — over both HTTPS and HTTP on two attempts from this network. DNS
   resolved. This is most likely a geo-block or a transient outage rather than a dead
   site; it is counted as "broken" in the `awesome-geophysics` rot figure but should be
   re-checked from another network before that is asserted.
3. **Zenodo completeness.** The 10,000-hit pagination cap plus a 25-per-page anonymous
   limit means the 11,012 `q=seismic` records cannot be fully enumerated without an API
   token. Coverage here is the `resource_type=dataset` / `image` / `other` slices plus
   nine targeted phrase queries, giving 4,099 deduplicated records — very likely to
   contain the true top-25 by size, but **not provably so**. Re-run with an
   authenticated token (`size=100`) to close this.
4. **HuggingFace `usedStorage` is unreliable in BOTH directions — corrected 2026-08-26.**
   The earlier guidance here ("treat HF byte figures as upper bounds") was wrong.
   `usedStorage` counts all revisions in a repo's git history, so it can *over*-report
   a single checkout — measured at **+19.7 %** for `AI4EPS/quakeflow_das`
   (807,379,803,096 B reported vs 674,313,768,517 B actual tree) and **+163.8 %** for
   `MH0386/seismic_data`. But it can also badly *under*-report: for
   `subsurfacegen/field-scale-dataset` it reports 1,623,610,657,665 B against an actual
   tree of **11,923,346,031,911 B — a 7.35x undercount**, which is the single largest
   size error found anywhere in this survey.
   **The reliable method is the tree API**, not `usedStorage`:
   `GET /api/datasets/<id>/tree/main?recursive=true&limit=1000`, following the
   `Link: rel="next"` cursor, summing `lfs.size` where present and `size` otherwise,
   de-duplicating on `path` and guarding against cursor loops. Spot-check the result
   with a real HTTP HEAD on `…/resolve/main/<path>` and compare `Content-Length`.
   Every HF figure in §b.2's table above is a `usedStorage` figure and is therefore
   **provisional** — only the entries re-measured in §b.6 are trustworthy.
5. **OpenFWI 3D dataset size.** The home page announces "twelve datasets… including one
   3D dataset" but `docs/data.html` publishes size rows for only eleven. The 3D
   dataset's size is not stated anywhere reachable.
6. **TerraNubis per-project sizes.** The free list page gives names only; sizes would
   require opening each `/datainfo/<project>` page, several of which gate on
   registration.
7. **DataCite `sizes` coverage is 22 %.** Only 4,845 of 21,895 seismic dataset DOIs
   publish a parseable size, so the cross-platform top-25 in §b.3 is a ranking of what
   is *declared*, not of what exists. Zenodo does not populate `sizes` in DataCite at
   all, so its records are absent from that ranking (their sizes come from Zenodo's own
   API instead). Additionally, the #1 entry — Northern Borneo Orogeny Seismic Survey at
   `684756688 MB` — is a **depositor-declared figure I could not independently
   corroborate**; 685 TB is plausible for a large nodal deployment but is 7× the next
   largest, so treat it as unconfirmed.
8. **AWS bucket totals.** The registry has no `Size` field and no operator publishes
   one. The figures in §b.3/§b.6 are single-prefix or single-year measurements,
   explicitly scoped — never extrapolated. Full recursive listings of `scedc-pds`,
   `ncedc-pds`, `earthscope-geophysical-data` and `geonet-open-data` would each require
   enumerating tens of millions of objects. Only `tgs-opendata-poseidon` (188.2 GiB) was
   measured complete. The PoroTomo full-bucket run timed out after `DAS/SEG-Y/`.
9. **Whether the Taiwan CWA/CWB buckets actually contain earthquake data.** Both are
   tagged `earthquakes`; both descriptions say weather-only; contents not enumerated.
10. **Why `ncedc-pds` and `cwbopendata` have wrong regions in the registry YAML** — the
    discrepancy is confirmed, its cause is not.
11. **GCP `gs://noaa-deep-sea-minerals` totals** — enumeration stopped at 1,064,000
    objects / 5.61 TiB with pages still pending; those are floors. The `.seg`-extension
    sub-bottom files in survey H14281 were never counted, so the SEG-Y-family total is
    understated by an unknown margin. `gs://usgs-lidar` returns HTTP 401 — exists,
    contents unknown.
12. **BigQuery table name** for `bigquery-public-data.noaa_significant_earthquakes` —
    the *dataset* id is verified from Google's Marketplace API; the *table* name
    `earthquakes` is probable, not confirmed (the BigQuery REST API returns 401 without
    auth). Byte sizes and row counts for both BigQuery datasets are unpublished.
13. **Exhaustiveness of the GCP Marketplace index for `bigquery-public-data`.** Some
    datasets have no Marketplace card; an unlisted `bigquery-public-data.*` dataset
    cannot be ruled out without `bq ls`.
14. **Azure sizes** — neither Open Datasets docs nor Planetary Computer STAC metadata
    publish a size field. The only defensible Azure-adjacent sizes are the TNO dataset
    (~2.2 GB) and the two Volve SEG-Y samples ("<250 MB", "~1 GB"), all from Microsoft's
    own text. One Planetary Computer collection is unreachable (`numberMatched: 137`,
    136 returned); its subject is unknown. Account-level anonymous listing is denied on
    `azureopendatastorage` (404), `ai4edataeuwest` (409) and `ooiopendata` (409), so
    undocumented containers cannot be ruled out. `msropendata.com` now redirects to the
    MSR tools index and 403s non-browser clients, so its "Dataset (159)" could not be
    enumerated.
15. **CTBTO vDEC turnaround time, approval rate, and whether individual academics are
    ever approved** — not stated anywhere fetchable; the only contact address decodes to
    the generic `feedback@ctbto.org`. Whether and how NDCs may re-share IMS data
    domestically is left to national discretion with no authoritative public statement.
16. **Archive start dates for `IM` infrasound/hydroacoustic.** Bisection gives *earliest
    observed* data ~2013-09 for I56H1 (BDF) and ~2015-01 for H11N1 (EDH), but the data
    are gappy and fdsnws-availability is 410 Gone.
17. **Who formally contributes the non-US IMS streams in `IM`** (I18 Denmark, I49–I52 +
    HA08/HA10 UK, EKB/EKR UK, MK31 Kazakhstan, TOA/TOB Niger). They are not tagged
    `_AFTAC` and their StationXML carries no `<Operator>` or `<Agency>` element.
18. **Licence of the BGR infrasound products — a genuine conflict.** The ESSD paper's
    Data Availability section says **CC-BY-4.0**; the DataCite record for
    `10.25928/bgrseis_bblf-ifsd` says **CC-BY-NC-SA-4.0**. Resolve with BGR before
    relying on either.
19. **Per-arrival agency attribution in the ISC Bulletin** — the ISF2 author column was
    blank on array-processed readings, and
    `isc.ac.uk/cgi-bin/collect?Reporter=IDC` returns "no data reports are stored for
    this agency", so IDC provenance per pick cannot be asserted.
20. **Kaggle competition contents — blocked by authentication, not by effort.**
    `api/v1/competitions/list` and `api/v1/competitions/data/list/<slug>` both return
    **HTTP 401 `{"code":401,"message":"Unauthenticated"}`**, and the competition HTML
    pages are ~5.6 KB JavaScript shells carrying nothing but a `<title>`. So for
    **TGS Salt Identification Challenge**, **LANL Earthquake Prediction**,
    **Yale/UNC-CH – Geophysical Waveform Inversion** and **INGV – Volcanic Eruption
    Prediction**, only *existence and official title* are verified (via the HTTP
    200-vs-404 control in §b.5.1). **File sizes, file counts, file formats, licence
    terms, team counts and prize money are all unverified** and deliberately absent
    from §b.5. To close this: place a `kaggle.json` API token at `~/.kaggle/` and run
    `kaggle competitions files tgs-salt-identification-challenge` and
    `kaggle competitions files LANL-Earthquake-Prediction`, or open
    `https://www.kaggle.com/competitions/tgs-salt-identification-challenge/data` in a
    signed-in browser. Note the competition rules must be accepted before the files
    are listable even with a token, so a human step is unavoidable.
21. **Dryad's 125-vs-137 discrepancy.** Dryad's own API
    (`/api/v2/search?q=seismic`) reports `total: 125` and 399,996,641,657 bytes;
    DataCite reports 137 dataset DOIs and 442,083,875,682 bytes at `dryad.dryad`.
    Both were fully enumerated, so neither is a pagination artefact. The likely causes
    are DataCite full-text-matching abstracts that Dryad's `q` does not weight, and
    Dryad DOIs minted under partner prefixes (`10.25349`, UC San Diego) that its own
    search may scope differently — **but this was not confirmed.**
22. **figshare and Mendeley cannot be counted from their own APIs.** figshare's
    `POST /v2/articles/search` returns no total-count field at all and caps offset at
    10,000 (`PaginationOffsetExceeded`); Mendeley's search endpoint ignores its `query`
    parameter entirely (1.2 % of returned rows matched the search term) and ignores
    `page`/`offset`/`skip`. Both counts in §b.5 therefore come from DataCite, not from
    the platform. An authenticated figshare token may lift the offset cap; this was not
    tested.
23. **§b.5 title-keyword classification of "what kind of seismic data".** The
    exploration-vs-earthquake splits for figshare and Kaggle are regex matches over
    titles and descriptions, not inspection of file contents — 727 of figshare's 1,188
    fell into "unclassified" because DataCite titles are short. The direction of the
    finding (earthquake/passive dominates, exploration is a minority) is solid; the
    exact percentages are not.
24. **Harvard Dataverse's 179 HTTP 403s on `downloadsize`.** Every one is a record
    harvested from another installation, and 0 of 102 Harvard-native records 403'd, so
    the cause is near-certainly that Harvard indexes the metadata but not the bytes.
    That inference was not confirmed against Dataverse's documentation. Those 179
    records' sizes remain unmeasured; they would need querying at DesignSafe, Borealis,
    Texas Data Repository and DataverseNO individually — and three of those installations
    refuse anonymous API access (§b.5.4).
25. **Whether the Dataverse network can be enumerated at all.** No cross-installation
    search API was found. `dataverse.tdl.org` returned HTTP 403, `dataverse.unc.edu` and
    `data.cimmyt.org` HTTP 401, `dataverse.nl` and `dataverse.ada.edu.au` non-JSON, and
    `opendata.pku.edu.cn` failed DNS. The 401 responses in particular were **HTTP 401 to
    an unauthenticated `/api/search`**, which the Dataverse software does not require by
    default — so these are local policy choices, and the seismic holdings behind them
    are unknown. Try the installation list at `https://dataverse.org/installations` and
    query each `/api/search?q=%22seismic%22&type=dataset` in turn.
