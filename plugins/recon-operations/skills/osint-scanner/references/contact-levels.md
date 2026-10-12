# Contact levels

`scripts/check_passive.py` classifies every planned action into one of three
levels. Contact is the single fact that decides whether OSINT stayed passive.

| Level | Meaning | Examples |
|---|---|---|
| `none` | A third party already did the looking; you read their result. Zero packets reach the target. | Shodan, Censys, crt.sh, DeHashed, BuiltWith, Hunter, Google dorking, amass passive, dig against a public resolver cache |
| `target` | Traffic reaches infrastructure the target controls or monitors. | httpx/whatweb/Wappalyzer against the site, dig against the target's authoritative NS, amass active/brute, theHarvester active resolution, any port scanner |
| `unknown` | Tool or mode not in the contact map. | anything unclassified |

## Why `unknown` fails a passive plan

An unexamined action is not a safe action. In a passive plan the checker treats
`unknown` exactly like `target` and fails, because the cost of being wrong is
detection. Classify the tool — add it to the map in `check_passive.py` with a
one-line reason — and run again. Failing closed is the correct default when the
downside is getting caught.

## Dual-mode tools

Several tools are passive or active depending on how they are run. The checker
resolves them only when a `mode` is given:

| Tool | passive mode | active mode |
|---|---|---|
| `amass` | `passive` / `enum` → none | `active` / `brute` → target |
| `theharvester` | `passive` → none | `active` → target |
| `subfinder` | `passive` → none | `resolve` → target |
| `dig` | `cache` → none | `authoritative` → target |

A dual-mode tool with no mode declared is reported `unknown`, which fails a
passive plan. State the mode; do not let the default decide for you.

## Plan format

```json
{
  "stealth": "passive",
  "target": "example.com",
  "actions": [
    {"tool": "crtsh", "note": "subdomains from CT logs"},
    {"tool": "amass", "mode": "passive"},
    {"tool": "dig", "mode": "cache", "note": "MX/TXT"}
  ]
}
```

Set `stealth` to `target-contact-authorized` only when the rules of engagement
permit touching the target. That flag is a decision with a consequence, not a
way to silence the check.
