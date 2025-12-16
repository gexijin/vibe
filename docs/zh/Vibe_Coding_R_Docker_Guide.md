[首页](./)

# 使用 Claude Code 和 Docker 在 R 中进行 Vibe 编程

Vibe 编程就像与计算机对话——你描述想要的结果,Claude Code 来构建,你测试并改进。这不是魔法,而是一种全新的工作方式:你负责愿景,AI 负责实现。本教程将教你如何仅用自然语言请求构建真实的 NBA 统计数据仪表板。

## 核心概念

- **[Claude Code](https://code.claude.com/)** - AI 编程助手,根据你的自然语言请求编写、调试和重构代码
- **[hoopR](https://hoopr.sportsdataverse.org/)** - R 包,提供对 NBA 球员统计数据和比赛数据的便捷访问
- **迭代改进** - Vibe 编程的核心模式:描述 → 测试 → 改进 → 提交可用版本

## 准备工作

- 完成 [通过 Docker 在 VS Code 中进行 R 编程](./R_Coding_Docker_Guide)
- 完成 [将 GitHub Desktop 与 Claude Code 结合使用](./GitHub_Desktop_Claude_Code_Workflow)
- 已安装并启动 Docker Desktop
- 25-30 分钟

## 步骤 1:创建新的 GitHub 仓库

- 打开 GitHub Desktop
- 点击 **File > New Repository**
- 填写详细信息:
  - **Name:** `nba-dashboard`
  - **Description:** `NBA stats dashboard built with vibe coding`
  - **Local Path:** 选择一个位置(如 Documents 或工作文件夹)
  - 勾选 **Initialize this repository with a README**
- 点击 **Create Repository**
- 点击顶部的 **Publish repository**
- 如果希望公开,取消勾选 **Keep this code private**(可选)
- 点击 **Publish Repository**

现在你已拥有本地 Git 仓库和 GitHub 上的备份。

## 步骤 2:复制 Docker 配置

- 访问 https://github.com/gexijin/vibe
  - **ARM64 用户注意(Apple Silicon Mac):** 请使用 https://github.com/gexijin/vibe/tree/ARM64
- 点击 **Code** 并下载 Zip
- 打开文件资源管理器(Windows)或访达(Mac)
- 在下载文件夹中解压文件
- 导航到你的 vibe 项目文件夹(如 `Documents/vibe`)
- 找到 `.devcontainer` 文件夹
- 复制整个文件夹(包含 `Dockerfile` 和 `devcontainer.json`)
- 导航到新建的 `nba-dashboard` 文件夹
- 将 `.devcontainer` 文件夹粘贴到这里

你的 `nba-dashboard` 文件夹现在应包含:
- `.devcontainer/`(你刚复制的文件夹)
- `README.md`(由 GitHub Desktop 创建)
- `.git/`(版本控制的隐藏文件夹)

## 步骤 3:在容器中打开项目

- 从 Windows 或 Mac 启动 **Docker Desktop** 应用程序。让它在后台运行
- 打开 VS Code
- 点击 **File > Open Folder**
- 导航到 `nba-dashboard` 文件夹
- 点击 **Select Folder**(Windows)或 **Open**(Mac)
- 右下角出现通知:**Folder contains a Dev Container configuration file**
- 点击 **Reopen in Container**
- 如果没看到通知,点击左下角的绿色图标,选择 **Reopen in Container**
- VS Code 构建 Docker 容器(首次需要 3-5 分钟)
- 观察显示构建步骤的进度通知
- 完成后,绿色图标显示 **Dev Container: R in Docker**

## 步骤 4:启动 Claude Code

- 在 VS Code 中,点击 **Terminal > New Terminal**
- 你现在位于 Docker 容器内
- 输入以下命令启动 Claude Code:

```bash
claude
```

- 浏览器窗口打开进行身份验证
- 点击 **Continue with Google** 或 **Continue with Email**
- 使用你的 Claude 账户登录(或创建一个)
- 身份验证成功后,返回 VS Code 终端
- 你将看到 Claude 的欢迎消息

Claude Code 现在已准备就绪,可接受你的请求。

## 步骤 5:第一次 Vibe - 获取 NBA 数据

现在开始有趣的部分。无需查找文档,只需描述你想要的内容。

- 在 Claude Code 终端中,输入:

```
安装 hoopR 包并加载当前 NBA 球员统计数据。显示本赛季总得分前 10 的球员。以漂亮的表格形式展示。
```

- 按 Enter
- 观察 Claude:
  - 安装 hoopR 包
  - 编写 R 代码加载数据
  - 创建脚本显示得分最高的球员
  - 运行代码
- 查看显示球员姓名、球队和得分的输出

你刚刚使用了 Vibe 编程!无需搜索文档,无需反复试错——只需描述和测试。

**保存进度:** 要求 Claude 使用 Git 提交,或从 GitHub Desktop 自己完成:
```
提交这些更改。
```

## 步骤 6:第二次 Vibe - 探索数据

构建仪表板前先了解你拥有什么数据。

- 在 Claude Code 终端中,输入:

```
显示这个 NBA 数据中有哪些可用列。然后创建摘要显示：球员数量、球队数量、每位球员的平均得分，以及谁的助攻和篮板最多。
```

- 按 Enter
- Claude 探索数据集并展示有趣的统计数据
- 查看输出以了解可用的列,如:player_name、team、points、assists、rebounds、field_goal_percentage 等

这种探索帮助你决定在仪表板中放置什么内容。

**保存进度:** 要求 Claude 提交,或使用 GitHub Desktop。

## 步骤 7:第三次 Vibe - 创建基础 Shiny 应用

开始构建交互式仪表板。

- 在 Claude Code 终端中,输入:

```
在名为 app.R 的文件中创建一个 Shiny 应用，显示 NBA 球员统计数据的交互式表格。包含球员姓名、球队、得分、助攻和篮板列。添加滑块按最低得分（0 到 1000）过滤球员。让它看起来简洁专业。
```

- 按 Enter
- Claude 创建包含完整 Shiny 应用程序的 `app.R`
- 等待 Claude 完成文件编写

## 步骤 8:运行 Shiny 应用

测试仪表板以查看它是否工作。

- 查看 VS Code 编辑器右上角(`app.R` 打开的位置)
- 找到带下拉箭头的 **▶** 按钮
- 点击下拉菜单并选择 **Run Shiny App**
- 应用启动,出现通知:**Open in Browser**
- 点击 **Open in Browser**
- NBA 仪表板在你的网络浏览器中打开
- 尝试移动得分滑块——表格实时过滤
- 滚动浏览球员数据
- 如果应用正常工作,提交更改

如果出现问题,复制任何错误消息并粘贴给 Claude 进行修复。

## 步骤 9:第四次 Vibe - 添加可视化

表格很有用,但可视化讲述更好的故事。

- 返回 Claude Code 终端,输入:

```
在表格下方添加柱状图，显示得分前 15 的球员。每个球员使用不同颜色。同时添加散点图，显示所有过滤球员的得分和助攻之间的关系。
```

- 按 Enter
- Claude 使用可视化代码更新 `app.R`
- 再次点击 **Run Shiny App** 重新加载应用
- 刷新你的浏览器
- 你现在看到彩色条形图和散点图
- 移动滑块——所有可视化一起更新

这就是 Vibe 编程的实际操作:描述功能,测试,迭代。

## 步骤 10:第五次 Vibe - 添加球队过滤器

通过球队选择使仪表板更具交互性。

- 在 Claude Code 终端中,输入:

```
添加下拉菜单按球队过滤球员。放在顶部。当我选择一个球队时，只显示该球队的球员。包含"所有球队"选项以显示所有人。
```

- 按 Enter
- Claude 添加球队过滤器
- 刷新你的浏览器
- 测试下拉菜单——选择不同的球队,如 Lakers、Warriors、Celtics
- 观察每个球队的表格和图表更新

你正在通过对话构建专业的仪表板。

## 步骤 11:审查并提交

提交前先审查 Claude 构建的内容。

- 在 VS Code 资源管理器中,点击 `app.R` 打开
- 浏览代码——注意 UI 布局、服务器逻辑和绘图代码
- 你不需要理解每一行,但要了解结构
- 打开 GitHub Desktop
- 你将看到 `app.R` 列为新文件
- 右侧面板显示所有绿色代码(新添加)
- 在左下角的 **Summary** 字段中,输入:

```
Create NBA dashboard with team filter and visualizations
```

- 点击 **Commit to main**
- 点击 **Push origin** 备份到 GitHub

你已保存了第一个可用版本!

## 步骤 12:迭代和改进

Vibe 编程在迭代时更显威力。尝试通过描述来添加功能:

**向 Claude 请求的示例:**

- "添加球员搜索框，让我可以输入球员姓名并跳转到他们"
- "在下拉菜单中的球队名称旁边显示球队标志"
- "添加折线图显示所选球队的场均得分趋势"
- "让柱状图可以通过点击列标题排序"
- "为散点图添加工具提示，悬停时显示球员姓名"

每次成功添加功能后:
- 在浏览器中测试
- 如果有效,使用 GitHub Desktop 提交
- 如果出现问题,告诉 Claude 错误并要求修复
- 修复后,提交可用版本


**核心原则:**

- **描述结果,而非实现** - 说"显示得分最高的球员"而不是"使用 arrange() 和 head()"
- **快速迭代** - 测试 → 改进 → 测试 → 改进
- **提交可用版本** - 在尝试新功能前保存每次成功
- **拥抱失败** - 如果 Claude 的代码出错,只需描述错误并要求修复
- **保持控制** - 你决定功能、优先级以及何时足够好

每次都遵循这个模式:描述 → 测试 → 迭代 → 提交。

## 下一步

- **应用到你的领域** - 将 Vibe 编程用于你自己的数据(研究、业务、爱好)
- **尝试其他包** - 要求 Claude 使用 `nflfastR` 处理橄榄球数据或 `worldfootballR` 处理足球数据
- **通过提问学习** - 当 Claude 编写代码时,询问"解释这个函数的作用"以学习 R
- **分享你的仪表板** - 部署到 [shinyapps.io](https://www.shinyapps.io/)(向 Claude 询问方法)
- **阅读有关 Vibe 编程的内容** - 访问 [IBM 指南](https://www.ibm.com/think/topics/vibe-coding)了解更多

## 故障排除

- **hoopR 安装失败** - 检查互联网连接,该包从网络下载数据。尝试在 R 终端中运行 `install.packages("hoopR")` 以查看详细错误消息。
- **Shiny 应用无法启动** - 验证是否已安装 Shiny 扩展(在 VS Code 扩展中搜索"Posit.shiny")。检查终端中的错误消息并粘贴给 Claude。
- **没有显示数据** - hoopR 包提取实时数据,如果 NBA 赛季尚未开始,可能数据有限。要求 Claude 使用示例数据或上一赛季的数据。
- **Claude 出错** - 这是正常的!复制错误消息,粘贴给 Claude,并说"修复此错误"。Vibe 编程包括迭代和调试。
- **无法推送到 GitHub** - 确保你已登录 GitHub Desktop 并发布了仓库(步骤 1)。检查互联网连接。

## 工作流程概述

本教程将几种技术组合成一个工作流程:

- **GitHub Desktop** - 具有可视化界面的版本控制(创建仓库、提交、推送)
- **Docker 容器** - 预装所有依赖项的隔离 R 环境
- **VS Code** - 连接到 Docker 容器的代码编辑器
- **Claude Code** - 根据你的描述编写 R 和 Shiny 代码的 AI 助手
- **hoopR 包** - 具有简单 API 的 NBA 数据源
- **Shiny 框架** - R 中的交互式 Web 应用程序

神奇之处不在于任何单一工具——而在于 Vibe 编程如何让你描述想要的内容并快速迭代。你在不到 30 分钟内从空项目到可用的体育仪表板,而无需手动编写任何一行代码。

## 日常工作流程

完成初始设置后,你的日常 Vibe 编程流程变为:

1. **启动 Docker Desktop** - 启动应用,等待绿色状态
2. **打开 VS Code** - 打开你的项目,如需要则在容器中重新打开
3. **启动 Claude Code** - 在终端中输入 `claude`
4. **描述你的目标** - "添加一个功能..."或"修复...的错误"
5. **测试更改** - 运行你的应用,检查是否有效
6. **迭代或提交** - 如果出现问题,描述修复方法;如果有效,使用 GitHub Desktop 提交
7. **定期推送** - 点击 **Push origin** 备份到 GitHub

你练习得越多,就越能更好地描述你想要的内容。Vibe 编程是一项技能——你学会什么样的描述效果最好,以及如何将大创意分解为可测试的部分。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
