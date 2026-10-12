---
name: memory-forensics-triage
description: "Triages supplied Windows, Linux, or other volatile-memory images while preserving acquisition provenance, image integrity, process and region evidence, network and object correlations, extracted-artifact custody, timeline limits, and claim confidence. Use for offline memory-forensics review and handoff, not live rootkit trust assessment or full malware reverse engineering."
allowed-tools: Read Grep Glob
---

# Memory forensics triage

Memory is a captured vantage, not an infallible narrator. Acquisition changes the
system; the acquisition path can be subverted; symbols can be wrong; one image can
produce many correlated outputs without becoming multiple independent sources.

This skill analyzes supplied image facts and normalized outputs. It does not
acquire memory, provide live collection commands, recover credential material,
execute extracted code, query reputation services, or authorize containment.

## When to Use

- Triage memory forensics for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record written authorization, case and asset identity, platform, image name,
   size, format, acquisition method and window, tool identity, hash, transfer,
   custodian, storage, access-log state, acquisition impact, and clock basis.
2. Record the analysis engine, version, reported platform or build, selected
   symbols or profile, match state, validation evidence, and limitations. A
   successful plugin run does not prove the profile is correct.
3. Inventory each supplied observation with its image, source group, artifact
   class, locator, role, honest time precision, and limitations. Different
   plugins over one image share one source group.
4. Correlate process inventory and lineage, executable regions, modules or
   mappings, network objects, handles, registry objects, files, credentials,
   kernel or driver structures, and supplied baselines. Preserve benign
   alternatives and missing cross-vantage evidence.
5. Keep claim types narrow. A connection is a network object, not C2 attribution.
   An LSASS handle is credential access capability, not credential extraction. A
   Run value is a persistence mechanism, not proof it executed.
6. Use `suspicious` for mutually reinforcing indicators within one source group.
   Use `corroborated` only with at least two independent source groups. Use
   `confirmed` only when the claim-specific proof requirements in
7. Track every candidate extraction. `extracted` needs a preserved digest and
   custody. Malware classification needs analysis of the extracted artifact;
   bytes that were never recovered cannot be classified.
8. Build timeline events only from cited times. Keep host-clock time separate
   from trusted time; unknown skew remains a limitation. Do not assign an exact
   timestamp to an object merely because the image has an acquisition window.
9. Cover all required artifact and case categories. Mark missing work `blocked`
   with a blocker rather than calling the surface clean.
10. Record owned, authorization-aware next steps and handoffs. Contact with a
    live host or external service needs explicit authority beyond offline review.

## Boundary with adjacent skills

- Use `rootkit-triage` when live host views may be lying and the task is to
  compare kernel, boot, firmware, memory, disk, and external vantages.
- Use `protocol-traffic-analysis` for packet-capture interpretation.
- Use `credential-exposure-audit` for credential-material inventory and handling.
- Hand extracted binaries to a malware or binary-analysis workflow; this skill
  preserves extraction provenance and the questions to answer.
- Use `detection-engineering` to turn stable observations into detector logic.
- Use `findings-report` for final stakeholder finding prose.

## Rationalizations to reject

- **"Several plugins agree, so the finding is independently corroborated."**
  Plugins reading one image share acquisition and parsing dependencies.
- **"RWX plus an MZ header proves malware."** Legitimate software and injected
  security components can create similar regions; preserve and analyze the bytes.
- **"Port 443 from a suspicious process is C2."** The memory object proves a
  connection, not destination ownership, protocol content, or intent.
- **"A handle to LSASS proves credentials were stolen."** Access capability is
  not proof that credential material was read or used.
- **"A Run value proves persistence succeeded."** It proves a mechanism was
  represented in memory; execution and durable disk state need more evidence.
- **"The image hash makes acquisition trustworthy."** It protects the captured
  file after hashing; it does not validate the acquisition binary or compromised
  source path.
- **"Exact plugin timestamps are trusted UTC."** They remain host-clock values
  until clock basis and skew are established.
