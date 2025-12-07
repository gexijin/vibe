# Create a Beginner Tutorial

Create a beginner-friendly tutorial for: $ARGUMENTS

It needs to be focused, hands-on, and succinct. Design a minimal set of hands-on activities through a demo project so that users can follow just to get the main idea. It is not a comprehensive tutorial. It is an introduction to a topic for completely new users.

**Keep it short.** Aim for ~400 lines or less. Remove unnecessary explanations.

## Phase 1: Research

**Search the web first** to get the most current information:
- Latest version numbers and download links
- Current best practices and recommended approaches
- Up-to-date installation methods

## Phase 2: Get User Input

**Before writing the tutorial, present a brief plan to the user:**

1. Summarize what you learned from research (2-3 bullet points)
2. If multiple approaches exist, recommend ONE simplest option for beginners
3. List the major steps you plan to include (5-10 items)
4. Ask: "Does this approach work for you, or would you prefer a different option?"

**Wait for user approval before proceeding to Phase 3.**

**Iterate with user** - they may request changes to the plan. Update accordingly.

## Phase 3: Write the Tutorial

### Structure

1. **Title** - Clear, descriptive (e.g., "Installing Claude Code on Windows Using WSL")

2. **Hook** (one paragraph, 2-3 sentences)
   - Combine: problem scenario + simple analogy + why this matters
   - Keep it compact, not multiple paragraphs

3. **Key Concepts** (3-4 terms max)
   - Use bullet list format for compact spacing: `- **Term** - explanation`
   - One sentence per concept

4. **What You'll Do** - Bullet list of main steps (5-10 items)

5. **What You'll Need** - Prerequisites (3-5 items)

6. **Step-by-Step Instructions**
   - Format: `## Step N: Action Verb + What`
   - Use **bullet points** for sub-steps (not numbered lists) to avoid confusion with step numbers
   - Exact actions: "Click **Button Name**" or "Type `command`"
   - Code blocks for commands
   - Keep explanations minimal - one short sentence when needed

7. **Next Steps** - What to try next using this setup to learn on your own(2-3 examples)

8. **Troubleshooting** - Use bullet list format, 2-3 most common issues with one-line solutions

9. **Workflow overview** - Summary of the workflow / tech stack (optional). 3-5 bullet points. 



### Formatting Rules

**Use bullet lists for compact spacing:**
- Key Concepts, Troubleshooting, and similar sections should use bullet lists
- This keeps related items visually grouped without excessive blank lines

**Avoid numbered list confusion:**
- Steps use numbers in headings: Step 1, Step 2, Step 3...
- Sub-steps within each step use bullets (-) not numbers
- This creates clear visual hierarchy

**Be concise:**
- Short paragraphs (2-3 sentences max)
- Bullet points over prose
- One short sentence only when essential to talk about why each step is important
- No "What You've Learned" sections

**Be explicit for beginners:**
- Describe exactly what to click
- Tell them what they'll see (briefly)
- Never assume prior knowledge
- Avoid jargons

**Format for scanning:**
- Headers to break up sections
- Code blocks for all commands
- Bold for UI elements: **Button Name**
- Backticks for commands: `command here`

**Add links inline:**
- Link tool names to official sites on first mention
- No separate "Sources" section

**Add estimated time to completion and creation date** at the very end: "Estimated complation time: 20 minutes. Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on [date]."

**Add link to GitHub repo** at the very end like this '[Other tutorials](https://gexijin.github.io/vibe)'
## Output

Save the tutorial in the `docs/` folder with a descriptive filename:
- Pattern: `Install_TOOLNAME_PLATFORM.md` or `TOPIC_Guide.md`
- Examples: `docs/Install_Docker_Mac.md`, `docs/Git_Basics_Guide.md`
