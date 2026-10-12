#!/usr/bin/env bash
# Proves inspect_tools.py still detects its targets and refuses an empty manifest.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/agent-surface-audit/scripts/inspect_tools.py"
fixtures="$here/fixtures/agent-surface-audit"

run() { python3 -I "$script" "$@"; }

echo "-- poisoned manifest must produce high findings and exit 1"
set +e
out="$(run "$fixtures/poisoned.json")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  exit 1
}
for want in imperative-description hidden-content free-form-sink additional-properties destructive-no-guard no-description; do
  echo "$out" | grep -E -q "$want" || {
    echo "missing check: $want"
    echo "$out"
    exit 1
  }
done

echo "-- clean manifest must exit 0 with no high/medium"
run "$fixtures/clean.json" >/dev/null

echo "-- empty manifest must exit 2"
set +e
run "$fixtures/empty.json" >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2 on empty manifest, got $rc"
  exit 1
}

echo "ok"
