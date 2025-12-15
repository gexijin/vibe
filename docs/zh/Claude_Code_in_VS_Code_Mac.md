[首页](./)

# 在 Mac 的 VS Code 中使用 Claude Code

您已经在 Mac 上安装了 Claude Code，现在想要一个可视化编辑器来处理代码。VS Code 让您可以可视化地编辑文件，同时在集成终端中运行 Claude Code。可以把它想象成在一个窗口中同时拥有代码编辑器和 AI 助手。

## 核心概念

- **VS Code** - 微软开发的免费代码编辑器，可在 Mac 上运行
- **Integrated Terminal（集成终端）** - VS Code 内部的终端面板，您可以在其中运行 Claude Code
- **Explorer Panel（资源管理器面板）** - VS Code 左侧的文件浏览器

## 准备工作

- 完成[在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS)
- 完成 [VS Code 基础教程](./VS_Code_Getting_Started)
- 10-15 分钟

## 步骤 1：启动 VS Code

- 打开 **Finder** 并进入 **Applications（应用程序）**
- 找到 **Visual Studio Code** 并双击打开
- 如果看到警告"Visual Studio Code is an app downloaded from the internet（Visual Studio Code 是从互联网下载的应用）"，点击 **Open（打开）**
- VS Code 会打开并显示欢迎标签页，您可以关闭这个标签页

**提示：**在 Dock 中右键点击 VS Code，选择 **Options > Keep in Dock（选项 > 在 Dock 中保留）**，方便以后快速访问。

## 步骤 2：创建项目文件夹

- 打开 **Finder**
- 点击左侧边栏中的 **Documents（文稿）**
- 点击菜单栏中的 **File（文件）**，然后选择 **New Folder（新建文件夹）**
- 将文件夹命名为 `test_claude`

## 步骤 3：在 VS Code 中打开文件夹

- 在 VS Code 中，点击菜单栏中的 **File（文件）**，然后选择 **Open Folder（打开文件夹）**
- 导航到 **Documents（文稿）** 并选择您创建的 `test_claude` 文件夹
- 点击 **Open（打开）**
- 如果提示"Do you trust the authors of the files in this folder?（您信任此文件夹中文件的作者吗？）"，点击 **Yes, I trust the authors（是的，我信任这些作者）**

现在您应该能在左侧的资源管理器面板中看到 `TEST_CLAUDE`。

## 步骤 4：启动 Claude Code

- 打开新终端：点击菜单栏中的 **Terminal（终端）**，然后选择 **New Terminal（新建终端）**
- 终端面板会出现在 VS Code 底部
- 在终端中输入：
  ```
  claude
  ```
- Claude Code 启动，您会看到熟悉的 Claude Code 界面
- 现在您可以在 VS Code 中编辑文件的同时使用 Claude Code 了

## 步骤 5：测试工作流程

- 在 Claude Code 中输入：
```
Write a short article explaining why LLMs like to use Markdown format. Save it as article.md
```
- Claude Code 创建文件，您会看到 `article.md` 出现在左侧的资源管理器面板中
- 点击资源管理器中的 `article.md` 在编辑器中查看
- 预览格式化后的文章：右键点击 `article.md` 标签页，选择 **Open Preview（打开预览）**
- 您会看到渲染后的 Markdown，包含正确的标题、项目符号和格式

## 稍后在 VS Code 中重新打开 Claude

关闭 VS Code 后，以下是返回项目的方法：

- **方法 A：** 打开 VS Code，点击 **File > Open Recent（文件 > 打开最近使用）**，然后选择 `test_claude`
- **方法 B：** 打开 Terminal（终端），使用 `cd ~/Documents/test_claude` 导航到您的项目，然后输入 `code .`

VS Code 会记住您最近使用的文件夹，因此使用方法 A 的 Open Recent（打开最近使用）通常是最快的。

## 下一步

- 让 Claude Code 解释现有代码库："Explain what this project does"
- 让 Claude Code 帮助您编写新功能："Add a function that calculates the average of a list"
- 使用 Claude Code 修复错误："This code gives an error, can you fix it?"
- 尝试 Claude Code VS Code 扩展，获得可视化界面和内联差异显示（在扩展中搜索"Claude Code"）

## 故障排除

- **终端显示"zsh"但 Claude Code 无法启动** - 确保 Claude Code 已正确安装；运行 `claude --version` 进行验证
- **Terminal 中提示"code"命令未找到** - 在 VS Code 中，点击菜单栏中的 **View（查看）**，然后选择 **Command Palette（命令面板）**，输入"shell command"，并选择 **Shell Command: Install 'code' command in PATH（Shell 命令：在 PATH 中安装 'code' 命令）**
- **VS Code 因来自未识别的开发者而无法打开** - 前往 **System Settings > Privacy & Security（系统设置 > 隐私与安全性）** 并点击 **Open Anyway（仍要打开）**

## 工作流程概述

- **VS Code** 提供可视化编辑器界面
- **Integrated Terminal（集成终端）** 在 VS Code 内部运行 Claude Code
- 您的文件保存在 Documents 文件夹中（或您选择的任何位置）
- 在编辑器中编辑文件，在终端中与 Claude Code 对话，两全其美

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 10 日。
