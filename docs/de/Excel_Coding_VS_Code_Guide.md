---
title: "Claude Code mit Excel in VS Code verwenden"
lang: "de"
---
[Startseite](./)

# Claude Code mit Excel in VS Code verwenden

Sie möchten eine Tabelle erstellen – mit Formeln, Formatierung, vielleicht einem Diagramm –, aber keine Lust, sich durch die Menüs von Excel zu kämpfen. Stellen Sie sich Claude Code als Assistenten vor, der Excel in- und auswendig kennt: Sie beschreiben in einfachen Worten, was Sie möchten, und er erstellt eine echte `.xlsx`-Datei mit funktionierenden Formeln. Dieses Tutorial zeigt Ihnen, wie Sie in VS Code einen Projektordner einrichten und Claude Code Excel-Tabellen für Sie erstellen und bearbeiten lassen.

## Wichtige Konzepte

- **xlsx-Skill** - Fähigkeit von Claude Code, `.xlsx`-Tabellen mit echten Formeln, Formatierung und Diagrammen zu erstellen und zu bearbeiten. Sie steht automatisch zur Verfügung, wenn Sie sich mit Ihrem Claude-Konto anmelden. Im Hintergrund nutzt Claude sie, um kleine Python-Programme zu schreiben und auszuführen, die die Datei erstellen
- **[Spreadsheet Viewer-Erweiterung](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)** (früher Excel Viewer) - VS Code-Erweiterung, mit der Sie die Zahlen in einer Tabelle schnell prüfen können, ohne den Editor zu verlassen. Diagramme zeigt sie nicht an
- **Formeln statt fest eingetragener Zahlen** - Claude Code schreibt echte Excel-Formeln (wie `=SUM(B2:B9)`), sodass Ihre Tabelle neu rechnet, wenn Sie die Daten ändern. In einem deutschen Excel oder LibreOffice sehen Sie dieselbe Formel als `=SUMME(B2:B9)` – das ist normal, das Programm übersetzt die Formelnamen automatisch

## Was Sie benötigen

- Abgeschlossenes Tutorial [Erste Schritte mit VS Code](./VS_Code_Getting_Started)
- Claude Code installiert und funktionsfähig (siehe [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win) oder [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS))
- Microsoft Excel, [LibreOffice Calc](https://de.libreoffice.org/download/download/) (kostenlos) oder Google Sheets (kostenlos in Ihrem Webbrowser), um Diagramme zu sehen
- 20-25 Minuten

## Schritt 1: Python installieren

Claude erstellt Tabellen, indem es kleine Python-Programme schreibt. Deshalb braucht Ihr Computer Python. Sie selbst müssen kein Python schreiben.

- **Windows**:
  - Gehen Sie zu [python.org/downloads/windows](https://www.python.org/downloads/windows/) (die Seite ist auf Englisch)
  - Klicken Sie unter der neuesten Python 3-Version auf **Windows installer (64-bit)**
  - Führen Sie die heruntergeladene Datei aus
  - **Aktivieren Sie das Kästchen „Add python.exe to PATH“** unten im ersten Fenster und klicken Sie dann auf **Install Now**
- **Mac**:
  - Gehen Sie zu [python.org/downloads](https://www.python.org/downloads/) und klicken Sie auf die gelbe Schaltfläche **Download Python**
  - Öffnen Sie die heruntergeladene Datei und folgen Sie dem Installationsprogramm, indem Sie auf **Fortfahren** und **Installieren** klicken

Falls VS Code bereits geöffnet ist, schließen Sie es und öffnen Sie es erneut, damit es Python findet.

## Schritt 2: Die Spreadsheet Viewer-Erweiterung in VS Code installieren

- Öffnen Sie VS Code
- Klicken Sie in der linken Seitenleiste auf das Symbol **Extensions** (oder klicken Sie auf **View > Extensions**)
- Suchen Sie nach `GrapeCity.gc-excelviewer`
- Klicken Sie bei **Spreadsheet Viewer** von **MESCIUS** auf **Install**

**Hinweis:** Diese Erweiterung hieß früher **Excel Viewer** von **GrapeCity**, und ältere Anleitungen und Videos verwenden eventuell noch diesen Namen. Eine Suche nach „Excel Viewer" zeigt inzwischen mehrere andere Erweiterungen an. Suchen Sie daher nach der oben genannten ID, um die richtige zu finden. Die ID beginnt weiterhin mit `GrapeCity` – das ist so gewollt.

Damit können Sie jede `.xlsx`-Datei anklicken und ihre Tabellenblätter, Zahlen und Formeln direkt in VS Code sehen. Das ist ideal für schnelle Kontrollen, aber Diagramme, farbige Hervorhebungen und Dropdown-Listen kann die Erweiterung nicht anzeigen – dafür öffnen Sie die Datei in Excel, LibreOffice Calc oder Google Sheets.

## Schritt 3: Ihren Projektordner erstellen

- Erstellen Sie einen neuen Ordner auf Ihrem Computer (z.B. `my-excel-project`)
- Klicken Sie in VS Code auf **File > Open Folder** und wählen Sie Ihren neuen Ordner aus
- Klicken Sie auf **Ordner auswählen** (Windows) oder **Öffnen** (Mac) – bei englischer Anzeige heißen die Schaltflächen **Select Folder** bzw. **Open**

## Schritt 4: Claude Code starten

- Klicken Sie in VS Code auf **Terminal > New Terminal**
- Geben Sie diesen Befehl ein und drücken Sie Enter:

```bash
claude
```

- Wenn Sie Claude Code zum ersten Mal verwenden, öffnet sich ein Browserfenster zur Authentifizierung – melden Sie sich mit Ihrem Claude-Konto an
- Kehren Sie zu VS Code zurück, sobald Sie die Willkommensnachricht von Claude im Terminal sehen

## Schritt 5: Ihre erste Tabelle erstellen

- Geben Sie im Claude Code-Terminal ein:

```
Erstelle eine Tabelle namens budget.xlsx mit den Spalten Kategorie, Monatsbetrag und Notizen. Füge 6 Beispiel-Ausgabenkategorien wie Miete, Lebensmittel und Nebenkosten mit realistischen Beträgen hinzu. Füge unten eine Zeile „Summe" hinzu, die die Spalte Monatsbetrag mit einer Formel addiert.
```

- Drücken Sie Enter
- Beobachten Sie, wie Claude ein Python-Skript schreibt, es ausführt und `budget.xlsx` in Ihrem Projektordner erzeugt
- Claude bittet um Erlaubnis, bevor es Befehle ausführt oder Hilfswerkzeuge installiert (wie `openpyxl`, eine Python-Erweiterung für Tabellen) – wählen Sie **Yes**, damit es weitermachen kann
- Wenn Claude meldet, dass Python nicht installiert ist oder nicht gefunden wird, gehen Sie zurück zu Schritt 1 und schließen und öffnen Sie VS Code danach erneut

## Schritt 6: Das Ergebnis ansehen

- Klicken Sie im Explorer-Bereich von VS Code (links) auf `budget.xlsx`
- Die Spreadsheet Viewer-Erweiterung öffnet die Datei als Tabelle
- Wenn Sie stattdessen wirre Zeichen und Symbole sehen, hat VS Code die Datei als reinen Text geöffnet – siehe Fehlerbehebung unten
- Klicken Sie unten auf die Zelle **Summe** – Sie werden sehen, dass es sich um eine Formel handelt und nicht um eine eingetippte Zahl
- Wenn Sie Excel oder LibreOffice Calc installiert haben, können Sie die Datei stattdessen auch im Datei-Explorer (Windows) oder im Finder (Mac) doppelklicken, um sie dort zu öffnen

## Schritt 7: Claude bitten, ein Diagramm hinzuzufügen

- Geben Sie wieder im Claude Code-Terminal ein:

```
Füge budget.xlsx ein Kreisdiagramm hinzu, das den Anteil jeder Kategorie an den gesamten monatlichen Ausgaben zeigt.
```

- Drücken Sie Enter
- Um das Diagramm zu sehen, öffnen Sie `budget.xlsx` in Excel oder LibreOffice Calc (doppelklicken Sie die Datei im Datei-Explorer oder im Finder) oder laden Sie sie in Google Sheets hoch
- Der Spreadsheet Viewer in VS Code zeigt das Diagramm nicht an – das ist normal, das Diagramm ist trotzdem in der Datei

## Schritt 8: Die Daten bearbeiten und Claude um eine Aktualisierung bitten

- Ändern Sie in Excel oder LibreOffice Calc einen der Beträge (verdoppeln Sie zum Beispiel den Wert für Miete)
- Speichern und schließen Sie die Datei
- Nehmen Sie diese Änderung nicht im Spreadsheet Viewer vor – beim Speichern von dort aus kann das Diagramm aus der Datei verschwinden
- Geben Sie im Claude Code-Terminal ein:

```
Ich habe einige Zahlen in budget.xlsx geändert. Berechne die Summen neu und stelle sicher, dass das Diagramm noch zu den Daten passt.
```

- Drücken Sie Enter
- Claude liest Ihre Änderungen, prüft die Formeln und bestätigt, dass alles zusammenpasst

**Kein Excel oder LibreOffice?** Überspringen Sie die Änderung von Hand und bitten Sie stattdessen Claude: „Verdopple den Betrag für Miete in budget.xlsx.“

Das ist der zentrale Arbeitsablauf: Beschreiben Sie, was Sie möchten, lassen Sie Claude es erstellen, prüfen Sie das Ergebnis und bitten Sie in einfachen Worten um Änderungen.

## Schritt 9: Claude bitten, unordentliche Daten zu bereinigen

Claude Code ist auch nützlich, um Tabellen zu reparieren, die bereits durcheinander sind.

- Geben Sie ein:

```
Erstelle eine Datei messy_sales.csv mit 15 Zeilen Verkaufsdaten, die einige Probleme enthält: ein paar leere Zellen, uneinheitliche Datumsformate und eine doppelte Zeile. Erstelle dann eine bereinigte Version namens sales_clean.xlsx, die diese Probleme behebt, und erkläre, was du behoben hast.
```

- Drücken Sie Enter
- Lesen Sie die Zusammenfassung, die Claude Ihnen darüber gibt, was es gefunden und behoben hat
- Öffnen Sie `sales_clean.xlsx`, um zu prüfen, ob die Daten richtig aussehen

## Nächste Schritte

- Bitten Sie Claude, eine Tabelle aus einer CSV-Datei zu erstellen, die Sie bereits haben (ziehen Sie sie zuerst in Ihren Projektordner)
- Probieren Sie anspruchsvollere Anfragen aus: „Füge eine bedingte Formatierung hinzu, sodass jede Kategorie über $500 rot wird"
- Bitten Sie Claude, ein zweites Tabellenblatt hinzuzufügen, das die Daten aus dem ersten Blatt zusammenfasst
- Kombinieren Sie dies mit [GitHub Desktop mit Claude Code verwenden](./GitHub_Desktop_Claude_Code_Workflow), um nach und nach Versionen Ihrer Tabellen zu speichern
- Machen Sie weiter mit [Vibe Coding eines Budget-Trackers in Excel](./Vibe_Coding_Excel_Guide), um ein vollständiges Projekt mit mehreren Tabellenblättern zu erstellen

## Fehlerbehebung

- **`budget.xlsx` öffnet sich als wirrer Text mit Symbolen (beginnend mit `PK`)**: VS Code zeigt die Rohdatei an, weil kein Tabellen-Viewer sie übernommen hat. Die Datei selbst ist in Ordnung – eine `.xlsx`-Datei ist ein komprimiertes Paket und kein reiner Text. Prüfen Sie, ob **Spreadsheet Viewer** von MESCIUS (`GrapeCity.gc-excelviewer`) installiert und aktiviert ist. Schließen Sie dann den Tab, klicken Sie im Explorer-Bereich mit der rechten Maustaste auf `budget.xlsx`, wählen Sie **Open With...** und dann **Excel Editor** (den Editor von Spreadsheet Viewer für `.xlsx`-Dateien). Wenn zusätzlich eine andere Tabellen-Erweiterung installiert ist, wählen Sie in derselben Liste **Configure default editor for '*.xlsx'...** und dann **Excel Editor**, damit die Datei künftig schon mit einem einfachen Klick darin geöffnet wird.
- **Spreadsheet Viewer zeigt eine leere oder fehlerhafte Vorschau**: Schließen Sie den Tab und öffnen Sie die Datei erneut. Wenn es immer noch nicht funktioniert, öffnen Sie die Datei stattdessen in Excel, LibreOffice Calc oder Google Sheets – die Datei selbst ist in Ordnung, es handelt sich nur um einen Fehler in der Vorschau.
- **Formelzellen sind leer statt eine Zahl anzuzeigen**: Das bedeutet meist, dass die Datei nach dem Schreiben nicht neu berechnet wurde. Bitten Sie Claude: „Berechne budget.xlsx neu und bestätige, dass es keine Formelfehler gibt."
- **Die Änderungen von Claude werden nicht angezeigt**: Stellen Sie sicher, dass Sie sich dieselbe Datei ansehen, die Claude bearbeitet hat (prüfen Sie den Dateinamen, den Claude nennt). Schließen und öffnen Sie den Tab in VS Code erneut, um eine Aktualisierung zu erzwingen.
- **„claude is not recognized“ im Terminal**: Claude Code ist nicht korrekt installiert. Sehen Sie sich die Installationsanleitung für [Windows](./Install_CLAUDE_Code_Win) oder [Mac](./Install_Claude_Code_MacOS) noch einmal an.
- **Das Diagramm fehlt**: Der Spreadsheet Viewer kann keine Diagramme anzeigen. Öffnen Sie die Datei in Excel, LibreOffice Calc oder Google Sheets. Wenn das Diagramm dort ebenfalls fehlt, bitten Sie Claude: „Das Kreisdiagramm fehlt in budget.xlsx – bitte füge es wieder hinzu.“

## Workflow-Zusammenfassung

- **VS Code** - Ihr Projektordner und ein Ort, um Tabellen mit der Spreadsheet Viewer-Erweiterung anzusehen
- **Claude Code** - Schreibt und bearbeitet echte `.xlsx`-Dateien mit funktionierenden Formeln, basierend auf Ihren Anfragen in einfachen Worten
- **Excel / LibreOffice / Google Sheets** - Um Diagramme anzusehen und die von Claude erstellten Dateien von Hand anzupassen
- **Iterieren** - Beschreiben Sie, was Sie möchten, prüfen Sie das Ergebnis, beschreiben Sie die nächste Änderung

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 21. September 2026.
