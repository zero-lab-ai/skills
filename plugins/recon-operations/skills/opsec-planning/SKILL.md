---
name: opsec-planning
description: "Builds red-team OPSEC plans that connect an authorized objective to observable artifacts, detection risk, countermeasures, abort conditions, cleanup, and post-operation review. Use before a significant action or attack chain when stealth matters, when choosing between noisy and quiet approaches, or when an operator needs an auditable go/no-go decision."
allowed-tools: Read Grep Glob
---

# OPSEC planning

OPSEC is deliberate risk selection. The goal is not zero telemetry; every
meaningful action leaves evidence somewhere. The output is a plan that states
what the operation protects, who can observe it, which artifacts each action
creates, why the risk is worth taking, and when the operator stops.

This skill operates only inside written authorization. It helps choose among
authorized actions and never expands scope or grants permission to execute.

## When to Use

- Use OPSEC Planning for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Build the plan

1. **State the objective and posture.** Define the smallest proof that satisfies
   the engagement objective. Choose maximum stealth, balanced, or speed priority.
2. **Identify critical information.** Record what would expose the operation:
   infrastructure, identities, tooling, credentials, timing, and target pattern.
3. **Model the observers.** Name the people and controls able to see the work and
   the telemetry available to them. Unknown visibility increases uncertainty; it
   does not count as absence of monitoring.
4. **Reduce the chain.** Remove actions that do not directly advance the stated
   objective. Being in scope makes an action permissible, not necessary.
5. **Account for four surfaces.** For every remaining action, describe disk,
   memory, log, and network artifacts. If a surface has no expected artifact,
   say why. Never leave it blank.
6. **Score before mitigation.** Estimate detection probability from `0.0` to
   `1.0`, detection impact from `1` to `10`, and success value from `1` to `10`.
   Compute `risk = probability × impact` and record the evidence behind the
   estimates.
7. **Choose and link countermeasures.** Each countermeasure references the
   exposure it changes. Explicitly accept any remaining exposure; silence is not
   acceptance. Recalculate residual probability and risk.
8. **Set stop and recovery conditions.** Give each action a concrete abort
   condition. Cover every artifact with removal, reversion, expiration
   verification, authorized retention, or documentation as unremovable.
9. **Plan the detection review.** Name the telemetry or coordination evidence
   that will confirm what fired and what did not.

## Decision thresholds

| Initial or residual risk | Success value | Consistent decision |
|---|---:|---|
| `< 3` | `> 5` | execute |
| `3` to `< 5` | `> 7` | execute with caution |
| `5` to `8` | any | mitigate first |
| `> 8` | any | abort or request authorization |

The source method leaves low-value gaps between its explicit thresholds. In
those gaps, abort or request authorization rather than inventing permission.
At the shared boundary of `5`, use the safer `mitigate-first` decision.

## Judgment calls

- **Probability needs evidence.** Base it on observed controls, telemetry,
  baselines, and prior validation. A precise decimal with no evidence is still
  a guess.
- **A linked countermeasure may still be weak.** A complete record shows that
  every exposure was addressed or accepted; it cannot prove the proposed
  change reduces detection.
- **Normal-looking is environment-specific.** Native tooling and business-hour
  activity can be more visible when the baseline says they are unusual.
- **Residual risk is a new claim.** Explain what changed between the initial and
  residual probability. Do not lower the number merely because a mitigation was
  written down.
- **Authorization remains external.** A complete record validates the document,
  not the action. Required human approval still governs execution.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "It is in scope, so we should test it." | Scope permits an action. The objective decides whether it belongs in this chain. |
| "This native command will blend in." | Native is not invisible. Decide from the target's baseline and monitored channels. |
| "We will clean it up afterward." | Logs and network records may be immutable. Name them and document them instead of promising deletion. |
| "The risk score is low enough." | A score without evidence for probability and impact is decorative arithmetic. |
| "The countermeasure handles it." | State which exposure changes and why the residual probability is lower. |
| "We can decide the stop condition live." | Fatigue and proximity to the objective bias the operator toward continuing. Set the stop before execution. |
| "A complete record means go." | It means the plan is internally consistent. Authorization and operator judgment still control execution. |
