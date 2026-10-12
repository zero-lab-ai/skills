# Eval suite for `detection-validate`

These cases guard the two outcome distinctions that most often inflate
coverage: detected versus not detected, and not detectable versus covered.

Run manually:

```sh
claude plugin eval . --judge-model sonnet --no-publish --json results/run.json
```

The cases score outcome classification and denominator handling. They do not
score stylistic phrasing.

## Pilot receipt

On 2026-10-12, OpenCode 1.18.35 with `forge1/qwen3.8-27b` loaded
`detection-validate` through its native skill tool. One isolated run of each
case passed its grader: **2 passed / 0 failed**. This pilot is not a claim about
three-run reliability.
