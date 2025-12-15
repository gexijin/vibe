[首页](./)

# 使用 Claude Code 和 Docker 在 R 中进行 Vibe 编程

Vibe 编程就像与您的计算机对话一样——您描述想要的结果，Claude Code 来构建它，您测试并改进。这不是魔法，而是一种全新的工作方式，您引导愿景，AI 负责实现。本教程将向您展示如何仅使用自然语言请求构建一个真实的 NBA 统计数据仪表板。

## 核心概念

- **[Claude Code](https://code.claude.com/)** - AI 编程助手，根据您的自然语言请求编写、调试和重构代码
- **[hoopR](https://hoopr.sportsdataverse.org/)** - R 包，提供对 NBA 球员统计数据和比赛数据的便捷访问
- **迭代改进** - Vibe 编程的核心模式：描述 → 测试 → 改进 → 提交可用版本

## 您需要准备的内容

- 完成[通过 Docker 在 VS Code 中进行 R 编程](./R_Coding_Docker_Guide)
- 完成[将 GitHub Desktop 与 Claude Code 结合使用](./GitHub_Desktop_Claude_Code_Workflow)
- 已安装并启动 Docker Desktop
- 25-30 分钟

## 步骤 1：创建新的 GitHub 仓库

- 打开 GitHub Desktop
- 点击 **File > New Repository**
- 填写详细信息：
  - **Name：** `nba-dashboard`
  - **Description：** `NBA stats dashboard built with vibe coding`
  - **Local Path：** 选择一个位置（例如 Documents 或工作文件夹）
  - 勾选 **Initialize this repository with a README**
- 点击 **Create Repository**
- 点击顶部的 **Publish repository**
- 如果您希望公开，取消勾选 **Keep this code private**（可选）
- 点击 **Publish Repository**

您现在拥有一个本地 Git 仓库和 GitHub 上的备份。

## 步骤 2：复制 Docker 配置

- 访问 https://github.com/gexijin/vibe
  - **ARM64 用户注意（Apple Silicon Mac）：** 请使用 https://github.com/gexijin/vibe/tree/ARM64
- 点击 **Code** 并下载 Zip
- 打开文件资源管理器（Windows）或访达（Mac）
- 在下载文件夹中解压文件
- 导航到您的 vibe 项目文件夹（例如 `Documents/vibe`）
- 找到 `.devcontainer` 文件夹
- 复制整个文件夹（包含 `Dockerfile` 和 `devcontainer.json`）
- 导航到您的新 `nba-dashboard` 文件夹
- 将 `.devcontainer` 文件夹粘贴到那里

您的 `nba-dashboard` 文件夹现在应该包含：
- `.devcontainer/`（您刚刚复制的文件夹）
- `README.md`（由 GitHub Desktop 创建）
- `.git/`（版本控制的隐藏文件夹）

## 步骤 3：在容器中打开项目

- 从 Windows 或 Mac 启动 **Docker Desktop** 应用程序。让它在后台运行
- 打开 VS Code
- 点击 **File > Open Folder**
- 导航到 `nba-dashboard` 文件夹
- 点击 **Select Folder**（Windows）或 **Open**（Mac）
- 右下角出现通知：**Folder contains a Dev Container configuration file**
- 点击 **Reopen in Container**
- 如果您没有看到通知，点击左下角的绿色图标并选择 **Reopen in Container**
- VS Code 构建 Docker 容器（首次需要 3-5 分钟）
- 观察显示构建步骤的进度通知
- 完成后，绿色图标显示 **Dev Container: R in Docker**

## 步骤 4：启动 Claude Code

- 在 VS Code 中，点击 **Terminal > New Terminal**
- 您现在位于 Docker 容器内
- 输入以下命令启动 Claude Code：

```bash
claude
```

- 浏览器窗口打开进行身份验证
- 点击 **Continue with Google** 或 **Continue with Email**
- 使用您的 Claude 账户登录（或创建一个）
- 身份验证成功后，返回 VS Code 终端
- 您将看到 Claude 的欢迎消息

Claude Code 现在正在运行，准备接受您的请求。

## 步骤 5：第一次 Vibe - 获取 NBA 数据

现在开始有趣的部分。无需查找文档，只需描述您想要的内容。

- 在 Claude Code 终端中，输入：

```
Install the hoopR package and load current NBA player statistics. Show me the top 10 players by total points scored this season. Display it as a nice table.
```

- 按 Enter
- 观察 Claude：
  - 安装 hoopR 包
  - 编写 R 代码加载数据
  - 创建脚本显示得分最高的球员
  - 运行代码
- 查看显示球员姓名、球队和得分的输出

您刚刚使用了 Vibe 编程！无需搜索文档，无需反复试错——只需描述和测试。

**保存您的进度：** 要求 Claude 使用 Git 提交，或从 GitHub Desktop 自己完成：
```
Commit these changes.
```

## 步骤 6：第二次 Vibe - 探索数据

在构建仪表板之前，了解您拥有什么数据。

- 在 Claude Code 终端中，输入：

```
Show me what columns are available in this NBA data. Then create a summary showing: number of players, number of teams, average points per player, and who has the most assists and rebounds.
```

- 按 Enter
- Claude 探索数据集并向您展示有趣的统计数据
- 查看输出以了解可用的列，例如：player_name、team、points、assists、rebounds、field_goal_percentage 等

这种探索可以帮助您决定在仪表板中放置什么内容。

**保存您的进度：** 要求 Claude 提交，或使用 GitHub Desktop。

## 步骤 7：第三次 Vibe - 创建基础 Shiny 应用

是时候构建交互式仪表板了。

- 在 Claude Code 终端中，输入：

```
Create a Shiny app in a file called app.R that shows an interactive table of NBA player stats. Include columns for player name, team, points, assists, and rebounds. Add a slider to filter players by minimum points scored (from 0 to 1000). Make it look clean and professional.
```

- 按 Enter
- Claude 创建包含完整 Shiny 应用程序的 `app.R`
- 等待 Claude 完成文件编写

## 步骤 8：运行 Shiny 应用

测试您的仪表板以查看它是否工作。

- 查看 VS Code 编辑器右上角（`app.R` 打开的位置）
- 找到带下拉箭头的 **▶** 按钮
- 点击下拉菜单并选择 **Run Shiny App**
- 应用程序启动，出现通知：**Open in Browser**
- 点击 **Open in Browser**
- NBA 仪表板在您的网络浏览器中打开
- 尝试移动得分滑块——表格实时过滤
- 滚动浏览球员数据
- 如果应用程序正常工作，提交更改

如果出现问题，复制任何错误消息并粘贴给 Claude 进行修复。

## 步骤 9：第四次 Vibe - 添加可视化

表格很有用，但可视化讲述更好的故事。

- 返回 Claude Code 终端，输入：

```
Add a bar chart below the table showing the top 15 players by points. Use different colors for each player. Also add a scatter plot showing the relationship between points and assists for all filtered players.
```

- 按 Enter
- Claude 使用可视化代码更新 `app.R`
- 再次点击 **Run Shiny App** 重新加载应用程序
- 刷新您的浏览器
- 您现在看到彩色条形图和散点图
- 移动滑块——所有可视化一起更新

这就是 Vibe 编程的实际操作：描述功能，测试它，迭代。

## 步骤 10：第五次 Vibe - 添加球队过滤器

通过球队选择使仪表板更具交互性。

- 在 Claude Code 终端中，输入：

```
Add a dropdown menu to filter players by team. Put it at the top. When I select a team, show only players from that team. Include an "All Teams" option to show everyone.
```

- 按 Enter
- Claude 添加球队过滤器
- 刷新您的浏览器
- 测试下拉菜单——选择不同的球队，如 Lakers、Warriors、Celtics
- 观察每个球队的表格和图表更新

您正在通过对话构建专业的仪表板。

## 步骤 11：审查并提交

在提交之前，审查 Claude 构建的内容。

- 在 VS Code 资源管理器中，点击 `app.R` 打开它
- 浏览代码——注意 UI 布局、服务器逻辑和绘图代码
- 您不需要理解每一行，但要了解结构
- 打开 GitHub Desktop
- 您将看到 `app.R` 列为新文件
- 右侧面板显示所有绿色代码（新添加）
- 在左下角的 **Summary** 字段中，输入：

```
Create NBA dashboard with team filter and visualizations
```

- 点击 **Commit to main**
- 点击 **Push origin** 备份到 GitHub

您已保存了第一个可用版本！

## 步骤 12：迭代和改进

Vibe 编程在迭代时更显光彩。尝试通过描述来添加功能：

**向 Claude 请求的示例：**

- "Add a player search box so I can type a player's name and jump to them"
- "Show the team logos next to team names in the dropdown"
- "Add a line chart showing points per game trend for the selected team"
- "Make the bar chart sortable by clicking column headers"
- "Add tooltips to the scatter plot showing player names when I hover"

每次成功添加功能后：
- 在浏览器中测试
- 如果有效，使用 GitHub Desktop 提交
- 如果出现问题，告诉 Claude 错误并要求修复
- 修复后，提交可用版本


**关键原则：**

- **描述结果，而非实现** - 说"显示得分最高的球员"而不是"使用 arrange() 和 head()"
- **快速迭代** - 测试 → 改进 → 测试 → 改进
- **提交可用版本** - 在尝试新功能之前保存每次成功
- **拥抱失败** - 如果 Claude 的代码出错，只需描述错误并要求修复
- **保持控制** - 您决定功能、优先级以及何时足够好

每次都遵循这个模式：描述 → 测试 → 迭代 → 提交。

## 下一步

- **应用到您的领域** - 将 Vibe 编程用于您自己的数据（研究、业务、爱好）
- **尝试其他包** - 要求 Claude 使用 `nflfastR` 处理橄榄球数据或 `worldfootballR` 处理足球数据
- **通过提问学习** - 当 Claude 编写代码时，询问"解释这个函数的作用"以学习 R
- **分享您的仪表板** - 部署到 [shinyapps.io](https://www.shinyapps.io/)（向 Claude 询问方法）
- **阅读有关 Vibe 编程的内容** - 访问 [IBM 指南](https://www.ibm.com/think/topics/vibe-coding)了解有关这种编码风格的更多信息

## 故障排除

- **hoopR 安装失败** - 检查您的互联网连接，该包从网络下载数据。尝试在 R 终端中运行 `install.packages("hoopR")` 以查看详细的错误消息。
- **Shiny 应用无法启动** - 验证是否已安装 Shiny 扩展（在 VS Code 扩展中搜索"Posit.shiny"）。检查终端中的错误消息并将其粘贴给 Claude。
- **没有显示数据** - hoopR 包提取实时数据，如果 NBA 赛季尚未开始，可能数据有限。要求 Claude 使用示例数据或上一赛季的数据。
- **Claude 出错** - 这是正常的！复制错误消息，粘贴给 Claude，并说"修复此错误"。Vibe 编程包括迭代和调试。
- **无法推送到 GitHub** - 确保您已登录 GitHub Desktop 并发布了仓库（步骤 1）。检查您的互联网连接。

## 工作流程概述

本教程将几种技术组合成一个工作流程：

- **GitHub Desktop** - 具有可视化界面的版本控制（创建仓库、提交、推送）
- **Docker 容器** - 预装所有依赖项的隔离 R 环境
- **VS Code** - 连接到 Docker 容器的代码编辑器
- **Claude Code** - 根据您的描述编写 R 和 Shiny 代码的 AI 助手
- **hoopR 包** - 具有简单 API 的 NBA 数据源
- **Shiny 框架** - R 中的交互式 Web 应用程序

神奇之处不在于任何单一工具——而在于 Vibe 编程如何让您描述想要的内容并快速迭代。您在不到 30 分钟内从空项目到可用的体育仪表板，而无需手动编写任何一行代码。

## 日常工作流程

完成初始设置后，您的日常 Vibe 编程例程变为：

1. **启动 Docker Desktop** - 启动应用程序，等待绿色状态
2. **打开 VS Code** - 打开您的项目，如需要则在容器中重新打开
3. **启动 Claude Code** - 在终端中输入 `claude`
4. **描述您的目标** - "添加一个功能..."或"修复...的错误"
5. **测试更改** - 运行您的应用程序，检查是否有效
6. **迭代或提交** - 如果出现问题，描述修复方法，如果有效，使用 GitHub Desktop 提交
7. **定期推送** - 点击 **Push origin** 备份到 GitHub

您练习得越多，就越能更好地描述您想要的内容。Vibe 编程是一项技能——您学会什么样的描述效果最好，以及如何将大创意分解为可测试的部分。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
