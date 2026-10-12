---
name: covert-channel-assessment
description: "Assesses covert-channel and data-egress exposure, then plans or records bounded purple-team validation with synthetic data. Use when evaluating DNS, web, cloud, ICMP, tunnel, timing, steganographic, or dead-drop paths without turning a plausible route into a claim of successful exfiltration."
allowed-tools: Read Grep Glob
---

# Covert channel assessment

A permitted protocol is not a working covert channel. A working channel is not
automatically undetected. Keep route feasibility, execution proof, detection
outcome, and data custody as separate claims.

This skill assesses supplied evidence and bounded synthetic tests. It does not
provide payloads, encodings, tunneling commands, evasion settings, C2 design,
pivoting, persistence, credential use, third-party abuse, or authority to move
real data.

## When to Use

- Evaluating DNS, web, cloud, ICMP, tunnel, timing, steganographic, or dead-drop paths without turning a plausible route into a claim of successful exfiltration.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record the written authorization, exact sources, assessment window, approved
   receivers, synthetic marker hash, byte and duration ceilings, prohibited data,
   services, and actions. Receiver ownership and authorization are different facts.
2. Inventory evidence with source, locator, honest time precision, and integrity
   hash for copied artifacts. Use null time fields when the source supplies no
   observation time; the assessment window is not evidence time. Preserve unknowns;
   do not invent throughput, queries, alerts, endpoints, accounts, transfer times,
   or successful delivery.
3. For every source, assess all eight approved channel families. Keep a
   family unknown or blocked when evidence is absent or testing is prohibited.
4. Treat `plausible` as a route hypothesis. Use `validated` only after an authorized
   test records the approved marker, receiver, exact bounded times, observed bytes,
   source evidence, and receiver-side delivery evidence.
5. Describe capacity as `unknown`, `estimated`, or `measured`. Only an executed test
   can produce measured throughput. Baselines describe normal traffic, not covert
   channel capacity.
6. Inventory telemetry by source, health, retained fields, window, and limitation.
   Packet counts do not prove payload inspection; process telemetry does not prove
   delivery; a detection rule does not prove an alert fired.
7. Predeclare a detection check for every planned or executed test. `not-detected`
   requires healthy telemetry queried across the entire test window. An absent alert
   without that evidence is `inconclusive`.
8. Enforce byte and duration ceilings per test and in aggregate per source. Keep
   blocked or prohibited paths visible; do not force a transfer to complete coverage.
9. Track marker creation, source staging, receiver storage, retention, and destruction
   for every planned or executed test. A synthetic marker still has a custody trail.
10. Link medium-or-higher channels to an owned response: validate safely, improve
    telemetry, tighten egress, or accept the documented risk.

## Interpretation rules

- An allowed port proves a route control state, not delivery, throughput, or stealth.
- Encryption protects content. It can increase entropy and does not erase volume,
  timing, destination, process, or policy observables.
- A normal-volume test can validate content or rule coverage. It cannot prove that a
  larger transfer would blend into the baseline.
- A blocked path can be a successful control result without becoming a validated
  channel.
- Receiver logs prove delivery only for the receiver, marker, source, and window they
  identify. They do not prove endpoint cleanup.
- Detection requires an alert or documented analytic result. Visibility means the
  telemetry existed; the two are not interchangeable.
- A `not-detected` result is a real gap only when the expected telemetry was healthy
  and fully queried. Otherwise the result is inconclusive.

## Boundary with adjacent skills

- Use `protocol-traffic-analysis` to interpret supplied captures without transmitting.
- Use `detection-validate` for the broader ATT&CK technique coverage map.
- Use `detection-engineering` to build or tune the detector itself.
- Command-and-control architecture design is outside this collection; this skill
  owns bounded channel exposure and detection validation only.
- Use `opsec-planning` for a red-team operation's full artifact and detection-risk plan.
- Use `findings-report` for final finding prose.

## Rationalizations to reject

- **"Port 443 is open, so HTTPS exfiltration works."** A route still depends on the
  proxy, allowlist, receiver, authentication, content controls, and actual delivery.
- **"No alert fired, so the channel is covert."** Without healthy telemetry and a
  complete query, silence is an unknown observation.
- **"The file is synthetic, so the transfer limits do not matter."** The exercise can
  still disrupt systems, trigger incidents, or teach the wrong control conclusion.
- **"Encryption makes the transfer invisible."** Metadata, volume, timing, process,
  destination, and policy observables remain.
- **"We should try every channel to prove coverage."** Blocked and prohibited paths
  are honest results; execution must stay inside the rules of engagement.
- **"A receiver log proves cleanup."** Delivery, source deletion, receiver deletion,
  and retention are separate evidence.
- **"A complete record authorizes the test."** It validates the record. Written authority
  and the operator govern execution.
