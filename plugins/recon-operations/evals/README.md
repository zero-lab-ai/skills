# Eval suite for `recon-operations`

These cases exercise scope refusal and the central negative-result rule: no
response with no measured coverage is an unanswered question, not a clean
network.

Run manually:

```sh
claude plugin eval . --judge-model sonnet --no-publish --json results/run.json
```

The suite is intentionally small and behavioral. It does not reward a specific
scanner command.

## Pilot receipt

On 2026-10-12, OpenCode 1.18.35 with `forge1/qwen3.8-27b` loaded the named
skills through its native skill tool. One isolated run of each case produced a
final **3 passed / 0 failed** result. The target-refusal case initially widened
discovery beyond the supplied target list; the skill was corrected and the case
passed on rerun. This pilot is not a claim about three-run reliability.
