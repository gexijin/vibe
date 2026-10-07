---
title: "VS Code für Claude Code unter Windows einrichten"
lang: "de"
---
[Startseite](./)

# VS Code für Claude Code unter Windows einrichten

Sie haben Claude Code auf Ihrem Windows-Rechner installiert – jetzt möchten Sie einen visuellen Editor, um mit Ihrem Code zu arbeiten. Mit VS Code können Sie Dateien visuell bearbeiten und gleichzeitig Claude Code im integrierten Terminal ausführen – direkt nebeneinander im selben Fenster.

## Wichtige Konzepte

- **VS Code** - Ein kostenloser Code-Editor von Microsoft mit einem eingebauten Terminal
- **Integriertes Terminal** - Ein PowerShell-Terminal-Panel innerhalb von VS Code, sodass Sie zum Ausführen von Claude Code nicht das Fenster wechseln müssen
- **Arbeitsordner** - Der Ordner, den Sie in VS Code öffnen; Claude Code liest und bearbeitet die Dateien darin

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win)
- Abgeschlossenes Tutorial [VS Code Grundlagen](./VS_Code_Getting_Started)
- 10-15 Minuten

## Schritt 1: Einen Projektordner erstellen

- Öffnen Sie den **Datei-Explorer** (klicken Sie auf das Ordner-Symbol in Ihrer Taskleiste)
- Navigieren Sie zu **Dokumente**
- Klicken Sie mit der rechten Maustaste in den leeren Bereich, wählen Sie **Neu > Ordner**
- Nennen Sie den Ordner `test_claude`

## Schritt 2: VS Code starten

- Klicken Sie auf die **Windows-Starttaste** (unten links auf Ihrem Bildschirm)
- Geben Sie `Visual Studio Code` oder `VS Code` in das Suchfeld ein
- Klicken Sie auf **Visual Studio Code**, wenn es in den Suchergebnissen erscheint
- VS Code öffnet sich mit einem Willkommen-Tab – Sie können diesen Tab schließen


## Schritt 3: Den Ordner in VS Code öffnen

- Klicken Sie in VS Code in der Menüleiste auf **File**, dann auf **Open Folder**
- Navigieren Sie zu **Dokumente** und wählen Sie den Ordner `test_claude` aus
- Klicken Sie auf **Select Folder**. VS Code lädt mit Ihrem `test_claude`-Ordner neu
- Wenn Sie gefragt werden „Vertrauen Sie den Autoren?", klicken Sie auf **Ja, ich vertraue den Autoren**


## Schritt 4: Claude Code starten

- Nachdem VS Code neu geladen hat, öffnen Sie ein neues Terminal: Klicken Sie in der Menüleiste auf **Terminal**, dann auf **Neues Terminal**
- Geben Sie im Terminal-Panel ein:
  ```
  claude
  ```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im [Installations-Tutorial](Install_CLAUDE_Code_Win.md) beschrieben. Nach der Anmeldung sehen Sie eine Willkommensnachricht und die Claude Code-Eingabeaufforderung.

## Schritt 5: Den Workflow testen

- Geben Sie in Claude Code ein:
```
Schreibe einen kurzen Artikel, der erklärt, warum LLMs gerne das Markdown-Format verwenden. Speichere ihn als article.md
```
- Claude Code erstellt die Datei – Sie sehen `article.md` im Explorer-Panel auf der linken Seite erscheinen
- Klicken Sie auf `article.md` im Explorer, um sie im Editor anzuzeigen
- Um den formatierten Artikel in der Vorschau anzuzeigen: Klicken Sie mit der rechten Maustaste auf den Tab `article.md` und wählen Sie **Vorschau öffnen**
- Sie sehen das Markdown mit korrekten Überschriften, Aufzählungspunkten und Formatierung gerendert

## Claude später in VS Code wieder öffnen

Nachdem Sie VS Code geschlossen haben, so kommen Sie zurück zu Ihrem Projekt:

- **Option A:** Öffnen Sie VS Code, klicken Sie auf **File > Open Recent** und wählen Sie `test_claude`
- **Option B:** Öffnen Sie den **Datei-Explorer**, klicken Sie mit der rechten Maustaste auf den Ordner `test_claude` und wählen Sie **Open with Code**

## Nächste Schritte

- Bitten Sie Claude Code, eine bestehende Codebasis zu erklären: „Erkläre, was dieses Projekt macht"
- Lassen Sie Claude Code Ihnen beim Schreiben neuer Funktionen helfen: „Füge eine Funktion hinzu, die den Durchschnitt einer Liste berechnet"
- Verwenden Sie Claude Code, um Fehler zu beheben: „Dieser Code gibt einen Fehler aus, kannst du ihn beheben?"
- Probieren Sie die Claude Code VS Code-Erweiterung für eine visuelle Oberfläche mit Inline-Diffs aus (suchen Sie nach „Claude Code" in Extensions)

## Fehlerbehebung

- **Befehl `claude` nicht gefunden** - Führen Sie `claude --version` im VS Code-Terminal aus, um zu prüfen, ob Claude Code installiert ist; wenn nicht, folgen Sie zuerst dem [Installations-Tutorial](Install_CLAUDE_Code_Win.md)
- **Sie verwenden stattdessen WSL?** - Wenn Sie den optionalen WSL/Ubuntu-Weg eingerichtet haben, installieren Sie die Erweiterung **WSL** über die Extensions-Seitenleiste, klicken Sie auf das blaue/grüne Symbol in der unteren linken Ecke und wählen Sie **Connect to WSL**, bevor Sie Ihren Projektordner öffnen (erreichbar unter `/mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude`)

## Workflow-Überblick

- **VS Code** läuft unter Windows und bietet die visuelle Editor-Oberfläche
- **Integriertes Terminal** führt Claude Code direkt in VS Code aus
- Bearbeiten Sie Dateien im Editor, chatten Sie mit Claude Code im Terminal – das Beste aus beiden Welten

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 10. Dezember 2025.
