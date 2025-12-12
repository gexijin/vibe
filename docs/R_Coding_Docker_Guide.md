[Home](./)

# R Coding in VS Code via Docker Container

Ever tried to share your R code with a colleague, only to spend hours debugging "but it works on my machine" issues? Docker containers are like shipping containers for code—they package your R environment, libraries, and dependencies into a sealed box that works the same everywhere. Plus, you get access to tens of thousands of pre-built images on [Docker Hub](https://hub.docker.com/), where software developers publish ready-to-use environments, skipping the pain of manual software installation. This tutorial shows you how to run R in an isolated, reproducible environment using VS Code and Docker Desktop.

## Key Concepts

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Application that runs containers on your computer, managing isolated environments
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code feature that lets you code inside a Docker container with full IDE support
- **Container Isolation** - Your code runs in a separate Linux environment that only sees your project folder, not your entire computer
- **[Rocker](https://rocker-project.org/)** - Pre-built Docker images specifically designed for R development

## What You'll Need

- Finished [R Coding in VS Code](./R_Coding_VS_Code_Guide)
- Finished [GitHub Desktop Basics](./Github_desktop)
- 20-25 minutes

## Step 1: Install Docker Desktop

- Visit [Docker Desktop download page](https://www.docker.com/products/docker-desktop/)
- Click **Download for Windows** (or Mac/Linux based on your system)
- Run the installer and follow the installation wizard
- When prompted, enable WSL 2 (Windows users) or accept default settings
- After installation, launch Docker Desktop
- Wait for the Docker engine to start (you'll see a green status indicator in the bottom left)

## Step 2: Install Dev Containers Extension

- Open VS Code
- Click the **Extensions** icon in the left sidebar (or click **View > Extensions**)
- Type `dev containers` in the search box
- Find **Dev Containers** by Microsoft
- Click **Install**

## Step 3: Clone the Vibe Project with GitHub Desktop

- Open GitHub Desktop
- Click **File > Clone repository**
- Click the **URL** tab
- In the **Repository URL** field, paste: `https://github.com/gexijin/vibe`
- Choose where to save the project (the **Local Path** field)
- Click **Clone**
- GitHub Desktop will download the project to your chosen location

## Step 4: Open Project in VS Code

- In VS Code, click **File > Open Folder**
- Navigate to the `vibe` folder you just cloned
- Click **Select Folder**
- You'll see the project files in the Explorer sidebar

## Step 5: Reopen in Container

- Look for a notification in the bottom right: **Folder contains a Dev Container configuration file**
- Click **Reopen in Container**
- If you don't see the notification, click the green icon in the bottom-left corner
- Select **Reopen in Container** from the menu
- VS Code will build the container (this takes 5-10 minutes the first time)
- You'll see a progress notification showing the build steps
- When complete, the green icon will show **Dev Container: R in Docker**

**Note:** The container automatically includes the R extension and languageserver package. The Dockerfile and devcontainer.json handle this for you.

## Step 6: Understand the Container Environment

Now you're coding inside a Linux container. Let's explore what this means.

- Click **Terminal > New Terminal** to open a terminal inside the container
- Check your current location:

```bash
pwd
```

You'll see `/workspaces/vibe` - this is your project folder inside the container.

- List the files:

```bash
ls
```

You'll see the same files from the project: `R/`, `.devcontainer/`, `README.md`, etc.

- Try going up one directory:

```bash
cd ..
ls
```

You'll only see `vibe/` - the container is isolated. You can't access your computer's other folders, Desktop, or Documents. This isolation ensures your R environment is clean and reproducible.

- Return to the project folder:

```bash
cd vibe
```

## Step 7: Run R Code Line by Line

The container has R pre-installed with common packages. Let's run a simple data analysis script.

- In VS Code Explorer, navigate to `R/iris_analysis.R`
- Click to open the file
- You'll see R code that analyzes the iris dataset
- Select the first line: `data(iris)`
- Press `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac) to run it
- If you don't have an R terminal open, the first time creates one, the second time runs the code
- Continue running each line one at a time
- When you run `head(iris)`, you'll see the first 6 rows in the terminal
- When you run `summary(iris)`, you'll see statistical summaries
- When you run the `hist()` commands, histogram plots will open in separate windows
- You can also select multiple lines and run them together with `Ctrl+Enter` or `Cmd+Enter`

## Step 8: Run the App

The project includes a demo Shiny app that creates an interactive histogram.

- In VS Code Explorer, navigate to `R/app.R`
- Click to open the file
- You'll see code for a Shiny web application
- Look at the top right of the editor window for a **▶** button
- Click the dropdown arrow next to it and select **Run Shiny App**
- The app will start and VS Code will automatically forward port 3838
- A notification appears: **Open in Browser**
- Click **Open in Browser**
- The Shiny app opens in your web browser
- Move the slider to change the histogram bins - the chart updates in real-time

## Step 9: Make a Simple Change

Let's modify the app to see how development works.

- Keep the app running
- In VS Code, edit `R/app.R`
- Find line 16: `titlePanel("Old Faithful Geyser Data")`
- Change it to:

```r
titlePanel("My First R Docker App")
```

- Save the file (**File > Save**)
- The Shiny extension will automatically reload the app
- Refresh your browser (or it may refresh automatically)
- The title now shows your custom text

## Step 10: Understanding the Dockerfile (Optional)

- In VS Code Explorer, navigate to `.devcontainer/Dockerfile`
- Click to open the file
- You'll see the complete configuration:

```dockerfile
# choose a Dockerhub base image
FROM rocker/shiny-verse:latest

# 1. System deps commonly needed by R packages
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# 2. R packages for VS Code integration: language server + debugger
RUN R -q -e 'install.packages(c("rstudioapi", "languageserver"), repos="https://cloud.r-project.org")'

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest
    
# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Shiny server port
EXPOSE 3838
```

**Key parts:**

- `FROM rocker/shiny-verse:latest` - Base image with R, Shiny, and tidyverse pre-installed
- `RUN apt-get install` - Linux system libraries for R packages
- `RUN R -q -e 'install.packages(...)'` - Permanently installs R packages
- `RUN curl... && apt-get install -y nodejs` - Installs Node.js, required to run Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Installs Claude Code globally for AI assistance
- `EXPOSE 3838` - Opens port 3838 for Shiny apps

**Other Rocker images you can use:**

- `rocker/r-ver:4.5.3` - Just R (specific version)
- `rocker/rstudio:latest` - R with RStudio Server
- `rocker/tidyverse:latest` - R with tidyverse packages
- `rocker/shiny-verse:latest` - R with Shiny and tidyverse (what we're using)

After changing the base image, rebuild the container to apply changes.

## Step 11: Install R Packages in the Docker Image (Optional)

Packages installed via the R console (`install.packages()`) are temporary and disappear when you rebuild the container. To make packages permanent, add them to the Dockerfile.

- In VS Code Explorer, navigate to `.devcontainer/Dockerfile`
- Click to open the file
- Add a new line below other 'install.packages' lines to install the `data.table` package:
```dockerfile
RUN R -q -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
```

- Save the file (**File > Save**)
- Click the green icon in the bottom-left corner
- Select **Rebuild Container** from the menu
- VS Code will rebuild the container with your new package (this takes 2-5 minutes)
- To verify, open an R terminal and type:

```r
library(data.table)
```

If it loads without errors, the package is installed permanently.

## Next Steps

- **Create a new R script** - Make a new `.R` file in the `R/` folder, write data analysis code using built-in datasets like `mtcars` or `iris`
- **Install R packages** - Add packages you need by editing the Dockerfile and rebuilding the container
- **Explore tidyverse** - Try data manipulation with `dplyr` and visualization with `ggplot2` using example datasets

## Troubleshooting

- **Docker Desktop not running** - Open Docker Desktop and wait for the green status indicator before reopening the container
- **Container build fails** - Check your internet connection; the first build downloads ~2GB. Click **Rebuild Container** to retry
- **Port 3838 already in use** - Stop other apps using that port, or change the port in `.devcontainer/devcontainer.json` 

## Workflow Overview

This setup gives you a professional R development environment:

- **VS Code** provides the code editor with syntax highlighting and IntelliSense
- **Docker container** runs an isolated Linux environment with R and all dependencies
- **Rocker image** (`rocker/shiny-verse`) includes R, Shiny, tidyverse, and development tools
- **Dev Container config** (`.devcontainer/`) automatically installs VS Code extensions for R debugging and language support
- **Port forwarding** lets you access the Shiny app running inside the container from your browser

## Everyday Workflow

Once everything is set up, here's your daily routine:

1. **Start Docker Desktop** - Open the app and wait for the green status indicator (Docker must be running)
2. **Open VS Code** - Launch VS Code and open your project folder
3. **Reopen in Container** - If not already in the container, click the green icon (bottom-left) and select **Reopen in Container**
4. **Write and run code** - Edit `.R` files, run line-by-line with `Ctrl+Enter`/`Cmd+Enter`, or run Shiny apps with the **▶ Run Shiny App** button
5. **Save your work** - Your code files (`.R`, `.Rmd`) are saved to your computer and persist across sessions
6. **Commit and push** - Use GitHub Desktop to commit your changes and push to the repository

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
