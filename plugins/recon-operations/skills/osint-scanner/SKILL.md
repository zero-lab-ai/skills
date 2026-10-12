---
name: osint-scanner
description: "Maps a target's public footprint — infrastructure, tech stack, leaked credentials, and people — using third-party data so no packet reaches the target. Use when scoping an engagement, planning a phishing pretext, or doing reconnaissance where the target must not detect it, and when deciding whether a recon action actually touches the target or not."
allowed-tools: Read Grep Glob Bash
---

# OSINT scanner

The stealthiest scan is the one you never send. OSINT reaches a target's
footprint by asking third parties who already looked — so done correctly it
generates **zero packets to the target** and nothing to detect.

**The single discipline that makes this red-team-safe: know, for every action,
whether it touches the target.** A query to Shodan reads a scan Shodan already
ran. Pointing a tool at the target's own web host or authoritative nameserver
is contact, and contact is what a defender sees. The line between them is the
skill; blur it and OSINT stops being passive.

## When to Use

- Scoping an engagement, planning a phishing pretext, or doing reconnaissance where the target must not detect it, and when deciding whether a recon action actually touches the target or not.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Classify contact before you run anything

```sh
uv run {baseDir}/scripts/check_passive.py plan.json
```

Takes a plan of intended actions and reports each one's contact level —
`none` (third party only), `target` (reaches the target's infrastructure), or
`unknown` — and **fails a passive plan that contains any `target` or
`unknown` action.** An unexamined "maybe" is treated as contact, because on a
red team op an unexamined maybe is how you get caught. See
`references/contact-levels.md`.

## What you can learn without touching the target

### Infrastructure and DNS
Map servers, subdomains and cloud without a packet to their firewall.

| Tool | Gets you | Contact |
|---|---|---|
| `amass` (passive) | subdomains from hundreds of passive sources | none |
| `crt.sh` | every TLS cert ever issued — exposes dev/staging subdomains | none |
| Shodan / Censys | open ports, software versions, exposures from global scans | none |
| `dig` TXT/MX (public resolver) | mail provider and security stack (Proofpoint, Mimecast, Google) | none |

> ⚠ `amass` and `theHarvester` also have **active** modes that resolve and
> brute-force against the target. Those are contact. Declare the mode.

### Defensive stack
Know what you are up against before planning anything.

- **BuiltWith / Wappalyzer** — frameworks, CMS, trackers (programmatic Wappalyzer
  fetches the pages — that is contact; the catalog lookup is not).
- **SPF / DMARC records** — reveal the mail-security vendor, so you learn their
  phishing defenses before writing a pretext.

### Credentials and exposure
The initial foothold that needs no exploit.

- **DeHashed** — historical breach corpus; search the domain for reused passwords.
- **TruffleHog** — scans the target's *public* repos for leaked keys and secrets
  in commit history (the repo is public; you are reading what they published).
- **Google dorking** — `site:target.com filetype:pdf "confidential"`.

### People — the phishing/vishing surface
- **theHarvester** (passive sources) — emails, names, subdomains from search engines.
- **Hunter.io** — corporate email format, to turn a name into an address.

## This is red-team recon, not a pentest sweep

If you want completeness and do not care about noise, you want the
`network-recon` skill (penetration-testing). This skill assumes the opposite:
the target must not know you looked. Thoroughness that generates detectable
contact is a loss here, not a win.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "It's just recon, it's harmless." | Recon that touches the target is detectable and attributable. Contact is the thing to avoid, not the payload. |
| "`dig` is passive." | `dig` against the target's authoritative nameserver is contact. Only a public-resolver cache read is not. State which. |
| "amass is a passive tool." | Only in passive mode. Active/brute resolves against the target. Declare the mode or the script fails the plan. |
| "I'll run a quick httpx to confirm the hosts are live." | That is the first packet you send the target, and it undoes the point of everything passive that came before. |
| "The tool isn't in the list, probably fine." | Unknown is treated as contact and fails a passive plan. Classify it first. |
| "More thorough is better." | On a red team op, more contact is worse. The quiet result that no one noticed beats the complete one that tripped an alert. |
| "TruffleHog touches their repo." | It reads a repo they published publicly. Reading public data is not contact with their production infrastructure. |

## References

- [Contact levels](references/contact-levels.md) — what `none` / `target` / `unknown` mean and how the checker decides
- [Sources](references/sources.md) — the aggregators, what each exposes, and its contact level
