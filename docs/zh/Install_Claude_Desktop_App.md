---
title: "安装 Claude Desktop 应用"
lang: "zh"
---
[首页](./)

# 安装 Claude Desktop 应用

Claude Desktop 是一款适用于 Windows 和 Mac 的独立聊天应用。打开它，输入一条消息，Claude 就会回答——不需要 Terminal，也不需要输入命令。无论是日常提问、查资料还是写作，它都是和 Claude 聊天的好方式。

它和 **Claude Code** 不同。Claude Code 是本站其他教程中使用的工具，运行在 Terminal 中，帮助你在项目文件夹里编写和修改代码。Claude Desktop 则是一个通用的聊天窗口。两者可以同时安装；在付费套餐中，你甚至可以直接在 Claude Desktop 里打开 Claude Code。

## 核心概念

- **Claude Desktop**：一款适用于 Windows 和 Mac 的原生应用，你可以像使用聊天软件一样直接和 Claude 对话。
- **Claude.ai 账户**：你用来登录的账户——和你在 [claude.ai](https://claude.ai) 上使用的是同一个。免费和付费套餐都可以使用。
- **Claude Code**：本站其他教程介绍的、基于 Terminal 的编程助手。它需要单独安装——请参阅[在 Windows 上安装 Claude Code](./Install_CLAUDE_Code_Win.md)或[在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS.md)。

## 你需要准备的内容

- 一台 Windows 10（或更新版本）电脑，或一台 Mac（macOS 11 Big Sur 或更新版本）
- 网络连接
- 一个免费或付费的 Claude.ai 账户（如果还没有，可以在设置过程中创建）
- 5 分钟

## 步骤 1：下载安装程序

- 访问 [claude.ai/download](https://claude.ai/download)
- **Windows：** 点击 **Download for Windows**。（如果你的电脑是基于 ARM 的 Windows 电脑——这种情况不常见——请改用页面上单独的 arm64 下载链接。）
- **Mac：** 点击 **Download for macOS**。这个安装包同时适用于 Intel 和 Apple Silicon 芯片的 Mac，所以你不需要知道自己的 Mac 用的是哪种芯片。

## 步骤 2：安装应用

### Windows

- 打开下载的文件（如果没有自动打开，请在**下载**文件夹中查找）
- 按照安装程序的屏幕提示操作
- 安装完成后，在**开始**菜单中找到 **Claude**

### Mac

- 打开下载的文件
- 出现提示时，将 **Claude** 图标拖到**应用程序**文件夹中
- 从**应用程序**文件夹或启动台打开 **Claude**

## 步骤 3：登录

- 启动 Claude 应用
- 按照屏幕提示，使用你的 Claude.ai 账户登录
- 还没有账户？请先访问 [claude.ai](https://claude.ai) 创建一个免费账户，然后回来登录

## 步骤 4：发送第一条消息

- 点击消息输入框
- 输入类似这样的内容：`What can you help me with?`
- 按 **Enter** 发送
- Claude 会直接在应用窗口中回复

## 步骤 5：（可选）了解 Claude Desktop 的其他功能

Claude Desktop 不只是用来聊天。根据你的套餐不同，还可以使用：

- **Chat（聊天）**——所有套餐都可用，包括免费套餐
- **Claude Code**——Pro、Max、Team 和 Enterprise 套餐可以直接在 Claude Desktop 中启动 Claude Code，无需另外打开 Terminal
- **Claude Cowork**——付费套餐可用，让 Claude 在可以访问本地文件的情况下完成多步骤任务
- **Desktop Extensions（桌面扩展）**——一项高级功能，通过可安装扩展的目录将 Claude 连接到本地应用和文件；入门时不需要

日常聊天用不到这些功能——等你熟悉了基本操作之后，再去探索它们也不迟。

## 下一步

- [在 Windows 上安装 Claude Code](./Install_CLAUDE_Code_Win.md)或[在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS.md)——安装本站其他教程中使用的、基于 Terminal 的编程助手
- [Claude Code 基本操作](./Claude_Code_Basic_Operations.md)——安装好 Claude Code 后，学习基本用法
- [什么是 Anthropic 和 Claude？](./What_Is_Anthropic_And_Claude.md)——如果你刚接触 Claude，这是一篇简短的入门介绍

## 故障排除

- **Windows 显示"Windows 已保护你的电脑"并阻止安装程序**——这是 Windows 对新下载文件的标准 SmartScreen 警告，并不是 Claude 特有的。如果你信任来源（官方的 claude.ai/download 页面），请点击**更多信息**，然后点击**仍要运行**。
- **Mac 提示应用"无法打开，因为它来自身份不明的开发者"**——这是 macOS 的 Gatekeeper 标准安全检查。右键点击（或按住 Control 键点击）Claude 应用，选择**打开**，然后确认。
- **无法登录**——检查网络连接，并先确认你能在浏览器中登录 [claude.ai](https://claude.ai)。
- **安装后应用无法启动**——重启电脑，然后再次尝试打开 Claude。如果仍然不行，请从 [claude.ai/download](https://claude.ai/download) 重新下载安装程序。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2026 年 9 月 18 日。
