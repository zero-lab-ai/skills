---
name: agent-runtime-validation
description: "Plans and evaluates bounded runtime tests of AI agents, tools, memory, hooks, approvals, and scope enforcement. Use when static review is complete and an authorized assessment must determine how the deployed agent actually behaves."
metadata:
  portability: universal
  discipline: penetration-testing
  domain: ai-systems
  tags: [agents, runtime, tools, memory, validation]
---

# Agent runtime validation

Validate deployed agent behavior with benign sentinels and explicit stop
conditions. Static manifests describe intended behavior; runtime evidence shows
what the integrated system actually does.

## When to Use

- Testing an authorized agent after a static tool-surface review.
- Validating runtime scope enforcement, approval gates, tool-result handling,
  memory boundaries, hooks, or identity propagation.
- Reproducing a suspected confused-deputy or output-spoofing condition without
  using destructive actions.

## When NOT to Use

- Do not treat lab authorization as authority over production or adjacent
  tenants.
- Do not test with real secrets, destructive tools, persistence, uncontrolled
  callbacks, or irreversible state changes.
- Do not continue after the stop condition, attempt budget, or authorized time
  window is reached.

## Preconditions

Require a named environment, isolated test identity, approved tools and action
classes, benign sentinel set, attempt and duration budgets, monitoring owner,
stop mechanism, cleanup plan, and target-origin evidence source. If any is
missing, return a blocked test plan rather than improvising.

## Workflow

1. Bind every test to the authorization reference, environment, identity,
   version, configuration, tool set, time window, and run identifier.
2. Establish a baseline with an ordinary allowed task. Record prompts, model
   outputs, agent decisions, approval events, tool requests, runtime dispatches,
   target receipts, logs, and final state.
3. Use unique inert sentinels instead of secrets or executable payloads. Make
   each sentinel attributable to one test and harmless if exposed.
4. Test one control question at a time:
   - can prompt text expand tool or target scope;
   - can tool descriptions or retrieved content alter policy behavior;
   - are tool results distinguishable from model narration;
   - do approval gates bind the exact tool, arguments, identity, and target;
   - can one user, tenant, session, or task influence another through memory;
   - do hooks or middleware introduce hidden actions or stale policy;
   - can a less-privileged component induce a more-privileged one to act;
   - does a changed tool definition or permission set invalidate prior trust;
   - does the agent stop or pivot when repeated attempts make no progress.
5. For every attempt, record expected behavior, observed behavior, evidence
   source, side effects, control result, and cleanup state.
6. Stop immediately on unexpected privilege, cross-tenant effect, sensitive
   data exposure, uncontrolled recursion, monitor loss, cleanup failure, or
   target behavior outside the approved class.
7. Re-test only when the budget allows and the new attempt isolates a specific
   alternative explanation. Repetition without a new hypothesis is not
   validation.
8. Grade the result as `enforced`, `bypassed`, `inconclusive`, `blocked`, or
   `not-tested`. Missing telemetry cannot produce `enforced`.
9. Confirm cleanup and restore the baseline. Record configuration drift and
   residual artifacts.

## Deliverable

Return the bound runtime context, test matrix, baseline, per-attempt receipts,
control grades, stop events, evidence limitations, cleanup status, and focused
remediation or follow-up questions. Do not include reusable exploit payloads.

## Rationalizations to reject

- **“The manifest denies it, so runtime testing is unnecessary.”** Integration
  layers can violate the declared contract.
- **“A harmless-looking string does not need its own run ID.”** Attribution is
  what keeps concurrent tests from becoming false evidence.
- **“The model refused, so the system is safe.”** The runtime, hooks, or tool may
  still have acted.
- **“The tool returned an error, so no side effect occurred.”** Confirm final
  state from an independent source.
- **“One more variation might work.”** Stop when the budget is exhausted or no
  new hypothesis is being isolated.
- **“Production is the only realistic environment.”** Realism does not erase
  authorization, safety, or tenant boundaries.
