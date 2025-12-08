[Home](./)

# Getting Started with VS Code

You want to write code, but Notepad or TextEdit feels limiting. You need something that helps you code faster - with syntax highlighting, autocomplete, and built-in tools. **VS Code is like a smart notebook for code** - it understands what you're writing and helps you along the way. [Visual Studio Code](https://code.visualstudio.com) is free, runs on any OS, and is used by millions of developers.

## Key Concepts

- **Editor** - The main area where you write code
- **Explorer** - The sidebar that shows your files and folders
- **Extensions** - Add-ons that give VS Code new features
- **Integrated Terminal** - A command line built into VS Code

## What You'll Need

- Windows, macOS, or Linux computer
- Internet connection
- ~500 MB disk space
- 20-25 minutes

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

## Step 3: Open a Folder and Explore

- Click **File** → **Open Folder**
- Navigate to any existing folder on your computer (e.g., Documents)
- Click **Open** (or **Select Folder**)
- If prompted "Do you trust the authors?", click **Yes, I trust the authors**

The Explorer sidebar now shows your folder's files:

- Click on a folder to expand it
- Click on any file to open it in the editor
- Click the **Search** icon in the Activity Bar (magnifying glass) to search across all files

## Step 4: Create a Markdown File

- In Explorer, click the **New File** icon (page with +)
- Name it `README.md`
- Add this content:

```
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
- Click **File** → **Save** to save

Markdown is a simple text format that uses symbols like `#` for headings, `**` for bold, and `-` for lists. It's widely used for documentation and communicating with LLMs like ChatGPT and Claude.

## Step 5: Install Markdown Preview Extension

- Click the **Extensions** icon in Activity Bar (the squares icon)
- Type `Markdown Preview Enhanced` in the search box
- Find **Markdown Preview Enhanced** in the results
- Click **Install**

## Step 6: Preview Your Markdown File

- Open `README.md` if not already open
- Right-click in the editor and select **Markdown Preview Enhanced: Open Preview to the Side**

A preview panel opens showing your formatted Markdown - edit on the left, see changes on the right in real-time!

## Step 7: Use the Integrated Terminal

- Click **Terminal** → **New Terminal** (or press `` Ctrl+` `` with backtick)
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

Check Explorer - the `notes` folder appears! The terminal runs in your project folder, so commands affect your project directly.

## Step 8: Use AI Agents in VS Code (Optional)

VS Code includes [GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat), an AI assistant that can explain, write, and debug code.

- Open the `README.md` file (or any other file in your project)
- Click **Chat** → **Open Chat** in the title bar (or press `Ctrl+Alt+I` on Windows/Linux, `Ctrl+Cmd+I` on Mac)
- If prompted, sign in with your **GitHub account** (a free plan is available)
- In the chat panel that opens, type: "Explain this file"
- Press **Enter**

GitHub Copilot will analyze your file and explain what it does. You can ask it to write new code, fix bugs, or answer questions like "How do I add more features?"

**Tip:** For [inline editing](https://code.visualstudio.com/docs/copilot/copilot-chat), highlight code in any file and press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac) to ask Copilot to modify, fix, or explain just that section.

## How to Reopen Your Project

- Open VS Code from Start menu (Windows), Spotlight (Mac), or Applications (Linux)
- Click **File** → **Open Recent** → select your folder
- Or click **File** → **Open Folder** and navigate to it

## Troubleshooting

- **Preview not showing:** Make sure Markdown Preview Enhanced extension is installed and you have a `.md` file open
- **Terminal shows wrong directory:** Click the trash icon in terminal panel, then click **Terminal** → **New Terminal**
- **Chat menu not visible:** GitHub Copilot Chat may need to be installed - click **Extensions** icon, search for "GitHub Copilot Chat", and install it
- **Extensions not working:** Click **View** → **Command Palette**, type "reload window", and select **Developer: Reload Window**

## The Complete Workflow

1. Open folder in VS Code
2. Create/edit files
3. Use extensions to preview
4. Use terminal for commands
5. Use AI to understand and improve code
6. Save and repeat

## Next Steps

- **Try other file types:** Create `.html`, `.css`, `.js`, or `.py` files and see VS Code's syntax highlighting
- **Explore AI features:** Ask AI to write code, fix bugs, or suggest improvements to your projects
- **Install more extensions:** Try "Prettier" for auto-formatting or "GitLens" for Git features
- **Learn shortcuts:** Click **Help** → **Keyboard Shortcuts Reference** to speed up your workflow

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
