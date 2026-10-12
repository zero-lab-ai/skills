---
name: physical-recon
description: "Assesses supplied daylight physical-security observations from authorized public vantage points at opaque site and control level. Use when reviewing physical reconnaissance without entering property, tracking people, collecting identifiers, planning approaches, or generating intrusion methods."
allowed-tools: Read Grep Glob
---

# Physical recon

Physical reconnaissance can reveal visible control surfaces and documentation gaps. A
defensive assessment records bounded observations without converting them into routes,
schedules, identities, or intrusion instructions.

This skill analyzes supplied observation records. It does not direct collection, enter
property, follow or contact people, photograph private areas, identify people or vehicles,
collect discarded material, operate drones, transmit RF, rank sites or shifts, select
approach routes, or design entry, badge-cloning, bypass, concealment, or evasion methods.

## When to Use

- Reviewing physical reconnaissance without entering property, tracking people, collecting identifiers, planning approaches, or generating intrusion methods.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record digest-addressed written authority, approving opaque role, valid assessment and
   observation windows, `public-right-of-way-only` mode, daylight-only observation, opaque
   identities, bounded retention, and every prohibited method.
2. Inventory opaque sites and public-right-of-way observation points. Bind each point and
   permitted method to an approved authorization; store no address, coordinate, map, route,
   tenant, person, vehicle, or schedule.
3. Import supplied evidence with a unique artifact reference, original-origin evidence,
   class, time, site and point binding, privacy state, disposition, and limitations.
4. Record each field session with its exact authorized site, point, window, daylight visual
   method, safety receipt, required stop conditions, and explicit false values for target
   contact, property entry, and material collection.
5. Separate client policy requirements from direct observation. Policy evidence can define
   expected control design but cannot prove a visible condition; imported OSINT cannot prove
   one either.
6. Exclude material with unknown site, time, vantage, custody, scope, or privacy status.
   Public visibility does not repair missing provenance.
7. Record controlled observations as `visible`, `not-observed`, or `indeterminate`. Never
   use absence: non-observation is not proof that a control does not exist.
8. Derive each site/control assessment from all current policy requirements and direct
   observations: `consistent`, `potential-variance`, `inconclusive`, or `not-assessed`.
   Potential variance is a review trigger, not a confirmed vulnerability.
9. Keep one custody record for every artifact-bearing evidence item. Bound retention to the
   engagement ceiling; require chronological receipts for redaction or destruction.
10. Create defensive handoffs for internal control review, remediation, or a separately
   authorized assessment. Carry opaque assessment IDs, never routes, targets, or methods.
11. Cover authority, public boundary, provenance, policy baseline, time, privacy, custody,
   safety, seven physical-control classes, and defensive handoff for every site. Proof must
   match its class.

## Boundary with adjacent skills

- Use `osint-scanner` to classify remote third-party acquisition and target contact.
- Use `social-engineering-recon` for human-layer roles, processes, channels, and
  relationships; this skill stores no person or behavioral profile.
- Use `wireless-assessment-plan` for RF receiving or transmission; both are prohibited here.
- Use `social-engineering-engagement-plan` before any interaction with staff.
- Physical entry, tailgating, cloning, bypass, covert routes, and on-site validation require
  a separate capability and explicit method-level authority; this skill never supplies them.

## Rationalizations to reject

- **"It is visible from public space, so anything is fair game."** Privacy, scope, time,
  custody, retention, and harm constraints still apply.
- **"One open door proves a recurring gap."** A transient observation proves only itself.
- **"Two observers used the map, so it is corroborated."** Copies of one origin are one.
- **"A photo is evidence even without metadata."** Unknown site, time, vantage, or custody
  prevents a defensible physical conclusion.
- **"Shift ranking is just prioritization."** It turns control assessment into person and
  schedule targeting.
- **"A route explains the finding."** Approach and evasion guidance is operational planning.
- **"Passive includes drones or receive-only RF."** This contract permits neither; use a
  separately authorized capability.
- **"The sponsor asked for badge cloning."** Sponsor pressure does not expand recorded scope.
- **"No visible control means no control exists."** Missing public evidence is not absence.
- **"a complete record authorizes a field action."** It validates a supplied record only.
