[首页](./)

# 创建你的第一个 Claude Skill

你一直在手动输入 `/stock-report AAPL` 来生成报告。如果 Claude 能够根据你的对话自动决定何时创建股票报告会怎么样？这就是 Skill 的强大之处——就像从手动换挡升级到自动变速箱，能在需要时自动换挡。

## 核心概念

- **Skill** - 存储在 `.claude/skills/` 中的模型调用能力，Claude 会根据上下文自动激活
- **模型调用（Model-invoked）** - Claude 通过阅读 Skill 的描述来决定何时使用它，无需你输入命令
- **SKILL.md** - 包含 YAML 前置内容（元数据）和 Claude 指令的主文件

## 你需要准备什么

- 完成[创建自定义 Slash 命令](./Reuse_Prompts_via_Slash_Commands.md)教程
- 该教程中的 `stock-report` slash 命令
- 已安装 VS Code
- 10-15 分钟

## 步骤 1：导航到项目文件夹

**Windows（WSL）：**
- 从开始菜单打开 **Ubuntu**
- 输入：
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  将 `YOUR_USERNAME` 替换为你的 Windows 用户名

  如果文件夹不存在，请先创建它：
  ```bash
  mkdir -p /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```

**Mac：**
- 打开 **Terminal**（应用程序 > 实用工具）
- 输入：
  ```bash
  cd ~/Documents/test_claude
  ```

  如果文件夹不存在，请先创建它：
  ```bash
  mkdir -p ~/Documents/test_claude
  cd ~/Documents/test_claude
  ```

## 步骤 2：启动 Claude Code

输入：
```
claude
```

Claude Code 启动并显示欢迎信息。

## 步骤 3：启用编辑自动批准

按 `Ctrl+E`（Windows/Linux）或 `Cmd+E`（Mac）来启用编辑自动批准模式。

这样可以让 Claude 创建和修改文件，而无需每次都请求权限。

## 步骤 4：让 Claude 转换 Slash 命令

输入以下提示：
```
Convert my stock-report slash command to a Skill called generate-stock-reports.
The Skill should activate automatically when I ask about companies or stocks.
```

Claude 会分析你现有的 slash 命令，并将其转换为 `.claude/skills/stock-report/` 中的 Skill。

**发生了什么：** Claude 创建了一个新的文件夹结构，其中 `SKILL.md` 包含 YAML 前置内容，告诉 Claude 何时自动使用这个 Skill。

## 步骤 5：查看 Skill 结构

打开 VS Code 并查看项目：
- 点击 **File > Open Folder**
- 选择 `Documents/test_claude`
- 在文件浏览器中，导航到 `.claude/skills/stock-report/`
- 点击 `SKILL.md` 打开它

注意其结构：
```yaml
---
name: stock-report
description: Generates reports on companies... Use when users ask about stocks, companies, or ticker symbols.
---

[Rest of the instructions]
```

`description` 字段是关键——它准确地告诉 Claude 何时自动激活这个 Skill。

## 步骤 6：测试 Skill（无需输入命令）

不要输入 `/stock-report AAPL`，只需提出一个自然的问题：
```
What's happening with Apple lately?
```

**关键区别：** 你没有输入命令。Claude 阅读你的问题，识别出你在询问某家公司，检查 Skill 描述，然后自动决定使用 stock-report Skill。

观察 Claude 的工作——它应该生成与之前看到的相同的综合报告。

## 步骤 7：比较两种方法

**Slash 命令（手动）：**
```
/stock-report AAPL
```
- 你明确告诉 Claude 要做什么
- 每次都一样
- 适合重复的、可预测的任务

**Skill（自动）：**
```
Tell me about Tesla's recent developments
```
或
```
I'm thinking about investing in Microsoft
```
或
```
What's NVIDIA up to?
```
- Claude 决定是否使用 Skill
- 更自然的对话
- 适合 Claude 为你管理的复杂工作流程

## 步骤 8：测试边缘情况

尝试不应该触发股票报告 Skill 的问题：
```
How do I install Python?
```

Claude 正常回答，不调用 Skill。

现在尝试一个应该触发它的问题：
```
Compare Google and Meta
```

Claude 应该使用 Skill 两次——一次用于 Google，一次用于 Meta。

## 步骤 9：修改 Skill 描述（可选）

让我们使 Skill 更具选择性。询问 Claude：
```
Update the stock-report Skill to only activate when I explicitly mention
"analyze" or "report" along with a company name.
```

Claude 会更新 `SKILL.md` 中的 `description` 字段。测试差异：
```
What's Apple doing?
```
（现在可能不会触发 Skill）

```
Analyze Apple
```
（应该触发 Skill）

## 下一步

既然你已经理解了 Skill，为你的工作流程创建更多：

- **Research Skill** - 当你提出需要网络研究的问题时自动激活
- **Code Review Skill** - 当你提到错误、问题或代码问题时激活
- **Meeting Notes Skill** - 当你粘贴会议记录或提到摘要时激活

模式是：定义 Claude 何时应该自动帮助，而不仅仅是你手动触发的快捷方式。

## 故障排除

- **Skill 未激活：** 检查 `SKILL.md` 中的 `description` 字段——它必须包含与你的问题相关的触发词
- **Skill 激活过于频繁：** 使描述更具体地说明何时使用它
- **找不到 Skill 文件夹：** Skill 位于 `.claude/skills/`（隐藏文件夹——在文件浏览器中启用"显示隐藏文件"）
- **对 SKILL.md 的更改不起作用：** Skill 在修改后会自动加载——无需重启。如果仍然不起作用，请检查 YAML 格式

## 工作流程概述

- **Slash 命令**是你手动输入的快捷方式（类似书签）
- **Skill**是 Claude 自动发现和使用的能力（类似了解你偏好的助手）
- **Skill 描述**充当指令，告诉 Claude："当用户说 X 时使用我"
- **两者可以共存** - 使用 slash 命令执行快速、重复的任务；使用 Skill 处理复杂的工作流程
- **Skill 更具扩展性** - 你不需要记住命令名称；Claude 根据上下文决定

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 13 日。
