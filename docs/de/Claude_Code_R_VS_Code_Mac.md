[Startseite](./)

# Claude Code für R in VS Code auf dem Mac verwenden

Sie haben R in VS Code eingerichtet und können Code manuell schreiben. Jetzt möchten Sie, dass KI Ihnen hilft, Ihren R-Code zu schreiben, zu verbessern und zu debuggen, während Sie sich auf die Analyse konzentrieren. Stellen Sie sich Claude Code als Programmierpartner vor, der in VS Code lebt – Sie beschreiben, was Sie möchten, und er schreibt oder verbessert den Code, während Sie im selben Fenster bleiben.

## Wichtige Konzepte

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - VS Code-Erweiterung, die den Claude KI-Assistenten direkt in Ihren Editor bringt, mit Inline-Code-Bearbeitungen
- **Chat-Panel** - Seitenpanel in VS Code, in dem Sie mit Claude über Ihren Code kommunizieren
- **Inline-Bearbeitungen** - Claudes vorgeschlagene Codeänderungen erscheinen direkt in Ihren Dateien mit Diffs, die Sie akzeptieren oder ablehnen können

## Was Sie benötigen

- Abgeschlossenes Tutorial [R in VS Code](./R_Coding_VS_Code_Guide) - R sollte in VS Code funktionieren
- Abgeschlossenes Tutorial [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS) - Claude Code CLI sollte installiert sein
- Claude Pro/Max-Abonnement oder Anthropic-API-Schlüssel
- 20-30 Minuten

## Schritt 1: VS Code öffnen und R-Projekt erstellen

- Öffnen Sie **Visual Studio Code**
- Klicken Sie in der Menüleiste auf **File**, dann auf **Open Folder**
- Navigieren Sie zu Ihrem **Dokumente**-Ordner
- Klicken Sie unten im Dialog auf **New Folder**
- Nennen Sie den Ordner `claude_r_test`
- Klicken Sie auf **Open**, um den neuen Ordner zu öffnen
- Wenn Sie gefragt werden „Vertrauen Sie den Autoren?", klicken Sie auf **Ja, ich vertraue den Autoren**

## Schritt 2: Claude Code Extension installieren und anmelden

- Klicken Sie auf das **Extensions**-Symbol in der linken Seitenleiste (Symbol mit vier Quadraten)
- Geben Sie im Suchfeld `Claude Code` ein
- Finden Sie **Claude Code** von Anthropic und klicken Sie auf **Install**
- Nach der Installation erscheint ein Claude-Symbol (Funkeln) in der linken Seitenleiste
- Klicken Sie auf das Claude-Symbol, um das Chat-Panel zu öffnen
- Klicken Sie auf **Sign in to Claude Code** im Chat-Panel
- Wählen Sie Ihre Authentifizierungsmethode:
  - **Claude Pro/Max-Benutzer**: Klicken Sie auf **Sign in with Claude.ai**, autorisieren Sie im Browser und kopieren Sie den Code zurück nach VS Code
  - **API-Schlüssel-Benutzer**: Klicken Sie auf **Use API Key** und fügen Sie Ihren Anthropic-API-Schlüssel ein
- Für detaillierte Authentifizierungsschritte siehe die Anleitung [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS) (Schritt 5)
- Nach der Anmeldung sehen Sie „Ready to help" im Chat-Panel

## Schritt 3: Erstes R-Skript manuell erstellen

- Klicken Sie in der Menüleiste auf **File > New File**
- Klicken Sie auf **Select a language** und geben Sie `R` ein, dann wählen Sie **R**
- Speichern Sie die Datei durch Klicken auf **File > Save**, nennen Sie sie `iris_analysis.R`
- Geben Sie diesen Code ein:

```r
data(iris)
str(iris)
summary(iris)
```

- Speichern Sie die Datei durch Klicken auf **File > Save**
- Öffnen Sie das R-Terminal: Klicken Sie in der Menüleiste auf **View**, dann auf **Command Palette**, geben Sie `R: Create R Terminal` ein und drücken Sie Enter
- Wählen Sie den Code aus und drücken Sie `Strg+Enter` (Windows/Linux) oder `Cmd+Enter` (Mac), um ihn auszuführen
- Sie sollten die Datensatzstruktur und zusammenfassende Statistiken im Terminal sehen

## Schritt 4: Claude bitten, ein Streudiagramm hinzuzufügen

- Klicken Sie auf das **Claude**-Symbol in der linken Seitenleiste, um das Chat-Panel zu öffnen
- Geben Sie im Chat-Feld unten ein:

```
Füge Code zu iris_analysis.R hinzu, um ein Streudiagramm von Kelchblattlänge vs. -breite zu erstellen, gefärbt nach Art. Verwende ggplot2.
```

- Drücken Sie Enter zum Senden
- Claude liest Ihre Datei und schlägt Änderungen vor – Sie sehen ein Diff mit neuem Code zum Hinzufügen
- Klicken Sie auf **Accept**, um die Änderungen zu übernehmen
- Der ggplot2-Code erscheint in Ihrer Datei
- Wenn Sie ggplot2 nicht installiert haben, führen Sie `install.packages("ggplot2")` im R-Terminal aus

## Schritt 5: Den aktualisierten Code ausführen

- Wählen Sie den gesamten Code in `iris_analysis.R` aus
- Drücken Sie `Strg+Enter` (Windows/Linux) oder `Cmd+Enter` (Mac)
- Ein Streudiagramm erscheint in einem separaten Grafikfenster
- Sie sollten Punkte sehen, die nach Art gefärbt sind (setosa, versicolor, virginica)

## Schritt 6: Claude bitten, das Diagramm zu verfeinern

- Geben Sie im Claude-Chat-Panel ein:

```
Entferne den Titel. Ändere den Markertyp nach Art. Wechsle zum klassischen Theme.
```

- Drücken Sie Enter
- Claude zeigt die aktualisierten Codeänderungen
- Klicken Sie auf **Accept**
- Führen Sie den aktualisierten Code erneut aus: Wählen Sie alles aus und drücken Sie `Strg+Enter` / `Cmd+Enter`
- Das Diagramm zeigt jetzt verschiedene Markierungsformen pro Art, keinen Titel und das klassische Theme

## Schritt 7: Claude um PCA-Analyse bitten

- Geben Sie im Claude-Chat-Panel ein:

```
Füge Code hinzu, um eine PCA auf den numerischen Variablen durchzuführen und die Proben mit den ersten beiden Hauptkomponenten darzustellen.
```

- Drücken Sie Enter
- Claude fügt PCA-Code zu Ihrem Skript hinzu
- Klicken Sie auf **Accept**
- Führen Sie den gesamten Code aus: Wählen Sie alles aus und drücken Sie `Strg+Enter` / `Cmd+Enter`
- Ein PCA-Plot erscheint, der Proben auf PC1 und PC2 projiziert zeigt, gefärbt nach Art

## Schritt 8: Claude um Überprüfung und Kommentare bitten

- Geben Sie im Claude-Chat-Panel ein:

```
Überprüfe das gesamte Skript auf Korrektheit. Füge bei Bedarf Kommentare hinzu.
```

- Drücken Sie Enter
- Claude überprüft den Code und schlägt Kommentare vor, die jeden Abschnitt erklären
- Klicken Sie auf **Accept**
- Ihr Skript hat jetzt klare Kommentare, die das Laden der Daten, die Visualisierung und die PCA-Analyse erklären

## Nächste Schritte

- Bitten Sie Claude, einen R-Markdown-Bericht zu erstellen: „Erstelle eine R-Markdown-Datei für diese Analyse"
- Verwenden Sie Claude, um Fehler zu debuggen: „Dieser Code gibt Fehler X, kannst du ihn beheben?"
- Fordern Sie statistische Tests an: „Füge einen t-Test hinzu, der die Kelchblattlänge zwischen setosa und versicolor vergleicht"
- Bitten Sie Claude, Code zu optimieren: „Mache diese Schleife schneller durch Vektorisierung"
- Holen Sie Hilfe bei unbekannten Funktionen: „Erkläre, was dplyr::mutate macht"

## Fehlerbehebung

- **Claude-Erweiterung wird nicht angezeigt** - Starten Sie VS Code nach der Installation neu. Klicken Sie auf **View > Extensions**, um zu überprüfen, ob sie installiert ist.
- **„Cannot read R file"-Fehler** - Stellen Sie sicher, dass Sie die Datei mit der Erweiterung `.R` gespeichert haben. Claude benötigt gespeicherte Dateien, um sie zu lesen.
- **Authentifizierung fehlgeschlagen** - Überprüfen Sie, ob Ihr Claude Pro/Max-Abonnement aktiv ist oder Ihr API-Schlüssel gültig ist. Siehe [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS) für Fehlerbehebung bei der Authentifizierung.
- **ggplot2 nicht gefunden** - Installieren Sie es im R-Terminal: `install.packages("ggplot2")`. Warten Sie, bis die Installation abgeschlossen ist, bevor Sie den Code ausführen.
- **Codeänderungen werden nicht übernommen** - Stellen Sie sicher, dass Sie auf **Accept** beim Diff klicken. Wenn es nicht funktioniert, versuchen Sie, Claudes vorgeschlagenen Code manuell zu kopieren.

## Workflow-Zusammenfassung

- **Claude Code Extension** bietet einen KI-Assistenten direkt in VS Code mit Chat-Panel und Inline-Diffs
- **Iterative Verfeinerung** - Beginnen Sie mit einfachem Code, bitten Sie Claude um Verbesserungen, testen Sie sofort, dann verfeinern Sie weiter
- **Kontextbewusstsein** - Claude liest Ihre R-Dateien und versteht Ihre Projektstruktur
- **Inline-Bearbeitung** - Vorgeschlagene Änderungen erscheinen als Diffs in Ihren tatsächlichen Dateien, nicht als separate Chat-Antworten
- **Im Flow bleiben** - Kein Wechseln zwischen Browser und Editor – alles passiert in VS Code

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2025.
