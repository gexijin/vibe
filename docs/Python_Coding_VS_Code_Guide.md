[Home](./)

# Python Coding in VS Code

You want to write Python code but aren't sure which editor to use, or you're looking for something lighter than PyCharm. Think of VS Code as a Swiss Army knife - it handles Python, R, JavaScript, and many other languages in one lightweight editor. This tutorial shows you how to set up Python in VS Code with smart features like code completion, interactive debugging, and even web apps.

## Key Concepts

- **[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - VS Code extension by Microsoft that provides syntax highlighting, debugging, code execution, and Jupyter notebook support
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - Language server that enables fast IntelliSense, type checking, and auto-imports for Python
- **[Virtual Environment](https://docs.python.org/3/library/venv.html)** - Isolated Python environment for managing project-specific packages without affecting system Python
- **[Streamlit](https://streamlit.io/)** - Python library for creating interactive web apps with simple Python scripts

## What You'll Need

- VS Code already installed
- Internet connection to download Python and packages
- 15-20 minutes
- Basic familiarity with installing software

## Step 1: Install Python

You need Python 3.8 or higher for the best compatibility with modern packages.

- **Windows**:
  - Download the latest Python from [python.org](https://www.python.org/downloads/)
  - Run the installer
  - **Check the box "Add python.exe to PATH"** before clicking Install Now
  - Note the installation location (typically `C:\Users\YourName\AppData\Local\Programs\Python\Python312`)

- **macOS**:
  - Download from [python.org](https://www.python.org/downloads/) and run the installer
  - Or use Homebrew: open Terminal and type `brew install python`
  - Homebrew path: `/opt/homebrew/bin/python3` (Apple Silicon) or `/usr/local/bin/python3` (Intel)

- **Linux**:
  - Python is usually pre-installed. Check version with `python3 --version`
  - If needed, install via package manager: `sudo apt install python3 python3-pip python3-venv` (Ubuntu/Debian)

Verify installation by opening a terminal and typing `python3 --version` or `python --version`.

## Step 2: Install Python Extensions in VS Code

- Open VS Code
- Click the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X` on Windows/Linux, `Cmd+Shift+X` on Mac)
- Search for `ms-python.python` and click **Install** on the Python extension by Microsoft
- Pylance should install automatically with the Python extension. If not, search for `ms-python.vscode-pylance` and install it

The Python extension includes support for debugging, IntelliSense, code formatting, and Jupyter notebooks.

## Step 3: Create Your Python Project

- Create a new folder on your computer (e.g., `my-python-project`)
- In VS Code, click **File > Open Folder** and select your new folder
- Click **File > New File** in the top menu
- Save the file as `analysis.py` by clicking **File > Save**

## Step 4: Select Python Interpreter

VS Code needs to know which Python installation to use.

- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette
- Type `Python: Select Interpreter` and select it
- Choose the Python version you installed (e.g., `Python 3.12.x` or similar)
- The selected interpreter appears in the bottom-right corner of VS Code

If you don't see your Python installation, click **Enter interpreter path** and navigate to where Python is installed.

## Step 5: Create a Virtual Environment

Virtual environments keep your project dependencies isolated.

- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
- Type `Python: Create Environment` and select it
- Choose **Venv** (built-in virtual environment)
- Select your Python interpreter from the list
- Wait for VS Code to create the environment (you'll see a `.venv` folder appear)
- VS Code will automatically activate this environment for your project

You'll see `(.venv)` in your terminal prompt when the environment is active.

## Step 6: Install Required Packages

- Open a new terminal in VS Code by clicking **View > Terminal**
- The terminal should show `(.venv)` indicating your virtual environment is active
- Install packages by typing these commands:

```bash
pip install pandas matplotlib streamlit
```

- Wait for installation to complete (may take 1-2 minutes)

If `(.venv)` doesn't appear, the environment isn't active. Press `Ctrl+Shift+P` and run `Python: Select Interpreter`, then choose the interpreter with `('.venv': venv)` next to it.

## Step 7: Write Your First Python Script

Type this code into `analysis.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# View the first few rows
print(iris.head())

# Generate summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- Save the file by clicking **File > Save**

## Step 8: Run Python Code Interactively

- With `analysis.py` open, click the **▶ Run Python File** button in the top-right corner
- Or right-click in the editor and select **Run Python File in Terminal**
- Watch the output appear in the terminal panel
- A histogram window will pop up showing your plot
- You can also select specific lines and press `Shift+Enter` to run just those lines in an interactive Python session

## Step 9: Create a Simple Streamlit App

- Create a new file: **File > New File**
- Save it as `app.py`
- Type this code:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# Sidebar slider
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# Load data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Create histogram
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# Display in Streamlit
st.pyplot(fig)
```

- Save the file
- Open the terminal and run:

```bash
streamlit run app.py
```

- The app opens in your browser (usually at `http://localhost:8501`)
- Move the slider in the sidebar and watch the histogram update instantly
- Press `Ctrl+C` in the terminal to stop the app

## Step 10: Use Code Completion and IntelliSense

- In `analysis.py`, start typing `iris.` on a new line
- A dropdown appears with all available methods and attributes
- Type `iris.gr` and watch it suggest `groupby()`
- Hover your mouse over `pd.read_csv` in your existing code
- A popup shows function signature, parameters, and documentation
- Try typing `import ` and watch VS Code suggest package names
- When you type a function call, IntelliSense shows parameter hints

## Step 11: Try Debugging

- In `analysis.py`, click to the left of line number 8 (the `print(iris.head())` line) to set a breakpoint (red dot appears)
- Press `F5` or click **Run > Start Debugging**
- Select **Python File** when prompted
- Code execution pauses at the breakpoint
- Use the debug toolbar to step through code, inspect variables, and see the call stack
- Press `F5` again to continue execution

## Next Steps

- Explore [pandas](https://pandas.pydata.org/) for data manipulation and analysis
- Learn [Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) in VS Code for interactive data science
- Try [Flask](https://flask.palletsprojects.com/) or [FastAPI](https://fastapi.tiangolo.com/) for building web APIs
- Install [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) for automatic code formatting
- Use [pytest](https://docs.pytest.org/) for writing and running tests

## Troubleshooting

- **"Python is not recognized" in terminal**: Python isn't in your system PATH. On Windows, reinstall Python and check "Add python.exe to PATH". On Mac/Linux, use `python3` instead of `python`. Restart VS Code after fixing.

- **No interpreter found**: Click the interpreter selector in the bottom-right corner of VS Code, or press `Ctrl+Shift+P` and run `Python: Select Interpreter`. If your Python installation doesn't appear, select **Enter interpreter path** and browse to your Python executable.

- **Virtual environment not activating**: VS Code should auto-activate it when you open a terminal. If not, manually activate: Windows: `.venv\Scripts\activate`, Mac/Linux: `source .venv/bin/activate`. Verify by seeing `(.venv)` in your terminal prompt.

- **IntelliSense not working**: Make sure Pylance is installed and enabled. Check the bottom-right corner shows your selected interpreter. Wait 10-20 seconds after opening a file for Pylance to initialize. Restart VS Code if issues persist.

- **pip install fails**: Ensure your virtual environment is activated (look for `(.venv)` in terminal). On Linux, you might need to install `python3-venv` first. On Windows, check antivirus isn't blocking pip.

- **Streamlit app won't run**: Ensure streamlit is installed in your virtual environment (`pip list | grep streamlit`). Check the terminal for error messages. Make sure no other app is using port 8501.

## Workflow Summary

VS Code provides a modern, lightweight environment for Python development with these advantages:

- **Unified environment**: Code Python, R, JavaScript, and more in one editor
- **Powerful IntelliSense**: Smart completions, type checking, and auto-imports via Pylance
- **Integrated debugging**: Set breakpoints, inspect variables, and step through code
- **Jupyter support**: Run notebooks directly in VS Code without separate applications
- **Version control**: Built-in Git integration for tracking changes
- **Extensions ecosystem**: Thousands of extensions for testing, formatting, linting, and more

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.

[Other tutorials](https://github.com/gexijin/vibe)
