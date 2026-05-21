#!/usr/bin/env python3
"""Validate the Codex Agent Skills plugin shape."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY_SKILLS = {
    "spec",
    "plan",
    "build",
    "test",
    "review",
    "code-simplify",
    "ship",
    "product-discovery",
    "founder-review",
    "business-model-review",
    "design-plan-review",
    "qa",
    "health-check",
    "retro",
    "learn",
}
LIBRARY_SKILLS = {
    "using-agent-skills",
    "interview-me",
    "idea-refine",
    "spec-driven-development",
    "planning-and-task-breakdown",
    "incremental-implementation",
    "test-driven-development",
    "context-engineering",
    "source-driven-development",
    "doubt-driven-development",
    "frontend-ui-engineering",
    "api-and-interface-design",
    "browser-testing-with-devtools",
    "debugging-and-error-recovery",
    "code-review-and-quality",
    "code-simplification",
    "security-and-hardening",
    "performance-optimization",
    "git-workflow-and-versioning",
    "ci-cd-and-automation",
    "deprecation-and-migration",
    "documentation-and-adrs",
    "shipping-and-launch",
    "founder-product-critique",
    "business-model-evaluation",
    "live-qa-methodology",
}
REQUIRED_REFERENCES = {
    "accessibility-checklist.md",
    "performance-checklist.md",
    "security-checklist.md",
    "testing-patterns.md",
    "product-discovery-checklist.md",
    "business-model-checklist.md",
    "design-quality-checklist.md",
    "qa-checklist.md",
}
REQUIRED_PERSONAS = {
    "code-reviewer.md",
    "security-auditor.md",
    "test-engineer.md",
}


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def resolve_plugin_path(value: str) -> Path:
    if not value.startswith("./"):
        fail(f"Manifest path must be relative and start with ./, got {value!r}")
    return (ROOT / value[2:]).resolve()


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} must start with YAML frontmatter")

    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} is missing closing frontmatter marker")

    raw = text[4:end].strip()
    body = text[end + len("\n---") :].strip()
    metadata: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith(" ") or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"'")
    return metadata, body


def validate_manifest() -> None:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)

    if manifest.get("name") != ROOT.name:
        fail("Manifest name must match the plugin folder name")
    if manifest.get("skills") != "./skills/":
        fail('Manifest must set "skills" to "./skills/"')
    if manifest.get("license") != "MIT":
        fail('Public plugin manifest must set "license" to "MIT"')
    if not (ROOT / "LICENSE").is_file():
        fail("Public plugin must include a root LICENSE file")

    skills_dir = resolve_plugin_path(manifest["skills"])
    if not skills_dir.is_dir():
        fail("Manifest skills path does not exist")

    for key in ("hooks", "mcpServers", "apps"):
        if key in manifest:
            target = resolve_plugin_path(str(manifest[key]))
            if not target.exists():
                fail(f"Manifest {key} path does not exist: {manifest[key]}")

    prompts = manifest.get("interface", {}).get("defaultPrompt", [])
    if len(prompts) > 3:
        fail("interface.defaultPrompt must contain at most 3 prompts")
    for prompt in prompts:
        if len(prompt) > 128:
            fail(f"interface.defaultPrompt entry is over 128 characters: {prompt!r}")


def validate_marketplace() -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    marketplace = load_json(path)
    if marketplace.get("name") != ROOT.name:
        fail("Marketplace name must match the plugin name")

    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        fail("Marketplace must contain at least one plugin entry")

    matching = [entry for entry in entries if entry.get("name") == ROOT.name]
    if len(matching) != 1:
        fail("Marketplace must contain exactly one codex-agent-skills entry")

    entry = matching[0]
    if entry.get("source", {}).get("source") != "local":
        fail("Marketplace entry source must be local")
    if entry.get("source", {}).get("path") != ".":
        fail('Marketplace entry source.path must be "." for this repo-root marketplace')
    if entry.get("policy", {}).get("installation") != "AVAILABLE":
        fail("Marketplace installation policy must be AVAILABLE")
    if entry.get("policy", {}).get("authentication") != "ON_INSTALL":
        fail("Marketplace authentication policy must be ON_INSTALL")
    if not entry.get("category"):
        fail("Marketplace entry must include a category")


def validate_skill(path: Path) -> None:
    metadata, body = parse_frontmatter(path)
    rel = path.relative_to(ROOT)
    skill_dir = path.parent.name

    if metadata.get("name") != skill_dir:
        fail(f"{rel} frontmatter name must match directory name {skill_dir!r}")
    description = metadata.get("description", "")
    if not description or len(description) < 30:
        fail(f"{rel} must include a useful description")
    if "[TODO" in body or "[TODO" in description:
        fail(f"{rel} contains unresolved TODO placeholder text")
    if len(body.split()) < 25:
        fail(f"{rel} body is too short to be a useful workflow")

    if skill_dir in ENTRY_SKILLS:
        for heading in ("## Purpose", "## Workflow", "## Verification"):
            if heading not in body:
                fail(f"{rel} entry skill is missing {heading}")
        if "## Stop Conditions" not in body:
            fail(f"{rel} entry skill is missing ## Stop Conditions")
        if len(body.splitlines()) > 180:
            fail(f"{rel} entry skill is too large; keep command skills thin")


def validate_skills() -> None:
    skills_dir = ROOT / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    names = {path.parent.name for path in skill_files}

    missing = sorted((ENTRY_SKILLS | LIBRARY_SKILLS) - names)
    if missing:
        fail(f"Missing required skills: {', '.join(missing)}")

    for path in skill_files:
        validate_skill(path)

    duplicate_names = [
        name for name in names if len(list(skills_dir.glob(f"{re.escape(name)}/SKILL.md"))) > 1
    ]
    if duplicate_names:
        fail(f"Duplicate skill names found: {', '.join(sorted(duplicate_names))}")


def validate_support_files() -> None:
    references_dir = ROOT / "references"
    missing_refs = sorted(
        name for name in REQUIRED_REFERENCES if not (references_dir / name).is_file()
    )
    if missing_refs:
        fail(f"Missing required references: {', '.join(missing_refs)}")

    agents_dir = ROOT / "agents"
    missing_personas = sorted(
        name for name in REQUIRED_PERSONAS if not (agents_dir / name).is_file()
    )
    if missing_personas:
        fail(f"Missing required personas: {', '.join(missing_personas)}")


def main() -> int:
    checks = (validate_manifest, validate_marketplace, validate_skills, validate_support_files)
    try:
        for check in checks:
            check()
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("OK: plugin shape is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
