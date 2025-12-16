[首页](./)

# 创建自定义 Slash Command

厌倦了反复输入相同的详细提示词?自定义 slash command 让你将复杂指令保存为可重复使用的快捷方式。就像为常用任务创建键盘快捷键,slash command 可以将冗长提示词转化为简单命令,例如 `/stock-report Apple` 就能立即生成综合报告。

最棒的部分?我们用 Claude 来编写详细提示词并创建 Skill。是的,Claude 非常擅长为……自己编写提示词。

## 核心概念

- **Slash command** - 可重复使用的提示词,以 Markdown 文件形式存储,输入 `/command-name` 时 Claude Code 会执行
- **参数(Arguments)** - 传递给命令的变量(如股票代码),使用特殊关键字 `$ARGUMENTS`
- **`.claude/commands/` 文件夹** - Claude Code 自动发现和加载自定义命令的位置

## 你需要准备的内容

- 完成 [Windows 上的 VS Code 中的 Claude Code](./Claude_Code_in_VS_Code_Win.md) 或 [Mac 上的 VS Code 中的 Claude Code](./Claude_Code_in_VS_Code_Mac.md)
- 一个研究主题(我们将使用股票报告作为示例)
- 安装文本编辑器,如 VS Code
- 15-20 分钟

## 步骤 1:创建项目文件夹

**Windows(WSL):**
- 从开始菜单打开 **Ubuntu**
- 输入以下命令:
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir test_claude
  cd test_claude
   ```
  将 `YOUR_USERNAME` 替换为你的 Windows 用户名

**Mac:**
- 打开 **Terminal**(在 应用程序 > 实用工具 中找到)
- 输入以下命令:
  ```bash
  cd ~/Documents
  mkdir test_claude
  cd test_claude
  ```

## 步骤 2:启动 Claude Code

**Windows(WSL):**
- 仍在 Ubuntu 终端中,输入:
  ```
  claude
  ```

**Mac:**
- 仍在 Terminal 中,输入:
  ```
  claude
  ```

Claude Code 启动并显示欢迎消息。

## 步骤 3:让 Claude 创建 Slash Command

无需手动创建文件,让 Claude 来完成。输入此提示词:

```
创建一个名为 stock-report 的 slash command,用于生成
通过公司名称或股票代码识别的公司近期发展报告。
包含:
- 产品或服务新闻
- 管理团队新闻
- 近期财务报告
- 分析师报告
```
当被询问时,授权 Claude 创建文件。
Claude 会创建详细提示词,并保存为 `stock-report.md` 到 `.claude/commands/` 文件夹。

**注意:** 我们在所有地方都使用 Markdown 格式:提示词、报告和 slash command。Markdown 对 AI 友好,可以轻松作为纯文本文件编辑。

## 步骤 4:查看命令

用任何文本编辑器打开 `.claude/commands/` 文件夹中的 `stock-report.md` 文件。这就是 slash command 的提示词。

如果安装了 VS Code(推荐):
- 启动 VS Code
- 从 **File** 菜单,选择 **Open folder**,选择项目文件夹 `Documents/test_claude`
- 从文件资源管理器,导航到 `.claude/commands` 并点击文件 `stock-report.md` 打开

查看提示词,如需要可以修改指令。

**注意:** Claude 在编写提示词方面非常出色。可以看到它的提示词使用 markdown 格式,结构良好且清晰。学习这样编写提示词。它有时甚至会包含指令,在标识符不明确时要求澄清。

## 步骤 5:测试命令

首先按 **Ctrl+C** 两次**退出**当前 Claude Code 会话。然后重新启动 Claude,以便加载新 slash command:
  ```
  claude
  ```
现在用真实股票代码测试新命令:

```
/stock-report Apple
```

Claude 会搜索网络并生成关于 Apple Inc. 的综合报告。这可能需要 1-2 分钟。

## 步骤 6:查看生成的报告

Claude 在命令行创建报告。查看输出:

- 检查每个部分是否有相关的最新信息
- 验证来源是否可信且最新
- 注意 Claude 如何组织信息

## 步骤 7:将报告保存到文件

让我们修改 slash command,使其自动将报告保存为 markdown 文件。手动将以下内容附加到 slash command markdown 文件。

- 打开 `.claude/commands/` 文件夹中的 `stock-report.md` 文件
- 将以下内容附加到末尾。
  ```
  将报告保存为 markdown 文件。文件名包含公司名称和日期。
  ```
- 保存文件。

## 步骤 8:重新运行命令

- 首先按 **Ctrl+C** 两次**退出**当前 Claude Code 会话。然后重新启动 Claude,以便加载新 slash command:
  ```
  claude
  ```
- 现在用真实股票代码测试新命令:

  ```
  /stock-report AAPL
  ```
- 打开报告

Claude 生成报告并保存为名为 `Apple_2025-12-13.md` 之类的 markdown 文件。在 VS Code 中点击文件查看。

## 步骤 9:通过 Claude 修改命令

可以让 Claude 编辑 slash command:

```
修改 stock-report slash command,将报告保存为 html 文件。
```

Claude 更新命令文件。可以从编辑器验证。

## 步骤 10:测试更新后的命令

- 首先按 **Ctrl+C** 两次**退出**当前 Claude Code 会话。然后重新启动 Claude,以便加载新 slash command:
  ```
  claude
  ```

- 测试增强后的命令:

  ```
  /stock-report AAPL
  ```

Claude 创建名为 `Apple_2025-12-13.html` 之类的文件。在 Windows 或 Mac 上从文件资源管理器点击此文件,在默认浏览器打开。

## 步骤 11:重复使用 slash command(可选)

slash command 中的 `$ARGUMENTS` 关键字充当占位符。输入 `/stock-report AAPL` 时,Claude 在执行提示词前会用 `AAPL` 替换 `$ARGUMENTS`。

尝试另一个股票代码:

```
/stock-report TSLA
```

相同命令结构现在研究的是特斯拉。

## 步骤 12:尝试另一个 Slash Command(可选)

如果完成了[使用 Claude Code 撰写研究论文](./Writing_Research_Paper_Claude_Code.md)教程,应该有一个 `/research-paper` 命令。在新主题上测试它。

首先,清除 Claude 的内存重新开始:

```
/clear
```

然后运行研究论文命令:

```
/research-paper AI in schools
```

两个关键区别:
- `/research-paper` 是在会话结束时通过捕获人类交互创建的,而 `/stock-report` 是从头开始创建的。
- `/research-paper` 在起草论文前会交互式地询问输入。

## 下一步

现在理解了 slash command,为工作流程创建更多自定义命令:

- **代码审查:** `/review-code` - 分析代码以查找错误和改进
- **会议记录:** `/meeting-summary` - 生成结构化会议摘要
- **电子邮件草稿:** `/email-reply` - 创建专业电子邮件回复

## 故障排除

- **找不到命令:** 重新启动 Claude Code 以从 `.claude/commands/` 重新加载命令
- **参数不起作用:** 检查命令文件中的 `$ARGUMENTS` 拼写是否正确(区分大小写)
- **报告不完整:** 要求 Claude "继续" 或 "为[部分名称]部分添加更多细节"

## 工作流程概述

- **自定义 slash command** 通过将复杂提示词转化为简单快捷方式来节省时间
- **参数**使命令能够灵活处理不同输入(股票代码、主题、文件)
- **Claude 构建命令** - 无需手动编写 Markdown 文件;只需描述想要什么
- **命令可重复使用** - 一旦创建,就可以在项目和会话中使用
- **组合命令** - 为不同任务构建专业命令库

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 13 日。
