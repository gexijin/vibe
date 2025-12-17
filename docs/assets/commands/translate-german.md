# Translate English Tutorial to German

Translate the English tutorial to German: $ARGUMENTS

## Phase 1: Read the English Tutorial

1. **Read the English tutorial** at `docs/$ARGUMENTS`

If the file doesn't exist, report the error and stop.

## Phase 2: Check for Existing German Translation

Check if a German translation already exists at `docs/de/$ARGUMENTS`

- **If it exists:** Ask the user if they want to update the existing translation or start fresh
- **If it doesn't exist:** Proceed to create a new translation

## Phase 3: Translate to German

Create the German translation following these guidelines:

### Translation Rules

**Keep in English (do not translate):**
- Code blocks and commands
- Technical terms: Git, Docker, VS Code, Claude Code, WSL, Terminal, etc.
- File names and paths
- URLs and links
- Brand names and product names

**Translate to German:**
- All instructional text
- Section headings
- Explanations and descriptions
- UI element names ONLY if the software has official German localization
- Troubleshooting descriptions

### Language Guidelines

**Tone and Style:**
- Use formal "Sie" form for consistency (not informal "du")
- Keep sentences clear and direct
- Use natural German phrasing, not word-for-word translation
- Maintain a friendly but professional tone

**Common Technical Translations:**
- Click = Klicken Sie auf
- Type = Geben Sie ein / Tippen Sie
- Open = Öffnen Sie
- Close = Schließen Sie
- Save = Speichern Sie
- File = Datei
- Folder = Ordner
- Settings = Einstellungen
- Install = Installieren Sie
- Download = Laden Sie herunter / Herunterladen
- Run = Führen Sie aus / Ausführen
- Button = Schaltfläche / Button
- Window = Fenster
- Next Steps = Nächste Schritte
- Troubleshooting = Fehlerbehebung
- What You'll Need = Was Sie benötigen
- Key Concepts = Wichtige Konzepte
- Prerequisites = Voraussetzungen
- Getting Started = Erste Schritte
- Step = Schritt
- Note = Hinweis
- Tip = Tipp
- Warning = Warnung
- Overview = Überblick
- Summary = Zusammenfassung
- Example = Beispiel
- See also = Siehe auch

### Formatting Requirements

1. **Home Link** - Change to `[Startseite](./)` at the top
2. **Preserve structure** - Keep the same sections and order as English
3. **Code blocks** - Copy exactly, do not translate
4. **Bold/backtick formatting** - Preserve all formatting
5. **Links** - Keep URLs unchanged, translate link text if appropriate
6. **Punctuation** - Use German punctuation rules:
   - Use German quotation marks „ " (opening at bottom, closing at top)
   - Compound words are written together (e.g., Fehlerbehebung, not Fehler Behebung)

## Phase 4: Create the German File

1. Create the `docs/de/` directory if it doesn't exist
2. Save the translation to `docs/de/$ARGUMENTS`
3. Update the creation credit at the bottom (keep author name, translate surrounding text):
   - "Erstellt von [Author Name](link) am [date]."

## Phase 5: Quality Review

Review the translation for:

- [ ] Natural German flow (not literal translation)
- [ ] Consistent terminology throughout
- [ ] Correct German punctuation
- [ ] Correct grammatical cases (Nominativ, Akkusativ, Dativ, Genitiv)
- [ ] Proper umlauts (ä, ö, ü) and ß
- [ ] Code blocks unchanged
- [ ] All links working
- [ ] Same structure as English original

## Phase 6: Report

Present to the user:

1. **Translation completed** - Confirm file location
2. **Key decisions made** - Any translation choices worth noting
3. **Recommendations** - Suggestions for improvement if any

## Notes

- English tutorials are in `docs/`
- German translations go in `docs/de/`
- Both should have the same filename
- When in doubt about a technical term, keep it in English
- Test that the German home link `./` will work in the site structure
