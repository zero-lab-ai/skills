# RAG Security

Security assessment skills for retrieval-augmented AI systems. The bundle maps
the retrieval surface, tests source and context integrity, and measures data
exposure while keeping each evidence state separate.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`retrieval-integrity-assessment`](skills/retrieval-integrity-assessment/SKILL.md) | Assessing source, tenant, retrieval, context, citation, output, and cleanup integrity with benign canaries |
| [`rag-surface-recon`](skills/rag-surface-recon/SKILL.md) | Mapping sources, connectors, indexes, filters, ranking, caches, citations, and exposed result fields |
| [`rag-data-exposure-audit`](skills/rag-data-exposure-audit/SKILL.md) | Measuring tenant and authorization boundaries with controlled fixtures and exposure-state evidence |

## Install

```text
/plugin install rag-security@zero-lab
```

The behavioral evals check that acceptance is not misreported as retrieval,
observations are not promoted into configuration claims, and answer refusal is
not mistaken for tenant isolation when metadata or content is exposed.

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## Tested on

- Claude Code: strict manifest validation and marketplace install, 2026-10-12.
- Codex CLI: marketplace and skill discovery, 2026-10-12.
- OpenCode 1.18.35 with `forge1/qwen3.8-27b`: native skill discovery and one
  pilot run for each of the three behavioral cases, 2026-10-12.

## License

[Apache License 2.0](../../LICENSE)
