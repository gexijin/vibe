---
title: "VS Codeを始めよう"
lang: "ja"
---
[ホーム](./)

# VS Codeを始めよう

メモ帳やテキストエディットでは色分けも補完もなくて不便——そんなときに頼れるのが[Visual Studio Code](https://code.visualstudio.com)（VS Code）です。**VS Codeはコード用のスマートノート**。書いている内容を理解し、ハイライトや補完、便利な拡張機能で作業を手助けしてくれます。しかも無料で、Windows / macOS / Linuxすべてに対応し、世界中の何百万人もの開発者に使われています。

## キー概念

- **エディター**：中央の編集画面。ここにコードを入力
- **エクスプローラー**：左側のファイル/フォルダ一覧
- **拡張機能**：VS Codeに機能を追加するアドオン
- **統合ターミナル**：VS Code内で使えるコマンドライン

## 必要なもの

- Windows / macOS / Linux いずれかのPC
- インターネット接続
- 約500MBのディスク空き
- 作業時間 20〜25分

## ステップ1：VS Codeをダウンロード＆インストール

- [code.visualstudio.com](https://code.visualstudio.com) を開く
- OSを自動判別した **Download** ボタンをクリック
- インストーラーを実行
   - **Windows**：`.exe` をダブルクリック → 画面の指示に従い **Next** を押していく。**追加タスクの選択**（Select Additional Tasks）画面では、**エクスプローラーのディレクトリ コンテキスト メニューに [Code で開く] アクションを追加する**（Add "Open with Code" action to Windows Explorer directory context menu）にもチェックを入れておくと、後でエクスプローラーからプロジェクトフォルダを開けます
   - **Mac**：`.dmg` を開き、VS Code を **Applications** フォルダにドラッグ
   - **Linux**：パッケージマネージャーの案内に従う
- VS Codeを起動

はじめに使えるオプションが並んだWelcomeタブが表示されます。

## ステップ2：画面構成を見てみる

VS Codeは主に5つの領域で構成されています。

- **アクティビティバー**（最左列）：エクスプローラー、検索、Git、拡張機能などのアイコン
- **サイドバー**：選択したアクティビティに応じてファイル一覧や検索結果を表示
- **エディター**（中央）：コードを書く場所
- **パネル**（下部）：ターミナル、Problems、Output など
- **ステータスバー**（最下部）：ファイルやプロジェクトに関する情報

アクティビティバー上部の **エクスプローラー** アイコンをクリックすると、ファイルブラウザが表示されます。

## ステップ3：フォルダを開いて探索

- **File** → **Open Folder**（ファイル → フォルダーを開く）をクリック
- **書類**（Documents）フォルダに移動し、練習用の新しい空のフォルダ（例：`vscode_practice`）を作成（ウィンドウ内の **新規フォルダ**（New Folder）ボタンを使います）
- その新しいフォルダを選択し、**開く**（Open）をクリック（Windowsではボタン名が **フォルダーの選択**（Select Folder）の場合があります）
- 「Do you trust the authors?」（作成者を信頼しますか？）と表示されたら **Yes, I trust the authors**（はい、作成者を信頼します）をクリック

エクスプローラーサイドバーにフォルダ内のファイルが表示されます：

- フォルダをクリックして展開
- 任意のファイルをクリックしてエディターで開く
- アクティビティバーの **検索** アイコン（虫眼鏡）をクリックすると、すべてのファイルを横断検索できます

## ステップ4：Markdownファイルを作ってみる

- エクスプローラーで上部のフォルダ名にマウスを合わせ、表示される **New File**（新しいファイル）アイコン（+付きページ）をクリック
- ファイル名を `README.md` に設定
- 以下の内容を追加：

```
# My Project

This is a **demo project** for learning VS Code.

## Features
- Easy to edit
- Markdown formatting
- Live preview

## Next Steps
1. Add more content
2. Try other file types
3. Explore extensions
```
- **File** → **Save**（ファイル → 保存）をクリックして保存

Markdownは `#` で見出し、`**` で太字、`-` でリストを表す簡単なテキスト記法で、ドキュメントやChatGPTやClaudeなどのLLMとのコミュニケーションに広く使われています。

## ステップ5：Markdown Preview拡張機能をインストール

- アクティビティバーの **Extensions**（拡張機能）アイコン（四角いアイコン）をクリック
- 検索欄に `Markdown Preview Enhanced` と入力
- 検索結果から **Markdown Preview Enhanced** を見つける
- **Install** をクリック

## ステップ6：Markdownファイルをプレビュー

- `README.md` がまだ開いていない場合は開く
- エディター内を右クリックし、**Markdown Preview Enhanced: Open Preview to the Side** を選択

フォーマットされたMarkdownを表示するプレビューパネルが開きます。左で編集、右でリアルタイムに変更を確認できます！

## ステップ7：統合ターミナルを使う

- **Terminal** → **New Terminal**（ターミナル → 新しいターミナル）をクリック
- 以下のコマンドを試してみましょう：

**ファイル一覧を表示：**
```
ls
```
（Windowsのコマンドプロンプトでは `dir` を使用）

**作業ディレクトリを表示：**
```
pwd
```
（Windowsのコマンドプロンプトでは `cd` を使用）

**新しいフォルダを作成：**
```
mkdir notes
```

エクスプローラーを確認すると、`notes` フォルダが表示されます！ターミナルはプロジェクトフォルダ内で実行されるため、コマンドはプロジェクトに直接影響します。

## ステップ8：VS CodeでAIエージェントを使う（任意）

VS Codeには[GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)が搭載されており、コードの説明、作成、デバッグを支援するAIアシスタントです。

- `README.md` ファイル（またはプロジェクト内の他のファイル）を開く
- タイトルバーの **Chat > Open Chat** をクリック（またはWindows/Linuxでは `Ctrl+Alt+I`、Macでは `Ctrl+Cmd+I` を押す）
- サインインを求められたら、**GitHubアカウント**でサインイン（無料プランも利用可能）
- 開いたチャットパネルに「このファイルを説明してください」と入力
- **Enter**を押す

GitHub Copilotがファイルを分析し、その内容を説明します。新しいコードの作成、バグの修正、機能追加の方法などについて質問することも可能です。

**ヒント：** [インライン編集](https://code.visualstudio.com/docs/chat/inline-chat)を使う場合は、任意のファイルでコードをハイライトし、`Ctrl+I`（Windows/Linux）または `Cmd+I`（Mac）を押すと、Copilotにその部分のみの変更、修正、説明を依頼できます。

## プロジェクトを再度開くには

- スタートメニュー（Windows）、Spotlight（Mac）、アプリケーション（Linux）からVS Codeを開く
- **File > Open Recent**（ファイル > 最近使用した項目を開く）→ フォルダを選択
- または **File > Open Folder** で移動して選択

## トラブルシューティング

- **プレビューが表示されない：** Markdown Preview Enhanced拡張機能がインストールされており、`.md` ファイルを開いていることを確認してください
- **ターミナルに間違ったディレクトリが表示される：** ターミナルパネルのゴミ箱アイコンをクリックし、**Terminal > New Terminal** をクリックします
- **Chatメニューが表示されない：** AI機能がオフになっている可能性があります。設定を開き（Windows/Linuxでは`Ctrl+,`、Macでは`Cmd+,`）、`disable AI features`を検索してチェックを外します。次に、ステータスバー（下部）のCopilotアイコンにマウスを合わせ、**Use AI Features**を選択します
- **拡張機能が動作しない：** **View > Command Palette**（表示 > コマンド パレット）をクリックし、「reload window」と入力して **Developer: Reload Window** を選択します

## 完全なワークフロー

1. VS Codeでフォルダを開く
2. ファイルを作成／編集
3. 拡張機能を使ってプレビュー
4. ターミナルでコマンドを実行
5. AIを使ってコードを理解・改善
6. 保存して繰り返す

## 次のステップ

- **他のファイルタイプを試す：** `.html`、`.css`、`.js`、`.py` ファイルを作成して、VS Codeのシンタックスハイライトを確認
- **AI機能を探索：** AIにコードの作成、バグの修正、プロジェクトの改善提案を依頼
- **さらに拡張機能をインストール：** 自動フォーマット用の「Prettier」やGit機能用の「GitLens」を試す
- **ショートカットを学ぶ：** **Help > Keyboard Shortcuts Reference** をクリックして、ワークフローを高速化

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2025年12月7日）
