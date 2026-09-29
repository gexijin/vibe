---
title: "Workshop Prep: Windows Setup"
---
[Home](./)

# Workshop Prep: Windows Setup

You're about to attend a hands-on coding workshop. To hit the ground running, you need four tools installed and ready before the session starts. This guide walks you through each installation step by step so you can show up prepared and focus on learning, not setup.

## Tool Overview & Quick Links

Here are the four tools you'll install, with links to their official documentation:

| # | Tool | What It Does | Official Docs |
|---|------|-------------|---------------|
| 1 | **Git** | Tracks every change to your files, creating restore points | [Git Documentation](https://git-scm.com/doc) |
| 2 | **Docker Desktop** | Runs apps in isolated containers that work the same everywhere | [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/) |
| 3 | **VS Code** | A smart code editor with syntax highlighting and extensions | [VS Code](https://code.visualstudio.com/) |
| 4 | **Google Antigravity** | An AI-powered development platform with agentic coding features | [Google Antigravity](https://antigravity.google/) |

## Key Concepts

- **PowerShell** - Windows' built-in command-line tool, used throughout this guide to install and verify tools
- **Git** - Version control software that saves snapshots of your project so you can always go back to a working version
- **Docker Desktop** - An application that runs containers on your computer, packaging code and dependencies into isolated environments
- **VS Code (Visual Studio Code)** - A free code editor with built-in terminal, file explorer, and thousands of extensions
- **Google Antigravity** - Google's agentic development platform that combines a code editor with AI agents that can plan, execute, and verify tasks

## What You'll Need

- Windows 10 (version 2004 or higher) or Windows 11
- Administrator access on your computer
- Personal Gmail account (for Google Antigravity)
- Internet connection
- 30-45 minutes

**Note:** This guide uses native Windows tools throughout (PowerShell, not WSL/Ubuntu). If you prefer to work inside a Linux environment, WSL is available as an optional advanced setup — see Step 7 of [Install Claude Code on Windows](Install_CLAUDE_Code_Win.md) — but it isn't required for this workshop.

## Step 1: Install Git

Git tracks your file changes and creates restore points you can return to.

- Click the **Windows Start button**
- Type `PowerShell` and click on **Windows PowerShell**
- Check whether Git is already installed:
  ```
  git --version
  ```
- If you see a version number like `git version 2.45.0`, skip to "Configure your identity" below
- If you see an error, install Git for Windows:
  - Go to [git-scm.com/download/win](https://git-scm.com/download/win)
  - The download should start automatically — open the installer when it finishes
  - Click **Next** through the installer, accepting the default options
  - Click **Install**, then **Finish**
  - Close and reopen PowerShell, then verify again with `git --version`

**Configure your identity:**

Git needs to know who you are for commit messages.

- Set your name and email:
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

Replace `Your Name` and `your.email@example.com` with your actual name and email.

## Step 2: Install Docker Desktop

Docker runs your code in isolated containers that work the same on every machine.

- Visit the [Docker Desktop download page](https://www.docker.com/products/docker-desktop/)
- Click **Download for Windows**
- Run the downloaded installer
- Follow the installation wizard and accept the defaults (Docker Desktop manages its own Linux backend automatically)
- After installation, launch **Docker Desktop**
- Wait for the Docker engine to start (you'll see a green status indicator in the bottom left)

**Verify Docker works:**

- In PowerShell, type:
  ```
  docker --version
  ```
- You should see something like `Docker version 27.x.x`

**Note:** If Docker Desktop shows a virtualization error during setup, restart your computer, enter your BIOS settings (usually by pressing **F2**, **F10**, **Del**, or **Esc** during startup), and enable **Virtualization Technology**, **Intel VT-x**, **AMD-V**, or **SVM Mode**.

## Step 3: Install VS Code on Windows

- Go to [code.visualstudio.com](https://code.visualstudio.com)
- Click the **Download for Windows** button
- Run the downloaded `.exe` installer
- Click **Next** through the prompts and complete the installation
- Launch VS Code

## Step 4: Install Google Antigravity

Google Antigravity is an AI-powered development platform with built-in agentic coding features.

- Go to [antigravity.google/download](https://antigravity.google/download)
- Select the **Windows** version
- Run the downloaded installer and complete the installation
- Launch **Google Antigravity**

**Initial setup:**

- When asked about your setup, choose **Start fresh** (or import from VS Code if you prefer your existing settings)
- Choose your preferred editor theme (dark or light)
- For agent autonomy, select **Agent-assisted development** (recommended for beginners)
- Configure keybindings and install any language extensions you want
- When prompted, click **Sign in** - this opens your browser
- Sign in with your **personal Gmail account**
- Return to Antigravity after signing in

You should see the Antigravity editor ready to use.

## Verify Your Setup

Run through this checklist to confirm everything is working.

**Git:**
- In PowerShell, type:
  ```
  git --version
  ```
- You should see a version number

**Docker:**
- Make sure Docker Desktop is running (green indicator in the bottom left)
- In PowerShell, type:
  ```
  docker --version
  ```
- You should see a version number

**VS Code:**
- Open VS Code
- Confirm the editor launches and you can see the Explorer panel on the left

**Google Antigravity:**
- Open Google Antigravity
- Confirm you see the editor interface and are signed in

All four tools working? You're ready for the workshop!

## Troubleshooting

### Docker Desktop not starting or showing errors
- Make sure virtualization is enabled: open **Task Manager** → **Performance** → **CPU** and check if **Virtualization** says **Enabled**; if not, restart your computer, enter BIOS settings, and enable it (see Step 2 for details)
- Try restarting Docker Desktop

### `git` command not found
- Close and reopen PowerShell after installing Git for Windows so the PATH updates
- Run `git --version` again to confirm

## Need Help?

- **Git:** [Git Documentation](https://git-scm.com/doc)
- **Docker Desktop:** [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- **VS Code:** [VS Code Documentation](https://code.visualstudio.com/docs)
- **Google Antigravity:** [Google Antigravity](https://antigravity.google/)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on February 11, 2026.
