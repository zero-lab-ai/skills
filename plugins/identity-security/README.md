# Identity Security

Identity and directory-security skills spanning Active Directory, AD CS,
Kerberos, credentials, privilege escalation, lateral movement, and durable
directory exposure. The bundle separates structural reachability, usable
access, authorization, validation, and demonstrated impact.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`active-directory-attack-path`](skills/active-directory-attack-path/SKILL.md) | Analyzing evidence-backed AD paths and remediation coverage |
| [`adcs-exposure-audit`](skills/adcs-exposure-audit/SKILL.md) | Auditing certificate templates, CA policy, enrollment, mapping, and PKI ACLs |
| [`kerberos-exposure-audit`](skills/kerberos-exposure-audit/SKILL.md) | Auditing supplied Kerberos policy, protection, and monitoring evidence |
| [`directory-persistence-audit`](skills/directory-persistence-audit/SKILL.md) | Auditing directory-service governance for durable-control exposure |
| [`credential-exposure-audit`](skills/credential-exposure-audit/SKILL.md) | Reviewing supplied credential evidence without using the material |
| [`privilege-escalation-assessment`](skills/privilege-escalation-assessment/SKILL.md) | Ranking elevation paths without overstating achieved privilege |
| [`lateral-movement-map`](skills/lateral-movement-map/SKILL.md) | Mapping movement routes without confusing reachability with access |
| [`lateral-movement-readiness`](skills/lateral-movement-readiness/SKILL.md) | Reviewing candidates before a separate validation handoff |

## Install

```text
/plugin install identity-security@zero-lab
```

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## License

[Apache License 2.0](../../LICENSE)
