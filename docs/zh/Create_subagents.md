[首页](./)

# 在Claude Code中创建Subagent

你想比较投资机会，但研究多家公司并对它们进行评分需要花费数小时。可以把subagent想象成雇佣一位金融分析师，他确切地知道如何使用你的研究工具——给他们公司名称，他们就会收集报告，在关键指标上为每家公司评分，并推荐最佳投资。一旦你学会构建subagent，就可以在工作中自动化任何重复性的多步骤工作流程。本教程将展示如何构建这样一个分析师。

## 关键概念

- **Subagent** - 专门的AI工作者，拥有自己的目标、系统提示词和工具，能够自主完成任务
- **Skill** - 可重用的能力（如生成股票报告），subagent可以调用它来完成目标
- **System Prompt** - 定义subagent做什么、如何为公司评分以及返回什么格式的指令
- **关注点分离** - Skill收集数据；subagent使用这些数据做出决策

## 你需要准备什么

- 完成[Windows上VS Code中的Claude Code](./Claude_Code_in_VS_Code_Win.md)或[Mac上VS Code中的Claude Code](./Claude_Code_in_VS_Code_Mac.md)
- 已安装的股票报告skill（在`.claude/skills/generate-stock-reports/`中）
- VS Code或其他文本编辑器
- 20-25分钟

## 步骤1：创建项目文件夹并启动Claude Code

**Windows (WSL)：**
- 从开始菜单打开**Ubuntu**
- 输入以下命令：
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
  将`YOUR_USERNAME`替换为你的Windows用户名
- 启动Claude Code：
  ```
  claude
  ```

**Mac：**
- 打开**Terminal**（在"应用程序 > 实用工具"中找到它）
- 输入以下命令：
  ```bash
  cd ~/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
- 启动Claude Code：
  ```
  claude
  ```

Claude Code启动并显示欢迎消息。

## 步骤2：验证股票报告Skill是否存在

在构建subagent之前，确认skill可用。输入：

```
List all available skills
```

应该在输出中看到`generate-stock-reports`。这个skill研究公司并生成涵盖产品新闻、管理层更新、财务绩效和分析师见解的报告。

如果没有看到它，skill文件应该在`.claude/skills/generate-stock-reports/`（项目级别）中。

## 步骤3：理解Subagent与Skill架构

以下是subagent和skill如何协同工作：

| 组件 | 目的 | 示例 |
|-----------|---------|---------|
| **Skill** | 收集有关一家公司的原始数据 | "生成Apple的报告：产品、财务、管理层、分析师" |
| **Subagent** | 使用skill数据来完成目标 | "获取Apple和Microsoft的报告，为两者评分，推荐应该投资哪家" |

**关键区别：**
- **Skill = 工具**，用于做研究
- **Subagent = 决策者**，使用工具并应用逻辑

你的股票选择器subagent将：
1. 为每家公司调用股票报告skill（2次或更多）
2. 在各个类别中为公司评分（财务、增长、管理层、情绪）
3. 比较分数并推荐最佳投资

## 步骤4：创建股票选择器Subagent

输入以下命令：

```
/agents
```

会看到Claude Code agents界面，显示现有的subagent（如果有的话）以及**创建**、**编辑**或**删除**subagent的选项。

现在创建你的subagent：
- 选择**Create new subagent**
- 选择**Project**
- 选择**Generate with Claude (recommended)**
- 粘贴以下指令：
  ```
  Create a markdown file for a new subagent called stock-picker:
  - It takes two or more stocks
  - Uses the generate-stock-reports skill to do research
  - Score cards are created based on the categories of data collected
  - A final recommendation is given.
  ```
- 在**[Continue]**上按**Enter**以使用**All tools**
- 选择**Sonnet**作为模型
- 按**Enter**随机选择一种颜色

## 步骤5：查看你构建的内容（反思检查点）

要在VS Code中打开文件，点击**File > Open File...**并导航到`.claude/agents/stock-picker.md`。

或者让Claude：
```
Show me the stock-picker subagent file.
```
Claude将显示位于`.claude/agents/stock-picker.md`的subagent文件。会看到：

顶部有一个**YAML frontmatter**：
```
---
name: stock-picker
description: Compares multiple companies for investment decisions...
skills: generate-stock-reports
---
```

这个frontmatter（`---`标记之间的部分）告诉Claude Code何时激活这个subagent以及它可以使用哪些skill。

frontmatter下方有一个**系统提示词**，包含你的评分方法。

**确认这些关键要素：**
- Subagent可以访问`generate-stock-reports` skill
- 系统提示词解释了评分细分
- Subagent的目标很明确：比较公司并推荐一个

可以直接编辑文件或让Claude更新它。

## 步骤6：测试Subagent

现在用真实的比较来测试subagent。输入：

```
Which is a better investment: Apple or Google?
```

subagent将根据描述自动激活。

## 步骤7：观察Subagent工作

当subagent运行时，会看到它：
1. **调用skill两次** - 为Apple调用一次generate-stock-reports skill，然后为Google调用一次
2. **收集数据** - 每次skill调用都会搜索网络并生成公司报告
3. **为公司评分** - 在各个类别中应用40/30/20/10的权重
4. **生成输出** - 创建比较表和推荐

这可能需要2-3分钟，因为涉及网络研究。

## 步骤8：查看输出

subagent返回详细的分析，包括：
- **单个公司报告** - 每只股票的产品更新、财务指标、管理层变化、分析师情绪
- **比较评分卡** - 各类别的数值分数（财务健康、增长潜力、管理层质量、市场情绪）
- **最终推荐** - 应该投资哪只股票以及原因

subagent可能会在终端中显示这些内容，或生成一个包含完整报告的markdown文件。可以编辑subagent文件来自定义评分权重或输出格式。

## 下一步

现在你有了一个可用的股票选择器subagent，尝试这些扩展：

- **比较3只或更多股票**："Compare AAPL, MSFT, and GOOGL"，看看subagent如何处理更多选项
- **调整评分权重**：编辑subagent文件以更改40/30/20/10的细分（例如，如果偏好成长股，可以将增长设为40%）
- **创建其他subagent**：为不同任务构建"code-reviewer" subagent、"bug-hunter" subagent或"document-writer" subagent

## 故障排除

- **Subagent未激活**：确保请求提到了比较公司或投资决策。尝试："Use the stock-picker subagent to compare..."
- **找不到Skill**：验证`.claude/skills/generate-stock-reports/SKILL.md`是否存在。如果刚添加，请重启Claude Code。
- **评分不完整**：让subagent "continue"或"explain the scores for each category in more detail"
- **创建subagent时出错**：检查`.claude/agents/`文件夹是否存在。Claude Code应该会自动创建它。

## 工作流程概述

- **Subagent自动化多步骤工作流程** - 它们编排skill、应用逻辑并提供决策
- **Skill是可重用工具** - 一个skill可以被多个subagent用于不同目标
- **系统提示词定义行为** - 清晰的指令和评分标准使subagent可靠
- **Subagent保持专注** - 每个subagent都有一个单一、明确的目的（股票选择、代码审查等）
- **组合可扩展** - 构建一个skill和subagent库，它们可以协同工作

---

由[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)于2025年12月14日创建。
