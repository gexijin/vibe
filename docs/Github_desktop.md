[Home](./)

# Getting Started with Version Control

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

You just created your first save point!

## Step 8: Push to GitHub (Back Up to the Cloud)

- Click the blue **Publish repository** button at the top
- Keep the name as is
- Uncheck "Keep this code private" if you want others to see it (optional)
- Click **Publish Repository**

Your code is now backed up online at: `https://github.com/YOUR-USERNAME/my-first-project`

## Your Daily Workflow

### 1. Make Changes
Work on your project—edit files, add new files, etc.

### 2. Review Changes
Open GitHub Desktop to see what changed:
- Changed files appear in the left panel
- Specific changes appear on the right (green = added, red = removed)

### 3. Commit Your Changes
Write a short message describing what you did:
- **Good messages:** "Added login button", "Fixed spelling error in header"
- **Bad messages:** "Updated stuff", "Changes"

Click **Commit to main**.

### 4. Push to GitHub
Click **Push origin** to back up your commits to GitHub.

**Tip:** Commit often! Small, frequent commits are better than one giant commit.

## Useful Tasks

### View Your History
- In GitHub Desktop, click the **History** tab
- You'll see all your commits (save points)
- Click any commit to see what changed

### Undo Your Last Commit
If you haven't pushed yet:
- Go to **History** tab
- Right-click on your last commit
- Click **Undo Commit**

### Go Back to an Earlier Version
- Go to **History** tab
- Find the commit you want to go back to
- Right-click and select **Revert Changes in Commit**
- This creates a new commit that undoes those changes

### Discard Changes You Haven't Committed
- Right-click on the file in the Changes list
- Click **Discard Changes**
- The file returns to how it was in your last commit

## Working with Claude Code

Claude Code can help you with version control:
- "What files have I changed?"
- "Write a commit message for my recent changes"
- "Explain what I changed in this file"
- "How do I undo my last change?"

When working on a project with Claude:
- Ask Claude to make changes
- Review the changes in GitHub Desktop
- Commit with a descriptive message
- Push to GitHub

## Next Steps

- Try editing your README file again and committing the changes
- Create a new file in your project folder and commit it
- Explore the History tab to see how your project evolves over time

## Troubleshooting

- **Can't sign in to GitHub** - Check your internet connection. Try signing in at github.com first to verify your credentials work.
- **Changes don't appear in GitHub Desktop** - Make sure you saved your files. Click **Repository** → **Refresh** or restart GitHub Desktop.
- **Push fails with "rejected" error** - Someone else pushed changes. Click **Fetch origin** first, then try pushing again.

## Common Questions

**How often should I commit?**
Commit whenever you complete a small, logical piece of work. If you can describe what you did in one sentence, it's a good time to commit.

**What if I forget to commit?**
No problem! You can still commit later. Review all your changes and make one commit, or organize them into multiple commits.

**What if I make a mistake?**
That's the point of version control! You can always go back to any previous commit.

**Do I need internet to commit?**
No! Commits are saved on your computer first. You only need internet when you push to GitHub.

**What's the difference between commit and push?**
- **Commit** = Save locally (on your computer)
- **Push** = Upload to GitHub (in the cloud)

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
