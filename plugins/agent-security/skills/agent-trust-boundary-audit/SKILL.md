---
name: agent-trust-boundary-audit
description: "Maps identity, authority, instruction, data, memory, and approval propagation across agents and agent-to-agent handoffs. Use when reviewing multi-agent systems, orchestrators, delegated tools, or confused-deputy exposure."
metadata:
  portability: universal
  discipline: blue-team
  domain: ai-systems
  tags: [agents, a2a, trust-boundaries, identity, confused-deputy]
---

# Agent trust boundary audit

Map how authority actually crosses an agent system. Keep communication,
authentication, authorization, delegation, and downstream effect distinct; a
message path alone does not establish permission to act.

## When to Use

- Reviewing multi-agent, orchestrated, delegated-tool, or agent-to-agent
  architectures.
- Investigating confused-deputy, identity propagation, approval, memory, or
  handoff-validation concerns.
- Establishing which component can cause which other component to act and under
  whose identity.

## When NOT to Use

- Do not treat the audit as authority to exercise a handoff or invoke a tool.
- Do not infer effective permissions from component names, intended roles, or a
  protocol's default security model.
- Do not collapse all agents into one trust zone merely because they share an
  orchestrator or model provider.

## Workflow

1. Define the reviewed system, environments, tenants, versions, evidence cutoff,
   owners, and intended security properties.
2. Inventory principals and components: humans, service identities, agents,
   orchestrators, models, brokers, tools, memories, queues, approval services,
   policy engines, targets, and administrative planes.
3. Record each component's authentication method, effective identity, privilege,
   tenant context, reachable resources, secret access, and policy source.
4. Map five edge types separately:
   - data transfer;
   - instruction transfer;
   - identity or token transfer;
   - delegated authority;
   - result or state transfer.
5. For every handoff, record sender, receiver, message type, provenance,
   integrity, freshness, audience binding, replay protection, target binding,
   approval binding, and failure behavior.
6. Trace authority end to end. Identify where a low-authority principal can
   shape inputs consumed by a higher-authority component, even when no
   credential crosses the boundary.
7. Review confused-deputy conditions: mismatched requester and execution
   identity, ambient authority, incomplete target binding, untrusted arguments,
   result reuse, and approval detached from final action.
8. Review memory and state boundaries: writer, reader, tenant, lifetime,
   revocation, provenance, conflict handling, and stale-state invalidation.
9. Label every edge `observed`, `reported`, `inferred`, `contradicted`, or
   `unknown`. Preserve the exact evidence supporting effective authority.
10. Build abuse-path hypotheses without exercising them. A path remains
    conditional when any identity, authority, policy, or target transition is
    unproven.
11. Prioritize choke points where one control limits multiple paths: scoped
    identity, explicit delegation, exact approval binding, provenance checks,
    tenant isolation, revocation, and target-side authorization.

## Boundary with adjacent skills

- Use `agent-surface-audit` for individual tool definitions and parameter risk.
- Use `agent-runtime-validation` to exercise authorized runtime controls.
- Use `ai-threat-model` for the broader system threat model and crown jewels.

## Deliverable

Return the component and principal inventory, typed trust-edge map, effective
authority matrix, handoff-control table, confused-deputy hypotheses, memory and
tenant findings, evidence gaps, and prioritized control choke points.

## Rationalizations to reject

- **“The agents are internal, so the handoff is trusted.”** Internal components
  can have different identities, tenants, policies, and compromise assumptions.
- **“The protocol authenticates both sides.”** Authentication does not prove
  authorization for the requested target or action.
- **“The approval happened in the workflow.”** Verify that it binds the final
  arguments, identity, target, and time.
- **“No credential is forwarded, so authority does not propagate.”** A deputy
  can act with ambient authority on attacker-shaped input.
- **“Shared memory is just context.”** Persistent context is a cross-task data
  and instruction boundary.
- **“The diagram shows the intended path.”** Intended architecture is reported
  evidence until deployment facts confirm it.
