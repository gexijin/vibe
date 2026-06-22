---
title: "在 Mac 上安装 Claude Code"
lang: "zh"
---
[首页](./)

# 在 Mac 上安装 Claude Code

Claude Code 是运行在 Terminal 中的 AI 编程助手，可以帮助你编写、调试和理解代码。把它想象成随时待命的编程伙伴。无论你是初学者还是经验丰富的开发者，Claude Code 都能提升你的工作效率并帮助你学习。

本指南将逐步引导你完成安装，包含详细的初学者说明。

## 概览

- 打开 Terminal
- 安装 Claude Code
- 配置 API 连接
- 开始使用 Claude Code

## 核心概念

- **Terminal**：Mac 内置的命令行应用，通过输入命令来操作系统。这是与 Claude Code 交互的方式。
- **Claude Code**：运行在 Terminal 中的 AI 编程助手，可以回答问题、编写代码并帮助理解项目。

## 准备内容

- 运行 macOS 13.0 Ventura 或更高版本的 Mac 电脑
- 互联网连接
- 管理员权限
- Claude Pro/Max 订阅或 API 密钥
- 5 - 10 分钟

## 步骤 1：打开 Terminal

- 点击 Dock 中的 **Launchpad** 图标（彩色方块图标）
- 在搜索框中输入 `Terminal`
- 点击 **Terminal**（黑色方块图标）
- Terminal 窗口将打开，显示闪烁的光标

**提示：** 保持 Terminal 打开以继续下一步。

## 步骤 2：安装 Claude Code

在 Terminal 中复制并粘贴以下命令，然后按 **Return**：
```
curl -fsSL https://claude.ai/install.sh | bash
```

- 等待 Claude Code 安装完成（1-2 分钟）
- 安装过程中可能会看到一些进度信息，这是正常的
- 安装完成后，关闭并重新打开 Terminal，然后输入以下命令验证：
   ```
   claude --version
   ```
- 应该显示 Claude Code 的版本号

**替代方案：使用 Homebrew 安装**

如果你使用 Homebrew，可以通过以下命令安装 Claude Code：
```
brew install --cask claude-code
```

**提示：** 安装完成后运行 `claude doctor` 检查一切是否设置正确。

## 步骤 3：连接 Anthropic 账户

### 选项 A. 使用 Claude Pro 或 Max 订阅

- 在 Terminal 中输入：
   ```
   claude
   ```
- Claude 会尝试打开浏览器。如果未自动打开，复制 Terminal 中显示的 URL 并粘贴到浏览器
- 登录 Claude.ai 账户（可能自动完成）
- 点击 **Authorize**
- 出现长代码时点击 **Copy Code**
- 返回 Terminal 窗口
- 在 Terminal 中粘贴代码：点击菜单栏的 **Edit**，然后点击 **Paste**
- 应该显示成功消息
- 按照说明完成设置

### 选项 B. 使用 Anthropic API 密钥

如果使用 Anthropic API 密钥而非 Claude 订阅：

- 首先从 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥
- 在 Terminal 中输入：
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   将 `your-api-key-here` 替换为实际的 API 密钥
- 要永久保存（避免每次都要设置），添加到 shell 配置文件：
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```
   将 `your-api-key-here` 替换为实际的 API 密钥
- 关闭并重新打开 Terminal 使更改生效

**注意：** 如果使用较旧的 Mac（bash 而非 zsh），将上面命令中的 `~/.zshrc` 替换为 `~/.bash_profile`。

### 选项 C. 使用 OpenRouter API（免费开始！）

OpenRouter 是一个统一的 API 网关，通过单一 API 密钥可访问 500 多个大型语言模型。这是使用 Claude Code 的经济方式，因为你只需按使用量付费，并可以从不同价位的模型中选择。

- 在 [openrouter.ai](https://openrouter.ai) 注册并登录
- 点击 **Get API key** 并将密钥复制到安全位置
- 在启动 Claude Code 之前设置所需的环境变量：
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
- 将 `your-openrouter-api-key` 替换为你的实际 OpenRouter API 密钥
- `ANTHROPIC_API_KEY` 必须显式设置为空
- 要使用替代模型，它们必须支持**工具使用功能**。你可以通过以下方式覆盖模型：
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- 在 [openrouter.ai/models](https://openrouter.ai/models) 浏览可用模型
- 免费套餐每天提供 50 次 API 请求
- 查看[官方 OpenRouter 指南](https://openrouter.ai/docs/guides/claude-code-integration)了解更多详情


### 选项 D. 通过 Azure Foundry 使用 Anthropic API

适用于使用 Azure 托管 Claude 模型的组织。在 Terminal 中粘贴以下代码定义环境变量（启动 Claude 前）：
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

**注意：** 将 `xxxx-eastus2` 替换为你的 Foundry Resource 名称（仅名称，不要使用完整的 URL）。将 `your_api_key` 替换为从 Azure 门户获取的完整 API 密钥。

## 步骤 4：测试 Claude Code

一切就绪！以下是使用 Claude Code 的方法：

- 在 Terminal 中输入：
   ```
   claude
   ```
- Claude 会先问你几个问题，然后准备好开始对话
- 要测试是否正常工作，可以问一个一般性问题，例如"解释量子计算。"

## 步骤 5：导航到项目

- 如果 Mac 中有项目文件夹，可以先导航到该文件夹：
   ```
   cd ~/Documents/test_claude
   ```
   将 `test_claude` 替换为实际的项目文件夹名称

- 然后启动 Claude：
   ```
   claude
   ```
- 先让 Claude 解释代码库
- 可以让 Claude 进行修改
- 在你常用的 IDE 中测试代码

**注意：** Claude 在项目文件夹内操作，控制该文件夹的写入权限并在其中保存设置。这是 Claude 的工作区。

## 步骤 6：更新 Claude Code

通过原生安装程序安装的 Claude Code 会在后台自动更新。你也可以手动触发更新：

- 在 Terminal 中输入：
   ```
   sudo claude
   ```
- Claude Code 会检查更新并安装最新版本

**注意：** 通过 Homebrew 安装的版本不会自动更新。请定期运行 `brew upgrade claude-code` 以获取最新版本。

## 下一步
- [VS Code 入门指南](./VS_Code_Getting_Started.md) - 学习使用 VS Code，一款流行的代码编辑器
- [在 Mac 上的 VS Code 中使用 Claude Code](./Claude_Code_in_VS_Code_Mac.md) - 在 VS Code 中运行 Claude Code
- [使用 Claude Code 撰写研究论文](./Writing_Research_Paper_Claude_Code.md) - 使用 Claude Code 进行学术写作

## 重新打开 Terminal

关闭 Terminal 后，重新打开的方法：

- 点击 Dock 中的 **Launchpad** 图标（彩色方块图标）
- 在搜索框中输入 `Terminal`
- 点击 **Terminal**
- Terminal 窗口将打开

## 故障排除

### 第一步：运行 Claude Doctor
如果遇到问题，首先运行以下命令：
```
claude doctor
```
它会检查你的安装并报告所有问题。

### 安装脚本失败
- 确保 macOS 版本为 13.0 或更高
- 尝试 Homebrew 替代方案：`brew install --cask claude-code`
- 检查网络连接并重试

### 找不到 Claude Code 命令
- 完全关闭 Terminal（点击菜单栏的 **Terminal**，然后点击 **Quit Terminal**）
- 重新打开 Terminal
- 输入 `claude --version` 检查是否已安装
- 尝试重新运行安装命令：`curl -fsSL https://claude.ai/install.sh | bash`

### 认证失败
- 确保你有有效的 Claude Pro/Max 订阅或有效的 API 密钥
- 尝试重新运行 `claude` 并完成登录流程
- 检查浏览器是否打开了正确的授权页面

## Mac 用户提示

### 查找项目路径
快速获取文件夹路径：
- 打开 Finder
- 导航到项目文件夹
- 将文件夹拖放到 Terminal，完整路径会自动显示！

### 使用其他 Terminal 应用
你也可以使用其他终端应用，例如：
- iTerm2（功能更强的流行替代品）
- Warp（具有 AI 功能的现代终端）
- Hyper（跨平台终端）

Claude Code 兼容所有这些应用！

## 需要帮助？

- Claude Code 问题：[Claude Code GitHub](https://github.com/anthropics/claude-code)
- 官方安装文档：[Claude Code Setup Guide](https://code.claude.com/docs/en/setup)

---

*最后更新：2026 年 2 月*
