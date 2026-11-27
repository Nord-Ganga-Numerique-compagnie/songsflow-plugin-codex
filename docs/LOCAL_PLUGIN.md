# SongsFlow local Codex plugin

The plugin provides the six existing songwriting tools and a songwriting skill.
It runs over stdio and starts an HTTP listener on an available **127.0.0.1** port
for temporary downloads and widget requests. It does not expose FL Studio control
tools. No hosting, account upload or public publication is required.

## Build and install

Install uv, Python 3.11+ and the frontend dependencies described in SONGSFLOW.md.
From the repository root:

```sh
npm --prefix web run build
python3 scripts/build_local_plugin.py
codex plugin marketplace add .
codex plugin add songsflow@songsflow-local
```

The marketplace lives in `.agents/plugins/marketplace.json`. The self-contained
plugin lives in `plugins/songsflow`; its generated runtime copies the Python app,
built editor and license notices. It installs only songwriting dependencies,
without the MIDI hardware and keyboard-control dependencies of the legacy bridge.
uv prepares a separate environment at first launch; this needs package network
access. Codex must be able to find `uv` in its PATH.

Open a new Codex chat, select SongsFlow, and ask:

> Create an eight-bar verse in C major at 100 BPM and export MIDI and a JSON backup.

Then try `Open SongsFlow`. Embedded editor rendering, audio attachment APIs and
local download navigation depend on the host and require live acceptance testing.
An MCP resource being readable does not prove it renders in Codex. If the editor
is unavailable, the tools still support song documents, validation and exports in
chat. Proposal acceptance happens in the editor, or through explicit chat review
when using song documents directly.

Export links work on this Mac while the plugin process runs and expire after
15 minutes. Download backups before closing the chat or restarting the plugin.

## Improve and retest

Edit the original files in `src/songsflow` and `web/src`, then rebuild using the
first two commands above. Do not edit generated `plugins/songsflow/runtime` or
Codex's installed cache. Bump both plugin manifest versions together for releases,
reinstall with `codex plugin add songsflow@songsflow-local`, and start a fresh chat
to load the revised server. The private portable ZIP is `dist/songsflow-local.zip`;
it does not include a virtual environment or credentials.

There is no project AGENTS.md or .codex directory yet. Suggested future structure:
`AGENTS.md` and `.codex/{agents,references,plans,todos,skills,automations}/`.
