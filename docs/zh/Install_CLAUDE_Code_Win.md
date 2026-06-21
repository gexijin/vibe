[首页](./)

# 在 Windows 上安装 Claude Code

Claude Code 是一款 AI 助手，运行在终端中，帮助你编写、调试和理解代码。本指南将带你完成在 Windows 上的原生安装，只需几分钟即可上手。指南末尾还提供了可选的、更进阶的 WSL2 设置方法。

## 核心概念

- **PowerShell** - Windows 内置的命令行工具，用于安装和运行 Claude Code
- **Git for Windows** - 一款可免费下载的工具，内含 **Git Bash**，也就是 Claude Code 用来运行命令的 shell
- **WSL（Windows Subsystem for Linux）** - 可选的 Windows 功能，可在 Windows 中运行真正的 Linux 系统，用于末尾的进阶设置

## 准备内容

- Windows 10 或 Windows 11 电脑
- Claude Pro/Max 订阅，或一个 API 密钥
- 5 - 10 分钟

## 步骤 1：安装 Git for Windows（推荐）

Git for Windows **推荐安装，但并非必需**。它提供 **Git Bash**，也就是 Claude Code 用来运行命令的 shell。如果跳过这一步，Claude Code 会改用 PowerShell——因此你也可以直接进入步骤 2，以后再安装 Git。

- 访问 [git-scm.com/download/win](https://git-scm.com/download/win)
- 下载通常会自动开始——完成后打开安装程序
- 在安装程序中一路点击 **Next**，保持默认选项即可
- 点击 **Install**，然后点击 **Finish**

完成后，Claude Code 在启动时会自动检测到 Git Bash。

## 步骤 2：安装 Claude Code

- 点击 **Windows 开始按钮**
- 输入 `PowerShell`，然后点击 **Windows PowerShell**
- 在 PowerShell 窗口中输入：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- 等待安装完成
- 关闭并重新打开 PowerShell，然后输入以下命令进行验证：
   ```
   claude --version
   ```
- 你应该会看到 Claude Code 的版本号

## 步骤 3：连接 Anthropic 账户

### 选项 A. 使用 Claude Pro 或 Max 订阅

- 在 PowerShell 窗口中输入：
   ```
   claude
   ```
- Claude 会尝试打开浏览器。如果无法自动打开，按住 **Ctrl** 并点击那串很长的 URL 在浏览器中打开；也可以复制该 URL 并粘贴到外部浏览器
- 登录 Claude.ai 账户（如果使用 Chrome，可能会自动完成）
- 点击 **Authorize**
- 出现一长串代码时，点击 **Copy Code**
- 返回终端窗口
- 在终端中粘贴：**右键单击**并选择**粘贴**（或按 **Ctrl+Shift+V**）
- 你应该会看到成功消息
- 按说明完成设置

下面这些使用 API 的选项都在 **PowerShell** 中操作，并使用 `setx` 命令，该命令会永久保存设置。运行 `setx` 后，请**关闭并重新打开 PowerShell** 使更改生效，然后再启动 `claude`。

### 选项 B. 使用 Anthropic API 密钥

如果使用 Anthropic API 密钥而非 Claude 订阅：

- 从 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥
- 在 PowerShell 中输入：
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
   将 `your-api-key-here` 替换为实际的 API 密钥
- 关闭并重新打开 PowerShell 使更改生效
- 启动 Claude Code：
   ```
   claude
   ```

### 选项 C. 使用 OpenRouter API（可免费开始！）

OpenRouter 是一个统一的 API 网关，通过单个 API 密钥可访问 500 多个大型语言模型。这是一种经济的 Claude Code 使用方式，因为你只需按使用量付费，并可从不同价位的模型中选择。

- 在 [openrouter.ai](https://openrouter.ai) 注册并登录
- 点击 **Get API key** 并将密钥复制到安全位置
- 在 PowerShell 中设置所需的环境变量：
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- 关闭并重新打开 PowerShell，然后启动 Claude Code：
   ```
   claude
   ```
- 在 Claude Code 中输入 `/status` 验证连接

**注意：**
- 将 `your-openrouter-api-key` 替换为实际的 OpenRouter API 密钥
- `ANTHROPIC_API_KEY` 必须显式设置为空
- 要使用替代模型，它们必须支持**工具使用功能**。可以通过以下方式覆盖模型：
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- 在 [openrouter.ai/models](https://openrouter.ai/models) 浏览可用模型
- 免费套餐每天提供 50 次 API 请求
- 详情请参阅[官方 OpenRouter 指南](https://openrouter.ai/docs/guides/claude-code-integration)

### 选项 D. 通过 Azure Foundry 使用 Anthropic API

在 PowerShell 中粘贴以下代码定义环境变量：
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**注意：**将 `xxxx-eastus2` 替换为 Foundry Resource 名称（不要使用完整的基础 URL）。将 `your_api_key` 替换为从 Azure 门户获得的完整 API 密钥。

然后关闭并重新打开 PowerShell，并启动 Claude Code：
```
claude
```

现在应该能使用 Azure 部署的 Claude 模型运行 Claude Code。

## 步骤 4：测试 Claude Code

一切就绪！在 PowerShell 中输入 `claude`，然后随便问它一个问题，例如"解释一下量子计算。"

## 步骤 5：访问项目

- 如果有项目文件夹，在 PowerShell 中导航到该文件夹：
   ```
   cd ~/Documents/test_claude
   ```
- 然后启动 Claude：
   ```
   claude
   ```
- 可以先让 Claude 为你解释代码库
- 也可以让 Claude 进行修改
- 在你常用的 IDE 中测试代码

**注意：**Claude 在项目文件夹内运行，将设置保存在该文件夹中。这是 Claude 的工作区。

## 步骤 6：（可选）安装 WSL2 以获得完整的 Linux 体验

上面的原生设置几乎已能满足大多数人的需求。不过 Claude Code 在 Linux 下表现更佳。WSL2 可在 Windows 中运行真正的 Linux 系统，提供 **Bash 工具沙盒**（一项安全特性），并与 Linux 工具链有更好的兼容性。它的设置耗时更长，还需要重启电脑，因此只有当你想要完整的 Linux 体验时，才需要进行此步骤。

### a) 检查虚拟化并安装 WSL

**首先，检查虚拟化是否已启用：**

- **右键单击**任务栏（屏幕底部的栏）
- 从菜单点击**任务管理器**
- 如果任务管理器以小窗口打开，点击底部的**更多详细信息**
- 点击顶部的**性能**选项卡
- 点击左侧边栏的 **CPU**
- 找到**虚拟化：**那一行，看它是否显示**已启用**

**如果显示"已禁用"：**需要在计算机的 BIOS 设置中启用虚拟化：
- 重启计算机
- 启动期间按 BIOS 键（通常是 **F2**、**F10**、**Del** 或 **Esc** — 取决于计算机制造商）
- 查找"Virtualization Technology"、"Intel VT-x"、"AMD-V"或"SVM Mode"相关设置
- 启用这些设置
- 保存并退出 BIOS（通常按 **F10**）

**现在安装 WSL：**

- 点击 **Windows 开始按钮**，输入 `PowerShell`
- **右键单击** **Windows PowerShell**，然后点击**以管理员身份运行**
- 弹出窗口询问"你要允许此应用对你的设备进行更改吗？"时，点击**是**
- 在 PowerShell 窗口中输入：
   ```
   wsl --install
   ```
- 可能会看到类似"Installing: Windows Subsystem for Linux"和"Installing: Ubuntu"的消息
- 安装完成后，重启计算机

**注意：**`wsl --install` 需要 Windows 10 版本 2004 或更高，或 Windows 11。如果命令无法识别，你的 Windows 版本可能太旧。

### b) 设置 Ubuntu

计算机重启后，标题中带有"Ubuntu"的终端窗口应该会在 2-5 分钟内自动打开。如果未打开，点击 **Windows 开始按钮**，输入 `Ubuntu`，然后点击 **Ubuntu** 应用（橙色圆形图标）。

- 等待出现提示：`Enter new UNIX username:`
- 输入用户名（仅使用小写字母和数字，不要有空格）——例如 `john`
- 随后会出现：`New password:`
- 输入一个简单的密码（输入时不会显示字符——这是正常的）
- 出现提示时再次输入相同的密码

**重要：**记住这个用户名和密码——以后会需要它们。

### c) 在 WSL 中安装 Claude Code

- 在 Ubuntu 终端中输入：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- 输入以下命令进行验证：
   ```
   claude --version
   ```
- 在 Ubuntu 终端中输入 `claude` 并按浏览器登录流程连接账户（与步骤 3 的选项 A 相同）。如果改用 API 密钥，使用 `export ANTHROPIC_API_KEY="your-api-key-here"` 设置（WSL 使用 Linux 命令，而非 `setx`）
- 从 WSL 打开 Windows 项目文件夹：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   将 `Username` 替换为实际的 Windows 用户名。

## 下一步

- **设置 VS Code**：按照 [VS Code Getting Started](VS_Code_Getting_Started) 指南操作，然后使用 [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win) 将其连接到 Claude Code
- **学习 Git 基础**：使用 [Claude Code Git on Windows](Claude_Code_Git_Windows) 为项目添加版本控制
- **尝试一个项目**：完成 [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code)，看看 Claude Code 的实际应用

## 故障排除

### 第一步：运行 Claude Doctor

如果遇到问题，先尝试运行以下命令：
```
claude doctor
```
这个内置诊断工具会检查你的安装情况并报告常见问题。

### 找不到 Claude 命令（原生 Windows）

- 关闭并重新打开 PowerShell
- 尝试重新运行安装命令：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- 确保 PATH 中包含 Claude 的安装目录

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
此错误表示未启用虚拟化：
- 在任务管理器中检查虚拟化是否已启用（参见上面的可选 WSL 部分）
- 如果已禁用，需要在计算机 BIOS 中启用
- 启用虚拟化后，重启计算机并再次尝试 `wsl --install`

### "wsl --install" 不起作用
- 确保以管理员身份运行 PowerShell
- 确保是 Windows 10 版本 2004+ 或 Windows 11
- 尝试先运行：`wsl --update`，然后再次尝试 `wsl --install`

### 重启后 Ubuntu 窗口未打开
- 点击 **Windows 开始按钮**，输入 `Ubuntu`，然后点击 **Ubuntu** 应用手动启动

## 需要帮助？

- 有关 WSL 问题：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- 有关 Claude Code 问题：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 11 日。2026 年 6 月更新。
