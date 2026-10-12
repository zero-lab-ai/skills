---
name: ai-threat-model
description: "Builds an evidence-bound AI threat model from partial architecture, trust, identity, data-flow, and control information. Use when scoping an AI assessment, reviewing a design, or prioritizing realistic attack paths under uncertainty."
metadata:
  portability: universal
  discipline: engagement-operations
  domain: ai-systems
  tags: [ai, threat-modeling, architecture, trust-boundaries, risk]
---

# AI threat model

Turn incomplete system knowledge into a decision-ready threat model without
inventing architecture. Preserve uncertainty as a first-class result and update
the model when evidence changes.

## When to Use

- Scoping an AI security review or penetration test.
- Reviewing a design that combines models, retrieval, agents, tools, data, and
  conventional application or cloud services.
- Prioritizing assessment paths when architecture evidence is incomplete or
  contradictory.

## When NOT to Use

- Do not treat the model as permission to validate a threat on a live target.
- Do not use a generic AI risk list in place of the system's actual boundaries.
- Do not assign likelihood or impact precision unsupported by evidence.

## Workflow

1. State the decision the threat model must support, the assessment scope, and
   the evidence cutoff date.
2. Build an assumption register. For every unknown needed to continue, record
   the assumption, why it matters, the evidence that would resolve it, its
   owner, and the consequence if it is false.
3. Identify crown jewels and safety properties. Include sensitive data,
   model behavior, tool authority, workload identity, evaluation integrity,
   deployment artifacts, human approvals, and availability where relevant.
4. Map components and trust zones. Include users, applications, model gateways,
   model providers, retrieval pipelines, agent runtimes, tools, memory,
   registries, CI/CD, monitoring, and administrative planes.
5. Draw data, instruction, identity, and artifact flows separately. A component
   can trust data but not instructions, or accept an artifact without loading it.
6. For each boundary, ask what can cross, who authorizes it, which identity is
   used, what validation occurs, what logs survive, and what downstream
   consumer acts on the result.
7. Construct attack-path hypotheses from evidence-backed transitions. Label
   every step `observed`, `assumed`, `inferred`, or `blocked`; one unknown step
   prevents the full path from being called demonstrated.
8. Evaluate threats across the AI-specific surfaces:
   - instruction and context control;
   - retrieval and knowledge integrity;
   - agent and tool authority;
   - model and artifact supply chain;
   - identity and secret propagation;
   - output consumption and automation;
   - monitoring, evaluation, and human oversight.
9. Prioritize by plausible consequence, exposed preconditions, boundary count,
   control evidence, and uncertainty. Do not multiply arbitrary numbers to
   manufacture precision.
10. Convert priorities into bounded review questions, control gaps, evidence
    requests, and separately authorized validation objectives.
11. Version the model. Record which new evidence confirmed, weakened, blocked,
    or split each path.

## Deliverable

Return a threat-model package containing the system purpose, scope, evidence
cutoff, crown jewels, component and trust-zone map, separated flow maps,
assumption register, attack-path hypotheses, control observations, prioritized
review questions, and change log.

## Rationalizations to reject

- **“This is a standard RAG architecture.”** Shared labels do not prove shared
  trust boundaries or controls.
- **“The diagram is authoritative because the client supplied it.”** Supplied
  architecture is reported evidence and may be stale.
- **“An assumed step is probably true, so the path is complete.”** A path is no
  stronger than its weakest unsupported transition.
- **“Map every framework technique.”** Exhaustive taxonomy mapping can obscure
  the system-specific decisions the model exists to support.
- **“A low likelihood makes the control gap unimportant.”** Weak evidence for
  likelihood should remain uncertainty, not become a reassuring score.
- **“The model is finished once the diagram is drawn.”** A threat model is a
  versioned decision artifact, not a static picture.
