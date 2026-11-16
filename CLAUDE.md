# Bedrock: working rules

@../../shared/idiom/CORE.md

Voice and dataset terms follow Idiom (`CORE.md`, `DATASETS.md`; private repo, normally linked at `../../shared/idiom`). The import is harmless when the file is absent. Public repo: never copy anything from Idiom's `personal/` or `working/` folders here.

A static public gallery of display layers from the author's private geology-map and source-to-sink pipelines, on Relief terrain. Owner: Adam McCarthy.

- The layers under `site/data/`, the reduced frames under `site/relief/` and `site/manifest.json` are finished files written here by the author's private pipelines, which copy only allow-listed regions whose every map has an open licence for display. This repo does not regenerate them and depends on nothing private; never copy layer files by hand.
- A map whose licence is unverified or restricts display is not published, whatever its value. `DATA-LICENCE.md` lists what is shown and what is held back; keep it in step with Idiom `DATASETS.md`.
- The viewers (the pages, `site/geology.js`, `site/s2s.js`, `site/style.css`, `site/palettes.json`) belong to this repo: change them here.
- Relief's hillshade and bands are copied reduced with Relief's attribution; nothing else of Relief's data is copied.
- Screenshots in `site/shots/` are WebP made by `scripts/shots.py` (`uv run python scripts/shots.py`) with headless Chrome; look at them before publishing.
- The site is static: `python -m http.server` in `site/` shows it; GitHub Pages serves `site/` from `.github/workflows/pages.yml`.
