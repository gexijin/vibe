[Home](./)

# Installing Claude Code on Windows Using WSL

This guide will walk you through installing Claude Code on Windows using Windows Subsystem for Linux (WSL). Each step includes detailed instructions for beginners.

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

## Step 1: Check if Virtualization is Enabled

Before installing WSL, you need to verify that virtualization is enabled on your computer. This is required for WSL to work.

1. **Right-click** on the taskbar (the bar at the bottom of your screen)
2. Click on **Task Manager** from the menu
3. If Task Manager opens in a small window, click **More details** at the bottom
4. Click on the **Performance** tab at the top
5. Click on **CPU** in the left sidebar
6. Look at the bottom-right section of the window
7. Find the line that says **Virtualization:** and check if it says **Enabled**

**If it says "Enabled":** Great! Continue to Step 2.

**If it says "Disabled":** You need to enable virtualization in your computer's BIOS settings:
- Restart your computer
- During startup, press the BIOS key (usually **F2**, **F10**, **Del**, or **Esc** - it depends on your computer manufacturer)
- Look for settings related to "Virtualization Technology", "Intel VT-x", "AMD-V", or "SVM Mode"
- Enable these settings
- Save and exit BIOS (usually **F10**)
- Your computer will restart normally

## Step 2: Open PowerShell as Administrator

1. Click the **Windows Start button** (Windows icon in the bottom-left corner)
2. Type `PowerShell` in the search box
3. In the search results, you'll see **Windows PowerShell**
4. **Right-click** on **Windows PowerShell**
5. Click **Run as administrator** from the menu
6. A window will pop up asking "Do you want to allow this app to make changes to your device?"
7. Click **Yes**

A blue window with white text will open - this is PowerShell running as administrator.

## Step 3: Install WSL

1. In the PowerShell window, type:
   ```
   wsl --install
   ```
2. You'll see text appearing as Windows downloads and installs WSL
3. This process may take 5-15 minutes depending on your internet speed
4. You might see messages like "Installing: Windows Subsystem for Linux" and "Installing: Ubuntu"
5. When you see a message saying installation is complete, you need to restart your computer:
   - Click the **Windows Start button**
   - Click the **Power icon**
   - Click **Restart**
6. Your computer will restart - this takes about 1-2 minutes

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
1. Click the **Windows Start button**
2. Type `Ubuntu` in the search box
3. Click on **Ubuntu** (you'll see a circular orange icon)
4. The Ubuntu terminal will open and continue the setup

**Now complete the first-time setup:**

1. Wait for the message: `Enter new UNIX username:`
2. Type a username (use lowercase letters and numbers only, no spaces)
   - Example: `myname` or `john123`
3. Press **Enter**
4. You'll see: `New password:`
5. Type a password (you won't see the characters as you type - this is normal for security)
6. Press **Enter**
7. You'll see: `Retype new password:`
8. Type the same password again
9. Press **Enter**
10. Wait for the setup to complete - you'll see a message like `Installation successful!`

**Important:** Remember this username and password - you'll need them later.

## Step 5: Update Ubuntu

1. In the Ubuntu terminal window, type:
   ```
   sudo apt update
   ```
2. Press **Enter**
3. Type your password (the one you just created) and press **Enter**
   - Again, you won't see the characters as you type
4. Wait for the update to complete (1-3 minutes)
5. Next, type:
   ```
   sudo apt upgrade -y
   ```
6. Press **Enter**
7. Wait for all packages to upgrade (this may take 5-10 minutes)

## Step 6: Install Node.js 

Claude Code requires Node.js version 18 or higher. Follow these steps:

1. In the Ubuntu terminal, type these commands one at a time:

   First, download the nvm installer:
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   ```

   Then run the installer:
   ```
   cat install.sh | bash
   ```

2. Load nvm by typing:
   ```
   \. "$HOME/.nvm/nvm.sh"
   ```

3. Install Node.js version 24 by typing:
   ```
   nvm install 24
   ```
4. Wait for Node.js to install (2-5 minutes)
5. Verify installation by typing:
   ```
   node --version
   ```
6. You should see something like `v24.x.x` (the exact numbers may vary)

## Step 7: Install Claude Code

1. In the Ubuntu terminal, type:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
2. Wait for Claude Code to install (2-5 minutes)
3. You may see some warnings in yellow or red text - this is usually normal
5. When installation is complete, verify by typing:
   ```
   claude --version
   ```
6. You should see the version number of Claude Code

## Step 8: Link with Your Anthropic API

### Option A. Use your Claude Pro or Max subscription

1. In the Ubuntu terminal, type:
   ```
   claude
   ```
2. Claude tries to open a browser. If it cannot open automatically, hold **Ctrl** and click on the long URL to open it in a browser. Alternatively, copy the URL and paste it into an external browser.
3. Log in to your Claude.ai account (this may happen automatically if you're using Chrome)
4. Click **Authorize**
5. Click **Copy Code** when a long code appears
6. Go back to the terminal window
7. To paste in the terminal: **Right-click** and select **Paste** (or press **Ctrl+Shift+V**)
8. Press **Enter**
9. You should see a success message
10. Follow the instructions to complete the setup

### Option B. Use Anthropic API via Azure

In the terminal window, paste this code to define environment variables:
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=gexij-m7zjh4bo-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=AqJqe
```

Press **Enter** after pasting. You should now be able to use Claude Code with Azure-deployed Claude models.

**Note:** The API key shown above is incomplete. You'll need to get your complete API key from your Azure portal.

## Step 9: Start Using Claude Code

You're all set! Here's how to use Claude Code:

1. In the Ubuntu terminal, type:
   ```
   claude
   ```
2. Press **Enter**
3. You can now chat with Claude!
4. To see if it works, ask a general question such as "Explain quantum computing."

## Step 10: Navigate to Your Project
1. If you have a project in your Windows folders, you can access it:
   ```
   cd /mnt/c/Users/Username/Documents/YourProject
   ```
   Replace `Username` with your actual Windows username
2. Then start Claude:
   ```
   claude
   ```
3. Start by asking Claude to explain the codebase to you. 
4. You can ask Claude to make changes. 
5. Test your code in your prefered IDE.

## How to Open Ubuntu Terminal Again

After closing the terminal, here's how to open it again:

1. Click the **Windows Start button**
2. Type `Ubuntu` in the search box
3. Click on **Ubuntu** (you'll see a circular orange icon)
4. The Ubuntu terminal will open

## Troubleshooting

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
This error means virtualization is not enabled:
1. Go back to Step 1 and check Task Manager to see if virtualization is enabled
2. If disabled, you need to enable it in your computer's BIOS (see Step 1 for instructions)
3. After enabling virtualization, restart your computer and try `wsl --install` again

### "wsl --install" doesn't work
- Make sure you're running PowerShell as Administrator
- Make sure you have Windows 10 version 2004+ or Windows 11
- Try running: `wsl --update` first, then try `wsl --install` again

### Ubuntu window doesn't open after restart
1. Click Windows Start
2. Type `Ubuntu`
3. Click on the Ubuntu app to launch it manually

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



