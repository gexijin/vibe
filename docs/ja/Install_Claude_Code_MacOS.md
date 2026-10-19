---
title: "MacにClaude Codeをインストール"
lang: "ja"
---
[ホーム](./)

# MacにClaude Codeをインストール

Claude Codeは、ターミナル上で動作するAIアシスタントで、コードの作成、デバッグ、理解を支援します。いつでも相談できる頼れるコーディングパートナーのようなものです。完全な初心者でも経験豊富な開発者でも、Claude Codeはワークフローを加速し、学習を助けます。

このガイドでは、初心者にもわかりやすいよう、インストール手順をステップごとに詳しく説明します。

## 概要

- ターミナルを開く
- Claude Codeをインストール
- API接続を設定
- Claude Codeを使い始める

## 主要な概念

- **ターミナル**（Terminal）：ボタンをクリックする代わりにコマンドを入力するMac内蔵のアプリです。Claude Codeとのやり取りはここで行います。
- **Claude Code**：ターミナルで実行するAIコーディングアシスタントです。質問に答えたり、コードを書いたり、既存のプロジェクトを理解するのを助けたりできます。

## 用意するもの

- Mac（macOS 13.0 Ventura以降）
- インターネット接続
- Claude Pro/MaxサブスクリプションまたはAPIキー
- 5〜10分

## ステップ1：ターミナルを開く

- **Command (⌘) + Space**を押してSpotlight検索を開く
- `ターミナル`と入力
- **Return**キーを押す（または検索結果の**ターミナル**（Terminal、黒い四角アイコン）をクリック）
- ターミナルウィンドウが開き、カーソルが点滅します

**ヒント：** 次のステップでもターミナルを使うので、開いたままにしておいてください。

## ステップ2：Claude Codeをインストール

ターミナルで以下のコマンドをコピー＆ペーストして、**Return**キーを押してください：
```
curl -fsSL https://claude.ai/install.sh | bash
```

- Claude Codeのインストールを待ちます（1〜2分）
- ダウンロード中はウィンドウに何もメッセージが表示されないことがありますが、正常です。そのまま待ってください
- インストールが完了したら、ターミナルを閉じて再度開き、以下を入力して確認します：
   ```
   claude --version
   ```
- Claude Codeのバージョン番号が表示されるはずです
- 代わりに`zsh: command not found: claude`と表示された場合は、次の2行を実行して（MacにClaude Codeの場所を教えるためのものです）、もう一度`claude --version`を試します：
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

**別の方法：Homebrewでインストール**

Homebrewを使用している場合は、以下のコマンドでClaude Codeをインストールできます：
```
brew install --cask claude-code
```

**ヒント：** インストール後に`claude doctor`を実行すると、すべてが正しくセットアップされているか確認できます。

## ステップ3：Anthropicアカウントに接続

### オプションA. Claude ProまたはMaxサブスクリプションを使用

- ターミナルで以下を入力：
   ```
   claude
   ```
- Claudeがブラウザを開こうとします。自動的に開かない場合は、**c**を押してログインリンクをコピーし、ブラウザに貼り付けてください。
- Claude.aiアカウントにログインします（自動的にログインされる場合もあります）
- **Authorize**をクリック。ブラウザにログイン済みと表示され、ターミナルに成功メッセージが表示されます
- ブラウザに長いコードが表示された場合のみ、**Copy Code**をクリックしてターミナルに戻り、**Paste code here if prompted**の箇所に貼り付け（**Command (⌘) + V**を押す）、**Return**を押します
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
- `claude`と入力してClaude Codeを起動します。初回は、見つかったAPIキーを使うかどうか尋ねてきます。**Yes**を選択します。（誤って**No**を選んだ場合は、`/config`と入力して**Use custom API key**をオンにします。）

**注意：** bashを使用している古いMacの場合は、上記のコマンドで`~/.zshrc`を`~/.bash_profile`に置き換えてください。

### オプションC. OpenRouter APIを使用（従量課金）

OpenRouterは、500以上の大規模言語モデルに単一のAPIキーでアクセスできる統合APIゲートウェイです。使用量に応じた課金で、さまざまな価格帯のモデルから選択できるため、Claude Codeを経済的に使用する方法となります。

- [openrouter.ai](https://openrouter.ai)でサインアップしてログイン
- **Get API key**をクリックしてキーを安全な場所にコピー
- Claude Codeを起動する前に、必要な環境変数を設定：
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="~anthropic/claude-sonnet-latest"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="~anthropic/claude-opus-latest"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="~anthropic/claude-haiku-latest"
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
- 無料（`:free`）モデルは1日50リクエストまでに制限されており、Claude Codeの1つのタスクですぐに使い切ってしまうことがあります
- 上記のモデルは有料モデルです。使う前に[openrouter.ai/models](https://openrouter.ai/models)で料金を確認してください
- OpenRouter経由でClaude Codeの動作が保証されているのはAnthropicのモデルだけです
- 詳細は[公式OpenRouterガイド](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration)を参照してください


### オプションD. Microsoft Foundry（Azure）経由でAnthropic APIを使用

このオプションは、Azure上でClaudeモデルをホストしている組織向けです。Claudeを起動する前に、ターミナルウィンドウで以下のコードを貼り付けて環境変数を定義します：
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**注意：** `xxxx-eastus2`を実際のFoundryリソース名に置き換えてください（ベースURL全体ではなく、リソース名のみ）。`your_api_key`をAzureポータルから取得した完全なAPIキーに置き換えてください。

次に`claude`と入力してClaude Codeを起動します。

## ステップ4：Claude Codeをテストする

これで準備完了です！Claude Codeの使い方は次のとおりです：

- ターミナルで以下を入力：
   ```
   claude
   ```
- チャットの準備をする前にいくつか質問されます
- 動作を確認するには、「Explain quantum computing.」のような一般的な質問をしてみてください

## ステップ5：プロジェクトに移動する

- Macのフォルダにプロジェクトがある場合は、そこに移動できます：
   ```
   cd ~/Documents/test_claude
   ```
   `test_claude`を実際のプロジェクトフォルダ名に置き換えてください

- 次にClaudeを起動します：
   ```
   claude
   ```
- まずは、Claudeにコードベースについて説明してもらうことから始めましょう。
- Claudeに変更を依頼できます。
- お好みのIDEでコードをテストしてください。

**注意：** Claudeはプロジェクトフォルダ内で動作します。フォルダ内で書き込み権限を定義し、そのフォルダに設定を保存します。これがClaudeのワークスペースです。

## ステップ6：Claude Codeをアップデートする

ネイティブインストーラーでインストールしたClaude Codeは、バックグラウンドで自動的にアップデートされます。手動でアップデートを実行することもできます：

- ターミナルで以下を入力：
   ```
   claude update
   ```
- Claude Codeがアップデートを確認し、最新バージョンをインストールします

**注意：** `sudo`を使ってClaude Codeを実行したりアップデートしたりしないでください。`~/.claude`フォルダにroot所有のファイルが残り、次回通常どおりClaude Codeを実行したときに権限エラーが発生する可能性があります。

**注意：** Homebrewでインストールした場合は自動アップデートされません。定期的に`brew upgrade claude-code`を実行して最新バージョンを取得してください。

## 次のステップ
- [VS Code入門](./VS_Code_Getting_Started.md) - 人気のコードエディタVS Codeの使い方を学ぶ
- [VS CodeでClaude Code（Mac）](./Claude_Code_in_VS_Code_Mac.md) - VS Code内でClaude Codeを実行
- [Claude Codeで研究論文を書く](./Writing_Research_Paper_Claude_Code.md) - 学術論文執筆にClaude Codeを活用

## ターミナルを再度開く方法

ターミナルを閉じた後、再度開く方法は次のとおりです：

- **Command (⌘) + Space**を押してSpotlight検索を開く
- `ターミナル`と入力
- **Return**キーを押す
- ターミナルウィンドウが開きます

## トラブルシューティング

### まず最初に：Claude Doctorを実行
何かうまくいかない場合は、まず以下のコマンドを実行してください：
```
claude doctor
```
インストール状況を確認し、問題があれば報告してくれます。

### インストールスクリプトが失敗する
- macOS 13.0以降であることを確認してください
- Homebrewでの代替方法を試してください：`brew install --cask claude-code`
- インターネット接続を確認して再度試してください

### Claude Codeコマンドが見つからない
- ターミナルを完全に終了します（メニューバーの**ターミナル**をクリックし、**ターミナルを終了**を選択）
- ターミナルを再度開きます
- `claude --version`でインストールされているか確認してください
- それでも`command not found`と表示される場合は、次の2行を実行してから、もう一度`claude --version`を試します：
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### 認証に失敗する
- 有効なClaude Pro/Maxサブスクリプションまたは有効なAPIキーがあることを確認してください
- `claude`を再度実行してログインプロセスを完了してください
- ブラウザで正しい認証ページが開かれたか確認してください

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

- Claude Codeの問題：[Claude Code GitHub](https://github.com/anthropics/claude-code)
- 公式セットアップドキュメント：[Claude Codeセットアップガイド](https://code.claude.com/docs/en/setup)

---

*最終更新：2026年2月*
