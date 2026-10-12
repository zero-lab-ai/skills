# ML System Security

Security review skills for machine-learning systems, datasets, decision gates,
serving surfaces, and artifact supply chains. The bundle traces evidence from
data and model intake through protected decisions, runtime access, monitoring,
revocation, and retirement.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`model-artifact-lifecycle-audit`](skills/model-artifact-lifecycle-audit/SKILL.md) | Auditing model artifacts from intake through loading, execution, revocation, and cleanup |
| [`ml-decision-boundary-assessment`](skills/ml-decision-boundary-assessment/SKILL.md) | Testing whether model-output changes alter downstream security decisions or protected effects |
| [`dataset-integrity-assessment`](skills/dataset-integrity-assessment/SKILL.md) | Auditing dataset sources, transformations, review, lineage, retraining, and rollback evidence |
| [`model-serving-exposure-audit`](skills/model-serving-exposure-audit/SKILL.md) | Auditing model-serving APIs, identities, administrative surfaces, data stores, and access evidence |

## Install

```text
/plugin install ml-system-security@zero-lab
```

The behavioral evals keep artifact lifecycle, model decisions, dataset trust,
serving reachability, access, and protected-system effects as distinct evidence
states.

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## Tested on

- Claude Code: strict manifest validation and marketplace install, 2026-10-12.
- Codex CLI: marketplace and skill discovery, 2026-10-12.
- OpenCode 1.18.35 with `forge1/qwen3.8-27b`: native skill discovery and one
  pilot run for each of the four behavioral cases, 2026-10-12.

## License

[Apache License 2.0](../../LICENSE)
