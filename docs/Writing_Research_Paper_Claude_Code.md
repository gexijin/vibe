[Home](./)

# Writing a Research Paper with Claude Code

Write research papers using Claude Code as an assistant for research, brainstorming, planning, drafting, and editing. Use Git to track every version. See an [example paper](./example_paper.md) created using this workflow.

## Key Concepts

- **Research Paper Workflow** - Research → Brainstorm → Focused Research → Outline → Draft → Revise manually → Polish with AI → Add Abstract → Improve Title → Check references → Proofread with AI  
- **AI assistant** - Human makes key decisions while AI does the tedious work
- **Claude Code** - Agentic AI system that searches the web, organizes research, drafts content, and handles version control through simple requests
- **Git** - Tracks every change to your files, creating restore points (commits) you can return to anytime

## What You'll Need

- Claude Code installed ([Windows guide](./Install_CLAUDE_Code_Win.md) | [Mac guide](./Install_Claude_Code_MacOS.md))
- Git installed (comes with Mac/Linux, [Windows guide](https://git-scm.com/download/win))
- VS Code installed ([download](https://code.visualstudio.com/))
- Terminal access
- 45-60 minutes

## Step 1: Set Up Project and Start Claude Code

If you've completed the [Windows tutorial](./Claude_Code_Git_Windows.md) or [Mac tutorial](./Claude_Code_Git_Mac.md), you already have Git configured and can skip the `git config` commands below.

First, navigate to a user folder. 

**Windows (WSL Ubuntu):**
```bash
cd /mnt/c/Users/YOUR_USERNAME/Documents
```
Replace `YOUR_USERNAME` with your actual Windows username. (To find it, type `whoami` in the terminal—it shows after the backslash.) 

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

**First save point created!** A commit is a snapshot of your work—like a save point in a video game. You can always return to this exact version later. 

## Step 3: Read the Sources
Read through the research document and click through to the original sources to verify the information. Open the file in **VS Code**:
1. Go to File → **Open Folder** → navigate to the `ai_research` folder
2. Click `general_research.md` in the Explorer panel on the left
3. Preview the formatted document: **Ctrl + Shift + V** (Windows/Linux) or **Cmd + Shift + V** (Mac)
4. Click the source links to read the original articles and studies

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
Give me 3 options for a brief outline for my paper based on the focused
research and my chosen angle. Use bullet points for the narrative flow.
Save as outlines.md
```

Review the outline and ask Claude to adjust as needed (e.g., "Make section 2 focus more on case studies" or "Add a section on limitations"). Then commit:

```
commit these changes
```

**Third save point created!** If you don't like the paper in the end, you can revert to this point to start over with a different outline. 

## Step 7: Draft the Paper

Select your outline and ask Claude to write the full draft:

```
I like outline #2 [your chosen option].

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

Save your changes, then commit:

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

**Sixth save point created!**

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

**Seventh save point created!**

## Step 11: Improve Title

Ask Claude to give you a few options for the title:

```
Give me a few options for the title. Make it more appealing.
```

Select a title. Add your own touch. Edit the paper and commit:

```
I like option #2 [your choice]. Edit the file and commit.
```

**Eighth save point created!**

## Step 12: Check References (Optional)
Ask Claude to verify your citations are consistent and complete:
```
Check all references in my paper:
- Verify each citation number [1], [2], etc. has a matching reference
- Verify each reference in the list is actually cited in the paper
- Check that author names and titles are consistent
- Verify the cited data and examples appear in the source
```

Note: Claude can only verify publicly accessible sources. For paywalled articles, manually check that your citations match what you read.

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

**Final version saved!**

To view your complete writing journey, type: `show my commit history`

**Export to Word:** In VS Code, open the markdown preview with **Ctrl + Shift + V** (Windows/Linux) or **Cmd + Shift + V** (Mac). Click inside the preview pane, press **Ctrl + A** (or **Cmd + A** on Mac) to select all, then **Ctrl + C** (or **Cmd + C**) to copy. Paste into Microsoft Word—the formatting will be retained.

## The Complete Workflow

1. **Research** - Claude searches for general information on your topic
2. **Read Sources** - Review the research in VS Code
3. **Brainstorm** - Pick your angle/perspective
4. **Focused Research** - Claude finds targeted data for your chosen angle
5. **Plan** - Claude creates outline options based on your perspective
6. **Draft** - Claude writes the full paper with references
7. **Revise Manually** - You add your voice and make changes
8. **Polish with AI** - Claude improves specific sections
9. **Add Abstract** - Claude creates executive summary
10. **Improve Title** - Claude suggests title options, you customize
11. **Check References** - (Optional) Claude verifies all citations
12. **Proofread with AI** - Claude fixes errors and improves flow

Commit at each phase to create restore points. Version control means you can experiment fearlessly—return to any previous version anytime.

## Next Steps

Try writing more papers on different topics:

- **Technology:** "Impact of social media on teen mental health"
- **Business:** "Remote work productivity"
- **Science:** "CRISPR gene editing ethics"
- **Longer papers:** Tell Claude to create a 5-page paper with more detailed sections

## Advanced: Create a Slash Command (Optional)

Once you're comfortable with the workflow, you can save it as a reusable command:

```
Create a slash command called /research-paper that guides me through
this entire workflow. Save it so I can use it for future research papers.
```

Claude will create a custom slash command in your `.claude/commands/` folder. Then start future papers by typing `/research-paper [your topic]`.

## Troubleshooting

- **"not a git repository" error:** Make sure you're in your project folder (`cd ~/Documents/ai_research` or equivalent)
- **Claude search results seem outdated:** Specify "search for 2024-2025 data on [topic]"
- **Draft is too long/short:** Tell Claude: "Make this approximately 1,000 words"
- **Can't find files:** In terminal, type `ls` to list all files in current folder
- **Want to see what changed:** In Claude Code, type `show me what changed since last commit`

## What You Can Ask Claude

- `search for more recent statistics on [topic]` - Find newer data
- `summarize the key arguments in this paper` - Get overview
- `make the conclusion more persuasive` - Improve specific sections
- `cite all sources in APA format` - Format references
- `go back to the previous commit` - Undo all changes since last commit

Claude handles research, writing, and Git operations through natural language—no commands to memorize!

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 9, 2025.
