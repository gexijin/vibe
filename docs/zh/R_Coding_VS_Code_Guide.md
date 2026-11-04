---
title: "在 VS Code 中运行 R"
lang: "zh"
---
[首页](./)

# 在 VS Code 中运行 R

想编写 R 代码，却觉得 RStudio 太重？或者更喜欢 VS Code 的灵活性？把 VS Code 想象成瑞士军刀——一个轻量级编辑器就能处理 R、Python 等多种语言。本教程将教你在 VS Code 中设置 R，获得代码补全、交互式绘图，甚至运行 Shiny 应用。

## 关键概念

- **[languageserver](https://github.com/REditorSupport/languageserver)** - R 包，在 VS Code 中启用代码补全、语法检查和悬停文档
- **[R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - VS Code 扩展，连接编辑器和 R，提供语法高亮、代码执行和调试
- **[Shiny Extension](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - VS Code 扩展，用于创建和运行交互式 Shiny Web 应用，支持自动重载

## 你需要准备的

- 完成 [VS Code 入门指南](./VS_Code_Getting_Started)
- 互联网连接以下载 R 和软件包
- 10-15 分钟

## 步骤 1：安装或更新 R

需要 R 4.0 或更高版本以获得最佳兼容性。

- **Windows**：
  - 从 [CRAN Windows](https://cran.r-project.org/bin/windows/base/) 下载最新 R 并运行安装程序
  - 安装时，**记住安装路径**（如：`C:\Program Files\R\R-4.6.1`）
  - 如有旧版本，先通过"设置 > 应用"卸载

- **macOS**：
  - 从 [CRAN macOS](https://cran.r-project.org/bin/macosx/) 下载并运行 .pkg 安装程序
  - 无论是 Intel 还是 Apple Silicon Mac,CRAN 安装程序都会把 R 安装在 `/Library/Frameworks/R.framework/Resources/bin/R`（如果你改用 Homebrew 安装 R，在 Apple Silicon 上则位于 `/opt/homebrew/bin/R`）
  - 如是更新，新版本会替换旧版本

- **Linux**：
  - 使用包管理器（如 Ubuntu 上用 `sudo apt install r-base`）
  - 或遵循 [CRAN Linux](https://cran.r-project.org/bin/linux/) 说明

步骤 4 中会配置 VS Code 以找到 R，所以如果 `R --version` 在终端还不起作用，不必担心。

## 步骤 2：在 VS Code 中安装 R 扩展

- 打开 VS Code
- 点击左侧边栏的 **Extensions**（扩展）图标
- 搜索 `REditorSupport.r`，点击 REditorSupport 的 R 扩展上的 **Install**
- 搜索 `Posit.shiny`，点击 Posit 的 Shiny 扩展上的 **Install**

## 步骤 3：查找你的 R 安装路径

配置 VS Code 前，需要知道 R 安装在系统的什么位置。

### Windows 用户

- 打开**文件资源管理器**
- 导航至 `C:\Program Files\R\`
- 会看到类似 `R-4.6.1` 的文件夹（你的版本号可能不同）
- 打开该文件夹 → 打开 `bin` 文件夹
- 会看到 `R.exe`
- 完整路径为：`C:\Program Files\R\R-4.6.1\bin\R.exe`

**记住版本号**（如 `R-4.6.1`）——步骤 4 需要用到。

### macOS 用户

R 安装通常位于以下位置之一：

- **标准安装（Intel 或 Apple Silicon）**：`/Library/Frameworks/R.framework/Resources/bin/R`
- **Apple Silicon 上的 Homebrew**：`/opt/homebrew/bin/R`
- **Intel 上的 Homebrew**：`/usr/local/bin/R`

验证路径，打开**终端**并输入：
```bash
which R
```

会显示 R 安装的确切路径。

### Linux 用户

R 通常安装在：`/usr/bin/R`

打开终端，输入以下命令验证：
```bash
which R
```

## 步骤 4：配置 VS Code 以找到 R

- VS Code 中，点击 **View > Command Palette**
- 输入 `Preferences: Open User Settings (JSON)` 并选择它
- settings.json 文件会打开
- 在花括号 `{}` 内添加适合你平台的那一行。如果里面已有其他行，确保你添加的这行上方那一行以逗号结尾

**对于 Windows**，添加此行（将 `R-4.6.1` 替换为你在步骤 3 中的版本）：

```json
"r.executablePath": "C:\\Program Files\\R\\R-4.6.1\\bin\\R.exe",
```

**为什么用两个反斜杠（`\\`）？**在 JSON 文件中，反斜杠 `\` 是特殊字符（称为转义字符）。要在实际文件路径中表示单个反斜杠，必须输入两个反斜杠 `\\`。因此，`C:\Program Files` 在 settings.json 中变成 `C:\\Program Files`。

**对于 macOS**，添加以下行之一：

```json
"r.executablePath": "/Library/Frameworks/R.framework/Resources/bin/R",
```

或者，如果在 Apple Silicon 上通过 Homebrew 安装 R:

```json
"r.executablePath": "/opt/homebrew/bin/R",
```

**对于 Linux**，添加：

```json
"r.executablePath": "/usr/bin/R",
```

- 点击 **File > Save** 保存文件
- **完全重启 VS Code** 以使更改生效

## 步骤 5：安装所需的 R 包

- VS Code 中，点击顶部菜单的 **View**，然后选择 **Command Palette**
- 输入 `R: Create R Terminal` 并选择
- R 控制台会出现在底部终端面板
  - 应该会看到 R 启动并显示版本信息
  - 如果 VS Code 询问是否安装 **sess** 包，点击 **Yes**（或 **Install bundled sess**）并等待安装完成。它让 VS Code 能够显示你的图形和变量
  - 如出现错误，仔细检查步骤 4 中的 settings.json 配置并重启 VS Code
- 逐个输入以下命令安装包：

```r
install.packages("languageserver")
install.packages("shiny")
```

- 等待安装完成（可能需要几分钟）
- 输入 `q()` 并按 Enter 退出 R
- R 会立即关闭（如果询问是否保存工作空间，输入 `n`）

仅在常规终端输入 `R` 不起作用，除非 R 在系统 PATH 中。R 扩展使用 `r.executablePath` 设置找到 R。

## 步骤 6：创建你的 R 项目

- 在计算机上创建新文件夹（如 `my-r-project`）
- VS Code 中，点击 **File > Open Folder** 选择你的新文件夹
- 点击顶部菜单的 **File > New File...**，然后从窗口顶部的列表中选择 **R Document**
- 点击 **File > Save** 将文件保存为 `analysis.R`

## 步骤 7：编写你的第一个 R 脚本

- 在 `analysis.R` 中输入以下代码：

```r
# Load the iris dataset
data(iris)

# View the first few rows
head(iris)

# Generate summary statistics
summary(iris)

hist(iris$Sepal.Length)
```

- 点击 **File > Save** 保存文件

## 步骤 8：交互式运行 R 代码

- 打开 `analysis.R`，选择一行代码，按 `Ctrl+Enter`（Windows/Linux）或 `Cmd+Enter`（Mac）运行
- 如果还没有打开 R 终端，窗口顶部会出现一个 **Run R code** 列表。选择 **Create R terminal**（不要选 **New R Interactive window**，它需要安装额外的软件）。R 终端会打开并运行你选中的那一行
- 输出会出现在终端。直方图会在 VS Code 内脚本旁边的绘图标签页中打开
- 也可以选择所有行，用相同方式运行

## 步骤 9：创建一个简单的 Shiny 应用

- 在项目文件夹创建新文件：点击 **File > New File...**，然后选择 **R Document**
- 保存为 `app.R`
- 输入以下代码：

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Interactive Histogram"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 5,
                  max = 50,
                  value = 30)
    ),

    mainPanel(
      plotOutput("histogram")
    )
  )
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    x <- faithful$waiting
    bins <- seq(min(x), max(x), length.out = input$bins + 1)

    hist(x, breaks = bins, col = "steelblue", border = "white",
         xlab = "Waiting time (minutes)",
         main = "Distribution of Waiting Times")
  })
}

shinyApp(ui = ui, server = server)
```

- 保存文件
- 注意编辑器右上角出现的 **▶** 按钮
- 点击下拉菜单选择 **Run Shiny App**
- 应用会在浏览器或 VS Code 面板打开
- 移动滑块，观察直方图即时更新

## 步骤 10：使用代码补全和悬停帮助

- 在 `analysis.R` 新行开始输入 `mea`
- 会出现带建议的下拉菜单——按 Enter 选择 `mean()`
- 鼠标悬停在你刚输入的单词 `mean` 上
- 会出现弹出窗口，显示函数文档和使用示例
- 尝试悬停在脚本中的 `summary` 或 `hist` 上查看文档
- 输入 `iris$`，观察 VS Code 建议列名（`Sepal.Length`、`Species` 等）

## 步骤 11：尝试更多功能

- **Markdown 集成**：创建 R Markdown 文件（`.Rmd`）以混合代码、输出和文本
- **代码格式化**：在 R 脚本中右键选择 **Format Document**（格式化文档）以自动格式化代码
- **调试**：安装 [R Debugger 扩展](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger)，并按照其设置页面的说明添加断点、逐步执行代码
- **Git 集成**：使用 VS Code 内置 Git 功能对 R 项目进行版本控制

## 下一步

- 创建包含单独 `ui.R` 和 `server.R` 文件的多文件 Shiny 应用
- 探索 [ggplot2](https://ggplot2.tidyverse.org/) 进行高级数据可视化
- 尝试 [tidyverse](https://www.tidyverse.org/) 包（`dplyr`、`tidyr`）进行数据操作
- 学习 R Markdown 或 [Quarto](https://quarto.org/) 创建嵌入 R 代码的报告
- 安装 [R Debugger 扩展](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger)进行高级调试

## 故障排除

- **VS Code 终端中"无法识别 R"**：VS Code 找不到 R。检查 settings.json（步骤 4）——验证 R 路径是否正确并指向 `R.exe`（Windows）或 R 二进制文件（Mac/Linux）。示例路径：
  - Windows：`C:\\Program Files\\R\\R-4.6.1\\bin\\R.exe`（调整版本号）
  - macOS（CRAN 安装程序，Intel 或 Apple Silicon）：`/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew：`/opt/homebrew/bin/R`
  - Linux：`/usr/bin/R`
  修复后，完全重启 VS Code。

- **settings 中的 R 版本不匹配**：如果更新了 R 但 VS Code 仍在使用旧版本，更新 settings.json 中 `r.executablePath` 这一行的版本号以匹配新 R 安装（参见步骤 3 找到当前安装路径）。

- **代码补全不起作用**：确保 languageserver 已成功安装（步骤 5）。安装后重启 VS Code。打开 R 文件后等 10-20 秒让语言服务器初始化。检查输出面板（View > Output > R Language Server）中的错误。

- **图形未显示**：图形会在 VS Code 内的标签页中打开。如果什么都没出现，确保你是通过 **R: Create R Terminal** 启动 R 的（而不是在普通终端中输入 `R`），然后重新运行 `hist()` 那一行。

- **Shiny 应用无法运行**：确保已安装 Shiny 扩展（步骤 2）、已安装 shiny 包（步骤 5）且文件名为 `app.R`。检查终端错误消息。仅当 VS Code 将文件识别为 Shiny 应用时，运行按钮才会出现。

## 工作流程总结

VS Code 提供 RStudio 的现代、轻量级替代方案，主要优势：

- **统一环境**：一个编辑器编写 R、Python、JavaScript 等代码
- **可定制**：仅安装需要的扩展，实现精简设置
- **集成终端**：并排运行 R、Git 和 shell 命令
- **Shiny 开发**：一键启动应用并自动重载，节省时间
- **版本控制**：内置 Git 集成，无需外部工具

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
