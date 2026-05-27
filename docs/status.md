# Project Status: Assembly

Last updated: 2026-05-27
Current phase: proposal

## Phase Verdict

- Current phase: proposal
- Why: Assembly now installs and loads as a working Codex plugin, and the bundle has been extended with a Claude Code manifest and marketplace so the same skills work in both runtimes. The remaining proposal work is turning that direction into a 1.0 spec and release gate.
- Evidence: PR #1 merged the project-workflow foundation into `main`; local `main` is clean at merge commit `210b3fd`; `codex plugin marketplace upgrade assembly` installed Assembly `0.8.1` under `~/.codex/plugins/cache/assembly/assembly/0.8.1`; validators passed before merge; repo has been renamed to `benjaminsehl/assembly`; dual-runtime support added on 2026-05-27 via `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and validator/audit-script updates.
- Structure decision: agent-only operating files now belong under `.agents/`, with root `AGENTS.md` as the visible entrypoint and `reference/` reserved for raw source material.
- Product decision: the Codex-first stance from 2026-05-23 is now extended to dual-runtime; the same plugin bundle ships as both a Codex plugin and a Claude Code plugin, and 1.0 must pass install/smoke checks in both. See `docs/decisions/2026-05-27-dual-runtime-claude-code.md`.
- Next gate: 1.0 spec written and reviewed, covering both runtimes.

## Next Recommended Skills

- `product-discovery`
- `spec`

## Current 1.0 Direction

- Candidate wedge: install Assembly, scaffold a repo, say `next`, and have Codex orient to phase, missing context, and the next useful workflow without guessing.
- Primary user: Sai building real projects with Codex.
- Secondary user: people who want a compact Codex-native product-building workflow instead of a pile of overlapping skills.
- Default stance: optimize 1.0 as Sai's personal stack first, while keeping the public plugin installable, documented, and conflict-aware enough that another serious builder could adopt it.
- Recommended proof path: Assembly self-hosts the workflow, CFO proves a greenfield/restart setup, and Hyper remains the richer retrofit proof or release stretch.
- Post-1.0 north star: Hermes orchestrates scoped Codex sessions using Assembly's project trail, phase gates, and GitHub handoff loop.
- Latest usage feedback: `product-discovery` should interview before deciding unless delegated; empty or minimal `build` prompts should infer and execute the first unambiguous build-track gate.

## Open Questions

- What exact behavior should count as success for `next` across proposal, prototype, build, and release phases?
- How much project-paper-trail scaffolding is helpful before it becomes ceremony?
- Should Assembly always default to draft PR handoff for material GitHub-backed changes, with local-only as the exception?
- Should 1.0 include only skills/docs/scripts, or also a more automated installer/migration helper?
- How much of the future dream/desloppification workflow belongs in `.agents/` versus lifecycle references?
- What is the smallest Hermes orchestration spike that proves the post-1.0 direction without delaying 1.0?

## Next Concrete Action

Write the Assembly 1.0 spec for the dual-runtime plugin (Codex + Claude Code), with Hermes orchestration captured as the next strategic horizon.
