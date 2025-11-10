## Vibe Coding in VS Code + Docker Container for R

This minimal setup enables both Claude Code and OpenAI's Codex to run inside a Docker container. To support Shiny apps, we use the [rocker/shiny-verse](https://rocker-project.org/images/versioned/shiny.html) image.   A more advanced version for general development is provided by [Claude](https://code.claude.com/docs/en/devcontainer).

0. (Windows only) Install WSL2 (Windows Subsystem for Linux 2)
  
   -  Start Windows PowerShell as an **Administrator**. From Windows search bar, type **PowerShell** to find the Windows PowerShell app. And then select **Run as an Administrator**. For details, see [here](https://www.howtogeek.com/742916/how-to-open-windows-powershell-as-an-admin-in-windows-10/).
   -  Enable [Windows Subsystem for Linux 2 (WSL2).](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

1. Install Docker Desktop. Start it and let it run in the background.

2. Install GitHub Desktop. Login. 

3. Clone your project repo locally to a folder (C:\work\myproject). Create a repo for new project.

4. Install VS Code. 

5. Install Dev Containers extension on VS Code

6. From GitHub Desktop, clone this repo locally to a different folder (C:\work\vibe).

7. Copy the .devcontainer folder from the vibe repo (C:\work\vibe) to your repo (C:\work\myproject). Copy the entire folder. It has two files. The Dockerfile defines the container image, and the devcontainer.json includes settings.

8. Start VS Code. File --> Open Folder--> (C:\work\myproject).   When prompted, click “Reopen in Container”. 

9. Open a terminal in VS Code, and type in ```claude``` to start Claude Code. Login through the browser. I recommend create a Claude.me file first.

10. Install OpenAI's Codex extension to VS Code. Login in using your ChatGPT credentials. 

To update Claude Code, go to Docker Desktop. Select Containers from the left sidebar. Find the container and click on the three dots (...). Select "|> Open in Terminal". And paste this command 
```
npm install -g @anthropic-ai/claude-code
```

From this terminal, you can also install R packages. To install lots of packages to the Docker image, put these R commands in a file called packages.R and saved it to project folder (C:\work\myproject). And uncomment these two lines of code in Dockerfile. 
```COPY ./packages.R /tmp/packages.R
#RUN Rscript /tmp/packages.R
```

To test Shiny apps, open a new terminal in VS Code. Start R by typing ```R```. Then select all the code in the app.R and use Ctrl+Enter. When prompted, click on the link such as http://127.0.0.1:6778/, which is open in a web browser.


