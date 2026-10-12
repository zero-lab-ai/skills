---
name: lateral-movement-map
description: "Maps lateral movement candidates and multi-hop routes across Windows, Linux, network, DevOps, and cloud environments while separating transport reachability, authentication material, destination rights, authorization, execution proof, resulting access, detection exposure, and cleanup. Use when planning or documenting remote access paths after a foothold."
allowed-tools: Read Grep Glob
---

# Lateral movement map

Lateral movement is a chain of claims. A listening service does not prove
reachability. Reachability does not prove authentication. Authentication does
not prove destination rights. A successful hop does not prove the next hop.

This skill maps supplied facts and bounded validation plans. It does not supply
commands, recover or replay secrets, contact systems, create remote processes,
deploy tunnels, establish persistence, or authorize activity.

## When to Use

- Planning or documenting remote access paths after a foothold.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record the objective, assessment window, supplied operational-signal ceiling
   or null, written authorization, permitted sources, destinations, material
   references, and action classes. Preserve explicit prohibitions.
2. Inventory assets and current access contexts. Mark a context `observed` only
   when evidence establishes that identity and privilege on that asset. Projected
   contexts identify the exact prior movement that would create them.
3. Inventory authentication material as references only. Record type, identity,
   state, source, permitted use, limitations, and evidence. Never place a raw
   password, hash, ticket, token, key, or secret in the map.
4. Separate reachability, destination rights, administrative baseline, and
   telemetry health. Each answers a different question and needs its own evidence.
5. Build each candidate hop from one source context to one destination. Link the
   material, transport, required right, authorization, expected defensive
   artifacts, operational signal, stop conditions, and cleanup obligation.
6. Derive hop state. Known deny or prohibition is `blocked`;
   missing prerequisites are `unknown`; complete prerequisites behind a consent
   gate are `approval-required`; authorized complete prerequisites are
   `authorized`. Only execution evidence can produce `executed` or `failed`.
7. Record resulting access narrowly. Planned access is `projected`; achieved
   identity and privilege are `observed` only after cited execution evidence.
8. Assemble ordered routes. The destination of one hop must be the source of the
   next, and the next source context must be derived from the preceding hop.
   Route state is limited by its weakest hop.
9. Select the smallest authorized validation that advances the objective within
   the signal ceiling. Unknown sensor health increases uncertainty; it does not
   make an action quiet.
10. Cover every required planning and evidence category. Record blocked or
    unknown work explicitly, then complete the assessment.

## Boundary with adjacent skills

- Use `active-directory-attack-path` to analyze directory control relationships
  and privilege paths before operational movement.
- Use `privilege-escalation-assessment` for elevation on the current host.
- Use `credential-exposure-audit` to inventory and contain credential material;
  this skill accepts references and allowed-use state only.
- Use `cloud-attack-path` for cloud IAM graph analysis. Record an approved cloud
  transition here only when it participates in the movement campaign.
- Use `covert-channel-assessment` for tunnel or egress feasibility.
- Use `detection-validate` when the purpose is to execute a technique and prove a
  detector, rather than reach an engagement objective.

## Rationalizations to reject

- **"The port is open, so the path works."** Transport says nothing about
  authentication, rights, policy, or resulting privilege.
- **"A hash-shaped value is a credential."** An indicator without usable,
  authorized material cannot support a movement hop.
- **"The account is privileged somewhere, so it is privileged here."** Rights
  are destination and capability specific.
- **"A quieter technique is safe."** Detection depends on the environment's
  baseline, sensors, target sensitivity, and actual implementation.
- **"One successful hop proves the route."** Every hop has separate prerequisites
  and the next hop needs a real or explicitly projected source context.
- **"No alert means no detection."** Without healthy telemetry and a reviewed
  query window, silence is not an outcome.
- **"Planned cleanup is proof of cleanup."** Completion needs evidence tied to
  the state-changing hop.
