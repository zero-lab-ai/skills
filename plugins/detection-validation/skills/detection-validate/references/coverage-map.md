# Coverage map

The JSON `coverage_map.py` consumes. Every technique executed in an exercise is
mapped to whether a detection fired.

```json
{
  "techniques": [
    {"id": "T1595.001", "name": "Active Scanning: Port Scan",
     "executed": true, "coverage": "covered", "rule": "det-recon-001"},
    {"id": "T1589", "name": "Gather Victim Identity Info",
     "executed": true, "coverage": "not-detectable"},
    {"id": "T1021.001", "name": "Remote Services: RDP",
     "executed": true, "coverage": "not-detected"}
  ]
}
```

| Field | Meaning |
|---|---|
| `id` | ATT&CK technique ID |
| `name` | human label, for the report |
| `executed` | was the technique actually run in this exercise |
| `coverage` | one of `covered` / `partial` / `not-detected` / `not-detectable` / `unknown` |
| `rule` | optional ID of the detection that fired, for traceability |

## The five outcomes

- **covered** — executed and a detection fired. The only unqualified win.
- **partial** — fired weakly, late, or on only some variants. Counts toward
  coverage but flagged for tuning.
- **not-detected** — executed and nothing fired. A real, un-accepted gap. Exit 1.
- **not-detectable** — a passive technique that produces no observable: OSINT,
  reading public records, certificate transparency. There is nothing to detect,
  and that is a fact about the technique, not a failure of the SOC. Removed from
  the coverage denominator.
- **unknown** — executed but no outcome recorded. Treated as a gap. An executed
  technique with a blank `coverage` becomes `unknown` automatically; you cannot
  leave it off the books.

## How coverage is computed

```
detectable = executed - not-detectable
coverage%  = (covered + partial) / detectable
```

`not-detectable` techniques leave the denominator honestly. The alternative —
counting them as covered to inflate the number, or as failures to deflate it —
is the mistake the whole skill exists to prevent. You report what you can
actually see, over what could actually be seen.

## Why unknown cannot pass

An `unknown` is an executed technique whose detection outcome nobody wrote down.
Allowing it to pass would let an exercise claim coverage it never measured —
the confident-summary-over-an-unanswered-question failure. The scorer treats
`unknown` exactly like `not-detected`: a gap that fails the run until it is
resolved to a real outcome.
