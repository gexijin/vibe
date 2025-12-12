# Vibe Tutorials Documentation

This folder contains beginner-friendly tutorials for using Claude Code, VS Code, and related tools.

## Learning Paths

The tutorials follow a progression shown in the interactive graph on `index.html`. Here are the recommended sequences:

### Windows - Basic Path (Research & Writing)
1. `Install_CLAUDE_Code_Win.md` - Install Claude Code via WSL
2. `VS_Code_Getting_Started.md` - VS Code basics
3. `Claude_Code_in_VS_Code_Win.md` - Connect VS Code to Claude Code
4. `Claude_Code_Git_Windows.md` - Local version control
5. `Writing_Research_Paper_Claude_Code.md` - Research paper workflow

### Mac - Basic Path (Research & Writing)
1. `Install_Claude_Code_MacOS.md` - Install Claude Code
2. `VS_Code_Getting_Started.md` - VS Code basics
3. `Claude_Code_in_VS_Code_Mac.md` - Connect VS Code to Claude Code
4. `Claude_Code_Git_Mac.md` - Local version control
5. `Writing_Research_Paper_Claude_Code.md` - Research paper workflow

### R Coding Path
1. Install Claude Code (Windows or Mac)
2. `VS_Code_Getting_Started.md` - VS Code basics
3. `R_Coding_VS_Code_Guide.md` - Set up R in VS Code
4. `R_Coding_Docker_Guide.md` - R in Docker containers
5. `Github_desktop.md` - Version control basics
6. `GitHub_Desktop_Claude_Code_Workflow.md` - Combined workflow
7. `Vibe_Coding_R_Docker_Guide.md` - Build an NBA dashboard with vibe coding

**Alternative R paths:**
- `Claude_Code_RStudio_Mac.md` - Use Claude Code with RStudio on Mac
- `Claude_Code_WSL_RStudio_Windows.md` - Use Claude Code with RStudio on Windows
- `Claude_Code_R_VS_Code_Mac.md` - Claude Code for R in VS Code (Mac)

### Python Coding Path
1. Install Claude Code (Windows or Mac)
2. `VS_Code_Getting_Started.md` - VS Code basics
3. `Python_Coding_VS_Code_Guide.md` - Set up Python in VS Code
4. `Python_Coding_Docker_Guide.md` - Python in Docker containers
5. `Github_desktop.md` - Version control basics
6. `GitHub_Desktop_Claude_Code_Workflow.md` - Combined workflow
7. `Vibe_Coding_Python_Docker_Guide.md` - Vibe coding with Python

**Alternative Python path:**
- `Claude_Code_Python_VS_Code_Mac.md` - Claude Code for Python in VS Code (Mac)

## Content Overview

### Installation Guides
- `Install_CLAUDE_Code_Win.md` - Windows installation via WSL
- `Install_Claude_Code_MacOS.md` - macOS installation

### VS Code Setup
- `VS_Code_Getting_Started.md` - VS Code basics for beginners
- `Claude_Code_in_VS_Code_Win.md` - Running Claude Code in VS Code on Windows
- `Claude_Code_in_VS_Code_Mac.md` - Running Claude Code in VS Code on Mac

### Git Workflows
- `Claude_Code_Git_Windows.md` - Git integration on Windows
- `Claude_Code_Git_Mac.md` - Git integration on Mac
- `Github_desktop.md` - GitHub Desktop basics
- `GitHub_Desktop_Claude_Code_Workflow.md` - Combined workflow

### R Coding Guides
- `R_Coding_VS_Code_Guide.md` - R development in VS Code
- `R_Coding_Docker_Guide.md` - R in Docker
- `Vibe_Coding_R_Docker_Guide.md` - Vibe coding with R and Shiny
- `Claude_Code_RStudio_Mac.md` - Claude Code with RStudio on Mac
- `Claude_Code_WSL_RStudio_Windows.md` - Claude Code with RStudio on Windows
- `Claude_Code_R_VS_Code_Mac.md` - Claude Code for R in VS Code (Mac)

### Python Coding Guides
- `Python_Coding_VS_Code_Guide.md` - Python development in VS Code
- `Python_Coding_Docker_Guide.md` - Python in Docker
- `Vibe_Coding_Python_Docker_Guide.md` - Vibe coding with Python
- `Claude_Code_Python_VS_Code_Mac.md` - Claude Code for Python in VS Code (Mac)

### Projects
- `Writing_Research_Paper_Claude_Code.md` - Research paper workflow
- `example_paper.md` - Sample output from the research paper tutorial

## Writing Style

- Target audience: Complete beginners with no coding experience
- Use step-by-step instructions with explicit clicks and menu navigation
- Avoid keyboard shortcuts; prefer menu-based instructions
- Include "What You'll Need" and time estimates at the start
- Add troubleshooting sections for common issues
- Link back to Home (./) at the top of each tutorial

## Slash Commands

Custom commands in `.claude/commands/`:

- `/tutorial [topic]` - Create a new beginner-friendly tutorial following the style guide
- `/review-tutorial [file]` - Review and polish an existing tutorial for clarity, accuracy, and formatting
- `/bioinfo-newsletter` - Generate a bioinformatics research newsletter from blog content

## File Structure

- `index.html` - Landing page with interactive tutorial graph
- `_config.yml` - Jekyll configuration
- `_layouts/` - HTML templates
- `assets/` - Images and static files
- `ja/` - Japanese translations
