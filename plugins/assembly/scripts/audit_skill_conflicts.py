#!/usr/bin/env python3
"""Report likely skill-name conflicts with local user skill roots."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS = {
    "next",
    "init",
    "project-status",
    "product-discovery",
    "prototype",
    "spec",
    "plan",
    "build",
    "test",
    "qa",
    "review",
    "code-simplify",
    "ship",
}


def skill_names(root: Path) -> set[str]:
    if not root.exists():
        return set()
    return {path.parent.name for path in root.glob("*/SKILL.md")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        action="append",
        type=Path,
        help="Extra skill root to inspect. Can be passed more than once.",
    )
    args = parser.parse_args()

    codex_cache_roots = [
        root
        for root in sorted((Path.home() / ".codex" / "plugins" / "cache").glob("*/*/*/skills"))
        if root.parts[-4:-2] != ("assembly", "assembly")
    ]
    claude_cache_roots = [
        root
        for root in sorted((Path.home() / ".claude" / "plugins" / "cache").glob("*/*/*/skills"))
        if root.parts[-4:-2] != ("assembly", "assembly")
    ]
    roots = [
        Path.home() / ".agents" / "skills",
        Path.home() / ".codex" / "skills",
        Path.home() / ".claude" / "skills",
        *codex_cache_roots,
        *claude_cache_roots,
        *(args.root or []),
    ]

    found = False
    print("Assembly public lifecycle names:")
    print(", ".join(sorted(PUBLIC_SKILLS)))
    print()

    for root in roots:
        names = skill_names(root)
        conflicts = sorted(PUBLIC_SKILLS & names)
        if not conflicts:
            print(f"OK: no public-skill conflicts in {root}")
            continue
        found = True
        print(f"CONFLICT: {root}")
        for name in conflicts:
            print(f"  - {name}")

    if found:
        print()
        print("Recommendation: make assembly the owner of lifecycle skills.")
        print("Disable, rename, or avoid older overlapping lifecycle skills before installing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
