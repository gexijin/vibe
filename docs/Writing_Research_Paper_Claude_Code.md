[Home](./)

# Writing a Research Paper with Claude Code

Write research papers faster using Claude Code for research and drafting, while Git tracks every version. **Version control is like an undo button for your entire writing process.** Create save points at each phase—research, draft, revisions—and return to any version anytime.

## Key Concepts

- **Claude Code** - AI assistant that searches the web, organizes research, drafts content, and handles version control through simple requests
- **Git** - Tracks every change to your files, creating restore points (commits) you can return to anytime
- **Commit** - A snapshot of your project at a specific point in time with a description of what changed (e.g., "Add research notes", "Complete first draft")
- **Research Paper Workflow** - Research → Brainstorm → Focused Research → Plan → Draft → Revise 
- **Use AI as an assistant** for reserach, brainstorming, drafting, editing

## What You'll Need

- Claude Code installed ([installation guide](https://code.claude.com/docs/en/installation))
- Git installed (comes with Mac/Linux, [Windows guide](https://git-scm.com/download/win))
- Text editor (VS Code, TextEdit, Notepad, or any editor)
- Terminal access
- 15-20 minutes

## Step 1: Set Up Project and Start Claude Code

If you've completed the [Windows tutorial](./Claude_Code_Git_Windows.md) or [Mac tutorial](./Claude_Code_Git_Mac.md), you already have Git configured. Now create a new project folder for your research paper.

**Windows (WSL Ubuntu):**
```bash
cd /mnt/c/Users/YOUR_USERNAME/Documents
mkdir ai-workplace-research
cd ai-workplace-research
git init
claude
```

**Mac:**
```bash
cd ~/Documents
mkdir ai-workplace-research
cd ai-workplace-research
git init
claude
```

Replace `YOUR_USERNAME` with your actual Windows username. Git is now tracking changes in this folder. Claude Code is ready.

## Step 2: Research and Plan

Ask Claude to research your topic and create an outline:

```
I'm writing a 2-page research paper on AI adoption in the workplace.
Search for recent data on productivity gains and job displacement.
Organize the information sources. Save as general_research.md
```

Claude will search the web, organize findings, and create your outline. Review the file in your text editor and add notes where you want your perspective. 

Instract Claude to commit changes. 
```
commit these changes
```

**First save point created!**

## Step 3: Draft the Paper

Ask Claude to write your paper:

```
Using the outline and research, write a complete 2-page paper in
paper.md. Include introduction, body with data and citations,
and conclusion. Leave a placeholder for my perspective.
```

Claude writes the full draft. Then commit:

```
commit these changes
```

**Second save point created!**

## Step 4: Revise and Add Your Voice

Open `paper.md` in your editor. Read through and add your perspective where the placeholder is. Then ask Claude for any revisions:

```
Make the introduction more engaging with a compelling hook.
```

After revisions, commit again:

```
commit these changes
```

**Third save point created!**

## Step 5: Finalize

Polish the paper in your editor—fix phrasing, check citations. Then commit the final version:

```
commit these changes
```

**Final version saved!**

## Step 6: View Your History

See your complete writing journey:

```
show my commit history
```

Each commit is a restore point you can return to anytime.

## The Complete Workflow

1. **Research & Plan** - Claude searches, organizes findings, creates outline
2. **Draft** - Claude writes the paper based on your plan
3. **Revise** - You add your voice, request improvements from Claude
4. **Finalize** - Polish and save final version
5. **Commit** - Save at each phase to create restore points

Version control means you can experiment fearlessly—return to any previous version anytime.

## Next Steps

Try writing more research papers using this workflow:

- **Technology topics:** "Impact of social media on teen mental health", "Electric vehicles and climate change"
- **Business topics:** "Remote work productivity", "Gig economy and worker rights"
- **Science topics:** "CRISPR gene editing ethics", "Renewable energy adoption challenges"
- **Longer papers:** Ask Claude to create a 5-page paper with more detailed sections

Remember: Research & Plan → Draft → Revise → Finalize. Commit after each phase.

## Troubleshooting

- **"not a git repository" error:** Make sure you're in your project folder (`cd ~/Documents/ai-workplace-research`)
- **Claude search results seem outdated:** Specify "search for 2024-2025 data on [topic]"
- **Draft is too long/short:** Tell Claude: "Make this 2 pages, approximately 1000 words"
- **Can't find files:** In terminal, type `ls` to list all files in current folder
- **Want to see what changed:** In Claude Code, type `show me what changed since last commit`

## What You Can Ask Claude

- `search for more recent statistics on [topic]` - Find newer data
- `summarize the key arguments in this paper` - Get overview
- `make the conclusion more persuasive` - Improve specific sections
- `cite all sources in APA format` - Format references
- `what files have I changed?` - See uncommitted work
- `show me the diff` - See exactly what code changed
- `go back to the previous commit` - Undo all changes since last commit

Claude handles research, writing, and Git operations through natural language—no commands to memorize!

## Quick Summary

- **Setup:** One-time project and Git initialization
- **Research & Plan:** Claude searches and creates your outline
- **Draft:** Claude writes the paper
- **Revise:** You add your voice, Claude improves sections
- **Commit:** Save work at each phase with "commit these changes"
- **Safety:** Return to any previous version anytime

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 9, 2025.
