# Vibe 教程文档

本仓库包含关于使用 Claude Code、VS Code 及相关开发工具的全面初学者友好教程。所有教程都是为没有任何编程经验的完全初学者设计的。

## 学习路径

这些教程遵循 `index.html` 中交互式图表所示的进度。以下是推荐的学习顺序：

### Windows - 基础路径（研究与写作）
1. `Install_CLAUDE_Code_Win.md` - 通过 WSL 安装 Claude Code
2. `Claude_Code_Basic_Operations.md` - 基本 Claude Code 操作
3. `VS_Code_Getting_Started.md` - VS Code 基础入门
4. `Claude_Code_in_VS_Code_Win.md` - 将 VS Code 连接到 Claude Code
5. `Writing_Research_Paper_Claude_Code.md` - 完整的研究论文工作流程
6. `Reuse_Prompts_via_Slash_Commands.md` - 创建自定义斜杠命令
7. `Create_Your_First_Claude_Skill.md` - 构建你的第一个 Claude 技能
8. `Medical_Research_Skill.md` - 使用 Claude 技能进行医学研究
9. `Create_subagents.md` - 构建自主代理

**Windows 替代路径：**
- `Claude_Code_Git_Windows.md` - 本地版本控制（从第1步分支）
- `Claude_Code_WSL_RStudio_Windows.md` - 在 Claude Code 中使用 RStudio（从第1步分支）

### Mac - 基础路径（研究与写作）
1. `Install_Claude_Code_MacOS.md` - 在 macOS 上安装 Claude Code
2. `Claude_Code_Basic_Operations.md` - 基本 Claude Code 操作
3. `VS_Code_Getting_Started.md` - VS Code 基础入门
4. `Claude_Code_in_VS_Code_Mac.md` - 将 VS Code 连接到 Claude Code
5. `Writing_Research_Paper_Claude_Code.md` - 完整的研究论文工作流程
6. `Reuse_Prompts_via_Slash_Commands.md` - 创建自定义斜杠命令
7. `Create_Your_First_Claude_Skill.md` - 构建你的第一个 Claude 技能
8. `Medical_Research_Skill.md` - 使用 Claude 技能进行医学研究
9. `Create_subagents.md` - 构建自主代理

**Mac 替代路径：**
- `Claude_Code_Git_Mac.md` - 本地版本控制（从第1步分支）
- `Claude_Code_RStudio_Mac.md` - 在 Claude Code 中使用 RStudio（从第1步分支）

### R 编程路径
**主要路径（Docker + VS Code）：**
1. 安装 Claude Code（`Install_CLAUDE_Code_Win.md` 或 `Install_Claude_Code_MacOS.md`）
2. `VS_Code_Getting_Started.md` - VS Code 基础
3. `R_Coding_VS_Code_Guide.md` - 在 VS Code 中设置 R 开发环境
4. `R_Coding_Docker_Guide.md` - Docker 容器中的 R，实现可重现性
5. `Vibe_Coding_R_Docker_Guide.md` - 使用 vibe 编程构建 NBA 仪表板

**支持技能（从第1步分支）：**
- `Github_desktop.md` - 使用 GitHub Desktop 进行版本控制基础
- `GitHub_Desktop_Claude_Code_Workflow.md` - 集成开发工作流程

**R 替代路径：**
- **Mac 上的 RStudio：** 安装 → `Claude_Code_RStudio_Mac.md`
- **Windows 上的 RStudio：** 安装 → `Claude_Code_WSL_RStudio_Windows.md`
- **Claude Code + R（仅限 Mac）：** VS Code 中的 R → `Claude_Code_R_VS_Code_Mac.md`

### Python 编程路径
**主要路径（Docker + VS Code）：**
1. 安装 Claude Code（`Install_CLAUDE_Code_Win.md` 或 `Install_Claude_Code_MacOS.md`）
2. `VS_Code_Getting_Started.md` - VS Code 基础
3. `Python_Coding_VS_Code_Guide.md` - 在 VS Code 中设置 Python 开发环境
4. `Python_Coding_Docker_Guide.md` - Docker 容器中的 Python
5. `Vibe_Coding_Python_Docker_Guide.md` - 使用 Python 和 Streamlit 进行 Vibe 编程

**支持技能（从第1步分支）：**
- `Github_desktop.md` - 使用 GitHub Desktop 进行版本控制基础
- `GitHub_Desktop_Claude_Code_Workflow.md` - 集成开发工作流程

**Python 替代路径：**
- **Claude Code + Python（仅限 Mac）：** VS Code 中的 Python → `Claude_Code_Python_VS_Code_Mac.md`

## 内容概览

### 安装指南
- `Install_CLAUDE_Code_Win.md` - 通过 WSL2 和 Ubuntu 在 Windows 上安装
- `Install_Claude_Code_MacOS.md` - 使用 Terminal 在 macOS 上安装

### VS Code 设置
- `VS_Code_Getting_Started.md` - 为初学者提供完整的 VS Code 基础知识
- `Claude_Code_in_VS_Code_Win.md` - 在 Windows 的 VS Code 中运行 Claude Code
- `Claude_Code_in_VS_Code_Mac.md` - 在 Mac 的 VS Code 中运行 Claude Code

### 核心操作
- `Claude_Code_Basic_Operations.md` - 基本 Claude Code 命令和工作流程

### Git 与版本控制
- `Claude_Code_Git_Windows.md` - Windows 上的 Git 基础和本地版本控制
- `Claude_Code_Git_Mac.md` - Mac 上的 Git 基础和本地版本控制
- `Github_desktop.md` - 面向初学者的 GitHub Desktop
- `GitHub_Desktop_Claude_Code_Workflow.md` - Claude Code + GitHub 集成工作流程

### R 编程指南
- `R_Coding_VS_Code_Guide.md` - VS Code 中的 R 开发环境
- `R_Coding_Docker_Guide.md` - Docker 容器中的 R，实现可重现性
- `Vibe_Coding_R_Docker_Guide.md` - 使用 Shiny 构建 NBA 仪表板
- `Claude_Code_RStudio_Mac.md` - Mac 上 Claude Code 与 RStudio 的集成
- `Claude_Code_WSL_RStudio_Windows.md` - 通过 WSL 在 Windows 上使用 Claude Code 与 RStudio
- `Claude_Code_R_VS_Code_Mac.md` - Mac 上 VS Code 中的简化 R 编程

### Python 编程指南
- `Python_Coding_VS_Code_Guide.md` - VS Code 中的 Python 开发环境
- `Python_Coding_Docker_Guide.md` - Docker 容器中的 Python
- `Vibe_Coding_Python_Docker_Guide.md` - 使用 vibe 编程构建 Streamlit 仪表板
- `Claude_Code_Python_VS_Code_Mac.md` - Mac 上 VS Code 中的简化 Python 编程

### 高级教程
- `Create_Your_First_Claude_Skill.md` - 创建自定义 Claude Code 技能
- `Create_subagents.md` - 为复杂任务构建专门的子代理
- `Reuse_Prompts_via_Slash_Commands.md` - 创建可重用的斜杠命令
- `Medical_Research_Skill.md` - 使用 Claude Code 进行医学研究

### 研究与写作项目
- `Writing_Research_Paper_Claude_Code.md` - 完整的学术写作工作流程
- `example_paper.md` - 研究论文教程的示例输出

## 可用技能

Claude Code 技能通过专门的功能扩展其能力：

### 文档处理技能
- **docx** - Microsoft Word 文档的创建、编辑和分析
- **pdf** - PDF 操作、文本提取、表单填充和生成
- **pptx** - PowerPoint 演示文稿的创建、编辑和分析
- **xlsx** - Excel 电子表格的创建、分析、公式和可视化

### 研究技能
- **medical-research** - PubMed 搜索和科学文献摘要
- **generating-stock-reports** - 公司研究和股票分析报告

### 数据分析技能
- **csv-stats** - CSV 文件统计和数据分析

## 斜杠命令

通过 `.claude/commands/` 提供的自定义命令：

- `/tutorial [topic]` - 按照样式指南创建新的初学者友好教程
- `/review-tutorial [file]` - 审查和优化现有教程的清晰度、准确性和格式
- `/review-translation [file]` - 审查和更新日语翻译以匹配英文原文
- `/bioinfo-newsletter` - 从博客内容生成生物信息学研究通讯

## 写作风格指南

所有教程遵循以下原则：

### 目标受众
- 没有编程经验的完全初学者
- 学习开发工具的非技术用户
- 没有行话的清晰解释

### 结构
- 顶部有 `[首页](./)` 链接
- 引人入胜的开场白（2-4句话）
- 关键概念部分（最多3-4个术语）
- 你需要什么（先决条件 + 时间估计）
- 逐步说明，使用 `## 步骤 N：动词 + 内容` 格式
- 下一步部分（2-3个建议）
- 故障排除部分（2-3个常见问题）
- 底部注明创建日期和作者

### 格式
- 使用项目符号（-）表示子步骤，而不是编号列表
- UI 元素使用粗体：**按钮名称**
- 命令使用反引号：`command`
- 多行命令使用代码块
- 短段落（最多2-3句话）
- 使用基于菜单的说明而非键盘快捷键

### 长度
- 目标约400行或更少
- 专注于必要信息
- 删除不必要的解释
- 保持可操作性和简洁性

## 日语翻译

完整的日语翻译可在 `ja/` 文件夹中找到。所有英文教程都有相应的日语版本，文件名结构相同：

- 所有安装指南
- 所有 VS Code 设置指南
- 所有编程指南（R 和 Python）
- 所有 Git 和 GitHub 指南
- 所有高级教程
- 研究和写作项目

翻译指南：
- 技术术语（Git、Docker、VS Code）保持英文
- 命令行指令从不翻译
- UI 元素在适用时匹配日语本地化
- 使用です/ます形式的自然流畅的日语
- 整个文档保持术语一致性

## 文件结构

```
docs/
├── index.html                              # 带有教程图表的主页
├── CLAUDE.md                               # 本文档文件
├── _config.yml                             # Jekyll 配置
├── _layouts/                               # HTML 模板
│   └── default.html
├── assets/                                 # 图片和静态文件
├── ja/                                     # 日语翻译
│   ├── index.html
│   └── [所有日语教程]
│
├── Install_CLAUDE_Code_Win.md
├── Install_Claude_Code_MacOS.md
├── VS_Code_Getting_Started.md
├── Claude_Code_in_VS_Code_Win.md
├── Claude_Code_in_VS_Code_Mac.md
├── Claude_Code_Basic_Operations.md
├── Claude_Code_Git_Windows.md
├── Claude_Code_Git_Mac.md
├── Github_desktop.md
├── GitHub_Desktop_Claude_Code_Workflow.md
│
├── R_Coding_VS_Code_Guide.md
├── R_Coding_Docker_Guide.md
├── Vibe_Coding_R_Docker_Guide.md
├── Claude_Code_RStudio_Mac.md
├── Claude_Code_WSL_RStudio_Windows.md
├── Claude_Code_R_VS_Code_Mac.md
│
├── Python_Coding_VS_Code_Guide.md
├── Python_Coding_Docker_Guide.md
├── Vibe_Coding_Python_Docker_Guide.md
├── Claude_Code_Python_VS_Code_Mac.md
│
├── Create_Your_First_Claude_Skill.md
├── Create_subagents.md
├── Reuse_Prompts_via_Slash_Commands.md
├── Medical_Research_Skill.md
├── Writing_Research_Paper_Claude_Code.md
└── example_paper.md
```

## 贡献

创建或更新教程时：

1. 使用 `/tutorial [topic]` 命令创建新教程
2. 使用 `/review-tutorial [file]` 命令审查现有教程
3. 遵循上述写作风格指南
4. 保持教程重点突出，不超过400行
5. 测试所有命令和说明
6. 包含常见问题的故障排除
7. 添加创建日期和作者署名

## 其他资源

- `.claude/commands/` - 斜杠命令定义
- `.claude/skills/` - 技能实现
- `.devcontainer/` - Docker 开发容器配置
