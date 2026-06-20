[Home](./)

# Version Control with GitHub Desktop: Build a Data Dashboard and Branch Safely

You ask an AI to build you a working app, then change one thing and the whole thing breaks—with no way back. Version control fixes this: every "commit" is a save point like in a video game, and a "branch" is a parallel copy where you can try new ideas without touching the version that works. In this hands-on tutorial you'll build a simple dashboard from a real heart-attack dataset with ChatGPT, save your progress with GitHub Desktop, and branch off to add a chart—safely.

## Key Concepts

- **Commit** - A save point that records the current state of your files
- **Branch** - A separate copy of your project where you can experiment without affecting the working version
- **main** - The default branch, where your stable, working code lives
- **Merge** - Combining the changes from a branch back into `main`

## What You'll Need

- [GitHub Desktop](https://desktop.github.com/download/) installed and signed in — see [Get Started with Version Control](./Github_desktop.md) if you haven't
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

## Step 2: Download the Data

- Open this link in your browser: [heart attack data](https://raw.githubusercontent.com/gexijin/learnR/master/datasets/heartatk4R.txt)
- You'll see rows of hospital records—one heart-attack patient per row
- **Right-click** the page and choose **Save as** (or **Save Page As**)
- Save it into your `heart-dashboard` folder, named `heartatk4R.txt`
- *Optional:* open it in **Excel** (**File** → **Open** → pick the file → choose **Tab** as the separator) to see the columns: `SEX`, `DIED`, `CHARGES`, `LOS` (length of stay), `AGE`

## Step 3: Get the Dashboard from ChatGPT

- Go to [chat.openai.com](https://chat.openai.com)
- Type this prompt:
  ```
  Make a one-page HTML dashboard in a single file. Add a button to
  load a tab-separated .txt file from my computer. Columns: SEX,
  DIED (0 or 1), CHARGES, LOS, AGE. Show total patients, percent
  died, and average age, charges, and stay as cards. Ignore NA.
  ```
- Click the **Copy** button on the code block ChatGPT provides

## Step 4: Save the Dashboard to Your Project

Use a plain text editor—**Notepad** on Windows or **TextEdit** on Mac. Don't use Microsoft Word.

**On Windows:**
- Open the **Start menu**, type `Notepad`, and open it
- Paste the copied code into the empty window
- Click **File** → **Save As**
- In the **Save as type** dropdown, choose **All Files**
- Name the file `index.html`
- Browse to your `heart-dashboard` folder and click **Save**

**On Mac:**
- Open **TextEdit**
- Click **Format** → **Make Plain Text** (important—do this before pasting)
- Paste the copied code into the window
- Click **File** → **Save**
- Name the file `index.html`; if asked about the extension, click **Use .html**
- Browse to your `heart-dashboard` folder and click **Save**

Keep this editor open—you'll come back to it.

## Step 5: Test the Dashboard in Your Browser

- In the `heart-dashboard` folder, double-click `index.html`
- It opens in your web browser
- Click the **Choose File** button (or similar) and pick `heartatk4R.txt` from your folder
- The cards fill in with numbers from the data

**Note:** After every refresh, click the button and pick the file again—browsers can't auto-load files from your computer.

## Step 6: Make Your First Commit (Save Point)

- Return to **GitHub Desktop**
- You'll see **two** files listed on the left: `index.html` and `heartatk4R.txt`
- At the bottom left, type a commit message: `Add dashboard and data`
- Click the blue **Commit to main** button

Git now tracks both your code and your data.

## Step 7: Add a Filter and Commit Again

- Go back to ChatGPT and ask for one improvement:
  ```
  Add a dropdown to filter by SEX (All, M, F) that updates the cards.
  Give me the full HTML file.
  ```
- Copy the new code
- Switch to your text editor where `index.html` is open
  - If you closed it, reopen the file: in the editor click **File** → **Open**, then pick `index.html` from your `heart-dashboard` folder
- Select all the old text (**Edit** → **Select All**), delete it, then paste the new code
- Save the file (**File** → **Save**)
- Refresh the browser, load `heartatk4R.txt` again, and try the dropdown
- In GitHub Desktop, type a commit message: `Add sex filter`
- Click **Commit to main**

## Step 8: View Your History

- In GitHub Desktop, click the **History** tab (top left)
- You'll see your commits listed, newest first
- Click any commit to see exactly what changed—your safety net

## Step 9: Split the App into Separate Files

Separate files keep the project organized—and it's how real apps (including React) are built.

- Go back to ChatGPT and ask:
  ```
  Split this dashboard into three files: index.html, style.css,
  and app.js. Show each file in its own code block.
  ```
- ChatGPT returns three code blocks. Save each into your `heart-dashboard` folder:
  - **index.html** — open it in your editor, replace all the contents with the new `index.html` block, and save
  - **style.css** — in your editor click **File** → **New**, paste the `style.css` block, then **Save As** `style.css` (Notepad: set **Save as type** to **All Files**)
  - **app.js** — make another new file, paste the `app.js` block, then **Save As** `app.js`
- Refresh the browser and load `heartatk4R.txt`—the dashboard should look exactly the same as before
- In GitHub Desktop, you'll see `index.html` changed plus two new files (`style.css` and `app.js`)
- Type a commit message: `Split into separate files`
- Click **Commit to main**

## Step 10: Create a Branch to Experiment

- Click the **Current Branch** button at the top (it says **main**)
- Click **New Branch**
- Name it `add-chart`
- Click **Create Branch**

You're now working on a copy. Anything you do here won't affect `main`.

## Step 11: Add a Chart on the Branch

- Ask ChatGPT for a bigger change:
  ```
  Add a Chart.js bar chart (from a CDN) showing death rate by age
  group: under 50, 50-69, and 70+. My app is in index.html,
  style.css, and app.js. Give me the updated files.
  ```
- ChatGPT will return one or more updated files (likely `index.html` and `app.js`)
- For each file it gives you: open that file in your editor, replace all the contents with the new version, and save
- Refresh the browser and load `heartatk4R.txt` again to see the chart
- In GitHub Desktop, commit with the message: `Add death rate chart`
- Click **Commit to add-chart**

## Step 12: Switch Back to main and See the Difference

- Click the **Current Branch** button → select **main**
- Refresh the browser and load `heartatk4R.txt` again
- The chart is **gone**—`main` is exactly as you left it, cards and filter still working

This is the magic of branches: your experiment is safely tucked away while `main` stays stable.

## Step 13: Merge Your Chart into main

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

- **`index.html` shows raw code instead of a dashboard** - The file was saved as `index.html.txt`. In Notepad, use **File** → **Save As** with **Save as type** set to **All Files** and re-save as `index.html`.
- **Cards are empty or blank** - You need to load the data: click **Choose File** and pick `heartatk4R.txt` after every refresh.
- **Dashboard looks plain or broken after splitting files** - Make sure `style.css` and `app.js` are in the same folder as `index.html` and named exactly (not `style.css.txt`). Re-save with **Save as type** set to **All Files**.
- **Numbers show `NaN`** - Tell ChatGPT: "Some values are NA and some numbers have leading zeros—skip NA and convert text to numbers."
- **Double-clicking `index.html` won't let me edit** - Double-click opens it in the browser. To edit, open your text editor first, then use **File** → **Open** to load the file.
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
