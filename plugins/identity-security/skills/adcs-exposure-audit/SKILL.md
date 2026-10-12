---
name: adcs-exposure-audit
description: "Audits Active Directory Certificate Services configuration for dangerous certificate templates, PKI ACLs, enrollment interfaces, mapping policy, and identity escalation paths. Use during an authorized identity security review when assessing AD CS, certificate templates, enterprise CAs, or Certipy-style inventory without exercising an attack path."
allowed-tools: Read Grep Glob
---

# AD CS exposure audit

AD CS issues are combinations. A broad enrollment ACL alone may be intended;
the same ACL combined with an authentication purpose, requester-controlled
identity, and weak issuance controls becomes an escalation surface. Record
facts separately and derive the combinations.

## When to Use

- An authorized identity security review when assessing AD CS, certificate templates, enterprise CAs, or Certipy-style inventory without exercising an attack path.
- Use only within explicit authorization and the stated rules of engagement.

## When NOT to Use

- Do not treat this skill as permission to access, test, or change a target.
- Do not convert missing evidence into a clean result or a stronger claim.

## Workflow

1. Confirm the authorized domains, CAs, directory objects, and read-only
   collection actions. Do not request a certificate, relay authentication,
   coerce authentication, modify an object, or attempt certificate logon
   unless those actions are separately authorized.
2. Inventory every enterprise CA and every template it publishes. Record CA
   flags, SID-extension policy, patch state, enrollment interfaces,
   administrative rights, HSM signing controls, and enrollment-agent
   restrictions.
3. Record template publication, schema version, effective enrollment
   principals, subject-supply behavior, EKUs or application policies,
   approval, authorized signatures, SID-extension behavior, and issuance
   policy OIDs. For templates requiring authorized signatures, record the
   required registration-authority application policies.
4. Record effective ACLs on templates, CA configuration, NTAuthCertificates,
   enrollment services, CA computer objects, and OID objects. Resolve nested
   membership before calling a principal low privilege.
5. Record certificate mapping on every relevant domain controller and
   certificate-authenticating service. Include strong binding mode, enabled
   Schannel mapping methods, and explicit `altSecurityIdentities` mappings.

## Interpretation rules

- Treat template, CA, network, mapping, and directory-control findings as
  separate claims even when they form one path.
- Strong KDC mapping can block a specific arbitrary-identity path while the
  source template remains dangerously broad for other certificate consumers.
- HTTPS alone does not resolve NTLM relay exposure. Record Extended Protection
  and channel-binding enforcement.
- A missing SID extension is a configuration exposure. Its exploitation path
  still depends on mapping policy or another identity-injection condition.
- `ManageCA`, certificate-manager rights, template control, and PKI-object
  control are not interchangeable; report the authority actually observed.
- Absence from the supplied inventory is unknown, not clean.

## Rationalizations to reject

- **"Certipy did not label it vulnerable."** Tool labels cannot replace the
  underlying template, ACL, CA, mapping, and endpoint facts.
- **"Full enforcement makes subject supply harmless."** It constrains KDC
  mapping; other certificate consumers and chained configuration changes
  remain in scope.
- **"The right is expected, so it is safe."** Expected Tier Zero authority
  still needs an accountable owner and evidence. Low-privilege authority is
  an exposure regardless of intent.
- **"We can prove it by requesting one certificate."** A configuration audit
  does not create credentials or exercise identity paths without separate
  authorization.
- **"ESC numbering is the finding."** Describe the actual control failure and
  conditions; catalogs evolve.
