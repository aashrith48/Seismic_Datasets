# Earthquake / Passive Seismology, DAS, Large-N, Strong-Motion & Planetary

Legend: **~** = approximate; **(est.)** = estimate, not verified; **(verified)** = confirmed from a fetched page during research.

## Global / Petabyte-Scale Archives

| # | Name | Host | Region | Type | Size / counts | License / access | URL | Bulk access | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **EarthScope Data Archive (ex-IRIS DMC, NSF SAGE)** | EarthScope Consortium, USA | Global | Continuous + event miniSEED, metadata, PH5 nodal | **>1 PB miniSEED (verified, 2025)**; >70,000 seismometers ever archived; GSN, TA, PASSCAL, international nets | Fully open (some embargoed PI data ≤2 yr); cite network DOI | https://ds.iris.edu / https://www.earthscope.org/data/ | FDSNWS (service.iris.edu), ROVER, PH5, **AWS S3 `s3://earthscope-geophysical-data` (us-east-2; nets AK, II, IU, N4, PB, TA, UU, UW; `--no-sign-request`)** | Largest open seismic archive in the world. Also hosts Apollo (XA) & InSight (XB) mirrors, Ridgecrest DAS. |
| 2 | **SCEDC (Southern California Earthquake Data Center)** | Caltech | S. California | Continuous + event waveforms, catalog (1932–), phase picks, DAS | **~150 TB on S3 (verified)**; 540+ stations (1999–present) | Open, cite doi:10.7909/C3WD3xH1 | https://scedc.caltech.edu/data/cloud.html | **AWS S3 `s3://scedc-pds` (us-west-2, daily updates)**, FDSNWS, STP | Includes Ridgecrest DAS (June–July 2020, 250 Hz SEG-Y hourly). |
| 3 | **NCEDC (Northern California Earthquake Data Center)** | UC Berkeley | N. California | Continuous/event waveforms, catalogs, GPS, strain | **>184–190 TB (verified)**; 29 networks; 2,640 stations | Open | https://ncedc.org | **AWS S3 `s3://ncedc-pds` (us-east-2, entire archive)**, FDSNWS | Includes BK, NC, BP (Parkfield HRSN borehole). |
| 4 | **USGS NEIC / ANSS ComCat** | USGS | Global catalog | Event catalog, ShakeMap, moment tensors, PAGER | Millions of events (catalog only) | Public domain | https://earthquake.usgs.gov/earthquakes/search/ | FDSN event WS, GeoJSON feeds | Waveforms via EarthScope. |
| 5 | **ISC Bulletin** | International Seismological Centre, UK | Global | Bulletin/catalog + phase readings | **>4 M events; ~50 M station readings; ~17,000 stations; ~90 GB DB**; 1904–present | Open (CC-BY) | https://www.isc.ac.uk/iscbulletin/ | Web search, ISC web services, mirror at isc-mirror.iris.washington.edu | ISC-GEM, ISC-EHB. |
| 6 | **GSN (Global Seismographic Network)** | USGS/ASL + UCSD/IDA via EarthScope | Global | ~150 broadband stations (IU, II) | Part of EarthScope PB; IU/II in S3 bucket | Open | https://www.iris.edu/hq/programs/gsn | FDSNWS, S3 | |
| 7 | **GEOSCOPE** | IPGP, France | Global | ~34 VBB stations (network G), 1982– | ~tens of TB (est.) | Open | http://geoscope.ipgp.fr | FDSNWS (datacenter.ipgp.fr) | |
| 8 | **ORFEUS EIDA (federation)** | ORFEUS/EPOS | Europe | Continuous waveforms from ~11 nodes | **Aggregate ~1 PB+ (est.)** | Open (some restricted via tokens) | https://www.orfeus-eu.org/data/eida/ | Federated FDSNWS (`eida-federator`), routing service | |
| 9 | **GEOFON (GFZ)** | GFZ Potsdam | Global/Europe | GE network + ~100 hosted networks | **~>400 TB (est.)** | Open | https://geofon.gfz.de/waveform/ | FDSNWS, EIDA | Largest EIDA node. |
| 10 | **EPOS-France / RESIF** | RESIF/EPOS-FR | France & overseas | Broadband, accelerometric (RAP), temporary | ~hundreds of TB (est.) | Open (CC-BY) | https://seismology.epos-france.fr | FDSNWS | |
| 11 | **INGV EIDA node** | INGV, Italy | Italy/Mediterranean | IV network ~500 stations + others | ~hundreds of TB (est.) | Open (CC-BY) | https://www.eida.ingv.it | FDSNWS | Feeds INSTANCE, ITACA, ESM. |
| 12 | **ETH / SED** | ETH Zurich | Switzerland | CH network + temporary | ~tens of TB (est.) | Open | https://eida.ethz.ch | FDSNWS | |
| 13 | **BGR** | BGR Hannover | Germany | GR + GRSN; GERES array | ~tens of TB (est.) | Open | https://eida.bgr.de | FDSNWS | |
| 14 | **NOA** | National Obs. Athens | Greece | HL network | ~tens of TB (est.) | Open | https://eida.gein.noa.gr | FDSNWS | |
| 15 | **KOERI** | Kandilli Obs., Turkey | Turkey | KO network | ~tens of TB (est.) | Open | https://eida.koeri.boun.edu.tr | FDSNWS | |
| 16 | **NIEP** | INFP Romania | Romania | RO network | ~tens of TB (est.) | Open | https://eida-sc3.infp.ro | FDSNWS | |
| 17 | **ICGC** | ICGC Catalonia | Spain | CA network | ~TB (est.) | Open | https://ws.icgc.cat | FDSNWS | |
| 18 | **UIB-NORSAR** | Univ. Bergen/NORSAR | Norway/Arctic | NS, NO arrays | ~tens of TB (est.) | Open | https://eida.geo.uib.no | FDSNWS | |
| 19 | **ODC/KNMI** | ORFEUS Data Centre | Netherlands/Europe | NL + many nets | ~tens of TB (est.) | Open | https://www.orfeus-eu.org/data/odc/ | FDSNWS | |
| 20 | **BGS EIDA node** | British Geological Survey | UK | GB network | ~TB (est.) | Open | https://eida.bgs.ac.uk | FDSNWS | Newest node. |
| 21 | **Other FDSN centers** | — | — | — | — | — | https://www.fdsn.org/datacenters/ | — | IPGP, LMU, KIT, IGN, EMSC, KAGSR (Kamchatka), CATAC (Nicaragua), OSDC (SUSTech China OBS), RASPISHAKE, USP/RSBR, IESDMC (Taiwan BATS). |

## Regional / National Networks

| # | Name | Host | Region | Type | Size / counts | License / access | URL | Bulk access | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 22 | **NIED Hi-net** | NIED, Japan | Japan | ~800 borehole short-period stations, 100 Hz continuous | NIED total ~>1 PB (est.) | **Free registration**; WIN32 format; 50 MB/request cap; no redistribution; must report results | https://www.hinet.bosai.go.jp | Web download, HinetPy; no FDSN/S3 | Data from 2004 online. |
| 23 | **NIED F-net** | NIED | Japan | ~70 broadband | ~tens of TB (est.) | Registration | https://www.fnet.bosai.go.jp | Web/HinetPy | |
| 24 | **NIED K-NET / KiK-net** | NIED | Japan | Strong motion: ~1,000 surface + ~700 surface/borehole pairs | >1 M records; TB-scale | Registration | https://www.kyoshin.bosai.go.jp/en/ | Web download | Largest strong-motion set globally. |
| 25 | **NIED S-net** | NIED | Japan Trench seafloor | 150 cabled OBS/pressure nodes, 5,700 km cable | ~>100 TB (est.) | Registration (MOWLAS policy) | https://www.seafloor.bosai.go.jp | Web | Operational since 2017. |
| 26 | **NIED DONET1/2 & N-net** | NIED | Nankai Trough | 51 observatories; N-net 2025 | ~tens of TB (est.) | Registration | https://www.seafloor.bosai.go.jp | Web | |
| 27 | **JMA** | Japan Meteorological Agency | Japan | ~200 stations + unified hypocenter catalog | Catalog open | Open catalog | https://www.data.jma.go.jp/svd/eqev/data/bulletin/ | HTTP | |
| 28 | **GeoNet** | GNS Science, NZ | New Zealand | >600 seismic + strong-motion sites; GNSS, tsunami gauges | **~12 GB/day miniSEED**; archive >100 TB (est.) | **CC BY 3.0 NZ** | https://www.geonet.org.nz/data/access/aws | **AWS S3 `s3://geonet-open-data` (ap-southeast-2)**, FDSNWS | |
| 29 | **AusPass** | ANU/AuScope | Australia | Temporary + permanent broadband since 1997 | ~tens of TB (est.) | Open | https://auspass.edu.au | FDSNWS, NCI mirror | |
| 30 | **Geoscience Australia ANSN** | GA | Australia | >100 permanent stations | ~tens of TB (est.) | Open | https://earthquakes.ga.gov.au | FDSNWS; also via IRIS (AU) | |
| 31 | **CNDC / NRCan** | Natural Resources Canada | Canada | CN network >300 stations | ~tens of TB (est.) | Open | https://earthquakescanada.nrcan.gc.ca/stndon/CNDC/ | FDSNWS | |
| 32 | **CEA / CENC (China)** | China Earthquake Administration | China | ~1,000+ permanent + ChinArray | PB-class (est.) | **Restricted**: only 20 national stations' event waveforms to IRIS; Level-1 waveform needs request | http://www.ceic.ac.cn / http://chinageorefmodel.org | Request-based | DiTing/CSNCD derived datasets are the practical open route. |
| 33 | **Taiwan CWA (ex-CWB) / TSMIP / BATS** | CWA & Academia Sinica | Taiwan | ~700 TSMIP strong-motion + ~100 broadband | ~tens of TB (est.) | GDMS registration; BATS open via FDSN | https://gdmsn.cwa.gov.tw ; http://batsws.earth.sinica.edu.tw/fdsnws/ | FDSNWS (BATS), web (CWA) | |
| 34 | **Korea KMA / KIGAM** | KMA | Korea | ~300 stations | ~tens of TB (est.) | Registration, partial | https://necis.kma.go.kr | Web | |
| 35 | **India NCS** | National Center for Seismology | India | ~150 stations | Catalog open; waveforms limited | Restricted | https://seismo.gov.in | Web | |
| 36 | **Turkey AFAD-TDVMS** | AFAD | Turkey | ~800 strong-motion + ~300 broadband | ~tens of TB (est.) | Registration, free | https://tdvms.afad.gov.tr | Web, FDSNWS (partial) | |
| 37 | **Iran IIEES / IRSC** | IIEES, Tehran Univ. | Iran | ~100+ broadband, strong-motion | ~TB (est.) | Request-based | http://www.iiees.ac.ir ; http://irsc.ut.ac.ir | Web | |
| 38 | **Chile CSN** | Univ. de Chile | Chile | >100 broadband + ~300 accelerometers (C1) | ~tens of TB (est.) | Open via IRIS (C1) | https://www.sismologia.cl | FDSNWS (EarthScope) | |
| 39 | **Mexico SSN** | UNAM | Mexico | >60 broadband + strong motion | ~tens of TB (est.) | Open (registration) | http://www.ssn.unam.mx | FDSNWS | |
| 40 | **Brazil RSBR** | USP/ON/UnB/UFRN | Brazil | ~100 stations | ~tens of TB (est.) | Open | http://rsbr.on.br / http://www.moho.iag.usp.br | FDSNWS | |
| 41 | **South Africa CGS SANSN** | Council for Geoscience | South Africa | >50 stations | ~TB (est.) | Request | https://www.geoscience.org.za | Web | |
| 42 | **Peru IGP** | Instituto Geofísico del Perú | Peru | >100 stations | ~TB (est.) | Partial via IRIS | https://www.igp.gob.pe | Web | |
| 43 | **USArray Transportable Array (TA)** | EarthScope | Contiguous US → Alaska | ~1,700 site footprint, 2004–2021 | ~>100 TB (est.); in S3 bucket | Open | https://ds.iris.edu/ds/nodes/dmc/earthscope/usarray/ | FDSNWS, S3 | Ambient-noise gold standard. |
| 44 | **Volcano observatories: HVO (HV), AVO (AV), CVO (CC), INGV-OE Etna** | USGS / INGV | Hawaii, Alaska, Cascades, Etna | Real-time nets | Each ~tens of TB (est.) | Open | via EarthScope FDSNWS / INGV EIDA | FDSNWS | |
| 45 | **Raspberry Shake (AM network)** | Raspberry Shake / OSOP | Global citizen | >2,000 citizen sensors | ~tens of TB (est.) | Open | https://raspberryshake.org | FDSNWS (`data.raspberryshake.org`) | |

## ML Benchmark Datasets (earthquake)

| # | Name | Host | Region | Type | Size / counts | License / access | URL | Bulk access | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 46 | **STEAD** | Stanford (Mousavi) | Global | 60 s 3C, 100 Hz; picks, coda, noise | **~1.2 M traces; ~85 GB HDF5** | CC-BY-4.0 | https://github.com/smousavi05/STEAD | HTTP chunks, SeisBench | EQTransformer training set. |
| 47 | **INSTANCE** | INGV | Italy | 120 s 3C, 100 Hz | **~1.2 M EQ traces + 130k noise; ~330 GB** | CC-BY-4.0 | https://data.ingv.it/en/dataset/471 | HTTP, SeisBench | |
| 48 | **ETHZ** | SED/ETH | Switzerland | 2013–2020 | ~36k traces | CC-BY | SeisBench | SeisBench | |
| 49 | **GEOFON** | GFZ | Global (2010–2013) | Regional + teleseismic P picks | ~161k traces | CC-BY | SeisBench | SeisBench | |
| 50 | **Iquique** | KIT | N. Chile | 2014 aftershocks | ~13.4k traces | CC-BY | SeisBench | SeisBench | |
| 51 | **LenDB** | Magrini et al. | Global | Local detection | **~1.25 M traces** | CC-BY | https://doi.org/10.5281/zenodo.3676173 | Zenodo / SeisBench | |
| 52 | **SCEDC (SeisBench)** | SCEDC | S. California 2000–2020 | Event windows | ~8 M traces (est.); largest SeisBench set | Open | SeisBench | SeisBench | Also Ross2018, Meier2019 subsets. |
| 53 | **PNW (Ni et al. 2023)** | PNSN/UW | Pacific Northwest | EQ, explosions, exotic (surface events) | **~190k traces + 9.2k exotic** | CC-BY | https://github.com/niyiyu/PNW-ML | SeisBench | |
| 54 | **MLAAPDE** | USGS NEIC | Global | 120 s 3C broadband P/S phases | **>5.1 M recordings**; TB-scale | Public domain | https://doi.org/10.5066/P9OJGE3G | ScienceBase / SeisBench | |
| 55 | **NEIC (Yeck & Patton)** | USGS | Global | Phase arrivals | ~1.3 M phase arrivals | Public domain | SeisBench | SeisBench | |
| 56 | **CREW** | Stanford (Suarez & Beroza 2024) | Global regional | 5-min 3C, P & S labeled | **2.3 M waveforms** | CC-BY | https://doi.org/10.5281/zenodo.11276286 | Zenodo / SeisBench | |
| 57 | **TXED** | UT Austin / TexNet | Texas | 2017–2023 | **~500k traces** | CC-BY | https://github.com/chenyk1990/txed | HTTP / SeisBench | |
| 58 | **CEED** | Berkeley/Stanford (Zhu 2025) | California 2000–2024 | Origins, P/S picks, polarities, GM; NC+SC | several M traces; >1 TB (est.) | Open | https://arxiv.org/abs/2502.11500 | Cloud/AWS + SeisBench | Merges NCEDC+SCEDC for ML. |
| 59 | **DiTing** | CEA/CENC (Zhao et al. 2023) | China 2013–2020 | 180 s, 50 Hz, 3C; P/S + polarity | **2.73 M traces, 787k events** | Open (registration) | https://doi.org/10.1016/j.eqs.2022.01.022 ; https://data.earthquake.cn | HTTP | Also DiTing 2.0 & CSNCD (2024). |
| 60 | **CWA Benchmark (Taiwan)** | CWA (Tang et al. 2024) | Taiwan 2011–2021 | Broadband + strong motion | millions of traces (est.) | Open | SeisBench (CWA, CWANoise) | SeisBench | |
| 61 | **OBS (PickBlue)** | GEOMAR/GFZ | Global oceans | 355 stations, 13,190 events, 109k traces | CC-BY | https://zenodo.org/records/10277799 | Zenodo / SeisBench | |
| 62 | **OBST2024** | Niksejel & Zhang | Global OBS | ~60k waveforms | Open | SeisBench | SeisBench | |
| 63 | **AQ2009** | INGV | L'Aquila 2009 | Aftershock sequence | hundreds of k traces (est.) | CC-BY | SeisBench | SeisBench | |
| 64 | **ISC-EHB DepthPhases** | ISC / SeisBench | Global | Depth phase picks | hundreds of k (est.) | Open | SeisBench | SeisBench | |
| 65 | **LFE stacks (Cascadia, Mexico, San Andreas)** | SeisBench | Various | LFE template stacks | thousands each | Open | SeisBench | SeisBench | |
| 66 | **PiSDL** | SED | CAN/CH/DE/FR | Induced seismicity | tens of k (est.) | Open | SeisBench | SeisBench | |
| 67 | **VCSEIS** | Volcanic | Alaska, Hawaii, Cascades | Volcano seismic classes | hundreds of k (est.) | Open | SeisBench | SeisBench | |
| 68 | **ESM25 (SeisBench)** | ORFEUS ESM | Europe | Strong-motion | ~76k GMs | CC-BY | SeisBench | SeisBench | |
| 69 | **EQSDenoiser, BohemiaSaxony, MLSubDAS** | SeisBench misc. | Various | Denoising; WEBNET; DAS sub-dataset | Various | Mixed | SeisBench | SeisBench | MLSubDAS = first DAS class in SeisBench. |
| 70 | **PhaseNet training data** | Zhu & Beroza 2019 | N. California | 30 s windows from NCEDC | ~780k traces (est.) | Open | https://github.com/AI4EPS/PhaseNet | HTTP | |
| 71 | **QuakeFlow datasets** | AI4EPS | NC/SC/global | Cloud pipelines over NCEDC/SCEDC S3 + CEED | uses S3 archives | Open | https://github.com/AI4EPS/QuakeFlow | S3 | |
| 72 | **SeisLM pretraining set** | Liu et al. 2024 | Global | Foundation model | union of SeisBench datasets; >4 M traces (est.) | Open | https://arxiv.org/abs/2410.15765 | SeisBench | |
| 73 | **Kaggle LANL Earthquake Prediction** | LANL / Kaggle | Lab | Acoustic emission | ~9–10 GB | Kaggle rules | https://www.kaggle.com/c/LANL-Earthquake-Prediction | Kaggle API | Lab quakes. |
| 74 | **SeisBench (all wrapped datasets)** | seisbench | Global | ~45 dataset classes | — | Mixed open | https://seisbench.readthedocs.io/en/stable/pages/documentation/data/waveform_datasets.html | pip + auto download | Canonical loader. |

## DAS (Distributed Acoustic Sensing)

| # | Name | Host | Region | Type | Size / counts | License / access | URL | Bulk access | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 75 | **PubDAS** | Univ. Michigan (Spica, Ajo-Franklin et al. 2023) | Multi | 8 datasets | **~90 TB total (verified)** | Open (CC-BY) | https://pubdas.org (Globus endpoint "PubDAS") | **Globus** | Sub-datasets: PoroTomo/Brady Hot Springs NV (~12–13 TB), Utah FORGE, Stanford Fiber Optic Seismic Observatory (tens of TB), LaSalle IL, Garner Valley CA, Valencia–ISLALINK submarine (Spain), Sandia/Fairbanks, mining. Paper: https://www.osti.gov/pages/biblio/1957924 |
| 76 | **PoroTomo (Brady Hot Springs)** | DOE GDR / Univ. Wisconsin | Nevada | DAS surface + borehole, nodal, vibroseis, 2016 | >12 TB DAS (est.); 8,700 channels | Open (GDR) | https://gdr.openei.org/submissions/980 | GDR HTTP, AWS S3 mirror, PubDAS | |
| 77 | **Utah FORGE DAS** | DOE GDR / Univ. Utah CHPC | Utah | Downhole microseismic DAS (2019, 2022, 2024) | Multi-TB; hosted at CHPC | Open | https://gdr.openei.org/submissions/1185 ; /1680 ; /1725 | HTTP, shell script, PubDAS | |
| 78 | **SAFOD DAS / San Andreas fiber** | Stanford / EarthScope | Parkfield | Borehole DAS | ~TB (est.) | Open (limited) | Via EarthScope/PubDAS | HTTP | |
| 79 | **Stanford DAS Array (SDASA)** | Stanford (Biondi) | Stanford campus | Telecom dark fiber, 2016– | tens of TB (est.) | Open subsets via PubDAS | https://pubdas.org | Globus | |
| 80 | **Ridgecrest DAS** | SCEDC/Caltech | Ridgecrest CA | 2020 fiber, 250 Hz, SEG-Y hourly | TB-scale (est.) | Open | https://scedc.caltech.edu/data/cloud.html | **S3 `s3://scedc-pds`** | |
| 81 | **Rutford Ice Stream DAS / DAS-N2N** | Univ. Bristol / Oxford | Antarctica | 1 km cable, 1 kHz, Jan 2020 | hundreds of GB–TB | CC-BY | https://zenodo.org/records/4778368 ; https://zenodo.org/records/7064405 | Zenodo | Denoising benchmark. |
| 82 | **OOI RCA community DAS (Oregon)** | UW / OOI | Offshore Oregon | Nov 2021 4-day test on two RCA cables; DOI 10.58046/5J60-FJ89 | tens of TB (est.) | Open | https://oceanobservatories.org/pi-instrument/rapid-a-community-test-of-distributed-acoustic-sensing-on-the-ocean-observatories-initiative-regional-cabled-array/ | HTTP | |
| 83 | **Alaska submarine DAS (Quintillion / Oliktok)** | Sandia / Univ. Alaska | Arctic Alaska | Sea-ice, ocean waves | ~TB (est.) | Partial via PubDAS | Via PubDAS | Globus | |
| 84 | **EarthScope DAS holdings (DASDMS)** | EarthScope | Multi | Growing DAS data mgmt system | hundreds of TB (est.) | Open | https://www.earthscope.org/data/das/ | HTTP/S3 planned | |
| 85 | **Zenodo DAS collections (misc.)** | Zenodo | Global | Urban traffic, Athens, Bern, Grimsel, Iceland, MLSubDAS | GB–TB each | CC-BY | https://zenodo.org/search?q=distributed%20acoustic%20sensing | Zenodo | |

## Large-N Nodal Arrays

| # | Name | Host | Region | Type | Size / counts | License / access | URL | Bulk access | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 86 | **Long Beach 3D array** | Signal Hill Petroleum / NodalSeismic | Long Beach CA | 5,200 nodes, 100 m spacing, Jan–Jun 2011 | >20 TB (est.) | Proprietary; subsets via IRIS by request | https://ds.iris.edu | Request | |
| 87 | **Sweetwater TX dense array** | NodalSeismic/Nanometrics/PASSCAL 2014 | Texas | Thousands of nodes + broadband | >10 TB (est.) | Open (PH5) | https://ds.iris.edu/mda/ | PH5 / FDSN | |
| 88 | **SanJac (San Jacinto Fault Zone) nodal** | UCSD (Ben-Zion) | S. California | 1,100 nodes, 2014 | few TB (est.) | Open (PH5) | EarthScope network YN/ZG | PH5 | |
| 89 | **iMUSH (Mount St Helens)** | Rice/UW (XD 2014) | Washington | ~900 nodes + 70 broadband | several TB (est.) | Open | https://ds.iris.edu | PH5/FDSN | |
| 90 | **Dead Sea / Jordan dense array** | Ben-Zion et al. 2015 | Israel/Jordan | ~1,100 nodes | ~TB (est.) | Open (PH5) | EarthScope | PH5 | |
| 91 | **ChinArray (Phase I–III)** | CEA | China | >2,000 broadband per phase | PB-class (est.) | **Restricted** | http://www.chinarraydmc.cn | Request | |
| 92 | **AlpArray / AdriaArray** | ORFEUS EIDA | Alps/Adria | ~600 broadband 2015–2019; AdriaArray 2022– | >50 TB (est.) | Open | https://www.alparray.ethz.ch | EIDA FDSNWS | |
| 93 | **PASSCAL/EarthScope nodal archive (PH5)** | EarthScope | Global | >100 experiments | hundreds of TB (est.) | Open | https://ds.iris.edu/ds/nodes/dmc/data/formats/ph5/ | PH5 web services | |

## Strong-Motion Databases

| # | Name | Host | Region | Size / counts | License / access | URL | Notes |
|---|---|---|---|---|---|---|---|
| 94 | **NGA-West2** | PEER, Berkeley | Global shallow-crustal | ~21,300 3C records, ~600 events | Registration; **paid membership from July 2026**; 200 records/2 wk cap | https://ngawest2.berkeley.edu | |
| 95 | **NGA-East / NGA-Sub** | PEER | CENA / subduction | NGA-Sub ~70k records (est.) | Same terms | https://peer.berkeley.edu/research/nga-sub | |
| 96 | **ESM (Engineering Strong Motion DB)** | INGV/ORFEUS | Europe & Mediterranean | **76,242 GMs, 9,927 stations, 1,391 events** | CC-BY (registration) | https://esm-db.eu | Web services esm-db.eu/esmws |
| 97 | **ITACA v4** | INGV | Italy | >60k records (est.) | CC-BY | https://itaca.mi.ingv.it | |
| 98 | **RESORCE** | SIGMA project | Europe/Middle East | ~5,900 records | Free registration | http://www.resorce-portal.eu | |
| 99 | **CESMD** | USGS/CGS/ANSS | USA + international | tens of k records; 2,000+ stations | Public domain | https://www.strongmotioncenter.org | |
| 100 | **K-NET / KiK-net** | NIED | Japan | >1 M records | Registration | https://www.kyoshin.bosai.go.jp/en/ | Largest globally. |
| 101 | **GeoNet strong motion** | GNS | New Zealand | tens of k events | CC BY 3.0 NZ | https://www.geonet.org.nz/data/types/strong_motion | S3 `seismic-products/strong-motion` |
| 102 | **AFAD TDVMS** | AFAD | Turkey | >100k records (est.) | Registration | https://tdvms.afad.gov.tr | |
| 103 | **AGMD Australian Ground-Motion DB** | GA (2025) | Australia | thousands | Open | https://pubs.geoscienceworld.org/ssa/srl/article/doi/10.1785/0220250316 | |

## Planetary & Ocean

| # | Name | Host | Region | Type | Size | License / access | URL | Bulk access |
|---|---|---|---|---|---|---|---|---|
| 104 | **InSight SEIS (Mars)** | NASA PDS Geosciences Node; mirrored EarthScope (XB) & IPGP | Mars | VBB + SP seismometer 2018–2022; ~1,300 marsquakes | hundreds of GB–<1 TB | Public domain | https://pds-geosciences.wustl.edu/missions/insight/seis.htm | HTTP (PDS), FDSNWS (XB) |
| 105 | **Apollo PSE (ALSEP lunar seismic)** | PDS + EarthScope (XA) | Moon | Apollo 11–17, 1969–1977; ~13,000 events | tens of GB | Public domain | https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_pse | HTTP (PDS), FDSNWS (XA) |
| 106 | **Viking 2 seismometer (Mars 1976–78)** | NASA PDS/NSSDC | Mars | Lander-mounted | ~MB | Public domain | https://pds-geosciences.wustl.edu/missions/vlander/ | HTTP |
| 107 | **OOI Regional Cabled Array (RCA)** | OOI/UW | Cascadia/Axial Seamount | Broadband & short-period OBS, hydrophones, 2014– | >100 TB all streams (est.) | Open (CC-BY) | https://oceanobservatories.org ; network OO at EarthScope | FDSNWS, OOI raw HTTP |
| 108 | **ONC NEPTUNE / VENUS** | Ocean Networks Canada | NE Pacific | Cabled OBS (network NV), hydrophones | >1 PB all ONC (est.); seismic tens of TB | Open (registration) | https://data.oceannetworks.ca | Oceans 3.0 API, FDSNWS |
| 109 | **OBSIC OBS deployments** | EarthScope | Global oceans | Cascadia Initiative 7D, Alaska Amphibious XO, etc. | tens of TB (est.) | Open | https://ds.iris.edu | FDSNWS |
| 110 | **OSDC (SUSTech Ocean Seismic Data Center)** | SUSTech, China | S. China Sea | OBS archive | ~TB (est.) | Partial | https://obslab.sustech.edu.cn/mda/ | FDSNWS |

## Top 15 by size

| Rank | Archive | Approx. size | Basis |
|---|---|---|---|
| 1 | EarthScope/IRIS DMC | **>1 PB** miniSEED (+ PH5 nodal + DAS) | verified |
| 2 | NIED MOWLAS combined (Hi-net + F-net + K/KiK-net + S-net + DONET) | ~1 PB (est.) | station counts |
| 3 | ORFEUS EIDA federation | ~1 PB aggregate (est.) | sum of nodes |
| 4 | CEA/CENC + ChinArray | PB-class (est.), largely restricted | station counts |
| 5 | All cloud/community DAS (EarthScope DAS + AWS + PubDAS) | "surpassing PBs"; PubDAS 90 TB verified | verified/est. |
| 6 | GEOFON (GFZ) | ~400+ TB (est.) | largest EIDA node |
| 7 | Ocean Networks Canada (all streams) | ~PB (est.) | est. |
| 8 | EPOS-France / RESIF | ~300 TB (est.) | est. |
| 9 | INGV EIDA | ~300 TB (est.) | est. |
| 10 | NCEDC | **184–190 TB** | verified |
| 11 | SCEDC | **~150 TB** on S3 | verified |
| 12 | GeoNet NZ | ~100+ TB | est. from 12 GB/day |
| 13 | USArray TA | ~100+ TB | est. |
| 14 | PubDAS | **~90 TB** | verified |
| 15 | OOI RCA | ~100 TB (est.) | est. |

## Key findings

- **Cloud-native open archives on AWS S3 (all `--no-sign-request`)**: EarthScope (`s3://earthscope-geophysical-data`, us-east-2), SCEDC (`s3://scedc-pds`, us-west-2), NCEDC (`s3://ncedc-pds`, us-east-2), GeoNet (`s3://geonet-open-data`, ap-southeast-2) — **~1.3 PB of miniSEED total on S3**.
- **Japan (NIED)** is the largest non-cloud archive but requires registration, WIN32 format, 50 MB/request cap, no redistribution.
- **China** raw waveforms are effectively closed to non-Chinese users; DiTing / CSNCD benchmarks are the practical route.
- **NGA-West2** moves to paid membership on 2 July 2026.
- **SeisBench** wraps ~45 dataset classes and is the canonical loader for ML benchmarks.
- **PubDAS** (~90 TB, Globus) is the main open DAS repository; the largest single DAS sets (FORGE, PoroTomo) live on DOE GDR / Utah CHPC and AWS.
