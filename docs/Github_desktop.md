# Getting Started with Version Control

This guide introduces you to Git and GitHub Desktop - tools that help you track changes to your code and never lose your work.

## Why Version Control?

Imagine you're working on a project. You make changes, and suddenly everything breaks. You can't remember what you changed. You wish you could just go back to when it was working.

**Version control is like save points in a video game.** Every time you "commit" your work, you create a save point. You can always go back to any save point if something goes wrong.

**GitHub** is like cloud storage for your save points. Your code is safely backed up online, and you can access it from any computer.

### Version Control and AI Coding

When working with AI tools like Claude Code, version control becomes even more essential:

1. **Undo AI changes easily.** Sometimes AI makes changes you don't want. With version control, you can instantly revert to how things were before - no need to manually undo each change.

2. **AI can use git to help you.** Claude Code can see your recent changes, write commit messages for you, and even commit and push on your behalf. It understands what changed and can explain it to you.

Think of it as a safety net for AI-assisted coding. You can let Claude make bold changes knowing you can always go back if needed.

## Key Concepts

Before we start, here are three terms you'll see throughout this guide:

### Git
**Git** is a version control system - software that tracks changes to your files. It runs on your computer and remembers every change you make. Git is powerful but uses command-line commands, which can be intimidating for beginners.

### GitHub
**GitHub** is a website that stores your code in the cloud. Think of it as Google Drive for code. You "push" your changes to GitHub to back them up and share them with others. GitHub is where millions of developers store and collaborate on code.

### GitHub Desktop
**GitHub Desktop** is an app that makes Git easy to use. Instead of typing commands, you click buttons. It connects to GitHub automatically and shows your changes visually. This guide uses GitHub Desktop because it's the friendliest way to learn version control.

**In short:**
- **Git** = The engine (tracks changes)
- **GitHub** = The cloud (stores your code online)
- **GitHub Desktop** = The dashboard (easy-to-use interface)

## What You'll Learn

- Create save points (commits) for your code
- Back up your code to GitHub (push)
- View the history of your changes
- Go back to an earlier version if needed

## Step 1: Create a GitHub Account

1. Open your web browser
2. Go to: https://github.com
3. Click **Sign up**
4. Enter your email, create a password, and choose a username
5. Complete the verification steps
6. You now have a GitHub account!

## Step 2: Download GitHub Desktop

1. Go to: https://desktop.github.com
2. Click the **Download** button
3. Open the downloaded file to install

**On Windows:**
- Double-click the installer file
- GitHub Desktop will install and open automatically

**On Mac:**
- Open the downloaded `.zip` file
- Drag **GitHub Desktop** to your Applications folder
- Open GitHub Desktop from Applications

## Step 3: Sign In to GitHub Desktop

1. Open GitHub Desktop
2. Click **Sign in to GitHub.com**
3. Your browser will open - click **Authorize desktop**
4. Return to GitHub Desktop
5. Click **Finish** to complete setup

## Step 4: Create Your First Repository

A **repository** (or "repo") is a project folder that tracks all your changes.

1. In GitHub Desktop, click **Create a New Repository on your Hard Drive**
2. Fill in the form:
   - **Name:** `my-first-project` (or any name you like)
   - **Description:** `Learning version control` (optional)
   - **Local Path:** Choose where to save it (Documents folder is fine)
   - Check **Initialize this repository with a README**
3. Click **Create Repository**

You've just created your first repository!

## Step 5: Open Your Project Folder

1. In GitHub Desktop, click **Show in Finder** (Mac) or **Show in Explorer** (Windows)
2. You'll see a folder with your project name
3. Inside is a file called `README.md` - this is where you describe your project

## Step 6: Make Your First Change

Let's edit the README file:

1. Open `README.md` in any text editor (Notepad, TextEdit, or VS Code)
2. Change the contents to:
   ```
   # My First Project

   I'm learning version control with GitHub Desktop.

   ## What I'm Building

   This is a practice project to learn how to:
   - Track changes to my code
   - Create save points (commits)
   - Back up my work to GitHub
   ```
3. Save the file

## Step 7: Create Your First Commit (Save Point)

Now let's save this change as a commit:

1. Go back to GitHub Desktop
2. You'll see your changes highlighted on the right side
   - Green means lines were added
   - Red means lines were removed
3. At the bottom left, you'll see a text box for your **commit message**
4. Type a short description: `Updated README with project description`
5. Click the blue **Commit to main** button

Congratulations! You just created your first save point!

## Step 8: Push to GitHub (Back Up to the Cloud)

Your commit is saved on your computer. Let's back it up to GitHub:

1. Click the blue **Publish repository** button at the top
2. Keep the name as is
3. Uncheck "Keep this code private" if you want others to see it (optional)
4. Click **Publish Repository**

Your code is now backed up to GitHub! You can see it online at:
```
https://github.com/YOUR-USERNAME/my-first-project
```

## Your Daily Workflow

Now that you're set up, here's how to use version control every day:

### 1. Make Changes
Work on your project as normal - edit files, add new files, etc.

### 2. Review Changes
Open GitHub Desktop to see what you've changed:
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

1. In GitHub Desktop, click the **History** tab
2. You'll see all your commits (save points)
3. Click any commit to see what changed

### Undo Your Last Commit

Made a mistake? If you haven't pushed yet:
1. Go to **History** tab
2. Right-click on your last commit
3. Click **Undo Commit**

### Go Back to an Earlier Version

1. Go to **History** tab
2. Find the commit you want to go back to
3. Right-click and select **Revert Changes in Commit**
4. This creates a new commit that undoes those changes

### Discard Changes You Haven't Committed

Changed something and want to undo it before committing?
1. Right-click on the file in the Changes list
2. Click **Discard Changes**
3. The file goes back to how it was in your last commit

## Working with Claude Code

Claude Code can help you with version control! Try asking:

- "What files have I changed?"
- "Write a commit message for my recent changes"
- "Explain what I changed in this file"
- "How do I undo my last change?"

When working on a project with Claude:
1. Ask Claude to make changes
2. Review the changes in GitHub Desktop
3. Commit with a descriptive message
4. Push to GitHub

## Common Questions

### How often should I commit?
Commit whenever you complete a small, logical piece of work. A good rule: if you can describe what you did in one sentence, it's a good time to commit.

### What if I forget to commit?
No problem! You can still commit later. Just review all your changes and make one commit, or organize them into multiple commits.

### What if I make a mistake?
That's the whole point of version control! You can always go back to any previous commit. Don't be afraid to experiment.

### Do I need internet to commit?
No! Commits are saved on your computer first. You only need internet when you push to GitHub.

### What's the difference between commit and push?
- **Commit** = Save locally (on your computer)
- **Push** = Upload to GitHub (in the cloud)

## Summary

You've learned to:
- Create a repository (project with version tracking)
- Make commits (save points)
- Push to GitHub (cloud backup)
- View history and undo changes

**Remember:**
1. Make changes to your code
2. Commit often with clear messages
3. Push to GitHub to back up your work

You're now using version control like a professional developer!

## Next Steps (Optional)

Once you're comfortable with the basics, you can learn about:
- **Branches:** Work on new features without affecting your main code
- **Pull Requests:** Propose changes and get feedback
- **Collaboration:** Work with others on the same project
- **Command Line Git:** Use git commands in Terminal (Claude Code can help!)

These topics are for later - master the basics first!
