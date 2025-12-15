[首页](./)

# 在 Windows 上使用 WSL 安装 Claude Code

Claude Code 是一个强大的 AI 编程助手，但 Windows 用户面临一个挑战：许多开发工具在 Linux 上运行得更好。解决方案是什么？WSL（Windows Subsystem for Linux）让你可以在 Windows 内部运行完整的 Linux 环境——就像在一台电脑上拥有两台电脑。本指南将带你完成整个设置，让你可以在大约 20 分钟内开始使用 Claude 编程。

## 关键概念

- **WSL（Windows Subsystem for Linux）** - 一个 Windows 功能，可以在 Windows 中运行真正的 Linux 系统
- **Ubuntu** - 一个流行的、对初学者友好的 Linux 发行版，我们将通过 WSL 安装它
- **PowerShell** - Windows 内置的命令行工具，在这里用于安装 WSL
- **Node.js** - Claude Code 运行所需的 JavaScript 运行时环境
- **Terminal** - 用于运行命令的基于文本的界面（如 Ubuntu 的命令行）

## 你需要准备的

- Windows 10（版本 2004 或更高）或 Windows 11 电脑
- 计算机的管理员访问权限
- Claude Pro/Max 订阅或通过 Azure Foundry 获取的 API 密钥
- 15-20 分钟

## 步骤 1：检查是否启用虚拟化

在安装 WSL 之前，你需要验证计算机上是否启用了虚拟化。这是 WSL 工作所必需的。

- **右键单击**任务栏（屏幕底部的栏）
- 从菜单中点击**任务管理器**
- 如果任务管理器以小窗口打开，点击底部的**更多详细信息**
- 点击顶部的**性能**选项卡
- 点击左侧边栏中的 **CPU**
- 查看窗口右下角的部分
- 找到显示**虚拟化：**的行，检查它是否显示**已启用**

**如果显示"已启用"：**太好了！继续步骤 2。

**如果显示"已禁用"：**你需要在计算机的 BIOS 设置中启用虚拟化：
- 重启计算机
- 在启动期间，按 BIOS 键（通常是 **F2**、**F10**、**Del** 或 **Esc** - 取决于你的计算机制造商）
- 查找与"Virtualization Technology"、"Intel VT-x"、"AMD-V"或"SVM Mode"相关的设置
- 启用这些设置
- 保存并退出 BIOS（通常按 **F10**）
- 你的计算机将正常重启

## 步骤 2：以管理员身份打开 PowerShell

- 点击 **Windows 开始按钮**（左下角的 Windows 图标）
- 在搜索框中输入 `PowerShell`
- 在搜索结果中，你会看到 **Windows PowerShell**
- **右键单击** **Windows PowerShell**
- 从菜单中点击**以管理员身份运行**
- 会弹出一个窗口询问"你要允许此应用对你的设备进行更改吗？"
- 点击**是**

将打开一个带有白色文本的蓝色窗口——这就是以管理员身份运行的 PowerShell。

## 步骤 3：安装 WSL

**首先，检查是否已经安装了 WSL 和 Ubuntu：**

- 在 PowerShell 窗口中，输入：
   ```
   wsl --list --verbose
   ```
- 查看结果：
   - **如果看到列出的"Ubuntu"**，STATE 为"Running"或"Stopped"：WSL 和 Ubuntu 已经安装！跳到步骤 4。
   - **如果看到错误消息**或"Windows Subsystem for Linux has no installed distributions"：继续下面的安装。

**安装 WSL 和 Ubuntu：**

- 在 PowerShell 窗口中，输入：
   ```
   wsl --install
   ```
- 你可能会看到类似"Installing: Windows Subsystem for Linux"和"Installing: Ubuntu"的消息
- 当你看到安装完成的消息时，需要重启计算机：
   - 点击 **Windows 开始按钮**
   - 点击**电源图标**
   - 点击**重启**
- 你的计算机将重启——这需要大约 1-2 分钟

**为什么需要重启：**重启允许 Windows 启用刚刚安装的 WSL 和虚拟机平台功能。

**注意：**如果出现命令无法识别的错误，你的 Windows 版本可能太旧。确保你有 Windows 10 版本 2004 或更高版本，或 Windows 11。运行 Windows Update 以获取最新版本。

## 步骤 4：设置 Ubuntu（仅首次）

计算机重启后，标题中带有"Ubuntu"的终端窗口应该会在 2-5 分钟内自动打开。

**如果 Ubuntu 窗口没有自动打开：**
- 点击 **Windows 开始按钮**
- 在搜索框中输入 `Ubuntu`
- 点击 **Ubuntu**（你会看到一个橙色圆形图标）
- Ubuntu 终端将打开并继续设置

**现在完成首次设置：**

- 等待消息：`Enter new UNIX username:`
- 输入用户名（仅使用小写字母和数字，不要有空格）
   - 例如：`john`
- 你会看到：`New password:`
- 输入一个简单的密码（甚至可以与用户名相同，如 `john`）
- 在输入时你不会看到字符——这是正常的
- 提示时再次输入相同的密码

**重要：**记住这个用户名和密码——你以后会需要它们。

## 步骤 5：更新 Ubuntu

- 在 Ubuntu 终端窗口中，输入：
   ```
   sudo apt update
   ```
- 提示时输入你的密码（你刚创建的密码）
- 接下来，输入：
   ```
   sudo apt upgrade -y
   ```
- 等待所有软件包升级（这可能需要 5 分钟）

## 步骤 6：安装 Node.js

Claude Code 需要 Node.js 版本 18 或更高。按照以下步骤操作：

- 在 Ubuntu 终端中，复制并粘贴以下命令：

   首先，下载 nvm 安装程序：
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   cat install.sh | bash
   \. "$HOME/.nvm/nvm.sh"
   nvm install 24
   ```
   这首先下载 nvm 安装程序，安装它，然后使用它安装 node.js v 24.0
- 等待 Node.js 安装（2-5 分钟）
- 通过输入以下命令验证安装：
   ```
   node --version
   ```
- 你应该看到类似 `v24.x.x` 的内容（具体数字可能有所不同）

## 步骤 7：安装 Claude Code

- 在 Ubuntu 终端中，输入：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- 等待 Claude Code 安装（2-5 分钟）
- 你可能会看到一些黄色或红色文本的警告——这通常是正常的
- 安装完成后，通过输入以下命令验证：
   ```
   claude --version
   ```
- 你应该看到 Claude Code 的版本号

## 步骤 8：配置你的 Anthropic API 连接

### 选项 A. 使用你的 Claude Pro 或 Max 订阅

- 在 Ubuntu 终端中，输入：
   ```
   claude
   ```
- Claude 尝试打开浏览器。如果它无法自动打开，按住 **Ctrl** 并点击长 URL 以在浏览器中打开它。或者，复制 URL 并将其粘贴到外部浏览器中。
- 登录到你的 Claude.ai 账户（如果你使用 Chrome，这可能会自动发生）
- 点击**授权**
- 当出现长代码时，点击**复制代码**
- 返回终端窗口
- 在终端中粘贴：**右键单击**并选择**粘贴**（或按 **Ctrl+Shift+V**）
- 你应该看到成功消息
- 按照说明完成设置

### 选项 B. 使用 Anthropic API 密钥

如果你有 Anthropic API 密钥而不是 Claude 订阅：

- 首先，从 [Anthropic Console](https://console.anthropic.com/) 获取你的 API 密钥
- 在 Ubuntu 终端中，输入：
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   将 `your-api-key-here` 替换为你的实际 API 密钥
- 要使其永久生效（这样你就不必每次都设置它），将其添加到你的 shell 配置文件：
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   将 `your-api-key-here` 替换为你的实际 API 密钥
- 关闭并重新打开 Ubuntu 终端以使更改生效
- 你现在应该能够使用你的 API 密钥使用 Claude Code

### 选项 C. 通过 Azure Foundry 使用 Anthropic API

在启动 Claude Code 之前，在 Ubuntu 终端窗口中，粘贴此代码以定义环境变量：
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**注意：**将 `xxxx-eastus2` 替换为你的 Foundry Resource 名称（不要使用整个基础 URL）。将 `your_api_key` 替换为你从 Azure 门户获得的完整 API 密钥。

然后启动 Claude Code：
```
claude
```

你现在应该能够使用 Azure 部署的 Claude 模型使用 Claude Code。


## 步骤 9：测试 Claude Code

一切就绪！要查看它是否有效，问一个一般性问题，例如"解释量子计算。"

## 步骤 10：访问你的 Windows 项目
- 如果你有一个名为 `test_claude` 的 Windows 文件夹，其中包含项目的文件，你可以访问它：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   将 `Username` 替换为你的实际 Windows 用户名。
- 然后启动 Claude：
   ```
   claude
   ```
- 首先要求 Claude 向你解释代码库。
- 你可以要求 Claude 进行更改。
- 在你喜欢的 IDE 中测试你的代码。

**注意：**Claude 在项目文件夹内运行。它将设置保存在该文件夹中。这是 Claude 的工作区。

## 下一步

- **设置 VS Code**：按照 [VS Code Getting Started](VS_Code_Getting_Started) 指南操作，然后使用 [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win) 将其连接到 Claude Code
- **学习 Git 基础**：使用 [Claude Code Git on Windows](Claude_Code_Git_Windows) 为你的项目添加版本控制
- **尝试一个项目**：完成 [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code)，看看 Claude Code 的实际应用

## 故障排除

### 关闭后如何打开 Ubuntu 终端
- 点击 **Windows 开始按钮**，输入 `Ubuntu`，然后点击 **Ubuntu** 应用（橙色圆形图标）

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
此错误意味着未启用虚拟化：
- 返回步骤 1 并检查任务管理器以查看是否启用了虚拟化
- 如果已禁用，你需要在计算机的 BIOS 中启用它（有关说明，请参见步骤 1）
- 启用虚拟化后，重启计算机并再次尝试 `wsl --install`

### "wsl --install" 不起作用
- 确保你以管理员身份运行 PowerShell
- 确保你有 Windows 10 版本 2004+ 或 Windows 11
- 尝试先运行：`wsl --update`，然后再次尝试 `wsl --install`

### 重启后 Ubuntu 窗口未打开
- 点击 Windows 开始
- 输入 `Ubuntu`
- 点击 Ubuntu 应用以手动启动它

### "sudo: apt: command not found"
- 你的 WSL 可能未正确安装
- 在 PowerShell（以管理员身份）中，输入：`wsl --unregister Ubuntu`
- 然后再次运行 `wsl --install`

### Node.js 安装失败
- 确保你首先运行了 `sudo apt update`
- 再次尝试安装命令

### 找不到 Claude Code 命令
- 确保安装成功完成
- 尝试关闭并重新打开 Ubuntu 终端
- 尝试再次运行安装命令：`curl -fsSL https://claude.ai/install.sh | bash`

## 需要帮助？

- 有关 WSL 问题：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- 有关 Claude Code 问题：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 11 日。
