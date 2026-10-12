---
name: web-assessment-coverage
description: "Tracks web application assessment coverage across endpoints, inputs, roles, authentication states, and test families, preventing untested or blocked work from being reported as clean. Use when planning, conducting, reviewing, or handing over an authorized web or API penetration test."
allowed-tools: Read Grep Glob
---

# Web assessment coverage

A web assessment is complete only when every discovered surface has an honest
disposition. A route inventory is not coverage, and a planned test is not a
negative result.

Use this skill only inside written authorization. Scope, rate, impact, test
accounts, and permission for state changes come from the engagement, not from
this skill.

## When to Use

- Planning, conducting, reviewing, or handing over an authorized web or API penetration test.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Build the coverage ledger

1. **Record the assessment boundary.** State the exact in-scope origins,
   engagement type, available identities, action classes allowed now, request
   limits, excluded systems, and handling constraints. Stop at out-of-scope
   redirects and resource hosts.
2. **Inventory surfaces before testing.** Record every observed route, method,
   input, authentication state, API operation, GraphQL operation, WebSocket,
   upload, business workflow, client-side surface, and configuration surface.
   Preserve distinct methods and trust contexts as distinct surfaces.
3. **Derive required families.** require:
   - any surface with input: `injection`;
   - authentication surface: `authentication` and `session-management`;
   - API: `api`; GraphQL: `api` and `graphql`;
   - upload, WebSocket, business logic, client side, and configuration: their
     matching test family;
   - ownership-sensitive surface: `horizontal-access-control` role checks;
   - privilege boundary: `vertical-access-control` role checks.
4. **Name access-control pairs.** For horizontal checks, identify the actor and
   peer resource owner, including the reverse direction when both matter. For
   vertical checks, identify the lower-privilege actor and privileged target.
   An unavailable administrator account limits what can be concluded; it does
   not make vertical coverage complete.
5. **Give each required case one status.** Use `planned`, `executed`, `blocked`,
   or `not-applicable`. Blocked cases name the blocker. Not-applicable cases
   explain why the family does not apply. Planned cases remain untested.
6. **Separate status from outcome.** Only an executed case can report
   `finding`, `no-issue`, or `inconclusive`, and every executed case links to
   evidence. Every other status uses `not-run`.
7. **Enforce authorization per case.** Classify the action as read-only,
   authenticated read, reversible state change, state change, active execution,
   high volume, or external contact. Work outside the currently allowed classes
   is marked `requires-separate-approval`; never present it as executable now.
8. **Summarize by family without hiding gaps.** Each family summary references
   all of its coverage records. derive the claim:
   - any evidenced finding → `finding`;
   - any planned or blocked case → `incomplete`;
   - otherwise any inconclusive execution → `inconclusive`;
   - fully executed cases with no findings → `no-issue`;
   - all cases justified as not applicable → `not-applicable`.
9. **Send confirmed vulnerabilities to the reporting skill.** Coverage says
   what was tested. A finding still needs reproducibility, impact, severity, and
   remediation.

## Test depth follows the engagement

- **Completeness does not mean maximum impact.** Cover a high-impact family with
  a blocked or approval-gated record when safe validation is unavailable.
- **Use known fixtures for authorization.** Comparing two supplied accounts is
  evidence; enumerating other customers is scope expansion.
- **State changes need recovery.** Define the exact mutation, expected artifact,
  restoration action, and maximum attempts before seeking approval.
- **Negative bounded tests have limits.** A small race or rate sample may find a
  flaw, but silence does not establish resilience against higher volume.
- **Third-party services remain separate targets.** Record an external redirect,
  storage URL, mail system, or payment processor without touching it unless its
  origin is explicitly in scope.

## Judgment calls

The script derives required families from the normalized surface fields and
checks the evidence contract. It cannot decide whether the route inventory is
complete, whether a payload was technically adequate, or whether linked
evidence proves the claimed security behavior. Review those judgments directly.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "We planned the test, so this area is covered." | Planned means unexecuted. It supports an `incomplete` summary. |
| "The scanner found nothing." | A tool result proves only the surfaces and techniques it actually exercised. |
| "One user-to-user check covers IDOR." | Record every required direction and role pair explicitly. |
| "We lack an admin account, so vertical access control is not applicable." | Low-privilege denial may be testable; privileged workflow coverage remains blocked. |
| "No finding means secure." | It means no issue was observed within the executed coverage and its limits. |
| "A harmless upload or checkout does not count as a state change." | It still creates client state and requires the authorization assigned to that action class. |
| "The route points to another host, so it is part of the app." | Scope follows explicit origins, not architectural association. |
