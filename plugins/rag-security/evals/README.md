# Eval suite for `rag-security`

These cases test whether retrieval assessment preserves the evidence boundary
between observed surfaces, accepted sources, indexed content, retrieved chunks,
context use, metadata or content exposure, output influence, and downstream
action.

Run manually with the plugin eval harness; paid model runs are not part of CI.

## Pilot receipt

On 2026-10-12, OpenCode 1.18.35 with `forge1/qwen3.8-27b` loaded each named
skill through its native skill tool. One isolated run of each case passed its
grader: **3 passed / 0 failed**. This pilot is evidence of one observed run per
case, not a claim about three-run reliability.
