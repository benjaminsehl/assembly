#!/usr/bin/env python3
"""Validate public skill references."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILL_REFERENCES = {
    "next": [
        "references/project-phases.md",
        "references/agent-operating-protocol.md",
        "references/workflows/project-lifecycle.md",
    ],
    "spec": [
        "references/workflows/engineering-delivery.md",
        "references/product-discovery-checklist.md",
        "references/project-phases.md",
    ],
    "plan": [
        "references/workflows/engineering-delivery.md",
        "references/project-phases.md",
    ],
    "build": [
        "references/workflows/engineering-delivery.md",
        "references/testing-patterns.md",
    ],
    "test": [
        "references/workflows/engineering-delivery.md",
        "references/testing-patterns.md",
        "references/qa-checklist.md",
    ],
    "review": [
        "references/workflows/engineering-delivery.md",
        "references/security-checklist.md",
        "references/performance-checklist.md",
        "references/accessibility-checklist.md",
    ],
    "code-simplify": [
        "references/workflows/engineering-delivery.md",
        "references/testing-patterns.md",
    ],
    "ship": [
        "references/workflows/qa-and-release.md",
        "references/security-checklist.md",
        "references/performance-checklist.md",
        "references/testing-patterns.md",
    ],
    "product-discovery": [
        "references/product-discovery-checklist.md",
        "references/business-model-checklist.md",
        "references/design-quality-checklist.md",
        "references/workflows/product-strategy.md",
    ],
    "qa": [
        "references/qa-checklist.md",
        "references/testing-patterns.md",
        "references/workflows/qa-and-release.md",
    ],
    "prototype": [
        "references/design-quality-checklist.md",
        "references/business-model-checklist.md",
        "references/workflows/product-strategy.md",
        "references/project-phases.md",
    ],
    "project-status": [
        "references/project-phases.md",
        "references/project-kernel-structure.md",
        "references/agent-operating-protocol.md",
        "references/workflows/project-lifecycle.md",
    ],
}


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def skill_path(name: str) -> Path:
    return ROOT / "skills" / name / "SKILL.md"


def read_skill(name: str) -> str:
    path = skill_path(name)
    if not path.exists():
        fail(f"Missing skill: {name}")
    return path.read_text(encoding="utf-8")


def validate_graph() -> None:
    for entry, references in SKILL_REFERENCES.items():
        text = read_skill(entry)
        if "## References" not in text:
            fail(f"{entry} must include a References section")
        if "## Underlying skills" in text:
            fail(f"{entry} must not reference triggerable underlying skills")

        for reference in references:
            if not (ROOT / reference).exists():
                fail(f"{entry} references missing file {reference}")
            if reference not in text:
                fail(f"{entry} does not mention required reference {reference}")

        if len(text.splitlines()) > 120:
            fail(f"{entry} is too large; public skills should stay thin")


def validate_no_missing_orphans() -> None:
    available = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    required = set(SKILL_REFERENCES)

    missing = sorted(required - available)
    if missing:
        fail(f"Missing required public skills: {', '.join(missing)}")
    unexpected = sorted(available - required)
    if unexpected:
        fail(f"Unexpected triggerable skills: {', '.join(unexpected)}")


def main() -> int:
    try:
        validate_no_missing_orphans()
        validate_graph()
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("OK: skill references are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
