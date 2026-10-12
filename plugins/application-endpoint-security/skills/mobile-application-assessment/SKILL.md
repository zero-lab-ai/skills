---
name: mobile-application-assessment
description: "Tracks Android and iOS application assessment coverage across packages, platform components, local storage, device behavior, WebViews, native code, network trust, and delegated backend APIs. Use when planning, conducting, reviewing, or handing over an authorized mobile app penetration test."
allowed-tools: Read Grep Glob
---

# Mobile application assessment

A decompiled indicator is not a runtime exploit, a rooted-device observation is
not ordinary-device reachability, and one denied backend request is not an API
authorization assessment. Keep each claim tied to its build, layer, method, and
evidence.

## When to Use

- Planning, conducting, reviewing, or handing over an authorized mobile app penetration test.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record the exact Android package or iOS bundle, platform, build kind, and
   SHA-256. Keep evidence from different builds in separate assessments.
2. State allowed action classes, structured test devices and accounts, in-scope
   origins, and constraints. Prevent production and third-party traffic at the test boundary
   when the app contains out-of-scope destinations.
3. Inventory one `application` surface per build, then add discovered storage,
   component, network endpoint, WebView, native library, cryptographic use,
   runtime defense, privacy channel, and backend API surfaces.
4. Give every surface an evidence reference and disposition. Static reachability
   supports a conditional exposure; runtime effect needs runtime evidence.
5. Cover all eight current MASVS categories for the application surface:
   storage, cryptography, authentication, network, platform interaction, code,
   resilience, and privacy. Add the categories derived for each detailed surface.
6. Record each case as `executed`, `planned`, `blocked`, `not-applicable`, or
   `delegated`. Only executed cases can claim a finding, no issue, or an
   inconclusive result. Preserve blockers and technical rationales.
7. Separate app, device, backend, and third-party evidence. A mobile client can
   expose an API route, but server-side authorization coverage belongs in the
   web assessment ledger. Preserve a bounded observed backend request as an
   executed case, then add a separate `delegated` case for the broader handoff.
8. Treat public identifiers, private secrets, exported components, client-side
   state, pinning, backup settings, root detection, and native code according to
   demonstrated impact. Their presence alone does not set severity.
9. Build category summaries from all recorded cases. Record the derived open
   case IDs so planned, blocked, delegated, and inconclusive work stays visible
   even when a confirmed finding takes precedence in the category claim.

## Interpretation rules

- App-private plaintext remains relevant under the stated compromised-device
  threat model; it does not mean another ordinary app can read the data.
- `exported=true` proves reachability, not missing authorization or unsafe effect.
- Pinning observed on one flow says nothing about unobserved endpoints. Bypassing
  it in a lab is a test-enablement action, not itself a finding.
- A publishable key is not a private secret. Identify the key type and supported
  privilege before reporting exposure.
- Changing local UI state proves client control of presentation. It proves a
  server authorization issue only when the server accepts the resulting action.
- Root or jailbreak detection is threat-model dependent. Record what it protects
  and whether enforcement is local or server-side.
- A native library is an analysis surface, not a vulnerability.

## Rationalizations to reject

- **"The manifest proves exploitation."** It proves configuration and potential
  reachability. Trace and test the effect before claiming impact.
- **"The emulator is rooted, so plaintext storage is automatically critical."**
  Severity depends on data value, token lifetime, replay, device assumptions, and
  compensating server controls.
- **"We bypassed pinning, so pinning failed."** An authorized instrumentation
  bypass proves tester capability, not a defect in the deployed control.
- **"The API denied one cross-user request, so authorization is sound."** The
  result applies only to that actor, target, operation, identifier, and backend.
- **"The hostname is in the APK, so it is in scope."** Scope comes from written
  authorization. Record an out-of-scope destination without contacting it.
- **"A scanner covered MASVS."** Coverage requires explicit cases, evidence,
  blockers, and honest summaries across static and dynamic methods.
