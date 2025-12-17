[Startseite](./)

# Claude Code aus VS Code auf dem Mac verwenden

Sie haben Claude Code auf Ihrem Mac installiert – jetzt möchten Sie einen visuellen Editor, um mit Ihrem Code zu arbeiten. VS Code ermöglicht es Ihnen, Dateien visuell zu bearbeiten, während Sie Claude Code im integrierten Terminal ausführen. Stellen Sie es sich vor, als hätten Sie Ihren Code-Editor und KI-Assistenten Seite an Seite in einem Fenster.

## Wichtige Konzepte

- **VS Code** - Ein kostenloser Code-Editor von Microsoft, der auf dem Mac läuft
- **Integriertes Terminal** - Ein Terminal-Panel innerhalb von VS Code, in dem Sie Claude Code ausführen
- **Explorer-Panel** - Der Dateibrowser auf der linken Seite von VS Code

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS)
- Abgeschlossenes Tutorial [VS Code Grundlagen](./VS_Code_Getting_Started)
- 10-15 Minuten

## Schritt 1: VS Code starten

- Öffnen Sie den **Finder** und gehen Sie zu **Programme**
- Finden Sie **Visual Studio Code** und doppelklicken Sie darauf
- Wenn Sie eine Warnung sehen „Visual Studio Code ist eine aus dem Internet heruntergeladene App", klicken Sie auf **Öffnen**
- VS Code öffnet sich mit einem Willkommen-Tab – Sie können diesen Tab schließen

**Tipp:** Klicken Sie mit der rechten Maustaste auf VS Code im Dock und wählen Sie **Optionen > Im Dock behalten** für späteren schnellen Zugriff.

## Schritt 2: Einen Projektordner erstellen

- Öffnen Sie den **Finder**
- Klicken Sie in der linken Seitenleiste auf **Dokumente**
- Klicken Sie in der Menüleiste auf **File**, dann auf **New Folder**
- Nennen Sie den Ordner `test_claude`

## Schritt 3: Den Ordner in VS Code öffnen

- Klicken Sie in VS Code in der Menüleiste auf **File**, dann auf **Open Folder**
- Navigieren Sie zu **Dokumente** und wählen Sie den Ordner `test_claude`, den Sie erstellt haben
- Klicken Sie auf **Öffnen**
- Wenn Sie gefragt werden „Vertrauen Sie den Autoren der Dateien in diesem Ordner?", klicken Sie auf **Ja, ich vertraue den Autoren**

Sie sollten nun `TEST_CLAUDE` im Explorer-Panel auf der linken Seite sehen.

## Schritt 4: Claude Code starten

- Öffnen Sie ein neues Terminal: Klicken Sie in der Menüleiste auf **Terminal**, dann auf **New Terminal**
- Ein Terminal-Panel erscheint am unteren Rand von VS Code
- Geben Sie im Terminal ein:
  ```
  claude
  ```
- Claude Code startet – Sie sehen die vertraute Claude Code-Oberfläche
- Sie sind nun bereit, Claude Code zu verwenden, während Sie Dateien in VS Code bearbeiten

## Schritt 5: Den Workflow testen

- Geben Sie in Claude Code ein:
```
Schreibe einen kurzen Artikel, der erklärt, warum LLMs gerne das Markdown-Format verwenden. Speichere ihn als article.md
```
- Claude Code erstellt die Datei – Sie sehen `article.md` im Explorer-Panel auf der linken Seite erscheinen
- Klicken Sie auf `article.md` im Explorer, um sie im Editor anzuzeigen
- Um den formatierten Artikel in der Vorschau anzuzeigen: Klicken Sie mit der rechten Maustaste auf den Tab `article.md` und wählen Sie **Open Preview**
- Sie sehen das Markdown mit korrekten Überschriften, Aufzählungspunkten und Formatierung gerendert

## Claude später in VS Code wieder öffnen

Nachdem Sie VS Code geschlossen haben, so kommen Sie zurück zu Ihrem Projekt:

- **Option A:** Öffnen Sie VS Code, klicken Sie auf **File > Open Recent** und wählen Sie `test_claude`
- **Option B:** Öffnen Sie Terminal, navigieren Sie mit `cd ~/Documents/test_claude` zu Ihrem Projekt und geben Sie `code .` ein

VS Code merkt sich Ihre letzten Ordner, daher ist Option A mit Open Recent normalerweise am schnellsten.

## Nächste Schritte

- Bitten Sie Claude Code, eine bestehende Codebasis zu erklären: „Erkläre, was dieses Projekt macht"
- Lassen Sie Claude Code Ihnen beim Schreiben neuer Funktionen helfen: „Füge eine Funktion hinzu, die den Durchschnitt einer Liste berechnet"
- Verwenden Sie Claude Code, um Fehler zu beheben: „Dieser Code gibt einen Fehler, kannst du ihn beheben?"
- Probieren Sie die Claude Code VS Code-Erweiterung für eine visuelle Oberfläche mit Inline-Diffs aus (suchen Sie nach „Claude Code" in Extensions)

## Fehlerbehebung

- **Terminal zeigt „zsh", aber Claude Code startet nicht** - Stellen Sie sicher, dass Claude Code korrekt installiert ist; führen Sie `claude --version` aus, um es zu überprüfen
- **Befehl „code" wird im Terminal nicht gefunden** - Klicken Sie in VS Code in der Menüleiste auf **View**, dann auf **Command Palette**, geben Sie „shell command" ein und wählen Sie **Shell Command: Install 'code' command in PATH**
- **VS Code öffnet sich nicht, weil es von einem nicht identifizierten Entwickler stammt** - Gehen Sie zu **Systemeinstellungen > Datenschutz & Sicherheit** und klicken Sie auf **Trotzdem öffnen**

## Workflow-Überblick

- **VS Code** bietet die visuelle Editor-Oberfläche
- **Integriertes Terminal** führt Claude Code innerhalb von VS Code aus
- Ihre Dateien bleiben in Ihrem Dokumente-Ordner (oder wo auch immer Sie wählen)
- Bearbeiten Sie Dateien im Editor, chatten Sie mit Claude Code im Terminal – das Beste aus beiden Welten

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 10. Dezember 2025.
