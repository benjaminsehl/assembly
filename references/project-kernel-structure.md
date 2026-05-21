# Project Kernel Structure

This is a project-focused adaptation of the agent-kernel idea: small, inspectable markdown files that let a future agent restart with less drift. It is not a long-running-agent memory system.

Projects are recursive. A whole repo can be a project, and a client, agent layer, release, or feature inside it can also be a project with its own proposal, prototype, build, and release trail.

Keep docs co-located with the closest sensible project boundary. The point is Chesterton's fence: future work should find the original reasoning before changing or removing a structure.

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
|-- projects/
|   `-- README.md
|-- research/
|   `-- README.md
|-- qa/
|   `-- README.md
`-- release/
    `-- README.md
```

## Subprojects

If the subproject has its own code boundary, scaffold inside that boundary:

```text
repo/
`-- ios/Hyper/
    `-- docs/project/
        `-- same files as docs/project/
```

If the subproject belongs inside an existing project and does not have a clearer code directory, nest it under that project's `projects/` folder:

```text
docs/project/projects/<project-slug>/
`-- same files as docs/project/
```

The older flat form is still acceptable for peer projects at the repo boundary:

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
- `projects/`: child projects that need their own phase trail.
- `research/`: observed evidence, source notes, and market or user research.
- `qa/`: tested flows, bugs, repro steps, evidence, and regression recommendations.
- `release/`: launch, rollback, ship, and post-release notes.

## Scaffold Command

Root project in a repo or code boundary:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

Peer project at the repo boundary:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name" --slug project-name
```

Child project inside an existing project workspace:

```bash
python3 scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs/project \
  --name "Agent Layer" \
  --slug agent-layer
```

Co-located project inside a code subdirectory:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo/ios/Hyper --name "iOS Client"
```

The script skips existing files by default. Use `--force` only when intentionally regenerating scaffold files.
