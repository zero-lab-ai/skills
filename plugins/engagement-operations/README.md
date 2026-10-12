# Engagement Operations

The work around security testing: exercise planning, threat modeling, evidence
review, tool governance, sequence review, findings writing, and final package
assembly. These skills preserve authorization and evidence boundaries without
becoming a separate governance platform.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`findings-report`](skills/findings-report/SKILL.md) | Writing reproducible, severity-justified, evidence-bound findings |
| [`social-engineering-engagement-plan`](skills/social-engineering-engagement-plan/SKILL.md) | Planning authorized human-security exercises with participant safeguards |
| [`security-test-tool-governance`](skills/security-test-tool-governance/SKILL.md) | Reviewing supplied security-test artifacts before controlled lab handoff |
| [`assessment-sequence-governance`](skills/assessment-sequence-governance/SKILL.md) | Checking a supplied assessment sequence's ordering, authority, and safeguards |
| [`engagement-report-assembly`](skills/engagement-report-assembly/SKILL.md) | Assembling validated artifacts without rewriting source findings |
| [`ai-threat-model`](skills/ai-threat-model/SKILL.md) | Modeling AI architecture, trust boundaries, assumptions, and attack-path hypotheses |
| [`agent-action-proof`](skills/agent-action-proof/SKILL.md) | Grading what agent callbacks, tool traces, target receipts, and state changes actually prove |

## Install

```text
/plugin install engagement-operations@zero-lab
```

The bundle includes behavioral evals for the line between a reproducible
finding and an unverified lead.

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## Tested on

- Claude Code: strict manifest validation and marketplace install, 2026-10-12.
- Codex CLI: marketplace and skill discovery, 2026-10-12.
- OpenCode 1.18.35 with `forge1/qwen3.8-27b`: native skill discovery and one
  pilot run for each of the four behavioral cases, 2026-10-12.

## License

[Apache License 2.0](../../LICENSE)
