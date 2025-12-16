[首页](./)

# 在 WSL 上为 Claude Code 设置 VS Code

你已在 Windows 上安装了 WSL 和 Claude Code，现在需要一个可视化编辑器来处理代码。VS Code 在 Windows 和 Linux 环境之间架起桥梁，让你可视化编辑文件，同时在集成终端中运行 Claude Code。可以把 VS Code 看作通往 Linux 世界的窗口。

## 关键概念

- **VS Code** - 微软推出的免费代码编辑器，运行在 Windows 上可连接到 WSL
- **WSL Extension** - 将 VS Code 连接到 Linux 环境，以便运行 Claude Code 等 Linux 工具
- **Integrated Terminal** - VS Code 内置终端面板，在 WSL（Linux）环境中运行
- **/mnt/c/** - WSL 访问 Windows 文件的路径（如 `/mnt/c/Users/...` = `C:\Users\...`）

## 所需准备

- 完成[在 Windows 上安装 Claude Code](./Install_CLAUDE_Code_Win)
- 完成 [VS Code 基础](./VS_Code_Getting_Started)
- 10-15 分钟

## 步骤 1：创建项目文件夹

- 打开**文件资源管理器**（点击任务栏中的文件夹图标）
- 导航到**文档**
- 在空白处右键单击，选择**新建 > 文件夹**
- 将文件夹命名为 `test_claude`

## 步骤 2：启动 VS Code

- 点击 **Windows 开始按钮**（屏幕左下角）
- 在搜索框中输入 `Visual Studio Code` 或 `VS Code`
- 点击搜索结果中的 **Visual Studio Code**
- VS Code 打开并显示欢迎标签页，可以关闭此标签页


## 步骤 3：安装 WSL Extension

- 在 VS Code 中，点击左侧边栏的 **Extensions** 图标（四个方块）
- 在搜索框中输入 `WSL`
- 找到微软的 **WSL**（第一个结果）
- 点击蓝色 **Install** 按钮
- 等待几秒钟完成安装

## 步骤 4：将 VS Code 连接到 WSL

- 查看 VS Code 左下角，你会看到一个蓝色或绿色图标
- 点击此图标打开远程连接菜单
- 选择 **Connect to WSL**
- VS Code 将重新加载并连接到 Ubuntu
- 左下角现在应显示 **WSL: Ubuntu**

首次连接时，VS Code 会在 WSL 中安装小型服务器，约需 30 秒。

## 步骤 5：在 VS Code 中打开文件夹

- 在 VS Code 中（连接到 WSL 状态），点击 **File > Open Folder**
- 顶部中央出现 **Open Folder** 下拉菜单
- 输入以下路径找到文件夹：
  ```
  /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  将 `YOUR_USERNAME` 替换为你的 Windows 用户名（如 `John.Smith`）
- 点击 **OK**，VS Code 将重新加载 `test_claude` 文件夹
- 如果提示"Do you trust the authors?"，点击 **Yes, I trust the authors**


## 步骤 6：启动 Claude Code

- VS Code 重新加载后，打开新终端：点击 **Terminal > New Terminal**
- 在终端面板中输入：
  ```
  claude
  ```
- Claude Code 启动，你会看到熟悉的界面
- 现在可以在 VS Code 中编辑文件的同时使用 Claude Code

## 步骤 7：测试工作流程

- 在 Claude Code 中输入：
```
写一篇简短的文章，解释为什么 LLM 喜欢使用 Markdown 格式。保存为 article.md
```
- Claude Code 创建文件，你会看到 `article.md` 出现在左侧资源管理器面板中
- 点击 `article.md` 在编辑器中查看
- 预览格式化后的文章：右键点击 `article.md` 标签，选择 **Open Preview**
- 你会看到渲染后的 Markdown，包括标题、项目符号等格式

## 稍后在 VS Code 中重新打开 Claude

关闭 VS Code 后，返回 WSL 项目的方法：

- **方法 A：** 打开 VS Code，点击左下角，选择 **Connect to WSL**，再选择 **File > Open Recent**，选择 `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude [WSL: Ubuntu]`
- **方法 B：** 从 Windows 打开 Ubuntu 应用，在终端中导航到项目，输入 `code .`

VS Code 会记住最近的文件夹，使用方法 A 的"Open Recent"通常最快。

## 下一步

- 让 Claude Code 解释现有代码库："解释这个项目做什么"
- 让 Claude Code 编写新功能："添加一个计算列表平均值的函数"
- 使用 Claude Code 修复错误："这段代码出现错误，你能修复它吗？"
- 尝试 Claude Code VS Code 扩展，获得内联差异的可视化界面（在扩展中搜索"Claude Code"）
- 处理大文件时，可在 WSL 文件系统（`/home/user/`）中创建文件夹。从 Windows 在文件资源管理器侧边栏底部找 Linux 图标，或在地址栏输入 `\\wsl.localhost\`

## 故障排除

- **左下角未显示"WSL: Ubuntu"** - 确保已正确安装 WSL，先打开 Ubuntu 终端验证是否正常工作
- **终端显示 PowerShell 而非 Linux** - 点击终端面板中 **+** 旁边的下拉箭头，选择 **Ubuntu (WSL)**
- **找不到 `claude` 命令** - 运行 `claude --version` 检查是否已安装 Claude Code，如未安装请先按照 WSL 安装教程操作

## 工作流程概述

- **VS Code** 在 Windows 上运行，提供可视化编辑界面
- **WSL Extension** 将 VS Code 连接到 Ubuntu，以便运行 Linux 工具
- **Integrated Terminal** 在 WSL 内运行 Claude Code
- 文件保存在 Windows（文档文件夹）中，WSL 通过 `/mnt/c/` 访问
- 编辑器中编辑文件，终端中与 Claude Code 交流，两全其美

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 10 日。
