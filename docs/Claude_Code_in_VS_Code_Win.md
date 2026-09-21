---
title: "Set Up VS Code for Claude Code on Windows"
---
[Home](./)

# Set Up VS Code for Claude Code on Windows

You've installed Claude Code on your Windows machine - now you want a visual editor to work with your code. VS Code lets you edit files visually while running Claude Code in the integrated terminal, right next to each other in the same window.

## Key Concepts

- **VS Code** - A free code editor from Microsoft with a built-in terminal
- **Integrated Terminal** - A PowerShell terminal panel inside VS Code, so you don't need to switch windows to run Claude Code
- **Workspace folder** - The folder you open in VS Code; Claude Code reads and edits files within it

## What You'll Need

- Finished [Installing Claude Code on Windows](./Install_CLAUDE_Code_Win)
- Finished [VS Code Basics](./VS_Code_Getting_Started)
- 10-15 minutes

## Step 1: Create a Project Folder

- Open **File Explorer** (click the folder icon in your taskbar)
- Navigate to **Documents**
- Right-click in the empty space, select **New > Folder**
- Name the folder `test_claude`

## Step 2: Start VS Code

- Click the **Windows Start button** (bottom-left corner of your screen)
- Type `Visual Studio Code` or `VS Code` in the search box
- Click on **Visual Studio Code** when it appears in the search results
- VS Code opens with a Welcome tab - you can close this tab


## Step 3: Open the Folder in VS Code

- In VS Code, click **File** in the menu bar, then **Open Folder**
- Navigate to **Documents**, select the `test_claude` folder
- Click **Select Folder**. VS Code reloads with your `test_claude` folder
- If prompted "Do you trust the authors?", click **Yes, I trust the authors**


## Step 4: Start Claude Code

- After VS Code reloads, open a new terminal: click **Terminal** in the menu bar, then **New Terminal**
- In the terminal panel, type:
  ```
  claude
  ```

Log in with your Claude subscription following the [installation tutorial](Install_CLAUDE_Code_Win.md). After logging in, you'll see a welcome message and the Claude Code prompt.

## Step 5: Test the Workflow

- In Claude Code, type: 
```
Write a short article explaining why LLMs like to use Markdown format. Save it as article.md
```
- Claude Code creates the file - you'll see `article.md` appear in the Explorer panel on the left
- Click on `article.md` in the Explorer to view it in the editor
- To preview the formatted article: right-click on the `article.md` tab and select **Open Preview**
- You'll see the Markdown rendered with proper headings, bullet points, and formatting

## Reopening Claude in VS Code Later

After closing VS Code, here's how to get back to your project:

- **Option A:** Open VS Code, click **File > Open Recent**, and select `test_claude`
- **Option B:** Open **File Explorer**, right-click the `test_claude` folder, and select **Open with Code**

## Next Steps

- Ask Claude Code to explain an existing codebase: "Explain what this project does"
- Have Claude Code help you write new features: "Add a function that calculates the average of a list"
- Use Claude Code to fix bugs: "This code gives an error, can you fix it?"
- Try the Claude Code VS Code extension for a visual interface with inline diffs (search "Claude Code" in Extensions)

## Troubleshooting

- **`claude` command not found** - Run `claude --version` in the VS Code terminal to check if Claude Code is installed; if not, follow the [installation tutorial](Install_CLAUDE_Code_Win.md) first
- **Using WSL instead?** - If you set up the optional WSL/Ubuntu path, install the **WSL** extension from the Extensions sidebar, click the blue/green icon in the bottom-left corner, and select **Connect to WSL** before opening your project folder (accessed at `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude`)

## Workflow Overview

- **VS Code** runs on Windows and provides the visual editor interface
- **Integrated Terminal** runs Claude Code right inside VS Code
- Edit files in the editor, chat with Claude Code in the terminal - best of both worlds

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 10, 2025.
