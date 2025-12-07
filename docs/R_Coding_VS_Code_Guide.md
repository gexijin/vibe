[Home](./)

# R Coding in VS Code

You want to write R code but RStudio feels heavy or you prefer VS Code's flexibility. Think of VS Code as a Swiss Army knife - it can handle R, Python, and many other languages in one lightweight editor. This tutorial shows you how to set up R in VS Code with smart features like code completion, interactive plots, and even Shiny apps.

## Key Concepts

- **[languageserver](https://github.com/REditorSupport/languageserver)** - R package that enables code completion, syntax checking, and hover documentation in VS Code
- **[httpgd](https://github.com/nx10/httpgd)** - R package that displays plots interactively in VS Code's plot viewer
- **[R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - VS Code extension that connects your editor to R and provides syntax highlighting, code execution, and debugging
- **[Shiny Extension](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - VS Code extension for creating and running interactive Shiny web apps with auto-reload

## What You'll Do

- Install or update R on your system
- Install R and Shiny extensions in VS Code
- Install R packages for language support and plotting
- Create a project folder with R scripts
- Write and run R code interactively
- Create visualizations that appear in VS Code
- Build a simple Shiny app with interactive plots
- Use code completion and hover help

## What You'll Need

- VS Code already installed
- Internet connection to download R and packages
- 10-15 minutes
- Basic familiarity with installing software

## Step 1: Install or Update R

You need R version 4.0 or higher for the best compatibility.

- **Check if R is installed**: Open a terminal and type `R --version`
- **If R is not installed or outdated**:
  - **Windows**: Download the latest R from [CRAN Windows](https://cran.r-project.org/bin/windows/base/) and run the installer. If you have an old version, uninstall it first via Settings > Apps.
  - **macOS**: Download from [CRAN macOS](https://cran.r-project.org/bin/macosx/) and run the .pkg installer. If updating, the new version will replace the old one.
  - **Linux**: Use your package manager (e.g., `sudo apt install r-base` on Ubuntu) or follow [CRAN Linux](https://cran.r-project.org/bin/linux/) instructions.
- **Verify installation**: Type `R --version` again to confirm you have version 4.0+

## Step 2: Install R Extensions in VS Code

Two extensions make R development smooth in VS Code.

- Open VS Code
- Click the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
- Search for `REditorSupport.r` and click **Install** on the R extension by REditorSupport
- Search for `Posit.shiny` and click **Install** on the Shiny extension by Posit
- You'll see both extensions listed in your installed extensions

The R extension provides code execution and language support, while Shiny enables one-click app launching.

## Step 3: Install Required R Packages

Two R packages enable smart features in VS Code.

- Open VS Code's integrated terminal (**Terminal > New Terminal** or `` Ctrl+` ``)
- Type `R` and press Enter to start an R session
- Install packages by typing these commands one at a time:

```r
install.packages("languageserver")
install.packages("httpgd")
install.packages("shiny")
```

- Wait for installation to complete (may take a few minutes)
- Type `q()` and press Enter to exit R, then type `n` when asked about saving workspace

These packages enable code completion, interactive plots, and Shiny apps.

## Step 4: Configure the R Extension

Enable httpgd for interactive plotting.

- In VS Code, open Settings (`Ctrl+,` / `Cmd+,`)
- Type `r.plot` in the search box
- Find **R > Plot: Use Httpgd** and check the box to enable it
- Close the Settings tab

This tells VS Code to display plots using httpgd instead of static images.

## Step 5: Create Your R Project

Organize your work in a dedicated folder.

- Create a new folder on your computer (e.g., `my-r-project`)
- In VS Code, click **File > Open Folder** and select your new folder
- Click **New File** icon or press `Ctrl+N` / `Cmd+N`
- Save the file as `analysis.R` (`Ctrl+S` / `Cmd+S`)

You now have a workspace for your R code.

## Step 6: Write Your First R Script

Create a simple data analysis script with functions you can explore.

- Type this code into `analysis.R`:

```r
# Create sample data
set.seed(42)
data <- data.frame(
  x = rnorm(100, mean = 50, sd = 10),
  y = rnorm(100, mean = 100, sd = 20)
)

# Calculate statistics
mean_x <- mean(data$x)
mean_y <- mean(data$y)

print(paste("Mean of x:", round(mean_x, 2)))
print(paste("Mean of y:", round(mean_y, 2)))

# Create a linear model
model <- lm(y ~ x, data = data)
print(summary(model))

# Create a scatter plot
plot(data$x, data$y,
     main = "X vs Y Relationship",
     xlab = "X values",
     ylab = "Y values",
     pch = 19,
     col = "blue")
abline(model, col = "red", lwd = 2)
```

- Save the file

This script generates data, calculates means, fits a linear model, and creates a plot - perfect for testing VS Code features.

## Step 7: Run R Code Interactively

Execute your code and see results in VS Code.

- With `analysis.R` open, press `Ctrl+Shift+P` / `Cmd+Shift+P` to open the Command Palette
- Type `R: Create R Terminal` and select it
- An R console appears in the terminal panel at the bottom
- Select all code (`Ctrl+A` / `Cmd+A`) and press `Ctrl+Enter` / `Cmd+Enter` to run it
- Watch the output appear in the terminal and the plot appear in the **PLOTS** panel on the right

You can also select specific lines and press `Ctrl+Enter` / `Cmd+Enter` to run just those lines.

## Step 8: Create a Simple Shiny App

Build an interactive web app that updates plots in real-time.

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
- Notice the **▶ Run Shiny App** button that appears at the top right of the editor
- Click **▶ Run Shiny App**
- The app opens in a browser or VS Code panel
- Move the slider and watch the histogram update instantly

The Shiny extension automatically detects `app.R` files and provides the run button.

## Step 9: Use Code Completion and Hover Help

VS Code provides smart assistance as you code.

- In `analysis.R`, start typing `mea` on a new line
- A dropdown appears with suggestions - select `mean()` by pressing Enter
- Hover your mouse over the word `mean` in your existing code
- A popup shows the function documentation and usage examples
- Try hovering over `lm`, `summary`, or `plot` to see their documentation
- Type `data$` and watch VS Code suggest column names (`x` and `y`)

The languageserver package enables these smart features by analyzing your code in real-time.

## Step 10: Try More Features

Explore additional VS Code R capabilities.

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

- **Code completion not working**: Make sure languageserver installed successfully (`install.packages("languageserver")` in R). Restart VS Code after installation.
- **Plots not appearing**: Verify httpgd is installed and enabled in settings (`R > Plot: Use Httpgd`). Try running `library(httpgd)` in R terminal to check for errors.
- **Shiny app won't run**: Ensure the Shiny extension is installed and your file is named `app.R`. Check the terminal for error messages about missing packages.
- **R terminal not starting**: Check that R is in your system PATH. Type `R --version` in a regular terminal - if it fails, reinstall R and ensure "Add to PATH" is checked.

## Workflow Summary

VS Code provides a modern, lightweight alternative to RStudio with these key advantages:

- **Unified environment**: Code R, Python, JavaScript, and more in one editor
- **Customizable**: Install only the extensions you need for a lean setup
- **Integrated terminal**: Run R, Git, and shell commands side-by-side
- **Shiny development**: One-click app launching with auto-reload saves time
- **Version control**: Built-in Git integration without external tools

---

Estimated completion time: 15 minutes. Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.

[Other tutorials](https://github.com/gexijin/vibe)
