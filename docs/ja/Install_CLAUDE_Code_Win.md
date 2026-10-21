---
title: "WindowsにClaude Codeをインストール"
lang: "ja"
---
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
- ページ上部の **Click here to download** をクリックし、ダウンロードが完了したらインストーラーを開きます
- デフォルトのまま **Next**（次へ） を進めます
- **Install**（インストール）、続いて **Finish**（完了） をクリックします

これで完了です。Claude Codeは起動時にGit Bashを自動的に検出します。

## ステップ2：Claude Codeをインストール

- **Windowsスタートボタン**をクリックします
- `PowerShell`と入力し、**Windows PowerShell**をクリックします
- PowerShellで次のように入力します：
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- インストールが完了するまで待ちます（ダウンロード中の1分ほどは、ウィンドウに何も表示されないことがありますが正常です）
- PowerShellを閉じて再度開き、次のコマンドで確認します：
   ```
   claude --version
   ```
- Claude Codeのバージョン番号が表示されるはずです
- 代わりに `'claude' is not recognized`（日本語版Windowsでは「用語 'claude' は、…認識されません」）と表示された場合は、PowerShellで次の2行を実行し、PowerShellを閉じて再度開いてから、もう一度 `claude --version` を試します：
   ```
   $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
   [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
   ```

## ステップ3：（オプション）VS CodeでClaude Codeを開く

まだVS Codeを持っていない場合は、このステップを飛ばしてください。後で[VS Codeを始めよう](VS_Code_Getting_Started.md)でインストールしてから戻ってくることができます。

Claude Codeをインストールしたので、ターミナルだけでなくVS Codeの中でも使えるようになりました。エディタから離れずに、ファイルを読んだり、コードを編集したり、助けを求めたりできるので、多くの場合これが一番手軽な使い方です。

Claude Codeのサイドバーは、VS Codeの中にあるチャットウィンドウだと考えてください。同じ画面で作業しながら、質問したり、コードの説明を頼んだり、手助けを受けたりできます。

### Claude Codeのサイドバーを開く方法

- VS Codeを開きます
- ウィンドウの一番左側を見ます
- Claude Codeのパネルがまだ表示されていない場合は、**Extensions**（拡張機能）アイコンをクリックします
- 拡張機能マーケットプレイスで `Claude Code` を検索します
- まだインストールされていない場合は、**Install**（インストール）をクリックします
- インストール後、ウィンドウ右下の **✻ Claude Code** をクリックするとチャットが開きます。（左側のサイドバーにあるSparkアイコンをクリックすると、代わりにセッションの一覧が開き、そこから新しいセッションを始められます。）

Claude Codeのアイコンが見つからない場合は、次の方法を試してください：

- **Ctrl + Shift + P**を押します
- 次のように入力します：`Claude Code: Open in Side Bar`
- 一覧に表示された該当する項目をクリックします

それでも表示されない場合は、VS Codeを閉じてから開き直してください。拡張機能を再起動しないと、サイドバーが表示されないことがあります。

### サイドバーでできること

Claude Codeのサイドバーでは、次のことができます：

- プロジェクトについて質問する
- エラーの修正を手伝ってもらう
- 理解できないコードを説明してもらう
- ファイルを作成・更新する
- VS Codeから離れずに、より視覚的な方法で作業する

コードをエディタで開いたまま、同じウィンドウでClaudeに助けを求められるので便利です。

### 簡単なテスト

サイドバーが開いたら：

- 次のように入力します：Explain this project to me
- **Enter**を押します

Claudeが返答すれば、使う準備は完了です。初回は、代わりにサイドバーがサインインを求めてくることがあります。その場合は表示される指示に従うか、下のステップ4でアカウントを接続してからもう一度試してください。

> ヒント：それでもサイドバーが見つからない場合は、Claude Code拡張機能がインストールされていること、そしてVS Codeを再起動したことを確認してください。

## ステップ4：Anthropicアカウントに接続

### オプションA. Claude ProまたはMaxサブスクリプションを使用

- PowerShellで次のように入力します：
   ```
   claude
   ```
- Claudeがブラウザを開こうとします。自動で開かない場合は、**c**を押してログインリンクをコピーし、ブラウザに貼り付けます
- Claude.aiアカウントにログインします（Chromeでは自動の場合があります）
- **Authorize**をクリックします。ブラウザにログイン済みと表示され、PowerShellに成功メッセージが表示されます
- ブラウザに長いコードが表示された場合のみ（WSL/Ubuntuで起こります）、**Copy Code**をクリックしてターミナルに戻り、**Paste code here if prompted** の箇所に貼り付け（**右クリック**または**Ctrl+V**）、**Enter**を押します
- 指示に従ってセットアップを完了します

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
- 初回は、見つかったAPIキーを使うかどうかClaude Codeが尋ねてきます。**Yes**を選択します。（誤って**No**を選んだ場合は、`/config`と入力して**Use custom API key**をオンにします。）

### オプションC. OpenRouter APIを使用（従量課金）

OpenRouterは、単一のAPIキーで500以上の大規模言語モデルにアクセスできる統合APIゲートウェイです。使用量に応じた課金で、様々な価格帯のモデルから選べるため、Claude Codeを経済的に利用できます。

- [openrouter.ai](https://openrouter.ai)でサインアップしてログインします
- **Get API key**をクリックし、キーを安全な場所にコピーします
- PowerShellで必要な環境変数を設定します：
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   [Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', $null, 'User')
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "~anthropic/claude-sonnet-latest"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "~anthropic/claude-opus-latest"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "~anthropic/claude-haiku-latest"
   ```
- PowerShellを閉じて再度開き、Claude Codeを起動します：
   ```
   claude
   ```
- Claude Codeで`/status`と入力して接続を確認します

**注意：**
- `your-openrouter-api-key`を実際のOpenRouter APIキーに置き換えてください
- `ANTHROPIC_API_KEY`の行は保存済みのAnthropic APIキーを削除します。OpenRouterを使うときは、このキーが設定されていてはいけません
- 代替モデルは**ツール使用機能**をサポートしている必要があります。以下で上書きできます：
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- 利用可能なモデルは[openrouter.ai/models](https://openrouter.ai/models)で確認できます
- 無料（`:free`）モデルは1日50リクエストまでに制限されており、Claude Codeの1つのタスクですぐに使い切ってしまうことがあります
- 上記のモデルは有料モデルです。使う前に[openrouter.ai/models](https://openrouter.ai/models)で料金を確認してください
- OpenRouter経由でClaude Codeの動作が保証されているのはAnthropicのモデルだけです
- 詳細は[公式OpenRouterガイド](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration)を参照してください

### オプションD. Microsoft Foundry（Azure）経由でAnthropic APIを使用

PowerShellで以下を貼り付けて環境変数を定義します：
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-8"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**注意：** `xxxx-eastus2`を実際のFoundryリソース名に置き換えてください（ベースURL全体ではなくリソース名のみ）。`your_api_key`はAzureポータルから取得した完全なAPIキーに置き換えてください。

次にPowerShellを閉じて再度開き、Claude Codeを起動します：
```
claude
```

これでAzureにデプロイされたClaudeモデルを使用できます。

## ステップ5：Claude Codeをテスト

準備完了です！PowerShellで`claude`と入力し、「Explain quantum computing.」のような質問を試してみましょう。

## ステップ6：プロジェクトにアクセス

- プロジェクトフォルダがあれば、PowerShellで移動します：
   ```
   cd ~/Documents/test_claude
   ```
   `test_claude`は実際のプロジェクトフォルダ名に置き換えてください。ヒント：`cd `（スペース付き）と入力し、エクスプローラーからフォルダをPowerShellウィンドウにドラッグするとフルパスが貼り付けられるので、**Enter**を押します。
- Claudeを起動します：
   ```
   claude
   ```
- まずはClaudeにコードベースを説明してもらいましょう
- Claudeに変更を依頼できます
- 好みのIDEでコードをテストします

**注意：** Claudeはプロジェクトフォルダ内で動作し、そのフォルダに設定を保存します。これがClaudeのワークスペースです。

## ステップ7：（オプション）フルLinux環境のためにWSL2をインストール

上記のネイティブセットアップでほとんどの人には十分です。ただし、一部の機能はLinux上でしか動作しません。WSL2はWindows内で本物のLinuxを実行し、**Bashツールのサンドボックス**（セキュリティ機能）とLinuxツールチェーンとの高い互換性を提供します。セットアップに時間がかかり再起動も必要なので、フルLinux環境が欲しい場合のみ実行してください。

### a) 仮想化の確認とWSLのインストール

**まず仮想化が有効か確認します：**

- タスクバー（画面下部のバー）を**右クリック**し、**タスクマネージャー**を選びます
- 小さなウィンドウで開いた場合は、下部の**詳細**をクリックします
- **パフォーマンス**（Windows 10では上部のタブ、Windows 11では左側メニューのアイコン）、左側の**CPU**の順にクリックします
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
- Ubuntuウィンドウを閉じ、スタートメニューから**Ubuntu**をもう一度開いてから、次のコマンドで確認します：
   ```
   claude --version
   ```
- それでも`command not found`と表示される場合は、次の行を実行してから、もう一度`claude --version`を試します：
   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
   ```
- `claude`と入力し、ブラウザでのログイン（ステップ4のオプションAと同じ）でアカウントを接続します。APIキーを使う場合は`echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc && source ~/.bashrc`で保存します（WSLは`setx`ではなくLinuxコマンドを使います）
- WSLからWindowsのプロジェクトフォルダを開くには（`Username`は実際のWindowsユーザー名に置き換え）：
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```

## 次のステップ

- **VS Codeをセットアップ：** [VS Codeを始めよう](VS_Code_Getting_Started)に従い、[WindowsでClaude Code用にVS Codeをセットアップ](Claude_Code_in_VS_Code_Win)でClaude Codeに接続します
- **Gitの基本を学ぶ：** [Windows版Claude Codeでローカルバージョン管理](Claude_Code_Git_Windows)でプロジェクトにバージョン管理を追加します
- **プロジェクトを試す：** [Claude Codeで研究論文を書く](Writing_Research_Paper_Claude_Code)でClaude Codeの実際の動作を確認します

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
- `'claude' is not recognized`（日本語版Windowsでは「…認識されません」）と表示される場合は、PowerShellで次の2行を実行し、PowerShellを閉じて再度開きます：
   ```
   $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
   [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
   ```

### 「Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS」というエラーが表示される
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
