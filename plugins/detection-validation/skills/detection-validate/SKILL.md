---
name: detection-validate
description: "Runs attacker techniques and confirms whether detections actually fire, producing an honest ATT&CK coverage map that separates real gaps from accepted ones. Use when running a purple-team exercise, measuring detection coverage, validating that a SOC can see a technique, or turning 'we think we're covered' into evidence per technique."
allowed-tools: Read Grep Glob Bash
---

# Detection validation

Purple team answers one question, per technique: we executed it — did a
detection fire? Everything else is commentary.

**"We think we're covered" is not coverage.** Coverage is a specific claim
about specific techniques, backed by a recorded outcome for each. A map with
blanks in the detection column is the same lie as a port scan that came back
clean with zero coverage — a confident summary over an unanswered question.

## When to Use

- Running a purple-team exercise, measuring detection coverage, validating that a SOC can see a technique, or turning 'we think we're covered' into evidence per technique.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Every executed technique gets exactly one honest outcome

| Outcome | Meaning |
|---|---|
| `covered` | executed, a detection fired |
| `partial` | fired weakly, or on only some variants |
| `not-detected` | executed, nothing fired — **a real gap** |
| `not-detectable` | passive technique with no observable (OSINT, reading public records) — **an accepted gap, not a failure** |
| `unknown` | executed but the outcome was never recorded — **the one that poisons the report** |

The distinction that matters: `not-detectable` is honest (you looked, there is
nothing to see, you accept it) while `unknown` is a blank wearing a confident
coverage number. They must never be conflated.

## Score the map

```sh
uv run {baseDir}/scripts/coverage_map.py map.json
```

Computes real coverage as covered+partial over everything executed that *could*
be detected — passive `not-detectable` techniques are removed from the
denominator. Exit `0` only when every executed technique has a known, non-gap
outcome; `1` when any `not-detected` or `unknown` remains; `2` on bad or empty
input. See `references/coverage-map.md`.

## Validation record

For each technique, return the technique and variant, execution receipt,
expected observable, telemetry-health evidence, alert evidence, one outcome
from the table above, limitations, and an owner for any gap. Keep the execution
receipt and alert receipt separate: the same timestamp or operator note cannot
prove both sides of the join.

End with counts for `covered`, `partial`, `not-detected`, `not-detectable`, and
`unknown`, plus the denominator used. Never publish only a percentage.

## Pair with the attacker and the detector

This skill is the join between offense and defense:

- The offensive technique comes from the operator (or an attack simulation). If
  you cannot execute it, you cannot validate its detection — an untested
  technique is `unknown`, never assume `covered`.
- The detection that should fire is engineered and proven separately. A rule
  that passed its own true-positive test in isolation can still fail to fire in
  a live exercise against the real technique variant — that is exactly what this
  measures, and why the exercise is not redundant with the rule's unit test.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "We ran 40 techniques, we're covered." | Not until all 40 have a recorded outcome. Blanks are `unknown`, and unknown is not coverage. |
| "No alert fired, so the technique must be benign." | No alert fired means you did not detect it. That is a gap, not an all-clear. |
| "It's probably detected, the rule exists." | A rule existing is not a rule firing. The exercise exists because rules fail live that passed in isolation. |
| "Mark the passive stuff as covered so the number looks complete." | `not-detectable` is removed from the denominator, not counted as covered. Honest beats complete. |
| "We'll fill in the blanks later." | A blank is `unknown` now. Ship the map honest with the gaps visible, or re-run the technique. |
| "100% coverage." | Almost always means the un-run techniques were left off the map. Coverage is over what you executed, and the map must show what you did not. |

## References

- [Coverage map format](references/coverage-map.md) — the JSON the scorer consumes, the five outcomes, and how the denominator is computed
