---
name: findings-report
description: "Writes security findings that survive triage: reproducible, severity-justified, and fixable, in a fixed structure with a severity rubric. Use when turning a discovered vulnerability, misconfiguration, or weakness into a report entry, ticket, or disclosure."
allowed-tools: Read Grep Glob
---

# Writing security findings

A finding is an argument: here is a flaw, here is how to see it yourself,
here is what it costs you, here is what to do. Most findings fail at triage
because one of those four is missing or because the severity was asserted
rather than derived. This skill produces findings in a fixed shape and checks
the argument before prose can hide a missing part.

## When to Use

- Turning a discovered vulnerability, misconfiguration, or weakness into a report entry, ticket, or disclosure.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Quick start

1. Collect, before writing a word: the exact reproduction (input, steps,
   observed result), the affected component and version, and evidence
   (output, screenshot path, request/response). If you cannot reproduce it,
   it is a *lead*, not a finding; label it as such.
2. Fill `references/finding-template.md` from the checked record. Every
   section is required. "N/A" is acceptable only for `References`.
3. Write the fix as a concrete change, not a category. "Validate input" is a
   category. "Reject `path` values that resolve outside `DATA_ROOT` after
   `os.path.realpath`" is a fix.
4. Reread the title. It should name the component and the flaw, and a reader
   should be able to guess the severity from it.

## Finding or lead

| Evidence state | Report as | Why |
| --- | --- | --- |
| Reproduced flaw with bounded impact | Finding with severity | The argument can be independently checked |
| Strong signal, reproduction incomplete | Unrated lead | The signal deserves follow-up but impact is not established |
| Version or pattern match only | Observation or lead | Applicability is not proven by a label |
| Control claimed but not verified | Open precondition | A stated control cannot reduce severity without evidence |
| Work blocked by scope or safety limit | Limitation | Blocked work is not a negative result |

Example: a response containing another user's record supports an authorization
finding. A route name containing `admin` does not; it is a lead until access and
impact are demonstrated.

## Rules that keep findings credible

- **One flaw per finding.** Two flaws in one entry get one fix and one
  severity, and one of them is wrong.
- **Reproduce in the reader's environment, not yours.** Replace your paths,
  hostnames and tokens with the reader's or with placeholders they can fill.
- **Quote the evidence, do not describe it.** Paste the response body, the
  log line, the stack trace. Trim, do not paraphrase.
- **Impact is what an attacker gets, not what the bug is.** "SQL injection"
  is the bug. "Read any row in `users`, including password hashes, as an
  unauthenticated caller" is the impact.
- **Quantifiers are evidence claims.** One tested account and two records prove
  that account reached those records. They do not prove every account, every
  record, or exploitation at scale. State the demonstrated set, then label
  broader blast radius as a hypothesis requiring coverage evidence.
- **Likelihood is about preconditions.** Say what the attacker needs:
  network position, an account, a victim click, a race. Each precondition
  lowers likelihood; say so explicitly.
- **Never pad with speculation.** "Could potentially lead to RCE" without a
  demonstrated path is a lead. Put it in `Notes`, not `Impact`.
- **Fix and mitigation are different.** The fix removes the flaw. A
  mitigation reduces exposure while the fix is pending. Label each.

## Severity in one line each

| Severity | Shape of the justification |
| --- | --- |
| Critical | Unauthenticated or low-privilege attacker gets full control or all data, no victim interaction |
| High | Significant data or control, with one precondition (account, victim action, adjacent network) |
| Medium | Limited data or control, or significant impact behind two or more preconditions |
| Low | Information useful for other attacks, or impact confined to the attacker's own session |
| Info | No direct security impact; hygiene, defense in depth, or a deviation from stated policy |

Full rubric with worked examples: `references/severity-rubric.md`.

## Rationalizations to reject

- **"The prose makes the severity obvious."** Readers can disagree; the
  normalized factors and review make the decision reproducible.
- **"The screenshot exists somewhere."** If the record cannot point to it,
  triage cannot verify the claim.
- **"This lead is probably critical."** Unreproduced escalation stays an
  unrated lead until evidence establishes its impact.
- **"The IDs are predictable, so every record is exposed."** Predictability
  supports a follow-up hypothesis; only tested coverage or authoritative access
  logic supports a universal impact claim.
- **"The workaround is good enough to call a fix."** A mitigation reduces
  exposure and states its limit; only a change that removes the flaw is a fix.
