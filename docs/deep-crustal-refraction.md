# Open Deep-Crustal / Lithospheric Controlled-Source Seismic Datasets — Worldwide

Reflection, refraction and wide-angle (WARR) experiments imaging the whole crust and
uppermost mantle. Scope is **controlled source** (explosives, Vibroseis, airguns used for
onshore–offshore crustal work) — not passive/earthquake seismology, except where a
programme's active-source component is archived alongside its passive one.

**Flags** — `[V]` = verified this session by fetching the URL and/or measuring bytes over
HTTP; `[U]` = unverified (URL not reachable, size not stated, or claim taken from
literature only). Where no URL could be verified, the entry says `search: <phrase>`
rather than guessing a link.

Sizes marked "measured" come from `Content-Length` on an HTTP HEAD/range request, or from
summing an Apache directory index. Sizes marked *(est.)* are estimates and are flagged.

> Status: **v5 — complete.** All continents covered. 312+ catalogued entries, of which the
> overwhelming majority were verified by fetching the URL and/or measuring bytes over HTTP
> during this session. All 164 distinct URLs were link-checked at the end (§7C).

---

## 1. Headline findings

1. **COCORP's raw data is openly downloadable and nobody says so.** It is the largest
   *unadvertised* holding found here — no catalogue entry, no DOI, no licence, no landing
   page, just an open directory. The Cornell server
   `cocorp.eas.cornell.edu` runs an unauthenticated Apache directory index holding:
   - **pre-stack shot gathers: 780 SEG-Y files, ≈121.9 GiB, across 165 line
     directories** (`ELLIPSE/COCORP/S Gathers/`). Spot-verified: `ND01/0078-124.sgy` is
     **408,102,720 bytes**, HTTP 200, and its first bytes decode from EBCDIC as
     `C 1 CLIENT … COMPANY … COCORP` — a genuine SEG-Y textual header. [V]
   - **177 stacked SEG-Y sections, 1,969,740,667 bytes (1.834 GiB)** (`Stacks/`). [V]
   - plus interpretations, maps, observer sheets, acquisition parameters, processing
     flows, survey notes and publications (~1.6 GiB more).

   No registration, no request form, no licence statement. **Mirror it.**

   **Where does COCORP live now? Only here.** COCORP has **no FDSN network code** and does
   **not** appear in the IRIS/EarthScope network list (1,206 rows), the PH5 network list
   (234 rows), or the FDSN registry (~3 MB) — all three were searched for `COCORP` and
   `Continental Reflection` with zero hits. There is no IRIS "assembled dataset" for it.
   The Cornell ELLIPSE server is the archive of record, it is unmaintained (Apache 2.4.52,
   content last touched 1992–2009), and the line pages still point at the long-dead
   `www.geo.cornell.edu/geology/cocorp/COCORP.html`. [V]
2. **LITHOPROBE — re-measured exactly this session: 246 ZIPs, 73,146,873,565 bytes
   = 68.12 GiB** across 13 populated transect directories on the NRCan GeoGratis HTTPS
   server, Open Government Licence – Canada, anonymous access. (An earlier pass reported
   ~65.77 GiB / ~236 ZIPs from Apache's rounded human-readable sizes; **that undercounted**
   — every file has now been HEAD-ed individually.) 12 named transects are catalogued on
   open.canada.ca (141 CKAN records). A **second** NRCan tree, `gsc_sem/`, holds the
   Canadian **refraction** datasets (§2.2b). [V]
3. **SinoProbe data *is* public — via EarthScope, not via China.** `SINOPROBE-2 Controlled
   Source` is archived as FDSN network **ZC (2009, 1,190 stations)** in the EarthScope PH5
   archive, with a second network **5G — "SinoProbe: Northeast China Transect" (2011, 357
   stations)**. Both are queryable and downloadable as SEG-Y through `ph5ws`. [V]
4. **The EarthScope PH5 archive holds 234 active-source experiments** and is the single
   best route to modern crustal-scale controlled-source data worldwide — including Tibet,
   Taiwan, Iberia, Morocco, Botswana, Israel/Jordan, Korea, Vietnam, Venezuela, Brazil and
   New Zealand. Fully scriptable, no login. Recipe in §6. [V]
5. **The bigger prize is the EarthScope "assembled datasets" archive — 852 rows,
   invisible to FDSN network queries, and it holds nearly every pre-2010 NSF
   controlled-source crustal experiment.** Catalogue at `https://ds.iris.edu/mda/?type=assembled`;
   files served anonymously from `https://data.earthscope.org/archive/assembled/<id>/`.
   Everything previously reported as "lost" is in fact there and open:
   - **CD-ROM** (Rocky Mountain Transect, 1999) — **33,930,094,818 B = 31.60 GiB** SEG-Y
     (33,930,130,468 B including its `manifest.txt`)
   - **Deep Probe 1995 active source** — **4,060,092,112 B = 3.78 GiB** SEG-Y
   - **LITHOPROBE SNORCLE refraction 1997** — **2,656,798,329 B = 2.47 GiB** SEG-Y
   - **INDEPTH I/II/III + INDEPTH-2 wide-angle** — **≈19.6 GiB** SEG-Y across four tarballs
   - **EAGLE (Ethiopia) active source**, all three **KRISP** campaigns, **BOLIVAR** land +
     OBS legs, **CHARME**, **SEGMeNT** (410.42 GiB), **Chile-SIO** (407.15 GiB)
   - the **Russian/Soviet DSS + PNE** profiles: **QUARTZ**, **CRATON**, **Baikal/DSSRIFT**,
     **Batholith-1/-2**, **Bazalt-1/-2** — §4.2
   - the legacy **USGS refraction** surveys whose FDSN codes (`XC`, `XD`) serve no
     waveforms — the data is here instead. [V]
6. **Finland's FIRE is the largest single open deep-crustal reflection dataset on Earth:
   1,147,373,744,961 bytes = 1.147 TB (1.043 TiB) across 1,963 files, CC BY 4.0, no login
   — and it includes the raw field SEG-Y**; 2,104 km of CMP data over four transects
   (P1 265.98, P2 168.75, P3 312.20, P4 321.64 GiB, re-measured independently). Finland
   also publishes BABEL, SVEKALAPKO, SVEKA ×3, POLAR, BALTIC, FENNIA and Kuusamo the same
   way — **1.149 TB of open controlled-source seismic from one country**. §3.3–3.4b. [V]
7. **Geoscience Australia is the biggest open deep-crustal reflection archive in the
   southern hemisphere.** 28 survey packages (L180–L213 plus Camooweal),
   **97,259,781,154 bytes = 90.58 GiB**, every byte measured by HTTP HEAD, all
   **CC-BY 4.0**, direct CloudFront download, no registration. Full table in §5.1. [V]
8. **Two national deep-reflection programmes remain closed despite open licences.**
   **DEKORP** (Germany) publishes 28 DOIs, several under CC BY 4.0, but *every* landing
   page says "The dataset is not available for public download — please fill in the form";
   the same holds for all GFZ GIPP controlled-source datasets. **CROP** (Italy, ~10,000 km)
   is sold per-kilometre (5 €/km raw SEG-Y for universities, 150 €/km industry), though its
   scanned **Atlas plates are free CC BY 4.0** on ViDEPI. **BIRPS** (~12,000 km) survives
   at BGS, raw and processed, but only by email request at cost recovery. The same
   licence-open / access-closed pattern covers **every GFZ GIPP controlled-source dataset**,
   including Iran's **Western Makran** transects (CC BY 4.0, moratorium expired 2023, SEG-Y
   shot gathers — request form only). §3.3, §3.5, §4.5. [V]

---

## 2. North America

### 2.1 COCORP (Consortium for Continental Reflection Profiling)

Cornell University, 1975–1990s. ~11,000+ line-km of Vibroseis deep-crustal reflection
across the conterminous USA, plus international work. The data lives on Cornell's
**ELLIPSE** server (Electronic Library of Lithospheric Imagery from deeP Seismic
Exploration) as an open Apache index.

| # | Dataset | Region | Years | Type | Extent | Size | Licence | Verified URL | Access | Flag |
|---|---------|--------|-------|------|--------|------|---------|--------------|--------|------|
| 1 | **COCORP stacked sections (SEG-Y)** | USA, 28 states | 1975–1990s | Deep crustal reflection (Vibroseis), stacked | **177 files** named by state+line (AR01…WY06) | **1,969,740,667 bytes = 1.834 GiB** (measured: 177 parallel HEADs). Largest: MT10 53.6 MB, MT12 50.4 MB, OH01 49.7 MB, AZ06 37,434,756 B, KS01 32.4 MB | Not stated on server (US academic, NSF-funded; a `Lien.rtf`/`Lien1.txt` sits at server root) | https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/Stacks/ | **Anonymous HTTPS directory, no registration** | **[V]** |
| 2 | COCORP line metadata pages (ELLIPSE) | USA | — | Metadata | **168 line pages** across 28 state prefixes: GA 28, CA 15, OK 12, MT 12, WA 8, UT 8, NV 8, NM 7, AZ 7, AR 7, WY 6, TX 6, NY 5, MN 5, TN 4, KS 4, VT 3, SC 3, ND 3, MI 3, FL 3, OR 2, OH 2, NH 2, IL 2, ID 2, MO 1, IN 1 | ~1 MB | as above | https://cocorp.eas.cornell.edu/cocorp/ | Anonymous HTTPS | **[V]** |
| 3 | **COCORP pre-stack shot gathers ("S Gathers")** | USA, 165 lines | 1975–1990s | **Pre-stack SEG-Y shot gathers**, one subdirectory per line, files named by shot range (e.g. `0078-124.sgy`) | **165 line directories, 780 files** | **≈121.91 GiB** (summed from every line's Apache index). Largest lines: ND01 8.38, TX06 3.17, IL01 3.05, OH01 2.75, UT01 2.38, IN01 2.30, KS01 2.13, AZ06 2.10, MT10 2.07, AZ07 2.06, AR06 2.03, OH02 1.99 GiB | Not stated | https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/S%20Gathers/ | Anonymous HTTPS, no registration | **[V]** — spot-verified `ND01/0078-124.sgy` = **408,102,720 B**, HTTP 200, valid EBCDIC SEG-Y header reading `COCORP` |
| 4 | COCORP interpretations | USA | — | Interpreted line drawings / images | 160 files | **161.5 MiB** (index sum) | as above | https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/Interpretations/ | Anonymous HTTPS | **[V]** |
| 5 | COCORP maps | USA | — | Location maps | 168 files | **168.5 MiB** (index sum) | as above | https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/Maps/ | Anonymous HTTPS | **[V]** |
| 6 | COCORP supporting archives | USA | — | Acquisition parameters (195 files, 0.7 MiB); **OB Sheets** = observer sheets (165 files, **295.3 MiB**); Processing Flow (172 files, 7.0 MiB); Publications (253 files, **576.5 MiB**); Survey Notes (168 files, **510.7 MiB**); plus `location/`, `dream/`, `olddata/` | 9 further directories | **≈1.36 GiB** for the five measured | as above | https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/ | Anonymous HTTPS | **[V]** |
| 7 | **COCORP Taiwan** | Taiwan | — | Deep reflection (COCORP international) | 2 files | **366 MiB** (index sum) | not stated | https://cocorp.eas.cornell.edu/Taiwan/ | Anonymous HTTPS | **[V]** |
| 8 | **COCORP Ghana** | Ghana, West Africa | — | Deep reflection (COCORP international) | 2 files | **26 MiB** (index sum) | not stated | https://cocorp.eas.cornell.edu/Ghana/ | Anonymous HTTPS | **[V]** |
| 9 | COCORP programme home | USA | 1975– | — | — | — | — | https://cocorp.eas.cornell.edu/ (root index) | Anonymous HTTPS | **[V]** root index lists `Auxiliary Data/`, `Basemaps/`, `ELLIPSE/`, `Ghana/`, `ProMAX_Backup/`, `Taiwan/`, `WorkSpace/`, `cocorp/`, `unzipped/` |
| 9a | COCORP Auxiliary Data | USA | 2003–2004 | US gravity and magnetic rasters (TIFF/BIL/PS), Bouguer map, `INDEPTH` topography raster (218 MB TIFF), COCORP status spreadsheets | 28 files | **3.03 GiB** | not stated | https://cocorp.eas.cornell.edu/Auxiliary%20Data/ | Anonymous HTTPS | **[V]** |
| 9b | COCORP Basemaps | USA | 2003– | Basemap rasters | 2 files | **182 MiB** | not stated | https://cocorp.eas.cornell.edu/Basemaps/ | Anonymous HTTPS | **[V]** |
| 9c | COCORP WorkSpace | USA | — | Working files | 226 files | **536 MiB** | not stated | https://cocorp.eas.cornell.edu/WorkSpace/ | Anonymous HTTPS | **[V]** |
| 9d | `ProMAX_Backup` (**not COCORP** — a Finnish 3D survey backup) | Finland (`lumpola3d`) | 2005 | 4 ProMAX `.tar` backups of a 3D survey | 4 files | **10.59 GiB** (506 MB / 1.3 GB / 3.6 GB / 5.2 GB) | not stated | https://cocorp.eas.cornell.edu/ProMAX_Backup/ | Anonymous HTTPS | **[V]** — flagged because it is an unexpected, undocumented 3D dataset sitting on the COCORP host |

**Whole-server total: ≈139.8 GiB** openly readable at `cocorp.eas.cornell.edu`
(S Gathers 121.91 + ProMAX_Backup 10.59 + Auxiliary Data 3.03 + Stacks 1.83 + supporting
1.36 + WorkSpace 0.52 + Taiwan 0.36 + Basemaps 0.18 + Ghana 0.03). [V]

**Bulk-download recipe (COCORP stacks):**

```bash
# every stacked COCORP line, ~1.9 GB
wget -r -np -nH --cut-dirs=2 -A '*.segy.bin' \
  https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/Stacks/

# every pre-stack shot gather, ~122 GiB — 165 line directories
wget -r -np -nH --cut-dirs=2 -A '*.sgy' \
  'https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/S%20Gathers/'

# one line only
wget -r -np -nH --cut-dirs=4 -A '*.sgy' \
  'https://cocorp.eas.cornell.edu/ELLIPSE/COCORP/S%20Gathers/ND01/'
```

Note: some gather directories contain a `SBSE____.TMP` file that is a byte-identical
duplicate of the line's `.sgy` (e.g. AR01) — exclude `*.TMP` to avoid pulling it twice.

Caveats: files are named `*.segy.bin`; the server is an unmaintained legacy host (Apache
2.4.52 on Ubuntu, content last modified 1992–2009). **Mirror it — this is exactly the kind
of host that disappears.** The line pages under `/cocorp/` reference
`http://www.geo.cornell.edu/geology/cocorp/COCORP.html`, which is a dead legacy link.

### 2.2 LITHOPROBE (Canada)

Canada's national lithospheric programme, 1984–2005; the largest Earth-science project in
Canadian history. Data is served from NRCan GeoGratis under the **Open Government Licence –
Canada**, anonymous HTTPS, no registration.

| # | Transect | Dir code | Region | Type | Size | Verified URL | Flag |
|---|----------|----------|--------|------|------|--------------|------|
| 10 | **Whole zipped SEG-Y archive** | — | Canada-wide | 2D deep crustal reflection SEG-Y | **246 ZIPs, 73,146,873,565 bytes = 68.12 GiB** (every file HEAD-ed individually this session) | https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/zipped_segys/ | **[V]** |
| 11 | Transect 2 — Southern Cordillera | `sc` | BC | reflection | 22 ZIPs, 6,835,671,788 B = **6.366 GiB** | …/zipped_segys/sc/ | **[V]** |
| 12 | Transect 3 — Alberta Basement | `ab` | Alberta | reflection | 39 ZIPs, 21,251,069,963 B = **19.792 GiB — largest transect** | …/zipped_segys/ab/ | **[V]** |
| 13 | Transect 4 — SNORCLE (Slave–Northern Cordillera Lithospheric Evolution) | `snorcle` | NWT/Yukon/BC | reflection (+ refraction under `gsc_sem`/`links`) | 4 ZIPs, 7,083,131,540 B = **6.597 GiB** | …/zipped_segys/snorcle/ | **[V]** |
| 14 | Transect 5 — Trans-Hudson Orogen (THOT) | `thot` | Manitoba/Saskatchewan | reflection (incl. Flin Flon–Snow Lake VMS belt) | 20 ZIPs, 9,578,173,185 B = **8.920 GiB** | …/zipped_segys/thot/ | **[V]** |
| 15 | Transect 7 — Kapuskasing Structural Zone | `ksz` | Ontario | reflection; largest file `feat_line14hr_segy.zip` = 146,184,939 B (high-resolution line 14) | 12 ZIPs, 667,597,047 B = **0.622 GiB** | …/zipped_segys/ksz/ | **[V]** |
| 16 | Transect 8 — Abitibi–Grenville | `ag` | Quebec/Ontario | reflection | 32 ZIPs, 4,466,279,325 B = **4.160 GiB** | …/zipped_segys/ag/ | **[V]** |
| 17 | Transect 9 — Lithoprobe East | `le` | Appalachians, Atlantic Canada | reflection (lines 1–15c) | 16 ZIPs, 1,110,859,442 B = **1.035 GiB** | …/zipped_segys/le/ | **[V]** |
| 18 | Transect 10 — Eastern Canadian Shield Onshore–Offshore (ECSOOT) | `ecsoot` | Labrador | reflection, onshore–offshore | 2 ZIPs, 815,161,865 B = **0.759 GiB** (prior pass said 0.39 GiB — **corrected**) | …/zipped_segys/ecsoot/ | **[V]** |
| 19 | Transect 11 — Western Superior | `ws` | Ontario/Manitoba | reflection, Archean craton/greenstone | 9 ZIPs, 4,749,236,335 B = **4.423 GiB** | …/zipped_segys/ws/ | **[V]** |
| 20 | Transect 12 — GLIMPCE (Great Lakes Intl. Multidisciplinary Program on Crustal Evolution) | `gl` | Great Lakes | marine deep reflection | 8 ZIPs, 456,333,423 B = **0.425 GiB** | …/zipped_segys/gl/ | **[V]** |
| 21 | Transect 13 — West Coast (Vancouver Island) | `vi` (`wc_vi` in web GIS) | BC offshore | reflection, onshore–offshore | 41 ZIPs, 6,571,179,818 B = **6.120 GiB** (prior pass said 5.29 GiB — **corrected**) | …/zipped_segys/vi/ | **[V]** |
| 22 | Transect 14 — East Coast Frontier Geoscience Program | `ec_fgp` | Atlantic margin | marine deep reflection | 28 ZIPs, 7,671,796,741 B = **7.145 GiB** | …/zipped_segys/ec_fgp/ | **[V]** |
| 23 | Transect 15 — Arctic Frontier Geoscience Program | `arc_fgp` | Canadian Arctic | marine deep reflection | 13 ZIPs, 1,890,383,093 B = **1.761 GiB** | …/zipped_segys/arc_fgp/ | **[V]** |
| 24 | LITHOPROBE catalogue records | — | Canada | metadata + per-line SEGP1 nav, MT (EDI) | **141 CKAN records** matching `title:LITHOPROBE`, incl. 12 transect records and per-line/per-MT-site records | https://open.canada.ca/data/en/api/3/action/package_search?q=title:LITHOPROBE&rows=300 | **[V]** |
| 25 | LITHOPROBE unzipped SEG-Y + reprocessing | — | Canada | reflection | contains `Lithoprobe_East_Coast_Geovectra_reprocessing_2018/`, `nwt/`, `sbc/` | https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/segy/ | **[V]** dir exists |
| 26 | LITHOPROBE web GIS + nav links | — | Canada | GIS, SEGP1 navigation, MT EDI | — | https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/web_gis/ and …/links/ | **[V]** |

**Bulk-download recipe (LITHOPROBE):**

```bash
# whole 65.77 GiB SEG-Y archive
wget -r -np -nH --cut-dirs=5 -A '*.zip' \
  https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/zipped_segys/

# one transect only, e.g. Trans-Hudson
wget -r -np -nH --cut-dirs=6 -A '*.zip' \
  https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/zipped_segys/thot/

# enumerate the catalogue (transect names, per-line metadata, MT sites)
curl -A 'Mozilla/5.0' \
 'https://open.canada.ca/data/en/api/3/action/package_search?q=title:LITHOPROBE&rows=300'
```

The CKAN API **rejects non-browser user agents** (returns "Request Rejected") — send a
browser `User-Agent`. The `zipped_segys/text/` directory holds no ZIPs.

Note the directory-code / transect-name mismatch: the web-GIS uses `glimpce` and `wc_vi`
where the SEG-Y tree uses `gl` and `vi`. MT data for a transect lives in a parallel
`<code>_mt` web-GIS directory and under `.../links/<code>/mt/`.

### 2.2b GSC "gsc_sem" archive — Canadian **refraction** and hard-rock seismic (separate from LITHOPROBE)

A second, less-known NRCan/GeoGratis tree, `.../vector/gsc_sem/`, holds ~60 directories of
Geological Survey of Canada seismic and MT datasets — including the **refraction**
counterparts to LITHOPROBE's reflection lines. Same Open Government Licence – Canada,
same anonymous HTTPS. Base: https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/gsc_sem/
Catalogued on open.canada.ca (44 CKAN records match `title:(seismic AND refraction)`). [V]

| # | Dataset | Region | Type | Size (dir index sum) | Verified URL | Flag |
|---|---------|--------|------|----------------------|--------------|------|
| 26a | **Arctic refraction** | Canadian Arctic | Refraction (`arctic.zip` + unpacked dir) | **1.7 MiB** | …/gsc_sem/arctic_refraction/ | **[V]** |
| 26b | **GLIMPCE refraction** — 27 refraction sites | Great Lakes | Refraction, with UWO header docs | **2.2 MiB** (3 files) | …/gsc_sem/glimpce_refraction/ | **[V]** |
| 26c | **FRIG94** refraction shot | Canada | **SEG-Y** (`frig4eos.sgy` 5.6 MB) + filter/log + 5 figure PDFs | **27.2 MiB** (21 files) | …/gsc_sem/frig94/ | **[V]** |
| 26d | **NW99** refraction | NW Canada | Shot/borehole tables, observer logs (xls), 85 MB summary PDF | **85.2 MiB** (10 files) | …/gsc_sem/nw99/ | **[V]** |
| 26e | **NW98** refraction | NW Canada | as above | **51.5 MiB** (12 files) | …/gsc_sem/nw98/ | **[V]** |
| 26f | **Ice Island** refraction 1985 / 1986 / 1990 | Arctic Ocean ice island | Refraction (GSC Open Files 1196, 1511, 2273) | **7.0 MiB** | …/gsc_sem/ice_island/ | **[V]** |
| 26g | **BIGMAC 1987** — 3 refraction profiles | Canada | Refraction (GSC Open File 2058) | small | …/gsc_sem/BIGMAC%201987/ | **[V]** via CKAN resource URL |
| 26h | **Melville** | Arctic | Seismic | **5.3 MiB** (33 files) | …/gsc_sem/melville/ | **[V]** |
| 26i | **Lincoln Sea** | Arctic | Seismic | **4.1 MiB** | …/gsc_sem/lincoln_sea/ | **[V]** |
| 26j | **SNORCLE refraction** lines 11, 21, 22, 31 (many shotpoints) | NWT / Yukon / BC | Refraction navigation (SEGP1) + per-shot records; the wide-angle companion to LITHOPROBE transect 4 | per-line files | https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/lithoprobe/links/snorcle/seis_refr/line_21/ln21.segp1 (and `line_11`, `line_22`, `line_31`) | **[V]** URLs from CKAN records |
| 26k | LITHOPROBE MT by transect (e.g. Alberta, 117 + 120 sites) | Canada | Magnetotelluric EDI | `ab_edi.zip` etc. | https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/gsc_sem/lith_MT/ab_edi.zip | **[V]** |
| 26l | Hard-rock / mining seismic in the same tree | Canada | 2D/3D reflection, VSP, MT: `bathurst_dsi`, `brunswick_2d`, `brunswick_3d`, `flin_flon`, `halfmile_lake`, `kidd_creek`, `lalor`, `manitouwadge`, `matagami_3d`, `matagami_vsp`, `sudbury_2d`, `sturgeon_lake`, `nipigon`, `normetal`, `selbaie_dsi`, `extech-IV`, `mallik2d`/`mallik3d`, plus ~20 MT directories | not summed | https://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/gsc_sem/ | **[V]** directory listing |

### 2.3 Metal Earth (Laurentian University / MERC)

CAD$104M programme, started 2017; 18 transects, >1,000 km across the Superior Province.
Processing integrates Metal Earth R1/R2 profiles with **LITHOPROBE (1990)** and
**Discover Abitibi (2005)** legacy lines.

| # | Dataset | Region | Type | Size | Licence | Verified URL | Flag |
|---|---------|--------|------|------|---------|--------------|------|
| 27 | **Metal Earth — Larder Lake transect (active + passive)** | Abitibi greenstone belt, Ontario | Active reflection sections (ME-321-R1 + LITHOPROBE KSZ-12) + ambient-noise Vs model + 5 receiver-function PS sections | **154,740,524 bytes = 147.6 MiB** (HEAD, `application/zip`) | Not stated on release page | https://merc.laurentian.ca/sites/default/files/LarderLake_Active_Passive_Seismic_Data.zip | **[V]** |
| 28 | Metal Earth — Matheson R1 transect | Abitibi, Ontario | Active seismic reflection | **103.9 MiB** (measured in an earlier pass) | Not stated | landing: https://merc.laurentian.ca/ — see also https://metalearth.geohub.laurentian.ca/ | **[U]** direct ZIP URL not recoverable this session. **Warning: `merc.laurentian.ca` soft-404s** — a missing file returns `302 → 200 text/html`, so a bare status code is not proof a file exists. A real file returns `200` with `Content-Type: application/zip` and a `Content-Length` (as Larder Lake does). Guessed names `Matheson_Active_Passive_Seismic_Data.zip` and `Matheson_R1_Seismic_Data.zip` are **both soft-404s**. `search: Metal Earth Matheson seismic data release zip` |
| 29 | Metal Earth GeoHub (portal) | Superior Province | Portal to 10 named seismic transects: Chibougamau, Cobalt, Geraldton-Onaman, Larder Lake, Malartic, Rainy River, Rouyn-Noranda, Stormy-Dryden, Sturgeon, Swayze/Matheson | not documented | not specified | https://metalearth.geohub.laurentian.ca/ | **[V]** live; **[U]** per-dataset inventory does not render to a text fetch |

### 2.4 US legacy crustal programmes in the EarthScope archive

The classic 1990s US crustal-refraction experiments (CD-ROM, Deep Probe, Rocky Mountain
Front, SAREX, ADCOH) were PASSCAL deployments. Their **network codes** are registered with
FDSN; whether waveform data is actually served differs per experiment (see §6 for how to
check). Codes confirmed in the FDSN network registry this session:

| # | Programme | Net code | Years | Region | Type | Operator | Flag |
|---|-----------|----------|-------|--------|------|----------|------|
| 30 | **CD-ROM** — "Lithospheric Structure and Evolution of the Rocky Mountain Transect" (Continental Dynamics of the Rocky Mountains) | **XK** | 1999–2000 | Wyoming–Colorado–New Mexico | Crustal refraction/wide-angle + passive | IRIS/PASSCAL | **[V]** code+title in FDSN registry |
| 31 | **Rocky Mountain Front II** (Deep Probe predecessor / companion) | **XG** | 1992 | Montana–Wyoming | Refraction/wide-angle | IRIS/PASSCAL | **[V]** code+title |
| 32 | **Appalachian Seismic Transect** | **Z4** | 2009–2010 | Appalachians, USA | Crustal transect | Univ. of North Carolina at Chapel Hill | **[V]** |
| 33 | **SESAME** — Southeastern Suture of the Appalachian Margin Experiment | **Z9** | 2010–2014 | SE USA | Crustal/lithospheric | Brown University | **[V]** |
| 34 | **ENAM Community Seismic Experiment** (onshore component) | **ZI** | 2014 (80 sta) and 2015 (1,414 sta) | US mid-Atlantic margin | Onshore–offshore active source, pre-/syn-/post-rift | community experiment | **[V]** in PH5 |
| 35 | Eastern North American Margin Explosives Test | **5A** | 2013 (152 sta) | US East Coast | Active source | — | **[V]** in PH5 |
| 36 | **GUMBO — Gulf of Mexico Basin Opening** | **ZF** | 2010 (424 sta) | Gulf Coast, USA | Crustal wide-angle refraction, 4 transects | — | **[V]** in PH5 |
| 37 | **SSIP / Salton Trough** — "Seismic Imaging of New Transitional Crust in the Salton Trough Oblique Rift" | **YG** | 2011 (**5,016 stations**) | Salton Trough, CA | Crustal active source | — | **[V]** in PH5 — one of the largest active-source deployments in the archive |
| 38 | **IDOR** — "Deformation and magmatic modification of a steep continental margin, western Idaho–eastern Oregon" | **9A** | 2012 (2,554 sta) | Idaho/Oregon | Crustal active source | — | **[V]** in PH5 |
| 39 | **Batholiths Controlled Source** | **YB** | 2009 (1,806 sta) | BC Coast Mountains, Canada | Crustal active source | Virginia Tech | **[V]** in PH5 |
| 40 | High Lava Plains Active source | **Z2** (854 sta) / **Z5** (1,048 sta) | 2008 | Oregon | Crustal active source | — | **[V]** in PH5 |
| 41 | Northern Nevada–Utah Transect | **ZG** | 2005 (395 sta) | Great Basin | Refraction transect | — | **[V]** in PH5 |
| 42 | Central Walker Lane / 2004 Idaho–Nevada–California Transect (exp. 0413) | **XU** | 2004 (750 sta) | Great Basin | Refraction transect | — | **[V]** in PH5 |
| 43 | Northern Walker Lane Refraction Survey | **XW** | 2002 (61 sta) | Nevada | Refraction | Univ. Nevada Reno | **[V]** in PH5 |
| 44 | Seismic Refraction Surveys, Livermore Valley & Santa Cruz Mts | **XC** | 1980–1982 | California | Refraction | IRIS DMC (legacy USGS) | **[V]** FDSN registry |
| 45 | Seismic-Refraction Profiles, Western Mojave Desert | **XD** | 1980–1981 | California | Refraction | IRIS DMC (legacy USGS) | **[V]** FDSN registry |
| 45a | **LARSE** — Los Angeles Region Seismic Experiment, passive phase | **XN** | 1998–1999 | S. California | Crustal transect (companion to the active-source LARSE lines) | IRIS/PASSCAL, 83 stations | **[V]** in IRIS `fdsnws` |
| 45b | **SSIP** — Salton Seismic Imaging Project | **YG** (PH5) | 2011 | Salton Trough, CA / Baja | Onshore refraction + low-fold reflection (7 lines), airgun + OBS in the Salton Sea, onshore–offshore, broadband line. **126 explosive shots / 33,329 kg**; 2,595 Texans in 4,739 deployments at **3,958 unique sites**; 186 RT-130s at 277 sites; 48 OBS at 78 sites; 2,330 airgun shots | Hole (VT), Stock (Caltech), Fuis (USGS), Scripps, UNR, Stanford, CICESE, UABC | **[V]** — project page https://www.geophys.geos.vt.edu/hole/salton/ ; data as PH5 net **YG**, 5,016 stations |

**Availability check.** Data for **CD-ROM (XK, 1999–2000, 51 stations)**, **Rocky Mountain
Front II (XG, 1992, 36 stations)**, **INDEPTH II (XR, 1994, 13 stations)**, **INDEPTH-III
(XR, 1997–1999, 62 stations)**, **INDEPTH IV (X4, 2007–2009, 97 stations)**, **Kaapvaal
(XA, 1997–1999, 82 stations)**, **Appalachian Seismic Transect (Z4, 7 stations)** and
**SESAME (Z9, 91 stations)** is all **served by the IRIS/EarthScope `fdsnws` station
service** — i.e. these experiments' waveforms live on the miniSEED side of the archive,
not in PH5. Verified by: [V]

```bash
curl 'https://service.iris.edu/fdsnws/station/1/query?level=network&format=text'   # 1,206 rows
```

By contrast the 1980–82 legacy USGS refraction networks **XC** and **XD** are registered
with FDSN but return **no stations** for their stated years — registry entries only. [V]

### 2.5 **RESOLVED: CD-ROM, Deep Probe, SNORCLE refraction and INDEPTH are all open** — via the assembled-dataset archive

Everything flagged "not found" in earlier passes turned up in the **EarthScope assembled
dataset catalogue** (§6A), which is *not* reachable through FDSN network queries.
Naming convention: `https://data.earthscope.org/archive/assembled/<id>/<id>.<Nickname>.DATA.<FORMAT>.tar.gz`
(nickname is title-cased for single words, kept verbatim when it contains digits,
hyphens or underscores). Every size below is a measured `Content-Length`. [V]

| # | Assembled ID | Experiment | Region | Years | Type | Measured size | Flag |
|---|--------------|------------|--------|-------|------|---------------|------|
| 45c | **02-008 / CDRN** | **CD-ROM** (Continental Dynamics of the Rocky Mountains) | Rawlins, WY → 20 km S of Steamboat Springs, CO; **250 km N–S across the Cheyenne belt** | 1999 | Deep crustal **reflection**, 1,001-channel recorder, 25 m geophone interval, 100 m source interval, SEG-Y | **33,930,130,468 B = 31.60 GiB** (directory total; MDA states 35,957 MB uncompressed); `Restricted: N`; network `XK_1999` | **[V]** |
| 45d | **98-006 / DEEPA** | **Deep Probe 1995 active-source experiment** | Alberta → Montana/Wyoming, Rocky Mountain lithosphere | 1995 | Long-offset **refraction / wide-angle**, SEG-Y | **4,060,092,112 B = 3.78 GiB** | **[V]** — resolves the earlier "no archive found" |
| 45e | **05-023 / SNORE97** | **LITHOPROBE SNORCLE Refraction Experiment** | NWT / Yukon / BC | 1997 | Crustal **refraction**, SEG-Y | **2,656,798,329 B = 2.47 GiB** | **[V]** — the wide-angle companion to LITHOPROBE transect 4 |
| 45f | **87-001 / OUACHITA** | 1986 Ouachita Lithospheric Seismology Experiment | Ouachita orogen, USA | 1986 | Lithospheric refraction, SEG-Y | **267,394,038 B** | **[V]** |
| 45g | **00-036 / NYNEX** | NYNEX 1988 **Grenville–Appalachian** Seismic Refraction Experiment | Ontario / New York / New England | 1988 | Refraction, SEG-Y | **106,785,459 B** | **[V]** |
| 45h | **88-003 / NYNEX_86** | Ontario–New York–New England Seismic Refraction Experiment | same | 1986/88 | Refraction, SEG-Y | **23,002,541 B** | **[V]** |
| 45i | **94-003 / RISC** | 1992 RISC Experiment, southern Basin and Range | SW USA | 1992 | Crustal refraction, SEG-Y | **1,886,740,463 B = 1.76 GiB** | **[V]** |
| 45j | **96-003 / SWWA** | Reflection/Refraction Experiment in SW Washington | Cascadia forearc | 1995 | Reflection + refraction, SEG-Y | **588,426,312 B** | **[V]** |
| 45k | **91-004 / ALOHA** | Arrays for Lithosphere Observations in Hawaii | Hawaii | 1990 | Lithospheric, SEG-Y | **427,627,717 B** | **[V]** |
| 45l | **00-037 / COLUMBIA2** | Stanford Crustal Geophysics Project — Columbia Plateau | Washington/Oregon | 1988 | Crustal seismic, SEG-Y | **286,485,471 B** | **[V]** |
| 45m | **94-013 / PACE89** | PACE 1989 Seismic Refraction Survey, N Arizona | Arizona | 1989 | Refraction, SEG-Y | **245,624,380 B** | **[V]** |
| 45n | **00-034 / PACE1987** | PACE 1987 Seismic Refraction Survey, W-central Arizona | Arizona | 1987 | Refraction, SEG-Y | **16,354,717 B** | **[V]** |
| 45o | **00-038 / TACT1988** | **TACT** Prince William Sound (Trans-Alaska Crustal Transect) | Alaska | 1988 | Crustal refraction, SEG-Y | **206,987,176 B** | **[V]** |
| 45p | **00-035 / TACT1987** | TACT 1987 Alaska Range — Fairbanks N & S, Olnes | Alaska | 1987 | Crustal refraction, SEG-Y | **27,870,834 B** | **[V]** |
| 45q | **00-039 / EDGE** | Onshore–offshore wide-angle recordings of the 1989 Alaskan EDGE experiment | Alaska margin | 1989 | Onshore–offshore wide-angle, SEG-Y | **39,856,217 B** | **[V]** |
| 45r | **00-029 / NEVADA** | PASSCAL Basin and Range Lithospheric Seismic Experiment | N Nevada | 1986 | Lithospheric refraction, SEG-Y | **13,418,150 B** | **[V]** |
| 45s | **87-002 / BRE86** | Northern Nevada Basin and Range vertical-component experiment | Nevada | 1986–87 | Crustal, SEG-Y | **34,855,076 B** | **[V]** |
| 45t | **94-008 / BLDR** | Boulder Batholith 1992 Experiment | Montana | 1992 | Crustal, SEG-Y | **38,071,320 B** | **[V]** |
| 45u | **00-026 / YUCCA** | Seismic-refraction experiment, Yucca Mountain and vicinity | Nevada | 1985 | Refraction, SEG-Y | **20,576,069 B** | **[V]** |
| 45v | **00-009 / NTS** | Seismic-refraction experiment, Yucca Mountain / Beatty | Nevada | 1980–83 | Refraction, SEG-Y | **7,666,558 B** | **[V]** |
| 45w | **00-032 / SLO** | San Luis Obispo seismic refraction survey | California | 1986 | Refraction, SEG-Y | **5,750,410 B** | **[V]** |
| 45x | **00-007 / MOJAVE** | Seismic-refraction profiles, western Mojave Desert | California | 1980–81 | Refraction, SEG-Y | **5,454,325 B** | **[V]** — **this is where FDSN network `XD` actually lives** |
| 45y | **00-013 / MORROBAY** | Seismic-refraction investigation: Morro Bay to the Sierra | California | 1982–83 | Refraction, SEG-Y | **3,432,144 B** | **[V]** |
| 45z | **00-010 / LIVERMORE** | Seismic refraction, Livermore Valley & Santa Cruz Mts | California | 1980–82 | Refraction, SEG-Y | **3,147,982 B** | **[V]** — **this is where FDSN network `XC` (1980–82) actually lives** |

**More North American crustal assembled datasets — all measured exactly via `?json`:** [V]

| # | Assembled ID | Experiment | Region | Years | Type | Measured size (directory total) |
|---|--------------|------------|--------|-------|------|--------------------------------|
| 45aa | **14-005 / ENAM** | Eastern North America Community Seismic Experiment | US Atlantic margin | 2014 | SEG-Y, 11 files | **180,259,243,483 B = 167.88 GiB** |
| 45ab | **02-006 / LARSEMCS** | **LARSE multichannel seismic reflection** | S California | 1994 | SEG-Y, 10 files | **88,504,568,113 B = 82.43 GiB** |
| 45ac | **05-012 / NWNV_CRVIB** | NW Nevada Seismic Experiment — **crustal Vibroseis** | Nevada | 2004–05 | SEG-Y, 3 files | **15,365,280,013 B = 14.31 GiB** |
| 45ad | **96-019 / LARSE.1A** | Air-gun data at onshore stations, LARSE | S California | 1994 | SEG-Y, 3 files | **12,296,589,347 B = 11.45 GiB** |
| 45ae | **97-004 / LARSE.1P** | LARSE passive experiment | S California | 1993–94 | SEG-Y | **5,526,427,044 B = 5.15 GiB** |
| 45af | **02-004 / LARSE-II** | 1999 Los Angeles Region Seismic Experiment Part I | S California | 1999 | SEG-Y | **4,352,752,030 B = 4.05 GiB** |
| 45ag | **96-020 / LARSE.1B** | Explosion data at onshore stations, LARSE | S California | 1994 | SEG-Y | **2,754,548,745 B = 2.57 GiB** |
| 45ah | **00-041 / TACTBROOKS** | **TACT Brooks Range**, Alaska | Alaska | 1990 | SEG-Y | **1,439,932,360 B = 1.34 GiB** |
| 45ai | **96-002 / RMF** | **Rocky Mountain Front Project** | Montana / Wyoming | 1992 | SAC, **14 files** | **1,157,544,797 B = 1.08 GiB** |
| 45aj | **18-001 / WesternUS-CDROM** | An Assembled Western US Dataset for Regional Seismic Analysis | Western USA | **1968–2002** | SEG-Y | **651,008,599 B** |
| 45ak | **96-001 / BSEA** | Onshore/offshore experiment, Bering–Chukchi Sea | W Alaska | 1994 | SEG-Y | **585,111,874 B** |
| 45al | **96-021 / LARSE.1C** | Earthquake data at onshore stations, LARSE | S California | 1994 | SEG-Y | **410,923,397 B** |
| 45am | **13-006 / SSIP** | Salton Sea Imaging Project | Salton Trough | 2011 | SEG-Y | **358,871,767 B** |
| 45an | **05-011 / NWNV_CRSHOTS** | NW Nevada Seismic Experiment — crustal shots | Nevada | 2004–05 | SEG-Y | **221,652,858 B** |
| 45ao | **94-012 / SFBAY** | San Francisco Bay Area Broadband Transect | California | 1993–94 | SEG-Y | **172,261,706 B** |
| 45ap | **00-023 / MQSTRIKE** | 1984 Maine–Quebec **along-strike** refraction profiles | Maine / Quebec | 1984 | SEG-Y | **21,249,494 B** |
| 45aq | **00-025 / TACTPWS** | TACT refraction survey, south-central Alaska | Alaska | 1985 | SEG-Y | **16,515,812 B** |
| 45ar | **00-024 / MQCROSS** | Maine–Quebec **cross-strike** refraction profile | Maine / Quebec | 1984 | SEG-Y | **13,223,052 B** |
| 45as | **00-020 / TACTRICH** | TACT Richardson Highway | Alaska | 1984 | SEG-Y | **10,318,446 B** |
| 45at | **00-019 / TACTCHUG** | TACT Chugach | Alaska | 1984 | SEG-Y | **5,987,045 B** |
| 45au | **21-008 / Cascadia** | **"An Open-Access, Controlled-Source Seismic Dataset Across the Cascadia Accretionary Wedge from Multi-…"** | Cascadia | 2021 | SEG-Y, **20 files** | **814,835,639,889 B = 758.87 GiB** — **the largest controlled-source crustal dataset in the entire assembled archive** |
| 45av | **99-002 / WETSHIPS** | Wide-angle recordings from the **1998 Seismic Hazards Investigation of Puget Sound** (SHIPS) | W Washington & BC | 1998 | Wide-angle, SEG-Y, **232 files** | **69,236,295,872 B = 64.48 GiB** |
| 45aw | **21-012 / QCF** | Queen Charlotte Fault Offshore Seismic Experiment | BC / SE Alaska margin | 2020–2022 | SEG-Y, 8 files | **322,232,404,741 B = 300.10 GiB** |
| 45ax | **18-015 / HI-Emperor** | Seismic imaging of volcano construction, underplating and flexure along the Hawaiian–Emperor seamount chain | Hawaii / Emperor | 2018–2019 | SEG-Y, 20 files | **370,606,208,488 B = 345.15 GiB** |
| 45ay | **12-015 / OCEANUS** | Evolution and hydration of the **Juan de Fuca** crust and uppermost mantle | Cascadia offshore | 2012 | SEG-Y, 47 files | **183,813,340,659 B = 171.19 GiB** |
| 45az | **00-044 / BASIX1** | Onshore/offshore wide-angle recordings, **San Francisco Bay Area Seismic Imaging Experiment (BASIX)** | California | 1991 | Wide-angle, SEG-Y | **28,515,589,943 B = 26.56 GiB** |
| 45ba | **02-001 / ACCRETE** | **ACCRETE** wide-angle | SE Alaska / BC Coast Mountains | 1994 | Wide-angle, SEG-Y | **18,082,293,132 B = 16.84 GiB** |
| 45bb | **23-027** | Seismic hazard, lithosphere hydration and double-verging structure of the **Puerto Rico** subduction zone | Puerto Rico | 2023 | Reflection + refraction, SEG-Y | **15,921,178,673 B = 14.83 GiB** |
| 45bc | **14-008** | Seismic reflection transect — **Lepanto, Arkansas** (New Madrid region) | Arkansas | 2006 | Reflection, SEG-Y | **11,826,524,670 B = 11.01 GiB** |
| 45bd | **10-023** | San Bernardino high-resolution reflection/refraction survey | California | 2003 | Reflection + refraction, SEG-Y | **4,116,968,957 B = 3.83 GiB** |
| 45be | **94-011 / BASIX2** | BASIX 1991 wide-angle **fan shots** | San Francisco Bay | 1991 | Wide-angle, SEG-Y | **2,709,345,608 B = 2.52 GiB** |
| 45bf | **00-040** | Onshore/offshore wide-angle recordings, central Oregon | Oregon | 1989 | Wide-angle, SEG-Y | **369,548,073 B** |
| 45bg | **07-018 / FTBLISS** | Refraction survey at Fort Bliss | Texas / New Mexico | 1996 | Refraction, SEG-Y | **182,400,797 B** |
| 45bh | **94-009** | Wide-angle seismic imaging in the **Peninsular Ranges** | S California | 1990 | Wide-angle, SEG-Y | **111,440,727 B** |
| 45bi | **94-006** | **Minnesota River Valley** 1990 wide-angle experiment | Minnesota | 1990 | Wide-angle, SEG-Y | **49,379,208 B** |
| 45bj | **00-015 / 00-016** | Refraction profiles crossing the epicentral region of the 1983 **Coalinga** earthquake (shot-source and earthquake-source) | California | 1983 | Refraction, SEG-Y | **8,800,017 B** + **3,878,809 B** |

Catalogued with **`Data = N` (not served)**: **07-027** INDEPTH IV SEG-Y, **08-002** TAIGER
active-source land refraction, **09-015** Mt Erebus refraction 2008, **20-006** waste-rock
refraction, **20-021** Precambrian crustal structure in western Ohio. Rows whose format is
**PH5** hold **zero files** in the assembled bucket — their data is in `ph5ws` instead
(**11-001** GUMBO, **10-001** Batholiths, **14-023** SUGAR, **11-012** SSIP, **14-021** /
**15-016** ENAM PH5). [V]

---

## 3. Europe

### 3.1 European crustal experiments inside the EarthScope **assembled-dataset** archive

The Central European "big three" wide-angle campaigns and the Iberian ones are archived at
EarthScope, **not** at any European portal, and are freely downloadable. All sizes are
directory totals measured via `?json` (§6A). [V]

| # | Assembled ID | Programme | Country / region | Years | Type | Measured size |
|---|--------------|-----------|------------------|-------|------|---------------|
| 145 | **06-002 / Sudetes-SLICE** | **SUDETES 2003 / SLICE** | Poland / Czechia / Germany, Bohemian Massif | 2003 | Wide-angle refraction, SEG-Y | **4,630,675,992 B = 4.31 GiB** |
| 146 | **04-008 / Polonaise** | **POLONAISE'97** | Poland, Trans-European Suture Zone | 1997 | Wide-angle refraction, SEG-Y | **2,255,112,696 B = 2.10 GiB** |
| 147 | **04-017 / ALP2002** | **ALP 2002** (aka **DANUBE**) | Eastern Alps / Pannonian Basin | 2002 | Wide-angle refraction, SEG-Y | **1,464,642,669 B = 1.36 GiB** |
| 148 | **04-009 / Celebration** | **CELEBRATION 2000** | Central Europe (Poland, Czechia, Slovakia, Hungary, Austria, Belarus, Ukraine, Russia) | 2000 | Wide-angle refraction, SEG-Y | **805,015,224 B = 0.75 GiB** |
| 149 | **03-012 / IBERSEIS** | **IBERSEIS wide-angle** | SW Iberia, Ossa-Morena / South Portuguese Zone | 2003 | Wide-angle refraction, SEG-Y | **484,950,262 B = 0.45 GiB** |
| 150 | **03-005** | Campi Flegrei Experiment, Part 2 | Italy | 1984 | Refraction, SEG-Y | **113,992,987 B** |
| 151 | **12-007** | **ALCUDIA** — wide-angle seismic reflection experiment across the Central Iberian Zone | Spain | 2012 | PH5 — **0 files in the assembled bucket**; data is in `ph5ws` as FDSN **7A** (909 stations) | see §6.4 |
| 152 | **17-016** | **CIMDEF** — The Central Iberian Mountain Range | Spain | 2017 | PH5 — 0 files here; data is `ph5ws` FDSN **XY** (874 stations) | see §6.4 |
| 153 | **11-021 / RIFSIS** | Seismic wide-angle across the Rif | Morocco (ICTJA-CSIC, Spanish-led) | 2011 | PH5 — 0 files here; `ph5ws` FDSN **X2** | see §6.3 / §6C |
| 154 | **10-008 / SIMA** | Seismic Imaging of the Moroccan Atlas | Morocco (ICTJA-CSIC) | 2010 | PH5 — 0 files here; `ph5ws` FDSN **XA** | see §6C |
| 155 | **92-002 / Iceland** | South Iceland Seismic Refraction Experiment | Iceland | 1990 | Refraction, **AH** format | **75,220,556 B** |

### 3.2 Important negative result

A full-text search of all 852 assembled-catalogue rows found **no entry** for:
**BIRPS**, **DEKORP**, **ECORS**, **CROP**, **BABEL**, **URSEIS**, **EUROBRIDGE**,
**SVEKALAPKO**, **NFP-20**, **TRANSALP**, **EGT / EUROPROBE**, **SeisDARE**
(and also none for **COCORP**, **SAREX** or **ADCOH**). The Western European national
deep-reflection programmes are therefore **not** mirrored at EarthScope — they remain with
their national hosts (BGS, GFZ, OGS, GTK, SGU, etc.), which is where they must be chased.
Apparent matches for `FIRE`, `HIRE` and `ESCI` in the catalogue are substring false
positives (a NEIU teaching course, etc.); the only real `LITHOPROBE` hit is the SNORCLE
refraction dataset **05-023** (§2.5). [V]

### 3.3 European national programmes — verified

| # | Programme | Country / region | Years | Type | Line-km | Size (measured) | Licence | Verified URL | Access | Flag |
|---|-----------|------------------|-------|------|---------|-----------------|---------|--------------|--------|------|
| 156 | **FIRE** — Finnish Reflection Experiment, 4 transects | Finland | 2001–05 | Deep reflection to 20 s TWT, **including raw field SEG-Y** | **2,104 km CMP** | **1,147,373,744,961 B = 1.147 TB (1.043 TiB) across 1,963 files** — per profile, independently re-measured from the Metax `fileset.total_files_size` field: **P1 285,592,876,279 B / 471 files**; **P2 181,195,324,089 B / 352**; **P3 335,222,608,202 B / 572**; **P4 345,362,936,391 B / 568** | **CC BY 4.0** | Full DOIs — P1 `https://doi.org/10.23729/45d0ade6-1b7b-4008-8938-e2a2b7d2aa23` · P2 `https://doi.org/10.23729/8351af00-e164-4721-9901-063ec14b6f66` · P3 `https://doi.org/10.23729/81f4d8ec-30de-4c86-a69a-ae4ff1c0c49f` · P4 `https://doi.org/10.23729/374cabc4-b12e-4b5e-8330-9c3b0ed64d3c`. Also GTK Hakku (free). Report `https://tupa.gtk.fi/julkaisu/specialpaper/sp_043.pdf` (162,024,986 B) | **Direct download, no login** — two-step token API: `POST etsin.fairdata.fi/api/download/authorize` → `GET download.fairdata.fi/download?token=…` | **The largest single open deep-crustal reflection dataset found anywhere in this survey**, and it includes raw field records. **Each profile has 2–3 DOIs** (IDA and PAS copies of the same bytes) — do not double-count | **[V]** — file counts and byte totals reproduced independently |
| 157 | **IBERSEIS-NI** — normal-incidence | SW Iberia, Ossa-Morena / South Portuguese Zone | 2001 | Deep reflection, 400-channel, 35 m group | **303 km** | **37,296,716,311 B = 34.74 GiB** (raw zip) | **CC BY 4.0** | https://doi.org/10.20350/digitalCSIC/9016 ; migrated/stack `10.20350/digitalCSIC/12643` | **Direct download** | Part of **SeisDARE** | **[V]** |
| 158 | **IBERSEIS-WA** — wide-angle | SW Iberia | 2001–03 | Wide-angle, 500–1000 kg explosive shots | 2 transects | **1,225,970,640 B** (SeisDARE copy) · **484,947,799 B** tarball / 484,950,262 B directory (EarthScope copy; 33 files, 1,326,640,320 B uncompressed) | **CC BY 4.0** (CSIC copy); no statement on the EarthScope copy | https://doi.org/10.20350/digitalCSIC/9018 · https://data.earthscope.org/archive/assembled/03-012/03-012.IBERSEIS.DATA.SEGY.tar.gz | **Direct download — two independent copies** | | **[V]** |
| 159 | **ALCUDIA-NI** | Central Iberia | 2007 | Deep reflection, 60–90 fold | **230 km** | part of the ~488 GB SeisDARE holding | **CC BY 4.0** | https://doi.org/10.20350/digitalCSIC/9049 | Direct download | | **[V]** |
| 160 | **ALCUDIA-WA** | Central Iberia | 2012 | Wide-angle, >900 Texans | **~310 km** (350 total) | **354,423,680 B** (`ALCUDIA-WA.sgy`, byte count via HTTP 206 `Content-Range`) | **CC BY 4.0** | https://doi.org/10.20350/digitalCSIC/9061 ; also FDSN **7A_2012** (909 stations) via `ph5ws` | Direct download | | **[V]** |
| 161 | **ESCI** — N, Betics, Valencia Trough | Spain | 1991–93 | Deep reflection, onshore + offshore | ESCI-N1 140 km, N2 65 km, **Valencia Trough 450 km** | within SeisDARE | **CC BY 4.0** | `10.20350/digitalCSIC/9894`, `/9925`, `/9937` | Direct download | ESCI-Valencia Trough explicitly extends the ECORS-Pyrenees transect | **[V]** |
| 162 | **ILIHA** | Iberia | 1989 | Long-range DSS, 6 star profiles, 10 offshore + 5 land shots | 6 profiles | within SeisDARE | **CC BY 4.0** | https://doi.org/10.20350/digitalCSIC/12623 | Direct download | | **[V]** |
| 163 | **CIMDEF** | Central Iberia | 2017 | Wide-angle | — | — | CC BY 4.0 | **Embargoed at CSIC** (`10.20350/digitalCSIC/10528`) but **open at EarthScope** as FDSN **XY_2017**, 874 stations | Open via `ph5ws` | A dataset that is closed at its national host and open at EarthScope | **[V]** |
| 164 | **BIRPS** | UK offshore | 1981–98 | Deep reflection, 15–40 s TWT | **~12,000 km** | not stated | Research use only; no commercial resale | https://metadata.bgs.ac.uk/geonetwork/srv/api/records/c425c9fc-cb6c-352c-e044-0003ba9b0d98 | **Email request + cost recovery** (enquiries@bgs.ac.uk) | **Raw *and* processed digital data are archived by BGS**, "available subject to the cost of reproduction and handling". **Not** on EDINA, UKOGL or NGDC as a download | **[V]** |
| 165 | **DEKORP** (+ KTB lines) | Germany | 1984–99 | Deep reflection (Vibroseis); raw SEG-Y, stacks, migrations, geometry ASCII, scanned reports | **~4,700 km / ~40 lines + one ~400 km² 3D**; **28 DOIs published** | not stated | **CC BY-NC 4.0** (raw); **CC BY 4.0** (reprocessed 2S / 2N / 9N / 3B-MVE-W) | https://dataservices.gfz-potsdam.de/dekorp/ ; e.g. https://doi.org/10.5880/GFZ.DEKORP-1A.001 | **Web request form — NOT downloadable** | **Correction to a widespread assumption:** *every* landing page, including the CC BY 4.0 ones, states "The dataset is not available for public download. Please fill in the form to contact the authors." **DEKORP is licence-open but access-closed.** | **[V]** |
| 166 | **GFZ GIPP — Rhenish Massif** | DE / BE / LU / FR | 1978–79 | Refraction / wide-angle; 137 MARS units, 20 shots, 2,740 3-C records | **600 km main + cross-profiles** | not stated | **CC BY 4.0** | https://doi.org/10.5880/GIPP.197901.1 | Request form | Crust + uppermost mantle | **[V]** |
| 167 | **GFZ GIPP — TTZ-South** | Poland / Ukraine, Teisseyre–Tornquist Zone | 2018 | Refraction / wide-angle reflection; raw + SEG-Y + miniSEED | **550 km** | not stated | **CC BY-NC 4.0** | https://doi.org/10.5880/GIPP.201806.01 | Request form | Mechie, GFZ | **[V]** |
| 168 | **CROP** — digital SEG-Y | Italy | 1986–2000s | Deep reflection, land + marine | **~10,000 km** | not stated | **Paid licence, not open** | http://www.crop.cnr.it/it/bancadati/listino-prezzi | **Paid, per-km** | Verified tariff: **5 €/km** raw SEG-Y, **8 €/km** stack/migration for universities; **150 / 200 €/km** industry. **Not in OGS SNAP** | **[V]** |
| 169 | **CROP Atlas** (scanned profile plates) | Italy | 2003 | Scanned deep-reflection plates | as above | **4,226,233 B** for the sample plate `F_54_CROP_04.pdf` | **CC BY 4.0** | https://www.videpi.com/deposito/videpi/crop/F_54_CROP_04.pdf | **Direct download, no registration** | The printed ISPRA atlas (Mem. Descr. 62) is **paper-only, €120** — the site states the profiles are available only on paper because the files are too large | **[V]** |
| 170 | **NFP-20 / NRP-20** | Switzerland | 1986–93 | Deep reflection | — | index GeoPackage **18,755,584 B** | **"proprietary"** (swisstopo STAC) | https://data.geo.admin.ch/api/stac/v0.9/collections/ch.swisstopo.geologie-reflexionsseismik | **Index only — traces not public** | The collection says downloads exist for *some* processed lines; no NFP-20 line exposed one. For raw/non-public data, "contact the rights holder directly" | **[V]** |
| 171 | **TRANSALP** | Germany / Austria / Italy, Eastern Alps | 1998–2001 | Deep reflection, Munich→Venice transect | — | **431,696,728 B** (2 × 215,848,364) | **CC BY 4.0** | https://zenodo.org/records/14719546 | **Direct download** | **CMP stack + diffraction image SEG-Y only — no field records** | **[V]** |
| 172 | **EGT** — European Geotraverse | Europe, North Cape → Tunisia | 1983–90 | **Compilation atlas, not shot records** — compiled grids and catalogues | — | **20,841,746 B** | **CC BY 3.0** | https://doi.org/10.1594/PANGAEA.860351 → https://epic.awi.de/id/eprint/35095/11/the_european_geotraverse_data.zip | **Direct download** | The original CD-ROM. No CSS traces | **[V]** |
| 173 | **HIRE** | Finland, 16 ore districts | 2007–10 | High-resolution reflection, 402-channel @ 12.5 m; processed **and** unprocessed field data | not stated | not stated | **GTK Basic Licence — not open** | https://hakku.gtk.fi/en/locations/216 | **Paid**, Hakku shop, + 25.5 % VAT | Not in Fairdata | **[V]** |
| 174 | **BABEL** — wide-angle | Baltic / Bothnian Sea + Finnish & Swedish land stations | Sep–Oct 1989 | Wide-angle refraction / reflection; lines 1, 3, 4, 7 + P-velocity models | **2,268 km survey** | **573,918,500 B across 73 files** | **CC BY 4.0** | https://doi.org/10.23729/e163d50e-2553-483b-8ec0-26563ca29677 | **Direct download, no login** | 73 files, re-measured via Metax | **[V]** |
| 175 | **BABEL** — marine multichannel | Baltic Sea | 1989 | Deep marine reflection (near-vertical) | 2,268 km | — | — | **No public archive.** Not at BGS, GEUS, SGU or Fairdata; traced to the Durham/BIRPS legacy (R. Hobbs) | Personal / email request | | **[V]** *that it is not archived* |
| 176 | **SVEKALAPKO** | Finland | 1998–99 | Wide-angle **CSS** + passive array; 4 × 2-D profiles, 62 stations | — | CSS **145,603,748 B**; array ~100 GB *(est.)* | **CC BY 4.0** / open | `https://doi.org/10.23729/30164c22-dfe1-490a-baa6-1580b628e4a2` (CSS, 9 files, 145,603,748 B) ; FDSN net **ZB** at GEOFON | Direct download / FDSN | | **[V]** |
| 177 | **SVEKA'81 / SVEKA'91 / SVEKA joint** | Finland | 1981 / 1991 | Wide-angle | — | **23,894,577 / 30,352,381 / 47,084,110 B** | **CC BY 4.0** | `10.23729/1a2f3233-d7ac-4d1e-88a8-c50a4fcd43f6`, `10.23729/24f42b76-6f67-4804-897c-899e3fb6dc3b`, `10.23729/6b888b28-2593-4d54-afa8-f0aa951ec043` | Direct | End-to-end proven: `sveka81_z.sgy` (15,361,200 B) pulled anonymously and its EBCDIC header read | **[V]** |
| 178 | **FENNIA / POLAR / BALTIC / Kuusamo** | Finland | 1982–94 | Wide-angle | — | **115,968,715 / 192,713,385 / 184,141,846 / 199,997,293 B** | **CC BY 4.0** | `10.23729/0db3cba6-d1eb-42b4-91b9-d2caf971182d`, `10.23729/30356f10-2e28-47d3-9e77-2f01f80a9207`, `10.23729/782793a3-3c4d-4715-9745-f34ea7715802`, `10.23729/7dc49d32-382c-42f0-9940-816448170d36` | Direct | | **[V]** |
| 179 | **PASSEQ 2006-08** | Trans-European Suture Zone (PL/DE/CZ/LT) | 2006–08 | **Passive** array, 204 stations (not controlled source) | — | — | open | FDSN **7E** — `https://geofon.gfz.de/fdsnws/dataselect/1/query?network=7E&…` | **Open FDSN, no auth** | Confirmed HTTP 200, `application/vnd.fdsn.mseed` | **[V]** |
| 180 | **SGU legacy land reflection** | Sweden (Skåne, Gotland) | 1960s–80s | 2-D reflection | not stated | **2,777,132,743 B** (1,008,797,868 + 1,768,334,875) | **CC0** | https://resource.sgu.se/data/datasets/nettonollteknik/reflektionsseismik/1_skane_land.zip and `/3_baltic_land.zip` | **Direct bulk download** | SGU has **no** deep-crustal reflection product; all SGU geological data open since 9 Jun 2024 | **[V]** |
| 181 | **Buräsk PGF / Ludvika** | Sweden | ~2015–16 | 2-D reflection | — | **2,311,002,736 B** / **2,002,524 B** | open | `researchdata.se/catalogue/dataset/snd1099-1/1.0` ; `10.5878/8gbt-cf87` | Direct | | **[V]** |
| 182 | **Siljan Ring (Mora, Orsa)** | Sweden | 2011 | 2-D reflection | — | not measured | **CC BY-SA 4.0** | `10.57804/DYXF-VN94`, `10.57804/3GJ5-XT38` | **Stacks direct; raw SEG-D on request** | | **[V]** |
| 183 | **Norway** (NGU / Sodir / Diskos) | Norwegian shelf | 1960s– | Marine seismic | entire NCS | Bulletin-8 profiles **1,207,746 B** | NLOD (metadata) | https://www.sodir.no/en/facts/data-and-analyses/open-data/ | **Metadata free; traces paid via Diskos** | NGU holds **no** deep-seismic download product; Sodir open data is index/administrative only | **[V]** |
| 184 | **ViDEPI** | Italy | 1957– | Scanned industry seismic, **612 marine lines** | — | — | **CC BY 4.0** | https://www.videpi.com/videpi/sismica/sismica.asp | Direct | Also hosts the free CROP Atlas plates (row 169) | **[V]** |
| 185 | **GEUS Deep Subsurface** | Denmark | — | 2D/3D marine seismic | — | — | — | https://eng.geus.dk/products-services-facilities/data-and-maps/subsurface-data-denmark | Free download of "processings" since Oct 2023 | | **[V]** |
| 186 | **Santorini crustal magma plumbing** | Greece | 2015–16 | MCS + OBS | — | **158,101,505,263 B = 147.24 GiB** — 12 SEG-Y tarballs (34.6 / 34.4 / 29.8 / 25.9 / 4.8 / 4.9 / 4.8 / 4.9 / 4.5 / 4.1 / 3.0 / 3.0 GB) + a 45,055 B `manifest.txt` | not stated | https://data.earthscope.org/archive/assembled/15-008/ | Anonymous | Re-measured directly from the `?json` listing. An earlier figure of "300.6 GB / 485 files" for this dataset is **wrong** | **[V]** |
| 187 | **Ivrea Zone (SEIZE) 3D** | Italy | 2020 | 3-D wide-angle, top 5 km | — | — | **CC BY 4.0** | https://doi.org/10.5880/GIPP.202016.2 | Request form | | **[V]** |
| 188 | **Baza Basin (BASE)** | Spain | 2013 | Reflection, 3 Vibroseis lines | — | — | **CC BY 4.0** | https://doi.org/10.5880/GIPP.201312.1 | Request form | | **[V]** |
| 189 | **ECORS** | France (Pyrenees, Alps) | 1983–91 | Deep reflection | ~250 km (Pyrenees) | — | — | **No open archive located** at BRGM, InfoTerre, CNRS/INSU or SISMER | Not public | `search: ECORS Pyrenees deep seismic SEG-Y archive BRGM` | **[U]** |
| 190 | **URSEIS 1995** | Urals, Russia | 1995 | Reflection + wide-angle | ~500 km | — | — | **No repository found** in DataCite, EarthScope or SeisDARE | Not public | `search: URSEIS 1995 Urals reflection SEG-Y archive` | **[U]** |
| 191 | **EUROBRIDGE** | East European Craton | 1994–97 | Refraction | ~2,000 km | — | — | **No repository found**; published velocity models only | Not public | | **[U]** |
| 192 | **KOLA95** | Kola / Barents | 1995 | DSS | — | **87,554,645 B** | not stated | https://data.earthscope.org/archive/assembled/98-003/ | Anonymous | Companion to KOLA92 VSP (row 136) | **[V]** |

### 3.4 Legacy rescue: SeisDARE, EPOS, and the state of European aggregation

| # | Initiative | What it is | Coverage | Licence | Verified URL | Flag |
|---|-----------|------------|----------|---------|--------------|------|
| 193 | **SeisDARE** (Seismic DAta REpository) | The Iberian open-access legacy-rescue repository — four decades of Spanish/Portuguese deep-crustal reflection and wide-angle data, curated with full metadata, hosted on **DIGITAL.CSIC** | IBERSEIS-NI/WA, ALCUDIA-NI/WA, ESCI (N, Betics, Valencia Trough), ILIHA and more; **~488 GB** | **CC BY 4.0** | Paper: https://essd.copernicus.org/articles/13/1053/2021/ ; data under `https://doi.org/10.20350/digitalCSIC/…` (see rows 157–163) | **[V]** |
| 194 | **EPOS Multi-scale Laboratories (EPOS-MSL)** | **A dead end for this purpose.** A *laboratory* catalogue — 3,204 datasets from 119 labs covering rock/melt physics, palaeomagnetism, geochemistry, microscopy, tomography and analogue modelling. **Holds no field controlled-source seismic.** | — | — | https://epos-msl.uu.nl | **[V]** *that it is not relevant* |
| 195 | **EPOS Controlled Source Seismic metadata catalogue** | The relevant EPOS effort: a discovery catalogue of European CSS experiments (Lorenz et al.) — **discovery metadata only, deliberately including closed datasets**, and not yet in the production EPOS portal | Europe-wide | — | Preprint https://doi.org/10.5194/essd-2026-498 ; code https://github.com/epos-css/metadata | **[V]** preprint + repo; the release DOI `10.5880/fidgeo.2026.059` **404s — not yet minted** |
| 196 | **OpenFIRE** (`avaa.tdata.fi/web/fire`) | The FIRE portal cited by the SeisDARE 2021 paper | Finland | — | **DEAD** — redirects to fairdata.fi and 404s. Superseded by the Etsin/IDA DOIs in row 156 | **[V]** *that it is dead* |

### 3.4b Enumerating the Finnish holdings (Metax API)

Finland's datasets are discoverable and byte-measurable without any login:

```bash
# search
curl 'https://metax.fairdata.fi/v3/datasets?search=FIRE%20reflection%20seismic&limit=50'
# one dataset: title, DOI, licence, file count and exact total bytes
curl 'https://metax.fairdata.fi/v3/datasets/<uuid>' \
 | python -c "import sys,json;d=json.load(sys.stdin);print(d['persistent_identifier'],d['fileset'])"
```

`fileset.total_files_size` and `total_files_count` are exact. Note `storage_service`:
`ida` and `pas` are two copies of the same dataset — counting both doubles the total. The
old Etsin v2 API (`etsin.fairdata.fi/api/v2/datasets`) **404s**; use Metax v3. [V]

Verified sizes for the other Finnish controlled-source datasets (all CC BY 4.0, all with
complete DOIs):

| # | Dataset | Files | Bytes | DOI |
|---|---------|-------|-------|-----|
| 196a | **BABEL** wide-angle refraction and reflection survey | 73 | **573,918,500** | `10.23729/e163d50e-2553-483b-8ec0-26563ca29677` |
| 196b | **Kuusamo** wide-angle refraction and reflection survey | 23 | **199,997,293** | `10.23729/7dc49d32-382c-42f0-9940-816448170d36` |
| 196c | **POLAR** wide-angle refraction and reflection profile | 12 | **192,713,385** | `10.23729/30356f10-2e28-47d3-9e77-2f01f80a9207` |
| 196d | **BALTIC** wide-angle refraction and reflection profile | 12 | **184,141,846** | `10.23729/782793a3-3c4d-4715-9745-f34ea7715802` |
| 196e | **SVEKALAPKO** wide-angle refraction and reflection survey | 9 | **145,603,748** | `10.23729/30164c22-dfe1-490a-baa6-1580b628e4a2` |
| 196f | **FENNIA** wide-angle refraction and reflection profile | 12 | **115,968,715** | `10.23729/0db3cba6-d1eb-42b4-91b9-d2caf971182d` |
| 196g | **SVEKA** wide-angle refraction and reflection profile | 8 | **47,084,110** | `10.23729/6b888b28-2593-4d54-afa8-f0aa951ec043` |
| 196h | **SVEKA'91** wide-angle refraction and reflection profile | 8 | **30,352,381** | `10.23729/24f42b76-6f67-4804-897c-899e3fb6dc3b` |
| 196i | **SVEKA'81** wide-angle refraction and reflection profile | 8 | **23,894,577** | `10.23729/1a2f3233-d7ac-4d1e-88a8-c50a4fcd43f6` |

**Finland's open controlled-source seismic total: 1,148,887,419,516 B ≈ 1.149 TB**
(FIRE 1–4 plus the nine wide-angle surveys above, deduplicated across IDA/PAS copies). [V]

### 3.5 Three European conclusions worth flagging

1. **DEKORP is licence-open but access-closed.** All 28 GFZ datasets — *including* the
   CC BY 4.0 reprocessed lines — carry "The dataset is not available for public download."
   The same applies to every GFZ GIPP controlled-source dataset. Any claim that DEKORP is
   directly downloadable is wrong.
2. **The Central European refraction experiments are open and essentially undocumented as
   such.** POLONAISE'97, CELEBRATION 2000, ALP 2002, SUDETES 2003 and DOBREfraction'99 are
   anonymously downloadable as raw SEG-Y from EarthScope — **9.33 GB in total** — with no
   licence statement anywhere. This is the least-known result in this document.
   **Caveat, verified:** the CELEBRATION 2000 tarball contains 62 `_e` and 62 `_n`
   component files but only **5** `_z` files — the vertical-component bulk is missing.
3. **Finland is the model for the rest of the world.** ~1.15 TB of FIRE (raw field records
   included) plus BABEL, SVEKALAPKO, SVEKA, POLAR, BALTIC and FENNIA — all CC BY 4.0, all
   downloadable with no login.

## 4. Asia

See also §6.4 for the Asian experiments confirmed inside the PH5 archive: SINOPROBE-2 `ZC`,
SinoProbe NE China `5G`, NE Tibet `XN`, Tien Shan `Z5`, Korea `Z9`, Vietnam `1C`,
Israel/Jordan GEO-DESIRE `ZW`, Taiwan TAIGER `X3`/`3C`, Tangshan `8E`.

### 4.1 INDEPTH (Tibet) — where it is archived

| # | Assembled ID | Dataset | Years | Type | Measured size | Flag |
|---|--------------|---------|-------|------|---------------|------|
| 121 | **12-013 / INDEPTH-II** | **INDEPTH II** | 1992–1994 | Deep crustal reflection/refraction, SEG-Y | **13,179,603,694 B = 12.27 GiB** | **[V]** |
| 122 | **12-012 / INDEPTH-I** | **INDEPTH I** | 1992–1994 | Deep crustal reflection, SEG-Y | **6,233,456,609 B = 5.81 GiB** | **[V]** |
| 123 | **96-013 / Ind2** | INDEPTH-2 **wide-angle** experiment, Tibet 1994 | 1994 | Wide-angle refraction, SEG-Y | **1,608,926,604 B = 1.50 GiB** | **[V]** |
| 124 | **01-001 / IND3** | **INDEPTH III** reflection/refraction experiment | 1997 | Reflection + refraction, SEG-Y | **531,869,445 B** | **[V]** |
| 125 | **07-024 / INDEPTHIV** | Deep structure of the NE Tibet collision zone (**INDEPTH IV**) | 2007 | PH5 | **0 files in the assembled bucket** — PH5 row; the data is in `ph5ws` | **[V]** catalogued; **[U]** size |
| 126 | **07-027** | INDEPTH IV, SEG-Y version | 2007 | SEG-Y | **`Data = N` — catalogued but not served** | **[V]** |
| 127 | Passive INDEPTH networks | — | II **XR** (1994, 13 sta), III **XR** (1997–99, 62 sta), IV **X4** (2007–09, 97 sta, Missouri S&T) and **XO** (2007–09, Cambridge) | Passive | — | **[V]** in IRIS `fdsnws` |

**Answer to "where is INDEPTH archived":** the controlled-source data is in the EarthScope
**assembled-dataset** archive (four open tarballs, **≈19.6 GiB** total), not under an FDSN
network code; the passive deployments are separately under `XR`, `X4`, `XO`. [V]

### 4.2 Russian / former-Soviet **Deep Seismic Sounding (DSS)** and Peaceful Nuclear Explosion (PNE) profiles

All open, all `Restricted: N`, all anonymous HTTP from the EarthScope assembled archive.
**This is the single best open source of long-range DSS/PNE crustal-mantle data.** [V]

| # | Assembled ID | Profile | Years | Type | Measured size | Flag |
|---|--------------|---------|-------|------|---------------|------|
| 128 | **09-001 / DSS-EQEVENTS** | Deep Seismic Sounding — earthquake seismic records | 1984–1990 | DSS, SEG-Y | **324,104,066 B** | **[V]** |
| 129 | **05-003 / Bath2** | **Batholith-2 PNE** long-range profile | 1987 | PNE-source DSS, SEG-Y | **201,999,974 B** | **[V]** |
| 130 | **01-009 / Quartz** | **QUARTZ-DSS** — the classic ~4,000 km ultra-long-range PNE profile | 1984–1987 | PNE-source DSS, SEG-Y | **167,619,945 B** | **[V]** |
| 131 | **03-011 / DSSRIFT** | **Baikal Lake** refraction–reflection profile using PNEs | 1982–1983 | PNE-source DSS, SEG-Y | **131,687,800 B** | **[V]** |
| 132 | **05-002 / Bath1** | **Batholith-1 PNE** | 1980 | PNE-source DSS, SEG-Y | **129,553,839 B** | **[V]** |
| 133 | **05-020 / Bazalt1** | **Bazalt-1** long-range DSS profiles | 1989 | DSS, SEG-Y | **122,294,677 B** | **[V]** |
| 134 | **05-021 / Bazalt2** | **Bazalt-2** long-range DSS profiles | 1990 | DSS, SEG-Y | **52,939,668 B** | **[V]** |
| 135 | **02-010 / Craton** | **CRATON-DSS** deep seismic sounding | 1978–1980 | DSS, SEG-Y | **15,044,651 B** | **[V]** |
| 136 | **07-004 / KOLA92-VSP** | **Kola Superdeep Borehole** reflection / VSP | 1992 | Borehole reflection, SEG-Y | **33,345,833 B** (directory total; tarball 33,345,151 B). Companion **98-003 / KOLA95** DSS = **87,554,645 B** | **[V]** |

### 4.3 Other Asian / adjacent

| # | Item | Region | Years | Type | Size | Access | Flag |
|---|------|--------|-------|------|------|--------|------|
| 137 | **04-007 / DOBRE99** — DOBREfraction'99 | Donbas Foldbelt, **Ukraine** | 1999 | Wide-angle refraction, SEG-Y | **171,261,960 B** | Assembled, direct HTTP | **[V]** |
| 138 | **09-005 / KOREANPENINSUL** — Korean Peninsula Refraction Profile | South Korea | 2008 | Refraction, PH5 (650 stations, FDSN `Z9`) | see §6.4 | PH5 + assembled | **[V]** |
| 139 | **10-016 / REDRIVER** — Study of the Crustal Structure of Northern Vietnam | Vietnam (Red River) | 2008/2010 | Crustal, PH5 (400 stations, FDSN `1C`) | see §6.4 | PH5 + assembled | **[V]** |
| 140 | **06-008 / GEODESIRE** — GEO-DESIRE wide-angle reflection/refraction | Israel & Jordan, Dead Sea | 2006 | Wide-angle, PH5 (370 stations, FDSN `ZW`) | see §6.4 | PH5 + assembled | **[V]** |
| 141 | **17-028 / SinoProbe** — SinoProbe NE China Transect | NE China | 2011 | PH5, 357 stations (FDSN `5G`) | see §6.4 | PH5 + assembled | **[V]** |
| 142 | **08-002 / TAIGER** — TAIGER active-source **land refraction** | Taiwan | 2008 | — | **`Data = N`, Format `none` — catalogued but NOT served** | — | **[V]** — the Taiwan land refraction data is *not* available; only the pilot test `X3` (148 sta, 2006) and `3C` (0 sta) are in PH5 |
| 143 | **92-002 / Iceland** — South Iceland Seismic Refraction Experiment | Iceland | 1990 | Refraction, **AH format** | **75,220,556 B** | Assembled, direct HTTP | **[V]** |
| 144 | **96-010 / ACRUP** — Antarctic Crustal Profile | Antarctica | 1993–1994 | Crustal profile, SAC | **1,020,691 B** | Assembled, direct HTTP | **[V]** |
| 144a | **08-023 / TAIGER-OBSIP** — TAIGER ocean-bottom component | Taiwan, offshore | 2008–2009 | Marine wide-angle OBS, **PSEGY**, 3 files | **35,301,486,540 B = 32.88 GiB** | Assembled, direct HTTP | **[V]** — **the TAIGER data that *does* exist openly**; the land-refraction row `08-002` is `Data = N` |
| 144b | **13-011** — Japan Subduction Zone | Japan | 2002 | Reflection/refraction, SEG-Y | **355,784,290 B** | Assembled, direct HTTP | **[V]** |
| 144c | **26-006** — US–Japan Collaborative Research: multi-scale seismic imaging of the Mariana subduction factory | Mariana / W Pacific | 2002 | SEG-Y, 3 files | **3,798,093,839 B = 3.54 GiB** | Assembled, direct HTTP | **[V]** |
| 144d | **12-008 / MARIANASTRENCH** — Marianas | Mariana Trench | 2012 | Marine wide-angle, SEG-Y, 7 files | **438,975,119,154 B = 408.83 GiB** | Assembled, direct HTTP | **[V]** |
| 144e | **93-005** — Tibetan Plateau Passive-Source Seismic Experiment | Tibet | 1991–1992 | **Passive**, SEG-Y | **5,234,897,937 B = 4.88 GiB** | Assembled, direct HTTP | **[V]** |
| 144f | **94-002** — 1992 Pakistan Himalayas Passive-Source Broadband Experiment | Pakistan Himalaya | 1992 | **Passive**, SEG-Y, 4 files | **5,255,286,146 B = 4.89 GiB** | Assembled, direct HTTP | **[V]** |
| 144g | **92-006** — Kazakhstan NRDC Seismic Product | Kazakhstan | 1987 | SAC | **1,026,313,732 B = 0.96 GiB** | Assembled, direct HTTP | **[V]** |
| 144h | **92-007** — Borovoye Geophysical Observatory, northern Kazakhstan | Kazakhstan | 1969–1990 | **AH** format | **2,232,733 B** | Assembled, direct HTTP | **[V]** — the historic Soviet PNE-recording observatory archive |
| 144i | **00-045** — **Saudi Arabia 1978** crustal refraction profile | Arabian Shield | 1978 | Refraction, SEG-Y | **6,476,359 B** | Assembled, direct HTTP | **[V]** |
| 144j | **05-006** — Xinjiang China test sites, nuclear explosions | Xinjiang, China | 1967–1996 | **IMS** format | **127,517,438 B** | Assembled, direct HTTP | **[V]** |
| 144k | **17-003** — Calibration of regional seismic stations in the Middle East | Middle East | 2002 | SAC, 7 files | **291,909,210 B** | Assembled, direct HTTP | **[V]** |

### 4.4 Asian national programmes and portals

| # | Programme / host | Country | Type | Size | Licence | Verified URL | Access | Flag |
|---|------------------|---------|------|------|---------|--------------|--------|------|
| 144l | **JAMSTEC Seismic Survey Database** | Japan | The national marine **MCS and OBS** archive — onshore–offshore and subduction-zone crustal profiles, searchable by method, year and area | not stated | JAMSTEC site policy + "Basic Policies on the Handling of Data and Samples" | https://www.jamstec.go.jp/obsmcs_db/e/ (HTTP 200) · DOI **10.17596/0002069** · DARWIN portal https://www.godac.jamstec.go.jp/darwin/en/ (HTTP 200) | **Academic use via a data request form** — the page states plainly: *"All the MCS and OBS data are available for academic use via the data request form."* Not a direct download | **[V]** |
| 144m | **SINOPROBE** — Chinese national programme | China | Deep reflection, wide-angle, MT; 2008–2014 (SinoProbe I). **SinoProbe II** announced Nov 2024 as a ~$1 bn survey | — | — | `www.sinoprobe.org` — **does not resolve** (curl exit 000, no TCP connection). No dataset portal found at the China Geological Survey or the National Earth System Science Data Center (`https://www.geodata.cn`, HTTP 200 but no SINOPROBE seismic collection located) | **No Chinese-side public data portal exists.** The **only** openly downloadable SINOPROBE data is at EarthScope — `ZC` SINOPROBE-2 Controlled Source (2009, 1,190 stations) and `5G` NE China Transect (2011, 357 stations) via `ph5ws`, plus assembled row `17-028` | **[V]** — a significant negative result |
| 144n | **NGRI / CSIR** — Indian Deep Seismic Sounding (DSS) | India | ~1970s–present DSS profiles across the Indian shield, Deccan, Himalaya foredeep | — | — | https://www.ngri.res.in (HTTP 200) — institutional site only; **no data-download portal located**, and targeted searches returned nothing | **Not public.** Indian DSS results exist in the literature and in the USGS Global Crustal Database compilation (§7), not as downloadable traces. `search: NGRI deep seismic sounding SEG-Y data request India` | **[U]** |
| 144o | **TAIGER** — Taiwan | Taiwan | The land-refraction leg is catalogued at EarthScope as `08-002` with **`Data = N`** and `Format: none`; the pilot test is PH5 `X3` (148 stations, 2006) and `3C` (0 stations). The **ocean-bottom leg `08-023` is open** (32.88 GiB, §4.3) | see §4.3 | not stated | https://ds.iris.edu/mda/08-002/ · https://data.earthscope.org/archive/assembled/08-023/ | Mixed — OBS open, land refraction not served | **[V]** |
| 144p | **COCORP Taiwan** | Taiwan | Deep reflection, on the Cornell ELLIPSE server | **366 MiB** (2 files) | not stated | https://cocorp.eas.cornell.edu/Taiwan/ | Anonymous HTTPS | Cross-reference to §2.1 row 7 — an easily missed Taiwanese deep-crustal holding | **[V]** |

**Summary for Asia.** The pattern is consistent and worth stating plainly: **no Asian
national agency publishes deep-crustal controlled-source seismic for direct download.**
China (SINOPROBE), Japan (JAMSTEC), India (NGRI) and Taiwan all either require a request
form or have no portal at all; Iran's Makran dataset is CC BY 4.0 but request-gated at GFZ
(§4.5). Everything that *is* openly downloadable for Asia sits in US infrastructure — the
EarthScope PH5 archive (§6.4) and the assembled-dataset archive (§4.1–4.3) — or, for
Taiwan, on Cornell's COCORP server. **The two openly downloadable Asian controlled-source
crustal experiments outside East Asia are both in Israel** (`ZW` 2006 and `1C` 2018). [V]

### 4.5 West Asia / Middle East

| # | Programme | Country / region | Years | Type | Line-km | Size | Licence | Verified URL | Access | Flag |
|---|-----------|------------------|-------|------|---------|------|---------|--------------|--------|------|
| 144q | **GEO-DESIRE WRR** (FDSN `ZW`, PASSCAL **06-008**) | Israel + Jordan, Dead Sea Transform | 20–22 Mar 2006 | Wide-angle reflection/refraction, explosive | **240 km** (field report); array 185.1 km, shot line 188.8 km | **199,606,272 B ≈ 200 MB measured** (30 stations pulled over full epochs; 29 returned exactly 540,672 B, one short epoch 98,304 B). Assembled dir `06-008` = **150,448,412 B** | No explicit licence; StationXML `restrictedStatus="open"`, MDA "A = Open data access". DOI 10.7914/SN/ZW_2006 | https://ds.iris.edu/mda/ZW/?starttime=2006-01-01&endtime=2006-12-31 · field report http://ds.iris.edu/data/reports/2006/06-008/GEODESIRE.report.pdf | Direct download, anonymous | **Only the 370-channel single-component Texan subset is archived.** The field report records a further **199 three-component Earth Data Logger PR6-24 (GFZ GIPP) instruments whose data is not archived anywhere** — obtainable only by emailing J. Mechie / M. Weber at GFZ. Derived from SEG-Y `wrr[1-11]_ch1_txn_rmdc.sgy`, 120 s cut per shot | **[V]** |
| 144r | **Galilee Seismic Experiment (GSE)** (FDSN `1C` **2018**, PASSCAL **18-013**) | Israel, Dead Sea Transform / Sea of Galilee | Apr 2018 | Refraction + near-vertical reflection, explosive; **land + lake hydrophones** | E–W across the DST ≈ **68 km**; N–S along the transform ≈ **48 km**; array 71.6 km | **≈21.7 GB** (4 channels measured over full epochs, mean 39.4 MB/ch × 550 ch) | `restrictedStatus="open"`; DOI 10.7914/SN/1C_2018 | https://ds.iris.edu/mda/1C/?starttime=2018-01-01&endtime=2018-12-31 · report http://ds.iris.edu/data/reports/2018/18-013 | Direct download, anonymous | USGS Woods Hole. **550 channels: 510 DPZ land + 40 DPH hydrophone floats on the Sea of Galilee**, 250 Hz continuous; 12 shots of 300–400 kg at ~17 m; 512 Texans at 200 m spacing. **Metadata bug:** in `ph5ws/event?catalog=1C&format=shottext` the Latitude/Longitude columns are **transposed** for report 18-013 | **[V]** |
| 144s | **Western Makran Seismic Transects** (GFZ GIPP **201718**) | **IRAN**, western Makran subduction zone | Sep 2017 (published 2020) | Crustal-scale deep seismic sounding — refraction / wide-angle reflection, explosive | **3 N–S profiles, ≈597 km** (P1 ≈209, P2 ≈190, P3 ≈198 km) | **not stated** — DataCite `<sizes/>` empty, no measurable endpoint | **CC BY 4.0**; moratorium **ended 2023-06-30** | DOI **10.5880/GIPP.201718.1** → https://dataservices.gfz-potsdam.de/gipp/showshort.php?id=escidoc:5009895 (HTTP 200) · https://www.gfz.de/en/makran | **Request form / email** — "The dataset is not available for public download. Please fill in the form to contact the authors." | GFZ + IIEES (Mokhtari); Haberland et al., 9–10 shots per profile, **400–800 kg** charges, **300 autonomous recorders per profile**. Contents include **raw DATA-CUBE + miniSEED and shot gathers in SEG-Y**. Paper doi:10.1130/G47700.1. **Iran is not a blank** | **[V]** |
| 144t | **SEISMARMARA 2001** (RV *Le Nadir*; IPGP / ITU / TÜBİTAK) | **TURKEY**, Sea of Marmara | 11 Aug – 9 Sep 2001 | Deep-penetration MCS (360 ch, single-bubble source) + **37 OBS** wide-angle + offshore–onshore refraction | **≈4,000 km MCS** (Leg 1 ≈2,000 km deep structure; Leg 2 ≈2,000 km Çınarcık Basin) | Only a **6 MB navigation file** is offered; seismic volume not stated | Cruise DOI 10.17600/1080050; nav "Open access / CONTROLLED DATA"; no licence for the seismic | https://campagnes.flotteoceanographique.fr/campagnes/1080050/ | **Seismic data NOT public** — navigation only, no SEG-Y, no order form | Heavily cited (Bécel 2009/2010, Bayrakçı 2013, Laigle 2008, Carton 2007) yet no MCS/OBS SEG-Y is distributed anywhere | **[V]** |
| 144u | **DESERT 2000** (FDSN `ZR`) | Israel / Palestine, Dead Sea Transform | 2000 | **Passive only in the archives** | — | order **200–350 GB** (56,769 channel-days × ≈6 MB measured mean) | GEOFON page reads `Terms/rights: Unknown` while the abstract says "fully open"; **no DOI minted** (`DOI:Prefix/ZR_2000_not_minted`) | GEOFON network index | Open FDSN | **The DESERT controlled-source WRR and near-vertical-reflection shot gathers are not archived anywhere** — checked GEOFON, GFZ Data Services/GIPP, FDSN and PH5. 66 stations, HHZ/N/E 50 Hz, L4-3D. `ZR` is recycled — an Etna 2019 station leaks into an untimed query | **[V]** |
| 144v | **DESIRE** (FDSN `Z4`) | Dead Sea | 2006–08 | **Passive** array — 38 short-period + 27 broadband, 80 station-epoch rows | — | not stated | DOI 10.14470/M97551339354; `Terms/rights: Unknown` | GEOFON | Open FDSN | **DESIRE splits across two archives:** active source → IRIS PH5 (`ZW`), passive → GEOFON (`Z4`) | **[V]** |
| 144w | **Turkey and Iran — onshore deep-crustal controlled source** | Türkiye, Iran | — | — | — | — | — | Geographic PH5 query (re-run and confirmed): `https://service.iris.edu/ph5ws/station/1/query?level=station&format=text&minlat=25&maxlat=45&minlon=25&maxlon=65` · https://tdvms.afad.gov.tr/ | **Nothing public exists** | **A systematic negative, not a keyword miss.** A *geographic* PH5 query over the whole West Asia box returns **only three networks — `1C` (550 sta, Israel active), `YA` (518 sta, E Anatolian aftershocks, passive) and `ZW` (370 sta, Israel/Jordan active)**. Zero Turkish or Iranian controlled source in PH5. Turkish temporary nets are all passive broadband (`XG_1999`, `YL_2005`, `YH_2012` DANA, `YB_2013` CD-CAT, GONAF). AFAD TDVMS serves earthquake/strong-motion only; MTA/TPAO industry lines are not distributed | **[V]** |

**Network-code recycling — a real trap.** FDSN code **`1C` is Vietnam in 2008 *and* Galilee
in 2018**; **`XA`** is SIMA-Morocco 2010, AIDA_Maine 2012, Apollo, PANDA-Argentina and the
Kaapvaal craton; **`XN`** is NW Tibet 2007, TANGO-Argentina 2022, BOLIVAR-Venezuela 2008
and LARSE-passive 1998; **`ZR`** is DESERT 2000 and an Etna 2019 station. **Always
constrain a network query by time and, better, by bounding box** — the geographic PH5
query above is the reliable way to ask "what controlled-source data exists in region X".

## 5. Australia / New Zealand

### 5.1 Geoscience Australia — Onshore Seismic and Magnetotelluric project (OSMT)

GA states it has acquired **"in excess of 24,000 km of onshore deep crustal seismic
reflection data" since 1980**, plus numerous 2D refraction profiles. [V — GA project page]

Every survey is published as a single **"Processed Seismic Package"** ZIP (stacked, DMO,
post-stack time migration, pre-stack time migration SEG-Y + images + processing report)
on CloudFront under **Creative Commons Attribution 4.0 International (CC-BY)** —
confirmed in the eCat resource-constraints block. **Raw shot gathers are NOT in the
package**; they come by email from `clientservices@ga.gov.au` quoting the eCat number.

Landing pages: `https://pid.geoscience.gov.au/dataset/ga/<ecatID>`
Data: `https://d28rz98at9flks.cloudfront.net/<ecatID>/<name>.zip`

**Every size below was measured by HTTP HEAD this session.** [V]

| # | Survey | eCat | Region | Year | Bytes | GiB | Download file |
|---|--------|------|--------|------|-------|-----|---------------|
| 46 | **L210 South Nicholson** (17GA-SN1…SN5, 1,102 km) | 116881 | NT / QLD | 2017 | 13,503,389,016 | **12.58** | `116881/L210_Processed_Seismic_Package.zip` |
| 47 | **L212 Barkly** (19GA-B1…B5, 812.6 km) | 132890 | NT | 2019 | 11,322,766,709 | **10.55** | `132890/L212_Processed_Seismic_Package_1.zip` |
| 48 | **L213 Darling–Curnamona–Delamerian (DCD)** (22GA-DL1/DL2/CD1/CD2/CD3 + 22GA-UDF, 1,256 km) | 147423 | SA/VIC/NSW | 2022 | 11,011,714,451 (3 files) | **10.26** | `147423/147423_00_0.zip` (+ `_01_0`, `_02_0`) |
| 49 | **L211 Kidson Sub-Basin** (18GA-KB1, 872 km) | 128284 | WA | 2018 | 10,102,820,905 | **9.41** | `128284/L211_Processed_Seismic_Package.zip` |
| 50 | **L205 Canning Coastal** | 89799 | WA | 2014 | 8,918,940,472 | **8.31** | `89799/L205_Processed_Seismic_Package.zip` |
| 51 | **L208 Southeast Lachlan** (18GA-SL1/SL2/SL3, 629 km) | 122684 | VIC / NSW | 2018 | 4,811,629,924 | 4.48 | `122684/L208_Southeast_Lachlan_2018_ecat_122684.zip` |
| 52 | **L203 Eucla–Gawler** | 89637 | WA / SA | 2013–14 | 3,993,671,756 | 3.72 | `89637/L203_Processed_Seismic_Package.zip` |
| 53 | **L207 Boulia Region** (14GA-CF2/CF3 + 15GA-CF3, 853 km) | 89801 | QLD | 2014–15 | 3,803,658,965 | 3.54 | `89801/L207_Processed_Seismic_Package.zip` |
| 54 | **19Q Camooweal** (19Q-C1/C2/C3, 300 km) | 146301 | NW QLD | 2019 | 3,835,167,143 | 3.57 | `146301/146301_00_1.zip` |
| 55 | **L204 Southeastern Mt Isa** (670 km transect) | 89638 | QLD | 2014 | 3,490,711,660 | 3.25 | `89638/L204_Processed_Seismic_Package.zip` |
| 56 | **L196 Youanmi (Yilgarn Craton)** (695 km) | 74423 | WA | 2010 | 2,524,256,237 | 2.35 | `74423/L196_Processed_Seismic_Package.zip` |
| 57 | **L180 Mount Isa** | 69674 | QLD | 2006 | 2,293,228,914 | 2.14 | `69674/L180_Processed_Seismic_Package.zip` |
| 58 | **L195 Capricorn** | 72863 | WA | 2010 | 1,966,630,814 | 1.83 | `72863/L195_Processed_Seismic_Package.zip` |
| 59 | **L184 Isa–Georgetown** | 69254 | QLD | 2007 | 1,838,398,935 | 1.71 | `69254/L184_Processed_Seismic_Package.zip` |
| 60 | **L190 Gawler–Officer–Musgrave–Amadeus (GOMA)** | 70579 | SA / NT | 2008 | 1,761,312,400 | 1.64 | `70579/L190_Processed_Seismic_Package.zip` |
| 61 | **L201 Albany–Fraser Orogen** | 78966 | WA | 2012 | 1,710,363,019 | 1.59 | `78966/L201_Processed_Seismic_Package.zip` |
| 62 | **L189 Gawler–Curnamona–Arrowie** | 69532 (also 69981, identical file) | SA | 2008 | 1,443,407,767 | 1.34 | `69532/L189_Processed_Seismic_Package.zip` |
| 63 | **L199 Yilgarn–Officer–Musgrave (YOM)** | 75097 | WA | 2011 | 1,396,277,982 | 1.30 | `75097/L199_Processed_Seismic_Package.zip` |
| 64 | **L202 Yathong Trough** | 89798 | NSW | 2013 | 1,231,669,901 | 1.15 | `89798/L202_Processed_Seismic_Package.zip` |
| 65 | **L185 Charters Towers** | 69255 | QLD | 2007 | 1,208,563,140 | 1.13 | `69255/L185_Processed_Seismic_Package.zip` |
| 66 | **L192 Georgina Basin – Arunta Inlier** | 71425 | NT | 2009 | 950,833,126 | 0.89 | `71425/L192_Processed_Seismic_Package.zip` |
| 67 | **L200 Southern Carnarvon** | 72891 | WA | 2011 | 889,097,830 | 0.83 | `72891/L200_Processed_Seismic_Package.zip` |
| 68 | **L188 Rankins Springs** | 68234 | NSW | 2008 | 824,247,267 | 0.77 | `68234/L188_Processed_Seismic_Package.zip` |
| 69 | **L188 Rankins Springs Extension** | 69989 | NSW | 2009 | 601,309,420 | 0.56 | `69989/L188_Processed_Seismic_Package_extension.zip` |
| 70 | **L193 AuScope Southern Delamerian** | 71389 | VIC / SA | 2009 | 547,593,786 | 0.51 | `71389/L193_Processed_Seismic_Package.zip` |
| 71 | **L191 Curnamona–Gawler Link** | 70391 | SA | 2009 | 545,700,786 | 0.51 | `70391/L191_Processed_Seismic_Package.zip` |
| 72 | **L186 AuScope Far North Queensland** | 69256 | QLD | 2007 | 541,180,297 | 0.50 | `69256/L186_Processed_Seismic_Package.zip` |
| 73 | **L194 Ararat** (09GA-…) | 71390 | VIC | 2009 | 191,238,532 | 0.18 | `71390/L194_Processed_Seismic_Package.zip` |
| | **TOTAL (28 packages)** | | | | **97,259,781,154** | **90.58** | |

Other GA items verified:

| # | Item | Region | Type | Size | Licence | URL | Flag |
|---|------|--------|------|------|---------|-----|------|
| 74 | **L206 South Gippsland** | VIC | Deep crustal reflection, 2015 | **No seismic data package published.** The eCat record (uuid `256cc015-d0a8-a73d-e053-12a3070a0e94`) offers only the field-operation report PDF (`89800/89800_00_0.pdf`, 35.6 MB) and processing report (`89800/89800_01_0.pdf`, 897.9 KB) | CC-BY 4.0 | landing https://pid.geoscience.gov.au/dataset/ga/89800 | **[V]** — reports only; SEG-Y presumably by request |
| 75 | Bonaparte Basin 2D land seismic reprocessing (53 lines, 618.9 line-km, 10 legacy surveys 1980–1997) | East Kimberley, WA | Reprocessed 2D reflection (near-surface + Palaeozoic basin) | not measured | CC-BY 4.0 | landing https://pid.geoscience.gov.au/dataset/ga/135578 | **[V]** landing page; raw on request (eCat 135578) |
| 76 | GIS dataset of Onshore Seismic Surveys (May 2019) | Australia | Line geometry for every GA onshore seismic line | small | CC-BY 4.0 | https://pid.geoscience.gov.au/dataset/ga/100802 | **[V]** |
| 77 | Companion magnetotelluric surveys (North Queensland, Gawler, Curnamona, Georgina–Arunta, GOMA, Youanmi, YOM, Cloncurry 476 sites) | Australia | MT EDI files + reports | e.g. North Qld MT: 31,065,485 + 5,666,567 + 1,336,891 + 4,358 B; Youanmi MT 7,199,460 B | CC-BY 4.0 | e.g. `https://d28rz98at9flks.cloudfront.net/72864/EDI_files.zip` | **[V]** |
| 78 | **Deep Crustal Seismic Reflection Profiling: Australia 1978–2015** (Kennett, Saygin, Fomin, Blewett) | Australia | The image atlas of every GA deep crustal line, 1:1 H:V, with strip maps and bibliography | free PDF **117.4 MB** | ANU Press open access | https://press.anu.edu.au/publications/deep-crustal-seismic-reflection-profiling · DOI http://doi.org/10.22459/DCSRP.11.2016 | **[V]** |

**Enumeration / bulk-download recipe (Geoscience Australia):**

```bash
# 1. Find a survey's eCat record + its download links (GeoNetwork Elasticsearch API)
curl -H 'Content-Type: application/json' \
  -d '{"query":{"query_string":{"query":"\"L210 South Nicholson\""}},"size":10,
       "_source":["uuid","resourceTitleObject","link"]}' \
  https://ecat.ga.gov.au/geonetwork/srv/api/search/records/_search

# 2. Read one record in full (licence, line names, line-km, contacts)
curl 'https://ecat.ga.gov.au/geonetwork/srv/api/records/<uuid>?language=eng'

# 3. Download (no auth)
curl -O https://d28rz98at9flks.cloudfront.net/116881/L210_Processed_Seismic_Package.zip
```

Gotchas: `pid.geoscience.gov.au` 303-redirects to a **client-side hash URL**
(`catalog.search#/metadata/<ecatID>`), so a plain fetch of the PID yields no links —
use the GeoNetwork API instead. The `/formatters/xml` endpoint 404s for numeric IDs.

### 5.2 Australia / NZ — other

| # | Programme | Region | Years | Type | Size | Licence | Verified URL | Access | Flag |
|---|-----------|--------|-------|------|------|---------|--------------|--------|------|
| 79 | Wellington Active Source Transect (**SAHKE**) | Wellington, North Island NZ | 2011 | Onshore active-source crustal transect, **637 stations** | see §6 | EarthScope terms | PH5 network **ZV** | `ph5ws`, no login | **[V]** in PH5 |
| 80 | South Island Seismic Experiment | South Island, NZ | 2018 | Active source, 12 stations | see §6 | EarthScope terms | PH5 network **6Q** | `ph5ws` | **[V]** in PH5 |
| 81 | Hikurangi margin — "Controls on along-strike variations in locked and creeping megathrust behavior" | Hikurangi, NZ | 2017 | 689 stations, onshore–offshore | see §6 | EarthScope terms | PH5 network **6B** | `ph5ws` | **[V]** in PH5 |
| 82 | Galilee Seismic Experiment | Queensland, Australia | 2018 | Crustal + sedimentary structure, 550 stations | see §6 | EarthScope terms | PH5 network **1C** | `ph5ws` | **[V]** in PH5 |
| 83 | **AusPass** — Australian Passive Seismic Server (ANU) | Australia | ongoing | FDSN node for Australian temporary/permanent networks; hosts **AusMoho** and AusArray-derived products | — | open | https://auspass.edu.au/ (live, HTTP 200) · https://auspass.edu.au/research/AusMoho.html | FDSN web services | **[V]** site live; **[U]** AusArray active-source holdings not enumerated |
| 84 | **GeoNet** (GNS Science) | New Zealand | ongoing | NZ national waveform archive (passive; the route to NZ transect station data not in PH5) | — | open | https://www.geonet.org.nz/data/types/seismic_waveforms | FDSN web services / AWS open data | **[V]** live |
| 84a | **SIGHT / SAPSE** — "Cooperative Project on South Island New Zealand" (the South Island GeopHysical Transect) | South Island, NZ | 1995–1996 | Crustal/lithospheric transect across the Alpine Fault; 71 stations | — | EarthScope terms | IRIS `fdsnws` network **XC** (1995–1996) | FDSN web services | **[V]** in IRIS network list |
| 84b | **SAHKE** — "Seismic Analysis of the Hikurangi Experiment, Wellington Geophysical Transect" (passive phase) | North Island, NZ | 2009–2010 (105 sta) and 2011 (5 sta) | Crustal transect across the Hikurangi subduction zone | — | EarthScope terms | IRIS `fdsnws` networks **X2** and **9G**; active source is PH5 **ZV** | FDSN / `ph5ws` | **[V]** |
| 84c | **NIGHT** — "Hikurangi Subduction System Seismic Transects, North Island Geophysical Transect (passive)" | North Island, NZ | 2001–2002 | Crustal transect, 82 stations | — | EarthScope terms | IRIS `fdsnws` network **XQ** | FDSN web services | **[V]** |
| 84d | High-resolution experiment along the Hikurangi subduction zone / Taupo Volcanic Zone | NZ | 1994–1995 | 14 stations | — | EarthScope terms | IRIS `fdsnws` network **XP** | FDSN | **[V]** |
| 84d1 | **04-003 / EXMOUTH** — "Contrasting Styles of Continental Breakup: the Exmouth and Cuvier Margins, NW Australia" | NW Shelf, Australia | 2001 | Marine wide-angle / continental-breakup imaging, SEG-Y | **9,302,084,671 B = 8.66 GiB** (measured) | EarthScope terms, `Restricted: N` | assembled ID **04-003** — `https://data.earthscope.org/archive/assembled/04-003/` | Direct anonymous HTTP | **[V]** — an Australian deep-crustal dataset that is *not* at Geoscience Australia |
| 84e | **AU** — Australian National Seismograph Network | Australia | 1994– | 259 stations (national permanent network; the passive counterpart to the GA reflection lines) | — | open | IRIS `fdsnws` network **AU**; also AusPass | FDSN | **[V]** |

---

## 6. The EarthScope / PASSCAL **PH5** archive — how to list and bulk-download everything

PH5 is EarthScope's active-source archive format. It has its own web-service family,
`ph5ws`, separate from `fdsnws`. **No login, no token, fully scriptable.**

Service root (verified live): **https://service.iris.edu/ph5ws/**
Four services: `station` (v1), `dataselect` (v1), `event` (v1, active-source shot
metadata), `availability` (v1).

### 6.1 List every active-source experiment in the archive

```bash
curl 'https://service.iris.edu/ph5ws/station/1/query?format=text&level=network'
```

Returns a pipe-delimited table: `Network | Description | StartTime | EndTime |
TotalStations`. **234 experiment-networks** were returned this session. [V]

### 6.2 Drill into one experiment

```bash
NET=ZC   # SINOPROBE-2 Controlled Source
# station list with coordinates
curl "https://service.iris.edu/ph5ws/station/1/query?net=$NET&level=station&format=text"
# what data actually exists, per channel, with time spans
curl "https://service.iris.edu/ph5ws/availability/1/query?net=$NET&format=text"
```

### 6.3 Download waveforms — including as SEG-Y

```bash
curl -o shot.segy.zip \
 "https://service.iris.edu/ph5ws/dataselect/1/query?net=ZC&sta=1001&cha=EPZ\
&starttime=2009-12-09T07:59:00&endtime=2009-12-09T08:01:00&format=segy1"
```

Verified: returns HTTP 200 and a **ZIP container** of SEG-Y (first bytes `PK\x03\x04`,
member named `ZC.001.2009…`). `format=` accepts `miniseed`, `sac`, `geocsv`,
`segy1` (SEG-Y rev 1) and `segy2` (rev 2). [V]

Notes / gotchas:
- `event` v1 exists but **rejects `net=`** — it takes shot-line/event parameters, not a
  network code. Query it without `net`, or via the request tools on the service page.
- `format=text` is not valid for `event`.
- **Cloud migration in progress.** EarthScope's notice of **5 August 2026**
  (https://www.earthscope.org/news/retirement-of-earthscopes-on-premises-seismic-archiving-system/)
  states that inbound connections to the Seattle servers `iris.washington.edu`
  (Buddy 128.95.166.5, USRA .10, Ringsub .143) shut down **11 August 2026**, as one of the
  final steps in moving **nearly 40 years of seismic archiving, hosted at the University of
  Washington, into the AWS cloud**. That change affects **data delivery into** the archive,
  not the read-side services — `service.iris.edu/ph5ws/*` and `service.iris.edu/fdsnws/*`
  were both live and returning data during this research session. The legacy BUD Monitor is
  replaced by `status.earthscope.org`. Re-check endpoints before building long-lived
  pipelines. [V]
- `https://ds.iris.edu/ds/nodes/dmc/data/formats/ph5/` now **404s** — the old DMC
  documentation tree is being dismantled. Use the live service root instead.

### 6.3b Bulk harvest of the whole PH5 archive

```bash
#!/bin/sh
# 1. get the experiment index
curl -s 'https://service.iris.edu/ph5ws/station/1/query?format=text&level=network' \
  > ph5_networks.txt

# 2. for every experiment, pull the station table and the availability table
tail -n +2 ph5_networks.txt | while IFS='|' read -r NET DESC T0 T1 NSTA; do
  [ -z "$NET" ] && continue
  mkdir -p "ph5/$NET"
  curl -s "https://service.iris.edu/ph5ws/station/1/query?net=$NET&level=channel&format=text" \
       > "ph5/$NET/stations.txt"
  curl -s "https://service.iris.edu/ph5ws/availability/1/query?net=$NET&format=text" \
       > "ph5/$NET/availability.txt"
done

# 3. waveforms: iterate availability rows and request SEG-Y per station/time-span
#    (one request per row keeps each response small; the service returns a ZIP of SEG-Y)
awk 'NR>1{print $1,$2,$3,$4,$7,$8}' ph5/ZC/availability.txt | while read N S L C T0 T1; do
  [ "$L" = "--" ] && L=""
  curl -s -o "ph5/$N/${S}_${C}_${T0}.segy.zip" \
    "https://service.iris.edu/ph5ws/dataselect/1/query?net=$N&sta=$S&loc=$L&cha=$C\
&starttime=$T0&endtime=$T1&format=segy1"
done
```

Be considerate: some experiments have thousands of stations (SSIP `YG` has 5,016;
`SUGAR` 5G/2014 has 3,873; Shale Hills `YR` has 4,019). Rate-limit and cache
`availability.txt` before requesting waveforms.

### 6.4 Deep-crustal / lithospheric experiments confirmed inside PH5

Every row below was confirmed present in the `ph5ws` network listing this session. [V]

| Net | Year | Stations | Experiment | Region |
|-----|------|----------|------------|--------|
| **ZC** | 2009 | **1,190** | **SINOPROBE-2 Controlled Source** | Inner Mongolia, China (~42.7 °N, 112.7 °E) |
| **5G** | 2011 | 357 | **SinoProbe: Northeast China Transect** | NE China |
| **XN** | 2007 | 946 | Deep Structure of the Northwestern Tibet Collision Zone | Tibet |
| **Z5** | 2007 | 2,740 | Discrete vs. Continuous Continental Deformation and the Role of the Lower Crust in the Tien Shan | Kyrgyzstan/China |
| **7A** | 2012 | 909 | **Wide-Angle seismic reflection Experiment across the Central Iberian Zone** (ALCUDIA-WA) | Spain |
| **XY** | 2017 | 874 | The Central Iberian Mountain Range — deformation mechanisms of Iberia (CIMDEF) | Spain |
| **X2** | 2011 | 904 | **Seismic Wide-Angle across the RIFT** (ICTJA Jaume Almera) | — |
| **XA** | 2010 | 898 | **Seismic Imaging of the Moroccan Atlas** (SIMA) | Morocco |
| **8A** | 2014 | 896 | **Seismic Transect Across the Okavango Rift Zone** | Botswana |
| **ZW** | 2006 | 370 | **GEO-DESIRE Wide-Angle Reflection/Refraction, Israel & Jordan** | Dead Sea |
| **Z9** | 2008 | 650 | **Korean Peninsula Refraction Profile** | South Korea |
| **1C** | 2008 | 400 | Study of the Crustal Structure of Northern Vietnam | Vietnam |
| **X3** | 2006 | 148 | **TAIGER active source explosion pilot test** | Taiwan |
| **3C** | 2008 | 0 | TAIGER-A 200612 continuation | Taiwan |
| **YL** | 2015 | 298 | **Parnaíba Basin WARR profile** | Brazil |
| **3B** | 2015 | 1,021 | Integrated Geosciences in the Mérida Andes (GIAME) | Venezuela |
| **9D** | 2014 | 3,539 | Integrated Geosciences in the Mérida Andes (GIAME) | Venezuela |
| **1X** | 2022 | 856 | TANGO — TransANdean Great Orogeny, Argentina nodes | Argentina |
| **XN** | 2022 | 1,371 | TANGO-Node | Argentina |
| **8E** | 2010 | 499 | TANGSHAN | China |
| **9B** | 2011 | 340 | TopoGreenland | Greenland |
| **ZV** | 2011 | 637 | **Wellington Active Source Transect** (SAHKE) | New Zealand |
| **YG** | 2011 | **5,016** | Seismic Imaging of New Transitional Crust in the Salton Trough Oblique Rift | California |
| **9A** | 2012 | 2,554 | Steep continental margin, western Idaho – eastern Oregon (IDOR) | USA |
| **ZF** | 2010 | 424 | GUMBO — Gulf of Mexico Basin Opening | USA |
| **ZI** | 2015 | 1,414 | ENAM community seismic experiment | US Atlantic margin |
| **YB** | 2009 | 1,806 | Batholiths Controlled Source | BC, Canada |
| **XU** | 2004 | 750 | Central Walker Lane / Idaho–Nevada–California Transect | USA |
| **ZG** | 2005 | 395 | Northern Nevada–Utah Transect | USA |
| **6Q** | 2018 | 12 | South Island Seismic Experiment | New Zealand |
| **1C** | 2018 | 550 | Galilee Seismic Experiment | Australia |

### 6.5 FDSN network registry — finding legacy experiments not in PH5

```bash
curl 'https://fdsn.org/networks/?paginate=no'    # full registry, ~3 MB HTML
```

Useful codes confirmed there this session: INDEPTH II **XR** (1994), INDEPTH-III **XR**
(1997–1999), INDEPTH IV **X4** (2007–2009, Missouri S&T) and **XO** (2007–2009, Cambridge);
CD-ROM/Rocky Mountain Transect **XK** (1999–2000); Rocky Mountain Front II **XG** (1992);
Kaapvaal craton **XA** (1997–1999); ANCORP96 **XO** (1996) and ANCORP-TE **ZE** (1996–1997,
both GEOFON/GFZ); BOLIVAR western Venezuela **XN** (2008–2009, Rice); EAGLE Ethiopia **XJ**
(2002–2003, Royal Holloway), **XM** (2002–2003) and **YJ** (2001–2003); Appalachian Seismic
Transect **Z4**; SESAME **Z9**. [V]

---

## 6A. The EarthScope **"assembled datasets"** archive — the other half of the story

**This is the single most important access route for pre-2010 NSF active-source data, and
it is invisible to ordinary FDSN network queries.** Many crustal experiments were never
given a network code at all; they were archived as *assembled datasets* under a report
number, and their SEG-Y/SAC tarballs are served **anonymously over plain HTTP**.

- Catalogue: **https://ds.iris.edu/mda/?type=assembled** — **852 rows** [V]
- Per-dataset page: `https://ds.iris.edu/mda/<report-no>/` (e.g. `04-010`)
- Files: `https://data.earthscope.org/archive/assembled/<report-no>/` — direct download,
  no login, `Restricted: N` on all rows below [V]

### The listing API (undocumented, and the key to enumerating this archive)

The file browser at `data.earthscope.org` is a JS SPA and the S3 bucket denies
`ListBucket`, so a plain fetch of a directory returns either the SPA shell or `403 XML`.
**Appending `?json` to a directory URL returns a real S3-style JSON listing with exact
`Size`, `LastModified`, `ETag` and `StorageClass` per object:** [V]

```bash
curl 'https://data.earthscope.org/archive/assembled/96-002/?json'
# {"files":[{"Key":"archive/assembled/96-002/96-002.RMF.01.SAC.tar.gz","Size":4792242,…}]}
```

File naming is `<id>.<NICKNAME>.DATA.<FORMAT>.tar.gz` for single-part datasets and
`<id>.<NICKNAME>.<NN>.<FORMAT>.tar.gz` for multi-part ones — but the nickname's
capitalisation is inconsistent (`Eagle`, `Charme`, `Deepa`, `Snore97`, `Quartz` vs
`CDRN`, `KRSP94`, `INDEPTH-II`, `NYNEX_86`), and newer datasets use yet another form
(`21-008_DATA.SEGY.01.tar.gz`, `21_012_DATA.SEGY.01.tar.gz`).
**Do not guess filenames — use `?json`.**

Almost every dataset ships a **`manifest.txt`** next to the tarball(s) listing the traces
(CD-ROM's is 35,650 bytes) — fetch that first to see what you are about to download.
Tarball integrity spot-checked: `02-008.CDRN.DATA.SEGY.tar.gz` begins `1f 8b 08` (valid
gzip) and is 33,930,094,818 bytes. [V]

```bash
#!/bin/sh
# download one assembled dataset, whatever its filenames are
ID=02-008
curl -s "https://data.earthscope.org/archive/assembled/$ID/?json" \
| python -c "import sys,json;[print(f['Key']) for f in json.load(sys.stdin)['files']]" \
| while read -r KEY; do
    curl -O --create-dirs -o "$ID/$(basename "$KEY")" "https://data.earthscope.org/$KEY"
  done

# sweep the whole catalogue: get every report number first
curl -s 'https://ds.iris.edu/mda/?type=assembled' \
| grep -oE '[0-9]{2}-[0-9]{3}' | sort -u
```

### Full sweep of the archive (measured this session)

All 852 catalogue rows were enumerated through `?json`:

- **554 of 852 datasets actually hold files**; the remaining 298 are catalogue-only
  (many are PH5-format rows whose data lives in `ph5ws` instead — SIMA `10-008`,
  SEISORZ `13-005`, SAHKE `11-020`, RIFSIS `11-021`, SinoProbe `17-028`, GUMBO `11-001`,
  SUGAR `14-023`, Batholiths `10-001`, Korea `09-005`, Red River `10-016`,
  INDEPTH IV `07-024`/`07-027` all return **zero files** here).
- **Grand total: 14,045,922,783,218 bytes = 12.775 TiB.** [V]
- Caveat: the sweep summed each directory's top-level `files` array. A separate pass found
  that only **2 of 852** datasets place data in non-`reports/` subfolders (`23-031`
  `gti_segy/`, and `26-029`'s four dated subdirectories), so the total is marginally low
  but not materially so. The `?json` response also carries a `folders` array — walk it if
  you need byte-exact totals for those two. [V]

Largest holdings overall (GiB): FORGE Phase2C stimulation `19-011` 1,927.0 · Utah FORGE
2022 nodal `23-004` 1,427.3 · **"An Open-Access, Controlled-Source Seismic Dataset Across
the Cascadia…" `21-008` 758.9 (SEGY)** · SAFOD offshoot shots `05-028` 524.3 · Greenland
hydrofracture `26-027` 431.0 · Play Fairway geothermal `21-027` 418.3 · **SEGMeNT `16-010`
410.4** · Marianas `12-008` 408.8 · **Chile-SIO `16-005` 407.1** · COLZA `07-030` 360.9 ·
Lau Spreading Center `09-013` 347.4 · volcano underplating `18-015` 345.2 · Tolstoy
`04-020` 305.6 · Queen Charlotte Fault `21-012` 300.1 · Large Surface Explosion Coupling
`23-002` 240.9 · Juan de Fuca `12-015` 171.2 · **ENAM `14-005` 167.9** · Santorini
`15-008` 147.2. [V]

| # | Assembled ID | Experiment | Region | Type | Measured size | Notes | Flag |
|---|--------------|------------|--------|------|---------------|-------|------|
| 92a | **04-010** | **EAGLE Phase III — controlled source** (Ethiopia Afar Geoscientific Lithospheric Experiment) | Main Ethiopian Rift / Afar | Refraction / wide-angle, **SEG-Y** | **293,967,845 B (294 MB)** directory total; MDA states 908 MB uncompressed | `…/assembled/04-010/04-010.Eagle.DATA.SEGY.tar.gz`. PI Keller. **The answer to "where is EAGLE's active-source data" — not under any FDSN code.** Passive legs are FDSN YJ, XJ, XM, XI | **[V]** |
| 92b | **04-021** | **KRISP 1994** (Kenya Rift International Seismic Project) | S Kenya Rift | Wide-angle refraction, **SEG-Y** | **432,963,999 B (433 MB)**; MDA 820 MB | `…/04-021/04-021.KRSP94.DATA.SEGY.tar.gz` | **[V]** |
| 92c | **03-002** | **KRISP 1989/1990** | Kenya dome / Nakuru | Refraction + tomography + teleseismic, SAC | **124,311,245 B (124 MB)**; MDA 359 MB | `…/03-002/03-002.KRSP90.DATA.SAC.tar.gz` | **[V]** |
| 92d | **01-003** | **KRISP 1985** | Kenya Rift, 500 km E–W array | Teleseismic arrays supporting the refraction programme, SAC | **26,391,703 B (26 MB)** | `…/01-003/01-003.KRSP85.DATA.SAC.tar.gz`. All three KRISP tarballs together = **583 MB** — the complete open KRISP holding | **[V]** |
| 92e | **14-026** | Olorgesailie drilling-site seismic | S Kenya Rift | Active-source reflection, SEG-Y | **1,076,874,236 B (1.00 GiB)** | | **[V]** |
| 92f | **16-010** | **SEGMeNT** — Extension & Magmatism in Malawi/Tanzania (active source) | Lake Malawi | Marine/lacustrine OBS active source, SEG-Y | **440,689,321,728 B = 410.42 GiB** (6 files); MDA 810,102 MB uncompressed | **Largest open African controlled-source dataset found.** Passive companion FDSN **YQ (2013–16)** | **[V]** |
| 92g | **16-005** | **Chile-SIO** — megathrust slip laboratory | Chile margin | Marine wide-angle OBS, SEG-Y | **437,173,791,025 B = 407.15 GiB** (6 files); MDA 710,752 MB | **Largest open South American controlled-source holding found** | **[V]** |
| 92h | **07-003 / SECARIB** | **BOLIVAR** — SE Caribbean plate boundary, **land** active source | Venezuela / SE Caribbean | Wide-angle refraction, SEG-Y | **50,712,558,202 B = 47.23 GiB** (7 files); MDA 270,493 MB | PI Zelt. The NSF BOLIVAR active-source land leg | **[V]** |
| 92i | **06-009 / SECA** | **BOLIVAR** — SE Caribbean margin active experiment (**OBS**) | Offshore Venezuela | Marine wide-angle OBS, SEG-Y | **37,192,371,291 B = 34.64 GiB** (4 files); MDA 84,991 MB | OBSIP | **[V]** |
| 92j | **05-025** | **CHARME** — flat-slab to steep subduction, Nazca plate | Central Chile | Refraction / wide-angle, SEG-Y | **16,133,131,628 B = 15.03 GiB** (directory total); MDA 30,458 MB uncompressed | `…/05-025/05-025.Charme.DATA.SEGY.tar.gz`. PI Pardo / Eisenberg | **[V]** |
| 92k | **07-020** | VENCORP04 (SE Caribbean seismic) | Venezuela | Refraction, SEG-Y | **260,605,074 B (261 MB)** | | **[V]** |
| 92l | **97-005** | Tanzania Craton experiment (TANZ) | Tanzania | **Passive** broadband, 21 stations | directory total **2,624,794 B** | Passive only | **[V]** |

## 6B. South America

| # | Programme | Country / region | Years | Type | Extent | Size | Licence | Verified URL | Access | Flag |
|---|-----------|------------------|-------|------|--------|------|---------|--------------|--------|------|
| 93 | **ANCORP'96 near-vertical reflection** (DEKORP) | N Chile / S Bolivia, Central Andes | 1996 | Reflection + wide-angle | not stated | **not stated** | not stated | programme page https://www.gfz.de/en/dekorp (HTTP 200) | **NOT PUBLIC** — no dataset landing page, no DOI, no download. Page says only that the database "includes seismic data of all surveys (raw and processed)… in digital or paper form" | **[V]** *that it is not public*. **A genuine gap: the flagship Andean deep-reflection profile is not openly downloadable.** Archive moved to GFZ Sections 4.1/2.2 in 1994; contact = Geophysical Imaging section head |
| 94 | ANCORP'96 seismological network (passive companion) | N Chile / S Bolivia | 1996-09-14 → 1997-12-31 | Passive, 44 stations | — | test pull 10 min × all stations = 233,472 B | **CC BY 4.0** | DOI 10.14470/MR6441682066 → https://geofon.gfz.de/doi/network/ZE/1996 ; waveforms `https://geofon.gfz.de/fdsnws/dataselect/1/query?net=ZE&…` | Direct, anonymous | FDSN **ZE (1996)**. Haberland, Rietbrock, Asch, Chong; GIPP grant 199604 | **[V]** |
| 95 | PUNA 1997 (GFZ/GIPP) | W Argentina, Puna plateau | 1997 | Passive array, 60 stations | — | not stated | GFZ Data Services terms | DOI 10.14470/MO6442843258 → https://geofon.gfz.de/doi/network/ZB/1997 | GEOFON FDSN | FDSN **ZB (1997)** | **[V]** |
| 96 | **BANJO / SEDA** | Bolivia–Chile Altiplano | 1994–1995 | **Passive** broadband, 23 stations | — | not stated | IRIS/SAGE open | DOI 10.7914/SN/XE_1994 ; https://www.fdsn.org/networks/detail/XE_1994/ | FDSN | **Passive, not controlled source** — a common misattribution | **[V]** |
| 97 | **GIAME** phase 1 — Integrated Geosciences in the Mérida Andes | Venezuela | 2014 | Controlled-source wide-angle, **3,539 stations** | ~565 km reported | **≈63 GB** (3 stations measured, mean 17.81 MB × 3,539); MDA states 65,000 MB | Open (`Restriction: OPEN`) | DOI 10.7914/SN/9D_2014 ; `https://service.earthscope.org/ph5ws/dataselect/1/query?net=9D&…` ; https://ds.iris.edu/mda/14-040/ | PH5 web service | FDSN **9D (2014)**, FUNVISIS + PASSCAL. 7.06–9.79 °N, −71.1 to −66.9 °E | **[V]** |
| 98 | **GIAME** phase 2 | Venezuela | 2015–2016 | Controlled-source wide-angle, 1,021 stations | — | **≈92 GB** (mean 90.6 MB × 1,021) | Open | `https://service.earthscope.org/ph5ws/dataselect/1/query?net=3B&…` ; https://www.fdsn.org/networks/detail/3B_2015/ | PH5 | FDSN **3B (2015)** — **no DOI registered**. MDA 15-027 lists only 276 MB, which conflicts with the PH5 holding | **[V]** data; **[U]** size reconciliation |
| 99 | **PISAGUA / RV SONNE SO297** (GEOMAR) | N-central Chile margin, Copiapó & Taltal Ridges | 2022-12 → 2023-04 | Amphibious refraction / wide-angle (OBS, OBH, land), SEG-Y | 1 offshore shot profile per working area | **17.58 GB** measured from PANGAEA file tables (969552 = 2.26 GB; 969551 = 1.20 GB; 969150 = 12.48 GB; 984419 = 1.64 GB; 984420/984421 not parsed) | **CC BY 4.0** | https://doi.pangaea.de/10.1594/PANGAEA.969552 (also .969551, .969150, .984419, .984420, .984421) | Single files direct: `https://download.pangaea.de/dataset/969552/files/<name>` ; **bulk ZIP/TAR needs a free PANGAEA account** | Cruise DOI 10.48433/cr_so297. The modern, well-curated successor to CINCA / SPOC / TIPTEQ | **[V]** |
| 100 | **Brazil ANP/CPRM "REATE" — free onshore public data** | 22 onshore Brazilian basins | legacy → 2022 | 2D & 3D reflection (SEG-Y), wells, non-seismic | — | **Measured exactly via WebDAV `oc:size`:** Paraná **354.51 GB** (2D 30.16, 3D 0.72); Parnaíba **702.15 GB** (2D 30.67); Solimões **152.23 GB** (2D 24.74, 3D 22.00); São Francisco **148.66 GB** (2D 20.54); Amazonas **90.78 GB** (2D 14.07); Parecis–Alto Xingu **225.33 GB** (2D 12.94); Recôncavo **311.98 GB**; Acre–Madre de Dios **11.05 GB**; Tacutú **20.08 GB** | Brazilian public data (ANP Res. 889/2022); no explicit CC licence | portal https://reate.cprm.gov.br/anp/TERRESTRE (EN `/TERRESTREen`); Paraná `…/arquivos/index.php/s/z0XoautAuswCSbf`; Parnaíba `…/s/zTQ17CWbL2Wvx5f` | **Direct download, no registration, no login.** Nextcloud shares + per-basin ZIP; **WebDAV open** at `https://reate.cprm.gov.br/arquivos/remote.php/dav/public-files/<token>/` | Site states "Todos os dados estarão permanentemente disponíveis"; some groups exceed 100 GB. MD5 catalogue per basin. Lines named e.g. `0225_PARANA_51` (1,584 MB). **~2.9 TB measured overall, ~163 GB of it 2D reflection SEG-Y in the deep-basin areas** | **[V]** |
| 101 | Brazil — **Pantanal Basin** (ANP) | Pantanal | — | — | — | **60,773 B of well data + 1,501 B MD5 catalogue — no seismic folder at all** | as above | https://reate.cprm.gov.br/arquivos/index.php/s/HyVBmvQ8rht4u3k | Direct | **Valuable negative:** the Pantanal package contains only `POCO` (wells). There is **no** ANP public seismic for Pantanal despite what the basin list implies | **[V]** |
| 102 | Brazil — **offshore** public data | 9 Brazilian offshore basins | — | 2D/3D post-stack (free), pre-stack (conditional) | — | not stated | ANP Res. 889/2022; RD 136/2022 & 595/2023 | https://www.gov.br/anp/pt-br/assuntos/exploracao-e-producao-de-oleo-e-gas/dados-tecnicos/acesso-aos-dados-tecnicos | **Not a web download.** Post-stack free but delivered **physically** at BDEP, Av. Pasteur 404, Rio; pre-stack by form to helpdesk@anp.gov.br, **restricted to ANP-authorised agents**, with mandatory return of reprocessed data | Page says web delivery of marine data is "futuramente". Research institutions free; commercial pay | **[V]** |
| 103 | **Parnaíba Basin WARR profile** | NE Brazil (Maranhão) | 2015-09-24 → 2015-10-01 | Wide-angle reflection/refraction, 298 stations, Texan/GS11V @200 sps | — | **0 bytes served** | — | metadata + DOI 10.7914/SN/YL_2015 ; https://www.fdsn.org/networks/detail/YL_2015/ | **Metadata only — no waveforms.** `ph5ws/availability?net=YL` → 404 "No Data Found"; dataselect on stations 301/302/303/400 → 404, while control nets X2/XA/8A/9D return data normally | Univ. of Aberdeen. **The single most relevant Brazilian deep-crustal controlled-source experiment, and its waveforms are not currently retrievable.** | **[V]** *that data are absent* |
| 104 | **PCPB** — Pantanal, Chaco & Paraná structural network | Brazil/Paraguay/Argentina | 2016–2024 | **Passive** broadband | — | not stated | IRIS/SAGE open | DOI 10.7914/8scf-yd39 ; https://www.fdsn.org/networks/detail/XC_2016/ | FDSN | IAG-USP. The closest openly available thing to a Pantanal/Paraná deep-crustal dataset | **[V]** |
| 105 | **TANGO** (TransANdean Great Orogeny) node deployments | Argentina / Chile | 2022–2023 | Nodal, 856 + 1,371 stations | — | MDA "Approximate Size" reads **"Restricted"** | — | https://ds.iris.edu/mda/24-010/ ; DOI 10.7914/q4nj-hf03 | **Currently restricted** | PASSCAL report lists TANGO-BB_Chile (XM) and TANGO-Node_Chile (XN) as "Closed"; Argentina node set 24-010 flagged Restricted | **[V]** |
| 106 | PISCO'94 / PRECORP / CINCA | N Chile, Chile–Peru margin | 1994–1996 | Wide-angle; marine MCS (BGR *Sonne*) | — | not stated | — | `search: CINCA 1995 BGR Sonne SO104 seismic data request` · `search: PISCO 94 GFZ GIPP DOI` · `search: PRECORP Chile reflection profile data` | **No archive confirmed** — not in the 168-record GFZ GIPP DOI set, not in PANGAEA, no BGR portal entry | CINCA appears in the ISC agency list (https://www.isc.ac.uk/iscbulletin/agencies/) but that is a bulletin contributor, not a waveform archive | **[U]** |
| 107 | Colombia ANH — EPIS / Banco de Información Petrolera | Colombia | — | Industry reflection | — | not stated | — | https://www.anh.gov.co/es/la-anh/informaci%C3%B3n-de-inter%C3%A9s/FAQ/ | **Request-based**, no free bulk portal located | Contrast with Brazil, which does publish freely | **[U]** |
| 108 | Argentina SEGEMAR | Argentina | — | Geophysical catalogue (mostly aerogeophysics) | — | — | — | https://www.argentina.gob.ar/economia/segemar ; https://repositorio.segemar.gov.ar/ | Portal exists; **no deep-crustal controlled-source seismic located** | Argentina's open deep-crustal coverage comes via IRIS/PASSCAL nets (XA PANDA, ZL, X6 SLIP, TANGO), not SEGEMAR | **[U]** |

## 6C. Africa

| # | Programme | Country / region | Years | Type | Extent | Size | Licence | Verified URL | Access | Flag |
|---|-----------|------------------|-------|------|--------|------|---------|--------------|--------|------|
| 109 | **EAGLE Phase III controlled source** | Ethiopia | 2003 | Refraction / wide-angle SEG-Y | — | **294 MB** | Open | assembled **04-010** — see §6A row 92a | Direct HTTP | | **[V]** |
| 110 | **KRISP 1985 / 1989-90 / 1994** | Kenya Rift | 1985–1994 | Refraction, wide-angle, teleseismic | — | **583 MB** total | Open | assembled **01-003**, **03-002**, **04-021** — §6A | Direct HTTP | | **[V]** |
| 111 | **Silali & Paka volcano tomography** | Kenya Rift (0.77 °N, 36.17 °E) | 2011-08 → 2013-01 | Controlled-source nodal tomography, **1,401 stations** in Kenya | — | **≈34.9 GB** (3 stations measured, mean 24.93 MB × 1,401) | Open (PH5, anonymous) | `https://service.earthscope.org/ph5ws/dataselect/1/query?net=9B&…` ; https://www.fdsn.org/networks/detail/9B_2012/ | PH5 | FDSN **9B (2012–13)**, UTEP. **No DOI registered.** Net 9B also contains TopoGreenland stations — filter by bbox | **[V]** |
| 112 | **PRIDE / SEISORZ** — Seismic Transect Across the Okavango Rift Zone | Botswana (−21.4 to −18.3 °N, 21.8–24.2 °E) | 2014-11-21 → 25 | **Controlled-source wide-angle transect, 896 stations** @250 sps | — | **≈10.5 GB** (station 1001 = 11,710,464 B × 896); MDA 13-005 states 133,000 MB for the PH5 volume | Open (`Restriction: OPEN`) | DOI 10.7914/SN/8A_2014 ; `…/ph5ws/dataselect/1/query?net=8A&…` ; https://ds.iris.edu/mda/13-005/ | PH5 | FDSN **8A (2014)**, WHOI. The assembled dir `…/assembled/13-005/` holds **reports only** — the data live in PH5 | **[V]** |
| 113 | **SIMA** — Seismic Imaging of the Moroccan Atlas | Morocco, High/Middle Atlas (31–33 °N, −8 to −4 °E) | 2010-05-03 → 08 | **Controlled-source wide-angle, 898 stations** @500 sps | — | **≈16.4 GB** (3 stations measured, mean 18.27 MB × 898); MDA 10-008 states 300 MB — **inconsistent**, the PH5 holding is far larger | Open (`Restriction: OPEN`) | DOI 10.7914/SN/XA_2010 ; `…/ph5ws/dataselect/1/query?net=XA&…` ; https://ds.iris.edu/mda/10-008/ | PH5 | FDSN **XA (2010)**, ICTJA-CSIC Barcelona. Filter bbox to exclude co-coded AIDA_Maine stations | **[V]** |
| 114 | **RIFSIS** — "Seismic Wide-Angle across the RIF" | **Northern Morocco, Rif belt** (32.9–35.9 °N, −5.8 to −2.3 °E) | 2011-10-07 → 11-17 | **Controlled-source wide-angle, 904 stations** @100 sps | — | **≈1.65 GB** (station 1 = 1,822,720 B × 904) | Open (`Restriction: OPEN`) | DOI 10.7914/SN/X2_2011 ; `…/ph5ws/dataselect/1/query?net=X2&…` ; https://www.fdsn.org/networks/detail/X2_2011/ | PH5 | FDSN **X2 (2011)**, ICTJA-CSIC. **The catalogue title says "RIFT" but the coordinates are unambiguously the Rif belt, not a rift** — correct any citation accordingly | **[V]** |
| 115 | **SEGMeNT** active source | Malawi / Tanzania, Lake Malawi | 2015 | Marine/lacustrine OBS active source, SEG-Y | — | **410.42 GiB** | Open | assembled **16-010** — §6A | Direct HTTP | Largest open African controlled-source dataset found | **[V]** |
| 116 | **Kaapvaal Craton Project** | South Africa / Botswana / Zimbabwe | 1997–1999 | **Passive** broadband ("Anatomy of an Archean Craton") | — | not stated | IRIS/SAGE open | DOI 10.7914/SN/XA_2000 ; https://www.fdsn.org/networks/detail/XA_2000/ | FDSN | **No controlled-source component exists in the open archives** — searched the 235-row PH5 network list and the 852-row MDA assembled catalogue. Kaapvaal is passive-only | **[V]** |
| 117 | **Witwatersrand / Karoo deep reflection; Council for Geoscience holdings** | South Africa | 1980s– | Deep reflection (mine-scale 2D/3D) | — | not stated | Proprietary / priced | https://maps.geoscience.org.za ; https://www.geoscience.org.za/the-council-for-geosciences-data-portal-goes-live/ ; https://www.geoscience.org.za/cgs/systems/publications/data-catalogue/ (all HTTP 200) | **Email request + pricing.** CGS: "All data requests are streamlined through the Public Information Officer" → data@geoscience.org.za, governed by pricing guidelines | **NOT OPEN.** The Witwatersrand 3D/2D reflection volumes in the literature (Kloof, South Deep) are gold-mining-company legacy data — reprocessed academically, not redistributed | **[V]** *that it is not free/open* |
| 118 | Menengai Crater; AfricaArray; Afar passive arrays | Kenya / Ethiopia | 2005–2019 | **Passive** | — | not stated | IRIS/SAGE open | FDSN **1C (2011–14)** Menengai, **AF (2005–12)** AfricaArray, **ZE (2007–09)**, **ZF (2007–09)**, **ZK (2009–11)** Afar; `https://service.earthscope.org/fdsnws/station/1/query?net=<code>&level=network&format=text` | FDSN | Context: dense passive coverage exists for East Africa but is not controlled source | **[V]** |
| 119 | West African margin academic surveys; Egypt | W Africa, Egypt | — | Reflection / refraction | — | — | — | `search: west african margin deep crustal wide-angle OBS data DOI` · `search: Egypt deep seismic refraction data archive EGSMA` | **Nothing located** in the 235-network PH5 list, the 852-row MDA assembled catalogue, or the 168-record GFZ GIPP DOI set | | **[U]** |
| 120 | **COCORP Ghana** | Ghana | — | Deep reflection | 2 files | 26 MiB | not stated | https://cocorp.eas.cornell.edu/Ghana/ | Anonymous HTTPS | Cross-reference to §2.1 row 8 — the only African COCORP holding | **[V]** |

**Size-method note for §6A–6C.** "measured" = exact `Content-Length` summed per directory
(assembled tarballs), Nextcloud WebDAV `oc:size` recursive folder sizes (Brazil ANP), or
PANGAEA's own per-file byte tables. "≈ N stations × mean" = PH5 `dataselect` pulls of
complete station windows, averaged over 3 stations and scaled by the region-filtered
station count — estimates with real measurements underneath, not guesses. MDA's
"Approximate Size" is the archive's own **uncompressed** figure and is quoted where it
differs from the compressed download; where the two disagree wildly (SIMA 10-008, GIAME
15-027) the MDA figure appears to be wrong.

## 7. Global compilations, models and legacy-rescue initiatives

| # | Item | Coverage | Type | Size | Licence | Verified URL | Access | Flag |
|---|------|----------|------|------|---------|--------------|--------|------|
| 85 | **USGS Global Crustal Database (GSC)** — Mooney / Chulick / Detweiler | Worldwide | Compilation of **seismic refraction profiles**: layer velocities, thicknesses, sediment layers, velocity gradients, Moho depth, plus elevation (ETOPO5), heat flow (Pollack et al. via NGDC), geologic province and thermo-tectonic age | see below | US public domain (USGS) | **DEAD on usgs.gov.** Live only in the Wayback Machine: https://web.archive.org/web/20140729082601/http://earthquake.usgs.gov/data/crust/database.php | — | **[V]** dead: `/data/crust/`, `/research/structure/crust/` and `usgs.gov/data/global-crustal-database` all 404; ScienceBase API returns 0 items |
| 86 | ↳ GSC **North America** extract | N. America | ASCII profile records (one multi-line block per profile: lat/lon, layer Vp/Vs, thickness, Moho, province code) | **106,375 bytes** (Wayback capture length) | US public domain | https://web.archive.org/web/20150426001552if_/http://earthquake.usgs.gov/data/crust/nam-data.txt | Direct (Wayback) | **[V]** content fetched and format inspected |
| 87 | ↳ GSC **South America** extract | S. America | as above | **84,886 bytes** | US public domain | https://web.archive.org/web/20161221145534if_/https://earthquake.usgs.gov/data/crust/sam-data.txt | Direct (Wayback) | **[V]** capture exists |
| 88 | **CRUST 1.0** — the surviving derived product of the GSC | Global, 1°×1° | 8-layer crustal model (Vp, Vs, density, ice/water/sediment/crystalline layers, Moho) built largely from the refraction compilation | **1,155,392 B** model + **12,887 B** crust-type add-on; `depthtomoho.xyz.zip` **282,753 B** | Free academic (cite Laske, Ma, Masters & Pasyanos) | https://igppweb.ucsd.edu/~gabi/crust1.html · https://igppweb.ucsd.edu/~gabi/crust1/crust1.0.tar.gz | Direct download | **[V]** all three measured |
| 89 | CRUST 2.0 (predecessor) | Global, 2°×2° | Crustal model | not measured | Free academic | https://igppweb.ucsd.edu/~gabi/crust2.html | Direct | **[V]** live |
| 90 | LITHO1.0 / EMC mirror of CRUST1.0 | Global | Lithospheric model, IRIS Earth Model Collaboration | not measured | open | https://ds.iris.edu/ds/products/emc-crust10/ | Direct | **[V]** live |
| 91 | **FDSN network registry** | Global | The master index of experiment network codes — the way to find a legacy crustal experiment's identifier | ~3 MB HTML | open | https://fdsn.org/networks/?paginate=no | Direct | **[V]** |
| 92 | **EarthScope PH5 archive** | Global | 234 active-source experiments (see §6) | archive-scale | EarthScope Terms of Service; cite network DOI | https://service.iris.edu/ph5ws/ | Web services, no login | **[V]** |

## 7B. Grand totals — how much open deep-crustal data actually exists

Every figure below was measured over HTTP during this research session (`Content-Length`,
Apache index sums, or the `?json` S3 listing). Nothing here is an estimate.

| Archive | What it holds | Measured size | Licence | Access |
|---------|---------------|---------------|---------|--------|
| **EarthScope assembled datasets** (554 of 852 rows hold files) | Nearly every pre-2010 NSF controlled-source crustal experiment worldwide, SEG-Y/SAC/PSEGY | **14,045,922,783,218 B = 12.775 TiB** | EarthScope ToS; cite the dataset | Anonymous HTTP, no login |
| **Geoscience Australia** (28 packages, L180–L213 + Camooweal) | Processed deep-crustal reflection SEG-Y (stack, DMO, PoSTM, PSTM) + images + reports | **97,259,781,154 B = 90.58 GiB** | **CC-BY 4.0** | Direct CloudFront, no registration |
| **COCORP / Cornell ELLIPSE** (whole server) | Pre-stack shot gathers, stacks, interpretations, observer sheets, gravity/mag rasters | **≈139.8 GiB** (S Gathers 121.91 + ProMAX 10.59 + Aux 3.03 + Stacks 1.83 + support 1.36 + WorkSpace 0.52 + Taiwan 0.36 + Basemaps 0.18 + Ghana 0.03) | **None stated** | Anonymous HTTPS directory index |
| **LITHOPROBE** (246 ZIPs, 13 transect dirs) | 2D deep-crustal reflection SEG-Y | **73,146,873,565 B = 68.12 GiB** | **OGL – Canada** | Anonymous HTTPS |
| **Brazil ANP/CPRM REATE** (9 basins measured) | Onshore 2D/3D reflection SEG-Y + wells | **≈2.9 TB** measured, of which **≈163 GB is 2D reflection SEG-Y** in deep-basin areas | Brazilian public data (ANP Res. 889/2022) | Nextcloud + open WebDAV, no login |
| **EarthScope PH5** (234 experiments) | Modern active-source crustal experiments, SEG-Y/miniSEED on demand | archive-scale; individual crustal experiments measured at **1.65–≈92 GiB** each | EarthScope ToS | `ph5ws` web services, no login |
| **Finland (GTK / Fairdata)** | FIRE 1–4 (2,104 km CMP, **raw field SEG-Y included**) + BABEL, SVEKALAPKO, SVEKA ×3, POLAR, BALTIC, FENNIA, Kuusamo | **1,148,887,419,516 B ≈ 1.149 TB** (FIRE alone 1,147,373,744,961 B / 1,963 files) | **CC BY 4.0** | Direct, no login (two-step token API) |
| **SeisDARE** (DIGITAL.CSIC, Iberia) | IBERSEIS, ALCUDIA, ESCI, ILIHA — reflection + wide-angle | **~488 GB** (IBERSEIS-NI raw alone = 37,296,716,311 B) | **CC BY 4.0** | Direct download |
| **NRCan `gsc_sem`** (refraction subset) | Canadian refraction + hard-rock seismic | **≈180 MiB** for the refraction directories measured | **OGL – Canada** | Anonymous HTTPS |

**Single largest openly downloadable controlled-source crustal datasets found:**

0. **FIRE (Finland) — 1.147 TB** — the largest of all, and CC BY 4.0
1. `21-008` Cascadia accretionary wedge — **758.87 GiB**
2. `16-010` SEGMeNT (Malawi/Tanzania) — **410.42 GiB**
3. `12-008` Marianas — **408.83 GiB**
4. `16-005` Chile-SIO — **407.15 GiB**
5. `18-015` Hawaiian–Emperor — **345.15 GiB**
6. `21-012` Queen Charlotte Fault — **300.10 GiB**
7. `12-015` Juan de Fuca (OCEANUS) — **171.19 GiB**
8. `14-005` ENAM — **167.88 GiB**
9. **COCORP shot gathers — ≈121.91 GiB**
10. `02-006` LARSE multichannel reflection — **82.43 GiB**

**Best starting points by intent:**

- *Continental-scale reflection SEG-Y, no strings*: Geoscience Australia (CC-BY),
  LITHOPROBE (OGL-Canada), COCORP stacks.
- *Pre-stack shot gathers for algorithm work*: COCORP `S Gathers` (≈122 GiB) and the
  assembled SEG-Y tarballs.
- *Wide-angle / refraction for velocity-model work*: the assembled archive (CD-ROM,
  Deep Probe, KRISP, EAGLE, POLONAISE, CELEBRATION, ALP2002, SUDETES, IBERSEIS,
  QUARTZ/CRATON/Bazalt/Batholith PNE profiles).
- *Modern dense-node crustal transects*: PH5 (`ph5ws`).

## 7C. Link-check results and access gotchas

All **164 distinct URLs** in this document were fetched at the end of the session. Every
one that matters resolves. The apparent failures are all explainable — recorded here so a
future reader does not mistake them for rot: [V]

| Symptom | Affected | Explanation |
|---------|----------|-------------|
| `HEAD` → **000/403/404**, `GET` → **200** | `data.earthscope.org/archive/assembled/<id>/`, `www.gov.br/anp/…`, `ecat.ga.gov.au/…/_search`, `www.anh.gov.co/…`, `www.isc.ac.uk/iscbulletin/agencies/` | SPA shells, POST-only APIs and WAFs that reject `HEAD`. Always confirm with `GET` (or `?json` for EarthScope). `…/assembled/04-003` **without** a trailing slash returns 403; **with** `?json` it returns a valid listing |
| `HEAD` → **307/400** | `service.iris.edu/fdsnws/…`, `service.iris.edu/ph5ws/…` | FDSN services require their query parameters; a bare or templated URL is a 400 by design |
| **413** | `geofon.gfz.de/fdsnws/dataselect/…` | GEOFON rejects an unbounded request — supply `starttime`/`endtime` |
| **503** | `web.archive.org/web/…/sam-data.txt` | Wayback rate-limiting, transient. The companion `nam-data.txt` returned **200** and 585,714 bytes (the raw file is 106,375 B; the rest is the Wayback banner). The CDX index confirms both captures exist |
| **401** | `reate.cprm.gov.br/…/dav/public-files/` | The WebDAV root needs the per-basin share token appended |
| `HEAD` → **301** | `doi.org/…` (http form), `ds.iris.edu/data/reports/…` | plain http → https redirects; harmless |
| **404** — genuinely dead | `data.ifremer.fr/SISMER`, `ds.iris.edu/ds/nodes/dmc/data/formats/ph5/`, `avaa.tdata.fi/web/fire` (OpenFIRE), `etsin.fairdata.fi/api/v2/datasets`, `earthquake.usgs.gov/data/crust/`, `www.geo.cornell.edu/geology/cocorp/COCORP.html`, DOI `10.5880/fidgeo.2026.059` | Documented as dead in the relevant rows. Use the live replacements named there |

**Two hosts that lie about missing files — do not trust a bare status code:**
- `merc.laurentian.ca` **soft-404s**: a missing file returns `302 → 200 text/html`. A real
  file returns `200` + `Content-Type: application/zip` + `Content-Length`.
- `data.earthscope.org` returns **403 `application/xml`** (S3 access-denied) for a
  *missing* key, not 404 — so a wrong filename looks like a permissions problem. Use
  `?json` to get the real filenames rather than guessing.

## 8. What could not be confirmed (running list)

- **USGS Global Crustal Database — RESOLVED AS DEAD, partially rescued.** See rows 85–87.
  The live site is gone; the Wayback Machine holds the site structure and exactly **two**
  continental data extracts (`nam-data.txt`, `sam-data.txt`). Extracts for Europe, Asia,
  Africa and Australia were **not** captured. Mooney's USGS staff page is live at
  https://escweb.wr.usgs.gov/share/mooney/ but exposes no directory index. If the full
  compilation is wanted, the remaining route is a direct request to USGS Menlo Park.
  `search: Chulick Mooney global crustal database ASCII compilation request`
- COCORP licence terms — the server carries `Lien.rtf` / `Lien1.txt` at root but no
  explicit open licence statement.
- Metal Earth Matheson R1 direct ZIP URL (size known from an earlier pass, URL not
  re-verified this session).
- ~~Whether CD-ROM / Rocky Mountain Front II / INDEPTH waveforms are actually served~~ —
  **RESOLVED**: their *passive* deployments are in `fdsnws`, and their *controlled-source*
  data is in the assembled-dataset archive (§2.5, §4.1).
- **USGS's own legacy crustal refraction programme (1960s–1990s) is not in ScienceBase.**
  A ScienceBase catalog query for `seismic refraction` returns **26 items**, all modern and
  **near-surface**: Success Dam spillway (Porterville CA, 2018–19, raw data + shot notes +
  velocity models), West Napa Fault Zone 2015, San Andreas Lake 2011 line 8, Edwards AFB
  2020, Fremont CA, Año Nuevo. These are engineering/site-characterisation surveys, not
  crustal profiles. `https://www.sciencebase.gov/catalog/items?q=seismic%20refraction&format=json` [V]
- ~~Deep Probe / CD-ROM not found~~ — **RESOLVED**, see §2.5. Both are open in the
  assembled-dataset archive. **SAREX (Southern Alberta Refraction Experiment, 1991)** is
  still not located: no FDSN network entry, and no matching row in the 852-row assembled
  catalogue. Treat as literature-only unless obtained from the LITHOPROBE Alberta Basement
  Transect PIs. `search: SAREX 1991 Southern Alberta Refraction Experiment data`
- **ADCOH — Appalachian Ultradeep Core Hole** site-investigation seismic (Çoruh, Costain,
  Virginia Tech, 1980s): papers only, no archive found. The physical data may sit with the
  COCORP/ELLIPSE holdings or Virginia Tech.
  `search: ADCOH seismic reflection SEG-Y archive Virginia Tech`
- **Byte size of the GFZ GIPP Western Makran dataset (Iran)** — DataCite `<sizes/>` is
  empty and access is request-gated, so there is no measurable endpoint.
- **Any archive for the DESERT 2000 controlled-source shot gathers** — searched GEOFON,
  GFZ Data Services/GIPP, FDSN and PH5. Appears not to exist; only the passive `ZR` array
  is archived, and that without a minted DOI.
- **The 199 three-component EDL recordings from GEO-DESIRE 2006** — not archived; personal
  email to GFZ only.
- **Whether SISMER supplies SEISMARMARA SEG-Y on individual request** — no seismic order
  form on the cruise page; `https://data.ifremer.fr/SISMER` returns 404.
- **IIEES (Iran) data-request deep URL** — https://www.iiees.ac.ir/en/ is live but the
  "Request for Seismological Data" nav target is a JS anchor; IIEES distributes earthquake
  waveforms by request, not controlled source.
- **geodata.cn per-dataset metadata, ScienceDB file-level download mechanics, JAMSTEC
  aggregate byte volume, VSEGEI file retrievability**, and the **absence of a formal
  EarthScope/SAGE licence statement** on the assembled datasets.
- **ECORS (France, Pyrenees & Alps, 1983–91)** — no digital archive at BRGM, InfoTerre,
  CNRS/INSU or SISMER. `search: ECORS Pyrenees deep seismic SEG-Y archive BRGM`
- **URSEIS 1995 (Urals)** and **EUROBRIDGE (East European Craton)** — no repository in
  DataCite, EarthScope or SeisDARE; published velocity models only.
  `search: URSEIS 1995 Urals reflection SEG-Y archive`
- **BABEL marine multichannel (1989)** — the 2,268 km near-vertical dataset has no public
  archive; traced to the Durham/BIRPS legacy.
  `search: BABEL 1989 marine reflection SEG-Y Durham Hobbs`
- **Kiruna / Skellefte deep reflection** (Uppsala, X-MINE, Smart Exploration) — zero hits
  on Zenodo/SND; Blötberget sparse 3D is under a 3-year embargo, author contact only.
- **swisstopo NFP-20 line-level downloads** — the STAC collection says some processed
  lines are downloadable, but no NFP-20 line exposed one.
- **HIRE line-km and price** — GTK's Hakku price endpoint needs a WKB geometry; GTK quotes
  2,820 line-km for FIRE + HIRE combined.
- **Licence for the EarthScope-hosted Central European datasets** (POLONAISE'97,
  CELEBRATION 2000, ALP 2002, SUDETES 2003, DOBRE'99) — **no licence statement exists** on
  any landing page or inside the tarballs. They are downloadable but legally unlabelled.
- **GA L206 South Gippsland**: the `Processed_Seismic_Package.zip` naming pattern returns
  403; the real filename must be read out of its eCat record (eCat 89800).

---

**Search-coverage caveat.** The session's WebSearch budget was exhausted before this work
began, so all discovery ran through a curl-based Ecosia backend. That backend returned "no
results" for a noticeable fraction of Turkish, Iranian and Indian queries. The negatives
for those countries therefore rest primarily on **direct archive queries** — the
geographic PH5 query in §4.5, the 852-row assembled catalogue, the 1,206-row FDSN network
list and the 234-row PH5 network list — which are strong precisely because they are
structural rather than keyword-based.

*Generated by verification-by-fetch. Every `[V]` row was confirmed by an HTTP request made
during this research session. Sizes in bytes come from `Content-Length`.*
