[ホーム](./)

# Windows版Claude Codeとバージョン管理

AIの支援を受けて作業しています。AIはファイルを変更します。変更が素晴らしいこともあれば、そうでないこともあります。**バージョン管理はプロジェクト全体の取り消しボタンのようなものです。** スナップショット（「コミット」と呼ばれる）を保存するたびに、いつでも戻れる復元ポイントが作成されます。しかも、すべてコンピューター上で実行でき、Claude Codeがすべて処理してくれます。

## 主要な概念

- **WSL (Windows Subsystem for Linux)**：Linuxツール（Gitなど）をWindows上でそのまま実行できる仕組み
- **Git**：ファイルの変更履歴をすべて記録し、任意の時点に戻れるようにするバージョン管理システム
- **コミット**：特定の時点でのプロジェクトの状態を説明付きで保存したもの
- **Claude Code**：自然言語で指示するだけでコード作成・修正・Git操作まで行ってくれるAIアシスタント

## 必要なもの

- [WindowsへのClaude Codeのインストール](./Install_CLAUDE_Code_Win)が完了していること
- WSLとUbuntuがインストール済み
- 20分

## ステップ1：Ubuntuターミナルを開く

- **スタート**メニューをクリック
- `Ubuntu` と入力
- **Ubuntu** をクリックしてターミナルを開く

`$` で終わるコマンドプロンプトが表示されます。

## ステップ2：Gitをインストール

- 次のコマンドを入力してEnterを押します：
  ```
  sudo apt-get install git
  ```
- パスワードを求められたら入力してEnterを押します
- インストールが完了するまで待ちます（10〜30秒）
- Gitがインストールされたことを確認します：
  ```
  git --version
  ```

`git version 2.34.1` のように表示されるはずです。

## ステップ3：Gitに身元情報を登録

Gitはコミットメッセージに誰が変更したかを記録する必要があります。

- 名前とメールアドレスを設定します（架空のものでも構いません）
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

複数人で作業する場合、名前とメールアドレスを使うことで誰が変更したかを識別できます。

## ステップ4：Windowsフォルダへ移動

WSLは `/mnt/c/` を通じてWindowsファイルにアクセスできます。

- Windowsのユーザーフォルダに移動します：
  ```
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  ```
  `YOUR_USERNAME` は実際のWindowsユーザー名に置き換えてください。
- 正しい場所にいることを確認します：
  ```
  pwd
  ```

`/mnt/c/Users/YOUR_USERNAME/Documents` と表示されるはずです。

## ステップ5：プロジェクトフォルダを作成

- `timer` というフォルダを作成します：
  ```
  mkdir timer
  ```
- フォルダ内に移動します：
  ```
  cd timer
  ```

ここがプロジェクトの作業場所になります。

## ステップ6：Claude Codeを起動

- Claude Codeを起動します：
  ```
  claude
  ```

Claude Codeが起動し、リクエストを待機します。

## ステップ7：ClaudeにGitの初期化を依頼

- このリクエストを入力します：
  ```
  Start tracking changes
  ```

ClaudeがフォルダにGitリポジトリを初期化します（2〜5秒かかります）。これでバージョン管理の準備が整いました。

## ステップ8：タイマーアプリを構築

- Claude Codeで次のように入力します：
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  ```

Claudeが `timer.html` を作成します（10〜30秒かかります）。CSSとJavaScriptのコードも含まれます。

## ステップ9：タイマーをテスト

- Windowsのファイルエクスプローラーを開く
- `Documents\timer` に移動
- `timer.html` をダブルクリックしてブラウザで開く
- タイマーを試します：
  - 入力フィールドに `1` と入力
  - **Start** をクリック
  - カウントダウンを確認

**何か壊れている場合：** Claude Codeで、エラーを説明します：`I'm seeing this error: [何が起こったか説明]. Can you fix it?`

## ステップ10：Claudeにコミットを依頼

- Claude Codeで次のように入力します：
  ```
  Save these changes.
  ```

Claudeが次の処理を行います：
- 変更されたファイルを確認
- 説明的なコミットメッセージを作成
- コミットを作成（5〜10秒かかります）

最初のセーブポイントが作成されました。いつでもこの動作するバージョンに戻ることができます。

## ステップ11：プリセットボタンを追加

- Claude Codeで次のように入力します：
  ```
  Add two buttons on the top. If I click on them it automatically starts 1- and 5-minute timers.
  ```
- ブラウザタブを更新
- テスト：**5 min** ボタンをクリック
- 動作する場合は、変更をコミットします：
  ```
  Save these changes.
  ```

2つ目のセーブポイントが作成されました。このバージョンでは2つのボタンが動作しています。

## ステップ12：別のボタンを追加

- Claude Codeで次のように入力します：
  ```
  Add a 15-minute button.
  ```
- ブラウザタブを更新
- テスト：**15 min** ボタンをクリック

**このチュートリアルでは：** 15分ボタンが正しく動作しないふりをします。まだコミットしないでください。不適切な変更を破棄する練習をします。

## ステップ13：変更を破棄

AIのコードがうまく動作しないことがあり、最後のセーブポイントからやり直す必要があります。

- Claude Codeで次のように入力します：
  ```
  discard these changes.
  ```
- Claudeが確認を求めます
- `yes` と入力してEnterを押します
- ブラウザを更新すると、15分ボタンが消えます

Claudeが気に入らない新しい変更を破棄します。タイマーは1分と5分のボタンだけで再び動作します。

## ステップ14：サウンド通知を追加

- Claude Codeで次のように入力します：
  ```
  Add a sound notification when the timer reaches zero.
  ```
- Claudeの処理が終わったらブラウザを更新してテスト（タイマーを0.1分に設定）
- 動作する場合は、変更をコミットします：
  ```
  Save these changes.
  ```

## ステップ15：スヌーズボタンを追加

- Claude Codeで次のように入力します：
  ```
  The sound should continue until I click a button to snooze it.
  ```
- Claudeの処理が終わったらブラウザを更新してテスト（タイマーを0.1分に設定）
- 動作する場合は、変更をコミットします：
  ```
  Save these changes.
  ```

## ステップ16：コミット履歴を表示

- Claude Codeで次のように入力します：
  ```
  show my change history
  ```

Claudeがコミットを読みやすい形式で表示します。次のように表示されるはずです：
- 初期のタイマーアプリのコミット
- プリセットボタン（1分と5分）のコミット
- サウンド通知のコミット
- スヌーズボタン

15分ボタンの試みはありません。破棄したからです。

## ステップ17：コードを確認

- アプリを表示しているブラウザで、右クリックして **ページのソースを表示** を選択
- コードのソースを確認できます。
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

いつでも任意のコミットに戻ることができます。恐れずに破棄してください。動作するコードだけをコミットします。

## 次のステップ

タイマーにさらに機能を追加してみましょう：

- **15分ボタン：** `Add a working 15-minute preset button`（破棄したものをやり直します）
- **一時停止ボタン：** `Add a Pause/Resume button that toggles the timer state`
- **スタイル改善：** `Improve the visual design with a modern color scheme and larger fonts`
- **プログレスバー：** `Add a visual progress bar showing time remaining`

各機能の後にテストし、成功したらコミット、失敗したら破棄することを忘れないでください。

## トラブルシューティング

- **"not a git repository" エラー：** timerフォルダにいることを確認してください（`cd /mnt/c/Users/YOUR_USERNAME/Documents/timer`）
- **Windows上でtimer.htmlが見つからない：** ファイルは `C:\Users\YOUR_USERNAME\Documents\timer\timer.html` にあります
- **Gitがパスワードを要求する：** `sudo` パスワードの入力ミスです。注意深く再入力してください
- **タイマーが動作しない：** ブラウザコンソールを開いて（ページを右クリック、**検証** を選択、**Console** タブをクリック）、赤いエラーメッセージをコピーしてClaudeに貼り付けてください

## Claudeに依頼できること

- `what files have I changed?` - コミットされていない変更を確認
- `show me the diff` - 変更されたコードを正確に確認
- `explain what the timer code does` - 実装を理解
- `create a branch called experiment` - リスクのある変更を安全に試す
- `go back to the previous commit` - 最後のコミット以降のすべてを元に戻す

ClaudeはすべてのGit操作を自然言語で処理します。コマンドを覚える必要はありません。

## ワークフロー概要

- **セットアップ：** Gitを一度インストールし、身元情報を一度設定
- **開発：** Claudeがコードを書き、ブラウザでテスト
- **バージョン管理：** ClaudeがシンプルなリクエストですべてのGit操作を処理
- **安全性：** いつでも不適切な変更を破棄し、任意の過去のコミットに戻れる
- **ローカル：** すべてがコンピューター上で完結。アカウントやインターネット接続は不要

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2025年12月8日）
