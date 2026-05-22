# Smoke Tests

These smoke tests verify that the public skills route correctly and do not rely on deleted support skills.

## Prerequisites

```bash
codex plugin marketplace add benjaminsehl/codex-agent-skills
```

If the plugin was already registered:

```bash
codex plugin marketplace upgrade codex-agent-skills
```

After enabling and restarting Codex, confirm `Codex Agent Skills` appears in the active plugin list and that a cache bundle exists under `~/.codex/plugins/cache/codex-agent-skills/codex-agent-skills/`.

## Test Matrix

| Public skill | Smoke prompt | Expected evidence |
| --- | --- | --- |
| `next` | "Use next to do the next normal thing." | Reads project status, names phase/evidence, runs the next unambiguous skill or asks one concise question. |
| `project-status` | "Use project-status to tell me what phase this project is in." | Phase verdict with evidence, missing artifacts, next gate, next skills, and one action. |
| `project-status` | "Use project-status to scaffold a project called Habit Coach." | Creates project docs and reports skipped files or manual `AGENTS.md` merge. |
| `project-status` | "Use project-status to get this stale project back on track." | Conformity verdict, status update or skip reason, recovery plan, and next action. |
| `product-discovery` | "Use product-discovery on an app that summarizes my meetings." | Discovery brief with pain, wedge, alternatives, founder/business/design risks, and evidence needed. |
| `prototype` | "Use prototype to explore three onboarding directions before build." | Prototype question, throwaway artifact, inspection path, and verdict. |
| `spec` | "Use spec to define a tiny CLI that reverses lines from stdin." | Spec with assumptions, commands, boundaries, and success criteria. |
| `plan` | "Use plan on the approved spec and create implementation tasks." | Task list with dependencies, acceptance criteria, and verification steps. |
| `build` | "Use build to implement the first task." | One slice implemented with changed files and verification. |
| `test` | "Use test to prove blank input returns blank output." | Failing or targeted test evidence, then passing result. |
| `qa` | "Use qa on this local app." | Tested flows, repro steps for bugs, evidence, and regression recommendations. |
| `review` | "Use review on the current diff." | Findings first, file/line references when issues exist, and test gaps. |
| `code-simplify` | "Use code-simplify on the changed files." | Behavior-preserving cleanup with verification evidence. |
| `ship` | "Use ship to decide whether this is ready to release." | GO/NO-GO, blockers, risks, evidence, rollback, and follow-up learning. |

## Manual Acceptance Checklist

- [ ] Only the 12 public skills are triggerable from this plugin.
- [ ] `next` dispatches to the next evidence-backed action and does not guess when status is ambiguous.
- [ ] `project-status` handles scaffold, status, and repair without separate `new-project` or `introspect` skills.
- [ ] `product-discovery` handles founder, business, and design-plan lenses without separate review skills.
- [ ] Public skills load references conditionally and do not name deleted support skills as dependencies.
- [ ] `plugins/codex-agent-skills/scripts/audit_skill_conflicts.py` reports local overlapping lifecycle skills.
- [ ] Missing phase prerequisites produce a warning and double-back skill recommendation.
