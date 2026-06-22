---
title: "Workshop Prep: Linux Setup (Ubuntu)"
---
[Home](./)

# Workshop Prep: Linux Setup (Ubuntu)

You're about to attend a hands-on coding workshop. To hit the ground running, you need four tools installed and ready before the session starts. Since you're already on Linux, there's no need for WSL or virtualization — you can install everything natively. This guide walks you through each step so you can show up prepared and focus on learning, not setup.

## Tool Overview & Quick Links

Here are the four tools you'll install, with links to their official documentation:

| # | Tool | What It Does | Official Docs |
|---|------|-------------|---------------|
| 1 | **Git** | Tracks every change to your files, creating restore points | [Git Documentation](https://git-scm.com/doc) |
| 2 | **Docker Desktop** | Runs apps in isolated containers that work the same everywhere | [Docker Desktop for Ubuntu](https://docs.docker.com/desktop/setup/install/linux/ubuntu/) |
| 3 | **VS Code** | A smart code editor with syntax highlighting and extensions | [VS Code](https://code.visualstudio.com/) |
| 4 | **Google Antigravity** | An AI-powered development platform with agentic coding features | [Google Antigravity](https://antigravity.google/) |

## Key Concepts

- **Git** - Version control software that saves snapshots of your project so you can always go back to a working version
- **Docker Desktop** - An application that runs containers on your computer, packaging code and dependencies into isolated environments
- **VS Code (Visual Studio Code)** - A free code editor with built-in terminal, file explorer, and thousands of extensions
- **Google Antigravity** - Google's agentic development platform that combines a code editor with AI agents that can plan, execute, and verify tasks

## What You'll Need

- Ubuntu 22.04 LTS or newer (or compatible Debian-based distro)
- sudo access on your computer
- Personal Gmail account (for Google Antigravity)
- Internet connection
- 20-30 minutes

## Step 1: Update System and Install Git

Git tracks your file changes and creates restore points you can return to.

**Open a terminal:**

- Press **Ctrl+Alt+T** or open **Terminal** from the app menu

**Update packages and install Git:**

- Type the following command and press Enter:
  ```
  sudo apt-get update && sudo apt-get install git
  ```
- Type your password when prompted and press Enter
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

## Step 2: Install Docker Desktop

Docker runs your code in isolated containers that work the same on every machine.

**Install prerequisites:**

- In your terminal, run:
  ```
  sudo apt-get install ca-certificates curl gnupg
  ```

**Add Docker's official GPG key and repository:**

- Run these commands one at a time:
  ```
  sudo install -m 0755 -d /etc/apt/keyrings
  ```
  ```
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  ```
  ```
  sudo chmod a+r /etc/apt/keyrings/docker.gpg
  ```
  ```
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

**Install Docker Desktop:**

- Update the package list and install:
  ```
  sudo apt-get update
  ```
  ```
  sudo apt-get install docker-desktop
  ```
- Launch **Docker Desktop** from the app menu
- Wait for the Docker engine to start (you'll see a green status indicator in the bottom left)

**Add your user to the docker group:**

This lets you run Docker commands without `sudo`.

- Run:
  ```
  sudo usermod -aG docker $USER
  ```
- Log out and log back in for the change to take effect

**Verify Docker is working:**

- Open a new terminal and type:
  ```
  docker --version
  ```
- You should see something like `Docker version 27.x.x`

## Step 3: Install VS Code

VS Code is a code editor with built-in terminal, extensions, and language support.

**Option A: Download the .deb package (recommended)**

- Go to [code.visualstudio.com](https://code.visualstudio.com)
- Click **Download for Linux (.deb)**
- Open a terminal and navigate to your Downloads folder:
  ```
  cd ~/Downloads
  ```
- Install the package:
  ```
  sudo dpkg -i code_*.deb
  ```
- If you see dependency errors, fix them with:
  ```
  sudo apt-get install -f
  ```

**Option B: Install via snap**

- Run:
  ```
  sudo snap install code --classic
  ```

**Launch VS Code:**

- Open VS Code from the app menu or type `code` in the terminal

No WSL extension needed — you're already running native Linux.

## Step 4: Install Google Antigravity

Google Antigravity is an AI-powered development platform with built-in agentic coding features.

- Go to [antigravity.google/download](https://antigravity.google/download)
- Select the **Linux** version
- Download the `.deb` package
- Open a terminal and navigate to your Downloads folder:
  ```
  cd ~/Downloads
  ```
- Install the package:
  ```
  sudo dpkg -i google-antigravity_*.deb
  ```
- If you see dependency errors, fix them with:
  ```
  sudo apt-get install -f
  ```
- Launch **Google Antigravity** from the app menu

**Initial setup:**

- When asked about your setup, choose **Start fresh** (or import from VS Code if you prefer your existing settings)
- Choose your preferred editor theme (dark or light)
- For agent autonomy, select **Agent-assisted development** (recommended for beginners)
- Configure keybindings and install any language extensions you want
- When prompted, click **Sign in** — this opens your browser
- Sign in with your **personal Gmail account**
- Return to Antigravity after signing in

You should see the Antigravity editor ready to use.

## Verify Your Setup

Run through this checklist to confirm everything is working.

**Git:**
- Open a terminal and type:
  ```
  git --version
  ```
- You should see a version number

**Docker:**
- Make sure Docker Desktop is running (green indicator in the bottom left)
- In the terminal, type:
  ```
  docker --version
  ```
- You should see a version number

**VS Code:**
- In the terminal, type:
  ```
  code --version
  ```
- You should see a version number

**Google Antigravity:**
- Open Google Antigravity from the app menu
- Confirm you see the editor interface and are signed in

All four tools working? You're ready for the workshop!

## Troubleshooting

### dpkg dependency errors during installation
- Run `sudo apt-get install -f` to automatically install missing dependencies
- Then retry the `dpkg -i` command

### Docker permission denied
- Make sure you added your user to the docker group:
  ```
  sudo usermod -aG docker $USER
  ```
- Log out and log back in for the change to take effect
- Try running `docker --version` again in a new terminal

### VS Code not launching or showing errors
- Install any missing dependencies:
  ```
  sudo apt-get install -f
  ```
- If installed via .deb, try reinstalling:
  ```
  sudo dpkg -i code_*.deb && sudo apt-get install -f
  ```

## Need Help?

- **Git:** [Git Documentation](https://git-scm.com/doc)
- **Docker Desktop:** [Docker Desktop for Ubuntu](https://docs.docker.com/desktop/setup/install/linux/ubuntu/)
- **VS Code:** [VS Code Documentation](https://code.visualstudio.com/docs)
- **Google Antigravity:** [Google Antigravity](https://antigravity.google/)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on February 11, 2026.
