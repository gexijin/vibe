[Home](./)

# Version Control with GitHub Desktop: Build a Timer App and Branch Safely

You ask an AI to build you a working app, then change one thing and the whole thing breaks—with no way back. Version control fixes this: every "commit" is a save point like in a video game, and a "branch" is a parallel copy where you can try new ideas without touching the version that works. In this hands-on tutorial you'll build a simple countdown timer with ChatGPT, save your progress with GitHub Desktop, and branch off to experiment safely.

## Key Concepts

- **Commit** - A save point that records the current state of your files
- **Branch** - A separate copy of your project where you can experiment without affecting the working version
- **main** - The default branch, where your stable, working code lives
- **Merge** - Combining the changes from a branch back into `main`

## What You'll Need

- [GitHub Desktop](https://desktop.github.com/download/) installed and signed in — see [Get Started with Version Control](./Github_desktop.md) if you haven't
- A free [ChatGPT](https://chat.openai.com) account
- A web browser (Chrome, Edge, or Safari)
- 30 minutes

## Step 1: Create a Local Repository

- Open **GitHub Desktop**
- Click **File** → **New Repository**
- Fill in the form:
  - **Name:** `timer-app`
  - **Local Path:** Choose where to save it (Documents is fine)
  - Check **Initialize this repository with a README**
- Click **Create Repository**

## Step 2: Get a Timer App from ChatGPT

- Go to [chat.openai.com](https://chat.openai.com)
- Type this prompt:
  ```
  Make a countdown timer in one HTML file. I enter minutes,
  click Start, and get an alert at zero. All code in one file.
  ```
- Click the **Copy** button on the code block ChatGPT provides

## Step 3: Save the App to Your Project

Use a plain text editor—**Notepad** on Windows or **TextEdit** on Mac. Don't use Microsoft Word.

**On Windows:**
- Open the **Start menu**, type `Notepad`, and open it
- Paste the copied code into the empty window
- Click **File** → **Save As**
- In the **Save as type** dropdown, choose **All Files**
- Name the file `index.html`
- Browse to your `timer-app` folder and click **Save**

**On Mac:**
- Open **TextEdit**
- Click **Format** → **Make Plain Text** (important—do this before pasting)
- Paste the copied code into the window
- Click **File** → **Save**
- Name the file `index.html`; if asked about the extension, click **Use .html**
- Browse to your `timer-app` folder and click **Save**

Keep this editor open—you'll come back to it.

## Step 4: Test the App in Your Browser

- In the `timer-app` folder, double-click `index.html`
- It opens in your web browser
- Enter a short time and start it to confirm it works

## Step 5: Make Your First Commit (Save Point)

- Return to **GitHub Desktop**
- You'll see `index.html` listed on the left with its changes shown on the right
- At the bottom left, type a commit message: `Add countdown timer app`
- Click the blue **Commit to main** button

## Step 6: Improve the App and Commit Again

- Go back to ChatGPT and ask for one improvement:
  ```
  Add Pause and Reset buttons. Give me the full HTML file.
  ```
- Copy the new code
- Switch to your text editor (Notepad or TextEdit) where `index.html` is open
  - If you closed it, reopen the file: in the editor click **File** → **Open**, then pick `index.html` from your `timer-app` folder
- Select all the old text (**Edit** → **Select All**), delete it, then paste the new code
- Save the file (**File** → **Save**)
- Refresh the timer in your browser to see the change (click the reload button or press **F5**)
- In GitHub Desktop, type a commit message: `Add pause and reset buttons`
- Click **Commit to main**

## Step 7: View Your History

- In GitHub Desktop, click the **History** tab (top left)
- You'll see both commits listed, newest first
- Click any commit to see exactly what changed

This is your safety net—you can always look back at how the project evolved.

## Step 8: Create a Branch to Experiment

- Click the **Current Branch** button at the top (it says **main**)
- Click **New Branch**
- Name it `new-feature`
- Click **Create Branch**

You're now working on a copy. Anything you do here won't affect `main`.

## Step 9: Add a Risky Feature on the Branch

- Ask ChatGPT for a bigger change:
  ```
  Add preset buttons for 5, 10, and 25 minutes. Give me the full HTML file.
  ```
- Copy the code
- In your text editor, open `index.html`, select all the old text, delete it, and paste the new code
- Save the file, then refresh the browser to test it
- In GitHub Desktop, commit with the message: `Add preset time buttons`
- Click **Commit to new-feature**

## Step 10: Switch Back to main and See the Difference

- Click the **Current Branch** button → select **main**
- Open `index.html` in your browser again (refresh)
- The preset buttons are **gone**—`main` is exactly as you left it

This is the magic of branches: your experiment is safely tucked away while `main` stays stable.

## Step 11: Merge Your Feature into main

If you like the new feature and want to keep it:

- Make sure you're on **main** (check the **Current Branch** button)
- Click **Branch** in the menu bar → **Merge into Current Branch**
- Select **new-feature**
- Click **Merge new-feature into main**
- Refresh the app—the preset buttons are now part of `main`

## Next Steps

- Create another branch and ask ChatGPT for a different theme (dark mode, retro look) — keep the experiments separate
- Click **Publish repository** to back up your app to GitHub in the cloud
- Try editing the file, then use **History** to compare against an earlier commit

## Troubleshooting

- **`index.html` shows raw code instead of running** - The file was saved as `index.html.txt`. In Notepad, use **File** → **Save As** with **Save as type** set to **All Files** and re-save as `index.html`.
- **Double-clicking `index.html` won't let me edit** - Double-click opens it in the browser. To edit, open your text editor first, then use **File** → **Open** to load the file.
- **Changes don't appear in GitHub Desktop** - Confirm you saved the file in your editor. Click **Repository** → **Refresh**.
- **Switching branches asks about my changes** - Commit your changes first. If GitHub Desktop prompts when switching, choose **Leave my changes on the current branch**.

## Workflow Overview

- Build or change your code (with help from ChatGPT)
- Test it in your browser
- Commit each working version as a save point on `main`
- Create a **branch** before trying something risky
- Switch back to `main` anytime to return to safe ground
- **Merge** the branch into `main` once you're happy with it

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on June 20, 2026.
