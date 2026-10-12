#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check an OSINT plan against its own stealth premise. Does NOT run any recon.

On a red team operation the value of OSINT is that it reaches the target's
footprint without touching the target's infrastructure. A plan that calls
itself passive but contains an action that sends packets to target-controlled
infrastructure has broken that premise, and nothing in the plan's prose will
stop it -- so this does.

Contact level is the one fact that matters and it is deterministic:

  none    the action queries a third party that already did the scanning
          (Shodan, Censys, crt.sh, DeHashed, BuiltWith, Hunter, Google). Zero
          packets reach the target.
  target  the action sends traffic to infrastructure the target controls or
          monitors (probing their web host, resolving against their
          authoritative nameserver, active subdomain brute force, any port
          scanner).

Several tools have both a passive and an active mode; those are reported
`depends` until a `mode` disambiguates them, and an unresolved `depends` in a
passive plan is treated as a violation, because an unexamined maybe is not a no.

Input: a JSON plan. `{"stealth": "passive"|"target-contact-authorized",
"target": "...", "actions": [{"tool": "...", "mode": "...", "note": "..."}]}`.

Exit codes: 0 = plan is internally consistent. 1 = a passive plan contains
target-contact (or unresolved) actions. 2 = bad input or an empty plan; a
review of nothing is not a pass.

No network, no file writes, stdlib only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# tool -> (default contact level, note). `depends` means the mode decides.
# Kept deliberately small and honest: a tool that is not listed is reported
# `unknown`, which a passive plan must resolve rather than wave through.
TOOLS: dict[str, tuple[str, str]] = {
    # third-party aggregators — zero packets to the target
    "shodan": ("none", "queries Shodan's prior scans, not the target"),
    "censys": ("none", "queries Censys' prior scans, not the target"),
    "crtsh": ("none", "Certificate Transparency logs, not the target"),
    "crt.sh": ("none", "Certificate Transparency logs, not the target"),
    "dehashed": ("none", "historical breach corpus, not the target"),
    "builtwith": ("none", "cataloged tech stack, not a live fetch"),
    "hunter": ("none", "email-format aggregator"),
    "hunter.io": ("none", "email-format aggregator"),
    "google": ("none", "search-engine dorking; Google fetched the pages, not you"),
    "google-dorking": ("none", "search-engine index, not the target"),
    # dual-mode
    "amass": ("depends", "passive = aggregators only; active/brute resolves against target"),
    "theharvester": ("depends", "passive sources = none; active DNS resolution hits target"),
    "subfinder": ("depends", "passive by default; -rl/resolution touches target DNS"),
    "dig": ("depends", "public cache = low; @ target's authoritative NS = target contact"),
    # target-contact by nature
    "whatweb": ("target", "fetches the target's pages"),
    "wappalyzer": ("target", "programmatic run fetches the target's pages"),
    "httpx": ("target", "probes the target's hosts"),
    "nmap": ("target", "sends packets to the target"),
    "masscan": ("target", "sends packets to the target"),
    "rustscan": ("target", "sends packets to the target"),
}

# mode overrides: (tool, mode) -> contact level
MODES: dict[tuple[str, str], str] = {
    ("amass", "passive"): "none",
    ("amass", "enum"): "none",
    ("amass", "active"): "target",
    ("amass", "brute"): "target",
    ("theharvester", "passive"): "none",
    ("theharvester", "active"): "target",
    ("subfinder", "passive"): "none",
    ("subfinder", "resolve"): "target",
    ("dig", "cache"): "none",
    ("dig", "authoritative"): "target",
}


def classify(action: dict) -> tuple[str, str, str]:
    """Return (tool, contact_level, reason) for one planned action."""
    tool = str(action.get("tool", "")).strip().lower()
    mode = str(action.get("mode", "")).strip().lower()
    if not tool:
        return ("(unnamed)", "unknown", "action has no tool")
    if (tool, mode) in MODES:
        lvl = MODES[(tool, mode)]
        return (tool, lvl, f"mode={mode}: {lvl}")
    if tool not in TOOLS:
        return (tool, "unknown", "tool not in the contact map; classify it before running")
    lvl, note = TOOLS[tool]
    if lvl == "depends" and mode:
        return (tool, "unknown", f"mode {mode!r} not recognised; {note}")
    return (tool, lvl, note)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("plan", type=Path, help="JSON OSINT plan")
    ap.add_argument("--json", action="store_true", help="emit result as JSON")
    args = ap.parse_args()

    if not args.plan.exists():
        print(f"error: {args.plan} does not exist", file=sys.stderr)
        return 2
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"error: cannot read plan: {e}", file=sys.stderr)
        return 2

    actions = plan.get("actions") if isinstance(plan, dict) else None
    if not isinstance(actions, list) or not actions:
        print("error: plan has no actions; a review of nothing is not a pass", file=sys.stderr)
        return 2

    stealth = str(plan.get("stealth", "passive")).strip().lower()
    passive_required = stealth != "target-contact-authorized"

    results = [classify(a) for a in actions]
    violations = [r for r in results if passive_required and r[1] in ("target", "unknown")]

    if args.json:
        print(
            json.dumps(
                {
                    "stealth": stealth,
                    "passive_required": passive_required,
                    "actions": [{"tool": t, "contact": c, "reason": r} for t, c, r in results],
                    "violations": [
                        {"tool": t, "contact": c, "reason": r} for t, c, r in violations
                    ],
                },
                indent=2,
            )
        )
    else:
        mode_label = "passive required" if passive_required else "target contact authorized"
        print(f"stealth={stealth} ({mode_label}), {len(actions)} action(s)")
        for tool, lvl, reason in results:
            mark = "!!" if (passive_required and lvl in ("target", "unknown")) else "  "
            print(f"  {mark} {lvl:<8} {tool:<16} {reason}")
        if violations:
            print(
                f"\n{len(violations)} action(s) break the passive premise. Reclassify, remove, "
                "or set stealth to target-contact-authorized and accept the contact."
            )

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
