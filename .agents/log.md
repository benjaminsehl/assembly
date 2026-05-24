# Agent Log

Append meaningful agent handoff events, skipped gates, recovery notes, and project-operation changes here.

## 2026-05-22

- Scaffolded Assembly's root project trail under `docs/`.
- Added GitHub handoff guidance for focused commits, draft PRs, self-review, simplification, and ready-for-review gates.
- Moved agent-only operating material under `.agents/` while keeping root `AGENTS.md` as the visible entrypoint.

## 2026-05-23

- Merged PR #1 into `main` at `210b3fd`, upgraded the local marketplace install to Assembly `0.8.1`, and repaired `docs/status.md` to reflect the post-merge proposal state.
- Used `next` to route into proposal-phase product discovery; recorded the recommended 1.0 stance as personal-stack-first with public installability as a quality bar.
- Recorded the product decision that Assembly 1.0 should finish the Codex plugin first; Claude support is not a near-term priority; Hermes orchestration is the post-1.0 north star.
- Captured usage feedback: `product-discovery` must ask more questions by default, and `build` with an empty/minimal prompt should infer the next build-track gate and proceed.

## 2026-05-24

- Used `next` to repair stale status after PR #2 was marked ready for review. Merge remains an explicit approval boundary; the next release step is merge plus local plugin upgrade only when the user asks for it.
