---
title: "VS CodeでClaude CodeとExcelを使う"
lang: "ja"
---
[ホーム](./)

# VS CodeでClaude CodeとExcelを使う

数式や書式、できればグラフも入ったスプレッドシートを作りたい。でも、Excelのメニューと格闘するのは避けたい。そんなときは、Claude CodeをExcelを知り尽くしたアシスタントだと考えてください。作りたいものを普段の言葉で説明するだけで、きちんと動く数式が入った本物の`.xlsx`ファイルを作ってくれます。このチュートリアルでは、VS Codeでプロジェクトフォルダを準備し、Claude CodeにExcelのスプレッドシートを作成・編集してもらう方法を紹介します。

## 主要な概念

- **xlsxスキル** - 本物の数式、書式、グラフを含む`.xlsx`スプレッドシートを作成・編集するための、Claude Codeに組み込まれた機能
- **[Spreadsheet Viewer拡張機能](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)**（旧名称：Excel Viewer） - エディターを離れずにスプレッドシートファイルをプレビュー・編集できるVS Code拡張機能
- **数式と直接入力した数値の違い** - Claude Codeは実際のExcel数式（`=SUM(B2:B9)`など）を書くため、データを変更するとシートが自動で再計算されます

## 必要なもの

- [VS Codeの基本](./VS_Code_Getting_Started)を完了していること
- Claude Codeがインストールされ、動作していること（[WindowsにClaude Codeをインストール](./Install_CLAUDE_Code_Win)または[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS)を参照）
- 完成したファイルを開くためのMicrosoft Excel、LibreOffice Calc、またはGoogle Sheets（任意 - Spreadsheet Viewer拡張機能はこれらがなくても使えます）
- 15〜20分

## ステップ1：VS CodeにSpreadsheet Viewer拡張機能をインストール

- VS Codeを開きます
- 左サイドバーの**Extensions**アイコンをクリックします（または**View > Extensions**をクリック）
- `GrapeCity.gc-excelviewer`で検索します
- **MESCIUS**の**Spreadsheet Viewer**の**Install**をクリックします

**注：** この拡張機能は以前、**GrapeCity**の**Excel Viewer**という名前でした。古いガイドや動画では今もその名前が使われていることがあります。現在「Excel Viewer」で検索すると他の拡張機能もいくつか表示されるため、正しいものを見つけるには上記のIDで検索してください。IDが今も`GrapeCity`で始まっているのは正常です。

これで、どの`.xlsx`ファイルもクリックするだけで、別のアプリに切り替えることなくVS Code内でスプレッドシートとして表示できるようになります。

## ステップ2：プロジェクトフォルダを作成

- パソコン上に新しいフォルダを作成します（例：`my-excel-project`）
- VS Codeで**File > Open Folder**をクリックし、作成したフォルダを選択します
- **Select Folder**（Windows）または**Open**（Mac）をクリックします

## ステップ3：Claude Codeを起動

- VS Codeで**Terminal > New Terminal**をクリックします
- 次のコマンドを入力してEnterキーを押します：

```bash
claude
```

- 初めて使う場合は、認証のためにブラウザウィンドウが開きます。Claudeアカウントでログインしてください
- ターミナルにClaudeのウェルカムメッセージが表示されたら、VS Codeに戻ります

## ステップ4：最初のスプレッドシートを作成

- Claude Codeのターミナルに次のように入力します：

```
budget.xlsxという名前のスプレッドシートを作成してください。列は「カテゴリ」「月額」「メモ」の3つにしてください。家賃、食料品、光熱費などの支出カテゴリの例を6つ、現実的な金額で追加してください。一番下に「合計」行を追加し、数式を使って「月額」列を合計してください。
```

- Enterキーを押します
- ClaudeがPythonスクリプトを書いて実行し、プロジェクトフォルダに`budget.xlsx`を作成する様子を見守ります
- Claudeはファイルの再計算も行うため、数式のセルは空白ではなく実際の数値が表示されます

## ステップ5：結果をプレビュー

- VS CodeのExplorerパネル（左側）で`budget.xlsx`をクリックします
- Spreadsheet Viewer拡張機能がファイルをスプレッドシートとして開きます
- 代わりに文字化けしたテキストや記号が表示された場合は、VS Codeがファイルをプレーンテキストとして開いています。下のトラブルシューティングを参照してください
- 一番下の**合計**セルをクリックします。入力された数値ではなく、数式になっていることを確認してください
- ExcelやLibreOffice Calcがインストールされている場合は、エクスプローラー（Windows）またはFinder（Mac）でファイルをダブルクリックして、そちらで開くこともできます

## ステップ6：Claudeにグラフの追加を依頼

- Claude Codeのターミナルに戻り、次のように入力します：

```
budget.xlsxに、月々の支出合計に対する各カテゴリの割合を示す円グラフを追加してください。
```

- Enterキーを押します
- Spreadsheet Viewerのタブで`budget.xlsx`を開き直し（更新アイコンをクリックするか、ファイルを閉じて開き直します）、新しいグラフを確認します

## ステップ7：データを編集してClaudeに更新を依頼

- Spreadsheet Viewer、またはExcel/LibreOfficeで開いている場合はそちらで、金額の1つを変更します（例：家賃の値を2倍にする）
- ファイルを保存します
- Claude Codeのターミナルに次のように入力します：

```
budget.xlsxの数値をいくつか変更しました。合計を再計算して、グラフが引き続きデータと一致しているか確認してください。
```

- Enterキーを押します
- Claudeがあなたの編集内容を読み取り、数式を再計算して、すべてが正しく揃っていることを確認します

これが基本のワークフローです。作りたいものを説明し、Claudeに作ってもらい、結果を確認し、普段の言葉で変更を依頼します。

## ステップ8：Claudeに乱雑なデータの整理を依頼

Claude Codeは、すでに散らかってしまったスプレッドシートを直すのにも役立ちます。

- 次のように入力します：

```
問題を含む15行の売上データを持つmessy_sales.csvファイルを作成してください。問題とは、いくつかの空白セル、統一されていない日付形式、1つの重複行です。次に、これらの問題を修正したクリーンなバージョンをsales_clean.xlsxという名前で作成し、何を修正したか説明してください。
```

- Enterキーを押します
- Claudeが見つけて修正した内容の要約を確認します
- `sales_clean.xlsx`を開き、データが正しく見えることを確認します

## 次のステップ

- 手元にあるCSVファイルからスプレッドシートを作るようClaudeに依頼してみましょう（先にファイルをプロジェクトフォルダにドラッグしておきます）
- より高度なリクエストを試してみましょう：「$500を超えるカテゴリが赤くなるように条件付き書式を追加して」
- 1枚目のシートのデータを集計する2枚目のシートを追加するようClaudeに依頼してみましょう
- [GitHub DesktopとClaude Codeを使用](./GitHub_Desktop_Claude_Code_Workflow)と組み合わせて、作業を進めながらスプレッドシートのバージョンを保存しましょう
- [Claude CodeでExcelの家計簿をVibe Coding](./Vibe_Coding_Excel_Guide)に進み、複数シートの本格的なプロジェクトを作りましょう

## トラブルシューティング

- **`budget.xlsx`が文字化けしたテキストや記号（`PK`で始まる）で開かれる**：スプレッドシートビューアーがファイルを処理しなかったため、VS Codeが生のファイルを表示しています。ファイル自体は問題ありません。`.xlsx`はプレーンテキストではなく圧縮されたファイルの集まりです。MESCIUSの**Spreadsheet Viewer**（`GrapeCity.gc-excelviewer`）がインストールされ、有効になっていることを確認してください。次にタブを閉じ、Explorerパネルで`budget.xlsx`を右クリックして**Open With...**を選び、**Excel Editor**（Spreadsheet Viewerの`.xlsx`ファイル用エディター）を選択します。他のスプレッドシート拡張機能もインストールされている場合は、同じ一覧から**Configure default editor for '*.xlsx'...**を選んで**Excel Editor**を選択すると、今後はファイルをクリックするだけでこのエディターが使われるようになります。
- **Spreadsheet Viewerのプレビューが空白または崩れて表示される**：タブを閉じてファイルを開き直してください。それでもうまくいかない場合は、代わりにExcel、LibreOffice Calc、またはGoogle Sheetsでファイルを開いてください。ファイル自体は問題なく、プレビューの一時的な不具合です。
- **数式のセルに数値ではなく空白が表示される**：通常、ファイルを書き込んだ後に再計算されていないことが原因です。Claudeに次のように依頼してください：「budget.xlsxを再計算して、数式エラーがないことを確認して」
- **Claudeの変更が反映されない**：Claudeが編集したのと同じファイルを見ているか確認してください（Claudeが示したファイル名を確認します）。VS Codeでタブを閉じて開き直すと、強制的に更新されます。
- **ターミナルに「claude is not recognized」と表示される**：Claude Codeが正しくインストールされていません。お使いのプラットフォーム向けの[インストールガイド](./Install_CLAUDE_Code_Win)をもう一度確認してください。

## ワークフロー概要

- **VS Code** - プロジェクトフォルダを管理し、Spreadsheet Viewer拡張機能でスプレッドシートをプレビューする場所
- **Claude Code** - 普段の言葉によるリクエストをもとに、動く数式を含む本物の`.xlsx`ファイルを作成・編集
- **Excel / LibreOffice / Google Sheets** - 任意。Claudeが作成したファイルを開いたり、手動で微調整したりするために使用
- **反復** - 作りたいものを説明し、結果を確認し、次の変更を説明する

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2026年9月21日に作成。
