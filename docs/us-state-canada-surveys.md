# US State Geological Surveys & Canadian Provincial Agencies — Public Seismic Data

Verification pass: **2026-08-24**. Method: direct HTTP fetch of agency pages and directory listings,
CKAN/REST APIs (DOE NETL EDX, DOE GDR, ArcGIS FeatureServer, USGS ScienceBase, Zenodo), NAMSS WMS
`GetFeatureInfo`, ZIP central-directory parsing by HTTP range request, and Internet Archive CDX history.
**No URL in this document is invented** — every URL under a VERIFIED row was actually retrieved.

Status legend: **VERIFIED** = fetched in this pass · **UNVERIFIED** = blocked (403/timeout) or secondary only.

Access legend: `free-dl` = anonymous direct download · `free-reg` = free with registration ·
`fee` = paid · `request` = written request · `onsite` = physical visit only · `none` = nothing released.

---

## 0. Headline finding — KANSAS (settled)

> **Kansas publishes NO free, downloadable seismic reflection data. There is no working public SEG-Y
> path at the Kansas Geological Survey. The prior verification pass was correct.**

The widely repeated claim that the **Dickman**, **Wellington** and **Cutter** 3D volumes are free downloads
from KGS is **not supported by any working URL**. Evidence gathered this pass:

| Check | URL | Result |
|---|---|---|
| KGS Geophysics section index | `https://www.kgs.ku.edu/Geophysics/` | VERIFIED — subdirs `4Dseismic/ CSTS/ Earthquakes/ Equip/ OFR/ Reports/ Reports2/ gifs/` and HTML pages only. **No data files.** |
| KGS 4-D seismic project dir | `https://www.kgs.ku.edu/Geophysics/4Dseismic/` | VERIFIED — site-visit reports, processing updates, photo galleries, AAPG abstracts. **All PDF/HTML. No SEG-Y.** |
| Full 3-level crawl of `/Geophysics/` | (server has directory listings enabled) | VERIFIED — the **only** binary archives in the whole tree are `EavesDemoData/england.zip` (175 KB) and `tutorial.zip` (457 KB): a **1993 DOS demo of the EAVESDROPPER shallow-seismic processing package**, not reservoir data. |
| KGS petroleum database | `https://www.kgs.ku.edu/PRS/petroDB.html` | VERIFIED — production, well master list, wireline logs (LAS/TIF), tops, DSTs, cores, brine, UIC. **Seismic is not among the datasets.** |
| KGS `/Datasale/` (found via robots.txt) | `https://www.kgs.ku.edu/Datasale/` | VERIFIED — only `Maps/`, `catalog/`, `suprpump.html`. |
| KGS `robots.txt` hidden-path check | `https://www.kgs.ku.edu/robots.txt` | VERIFIED — 40 disallowed paths inspected; none is a seismic data store. |
| KGS CarbonSAFE / IMSCS Hub | `https://www.kgs.ku.edu/PRS/IMSCSH/` | VERIFIED — well logs (PDF), core photos, drilling/completion reports. **No seismic products.** |
| KGS Ozark project (Wellington + Cutter) | `https://www.kgs.ku.edu/PRS/Ozark/` | VERIFIED — the page states interpretation used **"donated regional 3D seismic"**, i.e. industry-donated under licence. `Wellington/`, `Dickman/`, `Seismic/` sibling paths all **404**. |
| DOE NETL EDX — dataset resources | `https://edx.netl.doe.gov/api/3/action/package_show?id=4-d-high-resolution-seismic-reflection-monitoring-of-miscible-co2-injected-into-a-carbonate-reser1` | VERIFIED — the whole "4-D High-Resolution Seismic Reflection Monitoring of Miscible CO2…" dataset is **one 198 KB PDF** (`NT15414_2006.pdf`). Licence `Other-Open`. **No SEG-Y.** |
| DOE NETL EDX — Kansas sweep | `https://edx.netl.doe.gov/api/3/action/package_search?q=Kansas%20seismic&rows=50` | VERIFIED — ~11 Kansas records; **every resource format is PDF or HTML**. |
| Zenodo | `https://zenodo.org/api/records?q=kansas%20seismic%20segy` / `?q=Dickman%20seismic` | VERIFIED — no Kansas/Dickman seismic records. |
| **Internet Archive CDX, entire history of `kgs.ku.edu`** | `http://web.archive.org/cdx/search/cdx?url=kgs.ku.edu*&filter=urlkey:.*seg.?y.*` | VERIFIED — **the only SEG-Y-matching URL ever archived is `/software/surfseis/segy2fpt.exe`**, a converter for KGS's SurfSeis MASW software. A `*.sgy` filter returns **zero** rows. No SEG-Y data file has ever been hosted on the KGS domain. |
| Kansas Corporation Commission | `https://www.kcc.ks.gov/oil-gas` | VERIFIED — the only occurrence of "seismic" is **"Induced Seismicity"**. Kansas does not collect seismic reflection surveys. |

**Interpretation.** Kansas has no statutory seismic-filing regime, so the state never accumulated an
archive to release. KGS work on Dickman / Wellington / Cutter used **industry-donated, licence-restricted**
3D volumes; only interpretations and reports were published. Copies circulating in the ML literature are
best treated as **request-only / collaboration-only**. **Do not plan around a Kansas download.**

*Distinct and genuinely public:* KGS **induced-seismicity earthquake waveforms** (passive seismology, not
reflection) are distributed through EarthScope/IRIS, not by KGS.

---

## 0b. Cross-cutting channels that matter more than most state surveys

**The single most important structural finding of this pass:** almost all genuinely free US seismic is
published **federally** — by USGS, DOE NETL EDX, or the DOE Geothermal Data Repository — *not* by state
geological surveys. Several state surveys are the *authors* of these datasets but host nothing themselves.

| Channel | URL | Holdings | Access / licence |
|---|---|---|---|
| **USGS NAMSS** — National Archive of Marine Seismic Surveys | `https://walrus.wr.usgs.gov/namss/` · about `.../about/` · DOI `10.5066/F7930R7P` | **972 3D surveys, 697,446 km²**; **610 2D surveys, 35,690 tracklines, 1,912,967 line-km**. Mostly SEG-Y + shotpoint nav, TIFF side-labels, processing reports | `free-dl`, **public domain**, "no restrictions on usage or publication" |
| **DOE NETL EDX** | `https://edx.netl.doe.gov/` · API `.../api/3/action/package_search?q=<terms>&rows=25` | State-survey CCS deliverables: Kevin Dome (MT), IBDP + FutureGen (IL), ND CarbonSAFE, South Georgia Rift (SC/GA) | `free-dl` anonymous — verified `200 OK` + `content-disposition: attachment` with no cookie |
| **DOE Geothermal Data Repository (GDR)** | `https://gdr.openei.org/` | Utah FORGE (~127 GB SEG-Y), Soda Lake NV (171 GB SEG-Y), other NV/OR geothermal | `free-dl`, **CC BY 4.0**; some also on anonymous S3 |
| **USGS ScienceBase** — Mid-Continent Vibroseis Archive | `https://www.sciencebase.gov/catalog/item/57da9b09e4b090824ffc308f` | ~280 km 2D CDP, raw + stack SEG-Y, SE Missouri / NE Arkansas / NW Tennessee | `free-dl`, public domain |

### NGDS / geothermaldata.org — DEAD, do not chase old links (VERIFIED)

The AASG **National Geothermal Data System** portal at `geothermaldata.org`, through which many state
surveys published in the 2010s, **no longer exists**. The domain lapsed and was re-registered; it now
serves an unrelated personal portfolio site with a TLS certificate for unrelated domains. Every
`geothermaldata.org` citation is dead, as is `www.usgin.org` (does not resolve). Successor: **GDR** above.

**Caveat on EDX searching:** a 25-query sweep of the EDX CKAN API found only Kevin Dome and ND CarbonSAFE
via the `format` field. The IBDP, FutureGen and South Georgia Rift SEG-Y are **buried inside ZIP/tar.bz2
archives** and invisible to format search. They were found only by listing ZIP central directories over
HTTP range requests. Assume format-facet searches under-report.

---

## 1. United States

### 1.1 Summary — everything genuinely obtainable

| State | Source | What | Format | Volume | Access | Licence | Status |
|---|---|---|---|---|---|---|---|
| **Montana** | Big Sky CSP (MSU), **Kevin Dome**, via EDX | **3-D nine-component (9-C), 37.25 sq mi**, 2011–2014: shots, CDP gathers, PSTM + angle stacks, raw stacks, velocities, joint inversions | `.sgy` | **≈589 GB SEG-Y, 41 files**; 644.7 GB with models/logs/core | `free-dl` | none set (DOE) | VERIFIED |
| **Nevada** | DOE GDR — **Soda Lake** geothermal | **3D + 3C raw shot records**, ~36 sq mi, 2010 survey | SEG-Y | **8,321 files, 171.04 GB** + 1.02 GB field logs | `free-dl` (also anon S3) | **CC BY 4.0** | VERIFIED |
| **Utah** | DOE GDR — **Utah FORGE** | 2D + 3D: raw uncorrelated *and* correlated shot gathers; plus unmigrated/PSTM/PSDM + velocity model | SEG-Y | **1,122 shot files ≈ 127 GB**; + 849.5 MB reprocessed | `free-dl` | **CC BY 4.0** | VERIFIED |
| **Illinois** (+ IN, KY) | **ISGS Geophysics Data Viewer** — *a real state-survey SEG-Y archive* | **261 profiles**, 2D + at least one full 3D migrated volume; P-wave, S-wave, MASW; 1985–2023 | **SEG-Y** + PNG sections + PDF reports | **233 SGY links, 218 live, 23,454,805,865 B = 23.45 GB** | `free-dl`, no registration | **ISGS Terms of Use — © all rights reserved**; see caution below | VERIFIED |
| **Illinois** | **FutureGen 2.0** via EDX | **Five WesternGeco 2D lines**, full chain: raw SS shot gathers → pre-migration gathers → PSTM gathers/CMPs → velocity fields → migrated stacks | 52 × `.sgy` + 72 extensionless SEG-Y/SEG-D tapes | **47.16 GB** + 0.11 GB VSP + 1.02 GB gravity | `free-dl` | none set (DOE) | VERIFIED |
| **Illinois / Indiana** | **ISGS Wabash CarbonSAFE** via EDX (DE-FE0031626) | 2021 Piatt–Champaign–Vermilion 2D line, 2021 Paris–Wabash 2D line, 2019 Wabash 2D lines — PSTM, structural, X- and Z-X migration, RMS/interval velocity, angle stacks | **42 × `.SGY`** + TIFF sections | **5.12 GB** ZIP | `free-dl` | none stated | VERIFIED |
| **Kentucky** | Battelle / MRCSP **East Bend** via EDX | 2D reflection, Duke Energy East Bend Station, Boone Co. | **4 × `.sgy`** + pre-migrated stacks, 33 horizon files, shotpoint maps | **82.5 MB** ZIP (+ 8.9 MB VSP dataset) | `free-dl` | none stated | VERIFIED |
| **Illinois** | **ISGS / IBDP** via EDX | 2D lines, **reprocessed 3D volume, 3D VSP, 4D volume**, passive microseismic | tar.bz2 / ZIP | **49.3 GB** active + 7.36 GB 3D VSP + 7.81 GB microseismic | `free-dl` | none set (DOE) | VERIFIED |
| **Alaska** | DGGS **Geologic Materials Center** | 56 released tax-credit surveys (**21× 2D, 35× 3D**): poststack, prestack, support | **SEG-Y** (field records may be SEG-D) | **~298 TB**; 2D ≈ 3,476 line-km; 3D ≈ 14,558 km² | **`fee`, waived in full for academic/gov** | asymmetric — see §1.3 | VERIFIED |
| **Alaska** | DGGS GMC well data | Borehole seismic — **VSP and check-shot** (not held by AOGCC) | ZIP | **105 wells, ~171 GB** | `free-dl` | "all well data is free of charge" | VERIFIED |
| **North Dakota** | EERC (UND) CarbonSAFE via EDX | 2D CarbonSAFE line: edited stack + 3 channel sets + full raw input | `.sgy` | **6.43 + 3 × 2.14 + 9.5 GB ≈ 27 GB** | `free-dl` | none set (DOE) | VERIFIED |
| **S. Carolina / Georgia** | SC Research Foundation, South Georgia Rift ARRA, via EDX | **360 raw 3D shot records + 2 VSP**, geometry, LAS logs, core | `.sgy` | **362 files, 1.57 GB** in a 1.83 GB ZIP | `free-dl` | none set (ARRA/DOE) | VERIFIED |
| **Missouri / Arkansas / Tennessee** | USGS Mid-Continent Vibroseis Archive (ScienceBase) | ~280 km 2D CDP, 1977–79 GSI + Western Geophysical, New Madrid | **SEG-Y** raw + stack, + observer logs (PDF), scanned sections (JPG) | **16 ZIPs, 1.57 GB** | `free-dl` | USGS **public domain** | VERIFIED |
| **Utah** | UGS — deep-basin structure | Published **seismic sections as PDF scans** (Great Salt Lake, east shore, N. Salt Lake Valley, Utah Valley) | PDF + XLS index | **67.1 MB / 682 pp** | `free-dl` | not stated | VERIFIED |
| **North Dakota** | NDIC DMR Oil & Gas Division | **Acquisition geometry & footprints** — 347 permitted programs, pre/post-plot maps | scanned PDF + ArcGIS FeatureServer | ~4.4 GB PDFs; 181 3D polygons + 76 2D polylines | `free-dl` | state public record | VERIFIED |
| *(federal, all coastal states)* | USGS **NAMSS** | 972 3D + 610 2D marine surveys | SEG-Y | 697,446 km²; 1.91 M line-km | `free-dl` | **public domain** | VERIFIED |

### 1.2 Montana — Kevin Dome 9-C 3D: the best free onshore US 3D found in this pass (VERIFIED)

Big Sky Carbon Sequestration Partnership (Montana State University), **Kevin Dome**, Toole County, Montana.
22 Kevin Dome datasets on DOE NETL EDX. From the dataset description: *"A 3-D nine component (9-C) survey
was conducted over a **37.25 Square Mile** area in the Kevin Dome project area. This extensive survey was
collected over **three seasons between 2011 and 2014**."* Wave modes: **PP, PS, RR (SH), TT**.

| EDX dataset (`name`) | Files | SEG-Y | Contents |
|---|---|---|---|
| `kevin-dome-seismic-survey-cdp-gathers` | 4 | **227.65 GB** | `PP_cdps` 47.43 · `TT_cdps` 66.70 · `RR_cdps` 66.70 · `PS_cdps` 46.82 GB |
| `kevin-dome-seismic-survey-shots` | 3 | **144.31 GB** | `PP_shots_with_geom` 47.90 · `PS_shots_with_geom` 94.36 · `PS` 2.05 GB |
| `kevin-dome-seismic-survey-pstm` | 22 | **143.99 GB** | PSTM + angle stacks (PP 0-15/15-30/30-45, RR 0-7/7-14/14-21, TT 0-10/10-20/20-30, PS 15-25…35-45 deg), `PS_ccps` 95.28 GB |
| `kevin-dome-seismic-survey-joint-inversions` | 4 | **52.84 GB** | `Ip_joint_PSHSV_lam880`, `Is_joint_PSHSV_lam880`, `Is_SH_time_prestk_SH`, `PP_cdps` |
| `kevin-dome-seismic-survey-velocities` | 4 | **10.51 GB** | `PP` `PS` `RR` `TT` |
| `kevin-dome-seismic-survey-raw-stacks` | 4 | **10.12 GB** | `PP` `PS` `RR` `TT` |
| **SEG-Y total** | **41** | **≈589.4 GB** | |

Companions: `kevin-dome-geologic-model` **53.32 GB**; `danielson-33-17-well-logs` 1.46 GB;
`wallewein-22-1-well-logs` 0.19 GB; core, well tests, gas/liquid analyses, well eBooks, met and
eddy-covariance data. **Grand total across all 22 datasets: 644.7 GB.**

Access verified by unauthenticated HEAD on `rr.sgy` → `200 OK`, `Content-Length: 3013919960`,
`content-disposition: attachment`. Licence: none set. Confidentiality: none.

A rare full **multicomponent prestack-to-inversion chain** — field shots, CDP gathers, velocities, raw
stacks, PSTM angle stacks, joint PP-PS inversions — released openly. **Strongest free onshore 3D option.**

### 1.3 Alaska — the only US state with a real seismic release programme (VERIFIED)

DGGS **Geologic Materials Center**. Order `https://dggs.alaska.gov/gmc/seismic-order.html` · summary
`.../gmc/seismic-well-data-summary.html` · fees `.../gmc/fees.html` · terms
`.../gmc/download/AK-DNR-Seismic-Data-Terms-and-Conditions.pdf` · free well data
`https://dggs.alaska.gov/webpubs/dggs/gmc/well_data/` · AK DOG `https://dog.dnr.alaska.gov/Information/GeologicalAndGeophysicalData`

**Why it exists.** Companies claiming the **AS 43.55.025 / 43.55.023** exploration tax credit had to
surrender G&G data to the Division of Oil and Gas. That is the *only* reason a US state holds a releasable
seismic archive. **Confidentiality:** eligible for release **2 or 10 years** after the exploration activity.

**What ships:** *Poststack* — "seismic volumes in this directory will be in **SEG-Y** format" (migrated,
unmigrated, partial angle stacks). *Prestack* — field records "in either **SEG-Y or SEG-D**", CDP gathers in
SEG-Y. *Support* — acquisition/processing reports, navigation, velocities, observer's logs, 3D bin centres,
post-plot maps.

**Inventory** from the live ArcGIS FeatureServer behind the order map
(`https://services1.arcgis.com/7HDiw78fcUiM2BWn/ArcGIS/rest/services/GMCTaxCreditData/FeatureServer`,
layer 1 = 2D, 2 = 3D, 0 = wells): **56 surveys marked "Released", 2017–2026.**
3D examples: *Kad River* (174 sq-mi, **93,305 GB**), *Schrader Bluff* (233 sq-mi, **86,556 GB**),
*Nigliq Fjord* (196 sq-mi, **69,675 GB**), *Nikiski Marine* (345 sq-mi, 20,480 GB), *Tabasco* (75 sq-mi,
9,984 GB), *Great Bear 2015* (497 sq-mi, 4,377 GB), *NE NPRA* (670 sq-mi, 2,405 GB),
*Aklaq/Smith Bay/Simpson* (602 sq-mi, 1,055 GB); Cook Inlet: Tyonek, Ninilchik, Deep Creek, Kenai Loop,
North Fork, Granite Point Transition. 2D examples: *South Kenai* (375 line-mi, 320 GB), *Toolik/Foothills*
(243), *North Kenai* (200), *Nenana Basin* (197), *Ikpikpuk* (166 line-mi, 429 GB), White Hills, Sagwon, Umiat.

**Fees** (Director's Order, 2017, updated 1 Jul 2019): 2D **$7,500 + $75/line-mile**;
3D **$15,000 + $250/sq-mile + $1/GB**. Poststack only = 25%, prestack only = 75%; both credit toward full.
Worked examples: *Sagwon 2D* $11,784 full / $2,946 poststack; *NE NPRA 3D* $185,008; *Kad River 3D* $151,783.

**Fee waiver.** Fees **shall be waived** for (a) students/classes at accredited institutions, (b) "a
professor, an academic staff member, or a student conducting academic research and associated with an
accredited postsecondary educational institution", (c) State of Alaska and US government agencies.
"Academic research… does not include research performed with the intent to withhold the research from the
public as proprietary information or a trade secret." Waived requesters supply a **USB 3.0 drive** and
pre-paid return label.

**Licence asymmetry — read before planning.** *Purchased* data: "**There are no licensing agreements or
other restrictions when purchasing the data**"; citation required. *Fee-waived* data: "may **NOT** be
reproduced, in part or in whole and by any means, without further permission and charge" — derived figures
and interpretations may still be published. Ownership stays with the originating company.

**Free, no strings:** `https://dggs.alaska.gov/webpubs/dggs/gmc/well_data/` is an open directory —
**105 well ZIPs, ~171 GB**, files up to 16 GB. "**All well data is free of charge.**" Includes **VSP and
check-shot velocity surveys, which are NOT available through AOGCC**.

**AOGCC** (`https://www.commerce.alaska.gov/web/aogcc/`) is DataDome-blocked (403) — **UNVERIFIED**
directly; DGGS describes its holdings as scanned well history/production/injection plus digital logs on
request, **no seismic**.

Contacts: kurt.johnson@alaska.gov (907-754-3597); DOG.TcData@alaska.gov. Release list:
`http://list.state.ak.us/mailman/listinfo/dog.tcdatarelease`.

### 1.4 Utah — FORGE SEG-Y (federal) plus UGS scanned sections (state) (VERIFIED)

**Utah FORGE** — University of Utah / EGI, DOE-funded, on the Geothermal Data Repository, **CC BY 4.0,
free, no account**:
- `https://gdr.openei.org/submissions/1015` — *Utah FORGE: 2D and 3D Seismic Data*, DOI 10.15121/1452746.
  *"The zipped archives numbered from 1-100 to 1001-1122 contain 3D seismic uncorrelated shot gatherers
  SEG-Y files. The zipped archives numbered from 1-100C to 1001-1122C contain 3D seismic correlated shot
  gatherers SEG-Y files."* **1,122 SEG-Y shot files**; plus `2D_seismic_data.zip` (1.92 GB, complete 2D set)
  and `2D-and-3D-Files-List.xls`. **20 resources ≈ 127.3 GB.** Roosevelt Hot Springs / Milford, Utah.
- `https://gdr.openei.org/submissions/1141` — *Utah FORGE: Seismic Reflection Data*, DOI 10.15121/1542059.
  Phase 2c reprocessing, **849.51 MB**. *"For all 3D and 2D data the following datasets were created and
  output in SEG-Y format: Unmigrated Time; Prestack Time Migration (PSTM), Unenhanced and Enhanced;
  Prestack Depth Migration (PSDM), Unenhanced and Enhanced; Velocity Model used for Migration."*

**UGS (the state survey)** — `https://geology.utah.gov/map-pub/data-databases/cvm-geophysical/`. Its
Deep-Basin-Structure section: *"Deep geophysical data consist mostly of **publicly available oil
exploration seismic sections** and are limited to Salt Lake Valley, Great Salt Lake, and the eastern shore
area of Great Salt Lake… **Seismic data are downloadable as Adobe PDF format scans of seismic sections**
found in the referenced material."* Free downloads:
`https://geology.utah.gov/docs/pdf/deep_basin_logs_all.pdf` (**67,137,064 B, 682 pp**) and
`https://geology.utah.gov/docs/xls/deep_basin_summary.xls` (index). Sources cited: McNeil & Smith (1992),
Radkins et al. (1989), Bashore (1982), Schuster (2003), Stephensen et al. (2007). UGS actively solicits
geophysical data donations.

UGS **GeoData Archive** (`https://geodata.geology.utah.gov/pages/home.php`): 6,010 hits for "seismic",
155 for "seismic reflection", 93 for "SEG-Y" — but on inspection overwhelmingly geotechnical
*seismic-hazard* reports; **no SEG-Y in the archive**, everything is PDF/JPG/MP4. Utah Core Research Center
and Utah DOGM: **zero "seismic"**.

### 1.5 Nevada — nothing from NBMG; excellent free SEG-Y from DOE (VERIFIED)

`https://gdr.openei.org/submissions/1655` — *Soda Lake Geothermal: Raw 3D and 3C Seismic-Reflection Data
from 2010 Survey*, DOI 10.15121/2479167, **CC BY 4.0**. *"a petroleum-industry-quality three-dimensional
(3D) and three-component (3C) seismic reflection survey covering about 36 square miles … saved as hundreds
of SEG-Y files, with one 3D seismic record file per vibrator source location."*
**8,321 SEG-Y files, 171.04 GB**, plus `Field Logs.zip` (1.02 GB), `Project Reports.zip` (46.79 MB) and a
SEG-Y processing Jupyter notebook. Anonymous S3:
`aws s3 ls --no-sign-request s3://gdr-data-lake/soda_lake/raw_seismic/2010/v1.0.0/`.

Further Nevada GDR items (titles verified, contents not opened — **UNVERIFIED** as to content):
Hawthorne NV Deep Direct-Use 3D Seismic `/submissions/1043`; Walker Ranch 3D Seismic Images
`/submissions/833`; Steptoe Valley geophysical imaging `/submissions/1568`; Brady's Hot Springs
active-source 3D tomography `/submissions/1070`.

**NBMG itself publishes nothing.** `https://nbmg.unr.edu/` (homepage, `Oil&Gas/`, `Geothermal/`,
`Collections.html`, `Maps&Data/`) — **all zero occurrences of "seismic"**. The pub store
(`https://pubs.nbmg.unr.edu/searchresults.asp?Search=seismic`) has 35 "seismic" items, only **2** for
"seismic reflection" — OF2017-04 ($20) and R062 ($25), both **interpretive, for sale**. NBMG Open Data
DCAT feed: 156 datasets, only "Peak Ground Acceleration" matches. Nevada Division of Minerals
(`https://minerals.nv.gov/`): zero "seismic". Great Basin Center for Geothermal Energy
(`https://www.gbcge.org/`): 406 to curl, homepage lists no datasets — **UNVERIFIED**.

### 1.6 Illinois — the strongest US state for free 2D + 3D + 4D (VERIFIED)

**(0) ISGS Geophysics Data Viewer — the only true state-survey SEG-Y archive found in the entire US.**
`https://go.illinois.edu/geophysics` → `https://prairie-research.maps.arcgis.com/apps/webappviewer/index.html?id=93e86a22e3af49fb97abfe6749bd067f`

The "Seismic Methods → Seismic Reflection" layer is an open ArcGIS FeatureServer:
`https://services9.arcgis.com/9NSsJKjbseNHCAQD/arcgis/rest/services/Seismic_Reflection/FeatureServer/0` —
**261 polyline profiles** with fields `Profile_Name, Project_ID, Project_Name, Year, Type, Images, SGY, PI,
Report, Publication`. **The `SGY` field is a direct download URL.**

- **233 unique SGY URLs; all HEAD-requested: 218 return HTTP 200, totalling 23,454,805,865 B (23.45 GB).**
  15 are broken links.
- Files live under `https://isgs.illinois.edu/geophysics/seismic-reflection/reflection_SGY/`.
- Format confirmed by downloading `736.SGY` (342,622,800 B) and parsing its binary header: genuine SEG-Y,
  ASCII textual header (`C 1 CLIENT … C 2 LINE C:\A-H\07\NEIL\7360000\7`), **format code 2, 2000
  samples/trace, 250 µs sample interval**.
- Survey types: **113 P-wave, 64 S-wave, 18 MASW, 2 P+S, 64 unlabelled**; years **1985–2023**.
- **Includes a full 3D migrated volume:** `OneEarthEnergy_GIBSON-CITY-3D_FFXPSMIGR.SGY` =
  **2,905,914,672 B (2.9 GB)**, free and direct.
- Other highlights: `ADM_DECATUR_2D_L101/L201/L301/L401.SGY` (the IBDP 2D grid);
  `Washington_County_A01–A08` (Illinois Storage Corridor CarbonSAFE, 20 profiles);
  `Macon_CarbonSAFE_MOUNT_AUBURN_2D` incl. a porosity-inversion volume; Wabash CarbonSAFE; FutureGen;
  Hicks Dome; Superconducting Super Collider (1985–87, index only, no SGY).
- **The viewer also covers neighbouring states:** `HendersonKY2006` (7 profiles, Henderson Co. KY),
  `CalhounCo2010` (8 profiles, northern KY), `Indiana2008-10` (13 profiles, NE Indiana),
  `Mitchell CarbonSAFE` (8 profiles, Lawrence Co. IN), `NewCastle` (3 profiles, Henry Co. IN). Example live
  file: `https://isgs.illinois.edu/geophysics/seismic-reflection/reflection_SGY/11015.SGY` (100,663,440 B,
  HTTP 200 verified); `.../815.SGY` (66,450,960 B).

> **LICENCE CAUTION — the strictest terms of anything in this document.** ISGS Terms of Use
> (`https://isgs.illinois.edu/terms-use/`): *"ISGS electronic services and most information contained
> therein are copyrighted with all rights reserved"*, fair use permitted **if ISGS is credited**, and
> *"License fees and a license agreement may be required, depending on the proposed usage."* The files are
> free to fetch but are **not** open-licensed. For redistribution or model training, the EDX/IBDP CC-BY
> material is far cleaner. `https://isgs.illinois.edu/geophysics/` returns 403 to fetchers (human-facing
> landing page **UNVERIFIED**), but the data files themselves serve fine.

**(a) ISGS / Illinois Basin – Decatur Project (IBDP)** — MGSC Phase III, DOE **DE-FC26-05NT42588**.
EDX `illinois-state-geological-survey-isgs-illinois-basin-decatur-project-ibdp-seismic-data-updated`.
The `readme_seismicdata.txt` (fetched) states the archive contains **`Active_Seismic_Data/`** with
subfolders **`2D_Lines`, `3D_Seismic_Volume_Reprocessed`, `3D_VSP_Reprocessed`, `4D_Seismic_Volume`**, and
**`Passive_Seismic_Events_Monitoring/`** with `Downhole_Geophone_Data` and `Surface_Seismometer_Data`.

| Resource | Size |
|---|---|
| `ibdp_active_seismic.tar.bz2` | **49,307,257,896 B ≈ 49.3 GB** |
| `ibdp_3d_vsp_data_original_surveys.zip` | **7,357,644,376 B ≈ 7.36 GB** |
| `ibdp_located_microseismic_event_data.zip` | 7,809,939,546 B ≈ 7.81 GB |
| `passive_seismic_catalog.zip` | 9.53 MB |
| `ibdp_20151217_decatur_4d_processing_report_final.pdf` | 36.8 MB |

Dataset page `https://edx.netl.doe.gov/dataset/illinois-state-geological-survey-isgs-illinois-basin-decatur-project-ibdp-seismic-data-updated`,
**DOI 10.18141/1854142**. Licences on EDX are **mixed CC-BY / CC-BY-SA** — cleaner for redistribution and
model training than the ISGS viewer's terms. Downloads verified by HEAD: `200 OK`,
`content-disposition: attachment`, **no login**.

**One caveat:** the complete passive-seismic monitoring archive (**~75 TB**) is **not** downloadable — a
resource row reads *"PASSIVE SEISMIC EVENTS MONITORING … Contact for access"* (shipped on external hard
drive). The **3D baseline and 4D monitor volumes ARE downloadable**; only the raw passive archive is
request-only.

Companion IBDP datasets (same `free-dl`): Geological Models — `ibdp_static_geologic_model.zip` **37.76 GB**,
`ibdp_geomechanical_model.tar.bz2` **~590 GB**, `ibdp_dynamic_reservoir_model.zip` 1.34 GB; Well Information
4.59 GB (CCS1/VW1/GM1 logs, core, sidewall core, well tests); CO2 Injection Monitoring 8.36 GB; MVA GIS +
imagery 13.31 GB; Photos 629 MB; Selected Reports 353 MB. Archives are `.tar.bz2` — plan decompression space.

**Mirror:** CO2DataShare (SINTEF) republishes IBDP at
`https://co2datashare.org/dataset/illinois-basin-decatur-project-dataset` — a **14.3 GiB** seismic component
including "a high resolution 3D seismic survey", under the *"Illinois Basin – Decatur Project (IBDP) CO2
Injection Datasets License"*, open access with click-through acceptance; 13,442 component downloads since
1 March 2022.

**(a2) ISGS Wabash CarbonSAFE** — `https://edx.netl.doe.gov/dataset/illinois-state-geological-survey-isgs-wabash-carbonsafe-seismic-data`,
DOE **DE-FE0031626**, a single **5,123,227,868 B** ZIP. Central directory read by HTTP range request
(ZIP64): **75 entries, 42 × `.SGY`** —
`2021_Piatt_Champaign_Vermilion_2D_Line/Processed_SGY_Data/` (15 SEG-Y @ 206.6 MB each — PSTM, structural,
X-migration, Z-X migration, RMS and interval velocity, angle stacks),
`2021_Paris_Wabash_2D_Line/Processed_Data_SGY/` (17 SEG-Y @ 166.8 MB each),
`2019_Wabash_2D_Lines_1000_2000/`, plus TIFF sections and a 67.5 MB locations map. Tagged both **Illinois**
and **Indiana / Vigo County**.

**(a3) Kentucky — East Bend (Battelle / MRCSP).** `https://edx.netl.doe.gov/dataset/east-bend-seismic-data`
(Duke Energy East Bend Station, Boone Co., KY). The **82,502,774 B** `seismic-2d.zip` was downloaded and
enumerated: **130 entries including 4 SEG-Y** — `Seismic V1 Raw Data/enhmig.sgy` (3.62 MB),
`enhstr.sgy` (3.61 MB), `Seismic V2 Raw Data/enhmig.sgy` (3.25 MB), `enhstr.sgy` (3.24 MB) — plus
pre-migrated stacks, 33 horizon files, `Eastbend shot pts_maps.pdf`, and a line-coordinate spreadsheet.
Companion `https://edx.netl.doe.gov/dataset/east-bend-vsp-data` is an 8.9 MB VSP ZIP. Direct storage URLs
return HTTP 200 with no authentication.

**(a4) MRCI Legacy Seismic Inventory — a free line index for MI / WV / OH / IL.**
`https://edx.netl.doe.gov/dataset/mrci-legacy-seismic-inventory`. The XLSX was downloaded and parsed:
**920 legacy 2D lines** with line name, county, state, acquisition date, BSP/ESP, length, group and source
interval, processing date, energy source. Breakdown: **Michigan 603, West Virginia 147, Ohio 142,
Illinois 28**. Metadata only — no traces — but it is a usable shotpoint/line index for four states whose
own surveys publish nothing.

**(b) FutureGen 2.0** — Morgan County, Illinois. EDX `vetted-futuregen-2-0-technical-data` (30 packages
"T8"–"T31"). Seismic package **`T9 - 2D Seismic`, 47,159,760,989 B (47.16 GB)**; central directory listed
by range request, **193 entries**:

| Folder | Files | Uncompressed |
|---|---|---|
| `T9.2 - L201_WesternGeco_Data_Acquisition Morgan County` | 13 | **14.64 GB** |
| `T9.1 - L101_WesternGeco_Data_Acquisition Morgan County` | 11 | **11.75 GB** |
| `T9.3 - L301_WesternGeco_Data_Acquisition Fayette County` | 11 | **10.28 GB** |
| `T9.4 - L401_WesternGeco_Data_Acquisition Douglas County` | 11 | **9.43 GB** |
| `T9.5 - L501_WesternGeco_Data_Acquisition Douglas County` | 10 | **4.92 GB** |
| `T9.8 - EDI_Data_Reprocessing_PSTM_Data_Sep2012` | 60 | 0.21 GB |
| `T9.11 - Bob_Hardage Seismic Interpretation Reports` | 37 | 0.22 GB |
| `T9.9 - EDI_Data_Reprocessing_PSTM_Data_Nov2013` | 21 | 0.10 GB |
| `T9.10 - EDI Third Reprocessing Jan 2014 (without trip statics)` | 10 | 0.07 GB |
| `T9.7 - Schlumberger_Data_Processing` | 8 | 0.26 GB |

Five 2D lines, each a complete chain — file names include `RAW_SS_SHOT_GATHERS`,
`PRE_MIGRATION_SHOT_GATHERS`, `PRE_STACK_MIGRATION_GATHERS`, `PRE_STACK_MIGRATION_CMPS`, `VELOCITY_FIELD`,
`QUICKLOOK_MIG`, `RAW_/HIGH_FREQ_/ENHANCED_PRE_STACK_MIGRATION_STACK`. Largest entries: 5.89 GB
(`FUTUREGEN_Morgan_PRE_MIGRATION_SHOT_GATHERS_L101`), 4.93 (`..._RAW_SS_SHOT_GATHERS_L201`), 4.81, 4.21,
4.06, 3.88, 3.70, 3.67 GB. By extension: **52 × `.sgy` (0.36 GB)** processed stacks; **72 extensionless
files totalling 51.00 GB** = the WesternGeco tape deliverables (SEG-Y/SEG-D without extension). Also
`.sp1`/`.spr` navigation, `.vel`, `.as0`, 29 PDFs, and a Readme. Companions: `T13 - 2013 FGA-1 VSP Seismic
Program` (0.11 GB), `T12.1 - Gravity Data` (1.02 GB, also `futuregen-geophysical-gravity-data`),
`T20 - MVA Design Basis` 15.95 GB, `T21 - Reservoir Model UIC Permit` 8.52 GB,
`T31.8 - Illinois Geospatial Datasets` 3.59 GB, `T10 - FGA-1 Borehole Geophysical Log Data` 1.21 GB.

### 1.7 North Dakota — a rich *permit* database and a separate EDX SEG-Y release (VERIFIED)

**(a) EERC CarbonSAFE SEG-Y on EDX** — DOE **DE-FE0029488**, EDX
`de-fe0029488-nd-integrated-carbon-capture-and-storage-complex-feasibility-study-public-data`:

| Resource | Size | Format |
|---|---|---|
| `carbonsafe-2d-line-edited.sgy` | **6,431,677,920 B ≈ 6.43 GB** | **SEG-Y** |
| `carbonsafe-2d-line-edited-channel-set-1/2/3.sgy` | 2,143,895,040 B each ≈ **3 × 2.14 GB** | **SEG-Y** |
| `carbonsafe-2d-input-data.zip` | **9,499,468,518 B ≈ 9.5 GB** | raw input |
| `2DSeismicNotesandDescriptions.zip` | 16.0 MB | maps, logs, descriptors |
| `NDICFileNo.37672-J-ROC1.zip` / `.37380-J-LOC1.zip` | 219 MB / 6.6 MB | NDIC well files |
| `Core_Petrophysics.zip`, `WellTesting.zip` | 185 KB / 114 KB | Flemmer-1 (API 33-057-00039), BNI-1 (33-065-00018) |

**≈27 GB total.** Verified by unauthenticated HEAD: `200 OK`, `content-length: 2143895040`,
`content-disposition: attachment`. Licence: none set; the bundled `eerc-doe-disclaimer.txt` is a standard
EERC/DOE liability disclaimer with no use restriction.

**(b) NDIC DMR Oil & Gas Division — geometry, not signal.** `https://www.dmr.nd.gov/oilgas/seismic/seismic.asp`
states: *"Seismic location and post-plot maps displaying the source and receiver layouts will be available
electronically through our GIS map server link."*
The table `https://www.dmr.nd.gov/oilgas/seismic/seismicstats.asp` ("Seismic Programs Permitted Since July
1997", *"Click on Permit# to see permit file and maps"*) was parsed in full: **347 programs**, with permit
#, name, status, dates, geophysical contractor, client, township-range, county, source-point count, sq-mi
(3D) or linear-mi (2D), method. Aggregates: **10,121.6 sq mi of 3D**, **1,406.9 linear miles of 2D**,
**1,185,102 source points**. Methods: vibroseis 162, shot-hole 106, combo 31, seismic/micro 14, weight drop
12, orphan 7, EM 6, passive seismic 3, e-vibe 2, surface orbital vibe 2, air gun 1.
Permit PDFs at `https://www.dmr.nd.gov/oilgas/seismic/permits/{permit}.pdf` — 347 files, 1.4–52 MB,
**~4.4 GB total**, free, no auth (sample `970342.pdf` fetched: 12 pages of **scanned raster** pre-plot vibe
maps over aerial imagery).
**Open ArcGIS FeatureServers** (unauthenticated, `Query` enabled, maxRecordCount 2000, harvestable as GeoJSON):
- `https://gis.dmr.nd.gov/dmrpublicservices/rest/services/OilGasPublicMapDataVectorTiles/Seismic2D/FeatureServer/0` — `OGD_Seismic2DPreplot`, polyline, **count 76**
- `.../Seismic3D/FeatureServer/0` — `OGD_Seismic3DPreplot`, polygon, **count 181**
Fields: `permit, progname, geophyscon, client, loctr, county, permitd, commenced, completed, numpoints, sqmi, linmi, method, status`.

**Confidentiality — notable.** Full text of **NDCC ch. 38-08.1** (`https://ndlegis.gov/cencode/t38c08-1.pdf`)
and **NDAC ch. 43-02-12** (`https://www.ndlegis.gov/information/acdata/pdf/43-02-12.pdf`) was searched:
**zero occurrences of "confidential" in either.** There is no confidentiality period, because trace data is
never filed with the state. What *is* required is geometry — **NDAC 43-02-12-06**: *"Within thirty days
following the completion of geophysical exploration … shall file with the commission a seismic completion
report … incorporating a postplot map displaying the actual source point location … **If obtained by the
contractor, the latitude and longitude of each source and receiver point shall be submitted to the
commission to the nearest tenth of a second.**"* The only fee is the industry's **$100 permit application
fee** (43-02-12-04(1)(k)). NDGS itself (`https://www.dmr.nd.gov/dmr/ndgs`): **no seismic**.

**Practical implication:** ND is the best US state source for free public **acquisition geometry and survey
footprints** — but source/receiver tables live inside scanned PDFs, and traces are never public.

### 1.8 Missouri / Arkansas / Tennessee — USGS Mid-Continent Vibroseis Archive (VERIFIED, federal)

Parent record `https://www.sciencebase.gov/catalog/item/57c8269fe4b0f2f0cec02347` (Hamilton & Zoback, 1979,
*Seismic Reflection Profiles in the Northern Mississippi Embayment*); **data child**
`https://www.sciencebase.gov/catalog/item/57da9b09e4b090824ffc308f` — **16 ZIPs** (`D1_all.zip`–`D3_all.zip`,
`S1_all.zip`–`S13_all.zip`), **1,568,584,994 B**. Each contains `*_raw.sgy` (raw field data), `*_stack.sgy`
(stack where recoverable), `*-Oblog.pdf` (observer's logs), `*.jpg` (scanned grayscale stacked section).
**~280 km of multichannel CDP profiles acquired 1977–79 by Geophysical Service Inc. and Western Geophysical**
under USGS contract, over SE Missouri / NE Arkansas / NW Tennessee; read off 9-track tape 2007–2009 and
converted via ProMAX. `free-dl`, no registration, **USGS public domain**. The README notes "All recoverable
**non-proprietary** vibroseis data"; the released SEG-Y carries no restriction.

### 1.9 South Carolina / Georgia — South Georgia Rift ARRA seismic (VERIFIED)

*Geologic Characterization of the South Georgia Rift Basin for Source Proximal CO2 Storage* — South
Carolina Research Foundation, ARRA project **DE-FE0001965**. EDX
`https://edx.netl.doe.gov/dataset/geologic-characterization-of-the-south-georgia-rift-basin-for-source-proximal-co2-storage`.
One file, `SouthCarolinaARRAsitecharacterizationdata.zip`, **1,827,856,310 B**; HTTP 206 `application/zip`,
**no login or API key**. Bounding box (EDX `spatial`): **−82.376 to −80.486 lon, 31.616 to 32.750 lat**.
Licence: `license_title`/`license_id` both null. POC mary.dailey@netl.doe.gov.

Central directory parsed twice independently — **502 entries**:

| Folder | Files | Uncompressed |
|---|---|---|
| `South Carolina Data ARRA Data/3D Seismic/` | **366** (360 × `.sgy` raw 3D shot records @ 4,337,976 B each, + `SCO2 3D.grid`, `SCO2_3DSRC.src`, `SCO2_3DREC.rec`, `SCO2-3D_ObNotes.XLS`) | **1.57 GB** |
| `.../Rizer_#1_VSP/` | 3 (2 × VSP SEG-Y, `VSI_001_A_geo_wavefield_*.sgy`) | small |
| `.../GIS/` | 72 (incl. `2D_Seismic_Shapefiles/SCO2_1CDP`…`SCO2_7CDP`) | small |
| `.../Conventional_Core_Weatherford/` | 19 | 0.29 GB |
| `.../Rotary_Core_Weatherford/` | 17 | 0.08 GB |
| `.../Rizer_#1_Well_Logs/` | 20 (9 × `.las` — ELAN, SonicScanner, 3D rock properties; PDS/PDF images) | 0.03 GB |
| `.../Cuttings_Weatherford/` | 4 | small |

**362 SEG-Y files, 1,566,078,856 B uncompressed.**

**Important correction.** The abstract describes *"approximately **81 kilometres of 2-D seismic reflection**
data … collected by **Bay Geophysical, Inc.** … divided into **two lines approximately 40.5 km each**, with
Line 1 intersecting Georgia well **GGS-3457**."* **That 2D SEG-Y is NOT in the ZIP** — only 2D CDP *location*
shapefiles ship. What *is* included as SEG-Y are the **360 raw 3D shot records** and 2 VSP files. The
**Rizer #1** test well is the South Carolina leg.

Offshore GA/SC/NC is covered by **NAMSS** — e.g. survey `b-05-86-at`
(`https://walrus.wr.usgs.gov/namss/survey/b-05-86-at/`), download
`https://walrus.wr.usgs.gov/namss/data/1986/namss.B-05-86-AT.mcs.airgun.zip` (89.9 MB, HTTP 206). Other
surveys over the Georgia Embayment: **B-02-80-AT** (1980, *Gulf Seal*), **B-01-81-AT** (1981, *Rob Ray I*).
All 2D MCS, airgun + streamer, contributed by BOEM. Terms, quoted from the survey page: *"Under the terms of
procurement, these data are to be available to the public **25 years after the issuance of the exploration
permit**."* Machine-queryable via WMS `GetFeatureInfo` — layer name is **`namss`**:
`https://walrus.wr.usgs.gov/namss/wms?...&LAYERS=namss&QUERY_LAYERS=namss&INFO_FORMAT=application/json&BUFFER=...`
(note: WebFetch 403s the NAMSS host; use curl.)

### 1.10 Explicit negatives — states with NO public seismic reflection data

| State | Agency (verified URL) | Finding | Status |
|---|---|---|---|
| **Kansas** | KGS `https://www.kgs.ku.edu/` ; KCC `https://www.kcc.ks.gov/oil-gas` | **NO seismic, ever.** Full evidence chain in §0. | VERIFIED |
| **California** | CalGEM `https://www.conservation.ca.gov/calgem` ; CGS `https://www.conservation.ca.gov/cgs` | **NO.** "seismic"/"geophysic" appear **zero times** on the CalGEM homepage source. GIS downloads page (`.../calgem/maps/Pages/GISMapping2.aspx`) lists exactly 12 datasets — all well/boundary/facility vectors. CGS's "Seismic Hazards and Faults" is **earthquake hazard zonation** (Alquist-Priolo), not reflection. **PRC §3234** covers *well records* and expressly excludes "interpretive data not generally available to all operators"; no operator duty to file seismic. Legacy CA 2D/3D remains proprietary multiclient. SCEC CVM (`https://southern.scec.org/research/cvm`) is a **derived velocity model**, not data. | VERIFIED |
| **Colorado** | CGS `https://coloradogeologicalsurvey.org/` ; ECMC `https://ecmc.state.co.us/` | **NO.** Every CGS "seismic" hit is earthquake seismology/paleoseismology (ON-006-15M, IS-60, SP-19, SP-28, MI-97 Cheraw fault, OF-78-03, B-43). `"seismic reflection"` returns only ON-010 and SP-10. ECMC `sitemap.xml` (66 URLs) has **no seismic entry**; `data.html` and `app/data/downloads.html` contain zero "seismic". | VERIFIED |
| **New Mexico** | NMBGMR `https://geoinfo.nmt.edu/libraries/subsurface/home.html` ; OCD `https://www.emnrd.nm.gov/ocd/` | **NO.** Library of Subsurface Data holds 50,000+ core boxes from 2,500+ wells, 51,000+ cuttings boxes from 15,500+ wells, **well** logs from 50,000+ wells, records, maps, production, porosity/perm and source-rock analyses. **Seismic is not mentioned at all.** OCD and its `/ocd-data/ocd-imaging/`, `/ocd-data/ftp-server/`: **zero "seismic"**. State Land Office `https://www.nmstatelands.org/`: zero. | VERIFIED |
| **Wyoming** | WSGS `https://main.wsgs.wyo.gov/` ; WOGCC `https://wogcc.wyo.gov/` | **NO.** Full WSGS catalogue exported as CSV (1,426,055 B) — **only 5 "seismic" records**, all interpretive/hazard: RI-61 (Cow Creek Field seismic attributes), HR-96-1, PHR-95-2, OFR-2019-1 (Teton fault), a Precambrian note. WSGS "GLCS = Geophysical Log Cross Section" is *well* logs. WOGCC homepage, `/public-resources/oil-gas-resources` and `/rules`: **zero "seismic"/"geophysical"** — seismic permitting sits with the Office of State Lands and BLM, not WOGCC. | VERIFIED |
| **South Dakota** | SDGS `https://www.sdgs.usd.edu/` | **NO.** Publication catalogue `https://www.sdgs.usd.edu/publications/PUBLIST.pdf` — 131 pages, 172,784 characters, **0 occurrences of "seismic"**. Online Databases page lists only Lithologic Logs, Oil & Gas, Publications, Water Quality, Core & Cuttings. Oil & Gas Initiative product is **scanned geophysical *well* logs** — "~6,043 geophysical logs representing 5,391 drill sites… scanned into Adobe PDF and/or TIFF". | VERIFIED |
| **Louisiana** | SONRIS `https://sonlite.dnr.state.la.us/ords/f?p=108:1` ; `https://www.dce.louisiana.gov/` | **NO.** Full Data Portal report list enumerated (~90 reports): scout reports, proration, LUW production, transporter/refinery ledgers, orphan wells, UIC, CUP, pits. **Zero seismic reports.** Louisiana **leases the right to shoot seismic** on state water bottoms via the State Mineral and Energy Board (e.g. a 2003 $4.6 M exclusive geophysical agreement, Iberia Parish) but never takes delivery of the data. DENR became the **Department of Conservation and Energy** on 1 Oct 2025. LGS (`https://www.lsu.edu/lgs/sections/geophysical-resources.php`) offers near-surface **refraction** *services*, not an archive. | VERIFIED |
| **Mississippi** | MSOGB `https://www.ogb.state.ms.us/` ; MDEQ `https://www.mdeq.ms.gov/geology/` | **NO.** Full MSOGB menu tree extracted; "seismic"/"geophysic" appear **zero times** in page source. MDEQ logging is resistivity/SP/gamma for water wells. Energy Library `https://geology.deq.ms.gov/energy/` is well documents. | VERIFIED |
| **Alabama** | GSA `https://www.gsa.state.al.us/` ; OGB `https://www.gsa.state.al.us/ogb/` | **NO.** Angular app; both menu templates pulled directly (`/Scripts/GSAOGB/main/ogbMenu.html` + GSA menu): Well Database, Engineering, Field & Pool, Production, Full Text Document Search, Online Map, GIS Data, Logroom/Facilities, Core and Sample Database. **No seismic entry in either menu.** `/inter/facilities` and `/ogb/rules` render client-side — UNVERIFIED, so no Alabama confidentiality rule can be quoted. | VERIFIED (menus) |
| **Arkansas** | AGS `https://www.geology.arkansas.gov/` | **NO.** "seismic" appears zero times. Subsurface page (`.../maps-and-data/well-cuttings-core-inventory-well-logs.html`): ~10,000,000 ft of cuttings from 2,500 wells, 2,500 ft oil/gas core, 300,000 ft mineral core, electric/strip logs — **"No seismic data is mentioned."** Access **onsite only**: "No sample materials are permitted to leave the premises at any time"; "There is no charge for an onsite examination." AOGC (`https://www.aogc.state.ar.us/`) Cloudflare-403 on every path — **UNVERIFIED**. | AGS VERIFIED |
| **Florida** | FGS `https://floridadep.gov/fgs/data-maps` | **NO trace data** — but seismic line *locations* are statutory. **Fla. Stat. 377.075(4)(g)** obliges FGS to publish maps identifying "the location in latitude and longitude of… **seismic line recording points**". The 10-year confidentiality cap in **377.075(4)(f)** attaches to *economic mineral industry company data*, **not** seismic. FGS offers GEODES boreholes, Map Direct, `https://geodata.dep.state.fl.us/`, STATEMAP, scanned field books, a Qlik geophysical-*log* lookup — **no SEG-Y**. Collections are **appointment-only**. FDEP permits "geophysical operations" under **Rule 62C-26.007** (eff. 5/9/2013); full text not retrievable — UNVERIFIED whether trace data must be filed. | VERIFIED |
| **Missouri** | MO DNR `https://dnr.mo.gov/land-geology/geology` ; `.../maps-data-research` | **NO.** Complete inventory: geologic maps, Mine Map Repository (~2,000 maps), field notebooks, bibliography, **GeoSTRAT**, **WISDIM**, McCracken Core Library, ArcGIS Hub. GeoSTRAT's only "geophysical" holding is **~4,100 *downhole* logs**. No oil-and-gas data page exists under `/land-geology/` (four candidate paths probed, all 404). New Madrid profiles are **USGS-owned**, see §1.8. CERI (`https://www.memphis.edu/ceri/`) operates the network and publishes an earthquake map — **no reflection distribution**. | VERIFIED |
| **Iowa** | IGS `https://iowageologicalsurvey.uiowa.edu/` | **Essentially NO** — one scanned report. **GeoSam** (`https://igs.iihr.uiowa.edu/igs/geosam/home`) is samples and well records, no seismic. Publications catalog category dropdown includes *Aeromagnetic Surveys* but **no seismic category**. The single seismic item: **OFR 83-2**, *"Data collection and processing parameters for the Malvern seismic reflection traverse"* (Cumerlato, 1983, 16 pp), free PDF **17,794,902 B**, `https://igs.iihr.uiowa.edu/igs/publications/uploads/OFR-1983-2.pdf` — acquisition/processing parameters, **not SEG-Y**. No Manson impact-structure seismic in the catalog. *(Note: `www.iihr.uiowa.edu` no longer resolves; use `igs.iihr.uiowa.edu`.)* | VERIFIED |
| **Minnesota** | MGS `https://cse.umn.edu/mgs` ; `https://mngs-umn.opendata.arcgis.com/` | **NO.** The Geophysics Portal's own description is the citation: *"This includes **aeromagnetic, gravity, rock properties and passive seismic** data"* — i.e. **no reflection seismic**. MGS "passive seismic" layers are **HVSR point soundings** in County Geologic Atlases (e.g. `Cook_County_Geology_WFL1/FeatureServer/6`), used for depth-to-bedrock. **GLIMPCE / Midcontinent Rift deep profiles are not an MGS product** — ScienceBase returns 0, EDX returns 0; it was a joint USGS/GSC program, so any holding is federal or Canadian. Current public home of GLIMPCE SEG-Y: **UNVERIFIED**. | VERIFIED |
| **Wisconsin** | WGNHS `https://home.wgnhs.wisc.edu/data/` | **NO data** — interpretive only. Data index offers GIS, GeMS GIS, rock porosity/density, TillPro, wiscLITH. Catalog search `?q=seismic` returns exactly **3** items, all interpretive: McGinnis & Mudrey (2003) *Seismic Reflection Profiling and Tectonic Evolution of the Midcontinent Rift in Lake Superior* (report + large plates); Dickas & Mudrey (2002) regional interpretation (interactive HTML); *Geoscience Wisconsin* v.12 (1988, a **refraction** article). Files served from `https://data.wgnhs.wisc.edu/pubshare/`. | VERIFIED |
| **Virginia** | Virginia Energy DGMR `https://energy.virginia.gov/geology/geologymineralresources.shtml` | **NO.** Collections page (`.../geology/Collections.shtml`) lists every collection with counts — **no seismic collection**: Aerial Photographs 7,622 · Borehole Data 1,800 · Core Repository 447 · Geologic Sections 5,500 · **Geophysical Data 1,734** · O&G Well Cuttings 7,376 · OCS Sand Resources 6,273 · Publications 5,200 · Rock Repository 7,500. Proof that "Geophysical Data" = **borehole logs**: the DGMR web map Experience Builder config (`.../webmaps/GeologyMineralResources/cdn/2/config.json`, 353,045 B) has **24 occurrences of "Geophysical", every one a `Geophysical_Log` string field on well/borehole tables, and ZERO occurrences of "Seismic".** Taylorsville Basin CCS on EDX yields only **gravity and magnetic** surveys. *(Note: `energy.virginia.gov/geology/` 403s; `geologyhome.shtml` 404s.)* | VERIFIED |
| **Tennessee** | TDEC `https://www.tn.gov/environment/program-areas/geology.html` | **NO.** Data Preservation & Historical Document Collections lists **18 collections** — maps, reports, geochemical analyses, field observations, drillers logs, correspondence, TVA documents, zinc mining, rock cores. **Seismic appears in none.** Caveat: the document viewer (`https://tdec.tn.gov/document-viewer/search/tgs`) is an Angular SPA with no reachable JSON API, so the negative rests on published collection descriptions, not a keyword query. NW Tennessee **is** covered by the free USGS vibroseis archive (§1.8). | VERIFIED (collections list) |
| **Georgia** | EPD `https://epd.georgia.gov/publications` | **NO.** The Georgia Geologic Survey no longer exists as a standalone unit (five candidate paths all 404); material sits under EPD's Watershed Protection Branch. The whole offering is six publication series — Atlases, Bulletins, Circulars, Guides and Reports, Information Circulars, Maps. **No seismic data of any kind.** Onshore southern Georgia seismic is public **from DOE**, not the state (§1.9); offshore from NAMSS. | VERIFIED |
| **South Carolina** | SCGS `https://www.dnr.sc.gov/geology/index.html` | **NO.** Offering: SC Geology journal volumes, Bulletins, 1:24,000 quadrangle maps, an ArcGIS viewer. The strongest citation is the survey's own digital-data page (`.../geology/digital-data.html`): *"This section of the SCDNR website is currently **obsolete**"* — offering only quad-map compilations and KML. GIS by email request. SC-relevant seismic exists **federally** (§1.9). | VERIFIED |
| **North Carolina** | NCGS `https://www.deq.nc.gov/about/divisions/energy-mineral-land-resources/north-carolina-geological-survey` | **NO data** — publishes seismic **line-location maps** only. **NCGS OFR 2010-07** (Reid & Taylor, 2010), a digital compilation of the Sanford sub-basin, whose components are *"**Seismic lines**, drill hole locations, geologic units, hydrocarbon shows"* — i.e. line traces on a map. Free PDF **5,467,276 B**. Also OFR 2013-01 (Mesozoic rift basins), OFR 2009-01, and USGS OFR 2008-1108. **No SEG-Y and no scanned seismic sections.** Other pubs fee via `http://www.nc-maps.com/`. Offshore NC covered by NAMSS. | VERIFIED |

| **Texas** | BEG `https://www.beg.utexas.edu/about/facilities` ; RRC `https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/` | **NO free BEG seismic beyond the already-documented Stratton survey.** All **57,740 archived URLs** on `beg.utexas.edu` were enumerated via the Wayback CDX API: **not a single `.sgy` or `.segy` file**, and no seismic data-sales/download product page ever existed. BEG's "data repositories" are physical — Austin CRC (700,000+ boxes), Houston RC (900,000+ boxes), Midland CRC (**permanently closed to the public 1 Nov 2024**), and the **Geophysical Log Facility**, explicitly wireline-only: "Only the raster images of well logs are available, we do not currently offer LAS files", **$5.00 per log**, appointment only. **RRC's whole ~50-dataset download catalogue contains nothing seismic.** A legacy BEG "SAND2" page once distributed Boonsville-3D ancillary products (`Amplitude_Slices_tifs.zip`, `Horizons.zip`, `Cultural_Data_zgfs.zip`, `BOONSVILLE_LAS+PROD_DLC.zip`) — all now **404**. TexNet (`https://texnet.beg.utexas.edu/`) is an **earthquake** catalogue (free, since 1 Jan 2017, plus a "High Resolution Catalog" and an "Earthquake Dataset for AI") — no reflection data. | VERIFIED |
| **Oklahoma** | OGS `https://www.ou.edu/ogs/data` ; OPIC `https://www.ou.edu/ogs/opic/welldata` ; OCC `https://oklahoma.gov/occ/divisions/oil-gas.html` | **NO.** OGS's data index has exactly nine categories — Oil and Gas, Coal, Fault Database, Brine, Slimhole Cores, Aerial Photographs, Basin Bibliographies, Well Pressure, NGGDPP — **none seismic**. **2,274 archived `ou.edu/ogs` URLs** enumerated: every "seismic" URL is earthquake monitoring. OPIC is "Oklahoma's official repository for full-scale **paper logs** from more than 367,000 wells" plus microfiche, 1002A reports, scout tickets, mud logs, 1940–60 aerial photos; 100 mi of core; 50,000-well samples. Terms: **"There is no cost to use the collection. Copies are 15 cents"**, public access **by appointment only**. OCC's only seismic-named unit is the **Induced Seismicity & UIC Department**. | VERIFIED |
| **Nebraska** | NOGCC `http://nogcc.ne.gov/` (HTTP only) ; CSD `https://snr.unl.edu/csd-esic/` | **NO — the cleanest negative of all.** The consolidated NOGCC rules PDF (`http://nogcc.ne.gov/Publications/NE_Rules.pdf`) was downloaded and ~316,000 characters of text extracted: **zero occurrences of "seismic" or "geophysic"** — Nebraska has **no seismic filing requirement and therefore no confidentiality period**. Closest geophysics offered is **Aeromagnetics, Bouguer Gravity and Lineaments** maps for the Forest City Basin (potential-field). **7,990 archived `snr.unl.edu/csd*` and 10,107 `snr.unl.edu/data*` URLs** enumerated; the single geophysics hit is `NGC_GeophysicalLogs_Metadata_Standard_v1_0.pdf` (well-log metadata). *(HTTPS and `nogcc.nebraska.gov` do not resolve. Live CSD pages 403 — archival evidence only, so the live check is UNVERIFIED.)* | VERIFIED |
| **Michigan** | MGRRE `https://mgs.wmich.edu/michigan-geological-repository-for-research-and-education/` ; EGLE `https://www.michigan.gov/egle/about/organization/geologic-resources-management/resources-and-data` | **NO catalogued seismic holding** — contrary to the common assumption that MGRRE holds a big seismic archive. MGRRE's collection pages enumerate **only** cores, drill cuttings, cuttings analyses, well logs and thin sections (530,000 ft of core from ~1,850 wells; cuttings from 28,000+ wells; 2,500+ thin sections; headline 600,000+ linear ft, 50,000+ well records). The archived URL tree contains **no seismic slug**, and the site's WordPress search API returns exactly **one** page for "seismic" — the research-goals list, which reads: *"Preserve and reinterpret **legacy seismic data** to better identify Michigan's geological resources."* So legacy seismic is a preservation **project**, not a catalogued or downloadable collection. In-person, one week's notice; **onsite access suspended from 1 July 2026** for the Parkview Campus move. EGLE (the Oil, Gas and Minerals Division is now **Geologic Resources Management**) offers a free FTP of Formation Tops, Drillers Logs, **Geophysical (Raster) Logs in TIFF/PDF/LAS**, Early Production and Mining — **"seismic" appears zero times**; "geophysical" means wireline. Data Miner covers "oil, gas, and **non-confidential** mineral wells" — the only confidentiality flag found, and it applies to mineral wells, not seismic. *(Michigan does, however, have **603 legacy 2D lines indexed** in the MRCI inventory — see §1.6(a4).)* | VERIFIED |
| **Ohio** | ODNR `https://ohiodnr.gov/discover-and-learn/safety-conservation/about-odnr/geologic-survey/publications-maps/publications-catalog` | **NO in the current catalogue.** The entire **Ohio Geology Publications Catalog** (2,665 rows of embedded JSON) was pulled and searched: **0 hits for "reflection", 0 for "refraction", 0 for "MASW"**. The 17 "seismic" rows are all earthquake items (OhioSeis newsletters, GeoFacts 3, OFR 2017-1 earthquake catalogue, HVSR Teays-Valley posters), plus IC-56 (1990), a cored-hole report that merely *includes* "a seismic profile across the core site". **Two things existed on the legacy site and are now delisted — see §1.11.** OhioSeis / Ohio Seismic Network is earthquakes. *(Ohio has **142 legacy 2D lines indexed** in the MRCI inventory.)* | VERIFIED |
| **West Virginia** | WVGES `https://www.wvgs.wvnet.edu/www/datastat/datastat.htm` | **NO.** The data-and-statistics index lists Pipeline and Pipeline-Plus well databases, DDS-5 well data DVD, scanned well logs, digitized logs, scanned well records (`downloads.wvgs.wvnet.edu`), the Appalachian gas-plays atlas, production search back to 1979, CBM/Trenton/Martinsburg/basement-test well lists, geostatistical case studies — **no seismic, no SEG-Y**. **11,243 archived `wvgs.wvnet.edu` URLs** enumerated: *every* "seismic" URL is earthquake monitoring. The multi-state **Utica Shale Playbook** hosted by WVGES distributes shapefiles, digitized and scanned well logs, source-rock analyses, TOC, core photos, SEM images and thin sections — **no seismic category**. *(WV has **147 legacy 2D lines indexed** in the MRCI inventory.)* | VERIFIED |
| **Kentucky** | KGS `https://kygs.uky.edu/` ; `https://kygs.uky.edu/data/oilgas/` | **NO from the state survey.** Downloads are well locations (162,157 wells), deviated-well traces, gathering lines, field outlines — zipped shapefiles. The searchable-database index (`https://kgs.uky.edu/kgsweb/DataSearching/OilGas/OGSearch.asp`) lists oil-and-gas records, production, rock core, thin section, coal borehole/thickness/quality, water wells, geologic descriptions — **no seismic category**. Everything labelled "seismic" is the Kentucky Seismic and Strong-Motion Network. The KY Consortium for Carbon Storage (`https://www.uky.edu/KGS/kyccs/`) mentions 2008 "seismic data acquisition" but publishes only quarterly reports. The Trenton–Black River page (`https://www.uky.edu/KGS/emsweb/research/trenton/seismic.htm`) describes a NETL/NYSERDA-funded shallow P- and S-wave programme in Clark County whose "deliverables … will be the seismic-reflection profiles" — **never posted**. *(Free KY SEG-Y does exist, from other publishers — see §1.6(a3) and §1.6(0).)* | VERIFIED |
| **Indiana** | IGWS `https://igws.iu.edu/` (`igws.indiana.edu` 301s here) | **NO reflection data — refraction points only.** The site is a React SPA; its CMS API (`https://igws.iu.edu/api/cms/allPages`, 861 KB JSON) was read directly: all 31 "seismic" occurrences are earthquake-hazard/outreach content plus one fact-sheet card. IGWS Digital Collections (`https://data.igws.indiana.edu/pages/search.php?search=seismic`) returns **84 results**, all reports, maps and photographs (incl. 2023 field photos of Vibroseis acquisition for CarbonSAFE Mitchell) — **no SEG-Y**. The only IndianaMap seismic layer is **"Seismic Refraction Data (1983)"** (ArcGIS item `0105b1d044a049759446ae6be8922d7f`) — *"seismic shot information (13,888 points) … to determine the depth to bedrock"*: **refraction, point geometry, not traces**. *(Free IN SEG-Y exists via ISGS and EDX — see §1.6(0) and §1.6(a2).)* | VERIFIED |
| **New York** | ESOGIS `https://esogis.nysm.nysed.gov/` ; NYSDEC `https://dec.ny.gov/environmental-protection/oil-gas` | **NO surface seismic — this contradicts the common premise that ESOGIS serves seismic line info.** Full site navigation enumerated (`/about-us`, `/maps-displays`, `/well-log-type`, a well-details page): **no seismic line layer, no shotpoint map, no SEG-Y**. What ESOGIS *does* have is a well-log type vocabulary containing **borehole** velocity entries — `3-D Velocity or Seismic Survey [V3D]`, `3-Dimensional Velocity [3DV]`, `Acoustic Velocity [AVL]`, `Dipole Sonic Imager [DSI]`, `Compressional to Shear Velocity Ratio [VPVS]` — i.e. **scanned wireline logs tied to individual wells**, not surface surveys. Access model is **free with registration**: the site says "All data is free to download", but a well-details page shows 24 scanned PDFs each gated behind **"Log In To Download"**. NYSDEC offers a `wellspublic.csv` of >40,000 wells and mentions neither seismic surveys nor geophysical exploration permits. *(See also the Newark Basin near-miss, §1.13.)* | VERIFIED |
| **Pennsylvania** | DCNR `https://www.pa.gov/agencies/dcnr/conservation/geology/publications-and-data` ; EDWIN `https://www.edwin.dcnr.pa.gov/` | **NO — and the well data itself is expensive.** DCNR's downloadable products are 1:250,000 bedrock shapefiles, the 1980 geologic map, PaGEODE, oil-and-gas wells, water wells and springs, coalbed-methane wells, quarries, sinkholes, earthquake epicentres — **no geophysical logs and no seismic**. PaGEODE covers "bedrock geology, surficial geology, quarries, water wells, and springs". **PA\*IRIS/WIS is retired**, replaced September 2016 by **EDWIN**, quoted verbatim: *"The initial subscription fee is **$5,000**, which covers the software license and initial training… An annual maintenance fee of **$500**…"* EDWIN is a *well* information system; neither its home page nor FAQ mentions seismic. 58 Pa.C.S. § 3222.1 speaks only generically of trade secrets under the Right-to-Know Law — no seismic-specific period found (**UNVERIFIED**). | VERIFIED |
| **Montana** (state agencies) | MBMG `https://mbmg.mtech.edu/` ; BOGC `https://bogapps.dnrc.mt.gov/dataminer/Default.aspx` | **NO from either state agency** — note this sits alongside the *federal* Kevin Dome release (§1.2), which is the DOE/BSCSP dataset, not an MBMG product. MBMG routes data through `https://gis-data-hub-mbmg.hub.arcgis.com/`; an ArcGIS Online search scoped to Montana returned **only** earthquake-seismology items from MBMG's own account. BOGC Data Miner exposes Wells (incl. cores/cuttings), Production, UIC, Leases, Statistics, CBM, Board Orders, Reference — **no seismic, no geophysical logs**. Rules (ARM Title 36 ch. 22, MCA Title 82 ch. 10–11) say nothing on seismic submission or confidentiality. Bell Creek field (Powder River Co.) on EDX offers only **derived RMS-amplitude rasters** in ESRI GRID (`w001001.adf` 77.9 MB; `clpMon2014.ovr` 8.4 MB) and a 2.4 MB JPG basemap of legacy line locations — **no traces**. *(`bogc.dnrc.mt.gov` no longer resolves; `mbmg.mtech.edu/publications/pubsearch.asp` 404s.)* | VERIFIED |

**Structural reason for the negatives.** None of these states has a statute compelling operators to
surrender seismic surveys to the state. Alaska's holding exists *only* because AS 43.55.025 made data
submission the price of a cash exploration tax credit; North Dakota gets *geometry* only because NDAC
43-02-12-06 requires a post-plot map, not traces.

**Confidentiality — a caution.** No statutory seismic-confidentiality provision was found in **TX, OK, MI,
OH, WV, KY, NY or PA**, and the structural reason is that none of those regulators requires seismic to be
filed at all. Only **Nebraska** was positively proven (zero "seismic"/"geophysical" in the full NOGCC rules
text). For the others, treat "no seismic confidentiality rule" as **not found**, not as *proven absent*.

### 1.11 Ohio — delisted legacy seismic (archaeology worth recording) (VERIFIED via Wayback)

Two Ohio seismic products existed on the legacy `geosurvey.ohiodnr.gov` site and are now gone from the
current catalogue:

1. **"Seismic Reflectivity Studies"** open-file category — despite the name, this is shallow seismic
   **refraction and MASW**: *"reports contain analyses, documents, and data from seismic refraction and
   multichannel analysis of surface waves (MASW) investigations performed in the state of Ohio by the Ohio
   Geological Survey"*, run since June 2002 for bedrock-depth and drift mapping, published as **~25 free
   county/township PDFs (0.7–1.8 MB each)** under `/portals/geosurvey/PDFs/Shallow_Seismic_Investigations/`,
   covering 15+ counties. Those PDFs **404 on the current asset host** and are absent from the catalogue.
   Archived snapshot: `geosurvey.ohiodnr.gov/open-file-materials-pgs/seismic-reflectivity-studies` (2019-05-05).
2. **COCORP profile across Ohio.** Archived page (2019-10-09), quoted verbatim: *"In the fall of 1987, the
   Consortium for Continental Reflection Profiling (COCORP) conducted a National Science Foundation-funded
   seismic-reflection profile across Ohio from the Indiana line to the Ohio River. The seismic profile (in
   three segments) and the location map are **no longer available from the Division of Geological Survey**.
   However, interested parties are encouraged to visit the Cornell University Institute for the Study of
   the Continents…"* — items 90–93 (Ohio 1, Ohio 1 continued, Ohio 2) all marked **OUT OF STOCK**.

Ohio's only true reflection product was resold **paper** COCORP sections, and it is gone. Route: **Cornell
INSTOC**.

### 1.12 Texas — the one BEG seismic that is publicly accessible, and one CC0 dataset (VERIFIED)

- **Devine Geophysical Test Site** — `https://www.beg.utexas.edu/about/facilities/dts/inventory`. Holds a
  BP legacy dataset described as *"crosswell and vertical seismic profiles, digital well logs, hardcopy
  data, and nearly 30 ft of full core… available for review and copy at the **EGL public-access data
  room** at the Bureau's headquarters in Austin."* This is **borehole seismic (VSP/crosswell),
  archive-visit-only** — not surface reflection — but it is the only agency-held seismic in TX/OK/NE/MI/OH/WV
  explicitly described as open to the public.
- **Texas Data Repository**, `https://dataverse.tdl.org/citation?persistentId=doi:10.18738/T8/ROWA0Y` —
  *"UT Austin BEG Reports to TXRRC for Seismic Data Acquisition and Fault Mapping Project"*, BEG/CISR ↔ RRC
  interagency contract 455-24-1012. **CC0-1.0, free, 40 files**, largest ~27 MB: 3D-seismic *interpretation*
  reports plus fault-slip-potential shapefiles. **No SEG-Y** — the underlying 3D volumes were licensed, not
  released. Cleanest licence of any Texas item, but interpretive products only.

### 1.13 "Seismic was acquired but the traces were NOT deposited" — near-misses (VERIFIED)

| Project / state | What was acquired | What is actually public | Status |
|---|---|---|---|
| **Newark Basin, NEW YORK / NJ / PA** — Sandia Technologies + Conrad Geoscience. EDX `characterization-of-the-triassic-newark-basin-for-storage-of-carbon-dioxide` | "an integration of **seismic**, geologic, borehole, and formation core results"; two cored test wells incl. the 2011 **1-NYSTA Tandem Lot** | `NewarkBasinDatabase.zip`, **31.49 GB, 8,507 entries** — central directory listed by range request: **zero `.sgy`/`.segy`**. Content: 3,078 JPG (8.39 GB), 1,146 PDF (11.03 GB), 205 SHP + 138 gdbtable, 157 LAS (0.14 GB), 142 TIF, 96 PDS, 88 MXD. Folders: `FieldWork` 23.61 GB, `GIS_Project_TriCarb-Final` 7.75 GB, `Phase I Characterization` 6.94 GB, `References`, `Presentations-Outreach`, `Phase II Characterization`, `Project Base Maps` | **VERIFIED negative** |
| **Rock Springs Uplift, WYOMING** — WY-CUSP, University of Wyoming. EDX `site-characterization-of-the-highest-priority-geologic-formations-for-co2-storage-in-wyoming` | "drilled a stratigraphic test well and acquired a **3-D seismic survey covering 25 square miles**"; 916 ft of core from a 12,810-ft well | The only resource is `UniversityofWyoming.zip` at **21,544 bytes (21 KB)**. The 3D survey was **not** deposited. | **VERIFIED negative** |
| **Wilmington Graben, CALIFORNIA** — GeoMechanics Technologies. EDX `wilmington-graben-offshore-los-angeles` | "analyzed and interpreted **existing** geophysical data" | **31.7 MB** ZIP — interpretation products only, no trace data | **VERIFIED negative** |

---

## 2. Canada — by province / territory

### 2.1 Summary

| Jurisdiction | Agency | Publishes seismic? | 2D/3D | Format | Volume | Access | Licence | Statutory confidentiality | Status |
|---|---|---|---|---|---|---|---|---|---|
| **British Columbia** | **Geoscience BC — Nechako Basin** | **YES — free direct-download SEG-Y** | **2D**, 7 lines | **SEG-Y** (structure stack + migration), zipped; + PDF plots + acquisition package | **1,911,553,723 B = 1.78 GiB** of SEG-Y in 14 zips; ~330–350 line-km | **`free-dl`, no registration** (all 14 URLs HTTP 200 verified) | **NO licence statement anywhere — verified absence** | n/a (not a regulatory filing) | VERIFIED |
| **British Columbia** | BC Energy Regulator | **NO** reflection; "seismic" = induced-seismicity catalogues | — | — | 131 data-centre items, none seismic reflection | free | — | **PNG Act s.122(2) — NO EXPIRY**; release only by Order in Council or owner's written consent | VERIFIED |
| **Alberta** | AER | **NO** — regulates seismic *programs*, never collects trace data | — | — | — | — | — | **None.** Exploration Regulation AR 284/2006 contains **zero** occurrences of "confidential" | VERIFIED |
| **Alberta** | Alberta Geological Survey | **NO SEG-Y** — seismic *line locations* + earthquake catalogues only | line geometry | SHP/GeoJSON/KML/CSV/GPKG/GDB — **no SEGY format in the catalogue** | 41 open datasets; 3 mention seismic | `free-dl` | **Open Government Licence – Alberta** | n/a | VERIFIED |
| **Saskatchewan** | Ministry of Energy and Resources | **ONLY-SCANNED-IMAGES** — interpreted seismic time-structure / contour maps | 2D-derived contour maps | scanned **PDF in ZIP**, 300 dpi. **No SEG-Y** (0 hits across 62,557 catalogue products) | **74** Seismic Time Structure Map downloads + **44** Gravity Seismic Maps + ~12 regional sheets; files 1–29 MB | **`free-dl`, price $0.00, no account** | Government of Saskatchewan, with disclaimer | **1 year after the permit expires, is surrendered in its entirety or is cancelled** (Crown Minerals Act regs) | VERIFIED |
| **Saskatchewan** | PTRC **Aquistore** | **NO** — partners only | 3D/3C + DAS | — | >620,000 t CO₂ injected at 3.4 km | **`request`** — "PTRC offers investing partners access to its datasets" | not published | — | VERIFIED |
| **Manitoba** | Petroleum Branch | **ARCHIVE-VISIT-ONLY** — seismic filed under Geophysical Licences, held in Winnipeg | mostly 2D vintage | paper/analogue; nothing digital | **165 geophysical licences, 1947–1980** | **`onsite`**, **$50.00 per hour** for research and reproduction | — | **M.R. 110/94 s.20(1): 1 year / 3 years / 10 years** — the clearest statutory clock in Canada | VERIFIED |
| **Ontario** | Ontario Geological Survey | **NO trace data** — a seismic **line-location index** only, and it redirects users to federal NRCan | 2D line geometry | ESRI shapefile (`seismic.zip`, 120,214 B, Apr 2013) + KML | **85 line records** | `free-dl` | Ministry Terms of Use | n/a | VERIFIED |
| **Ontario** | Oil, Gas and Salt Resources Library (OGSRL) | **NO seismic in the free tier**; free "Geophysics **Locations** Shapefile" (500 KB, 2012) is line locations. Geochemical/Geophysical Exploration Reports are **members-only** | 2D locations | SHP/CSV/XLSX; no SEG-Y | 27,000+ well records, 13,000+ cuttings sets, 1,000+ cores | **`fee`** — Personal **$660/yr**, Corporate **$1,925/yr**; remote requests billed on labour + reproduction | *"may not copy, distribute, resell, or reproduce in other media"* | n/a | VERIFIED |
| **Québec** | MRNF/MEIE, **SIGPEG** | **YES but NOT free** — categories "Seismic (field data)" + "Seismic (processed data)" | 2D (onshore + Gulf) | **SEG-Y**, SEG-D field data, raster TIF, SHP nav | not published | **`fee`** — SEG-Y **$59**, SEG-D **$413**, raster **$29.50**, province-wide line SHP **$1,179**; reports free. CAPTCHA gate, no login | Restrictive **MEIE end-user licence** — internal use only, no resale or transfer | Reprocessed data public **3 yrs** after the request date; *Loi sur les hydrocarbures* repealed 23 Aug 2022 | VERIFIED |
| **Nova Scotia** | Dept. of Energy (onshore) | **ONLY-SCANNED-IMAGES + nav** — the Dept. holds the SEG-Y in-house | **2D + 2 × 3D** | Section images in PDF (captioned "Format: SEGY"); nav = **shapefile**; logs = **LAS** | **~45 surveys 1942–2013, ≈4,900 line-km**; 165 published line displays; 3D 52.7 km² + 62.8 km² | **`free-dl`**, no registration | *"considered public information and may be distributed or copied"* (credit requested) | not stated on site | VERIFIED |
| **Newfoundland & Labrador** | **C-NLOER** Data & Information Hub (offshore) | **YES — SEG-Y released free on request** | **153 × 2D + 195 × 3D programs** | **SEG-Y** + scanned inventory + shapefiles | **348 programs, 1964–2020** | Inventory/shapefiles `free-dl`; **SEG-Y free by e-mail** to `information@cnlopb.ca` | Click-through disclosure agreement (indemnity, no warranty) | Accord Act s.119(5)(d)(ii): **5 yrs**; non-exclusive/multi-client **15 yrs** (5 privilege + 10 confidentiality) | VERIFIED |
| **Newfoundland & Labrador** | Provincial (GSNL / Energy & Mines) | **Bibliographic only** — Western NL Geoscience DB indexes "seismic data" | — | publication links | ~3,300 records | free | Crown copyright | — | VERIFIED (partial) |
| **Yukon** | YGS / EMR Oil & Gas | **Metadata only — NO trace data** | 2D line geometry | **XLS** seismic line coordinates + attributes; GeoYukon seismic-line layer | lines cut **1961–1984** (NEB source); 692.5 KB XLS | **`free-dl`** | Government of Yukon copyright | *Oil and Gas Act* s.103 — all records confidential except as regulations provide (periods UNVERIFIED) | VERIFIED |
| **Northwest Territories** | **OROGO** (+ NTGS) | **ONLY-SCANNED-REPORTS** (free) — no SEG-Y | 2D | **scanned PDF** survey reports | **573 seismic programs** of 1,201 total, **1943–2013** | **`free-dl`** per program | GNWT | *Oil and Gas Operations Act*: **5 yrs** after completion; **15 yrs** for non-exclusive surveys | VERIFIED |
| **New Brunswick** | DNRED, Minerals & Petroleum | **NO** — "Petroleum Data" is well reports, rights maps, production/royalty stats only | — | — | — | request to Dept. only | — | Reg. **86-191 s.7(1)(a)**: data become Crown property; Minister **may** release **1 yr after licence termination** | VERIFIED |
| **Nunavut** | CNGO (+ NIRB) | **NO** — no petroleum or seismic series at all | — | — | — | — | — | — | VERIFIED |
| *(federal, all provinces)* | **NRCan LITHOPROBE / GLIMPCE / Arctic FGP** | **YES — free SEG-Y** covering AB, BC, ON, QC, SK, MB, NWT, YT, NL | 2D deep-crustal | **SEG-Y** (STACK / MIG / FK MIG / FX DEC / SEMBL / MIG FIL) | **1,893 `.sgy` files across 12 transects** | **`free-dl`**, anonymous HTTPS | **Open Government Licence – Canada** | n/a (GSC-collected) | VERIFIED |

### 2.2 British Columbia — Geoscience BC Nechako: confirmed, with every link checked (VERIFIED)

The widely-cited claim is **TRUE**. Landing pages, both live:
`https://www.geosciencebc.com/major-projects/nechako-seismic/` and
`https://www.geosciencebc.com/reports/gbcr-2009-09/` (Geoscience BC Report 2009-09, project 2007-N004,
A.J. Calvert, Simon Fraser University).

Verbatim from the page: *"Refer to map to select appropriate line data and image downloads… Click on
'Structure Stack' and 'Migration' links below for each line to download zip files containing seismic data
in **SEGY format**."*

**Survey:** vibroseis 2D, acquired **July 2008**, **$2.5 M** ($2.0 M Geoscience BC + $0.5 M Northern
Development Initiative Trust Pine Beetle Recovery Account). ~**350 line-km** per the page (the 2009 release
stated **330 line-km**). **Seven lines released**: 2008-05, -06, -10, -11, -12, -13, -15.

All 14 SEG-Y zips HEAD-checked — **every one HTTP 200, `Content-Type: application/zip`, no authentication**:

| Line | Structure stack (bytes) | Migration (bytes) |
|---|---|---|
| 2008-05 | 121,760,910 | 122,158,859 |
| 2008-06 | 106,963,942 | 107,407,703 |
| 2008-10 | 235,518,116 | 236,890,679 |
| 2008-11 | 79,537,339 | 79,919,136 |
| 2008-12 | 118,386,858 | 119,173,837 |
| 2008-13 | 246,684,791 | 248,023,021 |
| 2008-15 | 44,455,479 | 44,673,053 |
| **TOTAL** | **1,911,553,723 B = 1.78 GiB** | |

URL pattern: `https://cdn.geosciencebc.com/project_data/NechakoSeismic/Data/{5,6,10,11,12,13,15}.U-{STR,MIG}.zip`
Also live: compressed plots `https://cdn.geosciencebc.com/project_data/NechakoSeismic/Images/NEC{5,6,10,11,12,13,15}.zip`
(~108 MB total); line map `.../Map_Seismic_Lines.pdf` (1,849,653 B); **acquisition data package**
`https://www.geosciencebc.com/i/project_data/GBCReport2009-09/GBCR_2009-09_Seismic_Acquisition_Data.zip`
(**155,700,936 B**).

**Prestack is by request, not download**, quoted verbatim: *"Prestack data can also be provided on request
at cost of reproduction as uncorrelated field records (SEGD), correlated unprocessed shot gathers (SEGY),
and processed CDP gathers (SEGY). Please contact Andy Calvert at acalvert@sfu.ca."*

> **LICENCE WARNING — a verified absence.** There is **no licence, terms-of-use, copyright or disclaimer
> statement on the Nechako page**. The raw HTML (104,815 B) was grepped for `terms|disclaimer|licen|copyright`
> and for any `©` text: **zero matches**; the only legal link is a cookie/privacy notice.
> `https://www.geosciencebc.com/terms-of-use/` returns **404**. A downloaded Geoscience BC report PDF carries
> only a citation line. **Practical read: free public data with no stated licence — get written confirmation
> from Geoscience BC before commercial redistribution or model training.**

**Correction to the "2008 *and 2011*" premise: only the 2008 acquisition was released as SEG-Y.** The
2011/2012 Nechako outputs are reports and theses only — GBCR **2012-13** (Talinga & Calvert, tomographic
velocity + reflection, 78 pp PDF), GBCR **2012-14** (Farquharson, airborne EM + **reprocessing of vibroseis
data** — *the reprocessed data itself is not published*), project **2006-028** (passive/teleseismic, 7
broadband stations over ~33,000 km² — not active-source). No download was found for Geoscience BC's
reprocessing of the legacy 1980s Canadian Hunter Nechako lines — **UNVERIFIED** whether it was ever posted.

**Geoscience BC's other "seismic" is passive.** The 2020–21 Kiskatinaw / NEBC releases (project 2019-005)
are **earthquake/induced-seismicity waveforms** from a dense seismograph network, distributed through
**IRIS** after a **91-day embargo**. No Montney, Horn River or geothermal *reflection* SEG-Y was found.

**BC statutory confidentiality — strict and open-ended.** Petroleum and Natural Gas Act, RSBC 1996 c.361
(`https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96361_01`):
- **s.1** — geophysical exploration is *"investigation of the subsurface by seismic, gravimetric, magnetic,
  electric and geochemical operations… but does not include the use of geophysical well logs, vertical
  seismic profile surveys or other surveys obtained from a well"*.
- **s.122(2)** — *"Geological, geophysical and reports other than well reports and well data received by
  the ministry… and designated by the minister as confidential, **must not be released except under an
  order of the Lieutenant Governor in Council**."*
- **s.122(3)** — release is possible *"with the permission in writing of the person who holds the licence,
  permit or lease"*.
- **s.47(3)** — on exploration-permit renewal, requires *"a report and map displaying the detailed factual
  data obtained from the geological or geophysical examination"*.

**Crucially, BC's confidentiality has NO expiry.** Unlike Manitoba or Saskatchewan there is no statutory
clock. The **Geophysical Exploration Regulation, B.C. Reg. 280/2010**
(`https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1215528698`, replaced B.C. Reg. 361/98 on
4 Oct 2010) covers progress reports, final plans within 60 days, shot-hole plugging, damage remediation —
and contains **no data-submission, retention, confidentiality or public-release provisions** for the data.

### 2.3 Alberta — explicit negative, and a widely-repeated myth corrected (VERIFIED)

**AER holds no seismic trace data and publishes none.** The consolidated **Exploration Regulation, Alberta
Regulation 284/2006** (`https://kings-printer.alberta.ca/documents/Regs/2006_284.pdf`, 48 pp, consolidated
to AR 142/2025) was downloaded and text-extracted:
- It is a **surface-disturbance and licensing instrument** — shot holes, test holes, recording, trails,
  timber, road damage, reclamation, letters of clearance.
- It contains **no requirement to file seismic traces, sections or processed data** with the Crown.
- **`grep -c -i "confiden"` = 0.** There is no confidentiality provision at all.
- The only disclosure provision, **s.13** verbatim: *"Release of program information — Subject to the
  Exploration Directive, the Minister may release information collected in relation to an approved
  exploration program."* That is program metadata, not data.

> **MYTH CORRECTED — there is no Alberta 5-year seismic confidentiality rule.** The well-known 5-year clock
> is **federal**: **s. 101 of the Canada Petroleum Resources Act**, applying to frontier lands and the East
> Coast offshore Accord regime — privilege lapses *"after the expiration of five years following the date
> of completion of the work"*, with administrative extensions (NEB added 10 years for non-exclusive spec
> data → 15 total; C-NLOPB added 5 → 10 total). After expiry the boards may **copy and distribute** the
> data without compensating the creator — the point litigated in *Geophysical Service Inc. v. EnCana*
> (heard in Alberta courts, which is the only Alberta connection).
> Background: `https://ablawg.ca/2016/04/27/expiration-of-confidentiality-also-gives-boards-the-liberty-to-copy-and-distribute/`

**AGS has no SEG-Y.** The AGS ArcGIS open-data DCAT catalogue
(`https://geology-ags-aer.opendata.arcgis.com/api/feed/dcat-us/1.1.json`, 254,828 B) lists **41 datasets**
whose distribution formats are limited to *ArcGIS GeoServices REST API, CSV, GDB, GPKG, GeoJSON, KML, TXT,
Web Page, XLSX, ZIP* — **SEGY is not among them**. Only three mention seismic:
- **Lithoprobe Seismic Transects** — *"The location of reflection seismic lines acquired on the three
  LITHOPROBE transects in Alberta… include the Peace River Arch Industry Seismic Experiment (PRAISE)
  carried out in 1994, which collected a total of 654 km of reflection data in nine different line segments
  (lines 11–20)…"* — **locations only**.
- **Subsurface Lineaments** — *"faults interpreted by different oil and gas operators based on their
  seismic studies and provided to the Alberta Energy Regulator"* — **interpretations, not data**.
- **Alberta Earthquakes** — earthquake catalogue.

AGS publication searches for `seismic`, `seismic reflection`, `vibroseis`, `seismic survey SEG-Y` returned
**only induced-seismicity/earthquake products**. The **DIG series** is GIS/tabular geology, mineral
occurrences and drillhole compilations. **No public Quest or Alberta No.1 SEG-Y found.** The Geothermal
Atlas of Alberta (Dec 2024, `https://gaa-v1-ags-aer.hub.arcgis.com/`) is formation/temperature grids.

**Verdict: seismic in Alberta is privately owned and commercially brokered; it is never filed with the province.**

### 2.4 Saskatchewan — free scanned seismic maps under a genuine statutory disclosure rule (VERIFIED)

**The Seismic Exploration Regulations, 1999 (M-16.1 Reg 2)**
(`https://pubsaskdev.blob.core.windows.net/pubsask-prod/2157/M16-1R2.PDF`, 28 pp) was downloaded and
text-extracted: it governs licences, explosives permits, preliminary plans, notices, restoration, and
**s.28 "Final reports and maps"** (observer's report, shot-hole coordinates, misfires, Form B within 60
days). **`grep -c -i "confiden"` = 0.** No trace data is filed under these regulations.

**But under The Crown Minerals Act, interpreted seismic maps DO become public — and are free.** Verbatim
from the Saskatchewan Publications Centre record for **"Seismic Time Structure Maps"** (product 82468):

> *"Seismic time structure maps submitted for permit expenditure credit as provided by regulation under The
> Crown Minerals Act are **made available to the public one year after the permit expires, is surrendered in
> its entirety or is cancelled**. The regulations require a presentation of data in profile or contour or any
> other form best suited to determine its significance, including contour maps on the most dependable and
> continuous reflecting horizon above, at and below the top of the Paleozoic…"*
>
> *"Individual time structure maps dating as far back as the 1940's have been scanned and are made available
> as PDF files in zipped folders."*
>
> *"Note that the volume of maps submitted for credit dropped substantially after 1995 with the introduction
> of two new disposition types, Exploration Licences (ELs) and Special Exploratory Permits (SEPs)…"*

Companion product 82463, **"Gravity Seismic Maps"**: *"The individual block maps have been scanned from the
Ministry of the Economy's seismic archives ranging from the 1940s to 1970."*

**Verified free downloads** (all `price: 0.00`, `DIGITAL`, no account):
- Product **82468** — **74 downloadable formats**. Reference Grid = `application/pdf`, 6,317,661 B;
  "Block 01 – 01SC040 to 62" = `application/zip`, 28,692,607 B.
- Product **82463** — **44 downloadable formats**. Block 01 = `application/zip`, 1,013,811 B.
- Scanned regional sheets, 300 dpi: **N-1 Regina** (`application/pdf`, 4,507,757 B), N-2 Swift Current,
  N-3 Yorkton, N-4 Saskatoon, N-5 Prince Albert, N-6 North Battleford, N-7 Buffalo Narrows, SD-1 Souris
  River, SD-2 Big Muddy Lake, SD-5 Moose Mountain, SD-6 Lake of the Rivers, SM-1 Souris Lake.

Download URL pattern (verified 200):
`https://publications.saskatchewan.ca/api/v1/products/{productId}/formats/{formatId}/download` ·
human-facing `https://publications.saskatchewan.ca/#/products/82468`

**No SEG-Y in Saskatchewan.** The full publications catalogue (`https://publications.saskatchewan.ca/api/v1/products`,
40,228,141 B, **62,557 products**) was downloaded and searched locally: **`seg-y` = 0, `segy` = 0,
`seg y` = 0**. 70 products have "seismic" in the title — regulations, Athabasca Basin refraction and EXTECH
IV McArthur River high-resolution seismic *reports*, LITHOPROBE summaries, Prairie Evaporite papers, and
the scanned map series above.

**Aquistore (PTRC, near Estevan) is NOT public.** `https://ptrc.ca/aquistore` (aquistore.ca 301s here).
>620,000 t CO₂ injected at 3.4 km from SaskPower's Boundary Dam; the site references *"3D/3C seismic
surveys"* and DAS fibre imaging, but states **"PTRC offers investing partners access to its datasets"**
through a Scientific and Engineering Research Committee process. **No public download, no published licence
terms.** Contact info@ptrc.ca.

### 2.5 Manitoba — the clearest statutory clock in Canada, but paper-only (VERIFIED)

**Geophysical Regulation, M.R. 110/94** under The Oil and Gas Act (C.C.S.M. c. O34), registered 6 June 1994
— `https://web2.gov.mb.ca/laws/regs/current/110-94.php` (page downloaded, English text extracted):

> **s.19(1)** — within 60 days of completion the licensee submits a final report: dates; summary of field
> operations; **two copies of the map** showing licence number, deviations, *"the location of any sample
> station, recording station, or shot hole or other energy source"*, and constructed trails/roads; for each
> shot hole the ground elevation, depth and *"the presence of any gas, oil, water, coal, gravel, sand or
> other useful or potentially useful product"*; **(e)** *"the result of any gravity, magnetic, electrical,
> radioactivity or geochemical survey…"*; **(f)** expenditures.
>
> **s.19(2) "Submission of maps or processed data sections"** — *"The licensee may or, at the request of the
> director, shall submit maps or processed data sections based on data obtained from the geophysical
> operation."*
>
> **s.20(1) "Confidentiality of information in final report"** — *"The director shall hold confidential any
> information submitted under section 19, for the following periods of time from the day on which the
> geophysical operation is completed: (a) under clauses 19(1)(a) to (d), for **one year**; (b) under clause
> 19(1)(e), for **three years**; (c) under subsection 19(2), for **10 years**."*
>
> **s.20(2)** — expenditure information *"shall not be released other than as part of general statistical
> information."*

**So Manitoba is the one jurisdiction with an explicit statutory clock on processed seismic sections: 10
years from completion.** Note that submitting processed sections is discretionary unless the director
requests them (s.19(2)), so coverage is uneven.

**What is held:** `https://www.manitoba.ca/iem/petroleum/pubcat/geologic.html` — geological data from
structure test holes, core holes and wells; **seismic data submitted under Geophysical Licences and
Reservations**; other geophysical data (magnetic, gravity, radiation). **165 geophysical licences, 1947–1980**
— Licence 1 (California Standard, 1947) through Licence 165 (International Minerals & Chemical, Dec 1980).
Fee verbatim: *"Information researched and reproduced from these files will be charged a rate of **$50.00
per hour**."* Nothing is downloadable. MGS free publication downloads and the Data MB / geoportal.gov.mb.ca
open-data portal carry reports, maps and GIS — **no seismic traces**.

### 2.6 Ontario — a 117 KB index; the actual traces are federal (VERIFIED)

The single Ontario open-data hit for "seismic" is **"Geophysical dataset index"** (org "Energy and Mines"),
`https://data.ontario.ca/dataset/geophysical-dataset-index`, KML at
`https://www.geologyontario.mndm.gov.on.ca/mines/data/google/geophysicalatlas/OntarioGeophysics.kml`.

That KML (58,388 B) was downloaded; its "Seismic and Magnetotelluric Data" folder description, verbatim:

> *"Seismic and Magnetotelluric data have been acquired under a number of different federal and provincial
> programs and partnerships. **To access data please visit webpage here [http://www.geogratis.gc.ca/] or
> contact 613-992-5179 broberts@nrcan.gc.ca**"*

Its one download button → `http://www.geologyontario.mndm.gov.on.ca/mines/data/gdsatlas/seismic.zip`
(**120,214 B**, HTTP 200), which contains only `seismic_LL_NAD83_Apr2013.{shp,shx,dbf,prj,sbn,sbx,shp.xml}`
— an ESRI line shapefile with **85 records** and three attributes (`Line_ID`, `SURVEYTYPE`, `STUDY`):

| STUDY | lines | | SURVEYTYPE | lines |
|---|---|---|---|---|
| LITHOPROBE | 26 | | REFLECTION | 71 |
| LAKE HURON REFLECTION | 22 | | REFRACTION | 9 |
| SOUTHERN ONTARIO REFLECTION | 9 | | (blank) | 5 |
| Discover Abitibi | 9 | | | |
| GLIMPCE | 7 | | | |
| FALCONBRIDGE-TEMAGAMI | 3 | | | |
| ABITIBI/GRENVILLE | 3 | | | |
| LAKE ONTARIO (+ reflection) | 3 | | | |
| LAKE ERIE REFLECTION | 2 | | | |

**OGSRL (London, ON)** — `https://www.ogsrlibrary.com/data_free_petroleum_ontario`. **Free tier:** Petroleum
Well Data (XLSX 10 MB / CSV 5 MB), Petroleum Pools shapefile (5.0 MB), **Geophysics Locations shapefile
(500 KB, last updated 2012)**, Wireline Log Locations CSV (3.8 MB), Wireline Log Raster Database, Digital
LAS Curves Index, Google Earth KMLs. **Members-only:** annual production, **Geochemical/Geophysical
Exploration Reports**, core analyses, Base Data Package (1.2 GB SHP), bedrock faults, horizontal well paths,
salt unit extents, Leapfrog 3D models. **No seismic dataset in either tier** — "Geophysics Locations" is line
locations; "geophysical" in the well-record context means **wireline logs**. Holdings: *"cutting samples from
over 13,000 wells, core from nearly 1000 wells, and file information on over 26,000 wells."*
Costs: Personal **$660/yr**, Corporate **$1,925/yr**; remote requests *"based on labor time and reproduction
costs."* Licence verbatim: *"The User may only use the Licensed Material… for its own internal use, and may
not copy, distribute, resell, or reproduce in other media."* — restrictive; blocks redistribution in a
derived product. *(Caveat: `www.ogsrlibrary.com` began refusing connections partway through the pass —
ECONNREFUSED on 192.254.184.122:443. The two page fetches reported here succeeded earlier; a re-check is
worthwhile.)*

### 2.7 Québec — SIGPEG is alive, but the SEG-Y is NOT free (VERIFIED; corrects a common premise)

> **Québec is a false positive.** SIGPEG does hold SEG-Y, but it **sells** it under a restrictive
> internal-use licence. Only the *reports* are free.

**Current working URL: `https://sigpeg.mrn.gouv.qc.ca/`** — **not** `sigpeg.mrnf.gouv.qc.ca`, which refuses
connections. The root meta-refreshes to `https://sigpeg.mrn.gouv.qc.ca/gpg/classes/igpg`, behind a
**7-character image CAPTCHA** (no login, no fee to browse; a BIG-IP WAF rejects deep links). The catalogue
contents are therefore **UNVERIFIED**, but everything below is verified from live or archived pages.

Seismic is definitely in SIGPEG: the help page lists search categories *"GIS data / **Seismic (field data)**
/ **Seismic (processed data)**"*, and the live app has a `facette=SISMI` facet.

**The live price list** — `https://sigpeg.mrn.gouv.qc.ca/gpg/pdf/Price_list.pdf`, effective **1 Jan 2022**:

| Product | Format | Price |
|---|---|---|
| Field work reports — geological / **geophysical** / drilling | pdf | **FREE** |
| Seismic **field data** | SEG-D | **$413.00** |
| Seismic **processed data** | **SEG-Y** | **$59.00** |
| Seismic **raster** | tif | **$29.50** |
| Shot points & seismic lines database (entire Québec) | shp | **$1,179.00** |
| regional subsets A-B / C / D / F / G | shp | $590 / $236 / $296 / $178 / $178 |
| Well logs / composite well log | las / pdf | $29.50 / $59.00 |

*(The table has no unit column — whether the SEG-Y price is per line or per survey is **UNVERIFIED**.)*

**Free viewing layer:** the interactive hydrocarbons map at
`https://hydrocarbures.portailcartographique.gouv.qc.ca/` shows *"les levés sismiques et les puits"*, is
*"consultée gratuitement et ne nécessite aucune authentification"*, and exposes a free WMS named
`HYDROCARBURE_WMS`. Per the official user guide, only *permis de recherche, baux d'exploitation, régions
géologiques* are shapefile-downloadable — **the seismic-line layer is view-only** (you buy it for $1,179).

**Confidentiality / reprocessing rule (VERIFIED, SIGPEG "Avis à la clientèle"):** the Ministry holds the
**original field seismic tapes**. To reprocess, you file a form; MRN ships the originals to your chosen
processing centre; you must return a TIF raster plus **a SEG-Y file for each processing sequence**, and
*"Les fichiers issus du retraitement des données originales de terrain deviendront **publiques trois ans**
après la date de réception de la demande dûment complétée."* — **reprocessed data becomes public 3 years
after the request.**

**Licence:** `https://sigpeg.mrn.gouv.qc.ca/gpg/hydrocarbures/Licence_utilisation.pdf` — a *"Licence de droit
d'auteur pour l'utilisation finale"* granted by **MEIE** (energy moved from MRNF to the Ministère de
l'Économie, de l'Innovation et de l'Énergie). Non-exclusive, non-transferable, **end-user/internal use
only**; no resale, lending or transfer to third parties; must credit "© Gouvernement du Québec".
**Not an open licence.**

**Statute:** the *Loi sur les hydrocarbures* (RLRQ **c. H-4.2**) was **repealed 23 August 2022**; the title
was replaced by the *Loi sur le stockage de gaz naturel…* (c. S-34.1). Line/line-km/GB counts are not
published anywhere reachable — **UNVERIFIED**.

### 2.8 Nova Scotia — the best free *provincial onshore* package in Atlantic Canada (VERIFIED)

**Onshore Petroleum Atlas (2017)** — `https://novascotia.ca/onshore-atlas/`, all free direct downloads,
no registration:

- **OFR 2017-07 "Schedule of 2D Seismic Data, onshore Nova Scotia"**, Parts 1–3 (Cape Breton 103 MB,
  Cumberland 158 MB, Windsor 63 MB PDFs) — **165 uninterpreted seismic line displays** (48 + 84 + 33), each
  captioned `Line Name / Survey / Year / Operator / Type: 2D / **Format: SEGY** / Vintage: STK / CRS: NAD83
  UTM 20 / CDP range / well ties`. **This confirms the Department holds the SEG-Y; only the raster is
  published.** Appendix 2 lists **45 surveys, 1942–2013** (Cape Breton Petroleum 1942 → CCSNS 2013;
  operators incl. Chevron, Gulf, SOQUIP, Pacific Petroleum, Northstar, Husky, Elmworth, Forent, Petroworth).
  Summed ≈ **1,298 km (Cape Breton) + 2,195 km (Cumberland) + 1,398 km (Windsor) ≈ 4,900 line-km**
  *(approximate — the PDF table columns are imperfectly aligned)*. Includes **two 3D surveys**: Husky
  Shubenacadie 3D (**52.7 km²**) and Elmworth Windsor 3D (**62.8 km²**).
- **OFR 2017-11 "Navigation data for 2D seismic lines"** — Parts 1–3, **shapefile ZIPs**, free.
- **OFR 2017-06 "Seismic Interpretation in the Windsor Basin"** incl. Appendix 3 composite interpreted sections.
- **OFR 2017-09** well log **LAS** files; **OFR 2017-08** Schedule of Petroleum Wells; **OFR 2017-10** petrophysics.
- **Licence** (bundled `Disclaimer.txt`): *"Information contained with this electronic publication is
  **considered public information and may be distributed or copied**… We request that Public re-use of these
  materials bear a Nova Scotia Department of Energy byline/credit line."* — effectively open with attribution.

**Provincial offshore extras (beyond CNSOPB/CNSOER):**
- **Play Fairway Analysis 2011** — `https://novascotia.ca/play-fairway-analysis-2011/`; HTTP-HEAD verified:
  `3D_Seis_Interp.zip` **295.7 MB**, `2D_Interp_Line_CDP_XY_TWT.dat.zip` **116.2 MB**, `ARC-GIS-Data.zip`
  **279.0 MB**, plus TWT/TVDSS/ISOPACH grids, synthetics, time-depth data, 14 annexes, well packages.
  **This is seismic *interpretation* (horizons/grids/nav), not SEG-Y traces.**
- **Scotian Basin Integration Atlas 2023** — `https://novascotia.ca/scotian-basin-integration-atlas/`,
  7 chapters + 7 appendices, **PDF only**.
- Others via `https://novascotia.ca/offshore-oil-and-gas-geoscience-research/`: Laurentian Sub-basin 2014,
  SW NS Expansion 2015, Central Scotian Slope 2016, Sydney Basin PFA 2017, Shelburne Post-Mortem 2019.
- The **Geoscience & Mines Branch** (`https://novascotia.ca/natr/meb/`) is minerals-only — **no petroleum or
  seismic**. Onshore SEG-Y is presumably obtainable from the Dept. of Energy / Core Library
  (`https://novascotia.ca/natr/meb/information-services/core-library.asp`) — **UNVERIFIED**.
- The *Petroleum Resources Act* is being replaced by the **Subsurface Energy Resource Extraction Act**
  (introduced Feb 2026).

### 2.9 Newfoundland & Labrador — C-NLOER: free SEG-Y on request, with a dated unlock schedule (VERIFIED)

**Provincial side is thin.** Dept. of **Energy and Mines** `https://www.gov.nl.ca/em/` (`gov.nl.ca/iet/`
now redirects here). The **Western Newfoundland Geoscience Database**
(`https://www.gov.nl.ca/em/energy/petroleum/search-publications/`, app at `https://docs.gov.nl.ca/nr/`) is
~**3,300 geoscientific publications** for the Paleozoic basins (Anticosti, Bay St. George, Deer Lake,
Sydney, St. Anthony); the page says it *"contains information and links to digital files such as: **seismic
data**; gravity and magnetic data; well logs and well reports"*, and its vocabulary includes "seismic data",
"seismic surveys", "seismic stratigraphy". **The search form is session/CSRF-protected and returned no
results — whether it links to actual seismic files is UNVERIFIED.** It is a bibliographic index, not a repository.

**The offshore regulator is the real source.** C-NLOPB is now **C-NLOER** (`https://www.cnlopb.ca/` →
`https://www.cnloer.ca/`). Geoscience moved to the **Data and Information Hub**,
`https://home-cnlopb.hub.arcgis.com/`, geophysical page `https://home-cnlopb.hub.arcgis.com/pages/geophysical`.

Parsing the page's ArcGIS item data: **153 × 2D and 195 × 3D seismic programs, 1964–2020 (348 total)**, each
row giving *Program Number, Authorization Number, Year, Operator, **Inventory Release Date**, **SEGY Release
Date**, "Inventory & SEGY" (View), Shapefile (Download)*.

- Per-program pages carry a click-through **Disclosure Agreement** (indemnity, no warranty, NL law).
- Older programs say **"No SEGY Available"** but expose free scanned inventory — operations, processing and
  interpretation reports, shotpoint maps, raster crossline/inline displays.
- Programs with SEG-Y say: **"To obtain SEGY file(s) forward e-mail to `information@cnlopb.ca` indicating
  geophysical program number."** **No fee is stated anywhere in the policy — free, request-only.**

**Statutory rule (VERIFIED)** — *Canada–NL Atlantic Accord Implementation Act* s.119(5)
(`https://laws-lois.justice.gc.ca/eng/acts/C-7.5/section-119.html`): exploratory wells **2 years** after
well termination; geological/geophysical work *"after the end of **five years** following the date of
completion of the work"* (s.119(5)(d)(ii)). The **Disclosure of Digital Data and Information Policy**
elaborates: *"digital geophysical data (such as SEG-Y) will be disclosed following a **five year Privilege
Period**"*; *"Non-exclusive geophysical Digital Data (for example, SEG-Y) will be disclosed following a
**15 year Non-disclosure Period** comprised of a five year Privilege Period and a 10 year Confidentiality
Period."*

> **ACTIONABLE — the Nalcor question answered.** The Nalcor-commissioned multi-client surveys appear under
> operator **"Multi Klient Invest (MKI)"** — **28 programs, 2011–2020**, all non-exclusive → 15-year clock.
> Their SEG-Y release dates are already published:
> `45120-020-001` (2011) — inventory released 25 Apr 2022, **SEG-Y release 25 October 2026**;
> `45120-020-003` (2012) → 8 Nov 2027; `45120-020-005` (2013) → 14 Oct 2028; `45120-020-006` (2014) →
> 30 Nov 2029; 2015 → Oct 2030; 2016 → Nov 2031; 2017 → Oct 2032; 2018 → Sep 2033; 2019 → Sep 2034;
> 2020 → Sep 2035.
> **None of the Nalcor/MKI multi-client SEG-Y is free yet, but the first tranche becomes freely disclosable
> on 25 October 2026 — roughly two months from this pass.**

### 2.10 Yukon, NWT, Nunavut, New Brunswick (VERIFIED)

**Yukon — open, but only seismic *geometry*.**
`https://yukon.ca/en/doing-business/permits-and-licensing/find-oil-and-gas-maps-and-data`
*(note `yukon.ca/en/geology` 404s and `yukon.ca/en/yukon-geological-survey` 403s to bots.)*
- **GeoYukon** (`https://mapservices.gov.yk.ca/GeoYukon/index.html?layerTheme=9`) — oil & gas layers
  *"include: wells; **seismic lines**; sedimentary basins; and oil and gas rights"*; spatial downloads at
  `https://map-data.service.yukon.ca/geoyukon/Oil_and_Gas/`.
- Free spreadsheets: *"Seismic line coordinates (1961–1984) from the National Energy Board"*
  (`https://yukon.ca/en/seismic-line-coordinates-1961-1984-source-neb`, XLS, **692.5 KB**) and
  *"Seismic line attributes (1961–1984)"*. Well documents FTP:
  `https://emr-ftp.gov.yk.ca/emrweb/OilandGas/WellDocs/`.
- The YGS open-data API (`https://apps.gov.yk.ca/apexprd/ygsids/search/{collection}?query=…`) was
  reverse-engineered; the Property File Oil & Gas collection returns **557 items for "Eagle Plain"**, all
  *well* data (267 wireline logs, 143 datasheets, 40 well reports, cuttings, poroperm, RockEval,
  biostratigraphy). **Zero seismic reflection surveys.**
- **Statute:** *Oil and Gas Act* SY 2002 c.162 **s.103**: *"**Except as provided under the regulations**, no
  person shall communicate… any record or other information obtained under this Act…"*, and s.103(4)
  overrides ATIPP. Actual release periods sit in regulations — **UNVERIFIED**.

**Northwest Territories — 573 seismic programs as free scanned PDFs; SEG-Y only federally.**
**OROGO**, `https://www.orogo.gov.nt.ca/en/geophysical-programs` *(curl segfaults against `*.gov.nt.ca`;
fetched via WebFetch)*: *"This page gives access to the results of geoscience programs carried out in
OROGO's jurisdiction between 1943 and 2013 (no programs have been carried out since then)."*
- **1,201 programs** (1,153 completed, 43 withdrawn, 3 not completed, 2 projected). Type facets:
  **Seismic 566 + seismic 7 = 573 seismic programs**; Geology 297, Other 75, Gravity 58, Aeromagnetic 46,
  Photogeology 24, **Purchase and reprocessing 21**, magnetic 18, Geophysical 17, Structural 16,
  Geochemical 15, Stratigraphy 12, Ice 6, geotechnical 2.
- Free direct downloads per program. Verified example: *"Seismic Survey Report – Trainor Lake Area"*,
  Program 5550014, Amerada Hess Canada, 1968 — **19.18 MB** main report PDF. **No SEG-Y, no digital traces.**
  Also `https://www.orogo.gov.nt.ca/en/well-data` — 685 wells.
- **NTGS** (`https://www.nwtgeoscience.ca/`, `https://app.nwtgeoscience.ca/`) — seven databases (Geoscience
  Publications 10,174; Mineral Showings; KIDD; KIMC; KANDD; Till/Soil Geochemistry; Permafrost).
  **No petroleum or seismic database.**
- **Statute:** *Oil and Gas Operations Act* (NWT) — geological/geophysical work may be disclosed *"(ii) in
  the case of a **non-exclusive survey, 15 years** after completion… or (iii) in any other case, **five
  years** after completion"*; wells 2 years / 60 days. *"non-exclusive survey" = "geophysical work that is
  conducted to acquire data for the purpose of sale to the public."*

**Nunavut — clean negative.** `cngo.ca` now redirects to **`https://cngo-bgcn.ca/`** (flaky; intermittent
504s). Series: Summary of Activities, CNGO Geoscience Data Series, Open File Map, posters/presentations/maps,
Exploration Overviews. Stated expertise: *"Precambrian, Paleozoic and Quaternary geology, GIS and cartography
and online data dissemination."* **No petroleum, oil-and-gas or seismic reflection data of any kind.** NIRB
(`https://www.nirb.ca/`) is a public registry of project applications — **documents, not data**. Oil and gas
rights in Nunavut remain **federal** (CIRNAC/NRCan) under an Arctic offshore licensing moratorium. A CKAN
search `q=Nunavut seismic` returned only **magnetotelluric** datasets — **no Nunavut reflection-seismic
SEG-Y on open.canada.ca**.

**New Brunswick — explicit negative.**
`https://www2.gnb.ca/content/gnb/en/departments/erd/energy/content/minerals/content/Oil_Gas.html` —
"Petroleum Data" contains exactly four items: **Well Reports, Rights Maps, Monthly Production Statistics,
Monthly Royalty Statistics**. **No seismic product of any kind.** Geological Survey Open Data offers Bedrock
Geology, **Geophysical Data** (airborne mag/rad, via GeoNB), Metallic Minerals, Peatland, Surficial Geology,
Till Geochemistry — no seismic. The **GeoNB ArcGIS REST** service list (`https://geonb.snb.ca/arcgis/rest/services?f=json`)
was enumerated in full: **no seismic or petroleum service exists**. **PARIS**
(`https://dnr-mrn.gnb.ca/ParisWeb/`) is live and is the likely custodian of filed geophysical final reports,
but it is an ASP.NET postback app, not GET-queryable — **UNVERIFIED**.
- **Statute (VERIFIED):** *Geophysical Exploration Regulation* **86-191** under the *Oil and Natural Gas Act*
  (`https://laws.gnb.ca/en/ShowPdf/cr/86-191.pdf`), **s.7(1)(a)**: *"…all reports, plans, data and maps
  supplied become property of the Crown in right of New Brunswick and **may be made available to the public
  by the Minister after the expiration of one year after the termination of the licence**."* **s.12(6)**
  requires the final report to include **the computer stacking diagram for each line** — i.e. NB's statutory
  deliverable is a paper/raster stack section, not SEG-Y.

### 2.11 The Canadian federal fallback — NRCan LITHOPROBE / GLIMPCE / Arctic FGP SEG-Y (VERIFIED)

Where the provinces publish nothing, **Natural Resources Canada does** — in SEG-Y, under the **Open
Government Licence – Canada**, by anonymous HTTPS with no login. **This is the cleanest open licence of any
seismic in this document.**

Root: `https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/segy/`
Verified example: `.../le/ld0077_file_0125.sgy` → `HTTP/1.1 200 OK`, `Content-Length: 17041680`.

I enumerated every transect directory and counted `.sgy` files:

| Dir | Transect | `.sgy` files | Principal coverage |
|---|---|---|---|
| `ab` | Alberta Basement | **397** | Alberta |
| `sbc` | Southern Cordillera | **270** | British Columbia |
| `snorcle` | Slave–Northern Cordillera (SNORCLE) | **201** | NWT, Yukon, NE BC |
| `vi` | Vancouver Island | **175** | British Columbia |
| `le` | Lithoprobe East | **173** | Newfoundland / Atlantic Canada |
| `ag` | Abitibi–Grenville | **165** | Ontario, Québec |
| `thot` | Trans-Hudson Orogen | **164** | Saskatchewan, Manitoba |
| `ksz` | Kapuskasing Structural Zone | **109** | Ontario |
| `gl` | **GLIMPCE** | **74** | Great Lakes — Ontario waters, Lake Superior / Huron / Michigan |
| `ws` | Western Superior | **72** | Ontario, Manitoba |
| `nwt` | Arctic FGP / Beaufort | **51** | NWT, Beaufort Sea |
| `ecsoot` | Eastern Churchill–Superior / Torngat | **42** | Labrador, Québec |
| `bin` | (auxiliary) | 0 | — |
| **TOTAL** | | **1,893 SEG-Y files** | |

Processing stages present: **STACK / MIG / FK MIG / FX DEC / SEMBL / MIG FIL**. The `nwt/` directory holds
the **Arctic Frontier Geoscience Program and Beaufort Sea** lines — `86-1_stacks.sgy` (**154,104,960 B**,
HTTP 200 verified), `87_1_ab_stk.sgy`, `87_2_stk.sgy`, `87_3_3a_stk.sgy`, `87-4_stk_1/2.sgy`, `87-4a_stk.sgy`,
`beaufort_1/1a/1b/2/3/3a_stack.sgy`, and `fgp89_1..3` stacks **and migrations**. Catalogued on Open Government
(e.g. `https://open.canada.ca/data/en/dataset/852e7976-da2b-5d0a-998c-8fb0c3c14fee`, "Arctic FGP Seismic
Reflection Line 86-1", resource type `SEGY`).

**Why this matters:** every major Canadian jurisdiction that publishes nothing itself — Alberta, BC, Ontario,
Saskatchewan, Manitoba, NWT, Labrador — is nonetheless covered by openly-licensed SEG-Y here. This is also
the current home of the **GLIMPCE / Midcontinent Rift** profiles that Minnesota does not hold (§1.10).
Companion publication index: GEOSCAN, `https://geoscan.nrcan.gc.ca/`.

---

## 3. Coverage status of this pass

| Group | Status |
|---|---|
| **Kansas (priority re-check)** | **DONE — settled negative** |
| Cross-cutting (NAMSS, EDX, GDR, ScienceBase, NGDS-dead) | **DONE** |
| CA, AK, LA, MS, AL, AR, FL | **DONE** |
| ND, SD, WY, UT, CO, NM, NV | **DONE** |
| MO, IA, MN, WI, VA, TN, GA, SC, NC | **DONE** |
| IL, MT (via EDX) | **DONE** |
| TX, OK, NE, MI, OH, WV | **DONE** |
| KY, IN, NY, PA | **DONE** |
| AB, BC, SK, MB, ON | **DONE** |
| QC, NB, NS, NL, YT, NT, NU | **DONE** |

**Coverage complete: all 35 US states and all 13 Canadian provinces/territories in scope.**

### 3a. Bottom line — where to actually get data

**Free, direct download, no registration, open or unrestricted licence — take these first:**

1. **Kevin Dome, Montana** (DOE EDX) — **≈589 GB SEG-Y**, 9-component 3D, full prestack-to-inversion chain.
   The best free onshore US 3D found anywhere in this pass.
2. **NRCan LITHOPROBE / GLIMPCE / Arctic FGP** (geogratis) — **1,893 SEG-Y files** across 12 transects,
   **Open Government Licence – Canada**. Cleanest licence in the whole document; covers most of Canada.
3. **Soda Lake, Nevada** (DOE GDR) — **171 GB, 8,321 SEG-Y**, 3D + 3C, **CC BY 4.0**, anonymous S3.
4. **Utah FORGE** (DOE GDR) — **≈127 GB**, 2D + 3D, raw uncorrelated *and* correlated shot gathers plus
   PSTM/PSDM and velocity model, **CC BY 4.0**.
5. **USGS NAMSS** — 972 3D + 610 2D marine surveys, **public domain, no restrictions whatsoever**.
6. **Illinois via DOE EDX** — IBDP (49.3 GB active seismic incl. 3D and 4D volumes, **CC-BY/CC-BY-SA**) and
   FutureGen 2.0 (47.16 GB, five complete WesternGeco 2D chains).
7. **Geoscience BC Nechako** — 1.78 GiB, 7 2D lines, stack + migration. *Caveat: no licence statement exists.*
8. **North Dakota CarbonSAFE** (EDX) — ~27 GB SEG-Y. **South Georgia Rift** (EDX) — 362 SEG-Y, 1.57 GB.
   **USGS Mid-Continent Vibroseis** — 1.57 GB, public domain.

**Free to fetch but licence-encumbered — check before redistributing or training on them:**
- **ISGS Geophysics Data Viewer** (218 files, 23.45 GB, incl. a 2.9 GB 3D volume) — © all rights reserved;
  *"License fees and a license agreement may be required, depending on the proposed usage."*
- **Geoscience BC Nechako** — no licence statement at all; get written confirmation.

**Worth the paperwork:**
- **Alaska DGGS/GMC** — ~298 TB, 35 released 3D surveys, **fee waived entirely for academic/government**
  requesters (you supply a USB 3.0 drive). Note the licence asymmetry: *purchased* data has no restrictions,
  *fee-waived* data may not be redistributed.
- **C-NLOER (Newfoundland offshore)** — 348 programs; SEG-Y **free by e-mail request** after the statutory
  clock. **The first Nalcor/MKI multi-client tranche unlocks 25 October 2026.**

**Do not chase:** Kansas (nothing exists — §0), `geothermaldata.org` (dead domain), Québec SIGPEG if you
expected free SEG-Y (it is $59–$1,179 under an internal-use-only licence), the Newark Basin or WY-CUSP
"seismic" archives (traces were never deposited — §1.13).

**Two myths corrected by this pass:**
- **There is no Alberta 5-year seismic confidentiality rule.** That clock is federal — Canada Petroleum
  Resources Act s.101, for frontier lands and the offshore Accord regime. Alberta's Exploration Regulation
  contains **zero** occurrences of "confidential".
- **ESOGIS (New York) does not serve seismic line data.** It holds *borehole* velocity/seismic wireline logs
  only, behind a free registration.

**Statutory confidentiality, where it exists at all:**

| Jurisdiction | Rule |
|---|---|
| Manitoba | **1 yr / 3 yrs / 10 yrs** by report class (M.R. 110/94 s.20(1)) — the clearest clock in Canada |
| Saskatchewan | Interpreted seismic maps public **1 yr** after the permit expires/is surrendered/cancelled |
| Québec | Reprocessed data public **3 yrs** after the request date |
| NWT · NL offshore | **5 yrs** after completion; **15 yrs** for non-exclusive/multi-client surveys |
| New Brunswick | **1 yr** after licence termination (Reg. 86-191 s.7(1)(a)) |
| British Columbia | **No expiry** — release only by Order in Council or the owner's written consent (PNG Act s.122(2)) |
| Alberta · North Dakota | **None** — verified by full-text search of the governing regulation |
| Alaska | **2 or 10 yrs** after the exploration activity (AS 43.55.025 / .023) |
| Federal US (BOEM/NAMSS) | **25 yrs** from permit issuance (30 CFR 551, 580) |
| Federal Canada | **5 yrs** (CPRA s.101), extended administratively to 10–15 yrs for spec data |

---

## 4. Method notes / caveats

- The session WebSearch quota was exhausted early; all subsequent verification used **direct HTTP fetch**
  of constructed agency URLs, agency directory listings, and public JSON/REST APIs (CKAN on EDX and GDR,
  ArcGIS FeatureServer, USGS ScienceBase, Zenodo, NAMSS WMS `GetFeatureInfo`, Internet Archive CDX). This is
  a *stronger* form of verification than search snippets, but it can miss resources discoverable only
  through a site's internal search box. General search engines (DuckDuckGo, Mojeek, Bing, Startpage,
  Ecosia, SearXNG) were all CAPTCHA-walled, 403'd or returned junk.
- **ZIP central-directory parsing over HTTP range requests** was used to inspect multi-GB archives without
  downloading them. This is how the South Georgia Rift, FutureGen and Newark Basin contents were settled.
- Pages returning 403/timeout are recorded as UNVERIFIED, never as a negative.
- Byte sizes are as reported by the hosting API or `content-length`, not estimates.
- **WebFetch 403s some hosts that curl retrieves fine** (notably `walrus.wr.usgs.gov`, `wiki.seg.org`) — use
  curl with a browser user-agent for those.
