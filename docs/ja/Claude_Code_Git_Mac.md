[ホーム](./)

# Mac版Claude Codeでローカルバージョン管理

Claude Codeに変更を任せると、コードベースはどんどん書き換わります。完璧に動くときもあれば、期待とは違う結果になることも。そんなとき、**Gitは「プロジェクト全体の取り消しボタン」**として力を発揮します。スナップショット（コミット）を積み重ねれば、いつでも安全な状態に戻れます。しかもコミットや差分確認といった操作もClaude Codeに任せられます。

## 主要な概念

- **ターミナル**：Macに標準搭載されているコマンドラインツール
- **Git**：変更履歴を記録し、復元ポイントを作るバージョン管理システム
- **コミット**：特定時点の状態を説明付きで保存するスナップショット
- **Claude Code**：自然言語の指示でコード作成やGit操作までこなすAIアシスタント

## 必要なもの

- [MacにClaude Codeをインストール](./Install_Claude_Code_MacOS)済み
- 所要時間：30分

## ステップ1：ターミナルを開く

次のいずれかの方法を選択してください：

- **Spotlight**：`Command (⌘) + Space`を押し、`ターミナル`と入力してEnterを押す
- **Finder**：**アプリケーション** > **ユーティリティ** > **ターミナル**を開く
- **Launchpad**：Dockの**Launchpad**をクリックし、`ターミナル`を検索

`$`または`%`で終わるコマンドプロンプトが表示されます。

## ステップ2：Gitをインストール

Macには多くの場合Gitが事前にインストールされています。確認してみましょう：

- 次のコマンドを入力してEnterを押します：
  ```
  git --version
  ```

**バージョン番号が表示される場合**（例：`git version 2.39.0`）、Gitはすでにインストールされています。ステップ3に進んでください。

**「command not found」と表示される場合、または開発者ツールをインストールするポップアップが表示される場合：**
- ポップアップの**インストール**をクリックするか、次のコマンドを実行します：
  ```
  xcode-select --install
  ```
- インストールが完了するまで待ちます（1〜5分）
- Gitがインストールされたことを確認します：
  ```
  git --version
  ```

`git version 2.39.0`のような表示が出ればOKです。

## ステップ3：Gitに自分の情報を設定

Gitはコミットメッセージのために、あなたが誰であるかを知る必要があります。

- 名前とメールアドレスを設定します（架空のものでも可）：
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

名前とメールアドレスを使用することで、複数の人が作業する際に誰が変更を行ったかを識別できます。

## ステップ4：Documentsフォルダに移動

- Documentsフォルダに移動します：
  ```
  cd ~/Documents
  ```
- 正しい場所にいることを確認します：
  ```
  pwd
  ```

`/Users/YOUR_USERNAME/Documents`と表示されるはずです。

## ステップ5：プロジェクトフォルダを作成

- `test_claude`というフォルダを作成します：
  ```
  mkdir test_claude
  ```
- その中に移動します：
  ```
  cd test_claude
  ```

ここがプロジェクトの場所になります。

## ステップ6：Claude Codeを起動

- Claude Codeを起動します：
  ```
  claude
  ```

Claude Codeが起動し、リクエストを待機します。

## ステップ7：ClaudeにGitの初期化を依頼

- 次のリクエストを入力します：
  ```
  Start tracking changes
  ```

Claudeがフォルダ内にGitリポジトリを初期化します（2〜5秒かかります）。これでバージョン管理が有効になりました！

## ステップ8：タイマーアプリを構築

- Claude Codeで次のように入力します：
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  ```

Claudeが`timer.html`を作成します（10〜30秒かかります）。CSSとJavaScriptのコードも含まれています。

## ステップ9：タイマーをテスト

- Finderを開く
- **書類** > **test_claude**に移動
- `timer.html`をダブルクリックしてブラウザで開く
- タイマーを試してみます：
  - 入力欄に`1`と入力
  - **Start**をクリック
  - カウントダウンを確認

**何か問題がある場合：** Claude Codeでエラーを説明します：`I'm seeing this error: [何が起こったかを説明]. Can you fix it?`

## ステップ10：Claudeにコミットを依頼

- Claude Codeで次のように入力します：
  ```
  Save these changes.
  ```

Claudeは次のことを行います：
- 変更されたファイルを確認
- わかりやすいコミットメッセージを作成
- コミットを作成（5〜10秒かかります）

最初のセーブポイントが作成されました！いつでもこの動作するバージョンに戻ることができます。

## ステップ11：プリセットボタンを追加

- Claude Codeで次のように入力します：
  ```
  Add two buttons on the top. If I click on them it automatically starts 1- and 5-minute timers.
  ```
- ブラウザタブを更新します（または`Command (⌘) + R`を押します）
- テスト：**5 min**ボタンをクリック
- 動作する場合は、変更をコミットします：
  ```
  Save these changes.
  ```

2番目のセーブポイントが作成されました。このバージョンには2つのボタンが動作しています。

## ステップ12：別のボタンを追加

- Claude Codeで次のように入力します：
  ```
  Add a 15-minute button.
  ```
- ブラウザタブを更新します（`Command (⌘) + R`を押します）
- テスト：**15 min**ボタンをクリック

**このチュートリアルでは：** 15分ボタンが正しく動作しないと仮定してください。まだコミットしないでください。次は失敗した変更を破棄する練習をします。

## ステップ13：変更を破棄

AIのコードが動作しない場合があり、最後のセーブポイントからやり直す必要があります。

- Claude Codeで次のように入力します：
  ```
  discard these changes.
  ```
- Claudeが確認を求めます
- `yes`と入力してEnterを押します
- ブラウザを更新すると、15分ボタンが消えます

Claudeは気に入らない新しい変更を破棄します。タイマーは1分と5分のボタンだけで再び動作します！

## ステップ14：サウンド通知を追加

- Claude Codeで次のように入力します：
  ```
  Add a sound notification when time is up.
  ```
- Claudeが完了したらブラウザを更新してテスト（タイマーを0.1分に設定）
- 動作する場合は、変更をコミットします：
  ```
  Save these changes.
  ```

## ステップ15：スヌーズボタンを追加

- Claude Codeで次のように入力します：
  ```
  The sound should continue until I click a button to snooze it.
  ```
- Claudeが完了したらブラウザを更新してテスト（タイマーを0.1分に設定）
- 動作する場合は、変更をコミットします：
  ```
  Save these changes.
  ```

## ステップ16：コミット履歴を表示

- Claude Codeで次のように入力します：
  ```
  show my change history
  ```

Claudeがコミットを読みやすい形式で表示します。次のものが表示されます：
- 初期タイマーアプリのコミット
- プリセットボタン（1分と5分）のコミット
- サウンド通知のコミット
- スヌーズボタンのコミット

15分ボタンの試みはここにありません。破棄したからです！

## ステップ17：コードを確認

- アプリを表示しているブラウザで、右クリックして**ページのソースを表示**を選択（または`Option (⌥) + Command (⌘) + U`を押します）
- ソースコードが表示されます
- Claude Codeで次のように尋ねます：
  ```
  Explain this code. Just big picture.
  ```

## 完全なワークフロー

- Claudeに変更を依頼
- テスト
- 動作する場合 → Claudeにコミットを依頼
- 失敗する場合 → Claudeに修正を依頼
- 修正できない場合 → 変更を破棄して再試行
- 繰り返し

いつでも任意のコミットに戻ることができます。恐れずに破棄してください。動作するコードだけをコミットしましょう！

## 次のステップ

タイマーにさらに機能を追加してみましょう：

- **15分ボタン：** `Add a working 15-minute preset button`（破棄したものをやり直しましょう！）
- **一時停止ボタン：** `Add a Pause/Resume button that toggles the timer state`
- **より良いスタイリング：** `Improve the visual design with a modern color scheme and larger fonts`
- **プログレスバー：** `Add a visual progress bar showing time remaining`

覚えておいてください：各機能の後にテストし、成功したらコミットし、失敗したら破棄します。

## トラブルシューティング

- **「not a git repository」エラー：** test_claudeフォルダにいることを確認してください（`cd ~/Documents/test_claude`）
- **Finderでtimer.htmlが見つからない：** ファイルは`/Users/YOUR_USERNAME/Documents/test_claude/timer.html`にあります
- **Gitコマンドが動作しない：** ステップ2を完了してGitをインストールしたことを確認してください
- **タイマーが動作しない：** ブラウザコンソールを開き（ページを右クリックして**検証**を選択し、**コンソール**タブをクリック）、赤いエラーメッセージをコピーしてClaudeに貼り付けます

## Claudeに依頼できること

- `what files have I changed?` - コミットされていない変更を確認
- `show me the diff` - 変更されたコードを正確に確認
- `explain what the timer code does` - 実装を理解
- `create a branch called experiment` - リスクのある変更を安全に試す
- `go back to the previous commit` - 最後のコミット以降のすべてを元に戻す

ClaudeはすべてのGit操作を自然言語で処理します。コマンドを覚える必要はありません！

## ワークフロー概要

- **セットアップ：** Gitを一度インストールし、一度IDを設定
- **開発：** Claudeがコードを書き、ブラウザでテスト
- **バージョン管理：** Claudeが簡単なリクエストを通じてすべてのGit操作を処理
- **安全性：** いつでも失敗した変更を破棄し、以前のコミットに戻れる
- **ローカル：** すべてがコンピュータ上にとどまり、アカウントやインターネットは不要

作成者：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)（2025年12月8日）
