# Severity rubric

Severity = impact × likelihood, argued in one sentence. The table gives the
shape; the examples show the argument.

## Impact tiers

| Tier | Meaning |
| --- | --- |
| Total | Full control of the system, or all data of all users |
| Significant | A large class of data, a privileged action, or persistent access |
| Limited | One user's data, a bounded action, a single-session effect |
| Negligible | No direct effect; informational |

## Likelihood: count the preconditions

Each of these is one precondition. Zero preconditions is the worst case.

- attacker needs an account (free sign-up counts as half; invited-only as one)
- attacker needs a victim to act (click, open, approve)
- attacker needs network position (same LAN, MITM, VPN)
- attacker needs a race or timing window
- attacker needs a non-default configuration

## Mapping

| Impact \ Preconditions | 0 | 1 | 2+ |
| --- | --- | --- | --- |
| Total | Critical | High | Medium |
| Significant | High | Medium | Medium |
| Limited | Medium | Low | Low |
| Negligible | Info | Info | Info |

## Worked examples

**Critical.** "An unauthenticated request to `/api/export` returns every
customer record." Total impact, zero preconditions.

**High.** "A logged-in user can change any other user's email by editing
`user_id` in the profile form." Significant impact (account takeover path),
one precondition (free account).

**Medium.** "Reflected XSS in the search box executes attacker script in the
victim's session." Significant-to-limited impact, one precondition (victim
click) plus the session is the victim's own; lands on Medium unless the
session holds admin rights, in which case High.

**Low.** "Server version is disclosed in the `Server` header." Negligible
direct impact, useful for targeting; Low rather than Info because it
measurably helps a follow-on attack.

**Info.** "Password policy allows 8 characters; policy document says 12."
No demonstrated path; a deviation from stated intent.

## Adjustments, and when they are not allowed

- Raise one tier when the flaw is in a security control itself (auth,
  crypto, isolation), because the blast radius is everything behind it.
- Lower one tier when exploitation is demonstrably bounded by a second,
  independent control you verified, and say which one.
- Never raise severity for "could be chained"; chain it, then rate the chain.
- Never lower severity because the fix is easy, the team is busy, or the
  client would prefer it. Severity describes the flaw; priority is a
  separate conversation.
