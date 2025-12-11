[Home](./)

# Vibe Coding in R with Claude Code and Docker

You've written R code by typing every line yourself. But what if you could describe what you want in plain English and watch the code appear? Vibe coding is like having a conversation with your computer—you describe the outcome, Claude Code builds it, you test and refine. It's not magic; it's a new way to work where you guide the vision and AI handles the implementation. This tutorial shows you how to build a real NBA stats dashboard using nothing but natural language requests.

## Key Concepts

- **[Vibe Coding](https://www.ibm.com/think/topics/vibe-coding)** - Programming by describing what you want in natural language, then iterating based on results rather than writing code line-by-line
- **[Claude Code](https://code.claude.com/)** - AI coding assistant that writes, debugs, and refactors code based on your natural language requests
- **[hoopR](https://hoopr.sportsdataverse.org/)** - R package that provides easy access to NBA player statistics and game data
- **Iterative refinement** - The core vibe coding pattern: describe → test → refine → commit working versions

## What You'll Need

- Finished [R Coding in VS Code via Docker](./R_Coding_Docker_Guide)
- Finished [Using GitHub Desktop with Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 25-30 minutes

## Step 1: Create New GitHub Repository

- Open GitHub Desktop
- Click **File > New Repository**
- Fill in the details:
  - **Name:** `nba-dashboard`
  - **Description:** `NBA stats dashboard built with vibe coding`
  - **Local Path:** Choose a location (e.g., Documents or work folder)
  - Check **Initialize this repository with a README**
- Click **Create Repository**
- Click **Publish repository** at the top
- Uncheck **Keep this code private** if you want it public (optional)
- Click **Publish Repository**

You now have a local Git repository and a backup on GitHub.

## Step 2: Copy Docker Configuration

You need the `.devcontainer` folder from the vibe project to set up your Docker environment.

- Open File Explorer (Windows) or Finder (Mac)
- Navigate to your vibe project folder (e.g., `Documents/vibe`)
- Find the `.devcontainer` folder
- Copy the entire folder (it contains `Dockerfile` and `devcontainer.json`)
- Navigate to your new `nba-dashboard` folder
- Paste the `.devcontainer` folder there

Your `nba-dashboard` folder should now contain:
- `.devcontainer/` (folder you just copied)
- `README.md` (created by GitHub Desktop)
- `.git/` (hidden folder for version control)

## Step 3: Open Project in Container

- Open VS Code
- Click **File > Open Folder**
- Navigate to `nba-dashboard` folder
- Click **Select Folder**
- A notification appears in the bottom right: **Folder contains a Dev Container configuration file**
- Click **Reopen in Container**
- If you don't see the notification, click the green icon in bottom-left corner and select **Reopen in Container**
- VS Code builds the Docker container (takes 3-5 minutes first time)
- Watch the progress notification showing build steps
- When complete, the green icon shows **Dev Container: R in Docker**

## Step 4: Start Claude Code

- In VS Code, click **Terminal > New Terminal**
- You're now inside the Docker container
- Type this command to start Claude Code:

```bash
claude
```

- A browser window opens for authentication
- Click **Continue with Google** or **Continue with Email**
- Log in with your Claude account (or create one)
- After authentication succeeds, return to VS Code terminal
- You'll see Claude's welcome message

Claude Code is now running and ready for your requests.


## Step 5: First Vibe - Get NBA Data

Now the fun begins. Instead of looking up documentation, just describe what you want.

- In the Claude Code terminal, type:

```
Install the hoopR package and load current NBA player statistics. Show me the top 10 players by total points scored this season. Display it as a nice table.
```

- Press Enter
- Watch Claude:
  - Install the hoopR package
  - Write R code to load data
  - Create a script to show top scorers
  - Run the code
- Review the output showing player names, teams, and points

You just used vibe coding! No searching documentation, no trial and error—just describe and test.

Ask Claude to commit using Git. Or do this yourself from GitHub Desktop.
```
Commit these changes.
```
## Step 6: Second Vibe - Explore the Data

Before building a dashboard, understand what data you have.

- In Claude Code terminal, type:

```
Show me what columns are available in this NBA data. Then create a summary showing: number of players, number of teams, average points per player, and who has the most assists and rebounds.
```

- Press Enter
- Claude explores the dataset and shows you interesting statistics
- Look at the output to see available columns like: player_name, team, points, assists, rebounds, field_goal_percentage, etc.

This exploration helps you decide what to put in your dashboard.

Ask Claude to commit using Git. Or do this yourself from GitHub Desktop.

## Step 7: Third Vibe - Create Basic Shiny App

Time to build the interactive dashboard.

- In Claude Code terminal, type:

```
Create a Shiny app in a file called app.R that shows an interactive table of NBA player stats. Include columns for player name, team, points, assists, and rebounds. Add a slider to filter players by minimum points scored (from 0 to 1000). Make it look clean and professional.
```

- Press Enter
- Claude creates `app.R` with a complete Shiny application
- Wait for Claude to finish writing the file

## Step 8: Run the Shiny App

Test your dashboard to see if it works.

- Look at the top right of the VS Code editor (where `app.R` is open)
- Find the **▶** button with a dropdown arrow
- Click the dropdown and select **Run Shiny App**
- The app starts and a notification appears: **Open in Browser**
- Click **Open in Browser**
- The NBA dashboard opens in your web browser
- Try moving the points slider—the table filters in real-time
- Scroll through the player data

If something doesn't work, copy any error messages and paste them to Claude to fix.

## Step 9: Fourth Vibe - Add Visualization

Tables are useful, but visualizations tell better stories.

- Back in Claude Code terminal, type:

```
Add a bar chart below the table showing the top 15 players by points. Use different colors for each player. Also add a scatter plot showing the relationship between points and assists for all filtered players.
```

- Press Enter
- Claude updates `app.R` with visualization code
- The Shiny app automatically reloads (or click **Run Shiny App** again)
- Refresh your browser
- You now see a colorful bar chart and scatter plot
- Move the slider—all visualizations update together

This is vibe coding in action: describe the feature, test it, iterate.

## Step 10: Fifth Vibe - Add Team Filter

Make the dashboard more interactive with team selection.

- In Claude Code terminal, type:

```
Add a dropdown menu to filter players by team. Put it at the top. When I select a team, show only players from that team. Include an "All Teams" option to show everyone.
```

- Press Enter
- Claude adds the team filter
- Refresh your browser
- Test the dropdown—select different teams like Lakers, Warriors, Celtics
- Watch the table and charts update for each team

You're building a professional dashboard by having a conversation.

## Step 11: Review and Commit

Before committing, review what Claude built.

- In VS Code Explorer, click on `app.R` to open it
- Skim through the code—notice the UI layout, server logic, and plotting code
- You don't need to understand every line, but get a sense of the structure
- Open GitHub Desktop
- You'll see `app.R` listed as a new file
- The right panel shows all the code in green (new additions)
- In the **Summary** field at bottom left, type:

```
Create NBA dashboard with team filter and visualizations
```

- Click **Commit to main**
- Click **Push origin** to back up to GitHub

You've saved your first working version!

## Step 12: Iterate and Improve

Vibe coding shines when you iterate. Try adding features by describing them:

**Example requests to Claude:**

- "Add a player search box so I can type a player's name and jump to them"
- "Show the team logos next to team names in the dropdown"
- "Add a line chart showing points per game trend for the selected team"
- "Make the bar chart sortable by clicking column headers"
- "Add tooltips to the scatter plot showing player names when I hover"

After each successful feature:
- Test it in the browser
- If it works, commit with GitHub Desktop
- If it breaks, tell Claude the error and ask to fix it
- When fixed, commit the working version


**Key principles:**

- **Describe outcomes, not implementation** - Say "show top scorers" not "use arrange() and head()"
- **Iterate quickly** - Test → refine → test → refine
- **Commit working versions** - Save each success before trying new features
- **Embrace failures** - If Claude's code breaks, just describe the error and ask to fix it
- **Stay in control** - You decide features, priorities, and when it's good enough

Each time, follow the pattern: describe → test → iterate → commit.

## Next Steps

- **Apply to your domain** - Use vibe coding for your own data (research, business, hobbies)
- **Try other packages** - Ask Claude to use `nflfastR` for football or `worldfootballR` for soccer
- **Learn by asking** - When Claude writes code, ask "explain what this function does" to learn R
- **Share your dashboard** - Deploy to [shinyapps.io](https://www.shinyapps.io/) (ask Claude how)
- **Read about vibe coding** - Visit [IBM's guide](https://www.ibm.com/think/topics/vibe-coding) to learn more about this coding style

## Troubleshooting

- **hoopR installation fails** - Check your internet connection; the package downloads data from the web. Try running `install.packages("hoopR")` in an R terminal to see detailed error messages.
- **Shiny app won't start** - Verify the Shiny extension is installed (search "Posit.shiny" in VS Code Extensions). Check the terminal for error messages and paste them to Claude.
- **No data showing** - The hoopR package pulls live data; if NBA season hasn't started, there may be limited data. Ask Claude to use sample data or a previous season.
- **Claude makes mistakes** - Normal! Copy the error message, paste it to Claude, and say "fix this error." Vibe coding includes iteration and debugging.
- **Can't push to GitHub** - Make sure you're logged into GitHub Desktop and published the repository (Step 1). Check your internet connection.

## Workflow Overview

This tutorial combined several technologies into one workflow:

- **GitHub Desktop** - Version control with visual interface (create repos, commit, push)
- **Docker container** - Isolated R environment with all dependencies pre-installed
- **VS Code** - Code editor that connects to the Docker container
- **Claude Code** - AI assistant that writes R and Shiny code from your descriptions
- **hoopR package** - NBA data source with simple API
- **Shiny framework** - Interactive web apps in R

The magic isn't any single tool—it's how vibe coding lets you describe what you want and iterate rapidly. You went from empty project to working sports dashboard in 30 minutes without writing a single line of code manually.

## Everyday Workflow

After this initial setup, your daily vibe coding routine becomes:

1. **Start Docker Desktop** - Launch the app, wait for green status
2. **Open VS Code** - Open your project, reopen in container if needed
3. **Start Claude Code** - Type `claude` in the terminal
4. **Describe your goal** - "Add a feature that..." or "Fix the bug where..."
5. **Test the changes** - Run your app, check if it works
6. **Iterate or commit** - If broken, describe the fix; if working, commit with GitHub Desktop
7. **Push regularly** - Click **Push origin** to back up to GitHub

The more you practice, the better you get at describing what you want. Vibe coding is a skill—you learn what kinds of descriptions work best and how to break big ideas into testable pieces.

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
