# Vibe Tutorials Documentation

This repository contains comprehensive beginner-friendly tutorials for using Claude Code, VS Code, and related development tools. All tutorials are designed for complete beginners with no prior coding experience.

## Learning Paths

The tutorials follow a progression shown in the interactive graph on `index.html`. Here are the recommended sequences:

### Windows - Basic Path (Research & Writing)
1. `Install_CLAUDE_Code_Win.md` - Install Claude Code via WSL
2. `Claude_Code_Basic_Operations.md` - Essential Claude Code operations
3. `VS_Code_Getting_Started.md` - VS Code basics for beginners
4. `Claude_Code_in_VS_Code_Win.md` - Connect VS Code to Claude Code
5. `Writing_Research_Paper_Claude_Code.md` - Complete research paper workflow
6. `Reuse_Prompts_via_Slash_Commands.md` - Create custom slash commands
7. `Create_Your_First_Claude_Skill.md` - Build your first Claude skill
8. `Medical_Research_Skill.md` - Medical research with Claude skills
9. `Create_subagents.md` - Build autonomous agents

**Alternative Windows paths:**
- `Claude_Code_Git_Windows.md` - Local version control (branch from step 1)
- `Claude_Code_WSL_RStudio_Windows.md` - Use RStudio with Claude Code (branch from step 1)

### Mac - Basic Path (Research & Writing)
1. `Install_Claude_Code_MacOS.md` - Install Claude Code on macOS
2. `Claude_Code_Basic_Operations.md` - Essential Claude Code operations
3. `VS_Code_Getting_Started.md` - VS Code basics for beginners
4. `Claude_Code_in_VS_Code_Mac.md` - Connect VS Code to Claude Code
5. `Writing_Research_Paper_Claude_Code.md` - Complete research paper workflow
6. `Reuse_Prompts_via_Slash_Commands.md` - Create custom slash commands
7. `Create_Your_First_Claude_Skill.md` - Build your first Claude skill
8. `Medical_Research_Skill.md` - Medical research with Claude skills
9. `Create_subagents.md` - Build autonomous agents

**Alternative Mac paths:**
- `Claude_Code_Git_Mac.md` - Local version control (branch from step 1)
- `Claude_Code_RStudio_Mac.md` - Use RStudio with Claude Code (branch from step 1)

### R Coding Path
**Main Path (Docker + VS Code):**
1. Install Claude Code (`Install_CLAUDE_Code_Win.md` or `Install_Claude_Code_MacOS.md`)
2. `VS_Code_Getting_Started.md` - VS Code basics
3. `R_Coding_VS_Code_Guide.md` - Set up R development in VS Code
4. `R_Coding_Docker_Guide.md` - R in Docker containers for reproducibility
5. `Vibe_Coding_R_Docker_Guide.md` - Build an NBA dashboard with vibe coding

**Supporting Skills (branch from step 1):**
- `Github_desktop.md` - Version control basics with GitHub Desktop
- `GitHub_Desktop_Claude_Code_Workflow.md` - Integrated development workflow

**Alternative R Paths:**
- **RStudio on Mac:** Install → `Claude_Code_RStudio_Mac.md`
- **RStudio on Windows:** Install → `Claude_Code_WSL_RStudio_Windows.md`
- **Claude Code + R (Mac only):** R in VS Code → `Claude_Code_R_VS_Code_Mac.md`

### Python Coding Path
**Main Path (Docker + VS Code):**
1. Install Claude Code (`Install_CLAUDE_Code_Win.md` or `Install_Claude_Code_MacOS.md`)
2. `VS_Code_Getting_Started.md` - VS Code basics
3. `Python_Coding_VS_Code_Guide.md` - Set up Python development in VS Code
4. `Python_Coding_Docker_Guide.md` - Python in Docker containers
5. `Vibe_Coding_Python_Docker_Guide.md` - Vibe coding with Python and Streamlit

**Supporting Skills (branch from step 1):**
- `Github_desktop.md` - Version control basics with GitHub Desktop
- `GitHub_Desktop_Claude_Code_Workflow.md` - Integrated development workflow

**Alternative Python Path:**
- **Claude Code + Python (Mac only):** Python in VS Code → `Claude_Code_Python_VS_Code_Mac.md`

## Content Overview

### Installation Guides
- `Install_CLAUDE_Code_Win.md` - Windows installation via WSL2 with Ubuntu
- `Install_Claude_Code_MacOS.md` - macOS installation with Terminal

### VS Code Setup
- `VS_Code_Getting_Started.md` - Complete VS Code basics for beginners
- `Claude_Code_in_VS_Code_Win.md` - Running Claude Code in VS Code on Windows
- `Claude_Code_in_VS_Code_Mac.md` - Running Claude Code in VS Code on Mac

### Core Operations
- `Claude_Code_Basic_Operations.md` - Essential Claude Code commands and workflows

### Git & Version Control
- `Claude_Code_Git_Windows.md` - Git basics and local version control on Windows
- `Claude_Code_Git_Mac.md` - Git basics and local version control on Mac
- `Github_desktop.md` - GitHub Desktop for beginners
- `GitHub_Desktop_Claude_Code_Workflow.md` - Integrated Claude Code + GitHub workflow

### R Coding Guides
- `R_Coding_VS_Code_Guide.md` - R development environment in VS Code
- `R_Coding_Docker_Guide.md` - R in Docker containers for reproducibility
- `Vibe_Coding_R_Docker_Guide.md` - Building an NBA dashboard with Shiny
- `Claude_Code_RStudio_Mac.md` - Claude Code integration with RStudio on Mac
- `Claude_Code_WSL_RStudio_Windows.md` - Claude Code with RStudio on Windows via WSL
- `Claude_Code_R_VS_Code_Mac.md` - Streamlined R coding in VS Code on Mac

### Python Coding Guides
- `Python_Coding_VS_Code_Guide.md` - Python development environment in VS Code
- `Python_Coding_Docker_Guide.md` - Python in Docker containers
- `Vibe_Coding_Python_Docker_Guide.md` - Building a Streamlit dashboard with vibe coding
- `Claude_Code_Python_VS_Code_Mac.md` - Streamlined Python coding in VS Code on Mac

### Advanced Tutorials
- `Create_Your_First_Claude_Skill.md` - Creating custom Claude Code skills
- `Create_subagents.md` - Building specialized subagents for complex tasks
- `Reuse_Prompts_via_Slash_Commands.md` - Creating reusable slash commands
- `Medical_Research_Skill.md` - Using Claude Code for medical research

### Research & Writing Projects
- `Writing_Research_Paper_Claude_Code.md` - Complete academic writing workflow
- `example_paper.md` - Sample output from the research paper tutorial

## Available Skills

Claude Code skills extend functionality with specialized capabilities:

### Document Processing Skills
- **docx** - Microsoft Word document creation, editing, and analysis
- **pdf** - PDF manipulation, text extraction, form filling, and generation
- **pptx** - PowerPoint presentation creation, editing, and analysis
- **xlsx** - Excel spreadsheet creation, analysis, formulas, and visualization

### Research Skills
- **medical-research** - PubMed search and scientific literature summarization
- **generating-stock-reports** - Company research and stock analysis reports

### Data Analysis Skills
- **csv-stats** - CSV file statistics and data analysis

## Slash Commands

Custom commands available via `.claude/commands/`:

- `/tutorial [topic]` - Create a new beginner-friendly tutorial following the style guide
- `/review-tutorial [file]` - Review and polish an existing tutorial for clarity, accuracy, and formatting
- `/review-translation [file]` - Review and update Japanese translations to match English originals
- `/bioinfo-newsletter` - Generate a bioinformatics research newsletter from blog content

## Writing Style Guidelines

All tutorials follow these principles:

### Target Audience
- Complete beginners with no coding experience
- Non-technical users learning development tools
- Clear explanations without jargon

### Structure
- `[Home](./)` link at the top
- Engaging hook (2-4 sentences)
- Key Concepts section (3-4 terms max)
- What You'll Need (prerequisites + time estimate)
- Step-by-step instructions with `## Step N: Action Verb + What` format
- Next Steps section (2-3 suggestions)
- Troubleshooting section (2-3 common issues)
- Creation date and author at bottom

### Formatting
- Use bullet points (-) for sub-steps, not numbered lists
- Bold for UI elements: **Button Name**
- Backticks for commands: `command`
- Code blocks for multi-line commands
- Short paragraphs (2-3 sentences max)
- Menu-based instructions over keyboard shortcuts

### Length
- Target ~400 lines or less
- Focus on essential information
- Remove unnecessary explanations
- Keep it actionable and concise

## Japanese Translations

Complete Japanese translations are available in the `ja/` folder. All English tutorials have corresponding Japanese versions with the same filename structure:

- All installation guides
- All VS Code setup guides
- All coding guides (R and Python)
- All Git and GitHub guides
- All advanced tutorials
- Research and writing projects

Translation guidelines:
- Technical terms (Git, Docker, VS Code) kept in English
- Command-line instructions never translated
- UI elements match Japanese localization when applicable
- Natural, fluent Japanese using です/ます form
- Consistent terminology throughout

## File Structure

```
docs/
├── index.html                              # Landing page with tutorial graph
├── CLAUDE.md                               # This documentation file
├── _config.yml                             # Jekyll configuration
├── _layouts/                               # HTML templates
│   └── default.html
├── assets/                                 # Images and static files
├── ja/                                     # Japanese translations
│   ├── index.html
│   └── [all tutorials in Japanese]
│
├── Install_CLAUDE_Code_Win.md
├── Install_Claude_Code_MacOS.md
├── VS_Code_Getting_Started.md
├── Claude_Code_in_VS_Code_Win.md
├── Claude_Code_in_VS_Code_Mac.md
├── Claude_Code_Basic_Operations.md
├── Claude_Code_Git_Windows.md
├── Claude_Code_Git_Mac.md
├── Github_desktop.md
├── GitHub_Desktop_Claude_Code_Workflow.md
│
├── R_Coding_VS_Code_Guide.md
├── R_Coding_Docker_Guide.md
├── Vibe_Coding_R_Docker_Guide.md
├── Claude_Code_RStudio_Mac.md
├── Claude_Code_WSL_RStudio_Windows.md
├── Claude_Code_R_VS_Code_Mac.md
│
├── Python_Coding_VS_Code_Guide.md
├── Python_Coding_Docker_Guide.md
├── Vibe_Coding_Python_Docker_Guide.md
├── Claude_Code_Python_VS_Code_Mac.md
│
├── Create_Your_First_Claude_Skill.md
├── Create_subagents.md
├── Reuse_Prompts_via_Slash_Commands.md
├── Medical_Research_Skill.md
├── Writing_Research_Paper_Claude_Code.md
└── example_paper.md
```

## Contributing

When creating or updating tutorials:

1. Use the `/tutorial [topic]` command to create new tutorials
2. Use the `/review-tutorial [file]` command to review existing tutorials
3. Follow the writing style guidelines above
4. Keep tutorials focused and under 400 lines
5. Test all commands and instructions
6. Include troubleshooting for common issues
7. Add creation date and author attribution

## Additional Resources

- `.claude/commands/` - Slash command definitions
- `.claude/skills/` - Skill implementations
- `.devcontainer/` - Docker development container configuration
