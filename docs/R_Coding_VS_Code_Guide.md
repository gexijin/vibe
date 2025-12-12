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
  - During installation, **note the installation path** (for example: `C:\Program Files\R\R-4.5.3`)
  - If you have an old version, uninstall it first via Settings > Apps

- **macOS**:
  - Download from [CRAN macOS](https://cran.r-project.org/bin/macosx/) and run the .pkg installer
  - Note whether you're using Intel (`/Library/Frameworks/R.framework/Resources/bin/R`) or Apple Silicon with Homebrew (`/opt/homebrew/bin/R`)
  - If updating, the new version will replace the old one

- **Linux**:
  - Use your package manager (e.g., `sudo apt install r-base` on Ubuntu)
  - Or follow [CRAN Linux](https://cran.r-project.org/bin/linux/) instructions

You'll configure VS Code to find R in Step 3, so don't worry if `R --version` doesn't work in your terminal yet.

## Step 2: Install R Extensions in VS Code

- Open VS Code
- Click the **Extensions** icon in the left sidebar
- Search for `REditorSupport.r` and click **Install** on the R extension by REditorSupport
- Search for `Posit.shiny` and click **Install** on the Shiny extension by Posit

## Step 3: Find Your R Installation Path

Before configuring VS Code, you need to know where R is installed on your system.

### For Windows Users

1. Open **File Explorer**
2. Navigate to `C:\Program Files\R\`
3. You'll see a folder like `R-4.5.3` (your version number may differ)
4. Open that folder → Open the `bin` folder
5. You'll see `R.exe` there
6. The full path is: `C:\Program Files\R\R-4.5.3\bin\R.exe`

**Write down or remember your version number** (e.g., `R-4.5.3`) - you'll need it in Step 4.

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

- In VS Code, click the **gear icon** in the lower left corner
- Select **Settings** from the menu
- In the search bar at the top, type `r.rpath.windows` (Windows), `r.rpath.mac` (macOS), or `r.rpath.linux` (Linux)
- You should see the setting appear. Click **Edit in settings.json** below the setting
- The settings.json file will open
- Add the appropriate configuration for your platform inside the curly braces `{}`

**For Windows**, add this line (replace `R-4.5.3` with your version from Step 3):

```json
"r.rpath.windows": "C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe",
```

**Why two backslashes (`\\`)?** In JSON files, the backslash `\` is a special character (called an escape character). To represent a single backslash in the actual file path, you must type two backslashes `\\`. So `C:\Program Files` becomes `C:\\Program Files` in settings.json.

**For macOS**, add one of these lines:

```json
"r.rpath.mac": "/Library/Frameworks/R.framework/Resources/bin/R",
```

Or if you installed R via Homebrew on Apple Silicon:

```json
"r.rpath.mac": "/opt/homebrew/bin/R",
```

**For Linux**, add:

```json
"r.rpath.linux": "/usr/bin/R",
```

- Save the file by clicking **File > Save**
- **Restart VS Code** completely for changes to take effect

## Step 5: Install Required R Packages

- In VS Code, click **View** in the top menu, then select **Command Palette**
- Type `R: Create R Terminal` and select it
- An R console will appear in the terminal panel at the bottom
  - You should see R start up with version information
  - If you get an error, double-check your settings.json configuration in Step 4 and restart VS Code
- Install packages by typing these commands one at a time:

```r
install.packages("languageserver")
install.packages("shiny")
```

- Wait for installation to complete (may take a few minutes)
- Type `q()` and press Enter to exit R
- Type `n` when asked about saving workspace

Simply typing `R` in a regular terminal won't work unless R is in your system PATH. The R extension uses your `r.rpath` setting to find R.

## Step 6: Create Your R Project

- Create a new folder on your computer (e.g., `my-r-project`)
- In VS Code, click **File > Open Folder** and select your new folder
- Click **File > New File** in the top menu
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
- If you don't have a terminal open, the first `Ctrl+Enter` / `Cmd+Enter` opens an R terminal. The second runs the code.
- Watch the output appear in the terminal and the plot will open in a separate window
- You can also select all lines and run them the same way.

## Step 9: Create a Simple Shiny App

- Create a new file in your project folder: **File > New File**
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
- Hover your mouse over the word `mean` in your existing code
- A popup shows the function documentation and usage examples
- Try hovering over `lm`, `summary`, or `plot` to see their documentation
- Type `data$` and watch VS Code suggest column names (`x` and `y`)

## Step 11: Try More Features

- **Markdown integration**: Create an R Markdown file (`.Rmd`) to mix code, output, and text
- **Code formatting**: Right-click in your R script and select **Format Document** to auto-format code
- **Debugging**: Set breakpoints by clicking left of line numbers, then run code in debug mode
- **Git integration**: Use VS Code's built-in Git features to version control your R projects

## Next Steps

- Create a multi-file Shiny app with separate `ui.R` and `server.R` files
- Explore [ggplot2](https://ggplot2.tidyverse.org/) for advanced data visualization
- Try the [tidyverse](https://www.tidyverse.org/) packages (`dplyr`, `tidyr`) for data manipulation
- Learn R Markdown or [Quarto](https://quarto.org/) for creating reports with embedded R code
- Install the [R Debugger extension](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) for advanced debugging

## Troubleshooting

- **"R is not recognized" in VS Code terminal**: VS Code can't find R. Check your settings.json (Step 4) - verify the R path is correct and points to `R.exe` (Windows) or the R binary (Mac/Linux). Example paths:
  - Windows: `C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe` (adjust version number)
  - macOS Intel: `/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew: `/opt/homebrew/bin/R`
  - Linux: `/usr/bin/R`
  After fixing, restart VS Code completely.

- **R version mismatch in settings**: If you updated R but VS Code still uses the old version, update the version number in your settings.json `r.rpath` configuration to match the new R installation (see Step 3 to find your current installation path).

- **Code completion not working**: Make sure languageserver installed successfully (Step 5). Restart VS Code after installation. Wait 10-20 seconds after opening an R file for the language server to initialize. Check the Output panel (View > Output > R Language Server) for errors.

- **Plots not appearing**: Plots will open in separate windows using R's default graphics device. Make sure you have a window manager available. On some systems, you may need to install X11 (macOS) or ensure graphics support is enabled.

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
