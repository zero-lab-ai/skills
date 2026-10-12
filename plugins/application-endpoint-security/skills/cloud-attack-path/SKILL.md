---
name: cloud-attack-path
description: "Maps cloud identity and authorization paths across AWS, Azure, GCP, and hybrid trust boundaries, separating proven access from plausible and blocked routes. Use during an authorized cloud penetration test when tracing how a starting identity could assume roles, use credentials, execute workloads, cross providers, or reach sensitive data."
allowed-tools: Read Grep Glob
---

# Cloud attack paths

Cloud attack paths are identity graphs. A principal reaches an objective through
permissions, credentials, workload identities, federation, and resource policy.
An allow statement is one input to that graph, not proof that the edge works.

Use this skill only inside written authorization. Mapping a possible path does
not authorize credential retrieval, role assumption, deployment, data access,
or any other validation action.

## When to Use

- An authorized cloud penetration test when tracing how a starting identity could assume roles, use credentials, execute workloads, cross providers, or reach sensitive data.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Build the map

1. **Define the endpoints.** State the starting identity, target resource or
   data, the cloud boundaries in scope, and the smallest proof the engagement
   requires.
2. **Record evidence before conclusions.** Classify each source as observed,
   reported current, reported stale, or inferred. Names such as
   `prod-admin-key` suggest provenance; they do not establish it.
3. **Normalize the graph.** Represent identities, credentials, services,
   resources, and data as nodes. Represent authorization, impersonation,
   credential material, federation, workload execution, and resource access as
   directed edges.
4. **Resolve effective access.** Account for identity and resource policies,
   explicit denies, conditions, permission boundaries, session restrictions,
   organization policy, encryption controls, service enablement, and network or
   perimeter controls that apply. Keep unresolved layers visible.
5. **Classify every edge.** Use:
   - `validated` when current evidence establishes the transition;
   - `candidate` when the transition is plausible but has unverified facts;
   - `blocked` when a known control prevents it;
   - `unknown` when available evidence cannot support a direction.
6. **Make boundary crossings explicit.** For every account, tenant, project,
   provider, or on-premises crossing, name the trust mechanism and its evidence.
   Credential files, federation, and workload identity are separate transitions.
7. **Assemble continuous paths.** Each edge must begin where the previous edge
   ended. Include blocked branches because they explain why apparent privilege
   does not produce a route.
8. **Plan minimum validation.** Prefer metadata and policy reads. Classify each
   validation step and compare it with written authorization. Mark credential
   reads, content access, active execution, and state changes as requiring
   separate approval when they are not already allowed.
9. **State only what the path proves.** A path is:
   - `proven` only when every edge is validated;
   - `plausible` when at least one edge is a candidate and none is blocked or unknown;
   - `blocked` when any edge is blocked;
   - `unknown` when uncertainty prevents a stronger result.

## Provider semantics to preserve

- **AWS:** an identity allow may still lose to an SCP, permissions boundary,
  session policy, resource policy, KMS policy, condition, or explicit deny.
  `PassRole` needs a permitted service action that can consume the role.
- **Azure:** distinguish Entra directory roles from Azure resource RBAC. Resolve
  assignment scope, deny assignments, managed identities, vault mode, and
  conditional access or network restrictions relevant to the transition.
- **GCP:** `serviceAccounts.actAs` lets a workload run as a service account; it
  does not itself mint a token. Resolve allow and deny policies, conditions,
  service enablement, service agents, and perimeter controls.
- **Hybrid and multi-cloud:** treat a credential or assertion as one node and
  the identity it may represent as another. The mapping between them needs its
  own evidence.

## Judgment calls

The script cannot interpret live provider policy or determine whether a
counterfactual deployment would succeed. It verifies the normalized record:
references, continuity, evidence strength, boundary declarations, deny
precedence, authorization classes, and claim strength. A clean result means the
assessment is honest about its inputs, not that the attack path is executable.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "The policy says Allow, so the edge is proven." | Effective access is the result of every applicable policy and condition. Record unresolved layers. |
| "The secret name tells us which identity it belongs to." | A name is inferred provenance. Use a key ID, application ID, deployment record, or other non-secret evidence. |
| "PassRole means I can become that role." | It only matters with an allowed service action that accepts the role. |
| "actAs is direct impersonation." | GCP workload attachment and token creation are different permissions. |
| "We can deploy a harmless function to verify it." | Deployment changes state and creates telemetry. Authorization decides whether it is permitted. |
| "The final object permission proves the whole chain." | Every preceding identity and trust transition must also hold. |
| "the record is complete, so the path works." | It passed structural and evidentiary checks over supplied facts. Provider behavior still requires authorized validation. |
