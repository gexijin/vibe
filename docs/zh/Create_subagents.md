[首页](./)

# 在 Claude Code 中创建 Subagent

你想比较投资机会，但研究多家公司并对它们进行评分需要花费数小时。可以把 subagent 想象成雇佣一位金融分析师，他确切地知道如何使用你的研究工具——你给他们公司名称，他们就会收集报告，在关键指标上为每家公司评分，并推荐最佳投资。一旦你学会构建 subagent，你就可以在工作中自动化任何重复性的多步骤工作流程。本教程将向你展示如何构建这样一个分析师。

## 关键概念

- **Subagent** - 一个专门的 AI 工作者，拥有自己的目标、系统提示词和工具，能够自主完成任务
- **Skill** - 一个可重用的能力（如生成股票报告），subagent 可以调用它来完成目标
- **System Prompt** - 定义 subagent 做什么、如何为公司评分以及返回什么格式的指令
- **关注点分离** - Skill 收集数据；subagent 使用这些数据做出决策

## 你需要准备什么

- 完成 [Windows 上 VS Code 中的 Claude Code](./Claude_Code_in_VS_Code_Win.md) 或 [Mac 上 VS Code 中的 Claude Code](./Claude_Code_in_VS_Code_Mac.md)
- 已安装的股票报告 skill（在 `.claude/skills/generate-stock-reports/` 中）
- VS Code 或其他文本编辑器
- 20-25 分钟

## 步骤 1：创建项目文件夹并启动 Claude Code

**Windows (WSL)：**
- 从开始菜单打开 **Ubuntu**
- 输入以下命令：
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
  将 `YOUR_USERNAME` 替换为你的 Windows 用户名
- 启动 Claude Code：
  ```
  claude
  ```

**Mac：**
- 打开 **Terminal**（在"应用程序 > 实用工具"中找到它）
- 输入以下命令：
  ```bash
  cd ~/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
- 启动 Claude Code：
  ```
  claude
  ```

Claude Code 启动并显示欢迎消息。

## 步骤 2：验证股票报告 Skill 是否存在

在构建 subagent 之前，确认 skill 可用。输入：

```
List all available skills
```

你应该在输出中看到 `generate-stock-reports`。这个 skill 研究公司并生成涵盖产品新闻、管理层更新、财务绩效和分析师见解的报告。

如果你没有看到它，skill 文件应该在 `.claude/skills/generate-stock-reports/`（项目级别）中。

## 步骤 3：理解 Subagent 与 Skill 架构

以下是 subagent 和 skill 如何协同工作：

| 组件 | 目的 | 示例 |
|-----------|---------|---------|
| **Skill** | 收集有关一家公司的原始数据 | "生成 Apple 的报告：产品、财务、管理层、分析师" |
| **Subagent** | 使用 skill 数据来完成目标 | "获取 Apple 和 Microsoft 的报告，为两者评分，推荐应该投资哪家" |

**关键区别：**
- **Skill = 工具**，用于做研究
- **Subagent = 决策者**，使用工具并应用逻辑

你的股票选择器 subagent 将：
1. 为每家公司调用股票报告 skill（2 次或更多）
2. 在各个类别中为公司评分（财务、增长、管理层、情绪）
3. 比较分数并推荐最佳投资

## 步骤 4：创建股票选择器 Subagent

输入以下命令：

```
/agents
```

你会看到 Claude Code agents 界面，显示现有的 subagent（如果有的话）以及**创建**、**编辑**或**删除** subagent 的选项。

现在创建你的 subagent：
- 选择 **Create new subagent**
- 选择 **Project**
- 选择 **Generate with Claude (recommended)**
- 粘贴以下指令：
  ```
  Create a markdown file for a new subagent called stock-picker:
  - It takes two or more stocks
  - Uses the generate-stock-reports skill to do research
  - Score cards are created based on the categories of data collected
  - A final recommendation is given.
  ```
- 在 **[Continue]** 上按 **Enter** 以使用 **All tools**
- 选择 **Sonnet** 作为模型
- 按 **Enter** 随机选择一种颜色

## 步骤 5：查看你构建的内容（反思检查点）

要在 VS Code 中打开文件，点击 **File > Open File...** 并导航到 `.claude/agents/stock-picker.md`。

或者你可以让 Claude：
```
Show me the stock-picker subagent file.
```
Claude 将显示位于 `.claude/agents/stock-picker.md` 的 subagent 文件。你会看到：

顶部有一个 **YAML frontmatter**：
```
---
name: stock-picker
description: Compares multiple companies for investment decisions...
skills: generate-stock-reports
---
```

这个 frontmatter（`---` 标记之间的部分）告诉 Claude Code 何时激活这个 subagent 以及它可以使用哪些 skill。

frontmatter 下方有一个**系统提示词**，包含你的评分方法。

**确认这些关键要素：**
- Subagent 可以访问 `generate-stock-reports` skill
- 系统提示词解释了评分细分
- Subagent 的目标很明确：比较公司并推荐一个

你可以直接编辑文件或让 Claude 更新它。

## 步骤 6：测试 Subagent

现在用真实的比较来测试你的 subagent。输入：

```
Which is a better investment: Apple or Google?
```

subagent 将根据你的描述自动激活。

## 步骤 7：观察 Subagent 工作

当 subagent 运行时，你会看到它：
1. **调用 skill 两次** - 为 Apple 调用一次 generate-stock-reports skill，然后为 Google 调用一次
2. **收集数据** - 每次 skill 调用都会搜索网络并生成公司报告
3. **为公司评分** - 在各个类别中应用 40/30/20/10 的权重
4. **生成输出** - 创建比较表和推荐

这可能需要 2-3 分钟，因为涉及网络研究。

## 步骤 8：查看输出

subagent 返回详细的分析，包括：
- **单个公司报告** - 每只股票的产品更新、财务指标、管理层变化、分析师情绪
- **比较评分卡** - 各类别的数值分数（财务健康、增长潜力、管理层质量、市场情绪）
- **最终推荐** - 应该投资哪只股票以及原因

subagent 可能会在终端中显示这些内容，或生成一个包含完整报告的 markdown 文件。你可以编辑 subagent 文件来自定义评分权重或输出格式。

## 下一步

现在你有了一个可用的股票选择器 subagent，尝试这些扩展：

- **比较 3 只或更多股票**："Compare AAPL, MSFT, and GOOGL"，看看 subagent 如何处理更多选项
- **调整评分权重**：编辑 subagent 文件以更改 40/30/20/10 的细分（例如，如果你偏好成长股，可以将增长设为 40%）
- **创建其他 subagent**：为不同任务构建"code-reviewer" subagent、"bug-hunter" subagent 或"document-writer" subagent

## 故障排除

- **Subagent 未激活**：确保你的请求提到了比较公司或投资决策。尝试："Use the stock-picker subagent to compare..."
- **找不到 Skill**：验证 `.claude/skills/generate-stock-reports/SKILL.md` 是否存在。如果刚添加，请重启 Claude Code。
- **评分不完整**：让 subagent "continue" 或"explain the scores for each category in more detail"
- **创建 subagent 时出错**：检查 `.claude/agents/` 文件夹是否存在。Claude Code 应该会自动创建它。

## 工作流程概述

- **Subagent 自动化多步骤工作流程** - 它们编排 skill、应用逻辑并提供决策
- **Skill 是可重用工具** - 一个 skill 可以被多个 subagent 用于不同目标
- **系统提示词定义行为** - 清晰的指令和评分标准使 subagent 可靠
- **Subagent 保持专注** - 每个 subagent 都有一个单一、明确的目的（股票选择、代码审查等）
- **组合可扩展** - 构建一个 skill 和 subagent 库，它们可以协同工作

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 于 2025 年 12 月 14 日创建。
