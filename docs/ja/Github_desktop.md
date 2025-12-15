[ホーム](./ja/)

# バージョン管理を始めよう

動いていたコードに手を加えたら突然壊れてしまった——そんな経験はありませんか？何を変えたか思い出せず、「動いていたときに戻れたらいいのに…」と思うはずです。バージョン管理はまさにビデオゲームのセーブポイント。コミットを作るたびに復元ポイントができ、必要なときにいつでも戻れます。[GitHub](https://github.com) を使えば、そのセーブポイントをクラウドに保存して安全にバックアップできます。

## 主要な概念

- **Git**：ローカルPC上のファイル変更履歴を追跡するソフト
- **GitHub**：その履歴をクラウドに保存するサービス（コード版Google Drive）
- **GitHub Desktop**：GitをGUIで操作できる公式クライアント
- **リポジトリ（repo）**：変更履歴を記録するプロジェクトフォルダ

## 必要なもの

- Windows、macOS、またはLinux PC
- インターネット接続
- GitHubアカウント用のメールアドレス
- 15〜20分

## ステップ1：GitHubアカウントを作成

1. ブラウザで [github.com](https://github.com) へ
2. **Sign up** をクリック
3. メールアドレス・パスワード・ユーザー名を入力
4. 案内に従って本人確認を完了

## ステップ2：GitHub Desktopをインストール

1. [desktop.github.com](https://desktop.github.com) を開き、**Download** をクリック
2. ダウンロードしたファイルを開いてインストール
   - **Windows**：インストーラーをダブルクリックすると自動でセットアップ＆起動
   - **Mac**：ダウンロードした`.zip`ファイルを開き、**GitHub Desktop**をApplicationsフォルダへドラッグして起動

## ステップ3：GitHub Desktopにサインイン

1. アプリを開き **Sign in to GitHub.com**
2. ブラウザが自動で開くので **Authorize desktop**
3. アプリに戻り **Finish** でセットアップ完了

## ステップ4：最初のリポジトリを作る

1. GitHub Desktop のトップ画面で **Create a New Repository on your Hard Drive**
2. 次のように入力：
   - **Name**: `my-first-project`
   - **Description**: `Learning version control`（任意）
   - **Local Path**: 保存先（Documentsなど）
   - **Initialize this repository with a README** にチェック
3. **Create Repository** をクリック

## ステップ5：フォルダを開いてみる

- **Repository > Show in Finder/Explorer** を選択
- `my-first-project` フォルダと `README.md` ファイルが確認できます

## ステップ6：READMEを編集

1. `README.md` をメモ帳／TextEdit／VS Codeなどで開く
2. 内容を以下に書き換え、保存
   ```
   # My First Project

   I'm learning version control with GitHub Desktop.

   ## What I'm Building

   This is a practice project to learn how to:
   - Track changes to my code
   - Create save points (commits)
   - Back up my work to GitHub
   ```

## ステップ7：初めてのコミット

1. GitHub Desktopに戻ると差分が表示される（緑＝追加、赤＝削除）
2. 左下のメッセージ欄に `Updated README with project description` と入力
3. **Commit to main** をクリック

## ステップ8：GitHubにプッシュ

1. 画面上部の **Publish repository** をクリック
2. 必要に応じて「Keep this code private」をオン／オフ
3. **Publish Repository** を押して完了

これで `https://github.com/YOUR-USERNAME/my-first-project` にリポジトリが公開されました。

## 次のステップ

- READMEをもう一度編集 → コミット → プッシュ
- 新しいファイルを作ってコミット
- GitHub Desktopの **History** タブで履歴を確認

## トラブルシューティング

| 症状 | 対処 |
| --- | --- |
| GitHubにサインインできない | ネット接続を確認。まずブラウザでgithub.comにログインできるかチェック |
| 変更が表示されない | ファイルを保存したか確認。**Repository > Refresh** またはアプリ再起動を試す |
| Pushがrejectedと言われる | 他の人が先にPushした可能性。**Fetch origin** → もう一度Push |

## 基本ワークフロー

1. ファイルを編集・保存
2. GitHub Desktopで差分を確認
3. 説明的なメッセージを付けて **Commit to main**
4. **Push origin** でGitHubにバックアップ
5. 繰り返す

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2025年12月7日）
