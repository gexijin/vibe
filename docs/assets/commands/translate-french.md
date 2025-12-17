# Translate English Tutorial to French

Translate the English tutorial to French: $ARGUMENTS

## Phase 1: Read the English Tutorial

1. **Read the English tutorial** at `docs/$ARGUMENTS`

If the file doesn't exist, report the error and stop.

## Phase 2: Check for Existing French Translation

Check if a French translation already exists at `docs/fr/$ARGUMENTS`

- **If it exists:** Ask the user if they want to update the existing translation or start fresh
- **If it doesn't exist:** Proceed to create a new translation

## Phase 3: Translate to French

Create the French translation following these guidelines:

### Translation Rules

**Keep in English (do not translate):**
- Code blocks and commands
- Technical terms: Git, Docker, VS Code, Claude Code, WSL, Terminal, etc.
- File names and paths
- URLs and links
- Brand names and product names

**Translate to French:**
- All instructional text
- Section headings
- Explanations and descriptions
- UI element names ONLY if the software has official French localization
- Troubleshooting descriptions

### Language Guidelines

**Tone and Style:**
- Use formal "vous" form for consistency (not informal "tu")
- Keep sentences clear and direct
- Use natural French phrasing, not word-for-word translation
- Maintain a friendly but professional tone

**Common Technical Translations:**
- Click = Cliquez sur
- Type = Tapez / Saisissez
- Open = Ouvrez
- Close = Fermez
- Save = Enregistrez
- File = Fichier
- Folder = Dossier
- Settings = Paramètres
- Install = Installez
- Download = Téléchargez
- Run = Exécutez
- Button = Bouton
- Window = Fenêtre
- Next Steps = Prochaines Étapes
- Troubleshooting = Dépannage
- What You'll Need = Ce Dont Vous Aurez Besoin
- Key Concepts = Concepts Clés
- Prerequisites = Prérequis
- Getting Started = Premiers Pas
- Step = Étape
- Note = Remarque
- Tip = Astuce
- Warning = Avertissement

### Formatting Requirements

1. **Home Link** - Change to `[Accueil](./fr/)` at the top
2. **Preserve structure** - Keep the same sections and order as English
3. **Code blocks** - Copy exactly, do not translate
4. **Bold/backtick formatting** - Preserve all formatting
5. **Links** - Keep URLs unchanged, translate link text if appropriate
6. **Punctuation** - Use French punctuation rules:
   - Add a non-breaking space before : ; ! ? » and after «
   - Use French quotation marks « » when appropriate

## Phase 4: Create the French File

1. Create the `docs/fr/` directory if it doesn't exist
2. Save the translation to `docs/fr/$ARGUMENTS`
3. Update the creation credit at the bottom (keep author name, translate surrounding text):
   - "Créé par [Author Name](link) le [date]."

## Phase 5: Quality Review

Review the translation for:

- [ ] Natural French flow (not literal translation)
- [ ] Consistent terminology throughout
- [ ] Correct French punctuation (spaces before : ; ! ?)
- [ ] Gender agreement in adjectives and articles
- [ ] Proper accent marks (é, è, ê, ë, à, â, ù, û, ô, î, ï, ç)
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
- French translations go in `docs/fr/`
- Both should have the same filename
- When in doubt about a technical term, keep it in English
- Test that the French home link `./fr/` will work in the site structure
