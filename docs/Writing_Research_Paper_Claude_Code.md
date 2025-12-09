[Home](./)

# Writing a Research Paper with Claude Code

Write research papers using Claude Code as an assistant for research, brainstorming, planning, drafting and polishing. Use Git to track every version. 

## Key Concepts

- **Claude Code** - AI assistant that searches the web, organizes research, drafts content, and handles version control through simple requests
- **Git** - Tracks every change to your files, creating restore points (commits) you can return to anytime
- **Commit** - A snapshot of your project at a specific point in time with a description of what changed (e.g., "Add research notes", "Complete first draft")
- **Research Paper Workflow** - Research → Brainstorm → Focused Research → Plan → Draft → Revise manually → Polish with AI → Add Abstract → Proofread with AI  
- **Use AI as an assistant** for research, brainstorming, drafting, editing

## What You'll Need

- Claude Code installed ([installation guide](https://code.claude.com/docs/en/installation))
- Git installed (comes with Mac/Linux, [Windows guide](https://git-scm.com/download/win))
- Text editor (VS Code, TextEdit, Notepad, or any editor)
- Terminal access
- 35-45 minutes

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

## Step 2: Initial Research

Ask Claude to research your topic:

```
I'm writing a 2-page research paper on AI adoption in the workplace.
Search for recent data (2023-2025) on:
- Productivity gains from AI tools
- Job displacement concerns and statistics
- Real-world case studies from companies

Organize the findings with clear sections and cite all sources.
Prioritize peer-reviewed research and credible industry reports.
Avoid anecdotes and opinion pieces.
Save as general_research.md
```

Claude searches the web and organizes findings. Review `general_research.md` in your text editor. Then commit:

```
commit these changes
```

**First save point created!**

## Step 3: Brainstorm Your Angle

Read through the research and decide on your perspective. Ask Claude to help brainstorm:

```
Based on this research, brainstorm 3-4 different angles or perspectives
I could take for this paper. Save as brainstorm.md
```

Review the angles in your editor and pick the one that interests you most. Add a note in `brainstorm.md` marking your choice.

## Step 4: Focused Research

Now that you have your angle, ask Claude for targeted research:

```
I want to focus on [your chosen angle]. Search for more specific data
and examples that support this perspective. Save as focused_research.md
```

Claude finds targeted information. Commit your work:

```
commit these changes
```

**Second save point created!**

## Step 5: Create Your Plan

Ask Claude to create an outline based on your chosen angle:

```
Create a brief outline for my 2-page paper based on the focused
research and my chosen angle. Just give me main points for each paragraph in bullet points.
Structure it with:

1. Introduction
   - Hook to grab attention
   - Background context (2-3 sentences)
   - Clear thesis statement

2. Main Body (2-3 sections)
   - Each section with a clear argument
   - Key statistics/evidence to include
   - Specific examples from the research

3. Conclusion
   - Summary of main points
   - Implications or call to action

For each section, note which sources [1], [2], etc. to cite.
Aim for approximately 1,400 words total.
```

Review the outline and **prompt to adjust** as needed. Then commit:

```
commit these changes
```

**Third save point created!**

## Step 6: Draft the Paper

Ask Claude to write the full draft:

```
Using the outline and research, write a complete 2-page technical
report in paper.md.

Writing Style:
- Clear and concise prose
- Short, direct sentences (15-20 words average)
- Analytical and objective tone
- Active voice where possible

Content Requirements:
- Strong opening hook in the introduction
- Statistics woven naturally into prose (not bullet lists)
- Concrete examples from the research to illustrate key points
- Smooth transitions between sections
- Each paragraph should have a clear topic sentence

Citations and References:
- Add numbered references [1], [2], etc. for all citations
- Place citations after relevant statements or quotes
- 5-20 references
- Create a "References" section at the end with full source details
- List references in order [1], [2], [3]...

Length: Approximately 1,400 words (fits 2 pages with standard formatting)

Save as paper.md
```

Claude writes the draft. Commit:

```
commit these changes
```

**Fourth save point created!**

## Step 7: Revise Manually

Open `paper.md` in your text editor. Read through carefully and make your own revisions:
- Add your personal voice and insights
- Adjust arguments to match your thinking
- Fix any awkward phrasing
- Ensure citations are accurate

Save your changes after editing, then commit:

```
commit these changes
```

**Fifth save point created!**

## Step 8: Polish with AI

Ask Claude to improve specific sections:

```
Make the introduction more engaging with a compelling hook.
```

```
Strengthen the conclusion with a clear call to action.
```


Review Claude's changes. If satisfied, commit:

```
commit these changes
```

**Sixth save point created!**

## Step 9: Add an Abstract

Ask Claude to add a short executive summary at the beginning:

```
Add an abstract at the beginning of the paper. Write 4-5 sentences
that summarize the main argument, key findings, and conclusion.
```

Claude will add the abstract. Review to ensure it accurately captures your paper's essence. Then commit:

```
commit these changes
```

**Seventh save point created!**

## Step 10: Proofread with AI

Ask Claude to do a final proofread:

```
Do a final proofread of paper.md:
- Fix any spelling and grammar errors
- Ensure consistent formatting throughout
- Verify all reference numbers [1], [2]... match the References section
- Improve any awkward sentences for better flow
```

Review Claude's changes, then commit the final version:

```
commit these changes
```

**Final version saved!**

To view your complete writing journey anytime, type: `show my commit history`

## Step 11: Create a Slash Command for Future Papers

Save this workflow as a reusable slash command for your next research paper:

```
Create a slash command called /research-paper that guides me through
this entire workflow: initial research, brainstorm angles, focused
research, create outline, draft paper with references, manual revision,
AI polish, add abstract, and AI proofread. Save it so I can use it for
future research papers.
```

Claude will create a custom slash command in your `.claude/commands/` folder. Now you can start your next research paper by simply typing `/research-paper [your topic]`!

## The Complete Workflow

1. **Research** - Claude searches for general information on your topic
2. **Brainstorm** - Review findings and pick your angle/perspective
3. **Focused Research** - Claude finds targeted data for your chosen angle
4. **Plan** - Claude creates a detailed outline based on your perspective
5. **Draft** - Claude writes the full paper with references
6. **Revise Manually** - You add your voice and make changes
7. **Polish with AI** - Claude improves specific sections
8. **Add Abstract** - Claude creates executive summary
9. **Proofread with AI** - Claude fixes errors and improves flow
10. **Commit** - Save at each phase to create restore points
11. **Create Slash Command** - Save the workflow for future papers

Version control means you can experiment fearlessly—return to any previous version anytime.

## Next Steps

Now that you have the `/research-paper` slash command, try writing more papers:

- **Technology topics:** `/research-paper "Impact of social media on teen mental health"`
- **Business topics:** `/research-paper "Remote work productivity"`
- **Science topics:** `/research-paper "CRISPR gene editing ethics"`
- **Longer papers:** Tell Claude to create a 5-page paper with more detailed sections

The slash command will guide you through the entire workflow automatically!

Remember: Research → Brainstorm → Focused Research → Plan → Draft → Revise Manually → Polish with AI → Add Abstract → Proofread with AI → Save as Slash Command. Commit after each phase.

## Troubleshooting

- **"not a git repository" error:** Make sure you're in your project folder (`cd ~/Documents/ai-workplace-research`)
- **Claude search results seem outdated:** Specify "search for 2024-2025 data on [topic]"
- **Draft is too long/short:** Tell Claude: "Make this 2 pages, approximately 1400 words"
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

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 9, 2025.
