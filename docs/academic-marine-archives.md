# Academic / Government Marine & Crustal Seismic Archives

Legend: **V** = URL verified live during research; "est." = estimate from published line-km / survey counts (treat as ±3x).

## North America

| # | Archive | Host / institution | Region | Data type | Approx. size & count | Access / license | URL | Bulk download | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **NAMSS – National Archive of Marine Seismic Surveys** | USGS PCMSC (+ BOEM) | US OCS: GoM, Atlantic, Pacific, Alaska | Industry 2D/3D MCS (SEG-Y, mostly post-stack; some field), nav | **567 2D surveys / 2.36 M line-km + 182 3D surveys** (Jan 2019, likely >800 now); 2024 paper: ~**10 TB** public release tranche; total holdings tens of TB | Free, public domain (US Gov); no registration | https://walrus.wr.usgs.gov/namss/ | Per-survey ZIP over HTTPS from survey pages (`/namss/survey/<id>/dataset/`); no API/S3; scriptable with wget once IDs known | Largest open marine 3D collection in the US; EDX mirror at edx.netl.doe.gov/dataset/namss |
| 2 | **MGDS / Academic Seismic Portal (ASP at LDEO, formerly + UTIG)** | Lamont-Doherty, Columbia (IEDA/NSF) | Global (US academic fleet: Langseth, Ewing, Conrad, Vema, UTIG cruises) | Raw & processed MCS, SCS, OBS/refraction, SEG-D/SEG-Y, nav | **MGDS total 151.2 TB, 2.6 M files, 3,905 programs** (V); ASP: >80 TB seismic from >500 programs; UTIG merge added >340 cruises; ~2,755 datasets | CC BY-NC-SA 3.0; open, no login (V) | https://www.marine-geo.org/ (V); https://www.marine-geo.org/collections/ | Direct HTTPS per file (`/tools/files/<id>`), OGC web services, DataONE mirror, GeoMapApp; per-cruise tarballs; no S3 | Since 2020 the single US academic seismic archive; also holds SDLS US branch data |
| 3 | **IEDA (EarthChem + MGDS)** | Columbia/LDEO | Global | Umbrella for MGDS | See #2 | CC BY-NC-SA | https://www.iedadata.org | via MGDS | Not a separate seismic store |
| 4 | **IODP/ODP/DSDP Site Survey Data Bank (SSDB)** | IODP SSO | Global drilling sites | SCS/MCS SEG-Y, OBS, images supporting drilling proposals | Tens of TB historically (est.); **now shut down as public access point** (V) | Was free with basic account | https://ssdb.iodp.org/ (shutdown notice) | Data migrating to **Zenodo IODP community** (https://zenodo.org/communities/iodp) and https://iodp.tamu.edu/database/zenodo.html (V); older cruise data also in MGDS | Legacy ODP/DSDP site-survey seismic partially in NCEI and MGDS |
| 5 | **NOAA NCEI Marine Trackline Geophysical Data (GEODAS) + Marine Seismic Reflection archive** | NOAA NCEI Boulder | Global, 1939–present | SCS/MCS/refraction (SEG-Y + scanned analog sections), bathy, mag, grav (MGD77T) | Thousands of cruises; est. **10–30 TB digital seismic + scans**; migrating to cloud | US Gov public domain; no login (V) | https://www.ncei.noaa.gov/products/marine-seismic-reflection (V); https://www.ncei.noaa.gov/products/marine-trackline-geophysical-data (V) | Trackline Geophysical Data Viewer (HTTPS zips); legacy FTP migrating to NOAA Open Data Dissemination (AWS/GCP/Azure); email for offline sets | Only "some lines" online; much still request-based |
| 6 | **USGS CMGDS (Coastal & Marine Geoscience Data System)** | USGS CMHRP | US coasts, Great Lakes | Chirp / boomer / sparker sub-bottom, high-res MCS (SEG-Y), nav | Hundreds of field activities; est. **5–20 TB** | Public domain, DOI'd data releases | https://cmgds.marine.usgs.gov/ | HTTPS from data-release pages; ScienceBase API (sciencebase.gov) | Largest US open chirp/sub-bottom collection |
| 7 | **Canadian National Marine Seismic Data Repository / Expedition Database** | NRCan / GSC Atlantic & Pacific | Atlantic, Pacific, Arctic Canada | 50 yr of scanned SCS/sparker/Huntec/sounder records (JPEG2000) + nav; some SEG-Y | est. **>10 TB** (mostly images) | Open Government Licence – Canada (V) | https://open.canada.ca/data/en/dataset/e1fa0090-4b06-e476-5c71-e2326666a4d0 (V) | FTP/HTTPS: ftp.maps.canada.ca/pub/nrcan_rncan/Seismology_Sismologie/Seismic_Reflection-Imagerie_Sismique/ ; ESRI REST, WMS, KML | Mostly images, not SEG-Y |
| 8 | **LITHOPROBE archive** | NRCan / GSC | Canada (crustal transects) | Deep crustal 2D reflection (raw + processed SEG-Y), MT | tens of transects; est. **1–5 TB** | Open Government Licence – Canada (V) | https://open.canada.ca/data/en/dataset/959c15a2-a9ae-580a-b5ea-077140e219b7 (one line of many) | GeoGratis FTP per line | Search open.canada.ca for "Lithoprobe" to enumerate lines |
| 9 | **COCORP** | Cornell Univ. | USA (continental) | Deep crustal Vibroseis reflection 1975–2000s | >11,000 line-km; est. <1 TB | Academic, on request | Partly at IRIS DMC assembled datasets | Request / IRIS | Legacy tapes |
| 10 | **EarthScope (IRIS) DMC – PASSCAL / USArray Flexible Array assembled & active-source data** | EarthScope Consortium (NSF SAGE) | Global, mainly USA | Controlled-source refraction/reflection, onshore–offshore OBS, in **PH5** & SEG-Y | Whole DMC >1 PB; active-source growth >5 TB/yr; hundreds of experiments | Open, free, no login for most | https://ds.iris.edu/data/sources.htm (V); https://ds.iris.edu/ds/nodes/dmc/ | FDSN web services (dataselect), PH5 web services (ph5ws) delivering SEG-Y/miniSEED; ROVER; cloud migration underway | Best source for crustal-scale controlled-source experiments in N. America |
| 11 | **Mexico CNIH (CNH National Data Repository)** | Comisión Nacional de Hidrocarburos | Mexican onshore/offshore | 2D/3D industry seismic | **>11 PB** total repository | Licensed/paid; registration | https://portal.cnih.cnh.gob.mx/ | Data-room / portal delivery | Mostly commercial; included for completeness |

## South America

| # | Archive | Host | Region | Data type | Size & count | Access | URL | Bulk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 12 | **ANP BDEP / eBID (REATE onshore public data)** | ANP Brazil | Brazil basins | 2D/3D field & processed | BDEP total **≈7 PB**; public offering: **100 TB pre-stack + 37 TB offshore post-stack** | Free for public onshore data (REATE); registration | https://ebid.anp.gov.br/ | Portal ordering; on-demand disks | |

## Europe

| # | Archive | Host | Region | Data type | Size & count | Access | URL | Bulk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 13 | **BGS Marine geophysical & seismic data (NGDC / MEDIN DAC)** | British Geological Survey | UK Continental Shelf, 1966– | Airgun/sparker/boomer/pinger SCS, some MCS; scanned analog | **≈350,000 line-km** (V); est. 5–20 TB incl. scans | NERC copyright; free for research on request | https://www.data.gov.uk/dataset/cb7c667b-25e2-401c-8260-ac8168946235 (V); GeoIndex Offshore | Request SEG-Y via enquiries@bgs.ac.uk; WMS; no bulk API | BIRPS deep reflection data also held by BGS (request) |
| 14 | **NSTA National Data Repository (UK offshore)** | North Sea Transition Authority | UKCS | Released 2D/3D industry seismic (post/pre-stack) | Hundreds of TB → PB scale (est.); 2016 OGA release 42,000 km 2D | Open Government Licence after release; free registration | https://ndr.nstauthority.co.uk/ | Portal download (large orders staged) | Successor to CDA UKOilandGasData |
| 15 | **UKOGL** | UK Onshore Geophysical Library | UK onshore | 2D/3D field & processed SEG-Y, scans | **>87,000 km 2D, >2,900 km² 3D** (V) | Images free; SEG-Y licensed/paid (V) | https://ukogl.org.uk/archives/ (V) | Interactive map, shapefiles; SEG-Y via licence | Also hosts BGS & Coal Authority post-stack free |
| 16 | **GEUS Subsurface Archive / Subsurface Data Portal (ex-Frisbee)** | GEUS Denmark | Denmark, North Sea, Greenland | 2D/3D processed seismic, wells | **~1,400 2D/3D surveys, ~2,000 wells** (V); est. tens of TB | Free download since Oct 2023; field data handling fee (V) | https://data.geus.dk/geusmap/?mapname=oil_and_gas&lang=en (V) | Map-based download; no API | Frisbee webshop discontinued 2023 |
| 17 | **Diskos NDR (Sodir/NPD)** | Norwegian Offshore Directorate | Norwegian Continental Shelf | 2D/3D post-stack, velocity, nav; pre-stack since 2012 | **>22 PB stored (1 Jan 2026); >1,300 public 3D surveys; >24,000 public post-stack cubes; 30,000 released datasets** | Released data free to members; non-members order via Diskos Public Portal (media/handling fee) | https://www.sodir.no/en/diskos/seismic/ | Portal order; members: direct download/API (Halliburton NDR 2.0, multi-cloud) | Largest government seismic repository in Europe |
| 18 | **NLOG / DINO (TNO)** | TNO Geological Survey NL | Netherlands on/offshore | 2D lines (~5,920 NAM lines) & **>135 3D surveys / ~99,900 km²**; pre-stack on request | est. 50–200 TB | Free, no charge (V) | https://www.nlog.nl/en/seismic-data (V) | Interactive map / data centre downloads; service-desk requests | One of the most open European national archives |
| 19 | **Ifremer SISMER** | Ifremer (French fleet) | Global, 1969– | MCS (SEG-D/SEG-Y), SCS, OBS, sub-bottom | Hundreds of cruises; est. >100 TB | Open after embargo; contact sismer@ifremer.fr (V) | https://data.ifremer.fr/en/data-management/Themes/Geophysics/Seismics (V); SEANOE DOIs | Request; SEANOE DOI direct HTTPS for published sets | |
| 20 | **OGS SNAP – Seismic data Network Access Point** | OGS Trieste, Italy | Mediterranean, Black Sea, Adriatic | MCS (vintage rescued + modern), multibeam | **≈91,000–100,000 km seismic lines; 351,000 km² multibeam** (V) | Free; registration; feeds EMODnet/SeaDataNet | https://snap.ogs.it/cache/index.jsp (V) | Web portal (geographic search, SEG-Y download) | Hosts SDLS too |
| 21 | **PANGAEA seismic (GEOMAR, AWI, MARUM, BGR, Uni Kiel/Hamburg/Bremen)** | PANGAEA (AWI/MARUM) | Global, German fleet (Sonne, Meteor, Maria S. Merian, Poseidon, Polarstern) | 2D/3D MCS raw (SEG-D) & processed (SEG-Y), OBS/wide-angle, P-Cable 3D | Hundreds of DOI'd datasets since 2020; per-cruise 0.1–2 TB; est. **>50 TB** | CC BY 4.0 mostly; open, no login (V) | https://wiki.pangaea.de/wiki/Seismic (V); viewer https://marine-data.de | Direct HTTPS per DOI; pangaeapy API; no bulk mirror | Fastest growing academic marine archive in Europe |
| 22 | **BGR marine seismic** | Federal Inst. for Geosciences, Hannover | Global (BGR cruises), N. Sea, Antarctic, polar | Industry-grade MCS, high-res MCS | Hundreds of thousands of line-km (est.) | On request; moving to PANGAEA | https://www.bgr.bund.de (V) | Request; PANGAEA DOIs going forward | |
| 23 | **DEKORP (GFZ Data Services)** | GFZ Potsdam | Germany | Deep crustal Vibroseis 2D + one 3D | **~40 lines / ~4,700 km + 400 km² 3D** (V); est. 1–2 TB | CC BY-NC 4.0; request form (V) | https://dataservices.gfz-potsdam.de/dekorp/ (V) | Per-profile request; EPOS-MSL mirror https://acc.epos-msl.uu.nl (V) | |
| 24 | **SeisDARE** | CSIC (DIGITAL.CSIC), Spain | Iberia, Morocco, Texas | Deep seismic sounding + high-res, wide-angle; SEG-Y/SEG-D | **21 datasets** (2021); <1 TB | CC BY 4.0, DOIs (V) | https://digital.csic.es/handle/10261/101879 | HTTPS per DOI | Ties to ESCI, IAM, ILIHA legacy programs; paper: https://essd.copernicus.org/articles/13/1053/2021/ |
| 25 | **ECORS / BIRPS / NFP-20 / FIRE-HIRE legacy** | France (CNRS/IFP), UK (BGS), Switzerland, Finland (GTK) | Europe | Deep crustal reflection | Each ≤1 TB; scattered | On request | via institutions | Request | No single portal |
| 26 | **EPOS** | EPOS ERIC | Europe | Mostly passive seismology; MSL hosts DEKORP mirror | — | Open | https://www.epos-eu.org/ | API | Pointer only |
| 27 | **Ireland PAD / GSI / INFOMAR** | DECC Petroleum Affairs Division; Marine Institute | Irish offshore | 44 3D surveys (1982–2014) + 2D 1965–2015; SEG-Y via PAD; INFOMAR sub-bottom | est. 10–50 TB | CC BY 4.0 for metadata; SEG-Y free on request | https://data.gov.ie/dataset/3d-seismic-survey | Shapefiles direct; data via PAD data room | |
| 28 | **Spain IGME SIGEOF / Portugal DGEG-ENMC** | IGME-CSIC; Portugal DGEG | Iberian margins | Marine geophysics, legacy MCS | Small (est. <5 TB) | Request | https://info.igme.es/sigeof/ | Request | Seismic-oceanography Gulf of Cadiz set on Zenodo |

## Africa

| # | Archive | Host | Region | Data type | Size & count | Access | URL | Bulk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 29 | **Petroleum Agency SA (PASA) GeoPortal** | PASA, Cape Town | South African offshore/onshore | 2D/3D field & processed | **>300,000 line-km 2D, >40,000 km² 3D** + 9,800 km onshore; est. hundreds of TB | Registration; data room / paid (academic tier) (V) | https://www.petroleumagencysa.com/viewing-our-technical-data/ (V); geoportal.petroleumagencysa.com | Shapefiles free; data ordered | |

## Asia

| # | Archive | Host | Region | Data type | Size & count | Access | URL | Bulk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 30 | **JAMSTEC Seismic Survey Database (OBS/MCS)** | JAMSTEC | NW Pacific, Nankai, Japan Trench, Izu-Bonin | MCS (Kairei KR, Kaiyo KY, Yokosuka), OBS refraction/wide-angle | ~200+ MCS cruises (est.); tens–100+ TB (est.) | Academic use via request form; DOI 10.17596/0002069 (V) | https://www.jamstec.go.jp/obsmcs_db/e/ (V) | Request → download/HDD | Best OBS crustal dataset in Asia |
| 31 | **India NDR (DGH)** | Directorate General of Hydrocarbons | Indian basins | 2D/3D seismic, wells | PB-scale (est.) | Paid/licensed; registration | https://ndr.dghindia.gov.in/ | Portal | |
| 32 | **KIGAM / KIOST (Korea), SINOPROBE / CGS (China), Taiwan Ocean Data Bank** | national | — | MCS, deep reflection | Unknown | Restricted | — | — | No public bulk archives found |

## Oceania

| # | Archive | Host | Region | Data type | Size & count | Access | URL | Bulk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 33 | **Geoscience Australia – Australian National Offshore Seismic Survey Data Collection (via NOPIMS)** | GA / NOPTA | Australian offshore | 2D/3D field (SEG-D), processed, velocity, nav, scans | "one of the world's largest petroleum data collections" — **PB-scale** (est. 2–5 PB); thousands of surveys | **CC BY 4.0** (V) after release; free registration | https://ecat.ga.gov.au/geonetwork/srv/api/records/224db798-72f1-43b5-b2a3-61c0e7228d2e (V); https://www.ga.gov.au/nopims (V) | NOPIMS portal download; large orders via GA client services; no public S3 bucket found | Release rules changed 28 Nov 2025 (ministerial approval) |
| 34 | **NZP&M Petroleum Data Pack + Geodata Catalogue / GNS NZASSDR** | NZ Petroleum & Minerals; GNS Science | NZ basins | Open-file 2D/3D; NZASSDR academic active-source | **475,000 line-km 2D + >24,000 km² 3D** (V) | Free (Geodata catalogue) / NZ$250 HDD pack; CC BY | https://www.nzpam.govt.nz/maps-geoscience/petroleum-datapack (V) | Online Permitting System / hard drive | NIWA holds sub-bottom/TOPAS |

## Polar

| # | Archive | Host | Region | Data type | Size & count | Access | URL | Bulk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 35 | **Antarctic SDLS (SCAR)** | OGS Trieste (branches at USGS, LDEO, AWI, etc.) | South of 60°S | Final-stack MCS SEG-Y, nav | **>350,000 km acquired; 228,000–300,000 km public** (V); est. 5–15 TB | Antarctic Treaty mandate; free registration; unrestricted 8 yr after collection; non-commercial (V) | https://sdls.ogs.it/cache/index.jsp (V); https://www.usap-dc.org/sdls (V) | Portal download after login; GeoMapApp | |
| 36 | **AWI Arctic/Antarctic seismic (PANGAEA + marine-data.de)** | Alfred Wegener Institute | Arctic Ocean, Southern Ocean, Polarstern 1985– | MCS, OBS, 3D | Dozens of profile DOIs; est. 5–10 TB | CC BY 4.0 (V) | https://zenodo.org/records/15489541 (V); marine-data.de | HTTPS per PANGAEA DOI | MetaSeis project |
| 37 | **USGS/NOAA Arctic legacy (Chukchi, Beaufort lines)** | USGS/NCEI | Alaska Arctic | MCS | in NAMSS / NCEI | Public domain | see #1, #5 | HTTPS | |

## Global / cross-cutting

| # | Archive | Host | Type | Size | Access | URL |
|---|---|---|---|---|---|---|
| 38 | **Zenodo (IODP community, misc. OBS/MCS)** | CERN | Site-survey & published SEG-Y | GB–TB per record; 50 GB/record cap | CC BY | https://zenodo.org/communities/iodp |
| 39 | **SeaDataNet / EMODnet Geology** | EU | Metadata + links to SNAP/BGS/GEUS/Ifremer | Index only | Open | https://www.seadatanet.org |
| 40 | **re3data listings** (ASP-UTIG r3d100010631, ASP-LDEO r3d100010644, SSDB r3d100011543, BDEP r3d100010989) | re3data | Registry | — | — | https://www.re3data.org |

## Largest archives ranked by (estimated) size

1. Diskos NDR (Norway) – **>22 PB** (published, 1 Jan 2026)
2. Mexico CNIH – **>11 PB** (published)
3. Brazil ANP BDEP – **≈7 PB** (published; 137 TB public)
4. Geoscience Australia / NOPIMS – **PB-scale** (est. 2–5 PB)
5. UK NSTA NDR – **hundreds of TB–PB** (est.)
6. EarthScope/IRIS DMC (all seismology; active-source subset ~tens of TB) – **>1 PB** total
7. South Africa PASA – **hundreds of TB** (est.)
8. NZP&M open-file – **~100–300 TB** (est.)
9. **MGDS / Academic Seismic Portal – 151 TB total, >80 TB seismic** (published) — largest *purely academic* marine seismic archive
10. NLOG/TNO – **50–200 TB** (est.)
11. Ifremer SISMER – **>100 TB** (est.)
12. JAMSTEC OBS/MCS – **tens–100+ TB** (est.)
13. PANGAEA German marine seismic – **>50 TB** (est., growing)
14. USGS NAMSS – **tens of TB** (10 TB in the 2024 public release; 749+ surveys)
15. GEUS – **tens of TB** (1,400 surveys)
16. NOAA NCEI seismic reflection – **10–30 TB** (est.)
17. BGS marine – **5–20 TB**
18. USGS CMGDS chirp/sub-bottom – **5–20 TB** (est.)
19. SDLS Antarctica – **5–15 TB** (est.)
20. NRCan scanned repository – **>10 TB** (images)
21. OGS SNAP – **~5–10 TB**
22. AWI polar – **5–10 TB**
23. LITHOPROBE – **1–5 TB**; DEKORP – **1–2 TB**; SeisDARE, COCORP, BIRPS, ECORS – **<1 TB each**

## Caveats

- Only MGDS (151.2 TB), Diskos (22 PB), CNIH (11 PB), BDEP (7 PB) and NAMSS (10 TB release) publish an actual byte total; everything else is estimated from line-km / survey counts.
- True bulk-download (S3 `aws s3 sync`) exists only for the SEG/AWS open datasets (Poseidon, Volve, etc.). Government archives (NAMSS, NOPIMS, GEUS, NLOG, SDLS, SNAP) are per-survey HTTPS ZIP via web portals; MGDS has per-file HTTPS + OGC services; IRIS has FDSN/PH5 web services (fully scriptable); NRCan/LITHOPROBE and legacy NCEI use FTP.
- IODP SSDB is closed as a public access point; site-survey seismic is moving to Zenodo and MGDS.
- The Academic Seismic Portal at UTIG no longer exists separately (merged into LDEO/MGDS on 1 June 2020).
- Geological Survey of Norway (NGU) has no large seismic archive; Norway's data is Diskos.
