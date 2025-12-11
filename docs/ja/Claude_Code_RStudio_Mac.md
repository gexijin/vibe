[ホーム](./)

# MacでRStudioとClaude Codeを併用する

MacではRStudioでRコードを実行し、Claude CodeでAIによるコーディング支援を受けられます。このチュートリアルでは、同じプロジェクトフォルダを共有しながら両方のツールを切り替えて使う方法を紹介します。まずRStudioでシンプルな分析を書き、続いてターミナルのClaude Codeに可視化やPCAまで生成させ、最後にR Markdownレポートまで仕上げます。

## 主要コンセプト

- **ターミナル**：Claude Codeを実行するMacのコマンドライン
- **共有ファイル**：`~/Documents` 内の同じファイルをRStudioとClaude Codeが同時に扱う
- **ハイブリッドワークフロー**：RStudioでコードを実行・確認し、Claudeにコード生成や改善を依頼

## 必要なもの

- [MacでClaude Codeをインストール](./Install_Claude_Code_MacOS.md)済み
- RStudio（Mac版）
- 所要時間：20〜30分

---

## ステップ1：RStudioを起動

1. Dockの**Launchpad**をクリックし、`RStudio`と入力
2. 表示された **RStudio** を開くと、複数ペインのウィンドウが表示されます

## ステップ2：新規Rプロジェクトを作成

1. 上部メニューから **File > New Project…**
2. **New Directory > New Project** を選択
3. **Directory name** に `test_claude` と入力
4. **Browse** で **Documents** を指定 → **Create Project**
5. RStudioが新規プロジェクトに切り替わります

## ステップ3：Rスクリプトを用意

1. **File > New File > R Script**
2. 空のスクリプトが開いたら **Command (⌘) + S** で保存し、`iris.R` という名前を付けます

## ステップ4：初期コードを手書き

`iris.R` に以下を入力し、保存します。
```r
data(iris)
str(iris)
summary(iris)
```
スクリプト全体を選択して **Run** を押すと、Consoleに構造と要約が表示されます。

## ステップ5：ターミナルを開く

- **Command (⌘) + Space** → `Terminal` と入力 → **Terminal** を開きます（黒いアイコン）

## ステップ6：プロジェクトフォルダへ移動

```bash
cd ~/Documents/test_claude
ls
```
`iris.R` と `test_claude.Rproj` が見えればOKです。
> **ヒント**：Finderからフォルダをターミナルへドラッグ＆ドロップするとフルパスが自動入力されます。

## ステップ7：Claude Codeを起動

```bash
claude
```
初回は認証が求められる場合があります。完了すると指示待ちの状態になります。

## ステップ8：散布図コードを追加

Claudeに次を送信：
```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claudeが`iris.R`を読み込み、ggplot2による散布図コードを追加します
- ファイル編集の許可を求められたら承認してください

## ステップ9：RStudioで実行

1. RStudioに戻り、変更を読み込むか聞かれたら **Yes**
2. 全コードを選んで **Run**
3. **Plots**ペインに散布図が表示されます
4. ggplot2が未インストールなら Console で `install.packages("ggplot2")`

## ステップ10：散布図を改良依頼

ターミナルで：
```
Remove title. Change marker type by species. Change to the classic theme.
```
再びRStudioでファイルを読み込み直して実行すると、タイトルなし・種ごとに形の違うクラシックテーマのプロットになります。

## ステップ11：PCAプロットを追加

ターミナルで：
```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```
RStudioで再度実行すると、PC1×PC2の散布図が生成され、種ごとに色分けされます。

## ステップ12：スクリプトのレビューとコメント

ターミナルで：
```
Review the entire script for correctness. Add comments when necessary.
```
Claudeがコードを点検し、要所にコメントを追加します。

## ステップ13：R Markdownを生成

ターミナルで：
```
Create a new R Markdown file for this analysis. Save as iris_report.Rmd
```
同意すると、`iris_report.Rmd` がプロジェクトフォルダに作成されます。

## ステップ14：RStudioでKnit

1. **File > Open File…** で `iris_report.Rmd` を開く
2. エディタ上部の **Knit**（毛糸玉アイコン）をクリック
3. HTMLレポートが生成され、新しいウィンドウで表示されます（ファイルもフォルダに保存）

---

## トラブルシューティング

| 症状 | 解決策 |
| --- | --- |
| RStudioがファイル更新を拾わない | **File > Reopen with Encoding > UTF-8** またはファイルを閉じて開き直す |
| `claude: command not found` | インストールガイドを再確認。ターミナルを **Command (⌘) + Q** で終了→再起動 |
| プロットが出ない | Consoleで `install.packages("ggplot2")` を実行してから再度Run |
| `No such file or directory` | `cd ~/Documents/test_claude` が正しいか確認。ドラッグ＆ドロップでパスを入力すると確実 |
| 初回リクエストが遅い | 30〜60秒待つと初期化が完了し、以降は高速になります |

## Macで役立つショートカット

- **Command (⌘) + Tab**：アプリ間を素早く切り替え
- **Command (⌘) + `** ：同一アプリ内のウィンドウ切り替え
- **Command (⌘) + Space**：Spotlightでアプリ検索
- **Command (⌘) + Q**：アプリを完全終了

## 次のステップ例

- Claudeに統計検定（t検定、ANOVA）や回帰分析を追記させる
- Python版スクリプトとQuartoレポートを生成させる
- 反復処理を関数化するよう依頼
- エラーメッセージをClaudeに貼り付けてデバッグを依頼
- 遅いコードを高速化してもらう

## ワークフローまとめ

- **RStudio**：コード実行・可視化・KnitなどGUI操作が得意
- **Claude Code**：コード生成、改善、コメント付与、レポート作成もAIに任せられる
- **共有フォルダ**：どちらのアプリから編集しても即座に反映され、手動同期は不要

ターミナルでClaudeに書かせたコードを、すぐRStudioで実行して確認する——この往復だけで高度な分析やレポート作成まで完了します。

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2024年12月11日）
