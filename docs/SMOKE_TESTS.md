# Smoke Tests

These smoke tests verify that the entry skills route correctly. They are designed for throwaway projects so the workflows can be exercised without risking real work.

## Prerequisites

Register and enable the plugin, then restart Codex:

```bash
codex plugin marketplace add benjaminsehl/codex-agent-skills
```

If the plugin was already registered before the latest push:

```bash
codex plugin marketplace upgrade codex-agent-skills
```

## Test Matrix

| Entry skill | Smoke prompt | Expected evidence |
| --- | --- | --- |
| `spec` | "Use spec to define a tiny CLI that reverses lines from stdin." | Creates or proposes a spec with assumptions, commands, boundaries, and success criteria. |
| `plan` | "Use plan on the approved spec and create implementation tasks." | Creates a task list with acceptance criteria and verification steps. |
| `build` | "Use build to implement the first task." | Implements one slice, runs checks, and reports changed files. |
| `test` | "Use test to prove blank input returns blank output." | Adds or identifies a failing test first when practical, then passes it. |
| `review` | "Use review on the current diff." | Findings first, file/line references when issues exist, and test gaps. |
| `code-simplify` | "Use code-simplify on the changed files." | Behavior-preserving cleanup with verification evidence. |
| `ship` | "Use ship to decide whether this is ready to release." | GO/NO-GO, blockers, risks, evidence, and rollback procedure. |
| `product-discovery` | "Use product-discovery on an app that summarizes my meetings." | Discovery brief with user pain, wedge, alternatives, risks, and evidence needed. |
| `founder-review` | "Use founder-review on this product plan." | Expand/Narrow/Hold/Stop verdict with user-love and scope recommendations. |
| `business-model-review` | "Use business-model-review on this product concept." | ICP, willingness-to-pay, distribution, retention, and validation step. |
| `design-plan-review` | "Use design-plan-review before we build this dashboard." | UX verdict with must-fix issues and approved build shape. |
| `qa` | "Use qa on this local app." | Tested flows, bug repro steps, evidence, and regression recommendations. |
| `health-check` | "Use health-check on this repo." | Health report with blockers, important fixes, quick wins, and next action. |
| `retro` | "Use retro on what we shipped this week." | Wins, misses, learnings, decisions, and next actions. |
| `learn` | "Use learn to capture this project preference." | Proposed lesson, scope, destination, and exact wording. |
| `new-project` | "Use new-project to scaffold a project called Habit Coach." | Creates root project docs with status, phases, product, decisions, tech-design, specs, plans, prototypes, child projects, QA, and release files. |
| `prototype` | "Use prototype to explore three onboarding directions before build." | States the prototype question, creates or proposes a throwaway artifact, gives one way to inspect it, and captures a verdict. |
| `project-status` | "Use project-status to tell me what phase this project is in." | Phase verdict with evidence, missing artifacts, next gate, next recommended skills, and one next action. |

## Manual Acceptance Checklist

- [ ] `spec` stops at review instead of drifting into implementation.
- [ ] `plan` writes tasks that can be completed one slice at a time.
- [ ] `build` does not silently skip tests.
- [ ] `test` uses the Prove-It pattern for bugs.
- [ ] `review` leads with findings instead of a summary.
- [ ] `code-simplify` preserves behavior.
- [ ] `ship` does not use subagents unless explicitly authorized.
- [ ] `product-discovery` does not drift into implementation.
- [ ] `business-model-review` separates usefulness from viability.
- [ ] `qa` reports reproducible bugs and respects report-only mode.
- [ ] `learn` proposes guidance without silently editing global memory.
- [ ] `new-project` skips existing files by default.
- [ ] `new-project` can create a child project under a parent project workspace.
- [ ] `prototype` captures a verdict instead of leaving throwaway code orphaned.
- [ ] `project-status` cites artifacts before recommending next skills.
