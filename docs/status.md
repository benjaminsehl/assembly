# Project Status: Assembly

Last updated: 2026-05-23
Current phase: proposal

## Phase Verdict

- Current phase: proposal
- Why: Assembly now installs and loads as a working Codex plugin, but the 1.0 product promise, target user, success criteria, and release gate still need explicit alignment.
- Evidence: PR #1 merged the project-workflow foundation into `main`; local `main` is clean at merge commit `210b3fd`; `codex plugin marketplace upgrade assembly` installed Assembly `0.8.1` under `~/.codex/plugins/cache/assembly/assembly/0.8.1`; validators passed before merge; repo has been renamed to `benjaminsehl/assembly`.
- Structure decision: agent-only operating files now belong under `.agents/`, with root `AGENTS.md` as the visible entrypoint and `reference/` reserved for raw source material.
- Next gate: 1.0 proposal accepted by the user.

## Next Recommended Skills

- `product-discovery`
- `spec`

## Current 1.0 Direction

- Candidate wedge: install Assembly, scaffold a repo, say `next`, and have Codex orient to phase, missing context, and the next useful workflow without guessing.
- Primary user: Sai building real projects with Codex.
- Secondary user: people who want a compact Codex-native product-building workflow instead of a pile of overlapping skills.
- Default stance: optimize 1.0 as Sai's personal stack first, while keeping the public plugin installable, documented, and conflict-aware enough that another serious builder could adopt it.
- Recommended proof path: Assembly self-hosts the workflow, CFO proves a greenfield/restart setup, and Hyper remains the richer retrofit proof or release stretch.

## Open Questions

- Is 1.0 primarily a personal operating system or a public plugin others should install confidently?
- What exact behavior should count as success for `next` across proposal, prototype, build, and release phases?
- How much project-paper-trail scaffolding is helpful before it becomes ceremony?
- Should Assembly always default to draft PR handoff for material GitHub-backed changes, with local-only as the exception?
- Which real projects should prove 1.0: Assembly itself, Hyper, CFO, or all three?
- Should 1.0 include only skills/docs/scripts, or also a more automated installer/migration helper?
- How much of the future dream/desloppification workflow belongs in `.agents/` versus lifecycle references?

## Next Concrete Action

Review and accept or revise the 1.0 default stance in `docs/product/discovery-1-0.md`; once accepted, write the 1.0 spec.
