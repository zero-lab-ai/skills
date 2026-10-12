#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Classify post-foothold enumeration commands by the signal they generate.
Runs nothing; it reads a plan and judges noise.

You have a shell on a host that is not yours. Every command is a potential
alert: Sysmon logs process creation, the EDR watches, the SOC analyst is one
anomaly away from pulling your access. Situational awareness is assessing
quietly before you act. The deterministic question per command is: how much
NEW, detectable signal does it generate?

  silent  reads local host state, zero network packets, low host telemetry
          (whoami, id, cat /etc/passwd, arp -a, netstat, ip route, /proc reads)
  blend   generates traffic that looks like normal administration — the point
          of living off the land (an LDAP query to the DC, a single DNS lookup,
          net view). Present, but lost in the baseline
  loud     anomalous traffic or activity a monitored environment flags (ping
          sweep, nmap, arp-scan, mass SMB enumeration, Responder)

Some commands run through a monitored channel (PowerShell with script-block
logging, WMI). Those carry a `monitored` note on top of their level, because
"it ran" is not "it was unseen".

Input: a JSON plan. `{"stealth": "required"|"relaxed", "actions":
[{"cmd": "arp -a", "note": "..."}]}` — `cmd` is matched on its leading tool.

Exit codes: 0 = plan consistent with its stealth setting. 1 = a stealth-required
plan contains loud (or unknown) actions. 2 = bad or empty input.

No network, no file writes, stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Match the leading command token (strip sudo/powershell wrappers first). Each
# entry: pattern -> (level, monitored, reason).
RULES: list[tuple[str, tuple[str, bool, str]]] = [
    # loud — anomalous, scans, sweeps, broadcast
    (r"^(nmap|masscan|rustscan|unicornscan)\b", ("loud", False, "port scanner from the host")),
    (r"^(arp-scan|netdiscover|fping|nbtscan)\b", ("loud", False, "active sweep / broadcast probe")),
    (r"^responder\b", ("loud", False, "poisons broadcast protocols; highly detectable")),
    (r"\bping\b.*(-b|/24|/16|\bfor\b|\bseq\b)", ("loud", False, "ping sweep across a range")),
    (
        r"^(crackmapexec|cme|nxc)\b.*\b(smb|ldap)\b.*\b(0\.0|/24|/16|,)",
        ("loud", False, "mass host enumeration"),
    ),
    # blend — looks like normal admin to the DC / DNS / shares
    (
        r"^(ldapsearch|nltest|setspn)\b",
        ("blend", False, "LDAP/AD query — normal admin traffic to the DC"),
    ),
    (r"^net\b", ("blend", False, "net command — common admin, but net view touches the DC")),
    (
        r"^(nslookup|dig|host)\b",
        ("blend", False, "a single DNS lookup blends; a zone transfer does not"),
    ),
    (
        r"^(smbclient|smbmap)\b",
        ("blend", False, "SMB to a share you'd plausibly touch; mass enum is loud"),
    ),
    (
        r"(get-aduser|get-adcomputer|get-addomain)\b",
        ("blend", True, "AD cmdlet via LDAP; PowerShell is script-block logged"),
    ),
    # silent — local host reads, zero network
    (
        r"^(whoami|id|hostname|uname|groups|w|who|last)\b",
        ("silent", False, "local identity/host read"),
    ),
    (
        r"^(ipconfig|ifconfig|ip|route|netstat|ss|arp)\b",
        ("silent", False, "local network-state read, no packets"),
    ),
    (r"^(cat|less|head|tail|ls|dir|env|set|printenv)\b", ("silent", False, "local file/env read")),
    (r"^(sudo\s+-l|getcap|find)\b", ("silent", False, "local privilege/filesystem inspection")),
    (r"/proc/", ("silent", False, "procfs read, no network")),
    (
        r"^(systeminfo|wmic\s+os|sc\s+query|tasklist|ps)\b",
        ("silent", False, "local system/process read"),
    ),
    # monitored channel wrappers
    (
        r"^(powershell|pwsh)\b",
        ("blend", True, "PowerShell: subject to AMSI + script-block logging"),
    ),
    (r"^wmic\b", ("blend", True, "WMI: commonly monitored for lateral/recon abuse")),
]
COMPILED = [(re.compile(p, re.I), v) for p, v in RULES]


def classify(cmd: str) -> tuple[str, bool, str]:
    c = cmd.strip()
    # peel a leading sudo so the real tool is matched
    c_stripped = re.sub(r"^sudo\s+(-\S+\s+)*", "", c, flags=re.I)
    for rx, (level, monitored, reason) in COMPILED:
        if rx.search(c_stripped) or rx.search(c):
            return (level, monitored, reason)
    return ("unknown", False, "command not classified; assess its noise before running")


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("plan", type=Path, help="JSON enumeration plan")
    ap.add_argument("--json", action="store_true", help="emit result as JSON")
    args = ap.parse_args()

    if not args.plan.exists():
        print(f"error: {args.plan} does not exist", file=sys.stderr)
        return 2
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"error: cannot read plan: {e}", file=sys.stderr)
        return 2

    actions = plan.get("actions") if isinstance(plan, dict) else None
    if not isinstance(actions, list) or not actions:
        print("error: plan has no actions; a review of nothing is not a pass", file=sys.stderr)
        return 2

    stealth = str(plan.get("stealth", "required")).strip().lower()
    stealth_required = stealth != "relaxed"

    results = []
    for a in actions:
        cmd = str(a.get("cmd", "")).strip()
        level, monitored, reason = classify(cmd) if cmd else ("unknown", False, "action has no cmd")
        results.append((cmd or "(empty)", level, monitored, reason))

    violations = [r for r in results if stealth_required and r[1] in ("loud", "unknown")]

    if args.json:
        print(
            json.dumps(
                {
                    "stealth": stealth,
                    "actions": [
                        {"cmd": c, "level": lv, "monitored": m, "reason": r}
                        for c, lv, m, r in results
                    ],
                    "violations": [{"cmd": c, "level": lv} for c, lv, m, r in violations],
                },
                indent=2,
            )
        )
    else:
        label = "stealth required" if stealth_required else "stealth relaxed"
        print(f"{label}, {len(actions)} action(s)")
        for cmd, level, monitored, reason in results:
            bad = stealth_required and level in ("loud", "unknown")
            mark = "!!" if bad else ("* " if monitored else "  ")
            mon = " [monitored channel]" if monitored else ""
            print(f"  {mark} {level:<8} {cmd[:40]:<40} {reason}{mon}")
        if violations:
            print(
                f"\n{len(violations)} action(s) too loud for a stealth plan. Replace with a "
                "silent or blend equivalent, or set stealth to relaxed and accept the signal."
            )

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
