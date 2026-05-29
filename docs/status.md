# Project Status: Assembly

Last updated: 2026-05-29
Current phase: proposal
Traffic state: pre-live

## Autonomy

- Traffic state: pre-live. Assembly is not yet depended on by real users, so agents run the roadmap autonomously — open PRs, run reviewer sub-agents, merge, and (where a deploy path exists) deploy — escalating only product/UX decisions and always-ask floor items. Flip to `live` when external builders depend on the published plugin and you want the deploy-to-users moment to become a founder GO/NO-GO.
- Escalation model defined in `docs/decisions/2026-05-29-autonomy-escalation-model.md` and `plugins/assembly/references/agent-operating-protocol.md`.

## Phase Verdict

- Current phase: proposal
- Why: Assembly now installs and loads as a working plugin in both Codex and Claude Code, and the product direction is sharper: Assembly 1.0 proves the human-led control loop for an eventual agentic app factory across both runtimes; a post-1.0 orchestrator becomes the next step only after the loop is reliable.
- Evidence: PR #1 merged the project-workflow foundation into `main`; PR #2 merged as `15cb36a`; PR #4 added dual-runtime support via `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and validator/audit-script updates; Assembly `0.8.3` is installed under `~/.codex/plugins/cache/assembly/assembly/0.8.3`; `docs/specs/assembly-1-0.md` defines the 1.0 behavior spec; `docs/product/app-factory-north-star.md`, `docs/research/2026-05-27-agentic-orchestration-research.md`, `docs/plans/2026-05-27-assembly-1-0-release-plan.md`, and `docs/plans/2026-05-27-post-1-0-orchestrator-roadmap.md` now capture the north star, research synthesis, release path, and post-1.0 roadmap.
- Structure decision: agent-only operating files now belong under `.agents/`, with root `AGENTS.md` as the visible entrypoint and `reference/` reserved for raw source material.
- Product decision: 1.0 ships as a dual-runtime plugin (Codex + Claude Code) from the same bundle and must pass install/smoke checks in both runtimes; post-1.0 orchestration is the next strategic direction. See `docs/decisions/2026-05-27-dual-runtime-claude-code.md`.
- Product-intent completeness: what is being built, why it matters, and what good looks like are now explicit in the spec and north-star docs.
- Next gate: founder review/acceptance of `docs/specs/assembly-1-0.md`, then `plan` for release-candidate implementation and proof tasks.

## Next Recommended Skills

- `spec`
- `plan`

## Current 1.0 Direction

- Candidate wedge: install Assembly, scaffold a repo, say `next`, and have Codex orient to phase, missing context, and the next useful workflow without guessing or silently taking product authority.
- Primary user: Ben acting as founder/product director while agents help clarify, execute, verify, and preserve the project trail.
- Secondary user: people who want a compact Codex-native product-building workflow instead of a pile of overlapping skills.
- Default stance: optimize 1.0 as Ben's personal stack first, built in public so other builders can adopt it if they want; they are not the audience 1.0 is designed around.
- Recommended proof path: Assembly self-hosts the workflow, CFO proves a greenfield/restart setup, and Hyper remains the richer retrofit proof or release stretch.
- Post-1.0 north star: a post-1.0 orchestrator coordinates scoped agent sessions using Assembly's project trail, phase gates, and GitHub handoff loop.
- Latest usage feedback: `product-discovery` should interview before deciding unless delegated; empty or minimal `build` prompts should infer and execute the first unambiguous build-track gate.

## 1.0 Open Questions

- Founder acceptance: is the 1.0 spec and north-star framing right?
- CFO proof scope: how much should the proof mutate `/Users/sai/cfo` versus inspect and report first?
- Release-candidate timing: should Hyper retrofit stay stretch, or become blocking after CFO?

## Next Concrete Action

Review `docs/specs/assembly-1-0.md` and `docs/product/app-factory-north-star.md`; once accepted, use `plan` to turn `docs/plans/2026-05-27-assembly-1-0-release-plan.md` into implementation and proof tasks. Plugin version is now `0.9.0` (testing pass before 1.0).
