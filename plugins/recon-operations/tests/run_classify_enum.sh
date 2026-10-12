#!/usr/bin/env bash
# Proves classify_enum.py holds the stealth premise and fails closed.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/situational-awareness/scripts/classify_enum.py"
f="$here/fixtures/situational-awareness"

run() { python3 -I "$script" "$@"; }

echo "-- an all-silent + blend plan passes under stealth"
run "$f/quiet-plan.json" >/dev/null

echo "-- loud actions fail a stealth plan and are named"
set +e
out="$(run "$f/loud-in-stealth.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "loud .*nmap" || {
  echo "missed nmap"
  exit 1
}
echo "$out" | grep -E -q "loud .*responder" || {
  echo "missed responder"
  exit 1
}

echo "-- the SAME loud actions pass when stealth is relaxed"
run "$f/relaxed-same.json" >/dev/null

echo "-- an unclassified command fails closed, not open"
set +e
run "$f/unknown-cmd.json" >/dev/null
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1 on unknown cmd, got $rc"
  exit 1
}

echo "-- a monitored-channel command is blend, flagged, and does NOT fail"
out="$(run "$f/monitored.json")"
echo "$out" | grep -E -q "monitored channel" || {
  echo "monitored flag missing"
  echo "$out"
  exit 1
}

echo "-- an empty plan exits 2"
set +e
run "$f/empty.json" >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2 on empty plan, got $rc"
  exit 1
}

echo "ok"
