# Review and Update Japanese Translation

Review and update the Japanese translation for: $ARGUMENTS

## Phase 1: Read Both Versions

1. **Read the English tutorial** at `docs/$ARGUMENTS`
2. **Read the Japanese translation** at `docs/ja/$ARGUMENTS`

If either file doesn't exist, report the error and stop.

## Phase 2: Compare and Update

Compare the English original with the Japanese translation:

1. **Identify structural differences:**
   - Missing sections in Japanese version
   - Extra/outdated sections in Japanese version
   - Different step ordering

2. **Identify content differences:**
   - Updated instructions in English not reflected in Japanese
   - Changed commands, URLs, or version numbers
   - Added or removed content

3. **Report findings to user:**
   - List sections that need updating
   - Note any major structural changes required
   - Ask: "Would you like me to update the Japanese translation to match the current English version?"

4. **After user approval, update the Japanese translation:**
   - Translate new/changed content into Japanese
   - Remove outdated content
   - Maintain consistent structure with the English version

## Phase 3: Review Japanese Quality

Review the Japanese translation for quality, regardless of whether updates were needed:

### Translation Accuracy
- [ ] Technical terms translated correctly or appropriately kept in English
- [ ] Commands and code blocks unchanged (not translated)
- [ ] UI element names match actual Japanese UI (if localized) or kept in English
- [ ] URLs and links are correct

### Language Quality
- [ ] Natural, fluent Japanese (not word-for-word translation)
- [ ] Consistent terminology throughout
- [ ] Appropriate politeness level (です/ます form for tutorials)
- [ ] No unnatural katakana overuse
- [ ] Clear, concise sentences

### Formatting Consistency
- [ ] Same structure as English version
- [ ] `[ホーム](./ja/)` link at the top (Japanese home page)
- [ ] Step headings follow same pattern
- [ ] Code blocks preserved exactly
- [ ] Bold/backtick formatting preserved

### Common Issues to Check
- [ ] Particles used correctly (は/が, を, に, で, etc.)
- [ ] No mixed formal/informal language
- [ ] Numbers and measurements in appropriate format
- [ ] Dates in Japanese format if applicable

## Phase 4: Report and Fix

Present findings to the user:

1. **Translation Status** - Up-to-date or updates needed
2. **Quality Issues Found:**
   - Translation errors
   - Awkward phrasing
   - Inconsistencies
   - Formatting problems
3. **Recommended Changes** - Specific fixes with context

Ask: "Would you like me to apply these quality improvements?"

After user approval:
1. Apply fixes using the Edit tool
2. Maintain the translation style and tone
3. Keep changes minimal - fix issues without rewriting entire sections
4. Report completed changes

## Notes

- English tutorials are in `docs/`
- Japanese translations are in `docs/ja/`
- Both should have the same filename
- Technical terms (Git, Docker, VS Code, etc.) are usually kept in English
- Command-line instructions should never be translated
