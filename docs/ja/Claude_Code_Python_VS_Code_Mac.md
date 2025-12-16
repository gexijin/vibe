[ホーム](./)

# MacのVS CodeでPythonにClaude Codeを使う

VS CodeでPythonをセットアップし、手動でコードを書くことができるようになりました。次は、AIにコードの作成、改善、デバッグを手伝ってもらいながら、あなたは分析に集中したいと思います。Claude CodeをVS Code内に住むコーディングパートナーと考えてください - やりたいことを説明すれば、同じウィンドウ内でコードを書いたり改善したりしてくれます。

## 主要な概念

- **[Claude Code拡張機能](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - Claude AIアシスタントを直接エディタに組み込み、インラインでコード編集を行うVS Code拡張機能
- **チャットパネル** - VS Codeのサイドパネルで、Claudeとコードについて会話できます
- **インライン編集** - Claudeが提案するコード変更が、受け入れるか拒否できる差分としてファイル内に直接表示されます

## 必要なもの

- [VS CodeでPython](./Python_Coding_VS_Code_Guide.md)チュートリアルを完了していること - VS CodeでPythonが動作していること
- [MacにClaude Codeをインストール](./Install_Claude_Code_MacOS.md)チュートリアルを完了していること - Claude Code CLIがインストールされていること
- Claude Pro/Maxサブスクリプション または Anthropic APIキー
- 20〜30分

## ステップ1: VS Codeを開いてPythonプロジェクトを作成

- **Visual Studio Code**を開きます
- メニューバーの**File**をクリックし、**Open Folder**を選択します
- **Documents**フォルダに移動します
- ダイアログの下部にある**New Folder**をクリックします
- フォルダ名を`claude_python_test`にします
- **Open**をクリックして新しいフォルダを開きます
- 「Do you trust the authors?」と表示されたら、**Yes, I trust the authors**をクリックします

## ステップ2: Claude Code拡張機能をインストールしてサインイン

- 左サイドバーの**Extensions**アイコン（4つの正方形のアイコン）をクリックします
- 検索ボックスに`Claude Code`と入力します
- Anthropicの**Claude Code**を見つけて**Install**をクリックします
- インストール後、左サイドバーにClaudeアイコン（キラキラマーク）が表示されます
- Claudeアイコンをクリックしてチャットパネルを開きます
- チャットパネルの**Sign in to Claude Code**をクリックします
- 認証方法を選択します：
  - **Claude Pro/Maxユーザー**: **Sign in with Claude.ai**をクリックし、ブラウザで認証してコードをVS Codeにコピーします
  - **APIキーユーザー**: **Use API Key**をクリックしてAnthropic APIキーを貼り付けます
- 詳細な認証手順については、[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS.md)ガイド（ステップ5）を参照してください
- サインインすると、チャットパネルに「Ready to help」と表示されます

## ステップ3: 最初のPythonスクリプトを手動で作成

- メニューバーの**File > New File**をクリックします
- **Select a language**をクリックして`Python`と入力し、**Python**を選択します
- **File > Save**をクリックしてファイルを保存し、`iris_analysis.py`と名前を付けます
- 次のコードを入力します：

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

- **File > Save**をクリックしてファイルを保存します
- Pythonターミナルを開く：メニューバーの**View**をクリックし、**Terminal**を選択します
- ターミナルで次を実行：`python iris_analysis.py`
- ターミナルにデータセットの構造と要約統計が表示されます

## ステップ4: Claudeに散布図の追加を依頼

- 左サイドバーの**Claude**アイコンをクリックしてチャットパネルを開きます
- 下部のチャットボックスに次のように入力します：

```
iris_analysis.pyに、sepal lengthとwidthの散布図を作成するコードを追加してください。種ごとに色分けして、seabornを使用してください。
```

- Enterを押して送信します
- Claudeがファイルを読み取り、変更を提案します - 追加する新しいコードを示す差分が表示されます
- **Accept**をクリックして変更を適用します
- seaborn/matplotlibコードがファイルに表示されます
- 必要なパッケージがインストールされていない場合は、ターミナルで実行します：
  ```
  pip install seaborn matplotlib scikit-learn pandas
  ```

## ステップ5: 更新したコードを実行

- ターミナルで次を実行：`python iris_analysis.py`
- 散布図ウィンドウが表示されます
- 種（setosa、versicolor、virginica）ごとに色分けされた点が表示されます
- プロットウィンドウを閉じて続けます

## ステップ6: Claudeにグラフの改善を依頼

- Claudeチャットパネルに次のように入力します：

```
タイトルを削除してください。種ごとにマーカーの形状を変更してください。whitegridスタイルに変更してください。
```

- Enterを押します
- Claudeが更新されたコード変更を表示します
- **Accept**をクリックします
- 更新されたコードを再度実行：ターミナルで`python iris_analysis.py`
- グラフが種ごとに異なるマーカー形状、タイトルなし、whitegridスタイルで表示されます
- プロットウィンドウを閉じて続けます

## ステップ7: ClaudeにPCA分析を依頼

- Claudeチャットパネルに次のように入力します：

```
数値変数に対してPCAを実行し、最初の2つの主成分を使用してサンプルをプロットするコードを追加してください。
```

- Enterを押します
- ClaudeがPCAコードをスクリプトに追加します
- **Accept**をクリックします
- コードを実行：ターミナルで`python iris_analysis.py`
- 種ごとに色分けされた、PC1とPC2に投影されたサンプルを示すPCAプロットが表示されます
- 完了したらプロットウィンドウを閉じます

## ステップ8: Claudeにレビューとコメント追加を依頼

- Claudeチャットパネルに次のように入力します：

```
スクリプト全体の正確性をレビューしてください。必要に応じてコメントを追加してください。
```

- Enterを押します
- Claudeがコードをレビューし、各セクションを説明するコメントを提案します
- **Accept**をクリックします
- スクリプトにデータ読み込み、可視化、PCA分析を説明する明確なコメントが追加されます

## 次のステップ

- ClaudeにJupyter notebookの作成を依頼：「これをJupyter notebookに変換してください」
- Claudeを使ってエラーをデバッグ：「このコードがエラーXを出します。修正してもらえますか？」
- 統計検定を要求：「setosaとversicolorの間でsepal lengthを比較するt検定を追加してください」
- Claudeにコードの最適化を依頼：「numpyのベクトル化を使ってこのコードをより効率的にしてください」
- 馴染みのない関数について助けを得る：「pandas.groupbyが何をするのか説明してください」

## トラブルシューティング

- **Claude拡張機能が表示されない** - インストール後にVS Codeを再起動してください。**View > Extensions**をクリックしてインストールされていることを確認してください。
- **「Cannot read Python file」エラー** - ファイルが`.py`拡張子で保存されていることを確認してください。Claudeは保存されたファイルを読み取る必要があります。
- **認証失敗** - Claude Pro/Maxサブスクリプションがアクティブか、APIキーが有効であることを確認してください。認証のトラブルシューティングについては[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS.md)を参照してください。
- **パッケージが見つからないエラー** - ターミナルで必要なパッケージをインストール：`pip install seaborn matplotlib scikit-learn pandas`。コードを実行する前にインストールが完了するまで待ってください。
- **コード変更が適用されない** - 差分の**Accept**をクリックしてください。それでもうまくいかない場合は、Claudeが提案したコードを手動でコピーしてみてください。
- **プロットが表示されない** - ディスプレイがあることを確認してください。一部のシステムでは、最後に`plt.show()`を追加するか、Jupyterで`%matplotlib inline`を使用する必要がある場合があります。

## ワークフローの概要

- **Claude Code拡張機能**はチャットパネルとインライン差分を備えたAIアシスタントをVS Codeに直接提供します
- **反復的な改善** - 基本的なコードから始め、Claudeに改善を依頼し、すぐにテストし、さらに改良します
- **コンテキスト認識** - ClaudeはPythonファイルを読み取り、プロジェクト構造を理解します
- **インライン編集** - 提案された変更は、別のチャット応答ではなく、実際のファイルに差分として表示されます
- **フローを維持** - ブラウザとエディタを切り替える必要はありません - すべてVS Code内で行われます

---

作成者: [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 2025年12月11日
