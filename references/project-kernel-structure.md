# Project Kernel Structure

This is a project-focused adaptation of the agent-kernel idea: small, inspectable markdown files that let a future agent restart with less drift. It is not a long-running-agent memory system.

## Default Root Project

Use this shape for a single-purpose repo:

```text
docs/project/
|-- README.md
|-- status.md
|-- phases/
|   |-- proposal.md
|   |-- prototype.md
|   |-- build.md
|   `-- release.md
|-- product/
|   |-- vision.md
|   `-- principles.md
|-- decisions/
|   `-- README.md
|-- tech-design/
|   `-- README.md
|-- specs/
|   `-- README.md
|-- plans/
|   `-- README.md
|-- prototypes/
|   `-- README.md
|-- research/
|   `-- README.md
|-- qa/
|   `-- README.md
`-- release/
    `-- README.md
```

## Subproject or Big-App Slice

Use this shape when the repo contains many projects or product surfaces:

```text
docs/projects/<project-slug>/
`-- same files as docs/project/
```

## What Belongs Where

- `status.md`: current phase, evidence, next gate, next skills, and one next action.
- `phases/proposal.md`: outcomes, assumptions, principles, risks, and what good looks like.
- `phases/prototype.md`: prototype question, artifacts, findings, and verdict.
- `phases/build.md`: approved direction, slices, acceptance criteria, verification, and risks.
- `phases/release.md`: QA, polish, ship decision, grading, and follow-up work.
- `product/`: vision, user, painful moment, promise, principles, non-goals.
- `decisions/`: decision records only for trade-offs that are hard to reverse, surprising, and consequential.
- `tech-design/`: architecture, interfaces, data model, runtime constraints, security, performance, migrations.
- `specs/`: approved behavior specs.
- `plans/`: implementation plans and task breakdowns.
- `prototypes/`: prototype notes, links, verdicts, and cleanup status.
- `research/`: observed evidence, source notes, and market or user research.
- `qa/`: tested flows, bugs, repro steps, evidence, and regression recommendations.
- `release/`: launch, rollback, ship, and post-release notes.

## Scaffold Command

From this plugin repo:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

For a project slice in a larger app:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name" --slug project-name
```

The script skips existing files by default. Use `--force` only when intentionally regenerating scaffold files.
