[Home](./)

# Install Claude Code on Windows Using WSL

Claude Code is a powerful AI coding assistant, but Windows users face a challenge: many developer tools work better on Linux. The solution? WSL (Windows Subsystem for Linux) lets you run a full Linux environment inside Windows—like having two computers in one. This guide walks you through the complete setup so you can start coding with Claude in about 20 minutes.

## Key Concepts

- **WSL (Windows Subsystem for Linux)** - A Windows feature that runs a real Linux system alongside Windows
- **Ubuntu** - A popular, beginner-friendly Linux distribution we'll install through WSL
- **PowerShell** - Windows' built-in command-line tool, used here to install WSL
- **Node.js** - A JavaScript runtime that Claude Code requires to run
- **Terminal** - A text-based interface for running commands (like Ubuntu's command line)

## What You'll Need

- A Windows 10 (version 2004 or higher) or Windows 11 computer
- Administrator access on your computer
- Claude Pro/Max subscription or API key through Azure Foundry
- 15 - 20 minutes

## Step 1: Check if Virtualization is Enabled

Before installing WSL, you need to verify that virtualization is enabled on your computer. This is required for WSL to work.

- **Right-click** on the taskbar (the bar at the bottom of your screen)
- Click on **Task Manager** from the menu
- If Task Manager opens in a small window, click **More details** at the bottom
- Click on the **Performance** tab at the top
- Click on **CPU** in the left sidebar
- Look at the bottom-right section of the window
- Find the line that says **Virtualization:** and check if it says **Enabled**

**If it says "Enabled":** Great! Continue to Step 2.

**If it says "Disabled":** You need to enable virtualization in your computer's BIOS settings:
- Restart your computer
- During startup, press the BIOS key (usually **F2**, **F10**, **Del**, or **Esc** - it depends on your computer manufacturer)
- Look for settings related to "Virtualization Technology", "Intel VT-x", "AMD-V", or "SVM Mode"
- Enable these settings
- Save and exit BIOS (usually **F10**)
- Your computer will restart normally

## Step 2: Open PowerShell as Administrator

- Click the **Windows Start button** (Windows icon in the bottom-left corner)
- Type `PowerShell` in the search box
- In the search results, you'll see **Windows PowerShell**
- **Right-click** on **Windows PowerShell**
- Click **Run as administrator** from the menu
- A window will pop up asking "Do you want to allow this app to make changes to your device?"
- Click **Yes**

A blue window with white text will open - this is PowerShell running as administrator.

## Step 3: Install WSL

**First, check if WSL and Ubuntu are already installed:**

- In the PowerShell window, type:
   ```
   wsl --list --verbose
   ```
- Look at the results:
   - **If you see "Ubuntu" listed** with a STATE of "Running" or "Stopped": WSL and Ubuntu are already installed! Skip to Step 4.
   - **If you see an error message** or "Windows Subsystem for Linux has no installed distributions": Continue with the installation below.

**To install WSL and Ubuntu:**

- In the PowerShell window, type:
   ```
   wsl --install
   ```
- You might see messages like "Installing: Windows Subsystem for Linux" and "Installing: Ubuntu"
- When you see a message saying installation is complete, you need to restart your computer:
   - Click the **Windows Start button**
   - Click the **Power icon**
   - Click **Restart**
- Your computer will restart - this takes about 1-2 minutes

**Why restart is needed:** The restart allows Windows to enable the WSL and Virtual Machine Platform features that were just installed. 

**Note:** If you get an error saying the command is not recognized, your Windows version might be too old. Make sure you have Windows 10 version 2004 or higher, or Windows 11. Run Windows Update to get the latest version.

## Step 4: Set Up Ubuntu (First Time Only)

After your computer restarts, a terminal window with "Ubuntu" in the title should open automatically within 2-5 minutes.

**If the Ubuntu window did NOT open automatically:**
- Click the **Windows Start button**
- Type `Ubuntu` in the search box
- Click on **Ubuntu** (you'll see a circular orange icon)
- The Ubuntu terminal will open and continue the setup

**Now complete the first-time setup:**

- Wait for the message: `Enter new UNIX username:`
- Type a username (use lowercase letters and numbers only, no spaces)
   - Example:  `john`
- You'll see: `New password:`
- Type a simple password (even the same as the user name `john`)
- You won't see the characters as you type - this is normal
- Type the same password again when prompted

**Important:** Remember this username and password - you'll need them later.

## Step 5: Update Ubuntu

- In the Ubuntu terminal window, type:
   ```
   sudo apt update
   ```
- Type your password (the one you just created) when prompted
- Next, type:
   ```
   sudo apt upgrade -y
   ```
- Wait for all packages to upgrade (this may take 5 minutes)

## Step 6: Install Node.js

Claude Code requires Node.js version 18 or higher. Follow these steps:

- In the Ubuntu terminal, copy and paste these commands:

   First, download the nvm installer:
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   cat install.sh | bash
   \. "$HOME/.nvm/nvm.sh"
   nvm install 24
   ```
   This first downloads the nvm installer, installs it, then use it to install node.js v 24.0
- Wait for Node.js to install (2-5 minutes)
- Verify installation by typing:
   ```
   node --version
   ```
- You should see something like `v24.x.x` (the exact numbers may vary)

## Step 7: Install Claude Code

- In the Ubuntu terminal, type:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Wait for Claude Code to install (2-5 minutes)
- You may see some warnings in yellow or red text - this is usually normal
- When installation is complete, verify by typing:
   ```
   claude --version
   ```
- You should see the version number of Claude Code

## Step 8: Configure Your Anthropic API Connection

### Option A. Use your Claude Pro or Max subscription

- In the Ubuntu terminal, type:
   ```
   claude
   ```
- Claude tries to open a browser. If it cannot open automatically, hold **Ctrl** and click on the long URL to open it in a browser. Alternatively, copy the URL and paste it into an external browser.
- Log in to your Claude.ai account (this may happen automatically if you're using Chrome)
- Click **Authorize**
- Click **Copy Code** when a long code appears
- Go back to the terminal window
- To paste in the terminal: **Right-click** and select **Paste** (or press **Ctrl+Shift+V**)
- You should see a success message
- Follow the instructions to complete the setup

### Option B. Use Anthropic API key

If you have an Anthropic API key instead of a Claude subscription:

- First, get your API key from the [Anthropic Console](https://console.anthropic.com/)
- In the Ubuntu terminal, type:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Replace `your-api-key-here` with your actual API key
- To make this permanent (so you don't have to set it every time), add it to your shell profile:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   Replace `your-api-key-here` with your actual API key
- Close and reopen the Ubuntu terminal for the changes to take effect
- You should now be able to use Claude Code with your API key

### Option C. Use OpenRouter API (starts for free!)

OpenRouter is a unified API gateway that provides access to 500+ large language models through a single API key. This can be an economical way to use Claude Code, as you pay only for usage and can choose from models at various price points.

- Sign up at [openrouter.ai](https://openrouter.ai) and log in
- Click **Get API key** and copy the key to a safe location
- Set the required environment variables before starting Claude Code:
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- Start Claude Code:
   ```
   claude
   ```
- Verify the connection by typing `/status` in Claude Code

**Notes:**
- Replace `your-openrouter-api-key` with your actual OpenRouter API key
- `ANTHROPIC_API_KEY` must be explicitly set to empty
- To use alternative models, they must support **tool use capabilities**. You can override models with:
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Browse available models at [openrouter.ai/models](https://openrouter.ai/models)
- Free tier give you 50 API requests per day
- See the [official OpenRouter guide](https://openrouter.ai/docs/guides/claude-code-integration) for more details 


### Option D. Use Anthropic API via Azure Foundry

Before starting Claude Code, in the Ubuntu terminal window, paste this code to define environment variables:
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Note:** Replace `xxxx-eastus2` with your Foundry Resource name (do not use the entire base URL). Replace `your_api_key` with your complete API key from your Azure portal.
 
Then start Claude Code:
``` 
claude
```

You should now be able to use Claude Code with Azure-deployed Claude models.


## Step 9: Test Claude Code

You're all set! To see if it works, ask a general question such as "Explain quantum computing."

## Step 10: Access Your Windows Projects
- If you have a Windows folder called `test_claude` containing the files of a project, you can access it:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Replace `Username` with your actual Windows username.
- Then start Claude:
   ```
   claude
   ```
- Start by asking Claude to explain the codebase to you.
- You can ask Claude to make changes.
- Test your code in your preferred IDE.

**Note:** Claude operates inside a project folder. It saves settings in that folder. It's Claude's workspace.

## Next Steps

- **Set up VS Code**: Follow the [VS Code Getting Started](VS_Code_Getting_Started) guide, then connect it to Claude Code with [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)
- **Learn Git basics**: Add version control to your projects with [Claude Code Git on Windows](Claude_Code_Git_Windows)
- **Try a project**: Work through [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) to see Claude Code in action

## Troubleshooting

### How to open Ubuntu terminal after closing it
- Click the **Windows Start button**, type `Ubuntu`, and click the **Ubuntu** app (orange circle icon)

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
This error means virtualization is not enabled:
- Go back to Step 1 and check Task Manager to see if virtualization is enabled
- If disabled, you need to enable it in your computer's BIOS (see Step 1 for instructions)
- After enabling virtualization, restart your computer and try `wsl --install` again

### "wsl --install" doesn't work
- Make sure you're running PowerShell as Administrator
- Make sure you have Windows 10 version 2004+ or Windows 11
- Try running: `wsl --update` first, then try `wsl --install` again

### Ubuntu window doesn't open after restart
- Click Windows Start
- Type `Ubuntu`
- Click on the Ubuntu app to launch it manually

### "sudo: apt: command not found"
- Your WSL might not have installed correctly
- In PowerShell (as Admin), type: `wsl --unregister Ubuntu`
- Then run `wsl --install` again

### Node.js installation fails
- Make sure you ran `sudo apt update` first
- Try the installation command again

### Claude Code commands not found
- Make sure the installation completed successfully
- Try closing and reopening the Ubuntu terminal
- Try running the installation command again: `curl -fsSL https://claude.ai/install.sh | bash`

## Need Help?

- For WSL issues: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- For Claude Code issues: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
