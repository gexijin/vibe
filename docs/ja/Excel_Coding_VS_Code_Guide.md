---
title: "VS CodeでClaude CodeとExcelを使う"
lang: "ja"
---
[ホーム](./)

# VS CodeでClaude CodeとExcelを使う

数式や書式、できればグラフも入ったスプレッドシートを作りたい。でも、Excelのメニューと格闘するのは避けたい。そんなときは、Claude CodeをExcelを知り尽くしたアシスタントだと考えてください。作りたいものを普段の言葉で説明するだけで、きちんと動く数式が入った本物の`.xlsx`ファイルを作ってくれます。このチュートリアルでは、VS Codeでプロジェクトフォルダを準備し、Claude CodeにExcelのスプレッドシートを作成・編集してもらう方法を紹介します。

## 主要な概念

- **xlsxスキル** - 本物の数式、書式、グラフを含む`.xlsx`スプレッドシートを作成・編集するためのClaude Codeの機能。Claudeアカウントでログインすると自動的に使えるようになります。裏側では、Claudeがこの機能を使って小さなPythonプログラムを書いて実行し、ファイルを作成します
- **[Spreadsheet Viewer拡張機能](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)**（旧名称：Excel Viewer） - エディターを離れずにスプレッドシートの数値をすばやく確認できるVS Code拡張機能。グラフは表示されません
- **数式と直接入力した数値の違い** - Claude Codeは実際のExcel数式（`=SUM(B2:B9)`など）を書くため、データを変更するとシートが自動で再計算されます

## 必要なもの

- [VS Codeを始めよう](./VS_Code_Getting_Started)を完了していること
- Claude Codeがインストールされ、動作していること（[WindowsにClaude Codeをインストール](./Install_CLAUDE_Code_Win)または[MacにClaude Codeをインストール](./Install_Claude_Code_MacOS)を参照）
- グラフを見るためのMicrosoft Excel、[LibreOffice Calc](https://www.libreoffice.org/download/download-libreoffice/)（無料）、またはGoogle Sheets（Webブラウザで無料で使えます）
- 20〜25分

## ステップ1：Pythonをインストール

ClaudeはPythonの小さなプログラムを書いてスプレッドシートを作るため、パソコンにPythonが必要です。あなた自身がPythonを書く必要はありません。

- **Windows**：
  - [python.org/downloads/windows](https://www.python.org/downloads/windows/)にアクセスします
  - 最新のPython 3リリースの下にある**Windows installer (64-bit)**をクリックします
  - ダウンロードしたファイルを実行します
  - 最初の画面の下部にある**「Add python.exe to PATH」のチェックボックスにチェックを入れてから**、**Install Now**をクリックします
- **Mac**：
  - [python.org/downloads](https://www.python.org/downloads/)にアクセスし、黄色の**Download Python**ボタンをクリックします
  - ダウンロードしたファイルを開き、**Continue**と**Install**をクリックしながらインストーラーの指示に従います

VS Codeをすでに開いている場合は、Pythonを認識させるために一度閉じてから開き直してください。

## ステップ2：VS CodeにSpreadsheet Viewer拡張機能をインストール

- VS Codeを開きます
- 左サイドバーの**Extensions**（拡張機能）アイコンをクリックします（または**View > Extensions**（表示 > 拡張機能）をクリック）
- `GrapeCity.gc-excelviewer`で検索します
- **MESCIUS**の**Spreadsheet Viewer**の**Install**（インストール）をクリックします

**注：** この拡張機能は以前、**GrapeCity**の**Excel Viewer**という名前でした。古いガイドや動画では今もその名前が使われていることがあります。現在「Excel Viewer」で検索すると他の拡張機能もいくつか表示されるため、正しいものを見つけるには上記のIDで検索してください。IDが今も`GrapeCity`で始まっているのは正常です。Marketplaceのページには現在は積極的にメンテナンスされていないと書かれていますが、このチュートリアルのファイルをプレビューするには問題なく使えます。

これで、どの`.xlsx`ファイルもクリックするだけで、そのシート、数値、数式をVS Code内で確認できるようになります。ちょっとした確認には便利ですが、グラフ、色付きの強調表示、ドロップダウンリストは表示できません。これらを見るには、Excel、LibreOffice Calc、またはGoogle Sheetsでファイルを開いてください。

## ステップ3：プロジェクトフォルダを作成

- パソコン上に新しいフォルダを作成します（例：`my-excel-project`）
- VS Codeで**File > Open Folder**（ファイル > フォルダーを開く）をクリックし、作成したフォルダを選択します
- **フォルダーの選択**（Select Folder、Windows）または**開く**（Open、Mac）をクリックします

## ステップ4：Claude Codeを起動

- VS Codeで**Terminal > New Terminal**（ターミナル > 新しいターミナル）をクリックします
- 次のコマンドを入力してEnterキーを押します：

```bash
claude
```

- 初めて使う場合は、認証のためにブラウザウィンドウが開きます。Claudeアカウントでログインしてください
- ターミナルにClaudeのウェルカムメッセージが表示されたら、VS Codeに戻ります

## ステップ5：最初のスプレッドシートを作成

- Claude Codeのターミナルに次のように入力します：

```
budget.xlsxという名前のスプレッドシートを作成してください。列は「カテゴリ」「月額」「メモ」の3つにしてください。家賃、食料品、光熱費などの支出カテゴリの例を6つ、現実的な金額で追加してください。一番下に「合計」行を追加し、数式を使って「月額」列を合計してください。
```

- Enterキーを押します
- ClaudeがPythonスクリプトを書いて実行し、プロジェクトフォルダに`budget.xlsx`を作成する様子を見守ります
- Claudeがコマンドの実行や補助ツール（スプレッドシート用のPythonの追加機能である`openpyxl`など）のインストールの許可を求めてきた場合は、**Yes**を選んで続けさせてください
- ClaudeからPythonがインストールされていない、または見つからないと言われた場合は、ステップ1に戻り、VS Codeを閉じてから開き直してください

## ステップ6：結果をプレビュー

- VS CodeのExplorerパネル（左側）で`budget.xlsx`をクリックします
- Spreadsheet Viewer拡張機能がファイルをスプレッドシートとして開きます
- 代わりに文字化けしたテキストや記号が表示された場合は、VS Codeがファイルをプレーンテキストとして開いています。下のトラブルシューティングを参照してください
- 一番下の**合計**セルをクリックします。入力された数値ではなく、数式になっていることを確認してください
- ExcelやLibreOffice Calcがインストールされている場合は、エクスプローラー（Windows）またはFinder（Mac）でファイルをダブルクリックして、そちらで開くこともできます

## ステップ7：Claudeにグラフの追加を依頼

- Claude Codeのターミナルに戻り、次のように入力します：

```
budget.xlsxに、月々の支出合計に対する各カテゴリの割合を示す円グラフを追加してください。
```

- Enterキーを押します
- グラフを見るには、`budget.xlsx`をExcelまたはLibreOffice Calcで開く（エクスプローラーまたはFinderでダブルクリックします）か、Google Sheetsにアップロードします
- VS CodeのSpreadsheet Viewerにはグラフが表示されませんが、これは正常です。グラフはファイルの中にちゃんと入っています

## ステップ8：データを編集してClaudeに更新を依頼

- ExcelまたはLibreOffice Calcで、金額の1つを変更します（例：家賃の値を2倍にする）
- ファイルを保存して閉じます
- この編集はSpreadsheet Viewerでは行わないでください。そこから保存すると、ファイルからグラフが消えてしまうことがあります
- Claude Codeのターミナルに次のように入力します：

```
budget.xlsxの数値をいくつか変更しました。合計を再計算して、グラフが引き続きデータと一致しているか確認してください。
```

- Enterキーを押します
- Claudeがあなたの編集内容を読み取り、数式をチェックして、すべてが正しく揃っていることを確認します

**ExcelやLibreOfficeがない場合は？** 手動での編集は飛ばして、代わりにClaudeに「budget.xlsxの家賃の金額を2倍にしてください。」と依頼してください。

これが基本のワークフローです。作りたいものを説明し、Claudeに作ってもらい、結果を確認し、普段の言葉で変更を依頼します。

## ステップ9：Claudeに乱雑なデータの整理を依頼

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
- より高度なリクエストを試してみましょう：「月額が5万円を超えるカテゴリが赤くなるように条件付き書式を追加して」
- 1枚目のシートのデータを集計する2枚目のシートを追加するようClaudeに依頼してみましょう
- [GitHub DesktopとClaude Codeを組み合わせて使う](./GitHub_Desktop_Claude_Code_Workflow)と組み合わせて、作業を進めながらスプレッドシートのバージョンを保存しましょう
- [Claude CodeでExcelの家計簿をVibe Coding](./Vibe_Coding_Excel_Guide)に進み、複数シートの本格的なプロジェクトを作りましょう

## トラブルシューティング

- **`budget.xlsx`が文字化けしたテキストや記号（`PK`で始まる）で開かれる**：スプレッドシートビューアーがファイルを処理しなかったため、VS Codeが生のファイルを表示しています。ファイル自体は問題ありません。`.xlsx`はプレーンテキストではなく圧縮されたファイルの集まりです。MESCIUSの**Spreadsheet Viewer**（`GrapeCity.gc-excelviewer`）がインストールされ、有効になっていることを確認してください。次にタブを閉じ、Explorerパネルで`budget.xlsx`を右クリックして**Open With...**（ファイルを開くアプリケーションの選択...）を選び、**Excel Editor**（Spreadsheet Viewerの`.xlsx`ファイル用エディター）を選択します。他のスプレッドシート拡張機能もインストールされている場合は、同じ一覧から**Configure default editor for '*.xlsx'...**（'*.xlsx' の既定のエディターを構成...）を選んで**Excel Editor**を選択すると、今後はファイルをクリックするだけでこのエディターが使われるようになります。
- **Spreadsheet Viewerのプレビューが空白または崩れて表示される**：タブを閉じてファイルを開き直してください。それでもうまくいかない場合は、代わりにExcel、LibreOffice Calc、またはGoogle Sheetsでファイルを開いてください。ファイル自体は問題なく、プレビューの一時的な不具合です。
- **数式のセルに数値ではなく空白が表示される**：通常、ファイルを書き込んだ後に再計算されていないことが原因です。Claudeに次のように依頼してください：「budget.xlsxを再計算して、数式エラーがないことを確認して」
- **Claudeの変更が反映されない**：Claudeが編集したのと同じファイルを見ているか確認してください（Claudeが示したファイル名を確認します）。VS Codeでタブを閉じて開き直すと、強制的に更新されます。
- **ターミナルに「claude is not recognized」と表示される**：Claude Codeが正しくインストールされていません。[Windows](./Install_CLAUDE_Code_Win)または[Mac](./Install_Claude_Code_MacOS)のインストールガイドをもう一度確認してください。
- **グラフが表示されない**：Spreadsheet Viewerではグラフを表示できません。Excel、LibreOffice Calc、またはGoogle Sheetsでファイルを開いてください。そこでもグラフがない場合は、Claudeに次のように依頼してください：「budget.xlsxから円グラフが消えています。もう一度追加してください。」

## ワークフロー概要

- **VS Code** - プロジェクトフォルダを管理し、Spreadsheet Viewer拡張機能でスプレッドシートをプレビューする場所
- **Claude Code** - 普段の言葉によるリクエストをもとに、動く数式を含む本物の`.xlsx`ファイルを作成・編集
- **Excel / LibreOffice / Google Sheets** - グラフを見たり、Claudeが作成したファイルを手動で微調整したりするために使用
- **反復** - 作りたいものを説明し、結果を確認し、次の変更を説明する

---

[Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/)が2026年9月21日に作成。
