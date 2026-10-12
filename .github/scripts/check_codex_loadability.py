#!/usr/bin/env python3
"""Prove Codex discovers every marketplace plugin and every bundled skill."""

from __future__ import annotations

import argparse
import json
import os
import select
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, TextIO

ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE = Path(".claude-plugin/marketplace.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=ROOT)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=float, default=30.0)
    return parser.parse_args()


def read_message(stream: TextIO, timeout: float) -> dict[str, Any]:
    ready, _, _ = select.select([stream], [], [], timeout)
    if not ready:
        raise RuntimeError(f"timed out after {timeout:g}s waiting for Codex app-server")
    line = stream.readline()
    if not line:
        raise RuntimeError("Codex app-server closed stdout unexpectedly")
    payload = json.loads(line)
    if not isinstance(payload, dict):
        raise RuntimeError("Codex app-server returned a non-object JSON-RPC message")
    return payload


def send_message(stream: TextIO, payload: dict[str, Any]) -> None:
    stream.write(json.dumps(payload, separators=(",", ":")) + "\n")
    stream.flush()


def request(
    process: subprocess.Popen[str],
    request_id: int,
    method: str,
    params: dict[str, Any],
    timeout: float,
) -> Any:
    if process.stdin is None or process.stdout is None:
        raise RuntimeError("Codex app-server pipes were not created")
    send_message(
        process.stdin,
        {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params},
    )
    deadline = time.monotonic() + timeout
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise RuntimeError(f"timed out waiting for {method}")
        message = read_message(process.stdout, remaining)
        if message.get("id") != request_id:
            continue
        if "error" in message:
            raise RuntimeError(
                f"Codex {method} returned an error:\n"
                + json.dumps(message["error"], indent=2, sort_keys=True)
            )
        return message.get("result")


def expected_skills(plugin_root: Path) -> set[str]:
    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        return set()
    return {path.parent.name for path in skills_root.glob("*/SKILL.md")}


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    binary = shutil.which(args.codex_bin)
    if binary is None:
        raise RuntimeError(f"Codex executable not found: {args.codex_bin}")

    marketplace_path = repo / MARKETPLACE
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    marketplace_name = marketplace["name"]
    plugins = marketplace["plugins"]

    with tempfile.TemporaryDirectory(prefix="zero-lab-codex-") as temp:
        temp_root = Path(temp)
        home = temp_root / "home"
        codex_home = temp_root / "codex"
        home.mkdir()
        codex_home.mkdir()
        (codex_home / "config.toml").write_text(
            "[features]\nplugins = true\nplugin_hooks = true\n",
            encoding="utf-8",
        )
        env = os.environ.copy()
        env.update({"HOME": str(home), "CODEX_HOME": str(codex_home)})
        process = subprocess.Popen(
            [
                binary,
                "app-server",
                "--listen",
                "stdio://",
                "--enable",
                "plugins",
                "--enable",
                "plugin_hooks",
            ],
            cwd=repo,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        try:
            request(
                process,
                1,
                "initialize",
                {
                    "clientInfo": {
                        "name": "zero-lab-loadability",
                        "version": "1.0.0",
                    },
                    "capabilities": {"experimentalApi": True},
                },
                args.timeout,
            )
            if process.stdin is None:
                raise RuntimeError("Codex app-server stdin was not created")
            send_message(
                process.stdin,
                {"jsonrpc": "2.0", "method": "initialized", "params": {}},
            )

            listing = request(
                process,
                2,
                "plugin/list",
                {
                    "cwds": [str(repo)],
                    "forceRefetch": False,
                    "marketplaceKinds": ["local"],
                },
                args.timeout,
            )
            if not isinstance(listing, dict):
                raise RuntimeError("Codex plugin/list returned an invalid result")
            load_errors = listing.get("marketplaceLoadErrors", [])
            if load_errors:
                raise RuntimeError(
                    "Codex reported marketplace load errors:\n"
                    + json.dumps(load_errors, indent=2, sort_keys=True)
                )
            marketplaces = listing.get("marketplaces", [])
            local_marketplace = next(
                (
                    entry
                    for entry in marketplaces
                    if isinstance(entry, dict) and entry.get("name") == marketplace_name
                ),
                None,
            )
            if local_marketplace is None:
                raise RuntimeError(f"Codex did not discover marketplace {marketplace_name!r}")
            listed_plugins = {
                plugin["name"]
                for plugin in local_marketplace.get("plugins", [])
                if isinstance(plugin, dict) and isinstance(plugin.get("name"), str)
            }
            expected_plugins = {plugin["name"] for plugin in plugins}
            missing_plugins = expected_plugins - listed_plugins
            if missing_plugins:
                raise RuntimeError(
                    "Codex marketplace omitted plugins: " + ", ".join(sorted(missing_plugins))
                )

            loaded_skills = 0
            for request_id, plugin in enumerate(plugins, start=3):
                plugin_root = (repo / plugin["source"]).resolve()
                skill_names = {f"{plugin['name']}:{name}" for name in expected_skills(plugin_root)}
                detail = request(
                    process,
                    request_id,
                    "plugin/read",
                    {
                        "marketplacePath": str(marketplace_path),
                        "remoteMarketplaceName": None,
                        "pluginName": plugin["name"],
                    },
                    args.timeout,
                )
                if not isinstance(detail, dict) or not isinstance(detail.get("plugin"), dict):
                    raise RuntimeError(
                        f"Codex plugin/read returned invalid detail for {plugin['name']}"
                    )
                loaded = detail["plugin"].get("skills", [])
                loaded_names = {
                    skill["name"]
                    for skill in loaded
                    if isinstance(skill, dict) and isinstance(skill.get("name"), str)
                }
                if loaded_names != skill_names:
                    missing = sorted(skill_names - loaded_names)
                    unexpected = sorted(loaded_names - skill_names)
                    raise RuntimeError(
                        f"Codex loaded the wrong skills for {plugin['name']}: "
                        f"missing={missing}, unexpected={unexpected}"
                    )
                loaded_skills += len(loaded_names)
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
            if process.returncode not in (0, -15):
                stderr = process.stderr.read() if process.stderr else ""
                if stderr:
                    print(stderr, file=sys.stderr, end="")

    print(f"Codex loaded {len(plugins)} plugins and {loaded_skills} skills from {marketplace_name}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, OSError, RuntimeError, TypeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
