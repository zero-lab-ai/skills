# Eval suite for `engagement-operations`

The suite checks whether the skill turns reproduced evidence into a defensible
finding while keeping unverified vulnerability matches as unrated leads.

Run manually:

```sh
claude plugin eval . --judge-model sonnet --no-publish --json results/run.json
```

Judge the argument and evidence boundary, not template wording.

## Pilot receipt

On 2026-10-12, OpenCode 1.18.35 with `forge1/qwen3.8-27b` loaded the named
skills through its native skill tool. One isolated run of each case produced a
final **4 passed / 0 failed** result. The cross-account case initially
generalized from one account to all account holders; the skill was corrected
and the case passed on rerun. This pilot is not a claim about three-run
reliability.
