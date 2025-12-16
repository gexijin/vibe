[首页](./)

# 使用 Claude Code 和 Docker 进行 Python Vibe 编程

你曾经逐行输入 Python 代码。但如果你只需用简单的英语描述想要的功能,代码就能自动生成呢?Vibe 编程就像与计算机对话——你描述结果,Claude Code 构建代码,你测试并完善。这不是魔法,而是一种新的工作方式:你负责愿景,AI 负责实现。本教程将教你如何仅用自然语言请求来分析经典的鸢尾花数据集。

## 核心概念

- **[Vibe Coding](https://www.ibm.com/think/topics/vibe-coding)** - 用自然语言描述想要的功能,根据结果迭代,而非逐行编写代码
- **[Claude Code](https://code.claude.com/)** - AI 编程助手,根据你的自然语言请求编写、调试和重构代码
- **[Iris Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)** - 经典数据集,包含三个物种 150 朵鸢尾花的测量数据
- **迭代完善** - Vibe 编程的核心模式:描述 → 测试 → 完善 → 提交可用版本

## 准备工作

- 完成 [通过 Docker 在 VS Code 中进行 Python 编程](./Python_Coding_Docker_Guide)
- 完成 [使用 GitHub Desktop 配合 Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 20-25 分钟

## 步骤 1:创建新的 GitHub 仓库

- 打开 GitHub Desktop
- 点击 **File > New Repository**
- 填写详细信息:
  - **Name:** `iris-analysis`
  - **Description:** `Iris data analysis built with vibe coding`
  - **Local Path:** 选择一个位置(如 Documents 或工作文件夹)
  - 勾选 **Initialize this repository with a README**
- 点击 **Create Repository**
- 点击顶部的 **Publish repository**
- 如果希望公开,取消勾选 **Keep this code private**(可选)
- 点击 **Publish Repository**

现在你已拥有本地 Git 仓库和 GitHub 上的备份。

## 步骤 2:复制 Docker 配置

你需要从 vibe 项目复制 `.devcontainer` 文件夹来设置 Docker 环境。

- 打开 File Explorer(Windows)或 Finder(Mac)
- 导航到你的 vibe 项目文件夹(如 `Documents/vibe`)
- 找到 `.devcontainer` 文件夹
- 复制整个文件夹(包含 `Dockerfile` 和 `devcontainer.json`)
- 导航到新建的 `iris-analysis` 文件夹
- 将 `.devcontainer` 文件夹粘贴到这里

你的 `iris-analysis` 文件夹现在应包含:
- `.devcontainer/`(你刚复制的文件夹)
- `README.md`(由 GitHub Desktop 创建)
- `.git/`(版本控制的隐藏文件夹)

## 步骤 3:在容器中打开项目

- 打开 VS Code
- 点击 **File > Open Folder**
- 导航到 `iris-analysis` 文件夹
- 点击 **Select Folder**
- 右下角出现通知:**Folder contains a Dev Container configuration file**
- 点击 **Reopen in Container**
- 如果没看到通知,点击左下角的绿色图标,选择 **Reopen in Container**
- VS Code 构建 Docker 容器(首次需要 3-5 分钟)
- 观察显示构建步骤的进度通知
- 完成后,绿色图标显示 **Dev Container: Python in Docker**

## 步骤 4:启动 Claude Code

- 在 VS Code 中,点击 **Terminal > New Terminal**
- 你现在位于 Docker 容器内部
- 输入此命令启动 Claude Code:

```bash
claude
```

- 浏览器窗口打开进行身份验证
- 点击 **Continue with Google** 或 **Continue with Email**
- 使用你的 Claude 账户登录(或创建一个)
- 身份验证成功后,返回 VS Code 终端
- 你将看到 Claude 的欢迎消息

Claude Code 现在已准备就绪,可接收你的请求。

## 步骤 5:第一次 Vibe - 加载数据

现在开始有趣的部分。无需查找文档,只需描述你想要的功能。

- 在 Claude Code 终端中,输入:

```
Load the iris dataset from scikit-learn. Convert it to a pandas dataframe with proper column names. Add the species names as a column (not just numbers). Show me the first 10 rows. Save the code to a file called iris_exploration.py
```

- 按 Enter
- 观察 Claude:
  - 编写 Python 代码加载数据
  - 创建带有适当导入的脚本
  - 运行代码并展示结果
- 查看显示花卉测量数据和物种名称的输出

你刚刚使用了 Vibe 编程!无需搜索文档,无需反复试错——只需描述和测试。

要求 Claude 使用 Git 提交,或从 GitHub Desktop 自己完成:
```
Commit these changes.
```
## 步骤 6:第二次 Vibe - 汇总统计

在创建可视化之前,先了解数据内容。

- 在 Claude Code 终端中,输入:

```
Show me summary statistics for the iris data grouped by species. I want to see the mean, min, and max for each measurement (sepal length, sepal width, petal length, petal width) for each of the three species. Add this to iris_exploration.py
```

- 按 Enter
- Claude 更新脚本并显示统计信息
- 注意不同物种的测量范围差异
- Setosa 的花瓣比 Virginica 小得多

这种探索帮助你理解数据中的模式。

要求 Claude 使用 Git 提交,或从 GitHub Desktop 自己完成。

## 步骤 7:第三次 Vibe - 创建直方图

开始可视化数据。

- 在 Claude Code 终端中,输入:

```
Create a histogram showing the distribution of petal lengths for all flowers. Use 20 bins. Add a title and axis labels. Save the plot as petal_length_histogram.png. Add this code to iris_exploration.py
```

- 按 Enter
- Claude 创建可视化代码
- 项目文件夹中出现 PNG 文件
- 打开 `petal_length_histogram.png` 查看图表
- 注意两个峰值——这显示物种具有不同的花瓣长度

## 步骤 8:第四次 Vibe - 散点图

散点图显示两个变量之间的关系。

- 在 Claude Code 终端中,输入:

```
Create a scatter plot with petal length on the x-axis and petal width on the y-axis. Color each point by species using different colors. Add a legend showing which color is which species. Save as petal_scatter.png. Add this to iris_exploration.py
```

- 按 Enter
- Claude 创建散点图
- 打开 `petal_scatter.png` 查看结果
- 注意三个物种形成不同的聚类
- Setosa(小花瓣)与其他物种明显分离

这就是 Vibe 编程的实际应用:描述可视化,测试,迭代。

## 步骤 9:第五次 Vibe - 箱线图

箱线图非常适合比较各组之间的分布。

- 在 Claude Code 终端中,输入:

```
Create a box plot comparing petal lengths across the three species. Put species on the x-axis and petal length on the y-axis. Use different colors for each species. Add a title. Save as species_boxplot.png. Add this to iris_exploration.py
```

- 按 Enter
- Claude 添加箱线图代码
- 打开 `species_boxplot.png` 查看比较
- 箱体显示每个物种的中位数和四分位数
- 你可以清楚地看到 Virginica 的花瓣最长

## 步骤 10:审查并提交

提交前先审查 Claude 构建的内容。

- 在 VS Code Explorer 中,点击 `iris_exploration.py` 打开
- 浏览代码——注意导入、数据加载和绘图部分
- 你不需要理解每一行,但要了解结构
- 检查是否创建了所有 PNG 文件:`petal_length_histogram.png`、`petal_scatter.png`、`species_boxplot.png`
- 打开 GitHub Desktop
- 你将看到列出的所有新文件(Python 脚本和 PNG 图像)
- 在左下角的 **Summary** 字段中,输入:

```
Iris data analysis with histograms, scatter plots, and box plots
```

- 点击 **Commit to main**
- 点击 **Push origin** 备份到 GitHub

你已保存了第一个可用分析!

## 步骤 11:迭代并改进

Vibe 编程在迭代时更显威力。尝试通过描述来添加功能:

**向 Claude 请求的示例:**

- "Add a correlation matrix heatmap showing relationships between all four measurements"
- "Create a violin plot comparing sepal width across species"
- "Calculate and display the correlation coefficient between petal length and width"
- "Add statistical test results comparing species (ANOVA or t-test)"
- "Create a pair plot showing all variable relationships colored by species"

每次成功添加功能后:
- 通过运行脚本测试
- 如果有效,使用 GitHub Desktop 提交
- 如果出现问题,告诉 Claude 错误并要求修复
- 修复后,提交可用版本


**核心原则:**

- **描述结果,而非实现** - 说"显示相关性热图"而不是"使用 seaborn.heatmap() 配合 df.corr()"
- **快速迭代** - 测试 → 完善 → 测试 → 完善
- **提交可用版本** - 在尝试新功能前保存每个成功
- **拥抱失败** - 如果 Claude 的代码出错,只需描述错误并要求修复
- **保持控制** - 你决定功能、优先级以及何时足够好

每次都遵循这个模式:描述 → 测试 → 迭代 → 提交。

## 下一步

- **尝试不同的数据集** - 要求 Claude 使用葡萄酒数据集、数字数据集或加载 CSV 文件
- **探索更多可视化** - 尝试热图、配对图或小提琴图
- **通过提问学习** - 当 Claude 编写代码时,询问"解释这一行的作用"来学习 Python
- **应用到你的数据** - 使用 Vibe 编程分析你的研究或工作数据
- **阅读有关 Vibe 编程的内容** - 访问 [IBM 的指南](https://www.ibm.com/think/topics/vibe-coding)了解更多

## 故障排除

- **图表未显示** - 代码将图表保存为 PNG 文件。在项目文件夹中查找并直接在 VS Code 中打开图像文件。
- **导入错误** - Docker 容器应该预装了 pandas、matplotlib 和 scikit-learn。如果没有,要求 Claude 使用 pip 安装它们。
- **Claude 犯错误** - 正常!复制错误消息,粘贴给 Claude,并说"修复此错误。"Vibe 编程包括迭代和调试。
- **无法推送到 GitHub** - 确保你已登录 GitHub Desktop 并发布了仓库(步骤 1)。检查互联网连接。
- **容器无法启动** - 确保 Docker Desktop 正在运行(绿色状态指示器)。尝试点击 VS Code 中的绿色图标并选择 **Rebuild Container**。

## 工作流程概述

本教程将几种技术组合成一个工作流程:

- **GitHub Desktop** - 具有可视化界面的版本控制(创建仓库、提交、推送)
- **Docker 容器** - 预装所有依赖项的隔离 Python 环境
- **VS Code** - 连接到 Docker 容器的代码编辑器
- **Claude Code** - 根据你的描述编写 Python 代码的 AI 助手
- **scikit-learn** - 提供 Iris 数据集和机器学习工具
- **pandas** - 数据操作和分析
- **matplotlib** - 创建可视化

魔法不在于任何单一工具——而在于 Vibe 编程如何让你描述想要的内容并快速迭代。你在 20 分钟内从空项目到具有多个可视化的完整数据分析,而无需手动编写一行代码。


---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 December 11, 2025。
