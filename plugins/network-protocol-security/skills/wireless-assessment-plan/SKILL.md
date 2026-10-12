---
name: wireless-assessment-plan
description: "Plans authorized Wi-Fi, Bluetooth, RFID/NFC, SDR, and other radio assessments with explicit physical scope, transmission authority, disruption budgets, capture handling, coverage, and handoffs. Use before conducting or reviewing a wireless penetration test."
allowed-tools: Read Grep Glob
---

# Wireless assessment plan

Radio signals cross walls, property lines, and engagement boundaries. Receiving
a signal can be passive while retaining its content, targeting its source, or
transmitting a response creates separate scope, privacy, safety, and regulatory
questions. Model those decisions before activating test equipment.

## When to Use

- Plan wireless assessment for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. State the objective, written authorization references, approved locations,
   technologies, actions, transmission bands, disruption budget, and data rules.
   Bind every location to the authorization that names it; do not invent a
   survey, staging, or observation area to make existing evidence fit.
2. Inventory exact radio targets. Separate in-scope systems from excluded and
   unattributed signals. An observed identifier is not proof of ownership.
3. Inventory equipment by receive, transmit, emulate, and write capability.
   Keep transmit-capable equipment disabled until the plan authorizes its use.
4. Start with passive observation. Bind identifiers, channel or frequency,
   location, time, and signal evidence before proposing active work.
5. Record every proposed action against one in-scope target, one location, one
   device, one authorization reference, a stop condition, and recovery steps.
6. Treat protocol reads, association, active enumeration, authentication,
   credential testing, impersonation, protocol writes, disruption, emulation,
   and replay as RF emission. Verify written transmission authority and the
   approved band.
7. Give disruptive work an explicit duration and affected-device ceiling.
   Availability impact includes nearby clients and safety systems, not only the
   named access point or reader.
8. Cover each declared technology across scope, passive inventory, attribution,
   trust, confidentiality, integration, client behavior, availability,
   monitoring, and data safety as applicable. Preserve blocked and delegated work.
9. Register captures containing credentials, personal data, or bystander traffic
   and assign a restricted, redacted, destroyed, or other approved disposition.
10. Delegate wired segmentation, identity infrastructure, companion apps,
    backend services, and physical-access consequences with an owner and status.

## Interpretation rules

- A visible SSID, device address, tag identifier, or signal is an observation,
  not attribution or authorization.
- A capture proves only what its location, time, receiver, and recorded band
  support. Signal strength alone does not prove physical location.
- A handshake or challenge capture does not prove a weak credential. An offline
  credential test and its result are separate evidence.
- Failure to disrupt does not prove protected management or resilient service;
  range, channel, equipment, client state, and rate can explain the result.
- A successful association does not prove segmentation failure. The downstream
  path needs its own authorized evidence or handoff.
- Receive-only authority does not permit active protocol reads, replay,
  emulation, jamming, cloning, enumeration, or writes.

## Rationalizations to reject

- **"The signal reaches us, so it is in scope."** Propagation does not establish
  ownership, attribution, or authority.
- **"It is an unlicensed band, so transmission is allowed."** Band rules,
  power limits, engagement authority, interference, and local law still apply.
- **"One short deauthentication or jam will not hurt anything."** Disruption
  needs an explicit budget and can affect bystanders or safety-relevant systems.
- **"We only captured traffic; we did not attack it."** Captures can contain
  credentials, personal data, and unrelated communications that require handling.
- **"The SSID and company name match, so this is their access point."** Names
  are forgeable. Preserve attribution as unresolved until evidence supports it.
- **"a complete record means we can transmit."** It validates the document.
  Written authorization and the operator still govern execution.
