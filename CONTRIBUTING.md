# Contributing

Corrections are more valuable here than additions. A catalogue whose sizes and links
are wrong is worse than no catalogue — so the bar for *adding* is "does it exist and
is it reachable", and the bar for *asserting a number* is "did you measure it".

## The one rule that matters

**Never write a number or URL you have not verified.**

An empty `size_bytes` with a note is correct. A plausible-looking rounded figure is
not. Six published sizes were found wrong during the original survey, by margins from
4× to 460×, and every one of them erred *large*. Assume the published figure is wrong
until you have measured it.

```bash
curl -sIL "https://example.org/survey.sgy" | grep -i content-length
```

If the server refuses `HEAD`, try a ranged `GET`:

```bash
curl -sL -r 0-0 -D - -o /dev/null "https://example.org/survey.sgy" | grep -i content-range
```

For S3 and GCS, list the prefix and sum it — don't trust the landing page.

## Adding or correcting an entry

1. Edit [`catalog/datasets.yaml`](catalog/datasets.yaml). The schema is documented in
   [`catalog/SCHEMA.md`](catalog/SCHEMA.md).
2. Run the checks:

   ```bash
   python scripts/check_usage.py      # must pass with 0 errors
   python scripts/build_readme.py     # regenerates CATALOG.md
   ```

3. If you touched a CSV, rebuild the workbook:

   ```bash
   python scripts/build_workbook.py
   ```

4. Open a PR describing **how** you verified — the command you ran, the header you
   read, the API you queried. "Checked the website" is not verification.

Do not hand-edit `CATALOG.md`; it is generated.

## Field conventions

**Sizes.** `size_bytes` is exact or absent. Ranges go in `size_bytes_min` /
`size_bytes_max`. Decimal (GB/TB) and binary (GiB/TiB) units are distinct and are not
interchanged — DOE GDR labels binary units as "TB", which is exactly how a 187 TB
figure turned out to mean something else.

**Usage rights.** Five axes: `commercial`, `redistribution`, `attribution_required`,
`share_alike`, `ml_training`. Every value is `yes`, `no`, or `unclear`.

- `unclear` is the default. A right is asserted only when the holder's text grants it.
  **Silence is recorded as silence, never as permission.**
- **Cost is not a restriction.** A media or handling fee is an `access` property. It
  never sets `commercial: "no"` on its own. Use `commercial: "no"` only where the
  holder genuinely gates commercial use — an NC licence, an explicit non-commercial
  condition, or "free for academia, fee for industry".
- Watch for licence strings that name a *software* licence alongside *data* terms.
  The Equinor Open Data Licence text ends by mentioning Apache-2.0 tooling; the data
  is still academic-use-only.
- Watch for laundering. One Zenodo record declares CC-BY-4.0 while repackaging
  CC BY-NC-SA upstream data. Record `unclear` and note the conflict.

**Dead ends are contributions.** If you establish that a widely-cited dataset is *not*
downloadable, that is worth a PR. `docs/` records several — Kansas Geological Survey
has never published a single `.sgy` file, and proving that took an Internet Archive
CDX sweep of the site's entire history.

## Reporting a broken link

```bash
python scripts/check_links.py --json report.json
```

Open an issue with the relevant rows. Note that `blocked` is not `dead` — several
government hosts (SEG wiki, Sodir, USGS NAMSS) refuse automated requests while working
fine in a browser. The checker labels those separately for that reason.

## Scope

**In scope:** open or potentially accessible seismic data — exploration reflection
(2D/3D/4D, pre- and post-stack), national archives, academic marine and crustal,
earthquake and passive waveforms, DAS, strong motion, planetary, plus ML-ready and
synthetic benchmark datasets.

**Out of scope:** commercial data libraries with no public tier, datasets requiring a
negotiated contract, and non-seismic geophysics (gravity, magnetics, EM) unless bundled
with seismic. Closed archives are catalogued as `closed` when knowing they're closed
saves someone a search.

## Prefer institutional hosts

When a dataset is available from more than one place, link the institutional
repository rather than a vendor page or a cloud-drive folder. The measured evidence:
the SEG wiki's Open Data page has 28% dead links, while `awesome-das` — untouched
since 2022 — has zero, because it points at institutional repositories. Where you link
determines whether the entry survives.
