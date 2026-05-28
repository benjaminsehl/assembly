# Release Checklist: Assembly 1.0

Last updated: 2026-05-27
Status: draft

## Product Gate

- [ ] Founder accepts the 1.0 spec.
- [ ] Founder accepts the app-factory north star.
- [ ] 1.0 blockers are separated from post-1.0 orchestrator work.
- [ ] Product-discovery interview behavior is verified.
- [ ] `next` behavior is verified on a real project trail.

## Plugin Gate

- [ ] Codex manifest (`.codex-plugin/plugin.json`) name, version, description, and icon are correct.
- [ ] Claude Code manifest (`.claude-plugin/plugin.json`) name, version, description, and icon are correct.
- [ ] Marketplace metadata (`.claude-plugin/marketplace.json`) is correct.
- [ ] Only the 12 intended public skills are exposed in both runtimes.
- [ ] Skill graph validates.
- [ ] Plugin shape validates.
- [ ] Local conflict audit runs.
- [ ] Install and upgrade docs are accurate for both Codex and Claude Code.

## Project Scaffold Gate

- [ ] Root scaffold creates `AGENTS.md`, `.agents/`, `docs/`, and `reference/`.
- [ ] Existing `AGENTS.md` is not overwritten.
- [ ] Force scaffold preserves protected files and appends to `.agents/log.md`.
- [ ] Subproject scaffold creates `docs/projects/<slug>/`.

## Behavior Gate

- [ ] `next` repairs stale or missing status before dispatching.
- [ ] `next` asks one concise question when multiple next actions are plausible.
- [ ] `build` with a minimal prompt infers the next unambiguous build-track gate.
- [ ] GitHub handoff creates or updates a descriptive draft PR.
- [ ] Ready-for-review requires explicit user authorization.
- [ ] Merge requires explicit user direction and clean review-thread/check state or acknowledged risk.

## Proof Gate

- [ ] Assembly self-host proof is complete.
- [ ] CFO proof is complete.
- [ ] Hyper retrofit proof is complete or explicitly deferred.
- [ ] Smoke-test evidence is recorded.
- [ ] Release retro is recorded.

## Release Gate

- [ ] Version is bumped.
- [ ] Release PR is approved.
- [ ] PR is merged after explicit founder approval.
- [ ] Local Codex plugin is upgraded.
- [ ] Local Claude Code plugin is upgraded.
- [ ] Fresh Codex session confirms Assembly skills are visible.
- [ ] Fresh Claude Code session confirms Assembly skills are visible.
- [ ] `Use next` works in the installed plugin in both runtimes.

## Current Verdict

NO-GO until spec acceptance, release-candidate implementation, real smoke evidence, and CFO proof are complete.
