[ホーム](./)

# Docker経由でVS CodeでRコーディング

Rコードを同僚と共有しようとして、「でも私のマシンでは動くよ」問題のデバッグに何時間も費やしたことはありませんか？Dockerコンテナはコード用の輸送コンテナのようなものです—R環境、ライブラリ、依存関係を、どこでも同じように動作する密閉されたボックスにパッケージ化します。さらに、[Docker Hub](https://hub.docker.com/)には何万もの事前構築イメージがあり、ソフトウェア開発者がすぐに使える環境を公開しているので、手動インストールの苦痛をスキップできます。このチュートリアルでは、VS CodeとDocker Desktopを使って、隔離された再現可能な環境でRを実行する方法を紹介します。

## 主要な概念

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - コンピュータ上でコンテナを実行し、隔離された環境を管理するアプリケーション
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - Dockerコンテナ内で完全なIDEサポートでコーディングできるVS Code機能
- **コンテナ隔離** - コードは別のLinux環境で実行され、プロジェクトフォルダのみが見え、コンピュータ全体は見えません
- **[Rocker](https://rocker-project.org/)** - R開発用に特別に設計された事前構築Dockerイメージ

## 必要なもの

- [VS CodeでRコーディング](./R_Coding_VS_Code_Guide)を完了
- [GitHub Desktopの基本](./Github_desktop)を完了
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

## ステップ3：GitHub DesktopでVibeプロジェクトをクローン

- GitHub Desktopを開く
- **File > Clone repository**をクリック
- **URL**タブをクリック
- **Repository URL**フィールドに貼り付け：`https://github.com/gexijin/vibe`
- プロジェクトを保存する場所を選択（**Local Path**フィールド）
- **Clone**をクリック
- GitHub Desktopが選択した場所にプロジェクトをダウンロードします

## ステップ4：VS Codeでプロジェクトを開く

- VS Codeで**ファイル > フォルダーを開く**をクリック
- クローンした`vibe`フォルダに移動
- **フォルダーの選択**をクリック
- エクスプローラーサイドバーにプロジェクトファイルが表示されます

## ステップ5：コンテナで再度開く

- 右下に通知が表示されます：**Folder contains a Dev Container configuration file**
- **Reopen in Container**をクリック
- 通知が表示されない場合は、左下隅の緑色のアイコンをクリック
- メニューから**Reopen in Container**を選択
- VS Codeがコンテナをビルドします（初回は5〜10分かかります）
- ビルドステップを示す進行通知が表示されます
- 完了すると、緑色のアイコンに**Dev Container: R in Docker**と表示されます

**注：** コンテナにはR拡張機能とlanguageserverパッケージが自動的に含まれます。Dockerfileとdevcontainer.jsonがこれを処理します。

## ステップ6：コンテナ環境を理解する

これでLinuxコンテナ内でコーディングしています。これが何を意味するか探索しましょう。

- **ターミナル > 新しいターミナル**をクリックしてコンテナ内のターミナルを開く
- 現在の場所を確認：

```bash
pwd
```

`/workspaces/vibe`と表示されます - これはコンテナ内のプロジェクトフォルダです。

- ファイルをリスト：

```bash
ls
```

プロジェクトと同じファイルが表示されます：`R/`、`.devcontainer/`、`README.md`など。

- 一つ上のディレクトリに移動してみる：

```bash
cd ..
ls
```

`vibe/`だけが表示されます - コンテナは隔離されています。コンピュータの他のフォルダ、デスクトップ、ドキュメントにはアクセスできません。この隔離により、R環境がクリーンで再現可能になります。

- プロジェクトフォルダに戻る：

```bash
cd vibe
```

## ステップ7：Rコードを行ごとに実行

コンテナには一般的なパッケージ付きのRがプリインストールされています。シンプルなデータ分析スクリプトを実行しましょう。

- VS Codeエクスプローラーで`R/iris_analysis.R`に移動
- クリックしてファイルを開く
- irisデータセットを分析するRコードが表示されます
- 最初の行を選択：`data(iris)`
- `Ctrl+Enter`（Windows/Linux）または`Cmd+Enter`（Mac）を押して実行
- Rターミナルが開いていない場合、最初に作成され、2回目でコードが実行されます
- 各行を1つずつ実行し続ける
- `head(iris)`を実行すると、ターミナルに最初の6行が表示されます
- `summary(iris)`を実行すると、統計的な要約が表示されます
- `hist()`コマンドを実行すると、ヒストグラムプロットが別ウィンドウで開きます
- 複数の行を選択して`Ctrl+Enter`または`Cmd+Enter`で一緒に実行することもできます

## ステップ8：アプリを実行

プロジェクトには対話型ヒストグラムを作成するデモShinyアプリが含まれています。

- VS Codeエクスプローラーで`R/app.R`に移動
- クリックしてファイルを開く
- Shiny Webアプリケーション用のコードが表示されます
- エディターウィンドウの右上に**▶**ボタンを探す
- その横のドロップダウン矢印をクリックして**Run Shiny App**を選択
- アプリが起動し、VS Codeが自動的にポート3838をフォワードします
- 通知が表示されます：**Open in Browser**
- **Open in Browser**をクリック
- ShinyアプリがWebブラウザで開きます
- スライダーを動かしてヒストグラムのビン数を変更 - チャートがリアルタイムで更新されます

## ステップ9：簡単な変更を加える

アプリを変更して開発がどのように機能するか見てみましょう。

- アプリを実行したまま
- VS Codeで`R/app.R`を編集
- 16行目を見つける：`titlePanel("Old Faithful Geyser Data")`
- 以下に変更：

```r
titlePanel("初めてのR Dockerアプリ")
```

- ファイルを保存（**ファイル > 保存**）
- Shiny拡張機能が自動的にアプリをリロードします
- ブラウザを更新（または自動的に更新される場合があります）
- タイトルがカスタムテキストで表示されます

## ステップ10：Dockerfileを理解する（オプション）

- VS Codeエクスプローラーで`.devcontainer/Dockerfile`に移動
- クリックしてファイルを開く
- 完全な設定が表示されます：

```dockerfile
# Dockerhubベースイメージを選択
FROM rocker/shiny-verse:latest

# 1. Rパッケージに一般的に必要なシステム依存関係
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# 2. VS Code統合用のRパッケージ：言語サーバー + デバッガー
RUN R -q -e 'install.packages(c("rstudioapi", "languageserver"), repos="https://cloud.r-project.org")'

# 3. NodeSourceからNode.js LTSをインストール
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Claude Codeをグローバルにインストール
RUN npm install -g @anthropic-ai/claude-code

# 5. Shinyサーバーポートを公開
EXPOSE 3838
```

**重要な部分：**

- `FROM rocker/shiny-verse:latest` - R、Shiny、tidyverseがプリインストールされたベースイメージ
- `RUN apt-get install` - Rパッケージ用のLinuxシステムライブラリ
- `RUN R -q -e 'install.packages(...)'` - Rパッケージを永続的にインストール
- `RUN curl... && apt-get install -y nodejs` - Claude Codeを実行するために必要なNode.jsをインストール
- `RUN npm install -g @anthropic-ai/claude-code` - AIアシスタンス用にClaude Codeをグローバルにインストール
- `EXPOSE 3838` - Shinyアプリ用にポート3838を開く

**使用できる他のRockerイメージ：**

- `rocker/r-ver:4.5.3` - Rのみ（特定バージョン）
- `rocker/rstudio:latest` - RとRStudio Server
- `rocker/tidyverse:latest` - Rとtidyverseパッケージ
- `rocker/shiny-verse:latest` - RとShinyとtidyverse（使用中）

ベースイメージを変更した後、コンテナを再ビルドして変更を適用してください。

## ステップ11：DockerイメージにRパッケージをインストール（オプション）

Rコンソールでインストールしたパッケージ（`install.packages()`）は一時的で、コンテナを再ビルドすると消えます。パッケージを永続的にするには、Dockerfileに追加してください。

- VS Codeエクスプローラーで`.devcontainer/Dockerfile`に移動
- クリックしてファイルを開く
- 他の'install.packages'の行の下に新しい行を追加して`data.table`パッケージをインストール：

```dockerfile
RUN R -q -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
```

- ファイルを保存（**ファイル > 保存**）
- 左下隅の緑色のアイコンをクリック
- メニューから**Rebuild Container**を選択
- VS Codeが新しいパッケージでコンテナを再ビルドします（2〜5分かかります）
- 確認するには、Rターミナルを開いて入力：

```r
library(data.table)
```

エラーなく読み込まれれば、パッケージは永続的にインストールされています。

## 次のステップ

- **新しいRスクリプトを作成** - `R/`フォルダに新しい`.R`ファイルを作成し、`mtcars`や`iris`などの組み込みデータセットを使用してデータ分析コードを書く
- **Rパッケージをインストール** - Dockerfileを編集してコンテナを再ビルドして、必要なパッケージを追加
- **tidyverseを探索** - サンプルデータセットを使用して`dplyr`でデータ操作、`ggplot2`で可視化を試す

## トラブルシューティング

- **Docker Desktopが実行されていない** - Docker Desktopを開き、コンテナを再度開く前に緑色のステータスインジケーターを待つ
- **コンテナビルドが失敗** - インターネット接続を確認。最初のビルドは約2GBダウンロードします。**Rebuild Container**をクリックして再試行
- **ポート3838がすでに使用中** - そのポートを使用している他のアプリを停止するか、`.devcontainer/devcontainer.json`でポートを変更

## ワークフロー概要

このセットアップにより、プロフェッショナルなR開発環境が得られます：

- **VS Code**がシンタックスハイライトとIntelliSenseを持つコードエディターを提供
- **Dockerコンテナ**がRとすべての依存関係を持つ隔離されたLinux環境を実行
- **Rockerイメージ**（`rocker/shiny-verse`）がR、Shiny、tidyverse、開発ツールを含む
- **Dev Container設定**（`.devcontainer/`）がRデバッグと言語サポート用のVS Code拡張機能を自動的にインストール
- **ポートフォワーディング**によりコンテナ内で実行されているShinyアプリにブラウザからアクセス可能

## 日常のワークフロー

すべてがセットアップされたら、日常のルーティンは以下の通りです：

1. **Docker Desktopを起動** - アプリを開いて緑色のステータスインジケーターを待つ（Dockerが実行されている必要があります）
2. **VS Codeを開く** - VS Codeを起動してプロジェクトフォルダを開く
3. **コンテナで再度開く** - まだコンテナ内でない場合、緑色のアイコン（左下）をクリックして**Reopen in Container**を選択
4. **コードを書いて実行** - `.R`ファイルを編集し、`Ctrl+Enter`/`Cmd+Enter`で行ごとに実行、またはShinyアプリを**▶ Run Shiny App**ボタンで実行
5. **作業を保存** - コードファイル（`.R`、`.Rmd`）はコンピュータに保存され、セッション間で永続
6. **コミットしてプッシュ** - GitHub Desktopを使用して変更をコミットし、リポジトリにプッシュ

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2025年12月7日に作成。
