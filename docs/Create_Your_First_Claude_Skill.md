[Home](./)

# Create Your First Claude Skill

You've been manually typing `/stock-report AAPL` to generate reports. What if Claude could automatically decide when to create a stock report based on your conversation? That's the power of Skills—like upgrading from manual gear shifting to an automatic transmission that shifts when needed.

## Key Concepts

- **Skill** - A model-invoked capability stored in `.claude/skills/` that Claude automatically activates based on context
- **Model-invoked** - Claude decides when to use the Skill by reading its description, without you typing a command
- **SKILL.md** - The main file containing YAML frontmatter (metadata) and instructions for Claude

## What You'll Need

- Completed [Create Custom Slash Commands](./Reuse_Prompts_via_Slash_Commands.md) tutorial
- The `stock-report` slash command from that tutorial
- VS Code installed
- 10-15 minutes

## Step 1: Navigate to Project Folder

**Windows (WSL):**
- Open **Ubuntu** from the Start menu
- Type:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Replace `YOUR_USERNAME` with your Windows username

  If the folder doesn't exist, create it first:
  ```bash
  mkdir -p /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```

**Mac:**
- Open **Terminal** (Applications > Utilities)
- Type:
  ```bash
  cd ~/Documents/test_claude
  ```

  If the folder doesn't exist, create it first:
  ```bash
  mkdir -p ~/Documents/test_claude
  cd ~/Documents/test_claude
  ```

## Step 2: Start Claude Code

Type:
```
claude
```

Claude Code starts and displays the welcome message.

## Step 3: Enable Auto-Approve for Edits

Press `Ctrl+E` (Windows/Linux) or `Cmd+E` (Mac) to enable auto-approve mode for edits.

This allows Claude to create and modify files without asking permission each time.

## Step 4: Ask Claude to Convert the Slash Command

Type this prompt:
```
Convert my stock-report slash command to a Skill.
The Skill should activate automatically when I ask about companies or stocks.
```

Claude analyzes your existing slash command and converts it to a Skill in `.claude/skills/stock-report/`.

**What happens:** Claude creates a new folder structure with `SKILL.md` containing YAML frontmatter that tells Claude when to automatically use this Skill.

## Step 5: Review the Skill Structure

Open VS Code and view the project:
- Click **File > Open Folder**
- Select `Documents/test_claude`
- In the file explorer, navigate to `.claude/skills/stock-report/`
- Click `SKILL.md` to open it

Notice the structure:
```yaml
---
name: stock-report
description: Generates reports on companies... Use when users ask about stocks, companies, or ticker symbols.
---

[Rest of the instructions]
```

The `description` field is the key—it tells Claude exactly when to activate this Skill automatically.

## Step 6: Test the Skill (Without Typing a Command)

Instead of typing `/stock-report AAPL`, just ask a natural question:
```
What's happening with Apple lately?
```

**The key difference:** You didn't type a command. Claude reads your question, recognizes you're asking about a company, checks the Skill descriptions, and automatically decides to use the stock-report Skill.

Watch Claude work—it should generate the same comprehensive report you saw before.

## Step 7: Compare the Two Approaches

**Slash Command (Manual):**
```
/stock-report AAPL
```
- You explicitly tell Claude what to do
- Same every time
- Good for repeated, predictable tasks

**Skill (Automatic):**
```
Tell me about Tesla's recent developments
```
or
```
I'm thinking about investing in Microsoft
```
or
```
What's NVIDIA up to?
```
- Claude decides whether to use the Skill
- More natural conversation
- Good for complex workflows Claude manages for you

## Step 8: Test Edge Cases

Try questions that should NOT trigger the stock report Skill:
```
How do I install Python?
```

Claude answers normally without invoking the Skill.

Now try a question that SHOULD trigger it:
```
Compare Google and Meta
```

Claude should use the Skill twice—once for Google, once for Meta.

## Step 9: Modify the Skill Description (Optional)

Let's make the Skill more selective. Ask Claude:
```
Update the stock-report Skill to only activate when I explicitly mention
"analyze" or "report" along with a company name.
```

Claude updates the `description` field in `SKILL.md`. Test the difference:
```
What's Apple doing?
```
(Might not trigger the Skill now)

```
Analyze Apple
```
(Should trigger the Skill)

## Next Steps

Now that you understand Skills, create more for your workflows:

- **Research Skill** - Automatically activates when you ask questions requiring web research
- **Code Review Skill** - Activates when you mention bugs, issues, or code problems
- **Meeting Notes Skill** - Activates when you paste meeting transcripts or mention summaries

The pattern: Define when Claude should automatically help, not just shortcuts you manually trigger.

## Troubleshooting

- **Skill doesn't activate:** Check the `description` field in `SKILL.md`—it must include trigger words related to your question
- **Skill activates too often:** Make the description more specific about when to use it
- **Can't find the Skill folder:** Skills are in `.claude/skills/` (hidden folder—enable "Show hidden files" in your file explorer)
- **Changes to SKILL.md not working:** Skills load automatically when modified—no restart needed. If still not working, check YAML formatting

## Workflow Overview

- **Slash commands** are shortcuts you type manually (like bookmarks)
- **Skills** are capabilities Claude discovers and uses automatically (like an assistant who knows your preferences)
- **Skill descriptions** act as instructions telling Claude: "Use me when the user says X"
- **Both can coexist** - Use slash commands for quick, repetitive tasks; use Skills for complex workflows
- **Skills scale better** - You don't need to remember command names; Claude decides based on context

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 13, 2025.
