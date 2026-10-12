# Network and Protocol Security

Planning and evidence-analysis skills for wireless systems, packet captures,
protocol weaknesses, command channels, and bounded synthetic egress tests. The
bundle keeps route feasibility, reproduced behavior, visibility, detection,
and cleanup as separate claims.

## Skills

| Skill | Use it when… |
| --- | --- |
| [`wireless-assessment-plan`](skills/wireless-assessment-plan/SKILL.md) | Planning authorized Wi-Fi, Bluetooth, RFID/NFC, SDR, or other radio testing |
| [`protocol-traffic-analysis`](skills/protocol-traffic-analysis/SKILL.md) | Turning supplied captures into evidence-bound conversations and limitations |
| [`protocol-exploitation-assessment`](skills/protocol-exploitation-assessment/SKILL.md) | Dispositioning protocol candidates without promoting weak signals into vulnerabilities |
| [`covert-channel-assessment`](skills/covert-channel-assessment/SKILL.md) | Measuring whether bounded synthetic channels are blocked, visible, detected, and cleaned up |
| [`command-channel-defense-assessment`](skills/command-channel-defense-assessment/SKILL.md) | Measuring defensive coverage against opaque command-channel scenarios |

## Install

```text
/plugin install network-protocol-security@zero-lab
```

Each skill folder remains independently portable to any harness that reads
`SKILL.md`.

## License

[Apache License 2.0](../../LICENSE)
