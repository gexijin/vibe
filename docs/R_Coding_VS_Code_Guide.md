---
title: "Run R in VS Code"
---
[Home](./)

# Run R in VS Code

You want to write R code but RStudio feels heavy or you prefer VS Code's flexibility. Think of VS Code as a Swiss Army knife - it can handle R, Python, and many other languages in one lightweight editor. This tutorial shows you how to set up R in VS Code with smart features like code completion, interactive plots, and even Shiny apps.

## Key Concepts

- **[languageserver](https://github.com/REditorSupport/languageserver)** - R package that enables code completion, syntax checking, and hover documentation in VS Code
- **[R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - VS Code extension that connects your editor to R and provides syntax highlighting, code execution, and debugging
- **[Shiny Extension](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - VS Code extension for creating and running interactive Shiny web apps with auto-reload

## What You'll Need

- Finished [VS Code Basics](./VS_Code_Getting_Started)
- Internet connection to download R and packages
- 10-15 minutes

## Step 1: Install or Update R

You need R version 4.0 or higher for the best compatibility.

- **Windows**:
  - Download the latest R from [CRAN Windows](https://cran.r-project.org/bin/windows/base/) and run the installer
  - During installation, **note the installation path** (for example: `C:\Program Files\R\R-4.6.1`)
  - If you have an old version, uninstall it first via Settings > Apps

- **macOS**:
  - Download from [CRAN macOS](https://cran.r-project.org/bin/macosx/) and run the .pkg installer
  - The CRAN installer puts R at `/Library/Frameworks/R.framework/Resources/bin/R` on both Intel and Apple Silicon Macs (if you installed R with Homebrew instead, it's `/opt/homebrew/bin/R` on Apple Silicon)
  - If updating, the new version will replace the old one

- **Linux**:
  - Use your package manager (e.g., `sudo apt install r-base` on Ubuntu)
  - Or follow [CRAN Linux](https://cran.r-project.org/bin/linux/) instructions

You'll configure VS Code to find R in Step 4, so don't worry if `R --version` doesn't work in your terminal yet.

## Step 2: Install R Extensions in VS Code

- Open VS Code
- Click the **Extensions** icon in the left sidebar
- Search for `REditorSupport.r` and click **Install** on the R extension by REditorSupport
- Search for `Posit.shiny` and click **Install** on the Shiny extension by Posit

## Step 3: Find Your R Installation Path

Before configuring VS Code, you need to know where R is installed on your system.

### For Windows Users

- Open **File Explorer**
- Navigate to `C:\Program Files\R\`
- You'll see a folder like `R-4.6.1` (your version number may differ)
- Open that folder → Open the `bin` folder
- You'll see `R.exe` there
- The full path is: `C:\Program Files\R\R-4.6.1\bin\R.exe`

**Write down or remember your version number** (e.g., `R-4.6.1`) - you'll need it in Step 4.

### For macOS Users

Your R installation is typically in one of these locations:

- **Standard installation (Intel or Apple Silicon)**: `/Library/Frameworks/R.framework/Resources/bin/R`
- **Homebrew on Apple Silicon**: `/opt/homebrew/bin/R`
- **Homebrew on Intel**: `/usr/local/bin/R`

To verify which path you have, open **Terminal** and type:
```bash
which R
```

This will show you the exact path to your R installation.

### For Linux Users

R is typically installed at: `/usr/bin/R`

Verify by opening a terminal and typing:
```bash
which R
```

## Step 4: Configure VS Code to Find R

- In VS Code, click **View > Command Palette**
- Type `Preferences: Open User Settings (JSON)` and select it
- The settings.json file opens
- Add the line for your platform inside the curly braces `{}`. If there are other lines already, make sure the line above yours ends with a comma

**For Windows**, add this line (replace `R-4.6.1` with your version from Step 3):

```json
"r.executablePath": "C:\\Program Files\\R\\R-4.6.1\\bin\\R.exe",
```

**Why two backslashes (`\\`)?** In JSON files, the backslash `\` is a special character (called an escape character). To represent a single backslash in the actual file path, you must type two backslashes `\\`. So `C:\Program Files` becomes `C:\\Program Files` in settings.json.

**For macOS**, add one of these lines:

```json
"r.executablePath": "/Library/Frameworks/R.framework/Resources/bin/R",
```

Or if you installed R via Homebrew on Apple Silicon:

```json
"r.executablePath": "/opt/homebrew/bin/R",
```

**For Linux**, add:

```json
"r.executablePath": "/usr/bin/R",
```

- Save the file by clicking **File > Save**
- **Restart VS Code** completely for changes to take effect

## Step 5: Install Required R Packages

- In VS Code, click **View** in the top menu, then select **Command Palette**
- Type `R: Create R Terminal` and select it
- An R console will appear in the terminal panel at the bottom
  - You should see R start up with version information
  - If VS Code asks to install the **sess** package, click **Yes** (or **Install bundled sess**) and wait for it to finish. It lets VS Code show your plots and variables
  - If you get an error, double-check your settings.json configuration in Step 4 and restart VS Code
- Install packages by typing these commands one at a time:

```r
install.packages("languageserver")
install.packages("shiny")
```

- Wait for installation to complete (may take a few minutes)
- Type `q()` and press Enter to exit R
- R closes right away (if it asks about saving the workspace, type `n`)

Simply typing `R` in a regular terminal won't work unless R is in your system PATH. The R extension uses your `r.executablePath` setting to find R.

## Step 6: Create Your R Project

- Create a new folder on your computer (e.g., `my-r-project`)
- In VS Code, click **File > Open Folder** and select your new folder
- Click **File > New File...** in the top menu, then choose **R Document** from the list at the top of the window
- Save the file as `analysis.R` by clicking **File > Save**

## Step 7: Write Your First R Script

- Type this code into `analysis.R`:

```r
# Load the iris dataset
data(iris)

# View the first few rows
head(iris)

# Generate summary statistics
summary(iris)

hist(iris$Sepal.Length)
```

- Save the file by clicking **File > Save**

## Step 8: Run R Code Interactively

- With `analysis.R` open, select a line of code and press `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac) to run it
- If no R terminal is open, a **Run R code** list appears at the top of the window. Choose **Create R terminal** (not **New R Interactive window**, which needs extra software). The R terminal opens and runs your line
- Watch the output appear in the terminal. The histogram opens in a plot tab inside VS Code, next to your script
- You can also select all lines and run them the same way.

## Step 9: Create a Simple Shiny App

- Create a new file in your project folder: click **File > New File...**, then choose **R Document**
- Save it as `app.R`
- Type this code:

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Interactive Histogram"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 5,
                  max = 50,
                  value = 30)
    ),

    mainPanel(
      plotOutput("histogram")
    )
  )
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    x <- faithful$waiting
    bins <- seq(min(x), max(x), length.out = input$bins + 1)

    hist(x, breaks = bins, col = "steelblue", border = "white",
         xlab = "Waiting time (minutes)",
         main = "Distribution of Waiting Times")
  })
}

shinyApp(ui = ui, server = server)
```

- Save the file
- Notice the **▶** button that appears at the top right of the editor
- Click the drop down to select **Run Shiny App**
- The app opens in a browser or VS Code panel
- Move the slider and watch the histogram update instantly

## Step 10: Use Code Completion and Hover Help

- In `analysis.R`, start typing `mea` on a new line
- A dropdown appears with suggestions - select `mean()` by pressing Enter
- Hover your mouse over the word `mean` you just typed
- A popup shows the function documentation and usage examples
- Try hovering over `summary` or `hist` in your script to see their documentation
- Type `iris$` and watch VS Code suggest column names (`Sepal.Length`, `Species`, and so on)

## Step 11: Try More Features

- **Markdown integration**: Create an R Markdown file (`.Rmd`) to mix code, output, and text
- **Code formatting**: Right-click in your R script and select **Format Document** to auto-format code
- **Debugging**: Install the [R Debugger extension](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) and follow its setup page to add breakpoints and step through code
- **Git integration**: Use VS Code's built-in Git features to version control your R projects

## Next Steps

- Create a multi-file Shiny app with separate `ui.R` and `server.R` files
- Explore [ggplot2](https://ggplot2.tidyverse.org/) for advanced data visualization
- Try the [tidyverse](https://www.tidyverse.org/) packages (`dplyr`, `tidyr`) for data manipulation
- Learn R Markdown or [Quarto](https://quarto.org/) for creating reports with embedded R code
- Install the [R Debugger extension](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) for advanced debugging

## Troubleshooting

- **"R is not recognized" in VS Code terminal**: VS Code can't find R. Check your settings.json (Step 4) - verify the R path is correct and points to `R.exe` (Windows) or the R binary (Mac/Linux). Example paths:
  - Windows: `C:\\Program Files\\R\\R-4.6.1\\bin\\R.exe` (adjust version number)
  - macOS (CRAN installer, Intel or Apple Silicon): `/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew: `/opt/homebrew/bin/R`
  - Linux: `/usr/bin/R`
  After fixing, restart VS Code completely.

- **R version mismatch in settings**: If you updated R but VS Code still uses the old version, update the version number in your settings.json `r.executablePath` line to match the new R installation (see Step 3 to find your current installation path).

- **Code completion not working**: Make sure languageserver installed successfully (Step 5). Restart VS Code after installation. Wait 10-20 seconds after opening an R file for the language server to initialize. Check the Output panel (View > Output > R Language Server) for errors.

- **Plots not appearing**: Plots open in a tab inside VS Code. If nothing appears, make sure you started R with **R: Create R Terminal** (not by typing `R` in a plain terminal), then run the `hist()` line again.

- **Shiny app won't run**: Ensure the Shiny extension is installed (Step 2), shiny package is installed (Step 5), and your file is named `app.R`. Check the terminal for error messages. The Run button only appears when VS Code recognizes the file as a Shiny app.

## Workflow Summary

VS Code provides a modern, lightweight alternative to RStudio with these key advantages:

- **Unified environment**: Code R, Python, JavaScript, and more in one editor
- **Customizable**: Install only the extensions you need for a lean setup
- **Integrated terminal**: Run R, Git, and shell commands side-by-side
- **Shiny development**: One-click app launching with auto-reload saves time
- **Version control**: Built-in Git integration without external tools

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
