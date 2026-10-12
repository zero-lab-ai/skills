---
name: model-serving-exposure-audit
description: "Audits model-serving APIs, administrative and debug surfaces, vector stores, object storage, caches, workload identity, metadata access, and orchestration credentials. Use when reviewing the deployed infrastructure around model inference."
metadata:
  portability: universal
  discipline: blue-team
  domain: ai-systems
  tags: [model-serving, infrastructure, workload-identity, debug, exposure]
---

# Model serving exposure audit

Review the infrastructure that loads and serves models. Separate network
reachability, authentication, authorization, effective identity, and
demonstrated access so a visible endpoint does not become an overstated finding.

## When to Use

- Reviewing model servers, gateways, batch inference, deployment controllers,
  or supporting data services.
- Auditing administrative, debug, metrics, metadata, storage, secret, and
  workload-identity exposure around inference.
- Investigating whether a serving component has more authority than its role
  requires.

## When NOT to Use

- Do not actively enumerate, authenticate to, or exploit a service without the
  corresponding written authority.
- Do not retrieve real credentials or sensitive model data to prove a control
  gap when configuration and benign identity evidence suffice.
- Do not treat a banner, port, or product name as proof of a vulnerability.

## Workflow

1. Define environments, networks, clusters, accounts, namespaces, services,
   identities, evidence window, approved observation methods, and exclusions.
2. Inventory the serving chain: clients, API gateways, model routers, inference
   servers, batch workers, deployment controllers, registries, object stores,
   vector databases, feature stores, caches, queues, telemetry, and admin planes.
3. Inventory surfaces by function rather than port:
   - inference, streaming, embedding, and batch APIs;
   - health, metrics, profiling, tracing, debug, and documentation endpoints;
   - model load, unload, configuration, adapter, and promotion controls;
   - storage, cache, queue, registry, and vector-store interfaces;
   - orchestrator, node, metadata, secret, and workload-identity services.
4. Record each surface's bind address, network path, authentication,
   authorization, tenant boundary, rate control, transport protection, and
   logging from supplied configuration or approved observation.
5. Map effective identities and privileges. Include service accounts, instance
   roles, managed identities, tokens, filesystem access, device access, network
   egress, registry permissions, secret access, and impersonation rights.
6. Trace sensitive flows: prompts, retrieved context, model artifacts, adapters,
   outputs, telemetry, credentials, metadata, and temporary files.
7. Keep evidence states separate: `declared`, `reachable`, `authenticated`,
   `authorized`, `resource-accessed`, and `effect-demonstrated`.
8. Review cross-service trust: gateway-to-server headers, proxy identity,
   controller-to-node authority, registry-to-loader trust, callback destinations,
   and tenant or namespace propagation.
9. Review hardening and response: minimal images, patch and dependency evidence,
   filesystem and process isolation, egress limits, secret rotation, exact model
   identity in logs, alerting, revocation, rollback, and residual workloads.
10. Produce separate validation handoffs for unresolved live behavior; keep this
    audit from becoming an exploit plan.

## Boundary with adjacent skills

- Use `ai-surface-recon` for externally observable AI-system mapping.
- Use `model-artifact-lifecycle-audit` for artifact intake through retirement.
- Use `agent-surface-audit` for agent tool definitions and parameter risk.

## Deliverable

Return the service and surface inventory, network and trust map, effective
identity matrix, sensitive-flow map, evidence-state findings, hardening gaps,
telemetry and response coverage, unknowns, and bounded validation handoffs.

## Rationalizations to reject

- **“It is only reachable inside the cluster.”** Internal reachability still
  intersects compromised workloads, tenants, and service identities.
- **“Authentication is enabled.”** Verify authorization, audience, target,
  tenant, and privilege after authentication.
- **“The metadata service is standard.”** Effective workload access depends on
  platform configuration, identity scope, and network controls.
- **“The debug endpoint contains no secrets.”** It may disclose paths, models,
  arguments, environment, topology, or control functions.
- **“The model server only performs inference.”** Loaders, adapters, plugins,
  filesystems, devices, and callbacks can carry broader authority.
- **“A version match proves exploitability.”** Preserve applicability and live
  validation as separate evidence.
