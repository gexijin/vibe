---
title: "Build Your First Dashboard with React"
---
[Home](./)

# Build Your First Dashboard with React

You built a dashboard by hand, re-picking your data file after every refresh and re-running the filter yourself. React—the tool behind much of the modern web—lets the page update itself when something changes, and a real project setup loads your data automatically. In this tutorial you'll create your first React app on Windows and rebuild your heart-attack dashboard so it reacts to you.

You'll use two programs: **PowerShell** to create and run the app, and **VS Code** to edit it.

## Key Concepts

- **React** - A tool for building web pages out of reusable pieces
- **Component** - A function that returns what to show on the screen
- **useState** - React's way to remember a value and update the screen when it changes
- **Vite** - A tool that creates and runs your React project

## What You'll Need

- A Windows computer with [VS Code](./VS_Code_Getting_Started.md) installed
- A free [ChatGPT](https://chat.openai.com) account
- *(Optional)* [GitHub Desktop](./Github_desktop.md) to save your work
- An internet connection
- 30–40 minutes

## Step 1: Install Node.js

Node.js lets your computer build and run React apps.

- Go to [nodejs.org](https://nodejs.org) and click **Get Node.js®**
- On the download page (it already picks the recommended **LTS** version), click the **Windows Installer (.msi)** button
- Open the downloaded file. Tick **I accept the terms in the License Agreement**, then click **Next** through the rest, keeping the defaults
- Click **Install** (click **Yes** if Windows asks for permission), then **Finish**

## Step 2: Open PowerShell

PowerShell is a window where you type commands instead of clicking. You'll only need a few.

- Click the **Start** button (Windows logo, bottom-left)
- Type `PowerShell`
- Click **Windows PowerShell** in the results
- A window opens with a blinking cursor—you type a command there and press **Enter**

## Step 3: Go to Your Documents Folder

Before creating the app, you'll move into your **Documents** folder—the same folder you open in File Explorer. This is where your project will be saved, so it's easy to find later.

The command below is `cd`, short for "change directory." It simply moves you into a folder, the way double-clicking a folder opens it.

- Type this and press **Enter**:
  ```
  cd ~\Documents
  ```
  (If your Documents folder is synced with OneDrive, use `cd ~\OneDrive\Documents` instead.)

You won't see much happen—that's normal. The text to the left of the blinking cursor changes to show you're now inside Documents.

## Step 4: Create Your React App

Type this command and press **Enter**:

```
npm create vite@latest heart-react -- --template react --no-interactive
```

- If it asks **Ok to proceed? (y)**, type `y` and press **Enter**
- When it finishes, it prints `Done. Now run:` followed by three commands. You'll run them in the next step.

This creates a new folder called heart-react inside Documents, with your project inside it.

## Step 5: Install and Start the App

Type these commands one at a time, pressing **Enter** after each and waiting for it to finish:

```
cd heart-react
```
```
npm install
```
```
npm run dev
```

- `npm install` downloads the pieces React needs (this takes a minute)
- After `npm run dev`, look for a line like `Local: http://localhost:5173/`
- Hold **Ctrl** and click that link, or type it into your browser
- You'll see the default React welcome page

**Leave this PowerShell window open**—it's your app's engine. Don't type anything else here.

## Step 6: Add the Data File

- In your browser, open [heart attack data](https://raw.githubusercontent.com/gexijin/learnR/master/datasets/heartatk4R.txt)
- **Right-click** the page and choose **Save as**
- In the Save window, browse into your `heart-react` folder (in Documents), then into the `public` folder inside it
- Name the file `heartatk4R.txt` and click **Save**

## Step 7: Open the Project in VS Code

- Open **VS Code**
- Click **File** → **Open Folder**
- Open your `heart-react` folder (in Documents) and click **Select Folder** (if VS Code asks whether you trust the authors, click **Yes, I trust the authors**)
- The **Explorer** on the left shows your project, including the `src` and `public` folders

## Step 8: Build the Dashboard with ChatGPT

- Go to [chat.openai.com](https://chat.openai.com) and type:
  ```
  I have a React app made with Vite. Replace App.jsx so that on load
  it fetches /heartatk4R.txt (tab-separated with a header row; columns
  Patient, DIAGNOSIS, SEX, DRG, DIED (0/1), CHARGES, LOS, AGE). Show
  total patients and average age and charges
  as cards. Ignore NA. Give me the full App.jsx.
  ```
- Copy the code
- In VS Code's **Explorer** (left side), open the `src` folder and click **App.jsx**
- Select all the old text (press **Ctrl+A**, or **Selection** → **Select All**), delete it, and paste the new code
- Click **File** → **Save**
- Look at your browser—it updates by itself with your dashboard. No refresh, no picking a file!

**Note:** Sometimes, the pasted code starts or ends with a line of three backticks (```` ``` ````), delete those lines. 

## Step 9: Add a Filter with useState

- Back in ChatGPT, type:
  ```
  Add a dropdown to filter by SEX (All, M, F) using useState that
  updates the cards. Give me the full App.jsx.
  ```
- Copy the code
- Open `App.jsx` again, select all the old text, delete it, paste the new code, and **Save**
- In your browser, choose **M** or **F**—the cards change instantly

That instant update is what React is all about: you change a value, React updates the screen for you.

## Step 10: Save Your Work with GitHub Desktop

- Open **GitHub Desktop**
- Click **File** → **Add Local Repository**
- Click **Choose...**, select your `heart-react` folder, and click **Add Repository**
- GitHub Desktop says the folder doesn't appear to be a Git repository. Click the **create a repository** link, then click **Create repository**
- GitHub Desktop saves all your files as a first commit called **Initial commit**. Click the **History** tab to see it
- Notice `node_modules` is **not** in that commit. Vite added a `.gitignore` file that tells Git to skip it
- From now on, each time you change `App.jsx`, type a commit message (for example `Add sex filter`) and click **Commit to main**

## Next Steps

- Ask ChatGPT to add a bar chart of death rate by age group
- Add an age slider that filters the dashboard, using `useState`
- Ask ChatGPT to split the dashboard into smaller components

## Troubleshooting

- **`npm` is not recognized** - Node.js isn't installed yet, or PowerShell was open before you installed it. Close PowerShell, open it again, and retry.
- **"running scripts is disabled on this system"** - Type `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` and press **Enter** (answer `Y`), then try again. Or use **Command Prompt** instead of PowerShell—the same commands work there.
- **The browser page is blank** - `App.jsx` may import a file that doesn't exist. Tell ChatGPT: "Remove any image or CSS imports so App.jsx runs on its own."
- **Cards show `NaN`** - Tell ChatGPT: "Some values are NA and some numbers have leading zeros—skip NA and convert text to numbers."
- **The page won't load (`localhost refused to connect`)** - The server stopped. Go to the PowerShell window and run `npm run dev` again.
- **Page didn't update after saving** - Make sure the PowerShell window is still running `npm run dev` and you saved `App.jsx` (**File** → **Save**).

## Workflow Overview

- In PowerShell, set up once and start the app with `npm run dev`
- Edit `App.jsx` in VS Code and save—the browser updates itself
- Ask ChatGPT for changes, paste them in, and save
- Commit working versions with GitHub Desktop
- When you're done, click the PowerShell window and press **Ctrl + C** to stop the server

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on June 20, 2026.
