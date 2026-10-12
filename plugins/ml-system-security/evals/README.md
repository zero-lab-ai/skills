# Eval suite for `ml-system-security`

These cases test whether ML-system reviews preserve distinct artifact lifecycle,
model-decision, downstream-gate, dataset-lineage, serving-reachability, access,
and effect states.

Run manually with the plugin eval harness; paid model runs are not part of CI.

## Pilot receipt

On 2026-10-12, OpenCode 1.18.35 with `forge1/qwen3.8-27b` loaded each named
skill through its native skill tool. One isolated run of each case passed its
grader: **4 passed / 0 failed**. This pilot is evidence of one observed run per
case, not a claim about three-run reliability.
