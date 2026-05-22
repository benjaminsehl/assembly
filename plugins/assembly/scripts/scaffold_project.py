#!/usr/bin/env python3
"""Create a project lifecycle workspace inside a target repository."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "project"


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def resolve_parent_project(value: str, root: Path) -> Path:
    parent = Path(value).expanduser()
    if not parent.is_absolute():
        parent = root / parent
    parent = parent.resolve()
    if not parent.exists():
        raise SystemExit(f"Parent project workspace does not exist: {parent}")
    if not parent.is_dir():
        raise SystemExit(f"Parent project workspace is not a directory: {parent}")
    if not (parent / "status.md").is_file():
        raise SystemExit(
            f"Parent project workspace must contain status.md: {parent}"
        )
    return parent


def load_required_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Required scaffold template is missing: {path}")


def template_files(
    project_name: str,
    project_dir: Path,
    root: Path,
    protocol_text: str,
) -> dict[Path, str]:
    today = date.today().isoformat()
    status_path = rel(project_dir / "status.md", root)
    agent_guidance_path = rel(root / ".agents" / "AGENT-GUIDANCE.md", root)

    return {
        project_dir / "README.md": f"""# {project_name}

Project workspace for proposal, prototype, build, release, decisions, specs, plans, QA, and follow-up learning.

Start here:

- Current status: `{status_path}`
- Phase model: `phases/`
- Decisions: `decisions/`
- Product vision: `product/vision.md`
- Tech design: `tech-design/`
- Agent guidance: top-level `AGENTS.md` and `{agent_guidance_path}`
- Child projects: `projects/`
""",
        project_dir / "status.md": f"""# Project Status: {project_name}

Last updated: {today}
Current phase: proposal

## Phase Verdict

- Current phase: proposal
- Why: initial scaffold created; proposal outcomes and assumptions still need alignment.
- Next gate: proposal accepted by the user.

## Next Recommended Skills

- `product-discovery`
- `spec`

## Open Questions

- Who is the target user?
- What becomes 10x better if this project succeeds?
- What does good look like at release?
- Which assumptions are riskiest?
""",
        root / ".agents" / "AGENT-GUIDANCE.md": protocol_text,
        root / ".agents" / "log.md": f"""# Agent Log

Append meaningful agent handoff events, skipped gates, recovery notes, and project-operation changes here.

## {today}

- Project workspace scaffolded for `{project_name}`.
""",
        root / ".agents" / "notes" / "README.md": """# Agent Notes

Use dated notes for temporary agent working context, open loops, and handoff breadcrumbs.

Promote durable product, technical, or decision context into `docs/`. Keep source material in `reference/`.
""",
        root / "reference" / "README.md": """# Reference

Store raw source material, imports, screenshots, transcripts, datasets, vendor docs, and other evidence that should remain close to the project but should not be rewritten as project documentation.

When a reference changes a decision, summarize the durable conclusion in `docs/decisions/`, `docs/research/`, or the relevant phase file.
""",
        project_dir / "phases" / "proposal.md": """# Proposal Phase

## What Becomes 10x Better

Describe the user-visible improvement this project must create.

## What Good Looks Like

Define the observable outcome at the end of the project.

## Desired Outcomes

- TBD

## Assumptions

- TBD

## Principles

- TBD

## Risks

- TBD

## Decision Gate

Proposal is ready to leave this phase when outcomes, assumptions, principles, and success criteria are explicit enough to judge future work against them.
""",
        project_dir / "phases" / "prototype.md": """# Prototype Phase

## Prototype Question

What must we learn or feel before production build work is justified?

## Tangible Artifacts

- TBD

## What Must Feel True

- TBD

## Findings

- TBD

## Decision Gate

Prototype is ready to leave this phase when it proves, changes, or rejects the proposed direction.
""",
        project_dir / "phases" / "build.md": """# Build Phase

## Approved Direction

Link to the accepted proposal, prototype verdict, and spec.

## Implementation Slices

- TBD

## Acceptance Criteria

- TBD

## Verification

- TBD

## Risks

- TBD

## Decision Gate

Build is ready to leave this phase when production behavior is implemented, verified, and ready for QA and release polish.
""",
        project_dir / "phases" / "release.md": """# Release Phase

## QA Scope

- TBD

## Polish Checklist

- TBD

## Ship Decision

- Verdict:
- Evidence:
- Rollback:

## Grade Against Proposal

- What became 10x better:
- What good looked like:
- Result:

## Follow-Up Work

- TBD

## Decision Gate

Release is done when the work is shipped or intentionally held, graded against the original proposal, and follow-up learning is captured.
""",
        project_dir / "product" / "vision.md": f"""# Product Vision: {project_name}

## User

Who this is for.

## Painful Moment

The moment that makes this project matter.

## Promise

The user-visible promise this project should keep.

## Non-Goals

- TBD
""",
        project_dir / "product" / "principles.md": """# Product Principles

Principles that should shape decisions throughout the project.

- TBD
""",
        project_dir / "decisions" / "README.md": """# Decisions

Use this folder for decisions that are hard to reverse, surprising without context, and the result of a real trade-off.

## Decision Record Template

```markdown
# YYYY-MM-DD Decision Title

## Status

Proposed | Accepted | Replaced

## Context

What forced the decision?

## Options Considered

- TBD

## Decision

What did we choose?

## Why This Wins

Why is this best for the project outcomes and principles?

## Consequences

What gets easier, harder, or riskier?
```
""",
        project_dir / "tech-design" / "README.md": """# Tech Design

Capture architecture, interfaces, data model, runtime constraints, performance constraints, security constraints, and migration notes.

Prefer short design notes linked to specs, plans, and decisions.
""",
        project_dir / "specs" / "README.md": """# Specs

Save approved behavior specs here. Specs should define user-visible behavior, constraints, acceptance criteria, and verification.
""",
        project_dir / "plans" / "README.md": """# Plans

Save implementation plans here. Plans should break approved specs into small verifiable slices with explicit checks.
""",
        project_dir / "prototypes" / "README.md": """# Prototypes

Save prototype notes and links here. Prototype code should stay clearly temporary and should be deleted or absorbed after the verdict is captured.
""",
        project_dir / "research" / "README.md": """# Research

Save user, market, source, and technical research here. Separate observed evidence from assumptions.
""",
        project_dir / "qa" / "README.md": """# QA

Save QA plans, tested flows, bugs, repro steps, evidence, and regression recommendations here.
""",
        project_dir / "release" / "README.md": """# Release

Save launch checklists, ship decisions, rollout notes, rollback plans, and post-release grading here.
""",
        project_dir / "projects" / "README.md": """# Child Projects

Use this folder for nested projects that belong inside this project boundary.

Create a child project here when the work needs its own proposal, prototype, build, and release trail.
""",
    }


def write_files(files: dict[Path, str], root: Path, force: bool) -> dict[str, list[str]]:
    created: list[str] = []
    skipped: list[str] = []

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and not force:
            skipped.append(rel(path, root))
            continue
        path.write_text(content, encoding="utf-8")
        created.append(rel(path, root))

    return {"created": created, "skipped": skipped}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold docs for a project lifecycle workspace."
    )
    parser.add_argument("--root", default=".", help="Target repository root.")
    parser.add_argument("--name", default="", help="Human-readable project name.")
    parser.add_argument(
        "--slug",
        default="",
        help="Project slug. If provided, files are created under docs/projects/<slug>/.",
    )
    parser.add_argument(
        "--parent",
        default="",
        help=(
            "Existing project workspace to nest under, for example docs. "
            "Requires --slug and creates <parent>/projects/<slug>/."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files.",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Target root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Target root is not a directory: {root}")

    project_name = args.name.strip() or args.slug.strip() or "Project"
    slug = slugify(args.slug.strip() or project_name)
    protocol_text = load_required_text(PLUGIN_ROOT / "references" / "agent-operating-protocol.md")
    agents_template = load_required_text(PLUGIN_ROOT / "templates" / "AGENTS.md")
    if args.parent.strip():
        if not args.slug.strip():
            raise SystemExit("--parent requires --slug so the child project has a stable path")
        parent_project = resolve_parent_project(args.parent.strip(), root)
        project_dir = parent_project / "projects" / slug
    elif args.slug.strip():
        project_dir = root / "docs" / "projects" / slug
    else:
        project_dir = root / "docs"

    files = template_files(project_name, project_dir, root, protocol_text)
    agents_path = root / "AGENTS.md"
    agents_exists = agents_path.exists()
    if not agents_exists:
        files[agents_path] = agents_template

    result: dict[str, object] = write_files(
        files, root, args.force
    )
    result["project_dir"] = rel(project_dir, root)
    result["name"] = project_name
    if agents_exists:
        result["skipped"].append("AGENTS.md")
        result["manual_merge"] = [
            "AGENTS.md already exists; merge templates/AGENTS.md manually if needed.",
            ".agents/AGENT-GUIDANCE.md contains the reusable operating protocol unless it was also skipped.",
        ]
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
