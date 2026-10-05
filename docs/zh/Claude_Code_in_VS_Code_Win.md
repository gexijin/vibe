---
title: "在 Windows 上为 Claude Code 设置 VS Code"
lang: "zh"
---
[首页](./)

# 在 Windows 上为 Claude Code 设置 VS Code

你已在 Windows 上安装了 Claude Code，现在需要一个可视化编辑器来处理代码。VS Code 让你可视化编辑文件，同时在集成终端中运行 Claude Code，两者并排显示在同一个窗口中。

## 关键概念

- **VS Code** - 微软推出的免费代码编辑器，内置终端
- **Integrated Terminal** - VS Code 内置的 PowerShell 终端面板，无需切换窗口即可运行 Claude Code
- **Workspace folder（工作区文件夹）** - 你在 VS Code 中打开的文件夹；Claude Code 会读取和编辑其中的文件

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


## 步骤 3：在 VS Code 中打开文件夹

- 在 VS Code 中，点击 **File > Open Folder**
- 导航到**文档**，选择 `test_claude` 文件夹
- 点击 **Select Folder**，VS Code 将重新加载 `test_claude` 文件夹
- 如果提示"Do you trust the authors?"，点击 **Yes, I trust the authors**


## 步骤 4：启动 Claude Code

- VS Code 重新加载后，打开新终端：点击 **Terminal > New Terminal**
- 在终端面板中输入：
  ```
  claude
  ```

按照[安装教程](Install_CLAUDE_Code_Win.md)使用你的 Claude 订阅登录。登录后，你将看到欢迎消息和 Claude Code 提示符。

## 步骤 5：测试工作流程

- 在 Claude Code 中输入：
```
写一篇简短的文章，解释为什么 LLM 喜欢使用 Markdown 格式。保存为 article.md
```
- Claude Code 创建文件，你会看到 `article.md` 出现在左侧资源管理器面板中
- 点击 `article.md` 在编辑器中查看
- 预览格式化后的文章：右键点击 `article.md` 标签，选择 **Open Preview**
- 你会看到渲染后的 Markdown，包括标题、项目符号等格式

## 稍后在 VS Code 中重新打开 Claude Code

关闭 VS Code 后，返回项目的方法：

- **方法 A：** 打开 VS Code，点击 **File > Open Recent**，选择 `test_claude`
- **方法 B：** 打开**文件资源管理器**，右键单击 `test_claude` 文件夹，选择 **Open with Code**

## 下一步

- 让 Claude Code 解释现有代码库："解释这个项目做什么"
- 让 Claude Code 编写新功能："添加一个计算列表平均值的函数"
- 使用 Claude Code 修复错误："这段代码出现错误，你能修复它吗？"
- 尝试 Claude Code VS Code 扩展，获得内联差异的可视化界面（在扩展中搜索"Claude Code"）

## 故障排除

- **找不到 `claude` 命令** - 在 VS Code 终端中运行 `claude --version` 检查是否已安装 Claude Code，如未安装请先按照[安装教程](Install_CLAUDE_Code_Win.md)操作
- **改用 WSL？** - 如果你选择了可选的 WSL/Ubuntu 方式，请先从 Extensions 侧边栏安装 **WSL** 扩展，点击左下角的蓝色/绿色图标，选择 **Connect to WSL**，然后再打开项目文件夹（路径为 `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude`）

## 工作流程概述

- **VS Code** 在 Windows 上运行，提供可视化编辑界面
- **Integrated Terminal** 直接在 VS Code 内运行 Claude Code
- 编辑器中编辑文件，终端中与 Claude Code 交流，两全其美

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 10 日。
