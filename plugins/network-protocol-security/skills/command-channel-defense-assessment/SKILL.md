---
name: command-channel-defense-assessment
description: "Assesses supplied defensive evidence for prevention, visibility, detection, containment, and recovery coverage against opaque command-channel scenarios. Use when reviewing command-and-control exposure or control gaps without designing infrastructure, live tests, or operational guidance."
allowed-tools: Read Grep Glob
---

# Command channel defense assessment

Measure defensive assurance against supplied opaque scenarios. This is an
evidence review, not a design, simulation, validation plan, or authorization.

Never represent topology, components, services, channels, endpoints,
transports, infrastructure, implementation recommendations, or rule, query, or
configuration bodies. Never supply commands, live identifiers, credentials,
payloads, evasion, deployment, or testing guidance.

## When to Use

- Reviewing command-and-control exposure or control gaps without designing infrastructure, live tests, or operational guidance.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record one assessment cutoff and engagement window. Bind the governing
   policy and opaque scope reference.
2. Record environment and control fingerprints without names, addresses,
   products, services, or implementation details.
3. Classify the environment. Production review is passive and sanitized only.
   Active or imported validation evidence must bind an `isolated-lab` or
   `dedicated-test-tenant` with an active-validation receipt.
4. Keep three independent tracks per coverage cell: configuration is
   `unknown`, `absent`, or `present`; health is `unknown`, `degraded`, or
   `healthy`; validation is `not-tested`, `inconclusive`, `supported`, or `gap`.
5. Create exactly one cell for each scenario and applicable objective:
   `prevent`, `observe`, `detect`, `contain`, and `recover`.
6. Keep policy, configuration, health, observation, detection, containment,
   recovery, and validation evidence separate.
7. Bind every cited item to the exact scenario, bundle digest, environment and
   control fingerprints, scope, policy, validation receipt, assessment window,
   and custody record.
8. Derive the cell state from the three tracks. Configuration or health evidence
   without validation is `evidence-only`, never `validation-supported`.
9. Record observed validation gaps as immutable open facts. A later fix creates
   a new ledger; it does not rewrite the record that observed the gap.
10. Use `not-applicable` only with a closed policy reason and current policy
    evidence. Missing coverage is not non-applicability.
11. Record defensive handoffs only: evidence refresh, control review, or gap
    remediation. A handoff is neither approval nor completion.
12. Resolve contradictions without changing scenario identity or adding
    operational detail.

## Derivation rules

- `unassessed`: all three tracks are unknown or not tested.
- `evidence-only`: configuration or health is known, but validation is not.
- `validation-supported`: current exact validation supports the objective.
- `gap-observed`: current exact validation demonstrates a gap and an immutable
  gap record exists.
- `inconclusive`: current exact validation is inconclusive.
- `stale`: prior validation is expired, disposed, or invalidated by drift.
- `not-applicable`: current exact policy evidence supports an allowed reason.
- A scenario is validated only when every applicable objective is currently
  validation-supported. One stale, gap, inconclusive, or unassessed cell limits
  the aggregate.

## Report

Return opaque scenario IDs, per-objective derived states, aggregate counts,
open gap IDs, defensive handoffs, and blocking reason codes. Do not quote
restricted values from rejected input.

## Boundary

- Receive scenario IDs and taxonomy receipts from an upstream assessment.
- Send authorized active validation to a separate isolated-lab workflow.
- Send gaps to detection, containment, or recovery owners without prescribing
  implementations.
- Treat `PASS` as consistency only, never authenticity, effectiveness, approval,
  completion, or authority.

## Rationalizations to reject

- **“Configured means covered.”** Presence does not prove health or outcome.
- **“Healthy telemetry proves detection.”** Visibility and detection are
  separate claims with separate evidence.
- **“No alert proves a gap.”** Silence without exact observation and validation
  evidence is inconclusive.
- **“Production is the most realistic test.”** This skill permits passive,
  sanitized production review only.
- **“An imported result applies here.”** It must bind the exact scenario,
  non-production fingerprint, control fingerprint, scope, policy, and window.
- **“The control name is unchanged.”** Fingerprint drift invalidates prior
  claims.
- **“We fixed the gap, so close it here.”** Preserve the observed fact and open
  a later assessment.
- **“The handoff approves the work.”** A handoff transfers defensive work; it
  never grants authority or attests completion.
