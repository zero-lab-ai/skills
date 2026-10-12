# Recon Operations

Reconnaissance skills for penetration tests, red-team operations, passive
exposure mapping, target synthesis, and the governance around repeated work.
The individual skills keep loud completeness-oriented scanning separate from
quiet operational reconnaissance.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`network-recon`](skills/network-recon/SKILL.md) | Enforcing IP scope, planning network discovery, or auditing scan coverage |
| [`osint-scanner`](skills/osint-scanner/SKILL.md) | Mapping public exposure without contacting the target |
| [`social-engineering-recon`](skills/social-engineering-recon/SKILL.md) | Mapping passive, privacy-preserving human-layer exposure |
| [`physical-recon`](skills/physical-recon/SKILL.md) | Reviewing supplied public-vantage physical-security observations |
| [`target-profile-synthesis`](skills/target-profile-synthesis/SKILL.md) | Joining validated cross-domain evidence into exposure themes |
| [`situational-awareness`](skills/situational-awareness/SKILL.md) | Assessing a foothold within an operation's noise budget |
| [`opsec-planning`](skills/opsec-planning/SKILL.md) | Connecting objectives to artifacts, detection risk, abort conditions, and cleanup |
| [`recon-automation-governance`](skills/recon-automation-governance/SKILL.md) | Governing jobs, budgets, retries, stop controls, and evidence custody |
| [`ai-surface-recon`](skills/ai-surface-recon/SKILL.md) | Mapping models, retrieval paths, agents, tools, guardrails, endpoints, and privileged consumers |

## Install

```text
/plugin install recon-operations@zero-lab
```

The bundle includes deterministic checks for scope, scan coverage, passive
contact, and enumeration noise, plus behavioral evals for scope refusal and
empty-scan handling.

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## Tested on

- Claude Code: strict manifest validation and marketplace install, 2026-10-12.
- Codex CLI: marketplace and skill discovery, 2026-10-12.
- OpenCode 1.18.35 with `forge1/qwen3.8-27b`: native skill discovery and one
  pilot run for each of the three behavioral cases, 2026-10-12.

## License

[Apache License 2.0](../../LICENSE)
