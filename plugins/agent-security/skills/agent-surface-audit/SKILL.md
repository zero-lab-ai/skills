---
name: agent-surface-audit
description: "Reviews an MCP server's tool surface for tool poisoning, over-broad parameters, missing descriptions, and privilege escalation paths. Use when auditing, onboarding, or writing an MCP server, or when a user asks whether a server is safe to connect to an agent."
allowed-tools: Read Grep Glob Bash
---

# Reviewing MCP servers

An MCP server hands an agent a set of tools. Each tool is a name, a
description the model reads, and a parameter schema the model fills in. The
attack surface is those three things plus whatever the tool does when called.
This skill reviews the surface deterministically first, then reads the
implementation for the parts a scanner cannot judge.

## When to Use

- Auditing, onboarding, or writing an MCP server, or when a user asks whether a server is safe to connect to an agent.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Quick start

1. Get the server's tool list as JSON. Any of these work:
   - the server's `tools/list` response, saved to a file
   - a harness's exported MCP config or tool dump
   - for a source checkout, the decorated tool definitions, converted to the
     same JSON shape (see `references/manifest-format.md`)
2. Run the checker:
   ```
   uv run {baseDir}/scripts/inspect_tools.py path/to/tools.json
   ```
   It prints one finding per line with a severity and exits non-zero if the
   input contains zero tools. An empty manifest is a failed review, not a
   clean one.
3. For every `high` finding, open the implementation and confirm whether the
   risk is real (step 4). For `medium` and `info`, record them and move on.
4. Read the implementation for what the scanner cannot see, using
   `references/checklist.md`:
   - does the tool execute, eval, or template any parameter into a shell,
     SQL, or URL?
   - does it read or write outside the paths its description claims?
   - does it make network calls to hosts the user did not name?
   - does it carry credentials, and are they scoped to the operation?
5. Write findings with the `findings-report` skill if it is
   installed; otherwise use the structure in `references/finding-shape.md`.

## Review deliverable

Return one compact review record before writing individual findings:

| Field | What to record |
| --- | --- |
| Scope | Server name, version or commit, deployment context, and tool count |
| Manifest signals | Every scanner result, including medium and informational signals |
| Implementation checks | The code path reviewed for each high-risk parameter or side effect |
| Privilege paths | What data, credentials, networks, and hosts the server can actually reach |
| Evidence gaps | Missing source, deployment configuration, or runtime controls |
| Disposition | Acceptable as deployed, acceptable with stated constraints, or reject pending change |

Do not call the server safe merely because the manifest scan is clean. A clean
manifest means the description and parameter surface passed; the implementation
and deployment blast radius remain separate claims.

## What the scanner flags

| Check | Why it matters |
| --- | --- |
| Imperative text in a description (`ignore`, `always`, `you must`, `before calling`) | Tool poisoning: descriptions are prompt text the model obeys |
| Description references other tools or the system prompt | Cross-tool shadowing and instruction override |
| Hidden text markers (`<!-- -->`, zero-width chars, `<IMPORTANT>`) | Content meant for the model, not the human reviewer |
| Free-form string parameter named like a command, path, query, or URL | Injection sink; the model fills it from untrusted context |
| Parameter with no description or `additionalProperties: true` | Model guesses; reviewer cannot bound behavior |
| Tool name implies destructive action with no confirmation parameter | Irreversible side effect on a single model decision |
| Tool with no description at all | Unreviewable; the model will invent one |

Severity is assigned by the script and is a starting point, not a verdict.

## Judgment calls the script leaves to you

- **A shell tool is not automatically a finding.** `run_command` on a
  sandboxed dev container is the product. `run_command` on a production host
  reachable from a chat window is critical. Severity follows the blast radius
  of the deployment, which is in the config, not the manifest.
- **Descriptions that instruct the model are sometimes legitimate.** "Call
  `get_schema` before `run_query`" is good UX. "Ignore prior instructions
  about credentials" is an attack. The script flags both; you decide, and
  you record why.
- **Read-only is a claim, not a property.** A tool described as read-only
  that takes a path parameter can still read secrets. Check what the path is
  resolved against.

## Rationalizations to reject

- *"It's a first-party server from a reputable vendor."* Vendor servers have
  shipped `run_command` with no sandbox and descriptions with hidden
  instructions. Reputation changes the prior, not the review.
- *"The harness will ask the user before destructive calls."* Some do, some
  do not, and the approval prompt shows the tool name, not the parameters.
  Review as if every call auto-approves.
- *"The parameter schema is strict so injection is bounded."* A schema bounds
  the type, not the content. A `string` with `maxLength: 10000` is a shell
  command.
- *"The server only runs locally."* Local is where the user's SSH keys,
  cloud credentials, and source trees are. Local is the high-value target.
- *"There are too many tools to read them all."* Then the server has too
  many tools, and that is the first finding. Review all of them; the script
  makes the first pass cheap.

## Harness notes

In Claude Code, the server's tool list can be read from the active session's
MCP configuration rather than a saved file; the review itself is unchanged.
