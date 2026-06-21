[ホーム](./)

# WindowsにClaude Codeをインストール

Claude Codeは、ターミナル上で動作し、コードの作成・デバッグ・理解を支援するAIアシスタントです。このガイドでは、数分でWindowsにネイティブインストールする方法を説明します。より高度なセットアップとして、最後にWSL2もオプションで紹介します。

## 主要な概念

- **PowerShell** - Windows組み込みのコマンドラインツール。Claude Codeのインストールと実行に使用します
- **Git for Windows** - 無料のソフトで、Claude Codeがコマンド実行に使うシェル **Git Bash** を追加します
- **WSL（Windows Subsystem for Linux）** - Windows上で本物のLinuxを実行できるオプション機能。最後の高度なセットアップで使用します

## 用意するもの

- Windows 10またはWindows 11のコンピューター
- Claude Pro/MaxサブスクリプションまたはAPIキー
- 5〜10分の時間

## ステップ1：Git for Windowsをインストール（オプション、推奨）

Git for Windowsは **推奨ですがオプション** で、Claude Codeがコマンド実行に使うシェル **Git Bash** を追加します。スキップするとClaude CodeはPowerShellを使うため、ステップ2に直接進み、後でGitを入れることもできます。

- [git-scm.com/download/win](https://git-scm.com/download/win) にアクセスします
- ダウンロードが自動的に始まります。完了したらインストーラーを開きます
- デフォルトのまま **次へ（Next）** を進めます
- **インストール（Install）**、続いて **完了（Finish）** をクリックします

これで完了です。Claude Codeは起動時にGit Bashを自動的に検出します。

## ステップ2：Claude Codeをインストール

- **Windowsスタートボタン**をクリックします
- `PowerShell`と入力し、**Windows PowerShell**をクリックします
- PowerShellで次のように入力します：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- インストールが完了するまで待ちます
- PowerShellを閉じて再度開き、次のコマンドで確認します：
   ```
   claude --version
   ```
- Claude Codeのバージョン番号が表示されるはずです

## ステップ3：Anthropicアカウントに接続

### オプションA. Claude ProまたはMaxサブスクリプションを使用

- PowerShellで次のように入力します：
   ```
   claude
   ```
- Claudeがブラウザを開こうとします。自動で開かない場合は、**Ctrl**を押しながら長いURLをクリックするか、URLをコピーしてブラウザに貼り付けます
- Claude.aiアカウントにログインします（Chromeでは自動の場合があります）
- **Authorize**をクリックします
- 長いコードが表示されたら**Copy Code**をクリックします
- ターミナルに戻り、**右クリック**して**貼り付け**を選択します（または**Ctrl+Shift+V**）
- 成功メッセージが表示されます。指示に従ってセットアップを完了します

以下のAPIベースのオプションは **PowerShell** 上で、設定を永続保存する `setx` コマンドを使います。`setx` 実行後は **PowerShellを閉じて再度開いてから** `claude` を起動してください。

### オプションB. Anthropic APIキーを使用

Claudeサブスクリプションの代わりにAnthropic APIキーをお持ちの場合：

- [Anthropic Console](https://console.anthropic.com/)からAPIキーを取得します
- PowerShellで次のように入力します（`your-api-key-here`は実際のキーに置き換え）：
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
- PowerShellを閉じて再度開き、Claude Codeを起動します：
   ```
   claude
   ```

### オプションC. OpenRouter APIを使用（無料で始められます！）

OpenRouterは、単一のAPIキーで500以上の大規模言語モデルにアクセスできる統合APIゲートウェイです。使用量に応じた課金で、様々な価格帯のモデルから選べるため、Claude Codeを経済的に利用できます。

- [openrouter.ai](https://openrouter.ai)でサインアップしてログインします
- **Get API key**をクリックし、キーを安全な場所にコピーします
- PowerShellで必要な環境変数を設定します：
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- PowerShellを閉じて再度開き、Claude Codeを起動します：
   ```
   claude
   ```
- Claude Codeで`/status`と入力して接続を確認します

**注意：**
- `your-openrouter-api-key`を実際のOpenRouter APIキーに置き換えてください
- `ANTHROPIC_API_KEY`は明示的に空に設定する必要があります
- 代替モデルは**ツール使用機能**をサポートしている必要があります。以下で上書きできます：
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- 利用可能なモデルは[openrouter.ai/models](https://openrouter.ai/models)で確認できます
- 無料枠は1日50件のAPIリクエストが可能です
- 詳細は[公式OpenRouterガイド](https://openrouter.ai/docs/guides/claude-code-integration)を参照してください

### オプションD. Azure Foundry経由でAnthropic APIを使用

PowerShellで以下を貼り付けて環境変数を定義します：
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**注意：** `xxxx-eastus2`を実際のFoundryリソース名に置き換えてください（ベースURL全体ではなくリソース名のみ）。`your_api_key`はAzureポータルから取得した完全なAPIキーに置き換えてください。

次にPowerShellを閉じて再度開き、Claude Codeを起動します：
```
claude
```

これでAzureにデプロイされたClaudeモデルを使用できます。

## ステップ4：Claude Codeをテスト

準備完了です！PowerShellで`claude`と入力し、「Explain quantum computing.」のような質問を試してみましょう。

## ステップ5：プロジェクトにアクセス

- プロジェクトフォルダがあれば、PowerShellで移動します：
   ```
   cd ~/Documents/test_claude
   ```
- Claudeを起動します：
   ```
   claude
   ```
- まずはClaudeにコードベースを説明してもらいましょう
- Claudeに変更を依頼できます
- 好みのIDEでコードをテストします

**注意：** Claudeはプロジェクトフォルダ内で動作し、そのフォルダに設定を保存します。これがClaudeのワークスペースです。

## ステップ6：（オプション）フルLinux環境のためにWSL2をインストール

上記のネイティブセットアップでほとんどの人には十分です。ただしClaude CodeはLinux上でより良く動作します。WSL2はWindows内で本物のLinuxを実行し、**Bashツールのサンドボックス**（セキュリティ機能）とLinuxツールチェーンとの高い互換性を提供します。セットアップに時間がかかり再起動も必要なので、フルLinux環境が欲しい場合のみ実行してください。

### a) 仮想化の確認とWSLのインストール

**まず仮想化が有効か確認します：**

- タスクバー（画面下部のバー）を**右クリック**し、**タスクマネージャー**を選びます
- 小さなウィンドウで開いた場合は、下部の**詳細**をクリックします
- 上部の**パフォーマンス**タブ、左側の**CPU**の順にクリックします
- **仮想化:** の行が**有効**になっているか確認します

**「無効」の場合：** BIOS設定で仮想化を有効にする必要があります：
- コンピューターを再起動し、起動中にBIOSキー（通常は**F2**、**F10**、**Del**、または**Esc** — メーカーにより異なります）を押します
- 「Virtualization Technology」「Intel VT-x」「AMD-V」「SVM Mode」などの設定を有効にします
- BIOSを保存して終了します（通常は**F10**）

**次にWSLをインストールします：**

- **Windowsスタートボタン**をクリックし、`PowerShell`と入力します
- **Windows PowerShell**を**右クリック**し、**管理者として実行**をクリックします
- 「このアプリがデバイスに変更を加えることを許可しますか？」と表示されたら**はい**をクリックします
- PowerShellで次のように入力します：
   ```
   wsl --install
   ```
- 「Installing: Windows Subsystem for Linux」や「Installing: Ubuntu」のようなメッセージが表示されることがあります
- インストールが完了したら、コンピューターを再起動します

**注意：** `wsl --install` にはWindows 10バージョン2004以降、またはWindows 11が必要です。コマンドが認識されない場合、Windowsのバージョンが古い可能性があります。

### b) Ubuntuのセットアップ

再起動後、2〜5分以内にタイトルに「Ubuntu」と表示されたターミナルが自動的に開きます。開かない場合は、**Windowsスタートボタン**から`Ubuntu`と入力し、**Ubuntu**アプリ（オレンジ色の円形アイコン）をクリックします。

- `Enter new UNIX username:`と表示されたら、ユーザー名を入力します（小文字と数字のみ、スペースなし） — 例：`john`
- `New password:`と表示されたら、シンプルなパスワードを入力します（入力中に文字は表示されませんが正常です）
- プロンプトに従って同じパスワードをもう一度入力します

**重要：** このユーザー名とパスワードは後で必要になるので覚えておいてください。

### c) WSLにClaude Codeをインストール

- Ubuntuターミナルで次のように入力します：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- 次のコマンドで確認します：
   ```
   claude --version
   ```
- `claude`と入力し、ブラウザでのログイン（ステップ3のオプションAと同じ）でアカウントを接続します。APIキーを使う場合は`export ANTHROPIC_API_KEY="your-api-key-here"`で設定します（WSLは`setx`ではなくLinuxコマンドを使います）
- WSLからWindowsのプロジェクトフォルダを開くには（`Username`は実際のWindowsユーザー名に置き換え）：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```

## 次のステップ

- **VS Codeをセットアップ：** [VS Code Getting Started](VS_Code_Getting_Started)に従い、[Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)でClaude Codeに接続します
- **Gitの基本を学ぶ：** [Claude Code Git on Windows](Claude_Code_Git_Windows)でプロジェクトにバージョン管理を追加します
- **プロジェクトを試す：** [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code)でClaude Codeの実際の動作を確認します

## トラブルシューティング

### 最初のステップ：Claude Doctorを実行

うまくいかない場合は、まず以下を試してください：
```
claude doctor
```
この組み込み診断ツールがインストール状態をチェックし、よくある問題を報告します。

### claudeコマンドが見つからない（ネイティブWindows）

- PowerShellを閉じて再度開きます
- インストールコマンドを再実行します：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- PATHにClaudeのインストールディレクトリが含まれているか確認します

### 「Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS」
このエラーは仮想化が有効でないことを意味します：
- タスクマネージャーで仮想化が有効か確認します（上記のオプションのWSLセクション参照）
- 無効の場合は、コンピューターのBIOSで有効にします
- 有効にした後、再起動して`wsl --install`を再度試します

### 「wsl --install」が機能しない
- PowerShellを管理者として実行しているか確認します
- Windows 10バージョン2004以降またはWindows 11か確認します
- まず`wsl --update`を実行してから、`wsl --install`を再度試します

### 再起動後にUbuntuウィンドウが開かない
- **Windowsスタートボタン**から`Ubuntu`と入力し、**Ubuntu**アプリをクリックして手動で起動します

## 困ったときは

- WSLの問題：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Claude Codeの問題：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

作成：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 2025年12月11日。2026年6月更新。
