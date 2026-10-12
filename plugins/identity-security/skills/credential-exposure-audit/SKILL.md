---
name: credential-exposure-audit
description: "Audits supplied evidence when passwords, hashes, private keys, browser or vault entries, cloud CLI credentials, application secrets, tokens, or credential-bearing artifacts may be exposed. Use for defensive review that must distinguish indicators from material and validity from privilege without decrypting, cracking, replaying, or authenticating."
allowed-tools: Read Grep Glob
---

# Credential exposure audit

A credential-shaped string, record, file, or log entry does not by itself prove
usable material. Keep material presence separate from current validity, identity,
privilege, and reachable systems. Preserve raw values in restricted evidence;
the audit contains redacted references only.

This skill reviews supplied evidence and protection controls. It does not collect
new credential material, decrypt stores, inspect unsupplied memory, crack hashes,
authenticate, replay tokens, test destinations, or plan lateral movement.

## When to Use

- Audit credential exposure for authorized security work.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Record authorization, exact assets, business context, the supplied-evidence
   boundary, restricted evidence location, retention, and disposition owner. Use
   `unknown` or null when a handling fact was not supplied;
   do not invent a vault path, owner, retention period, or asset purpose.
2. Inventory each evidence item with its asset, locator, class, access state,
   protection, integrity hash for copied artifacts, and exact time or honest
   bounded collection window. Never invent acquisition precision or a digest. If
   content is described but no copied artifact and hash were supplied, use the
   matching metadata or configuration evidence kind and state the integrity gap.
   Never use repeated hexadecimal characters as a stand-in digest.
   Do not assign evidence to a host because its content names that host or a URL.
   When the source asset is not supplied, use an `other` asset named
   `Unattributed supplied evidence` and record the provenance gap.
3. Keep raw secrets out of the audit. Use a restricted redacted reference and a
   disposition record for every observed or redacted secret-bearing item.
4. Classify what the evidence establishes: indicator, credential reference,
   protected material, redacted material, direct observation, potential
   container, or expected credential mechanism.
5. Record exposure separately: protected, owner-accessible, broadly accessible,
   historical broad access, unknown, or not an exposure. A variable name, masked
   value, or uninspected dump is not confirmed material exposure.
6. Record freshness, longevity, identity binding, privilege, and reachability as
   separate facts. Mark them verified only from administrative, runtime, or
   configuration evidence; never infer them from a filename, account label, or
   credential format.
7. Bind each protection control to evidence and state its limitation. Encryption,
   file permissions, masking, short lifetime, process protection, and storage ACLs
   reduce different risks and cannot clear unrelated surfaces.
8. Cover memory, local stores, browser and vault data, private keys, cloud caches,
   application configuration, histories and logs, process environments, workload
   identity, retained artifacts, authorization, and handling. Blocked work stays
   visible and receives a reason.
9. Link every medium-or-higher observation to an owned action and verification
    method. Administrative inventory can close identity, validity, privilege, and
    last-use gaps without authenticating with the credential.

## Interpretation rules

- Encrypted material proves a protected object exists. It does not prove
  decryptability, plaintext knowledge, current validity, or successful use.
- Owner-only access limits local readers. It does not establish that the owner is
  uncompromised or that a remote credential is inactive.
- A private-key header proves key material is present only when the supplied
  artifact supports that claim. It does not establish passphrase state, trust
  destinations, or validity.
- A masked CI value or environment-variable name is an indicator. It does not
  prove the underlying value appeared in the evidence.
- An intended short-lived workload token is a mechanism, not a finding. Audience,
  RBAC, runtime issuance, and pod access remain separate questions.
- A crash dump or memory image is a potential container until inspected under
  separate authority. Restricting it does not prove it contains credentials.
- Rotation can be precautionary when validity is unknown. Describe it that way;
  do not rewrite precaution as confirmed compromise.

## Boundary with adjacent skills

- Use `password-audit-plan` for authorized password-strength or cracking policy.
- Use `kerberos-exposure-audit` for directory Kerberos configuration and ticket
  exposure controls.
- Use `cloud-attack-path` after administrative evidence binds a credential to an
  identity and permissions.
- Use `protocol-traffic-analysis` for authentication material observed in packet
  captures.
- Use `findings-report` to turn verified audit observations into final findings.

## Rationalizations to reject

- **"It looks like a credential, so it is valid."** Format establishes neither
  issuance nor current administrative state.
- **"The command names that server, so the history came from it."** A destination
  in evidence is not the source of that evidence. Keep the source unattributed
  until collection provenance binds it.
- **"The username says admin, so the privilege is high."** Names are inferred
  identity and privilege until authoritative records bind them.
- **"The value was masked, so the secret definitely existed."** Masking output can
  be static text; record an indicator until the source is established.
- **"Mode 0600 means there is no exposure."** It limits filesystem readers while
  leaving owner compromise, lifetime, remote permissions, and retention open.
- **"The token expires in an hour, so the workload is safe."** Lifetime does not
  prove audience, RBAC, pod isolation, or absence of theft during that hour.
- **"Rotate everything immediately."** Rotation can disrupt production and destroy
  evidence. Give it an owner, authorization state, reason, and verification method.
- **"The artifact was supplied, so I can add a placeholder hash."** Artifact
  availability and digest availability are separate facts. Record the integrity
  gap unless a digest was supplied or actually computed from the artifact.
- **"We can test it once to learn the scope."** Authentication is a separate action
  with detection, lockout, state-change, and authorization consequences.
