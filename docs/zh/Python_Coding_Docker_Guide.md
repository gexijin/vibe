[首页](./)

# 通过 Docker 容器在 VS Code 中进行 Python 编程

您是否曾尝试与同事分享 Python 代码，却花费数小时调试"但在我的机器上可以运行"的问题？Docker 容器就像代码的集装箱——它们将您的 Python 环境、库和依赖项打包到一个密封的盒子中，在任何地方都能以相同方式运行。此外，您可以在 [Docker Hub](https://hub.docker.com/) 上访问数以万计的预构建镜像，软件开发者在那里发布即用型环境，省去手动安装软件的麻烦。本教程将向您展示如何使用 VS Code 和 Docker Desktop 在隔离、可重现的环境中运行 Python。

## 核心概念

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - 在您的计算机上运行容器的应用程序，管理隔离的环境
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code 功能，让您可以在 Docker 容器内编写代码，并获得完整的 IDE 支持
- **容器隔离** - 您的代码在一个独立的 Linux 环境中运行，只能看到您的项目文件夹，而不是整个计算机
- **[Python 官方镜像](https://hub.docker.com/_/python)** - 预构建的 Docker 镜像，已预装 Python 和基本工具

## 您需要准备的内容

- 完成 [在 VS Code 中进行 Python 编程](./Python_Coding_VS_Code_Guide)
- 20-25 分钟

## 步骤 1：安装 Docker Desktop

- 访问 [Docker Desktop 下载页面](https://www.docker.com/products/docker-desktop/)
- 点击 **Download for Windows**（或根据您的系统选择 Mac/Linux）
- 运行安装程序并按照安装向导操作
- 出现提示时，启用 WSL 2（Windows 用户）或接受默认设置
- 安装完成后，启动 Docker Desktop
- 等待 Docker 引擎启动（您将在左下角看到绿色状态指示器）

## 步骤 2：安装 Dev Containers 扩展

- 打开 VS Code
- 点击左侧边栏中的 **Extensions** 图标（或点击 **View > Extensions**）
- 在搜索框中输入 `dev containers`
- 找到 Microsoft 的 **Dev Containers**
- 点击 **Install**

## 步骤 3：创建 Python 项目文件夹

- 在您的计算机上创建一个名为 `python-docker-demo` 的新文件夹
- 在其中创建一个名为 `.devcontainer` 的子文件夹
- 在其中创建一个名为 `python` 的子文件夹
- 您的结构应如下所示：`python-docker-demo/.devcontainer/` 和 `python-docker-demo/python/`

## 步骤 4：创建 Dockerfile

- 在 VS Code 中，点击 **File > Open Folder**
- 导航到您刚创建的 `python-docker-demo` 文件夹
- 点击 **Select Folder**
- 在资源管理器侧边栏中，右键点击 `.devcontainer` 文件夹
- 点击 **New File**
- 将其命名为 `Dockerfile`
- 粘贴以下内容：

```dockerfile
# Choose the official Python slim image
FROM python:3.12-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Install Python packages for data science and web apps
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Streamlit port
EXPOSE 8501
```

- 点击 **File > Save**

## 步骤 5：创建 Dev Container 配置

- 在 `.devcontainer` 文件夹中，创建一个名为 `devcontainer.json` 的新文件
- 粘贴以下内容：

```json
{
  "name": "Python in Docker",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy"
      ]
    }
  },
  "forwardPorts": [8501],
  "postCreateCommand": "python3 --version"
}
```

- 点击 **File > Save**

## 步骤 6：创建 Python 数据分析脚本

- 在 `python` 文件夹中，创建一个名为 `iris_analysis.py` 的新文件
- 粘贴以下内容：

```python
# Simple data analysis using the iris dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Sepal Length')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Sepal Width')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Iris Sepal Measurements')
plt.legend()
plt.show()
```

- 点击 **File > Save**

## 步骤 7：创建 Streamlit Web 应用

- 在 `python` 文件夹中，创建一个名为 `app.py` 的新文件
- 粘贴以下内容：

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geyser Data")

# Slider for number of bins
bins = st.slider("Number of bins:", min_value=5, max_value=50, value=30)

# Generate sample data (simulating Old Faithful eruption durations)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Create histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Eruption Duration (minutes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram with {bins} bins')

st.pyplot(fig)
```

- 点击 **File > Save**

## 步骤 8：在容器中重新打开

- 点击 VS Code 左下角的绿色图标
- 从菜单中选择 **Reopen in Container**
- VS Code 将构建容器（第一次需要 5-10 分钟）
- 您将看到一个进度通知显示构建步骤
- 完成后，绿色图标将显示 **Dev Container: Python in Docker**

## 步骤 9：了解容器环境

现在您正在 Linux 容器内编写代码。让我们探索这意味着什么。

- 点击 **Terminal > New Terminal** 在容器内打开终端
- 检查您当前的位置：

```bash
pwd
```

您将看到 `/workspaces/python-docker-demo` - 这是容器内的项目文件夹。

- 列出文件：

```bash
ls
```

您将看到您创建的文件夹：`.devcontainer/`、`python/` 等。

- 尝试向上一级目录：

```bash
cd ..
ls
```

您只会看到 `python-docker-demo/` - 容器是隔离的。您无法访问计算机的其他文件夹、桌面或文档。这种隔离确保您的 Python 环境干净且可重现。

- 返回项目文件夹：

```bash
cd python-docker-demo
```

## 步骤 10：逐行运行 Python 代码

容器已预装 Python 和数据科学包。让我们运行分析脚本。

- 在 VS Code 资源管理器中，导航到 `python/iris_analysis.py`
- 点击打开文件
- 选择第一行：`import pandas as pd`
- 按 `Shift+Enter` 在交互式 Python 终端中运行
- 底部会打开一个 Python 终端
- 继续使用 `Shift+Enter` 逐行或逐块运行
- 当您运行 `print(df.head())` 时，您将在终端中看到前 5 行
- 当您运行 `print(df.describe())` 时，您将看到统计摘要
- 当您运行直方图代码时，将打开一个绘图窗口显示可视化

## 步骤 11：运行 Streamlit 应用

该项目包含一个演示 Streamlit 应用，用于创建交互式直方图。

- 在 VS Code 资源管理器中，导航到 `python/app.py`
- 点击打开文件
- 打开一个新终端（**Terminal > New Terminal**）
- 运行应用：

```bash
cd python
streamlit run app.py
```

- 应用将启动并显示一个 URL：`http://localhost:8501`
- 出现一个通知：**Open in Browser**
- 点击 **Open in Browser**
- Streamlit 应用在您的 Web 浏览器中打开
- 移动滑块以更改直方图的箱数 - 图表会实时更新

## 步骤 12：进行简单更改

让我们修改应用以了解开发是如何工作的。

- 保持应用运行
- 在 VS Code 中，编辑 `python/app.py`
- 找到第 6 行：`st.title("Old Faithful Geyser Data")`
- 将其更改为：

```python
st.title("My First Python Docker App")
```

- 点击 **File > Save**
- 返回浏览器
- 点击右上角的 **Always rerun**
- 标题现在显示您的自定义文本

## 步骤 13：了解 Dockerfile（可选）

- 在 VS Code 资源管理器中，导航到 `.devcontainer/Dockerfile`
- 点击打开文件
- 您将看到完整的配置

**关键部分：**

- `FROM python:3.12-slim` - 官方 Python 3.12 基础镜像（基于 Debian 的轻量级版本）
- `RUN apt-get install` - 用于构建 Python 包的 Linux 系统库
- `RUN pip install --no-cache-dir ...` - 永久安装 Python 包
- `RUN curl... && apt-get install -y nodejs` - 安装 Node.js，运行 Claude Code 所需
- `RUN npm install -g @anthropic-ai/claude-code` - 全局安装 Claude Code 以获得 AI 辅助
- `EXPOSE 8501` - 为 Streamlit 应用打开端口 8501

**您可以使用的其他 Python 镜像：**

- `python:3.12` - 完整的 Python 镜像，包含更多工具（体积更大）
- `python:3.12-slim` - 带有 Python 和 pip 的轻量级镜像（我们正在使用的）
- `python:3.12-alpine` - 基于 Alpine Linux 的最小镜像（体积最小）
- `jupyter/datascience-notebook` - 预配置的 Jupyter，包含数据科学库

更改基础镜像后，重新构建容器以应用更改。

## 步骤 14：在 Docker 镜像中安装 Python 包（可选）

通过终端中的 pip 安装的包（`pip install package`）是临时的，重新构建容器时会消失。要使包永久化，请将它们添加到 Dockerfile。

- 在 VS Code 资源管理器中，导航到 `.devcontainer/Dockerfile`
- 点击打开文件
- 找到第 9 行：`RUN pip install --no-cache-dir ...`
- 将 `scikit-learn` 添加到列表中：

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- 点击 **File > Save**
- 点击左下角的绿色图标
- 从菜单中选择 **Rebuild Container**
- VS Code 将使用新包重新构建容器（需要 2-5 分钟）
- 要验证，打开 Python 终端并输入：

```python
import sklearn
print(sklearn.__version__)
```

如果显示版本号且没有错误，则包已永久安装。

## 下一步

- **创建新的 Python 脚本** - 在 `python/` 文件夹中创建新的 `.py` 文件，使用内置数据集编写数据分析代码或加载您自己的 CSV 文件
- **安装 Python 包** - 通过编辑 Dockerfile（第 9 行）并重新构建容器来添加您需要的包
- **探索数据科学** - 尝试使用 pandas 进行数据处理，使用 matplotlib 或 seaborn 进行可视化
- **构建 Web 应用** - 使用 Streamlit 或 Flask 创建交互式仪表板

## 故障排除

- **Docker Desktop 未运行** - 打开 Docker Desktop 并等待绿色状态指示器出现，然后再重新打开容器
- **容器构建失败** - 检查您的互联网连接；第一次构建会下载镜像和包。点击 **Rebuild Container** 重试
- **端口 8501 已被占用** - 停止使用该端口的其他应用，或在 Dockerfile 和 `devcontainer.json` 中更改端口

## 工作流程概述

此设置为您提供了专业的 Python 开发环境：

- **VS Code** 提供代码编辑器，具有语法高亮、IntelliSense 和调试功能
- **Docker 容器** 运行隔离的 Linux 环境，包含 Python 和所有依赖项
- **Python 官方镜像**（`python:3.12-slim`）包括 Python、pip 和基本工具
- **Dev Container 配置**（`.devcontainer/`）自动安装 VS Code 扩展，用于 Python 调试和语言支持
- **端口转发** 允许您从浏览器访问在容器内运行的 Web 应用（Streamlit、Flask）

## 日常工作流程

设置完成后，这是您的日常例程：

1. **启动 Docker Desktop** - 打开应用并等待绿色状态指示器（Docker 必须运行）
2. **打开 VS Code** - 启动 VS Code 并打开您的项目文件夹
3. **在容器中重新打开** - 如果尚未在容器中，点击绿色图标（左下角）并选择 **Reopen in Container**
4. **编写和运行代码** - 编辑 `.py` 文件，使用 `Shift+Enter` 逐行运行，或使用 `streamlit run app.py` 运行应用
5. **保存您的工作** - 您的代码文件（`.py`、`.ipynb`）保存到您的计算机，并在会话之间持久存在
6. **提交并推送** - 使用 GitHub Desktop 提交更改并推送到存储库

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 7 日。
