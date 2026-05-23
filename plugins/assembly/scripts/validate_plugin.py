#!/usr/bin/env python3
"""Validate the Assembly plugin shape."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = (
    PLUGIN_ROOT.parents[1]
    if PLUGIN_ROOT.parent.name == "plugins"
    else PLUGIN_ROOT
)
PLUGIN_NAME = PLUGIN_ROOT.name
PUBLIC_SKILLS = {
    "next",
    "spec",
    "plan",
    "build",
    "test",
    "review",
    "code-simplify",
    "ship",
    "product-discovery",
    "qa",
    "prototype",
    "project-status",
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
    "project-phases.md",
    "project-kernel-structure.md",
    "matt-pocock-skills-notes.md",
    "hyper-project-notes.md",
    "agent-operating-protocol.md",
    "workflows/project-lifecycle.md",
    "workflows/product-strategy.md",
    "workflows/engineering-delivery.md",
    "workflows/qa-and-release.md",
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
        fail(f"Missing required file: {rel(path)}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {rel(path)}: {exc}")


def rel(path: Path) -> str:
    for root in (PLUGIN_ROOT, REPO_ROOT):
        try:
            return str(path.relative_to(root))
        except ValueError:
            continue
    return str(path)


def resolve_plugin_path(value: str) -> Path:
    if not value.startswith("./"):
        fail(f"Manifest path must be relative and start with ./, got {value!r}")
    return (PLUGIN_ROOT / value[2:]).resolve()


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{rel(path)} must start with YAML frontmatter")

    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{rel(path)} is missing closing frontmatter marker")

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
    manifest_path = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)

    if manifest.get("name") != PLUGIN_NAME:
        fail("Manifest name must match the plugin folder name")
    if manifest.get("skills") != "./skills/":
        fail('Manifest must set "skills" to "./skills/"')
    if manifest.get("license") != "MIT":
        fail('Public plugin manifest must set "license" to "MIT"')
    if not (PLUGIN_ROOT / "LICENSE").is_file():
        fail("Public plugin bundle must include a LICENSE file")

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
    path = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
    marketplace = load_json(path)
    if marketplace.get("name") != PLUGIN_NAME:
        fail("Marketplace name must match the plugin name")

    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        fail("Marketplace must contain at least one plugin entry")

    matching = [entry for entry in entries if entry.get("name") == PLUGIN_NAME]
    if len(matching) != 1:
        fail(f"Marketplace must contain exactly one {PLUGIN_NAME} entry")

    entry = matching[0]
    if entry.get("source", {}).get("source") != "local":
        fail("Marketplace entry source must be local")
    expected_path = f"./plugins/{PLUGIN_NAME}"
    if entry.get("source", {}).get("path") != expected_path:
        fail(f'Marketplace entry source.path must be "{expected_path}"')
    if entry.get("policy", {}).get("installation") != "AVAILABLE":
        fail("Marketplace installation policy must be AVAILABLE")
    if entry.get("policy", {}).get("authentication") != "ON_INSTALL":
        fail("Marketplace authentication policy must be ON_INSTALL")
    if not entry.get("category"):
        fail("Marketplace entry must include a category")


def validate_skill(path: Path) -> None:
    metadata, body = parse_frontmatter(path)
    rel_path = rel(path)
    skill_dir = path.parent.name

    if metadata.get("name") != skill_dir:
        fail(f"{rel_path} frontmatter name must match directory name {skill_dir!r}")
    description = metadata.get("description", "")
    if not description or len(description) < 30:
        fail(f"{rel_path} must include a useful description")
    if len(description.split()) > 45:
        fail(f"{rel_path} description is too broad; keep trigger text concise")
    if "[TODO" in body or "[TODO" in description:
        fail(f"{rel_path} contains unresolved TODO placeholder text")
    if len(body.split()) < 25:
        fail(f"{rel_path} body is too short to be a useful workflow")

    for heading in ("## Purpose", "## References", "## Workflow", "## Verification"):
        if heading not in body:
            fail(f"{rel_path} public skill is missing {heading}")
    if "## Stop Conditions" not in body:
        fail(f"{rel_path} public skill is missing ## Stop Conditions")
    if "## Underlying skills" in body:
        fail(f"{rel_path} must use references, not triggerable underlying skills")
    if len(body.splitlines()) > 120:
        fail(f"{rel_path} is too large; keep public skills thin")


def validate_skills() -> None:
    skills_dir = PLUGIN_ROOT / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    names = {path.parent.name for path in skill_files}

    missing = sorted(PUBLIC_SKILLS - names)
    if missing:
        fail(f"Missing required skills: {', '.join(missing)}")

    unexpected = sorted(names - PUBLIC_SKILLS)
    if unexpected:
        fail(f"Unexpected triggerable skills: {', '.join(unexpected)}")

    for path in skill_files:
        validate_skill(path)

    duplicate_names = [
        name for name in names if len(list(skills_dir.glob(f"{re.escape(name)}/SKILL.md"))) > 1
    ]
    if duplicate_names:
        fail(f"Duplicate skill names found: {', '.join(sorted(duplicate_names))}")


def validate_support_files() -> None:
    references_dir = PLUGIN_ROOT / "references"
    missing_refs = sorted(name for name in REQUIRED_REFERENCES if not (references_dir / name).is_file())
    if missing_refs:
        fail(f"Missing required references: {', '.join(missing_refs)}")

    for path in sorted(references_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        rel_path = rel(path)
        if len(text.splitlines()) > 100 and "## Contents" not in text and "## Table of Contents" not in text:
            fail(f"{rel_path} is over 100 lines and must include a ## Contents section")

    install_text = (PLUGIN_ROOT / "docs" / "INSTALL.md").read_text(encoding="utf-8")
    for required in (
        "Existing Skill Conflicts",
        "Replacing A Loose Skill Set",
        "disable",
        "rename",
        "entry skills",
        "next",
        "spec",
        "plan",
        "build",
        "test",
        "review",
        "ship",
    ):
        if required not in install_text:
            fail(f"docs/INSTALL.md must document skill-conflict guidance: {required}")

    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    if "de-duplicate" not in readme_text or "lifecycle" not in readme_text:
        fail("README.md must include lifecycle de-duplication guidance")
    for required in (
        "explicit user authorization",
        "unresolved review threads",
    ):
        if required not in readme_text:
            fail(f"README.md must document GitHub handoff behavior: {required}")

    command_contract_text = (PLUGIN_ROOT / "docs" / "COMMAND_CONTRACT.md").read_text(encoding="utf-8")
    for required in (
        "ask before ready-for-review",
        "PR review feedback",
        "explicit user authorization",
    ):
        if required not in command_contract_text:
            fail(f"docs/COMMAND_CONTRACT.md must document GitHub handoff behavior: {required}")

    template_text = (PLUGIN_ROOT / "templates" / "AGENTS.md").read_text(encoding="utf-8")
    if "Assembly" not in template_text or "lifecycle" not in template_text:
        fail("templates/AGENTS.md must identify Assembly as lifecycle owner")
    if ".agents/AGENT-GUIDANCE.md" not in template_text:
        fail("templates/AGENTS.md must point to .agents/AGENT-GUIDANCE.md")

    project_structure_text = (PLUGIN_ROOT / "references" / "project-kernel-structure.md").read_text(encoding="utf-8")
    for required in (
        ".agents/AGENT-GUIDANCE.md",
        ".agents/log.md",
        ".agents/notes/",
        "reference/",
        "append-only",
        "protected once they exist",
        ".agents/notes/README.md",
        "reference/README.md",
    ):
        if required not in project_structure_text:
            fail(f"project-kernel-structure.md must document scaffold path: {required}")

    agents_dir = PLUGIN_ROOT / ".agents" / "personas"
    if not (agents_dir / "README.md").is_file():
        fail("Missing required persona docs: .agents/personas/README.md")
    missing_personas = sorted(
        name for name in REQUIRED_PERSONAS if not (agents_dir / name).is_file()
    )
    if missing_personas:
        fail(f"Missing required personas: {', '.join(missing_personas)}")

    scaffold_script = PLUGIN_ROOT / "scripts" / "scaffold_project.py"
    if not scaffold_script.is_file():
        fail("Missing required scaffold script: scripts/scaffold_project.py")
    scaffold_text = scaffold_script.read_text(encoding="utf-8")
    for required in (
        '.agents" / "AGENT-GUIDANCE.md"',
        '.agents" / "log.md"',
        '.agents" / "notes"',
        '"reference" / "README.md"',
        "agent_notes_readme_path",
        "reference_readme_path",
        "append_log_entry",
    ):
        if required not in scaffold_text:
            fail(f"scaffold_project.py must create {required}")
    if 'project_dir / "agent-guidance.md"' in scaffold_text:
        fail("scaffold_project.py must not create docs/agent-guidance.md")

    engineering_text = (
        PLUGIN_ROOT / "references" / "workflows" / "engineering-delivery.md"
    ).read_text(encoding="utf-8")
    for required in (
        "PR Review Feedback",
        "git switch <topic-branch> || git switch -c <topic-branch>",
        "gh pr edit",
        "handoff is blocked",
        "explicit user authorization",
        "Reply to review threads and mark them resolved only when the user explicitly asks",
    ):
        if required not in engineering_text:
            fail(f"engineering-delivery.md must document GitHub handoff behavior: {required}")

    build_text = (PLUGIN_ROOT / "skills" / "build" / "SKILL.md").read_text(encoding="utf-8")
    if "handoff is blocked" not in build_text:
        fail("build skill must document blocked GitHub handoff fallback")

    qa_release_text = (
        PLUGIN_ROOT / "references" / "workflows" / "qa-and-release.md"
    ).read_text(encoding="utf-8")
    if "Ask before marking ready" not in qa_release_text or "explicitly authorizes" not in qa_release_text:
        fail("qa-and-release.md must require explicit authorization before gh pr ready")

    if not (PLUGIN_ROOT / "AGENTS.md").is_file():
        fail("Missing required plugin agent guidance: AGENTS.md")
    if not (PLUGIN_ROOT / "templates" / "AGENTS.md").is_file():
        fail("Missing required downstream agent template: templates/AGENTS.md")


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
