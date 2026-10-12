---
name: ai-surface-recon
description: "Maps an authorized AI system's externally observable models, retrieval paths, agent tools, guardrails, endpoints, and privileged consumers. Use when scoping an AI security assessment or building an evidence-bound attack-surface inventory."
metadata:
  portability: universal
  discipline: penetration-testing
  domain: ai-systems
  tags: [ai, reconnaissance, models, rag, agents]
---

# AI surface recon

Build an evidence-bound map of an AI system before deeper testing. Separate
what is observed from what is inferred, and separate passive collection from
actions that contact the target.

## When to Use

- Scoping an authorized AI security assessment.
- Inventorying model, retrieval, agent, guardrail, API, or privileged-consumer
  surfaces from supplied evidence and approved observations.
- Reconciling public documentation, client architecture material, and bounded
  target responses without treating any one source as authoritative.

## When NOT to Use

- Do not use this skill as authorization to probe an endpoint or enumerate an
  adjacent service.
- Do not use it to generate jailbreaks, exploit payloads, persistence, or
  destructive tests.
- Do not turn an unverified product label, error string, or model claim into a
  confirmed implementation fact.

## Workflow

1. Record the written scope: named systems, tenants, identities, environments,
   approved contact methods, exclusions, time window, and disruption ceiling.
2. Create an evidence register. Give each source an identifier, origin,
   collection time, collection method, integrity note, and handling limit.
3. Classify every collection action before using it:
   - `passive`: supplied artifacts or third-party material that does not contact
     the target;
   - `target-contact`: an approved request to a named in-scope service;
   - `prohibited-or-unapproved`: anything outside the written authority.
4. Inventory the visible surfaces:
   - user and service entry points;
   - model providers, routers, versions, and fallback behavior;
   - retrieval sources, ingestion paths, indexes, citations, and freshness;
   - agents, tools, plugins, connectors, memories, and approval gates;
   - system prompts, policy layers, filters, and output handling;
   - credentials, workload identities, callbacks, queues, and data stores;
   - logs, evaluations, monitoring, administrative planes, and deployment
     boundaries.
5. Map service handoffs. For each transition, record the producer, consumer,
   data or instruction crossed, trust change, identity used, and supporting
   evidence.
6. Identify privileged consumers: components that execute, retrieve, publish,
   approve, or act on model output. Rank these by consequence, not proximity to
   the model.
7. Record each claim as `observed`, `reported`, `inferred`, `contradicted`, or
   `unknown`. Keep inference and its supporting observations in separate fields.
8. Note candidate assessment surfaces without prescribing exploit steps. For
   each candidate, state the exact authorization needed, safe validation class,
   expected evidence, stop condition, and likely defensive owner.
9. Report coverage gaps. A surface not observed is `unknown`, not absent.

## Deliverable

Return:

- scope and collection-method table;
- evidence register;
- component and endpoint inventory;
- trust-zone and service-handoff map;
- privileged-consumer list;
- claim register with confidence and contradictions;
- bounded validation candidates; and
- unknowns, exclusions, and owner-assigned follow-ups.

## Rationalizations to reject

- **“The model named itself, so the fingerprint is confirmed.”** Model output
  is attacker-influenceable metadata, not implementation proof.
- **“A public hostname is fair game.”** Public reachability does not establish
  authorization.
- **“The vector database is behind the app, so it is not part of the surface.”**
  Retrieval handoffs can change model behavior and downstream actions.
- **“The callback proves command execution.”** A callback proves only the
  interaction represented by its receipt.
- **“No error appeared, so the guardrail is absent.”** Missing evidence cannot
  support a negative architecture claim.
- **“One endpoint represents the whole product.”** Routers, fallbacks, admin
  planes, and privileged consumers can have different trust boundaries.
