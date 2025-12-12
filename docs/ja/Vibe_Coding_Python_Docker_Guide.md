[ホーム](./)

# Claude CodeとDockerでPythonのVibe Coding

今まですべての行を自分で入力してPythonコードを書いてきました。でも、欲しいものを平易な言葉で説明するだけでコードが現れたらどうでしょう？Vibe Codingはコンピュータとの会話のようなものです—結果を説明し、Claude Codeがそれを構築し、テストして改良します。魔法ではありません。あなたがビジョンを導き、AIが実装を処理する新しい作業方法です。このチュートリアルでは、自然言語のリクエストだけを使って古典的なIrisフラワーデータセットを分析する方法を紹介します。

## 主要な概念

- **[Vibe Coding](https://www.ibm.com/think/topics/vibe-coding)** - コードを行ごとに書くのではなく、欲しいものを自然言語で説明し、結果に基づいて反復するプログラミング
- **[Claude Code](https://code.claude.com/)** - 自然言語リクエストに基づいてコードを書き、デバッグし、リファクタリングするAIコーディングアシスタント
- **[Irisデータセット](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)** - 3種150個のアイリスの花の測定値を含む古典的なデータセット
- **反復的改良** - Vibe codingの中核となるパターン：説明 → テスト → 改良 → 動作バージョンをコミット

## 必要なもの

- [Docker経由でVS CodeでPythonコーディング](./Python_Coding_Docker_Guide)を完了
- [GitHub DesktopとClaude Codeを使用](./GitHub_Desktop_Claude_Code_Workflow)を完了
- 20〜25分

## ステップ1：新しいGitHubリポジトリを作成

- GitHub Desktopを開く
- **File > New Repository**をクリック
- 詳細を記入：
  - **Name：** `iris-analysis`
  - **Description：** `vibe codingで構築したIrisデータ分析`
  - **Local Path：** 場所を選択（例：ドキュメントまたは作業フォルダ）
  - **Initialize this repository with a README**にチェック
- **Create Repository**をクリック
- 上部の**Publish repository**をクリック
- 公開したい場合は**Keep this code private**のチェックを外す（オプション）
- **Publish Repository**をクリック

ローカルGitリポジトリとGitHub上のバックアップができました。

## ステップ2：Docker設定をコピー

Docker環境をセットアップするために、vibeプロジェクトの`.devcontainer`フォルダが必要です。

- エクスプローラー（Windows）またはFinder（Mac）を開く
- vibeプロジェクトフォルダに移動（例：`Documents/vibe`）
- `.devcontainer`フォルダを見つける
- フォルダ全体をコピー（`Dockerfile`と`devcontainer.json`が含まれています）
- 新しい`iris-analysis`フォルダに移動
- `.devcontainer`フォルダを貼り付け

`iris-analysis`フォルダには以下が含まれるはずです：
- `.devcontainer/`（コピーしたフォルダ）
- `README.md`（GitHub Desktopが作成）
- `.git/`（バージョン管理用の隠しフォルダ）

## ステップ3：コンテナでプロジェクトを開く

- VS Codeを開く
- **ファイル > フォルダーを開く**をクリック
- `iris-analysis`フォルダに移動
- **フォルダーの選択**をクリック
- 右下に通知が表示されます：**Folder contains a Dev Container configuration file**
- **Reopen in Container**をクリック
- 通知が表示されない場合は、左下隅の緑色のアイコンをクリックして**Reopen in Container**を選択
- VS CodeがDockerコンテナをビルドします（初回は3〜5分かかります）
- ビルドステップを示す進行通知を見る
- 完了すると、緑色のアイコンに**Dev Container: Python in Docker**と表示されます

## ステップ4：Claude Codeを起動

- VS Codeで**ターミナル > 新しいターミナル**をクリック
- これでDockerコンテナ内にいます
- このコマンドを入力してClaude Codeを起動：

```bash
claude
```

- 認証用のブラウザウィンドウが開きます
- **Continue with Google**または**Continue with Email**をクリック
- Claudeアカウントでログイン（または作成）
- 認証が成功したら、VS Codeターミナルに戻る
- Claudeのウェルカムメッセージが表示されます

Claude Codeが実行中で、リクエストの準備ができました。

## ステップ5：最初のVibe - データを読み込む

ここからが楽しい部分です。ドキュメントを調べる代わりに、欲しいものを説明するだけです。

- Claude Codeターミナルで入力：

```
scikit-learnからirisデータセットを読み込んで。適切な列名でpandas dataframeに変換して。種名を列として追加して（数字だけではなく）。最初の10行を表示して。コードをiris_exploration.pyというファイルに保存して。
```

- Enterを押す
- Claudeの動作を見る：
  - データを読み込むPythonコードを書く
  - 適切なインポートでスクリプトを作成
  - 結果を表示するためにコードを実行
- 花の測定値と種名を表示する出力を確認

vibe codingを使いました！ドキュメント検索も試行錯誤もなし—説明してテストするだけ。

Gitを使ってコミットするようClaudeに依頼します。または、GitHub Desktopから自分で行うこともできます。
```
これらの変更をコミットして。
```

## ステップ6：2番目のVibe - 要約統計

可視化を作成する前に、データに何が含まれているか理解しましょう。

- Claude Codeターミナルで入力：

```
irisデータの種ごとにグループ化した要約統計を見せて。各種について各測定値（がく片の長さ、がく片の幅、花びらの長さ、花びらの幅）の平均、最小、最大を見たい。これをiris_exploration.pyに追加して。
```

- Enterを押す
- Claudeがスクリプトを更新して統計を表示
- 異なる種が異なる測定範囲を持っていることに注目
- SetosaはVirginicaよりもはるかに小さい花びらを持っている

この探索によりデータのパターンを理解できます。

Gitを使ってコミットするようClaudeに依頼します。または、GitHub Desktopから自分で行うこともできます。

## ステップ7：3番目のVibe - ヒストグラムを作成

データを可視化する時間です。

- Claude Codeターミナルで入力：

```
全ての花の花びらの長さの分布を示すヒストグラムを作成して。20ビンを使用して。タイトルと軸ラベルを追加して。プロットをpetal_length_histogram.pngとして保存して。このコードをiris_exploration.pyに追加して。
```

- Enterを押す
- Claudeが可視化コードを作成
- プロジェクトフォルダにPNGファイルが表示されます
- `petal_length_histogram.png`を開いてチャートを確認
- 2つのピークに注目—これは種ごとに異なる花びらの長さがあることを示しています

## ステップ8：4番目のVibe - 散布図

散布図は2つの変数間の関係を示します。

- Claude Codeターミナルで入力：

```
x軸に花びらの長さ、y軸に花びらの幅を持つ散布図を作成して。各点を種ごとに異なる色で色付けして。どの色がどの種かを示す凡例を追加して。petal_scatter.pngとして保存して。これをiris_exploration.pyに追加して。
```

- Enterを押す
- Claudeが散布図を作成
- `petal_scatter.png`を開いて結果を確認
- 3つの種が明確なクラスターを形成していることに注目
- Setosa（小さい花びら）は他から明確に分離されている

これがvibe codingの実践：可視化を説明し、テストし、反復。

## ステップ9：5番目のVibe - 箱ひげ図

箱ひげ図はグループ間の分布を比較するのに最適です。

- Claude Codeターミナルで入力：

```
3つの種間で花びらの長さを比較する箱ひげ図を作成して。x軸に種、y軸に花びらの長さを配置して。各種に異なる色を使用して。タイトルを追加して。species_boxplot.pngとして保存して。これをiris_exploration.pyに追加して。
```

- Enterを押す
- Claudeが箱ひげ図コードを追加
- `species_boxplot.png`を開いて比較を確認
- 箱が各種の中央値と四分位数を表示
- Virginicaが最も長い花びらを持っていることが明確にわかる

## ステップ10：確認してコミット

コミットする前に、Claudeが構築したものを確認しましょう。

- VS Codeエクスプローラーで`iris_exploration.py`をクリックして開く
- コードをざっと見る—インポート、データ読み込み、プロッティングセクションに注目
- 全ての行を理解する必要はありませんが、構造の感覚をつかむ
- すべてのPNGファイルが作成されたことを確認：`petal_length_histogram.png`、`petal_scatter.png`、`species_boxplot.png`
- GitHub Desktopを開く
- すべての新しいファイルがリストされている（PythonスクリプトとPNG画像）
- 左下の**Summary**フィールドに入力：

```
ヒストグラム、散布図、箱ひげ図付きのIrisデータ分析
```

- **Commit to main**をクリック
- **Push origin**をクリックしてGitHubにバックアップ

最初の動作する分析を保存しました！

## ステップ11：反復して改善

Vibe codingは反復するときに輝きます。説明するだけで機能を追加してみてください：

**Claudeへのリクエスト例：**

- 「4つの測定すべての間の関係を示す相関行列ヒートマップを追加して」
- 「種間でがく片の幅を比較するバイオリンプロットを作成して」
- 「花びらの長さと幅の間の相関係数を計算して表示して」
- 「種を比較する統計検定結果を追加して（ANOVAまたはt検定）」
- 「種ごとに色分けされたすべての変数の関係を示すペアプロットを作成して」

成功した機能の後に：
- スクリプトを実行してテスト
- うまくいったら、GitHub Desktopでコミット
- 壊れたら、エラーをClaudeに伝えて修正を依頼
- 修正されたら、動作するバージョンをコミット


**重要な原則：**

- **実装ではなく結果を説明** - 「相関ヒートマップを表示して」と言い、「seaborn.heatmap()をdf.corr()で使って」とは言わない
- **素早く反復** - テスト → 改良 → テスト → 改良
- **動作するバージョンをコミット** - 新しい機能を試す前に各成功を保存
- **失敗を受け入れる** - Claudeのコードが壊れたら、エラーを説明して修正を依頼するだけ
- **コントロールを維持** - 機能、優先順位、十分かどうかを決めるのはあなた

毎回、説明 → テスト → 反復 → コミットのパターンに従います。

## 次のステップ

- **異なるデータセットを試す** - Claudeにwineデータセット、digitsデータセット、またはCSVファイルの読み込みを依頼
- **より多くの可視化を探索** - ヒートマップ、ペアプロット、バイオリンプロットを試す
- **質問して学ぶ** - Claudeがコードを書いたとき、「この行は何をしているか説明して」と聞いてPythonを学ぶ
- **自分のデータに適用** - vibe codingを使って自分の研究や仕事のデータを分析
- **vibe codingについて読む** - [IBMのガイド](https://www.ibm.com/think/topics/vibe-coding)を訪問してこのコーディングスタイルについて詳しく学ぶ

## トラブルシューティング

- **プロットが表示されない** - コードはプロットをPNGファイルとして保存します。プロジェクトフォルダを探して、VS Codeで直接画像ファイルを開いてください。
- **インポートエラー** - Dockerコンテナにはpandas、matplotlib、scikit-learnがプリインストールされているはずです。そうでない場合は、Claudeにpipでインストールを依頼してください。
- **Claudeが間違える** - 正常です！エラーメッセージをコピーし、Claudeに貼り付けて「このエラーを修正して」と言ってください。Vibe codingには反復とデバッグが含まれます。
- **GitHubにプッシュできない** - GitHub Desktopにログインし、リポジトリを公開したことを確認してください（ステップ1）。インターネット接続を確認してください。
- **コンテナが起動しない** - Docker Desktopが実行中であることを確認（緑色のステータスインジケーター）。VS Codeの緑色のアイコンをクリックして**Rebuild Container**を選択してみてください。

## ワークフロー概要

このチュートリアルでは、複数の技術を1つのワークフローに組み合わせました：

- **GitHub Desktop** - ビジュアルインターフェースでのバージョン管理（リポジトリ作成、コミット、プッシュ）
- **Dockerコンテナ** - すべての依存関係がプリインストールされた隔離されたPython環境
- **VS Code** - Dockerコンテナに接続するコードエディター
- **Claude Code** - 説明からPythonコードを書くAIアシスタント
- **scikit-learn** - Irisデータセットと機械学習ツールを提供
- **pandas** - データ操作と分析
- **matplotlib** - 可視化の作成

魔法は単一のツールではありません—Vibe codingにより欲しいものを説明して素早く反復できることです。空のプロジェクトから複数の可視化を含む完全なデータ分析まで、手動で1行もコードを書かずに20分で達成しました。

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2025年12月11日に作成。
