Read `AGENTS.md` before making changes. It contains the complete,
validator-enforced authoring and release rules for this repository.

Repository rules:
- No AI attribution: no Co-Authored-By or Claude-Session trailers in commits, no "Generated with" lines in PR descriptions.
- Run `make check` before every commit. Never loosen the validator to make a skill pass.
- Keep plugin packaging thin and keep each `SKILL.md` usable from its own skill folder.
