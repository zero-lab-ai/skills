---
name: assessment-sequence-governance
description: "Validates supplied immutable ordered manifests of opaque defensive assessment actions for authority, safeguards, evidence, and separate-operator review. Use when reviewing assessment sequencing without creating, changing, or executing actions."
allowed-tools: Read Grep Glob
---

# Assessment sequence governance

## When to Use

- Reviewing assessment sequencing without creating, changing, or executing actions.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Purpose

Validate a supplied ledger without designing the assessment. A passing result
means only that the recorded sequence is internally consistent for separate
review. It is never execution authority.

## Boundary

Never create, select, add, remove, reorder, rank, or substitute actions or
dependencies. Never choose targets, routes, tactics, timing, or tools. Never
schedule or run anything. Do not provide commands, queries, configurations,
credentials, payloads, protocols, infrastructure, stealth, or deployment
guidance. Accept opaque identifiers and digests only.

## Workflow

1. Obtain the already-supplied immutable ledger and confirm the operator wants
   an offline governance review.
2. Stop if the material contains operational instructions or live identifiers.
   Do not quote the rejected value.
3. Preserve the supplied manifest and action order byte-for-byte. Do not repair
   missing actions, dependencies, bindings, or evidence.
4. Reject malformed shapes, types, references, timestamps, digests, restricted
   content, duplicate identifiers, and an empty assessment universe.
5. Keep manifest integrity separate from action identity, authority,
   prerequisites, environment, budget, stop, cleanup, and custody coverage.
6. Require exact action, sequence, manifest, scope, environment, policy,
   authority, and window joins. Similar-looking records never substitute.
7. Preserve supplied predecessor sets. Verify acyclicity, contiguous ordinals,
   and predecessor chronology; do not improve or reorder the sequence.
8. Treat budgets as nontransferable reservations with nonnegative integer
   attempts, duration, impact, and evidence-byte dimensions.
9. Require a passed stop pretest, an armed available stop, and exact action-set
   binding. Bind canonical budget, stop, and cleanup fingerprints through the
   authority and every supporting evidence record.
10. Accept cleanup `not-required` only with exact current policy proof. Never
    infer cleanup from silence.
11. Count every action against all nine required coverage roles. Never omit a
    blocked, prohibited, or historical action.
12. Derive the gate in precedence order: `prohibited`, `approval-required`,
    `blocked`, then `sequence-consistent`.
13. Treat a recorded handoff as historical custody of review work, not
    permission. Derive `withdrawal-required` after authority expiry or
    revocation, manifest or action drift, budget exhaustion, a fired or lost
    stop, cleanup loss, or custody loss.
14. Accept `withdrawn` only from a later exact withdrawal receipt. Never infer
    retry, resumption, or restored authority.

## Report

State the manifest identifier, derived gate, handoff state, contradictions,
coverage gaps, and withdrawal obligations. Add: “Internal consistency only;
separate review is required; no execution authority is granted.”

## Rationalizations to reject

- **“The order is obviously intended.”** Intent cannot repair an immutable
  manifest.
- **“A nearby authorization is close enough.”** Authority is an exact tuple.
- **“Unused budget can move to another action.”** Reservations do not transfer.
- **“The stop can be tested later.”** Readiness requires a passed prior pretest.
- **“No cleanup is probably needed.”** Not-required needs current policy proof.
- **“A recorded handoff permits the run.”** Handoffs grant no authority.
- **“We can reorder one dependency to make it safe.”** This skill never edits
  the supplied sequence.
- **“The record is complete, so proceed.”** Completeness means internally
  consistent for separate review only.
