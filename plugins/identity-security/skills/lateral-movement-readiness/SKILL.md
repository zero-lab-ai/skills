---
name: lateral-movement-readiness
description: "Reviews an already-supplied lateral movement candidate for exact upstream map binding, authorization, non-production isolation, containment, telemetry, stop control, rollback, cleanup ownership, custody, tool governance, and a separate-validation handoff. Use before transferring a candidate to a lab validation team."
allowed-tools: Read Grep Glob
---

# Lateral movement readiness

This skill answers one narrow question: may an already-supplied movement
candidate be handed to a separate validation team? It checks records; it does
not grant execution authority.

Never create, select, rank, enrich, or modify a movement candidate. Never
produce commands, credentials, payloads, protocols, target locators, evasion,
deployment, execution steps, or infrastructure. Accept only opaque identifiers
and digests from the supplied record.

## When to Use

- Review lateral movement readiness for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Set one engagement assessment time and window. Record the governing policy
   and every supplied movement; the review treats all of them as the
   denominator.
2. Bind each movement to the exact upstream map identifier and digest, scope,
   source, destination, policy, and environment. A digest or reference change
   is a different candidate, not a harmless edit.
3. Accept only `isolated-lab` or `dedicated-non-production` environments. A
   production, shared, ambiguous, or merely named “test” environment is not
   eligible.
4. Record bounded `separate-validation` authority. Bind it to the complete
   movement tuple and assessment window. Revocation and expiry take effect
   immediately.
5. Cite independent evidence for map receipt, environment assurance,
   containment, telemetry, stop pretest, rollback, cleanup readiness, custody,
   and tool governance. Evidence must be current, eligible, and exactly bound.
6. Assign cleanup ownership before readiness. A plan without an accountable
   owner remains blocked.
7. Record one coverage cell for every movement and required role. Missing cells
   cannot become implicit non-applicability.
8. Record a handoff only after exact approval and record receipts. Map drift,
    expiry, revocation, or a fired stop makes an existing handoff
    `withdrawal-required`. Resumption needs a new review; it is never automatic.
9. For withdrawal, cite a later exact withdrawal receipt. Preserve the prior
    record and chronology.
10. Complete the assessment and resolve every finding without altering the supplied
    movement identity.

## Decision rules

- `prohibited` overrides every other state.
- `approval-required` means the bounded authority is absent, expired, or not
  yet effective; it does not mean “almost approved.”
- `blocked` means a non-authority prerequisite is absent, stale, failed, or
  contradictory, including a fired stop.
- `ready-for-separate-validation` requires every exact join and current receipt.
- A recorded handoff is historical fact. It becomes `withdrawal-required` when
  its supporting state ceases to be current, and `withdrawn` only after proof.
- “Not applicable” needs a documented reason; convenience is not evidence.

## Report

Return the candidate ID, derived gate and validity, blocking codes, coverage
counts, handoff state, and the next governance action. Keep all identifiers
opaque. Do not quote restricted input in diagnostics or narrative.

## Boundary

- Use `lateral-movement-map` to construct or revise the upstream map.
- Use a separate validation skill or authorized operator for any execution.
- Send environment construction, telemetry configuration, or rollback
  implementation back to their accountable owners.
- Treat a complete record as record consistency only, never authenticity,
  environment safety, operator competence, or execution authorization.

## Rationalizations to reject

- **“It is only a lab.”** Labels do not prove production separation or
  containment.
- **“The map is close enough.”** A changed digest, source, destination, or scope
  invalidates the reviewed identity.
- **“The approval covers the general technique.”** Authority is exact to the
  candidate, environment, bindings, action, and time window.
- **“Telemetry can be checked during the run.”** Separate validation begins
  only after current observability assurance exists.
- **“A stop plan is enough.”** The stop control needs independent, current,
  correctly bound pretest evidence; firing it invalidates readiness.
- **“Cleanup belongs to whoever runs it.”** Ownership and rollback evidence are
  prerequisites, not post-run paperwork.
- **“The old handoff resumes when the issue clears.”** Withdrawal and a fresh
  review are required; no auto-resume exists.
- **“PASS means approved.”** The review proves only internal consistency of
  supplied facts.
