[Home](./)

# Getting Started with VS Code

## The Problem

You want to write code, but Notepad or TextEdit feels limiting. You need something that helps you code faster - with syntax highlighting, autocomplete, and built-in tools. **VS Code is like a smart notebook for code** - it understands what you're writing and helps you along the way. [Visual Studio Code](https://code.visualstudio.com) is free, runs on any OS, and is used by millions of developers.

## Key Concepts

- **Editor** - The main area where you write code
- **Explorer** - The sidebar that shows your files and folders
- **Extensions** - Add-ons that give VS Code new features
- **Integrated Terminal** - A command line built into VS Code

## What You'll Do

- Download and install VS Code
- Tour the interface
- Open a folder and navigate files
- Create and edit a Markdown file
- Install Markdown Preview extension
- Preview your file in VS Code
- Run commands in the integrated terminal

## What You'll Need

- Windows, macOS, or Linux computer
- Internet connection
- ~500 MB disk space

## Step 1: Download and Install VS Code

- Go to [code.visualstudio.com](https://code.visualstudio.com)
- Click the **Download** button (it detects your OS)
- Run the installer:
   - **Windows:** Double-click the `.exe`, click **Next** through the prompts
   - **Mac:** Open the `.dmg`, drag VS Code to **Applications**
   - **Linux:** Follow instructions for your package manager
- Launch VS Code

You'll see a Welcome tab with getting started options.

## Step 2: Tour the Interface

VS Code has five main areas:

- **Activity Bar** (left edge) - Icons for Explorer, Search, Git, Extensions, etc.
- **Side Bar** - Shows content for selected activity (files, search results)
- **Editor** (center) - Where you write code
- **Panel** (bottom) - Terminal, Problems, Output
- **Status Bar** (bottom edge) - Info about your file and project

Click the **Explorer** icon (top of Activity Bar) to see the file browser.

## Step 3: Open a Project Folder

- Click **File** → **Open Folder**
- Navigate to any existing folder on your computer (e.g., Documents or a project you've downloaded)
- Select it and click **Open**
- If prompted "Do you trust the authors?", click **Yes, I trust the authors**
- In the Explorer sidebar, click on a folder to expand it
- Click on any file to open it in the editor
- Click the **Search** icon in the Activity Bar (magnifying glass) to search across all files in your folder - type a word and see results from multiple files

## Step 4: Create a Markdown File

- In Explorer, click the **New File** icon (page with +)
- Name it `README.md`
- Add this content:
   ```markdown
   # My Project

   This is a **demo project** for learning VS Code.

   ## Features
   - Easy to edit
   - Markdown formatting
   - Live preview

   ## Next Steps
   1. Add more content
   2. Try other file types
   3. Explore extensions
   ```
- Press `Ctrl+S` (Windows/Linux) or `Cmd+S` (Mac) to save

Markdown is a simple text format that uses symbols like `#` for headings, `**` for bold, and `-` for lists. It's widely used for documentation, README files, and notes. Markdown is also the native format for communicating with LLMs like ChatGPT and Claude - learning it helps you write better prompts and read AI responses.

## Step 5: Install Markdown Preview Extension

- Click the **Extensions** icon in Activity Bar (or `Ctrl+Shift+X`)
- Type `Markdown Preview Enhanced` in the search box
- Find **Markdown Preview Enhanced**
- Click **Install**

## Step 6: Preview Your Markdown File

- Open `README.md` if not already open
- Press `Ctrl+Shift+V` (Windows/Linux) or `Cmd+Shift+V` (Mac)

A preview panel opens showing your formatted Markdown!

**Tip:** Use `Ctrl+K V` (Windows/Linux) or `Cmd+K V` (Mac) to open preview side-by-side. Edit on the left, see changes on the right.

## Step 7: Use the Integrated Terminal

- Press `` Ctrl+` `` (backtick) to open the terminal
- Try these commands:

**List files:**
```
ls
```
(On Windows Command Prompt, use `dir`)

**Print working directory:**
```
pwd
```
(On Windows Command Prompt, use `cd`)

**Create a new folder:**
```
mkdir notes
```

- Check Explorer - the `notes` folder appears!

The terminal runs in your project folder, so commands affect your project directly.

## How to Reopen

**Open VS Code:** Start menu/Spotlight → type "Visual Studio Code"

**Open your project:**
- **File** → **Open Recent** → select your folder
- Or **File** → **Open Folder**

## Troubleshooting

- **Preview not showing:** Make sure Markdown Preview Enhanced extension is installed and you have a `.md` file open
- **Terminal shows wrong directory:** Click the trash icon to close terminal, then reopen with `` Ctrl+` ``
- **Extensions not working:** Try **Developer: Reload Window** from Command Palette (`Ctrl+Shift+P`)
- **Need help?** [VS Code Docs](https://code.visualstudio.com/docs) • [VS Code GitHub](https://github.com/microsoft/vscode/issues)

## The Complete Workflow

1. Open folder in VS Code
2. Create/edit files
3. Use extensions to preview
4. Use terminal for commands
5. Save and repeat

## Next Steps

- **Try other file types:** Create `.html`, `.css`, `.js`, or `.py` files
- **Install more extensions:** Try "Prettier" for auto-formatting, "GitLens" for Git features
- **Learn shortcuts:** **Help** → **Keyboard Shortcuts Reference**

---

*Created on December 7, 2025 with help from Claude Code.*
