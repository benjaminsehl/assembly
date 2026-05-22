# Assembly

Assembly is a compact personal product-building stack for Codex: contextual next steps, project orientation, product discovery, prototypes, specs, plans, implementation, tests, QA, review, simplification, and release decisions.

The plugin intentionally exposes a small public skill surface. Detailed guidance lives in the plugin bundle's `references/` directory so agents load it only when needed.

## Quick Start

Register the public marketplace:

```bash
codex plugin marketplace add benjaminsehl/assembly
```

If it is already registered:

```bash
codex plugin marketplace upgrade assembly
```

Migrating from the old name:

```bash
codex plugin marketplace remove codex-agent-skills
codex plugin marketplace add benjaminsehl/assembly
```

Then invoke public skills in natural language:

```text
Use next to do the next normal thing.
Use project-status to tell me what phase we are in and what skills to use next.
Use project-status to scaffold this project.
Use product-discovery on this idea.
Use prototype before we build this direction.
Use spec to define this feature before coding.
Use plan to break the approved spec into tasks.
Use build to implement the next planned slice.
Use test to prove this bug.
Use qa on this local app.
Use review on the current diff.
Use code-simplify on the changed files.
Use ship to decide whether this is ready.
```

If you already have personal lifecycle skills installed, treat this plugin as the owner of that surface. Keep specialized platform skills, but de-duplicate older lifecycle skills named `next`, `spec`, `plan`, `build`, `test`, `review`, `ship`, `qa`, `prototype`, `product-discovery`, or `project-status`.

## Public Skills

| Skill | Job |
| --- | --- |
| `next` | Contextual continuation: inspect project state, choose the next normal action, and proceed when unambiguous |
| `project-status` | Project gateway for status, scaffolding, repair, retro, and next-skill routing |
| `product-discovery` | Product gateway for raw ideas, founder critique, business viability, and design-plan pressure tests |
| `prototype` | Tangible proof before production build |
| `spec` | Requirements before coding |
| `plan` | Dependency-ordered tasks after spec |
| `build` | One verified implementation slice |
| `test` | Behavior proof, bug reproduction, and runtime checks |
| `qa` | User-like product testing after implementation |
| `review` | Diff, branch, commit, or PR review |
| `code-simplify` | Behavior-preserving cleanup |
| `ship` | Go/no-go release decision |

## Project Docs Convention

The root project workspace is `docs/`. Subprojects live under `docs/projects/<slug>/` and can nest recursively.

```text
my-app/
|-- AGENTS.md
|-- .agents/
|   |-- AGENT-GUIDANCE.md
|   |-- log.md
|   `-- notes/
|-- docs/
|   |-- status.md
|   |-- phases/
|   |-- product/
|   |-- decisions/
|   |-- tech-design/
|   |-- specs/
|   |-- plans/
|   |-- prototypes/
|   |-- qa/
|   |-- release/
|   `-- projects/
|-- reference/
`-- src/
```

Why this shape:

- Agent-only operating material is tucked under `.agents/`, with `AGENTS.md` kept as the top-level entrypoint.
- Instruction-like project files use uppercase names, such as `AGENT-GUIDANCE.md`; records like `log.md` and `notes/` stay lowercase.
- Agents get one obvious place to start: `docs/status.md`.
- Project reasoning is centralized instead of scattered across package folders.
- Subprojects still get their own paper trail.
- Chesterton's fence is visible before important decisions are changed.

## How Agents Should Work Through A Project

1. Use `next` when the user asks to continue through the normal process.
2. Read `docs/status.md` and nearest subproject status.
3. Use `project-status` when the phase, scaffold, repair path, or next skill is not obvious.
4. Use `product-discovery` when product direction, user love, or business viability is unclear.
5. Choose the matching lifecycle skill for the current phase.
6. If prerequisites are missing, warn once and recommend the right double-back skill.
7. If the user insists, proceed while naming the skipped gate and risk unless a hard safety boundary applies.
8. For material changes in GitHub-backed repos, use `gh` to create a draft PR, run self-review and code simplification, then mark the PR ready when verification passes.

## GitHub Handoff

Assembly expects agents to leave real work reviewable:

- Commit focused changes on a topic branch.
- Push the branch.
- Open or update a descriptive draft PR with `gh`.
- Explain why the PR exists, the first principles behind the change, and how the agent approached it.
- Run `review` and `code-simplify` before marking ready.
- Mark the PR ready with `gh pr ready` only after verification, self-review, and simplification pass.
- Do not merge, deploy, or create non-draft PRs without explicit direction.

The canonical agent protocol lives in [references/agent-operating-protocol.md](plugins/assembly/references/agent-operating-protocol.md). New projects receive a copy at `.agents/AGENT-GUIDANCE.md`.

## Scaffolding

From this plugin checkout, scaffold a root project:

```bash
python3 plugins/assembly/scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

Scaffold a subproject:

```bash
python3 plugins/assembly/scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs \
  --name "Agent Layer" \
  --slug agent-layer
```

The script skips existing files by default. If the target repo already has `AGENTS.md`, the scaffold will not overwrite it; merge [templates/AGENTS.md](plugins/assembly/templates/AGENTS.md) manually.

## Validation

```bash
python3 plugins/assembly/scripts/validate_plugin.py
python3 plugins/assembly/scripts/validate_skill_graph.py
python3 plugins/assembly/scripts/audit_skill_conflicts.py
python3 -m py_compile plugins/assembly/scripts/validate_plugin.py plugins/assembly/scripts/validate_skill_graph.py plugins/assembly/scripts/scaffold_project.py plugins/assembly/scripts/audit_skill_conflicts.py
```

## Source References

- Addy Osmani `agent-skills`: https://github.com/addyosmani/agent-skills
- Garry Tan `gstack`: https://github.com/garrytan/gstack
- Matt Pocock `skills`: https://github.com/mattpocock/skills
- Benjamin Sehl `agent-kernel`: https://github.com/benjaminsehl/agent-kernel
- Install details: [docs/INSTALL.md](plugins/assembly/docs/INSTALL.md)
- Source notes: [docs/SOURCE_NOTES.md](plugins/assembly/docs/SOURCE_NOTES.md)
