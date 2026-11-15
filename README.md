# Bedrock

[![Pages](https://github.com/AdmcCarthy/kit-bedrock/actions/workflows/pages.yml/badge.svg)](https://github.com/AdmcCarthy/kit-bedrock/actions/workflows/pages.yml)
[![Licence](https://img.shields.io/badge/licence-MIT%20with%20acknowledgement-lightgrey)](LICENSE)

A public gallery, in Relief's manner, of open geological maps read into one language and of the catchments that erode them, drawn with D3 at several levels of detail with every display type the pipelines offer. Live at https://admccarthy.github.io/kit-bedrock/ once Pages has deployed.

| Page | What | Views |
| :--- | :--- | :--- |
| `geology.html?r=<region>` | A bedrock region at overview, regional and detail levels | age (chart, vintage or paper palette), lithology, age with rock as hatch, rock with age as tone, fjord ramp; plain or vintage frame; hillshade strength on Relief frames |
| `s2s.html?r=<region>` | A source-to-sink region: catchments, rivers, outlets on Relief terrain | bedrock group, sand quality, yield, sand supply, shield and carbonate shares, size classes with a fold; rivers, flow lines, slope flow; strong or subtle ink |

Regions: Norway, Britain and Ireland, the North Sea, Fennoscandia, Austria and an open-licence North-east Europe for bedrock; the North Sea, the Norwegian Sea and North-east Europe for source to sink.

The layers are published from the author's private pipelines (`europe-gis-data`, `kit-geology-maps`, `source-to-sink`) by `scripts/publish.py`, which copies only regions whose every map carries an open licence for display and writes the sources into `site/manifest.json`. `DATA-LICENCE.md` is the record of terms. The site is static. The big layer files (detail-level TopoJSON and slope-flow lines, about 50 MB) are assets of the GitHub release `data-2026-11-10`, not in git: `scripts/release_data.py` uploads them, the Pages workflow downloads them into `site/release/` before it deploys, and `python scripts/fetch_release.py` does the same for a local preview. GitHub Pages then serves `site/` as it is.

Add `&theme=light` or `&theme=dark` to a page address to force a theme; the other options are buttons on the page.

## Licence and acknowledgement

MIT License with Acknowledgement ([LICENSE](LICENSE)): the MIT terms plus one condition. Anything built with this work says so,
visibly and in plain words, and does not imply endorsement: "Built with kit-bedrock by Adam McCarthy (https://github.com/AdmcCarthy/kit-bedrock)". The wording is custom, so
the licence is not OSI-approved. Data terms are in DATA-LICENCE.md; layers derived from third-party maps keep their own terms and attribution.
