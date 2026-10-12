---
name: rootkit-triage
description: "Triages suspected rootkits, bootkits, hidden processes, kernel hooks, driver or module anomalies, concealed network activity, eBPF implants, and boot-integrity failures. Use when host tools may be lying and the incident needs evidence-preserving cross-view analysis, containment, or forensic handoff."
allowed-tools: Read Grep Glob
---

# Rootkit triage

A suspected rootkit changes the reliability of the instrument used to inspect
it. Treat live host output as one view, preserve provenance, and seek evidence
from a different or lower trust layer before strengthening the claim.

This skill decides whether rootkit suspicion is unsupported, suspected,
corroborated, or confirmed; what to preserve; and what containment or specialist
handoff is justified. It does not perform full memory reconstruction, develop or
deploy a rootkit, or prescribe live deletion from a system whose kernel or boot
chain may be compromised.

## When to Use

- Host tools may be lying and the incident needs evidence-preserving cross-view analysis, containment, or forensic handoff.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record the asset, platform, authorization, business context, current
   isolation state, and suspected layers: userland, kernel, eBPF or driver,
   boot, hypervisor, or firmware.
2. Inventory supplied evidence with its source, locator, acquisition time or
   bounded window, vantage, role, and integrity hash where the evidence record requires
   one. Do not invent acquisition precision.
3. Assign trust from vantage rather than tool reputation. Live OS output is low
   trust for rootkit absence; external network observations and offline disk are
   medium; offline memory, hardware attestation, and external firmware reads are
   high.
4. Compare independent views of processes, files, network activity, modules or
   drivers, hooks, eBPF state, boot measurements, firmware, and timing. Two tools
   that depend on the same live kernel do not form an independent cross-view.
5. Build hypotheses from evidence and comparisons. A discrepancy supports
   suspicion. Corroboration needs independent vantage groups. Confirmation needs
   a high-trust direct artifact, an independent supporting vantage, and a
   discrepancy tied to the claim.
6. Cover case context, preservation, process, file, network, module or driver,
   control-flow hook, eBPF, boot, firmware or hypervisor, memory, and containment
   questions. Keep unavailable layers blocked rather than clean.
7. Plan preservation before reboot, artifact removal, rebuild, or firmware
   changes. Record authorization and evidence impact on every action. A review
   pass is not permission to execute it.
8. Choose containment from the evidence strength and business impact. Preserve
   volatile evidence when feasible, isolate confirmed or corroborated cases,
   and use trusted-media rebuild or hardware escalation when the affected trust
   layer makes live cleanup unreliable.
9. Hand detailed memory reconstruction to a memory-forensics workflow. Hand
   firmware acquisition to a hardware or firmware workflow. Keep the triage
   record as the chain between the initial discrepancy and those analyses.

## Interpretation rules

- Agreement among live tools is weak evidence because they may share the same
  compromised API, kernel structure, or hook.
- A cross-view discrepancy is an indicator. Benign races, collection timing,
  permissions, parsing, and normal updates remain alternative explanations.
- A matching boot measurement is evidence about measured components and the
  referenced baseline. It does not clear unmeasured firmware or runtime state.
- A memory image acquired through the suspected kernel can still be manipulated.
  Record the acquisition vantage and preserve that limitation.
- A valid signature establishes signer and file integrity, not benign behavior.
- If kernel, boot, hypervisor, or firmware compromise is confirmed, restoration
  from trusted media and re-attestation are usually more defensible than live
  artifact deletion.

## Rationalizations to reject

- **"Every live tool agrees, so the host is clean."** Shared dependence on the
  same compromised layer can make agreement systematic deception.
- **"A discrepancy proves a rootkit."** Collection races, permissions, parsing,
  and legitimate changes must remain visible until independent evidence resolves them.
- **"The scanner named a rootkit family."** Signature output is a lead until its
  matched artifact and provenance are preserved and examined.
- **"Reboot first and see if it goes away."** Reboot destroys volatile evidence
  and can activate boot persistence or recovery behavior.
- **"We found the file, so delete it now."** Live removal can destroy evidence,
  trigger defensive behavior, or leave the lower trust layer compromised.
- **"Secure Boot passed, so firmware is fine."** Attestation covers the measured
  chain and baseline; it does not establish every firmware component is benign.
