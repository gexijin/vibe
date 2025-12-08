[Home](./)

# Python Coding in VS Code via Docker Container

Ever tried to share your Python code with a colleague, only to spend hours debugging "but it works on my machine" issues? Docker containers are like shipping containers for code—they package your Python environment, libraries, and dependencies into a sealed box that works the same everywhere. Plus, you get access to tens of thousands of pre-built images on [Docker Hub](https://hub.docker.com/), where software developers publish ready-to-use environments, skipping the pain of manual software installation. This tutorial shows you how to run Python in an isolated, reproducible environment using VS Code and Docker Desktop.

## Key Concepts

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Application that runs containers on your computer, managing isolated environments
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code feature that lets you code inside a Docker container with full IDE support
- **Container Isolation** - Your code runs in a separate Linux environment that only sees your project folder, not your entire computer
- **[Python Official Images](https://hub.docker.com/_/python)** - Pre-built Docker images with Python and essential tools pre-installed

## What You'll Need

- [VS Code](https://code.visualstudio.com/) already installed
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [GitHub Desktop](https://desktop.github.com/) already installed (optional, for cloning projects)
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

## Step 3: Create a Python Project Folder

- Create a new folder on your computer named `python-docker-demo`
- Inside it, create a subfolder named `.devcontainer`
- Inside it, create a subfolder named `python`
- Your structure should look like: `python-docker-demo/.devcontainer/` and `python-docker-demo/python/`

## Step 4: Create the Dockerfile

- In VS Code, click **File > Open Folder**
- Navigate to the `python-docker-demo` folder you just created
- Click **Select Folder**
- In the Explorer sidebar, right-click the `.devcontainer` folder
- Click **New File**
- Name it `Dockerfile`
- Paste the following content:

```dockerfile
# Choose the official Python slim image
FROM python:3.12-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Install Python packages for data science and web apps
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Streamlit port
EXPOSE 8501
```

- Click **File > Save**

## Step 5: Create the Dev Container Configuration

- In the `.devcontainer` folder, create a new file named `devcontainer.json`
- Paste the following content:

```json
{
  "name": "Python in Docker",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy"
      ]
    }
  },
  "forwardPorts": [8501],
  "postCreateCommand": "python3 --version"
}
```

- Click **File > Save**

## Step 6: Create a Python Data Analysis Script

- In the `python` folder, create a new file named `iris_analysis.py`
- Paste the following content:

```python
# Simple data analysis using the iris dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Sepal Length')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Sepal Width')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Iris Sepal Measurements')
plt.legend()
plt.show()
```

- Click **File > Save**

## Step 7: Create a Streamlit Web App

- In the `python` folder, create a new file named `app.py`
- Paste the following content:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geyser Data")

# Slider for number of bins
bins = st.slider("Number of bins:", min_value=5, max_value=50, value=30)

# Generate sample data (simulating Old Faithful eruption durations)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Create histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Eruption Duration (minutes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram with {bins} bins')

st.pyplot(fig)
```

- Click **File > Save**

## Step 8: Reopen in Container

- Click the green icon in the bottom-left corner of VS Code
- Select **Reopen in Container** from the menu
- VS Code will build the container (this takes 5-10 minutes the first time)
- You'll see a progress notification showing the build steps
- When complete, the green icon will show **Dev Container: Python in Docker**

## Step 9: Understand the Container Environment

Now you're coding inside a Linux container. Let's explore what this means.

- Click **Terminal > New Terminal** to open a terminal inside the container
- Check your current location:

```bash
pwd
```

You'll see `/workspaces/python-docker-demo` - this is your project folder inside the container.

- List the files:

```bash
ls
```

You'll see the folders you created: `.devcontainer/`, `python/`, etc.

- Try going up one directory:

```bash
cd ..
ls
```

You'll only see `python-docker-demo/` - the container is isolated. You can't access your computer's other folders, Desktop, or Documents. This isolation ensures your Python environment is clean and reproducible.

- Return to the project folder:

```bash
cd python-docker-demo
```

## Step 10: Run Python Code Line by Line

The container has Python pre-installed with data science packages. Let's run the analysis script.

- In VS Code Explorer, navigate to `python/iris_analysis.py`
- Click to open the file
- Select the first line: `import pandas as pd`
- Press `Shift+Enter` to run it in an interactive Python terminal
- A Python terminal opens at the bottom
- Continue running each line or block one at a time with `Shift+Enter`
- When you run `print(df.head())`, you'll see the first 5 rows in the terminal
- When you run `print(df.describe())`, you'll see statistical summaries
- When you run the histogram code, a plot window will open showing the visualization

## Step 11: Run the Streamlit App

The project includes a demo Streamlit app that creates an interactive histogram.

- In VS Code Explorer, navigate to `python/app.py`
- Click to open the file
- Open a new terminal (**Terminal > New Terminal**)
- Run the app:

```bash
cd python
streamlit run app.py
```

- The app will start and display a URL: `http://localhost:8501`
- A notification appears: **Open in Browser**
- Click **Open in Browser**
- The Streamlit app opens in your web browser
- Move the slider to change the histogram bins - the chart updates in real-time

## Step 12: Make a Simple Change

Let's modify the app to see how development works.

- Keep the app running
- In VS Code, edit `python/app.py`
- Find line 6: `st.title("Old Faithful Geyser Data")`
- Change it to:

```python
st.title("My First Python Docker App")
```

- Click **File > Save**
- Return to your browser
- Click **Always rerun** in the top-right corner
- The title now shows your custom text

## Step 13: Understanding the Dockerfile (Optional)

- In VS Code Explorer, navigate to `.devcontainer/Dockerfile`
- Click to open the file
- You'll see the complete configuration

**Key parts:**

- `FROM python:3.12-slim` - Official Python 3.12 base image (lightweight Debian-based)
- `RUN apt-get install` - Linux system libraries for building Python packages
- `RUN pip install --no-cache-dir ...` - Permanently installs Python packages
- `RUN curl... && apt-get install -y nodejs` - Installs Node.js, required to run Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Installs Claude Code globally for AI assistance
- `EXPOSE 8501` - Opens port 8501 for Streamlit apps

**Other Python images you can use:**

- `python:3.12` - Full Python image with more tools (larger size)
- `python:3.12-slim` - Lightweight image with Python and pip (what we're using)
- `python:3.12-alpine` - Minimal Alpine Linux-based image (smallest size)
- `jupyter/datascience-notebook` - Pre-configured Jupyter with data science libraries

After changing the base image, rebuild the container to apply changes.

## Step 14: Install Python Packages in the Docker Image (Optional)

Packages installed via pip in the terminal (`pip install package`) are temporary and disappear when you rebuild the container. To make packages permanent, add them to the Dockerfile.

- In VS Code Explorer, navigate to `.devcontainer/Dockerfile`
- Click to open the file
- Find line 9: `RUN pip install --no-cache-dir ...`
- Add `scikit-learn` to the list:

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- Click **File > Save**
- Click the green icon in the bottom-left corner
- Select **Rebuild Container** from the menu
- VS Code will rebuild the container with your new package (this takes 2-5 minutes)
- To verify, open a Python terminal and type:

```python
import sklearn
print(sklearn.__version__)
```

If it displays the version without errors, the package is installed permanently.

## Next Steps

- **Create a new Python script** - Make a new `.py` file in the `python/` folder, write data analysis code using built-in datasets or load your own CSV files
- **Install Python packages** - Add packages you need by editing the Dockerfile (line 9) and rebuilding the container
- **Explore data science** - Try data manipulation with pandas and visualization with matplotlib or seaborn
- **Build web apps** - Create interactive dashboards with Streamlit or Flask

## Troubleshooting

- **Docker Desktop not running** - Open Docker Desktop and wait for the green status indicator before reopening the container
- **Container build fails** - Check your internet connection; the first build downloads images and packages. Click **Rebuild Container** to retry
- **Port 8501 already in use** - Stop other apps using that port, or change the port in the Dockerfile and `devcontainer.json`

## Workflow Overview

This setup gives you a professional Python development environment:

- **VS Code** provides the code editor with syntax highlighting, IntelliSense, and debugging
- **Docker container** runs an isolated Linux environment with Python and all dependencies
- **Python official image** (`python:3.12-slim`) includes Python, pip, and essential tools
- **Dev Container config** (`.devcontainer/`) automatically installs VS Code extensions for Python debugging and language support
- **Port forwarding** lets you access web apps (Streamlit, Flask) running inside the container from your browser

## Everyday Workflow

Once everything is set up, here's your daily routine:

1. **Start Docker Desktop** - Open the app and wait for the green status indicator (Docker must be running)
2. **Open VS Code** - Launch VS Code and open your project folder
3. **Reopen in Container** - If not already in the container, click the green icon (bottom-left) and select **Reopen in Container**
4. **Write and run code** - Edit `.py` files, run line-by-line with `Shift+Enter`, or run apps with `streamlit run app.py`
5. **Save your work** - Your code files (`.py`, `.ipynb`) are saved to your computer and persist across sessions
6. **Commit and push** - Use GitHub Desktop to commit your changes and push to the repository

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
