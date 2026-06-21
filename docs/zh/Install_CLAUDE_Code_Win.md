[首页](./)

# 在 Windows 上安装 Claude Code

Claude Code 是一款运行在终端里的 AI 助手，能帮你编写、调试和理解代码。按照本指南，几分钟就能在 Windows 上完成原生安装并上手。如果想要更进阶的环境，指南末尾还介绍了可选的 WSL2 安装方法。

## 核心概念

- **PowerShell** - Windows 自带的命令行工具，本指南用它来安装和运行 Claude Code
- **Git for Windows** - 一款免费工具，自带 Claude Code 执行命令时使用的 shell **Git Bash**
- **WSL（Windows Subsystem for Linux）** - Windows 的一项可选功能，能在 Windows 里运行真正的 Linux 系统；指南末尾的进阶设置会用到

## 准备内容

- 一台 Windows 10 或 Windows 11 电脑
- Claude Pro/Max 订阅，或一个 API 密钥
- 5 - 10 分钟

## 步骤 1：安装 Git for Windows（可选，推荐）

Git for Windows **推荐但并非必需**，它会提供 Claude Code 执行命令时使用的 shell **Git Bash**。如果跳过，Claude Code 会改用 PowerShell，因此你也可以直接进入步骤 2，以后再装 Git。

- 访问 [git-scm.com/download/win](https://git-scm.com/download/win)，页面通常会自动开始下载，完成后打开安装程序
- 一路点击 **Next**，保持默认选项
- 点击 **Install**，最后点击 **Finish**

装好之后，Claude Code 启动时会自动识别 Git Bash。

## 步骤 2：安装 Claude Code

- 点击 **Windows 开始按钮**，输入 `PowerShell`，点击 **Windows PowerShell**
- 在 PowerShell 窗口里输入：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- 等待安装完成
- 关闭并重新打开 PowerShell，输入以下命令验证：
   ```
   claude --version
   ```
- 此时应该会显示 Claude Code 的版本号

## 步骤 3：连接 Anthropic 账户

### 选项 A. 使用 Claude Pro 或 Max 订阅

- 在 PowerShell 窗口里输入：
   ```
   claude
   ```
- Claude 会尝试打开浏览器。如果没能自动打开，按住 **Ctrl** 点击那一长串网址，或把网址复制到浏览器里打开
- 登录 Claude.ai 账户（用 Chrome 的话可能会自动登录）
- 点击 **Authorize**
- 看到一长串代码后，点击 **Copy Code**
- 回到终端窗口，**右键单击**后选择**粘贴**（或按 **Ctrl+Shift+V**）
- 看到成功提示后，按照提示完成后续设置

下面几种基于 API 的方式都在 **PowerShell** 里完成，用到的 `setx` 命令会把设置永久保存。运行 `setx` 之后，记得**先关闭再重新打开 PowerShell** 让设置生效，然后再启动 `claude`。

### 选项 B. 使用 Anthropic API 密钥

如果你用的是 Anthropic API 密钥，而不是 Claude 订阅：

- 先到 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥
- 在 PowerShell 里输入（把 `your-api-key-here` 换成你自己的密钥）：
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
- 关闭并重新打开 PowerShell 让设置生效，然后启动 Claude Code：
   ```
   claude
   ```

### 选项 C. 使用 OpenRouter API（可免费开始！）

OpenRouter 是一个统一的 API 网关，用一个密钥就能访问 500 多种大语言模型。它按用量计费，还能在不同价位的模型之间挑选，是一种比较省钱的 Claude Code 使用方式。

- 在 [openrouter.ai](https://openrouter.ai) 注册并登录
- 点击 **Get API key**，把密钥复制到安全的地方
- 在 PowerShell 里设置好这些环境变量：
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- 关闭并重新打开 PowerShell，再启动 Claude Code：
   ```
   claude
   ```
- 在 Claude Code 里输入 `/status`，确认连接是否成功

**注意：**
- 把 `your-openrouter-api-key` 换成你自己的 OpenRouter API 密钥
- `ANTHROPIC_API_KEY` 必须明确设为空值
- 想换用其他模型，它们必须支持**工具调用（tool use）功能**。可以这样覆盖默认模型：
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- 可用模型可在 [openrouter.ai/models](https://openrouter.ai/models) 查看
- 免费套餐每天有 50 次 API 请求额度
- 更多细节见[官方 OpenRouter 指南](https://openrouter.ai/docs/guides/claude-code-integration)

### 选项 D. 通过 Azure Foundry 使用 Anthropic API

在 PowerShell 里粘贴下面这段代码，定义相应的环境变量：
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

**注意：**把 `xxxx-eastus2` 换成你的 Foundry Resource 名称（不要填完整的基础 URL）；把 `your_api_key` 换成你在 Azure 门户里拿到的完整 API 密钥。

然后关闭并重新打开 PowerShell，再启动 Claude Code：
```
claude
```

这样就可以用 Azure 上部署的 Claude 模型来运行 Claude Code 了。

## 步骤 4：测试 Claude Code

全部搞定！在 PowerShell 里输入 `claude`，随便问它点什么，比如"解释一下量子计算"。

## 步骤 5：访问项目

- 如果已经有项目文件夹，在 PowerShell 里切换到该目录：
   ```
   cd ~/Documents/test_claude
   ```
- 然后启动 Claude：
   ```
   claude
   ```
- 可以先让 Claude 帮你讲解整个代码库，也可以让它直接帮你改代码
- 再用你惯用的 IDE 测试代码

**注意：**Claude 在项目文件夹里运行，并把设置保存在其中——这个文件夹就是它的工作区。

## 步骤 6：（可选）安装 WSL2 以获得完整的 Linux 体验

对大多数人来说，上面的原生设置已经够用了。不过 Claude Code 在 Linux 下会跑得更顺：WSL2 能在 Windows 里运行真正的 Linux 系统，带来 **Bash 工具沙盒**（一项安全特性），也能和各种 Linux 工具链配合得更好。它配置更花时间，还要重启电脑，所以只有在你确实想要完整 Linux 体验时再做这一步。

### a) 检查虚拟化并安装 WSL

**先检查虚拟化是否已启用：**

- **右键单击**任务栏（屏幕最下方的那条栏），在菜单里点击**任务管理器**
- 如果打开的是精简窗口，点击底部的**更多详细信息**
- 依次点击顶部的**性能**选项卡和左侧的 **CPU**
- 找到**虚拟化：**那一行，看它是否显示**已启用**

**如果显示"已禁用"：**你需要进入电脑的 BIOS 设置开启虚拟化：
- 重启电脑，开机过程中按下进入 BIOS 的按键（通常是 **F2**、**F10**、**Del** 或 **Esc**，具体取决于电脑品牌）
- 找到"Virtualization Technology"、"Intel VT-x"、"AMD-V"或"SVM Mode"等相关选项并开启
- 保存并退出 BIOS（通常按 **F10**）

**接下来安装 WSL：**

- 点击 **Windows 开始按钮**，输入 `PowerShell`
- **右键单击 Windows PowerShell**，选择**以管理员身份运行**
- 系统弹出"你要允许此应用对你的设备进行更改吗？"时，点击**是**
- 在 PowerShell 窗口里输入：
   ```
   wsl --install
   ```
- 你可能会看到"Installing: Windows Subsystem for Linux""Installing: Ubuntu"之类的提示
- 安装完成后重启电脑

**注意：**`wsl --install` 需要 Windows 10 版本 2004 及以上，或 Windows 11。如果系统提示无法识别该命令，可能是你的 Windows 版本太旧了。

### b) 设置 Ubuntu

电脑重启后，一个标题带有"Ubuntu"的终端窗口通常会在 2-5 分钟内自动弹出。如果没有，点击 **Windows 开始按钮**，输入 `Ubuntu`，再点击 **Ubuntu** 应用（橙色圆形图标）即可。

- 等待出现 `Enter new UNIX username:` 提示后，输入一个用户名（只用小写字母和数字，不要有空格），例如 `john`
- 看到 `New password:` 后，输入一个简单的密码（输入时屏幕不会显示任何字符，这是正常现象）
- 按提示再输入一次相同的密码

**重要：**记住这个用户名和密码，后面还会用到。

### c) 在 WSL 中安装 Claude Code

- 在 Ubuntu 终端里输入：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- 输入以下命令验证：
   ```
   claude --version
   ```
- 输入 `claude`，按浏览器登录流程连接账户（和步骤 3 的选项 A 一样）。如果改用 API 密钥，则用 `export ANTHROPIC_API_KEY="your-api-key-here"` 来设置（WSL 里用的是 Linux 命令，而不是 `setx`）
- 要在 WSL 中打开 Windows 上的项目文件夹（把 `Username` 换成你实际的 Windows 用户名）：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```

## 下一步

- **配置 VS Code**：先按 [VS Code Getting Started](VS_Code_Getting_Started) 指南操作，再用 [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win) 把它和 Claude Code 连接起来
- **学习 Git 基础**：用 [Claude Code Git on Windows](Claude_Code_Git_Windows) 给项目加上版本控制
- **动手做个项目**：跟着 [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) 走一遍，看看 Claude Code 的实战效果

## 故障排除

### 第一步：运行 Claude Doctor

遇到问题时，先运行下面这条命令试试：
```
claude doctor
```
这个内置的诊断工具会检查你的安装，并报告常见问题。

### 找不到 Claude 命令（原生 Windows）

- 关闭并重新打开 PowerShell
- 重新运行一遍安装命令：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- 确认 PATH 环境变量里包含 Claude 的安装目录

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
这个错误说明虚拟化还没开启：
- 在任务管理器里查看虚拟化是否已启用（参见上面可选的 WSL 部分）
- 如果是禁用状态，需要到电脑的 BIOS 里开启
- 开启后重启电脑，再次运行 `wsl --install`

### "wsl --install" 不起作用
- 确认是以管理员身份运行的 PowerShell
- 确认系统是 Windows 10 版本 2004 及以上，或 Windows 11
- 先运行 `wsl --update`，再重新执行 `wsl --install`

### 重启后 Ubuntu 窗口未打开
- 点击 **Windows 开始按钮**，输入 `Ubuntu`，再点击 **Ubuntu** 应用手动打开

## 需要帮助？

- WSL 相关问题：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Claude Code 相关问题：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 11 日。2026 年 6 月更新。
