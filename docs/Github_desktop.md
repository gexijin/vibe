---
title: "Get Started with Version Control"
---
[Home](./)

# Get Started with Version Control

You're working on a project and make changes that break everything. You can't remember what you changed, and you wish you could go back to when it worked. Version control is like save points in a video game—every time you "commit" your work, you create a restore point you can always return to. [GitHub](https://github.com) stores your save points in the cloud, so your code is safely backed up and accessible from any computer.

## Key Concepts

- **Git** - Version control software that tracks changes to your files on your computer
- **GitHub** - Website that stores your code in the cloud, like Google Drive for code
- **GitHub Desktop** - App that makes Git easy to use with buttons instead of commands
- **Repository (repo)** - A project folder that tracks all your changes

## What You'll Need

- Windows, macOS, or Linux computer
- Internet connection
- Email address for GitHub account
- 15-20 minutes

## Step 1: Create a GitHub Account

- Open your web browser
- Go to [github.com](https://github.com)
- Click **Sign up**
- Enter your email, create a password, and choose a username
- Complete the verification steps

## Step 2: Download GitHub Desktop

- Go to [desktop.github.com](https://desktop.github.com)
- Click the **Download** button
- Open the downloaded file to install

**On Windows:**
- Double-click the installer file
- GitHub Desktop installs and opens automatically

**On Mac:**
- Open the downloaded `.zip` file
- Drag **GitHub Desktop** to your Applications folder
- Open GitHub Desktop from Applications

## Step 3: Sign In to GitHub Desktop

- Open GitHub Desktop
- Click **Sign in to GitHub.com**
- Your browser opens—click **Authorize desktop**
- Return to GitHub Desktop
- Click **Finish** to complete setup

## Step 4: Create Your First Repository

- In GitHub Desktop, click **Create a New Repository on your Hard Drive**
- Fill in the form:
  - **Name:** `my-first-project` (or any name you like)
  - **Description:** `Learning version control` (optional)
  - **Local Path:** Choose where to save it (Documents folder is fine)
  - Check **Initialize this repository with a README**
- Click **Create Repository**

## Step 5: Open Your Project Folder

- In GitHub Desktop, click **Repository** in the menu bar
- Select **Show in Finder** (Mac) or **Show in Explorer** (Windows)
- You'll see a folder with your project name
- Inside is a file called `README.md`

## Step 6: Make Your First Change

- Open `README.md` in any text editor (Notepad, TextEdit, or VS Code)
- Replace the contents with:
  ```
  # My First Project

  I'm learning version control with GitHub Desktop.

  ## What I'm Building

  This is a practice project to learn how to:
  - Track changes to my code
  - Create save points (commits)
  - Back up my work to GitHub
  ```
- Click **File** → **Save**

## Step 7: Create Your First Commit (Save Point)

- Return to GitHub Desktop
- You'll see your changes highlighted on the right side (green = added, red = removed)
- At the bottom left, type a commit message: `Updated README with project description`
- Click the blue **Commit to main** button

## Step 8: Push to GitHub (Back Up to the Cloud)

- Click the blue **Publish repository** button at the top
- Keep the name as is
- Uncheck "Keep this code private" if you want others to see it (optional)
- Click **Publish Repository**

Your code is now backed up online at: `https://github.com/YOUR-USERNAME/my-first-project`

## Next Steps

- Edit your README file again and commit the changes
- Create a new file in your project folder and commit it
- Explore the **History** tab to see how your project evolves over time

## Troubleshooting

- **Can't sign in to GitHub** - Check your internet connection. Try signing in at github.com first to verify your credentials work.
- **Changes don't appear in GitHub Desktop** - Make sure you saved your files. Click **Repository** → **Refresh** or restart GitHub Desktop.
- **Push fails with "rejected" error** - Someone else pushed changes. Click **Fetch origin** first, then try pushing again.

## Workflow Overview

- Make changes to your project files
- Review changes in GitHub Desktop (green = added, red = removed)
- Write a descriptive commit message and click **Commit to main**
- Click **Push origin** to back up to GitHub
- Repeat

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
