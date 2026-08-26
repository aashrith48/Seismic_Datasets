# Government / Regulator Petroleum Data Portals (country-by-country)

Legend: **[V]** = confirmed live/accurate during research; **[K]** = from prior knowledge, not re-verified — treat volumes as indicative and re-check before citing.

Confirmed during research: UK NDR >600 TB (now ~1 PB), 135 TB uploaded in one half-year; NLOG 5-yr statutory confidentiality (10-yr multi-client); NOPIMS now at ga.gov.au / public.neats.nopta.gov.au; SDLS ~300,000 line-km; ViDEPI free CC-BY 4.0; C-NLOPB renamed **C-NLOER** (cnloer.ca), CNSOPB renamed **CNSOER** (cnsoer.ca); PASA is at pasa.co.za; BOEM public seismic is delivered through USGS NAMSS.

## North America

| # | Country | Agency | Portal / URL | Seismic released | Volume | Access | Notable surveys | Bulk mechanism | Confidentiality | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | USA | BOEM/BSEE | BOEM Data Center — https://www.data.boem.gov/Main/Seismic.aspx | Public 2D/3D post-stack via NAMSS; permit metadata; nav | see NAMSS | Free | GOM 2D grids (1970s–90s), Atlantic, Alaska OCS | Redirects to NAMSS; File Request System for permit scans | OCS G&G permit data proprietary 25 yr | [V] |
| 2 | USA | USGS CMHRP | NAMSS — https://walrus.wr.usgs.gov/namss | 2D stacks + dozens of 3D post-stack volumes; SEG-Y, SEG-P1 nav; no pre-stack | ~30–40 TB total (several 3D volumes 100s of GB each) | Open download, no registration | GOM 3D volumes, Atlantic USGS/BOEM 2D, Beaufort/Chukchi 2D, Bering Sea | HTTP per-file; no API | Inherits BOEM 25-yr term | [K] volume; [V] existence |
| 3 | USA | USGS CMGP/CMHRP | CMGDS — https://cmgds.marine.usgs.gov | High-res sparker/chirp/boomer 2D SEG-Y from research cruises | ~10s TB | Open (public domain) | Atlantic margin, Cascadia, Gulf | HTTP/ScienceBase; per-survey zip | None | [K] |
| 4 | USA | NSF/UTIG/LDEO | Academic Seismic Portal (MGDS) — https://www.marine-geo.org | Academic MCS 2D/3D incl. pre-stack field data | 100s TB (R/V Langseth archive) | Open after 2-yr NSF moratorium | Cascadia CASIE21, ENAM, Costa Rica CRISP, Hikurangi NZ3D | HTTP/FTP from MGDS; DOI'd datasets | 2-yr NSF | [K] |
| 5 | USA | Texas BEG | https://www.beg.utexas.edu | Very limited public SEG-Y; mostly reports; Stratton 3D via SEG wiki | small | Request / mixed | Stratton 3D | Request | n/a | [K] |
| 6 | USA | Kansas Geological Survey | https://kgs.ku.edu/Geophysics/ ; https://kgs.ku.edu/PRS/ | Multiple free 2D lines and several free 3D SEG-Y volumes (high-res, Kansas) | <1 TB (dozens of GB) | Open download | Dickman Field 3D, Wellington Field 3D (CO2 CCUS + 4D), Cutter Field 3D, Hugoton lines, Cherokee Basin 2D | HTTP per-file | None | [K] |
| 7 | USA | Oklahoma Geological Survey | https://www.ou.edu/ogs | No seismic SEG-Y; earthquake network data | small | Open | — | Web | n/a | [K] |
| 8 | USA | Louisiana DNR | SONRIS — https://www.sonris.com | Seismic permits/index only | — | Open | — | Web | n/a | [K] |
| 9 | USA | Alaska DGGS / GMC | https://dggs.alaska.gov/gmc/seismic-well-data.php | Released state-lease 2D/3D SEG-Y via Geologic Materials Center | ~10s TB | Free/at-cost copy | North Slope 2D grids; NPRA legacy 2D | Request / physical media | 25 yr for state data | [V] page; [K] details |
| 10 | USA | USGS Alaska | NPRA Legacy Data Archive — https://energy.usgs.gov / ScienceBase | Full NPRA 2D SEG-Y (reprocessed) + nav | ~1–2 TB | Open | ~15,000 line-mi NPRA 2D | HTTP | none | [K] |
| 11 | USA | DOE NETL | EDX — https://edx.netl.doe.gov | Teapot Dome 3D (+ logs), Wyoming/Illinois basin CCS datasets, NAMSS mirror | ~1 TB | Free with login | Teapot Dome (RMOTC) 3D, Kimberlina, Illinois Basin Decatur (IBDP) | HTTP; EDX API | none | [V] login model |
| 12 | USA | DOE RMOTC (legacy) | Teapot Dome — via SEG wiki & EDX | 3D post-stack + pre-stack gathers, VSP, logs | ~200 GB | Open | Teapot Dome 3D | HTTP | none | [K] |
| 13 | USA | Wyoming State Geological Survey | https://www.wsgs.wyo.gov | No public SEG-Y | — | — | — | — | — | [K] |
| 14 | USA | Utah Geological Survey | https://geology.utah.gov | No public SEG-Y; some UGS 2D on request | tiny | Request | — | — | — | [K] |
| 15 | USA | Illinois State Geological Survey | https://isgs.illinois.edu ; https://sequestration.org | IBDP Decatur 3D/4D and VSP via EDX | <1 TB | Free | Illinois Basin Decatur 3D | HTTP | none | [K] |
| 16 | USA | SEG | SEG Open Data wiki — https://wiki.seg.org/wiki/Open_data | Curated list; links to Stratton, Teapot, Poseidon, F3, Parihaka, etc. | few TB aggregate | Open | Parihaka 3D, Poseidon 3D | HTTP/S3 | none | [K] |
| 17 | Canada | C-NLOER (ex-C-NLOPB) | https://www.cnloer.ca ; https://home-cnlopb.hub.arcgis.com | Released 2D/3D; SEG-Y by request; nav via hub | ~100s TB archive | At-cost reproduction via Information Resources Centre | Jeanne d'Arc, Flemish Pass, Orphan Basin 2D/3D | Request order form; physical media | Non-exclusive 15 yr; exclusive 5 yr | [V] rename; [K] rules |
| 18 | Canada | CNSOER (ex-CNSOPB) | https://www.cnsoer.ca/geoscience/geophysical-data | Released 2D/3D; nav & index on GIS; SEG-Y via data centre | 10s–100s TB | Free/at-cost | Sable Island 3Ds, Scotian Slope 2D; NS Play Fairway Analysis data (free) | Request; some downloads | 5 yr exclusive / 15 yr non-exclusive | [V] rename |
| 19 | Canada | NRCan / GSC | GEOSCAN — https://geoscan.nrcan.gc.ca ; https://open.canada.ca | GSC research 2D MCS/high-res (Atlantic, Arctic, Pacific) SEG-Y | ~10s TB | Open (OGL-Canada) | Labrador Sea, Baffin Bay, Beaufort; Frontier Geoscience Program lines | HTTP; FTP | none | [K] |
| 20 | Canada | Alberta AER | https://www.aer.ca ; https://ags.aer.ca | No public SEG-Y (seismic private in AB); AGS open data has interpreted horizons | — | Closed | — | — | Proprietary indefinitely | [K] |
| 21 | Canada | BC / Geoscience BC | https://www.geosciencebc.com | Some public 2D/3D (Nechako 2D) | small | Open | Nechako Basin 2D | HTTP | — | [K] |
| 22 | Canada | Newfoundland & Labrador (Nalcor/OilCo) | https://www.gov.nl.ca/iet | Government-funded regional 2D via TGS/PGS — licensed, not free | >150,000 km 2D | Commercial | Labrador Sea/Orphan 2D & 3D | Commercial licence | 15 yr | [K] |
| 23 | Mexico | CNH | CNIH — https://portal.cnih.cnh.gob.mx ; https://www.gob.mx/cnh | Full national 2D/3D incl. pre-stack; access via Data Room | ~2 PB+ (CNIH >1.5 PB in 2018; other sources say >11 PB); ~8,000+ surveys | Fee-based licence (per km / km²); registration | Perdido, Campeche deepwater 3Ds; Sureste basin | Order form; media/cloud | Licence-specific; Pemex legacy fee-based | [K] |

## South America & Caribbean

| # | Country | Agency | Portal / URL | Seismic released | Volume | Access | Notable surveys | Bulk mechanism | Confidentiality | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 24 | Brazil | ANP | BDEP / ReATE / Dados Abertos — https://www.gov.br/anp/pt-br/assuntos/exploracao-e-producao-de-oleo-e-gas/dados-tecnicos ; https://reate.cprm.gov.br | Public (non-exclusive) 2D/3D nav & SEG-Y; full SEG-Y via BDEP with fees; some pre-stack | BDEP ~5–7 PB; public-domain post-stack subset PB-scale (100 TB pre-stack + 37 TB offshore post-stack released via REATE) | Fee-based delivery; universities free under agreement | Santos/Campos/Espírito Santo 3Ds; Equatorial margin 2D | Order form; media/SFTP; ReATE web GIS | 2–10 yr exclusive; then public (fee) | [V] fee model |
| 25 | Argentina | Secretaría de Energía | SIGMA — https://sigma.energia.gob.ar | Mostly index/nav; SEG-Y via request | small | Request | Neuquén basin | Web GIS, request | Ley 17.319 | [K] |
| 26 | Colombia | ANH | EPIS / BIP — https://www.anh.gov.co ; https://epis.anh.gov.co | Full national 2D/3D & pre-stack after confidentiality | ~1.5 PB (~150,000 km 2D, 30,000 km² 3D) | Free for academia; fee for industry; registration | Llanos, Magdalena 3Ds; Caribbean offshore 2D | Order/download from EPIS | 5 yr, then public | [K] |
| 27 | Peru | Perupetro | https://www.perupetro.com.pe | 2D/3D; nav on GIS; SEG-Y via data room | ~100s TB (~250,000 km 2D, 30,000 km² 3D) | Fee-based; some free to academia | Marañon, Talara, offshore | Request; media | Contract-based | [K] |
| 28 | Venezuela | MinPetróleo/PDVSA | — | No public portal | — | Closed | — | — | — | [K] |
| 29 | Trinidad & Tobago | MEEI | https://www.energy.gov.tt | 2D/3D via licensed packages | ~10s–100s TB | Fee/bid-round | Columbus Basin 3D | Data room | Contract | [K] |
| 30 | Guyana | Ministry of Natural Resources | https://petroleum.gov.gy | Regional 2D/3D via licensed packages | — | Fee | Stabroek-era 3D (proprietary) | Data room | Contract | [K] |
| 31 | Suriname | Staatsolie | https://www.staatsolie.com/en/exploration | Offshore 2D/3D via licensed package | ~100 TB | Fee | Block 58 region 3Ds, regional 2D | Virtual data room | Contract | [K] |

## Europe

| # | Country | Agency | Portal / URL | Seismic released | Volume | Access | Notable surveys | Bulk mechanism | Confidentiality | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 32 | UK | NSTA | National Data Repository — https://ndr.nstauthority.co.uk | Released 2D/3D post-stack SEG-Y, pre-stack (mandatory full upload since 2018), nav; NSTA gov-funded reprocessing | **>600 TB (2023); ~1 PB (2024–25)**; 135 TB uploaded in one half-year | Free, registration | CNS/NNS/WoS post-stack mega-merges; 2016–2019 government-funded 2D (SW Britain, ESP ~19,000 km, Rockall, Mid-North Sea High); Rockall 3D | Web (Osokey-built) preview + download; bulk requests | 4 yr seismic; 3 yr wells | [V] |
| 33 | UK (onshore) | UKOGL | https://ukogl.org.uk | Onshore 2D/3D SEG-Y; free to view images, SEG-Y licensed | ~60–87,000 km 2D onshore, ~40 3Ds | Free viewing; SEG-Y fee (free for academia) | Weald, East Midlands 3Ds | Order | 4 yr | [K] |
| 34 | UK | BGS | Offshore GeoIndex / NGDC — https://www.bgs.ac.uk | Legacy BGS 2D shallow seismic scans/SEG-Y | ~1 TB | Open (OGL) | Regional sparker/boomer | Web | none | [K] |
| 35 | Norway | Sodir (ex-NPD) / Diskos | https://www.sodir.no/en/diskos ; FactPages https://factpages.sodir.no | All released 2D/3D (nav, post-stack SEG-Y; pre-stack/field where filed); released data **free** (media/handling cost only) | Diskos ~8–22 PB total; >2,000 3D surveys; ~1 PB+ released post-stack | Free (released); membership for members; public portal for released | Barents Sea regional 3Ds; NPD-acquired free; Norwegian Sea broadband | Portal download; large via transfer request | 5 yr exclusive; 10 yr multi-client; NPD-acquired immediate | [K] |
| 36 | Netherlands | TNO – Geological Survey NL | NLOG — https://www.nlog.nl/en/data | **All released 2D/3D**: SEG-Y post-stack, nav; pre-stack for some; onshore & offshore; no fee | ~1,000+ 2D surveys, ~135–200 3D surveys; ~50–100 TB post-stack online | Open download, no registration | Whole Dutch North Sea 3D coverage, onshore Groningen 3D | HTTP per-survey; FTP for large | 5 yr statutory; 10 yr multi-client | [V] rules |
| 37 | Denmark | GEUS / DEA | GEUS Subsurface Data Portal — https://data.geus.dk/geusmap/?mapname=oil_and_gas | Released 2D/3D SEG-Y & nav | ~10s TB; several hundred 2D surveys, ~60 3Ds (1,400 surveys total) | Free (registration); handling fee for field data | Danish Central Graben 3Ds; GEUS onshore 2D | Web/FTP request | 5 yr, then free | [K] |
| 38 | Germany | LBEG (Lower Saxony) | NIBIS — https://nibis.lbeg.de | Seismic line index; SEG-Y by request, limited | — | Request, fee | — | Request | 10 yr | [V] no direct SEG-Y |
| 39 | Germany | BGR | via PANGAEA — https://www.pangaea.de | BGR research 2D lines (Arctic, Antarctic, N. Atlantic) | ~10 TB | Open via PANGAEA / request | BGR polar 2D | HTTP | Research | [K] |
| 40 | Poland | PGI-NRI | CBDG — https://geologia.pgi.gov.pl | Seismic index; SEG-Y for released surveys on request | ~10s TB | Fee/free for state data | Carpathians, Baltic 2D/3D | Order | 5 yr | [K] |
| 41 | Ireland | DECC PAD / GSI | PAD Data Hub — https://www.gov.ie (PAD); https://data.gov.ie/dataset/3d-seismic-survey | Released 2D/3D SEG-Y; large regional Atlantic packages | ~100s TB; ~400,000 km 2D, ~44 3Ds | Free (registration) since 2013 | Irish Atlantic regional 2D (ENI/PAD 2013 ~18,000 km), Porcupine 3Ds | Web/FTP; ordered on disk | 5 yr exclusive; 6 yr non-exclusive | [K] |
| 42 | France | BRGM | InfoTerre / Minergies — https://infoterre.brgm.fr ; https://www.minergies.fr | Onshore 2D index; SEG-Y via BRGM at cost | ~1–5 TB | Fee/request | Paris Basin 2D | Order | 10 yr | [K] |
| 43 | Italy | MIMIT DGIS-UNMIG | ViDEPI — https://www.videpi.com | Free scanned seismic sections (raster) + some SEG-Y; 2D only | ~85,000 km 2D as images | Open, CC-BY 4.0 | Adriatic, Po Valley 2D | HTTP | 1 yr after permit expiry | [V] |
| 44 | Spain | IGME-CSIC / MITECO | Archivo Técnico de Hidrocarburos — https://www.igme.es | Released 2D/3D SEG-Y & scans | ~10s TB (>200,000 km 2D) | Free (request) | Iberian offshore 2D, Ebro 3D | Request; portal for scans | 5 yr | [K] |
| 45 | Portugal | DGEG (ENSE) | https://www.dgeg.gov.pt | Released 2D/3D; SEG-Y by request | ~10s TB (~130,000 km 2D) | Free/fee | Lusitanian, Peniche, Alentejo 3Ds | Request | 5 yr | [K] |
| 46 | Greece | HEREMA (ex-HHRM) | https://herema.gr | PGS 2012–13 regional 2D (12,500 km) — licensed | ~10s TB | Fee/data room | PGS Western Greece 2D | Data room | Contract | [K] |
| 47 | Romania | NAMR | https://www.namr.ro | Released 2D/3D by request; fee | — | Fee | Black Sea 3Ds | Request | — | [K] |
| 48 | Croatia | CHA (AZU) | https://www.azu.hr | Adriatic 2D/3D (Spectrum multi-client + legacy INA) | ~10 TB | Fee/data room | Adriatic 2D (Spectrum 2013) | Data room | Contract | [K] |
| 49 | Cyprus | Ministry of Energy | https://www.mcit.gov.cy | PGS multi-client 2D/3D — licensed | — | Fee | Levant Basin 3D | Data room | Contract | [K] |
| 50 | Israel | Ministry of Energy | https://www.gov.il/en/departments/ministry_of_energy | Released 2D/3D nav and SEG-Y; some free after confidentiality | ~10s TB | Free/fee | Levant 3Ds | Request | 5 yr | [K] |
| 51 | Turkey | MAPEG / TPAO | https://www.mapeg.gov.tr | Released 2D/3D by request; largely closed | — | Fee/request | Black Sea 3Ds | Request | — | [K] |
| 52 | Russia | Rosnedra / Rosgeolfond | https://rfgf.ru | Inaccessible to foreigners | huge | Closed | — | — | — | [K] |
| 53 | Azerbaijan | SOCAR | — | Closed | — | Closed | — | — | — | [K] |
| 54 | Kazakhstan | Ministry of Energy / National Data Bank | https://geology.gov.kz | Index & fee-based SEG-Y | — | Fee | Caspian 2D/3D | Request | — | [K] |

## Africa & Middle East

| # | Country | Agency | Portal / URL | Seismic released | Volume | Access | Notable surveys | Flag |
|---|---|---|---|---|---|---|---|---|
| 55 | South Africa | PASA | https://www.pasa.co.za ; geoportal.petroleumagencysa.com | Released 2D/3D SEG-Y | ~100s TB (~250–300,000 km 2D, ~30+ 3Ds incl. Orange Basin) | Fee (data packages); free indexes; academic tier | Orange Basin 3Ds, Outeniqua | [V] domain |
| 56 | Namibia | NAMCOR | https://www.namcor.com.na ; https://gisportal.namcor.com.na/viewer | Released 2D/3D; fee | ~100s TB | Fee | Orange Basin 3Ds, regional 2D | [V] portal |
| 57 | Angola | ANPG | https://anpg.co.ao | Closed; licensed via bid rounds | PB-scale | Fee/data room | Kwanza, Lower Congo 3Ds | [K] |
| 58 | Mozambique | INP | https://www.inp.gov.mz | Bid-round packages; multi-client | 100s TB | Fee | Rovuma 3Ds | [K] |
| 59 | Tanzania | TPDC / PURA | https://www.tpdc.co.tz ; https://www.pura.go.tz | Closed/licensed | — | Fee | Deepwater 3D | [K] |
| 60 | Kenya | NOCK | https://nationaloil.co.ke | Data room | — | Fee | Lamu basin 2D/3D | [K] |
| 61 | Uganda | PAU | https://www.pau.go.ug | National Data Centre; fee | — | Fee | Albertine 2D/3D | [K] |
| 62 | Ghana | Petroleum Commission | https://www.petrocom.gov.gh | Fee-based NDR | ~100s TB | Fee | Tano/Cape Three Points 3Ds | [K] |
| 63 | Nigeria | NUPRC / NNPC | https://www.nuprc.gov.ng | Fee-based NDR | PB-scale (Niger Delta 3Ds) | Fee | Niger Delta 3Ds | [K] |
| 64 | Gabon | DGH | https://www.dgh.gouv.ga | Licensed (CGG multi-client) | — | Fee | Deepwater 3D | [K] |
| 65 | Senegal | Petrosen | https://www.petrosen.sn | Data room | — | Fee | MSGBC 3Ds | [K] |
| 66 | Morocco | ONHYM | https://www.onhym.com | Data room; some free scans | — | Fee (discounted) | Atlantic margin 2D/3D | [K] |
| 67 | Egypt | EGAS / EGPC | Egypt Upstream Gateway — https://eug.egas.com.eg | Digital data via EUG (2021); fee | PB-scale | Fee | Mediterranean/Red Sea 3Ds | [K] |
| 68 | Libya | NOC | https://noc.ly | Closed | huge | Closed | — | [K] |
| 69 | Algeria | ALNAFT | https://www.alnaft.gov.dz | Closed / data room | — | Fee | — | [K] |
| 70 | Mauritania | Ministry | https://www.petrole.gov.mr | Data room | — | Fee | Offshore 3D | [K] |
| 71 | Somalia | SPA | https://spa.so | TGS multi-client 2D licensed | ~20,000 km 2D | Fee | TGS 2D | [K] |
| 72 | Sierra Leone | PDSL | https://www.pdsl.gov.sl | Data room | — | Fee | Offshore 3D | [K] |
| 73 | Liberia | LPRA | https://www.lpra.gov.lr | Data room | — | Fee | Offshore 3D | [K] |
| 74 | Côte d'Ivoire | Petroci | https://www.petroci.ci | Data room | — | Fee | Offshore 3Ds | [K] |
| 75 | Equatorial Guinea | MMH | — | Closed | — | Fee | — | [K] |
| 76 | Congo (Brazzaville) | SNPC | https://www.snpc.cg | Closed | — | Fee | — | [K] |
| 77 | Madagascar | OMNIS | https://www.omnis.mg | Data room | — | Fee | Offshore 2D | [K] |
| 78 | Oman | MEM | — | Closed | — | Closed | — | [K] |
| 79 | UAE | ADNOC / SPC | — | Closed | — | Closed | — | [K] |
| 80 | Saudi Arabia | Saudi Aramco / MEM | — | Closed | — | Closed | — | [K] |

## Asia-Pacific

| # | Country | Agency | Portal / URL | Seismic released | Volume | Access | Notable surveys | Bulk mechanism | Confidentiality | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| 81 | Australia | NOPTA / Geoscience Australia | NOPIMS — https://www.ga.gov.au/nopims ; https://public.neats.nopta.gov.au/nopims | All released Commonwealth offshore 2D/3D: nav, post-stack SEG-Y, **field/pre-stack** where lodged; free | **~3–4 PB** (100s of 3D surveys) | Free, registration; large volumes via GA data request | Browse, Carnarvon, Bonaparte 3Ds; GA-acquired 2D (Capel-Faust, Bight); Poseidon 3D | Web download; bulk via data request; S3 delivery | Basic 3 yr, interpretive 5 yr; GA-acquired immediate | [V] URL; [K] volume |
| 82 | Australia | Geoscience Australia | eCat — https://ecat.ga.gov.au | GA marine survey SEG-Y (regional 2D) | ~100s TB | Open (CC-BY) | Southwest Margins 2D, Bight | HTTP/S3 | none | [K] |
| 83 | Australia – WA | DEMIRS | WAPIMS — https://wapims.dmirs.wa.gov.au | Onshore/state-waters released 2D/3D SEG-Y | ~100s TB | Free | Canning, Perth Basin 3Ds | Web; large via request | 2–3 yr basic, 5 yr interp | [K] |
| 84 | Australia – QLD | GSQ | GSQ Open Data Portal — https://geoscience.data.qld.gov.au | Released 2D/3D SEG-Y | ~100s TB (Bowen/Surat/Cooper) | Open, CC-BY, S3 | Cooper/Eromanga 3Ds | S3 bucket + web | 2 yr basic | [K] |
| 85 | Australia – SA | Dept Energy & Mining | SARIG — https://map.sarig.sa.gov.au | All released 2D/3D SEG-Y & field data (Cooper/Otway) | **~1 PB+**; ~200 3Ds | Open, no fee; bulk via AWS S3 | Cooper Basin 3D mega-merges, Otway 3Ds | S3 / web | 2 yr basic | [K] |
| 86 | Australia – VIC | GSV | https://earthresources.vic.gov.au | Released 2D/3D SEG-Y (Gippsland, Otway onshore) | ~10s TB | Free | Otway, Gippsland 3Ds | Web/request | 2 yr | [K] |
| 87 | Australia – NSW | GSNSW | DIGS — https://digsopen.minerals.nsw.gov.au | Seismic reports & some SEG-Y | ~1–10 TB | Open | Sydney/Darling 2D | Web | — | [K] |
| 88 | Australia – NT | NTGS | GEMIS — https://geoscience.nt.gov.au | Released onshore 2D/3D SEG-Y (Beetaloo) | ~10s TB | Open | Beetaloo 2D, McArthur | Web | 2 yr | [K] |
| 89 | New Zealand | NZP&M (MBIE) | https://www.nzpam.govt.nz/maps-geoscience/petroleum-data | All released 2D/3D SEG-Y + field data; free | ~100s TB; ~1,500 surveys | Free, registration; HDD request for large | Parihaka 3D, Pegasus, Great South 2D | Web + Exploration Data Packs; HDD order | 5 yr | [V] site |
| 90 | PNG | Dept of Petroleum & Energy | https://www.petroleum.gov.pg | Data room; fee | — | Fee | Gulf of Papua 3D | Data room | — | [K] |
| 91 | Indonesia | MIGAS / Patra Nusa Data | https://www.migas.esdm.go.id ; https://www.pnd.co.id | Fee-based; PND manages | PB-scale | Fee (open-data policy since 2020 but delivery fee) | Kutai, N. Sumatra 3Ds | Order | 4–6 yr | [V] site |
| 92 | Malaysia | PETRONAS MPM | MyPROdata — https://mypro.petronas.com | Fee/licensed | PB-scale | Fee | Sabah/Sarawak 3Ds | Data room | — | [K] |
| 93 | Thailand | DMF | https://www.dmf.go.th | Fee; data room | — | Fee | Gulf of Thailand 3D | Request | — | [K] |
| 94 | Vietnam | PVN / VPI | https://www.pvn.vn | Closed/fee | — | Fee | — | — | — | [K] |
| 95 | Philippines | DOE | https://www.doe.gov.ph | Bid-round packages | — | Fee | Palawan 2D/3D | Data room | — | [K] |
| 96 | India | DGH | NDR — https://ndr.dghindia.gov.in ; https://www.dghindia.gov.in | Full national 2D/3D & pre-stack (post-2017); free viewing; fee for download (free for academia) | **~8–10 PB** (~2.5 M line-km 2D, ~500,000 km² 3D) | Fee (waived academia); registration | KG, Mumbai Offshore 3Ds; NSP 2D (48,000 km) | Web/FTP request; media | 7 yr exclusive; NSP immediate | [K] |
| 97 | Pakistan | DGPC / LMKR | https://www.dgpc.gov.pk | Fee | — | Fee | Indus 2D/3D | Order | — | [K] |
| 98 | Bangladesh | Petrobangla | https://petrobangla.org.bd | Closed | — | Fee | — | — | — | [K] |
| 99 | Myanmar | MOGE | — | Closed | — | Closed | — | — | — | [K] |
| 100 | China | MNR / CNPC / Sinopec | — | Closed (state secrecy) | huge | Closed | — | — | — | [K] |
| 101 | Japan | JOGMEC / METI / AIST GSJ | https://www.gsj.jp ; https://www.jogmec.go.jp | METI Basic Survey 2D/3D on request; AIST GSJ marine 2D free | ~10s TB | Request/free | Sea of Japan 3D basic surveys; GSJ shelf 2D | Request | — | [K] |
| 102 | South Korea | KIGAM / KNOC | https://data.kigam.re.kr | KIGAM research 2D; KNOC closed | ~1 TB | Open (KIGAM) | Ulleung basin 2D | Web | — | [K] |

## Antarctica & multinational / open initiatives

| # | Scope | Agency | Portal / URL | Seismic released | Volume | Access | Notable | Flag |
|---|---|---|---|---|---|---|---|---|
| 103 | Antarctica | SCAR / OGS | SDLS — https://sdls.ogs.it | All Antarctic MCS 2D SEG-Y (stacked) | **~300,000 line-km**; ~5–15 TB | Free; ATCM rules (4 yr view-only, 8 yr open) | Ross Sea, Weddell, Wilkes Land | [V] |
| 104 | Global | OSDU Forum | OSDU Open Test Data — https://community.opengroup.org/osdu/platform/data-flow/data-loading/open-test-data | Volve, TNO/NLOG subset, Poseidon 3D | ~1–2 TB | Open (Apache-2.0 repo; data per source licence) | Volve 3D/4D, TNO | [V] |
| 105 | Global | Equinor | Volve — https://www.equinor.com/energy/volve-data-sharing | Volve 3D (pre-/post-stack), 4D, VSP, wells | ~5 TB (40,000 files) | Open (Equinor Open Data Licence) | Volve | [V] |
| 106 | Global | Equinor | Northern Lights open data | Well & seismic subset for CCS | ~1 TB | Open | Northern Lights | [K] |
| 107 | Global | Equinor / Sodir | CO2 DataShare — https://co2datashare.org | Sleipner 4D seismic, Smeaheia 3D | ~1 TB | Open | Sleipner 4D | [K] |
| 108 | Global | Shell / NAM | Groningen 3D via NLOG | see NLOG | Open via NLOG | Groningen | [K] |
| 109 | Global | dGB / OpendTect | TerraNubis — https://terranubis.com | F3 (NL), Penobscot (Canada), Netherlands offshore, Blake Ridge | ~1 TB | Free (registration) | F3 3D, Penobscot 3D | [K] |
| 110 | Global | SEG / SEAM | https://seg.org/SEAM | Synthetic 3D pre-stack (SEAM Phase I/II) | ~10s TB | Fee for non-members; some free | SEAM I | [K] |
| 111 | Commercial | TGS (incl. PGS) | https://www.tgs.com | PB-scale multi-client | >10 PB | Licensed — **not open** | — | [K] |
| 112 | Commercial | Searcher Seismic | https://www.searcherseismic.com | Multi-client | — | Licensed — not open | — | [V] |
| 113 | Commercial | Viridien (CGG) / Shearwater / Geoex MCG | — | Licensed | — | Not open | — | [K] |

## Top 20 largest publicly accessible seismic archives (by TB)

"Publicly accessible" = a member of the public can obtain released SEG-Y for free or a nominal handling fee. Confidence: H = verified/official; M = official statement recalled; L = order-of-magnitude estimate.

| Rank | Archive | Est. released/accessible volume | Confidence | Notes |
|---|---|---|---|---|
| 1 | Norway Diskos/Sodir | ~1 PB+ released (total 8–22 PB) | M | Released data free; heavy pre-stack |
| 2 | UK NSTA NDR | ~1 PB loaded, >600 TB confirmed 2023 | **H** | Free registration; pre-stack for post-2018 |
| 3 | Australia NOPIMS / GA | ~3–4 PB open-file (incl. field data) | M | Free; largest open field-data holding |
| 4 | Australia SARIG (SA) | ~1 PB (Cooper/Otway incl. field) | M | Open, S3 bulk |
| 5 | Brazil ANP BDEP (public subset) | ~1–2 PB public-domain | L | Fee delivery; free for universities |
| 6 | India DGH NDR | ~8–10 PB total; public subset unknown | L | Fee except academia |
| 7 | Mexico CNIH | ~2–11 PB total; fee | L | Fee per km/km² |
| 8 | Colombia ANH EPIS | ~1.5 PB | L | Free academia / fee industry |
| 9 | Netherlands NLOG | ~50–100 TB post-stack online; more on request | M | Fully free, no registration |
| 10 | New Zealand NZP&M | ~100s TB | M | Free |
| 11 | Ireland PAD | ~100s TB | M | Free |
| 12 | Queensland GSQ Open Data | ~100s TB | L | Open S3 |
| 13 | WA WAPIMS | ~100s TB | L | Free |
| 14 | C-NLOER (Newfoundland) | ~100s TB released; at-cost | L | Order form |
| 15 | Academic Seismic Portal (MGDS) | 151 TB incl. pre-stack | H | Open |
| 16 | South Africa PASA | ~100s TB | L | Fee packages |
| 17 | USGS NAMSS | ~30–40 TB | M | Open download, no registration |
| 18 | CNSOER (Nova Scotia) | ~10s–100s TB | L | At-cost |
| 19 | Denmark GEUS | ~10s TB | L | Free |
| 20 | Alaska DGGS / USGS NPRA | ~10s TB | L | Free/at-cost |

Honorable mentions for "free and frictionless" (small but zero-friction): Kansas KGS 3Ds, Teapot Dome (EDX), Volve, TerraNubis F3/Penobscot, SDLS Antarctica, ViDEPI Italy.

## Effectively closed / fee-only (no free public SEG-Y)

Russia (Rosnedra), China (MNR), Saudi Arabia, UAE, Oman, Libya, Algeria, Azerbaijan, Myanmar, Venezuela, Bangladesh, Vietnam, Alberta AER, Malaysia PETRONAS, Indonesia MIGAS/PND (fee), Thailand DMF, Pakistan, Angola ANPG, Mozambique INP, Tanzania, Nigeria NUPRC, Egypt EUG, Ghana PC, Gabon, Senegal, Kenya, Uganda, Morocco, Mauritania, Somalia, Sierra Leone, Liberia, Côte d'Ivoire, Eq. Guinea, Congo, Madagascar, PNG, Philippines, Trinidad, Guyana, Suriname, Greece, Cyprus, Romania, Croatia, Turkey, Kazakhstan, Germany LBEG (request/fee), France BRGM (fee), Poland (mixed), Peru (fee), Argentina (request), and all commercial libraries (TGS/PGS, Searcher, Viridien/CGG, Shearwater, Geoex MCG).

## Shortlist: truly huge + truly free + pre-stack available

**Australia NOPIMS/GA + SARIG**, **Norway Diskos released data**, **UK NSTA NDR**, then **NLOG** and **NZP&M**. Everything else at PB scale (Brazil, India, Mexico, Colombia) is fee-gated for industry (often free for academia).
