#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check proposed IP targets against an explicit authorization manifest.

Input JSON:
{
  "authorized": ["10.0.0.0/24", "2001:db8::/64"],
  "excluded": ["10.0.0.64/27"],
  "targets": ["10.0.0.12", "10.0.0.128/26"]
}

A target is authorized only when its entire IP or CIDR range is contained in
an authorized range and it does not overlap an exclusion. Hostnames are not
resolved: the checker is deterministic and makes no network calls.

Exit codes: 0 = every target authorized; 1 = scope violation; 2 = invalid or
empty input.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import sys
from pathlib import Path
from typing import Any

Network = ipaddress.IPv4Network | ipaddress.IPv6Network


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("manifest must be a JSON object")
    return data


def parse_list(data: dict[str, Any], field: str, *, required: bool) -> list[tuple[str, Network]]:
    raw = data.get(field)
    if raw is None and not required:
        raw = []
    if not isinstance(raw, list) or (required and not raw):
        qualifier = "a non-empty" if required else "an"
        raise ValueError(f"{field} must be {qualifier} array")

    parsed: list[tuple[str, Network]] = []
    for value in raw:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field} entries must be non-empty IP or CIDR strings")
        try:
            network = ipaddress.ip_network(value.strip(), strict=False)
        except ValueError as exc:
            raise ValueError(f"invalid {field} entry {value!r}: {exc}") from exc
        parsed.append((value.strip(), network))
    return parsed


def fully_contained(target: Network, authorized: Network) -> bool:
    return target.version == authorized.version and target.subnet_of(authorized)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="scope manifest JSON")
    args = parser.parse_args()

    try:
        data = load_manifest(args.manifest)
        authorized = parse_list(data, "authorized", required=True)
        excluded = parse_list(data, "excluded", required=False)
        targets = parse_list(data, "targets", required=True)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    violations = 0
    for label, target in targets:
        containing = [
            auth_label for auth_label, auth in authorized if fully_contained(target, auth)
        ]
        if not containing:
            print(f"OUTSIDE   {label}   not wholly contained in an authorized range")
            violations += 1
            continue

        overlaps = [
            excluded_label
            for excluded_label, blocked in excluded
            if target.version == blocked.version and target.overlaps(blocked)
        ]
        if overlaps:
            print(f"EXCLUDED  {label}   overlaps {', '.join(overlaps)}")
            violations += 1
            continue

        print(f"AUTHORIZED {label}   within {', '.join(containing)}")

    if violations:
        print(f"{violations} scope violation(s); refuse those targets")
        return 1

    print(f"{len(targets)} target(s) authorized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
