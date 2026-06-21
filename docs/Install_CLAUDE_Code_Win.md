[Home](./)

# Install Claude Code on Windows

Claude Code is an AI assistant that lives in your terminal and helps you write, debug, and understand code. This guide gets you running natively on Windows in just a few minutes. WSL2 is also available at the end as an optional, more advanced setup.

## Key Concepts

- **PowerShell** - Windows' built-in command-line tool, used here to install and run Claude Code
- **Git for Windows** - A free download that adds **Git Bash**, the shell Claude Code uses to run commands
- **WSL (Windows Subsystem for Linux)** - An optional Windows feature that runs a real Linux system alongside Windows, used for the advanced setup at the end

## What You'll Need

- A Windows 10 or Windows 11 computer
- Claude Pro/Max subscription, or an API key
- 5 - 10 minutes

## Step 1: Install Git for Windows (recommended, optional)

Git for Windows is **recommended but optional**. It adds **Git Bash**, the shell Claude Code uses to run commands. If you skip this step, Claude Code falls back to PowerShell instead — so you can move straight to Step 2 and install Git later if you prefer.

- Go to [git-scm.com/download/win](https://git-scm.com/download/win)
- The download should start automatically — open the installer when it finishes
- Click **Next** through the installer, accepting the default options
- Click **Install**, then **Finish**

That's it — Claude Code will detect Git Bash automatically when it starts.

## Step 2: Install Claude Code

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

## Step 3: Connect to Your Anthropic Account

### Option A. Use your Claude Pro or Max subscription

- In the PowerShell window, type:
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

The API-based options below stay in **PowerShell** and use the `setx` command, which saves a setting permanently. After running `setx`, **close and reopen PowerShell** so the change takes effect, then start `claude`.

### Option B. Use Anthropic API key

If you have an Anthropic API key instead of a Claude subscription:

- Get your API key from the [Anthropic Console](https://console.anthropic.com/)
- In PowerShell, type:
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
   Replace `your-api-key-here` with your actual API key
- Close and reopen PowerShell for the change to take effect
- Start Claude Code:
   ```
   claude
   ```

### Option C. Use OpenRouter API (starts for free!)

OpenRouter is a unified API gateway that provides access to 500+ large language models through a single API key. This can be an economical way to use Claude Code, as you pay only for usage and can choose from models at various price points.

- Sign up at [openrouter.ai](https://openrouter.ai) and log in
- Click **Get API key** and copy the key to a safe location
- In PowerShell, set the required environment variables:
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- Close and reopen PowerShell, then start Claude Code:
   ```
   claude
   ```
- Verify the connection by typing `/status` in Claude Code

**Notes:**
- Replace `your-openrouter-api-key` with your actual OpenRouter API key
- `ANTHROPIC_API_KEY` must be explicitly set to empty
- To use alternative models, they must support **tool use capabilities**. You can override models with:
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- Browse available models at [openrouter.ai/models](https://openrouter.ai/models)
- Free tier gives you 50 API requests per day
- See the [official OpenRouter guide](https://openrouter.ai/docs/guides/claude-code-integration) for more details

### Option D. Use Anthropic API via Azure Foundry

In PowerShell, paste this code to define the environment variables:
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**Note:** Replace `xxxx-eastus2` with your Foundry Resource name (do not use the entire base URL). Replace `your_api_key` with your complete API key from your Azure portal.

Then close and reopen PowerShell, and start Claude Code:
```
claude
```

You should now be able to use Claude Code with Azure-deployed Claude models.

## Step 4: Test Claude Code

You're all set! Type `claude` in PowerShell and ask a general question such as "Explain quantum computing."

## Step 5: Access Your Projects

- If you have a project folder, navigate to it in PowerShell:
   ```
   cd ~/Documents/test_claude
   ```
- Then start Claude:
   ```
   claude
   ```
- Start by asking Claude to explain the codebase to you.
- You can ask Claude to make changes.
- Test your code in your preferred IDE.

**Note:** Claude operates inside a project folder. It saves settings in that folder. It's Claude's workspace.

## Step 6: (Optional) Install WSL2 for the Full Linux Experience

The native setup above is almost all that most people need. But Claude Code performs better under Linux. WSL2 runs a real Linux system inside Windows and adds **Bash tool sandboxing** (a security feature) plus better compatibility with Linux toolchains. It takes longer to set up and requires a restart, so only do this if you want the full Linux experience.

### a) Check virtualization and install WSL

**First, check if virtualization is enabled:**

- **Right-click** on the taskbar (the bar at the bottom of your screen)
- Click on **Task Manager** from the menu
- If Task Manager opens in a small window, click **More details** at the bottom
- Click on the **Performance** tab at the top
- Click on **CPU** in the left sidebar
- Find the line that says **Virtualization:** and check if it says **Enabled**

**If it says "Disabled":** You need to enable virtualization in your computer's BIOS settings:
- Restart your computer
- During startup, press the BIOS key (usually **F2**, **F10**, **Del**, or **Esc** - it depends on your computer manufacturer)
- Look for settings related to "Virtualization Technology", "Intel VT-x", "AMD-V", or "SVM Mode"
- Enable these settings
- Save and exit BIOS (usually **F10**)

**Now install WSL:**

- Click the **Windows Start button**, type `PowerShell`
- **Right-click** on **Windows PowerShell** and click **Run as administrator**
- Click **Yes** when asked "Do you want to allow this app to make changes to your device?"
- In the PowerShell window, type:
   ```
   wsl --install
   ```
- You might see messages like "Installing: Windows Subsystem for Linux" and "Installing: Ubuntu"
- When installation is complete, restart your computer

**Note:** `wsl --install` requires Windows 10 version 2004 or higher, or Windows 11. If the command is not recognized, your Windows version may be too old.

### b) Set up Ubuntu

After your computer restarts, a terminal window with "Ubuntu" in the title should open automatically within 2-5 minutes. If it doesn't, click the **Windows Start button**, type `Ubuntu`, and click the **Ubuntu** app (orange circle icon).

- Wait for the message: `Enter new UNIX username:`
- Type a username (lowercase letters and numbers only, no spaces) — for example `john`
- You'll see: `New password:`
- Type a simple password (you won't see the characters as you type — this is normal)
- Type the same password again when prompted

**Important:** Remember this username and password — you'll need them later.

### c) Install Claude Code in WSL

- In the Ubuntu terminal, type:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Verify by typing:
   ```
   claude --version
   ```
- Connect your account by typing `claude` in the Ubuntu terminal and following the browser login (the same as Step 3, Option A). If you use an API key instead, set it with `export ANTHROPIC_API_KEY="your-api-key-here"` (WSL uses Linux commands, not `setx`)
- To open a Windows project folder from WSL:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Replace `Username` with your actual Windows username.

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
- Check Task Manager to see if virtualization is enabled (see the optional WSL section above)
- If disabled, enable it in your computer's BIOS
- After enabling virtualization, restart your computer and try `wsl --install` again

### "wsl --install" doesn't work
- Make sure you're running PowerShell as Administrator
- Make sure you have Windows 10 version 2004+ or Windows 11
- Try running: `wsl --update` first, then try `wsl --install` again

### Ubuntu window doesn't open after restart
- Click the **Windows Start button**, type `Ubuntu`, and click the **Ubuntu** app to launch it manually

## Need Help?

- For WSL issues: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- For Claude Code issues: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025. Updated June 2026.
