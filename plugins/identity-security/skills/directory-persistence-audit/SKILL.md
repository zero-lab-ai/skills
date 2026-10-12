---
name: directory-persistence-audit
description: "Audits supplied sanitized directory-service governance evidence for durable control and persistence exposure without contacting live systems. Use when reviewing defensive directory control, baseline, monitoring, or exception evidence."
allowed-tools: Read Grep Glob
---

# Directory persistence audit

Use this skill only for passive review of an already-supplied, sanitized evidence
package. It is not discovery, validation, exploitation, or authorization.

## When to Use

- Reviewing defensive directory control, baseline, monitoring, or exception evidence.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Boundary

Never query, contact, authenticate to, or enumerate a live directory or service.
Never provide commands, scripts, LDAP or API syntax, tool instructions, object
changes, persistence creation, attack paths, edges, ranking, or exploitation.

Reject distinguished names, security or object identifiers, user or service
principal values, object paths, names, hosts, domains, addresses, URLs,
credentials, tickets, certificates, secrets, raw access-control material, and
configuration bodies. Accept only opaque IDs and digests. Diagnostics stay
generic and never quote rejected content.

## Workflow

1. Accept only supplied-passive, sanitized evidence and opaque references.
2. Record the engagement cutoff, closed policy, snapshot receipt, and opaque
   scope and directory references.
3. Inventory only supplied abstract subjects. Do not discover or name objects.
4. Create one coverage cell for every subject and each required persistence-
   control family.
5. Keep control relationship, baseline, durability, protection, monitoring,
   freshness, and result as independent tracks.
6. Bind every evidence item to the exact subject, snapshot and digest, scope,
   directory, policy and digest, control and fingerprint, and upstream receipts.
7. Require supplied-passive mode, sanitization, eligibility, strict evidence
   window, cutoff compliance, and one retained custody receipt.
8. Keep policy, relationship, baseline, durability, protection, monitoring
   configuration, monitoring health, result, and upstream receipt roles separate.
9. Treat a nominal relationship as neither effective protection nor healthy
   monitoring. Policy assignment is neither application nor enforcement.
10. Accept imported Kerberos or certificate-service conclusions only through
    exact opaque receipts bound to the same snapshot and cell.
11. Use `not-applicable` only with a closed reason and exact current policy
    evidence. Keep that cell in the coverage denominator.
12. Create one immutable open finding for each exact current
    `observed-exposure`. This ledger cannot close findings.
13. Derive handoff state from exact finding, evidence, owner, and chronology.
    Handoffs transfer defensive work and grant no authority.
14. Resolve structural safety failures and semantic contradictions before
    relying on coverage or summaries.

## Interpretation rules

- `complete-no-observed-exposure` means every applicable cell is current and no
  exposure was observed. Policy-backed NA cells do not create unknowns.
- `complete-with-exposure` means at least one current observed exposure has an
  immutable open finding.
- `material-unknowns` means a material track is unknown or indeterminate.
- `stale` means historical evidence cannot support current claims.
- `incomplete` means the exact coverage matrix is incomplete.

## Report

Return the aggregate, track counts, open finding IDs, defensive handoffs, and
generic conflict codes. Never reconstruct real directory values or operational
steps from opaque evidence.

## Rationalizations to reject

- **“A read-only directory query is passive.”** It still contacts a live system
  and is outside this skill.
- **“The object name helps the reviewer.”** Real names and paths create exposure;
  preserve only opaque references.
- **“Membership proves durable control.”** A relationship is not proof of
  durability, protection, or effective application.
- **“Policy assignment proves enforcement.”** Require separate exact evidence.
- **“Monitoring is configured, so absence is meaningful.”** Configuration is not
  health or detection evidence.
- **“The upstream audit already passed.”** Imported claims require the exact
  current opaque receipt and matching bindings.
- **“The label did not change.”** Snapshot, policy, control, or receipt drift
  invalidates historical claims.
- **“We can close the finding here.”** Findings stay open in this ledger.
- **“The handoff approves remediation.”** Handoffs transfer defensive work only.
