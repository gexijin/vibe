# choose a Dockerhub base image with R, Shiny Server, and tidyverse packages
FROM rocker/shiny-verse:latest

# 1. System deps commonly needed by R packages
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# 2. R packages for VS Code integration: language server + debugger
RUN R -q -e 'install.packages(c("rstudioapi", "languageserver"), repos="https://cloud.r-project.org")'

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest
    
# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Additional R packages can be installed through a packages.R file
#COPY ./packages.R /tmp/packages.R
#RUN Rscript /tmp/packages.R

# Expose Shiny server port
EXPOSE 3838