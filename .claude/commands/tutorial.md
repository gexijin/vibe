# Create a Beginner Tutorial

Create a beginner-friendly tutorial for: $ARGUMENTS

## Before Writing

**Search the web first** to get the most current information:
- Latest version numbers and download links
- Current best practices and recommended approaches
- Up-to-date installation methods
- Any recent changes to tools or interfaces

## Tutorial Structure

### 1. Title
- Clear, descriptive title (e.g., "Installing Claude Code on Windows Using WSL")

### 2. Hook
- One relatable problem scenario (2-3 sentences)
- One simple analogy
- Why this matters (1 sentence)

### 3. Key Concepts
- Define only essential terms (3-4 max)
- One sentence per concept
- Bold the term, then explain simply

### 4. Overview
- Bullet list summarizing the main steps (5-8 items)
- Gives readers a roadmap of what's coming
- Example:
  ```
  - Install WSL (Windows Subsystem for Linux)
  - Set up Ubuntu Linux
  - Install Node.js
  - Ready to use!
  ```

### 5. What You'll Need (Prerequisites)
- System requirements (OS version, hardware)
- Required accounts or subscriptions
- Internet connection, admin access, etc.
- Keep to 3-5 items

### 4. Step-by-Step Instructions
Each step should be a major phase (Step 1, Step 2, etc.):

**Step title format:** `## Step N: Action Verb + What`

**Within each step include:**
- Numbered sub-steps (1, 2, 3...)
- Exact actions: "Click **Button Name**" or "Type `command`"
- Code blocks for any commands:
  ```
  command here
  ```
- **What you'll see:** Describe the visual result ("A blue window will open")
- **Why this matters:** Brief explanation when the reason isn't obvious
- **If/Then guidance:** Handle common variations
  - "**If it says 'Enabled':** Continue to Step 2"
  - "**If it says 'Disabled':** You need to..."
- **Notes:** Call out important info with `**Note:**`
- **Wait times:** Tell users how long things take ("This may take 5-10 minutes")

**For steps with multiple options:**
```
### Option A: First approach
[instructions]

### Option B: Alternative approach
[instructions]
```

### 5. How to Return/Reopen
- Show users how to get back to the tool after closing
- Step-by-step instructions to reopen

### 6. Troubleshooting
- Use exact error messages as headers (in quotes)
- Provide specific solutions
- Format:
  ```
  ### "Error message here"
  - What this means
  - How to fix it
  ```

### 7. Need Help?
- Links to official documentation
- Links to community resources or GitHub issues

## Writing Rules

**Be explicit for beginners:**
- Describe exactly what to click ("**Right-click** on the taskbar")
- Explain what users will see ("You'll see text appearing as Windows downloads...")
- Never assume prior knowledge
- Explain security behaviors ("you won't see characters as you type - this is normal")

**Be actionable:**
- Every step produces a visible result
- Tell them exactly what to click/type
- Show what success looks like

**Be current:**
- Use latest version numbers from web search
- Use current download links
- Note if something recently changed

**Format for scanning:**
- Short paragraphs (2-3 sentences max)
- Bullet points over prose
- Headers to break up sections
- Code blocks for all commands
- Bold for UI elements: **Button Name**, **Menu Item**
- Backticks for commands: `command here`

**Include timing expectations:**
- "This process may take 5-15 minutes"
- "Wait 2-5 minutes for the window to appear"
- "Your computer will restart - this takes about 1-2 minutes"

## Output

Save the tutorial in the `doc/` folder with a descriptive filename using the pattern `Install_TOOLNAME_PLATFORM.md` or `TOPIC_GUIDE.md` (e.g., `doc/Install_Docker_Mac.md`, `doc/Git_Basics_Guide.md`). Create the folder if it doesn't exist.
