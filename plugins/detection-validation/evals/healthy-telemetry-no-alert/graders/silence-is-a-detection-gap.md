---
type: llm
focus: last_message
weight: 1
---

Pass if the response assigns `not-detected`, cites the successful execution,
present telemetry, healthy collector, and complete no-alert query, and treats
the repository rule as insufficient proof. It should preserve a follow-up gap
rather than reinterpret the technique as benign.

Fail if it marks covered, partial, unknown, or not-detectable; blames missing
telemetry contradicted by the scenario; or counts the rule's existence as a
detection outcome.
