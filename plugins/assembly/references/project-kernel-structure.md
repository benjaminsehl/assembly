# Project Docs Structure

This is a project-focused adaptation of the agent-kernel idea: small, inspectable markdown files that let a future agent restart with less drift. It is not a long-running-agent memory system.

## Contents

- Root project
- Agent-only workspace
- Subprojects
- What belongs where
- Why root docs

Projects are recursive. A whole repo can be a project, and an agent layer, native client, release, or feature inside it can also be a project with its own proposal, prototype, build, and release trail.

Use one root docs tree. The point is Chesterton's fence: future work should find the original reasoning before changing or removing a structure.

## Root Project

Use this shape for the main project in a repo:

```text
AGENTS.md
.agents/
|-- AGENT-GUIDANCE.md
|-- log.md
`-- notes/
    `-- README.md
docs/
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
|-- release/
|   `-- README.md
`-- projects/
    `-- README.md
reference/
`-- README.md
```

## Agent-Only Workspace

Keep `AGENTS.md` at the repo root so agents have an obvious entrypoint. Put other agent-only operating material under `.agents/`.

Instruction-like project files use uppercase names, such as `.agents/AGENT-GUIDANCE.md`. Records and working context use lowercase names, such as `.agents/log.md` and `.agents/notes/`.

Do not put agent-only control files in `docs/`. `docs/` is the durable project paper trail; `.agents/` is the agent operating layer.

## Subprojects

Use this shape for a subproject:

```text
docs/projects/<project-slug>/
`-- same files as docs/
```

Use this shape for a nested subproject:

```text
docs/projects/<parent-slug>/projects/<child-slug>/
`-- same files as docs/
```

Prefer a single root `docs/` tree over package-level docs. Only use a different docs root when the work is genuinely in a different repo or the user explicitly chooses that boundary.

## What Belongs Where

- `AGENTS.md`: top-level entrypoint for agent behavior in the repo.
- `.agents/AGENT-GUIDANCE.md`: project-visible copy of the phase-aware agent operating protocol.
- `.agents/log.md`: append-only agent handoff events, skipped gates, recovery notes, and project-operation changes.
- `.agents/notes/`: temporary agent working notes and open loops.
- `reference/`: raw source material, imports, screenshots, transcripts, datasets, vendor docs, and evidence that should stay close to the project.
- `status.md`: current phase, evidence, next gate, next skills, and one next action.
- `phases/proposal.md`: outcomes, assumptions, principles, risks, existing constraints, and what good looks like.
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

Root project:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

This creates `AGENTS.md` only when it does not already exist. Existing project instructions must be merged manually.

The scaffold also creates `.agents/AGENT-GUIDANCE.md`, `.agents/log.md`, `.agents/notes/README.md`, and `reference/README.md` when absent.

Subproject:

```bash
python3 scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs \
  --name "Agent Layer" \
  --slug agent-layer
```

Nested subproject:

```bash
python3 scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs/projects/agent-layer \
  --name "Agent Evals" \
  --slug evals
```

The script skips existing files by default. Use `--force` only when intentionally regenerating scaffold files.
