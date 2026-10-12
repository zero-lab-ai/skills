RUFF_VERSION := 0.14.13
RUFF ?= uvx ruff@$(RUFF_VERSION)

.DEFAULT_GOAL := check
.NOTPARALLEL:
.PHONY: check self-test validate lint shell shell-suites fix help

PY := python3 -I

help:
	@echo "check        run everything CI runs locally"
	@echo "self-test    prove the validator rejects a known-bad plugin"
	@echo "validate     validate every plugin"
	@echo "lint         ruff check + format"
	@echo "shell        shellcheck + shfmt"
	@echo "shell-suites run plugins/*/tests/run_*.sh"
	@echo "fix          apply formatting"

check: self-test validate lint shell shell-suites
	@echo ""
	@echo "✓ check passed — CI-only loadability and version-increment checks remain"

self-test:
	$(PY) .github/scripts/validate_plugins.py --self-test

validate:
	$(PY) .github/scripts/validate_plugins.py

lint:
	@echo "→ ruff check"
	@$(RUFF) check --output-format=concise
	@echo "→ ruff format --check"
	@$(RUFF) format --check

shell:
	@echo "→ shellcheck"
	@find plugins .github/scripts -name '*.sh' -type f -exec shellcheck -x {} +
	@echo "→ shfmt"
	@find plugins .github/scripts -name '*.sh' -type f -exec shfmt -i 2 -ci -d {} +

shell-suites:
	@set -e; for s in plugins/*/tests/run_*.sh; do [ -e "$$s" ] || continue; echo "== $$s"; bash "$$s"; done

fix:
	@$(RUFF) format .
	@$(RUFF) check --fix .
	@find plugins .github/scripts -name '*.sh' -type f -exec shfmt -i 2 -ci -w {} +
