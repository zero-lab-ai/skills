# Detection test record

The JSON `check_detection.py` consumes. One entry per rule; the structure is
the proof that the rule earned deployment.

```json
{
  "rules": [
    {
      "id": "rb-cred-001",
      "attack": "T1003.001",
      "true_positive":  {"tested": true, "fired": true},
      "true_negative":  {"tested": true, "fired": false},
      "fp_rate": 0.02
    }
  ]
}
```

| Field | Proves |
|---|---|
| `id` | which rule; appears in the output so a failure is actionable |
| `attack` | ATT&CK technique. Required — an unmapped rule cannot be placed on a coverage map, so you cannot state what you can and cannot see |
| `true_positive.tested` / `.fired` | the rule was run against a known-bad sample, and it fired. Both must be true |
| `true_negative.tested` / `.fired` | the rule was run against a known-good sample, and it did NOT fire. `tested` true, `fired` false |
| `fp_rate` | optional measured false-positive rate. Over 0.90 the logic is wrong — rewrite, do not tune |

## Why both arms are mandatory

The two arms catch opposite failures and neither covers for the other:

- **No true-positive proof** → the rule may detect nothing. A Sigma rule with a
  typo in the field name is syntactically valid and matches forever-nothing.
- **No true-negative proof** → the rule may fire on everything. That is the
  false-positive storm that produces alert blindness, and alert blindness is how
  the real detection gets ignored.

A rule with only one arm tested is reported unproven, not partially proven.
There is no partial credit: a detection you cannot trust to fire, or cannot
trust to stay quiet, is one you cannot act on.

## What the checker does not do

It does not run your SIEM, execute rules, or judge rule quality. It checks that
the *evidence of testing* exists and is consistent. Producing the samples and
running the rule against them is the engineer's job; recording the outcome
honestly is what this reads. A fabricated record passes the checker and fails
the audit — the checker is a floor, not a substitute for actually testing.
