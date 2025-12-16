# Building a Tutorial Library at Scale: How I Automated Documentation with Claude Code Slash Commands

In December 2025, I set out to create a comprehensive tutorial library for Claude Code. My goal: hands-on, focused tutorials that walk complete beginners through real tasks step by step. No theory dumps. No comprehensive reference manuals. Just "do this, then this, then this" until you've accomplished something concrete.

What started as a few documentation files quickly evolved into a multi-language learning platform with over 100 tutorial documents. The secret? I didn't write them all manually. Instead, I built a set of custom slash commands that transformed Claude Code into an automated documentation factory—one that consistently produces tutorials in my hands-on, step-by-step style.

Here's how I turned repetitive tutorial work into a scalable, automated workflow.

## The Challenge: Creating Consistent, High-Quality Tutorials at Scale

Creating tutorials is time-consuming. Each one requires:
- Research for current best practices and version numbers
- Structured, beginner-friendly writing
- Consistent formatting and style
- Technical accuracy validation
- Translation into multiple languages
- Ongoing maintenance as tools evolve

Doing this manually for 20+ tutorials in 3+ languages would take weeks. I needed a better approach.

## The Solution: From Manual Process to Automated Slash Commands

The key insight: **automate proven workflows, not theoretical ones**.

I didn't sit down and design slash commands from scratch. Instead, I:
1. Created the first few tutorials manually through interactive prompting with Claude
2. Refined the process through iteration—what worked, what didn't
3. Asked Claude to codify the working process into a slash command

This is exactly the pattern described in my [research paper tutorial](./Writing_Research_Paper_Claude_Code.md): go through the workflow manually, then in the final step, ask Claude to save it as a reusable command.

The result was five specialized slash commands that handled the entire tutorial lifecycle:

### 1. [`/tutorial`](./assets/commands/tutorial.md) - The Tutorial Generator

Born from creating several tutorials interactively, this command captures the proven workflow. It follows a rigorous three-phase approach:

**Phase 1: Research First**
The command forces Claude to search the web for current information before writing anything. No more outdated version numbers or deprecated installation methods.

**Phase 2: Get User Approval**
Before writing a single word, Claude presents a plan with:
- What it learned from research
- Recommended approach for beginners
- Outline of major steps
- Request for user approval

This collaborative planning step was crucial. It prevented wasted effort on tutorials that didn't match my vision.

**Phase 3: Write According to Template**
Only after approval does Claude write the tutorial following strict formatting rules:
- `[Home](./)` link at the top
- Engaging hook (2-4 sentences)
- Key concepts (3-4 terms max)
- Step-by-step instructions with action verbs
- Troubleshooting section
- Creation date with author credit

The command enforces consistent structure across all tutorials. Every tutorial feels like it came from the same author—because they followed the same systematic process.

**Result**: I generated 20+ tutorials covering topics from basic Git operations to advanced Docker workflows, all with consistent quality and structure.

### 2. [`/review-tutorial`](./assets/commands/review-tutorial.md) - The Quality Control Bot

After generating tutorials, quality matters. This slash command performs comprehensive review against 40+ quality criteria:

- Content quality (hook, concepts, logical flow)
- Formatting standards (headers, code blocks, bullets)
- Beginner-friendliness (no jargon, explicit instructions)
- Technical accuracy (correct commands, realistic time estimates)
- Writing quality (grammar, consistency, conciseness)

The command presents findings in a structured report, then applies fixes after approval. I used this to batch-polish multiple tutorials at once (see commit `056c3b5: Mass polishing using slash command`), applying consistent improvements across the entire library.

**Result**: Uniform quality across all tutorials without manually reviewing each one multiple times.

### 3. [`/translate-chinese`](./assets/commands/translate-chinese.md) & [`/translate-spanish`](./assets/commands/translate-spanish.md) - The Localization Engine

Interestingly, the Japanese translations came first—and without a slash command. I simply asked Claude Code to translate all the tutorials to Japanese in one prompt. Claude automatically spawned 8 subagents running in parallel, each handling different tutorials simultaneously. The results were excellent, which gave me confidence to formalize the process into slash commands for Chinese and Spanish.

For Chinese and Spanish, I discovered Claude's remarkable ability to write prompts. I simply asked Claude to create a slash command for translating tutorials—without giving any specific guidelines. Claude generated comprehensive commands on its own, adding detailed rules for what to translate, what to keep in English, language-specific formatting, and quality checklists. The AI wrote better prompts than I would have.

With the slash commands ready, I asked Claude Code to translate all 25 tutorials using subagents. The entire translation—50 new files across two languages—took only 15 minutes.

These translation commands handle the complexity of technical translation:

**What Gets Translated:**
- Instructional text
- Section headings
- Explanations and descriptions

**What Stays in English:**
- Code blocks and commands
- Technical terms (Git, Docker, Claude Code)
- File paths and URLs
- Brand names

The commands include language-specific rules:
- Chinese: Use Simplified characters, proper punctuation (。，！？)
- Spanish: Formal "usted" form, proper accent marks (á, é, í)

Each translation command also performs a quality review checklist before saving, ensuring natural phrasing rather than word-for-word translation.

**Result**: 81 translated tutorial files across Chinese (zh), Spanish (es), and Japanese (ja) directories—all maintaining consistent quality and structure.

### 4. [`/review-translation`](./assets/commands/review-translation.md) - The Translation Maintenance Tool

Tutorials evolve. Commands change. New sections get added. This command keeps translations in sync:

**Phase 1: Read Both Versions**
Reads the English original and target language translation side-by-side.

**Phase 2: Compare and Update**
Identifies:
- Missing sections
- Outdated content
- Structural differences
- Changed commands or URLs

**Phase 3: Quality Review**
Even if translations are up-to-date, it checks:
- Translation accuracy (technical terms, UI elements)
- Language quality (natural flow, consistent terminology)
- Formatting consistency (same structure as English)

**Phase 4: Apply Fixes**
Presents findings, gets approval, applies updates.

**Result**: Maintaining multi-language documentation became manageable. When I updated English tutorials, I could quickly propagate changes to all translations.

## The Power of Systematic Automation

What made this approach so effective wasn't just having slash commands—it was the systematic, multi-phase structure within each command:

1. **Research/Read Phase**: Gather context before acting
2. **Analysis Phase**: Evaluate against clear criteria
3. **Report Phase**: Present findings to user
4. **Approval Phase**: Wait for user confirmation
5. **Execution Phase**: Apply changes systematically

This structure prevented errors and wasted effort. Claude never wrote tutorials based on outdated information. It never applied changes without my review. Each step built on validated information from the previous step.

## Scaling with Subagents

For truly parallel work, I used Claude's subagent feature. When polishing Japanese translations, I launched multiple review agents simultaneously (see commit `eea7fb5: Polish Japanese via subagents`), processing 19 files with coordinated improvements.

The combination of slash commands for structured workflows and subagents for parallelization created a documentation pipeline that scaled far beyond what manual effort could achieve.

## The Results: A Multi-Language Tutorial Library in Days

In less than two weeks, I created:
- **20+ English tutorials** covering beginner to intermediate topics
- **81 translated tutorials** across 3 languages (Chinese, Spanish, Japanese)
- **Consistent quality** through automated review processes
- **Maintainable documentation** with sync tools for translations

All tutorials follow the same structure, writing style, and formatting conventions—because they were generated by the same systematic process.

## Key Lessons for Automating Documentation

### 1. Start Manual, Then Automate

Don't write slash commands from scratch. Do the task manually first, refine the process, then ask Claude to save it as a command. The `/tutorial` command works because it codifies a workflow I'd already validated through creating real tutorials. Each command went through iterations (visible in commits like `3b28870: Update slash command`), but they were improvements to proven processes, not theoretical designs.

### 2. Structure Commands as Multi-Phase Workflows

Don't just tell Claude what to do—tell it **how to think through the problem**. The research → plan → approve → execute structure prevented countless issues.

### 3. Build Quality Control Into the Process

The `/review-tutorial` and `/review-translation` commands weren't afterthoughts—they were core parts of the workflow. Automated generation without automated quality control leads to inconsistent output.

### 4. Make Commands Collaborative, Not Autonomous

Every slash command includes approval steps. This kept me in control while eliminating repetitive work. Claude handled the tedious parts; I made the strategic decisions.

### 5. Templates Create Consistency at Scale

By encoding formatting rules, style guidelines, and quality criteria into the slash commands, I ensured every tutorial met the same standards—even when generated weeks apart.

## Try This Yourself

The beauty of slash commands is that they're just markdown files. You can adapt this approach to any repetitive documentation task:

- API documentation for multiple endpoints
- Setup guides for different platforms
- Changelog entries with consistent formatting
- Code review checklists
- Pull request templates with context-specific checks

The pattern is always the same:
1. Do the task manually with Claude first (like writing one API doc)
2. Refine the process through a few iterations
3. Ask Claude: "Create a slash command that captures this workflow"
4. Use the command to handle the next 10, 20, or 100 instances

## Conclusion

Building this tutorial library taught me that automation isn't about removing humans from the process—it's about amplifying human judgment. I didn't write 100+ tutorials manually, but every single one reflects my standards, my structure, and my approval.

Slash commands transformed Claude Code from a helpful assistant into a documentation factory that works at my direction, maintains my standards, and scales to whatever size project I need.

If you have repetitive documentation tasks, don't keep doing them manually. Build the slash command once, then deploy it dozens or hundreds of times.

That's the power of systematic automation.

---

*Want to see the slash commands I built? Check out the [commands folder](./assets/commands/). The full tutorial library is available at the [project documentation site](https://github.com/gexijin/vibe/tree/main/docs).*

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 15, 2025.

---

**P.S.** This blog post was itself drafted by Claude Code. My prompt:

> Review my commit history to understand how these tutorials were created. Write a blog post about the process, emphasizing how I used slash commands to automate the workflow.
