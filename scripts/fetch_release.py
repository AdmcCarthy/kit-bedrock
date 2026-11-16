"""Download the release assets that the layers point at into site/release/, so the gallery works from a plain checkout.

The Pages workflow does this before it deploys; run it by hand to preview locally. The release tag is DATA_TAG in
scripts/data_release.py. Public repository: no token needed.

Usage: python scripts/fetch_release.py
"""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "AdmcCarthy/kit-bedrock"


def main() -> None:
    tag = re.search(r'^DATA_TAG = "([^"]+)"', (ROOT / "scripts" / "data_release.py").read_text(encoding="utf-8"), re.M).group(1)
    with urllib.request.urlopen(f"https://api.github.com/repos/{REPO}/releases/tags/{tag}") as r:
        assets = json.load(r)["assets"]
    dest = ROOT / "site" / "release"
    dest.mkdir(parents=True, exist_ok=True)
    for a in assets:
        out = dest / a["name"]
        if out.exists() and out.stat().st_size == a["size"]:
            continue
        urllib.request.urlretrieve(a["browser_download_url"], out)
    print(f"{len(assets)} files from release {tag} in {dest}")


if __name__ == "__main__":
    main()
