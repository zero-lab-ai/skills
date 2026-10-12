---
name: detection-resilience-test-plan
description: "Plans and records bounded defensive tests of whether preventive controls, telemetry, and detections remain effective across pre-approved opaque technique variations. Use when a blue or purple team needs authorization-, safety-, evidence-, cleanup-, and remediation-gated resilience measurement without generating bypass procedures, commands, payloads, or stealth rankings."
allowed-tools: Read Grep Glob
---

# Detection resilience test plan

Measure whether a particular defensive environment prevents, observes, and
detects a pre-approved synthetic test. Keep those claims separate and bind them
to evidence, an exact environment fingerprint, and an expiry window. A finding
of a real control gap is a useful result; fabricated coverage is not.

## When to Use

- A blue or purple team needs authorization-, safety-, evidence-, cleanup-, and remediation-gated resilience measurement without generating bypass procedures, commands, payloads, or stealth rankings.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Boundary

Consume externally supplied fixtures by opaque ID and SHA-256 digest only.
Never create, transform, reconstruct, rank, or recommend a fixture or technique
implementation. Record only bounded defensive facts and approved receipts.
Use only the contract's bounded declarative grammar in descriptions and rationale;
arbitrary prose, imperatives, and comparative rankings cannot be recorded.

Version 0.1 permits `isolated-lab` and `dedicated-test-tenant` environments.
Production execution is prohibited. Do not include hostnames, addresses,
domains, accounts, paths, tenant names, organizations, credentials, client data,
or malware. Scope identifiers are opaque; evidence locators are opaque references.

Do not supply source code, pseudocode, operational commands, flags, payloads,
build instructions, mutation, encoding, packing, obfuscation, signature-avoidance,
loader guidance, injection, in-memory execution, syscall, sandbox-detection,
inspection bypass, security-tool disablement, or telemetry-blinding procedures.
Do not supply C2 profiles, jitter, protocol mimicry, fronting, traffic shaping,
product-specific working bypasses, stealth scores, likelihoods, rankings, or
deployment advice. A request for any of these cannot be fulfilled by this skill.

## Workflow

1. **Declare authority before planning attempts.** Start from an external
   authorization artifact bound to exact scope units, environment profiles,
   fixtures, action classes, operators, windows, and budgets. Placeholders are
   not approvals. Missing authority is a blocker, never implied permission.

2. **Pin isolation and the defensive environment.** Record the isolated
   environment class and broad scope categories. Bind immutable receipts for
   the platform, control product, engine, content, policy, analytic package,
   time synchronization, and rollback baseline. Drift makes prior results
   historical rather than current coverage.

3. **Reference approved opaque fixtures and declare hypotheses.** Record the
   supplier receipt, digest, integrity proof, synthetic provenance, taxonomy
   reference, benign effect class, and semantic-equivalence evidence. Define
   each hypothesis before execution for one exact fixture, environment, and
   scope tuple. A hypothesis says what to measure; it cannot predict the result.

4. **Declare readiness, budgets, and stop controls.** Bind per-case and aggregate
   attempt, duration, state-change, and signal ceilings. Name the stop owner and
   pretest evidence. Unexpected impact, telemetry loss, scope drift, exhausted
   budget, or lost rollback readiness requires stopping. There is no resume path
   within a stopped attempt; retry requires a new approval gate.

5. **Record supplied attempt facts within that envelope.** This skill records
   authorized execution performed through an external approved process; it does
   not execute or provide that process. Preserve failed, blocked, and stopped
   attempts. A retry is a new attempt and cannot borrow a previous result.

6. **Keep evidence roles distinct.** Record prevention response, benign effect,
   telemetry baseline and field availability, query completion and window, and
   alert outcome separately. Silence supports `not-detected` only with healthy
   telemetry and a complete query spanning the attempt; otherwise it is
   `inconclusive`.

7. **Preserve custody and prove cleanup.** Bind each evidence artifact to one
   terminal custody record, including artifacts unused in claims. Keep stale,
   unavailable, disposed, future, cross-scope, and tuple-mismatched evidence out
   of current claims. Cleanup completion requires causally later exact proof and
   never authorizes disposal of retained defender evidence.

8. **Record gaps, remediation, and the whole coverage universe.** Bind each gap
   to exact support and an owner. An implemented change is not verified
   remediation without a later bounded retest. Keep every hypothesis and
   applicable control-layer cell in the denominator, including planned,
   blocked, prohibited, stopped, inconclusive, excluded, and gap cases.

9. **Derive states from the supplied record.** Apply the declared precedence and
   evidence-role rules consistently to readiness, attempt, prevention,
   detection, benign effect, combined outcome, validity, cleanup, gaps, and
   remediation. Leave claims unresolved when required facts are unavailable. A
   complete record grants no execution authority and proves no deployment safety.

10. **Hand off the evidence-bound result.** Report current versus stale outcomes,
    blockers, gaps, budget consumption, cleanup failures, remediation state, and
    required owners. Keep unknown prerequisites, field availability, telemetry
    health, and incomplete queries visible; never invent receipts or measurements.

## Boundary with adjacent skills

- `detection-validate` owns broader post-exercise technique coverage; export only
  this ledger's final alert outcome with its evidence and validity limitations.
- `detection-engineering` owns detector creation and tuning. Hand off the gap and
  verification objective without rule logic or query text.
- `opsec-planning` owns red-team operational risk. This skill measures defensive
  resilience and cannot recommend quieter actions.
- `covert-channel-assessment` owns channel feasibility, receiver authorization,
  transfer budgets, and marker custody. Do not construct channels here.
- `protocol-exploitation-assessment` owns protocol weakness and demonstrated
  impact. Do not craft traffic or establish exploitability here.
- `findings-report` owns final finding prose and severity. Supply evidence-bound
  gaps and remediation state.
- `security-test-tool-governance` owns provenance, integrity, version-bound assurance,
  custody, and controlled internal-lab handoff for an externally supplied artifact.
  Neither skill constructs, modifies, or deploys tooling.

## Rationalizations to reject

| Shortcut | Why it fails |
| --- | --- |
| "a complete record authorizes the run." | Consistency is not authority. Exact external authorization and readiness govern every attempt. |
| "The fixture is approved, so adapting it is harmless." | Approval binds a digest and semantics. Adaptation changes the approved object and is outside this skill. |
| "The fixtures look equivalent; no receipt is needed." | Similar labels cannot prove identical benign semantics. Exact supplied equivalence evidence must bind the approved fixture and tuple. |
| "It was blocked, so detection is covered." | A prevention response cannot substitute for alert evidence or an observed effect. |
| "No alert means a control gap." | Silence under unhealthy or incomplete telemetry is inconclusive. |
| "This variation probably produces no alert." | A hypothesis is an expectation, not a measurement. Only bound health, complete query, and alert-absence evidence support measured silence. |
| "Rank the variations from quietest to loudest." | Stealth ranking turns defensive measurement into operational guidance. Hand off measured defensive gaps and their limits only. |
| "Production realism justifies relaxing isolation." | This version prohibits production. Realism cannot expand external authority or replace the isolated environment boundary. |
| "Reuse the old result after a product update." | Environment drift or expiry makes the old result stale. A current claim needs an exact current tuple. |
| "Keep retrying until something passes." | Each retry needs a new approval gate and consumes bounded budgets; stops do not permit resumption. |
| "Omit blocked cases to simplify the coverage number." | Unassessed cases remain in the universe. Removing them fabricates coverage. |
| "Cleanup includes clearing defensive logs." | Test-state cleanup and defender-evidence custody have independent lifecycles. |
| "The fix shipped; close the gap." | Verification requires causal post-change evidence and a current bounded retest reaching the objective. |
| "A real gap should fail validation." | The assessment validates truthful records. Hiding a measured failure corrupts the result. |
| "The finding needs a concrete bypass example." | Commands, payloads, recipes, and reconstruction details stay outside this skill even under pressure. Use opaque references and defensive facts. |
| "An alert makes query completeness irrelevant." | Alert presence can prove detection, but query status must still match its proof; telemetry restoration needs a complete query. |
| "Give the disposed proof a new evidence ID." | A label cannot change the artifact's custody lifecycle. Conflicting exact aliases invalidate current proof. |
| "Only configure the stop condition likely to fire." | Readiness requires the complete mandatory set, regardless of the one trigger recorded for an event. |
| "The gates once passed, so the expired plan is ready." | Readiness is assessed within the hypothesis lifetime; an old approval does not extend expiry. |
