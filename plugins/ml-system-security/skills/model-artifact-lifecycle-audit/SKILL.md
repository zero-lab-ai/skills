---
name: model-artifact-lifecycle-audit
description: "Audits how model artifacts are accepted, validated, stored, selected, loaded, executed, monitored, and retired. Use when reviewing model registries, loaders, CI/CD pipelines, scanner-to-runtime gaps, or ML supply-chain controls."
metadata:
  portability: universal
  discipline: blue-team
  domain: ai-systems
  tags: [models, artifacts, supply-chain, registries, mlops]
---

# Model artifact lifecycle audit

Trace a model artifact from intake through retirement. The audit focuses on
control and evidence gaps between scanners, registries, selectors, loaders,
runtimes, and downstream consumers; it does not build weaponized models.

## When to Use

- Reviewing model upload, registry, promotion, deployment, or retirement paths.
- Auditing artifact formats, scanners, signatures, provenance, loader behavior,
  CI/CD jobs, scheduled pipelines, or workload identity.
- Investigating whether an accepted artifact could reach a more privileged
  execution context than the intake controls imply.

## When NOT to Use

- Do not create malicious model artifacts or provide payload-building steps.
- Do not load an untrusted artifact to prove a control gap unless a separate,
  isolated validation is explicitly authorized.
- Do not treat a clean scanner result as proof of safe runtime behavior.

## Lifecycle states

Track each state independently: `submitted`, `accepted`, `validated`, `stored`,
`registered`, `selected`, `promoted`, `loaded`, `executed`, `served`,
`monitored`, `revoked`, `deleted`, and `residually-present`. A receipt for one
state does not prove the next.

## Workflow

1. Define the systems, artifact classes, environments, identities, business
   owners, evidence window, and audit boundaries.
2. Inventory every accepted artifact format and packaging layer, including
   archives, configuration, tokenizer or processor files, custom code,
   dependencies, conversion outputs, and generated caches.
3. Map producers, intake endpoints, validators, scanners, registries, object
   stores, promotion gates, selectors, deployment systems, loaders, runtimes,
   serving endpoints, and downstream consumers.
4. Record the identity and privilege at each transition. Include human,
   workload, CI/CD, scheduled-job, registry, and runtime identities.
5. Trace integrity controls: origin, digest, signature, attestation, dependency
   lock, policy decision, quarantine, immutability, approval, and revocation.
6. Compare validator semantics with loader semantics. Identify content the
   loader interprets but the scanner ignores, transformations that invalidate a
   prior decision, and defaults that enable custom or executable behavior.
7. Review selection and activation separately. A stored artifact is not loaded;
   a selected artifact is not executed; a served model does not prove which
   digest is active without runtime evidence.
8. Examine automated consumers. Determine whether CI, evaluation, conversion,
   optimization, deployment, or scheduled jobs load artifacts under identities
   or network access stronger than the submitter's.
9. Check monitoring and response: exact artifact identity in logs, promotion and
   load events, policy failures, anomalous runtime behavior, revocation
   propagation, rollback, deletion, cache eviction, and residual copies.
10. For every gap, state the weakest lifecycle claim supported, affected trust
    transition, plausible consequence, missing evidence, and safe remediation.

## Deliverable

Return the artifact and format inventory, lifecycle and identity map, control
matrix, scanner-versus-loader comparison, automation and privilege findings,
state-specific evidence gaps, revocation and cleanup assessment, and prioritized
remediation. Keep unexecuted hypotheses labeled as hypotheses.

## Rationalizations to reject

- **“The registry accepted it, so the model is approved.”** Intake, validation,
  promotion, and activation are different states.
- **“The scanner supports the format.”** Coverage depends on which fields and
  embedded components the scanner interprets compared with the loader.
- **“The digest matches, so the artifact is safe.”** Integrity proves identity,
  not trustworthiness.
- **“Custom code is disabled by default.”** Verify the effective loader and
  deployment configuration at the actual execution boundary.
- **“The model never reaches production.”** Evaluation and conversion workers
  may hold stronger identity or network access than production serving.
- **“Deletion from the registry removes it.”** Object stores, caches, converted
  artifacts, running workloads, and replicas may persist.
