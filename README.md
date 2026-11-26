# SongsFlow

**From first idea to finished song — a ChatGPT app for musicians who create in FL Studio.**

SongsFlow helps songwriters and producers capture lyrics, chords and a reference recording, shape a musical brief, and carry it into FL Studio. It is aimed at people who already know music and want to spend less time reconstructing an idea before producing it.

Start with lyrics and chords, or attach a guitar-and-vocal recording as a reference. The current prototype uses **manual lyric, chord, tempo and timing input**. Automatic analysis of recordings and guided production inside FL Studio are planned capabilities.

## Start here

- **[SongsFlow setup and usage](docs/SONGSFLOW.md)** — run the embedded editor and HTTP MCP server, connect ChatGPT, and export files.
- **[Original FL Studio MCP Server guide](docs/FL_STUDIO_MCP.md)** — desktop installation, virtual MIDI, controller scripts, tools, examples and troubleshooting.
- **[Privacy and data handling](docs/PRIVACY.md)** — draft storage, reference audio, temporary downloads and release requirements.

## What works in the prototype

- Write lyrics and place chords visually above the words.
- Create named sections and arrange or repeat them.
- Enter tempo and choose 4/4, 3/4 or 6/8.
- Attach MP3, WAV or M4A reference audio, up to 20 MB.
- Set chord durations on a beat grid, or tap changes during playback and edit start/end timestamps to follow a performance.
- Preview chords with a simple synthesized piano-like sound.
- Export chord MIDI, annotated lyric text and the unchanged reference recording as separate files.
- Save and import portable JSON song backups.
- Review ChatGPT's proposed lyric or chord changes before applying them.

The app does not currently transcribe audio, detect chords or estimate tempo. Reference recordings stay in browser memory during editing and are uploaded to the app server only for explicit audio export.

## From an idea to FL Studio

1. **Capture:** open SongsFlow in ChatGPT, write your lyrics and chords, and optionally attach a recording.
2. **Shape:** set tempo, arrange sections and mark chord timing. Review and correct the song before export.
3. **Export:** download MIDI, lyric text and, when attached, the original audio. Keep a JSON backup of your editable song.
4. **Continue in FL Studio:** match the project tempo and place MIDI and audio at the same project origin. Paste lyric text into project notes or Fruity NoteBook 2.

The reference recording is copied unchanged; rearranging sections does not rearrange the audio. Direct sending to FL Studio and assistance with arrangement, sounds and production remain roadmap work.

## Two components, separate workflows

| Component | Purpose | Guide |
| --- | --- | --- |
| SongsFlow ChatGPT app | Embedded songwriting editor, reference playback and file exports through an HTTP MCP server | [SongsFlow](docs/SONGSFLOW.md) |
| FL Studio MCP Server | Local desktop bridge using MIDI, JSON files and FL Studio controller scripts over stdio MCP | [Original server guide](docs/FL_STUDIO_MCP.md) |

The public songwriting endpoint does not expose the desktop control tools. The original desktop installers configure the local FL Studio bridge; they do not deploy the ChatGPT app.

## Development and setup

The SongsFlow app requires **Python 3.11+** (3.12 recommended), **Node 24**, **uv** and **npm**. Follow the [setup guide](docs/SONGSFLOW.md#run-and-connect) for dependency installation, widget building, local startup and HTTPS deployment for ChatGPT.

After setup, run the app checks from the repository root:

```sh
uv run --extra app pytest -q tests
uv run ruff check .
cd web
npm test
npm run test:e2e
npm run build
```

Browser tests use a mocked ChatGPT host. Local checks do not establish live ChatGPT attachment support or successful FL Studio import; those still require acceptance testing in the actual clients. See the setup guide for browser requirements and further validation commands.

GitHub stores committed source code and documentation. Codex cloud environment installation scripts, startup instructions, network rules and secrets are configured separately in environment settings; editing this README does not update those settings automatically.

## Roadmap

- Validate the connected ChatGPT experience and the full file-import workflow with FL Studio users.
- Estimate tempo and chord progressions from recordings, with musician review and correction.
- Connect the songwriting workspace to a local FL Studio companion.
- Help musicians develop the idea through arrangement, sound choices and production, with user-approved actions.

These are product goals, not shipped features or guarantees of analysis accuracy.

## Privacy and song ownership

There is no permanent song database or analytics in the prototype. Chat drafts are a convenience, not a guaranteed song library; download backups of work you want to keep. Export links expire after 15 minutes. ChatGPT's own handling of conversations and attachments is governed by OpenAI's applicable policies and your settings.

Use lyrics and recordings you have permission to use. Read the [privacy notice](docs/PRIVACY.md) before deployment, including the operator details and hosting requirements that must be completed before public distribution.

## Credits and license

SongsFlow builds on [karl-andres/fl-studio-mcp](https://github.com/karl-andres/fl-studio-mcp). The original architecture, setup instructions, tool reference and credits are retained in the [FL Studio MCP Server guide](docs/FL_STUDIO_MCP.md).

[MIT license](LICENSE). Third-party dependencies retain their own licenses; the widget build includes notices for bundled dependencies.
