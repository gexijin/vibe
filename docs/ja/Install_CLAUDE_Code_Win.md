[ホーム](./ja/)

# WSLを使ってWindowsにClaude Codeをインストール

Claude Codeは強力なAIコーディングアシスタントですが、Windowsユーザーには課題があります。多くの開発ツールはLinux上でより良く動作します。解決策は？WSL（Windows Subsystem for Linux）を使えば、Windows内で完全なLinux環境を実行できます。まるで1台のコンピューター内に2台のコンピューターがあるようなものです。このガイドでは、約20分でセットアップを完了し、Claudeでコーディングを始められるよう、すべての手順を説明します。

## 主要な概念

- **WSL（Windows Subsystem for Linux）** - Windows上で本物のLinuxシステムを実行できるWindowsの機能
- **Ubuntu** - 初心者に優しい人気のLinuxディストリビューション。WSL経由でインストールします
- **PowerShell** - Windowsに組み込まれたコマンドラインツール。ここではWSLのインストールに使用します
- **Node.js** - Claude Codeが動作に必要とするJavaScriptランタイム
- **ターミナル** - コマンドを実行するテキストベースのインターフェース（Ubuntuのコマンドラインなど）

## 用意するもの

- Windows 10（バージョン2004以降）またはWindows 11のコンピューター
- コンピューターの管理者アクセス権限
- Claude Pro/MaxサブスクリプションまたはAzure Foundry経由のAPIキー
- 15〜20分の時間

## ステップ1：仮想化が有効か確認

WSLをインストールする前に、コンピューターで仮想化が有効になっていることを確認する必要があります。これはWSLが動作するために必要です。

- タスクバー（画面下部のバー）を**右クリック**します
- メニューから**タスクマネージャー**をクリックします
- タスクマネージャーが小さなウィンドウで開いた場合は、下部の**詳細**をクリックします
- 上部の**パフォーマンス**タブをクリックします
- 左側のサイドバーで**CPU**をクリックします
- ウィンドウの右下のセクションを見ます
- **仮想化:** と書かれた行を探し、**有効**と表示されているか確認します

**「有効」と表示されている場合：** 素晴らしい！ステップ2に進んでください。

**「無効」と表示されている場合：** コンピューターのBIOS設定で仮想化を有効にする必要があります：
- コンピューターを再起動します
- 起動中にBIOSキー（通常は**F2**、**F10**、**Del**、または**Esc** - コンピューターメーカーによって異なります）を押します
- 「Virtualization Technology」、「Intel VT-x」、「AMD-V」、または「SVM Mode」に関連する設定を探します
- これらの設定を有効にします
- BIOSを保存して終了します（通常は**F10**）
- コンピューターが正常に再起動します

## ステップ2：管理者権限でPowerShellを開く

- **Windowsスタートボタン**（左下隅のWindowsアイコン）をクリックします
- 検索ボックスに`PowerShell`と入力します
- 検索結果に**Windows PowerShell**が表示されます
- **Windows PowerShell**を**右クリック**します
- メニューから**管理者として実行**をクリックします
- 「このアプリがデバイスに変更を加えることを許可しますか？」というウィンドウがポップアップ表示されます
- **はい**をクリックします

白い文字が表示された青いウィンドウが開きます - これが管理者として実行されているPowerShellです。

## ステップ3：WSLをインストール

**まず、WSLとUbuntuがすでにインストールされているか確認します：**

- PowerShellウィンドウで次のように入力します：
   ```
   wsl --list --verbose
   ```
- 結果を確認します：
   - **「Ubuntu」がSTATEが「Running」または「Stopped」として表示されている場合：** WSLとUbuntuはすでにインストールされています！ステップ4にスキップしてください。
   - **エラーメッセージまたは「Windows Subsystem for Linux has no installed distributions」と表示される場合：** 以下のインストールを続けます。

**WSLとUbuntuをインストールするには：**

- PowerShellウィンドウで次のように入力します：
   ```
   wsl --install
   ```
- 「Installing: Windows Subsystem for Linux」や「Installing: Ubuntu」のようなメッセージが表示されることがあります
- インストールが完了したというメッセージが表示されたら、コンピューターを再起動する必要があります：
   - **Windowsスタートボタン**をクリックします
   - **電源アイコン**をクリックします
   - **再起動**をクリックします
- コンピューターが再起動します - これには約1〜2分かかります

**再起動が必要な理由：** 再起動により、WindowsがインストールされたばかりのWSLと仮想マシンプラットフォーム機能を有効にすることができます。

**注意：** コマンドが認識されないというエラーが表示された場合、Windowsのバージョンが古い可能性があります。Windows 10バージョン2004以降、またはWindows 11があることを確認してください。Windows Updateを実行して最新バージョンを入手してください。

## ステップ4：Ubuntuのセットアップ（初回のみ）

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

## ステップ5：Ubuntuを更新

- Ubuntuターミナルウィンドウで次のように入力します：
   ```
   sudo apt update
   ```
- プロンプトが表示されたらパスワード（先ほど作成したもの）を入力します
- 次に、次のように入力します：
   ```
   sudo apt upgrade -y
   ```
- すべてのパッケージがアップグレードされるまで待ちます（これには5分かかる場合があります）

## ステップ6：Node.jsをインストール

Claude CodeにはNode.jsバージョン18以降が必要です。次の手順に従ってください：

- Ubuntuターミナルで、次のコマンドをコピーして貼り付けます：

   まず、nvmインストーラーをダウンロードします：
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   cat install.sh | bash
   \. "$HOME/.nvm/nvm.sh"
   nvm install 24
   ```
   これはまずnvmインストーラーをダウンロードし、インストールしてから、それを使ってNode.js v24.0をインストールします
- Node.jsがインストールされるまで待ちます（2〜5分）
- 次のように入力してインストールを確認します：
   ```
   node --version
   ```
- `v24.x.x`のような表示が出るはずです（正確な数字は異なる場合があります）

## ステップ7：Claude Codeをインストール

- Ubuntuターミナルで次のように入力します：
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Claude Codeがインストールされるまで待ちます（2〜5分）
- 黄色や赤色のテキストで警告が表示されることがありますが、これは通常正常です
- インストールが完了したら、次のように入力して確認します：
   ```
   claude --version
   ```
- Claude Codeのバージョン番号が表示されるはずです

## ステップ8：Anthropic API接続を設定

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

Claude.aiサブスクリプションの代わりにAnthropic APIキーをお持ちの場合：

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

### オプションC. Azure Foundry経由でAnthropic APIを使用

Claude Codeを起動する前に、Ubuntuターミナルウィンドウで次のコードを貼り付けて環境変数を定義します：
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

**注意：** `xxxx-eastus2`をFoundryリソース名に置き換えてください（ベースURL全体ではありません）。`your_api_key`をAzureポータルからの完全なAPIキーに置き換えてください。

次にClaude Codeを起動します：
```
claude
```

これでAzureにデプロイされたClaudeモデルでClaude Codeを使用できるようになります。

## ステップ9：Claude Codeをテスト

すべて完了です！動作するか確認するために、「量子コンピューティングについて説明してください」などの一般的な質問をしてみましょう。

## ステップ10：Windowsプロジェクトにアクセス
- `test_claude`というWindowsフォルダにプロジェクトのファイルが含まれている場合、次のようにアクセスできます：
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

## 次のステップ

- **VS Codeをセットアップ：** [VS Code Getting Started](VS_Code_Getting_Started)ガイドに従い、次に[Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)でClaude Codeに接続します
- **Gitの基本を学ぶ：** [Claude Code Git on Windows](Claude_Code_Git_Windows)でプロジェクトにバージョン管理を追加します
- **プロジェクトを試す：** [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code)を進めて、Claude Codeの実際の動作を確認します

## トラブルシューティング

### 閉じた後にUbuntuターミナルを開く方法
- **Windowsスタートボタン**をクリックし、`Ubuntu`と入力して、**Ubuntu**アプリ（オレンジ色の円形アイコン）をクリックします

### 「Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS」
このエラーは仮想化が有効になっていないことを意味します：
- ステップ1に戻り、タスクマネージャーで仮想化が有効になっているか確認します
- 無効の場合は、コンピューターのBIOSで有効にする必要があります（手順についてはステップ1を参照）
- 仮想化を有効にした後、コンピューターを再起動して`wsl --install`を再度試します

### 「wsl --install」が機能しない
- PowerShellを管理者として実行していることを確認します
- Windows 10バージョン2004以降またはWindows 11があることを確認します
- 最初に`wsl --update`を実行してから、`wsl --install`を再度試します

### 再起動後にUbuntuウィンドウが開かない
- Windowsスタートをクリックします
- `Ubuntu`と入力します
- Ubuntuアプリをクリックして手動で起動します

### 「sudo: apt: command not found」
- WSLが正しくインストールされていない可能性があります
- PowerShell（管理者として）で次のように入力します：`wsl --unregister Ubuntu`
- 次に`wsl --install`を再度実行します

### Node.jsのインストールが失敗する
- 最初に`sudo apt update`を実行したことを確認します
- インストールコマンドを再度試します

### Claude Codeコマンドが見つからない
- インストールが正常に完了したことを確認します
- Ubuntuターミナルを閉じて再度開きます
- インストールコマンドを再度実行します：`curl -fsSL https://claude.ai/install.sh | bash`

## サポート

- WSLの問題：[Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Claude Codeの問題：[Claude Code GitHub](https://github.com/anthropics/claude-code)

---

作成：[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 2025年12月11日
