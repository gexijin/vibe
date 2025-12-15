[首页](./)

# Mac 上的 Claude Code 本地版本控制

你正在使用 AI 辅助编程。它会修改你的文件。有时修改效果完美，有时则不然。**版本控制就像是整个项目的撤销按钮。** 每次保存快照（称为"commit"）时，你就创建了一个可以随时返回的还原点。最棒的是，你可以完全在自己的计算机上完成这些操作，Claude Code 会为你处理一切。

## 关键概念

- **Terminal** - Mac 内置的命令行界面，用于运行命令
- **Git** - 在你的计算机上跟踪文件的每个变化，创建你可以随时返回的还原点
- **Commit** - 项目在特定时间点的快照，包含对变化的描述
- **Claude Code** - AI 编程助手，通过简单的请求编写代码、修复错误并处理 Git 操作

## 你需要准备什么

- 完成 [在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS)
- 30 分钟

## 步骤 1：打开 Terminal

选择以下方法之一：

- **Spotlight：** 按 `Command (⌘) + Space`，输入 `Terminal`，按 Enter
- **Finder：** 打开 **应用程序** > **实用工具** > **Terminal**
- **Launchpad：** 点击 Dock 中的 **Launchpad**，搜索 `Terminal`

你会看到一个以 `$` 或 `%` 结尾的命令提示符。

## 步骤 2：安装 Git

Mac 通常已预装 Git。让我们检查一下：

- 输入此命令并按 Enter：
  ```
  git --version
  ```

**如果看到版本号**（如 `git version 2.39.0`），Git 已经安装——跳到步骤 3。

**如果看到"command not found"** 或弹出窗口要求安装开发者工具：
- 点击弹出窗口中的 **安装**，或运行：
  ```
  xcode-select --install
  ```
- 等待安装完成（1-5 分钟）
- 验证 Git 已安装：
  ```
  git --version
  ```

你应该看到类似 `git version 2.39.0` 的内容。

## 步骤 3：使用你的身份配置 Git

Git 需要知道你是谁，以便在提交信息中显示。

- 设置你的姓名和邮箱（可以是虚构的）：
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

使用你的姓名和邮箱有助于在多人协作时识别谁做了哪些更改。

## 步骤 4：导航到你的 Documents 文件夹

- 导航到你的 Documents 文件夹：
  ```
  cd ~/Documents
  ```
- 验证你在正确的位置：
  ```
  pwd
  ```

你应该看到 `/Users/YOUR_USERNAME/Documents`。

## 步骤 5：创建项目文件夹

- 创建一个名为 `test_claude` 的文件夹：
  ```
  mkdir test_claude
  ```
- 进入该文件夹：
  ```
  cd test_claude
  ```

这就是你的项目所在的位置。

## 步骤 6：启动 Claude Code

- 启动 Claude Code：
  ```
  claude
  ```

Claude Code 启动并等待你的请求。

## 步骤 7：让 Claude 初始化 Git

- 输入此请求：
  ```
  Start tracking changes
  ```

Claude 在你的文件夹中初始化一个 Git 仓库（需要 2-5 秒）。现在你有版本控制了！

## 步骤 8：构建计时器应用

- 在 Claude Code 中，输入：
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  ```

Claude 创建包含 CSS 和 JavaScript 代码的 `timer.html`（需要 10-30 秒）。

## 步骤 9：测试计时器

- 打开 Finder
- 导航到 **Documents** > **test_claude**
- 双击 `timer.html` 在浏览器中打开
- 试用计时器：
  - 在输入框中输入 `1`
  - 点击 **Start**
  - 观看倒计时

**如果出现问题：** 在 Claude Code 中描述错误：`I'm seeing this error: [describe what happened]. Can you fix it?`

## 步骤 10：让 Claude 提交

- 在 Claude Code 中，输入：
  ```
  Save these changes.
  ```

Claude 将：
- 检查哪些文件发生了变化
- 编写描述性的提交信息
- 创建提交（需要 5-10 秒）

你创建了第一个保存点！你可以随时返回到这个工作版本。

## 步骤 11：添加预设按钮

- 在 Claude Code 中，输入：
  ```
  Add two buttons on the top. If I click on them it automatically starts 1- and 5-minute timers.
  ```
- 刷新浏览器标签页（或按 `Command (⌘) + R`）
- 测试：点击 **5 min** 按钮
- 如果正常工作，提交更改：
  ```
  Save these changes.
  ```

我们创建了第二个保存点。这个版本有两个按钮正常工作。

## 步骤 12：添加另一个按钮

- 在 Claude Code 中，输入：
  ```
  Add a 15-minute button.
  ```
- 刷新浏览器标签页（按 `Command (⌘) + R`）
- 测试：点击 **15 min** 按钮

**在本教程中：** 假装 15 分钟按钮工作不正常。先不要提交——我们将练习丢弃不良更改。

## 步骤 13：丢弃更改

有时 AI 代码不能正常工作，你需要从上一个保存点重新开始。

- 在 Claude Code 中，输入：
  ```
  discard these changes.
  ```
- Claude 会要求确认
- 输入 `yes` 并按 Enter
- 刷新浏览器——15 分钟按钮消失了

Claude 丢弃了我们不喜欢的新更改。计时器再次正常工作，只有 1 分钟和 5 分钟按钮！

## 步骤 14：添加声音通知

- 在 Claude Code 中，输入：
  ```
  Add a sound notification when time is up.
  ```
- Claude 完成后刷新浏览器并测试（将计时器设置为 0.1 分钟）
- 如果正常工作，提交更改：
  ```
  Save these changes.
  ```

## 步骤 15：添加贪睡按钮

- 在 Claude Code 中，输入：
  ```
  The sound should continue until I click a button to snooze it.
  ```
- Claude 完成后刷新浏览器并测试（将计时器设置为 0.1 分钟）
- 如果正常工作，提交更改：
  ```
  Save these changes.
  ```

## 步骤 16：查看你的提交历史

- 在 Claude Code 中，输入：
  ```
  show my change history
  ```

Claude 以可读格式显示你的提交。你会看到：
- 你的初始计时器应用提交
- 预设按钮（1 分钟和 5 分钟）提交
- 声音通知提交
- 贪睡按钮提交

注意，15 分钟按钮的尝试不在其中——你丢弃了它！

## 步骤 17：检查代码

- 在显示应用的浏览器中，右键点击并选择 **View Page Source**（或按 `Option (⌥) + Command (⌘) + U`）
- 你可以看到源代码
- 在 Claude Code 中，询问：
  ```
  Explain this code. Just big picture.
  ```

## 完整工作流程

- 让 Claude 进行更改
- 测试
- 如果正常工作 → 让 Claude 提交
- 如果失败 → 让 Claude 修复
- 无法修复 → 丢弃更改并重试
- 重复

你可以随时返回任何提交。大胆丢弃——只提交能工作的代码！

## 下一步

尝试为你的计时器添加更多功能：

- **15 分钟按钮：** `Add a working 15-minute preset button`（重做我们丢弃的功能！）
- **暂停按钮：** `Add a Pause/Resume button that toggles the timer state`
- **更好的样式：** `Improve the visual design with a modern color scheme and larger fonts`
- **进度条：** `Add a visual progress bar showing time remaining`

记住：每个功能后测试，每次成功后提交，失败时丢弃。

## 故障排除

- **"not a git repository" 错误：** 确保你在 test_claude 文件夹中（`cd ~/Documents/test_claude`）
- **在 Finder 中找不到 timer.html：** 文件位于 `/Users/YOUR_USERNAME/Documents/test_claude/timer.html`
- **Git 命令不起作用：** 确保你完成了步骤 2 并安装了 Git
- **计时器不工作：** 打开浏览器控制台（右键点击页面，选择 **检查**，然后点击 **Console** 标签），复制任何红色错误信息，粘贴给 Claude

## 你可以问 Claude 什么

- `what files have I changed?` - 查看未提交的更改
- `show me the diff` - 查看具体更改了哪些代码
- `explain what the timer code does` - 理解实现方式
- `create a branch called experiment` - 安全地尝试有风险的更改
- `go back to the previous commit` - 撤销自上次提交以来的所有操作

Claude 通过自然语言处理所有 Git 操作——无需记忆命令！

## 工作流程概述

- **设置：** 安装 Git 一次，配置身份一次
- **开发：** Claude 编写代码，你在浏览器中测试
- **版本控制：** Claude 通过简单请求处理所有 Git 操作
- **安全：** 随时丢弃不良更改，返回任何以前的提交
- **本地：** 所有内容都保存在你的计算机上，不需要账户或互联网

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 8 日。
