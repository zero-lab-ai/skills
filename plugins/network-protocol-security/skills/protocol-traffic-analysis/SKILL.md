---
name: protocol-traffic-analysis
description: "Analyzes supplied PCAP and packet-capture evidence into hosts, conversations, dependencies, authentication exposure, timing patterns, blind spots, and defensible follow-up. Use when reviewing network traffic without transmitting to the observed systems."
allowed-tools: Read Grep Glob
---

# Protocol traffic analysis

A packet capture contains what reached one collection point during one time
window under one filter. It does not contain every host, service, packet, or
direction in the environment. Preserve that boundary while turning packets into
an evidence-backed map.

This skill analyzes supplied captures. It does not authorize capture placement,
active probing, credential cracking, replay, poisoning, exploitation, or target
contact. Send active discovery to a reconnaissance workflow and active protocol
validation to a separately authorized assessment.

## When to Use

- Reviewing network traffic without transmitting to the observed systems.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Hash each capture and record its source, authorization, collection point,
   time window, packet and byte counts, filter, snap length, directionality,
   clock basis, and reported packet drops.
2. State handling rules before reading payloads. Keep credentials, tokens,
   personal data, and session material in restricted evidence storage. Put only
   redacted references in the analysis record.
3. Build evidence locators from frame numbers, streams, fields, or deterministic
   aggregates. A narrative without a locator is not packet evidence.
4. Inventory hosts from observed addresses and names. Record role and operating
   system as `observed`, `inferred`, or `unknown`, with evidence for each claim.
5. Build directional conversations with endpoints, transport, time range,
   counts, service claim, authentication exposure, encryption state, and evidence.
   If the supplied facts do not include per-conversation counts or timestamps,
   mark those metrics unknown; never substitute `1` or the full capture window.
6. Separate protocol identity from port convention. Mark a service `observed`
   only when dissection, payload, negotiation, or equivalent evidence supports it.
7. Record dependencies, timing patterns, naming and broadcast intelligence,
   authentication exposure, and anomalies. Include alternative explanations for
   every inferred pattern.
8. Cover capture integrity, host inventory, service dependencies,
   authentication, naming and broadcast, encrypted traffic, timing, blind spots,
   and data handling. Blocked or absent coverage remains visible.

## Interpretation rules

- No observed packet is not evidence that a host, service, or protocol is absent.
- A filtered capture cannot answer questions about traffic excluded before storage.
- Packet drops, truncation, one-sided capture, and clock uncertainty weaken timing
  and completeness claims; they do not disappear because analysis succeeded.
- TTL, window size, user agent, naming, and protocol mix support hypotheses about
  host role or operating system. Preserve them as inferred unless direct evidence exists.
- Encrypted traffic exposes metadata and behavior, not plaintext content.
- Regular timing can indicate automation, monitoring, backup, or command and
  control. State the alternatives before recommending active follow-up.
- A captured challenge-response proves exposure in the capture. It does not prove
  that the credential is crackable, relayable, privileged, or still valid.

## Rationalizations to reject

- **"The capture is clean."** A capture has coverage and limitations; it is not a
  verdict on traffic it could not see.
- **"Port 443 means HTTPS."** Port convention is an inference until protocol
  evidence supports it.
- **"The periodic flow is command and control."** Regular services and health
  checks produce the same shape. Preserve alternatives.
- **"We can paste the credential into the report for proof."** Store the secret
  under access control and cite a redacted reference.
- **"Zero dropped packets means complete visibility."** It says nothing about
  the capture point, filter, direction, or traffic outside the time window.
- **"The PCAP showed a relay target, so relay is authorized."** Observation does
  not grant permission to crack, replay, poison, relay, or contact anything.
