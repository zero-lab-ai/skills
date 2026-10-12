# Application and Endpoint Security

Assessment-coverage skills for cloud, web, mobile, firmware, endpoint
persistence, and offline password auditing. Install this bundle when the
deliverable depends on showing what was tested, what was blocked, and what
evidence supports each conclusion.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`cloud-attack-path`](skills/cloud-attack-path/SKILL.md) | Mapping cloud identity, workload, credential, and trust transitions |
| [`web-assessment-coverage`](skills/web-assessment-coverage/SKILL.md) | Tracking web surfaces, roles, states, and test-family coverage |
| [`mobile-application-assessment`](skills/mobile-application-assessment/SKILL.md) | Tracking Android and iOS assessment coverage |
| [`firmware-hardware-assessment`](skills/firmware-hardware-assessment/SKILL.md) | Assessing device identity, firmware acquisition, update trust, and physical safety |
| [`persistence-surface-assessment`](skills/persistence-surface-assessment/SKILL.md) | Measuring Windows and Linux persistence exposure from supplied evidence |
| [`password-audit-plan`](skills/password-audit-plan/SKILL.md) | Planning bounded offline password audits and restricted result handling |

## Install

```text
/plugin install application-endpoint-security@zero-lab
```

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## License

[Apache License 2.0](../../LICENSE)
