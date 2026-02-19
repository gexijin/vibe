[Home](./)

# Install Claude Code on Mac

Claude Code is an AI assistant that lives in your Terminal and helps you write, debug, and understand code. Think of it as having a knowledgeable coding partner available whenever you need help. Whether you're a complete beginner or an experienced developer, Claude Code can accelerate your workflow and help you learn.

This guide walks you through installation step by step, with detailed instructions for beginners.

## Overview

- Open Terminal
- Install Claude Code
- Configure your API connection
- Start using Claude Code

## Key Concepts

- **Terminal**: A built-in Mac app where you type commands instead of clicking buttons. It's how you'll interact with Claude Code.
- **Claude Code**: An AI coding assistant you run in Terminal. It can answer questions, write code, and help you understand existing projects.

## What You'll Need

- A Mac computer (macOS 13.0 Ventura or newer)
- Internet connection
- Administrator access on your computer
- Claude Pro/Max subscription or API key
- 5 - 10 minutes

## Step 1: Open Terminal

- Click the **Launchpad** icon in your Dock (the icon with colorful squares)
- Type `Terminal` in the search box at the top
- Click on **Terminal** (a black square icon)
- A Terminal window will open with a blinking cursor

**Tip:** Keep Terminal open for the next steps.

## Step 2: Install Claude Code

In Terminal, copy and paste this command, then press **Return**:
```
curl -fsSL https://claude.ai/install.sh | bash
```

- Wait for Claude Code to install (1-2 minutes)
- You may see some progress messages - this is normal
- When installation is complete, close and reopen Terminal, then verify by typing:
   ```
   claude --version
   ```
- You should see the version number of Claude Code

**Alternative: Install with Homebrew**

If you use Homebrew, you can install Claude Code with:
```
brew install --cask claude-code
```

**Tip:** Run `claude doctor` after installation to check that everything is set up correctly.

## Step 3: Connect to Your Anthropic Account

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

## Step 4: Test Claude Code

You're all set! Here's how to use Claude Code:

- In Terminal, type:
   ```
   claude
   ```
- It asks you a few questions before getting ready to chat
- To see if it works, ask a general question such as "Explain quantum computing."

## Step 5: Navigate to Your Project

- If you have a project in your Mac folders, you can navigate to it:
   ```
   cd ~/Documents/test_claude
   ```
   Replace `test_claude` with your actual project folder name

- Then start Claude:
   ```
   claude
   ```
- Start by asking Claude to explain the codebase to you.
- You can ask Claude to make changes.
- Test your code in your preferred IDE.

**Note:** Claude operates inside a project folder. It defines writing permissions in the folder and saves settings in that folder. It's Claude's workspace.

## Step 6: Update Claude Code

Claude Code installed via the native installer automatically updates itself in the background. You can also manually trigger an update:

- In Terminal, type:
   ```
   sudo claude
   ```
- Claude Code will check for updates and install the latest version

**Note:** Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest version.

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

### First step: Run Claude Doctor
If something isn't working, run this command first:
```
claude doctor
```
It checks your installation and reports any issues.

### Installation script fails
- Make sure you have macOS 13.0 or newer
- Try the Homebrew alternative: `brew install --cask claude-code`
- Check your internet connection and try again

### Claude Code commands not found
- Close Terminal completely (click **Terminal** in the menu bar, then **Quit Terminal**)
- Open Terminal again
- Try `claude --version` to check if it's installed
- Try running the installation command again: `curl -fsSL https://claude.ai/install.sh | bash`

### Authentication fails
- Make sure you have an active Claude Pro/Max subscription or valid API key
- Try running `claude` again and complete the login process
- Check that your browser opened the correct authorization page

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

- For Claude Code issues: [Claude Code GitHub](https://github.com/anthropics/claude-code)
- For official setup docs: [Claude Code Setup Guide](https://code.claude.com/docs/en/setup)

---

*Last updated: February 2026*
