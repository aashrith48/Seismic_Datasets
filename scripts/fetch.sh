#!/usr/bin/env bash
# Download helper for the openly-hosted seismic datasets in this catalog.
#
#   ./scripts/fetch.sh list                 # show what can be fetched
#   ./scripts/fetch.sh <name> [DEST]        # fetch one
#   ./scripts/fetch.sh all-nz  [DEST]       # fetch a group
#
# Only covers datasets with a stable, no-account download path. Everything else
# needs a portal login or an emailed order — see the README.
set -euo pipefail

DEST_DEFAULT="./data"
NZ_BUCKET="http://s3.amazonaws.com/open.source.geoscience/open_data/newzealand/Taranaiki_Basin"

have() { command -v "$1" >/dev/null 2>&1; }

get() { # get <url> <outfile>
  local url="$1" out="$2"
  mkdir -p "$(dirname "$out")"
  if [ -f "$out" ]; then
    echo "  exists, skipping: $out"
    return 0
  fi
  echo "  -> $out"
  if have curl; then
    curl -fL --retry 3 --retry-delay 5 -C - -o "$out.part" "$url"
  elif have wget; then
    wget -c -O "$out.part" "$url"
  else
    echo "need curl or wget" >&2; exit 1
  fi
  mv "$out.part" "$out"
}

s3sync() { # s3sync <s3-uri> <destdir>
  if ! have aws; then
    echo "aws CLI not found — install it, or browse: ${1/s3:\/\//https://}.s3.amazonaws.com/index.html" >&2
    return 1
  fi
  mkdir -p "$2"
  echo "  -> aws s3 sync $1 $2 (no credentials needed)"
  aws s3 sync "$1" "$2" --no-sign-request
}

usage() {
  cat <<'EOF'
Fetchable targets (no account required):

  NEW ZEALAND (SEG-Y, open.source.geoscience S3)
    parihaka-full      Parihaka 3D full angle stack           5.1 GB
    parihaka-angles    Parihaka near+mid+far angle stacks    15.3 GB
    parihaka           all four Parihaka volumes             20.4 GB
    kerry              Kerry 3D PSTM                          1.1 GB
    opunake            Opunake 3D final stack                10.4 GB
    all-nz             everything above                      ~31.9 GB

  AUSTRALIA
    poseidon-mdio      Poseidon 3D, MDIO/zarr (TGS, CC BY 4.0, S3)

  PASSIVE / EARTHQUAKE (AWS Open Data, requester pays nothing)
    scedc-info         print SCEDC S3 usage
    ncedc-info         print NCEDC S3 usage
    earthscope-info    print EarthScope S3 usage
    geonet-info        print GeoNet S3 usage

Usage: ./scripts/fetch.sh <target> [DEST_DIR]
EOF
}

target="${1:-}"; dest="${2:-$DEST_DEFAULT}"

case "$target" in
  ""|list|-h|--help|help) usage ;;

  parihaka-full)
    get "$NZ_BUCKET/PARIHAKA-3D/Parihaka_PSTM_full_angle.sgy" \
        "$dest/nz/parihaka/Parihaka_PSTM_full_angle.sgy" ;;

  parihaka-angles)
    for s in near mid far; do
      get "$NZ_BUCKET/PARIHAKA-3D/Parihaka_PSTM_${s}_stack.sgy" \
          "$dest/nz/parihaka/Parihaka_PSTM_${s}_stack.sgy"
    done ;;

  parihaka)
    "$0" parihaka-full "$dest"; "$0" parihaka-angles "$dest" ;;

  kerry)
    # upstream really does spell the directory "Keri_3D"
    get "$NZ_BUCKET/Keri_3D/Kerry3D.segy" "$dest/nz/kerry/Kerry3D.segy" ;;

  opunake)
    get "$NZ_BUCKET/OPUNAKE-3D/OPUNAKE3D-PR3461-FS.3D.Final_Stack.sgy" \
        "$dest/nz/opunake/OPUNAKE3D-PR3461-FS.3D.Final_Stack.sgy" ;;

  all-nz)
    "$0" parihaka "$dest"; "$0" kerry "$dest"; "$0" opunake "$dest" ;;

  poseidon-mdio)
    s3sync "s3://tgs-opendata-poseidon" "$dest/au/poseidon" ;;

  scedc-info)
    echo "SCEDC (~150 TB, us-west-2):  aws s3 ls s3://scedc-pds/ --no-sign-request" ;;
  ncedc-info)
    echo "NCEDC (~190 TB, us-east-2):  aws s3 ls s3://ncedc-pds/ --no-sign-request" ;;
  earthscope-info)
    echo "EarthScope (>1 PB, us-east-2): aws s3 ls s3://earthscope-geophysical-data/ --no-sign-request"
    echo "  networks include AK II IU N4 PB TA UU UW" ;;
  geonet-info)
    echo "GeoNet NZ (CC BY 3.0 NZ, ap-southeast-2): aws s3 ls s3://geonet-open-data/ --no-sign-request" ;;

  *)
    echo "unknown target: $target" >&2; echo >&2; usage >&2; exit 1 ;;
esac
