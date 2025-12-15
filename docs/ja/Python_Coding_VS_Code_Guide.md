[ホーム](./ja/)

# VS CodeでPythonを書く

「Pythonを書きたいけど、どのエディターを使えばいい？」「PyCharmは少し重い…」そんなときはVS Code。軽快なのに高機能で、PythonやR、JavaScriptなどを1つのエディターで扱えます。このガイドでは、VS CodeにPython環境を整え、補完やデバッグ、Streamlitアプリまで動かすところを体験します。

## キーワード

- **[Python拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - Microsoftが提供するVS Code拡張機能。構文ハイライト、デバッグ、コード実行、Jupyterノートブックのサポートを提供します
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - 高速なインテリセンス、型チェック、自動インポートを実現する言語サーバー
- **[仮想環境](https://docs.python.org/ja/3/library/venv.html)** - システムのPythonに影響を与えずにプロジェクト固有のパッケージを管理するための独立したPython環境
- **[Streamlit](https://streamlit.io/)** - シンプルなPythonスクリプトでインタラクティブなWebアプリを作成できるPythonライブラリ

## 前提条件

- [VS Codeの基本](./VS_Code_Getting_Started.md)を完了していること
- Pythonとパッケージをダウンロードできるインターネット接続
- 作業時間：15〜20分

## ステップ1：Python本体をインストール

最新のパッケージとの互換性を確保するため、Python 3.8以降が必要です。

- **Windows**:
  - [python.org](https://www.python.org/downloads/)から最新のPythonをダウンロードします
  - インストーラーを実行します
  - **「Add python.exe to PATH」のチェックボックスにチェックを入れてから**、Install Nowをクリックします
  - インストール場所を確認します（通常は`C:\Users\YourName\AppData\Local\Programs\Python\Python312`）

- **macOS**:
  - [python.org](https://www.python.org/downloads/)からダウンロードしてインストーラーを実行します
  - またはHomebrewを使用：ターミナルを開いて`brew install python`と入力します
  - Homebrewのパス：`/opt/homebrew/bin/python3`（Apple Silicon）または`/usr/local/bin/python3`（Intel）

- **Linux**:
  - Pythonは通常プリインストールされています。`python3 --version`でバージョンを確認します
  - 必要に応じて、パッケージマネージャー経由でインストール：`sudo apt install python3 python3-pip python3-venv`（Ubuntu/Debian）

ターミナルを開いて`python3 --version`または`python --version`と入力してインストールを確認します。

## ステップ2：VS CodeにPython拡張機能をインストール

- VS Codeを開きます
- 左サイドバーの**拡張機能**アイコンをクリックします（または**表示 > 拡張機能**をクリック）
- `ms-python.python`を検索し、MicrosoftのPython拡張機能の**インストール**をクリックします
- PylanceはPython拡張機能と一緒に自動的にインストールされるはずです。されない場合は、`ms-python.vscode-pylance`を検索してインストールします

Python拡張機能には、デバッグ、インテリセンス、コードフォーマット、Jupyterノートブックのサポートが含まれています。

## ステップ3：Pythonプロジェクトを作成

- コンピューター上に新しいフォルダーを作成します（例：`my-python-project`）
- VS Codeで、**ファイル > フォルダーを開く**をクリックし、新しく作成したフォルダーを選択します
- トップメニューの**ファイル > 新しいファイル**をクリックします
- **ファイル > 保存**をクリックしてファイルを`analysis.py`として保存します

## ステップ4：Pythonインタープリタを選択

VS CodeがどのPythonインストールを使用するかを指定する必要があります。

- メニューバーの**表示**をクリックし、**コマンドパレット**を選択します
- `Python: Select Interpreter`と入力して選択します
- インストールしたPythonバージョンを選択します（例：`Python 3.12.x`など）
- 選択したインタープリタがVS Codeの右下隅に表示されます

Pythonインストールが表示されない場合は、**インタープリタパスを入力**をクリックし、Pythonがインストールされている場所に移動します。

## ステップ5：仮想環境を作成

仮想環境により、プロジェクトの依存関係を分離して管理できます。

- メニューバーの**表示**をクリックし、**コマンドパレット**を選択します
- `Python: Create Environment`と入力して選択します
- **Venv**（組み込みの仮想環境）を選択します
- リストからPythonインタープリタを選択します
- VS Codeが環境を作成するまで待ちます（`.venv`フォルダが表示されます）
- VS Codeがプロジェクト用にこの環境を自動的にアクティブ化します

環境がアクティブになると、ターミナルプロンプトに`(.venv)`が表示されます。

## ステップ6：必要なパッケージをインストール

- **表示 > ターミナル**をクリックして、VS Codeで新しいターミナルを開きます
- ターミナルに`(.venv)`が表示され、仮想環境がアクティブであることを確認します
- 次のコマンドを入力してパッケージをインストールします：

```bash
pip install pandas matplotlib streamlit
```

- インストールが完了するまで待ちます（1〜2分かかる場合があります）

`(.venv)`が表示されない場合、環境がアクティブになっていません。**表示 > コマンドパレット**をクリックし、`Python: Select Interpreter`を実行して、横に`('.venv': venv)`と表示されているインタープリタを選択します。

## ステップ7：最初のPythonスクリプトを書く

`analysis.py`に次のコードを入力します：

```python
import pandas as pd
import matplotlib.pyplot as plt

# irisデータセットを読み込む
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# 最初の数行を表示
print(iris.head())

# 要約統計を生成
print("\nSummary Statistics:")
print(iris.describe())

# ヒストグラムを作成
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- **ファイル > 保存**をクリックしてファイルを保存します

## ステップ8：Pythonコードをインタラクティブに実行

- `analysis.py`を開いた状態で、右上隅の**▶ Pythonファイルを実行**ボタンをクリックします
- またはエディター内で右クリックし、**ターミナルでPythonファイルを実行**を選択します
- 出力がターミナルパネルに表示されるのを確認します
- ヒストグラムを表示するウィンドウがポップアップします
- 特定の行を選択して`Shift+Enter`を押すと、その行だけをインタラクティブなPythonセッションで実行できます

## ステップ9：シンプルなStreamlitアプリを作成

- 新しいファイルを作成します：**ファイル > 新しいファイル**
- `app.py`として保存します
- 次のコードを入力します：

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# サイドバースライダー
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# データを読み込む
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# ヒストグラムを作成
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# Streamlitで表示
st.pyplot(fig)
```

- ファイルを保存します
- ターミナルを開いて次のコマンドを実行します：

```bash
streamlit run app.py
```

- アプリがブラウザで開きます（通常は`http://localhost:8501`）
- サイドバーのスライダーを動かすと、ヒストグラムが即座に更新されます
- アプリを停止するには、ターミナルで`Ctrl+C`を押します

## ステップ10：コード補完とインテリセンスを使用

- `analysis.py`で、新しい行に`iris.`と入力し始めます
- 利用可能なすべてのメソッドと属性を含むドロップダウンが表示されます
- `iris.gr`と入力すると、`groupby()`が提案されます
- 既存のコードの`pd.read_csv`にマウスを合わせます
- 関数のシグネチャ、パラメータ、ドキュメントを表示するポップアップが表示されます
- `import `と入力すると、VS Codeがパッケージ名を提案します
- 関数呼び出しを入力すると、インテリセンスがパラメータヒントを表示します

## ステップ11：デバッグを試す

- `analysis.py`で、8行目（`print(iris.head())`の行）の行番号の左側をクリックしてブレークポイントを設定します（赤い点が表示されます）
- メニューバーの**実行**をクリックし、**デバッグの開始**を選択します
- プロンプトが表示されたら**Pythonファイル**を選択します
- ブレークポイントでコードの実行が一時停止します
- デバッグツールバーを使用してコードをステップ実行し、変数を検査し、コールスタックを確認します
- **実行 > 続行**をクリックして実行を再開します

## 次のステップ

- データ操作と分析のために[pandas](https://pandas.pydata.org/)を探索する
- インタラクティブなデータサイエンスのためにVS Codeで[Jupyterノートブック](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)を学ぶ
- Web APIを構築するために[Flask](https://flask.palletsprojects.com/)や[FastAPI](https://fastapi.tiangolo.com/)を試す
- 自動コードフォーマットのために[Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)をインストールする
- テストを書いて実行するために[pytest](https://docs.pytest.org/)を使用する

## トラブルシューティング

- **ターミナルで「Pythonが認識されません」というエラー**：PythonがシステムのPATHに含まれていません。Windowsでは、Pythonを再インストールし、「Add python.exe to PATH」にチェックを入れます。Mac/Linuxでは、`python`の代わりに`python3`を使用します。修正後はVS Codeを再起動してください。

- **インタープリタが見つかりません**：VS Codeの右下隅にあるインタープリタセレクターをクリックするか、**表示 > コマンドパレット**をクリックして`Python: Select Interpreter`を実行します。Pythonインストールが表示されない場合は、**インタープリタパスを入力**を選択し、Pythonの実行可能ファイルを参照します。

- **仮想環境がアクティブにならない**：VS Codeはターミナルを開いたときに自動的にアクティブ化します。されない場合は手動でアクティブ化します：Windows：`.venv\Scripts\activate`、Mac/Linux：`source .venv/bin/activate`。ターミナルプロンプトに`(.venv)`が表示されることで確認できます。

- **インテリセンスが動作しない**：Pylanceがインストールされ、有効になっていることを確認します。右下隅に選択したインタープリタが表示されていることを確認します。Pylanceの初期化のために、ファイルを開いてから10〜20秒待ちます。問題が解決しない場合はVS Codeを再起動します。

- **pip installが失敗する**：仮想環境がアクティブになっていることを確認します（ターミナルに`(.venv)`が表示されているか確認）。Linuxでは、最初に`python3-venv`をインストールする必要がある場合があります。Windowsでは、ウイルス対策ソフトがpipをブロックしていないか確認します。

- **Streamlitアプリが実行されない**：streamlitが仮想環境にインストールされていることを確認します（`pip list | grep streamlit`）。エラーメッセージがないかターミナルを確認します。他のアプリがポート8501を使用していないことを確認します。

## ワークフローのまとめ

VS Codeは、次の利点を備えたPython開発のための現代的で軽量な環境を提供します：

- **統合環境**：Python、R、JavaScriptなど、1つのエディターで複数の言語をコーディング
- **強力なインテリセンス**：Pylanceによるスマートな補完、型チェック、自動インポート
- **統合デバッグ**：ブレークポイントの設定、変数の検査、コードのステップ実行
- **Jupyterサポート**：別のアプリケーションなしでVS Code内で直接ノートブックを実行
- **バージョン管理**：変更を追跡するための組み込みGit統合
- **拡張機能エコシステム**：テスト、フォーマット、リンティングなどのための数千の拡張機能

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
