[Home](./)

# Setting Up VS Code for Claude Code on WSL

You've installed WSL and Claude Code on your Windows machine - now you want a visual editor to work with your code. VS Code bridges the gap between Windows and your Linux environment, letting you edit files visually while running Claude Code in the integrated terminal. Think of VS Code as a window into your Linux world.

## Key Concepts

- **VS Code** - A free code editor from Microsoft that runs on Windows but can connect to WSL
- **WSL Extension** - Connects VS Code to your Linux environment so you can run Linux tools like Claude Code
- **Integrated Terminal** - A terminal panel inside VS Code that runs in your WSL (Linux) environment
- **/mnt/c/** - How WSL accesses your Windows files (e.g., `/mnt/c/Users/...` = `C:\Users\...`)

## What You'll Need

- Windows with WSL and Claude Code already installed (from the previous tutorial)
- Claude Pro/Max subscription or API key (already configured)
- Internet connection
- 10-15 minutes

## Step 1: Create a Project Folder

- Open **File Explorer** (click the folder icon in your taskbar)
- Navigate to **Documents**
- Right-click in the empty space, select **New > Folder**
- Name the folder `test_claude`

## Step 2: Start VS Code

- Windows Start button and search for VS Code


## Step 3: Install the WSL Extension

- In VS Code, click the **Extensions** icon in the left sidebar (it looks like four squares)
- Type `WSL` in the search box
- Find **WSL** by Microsoft (it should be the first result)
- Click the blue **Install** button
- Wait for installation to complete (a few seconds)

## Step 4: Connect VS Code to WSL

- Look at the bottom-left corner of VS Code - you'll see a blue or green icon
- Click this icon (or press `F1` and type "WSL")
- Select **Connect to WSL** from the menu
- VS Code will reload and connect to your Ubuntu installation
- The bottom-left corner should now show **WSL: Ubuntu**

The first time you connect, VS Code installs a small server in WSL. This takes about 30 seconds.

## Step 5: Open the Folder in VS Code

- In VS Code (still connected to WSL), click **File** in the menu bar, then **Open Folder**
- A **Open Folder** dropdown appears in the top center. 
- Type your folder by typing:
  ```
  /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Replace `YOUR_USERNAME` with your Windows username (e.g., `John.Smith`)
- Click **OK**. VS Code reloads with your `test_claude` folder 
- If prompted "Do you trust the authors?", click **Yes, I trust the authors**
- Close the original VS Code window

## Step 6: Start Claude Code

- After VS Code reloads, open a new terminal: click **Terminal** in the menu bar, then **New Terminal**
- In the terminal panel, type:
  ```
  claude
  ```
- Claude Code starts - you'll see the familiar Claude Code interface
- You're now ready to use Claude Code while editing files in VS Code

## Step 7: Test the Workflow

- In Claude Code, type: 
```
Write a short article explaining why LLMs like to use Markdown format. Save it as article.md
```
- Claude Code creates the file - you'll see `article.md` appear in the Explorer panel on the left
- Click on `article.md` in the Explorer to view it in the editor
- To preview the formatted article: right-click on the `article.md` tab and select **Open Preview**
- You'll see the Markdown rendered with proper headings, bullet points, and formatting

## Reopening VS Code Later

After closing VS Code, here's how to get back to your WSL projects:

- **Option A:** Open VS Code, click the bottom-left corner, select **Connect to WSL**, then **File > Open Recent**. Select '/mnt/c/Users/YOUR_USERNAME/Documents/test_claude[WSL:Ubuntu 24.01]`
- **Option B:** Open Ubuntu App from Windows, at the terminal terminal, navigate to your project, and type `code .`

VS Code remembers your recent folders, so Option A with Open Recent is usually the quickest.

## Next Steps

- Ask Claude Code to explain an existing codebase: "Explain what this project does"
- Have Claude Code help you write new features: "Add a function that calculates the average of a list"
- Use Claude Code to fix bugs: "This code gives an error, can you fix it?"
- Try the Claude Code VS Code extension for a visual interface with inline diffs (search "Claude Code" in Extensions)
- To handle bigger files more efficiently, create a folder in the WSL file system (/home/user/). From Windows, look for the Linux icon in bottom of the sidebar of File explorer. Or enter `\\wsl.localhost\' in the explorer.

## Troubleshooting

- **"WSL: Ubuntu" not showing in bottom-left** - Make sure WSL is installed correctly; try opening Ubuntu terminal first to verify it works
- **Terminal shows PowerShell instead of Linux** - Click the dropdown arrow next to the **+** in the terminal panel and select **Ubuntu (WSL)**
- **`claude` command not found** - Run `claude --version` to check if Claude Code is installed; if not, follow the WSL installation tutorial first

## Workflow Overview

- **VS Code** runs on Windows and provides the visual editor interface
- **WSL Extension** connects VS Code to Ubuntu so you can run Linux tools
- **Integrated Terminal** runs Claude Code inside WSL
- Your files stay in Windows (Documents folder) - WSL accesses them via `/mnt/c/`
- Edit files in the editor, chat with Claude Code in the terminal - best of both worlds

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 10, 2025.
