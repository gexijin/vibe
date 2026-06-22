---
title: "Workshop Prep: Windows Setup"
---
[Home](./)

# Workshop Prep: Windows Setup

You're about to attend a hands-on coding workshop. To hit the ground running, you need five tools installed and ready before the session starts. This guide walks you through each installation step by step so you can show up prepared and focus on learning, not setup.

## Tool Overview & Quick Links

Here are the five tools you'll install, with links to their official documentation:

| # | Tool | What It Does | Official Docs |
|---|------|-------------|---------------|
| 1 | **WSL** | Runs a Linux environment inside Windows | [Microsoft WSL Docs](https://learn.microsoft.com/en-us/windows/wsl/) |
| 2 | **Git** | Tracks every change to your files, creating restore points | [Git Documentation](https://git-scm.com/doc) |
| 3 | **Docker Desktop** | Runs apps in isolated containers that work the same everywhere | [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/) |
| 4 | **VS Code** | A smart code editor with syntax highlighting and extensions | [VS Code](https://code.visualstudio.com/) |
| 5 | **Google Antigravity** | An AI-powered development platform with agentic coding features | [Google Antigravity](https://antigravity.google/) |

## Key Concepts

- **WSL (Windows Subsystem for Linux)** - A Windows feature that runs a real Linux system alongside Windows, giving you access to Linux tools like Git
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

## Step 1: Install WSL and Ubuntu

WSL lets you run Linux tools natively on Windows. Several of the other tools depend on it.

**Check if virtualization is enabled:**

- **Right-click** on the taskbar (the bar at the bottom of your screen)
- Click on **Task Manager**
- If Task Manager opens in a small window, click **More details** at the bottom
- Click on the **Performance** tab at the top
- Click on **CPU** in the left sidebar
- Look for the line that says **Virtualization:** and check if it says **Enabled**

**If it says "Disabled":** You need to enable virtualization in your BIOS:
- Restart your computer
- During startup, press the BIOS key (usually **F2**, **F10**, **Del**, or **Esc** depending on your manufacturer)
- Look for "Virtualization Technology", "Intel VT-x", "AMD-V", or "SVM Mode"
- Enable the setting, save, and exit (usually **F10**)

**Install WSL:**

- Click the **Windows Start button**
- Type `PowerShell` in the search box
- **Right-click** on **Windows PowerShell** and click **Run as administrator**
- Click **Yes** when asked to allow changes
- Type this command and press Enter:
  ```
  wsl --install
  ```
- Wait for the installation to complete
- Restart your computer when prompted

**Set up Ubuntu:**

After restarting, an Ubuntu terminal window should open automatically within a few minutes.

- If it doesn't open, click the **Start** menu, type `Ubuntu`, and click the **Ubuntu** app
- When prompted, type a username (lowercase letters and numbers only, no spaces)
- Type a simple password (you won't see characters as you type - this is normal)
- Re-enter the password when prompted

**Important:** Remember this username and password.

## Step 2: Install Git in WSL

Git tracks your file changes and creates restore points you can return to.

- Click the **Start** menu, type `Ubuntu`, and click **Ubuntu** to open the terminal
- Update the package list and install Git:
  ```
  sudo apt-get update && sudo apt-get install git
  ```
- Type your Ubuntu password when prompted and press Enter
- Wait for the installation to complete (10-30 seconds)
- Verify Git is installed:
  ```
  git --version
  ```
- You should see something like `git version 2.34.1`

**Configure your identity:**

Git needs to know who you are for commit messages.

- Set your name and email:
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

Replace `Your Name` and `your.email@example.com` with your actual name and email.

## Step 3: Install Docker Desktop

Docker runs your code in isolated containers that work the same on every machine.

- Visit the [Docker Desktop download page](https://www.docker.com/products/docker-desktop/)
- Click **Download for Windows**
- Run the downloaded installer
- When prompted, make sure **Use WSL 2 instead of Hyper-V** is checked
- Follow the installation wizard and accept the defaults
- After installation, launch **Docker Desktop**
- Wait for the Docker engine to start (you'll see a green status indicator in the bottom left)

**Verify Docker works in WSL:**

- Open the Ubuntu terminal (Start menu → type `Ubuntu`)
- Type:
  ```
  docker --version
  ```
- You should see something like `Docker version 27.x.x`

**Note:** If you see an error, open Docker Desktop settings, go to **Resources** → **WSL Integration**, and make sure your Ubuntu distribution is enabled.

## Step 4: Install VS Code on Windows

VS Code is a code editor that connects to your WSL environment for a seamless workflow.

- Go to [code.visualstudio.com](https://code.visualstudio.com)
- Click the **Download for Windows** button
- Run the downloaded `.exe` installer
- Click **Next** through the prompts and complete the installation
- Launch VS Code

**Install the WSL extension:**

- In VS Code, click the **Extensions** icon in the left sidebar (the squares icon)
- Type `WSL` in the search box
- Find **WSL** by Microsoft
- Click **Install**

This extension lets VS Code connect directly to your WSL Ubuntu environment.

## Step 5: Install Google Antigravity

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

**WSL and Ubuntu:**
- Open the Start menu, type `Ubuntu`, and click to open the terminal
- You should see a command prompt ending with `$`

**Git:**
- In the Ubuntu terminal, type:
  ```
  git --version
  ```
- You should see a version number

**Docker:**
- Make sure Docker Desktop is running (green indicator in the bottom left)
- In the Ubuntu terminal, type:
  ```
  docker --version
  ```
- You should see a version number

**VS Code:**
- Open VS Code
- Click the green icon in the bottom-left corner
- Select **Connect to WSL** from the menu
- A new window opens connected to your Ubuntu environment

**Google Antigravity:**
- Open Google Antigravity
- Confirm you see the editor interface and are signed in

All five tools working? You're ready for the workshop!

## Troubleshooting

### Virtualization not enabled
- Open **Task Manager** → **Performance** → **CPU** and check if **Virtualization** says **Enabled**
- If disabled, restart your computer and enter BIOS settings to enable it (see Step 1 for details)

### WSL install fails or command not recognized
- Make sure you're running PowerShell **as Administrator**
- Make sure you have Windows 10 version 2004 or higher, or Windows 11
- Try running `wsl --update` first, then `wsl --install` again

### Docker Desktop not starting or showing errors
- Make sure virtualization is enabled (see above)
- Make sure WSL is installed and working first
- Open Docker Desktop settings → **Resources** → **WSL Integration** and enable your Ubuntu distribution
- Try restarting Docker Desktop

## Need Help?

- **WSL:** [Microsoft WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
- **Git:** [Git Documentation](https://git-scm.com/doc)
- **Docker Desktop:** [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- **VS Code:** [VS Code Documentation](https://code.visualstudio.com/docs)
- **Google Antigravity:** [Google Antigravity](https://antigravity.google/)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on February 11, 2026.
