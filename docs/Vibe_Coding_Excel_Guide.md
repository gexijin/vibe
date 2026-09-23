---
title: "Vibe Coding a Budget Tracker in Excel with Claude Code"
---
[Home](./)

# Vibe Coding a Budget Tracker in Excel with Claude Code

Vibe coding is like having a conversation with your computer - you describe the outcome, Claude Code builds it, you test and refine. It's not magic; it's a new way to work where you guide the vision and AI handles the spreadsheet mechanics: formulas, formatting, and charts. This tutorial walks you through building a real multi-sheet budget tracker using nothing but natural language requests.

## Key Concepts

- **[Claude Code](https://code.claude.com/)** - AI coding assistant that writes, edits, and fixes files based on your natural language requests
- **Multi-sheet workbook** - A single `.xlsx` file with several tabs (Income, Expenses, Summary) that reference each other with formulas
- **Iterative refinement** - The core vibe coding pattern: describe → test → refine → commit working versions

## What You'll Need

- Finished [Use Claude Code with Excel in VS Code](./Excel_Coding_VS_Code_Guide)
- Finished [Use GitHub Desktop with Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 25-30 minutes

## Step 1: Create New GitHub Repository

- Open GitHub Desktop
- Click **File > New Repository**
- Fill in the details:
  - **Name:** `budget-dashboard`
  - **Description:** `Personal budget tracker built with vibe coding`
  - **Local Path:** Choose a location (e.g., Documents or work folder)
  - Check **Initialize this repository with a README**
- Click **Create Repository**
- Click **Publish repository** at the top
- Uncheck **Keep this code private** if you want it public (optional)
- Click **Publish Repository**

You now have a local Git repository and a backup on GitHub.

## Step 2: Open the Project in VS Code

- Open VS Code
- Click **File > Open Folder**
- Select your `budget-dashboard` folder
- Click **Select Folder** (Windows) or **Open** (Mac)
- If you haven't already, install the **Excel Viewer** extension (`GrapeCity.gc-excelviewer`) so you can preview spreadsheets without leaving VS Code

## Step 3: Start Claude Code

- Click **Terminal > New Terminal**
- Type this command to start Claude Code:

```bash
claude
```

- Log in if prompted, then wait for Claude's welcome message

Claude Code is now running and ready for your requests.

## Step 4: First Vibe - Build the Income and Expenses Sheets

Instead of building a spreadsheet cell by cell, just describe what you want.

- In the Claude Code terminal, type:

```
Create a spreadsheet called budget.xlsx with two sheets: "Income" and "Expenses". Income should have columns for Source, Month, and Amount, with 3 example income sources across 2 months. Expenses should have columns for Category, Month, and Amount, with 6 example categories (like Rent, Groceries, Transportation, Utilities, Entertainment, Savings) across the same 2 months. Add a Total row at the bottom of each sheet using SUM formulas.
```

- Press Enter
- Watch Claude write and run a Python script that builds the workbook, then recalculates it so the totals show real numbers
- Open `budget.xlsx` in the Excel Viewer tab and click through both sheets

**Save your progress:** Ask Claude to commit using Git, or do this yourself from GitHub Desktop:
```
Commit these changes.
```

## Step 5: Second Vibe - Add a Summary Sheet

Before building charts, tie the two sheets together.

- In the Claude Code terminal, type:

```
Add a third sheet called "Summary" to budget.xlsx. It should show Total Income, Total Expenses, and Net Savings (Income minus Expenses), each computed with formulas that reference the Income and Expenses sheets - not hardcoded numbers.
```

- Press Enter
- Claude updates the workbook and recalculates it
- Open the **Summary** tab and click on the Net Savings cell to confirm it's a formula referencing the other sheets

**Save your progress:** Ask Claude to commit, or use GitHub Desktop.

## Step 6: Third Vibe - Add Charts

Numbers are useful, but charts tell the story at a glance.

- In the Claude Code terminal, type:

```
Add a pie chart to the Expenses sheet showing each category's total share of spending. Add a bar chart to the Summary sheet comparing Total Income vs Total Expenses for each month.
```

- Press Enter
- Claude adds both charts and recalculates the file
- Reopen `budget.xlsx` in the Excel Viewer (or refresh the tab) and check both sheets for the new charts

## Step 7: Fourth Vibe - Highlight Over-Budget Categories

Make problems visible at a glance instead of hunting through numbers.

- In the Claude Code terminal, type:

```
On the Expenses sheet, add conditional formatting so any expense over $500 in a single month is highlighted in red, and anything under $100 is highlighted in green.
```

- Press Enter
- Reopen the file and check the Expenses sheet - cells should now be colored based on their value

If something doesn't look right, copy what you see and describe it to Claude to fix.

## Step 8: Fifth Vibe - Add a Category Dropdown

Make the sheet easier to extend without typos.

- In the Claude Code terminal, type:

```
Add data validation to the Category column in the Expenses sheet so it only accepts values from a dropdown list of the existing categories, plus "Other". Add two blank rows at the bottom ready for new entries.
```

- Press Enter
- Open the file, click into one of the blank Category cells, and confirm a dropdown arrow appears with your category list

## Step 9: Review and Commit

Before committing, review what Claude built.

- In the Excel Viewer, click through all three sheets - Income, Expenses, Summary
- You don't need to understand every formula, but get a sense of the structure
- Open GitHub Desktop
- You'll see `budget.xlsx` listed as a changed file
- In the **Summary** field at bottom left, type:

```
Add charts, conditional formatting, and category dropdown to budget tracker
```

- Click **Commit to main**
- Click **Push origin** to back up to GitHub

You've saved a full working version of your budget tracker!

## Step 10: Iterate and Improve

Vibe coding shines when you iterate. Try adding features by describing them:

**Example requests to Claude:**

- "Add a Savings Goal row to the Summary sheet showing progress toward a $500/month savings target"
- "Add a fourth sheet that shows a year-over-year comparison once I add more months of data"
- "Change the pie chart colors to a blue and gray theme"
- "Add a note explaining each formula so I can learn what they do"
- "Create a second workbook called household_budget.xlsx for a family of four with more categories"

After each successful feature:
- Open the file and check it in the Excel Viewer
- If it works, commit with GitHub Desktop
- If something looks wrong, describe it to Claude and ask to fix it
- When fixed, commit the working version

**Key principles:**

- **Describe outcomes, not implementation** - Say "highlight expenses over $500" not "use conditional formatting with a CellIsRule"
- **Iterate quickly** - Test → refine → test → refine
- **Commit working versions** - Save each success before trying new features
- **Embrace failures** - If a formula or chart doesn't come out right, just describe the problem and ask Claude to fix it
- **Stay in control** - You decide what the tracker should show and when it's good enough

Each time, follow the pattern: describe → check the file → iterate → commit.

## Next Steps

- **Apply to your own finances** - Ask Claude to rebuild the tracker around your real income and expense categories
- **Import real data** - Drop a bank statement CSV into your project folder and ask Claude to fold it into the tracker
- **Learn by asking** - When Claude writes a formula, ask "explain what this formula does" to learn Excel
- **Share your tracker** - Push the finished file to GitHub so you (or family members) can grab the latest version
- **Read about vibe coding** - Visit [IBM's guide](https://www.ibm.com/think/topics/vibe-coding) to learn more about this coding style

## Troubleshooting

- **A formula cell shows blank or `None`** - The file needs to be recalculated after edits. Ask Claude: "Recalculate budget.xlsx and confirm there are no formula errors."
- **Chart doesn't update after changing data** - Reopen the tab in VS Code (close it and click the file again) to force the Excel Viewer to refresh.
- **Claude makes a mistake** - Normal! Describe what looks wrong and ask Claude to fix it. Vibe coding includes iteration and debugging.
- **Can't push to GitHub** - Make sure you're logged into GitHub Desktop and published the repository (Step 1). Check your internet connection.
- **Dropdown list doesn't appear** - Data validation only shows in real spreadsheet apps (Excel, LibreOffice, Google Sheets), not always in lightweight previewers. Open the file in Excel or LibreOffice Calc to test it.

## Workflow Overview

This tutorial combined several tools into one workflow:

- **GitHub Desktop** - Version control with visual interface (create repos, commit, push)
- **VS Code** - Editor with an Excel Viewer extension for quick previews
- **Claude Code** - AI assistant that builds and edits real `.xlsx` files from your descriptions
- **openpyxl (behind the scenes)** - The engine Claude uses to write formulas, formatting, and charts into the file

The magic isn't any single tool - it's how vibe coding lets you describe what you want and iterate rapidly. You went from an empty folder to a working, chart-filled budget tracker without writing a single formula by hand.

## Everyday Workflow

After this initial setup, your daily vibe coding routine becomes:

1. **Open VS Code** - Open your project folder
2. **Start Claude Code** - Type `claude` in the terminal
3. **Describe your goal** - "Add a feature that..." or "Fix the row where..."
4. **Check the file** - Open it in the Excel Viewer or in Excel/LibreOffice
5. **Iterate or commit** - If something's off, describe the fix; if it works, commit with GitHub Desktop
6. **Push regularly** - Click **Push origin** to back up to GitHub

The more you practice, the better you get at describing what you want. Vibe coding is a skill - you learn what kinds of descriptions work best and how to break big spreadsheet ideas into testable pieces.

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on September 21, 2026.
