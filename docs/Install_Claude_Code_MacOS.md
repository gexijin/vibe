[Home](./)

# Installing Claude Code on Mac

This guide will walk you through installing Claude Code on your Mac. Each step includes detailed instructions for beginners.

## Overview

- Download and install Node.js
- Install Claude Code using npm
- Configure your API key
- Ready to use Claude Code!

## What You'll Need

- A Mac computer (macOS 10.15 Catalina or newer recommended)
- Internet connection
- Administrator access on your computer

## Step 1: Download Node.js

Claude Code requires Node.js version 18 or higher.

1. Open your web browser (Safari, Chrome, Firefox, etc.)
2. Go to this website:
   ```
   https://nodejs.org/
   ```
3. You'll see the Node.js homepage
4. Click on the green button that says **Get Node.js**
5. Click the green button that says **macOS Installer (.pkg)** in the middle of the screen
6. A file will download to your Downloads folder (usually takes 30-60 seconds)
   - The file will be named something like `node-v24.x.x.pkg`

## Step 2: Install Node.js

1. Open **Finder** (click the blue smiling face icon in your Dock)
2. Click **Downloads** in the left sidebar
3. Find the file you just downloaded (looks like `node-v24.x.x.pkg`)
4. Double-click the file to open it
5. An installer window will appear - click **Continue**
6. Click **Continue** again on the License screen
7. Click **Agree** to accept the license
8. Click **Install**
9. You'll be asked for your Mac password (the one you use to log in)
10. Type your password and click **Install Software**
11. Wait for installation to complete (1-2 minutes)
12. Click **Close** when you see "The installation was successful"
13. You can move the installer to Trash if asked

## Step 3: Verify Node.js Installation

1. Press **Command (⌘) + Space** on your keyboard
2. Type `Terminal` in the search box
3. Click on **Terminal** (a black square icon)
4. A window will open with white or black background and text - this is Terminal
5. In Terminal, type:
   ```
   node --version
   ```
6. Press **Enter**
7. You should see something like `v24.x.x` (the exact numbers may vary)
8. If you see a version number, great! Node.js is installed correctly

**If you see "command not found":**
- Close Terminal completely (press **Command (⌘) + Q**)
- Open Terminal again
- Try the command again

**Tip:** Keep Terminal open for the next steps.

## Step 4: Install Claude Code

1. In Terminal, type:
   ```
   sudo npm install -g @anthropic/claude-code
   ```
2. You'll be asked for your Mac password
3. Type your password (you won't see it as you type) and press **Enter**
4. Wait for Claude Code to install (2-5 minutes)
5. You may see some warnings in yellow or red text - this is usually normal
6. When installation is complete, verify by typing:
   ```
   claude --version
   ```
7. Press **Enter**
8. You should see the version number of Claude Code

## Step 5: Link with Your Anthropic API

### Option A. Use your Claude Pro or Max subscription

1. In Terminal, type:
   ```
   claude
   ```
2. Press **Enter**
3. Claude tries to open a browser. If it cannot open automatically, hold **Command (⌘)** and click on the long URL to open it in a browser. Alternatively, copy the URL and paste it into your browser.
4. Log in to your Claude.ai account (this may happen automatically)
5. Click **Authorize**
6. Click **Copy Code** when a long code appears
7. Go back to the Terminal window
8. To paste in Terminal: **Right-click** and select **Paste** (or press **Command (⌘) + V**)
9. Press **Enter**
10. You should see a success message
11. Follow the instructions to complete the setup

### Option B. Use Anthropic API via Azure

In the Terminal window, paste this code to define environment variables:
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

Press **Enter** after pasting. You should now be able to use Claude Code with Azure-deployed Claude models.

**Note:** Replace `xxxx-eastus2` with your Foundry Resource name (do not use the entire base URL). Replace `your_api_key` with your complete API key from your Azure portal.

## Step 6: Start Using Claude Code

You're all set! Here's how to use Claude Code:

1. In Terminal, type:
   ```
   claude
   ```
2. Press **Enter**
3. You can now chat with Claude!
4. To see if it works, ask a general question such as "Explain quantum computing."

## Step 7: Navigate to Your Project

1. If you have a project in your Mac folders, you can navigate to it:
   ```
   cd ~/Documents/YourProject
   ```
   Replace `YourProject` with your actual project folder name

2. Then start Claude:
   ```
   claude
   ```
3. Start by asking Claude to explain the codebase to you.
4. You can ask Claude to make changes.
5. Test your code in your preferred IDE.

## How to Open Terminal Again

After closing Terminal, here's how to open it again:

1. Press **Command (⌘) + Space** (or click on **Launchpad** from the Dock)
2. Type `Terminal`
3. Click on **Terminal**
4. The Terminal window will open

## Troubleshooting

### Node.js installer won't open
- Make sure you downloaded the `.pkg` file from nodejs.org
- Try right-clicking the file and selecting **Open** instead of double-clicking
- Go to **System Settings** > **Privacy & Security** and click **Open Anyway**

### "node: command not found" after installation
- Close Terminal completely (press **Command (⌘) + Q**)
- Open Terminal again
- Try `node --version` again
- If still not working, restart your Mac and try again

### npm installation fails with permission errors
- Use `sudo` before the npm command:
  ```
  sudo npm install -g @anthropic/claude-code
  ```
- Enter your Mac password when prompted

### Claude Code commands not found
- Make sure npm installation completed successfully
- Try closing and reopening Terminal
- Check if Claude Code is installed: `npm list -g @anthropic/claude-code`
- Try installing again: `sudo npm install -g @anthropic/claude-code`

### "Cannot find module" errors
- Make sure Node.js is properly installed: `node --version`
- Try reinstalling Claude Code: `sudo npm uninstall -g @anthropic/claude-code` then `sudo npm install -g @anthropic/claude-code`

## Tips for Mac Users

### Finding Project Paths
To find the path to a folder:
1. Open Finder
2. Navigate to your project folder
3. Drag and drop the folder into Terminal - the full path will appear!

### Keyboard Shortcuts
- **Command (⌘) + T**: Open new Terminal tab
- **Command (⌘) + N**: Open new Terminal window
- **Command (⌘) + K**: Clear Terminal screen
- **Control + C**: Stop a running command

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
