# Spec: Codex Agent Skills Plugin

## Objective

Build a Codex plugin that gives us a small, reliable command-like workflow surface for full product development. The plugin should be the backbone for how future projects are started, oriented, discovered, prototyped, pressure-tested, specified, planned, designed, built, QAed, reviewed, launched, retroed, and improved.

The upstream engineering pattern comes from Addy Osmani's `agent-skills`: seven lifecycle commands map into a larger set of structured skills. The product/company layer is inspired by Garry Tan's GStack sprint model and specialist-role approach. Codex does not expose the same `.claude/commands/*.md` slash-command primitive in the local plugin spec we inspected, so this plugin implements command-like entry points as first-class Codex skills:

| Entry skill | Job | Underlying skills |
| --- | --- | --- |
| `spec` | Define what to build before coding | `interview-me`, `idea-refine`, `spec-driven-development` |
| `plan` | Convert a spec into small verifiable tasks | `planning-and-task-breakdown`, `context-engineering` |
| `build` | Implement the next planned slice | `incremental-implementation`, `test-driven-development`, `debugging-and-error-recovery`, `git-workflow-and-versioning` |
| `test` | Prove behavior with tests and runtime checks | `test-driven-development`, `browser-testing-with-devtools`, `debugging-and-error-recovery` |
| `review` | Review current changes before merge | `code-review-and-quality`, `security-and-hardening`, `performance-optimization` |
| `code-simplify` | Reduce complexity without changing behavior | `code-simplification`, `code-review-and-quality`, `test-driven-development` |
| `ship` | Produce a go/no-go launch decision | `shipping-and-launch`, `ci-cd-and-automation`, `security-and-hardening`, `documentation-and-adrs`, `deprecation-and-migration` |
| `product-discovery` | Pressure-test raw ideas before spec work | `interview-me`, `idea-refine`, `founder-product-critique`, `spec-driven-development` |
| `founder-review` | Challenge ambition, focus, scope, and user delight | `founder-product-critique`, `idea-refine`, `planning-and-task-breakdown` |
| `business-model-review` | Evaluate business viability and evidence needed | `business-model-evaluation`, `idea-refine`, `documentation-and-adrs` |
| `design-plan-review` | Review planned UX before implementation | `frontend-ui-engineering`, `founder-product-critique`, `performance-optimization` |
| `qa` | Test the product like a user after implementation | `live-qa-methodology`, `browser-testing-with-devtools`, `test-driven-development`, `debugging-and-error-recovery` |
| `health-check` | Audit project readiness and maintainability | `code-review-and-quality`, `performance-optimization`, `security-and-hardening`, `documentation-and-adrs`, `test-driven-development` |
| `retro` | Capture shipped outcomes and durable lessons | `documentation-and-adrs`, `code-review-and-quality`, `business-model-evaluation`, `founder-product-critique` |
| `learn` | Propose reusable guidance without replacing Codex memory | `documentation-and-adrs`, `context-engineering`, `retro` |
| `new-project` | Scaffold a project workspace and proposal gate | `product-discovery`, `founder-review`, `business-model-review`, `spec-driven-development`, `planning-and-task-breakdown`, `documentation-and-adrs` |
| `prototype` | Build a throwaway tangible artifact before production build | `idea-refine`, `frontend-ui-engineering`, `business-model-evaluation`, `documentation-and-adrs` |
| `project-status` | Determine current phase and next recommended skills | `context-engineering`, `documentation-and-adrs`, `product-discovery`, `prototype`, `build`, `qa`, `ship`, `retro`, `learn` |

Success means a future Codex session can invoke one of these entry skills by name, load only the necessary deeper workflows, and produce consistent evidence across three lenses: users love it, engineering is excellent, and the business model is viable. It should also be able to answer "what phase are we in?" from project artifacts and recommend the next skills.

## Project Phase Model

Every full project or major project slice follows four phases:

1. **Proposal:** define what becomes 10x better, what good looks like, outcomes, assumptions, principles, risks, and non-goals.
2. **Prototype:** create tangible proof or playable artifacts before committing to production build direction.
3. **Build:** implement approved slices with specs, plans, tests, reviews, and tech-design updates.
4. **Release:** run QA and polish, decide go/no-go, ship or hold intentionally, grade the result against the proposal, and capture follow-up learning.

The project workspace is inspired by `agent-kernel`'s inspectable markdown pattern, but adapted away from long-running-agent memory. Its default shape is `docs/project/` for a single-purpose repo or `docs/projects/<slug>/` for project slices inside a larger app.

## Tech Stack

- Codex local plugin manifest: `.codex-plugin/plugin.json`
- Skill format: one directory per skill with `SKILL.md` frontmatter and workflow body
- Documentation: Markdown in `docs/`
- Validation: lightweight local scripts under `scripts/`
- No runtime dependencies for v1 unless validation requires a small Node or Python script

## Commands

These are the project maintenance commands we should support once implementation starts:

```bash
# Validate plugin manifest JSON.
python3 -m json.tool .codex-plugin/plugin.json >/dev/null

# Validate expected folder and skill frontmatter shape.
python3 scripts/validate_plugin.py

# Audit orchestrator-to-underlying-skill references.
python3 scripts/validate_skill_graph.py
```

Until the validation scripts exist, the only reliable command is:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
```

## Project Structure

```text
.codex-plugin/plugin.json       # Codex plugin manifest
docs/SPEC.md                    # This specification
docs/PLAN.md                    # Implementation plan
tasks/todo.md                   # Task checklist used by build workflow
skills/<entry>/SKILL.md         # Command-like orchestrator skills
skills/<workflow>/SKILL.md      # Underlying reusable workflow skills
skills/<persona>/SKILL.md       # Optional reviewer personas, if Codex skill shape is the right fit
references/*.md                 # Checklists loaded only when needed
scripts/scaffold_project.py     # Deterministic project workspace scaffold
scripts/validate_plugin.py      # Shape validation
scripts/validate_skill_graph.py # Orchestrator mapping validation
assets/                         # Optional plugin UI assets
```

## Code Style

Skills should be process documents, not essays. Each `SKILL.md` must have a compact frontmatter block, a clear trigger description, ordered workflow steps, stop conditions, and verification evidence.

Example orchestrator style:

```markdown
---
name: build
description: Use when the user asks to implement the next task, build the next planned slice, or continue from the task list.
---

# Build

## Purpose

Implement exactly one planned slice at a time, with tests and verification evidence.

## Workflow

1. Read `tasks/todo.md` and choose the first pending task unless the user named a task.
2. Load the task acceptance criteria and the minimum relevant code context.
3. Follow `test-driven-development` and `incremental-implementation`.
4. If verification fails, switch to `debugging-and-error-recovery`.
5. Update the task status only after tests and build evidence are collected.

## Verification

- Targeted tests pass.
- Full project verification is run or the skipped portion is explicitly explained.
- The final response names changed files and evidence.
```

## Testing Strategy

This plugin is mostly instruction surface, so tests should validate structure, routing, and drift rather than application behavior.

- Manifest validation: `plugin.json` is valid JSON and references existing paths.
- Skill anatomy validation: every skill has `name`, `description`, `Purpose`, `Workflow`, and `Verification`.
- Entry-skill mapping validation: entry skills reference the expected underlying skills.
- Drift validation: source-derived skills preserve their workflow intent when adapted.
- Manual Codex smoke test: install or expose the plugin locally, invoke each entry skill in a throwaway repo, and verify it loads the intended workflow.

## Boundaries

Always:

- Keep entry skills thin and deterministic.
- Keep underlying workflow skills self-contained so the plugin works outside this machine.
- Prefer progressive disclosure: entry skills route; deeper skills carry detailed process.
- Include verification gates in every skill.
- Preserve source attribution for adapted content.

Ask first:

- Adding MCP servers, app connectors, hooks, or marketplace installation entries.
- Publishing the plugin, adding a remote repository, or choosing a public license.
- Changing the entry-skill command surface.
- Vendoring upstream content verbatim versus adapting it into our own words.

Never:

- Hide important behavior in undocumented hooks.
- Make `ship` produce a GO decision without rollback criteria.
- Make `build` skip tests silently.
- Make `review` summarize without file/line findings when code is available.
- Let entry skills grow into large duplicated copies of the deeper skills.

## Success Criteria

- The plugin has a valid `.codex-plugin/plugin.json`.
- The project contains a reviewed spec and plan.
- The original engineering entry skills exist and route to the correct deeper workflows.
- Product/company entry skills exist and route to the correct deeper workflows.
- Project lifecycle entry skills exist for scaffolding, prototyping, and status orientation.
- `scripts/scaffold_project.py` can create `docs/project/` or `docs/projects/<slug>/` without overwriting existing files by default.
- The underlying skills needed by those entry points are present in the plugin.
- Validation scripts catch missing skills, broken mappings, malformed frontmatter, and accidental entry-skill bloat.
- A manual smoke test proves each entry skill can be invoked by Codex in a clean project context.

## Decisions

- The plugin is self-contained: underlying workflow skills are copied into `skills/`.
- `ship` defaults to local audit and uses subagents only when the user explicitly authorizes parallel agent work.
- The repo includes marketplace metadata, but no active user-level Codex config entry is edited by the plugin itself.
- The repo is public and MIT licensed; upstream MIT attribution is preserved for vendored upstream material.
- GStack is cited as methodology inspiration only; no GStack code is vendored in this pass.
- Matt Pocock's `skills` and `agent-kernel` are cited as methodology and structure inspiration only; new project lifecycle skills are original Codex-native adaptations.
