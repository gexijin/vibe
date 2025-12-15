[首页](./)

# 在 Windows 上通过 WSL 使用 Claude Code 与 RStudio

您在 Windows 上安装了 RStudio 用于运行 R 代码，在 WSL 中安装了 Claude Code 用于 AI 驱动的编程辅助。本教程将向您展示如何在同一个项目文件上同时使用这两个工具。您将在 Windows 中创建一个 R 项目，手动编写一些代码，然后从 Ubuntu 终端使用 Claude Code 来增强代码，添加可视化和分析功能——同时保持 RStudio 打开以运行和测试您的代码。

## 核心概念

- **WSL (Windows Subsystem for Linux)** - 在 Windows 内运行 Ubuntu Linux，Claude Code 安装在其中
- **文件路径转换** - Windows 路径如 `C:\Users\YourName\Documents` 在 WSL 中变成 `/mnt/c/Users/YourName/Documents`
- **混合工作流** - RStudio (Windows) 运行代码；Claude Code (WSL) 编写和改进代码

## 所需准备

- 已完成 [在 Windows 上安装 Claude Code](./Install_CLAUDE_Code_Win) 指南
- 在 Windows 上安装了 RStudio
- 20-30 分钟

## 步骤 1：在 Windows 上打开 RStudio

- 点击 **Windows 开始按钮**
- 在搜索框中输入 `RStudio`
- 点击 **RStudio** 打开它
- RStudio 窗口打开，显示多个面板

## 步骤 2：创建新的 R 项目

- 在 RStudio 中，点击顶部菜单的 **File**
- 点击 **New Project...**
- 选择 **New Directory**
- 选择 **New Project**
- 在 **Directory name** 中输入：`test_claude`
- 点击 "Create project as subdirectory of:" 旁边的 **Browse**
- 导航到您的 **Documents** 文件夹
- 点击 **Select Folder**
- 点击 **Create Project**
- RStudio 创建项目并切换到该项目

## 步骤 3：创建新的 R 脚本

- 在 RStudio 中，点击 **File > New File > R Script**
- 在左上角面板中打开一个新的空白脚本
- 点击 **File > Save**（或保存图标）
- 将文件命名为：`iris.R`
- 点击 **Save**

## 步骤 4：手动编写初始代码

在您的 `iris.R` 文件中输入以下代码：

```r
data(iris)
str(iris)
summary(iris)
```

- 点击 **File > Save** 保存更改
- 要运行代码：选中所有行，然后点击 **Run** 按钮（脚本面板右上角）
- 您应该在 Console 面板中看到输出，显示数据集结构和统计信息

## 步骤 5：打开 Ubuntu Terminal

- 点击 **Windows 开始按钮**
- 在搜索框中输入 `Ubuntu`
- 点击 **Ubuntu**（橙色圆形图标）
- Ubuntu 终端打开

## 步骤 6：导航到您的项目文件夹

- 在 Ubuntu 终端中，输入以下命令（将 `YourUsername` 替换为您的实际 Windows 用户名）：
  ```
  cd /mnt/c/Users/YourUsername/Documents/test_claude
  ```
- 要查找您的用户名，可以输入：`ls /mnt/c/Users/` 并查找您的文件夹名称
- 通过输入以下命令验证您在正确的位置：
  ```
  ls
  ```
- 您应该看到列出了 `iris.R` 和 `test_claude.Rproj`

## 步骤 7：启动 Claude Code

- 在 Ubuntu 终端中，输入：
  ```
  claude
  ```
- Claude Code 启动并显示欢迎消息
- 您可能需要重新登录——请参阅 [在 Windows 上安装 Claude Code](./Install_CLAUDE_Code_Win) 指南了解身份验证步骤
- 现在您已准备好为您的 R 项目使用 AI 辅助

## 步骤 8：请求 Claude 创建散点图

如果 Claude Code 运行缓慢或无响应，只需等待它初始化。然后，输入以下请求：

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Code 将读取您的 `iris.R` 文件并添加可视化代码
- 当被询问时，通过选择适当的选项授予 Claude 编辑 iris.R 文件的权限
- 等待 Claude 完成（您将看到确认消息）


## 步骤 9：在 RStudio 中运行新代码

- 切换回 RStudio（点击 RStudio 窗口）
- 您可能会看到提示说文件已更改——点击 **Yes** 重新加载
- 如果没有出现提示，点击 **File > Reopen with Encoding > UTF-8**
- 选中所有代码并点击 **Run**
- 散点图出现在 **Plots** 面板（右下角）
- 如果出现关于 ggplot2 的错误，请在 Console 面板中输入 `install.packages("ggplot2")` 来安装它

## 步骤 10：优化散点图

- 切换到 Ubuntu 终端
- 输入以下请求：
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## 步骤 11：查看优化后的图表

- 切换到 RStudio
- 如果出现提示，重新加载文件
- 选中更新后的代码并点击 **Run**
- 图表现在应该显示为没有标题，每个物种使用不同的标记形状，并使用经典主题


## 步骤 12：请求 Claude 创建 PCA 图

- 切换到 Ubuntu 终端
- 输入以下请求：
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## 步骤 13：运行 PCA 分析

- 切换到 RStudio
- 如果出现提示，重新加载文件
- 选中所有代码并点击 **Run**
- 出现 PCA 图，显示样本投影到 PC1 和 PC2 上，按物种着色

## 步骤 14：请求 Claude 审查并添加注释

- 切换到 Ubuntu 终端
- 输入以下请求：
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claude 将审查代码并添加全面的注释

## 步骤 15：请求 Claude 创建 R Markdown

- 切换到 Ubuntu 终端
- 输入以下请求：
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claude 将请求您的权限来创建此文件
- Claude 将在您的项目文件夹中创建一个新的 `.Rmd` 文件


## 步骤 16：编织 R Markdown 文件

- 切换到 RStudio
- 点击 **File > Open File...**
- 选择 `iris_report.Rmd` 并点击 **Open**
- 点击脚本面板顶部的 **Knit** 按钮（带有毛线球图标）
- RStudio 将生成 HTML 报告
- 报告在新窗口中打开，显示您的完整分析和叙述文本
- HTML 文件保存在您的项目文件夹中

## 故障排除

- **从 WSL 访问 Windows 文件时"Permission denied"** - 确保使用 `/mnt/c/` 而不是 `C:/`。检查路径中的用户名是否正确。
- **RStudio 不显示文件更改** - 点击 **File > Reopen with Encoding > UTF-8** 手动重新加载文件。
- **"claude: command not found"** - 确保您已完成安装指南。尝试打开一个新的 Ubuntu 终端窗口。
- **图表未显示** - 确保已安装 ggplot2。如需要，在 RStudio Console 中运行 `install.packages("ggplot2")`。
- **错误："cannot change working directory"** - 您的 Windows 路径包含空格。在步骤 6 中，将路径用引号括起来：`cd "/mnt/c/Users/Your Name/Documents/test_claude"`
- **Claude Code 首次请求时很慢** - 等待 30-60 秒让 Claude 初始化。后续请求会更快。

## 下一步

- 尝试请求 Claude 向您的分析添加统计检验（t 检验、ANOVA）
- 请求 Claude 获取此代码的 **Python 版本**并准备一个 Quarto 文档
- 请求 Claude 为 R 脚本中的重复性任务创建函数
- 使用 Claude 在 R 代码无法运行时调试错误消息
- 探索请求 Claude 优化运行缓慢的 R 代码以获得更好的性能

## 工作流总结

这种混合设置结合了两全其美：

- **RStudio (Windows)** - 交互式 R 控制台、即时图表查看、用于运行代码的熟悉 GUI
- **Claude Code (WSL)** - AI 驱动的代码生成、审查和改进
- **共享文件** - 两个工具通过 WSL 的 `/mnt/c/` 挂载点在同一文件上工作
- **迭代优化** - 从手动代码开始，用 Claude 增强，在 RStudio 中测试，然后进一步优化
- **文档** - Claude 可以为您的分析生成全面的报告和注释

工作流程很简单：在 Ubuntu 终端中使用 Claude 编写或编辑代码，然后立即在 RStudio 中测试和运行。无需文件复制或手动同步——WSL 和 Windows 无缝共享同一文件。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 11 日。
