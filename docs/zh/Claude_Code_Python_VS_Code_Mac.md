[首页](./)

# 在 Mac 的 VS Code 中使用 Claude Code 进行 Python 开发

你已在 VS Code 中设置好 Python 环境，可以手动编写代码。现在你想让 AI 帮助编写、改进和调试 Python 代码，以便专注于分析工作。可以把 Claude Code 想象成住在 VS Code 里的编程伙伴——你描述需求，它编写或改进代码，而你始终在同一窗口中工作。

## 核心概念

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - VS Code 扩展，将 Claude AI 助手直接集成到编辑器，提供内联代码编辑
- **Chat Panel（聊天面板）** - VS Code 侧边面板，可在此与 Claude 讨论代码
- **Inline Edits（内联编辑）** - Claude 建议的代码更改以差异对比形式直接显示在文件中，可接受或拒绝

## 准备工作

- 完成 [Python in VS Code](./Python_Coding_VS_Code_Guide) 教程 - Python 应该已在 VS Code 中正常工作
- 完成 [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) 教程 - Claude Code CLI 应该已安装
- Claude Pro/Max 订阅或 Anthropic API 密钥
- 20-30 分钟

## 步骤 1：打开 VS Code 并创建 Python 项目

- 打开 **Visual Studio Code**
- 点击菜单栏中的 **File**，然后点击 **Open Folder**
- 导航到你的 **Documents** 文件夹
- 点击对话框底部的 **New Folder**
- 将文件夹命名为 `claude_python_test`
- 点击 **Open** 打开新文件夹
- 如果提示"Do you trust the authors?"，点击 **Yes, I trust the authors**

## 步骤 2：安装并登录 Claude Code Extension

- 点击左侧边栏的 **Extensions** 图标（四个方块）
- 在搜索框中输入 `Claude Code`
- 找到 Anthropic 的 **Claude Code**，点击 **Install**
- 安装完成后，左侧边栏出现 Claude 图标（闪光图标）
- 点击 Claude 图标打开聊天面板
- 点击聊天面板中的 **Sign in to Claude Code**
- 选择身份验证方式：
  - **Claude Pro/Max 用户**：点击 **Sign in with Claude.ai**，在浏览器授权，将代码复制回 VS Code
  - **API 密钥用户**：点击 **Use API Key**，粘贴 Anthropic API 密钥
- 详细身份验证步骤请参阅 [Installing Claude Code on Mac](./Install_Claude_Code_MacOS) 指南（步骤 5）
- 登录成功后，聊天面板中显示"Ready to help"

## 步骤 3：手动创建初始 Python 脚本

- 点击菜单栏的 **File > New File**
- 点击 **Select a language**，输入 `Python`，选择 **Python**
- 点击 **File > Save** 保存文件，命名为 `iris_analysis.py`
- 输入以下代码：

```python
from sklearn import datasets
import pandas as pd

# Load iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

# Display structure
print(iris_df.info())
print("\nSummary statistics:")
print(iris_df.describe())
```

- 点击 **File > Save** 保存文件
- 打开 Python Terminal：点击 **View > Terminal**
- 在 Terminal 中运行：`python iris_analysis.py`
- 你应在 Terminal 中看到数据集结构和汇总统计信息

## 步骤 4：让 Claude 添加散点图

- 点击左侧边栏的 **Claude** 图标打开聊天面板
- 在底部聊天框中输入：

```
Add code to iris_analysis.py to create a scatter plot of sepal length vs. width, colored by species. Use seaborn.
```

- 按 Enter 发送
- Claude 读取文件并提出更改建议，你会看到显示新增代码的差异对比
- 点击 **Accept** 应用更改
- seaborn/matplotlib 代码出现在文件中
- 如未安装所需的包，在 Terminal 中运行：
  ```
  pip install seaborn matplotlib scikit-learn pandas
  ```

## 步骤 5：运行更新后的代码

- 在 Terminal 中运行：`python iris_analysis.py`
- 出现散点图窗口
- 你应看到按物种（setosa、versicolor、virginica）着色的点
- 关闭图表窗口继续

## 步骤 6：让 Claude 优化图表

- 在 Claude 聊天面板中，输入：

```
Remove title. Change marker type by species. Change to the whitegrid style.
```

- 按 Enter
- Claude 显示更新后的代码更改
- 点击 **Accept**
- 再次运行：在 Terminal 中输入 `python iris_analysis.py`
- 图表现在显示每个物种使用不同标记形状，无标题，使用 whitegrid 样式
- 关闭图表窗口继续

## 步骤 7：让 Claude 进行 PCA 分析

- 在 Claude 聊天面板中，输入：

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- 按 Enter
- Claude 向脚本添加 PCA 代码
- 点击 **Accept**
- 运行代码：在 Terminal 中输入 `python iris_analysis.py`
- 出现 PCA 图表，显示投影到 PC1 和 PC2 上的样本，按物种着色
- 完成后关闭图表窗口

## 步骤 8：让 Claude 审查并添加注释

- 在 Claude 聊天面板中，输入：

```
Review the entire script for correctness. Add comments when necessary.
```

- 按 Enter
- Claude 审查代码并建议添加解释各部分的注释
- 点击 **Accept**
- 脚本现在有清晰注释，解释数据加载、可视化和 PCA 分析

## 下一步

- 让 Claude 创建 Jupyter notebook："Convert this to a Jupyter notebook"
- 用 Claude 调试错误："This code gives Error X, can you fix it?"
- 请求统计检验："Add a t-test comparing sepal length between setosa and versicolor"
- 让 Claude 优化代码："Make this code more efficient using numpy vectorization"
- 获取函数帮助："Explain what pandas.groupby does"

## 故障排除

- **Claude Extension 未显示** - 安装后重启 VS Code，点击 **View > Extensions** 验证是否已安装
- **"Cannot read Python file" 错误** - 确保保存的文件使用 `.py` 扩展名，Claude 需读取已保存的文件
- **身份验证失败** - 验证 Claude Pro/Max 订阅是否有效或 API 密钥是否正确，故障排除参阅 [Installing Claude Code on Mac](./Install_Claude_Code_MacOS)
- **找不到包错误** - 在 Terminal 中安装所需包：`pip install seaborn matplotlib scikit-learn pandas`，等待安装完成后再运行代码
- **代码更改未应用** - 确保在差异对比上点击 **Accept**，如不起作用可手动复制 Claude 建议的代码
- **图表未显示** - 确保有显示器，某些系统可能需要在末尾添加 `plt.show()` 或在 Jupyter 中使用 `%matplotlib inline`

## 工作流程总结

- **Claude Code Extension** 直接在 VS Code 中提供 AI 助手，包含聊天面板和内联差异对比
- **迭代优化** - 从基础代码开始，让 Claude 增强，立即测试，进一步优化
- **上下文感知** - Claude 读取 Python 文件并理解项目结构
- **内联编辑** - 建议的更改以差异对比形式显示在实际文件中，非单独聊天响应
- **保持流畅** - 无需在浏览器和编辑器间切换，所有操作都在 VS Code 中完成

---

由 [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 创建于 2025 年 12 月 11 日。
