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

Codex does not expose Claude-style `.claude/commands/*.md` as the plugin primitive. This repo therefore implements natural-language lifecycle workflows as Codex skills.

Earlier versions vendored many underlying workflow skills as triggerable skill directories. Version `0.7.0` intentionally shrinks the public surface and moves detailed workflow guidance into references to reduce context load and avoid collisions with users' existing skills.

Public skills:

- `project-status`
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
