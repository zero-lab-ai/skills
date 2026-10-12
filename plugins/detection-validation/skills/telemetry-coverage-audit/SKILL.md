---
name: telemetry-coverage-audit
description: "Audits supplied sanitized passive telemetry evidence for policy-defined visibility, retention, custody, and investigation readiness. Use when reviewing evidence quality or profile-specific telemetry usability without contacting sources or claiming detection coverage."
allowed-tools: Read Grep Glob
---

# Telemetry coverage audit

## When to Use

- Reviewing evidence quality or profile-specific telemetry usability without contacting sources or claiming detection coverage.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Purpose

Validate an already-supplied passive evidence ledger. A complete review means
only that the ledger is internally consistent with supplied policy. It does not prove
detection coverage, effectiveness, activity absence, or operational readiness.

## Boundary

Never contact, poll, query, sample, or test a source. Never write queries or
rules, configure collectors or sensors, execute techniques, or propose live
tests. Do not accept raw events, live identifiers, product names, hosts,
accounts, tenants, addresses, paths, endpoints, locators, credentials,
configuration bodies, target details, commands, scripts, or payloads. Never map
results to ATT&CK, threats, rules, or detection effectiveness.

## Workflow

1. Obtain the supplied ledger, policy receipt, requirement bundle, investigation
   profiles, and sanitized passive evidence.
2. Stop on operational content. Do not quote a rejected value.
3. Preserve opaque source, profile, scope, and evidence identifiers. Do not
   enrich them from outside the ledger.
4. Keep the twelve supplied-policy dimensions separate. Evidence for one role
    never substitutes for another.
5. Configuration cannot prove delivery; current health cannot prove historical
    continuity; field presence cannot prove populated required fields.
6. Policy retention cannot prove retained or retrievable data; access cannot
    prove retrieval; event absence cannot prove collection or activity absence.
7. Require exact source fingerprint, scope, policy digest, bundle digest,
    profile digest, dimension, NA reason, authority, and window bindings.
8. Require every source to participate in a nonempty profile. Count every
    source-profile-dimension cell in the denominator; never shrink it for
    missing, stale, gap, or prohibited evidence.
9. Use `not-applicable` only with an allowed reason and exact current policy
    proof. Neutralize all operational evidence in that cell.
10. Derive each cell as `supported`, `partial`, `gap`, `unknown`, `stale`, or
    `not-applicable`; never calculate a score.
11. Derive each source-profile usability from its weakest required cell:
    `usable`, `limited`, `unusable`, `unknown`, or `stale`.
12. Do not generalize usability between profiles, even on the same source.
13. Require one immutable open gap for every gap cell. This ledger cannot close
    a gap.
14. Keep handoffs defensive, exact-bound, and non-authorizing. A recorded
    handoff transfers review work only.

## Coverage-state decision table

| State | Use when |
| --- | --- |
| `supported` | Current, exact-bound evidence supports every required role for the cell |
| `partial` | Some required roles are supported and the missing roles are named |
| `gap` | Required evidence shows the capability is absent or unusable |
| `unknown` | Required evidence was not supplied or cannot be joined exactly |
| `stale` | Evidence exists but falls outside the policy freshness window |
| `not-applicable` | Current policy explicitly excludes the cell with an allowed reason |

`Unknown`, `stale`, and `gap` remain in the denominator. Do not improve a state
because another profile or source performed better.

## Report

State the ledger reviewed, coverage-state counts, profile usability, exact
evidence gaps, limitations, and open gap IDs. Add: “Internal ledger
consistency only; no source was contacted and no detection effectiveness is
claimed.”

## Rationalizations to reject

- **“The collector is configured, so delivery is covered.”** Configuration and
  delivery require different evidence roles.
- **“Health is green now, so continuity was good.”** A point-in-time health
  record cannot establish history.
- **“The schema contains the field.”** Presence does not prove population.
- **“Retention policy says thirty days.”** Policy does not prove retained or
  retrievable data.
- **“The reviewer has access.”** Access does not prove successful retrieval.
- **“No event was found.”** Absence proves neither collection nor activity
  absence.
- **“This source worked for another profile.”** Usability is profile-specific.
- **“One score is easier.”** A score hides which independent claim is weak.
- **“We can test the source to settle this.”** This skill is passive only.
