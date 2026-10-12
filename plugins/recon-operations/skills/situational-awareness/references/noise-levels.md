# Noise levels

`classify_enum.py` sorts each planned command into one level. The level is the
one fact that decides whether post-foothold assessment stayed quiet.

| Level | Meaning | Examples |
|---|---|---|
| `silent` | Reads local host state. Zero network packets, low host telemetry. | `whoami`, `id`, `arp -a`, `netstat`, `ip route`, `cat /etc/passwd`, `/proc` reads, `tasklist` |
| `blend` | Generates traffic that looks like normal administration. Present in the logs, lost in the baseline. | `ldapsearch` / `nltest` to the DC, a single `nslookup`, `net view`, `smbclient` to a share you'd plausibly touch |
| `loud` | Anomalous activity a monitored environment flags. | `nmap`, `masscan`, `arp-scan`, `responder`, a ping sweep, mass `nxc`/`crackmapexec` host enumeration |
| `unknown` | Command not classified. | anything the rule set does not recognise |

## The monitored-channel flag

Some commands are `blend` by traffic but run through a channel that is itself
watched — PowerShell (AMSI + script-block logging), WMI. They are marked
`[monitored channel]`. The flag does not fail a stealth plan on its own, because
the action may still be the right call, but it records that the command left a
signature on the host even if its network traffic blended. "It ran" is not "it
was unseen".

## Why unknown fails closed

In a stealth-required plan an unclassified command is treated as loud and fails
the plan. The cost of being wrong is detection and lost access. Classify the
command — add it to the rule set in `classify_enum.py` with a one-line reason —
and run again. A maybe is not a yes when the downside is burning your foothold.

## Stealth setting

```json
{"stealth": "required", "actions": [{"cmd": "arp -a"}, {"cmd": "ldapsearch -x ..."}]}
```

`stealth: required` (the default) fails loud and unknown actions. `stealth:
relaxed` classifies everything but fails nothing — use it only when noise is
acceptable (a pentest, or a stage where you no longer care about detection).
Relaxing stealth is a decision with a consequence, not a way to silence the
classifier.

## Matching

`cmd` is matched on its leading tool, after stripping a leading `sudo`. The
classifier reads the command; it never runs it.
