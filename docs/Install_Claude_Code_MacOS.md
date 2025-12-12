[Home](./)

# Install Claude Code on Mac

Claude Code is an AI assistant that lives in your Terminal and helps you write, debug, and understand code. Think of it as having a knowledgeable coding partner available whenever you need help. Whether you're a complete beginner or an experienced developer, Claude Code can accelerate your workflow and help you learn.

This guide walks you through installation step by step, with detailed instructions for beginners.

## Overview

- Download and install Node.js
- Install Claude Code using npm
- Configure your API key
- Start using Claude Code

## Key Concepts

- **Terminal**: A built-in Mac app where you type commands instead of clicking buttons. It's how you'll interact with Claude Code.
- **Node.js**: Software that Claude Code needs to run. Think of it as the engine that powers Claude Code.
- **Claude Code**: An AI coding assistant you run in Terminal. It can answer questions, write code, and help you understand existing projects.

## What You'll Need

- A Mac computer (macOS 10.15 Catalina or newer recommended)
- Internet connection
- Administrator access on your computer
- Claude Pro/Max subscription or API key
- 15 - 20 minutes

## Step 1: Download Node.js

Claude Code requires Node.js version 18 or higher.

**First, check if Node.js is already installed:**

- Click the **Launchpad** icon in your Dock (the icon with colorful squares)
- Type `Terminal` in the search box at the top
- Click on **Terminal** (a black square icon)
- In Terminal, type:
   ```
   node --version
   ```
- Look at the results:
   - **If you see a version number like `v18.x.x` or higher**: Node.js is already installed! Skip to Step 4.
   - **If you see "command not found"**: Continue with the installation below.

**To download Node.js:**

- Open your web browser (Safari, Chrome, Firefox, etc.)
- Go to this website:
   ```
   https://nodejs.org/
   ```
- Click on the green button that says **Get Node.js**
- Click the green button that says **macOS Installer (.pkg)** in the middle of the screen
- A file will download to your Downloads folder (usually takes 30-60 seconds)
   - The file will be named something like `node-v24.x.x.pkg`

## Step 2: Install Node.js

- Open **Finder** (click the blue smiling face icon in your Dock)
- Click **Downloads** in the left sidebar
- Find the file you just downloaded (looks like `node-v24.x.x.pkg`)
- Double-click the file to open it
- An installer window will appear - click **Continue**
- Click **Continue** again on the License screen
- Click **Agree** to accept the license
- Click **Install**
- You'll be asked for your Mac password (the one you use to log in)
- Type your password and click **Install Software**
- Wait for installation to complete (1-2 minutes)
- Click **Close** when you see "The installation was successful"
- You can move the installer to Trash if asked

## Step 3: Verify Node.js Installation

- Click the **Launchpad** icon in your Dock (the icon with colorful squares)
- Type `Terminal` in the search box at the top
- Click on **Terminal** (a black square icon)
- A Terminal window will open
- In Terminal, type:
   ```
   node --version
   ```
- You should see something like `v24.x.x` (the exact numbers may vary)
- If you see a version number, great! Node.js is installed correctly

**If you see "command not found":**
- Close Terminal completely (click **Terminal** in the menu bar, then **Quit Terminal**)
- Open Terminal again
- Try the command again

**Tip:** Keep Terminal open for the next steps.

## Step 4: Install Claude Code

- In Terminal, type:
   ```
   npm install -g @anthropic/claude-code
   ```
- Wait for Claude Code to install (2-5 minutes)
- If you see a "permission denied" error, try with `sudo`:
   ```
   sudo npm install -g @anthropic/claude-code
   ```
   Then enter your Mac password when prompted (you won't see it as you type)
- You may see some warnings in yellow or red text - this is usually normal
- When installation is complete, verify by typing:
   ```
   claude --version
   ```
- You should see the version number of Claude Code

## Step 5: Connect to Your Anthropic Account

### Option A. Use your Claude Pro or Max subscription

- In Terminal, type:
   ```
   claude
   ```
- Claude tries to open a browser. If it doesn't open automatically, copy the URL shown in Terminal and paste it into your browser.
- Log in to your Claude.ai account (this may happen automatically)
- Click **Authorize**
- Click **Copy Code** when a long code appears
- Go back to the Terminal window
- To paste in Terminal: Click **Edit** in the menu bar, then click **Paste**
- You should see a success message
- Follow the instructions to complete the setup

### Option B. Use Anthropic API key

If you have an Anthropic API key instead of a Claude subscription:

- First, get your API key from the [Anthropic Console](https://console.anthropic.com/)
- In Terminal, type:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Replace `your-api-key-here` with your actual API key
- To make this permanent (so you don't have to set it every time), add it to your shell profile:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```
   Replace `your-api-key-here` with your actual API key
- Close and reopen Terminal for the changes to take effect

**Note:** If you're using an older Mac with bash instead of zsh, replace `~/.zshrc` with `~/.bash_profile` in the command above.

### Option C. Use Anthropic API via Azure Foundry

This option is for organizations using Azure-hosted Claude models. In the Terminal window, paste this code to define environment variables (before starting Claude):
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Note:** Replace `xxxx-eastus2` with your Foundry Resource name (do not use the entire base URL). Replace `your_api_key` with your complete API key from your Azure portal.

## Step 6: Start Using Claude Code

You're all set! Here's how to use Claude Code:

- In Terminal, type:
   ```
   claude
   ```
- It asks you a few questions before getting ready to chat
- To see if it works, ask a general question such as "Explain quantum computing."

## Step 7: Navigate to Your Project

- If you have a project in your Mac folders, you can navigate to it:
   ```
   cd ~/Documents/YourProject
   ```
   Replace `YourProject` with your actual project folder name

- Then start Claude:
   ```
   claude
   ```
- Start by asking Claude to explain the codebase to you.
- You can ask Claude to make changes.
- Test your code in your preferred IDE.

**Note:** Claude operates inside a project folder. It define writing permissions in the folder and saves settings in that folder. It's Claude's workspace.

## Next Steps
- [VS Code Getting Started](./VS_Code_Getting_Started.md) - Learn to use VS Code, a popular code editor
- [Claude Code in VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - Run Claude Code inside VS Code
- [Writing a Research Paper with Claude Code](./Writing_Research_Paper_Claude_Code.md) - Use Claude Code for academic writing

## How to Open Terminal Again

After closing Terminal, here's how to open it again:

- Click the **Launchpad** icon in your Dock (the icon with colorful squares)
- Type `Terminal` in the search box at the top
- Click on **Terminal**
- A Terminal window will open

## Troubleshooting

### Node.js installer won't open
- Make sure you downloaded the `.pkg` file from nodejs.org
- Try right-clicking the file and selecting **Open** instead of double-clicking
- Go to **System Settings** > **Privacy & Security** and click **Open Anyway**

### "node: command not found" after installation
- Close Terminal completely (click **Terminal** in the menu bar, then **Quit Terminal**)
- Open Terminal again
- Try `node --version` again
- If still not working, restart your Mac and try again

### npm installation fails with permission errors
- Add `sudo` before the npm command:
  ```
  sudo npm install -g @anthropic/claude-code
  ```
- Enter your Mac password when prompted (you won't see it as you type)

### Claude Code commands not found
- Make sure npm installation completed successfully
- Try closing and reopening Terminal
- Check if Claude Code is installed: `npm list -g @anthropic/claude-code`
- Try installing again: `npm install -g @anthropic/claude-code`

### "Cannot find module" errors
- Make sure Node.js is properly installed: `node --version`
- Try reinstalling Claude Code: `npm uninstall -g @anthropic/claude-code` then `npm install -g @anthropic/claude-code`

## Tips for Mac Users

### Finding Project Paths
To find the path to a folder:
- Open Finder
- Navigate to your project folder
- Drag and drop the folder into Terminal - the full path will appear!

### Using Different Terminal Apps
You can also use other terminal apps like:
- iTerm2 (popular alternative with more features)
- Warp (modern terminal with AI features)
- Hyper (cross-platform terminal)

Claude Code works with all of them!

## Need Help?

- For Node.js download: [Node.js Official Website](https://nodejs.org/)
- For Node.js issues: [Node.js Documentation](https://nodejs.org/docs/)
- For npm issues: [npm Documentation](https://docs.npmjs.com/)
- For Claude Code issues: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

*Last updated: December 2025*
