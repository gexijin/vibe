# CLAUDE.md

## What this is

A documentation/tutorial site teaching complete beginners how to "vibe code" with
Claude Code, VS Code, Docker, R, and Python. It also ships a `.devcontainer/` setup
that runs Claude Code and OpenAI Codex inside a `rocker/shiny-verse` container.

This repo has **no application code** — it is content (Markdown tutorials) plus a
Jekyll site published from `docs/`.

## Layout

- `docs/` — the Jekyll site. Tutorials are top-level `.md` files; `index.html` is the
  landing page with the tutorial graph; `_layouts/` and `_config.yml` configure Jekyll.
- `docs/{de,es,fr,ja,zh}/` — translations mirroring the English filenames.
- `.devcontainer/` — Docker dev container (amd64 and arm64 variants).
- `.claude/commands/` — slash commands (tutorial authoring + translation).
- `.claude/skills/`, `.claude/agents/` — skills and subagents.
- `docs/CLAUDE.md` — **detailed** reference: full tutorial index, learning paths,
  writing style guide, and translation rules. Read it before editing tutorials.

## Working on tutorials

- Audience is non-technical beginners — plain language, no jargon.
- Use `/tutorial [topic]` to draft and `/review-tutorial [file]` to polish.
- Follow the style guide in `docs/CLAUDE.md`: Home link at top, Key Concepts,
  step-by-step `## Step N:` headings, Troubleshooting, ~400 lines max.
- Keep technical terms (Git, Docker, VS Code) and commands untranslated.

## Translations

- Translation slash commands: `/translate-{chinese,french,german,spanish,general}`.
- `/review-translation [file]` updates a translation to match the English original.
- Each translated file keeps the same filename as its English source, under the
  matching language folder.
