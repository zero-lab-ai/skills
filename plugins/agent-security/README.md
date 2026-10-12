# Agent Security

Security review skills for agent and MCP tool surfaces, instruction-channel
exposure, deployed runtime behavior, and delegated authority. Install this
bundle to review what an integration declares and then validate how its tools,
memory, hooks, approvals, identities, and handoffs actually act.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`agent-surface-audit`](skills/agent-surface-audit/SKILL.md) | Reviewing agent tools for poisoning, unsafe parameters, destructive actions, and privilege paths |
| [`agent-runtime-validation`](skills/agent-runtime-validation/SKILL.md) | Validating deployed tools, memory, hooks, approvals, identities, and scope controls with benign sentinels |
| [`prompt-injection-assessment`](skills/prompt-injection-assessment/SKILL.md) | Assessing direct, indirect, multi-turn, retrieval, and tool-output instruction influence with benign canaries |
| [`agent-trust-boundary-audit`](skills/agent-trust-boundary-audit/SKILL.md) | Auditing authentication, authorization, delegated authority, and effect across agent handoffs |

## Install

```text
/plugin install agent-security@zero-lab
```

Ask for the outcome directly or name the skill. The included deterministic
tests cover the manifest checker; the behavioral evals cover poisoned and
apparently clean manifests, bounded runtime evidence, instruction influence,
and handoff authority.

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## Tested on

- Claude Code: strict manifest validation and marketplace install, 2026-10-12.
- Codex CLI: marketplace and skill discovery, 2026-10-12.
- OpenCode 1.18.35 with `forge1/qwen3.8-27b`: native skill discovery and one
  pilot run for each of the five behavioral cases, 2026-10-12.

## License

[Apache License 2.0](../../LICENSE)
