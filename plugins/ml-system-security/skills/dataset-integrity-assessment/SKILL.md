---
name: dataset-integrity-assessment
description: "Audits dataset sources, labels, transformations, review, versioning, split integrity, retraining triggers, and rollback controls for poisoning and targeted degradation risk. Use when reviewing an ML training or evaluation data supply chain."
metadata:
  portability: universal
  discipline: blue-team
  domain: ai-systems
  tags: [datasets, poisoning, provenance, labels, mlops]
---

# Dataset integrity assessment

Trace data from origin to trained or evaluated model. Determine where untrusted
content, labels, transformations, or review decisions can change the dataset and
whether lineage supports detection, rollback, and impact analysis.

## When to Use

- Reviewing training, fine-tuning, preference, retrieval, calibration, or
  evaluation datasets.
- Investigating suspected poisoning, label manipulation, split contamination,
  or targeted degradation.
- Assessing whether a retraining pipeline can identify and remove affected data.

## When NOT to Use

- Do not create poisoned datasets, harmful examples, or trigger-bearing model
  artifacts as part of this audit.
- Do not infer integrity from storage immutability alone.
- Do not call a suspicious record malicious without provenance, behavior, or
  corroborating evidence.

## Workflow

1. Define dataset purpose, owners, model consumers, protected behaviors, versions,
   environments, evidence window, and regulatory or contractual constraints.
2. Inventory every source and contribution path: internal systems, vendors,
   public corpora, user feedback, synthetic generation, human labeling,
   telemetry, merges, and derived datasets.
3. Map the lifecycle: collection, consent and licensing, validation, parsing,
   normalization, filtering, deduplication, labeling, review, augmentation,
   split assignment, packaging, storage, approval, training, evaluation,
   retention, revocation, and deletion.
4. Record identity and authority at each mutation point. Include automated jobs,
   maintainers, vendors, reviewers, service accounts, and emergency overrides.
5. Trace lineage using source identifiers, immutable versions, record or shard
   digests, transformation versions, label history, reviewer decisions, and
   parent-child dataset relationships.
6. Review integrity controls:
   - schema and content validation;
   - source reputation and contribution limits;
   - label agreement, adjudication, and reviewer independence;
   - duplicate, near-duplicate, and outlier handling;
   - class, cohort, language, and source distribution monitoring;
   - split isolation and benchmark contamination controls;
   - approval, signing, access control, and immutable release records.
7. Identify poisoning opportunities as conditional paths from a contributor or
   compromised job to a protected behavior. Keep insertion capability, survival
   through transformations, training influence, and model effect separate.
8. Review retraining triggers and automation. Determine whether one untrusted
   signal can cause collection, relabeling, promotion, or deployment without
   independent review.
9. Test incident readiness from supplied evidence: locate affected versions,
   consumers, training runs, models, evaluations, and deployments; then assess
   whether exclusion and rollback are reproducible.
10. Report unknown lineage and unmeasured distributions as gaps, not clean data.

## Deliverable

Return the source inventory, lifecycle and authority map, lineage coverage,
control matrix, conditional poisoning paths, review and retraining findings,
split-integrity observations, blast-radius map, rollback readiness, and owned
remediation priorities.

## Rationalizations to reject

- **“The bucket is immutable, so the dataset is trustworthy.”** Immutability
  preserves whatever was written, including poisoned or mislabeled content.
- **“The vendor cleaned it.”** Require source, method, version, and validation
  evidence for the delivered data.
- **“A small number of records cannot matter.”** Targeted subsets and repeated
  retraining can create disproportionate effects.
- **“Human review guarantees integrity.”** Reviewers need identity, guidance,
  independence, quality measurement, and tamper-evident decisions.
- **“The test split is separate.”** Trace derivation, near-duplicates, and
  benchmark leakage rather than trusting folder names.
- **“We can retrain if needed.”** Recovery requires exact affected versions,
  exclusion, reproducible transforms, evaluation, and deployment rollback.
