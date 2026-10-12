---
name: persistence-surface-assessment
description: "Measures local Windows and Linux endpoint persistence exposure from supplied evidence by deriving consumer, authority, lifecycle, prevention, context, telemetry, and coverage state. Use when auditing durable-execution risk without creating, activating, testing, ranking, or removing a persistence mechanism."
allowed-tools: Read Grep Glob
---

# Persistence surface assessment

Persistence exposure is not proof that persistence exists, executed, survived, was approved, or
is malicious. Measure whether current supplied evidence closes the prerequisites for durable local
execution while keeping every assessed surface opaque.

This skill is read-only and local-endpoint only. It does not enumerate a live host, reveal concrete
locations, create or rank mechanisms, execute triggers, change configuration, test survival, clean
artifacts, evade telemetry, inspect directory or cloud control planes, handle credentials, or assess
kernel, bootkit, firmware, or hidden-object integrity.

## When to Use

- Auditing durable-execution risk without creating, activating, testing, ranking, or removing a persistence mechanism.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record exact written authority, scoped Windows or Linux assets, the supplied-evidence boundary,
   assessment time, collection windows, and prohibited active actions.
2. Normalize evidence with one asset, source group, opaque locator, digest status, observed time or
   bounded window, validity, provenance, limitations, and custody. Do not invent precision, names,
   ownership, hashes, or independence.
3. Cover every required platform surface. Each asset-category cell is `assessed`, `blocked`, or
   `not-applicable`; one empty surface never proves asset-wide absence.
4. Represent each existing consumer only by an opaque surface reference and closed category. Keep
   consumer availability, effective change authority, lifecycle survival, preventive control,
   execution-context relation, and telemetry state as separate evidence-backed facts.
5. Require current same-asset evidence for every non-unknown fact. Evidence from one source group
   remains one vantage even when several parsers report it. Stale, unavailable, or disposed material
   cannot prove current exposure.
6. Keep execution separate from exposure. Execution needs an exact configuration-to-artifact-to-
   event binding in a compatible window; an existing registration is not compromise or success.
7. Mark higher-context exposure for a privilege-escalation handoff without claiming elevation. If
   host-view integrity is suspect, derive `inconclusive` and require rootkit triage.
8. Create only closed defensive remediation objectives and owned specialist handoffs. Rank fix
   urgency, never mechanism usefulness. A fix is complete only from post-change evidence.
9. Derive all surface states, coverage, priorities, and summaries. Preserve blocked, unknown,
    conditional, conflicting, and not-applicable work rather than converting silence to clean.

## Boundary with adjacent skills

- `privilege-escalation-assessment` owns vertical transitions and achieved identity.
- `rootkit-triage` owns hidden artifacts, compromised inspection layers, and boot or kernel integrity.
- `credential-exposure-audit` owns secret material, validity, privilege, and handling.
- `memory-forensics-triage` owns supplied volatile images; memory representation is not durability.
- `directory-persistence-audit` owns directory-wide identities, policy, delegation, and control paths.
- Cloud attack-path workflows own IAM, workload identity, provider schedulers, and control planes.
- Detection workflows own detector creation and authorized technique-to-alert validation.
- `findings-report` owns final claim-bearing stakeholder prose.

## Rationalizations to reject

- **"It is writable, so persistence is confirmed."** Consumer, survival, and prevention still bind.
- **"The ticket or signature makes it approved."** Neither binds the current exact configuration.
- **"The scheduler returned success."** A result code does not prove the intended artifact executed.
- **"The process name matches."** Names do not bind configuration, artifact, event, or context.
- **"One empty location means the host is clean."** Preserve the full platform denominator.
- **"Read authority permits a harmless test."** Triggers, restarts, logons, reboots, and edits are active.
- **"Show the exact location so remediation is easier."** Keep this artifact opaque and hand off safely.
- **"Rank the most reliable option."** Rank remediation urgency, never persistence utility.
- **"Disposed evidence still proves the state."** Preserve its disposition receipt, not a current claim.
- **"Unknown means low risk."** Unknown prerequisites yield conditional or inconclusive exposure.
