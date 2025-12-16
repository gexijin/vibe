[首页](./)

# 在 VS Code 中进行 Python 编程

想编写 Python 代码,却不知道用哪个编辑器?或者想找比 PyCharm 更轻量的工具?把 VS Code 想象成瑞士军刀——一个轻量级编辑器就能处理 Python、R、JavaScript 等多种语言。本教程将教你在 VS Code 中设置 Python,获得代码补全、交互式调试,甚至创建 Web 应用。

## 核心概念

- **[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - Microsoft 开发的 VS Code 扩展,提供语法高亮、调试、代码执行和 Jupyter notebook 支持
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - 语言服务器,为 Python 提供快速 IntelliSense、类型检查和自动导入
- **[Virtual Environment](https://docs.python.org/3/library/venv.html)** - 隔离的 Python 环境,管理项目专属包,不影响系统 Python
- **[Streamlit](https://streamlit.io/)** - Python 库,通过简单脚本创建交互式 Web 应用

## 你需要准备的

- 完成 [VS Code 基础](./VS_Code_Getting_Started)
- 可以联网以下载 Python 和包
- 15-20 分钟

## 步骤 1:安装 Python

需要 Python 3.8 或更高版本,以确保与现代包兼容。

- **Windows**:
  - 从 [python.org](https://www.python.org/downloads/) 下载最新版 Python
  - 运行安装程序
  - 点击 Install Now 前,**勾选"Add python.exe to PATH"**
  - 记住安装位置(通常是 `C:\Users\YourName\AppData\Local\Programs\Python\Python312`)

- **macOS**:
  - 从 [python.org](https://www.python.org/downloads/) 下载并运行安装程序
  - 或使用 Homebrew:打开终端,输入 `brew install python`
  - Homebrew 路径:`/opt/homebrew/bin/python3`(Apple Silicon)或 `/usr/local/bin/python3`(Intel)

- **Linux**:
  - Python 通常已预装,用 `python3 --version` 检查版本
  - 如需安装,使用包管理器:`sudo apt install python3 python3-pip python3-venv`(Ubuntu/Debian)

打开终端,输入 `python3 --version` 或 `python --version` 验证安装。

## 步骤 2:在 VS Code 中安装 Python 扩展

- 打开 VS Code
- 点击左侧边栏的 **Extensions** 图标(或 **View > Extensions**)
- 搜索 `ms-python.python`,点击 Microsoft 的 Python 扩展上的 **Install**
- Pylance 会自动安装。如果没有,搜索 `ms-python.vscode-pylance` 并安装

Python 扩展包含调试、IntelliSense、代码格式化和 Jupyter notebook 支持。

## 步骤 3:创建你的 Python 项目

- 在计算机上创建新文件夹(如 `my-python-project`)
- VS Code 中,点击 **File > Open Folder** 选择该文件夹
- 点击 **File > New File** 创建新文件
- 点击 **File > Save** 保存为 `analysis.py`

## 步骤 4:选择 Python 解释器

VS Code 需要知道使用哪个 Python。

- 点击 **View > Command Palette**
- 输入 `Python: Select Interpreter` 并选择
- 选择已安装的 Python 版本(如 `Python 3.12.x`)
- 所选解释器会显示在 VS Code 右下角

如果没看到你的 Python 安装,点击 **Enter interpreter path** 导航到安装位置。

## 步骤 5:创建虚拟环境

虚拟环境让项目依赖相互隔离。

- 点击 **View > Command Palette**
- 输入 `Python: Create Environment` 并选择
- 选择 **Venv**(内置虚拟环境)
- 从列表选择 Python 解释器
- 等待 VS Code 创建环境(会出现 `.venv` 文件夹)
- VS Code 自动激活该环境

环境激活后,终端提示符会显示 `(.venv)`。

## 步骤 6:安装所需的包

- 点击 **View > Terminal** 打开终端
- 终端应显示 `(.venv)`,表示虚拟环境已激活
- 输入以下命令安装包:

```bash
pip install pandas matplotlib streamlit
```

- 等待安装完成(约 1-2 分钟)

如果 `(.venv)` 未出现,说明环境未激活。运行 **View > Command Palette**,执行 `Python: Select Interpreter`,选择带 `('.venv': venv)` 的解释器。

## 步骤 7:编写你的第一个 Python 脚本

在 `analysis.py` 中输入以下代码:

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

- 点击 **File > Save** 保存文件

## 步骤 8:交互式运行 Python 代码

- 打开 `analysis.py`,点击右上角 **▶ Run Python File** 按钮
- 或右键选择 **Run Python File in Terminal**
- 输出会显示在终端面板
- 直方图会在新窗口弹出
- 也可以选择特定行,按 `Shift+Enter` 在交互式会话中运行

## 步骤 9:创建一个简单的 Streamlit 应用

- 创建一个新文件:**File > New File**
- 将其保存为 `app.py`
- 输入以下代码:

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
- 打开终端并运行:

```bash
streamlit run app.py
```

- 该应用会在你的浏览器中打开(通常在 `http://localhost:8501`)
- 移动侧边栏中的滑块,观察直方图立即更新
- 在终端中按 `Ctrl+C` 停止应用

## 步骤 10:使用代码补全和 IntelliSense

- 在 `analysis.py` 新行输入 `iris.`
- 下拉菜单会显示所有可用方法和属性
- 输入 `iris.gr`,会建议 `groupby()`
- 鼠标悬停在 `pd.read_csv` 上
- 弹出窗口显示函数签名、参数和文档
- 输入 `import `,VS Code 会建议包名称
- 输入函数调用时,IntelliSense 显示参数提示

## 步骤 11:尝试调试

- 在 `analysis.py`,点击第 8 行(`print(iris.head())`)行号左侧设置断点(显示红点)
- 点击 **Run > Start Debugging**
- 提示时选择 **Python File**
- 代码在断点处暂停
- 用调试工具栏逐步执行代码、检查变量、查看调用堆栈
- 点击 **Run > Continue** 继续执行

## 下一步

- 学习 [pandas](https://pandas.pydata.org/) 进行数据处理和分析
- 在 VS Code 中使用 [Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) 做数据科学
- 用 [Flask](https://flask.palletsprojects.com/) 或 [FastAPI](https://fastapi.tiangolo.com/) 构建 Web API
- 安装 [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) 自动格式化代码
- 用 [pytest](https://docs.pytest.org/) 编写和运行测试

## 故障排除

- **终端显示"Python is not recognized"**:Python 不在系统 PATH 中。Windows 上重新安装 Python,勾选"Add python.exe to PATH"。Mac/Linux 上使用 `python3` 而非 `python`。修复后重启 VS Code。

- **找不到解释器**:点击 VS Code 右下角的解释器选择器,或运行 **View > Command Palette** 中的 `Python: Select Interpreter`。如果 Python 未出现,选择 **Enter interpreter path** 浏览到 Python 可执行文件。

- **虚拟环境未激活**:打开终端时 VS Code 应自动激活。如果没有,手动激活:Windows: `.venv\Scripts\activate`,Mac/Linux: `source .venv/bin/activate`。验证终端提示符显示 `(.venv)`。

- **IntelliSense 不工作**:确保 Pylance 已安装并启用。检查右下角是否显示所选解释器。打开文件后等 10-20 秒让 Pylance 初始化。问题仍存在则重启 VS Code。

- **pip install 失败**:确保虚拟环境已激活(终端显示 `(.venv)`)。Linux 上可能需先安装 `python3-venv`。Windows 上检查杀毒软件是否阻止 pip。

- **Streamlit 应用无法运行**:确保虚拟环境中已安装 streamlit(`pip list | grep streamlit`)。检查终端错误消息。确保端口 8501 未被占用。

## 工作流程总结

VS Code 为 Python 开发提供现代、轻量级的环境:

- **统一环境**:一个编辑器处理 Python、R、JavaScript 等多种语言
- **强大 IntelliSense**:Pylance 提供智能补全、类型检查和自动导入
- **集成调试**:设置断点、检查变量、逐步执行代码
- **Jupyter 支持**:直接在 VS Code 运行 notebook,无需单独应用
- **版本控制**:内置 Git 集成跟踪更改
- **丰富扩展**:数千个测试、格式化、代码检查扩展

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
