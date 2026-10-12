---
name: recon-automation-governance
description: "Governs supplied reconnaissance job manifests with exact authority and scope binding, contact receipts, bounded waves and budgets, controlled retries, tested stop controls, custody, and defensive handoff. Use when reviewing or recording scheduled recon automation without generating commands, choosing targets, running reconnaissance, or expanding scope."
allowed-tools: Read Grep Glob
---

# Recon automation governance

Automation multiplies both consistency and mistakes. Govern supplied opaque job envelopes so a
scheduler cannot turn a valid recon method into unauthorized scope, unbounded contact, silent
retry, or persistent surveillance.

This skill is a control plane only. It does not acquire or select targets, classify a new action,
generate commands or queries, choose tools, execute reconnaissance, evade detection, interpret
results, build target profiles, or create findings.

## When to Use

- Reviewing or recording scheduled recon automation without generating commands, choosing targets, running reconnaissance, or expanding scope.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record current written authority, the immutable plan and configuration digests, exact opaque
   scope units, the engagement window, retention, and every prohibited output.
2. Import passed upstream review receipts. `osint-scanner` admission requires its passive-plan
   receipt; network admission requires the exact `network-recon` scope receipt. A post-run scan
   coverage receipt cannot substitute for scope. Input production, checking, and validity must
   precede and contain the work they admit. Never reclassify or strengthen these decisions.
3. Define each job as an opaque envelope with a fixed capability, posture, contact class, scope,
   input, authorization, wave, state, retry policy, and closed limitations. Store no target,
   endpoint, query, command, flag, identity, credential, or infrastructure detail. Unknown,
   unmapped, or posture-conflicting contact remains blocked.
4. Bind every runnable job to one current authorization whose exact reverse sets cover its plan,
   configuration, inputs, scope, contact, budget, and execution window. Register each receipt once
   with one typed purpose and subject; a receipt or digest cannot prove two roles. Authority and
   its approval receipt must exist before every bound gate and cover each full attempt.
5. Build an acyclic dependency graph. A prerequisite must be in an earlier wave, and a runnable
   job needs every dependency receipt satisfied.
6. Require an initial approval gate for runnable work, a target-contact gate for target contact,
   and a distinct attempt-bound retry gate after each retryable failure. Its receipt and decision
   must exist after the prior outcome and before the next attempt.
7. Reserve request, target-contact, runtime, rate, concurrency, storage, and attempt budgets before
   admission. Charge every attempt inside its budget window and reject per-job, wave,
   authorization, or global overflow.
8. Keep retry reasons closed, attempt numbers contiguous, backoff nondecreasing, and retry counts
   bounded. Authority, scope, drift, custody, review, and operator-kill failures never retry.
9. Quarantine discoveries as opaque IDs and source-job references only. Store no discovered target
   detail. A candidate may be rejected or handed to scope review, but its ID cannot enter a job,
   input, scope, or executable set without a new authority and immutable plan version.
10. Arm and successfully test the owned global kill switch before any allow gate. A fired stop is
    terminal for this ledger; v0.1 has no resume state. Operator kill prevents later starts and
    retries across the complete job set.
11. Bind attempt and stop evidence to digest-addressed artifacts, one custody record each, ordered
    retention and disposition, and opaque owners. Stale or disposed evidence proves no current
    completion and cannot enter a consuming handoff; retain only its opaque disposition receipt.
    No event, receipt, artifact, discovery, or attempt may postdate the analysis cutoff.
12. Derive job, wave, and attempt states from gates, attempts, evidence, stops, and freshness. Never
    author `complete`, `partial`, `failed`, `stale`, `blocked`, or `skipped` by intuition.
13. Create defensive handoffs only: upstream validation, scope review, coverage review, custody
    disposition, or specialist assessment. Governance output is not claim-bearing.
14. Cover authority, scope, inputs, contact, dependencies, gates, budgets, retries, stop controls,
    custody, discovery quarantine, and handoff for every job with exact proof sets.

## Boundary with adjacent skills

- `osint-scanner` classifies passive contact; this skill trusts only its exact passed receipt.
- `network-recon` scope receipts govern admission; its post-run coverage receipts support handoff
  only. Neither is interchangeable, and this skill imports no targets or commands.
- `opsec-planning` owns objective risk, observability, abort, and cleanup reasoning.
- `target-profile-synthesis` interprets validated evidence; governance output is boundary evidence.
- `findings-report` owns demonstrated issues, severity, reproduction, and fixes.

## Rationalizations to reject

- **"The upstream review passed, so the scheduler may run."** One receipt proves one boundary.
- **"A discovered adjacent asset is implied scope."** Quarantine it and request new authority.
- **"A retry is the same action."** It consumes new quota, contact, time, and approval.
- **"Passive jobs are free."** Third-party quotas, privacy, cost, retention, and policy still bind.
- **"Backoff makes every retry safe."** Some stops prohibit another attempt entirely.
- **"One receipt can prove several controls."** A digest proves only its typed subject and purpose.
- **"We can add the kill switch later."** It must be armed and tested before runnable state.
- **"Failure left no evidence."** Partial contact and errors still need custody and handoff.
- **"Stale means delete it now."** Follow authorized disposition; keep only its opaque receipt.
- **"Unknown contact is probably harmless."** Unknown and unmapped work remains blocked.
- **"Automation output is a finding."** It is governance evidence until a specialist validates it.
- **"Unused budget can move anywhere."** Allocation remains authority, scope, and class bound.
