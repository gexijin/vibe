[ホーム](./)

# WindowsにClaude Codeをインストール

Claude Codeは、ターミナル上で動作するAIアシスタントで、コードの作成、デバッグ、理解を支援します。このガイドでは、セットアップの全手順を説明します。まずPowerShellでのネイティブインストールを行い、次にWSL2でフルLinux環境を構築します。

## 主要な概念

- **WSL（Windows Subsystem for Linux）** - Windows上で本物のLinuxシステムを実行できるWindowsの機能
- **Ubuntu** - 初心者に優しい人気のLinuxディストリビューション。WSL経由でインストールできます
- **PowerShell** - Windowsに組み込まれたコマンドラインツール。ここではClaude CodeのインストールとWSLのセットアップに使用します

## 用意するもの

- Windows 10（バージョン2004以降）またはWindows 11のコンピューター
- コンピューターの管理者アクセス権限
- Claude Pro/MaxサブスクリプションまたはAzure Foundry経由のAPIキー
- 10〜15分の時間

## ステップ1：WindowsにClaude Codeをネイティブインストール（動作しますが非推奨）

- **Windowsスタートボタン**をクリックします
- `PowerShell`と入力し、**Windows PowerShell**をクリックします
- PowerShellウィンドウで次のように入力します：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- インストールが完了するまで待ちます
- PowerShellを閉じて再度開き、次のように入力して確認します：
   ```
   claude --version
   ```
- Claude Codeのバージョン番号が表示されるはずです

> **注意：** ネイティブWindowsインストールにはいくつかの制限があります：
> - Bashツールのサンドボックスが利用できません（WSL2/macOSでのみ利用可能なセキュリティ機能）
> - 一部のツールやワークフローはLinux環境でより良く動作します
>
> フル機能を利用するには、以下の手順に従ってWSL2をインストールしてください。

## ステップ2：仮想化の確認とWSLのインストール

**まず、仮想化が有効か確認します：**

- タスクバー（画面下部のバー）を**右クリック**します
- メニューから**タスクマネージャー**をクリックします
- タスクマネージャーが小さなウィンドウで開いた場合は、下部の**詳細**をクリックします
- 上部の**パフォーマンス**タブをクリックします
- 左側のサイドバーで**CPU**をクリックします
- ウィンドウの右下のセクションを見ます
- **仮想化:** と書かれた行を探し、**有効**と表示されているか確認します

**「有効」と表示されている場合：** 素晴らしいです！そのまま下へ進んでください。

**「無効」と表示されている場合：** コンピューターのBIOS設定で仮想化を有効にする必要があります：
- コンピューターを再起動します
- 起動中にBIOSキー（通常は**F2**、**F10**、**Del**、または**Esc** - コンピューターメーカーによって異なります）を押します
- 「Virtualization Technology」、「Intel VT-x」、「AMD-V」、または「SVM Mode」に関連する設定を探します
- これらの設定を有効にします
- BIOSを保存して終了します（通常は**F10**）
- コンピューターが正常に再起動します

**次にWSLをインストールします：**

- **Windowsスタートボタン**をクリックします
- 検索ボックスに`PowerShell`と入力します
- **Windows PowerShell**を**右クリック**し、**管理者として実行**をクリックします
- 「このアプリがデバイスに変更を加えることを許可しますか？」と表示されたら**はい**をクリックします

**WSLとUbuntuがすでにインストールされているか確認します：**

- PowerShellウィンドウで次のように入力します：
   ```
   wsl --list --verbose
   ```
- **「Ubuntu」が表示されている場合：** WSLはすでにインストールされています！ステップ3にスキップしてください。
- **エラーメッセージが表示される場合：** 以下のインストールを続けてください。

**WSLとUbuntuをインストールするには：**

- PowerShellウィンドウで次のように入力します：
   ```
   wsl --install
   ```
- 「Installing: Windows Subsystem for Linux」や「Installing: Ubuntu」のようなメッセージが表示されることがあります
- インストールが完了したら、コンピューターを再起動します：
   - **Windowsスタートボタン** → **電源アイコン** → **再起動** をクリックします
- コンピューターが再起動します — これには約1〜2分かかります

**注意：** コマンドが認識されないというエラーが表示された場合、Windowsのバージョンが古い可能性があります。Windows 10バージョン2004以降、またはWindows 11があることを確認してください。

## ステップ3：Ubuntuのセットアップ

コンピューターが再起動した後、2〜5分以内にタイトルに「Ubuntu」と表示されたターミナルウィンドウが自動的に開くはずです。

**Ubuntuウィンドウが自動的に開かなかった場合：**
- **Windowsスタートボタン**をクリックします
- 検索ボックスに`Ubuntu`と入力します
- **Ubuntu**（円形のオレンジ色のアイコン）をクリックします
- Ubuntuターミナルが開き、セットアップが続行されます

**次に初回セットアップを完了します：**

- `Enter new UNIX username:`というメッセージが表示されるまで待ちます
- ユーザー名を入力します（小文字と数字のみを使用し、スペースは入れません）
   - 例：`john`
- `New password:`と表示されます
- シンプルなパスワードを入力します（ユーザー名と同じ`john`でも構いません）
- 入力中に文字が表示されませんが、これは正常です
- プロンプトが表示されたら、同じパスワードをもう一度入力します

**重要：** このユーザー名とパスワードは後で必要になるので、覚えておいてください。

## ステップ4：WSLにClaude Codeをインストール

- Ubuntuターミナルで次のように入力します：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Claude Codeがインストールされるまで待ちます
- インストールが完了したら、次のように入力して確認します：
   ```
   claude --version
   ```
- Claude Codeのバージョン番号が表示されるはずです

## ステップ5：Anthropicアカウントに接続

### オプションA. Claude ProまたはMaxサブスクリプションを使用

- Ubuntuターミナルで次のように入力します：
   ```
   claude
   ```
- Claudeがブラウザを開こうとします。自動的に開かない場合は、**Ctrl**を押しながら長いURLをクリックしてブラウザで開きます。または、URLをコピーして外部ブラウザに貼り付けます。
- Claude.aiアカウントにログインします（Chromeを使用している場合は自動的に行われることがあります）
- **Authorize**をクリックします
- 長いコードが表示されたら**Copy Code**をクリックします
- ターミナルウィンドウに戻ります
- ターミナルに貼り付けるには：**右クリック**して**貼り付け**を選択します（または**Ctrl+Shift+V**を押します）
- 成功メッセージが表示されるはずです
- 指示に従ってセットアップを完了します

### オプションB. Anthropic APIキーを使用

Claudeサブスクリプションの代わりにAnthropic APIキーをお持ちの場合：

- まず、[Anthropic Console](https://console.anthropic.com/)からAPIキーを取得します
- Ubuntuターミナルで次のように入力します：
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   `your-api-key-here`を実際のAPIキーに置き換えてください
- これを永続的にするには（毎回設定する必要がないように）、シェルプロファイルに追加します：
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   `your-api-key-here`を実際のAPIキーに置き換えてください
- 変更を有効にするためにUbuntuターミナルを閉じて再度開きます
- これでAPIキーを使ってClaude Codeを使用できるようになります

### オプションC. OpenRouter APIを使用（無料で始められます！）

OpenRouterは、単一のAPIキーで500以上の大規模言語モデルにアクセスできる統合APIゲートウェイです。使用量に応じた課金で、様々な価格帯のモデルから選択できるため、Claude Codeを経済的に利用できます。

- [openrouter.ai](https://openrouter.ai)でサインアップしてログインします
- **Get API key**をクリックして、キーを安全な場所にコピーします
- Claude Codeを起動する前に、必要な環境変数を設定します：
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- Claude Codeを起動します：
   ```
   claude
   ```
- Claude Codeで`/status`と入力して接続を確認します

**注意：**
- `your-openrouter-api-key`を実際のOpenRouter APIキーに置き換えてください
- `ANTHROPIC_API_KEY`は明示的に空に設定する必要があります
- 代替モデルを使用するには、**ツール使用機能**をサポートしている必要があります。モデルは以下で上書きできます：
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- 利用可能なモデルは[openrouter.ai/models](https://openrouter.ai/models)で確認できます
- 無料枠では1日50件のAPIリクエストが可能です
- 詳細は[公式OpenRouterガイド](https://openrouter.ai/docs/guides/claude-code-integration)を参照してください

### オプションD. Azure Foundry経由でAnthropic APIを使用

Claude Codeを起動する前に、Ubuntuターミナルで以下のコードを貼り付けて環境変数を定義します：
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**注意：** `xxxx-eastus2`を実際のFoundryリソース名に置き換えてください（ベースURL全体ではなく、リソース名のみ）。`your_api_key`をAzureポータルから取得した完全なAPIキーに置き換えてください。

次にClaude Codeを起動します：
```
claude
```

これでAzureにデプロイされたClaudeモデルでClaude Codeを使用できるようになります。

## ステップ6：Claude Codeをテスト

準備完了です！Ubuntuターミナルで`claude`と入力し、「Explain quantum computing.」のような一般的な質問をしてみましょう。

## ステップ7：プロジェクトにアクセス

**ネイティブWindows（PowerShell）：**
- プロジェクトフォルダがある場合、そこに移動します：
   ```
   cd ~/Documents/test_claude
   ```
- 次にClaudeを起動します：
   ```
   claude
   ```

**WSL（Ubuntu）：**
- `test_claude`というWindowsフォルダがある場合、次のようにアクセスできます：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   `Username`を実際のWindowsユーザー名に置き換えてください。
- 次にClaudeを起動します：
   ```
   claude
   ```

- まずClaudeにコードベースを説明してもらうことから始めましょう。
- Claudeに変更を依頼できます。
- 好みのIDEでコードをテストします。

**注意：** Claudeはプロジェクトフォルダ内で動作します。そのフォルダに設定を保存します。これがClaudeのワークスペースです。

## ステップ8：Claude Codeを更新

Claude Codeは自動的に更新されますが、いつでも手動で更新できます：

**WSL（Ubuntu）：**
```
sudo claude update
```

**ネイティブWindows（PowerShell — 管理者として実行）：**
```
claude update
```

## 次のステップ

- **VS Codeをセットアップ：** [VS Code Getting Started](VS_Code_Getting_Started)ガイドに従い、次に[Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)でClaude Codeに接続します
- **Gitの基本を学ぶ：** [Claude Code Git on Windows](Claude_Code_Git_Windows)でプロジェクトにバージョン管理を追加します
- **プロジェクトを試す：** [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code)を進めて、Claude Codeの実際の動作を確認します

## トラブルシューティング

### 最初のステップ：Claude Doctorを実行

何かうまくいかない場合は、まず以下のコマンドを試してください：
```
claude doctor
```
この組み込み診断ツールがインストール状態をチェックし、よくある問題を報告します。

### claudeコマンドが見つからない（ネイティブWindows）

- PowerShellを閉じて再度開きます
- インストールコマンドを再度実行してみます：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- PATHにClaudeのインストールディレクトリが含まれていることを確認します

### 「Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS」
このエラーは仮想化が有効になっていないことを意味します：
- ステップ2に戻り、タスクマネージャーで仮想化が有効になっているか確認します
- 無効の場合は、コンピューターのBIOSで有効にする必要があります（手順についてはステップ2を参照）
- 仮想化を有効にした後、コンピューターを再起動して`wsl --install`を再度試します

### 「wsl --install」が機能しない
- PowerShellを管理者として実行していることを確認します
- Windows 10バージョン2004以降またはWindows 11があることを確認します
- まず`wsl --update`を実行してから、`wsl --install`を再度試します

### 再起動後にUbuntuウィンドウが開かない
- Windowsスタートをクリックします
- `Ubuntu`と入力します
- Ubuntuアプリをクリックして手動で起動します

### 閉じた後にUbuntuターミナルを開く方法
- **Windowsスタートボタン**をクリックし、`Ubuntu`と入力して、**Ubuntu**アプリ（オレンジ色の円形アイコン）をクリックします

### Claude Codeコマンドが見つからない（WSL）
- インストールが正常に完了したことを確認します
- Ubuntuターミナルを閉じて再度開いてみます
- インストールコマンドを再度実行します：`curl -fsSL https://claude.ai/install.sh | bash`

## 困ったときは

- WSLの問題：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Claude Codeの問題：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

作成：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 2025年12月11日。2026年2月更新。
