# Create a Beginner Tutorial

Create a beginner-friendly tutorial for: $ARGUMENTS

It needs to be focused, hands-on, and succinct. Design a minimal set of hands-on activities through a demo project so that users can follow just to get the main idea. It is not a comprehensive tutorial. It is an introduction to a topic for completely new users.

**Keep it short.** Aim for ~250 lines or less. Remove unnecessary explanations.

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

2. **Hook** (3-4 sentences max)
   - One relatable problem scenario
   - One simple analogy
   - Why this matters

3. **Key Concepts** (3-4 terms max)
   - One sentence per concept
   - Bold the term, then explain simply

4. **What You'll Do** - Bullet list of main steps (5-8 items)

5. **What You'll Need** - Prerequisites (3-5 items)

6. **Step-by-Step Instructions**
   - Format: `## Step N: Action Verb + What`
   - Numbered sub-steps (1, 2, 3...)
   - Exact actions: "Click **Button Name**" or "Type `command`"
   - Code blocks for commands
   - **If/Then guidance** for variations
   - Keep explanations minimal - one short sentence when needed

7. **How to Reopen** - Brief instructions to get back to the tool

8. **Troubleshooting** - Only 2-3 most common issues, one-line solutions, help links

9. **The Complete Workflow** - Summary of the cycle (optional)

10. **Next Steps** - What to try next with example prompts

### Writing Rules

**Be concise:**
- Short paragraphs (2-3 sentences max)
- Bullet points over prose
- Remove "Why this matters", "Why this is powerful" etc. - one short sentence only when essential
- No "What You've Learned" sections

**Be explicit for beginners:**
- Describe exactly what to click
- Tell them what they'll see (briefly)
- Never assume prior knowledge

**Be actionable:**
- Every step produces a visible result
- Tell them exactly what to click/type

**Format for scanning:**
- Headers to break up sections
- Code blocks for all commands
- Bold for UI elements: **Button Name**
- Backticks for commands: `command here`

**Add links inline:**
- Link tool names to official sites on first mention
- No separate "Sources" section

**Include timing** only for long waits (5+ minutes)

**Add creation date** at the very end: "Created on [date] with help from Claude Code."

## Output

Save the tutorial in the `doc/` folder with a descriptive filename:
- Pattern: `Install_TOOLNAME_PLATFORM.md` or `TOPIC_Guide.md`
- Examples: `doc/Install_Docker_Mac.md`, `doc/Git_Basics_Guide.md`
