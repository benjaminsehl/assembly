# Install and Use

This plugin can be registered with Codex as a private local marketplace. It provides seven command-like entry skills backed by a self-contained workflow skill library.

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
