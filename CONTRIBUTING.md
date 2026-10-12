# Contributing

Thanks for helping improve the Zero Lab skills collection.

## Before opening a change

- Use the existing bundle when the capability fits; a new skill does not
  automatically require a new plugin.
- Keep the skill folder independently portable. Core instructions must not
  depend on plugin wrappers, private infrastructure, or one agent harness.
- Preserve authorization, scope, evidence, and stop boundaries. A skill never
  creates permission to act.
- Do not include client data, credentials, private assessment artifacts,
  reusable bypass payloads, or Zero Lab internal material.

Read [AGENTS.md](AGENTS.md) for the complete authoring contract and repository
layout.

## Validate the change

Run the full local gate:

```sh
make check
```

For a new or materially changed skill, include a realistic behavioral case in
the bundle's `evals/` directory. Record only evidence produced by an actual
run; do not claim harness compatibility from formatting checks alone.

## Submit the change

Open a focused pull request that explains:

- the operator problem the change addresses;
- why it belongs in the selected bundle;
- the safety and authorization boundary;
- tests and behavioral evaluations run; and
- the required plugin version bump.

Security vulnerabilities should be reported privately as described in
[SECURITY.md](SECURITY.md), not in a public issue.
