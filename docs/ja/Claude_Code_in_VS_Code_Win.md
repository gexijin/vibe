---
title: "WindowsでClaude Code用にVS Codeをセットアップ"
lang: "ja"
---
[ホーム](./)

# WindowsでClaude Code用にVS Codeをセットアップ

WindowsにClaude Codeをインストールできたら、コードを編集するためのビジュアルエディターが欲しくなります。VS Codeなら、エディターでファイルを編集しながら、すぐ隣の統合ターミナルでClaude Codeを実行できます。すべてが1つのウィンドウにまとまります。

## 重要な概念

- **VS Code**：Microsoft製の無料エディター。ターミナルが組み込まれています。
- **統合ターミナル**：VS Code内にあるPowerShellターミナル。ウィンドウを切り替えずにClaude Codeを実行できます。
- **ワークスペースフォルダ**：VS Codeで開いたフォルダ。Claude Codeはこのフォルダ内のファイルを読み取り・編集します。

## 必要なもの

- [WindowsにClaude Codeをインストール](./Install_CLAUDE_Code_Win)済み
- [VS Codeを始めよう](./VS_Code_Getting_Started)を読了
- 10〜15分の作業時間

## ステップ1：プロジェクトフォルダを作成

- **エクスプローラー**（File Explorer、タスクバーのフォルダアイコン）を開く
- **ドキュメント**（Documents）フォルダへ移動
- 何もない場所を右クリック → **新規作成 > フォルダー**（New > Folder）
- フォルダ名を `test_claude` にする

## ステップ2：VS Codeを起動

- **Windowsスタートボタン**（タスクバーのWindowsロゴ）をクリック
- 検索ボックスに `Visual Studio Code` または `VS Code` と入力
- 検索結果の **Visual Studio Code** をクリック
- 起動直後に表示されるWelcomeタブは閉じてかまいません

## ステップ3：フォルダを開く

- VS Codeメニューバーから **File > Open Folder**（ファイル > フォルダーを開く）をクリック
- **ドキュメント** へ移動し、`test_claude` フォルダを選択
- **フォルダーの選択**（Select Folder）をクリックするとVS Codeが `test_claude` フォルダを読み込み直します
- 「Do you trust the authors?」（作成者を信頼しますか？）と表示されたら **Yes, I trust the authors**（はい、作成者を信頼します）を選択

## ステップ4：Claude Codeを起動

- VS Codeが読み込み直されたら、新しいターミナルを開きます：メニューバーの **Terminal > New Terminal**（ターミナル > 新しいターミナル）をクリック
- 下部に開いたターミナルで次を入力：
  ```
  claude
  ```

[インストールチュートリアル](Install_CLAUDE_Code_Win.md)に従って、Claudeサブスクリプションでログインしてください。ログイン後、ウェルカムメッセージとClaude Codeのプロンプトが表示されます。

## ステップ5：動作テスト

Claude Codeの入力欄に以下を入力してみましょう：
```
LLMがMarkdown形式を好む理由を説明する短い記事を書き、article.mdとして保存してください。
```
- Claude Codeがファイルを作成すると、左側のエクスプローラーに `article.md` が表示されます
- エクスプローラーで `article.md` をクリックすると、エディターで内容を確認できます
- 整形された記事をプレビューするには：`article.md` のエディター内を右クリックし、**Markdown Preview Enhanced: Open Preview to the Side** を選択（[VS Codeを始めよう](./VS_Code_Getting_Started)で入れた拡張機能です）。この拡張機能が入っていない場合は、代わりに `article.md` タブを右クリックして **Open Preview**（プレビューを開く）を選択
- 見出しや箇条書きなどが整形されたMarkdownが表示されます

## 後からVS Codeで再開するには

VS Codeを閉じた後、プロジェクトに戻る方法は次のとおりです：

- **方法A：** VS Codeを起動 → **File > Open Recent**（ファイル > 最近使用した項目を開く）で `test_claude` を選択
- **方法B：** **エクスプローラー**で `test_claude` フォルダを右クリックし、**Code で開く**（Open with Code）を選択（Windows 11では、先に **その他のオプションを確認**（Show more options）をクリック）。このオプションは、VS Codeのインストール時に **"Code で開く" アクションを追加する**（Add "Open with Code" action）にチェックを入れた場合にのみ表示されます。表示されない場合は方法Aを使ってください

## 次のステップ

- 既存プロジェクトの説明を依頼：「このプロジェクトが何をするのか説明してください」
- 新機能を追加：「リストの平均を計算する関数を追加してください」
- バグ修正を依頼：「このコードのエラーを修正してください」
- Claude Code拡張機能を試して、インライン差分付きのビジュアルなチャットパネルを使う。VS Codeのターミナルで `claude` を実行すると、通常は拡張機能が自動でインストールされます（されない場合は、拡張機能で「Claude Code」を検索）。任意のファイルを開き、エディターの右上にあるSparkアイコンをクリックします

## トラブルシューティング

- **`claude` が認識されない**：VS Codeを完全に閉じて（すべてのウィンドウ）もう一度開き、新しいターミナルを開いて `claude` を試してください。それでも失敗する場合は、通常のPowerShellウィンドウで `claude --version` を実行します。それも失敗する場合は、まず[インストール手順](Install_CLAUDE_Code_Win.md)に従ってください。
- **WSLを使っている場合**：オプションのWSL/Ubuntuの方法を設定した場合は、拡張機能サイドバーから **WSL** 拡張機能をインストールし、左下の **><** アイコンをクリックして **Connect to WSL**（WSLに接続）を選択してから、プロジェクトフォルダを開いてください（パスは `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude`）。

## ワークフローまとめ

- **VS Code**：Windows上で動作し、エディターを提供
- **統合ターミナル**：VS Code内でそのまま`claude`を実行
- エディターで編集しつつ、ターミナルでClaudeと会話 —— 両方のいいとこ取りです。

---

作成者：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)（2025年12月10日）
