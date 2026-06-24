# Review and Update a Translation

Review and update a translated tutorial to match the current English original.

`$ARGUMENTS` is `[language] [filename]`, where **language** is the translation
folder (`es`, `fr`, `de`, `ja`, or `zh`) and **filename** is the tutorial's
shared filename — e.g. `/review-translation fr Install_CLAUDE_Code_Win.md`.

- English original: `docs/<filename>`
- Translation: `docs/<language>/<filename>`

If the language is missing or unrecognized, ask the user which language to
review. If either file doesn't exist, report the error and stop.

Throughout, refer to the target language's existing files for conventions —
the project's per-language translation guides (`.claude/commands/translate-*.md`)
and the sibling tutorials already in `docs/<language>/`.

## Phase 1: Read Both Versions

1. **Read the English tutorial** at `docs/<filename>`.
2. **Read the translation** at `docs/<language>/<filename>`.
3. **Skim 1–2 sibling files** in `docs/<language>/` to absorb house conventions:
   register (e.g. usted / vous / Sie / です・ます), heading capitalization,
   recurring terminology, and the localized Home-link format.

## Phase 2: Compare and Sync Structure

Compare the English original with the translation:

1. **Structural differences:** missing sections, extra/outdated sections,
   different step ordering or numbering.
2. **Content differences:** updated instructions, changed commands, URLs,
   version numbers, or notes present in English but not the translation.
3. **Report findings** and ask: "Would you like me to update the
   `<language>` translation to match the current English version?"
4. **After approval, update:**
   - If the English was **restructured** (sections reordered, added, removed),
     prefer a **full rewrite** that mirrors the new structure rather than
     patching around the old shape.
   - If the change is minor, make targeted edits.
   - Translate new/changed content; remove outdated content; keep the section
     order identical to the English version.

## Phase 3: Naturalness Pass

Make it read like it was written by a native speaker, not translated.

- Hunt and remove calques / translationese (word-for-word constructions that
  are grammatical but unidiomatic).
- Use the **consistent register** the locale's sibling files use.
- Keep terminology consistent with the other translated tutorials.

## Phase 4: Succinctness Pass

Tighten the prose **without losing meaning**.

- Collapse wordy clauses, merge choppy short sentences, cut filler.
- This is a deliberate, separate pass from Phase 3 — read the whole file again
  with concision as the only goal.

## Phase 5: Anti-Over-Simplification Check

Confirm the tightening in Phase 4 didn't drop anything substantive.

- Diff the result back against the **English original**: every step, option,
  command, code block, note, warning, and nuance must still be present.
- Restore any lost detail (e.g. an "if you prefer" caveat, a troubleshooting
  bullet, an optional flag). Concise ≠ fewer facts.

## Invariants (must hold in every phase)

- [ ] Same filename as the English source; lives under `docs/<language>/`.
- [ ] Localized Home link at the top, matching sibling files' format.
- [ ] Same structure and section order as the English version.
- [ ] Commands, code blocks, and inline `code` are **never** translated.
- [ ] Technical terms (Git, Docker, VS Code, WSL, PowerShell) kept in English.
- [ ] UI button labels kept in English unless the project localizes them
      (**Authorize**, **Copy Code**, **Next**, **Install**).
- [ ] URLs and links unchanged and correct.
- [ ] Bold/backtick/heading formatting preserved.
- [ ] If the file has `title:`/`lang:` front matter, the `title` is the
      translated H1 and `lang` matches the folder.

## Phase 6: Report and Fix

Present findings to the user:

1. **Status** — up-to-date, or what was synced.
2. **Changes made** — structure, naturalness, succinctness, restored detail.
3. Apply remaining fixes with the Edit tool, preserving translation style.
4. Report completed changes.

Commit only when the user asks. Commit **one language per commit** (the single
translated file), and leave unrelated working-tree changes (e.g.
`.obsidian/workspace.json`) out of the commit.
