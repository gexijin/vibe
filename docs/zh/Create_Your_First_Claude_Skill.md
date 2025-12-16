[首页](./)

# 创建你的第一个Claude Skill

你一直在手动输入`/stock-report AAPL`来生成报告。如果Claude能够根据对话自动决定何时创建股票报告会怎么样？这就是Skill的强大之处——就像从手动换挡升级到自动变速箱，能在需要时自动换挡。

## 核心概念

- **Skill** - 存储在`.claude/skills/`中的模型调用能力，Claude会根据上下文自动激活
- **模型调用（Model-invoked）** - Claude通过阅读Skill的描述来决定何时使用它，无需输入命令
- **SKILL.md** - 包含YAML前置内容（元数据）和Claude指令的主文件

## 你需要准备什么

- 完成[创建自定义Slash命令](./Reuse_Prompts_via_Slash_Commands.md)教程
- 该教程中的`stock-report` slash命令
- 已安装VS Code
- 10-15分钟

## 步骤1：导航到项目文件夹

**Windows（WSL）：**
- 从开始菜单打开**Ubuntu**
- 输入：
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  将`YOUR_USERNAME`替换为你的Windows用户名

  如果文件夹不存在，请先创建它：
  ```bash
  mkdir -p /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```

**Mac：**
- 打开**Terminal**（应用程序 > 实用工具）
- 输入：
  ```bash
  cd ~/Documents/test_claude
  ```

  如果文件夹不存在，请先创建它：
  ```bash
  mkdir -p ~/Documents/test_claude
  cd ~/Documents/test_claude
  ```

## 步骤2：启动Claude Code

输入：
```
claude
```

Claude Code启动并显示欢迎信息。

## 步骤3：启用编辑自动批准

按`Ctrl+E`（Windows/Linux）或`Cmd+E`（Mac）来启用编辑自动批准模式。

这样可以让Claude创建和修改文件，而无需每次都请求权限。

## 步骤4：让Claude转换Slash命令

输入以下提示：
```
将我的 stock-report slash 命令转换为名为 generate-stock-reports 的 Skill。
这个 Skill 应该在我询问公司或股票时自动激活。
```

Claude会分析现有的slash命令，并将其转换为`.claude/skills/stock-report/`中的Skill。

**发生了什么：**Claude创建了一个新的文件夹结构，其中`SKILL.md`包含YAML前置内容，告诉Claude何时自动使用这个Skill。

## 步骤5：查看Skill结构

打开VS Code并查看项目：
- 点击**File > Open Folder**
- 选择`Documents/test_claude`
- 在文件浏览器中，导航到`.claude/skills/stock-report/`
- 点击`SKILL.md`打开它

注意其结构：
```yaml
---
name: stock-report
description: Generates reports on companies... Use when users ask about stocks, companies, or ticker symbols.
---

[Rest of the instructions]
```

`description`字段是关键——它准确地告诉Claude何时自动激活这个Skill。

## 步骤6：测试Skill（无需输入命令）

不要输入`/stock-report AAPL`，只需提出一个自然的问题：
```
苹果公司最近有什么动态？
```

**关键区别：**你没有输入命令。Claude阅读问题，识别出你在询问某家公司，检查Skill描述，然后自动决定使用stock-report Skill。

观察Claude的工作——它应该生成与之前看到的相同的综合报告。

## 步骤7：比较两种方法

**Slash命令（手动）：**
```
/stock-report AAPL
```
- 明确告诉Claude要做什么
- 每次都一样
- 适合重复的、可预测的任务

**Skill（自动）：**
```
告诉我特斯拉最近的发展情况
```
或
```
我在考虑投资微软
```
或
```
英伟达最近在做什么？
```
- Claude决定是否使用Skill
- 更自然的对话
- 适合Claude管理的复杂工作流程

## 步骤8：测试边缘情况

尝试不应该触发股票报告Skill的问题：
```
如何安装 Python？
```

Claude正常回答，不调用Skill。

现在尝试一个应该触发它的问题：
```
比较 Google 和 Meta
```

Claude应该使用Skill两次——一次用于Google，一次用于Meta。

## 步骤9：修改Skill描述（可选）

让我们使Skill更具选择性。询问Claude：
```
更新 stock-report Skill，使其仅在我明确提到"分析"或"报告"以及公司名称时才激活。
```

Claude会更新`SKILL.md`中的`description`字段。测试差异：
```
苹果公司在做什么？
```
（现在可能不会触发Skill）

```
分析苹果公司
```
（应该触发Skill）

## 下一步

既然你已经理解了Skill，为工作流程创建更多：

- **Research Skill** - 当提出需要网络研究的问题时自动激活
- **Code Review Skill** - 当提到错误、问题或代码问题时激活
- **Meeting Notes Skill** - 当粘贴会议记录或提到摘要时激活

模式是：定义Claude何时应该自动帮助，而不仅仅是手动触发的快捷方式。

## 故障排除

- **Skill未激活：**检查`SKILL.md`中的`description`字段——它必须包含与问题相关的触发词
- **Skill激活过于频繁：**使描述更具体地说明何时使用它
- **找不到Skill文件夹：**Skill位于`.claude/skills/`（隐藏文件夹——在文件浏览器中启用"显示隐藏文件"）
- **对SKILL.md的更改不起作用：**Skill在修改后会自动加载——无需重启。如果仍然不起作用，请检查YAML格式

## 工作流程概述

- **Slash命令**是手动输入的快捷方式（类似书签）
- **Skill**是Claude自动发现和使用的能力（类似了解偏好的助手）
- **Skill描述**充当指令，告诉Claude："当用户说X时使用我"
- **两者可以共存** - 使用slash命令执行快速、重复的任务；使用Skill处理复杂的工作流程
- **Skill更具扩展性** - 不需要记住命令名称；Claude根据上下文决定

---

由[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)创建于2025年12月13日。
