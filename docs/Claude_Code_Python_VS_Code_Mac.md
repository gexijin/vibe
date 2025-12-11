[Home](./)

# Use Claude Code for Python in VS Code on Mac

You've set up Python in VS Code and can write code manually. Now you want AI to help write, improve, and debug your Python code while you focus on the analysis. Think of Claude Code as a coding partner who lives inside VS Code - you describe what you want, and it writes or improves the code while you stay in the same window.

## Key Concepts

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - VS Code extension that brings Claude AI assistant directly into your editor with inline code edits
- **Chat Panel** - Side panel in VS Code where you converse with Claude about your code
- **Inline Edits** - Claude's suggested code changes appear directly in your files with diffs you can accept or reject

## What You'll Need

- Finished [Python in VS Code](./Python_Coding_VS_Code_Guide) tutorial - Python should be working in VS Code
- Finished [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) tutorial - Claude Code CLI should be installed
- Claude Pro/Max subscription or Anthropic API key
- 20-30 minutes

## Step 1: Open VS Code and Create Python Project

- Open **Visual Studio Code**
- Click **File** in the menu bar, then **Open Folder**
- Navigate to your **Documents** folder
- Click **New Folder** at the bottom of the dialog
- Name the folder `claude_python_test`
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

## Step 3: Create Initial Python Script Manually

- Click **File > New File** in the menu bar
- Click **Select a language** and type `Python`, then select **Python**
- Save the file by clicking **File > Save**, name it `iris_analysis.py`
- Type this code:

```python
from sklearn import datasets
import pandas as pd

# Load iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

# Display structure
print(iris_df.info())
print("\nSummary statistics:")
print(iris_df.describe())
```

- Save the file by clicking **File > Save**
- Open Python terminal: click **View** in menu bar, then **Terminal**
- In the terminal, run: `python iris_analysis.py`
- You should see dataset structure and summary statistics in the terminal

## Step 4: Ask Claude to Add Scatter Plot

- Click the **Claude** icon in the left sidebar to open the chat panel
- In the chat box at the bottom, type:

```
Add code to iris_analysis.py to create a scatter plot of sepal length vs. width, colored by species. Use seaborn.
```

- Press Enter to send
- Claude reads your file and proposes changes - you'll see a diff showing new code to add
- Click **Accept** to apply the changes
- The seaborn/matplotlib code appears in your file
- If you don't have the required packages, run in terminal:
  ```
  pip install seaborn matplotlib scikit-learn pandas
  ```

## Step 5: Run the Updated Code

- In the terminal, run: `python iris_analysis.py`
- A scatter plot window appears
- You should see points colored by species (setosa, versicolor, virginica)
- Close the plot window to continue

## Step 6: Ask Claude to Refine Plot

- In the Claude chat panel, type:

```
Remove title. Change marker type by species. Change to the whitegrid style.
```

- Press Enter
- Claude shows the updated code changes
- Click **Accept**
- Run the updated code again: `python iris_analysis.py` in the terminal
- The plot now displays with different marker shapes per species, no title, and whitegrid style
- Close the plot window to continue

## Step 7: Ask Claude for PCA Analysis

- In the Claude chat panel, type:

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- Press Enter
- Claude adds PCA code to your script
- Click **Accept**
- Run the code: `python iris_analysis.py` in the terminal
- A PCA plot appears showing samples projected onto PC1 and PC2, colored by species
- Close the plot window when done

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

- Ask Claude to create a Jupyter notebook: "Convert this to a Jupyter notebook"
- Use Claude to debug errors: "This code gives Error X, can you fix it?"
- Request statistical tests: "Add a t-test comparing sepal length between setosa and versicolor"
- Ask Claude to optimize code: "Make this code more efficient using numpy vectorization"
- Get help with unfamiliar functions: "Explain what pandas.groupby does"

## Troubleshooting

- **Claude extension not showing** - Restart VS Code after installation. Click **View > Extensions** to verify it's installed.
- **"Cannot read Python file" error** - Make sure you saved the file with `.py` extension. Claude needs saved files to read them.
- **Authentication failed** - Verify your Claude Pro/Max subscription is active or your API key is valid. See [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) for authentication troubleshooting.
- **Package not found errors** - Install required packages in terminal: `pip install seaborn matplotlib scikit-learn pandas`. Wait for installation to complete before running code.
- **Code changes not applying** - Make sure to click **Accept** on the diff. If it's not working, try copying Claude's suggested code manually.
- **Plot not showing** - Make sure you have a display. On some systems you may need to add `plt.show()` at the end or use `%matplotlib inline` in Jupyter.

## Workflow Summary

- **Claude Code Extension** provides an AI assistant directly in VS Code with chat panel and inline diffs
- **Iterative refinement** - Start with basic code, ask Claude to enhance, test immediately, then refine further
- **Context awareness** - Claude reads your Python files and understands your project structure
- **Inline editing** - Proposed changes appear as diffs in your actual files, not separate chat responses
- **Stay in flow** - No switching between browser and editor - everything happens in VS Code

---

Estimated completion time: 30 minutes. Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.

[Other tutorials](https://github.com/gexijin/vibe)
