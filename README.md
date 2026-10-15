# zero-lab skills

Portable, evidence-bound security skills for authorized defensive assessment,
penetration testing, red teaming, detection engineering, purple teaming, and
engagement operations.

The collection contains **56 skills in 10 installable plugins** from
[zero-lab.ai](https://zero-lab.ai). Install a coherent bundle, or copy an
individual skill folder into any agent harness that reads `SKILL.md`.

> [!IMPORTANT]
> These skills support authorized security work. They do not grant permission,
> expand scope, or replace an organization's rules of engagement. Skills that
> touch adversary behavior are designed to measure exposure, preserve evidence,
> and hand results back to defenders.

## Contents

- [Install](#install)
- [Bundles](#bundles)
- [Skill index](#skill-index)
- [Compatibility](#compatibility)
- [Trust and safety](#trust-and-safety)
- [Repository structure](#repository-structure)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [Security](#security)
- [License](#license)

## Install

### Claude Code

```text
/plugin marketplace add zero-lab-ai/skills
/plugin menu
```

Select the bundle you need from the marketplace menu.

### Codex

Codex reads the same marketplace metadata directly:

```sh
codex plugin marketplace add zero-lab-ai/skills
codex plugin list
codex plugin add <bundle-name>@zero-lab
```

### ChatGPT Workspace Marketplace

Use this repository's `.claude-plugin/marketplace.json` for workspace imports.
Each skill includes `agents/openai.yaml` with its display name, description,
Zero Lab mark, and brand color.

### Other agent harnesses

Install the cross-agent skills tree:

```sh
npx skills add zero-lab-ai/skills
```

You can also copy a single
`plugins/<bundle>/skills/<skill>/` directory into the location your harness
scans. Nothing outside that skill directory is required at runtime.

## Bundles

| Plugin | Skills | Purpose |
| --- | ---: | --- |
| [`agent-security`](plugins/agent-security) | 4 | Agent surfaces, prompt injection, runtime validation, and trust boundaries |
| [`recon-operations`](plugins/recon-operations) | 9 | Network, public-exposure, human, physical, and AI-system reconnaissance |
| [`identity-security`](plugins/identity-security) | 8 | Directory, credential, privilege, and lateral-movement security |
| [`application-endpoint-security`](plugins/application-endpoint-security) | 6 | Cloud, web, mobile, firmware, endpoint, and password assessment coverage |
| [`network-protocol-security`](plugins/network-protocol-security) | 5 | Wireless, traffic, protocol, command-channel, and egress security |
| [`binary-forensics`](plugins/binary-forensics) | 4 | Binary-fault, memory, and rootkit triage |
| [`detection-validation`](plugins/detection-validation) | 6 | Detection engineering, validation, telemetry, resilience, and control evidence |
| [`engagement-operations`](plugins/engagement-operations) | 7 | Planning, AI threat modeling, evidence proof, findings, and report assembly |
| [`rag-security`](plugins/rag-security) | 3 | Retrieval-surface, integrity, tenant, data-exposure, and cleanup assessment |
| [`ml-system-security`](plugins/ml-system-security) | 4 | Model artifacts, decision boundaries, datasets, and serving exposure |

## Skill index

### Agent and AI systems

Install [`agent-security`](plugins/agent-security).

| Skill | Use it when… |
| --- | --- |
| [`agent-surface-audit`](plugins/agent-security/skills/agent-surface-audit) | Reviewing agent tools for poisoning, excess privilege, unsafe parameters, and deployment blast radius |
| [`agent-runtime-validation`](plugins/agent-security/skills/agent-runtime-validation) | Validating deployed tools, memory, hooks, approvals, identities, and scope controls with benign sentinels |
| [`prompt-injection-assessment`](plugins/agent-security/skills/prompt-injection-assessment) | Assessing instruction influence and policy bypass across direct, indirect, retrieval, and tool-output channels |
| [`agent-trust-boundary-audit`](plugins/agent-security/skills/agent-trust-boundary-audit) | Auditing authentication, authorization, delegated authority, and effect across agent handoffs |

### Reconnaissance and exposure mapping

Install [`recon-operations`](plugins/recon-operations).

| Skill | Use it when… |
| --- | --- |
| [`network-recon`](plugins/recon-operations/skills/network-recon) | Enforcing IP scope, planning reconnaissance, or auditing scan coverage |
| [`osint-scanner`](plugins/recon-operations/skills/osint-scanner) | Mapping public exposure from third-party data without contacting the target |
| [`social-engineering-recon`](plugins/recon-operations/skills/social-engineering-recon) | Mapping passive, privacy-preserving human-layer exposure |
| [`physical-recon`](plugins/recon-operations/skills/physical-recon) | Assessing supplied public-vantage physical-security observations |
| [`target-profile-synthesis`](plugins/recon-operations/skills/target-profile-synthesis) | Joining validated cross-domain evidence into exposure themes and priorities |
| [`situational-awareness`](plugins/recon-operations/skills/situational-awareness) | Assessing a foothold without exceeding an operation's noise budget |
| [`opsec-planning`](plugins/recon-operations/skills/opsec-planning) | Connecting objectives to artifacts, detection risk, abort conditions, and cleanup |
| [`recon-automation-governance`](plugins/recon-operations/skills/recon-automation-governance) | Governing jobs, budgets, retries, stop controls, and evidence custody |
| [`ai-surface-recon`](plugins/recon-operations/skills/ai-surface-recon) | Mapping models, retrieval paths, agents, tools, guardrails, endpoints, and privileged consumers |

### Retrieval-augmented AI security

Install [`rag-security`](plugins/rag-security).

| Skill | Use it when… |
| --- | --- |
| [`retrieval-integrity-assessment`](plugins/rag-security/skills/retrieval-integrity-assessment) | Assessing source, tenant, retrieval, context, citation, output, and cleanup integrity with benign canaries |
| [`rag-surface-recon`](plugins/rag-security/skills/rag-surface-recon) | Mapping RAG sources, connectors, indexes, filters, ranking, caches, citations, and exposed fields |
| [`rag-data-exposure-audit`](plugins/rag-security/skills/rag-data-exposure-audit) | Measuring tenant and authorization boundaries with controlled fixtures and explicit exposure states |

### Model and ML system security

Install [`ml-system-security`](plugins/ml-system-security).

| Skill | Use it when… |
| --- | --- |
| [`model-artifact-lifecycle-audit`](plugins/ml-system-security/skills/model-artifact-lifecycle-audit) | Auditing model artifacts from intake through loading, execution, revocation, and retirement |
| [`ml-decision-boundary-assessment`](plugins/ml-system-security/skills/ml-decision-boundary-assessment) | Testing whether model-output changes alter downstream security decisions or protected effects |
| [`dataset-integrity-assessment`](plugins/ml-system-security/skills/dataset-integrity-assessment) | Auditing dataset sources, transformations, review, lineage, retraining, and rollback evidence |
| [`model-serving-exposure-audit`](plugins/ml-system-security/skills/model-serving-exposure-audit) | Auditing model-serving APIs, identities, administrative surfaces, data stores, and access evidence |

### Identity and directory security

Install [`identity-security`](plugins/identity-security).

| Skill | Use it when… |
| --- | --- |
| [`active-directory-attack-path`](plugins/identity-security/skills/active-directory-attack-path) | Analyzing evidence-backed AD paths while separating reachability from authorized traversal |
| [`adcs-exposure-audit`](plugins/identity-security/skills/adcs-exposure-audit) | Auditing certificate templates, CA policy, PKI ACLs, enrollment, and mapping controls |
| [`kerberos-exposure-audit`](plugins/identity-security/skills/kerberos-exposure-audit) | Auditing sanitized Kerberos policy, protection, monitoring, and evidence controls |
| [`directory-persistence-audit`](plugins/identity-security/skills/directory-persistence-audit) | Auditing directory-service governance for durable-control exposure |
| [`credential-exposure-audit`](plugins/identity-security/skills/credential-exposure-audit) | Auditing supplied credential evidence without using the credential material |
| [`privilege-escalation-assessment`](plugins/identity-security/skills/privilege-escalation-assessment) | Ranking Windows, Linux, or cloud elevation paths without overstating achieved privilege |
| [`lateral-movement-map`](plugins/identity-security/skills/lateral-movement-map) | Mapping movement routes without confusing transport reachability with access |
| [`lateral-movement-readiness`](plugins/identity-security/skills/lateral-movement-readiness) | Reviewing movement candidates before a separate validation handoff |

### Application, cloud, and endpoint assessment

Install [`application-endpoint-security`](plugins/application-endpoint-security).

| Skill | Use it when… |
| --- | --- |
| [`cloud-attack-path`](plugins/application-endpoint-security/skills/cloud-attack-path) | Mapping cloud identity, workload, credential, and trust transitions |
| [`web-assessment-coverage`](plugins/application-endpoint-security/skills/web-assessment-coverage) | Tracking application surfaces, roles, and test-family coverage |
| [`mobile-application-assessment`](plugins/application-endpoint-security/skills/mobile-application-assessment) | Tracking evidence-backed Android and iOS assessment coverage |
| [`firmware-hardware-assessment`](plugins/application-endpoint-security/skills/firmware-hardware-assessment) | Assessing device identity, firmware acquisition, update trust, and physical safety |
| [`persistence-surface-assessment`](plugins/application-endpoint-security/skills/persistence-surface-assessment) | Measuring Windows and Linux persistence exposure from supplied evidence |
| [`password-audit-plan`](plugins/application-endpoint-security/skills/password-audit-plan) | Planning bounded offline password audits and restricted result handling |

### Network, protocol, and channel security

Install [`network-protocol-security`](plugins/network-protocol-security).

| Skill | Use it when… |
| --- | --- |
| [`wireless-assessment-plan`](plugins/network-protocol-security/skills/wireless-assessment-plan) | Planning authorized Wi-Fi, Bluetooth, RFID/NFC, SDR, or other radio testing |
| [`protocol-traffic-analysis`](plugins/network-protocol-security/skills/protocol-traffic-analysis) | Turning supplied captures into evidence-bound conversations and limitations |
| [`protocol-exploitation-assessment`](plugins/network-protocol-security/skills/protocol-exploitation-assessment) | Assessing protocol candidates without promoting weak signals into proven vulnerabilities |
| [`covert-channel-assessment`](plugins/network-protocol-security/skills/covert-channel-assessment) | Measuring whether bounded synthetic channels are blocked, visible, detected, and cleaned up |
| [`command-channel-defense-assessment`](plugins/network-protocol-security/skills/command-channel-defense-assessment) | Measuring defensive coverage against opaque command-channel scenarios |

### Binary and forensic analysis

Install [`binary-forensics`](plugins/binary-forensics).

| Skill | Use it when… |
| --- | --- |
| [`binary-fault-triage`](plugins/binary-forensics/skills/binary-fault-triage) | Triaging supplied binary fault evidence without execution or weaponization |
| [`binary-fault-validation-readiness`](plugins/binary-forensics/skills/binary-fault-validation-readiness) | Checking whether fault evidence is ready for separate isolated validation |
| [`memory-forensics-triage`](plugins/binary-forensics/skills/memory-forensics-triage) | Triaging supplied volatile-memory images while preserving evidentiary limits |
| [`rootkit-triage`](plugins/binary-forensics/skills/rootkit-triage) | Triaging suspected rootkits or bootkits with independent evidence views |

### Detection and purple-team validation

Install [`detection-validation`](plugins/detection-validation).

| Skill | Use it when… |
| --- | --- |
| [`detection-engineering`](plugins/detection-validation/skills/detection-engineering) | Building rules proven against known-bad and known-good cases |
| [`detection-validate`](plugins/detection-validation/skills/detection-validate) | Running an authorized technique and confirming whether its detection fires |
| [`detection-resilience-test-plan`](plugins/detection-validation/skills/detection-resilience-test-plan) | Planning bounded resilience tests using pre-approved opaque fixtures |
| [`telemetry-coverage-audit`](plugins/detection-validation/skills/telemetry-coverage-audit) | Auditing passive coverage, retention, custody, and investigation readiness |
| [`incident-validation-correlation`](plugins/detection-validation/skills/incident-validation-correlation) | Correlating incident observations with separate isolated validation receipts |
| [`defensive-control-evidence-synthesis`](plugins/detection-validation/skills/defensive-control-evidence-synthesis) | Consolidating assessments into a lineage-preserving control matrix |

### Engagement planning, governance, and reporting

Install [`engagement-operations`](plugins/engagement-operations).

| Skill | Use it when… |
| --- | --- |
| [`findings-report`](plugins/engagement-operations/skills/findings-report) | Writing reproducible, severity-justified, evidence-bound findings |
| [`social-engineering-engagement-plan`](plugins/engagement-operations/skills/social-engineering-engagement-plan) | Planning authorized human-security exercises with participant safeguards |
| [`security-test-tool-governance`](plugins/engagement-operations/skills/security-test-tool-governance) | Reviewing supplied security-test artifacts before controlled lab handoff |
| [`assessment-sequence-governance`](plugins/engagement-operations/skills/assessment-sequence-governance) | Checking a supplied assessment sequence's ordering, authority, and safeguards |
| [`engagement-report-assembly`](plugins/engagement-operations/skills/engagement-report-assembly) | Assembling validated artifacts without rewriting source findings |
| [`ai-threat-model`](plugins/engagement-operations/skills/ai-threat-model) | Modeling AI architecture, trust boundaries, assumptions, and attack-path hypotheses |
| [`agent-action-proof`](plugins/engagement-operations/skills/agent-action-proof) | Grading what agent callbacks, tool traces, target receipts, and state changes actually prove |

## Compatibility

The repository uses the standard Claude marketplace layout also supported by
Codex. Each skill includes `agents/openai.yaml` for ChatGPT presentation and
keeps its core instructions in `SKILL.md`. References, scripts, assets, tests,
and evaluations are included only when the capability needs them.

Installing a plugin provides every skill in that bundle. Copying one skill
folder provides only that portable capability.

## Trust and safety

Agent skills are executable instructions. Review them with the same care as
code before giving an agent access to sensitive systems.

This repository's release gate checks that:

- every plugin is registered and its metadata agrees across manifests;
- skill frontmatter and UI metadata are complete;
- local paths and references resolve cleanly;
- security skills reject common rationalizations that cause missed findings;
- shell and Python helpers pass linting; and
- every discovered test suite passes through `make check`.

Scripts perform deterministic work only where the task benefits from it. Their
output does not authenticate evidence, authorize testing, or prove that a
target is secure.

## Repository structure

```text
plugins/<bundle>/
├── .claude-plugin/plugin.json   # installable bundle metadata
├── README.md                    # bundle overview and skill index
├── skills/
│   └── <skill>/
│       ├── SKILL.md             # independently portable entry point
│       ├── agents/openai.yaml   # ChatGPT presentation metadata
│       ├── assets/              # skill-local brand or deliverable assets
│       ├── references/          # optional supporting guidance
│       └── scripts/             # optional reusable tooling
├── tests/                       # optional deterministic code tests
└── evals/                       # optional behavioral model evaluations
```

The root [marketplace manifest](.claude-plugin/marketplace.json) registers the
ten installable bundles. A plugin README describes the bundle; each skill's
frontmatter controls when that capability activates.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for the
submission workflow and authoring contract. Start new work from
[`templates/plugin-template/`](templates/plugin-template/) and run:

```sh
make check
```

The same validator and plugin suites run in CI.

## Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for project attribution.

## Security

Report vulnerabilities privately to
[contact@zero-lab.ai](mailto:contact@zero-lab.ai). Do not open a public issue
for a vulnerability in a shipped skill or script. See
[SECURITY.md](SECURITY.md) for the review and reporting policy.

## License

Licensed under [Apache-2.0](LICENSE).
