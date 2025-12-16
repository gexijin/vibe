[首页](./)

# 版本控制入门指南

你正在做一个项目，结果改动了一些东西把一切都搞坏了。你不记得改了什么，真希望能回到代码还能用的时候。版本控制就像电子游戏中的存档点——每次"提交"工作时，就创建了一个可以随时返回的还原点。[GitHub](https://github.com) 将你的存档点保存在云端，这样代码就被安全备份，可从任何电脑访问。

## 核心概念

- **Git** - 版本控制软件，在你的电脑上跟踪文件的变更
- **GitHub** - 在云端存储代码的网站，就像代码的 Google Drive
- **GitHub Desktop** - 让 Git 变得简单易用的应用，用按钮操作而不是命令
- **Repository(仓库/repo)** - 跟踪所有变更的项目文件夹

## 你需要准备的

- Windows、macOS 或 Linux 电脑
- 互联网连接
- 用于创建 GitHub 账户的电子邮箱
- 15-20 分钟

## 第 1 步：创建 GitHub 账户

- 打开网页浏览器
- 访问 [github.com](https://github.com)
- 点击 **Sign up**
- 输入你的邮箱，创建密码，选择用户名
- 完成验证步骤

## 第 2 步：下载 GitHub Desktop

- 访问 [desktop.github.com](https://desktop.github.com)
- 点击 **Download** 按钮
- 打开下载的文件进行安装

**在 Windows 上：**
- 双击安装程序文件
- GitHub Desktop 会自动安装并打开

**在 Mac 上：**
- 打开下载的 `.zip` 文件
- 将 **GitHub Desktop** 拖到你的应用程序文件夹
- 从应用程序打开 GitHub Desktop

## 第 3 步：登录 GitHub Desktop

- 打开 GitHub Desktop
- 点击 **Sign in to GitHub.com**
- 你的浏览器会打开——点击 **Authorize desktop**
- 返回 GitHub Desktop
- 点击 **Finish** 完成设置

## 第 4 步：创建你的第一个仓库

- 在 GitHub Desktop 中，点击 **Create a New Repository on your Hard Drive**
- 填写表单：
  - **Name：** `my-first-project`(或任何你喜欢的名字)
  - **Description：** `Learning version control`(可选)
  - **Local Path：** 选择保存位置(Documents 文件夹就可以)
  - 勾选 **Initialize this repository with a README**
- 点击 **Create Repository**

## 第 5 步：打开你的项目文件夹

- 在 GitHub Desktop 中，点击菜单栏中的 **Repository**
- 选择 **Show in Finder**(Mac)或 **Show in Explorer**(Windows)
- 你会看到一个以你的项目命名的文件夹
- 里面有一个名为 `README.md` 的文件

## 第 6 步：做出第一次修改

- 在任何文本编辑器中打开 `README.md`(Notepad、TextEdit 或 VS Code)
- 将内容替换为：
  ```
  # My First Project

  I'm learning version control with GitHub Desktop.

  ## What I'm Building

  This is a practice project to learn how to:
  - Track changes to my code
  - Create save points (commits)
  - Back up my work to GitHub
  ```
- 点击 **File** → **Save**

## 第 7 步：创建你的第一个提交(存档点)

- 返回 GitHub Desktop
- 你会在右侧看到高亮显示的变更(绿色 = 添加的内容，红色 = 删除的内容)
- 在左下角，输入提交消息：`Updated README with project description`
- 点击蓝色的 **Commit to main** 按钮

## 第 8 步：推送到 GitHub(备份到云端)

- 点击顶部蓝色的 **Publish repository** 按钮
- 保持名称不变
- 如果想让其他人看到，取消勾选"Keep this code private"(可选)
- 点击 **Publish Repository**

你的代码现在已在线备份到：`https://github.com/YOUR-USERNAME/my-first-project`

## 接下来的步骤

- 再次编辑你的 README 文件并提交变更
- 在项目文件夹中创建一个新文件并提交
- 探索 **History** 标签，查看项目如何随时间演变

## 故障排除

- **无法登录 GitHub** - 检查互联网连接。先尝试在 github.com 登录以验证凭据是否有效。
- **变更没有出现在 GitHub Desktop 中** - 确保已保存文件。点击 **Repository** → **Refresh** 或重启 GitHub Desktop。
- **推送失败并显示"rejected"错误** - 有其他人推送了变更。先点击 **Fetch origin**，然后再尝试推送。

## 工作流程概览

- 对项目文件进行修改
- 在 GitHub Desktop 中查看变更(绿色 = 添加的内容，红色 = 删除的内容)
- 写一条描述性的提交消息并点击 **Commit to main**
- 点击 **Push origin** 备份到 GitHub
- 重复以上步骤

---

创建于 2025 年 12 月 7 日，作者：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)。
