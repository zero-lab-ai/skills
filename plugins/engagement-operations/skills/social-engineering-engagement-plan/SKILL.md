---
name: social-engineering-engagement-plan
description: "Plans authorized defensive phishing simulations, vishing exercises, and other social-engineering engagements with explicit channel and cohort scope, pretext approval, participant safety, data minimization, readiness gates, metrics, and debrief. Use before measuring human-security exposure or reviewing a proposed campaign."
allowed-tools: Read Grep Glob
---

# Social-engineering engagement plan

Defensive human-security testing measures organizational exposure and validates controls,
but it can cause harm even when every technical action is reversible.
Sponsor authority permits a bounded exercise; it does not prove the target list,
pretext, infrastructure, control cell, support route, or data handling are ready.

This skill creates a checked plan. It does not write deceptive content, call scripts,
payloads, collection pages, target profiles, or execution instructions.

## When to Use

- Plan authorized human-security exercises safely.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record the sponsor, window, timezone, owners, digest-bound written-authority
   evidence, its approving role and validity window, allowed and prohibited channels,
   asks, persona classes, themes, and actions. The v0.1 contract supports email and
   voice only; keep every other channel prohibited.
2. Define each target cohort by opaque ID, channel, supplied population, opaque
   inclusion and exclusion references, list state, and evidence. Never store
   addresses, numbers, names, or descriptive dossiers.
3. Describe pretexts by ID, persona class, channel, approved ask, state, evidence,
   and limitations. Store no message copy or scripts.
4. Inventory the target list, sending domain, training page, callback number, control
   cell, and support route as applicable. Planned infrastructure is not verified.
5. Define interaction stops for distress, participant request, reporting, active
   incidents, and out-of-scope people or data. Define campaign pauses for cumulative
   distress, client incidents, scope-risking defects, and loss of the control cell.
   Record whether a pause fired and bind a threshold-triggered pause to evidence.
6. Minimize data before execution. Allow only named event types; use opaque identities,
   aggregate reporting, no individual ranking, no public identification, and an owner
   for retention or disposition. Before readiness, choose no retention or a bounded
   retention period and name the disposition method. An unapproved event is not a
   useful extra metric.
7. Link each planned action to one authorization, cohort, approved pretext, safety
   policy, data policy, and every required infrastructure item. Keep it `planned`
   until all readiness evidence exists.
8. For executed actions, cite chronologically valid event-export or operator-log
   evidence and record bounded aggregate counts. Keep unexecuted and unapproved event
   fields null: zero is an observed measurement, not absence of collection. Never
   infer opens, delivery, reports, distress, or control adherence.
9. Cover authorization, cohort, pretext, infrastructure, safety, data handling,
   deconfliction, debrief, measurement, and reporting for every allowed channel.
10. Record immediate and organization-wide debrief ownership, participant support,
    feedback timing, and no-shaming rules.

## Boundary with adjacent skills

- Use `osint-scanner` or `social-engineering-recon` to collect public intelligence.
- Use `opsec-planning` to compare detection risk and operational artifacts.
- Use this skill to govern authorized interaction with people and participant care.
- Use `findings-report` after evidenced results exist.
- Credential collection, payload delivery, physical-entry methods, and target-system
  access require separate capabilities and explicit authority.

## Rationalizations to reject

- **"The sponsor approved phishing, so the campaign is ready."** Approval does not
  verify the target list, pretext, infrastructure, control cell, or support route.
- **"Open rate is standard."** If open tracking was not approved, it is prohibited
  data collection rather than a free metric.
- **"A click means the participant was compromised."** It proves only the approved
  event that was observed; credentials, execution, and access remain separate.
- **"We can exclude people manually during launch."** Exclusions belong in the
  checked target manifest before contact.
- **"Stopping one call handles distress."** Individual stops and campaign-wide pause
  thresholds solve different safety problems; both are required.
- **"Zero means we did not collect it."** Zero is a measured result. Prohibited or
  uncollected events stay null so the record cannot disguise unauthorized telemetry.
- **"Recording helps evidence."** Recording requires explicit authorization and legal
  review. A useful artifact does not create permission.
- **"Individual rankings make training actionable."** They increase harm and suppress
  reporting. Report cohort and process controls unless individual handling is approved.
- **"A successful test should stay secret until the report."** Timely debrief and a
  private support route are part of the engagement, not optional cleanup.
