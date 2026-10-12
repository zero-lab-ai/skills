# Detection and Validation

Blue- and purple-team skills for detection engineering, technique validation,
telemetry coverage, resilience testing, incident correlation, and control
evidence synthesis. The bundle is built around honest denominators: untested,
unknown, stale, and not-detectable are not silently counted as covered.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`detection-engineering`](skills/detection-engineering/SKILL.md) | Building rules proven against known-bad and known-good cases |
| [`detection-validate`](skills/detection-validate/SKILL.md) | Running an authorized technique and confirming whether its detection fires |
| [`detection-resilience-test-plan`](skills/detection-resilience-test-plan/SKILL.md) | Planning bounded resilience tests with pre-approved opaque fixtures |
| [`telemetry-coverage-audit`](skills/telemetry-coverage-audit/SKILL.md) | Auditing passive coverage, retention, custody, and investigation readiness |
| [`incident-validation-correlation`](skills/incident-validation-correlation/SKILL.md) | Correlating incident observations with isolated validation receipts |
| [`defensive-control-evidence-synthesis`](skills/defensive-control-evidence-synthesis/SKILL.md) | Consolidating assessments into a lineage-preserving control matrix |

## Install

```text
/plugin install detection-validation@zero-lab
```

The bundle includes deterministic tests for detection-rule proof and coverage
maps, plus behavioral evals for real detection gaps and non-detectable activity.

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## Tested on

- Claude Code: strict manifest validation and marketplace install, 2026-10-12.
- Codex CLI: marketplace and skill discovery, 2026-10-12.
- OpenCode 1.18.35 with `forge1/qwen3.8-27b`: native skill discovery and one
  pilot run for each of the two behavioral cases, 2026-10-12.

## License

[Apache License 2.0](../../LICENSE)
