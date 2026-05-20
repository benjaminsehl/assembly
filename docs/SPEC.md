# Spec: Codex Agent Skills Plugin

## Objective

Build a Codex plugin that gives us a small, reliable command-like workflow surface for everyday engineering work. The plugin should be the backbone for how future projects are specified, planned, built, tested, reviewed, simplified, and shipped.

The upstream pattern comes from Addy Osmani's `agent-skills`: seven lifecycle commands map into a larger set of structured skills. Codex does not expose the same `.claude/commands/*.md` slash-command primitive in the local plugin spec we inspected, so this plugin will implement those seven commands as first-class Codex skills:

| Entry skill | Job | Underlying skills |
| --- | --- | --- |
| `spec` | Define what to build before coding | `interview-me`, `idea-refine`, `spec-driven-development` |
| `plan` | Convert a spec into small verifiable tasks | `planning-and-task-breakdown`, `context-engineering` |
| `build` | Implement the next planned slice | `incremental-implementation`, `test-driven-development`, `debugging-and-error-recovery`, `git-workflow-and-versioning` |
| `test` | Prove behavior with tests and runtime checks | `test-driven-development`, `browser-testing-with-devtools`, `debugging-and-error-recovery` |
| `review` | Review current changes before merge | `code-review-and-quality`, `security-and-hardening`, `performance-optimization` |
| `code-simplify` | Reduce complexity without changing behavior | `code-simplification`, `code-review-and-quality`, `test-driven-development` |
| `ship` | Produce a go/no-go launch decision | `shipping-and-launch`, `ci-cd-and-automation`, `security-and-hardening`, `documentation-and-adrs`, `deprecation-and-migration` |

Success means a future Codex session can invoke one of these entry skills by name, load only the necessary deeper workflows, and produce consistent evidence without relying on memory of previous sessions.

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
skills/<entry>/SKILL.md         # Seven command-like orchestrator skills
skills/<workflow>/SKILL.md      # Underlying reusable workflow skills
skills/<persona>/SKILL.md       # Optional reviewer personas, if Codex skill shape is the right fit
references/*.md                 # Checklists loaded only when needed
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
- Entry-skill mapping validation: the seven entry skills reference the expected underlying skills.
- Drift validation: source-derived skills preserve their workflow intent when adapted.
- Manual Codex smoke test: install or expose the plugin locally, invoke each entry skill in a throwaway repo, and verify it loads the intended workflow.

## Boundaries

Always:

- Keep the seven entry skills thin and deterministic.
- Keep underlying workflow skills self-contained so the plugin works outside this machine.
- Prefer progressive disclosure: entry skills route; deeper skills carry detailed process.
- Include verification gates in every skill.
- Preserve source attribution for adapted content.

Ask first:

- Adding MCP servers, app connectors, hooks, or marketplace installation entries.
- Publishing the plugin, adding a remote repository, or choosing a public license.
- Changing the seven-entry command surface.
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
- The seven entry skills exist and route to the correct deeper workflows.
- The underlying skills needed by those entry points are present in the plugin.
- Validation scripts catch missing skills, broken mappings, malformed frontmatter, and accidental entry-skill bloat.
- A manual smoke test proves each entry skill can be invoked by Codex in a clean project context.

## Decisions

- The plugin is self-contained: underlying workflow skills are copied into `skills/`.
- `ship` defaults to local audit and uses subagents only when the user explicitly authorizes parallel agent work.
- The repo includes marketplace metadata, but no active user-level Codex config entry is edited by the plugin itself.
- The repo remains private and `UNLICENSED`; upstream MIT license text is preserved for vendored upstream material.
