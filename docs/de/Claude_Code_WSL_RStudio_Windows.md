[Startseite](./)

# Claude Code aus WSL mit RStudio unter Windows verwenden

Sie haben RStudio unter Windows zum Ausführen von R-Code und Claude Code in WSL für KI-gestützte Programmierunterstützung. Dieses Tutorial zeigt Ihnen, wie Sie beide Tools zusammen mit denselben Projektdateien verwenden können. Sie erstellen ein R-Projekt in Windows, schreiben etwas Code manuell und verwenden dann Claude Code vom Ubuntu-Terminal aus, um es mit Visualisierungen und Analysen zu erweitern – während RStudio geöffnet bleibt, um Ihren Code auszuführen und zu testen.

## Wichtige Konzepte

- **WSL (Windows Subsystem for Linux)** - Führt Ubuntu Linux innerhalb von Windows aus, wo Claude Code installiert ist
- **Pfadübersetzung** - Windows-Pfade wie `C:\Users\IhrName\Documents` werden zu `/mnt/c/Users/IhrName/Documents` in WSL
- **Hybrid-Workflow** - RStudio (Windows) führt Code aus; Claude Code (WSL) schreibt und verbessert ihn

## Was Sie benötigen

- Abgeschlossene Anleitung [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win)
- RStudio unter Windows installiert
- 20-30 Minuten

## Schritt 1: RStudio unter Windows öffnen

- Klicken Sie auf die **Windows-Starttaste**
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
- Klicken Sie auf **Ordner auswählen**
- Klicken Sie auf **Create Project**
- RStudio erstellt das Projekt und wechselt dorthin

## Schritt 3: Ein neues R-Skript erstellen

- Klicken Sie in RStudio auf **File > New File > R Script**
- Ein neues leeres Skript öffnet sich im oberen linken Bereich
- Klicken Sie auf **File > Save** (oder das Speichern-Symbol)
- Nennen Sie die Datei: `iris.R`
- Klicken Sie auf **Save**

## Schritt 4: Ersten Code manuell schreiben

Geben Sie diesen Code in Ihre `iris.R`-Datei ein:

```r
data(iris)
str(iris)
summary(iris)
```

- Klicken Sie auf **File > Save**, um Ihre Änderungen zu speichern
- Um den Code auszuführen: Markieren Sie alle Zeilen und klicken Sie auf die **Run**-Schaltfläche (oben rechts im Skriptbereich)
- Sie sollten die Ausgabe im Console-Bereich sehen, die Datensatzstruktur und Statistiken zeigt

## Schritt 5: Ubuntu-Terminal öffnen

- Klicken Sie auf die **Windows-Starttaste**
- Geben Sie `Ubuntu` in das Suchfeld ein
- Klicken Sie auf **Ubuntu** (orangefarbenes kreisförmiges Symbol)
- Das Ubuntu-Terminal öffnet sich

## Schritt 6: Zu Ihrem Projektordner navigieren

- Geben Sie im Ubuntu-Terminal diesen Befehl ein (ersetzen Sie `IhrBenutzername` durch Ihren tatsächlichen Windows-Benutzernamen):
  ```
  cd /mnt/c/Users/IhrBenutzername/Documents/test_claude
  ```
- Um Ihren Benutzernamen zu finden, können Sie eingeben: `ls /mnt/c/Users/` und nach Ihrem Ordnernamen suchen
- Überprüfen Sie, ob Sie am richtigen Ort sind, indem Sie eingeben:
  ```
  ls
  ```
- Sie sollten `iris.R` und `test_claude.Rproj` aufgelistet sehen

## Schritt 7: Claude Code starten

- Geben Sie im Ubuntu-Terminal ein:
  ```
  claude
  ```
- Claude Code startet und zeigt eine Willkommensnachricht
- Möglicherweise müssen Sie sich erneut anmelden – siehe die Anleitung [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win) für Authentifizierungsschritte
- Sie sind nun bereit, KI-Unterstützung für Ihr R-Projekt zu nutzen

## Schritt 8: Claude um ein Streudiagramm bitten

Wenn Claude Code langsam ist oder nicht reagiert, warten Sie einfach, bis es initialisiert ist. Dann geben Sie diese Anfrage ein:

```
Füge Code zu iris.R hinzu, um ein Streudiagramm der Kelchblattlänge vs. -breite zu erstellen, gefärbt nach Art. Verwende ggplot2.
```
- Claude Code liest Ihre `iris.R`-Datei und fügt den Visualisierungscode hinzu
- Wenn Sie gefragt werden, geben Sie Claude die Erlaubnis, die iris.R-Datei zu bearbeiten, indem Sie die entsprechende Option wählen
- Warten Sie, bis Claude fertig ist (Sie sehen eine Bestätigungsnachricht)


## Schritt 9: Den neuen Code in RStudio ausführen

- Wechseln Sie zurück zu RStudio (klicken Sie auf das RStudio-Fenster)
- Möglicherweise sehen Sie eine Aufforderung, dass die Datei geändert wurde – klicken Sie auf **Ja**, um sie neu zu laden
- Wenn keine Aufforderung erscheint, klicken Sie auf **File > Reopen with Encoding > UTF-8**
- Markieren Sie den gesamten Code und klicken Sie auf **Run**
- Ein Streudiagramm erscheint im **Plots**-Bereich (unten rechts)
- Wenn Sie einen Fehler zu ggplot2 erhalten, installieren Sie es durch Eingabe von `install.packages("ggplot2")` im Console-Bereich

## Schritt 10: Das Streudiagramm verfeinern

- Wechseln Sie zum Ubuntu-Terminal
- Geben Sie diese Anfrage ein:
  ```
  Entferne den Titel. Ändere den Markierungstyp nach Art. Wechsle zum klassischen Theme.
  ```

## Schritt 11: Das verfeinerte Diagramm ansehen

- Wechseln Sie zu RStudio
- Laden Sie die Datei neu, wenn Sie dazu aufgefordert werden
- Markieren Sie den aktualisierten Code und klicken Sie auf **Run**
- Das Diagramm sollte jetzt ohne Titel angezeigt werden, mit verschiedenen Markierungsformen für jede Art und mit dem klassischen Theme


## Schritt 12: Claude um PCA-Plot bitten

- Wechseln Sie zum Ubuntu-Terminal
- Geben Sie diese Anfrage ein:
  ```
  Füge Code hinzu, um eine PCA auf den numerischen Variablen durchzuführen und die Proben unter Verwendung der ersten beiden Hauptkomponenten zu plotten.
  ```

## Schritt 13: Die PCA-Analyse ausführen

- Wechseln Sie zu RStudio
- Laden Sie die Datei neu, wenn Sie dazu aufgefordert werden
- Markieren Sie den gesamten Code und klicken Sie auf **Run**
- Ein PCA-Plot erscheint, der Proben auf PC1 und PC2 projiziert zeigt, gefärbt nach Art

## Schritt 14: Claude um Überprüfung und Kommentare bitten

- Wechseln Sie zum Ubuntu-Terminal
- Geben Sie diese Anfrage ein:
  ```
  Überprüfe das gesamte Skript auf Korrektheit. Füge bei Bedarf Kommentare hinzu.
  ```
- Claude überprüft den Code und fügt umfassende Kommentare hinzu

## Schritt 15: Claude bitten, R Markdown zu erstellen

- Wechseln Sie zum Ubuntu-Terminal
- Geben Sie diese Anfrage ein:
  ```
  Erstelle eine neue R-Markdown-Datei für diese Analyse. Speichere sie als iris_report.Rmd
  ```
- Claude wird Sie um Erlaubnis bitten, diese Datei zu erstellen.
- Claude erstellt eine neue `.Rmd`-Datei in Ihrem Projektordner


## Schritt 16: Die R-Markdown-Datei knitten

- Wechseln Sie zu RStudio
- Klicken Sie auf **File > Open File...**
- Wählen Sie `iris_report.Rmd` und klicken Sie auf **Open**
- Klicken Sie auf die **Knit**-Schaltfläche (mit einem Wollknäuel-Symbol) oben im Skriptbereich
- RStudio generiert einen HTML-Bericht
- Der Bericht öffnet sich in einem neuen Fenster und zeigt Ihre vollständige Analyse mit erzählendem Text
- Die HTML-Datei wird in Ihrem Projektordner gespeichert

## Fehlerbehebung

- **„Permission denied" beim Zugriff auf Windows-Dateien von WSL** - Stellen Sie sicher, dass Sie `/mnt/c/` und nicht `C:/` verwenden. Überprüfen Sie, ob Ihr Benutzername im Pfad korrekt ist.
- **RStudio zeigt Dateiänderungen nicht an** - Klicken Sie auf **File > Reopen with Encoding > UTF-8**, um die Datei manuell neu zu laden.
- **„claude: command not found"** - Stellen Sie sicher, dass Sie die Installationsanleitung abgeschlossen haben. Versuchen Sie, ein neues Ubuntu-Terminal-Fenster zu öffnen.
- **Plots erscheinen nicht** - Stellen Sie sicher, dass ggplot2 installiert ist. Führen Sie `install.packages("ggplot2")` in der RStudio-Konsole aus, wenn nötig.
- **Fehler: „cannot change working directory"** - Ihr Windows-Pfad enthält Leerzeichen. In Schritt 6, setzen Sie den Pfad in Anführungszeichen: `cd "/mnt/c/Users/Ihr Name/Documents/test_claude"`
- **Claude Code ist bei der ersten Anfrage langsam** - Warten Sie 30-60 Sekunden, bis Claude initialisiert ist. Nachfolgende Anfragen werden schneller sein.

## Nächste Schritte

- Versuchen Sie, Claude zu bitten, statistische Tests (t-Tests, ANOVA) zu Ihrer Analyse hinzuzufügen
- Bitten Sie Claude, eine **Python-Version** dieses Codes zu erstellen und ein Quarto-Dokument vorzubereiten
- Bitten Sie Claude, Funktionen für sich wiederholende Aufgaben in Ihren R-Skripten zu erstellen
- Verwenden Sie Claude, um Fehlermeldungen zu debuggen, wenn Ihr R-Code nicht läuft
- Erkunden Sie, wie Sie Claude bitten können, langsamen R-Code für bessere Leistung zu optimieren

## Workflow-Zusammenfassung

Diese Hybrid-Einrichtung kombiniert das Beste aus beiden Welten:

- **RStudio (Windows)** - Interaktive R-Konsole, sofortige Plot-Anzeige, vertraute GUI zum Ausführen von Code
- **Claude Code (WSL)** - KI-gestützte Codegenerierung, Überprüfung und Verbesserung
- **Geteilte Dateien** - Beide Tools arbeiten an denselben Dateien über WSLs `/mnt/c/`-Einhängepunkt
- **Iterative Verfeinerung** - Beginnen Sie mit manuellem Code, verbessern Sie mit Claude, testen Sie in RStudio, dann verfeinern Sie weiter
- **Dokumentation** - Claude kann umfassende Berichte und Kommentare für Ihre Analyse generieren

Der Workflow ist einfach: Schreiben oder bearbeiten Sie Code mit Claude im Ubuntu-Terminal, dann testen und führen Sie ihn sofort in RStudio aus. Kein Dateikopieren oder manuelles Synchronisieren nötig – WSL und Windows teilen dieselben Dateien nahtlos.

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2025.
