[首页](./)

# 在 VS Code 中进行 Python 编程

你想编写 Python 代码，但不确定使用哪个编辑器，或者你正在寻找比 PyCharm 更轻量级的工具。可以把 VS Code 想象成一把瑞士军刀——它可以在一个轻量级编辑器中处理 Python、R、JavaScript 和许多其他语言。本教程将向你展示如何在 VS Code 中设置 Python，并获得代码补全、交互式调试甚至 Web 应用等智能功能。

## 核心概念

- **[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - 由 Microsoft 开发的 VS Code 扩展，提供语法高亮、调试、代码执行和 Jupyter notebook 支持
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - 语言服务器，为 Python 提供快速的 IntelliSense、类型检查和自动导入功能
- **[Virtual Environment](https://docs.python.org/3/library/venv.html)** - 隔离的 Python 环境，用于管理项目特定的包，而不影响系统 Python
- **[Streamlit](https://streamlit.io/)** - Python 库，用于通过简单的 Python 脚本创建交互式 Web 应用

## 你需要准备的

- 完成 [VS Code 基础](./VS_Code_Getting_Started)
- 可以联网以下载 Python 和包
- 15-20 分钟

## 步骤 1：安装 Python

你需要 Python 3.8 或更高版本，以获得与现代包的最佳兼容性。

- **Windows**：
  - 从 [python.org](https://www.python.org/downloads/) 下载最新版本的 Python
  - 运行安装程序
  - 在点击 Install Now 之前，**勾选"Add python.exe to PATH"复选框**
  - 记下安装位置（通常是 `C:\Users\YourName\AppData\Local\Programs\Python\Python312`）

- **macOS**：
  - 从 [python.org](https://www.python.org/downloads/) 下载并运行安装程序
  - 或使用 Homebrew：打开终端并输入 `brew install python`
  - Homebrew 路径：`/opt/homebrew/bin/python3`（Apple Silicon）或 `/usr/local/bin/python3`（Intel）

- **Linux**：
  - Python 通常已预装。使用 `python3 --version` 检查版本
  - 如有需要，通过包管理器安装：`sudo apt install python3 python3-pip python3-venv`（Ubuntu/Debian）

通过打开终端并输入 `python3 --version` 或 `python --version` 来验证安装。

## 步骤 2：在 VS Code 中安装 Python 扩展

- 打开 VS Code
- 点击左侧边栏中的 **Extensions** 图标（或点击 **View > Extensions**）
- 搜索 `ms-python.python` 并点击 Microsoft 开发的 Python 扩展上的 **Install**
- Pylance 应该会随 Python 扩展自动安装。如果没有，搜索 `ms-python.vscode-pylance` 并安装它

Python 扩展包括对调试、IntelliSense、代码格式化和 Jupyter notebook 的支持。

## 步骤 3：创建你的 Python 项目

- 在你的计算机上创建一个新文件夹（例如，`my-python-project`）
- 在 VS Code 中，点击 **File > Open Folder** 并选择你的新文件夹
- 点击顶部菜单中的 **File > New File**
- 通过点击 **File > Save** 将文件保存为 `analysis.py`

## 步骤 4：选择 Python 解释器

VS Code 需要知道使用哪个 Python 安装。

- 点击菜单栏中的 **View**，然后点击 **Command Palette**
- 输入 `Python: Select Interpreter` 并选择它
- 选择你安装的 Python 版本（例如，`Python 3.12.x` 或类似版本）
- 所选的解释器会出现在 VS Code 右下角

如果你没有看到你的 Python 安装，点击 **Enter interpreter path** 并导航到 Python 的安装位置。

## 步骤 5：创建虚拟环境

虚拟环境可以保持你的项目依赖项相互隔离。

- 点击菜单栏中的 **View**，然后点击 **Command Palette**
- 输入 `Python: Create Environment` 并选择它
- 选择 **Venv**（内置虚拟环境）
- 从列表中选择你的 Python 解释器
- 等待 VS Code 创建环境（你会看到一个 `.venv` 文件夹出现）
- VS Code 会自动为你的项目激活此环境

当环境激活时，你会在终端提示符中看到 `(.venv)`。

## 步骤 6：安装所需的包

- 通过点击 **View > Terminal** 在 VS Code 中打开一个新终端
- 终端应该显示 `(.venv)`，表示你的虚拟环境已激活
- 通过输入以下命令来安装包：

```bash
pip install pandas matplotlib streamlit
```

- 等待安装完成（可能需要 1-2 分钟）

如果 `(.venv)` 没有出现，说明环境未激活。点击 **View > Command Palette**，运行 `Python: Select Interpreter`，然后选择旁边带有 `('.venv': venv)` 的解释器。

## 步骤 7：编写你的第一个 Python 脚本

在 `analysis.py` 中输入以下代码：

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# View the first few rows
print(iris.head())

# Generate summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- 通过点击 **File > Save** 保存文件

## 步骤 8：交互式运行 Python 代码

- 打开 `analysis.py`，点击右上角的 **▶ Run Python File** 按钮
- 或在编辑器中右键点击并选择 **Run Python File in Terminal**
- 观察输出出现在终端面板中
- 一个直方图窗口会弹出显示你的图表
- 你还可以选择特定的行并按 `Shift+Enter` 在交互式 Python 会话中仅运行这些行

## 步骤 9：创建一个简单的 Streamlit 应用

- 创建一个新文件：**File > New File**
- 将其保存为 `app.py`
- 输入以下代码：

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# Sidebar slider
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# Load data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Create histogram
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# Display in Streamlit
st.pyplot(fig)
```

- 保存文件
- 打开终端并运行：

```bash
streamlit run app.py
```

- 该应用会在你的浏览器中打开（通常在 `http://localhost:8501`）
- 移动侧边栏中的滑块，观察直方图立即更新
- 在终端中按 `Ctrl+C` 停止应用

## 步骤 10：使用代码补全和 IntelliSense

- 在 `analysis.py` 中，在新行上开始输入 `iris.`
- 会出现一个下拉菜单，显示所有可用的方法和属性
- 输入 `iris.gr`，观察它建议 `groupby()`
- 将鼠标悬停在现有代码中的 `pd.read_csv` 上
- 一个弹出窗口会显示函数签名、参数和文档
- 尝试输入 `import `，观察 VS Code 建议包名称
- 当你输入函数调用时，IntelliSense 会显示参数提示

## 步骤 11：尝试调试

- 在 `analysis.py` 中，点击第 8 行（`print(iris.head())` 行）行号的左侧以设置断点（出现红点）
- 点击菜单栏中的 **Run**，然后点击 **Start Debugging**
- 在提示时选择 **Python File**
- 代码执行在断点处暂停
- 使用调试工具栏逐步执行代码、检查变量并查看调用堆栈
- 点击 **Run > Continue** 继续执行

## 下一步

- 探索 [pandas](https://pandas.pydata.org/) 进行数据处理和分析
- 在 VS Code 中学习 [Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) 进行交互式数据科学
- 尝试 [Flask](https://flask.palletsprojects.com/) 或 [FastAPI](https://fastapi.tiangolo.com/) 构建 Web API
- 安装 [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) 进行自动代码格式化
- 使用 [pytest](https://docs.pytest.org/) 编写和运行测试

## 故障排除

- **终端中显示"Python is not recognized"**：Python 不在你的系统 PATH 中。在 Windows 上，重新安装 Python 并勾选"Add python.exe to PATH"。在 Mac/Linux 上，使用 `python3` 而不是 `python`。修复后重启 VS Code。

- **找不到解释器**：点击 VS Code 右下角的解释器选择器，或点击 **View > Command Palette** 并运行 `Python: Select Interpreter`。如果你的 Python 安装没有出现，选择 **Enter interpreter path** 并浏览到你的 Python 可执行文件。

- **虚拟环境未激活**：当你打开终端时，VS Code 应该会自动激活它。如果没有，手动激活：Windows：`.venv\Scripts\activate`，Mac/Linux：`source .venv/bin/activate`。通过在终端提示符中看到 `(.venv)` 来验证。

- **IntelliSense 不工作**：确保 Pylance 已安装并启用。检查右下角是否显示你选择的解释器。打开文件后等待 10-20 秒让 Pylance 初始化。如果问题仍然存在，重启 VS Code。

- **pip install 失败**：确保你的虚拟环境已激活（查找终端中的 `(.venv)`）。在 Linux 上，你可能需要先安装 `python3-venv`。在 Windows 上，检查杀毒软件是否阻止了 pip。

- **Streamlit 应用无法运行**：确保 streamlit 已安装在你的虚拟环境中（`pip list | grep streamlit`）。检查终端中的错误消息。确保没有其他应用正在使用端口 8501。

## 工作流程总结

VS Code 为 Python 开发提供了一个现代、轻量级的环境，具有以下优势：

- **统一环境**：在一个编辑器中编写 Python、R、JavaScript 等多种语言的代码
- **强大的 IntelliSense**：通过 Pylance 实现智能补全、类型检查和自动导入
- **集成调试**：设置断点、检查变量并逐步执行代码
- **Jupyter 支持**：直接在 VS Code 中运行 notebook，无需单独的应用程序
- **版本控制**：内置 Git 集成用于跟踪更改
- **扩展生态系统**：数千个用于测试、格式化、代码检查等的扩展

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
