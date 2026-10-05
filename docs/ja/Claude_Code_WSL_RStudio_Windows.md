---
title: "WindowsでClaude CodeとRStudioを使用する"
lang: "ja"
---
[ホーム](./)

# WindowsでClaude CodeとRStudioを使用する

WindowsのRStudioでRコードを実行しながら、Claude CodeでAI支援を受ける方法を学びます。このチュートリアルでは、同じプロジェクトファイルを共有しながら両者を切り替えて使用します。Rプロジェクトを作成し、基本的なコードを記述した後、PowerShellのClaude Codeに可視化やPCA解析を生成させ、R Markdownレポートまで仕上げます。その間、RStudioは開いたままでコードの実行とテストができます。

## 主要コンセプト

- **PowerShell**：Windowsに標準搭載されているコマンドラインツール。ここではRStudioと並行してClaude Codeを実行するために使用します
- **ハイブリッドワークフロー**：RStudioでコードを実行・表示し、Claude Codeでコードを生成・改良
- **共有ファイル**：両ツールがまったく同じプロジェクトフォルダを操作するため、一方での変更がもう一方にも反映される

## 必要なもの

- [WindowsへのClaude Codeのインストール](./Install_CLAUDE_Code_Win)ガイドを完了済み
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

## ステップ5：PowerShellを開く

- **Windowsスタートボタン**をクリック
- 検索ボックスに`PowerShell`と入力
- **Windows PowerShell**をクリックして開く

## ステップ6：プロジェクトフォルダへ移動

- PowerShellで以下を入力：
  ```
  cd ~\Documents\test_claude
  ```
- 正しい場所にいることを確認するため、以下を入力：
  ```
  dir
  ```
- `iris.R`と`test_claude.Rproj`が表示されるはずです

## ステップ7：Claude Codeを起動

- PowerShellで以下を入力：
  ```
  claude
  ```

[インストールチュートリアル](Install_CLAUDE_Code_Win.md)に従って、Claudeサブスクリプションでログインしてください。ログイン後、ウェルカムメッセージとClaude Codeのプロンプトが表示されます。

## ステップ8：散布図コードを追加

Claude Codeの起動が遅い場合は、初期化が完了するまで待ちましょう。その後、以下のリクエストを入力します：

```
iris.Rに、がく片の長さと幅の散布図を種別ごとに色分けして作成するコードを追加してください。ggplot2を使用してください。
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

- PowerShellに切り替えます
- 以下のリクエストを入力：
  ```
  タイトルを削除してください。種別ごとにマーカーの形を変更してください。クラシックテーマに変更してください。
  ```

## ステップ11：改良されたプロットを表示

- RStudioに切り替えます
- プロンプトが表示されたらファイルを再読み込みします
- 更新されたコードを選択して**Run**をクリック
- プロットがタイトルなしで表示され、種ごとに異なるマーカー形状、クラシックテーマが適用されているはずです


## ステップ12：PCAプロットを追加

- PowerShellに切り替えます
- 以下のリクエストを入力：
  ```
  数値変数にPCAを実行し、第1・第2主成分を使ってサンプルをプロットするコードを追加してください。
  ```

## ステップ13：PCA解析を実行

- RStudioに切り替えます
- プロンプトが表示されたらファイルを再読み込みします
- すべてのコードを選択して**Run**をクリック
- PC1とPC2に投影されたサンプルを示すPCAプロットが表示され、種ごとに色分けされます

## ステップ14：レビューとコメント追加をClaudeに依頼

- PowerShellに切り替えます
- 以下のリクエストを入力：
  ```
  スクリプト全体の正確性をレビューしてください。必要に応じてコメントを追加してください。
  ```
- Claudeがコードをレビューし、包括的なコメントを追加します

## ステップ15：R Markdownを作成

- PowerShellに切り替えます
- 以下のリクエストを入力：
  ```
  この分析のための新しいR Markdownファイルを作成してください。iris_report.Rmdとして保存してください。
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
| RStudioが更新を検知しない | **File > Reopen with Encoding > UTF-8** で手動リロード |
| `claude: command not found` | インストールガイドを再確認。PowerShellのウィンドウを新しく開き直す |
| プロットが表示されない | RStudio Consoleで `install.packages("ggplot2")` を実行 |
| `cannot change working directory` | Windowsのパスにスペースが含まれています。ステップ6でパスを引用符で囲む：`cd "~\Documents\Your Name\test_claude"` |
| 初回リクエストが遅い | 30〜60秒待てば初期化され、その後は高速化します |
| WSLを使っている場合 | オプションのWSL/Ubuntuの方法を設定した場合は、ステップ5〜16でPowerShellの代わりに **Ubuntu** アプリを開き、`cd /mnt/c/Users/YourUsername/Documents/test_claude` でプロジェクトへ移動 |

## 次のステップ

- 統計検定（t検定、ANOVA）を分析に追加するようClaudeに依頼
- このコードのPython版を作成し、Quartoドキュメントを準備するようClaudeに依頼
- Rスクリプトの繰り返し処理のための関数を作成するようClaudeに依頼
- Rコード実行時のエラーメッセージのデバッグにClaudeを活用
- パフォーマンス向上のため、低速なRコードの最適化をClaudeに依頼

## ワークフローまとめ

このハイブリッドセットアップは両方のツールの長所を組み合わせます：

- **RStudio** - インタラクティブなRコンソール、即座のプロット表示、使い慣れたGUIでコードを実行
- **Claude Code（PowerShell）** - AIによるコード生成、レビュー、改善
- **共有ファイル** - 両ツールが同じプロジェクトフォルダを直接操作
- **反復的な改善** - 手動でコードを記述し、Claudeで強化し、RStudioでテストして、さらに改善
- **ドキュメント化** - Claudeが分析の包括的なレポートとコメントを生成

ワークフローはシンプルです。PowerShellのClaudeでコードを記述・編集し、すぐにRStudioでテストして実行します。ファイルのコピーや手動同期は不要で、両ツールが同じファイルを共有します。

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 11, 2025.
