---
name: firmware-hardware-assessment
description: "Tracks embedded-device and firmware assessment coverage across exact units, acquisition methods, debug interfaces, stored secrets, update trust, radios, physical safety, and delegated external systems. Use when planning, conducting, reviewing, or handing over an authorized hardware or IoT penetration test."
allowed-tools: Read Grep Glob
---

# Firmware and hardware assessment

A visible debug pad is not usable debug access. Matching flash reads prove a
repeatable acquisition, not authentic firmware. A signature block or downgrade
string does not prove enforcement. Keep each conclusion tied to the exact unit,
artifact, action, and evidence.

## When to Use

- Planning, conducting, reviewing, or handing over an authorized hardware or IoT penetration test.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record model, serial, hardware revision, reported firmware, and whether each
   device is sacrificial and authorized for damage.
2. State allowed action classes, in-scope external systems, and constraints.
   Treat voltage, power state, fixtures, and irreplaceable calibration as safety
   boundaries, not informal notes.
3. Bind photographs, measurements, logs, captures, and analysis to a device.
   Keep secret values out of summaries and report attachments.
4. Record each acquired artifact with its SHA-256, source, acquisition, and
   evidence. Preserve repeated reads as separate artifacts.
5. Derive acquisition consistency from artifact hashes. Matching reads establish
   repeatability only from the first recorded read onward.
6. Compare vendor and installed images by partitions and normalized content.
   Record per-device configuration and calibration before interpreting unequal
   whole-image hashes.
7. Inventory one `device` surface per unit, then components, debug interfaces,
   storage, firmware images, update mechanisms, local and network services,
   radios, and external systems.
8. Cover device identity, acquisition integrity, debug access, firmware
   analysis, credential material, update trust, communications, integration,
   supply chain, and physical safety. Preserve planned, blocked, delegated, and
   inconclusive work.
9. Use `finding` only for an executed, evidenced case. Limit claim scope to the
   tested unit unless evidence from additional devices supports a broader claim.
10. Delegate companion applications, vendor cloud, brokers, update services,
    and production systems. Discovery does not authorize contact.

## Interpretation rules

- A password prompt is a positive control for that interface, not proof of
  password strength or restricted post-authentication privilege.
- A locked root account says nothing about other support identities.
- A recovered private key proves extractability from that artifact. Fleet-wide
  reuse needs evidence from more than one unit.
- An apparent signature block is an indicator until verification code, trust
  anchor, signed regions, and failure behavior are established.
- An update error string does not prove rollback prevention.
- Interface pads prove physical presence. Pinout, lifecycle state, fuses,
  authentication, and effective access remain separate questions.
- Firmware version labels do not prove byte equivalence.

## Rationalizations to reject

- **"The hashes differ, so the installed firmware was tampered with."** Device
  configuration, calibration, logs, and writable state can explain the delta.
- **"Two reads match, so the firmware is authentic."** They prove acquisition
  repeatability, not origin or trust.
- **"JTAG pads exist, so JTAG is enabled."** Usability depends on pinout,
  electrical state, lifecycle controls, and authorization to interrogate it.
- **"The package is signed, so updates are secure."** Enforcement and coverage
  of every security-sensitive field still need evidence.
- **"The credential is in one unit, so the whole fleet shares it."** A
  single-device observation cannot establish provisioning behavior.
- **"A sacrificial fixture makes destructive work authorized."** Written action
  scope and explicit damage authorization are both required.
