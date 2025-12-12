[Home](./)

# Use Claude Code from VS Code on Mac

You've installed Claude Code on your Mac - now you want a visual editor to work with your code. VS Code lets you edit files visually while running Claude Code in the integrated terminal. Think of it as having your code editor and AI assistant side by side in one window.

## Key Concepts

- **VS Code** - A free code editor from Microsoft that runs on Mac
- **Integrated Terminal** - A terminal panel inside VS Code where you run Claude Code
- **Explorer Panel** - The file browser on the left side of VS Code

## What You'll Need

- Finished [Installing Claude Code on Mac](./Install_Claude_Code_MacOS)
- Finished [VS Code Basics](./VS_Code_Getting_Started)
- 10-15 minutes

## Step 1: Start VS Code

- Open **Finder** and go to **Applications**
- Find **Visual Studio Code** and double-click it
- If you see a warning "Visual Studio Code is an app downloaded from the internet", click **Open**
- VS Code opens with a Welcome tab - you can close this tab

**Tip:** Right-click VS Code in the Dock and select **Options > Keep in Dock** for easy access later.

## Step 2: Create a Project Folder

- Open **Finder**
- Click **Documents** in the left sidebar
- Click **File** in the menu bar, then **New Folder**
- Name the folder `test_claude`

## Step 3: Open the Folder in VS Code

- In VS Code, click **File** in the menu bar, then **Open Folder**
- Navigate to **Documents** and select the `test_claude` folder you created
- Click **Open**
- If prompted "Do you trust the authors of the files in this folder?", click **Yes, I trust the authors**

You should now see `TEST_CLAUDE` in the Explorer panel on the left side.

## Step 4: Start Claude Code

- Open a new terminal: click **Terminal** in the menu bar, then **New Terminal**
- A terminal panel appears at the bottom of VS Code
- In the terminal, type:
  ```
  claude
  ```
- Claude Code starts - you'll see the familiar Claude Code interface
- You're now ready to use Claude Code while editing files in VS Code

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
- **Option B:** Open Terminal, navigate to your project with `cd ~/Documents/test_claude`, and type `code .`

VS Code remembers your recent folders, so Option A with Open Recent is usually the quickest.

## Next Steps

- Ask Claude Code to explain an existing codebase: "Explain what this project does"
- Have Claude Code help you write new features: "Add a function that calculates the average of a list"
- Use Claude Code to fix bugs: "This code gives an error, can you fix it?"
- Try the Claude Code VS Code extension for a visual interface with inline diffs (search "Claude Code" in Extensions)

## Troubleshooting

- **Terminal shows "zsh" but Claude Code won't start** - Make sure Claude Code is installed correctly; run `claude --version` to verify
- **"code" command not found in Terminal** - In VS Code, click **View** in the menu bar, then **Command Palette**, type "shell command", and select **Shell Command: Install 'code' command in PATH**
- **VS Code won't open because it's from an unidentified developer** - Go to **System Settings > Privacy & Security** and click **Open Anyway**

## Workflow Overview

- **VS Code** provides the visual editor interface
- **Integrated Terminal** runs Claude Code inside VS Code
- Your files stay in your Documents folder (or wherever you choose)
- Edit files in the editor, chat with Claude Code in the terminal - best of both worlds

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 10, 2025.
