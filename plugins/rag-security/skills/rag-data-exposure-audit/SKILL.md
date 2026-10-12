---
name: rag-data-exposure-audit
description: "Assesses document authorization, tenant isolation, raw-chunk fields, citations, caches, exports, and sensitive-source leakage in retrieval systems. Use when an authorized RAG assessment must determine what data each identity can retrieve or disclose."
metadata:
  portability: universal
  discipline: penetration-testing
  domain: ai-systems
  tags: [rag, data-exposure, authorization, multi-tenant, provenance]
---

# RAG data exposure audit

Measure whether retrieval and generation preserve document- and tenant-level
authorization. Use controlled fixtures and restricted evidence handling so the
audit does not amplify any sensitive material it discovers.

## When to Use

- Testing document authorization and tenant isolation in an authorized RAG or
  enterprise-search deployment.
- Reviewing raw retrieval fields, citations, exports, caches, logs, or fallback
  paths for unintended disclosure.
- Reproducing a suspected source-policy mismatch with controlled documents.

## When NOT to Use

- Do not enumerate real sensitive documents or another tenant's corpus without
  explicit written authority.
- Do not place real credentials, personal data, or production secrets into test
  documents.
- Do not quote discovered sensitive content when a redacted evidence reference
  and digest are sufficient.

## Exposure states

Keep these states separate: `metadata-visible`, `candidate-returned`,
`chunk-retrieved`, `context-present`, `response-disclosed`, `citation-exposed`,
`exported`, and `downstream-propagated`. One state does not prove the next.

## Workflow

1. Bind the audit to exact tenants, identities, roles, corpora, connectors,
   routes, allowed data classes, query budget, monitoring, and cleanup duties.
2. Build an authorization matrix from authoritative source policy: identity ×
   document or collection × operation. Preserve unknown policy as unknown.
3. Establish controlled fixtures with unique inert markers across allowed,
   denied, tenant-specific, revoked, deleted, and stale states where authorized.
4. Record source ACL, ingestion identity, index namespace, metadata filters,
   retrieval identity, model identity, cache keying, and response channel for
   each fixture.
5. Establish same-identity baselines for ordinary allowed and denied requests.
6. Exercise only approved identity and query pairs. Capture target-origin query,
   retrieval, context, citation, response, export, cache, and policy receipts.
7. Test exposure surfaces independently:
   - source-to-index ACL propagation;
   - tenant and namespace filters;
   - raw chunk, metadata, debug, and citation fields;
   - query-time versus ingestion-time authorization;
   - revoked, deleted, stale, and cached content;
   - summaries, follow-up questions, exports, logs, and fallback sources;
   - downstream tools or agents that consume retrieved content.
8. Compare observed exposure with the authoritative matrix. Distinguish policy
   mismatch from stale policy, cache, route, index, or identity ambiguity.
9. Grade each pair `enforced`, `exposed`, `inconclusive`, `blocked`, or
   `not-tested`. Missing telemetry cannot produce `enforced`.
10. Remove fixtures, verify source and derived-store cleanup, and record residual
    retrieval or cached disclosure.

## Deliverable

Return the scope, authorization matrix, controlled-fixture register, tested
identity pairs, exposure-state receipts, policy mismatches, alternative
explanations, restricted evidence references, cleanup status, and owned fixes.

## Rationalizations to reject

- **“The model refused to quote it, so access control worked.”** Retrieval,
  context, citations, or debug fields may already have exposed the content.
- **“The source ACL is correct.”** Verify propagation through connectors,
  indexes, filters, caches, and response paths.
- **“A title is harmless metadata.”** Titles and metadata can disclose sensitive
  existence, ownership, or project context.
- **“The document was deleted.”** Derived stores and caches require separate
  cleanup evidence.
- **“An admin account can see everything, so the result is expected.”** Compare
  the tested identity with explicit authorized purpose and tenant scope.
- **“One denied query proves isolation.”** Coverage requires the relevant
  identities, routes, fields, and lifecycle states.
