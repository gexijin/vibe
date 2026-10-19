---
title: "バージョン管理を始めよう"
lang: "ja"
---
[ホーム](./)

# バージョン管理を始めよう

動いていたコードに手を加えたら突然壊れてしまった——そんな経験はありませんか？何を変えたか思い出せず、「動いていたときに戻れたらいいのに…」と思うはずです。バージョン管理はまさにビデオゲームのセーブポイント。コミットを作るたびに復元ポイントができ、必要なときにいつでも戻れます。[GitHub](https://github.com) を使えば、そのセーブポイントをクラウドに保存して安全にバックアップできます。

## 主要な概念

- **Git**：ローカルPC上のファイル変更履歴を追跡するソフト
- **GitHub**：その履歴をクラウドに保存するサービス（コード版Google Drive）
- **GitHub Desktop**：GitをGUIで操作できる公式クライアント
- **リポジトリ（repo）**：変更履歴を記録するプロジェクトフォルダ

## 必要なもの

- WindowsまたはMacのパソコン（GitHub DesktopはLinuxでは動作しません）
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
   - **Mac**：ダウンロードした`.zip`ファイルを開き、**GitHub Desktop**を**アプリケーション**（Applications）フォルダへドラッグし、アプリケーションフォルダから起動

## ステップ3：GitHub Desktopにサインイン

1. アプリを開き **Sign in to GitHub.com** をクリックします
2. ブラウザが自動で開くので、求められたらサインインし、**Authorize desktop** をクリックします
3. ブラウザが **GitHub Desktop** を開くか尋ねてきたら、**開く**（または **許可**）をクリックします
4. アプリに戻り **Finish** をクリックしてセットアップを完了します

## ステップ4：最初のリポジトリを作る

1. GitHub Desktop のトップ画面で **Create a New Repository on your Local Drive** をクリックします
2. 次のように入力：
   - **Name**: `my-first-project`
   - **Description**: `Learning version control`（任意）
   - **Local Path**: 保存先（**書類**／**ドキュメント**（Documents）フォルダなど）
   - **Initialize this repository with a README** にチェック
3. **Create Repository** をクリック

## ステップ5：フォルダを開いてみる

- **Repository > Show in Finder/Explorer** を選択
- `my-first-project` フォルダと `README.md` ファイルが確認できます

## ステップ6：READMEを編集

1. `README.md` を**メモ帳**（Notepad）／**テキストエディット**（TextEdit）／VS Codeなどで開く
2. 内容を以下に書き換え、保存
   ```
   # 初めてのプロジェクト

   GitHub Desktopでバージョン管理を学習中です。

   ## 作成するもの

   このプロジェクトで学ぶこと：
   - コードの変更を追跡する
   - セーブポイント（コミット）を作成する
   - 作業をGitHubにバックアップする
   ```

## ステップ7：初めてのコミット

1. GitHub Desktopに戻ると差分が表示される（緑＝追加、赤＝削除）
2. 左下のメッセージ欄に `プロジェクトの説明を追加` と入力
3. 青い **Commit 1 file to main** ボタンをクリック（数字は変更したファイルの数と一致します）

## ステップ8：GitHubにプッシュ

1. 画面上部の **Publish repository** をクリック
2. 名前はそのままにし、他の人にもコードを見せたい場合のみ「Keep this code private」のチェックを外す（任意）
3. **Publish Repository** を押して完了

これで `https://github.com/YOUR-USERNAME/my-first-project` にコードがバックアップされました。

## 次のステップ

- READMEをもう一度編集 → コミット → プッシュ
- 新しいファイルを作ってコミット
- GitHub Desktopの **History** タブで履歴を確認

## トラブルシューティング

| 症状 | 対処 |
| --- | --- |
| GitHubにサインインできない | ネット接続を確認。まずブラウザでgithub.comにログインできるかチェック |
| 変更が表示されない | ファイルを保存したか確認。別のアプリをクリックしてからGitHub Desktopに戻るか、アプリを再起動する |
| Pushがrejectedと言われる | 他の人が先にPushした可能性。**Fetch origin** → **Pull origin** → もう一度 **Push origin** をクリック |

## 基本ワークフロー

1. ファイルを編集・保存
2. GitHub Desktopで差分を確認
3. 説明的なメッセージを付けて、下部の青いコミットボタン（**Commit 1 file to main** のように表示）をクリック
4. **Push origin** でGitHubにバックアップ
5. 繰り返す

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) 作成（2025年12月7日）
