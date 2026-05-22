# Product Discovery: Assembly 1.0

Last updated: 2026-05-22

## Idea In User-Problem Language

Builders using Codex need a reliable way to keep agents oriented across the full product lifecycle. The painful moment is not "I need another skill"; it is "I am back in this project and do not remember the state, and I do not trust the agent to know the right next move."

## User And Painful Moment

- Primary user: Sai building real apps and project slices with Codex.
- Secondary user: a serious builder who wants a compact Codex-native operating system for product work.
- Painful moment: returning to a repo, starting a fuzzy idea, or asking an agent to continue and watching it guess, skip product context, or over-index on coding.
- Desired outcome: Codex can orient itself, name the phase, identify missing prerequisites, select the right workflow, and proceed only when the next action is evidence-backed.

## Current Workarounds

- Ad hoc prompts like "continue" or "what should we do?"
- Loose skills installed globally with overlapping names.
- Repo-local markdown notes that are helpful but not consistently structured.
- Manual reminders to check product vision, principles, decisions, QA, and release gates.
- Manual reminders to commit, push, open descriptive draft PRs, explain why the work matters, self-review, simplify, and mark PRs ready.
- Built-in platform plugins that help with execution but do not own the product lifecycle.

## Narrow 1.0 Wedge

Install Assembly, scaffold a repo, say `next`, and have Codex:

- read the local project trail,
- identify proposal, prototype, build, or release phase,
- name missing prerequisites,
- choose the right public skill,
- ask one clear question only when needed,
- update status when project-doc edits are in scope,
- for material GitHub-backed changes, commit, push, open a descriptive draft PR, explain why/principles/approach, self-review, simplify, and mark ready only after verification.

## Lovable Product Moment

The user returns after days away, types `next`, and Codex says what phase the project is in, why, what is missing, and either performs the next safe action or asks the one question that matters.

## Alternatives

- Addy-style individual skills: useful patterns, but not a cohesive Codex project operating system.
- GStack-style sprint roles: useful product/company methodology, but too broad and Claude/runtime-specific for this pass.
- Built-in Codex plugins: strong execution tools, but not a lifecycle owner.
- Manual `AGENTS.md` instructions: helpful, but too passive without status and phase artifacts.

## Founder Critique

Verdict: narrow, then prove.

Assembly has a compelling personal wedge, but 1.0 should resist becoming a generic app factory too early. The ambitious version is an agentic app factory; the 1.0 version should prove the control loop that such a factory would need: project trail, phase awareness, next-step routing, and evidence-based gates.

## Business Model Lens

Near-term business model is not the main constraint. Assembly should be evaluated as leverage for building better products faster.

Potential future business value:

- A public open-source workflow that becomes a personal brand asset.
- A premium app-factory layer, hosted project dashboard, or team workflow only after the local plugin proves real value.
- Consulting or product-building acceleration if the workflow produces visibly better apps.

Riskiest viability assumption: other builders will adopt a project-doc workflow unless the `next` experience is immediately and repeatedly useful.

## Main Risks

- Too much ceremony: agents write documents instead of improving the product.
- Too little structure: `next` becomes a polite guess.
- Install/session refresh friction hides the value.
- Skill conflicts make behavior unpredictable.
- Agents may finish with local diffs instead of reviewable GitHub artifacts.
- The stack overfits Sai's projects before being tested on enough project types.

## Evidence Needed Before 1.0

- Fresh install and upgrade works from `benjaminsehl/assembly`.
- Fresh Codex session sees `assembly:next`.
- Assembly itself uses root `docs/` and status successfully.
- Scaffolded projects separate durable docs, agent-only `.agents/` context, and raw `reference/` material.
- At least one real external project, ideally Hyper or CFO, gets a useful Assembly retrofit.
- `next` behaves well in at least proposal, build, and release-like states.
- At least one end-to-end change is committed, pushed, opened as a descriptive draft PR with `gh`, self-reviewed, simplified, and marked ready.
- Docs explain how to migrate from loose skills and how to handle conflicts.

## Candidate 1.0 Release Criteria

- Public plugin installs as `assembly` and exposes only the 12 intended public skills.
- `project-status` can scaffold and repair a project trail without overwriting existing `AGENTS.md`.
- Scaffolds keep `AGENTS.md` at the root, agent-only context in `.agents/`, durable project reasoning in `docs/`, and raw source material in `reference/`.
- `next` is reliable enough to be the default continuation command.
- GitHub-backed work has a reliable PR handoff loop: descriptive draft PR first, ready only after verification, self-review, and simplification.
- Validators cover manifest, marketplace layout, skill graph, references, and conflict audit.
- README gives a clear user guide from install to first project to ongoing use.
- 1.0 has a release checklist, smoke-test evidence, and a short retro from real project use.

## Recommended Next Step

Align on whether 1.0 should optimize for "personal stack that works beautifully for Sai" or "public plugin others can confidently install." Then write a 1.0 spec.
