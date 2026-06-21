[Home](./)

# Version Control with GitHub Desktop: Build a Data Dashboard

You ask an AI to build you a working app, then change one thing and the whole thing breaks—with no way back. Version control fixes this: every "commit" is a save point like in a video game, and a "branch" is a parallel copy where you can try new ideas without touching the version that works. In this hands-on tutorial you'll build a simple dashboard from a real heart-attack dataset with ChatGPT, edit it in VS Code, save your progress with GitHub Desktop, and branch off to add a chart—safely.

## Key Concepts

- **Commit** - A save point that records the current state of your files
- **Branch** - A separate copy of your project where you can experiment without affecting the working version
- **main** - The default branch, where your stable, working code lives
- **Merge** - Combining the changes from a branch back into `main`

## What You'll Need

- [GitHub Desktop](https://desktop.github.com/download/) installed and signed in — see [Get Started with Version Control](./Github_desktop.md) if you haven't
- [VS Code](https://code.visualstudio.com/) installed — see [Getting Started with VS Code](./VS_Code_Getting_Started.md) if you're new to it
- A free [ChatGPT](https://chat.openai.com) account
- A web browser (Chrome, Edge, or Safari) and an internet connection
- 30 minutes

## Step 1: Create a Local Repository

- Open **GitHub Desktop**
- Click **File** → **New Repository**
- Fill in the form:
  - **Name:** `heart-dashboard`
  - **Local Path:** Choose where to save it (Documents is fine)
  - Check **Initialize this repository with a README**
- Click **Create Repository**

## Step 2: Open the Folder in VS Code

You'll create and edit all your files in VS Code. Open your project folder once, and every file shows up in a sidebar—no hunting for files later.

- Open **VS Code**
- Click **File** → **Open Folder**
- Browse to your `heart-dashboard` folder and click **Open** (on Mac, **Select Folder**)
- If VS Code asks "Do you trust the authors?", click **Yes, I trust the authors**
- On the left you'll see the **Explorer** panel listing your folder, with the `README.md` file inside it

Keep VS Code open—you'll come back to it throughout.

## Step 3: Download the Data

- **Right-click** this link and choose **Save Link As** (or **Save Target As**): [heart attack data](https://raw.githubusercontent.com/gexijin/learnR/master/datasets/heartatk4R.txt)
- Save it into your `heart-dashboard` folder, named `heartatk4R.txt`
- Peek at the data in **Excel**: open Excel first, click **File** → **Open** → **Browse**, set the file-type dropdown to **All Files**, then pick `heartatk4R.txt` from your `heart-dashboard` folder
- Excel shows one heart-attack patient per row, with columns: `SEX`, `DIED`, `CHARGES`, `LOS` (length of stay), `AGE`
- Close Excel without saving—you only opened it to look
- Back in VS Code, `heartatk4R.txt` now appears in the Explorer panel too

## Step 4: Get the Dashboard from ChatGPT

- Go to [chat.openai.com](https://chat.openai.com)
- Type this prompt:
  ```
  Make a one-page HTML dashboard in a single file. Add a button to
  load a tab-separated .txt file from my computer. Columns: SEX,
  DIED (0 or 1), CHARGES, LOS, AGE. Show total patients, percent
  died, and average age, charges, and stay as cards. Ignore NA.
  ```
- Click the **Copy** button on the code block ChatGPT provides
- We are describing our data so that ChatGPT can write code. It's essential to get the column names exactly as they are.

**Note:** Sometimes, the pasted code starts or ends with a line of three backticks (```` ``` ````), delete those lines. 

## Step 5: Save the Dashboard to Your Project

- In VS Code, hover over the **HEART-DASHBOARD** folder name in the Explorer panel
- Click the **New File** icon that appears (or right-click the folder → **New File**)
- Type `index.html` and press **Enter**
- The empty file opens on the right—click inside it and paste the copied code (**Ctrl+V** on Windows, **Cmd+V** on Mac)
- Save the file: **Ctrl+S** (Windows) or **Cmd+S** (Mac)

Because you typed the real name `index.html`, VS Code saves it correctly—no extra steps, and the code is color-highlighted so it's easy to read.

## Step 6: Test the Dashboard in Your Browser

- In your `heart-dashboard` folder, double-click `index.html`
- It opens in your web browser
- Click the **Choose File** button (or similar) and pick `heartatk4R.txt` from your folder
- The cards fill in with numbers from the data

**Note:** After every refresh, click the button and pick the file again—browsers can't auto-load files from your computer.

## Step 7: Make Your First Commit (Save Point)

- Return to **GitHub Desktop**
- You'll see **two** files listed on the left: `index.html` and `heartatk4R.txt`
- At the bottom left, type a commit message: `Add dashboard and data`
- Click the blue **Commit to main** button

Git now tracks both your code and your data.

## Step 8: Add a Filter and Commit Again

- Go back to ChatGPT and ask for one improvement:
  ```
  Add a dropdown to filter by SEX (All, M, F) that updates the cards.
  Give me the full HTML file.
  ```
- Copy the new code
- Switch to VS Code and click `index.html` in the Explorer panel to open it
- Select all the old text (**Ctrl+A** on Windows, **Cmd+A** on Mac), then paste the new code over it
- Save the file (**Ctrl+S** or **Cmd+S**)
- Refresh the browser, load `heartatk4R.txt` again, and try the dropdown
- In GitHub Desktop, type a commit message: `Add sex filter`
- If it works, click **Commit to main**

## Step 9: View Your History

- In GitHub Desktop, click the **History** tab (top left)
- You'll see your commits listed, newest first
- Click any commit to see exactly what changed—your safety net

## Step 10: Split the App into Separate Files

Separate files keep the project organized—and it's how real apps (including React) are built.

- Go back to ChatGPT and ask:
  ```
  Split this dashboard into multiple files. 
  ```
- ChatGPT returns three code blocks. Save each into your `heart-dashboard` folder using VS Code:
  - **index.html** — click it in the Explorer, select all (**Ctrl+A**/**Cmd+A**), paste the new `index.html` block over it, and save
  - **style.css** — hover the folder name, click the **New File** icon, type `style.css`, paste the `style.css` block, and save
  - **app.js** — click **New File** again, type `app.js`, paste the `app.js` block, and save
- Refresh the browser and load `heartatk4R.txt`—the dashboard should look exactly the same as before
- In GitHub Desktop, you'll see `index.html` changed plus two new files (`style.css` and `app.js`)
- Type a commit message: `Split into separate files`
- Click **Commit to main**

## Step 11: Create a Branch to Experiment

- Click the **Current Branch** button at the top (it says **main**)
- Click **New Branch**
- Name it `add-chart`
- Click **Create Branch**

You're now working on a copy. Anything you do here won't affect `main`.

## Step 12: Add a Chart on the Branch

- Ask ChatGPT for a bigger change:
  ```
  Add a Chart.js bar chart (from a CDN) showing death rate by age
  group: under 50, 50-69, and 70+. Give me the updated files.
  ```
- ChatGPT will return one or more updated files (likely `index.html` and `app.js`)
- For each file it gives you: click that file in VS Code's Explorer, select all (**Ctrl+A**/**Cmd+A**), paste the new version over it, and save
- Refresh the browser and load `heartatk4R.txt` again to see the chart
- In GitHub Desktop, commit with the message: `Add death rate chart`
- Click **Commit to add-chart**

## Step 13: Switch Back to main and See the Difference

- Click the **Current Branch** button → select **main**
- Look at VS Code—the files change back automatically
- Refresh the browser and load `heartatk4R.txt` again
- The chart is **gone**—`main` is exactly as you left it, cards and filter still working

This is the magic of branches: your experiment is safely tucked away while `main` stays stable.

## Step 14: Merge Your Chart into main

If you like the chart and want to keep it:

- Make sure you're on **main** (check the **Current Branch** button)
- Click **Branch** in the menu bar → **Merge into Current Branch**
- Select **add-chart**
- Click **Merge add-chart into main**
- Refresh the browser and load the data—the chart is now part of `main`

## Next Steps

- Create another branch and ask ChatGPT for a different chart (average charges by sex) — keep the experiments separate
- Add an age slider that filters the dashboard, on its own branch
- Click **Publish repository** to back up your dashboard to GitHub in the cloud

## Troubleshooting

- **I don't see my files in VS Code** - Make sure you opened the *folder*, not a single file: **File** → **Open Folder** → pick `heart-dashboard`. The Explorer panel should show the folder name with your files inside.
- **Cards are empty or blank** - You need to load the data: click **Choose File** and pick `heartatk4R.txt` after every refresh.
- **Dashboard looks plain or broken after splitting files** - Make sure `style.css` and `app.js` are in the same folder as `index.html`, named exactly, and that you saved all three (an unsaved file shows a dot ● next to its name in the VS Code tab).
- **Numbers show `NaN`** - Tell ChatGPT: "Some values are NA and some numbers have leading zeros—skip NA and convert text to numbers."
- **Double-clicking `index.html` opens the browser, not the editor** - That's expected—double-click is for testing. To edit, click the file in VS Code's Explorer panel instead.
- **Switching branches asks about my changes** - Commit your changes first. If GitHub Desktop prompts when switching, choose **Leave my changes on the current branch**.

## Workflow Overview

- Build or change your code (with help from ChatGPT)
- Edit and save the files in VS Code
- Test it in your browser
- Commit each working version as a save point on `main`
- Create a **branch** before trying something risky
- Switch back to `main` anytime to return to safe ground
- **Merge** the branch into `main` once you're happy with it

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on June 20, 2026.
