#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check that a detection rule has been proven both ways. Does NOT run a SIEM.

A detection rule earns production on two pieces of evidence, and neither one
substitutes for the other:

  fires on known-bad   it actually triggered on a true-positive sample
  silent on known-good it did NOT trigger on a true-negative (benign) sample

A rule tested only against the attack is unproven against false positives, and
false positives are the silent killer of a SOC: analysts go alert-blind, then
the real alert gets the same shrug. A rule never tested against the attack is
unproven, full stop. Either gap means the rule has not earned deployment, and a
rule that was never tested at all must never read as ready.

Input: a JSON test record per rule.
  {"rules": [{"id": "...", "attack": "T1003.001",
              "true_positive": {"tested": true, "fired": true},
              "true_negative": {"tested": true, "fired": false},
              "fp_rate": 0.02}]}

Exit codes: 0 = every rule proven both ways and under the FP ceiling. 1 = one
or more rules unproven or over the ceiling. 2 = bad input or zero rules; a
review of nothing is not a pass.

No network, no file writes, stdlib only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Ch 1: "If a rule's false positive rate exceeds 90%, it needs a rewrite." Set
# the hard ceiling there; a rule may still be noisy below it, which is a tuning
# problem, not a validity failure.
FP_CEILING = 0.90


def check_rule(rule: dict) -> list[str]:
    """Return a list of failure strings for one rule; empty means proven."""
    rid = str(rule.get("id") or "(unnamed)")
    problems: list[str] = []

    tp = rule.get("true_positive")
    tn = rule.get("true_negative")

    # The true-positive arm: did it fire on known-bad?
    if not isinstance(tp, dict) or not tp.get("tested"):
        problems.append(f"{rid}: no true-positive test — unproven that it detects the attack")
    elif tp.get("fired") is not True:
        problems.append(f"{rid}: tested on known-bad and did NOT fire — detects nothing")

    # The true-negative arm: did it stay silent on known-good?
    if not isinstance(tn, dict) or not tn.get("tested"):
        problems.append(f"{rid}: no true-negative test — unproven against false positives")
    elif tn.get("fired") is not False:
        problems.append(f"{rid}: fired on known-good — false positive, causes alert blindness")

    fp = rule.get("fp_rate")
    if isinstance(fp, (int, float)) and fp > FP_CEILING:
        problems.append(
            f"{rid}: fp_rate {fp:.0%} over {FP_CEILING:.0%} ceiling — rewrite, not tune"
        )

    if not rule.get("attack"):
        problems.append(f"{rid}: no ATT&CK technique mapped — cannot be placed on a coverage map")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("record", type=Path, help="JSON detection test record")
    ap.add_argument("--json", action="store_true", help="emit result as JSON")
    args = ap.parse_args()

    if not args.record.exists():
        print(f"error: {args.record} does not exist", file=sys.stderr)
        return 2
    try:
        data = json.loads(args.record.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"error: cannot read record: {e}", file=sys.stderr)
        return 2

    rules = data.get("rules") if isinstance(data, dict) else None
    if not isinstance(rules, list) or not rules:
        print("error: record has no rules; a review of nothing is not a pass", file=sys.stderr)
        return 2

    results = [(str(r.get("id") or "(unnamed)"), check_rule(r)) for r in rules]
    failed = [(rid, probs) for rid, probs in results if probs]

    if args.json:
        print(
            json.dumps(
                {
                    "rules_checked": len(rules),
                    "proven": len(rules) - len(failed),
                    "unproven": [{"id": rid, "problems": probs} for rid, probs in failed],
                },
                indent=2,
            )
        )
    else:
        print(f"{len(rules)} rule(s): {len(rules) - len(failed)} proven, {len(failed)} unproven")
        for rid, probs in results:
            if not probs:
                print(f"  ok   {rid}")
            else:
                for p in probs:
                    print(f"  FAIL {p}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
