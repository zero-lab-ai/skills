---
name: defensive-control-evidence-synthesis
description: "Synthesizes supplied evidence-backed defensive assessment results and administrative receipts into a scope-bound control-evidence matrix that preserves lineage, freshness, contradictions, unknowns, and gaps. Use when consolidating defensive control evidence without scanning, scoring, certifying, or rewriting findings."
allowed-tools: Read Grep Glob
---

# Defensive control evidence synthesis

## When to Use

- Consolidating defensive control evidence without scanning, scoring, certifying, or rewriting findings.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Purpose

Build and validate a closed matrix from already-supplied specialist artifacts
and sanitized administrative, validation, or remediation-verification receipts.

## Boundary

Never contact a system, scan, sample, query, test, or execute. Reject raw logs,
configurations, ACLs, credentials, tickets, certificates, packets, live
identifiers, commands, queries, rules, test bodies, attack paths, and remediation
procedures. Never create, rewrite, merge, close, or severity-rank findings.
Never calculate a posture score, grade, maturity level, compliance result,
certification, or exploitability rank.

## Workflow

1. Accept only exact passed specialist artifacts and sanitized administrative,
   validation, or remediation-verification receipts already supplied.
2. Stop on operational or restricted content. Do not quote rejected values.
3. Preserve producer, artifact format, artifact digest, review receipt, scope,
   policy, time, window, origin lineage, upstream class, polarity, limitations,
   applicability, and strength.
4. Report only generic diagnostic codes; never reflect restricted values.
5. Keep all ten policy dimensions in the exact scope-by-dimension denominator.
6. Do not strengthen, reverse, or reinterpret an upstream claim. Preserve or
   weaken it only when freshness or custody requires that result.
7. Cap administrative evidence at `documented` or `configured`.
8. Treat a review pass as artifact-structure evidence, not proof of no exposure
   or proof that a control works.
9. Keep telemetry, detection, containment, and recovery evidence independent.
10. Accept a no-finding claim only from exact, complete, current upstream
    coverage.
11. Deduplicate shared origin lineage before assessing independence.
12. Require one open contradiction for eligible opposing independent claims.
13. Use `not-applicable` only when source, claim, binding, and cell carry the
    same exact current policy reason.
14. Require one immutable finding reference for each current or stale,
    otherwise-valid exposure claim; do not edit the upstream finding.
15. Treat remediation occurrence as unverified until a later exact verification
    receipt independently binds the earlier occurrence, scope, and dimension.
16. Keep evidence gaps administrative. They are not technical findings.
17. Keep handoffs exact-bound, chronological, defensive, and non-authorizing.
18. Return exact state counts, contradiction IDs, gap IDs, and finding-reference
    IDs. Never produce a score.

## Report

State the matrix identifier, exact state counts, contradictions, evidence gaps,
and immutable finding references. Add: “Internal synthesis consistency only; no
live interaction, score, compliance determination, certification, or finding
modification occurred.”

## Rationalizations to reject

- **“The record is complete, so there is no exposure.”** Completeness validates
  the supplied artifact contract, not the absence of findings.
- **“Configured means validated.”** Administrative receipts cannot prove
  observation or validation.
- **“Telemetry means detection.”** Collection evidence does not prove a
  detection outcome.
- **“Detection means containment or recovery.”** These are separate claims.
- **“Two copies are independent.”** Shared origin lineage is one source.
- **“Implementation closed the gap.”** Occurrence is not later verification.
- **“A score makes this easier.”** Aggregation would erase unknowns and disputes.
- **“We can clean up upstream findings.”** This skill never rewrites them.
