---
name: security-test-tool-governance
description: "Governs supplied benign security-test tool artifacts through purpose, authority, provenance, artifact integrity, safety-test evidence, version-bound review, custody, change control, and defensive handoff. Use when reviewing proposed security tooling or deciding whether an externally supplied artifact is ready for an authorized isolated test, without generating source code, payloads, build procedures, bypasses, or deployment instructions."
allowed-tools: Read Grep Glob
---

# Security test tool governance

Produce an evidence-bound ledger for externally supplied opaque benign artifacts.

## When to Use

- Reviewing proposed security tooling or deciding whether an externally supplied artifact is ready for an authorized isolated test, without generating source code, payloads, build procedures, bypasses, or deployment instructions.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Boundary

Accept inventory facts and external receipts only. Never fetch, reconstruct,
modify, compile, sign, execute, deploy, or distribute a referenced tool. Never
provide source code, pseudocode, tool commands or flags, build recipes, payloads,
loaders, injection or in-memory execution instructions, persistence, credential
access, lateral movement, C2, covert channels, evasion, packing, obfuscation,
signature avoidance, telemetry blinding, security-control tampering, target
selection or locators, stealth rankings, or quieter-tool recommendations.

Only isolated labs and dedicated non-production test tenants with explicit
separation evidence are supported. Release is an externally evidenced controlled
handoff to an approved internal lab. Production use, customer deployment, public
distribution, and operational use have no contract state. Restricted or unknown
capabilities are inventory facts that force prohibition and quarantine; an
authorization cannot waive that boundary.

## Workflow

1. Record purpose, policy snapshot, assessment cutoff, scope, authority window,
   permitted governance actions, operator roles, non-production boundary, and
   numeric ceilings. Missing authority remains visible; governance readiness
   never grants execution authority.
2. Register each supplied artifact, source, configuration, supplier, component,
   and declared capability using only opaque references and exact SHA-256
   digests. A digest establishes identity, not safety. Do not open opaque content
   to fill an evidence gap.
3. Have the offline review recompute the versioned canonical manifest from
   candidate identity and sorted component/capability declarations. Any material
   change requires a replacement candidate and fresh downstream evidence; a
   supplied digest assertion cannot inherit prior approval.
4. Pin the sandbox fingerprint, synthetic-data boundary, production separation,
   containment, rollback baseline, and validity window. Drift invalidates current
   claims even when the artifact bytes are unchanged.
5. Instantiate all assurance criteria for every candidate before importing
   results. Applicability comes from the artifact-class matrix. Keep planned,
   failed, blocked, prohibited, inconclusive, and evidence-bound not-applicable
   cells in the denominator; absence is never a pass.
6. Import separate provenance, integrity, dependency/source review, independent
   review, containment, functional, safety, observability, stop, and restoration
   receipts. Every supporting member must match its exact binding tuple and
   chronology. Supplier attestations cannot substitute for independent review;
   execution evidence cannot substitute for criterion-outcome evidence.
7. Record current readiness gates, reserved and consumed budgets, applicable
   successfully pretested stop controls, custody readiness, and cleanup readiness.
   Derive readiness from these records, authority, identity, coverage, and issues.
   Preserve approval-required, blocked, and prohibited states without laundering
   them into lab-ready.
8. Import facts from separately authorized bounded synthetic lab validation.
   This workflow does not perform it. Bind each run to its exact case, authority,
   candidate/manifest, sandbox/fingerprint, policy, gate, budget, stop, and cleanup
   records. Keep execution, criterion outcome, observability, stop event, and
   cleanup receipts distinct. Failed and stopped runs consume budget; a fired
   stop is terminal. A retry needs remaining capacity and a later decision.
9. Preserve custody for each evidence artifact and its aliases. Keep failed,
   stopped, inconclusive, and unexecuted cases. Evidence disposal requires its own
   external authority and receipt; endpoint cleanup cannot authorize it. Record
   cleanup separately and retain blocked or failed restoration obligations.
10. Derive issues and remediation from assurance failures and contradictions.
    A supplied change receipt does not close an issue. Record externally
    authorized change, a materially new replacement candidate, and later exact
    verification of the original criterion in an equivalent approved sandbox.
    Preserve the failed candidate, supporting evidence, and unresolved issues.
11. Derive lab eligibility only with complete applicable passing assurance,
    current identities and approval, complete run cleanup, and no blocking or
    prohibited capability. Validate a supplied release occurrence receipt against
    the exact candidate, manifest, artifact, sandbox, scope, policy, authority,
    internal-lab recipient, channel, owner, and window. Have the review recompute
    the canonical handoff digest over the exact recipient and release facts;
    recipient class is only `internal-lab`, and channels are only
    `controlled-repository`, `sealed-offline-media`, or `managed-lab-import`;
    approval, occurrence, and withdrawal receipts must bind that digest. Changed
    handoff facts invalidate inherited receipts. Occurrence is not approval.
12. Derive expiry and withdrawal obligations after authority expiry/revocation,
    policy or sandbox drift, material change, disposed evidence, prohibited
    behavior, or a blocking issue. A later exact withdrawal receipt records
    withdrawn. Export opaque blocker, cleanup, issue, remediation, and handoff
    IDs to defensive owners without operational instructions.

13. Treat a complete review as an internally consistent record only. It never
    establishes authenticity, safety, execution authority, production
    suitability, or release permission.

## Boundary with adjacent skills

`detection-resilience-test-plan` owns separate hypotheses, attempts, defensive
outcomes, test cleanup, and detector remediation. This skill owns artifact
provenance, assurance, custody, version validity, and defensive handoff beforehand.
Neither constructs implementations. `protocol-exploitation-assessment` owns
service weakness applicability and bounded reproduced faults; do not emit protocol
requests or vulnerability proofs here. `opsec-planning` owns observer analysis;
do not select quieter tools. `recon-automation-governance` owns jobs, targets,
schedules, contact budgets, and orchestration; this skill owns candidate assurance.
`findings-report` owns final findings and impact-derived severity. Export typed
assurance issues here, without assigning vulnerability ratings.
`binary-fault-triage` and `binary-fault-validation-readiness` own binary fault
prerequisites; never derive exploit primitives or feasibility here.
`engagement-report-assembly` owns the final engagement report; provide only the
typed governance export.

## Rationalizations to reject

- “The lab is authorized, so generate or execute the helper.” Authority cannot
  waive the opaque-artifact boundary; import external facts instead.
- “It is signed, reproducible, or hash-matched, so it is safe.” These establish
  limited identity/provenance facts and cannot replace independent assurance.
- “The function is optional or disabled.” Restricted or unresolved inventory
  still forces prohibited readiness and quarantined lifecycle.
- “The artifact barely changed; carry forward the review.” Material identity
  includes source, configuration, dependencies, capabilities, sandbox, and policy;
  mismatches invalidate current downstream claims.
- “Discard failed cases or count only tested cells.” This hides the denominator
  and creates unsupported coverage. Preserve every required cell and result.
- “A successful run proves every safety criterion.” Receipt roles and bindings
  are separate; a run cannot satisfy unrelated criteria.
- “Cleanup permits deleting inconvenient evidence.” Custody disposition and
  endpoint restoration need independent authority and receipts.
- “The fix or handoff happened, so approval is implied.” Changes require later
  verification; occurrence receipts never replace approval or withdrawal proof.
