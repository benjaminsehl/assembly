# Decision: Dual-Runtime Support for Claude Code

Date: 2026-05-27

## Context

The 2026-05-23 decision ([Codex First, Hermes Next](2026-05-23-codex-first-hermes-next.md)) scoped Assembly 1.0 to Codex only and explicitly deprioritized Claude Code support. That decision was correct at the time: it kept 1.0 small and avoided turning the project into a compatibility exercise before the core product loop was proven.

Since then two things changed:

1. The Codex plugin loads and works locally, so the core control loop is no longer the open risk.
2. The Codex and Claude Code plugin formats turn out to be near-identical at the skill level. Both runtimes load `skills/<name>/SKILL.md` with the same YAML frontmatter. The differences are confined to two thin metadata files and one marketplace catalog. Adding Claude Code support is an afternoon of plumbing, not a parallel project.

## Decision

The same plugin bundle at `plugins/assembly/` ships as both a Codex plugin and a Claude Code plugin. The bundle carries two sibling manifest directories:

- `.codex-plugin/plugin.json` — Codex manifest.
- `.claude-plugin/plugin.json` — Claude Code manifest.

The repo also carries two marketplace catalogs:

- `.agents/plugins/marketplace.json` — Codex marketplace.
- `.claude-plugin/marketplace.json` — Claude Code marketplace.

Skills, references, templates, helper scripts, and personas remain a single source of truth shared by both runtimes. Validation requires both manifests and both marketplaces to be well-formed.

## Why This Extends Rather Than Reverses

This decision does not reverse the 2026-05-23 stance; it extends it. The original concern — "do not let portability eat 1.0" — still holds for anything that would require a third runtime, a protocol abstraction, or duplicated skill content. None of those are introduced here. The cost surface of dual-runtime support is bounded to:

- Two ~30-line JSON manifests.
- One marketplace catalog file.
- A validator update covering both shapes.
- Runtime-neutral phrasing in user-facing docs.

If that cost surface ever grows beyond bounded, the right move is to retire one runtime, not to introduce an abstraction layer.

## Implications

- 1.0 must pass install and smoke checks in both Codex and Claude Code.
- User-facing docs (README, INSTALL, SMOKE_TESTS, PRIVACY, TERMS, SPEC) describe both runtimes; the bundle and its skills remain runtime-neutral.
- Hermes orchestration remains the post-1.0 north star and is independent of this change.
- Skill bodies must not embed runtime-specific behaviour. If a skill needs to talk about runtime differences, do it in a `references/` doc, not in the public skill body.

## Out of Scope

- Other agent runtimes beyond Codex and Claude Code.
- A protocol-style adapter layer.
- Automatic runtime detection inside skills.
