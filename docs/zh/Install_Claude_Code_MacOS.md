[首页](../zh/)

# 在 Mac 上安装 Claude Code

Claude Code 是运行在终端中的 AI 编程助手,可以帮助你编写、调试和理解代码。把它想象成随时待命的编程伙伴。无论你是初学者还是经验丰富的开发者,Claude Code 都能提升你的工作效率。

本指南将逐步引导你完成安装,包含详细的初学者说明。

## 概览

- 下载并安装 Node.js
- 使用 npm 安装 Claude Code
- 配置 API 密钥
- 开始使用 Claude Code

## 核心概念

- **Terminal**:Mac 内置的命令行应用,通过输入命令来操作系统。这是与 Claude Code 交互的方式。
- **Node.js**:Claude Code 的运行环境,类似驱动 Claude Code 的引擎。
- **Claude Code**:运行在 Terminal 中的 AI 编程助手,可以回答问题、编写代码并帮助理解项目。

## 准备内容

- 运行 macOS 10.15 Catalina 或更高版本的 Mac 电脑
- 互联网连接
- 管理员权限
- Claude Pro/Max 订阅或 API 密钥
- 15-20 分钟

## 步骤 1:下载 Node.js

Claude Code 需要 Node.js 版本 18 或更高。

**首先检查是否已安装 Node.js:**

- 点击 Dock 中的 **Launchpad** 图标(彩色方块图标)
- 在搜索框中输入 `Terminal`
- 点击 **Terminal**(黑色方块图标)
- 输入以下命令:
  ```
  node --version
  ```
- 查看结果:
  - **显示 `v18.x.x` 或更高版本号**:Node.js 已安装,跳到步骤 4
  - **显示 "command not found"**:继续以下安装步骤

**下载 Node.js:**

- 打开网页浏览器(Safari、Chrome、Firefox 等)
- 访问 https://nodejs.org/
- 点击绿色按钮 **Get Node.js**
- 点击屏幕中间的绿色按钮 **macOS Installer (.pkg)**
- 文件将下载到 Downloads 文件夹(约 30-60 秒)
  - 文件名类似 `node-v24.x.x.pkg`

## 步骤 2:安装 Node.js

- 打开 **Finder**(Dock 中的蓝色笑脸图标)
- 点击左侧边栏的 **Downloads**
- 找到刚下载的文件(类似 `node-v24.x.x.pkg`)
- 双击文件
- 安装程序窗口出现,点击 **Continue**
- 在许可证屏幕点击 **Continue**
- 点击 **Agree** 接受许可证
- 点击 **Install**
- 输入 Mac 密码(登录密码)
- 点击 **Install Software**
- 等待安装完成(1-2 分钟)
- 看到 "The installation was successful" 后点击 **Close**
- 可将安装程序移至废纸篓

## 步骤 3:验证 Node.js 安装

- 点击 Dock 中的 **Launchpad** 图标(彩色方块图标)
- 在搜索框中输入 `Terminal`
- 点击 **Terminal**(黑色方块图标)
- 在 Terminal 中输入:
  ```
  node --version
  ```
- 应该显示类似 `v24.x.x` 的版本号(具体数字可能不同)
- 看到版本号说明 Node.js 已正确安装

**如果显示 "command not found":**
- 完全关闭 Terminal(菜单栏 **Terminal** > **Quit Terminal**)
- 重新打开 Terminal
- 再次运行命令

**提示:** 保持 Terminal 打开以继续下一步。

## 步骤 4:安装 Claude Code

- 在 Terminal 中输入:
  ```
  npm install -g @anthropic-ai/claude-code
  ```
- 等待安装完成(2-5 分钟)
- 如果出现 "permission denied" 错误,使用 `sudo`:
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
  输入 Mac 密码(输入时不显示)
- 可能看到黄色或红色警告文本,这是正常的
- 安装完成后验证:
  ```
  claude --version
  ```
- 应该显示 Claude Code 的版本号

## 步骤 5:连接 Anthropic 账户

### 选项 A. 使用 Claude Pro 或 Max 订阅

- 在 Terminal 中输入:
  ```
  claude
  ```
- Claude 会尝试打开浏览器。如果未自动打开,复制 Terminal 中的 URL 并粘贴到浏览器
- 登录 Claude.ai 账户(可能自动完成)
- 点击 **Authorize**
- 出现长代码时点击 **Copy Code**
- 返回 Terminal
- 粘贴代码:菜单栏 **Edit** > **Paste**
- 应该显示成功消息
- 按说明完成设置

### 选项 B. 使用 Anthropic API 密钥

如果使用 API 密钥而非 Claude 订阅:

- 从 [Anthropic Console](https://console.anthropic.com/) 获取 API 密钥
- 在 Terminal 中输入:
  ```
  export ANTHROPIC_API_KEY="your-api-key-here"
  ```
  将 `your-api-key-here` 替换为实际的 API 密钥
- 要永久保存(避免每次设置),添加到 shell 配置文件:
  ```
  echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
  ```
  将 `your-api-key-here` 替换为实际的 API 密钥
- 关闭并重新打开 Terminal 使更改生效

**注意:** 如果使用较旧的 Mac(bash 而非 zsh),将 `~/.zshrc` 替换为 `~/.bash_profile`。

### 选项 C. 通过 Azure Foundry 使用 Anthropic API

适用于使用 Azure 托管 Claude 模型的组织。在 Terminal 中粘贴以下代码定义环境变量(启动 Claude 前):
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

**注意:** 将 `xxxx-eastus2` 替换为 Foundry Resource 名称(仅名称,非完整 URL)。将 `your_api_key` 替换为从 Azure 门户获取的完整 API 密钥。

## 步骤 6:开始使用 Claude Code

一切就绪!使用方法:

- 在 Terminal 中输入:
  ```
  claude
  ```
- Claude 会先问几个问题
- 测试是否正常工作,可以问:"解释量子计算。"

## 步骤 7:导航到项目

- 如果 Mac 中有项目,先导航到项目文件夹:
  ```
  cd ~/Documents/test_claude
  ```
  将 `test_claude` 替换为实际的项目文件夹名称

- 然后启动 Claude:
  ```
  claude
  ```
- 先让 Claude 解释代码库
- 可以让 Claude 进行修改
- 在 IDE 中测试代码

**注意:** Claude 在项目文件夹内操作,控制写入权限并保存设置。这是 Claude 的工作区。

## 下一步
- [VS Code Getting Started](./VS_Code_Getting_Started.md) - 学习使用 VS Code,一个流行的代码编辑器
- [Claude Code in VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - 在 VS Code 中运行 Claude Code
- [Writing a Research Paper with Claude Code](./Writing_Research_Paper_Claude_Code.md) - 使用 Claude Code 进行学术写作

## 重新打开 Terminal

关闭 Terminal 后重新打开的方法:

- 点击 Dock 中的 **Launchpad** 图标(彩色方块图标)
- 在搜索框中输入 `Terminal`
- 点击 **Terminal**

## 故障排除

### Node.js 安装程序无法打开
- 确保从 nodejs.org 下载了 `.pkg` 文件
- 右键点击文件选择 **Open**,而非双击
- 前往 **System Settings** > **Privacy & Security** 点击 **Open Anyway**

### 安装后显示 "node: command not found"
- 完全关闭 Terminal(菜单栏 **Terminal** > **Quit Terminal**)
- 重新打开 Terminal
- 再次运行 `node --version`
- 如果仍无效,重启 Mac 后重试

### npm 安装权限错误
- 在命令前添加 `sudo`:
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
- 输入 Mac 密码(输入时不显示)

### 找不到 Claude Code 命令
- 确保 npm 安装已成功完成
- 关闭并重新打开 Terminal
- 检查是否已安装:`npm list -g @anthropic/claude-code`
- 重新安装:`npm install -g @anthropic-ai/claude-code`

### "Cannot find module" 错误
- 确保 Node.js 已正确安装:`node --version`
- 重新安装 Claude Code:`npm uninstall -g @anthropic/claude-code` 然后 `npm install -g @anthropic-ai/claude-code`

## Mac 用户提示

### 查找项目路径
快速获取文件夹路径:
- 打开 Finder
- 导航到项目文件夹
- 将文件夹拖放到 Terminal,完整路径自动显示

### 使用其他 Terminal 应用
可选择其他终端应用:
- iTerm2(功能更强的流行替代品)
- Warp(具有 AI 功能的现代终端)
- Hyper(跨平台终端)

Claude Code 兼容所有这些应用。

## 需要帮助?

- Node.js 下载:[Node.js Official Website](https://nodejs.org/)
- Node.js 问题:[Node.js Documentation](https://nodejs.org/docs/)
- npm 问题:[npm Documentation](https://docs.npmjs.com/)
- Claude Code 问题:[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

*最后更新:2025 年 12 月*
