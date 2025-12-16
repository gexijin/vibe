[首页](./)

# 在 Mac 上使用 Claude Code 与 RStudio

你在 Mac 上拥有 RStudio 来运行 R 代码，同时拥有 Claude Code 来获得 AI 驱动的编码辅助。本教程将展示如何将两个工具一起用于同一项目文件。你将创建 R 项目，手动编写代码，然后从 Terminal 使用 Claude Code 通过可视化和分析增强它——同时 RStudio 保持打开以运行和测试代码。

## 关键概念

- **Terminal** - Mac 命令行界面，Claude Code 在此运行
- **共享文件** - RStudio 和 Claude Code 都处理 Documents 文件夹中的相同文件
- **混合工作流** - RStudio 运行代码，Claude Code 编写和改进代码

## 准备工作

- 完成 [在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS)
- Mac 上已安装 RStudio
- 20-30 分钟

## 步骤 1：在 Mac 上打开 RStudio

- 点击 Dock 中的 **Launchpad**（网格点图标）
- 在搜索框中输入 `RStudio`
- 点击 **RStudio** 打开
- RStudio 窗口打开，显示多个窗格

## 步骤 2：创建新的 R 项目

- 在 RStudio 中，点击 **File > New Project...**
- 选择 **New Directory**
- 选择 **New Project**
- 在 **Directory name** 中输入：`test_claude`
- 点击"Create project as subdirectory of:"旁边的 **Browse**
- 导航到 **Documents** 文件夹
- 点击 **Open**
- 点击 **Create Project**
- RStudio 创建项目并切换到此项目

## 步骤 3：创建新的 R 脚本

- 在 RStudio 中，点击 **File > New File > R Script**
- 新空脚本在左上方窗格中打开
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
- 运行代码：选中所有行，点击 **Run** 按钮（脚本窗格右上方）
- 你应在 Console 窗格中看到数据集结构和统计信息的输出

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
- 输入以下命令验证位置正确：
  ```
  ls
  ```
- 你应看到列出的 `iris.R` 和 `test_claude.Rproj`

**提示：** 如不确定确切路径，可将文件夹从 Finder 拖放到 Terminal 中，完整路径将自动出现。

## 步骤 7：启动 Claude Code

- 在 Terminal 中输入：
  ```
  claude
  ```
- Claude Code 启动并显示欢迎消息
- 如果是首次会话，可能需要进行身份验证
- 现在可以为 R 项目使用 AI 辅助

## 步骤 8：请求 Claude 创建散点图

如果 Claude Code 较慢或无响应，等待它初始化。然后输入请求：

```
在 iris.R 中添加代码，创建萼片长度与宽度的散点图，按物种着色。使用 ggplot2。
```
- Claude Code 读取 `iris.R` 文件并添加可视化代码
- 询问时，通过选择适当选项给 Claude 权限编辑 iris.R 文件
- 等待 Claude 完成（你会看到确认消息）


## 步骤 9：在 RStudio 中运行新代码

- 切换回 RStudio（点击 RStudio 窗口或按 **Command (⌘) + Tab**）
- 可能会看到文件已更改的提示，点击 **Yes** 重新加载
- 如无提示，点击 **File > Reopen with Encoding > UTF-8**
- 选中所有代码，点击 **Run**
- 散点图出现在 **Plots** 窗格（右下方）
- 如收到 ggplot2 错误，在 Console 窗格输入 `install.packages("ggplot2")` 安装

## 步骤 10：优化散点图

- 切换到 Terminal（按 **Command (⌘) + Tab** 或点击 Terminal 窗口）
- 输入这个请求：
  ```
  移除标题。按物种更改标记类型。更改为 classic 主题。
  ```

## 步骤 11：查看优化后的图表

- 切换到 RStudio
- 如有提示，重新加载文件
- 选中更新的代码，点击 **Run**
- 图表现在显示无标题，每个物种有不同标记形状，使用经典主题

## 步骤 12：请求 Claude 创建 PCA 图

- 切换到 Terminal
- 输入这个请求：
  ```
  添加代码对数值变量进行 PCA 分析，并使用前两个主成分绘制样本图。
  ```

## 步骤 13：运行 PCA 分析

- 切换到 RStudio
- 如有提示，重新加载文件
- 选中所有代码，点击 **Run**
- 出现 PCA 图，显示样本投影到 PC1 和 PC2 上，按物种着色

## 步骤 14：请求 Claude 审查和注释

- 切换到 Terminal
- 输入这个请求：
  ```
  检查整个脚本的正确性。必要时添加注释。
  ```
- Claude 审查代码并添加全面注释

## 步骤 15：请求 Claude 创建 R Markdown

- 切换到 Terminal
- 输入这个请求：
  ```
  为这个分析创建一个新的 R Markdown 文件。保存为 iris_report.Rmd
  ```
- Claude 请求你的权限来创建此文件
- Claude 在项目文件夹中创建新的 `.Rmd` 文件


## 步骤 16：编译 R Markdown 文件

- 切换到 RStudio
- 点击 **File > Open File...**
- 选择 `iris_report.Rmd`，点击 **Open**
- 点击脚本窗格顶部的 **Knit** 按钮（毛线球图标）
- RStudio 生成 HTML 报告
- 报告在新窗口打开，显示完整分析和叙述性文本
- HTML 文件保存在项目文件夹中

## 故障排除

- **RStudio 不显示文件更改** - 点击 **File > Reopen with Encoding > UTF-8** 手动重新加载文件，或关闭并重新打开文件
- **"claude: command not found"** - 确保完成 [安装指南](./Install_Claude_Code_MacOS)，尝试打开新 Terminal 窗口，或完全关闭 Terminal（**Command (⌘) + Q**）并重新打开
- **图表未出现** - 确保已安装 ggplot2，如需要在 RStudio Console 中运行 `install.packages("ggplot2")`
- **"No such file or directory"** - 检查步骤 6 中是否正确输入路径，尝试使用拖放：在输入 `cd ` 后（带空格），将 test_claude 文件夹从 Finder 拖到 Terminal
- **Claude Code 首次请求较慢** - 等待 30-60 秒让 Claude 初始化，后续请求会更快

## Mac 键盘快捷键

应用程序之间切换的有用快捷键：
- **Command (⌘) + Tab** - 在打开的应用程序间快速切换
- **Command (⌘) + `**（反引号）- 在同一应用程序的窗口间切换
- **Command (⌘) + Space** - 打开 Spotlight 搜索（打开应用程序）
- **Command (⌘) + Q** - 完全退出应用程序

## 下一步

- 请求 Claude 向分析中添加统计检验（t 检验、方差分析）
- 请求 Claude 获取此代码的 **Python 版本**并准备 Quarto 文档
- 请求 Claude 为 R 脚本中的重复任务创建函数
- 用 Claude 调试 R 代码无法运行时的错误消息
- 探索请求 Claude 优化慢速 R 代码以获得更好性能

## 工作流总结

这种混合设置结合两个世界的优点：

- **RStudio（Mac）** - 交互式 R 控制台、即时图表查看、熟悉的 GUI 运行代码
- **Claude Code（Terminal）** - AI 驱动的代码生成、审查和改进
- **共享文件** - 两个工具都处理 Documents 文件夹中的相同文件
- **迭代优化** - 从手动代码开始，用 Claude 增强，在 RStudio 中测试，进一步优化
- **文档** - Claude 可为分析生成全面报告和注释

工作流简单：在 Terminal 中用 Claude 编写或编辑代码，然后立即在 RStudio 中测试和运行。无需文件复制或手动同步，两个应用程序在 Mac 上无缝访问相同文件。

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2024 年 12 月 11 日。
