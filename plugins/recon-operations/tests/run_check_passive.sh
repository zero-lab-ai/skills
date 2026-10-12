#!/usr/bin/env bash
# Proves check_passive.py holds the passive premise and fails closed.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/osint-scanner/scripts/check_passive.py"
f="$here/fixtures/osint-scanner"

run() { python3 -I "$script" "$@"; }

echo "-- a fully passive plan exits 0"
run "$f/passive-clean.json" >/dev/null

echo "-- a passive plan with target contact exits 1 and names the offenders"
set +e
out="$(run "$f/violation.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "httpx" || {
  echo "missed httpx"
  exit 1
}
echo "$out" | grep -E -q "target .*amass" || {
  echo "missed active amass"
  exit 1
}

echo "-- the SAME actions pass when target contact is authorized"
run "$f/authorized.json" >/dev/null

echo "-- an unknown tool in a passive plan fails closed, not open"
set +e
run "$f/unknown-tool.json" >/dev/null
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1 on unknown tool, got $rc"
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
