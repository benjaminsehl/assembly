#!/usr/bin/env python3
"""Validate entry-skill orchestration references."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILL_GRAPH = {
    "spec": [
        "interview-me",
        "idea-refine",
        "spec-driven-development",
    ],
    "plan": [
        "planning-and-task-breakdown",
        "context-engineering",
    ],
    "build": [
        "incremental-implementation",
        "test-driven-development",
        "debugging-and-error-recovery",
        "git-workflow-and-versioning",
    ],
    "test": [
        "test-driven-development",
        "browser-testing-with-devtools",
        "debugging-and-error-recovery",
    ],
    "review": [
        "code-review-and-quality",
        "security-and-hardening",
        "performance-optimization",
    ],
    "code-simplify": [
        "code-simplification",
        "code-review-and-quality",
        "test-driven-development",
    ],
    "ship": [
        "shipping-and-launch",
        "ci-cd-and-automation",
        "security-and-hardening",
        "performance-optimization",
        "documentation-and-adrs",
        "deprecation-and-migration",
        "code-review-and-quality",
    ],
    "product-discovery": [
        "interview-me",
        "idea-refine",
        "founder-product-critique",
        "spec-driven-development",
    ],
    "founder-review": [
        "founder-product-critique",
        "idea-refine",
        "planning-and-task-breakdown",
    ],
    "business-model-review": [
        "business-model-evaluation",
        "idea-refine",
        "documentation-and-adrs",
    ],
    "design-plan-review": [
        "frontend-ui-engineering",
        "founder-product-critique",
        "performance-optimization",
    ],
    "qa": [
        "live-qa-methodology",
        "browser-testing-with-devtools",
        "test-driven-development",
        "debugging-and-error-recovery",
    ],
    "health-check": [
        "code-review-and-quality",
        "performance-optimization",
        "security-and-hardening",
        "documentation-and-adrs",
        "test-driven-development",
    ],
    "retro": [
        "documentation-and-adrs",
        "code-review-and-quality",
        "business-model-evaluation",
        "founder-product-critique",
    ],
    "learn": [
        "documentation-and-adrs",
        "context-engineering",
        "retro",
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
    for entry, dependencies in SKILL_GRAPH.items():
        text = read_skill(entry)
        if "Underlying skills" not in text:
            fail(f"{entry} must include an Underlying skills section")
        if entry in dependencies:
            fail(f"{entry} must not depend on itself")

        for dependency in dependencies:
            if not skill_path(dependency).exists():
                fail(f"{entry} references missing skill {dependency}")
            if f"`{dependency}`" not in text and f"- {dependency}" not in text:
                fail(f"{entry} does not mention required dependency {dependency}")

        if len(text.splitlines()) > 180:
            fail(f"{entry} is too large; entry skills should stay thin")


def validate_no_missing_orphans() -> None:
    available = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    required = set(SKILL_GRAPH)
    for dependencies in SKILL_GRAPH.values():
        required.update(dependencies)

    missing = sorted(required - available)
    if missing:
        fail(f"Missing required graph skills: {', '.join(missing)}")


def main() -> int:
    try:
        validate_no_missing_orphans()
        validate_graph()
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("OK: skill graph is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
