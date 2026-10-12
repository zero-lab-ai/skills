# Eval suite for `agent-security`

These cases test the failure modes that matter most: missing a poisoned or
over-privileged surface, inventing findings when runtime evidence is absent,
allowing a runtime test to escape its benign sentinel boundary, promoting
instruction influence into policy bypass, and confusing authentication with
delegated authority.

Run manually with the plugin eval harness; these paid model runs are not part
of CI:

```sh
claude plugin eval . --judge-model sonnet --no-publish --json results/run.json
```

Pilot one case with one run before running the full three-run suite. Grade the
review outcome, not exact phrasing.

## Pilot receipt

On 2026-10-12, OpenCode 1.18.35 with `forge1/qwen3.8-27b` loaded each named
skill through its native skill tool. One isolated run of each case passed its
grader: **5 passed / 0 failed**. This pilot is evidence of one observed run per
case, not a claim about three-run reliability.
