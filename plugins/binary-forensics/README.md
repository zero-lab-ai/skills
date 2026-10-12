# Binary and Forensics

Evidence-led triage for binary faults, volatile memory, suspected rootkits, and
the governance boundary before separate isolated validation. These skills do
not execute samples, develop exploits, or turn triage evidence into operational
instructions.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`binary-fault-triage`](skills/binary-fault-triage/SKILL.md) | Triaging supplied binary fault evidence without execution or weaponization |
| [`binary-fault-validation-readiness`](skills/binary-fault-validation-readiness/SKILL.md) | Checking whether fault evidence is ready for separate isolated validation |
| [`memory-forensics-triage`](skills/memory-forensics-triage/SKILL.md) | Triaging supplied volatile-memory images while preserving evidentiary limits |
| [`rootkit-triage`](skills/rootkit-triage/SKILL.md) | Triaging suspected rootkits or bootkits with independent evidence views |

## Install

```text
/plugin install binary-forensics@zero-lab
```

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## License

[Apache License 2.0](../../LICENSE)
