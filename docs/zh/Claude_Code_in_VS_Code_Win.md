[首页](./)

# 在 WSL 上为 Claude Code 设置 VS Code

您已经在 Windows 机器上安装了 WSL 和 Claude Code，现在您需要一个可视化编辑器来处理代码。VS Code 在 Windows 和 Linux 环境之间架起了桥梁，让您可以可视化地编辑文件，同时在集成终端中运行 Claude Code。可以把 VS Code 看作是通往 Linux 世界的一扇窗户。

## 关键概念

- **VS Code** - 微软推出的免费代码编辑器，运行在 Windows 上但可以连接到 WSL
- **WSL Extension** - 将 VS Code 连接到您的 Linux 环境，以便您可以运行 Claude Code 等 Linux 工具
- **Integrated Terminal** - VS Code 内部的终端面板，在您的 WSL（Linux）环境中运行
- **/mnt/c/** - WSL 访问 Windows 文件的方式（例如，`/mnt/c/Users/...` = `C:\Users\...`）

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
- 当 **Visual Studio Code** 出现在搜索结果中时点击它
- VS Code 打开并显示欢迎标签页 - 您可以关闭这个标签页


## 步骤 3：安装 WSL Extension

- 在 VS Code 中，点击左侧边栏中的 **Extensions** 图标（看起来像四个方块）
- 在搜索框中输入 `WSL`
- 找到微软的 **WSL**（应该是第一个结果）
- 点击蓝色的 **Install** 按钮
- 等待安装完成（几秒钟）

## 步骤 4：将 VS Code 连接到 WSL

- 查看 VS Code 左下角 - 您会看到一个蓝色或绿色的图标
- 点击此图标以打开远程连接菜单
- 从菜单中选择 **Connect to WSL**
- VS Code 将重新加载并连接到您的 Ubuntu 安装
- 左下角现在应该显示 **WSL: Ubuntu**

第一次连接时，VS Code 会在 WSL 中安装一个小型服务器。这大约需要 30 秒。

## 步骤 5：在 VS Code 中打开文件夹

- 在 VS Code 中（仍然连接到 WSL），点击菜单栏中的 **File**，然后选择 **Open Folder**
- 顶部中央会出现一个 **Open Folder** 下拉菜单。
- 通过输入以下内容找到您的文件夹：
  ```
  /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  将 `YOUR_USERNAME` 替换为您的 Windows 用户名（例如，`John.Smith`）
- 点击 **OK**。VS Code 将重新加载您的 `test_claude` 文件夹
- 如果提示"Do you trust the authors?"，点击 **Yes, I trust the authors**


## 步骤 6：启动 Claude Code

- VS Code 重新加载后，打开一个新终端：点击菜单栏中的 **Terminal**，然后选择 **New Terminal**
- 在终端面板中输入：
  ```
  claude
  ```
- Claude Code 启动 - 您会看到熟悉的 Claude Code 界面
- 您现在可以在 VS Code 中编辑文件的同时使用 Claude Code 了

## 步骤 7：测试工作流程

- 在 Claude Code 中输入：
```
Write a short article explaining why LLMs like to use Markdown format. Save it as article.md
```
- Claude Code 创建文件 - 您会看到 `article.md` 出现在左侧的资源管理器面板中
- 在资源管理器中点击 `article.md` 以在编辑器中查看它
- 要预览格式化后的文章：右键单击 `article.md` 标签并选择 **Open Preview**
- 您将看到渲染后的 Markdown，包含正确的标题、项目符号和格式

## 稍后在 VS Code 中重新打开 Claude

关闭 VS Code 后，以下是如何返回到您的 WSL 项目的方法：

- **方法 A：** 打开 VS Code，点击左下角，选择 **Connect to WSL**，然后选择 **File > Open Recent**。选择 `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude [WSL: Ubuntu]`
- **方法 B：** 从 Windows 打开 Ubuntu 应用，在终端中导航到您的项目，然后输入 `code .`

VS Code 会记住您最近的文件夹，所以使用"Open Recent"的方法 A 通常是最快的。

## 下一步

- 让 Claude Code 解释现有代码库："Explain what this project does"
- 让 Claude Code 帮助您编写新功能："Add a function that calculates the average of a list"
- 使用 Claude Code 修复错误："This code gives an error, can you fix it?"
- 尝试 Claude Code VS Code 扩展以获得具有内联差异的可视化界面（在扩展中搜索"Claude Code"）
- 要更高效地处理较大的文件，请在 WSL 文件系统（`/home/user/`）中创建一个文件夹。从 Windows，在文件资源管理器侧边栏底部查找 Linux 图标。或者在地址栏中输入 `\\wsl.localhost\`。

## 故障排除

- **左下角未显示"WSL: Ubuntu"** - 确保 WSL 已正确安装；尝试先打开 Ubuntu 终端以验证其是否正常工作
- **终端显示 PowerShell 而不是 Linux** - 点击终端面板中 **+** 旁边的下拉箭头，然后选择 **Ubuntu (WSL)**
- **找不到 `claude` 命令** - 运行 `claude --version` 检查 Claude Code 是否已安装；如果没有，请先按照 WSL 安装教程进行操作

## 工作流程概述

- **VS Code** 在 Windows 上运行并提供可视化编辑器界面
- **WSL Extension** 将 VS Code 连接到 Ubuntu，以便您可以运行 Linux 工具
- **Integrated Terminal** 在 WSL 内部运行 Claude Code
- 您的文件保存在 Windows（文档文件夹）中 - WSL 通过 `/mnt/c/` 访问它们
- 在编辑器中编辑文件，在终端中与 Claude Code 聊天 - 两全其美

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 10 日。
