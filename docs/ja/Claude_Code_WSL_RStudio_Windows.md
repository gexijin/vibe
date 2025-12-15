[ホーム](./)

# WindowsでWSL版Claude CodeとRStudioを併用する

WindowsではRStudioでRコードを実行し、WSLのUbuntu内にインストールしたClaude CodeでAI支援を受けられます。このチュートリアルでは、同じ`Documents`フォルダを共有しながら両者を切り替えて使う方法を解説します。RStudioでRプロジェクトを作成→基礎コードを手書き→UbuntuターミナルのClaudeに可視化やPCA解析を生成させ→R Markdownレポートまで仕上げる流れです。

## 主要コンセプト

- **WSL（Windows Subsystem for Linux）**：Windows上でUbuntuを動かし、Claude Codeを実行する環境
- **パスの変換**：`C:\Users\YourName\Documents` がWSLでは `/mnt/c/Users/YourName/Documents` になる
- **ハイブリッドワークフロー**：RStudio（Windows）でコードを実行し、Claude Code（WSL）でコードを生成・改良

## 必要なもの

- [WSL経由でClaude Codeをインストール](./Install_CLAUDE_Code_Win)済み
- Windows版RStudio
- 所要時間：20〜30分

---

## ステップ1：WindowsでRStudioを開く

- **Windowsスタートボタン**をクリック
- 検索ボックスに`RStudio`と入力
- **RStudio**をクリックして開く
- RStudioウィンドウが複数のペインとともに開きます

## ステップ2：新規Rプロジェクトを作成

- RStudioで、上部メニューから**File**をクリック
- **New Project...**をクリック
- **New Directory**を選択
- **New Project**を選択
- **Directory name**に：`test_claude`と入力
- "Create project as subdirectory of:"の横にある**Browse**をクリック
- **Documents**フォルダに移動
- **Select Folder**をクリック
- **Create Project**をクリック
- RStudioがプロジェクトを作成し、そのプロジェクトに切り替わります

## ステップ3：新規Rスクリプトを作成

- RStudioで**File > New File > R Script**をクリック
- 左上のペインに新しい空のスクリプトが開きます
- **File > Save**をクリック（または保存アイコン）
- ファイル名：`iris.R`と入力
- **Save**をクリック

## ステップ4：初期コードを手書き

`iris.R` ファイルに以下のコードを入力します：

```r
data(iris)
str(iris)
summary(iris)
```

- **File > Save**をクリックして変更を保存
- コードを実行するには：すべての行を選択し、**Run**ボタン（スクリプトペインの右上）をクリック
- Consoleペインに、データセットの構造と統計量が表示されるはずです

## ステップ5：Ubuntuターミナルを開く

- **Windowsスタートボタン**をクリック
- 検索ボックスに`Ubuntu`と入力
- **Ubuntu**（オレンジ色の円形アイコン）をクリック
- Ubuntuターミナルが開きます

## ステップ6：プロジェクトフォルダへ移動

- Ubuntuターミナルで以下のコマンドを入力します（`YourUsername`を実際のWindowsユーザー名に置き換えてください）：
  ```
  cd /mnt/c/Users/YourUsername/Documents/test_claude
  ```
- ユーザー名を確認するには：`ls /mnt/c/Users/`と入力してフォルダ名を確認できます
- 正しい場所にいることを確認するため、以下を入力：
  ```
  ls
  ```
- `iris.R`と`test_claude.Rproj`が表示されるはずです

## ステップ7：Claude Codeを起動

- Ubuntuターミナルで以下を入力：
  ```
  claude
  ```
- Claude Codeが起動し、ウェルカムメッセージが表示されます
- 再度サインインが必要な場合があります - 認証手順については[WSL経由でClaude Codeをインストール](./Install_CLAUDE_Code_Win)ガイドを参照してください
- これでRプロジェクトに対してAI支援を使用する準備ができました

## ステップ8：散布図コードを追加

Claude Codeの起動が遅い場合は、初期化が完了するまで待ちましょう。その後、以下のリクエストを入力します：

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Codeが`iris.R`ファイルを読み込み、可視化コードを追加します
- 確認を求められたら、適切な選択肢を選んでiris.Rファイルの編集を許可します
- Claudeが完了するまで待ちます（完了メッセージが表示されます）


## ステップ9：RStudioで新しいコードを実行

- RStudioウィンドウに戻ります（RStudioウィンドウをクリック）
- ファイルが変更されたというプロンプトが表示される場合があります - **Yes**をクリックして再読み込みします
- プロンプトが表示されない場合は、**File > Reopen with Encoding > UTF-8**をクリックします
- すべてのコードを選択して**Run**をクリック
- **Plots**ペイン（右下）に散布図が表示されます
- ggplot2に関するエラーが出た場合は、Consoleペインで`install.packages("ggplot2")`と入力してインストールします

## ステップ10：散布図を改良

- Ubuntuターミナルに切り替えます
- 以下のリクエストを入力：
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## ステップ11：改良されたプロットを表示

- RStudioに切り替えます
- プロンプトが表示されたらファイルを再読み込みします
- 更新されたコードを選択して**Run**をクリック
- プロットがタイトルなしで表示され、種ごとに異なるマーカー形状、クラシックテーマが適用されているはずです


## ステップ12：PCAプロットを追加

- Ubuntuターミナルに切り替えます
- 以下のリクエストを入力：
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## ステップ13：PCA解析を実行

- RStudioに切り替えます
- プロンプトが表示されたらファイルを再読み込みします
- すべてのコードを選択して**Run**をクリック
- PC1とPC2に投影されたサンプルを示すPCAプロットが表示され、種ごとに色分けされます

## ステップ14：レビューとコメント追加をClaudeに依頼

- Ubuntuターミナルに切り替えます
- 以下のリクエストを入力：
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claudeがコードをレビューし、包括的なコメントを追加します

## ステップ15：R Markdownを作成

- Ubuntuターミナルに切り替えます
- 以下のリクエストを入力：
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claudeがこのファイルの作成許可を求めます
- Claudeがプロジェクトフォルダに新しい`.Rmd`ファイルを作成します


## ステップ16：R Markdownファイルをニット

- RStudioに切り替えます
- **File > Open File...**をクリック
- `iris_report.Rmd`を選択して**Open**をクリック
- スクリプトペインの上部にある**Knit**ボタン（毛糸玉アイコン）をクリック
- RStudioがHTMLレポートを生成します
- 完全な解析とナラティブテキストを含むレポートが新しいウィンドウで開きます
- HTMLファイルはプロジェクトフォルダに保存されます

---

## トラブルシューティング

| 症状 | 対処 |
| --- | --- |
| WSLで `Permission denied` | `C:/` ではなく `/mnt/c/` パスを使用。ユーザー名の綴りを確認 |
| RStudioが更新を検知しない | **File > Reopen with Encoding > UTF-8** で手動リロード |
| `claude: command not found` | インストールガイドを再確認。Ubuntuターミナルを開き直す |
| プロットが表示されない | RStudio Consoleで `install.packages("ggplot2")` を実行 |
| `cannot change working directory` | Windowsのユーザー名にスペースがある場合、`cd "/mnt/c/Users/Your Name/Documents/..."` のように引用符で囲む |
| 初回リクエストが遅い | 30〜60秒待てば初期化され、その後は高速化します |

## 次のステップ

- 統計検定（t検定、ANOVA）を解析に追加するようClaudeに依頼
- このコードの**Python版**を取得し、Quartoドキュメントを準備するようClaudeに依頼
- Rスクリプトの繰り返し作業のための関数を作成するようClaudeに依頼
- Rコードが実行されないときのエラーメッセージのデバッグにClaudeを使用
- より良いパフォーマンスのために遅いRコードを最適化するようClaudeに依頼

## ワークフローまとめ

このハイブリッドセットアップは、両方の長所を組み合わせています：

- **RStudio（Windows）** - インタラクティブなRコンソール、即座のプロット表示、コード実行のための使い慣れたGUI
- **Claude Code（WSL）** - AI駆動のコード生成、レビュー、改善
- **共有ファイル** - WSLの`/mnt/c/`マウントポイントを通じて、両ツールが同じファイルを操作
- **反復的な改善** - 手動コードから始め、Claudeで強化、RStudioでテスト、そしてさらに改善
- **ドキュメント化** - Claudeが解析のための包括的なレポートとコメントを生成できます

ワークフローはシンプルです：UbuntuターミナルでClaudeを使ってコードを書くか編集し、すぐにRStudioでテストして実行します。ファイルのコピーや手動同期は不要です—WSLとWindowsは同じファイルをシームレスに共有します。

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
