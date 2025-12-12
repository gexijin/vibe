# Vibeチュートリアルドキュメント

このフォルダには、Claude Code、VS Code、および関連ツールを使用するための初心者向けチュートリアルが含まれています。

## 学習パス

チュートリアルは`index.html`のインタラクティブグラフに示されている進行に従っています。推奨される順序は以下の通りです：

### Windows - 基本パス（研究・執筆）
1. `Install_CLAUDE_Code_Win.md` - WSL経由でClaude Codeをインストール
2. `VS_Code_Getting_Started.md` - VS Codeの基本
3. `Claude_Code_in_VS_Code_Win.md` - VS CodeをClaude Codeに接続
4. `Claude_Code_Git_Windows.md` - ローカルバージョン管理
5. `Writing_Research_Paper_Claude_Code.md` - 研究論文ワークフロー

### Mac - 基本パス（研究・執筆）
1. `Install_Claude_Code_MacOS.md` - Claude Codeをインストール
2. `VS_Code_Getting_Started.md` - VS Codeの基本
3. `Claude_Code_in_VS_Code_Mac.md` - VS CodeをClaude Codeに接続
4. `Claude_Code_Git_Mac.md` - ローカルバージョン管理
5. `Writing_Research_Paper_Claude_Code.md` - 研究論文ワークフロー

### Rコーディングパス
1. Claude Codeをインストール（WindowsまたはMac）
2. `VS_Code_Getting_Started.md` - VS Codeの基本
3. `R_Coding_VS_Code_Guide.md` - VS CodeでRをセットアップ
4. `R_Coding_Docker_Guide.md` - Dockerコンテナ内でR
5. `Github_desktop.md` - バージョン管理の基本
6. `GitHub_Desktop_Claude_Code_Workflow.md` - 統合ワークフロー
7. `Vibe_Coding_R_Docker_Guide.md` - vibeコーディングでNBAダッシュボードを構築

**代替Rパス：**
- `Claude_Code_RStudio_Mac.md` - MacでRStudioとClaude Codeを使用
- `Claude_Code_WSL_RStudio_Windows.md` - WindowsでRStudioとClaude Codeを使用
- `Claude_Code_R_VS_Code_Mac.md` - MacのVS CodeでClaude CodeをRに使用

### Pythonコーディングパス
1. Claude Codeをインストール（WindowsまたはMac）
2. `VS_Code_Getting_Started.md` - VS Codeの基本
3. `Python_Coding_VS_Code_Guide.md` - VS CodeでPythonをセットアップ
4. `Python_Coding_Docker_Guide.md` - Dockerコンテナ内でPython
5. `Github_desktop.md` - バージョン管理の基本
6. `GitHub_Desktop_Claude_Code_Workflow.md` - 統合ワークフロー
7. `Vibe_Coding_Python_Docker_Guide.md` - PythonでVibeコーディング

**代替Pythonパス：**
- `Claude_Code_Python_VS_Code_Mac.md` - MacのVS CodeでClaude CodeをPythonに使用

## コンテンツ概要

### インストールガイド
- `Install_CLAUDE_Code_Win.md` - WSL経由のWindowsインストール
- `Install_Claude_Code_MacOS.md` - macOSインストール

### VS Codeセットアップ
- `VS_Code_Getting_Started.md` - 初心者向けVS Codeの基本
- `Claude_Code_in_VS_Code_Win.md` - WindowsのVS CodeでClaude Codeを実行
- `Claude_Code_in_VS_Code_Mac.md` - MacのVS CodeでClaude Codeを実行

### Gitワークフロー
- `Claude_Code_Git_Windows.md` - WindowsでのGit統合
- `Claude_Code_Git_Mac.md` - MacでのGit統合
- `Github_desktop.md` - GitHub Desktopの基本
- `GitHub_Desktop_Claude_Code_Workflow.md` - 統合ワークフロー

### Rコーディングガイド
- `R_Coding_VS_Code_Guide.md` - VS CodeでのR開発
- `R_Coding_Docker_Guide.md` - DockerでのR
- `Vibe_Coding_R_Docker_Guide.md` - RとShinyでのVibeコーディング
- `Claude_Code_RStudio_Mac.md` - MacでRStudioとClaude Code
- `Claude_Code_WSL_RStudio_Windows.md` - WindowsでRStudioとClaude Code
- `Claude_Code_R_VS_Code_Mac.md` - MacのVS CodeでClaude CodeをRに使用

### Pythonコーディングガイド
- `Python_Coding_VS_Code_Guide.md` - VS CodeでのPython開発
- `Python_Coding_Docker_Guide.md` - DockerでのPython
- `Vibe_Coding_Python_Docker_Guide.md` - PythonでのVibeコーディング
- `Claude_Code_Python_VS_Code_Mac.md` - MacのVS CodeでClaude CodeをPythonに使用

### プロジェクト
- `Writing_Research_Paper_Claude_Code.md` - 研究論文ワークフロー
- `example_paper.md` - 研究論文チュートリアルのサンプル出力

## 執筆スタイル

- 対象読者：コーディング経験がない完全な初心者
- 明示的なクリックとメニューナビゲーションを含むステップバイステップの指示を使用
- キーボードショートカットを避け、メニューベースの指示を優先
- 開始時に「必要なもの」と所要時間の見積もりを含める
- 一般的な問題のトラブルシューティングセクションを追加
- 各チュートリアルの上部にホーム（./）へのリンクを追加

## スラッシュコマンド

`.claude/commands/`のカスタムコマンド：

- `/tutorial [topic]` - スタイルガイドに従って新しい初心者向けチュートリアルを作成
- `/review-tutorial [file]` - 既存のチュートリアルをレビューし、明確性、正確性、書式を改善
- `/bioinfo-newsletter` - ブログコンテンツからバイオインフォマティクス研究ニュースレターを生成

## ファイル構造

- `index.html` - インタラクティブなチュートリアルグラフを含むランディングページ
- `_config.yml` - Jekyll設定
- `_layouts/` - HTMLテンプレート
- `assets/` - 画像と静的ファイル
- `ja/` - 日本語翻訳
