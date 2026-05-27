# Project Status: Assembly

Last updated: 2026-05-27
Current phase: proposal

## Phase Verdict

- Current phase: proposal
- Why: Assembly now installs and loads as a working Codex plugin, and the product direction is sharper: Assembly 1.0 proves the human-led Codex control loop for an eventual agentic app factory; Hermes becomes the post-1.0 orchestrator only after the loop is reliable.
- Evidence: PR #1 merged the project-workflow foundation into `main`; PR #2 merged as `15cb36a`; Assembly `0.8.3` is installed under `~/.codex/plugins/cache/assembly/assembly/0.8.3`; `docs/specs/assembly-1-0.md` defines the 1.0 behavior spec; `docs/product/app-factory-north-star.md`, `docs/research/2026-05-27-agentic-orchestration-research.md`, `docs/plans/2026-05-27-assembly-1-0-release-plan.md`, and `docs/plans/2026-05-27-hermes-orchestrator-roadmap.md` now capture the north star, research synthesis, release path, and post-1.0 roadmap.
- Structure decision: agent-only operating files now belong under `.agents/`, with root `AGENTS.md` as the visible entrypoint and `reference/` reserved for raw source material.
- Product decision: 1.0 is Codex-first; Claude support is not a near-term priority; Hermes orchestration is the post-1.0 strategic direction.
- Product-intent completeness: what is being built, why it matters, and what good looks like are now explicit in the spec and north-star docs.
- Next gate: founder review/acceptance of `docs/specs/assembly-1-0.md`, then `plan` for release-candidate implementation and proof tasks.

## Next Recommended Skills

- `spec`
- `plan`

## Current 1.0 Direction

- Candidate wedge: install Assembly, scaffold a repo, say `next`, and have Codex orient to phase, missing context, and the next useful workflow without guessing or silently taking product authority.
- Primary user: Sai acting as founder/product director while Codex helps clarify, execute, verify, and preserve the project trail.
- Secondary user: people who want a compact Codex-native product-building workflow instead of a pile of overlapping skills.
- Default stance: optimize 1.0 as Sai's personal stack first, while keeping the public plugin installable, documented, and conflict-aware enough that another serious builder could adopt it.
- Recommended proof path: Assembly self-hosts the workflow, CFO proves a greenfield/restart setup, and Hyper remains the richer retrofit proof or release stretch.
- Post-1.0 north star: Hermes orchestrates scoped Codex sessions using Assembly's project trail, phase gates, and GitHub handoff loop.
- Latest usage feedback: `product-discovery` should interview before deciding unless delegated; empty or minimal `build` prompts should infer and execute the first unambiguous build-track gate.

## 1.0 Open Questions

- Founder acceptance: is the 1.0 spec and north-star framing right?
- CFO proof scope: how much should the proof mutate `/Users/sai/cfo` versus inspect and report first?
- Release-candidate timing: should Hyper retrofit stay stretch, or become blocking after CFO?

## Next Concrete Action

Review `docs/specs/assembly-1-0.md` and `docs/product/app-factory-north-star.md`; once accepted, use `plan` to turn `docs/plans/2026-05-27-assembly-1-0-release-plan.md` into implementation and proof tasks.
