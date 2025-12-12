# Use native multi-arch image (works on ARM64 and AMD64)
# Note: rocker/shiny-verse has limited ARM64 support because Shiny Server
# doesn't distribute ARM64 binaries. Use rocker/r-ver instead.
FROM rocker/r-ver:4.4.3

# 1. Configure Posit Package Manager for prebuilt ARM64 binaries
# This dramatically speeds up package installation (minutes instead of 30+ min)
RUN echo 'options(repos = c(CRAN = "https://packagemanager.posit.co/cran/__linux__/jammy/latest"))' >> /usr/local/lib/R/etc/Rprofile.site

# 2. System deps (still needed for some packages that compile from source)
RUN apt-get update && apt-get install -y \
    build-essential \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    libgit2-dev \
    libsodium-dev \
    libcairo2-dev \
    cmake \
    git \
    curl \
 && rm -rf /var/lib/apt/lists/*

# 3. Install tidyverse and shiny (dependencies=NA skips optional "Suggests" like otelsdk)
RUN R -e "options(warn = 2); install.packages(c('tidyverse', 'shiny'), dependencies = NA)"

# 4. R packages for VS Code integration: language server + debugger
RUN R -e "options(warn = 2); install.packages(c('rstudioapi', 'languageserver'))"

# 5. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 6. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 7. Additional R packages can be installed through a packages.R file
#COPY ./packages.R /tmp/packages.R
#RUN Rscript /tmp/packages.R

# 8. Give shiny passwordless sudo for updating Claude Code from VS Code
RUN echo 'shiny ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    rm -rf /var/lib/apt/lists/*
# Expose Shiny server port
EXPOSE 3838
