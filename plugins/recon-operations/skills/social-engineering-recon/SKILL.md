---
name: social-engineering-recon
description: "Maps human-layer exposure from client-supplied and passive public evidence at cohort, role, process, channel, and relationship level. Use when preparing or defending an authorized social-engineering assessment without contacting people, building personal dossiers, ranking targets, or generating pretexts."
allowed-tools: Read Grep Glob
---

# Social-engineering recon

Public information can expose organizational roles, processes, channels, relationships,
and control assumptions. Defensive assessment measures those patterns without turning
people into targets.

This skill analyzes already supplied evidence. It does not discover sources, contact a
target, build personal profiles, rank people, or generate personas, pretexts, messages,
lures, payloads, or execution instructions.

## When to Use

- Preparing or defending an authorized social-engineering assessment without contacting people, building personal dossiers, ranking targets, or generating pretexts.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record digest-addressed written-authority evidence, its approving opaque role and
   validity window, an exact assessment time, `passive-only` mode, opaque identity
   handling, permitted source classes, bounded retention, and limitations.
2. Import digest-addressed acquisition receipts from `osint-scanner` or the supplying
   system. Preserve source class, opaque origin and its evidence, contact classification,
   retrieval time, validity evidence, disposition, and opaque source reference. Do not
   recreate a tool or query catalogue here.
3. Exclude out-of-scope, sensitive, unverifiable, and expired material explicitly.
   Public availability does not erase privacy or scope.
4. Represent only opaque organizational cohorts, roles, processes, channels, and
   relationships. Never store names, addresses, handles, personal profiles, routines,
   protected traits, health data, or susceptibility scores.
5. Record one direct fact per observation. Bind it to one source, one opaque claim, one
   or more organizational units, a controlled fact class, and a support or contradiction
   stance. Bind counterevidence directly to the supporting observation it counters. Store
   no free-form narrative.
6. Build assessments from observation IDs. Two result pages copied from one publication
   share one `origin_id`; repetition is not independent corroboration. Unknown or expired
   validity cannot establish current support. Accepted counterevidence forces `disputed`.
7. Keep conclusions organizational. `supported`, `limited`, `disputed`, and
   `not-supported` describe evidence strength, not exploitability, susceptibility,
   compromise, campaign readiness, or permission to contact anyone.
8. Create only defensive handoffs: control review, remediation, engagement planning, or
   a separate capability. Pass opaque assessment references, not target lists or tactics.
9. Cover authority, provenance, privacy, role, process, relationship, channel, timing,
   control assumptions, freshness and contradiction, and defensive handoff for every
   scope unit. Proof must match the coverage class.

## Boundary with adjacent skills

- Use `osint-scanner` to plan acquisition and classify whether a tool or mode contacts
  the target. This skill consumes its receipt and analyzes supplied evidence.
- Use `social-engineering-engagement-plan` for cohorts, approved pretexts, participant
  safety, infrastructure readiness, measurement, and debrief before any interaction.
- Use `opsec-planning` for action-level artifacts, detection risk, and abort decisions.
- Use `findings-report` only after a demonstrated issue is ready for formal reporting.

## Rationalizations to reject

- **"It is public, so it is fair game."** Public availability does not remove scope,
  privacy, retention, or harm constraints.
- **"Names make the assessment actionable."** Organizational controls can be assessed
  with opaque roles and cohorts; names turn analysis into dossiering.
- **"It is only recon."** Collection and synthesis can harm people before contact.
- **"Two search results corroborate it."** Copies of one origin are one origin.
- **"The old page is probably current."** Unknown freshness limits the claim.
- **"No control was visible, so none exists."** Missing evidence is not absence.
- **"Sponsor approval lets us verify live."** Passive authority forbids target contact.
- **"Ranking likely targets is defensive prioritization."** Prioritize controls and
  processes, never people.
- **"A sample pretext explains the risk."** It crosses into deceptive-content creation.
- **"A complete record means launch."** It validates the recon record only; the engagement
  planner still governs interaction.
