---
name: binary-fault-validation-readiness
description: "Governs an exact current binary-fault-triage assessment result and recorded validation-readiness handoff for separate isolated-lab review. Use when checking defensive authority, isolation, budget, stop, cleanup, custody, and independent-review readiness without analyzing faults, creating tests or inputs, determining exploitability, or authorizing execution or development."
allowed-tools: Read Grep Glob
---

# Binary fault validation readiness

## When to Use

- Checking defensive authority, isolation, budget, stop, cleanup, custody, and independent-review readiness without analyzing faults, creating tests or inputs, determining exploitability, or authorizing execution or development.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Purpose

Validate a supplied closed readiness ledger and produce, at most, a
non-authorizing handoff for separate isolated validation review. A complete
ledger establishes internal consistency only; it does not approve, perform, or
describe validation.

## Boundary

Never inspect or analyze a binary fault. Never execute, mutate, fuzz, debug,
disassemble, reproduce, or validate anything. Never create a test, input,
exploit, payload, proof of concept, command, pseudocode, debugger syntax,
address, offset, register, instruction, gadget, memory layout, primitive,
bypass, path, or target. Never determine exploitability, severity, success, or
validation outcome. Never authorize execution, exploit development, or use of a
production environment.

## Workflow

1. Accept only a supplied exact `binary-fault-triage/v2` assessment result whose
   review status is `passed` and whose upstream handoff is recorded
   `validation-readiness`.
2. Stop on operational or restricted content. Do not quote rejected values.
3. Verify the canonical imported receipt over the complete opaque binary,
   build, architecture, provenance, fault, input, environment, observation,
   artifact, review, policy, and upstream handoff bindings.
4. Record only supplied passive sanitized receipts. Never contact an artifact,
   source, lab, target, or downstream operator.
5. Instantiate all nine essential readiness checks. None is not-applicable.
6. Keep authority actions limited to `readiness-review` and
   `handoff-recording`; neither grants execution authority.
7. Require every satisfied check to carry one canonical role-specific subject
   proof. Require an isolated non-production lab, exact numeric ceilings, exact
   stop-pretest proof, ready cleanup, retained custody, and genuinely independent
   review lineage.
8. Derive gate precedence as `prohibited`, `triage-refresh-required`,
   `approval-required`, `blocked`, then `handoff-ready`.
9. Treat `handoff-ready` as readiness for separate review only. It is not
   execution permission, validation success, or a technical conclusion.
10. Keep handoffs exact-bound and chronological. Null ownership derives
    `withheld`; a recorded occurrence requires an opaque owner and later receipt.
11. Derive withdrawal after authority expiry or revocation, bound drift,
    custody disposal, budget exhaustion, a fired stop, or cleanup loss. Require
    a later exact trigger-bound receipt for `withdrawn`.

## Report

State the ledger identifier, contradictions, exact gate and handoff counts,
blocker gate IDs, and withdrawal handoff IDs. Add: “Internal readiness
consistency only; no fault analysis, validation, execution authority,
exploitability determination, or development authorization occurred.”

## Rationalizations to reject

- **“The triage review passed, so run a quick confirmation.”** The upstream
  receipt starts governance only; this skill never validates.
- **“Finding-ready means exploitable.”** Triage explicitly does not establish
  exploitability, and this ledger cannot add that claim.
- **“The input digest is available, so reconstruct the input.”** Digests bind
  identity only; restricted artifacts stay opaque.
- **“The lab is isolated, so authority is implied.”** Isolation and authority
  are independent mandatory checks.
- **“A handoff-ready gate authorizes the operator.”** It permits only separate
  review; downstream execution authority is outside this skill.
- **“A stopped or expired package can be resumed.”** No retry or resume state
  exists; refresh the evidence and establish a new readiness record.
