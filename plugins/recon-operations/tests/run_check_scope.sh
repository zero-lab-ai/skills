#!/usr/bin/env bash
# Proves check_scope.py fails closed on out-of-scope, excluded, and invalid targets.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/network-recon/scripts/check_scope.py"
fixtures="$here/fixtures/network-recon"

run() { python3 -I "$script" "$@"; }

echo "-- targets wholly inside authorization and outside exclusions pass"
out="$(run "$fixtures/scope-clean.json")"
echo "$out" | grep -E -q "3 target\(s\) authorized" || {
  echo "expected three authorized targets"
  echo "$out"
  exit 1
}

echo "-- a target outside every authorized range fails and is named"
set +e
out="$(run "$fixtures/scope-outside.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "OUTSIDE[[:space:]]+10\.1\.0\.0/24" || {
  echo "missing outside target"
  echo "$out"
  exit 1
}

echo "-- a target inside an excluded range fails and is named"
set +e
out="$(run "$fixtures/scope-excluded.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "EXCLUDED[[:space:]]+10\.0\.0\.70" || {
  echo "missing excluded target"
  echo "$out"
  exit 1
}

echo "-- partial CIDR overlap does not authorize the wider target"
set +e
out="$(run "$fixtures/scope-partial-overlap.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "OUTSIDE[[:space:]]+10\.0\.0\.0/24" || {
  echo "partial overlap was not rejected"
  echo "$out"
  exit 1
}

echo "-- empty targets fail as unmeasured input"
set +e
out="$(run "$fixtures/scope-empty.json" 2>&1)"
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2, got $rc"
  echo "$out"
  exit 1
}

echo "-- non-IP targets fail closed rather than triggering name resolution"
set +e
out="$(run "$fixtures/scope-invalid.json" 2>&1)"
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "internal\.example\.com" || {
  echo "invalid target was not named"
  echo "$out"
  exit 1
}

echo "ok"
