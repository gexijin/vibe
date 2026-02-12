[Home](./)

# Install Claude Code on Windows

Claude Code is an AI assistant that lives in your terminal and helps you write, debug, and understand code. This guide walks you through the complete setup: a quick native install via PowerShell, then WSL2 for the full Linux-powered experience.

## Key Concepts

- **WSL (Windows Subsystem for Linux)** - A Windows feature that runs a real Linux system alongside Windows
- **Ubuntu** - A popular, beginner-friendly Linux distribution you can install through WSL
- **PowerShell** - Windows' built-in command-line tool, used here to install Claude Code and WSL

## What You'll Need

- A Windows 10 (version 2004 or higher) or Windows 11 computer
- Administrator access on your computer
- Claude Pro/Max subscription or API key through Azure Foundry
- 10 - 15 minutes

## Step 1: Install Claude Code Natively on Windows (works but not recommended)

- Click the **Windows Start button**
- Type `PowerShell` and click on **Windows PowerShell**
- In the PowerShell window, type:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Wait for the installation to complete
- Close and reopen PowerShell, then verify by typing:
   ```
   claude --version
   ```
- You should see the version number of Claude Code

> **Note:** The native Windows install has some limitations:
> - No Bash tool sandboxing (a security feature only available in WSL2/macOS)
> - Some tools and workflows work better in a Linux environment
>
> Continue with the steps below to install WSL2 for the full experience.

## Step 2: Check Virtualization and Install WSL

**First, check if virtualization is enabled:**

- **Right-click** on the taskbar (the bar at the bottom of your screen)
- Click on **Task Manager** from the menu
- If Task Manager opens in a small window, click **More details** at the bottom
- Click on the **Performance** tab at the top
- Click on **CPU** in the left sidebar
- Look at the bottom-right section of the window
- Find the line that says **Virtualization:** and check if it says **Enabled**

**If it says "Enabled":** Great! Continue below.

**If it says "Disabled":** You need to enable virtualization in your computer's BIOS settings:
- Restart your computer
- During startup, press the BIOS key (usually **F2**, **F10**, **Del**, or **Esc** - it depends on your computer manufacturer)
- Look for settings related to "Virtualization Technology", "Intel VT-x", "AMD-V", or "SVM Mode"
- Enable these settings
- Save and exit BIOS (usually **F10**)
- Your computer will restart normally

**Now install WSL:**

- Click the **Windows Start button**
- Type `PowerShell` in the search box
- **Right-click** on **Windows PowerShell** and click **Run as administrator**
- Click **Yes** when asked "Do you want to allow this app to make changes to your device?"

**Check if WSL and Ubuntu are already installed:**

- In the PowerShell window, type:
   ```
   wsl --list --verbose
   ```
- **If you see "Ubuntu" listed:** WSL is already installed! Skip to Step 3.
- **If you see an error message:** Continue with the installation below.

**To install WSL and Ubuntu:**

- In the PowerShell window, type:
   ```
   wsl --install
   ```
- You might see messages like "Installing: Windows Subsystem for Linux" and "Installing: Ubuntu"
- When installation is complete, restart your computer:
   - Click the **Windows Start button** → **Power icon** → **Restart**
- Your computer will restart — this takes about 1-2 minutes

**Note:** If you get an error saying the command is not recognized, your Windows version might be too old. Make sure you have Windows 10 version 2004 or higher, or Windows 11.

## Step 3: Set Up Ubuntu

After your computer restarts, a terminal window with "Ubuntu" in the title should open automatically within 2-5 minutes.

**If the Ubuntu window did NOT open automatically:**
- Click the **Windows Start button**
- Type `Ubuntu` in the search box
- Click on **Ubuntu** (you'll see a circular orange icon)
- The Ubuntu terminal will open and continue the setup

**Now complete the first-time setup:**

- Wait for the message: `Enter new UNIX username:`
- Type a username (use lowercase letters and numbers only, no spaces)
   - Example: `john`
- You'll see: `New password:`
- Type a simple password (even the same as the user name `john`)
- You won't see the characters as you type - this is normal
- Type the same password again when prompted

**Important:** Remember this username and password — you'll need them later.

## Step 4: Install Claude Code in WSL

- In the Ubuntu terminal, type:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Wait for Claude Code to install
- When installation is complete, verify by typing:
   ```
   claude --version
   ```
- You should see the version number of Claude Code

## Step 5: Connect to Your Anthropic Account

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
- Free tier gives you 50 API requests per day
- See the [official OpenRouter guide](https://openrouter.ai/docs/guides/claude-code-integration) for more details

### Option D. Use Anthropic API via Azure Foundry

Before starting Claude Code, in the Ubuntu terminal, paste this code to define environment variables:
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

## Step 6: Test Claude Code

You're all set! Type `claude` in the Ubuntu terminal and ask a general question such as "Explain quantum computing."

## Step 7: Access Your Projects

**Native Windows (PowerShell):**
- If you have a project folder, navigate to it:
   ```
   cd ~/Documents/test_claude
   ```
- Then start Claude:
   ```
   claude
   ```

**WSL (Ubuntu):**
- If you have a Windows folder called `test_claude`, you can access it:
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

## Step 8: Update Claude Code

Claude Code updates automatically, but you can manually update at any time:

**WSL (Ubuntu):**
```
sudo claude update
```

**Native Windows (PowerShell — run as administrator):**
```
claude update
```

## Next Steps

- **Set up VS Code**: Follow the [VS Code Getting Started](VS_Code_Getting_Started) guide, then connect it to Claude Code with [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)
- **Learn Git basics**: Add version control to your projects with [Claude Code Git on Windows](Claude_Code_Git_Windows)
- **Try a project**: Work through [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) to see Claude Code in action

## Troubleshooting

### First step: Run Claude Doctor

If something isn't working, try running this command first:
```
claude doctor
```
This built-in diagnostic tool checks your installation and reports common issues.

### Claude command not found (native Windows)

- Close and reopen PowerShell
- Try running the installation command again:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Make sure your PATH includes the Claude installation directory

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
This error means virtualization is not enabled:
- Go back to Step 2 and check Task Manager to see if virtualization is enabled
- If disabled, you need to enable it in your computer's BIOS (see Step 2 for instructions)
- After enabling virtualization, restart your computer and try `wsl --install` again

### "wsl --install" doesn't work
- Make sure you're running PowerShell as Administrator
- Make sure you have Windows 10 version 2004+ or Windows 11
- Try running: `wsl --update` first, then try `wsl --install` again

### Ubuntu window doesn't open after restart
- Click Windows Start
- Type `Ubuntu`
- Click on the Ubuntu app to launch it manually

### How to open Ubuntu terminal after closing it
- Click the **Windows Start button**, type `Ubuntu`, and click the **Ubuntu** app (orange circle icon)

### Claude Code commands not found (WSL)
- Make sure the installation completed successfully
- Try closing and reopening the Ubuntu terminal
- Try running the installation command again: `curl -fsSL https://claude.ai/install.sh | bash`

## Need Help?

- For WSL issues: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- For Claude Code issues: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025. Updated February 2026.
