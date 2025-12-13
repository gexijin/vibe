[Home](./)

# Create Custom Slash Commands in Claude Code

Tired of typing the same detailed prompts over and over? Custom slash commands let you save complex instructions as reusable shortcuts. Like creating keyboard shortcuts for your most frequent tasks, slash commands turn lengthy prompts into simple commands like `/stock-report AAPL` that generate comprehensive reports instantly.

## Key Concepts

- **Slash command** - A reusable prompt stored as a Markdown file that Claude Code executes when you type `/command-name`
- **Arguments** - Variables you pass to commands (like stock tickers) using the special `$ARGUMENTS` keyword
- **`.claude/commands/` folder** - Where Claude Code automatically discovers and loads your custom commands

## What You'll Need

- Completed [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) or [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- A topic to research (we'll use stock reports as an example)
- 15-20 minutes

## Step 1: Create a Project Folder

**Windows (WSL):**
- Open **Ubuntu** from the Start menu
- Type these commands:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir stock_research
  cd stock_research
  ```
  Replace `YOUR_USERNAME` with your Windows username

**Mac:**
- Open **Terminal** (find it in Applications > Utilities)
- Type these commands:
  ```bash
  cd ~/Documents
  mkdir stock_research
  cd stock_research
  ```

## Step 2: Start Claude Code

**Windows (WSL):**
- Still in the Ubuntu terminal, type:
  ```b
  claude
  ```

**Mac:**
- Still in Terminal, type:
  ```
  claude
  ```

Claude Code starts and displays a welcome message.

## Step 3: Ask Claude to Create a Slash Command

Instead of manually creating files, let Claude do the work. Type this prompt:

```
Create a slash command called /stock-report that generates 
stock research reports on recent developments. The command should accept a stock ticker symbol as an argument.
The report should include these sections:
- Product or service news 
- Management team news 
- Recent financial reports 
- Analyst reports 

```

Claude will create the `.claude/commands/` folder structure and start building your command.

## Step 4: Test the Command

First quick the current Claude Code session by clicking Ctrl + C + C. And restart Claude, so that the new slash command is loaded:
  ```
  claude
  ```
Now test your new command with a real stock ticker:

```
/stock-report AAPL
```

Claude searches the web and generates a comprehensive report about Apple Inc. This may take 1-2 minutes.

## Step 5: Review the Generated Report

Claude creates a report with all four sections. Review the output:

- Check that each section has relevant, current information
- Verify the sources are credible and recent
- Notice how Claude organized the information


## Step 7: Understand How Arguments Work

The `$ARGUMENTS` keyword in your slash command acts as a placeholder. When you type `/stock-report AAPL`, Claude replaces `$ARGUMENTS` with `AAPL` before executing the prompt.

Try another ticker:

```
/stock-report TSLA
```

The same command structure now researches Tesla instead.

## Step 8: Modify the Command

Let's add a new section to assess competitive positioning. Ask Claude:

```
Open the stock-report.md slash command file and add a new section that assesses
the company's competitive edge. This section should analyze:
- Market position and competitive advantages
- Key competitors and market share
- Unique strengths or moats
```

Claude opens the command file and adds the competitive edge analysis section.

## Step 9: Test the Updated Command

Test the enhanced command:

```
/stock-report MSFT
```

The report now includes the competitive edge analysis section, giving you deeper insight into Microsoft's market position.

## Step 10: Try Another Slash Command (Optional)

If you completed the [Writing Research Paper](./Writing_Research_Paper_Claude_Code.md) tutorial, you should have a `/research-paper` command. Test it on a fresh topic.

First, clear Claude's memory to start fresh:

```
/clear
```

Then run the research paper command:

```
/research-paper AI in schools
```

Claude guides you through the entire research paper workflow automatically, from initial research to final draft.

## Next Steps

Now that you understand slash commands, create more custom commands for your workflows:

- **Code review:** `/review-code` - Analyze code for bugs and improvements
- **Meeting notes:** `/meeting-summary` - Generate structured meeting summaries
- **Email drafts:** `/email-reply` - Create professional email responses

## Troubleshooting

- **Command not found:** Restart Claude Code to reload commands from `.claude/commands/`
- **Arguments not working:** Check that `$ARGUMENTS` is spelled correctly in the command file (case-sensitive)
- **Report incomplete:** Ask Claude to "continue" or "add more detail to the [section name] section"

## Workflow Overview

- **Custom slash commands** save time by turning complex prompts into simple shortcuts
- **Arguments** make commands flexible for different inputs (stock tickers, topics, files)
- **Claude builds commands** - You don't need to manually write Markdown files; just describe what you want
- **Commands are reusable** - Once created, use them across projects and sessions
- **Combine commands** - Build a library of specialized commands for different tasks

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 13, 2025.
