[Home](./)

# Using Claude Code with RStudio on Mac

You have RStudio on Mac for running R code and Claude Code for AI-powered coding assistance. This tutorial shows you how to use both tools together on the same project files. You'll create an R project, write some code manually, then use Claude Code from Terminal to enhance it with visualizations and analysis—all while RStudio stays open to run and test your code.

## Key Concepts

- **Terminal** - Mac's command-line interface where Claude Code runs
- **Shared files** - Both RStudio and Claude Code work on the same files in your Documents folder
- **Hybrid workflow** - RStudio runs code; Claude Code writes and improves it

## What You'll Need

- Completed the [Install Claude Code on Mac](./Install_Claude_Code_MacOS) guide
- RStudio installed on Mac
- 20-30 minutes

## Step 1: Open RStudio on Mac

- Click on **Launchpad** in your Dock (the grid of dots icon)
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
- Click **Open**
- Click **Create Project**
- RStudio creates the project and switches to it

## Step 3: Create a New R Script

- In RStudio, click **File > New File > R Script**
- A new empty script opens in the top-left pane
- Click **File > Save** (or press **Command (⌘) + S**)
- Name the file: `iris.R`
- Click **Save**

## Step 4: Write Initial Code Manually

Type this code into your `iris.R` file:

```r
data(iris)
str(iris)
summary(iris)
```

- Click **File > Save** to save your changes (or press **Command (⌘) + S**)
- To run the code: highlight all lines, then click **Run** button (top-right of script pane)
- You should see output in the Console pane showing dataset structure and statistics

## Step 5: Open Terminal

- Open **Finder** and click **Applications** in the left sidebar
- Open the **Utilities** folder
- Double-click **Terminal**
- The Terminal window opens

## Step 6: Navigate to Your Project Folder

- In Terminal, type this command:
  ```
  cd ~/Documents/test_claude
  ```
- Verify you're in the right location by typing:
  ```
  ls
  ```
- You should see `iris.R` and `test_claude.Rproj` listed

**Tip:** If you're not sure of the exact path, you can drag and drop the folder from Finder into Terminal and the full path will appear automatically!

## Step 7: Launch Claude Code

- In Terminal, type:
  ```
  claude
  ```
- Claude Code starts and shows a welcome message
- You may need to authenticate if this is your first session
- You're now ready to use AI assistance for your R project

## Step 8: Ask Claude for a Scatter Plot

If Claude Code is slow or unresponsive, just wait for it to initialize. Then, type this request:

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Code will read your `iris.R` file and add the visualization code
- When asked, give Claude permission to edit the iris.R file by selecting the appropriate option
- Wait for Claude to finish (you'll see a confirmation message)


## Step 9: Run the New Code in RStudio

- Switch back to RStudio (click the RStudio window or press **Command (⌘) + Tab**)
- You may see a prompt saying the file has changed - click **Yes** to reload
- If no prompt appears, click **File > Reopen with Encoding > UTF-8**
- Highlight all code and click **Run**
- A scatter plot appears in the **Plots** pane (bottom-right)
- If you get an error about ggplot2, install it by typing `install.packages("ggplot2")` in the Console pane

## Step 10: Refine the Scatter Plot

- Switch to Terminal (press **Command (⌘) + Tab** or click the Terminal window)
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

- Switch to Terminal
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

- Switch to Terminal
- Type this request:
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claude will review the code and add comprehensive comments

## Step 15: Ask Claude to Create R Markdown

- Switch to Terminal
- Type this request:
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claude will ask you for permission to create this file
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

- **RStudio doesn't show file changes** - Click **File > Reopen with Encoding > UTF-8** to manually reload the file, or close and reopen the file.
- **"claude: command not found"** - Make sure you completed the [installation guide](./Install_Claude_Code_MacOS). Try opening a fresh Terminal window, or close Terminal completely (**Command (⌘) + Q**) and reopen it.
- **Plots not appearing** - Make sure ggplot2 is installed. Run `install.packages("ggplot2")` in RStudio Console if needed.
- **"No such file or directory"** - Check that you typed the path correctly in Step 6. Try using the drag-and-drop trick: drag the test_claude folder from Finder into Terminal after typing `cd ` (with a space).
- **Claude Code is slow on first request** - Wait 30-60 seconds for Claude to initialize. Subsequent requests will be faster.

## Mac Keyboard Shortcuts

Useful shortcuts for switching between apps:
- **Command (⌘) + Tab** - Switch between open applications quickly
- **Command (⌘) + `** (backtick) - Switch between windows of the same application
- **Command (⌘) + Space** - Open Spotlight search (to open apps)
- **Command (⌘) + Q** - Quit an application completely

## Next Steps

- Try asking Claude to add statistical tests (t-tests, ANOVA) to your analysis
- Ask Claude to get a **Python version** of this code and prepare a Quarto document
- Ask Claude to create functions for repetitive tasks in your R scripts
- Use Claude to debug error messages when your R code doesn't run
- Explore asking Claude to optimize slow R code for better performance

## Workflow Summary

This hybrid setup combines the best of both worlds:

- **RStudio (Mac)** - Interactive R console, immediate plot viewing, familiar GUI for running code
- **Claude Code (Terminal)** - AI-powered code generation, review, and improvement
- **Shared files** - Both tools work on the same files in your Documents folder
- **Iterative refinement** - Start with manual code, enhance with Claude, test in RStudio, then refine further
- **Documentation** - Claude can generate comprehensive reports and comments for your analysis

The workflow is simple: write or edit code with Claude in Terminal, then immediately test and run it in RStudio. No file copying or manual syncing needed—both applications access the same files seamlessly on your Mac.

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2024.
