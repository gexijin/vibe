[Home](./)

# Use Claude Code for R in VS Code on Mac

You've set up R in VS Code and can write code manually. Now you want AI to help write, improve, and debug your R code while you focus on the analysis. Think of Claude Code as a coding partner who lives inside VS Code - you describe what you want, and it writes or improves the code while you stay in the same window.

## Key Concepts

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - VS Code extension that brings Claude AI assistant directly into your editor with inline code edits
- **Chat Panel** - Side panel in VS Code where you converse with Claude about your code
- **Inline Edits** - Claude's suggested code changes appear directly in your files with diffs you can accept or reject

## What You'll Need

- Finished [R in VS Code](./R_Coding_VS_Code_Guide) tutorial - R should be working in VS Code
- Finished [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) tutorial - Claude Code CLI should be installed
- Claude Pro/Max subscription or Anthropic API key
- 20-30 minutes

## Step 1: Open VS Code and Create R Project

- Open **Visual Studio Code**
- Click **File** in the menu bar, then **Open Folder**
- Navigate to your **Documents** folder
- Click **New Folder** at the bottom of the dialog
- Name the folder `claude_r_test`
- Click **Open** to open the new folder
- If prompted "Do you trust the authors?", click **Yes, I trust the authors**

## Step 2: Install and Sign in to Claude Code Extension

- Click the **Extensions** icon in the left sidebar (four squares icon)
- In the search box, type `Claude Code`
- Find **Claude Code** by Anthropic and click **Install**
- After installation, a Claude icon (sparkle) appears in the left sidebar
- Click the Claude icon to open the chat panel
- Click **Sign in to Claude Code** in the chat panel
- Choose your authentication method:
  - **Claude Pro/Max users**: Click **Sign in with Claude.ai**, authorize in browser, and copy the code back to VS Code
  - **API key users**: Click **Use API Key** and paste your Anthropic API key
- For detailed authentication steps, see the [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) guide (Step 5)
- Once signed in, you'll see "Ready to help" in the chat panel

## Step 3: Create Initial R Script Manually

- Click **File > New File** in the menu bar
- Click **Select a language** and type `R`, then select **R**
- Save the file by clicking **File > Save**, name it `iris_analysis.R`
- Type this code:

```r
data(iris)
str(iris)
summary(iris)
```

- Save the file by clicking **File > Save**
- Open R terminal: click **View** in menu bar, then **Command Palette**, type `R: Create R Terminal`, press Enter
- Select the code and press `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac) to run it
- You should see dataset structure and summary statistics in the terminal

## Step 4: Ask Claude to Add Scatter Plot

- Click the **Claude** icon in the left sidebar to open the chat panel
- In the chat box at the bottom, type:

```
Add code to iris_analysis.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```

- Press Enter to send
- Claude reads your file and proposes changes - you'll see a diff showing new code to add
- Click **Accept** to apply the changes
- The ggplot2 code appears in your file
- If you don't have ggplot2 installed, run `install.packages("ggplot2")` in the R terminal

## Step 5: Run the Updated Code

- Select all code in `iris_analysis.R`
- Press `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac)
- A scatter plot appears in a separate graphics window
- You should see points colored by species (setosa, versicolor, virginica)

## Step 6: Ask Claude to Refine Plot

- In the Claude chat panel, type:

```
Remove title. Change marker type by species. Change to the classic theme.
```

- Press Enter
- Claude shows the updated code changes
- Click **Accept**
- Run the updated code again: select all and press `Ctrl+Enter` / `Cmd+Enter`
- The plot now displays with different marker shapes per species, no title, and classic theme

## Step 7: Ask Claude for PCA Analysis

- In the Claude chat panel, type:

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- Press Enter
- Claude adds PCA code to your script
- Click **Accept**
- Run all code: select all and press `Ctrl+Enter` / `Cmd+Enter`
- A PCA plot appears showing samples projected onto PC1 and PC2, colored by species

## Step 8: Ask Claude to Review and Comment

- In the Claude chat panel, type:

```
Review the entire script for correctness. Add comments when necessary.
```

- Press Enter
- Claude reviews the code and suggests comments explaining each section
- Click **Accept**
- Your script now has clear comments explaining the data loading, visualization, and PCA analysis

## Next Steps

- Ask Claude to create an R Markdown report: "Create an R Markdown file for this analysis"
- Use Claude to debug errors: "This code gives Error X, can you fix it?"
- Request statistical tests: "Add a t-test comparing sepal length between setosa and versicolor"
- Ask Claude to optimize code: "Make this loop faster using vectorization"
- Get help with unfamiliar functions: "Explain what dplyr::mutate does"

## Troubleshooting

- **Claude extension not showing** - Restart VS Code after installation. Click **View > Extensions** to verify it's installed.
- **"Cannot read R file" error** - Make sure you saved the file with `.R` extension. Claude needs saved files to read them.
- **Authentication failed** - Verify your Claude Pro/Max subscription is active or your API key is valid. See [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) for authentication troubleshooting.
- **ggplot2 not found** - Install it in R terminal: `install.packages("ggplot2")`. Wait for installation to complete before running code.
- **Code changes not applying** - Make sure to click **Accept** on the diff. If it's not working, try copying Claude's suggested code manually.

## Workflow Summary

- **Claude Code Extension** provides an AI assistant directly in VS Code with chat panel and inline diffs
- **Iterative refinement** - Start with basic code, ask Claude to enhance, test immediately, then refine further
- **Context awareness** - Claude reads your R files and understands your project structure
- **Inline editing** - Proposed changes appear as diffs in your actual files, not separate chat responses
- **Stay in flow** - No switching between browser and editor - everything happens in VS Code

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
