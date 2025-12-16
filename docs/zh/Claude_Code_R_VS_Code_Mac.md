[首页](./)

# 在Mac上的VS Code中使用Claude Code进行R编程

你已经在VS Code中设置好了R，可以手动编写代码。现在你希望AI帮助编写、改进和调试你的R代码，专注于数据分析本身。把Claude Code想象成你在VS Code中的编程伙伴——描述你想要什么，它就会编写或改进代码，无需切换窗口。

## 核心概念

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - 将Claude AI助手集成到VS Code的扩展，支持内联代码编辑
- **Chat Panel（聊天面板）** - VS Code侧边栏面板，用于与Claude讨论代码
- **Inline Edits（内联编辑）** - Claude建议的代码更改以差异对比形式显示在文件中，可接受或拒绝

## 准备工作

- 完成[在VS Code中使用R](./R_Coding_VS_Code_Guide)教程 - R已在VS Code中正常工作
- 完成[在Mac上安装Claude Code](./Install_Claude_Code_MacOS)教程 - Claude Code CLI已安装
- Claude Pro/Max订阅或Anthropic API密钥
- 20-30分钟

## 步骤1：打开VS Code并创建R项目

- 打开**Visual Studio Code**
- 点击菜单栏中的**File**，然后选择**Open Folder**
- 导航到**Documents**文件夹
- 点击对话框底部的**New Folder**
- 将文件夹命名为`claude_r_test`
- 点击**Open**打开新文件夹
- 如果提示"Do you trust the authors?"，点击**Yes, I trust the authors**

## 步骤2：安装并登录Claude Code Extension

- 点击左侧边栏的**Extensions**图标（四个方块图标）
- 在搜索框中输入`Claude Code`
- 找到Anthropic的**Claude Code**并点击**Install**
- 安装完成后，左侧边栏会出现Claude图标（星星图标）
- 点击Claude图标打开聊天面板
- 点击聊天面板中的**Sign in to Claude Code**
- 选择身份验证方法：
  - **Claude Pro/Max用户**：点击**Sign in with Claude.ai**，在浏览器中授权，然后将代码复制回VS Code
  - **API密钥用户**：点击**Use API Key**并粘贴Anthropic API密钥
- 详细身份验证步骤请参阅[在Mac上安装Claude Code](./Install_Claude_Code_MacOS)指南（步骤5）
- 登录后，聊天面板会显示"Ready to help"

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
- 应该在终端中看到数据集结构和摘要统计信息

## 步骤4：让Claude添加散点图

- 点击左侧边栏的**Claude**图标打开聊天面板
- 在底部聊天框中输入：

```
在 iris_analysis.R 中添加代码，创建萼片长度与宽度的散点图，按物种着色。使用 ggplot2。
```

- 按Enter发送
- Claude会读取文件并建议更改——以差异对比显示要添加的新代码
- 点击**Accept**应用更改
- ggplot2代码会出现在文件中
- 如果尚未安装ggplot2，在R终端中运行`install.packages("ggplot2")`

## 步骤5：运行更新后的代码

- 选择`iris_analysis.R`中的所有代码
- 按`Ctrl+Enter`（Windows/Linux）或`Cmd+Enter`（Mac）
- 散点图会出现在单独的图形窗口中
- 应该看到按物种（setosa、versicolor、virginica）着色的点

## 步骤6：让Claude优化图形

- 在Claude聊天面板中输入：

```
移除标题。按物种更改标记类型。更改为 classic 主题。
```

- 按Enter
- Claude会显示更新后的代码更改
- 点击**Accept**
- 再次运行更新后的代码：选择全部并按`Ctrl+Enter` / `Cmd+Enter`
- 现在图形显示每个物种使用不同的标记形状，没有标题，并使用经典主题

## 步骤7：让Claude进行PCA分析

- 在Claude聊天面板中输入：

```
添加代码对数值变量进行 PCA 分析，并使用前两个主成分绘制样本图。
```

- 按Enter
- Claude会向脚本添加PCA代码
- 点击**Accept**
- 运行所有代码：选择全部并按`Ctrl+Enter` / `Cmd+Enter`
- 会出现PCA图，显示样本投影到PC1和PC2上，按物种着色

## 步骤8：让Claude审查并添加注释

- 在Claude聊天面板中输入：

```
检查整个脚本的正确性。必要时添加注释。
```

- 按Enter
- Claude会审查代码并建议添加注释
- 点击**Accept**
- 脚本现在有了清晰的注释，解释了数据加载、可视化和PCA分析

## 下一步

- 让Claude创建R Markdown报告："为这个分析创建一个 R Markdown 文件"
- 使用Claude调试错误："这段代码报错 X，你能修复吗？"
- 请求统计检验："添加 t 检验比较 setosa 和 versicolor 的萼片长度"
- 让Claude优化代码："使用向量化使这个循环更快"
- 获取不熟悉函数的帮助："解释 dplyr::mutate 的作用"

## 故障排除

- **Claude扩展未显示** - 安装后重启VS Code。点击**View > Extensions**验证已安装。
- **"Cannot read R file"错误** - 确保使用`.R`扩展名保存文件。Claude需要已保存的文件才能读取。
- **身份验证失败** - 验证Claude Pro/Max订阅或API密钥是否有效。身份验证故障排除请参阅[在Mac上安装Claude Code](./Install_Claude_Code_MacOS)。
- **找不到ggplot2** - 在R终端中安装：`install.packages("ggplot2")`。运行代码前等待安装完成。
- **代码更改未应用** - 确保在差异对比上点击了**Accept**。如果不起作用，尝试手动复制Claude建议的代码。

## 工作流程总结

- **Claude Code Extension**在VS Code中提供AI助手，带有聊天面板和内联差异对比
- **迭代优化** - 从基础代码开始，让Claude增强，立即测试，然后进一步优化
- **上下文感知** - Claude读取R文件并理解项目结构
- **内联编辑** - 建议的更改以差异对比形式显示在实际文件中，而非单独的聊天响应
- **保持专注** - 无需在浏览器和编辑器之间切换——一切都在VS Code中完成

---

由[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)创建于2025年12月11日。
