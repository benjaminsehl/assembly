# Source Notes

## Upstream Sources

This plugin adapts the lifecycle-command pattern from Addy Osmani's `agent-skills` repository:

- Repository: https://github.com/addyosmani/agent-skills
- Pinned upstream commit inspected for the initial build: `f17c6e88c904dc747381c374312c2d58e10647ae`
- Upstream license: MIT, copied to `docs/UPSTREAM_LICENSE_agent-skills_MIT.txt`

It also takes methodology inspiration from:

- Garry Tan `gstack`: https://github.com/garrytan/gstack
- Matt Pocock `skills`: https://github.com/mattpocock/skills
- Benjamin Sehl `agent-kernel`: https://github.com/benjaminsehl/agent-kernel

No GStack, Matt Pocock, or agent-kernel code is vendored.

## Current Adaptation

The plugin implements lifecycle workflows as agent skills (`skills/<name>/SKILL.md`) rather than as flat `.claude/commands/*.md` shortcuts. The skill format is portable: Claude Code loads it directly, and Codex loads the same files via its own plugin manifest. The dual-target bundle keeps one source of truth for the skill bodies while exposing runtime-appropriate metadata in `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`.

Earlier versions vendored many underlying workflow skills as triggerable skill directories. Version `0.7.0` intentionally shrinks the public surface and moves detailed workflow guidance into references to reduce context load and avoid collisions with users' existing skills. Version `0.7.1` adds `next` as a small continuation dispatcher without expanding the support-skill surface.

Public skills:

- `project-status`
- `next`
- `product-discovery`
- `prototype`
- `spec`
- `plan`
- `build`
- `test`
- `qa`
- `review`
- `code-simplify`
- `ship`

Detailed workflow references live under `references/workflows/`.

## Public License

This repository is public and uses the MIT license. Upstream MIT attribution for Addy-style source material is preserved separately.
