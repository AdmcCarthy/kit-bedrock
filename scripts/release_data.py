"""Upload the big layer files to a GitHub release, so Pages stays small.

The author's publishing step moves every layer file over BIG_BYTES (scripts/data_release.py) to dist/<DATA_TAG>/ and points the
region's layers.json at site/release/. This script creates the release (or reuses it) and uploads the files with --clobber, so a
republish replaces them in place. The Pages workflow downloads them again before it deploys (scripts/fetch_release.py).

Usage: python scripts/release_data.py   (needs the GitHub CLI, signed in)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_release import DATA_TAG, DIST  # noqa: E402

REPO = "AdmcCarthy/kit-bedrock"


def main() -> None:
    files = sorted(p for p in DIST.glob("*") if p.is_file())
    if not files:
        raise SystemExit(f"nothing in {DIST}; publish the layers first")
    have = subprocess.run(["gh", "release", "view", DATA_TAG, "--repo", REPO], capture_output=True, text=True).returncode == 0
    if not have:
        subprocess.run(["gh", "release", "create", DATA_TAG, "--repo", REPO, "--title", f"Layer files {DATA_TAG}",
                        "--notes", "Display layers too large for Pages: detail-level bedrock TopoJSON and slope-flow lines. Written by the author's publishing step; terms in DATA-LICENCE.md."], check=True)
    total = sum(p.stat().st_size for p in files) / 1e6
    subprocess.run(["gh", "release", "upload", DATA_TAG, *map(str, files), "--repo", REPO, "--clobber"], check=True)
    print(f"{len(files)} files, {total:.0f} MB, on release {DATA_TAG}")


if __name__ == "__main__":
    main()
