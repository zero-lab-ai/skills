#!/usr/bin/env bash
# Proves audit_scan.py still detects its targets and never passes zero coverage.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
script="$here/../skills/network-recon/scripts/audit_scan.py"
fixtures="$here/fixtures/network-recon"

run() { python3 -I "$script" "$@"; }

echo "-- good coverage must exit 0 with no findings"
out="$(run "$fixtures/good-coverage.xml")"
echo "$out" | grep -E -q "0 coverage finding" || {
  echo "expected no findings"
  echo "$out"
  exit 1
}

echo "-- zero hosts up must exit 2, NOT 0 (a scan of nothing is not clean)"
set +e
out="$(run "$fixtures/zero-hosts-up.xml")"
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "zero-hosts-up" || {
  echo "missing check: zero-hosts-up"
  exit 1
}

echo "-- all-filtered with nothing open must flag high and exit 1"
set +e
out="$(run "$fixtures/all-filtered.xml")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
echo "$out" | grep -E -q "all-filtered-no-open" || {
  echo "missing check: all-filtered-no-open"
  exit 1
}

echo "-- narrow scan must flag the coverage it lacks"
set +e
out="$(run "$fixtures/narrow-scan.xml")"
rc=$?
set -e
[ "$rc" -eq 1 ] || {
  echo "expected exit 1, got $rc"
  echo "$out"
  exit 1
}
for want in no-udp-coverage no-service-detection limited-port-range; do
  echo "$out" | grep -E -q "$want" || {
    echo "missing check: $want"
    echo "$out"
    exit 1
  }
done

echo "-- empty report must exit 2"
set +e
run "$fixtures/empty.xml" >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 2 ] || {
  echo "expected exit 2 on empty report, got $rc"
  exit 1
}

echo "-- grepable input must parse and announce reduced checks"
printf '# Nmap 7.94 scan initiated as: nmap -sS -oG out.gnmap 10.0.0.0/30\nHost: 10.0.0.5 ()\tStatus: Up\nHost: 10.0.0.5 ()\tPorts: 22/open/tcp//ssh///\n' >"$fixtures/tmp.gnmap"
set +e
out="$(run "$fixtures/tmp.gnmap")"
rc=$?
set -e
rm -f "$fixtures/tmp.gnmap"
echo "$out" | grep -E -q "reduced-checks" || {
  echo "missing check: reduced-checks"
  echo "$out"
  exit 1
}

echo "ok"
