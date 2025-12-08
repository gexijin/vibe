[Home](./)

# Installing Claude Code on Windows Using WSL

This guide will walk you through installing Claude Code on Windows using Windows Subsystem for Linux (WSL). WSL enables a virtual machine running Linux operating system (OS) on your Windows machine. Although you can install Claude Code natively on Windows, it works much more efficiently under Linux due to the access of many command.

## Overview

- Install WSL
- Set up Ubuntu Linux
- Install Node.js
- Install Claude Code
- Configure your API key
- Ready to use Claude Code!

## What You'll Need

- A Windows 10 (version 2004 or higher) or Windows 11 computer
- Internet connection
- Administrator access on your computer
- Claude Pro/Max subscription or API key
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

**What happens after restart:**
- After you log back into Windows, wait 2-5 minutes
- An Ubuntu terminal window should **automatically appear** to continue the installation
- This is normal! The window opens automatically to complete the setup
- If the window doesn't appear after 5 minutes, don't worry - just manually open Ubuntu (instructions in Step 4)

**Why restart is needed:** The restart allows Windows to enable the WSL and Virtual Machine Platform features that were just installed. Without restarting, WSL won't work properly.

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
   - Example: `myname` or `john123`
- You'll see: `New password:`
- Type a password (you won't see the characters as you type - this is normal for security)
- You'll see: `Retype new password:`
- Type the same password again
- Wait for the setup to complete - you'll see a message like `Installation successful!`

**Important:** Remember this username and password - you'll need them later.

## Step 5: Update Ubuntu

- In the Ubuntu terminal window, type:
   ```
   sudo apt update
   ```
- Type your password (the one you just created) when prompted
   - Again, you won't see the characters as you type
- Wait for the update to complete (1-3 minutes)
- Next, type:
   ```
   sudo apt upgrade -y
   ```
- Wait for all packages to upgrade (this may take 5-10 minutes)

## Step 6: Install Node.js

Claude Code requires Node.js version 18 or higher. Follow these steps:

- In the Ubuntu terminal, type these commands one at a time:

   First, download the nvm installer:
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   ```

   Then run the installer:
   ```
   cat install.sh | bash
   ```

- Load nvm by typing:
   ```
   \. "$HOME/.nvm/nvm.sh"
   ```

- Install Node.js version 24 by typing:
   ```
   nvm install 24
   ```
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

## Step 8: Link with Your Anthropic API

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

**Important:** If you have a Claude Pro or Max subscription, do NOT set the ANTHROPIC_API_KEY environment variable. Leave it unset to use your subscription's included usage and avoid unexpected API charges.

### Option C. Use Anthropic API via Azure

In the terminal window, paste this code to define environment variables:
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=AqJqe
```

You should now be able to use Claude Code with Azure-deployed Claude models.

**Note:** The API key shown above is incomplete. You'll need to get your complete API key from your Azure portal.

## Step 9: Start Using Claude Code

You're all set! Here's how to use Claude Code:

- In the Ubuntu terminal, type:
   ```
   claude
   ```
- You can now chat with Claude!
- To see if it works, ask a general question such as "Explain quantum computing."

## Step 10: Navigate to Your Project
- If you have a project in your Windows folders, you can access it:
   ```
   cd /mnt/c/Users/Username/Documents/YourProject
   ```
   Replace `Username` with your actual Windows username
- Then start Claude:
   ```
   claude
   ```
- Start by asking Claude to explain the codebase to you.
- You can ask Claude to make changes.
- Test your code in your prefered IDE.

## How to Open Ubuntu Terminal Again

After closing the terminal, here's how to open it again:

- Click the **Windows Start button**
- Type `Ubuntu` in the search box
- Click on **Ubuntu** (you'll see a circular orange icon)
- The Ubuntu terminal will open

## Troubleshooting

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



