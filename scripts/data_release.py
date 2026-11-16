"""Where the big layer files live: the release that holds them, how large a file may be before it moves there, and the path the layers use.

A layer file over BIG_BYTES is not kept in git. It is a release asset: the author's publishing step collects such files in
dist/<DATA_TAG>/ (scripts/release_data.py uploads them) and the Pages workflow downloads them into site/release/ again before it
deploys (scripts/fetch_release.py does the same for a local preview). The pages fetch them from their own origin, because GitHub's
release downloads send no CORS header and a browser cannot fetch them directly.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_TAG = "data-2026-11-10"
BIG_BYTES = 2_500_000  # a layer file over this size is a release asset
RELEASE_PATH = "../../../release/"  # from a region's folder, site/data/<kind>/<region>/, to site/release/
DIST = ROOT / "dist" / DATA_TAG
