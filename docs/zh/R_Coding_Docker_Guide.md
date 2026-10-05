---
title: "通过 Docker 容器在 VS Code 中进行 R 编程"
lang: "zh"
---
[首页](./)

# 通过 Docker 容器在 VS Code 中进行 R 编程

曾经试图与同事分享 R 代码,却花费大量时间调试"在我机器上能跑"的问题?Docker 容器就像代码的集装箱——将 R 环境、库和依赖打包到密封容器中,在任何地方都能以相同方式运行。此外,[Docker Hub](https://hub.docker.com/) 上有数万个预构建镜像,开发者发布的即用环境,免去手动安装软件的麻烦。本教程将教你如何使用 VS Code 和 Docker Desktop 在隔离、可重现的环境中运行 R。

## 核心概念

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - 在计算机上运行容器的应用,管理隔离环境
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code 功能,允许在 Docker 容器内编写代码,具有完整 IDE 支持
- **容器隔离** - 代码在独立 Linux 环境中运行,只能看到项目文件夹,而非整个计算机
- **[Rocker](https://rocker-project.org/)** - 为 R 开发设计的预构建 Docker 镜像

## 准备工作

- 已完成 [R Coding in VS Code](./R_Coding_VS_Code_Guide)
- 已完成 [GitHub Desktop Basics](./Github_desktop)
- 20-25 分钟

## 步骤 1:安装 Docker Desktop

- 访问 [Docker Desktop 下载页面](https://www.docker.com/products/docker-desktop/)
- 点击 **Download for Windows**(或根据系统选择 Mac/Linux)
- 运行安装程序并按照向导操作
- 出现提示时,启用 WSL 2(Windows 用户)或接受默认设置
- 安装完成后,启动 Docker Desktop
- 等待 Docker 引擎启动(左下角显示绿色状态指示器)

## 步骤 2:安装 Dev Containers 扩展

- 打开 VS Code
- 点击左侧边栏的 **Extensions** 图标(或 **View > Extensions**)
- 在搜索框输入 `dev containers`
- 找到 Microsoft 的 **Dev Containers**
- 点击 **Install**

## 步骤 3:使用 GitHub Desktop 克隆 Vibe 项目

- 打开 GitHub Desktop
- 点击 **File > Clone repository**
- 点击 **URL** 选项卡
- 在 **Repository URL** 字段粘贴:`https://github.com/gexijin/vibe`
- 选择保存项目的位置(**Local Path** 字段)
- 点击 **Clone**
- GitHub Desktop 会将项目下载到所选位置

## 步骤 4:在 VS Code 中打开项目

- VS Code 中,点击 **File > Open Folder**
- 导航到刚克隆的 `vibe` 文件夹
- 点击 **Select Folder**
- 资源管理器侧边栏会显示项目文件

## 步骤 5:在容器中重新打开

- 查找右下角通知:**Folder contains a Dev Container configuration file**
- 点击 **Reopen in Container**
- 如果没看到通知,点击左下角绿色图标
- 从菜单选择 **Reopen in Container**
- VS Code 会构建容器(首次需 5-10 分钟)
- 会显示构建步骤的进度通知
- 完成后,绿色图标会显示 **Dev Container: R in Docker (AMD64)**

**注意:**容器自动包含 R 扩展和 languageserver 包。Dockerfile 和 devcontainer.json 会处理这些。

## 步骤 6:了解容器环境

现在你在 Linux 容器内编写代码。让我们探索一下这意味着什么。

- 点击 **Terminal > New Terminal** 在容器内打开终端
- 检查当前位置:

```bash
pwd
```

会看到 `/workspaces/vibe` - 这是容器内的项目文件夹。

- 列出文件:

```bash
ls
```

会看到项目中的相同文件:`R/`、`.devcontainer/`、`README.md` 等。

- 尝试向上移动一个目录:

```bash
cd ..
ls
```

只会看到 `vibe/` - 容器是隔离的。你无法访问计算机的其他文件夹、桌面或文档。这种隔离确保 R 环境干净且可重现。

- 返回项目文件夹:

```bash
cd vibe
```

## 步骤 7:逐行运行 R 代码

容器预装了 R 和常用包。让我们运行一个简单的数据分析脚本。

- VS Code 资源管理器中,导航到 `R/iris_analysis.R`
- 点击打开文件
- 会看到分析 iris 数据集的 R 代码
- 选择第一行:`data(iris)`
- 按 `Ctrl+Enter`(Windows/Linux)或 `Cmd+Enter`(Mac)运行
- 如果没有 R 终端,第一次会创建,第二次才运行代码
- 继续逐行运行每一行
- 运行 `head(iris)` 时,会在终端看到前 6 行
- 运行 `summary(iris)` 时,会看到统计摘要
- 运行 `hist()` 命令时,直方图会在单独窗口打开
- 也可以选择多行,用 `Ctrl+Enter` 或 `Cmd+Enter` 一起运行

## 步骤 8:运行应用程序

项目包含一个演示 Shiny 应用,用于创建交互式直方图。

- VS Code 资源管理器中,导航到 `R/app.R`
- 点击打开文件
- 会看到 Shiny Web 应用的代码
- 查看编辑器右上角的 **▶** 按钮
- 点击旁边下拉箭头,选择 **Run Shiny App**
- 应用会启动,VS Code 自动转发端口 3838
- 出现通知:**Open in Browser**
- 点击 **Open in Browser**
- Shiny 应用在 Web 浏览器打开
- 移动滑块改变直方图区间数 - 图表实时更新

## 步骤 9:进行简单更改

让我们修改应用,了解开发流程。

- 保持应用运行
- VS Code 中,编辑 `R/app.R`
- 找到第 16 行:`titlePanel("Old Faithful Geyser Data")`
- 改为:

```r
titlePanel("My First R Docker App")
```

- 保存文件(**File > Save**)
- Shiny 扩展会自动重新加载应用
- 刷新浏览器(或可能自动刷新)
- 标题现在显示自定义文本

## 步骤 10:了解 Dockerfile(可选)

- VS Code 资源管理器中,导航到 `.devcontainer/Dockerfile`
- 点击打开文件
- 会看到完整配置:

```dockerfile
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

# 5. Give shiny passwordless sudo for updating Claude Code from VS Code
RUN echo 'shiny ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    rm -rf /var/lib/apt/lists/*

# Expose Shiny server port
EXPOSE 3838
```

**关键部分:**

- `FROM rocker/shiny-verse:latest` - 预装 R、Shiny 和 tidyverse 的基础镜像
- `RUN apt-get install` - R 包所需的 Linux 系统库
- `RUN R -q -e 'install.packages(...)'` - 永久安装 R 包
- `RUN curl... && apt-get install -y nodejs` - 安装 Node.js,运行 Claude Code 所需
- `RUN npm install -g @anthropic-ai/claude-code` - 全局安装 Claude Code 获取 AI 辅助
- `RUN echo 'shiny ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers` - 让容器的用户无需输入密码即可运行 `sudo claude update`
- `EXPOSE 3838` - 为 Shiny 应用打开端口 3838

**可用的其他 Rocker 镜像:**

- `rocker/r-ver:4.5.3` - 仅 R(特定版本)
- `rocker/rstudio:latest` - 带 RStudio Server 的 R
- `rocker/tidyverse:latest` - 带 tidyverse 包的 R
- `rocker/shiny-verse:latest` - 带 Shiny 和 tidyverse 的 R(我们正在使用)

更改基础镜像后,重新构建容器以应用更改。

## 步骤 11:在 Docker 镜像中安装 R 包(可选)

通过 R 控制台(`install.packages()`)安装的包是临时的,重新构建容器时会消失。要使包永久存在,将它们添加到 Dockerfile 中。

- VS Code 资源管理器中,导航到 `.devcontainer/Dockerfile`
- 点击打开文件
- 在其他 'install.packages' 行下方添加新行以安装 `data.table` 包:
```dockerfile
RUN R -q -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
```

- 保存文件(**File > Save**)
- 点击左下角绿色图标
- 从菜单选择 **Rebuild Container**
- VS Code 会用新包重新构建容器(需 2-5 分钟)
- 验证,打开 R 终端并输入:

```r
library(data.table)
```

如果加载无错误,则包已永久安装。

## 下一步

- **创建新 R 脚本** - 在 `R/` 文件夹创建新 `.R` 文件,使用内置数据集(如 `mtcars` 或 `iris`)编写数据分析代码
- **安装 R 包** - 通过编辑 Dockerfile 并重新构建容器来添加所需包
- **探索 tidyverse** - 尝试用 `dplyr` 进行数据操作,用 `ggplot2` 和示例数据集进行可视化

## 故障排除

- **Docker Desktop 未运行** - 打开 Docker Desktop,等待绿色状态指示器,然后再重新打开容器
- **容器构建失败** - 检查互联网连接;首次构建会下载约 2GB 数据。点击 **Rebuild Container** 重试
- **端口 3838 已被使用** - 停止使用该端口的其他应用,或在 `.devcontainer/devcontainer.json` 中更改端口

## 工作流程概述

此设置提供专业的 R 开发环境:

- **VS Code** 提供带语法高亮和智能感知的代码编辑器
- **Docker 容器**运行隔离的 Linux 环境,包含 R 和所有依赖
- **Rocker 镜像**(`rocker/shiny-verse`)包含 R、Shiny、tidyverse 和开发工具
- **Dev Container 配置**(`.devcontainer/`)自动安装 VS Code 扩展以支持 R 调试和语言支持
- **端口转发**允许从浏览器访问容器内运行的 Shiny 应用

## 日常工作流程

一旦设置完成,这是日常例程:

1. **启动 Docker Desktop** - 打开应用并等待绿色状态指示器(Docker 必须运行)
2. **打开 VS Code** - 启动 VS Code 并打开项目文件夹
3. **在容器中重新打开** - 如果尚未在容器中,点击绿色图标(左下角)并选择 **Reopen in Container**
4. **编写和运行代码** - 编辑 `.R` 文件,用 `Ctrl+Enter`/`Cmd+Enter` 逐行运行,或用 **▶ Run Shiny App** 按钮运行 Shiny 应用
5. **保存工作** - 代码文件(`.R`、`.Rmd`)保存到计算机,在会话之间持久存在
6. **提交和推送** - 使用 GitHub Desktop 提交更改并推送到仓库

## 什么是 Docker Desktop?

Docker Desktop 是一个让你在计算机上更轻松使用 Docker 的应用。它提供 Docker 所需的后台服务,还有一个可视化窗口,让你查看和管理容器、镜像、存储以及其他 Docker 资源。

可以把 Docker Desktop 看作容器的控制中心。打开 Docker Desktop 时,它会启动 Docker 引擎。Docker 引擎是 Docker 中真正创建和运行容器的部分。通常你不需要直接操作引擎,因为 Docker Desktop 会替你管理它。

### Docker Desktop 做什么?

Docker Desktop 承担几项重要工作:

- **运行 Docker 引擎** - 引擎负责创建和运行装有你的软件的容器。
- **下载镜像** - 镜像是一个现成的起步包,例如装有 R 和常用 R 包的 Linux 系统。在本教程中,项目使用的是 Rocker 项目提供的镜像。
- **构建容器** - Docker 根据本项目中的 Dockerfile 和 Dev Container 设置,创建一个为 R 开发准备好的容器。
- **启动和停止容器** - 需要时,你可以打开、暂停、重启或停止容器。
- **将容器连接到你的文件** - 项目文件夹可以在容器内访问,因此你可以在 VS Code 中编辑文件,而代码在容器中运行。
- **将容器连接到你的浏览器** - 当 Shiny 应用使用端口 3838 时,Docker Desktop 和 VS Code 协同工作,让你能在 Web 浏览器中打开该应用。

### Docker Desktop 在本教程中的作用

有三个部分协同工作:

1. **Docker Desktop** 在你的计算机上运行 Docker 引擎。
2. **VS Code** 提供编辑器,你在其中编写和运行 R 代码。
3. **Dev Container** 提供一个准备好的 Linux 环境,包含 R、R 包以及本项目使用的工具。

当你选择 **Reopen in Container** 时,VS Code 会请 Docker Desktop 构建或启动项目的容器。应用仍然在你的计算机上运行,但 R 环境位于容器内。这样可以让 R 版本、包和系统工具与计算机的其他部分分开。

Docker Desktop 不会取代 VS Code、R 或 Web 浏览器。它提供运行容器的环境。VS Code 是你工作的地方,R 是你使用的语言,浏览器则是你查看 Shiny 应用的地方。

### 为什么使用 Docker Desktop?

直接在计算机上安装 R 和所有需要的包,有时会导致版本冲突。一个项目可能需要与另一个项目不同版本的包。Docker Desktop 为每个项目提供独立、可控的环境,帮助避免这些冲突。

例如,如果同学使用相同的项目文件和 Docker 设置,Docker 可以构建一个与你非常接近的环境。这样就不太容易遇到仅仅因为软件版本不同而导致的错误。你的 R 代码和项目文件仍保存在计算机上,而运行它们所需的工具则整理在容器内。

在构建项目或在容器中重新打开项目之前,Docker Desktop 必须已打开并正在运行。如果 Docker Desktop 已关闭,VS Code 将无法启动容器,你可能会看到提示 Docker 未运行的错误。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
