[首页](./)

# 在 Mac 上使用 Claude Code 与 RStudio

你在 Mac 上拥有 RStudio 来运行 R 代码，同时拥有 Claude Code 来获得 AI 驱动的编码辅助。本教程将向你展示如何将这两个工具一起用于同一个项目文件。你将创建一个 R 项目，手动编写一些代码，然后从 Terminal 使用 Claude Code 来通过可视化和分析增强它——同时 RStudio 保持打开状态以运行和测试你的代码。

## 关键概念

- **Terminal** - Mac 的命令行界面，Claude Code 在此运行
- **共享文件** - RStudio 和 Claude Code 都处理你 Documents 文件夹中的相同文件
- **混合工作流** - RStudio 运行代码；Claude Code 编写和改进代码

## 你需要什么

- 完成 [在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS) 指南
- Mac 上已安装 RStudio
- 20-30 分钟

## 步骤 1：在 Mac 上打开 RStudio

- 点击 Dock 中的 **Launchpad**（网格点图标）
- 在搜索框中输入 `RStudio`
- 点击 **RStudio** 打开它
- RStudio 窗口打开，显示多个窗格

## 步骤 2：创建一个新的 R 项目

- 在 RStudio 中，点击顶部菜单的 **File**
- 点击 **New Project...**
- 选择 **New Directory**
- 选择 **New Project**
- 在 **Directory name** 中输入：`test_claude`
- 点击"Create project as subdirectory of:"旁边的 **Browse**
- 导航到你的 **Documents** 文件夹
- 点击 **Open**
- 点击 **Create Project**
- RStudio 创建项目并切换到它

## 步骤 3：创建一个新的 R 脚本

- 在 RStudio 中，点击 **File > New File > R Script**
- 一个新的空脚本在左上方窗格中打开
- 点击 **File > Save**（或按 **Command (⌘) + S**）
- 命名文件为：`iris.R`
- 点击 **Save**

## 步骤 4：手动编写初始代码

在你的 `iris.R` 文件中输入这段代码：

```r
data(iris)
str(iris)
summary(iris)
```

- 点击 **File > Save** 保存更改（或按 **Command (⌘) + S**）
- 要运行代码：选中所有行，然后点击 **Run** 按钮（脚本窗格右上方）
- 你应该在 Console 窗格中看到显示数据集结构和统计信息的输出

## 步骤 5：打开 Terminal

- 打开 **Finder** 并点击左侧边栏中的 **Applications**
- 打开 **Utilities** 文件夹
- 双击 **Terminal**
- Terminal 窗口打开

## 步骤 6：导航到你的项目文件夹

- 在 Terminal 中，输入这个命令：
  ```
  cd ~/Documents/test_claude
  ```
- 通过输入以下命令验证你在正确的位置：
  ```
  ls
  ```
- 你应该看到列出了 `iris.R` 和 `test_claude.Rproj`

**提示：** 如果你不确定确切的路径，可以将文件夹从 Finder 拖放到 Terminal 中，完整路径将自动出现！

## 步骤 7：启动 Claude Code

- 在 Terminal 中输入：
  ```
  claude
  ```
- Claude Code 启动并显示欢迎消息
- 如果这是你的第一次会话，你可能需要进行身份验证
- 你现在可以为你的 R 项目使用 AI 辅助了

## 步骤 8：请求 Claude 创建散点图

如果 Claude Code 很慢或无响应，只需等待它初始化。然后，输入这个请求：

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Code 将读取你的 `iris.R` 文件并添加可视化代码
- 当被询问时，通过选择适当的选项给 Claude 权限编辑 iris.R 文件
- 等待 Claude 完成（你会看到确认消息）


## 步骤 9：在 RStudio 中运行新代码

- 切换回 RStudio（点击 RStudio 窗口或按 **Command (⌘) + Tab**）
- 你可能会看到文件已更改的提示 - 点击 **Yes** 重新加载
- 如果没有出现提示，点击 **File > Reopen with Encoding > UTF-8**
- 选中所有代码并点击 **Run**
- 散点图出现在 **Plots** 窗格中（右下方）
- 如果你收到关于 ggplot2 的错误，请在 Console 窗格中输入 `install.packages("ggplot2")` 来安装它

## 步骤 10：优化散点图

- 切换到 Terminal（按 **Command (⌘) + Tab** 或点击 Terminal 窗口）
- 输入这个请求：
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## 步骤 11：查看优化后的图表

- 切换到 RStudio
- 如果提示，重新加载文件
- 选中更新的代码并点击 **Run**
- 图表现在应该显示为没有标题，每个物种有不同的标记形状，并使用经典主题

## 步骤 12：请求 Claude 创建 PCA 图

- 切换到 Terminal
- 输入这个请求：
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## 步骤 13：运行 PCA 分析

- 切换到 RStudio
- 如果提示，重新加载文件
- 选中所有代码并点击 **Run**
- 出现一个 PCA 图，显示样本投影到 PC1 和 PC2 上，按物种着色

## 步骤 14：请求 Claude 审查和注释

- 切换到 Terminal
- 输入这个请求：
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claude 将审查代码并添加全面的注释

## 步骤 15：请求 Claude 创建 R Markdown

- 切换到 Terminal
- 输入这个请求：
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claude 将请求你的权限来创建这个文件
- Claude 将在你的项目文件夹中创建一个新的 `.Rmd` 文件


## 步骤 16：编译 R Markdown 文件

- 切换到 RStudio
- 点击 **File > Open File...**
- 选择 `iris_report.Rmd` 并点击 **Open**
- 点击脚本窗格顶部的 **Knit** 按钮（带有毛线球图标）
- RStudio 将生成一个 HTML 报告
- 报告在新窗口中打开，显示你的完整分析和叙述性文本
- HTML 文件保存在你的项目文件夹中

## 故障排除

- **RStudio 不显示文件更改** - 点击 **File > Reopen with Encoding > UTF-8** 手动重新加载文件，或关闭并重新打开文件。
- **"claude: command not found"** - 确保你完成了 [安装指南](./Install_Claude_Code_MacOS)。尝试打开一个新的 Terminal 窗口，或完全关闭 Terminal（**Command (⌘) + Q**）并重新打开它。
- **图表未出现** - 确保 ggplot2 已安装。如果需要，在 RStudio Console 中运行 `install.packages("ggplot2")`。
- **"No such file or directory"** - 检查你在步骤 6 中是否正确输入了路径。尝试使用拖放技巧：在输入 `cd ` 后（带一个空格），将 test_claude 文件夹从 Finder 拖到 Terminal 中。
- **Claude Code 第一次请求时很慢** - 等待 30-60 秒让 Claude 初始化。后续请求会更快。

## Mac 键盘快捷键

在应用程序之间切换的有用快捷键：
- **Command (⌘) + Tab** - 快速在打开的应用程序之间切换
- **Command (⌘) + `**（反引号）- 在同一应用程序的窗口之间切换
- **Command (⌘) + Space** - 打开 Spotlight 搜索（打开应用程序）
- **Command (⌘) + Q** - 完全退出应用程序

## 下一步

- 尝试请求 Claude 向你的分析中添加统计检验（t 检验、方差分析）
- 请求 Claude 获取此代码的 **Python 版本**并准备一个 Quarto 文档
- 请求 Claude 为 R 脚本中的重复任务创建函数
- 使用 Claude 调试 R 代码无法运行时的错误消息
- 探索请求 Claude 优化慢速 R 代码以获得更好的性能

## 工作流总结

这种混合设置结合了两个世界的优点：

- **RStudio（Mac）** - 交互式 R 控制台、即时图表查看、熟悉的 GUI 运行代码
- **Claude Code（Terminal）** - AI 驱动的代码生成、审查和改进
- **共享文件** - 两个工具都处理你 Documents 文件夹中的相同文件
- **迭代优化** - 从手动代码开始，用 Claude 增强，在 RStudio 中测试，然后进一步优化
- **文档** - Claude 可以为你的分析生成全面的报告和注释

工作流很简单：在 Terminal 中用 Claude 编写或编辑代码，然后立即在 RStudio 中测试和运行它。无需文件复制或手动同步——两个应用程序在你的 Mac 上无缝访问相同的文件。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2024 年 12 月 11 日。
