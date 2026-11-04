---
title: "MacでVS CodeからClaude Codeを使う"
lang: "ja"
---
[ホーム](./)

# MacでVS CodeからClaude Codeを使う

MacにClaude Codeを入れたら、次は「ファイルを編集しながらClaudeと会話したい」という場面が増えます。Visual Studio Code (VS Code) を使えば、エディターとターミナルが1ウィンドウに収まり、片側でファイルを編集しつつ、もう片側で`claude`を操作できます。

## キーコンセプト

- **VS Code**：Microsoft製の無料エディター。Macで動き、拡張機能も豊富
- **統合ターミナル**：VS Code下部にあるターミナルパネル。ここで`claude`を実行
- **エクスプローラーパネル**：左側のファイルツリー。Claudeが作ったファイルも即座に表示されます

## 必要なもの

- [MacにClaude Codeをインストール](./Install_Claude_Code_MacOS) を完了
- [VS Codeを始めよう](./VS_Code_Getting_Started) を完了
- 作業時間の目安：10〜15分

## ステップ1：VS Codeを起動

- **Finder** を開き、**アプリケーション**（Applications）に移動
- **Visual Studio Code** を見つけてダブルクリック
- 「Visual Studio Code はインターネットからダウンロードされたアプリケーションです」という警告が表示された場合は、**開く**（Open）をクリック
- Welcomeタブが開きます - このタブは閉じてもかまいません

**ヒント：** 後で簡単にアクセスできるように、Dock内のVS Codeを右クリックして **オプション > Dockに追加**（Options > Keep in Dock）を選択してください。

## ステップ2：作業用フォルダを作成

- **Finder** を開く
- 左サイドバーの **書類**（Documents）をクリック
- メニューバーの **ファイル**（File）をクリックし、次に **新規フォルダ**（New Folder）をクリック
- フォルダに `test_claude` と名前を付ける

## ステップ3：VS Codeでフォルダを開く

- VS Codeで、メニューバーの **File** をクリックし、次に **Open Folder**（フォルダーを開く）をクリック
- **書類** に移動し、作成した `test_claude` フォルダを選択
- **開く**（Open）をクリック
- 「Do you trust the authors of the files in this folder?」（このフォルダー内のファイルの作成者を信頼しますか？）と表示された場合は、**Yes, I trust the authors**（はい、作成者を信頼します）をクリック

左側のエクスプローラーパネルに `TEST_CLAUDE` が表示されます。

## ステップ4：Claude Codeを起動してログイン

- 新しいターミナルを開く：メニューバーの **Terminal** をクリックし、次に **New Terminal**（新しいターミナル）をクリック
- VS Codeの下部にターミナルパネルが表示されます
- ターミナルで、次のように入力：
  ```
  claude
  ```
- Claude Codeからログインを求められた場合は、[インストールチュートリアル](./Install_Claude_Code_MacOS)のログイン手順に従ってください。Claude Codeには有料のClaudeプラン（ProやMaxなど）またはAnthropic Consoleアカウントが必要です。無料プランには含まれていません。
- ウェルカムメッセージとClaude Codeのプロンプトが表示されます
- これで、VS Codeでファイルを編集しながらClaude Codeを使用できます

**注意：** ログインは一度だけで大丈夫です。次回以降はすぐにウェルカムメッセージが表示されます。

## ステップ5：ワークフローをテスト

- Claude Codeで、次のように入力：
```
LLMがMarkdown形式を好む理由を説明する短い記事を書き、article.mdとして保存してください。
```
- Claude Codeがファイルを作成します - 左側のエクスプローラーパネルに `article.md` が表示されます
- エクスプローラーで `article.md` をクリックすると、エディターで表示されます
- 整形された記事をプレビューするには：`article.md` のエディター内を右クリックし、**Markdown Preview Enhanced: Open Preview to the Side** を選択（[VS Codeを始めよう](./VS_Code_Getting_Started)で入れた拡張機能です）。この拡張機能が入っていない場合は、代わりに `article.md` タブを右クリックして **Open Preview**（プレビューを開く）を選択
- 適切な見出し、箇条書き、フォーマットでレンダリングされたMarkdownが表示されます

## 後でVS CodeでClaudeを再度開く

VS Codeを閉じた後、プロジェクトに戻る方法は次のとおりです：

- **方法A：** VS Codeを開き、**File > Open Recent**（ファイル > 最近使用した項目を開く）をクリックし、`test_claude` を選択
- **方法B：** ターミナルを開き、`cd ~/Documents/test_claude` でプロジェクトに移動し、`code .` と入力

VS Codeは最近使用したフォルダを記憶しているため、通常は「Open Recent」を使用する方法Aが最も早いです。

## 次のステップ

- Claude Codeに既存のコードベースの説明を依頼：「このプロジェクトが何をするのか説明してください」
- Claude Codeに新しい機能の作成を依頼：「リストの平均を計算する関数を追加してください」
- Claude Codeを使用してバグを修正：「このコードがエラーを出します。修正してもらえますか？」
- Claude Code拡張機能を試して、インライン差分付きのビジュアルなチャットパネルを使う。VS Codeのターミナルで `claude` を実行すると、通常は拡張機能が自動でインストールされます（されない場合は、拡張機能で「Claude Code」を検索）。任意のファイルを開き、エディターの右上にあるSparkアイコンをクリックします

## トラブルシューティング

- **ターミナルに「zsh」と表示されるが、Claude Codeが起動しない** - Claude Codeが正しくインストールされているか確認してください。`claude --version` を実行して確認します
- **ターミナルで「code」コマンドが見つからない** - VS Codeで、メニューバーの **View** をクリックし、次に **Command Palette**（コマンド パレット）をクリックして、「shell command」と入力し、**Shell Command: Install 'code' command in PATH** を選択します
- **VS Codeが不明な開発者からのものとして開けない** - **システム設定 > プライバシーとセキュリティ**（System Settings > Privacy & Security）に移動し、**このまま開く**（Open Anyway）をクリックします

## ワークフローの概要

- **VS Code** はビジュアルエディターインターフェースを提供します
- **統合ターミナル** はVS Code内でClaude Codeを実行します
- ファイルは書類フォルダ（または選択した場所）に保存されます
- エディターでファイルを編集し、ターミナルでClaude Codeとチャット - 両方の長所を活用できます

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2025年12月10日）
