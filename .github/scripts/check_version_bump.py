#!/usr/bin/env python3
"""Fail if a plugin changed on this branch without a version bump.

Clients only pull a plugin update when its version increases, so a fix
shipped without a bump reaches nobody. Compares each touched plugin's
plugin.json version against the base ref.

Usage: check_version_bump.py --base origin/main
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout


def parse_semver(v: str) -> tuple[int, int, int]:
    a, b, c = (int(x) for x in v.split("."))
    return a, b, c


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    args = ap.parse_args()

    changed = git("diff", "--name-only", f"{args.base}...HEAD").split()
    touched = sorted(
        {p.split("/")[1] for p in changed if p.startswith("plugins/") and p.count("/") >= 2}
    )
    if not touched:
        print("no plugins touched")
        return 0

    failures = 0
    for name in touched:
        pj = f"plugins/{name}/.claude-plugin/plugin.json"
        try:
            old = json.loads(git("show", f"{args.base}:{pj}")).get("version")
        except subprocess.CalledProcessError:
            print(f"{name}: new plugin, no bump required")
            continue
        new_path = ROOT / pj
        if not new_path.exists():
            print(f"{name}: removed")
            continue
        new = json.loads(new_path.read_text()).get("version")
        if parse_semver(str(new)) <= parse_semver(str(old)):
            print(f"{name}: version {old} -> {new} did not increase")
            failures += 1
        else:
            print(f"{name}: {old} -> {new}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
