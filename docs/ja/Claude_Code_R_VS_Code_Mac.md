[ホーム](./)

# MacのVS CodeでRにClaude Codeを使う

VS CodeでRをセットアップし、手動でコードを書くことができるようになりました。次は、AIにコードの作成、改善、デバッグを手伝ってもらいながら、あなたは分析に集中したいと思います。Claude CodeをVS Code内に住むコーディングパートナーと考えてください - やりたいことを説明すれば、同じウィンドウ内でコードを書いたり改善したりしてくれます。

## 主要な概念

- **[Claude Code拡張機能](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - Claude AIアシスタントを直接エディタに組み込み、インラインでコード編集を行うVS Code拡張機能
- **チャットパネル** - VS Codeのサイドパネルで、Claudeとコードについて会話できます
- **インライン編集** - Claudeが提案するコード変更が、受け入れるか拒否できる差分としてファイル内に直接表示されます

## 必要なもの

- [VS CodeでR](./R_Coding_VS_Code_Guide)チュートリアルを完了していること - VS CodeでRが動作していること
- [MacにClaude Codeをインストール](./Install_Claude_Code_MacOS)チュートリアルを完了していること - Claude Code CLIがインストールされていること
- Claude Pro/Maxサブスクリプション または Anthropic APIキー
- 20〜30分

## ステップ1: VS Codeを開いてRプロジェクトを作成

- **Visual Studio Code**を開きます
- メニューバーの**File**をクリックし、**Open Folder**を選択します
- **Documents**フォルダに移動します
- ダイアログの下部にある**New Folder**をクリックします
- フォルダ名を`claude_r_test`にします
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
- 詳細な認証手順については、[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS)ガイド（ステップ5）を参照してください
- サインインすると、チャットパネルに「Ready to help」と表示されます

## ステップ3: 最初のRスクリプトを手動で作成

- メニューバーの**File > New File**をクリックします
- **Select a language**をクリックして`R`と入力し、**R**を選択します
- **File > Save**をクリックしてファイルを保存し、`iris_analysis.R`と名前を付けます
- 次のコードを入力します：

```r
data(iris)
str(iris)
summary(iris)
```

- **File > Save**をクリックしてファイルを保存します
- Rターミナルを開く：メニューバーの**View**をクリックし、**Command Palette**を選択、`R: Create R Terminal`と入力してEnterを押します
- コードを選択して`Cmd+Enter`を押して実行します
- ターミナルにデータセットの構造と要約統計が表示されます

## ステップ4: Claudeに散布図の追加を依頼

- 左サイドバーの**Claude**アイコンをクリックしてチャットパネルを開きます
- 下部のチャットボックスに次のように入力します：

```
Add code to iris_analysis.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```

- Enterを押して送信します
- Claudeがファイルを読み取り、変更を提案します - 追加する新しいコードを示す差分が表示されます
- **Accept**をクリックして変更を適用します
- ggplot2コードがファイルに表示されます
- ggplot2がインストールされていない場合は、Rターミナルで`install.packages("ggplot2")`を実行します

## ステップ5: 更新したコードを実行

- `iris_analysis.R`のすべてのコードを選択します
- `Cmd+Enter`を押します
- 別のグラフィックウィンドウに散布図が表示されます
- 種（setosa、versicolor、virginica）ごとに色分けされた点が表示されます

## ステップ6: Claudeにグラフの改善を依頼

- Claudeチャットパネルに次のように入力します：

```
Remove title. Change marker type by species. Change to the classic theme.
```

- Enterを押します
- Claudeが更新されたコード変更を表示します
- **Accept**をクリックします
- 更新されたコードを再度実行：すべてを選択して`Cmd+Enter`を押します
- グラフが種ごとに異なるマーカー形状、タイトルなし、classicテーマで表示されます

## ステップ7: ClaudeにPCA分析を依頼

- Claudeチャットパネルに次のように入力します：

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- Enterを押します
- ClaudeがPCAコードをスクリプトに追加します
- **Accept**をクリックします
- すべてのコードを実行：すべてを選択して`Cmd+Enter`を押します
- 種ごとに色分けされた、PC1とPC2に投影されたサンプルを示すPCAプロットが表示されます

## ステップ8: Claudeにレビューとコメント追加を依頼

- Claudeチャットパネルに次のように入力します：

```
Review the entire script for correctness. Add comments when necessary.
```

- Enterを押します
- Claudeがコードをレビューし、各セクションを説明するコメントを提案します
- **Accept**をクリックします
- スクリプトにデータ読み込み、可視化、PCA分析を説明する明確なコメントが追加されます

## 次のステップ

- ClaudeにR Markdownレポートの作成を依頼：「Create an R Markdown file for this analysis」
- Claudeを使ってエラーをデバッグ：「This code gives Error X, can you fix it?」
- 統計検定を要求：「Add a t-test comparing sepal length between setosa and versicolor」
- Claudeにコードの最適化を依頼：「Make this loop faster using vectorization」
- 馴染みのない関数について助けを得る：「Explain what dplyr::mutate does」

## トラブルシューティング

- **Claude拡張機能が表示されない** - インストール後にVS Codeを再起動してください。**View > Extensions**をクリックしてインストールされていることを確認してください。
- **「Cannot read R file」エラー** - ファイルが`.R`拡張子で保存されていることを確認してください。Claudeは保存されたファイルを読み取る必要があります。
- **認証失敗** - Claude Pro/Maxサブスクリプションがアクティブか、APIキーが有効であることを確認してください。認証のトラブルシューティングについては[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS)を参照してください。
- **ggplot2が見つからない** - Rターミナルでインストール：`install.packages("ggplot2")`。コードを実行する前にインストールが完了するまで待ってください。
- **コード変更が適用されない** - 差分の**Accept**をクリックしてください。それでもうまくいかない場合は、Claudeが提案したコードを手動でコピーしてみてください。

## ワークフローの概要

- **Claude Code拡張機能**はチャットパネルとインライン差分を備えたAIアシスタントをVS Codeに直接提供します
- **反復的な改善** - 基本的なコードから始め、Claudeに改善を依頼し、すぐにテストし、さらに改良します
- **コンテキスト認識** - ClaudeはRファイルを読み取り、プロジェクト構造を理解します
- **インライン編集** - 提案された変更は、別のチャット応答ではなく、実際のファイルに差分として表示されます
- **フローを維持** - ブラウザとエディタを切り替える必要はありません - すべてVS Code内で行われます

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
