[ホーム](./)

# DockerコンテナによるVS CodeでのPythonコーディング

Pythonコードを同僚と共有しようとして、「でも私のマシンでは動くよ」問題のデバッグに何時間も費やしたことはありませんか？Dockerコンテナはコード用の輸送コンテナのようなものです。Python環境、ライブラリ、依存関係を、どこでも同じように動作する密閉されたボックスにパッケージ化します。さらに、[Docker Hub](https://hub.docker.com/)には何万もの事前構築イメージがあり、ソフトウェア開発者がすぐに使える環境を公開しているので、手動インストールの苦痛をスキップできます。このチュートリアルでは、VS CodeとDocker Desktopを使って、隔離された再現可能な環境でPythonを実行する方法を紹介します。

## 主要な概念

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - コンピュータ上でコンテナを実行し、隔離された環境を管理するアプリケーション
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - Dockerコンテナ内で完全なIDEサポートでコーディングできるVS Code機能
- **コンテナ隔離** - コードは別のLinux環境で実行され、プロジェクトフォルダのみが見え、コンピュータ全体は見えません
- **[Python公式イメージ](https://hub.docker.com/_/python)** - Pythonと必須ツールがプリインストールされた事前構築Dockerイメージ

## 必要なもの

- [VS CodeでPythonコーディング](./Python_Coding_VS_Code_Guide)を完了
- 20〜25分

## ステップ1：Docker Desktopをインストール

- [Docker Desktopダウンロードページ](https://www.docker.com/products/docker-desktop/)にアクセス
- **Download for Windows**をクリック（またはシステムに基づいてMac/Linux）
- インストーラーを実行し、インストールウィザードに従う
- プロンプトが表示されたら、WSL 2を有効にする（Windowsユーザー）またはデフォルト設定を受け入れる
- インストール後、Docker Desktopを起動
- Dockerエンジンが起動するまで待つ（左下に緑色のステータスインジケーターが表示されます）

## ステップ2：Dev Containers拡張機能をインストール

- VS Codeを開く
- 左サイドバーの**拡張機能**アイコンをクリック（または**表示 > 拡張機能**をクリック）
- 検索ボックスに`dev containers`と入力
- Microsoftの**Dev Containers**を見つける
- **インストール**をクリック

## ステップ3：Pythonプロジェクトフォルダを作成

- コンピュータに`python-docker-demo`という新しいフォルダを作成
- その中に`.devcontainer`というサブフォルダを作成
- `python-docker-demo`の中に`python`というサブフォルダを作成
- 構造は次のようになります：`python-docker-demo/.devcontainer/` と `python-docker-demo/python/`

## ステップ4：Dockerfileを作成

- VS Codeで**ファイル > フォルダーを開く**をクリック
- 作成した`python-docker-demo`フォルダに移動
- **フォルダーの選択**をクリック
- エクスプローラーサイドバーで`.devcontainer`フォルダを右クリック
- **新しいファイル**をクリック
- `Dockerfile`と名前を付ける
- 以下の内容を貼り付け：

```dockerfile
# Python slim公式イメージを選択
FROM python:3.12-slim

# 1. システム依存関係をインストール
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. データサイエンスとWebアプリ用のPythonパッケージをインストール
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter

# 3. NodeSourceからNode.js LTSをインストール
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Claude Codeをグローバルにインストール
RUN npm install -g @anthropic-ai/claude-code

# 5. Streamlitポートを公開
EXPOSE 8501
```

- **ファイル > 保存**をクリック

## ステップ5：Dev Container設定を作成

- `.devcontainer`フォルダに`devcontainer.json`という新しいファイルを作成
- 以下の内容を貼り付け：

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

- **ファイル > 保存**をクリック

## ステップ6：Pythonデータ分析スクリプトを作成

- `python`フォルダに`iris_analysis.py`という新しいファイルを作成
- 以下の内容を貼り付け：

```python
# irisデータセットを使ったシンプルなデータ分析
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# irisデータセットを読み込み
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# 最初の数行を表示
print(df.head())

# 要約統計
print("\n要約統計:")
print(df.describe())

# ヒストグラムを作成
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='がく片の長さ')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='がく片の幅')
plt.xlabel('測定値 (cm)')
plt.ylabel('頻度')
plt.title('アイリスのがく片測定値')
plt.legend()
plt.show()
```

- **ファイル > 保存**をクリック

## ステップ7：Streamlit Webアプリを作成

- `python`フォルダに`app.py`という新しいファイルを作成
- 以下の内容を貼り付け：

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("オールドフェイスフル間欠泉データ")

# ビン数のスライダー
bins = st.slider("ビンの数:", min_value=5, max_value=50, value=30)

# サンプルデータを生成（オールドフェイスフル噴出時間のシミュレーション）
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# ヒストグラムを作成
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('噴出時間 (分)')
ax.set_ylabel('頻度')
ax.set_title(f'{bins}ビンのヒストグラム')

st.pyplot(fig)
```

- **ファイル > 保存**をクリック

## ステップ8：コンテナ内で再度開く

- VS Code左下隅の緑色のアイコンをクリック
- メニューから**Reopen in Container**を選択
- VS Codeがコンテナをビルドします（初回は5〜10分かかります）
- ビルドステップを示す進行通知が表示されます
- 完了すると、緑色のアイコンに**Dev Container: Python in Docker**と表示されます

## ステップ9：コンテナ環境を理解する

これでLinuxコンテナ内でコーディングしています。これが何を意味するのか探ってみましょう。

- **ターミナル > 新しいターミナル**をクリックしてコンテナ内のターミナルを開く
- 現在の場所を確認します：

```bash
pwd
```

`/workspaces/python-docker-demo`と表示されます - これはコンテナ内のプロジェクトフォルダです。

- ファイルを一覧表示：

```bash
ls
```

作成したフォルダが表示されます：`.devcontainer/`、`python/` など。

- 一つ上のディレクトリに移動してみます：

```bash
cd ..
ls
```

`python-docker-demo/`だけが表示されます - コンテナは隔離されています。コンピュータの他のフォルダ、デスクトップ、ドキュメントにはアクセスできません。この隔離により、Python環境がクリーンで再現可能になります。

- プロジェクトフォルダに戻ります：

```bash
cd python-docker-demo
```

## ステップ10：Pythonコードを行ごとに実行

コンテナにはデータサイエンスパッケージ付きのPythonがプリインストールされています。分析スクリプトを実行しましょう。

- VS Codeエクスプローラーで`python/iris_analysis.py`に移動
- クリックしてファイルを開く
- 最初の行を選択：`import pandas as pd`
- `Shift+Enter`を押して対話型Pythonターミナルで実行
- 下部にPythonターミナルが開きます
- `Shift+Enter`で各行またはブロックを1つずつ実行し続ける
- `print(df.head())`を実行すると、ターミナルに最初の5行が表示されます
- `print(df.describe())`を実行すると、統計的な要約が表示されます
- ヒストグラムコードを実行すると、可視化を表示するプロットウィンドウが開きます

## ステップ11：Streamlitアプリを実行

プロジェクトには対話型ヒストグラムを作成するデモStreamlitアプリが含まれています。

- VS Codeエクスプローラーで`python/app.py`に移動
- クリックしてファイルを開く
- 新しいターミナルを開きます（**ターミナル > 新しいターミナル**）
- アプリを実行します：

```bash
cd python
streamlit run app.py
```

- アプリが起動し、URL: `http://localhost:8501`が表示されます
- 通知が表示されます：**Open in Browser**
- **Open in Browser**をクリック
- StreamlitアプリがWebブラウザで開きます
- スライダーを動かしてヒストグラムのビン数を変更 - チャートがリアルタイムで更新されます

## ステップ12：簡単な変更を加える

アプリを変更して開発がどのように機能するか見てみましょう。

- アプリを実行したまま
- VS Codeで`python/app.py`を編集
- 6行目を見つけます：`st.title("オールドフェイスフル間欠泉データ")`
- 以下に変更：

```python
st.title("私の初めてのPython Dockerアプリ")
```

- **ファイル > 保存**をクリック
- ブラウザに戻る
- 右上隅の**Always rerun**をクリック
- タイトルがカスタムテキストとして表示されます

## ステップ13：Dockerfileを理解する（オプション）

- VS Codeエクスプローラーで`.devcontainer/Dockerfile`に移動
- クリックしてファイルを開く
- 完全な設定が表示されます

**重要な部分：**

- `FROM python:3.12-slim` - Python 3.12公式ベースイメージ（軽量なDebian系）
- `RUN apt-get install` - Pythonパッケージをビルドするためのシステムライブラリ
- `RUN pip install --no-cache-dir ...` - Pythonパッケージを永続的にインストール
- `RUN curl... && apt-get install -y nodejs` - Claude Codeの実行に必要なNode.jsをインストール
- `RUN npm install -g @anthropic-ai/claude-code` - AIアシスタンス用にClaude Codeをグローバルにインストール
- `EXPOSE 8501` - Streamlitアプリ用にポート8501を公開

**使用できる他のPythonイメージ：**

- `python:3.12` - より多くのツールを含む完全なPythonイメージ（サイズが大きい）
- `python:3.12-slim` - Pythonとpipを含む軽量イメージ（使用中）
- `python:3.12-alpine` - 最小のAlpine Linuxベースイメージ（最小サイズ）
- `jupyter/datascience-notebook` - データサイエンスライブラリが事前設定されたJupyter

ベースイメージを変更した後は、コンテナを再ビルドして変更を適用します。

## ステップ14：DockerイメージにPythonパッケージをインストール（オプション）

ターミナルでpipを使ってインストールしたパッケージ（`pip install package`）は一時的で、コンテナを再ビルドすると消えます。パッケージを永続的にするには、Dockerfileに追加します。

- VS Codeエクスプローラーで`.devcontainer/Dockerfile`に移動
- クリックしてファイルを開く
- 9行目を見つけます：`RUN pip install --no-cache-dir ...`
- リストに`scikit-learn`を追加します：

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- **ファイル > 保存**をクリック
- 左下隅の緑色のアイコンをクリック
- メニューから**Rebuild Container**を選択
- VS Codeが新しいパッケージでコンテナを再ビルドします（2〜5分かかります）
- 確認するには、Pythonターミナルを開いて入力します：

```python
import sklearn
print(sklearn.__version__)
```

エラーなくバージョンが表示されれば、パッケージは永続的にインストールされています。

## 次のステップ

- **新しいPythonスクリプトを作成** - `python/`フォルダに新しい`.py`ファイルを作成し、組み込みデータセットを使用するか、独自のCSVファイルを読み込んでデータ分析コードを書く
- **Pythonパッケージをインストール** - Dockerfile（9行目）を編集してコンテナを再ビルドして、必要なパッケージを追加
- **データサイエンスを探索** - pandasでデータ操作、matplotlibやseabornで可視化を試す
- **Webアプリを構築** - StreamlitやFlaskで対話型ダッシュボードを作成

## トラブルシューティング

- **Docker Desktopが実行されていない** - Docker Desktopを開き、コンテナを再度開く前に緑色のステータスインジケーターを待つ
- **コンテナビルドが失敗** - インターネット接続を確認。最初のビルドはイメージとパッケージをダウンロードします。**Rebuild Container**をクリックして再試行
- **ポート8501がすでに使用中** - そのポートを使用している他のアプリを停止するか、Dockerfileと`devcontainer.json`でポートを変更

## ワークフロー概要

このセットアップにより、プロフェッショナルなPython開発環境が得られます：

- **VS Code**がシンタックスハイライト、IntelliSense、デバッグ機能を持つコードエディターを提供
- **Dockerコンテナ**がPythonとすべての依存関係を持つ隔離されたLinux環境を実行
- **Python公式イメージ**（`python:3.12-slim`）がPython、pip、必須ツールを含む
- **Dev Container設定**（`.devcontainer/`）がPythonデバッグと言語サポート用のVS Code拡張機能を自動的にインストール
- **ポートフォワーディング**によりコンテナ内で実行されているWebアプリ（Streamlit、Flask）にブラウザからアクセス可能

## 日常のワークフロー

すべてがセットアップされたら、日常のルーティンは以下の通りです：

1. **Docker Desktopを起動** - アプリを開いて緑色のステータスインジケーターを待つ（Dockerが実行されている必要があります）
2. **VS Codeを開く** - VS Codeを起動してプロジェクトフォルダを開く
3. **コンテナで再度開く** - まだコンテナ内でない場合、緑色のアイコン（左下）をクリックして**Reopen in Container**を選択
4. **コードを書いて実行** - `.py`ファイルを編集し、`Shift+Enter`で行ごとに実行、または`streamlit run app.py`でアプリを実行
5. **作業を保存** - コードファイル（`.py`、`.ipynb`）はコンピュータに保存され、セッション間で永続
6. **コミットしてプッシュ** - GitHub Desktopを使用して変更をコミットし、リポジトリにプッシュ

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2025年12月7日に作成。
