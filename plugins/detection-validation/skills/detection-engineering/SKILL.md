---
name: detection-engineering
description: "Builds detection rules that are proven before they ship — fire on known-bad, stay silent on known-good — and keeps false positives from blinding the SOC. Use when writing a Sigma/Suricata/YARA rule, reviewing a detection before deployment, triaging alert fatigue, or deciding whether a rule has earned production."
allowed-tools: Read Grep Glob Bash
---

# Detection engineering

A detection rule is a claim: *this pattern means an attack*. The claim is worth
nothing until it has been tested both ways.

**Every rule must pass two tests, and neither substitutes for the other:**

- **Fires on known-bad** — it actually triggered on a true-positive sample.
- **Silent on known-good** — it did *not* trigger on a benign sample.

A rule tested only against the attack is unproven against false positives. A
rule never tested against the attack is unproven, period. If you cannot show
both for a rule in production, you have a rule collection, not a detection
programme.

## When to Use

- Writing a Sigma/Suricata/YARA rule, reviewing a detection before deployment, triaging alert fatigue, or deciding whether a rule has earned production.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Prove it before it ships

```sh
uv run {baseDir}/scripts/check_detection.py record.json
```

Takes a test record per rule and fails any rule missing either proof, firing on
known-good, over the false-positive ceiling, or unmapped to an ATT&CK
technique. Exit `0` only when every rule is proven both ways; `1` on any
unproven rule; `2` on empty input. See `references/test-record.md`.

## Production decision

| Known-bad result | Known-good result | Disposition |
| --- | --- | --- |
| Fires | Silent | Eligible for controlled rollout |
| Fires | Fires | Rewrite or narrowly tune; false-positive proof failed |
| Silent | Silent | Do not ship; the rule did not detect the behavior |
| Missing | Any result | Unproven; collect the missing test evidence |
| Fires | Silent, but provenance or mapping missing | Hold until the rule can support a defensible coverage claim |

Record the decision per rule. A passing rule does not prove that the production
pipeline will deliver or alert on it; live validation belongs to
`detection-validate`.

## False positives are the silent killer

Analysts go alert-blind within weeks when most of what fires is garbage — then
the real alert gets the same shrug. Manage it in this order:

1. **Baseline first.** Run a new rule in detection-only mode for ~2 weeks. Count
   the fires, investigate a sample, learn what normal looks like.
2. **Exception lists, not rule disablement.** If a rule is noisy on one service
   account, exclude that account — do not switch the rule off for everyone.
3. **Track the rate.** Above ~90% false positives the logic is wrong, not the
   exceptions. Rewrite it; do not tune it.

## Every rule carries its provenance

For each rule you should be able to answer: where did the idea come from, what
threat it addresses, what log source powers it, when it was last tested, and
its false-positive rate. A rule whose last test date is unknown is an unproven
rule regardless of how long it has been deployed — time in production is not
evidence.

## Keep detections in version control

Rules in Git, tests beside them, CI that validates syntax and runs each rule
against sample known-bad and known-good log data before it compiles to your
SIEM format. A detection pipeline without a test step ships unproven rules by
construction.

## Rationalizations to reject

| Rationalization | Why it fails |
|---|---|
| “The attack sample fired, so the rule can ship.” | It remains unproven against false positives; the SOC goes blind |
| “It has been in production for a year, so it works.” | Time deployed is not a test. If the last-tested date is unknown, the rule is unproven |
| “The rule is noisy, so disable it.” | Disabling it loses the true positives with the false ones; use a bounded exception instead |
| “We can tune around a 95% false-positive rate.” | The logic is wrong, not the thresholds — rewrite it |
| “ATT&CK mapping is optional documentation.” | Without the mapping, the rule cannot support a defensible coverage claim |

## References

- [Test record format](references/test-record.md) — the JSON the checker consumes, and what each field proves
