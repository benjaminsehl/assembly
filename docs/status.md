# Project Status: Assembly

Last updated: 2026-05-24
Current phase: proposal

## Phase Verdict

- Current phase: proposal
- Why: Assembly now installs and loads as a working Codex plugin, and the product direction is clear: finish the Codex plugin first, then pursue Hermes as the orchestrator. PR #2 landed the next batch of 1.0 proposal, skill-behavior, and icon updates; the current work is turning that direction into a 1.0 spec and release gate.
- Evidence: PR #1 merged the project-workflow foundation into `main`; PR #2 merged as `15cb36a`; local `main` is synced with `origin/main`; `codex plugin marketplace upgrade assembly` reports the local marketplace install is already up to date; Assembly `0.8.3` is installed under `~/.codex/plugins/cache/assembly/assembly/0.8.3`; `docs/specs/assembly-1-0.md` drafts the 1.0 behavior spec.
- Structure decision: agent-only operating files now belong under `.agents/`, with root `AGENTS.md` as the visible entrypoint and `reference/` reserved for raw source material.
- Product decision: 1.0 is Codex-first; Claude support is not a near-term priority; Hermes orchestration is the post-1.0 strategic direction.
- Next gate: review and accept or revise `docs/specs/assembly-1-0.md`.

## Next Recommended Skills

- `spec`
- `plan`

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

Review `docs/specs/assembly-1-0.md`; once accepted, use `plan` to break 1.0 into implementation and proof tasks.
