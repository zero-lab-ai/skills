---
name: ml-decision-boundary-assessment
description: "Evaluates classifiers and scoring models used as security gates for adversarial robustness, preprocessing differences, thresholds, abstention, and fallback behavior. Use when an authorized assessment must measure whether bounded input changes alter a security decision."
metadata:
  portability: universal
  discipline: penetration-testing
  domain: ai-systems
  tags: [ml, classifiers, adversarial-robustness, security-gates, evaluation]
---

# ML decision boundary assessment

Measure the security behavior of a classifier or scoring model as an integrated
gate. Evaluate paired inputs, preprocessing, thresholds, fallbacks, and
downstream decisions instead of celebrating one changed label.

## When to Use

- Assessing a classifier, detector, moderation model, fraud score, or other ML
  component used to permit, block, route, or escalate activity.
- Measuring robustness within an approved perturbation and query budget.
- Determining whether model behavior and system enforcement remain aligned.

## When NOT to Use

- Do not test a public model or production decision service without explicit
  authority and impact limits.
- Do not generate weaponized evasion samples or optimize against protected real
  users, malware, fraud, or safety controls.
- Do not call one label change a system bypass without downstream evidence.

## Preconditions

Require the model or service version, protected decision, input domain,
evaluation identity, approved dataset, permissible transformations,
perturbation metric and ceiling, query and time budgets, target and non-target
success criteria, fallback behavior, monitoring, stop condition, and cleanup.

## Workflow

1. Record the security invariant and full decision path: input acquisition,
   canonicalization, preprocessing, model output, threshold, abstention,
   ensemble or rule logic, fallback, and downstream action.
2. Freeze or record every component version and randomization source. Note any
   remote service whose exact version cannot be established.
3. Build a representative baseline set with labels or expected dispositions,
   protected classes where relevant, and provenance. Separate development,
   calibration, and final evaluation data.
4. Measure baseline confusion, score distribution, threshold behavior,
   abstention, fallback, and downstream enforcement before adversarial cases.
5. Define paired transformations that preserve the test's permitted semantics
   and remain inside the approved budget. Record the exact distance or change
   measure for each pair.
6. Test one transformation family at a time. Avoid public payload recipes; keep
   sensitive samples in restricted artifacts.
7. Capture raw input reference, transformed input reference, preprocessing
   output where observable, model score or label, threshold decision, fallback,
   downstream action, telemetry, timestamp, and run identifier.
8. Distinguish outcomes:
   - `model-shift` — score or label changed;
   - `gate-shift` — the security disposition changed;
   - `system-bypass` — target-origin evidence confirms the prohibited outcome;
   - `inconclusive` — version, preprocessing, nondeterminism, or evidence gaps
     prevent attribution.
9. Measure target success and collateral error across the evaluation set. One
   successful pair is a reproducer, not a robustness rate.
10. Re-test remediation against the held-out set and ordinary inputs. Confirm
    that threshold or preprocessing changes do not merely move the failure.

## Deliverable

Return the decision-path map, frozen context, dataset provenance, baseline
metrics, perturbation contract, paired-case receipts, outcome classification,
target and collateral rates, limitations, stop events, and remediation options.

## Rationalizations to reject

- **“The label changed, so the security control was bypassed.”** Prove the gate
  and downstream disposition separately.
- **“The change looks imperceptible.”** Use the approved domain-specific metric
  and ceiling rather than visual intuition.
- **“One example demonstrates robustness failure rate.”** A reproducer does not
  establish prevalence.
- **“Raising the threshold fixes it.”** Measure false positives, false negatives,
  abstention, and fallback consequences.
- **“The model is the whole control.”** Preprocessing, rules, ensembles, and
  downstream authorization can strengthen or weaken the integrated gate.
- **“More queries only improve confidence.”** Query budgets limit operational
  impact and adaptive overfitting.
