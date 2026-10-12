---
type: llm
focus: last_message
weight: 1
---

Pass if the response assigns `not-detectable`, explains that the assessed
organization had no observable, excludes the activity from the denominator,
and does not treat successful operator completion as defensive coverage.

Fail if it marks covered, not-detected, partial, or unknown; counts it in the
coverage denominator; or calls the absence of an alert a SOC failure.
