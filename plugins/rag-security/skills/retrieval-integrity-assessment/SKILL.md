---
name: retrieval-integrity-assessment
description: "Assesses whether an authorized retrieval-augmented AI system preserves source, index, retrieval, context, and output integrity. Use when testing RAG poisoning, retrieval hijacking, context saturation, semantic substitution, or citation controls with benign canaries."
metadata:
  portability: universal
  discipline: penetration-testing
  domain: ai-systems
  tags: [rag, retrieval, integrity, canaries, provenance]
---

# Retrieval integrity assessment

Measure how content moves from an approved source through ingestion, indexing,
retrieval, context assembly, and model output. Use benign canaries to distinguish
acceptance from retrieval and retrieval from influence.

## When to Use

- Assessing an authorized RAG or enterprise-search deployment.
- Validating content provenance, tenant isolation, ranking controls, citation
  fidelity, or retrieval monitoring.
- Reproducing a suspected poisoning or retrieval-hijacking condition with
  controlled documents and reversible state.

## When NOT to Use

- Do not upload content, modify a corpus, or query a target without explicit
  authorization for that action and environment.
- Do not use real secrets, impersonated safety guidance, executable content, or
  uncontrolled public documents as test fixtures.
- Do not infer retrieval from an upload receipt or influence from a citation.

## State model

Keep these states separate:

1. `submitted` — the test document was offered to the ingestion boundary.
2. `accepted` — the service acknowledged the document.
3. `indexed` — index-origin evidence identifies the expected test artifact.
4. `retrieved` — a retrieval receipt ties the artifact to a specific query run.
5. `context-used` — the assembled model context contains the attributed content.
6. `output-influenced` — the response changed in the predicted bounded way.
7. `downstream-acted` — a separate consumer acted on that output.

## Workflow

1. Bind the test to the exact corpus, tenant, connector, index, model route,
   identity, time window, action authority, cleanup plan, and run identifier.
2. Preserve a clean baseline: source set, query set, retrieval results, ranking,
   context where observable, response, citations, and telemetry.
3. Create a unique inert canary document. Record its content digest, source,
   owner, labels, access policy, expected audience, and expiry.
4. Introduce the canary only through the approved ingestion path. Capture
   separate source, acceptance, indexing, and access-control receipts.
5. Run the same bounded query set. Record top results, scores where available,
   filters, chunk identifiers, context position, citation mapping, response,
   cache state, and target-origin timestamps.
6. Test integrity questions independently:
   - source and tenant boundary enforcement;
   - stale, revoked, or deleted content handling;
   - ranking displacement and context saturation;
   - semantic substitution or misleading near-duplicate content;
   - instruction-like content crossing into control behavior;
   - citation-to-source fidelity;
   - embedding, chunking, metadata, and filter manipulation;
   - monitoring and rollback visibility.
7. Compare baseline and canary runs. Do not attribute a response difference to
   retrieval when model, route, temperature, cache, corpus, or query also changed.
8. Grade each state in the ladder with its own receipt. Record alternative
   explanations and the evidence needed for the next state.
9. Remove the canary through the approved path, confirm source and index removal,
   expire caches where authorized, and record residual retrieval.

## Deliverable

Return the bound system context, baseline, canary manifest, query matrix,
state-ladder results, provenance and citation observations, tenant and policy
findings, alternative explanations, telemetry gaps, and cleanup receipt.

## Rationalizations to reject

- **“The upload succeeded, so poisoning is proven.”** Acceptance does not prove
  indexing, retrieval, influence, or impact.
- **“The answer used the phrase, so the document was retrieved.”** The model may
  already know it or another source may contain it.
- **“A citation proves source fidelity.”** Verify that the cited chunk supports
  the claim and belongs to the expected source and tenant.
- **“Higher ranking means successful exploitation.”** Ranking movement is an
  integrity observation, not automatically a security impact.
- **“Deletion from the source completes cleanup.”** Indexes, caches, and derived
  stores can retain content.
- **“One strange answer proves a deterministic weakness.”** Preserve model and
  retrieval variability and repeat only within the approved budget.
