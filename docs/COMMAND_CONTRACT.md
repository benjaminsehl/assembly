# Command Contract

This contract defines the stable public skills. Everything else is reference material, scripts, personas, or project documentation.

## Shared Rules

Every public skill must:

- Name the active workflow and why it applies.
- Identify the current project phase when project docs are available.
- Load the smallest relevant context and reference files.
- Produce evidence, not vibes.
- Warn when the user asks to skip missing phase prerequisites, recommend the right double-back skill, and record skipped gates if the user insists.
- Stop and ask when the next step would cross an `Ask first` boundary in `docs/SPEC.md`.

Every public skill must not:

- Invoke deleted support skills by name as dependencies.
- Invent project commands that are not in the target repo.
- Mark work complete without verification evidence.
- Overwrite an existing `AGENTS.md` while scaffolding.
- Continue into a different lifecycle phase unless the user asked for that phase.

If a prompt is unclear, state the inferred task, current phase, and recommended next skill, then ask a concise verification question before acting.

## Public Skill Surface

| Skill | Purpose | Main references |
| --- | --- | --- |
| `project-status` | Orient, scaffold, repair status, and recommend next skills | `project-phases`, `project-kernel-structure`, `agent-operating-protocol`, `workflows/project-lifecycle` |
| `product-discovery` | Shape raw ideas and product direction | `product-discovery-checklist`, `business-model-checklist`, `design-quality-checklist`, `workflows/product-strategy` |
| `prototype` | Build throwaway tangible proof before production build | `design-quality-checklist`, `business-model-checklist`, `workflows/product-strategy`, `project-phases` |
| `spec` | Turn intent into reviewed requirements | `workflows/engineering-delivery`, `product-discovery-checklist`, `project-phases` |
| `plan` | Turn approved requirements into verifiable tasks | `workflows/engineering-delivery`, `project-phases` |
| `build` | Implement one planned slice with verification | `workflows/engineering-delivery`, `testing-patterns` |
| `test` | Prove behavior or bugs with tests/runtime evidence | `workflows/engineering-delivery`, `testing-patterns`, `qa-checklist` |
| `qa` | Test the runnable product like a user | `qa-checklist`, `testing-patterns`, `workflows/qa-and-release` |
| `review` | Review diffs, commits, branches, or PRs | `workflows/engineering-delivery`, `security-checklist`, `performance-checklist`, `accessibility-checklist` |
| `code-simplify` | Simplify working code without behavior change | `workflows/engineering-delivery`, `testing-patterns` |
| `ship` | Produce a go/no-go release decision | `workflows/qa-and-release`, `security-checklist`, `performance-checklist`, `testing-patterns` |

## Gateway Policy

- `project-status` is the project gateway. It covers new project scaffolding, phase status, stale docs, recovery plans, retro capture, and durable project learning.
- `product-discovery` is the product gateway. It covers raw ideas, founder critique, business-model pressure tests, and planned UX critique before specs.
- The engineering spine is `spec` -> `plan` -> `build` -> `test` -> `review` -> `code-simplify` -> `ship`.
- `prototype` and `qa` stay public because they are frequent tangible-work moments that do not fit cleanly into spec/build/release commands.

## Trigger Examples

- `project-status`: "What phase are we in?", "Scaffold this project", "Get this project back on track", "What should we do next?"
- `product-discovery`: "I have an idea", "Pressure-test this", "Is this viable?", "Do a founder/business/design critique."
- `prototype`: "Build a throwaway prototype", "Can we feel this before committing?"
- `spec`: "Write the spec", "Define this before building."
- `plan`: "Break this into tasks", "Plan the approved spec."
- `build`: "Implement the next task", "Continue from task 3."
- `test`: "Prove this bug", "Write tests", "Verify this behavior."
- `qa`: "Test this app like a user", "Find product bugs."
- `review`: "Review this diff/PR/branch."
- `code-simplify`: "Simplify this working code without changing behavior."
- `ship`: "Is this ready to release?", "Make a go/no-go decision."

## Stop Conditions

All skills stop when:

- The requested scope is ambiguous enough that acting would pick an arbitrary direction.
- Required project artifacts are missing and skipping them would materially change risk.
- Verification cannot be run or interpreted safely.
- Private data, credentials, destructive operations, external messaging, money movement, or explicit-confirmation boundaries are involved.
