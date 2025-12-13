[Home](./)

# Create Custom Slash Commands 

Tired of typing the same detailed prompts over and over? Custom slash commands let you save complex instructions as reusable shortcuts. Like creating keyboard shortcuts for your most frequent tasks, slash commands turn lengthy prompts into simple commands like `/stock-report AAPL` that generate comprehensive reports instantly.

## Key Concepts

- **Slash command** - A reusable prompt stored as a Markdown file that Claude Code executes when you type `/command-name`
- **Arguments** - Variables you pass to commands (like stock tickers) using the special `$ARGUMENTS` keyword
- **`.claude/commands/` folder** - Where Claude Code automatically discovers and loads your custom commands

## What You'll Need

- Completed [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) or [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- A topic to research (we'll use stock reports as an example)
- A text editor such as VS Code installed
- 15-20 minutes

## Step 1: Create a Project Folder

**Windows (WSL):**
- Open **Ubuntu** from the Start menu
- Type these commands:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir test_claude
  cd test_claude
   ```
  Replace `YOUR_USERNAME` with your Windows username

**Mac:**
- Open **Terminal** (find it in Applications > Utilities)
- Type these commands:
  ```bash
  cd ~/Documents
  mkdir test_claude
  cd test_claude
  ```

## Step 2: Start Claude Code

**Windows (WSL):**
- Still in the Ubuntu terminal, type:
  ```
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
Create a slash command called stock-report that generates 
reports on recent developments of a company identified by name or ticker symbol.
Include:
- Product or service news 
- Management team news 
- Recent financial reports 
- Analyst reports 

```
When asked, grant Claude permission to create the file.
Claude will create a detailed prompt and save it as `stock-report.md` to the `.claude/commands/` folder.

**Note:** We use Markdown format a lot: in the prompt above, reports, and the slash command. It is friendly to AI. 

## Step 4: Review the Command 

Use any text editor to open the `stock-report.md` file from the `.claude/commands/` folder. That's the prompt for the slash command. 

If you have VS Code installed (recommended):
- Start VS Code 
- From **File**, choose **Open folder**, and select the project folder `Documents/test_claude`
- From the file explorer, navigate to `.claude/commands` and click the file `stock-report.md` to open it

Review the prompt and make changes to the instructions if you want.

**Note:** Claude is incredibly good at writing prompts. You can see that its prompts is structured well using markdown format. Clearly written. Learn to write prompts like this. When I run this, it even has instructions to ask for clarification if the identifier is ambiguous.

## Step 5: Test the Command

First **quit** the current Claude Code session by pressing **Ctrl+C** twice. Then restart Claude so the new slash command is loaded:
  ```
  claude
  ```
Now test your new command with a real stock ticker:

```
/stock-report Apple
```

Claude searches the web and generates a comprehensive report about Apple Inc. This may take 1-2 minutes.

## Step 6: Review the Generated Report

Claude creates a report in the command line. Review the output:

- Check that each section has relevant, current information
- Verify the sources are credible and recent
- Notice how Claude organized the information

## Step 7: Save report to file

Let's modify the slash command to automatically save reports as HTML files. Append this to the slash command markdown file manually.

- Open the `stock-report.md` file from the `.claude/commands/` folder
- Append this to the end.
```
Save the report as a markdown file. File name has company name and date.
```
- Save the file. 

## Step 8: Rerun Command

- First **quit** the current Claude Code session by pressing **Ctrl+C** twice. Then restart Claude so the new slash command is loaded:
  ```
  claude
  ```
- Now test your new command with a real stock ticker:

```
/stock-report AAPL
```
- Open the report

Claude generates the report and saves it as an markdown file named something like `Apple_2025-12-13.md`. Click the file in VS Code to view it.

## Step 9: Modify the Command through Claude

You can ask Claude to edit the slash commands:

```
Revise the stock-report slash command to save the report as a html file.
```

Claude opens the command file and adds the competitive edge analysis section.

## Step 10: Test the Updated Command

- First **quit** the current Claude Code session by pressing **Ctrl+C** twice. Then restart Claude so the new slash command is loaded:
  ```
  claude
  ```

Test the enhanced command:

```
/stock-report AAPL
```

Claude creates a html file named something like `Apple_2025-12-13.md`. Click on this file from File Explorer on Windows or Mac to open it in your default browser.

## Step 9: Understand How Arguments Work (Optional)

The `$ARGUMENTS` keyword in your slash command acts as a placeholder. When you type `/stock-report AAPL`, Claude replaces `$ARGUMENTS` with `AAPL` before executing the prompt.

Try another ticker:

```
/stock-report TSLA
```

The same command structure now researches Tesla instead.

## Step 12: Try Another Slash Command (Optional)

If you completed the [Writing Research Paper](./Writing_Research_Paper_Claude_Code.md) tutorial, you should have a `/research-paper` command. Test it on a fresh topic.

First, clear Claude's memory to start fresh:

```
/clear
```

Then run the research paper command:

```
/research-paper AI in schools
```

Claude guides you through the entire research paper workflow. There are two key differences:
- This slash command was created at the end of an interactive session, essentially capturing what we want through an example.
- This slash command is interactive. It ask for input during the process before drafting a paper.


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
