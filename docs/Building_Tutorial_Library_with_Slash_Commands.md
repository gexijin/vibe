# How Claude Code helped me create these tutorials

In mid-December 2025, I spent 2 hours trying to help my research assistant install Claude Code over Zoom. I realized that someone like her needs some specific, hands-on instructions, so I set out to create comprehensive tutorials for Claude Code. My goal: hands-on, focused tutorials that walk complete beginners through real tasks step by step. No theory dumps. No comprehensive reference manuals. Just "do this, then this, then this" until you've accomplished something concrete.

What started as a few documentation files quickly evolved into a multi-language learning platform with over 100 tutorial documents. The secret? I didn't write them all manually. Instead, I built a set of custom slash commands (reusable prompts, essentially) that transformed Claude Code into an automated documentation factory—one that consistently produces tutorials in my hands-on, step-by-step style.

## The Challenge

Creating tutorials is time-consuming. Each one requires research for current best practices, structured beginner-friendly writing, consistent formatting, technical accuracy validation, translation into multiple languages, and ongoing maintenance as tools evolve. Doing this manually for 20+ tutorials in 3+ languages would take weeks.

## The Solution: From Manual Process to Automated Slash Commands

I created five specialized slash commands that handled the entire tutorial lifecycle.

### [`/tutorial`](./assets/commands/tutorial.md) - The Tutorial Generator

I created the first few tutorials manually through interactive prompting with Claude. Refined the process through iteration, then asked Claude to codify the working process into a slash command.

This is exactly the pattern described in my [research paper tutorial](./Writing_Research_Paper_Claude_Code.md): go through the workflow manually, then in the final step, ask Claude to save it as a reusable command that captures the proven workflow:
1. **Research**: Claude searches the web for current information—no outdated version numbers or deprecated methods
2. **Plan**: Claude presents what it learned, recommends an approach, and outlines major steps
3. **Iterate**: I review the plan, prompt Claude to revise multiple times until satisfied
4. **Write**: After approval, Claude writes following strict formatting rules:
   - Home link at top
   - Engaging hook
   - Key concepts
   - Step-by-step instructions with action verbs
   - Troubleshooting section
   - Creation date
5. **Test**: I test the steps myself in a separate terminal, revise if needed
6. **Polish**: Sometimes I edit manually, sometimes I ask Claude to do it

The command enforces consistent structure across all tutorials. Every tutorial feels like it came from the same author—because they followed the same systematic process. I generated 20+ tutorials covering topics from basic Git operations to advanced Docker workflows.

### [`/review-tutorial`](./assets/commands/review-tutorial.md) - The Quality Control Bot

For this one, I simply asked Claude to "create a slash command to review tutorials." No detailed specifications. Claude generated a comprehensive three-phase workflow with 30+ quality criteria organized into categories:

- **Content Quality**: title, hook, key concepts, prerequisites, step flow, next steps, troubleshooting
- **Formatting Standards**: home link, step headings, bullet points, bold/backticks, code blocks, paragraphs
- **Beginner-Friendliness**: menu-based instructions, platform differences, exact click targets, no jargon
- **Technical Accuracy**: correct commands, current UI, realistic time estimates
- **Writing Quality**: grammar, consistent terminology, concise language

The command presents findings in a structured report, then applies fixes after approval. Why was this needed? Two reasons: Claude doesn't always follow the `/tutorial` rules strictly, and the `/tutorial` command itself evolved as I built more tutorials. The review command lets me batch-polish earlier tutorials to conform with the latest standards.

### [`/translate-chinese`](./assets/commands/translate-chinese.md) & [`/translate-spanish`](./assets/commands/translate-spanish.md) - The Localization Engine

The Japanese translations came first—without a slash command. I simply asked Claude Code to translate all the tutorials to Japanese in one prompt. Claude automatically spawned 8 subagents running in parallel, each handling different tutorials simultaneously.

For subsequent languages, I asked Claude to "create a slash command for translating tutorials to Chinese"—no specific guidelines. Claude generated a six-phase workflow with comprehensive rules:

- **Translation Rules**: Keep code blocks, technical terms (Git, Docker, VS Code), file paths, and URLs in English; translate instructional text, headings, and explanations
- **Language Guidelines**: Tone and style rules, common technical translations (Click = 点击, Install = 安装), formal address conventions
- **Formatting Requirements**: Localized home link, preserved structure, correct punctuation (。，！？ for Chinese, ¿? ¡! for Spanish)
- **Quality Review**: Natural flow checklist, consistent terminology, proper character usage

With the slash commands ready, I asked Claude Code to translate all 25 tutorials using subagents. The entire translation—50 new files across two languages—took only 15 minutes.

The result: 81 translated tutorial files across Chinese, Spanish, French, German, and Japanese directories—all maintaining consistent quality and structure.

### [`/review-translation`](./assets/commands/review-translation.md) - The Translation Maintenance Tool

Tutorials evolve. Commands change. New sections get added. This command keeps translations in sync through a four-phase workflow:

1. **Read Both Versions**: Load English original and translation side-by-side
2. **Compare and Update**: Identify missing sections, outdated content, changed commands or URLs
3. **Review Quality**: Check translation accuracy, language quality, formatting consistency
4. **Report and Fix**: Present findings, get approval, apply updates

The quality review is thorough—for Japanese, it checks natural phrasing (not word-for-word), appropriate politeness level (です/ます form), correct particle usage (は/が, を, に, で), and no unnatural katakana overuse. When I updated English tutorials, I could quickly propagate changes to all translations while maintaining language quality.

### Polishing Translations for Natural Flow

After syncing translations with English originals, I added a final polish step: editing each translated document on its own for language quality, without comparing to English. This step focuses purely on making the text read naturally to native speakers.

I used prompts in the target language. Instead of asking Claude in English to "polish this Japanese document," I used ChatGPT to write the prompts in Japanese, Chinese, or Spanish. This seemed to produce better results—Claude appeared to think more naturally in that language when the instructions were also in that language.

For example, to polish Chinese documents, I used: 
"修改 @docs/zh/ 目录下的中文文档。中文需要流畅、准确、言简意赅。提示词也要用中文。 Use subagents." For Spanish: "Revisa los documentos en @docs/es/. El español debe ser fluido, preciso y conciso. Use subagents." For Japanese: "@docs/ja/ のドキュメントを修正してください。日本語は流暢で正確、簡潔にしてください。Use subagents."

Better models such as Opus 4.5 also seem to help. This polish step caught awkward phrasings that weren't technically wrong but didn't sound natural. Combined with subagents, I could polish all 25+ documents in each language in a single batch operation. 

## Scaling with Subagents

For truly parallel work, I used Claude's subagent feature. When polishing Japanese translations, I launched multiple review agents simultaneously, processing 19 files with coordinated improvements.

The combination of slash commands for structured workflows and subagents for parallelization created a documentation pipeline that scaled far beyond what manual effort could achieve.

## The Results

In less than two weeks, I created 20+ English tutorials covering beginner to intermediate topics, 81 translated tutorials across 3 languages, consistent quality through automated review processes, and maintainable documentation with sync tools for translations.

All tutorials follow the same structure, writing style, and formatting conventions—because they were generated by the same systematic process.

## Key Lessons

- **Start manual, then automate.** Do the task manually first, refine the process, then ask Claude to save it as a command.
- **Structure commands as multi-phase workflows.** Tell Claude how to think through the problem, not just what to do.
- **Build quality control into the process.** Create a review command alongside your generation command.
- **Make commands collaborative, not autonomous.** Include approval steps. Claude handles tedious parts; you make strategic decisions.
- **Use subagents for batch processing.** When processing many documents, explicitly say "Use subagents" in your prompt. Press Shift+Tab first to enable auto-accept mode—subagents won't ask for permissions, making parallel processing seamless.

## Conclusion

Building this tutorial library taught me that automation isn't about removing humans from the process—it's about amplifying human judgment. I didn't write 100+ tutorials manually, but every single one reflects my standards, my structure, and my approval.

Slash commands transformed Claude Code from a helpful assistant into a documentation factory that works at my direction, maintains my standards, and scales to whatever size project I need.

If you have repetitive documentation tasks, don't keep doing them manually. Build the slash command once, then deploy it dozens or hundreds of times.

That's the power of systematic automation.

---

*Want to see the slash commands I built? Check out the [commands folder](./assets/commands/). The full tutorial library is available at the [project documentation site](https://github.com/gexijin/vibe/tree/main/docs).*

---

**P.S.** This blog post was itself drafted by Claude Code through iterative prompting:
1. "Review my commit history and write a blog post about how I created these tutorials, emphasizing my use of slash commands to automate."
2. "Reflect that the /tutorial command evolved from manual interactive prompting first."
3. "Emphasize my tutorial style: hands-on, focused, step-by-step."
4. "Add that Japanese translations came first without slash commands, and Claude used 8 subagents in parallel."
5. "Add that Claude wrote the translation slash commands without specific guidelines, and the use of subagents."
6. "Link to the saved commands in docs/assets/commands."
7. "Rewrite with fewer bullet points."
8. "Actually read the slash commands and add details."
9. "Summarize our interaction. Add a P.S. about how this blog was generated."

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 15, 2025.