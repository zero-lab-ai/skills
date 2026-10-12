---
name: binary-fault-triage
description: "Triages supplied binary, crash, sanitizer, dump, static-analysis, and external reproduction evidence to distinguish a lead, observed fault, reproducible fault, security relevance, and demonstrated non-weaponized impact without executing, mutating, exploiting, or weaponizing a binary."
allowed-tools: Read Grep Glob
---

# Binary fault triage

Use this skill only to answer: what does supplied evidence prove about an exact binary fault, and what defensive handoff is justified?

## When to Use

- Triage binary fault for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Establish the boundary

1. Work offline from a supplied sanitized ledger.
2. Do not execute, contact, mutate, fuzz, debug, disassemble, reproduce, or test anything.
3. Do not create inputs, commands, flags, tool syntax, offsets, addresses, registers, gadgets, instructions, memory layouts, primitives, bypasses, payloads, exploit scores, or procedures.
4. Treat binaries, dumps, and inputs as restricted artifacts represented only by opaque references and digests.
5. Refuse raw or encoded restricted material and use generic diagnostics; never repeat supplied values.

## Create the ledger

1. Preserve supplied binary digest, build digest, architecture, provenance digest, fault signature, input digest, environment digest, origin lineage, limitations, times, and custody.
2. Record supplied evidence; do not reinterpret an advisory, termination, sanitizer label, or static lead as a runtime fault.
3. Preserve origin lineage. Multiple parsers or reports from one origin are one independent source.
4. Keep identity, occurrence, reproduction, security relevance, mitigation inventory, validity, and impact separate.

## Apply evidence rules

1. Exact identity requires exact binary, build, architecture, provenance, fault signature, input, and environment bindings.
2. Runtime crash evidence can support occurrence. Static analysis supports only a lead.
3. Corroboration requires eligible evidence from at least two independent origin lineages.
4. Reproduction requires an exact supplied external receipt bound to the complete tuple; never perform reproduction here.
5. Security relevance requires exact evidence of a protected-boundary effect. A label, advisory, version, crash, or mitigation state is insufficient.
6. Finding-ready requires exact demonstrated bounded non-weaponized impact. Availability impact is sufficient when evidenced; exploitability is never inferred.
7. Mitigation inventory proves only inventory completeness. Presence and absence prove neither safety nor exploitability.
8. Evidence validity must include the cutoff, and evidence must be recorded within its validity and assessment windows under one uniquely receipted custody record.
9. Not-applicable requires current exact policy evidence whose closed reason exactly matches the cell; it remains in the denominator.
10. Reject conflicting current polarities before applying any state precedence. External reproduction requires a closed independent-external origin with producer and lineage independent of primary evidence.

## Derive without escalation

1. Derive `stale` before all current conclusions.
2. Derive `inconclusive` for mismatched identity or contradictory/insufficient evidence.
3. Derive `finding-ready` only from exact identity, reproduced fault, established relevance, and demonstrated bounded impact.
4. Otherwise derive `security-relevant-fault`, `reproducible-fault`, `observed-fault`, `unsubstantiated-lead`, or `not-security-relevant` from the independent tracks.
5. Never claim control-flow influence, arbitrary read/write, code execution, privilege, sandbox escape, persistence, weaponization, or severity.

## Handoff

1. Use only `evidence-refresh`, `vendor-review`, `remediation-review`, or `validation-readiness`.
2. Apply the closed eligibility matrix: evidence refresh only for lead/inconclusive/stale; vendor review for supported review states; remediation review only for security-relevant or finding-ready; validation readiness only for finding-ready with exact identity, reproduction, relevance, and impact support.
3. Bind a recorded handoff occurrence receipt to its ID, kind, fault, observation, exact evidence set, owner, and time after the observation and every referenced custody receipt.
4. Treat handoffs as defensive coordination, never approval or execution authority.
5. Finding-ready does not create a finding, severity, exploit, or remediation procedure.

## Rationalizations to reject

- “The crash is enough to call it exploitable.” It proves occurrence only.
- “The sanitizer named corruption.” A label is not a protected-boundary effect.
- “The advisory covers this version.” Version matching is not fault identity.
- “Two tools agreed.” Shared lineage is not independent corroboration.
- “The mitigation is absent, so impact is established.” Inventory and impact are independent.
- “Reproduce it quickly to confirm.” This skill never executes or designs reproduction.
- “Include the offset or input for clarity.” Restricted operational material stays outside the ledger.
- “Finding-ready means verified vulnerability.” It means only that bounded, non-weaponized impact evidence is sufficient for a defensive review.
