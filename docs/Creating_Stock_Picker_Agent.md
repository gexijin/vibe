[Home](./)

# Creating a Stock Picker Agent in Claude Code

You want to compare investment opportunities, but researching multiple companies and scoring them takes hours. Think of an agent like hiring a financial analyst who knows exactly how to use your research tools—you give them company names, and they gather reports, score each company across key metrics, and recommend the best investment. This tutorial shows you how to build that analyst.

## Key Concepts

- **Agent** - A specialized AI worker with its own goal, system prompt, and tools that autonomously completes tasks
- **Skill** - A reusable capability (like generating stock reports) that agents can invoke to accomplish their goals
- **System Prompt** - Instructions that define what the agent does, how it scores companies, and what format it returns
- **Separation of Concerns** - Skills gather data; agents use that data to make decisions

## What You'll Need

- Completed [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) or [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- The stock report skill already installed (in `.claude/skills/generating-stock-reports/`)
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

Claude Code starts and displays a welcome message.

## Step 2: Verify the Stock Report Skill Exists

Before building your agent, confirm the skill is available. Type:

```
List all available skills
```

You should see `generating-stock-reports` in the output. This skill researches companies and generates reports covering product news, management updates, financial performance, and analyst insights.

If you don't see it, the skill files should be in `.claude/skills/generating-stock-reports/` (project level) or `~/.claude/skills/generating-stock-reports/` (global level).

## Step 3: Understand Agent vs Skill Architecture

Here's how agents and skills work together:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Skill** | Gathers raw data about one company | "Generate report for Apple: products, financials, management, analysts" |
| **Agent** | Uses skill data to accomplish a goal | "Get reports for Apple and Microsoft, score both, recommend which to invest in" |

**Key difference:**
- **Skill = tool** that does research
- **Agent = decision maker** that uses the tool and applies logic

Your stock-picker agent will:
1. Invoke the stock report skill for each company (2+ times)
2. Score companies across categories (financials, growth, management, sentiment)
3. Compare scores and recommend the best investment

## Step 4: Open the Agents Command

Type this command:

```
/agents
```

You'll see the [Claude Code](https://code.claude.com) agents interface showing:
- List of existing agents (if any)
- Options to **Create**, **Edit**, or **Delete** agents

## Step 5: Create the Stock Picker Agent

Ask Claude to create the agent:

```
Create a new agent called stock-picker
```

Claude will guide you through the setup. When prompted, provide:

**Agent name:**
```
stock-picker
```

**Description** (when Claude should invoke this agent):
```
Compares multiple companies for investment decisions. Use when users want to know which stock is a better investment or need comparative analysis of 2 or more companies.
```

**Skills to enable:**
```
generating-stock-reports
```

This tells the agent it can use your existing stock report skill.

## Step 6: Write the Agent's System Prompt

The system prompt defines the agent's goal and methodology. When Claude asks for the system prompt, provide:

```
You are a stock analysis expert who helps investors compare companies and make informed decisions.

## Your Goal

Compare 2 or more companies and recommend which is the better investment based on systematic scoring.

## Process

1. **Gather Data**: Use the generating-stock-reports skill to get comprehensive reports for each company
2. **Score Each Company**: Evaluate across four categories:
   - Financial Performance (40%): Revenue growth, profitability, margins
   - Growth Potential (30%): Product pipeline, market expansion, innovation
   - Management Quality (20%): Leadership stability, strategic vision, execution
   - Analyst Sentiment (10%): Ratings, price targets, consensus

3. **Present Comparison**: Create a table showing:
   - Company name and ticker
   - Score for each category (0-10 scale)
   - Weighted total score (out of 10)
   - Key strengths and concerns

4. **Make Recommendation**: Identify the highest-scoring company and explain why it's the better investment based on the data

## Scoring Guidelines

- Be objective—base scores on concrete evidence from the reports
- A score of 7-10 is strong, 4-6 is moderate, 0-3 is weak
- Weight financial performance highest (40%) because fundamentals matter most
- If companies are very close (within 0.5 points), note it's a toss-up

## Output Format

Present your analysis as:
1. Brief summary of each company (2-3 sentences)
2. Comparison table with scores
3. Recommendation paragraph with rationale
4. Risk factors to consider

Always ground your recommendation in the data from the skill reports—no speculation.
```

Grant Claude permission to create the agent file.

## Step 7: Review What You Built (Reflection Checkpoint)

Before testing, let's verify the agent configuration. Type:

```
Show me the stock-picker agent file
```

Claude will display the agent file located at `.claude/agents/stock-picker.md`. You'll see:

**YAML frontmatter** at the top:
```yaml
---
name: stock-picker
description: Compares multiple companies for investment decisions...
skills: generating-stock-reports
---
```

**System prompt** below the frontmatter with your scoring methodology.

**Confirm these key elements:**
- Agent has access to the `generating-stock-reports` skill
- System prompt explains the 40/30/20/10 scoring breakdown
- Agent's goal is clear: compare companies and recommend one

If something looks wrong, you can edit the file directly or ask Claude to update it.

## Step 8: Test the Agent

Now test your agent with a real comparison. Type:

```
Use the stock-picker agent to compare AAPL and MSFT for investment
```

Or more naturally:

```
Which is a better investment: Apple or Microsoft?
```

The agent will automatically activate based on your description.

## Step 9: Watch the Agent Work

As the agent runs, you'll see it:
1. **Invoke the skill twice** - First for Apple, then for Microsoft
2. **Gather data** - Each skill invocation searches the web and generates a company report
3. **Score companies** - Applies the 40/30/20/10 weighting across categories
4. **Generate output** - Creates comparison table and recommendation

This may take 2-3 minutes since web research is involved.

## Step 10: Review the Output

The agent returns:

**Company Summaries**: Brief overview of each company's current state

**Comparison Table**:
| Company | Financial (40%) | Growth (30%) | Management (20%) | Sentiment (10%) | **Total** |
|---------|----------------|--------------|------------------|-----------------|-----------|
| Apple | 8.5 | 7.0 | 9.0 | 8.0 | **8.1** |
| Microsoft | 9.0 | 8.5 | 8.5 | 9.0 | **8.8** |

**Recommendation**: "Microsoft is the stronger investment with a score of 8.8 vs 8.1 for Apple. Key advantages: stronger cloud growth trajectory (Azure), higher analyst confidence, and more diversified revenue streams across enterprise and consumer markets..."

**Risk Factors**: Considerations for both companies

Check that scores match evidence from the reports and the recommendation is well-reasoned.

## Next Steps

Now that you have a working stock-picker agent, try these extensions:

- **Compare 3+ stocks**: "Compare AAPL, MSFT, and GOOGL" to see how the agent handles more options
- **Sector analysis**: "Compare AMD vs NVDA in the chip industry" for domain-specific comparisons
- **Adjust scoring weights**: Edit the agent file to change the 40/30/20/10 breakdown (e.g., make growth 40% if you prefer growth stocks)
- **Create other agents**: Build a "code-reviewer" agent, "bug-hunter" agent, or "document-writer" agent for different tasks

## Troubleshooting

- **Agent not activating**: Make sure your request mentions comparing companies or investment decisions. Try: "Use the stock-picker agent to compare..."
- **Skill not found**: Verify `.claude/skills/generating-stock-reports/SKILL.md` exists. Restart Claude Code if you just added it.
- **Incomplete scores**: Ask the agent to "continue" or "explain the scores for each category in more detail"
- **Error creating agent**: Check that the `.claude/agents/` folder exists. Claude Code should create it automatically.

## Workflow Overview

- **Agents automate multi-step workflows** - They orchestrate skills, apply logic, and deliver decisions
- **Skills are reusable tools** - One skill can be used by multiple agents for different goals
- **System prompts define behavior** - Clear instructions and scoring criteria make agents reliable
- **Agents maintain focus** - Each agent has a single, clear purpose (stock picking, code review, etc.)
- **Composition scales** - Build a library of skills and agents that work together

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 14, 2025.
