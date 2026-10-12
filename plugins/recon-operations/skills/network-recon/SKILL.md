---
name: network-recon
description: "Plans authorized network reconnaissance, checks proposed targets against explicit IP scope, chooses scanning tools by cost, and audits completed scans for coverage. Use when mapping a network, enumerating hosts and services, deciding which scanner to run, or determining whether an empty scan is a finding or a failure."
allowed-tools: Read Grep Glob Bash
---

# Network recon

Running a scanner is not the skill. Anyone can run nmap. The skill is choosing
the right tool for the cost you can afford, and knowing when the output is
lying to you.

**An empty result and an unanswered question look identical.** Most recon
mistakes are made in the gap between those two.

## When to Use

- Mapping a network, enumerating hosts and services, deciding which scanner to run, or determining whether an empty scan is a finding or a failure.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## This skill is loud, on purpose

It assumes **penetration test** conditions: an agreed scope, completeness as
the deliverable, and noise that nobody is scoring you on. Every recommendation
here optimises for *not missing things*.

**Do not apply it to a red team operation.** Red teaming optimises for the
opposite thing — reaching an objective without being detected, and testing the
security programme itself: people, processes, technology. A 65,535-port sweep
is correct practice here and disqualifying there. The tooling overlaps; the
optimisation function is reversed, and so is the right answer at almost every
decision point.

If stealth is a requirement, you want a quiet-enumeration skill, and this is
not it.

## Scope first, always

Establish and write down the authorized scope before the first packet. Refuse
targets outside it. A scan is an action against someone else's property; the
scope statement is the only thing that makes it legitimate, and "it was in the
same /16" is not a scope statement.

Treat authorization as a ceiling, not as a target list. When a request names
specific proposed targets inside a wider authorized range, admit only those
targets that pass the scope check. Do not expand discovery to the rest of the
range unless the requested target set explicitly includes it.

Before scanning, record IP/CIDR scope and proposed targets in a manifest and
run the deterministic check:

```sh
uv run {baseDir}/scripts/check_scope.py scope.json
```

```json
{
  "authorized": ["10.0.0.0/24"],
  "excluded": ["10.0.0.64/27"],
  "targets": ["10.0.0.12", "10.0.0.128/26"]
}
```

Exit `0` means every target is wholly contained in authorization and overlaps
no exclusion. Exit `1` names targets to refuse. Exit `2` means the manifest is
invalid or empty, so no scope decision was measured. The checker accepts IPs
and CIDRs only; resolve and authorize hostnames explicitly rather than making
the checker contact DNS.

## Tool selection

**Two stages, never one.** Fast discovery to find what is alive and listening,
then a targeted deep scan only on what answered. A single thorough scan across
an undiscovered range is the most common way to burn a day.

**Nmap carries ~99% of the work.** The others earn their place by being faster
at discovery, and they hand back to Nmap for fidelity.

| Goal | Tool | Cost | When it is the wrong choice |
|---|---|---|---|
| Find live hosts, layer 2 / local subnet | `netdiscover` (ARP) | seconds | Useless off-segment — ARP does not route |
| Sweep a large subnet for alive hosts | `masscan` | seconds–minutes | Trades precision and fingerprinting for raw speed. **Alive-tracking only**, then drop into Nmap |
| Find open TCP ports fast, all 65,535 | `rustscan` | seconds | Slow or lossy links can cost accuracy; it is a front end, not an answer |
| Initial TCP discovery | `nmap -sS` + top-ports, tuned `--min-rate` | seconds–minutes | Top-ports alone **will** miss non-standard ports. Never the last scan |
| Full TCP coverage | `nmap -p-` on discovered hosts | minutes–hours | Skipping it is how low-hanging fruit on odd ports gets missed |
| Service and version fidelity | `nmap -sV -sC` or `--script=safe,default` | minutes | Noisier and slower; without it, service names are guesses from port numbers |
| UDP, fast | `rustscan --udp` | seconds–minutes | **Finds only UDP ports that send back a response.** Silent services are invisible — a clean result here proves very little |
| UDP, complete | `nmap -sU` | hours to days on a full range | Almost always the wrong *default*. Scope it to the ports you care about and state the cost before starting |

**The standard chain:** `rustscan` or `masscan` for discovery → pipe the open
ports into `nmap -sV -sC` for identification → `nmap -p-` to confirm nothing
was missed.

**NSE:** `--script=safe,default` is the useful, non-destructive tier — basic
service information and versions without launching automated exploits. Treat
anything outside `safe,default` as an action requiring its own authorization.

### Protocol-specific enumeration

Once ports are known, stop using a network scanner and pivot:

| Service | Tool |
|---|---|
| Web — configuration and known issues | `nikto` |
| Web — content and directory discovery | `gobuster`, `feroxbuster`, `ffuf` |
| SMB / Windows — shares, users, null sessions | `enum4linux`, `netexec` (formerly CrackMapExec) |

### "Allowed" is context, not a property

Lists of permitted tools belong to the context that issued them. The tiering
above reflects what is sanctioned in OffSec exam conditions, which is a useful
baseline because it was drawn to exclude automated exploitation. **It is not a
permission slip anywhere else.** In an engagement the authority is the client's
rules of engagement, and in a lab it is the lab's. Check the authority that
actually governs the target in front of you.

## Reading results

Four readings that are wrong by default. Each one has cost real engagement time.

**`filtered` is not `closed`.** A blocked path and a closed port are
indistinguishable from a port scanner and are different facts. Before
concluding a segment is empty, prove a route exists to it — check the routing
table from the hosts you already hold. A segment that returns *all filtered,
nothing open* is more often unrouted than hardened.

**Clean with no coverage is not clean.** A scan that never reached the target
reports the same silence as a hardened host. Always audit coverage before
reporting a negative result; a scanner that cannot reach a box and calls it
clean is the worst output a scanner can produce.

**Absence is not evidence.** No UDP findings from a TCP-only scan is not a
finding about UDP. No service versions from a scan without version detection
means the service names are guesses from port numbers — do not write them into
a report as identified.

**"The environment is broken" is a live hypothesis.** When several independent
signals converge on nothing — no hosts responding, an unreachable subnet, no
credential anywhere, empty data stores — treat an unseeded or misconfigured
environment as a real possibility and verify it. Verifying the environment is
a skill, not a cop-out, and it beats hours spent grinding a target that was
never populated.

## Audit the scan before trusting it

```sh
uv run {baseDir}/scripts/audit_scan.py scan.xml          # nmap -oX (preferred) or -oG
uv run {baseDir}/scripts/audit_scan.py scan.xml --json
```

Reports coverage, not findings: hosts that actually responded, ports actually
probed, protocols covered, and which flags narrowed the scan. Exit `0` only
when there was real coverage; `1` on coverage gaps; **`2` when nothing
responded or no port was ever probed.** Zero coverage cannot exit `0`, by
design — see `references/coverage-checks.md`.

## Recon handoff

The handoff should make the denominator visible, not just list discovered
services:

| Field | Minimum content |
| --- | --- |
| Scope decision | Authorized ranges, exclusions, proposed targets, and checker result |
| Discovery coverage | Methods used, hosts attempted, hosts that responded, and route limitations |
| Port coverage | TCP and UDP ranges actually probed, including any rate or timing constraints |
| Service evidence | Observed protocol or version evidence; label port-based guesses as guesses |
| Open work | Unreached segments, filtered paths, incomplete UDP work, and blocked follow-up |
| Next action | The smallest authorized step that resolves the most important unknown |

An empty service list with nonempty open work is an incomplete assessment, not
a clean network.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "The scan came back clean, so it's clean." | Clean with zero coverage is an unanswered question. Audit coverage first. |
| "All ports are filtered, so the host is locked down." | More often there is no route. Prove reachability before concluding hardening. |
| "No UDP results, so no UDP services." | You did not scan UDP. Absence of a scan is not absence of a service. |
| "nmap said it's SSH." | Without version detection that is a guess from port 22. Do not report it as identified. |
| "I'll just run the full sweep to be safe." | "Safe" that costs days is a choice, not a default. State the cost and get it confirmed. |
| "The target is in the same range, close enough." | Scope is written down or it does not exist. |
| "The whole range is authorized, so I can discover all of it." | Authorization permits work; it does not request every permitted target. Preserve the supplied target set. |
| "Nothing is here, the range is empty." | Consider that the environment is unseeded or your path is wrong before concluding emptiness. |
| "It's faster to scan everything once than think about it." | The thinking is the skill. The scan is the easy part. |
| "Recon is recon — I'll use this on the red team engagement too." | No. This skill optimises for completeness and makes noise doing it. On a red team operation that noise is the finding, and it is the blue team's point. |

## References

- [Coverage checks](references/coverage-checks.md) — what the auditor checks and why each one exists
- [Scope and authorization](references/scope.md) — recording scope, and what to do when asked to exceed it
