#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Score an ATT&CK coverage map from a purple-team exercise. Runs no attacks.

A purple exercise answers one question per technique: we executed it — did a
detection fire? The honest answer for each technique is exactly one of:

  covered         executed, and a detection fired
  partial         executed, detection fired weakly or on only some variants
  not-detected    executed, nothing fired. A real gap
  not-detectable  a passive technique that generates no observable (OSINT,
                  reading public records). An accepted gap, not a failure
  unknown         executed but the detection outcome was never recorded

The one that poisons a coverage report is `unknown`. "We ran 40 techniques and
we're covered" with blanks in the detection column is the same lie as a clean
scan with zero coverage: a confident summary over an unanswered question. This
distinguishes the honest accepted gap (`not-detectable`) from the un-assessed
blank (`unknown`), and refuses to let `unknown` count as anything.

Input: a JSON coverage map.
  {"techniques": [{"id": "T1595.001", "name": "Port Scan",
                   "executed": true, "coverage": "covered", "rule": "rb-recon-001"}]}

Exit codes: 0 = every executed technique has a known outcome and there are no
`unknown` entries. 1 = gaps exist (not-detected or unknown among executed
techniques). 2 = bad input or zero techniques.

No network, no file writes, stdlib only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VALID = {"covered", "partial", "not-detected", "not-detectable", "unknown"}
# Outcomes that represent a real, un-accepted gap in the exercise.
GAPS = {"not-detected", "unknown"}


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("map", type=Path, help="JSON coverage map")
    ap.add_argument("--json", action="store_true", help="emit result as JSON")
    args = ap.parse_args()

    if not args.map.exists():
        print(f"error: {args.map} does not exist", file=sys.stderr)
        return 2
    try:
        data = json.loads(args.map.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"error: cannot read map: {e}", file=sys.stderr)
        return 2

    techs = data.get("techniques") if isinstance(data, dict) else None
    if not isinstance(techs, list) or not techs:
        print("error: map has no techniques; a review of nothing is not a pass", file=sys.stderr)
        return 2

    tally = {k: 0 for k in VALID}
    executed = 0
    gaps: list[tuple[str, str, str]] = []  # id, coverage, reason
    bad: list[str] = []

    for t in techs:
        tid = str(t.get("id") or "(no id)")
        cov = str(t.get("coverage", "")).strip().lower()
        is_exec = bool(t.get("executed"))
        # An executed technique with no recorded coverage is unknown, not blank.
        if is_exec and cov == "":
            cov = "unknown"
        if cov not in VALID:
            bad.append(f"{tid}: coverage {cov!r} is not one of {sorted(VALID)}")
            continue
        tally[cov] += 1
        if is_exec:
            executed += 1
            if cov in GAPS:
                reason = (
                    "executed but detection outcome never recorded"
                    if cov == "unknown"
                    else "executed and nothing fired"
                )
                gaps.append((tid, cov, reason))

    if bad:
        for b in bad:
            print(f"error: {b}", file=sys.stderr)
        return 2

    # Real coverage is covered/partial over everything executed that COULD be
    # detected. Passive not-detectable techniques are removed from the denominator
    # honestly rather than silently counted as either covered or failed.
    detectable = executed - tally["not-detectable"]
    real = tally["covered"] + tally["partial"]
    pct = (real / detectable * 100) if detectable else 0.0

    if args.json:
        print(
            json.dumps(
                {
                    "techniques": len(techs),
                    "executed": executed,
                    "detectable": detectable,
                    "covered": tally["covered"],
                    "partial": tally["partial"],
                    "not_detected": tally["not-detected"],
                    "not_detectable": tally["not-detectable"],
                    "unknown": tally["unknown"],
                    "coverage_pct": round(pct, 1),
                    "gaps": [{"id": i, "coverage": c, "reason": r} for i, c, r in gaps],
                },
                indent=2,
            )
        )
    else:
        print(
            f"{len(techs)} technique(s), {executed} executed, "
            f"{real}/{detectable} detectable covered ({pct:.0f}%)"
        )
        print(
            f"  covered {tally['covered']}  partial {tally['partial']}  "
            f"not-detected {tally['not-detected']}  not-detectable {tally['not-detectable']}  "
            f"unknown {tally['unknown']}"
        )
        for tid, cov, reason in gaps:
            print(f"  GAP  {cov:<13} {tid:<14} {reason}")
        if tally["unknown"]:
            print(
                f"\n{tally['unknown']} executed technique(s) have no recorded outcome. "
                "An unknown is not coverage. Record the result or re-run the technique."
            )

    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
