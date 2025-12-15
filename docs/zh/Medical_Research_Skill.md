[首页](./)

# 创建用于医学研究的 Claude Skill

跟上医学研究进展意味着要阅读充满专业术语的密集科学论文。Claude Skill 就像拥有一个研究助手，能够阅读数百篇论文并用通俗易懂的语言解释它们——无需花费数小时搜索 PubMed 和解读技术语言，你只需提出一个简单的问题，就能获得基于最新科学研究的清晰摘要。

在本教程中，你将创建一个可以搜索同行评审医学文献的 Claude Skill。我们首先创建一个 Python 脚本来查询 PubMed。最棒的是什么？你可以让 Claude 完成所有工作！它有一个创建 Skill 的 Skill！

## 关键概念

- **Claude Skill** - 一种专门的工具，通过存储在 `.claude/skills/` 中的自定义指令、代码和文档来扩展 Claude Code 的功能
- **PubMed** - 由美国国家医学图书馆维护的免费数据库，包含超过 3500 万篇生物医学研究论文
- **Biopython** - Python 库，提供以编程方式查询 PubMed 数据库的工具
- **自动编辑模式** - 通过 Shift+Tab 激活的功能，允许 Claude 进行多次文件更改而无需每次都请求许可

## 你需要准备什么

- 完成 [Windows 上 VS Code 中的 Claude Code](./Claude_Code_in_VS_Code_Win.md) 或 [Mac 上 VS Code 中的 Claude Code](./Claude_Code_in_VS_Code_Mac.md)
- 用于 PubMed 搜索的互联网连接
- 15-20 分钟

## 步骤 1：导航到项目文件夹

如果你完成了[斜杠命令教程](./Reuse_Prompts_via_Slash_Commands.md)，`test_claude` 文件夹已经存在。无论哪种情况，这些命令都可以使用。

**Windows (WSL)：**
- 从开始菜单打开 **Ubuntu**
- 输入以下命令：
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir -p test_claude
  cd test_claude
  ```
  将 `YOUR_USERNAME` 替换为你的 Windows 用户名

**Mac：**
- 打开 **Terminal**（在应用程序 > 实用工具中找到）
- 输入以下命令：
  ```bash
  cd ~/Documents
  mkdir -p test_claude
  cd test_claude
  ```

`-p` 标志会在文件夹不存在时创建它，如果已存在则不执行任何操作。

## 步骤 2：启动 Claude Code

输入以下命令：
```bash
claude
```

Claude Code 启动并显示欢迎消息。

## 步骤 3：启用自动编辑模式

按 **Shift+Tab** 启用自动编辑模式。你会看到一条确认消息。

自动编辑模式允许 Claude 创建和修改多个文件，而无需每次都请求许可。这对于构建涉及创建多个文件的 skill 至关重要。

## 步骤 4：创建 PubMed 搜索脚本

复制并粘贴以下提示：

```
Write a Python script called pubmed_search.py that:
- Takes a search query as command line argument
- Retrieves up to 10 recent papers
- Returns PMID, title, authors, journal, year, abstract preview, and URL
```
Claude 会创建脚本。它会安装所需的 Biopython 包，其中包括用于与 PubMed 交互的 entrez 模块。查看输出以了解脚本结构。

## 步骤 5：测试脚本

让 Claude 测试它：

```
Test the script with the query "immunotherapy breast cancer"
```

Claude 运行脚本并显示 10 篇关于乳腺癌免疫治疗的最新论文。你会看到标题、作者、摘要和 PubMed 链接。

**注意：** 搜索找到了数千篇论文，但仅检索最近的 10 篇以供快速查看。

## 步骤 6：创建医学研究 Skill

现在我们将把所有内容打包成一个可重用的 skill。复制并粘贴：

```
Create a Claude Skill called "medical-research" that:
- Takes on a medical question
- Designs queries to retrieve PubMed abstracts
- Creates plain-language summaries accessible to non-scientists
- Includes the pubmed_search.py script inside the skill folder
```

Claude 创建完整的 skill 结构：
- `.claude/skills/medical-research/pubmed_search.py` - 搜索脚本
- `.claude/skills/medical-research/SKILL.md` - 关于如何使用该 skill 的 Claude 指令
- `.claude/skills/medical-research/README.md` - 用户文档
- `.claude/skills/medical-research/EXAMPLES.md` - 示例输出

这需要 2-3 分钟，因为 Claude 会编写全面的文档。

## 步骤 7：测试 Skill

用通俗的语言提出一个研究问题：

```
Can I lose weight via keto diet?
```

Claude 会自动：
- 识别这是一个医学研究问题
- 激活 medical-research skill
- 在 PubMed 中搜索相关论文
- 分析研究结果
- 用通俗的语言解释研究，涵盖有效性、机制和注意事项

回复包括"工作原理"、"研究结果"、"重要注意事项"和"结论"等部分。

## 步骤 8：测试另一个问题

尝试另一个研究主题：

```
Does vaccine cause autism?
```

回复会解释科学共识、这个谬论的起源以及现实世界的后果。

## 步骤 9：探索 Skill 文件（可选）

打开 VS Code 查看 skill 结构：

**Windows：**
- 打开 **文件资源管理器**，导航到 `C:\Users\YOUR_USERNAME\Documents\test_claude`
- 右键单击文件夹并选择 **使用 Code 打开**

**Mac：**
- 打开 **Finder**，导航到 `Documents/test_claude`
- 右键单击文件夹并选择 **使用 Visual Studio Code 打开**
- 或者直接从 Terminal 输入 ``` code . ```

在 VS Code 中：
- 在文件资源管理器中展开 `.claude/skills/medical-research/`
- 打开 `SKILL.md` 查看 Claude 的详细指令
- 打开 `README.md` 查看用户文档
- 打开 `pubmed_search.py` 查看 Python 代码

**注意：** 该 skill 是完全独立的——所有代码和文档都存放在一个文件夹中。

## 步骤 10：从 Anthropic 的存储库安装 Skill

Anthropic 维护了一个预构建 skill 的存储库，你可以立即安装和使用。

- 要从存储库安装 skill，只需询问 Claude：

  ```
  Install the document skill from Anthropic's repository
  ```
- 尝试这个 skill：
  ```
  Create a PowerPoint presentation on Claude Skills.
  ```


**document skill** 帮助你读写 PDF、Word、PowerPoint 和 Excel 文件。Claude 会将该 skill 克隆到你的 `.claude/skills/` 文件夹中。

**Anthropic 存储库中的其他可用 skill：**
- 在 [github.com/anthropics/claude-skills](https://github.com/anthropics/skills) 浏览完整目录
- 询问 Claude "What skills are available in the Anthropic repository?" 查看当前列表

## 下一步

- **PDF：** 在此项目文件夹的子文件夹中复制几个 PDF 文件并请求摘要。
- **其他公共 skill：** 尝试 Anthropic 提供的 skill。
- **分享 skill：** Skill 只是压缩文件夹！
- **创建其他 skill：** 任何你感兴趣的内容。例如，你可以将自己的数据文件放在 skill 文件夹中。

## 故障排除

- **Biopython 未安装：** Claude 会在创建脚本时自动安装 Biopython。如果在测试时看到导入错误，请让 Claude 使用 `pip install biopython` 手动安装 Biopython
- **找不到脚本：** 检查是否启用了自动编辑模式（Shift+Tab）——Claude 需要许可才能创建文件
- **Skill 未激活：** 该 skill 在创建后应立即工作——尝试重新提出问题，或检查 SKILL.md 的标题中是否有正确的 `name: medical-research`

## 工作流程概述

- **Claude Skills** 比斜杠命令更强大——它们结合了代码、文档和自定义指令
- **自动编辑模式**（Shift+Tab）通过避免重复的许可提示来简化创建过程
- **独立打包** - 脚本存放在 skill 文件夹内，使其具有可移植性和可分享性
- **自动激活** - Skill 根据问题模式触发（研究问题激活 medical-research）
- **通俗语言界面** - 提出自然问题，无需了解技术细节

## Skill 与斜杠命令的比较

| 功能 | Skill | 斜杠命令 |
|---------|--------|----------------|
| **包含内容** | 提示、代码、数据和文档 | 仅提示 |
| **激活方式** | 在相关时自动加载 | 使用 `/command` 手动触发 |
| **使用场景** | 需要代码执行的复杂工作流程 | 快速提示模板和工作流程 |
| **文件位置** | `.claude/skills/skill-name/` | `.claude/commands/` |
| **结构** | 多个文件（SKILL.md、README.md、代码文件） | 每个命令一个 `.md` 文件 |

**关键要点：** 斜杠命令只是从 UI 注入提示。它很有用，但功能有限。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 13 日。
