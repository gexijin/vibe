[首页](./)

# Claude Code：基本操作

学习使用AI辅助编程一开始可能会让人感到不知所措。把Claude Code想象成坐在你身边的知识渊博的同事——你用简单的中文描述你想要什么，它就会帮助你实现。本教程将教你日常使用的基本操作，从开始对话到管理工作空间。

## 关键概念

- **Workspace（工作空间）** - 如果你从某个文件夹启动Claude Code，那个文件夹就是会话的工作空间。
- **REPL（读取-求值-打印循环）** - 一个交互式会话，你输入命令，Claude回应，对话持续进行直到你退出。
- **Context（上下文）** - Claude记住的代码和对话历史的数量；就像工作记忆，会随着时间填满。
- **Slash Commands（斜杠命令）** - 以`/`开头的内置快捷命令，用于执行特定操作，如清除历史记录或显示帮助。

## 你需要准备什么

- 已从[Windows](Install_CLAUDE_Code_Win.md)或[Mac](Install_Claude_Code_MacOS.md)教程安装Claude Code
- 基本熟悉使用Terminal或命令提示符
- 互联网连接
- 15-20分钟

## 步骤1：打开你的Terminal

- **Windows**：按Windows键，输入`Ubuntu`，然后按Enter打开WSL终端
- **Mac**：按`Cmd+Space`，输入`Terminal`，然后按Enter

将打开一个文本窗口，你可以在其中输入命令。

## 步骤2：获取演示项目

我们将使用一个真实的数据科学项目来探索Claude Code的功能。你可以用Git克隆它，也可以直接下载。

**选项A：使用Git克隆（如果你已安装Git）：**

```
git clone https://github.com/gexijin/data_projects
cd data_projects
```

**选项B：不使用Git直接下载：**

- 在浏览器中访问[https://github.com/gexijin/data_projects](https://github.com/gexijin/data_projects)
- 点击右上方的绿色**Code**按钮
- 点击**Download ZIP**
- 将ZIP文件解压到一个你记得住的位置（比如桌面或文档文件夹）
- 在Terminal中，导航到解压后的文件夹：
  - **Windows**：`cd C:\Users\YourName\Downloads\data_projects-main`
  - **Mac/Linux**：`cd ~/Downloads/data_projects-main`

将`YourName`替换为你的实际用户名，如果你解压到其他位置，请相应调整路径。

## 步骤3：从文件夹启动Claude Code

在你的Terminal中（确保你在data_projects文件夹内），输入：

```bash
claude
```

你将看到欢迎消息和Claude Code提示符。

## 步骤4：询问关于你项目的问题

Claude Code会在需要时自动读取你的文件。尝试这些问题来了解你的项目：

**询问文件夹结构：**

```
这个项目的文件夹结构是什么？
```

**询问技术栈：**

```
这个项目使用了哪些技术和库？
```

**询问最近的更改：**

```
这个项目最后一次更改是什么？
```

Claude会检查Git历史（如果可用）并告诉你最近的提交。

你可以用自然语言向Claude询问关于代码的任何问题。它会根据需要读取文件来回答你的问题。

## 步骤5：基本的斜杠命令

输入`/`然后按Enter，可以查看所有可用命令。以下是最重要的几个：

**查看所有命令：**

```
/
```

这会显示所有斜杠命令的菜单。使用方向键浏览，按Enter选择，或按Esc取消。

**获取帮助：**

```
/help
```
显示关于使用Claude Code的文档。



**检查上下文使用情况：**
管理上下文（Claude的"工作记忆"）非常重要。

```
/context
```

**清除对话历史：**

当上下文填满时，使用`/clear`开始新对话。
```
/clear
```
清除当前对话并重新开始。当你想要更换话题或对话变得太长时使用此命令。管理上下文至关重要。


**退出Claude Code：**

```
/exit
```

结束你的会话并返回到正常的Terminal提示符。你也可以按两次**Ctrl + C**。

## 步骤6：键盘快捷键

这些快捷键让使用Claude Code更快：

- **Shift+Tab** - 在计划模式、编辑模式或正常模式之间切换 - 对于复杂任务先进行计划
- **Alt+Enter**（Windows/Linux）或**Option+Return**（Mac）- 在消息中添加新行而不发送
- **Ctrl+C** - 取消当前操作或Claude的响应
- **Ctrl+D** - 当Claude请求权限时批准文件更改
- **Esc** - 关闭菜单或取消当前输入

## 步骤7：始终创建CLAUDE.md文件

CLAUDE.md文件是你项目的Claude使用说明手册。它在会话之间持久保存，所以Claude能记住关于你项目的重要上下文。

**创建文件：**

```
/init
```

Claude将创建一个包含你项目摘要的文件。这个文件保存在项目根目录中，每次启动新会话时Claude都会自动读取它。

你可以随时编辑项目文件夹中的CLAUDE.md，添加项目特定的说明、编码规范或重要上下文，如文件的用途等。

## 步骤8：引用文件或代码行

你可以使用`@`来引用特定文件：

```
解释 @Visualization/Matplotlib/Nested_Pie_Chart.ipynb 中的代码
```

Claude将读取该笔记本并解释它做什么、如何工作以及代码实现了什么。这有效地将文件带入上下文中。

如果你在VS Code中使用Claude Code并已安装Claude Code扩展，只需打开文件即可将其添加到上下文中。你会在命令窗口的右下角看到显示`In Nested_Pie_Chart.ipynb`。然后Claude就知道你在谈论这个文件。

此外，你可以选择几行代码，Claude会显示**3 lines selected**（已选择3行）。你可以要求Claude快速修改这些行或提出问题。因此，我强烈建议在VS Code中使用Claude Code。


## 步骤9：使用Linux命令执行操作

Claude可以通过多种形式运行Linux命令来执行操作。

- 安装软件
  ```
  安装pandas库
  ```

- 启动版本控制
  ```
  使用Git开始跟踪更改。我的名字是James Bond，我的电子邮件是bond@earth.com
  ```
- 提交更改
  ```
  提交这些更改。
  ```
- 查找并下载数据
  ```
  从UCI下载葡萄酒质量数据集。将它放在一个名为wine的新文件夹中。
  ```

- 执行代码
  ```
  将嵌套饼图代码重写为常规Python脚本。
  运行它并将新代码和图表保存在同一文件夹中。
  ```

我们可以问这个模糊的问题，因为我们刚刚要求它解释代码。之后会发生很多事情。Claude会安装软件、排查错误、解决环境问题——都是自动完成的。



你基本上拥有了一个Linux bash命令专家。只要你管理好权限并批准操作，你就可以非常高效。

## 下一步

现在你已经了解了基础知识，可以自己尝试这些：

- 要求Claude解释项目文件夹中的一个机器学习算法
- 请求修改现有笔记本（如更改图表颜色或添加新功能）
- 创建一个使用项目数据的新Python脚本
- 要求Claude比较代码库中的两种不同方法

## 故障排除

- **"Command not found"（命令未找到）错误** - Claude Code未安装或不在你的PATH中。运行`npm install -g @anthropic-ai/claude-code`来安装它。
- **Claude给出过时信息** - 使用`/clear`清除上下文并重新询问。长对话会填满Claude的内存。
- **文件更改不起作用** - 确保你在项目文件夹中有写权限。Claude会在修改文件之前请求批准——按Ctrl+D来批准。
- **上下文快速填满** - 使用`/context`检查使用情况。当接近满时，使用`/clear`开始一个全新的对话。

## 工作流程概述

使用Claude Code遵循以下模式：

- 在项目文件夹中使用`claude`启动Claude
- 用自然语言提问
- Claude根据需要读取文件并做出响应
- 请求代码更改——Claude在修改文件之前会请求权限
- 更换话题或上下文满时使用`/clear`
- 完成后使用`/exit`

创建者：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)，2025年12月14日。
