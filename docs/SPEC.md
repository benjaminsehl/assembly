# Spec: Codex Agent Skills Plugin

## Objective

Build a compact Codex plugin that acts as a personal product-building stack. It should help future agents continue to the next contextual step, orient a project, shape product direction, prototype, specify, plan, build, test, QA, review, simplify, and ship with evidence.

The public surface is intentionally small. Detailed workflow knowledge lives in `references/` so Codex can load it only when needed and avoid conflicts with users' existing skills.

## Public Skill Surface

| Public skill | Job | Key references |
| --- | --- | --- |
| `next` | Continue through the normal process by choosing the next evidence-backed action | `project-phases`, `agent-operating-protocol`, `workflows/project-lifecycle` |
| `project-status` | Project gateway for status, scaffold, repair, retro, and next-skill routing | `project-phases`, `project-kernel-structure`, `agent-operating-protocol`, `workflows/project-lifecycle` |
| `product-discovery` | Product gateway for ideas, founder critique, business viability, and design-plan critique | `product-discovery-checklist`, `business-model-checklist`, `design-quality-checklist`, `workflows/product-strategy` |
| `prototype` | Create tangible throwaway evidence before production build | `workflows/product-strategy`, `project-phases` |
| `spec` | Define what to build before coding | `workflows/engineering-delivery`, `project-phases` |
| `plan` | Convert approved requirements into small verifiable tasks | `workflows/engineering-delivery`, `project-phases` |
| `build` | Implement one planned slice with tests and verification | `workflows/engineering-delivery`, `testing-patterns` |
| `test` | Prove behavior with tests and runtime checks | `workflows/engineering-delivery`, `testing-patterns` |
| `qa` | Test the product like a user after implementation | `qa-checklist`, `workflows/qa-and-release` |
| `review` | Review current changes before merge | `workflows/engineering-delivery`, `security`, `performance`, `accessibility` checklists |
| `code-simplify` | Reduce complexity without changing behavior | `workflows/engineering-delivery`, `testing-patterns` |
| `ship` | Produce a go/no-go launch decision | `workflows/qa-and-release`, release checklists |

Success means a future Codex session can invoke one of these skills by name, load only the necessary references, and produce consistent evidence across three lenses: users love it, engineering is excellent, and the business model is viable.

## Project Phase Model

Every full project or substantial project slice follows four phases:

1. **Proposal:** define what becomes 10x better, what good looks like, outcomes, assumptions, principles, risks, and non-goals.
2. **Prototype:** create tangible proof or playable artifacts before committing to production build direction.
3. **Build:** implement approved slices with specs, plans, tests, reviews, and tech-design updates.
4. **Release:** run QA and polish, decide go/no-go, ship or hold intentionally, grade against proposal, and capture follow-up learning.

Projects are recursive. A repo can be a project, and clients, agent layers, releases, or features inside it can be subprojects with their own phase trail under `docs/projects/<slug>/`.

## Validation

Required commands:

```bash
python3 scripts/validate_plugin.py
python3 scripts/validate_skill_graph.py
python3 scripts/audit_skill_conflicts.py
python3 -m py_compile scripts/validate_plugin.py scripts/validate_skill_graph.py scripts/scaffold_project.py scripts/audit_skill_conflicts.py
git diff --check
```

Validation must ensure:

- Only the 12 public skills are triggerable from this plugin.
- Public skills have concise descriptions, required sections, and direct reference links.
- Public skills do not list deleted support skills as dependencies.
- Required references, templates, personas, and scaffold scripts exist.
- Install docs explain existing skill conflicts and replacement guidance.
- References over 100 lines include a `## Contents` section.

## Boundaries

Always:

- Prefer project conventions over generic workflow.
- Keep public skills thin.
- Put detailed guidance in `references/`.
- Preserve a decision paper trail.
- Validate before calling the plugin install-ready.

Ask first:

- Before overwriting existing `AGENTS.md`.
- Before destructive operations, external messaging, money movement, credential use, or privacy-sensitive work.
- Before skipping phase gates when risk materially changes.

Never:

- Expose broad triggerable support skills that collide with common user skills.
- Treat business or product assumptions as proven without evidence.
- Mark work complete without verification.
