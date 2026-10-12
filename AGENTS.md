# Authoring plugins and skills

This repository follows the same marketplace conventions used by established
Claude Code and Codex plugin repositories. Familiarity is a feature: someone
who already uses another skills marketplace should not need to learn a Zero Lab
runtime, vocabulary, or packaging model.

## Repository layout

```text
plugins/
  <plugin-name>/
    .claude-plugin/
      plugin.json
    skills/
      <skill-name>/
        SKILL.md
        agents/
          openai.yaml
        references/        # optional
        scripts/           # optional
        assets/            # optional
    commands/              # optional
    agents/                # optional
    hooks/                 # optional
    workflows/             # optional dynamic workflows
    evals/                 # optional behavioral evaluations
    tests/                 # optional code tests
    README.md
```

Only create component and resource directories that the plugin uses. Plugins
may contain one skill, several related skills, or another supported marketplace
component such as a command or workflow.

Keep plugin components at the plugin root. Only `plugin.json` belongs inside
`.claude-plugin/`. Do not add duplicate `.codex/`, `.agents/plugins/`, or other
vendor-specific sidecars; Codex reads the Claude marketplace metadata directly.

## Skill frontmatter

```yaml
---
name: network-recon
description: "Plans authorized network reconnaissance and audits scan coverage. Use when mapping hosts, services, or network exposure inside an agreed scope."
allowed-tools: Read Grep Glob Bash
---
```

- `name` is kebab-case, matches the directory, and is at most 64 characters.
- `description` states what the skill does and when it applies, using language a
  practitioner would naturally type.
- Quote descriptions containing a colon.
- `allowed-tools` is optional. Use the smallest set the workflow needs.
- Do not require custom metadata to use a skill. Repository catalog categories
  belong in the root README, not in the runtime interface.

## Write the skill, not a framework

Assume the model is capable. Add the domain knowledge, decisions, boundaries,
and failure modes that materially improve its work.

A strong `SKILL.md` usually contains:

- a short statement of purpose;
- `## When to Use` and `## When NOT to Use`;
- a direct workflow or decision process;
- the important judgment calls and tradeoffs;
- `## Rationalizations to reject` for security work; and
- links to supporting resources only where they are needed.

Use imperative instructions. Prefer ordinary practitioner language over
repository-specific terms. A user should not need to understand Zero Lab's
internal taxonomy before using a skill.

Keep `SKILL.md` under 500 lines. This is a ceiling, not a target. Move
conditional detail into references when progressive disclosure makes the core
workflow clearer.

## Supporting resources are optional

### References

Use `references/` for material the agent needs only in a particular mode:
protocol details, platform-specific guidance, extended examples, or policy
notes. Link every reference from `SKILL.md` and say when to read it.

Do not create a schema merely to make prose machine-readable. A schema belongs
only where another tool or external system genuinely consumes that exact
format.

### Scripts

Use `scripts/` when code performs real reusable work: parsing scanner output,
generating SARIF, checking IP scope, transforming artifacts, or another
operation where deterministic execution materially improves the result.

Do not add a script solely to prove that the skill followed its own prose.
Behavioral quality belongs in `evals/`; code correctness belongs in `tests/`.

Invoke skill-local scripts with `{baseDir}` so the path does not depend on the
user's current working directory:

```sh
uv run {baseDir}/scripts/check_scope.py scope.json
```

Python scripts with external dependencies use PEP 723 metadata and run through
`uv`. Shell scripts use `set -euo pipefail`, portable POSIX ERE, and explicit
error handling.

### Assets

Use `assets/` for files consumed or copied by the workflow and for UI branding.
Do not place instructions in assets. Each skill's `agents/openai.yaml` points to
its local Zero Lab mark so copied skills keep their presentation metadata.

## UI metadata

Every public skill includes `agents/openai.yaml`:

```yaml
interface:
  display_name: "Network Recon"
  short_description: "Plan authorized network reconnaissance and coverage"
  icon_small: "assets/zero-lab-mark.svg"
  icon_large: "assets/zero-lab-mark.svg"
  brand_color: "#30A46C"
```

Keep the display name, description, and skill behavior aligned. UI metadata is
presentation, not an alternative instruction channel.

## Security skill standard

Every security skill includes `## Rationalizations to reject`. Capture the
shortcuts that produce missed findings, unsafe actions, or unsupported claims,
and explain the required correction.

Preserve these collection-wide boundaries:

- authorization and scope remain external to the skill;
- a skill never creates permission to act;
- missing evidence remains missing;
- blocked and unknown work stays visible;
- observation, inference, validation, and demonstrated impact remain distinct;
- defensive purpose does not excuse unsafe execution; and
- report all supported findings with severity rather than pre-filtering them.

These boundaries should read as part of the practitioner workflow, not as a
separate governance product.

## Plugin metadata and registration

`plugins/<name>/.claude-plugin/plugin.json` contains:

```json
{
  "name": "plugin-name",
  "version": "0.2.0",
  "description": "One clear sentence describing the capability",
  "author": {
    "name": "zero-lab.ai",
    "email": "contact@zero-lab.ai",
    "url": "https://zero-lab.ai"
  }
}
```

Every plugin is registered in `.claude-plugin/marketplace.json`, linked from
the root README, and assigned in `CODEOWNERS`. Marketplace descriptions and
versions match `plugin.json` exactly.

Bump the plugin version whenever a user-visible change ships. Use a minor bump
for new behavior or a pre-1.0 breaking change, and a patch bump for a fix.

## Plugin README

Write for someone browsing the marketplace. Explain:

- what the plugin does;
- when to use it;
- the included skills or other entry points;
- installation and ordinary invocation; and
- the license.

Do not lead with internal schemas, checker exit codes, build history, or our
authoring philosophy.

## Tests and evaluations

Test code where code exists. Evaluation and unit testing are different:

- `tests/` verifies scripts, workflows, parsers, and deterministic outputs.
- `evals/` measures whether loading the skill changes model behavior on a
  realistic task.

An evaluation grader must measure an observable artifact or decision, not the
presence of expected wording. Self-test graders so an evaluation that stops
discriminating cannot report a false pass.

Do not require every prose skill to ship a script or a test directory. Add
resources in response to demonstrated need.

## Before submitting

```sh
make check
```

The local gate validates manifests and interfaces, checks references and path
hygiene, runs formatting and shell analysis, and executes every discovered
test suite. CI additionally verifies marketplace loading under Claude Code and
Codex.

## Reference implementations

- `agent-surface-audit` — tool-backed skill with references and tests.
- `network-recon` — multiple deterministic helpers that perform real work.
- `binary-fault-triage` — prose-only evidence-analysis skill.
- `findings-report` — concise reporting guidance without a runtime schema.
