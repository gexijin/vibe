[Startseite](./)

# Claude Code mit RStudio auf dem Mac verwenden

Sie haben RStudio auf dem Mac zum Ausführen von R-Code und Claude Code für KI-gestützte Programmierunterstützung. Dieses Tutorial zeigt Ihnen, wie Sie beide Tools zusammen mit denselben Projektdateien verwenden können. Sie erstellen ein R-Projekt, schreiben etwas Code manuell und verwenden dann Claude Code vom Terminal aus, um es mit Visualisierungen und Analysen zu erweitern – während RStudio geöffnet bleibt, um Ihren Code auszuführen und zu testen.

## Wichtige Konzepte

- **Terminal** - Die Befehlszeilenschnittstelle des Mac, in der Claude Code läuft
- **Geteilte Dateien** - Sowohl RStudio als auch Claude Code arbeiten an denselben Dateien in Ihrem Dokumente-Ordner
- **Hybrid-Workflow** - RStudio führt Code aus; Claude Code schreibt und verbessert ihn

## Was Sie benötigen

- Abgeschlossene Anleitung [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS)
- RStudio auf dem Mac installiert
- 20-30 Minuten

## Schritt 1: RStudio auf dem Mac öffnen

- Klicken Sie auf **Launchpad** in Ihrem Dock (das Symbol mit dem Punkteraster)
- Geben Sie `RStudio` in das Suchfeld ein
- Klicken Sie auf **RStudio**, um es zu öffnen
- Das RStudio-Fenster öffnet sich mit mehreren Bereichen

## Schritt 2: Ein neues R-Projekt erstellen

- Klicken Sie in RStudio im oberen Menü auf **File**
- Klicken Sie auf **New Project...**
- Wählen Sie **New Directory**
- Wählen Sie **New Project**
- Geben Sie als **Directory name** ein: `test_claude`
- Klicken Sie auf **Browse** neben „Create project as subdirectory of:"
- Navigieren Sie zu Ihrem **Dokumente**-Ordner
- Klicken Sie auf **Open**
- Klicken Sie auf **Create Project**
- RStudio erstellt das Projekt und wechselt dorthin

## Schritt 3: Ein neues R-Skript erstellen

- Klicken Sie in RStudio auf **File > New File > R Script**
- Ein neues leeres Skript öffnet sich im oberen linken Bereich
- Klicken Sie auf **File > Save** (oder drücken Sie **Command (⌘) + S**)
- Nennen Sie die Datei: `iris.R`
- Klicken Sie auf **Save**

## Schritt 4: Ersten Code manuell schreiben

Geben Sie diesen Code in Ihre `iris.R`-Datei ein:

```r
data(iris)
str(iris)
summary(iris)
```

- Klicken Sie auf **File > Save**, um Ihre Änderungen zu speichern (oder drücken Sie **Command (⌘) + S**)
- Um den Code auszuführen: Markieren Sie alle Zeilen und klicken Sie auf die **Run**-Schaltfläche (oben rechts im Skriptbereich)
- Sie sollten die Ausgabe im Console-Bereich sehen, die Datensatzstruktur und Statistiken zeigt

## Schritt 5: Terminal öffnen

- Öffnen Sie den **Finder** und klicken Sie in der linken Seitenleiste auf **Programme**
- Öffnen Sie den Ordner **Dienstprogramme**
- Doppelklicken Sie auf **Terminal**
- Das Terminal-Fenster öffnet sich

## Schritt 6: Zu Ihrem Projektordner navigieren

- Geben Sie im Terminal diesen Befehl ein:
  ```
  cd ~/Documents/test_claude
  ```
- Überprüfen Sie, ob Sie am richtigen Ort sind, indem Sie eingeben:
  ```
  ls
  ```
- Sie sollten `iris.R` und `test_claude.Rproj` aufgelistet sehen

**Tipp:** Wenn Sie sich beim genauen Pfad nicht sicher sind, können Sie den Ordner aus dem Finder per Drag & Drop ins Terminal ziehen und der vollständige Pfad erscheint automatisch!

## Schritt 7: Claude Code starten

- Geben Sie im Terminal ein:
  ```
  claude
  ```
- Claude Code startet und zeigt eine Willkommensnachricht
- Möglicherweise müssen Sie sich authentifizieren, wenn dies Ihre erste Sitzung ist
- Sie sind nun bereit, KI-Unterstützung für Ihr R-Projekt zu nutzen

## Schritt 8: Claude um ein Streudiagramm bitten

Wenn Claude Code langsam ist oder nicht reagiert, warten Sie einfach, bis es initialisiert ist. Dann geben Sie diese Anfrage ein:

```
Füge Code zu iris.R hinzu, um ein Streudiagramm der Kelchblattlänge gegen die Kelchblattbreite zu erstellen, gefärbt nach Art. Verwende ggplot2.
```
- Claude Code liest Ihre `iris.R`-Datei und fügt den Visualisierungscode hinzu
- Wenn Sie gefragt werden, geben Sie Claude die Erlaubnis, die iris.R-Datei zu bearbeiten, indem Sie die entsprechende Option wählen
- Warten Sie, bis Claude fertig ist (Sie sehen eine Bestätigungsnachricht)


## Schritt 9: Den neuen Code in RStudio ausführen

- Wechseln Sie zurück zu RStudio (klicken Sie auf das RStudio-Fenster oder drücken Sie **Command (⌘) + Tab**)
- Möglicherweise sehen Sie eine Aufforderung, dass die Datei geändert wurde – klicken Sie auf **Ja**, um sie neu zu laden
- Wenn keine Aufforderung erscheint, klicken Sie auf **File > Reopen with Encoding > UTF-8**
- Markieren Sie den gesamten Code und klicken Sie auf **Run**
- Ein Streudiagramm erscheint im **Plots**-Bereich (unten rechts)
- Wenn Sie einen Fehler zu ggplot2 erhalten, installieren Sie es durch Eingabe von `install.packages("ggplot2")` im Console-Bereich

## Schritt 10: Das Streudiagramm verfeinern

- Wechseln Sie zum Terminal (drücken Sie **Command (⌘) + Tab** oder klicken Sie auf das Terminal-Fenster)
- Geben Sie diese Anfrage ein:
  ```
  Entferne den Titel. Ändere die Markierungsart nach Art. Wechsle zum Classic-Theme.
  ```

## Schritt 11: Das verfeinerte Diagramm ansehen

- Wechseln Sie zu RStudio
- Laden Sie die Datei neu, wenn Sie dazu aufgefordert werden
- Markieren Sie den aktualisierten Code und klicken Sie auf **Run**
- Das Diagramm sollte jetzt ohne Titel angezeigt werden, mit verschiedenen Markierungsformen für jede Art und im Classic-Theme

## Schritt 12: Claude um PCA-Plot bitten

- Wechseln Sie zum Terminal
- Geben Sie diese Anfrage ein:
  ```
  Füge Code hinzu, um eine PCA für die numerischen Variablen durchzuführen und die Proben mithilfe der ersten beiden Hauptkomponenten zu plotten.
  ```

## Schritt 13: Die PCA-Analyse ausführen

- Wechseln Sie zu RStudio
- Laden Sie die Datei neu, wenn Sie dazu aufgefordert werden
- Markieren Sie den gesamten Code und klicken Sie auf **Run**
- Ein PCA-Plot erscheint, der Proben auf PC1 und PC2 projiziert zeigt, gefärbt nach Art

## Schritt 14: Claude um Überprüfung und Kommentare bitten

- Wechseln Sie zum Terminal
- Geben Sie diese Anfrage ein:
  ```
  Überprüfe das gesamte Skript auf Korrektheit. Füge Kommentare hinzu, wenn nötig.
  ```
- Claude überprüft den Code und fügt umfassende Kommentare hinzu

## Schritt 15: Claude bitten, R Markdown zu erstellen

- Wechseln Sie zum Terminal
- Geben Sie diese Anfrage ein:
  ```
  Erstelle eine neue R-Markdown-Datei für diese Analyse. Speichere sie als iris_report.Rmd
  ```
- Claude wird Sie um Erlaubnis bitten, diese Datei zu erstellen
- Claude erstellt eine neue `.Rmd`-Datei in Ihrem Projektordner


## Schritt 16: Die R-Markdown-Datei kompilieren

- Wechseln Sie zu RStudio
- Klicken Sie auf **File > Open File...**
- Wählen Sie `iris_report.Rmd` und klicken Sie auf **Open**
- Klicken Sie auf die **Knit**-Schaltfläche (mit einem Wollknäuel-Symbol) oben im Skriptbereich
- RStudio generiert einen HTML-Bericht
- Der Bericht öffnet sich in einem neuen Fenster und zeigt Ihre vollständige Analyse mit erzählendem Text
- Die HTML-Datei wird in Ihrem Projektordner gespeichert

## Fehlerbehebung

- **RStudio zeigt Dateiänderungen nicht an** - Klicken Sie auf **File > Reopen with Encoding > UTF-8**, um die Datei manuell neu zu laden, oder schließen Sie die Datei und öffnen Sie sie erneut.
- **„claude: command not found"** - Stellen Sie sicher, dass Sie die [Installationsanleitung](./Install_Claude_Code_MacOS) abgeschlossen haben. Versuchen Sie, ein neues Terminal-Fenster zu öffnen, oder schließen Sie Terminal vollständig (**Command (⌘) + Q**) und öffnen Sie es erneut.
- **Plots erscheinen nicht** - Stellen Sie sicher, dass ggplot2 installiert ist. Führen Sie `install.packages("ggplot2")` in der RStudio-Konsole aus, wenn nötig.
- **„No such file or directory"** - Überprüfen Sie, ob Sie den Pfad in Schritt 6 korrekt eingegeben haben. Versuchen Sie den Drag-and-Drop-Trick: Ziehen Sie den test_claude-Ordner aus dem Finder ins Terminal, nachdem Sie `cd ` (mit einem Leerzeichen) eingegeben haben.
- **Claude Code ist bei der ersten Anfrage langsam** - Warten Sie 30-60 Sekunden, bis Claude initialisiert ist. Nachfolgende Anfragen werden schneller sein.

## Mac-Tastenkombinationen

Nützliche Tastenkombinationen zum Wechseln zwischen Apps:
- **Command (⌘) + Tab** - Schnell zwischen geöffneten Anwendungen wechseln
- **Command (⌘) + `** (Backtick) - Zwischen Fenstern derselben Anwendung wechseln
- **Command (⌘) + Leertaste** - Spotlight-Suche öffnen (um Apps zu öffnen)
- **Command (⌘) + Q** - Eine Anwendung vollständig beenden

## Nächste Schritte

- Versuchen Sie, Claude zu bitten, statistische Tests (t-Tests, ANOVA) zu Ihrer Analyse hinzuzufügen
- Bitten Sie Claude, eine **Python-Version** dieses Codes zu erstellen und ein Quarto-Dokument vorzubereiten
- Bitten Sie Claude, Funktionen für sich wiederholende Aufgaben in Ihren R-Skripten zu erstellen
- Verwenden Sie Claude, um Fehlermeldungen zu debuggen, wenn Ihr R-Code nicht läuft
- Erkunden Sie, wie Sie Claude bitten können, langsamen R-Code für bessere Leistung zu optimieren

## Workflow-Zusammenfassung

Diese Hybrid-Einrichtung kombiniert das Beste aus beiden Welten:

- **RStudio (Mac)** - Interaktive R-Konsole, sofortige Plot-Anzeige, vertraute GUI zum Ausführen von Code
- **Claude Code (Terminal)** - KI-gestützte Codegenerierung, Überprüfung und Verbesserung
- **Geteilte Dateien** - Beide Tools arbeiten an denselben Dateien in Ihrem Dokumente-Ordner
- **Iterative Verfeinerung** - Beginnen Sie mit manuellem Code, verbessern Sie mit Claude, testen Sie in RStudio, dann verfeinern Sie weiter
- **Dokumentation** - Claude kann umfassende Berichte und Kommentare für Ihre Analyse generieren

Der Workflow ist einfach: Schreiben oder bearbeiten Sie Code mit Claude im Terminal, dann testen und führen Sie ihn sofort in RStudio aus. Kein Dateikopieren oder manuelles Synchronisieren nötig – beide Anwendungen greifen nahtlos auf dieselben Dateien auf Ihrem Mac zu.

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2024.
