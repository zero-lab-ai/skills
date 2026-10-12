# Scope and authorization

## Record it before the first packet

Write the authorized scope down where the work happens, not in memory:

- target ranges, in CIDR or explicit host list
- excluded hosts inside those ranges
- permitted techniques, and any that are explicitly out of bounds
- the time window
- who authorized it, and when

If any line is unknown, that is the first question to ask, not an assumption
to make.

An authorized range is the maximum permitted boundary. It is not automatically
the requested target set. If the operator supplies an explicit host list inside
that range, preserve that list and do not add other authorized addresses without
a request that names them.

## Refuse out of scope, every time

A target adjacent to scope is out of scope. "Same /16", "it's clearly theirs",
and "it resolved from an in-scope host" are not authorizations. Shared hosting
and cloud ranges make the adjacent-address assumption actively dangerous: the
next address can belong to someone who never agreed to anything.

When asked to exceed scope, say what is out of scope and what it would take to
bring it in. Do not quietly widen a range.

## Discovery that expands scope

Recon finds things scope did not anticipate — a trust relationship to an
unlisted domain, a host answering on an address nobody documented. The finding
is reportable. The new target is not in scope until someone says it is.

## Noise is a scope question too

Scan pacing and technique affect the target's availability and its monitoring.
A scan rate that degrades a production service is an impact even when no
exploit ran. State the expected noise and get it confirmed when the target is
production.
