#!/usr/bin/env python3
"""Prove Claude Code can discover and install every marketplace plugin."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE = Path(".claude-plugin/marketplace.json")
MANIFEST = Path(".claude-plugin/plugin.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=ROOT)
    parser.add_argument("--claude-bin", default="claude")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_claude(
    binary: str,
    args: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [binary, *args],
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        detail = "\n".join(part for part in (result.stdout, result.stderr) if part)
        raise RuntimeError(f"claude {' '.join(args)} failed:\n{detail}")
    return result


def plugin_ids(payload: Any, *, section: str | None = None) -> set[str]:
    original = payload
    if isinstance(payload, dict):
        payload = payload.get(section) if section else None
    if not isinstance(payload, list):
        raise RuntimeError(
            "claude plugin list --json returned an unexpected shape:\n"
            + json.dumps(original, indent=2, sort_keys=True)
        )
    return {
        plugin_id
        for entry in payload
        if isinstance(entry, dict)
        for plugin_id in (entry.get("id") or entry.get("pluginId"),)
        if isinstance(plugin_id, str)
    }


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    binary = shutil.which(args.claude_bin)
    if binary is None:
        raise RuntimeError(f"Claude Code executable not found: {args.claude_bin}")

    marketplace_path = repo / MARKETPLACE
    marketplace = load_json(marketplace_path)
    marketplace_name = marketplace["name"]
    plugins = marketplace["plugins"]
    expected_ids = {f"{plugin['name']}@{marketplace_name}" for plugin in plugins}

    with tempfile.TemporaryDirectory(prefix="zero-lab-claude-") as temp:
        temp_root = Path(temp)
        env = os.environ.copy()
        env.update(
            {
                "HOME": str(temp_root / "home"),
                "CLAUDE_CONFIG_DIR": str(temp_root / "claude-config"),
            }
        )
        Path(env["HOME"]).mkdir()
        Path(env["CLAUDE_CONFIG_DIR"]).mkdir()

        run_claude(
            binary,
            ["plugin", "validate", "--strict", str(marketplace_path)],
            cwd=repo,
            env=env,
        )
        for plugin in plugins:
            manifest = repo / plugin["source"] / MANIFEST
            run_claude(
                binary,
                ["plugin", "validate", "--strict", str(manifest)],
                cwd=repo,
                env=env,
            )

        run_claude(
            binary,
            ["plugin", "marketplace", "add", str(repo)],
            cwd=repo,
            env=env,
        )
        available = json.loads(
            run_claude(
                binary,
                ["plugin", "list", "--available", "--json"],
                cwd=repo,
                env=env,
            ).stdout
        )
        missing_available = expected_ids - plugin_ids(available, section="available")
        if missing_available:
            raise RuntimeError(
                "Claude marketplace omitted plugins: " + ", ".join(sorted(missing_available))
            )

        for plugin_id in sorted(expected_ids):
            run_claude(
                binary,
                ["plugin", "install", "--scope", "user", plugin_id],
                cwd=repo,
                env=env,
            )

        installed = json.loads(
            run_claude(
                binary,
                ["plugin", "list", "--json"],
                cwd=repo,
                env=env,
            ).stdout
        )
        missing_installed = expected_ids - plugin_ids(installed)
        if missing_installed:
            raise RuntimeError(
                "Claude failed to install plugins: " + ", ".join(sorted(missing_installed))
            )

        plugin_errors = {
            entry["id"]: entry["errors"]
            for entry in installed
            if isinstance(entry, dict) and entry.get("id") in expected_ids and entry.get("errors")
        }
        if plugin_errors:
            raise RuntimeError(
                "Claude reported plugin load errors:\n"
                + json.dumps(plugin_errors, indent=2, sort_keys=True)
            )

    print(f"Claude loaded {len(expected_ids)} plugins from {marketplace_name}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, OSError, RuntimeError, TypeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
