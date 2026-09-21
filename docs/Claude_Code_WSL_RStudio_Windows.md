---
title: "Using Claude Code with RStudio on Windows"
---
[Home](./)

# Using Claude Code with RStudio on Windows

You have RStudio on Windows for running R code and Claude Code for AI-powered coding assistance. This tutorial shows you how to use both tools together on the same project files. You'll create an R project, write some code manually, then use Claude Code from PowerShell to enhance it with visualizations and analysis—all while RStudio stays open to run and test your code.

## Key Concepts

- **PowerShell** - Windows' built-in command-line tool, used here to run Claude Code alongside RStudio
- **Hybrid workflow** - RStudio runs and displays code; Claude Code writes and improves it
- **Shared files** - Both tools work on the exact same project folder, so changes from one show up in the other

## What You'll Need

- Completed the [Install Claude Code on Windows](./Install_CLAUDE_Code_Win) guide
- RStudio installed on Windows
- 20-30 minutes

## Step 1: Open RStudio on Windows

- Click the **Windows Start button**
- Type `RStudio` in the search box
- Click on **RStudio** to open it
- RStudio window opens with multiple panes

## Step 2: Create a New R Project

- In RStudio, click **File** from the top menu
- Click **New Project...**
- Select **New Directory**
- Select **New Project**
- For **Directory name**, type: `test_claude`
- Click **Browse** next to "Create project as subdirectory of:"
- Navigate to your **Documents** folder
- Click **Select Folder**
- Click **Create Project**
- RStudio creates the project and switches to it

## Step 3: Create a New R Script

- In RStudio, click **File > New File > R Script**
- A new empty script opens in the top-left pane
- Click **File > Save** (or the save icon)
- Name the file: `iris.R`
- Click **Save**

## Step 4: Write Initial Code Manually

Type this code into your `iris.R` file:

```r
data(iris)
str(iris)
summary(iris)
```

- Click **File > Save** to save your changes
- To run the code: highlight all lines, then click **Run** button (top-right of script pane)
- You should see output in the Console pane showing dataset structure and statistics

## Step 5: Open PowerShell

- Click the **Windows Start button**
- Type `PowerShell` in the search box
- Click on **Windows PowerShell** to open it

## Step 6: Navigate to Your Project Folder

- In PowerShell, type:
  ```
  cd ~\Documents\test_claude
  ```
- Verify you're in the right location by typing:
  ```
  dir
  ```
- You should see `iris.R` and `test_claude.Rproj` listed

## Step 7: Launch Claude Code

- In PowerShell, type:
  ```
  claude
  ```

Log in with your Claude subscription following the [installation tutorial](Install_CLAUDE_Code_Win.md). After logging in, you'll see a welcome message and the Claude Code prompt.

## Step 8: Ask Claude for a Scatter Plot

If Claude Code is slow or unresponsive, just wait for it to initialize. Then, type this request:

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2. 
```
- Claude Code will read your `iris.R` file and add the visualization code
- When asked, give Claude permission to edit the iris.R file by selecting the appropriate option
- Wait for Claude to finish (you'll see a confirmation message)


## Step 9: Run the New Code in RStudio

- Switch back to RStudio (click the RStudio window)
- You may see a prompt saying the file has changed - click **Yes** to reload
- If no prompt appears, click **File > Reopen with Encoding > UTF-8**
- Highlight all code and click **Run**
- A scatter plot appears in the **Plots** pane (bottom-right)
- If you get an error about ggplot2, install it by typing `install.packages("ggplot2")` in the Console pane

## Step 10: Refine the Scatter Plot

- Switch to PowerShell
- Type this request:
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## Step 11: View the Refined Plot

- Switch to RStudio
- Reload the file if prompted
- Highlight the updated code and click **Run**
- The plot should now display without a title, with different marker shapes for each species, and using the classic theme


## Step 12: Ask Claude for PCA Plot

- Switch to PowerShell
- Type this request:
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## Step 13: Run the PCA Analysis

- Switch to RStudio
- Reload the file if prompted
- Highlight all code and click **Run**
- A PCA plot appears showing samples projected onto PC1 and PC2, colored by species

## Step 14: Ask Claude to Review and Comment

- Switch to PowerShell
- Type this request:
  ```
  Review the entire script for correctness. Add comments when necessary. 
  ```
- Claude will review the code and add comprehensive comments

## Step 15: Ask Claude to Create R Markdown

- Switch to PowerShell
- Type this request:
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claude will ask you for permission to create this file.
- Claude will create a new `.Rmd` file in your project folder


## Step 16: Knit the R Markdown File

- Switch to RStudio
- Click **File > Open File...**
- Select `iris_report.Rmd` and click **Open**
- Click the **Knit** button (with a yarn ball icon) at the top of the script pane
- RStudio will generate an HTML report
- The report opens in a new window showing your complete analysis with narrative text
- The HTML file is saved in your project folder

## Troubleshooting

- **RStudio doesn't show file changes** - Click **File > Reopen with Encoding > UTF-8** to manually reload the file.
- **"claude: command not found"** - Make sure you completed the installation guide. Try opening a fresh PowerShell window.
- **Plots not appearing** - Make sure ggplot2 is installed. Run `install.packages("ggplot2")` in RStudio Console if needed.
- **Error: "cannot change working directory"** - Your Windows path contains spaces. In Step 6, wrap the path in quotes: `cd "~\Documents\Your Name\test_claude"`
- **Claude Code is slow on first request** - Wait 30-60 seconds for Claude to initialize. Subsequent requests will be faster.
- **Using WSL instead?** - If you set up the optional WSL/Ubuntu path, open the **Ubuntu** app instead of PowerShell in Steps 5-16, and navigate to your project with `cd /mnt/c/Users/YourUsername/Documents/test_claude`

## Next Steps

- Try asking Claude to add statistical tests (t-tests, ANOVA) to your analysis
- Ask Claude to get a **Python version** of this code and prepare a Quarto document
- Ask Claude to create functions for repetitive tasks in your R scripts
- Use Claude to debug error messages when your R code doesn't run
- Explore asking Claude to optimize slow R code for better performance

## Workflow Summary

This hybrid setup combines the best of both worlds:

- **RStudio** - Interactive R console, immediate plot viewing, familiar GUI for running code
- **Claude Code (PowerShell)** - AI-powered code generation, review, and improvement
- **Shared files** - Both tools work directly on the same project folder
- **Iterative refinement** - Start with manual code, enhance with Claude, test in RStudio, then refine further
- **Documentation** - Claude can generate comprehensive reports and comments for your analysis

The workflow is simple: write or edit code with Claude in PowerShell, then immediately test and run it in RStudio. No file copying or manual syncing needed—both tools share the same files.

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
