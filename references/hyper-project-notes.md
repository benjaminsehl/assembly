# Hyper Project Notes

Use this when retrofitting a project that already has many useful notes but did not start from the four-phase project structure.

The inspected Hyper checkout showed valuable artifacts spread across:

- Top-level product and design docs.
- `.agents/` kernel-style notes, knowledge files, and decisions.
- `docs/plans/` dated specs and implementation plans.
- API docs and migration plans.

This is useful context, but it creates a resume problem: a future session can find many documents without a single current phase, next gate, or project verdict.

## Retrofit Approach

1. Use `project-status` first. Do not move files before understanding which project slice is being assessed.
2. Create phase docs at the closest project boundary:
   - Whole app: `/Users/sai/hyper/docs/project/`.
   - Cross-cutting app slice: `/Users/sai/hyper/docs/project/projects/<slug>/` or `/Users/sai/hyper/docs/projects/<slug>/`.
   - Clear code subdirectory, such as an iOS client: the subdirectory's own `docs/project/`.
3. Link existing artifacts instead of copying them:
   - Product/design docs into proposal.
   - Existing specs and dated plans into build.
   - QA evidence and release decisions into release.
   - `.agents/decisions` or ADRs into decisions.
4. Fill gaps with explicit "missing" entries, especially:
   - What becomes 10x better.
   - What good looks like.
   - Assumptions and principles.
   - Prototype verdict, if no prototype phase existed.
   - Release grading and follow-up learning.
5. Keep `.agents/` as broader durable agent context if the repo already uses it. The project workspace should not replace it; it should make a slice resumable and preserve the reason decisions exist.

## Retrofit Output

For each slice, produce:

- Current phase.
- Existing artifacts linked by path.
- Missing proposal/prototype/build/release evidence.
- Next recommended skills.
- One next action.
