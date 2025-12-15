[ホーム](./)

# MacでRStudioとClaude Codeを使用する

MacでRコードを実行するためのRStudioと、AIによるコーディング支援のためのClaude Codeがあります。このチュートリアルでは、同じプロジェクトファイルで両方のツールを一緒に使用する方法を紹介します。Rプロジェクトを作成し、手動でコードを書き、その後ターミナルからClaude Codeを使用して可視化と分析で強化します。RStudioは開いたままでコードを実行してテストできます。

## 主要コンセプト

- **ターミナル**：Claude Codeが実行されるMacのコマンドラインインターフェース
- **共有ファイル**：RStudioとClaude Codeの両方がDocumentsフォルダ内の同じファイルを操作
- **ハイブリッドワークフロー**：RStudioがコードを実行し、Claude Codeがコードを書いて改善

## 必要なもの

- [MacでClaude Codeをインストール](./Install_Claude_Code_MacOS.md)ガイドを完了していること
- MacにインストールされたRStudio
- 20〜30分

---

## ステップ1：MacでRStudioを開く

- Dockの**Launchpad**をクリック（グリッド状のドットアイコン）
- 検索ボックスに`RStudio`と入力
- **RStudio**をクリックして開く
- RStudioウィンドウが複数のペインで開きます

## ステップ2：新規Rプロジェクトを作成

- RStudioで、上部メニューから**File**をクリック
- **New Project...**をクリック
- **New Directory**を選択
- **New Project**を選択
- **Directory name**に`test_claude`と入力
- "Create project as subdirectory of:"の横の**Browse**をクリック
- **Documents**フォルダに移動
- **Open**をクリック
- **Create Project**をクリック
- RStudioがプロジェクトを作成し、それに切り替えます

## ステップ3：新規Rスクリプトを作成

- RStudioで、**File > New File > R Script**をクリック
- 左上のペインに新しい空のスクリプトが開きます
- **File > Save**をクリック（または**Command (⌘) + S**を押す）
- ファイル名を`iris.R`と入力
- **Save**をクリック

## ステップ4：初期コードを手動で書く

`iris.R`ファイルに次のコードを入力します：

```r
data(iris)
str(iris)
summary(iris)
```

- **File > Save**をクリックして変更を保存（または**Command (⌘) + S**を押す）
- コードを実行するには：すべての行をハイライトし、スクリプトペインの右上にある**Run**ボタンをクリック
- Consoleペインにデータセットの構造と統計情報が表示されます

## ステップ5：ターミナルを開く

- **Finder**を開き、左サイドバーの**Applications**をクリック
- **Utilities**フォルダを開く
- **Terminal**をダブルクリック
- ターミナルウィンドウが開きます

## ステップ6：プロジェクトフォルダに移動

- ターミナルで、次のコマンドを入力：
  ```
  cd ~/Documents/test_claude
  ```
- 次のコマンドを入力して、正しい場所にいることを確認：
  ```
  ls
  ```
- `iris.R`と`test_claude.Rproj`が表示されるはずです

**ヒント：** 正確なパスがわからない場合は、Finderからターミナルにフォルダをドラッグアンドドロップすると、フルパスが自動的に表示されます！

## ステップ7：Claude Codeを起動

- ターミナルで、次のように入力：
  ```
  claude
  ```
- Claude Codeが起動し、ウェルカムメッセージが表示されます
- 初回セッションの場合、認証が必要な場合があります
- これでRプロジェクトのAI支援を使用する準備が整いました

## ステップ8：散布図をClaudeに依頼

Claude Codeが遅い、または反応しない場合は、初期化されるまで待ちます。その後、次のリクエストを入力：

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Codeが`iris.R`ファイルを読み込み、可視化コードを追加します
- 求められたら、適切なオプションを選択してiris.Rファイルの編集をClaudeに許可します
- Claudeが完了するまで待ちます（確認メッセージが表示されます）

## ステップ9：RStudioで新しいコードを実行

- RStudioに戻る（RStudioウィンドウをクリックするか、**Command (⌘) + Tab**を押す）
- ファイルが変更されたというプロンプトが表示される場合があります - **Yes**をクリックして再読み込み
- プロンプトが表示されない場合は、**File > Reopen with Encoding > UTF-8**をクリック
- すべてのコードをハイライトして**Run**をクリック
- 散布図が**Plots**ペイン（右下）に表示されます
- ggplot2に関するエラーが表示される場合は、Consoleペインに`install.packages("ggplot2")`と入力してインストール

## ステップ10：散布図を改良

- ターミナルに切り替え（**Command (⌘) + Tab**を押すか、ターミナルウィンドウをクリック）
- 次のリクエストを入力：
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## ステップ11：改良されたプロットを表示

- RStudioに切り替え
- プロンプトが表示されたらファイルを再読み込み
- 更新されたコードをハイライトして**Run**をクリック
- プロットがタイトルなし、種ごとに異なるマーカーの形、クラシックテーマを使用して表示されるようになりました


## ステップ12：PCAプロットをClaudeに依頼

- ターミナルに切り替え
- 次のリクエストを入力：
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## ステップ13：PCA分析を実行

- RStudioに切り替え
- プロンプトが表示されたらファイルを再読み込み
- すべてのコードをハイライトして**Run**をクリック
- PC1とPC2に投影されたサンプルを示すPCAプロットが表示され、種ごとに色分けされます

## ステップ14：スクリプトのレビューとコメントをClaudeに依頼

- ターミナルに切り替え
- 次のリクエストを入力：
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claudeがコードをレビューし、包括的なコメントを追加します

## ステップ15：R MarkdownをClaudeに依頼

- ターミナルに切り替え
- 次のリクエストを入力：
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claudeがファイル作成の許可を求めます
- Claudeがプロジェクトフォルダに新しい`.Rmd`ファイルを作成します


## ステップ16：R Markdownファイルをニット

- RStudioに切り替え
- **File > Open File...**をクリック
- `iris_report.Rmd`を選択して**Open**をクリック
- スクリプトペインの上部にある**Knit**ボタン（毛糸玉のアイコン）をクリック
- RStudioがHTMLレポートを生成します
- 説明文を含む完全な分析を示すレポートが新しいウィンドウで開きます
- HTMLファイルがプロジェクトフォルダに保存されます

## トラブルシューティング

- **RStudioがファイル変更を表示しない** - **File > Reopen with Encoding > UTF-8**をクリックして手動でファイルを再読み込みするか、ファイルを閉じて再度開きます。
- **"claude: command not found"** - [インストールガイド](./Install_Claude_Code_MacOS.md)を完了していることを確認してください。新しいターミナルウィンドウを開くか、ターミナルを完全に閉じて（**Command (⌘) + Q**）再度開きます。
- **プロットが表示されない** - ggplot2がインストールされていることを確認してください。必要に応じてRStudio Consoleで`install.packages("ggplot2")`を実行します。
- **"No such file or directory"** - ステップ6でパスを正しく入力したか確認してください。ドラッグアンドドロップのコツを試してください：Finderから`cd `（スペース付き）と入力した後にtest_claudeフォルダをターミナルにドラッグします。
- **Claude Codeの最初のリクエストが遅い** - Claudeが初期化されるまで30〜60秒待ちます。その後のリクエストは高速になります。

## Macのキーボードショートカット

アプリ間の切り替えに便利なショートカット：
- **Command (⌘) + Tab**：開いているアプリケーション間を素早く切り替え
- **Command (⌘) + `**（バッククォート）：同じアプリケーションのウィンドウ間を切り替え
- **Command (⌘) + Space**：Spotlight検索を開く（アプリを開くため）
- **Command (⌘) + Q**：アプリケーションを完全に終了

## 次のステップ

- Claudeに統計検定（t検定、ANOVA）を分析に追加するよう依頼する
- Claudeにこのコードの**Python版**を取得し、Quartoドキュメントを準備するよう依頼する
- Rスクリプトの反復タスクのための関数を作成するようClaudeに依頼する
- Rコードが実行されないときにエラーメッセージのデバッグにClaudeを使用する
- パフォーマンス向上のため、遅いRコードを最適化するようClaudeに依頼する

## ワークフローまとめ

このハイブリッドセットアップは両方の長所を組み合わせます：

- **RStudio（Mac）**：インタラクティブなRコンソール、即座のプロット表示、コード実行のための使い慣れたGUI
- **Claude Code（ターミナル）**：AIによるコード生成、レビュー、改善
- **共有ファイル**：Documentsフォルダ内の同じファイルを両方のツールが操作
- **反復的な改善**：手動でコードを書き始め、Claudeで強化し、RStudioでテストし、さらに改善
- **ドキュメント化**：Claudeが分析の包括的なレポートとコメントを生成

ワークフローはシンプルです：ターミナルのClaudeでコードを書いたり編集したりし、すぐにRStudioでテストして実行します。ファイルのコピーや手動同期は不要で、両方のアプリケーションがMac上の同じファイルにシームレスにアクセスします。

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2024年12月11日）
