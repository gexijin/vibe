---
title: "在 VS Code 中使用 Claude Code 处理 Excel"
lang: "zh"
---
[首页](./)

# 在 VS Code 中使用 Claude Code 处理 Excel

你想做一个电子表格——有公式、有格式，也许再加一张图表——但不想和 Excel 的各种菜单较劲。不妨把 Claude Code 想象成一位对 Excel 了如指掌的助手：你用日常语言描述想要什么，它就会生成一个真正的 `.xlsx` 文件，里面的公式都能正常计算。本教程将教你如何在 VS Code 中建立项目文件夹，并让 Claude Code 为你创建和编辑 Excel 电子表格。

## 核心概念

- **xlsx skill** - Claude Code 的内置能力，可以创建和编辑 `.xlsx` 电子表格，支持真正的公式、格式和图表
- **[Spreadsheet Viewer 扩展](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)**（原名 Excel Viewer）- VS Code 扩展，让你无需离开编辑器就能预览和编辑电子表格文件
- **公式与固定数字** - Claude Code 写入的是真正的 Excel 公式（例如 `=SUM(B2:B9)`），所以当你修改数据时，表格会自动重新计算

## 你需要准备的内容

- 完成 [VS Code 入门指南](./VS_Code_Getting_Started)
- 已安装并能正常使用 Claude Code（参见 [在 Windows 上安装 Claude Code](./Install_CLAUDE_Code_Win) 或 [在 Mac 上安装 Claude Code](./Install_Claude_Code_MacOS)）
- 用于打开最终文件的 Microsoft Excel、LibreOffice Calc 或 Google Sheets（可选——没有这些软件，Spreadsheet Viewer 扩展也能正常使用）
- 15-20 分钟

## 步骤 1：在 VS Code 中安装 Spreadsheet Viewer 扩展

- 打开 VS Code
- 点击左侧边栏的 **Extensions** 图标（或点击 **View > Extensions**）
- 搜索 `GrapeCity.gc-excelviewer`
- 在 **MESCIUS** 发布的 **Spreadsheet Viewer** 上点击 **Install**

**注意**：这个扩展以前叫 **GrapeCity** 发布的 **Excel Viewer**，一些旧的教程和视频可能还在使用这个名字。现在搜索“Excel Viewer”会出现好几个其他扩展，所以请用上面的 ID 搜索，才能找到正确的那个。ID 仍然以 `GrapeCity` 开头——这是正常的。

安装后，你只需点击任意 `.xlsx` 文件，就能直接在 VS Code 中以电子表格的形式查看它，无需切换到其他应用。

## 步骤 2：创建项目文件夹

- 在电脑上新建一个文件夹（例如 `my-excel-project`）
- 在 VS Code 中，点击 **File > Open Folder**，然后选择刚才新建的文件夹
- 点击 **Select Folder**（Windows）或 **Open**（Mac）

## 步骤 3：启动 Claude Code

- 在 VS Code 中点击 **Terminal > New Terminal**
- 输入以下命令并按 Enter：

```bash
claude
```

- 如果是第一次使用，会弹出浏览器窗口进行身份验证——用你的 Claude 账号登录
- 当终端中出现 Claude 的欢迎信息后，回到 VS Code

## 步骤 4：创建你的第一个电子表格

- 在 Claude Code 终端中输入：

```
创建一个名为 budget.xlsx 的电子表格，包含“类别”、“月度金额”和“备注”三列。添加 6 个示例支出类别，比如房租、日用杂货和水电费，并填入符合实际的金额。在底部添加一个“合计”行，用公式对“月度金额”列求和。
```

- 按 Enter
- 看着 Claude 编写并运行一个 Python 脚本，在你的项目文件夹中生成 `budget.xlsx`
- Claude 还会重新计算这个文件，让公式显示真实的数字，而不是空白单元格

## 步骤 5：预览结果

- 在 VS Code 左侧的 Explorer 面板中，点击 `budget.xlsx`
- Spreadsheet Viewer 扩展会以电子表格的形式打开这个文件
- 如果你看到的是一堆乱码和符号，说明 VS Code 把文件当作纯文本打开了——请参阅下方的故障排除
- 点击底部的 **合计** 单元格——注意它是一个公式，而不是手动输入的数字
- 如果你安装了 Excel 或 LibreOffice Calc，也可以在 File Explorer（Windows）或 Finder（Mac）中双击这个文件，用它们打开

## 步骤 6：让 Claude 添加图表

- 回到 Claude Code 终端，输入：

```
在 budget.xlsx 中添加一个饼图，显示每个类别在每月总支出中所占的比例。
```

- 按 Enter
- 在 Spreadsheet Viewer 标签页中重新打开 `budget.xlsx`（点击刷新图标，或关闭后重新打开文件），就能看到新图表

## 步骤 7：编辑数据并让 Claude 更新

- 在 Spreadsheet Viewer 中（或者在已打开的 Excel/LibreOffice 中），修改其中一个金额（例如把房租翻倍）
- 保存文件
- 在 Claude Code 终端中输入：

```
我修改了 budget.xlsx 中的一些数字。请重新计算合计，并确保图表仍然与数据一致。
```

- 按 Enter
- Claude 会读取你的修改，重新计算公式，并确认一切都对得上

这就是核心工作流程：描述你想要的，让 Claude 来构建，检查结果，然后用日常语言提出修改要求。

## 步骤 8：让 Claude 清理杂乱的数据

Claude Code 也很擅长修复已经乱成一团的电子表格。

- 输入：

```
创建一个 messy_sales.csv 文件，包含 15 行销售数据，并故意带一些问题：几个空白单元格、不一致的日期格式，以及一行重复数据。然后创建一个名为 sales_clean.xlsx 的清理版本，修复这些问题，并说明你修复了哪些内容。
```

- 按 Enter
- 查看 Claude 给出的总结，了解它发现并修复了哪些问题
- 打开 `sales_clean.xlsx`，确认数据看起来正确

## 下一步

- 让 Claude 用你已有的 CSV 文件生成电子表格（先把文件拖进项目文件夹）
- 尝试更高级的请求：“添加条件格式，让超过 $500 的类别变成红色”
- 让 Claude 添加第二个工作表，用来汇总第一个工作表的数据
- 结合 [将 GitHub Desktop 与 Claude Code 结合使用](./GitHub_Desktop_Claude_Code_Workflow)，随时保存电子表格的各个版本
- 继续学习 [用 Vibe 编程在 Excel 中打造预算追踪表](./Vibe_Coding_Excel_Guide)，构建一个完整的多工作表项目

## 故障排除

- **`budget.xlsx` 打开后显示为乱码和符号（以 `PK` 开头）**：VS Code 显示的是原始文件内容，因为没有电子表格查看器来处理它。文件本身没有问题——`.xlsx` 是一个压缩包，而不是纯文本。请检查 MESCIUS 的 **Spreadsheet Viewer**（`GrapeCity.gc-excelviewer`）是否已安装并启用，然后关闭该标签页，在 Explorer 面板中右键点击 `budget.xlsx`，选择 **Open With...**，再选择 **Excel Editor**（Spreadsheet Viewer 用于 `.xlsx` 文件的编辑器）。如果还安装了其他电子表格扩展，请在同一列表中选择 **Configure default editor for '*.xlsx'...**，然后选择 **Excel Editor**，这样以后单击文件时就会默认使用它。
- **Spreadsheet Viewer 显示空白或损坏的预览**：关闭标签页后重新打开文件。如果仍然不行，改用 Excel、LibreOffice Calc 或 Google Sheets 打开——文件本身没有问题，只是预览出了小故障。
- **公式单元格显示为空白而不是数字**：这通常说明文件写入后没有重新计算。可以对 Claude 说：“重新计算 budget.xlsx，并确认没有公式错误。”
- **看不到 Claude 所做的修改**：确认你查看的是 Claude 编辑的同一个文件（核对它提到的文件名）。在 VS Code 中关闭并重新打开该标签页，强制刷新。
- **终端中提示“claude is not recognized”**：说明 Claude Code 没有正确安装。请重新查看适用于你系统的 [安装指南](./Install_CLAUDE_Code_Win)。

## 工作流程总结

- **VS Code** - 存放项目文件夹，并通过 Spreadsheet Viewer 扩展预览电子表格
- **Claude Code** - 根据你的日常语言请求，编写和编辑带有可用公式的真正 `.xlsx` 文件
- **Excel / LibreOffice / Google Sheets** - 可选，用于打开和手动微调 Claude 创建的文件
- **迭代** - 描述你想要的，检查结果，再描述下一个修改

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2026 年 9 月 21 日。
