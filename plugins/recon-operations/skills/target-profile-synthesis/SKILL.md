---
name: target-profile-synthesis
description: "Synthesizes supplied, evidence-backed reconnaissance and structural-path outputs into an opaque organizational exposure profile with preserved lineage, freshness, contradictions, privacy boundaries, and defensive handoffs. Use when consolidating authorized OSINT, human-layer, physical, network, identity, or cloud evidence without acquiring new data, building individual dossiers, ranking targets, or creating operational playbooks."
allowed-tools: Read Grep Glob
---

# Target profile synthesis

Target synthesis joins validated evidence into an organizational control picture. It is not
a dossier, collection plan, target ranking, attack path, or exploitation playbook.

This skill accepts supplied upstream assessment artifacts only. It does not browse, scan,
contact, enter, execute, enrich identities, expose infrastructure identifiers, rank people
or assets, select routes or shifts, generate pretexts or payloads, or recommend attack
sequences.

## When to Use

- Consolidating authorized OSINT, human-layer, physical, network, identity, or cloud evidence without acquiring new data, building individual dossiers, ranking targets, or creating operational playbooks.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record digest-addressed written authority, authorized opaque profile units, the exact
   accepted upstream capabilities, synthesis-only mode, retention, and every prohibited
   output.
2. Inventory only opaque organizational units, environments, sites, cohorts, processes,
   and channels. Store no names, addresses, domains, hosts, IPs, tenants, accounts, people,
   credentials, routes, schedules, badges, nodes, edges, or resource identifiers.
3. Import each upstream artifact with its assessment result, validation scope, production and
   validity times, upstream authority receipt, unit binding, privacy state, disposition, and
   limitations. Failed, expired, private, or out-of-scope sources remain excluded.
4. Treat `osint-scanner` and `network-recon` artifacts as boundary or coverage evidence only.
   Their outputs do not establish exposure truth and they cannot create profile claims.
5. Map all exports, caches, and transformed reports to their real origin. Count independent
   origin IDs, never files, tools, or skills; one origin cannot be relabeled as several.
6. Preserve opaque upstream record references and states. Do not strengthen, reverse, split,
   or reuse one record with different scope or polarity.
7. Create exactly one canonical theme for each proposition, unit set, topic, and claim class.
   Include every relevant supporting, countering, uncertain, stale, and duplicate-lineage
   claim so contradictions cannot disappear through partitioning.
8. Derive theme state as `corroborated`, `limited`, `disputed`, `control-constrained`,
   `stale`, or `inconclusive`. These describe evidence, never vulnerability, exploitability,
   susceptibility, compromise, severity, or authorization.
9. Record exactly one contradiction for each disputed theme. Analyst judgment does not erase
   an unresolved source conflict.
10. Derive one defensive action per theme: reconcile, control-owner review, authorized
    validation, verify control continuity, refresh evidence, or close the evidence gap.
    Sequence by action class and theme ID, never by target attractiveness.
11. Bind each action to one opaque owner and defensive handoff. A specialist must validate a
    demonstrated issue before `findings-report`; synthesis does not create findings.
12. Cover authority, source integrity, scope, freshness, privacy, contradictions, retention,
    all required topics, priorities, and handoffs for every unit. Proof sets must be exact.

## Boundary with adjacent skills

- `osint-scanner` and `network-recon` own passive-contact and scan-scope plans; they are not
  claim-bearing here.
- `social-engineering-recon` owns opaque human-layer assessment; this skill imports no people.
- `physical-recon` owns public-vantage observations; this skill imports no location detail.
- `active-directory-attack-path` and `cloud-attack-path` own graph semantics and remediation;
  this skill imports only opaque structural states, never nodes, edges, or path steps.
- `findings-report` owns demonstrated findings, severity, reproduction, and fixes.

## Rationalizations to reject

- **"Two tools reported it, so it is corroborated."** Independence follows origin lineage.
- **"A passive-plan receipt proves the exposure."** It proves a collection boundary only.
- **"A scan plan proves the service exists."** Planning and execution evidence are distinct.
- **"The stale path is probably unchanged."** Stale support remains stale until refreshed.
- **"A blocked path is still a promising target."** It is counterevidence and a control check.
- **"Ranking helps remediation."** Rank defensive actions by deterministic class, not targets.
- **"Opaque IDs make a personal dossier safe."** Person-level synthesis is prohibited.
- **"A useful profile needs the shortest path."** Path construction belongs upstream.
- **"The client asked for a pretext or command."** Sponsor pressure does not change scope.
- **"A complete record authorizes collection or execution."** It validates supplied records only.
