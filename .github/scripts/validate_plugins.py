#!/usr/bin/env python3
"""Validate marketplace plugins, skills, interfaces, and portable paths."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
HOME_PATH = re.compile(r"(?<![\w.])/(?:Users|home)/(?!vscode\b)[A-Za-z0-9_.-]+")
LEGACY_PY = re.compile(r"(?<![\w/-])(?:python3?\s+\S+\.py|pip install|python3?\s+-m\s+pip)\b")
MD_LINK = re.compile(r"\]\(([^)#?\s]+)")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checked_plugins: int = 0
    checked_skills: int = 0

    def err(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 4 :]


def scalar(block: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", block)
    if not match:
        return None
    value = match.group(1).strip()
    if value[:1] in {'"', "'"} and value[-1:] == value[:1]:
        value = value[1:-1]
    return value


def unquoted_scalar_hazards(block: str) -> list[str]:
    hazards: list[str] = []
    for raw in block.splitlines():
        if not raw or raw.startswith((" ", "#")) or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        value = value.strip()
        if value and not value.startswith(('"', "'", "[")) and (": " in value or " #" in value):
            hazards.append(key.strip())
    return hazards


def check_interface(skill_dir: Path, tag: str, rep: Report) -> None:
    interface = skill_dir / "agents" / "openai.yaml"
    if not interface.exists():
        rep.err(f"{tag}: agents/openai.yaml missing")
        return
    text = interface.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "icon_small", "icon_large", "brand_color"):
        if not re.search(rf"(?m)^\s{{2}}{key}:\s*.+$", text):
            rep.err(f"{tag}: agents/openai.yaml missing interface.{key}")
    short = re.search(r'(?m)^\s{2}short_description:\s*["\']?(.+?)["\']?\s*$', text)
    if short:
        value = short.group(1).strip().strip("\"'")
        if not 25 <= len(value) <= 64:
            rep.err(f"{tag}: interface.short_description must be 25-64 characters")
    for key in ("icon_small", "icon_large"):
        value = scalar(text.replace("  ", ""), key)
        if value and not (skill_dir / value).exists():
            rep.err(f"{tag}: interface.{key} path {value!r} does not resolve")


def check_skill(skill_dir: Path, plugin_name: str, rep: Report) -> None:
    rep.checked_skills += 1
    tag = f"{plugin_name}/skills/{skill_dir.name}"
    path = skill_dir / "SKILL.md"
    if not path.exists():
        rep.err(f"{tag}: SKILL.md missing")
        return
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        rep.err(f"{tag}: SKILL.md has no valid frontmatter")
        return
    for key in unquoted_scalar_hazards(frontmatter):
        rep.err(f"{tag}: frontmatter key `{key}` contains an unquoted YAML hazard")
    name = scalar(frontmatter, "name")
    description = scalar(frontmatter, "description")
    if name != skill_dir.name:
        rep.err(f"{tag}: frontmatter name {name!r} != directory {skill_dir.name!r}")
    if not isinstance(name, str) or not KEBAB.match(name) or len(name) > 64:
        rep.err(f"{tag}: name must be kebab-case and <=64 characters")
    if not description or len(description) < 20:
        rep.err(f"{tag}: description missing or too short")
    if re.search(r"(?m)^tools:", frontmatter):
        rep.err(f"{tag}: skills use `allowed-tools`, not `tools`")
    if "## When to Use" not in body:
        rep.err(f"{tag}: missing `## When to Use`")
    if "## When NOT to Use" not in body:
        rep.err(f"{tag}: missing `## When NOT to Use`")
    if not re.search(r"(?mi)^## Rationalizations to reject\s*$", body):
        rep.err(f"{tag}: missing `## Rationalizations to reject`")
    if text.count("\n") + 1 > 500:
        rep.warn(f"{tag}: SKILL.md exceeds 500 lines; use progressive disclosure")

    for file in skill_dir.rglob("*"):
        if file.is_dir() or file.suffix not in {
            ".md",
            ".py",
            ".json",
            ".sh",
            ".yml",
            ".yaml",
            ".toml",
            ".txt",
            ".svg",
        }:
            continue
        content = file.read_text(encoding="utf-8", errors="replace")
        hit = HOME_PATH.search(content)
        if hit:
            rep.err(f"{tag}: hardcoded home path {hit.group(0)!r} in {file.relative_to(skill_dir)}")
        if file.suffix == ".md":
            legacy = LEGACY_PY.search(content)
            if legacy:
                rep.err(
                    f"{tag}: legacy Python invocation {legacy.group(0)!r}; "
                    "use `uv run {baseDir}/scripts/...`"
                )
    for link in MD_LINK.findall(body):
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        target = skill_dir / link
        if not target.exists():
            rep.warn(f"{tag}: reference {link!r} does not resolve")
    check_interface(skill_dir, tag, rep)


def check_plugin(
    plugin_dir: Path, marketplace: dict, root_readme: str, codeowners: str, rep: Report
) -> None:
    rep.checked_plugins += 1
    name = plugin_dir.name
    tag = f"plugins/{name}"
    if not KEBAB.match(name) or len(name) > 64:
        rep.err(f"{tag}: directory name must be kebab-case and <=64 characters")

    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    manifest: dict = {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        rep.err(f"{tag}: plugin.json unreadable: {exc}")
    for key in ("name", "version", "description", "author"):
        if key not in manifest:
            rep.err(f"{tag}: plugin.json missing `{key}`")
    if manifest.get("name") != name:
        rep.err(f"{tag}: plugin.json name {manifest.get('name')!r} != directory {name!r}")
    if not SEMVER.match(str(manifest.get("version", ""))):
        rep.err(f"{tag}: plugin.json version must be semver")

    for component in ("skills", "commands", "agents", "hooks", "workflows"):
        if (plugin_dir / ".claude-plugin" / component).exists():
            rep.err(f"{tag}: `{component}/` must be at the plugin root")
    for sidecar in (".codex", ".codex-plugin", ".opencode", ".agents"):
        if (plugin_dir / sidecar).exists():
            rep.err(f"{tag}: vendor sidecar `{sidecar}/` is not allowed")
    if not (plugin_dir / "README.md").exists():
        rep.err(f"{tag}: README.md missing")

    entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == name]
    if len(entries) != 1:
        rep.err(f"{tag}: expected one marketplace entry, found {len(entries)}")
    else:
        entry = entries[0]
        if entry.get("source") != f"./plugins/{name}":
            rep.err(f"{tag}: marketplace source is incorrect")
        for key in ("version", "description", "author"):
            if entry.get(key) != manifest.get(key):
                rep.err(f"{tag}: marketplace `{key}` differs from plugin.json")
    if f"plugins/{name})" not in root_readme and f"plugins/{name}/" not in root_readme:
        rep.err(f"{tag}: not linked from root README")
    if not re.search(rf"(?m)^/plugins/{re.escape(name)}/\s+@\S+", codeowners):
        rep.err(f"{tag}: no CODEOWNERS entry")

    skills = (
        sorted((plugin_dir / "skills").glob("*/SKILL.md"))
        if (plugin_dir / "skills").exists()
        else []
    )
    if not skills:
        rep.err(f"{tag}: no skills found")
    for skill in skills:
        check_skill(skill.parent, name, rep)

    for script in plugin_dir.rglob("*.sh"):
        content = script.read_text(encoding="utf-8", errors="replace")
        if "set -euo pipefail" not in content:
            rep.err(f"{tag}: {script.relative_to(plugin_dir)} lacks `set -euo pipefail`")
        if re.search(r"\bgrep\s+(-[a-zA-Z]*P|--perl-regexp)", content):
            rep.err(f"{tag}: {script.relative_to(plugin_dir)} uses non-portable grep -P")


def validate(root: Path) -> Report:
    rep = Report()
    marketplace_path = root / ".claude-plugin" / "marketplace.json"
    try:
        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        rep.err(f"marketplace unreadable: {exc}")
        marketplace = {}
    root_readme = (
        (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else ""
    )
    codeowners = (
        (root / "CODEOWNERS").read_text(encoding="utf-8") if (root / "CODEOWNERS").exists() else ""
    )
    plugins_dir = root / "plugins"
    plugins = (
        sorted(path for path in plugins_dir.iterdir() if path.is_dir())
        if plugins_dir.exists()
        else []
    )
    for plugin in plugins:
        check_plugin(plugin, marketplace, root_readme, codeowners, rep)
    for entry in marketplace.get("plugins", []):
        if not (plugins_dir / str(entry.get("name"))).is_dir():
            rep.err(f"marketplace lists missing plugin {entry.get('name')!r}")
    if rep.checked_plugins == 0:
        rep.err("validator inspected zero plugins")
    if rep.checked_skills == 0:
        rep.err("validator inspected zero skills")
    return rep


def self_test() -> int:
    root = Path(tempfile.mkdtemp(prefix="zl-validator-selftest-"))
    try:
        (root / ".claude-plugin").mkdir()
        (root / ".claude-plugin" / "marketplace.json").write_text(
            json.dumps({"plugins": [{"name": "ghost"}]})
        )
        (root / "README.md").write_text("# Empty\n")
        (root / "CODEOWNERS").write_text("")
        plugin = root / "plugins" / "BadPlugin"
        skill = plugin / "skills" / "bad-skill"
        (plugin / ".claude-plugin" / "skills").mkdir(parents=True)
        skill.mkdir(parents=True)
        (plugin / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"name": "other", "version": "x"})
        )
        (skill / "SKILL.md").write_text(
            "---\nname: wrong\ndescription: Bad: value\ntools: Read\n---\n"
            "# Bad\n\nSee [missing](references/nope.md). Output to /Users/pete/x.\n"
        )
        tests = plugin / "tests"
        tests.mkdir()
        (tests / "bad.sh").write_text("grep -P x file\n")
        report = validate(root)
        expected = [
            "kebab-case",
            "missing `description`",
            "plugin.json name",
            "version must be semver",
            "must be at the plugin root",
            "README.md missing",
            "expected one marketplace entry",
            "not linked from root README",
            "no CODEOWNERS entry",
            "unquoted YAML hazard",
            "frontmatter name",
            "skills use `allowed-tools`",
            "missing `## When to Use`",
            "missing `## When NOT to Use`",
            "missing `## Rationalizations to reject`",
            "hardcoded home path",
            "agents/openai.yaml missing",
            "lacks `set -euo pipefail`",
            "grep -P",
            "marketplace lists missing plugin",
        ]
        missed = [
            needle for needle in expected if not any(needle in error for error in report.errors)
        ]
        if not any("does not resolve" in warning for warning in report.warnings):
            missed.append("unresolved reference warning")
        print(f"self-test: {len(expected) + 1} assertions, {len(report.errors)} errors")
        if missed:
            for item in missed:
                print(f"  MISSED: {item}")
            return 1
        empty = Path(tempfile.mkdtemp(prefix="zl-validator-empty-"))
        try:
            empty_report = validate(empty)
            if not any("zero plugins" in error for error in empty_report.errors):
                print("  MISSED: empty repository did not fail")
                return 1
        finally:
            shutil.rmtree(empty, ignore_errors=True)
        print("self-test: ok")
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    report = validate(args.root)
    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"error: {error}")
    print(
        f"checked {report.checked_plugins} plugins, {report.checked_skills} skills: "
        f"{len(report.errors)} errors, {len(report.warnings)} warnings"
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
