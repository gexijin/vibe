---
title: "VS CodeでRを実行"
lang: "ja"
---
[ホーム](./)

# VS CodeでRを実行

Rコードを書きたいけど、RStudioが重く感じる、またはVS Codeの柔軟性を好むという方へ。VS Codeはスイスアーミーナイフのように、R、Python、その他多くの言語を1つの軽量エディターで扱えます。このチュートリアルでは、VS CodeでRをセットアップし、コード補完、対話型プロット、Shinyアプリまで実行する方法を紹介します。

## 主要な概念

- **[languageserver](https://github.com/REditorSupport/languageserver)** - VS Codeでコード補完、構文チェック、ホバードキュメントを可能にするRパッケージ
- **[R拡張機能](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - エディターをRに接続し、シンタックスハイライト、コード実行、デバッグを提供するVS Code拡張機能
- **[Shiny拡張機能](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - 自動リロード付きで対話型Shiny Webアプリを作成・実行するためのVS Code拡張機能

## 必要なもの

- [VS Codeの基本](./VS_Code_Getting_Started)を完了
- Rとパッケージをダウンロードするためのインターネット接続
- 10〜15分

## ステップ1：Rをインストールまたは更新

最高の互換性のためにRバージョン4.0以上が必要です。

- **Windows**：
  - [CRAN Windows](https://cran.r-project.org/bin/windows/base/)から最新のRをダウンロードしてインストーラーを実行
  - インストール中、**インストールパスをメモ**（例：`C:\Program Files\R\R-4.6.1`）
  - 古いバージョンがある場合は、設定 > アプリ（Settings > Apps）から先にアンインストール

- **macOS**：
  - [CRAN macOS](https://cran.r-project.org/bin/macosx/)からダウンロードして.pkgインストーラーを実行
  - CRANのインストーラーは、IntelとApple SiliconのどちらのMacでもRを`/Library/Frameworks/R.framework/Resources/bin/R`に配置します（代わりにHomebrewでRをインストールした場合、Apple Siliconでは`/opt/homebrew/bin/R`です）
  - 更新する場合、新しいバージョンが古いものを置き換えます

- **Linux**：
  - パッケージマネージャーを使用（例：Ubuntuで`sudo apt install r-base`）
  - または[CRAN Linux](https://cran.r-project.org/bin/linux/)の手順に従う

ステップ4でVS CodeがRを見つけるように設定するので、ターミナルで`R --version`がまだ動作しなくても心配しないでください。

## ステップ2：VS CodeにR拡張機能をインストール

- VS Codeを開く
- 左サイドバーの**Extensions**（拡張機能）アイコンをクリック
- `REditorSupport.r`を検索してREditorSupportのR拡張機能の**Install**（インストール）をクリック
- `Posit.shiny`を検索してPositのShiny拡張機能の**Install**をクリック

## ステップ3：Rインストールパスを見つける

VS Codeを設定する前に、システム上のRがどこにインストールされているか知る必要があります。

### Windowsユーザー向け

1. **エクスプローラー**（File Explorer）を開く
2. `C:\Program Files\R\`に移動
3. `R-4.6.1`のようなフォルダが表示されます（バージョン番号は異なる場合があります）
4. そのフォルダを開く → `bin`フォルダを開く
5. そこに`R.exe`があります
6. フルパスは：`C:\Program Files\R\R-4.6.1\bin\R.exe`

**バージョン番号を書き留めるか覚えておいてください**（例：`R-4.6.1`）- ステップ4で必要になります。

### macOSユーザー向け

Rインストールは通常以下の場所のいずれかにあります：

- **標準インストール（IntelまたはApple Silicon）**：`/Library/Frameworks/R.framework/Resources/bin/R`
- **Apple SiliconのHomebrew**：`/opt/homebrew/bin/R`
- **IntelのHomebrew**：`/usr/local/bin/R`

どのパスがあるか確認するには、**ターミナル**（Terminal）を開いて入力：
```bash
which R
```

これでRインストールへの正確なパスが表示されます。

### Linuxユーザー向け

Rは通常以下にインストールされています：`/usr/bin/R`

ターミナルを開いて入力して確認：
```bash
which R
```

## ステップ4：VS CodeがRを見つけるように設定

- VS Codeで、**View > Command Palette**（表示 > コマンド パレット）をクリック
- `Preferences: Open User Settings (JSON)`と入力して選択
- settings.jsonファイルが開きます
- 中括弧`{}`内にプラットフォームに合った行を追加します。すでに他の行がある場合は、追加する行のすぐ上の行がカンマで終わっていることを確認してください

**Windowsの場合**、この行を追加（`R-4.6.1`をステップ3のバージョンに置き換え）：

```json
"r.executablePath": "C:\\Program Files\\R\\R-4.6.1\\bin\\R.exe",
```

**なぜバックスラッシュが2つ（`\\`）なのか？** JSONファイルでは、バックスラッシュ`\`は特殊文字（エスケープ文字と呼ばれる）です。実際のファイルパスで1つのバックスラッシュを表すには、`\\`と2つ入力する必要があります。そのため`C:\Program Files`はsettings.jsonでは`C:\\Program Files`になります。

**macOSの場合**、これらの行のいずれかを追加：

```json
"r.executablePath": "/Library/Frameworks/R.framework/Resources/bin/R",
```

または、Apple SiliconでHomebrewでRをインストールした場合：

```json
"r.executablePath": "/opt/homebrew/bin/R",
```

**Linuxの場合**、追加：

```json
"r.executablePath": "/usr/bin/R",
```

- **File > Save**（ファイル > 保存）をクリックしてファイルを保存
- 変更を有効にするにはVS Codeを完全に**再起動**

## ステップ5：必要なRパッケージをインストール

- VS Codeで、トップメニューの**View**（表示）をクリックし、**Command Palette**（コマンド パレット）を選択
- `R: Create R Terminal`と入力して選択
- 下部のターミナルパネルにRコンソールが表示されます
  - バージョン情報とともにRが起動するのが見えるはずです
  - VS Codeが**sess**パッケージのインストールを求めてきたら、**Yes**（または**Install bundled sess**）をクリックして完了を待ちます。これによりVS Codeでプロットや変数を表示できるようになります
  - エラーが表示された場合は、ステップ4のsettings.json設定を再確認してVS Codeを再起動してください
- これらのコマンドを1つずつ入力してパッケージをインストール：

```r
install.packages("languageserver")
install.packages("shiny")
```

- インストールが完了するまで待つ（数分かかる場合があります）
- `q()`と入力してEnterを押してRを終了
- Rはすぐに終了します（ワークスペースを保存するか聞かれたら`n`と入力）

通常のターミナルで単に`R`と入力してもRがシステムPATHにない限り動作しません。R拡張機能は`r.executablePath`設定を使用してRを見つけます。

## ステップ6：Rプロジェクトを作成

- コンピュータに新しいフォルダを作成（例：`my-r-project`）
- VS Codeで**File > Open Folder**（ファイル > フォルダーを開く）をクリックして新しいフォルダを選択
- トップメニューで**File > New File...**（ファイル > 新しいファイル...）をクリックし、ウィンドウ上部の一覧から**R Document**を選択
- **File > Save**（ファイル > 保存）をクリックして`analysis.R`として保存

## ステップ7：最初のRスクリプトを書く

- `analysis.R`に以下のコードを入力：

```r
# irisデータセットを読み込み
data(iris)

# 最初の数行を表示
head(iris)

# 要約統計を生成
summary(iris)

hist(iris$Sepal.Length)
```

- **File > Save**（ファイル > 保存）をクリックしてファイルを保存

## ステップ8：Rコードを対話的に実行

- `analysis.R`を開いた状態で、コードの行を選択して`Ctrl+Enter`（Windows/Linux）または`Cmd+Enter`（Mac）を押して実行
- ターミナルが開いていない場合、最初の`Ctrl+Enter` / `Cmd+Enter`でRターミナルが開き、2回目でコードが実行されます
- ターミナルに出力が表示されます。ヒストグラムはVS Code内のスクリプトの隣にあるプロットタブで開きます
- すべての行を選択して同じ方法で実行することもできます

## ステップ9：シンプルなShinyアプリを作成

- プロジェクトフォルダに新しいファイルを作成：**File > New File...**（ファイル > 新しいファイル...）をクリックし、**R Document**を選択
- `app.R`として保存
- 以下のコードを入力：

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Interactive Histogram"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 5,
                  max = 50,
                  value = 30)
    ),

    mainPanel(
      plotOutput("histogram")
    )
  )
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    x <- faithful$waiting
    bins <- seq(min(x), max(x), length.out = input$bins + 1)

    hist(x, breaks = bins, col = "steelblue", border = "white",
         xlab = "Waiting time (minutes)",
         main = "Distribution of Waiting Times")
  })
}

shinyApp(ui = ui, server = server)
```

- ファイルを保存
- エディター右上に表示される**▶**ボタンに注目
- ドロップダウンをクリックして**Run Shiny App**を選択
- アプリがブラウザまたはVS Codeパネルで開きます
- スライダーを動かすとヒストグラムが即座に更新されます

## ステップ10：コード補完とホバーヘルプを使用

- `analysis.R`で、新しい行に`mea`と入力し始める
- 提案を含むドロップダウンが表示されます - Enterを押して`mean()`を選択
- 今入力した`mean`という単語の上にマウスを置く
- 関数のドキュメントと使用例を表示するポップアップが現れます
- スクリプト内の`summary`または`hist`の上にマウスを置いてドキュメントを確認
- `iris$`と入力するとVS Codeが列名（`Sepal.Length`、`Species`など）を提案します

## ステップ11：他の機能を試す

- **Markdown統合**：コード、出力、テキストを混在させるR Markdownファイル（`.Rmd`）を作成
- **コードフォーマット**：Rスクリプト内で右クリックして**Format Document**（ドキュメントのフォーマット）を選択してコードを自動フォーマット
- **デバッグ**：[R Debugger拡張機能](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger)をインストールし、そのセットアップページに従ってブレークポイントを追加し、コードをステップ実行
- **Git統合**：VS Codeの内蔵Git機能を使用してRプロジェクトをバージョン管理

## 次のステップ

- 別々の`ui.R`と`server.R`ファイルでマルチファイルShinyアプリを作成
- 高度なデータ可視化のために[ggplot2](https://ggplot2.tidyverse.org/)を探索
- データ操作のために[tidyverse](https://www.tidyverse.org/)パッケージ（`dplyr`、`tidyr`）を試す
- 埋め込みRコードでレポートを作成するためにR Markdownや[Quarto](https://quarto.org/)を学ぶ
- 高度なデバッグのために[R Debugger拡張機能](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger)をインストール

## トラブルシューティング

- **VS Codeターミナルで「R is not recognized」**：VS CodeがRを見つけられません。settings.json（ステップ4）を確認 - Rパスが正しく`R.exe`（Windows）またはRバイナリ（Mac/Linux）を指していることを確認。パスの例：
  - Windows：`C:\\Program Files\\R\\R-4.6.1\\bin\\R.exe`（バージョン番号を調整）
  - macOS（CRANインストーラー、IntelまたはApple Silicon）：`/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew：`/opt/homebrew/bin/R`
  - Linux：`/usr/bin/R`
  修正後、VS Codeを完全に再起動してください。

- **設定のRバージョン不一致**：Rを更新したがVS Codeがまだ古いバージョンを使用している場合、settings.jsonの`r.executablePath`の行のバージョン番号を新しいRインストールに合わせて更新してください（ステップ3で現在のインストールパスを見つける）。

- **コード補完が動作しない**：languageserverが正常にインストールされたことを確認（ステップ5）。インストール後にVS Codeを再起動。Rファイルを開いた後、言語サーバーが初期化されるまで10〜20秒待つ。Output（出力）パネル（View > Output > R Language Server）でエラーを確認。

- **プロットが表示されない**：プロットはVS Code内のタブで開きます。何も表示されない場合は、（通常のターミナルで`R`と入力するのではなく）**R: Create R Terminal**でRを起動したことを確認し、`hist()`の行をもう一度実行してください。

- **Shinyアプリが実行されない**：Shiny拡張機能がインストールされていることを確認（ステップ2）、shinyパッケージがインストールされていること（ステップ5）、ファイル名が`app.R`であること。ターミナルでエラーメッセージを確認。実行ボタンはVS CodeがファイルをShinyアプリとして認識したときのみ表示されます。

## ワークフロー概要

VS CodeはRStudioに代わるモダンで軽量な環境を提供し、以下の主な利点があります：

- **統一環境**：1つのエディターでR、Python、JavaScriptなどをコーディング
- **カスタマイズ可能**：軽量なセットアップのために必要な拡張機能のみインストール
- **統合ターミナル**：R、Git、シェルコマンドを並行して実行
- **Shiny開発**：自動リロードでワンクリックアプリ起動が時間を節約
- **バージョン管理**：外部ツールなしでGit統合

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2025年12月7日に作成。
