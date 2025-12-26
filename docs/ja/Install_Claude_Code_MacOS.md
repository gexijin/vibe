[ホーム](./)

# MacにClaude Codeをインストール

Claude Codeは、ターミナル上で動作するAIアシスタントで、コードの作成、デバッグ、理解を支援します。いつでも相談できる頼れるコーディングパートナーのようなものです。完全な初心者でも経験豊富な開発者でも、Claude Codeはワークフローを加速し、学習を助けます。

このガイドでは、MacにClaude Codeをセットアップする手順を最初から最後まで説明します。初心者でも迷わないよう、各ステップを細かく分けて記載しています。

## 概要

- Node.jsをダウンロードしてインストール
- npmでClaude Codeをインストール
- APIキーを設定
- Claude Codeを使って作業開始

## 主要な概念

- **ターミナル**：ボタンをクリックする代わりにコマンドを入力するMac内蔵のアプリです。Claude Codeとのやり取りはここで行います。
- **Node.js**：Claude Codeを動かすために必要なソフトウェアです。Claude Codeを動かすエンジンのようなものです。
- **Claude Code**：ターミナルで実行するAIコーディングアシスタントです。質問に答えたり、コードを書いたり、既存のプロジェクトを理解するのを助けたりできます。

## 用意するもの

- Mac（macOS 10.15 Catalina以降を推奨）
- インターネット接続
- コンピュータの管理者権限
- Claude Pro/MaxサブスクリプションまたはAnthropic APIキー
- 15〜20分

## ステップ1：Node.jsをダウンロード

Claude CodeにはNode.js 18以上が必要です。まず現在の環境を確認しましょう。

**Node.jsが入っているか確認する：**

- Dockの**Launchpad**アイコン（カラフルな四角が並んだアイコン）をクリック
- 上部の検索ボックスに`ターミナル`と入力
- **ターミナル**（黒い四角アイコン）をクリック
- ターミナルで以下を入力：
  ```
  node --version
  ```
- 結果を確認：
  - **`v18.x.x`以上の数字が表示された場合**：Node.jsはすでにあります。**ステップ4**に進んでください。
  - **「command not found」と表示された場合**：続けてNode.jsをインストールします。

**Node.jsをダウンロードする：**

- Safari / Chrome / Firefox などのブラウザを開く
- 以下のURLを開く：
  ```
  https://nodejs.org/
  ```
- Node.jsのトップページが開いたら、緑の **Get Node.js** ボタンをクリック
- 画面中央の **macOS Installer (.pkg)** をクリック
- ダウンロードフォルダに`node-v24.x.x.pkg`のようなファイルが保存されます（30〜60秒程度）

## ステップ2：Node.jsをインストール

- Dockの青い顔アイコンから**Finder**を開く
- 左側の**ダウンロード**をクリック
- 先ほどの`node-v24.x.x.pkg`を見つけてダブルクリック
- インストーラーが開いたら手順に従う：
  - **続ける**をクリック
  - ライセンス画面でもう一度**続ける**→**同意する**
  - **インストール**をクリック
  - Macのログインパスワードを入力し、**ソフトウェアをインストール**
  - 1〜2分待ち、「インストールが成功しました」と表示されたら**閉じる**
  - メッセージが出た場合はインストーラをゴミ箱に移動してOK

## ステップ3：Node.jsが入ったか確認

- Dockの**Launchpad**アイコン（カラフルな四角が並んだアイコン）をクリック
- 上部の検索ボックスに`ターミナル`と入力
- **ターミナル**（黒い四角アイコン）をクリック
- ターミナルウィンドウが開きます
- ターミナルで以下を入力：
  ```
  node --version
  ```
- `v24.x.x`のような表示が出れば成功です（数字は多少違っていても問題ありません）
- バージョン番号が表示されれば、Node.jsは正しくインストールされています

**「command not found」が出た場合：**
- ターミナルを完全に終了します（メニューバーの**ターミナル**をクリックし、**ターミナルを終了**を選択）
- ターミナルを再度開きます
- もう一度コマンドを試してください

**ヒント：** 次のステップでもターミナルを使うので、開いたままにしておいてください。

## ステップ4：Claude Codeをインストール

- ターミナルで以下を入力：
  ```
  npm install -g @anthropic-ai/claude-code
  ```
- Claude Codeのインストールを待ちます（2〜5分）
- 「permission denied」エラーが表示された場合は、`sudo`を付けて試してください：
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
  その後、プロンプトが表示されたらMacのパスワードを入力します（入力中は表示されません）
- 黄色や赤のテキストで警告が表示される場合がありますが、通常は問題ありません
- インストールが完了したら、以下を入力して確認します：
  ```
  claude --version
  ```
- Claude Codeのバージョン番号が表示されるはずです

## ステップ5：Anthropicアカウントに接続

### オプションA. Claude ProまたはMaxサブスクリプションを使用

- ターミナルで以下を入力：
  ```
  claude
  ```
- Claudeがブラウザを開こうとします。自動的に開かない場合は、ターミナルに表示されたURLをコピーしてブラウザに貼り付けてください。
- Claude.aiアカウントにログインします（自動的にログインされる場合もあります）
- **Authorize**をクリック
- 長いコードが表示されたら**Copy Code**をクリック
- ターミナルウィンドウに戻ります
- ターミナルに貼り付けるには：メニューバーの**編集**をクリックし、次に**貼り付け**をクリック
- 成功メッセージが表示されるはずです
- 指示に従ってセットアップを完了してください

### オプションB. Anthropic APIキーを使用

Claudeサブスクリプションの代わりにAnthropic APIキーを使用する場合：

- まず、[Anthropic Console](https://console.anthropic.com/)からAPIキーを取得します
- ターミナルで以下を入力：
  ```
  export ANTHROPIC_API_KEY="your-api-key-here"
  ```
  `your-api-key-here`を実際のAPIキーに置き換えてください
- これを永続的にする（毎回設定する必要がないようにする）には、シェルプロファイルに追加します：
  ```
  echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
  ```
  `your-api-key-here`を実際のAPIキーに置き換えてください
- 変更を有効にするため、ターミナルを閉じて再度開いてください

**注意：** bashを使用している古いMacの場合は、上記のコマンドで`~/.zshrc`を`~/.bash_profile`に置き換えてください。

### オプションC. OpenRouter APIを使用（無料で始められます！）

OpenRouterは、500以上の大規模言語モデルに単一のAPIキーでアクセスできる統合APIゲートウェイです。使用量に応じた課金で、さまざまな価格帯のモデルから選択できるため、Claude Codeを経済的に使用する方法となります。

- [openrouter.ai](https://openrouter.ai)でサインアップしてログイン
- **Get API key**をクリックしてキーを安全な場所にコピー
- Claude Codeを起動する前に、必要な環境変数を設定：
  ```
  export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
  export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
  export ANTHROPIC_API_KEY=""
  export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
  export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
  export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
  ```
- Claude Codeを起動：
  ```
  claude
  ```
- Claude Codeで`/status`と入力して接続を確認

**注意：**
- `your-openrouter-api-key`を実際のOpenRouter APIキーに置き換えてください
- `ANTHROPIC_API_KEY`は明示的に空に設定する必要があります
- 代替モデルを使用する場合は、**ツール使用機能**をサポートしている必要があります。モデルは以下で上書きできます：
  ```
  export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
  ```
- 利用可能なモデルは[openrouter.ai/models](https://openrouter.ai/models)で確認できます
- 無料プランでは1日50回のAPIリクエストが可能です
- 詳細は[公式OpenRouterガイド](https://openrouter.ai/docs/guides/claude-code-integration)を参照してください


### オプションD. Azure Foundry経由でAnthropic APIを使用

このオプションは、Azure上でClaudeモデルをホストしている組織向けです。Claudeを起動する前に、ターミナルウィンドウで以下のコードを貼り付けて環境変数を定義します：
```
# Microsoft Foundry統合を有効化
export CLAUDE_CODE_USE_FOUNDRY=1
# Azureリソース名
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# モデルをリソースのデプロイメント名に設定
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**注意：** `xxxx-eastus2`を実際のFoundryリソース名に置き換えてください（ベースURL全体ではなく、リソース名のみ）。`your_api_key`をAzureポータルから取得した完全なAPIキーに置き換えてください。

## ステップ6：Claude Codeを使い始める

これで準備完了です！Claude Codeの使い方は次のとおりです：

- ターミナルで以下を入力：
  ```
  claude
  ```
- チャットの準備をする前にいくつか質問されます
- 動作を確認するには、次のような一般的な質問をしてみてください：
  ```
  量子コンピューティングについて説明してください
  ```

## ステップ7：プロジェクトに移動する

- Macのフォルダにプロジェクトがある場合は、そこに移動できます：
  ```
  cd ~/Documents/test_claude
  ```
  `test_claude`を実際のプロジェクトフォルダ名に置き換えてください

- 次にClaudeを起動します：
  ```
  claude
  ```
- まずは、Claudeにコードベースについて説明してもらうことから始めましょう：
  ```
  このプロジェクトの構造を説明してください
  ```
- Claudeに変更を依頼できます：
  ```
  このコードをリファクタリングして、読みやすくしてください
  ```
- お好みのIDEでコードをテストしてください。

**注意：** Claudeはプロジェクトフォルダ内で動作します。フォルダ内で書き込み権限を定義し、そのフォルダに設定を保存します。これがClaudeのワークスペースです。

## 次のステップ
- [VS Code入門](./VS_Code_Getting_Started.md) - 人気のコードエディタVS Codeの使い方を学ぶ
- [VS CodeでClaude Code（Mac）](./Claude_Code_in_VS_Code_Mac.md) - VS Code内でClaude Codeを実行
- [Claude Codeで研究論文を書く](./Writing_Research_Paper_Claude_Code.md) - 学術論文執筆にClaude Codeを使用

## ターミナルを再度開く方法

ターミナルを閉じた後、再度開く方法は次のとおりです：

- Dockの**Launchpad**アイコン（カラフルな四角が並んだアイコン）をクリック
- 上部の検索ボックスに`ターミナル`と入力
- **ターミナル**をクリック
- ターミナルウィンドウが開きます

## トラブルシューティング

### Node.jsインストーラーが開かない
- nodejs.orgからダウンロードした`.pkg`ファイルか確認してください
- ダブルクリックではなく右クリック > **開く**を試してください
- **システム設定** > **プライバシーとセキュリティ**の下部にある**このまま開く**をクリックしてください

### インストール後に「node: command not found」と表示される
- ターミナルを完全に終了します（メニューバーの**ターミナル**をクリックし、**ターミナルを終了**を選択）
- ターミナルを再度開きます
- もう一度`node --version`を試してください
- それでもうまくいかない場合は、Macを再起動して再度試してください

### npmインストールがパーミッションエラーで失敗する
- npmコマンドの前に`sudo`を付けます：
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
- プロンプトが表示されたらMacのパスワードを入力してください（入力中は表示されません）

### Claude Codeコマンドが見つからない
- npmのインストールが正常に完了したことを確認してください
- ターミナルを閉じて再度開いてみてください
- Claude Codeがインストールされているか確認します：`npm list -g @anthropic/claude-code`
- 再度インストールしてみてください：`npm install -g @anthropic-ai/claude-code`

### 「Cannot find module」エラー
- Node.jsが正しくインストールされていることを確認してください：`node --version`
- Claude Codeを再インストールしてみてください：`npm uninstall -g @anthropic/claude-code`を実行してから`npm install -g @anthropic-ai/claude-code`を実行

## Macユーザー向けのヒント

### プロジェクトパスを見つける
フォルダへのパスを見つけるには：
- Finderを開きます
- プロジェクトフォルダに移動します
- フォルダをターミナルにドラッグ＆ドロップすると、フルパスが表示されます！

### 別のターミナルアプリを使用する
他のターミナルアプリも使用できます：
- iTerm2（より多くの機能を持つ人気の代替品）
- Warp（AI機能を備えたモダンなターミナル）
- Hyper（クロスプラットフォームターミナル）

Claude Codeはすべてのターミナルで動作します！

## 困ったときは

- Node.jsのダウンロード：[Node.js公式ウェブサイト](https://nodejs.org/)
- Node.jsの問題：[Node.jsドキュメント](https://nodejs.org/docs/)
- npmの問題：[npmドキュメント](https://docs.npmjs.com/)
- Claude Codeの問題：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

*最終更新：2025年12月*
