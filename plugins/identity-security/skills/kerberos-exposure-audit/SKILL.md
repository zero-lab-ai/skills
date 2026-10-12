---
name: kerberos-exposure-audit
description: "Audits supplied sanitized Kerberos governance evidence for policy, protection, monitoring, and evidence-handling exposure without contacting live systems. Use when reviewing a defensive Kerberos evidence package or assessing identity-control coverage."
allowed-tools: Read Grep Glob
---

# Kerberos exposure audit

Use this skill only for passive review of an already-supplied, sanitized evidence
package. It is an evidence audit, not discovery, validation, or authorization.

## When to Use

- Reviewing a defensive Kerberos evidence package or assessing identity-control coverage.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Boundary

Never query, authenticate to, or contact a live system. Never request, forge,
replay, crack, decode, extract, or use tickets, credentials, secrets, or session
material. Never enumerate live identities, services, realms, hosts, or addresses.
Never coerce authentication, build an attack path, or provide commands, scripts,
queries, tool syntax, payloads, or configuration bodies.

Reject raw or encoded ticket material, ticket-derived usable digests, hashes,
session keys, passwords, secrets, service-principal strings, and real account,
domain, realm, host, or address values. Keep diagnostics generic and never quote
rejected content.

## Workflow

1. Accept only opaque IDs and 64-character lowercase hexadecimal digests.
2. Record the engagement cutoff, closed policy, sanitized snapshot receipt, and
   opaque directory and scope references.
3. Inventory only supplied subjects: identity, service identity, trust boundary,
   policy scope, or directory control. Do not discover new subjects.
4. Create exactly one coverage cell for every subject and each policy-
   required Kerberos control dimension.
5. Keep configuration, control effectiveness, freshness, and observed result as
   independent tracks. Do not infer one track from another.
6. Bind every current claim to the exact subject, snapshot and digest, scope,
   directory reference, policy and digest, control and fingerprint, and window.
7. Accept evidence only when it is supplied-passive, sanitized, inside its own
   validity window, no later than the cutoff, eligible, and in retained custody.
8. Keep policy, configuration, control assurance, telemetry configuration,
   telemetry health, and result observation roles separate.
9. Treat event absence as `not-observed` only when exact current telemetry
    configuration and healthy telemetry evidence support that same cell.
10. Use `not-applicable` only with a closed reason and exact current policy
    evidence. Never use it to remove a difficult subject or dimension.
11. Record each observed exposure as one immutable open finding. This ledger
    cannot close findings or claim remediation completion.
12. Record only defensive handoffs for assessment review, evidence refresh, or
    remediation review. A handoff grants no authority.

## Interpretation rules

- `complete-no-observed-exposure` means every applicable cell has current exact
  evidence and no exposure was observed. Exact policy-backed non-applicability
  does not create a material unknown. This aggregate does not mean secure.
- `complete-with-exposure` means at least one current exact observation is
  present and has an open finding.
- `material-unknowns` means one or more material tracks are unknown,
  unavailable, or indeterminate.
- `stale` means historical evidence cannot support a current claim.
- `incomplete` means the required coverage matrix is not complete.

## Report

Return the aggregate, state counts, open finding IDs, defensive handoffs, and
generic conflict codes. Keep opaque references opaque. Do not reconstruct or
describe operational identity values from the evidence package.

## Rationalizations to reject

- **“A passive check is harmless against production.”** Contact is still outside
  this skill; use only supplied evidence.
- **“The ticket is sanitized enough.”** Ticket bodies and usable derivatives do
  not belong in this ledger.
- **“Policy says the control exists.”** Policy evidence cannot substitute for
  configuration or effectiveness evidence.
- **“Configuration proves visibility.”** Telemetry configuration is not healthy
  collection or an exact result observation.
- **“No event means no exposure.”** Absence is meaningful only with current,
  healthy, complete telemetry evidence for the exact cell.
- **“The label did not change.”** Snapshot, policy, or control fingerprint drift
  invalidates prior claims.
- **“We can close the finding here.”** This ledger preserves open observations;
  later remediation belongs in a separately evidenced post-change record.
- **“The handoff approved action.”** Handoffs transfer defensive work only.
