---
title: "Claude Desktopアプリをインストール"
lang: "ja"
---
[ホーム](./)

# Claude Desktopアプリをインストール

Claude Desktopは、WindowsとMacで使える単独のチャットアプリです。アプリを開いてメッセージを入力すれば、Claudeが答えてくれます。Terminalもコマンド入力も必要ありません。日常的な質問、調べもの、文章作成などでClaudeとチャットするのにぴったりです。

これは、このサイトの他のチュートリアルで使っている**Claude Code**とは別のものです。Claude CodeはTerminal上で動作し、プロジェクトフォルダ内のコードの作成や編集を手伝います。Claude Desktopは汎用のチャットウィンドウです。両方インストールすることもでき、有料プランならClaude Desktopの中からClaude Codeを開くこともできます。

## 主要な概念

- **Claude Desktop**：WindowsとMac用のネイティブアプリです。メッセージアプリのように、Claudeと直接チャットできます。
- **Claude.aiアカウント**：サインインに使うアカウントで、[claude.ai](https://claude.ai)で使うものと同じです。無料プランでも有料プランでも使えます。
- **Claude Code**：このサイトの他のチュートリアルで扱っている、Terminalベースのコーディングアシスタントです。インストールは別に必要です。[WindowsにClaude Codeをインストール](./Install_CLAUDE_Code_Win.md)または[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS.md)を参照してください。

## 用意するもの

- Windows 10以降、またはMac（macOS 11 Big Sur以降）のコンピュータ
- インターネット接続
- 無料または有料のClaude.aiアカウント（持っていない場合はセットアップ中に作成できます）
- 5分

## ステップ1：インストーラーをダウンロードする

- [claude.ai/download](https://claude.ai/download)にアクセス
- **Windows：** **Download for Windows**をクリックします。（ARMベースのWindows PCを使っている場合は（あまり一般的ではありません）、ページにある別のarm64用ダウンロードリンクを使ってください。）
- **Mac：** **Download for macOS**をクリックします。このダウンロードはIntelとApple Siliconの両方のMacで動作するので、自分のMacのチップの種類を知らなくても大丈夫です。

## ステップ2：アプリをインストールする

### Windows

- ダウンロードしたファイルを開きます（自動で開かない場合は**ダウンロード**フォルダを確認してください）
- インストーラーの画面の指示に従います
- 完了したら、スタートメニューから**Claude**を探します

### Mac

- ダウンロードしたファイルを開きます
- 表示されたら、**Claude**アイコンを**アプリケーション**フォルダにドラッグします
- **アプリケーション**フォルダまたはLaunchpadから**Claude**を開きます

## ステップ3：サインインする

- Claudeアプリを起動します
- 画面の指示に従って、Claude.aiアカウントでログインします
- アカウントを持っていない場合は、先に[claude.ai](https://claude.ai)で無料アカウントを作成してから、戻ってサインインしてください

## ステップ4：最初のメッセージを送る

- メッセージ入力欄をクリックします
- たとえば`何を手伝ってもらえますか？`のように入力します
- **Enter**キーを押して送信します
- Claudeがアプリのウィンドウ内で返信します

## ステップ5：（オプション）Claude Desktopでできる他のことを見てみる

Claude Desktopはチャットだけのものではありません。プランによって次の機能が使えます：

- **チャット** — 無料プランを含むすべてのプランで利用できます
- **Claude Code** — Pro、Max、Team、EnterpriseプランではClaude Desktopの中からClaude Codeを起動でき、別のTerminalを開く必要がありません
- **Claude Cowork** — 有料プランでは、ローカルファイルにアクセスしながら、Claudeに複数ステップのタスクを任せられます
- **Desktop Extensions** — インストール可能な拡張機能のディレクトリを通じて、Claudeをローカルのアプリやファイルにつなぐ上級者向け機能です。始めるのに必要はありません

日常的なチャットにClaude Desktopを使うだけなら、これらはどれも必要ありません。基本に慣れてきたら試してみる価値があります。

## 次のステップ

- [WindowsにClaude Codeをインストール](./Install_CLAUDE_Code_Win.md)または[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS.md) — このサイトの他のチュートリアルで使う、Terminalベースのコーディングアシスタントをセットアップします
- [Claude Code: 基本操作](./Claude_Code_Basic_Operations.md) — Claude Codeをインストールしたら、基本を学びましょう
- [AnthropicとClaudeとは？](./What_Is_Anthropic_And_Claude.md) — Claudeをまったく初めて使う方向けの簡単な入門です

## トラブルシューティング

- **Windowsで「WindowsによってPCが保護されました」というメッセージが出てインストーラーがブロックされる** — これは新しくダウンロードしたファイルに対するWindows標準のSmartScreen警告で、Claudeに限ったものではありません。配布元（公式のclaude.ai/downloadページ）を信頼できる場合は、**詳細情報**をクリックしてから**実行**をクリックします。
- **Macで「開発元が未確認のため開けません」と表示される** — これはmacOSの標準的なセキュリティチェックであるGatekeeperです。Claudeアプリを右クリック（またはControlキーを押しながらクリック）して**開く**を選び、確認します。
- **サインインできない** — インターネット接続を確認し、まずブラウザで[claude.ai](https://claude.ai)にログインできるか確かめてください。
- **インストール後にアプリが起動しない** — コンピュータを再起動してから、もう一度Claudeを開いてみてください。それでも解決しない場合は、[claude.ai/download](https://claude.ai/download)からインストーラーをダウンロードし直してください。

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2026年9月18日に作成。
