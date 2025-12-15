[首页](./)

# 在Mac上的VS Code中使用Claude Code进行R编程

您已经在VS Code中设置好了R，可以手动编写代码。现在您希望AI帮助编写、改进和调试您的R代码，这样您就可以专注于数据分析。可以把Claude Code想象成一个生活在VS Code内部的编程伙伴——您描述您想要什么，它就会编写或改进代码，而您始终停留在同一个窗口中。

## 核心概念

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - 将Claude AI助手直接集成到编辑器中的VS Code扩展，支持内联代码编辑
- **Chat Panel（聊天面板）** - VS Code中的侧边面板，您可以在这里与Claude讨论您的代码
- **Inline Edits（内联编辑）** - Claude建议的代码更改会直接显示在您的文件中，以差异对比的形式呈现，您可以接受或拒绝

## 准备工作

- 完成[在VS Code中使用R](./R_Coding_VS_Code_Guide)教程 - R应该已经在VS Code中正常工作
- 完成[在Mac上安装Claude Code](./Install_Claude_Code_MacOS)教程 - Claude Code CLI应该已经安装
- Claude Pro/Max订阅或Anthropic API密钥
- 20-30分钟

## 步骤1：打开VS Code并创建R项目

- 打开**Visual Studio Code**
- 点击菜单栏中的**File**，然后选择**Open Folder**
- 导航到您的**Documents**文件夹
- 点击对话框底部的**New Folder**
- 将文件夹命名为`claude_r_test`
- 点击**Open**打开新文件夹
- 如果提示"Do you trust the authors?"，点击**Yes, I trust the authors**

## 步骤2：安装并登录Claude Code Extension

- 点击左侧边栏中的**Extensions**图标（四个方块图标）
- 在搜索框中输入`Claude Code`
- 找到Anthropic的**Claude Code**并点击**Install**
- 安装完成后，左侧边栏会出现一个Claude图标（星星图标）
- 点击Claude图标打开聊天面板
- 点击聊天面板中的**Sign in to Claude Code**
- 选择您的身份验证方法：
  - **Claude Pro/Max用户**：点击**Sign in with Claude.ai**，在浏览器中授权，然后将代码复制回VS Code
  - **API密钥用户**：点击**Use API Key**并粘贴您的Anthropic API密钥
- 有关详细的身份验证步骤，请参阅[在Mac上安装Claude Code](./Install_Claude_Code_MacOS)指南（步骤5）
- 登录后，您会在聊天面板中看到"Ready to help"

## 步骤3：手动创建初始R脚本

- 点击菜单栏中的**File > New File**
- 点击**Select a language**并输入`R`，然后选择**R**
- 点击**File > Save**保存文件，将其命名为`iris_analysis.R`
- 输入以下代码：

```r
data(iris)
str(iris)
summary(iris)
```

- 点击**File > Save**保存文件
- 打开R终端：点击菜单栏中的**View**，然后选择**Command Palette**，输入`R: Create R Terminal`，按Enter
- 选择代码并按`Ctrl+Enter`（Windows/Linux）或`Cmd+Enter`（Mac）运行
- 您应该在终端中看到数据集结构和摘要统计信息

## 步骤4：让Claude添加散点图

- 点击左侧边栏中的**Claude**图标打开聊天面板
- 在底部的聊天框中输入：

```
Add code to iris_analysis.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```

- 按Enter发送
- Claude会读取您的文件并提出更改建议——您会看到一个差异对比，显示要添加的新代码
- 点击**Accept**应用更改
- ggplot2代码会出现在您的文件中
- 如果您还没有安装ggplot2，请在R终端中运行`install.packages("ggplot2")`

## 步骤5：运行更新后的代码

- 选择`iris_analysis.R`中的所有代码
- 按`Ctrl+Enter`（Windows/Linux）或`Cmd+Enter`（Mac）
- 散点图会出现在单独的图形窗口中
- 您应该看到按物种（setosa、versicolor、virginica）着色的点

## 步骤6：让Claude优化图形

- 在Claude聊天面板中输入：

```
Remove title. Change marker type by species. Change to the classic theme.
```

- 按Enter
- Claude会显示更新后的代码更改
- 点击**Accept**
- 再次运行更新后的代码：选择全部并按`Ctrl+Enter` / `Cmd+Enter`
- 现在图形显示每个物种使用不同的标记形状，没有标题，并使用经典主题

## 步骤7：让Claude进行PCA分析

- 在Claude聊天面板中输入：

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- 按Enter
- Claude会向您的脚本添加PCA代码
- 点击**Accept**
- 运行所有代码：选择全部并按`Ctrl+Enter` / `Cmd+Enter`
- 会出现一个PCA图，显示投影到PC1和PC2上的样本，按物种着色

## 步骤8：让Claude审查并添加注释

- 在Claude聊天面板中输入：

```
Review the entire script for correctness. Add comments when necessary.
```

- 按Enter
- Claude会审查代码并建议添加解释每个部分的注释
- 点击**Accept**
- 您的脚本现在有了清晰的注释，解释了数据加载、可视化和PCA分析

## 下一步

- 让Claude创建R Markdown报告："Create an R Markdown file for this analysis"
- 使用Claude调试错误："This code gives Error X, can you fix it?"
- 请求统计检验："Add a t-test comparing sepal length between setosa and versicolor"
- 让Claude优化代码："Make this loop faster using vectorization"
- 获取不熟悉函数的帮助："Explain what dplyr::mutate does"

## 故障排除

- **Claude扩展未显示** - 安装后重启VS Code。点击**View > Extensions**验证它已安装。
- **"Cannot read R file"错误** - 确保您使用`.R`扩展名保存了文件。Claude需要保存的文件才能读取它们。
- **身份验证失败** - 验证您的Claude Pro/Max订阅是否有效或您的API密钥是否有效。有关身份验证故障排除，请参阅[在Mac上安装Claude Code](./Install_Claude_Code_MacOS)。
- **找不到ggplot2** - 在R终端中安装它：`install.packages("ggplot2")`。运行代码前等待安装完成。
- **代码更改未应用** - 确保在差异对比上点击了**Accept**。如果不起作用，尝试手动复制Claude建议的代码。

## 工作流程总结

- **Claude Code Extension**直接在VS Code中提供AI助手，带有聊天面板和内联差异对比
- **迭代优化** - 从基础代码开始，让Claude增强，立即测试，然后进一步优化
- **上下文感知** - Claude读取您的R文件并理解您的项目结构
- **内联编辑** - 建议的更改以差异对比的形式出现在您的实际文件中，而不是单独的聊天响应
- **保持专注** - 无需在浏览器和编辑器之间切换——一切都在VS Code中完成

---

由[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)创建于2025年12月11日。
