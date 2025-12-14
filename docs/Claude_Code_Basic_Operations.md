[Home](./)

# Claude Code: Basic Operations

Learning to code with AI assistance can feel overwhelming at first. Think of Claude Code as a knowledgeable colleague sitting next to you—you describe what you want in plain English, and it helps you get there. This tutorial teaches you the essential operations you'll use daily, from starting conversations to managing your workspace.

## Key Concepts

- **Workspace** - If you start Claude Code from a folder, that's the sessions workspace. 
- **REPL (Read-Eval-Print Loop)** - An interactive session where you type commands, Claude responds, and the conversation continues until you exit
- **Context** - The amount of code and conversation history Claude remembers; like working memory that fills up over time
- **Slash Commands** - Built-in shortcuts starting with `/` that perform specific actions like clearing history or showing help

## What You'll Need

- [Claude Code installed](https://code.claude.com/docs/en/quickstart) with an active Claude Pro/Max subscription or API key
- Basic familiarity with using a terminal or command prompt
- Internet connection
- 15-20 minutes

## Step 1: Open Your Terminal

- **Windows**: Press the Windows key, type `Terminal` or `PowerShell`, and press Enter
- **Mac**: Press `Cmd+Space`, type `Terminal`, and press Enter
- **Linux**: Press `Ctrl+Alt+T` or find Terminal in your applications menu

A text window will open where you can type commands.

## Step 2: Get the Demo Project

We'll use a real data science project to explore Claude Code's features. You can either clone it with Git or download it directly.

**Option A: Clone with Git (if you have Git installed):**

```
git clone https://github.com/gexijin/data_projects
cd data_projects
```

**Option B: Download without Git:**

- Visit [https://github.com/gexijin/data_projects](https://github.com/gexijin/data_projects) in your web browser
- Click the green **Code** button near the top right
- Click **Download ZIP**
- Extract the ZIP file to a location you'll remember (like your Desktop or Documents folder)
- In your terminal, navigate to the extracted folder:
  - **Windows**: `cd C:\Users\YourName\Downloads\data_projects-main`
  - **Mac/Linux**: `cd ~/Downloads/data_projects-main`

Replace `YourName` with your actual username and adjust the path if you extracted it elsewhere.

## Step 3: Start Claude Code from the folder

In your terminal (make sure you're inside the data_projects folder), type:

```bash
claude
```

You'll see a welcome message and the Claude Code prompt.

## Step 4: Ask Questions About Your Project

Claude Code automatically reads your files when needed. Try these questions to understand your project:

**Ask about the folder structure:**

```
What is the folder structure of this project?
```

**Ask about technologies:**

```
What technologies and libraries does this project use?
```

**Ask about recent changes:**

```
What was the last change made to this project?
```

Claude will check the Git history (if available) and tell you about recent commits.

You can ask Claude anything about your code in natural language. It reads files as needed to answer your questions.

## Step 5: Essential Slash Commands

Type `/` and press Enter to see all available commands. Here are the most important ones:

**View all commands:**

```
/
```

This displays a menu of all slash commands. Use arrow keys to browse, press Enter to select, or press Esc to cancel.

**Get help:**

```
/help
```
Shows documentation about using Claude Code.



**Check context usage:**
It is important to manage the context, Claude's "working memory". 

```
/context
```

**Clear conversation history:**

When context fills up, start a new conversation with `/clear`.
```
/clear
```
Wipes the current conversation and starts fresh. Use this when you want to change topics or when your conversation gets too long. It is essential to manage context.


**Exit Claude Code:**

```
/exit
```

Ends your session and returns to your normal terminal prompt. You can also hit **Ctrl + C** twice.

## Step 6: Keyboard Shortcuts

These shortcuts make working with Claude Code faster:

- **Shift+Tab** - Switch between, plan, edit, or normal mode - Plan first for complex tasks
- **Alt+Enter** (Windows/Linux) or **Option+Return** (Mac) - Add a new line in your message without sending it
- **Ctrl+C** - Cancel the current operation or Claude's response
- **Ctrl+D** - Approve file changes when Claude asks for permission
- **Esc** - Close menus or cancel the current input

## Step 7: Always Create a CLAUDE.md File

The CLAUDE.md file is your project's instruction manual for Claude. It persists across sessions, so Claude remembers important context about your project.

**Create the file:**

```
/init
```

Claude will create the file with a summary of your project. This file stays in your project root and Claude reads it automatically every time you start a new session.

You can edit CLAUDE.md in the project folder anytime to add project-specific instructions, coding conventions, or important context such as purpose of files, etc.

## Step 8: Referring to files or lines of code

You can use `@` to refer to a specific file:

```
Explain the code in @Visualization/Matplotlib/Nested_Pie_Chart.ipynb
```

Claude will read the notebook and explain what it does, how it works, and what the code accomplishes. This effectively brings the file to the context. 

If you working with Claude Code from VS Code and has the Claude Code extension installed, you can add the file to context simply by opening it. You will see in the lower right of the command windows that reads `In Nested_Pie_Chart.ipynb`. Then Claude knows you are talking about this file.

Furthermore, you can select a few lines of code and Claude will show **3 lines selected**. You can ask Claude to make quick changes to these lines or ask questions. Therefore, I highly recommend using Claude Code from VS Code. 


## Step 9: Take Actions with Linux Commands

Claude can take actions by running Linux commands in many forms. 

- Install software
  ```
  Install the pandas library
  ```

- Start version control
  ```
  Start tracking changes using Git. My name is James Bond and my email is bond@earth.com
  ```
- Commit changes
  ```
  Commit these changes.
  ```
- Find and download data
  ```
  Download the wine quality dataset from UCI. Put it in a new folder called wine.
  ```

- Execute code
  ```
  Rewrite the nested pie chart code as a regular Python script.
  Run it and save the new code and plots in the same folder.
  ```

We can ask this vague question because we just asked it to explain the code. Lots of things happen after this. Claude installs software, troubleshoots errors, solves environments - all on its own.



You essentially have an expert in Linux bash commands at your disposal. As long as you manage permissions and approve actions, you can be very productive. 

## Next Steps

Now that you know the basics, try these on your own:

- Ask Claude to explain a machine learning algorithm in one of the project folders
- Request modifications to an existing notebook (like changing chart colors or adding new features)
- Create a new Python script that uses data from the project
- Ask Claude to compare two different approaches in the codebase

## Troubleshooting

- **"Command not found" error** - Claude Code isn't installed or not in your PATH. Run `npm install -g @anthropic-ai/claude-code` to install it.
- **Claude gives outdated information** - Clear the context with `/clear` and ask again. Long conversations can fill up Claude's memory.
- **File changes not working** - Make sure you have write permissions in your project folder. Claude will ask for approval before modifying files—press Ctrl+D to approve.
- **Context filling up quickly** - Use `/context` to check usage. When it's nearly full, use `/clear` to start a fresh conversation with a clean slate.

## Workflow Overview

Working with Claude Code follows this pattern:

- Start Claude in your project folder with `claude`
- Ask questions in natural language
- Claude reads files as needed and responds
- Request code changes—Claude asks permission before modifying files
- Use `/clear` when changing topics or context gets full
- Use `/exit` when you're done

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 14, 2025.
