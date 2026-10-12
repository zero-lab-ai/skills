---
name: active-directory-attack-path
description: "Analyzes and prioritizes Active Directory and BloodHound attack paths using evidence freshness, disabled principals, prerequisites, authorization, operational noise, and remediation coverage. Use during an authorized red-team operation when reviewing AD graphs, nested groups, ACL abuse, delegation, sessions, GPO control, or routes to Tier Zero."
allowed-tools: Read Grep Glob
---

# Active Directory attack paths

A graph relationship describes possible control. It does not prove current
session state, usable credentials, authorized traversal, or the best route for
an operation. Keep those claims separate.

## When to Use

- An authorized red-team operation when reviewing AD graphs, nested groups, ACL abuse, delegation, sessions, GPO control, or routes to Tier Zero.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Confirm the owned starting principals, high-value objectives, allowed
   evidence reads, allowed traversal actions, and acceptable operational noise.
2. Inventory relevant users, groups, computers, GPOs, domains, and trusts.
   Record whether user and computer accounts are enabled and when volatile
   evidence was collected.
3. Normalize group membership, administrative rights, object-control rights,
   delegation, GPO-derived control, trusts, and session observations as directed
   edges. Resolve nested membership before declaring an effective path.
4. Give every node and edge an evidence reference and disposition. Current LDAP
   or security-descriptor evidence can establish a configuration relationship;
   stale session evidence remains a candidate.
5. Enumerate materially distinct paths from each owned principal to each stated
   objective. Include blocked branches when they explain why a visually
   connected graph is not viable.
6. For every edge, record required actions and operational noise. A structurally
   proven path may still require separate approval for a password reset, host
   access, credential interaction, authentication, ticket request, or state
   change.
7. Add remediations that sever every objective path. Prefer the smallest set of
   relationships or principals that removes the largest amount of reachability.
8. Report graph confidence and execution disposition separately. State that
    coverage applies to the supplied graph, not necessarily the whole domain.

## Path decision table

| Evidence state | Path disposition |
| --- | --- |
| Current configuration evidence, met prerequisites, and every action authorized | Validation candidate; still not achieved access until executed |
| Current configuration evidence but an active transition lacks approval | Structurally proven, approval required |
| Stale session or unverified credential availability | Plausible candidate, not a current path |
| Disabled principal, unmet prerequisite, explicit deny, or prohibited action | Blocked at the named edge |
| Missing graph segment or unknown evidence freshness | Unknown; preserve the gap |

For each objective, report materially distinct paths, the weakest edge in each,
required actions, operational signal, authorization state, and the smallest
remediation set that severs all reported routes.

## Interpretation rules

- A disabled user can retain group membership while blocking a current
  authentication path. Preserve both facts.
- `HasSession` is volatile. Its age, logon type, and credential availability
  determine whether it is evidence or only a lead.
- Object control establishes authority over the object. It does not establish
  that changing the object is authorized or operationally quiet.
- Membership, GPO application, credential access, authentication, and downstream
  impact are separate transitions.
- An edge after the objective may show business impact without belonging to the
  path used to reach that objective.

## Rationalizations to reject

- **"BloodHound drew a line, so the path works."** Graph data can be stale,
  incomplete, or dependent on disabled principals and unmet prerequisites.
- **"The shortest path is the best path."** A short password reset can be more
  disruptive and detectable than a longer read-only validation route.
- **"Membership proves authentication."** Disabled accounts and missing
  credential material can make a valid membership edge operationally useless.
- **"AdminTo proves credentials are available."** Host control and a session
  observation are separate claims; session material may be absent or protected.
- **"Read-only authorization covers harmless validation."** Resets, logons,
  ticket requests, host access, credential interaction, and policy changes are
  active actions regardless of intent.
- **"Fixing the first edge closes the domain."** Every distinct objective path
  needs an explicit severing control and evidence after remediation.
