# Install and Use

This plugin can be registered with Codex as a public GitHub marketplace or local marketplace. It provides project lifecycle, product, prototype, design, business, QA, engineering, launch, retro, and learning entry skills backed by a self-contained workflow skill library.

## Register the Marketplace

From this local checkout:

```bash
codex plugin marketplace add /Users/sai/codex-agent-skills
```

From GitHub:

```bash
codex plugin marketplace add benjaminsehl/codex-agent-skills
```

The marketplace name is `codex-agent-skills`.

## Enable the Plugin

If Codex exposes the plugin in the UI, enable `Codex Agent Skills` from the plugin picker after adding the marketplace.

If enabling manually through config is needed, the expected config key shape is:

```toml
[plugins."codex-agent-skills@codex-agent-skills"]
enabled = true
```

After changing plugin availability or config, restart Codex so the skill list is refreshed.

## Invocation Pattern

Codex does not need Claude-style slash commands. Use the entry skill names in natural language:

```text
Use spec to define this feature before coding.
Use plan to break the approved spec into tasks.
Use build to implement the next planned slice.
Use test to prove this bug and guard against regression.
Use review to check the current diff.
Use code-simplify on the changed files.
Use ship to make a go/no-go release decision.
Use product-discovery on this idea.
Use founder-review on this plan.
Use business-model-review on this product concept.
Use design-plan-review before we build this UI.
Use new-project to scaffold this project.
Use prototype to explore this direction before build.
Use project-status to tell me what phase we are in and what skills to use next.
Use qa on this local app.
Use health-check on this repo.
Use retro on what we shipped this week.
Use learn to capture this project preference.
```

For deterministic project scaffolding from this checkout:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name"
```

For a subproject:

```bash
python3 scripts/scaffold_project.py --root /path/to/repo --name "Project Name" --slug project-name
```

For a child project inside an existing project workspace:

```bash
python3 scripts/scaffold_project.py \
  --root /path/to/repo \
  --parent docs \
  --name "Agent Layer" \
  --slug agent-layer
```

When a GitHub marketplace copy is already registered and this repo receives updates, refresh it with:

```bash
codex plugin marketplace upgrade codex-agent-skills
```

## Development Loop

While building this plugin:

```bash
cd /Users/sai/codex-agent-skills
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
```

```bash
python3 scripts/validate_plugin.py
python3 scripts/validate_skill_graph.py
```
