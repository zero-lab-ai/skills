# Security

## What review covers

The release review for every plugin checks, at minimum:

- every script in `scripts/` for network calls, credential access, shell
  execution of untrusted input, and writes outside the working directory
- every `hooks/` file for commands that run on tool events
- `SKILL.md` and `references/` for instructions that would exfiltrate data,
  disable safety behavior, or expand the agent's permissions
- that the skill does what its description says and nothing else

## Reporting

Email contact@zero-lab.ai. Do not open a public issue for a vulnerability in
a shipped skill or script.

## Installing third-party skills

This repository contains zero-lab originals only. Published skills elsewhere
have been found carrying backdoors and malicious hooks. Read any skill before
you install it; the validator here is a floor, not a guarantee.
