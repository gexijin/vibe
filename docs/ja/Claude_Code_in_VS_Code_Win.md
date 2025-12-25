[ホーム](./)

# WSLでClaude Code用にVS Codeをセットアップ

WSLとClaude Codeの準備ができたら、コードを編集するためのビジュアルエディターが欲しくなります。VS CodeはWindowsとLinux環境をつなぎ、エディターでファイルを編集しながら統合ターミナルでClaude Codeを実行できます。VS Codeを「Linux環境への窓」と考えてください。

## 重要な概念

- **VS Code**：Windowsで動くMicrosoft製の無料エディター。WSLに接続してLinux側のファイルも扱えます。
- **WSL拡張機能**：VS CodeにWSLへの接続機能を追加。Linuxツール（Claude Codeなど）をそのまま使えます。
- **統合ターミナル**：VS Code内にあるターミナル。WSLのUbuntuで実行されるため、`claude`もここで実行可能。
- **/mnt/c/**：WSLからWindowsファイルへアクセスするパス（例：`/mnt/c/Users/...` = `C:\Users\...`）。

## 必要なもの

- [WindowsでClaude Codeをインストール](./Install_CLAUDE_Code_Win)済み
- [VS Codeの基本](./VS_Code_Getting_Started)を読了
- 10〜15分の作業時間

## ステップ1：プロジェクトフォルダを作成

1. **エクスプローラー**（タスクバーのフォルダアイコン）を開く
2. **ドキュメント**フォルダへ移動
3. 何もない場所を右クリック → **新規作成 > フォルダー**
4. フォルダ名を `test_claude` にする

## ステップ2：VS Codeを起動

1. **Windowsスタートボタン**をクリックし、`Visual Studio Code` または `VS Code` を検索
2. 検索結果の **Visual Studio Code** をクリック
3. 起動直後に表示されるWelcomeタブは閉じてかまいません

## ステップ3：WSL拡張機能をインストール

1. VS Code左サイドバーの**拡張機能**（四つの正方形アイコン）をクリック
2. 検索ボックスに `WSL` と入力
3. Microsoft製の **WSL** 拡張機能を選び、**インストール**をクリック
4. 数秒で完了します

## ステップ4：WSLに接続

1. VS Code左下のステータスバーにある青/緑のアイコンをクリック（または `F1` を押して「WSL」と入力）
2. **WSLに接続** を選択
3. VS Codeが再読み込みされ、Ubuntuに接続されます
4. 左下に **WSL: Ubuntu** と表示されれば成功。

初回接続時はWSL側に小さなサーバーがインストールされるため、30秒ほど待ちます。

## ステップ5：フォルダを開く

1. VS Codeメニューバーから **ファイル > フォルダーを開く** をクリック
2. 表示されたパス入力ボックスに以下を入力：
   ```
   /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
   ```
   ※ `YOUR_USERNAME` を自分のWindowsユーザー名に置き換える
3. **OK** を押すとVS Codeが `test_claude` フォルダを読み込みます
4. 「作成者を信頼しますか？」と表示されたら **はい** を選択

## ステップ6：Claude Codeを起動

1. メニューバーの **ターミナル > 新しいターミナル** をクリック
2. 下部に開いたターミナルで次を実行：
   ```
   claude
   ```

[インストールチュートリアル](Install_CLAUDE_Code_Win.md)に従って、Claudeサブスクリプションでログインしてください。ログイン後、ウェルカムメッセージとClaude Codeのプロンプトが表示されます。

## ステップ7：動作テスト

Claude Codeの入力欄に以下を入力してみましょう：
```
LLMがMarkdown形式を好む理由を説明する短い記事を書き、article.mdとして保存してください。
```
- 数秒後、左側のエクスプローラーに `article.md` が表示されます
- ファイルをクリックすると内容を編集・確認できます
- プレビューしたい場合はタブを右クリックして **プレビューを開く** を選択すると、Markdownが整形表示されます

## 後からVS Codeで再開するには

- **方法A：** VS Codeを起動 → 左下アイコンから **WSLへ接続** → **ファイル > 最近使った項目** で `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude [WSL: Ubuntu]` を選択
- **方法B：** WindowsでUbuntuアプリを開き、プロジェクトフォルダへ移動して `code .` を実行

最近使ったフォルダに表示されるので、方法Aが最も早いことが多いです。

## 次のステップ

- 既存プロジェクトの説明を依頼：「このプロジェクトが何をするのか説明してください」
- 新機能を追加：「リストの平均を計算する関数を追加してください」
- バグ修正を依頼：「このコードのエラーを修正してください」
- 「Claude Code」拡張機能を検索し、インライン差分付きのビジュアルUIを試す
- 大きなファイルをより効率的に扱うには、WSLファイルシステム内（`/home/user/`）にフォルダを作成します。Windowsからアクセスする場合は、エクスプローラーのサイドバー下部にあるLinuxアイコンを探すか、アドレスバーに `\\wsl.localhost\` と入力してください。

## トラブルシューティング

- **左下に「WSL: Ubuntu」が表示されない**：まずUbuntuターミナルを起動してWSLが動作しているか確認。
- **ターミナルがPowerShellになる**：ターミナルペインの `+` 右側の矢印から **Ubuntu (WSL)** を選択し、既定シェルを切り替え。
- **`claude` が見つからない**：`claude --version` で確認。見つからない場合は[WSLインストール手順](./Install_CLAUDE_Code_Win)を再確認してください。

## ワークフローまとめ

- **VS Code**：Windows上で動作し、エディターを提供
- **WSL拡張機能**：VS CodeをUbuntuに接続し、Linuxコマンドを実行可能に
- **統合ターミナル**：Ubuntu上で`claude`を実行
- **ファイル配置**：Windows側（例：Documents）に置いたまま `/mnt/c/` 経由でアクセス
- エディターで編集しつつ、ターミナルでClaudeと会話 —— WindowsとLinuxのいいとこ取りです。

---

作成者：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)（2025年12月10日）
