<!-- GENERATED FILE — edit catalog/datasets.yaml, then run scripts/build_readme.py -->

# Catalogue

A catalog of open, public, and potentially accessible seismic datasets worldwide — exploration reflection seismic, national archives, earthquake waveforms, DAS, and ML benchmarks.

## At a glance

- **80** catalogued entries across **23** countries/regions
- **53.3 TB** of directly-downloadable data with exact byte counts (15 entries measured)
- **67** entries are free to download (54 with no account at all)

| Category | Entries |
|---|---|
| [Named 3D field surveys](#named-3d-field-surveys) | 10 |
| [Named 2D surveys and line sets](#named-2d-surveys-and-line-sets) | 3 |
| [National / regulator archives](#national-regulator-archives) | 19 |
| [Academic and research archives](#academic-and-research-archives) | 13 |
| [ML-ready and labeled datasets](#ml-ready-and-labeled-datasets) | 9 |
| [Synthetic models and benchmarks](#synthetic-models-and-benchmarks) | 2 |
| [Earthquake / passive waveform archives](#earthquake-passive-waveform-archives) | 7 |
| [Distributed acoustic sensing (DAS)](#distributed-acoustic-sensing-das) | 5 |
| [Strong-motion databases](#strong-motion-databases) | 3 |
| [Planetary and ocean-bottom](#planetary-and-ocean-bottom) | 3 |
| [Hubs, registries, and curated lists](#hubs-registries-and-curated-lists) | 6 |

### Legend

| Badge | Meaning |
|---|---|
| 🟢 open | `open-download` |
| 🟡 free acct | `open-registration` |
| 🟡 request | `open-request` |
| 🟡 academic | `academic-free` |
| 🟠 fee | `fee` |
| 🔴 closed | `closed` |

**"Use" column — what you are permitted to DO with the data:**

| Token | Meaning |
|---|---|
| `COM` | Commercial use permitted |
| `COM?` | Commercial use **not stated** — assume you must ask |
| **`NC`** | Commercial use **excluded** (non-commercial only, or industry must pay a separate licence) |
| `BY` | Attribution required |
| `SA` | Share-alike — derivatives must carry the same licence |
| **`no-redist`** | You may not redistribute the data |
| `ML` | Licence permits ML/AI training use |

> **These flags are a research aid, not legal advice.** They are derived from each holder's published licence text and recorded in `usage_basis` as `spdx` (a recognised SPDX licence), `licence-text` (stated in prose), `per-dataset` (a hub — terms vary per dataset), or `unstated` (the holder publishes no usage terms). **Anything marked `COM?` or `unclear` means the holder did not say — verify before commercial use.**

Sizes marked *(est.)* are derived from line-km or survey counts and can be off by a factor of a few. Machine-readable bounds live in `size_bytes`, or `size_bytes_min`/`size_bytes_max` where the holder publishes only a range. See [catalog/SCHEMA.md](catalog/SCHEMA.md).

## Named 3D field surveys

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [Poseidon 3D](https://registry.opendata.aws/tgs-opendata-poseidon/) | Australia — NW Shelf, Browse Basin (~2,900 km²) | 3D angle stacks: near 55.23 / far 55.09 / mid 54.99 / full-AGC 36.80 GB, MDIO (zarr) and SEG-Y | 202.11 GB MDIO bucket (56,465 objects); ~50 GB SEG-Y set | 🟢 open | CC BY 4.0 (AWS registry); CC BY 3.0 AU (TerraNubis) | COM BY ML | [s3](https://tgs-opendata-poseidon.s3.amazonaws.com/index.html) · [segy+wells](https://terranubis.com/datainfo/NW-Shelf-Australia-Poseidon-3D) |
| [Volve field dataset (Equinor)](https://www.equinor.com/energy/volve-data-sharing) | Norwegian North Sea | 3D and 4D seismic (pre- and post-stack), VSP | ~5 TB total | 🟡 free acct | Equinor Open Data Licence | **NC** BY | Azure blob download |
| [Kerry 3D](https://wiki.seg.org/wiki/Kerry-3D) | New Zealand — onshore Taranaki | 3D post-stack PSTM, SEG-Y | 1.1 GB | 🟢 open | Free; acknowledge NZ Petroleum & Minerals | COM? BY | [https](http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin/Keri_3D/Kerry3D.segy) |
| [Maui 3D](https://geodata.nzpam.govt.nz/) | New Zealand — offshore Taranaki (Maui field) | 3D post-stack + reprocessed vintages, pre-stack orderable | 10s of GB stack; 100s of GB pre-stack *(est.)* | 🟡 free acct | Open-file under the Crown Minerals Act | COM? | NZP&M exploration database (RealMe login) |
| [Opunake 3D](https://wiki.seg.org/wiki/Opunake-3D) | New Zealand — southern Taranaki (215 km²) | 3D post-stack final stack, SEG-Y | 10.4 GB | 🟢 open | Free; acknowledge NZ Petroleum & Minerals | COM? BY | [https](http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin/OPUNAKE-3D/OPUNAKE3D-PR3461-FS.3D.Final_Stack.sgy) |
| [Parihaka 3D](https://wiki.seg.org/wiki/Parihaka-3D) | New Zealand — offshore Taranaki Basin | 3D post-stack, angle stacks (near/mid/far/full), SEG-Y | ~20.4 GB (4 × 5.1 GB) | 🟢 open | Free; acknowledge NZ Petroleum & Minerals (Crown Minerals) | COM? BY | [full stack](http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin/PARIHAKA-3D/Parihaka_PSTM_full_angle.sgy) · [near](http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin/PARIHAKA-3D/Parihaka_PSTM_near_stack.sgy) · [mid](http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin/PARIHAKA-3D/Parihaka_PSTM_mid_stack.sgy) · [far](http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin/PARIHAKA-3D/Parihaka_PSTM_far_stack.sgy) |
| [Waihapa 3D](https://wiki.seg.org/wiki/Waihapa-3D) | New Zealand — onshore Taranaki | 3D post-stack, SEG-Y | ~1–2 GB *(est.)* | 🟡 request | Free; acknowledge NZ Petroleum & Minerals | COM? BY | SEG wiki link, or order free from NZP&M |
| [Kevin Dome 3D (Big Sky Carbon Sequestration Partnership)](https://edx.netl.doe.gov/) | USA — Montana, Kevin Dome (37.25 sq mi) | 3D nine-component (9C) multicomponent, SEG-Y | ~589 GB SEG-Y | 🟢 open | Free (US DOE-funded; confirm terms on the host record) | COM? | DOE NETL EDX record |
| [Teal South 4C/4D (Eugene Island Block 354)](https://www.seismicrocks.com/tealsouth.html) | USA — Gulf of Mexico, Eugene Island Block 354 (~80 mi offshore Louisiana) | 3D OBC 4-component, time-lapse (4D): 1997 + 1999 surveys, P-Z CMP gathers, P-S converted-wave CCP gathers, final stacks + migrations, SEG-Y big-endian | 15.33 GB (14.27 GiB) across 38 files | 🟢 open | Open download; no licence stated by the host. Released via the Energy Research Clearing House (data originally Texaco). | COM? | [phase-1 P-Z CMP gathers](https://www.seismicrocks.com/tealsouth/seismic/TS-104544-phase1-pz.zip) · [phase-2 P-Z CMP gathers (part 1)](https://www.seismicrocks.com/tealsouth/seismic/TS-104546-phase2-pz-1.zip) · [phase-2 P-Z CMP gathers (part 2)](https://www.seismicrocks.com/tealsouth/seismic/TS-104547-phase2-pz-2.zip) · [phase-1 converted-wave CCP (c1)](https://www.seismicrocks.com/tealsouth/seismic/TS-103685-phase1-c1.zip) · [phase-1 converted-wave CCP (c2)](https://www.seismicrocks.com/tealsouth/seismic/TS-103686-phase1-c2.zip) · [phase-2 converted-wave CCP (c1)](https://www.seismicrocks.com/tealsouth/seismic/TS-103687-phase2-c1.zip) · [phase-2 converted-wave CCP (c2)](https://www.seismicrocks.com/tealsouth/seismic/TS-103688-phase2-c2.zip) · [well logs](https://www.seismicrocks.com/tealsouth/other/TealSouth_WellLogs.zip) · [VSP](https://www.seismicrocks.com/tealsouth/other/TealSouth_VSP.zip) |
| [Teapot Dome 3D (RMOTC)](https://edx.netl.doe.gov/) | USA — Wyoming | 3D post-stack, pre-stack gathers | 14.4 GB | 🟡 free acct | Public domain (US DOE) | COM ML | NETL EDX (free login); also mirrored via SEG wiki |

## Named 2D surveys and line sets

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [FIRE (Finnish Reflection Experiment)](https://www.gtk.fi/) | Finland — Fennoscandian Shield | 2D deep crustal reflection, RAW FIELD SEG-Y included, processed stacks | 1.147 TB | 🟢 open | CC BY 4.0 | COM BY ML | GTK / DOI-registered records |
| [Oz Yilmaz 40 shot gathers](https://www.seismicrocks.com/oz40.html) | Global — 40 shot records from surveys worldwide | 2D shot gathers, Seismic Unix (.su) little-endian, SEG-Y little-endian, display images | 33.36 MB (3 archives) | 🟢 open | No formal licence; acknowledge Oz Yilmaz and SEG (originally released by Western Geophysical) | COM? BY | [Seismic Unix, little-endian](https://www.seismicrocks.com/seismicunix/oz.forty.su.tgz) · [SEG-Y, little-endian](https://www.seismicrocks.com/seismicunix/oz.forty.sgy.tgz) · [shot-gather images](https://www.seismicrocks.com/seismicunix/oz40-images.tgz) |
| [COCORP (Consortium for Continental Reflection Profiling)](http://cocorp.eas.cornell.edu) | USA — continental deep crustal transects | 2D deep crustal reflection, PRE-STACK shot gathers (780 SEG-Y), 177 stacks | ~139.8 GiB total (121.9 GiB pre-stack shot gathers) | 🟢 open | Unstated — academic archive, no licence text published | COM? | [apache index](http://cocorp.eas.cornell.edu) |

## National / regulator archives

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [GSQ Open Data Portal (Queensland)](https://geoscience.data.qld.gov.au/data/seismic/?type=seismic&res_format=segy) | Queensland — Bowen, Surat, Cooper/Eromanga, Galilee | 2D and some 3D, SEG-Y + support data | ~100s of TB (1,402 seismic datasets) | 🟢 open | CC BY 4.0 (Queensland Government) | COM BY ML | [ckan-api](https://geoscience.data.qld.gov.au/api/3/action/package_search?q=seismic+segy) |
| [NOPIMS (Geoscience Australia / NOPTA)](https://www.ga.gov.au/nopims) | All Australian offshore basins | 2D/3D/4D field (pre-stack), processed, velocities, navigation | ~3–4 PB *(est.)* | 🟢 open | CC BY 4.0 after release | COM BY ML | [portal](https://public.neats.nopta.gov.au/nopims) · [odata](https://services.neats.nopta.gov.au/odata/v1/public/nopims/survey/PublicNopimsSurvey) |
| [SARIG (South Australia)](https://catalog.sarig.sa.gov.au/dataset/mesac719) | South Australia — Cooper/Eromanga, Otway, Officer | 2D SEG-Y (>8,000 lines, >150,000 line-km), 3D, field data | ~1 PB+ *(est.)* | 🟢 open | Free, SA Crown / CC-BY-style terms | COM BY ML | [ckan-api](https://catalog.sarig.sa.gov.au/api/3/action/package_search?q=seismic+segy) · [basin-in-a-box (Otway)](https://catalog.sarig.sa.gov.au/dataset/mesac29507) |
| [WAPIMS (Western Australia DEMIRS)](https://wapims.dmp.wa.gov.au/wapims) | WA onshore and state waters — Carnarvon, Perth, Canning | processed seismic, navigation, scanned sections | ~100s of TB *(est.)* | 🟢 open | Free, WA Government terms | COM? | individual items online; basin packages so large you mail in a hard drive |
| [ANP BDEP / REATE (Brazil)](https://www.gov.br/anp/pt-br/assuntos/exploracao-e-producao-de-oleo-e-gas/dados-tecnicos) | Brazilian basins — Santos, Campos, Equatorial Margin | 2D/3D field and processed, some pre-stack | ~5–7 PB total; 100 TB pre-stack + 37 TB post-stack publicly offered | 🟡 academic | Public data free for universities; fee for industry delivery | **NC** BY | portal ordering; delivery on media/SFTP |
| [ANH EPIS / BIP (Colombia)](https://www.anh.gov.co) | Colombia — Llanos, Magdalena, Caribbean offshore | 2D (~150,000 km), 3D (~30,000 km²), pre-stack after confidentiality | ~1.5 PB *(est.)* | 🟡 academic | Free for academia; fee for industry | **NC** BY | order/download from EPIS |
| [GEUS Subsurface Data Portal (Denmark)](https://data.geus.dk/geusmap/?mapname=oil_and_gas&lang=en) | Denmark, Danish North Sea, Greenland | 2D/3D processed seismic | ~10s of TB (~1,400 surveys) *(est.)* | 🟢 open | Free download; handling fee for field data | COM? | [postgrest-api](https://data.geus.dk/sambaweb/processing?id=eq.1961) · [azure-blob](https://geusdata.blob.core.windows.net/geusdata/seismic/3D/AG9801.zip) · [wfs-api](https://data.geus.dk/geusmap/ows/25832.jsp?mapname=oil_and_gas&service=WFS&version=1.0.0&request=GetFeature&typename=seismic_3d_processings) |
| [UK National Data Repository (NSTA)](https://ndr.nstauthority.co.uk/) | UK Continental Shelf | 2D/3D post-stack SEG-Y, pre-stack (mandatory upload since 2018), navigation | >600 TB confirmed 2023; ~1 PB quoted 2024–25 | 🟡 free acct | Open Government Licence after the release period | COM BY ML | [arcgis-hub](https://opendata-nstauthority.hub.arcgis.com/) |
| [Ireland PAD / GSI petroleum seismic](https://isde.ie/geonetwork/) | Irish offshore — Porcupine, Rockall, Celtic Sea | 2D (~400,000 km), 44 3D surveys, SEG-Y | ~100s of TB *(est.)* | 🟡 request | Free (metadata CC BY 4.0); SEG-Y free on request | COM? BY | [csw-api](https://isde.ie/geonetwork/srv/eng/csw) |
| [India NDR (DGH)](https://www.dghindia.gov.in/) | Indian basins — KG, Mumbai Offshore | 2D/3D and pre-stack (post-2017) | ~8–10 PB (~2.5 M line-km 2D, ~500,000 km² 3D) *(est.)* | 🟡 academic | Free viewing; fee for download, waived for academia | COM? | web/FTP request; media delivery |
| [ViDEPI (Italy)](https://www.videpi.com/videpi/videpi.asp) | Italy — Adriatic, Po Valley, onshore | scanned 2D seismic sections (raster), some SEG-Y | ~85,000 km of 2D as images | 🟢 open | CC BY 4.0 | COM BY ML | direct HTTP |
| [Antarctic Seismic Data Library System (SDLS)](https://sdls.ogs.it/) | Antarctica (south of 60°S) | final-stack MCS 2D SEG-Y, navigation | ~5–15 TB (~300,000 line-km public) *(est.)* | 🟡 free acct | Antarctic Treaty mandate; free registration; non-commercial | **NC** BY | [US mirror](https://www.usap-dc.org/sdls) |
| [CNIH (Mexico — CNH)](https://portal.cnih.cnh.gob.mx/) | Mexican onshore and offshore — Perdido, Campeche, Sureste | 2D/3D including pre-stack | ~2–11 PB *(est.)* | 🟠 fee | Fee-based licence per km / km² | COM? | order form; media or cloud delivery |
| [NLOG (TNO — Geological Survey of the Netherlands)](https://www.nlog.nl/en/seismic-data) | Netherlands onshore and offshore | 2D/3D post-stack SEG-Y, navigation, some pre-stack | ~50–100 TB online *(est.)* | 🟢 open | Free, no charge | COM? | [datacenter](https://www.nlog.nl/datacenter/smc-3d-surveys) · [rest-list](https://www.nlog.nl/nlog-mapviewer/rest/smc/3d/surveys) · [arcgis-rest](https://www.nlog.nl/standalone/rest/services/nlog_gdn/gdw_ng_smc_grid_utm_v1/MapServer/0/query?f=json&where=1=1&outFields=*) |
| [Diskos NDR (Sodir / Norwegian Offshore Directorate)](https://www.sodir.no/en/diskos/seismic/) | Norwegian Continental Shelf | 2D/3D post-stack, velocities, navigation, pre-stack since 2012 | >22 PB stored; ~1 PB+ released | 🟡 request | Released data free to members; public portal charges media/handling only | COM? | Public portal (DecisionSpace 365 Enterprise Search) checkbox->cart order; members get direct download/API |
| [NZP&M Petroleum Exploration Data Pack](https://www.nzpam.govt.nz/maps-geoscience/petroleum-datapack) | All New Zealand basins | 2D (475,000 line-km), 3D (>24,000 km²), field + processed | multi-TB *(est.)* | 🟡 free acct | Open-file under the Crown Minerals Act | COM? | [catalogue](https://geodata.nzpam.govt.nz/) |
| [Kansas Geological Survey free 3D surveys](https://www.kgs.ku.edu/Geophysics/) | USA — Kansas (Hugoton, Cherokee Basin) | 3D SEG-Y volumes, 2D lines, 4D (CCUS monitoring) | <1 TB (dozens of GB) *(est.)* | 🔴 closed | Free | COM? | none — KGS publishes no downloadable seismic |
| [NAMSS — National Archive of Marine Seismic Surveys (USGS)](https://walrus.wr.usgs.gov/namss/) | US OCS — Gulf of Mexico, Atlantic, Pacific, Alaska | 2D stacks, 3D post-stack volumes, SEG-Y, SEG-P1 navigation | ~30–40 TB *(est.)* | 🟢 open | Public domain (US Government) | COM ML | [wms-getfeatureinfo](https://walrus.wr.usgs.gov/namss/wms) · [file-pattern](https://walrus.wr.usgs.gov/namss/data/{YEAR}/namss.{SURVEY}.mcs3d.airgun.zip) · [mirror](https://edx.netl.doe.gov/dataset/namss) |
| [PASA (Petroleum Agency South Africa)](https://www.pasa.co.za) | South African offshore and onshore — Orange Basin, Outeniqua | 2D (~300,000 line-km), 3D (>40,000 km²), field and processed | ~100s of TB *(est.)* | 🟡 academic | Fee for data packages; free indexes; academic tier available | COM? | order via data centre |

## Academic and research archives

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [Canadian National Marine Seismic Data Repository (NRCan/GSC)](https://open.canada.ca/data/en/dataset/e1fa0090-4b06-e476-5c71-e2326666a4d0) | Atlantic, Pacific and Arctic Canada | 50 years of scanned SCS/sparker/Huntec records (JPEG2000), some SEG-Y | >10 TB (mostly images) *(est.)* | 🟢 open | Open Government Licence — Canada | COM BY ML | [ftp](ftp://ftp.maps.canada.ca/pub/nrcan_rncan/Seismology_Sismologie/Seismic_Reflection-Imagerie_Sismique/) |
| [LITHOPROBE](https://open.canada.ca/data/en/dataset/959c15a2-a9ae-580a-b5ea-077140e219b7) | Canada — crustal transects | deep crustal 2D reflection (raw + processed SEG-Y), magnetotellurics | ~1–5 TB *(est.)* | 🟢 open | Open Government Licence — Canada | COM BY ML | GeoGratis FTP per line |
| [DEKORP (GFZ Data Services)](https://dataservices.gfz-potsdam.de/dekorp/) | Germany — deep crustal | deep crustal Vibroseis 2D (~4,700 km) + one 400 km² 3D | ~1–2 TB *(est.)* | 🟡 request | CC BY-NC 4.0 | **NC** BY | [EPOS-MSL mirror](https://acc.epos-msl.uu.nl) |
| [PANGAEA seismic collection](https://wiki.pangaea.de/wiki/Seismic) | Global — German research fleet (Sonne, Meteor, Polarstern) | 2D/3D MCS raw (SEG-D) and processed (SEG-Y), OBS/wide-angle, P-Cable 3D | >50 TB and growing *(est.)* | 🟢 open | Mostly CC BY 4.0 | COM BY ML | [viewer](https://marine-data.de) |
| [SeisDARE](https://essd.copernicus.org/articles/13/1053/2021/) | Iberia, Morocco, Texas | deep seismic sounding, wide-angle, high-res; SEG-Y/SEG-D | <1 TB (21 datasets) | 🟢 open | CC BY 4.0, DOI'd | COM BY ML | [repository](https://digital.csic.es/handle/10261/101879) |
| [BGS marine geophysical and seismic data](https://www.bgs.ac.uk/) | UK Continental Shelf, 1966– | airgun/sparker/boomer/pinger SCS, some MCS, scanned analog | ~5–20 TB (~350,000 line-km) *(est.)* | 🟡 request | NERC copyright; free for research on request | COM? | request SEG-Y via enquiries@bgs.ac.uk; WMS for index |
| [OGS SNAP (Seismic data Network Access Point)](https://snap.ogs.it/cache/index.jsp) | Mediterranean, Adriatic, Black Sea | MCS (rescued vintage + modern), multibeam | ~5–10 TB (~91,000–100,000 line-km) *(est.)* | 🟡 free acct | Free with registration | COM? | web portal, geographic search, SEG-Y download |
| [JAMSTEC Seismic Survey Database (OBS/MCS)](https://www.jamstec.go.jp/obsmcs_db/e/) | NW Pacific — Nankai Trough, Japan Trench, Izu-Bonin | MCS, OBS refraction/wide-angle | tens to 100+ TB *(est.)* | 🟡 request | Academic use via request form (DOI 10.17596/0002069) | COM? | request, then download or HDD |
| [EarthScope Assembled Datasets archive](https://ds.iris.edu/ds/nodes/dmc/data/assembled/) | Global — controlled-source and legacy experiments | controlled-source reflection/refraction, SEG-Y, PH5, legacy program archives | 12.775 TiB across 852 datasets | 🟢 open | Open | COM? | undocumented '?json' listing API on the assembled-data endpoint |
| [MGDS / Academic Seismic Portal (Lamont-Doherty)](https://www.marine-geo.org/) | Global — US academic fleet (Langseth, Ewing, Conrad, Vema) | raw and processed MCS, SCS, OBS/refraction, SEG-D/SEG-Y, navigation | 151.2 TB total; >80 TB seismic | 🟢 open | CC BY-NC-SA 3.0 | **NC** BY SA | [collections](https://www.marine-geo.org/collections/) |
| [NOAA Deep Sea Minerals (gs://noaa-deep-sea-minerals)](https://console.cloud.google.com/marketplace/product/noaa-public/noaa-mcm) | American Samoa EEZ — Pacific | sub-bottom profiler SEG-Y, XTF sidescan, Kongsberg multibeam, CARIS HIPS/SIPS projects, seafloor imagery | 24.9 TB total; 998 GiB of SEG-Y (15,903 files) | 🟢 open | CC0 1.0 (public domain dedication) | COM ML | [gcs](https://storage.googleapis.com/noaa-deep-sea-minerals) |
| [NOAA NCEI Marine Trackline / Seismic Reflection archive](https://www.ncei.noaa.gov/products/marine-seismic-reflection) | Global, 1939–present | SCS/MCS/refraction SEG-Y, scanned analog sections, MGD77T | ~10–30 TB digital *(est.)* | 🟢 open | US Government public domain | COM ML | [trackline](https://www.ncei.noaa.gov/products/marine-trackline-geophysical-data) |
| [USGS Coastal & Marine Geoscience Data System (CMGDS)](https://cmgds.marine.usgs.gov/) | US coasts and Great Lakes | chirp, boomer, sparker sub-bottom, high-res MCS SEG-Y | ~5–20 TB *(est.)* | 🟢 open | Public domain, DOI'd data releases | COM ML | HTTPS from data-release pages; ScienceBase API |

## ML-ready and labeled datasets

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [Thebe — Gigabyte Interpreted Seismic Dataset for Fault Recognition](https://doi.org/10.7910/DVN/YBYGBK) | Australia — Exmouth Plateau, Carnarvon Basin (NW Shelf) | 3D post-stack (NumPy), fault labels | ~50 GB (81 files; ~33.5 GB primary seismic+fault payload) | 🟢 open | CC BY 4.0 | COM BY ML | [dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YBYGBK) |
| [Hardpicks — hardrock first-break picking benchmark](https://github.com/mila-iqia/hardpicks) | Canada — Brunswick & Halfmile Lake (NB), Lalor (MB), Sudbury (ON) | 3D land reflection shot gathers, HDF5 (.hdf5.xz), first-break picks in trace headers | 23.79 GB compressed (4 surveys) | 🟢 open | CC BY 4.0 (Brunswick, Halfmile Lake); Open Government Licence - Canada (Lalor, Sudbury) | COM BY ML | [Brunswick 3D](https://d3sakqnghgsk6x.cloudfront.net/Brunswick_3D/Brunswick_orig_1500ms_V2.hdf5.xz) · [Halfmile Lake 3D](https://d3sakqnghgsk6x.cloudfront.net/Halfmile_3D/Halfmile3D_add_geom_sorted.hdf5.xz) · [Lalor 3D](https://d3sakqnghgsk6x.cloudfront.net/Lalor_3D/Lalor_raw_z_1500ms_norp_geom_v3.hdf5.xz) · [Sudbury 3D](https://d3sakqnghgsk6x.cloudfront.net/Sudbury_3D/preprocessed_Sudbury3D.hdf.xz) |
| [DiTing](https://doi.org/10.1016/j.eqs.2022.01.022) | China, 2013–2020 | 180 s 3-component at 50 Hz, P/S picks, first-motion polarity | >100 GB (2.73 M traces, 787k events) *(est.)* | 🟡 free acct | Open (registration on the Chinese platform) | COM? | download via data.earthquake.cn |
| [MultiSeismo (PNNL) — multimodal seismic dataset](https://huggingface.co/datasets/PNNL/MultiSeismo) | Global — 16k+ events, 2010-2023 | multi-station waveforms, parquet, intensity maps, population-exposure rasters, textual event descriptions (JSON) | 106.53 GB (104 parquet files) | 🟢 open | CC0 1.0 | COM ML | [HuggingFace repo](https://huggingface.co/datasets/PNNL/MultiSeismo) |
| [INSTANCE](https://data.ingv.it/en/dataset/471) | Italy | 120 s 3-component at 100 Hz, ~50k events + 130k noise | ~330 GB (1.2 M traces) | 🟢 open | CC BY 4.0 | COM BY ML | HTTP; also via SeisBench |
| [CREW (Curated Regional Earthquake Waveforms)](https://doi.org/10.5281/zenodo.11276286) | Global regional | 5-minute 3-component windows with both P and S labeled | 2.3 M waveforms | 🟢 open | CC BY | COM BY ML | Zenodo; also via SeisBench |
| [MLAAPDE](https://doi.org/10.5066/P9OJGE3G) | Global | 120 s 3-component broadband, P/Pn/Pg/S/Sn/Sg labels | TB-scale (>5.1 M recordings) | 🟢 open | US Government public domain | COM ML | ScienceBase; also via SeisBench |
| [PNW-ML (Pacific Northwest)](https://github.com/niyiyu/PNW-ML) | USA — Pacific Northwest | earthquakes, explosions, "exotic" surface events | tens of GB (~190k traces + 9.2k exotic) | 🟢 open | CC BY | COM BY ML | HTTP; also via SeisBench |
| [STEAD (STanford EArthquake Dataset)](https://github.com/smousavi05/STEAD) | Global | 60 s 3-component waveforms at 100 Hz, P/S picks, coda, noise | ~85 GB (1.2 M traces) | 🟢 open | CC BY 4.0 | COM BY ML | HTTP chunks (6 × ~15 GB); also via SeisBench |

## Synthetic models and benchmarks

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [FaultSeg3D synthetic fault training data (Xinming Wu)](https://github.com/xinwucwp/faultSeg) | Synthetic | 3D synthetic seismic, fault labels, 128^3 volumes | ~1.5 GB (computed; Google Drive folder, not measured) *(est.)* | 🟢 open | CC BY-NC 4.0 | **NC** BY | [google-drive](https://drive.google.com/drive/folders/1FcykAxpqiy2NpLP1icdatrrSQgLRXLP8) |
| [SubsurfaceGen field-scale velocity + wavefield dataset](https://huggingface.co/datasets/subsurfacegen/field-scale-dataset) | Synthetic — field-scale models spanning multiple geological settings | 3D velocity volumes (SOS-smoothed, 619 depth samples), 2D velocity slices, acoustic wavefields, multi-source shot-gather cubes, HDF5 | 11.92 TB (47,084 files) | 🟢 open | CC BY 4.0 | COM BY ML | [HuggingFace repo](https://huggingface.co/datasets/subsurfacegen/field-scale-dataset) · [preview variant (2.81 GB)](https://huggingface.co/datasets/subsurfacegen/field-scale-dataset-preview) |

## Earthquake / passive waveform archives

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [ISC Bulletin](https://www.isc.ac.uk/iscbulletin/) | Global, 1904–present | event bulletin/catalog, phase readings | ~90 GB (>4 M events, ~50 M readings) | 🟢 open | CC BY | COM BY ML | web search + ISC web services; mirror at isc-mirror.iris.washington.edu |
| [NIED MOWLAS (Hi-net, F-net, K-NET, KiK-net, S-net, DONET)](https://www.hinet.bosai.go.jp) | Japan | borehole short-period, broadband, strong motion, cabled seafloor | ~1 PB (estimate; unmeasured) *(est.)* | 🟡 free acct | Free registration; no redistribution; results-reporting obligation | COM? BY **no-redist** | web download + HinetPy; WIN32 format; 50 MB/request cap; no FDSN/S3 |
| [ORFEUS EIDA federation](https://www.orfeus-eu.org/data/eida/) | Europe | continuous waveforms from ~11 federated nodes | ~1 PB+ aggregate (estimate; unmeasured) *(est.)* | 🟢 open | Open (some restricted via EIDA tokens) | COM? | federated FDSN web services (eida-federator) + routing service |
| [GeoNet (GNS Science, New Zealand)](https://www.geonet.org.nz/data/access/aws) | New Zealand | seismic, strong motion, GNSS, tsunami gauges | >100 TB (~12 GB/day miniSEED) *(est.)* | 🟢 open | CC BY 3.0 NZ | COM BY ML | aws s3 ls s3://geonet-open-data --no-sign-request (ap-southeast-2); FDSNWS |
| [EarthScope Data Archive (formerly IRIS DMC)](https://www.earthscope.org/data/) | Global | continuous and event miniSEED, PH5 nodal, station metadata | >1 PB (published; FDSN DOI sizes are estimates - see SCHEMA) | 🟢 open | Open; cite the network DOI | COM? BY | [s3](https://registry.opendata.aws/) |
| [NCEDC (Northern California Earthquake Data Center)](https://ncedc.org) | Northern California | continuous/event waveforms, catalogs, GPS, strain | 184–190 TB | 🟢 open | Open | COM? | aws s3 ls s3://ncedc-pds --no-sign-request (us-east-2); FDSNWS |
| [SCEDC (Southern California Earthquake Data Center)](https://scedc.caltech.edu/data/cloud.html) | Southern California | continuous and event waveforms, catalog from 1932, phase picks, DAS | ~150 TB | 🟢 open | Open; cite doi:10.7909/C3WD3xH1 | COM? BY | aws s3 ls s3://scedc-pds --no-sign-request (us-west-2, daily updates); FDSNWS; STP |

## Distributed acoustic sensing (DAS)

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [Rutford Ice Stream DAS / DAS-N2N](https://zenodo.org/records/4778368) | Antarctica | 1 km cable, 1 kHz, 1 m channel spacing, Jan 2020 | hundreds of GB to TB *(est.)* | 🟢 open | CC BY | COM BY ML | [denoising benchmark](https://zenodo.org/records/7064405) |
| [PubDAS](https://pubdas.org) | Multiple — Alaska, Pennsylvania, California, Illinois, Spain | distributed acoustic sensing, 8 datasets (Table 1) | 76.6 TB (Table 1 holdings) | 🟡 free acct | Open (CC BY) | COM BY ML | [paper](https://www.osti.gov/pages/biblio/1957924) |
| [PoroTomo (Brady Hot Springs)](https://gdr.openei.org/submissions/980) | USA — Nevada geothermal field | surface + borehole DAS, nodal seismic, vibroseis source | 186.86 TB decimal (169.94 TiB); ~52 TB unique | 🟢 open | Open (DOE Geothermal Data Repository) | COM? | aws s3 ls s3://nrel-pds-porotomo/DAS/ --no-sign-request (224,205 objects) |
| [QuakeFlow DAS (PhaseNet-DAS training data)](https://huggingface.co/datasets/AI4EPS/quakeflow_das) | USA — Arcata/Ferndale CA, Monterey Bay (SeaFOAM submarine cable), Ridgecrest North CA | DAS event windows, HDF5, microstrain/s, event metadata (origin time, location, magnitude) | 674.31 GB (7,697 files) | 🟢 open | MIT | COM BY ML | [HuggingFace repo](https://huggingface.co/datasets/AI4EPS/quakeflow_das) |
| [Utah FORGE DAS](https://gdr.openei.org/submissions/1185) | USA — Utah (enhanced geothermal) | downhole microseismic DAS (2019, 2022, 2024), 12-s HDF5 files | multi-TB *(est.)* | 🟢 open | Open | COM? | HTTP + shell script; hosted off-GDR at Utah CHPC; also in PubDAS |

## Strong-motion databases

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [ESM — Engineering Strong Motion database](https://esm-db.eu) | Europe and the Mediterranean | processed accelerograms, flatfiles | 76,242 ground motions, 9,927 stations, 1,391 events | 🟡 free acct | CC BY (registration) | COM BY ML | web services at esm-db.eu/esmws; also in SeisBench as ESM25 |
| [CESMD (Center for Engineering Strong Motion Data)](https://www.strongmotioncenter.org) | USA and international | processed and raw strong motion, instrumented structures | tens of thousands of records, 2,000+ stations *(est.)* | 🟢 open | US Government public domain | COM ML | web (IQR/IDR), Virtual Data Center |
| [NGA-West2 (PEER)](https://ngawest2.berkeley.edu) | Global shallow-crustal | ~21, 300 3-component records, ~600 events, flatfile + time series | ~21,300 records | 🟠 fee | Registration; paid annual membership from 2 July 2026 | COM? | web only; 200 records per 2 weeks cap |

## Planetary and ocean-bottom

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [Apollo Passive Seismic Experiment (Moon)](https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_pse) | Moon — Apollo 11/12/14/15/16/17 landing sites | lunar seismometers 1969–1977; ~13, 000 catalogued events | tens of GB *(est.)* | 🟢 open | Public domain (NASA) | COM ML | PDS HTTP; also FDSN as network XA via EarthScope |
| [InSight SEIS (Mars)](https://pds-geosciences.wustl.edu/missions/insight/seis.htm) | Mars — Elysium Planitia | VBB + SP seismometer, 2018–2022; ~1, 300 catalogued marsquakes | hundreds of GB *(est.)* | 🟢 open | Public domain (NASA) | COM ML | PDS HTTP; also FDSN web services as network XB via EarthScope |
| [OOI Regional Cabled Array](https://oceanobservatories.org) | Cascadia margin / Axial Seamount | broadband and short-period OBS, hydrophones, pressure, 2014– | >100 TB across all streams *(est.)* | 🟢 open | Open (CC BY) | COM BY ML | FDSN web services (network OO); OOI raw data archive HTTP |

## Hubs, registries, and curated lists

| Dataset | Region | Type | Size | Access | License | Use | Get it |
|---|---|---|---|---|---|---|---|
| [AWS Registry of Open Data](https://registry.opendata.aws/) | Global | cloud-hosted dataset registry | n/a (registry) | 🟢 open | Per-dataset | COM? | aws s3 sync --no-sign-request per bucket |
| [OSDU Open Test Data](https://community.opengroup.org/osdu/platform/data-flow/data-loading/open-test-data) | Global | reference datasets for OSDU platform testing | ~1–2 TB *(est.)* | 🟢 open | Apache-2.0 (repo); data per source licence | COM? | git / HTTP |
| [SEG Wiki — Open Data](https://wiki.seg.org/wiki/Open_data) | Global | curated index of open seismic datasets | n/a (index) | 🟢 open | Wiki content CC BY-SA; datasets keep their own terms | COM? | n/a |
| [SeisBench](https://seisbench.readthedocs.io/en/stable/pages/documentation/data/waveform_datasets.html) | Global | Python library wrapping ~45 waveform dataset classes + pretrained models | n/a (loader; datasets range GB–TB) | 🟢 open | GPL-3.0 (library); datasets keep their own licences | COM? | [github](https://github.com/seisbench/seisbench) |
| [TerraNubis (dGB Earth Sciences)](https://terranubis.com) | Global | packaged OpendTect projects: seismic + wells + interpretation | ~1 TB across free datasets *(est.)* | 🟡 free acct | Per-dataset (F3 and Penobscot are free) | COM? | web download of project bundles |
| [CO2 DataShare](https://co2datashare.org) | Norway and international CCS sites | CCS reference datasets — 4D seismic, wells, models | ~1 TB *(est.)* | 🟡 free acct | Open, per-dataset licences | COM? | web download |

## Contributing

Add or correct an entry in [`catalog/datasets.yaml`](catalog/datasets.yaml) and run `python scripts/build_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).
