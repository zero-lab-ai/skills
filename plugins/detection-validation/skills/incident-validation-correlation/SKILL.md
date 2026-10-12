---
name: incident-validation-correlation
description: "Correlates supplied sanitized incident observations with separately approved isolated defensive-validation receipts across prevent, observe, detect, contain, and recover. Use for defensive learning comparison without live response, hunting, technique design or execution, detection authoring, case management, findings, or reporting."
allowed-tools: Read Grep Glob
---

# Incident validation correlation

## When to Use

- Correlate incident evidence with validation results.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Purpose

Answer one question: is an exact, pre-approved isolated validation genuinely
comparable to a supplied sanitized incident observation, and what defensive
learning survives? A complete ledger does not close an incident, verify
remediation, establish attribution or scope, or prove coverage.

## Boundary

Never contact assets, identities, sources, responders, or attackers. Never hunt,
respond, validate production, design or execute techniques, author detections,
manage cases, create findings, or write reports. Reject hostnames, addresses,
accounts, tenants, domains, paths, victim identities, IOCs, raw events, packets,
memory, malware, credentials, tickets, certificates, commands, scripts, queries,
rules, payloads, technique procedures, tool syntax, infrastructure, and
operational timelines. Use sanitized opaque references and digests only.

## Workflow

1. Accept only supplied incident packages and supplied, immutable,
   pre-approved validation cases and receipts.
2. Stop on restricted content. Never quote a rejected value.
3. Preserve separate incident acceptance and validation execution authority.
4. Report only generic diagnostic codes; never reflect restricted values.
5. Require exactly one observation and one pre-approved case for each supplied
   learning item and objective.
6. Require observation time before learning creation and independent validation
    approval after learning creation.
7. Require exact semantic-equivalence binding across observation class,
    immutable fixture, objective, environment limitations, and expected benign
    effect. Taxonomy similarity is not equivalence.
8. Mark weak equivalence `not-comparable`. Never claim that a lab reproduces a
    production incident or that production predicts lab behavior.
9. Keep prevent, observe, detect, contain, and recover comparisons separate.
10. Keep observation, execution, benign-effect, telemetry, alert, containment,
    recovery, cleanup, custody, and policy evidence roles separate. Require the
    closed role/outcome matrix; labels never override contradictory evidence.
    Consume every supplied authority and environment exactly once.
11. An alert is not complete telemetry or control evidence. A validation alert
    is not incident reproduction.
12. Treat alert absence under unhealthy telemetry as `inconclusive`.
13. Accept only isolated-lab or dedicated-test-tenant validation receipts.
14. Treat a fired stop as terminal. Allow only later cleanup, custody, and
    withdrawal; retry needs a new separately approved case.
    Authority expiry, revocation, fixture drift, and environment drift are also
    terminal: no later execution, evidence, or result is valid.
15. Require exact current policy proof and a closed NA reason code for
    not-applicable. Keep every objective in the denominator.
16. Keep handoff occurrence, approval, authority, result, and withdrawal
    separate with typed exact receipts. Expiry, revocation, fixture drift,
    environment drift, and a fired stop require withdrawal. A handoff never
    grants authority. Custody precedes every consuming result, gap, or handoff
    receipt; withdrawal evidence is exact for its trigger.
17. Interpret `complete` as correlation complete only. Never call the incident
    closed or remediation verified.
18. Return comparison states, cycle states, learning-gap IDs, and handoff states.
    Never assign severity, compliance, or detection coverage.

## Report

State the ledger identifier, exact objective denominator, comparison and cycle
counts, learning gaps, and handoff states. Add: “Correlation consistency only;
no live interaction, incident closure, remediation verification, attribution,
severity, or coverage claim occurred.”

## Rationalizations to reject

- **“The taxonomy matches.”** Similar labels do not establish equivalence.
- **“The lab reproduced production.”** Environment limits survive correlation.
- **“The alert proves detection.”** Alert evidence is only one role.
- **“No alert means a gap.”** Unhealthy telemetry makes the result inconclusive.
- **“The stop cleared, so retry.”** A stop is terminal for that approved case.
- **“Cleanup means validation succeeded.”** Cleanup proves only cleanup.
- **“The handoff approved execution.”** Handoffs transfer defensive learning only.
- **“Complete means the incident is closed.”** It means correlation complete.
