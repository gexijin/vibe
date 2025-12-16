[首页](./)

# 在Windows上通过WSL使用Claude Code与RStudio

你在Windows上安装了RStudio用于运行R代码，在WSL中安装了Claude Code用于AI辅助编程。本教程将展示如何在同一个项目文件上同时使用这两个工具。你将在Windows中创建R项目，手动编写一些代码，然后从Ubuntu终端使用Claude Code来增强代码，添加可视化和分析功能——同时保持RStudio打开以运行和测试代码。

## 核心概念

- **WSL (Windows Subsystem for Linux)** - 在Windows内运行Ubuntu Linux，Claude Code安装在其中
- **文件路径转换** - Windows路径如`C:\Users\YourName\Documents`在WSL中变成`/mnt/c/Users/YourName/Documents`
- **混合工作流** - RStudio (Windows)运行代码；Claude Code (WSL)编写和改进代码

## 所需准备

- 已完成[在Windows上安装Claude Code](./Install_CLAUDE_Code_Win)指南
- 在Windows上安装了RStudio
- 20-30分钟

## 步骤1：在Windows上打开RStudio

- 点击**Windows开始按钮**
- 在搜索框中输入`RStudio`
- 点击**RStudio**打开它
- RStudio窗口打开，显示多个面板

## 步骤2：创建新的R项目

- 在RStudio中，点击顶部菜单的**File**
- 点击**New Project...**
- 选择**New Directory**
- 选择**New Project**
- 在**Directory name**中输入：`test_claude`
- 点击"Create project as subdirectory of:"旁边的**Browse**
- 导航到**Documents**文件夹
- 点击**Select Folder**
- 点击**Create Project**
- RStudio创建项目并切换到该项目

## 步骤3：创建新的R脚本

- 在RStudio中，点击**File > New File > R Script**
- 左上角面板中打开一个新的空白脚本
- 点击**File > Save**（或保存图标）
- 将文件命名为：`iris.R`
- 点击**Save**

## 步骤4：手动编写初始代码

在`iris.R`文件中输入以下代码：

```r
data(iris)
str(iris)
summary(iris)
```

- 点击**File > Save**保存更改
- 要运行代码：选中所有行，然后点击**Run**按钮（脚本面板右上角）
- 应该在Console面板中看到输出，显示数据集结构和统计信息

## 步骤5：打开Ubuntu Terminal

- 点击**Windows开始按钮**
- 在搜索框中输入`Ubuntu`
- 点击**Ubuntu**（橙色圆形图标）
- Ubuntu终端打开

## 步骤6：导航到项目文件夹

- 在Ubuntu终端中，输入以下命令（将`YourUsername`替换为你的实际Windows用户名）：
  ```
  cd /mnt/c/Users/YourUsername/Documents/test_claude
  ```
- 要查找用户名，可以输入：`ls /mnt/c/Users/`并查找你的文件夹名称
- 通过输入以下命令验证位置是否正确：
  ```
  ls
  ```
- 应该看到列出了`iris.R`和`test_claude.Rproj`

## 步骤7：启动Claude Code

- 在Ubuntu终端中，输入：
  ```
  claude
  ```
- Claude Code启动并显示欢迎消息
- 可能需要重新登录——请参阅[在Windows上安装Claude Code](./Install_CLAUDE_Code_Win)指南了解身份验证步骤
- 现在已准备好为R项目使用AI辅助

## 步骤8：请求Claude创建散点图

如果Claude Code运行缓慢或无响应，只需等待它初始化。然后，输入以下请求：

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Code将读取`iris.R`文件并添加可视化代码
- 被询问时，通过选择适当的选项授予Claude编辑iris.R文件的权限
- 等待Claude完成（将看到确认消息）


## 步骤9：在RStudio中运行新代码

- 切换回RStudio（点击RStudio窗口）
- 可能会看到提示说文件已更改——点击**Yes**重新加载
- 如果没有出现提示，点击**File > Reopen with Encoding > UTF-8**
- 选中所有代码并点击**Run**
- 散点图出现在**Plots**面板（右下角）
- 如果出现关于ggplot2的错误，在Console面板中输入`install.packages("ggplot2")`来安装它

## 步骤10：优化散点图

- 切换到Ubuntu终端
- 输入以下请求：
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## 步骤11：查看优化后的图表

- 切换到RStudio
- 如果出现提示，重新加载文件
- 选中更新后的代码并点击**Run**
- 图表现在应该显示为没有标题，每个物种使用不同的标记形状，并使用经典主题


## 步骤12：请求Claude创建PCA图

- 切换到Ubuntu终端
- 输入以下请求：
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## 步骤13：运行PCA分析

- 切换到RStudio
- 如果出现提示，重新加载文件
- 选中所有代码并点击**Run**
- 出现PCA图，显示样本投影到PC1和PC2上，按物种着色

## 步骤14：请求Claude审查并添加注释

- 切换到Ubuntu终端
- 输入以下请求：
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claude将审查代码并添加全面的注释

## 步骤15：请求Claude创建R Markdown

- 切换到Ubuntu终端
- 输入以下请求：
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claude将请求你的权限来创建此文件
- Claude将在项目文件夹中创建一个新的`.Rmd`文件


## 步骤16：编织R Markdown文件

- 切换到RStudio
- 点击**File > Open File...**
- 选择`iris_report.Rmd`并点击**Open**
- 点击脚本面板顶部的**Knit**按钮（带有毛线球图标）
- RStudio将生成HTML报告
- 报告在新窗口中打开，显示完整分析和叙述文本
- HTML文件保存在项目文件夹中

## 故障排除

- **从WSL访问Windows文件时"Permission denied"** - 确保使用`/mnt/c/`而不是`C:/`。检查路径中的用户名是否正确。
- **RStudio不显示文件更改** - 点击**File > Reopen with Encoding > UTF-8**手动重新加载文件。
- **"claude: command not found"** - 确保已完成安装指南。尝试打开一个新的Ubuntu终端窗口。
- **图表未显示** - 确保已安装ggplot2。如需要，在RStudio Console中运行`install.packages("ggplot2")`。
- **错误："cannot change working directory"** - Windows路径包含空格。在步骤6中，将路径用引号括起来：`cd "/mnt/c/Users/Your Name/Documents/test_claude"`
- **Claude Code首次请求时很慢** - 等待30-60秒让Claude初始化。后续请求会更快。

## 下一步

- 尝试请求Claude向分析添加统计检验（t检验、ANOVA）
- 请求Claude获取此代码的**Python版本**并准备一个Quarto文档
- 请求Claude为R脚本中的重复性任务创建函数
- 使用Claude在R代码无法运行时调试错误消息
- 探索请求Claude优化运行缓慢的R代码以获得更好的性能

## 工作流总结

这种混合设置结合了两全其美：

- **RStudio (Windows)** - 交互式R控制台、即时图表查看、用于运行代码的熟悉GUI
- **Claude Code (WSL)** - AI驱动的代码生成、审查和改进
- **共享文件** - 两个工具通过WSL的`/mnt/c/`挂载点在同一文件上工作
- **迭代优化** - 从手动代码开始，用Claude增强，在RStudio中测试，然后进一步优化
- **文档** - Claude可以为分析生成全面的报告和注释

工作流程很简单：在Ubuntu终端中使用Claude编写或编辑代码，然后立即在RStudio中测试和运行。无需文件复制或手动同步——WSL和Windows无缝共享同一文件。

---

由[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)创建于2025年12月11日。
