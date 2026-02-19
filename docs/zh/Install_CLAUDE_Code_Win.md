[首页](./)

# 在 Windows 上安装 Claude Code

Claude Code 是一款 AI 助手,运行在终端中,帮助你编写、调试和理解代码。本指南将带你完成整个设置过程:先通过 PowerShell 进行快速原生安装,然后安装 WSL2 以获得完整的 Linux 驱动体验。

## 核心概念

- **WSL（Windows Subsystem for Linux）** - Windows 功能,可在 Windows 中运行真正的 Linux 系统
- **Ubuntu** - 对初学者友好的流行 Linux 发行版,可通过 WSL 安装
- **PowerShell** - Windows 内置的命令行工具,用于安装 Claude Code 和 WSL

## 准备内容

- Windows 10（版本 2004 或更高）或 Windows 11 电脑
- 管理员访问权限
- Claude Pro/Max 订阅或通过 Azure Foundry 获取的 API 密钥
- 10 - 15 分钟

## 步骤 1：在 Windows 上原生安装 Claude Code（可用但不推荐）

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
- 应该显示 Claude Code 的版本号

> **注意：**原生 Windows 安装有一些局限性：
> - 没有 Bash 工具沙盒功能（这是仅在 WSL2/macOS 上可用的安全特性）
> - 部分工具和工作流在 Linux 环境中运行效果更佳
>
> 请继续以下步骤安装 WSL2 以获得完整体验。

## 步骤 2：检查虚拟化并安装 WSL

**首先，检查虚拟化是否已启用：**

- **右键单击**任务栏（屏幕底部的栏）
- 从菜单点击**任务管理器**
- 如果任务管理器以小窗口打开，点击底部的**更多详细信息**
- 点击顶部的**性能**选项卡
- 点击左侧边栏的 **CPU**
- 查看窗口右下角
- 找到显示**虚拟化：**的行，检查是否显示**已启用**

**如果显示"已启用"：**很好！继续下面的操作。

**如果显示"已禁用"：**需要在 BIOS 设置中启用虚拟化：
- 重启计算机
- 启动期间按 BIOS 键（通常是 **F2**、**F10**、**Del** 或 **Esc** — 取决于计算机制造商）
- 查找"Virtualization Technology"、"Intel VT-x"、"AMD-V"或"SVM Mode"相关设置
- 启用这些设置
- 保存并退出 BIOS（通常按 **F10**）
- 计算机将正常重启

**现在安装 WSL：**

- 点击 **Windows 开始按钮**
- 在搜索框中输入 `PowerShell`
- **右键单击** **Windows PowerShell**，然后点击**以管理员身份运行**
- 弹出窗口询问"你要允许此应用对你的设备进行更改吗？"时，点击**是**

**检查是否已安装 WSL 和 Ubuntu：**

- 在 PowerShell 窗口中输入：
   ```
   wsl --list --verbose
   ```
- **如果看到列出的"Ubuntu"：**WSL 已安装！跳到步骤 3。
- **如果看到错误消息：**继续下面的安装。

**安装 WSL 和 Ubuntu：**

- 在 PowerShell 窗口中输入：
   ```
   wsl --install
   ```
- 可能看到类似"Installing: Windows Subsystem for Linux"和"Installing: Ubuntu"的消息
- 安装完成后，重启计算机：
   - 点击 **Windows 开始按钮** → **电源图标** → **重启**
- 计算机将重启——约 1-2 分钟

**注意：**如果出现命令无法识别的错误，Windows 版本可能太旧。请确保是 Windows 10 版本 2004 或更高，或 Windows 11。

## 步骤 3：设置 Ubuntu

计算机重启后，标题中带有"Ubuntu"的终端窗口应该会在 2-5 分钟内自动打开。

**如果 Ubuntu 窗口未自动打开：**
- 点击 **Windows 开始按钮**
- 在搜索框中输入 `Ubuntu`
- 点击 **Ubuntu**（橙色圆形图标）
- Ubuntu 终端将打开并继续设置

**完成首次设置：**

- 等待消息：`Enter new UNIX username:`
- 输入用户名（仅使用小写字母和数字，不要有空格）
   - 例如：`john`
- 看到：`New password:`
- 输入一个简单的密码（甚至可与用户名相同，如 `john`）
- 输入时不显示字符——这是正常的
- 提示时再次输入相同密码

**重要：**记住这个用户名和密码——以后会需要它们。

## 步骤 4：在 WSL 中安装 Claude Code

- 在 Ubuntu 终端中输入：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- 等待 Claude Code 安装
- 安装完成后验证：
   ```
   claude --version
   ```
- 应该显示 Claude Code 的版本号

## 步骤 5：连接 Anthropic 账户

### 选项 A. 使用 Claude Pro 或 Max 订阅

- 在 Ubuntu 终端中输入：
   ```
   claude
   ```
- Claude 尝试打开浏览器。如果无法自动打开，按住 **Ctrl** 并点击长 URL 在浏览器中打开。或者复制 URL 并粘贴到外部浏览器
- 登录 Claude.ai 账户（如果使用 Chrome，这可能自动完成）
- 点击 **Authorize**
- 出现长代码时点击 **Copy Code**
- 返回终端窗口
- 在终端中粘贴：**右键单击**并选择**粘贴**（或按 **Ctrl+Shift+V**）
- 应该显示成功消息
- 按说明完成设置

### 选项 B. 使用 Anthropic API 密钥

如果使用 Anthropic API 密钥而非 Claude 订阅：

- 从 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥
- 在 Ubuntu 终端中输入：
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   将 `your-api-key-here` 替换为实际的 API 密钥
- 要永久保存（避免每次设置），添加到 shell 配置文件：
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   将 `your-api-key-here` 替换为实际的 API 密钥
- 关闭并重新打开 Ubuntu 终端使更改生效
- 现在应该能使用 API 密钥运行 Claude Code

### 选项 C. 使用 OpenRouter API（可免费开始！）

OpenRouter 是一个统一的 API 网关，通过单个 API 密钥可访问 500 多个大型语言模型。这是一种经济的 Claude Code 使用方式，因为你只需按使用量付费，并可从不同价位的模型中选择。

- 在 [openrouter.ai](https://openrouter.ai) 注册并登录
- 点击 **Get API key** 并将密钥复制到安全位置
- 启动 Claude Code 前设置所需的环境变量：
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- 启动 Claude Code：
   ```
   claude
   ```
- 在 Claude Code 中输入 `/status` 验证连接

**注意：**
- 将 `your-openrouter-api-key` 替换为实际的 OpenRouter API 密钥
- `ANTHROPIC_API_KEY` 必须显式设置为空
- 要使用替代模型，它们必须支持**工具使用功能**。可以通过以下方式覆盖模型：
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- 在 [openrouter.ai/models](https://openrouter.ai/models) 浏览可用模型
- 免费层每天提供 50 次 API 请求
- 详情请参阅[官方 OpenRouter 指南](https://openrouter.ai/docs/guides/claude-code-integration)

### 选项 D. 通过 Azure Foundry 使用 Anthropic API

启动 Claude Code 前，在 Ubuntu 终端中粘贴以下代码定义环境变量：
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**注意：**将 `xxxx-eastus2` 替换为 Foundry Resource 名称（不要使用完整的基础 URL）。将 `your_api_key` 替换为从 Azure 门户获得的完整 API 密钥。

然后启动 Claude Code：
```
claude
```

现在应该能使用 Azure 部署的 Claude 模型运行 Claude Code。

## 步骤 6：测试 Claude Code

一切就绪！在 Ubuntu 终端中输入 `claude`，然后问一个一般性问题，例如"Explain quantum computing."

## 步骤 7：访问项目

**原生 Windows（PowerShell）：**
- 如果有项目文件夹，导航到该文件夹：
   ```
   cd ~/Documents/test_claude
   ```
- 然后启动 Claude：
   ```
   claude
   ```

**WSL（Ubuntu）：**
- 如果有一个名为 `test_claude` 的 Windows 文件夹，可以访问它：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   将 `Username` 替换为实际的 Windows 用户名。
- 然后启动 Claude：
   ```
   claude
   ```

- 先让 Claude 解释代码库
- 可以让 Claude 进行修改
- 在 IDE 中测试代码

**注意：**Claude 在项目文件夹内运行，将设置保存在该文件夹中。这是 Claude 的工作区。

## 步骤 8：更新 Claude Code

Claude Code 会自动更新，但你也可以随时手动更新：

**WSL（Ubuntu）：**
```
sudo claude update
```

**原生 Windows（以管理员身份运行 PowerShell）：**
```
claude update
```

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
- 返回步骤 2，在任务管理器中检查虚拟化是否已启用
- 如果已禁用，需要在计算机 BIOS 中启用（详见步骤 2 的说明）
- 启用虚拟化后，重启计算机并再次尝试 `wsl --install`

### "wsl --install" 不起作用
- 确保以管理员身份运行 PowerShell
- 确保是 Windows 10 版本 2004+ 或 Windows 11
- 尝试先运行：`wsl --update`，然后再次尝试 `wsl --install`

### 重启后 Ubuntu 窗口未打开
- 点击 Windows 开始
- 输入 `Ubuntu`
- 点击 Ubuntu 应用手动启动

### 关闭后如何打开 Ubuntu 终端
- 点击 **Windows 开始按钮**，输入 `Ubuntu`，然后点击 **Ubuntu** 应用（橙色圆形图标）

### 找不到 Claude Code 命令（WSL）
- 确保安装成功完成
- 尝试关闭并重新打开 Ubuntu 终端
- 再次运行安装命令：`curl -fsSL https://claude.ai/install.sh | bash`

## 需要帮助？

- 有关 WSL 问题：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- 有关 Claude Code 问题：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 11 日。2026 年 2 月更新。
