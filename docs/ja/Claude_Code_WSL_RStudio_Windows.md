[ホーム](./)

# WindowsでWSL版Claude CodeとRStudioを併用する

WindowsではRStudioでRコードを実行し、WSLのUbuntu内にインストールしたClaude CodeでAI支援を受けられます。このチュートリアルでは、同じ`Documents`フォルダを共有しながら両者を切り替えて使う方法を解説します。RStudioでRプロジェクトを作成→基礎コードを手書き→UbuntuターミナルのClaudeに可視化やPCA解析を生成させ→R Markdownレポートまで仕上げる流れです。

## 主要コンセプト

- **WSL（Windows Subsystem for Linux）**：Windows上でUbuntuを動かし、Claude Codeを実行する環境
- **パスの変換**：`C:\Users\YourName\Documents` がWSLでは `/mnt/c/Users/YourName/Documents` になる
- **ハイブリッドワークフロー**：RStudio（Windows）でコードを実行し、Claude Code（WSL）でコードを生成・改良

## 必要なもの

- [WSL経由でClaude Codeをインストール](./Install_CLAUDE_Code_Win.md)済み
- Windows版RStudio
- 所要時間：20〜30分

---

## ステップ1：RStudioを起動

1. **Windowsスタートボタン**をクリック → `RStudio` と入力
2. 表示された **RStudio** を開くと、複数ペインのウィンドウが表示されます

## ステップ2：新規Rプロジェクトを作成

1. RStudio上部メニューから **File > New Project…**
2. **New Directory > New Project** を選択
3. **Directory name** に `test_claude` と入力
4. **Browse** で **Documents** フォルダを指定 → **Select Folder** → **Create Project**
5. RStudioがこの新規プロジェクトに切り替わります

## ステップ3：Rスクリプトを用意

1. **File > New File > R Script**
2. 空のスクリプトを **Ctrl + S**（または保存アイコン）で保存し、`iris.R` という名前を付けます

## ステップ4：初期コードを手書き

`iris.R` に以下を入力・保存します。
```r
data(iris)
str(iris)
summary(iris)
```
全行を選択して **Run** を押すと、Consoleに構造と統計量が出力されます。

## ステップ5：Ubuntuターミナルを開く

1. **Windowsスタートボタン** → `Ubuntu` と入力
2. オレンジ色の **Ubuntu** アプリを起動するとWSLのターミナルが開きます

## ステップ6：プロジェクトフォルダへ移動

```bash
cd /mnt/c/Users/YourUsername/Documents/test_claude
ls
```
`YourUsername` を自分のWindowsユーザー名に置き換えてください。`iris.R` と `test_claude.Rproj` が見えれば成功です。
> **ヒント**：`ls /mnt/c/Users/` でユーザーフォルダ一覧を確認できます。パスにスペースがある場合は `"Your Name"` のように引用符で囲みます。

## ステップ7：Claude Codeを起動

```bash
claude
```
初回は再ログインを求められる場合があります。完了すると指示待ち状態になります。

## ステップ8：散布図コードを追加

Claudeに以下を送信：
```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claudeが`iris.R`を読み込み、ggplot2を用いた散布図コードを追加します
- ファイル編集確認が出たら選択肢「2」を入力して許可します

## ステップ9：RStudioで実行

1. RStudioに戻り、変更の再読み込みを聞かれたら **Yes**
2. すべてのコードを選択して **Run**
3. **Plots**ペインに散布図が表示されます
4. ggplot2未インストールなら Console で `install.packages("ggplot2")`

## ステップ10：散布図を改良

Ubuntuターミナルで：
```
Remove title. Change marker type by species. Change to the classic theme.
```
再びRStudioでファイルを読み込み直して実行。タイトルなし、種ごとに異なるマーカーかつクラシックテーマのプロットが得られます。

## ステップ11：PCAプロットを追加

Ubuntuターミナルで：
```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```
RStudioに戻って実行すると、PC1×PC2に色分けされたPCA散布図が表示されます。

## ステップ12：スクリプトレビューとコメント

Ubuntuターミナルで：
```
Review the entire script for correctness. Add comments when necessary.
```
Claudeがコードをチェックし、要所にコメントを挿入します。

## ステップ13：R Markdownを生成

Ubuntuターミナルで：
```
Create a new R Markdown file for this analysis. Save as iris_report.Rmd
```
同意すると、`iris_report.Rmd` がプロジェクトフォルダに作成されます。

## ステップ14：RStudioでKnit

1. **File > Open File…** から `iris_report.Rmd` を開く
2. エディタ上部の **Knit**（毛糸玉アイコン）をクリック
3. HTMLレポートが生成され、新しいウィンドウで表示されます（ファイルもフォルダに保存）

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

## 次のステップ例

- t検定やANOVAなどの統計解析を追加するようClaudeに依頼
- Python版スクリプトとQuartoレポートを生成してもらう
- 繰り返し処理を関数化するコードを作成してもらう
- エラーをClaudeに貼り付けてデバッグを依頼
- 重い処理を高速化する最適化案を提案してもらう

## ワークフローまとめ

- **RStudio（Windows）**：GUIでRコードを実行し、プロットやKnitを即座に確認
- **Claude Code（WSL）**：AIによるコード生成・レビュー・コメント付け
- **共有ファイル**：`/mnt/c/...` を介して両環境が同じフォルダを操作
- **反復的な改良**：手動コード → Claudeの提案 → RStudioでテスト → さらに改良
- **ドキュメント化**：ClaudeにR Markdownやレポート作成も依頼可能

UbuntuターミナルでClaudeにコードを書かせ、そのままRStudioで実行して確認——この往復だけで高度な分析とレポート作成まで完結します。
