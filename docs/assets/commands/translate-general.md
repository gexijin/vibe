# Translate English Tutorial to Any Language

Translate the English tutorial to the specified language: $ARGUMENTS

**Expected format:** `[language] [filename]` (e.g., `French Claude_Code_Basic_Operations.md` or `Japanese Install_Claude_Code_MacOS.md`)

---

## Phase 1: Parse Arguments and Setup

1. **Parse the arguments** to identify:
   - **Target language** (first word)
   - **Tutorial filename** (remaining text)

2. **Determine the language folder code:**
   - French → `fr`
   - Spanish → `es`
   - Chinese → `zh`
   - Japanese → `ja`
   - German → `de`
   - Portuguese → `pt`
   - Italian → `it`
   - Korean → `ko`
   - Other → Ask user for 2-letter code

3. **Set language-specific conventions:**
   - Home link text (e.g., "Accueil", "Inicio", "首页", "ホーム")
   - Quotation style (e.g., « » for French, 「  」for Japanese)
   - Formal/informal address (e.g., "vous" vs "tu", "usted" vs "tú")
   - Attribution format (e.g., "Créé par", "Creado por", "由...创建")

---

## Phase 2: Read Source Tutorial

1. **Read the English tutorial** at `docs/[filename]`

2. **If file doesn't exist:** Report error and stop

3. **Analyze the content** to identify:
   - Main instructional text
   - AI prompts (text users type into Claude Code)
   - UI element references
   - Code blocks
   - Technical terms

---

## Phase 3: Check for Existing Translation

Check if a translation already exists at `docs/[language-code]/[filename]`

- **If it exists:** Ask user if they want to:
  - Update the existing translation
  - Start fresh (overwrite)
  - Cancel
- **If it doesn't exist:** Proceed to create new translation

---

## Phase 4: Translate Content

### 4A. What to Keep in English (DO NOT translate)

- Code blocks and terminal commands
- Technical terms: Git, Docker, VS Code, Claude Code, WSL, Terminal, Python, R, etc.
- File names and paths (e.g., `.claude/commands/`, `paper.md`)
- URLs and links
- Brand names and product names
- Programming keywords and function names

### 4B. What to Translate

1. **Main instructional text**
   - All explanations and descriptions
   - Section headings
   - Bullet points and lists
   - Troubleshooting descriptions

2. **AI Prompts** (CRITICAL - often missed!)
   - Translate ALL prompts that users type into Claude Code
   - These appear in code blocks but are natural language, not code
   - Example:
     ```
     English: "Create a simple countdown timer"
     French:  "Crée une application de minuterie simple"
     ```

3. **UI Elements**
   - Translate with English fallback in parentheses
   - Example: `**Autoriser** (ou **Authorize**)`
   - Only if software has official localization for that language

4. **Attribution line**
   - Translate "Created by" to target language
   - Keep author name and date unchanged

### 4C. Language-Specific Guidelines

**Tone:**
- Use the formal form appropriate for the language
- Keep sentences clear and direct
- Use natural phrasing, not word-for-word translation

**Punctuation:**
- Apply language-specific punctuation rules
- Use appropriate quotation marks for the language

**Common Section Translations:**
| English | French | Spanish | Chinese | Japanese |
|---------|--------|---------|---------|----------|
| Home | Accueil | Inicio | 首页 | ホーム |
| Key Concepts | Concepts Clés | Conceptos Clave | 关键概念 | 主要な概念 |
| What You'll Need | Ce Dont Vous Aurez Besoin | Lo Que Necesitará | 您需要准备 | 必要なもの |
| Step | Étape | Paso | 步骤 | ステップ |
| Next Steps | Prochaines Étapes | Próximos Pasos | 后续步骤 | 次のステップ |
| Troubleshooting | Dépannage | Solución de Problemas | 故障排除 | トラブルシューティング |
| Created by | Créé par | Creado por | 由...创建 | 作成者 |

---

## Phase 5: Create the Translated File

1. **Create the language directory** if it doesn't exist: `docs/[language-code]/`

2. **Write the translated file** to `docs/[language-code]/[filename]`

3. **Update the home link** at the top to use the language-specific text pointing to `./`

4. **Update the attribution** at the bottom with translated text

---

## Phase 6: Quality Review

Review the translation for:

- [ ] **Natural flow** - Reads naturally, not like a literal translation
- [ ] **AI prompts translated** - All user prompts in Claude Code are in target language
- [ ] **UI elements handled** - Translated with English fallback where appropriate
- [ ] **Consistent terminology** - Same terms used throughout
- [ ] **Proper punctuation** - Language-specific rules applied
- [ ] **Accent marks/characters** - All diacritics and special characters correct
- [ ] **Code blocks unchanged** - Terminal commands and code preserved exactly
- [ ] **Links working** - All URLs preserved, link text translated if appropriate
- [ ] **Same structure** - Matches the English original's organization
- [ ] **Attribution updated** - "Created by" translated appropriately

---

## Phase 7: Report to User

Present:

1. **Translation completed**
   - File location: `docs/[language-code]/[filename]`

2. **Summary of work**
   - Number of AI prompts translated
   - UI elements handled
   - Any terms kept in English (with reasoning)

3. **Key decisions made**
   - Translation choices worth noting
   - Ambiguous terms and how they were handled

4. **Recommendations**
   - Suggestions for improvement
   - Terms that may need native speaker review

---

## Notes

- English tutorials are in `docs/`
- Translations go in `docs/[language-code]/`
- Both should have the same filename
- When in doubt about a technical term, keep it in English
- AI prompts are the most commonly missed items - always check for them
- The home link should work in the site structure (`./` for relative linking)
