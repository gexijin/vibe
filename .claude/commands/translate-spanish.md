# Translate English Tutorial to Spanish

Translate the English tutorial to Spanish: $ARGUMENTS

## Phase 1: Read the English Tutorial

1. **Read the English tutorial** at `docs/$ARGUMENTS`

If the file doesn't exist, report the error and stop.

## Phase 2: Check for Existing Spanish Translation

Check if a Spanish translation already exists at `docs/es/$ARGUMENTS`

- **If it exists:** Ask the user if they want to update the existing translation or start fresh
- **If it doesn't exist:** Proceed to create a new translation

## Phase 3: Translate to Spanish

Create the Spanish translation following these guidelines:

### Translation Rules

**Keep in English (do not translate):**
- Code blocks and commands
- Technical terms: Git, Docker, VS Code, Claude Code, WSL, Terminal, etc.
- File names and paths
- URLs and links
- Brand names and product names

**Translate to Spanish:**
- All instructional text
- Section headings
- Explanations and descriptions
- UI element names ONLY if the software has official Spanish localization
- Troubleshooting descriptions

### Language Guidelines

**Tone and Style:**
- Use formal "usted" form for consistency (not informal "tú")
- Keep sentences clear and direct
- Use natural Spanish phrasing, not word-for-word translation
- Maintain a friendly but professional tone

**Common Technical Translations:**
- Click = Haga clic en
- Type = Escriba
- Open = Abra
- Close = Cierre
- Save = Guarde
- File = Archivo
- Folder = Carpeta
- Settings = Configuración
- Install = Instale
- Download = Descargue
- Run = Ejecute
- Button = Botón
- Window = Ventana
- Next Steps = Próximos Pasos
- Troubleshooting = Solución de Problemas
- What You'll Need = Lo Que Necesitará
- Key Concepts = Conceptos Clave

### Formatting Requirements

1. **Home Link** - Change to `[Inicio](./es/)` at the top
2. **Preserve structure** - Keep the same sections and order as English
3. **Code blocks** - Copy exactly, do not translate
4. **Bold/backtick formatting** - Preserve all formatting
5. **Links** - Keep URLs unchanged, translate link text if appropriate

## Phase 4: Create the Spanish File

1. Create the `docs/es/` directory if it doesn't exist
2. Save the translation to `docs/es/$ARGUMENTS`
3. Update the creation credit at the bottom (keep author name, translate surrounding text):
   - "Creado por [Author Name](link) el [date]."

## Phase 5: Quality Review

Review the translation for:

- [ ] Natural Spanish flow (not literal translation)
- [ ] Consistent terminology throughout
- [ ] Correct Spanish punctuation (¿? and ¡! where needed)
- [ ] Gender agreement in adjectives and articles
- [ ] Proper accent marks (á, é, í, ó, ú, ñ)
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
- Spanish translations go in `docs/es/`
- Both should have the same filename
- When in doubt about a technical term, keep it in English
- Test that the Spanish home link `./es/` will work in the site structure
