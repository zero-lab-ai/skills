#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Audit a completed network scan for coverage. Does NOT scan anything.

The question this answers is not "what did we find" but "was this scan capable
of finding it". A scan that reached nothing reports the same empty result as a
scan of a hardened host, and the two are not the same fact.

Input: an nmap XML report (`-oX`) or grepable report (`-oG`). XML carries the
command line and per-port states, so it supports every check; grepable supports
a reduced set and says so.

Output: one finding per line, `SEVERITY  check  detail`, sorted by severity.

Exit codes: 0 = scan had real coverage and no gap above info. 1 = coverage gaps
at medium or above. 2 = bad input, or ZERO coverage — nothing responded, or no
port was ever probed. A scan of nothing is not a clean result, so it cannot
exit 0.

No network, no file writes, stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SEV_ORDER = {"high": 0, "medium": 1, "info": 2}

# Flags that narrow a scan. Presence changes what "clean" is allowed to mean.
UDP_FLAGS = re.compile(r"(?:^|\s)-sU(?:\s|$)")
VERSION_FLAGS = re.compile(r"(?:^|\s)-(?:sV|A)(?:\s|$)")
LIMITED_PORTS = re.compile(r"(?:^|\s)(-F|--top-ports\s+\d+|-p\s*\S+)(?:\s|$)")
ALL_PORTS = re.compile(r"(?:^|\s)-p-|(?:^|\s)-p\s*1-65535(?:\s|$)")


class Scan:
    """Normalized view of a scan report, whatever format it arrived in."""

    def __init__(self) -> None:
        self.fmt = "unknown"
        self.args = ""
        self.hosts_total = 0
        self.hosts_up = 0
        self.ports_probed = 0  # port entries actually reported
        self.protocols: set[str] = set()
        self.states: dict[str, int] = {}
        self.hosts_all_filtered: list[str] = []
        self.hosts_with_open: list[str] = []


def parse_xml(path: Path) -> Scan | None:
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError):
        return None
    if root.tag != "nmaprun":
        return None
    s = Scan()
    s.fmt = "nmap-xml"
    s.args = root.get("args", "")
    for host in root.findall("host"):
        s.hosts_total += 1
        status = host.find("status")
        if status is None or status.get("state") != "up":
            continue
        s.hosts_up += 1
        addr_el = host.find("address")
        addr = addr_el.get("addr", "?") if addr_el is not None else "?"
        seen_states: set[str] = set()
        ports_el = host.find("ports")
        if ports_el is None:
            continue
        # extraports summarises large blocks nmap collapsed (e.g. 65000 filtered)
        for ep in ports_el.findall("extraports"):
            st = ep.get("state", "unknown")
            try:
                count = int(ep.get("count", "0"))
            except ValueError:
                count = 0
            s.ports_probed += count
            s.states[st] = s.states.get(st, 0) + count
            if count:
                seen_states.add(st)
        for port in ports_el.findall("port"):
            s.ports_probed += 1
            s.protocols.add(port.get("protocol", "?"))
            st_el = port.find("state")
            st = st_el.get("state", "unknown") if st_el is not None else "unknown"
            s.states[st] = s.states.get(st, 0) + 1
            seen_states.add(st)
        if "open" in seen_states:
            s.hosts_with_open.append(addr)
        elif seen_states and seen_states <= {"filtered"}:
            s.hosts_all_filtered.append(addr)
    return s


def parse_grepable(path: Path) -> Scan | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    if "Host:" not in text:
        return None
    s = Scan()
    s.fmt = "nmap-grepable"
    m = re.search(r"(?m)^# Nmap .* as: (.+)$", text)
    if m:
        s.args = m.group(1).strip()
    for line in text.splitlines():
        if not line.startswith("Host:"):
            continue
        s.hosts_total += 1
        if "Status: Up" in line:
            s.hosts_up += 1
        addr_m = re.match(r"Host:\s+(\S+)", line)
        addr = addr_m.group(1) if addr_m else "?"
        ports_m = re.search(r"Ports:\s+(.+?)(?:\tIgnored|$)", line)
        if not ports_m:
            continue
        seen_states: set[str] = set()
        for entry in ports_m.group(1).split(","):
            parts = [p.strip() for p in entry.strip().split("/")]
            if len(parts) < 3:
                continue
            s.ports_probed += 1
            st, proto = parts[1], parts[2]
            s.protocols.add(proto)
            s.states[st] = s.states.get(st, 0) + 1
            seen_states.add(st)
        if "open" in seen_states:
            s.hosts_with_open.append(addr)
        elif seen_states and seen_states <= {"filtered"}:
            s.hosts_all_filtered.append(addr)
    return s


def audit(s: Scan) -> list[tuple[str, str, str]]:
    """Return (severity, check, detail). Order of checks is deliberate: the
    zero-coverage cases come first because every later check is meaningless if
    the scan never reached anything."""
    f: list[tuple[str, str, str]] = []
    reduced = s.fmt == "nmap-grepable"

    if s.hosts_total == 0:
        f.append(("high", "no-hosts-in-report", "report contains zero hosts; nothing was scanned"))
        return f
    if s.hosts_up == 0:
        f.append(
            (
                "high",
                "zero-hosts-up",
                f"{s.hosts_total} host(s) in scope, 0 responded. This is NOT a clean "
                "result -- it is an unanswered question. Check routing and reachability "
                "before concluding the range is empty",
            )
        )
        return f
    if s.ports_probed == 0:
        f.append(
            (
                "high",
                "zero-ports-probed",
                f"{s.hosts_up} host(s) up but no port was reported. The scan proved "
                "liveness and nothing else",
            )
        )
        return f

    # A path that is blocked and a host that is closed look identical here and
    # are different facts. See the skill's `## Reading results`.
    if s.hosts_all_filtered and not s.hosts_with_open:
        f.append(
            (
                "high",
                "all-filtered-no-open",
                f"every reported port on all {len(s.hosts_all_filtered)} responding "
                "host(s) is filtered and nothing is open. Filtered is not closed: "
                "verify a route exists to this segment before scanning deeper",
            )
        )
    elif s.hosts_all_filtered:
        f.append(
            (
                "medium",
                "host-all-filtered",
                f"fully filtered host(s): {', '.join(sorted(s.hosts_all_filtered)[:8])}",
            )
        )

    if s.args:
        if not UDP_FLAGS.search(s.args):
            f.append(
                (
                    "medium",
                    "no-udp-coverage",
                    "no -sU in the command line; every UDP service is invisible to "
                    "this scan. Absence of UDP findings is not evidence",
                )
            )
        if not VERSION_FLAGS.search(s.args):
            f.append(
                (
                    "medium",
                    "no-service-detection",
                    "no -sV/-A; service names are inferred from port numbers, not "
                    "observed. Do not report them as identified",
                )
            )
        if LIMITED_PORTS.search(s.args) and not ALL_PORTS.search(s.args):
            f.append(
                (
                    "medium",
                    "limited-port-range",
                    "command line restricts the port range; unscanned ports are "
                    "unknown, not closed",
                )
            )
    else:
        f.append(
            (
                "info",
                "no-command-line",
                "report does not record the command line; flag-based coverage checks were skipped",
            )
        )

    if s.protocols and s.protocols <= {"tcp"}:
        f.append(("info", "tcp-only-results", "results contain TCP only"))

    down = s.hosts_total - s.hosts_up
    if down and down / s.hosts_total >= 0.9:
        f.append(
            (
                "info",
                "most-hosts-down",
                f"{down}/{s.hosts_total} hosts did not respond; consider whether the "
                "range, routing or timing is wrong rather than the range being empty",
            )
        )
    if reduced:
        f.append(
            (
                "info",
                "reduced-checks",
                "grepable input: per-port detail is coarse. Use -oX for full coverage auditing",
            )
        )
    return f


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("report", type=Path, help="nmap -oX (XML) or -oG (grepable) report")
    ap.add_argument("--json", action="store_true", help="emit findings as JSON")
    args = ap.parse_args()

    if not args.report.exists():
        print(f"error: {args.report} does not exist", file=sys.stderr)
        return 2
    if args.report.stat().st_size == 0:
        print("error: report is empty; an audit of nothing is not a pass", file=sys.stderr)
        return 2

    scan = parse_xml(args.report) or parse_grepable(args.report)
    if scan is None:
        print(
            f"error: {args.report} is not a recognised nmap XML or grepable report", file=sys.stderr
        )
        return 2

    findings = sorted(audit(scan), key=lambda x: SEV_ORDER.get(x[0], 9))

    if args.json:
        print(
            json.dumps(
                {
                    "format": scan.fmt,
                    "command_line": scan.args,
                    "hosts_total": scan.hosts_total,
                    "hosts_up": scan.hosts_up,
                    "ports_probed": scan.ports_probed,
                    "protocols": sorted(scan.protocols),
                    "port_states": scan.states,
                    "findings": [{"severity": s, "check": c, "detail": d} for s, c, d in findings],
                },
                indent=2,
            )
        )
    else:
        protos = ",".join(sorted(scan.protocols)) or "none"
        print(
            f"{scan.fmt}: {scan.hosts_up}/{scan.hosts_total} hosts up, "
            f"{scan.ports_probed} ports probed, protocols={protos}, "
            f"{len(findings)} coverage finding(s)"
        )
        for sev, check, detail in findings:
            print(f"{sev:<7} {check:<24} {detail}")

    # Zero coverage must never exit 0, regardless of how clean it looks.
    if any(
        c in ("no-hosts-in-report", "zero-hosts-up", "zero-ports-probed") for _, c, _ in findings
    ):
        return 2
    return 1 if any(s in ("high", "medium") for s, _, _ in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
