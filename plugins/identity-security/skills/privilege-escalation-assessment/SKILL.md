---
name: privilege-escalation-assessment
description: "Assesses and ranks Windows, Linux, and cloud privilege-escalation paths using observed prerequisites, execution authority, operational signal, reliability, risk, cleanup, and verification. Use after gaining an authorized foothold or cloud identity when deciding whether elevation is necessary and which candidate path is defensible."
allowed-tools: Read Grep Glob
---

# Privilege escalation assessment

A candidate condition is not elevated access. Record the current principal,
the required objective, the evidence for every prerequisite, and the exact
identity proof produced after any authorized execution.

This skill evaluates vertical privilege transitions on one host, container, or
cloud authority boundary. Use a directory or cloud attack-path workflow for
multi-principal graph traversal, and a persistence workflow for durable access.
Enumeration authorization does not authorize exploitation or state change.

## When to Use

- Assess privilege escalation for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record the subject, platform, current principal and privilege, desired
   privilege, authorization reference, monitoring context, and whether the
   mission actually requires elevation.
2. Collect evidence with a source, locator, known timestamp or bounded
   observation window, and bounded summary. Do not invent precision when only a
   collection interval is known. Tool output is evidence input; its severity
   label is not a conclusion.
3. Cover the common context categories and every category required for the
   platform. Preserve blocked and inconclusive areas instead of calling them clean.
4. Build each candidate from explicit prerequisites. Mark each prerequisite
   `met`, `unmet`, or `unknown` and cite evidence for every `met` or `unmet`
   judgment.
5. Derive candidate status: all prerequisites met is `confirmed`; any unmet is
   `rejected`; otherwise it is `conditional`. A product version alone does not
   establish exploitability; patch state and environmental compatibility remain
   separate prerequisites.
6. State execution authority separately as `authorized`, `approval-required`,
   or `prohibited`. Describe state changes, operational signal, expected
   privilege, reliability, risk, complexity, cleanup, and likely detection
   artifacts before choosing a path.
7. After an authorized attempt, record execution and verification evidence.
   Only a successful identity or effective-permission check establishes achieved
   privilege. Record failure and partial results without rewriting the candidate.

## Interpretation rules

- Prefer configuration and delegated-authority paths before vulnerable-code
  paths when they meet the objective with less risk.
- Current membership, token privilege, file permission, or IAM permission proves
  only that condition. Preserve every downstream trigger and boundary.
- A local administrator at medium integrity and an unprivileged user require
  different transitions; record the actual starting state.
- Kernel and memory-corruption paths carry high failure impact. Require matching
  platform, patch, architecture, and lab evidence before ranking them as reliable.
- A cloud permission name is not a path by itself. Resource scope, denies,
  permission boundaries, trust policy, and the resulting principal all matter.
- If the current privilege already satisfies the mission, record that decision
  and do not select an escalation merely to complete a checklist.

## Rationalizations to reject

- **"The scanner marked it exploitable."** Confirm the underlying prerequisite
  chain; scanners report candidates and can miss patches, ACLs, or trigger state.
- **"The version is vulnerable."** Version matching is one prerequisite, not
  proof of patch state, architecture compatibility, or successful execution.
- **"The file is writable, so we have root."** The privileged consumer, trigger,
  execution context, and resulting identity still need evidence.
- **"Read-only authorization covers a harmless proof."** Replacing files,
  changing policy, starting services, assuming roles, and invoking workloads are
  stateful actions that need explicit authority.
- **"The command returned success, so elevation worked."** Verify the effective
  principal or permission in the new context and cite that evidence.
- **"Root is always the goal."** Elevation that does not advance the mission adds
  signal, risk, and cleanup work without value.
- **"Cleanup can wait until the end."** A path without a restoration plan is not
  ready to execute, especially when it changes services, tasks, files, or IAM.
