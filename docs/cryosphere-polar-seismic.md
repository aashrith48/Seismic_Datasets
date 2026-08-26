# Cryosphere & Polar Seismic Datasets

Open / openly-discoverable seismic data on ice sheets, ice shelves, glaciers and polar regions:
active-source reflection & refraction, passive broadband, nodal arrays, and DAS.

**~180 entries. All facts below were verified against live API endpoints during this research pass.**

## Cross-references (documented elsewhere in this project — not repeated here)

| Dataset | Where it is documented |
|---|---|
| Antarctic Seismic Data Library System (SDLS) — ~300,000 line-km marine MCS | `academic-marine-archives.md` |
| AWI Arctic/Antarctic PANGAEA marine seismic holdings | `academic-marine-archives.md` |
| Rutford Ice Stream DAS / DAS-N2N Zenodo records | `earthquake-das-planetary.md` |
| Grimsel Test Site (rock-lab induced seismicity, not glacial) | `ccs-geothermal-mining.md` |

---

## Verification legend

- **VERIFIED** — I fetched the live endpoint in this research pass and the stated facts (network code, station count, dates, DOI, byte size, licence) came back from that endpoint.
- **VERIFIED (metadata)** — the DOI/title/size/licence came from the DataCite or PANGAEA API record; I did not additionally open the landing page.
- **VERIFIED (code+DOI)** — the FDSN registry confirmed the code, name, years and DOI, but the station count was not returned by the geographic station query (usually because the deployment is embargoed, future, or outside my bounding box).
- **UNVERIFIED / NOT CONFIRMED** — see Section 10.

## Two very different access models — read this before using anything below

**1. FDSN network codes** (Sections 1, 4, 6, 7). Waveform data, *not* a file download. There is no
published byte volume and no licence text; the data centre asks that you cite the network DOI.
Nearly all EarthScope-archived polar temporary networks become fully open ~2 years after the
deployment ends. Retrieve with `fdsnws-dataselect` / ObsPy / obspyDMC:

```
# waveforms
https://service.earthscope.org/fdsnws/dataselect/1/query?net=XH&sta=*&cha=BH?&start=2015-01-01&end=2015-01-02
# metadata for any code in this document
https://service.earthscope.org/fdsnws/station/1/query?net=<CODE>&level=station&format=text
# which data centre holds a given network
https://service.iris.edu/irisws/fedcatalog/1/query?net=<CODE>&format=text
```

Some polar codes are **not** at EarthScope: `AW` and `5L` are at **GEOFON/GFZ**; `1D_2019`,
`XG_2019`, `9F_2023` are at **RESIF/EPOS-France**; `4D` and `3Z` are at **SED/ETH Zürich**;
`DY` is at **INGV**. Use the fedcatalog URL above to route the request.

**2. File repositories** (Sections 2, 3, 5, 8). BAS Polar Data Centre, PANGAEA, USAP-DC, AADC,
Zenodo. These give SEG-Y / miniSEED / CSV files with **real byte sizes and explicit licences**.
For an ML or inversion project these are the entries worth starting from.

### On "SIZE" for FDSN networks
Almost no FDSN network publishes a byte volume. For those entries SIZE is the **verified station
count × deployment span** (station-years), which is the honest checkable quantity. As a rough
guide continuous 3-component 100 Hz miniSEED runs on the order of 15–20 GB per station-year and
40 Hz BH channels roughly 6–8 GB per station-year — **order-of-magnitude only, not published
figures.** The one polar network that *does* publish a volume is `5L` (Vatnajökull), at **574 GB**
for 25 stations over 2013–2017, which is a useful calibration point.

---

# 1. Antarctica — FDSN network codes

**Source, VERIFIED:** `https://service.earthscope.org/fdsnws/station/1/query?maxlatitude=-60&level=network&format=text`
(every network with ≥1 station south of 60°S), cross-checked for DOIs against
`https://www.fdsn.org/networks/?search=antarctic`, `?search=ice`, `?search=glacier`, `?search=polar`.

## 1.1 Ice-stream, ice-shelf & glacier dynamics deployments

| Network | Name | Region | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|---|
| **XH** | Dynamic Response of the Ross Ice Shelf to Ocean Waves + Structure & Dynamics of the Ross Sea (**RIS/DRIS**) | Ross Ice Shelf | Passive broadband | 2014–2017 | **34 stations**, ~4 yr | 10.7914/SN/XH_2014 | VERIFIED |
| **XN** | Dynamic Response of the Ross Ice Shelf to Wave-Induced Vibrations | Ross Ice Shelf | Passive broadband | 2014 | **15 stations**, 1 yr | — | VERIFIED |
| **7F** | Past and future deformation of the Ross Ice Shelf | Ross Ice Shelf | Passive broadband | 2016–2017 | **2 stations** | 10.7914/4gr5-k242 | VERIFIED |
| **9J** | Grounding Line Dynamics: Crary Ice Rise Revisited | Crary Ice Rise, Ross Ice Shelf | Passive + active | 2015–2016 | — | 10.7914/SN/9J_2015 | VERIFIED (code+DOI) |
| **1F** | Flexural-gravity-wave band gaps, Bragg scattering & ice damage | McMurdo Ice Shelf | Passive | 2025-08 → 2027-03 | **4 stations** | 10.7914/4sj1-k016 | VERIFIED |
| **1H** | McMurdo Ice Shelf Small Node Network | McMurdo Ice Shelf | **Nodal** | 2021–2022 | — | 10.7914/SN/1H_2021 | VERIFIED (code+DOI) |
| **YD** | **WISSARD** — Whillans Ice Stream Subglacial Access Research Drilling | Whillans Ice Stream / Subglacial Lake Whillans | Passive broadband + nodal | 2012–2017 | **40 stations**, ~6 yr | — | VERIFIED |
| **4A** | Subglacial hydrology & basal shear stress beneath Whillans Ice Stream | Whillans Ice Stream | Passive | 2008 | **4 stations** | 10.7914/SN/4A_2008 | VERIFIED |
| **2C** | Geophysical Study of Ice Stream Stick-Slip Dynamics | Whillans / Siple Coast | Passive, dense | 2010–2011 | **49 stations**, 2 yr | 10.7914/SN/2C_2010 | VERIFIED |
| **XF** | Antarctic Microearthquake Project — Monitoring of Ice Stream C | Kamb (Ice Stream C) | Passive microearthquake | 1995–1996 | **27 stations** | 10.7914/SN/XF_1995 | VERIFIED |
| **XW** | Siple Coast Antarctica Microearthquake Project | Siple Coast | Passive | 2003–2006 | — | — | VERIFIED (code+dates) |
| **5K** | Kamb Ice Stream Outlet Channel | Kamb Ice Stream | Passive + active | 2019–2020 | **12 stations** | 10.7914/SN/5K_2019 | VERIFIED |
| **1D** | Elevation change anomalies in West Antarctica & subglacial water dynamics | West Antarctica | Passive | 2010–2011 | **6 stations** | 10.7914/SN/1D_2010 | VERIFIED |
| **1D** | **UKANET** — UK Antarctic Network | West Antarctica / Peninsula | Passive broadband | 2016–2018 | **14 stations** | 10.7914/SN/1D_2016 | VERIFIED |
| **9B** | **BEAMISH** (Bed Access, Monitoring and Ice Sheet History) | Rutford Ice Stream | Passive + active | 2016–2019 | **40 stations**, 4 yr | — | VERIFIED |
| **6L** | BEAMISH 2019-20, Rutford Ice Stream | Rutford Ice Stream | Passive + active | 2019–2020 | **16 stations** | 10.7914/SN/6L_2019 | VERIFIED |
| **5B** | Rutford Ice Stream Cooperative Research Program with BAS | Rutford Ice Stream | Passive | 2018–2019 | — | 10.7914/SN/5B_2018 | VERIFIED (code+DOI) |
| **YG** | Gauging Rutford Ice Stream Transients | Rutford Ice Stream | Passive | 2009 | **10 stations** | — | VERIFIED |
| **XC** | Observing Pine Island Glacier ice-shelf deformation & fracture (GPS + seismic) | Pine Island Glacier | Passive | 2012–2014 | **5 stations** | 10.7914/SN/XC_2012 | VERIFIED |
| **7U** | Thwaites Margins Seismic Broadband (**ITGC / TIME**) | Thwaites Glacier | Passive broadband | 2019–2021 | **14 stations**, 3 yr | — | VERIFIED |
| **5I** | **TARSAN** active-source seismic survey, Dotson & Crosson Ice Shelves (**ITGC**) | Dotson / Crosson Ice Shelves | **Active-source** | 2019–2020 | — | 10.7914/az69-5f75 | VERIFIED (code+DOI) |
| **5V** | Thwaites Eastern Ice Shelf Daggers & Pinning Point Shear Zone (**ITGC**) | Thwaites Eastern Ice Shelf | Passive | 2022–2023 | — | 10.7914/fjb2-ve22 | VERIFIED (code+DOI) |
| **8A** | IPY: Stability of Larsen C Ice Shelf in a Warming Climate | Larsen C Ice Shelf | Passive | 2008–2009 | **1 station** | 10.7914/SN/8A_2008 | VERIFIED |
| **5J** | **LARISSA** — IPY Larsen Ice Shelf System, Abrupt Environmental Change | Larsen Ice Shelf | Passive | 2010-02 → 2013-05 | **2 stations** | 10.7914/sf9n-7561 | VERIFIED |
| **1T** | RAPID: Observing the Disintegration of the Scar Inlet Ice Shelf | Scar Inlet / Larsen B | Passive | 2015–2016 | — | 10.7914/SN/1T_2015 | VERIFIED (code+DOI) |
| **6Z** | Larsen C Ice Shelf Rift Tip Array | Larsen C Ice Shelf | Passive array | 2022 | — | — | VERIFIED (code+dates) |
| **9G** | Impact of Supraglacial Lakes on Ice-Shelf Stability | Antarctic ice shelves | Passive | 2016–2017 | **4 stations** | 10.7914/SN/9G_2016 | VERIFIED |
| **4E** | Antarctica Ice Rift Experiment | Antarctica | Passive | 2022–2023 | — | 10.7914/SN/4E_2022 | VERIFIED (code+DOI) |
| **7P** | Seismic Survey of the **Fimbul Ice Shelf** | Fimbul Ice Shelf, Dronning Maud Land | Active / passive | 2025–2027 | — | 10.7914/m8r7-0z46 | VERIFIED (code+DOI) |
| **X9** | Monitoring an active rift system at the front of the **Amery Ice Shelf** | Amery Ice Shelf, East Antarctica | Passive | 2004–2007 | **36 stations**, 4 yr | 10.7914/SN/X9_2004 | VERIFIED |
| **2A** | Sørsdal Glacier 2017-18 | Sørsdal Glacier, East Antarctica | Passive / nodal | 2017–2019 | **14 stations** | 10.7914/SN/2A_2017 | VERIFIED |
| **1J** | **Totten Glacier Active and Passive Source Experiment** | Totten Glacier, East Antarctica | **Active + passive** | 2018–2019 | **12 stations** | 10.7914/SN/1J_2018 | VERIFIED |
| **6N** | **Totten Glacier Active Source Experiment** | Totten Glacier | **Active-source** | 2017–2019 | — | 10.7914/SN/6N_2017 | VERIFIED (code+DOI) |
| **8T** | Denman Glacier System | Denman Glacier, East Antarctica | Passive | 2023–2027 | — | — | VERIFIED (code+dates) |
| **ZB** | Vanderford–Totten Glacier System | East Antarctica | Passive | 2024–2027 | — | — | VERIFIED (code+dates) |
| **ZF** | East Antarctic Outlet Glacier Dynamics | East Antarctica | Passive | 2012–2014 | **28 stations** | 10.7914/SN/ZF_2012 | VERIFIED |
| **ZB** | Anisotropy and structure of the Priestley Glacier shear margin | Priestley Glacier | Passive / nodal | 2019–2020 | — | 10.7914/SN/ZB_2019 | VERIFIED (code+DOI) |
| **8Q** | **Active-source** seismology on the Priestley Glacier shear zone | Priestley Glacier | **Active-source** | 2018–2019 | — | 10.7914/SN/8Q_2018 | VERIFIED (code+DOI) |
| **ZL** | David Glacier 2003-2004 | David Glacier | Passive | 2003–2004 | **5 stations** | — | VERIFIED |
| **XA** | Taylor Glacier Calving — Mechanics of Dry-Land Calving | Taylor Glacier, Dry Valleys | Passive | 2004–2007 | **6 stations** | 10.7914/SN/XA_2004 | VERIFIED |
| **YW** | **MIDGE** — Blood Falls, McMurdo Dry Valleys | Taylor Glacier / Blood Falls | Passive | 2013–2015 | **7 stations** | — | VERIFIED |
| **XV** | Collaborative research of the Earth's largest **icebergs** | Iceberg-mounted, Ross Sea | Passive | 2003–2006 | **11 stations** | — | VERIFIED |
| **ZD** | Tides E 2005 | Antarctic ice streams | Passive | 2005–2006 | **13 stations** | — | VERIFIED |
| **ZF** | Tidal modulation of ice stream flow (Tides) | Antarctic ice streams | Passive | 2005–2006 | **16 stations** | — | VERIFIED |
| **ZG** | Tidal modulation of ice stream flow — Tides B Upstream | Antarctic ice streams | Passive | 2004 | **14 stations** | — | VERIFIED |
| **ZH** | Tidal modulation of ice stream flow — Tides B Grounding Line | Antarctic grounding line | Passive | 2004 | **14 stations** | — | VERIFIED |
| **ZH** | NSFGEO-NERC: direct influence of meltwater on Antarctic Ice Sheet dynamics | Antarctica | Passive | 2024–2027 | — | 10.7914/dh2n-rf47 | VERIFIED (code+DOI) |
| **X1** | **Byrd Lake Reflection Seismics** — CReSIS | Byrd subglacial lake | **Active-source reflection** | 2011–2012 | **9 stations** | — | VERIFIED |
| **2E** | **WAIS Divide Source Testing** | WAIS Divide | **Active-source (source test)** | 2018–2019 | — | 10.7914/SN/2E_2018 | VERIFIED (code+DOI) |
| **XS** | **EASGON** — Eastwind Glacier Geophysical Surveys On Top of Antarctic Ice-Shelf Transition | Eastwind Glacier | Active + passive | 2023 | — | 10.7914/jah0-9856 | VERIFIED (code+DOI) |
| **7N** | EASGON Phase II | Eastwind Glacier | Active + passive | 2023–2024 | — | 10.7914/e8rs-yk70 | VERIFIED (code+DOI) |
| **9I** | **SWAIS 2C** — Sensitivity of the West Antarctic Ice Sheet to 2 °C | West Antarctica | Passive / active | 2025–2026 | — | 10.7914/36zt-ca71 | VERIFIED (code+DOI) |
| **2L** | New Instrument & Measurement Approach to Antarctic **Cryo-Seismogeodesy** | Antarctica | Passive / geodetic | 2024–2026 | — | 10.7914/htxs-4259 | VERIFIED (code+DOI) |
| **X8** | **Coulman High VSP**, Antarctica | Coulman High, Ross Ice Shelf | **VSP (active-source borehole)** | 2010/2011 | — | 10.7914/SN/X8_2011 | VERIFIED (code+DOI) |
| **8G** | Ice Sheets and Interactions, Dronning Maud Land and Coats Land | Dronning Maud Land | Passive | 2024–2028 | — | 10.7914/j9cq-xd60 | VERIFIED (code+DOI) |
| **7T** | "LHS" | Antarctica (south of 60°S) | Nodal, very dense | 2019–2020 | **195 stations** | — | VERIFIED (purpose unconfirmed) |

## 1.2 Antarctic lithosphere / crust & mantle deployments (TAMSEIS, AGAP/GAMSEIS, POLENET …)

| Network | Name | Region | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|---|
| **YT** | **IPY POLENET-Antarctica (ANET)** — links between geodynamics and ice sheets | Antarctica-wide | Passive broadband, long-term | 2007 → 2028 | **66 stations**, ongoing | 10.7914/SN/YT_2007 | VERIFIED |
| **XP** | **TAMSEIS** — Deep Continental Structure Across the East-West Antarctic Boundary | Transantarctic Mountains / East Antarctica | Passive broadband | 2000–2004 | **45 stations**, 5 yr | 10.7914/SN/XP_2000 | VERIFIED |
| **ZM** | **AGAP / GAMSEIS** — Lithosphere beneath the Gamburtsev Mountains | Gamburtsev Subglacial Mts, **Dome A**, East Antarctica | Passive broadband | 2007–2013 | **30 stations**, 7 yr | 10.7914/SN/ZM_2007 | VERIFIED |
| **ZJ** | **TAMNNET** — Transantarctic Mountains Northern Network | N. Transantarctic Mountains | Passive broadband | 2012–2015 | **15 stations** | 10.7914/SN/ZJ_2012 | VERIFIED |
| **YI** | **ANUBIS** — Antarctic Network of Unattended Broadband Seismometers | Antarctic interior | Passive broadband | 1997–2002 | **5 stations** | 10.7914/SN/YI_1997 | VERIFIED |
| **XU** | Trans-Antarctic | Antarctica | Passive | 1999–2000 | **10 stations** | — | VERIFIED |
| **XB** | **SEPA** — Seismic Experiment in Patagonia and Antarctica | Antarctic Peninsula / Scotia Sea | Passive broadband | 1997–1999 | **12 stations** | 10.7914/SN/XB_1997 | VERIFIED |
| **YN** | Seismic Experiment in Patagonia and Antarctica | Patagonia / Antarctica | Passive broadband | 1999–2004 | **5 stations** | — | VERIFIED |
| **1P** | Solid Earth response of the Patagonian Andes to post-Little-Ice-Age glacial retreat | Patagonia | Passive broadband | 2018–2021 | — | 10.7914/SN/1P_2018 | VERIFIED (code+DOI) |
| **XD** | Power & Communication for Remote Autonomous GPS and Seismic Stations | Antarctica | Passive (engineering) | 2007–2010 | **5 stations** | 10.7914/SN/XD_2007 | VERIFIED |
| **5K** | Seismic structure of the continent under Antarctica | Antarctica | Passive broadband | 2002–2014 | — | 10.7914/hf8d-4s28 | VERIFIED (code+DOI) |
| **5Q** | Ice Sheets and Interactions, East Antarctica | East Antarctica | Passive | 2023–2027 | — | 10.7914/74en-yt90 | VERIFIED (code+DOI) |
| **9R** | **EAIIST** — East Antarctic International Ice Sheet Traverse seismic network | East Antarctic plateau (**Dome C** sector) | Passive / active traverse | 2019–2021 | — | — | VERIFIED (code+dates) |
| **9U** | Magnetotellurics at a potential old-ice drilling site on **Dome A** | Dome A | MT (co-listed with seismic) | 2024–2025 | — | 10.7914/dmhj-4441 | VERIFIED (code+DOI) |
| **7K / 9X / Y6** | CAREER: crust & uppermost mantle beneath the **South Pole** | South Pole | Passive broadband | 2023–2026 | three codes | 10.7914/4zfz-wn70 · 10.7914/h0a3-nz85 · 10.7914/tvw3-c709 | VERIFIED (codes+DOIs) |
| **XI** | South Pole Analysis of Machines — HF noise characterisation | South Pole Station | Passive noise | 2006 | **8 stations** | 10.7914/SN/XI_2006 | VERIFIED |

## 1.3 Antarctic permanent / observatory networks

| Network | Name | Region | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|---|
| **AI** | **ASAIN** — Antarctic Seismographic Argentinean Italian Network | Antarctic Peninsula, Scotia Sea | Permanent broadband | 1992 → ongoing | **6 stations** south of 60°S | 10.7914/SN/AI | VERIFIED |
| **AW** | **AWI Network Antarctica** — Neumayer / **Ekström Ice Shelf**. Broadband VNA1, VNA2, VNA3, FRFJ + the **Watz-Array** (VNAA1-3, VNAB1-5, VNAC1-7) | Ekström Ice Shelf, Dronning Maud Land | Permanent broadband + array | 1980 → present (data from 2009) | **19 stations** | 10.14470/NJ617293 | VERIFIED — "All data are freely distributed by the GEOFON data center" |
| **DY** | **Polar Seismic Italian Network (David)** — INGV | **David Glacier, Antarctica** *and* Wolstenholme Fjord, NW Greenland | Permanent broadband | 2003 → open-ended | — | 10.13127/sd/n2im7z-ttv | VERIFIED (registry) |
| **GE** | GEOFON — includes VNA1/VNA2/VNA3 (Neumayer) | Antarctica | Permanent broadband | 1991 → ongoing | 144 stations total | — | VERIFIED |
| **KP** | Korea Polar Observation Network (KOPRI — Jang Bogo / King Sejong) | Antarctica | Permanent broadband | 2013 → ongoing | **2 stations** south of 60°S | 10.7914/SN/KP | VERIFIED |
| **ER** | Mount Erebus Volcano Observatory Seismic Network | Mt Erebus, Ross Island | Permanent volcano-seismic | 1981 → ongoing | **12 stations** | — | VERIFIED |
| **AU** | Australian National Seismograph Network (Mawson, Casey, Davis) | Antarctica + Australia | Permanent broadband | 1994 → ongoing | 259 total (few Antarctic) | — | VERIFIED |
| **IU** | GSN (IRIS/USGS) — SBA (Scott Base), QSPA (South Pole), PMSA (Palmer) | Antarctica | Permanent very-broadband | 1988 → ongoing | 116 total | — | VERIFIED |
| **G** | GEOSCOPE — DRV (Dumont d'Urville), CCD (Concordia / **Dome C**) | Antarctica | Permanent very-broadband | 1982 → ongoing | 58 total | — | VERIFIED |
| **B6** | Bransfield Strait Seismic Network | Bransfield Strait | Permanent | 2008 → ongoing | **3 stations** | — | VERIFIED |
| **ZX** | Bransfield Strait (temporary) | Bransfield Strait | Passive / OBS | 2019–2020 | **14 stations** | — | VERIFIED |
| **XU** | Deception Island Passive/Active Source | Deception Island | **Active + passive** | 2005 | **16 stations** | — | VERIFIED |

## 1.4 Mount Erebus — polar volcano-seismic (high-rate, low-noise polar reference data)

| Network | Name | Years | SIZE (verified) | Status |
|---|---|---|---|---|
| **1G** | Erebus Backbone Network | 2022–2028 | **8 stations** | VERIFIED |
| **8E** | Erebus low-noise broadband network | 2022–2028 | **4 stations** | VERIFIED |
| **2H** | Interim Broadband Monitoring of Mount Erebus | 2016–2024 | **11 stations** | VERIFIED |
| **Y4** | Mt. Erebus Volcano Observatory | 2008–2009 | **114 stations** | VERIFIED |
| **ZW** | Erebus Tomography and Source Studies | 2007–2009 | **25 stations** | VERIFIED |
| **ZO** | Erebus Small Array | 2011–2012 | **6 stations** | VERIFIED |
| **XZ** | Mount Erebus Seismic Studies | 1999–2000 | **8 stations** | VERIFIED |
| **XS** | Mount Erebus Observatory | 1996–1997 | **5 stations** | VERIFIED |

---

# 2. BAS / NERC EDS **UK Polar Data Centre** — the richest polar seismic *file* archive

**Source, VERIFIED:** DataCite API,
`https://api.datacite.org/dois?query=publisher:"UK Polar Data Centre" AND seismic&page[size]=100`
returned **meta.total = 53**. The file counts and byte sizes below are the `sizes` field of each
DataCite record — real published volumes, not estimates.

**Licence:** Open Government Licence v3.0 (OGL v3) unless noted; BEDMAP products are CC-BY-4.0.
**Access model:** fully open, no login. Landing page `https://data.bas.ac.uk/full-record.php?id=<ID>`;
files served from the BAS **Ramadda** repository at
`http://ramadda.data.bas.ac.uk/repository/entry/show?entryid=<uuid>`.

## 2.1 Antarctic & Greenland active-source seismic (SEG-Y shot gathers) — highest-value entries

| Dataset | Region | Type | Years | SIZE (verified) | Licence | DOI / URL | Status |
|---|---|---|---|---|---|---|---|
| Passive- and active-source seismic recorded with **Distributed Acoustic Sensing on Eastwind Glacier** | Eastwind Glacier, Antarctica | **DAS** (active + passive) | Feb 2024 | **131 files, 122.5 GB** | OGL v3 | 10.5285/23dbd529-3a57-4933-bb9d-16ee1c85fda0 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02082 | VERIFIED |
| **Downhole distributed acoustic seismic profiles at Skytrain Ice Rise** | Skytrain Ice Rise, West Antarctica | **Borehole DAS / DVSP** | Jan 2020 | **152 files, 86.8 GB** | OGL v3 | 10.5285/99f0d269-d8fa-48e0-89e6-358486d82330 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01458 | VERIFIED |
| **Passive seismic data from a rift tip on the Larsen C Ice Shelf** | Larsen C Ice Shelf | Passive | Nov–Dec 2022 | **15,835 files, 213 GB** | OGL v3 | 10.5285/7cf34af4-bc74-4e2b-9319-def18a654871 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02245 | VERIFIED |
| **Active source seismic survey, southern sector of Larsen C Ice Shelf** | Larsen C Ice Shelf | **Active-source** | Dec 2022 | **246 files, 724 MB** | OGL v3 | 10.5285/847a2898-51d1-4b74-a7b5-c73f179c8943 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02034 | VERIFIED |
| **Seismic refraction data, Larsen C Ice Shelf, after the calving of Iceberg A68** | Larsen C Ice Shelf | **Refraction** | Nov 2017 | **1,016 files, 1.5 GB** | OGL v3 | 10.5285/147baf64-b9af-4a97-8091-26aec0d3c0bb → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01226 | VERIFIED |
| Seismic refraction data, Larsen C Ice Shelf, **Whirlwind Inlet** | Larsen C Ice Shelf | **Refraction** | Nov–Dec 2015 | **495 files, 1.5 GB** | OGL v3 | 10.5285/5d63777d-b375-4791-918f-9a5527093298 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01246 | VERIFIED |
| Seismic refraction data, Larsen C Ice Shelf, **Cabinet Inlet** | Larsen C Ice Shelf | **Refraction** | Nov–Dec 2014 | **8 files, 19 MB** | OGL v3 | 10.5285/fff8afee-4978-495e-9210-120872983a8d → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01247 | VERIFIED |
| Seismic refraction data, Larsen C Ice Shelf, **Joerg Peninsula Suture Zone / Solberg Inlet** | Larsen C Ice Shelf | **Refraction** | Nov–Dec 2008 | **2 files, 3.3 MB** | OGL v3 | 10.5285/418a769b-2a35-4e06-bd02-9cd6d222558f → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01245 | VERIFIED |
| **Seismic bathymetry data, Larsen C Ice Shelf** | Larsen C Ice Shelf | **Active-source bathymetry** | 2016 | **354 files, 515 MB** | OGL v3 | 10.5285/315740b1-a7b9-4cf0-9521-86f046e33e9a → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01250 | VERIFIED |
| **Seismic reflection and refraction shot gathers from Korff Ice Rise** — IBM-real **SEG-Y**, 48 ch, 8 kHz (refl) / 16 kHz (refr), 24-bit, 3.7 km profile along the ice divide | Korff Ice Rise, West Antarctica (78.7 °S, 68.4–68.5 °W) | **Reflection + refraction** | Jan 2015 | **34 files, 98.0 MB** (31 refl + 3 refr) | OGL v3 | 10.5285/e9ed7128-eeed-4478-b308-8d1ea347dfa4 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01970 | VERIFIED (landing page opened) |
| **Unprocessed seismic reflection shot gathers from Ghost Ridge, Thwaites Glacier** | Thwaites Glacier | **Active-source reflection** | 2024 | **3 files, 263 MB** | OGL v3 | 10.5285/5923905d-edb4-459a-b744-5a684b1592fa → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02183 | VERIFIED |
| **Subglacial Lake Ellsworth seismic reflection profiles, raw seismic + GPS** | Subglacial Lake Ellsworth, West Antarctica | **Active-source reflection** | 2007/2008 | **6 files, 308.8 MB** | OGL v3 | 10.5285/f7eda2dc-245e-4704-aef8-4a267190c22a → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02091 | VERIFIED |
| Ice surface, ice base and lake bed elevation from seismic data over **Subglacial Lake Ellsworth** | Subglacial Lake Ellsworth | Derived picks | 2007–08 | **1 file, 51.2 kB** | OGL v3 | 10.5285/01f26c07-ea6c-4d89-893e-d86247874e78 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01330 | VERIFIED |
| **Seismic bathymetry surveys of Subglacial Lake CECs** | Subglacial Lake CECs, West Antarctica | **Active-source** | 2016 & 2022 | **101 files, 804.0 MB** | OGL v3 | 10.5285/768258e0-8719-446f-b20f-587725d55774 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01724 | VERIFIED |
| **Seismic measurements of ice draught and seabed elevation, southern & western Ronne Ice Shelf** | Ronne Ice Shelf | **Active-source** | 1994–95 | **162 files, 54 MB** | OGL v3 | 10.5285/4629cb1c-126e-46db-a874-9b7b969997d4 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02228 | VERIFIED |
| **Unprocessed shot gathers, active-source seismic over an inferred active subglacial lake, Isunnguata Sermia** | **West Greenland** | **Active-source** | 2024–2025 | **202 files, 451 MB** | OGL v3 | 10.5285/c91c5bda-9d40-4711-b926-11343444da19 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02184 | VERIFIED |

## 2.2 BAS PDC — Rutford icequake catalogues & derived seismic products

| Dataset | Region | Type | Years | SIZE (verified) | Licence | DOI / URL | Status |
|---|---|---|---|---|---|---|---|
| **Microseismic icequake catalogue, Rutford Ice Stream** | Rutford Ice Stream | Icequake catalogue | Nov 2018 – Feb 2019 | **4 files, 56 MB** | OGL v3 | 10.5285/b809a040-8305-4bc5-baff-76aa2b823734 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01432 | VERIFIED |
| **Shear wave splitting catalogue, Rutford Ice Stream** | Rutford Ice Stream | SWS measurements | Nov 2018 – Feb 2019 | **606,545 files, 12 GB** | OGL v3 | 10.5285/6fcc17ad-425b-4367-bd23-c4133a38e359 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01645 | VERIFIED |
| 3D radar topography, bed reflectivity and **seismic acoustic impedance of Rutford Ice Stream** | Rutford Ice Stream | Derived impedance | Dec 2005 – Jan 2017 | **6 files, 1.3 MB** | OGL v3 | 10.5285/11e5449d-2de7-40d8-8994-094238808625 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01656 | VERIFIED |
| 3D shear wave (Vsv) velocity model, **West Antarctic uppermost mantle** to 200 km | West Antarctica | Tomographic model | 2019 | **2,164 files, 209 MB** | OGL v3 | 10.5285/c11bdb27-df44-4b56-8f4c-afc51b6e1e3a → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01146 | VERIFIED |
| 3D shear wave (Vsv) velocity model, **West Antarctic crustal structure** | West Antarctica | Tomographic model | 2019 | **2,904 files, 106 MB** | OGL v3 | 10.5285/b5ffac8a-9846-4f86-9a71-3ce992a18148 → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01145 | VERIFIED |
| Geophysical survey of **Peninsula Point, NWT, Canada** (Tromino 3G ENGY) | Canadian Arctic permafrost coast | Passive HVSR | Jul–Aug 2019 | **255 files, 213.5 MB** | OGL v3 | 10.5285/8cdf7941-f13b-4237-b921-05a6c6cde40a → https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01351 | VERIFIED |

## 2.3 BAS PDC — companion airborne radar (RES)
Included because these are the standard co-located constraint for the seismic lines above and
share the same access model and licence. **This is where PolarGAP and AGAP actually live.**

| Dataset | Region | SIZE (verified) | Licence | URL | Status |
|---|---|---|---|---|---|
| **PolarGAP** processed airborne RES, South Pole / Foundation & Recovery Glaciers (V2) | East Antarctica | **152 files, 200.8 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01865 | VERIFIED |
| PolarGAP processed airborne RES (V1) | East Antarctica | **152 files, 200.8 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01552 | VERIFIED |
| Processed bed elevation picks from the **POLARGAP** radar survey, Pensacola-Pole Basin | East Antarctica | **1 file, 160.4 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01568 | VERIFIED |
| Dated radar stratigraphy **Dome A → South Pole** (AGAP North PASIN 2008-09 + PolarGAP PASIN2 2015-16) | East Antarctica | **3 files, 125 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01809 | VERIFIED |
| **AGAP** processed airborne RES, Gamburtsev Province | East Antarctica | **348 files, 54 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01544 | VERIFIED |
| **IMAFI** — Institute & Möller ice streams, Patriot Hills | West Antarctica | **325 files, 75.4 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01527 | VERIFIED |
| **WISE-ISODYN** — Wilkes Subglacial Basin | East Antarctica | **288 files, 58.7 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01521 | VERIFIED |
| **BBAS** — Pine Island Glacier basin | West Antarctica | **141 files, 30 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01529 | VERIFIED |
| Dated radar stratigraphy, **Pine Island Glacier** catchment (BBAS-PASIN + OIB-MCoRDS2) | West Antarctica | **13 files, 120 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01459 | VERIFIED |
| **ICEGRAV** — Recovery Catchment & interior Dronning Maud Land | East Antarctica | **129 files, 29 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01532 | VERIFIED |
| **GRADES-IMAGE** — Evans & Rutford ice streams, Ronne ice rises | West Antarctica | **136 files, 23.1 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01515 | VERIFIED |
| **Thwaites Glacier 2019** airborne survey, processed RES | Thwaites Glacier | **36 files, 22 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01322 | VERIFIED |
| Thwaites Glacier airborne survey — bed, surface elevation, ice thickness picks | Thwaites Glacier | **1 file, 46 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01520 | VERIFIED |
| **FISS 2016** — Filchner & Halley Ice Shelves, English Coast (V2) | West Antarctica | **115 files, 48.5 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01863 | VERIFIED |
| **FISS 2015** — Foundation Ice Stream, Bungenstock Ice Rise, Filchner (V2) | West Antarctica | **40 files, 13.3 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01864 | VERIFIED |
| **Ice radar data from Little Dome C** | **Dome C**, East Antarctica | **16 files, 300.2 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01623 | VERIFIED |
| **TOPAS** sub-bottom profiler, RRS James Clark Ross JR298 | Antarctic margin | **560 files, 13 GB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01517 | VERIFIED |
| Updated gravity-derived bathymetry, **Thwaites, Crosson and Dotson ice shelves** | Amundsen Sea sector | **5 files, 1.27 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/02123 | VERIFIED |
| Curie-depth points & geothermal heat-flow, Transantarctic Mts / Wilkes Subglacial Basin | East Antarctica | **11,569 files, 55 MB** | OGL v3 | https://data.bas.ac.uk/full-record.php?id=GB/NERC/BAS/PDC/01669 | VERIFIED |
| **BEDMAP3** standardised data points / shapefiles | Antarctica | **84 files, 6.9 GB** / **1,087 files, 4 GB** | CC-BY-4.0 | .../01614 · .../01502 | VERIFIED |
| **BEDMAP2** data points / shapefiles | Antarctica | **65 files, 2.4 GB** / **792 files, 2 GB** | CC-BY-4.0 | .../01616 · .../01618 | VERIFIED |
| **BEDMAP1** data points / shapefiles / grids | Antarctica | **1 file, 170 MB** / **6 files, 311 MB** / **4 files, 13 MB** | CC-BY-4.0 | .../01619 · .../01620 · .../01717 | VERIFIED |

---

# 3. PANGAEA — on-ice seismic (AWI and partners)

**Source, VERIFIED:** PANGAEA Elasticsearch API `https://ws.pangaea.de/es/pangaea/panmd/_search`.
Query `seismic AND (glacier OR icequake OR "ice sheet")` → **96 hits**;
`seismic AND "ice shelf"` → **15 hits**; `vibroseismic AND Antarctica` → **11 hits**;
`"Ekström Ice Shelf" AND seismic` → **4 hits**.
**Licence:** CC-BY-4.0 on every record checked. **Access:** open, no login, via
`https://doi.pangaea.de/10.1594/PANGAEA.<ID>` (tab-delimited download + zipped binaries).

*Note: PANGAEA's HTML search page renders results via JavaScript and returns nothing to a plain
fetch — use the `ws.pangaea.de` API endpoint above, not `www.pangaea.de/?q=`.*

| Dataset | Region | Type | Years | SIZE (verified) | Licence | DOI | Status |
|---|---|---|---|---|---|---|---|
| **Vibroseismic measurements on Thwaites Glacier, Antarctica, 2022/23 and 2023/24** (ITGC **GHOST** — Geophysical Habitat of Subglacial Thwaites; Zeising, Eisen, Hofstede, Brisbourne, Anandakrishnan). 210 km flow-parallel profile (2022/23) + 134 km flow-perpendicular profile (2023/24) | Thwaites Glacier (75.99–77.83 °S, 102.99–109.24 °W) | **Vibroseis active-source** | 2022/23 + 2023/24 | Parent collection of 2 child collections | CC-BY-4.0 | 10.1594/PANGAEA.987704 | VERIFIED (landing page opened) |
| Vibroseismic measurements on Thwaites Glacier, **2022/23** | Thwaites Glacier | Vibroseis | 2022/23 | **4 child datasets** (raw, stacked, migrated, attributes) | CC-BY-4.0 | 10.1594/PANGAEA.987687 | VERIFIED |
| Vibroseismic measurements on Thwaites Glacier, **2023/24** | Thwaites Glacier | Vibroseis | 2023/24 | **4 child datasets** | CC-BY-4.0 | 10.1594/PANGAEA.987693 | VERIFIED |
| **Raw data** of vibroseismic measurements on Thwaites Glacier, 2022/23 | Thwaites Glacier | **Raw vibroseis shot gathers** | 2022/23 | binary archive | CC-BY-4.0 | 10.1594/PANGAEA.987676 | VERIFIED |
| **Raw data** of vibroseismic measurements on Thwaites Glacier, 2023/24 | Thwaites Glacier | **Raw vibroseis shot gathers** | 2023/24 | multiple files | CC-BY-4.0 | 10.1594/PANGAEA.987694 | VERIFIED |
| **Stacked** vibroseismic section on Thwaites Glacier, 2022/23 | Thwaites Glacier | Stacked section | 2022/23 | 4 data points | CC-BY-4.0 | 10.1594/PANGAEA.987688 | VERIFIED |
| **Seismic attributes of ice base** from vibroseismic measurements on Thwaites Glacier, 2023/24 — reflection coefficients and acoustic impedance of the subglacial material along the 134 km profile | Thwaites Glacier | **Derived AVO / impedance** | 2023/24 | 2 data points | CC-BY-4.0 | 10.1594/PANGAEA.987703 | VERIFIED |
| **Sea floor depth under Ekström Ice Shelf from seismic vibroseis surveys 2010-2018** (Smith, Kuhn, Gaedicke, Drews, Ehlers, Franke, Hofstede, Lambrecht, Läufer, Mayer, Tiedemann, Eisen). Vibroseis source, **1500 m snow streamer, 60 channels** | Ekström Ice Shelf, Neumayer (70.52–71.93 °S, 7.49–9.43 °W) | **Vibroseis reflection** | 2010–2018 | **117,684 data points** | CC-BY-4.0 | 10.1594/PANGAEA.931928 | VERIFIED (landing page opened) |
| Sea floor bathymetry under **Ekström Ice Shelf** from a compilation of seismic vibroseis data | Ekström Ice Shelf, Neumayer | Derived bathymetry grid | 2019 | **21.5 MB** | CC-BY-4.0 | 10.1594/PANGAEA.907951 | VERIFIED |
| **Seismic reflection data of a basal channel and ocean cavity at the ice shelf-grounding line area of Support Force Glacier, Filchner Ice Shelf** | Filchner Ice Shelf | **Active-source reflection** | — | 54 data points | CC-BY-4.0 | 10.1594/PANGAEA.932278 | VERIFIED |
| Documentation of **Sub-EIS-Obs** sediment cores (companion to the Ekström vibroseis surveys) | Ekström Ice Shelf | Sediment cores | 2019 | 6-dataset collection | CC-BY-4.0 | 10.1594/PANGAEA.905409 | VERIFIED |
| Amundsen Sea shelf MCS profiles, RV Polarstern ANT-XXVI/3 | Amundsen Sea | **Marine MCS** | 2021 | **59.9–210.4 MB** each | CC-BY-4.0 | 10.1594/PANGAEA.933264 · .933265 · .933266 | VERIFIED |
| Vincennes Bay shelf profiles, RV Akademik Alexander Karpinsky (RAE59) | Vincennes Bay, East Antarctica | **Marine MCS** | 2026 | 6 data points each | CC-BY-4.0 | 10.1594/PANGAEA.991550 · .991551 | VERIFIED |

---

# 4. Greenland & the Arctic — FDSN network codes

**Source, VERIFIED:**
`https://service.earthscope.org/fdsnws/station/1/query?minlatitude=59&maxlatitude=84&minlongitude=-75&maxlongitude=-10&level=network&format=text`
plus `https://www.fdsn.org/networks/?search=greenland` and `?search=glacier`.

## 4.1 GLISN — Greenland Ice Sheet Monitoring Network

| Network | Name | Region | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|---|
| **GG** | **GLISN** — Greenland Ice Sheet Monitoring Network | Greenland-wide | Permanent broadband, multinational federated | 2012 → open-ended (registry end date 2599) | **1 station under the GG code: SE1, Kagssortoq, Greenland (63.24852 °N, −42.03487 °W), live from 2016-06-15** | 10.7914/SN/GG | VERIFIED (MDA page opened) |

**Important caveat, VERIFIED:** GLISN is a *federation*, not a single archived network. Only **one**
station (SE1) actually carries the `GG` code at the DMC. The remaining ~30 GLISN stations are
archived under their **operator** codes — principally **DK** (Danish Seismological Network / GEUS,
**22 stations** in the Greenland box), plus **GE** (GEOFON), **IU** and **II** (GSN), and **CN**
(Canada). To assemble the full GLISN dataset you must query those codes by station, not `GG`.

## 4.2 Greenland Ice Sheet — glaciological / cryoseismic deployments

| Network | Name | Region | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|---|
| **DK** | Danish Seismological Network (GEUS) — carries most GLISN Greenland sites | Greenland | Permanent broadband | 1976 → ongoing | **22 stations** in box | — | VERIFIED |
| **6H** | Imaging subglacial hydrology beneath the Greenland Ice Sheet | Greenland Ice Sheet | Passive / nodal | 2022 | **24 stations** | 10.7914/SN/6H_2022 | VERIFIED |
| **9C** | **SIIOS** — Seismometer to Investigate Ice and Ocean Structure, Greenland | Greenland Ice Sheet | Passive (planetary analogue) | 2018 | **21 stations** | 10.7914/SN/9C_2018 | VERIFIED |
| **4B** | SIIOS Field Experiment: **Lake Europa**, Greenland | Greenland | Passive (planetary analogue) | 2022 | **2 stations** | 10.7914/aqbv-fc17 | VERIFIED |
| **6R** | SIIOS Field Experiment | Polar | Passive (planetary analogue) | 2022 | — | 10.7914/nw0b-4c40 | VERIFIED (code+DOI) |
| **Y6** | Behaviour of **supraglacial lakes** and their role in outlet glacier dynamics and mass balance | Greenland Ice Sheet | Passive | 2006–2012 | **20 stations**, 7 yr | 10.7914/SN/Y6_2006 | VERIFIED |
| **ZS** | **CReSIS Greenland Lake Drainage 2009** | Greenland supraglacial lakes | Passive / active | 2009 | **4 stations** | 10.7914/SN/ZS_2009 | VERIFIED |
| **XW** | **CReSIS Greenland 2012** | Greenland Ice Sheet | Passive / active | 2012 | **8 stations** | 10.7914/SN/XW_2012 | VERIFIED |
| **10** | Hydrofracture at Greenland Lakes | Greenland supraglacial lakes | Passive | 2022–2023 | — | 10.7914/x1dm-nq93 | VERIFIED (code+DOI) |
| **5Q** | West Greenland **Moulins**, Sermeq Avannarleq | West Greenland | Passive | 2018 | **8 stations** | 10.7914/h6ar-x071 | VERIFIED |
| **14** | **GRuMPS** — Greenland Runoff Monitoring from Passive Seismology | Greenland | Passive | 2023–2027 | **1 station** so far | 10.7914/q2mq-bf42 | VERIFIED |
| **7T** | **Greenland SLIDE** project passive seismic network | Greenland Ice Sheet | Passive | 2023–2025 | **6 stations** | 10.7914/rbne-ad45 | VERIFIED |
| **ZO** | Seismic Monitoring of Greenland's Melting Ice Sheet | Greenland Ice Sheet | Passive | 2006 | **10 stations** | 10.7914/SN/ZO_2006 | VERIFIED |
| **7E** | Glacioseismic Monitoring of Rumblings in **Jakobshavn** Glacier | Jakobshavn Isbræ | Passive | 2010–2011 | **9 stations** | 10.7914/SN/7E_2010 | VERIFIED |
| **X3** | Understanding the thinning and acceleration of **Jakobshavn Isbræ** | Jakobshavn Isbræ | Passive | 2007–2011 | **2 stations** | 10.7914/SN/X3_2007 | VERIFIED |
| **3Z** | Glaciological monitoring of **Jakobshavn Isbræ** (SED/ETH — data at SED, not EarthScope) | Jakobshavn Isbræ | Passive | 2021–2024 | — | 10.12686/sed/networks/3z_2021 | VERIFIED (code+DOI) |
| **YM** | Physical controls on ocean-terminating glacier variability, **central west Greenland** | West Greenland | Passive | 2013–2015 | **4 stations** | 10.7914/SN/YM_2013 | VERIFIED |
| **9D** | Ice-ocean interaction at **Nuuk tidewater glaciers** | Nuuk fjords | Passive | 2010–2012 | **2 stations** | 10.7914/SN/9D_2010 | VERIFIED |
| **YF** | Observation of a glacier **calving event** using a network of GPS and seismic sensors | Greenland | Passive + GPS | 2012–2027 | **7 stations** | 10.7914/SN/YF_2012 | VERIFIED |
| **6D** | Temporary seismic deployments on **Bowdoin Glacier**, NW Greenland | Bowdoin Glacier | Passive | 2019 | — | — | VERIFIED (code+dates) |
| **XR** | **Bowdoin Glacier**, NE Greenland | Bowdoin Glacier | Passive | 2015 | — | — | VERIFIED (code+dates) |
| **ZA** | **Russell Glacier Catchment** 2009-12 | SW Greenland | Passive | 2009–2010 | — | — | VERIFIED (code+dates) |
| **XQ** | Basal hydrologic connectivity & impact on sliding, **West Greenland ablation zone** | West Greenland | Passive geophysical | 2026–2027 | — | 10.7914/zt6p-kj33 | VERIFIED (code+DOI) |
| **7Q** | **Greenland Ice Drilling for Climate History — site selection** (the closest FDSN entry to the NEEM/EGRIP deep-drilling programme) | Greenland ice-core sector | Active / passive site survey | 2023 | — | 10.7914/m8g7-4390 | VERIFIED (code+DOI) |
| **9R** | **DEGLASEIS** — NE Greenland Deglaciation Seismology (the closest FDSN entry to the **NEGIS** sector) | NE Greenland | Passive | 2025–2026 | — | — | VERIFIED (code+dates) |
| **1E** | ELLITE | Greenland | Passive | 2010–2012 | **9 stations** | — | VERIFIED |
| **DY** | Polar Seismic Italian Network (David) — INGV; covers **Wolstenholme Fjord, NW Greenland** as well as David Glacier, Antarctica | NW Greenland + Antarctica | Permanent broadband | 2003 → | — | 10.13127/sd/n2im7z-ttv | VERIFIED (registry) |

## 4.3 Greenland lithosphere / crustal deployments

| Network | Name | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|
| **XF** | Understanding Precambrian to Present Assembly of Greenland | Passive broadband | 2014–2016 | **7 stations** | 10.7914/SN/XF_2014 | VERIFIED |
| **ZN** | Lithospheric structure of West Greenland | Passive broadband | 2006–2007 | **5 stations** | — | VERIFIED |
| **9B** | TopoGreenland | Passive broadband | 2011 | — | 10.7914/SN/9B_2011 | VERIFIED (code+DOI) |
| **9F** | GreenlandSeismic (RESIF 2023, then EarthScope 2024-25) | Passive broadband | 2023 · 2024–2025 | — | 10.15778/RESIF.9F2023 · 10.7914/a9fc-5r56 | VERIFIED (codes+DOIs) |
| **YW** | Tectonic Influence on the Greenland Ice Sheet | Passive broadband | 2026–2029 | — | 10.7914/7gvn-wy77 | VERIFIED (code+DOI) |
| **XV** | **ICEMELT** Broadband Seismometer Experiment | Passive broadband | 1993–1996 | **16 stations** | — | VERIFIED |
| **YV** | North East Atlantic Tomography | Passive broadband | 2000–2003 | **13 stations** | — | VERIFIED |
| **CN** | Canadian National Seismograph Network | Permanent broadband | 1975 → ongoing | **302 stations** | — | VERIFIED |
| **PO** | **POLARIS** — Portable Observatories for Lithospheric Analysis and Research Investigating Seismicity | Passive broadband | 2000 → ongoing | **201 stations** | — | VERIFIED |
| **X5** | Hudson Bay Lithospheric Experiment | Passive broadband | 2007–2011 | **18 stations** | — | VERIFIED |

## 4.4 Canadian Arctic ice shelves, sea ice & Arctic rivers

| Network | Name | Type | Years | DOI | Status |
|---|---|---|---|---|---|
| **8U** | Seismic reconnaissance of **Milne Ice Shelf**, Nunavut, as a platform for sea-ice study using microseism | Passive | 2023 | 10.7914/8nm9-4h22 | VERIFIED (code+DOI) |
| **6W** | Milne Ice Shelf reconnaissance — year 2 | Passive | 2024 | 10.7914/d732-7v08 | VERIFIED (code+DOI) |
| **X1** | Mechanical interaction of **ocean waves and sea ice** observed by **DAS**, seismometers and hydrophone (WHOI) | **DAS + seismometers + hydrophone** | 2025 | 10.7914/z4fp-3j26 | VERIFIED (code+DOI) |
| **6C** | Listening for sediment transport and **river ice dynamics in Arctic Rivers** — Year 2 | Passive | 2024 | 10.7914/18bs-ec71 | VERIFIED (code+DOI) |
| **1H** | Geophones for quantifying bedload transport and **river ice break-up** | Passive | 2023 | 10.7914/ef6x-5102 | VERIFIED (code+DOI) |
| **8L** | **Mt. Meager Geothermal Nodal Array** (Univ. of Calgary) — glaciated volcanic massif, BC | **Nodal** | 2019 | 10.7914/SN/8L_2019 | VERIFIED |

## 4.5 Svalbard

| Network | Name | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|
| **NO** | **NORSAR** — Norwegian Seismic Array Network (includes the **SPITS** array, Spitsbergen) | Permanent array | 1971 → ongoing | **12 stations** in the Svalbard box | — | VERIFIED |
| **N9** | **Svalbard Glaciers Surge Monitoring** | Passive, glacier | active | — | 10.7914/g6dz-5a09 | VERIFIED (code+DOI) |
| **5W** | **SUBMERSE** Svalbard OBS deployment | OBS | 2023–2024 | — | 10.7914/12vn-4z72 | VERIFIED (code+DOI) |
| **X2** | CGF-Svalbard | Passive | 2023 | — | 10.7914/1b8m-rj75 | VERIFIED (code+DOI) |
| **XG** | Svalbard — **Vallunden** (RESIF; lake/sea-ice) | Passive | 2019 | — | 10.15778/RESIF.XG2019 | VERIFIED (code+DOI) |
| **PL** | Polish Seismological Network (Hornsund, Svalbard) | Permanent | 1990 → ongoing | **8 stations** in box | — | VERIFIED |

## 4.6 Iceland glaciers

| Network | Name | Type | Years | SIZE (verified) | DOI | Status |
|---|---|---|---|---|---|---|
| **5L** | **Seismic array data for monitoring & tracking tremor sources during subglacial floods (jökulhlaups) and volcanic eruptions at Vatnajökull** — GFZ + Dublin Inst. for Advanced Studies + Icelandic Met Office | Passive array | 2013–2017 | **25 stations, ~574 GB miniSEED** — the only polar/glacial network I found with a published byte volume | 10.14470/0Y7568667884 | **VERIFIED — CC-BY-4.0, open, via GEOFON FDSN web services** |
| **ZK** | **Vatnajökull Icequake and Tremor Array: Lite** | Passive icequake array | 2014 | **18 stations** | — | VERIFIED |
| **ZN** | Investigation of subglacial hydrologic seismic signals, **Breiðamerkurjökull** — a WISSARD test case | Passive | 2013 | **6 stations** | 10.7914/SN/ZN_2013 | VERIFIED |
| **7J** | Correlating seismic and visual (TLS) signals at **Breiðamerkurjökull** | Passive + TLS | 2011 | **4 stations** | 10.7914/SN/7J_2011 | VERIFIED |
| **8K** | Northern Volcanic Zone Iceland | Passive broadband | 2016–2022 | — | 10.7914/SN/8K_2016 | VERIFIED (code+DOI) |
| **Z7** | Northern Volcanic Zone | Passive broadband | 2010–2015 | **219 stations** | — | VERIFIED |
| **XD** | HOTSPOT — Seismic study of the Iceland hotspot | Passive broadband | 1996–1998 | **33 stations** | — | VERIFIED |

---

# 5. USAP-DC (US Antarctic Program Data Center)

**Source, VERIFIED:** DataCite API on the USAP-DC prefix.
`https://api.datacite.org/dois?prefix=10.15784&query=seismic` → **meta.total = 20**;
`…&query=icequake OR "active source" OR refraction OR geophone OR nodal` → **meta.total = 3**;
a broad geophysics query (`"ice stream" OR Thwaites OR WISSARD OR SALSA OR Whillans OR radar`)
→ **meta.total = 122** (overwhelmingly radar/ApRES/oceanographic; only a handful seismic).

**Licence:** CC-BY-4.0 on every USAP-DC record checked. **Access model:** open, no login;
landing page `https://www.usap-dc.org/view/dataset/<ID>` with a direct file download and MD5.

**Key structural fact:** USAP-DC hosts **derived products and catalogues, not raw waveform
archives**. Raw USAP-funded waveforms live at EarthScope under the network codes in Section 1.
Also note the USAP-DC HTML search UI (`https://www.usap-dc.org/search?searchType=dataset&q=seismic`)
returned an error page and `https://www.usap-dc.org/api/dataset/search` 404'd — **use the DataCite
API instead**.

| Dataset | Region | Type | Year | SIZE | Licence | URL | Status |
|---|---|---|---|---|---|---|---|
| **Icequake Catalog from Rutford Ice Stream, West Antarctica, January 2019** (Lee, Anandakrishnan, Alley). 29 stations, QuakeMigrate, target depths 1200–2000 m, 4–26 Jan 2019 | Rutford grounding line (78.28–78.33 °S, 83.26–83.49 °W) | Icequake catalogue (CSV + README) | 2025 | **64.0 MB** (`Rutford_GL_Icequake_Catalog.zip`, MD5 `c7c960b9848cdf5e04ab28e41fe919b9`) | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601932 | VERIFIED (landing page opened) |
| **Sub-ice-shelf seafloor elevation from point-source active-seismic data, Thwaites Eastern & Dotson Ice Shelves** (companion to FDSN `5I` TARSAN) | Thwaites Eastern / Dotson Ice Shelves | Derived from **active-source** seismic | 2024 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601827 | VERIFIED (metadata) |
| **UW Ringshear Seismic data** | Laboratory (ring-shear, ice–till interface) | Lab seismic | 2025 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/602012 | VERIFIED (metadata) |
| **A seismic catalog for the southernmost continent** | Antarctica-wide | Event catalogue | 2024 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601805 | VERIFIED (metadata) |
| **East Antarctic Seismicity from different Automated Event Detection Algorithms** | East Antarctica | Detection-algorithm comparison (**ML-relevant**) | 2024 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601762 | VERIFIED (metadata) |
| **Models from "Applying Machine Learning to Characterize and Extrapolate…"** | Antarctica | **ML models** | 2025 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601943 | VERIFIED (metadata) |
| **Full Waveform Ambient Noise Tomography for East Antarctica** | East Antarctica | Tomographic model | 2024 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601763 | VERIFIED (metadata) |
| **Shear Wave Velocity of the Antarctic Upper Mantle from Full Waveform Inversion** | Antarctica | Velocity model | 2023 & 2025 | not stated | CC-BY-4.0 | .../601744 · .../601909 | VERIFIED (metadata) |
| **Crustal thicknesses in Antarctica from Sp receiver functions** | Antarctica | Receiver-function product | 2025 (2 records) | not stated | CC-BY-4.0 | .../601898 · .../601978 | VERIFIED (metadata) |
| **2D shear-wave velocity model across the West Antarctic Rift System** | West Antarctic Rift | Velocity model | 2021 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601423 | VERIFIED (metadata) |
| **Investigating Ultra-low Velocity Zones (ULVZs) using an Antarctic Dataset** | Antarctica / deep mantle | Waveform analysis | 2020 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601265 | VERIFIED (metadata) |
| **Upper Mantle Seismic Structure beneath the Northern Transantarctic Mountains** (TAMNNET / `ZJ`) | N. Transantarctic Mts | Tomographic model | 2017 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/601017 | VERIFIED (metadata) |
| **Shear Wave Splitting Analysis and Seismic Anisotropy** | Antarctica | Anisotropy product | 2017 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/601019 | VERIFIED (metadata) |
| **A New Approach to Investigate the Seismic Velocity Structure beneath Antarctica** | Antarctica | Velocity model | 2014 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/600132 | VERIFIED (metadata) |
| **Ross Sea unconformities digital grids in depth and two-way time** | Ross Sea | Interpreted **MCS** horizons | 2018 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/601098 | VERIFIED (metadata) |
| **Ross Sea post-middle Miocene seismic interpretation** | Ross Sea | Interpreted **MCS** horizons | 2019 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/601227 | VERIFIED (metadata) |
| **Geophysical data from Crary Ice Rise, Ross Sea Embayment** | Crary Ice Rise | Mixed geophysics incl. seismic | 2019 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/601181 | VERIFIED (metadata) |
| **Geophysical measurements, Beardmore Glacier** | Beardmore Glacier | Mixed geophysics | 2018 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/601121 | VERIFIED (metadata) |
| **LISSARD** — Lake and Ice Stream Subglacial Access Research Drilling (**WISSARD** sub-project) | Subglacial Lake Whillans | Project data incl. geophysics | 2016 | not stated | CC-BY-4.0 | http://www.usap-dc.org/view/dataset/600154 | VERIFIED (metadata) |
| **Wideband magnetotelluric responses from Whillans Ice Stream** | Whillans Ice Stream | MT (companion to seismic) | 2022 | not stated | CC-BY-4.0 | https://www.usap-dc.org/view/dataset/601526 | VERIFIED (metadata) |
| **SALSA / Mercer Subglacial Lake** — sediment porewater, discrete bulk sediment, water-column biogeochemistry, CTD, noble gas & isotopic data | Mercer Subglacial Lake | **Non-seismic** SALSA companion data | 2021–2023 | not stated | CC-BY-4.0 | .../601664 · .../601663 · .../601661 · .../601657 · .../601498 | VERIFIED (metadata) — **no SALSA seismic dataset exists on USAP-DC** |

---

# 6. Australian Antarctic Data Centre (AADC)

**Source, VERIFIED:** `https://api.datacite.org/dois?prefix=10.26179&query=seismic` → **meta.total = 6**
(broadening the query to `seismic OR icequake OR geophone OR sonobuoy` returned the same 6).
**Access model:** metadata record at `https://data.aad.gov.au/metadata/<ID>`, data via the AADC portal.
**Rights were not populated in any of the six DataCite records — check each landing page before use.**

| Dataset | Region | Type | Years | SIZE | Licence | URL / DOI | Status |
|---|---|---|---|---|---|---|---|
| **Hammer plate seismic on the Shackleton Ice Shelf** | Shackleton Ice Shelf, East Antarctica | **Active-source (hammer/plate) refraction** | 2023–24 | not stated | not stated | https://data.aad.gov.au/metadata/AAS_4629_HPSeis_23-24 · 10.26179/s72d-3z71 | VERIFIED (metadata) |
| **Seismic reflection ice thickness and elevation data: Kemp Land 1957-1959** — IGY-era | Kemp Land, East Antarctica | **Historic active-source reflection** | 1957–1959 | not stated | not stated | http://data.aad.gov.au/metadata/Kemp_Ht_1957-59 · 10.26179/5b92195b1659f | VERIFIED (metadata) |
| **Seismic data collected in East Antarctica with broadband seismometers, 2015 onwards** | East Antarctica (Mawson / Casey / Davis) | Passive broadband | 2015 → | not stated | not stated | https://data.aad.gov.au/metadata/AAS_4318_seismic_data · 10.26179/g5gj-2y98 | VERIFIED (metadata) |
| **Casey-Wilkins Adaptable Array: Broadband Seismic Data** | Casey / Wilkins, East Antarctica | Passive broadband array | pub. 2027 | not stated | not stated | https://data.aad.gov.au/metadata/AAS_4591_Seismic_Casey-Wilkins_Adaptable_Array · 10.26179/x596-ew14 | VERIFIED (metadata) |
| **IN2020_V01 — Multichannel Seismic Reflection (MCS) dataset** (RV Investigator) | Southern Ocean / East Antarctic margin | **Marine MCS** | 2020 | not stated | not stated | https://data.aad.gov.au/metadata/AAS_4519_IN2020_V01_MCS · 10.26179/qe01-db93 | VERIFIED (metadata) |
| **Davis to Law Cairn survey** (natural surface levels, hand auger pits — runway proposal) | Vestfold Hills | Site-investigation geophysics | 2012–13 | not stated | not stated | https://data.aad.gov.au/metadata/Vestfold_Hills_CPD_2012_13 · 10.26179/wpy3-v740 | VERIFIED (metadata) |

---

# 7. Alpine, mountain & tidewater glaciers — FDSN network codes

**Source, VERIFIED:** `https://www.fdsn.org/networks/?search=glacier` and `?search=meager`.

## 7.1 Alpine / European

| Network | Name | Region | Type | Years | DOI | Status |
|---|---|---|---|---|---|---|
| **4D** | **Seismological Experiments on Swiss Glaciers** (SED/ETH Zürich) — the umbrella code covering the **Gornergletscher**, **Rhonegletscher** and Aletsch deployments | Swiss Alps | Passive, glacier | **1985–2009** | 10.12686/sed/networks/4d | VERIFIED |
| **4D** | **Swiss temporary deployments on glaciers** (SED/ETH) — modern continuation of the same code | Swiss Alps | Passive, glacier | **2012–2030** | 10.12686/sed/networks/4d | VERIFIED |
| **1D** | **Glacier d'Argentière** (RESIF, French Alps) — the FDSN half of the RESOLVE project | Mont Blanc massif, France | Dense passive array | 2019–2020 | 10.15778/RESIF.1D2019 | VERIFIED |
| **XT** | **TSARMINE** rock-glacier monitoring | Swiss Alps | Passive, rock glacier | 2021–2022 | — | VERIFIED (code+dates) |

Note: `4D` and `1D_2019` are **not** archived at EarthScope. Route requests to
**SED/ETH** (`http://eida.ethz.ch/fdsnws/dataselect/1/query`) and **RESIF/EPOS-France**
(`https://ws.resif.fr/fdsnws/dataselect/1/query`) respectively.

## 7.2 Generic glacier-process experiments

| Network | Name | Type | Years | DOI | Status |
|---|---|---|---|---|---|
| **2E** | **Reflection and Refraction Active Seismic Acquisition on Sourdough Rock Glacier** | **Active-source reflection + refraction** | 2021 | 10.7914/SN/2E_2021 | VERIFIED |
| **1B** | Using passive seismics to determine a glacier **sliding law** | Passive | 2019 | 10.7914/SN/1B_2019 | VERIFIED |
| **3C** | Glacier seismicity and its relationship to basal motion | Passive | 2010–2011 | 10.7914/SN/3C_2010 | VERIFIED |
| **XV** | Glacier Seismicity and High-Resolution Motion Records: Relation to Glacier Erosion | Passive | 2007–2008 | 10.7914/SN/XV_2007 | VERIFIED |
| **YE** | Water storage and routing within glaciers via planar voids | Passive | 2007 | 10.7914/SN/YE_2007 | VERIFIED |
| **XF** | Relating glacier-generated seismicity to ice motion, basal processes and iceberg calving | Passive | 2009–2011 | 10.7914/SN/XF_2009 | VERIFIED |

## 7.3 Alaskan glaciers

| Network | Name | Type | Years | DOI | Status |
|---|---|---|---|---|---|
| **YV** | **Bering Glacier Surge** Seismic Experiment | Passive | 2010 | 10.7914/SN/YV_2010 | VERIFIED |
| **ZR** | Reconnaissance survey of **Bering Glacier** basal seismicity and calving | Passive | 2007 | 10.7914/SN/ZR_2007 | VERIFIED |
| **ZR** | **Bering Glacier** Field Camp 2008 | Passive | 2008 | 10.7914/SN/ZR_2008 | VERIFIED |
| **YM** | **Columbia Glacier** Passive Seismic Experiment | Passive | 2004–2005 | 10.7914/SN/YM_2004 | VERIFIED |
| **XL** | Dynamic controls on tidewater glacier retreat (Columbia sector) | Passive | 2008–2011 | 10.7914/SN/XL_2008 | VERIFIED |
| **YO** | Tidewater glacier and ice-marginal dynamic behaviour | Passive | 2010–2011 | 10.7914/SN/YO_2010 | VERIFIED |
| **5C** | Dynamics of Lake-Calving Glaciers: **Yakutat Glacier** | Passive | 2009–2011 | 10.7914/SN/5C_2009 | VERIFIED |
| **ZQ** | **Taku Glacier** | Passive | 2015–2016 | 10.7914/SN/ZQ_2015 | VERIFIED |
| **YG** | Passive Seismic Observations of a glacier surge: **Turner Glacier** | Passive | 2020–2023 | 10.7914/SN/YG_2020 | VERIFIED |
| **1W** | Passive Seismic Observations of a glacier surge: **Turner Glacier** (phase 2) | Passive | 2024–2025 | 10.7914/t59y-k271 | VERIFIED |
| **3J** | Detecting buried ice in the forelands of **Malaspina Glacier** | Passive / active | 2021–2022 | 10.7914/SN/3J_2021 | VERIFIED |
| **X5** | **Lemon Creek Glacier** — UTEP | Passive | 2017 | 10.7914/SN/X5_2017 | VERIFIED |
| **YY** | **Mendenhall Glacier** Outburst Flood Seismicity and Next-Generation Instrument Testing | Passive | 2012 | 10.7914/SN/YY_2012 | VERIFIED |
| **3L** | Juneau Icefield Research Program | Passive | 2024 | 10.7914/4ygw-ys36 | VERIFIED |
| **XJ** | Impact of subglacial discharge on turbulent plume dynamics and ocean-glacier heat exchange | Passive | 2016–2017 | 10.7914/SN/XJ_2016 | VERIFIED |
| **X6** | Seismic Observations of **Glacier Creek** to Infer Timing and Magnitude of Bedload Transport | Passive | 2019–2020 | 10.7914/SN/X6_2019 | VERIFIED |
| **ZI** | Ambient Seismic Noise at Glacier Creek Preserve | Passive | 2026 | 10.7914/48ga-j113 | VERIFIED |

---

# 8. Cryoseismology file repositories (Zenodo) — including ML-ready sets

**Source, VERIFIED:** Zenodo REST API (`https://zenodo.org/api/records?q=…`). Sizes are the summed
`files` entries; licences are the record `license.id`. **Access:** direct anonymous HTTP download
from the record page, no login.

| Dataset | Region | Type | Year | SIZE (verified) | Licence | URL | Status |
|---|---|---|---|---|---|---|---|
| **Icequakes from Gornergletscher, Switzerland (Summer 2007)** | Gornergletscher, Swiss Alps | **Labelled icequake waveform set — ML-ready** | 2022 | **~87.6 MB** | **MIT** | https://zenodo.org/records/7007378 | VERIFIED |
| **Seismic Noise from Gornergletscher, Switzerland (Summer 2007)** — the matching negative class | Gornergletscher, Swiss Alps | **Labelled noise set — ML-ready** | 2022 | **~356 MB** | **MIT** | https://zenodo.org/records/6913695 | VERIFIED |
| **Icequake and Earthquake waveforms** | Glacier + tectonic | **Labelled two-class waveform set — ML-ready** | 2023 | **~1.5 GB** | CC-BY-4.0 | https://zenodo.org/records/7523349 | VERIFIED |
| **Saskatchewan Glacier Basal Icequake Event Repository** | Saskatchewan Glacier, Canadian Rockies | **Labelled basal icequake catalogue + waveforms** | 2023 | **~5.4 GB** | CC-BY-4.0 | https://zenodo.org/records/8393876 | VERIFIED |
| Icequake catalogues and velocity model for *"Array processing in cryoseismology"* | Glacier | Icequake catalogue | 2023 | **~3.1 MB** | CC-BY-4.0 | https://zenodo.org/records/8120941 | VERIFIED |
| **Icequake rupture suggests Antarctic ice stream beds may be stronger, yet more dynamic than assumed** | Antarctic ice stream | Icequake catalogue | 2025 | **~7.3 MB** | CC-BY-4.0 | https://zenodo.org/records/17311423 | VERIFIED |
| **Friction and slip measured at the bed of an Antarctic ice stream** | Rutford Ice Stream | Basal icequake / seismic | 2023 | **~33 MB** | CC-BY-4.0 | https://zenodo.org/records/7870307 | VERIFIED |
| **Quantifying subsurface fracture damage in glaciers using fibre-optic seismology** | Glacier | **DAS** | 2025 | **~2.6 GB** | CC-BY-4.0 | https://zenodo.org/records/18094550 | VERIFIED |
| **Seismic investigation of an Arctic glacier accelerating under climate warming** | Arctic glacier | Passive seismic waveforms | 2023 | **~5.6 GB** | CC-BY-4.0 | https://zenodo.org/records/10121799 | VERIFIED |
| **Self-sufficient seismic boxes for monitoring glacier seismology in Greenland** | Greenland | Passive seismic (instrument + data) | 2022 | **~15.7 GB** | CC-BY-4.0 | https://zenodo.org/records/7516192 | VERIFIED |
| **DATA of the RESOLVE Project** (Glacier d'Argentière; companion to FDSN `1D_2019`) | Glacier d'Argentière, French Alps | Dense passive array | 2020 | **~750 MB** | CC-BY-4.0 | https://zenodo.org/records/10013212 | VERIFIED |
| Unlocking DAS amplitude information through coherency coupling quantification | DAS methodology | **DAS** | 2024 | **~1 GB** | CC-BY-4.0 | https://zenodo.org/records/13684046 | VERIFIED |
| **Python package for icequake inversions** — source positions and ice thickness from sea ice in Svalbard, March 2019 | Svalbard sea ice | Software | 2023 | **50,765 bytes** | CC-BY-4.0 | https://zenodo.org/records/7755633 | VERIFIED |
| **GNSS data at the Astrolabe Glacier** (companion geodesy) | Astrolabe Glacier, Adélie Land | GNSS | 2024 | **~995 MB** | CC-BY-4.0 | https://zenodo.org/records/14003385 | VERIFIED |

---

# 9. ML benchmark status — an important negative result

**SeisBench**, the de-facto standard seismic ML benchmark library
(`https://github.com/seisbench/seisbench`), was checked in full via
`https://seisbench.readthedocs.io/en/stable/pages/data/benchmark_datasets.html`.

**VERIFIED: SeisBench contains no glacier, icequake, cryosphere, polar, Antarctic or Greenland
benchmark dataset.** Its 24 benchmark sets are AQ2009, Bohemia, CEED, CREW, CWA, ESM25, ETHZ,
EQSDenoiser, GEOFON, INSTANCE, Iquique, ISC-EHB Depth Phases, LENDB, LFE Stack Datasets, MLAAPDE,
NEIC, OBS, OBST2024, PiSDL, PNW, SCEDC, STEAD, TXED and VCSEIS — all tectonic, volcanic, induced
or ocean-bottom. The nearest analogues in spirit are **PNW** (which includes "exotic events") and
**VCSEIS** (volcanic).

**Implication:** there is a genuine gap. If you want a cryoseismology ML benchmark you must build
it from the Section 8 Zenodo sets. The most benchmark-shaped starting points, in order:

1. **Gornergletscher pair** (icequakes 87.6 MB + matched noise 356 MB, MIT licence) — the cleanest
   ready-made positive/negative pair, and the permissive MIT licence makes redistribution easy.
2. **Icequake and Earthquake waveforms** (~1.5 GB, CC-BY-4.0) — a two-class discrimination task.
3. **Saskatchewan Glacier Basal Icequake Event Repository** (~5.4 GB, CC-BY-4.0) — largest labelled
   basal-icequake set found.
4. **BAS Rutford microseismic icequake catalogue** (56 MB) + **shear-wave splitting catalogue**
   (606,545 files, 12 GB) — pair these with the `9B`/`6L`/`5B` FDSN waveforms for a full
   detection-and-location benchmark on a single well-studied ice stream.
5. **USAP-DC Rutford Icequake Catalog** (64.0 MB, 29 stations, QuakeMigrate labels) — a second,
   independently produced label set over the same glacier, which makes label-noise studies possible.
6. **USAP-DC East Antarctic Seismicity from different Automated Event Detection Algorithms** — an
   explicit multi-detector comparison, useful as an evaluation baseline.

---

# 10. What I could NOT confirm

| Item requested | Outcome |
|---|---|
| **ANTALITH** | **Not confirmed.** No FDSN network code, DataCite record or repository entry under this name was returned by any query (`fdsn.org/networks/?search=antalith` returned an empty table). The closest verified Italian Antarctic seismic entity is **DY, "Polar Seismic Italian Network (David)"**, INGV, 2003→, DOI 10.13127/sd/n2im7z-ttv, covering David Glacier (Antarctica) and Wolstenholme Fjord (NW Greenland). If ANTALITH exists it is likely a project name whose data sit under `DY` or `AI` — treat as unresolved. |
| **PolarGAP seismic** | **No on-ice seismic dataset exists.** PolarGAP was an airborne radar / gravity / magnetics survey. The verified deliverables are BAS PDC RES (152 files, 200.8 GB, OGL v3) and the Pensacola-Pole Basin bed picks (160.4 MB). Section 2.3. |
| **AGAP seismic** | Split across two verified holdings: the **ZM** FDSN network (30 stations, 2007–2013, DOI 10.7914/SN/ZM_2007) for passive broadband, and BAS PDC AGAP airborne RES (348 files, 54 GB) for radar. No separate AGAP active-source seismic file archive found. |
| **SALSA (Subglacial Lake Mercer) seismic** | **No seismic dataset found.** USAP-DC holds SALSA sediment porewater, bulk sediment, water-column biogeochemistry, CTD and noble-gas data (CC-BY-4.0) but nothing seismic. The seismic survey work at Subglacial Lake Whillans is covered by FDSN `YD` (WISSARD, 40 stations) and `4A`. |
| **Vostok seismic** | **Not confirmed.** No open dataset, FDSN code or repository record found for seismic acquisition at Vostok Station or over Lake Vostok. Russian Antarctic Expedition data are not in FDSN, DataCite, PANGAEA or Zenodo indices I queried. |
| **Dome C seismic** | Only the **GEOSCOPE CCD** permanent station (Concordia) is verified, plus the **9R / EAIIST** traverse network (2019–2021) and BAS Little Dome C radar (16 files, 300.2 MB). No dedicated Dome C active-source seismic dataset found. |
| **Dome A seismic** | Covered by **ZM** (AGAP/GAMSEIS, 30 stations) and **9U** (Dome A magnetotellurics, 2024–25). No separate Dome A active-source seismic archive found. |
| **Store Glacier (Sermeq Kujalleq) seismic / DAS** | **Not confirmed.** A Zenodo search for "Store Glacier" returned only calving-model, velocity-field and SST datasets — no seismic or DAS record. The Store Glacier DAS work is likely held institutionally (Leeds / Aberystwyth / Swansea) rather than in an open repository. |
| **Helheim Glacier** | **No dedicated FDSN network code found** (`fdsn.org/networks/?search=helheim` empty). The one Helheim item located is a USAP-DC *remote-sensing* melt dataset (601841), not seismic. Helheim seismicity is generally analysed from GLISN/DK regional stations. |
| **NEEM / EGRIP / NEGIS** | **No network code carries these names** (`?search=EGRIP` empty). Closest verified: **7Q** "Greenland Ice Drilling for Climate History; site selection" (2023, DOI 10.7914/m8g7-4390) and **9R** "DEGLASEIS — NE Greenland Deglaciation Seismology" (2025–2026), which covers the NEGIS sector. |
| **Byte volumes for FDSN networks** | Not published for any polar network except **5L** (574 GB). Section 1/4/7 SIZE columns give station-counts instead. Do not quote a GB figure for those without measuring it. |
| **AADC licences** | The `rightsList` field was **empty in all six** AADC DataCite records. Licence must be checked on each `data.aad.gov.au/metadata/` landing page before redistribution. |
| **USAP-DC file sizes** | Only exposed on the HTML landing page, not in DataCite. I opened one (601932 → 64.0 MB); the rest are marked "not stated". |
| **Network `7T` "LHS"** | 195 stations south of 60°S, 2019–2020 — a genuinely large nodal deployment, but the registry gives no expansion of the acronym and no DOI. Purpose unconfirmed. |
| **Gornergletscher / Rhonegletscher FDSN codes** | No dedicated per-glacier codes exist; both fall under the SED umbrella code **4D**. The Gornergletscher *data* are instead available as the two Zenodo sets in Section 8. |
| **Grimsel** | Grimsel Test Site is a hard-rock underground lab, not glacial seismology — see `ccs-geothermal-mining.md`. No glacier seismic dataset found under that name. |
| **PANGAEA HTML search** | `https://www.pangaea.de/?q=…` renders results client-side and returns nothing to a fetch. Use `https://ws.pangaea.de/es/pangaea/panmd/_search?q=…`. |
| **IRIS `service.iris.edu` fdsnws** | Returned "Duplicate Content-Length" parse errors throughout this pass. **`service.earthscope.org` works** — use it instead. |
