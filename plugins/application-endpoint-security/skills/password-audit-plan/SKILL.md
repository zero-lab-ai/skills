---
name: password-audit-plan
description: "Plans authorized offline password-strength audits across supplied hash datasets while enforcing compute budgets, progressive pass order, cohort coverage, aggregate-only reporting, and restricted handling. Use when preparing or documenting password cracking without online authentication, spraying, stuffing, replay, or credential reuse testing."
allowed-tools: Read Grep Glob
---

# Password audit plan

Offline password auditing is a measured experiment over supplied material. Algorithm,
hardware, candidate space, runtime, and cohort denominators determine what the result
means. Preserve unknowns until measurement exists.

This skill plans and records offline analysis. It does not collect hashes, expose raw
material, generate organization-derived candidates, authenticate, spray, stuff,
replay, test reuse, contact accounts, or access target systems.

## When to Use

- Preparing or documenting password cracking without online authentication, spraying, stuffing, replay, or credential reuse testing.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record authorization, offline-only boundary, compute and storage ceilings,
   prohibited sources and actions, stop conditions, workspace, retention, owner, and
   disposition evidence.
2. Inventory each dataset using opaque IDs. Record source class, record and unique
   digest counts, acquisition-time precision, algorithm claim, validation state,
   cost parameters, integrity, and limitations. Never place raw hashes in the plan.
3. Preserve record counts and digest counts separately. Deduplicate work while keeping
   the mapping needed to expand aggregate recoveries back to record and cohort counts.
4. Define cohorts with explicit denominators and overlap rules. Disabled, privileged,
   service, administrator, and standard populations remain separate where supplied.
5. Plan format validation and a measured benchmark before recovery passes. Do not
   invent throughput, runtime, keyspace completion, or recoveries.
6. Order bounded passes from generic baseline through generic rules, bounded masks,
   and optional adaptive work. Each pass names dependencies, candidate-source class,
   dataset, GPU budget, expected measurement, and stop conditions.
7. Let the review reject budget over-allocation, recovery before validation and
   benchmark, prohibited candidate sources, online actions, unproved results, and
   inconsistent cumulative counts.
8. Record pass results as counts and rates only. Attribute each unique recovery to its
   first successful pass; expand record recovery and cohort recovery from the preserved
   mapping without exposing plaintext.
9. Analyze aggregate length, character-class, duplicate, pattern-label, cohort, policy
   shape, and marginal-yield metrics. A policy document is a requirement, not proof a
   recovered password complied when created.
10. Track raw datasets, recovered material, potfiles, restore state, generated
    candidates, logs, and exports through disposition. Report only approved aggregate
    artifacts and opaque IDs.
11. Cover format, deduplication, cohorts, benchmark, baseline, rules, masks, adaptive
    work, handling, and reporting for every dataset. Blocked work remains visible.

## Boundary with adjacent skills

- Use `credential-exposure-audit` to inventory possible credential exposure without
  cracking or decrypting.
- Use `password-audit-plan` only after offline material and authority are supplied.
- Use `findings-report` after aggregate audit results are proven.
- Online authentication, spraying, stuffing, reuse checks, and account contact require
  a separate capability and authorization; they are outside this skill.

## Rationalizations to reject

- **"The manifest says NTLM, so mode selection is settled."** Validate structure before
  spending compute or interpreting results.
- **"Deduplication reduced 1,000 accounts to 860 hashes."** It reduced work items, not
  the reporting population. Expand results back to records and cohorts.
- **"The benchmark should be about this fast."** Hardware labels and published speeds
  are not measurements of this dataset and configuration.
- **"Eight hours means every pass gets an equal share."** Allocate from measured cost,
  expected evidence value, and explicit priorities; record the rationale.
- **"Recovered means valid."** Offline equality says nothing about current account
  state, usability, privilege, or successful authentication.
- **"Examples make the pattern finding clearer."** Plaintext examples and reusable
  candidate strings do not belong in the assessment record or report.
- **"The potfile is just tool state."** It contains recovered evidence and inherits the
  same storage, access, retention, and deletion rules.
- **"One more pass cannot hurt."** The compute ceiling and stop conditions are part of
  authorization, even when the hardware is idle.
