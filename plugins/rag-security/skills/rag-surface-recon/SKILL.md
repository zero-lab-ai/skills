---
name: rag-surface-recon
description: "Maps an authorized retrieval system's sources, connectors, chunking, embeddings, indexes, filters, ranking, caches, citations, and exposed retrieval fields. Use when scoping a RAG security assessment or explaining observed retrieval behavior."
metadata:
  portability: universal
  discipline: penetration-testing
  domain: ai-systems
  tags: [rag, reconnaissance, embeddings, vector-search, citations]
---

# RAG surface recon

Build an evidence-bound retrieval architecture map before testing integrity or
data exposure. Separate externally observed behavior from reported design and
inference.

## When to Use

- Scoping an authorized RAG, enterprise-search, or retrieval-agent assessment.
- Mapping sources, ingestion, chunking, embeddings, indexes, ranking, filters,
  citations, caches, and deletion behavior.
- Explaining retrieval observations without changing a corpus.

## When NOT to Use

- Do not upload documents, poison content, enumerate adjacent stores, or query
  another tenant without explicit authority.
- Do not identify an embedding model or vector database from one output pattern
  alone.
- Do not convert an omitted citation or empty result into proof that a document
  is absent from the corpus.

## Workflow

1. Record the exact application, tenant, identity, corpus, connector, route,
   query authority, time window, rate limit, and prohibited actions.
2. Create an evidence register covering supplied diagrams and configuration,
   approved responses, citations, retrieval receipts, logs, and owner statements.
3. Classify collection as `passive`, `authorized-query`, `authorized-admin-view`,
   or `prohibited-or-unapproved` before using it.
4. Inventory the retrieval chain:
   - source systems, ownership, tenancy, and access policy;
   - connectors, ingestion schedules, transformations, and deletion flow;
   - parsers, chunking, metadata extraction, and deduplication;
   - embedding models, dimensions where evidenced, and versioning;
   - indexes, namespaces, filters, hybrid search, ranking, and reranking;
   - top-k or context limits, caches, freshness, and fallback sources;
   - raw retrieval fields, citations, context assembly, and downstream consumers.
5. Build a bounded observation set using ordinary or supplied queries. Keep the
   query, route, identity, timestamp, results, ranks, scores where exposed,
   chunk IDs, citations, and response together under one run identifier.
6. Vary one non-destructive factor at a time when authorized: query phrasing,
   identity, filter, freshness window, or known source state. Do not infer fixed
   top-k from one result count.
7. Correlate source, index, retrieval, context, citation, and response artifacts.
   Record service handoffs and which component produced each field.
8. Label every architecture claim `observed`, `reported`, `inferred`,
   `contradicted`, or `unknown` with its evidence and confidence.
9. Identify privileged consumers that act on retrieved text, raw fields, or
   citations. Record the separate authority needed to assess them.
10. Hand integrity questions to `retrieval-integrity-assessment` and access or
    leakage questions to `rag-data-exposure-audit`.

## Deliverable

Return the scoped collection plan, evidence register, retrieval-chain map,
source and tenant inventory, query-observation table, handoff map, privileged
consumers, contradictions, unknowns, and bounded follow-up questions.

## Rationalizations to reject

- **“Five results means top-k is five.”** Filters, thresholds, deduplication,
  availability, and UI truncation can produce the same observation.
- **“The citation names the source, so provenance is proven.”** Correlate the
  citation with the retrieved chunk and source artifact.
- **“The model described the vector store.”** Model narration is not deployment
  evidence.
- **“No result means the document is absent.”** Authorization, filtering,
  freshness, ranking, and route behavior remain alternatives.
- **“A public search interface permits corpus enumeration.”** Reachability does
  not expand authorization.
- **“One query exposes the architecture.”** Preserve observation limits and
  avoid fingerprint certainty from sparse behavior.
