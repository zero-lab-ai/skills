#!/usr/bin/env bash
# Proves coverage_map.py refuses to count unknown as coverage.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/detection-validate/scripts/coverage_map.py"
f="$here/fixtures/detection-validate"

run() { python3 -I "$script" "$@"; }

echo "-- an honest, complete map exits 0 (passive technique excluded from denominator)"
out="$(run "$f/honest-complete.json")"
echo "$out" | grep -E -q "2/2 detectable covered \(100%\)" || {
  echo "denominator wrong"
  echo "$out"
  exit 1
}

echo "-- a real not-detected gap exits 1 and is named"
set +e
out="$(run "$f/real-gap.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "GAP  not-detected" || {
  echo "missed the gap"
  exit 1
}

echo "-- an executed technique with a blank outcome is unknown, not coverage, and fails"
set +e
out="$(run "$f/unknown-blank.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1 on unknown, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "unknown .* never recorded" || {
  echo "unknown not flagged"
  echo "$out"
  exit 1
}

echo "-- an invalid coverage value exits 2"
set +e
run "$f/bad-value.json" >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2 on bad value, got $rc"
  exit 1
}

echo "-- an empty map exits 2"
set +e
run "$f/empty.json" >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2 on empty map, got $rc"
  exit 1
}

echo "ok"
