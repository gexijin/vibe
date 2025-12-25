[Home](./)

# Create a Subagent in Claude Code

You want to compare investment opportunities, but researching multiple companies and scoring them takes hours. Think of a subagent like hiring a financial analyst who knows exactly how to use your research tools—you give them company names, and they gather reports, score each company across key metrics, and recommend the best investment. Once you learn to build subagents, you can automate any repetitive multi-step workflow in your work. This tutorial shows you how to build that analyst.

## Key Concepts

- **Subagent** - A specialized AI worker with its own goal, system prompt, and tools that autonomously completes tasks
- **Skill** - A reusable capability (like generating stock reports) that subagents can invoke to accomplish their goals
- **System Prompt** - Instructions that define what the subagent does, how it scores companies, and what format it returns
- **Separation of Concerns** - Skills gather data; subagents use that data to make decisions

## What You'll Need

- Completed [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) or [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- The stock report skill already installed (in `.claude/skills/generate-stock-reports/`)
- VS Code or another text editor
- 20-25 minutes

## Step 1: Create a Project Folder and Start Claude Code

**Windows (WSL):**
- Open **Ubuntu** from the Start menu
- Type these commands:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
  Replace `YOUR_USERNAME` with your Windows username
- Start Claude Code:
  ```
  claude
  ```

**Mac:**
- Open **Terminal** (find it in Applications > Utilities)
- Type these commands:
  ```bash
  cd ~/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
- Start Claude Code:
  ```
  claude
  ```

Log in with your Claude subscription following the installation tutorial ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). After logging in, you'll see a welcome message and the Claude Code prompt.

## Step 2: Verify the Stock Report Skill Exists

Before building your subagent, confirm the skill is available. Type:

```
List all available skills
```

You should see `generate-stock-reports` in the output. This skill researches companies and generates reports covering product news, management updates, financial performance, and analyst insights.

If you don't see it, the skill files should be in `.claude/skills/generate-stock-reports/` (project level).

## Step 3: Understand Subagent vs Skill Architecture

Here's how subagents and skills work together:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Skill** | Gathers raw data about one company | "Generate report for Apple: products, financials, management, analysts" |
| **Subagent** | Uses skill data to accomplish a goal | "Get reports for Apple and Microsoft, score both, recommend which to invest in" |

**Key difference:**
- **Skill = tool** that does research
- **Subagent = decision maker** that uses the tool and applies logic

Your stock-picker subagent will:
1. Invoke the stock report skill for each company (2+ times)
2. Score companies across categories (financials, growth, management, sentiment)
3. Compare scores and recommend the best investment

## Step 4: Create the Stock Picker Subagent

Type this command:

```
/agents
```

You'll see the Claude Code agents interface showing existing subagents (if any) and options to **Create**, **Edit**, or **Delete** subagents.

Now create your subagent:
- Select **Create new subagent**
- Select **Project**
- Select **Generate with Claude (recommended)**
- Paste the following for instructions:
  ```
  Create a markdown file for a new subagent called stock-picker:
  - It takes two or more stocks
  - Uses the generate-stock-reports skill to do research
  - Score cards are created based on the categories of data collected
  - A final recommendation is given.
  ```
- Press **Enter** on **[Continue]** to use **All tools**
- Select **Sonnet** for model
- Press **Enter** to randomly pick a color

## Step 5: Review What You Built (Reflection Checkpoint)

To open the file in VS Code, click **File > Open File...** and navigate to `.claude/agents/stock-picker.md`.

Or you can ask Claude to:
```
Show me the stock-picker subagent file.
```
Claude will display the subagent file located at `.claude/agents/stock-picker.md`. You'll see:

There is a **YAML frontmatter** at the top:
```
---
name: stock-picker
description: Compares multiple companies for investment decisions...
skills: generate-stock-reports
---
```

This frontmatter (the section between `---` markers) tells Claude Code when to activate this subagent and which skills it can use.

There is a **System prompt** below the frontmatter with your scoring methodology.

**Confirm these key elements:**
- Subagent has access to the `generate-stock-reports` skill
- System prompt explains the scoring breakdown
- Subagent's goal is clear: compare companies and recommend one

You can edit the file directly or ask Claude to update it.

## Step 6: Test the Subagent

Now test your subagent with a real comparison. Type:

```
Which is a better investment: Apple or Google?
```

The subagent will automatically activate based on your description.

## Step 7: Watch the Subagent Work

As the subagent runs, you'll see it:
1. **Invoke the skill twice** - Call the generate-stock-reports skill once for Apple, then for Google
2. **Gather data** - Each skill call searches the web and generates a company report
3. **Score companies** - Applies the 40/30/20/10 weighting across categories
4. **Generate output** - Creates comparison table and recommendation

This may take 2-3 minutes since web research is involved.

## Step 8: Review the Output

The subagent returns a detailed analysis including:
- **Individual company reports** - Product updates, financial metrics, management changes, analyst sentiment for each stock
- **Comparison scorecard** - Numerical scores across categories (Financial Health, Growth Potential, Management Quality, Market Sentiment)
- **Final recommendation** - Which stock to invest in and why

The subagent may display this in the terminal or generate a markdown file with the full report. You can edit the subagent file to customize scoring weights or output format.

## Next Steps

Now that you have a working stock-picker subagent, try these extensions:

- **Compare 3+ stocks**: "Compare AAPL, MSFT, and GOOGL" to see how the subagent handles more options
- **Adjust scoring weights**: Edit the subagent file to change the 40/30/20/10 breakdown (e.g., make growth 40% if you prefer growth stocks)
- **Create other subagents**: Build a "code-reviewer" subagent, "bug-hunter" subagent, or "document-writer" subagent for different tasks

## Troubleshooting

- **Subagent not activating**: Make sure your request mentions comparing companies or investment decisions. Try: "Use the stock-picker subagent to compare..."
- **Skill not found**: Verify `.claude/skills/generate-stock-reports/SKILL.md` exists. Restart Claude Code if you just added it.
- **Incomplete scores**: Ask the subagent to "continue" or "explain the scores for each category in more detail"
- **Error creating subagent**: Check that the `.claude/agents/` folder exists. Claude Code should create it automatically.

## Workflow Overview

- **Subagents automate multi-step workflows** - They orchestrate skills, apply logic, and deliver decisions
- **Skills are reusable tools** - One skill can be used by multiple subagents for different goals
- **System prompts define behavior** - Clear instructions and scoring criteria make subagents reliable
- **Subagents maintain focus** - Each subagent has a single, clear purpose (stock picking, code review, etc.)
- **Composition scales** - Build a library of skills and subagents that work together

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 14, 2025.
