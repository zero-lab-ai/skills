---
name: situational-awareness
description: "Assesses a freshly compromised host quietly before acting — who/where/what's here/what's watching/what's around — using local reads and living-off-the-land so the SOC never sees the recon. Use right after gaining a foothold, before privilege escalation or lateral movement, or when deciding whether an enumeration command is quiet enough to run."
allowed-tools: Read Grep Glob Bash
---

# Situational awareness

The shell is blinking. You're in. Now sit on your hands for sixty seconds.

The first mistake most operators make is `whoami && ipconfig && net user &&
systeminfo` in rapid fire — while Sysmon logs every process, the EDR watches,
and the night-shift analyst gets a very interesting alert. **Assess before you
act, and assess quietly.** Every command is a potential detection.

## When to Use

- Assess a foothold within an operation's noise budget.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## The five questions

Answer these before you escalate, dump, or move:

1. **Who am I?** user, privileges, groups
2. **Where am I?** host, network, domain
3. **What's here?** software, data, services
4. **What's watching me?** security tools, logging, alerting — answer this *early*, because it changes how you answer the rest
5. **What's around me?** other systems, connections, trust relationships

## Classify the noise before you run it

```sh
uv run {baseDir}/scripts/classify_enum.py plan.json
```

Classifies each planned command by the signal it generates and **fails a
stealth-required plan that contains a loud or unclassified command.**

- **silent** — local host read, zero packets (`whoami`, `arp -a`, `netstat`, `cat /proc/...`)
- **blend** — looks like normal administration (`ldapsearch` to the DC, one DNS lookup, `net view`)
- **loud** — anomalous: scans, sweeps, Responder. A stealth plan rejects these.

Unknown commands fail closed; a monitored channel (PowerShell, WMI) is `blend`
but flagged, because "it ran" is not "it was unseen". See
`references/noise-levels.md`.

## Prefer what's already there (living off the land)

The quietest enumeration sends no new packets and uses no dropped tools:

- **ARP cache** — `arp -a` or `/proc/net/arp` lists hosts this box already
  talked to. Active targets, zero new traffic.
- **Passive capture** — sit on an interface with a native sniffer; broadcast,
  mDNS, LLMNR and DHCP reveal hostnames and services without a probe.
- **Ask the directory, don't scan it** — one LDAP query to the DC returns every
  computer and SPN. That is inventory without a port scan, and it looks like
  normal admin traffic.
- **Native loops over dropped scanners** — a slow `Test-NetConnection` or
  `/dev/tcp` check reads as background admin noise; a port scanner reads as an
  attacker.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "Let me just run my standard recon one-liner." | That one-liner is a signature. Rapid-fire enumeration is the classic post-exploitation alert. |
| "I'll scan the subnet to see what's around." | A scan from a foothold is the loudest thing you can do. Read the ARP cache and ask the DC instead. |
| "PowerShell ran, so I'm fine." | PowerShell is script-block logged and AMSI-scanned. It ran and it was recorded. |
| "I need a full picture before I move." | Completeness is a pentest value. Here, the picture you got without being seen beats the complete one that burned your access. |
| "This command isn't in the classifier, probably quiet." | Unknown fails closed. Assess its signal before you run it, not after. |
| "Answer 'what's watching me' later." | Answer it first. What's watching changes every other choice you make on the host. |

## References

- [Noise levels](references/noise-levels.md) — silent / blend / loud, the monitored-channel flag, and how the classifier decides
