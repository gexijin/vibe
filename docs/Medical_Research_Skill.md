[Home](./)

# Create a Claude Skill for Medical Research

Keeping up with medical research means wading through dense scientific papers filled with jargon. A Claude Skill is like having a research assistant that reads hundreds of papers and explains them in plain English - instead of spending hours searching PubMed and decoding technical language, you ask a simple question and get a clear summary based on the latest science.

In this tutorial, you'll create a Claude Skill that searches peer-reviewed medical literature. We first create a Python script to query PubMed. The best part? You can ask Claude to do all the work! It has a Skill that creates Skills!

## Key Concepts

- **Claude Skill** - A specialized tool that extends Claude Code's capabilities with custom instructions, code, and documentation stored in `.claude/skills/`
- **PubMed** - Free database of 35+ million biomedical research papers maintained by the US National Library of Medicine
- **Biopython** - Python library that provides tools to query PubMed's database programmatically
- **Auto-edit mode** - Feature activated with Shift+Tab that lets Claude make multiple file changes without asking permission each time

## What You'll Need

- Completed [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) or [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- Internet connection for PubMed searches
- 15-20 minutes

## Step 1: Navigate to Project Folder

If you completed the [slash commands tutorial](./Reuse_Prompts_via_Slash_Commands.md), the `test_claude` folder already exists. These commands work either way.

**Windows (WSL):**
- Open **Ubuntu** from the Start menu
- Type these commands:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir -p test_claude
  cd test_claude
  ```
  Replace `YOUR_USERNAME` with your Windows username

**Mac:**
- Open **Terminal** (find it in Applications > Utilities)
- Type these commands:
  ```bash
  cd ~/Documents
  mkdir -p test_claude
  cd test_claude
  ```

The `-p` flag creates the folder if it doesn't exist, or simply does nothing if it already exists.

## Step 2: Start Claude Code

Type this command:
```bash
claude
```

Claude Code starts and displays a welcome message.

## Step 3: Enable Auto-Edit Mode

Press **Shift+Tab** to enable auto-edit mode. You'll see a confirmation message.

Auto-edit mode allows Claude to create and modify multiple files without asking for permission each time. This is essential for building skills which involve creating many files.

## Step 4: Create the PubMed Search Script

Copy and paste this prompt:

```
Write a Python script called pubmed_search.py that:
- Takes a search query as command line argument
- Retrieves up to 10 recent papers
- Returns PMID, title, authors, journal, year, abstract preview, and URL
```
Claude creates the script. It installs the required Biopython package, which includes a entrez module for interacting with PubMed. Review the output to see the script structure.

## Step 5: Test the Script

Ask Claude to test it:

```
Test the script with the query "immunotherapy breast cancer"
```

Claude runs the script and displays 10 recent papers about immunotherapy for breast cancer. You'll see titles, authors, abstracts, and PubMed links.

**Note:** The search finds thousands of papers but retrieves only the 10 most recent for quick review.

## Step 6: Create the Medical Research Skill

Now we'll package everything into a reusable skill. Copy and paste:

```
Create a Claude Skill called "medical-research" that:
- Takes on a medical question
- Designs queries to retrieve PubMed abstracts
- Creates plain-language summaries accessible to non-scientists
- Includes the pubmed_search.py script inside the skill folder
```

Claude creates the complete skill structure:
- `.claude/skills/medical-research/pubmed_search.py` - The search script
- `.claude/skills/medical-research/SKILL.md` - Instructions for Claude on how to use the skill
- `.claude/skills/medical-research/README.md` - User documentation
- `.claude/skills/medical-research/EXAMPLES.md` - Example outputs

This takes 2-3 minutes as Claude writes comprehensive documentation.

## Step 7: Test the Skill

Ask a research question in plain language:

```
Can I lose weight via keto diet?
```

Claude automatically:
- Recognizes this as a medical research question
- Activates the medical-research skill
- Searches PubMed for relevant papers
- Analyzes the findings
- Explains the research in plain language covering effectiveness, mechanisms, and considerations

The response includes sections like "How It Works," "Research Findings," "Important Considerations," and "The Bottom Line."

## Step 8: Test Another Question

Try another research topic:

```
Does vaccine cause autism?
```

The response explains the scientific consensus, the origin of the myth, and real-world consequences.

## Step 9: Explore the Skill Files (Optional)

Open VS Code to see the skill structure:

**Windows:**
- Open **File Explorer**, navigate to `C:\Users\YOUR_USERNAME\Documents\test_claude`
- Right-click the folder and select **Open with Code**

**Mac:**
- Open **Finder**, navigate to `Documents/test_claude`
- Right-click the folder and select **Open with Visual Studio Code**
- Or just type ``` code . ``` from Terminal

In VS Code:
- Expand `.claude/skills/medical-research/` in the file explorer
- Open `SKILL.md` to see detailed instructions for Claude
- Open `README.md` to see user documentation
- Open `pubmed_search.py` to see the Python code

**Note:** The skill is completely self-contained - all code and documentation live in one folder.

## Step 10: Installing Skills from Anthropic's Repository

Anthropic maintains a repository of pre-built skills that you can install and use instantly. 

- To install a skill from the repository, simply ask Claude:

  ```
  Install the document skill from Anthropic's repository
  ```
- Try this skill:
  ```
  Create a PowerPoint presentation on Claude Skills.
  ```


The **document skill** helps you read and write files in PDF, Word, PowerPoint, and Excel. Claude will clone the skill into your `.claude/skills/` folder.

**Other available skills from Anthropic's repository:**
- Browse the full catalog at [github.com/anthropics/claude-skills](https://github.com/anthropics/skills)
- Ask Claude "What skills are available in the Anthropic repository?" to see the current list

## Next Steps

- **PDF:** Copy a few PDF files in a subfolder in this project folder and ask for summaries.
- **Other public skills:** Try skills available from Anthropic.
- **Share skills:** Skills are just zipped folders!
- **Create other skills:** Anything you are interested in. For example, you can put your own data files in a skill folder.

## Troubleshooting

- **Biopython not installed:** Claude will automatically install Biopython when it creates the script. If you see import errors when testing, ask Claude to install Biopython manually with `pip install biopython`
- **Script not found:** Check that auto-edit mode was enabled (Shift+Tab) - Claude needs permission to create files
- **Skill doesn't activate:** The skill should work immediately after creation - try asking the question again or check that SKILL.md has the correct `name: medical-research` in the header

## Workflow Overview

- **Claude Skills** are more powerful than slash commands - they combine code, documentation, and custom instructions
- **Auto-edit mode** (Shift+Tab) streamlines creation by avoiding repeated permission prompts
- **Self-contained packaging** - Scripts live inside skill folders, making them portable and shareable
- **Automatic activation** - Skills trigger based on question patterns (research questions activate medical-research)
- **Plain-language interface** - Ask natural questions without knowing the technical details

## Skills vs Slash Commands

| Feature | Skills | Slash Commands |
|---------|--------|----------------|
| **What it contains** | Prompts, code, data, and documentation | Prompts only |
| **Activation** | Automatically loaded when relevant | Manually triggered with `/command` |
| **Use case** | Complex workflows requiring code execution | Quick prompt templates and workflows |
| **File location** | `.claude/skills/skill-name/` | `.claude/commands/` |
| **Structure** | Multiple files (SKILL.md, README.md, code files) | Single `.md` file per command |

**Key Takeaway:** Slash Commands just injects prompts from the UI. It is useful, but limited.

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 13, 2025.
