# Coverage checks

What `scripts/audit_scan.py` checks, and why each check exists. The auditor
answers "was this scan capable of finding it", never "what did it find".

## Zero-coverage checks — these exit 2, never 0

| Check | Trigger | Why |
|---|---|---|
| `no-hosts-in-report` | report has zero hosts | nothing was scanned; there is no result to interpret |
| `zero-hosts-up` | hosts in scope, none responded | an unanswered question, not an empty network. Routing and reachability come before conclusions |
| `zero-ports-probed` | hosts up, no port reported | the scan proved liveness and nothing else |

A scan of nothing cannot exit `0`. If it could, a broken scan and a clean
network would be indistinguishable to anything consuming the exit code — and
the consumer is usually a report.

## Coverage gaps — exit 1

| Check | Trigger | Why |
|---|---|---|
| `all-filtered-no-open` | every reported port filtered, nothing open | reads as hardening, is usually an absent route |
| `host-all-filtered` | an individual host fully filtered | same question, scoped to one host |
| `no-udp-coverage` | no `-sU` in the command line | UDP services are invisible; absence is not evidence |
| `no-service-detection` | no `-sV`/`-A` | service names are inferred from port numbers, not observed |
| `limited-port-range` | `-F`, `--top-ports`, or a `-p` subset without `-p-` | unscanned ports are unknown, not closed |

## Informational

| Check | Trigger |
|---|---|
| `no-command-line` | report does not record the invocation, so flag-based checks were skipped |
| `tcp-only-results` | results contain TCP only |
| `most-hosts-down` | 90%+ of the range did not respond — consider wrong range, routing, or timing |
| `reduced-checks` | grepable input; per-port detail is coarse, prefer `-oX` |

## Input formats

`-oX` XML is preferred: it records the command line, per-port states, and
`extraports` blocks, so every check above can run. `-oG` grepable parses but
carries less, and the auditor says so rather than silently checking less.

## Why the command line matters

Most coverage facts are not in the results, they are in the invocation. A scan
with no `-sU` will never produce a UDP finding no matter how long it runs, and
nothing in the output says so. Reading the recorded command line is how the
auditor distinguishes "looked and found nothing" from "never looked".
