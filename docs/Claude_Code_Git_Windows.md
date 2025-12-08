[Home](./)

# Claude Code with local version control for Windows

You're coding with AI assistance. It makes changes to your files. Sometimes the changes work perfectly. Sometimes they don't. **Version control is like an undo button for your entire project.** Every time you save a snapshot (called a "commit"), you create a restore point you can always go back to. Best of all, you can do this entirely on your computer—no account, no cloud, just local safety nets.

## Key Concepts

- **WSL (Windows Subsystem for Linux)** - Runs Linux tools like Git natively on Windows
- **Git** - Tracks every change to your files on your computer, creating restore points you can return to anytime
- **Commit** - A snapshot of your project at a specific point in time with a description of what changed
- **Claude Code** - AI coding assistant that writes code, fixes bugs, and handles Git operations through simple requests

## What You'll Need

- Windows 10 or 11 with WSL installed ([installation guide](https://learn.microsoft.com/en-us/windows/wsl/install))
- Ubuntu running in WSL
- Claude Code installed ([installation guide](https://code.claude.com/docs/en/installation))
- 20 minutes

## Step 1: Open Ubuntu Terminal

- Click the **Start** menu
- Type `Ubuntu`
- Click **Ubuntu** to open the terminal

You'll see a command prompt ending with `$`.

## Step 2: Install Git

- Type this command and press Enter:
  ```
  sudo apt-get install git
  ```
- When prompted, type your password and press Enter
- Wait for installation to complete (10-30 seconds)
- Verify Git is installed:
  ```
  git --version
  ```

You should see something like `git version 2.34.1`.

## Step 3: Configure Git with Your Identity

Git needs to know who you are for commit messages.

- Set your name and email (can be fake)
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

Using your name and email helps you identify who made changes when multiple persons work on this.

## Step 4: Navigate to a Windows Folder

WSL can access your Windows files through `/mnt/c/`.

- Navigate to your Windows user folder:
  ```
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  ```
  Replace `YOUR_USERNAME` with your actual Windows username.
- Verify you're in the right place:
  ```
  pwd
  ```

You should see `/mnt/c/Users/YOUR_USERNAME/Documents`.

## Step 5: Create Project Folder

- Create a folder called `timer`:
  ```
  mkdir timer
  ```
- Navigate into it:
  ```
  cd timer
  ```

This is where your project will live.

## Step 6: Start Claude Code

- Start Claude Code:
  ```
  claude
  ```

Claude Code launches and waits for your request.

## Step 7: Ask Claude to Initialize Git

- Type this request:
  ```
  Start tracking changes
  ```

Claude initializes a Git repository in your folder (takes 2-5 seconds). You now have version control!

## Step 8: Build the Timer App

- In Claude Code, type:
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  ```

Claude creates `timer.html` (takes 10-30 seconds) with the CSS and JavaScript code.

## Step 9: Test the Timer

- Open Windows File Explorer
- Navigate to `Documents\timer`
- Double-click `timer.html` to open it in your browser
- Try the timer:
  - Type `1` in the input field
  - Click **Start**
  - Watch the countdown

**If something's broken:** In Claude Code, describe the error: `I'm seeing this error: [describe what happened]. Can you fix it?`

## Step 10: Ask Claude to Commit

- In Claude Code, type:
  ```
  Save these changes.
  ```

Claude will:
- Check what files changed
- Write a descriptive commit message
- Create the commit (takes 5-10 seconds)

You've created your first save point! You can always return to this working version.

## Step 11: Add Preset Buttons

- In Claude Code, type:
  ```
  Add two buttons on the top. If I click on them it automatically starts 1- and 5-minute timers.
  ```
- Refresh your browser tab (or press `F5`)
- Test: Click the **5 min** button
- If it works, commit the changes:
  ```
  Save these changes.
  ```

We created a 2nd save point. This version has the two buttons working.


## Step 12: Add Another Button

- In Claude Code, type:
  ```
  Add a 15-minute button.
  ```
- Refresh your browser tab (press `F5`)
- Test: Click the **15 min** button

**For this tutorial:** Pretend the 15-minute button doesn't work correctly. Don't commit yet—we'll practice discarding bad changes.

## Step 13: Discard Changes

Sometimes AI code doesn't work and you need to start over from your last save point.

- In Claude Code, type:
  ```
  discard these changes.
  ```
- Claude will ask for confirmation
- Type `yes` and press Enter
- Refresh your browser—the 15-minute button disappears

Claude throws away the new changes we don't like. The timer works again with just the 1- and 5-minute buttons!

## Step 14: Add Sound Notification

- In Claude Code, type:
  ```
  Add a sound notification when the timer reaches zero.
  ```
- Refresh browser and test after Claude is done (set timer for 0.1 minutes)
- If it works, commit the changes:
  ```
  Save these changes.
  ```

## Step 15: Add snooze button

- In Claude Code, type:
  ```
  The sound should continue until I click a button to snooze it. 
  ```
- Refresh browser and test after Claude is done (set timer for 0.1 minutes)
- If it works, commit the changes:
  ```
  Save these changes.
  ```
## Step 16: View Your Commit History

- In Claude Code, type:
  ```
  show my change history
  ```

Claude displays your commits in a readable format. You'll see:
- Your initial timer app commit
- The preset buttons (1-min and 5-min) commit
- The sound notification commit
- The snooze button.

Notice the 15-minute button attempt isn't there—you discarded it!

## Step 17: Examine the code

- In the browser that shows the app, right click and select **View Page Source**
- You can see the source code for this. 
- In Claude Code, ask
  ```
  Explain this code. Just big picture.
  ```

## The Complete Workflow

- Ask Claude to make changes
- Test 
- If it works → Ask Claude to commit
- If it fails → Ask Claude to fix it. 
- Unable to fix → Discard changes and try again
- Repeat

You can always return to any commit. Discard fearlessly—only commit working code!

## Next Steps

Try adding more features to your timer:

- **15-minute button:** `Add a working 15-minute preset button` (redo what we discarded!)
- **Pause button:** `Add a Pause/Resume button that toggles the timer state`
- **Better styling:** `Improve the visual design with a modern color scheme and larger fonts`
- **Progress bar:** `Add a visual progress bar showing time remaining`

Remember: Test after each feature, commit after each success, discard failures.

## Troubleshooting

- **"not a git repository" error:** Make sure you're in the timer folder (`cd /mnt/c/Users/YOUR_USERNAME/Documents/timer`)
- **Can't find timer.html in Windows:** The file is at `C:\Users\YOUR_USERNAME\Documents\timer\timer.html`
- **Git asks for password:** You mistyped the `sudo` password—try again carefully
- **Timer doesn't work:** Open browser console (press `F12`, click **Console** tab), copy any red error messages, paste them to Claude

## What You Can Ask Claude

- `what files have I changed?` - See uncommitted changes
- `show me the diff` - See exactly what code changed
- `explain what the timer code does` - Understand the implementation
- `create a branch called experiment` - Try risky changes safely
- `go back to the previous commit` - Undo everything since last commit

Claude handles all Git operations through natural language—no commands to memorize!

## Workflow Overview

- **Setup:** Install Git once, configure identity once
- **Development:** Claude writes code, you test in browser
- **Version Control:** Claude handles all Git operations via simple requests
- **Safety:** Discard bad changes anytime, return to any previous commit
- **Local:** Everything stays on your computer, no account or internet required

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 8, 2025.
