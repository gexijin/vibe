[首页](./)

# VS Code 入门指南

您想要编写代码，但记事本或文本编辑器功能有限。您需要一个能帮助您更快编码的工具——具有语法高亮、自动完成和内置工具。**VS Code 就像一个智能的代码笔记本**——它能理解您正在编写的内容并在过程中提供帮助。[Visual Studio Code](https://code.visualstudio.com) 是免费的，可在任何操作系统上运行，并被数百万开发者使用。

## 核心概念

- **Editor（编辑器）** - 您编写代码的主要区域
- **Explorer（资源管理器）** - 显示文件和文件夹的侧边栏
- **Extensions（扩展）** - 为 VS Code 提供新功能的附加组件
- **Integrated Terminal（集成终端）** - VS Code 内置的命令行工具

## 所需准备

- Windows、macOS 或 Linux 计算机
- 互联网连接
- 约 500 MB 磁盘空间
- 20-25 分钟

## 步骤 1：下载并安装 VS Code

- 访问 [code.visualstudio.com](https://code.visualstudio.com)
- 点击 **Download** 按钮（会自动检测您的操作系统）
- 运行安装程序：
   - **Windows：** 双击 `.exe` 文件，在提示中点击 **Next**
   - **Mac：** 打开 `.dmg` 文件，将 VS Code 拖到 **Applications** 文件夹
   - **Linux：** 根据您的包管理器遵循相应说明
- 启动 VS Code

您会看到一个欢迎标签页，其中包含入门选项。

## 步骤 2：界面导览

VS Code 有五个主要区域：

- **Activity Bar（活动栏）**（左边缘）- Explorer、Search、Git、Extensions 等图标
- **Side Bar（侧边栏）** - 显示所选活动的内容（文件、搜索结果）
- **Editor（编辑器）**（中央）- 您编写代码的地方
- **Panel（面板）**（底部）- Terminal、Problems、Output
- **Status Bar（状态栏）**（底部边缘）- 关于文件和项目的信息

点击 **Explorer** 图标（活动栏顶部）可查看文件浏览器。

## 步骤 3：打开文件夹并浏览

- 点击 **File** → **Open Folder**
- 导航到计算机上的任何现有文件夹（例如 Documents）
- 点击 **Open**（或 **Select Folder**）
- 如果提示"Do you trust the authors?"，点击 **Yes, I trust the authors**

Explorer 侧边栏现在显示您文件夹中的文件：

- 点击文件夹可展开它
- 点击任何文件可在编辑器中打开
- 点击活动栏中的 **Search** 图标（放大镜）可在所有文件中搜索

## 步骤 4：创建 Markdown 文件

- 在 Explorer 中，点击 **New File** 图标（带 + 的页面图标）
- 将其命名为 `README.md`
- 添加以下内容：

```
# My Project

This is a **demo project** for learning VS Code.

## Features
- Easy to edit
- Markdown formatting
- Live preview

## Next Steps
1. Add more content
2. Try other file types
3. Explore extensions
```
- 点击 **File** → **Save** 保存

Markdown 是一种简单的文本格式，使用 `#` 表示标题，`**` 表示粗体，`-` 表示列表等符号。它广泛用于文档编写以及与 ChatGPT 和 Claude 等 LLM 的交互。

## 步骤 5：安装 Markdown Preview Extension

- 点击活动栏中的 **Extensions** 图标（方块图标）
- 在搜索框中输入 `Markdown Preview Enhanced`
- 在结果中找到 **Markdown Preview Enhanced**
- 点击 **Install**

## 步骤 6：预览 Markdown 文件

- 打开 `README.md`（如果尚未打开）
- 在编辑器中右键点击，选择 **Markdown Preview Enhanced: Open Preview to the Side**

预览面板会打开，显示格式化后的 Markdown——在左侧编辑，在右侧实时查看更改！

## 步骤 7：使用集成终端

- 点击 **Terminal** → **New Terminal**
- 尝试以下命令：

**列出文件：**
```
ls
```
（在 Windows 命令提示符中，使用 `dir`）

**打印当前工作目录：**
```
pwd
```
（在 Windows 命令提示符中，使用 `cd`）

**创建新文件夹：**
```
mkdir notes
```

查看 Explorer——`notes` 文件夹出现了！终端在您的项目文件夹中运行，因此命令会直接影响您的项目。

## 步骤 8：在 VS Code 中使用 AI Agent（可选）

VS Code 包含 [GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)，这是一个可以解释、编写和调试代码的 AI 助手。

- 打开 `README.md` 文件（或项目中的任何其他文件）
- 点击标题栏中的 **Chat** → **Open Chat**（或在 Windows/Linux 上按 `Ctrl+Alt+I`，在 Mac 上按 `Ctrl+Cmd+I`）
- 如果提示，请使用您的 **GitHub 账户**登录（有免费计划可用）
- 在打开的聊天面板中，输入："Explain this file"
- 按 **Enter**

GitHub Copilot 会分析您的文件并解释其功能。您可以要求它编写新代码、修复错误，或回答诸如"How do I add more features?"之类的问题。

**提示：** 对于[内联编辑](https://code.visualstudio.com/docs/copilot/copilot-chat)，在任何文件中高亮显示代码并按 `Ctrl+I`（Windows/Linux）或 `Cmd+I`（Mac），要求 Copilot 仅修改、修复或解释该部分。

## 如何重新打开项目

- 从开始菜单（Windows）、Spotlight（Mac）或应用程序（Linux）打开 VS Code
- 点击 **File** → **Open Recent** → 选择您的文件夹
- 或点击 **File** → **Open Folder** 并导航到它

## 故障排除

- **预览未显示：** 确保已安装 Markdown Preview Enhanced extension，并且您打开了 `.md` 文件
- **Terminal 显示错误目录：** 点击终端面板中的垃圾桶图标，然后点击 **Terminal** → **New Terminal**
- **Chat 菜单不可见：** 可能需要安装 GitHub Copilot Chat——点击 **Extensions** 图标，搜索"GitHub Copilot Chat"，然后安装
- **Extensions 无法工作：** 点击 **View** → **Command Palette**，输入"reload window"，并选择 **Developer: Reload Window**

## 完整工作流程

1. 在 VS Code 中打开文件夹
2. 创建/编辑文件
3. 使用 extensions 进行预览
4. 使用 terminal 执行命令
5. 使用 AI 理解和改进代码
6. 保存并重复

## 后续步骤

- **尝试其他文件类型：** 创建 `.html`、`.css`、`.js` 或 `.py` 文件，查看 VS Code 的语法高亮功能
- **探索 AI 功能：** 让 AI 编写代码、修复错误或为您的项目提供改进建议
- **安装更多 extensions：** 尝试"Prettier"进行自动格式化，或"GitLens"获取 Git 功能
- **学习快捷键：** 点击 **Help** → **Keyboard Shortcuts Reference** 加快您的工作流程

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
