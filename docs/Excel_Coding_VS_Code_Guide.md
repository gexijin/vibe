---
title: "Use Claude Code with Excel in VS Code"
---
[Home](./)

# Use Claude Code with Excel in VS Code

You want a spreadsheet built - formulas, formatting, maybe a chart - but you don't want to fight with Excel's menus. Think of Claude Code as an assistant who knows Excel inside and out: you describe what you want in plain English, and it builds a real `.xlsx` file with working formulas. This tutorial shows you how to set up a project folder in VS Code and have Claude Code create and edit Excel spreadsheets for you.

## Key Concepts

- **xlsx skill** - Built-in Claude Code capability for creating and editing `.xlsx` spreadsheets with real formulas, formatting, and charts
- **[Excel Viewer extension](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)** - VS Code extension that lets you preview and edit spreadsheet files without leaving the editor
- **Formulas vs. hardcoded numbers** - Claude Code writes actual Excel formulas (like `=SUM(B2:B9)`) so your sheet recalculates when you change the data

## What You'll Need

- Finished [VS Code Basics](./VS_Code_Getting_Started)
- Claude Code installed and working (see [Install Claude Code on Windows](./Install_CLAUDE_Code_Win) or [Install Claude Code on Mac](./Install_Claude_Code_MacOS))
- Microsoft Excel, LibreOffice Calc, or Google Sheets to open the finished file (optional - the Excel Viewer extension works without any of these)
- 15-20 minutes

## Step 1: Install the Excel Viewer Extension in VS Code

- Open VS Code
- Click the **Extensions** icon in the left sidebar (or click **View > Extensions**)
- Search for `GrapeCity.gc-excelviewer`
- Click **Install** on **Excel Viewer** (also listed as **Spreadsheet Viewer**) by GrapeCity

This lets you double-click any `.xlsx` file and see it rendered as a spreadsheet right inside VS Code, with no need to switch to another app.

## Step 2: Create Your Project Folder

- Create a new folder on your computer (e.g., `my-excel-project`)
- In VS Code, click **File > Open Folder** and select your new folder
- Click **Select Folder** (Windows) or **Open** (Mac)

## Step 3: Start Claude Code

- Click **Terminal > New Terminal** in VS Code
- Type this command and press Enter:

```bash
claude
```

- If this is your first time, a browser window opens for authentication - log in with your Claude account
- Return to VS Code once you see Claude's welcome message in the terminal

## Step 4: Create Your First Spreadsheet

- In the Claude Code terminal, type:

```
Create a spreadsheet called budget.xlsx with columns for Category, Monthly Amount, and Notes. Add 6 example expense categories like Rent, Groceries, and Utilities with realistic amounts. Add a Total row at the bottom that sums the Monthly Amount column using a formula.
```

- Press Enter
- Watch Claude write a Python script, run it, and produce `budget.xlsx` in your project folder
- Claude also recalculates the file so the formulas show real numbers, not blank cells

## Step 5: Preview the Result

- In VS Code's Explorer panel (left side), click `budget.xlsx`
- The Excel Viewer extension opens the file as a spreadsheet
- Click the **Total** cell at the bottom - notice it's a formula, not a typed-in number
- If you have Excel or LibreOffice Calc installed, you can also double-click the file in File Explorer (Windows) or Finder (Mac) to open it there instead

## Step 6: Ask Claude to Add a Chart

- Back in the Claude Code terminal, type:

```
Add a pie chart to budget.xlsx showing each category's share of the total monthly spending.
```

- Press Enter
- Reopen `budget.xlsx` in the Excel Viewer tab (click the refresh icon, or close and reopen the file) to see the new chart

## Step 7: Edit the Data and Ask Claude to Update It

- In the Excel Viewer, or in Excel/LibreOffice if you have it open, change one of the amounts (for example, double the Rent value)
- Save the file
- In the Claude Code terminal, type:

```
I changed some numbers in budget.xlsx. Recalculate the totals and make sure the chart still matches the data.
```

- Press Enter
- Claude reads your edits, recalculates the formulas, and confirms everything lines up

This is the core workflow: describe what you want, let Claude build it, check the result, and ask for changes in plain English.

## Step 8: Ask Claude to Clean Up Messy Data

Claude Code is also useful for fixing spreadsheets that are already a mess.

- Type:

```
Create a messy_sales.csv file with 15 rows of sales data that has some issues: a few blank cells, inconsistent date formats, and one duplicate row. Then create a cleaned version called sales_clean.xlsx that fixes these problems and explain what you fixed.
```

- Press Enter
- Review the summary Claude gives you of what it found and fixed
- Open `sales_clean.xlsx` to confirm the data looks right

## Next Steps

- Ask Claude to build a spreadsheet from a CSV file you already have (drag it into your project folder first)
- Try more advanced requests: "add conditional formatting so any category over $500 turns red"
- Ask Claude to add a second sheet that summarizes data from the first sheet
- Combine this with [Use GitHub Desktop with Claude Code](./GitHub_Desktop_Claude_Code_Workflow) to save versions of your spreadsheets as you go
- Move on to [Vibe Coding a Budget Tracker in Excel](./Vibe_Coding_Excel_Guide) to build a full multi-sheet project

## Troubleshooting

- **Excel Viewer shows a blank or broken preview**: Close the tab and reopen the file. If it still fails, open the file in Excel, LibreOffice Calc, or Google Sheets instead - the file itself is fine, it's just a preview glitch.
- **Formula cells show blank instead of a number**: This usually means the file wasn't recalculated after being written. Ask Claude: "Recalculate budget.xlsx and confirm there are no formula errors."
- **Claude's changes don't show up**: Make sure you're looking at the same file Claude edited (check the filename it mentions). Close and reopen the tab in VS Code to force a refresh.
- **"claude is not recognized" in the terminal**: Claude Code isn't installed correctly. Revisit the [installation guide](./Install_CLAUDE_Code_Win) for your platform.

## Workflow Summary

- **VS Code** - Your project folder and a place to preview spreadsheets with the Excel Viewer extension
- **Claude Code** - Writes and edits real `.xlsx` files with working formulas, based on your plain-English requests
- **Excel / LibreOffice / Google Sheets** - Optional, for opening and manually tweaking the files Claude creates
- **Iterate** - Describe what you want, check the result, describe the next change

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on September 21, 2026.
