#!/usr/bin/env bash
# Proves check_detection.py requires both proofs and never passes an untested rule.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/detection-engineering/scripts/check_detection.py"
f="$here/fixtures/detection-engineering"

run() { python3 -I "$script" "$@"; }

echo "-- a rule proven both ways exits 0"
run "$f/proven.json" >/dev/null

fail_case() {
  local file="$1" want="$2"
  set +e
  out="$(run "$f/$file.json")"
  rc=$?
  set -e
  [ "$rc" -eq 1 ] || {
    echo "$file: expected exit 1, got $rc"
    echo "$out"
    exit 1
  }
  echo "$out" | grep -E -q "$want" || {
    echo "$file: missing '$want'"
    echo "$out"
    exit 1
  }
}

echo "-- a rule with no true-negative test fails (unproven against FPs)"
fail_case untested-tn "no true-negative test"

echo "-- a rule that fires on known-good fails (false positive)"
fail_case fires-on-benign "fired on known-good"

echo "-- a rule that never fires on known-bad fails (does not detect)"
fail_case never-fires "did NOT fire"

echo "-- a rule over the 90% FP ceiling fails (rewrite, not tune)"
fail_case over-fp-ceiling "over 90% ceiling"

echo "-- an empty record exits 2"
set +e
run "$f/empty.json" >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2 on empty record, got $rc"
  exit 1
}

echo "ok"
