[Home](./)

# Writing a Research Paper with Claude Code

Write research papers using Claude Code as an assistant for research, brainstorming, planning, drafting and polishing. Use Git to track every version. 

## Key Concepts

- **Use AI as an assistant** for research, brainstorming, drafting, editing
- **Research Paper Workflow** - Research → Brainstorm → Focused Research → Plan → Draft → Revise manually → Polish with AI → Add Abstract → Improve Title → Proofread with AI  
- **Claude Code** - AI assistant that searches the web, organizes research, drafts content, and handles version control through simple requests
- **Git** - Tracks every change to your files, creating restore points (commits) you can return to anytime


## What You'll Need

- Claude Code installed ([installation guide](https://code.claude.com/docs/en/installation))
- Git installed (comes with Mac/Linux, [Windows guide](https://git-scm.com/download/win))
- Text editor (VS Code, TextEdit, Notepad, or any editor)
- Terminal access
- 35-45 minutes

## Step 1: Set Up Project and Start Claude Code

If you've completed the [Windows tutorial](./Claude_Code_Git_Windows.md) or [Mac tutorial](./Claude_Code_Git_Mac.md), you already have Git configured. 
First, we navigate to a user folder. 

**Windows (WSL Ubuntu):**
```bash
cd /mnt/c/Users/YOUR_USERNAME/Documents
```
Replace `YOUR_USERNAME` with your actual Windows username. 

**Mac:**
```bash
cd ~/Documents
```

**Linux, or running inside Docker:**
```bash
cd ~
```

For all platforms, we create a new project folder for your research paper.
We also configure git for version control before starting Claude Code.

```
mkdir ai_research
cd ai_research
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
claude
```
Git is now tracking changes in this folder. Claude Code is ready.

## Step 2: Initial Research

Ask Claude to research your topic:

```
I'm writing a ~1,000 word research paper on AI adoption in the workplace.
Search for recent data (2023-2025) on:
- Productivity gains from AI tools
- Job displacement concerns and statistics
- Real-world case studies from companies

Requirements:
- Prioritize peer-reviewed research and credible industry reports
- Avoid anecdotes and opinion pieces
- List each source with a 1-3 sentence summary
- Group sources by topic

Save as general_research.md
```

Claude searches the web and organizes findings. Review `general_research.md` in your text editor. Then commit:

```
commit these changes
```

**First save point created!** 

## Step 3: Read the sources.
Read through the research document by openning it in a text Editor such as **Visual Studio Code**.  It includes a built-in markdown preview feature.
- Install VS Code 
- Go to File and then select **Open Foler**
- Navigate to the ai_research folder and click to open
- Click to open the general_research.md file from the EXPLORER on the top left. 
- Ctrl + Shift + V to preview

## Step 4: Brainstorm Your Angle

Ask Claude to help brainstorm:

```
Based on this research, suggest 3-4 angles I could take for this paper.
```

Review the angles and pick the one that interests you most. 

## Step 5: Focused Research

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

## Step 6: Create Your Plan

Ask Claude to create an outline based on your chosen angle:

```
Give me 3 options for an brief outline for my paper based on the focused
research and my chosen angle.  Use bullet points for the narrative flow.
Save as outlines.md

```

Review the outline and **prompt to adjust** as needed. Then commit:

```
commit these changes
```

**Third save point created!** If we don't like the paper in the end, we can revert to this point to start over with a different option. 

## Step 7: Draft the Paper

Select your outline and ask Claude to write the full draft:

```
I like outline [ #2, your chosen option ]. 

Write a ~1,000 word research paper based on the outline and research.

Structure:
- Introduction: Hook, context, thesis statement
- Body: 2-3 sections with arguments, statistics, and examples
- Conclusion: Summary and implications

Style:
- Clear, concise sentences (15-20 words average)
- Active voice, analytical tone
- Statistics woven into prose (no bullet lists)
- Smooth transitions between paragraphs

Citations:
- Use numbered references [1], [2], etc. after claims
- Include 5-15 references
- Add a References section at the end

Save as paper.md
```

Claude writes the draft. Commit:

```
commit these changes
```

**Fourth save point created!**

## Step 8: Revise Manually

Open `paper.md` in your text editor. Read through carefully and make your own revisions:
- Add your personal voice and insights
- Adjust arguments to match your thinking
- Fix any awkward phrasing
- Ensure citations are accurate

Save your changes after editing each paragraph, then commit:

```
commit these changes
```

**Fifth save point created!**

## Step 9: Polish with AI

Ask Claude to improve specific sections:

```
Make the introduction more engaging with a compelling hook.
```

```
Strengthen the conclusion with a clear call to action. Do not increase its overall length.
```


Review Claude's changes. If satisfied, commit:

```
commit these changes
```

## Step 10: Add an Abstract

Ask Claude to add a short executive summary at the beginning:

```
Add an abstract at the beginning of the paper. Write 2-3 short sentences
that summarize the paper.
```

Claude will add the abstract. Review and edit to ensure it accurately captures your paper's essence. Then commit:

```
commit these changes
```



## Step 11: Improve Title

Ask Claude to give you a few options for the title:

```
Give me a few options for the title. Make it more appealing.
```

Select a title. Add your own touch. Edit the paper and commit:

```
I like option #XXX. Edit the file and commit.
```

## Step 12: Check references (Optional)
Ask Claude to check and verify all references.
```
Check all references. For each listed reference:
- Read it again using the link 
- Make sure citation information is correct
- The cited data, example, and other information are in the source
- Make sure all the listed references are cited.
- Make sure all the citation numbers ([1], [2], etc.) in the paper has a corresponding reference
```

## Step 13: Proofread with AI

Ask Claude to do a final proofread:

```
Do a final proofread of the paper:
- Fix any spelling and grammar errors
- Ensure consistent formatting throughout
- Check flow and transition
```

Review Claude's changes, then commit the final version:

```
commit these changes
```

In VS Code, you can preview the Markdown file by Ctrl + Shift + V. In the preview mode, you can select the entire paper, and copy. Then paste to Microsoft Word. The format will be retained. 

## Step 14: Create a Slash Command for Future Papers

Save this workflow as a reusable slash command for your next research paper:

```
Create a slash command called /research-paper that guides me through
this entire workflow. Save it so I can use it for future research papers.
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
9. **Improve Title** - Claude suggests title options, you customize
10. **Proofread with AI** - Claude fixes errors and verifies references
11. **Create Slash Command** - Save the workflow for future papers
12. **Commit** - Save at each phase to create restore points

Version control means you can experiment fearlessly—return to any previous version anytime.

## Next Steps

Now that you have the `/research-paper` slash command, try writing more papers:

- **Technology topics:** `/research-paper "Impact of social media on teen mental health"`
- **Business topics:** `/research-paper "Remote work productivity"`
- **Science topics:** `/research-paper "CRISPR gene editing ethics"`
- **Longer papers:** Tell Claude to create a 5-page paper with more detailed sections

The slash command will guide you through the entire workflow automatically!

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
