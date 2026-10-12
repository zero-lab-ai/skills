#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Deterministic first pass over an MCP server's tool manifest.

Input: a JSON file containing either a `tools/list` response
(`{"tools": [...]}`), a bare list of tool objects, or a JSON-RPC envelope
(`{"result": {"tools": [...]}}`). Each tool has `name`, `description`, and
`inputSchema` (JSON Schema).

Output: one finding per line, `SEVERITY  tool  check  detail`, sorted by
severity. Exit codes: 0 = ran and found nothing above info, 1 = findings at
medium or above, 2 = bad input or zero tools (a review of nothing is not a
pass).

No network, no file writes, stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SEV_ORDER = {"high": 0, "medium": 1, "info": 2}

IMPERATIVE = re.compile(
    r"\b(ignore|disregard|always|never|you must|must not|before (?:calling|using)|"
    r"do not (?:tell|mention|reveal)|system prompt|previous instructions|"
    r"override|instead of)\b",
    re.I,
)
HIDDEN = re.compile(r"<!--|-->|<IMPORTANT>|​|‌|‍|⁠|﻿")
MENTIONS_OTHER_TOOL = re.compile(r"\b(call|use|invoke)\s+`?[a-z_]+(?:_[a-z]+)+`?", re.I)
SINK_NAMES = re.compile(
    r"(cmd|command|shell|script|exec|query|sql|path|file|url|uri|href|code|expression|eval)",
    re.I,
)
DESTRUCTIVE = re.compile(
    r"\b(delete|remove|drop|destroy|purge|rm|truncate|wipe|reset|revoke|kill|terminate|force)\b",
    re.I,
)
CONFIRM = re.compile(r"(confirm|dry_run|dryrun|force|yes|i_understand)", re.I)


def load_tools(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if "tools" in data and isinstance(data["tools"], list):
            return data["tools"]
        if "result" in data and isinstance(data["result"], dict):
            return data["result"].get("tools", [])
    return []


def walk_props(schema: dict, prefix: str = "") -> list[tuple[str, dict]]:
    out = []
    props = schema.get("properties", {}) if isinstance(schema, dict) else {}
    for name, sub in props.items():
        full = f"{prefix}{name}"
        out.append((full, sub if isinstance(sub, dict) else {}))
        if isinstance(sub, dict) and sub.get("type") == "object":
            out.extend(walk_props(sub, full + "."))
    return out


def check_tool(tool: dict) -> list[tuple[str, str, str, str]]:
    f: list[tuple[str, str, str, str]] = []
    name = str(tool.get("name", "<unnamed>"))
    desc = str(tool.get("description") or "")
    schema = tool.get("inputSchema") or tool.get("input_schema") or {}

    if not desc.strip():
        f.append(("high", name, "no-description", "tool has no description; model will invent one"))
    else:
        m = IMPERATIVE.search(desc)
        if m:
            f.append(
                ("high", name, "imperative-description", f"instruction-like text: {m.group(0)!r}")
            )
        if HIDDEN.search(desc):
            f.append(
                (
                    "high",
                    name,
                    "hidden-content",
                    "comment, tag, or zero-width characters in description",
                )
            )
        m = MENTIONS_OTHER_TOOL.search(desc)
        if m:
            f.append(
                (
                    "medium",
                    name,
                    "cross-tool-reference",
                    f"description steers other tool use: {m.group(0)!r}",
                )
            )
        if len(desc) > 1500:
            f.append(
                (
                    "info",
                    name,
                    "long-description",
                    f"{len(desc)} chars; review for buried instructions",
                )
            )

    if not isinstance(schema, dict) or not schema:
        f.append(("medium", name, "no-schema", "no inputSchema; parameters are unbounded"))
    else:
        if schema.get("additionalProperties") is True:
            f.append(
                ("medium", name, "additional-properties", "schema accepts arbitrary extra fields")
            )
        for pname, p in walk_props(schema):
            ptype = p.get("type")
            if not p.get("description"):
                f.append(("info", name, "param-no-description", f"`{pname}` has no description"))
            if (
                ptype == "string"
                and SINK_NAMES.search(pname)
                and not p.get("enum")
                and not p.get("pattern")
            ):
                f.append(
                    (
                        "high",
                        name,
                        "free-form-sink",
                        f"`{pname}` is an unconstrained string named like a command/path/query/url",
                    )
                )
            if ptype == "string" and p.get("maxLength", 0) and p["maxLength"] > 4000:
                f.append(
                    ("info", name, "large-string", f"`{pname}` allows up to {p['maxLength']} chars")
                )

    name_words = re.sub(r"[_\-.]", " ", name)
    if DESTRUCTIVE.search(name_words) or DESTRUCTIVE.search(desc[:200]):
        params = " ".join(n for n, _ in walk_props(schema)) if isinstance(schema, dict) else ""
        if not CONFIRM.search(params):
            f.append(
                (
                    "medium",
                    name,
                    "destructive-no-guard",
                    "destructive verb with no confirm/dry_run parameter",
                )
            )
    return f


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--json", action="store_true", help="emit findings as JSON")
    args = ap.parse_args()

    try:
        tools = load_tools(args.manifest)
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: cannot read manifest: {e}", file=sys.stderr)
        return 2
    if not tools:
        print("error: manifest contains zero tools; nothing was reviewed", file=sys.stderr)
        return 2

    findings = []
    for t in tools:
        if not isinstance(t, dict):
            print(f"error: tool entry is not an object: {t!r}", file=sys.stderr)
            return 2
        findings.extend(check_tool(t))
    findings.sort(key=lambda x: (SEV_ORDER[x[0]], x[1], x[2]))

    if args.json:
        print(
            json.dumps(
                [
                    dict(zip(("severity", "tool", "check", "detail"), x, strict=True))
                    for x in findings
                ],
                indent=2,
            )
        )
    else:
        print(f"reviewed {len(tools)} tools, {len(findings)} findings")
        for sev, tool, check, detail in findings:
            print(f"{sev:<7} {tool:<28} {check:<24} {detail}")
    return 1 if any(s in ("high", "medium") for s, *_ in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
