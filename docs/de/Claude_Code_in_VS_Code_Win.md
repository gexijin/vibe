[Startseite](./)

# VS Code für Claude Code unter WSL einrichten

Sie haben WSL und Claude Code auf Ihrem Windows-Rechner installiert – jetzt möchten Sie einen visuellen Editor, um mit Ihrem Code zu arbeiten. VS Code überbrückt die Lücke zwischen Windows und Ihrer Linux-Umgebung und ermöglicht es Ihnen, Dateien visuell zu bearbeiten, während Sie Claude Code im integrierten Terminal ausführen. Betrachten Sie VS Code als ein Fenster in Ihre Linux-Welt.

## Wichtige Konzepte

- **VS Code** - Ein kostenloser Code-Editor von Microsoft, der unter Windows läuft, aber eine Verbindung zu WSL herstellen kann
- **WSL-Erweiterung** - Verbindet VS Code mit Ihrer Linux-Umgebung, sodass Sie Linux-Tools wie Claude Code ausführen können
- **Integriertes Terminal** - Ein Terminal-Panel innerhalb von VS Code, das in Ihrer WSL (Linux)-Umgebung läuft
- **/mnt/c/** - So greift WSL auf Ihre Windows-Dateien zu (z.B. `/mnt/c/Users/...` = `C:\Users\...`)

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


## Schritt 3: Die WSL-Erweiterung installieren

- Klicken Sie in VS Code auf das **Extensions**-Symbol in der linken Seitenleiste (es sieht aus wie vier Quadrate)
- Geben Sie `WSL` in das Suchfeld ein
- Finden Sie **WSL** von Microsoft (es sollte das erste Ergebnis sein)
- Klicken Sie auf die blaue Schaltfläche **Install**
- Warten Sie, bis die Installation abgeschlossen ist (ein paar Sekunden)

## Schritt 4: VS Code mit WSL verbinden

- Schauen Sie in die untere linke Ecke von VS Code – Sie sehen ein blaues oder grünes Symbol
- Klicken Sie auf dieses Symbol, um das Remote-Verbindungsmenü zu öffnen
- Wählen Sie **Connect to WSL** aus dem Menü
- VS Code wird neu geladen und verbindet sich mit Ihrer Ubuntu-Installation
- Die untere linke Ecke sollte jetzt **WSL: Ubuntu** anzeigen

Beim ersten Verbinden installiert VS Code einen kleinen Server in WSL. Dies dauert etwa 30 Sekunden.

## Schritt 5: Den Ordner in VS Code öffnen

- Klicken Sie in VS Code (noch mit WSL verbunden) in der Menüleiste auf **Datei**, dann auf **Ordner öffnen**
- Ein **Ordner öffnen**-Dropdown erscheint oben in der Mitte.
- Finden Sie Ihren Ordner durch Eingabe von:
  ```
  /mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude
  ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren Windows-Benutzernamen (z.B. `Max.Mustermann`)
- Klicken Sie auf **OK**. VS Code lädt mit Ihrem `test_claude`-Ordner neu
- Wenn Sie gefragt werden „Vertrauen Sie den Autoren?", klicken Sie auf **Ja, ich vertraue den Autoren**


## Schritt 6: Claude Code starten

- Nachdem VS Code neu geladen hat, öffnen Sie ein neues Terminal: Klicken Sie in der Menüleiste auf **Terminal**, dann auf **Neues Terminal**
- Geben Sie im Terminal-Panel ein:
  ```
  claude
  ```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im [Installations-Tutorial](Install_CLAUDE_Code_Win.md) beschrieben. Nach der Anmeldung sehen Sie eine Willkommensnachricht und die Claude Code-Eingabeaufforderung.

## Schritt 7: Den Workflow testen

- Geben Sie in Claude Code ein:
```
Schreibe einen kurzen Artikel, der erklärt, warum LLMs gerne das Markdown-Format verwenden. Speichere ihn als article.md
```
- Claude Code erstellt die Datei – Sie sehen `article.md` im Explorer-Panel auf der linken Seite erscheinen
- Klicken Sie auf `article.md` im Explorer, um sie im Editor anzuzeigen
- Um den formatierten Artikel in der Vorschau anzuzeigen: Klicken Sie mit der rechten Maustaste auf den Tab `article.md` und wählen Sie **Vorschau öffnen**
- Sie sehen das Markdown mit korrekten Überschriften, Aufzählungspunkten und Formatierung gerendert

## Claude später in VS Code wieder öffnen

Nachdem Sie VS Code geschlossen haben, so kommen Sie zurück zu Ihren WSL-Projekten:

- **Option A:** Öffnen Sie VS Code, klicken Sie auf die untere linke Ecke, wählen Sie **Mit WSL verbinden**, dann **Datei > Zuletzt geöffnet**. Wählen Sie `/mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude [WSL: Ubuntu]`
- **Option B:** Öffnen Sie die Ubuntu-App von Windows, navigieren Sie im Terminal zu Ihrem Projekt und geben Sie `code .` ein

VS Code merkt sich Ihre letzten Ordner, daher ist Option A mit Zuletzt geöffnet normalerweise am schnellsten.

## Nächste Schritte

- Bitten Sie Claude Code, eine bestehende Codebasis zu erklären: „Erkläre, was dieses Projekt macht"
- Lassen Sie Claude Code Ihnen beim Schreiben neuer Funktionen helfen: „Füge eine Funktion hinzu, die den Durchschnitt einer Liste berechnet"
- Verwenden Sie Claude Code, um Fehler zu beheben: „Dieser Code gibt einen Fehler aus, kannst du ihn beheben?"
- Probieren Sie die Claude Code VS Code-Erweiterung für eine visuelle Oberfläche mit Inline-Diffs aus (suchen Sie nach „Claude Code" in Extensions)
- Um größere Dateien effizienter zu handhaben, erstellen Sie einen Ordner im WSL-Dateisystem (`/home/user/`). Von Windows aus suchen Sie nach dem Linux-Symbol unten in der Seitenleiste im Datei-Explorer. Oder geben Sie `\\wsl.localhost\` in die Adressleiste ein.

## Fehlerbehebung

- **„WSL: Ubuntu" wird nicht in der unteren linken Ecke angezeigt** - Stellen Sie sicher, dass WSL korrekt installiert ist; versuchen Sie zuerst, das Ubuntu-Terminal zu öffnen, um zu überprüfen, ob es funktioniert
- **Terminal zeigt PowerShell statt Linux** - Klicken Sie auf den Dropdown-Pfeil neben dem **+** im Terminal-Panel und wählen Sie **Ubuntu (WSL)**
- **Befehl `claude` nicht gefunden** - Führen Sie `claude --version` aus, um zu prüfen, ob Claude Code installiert ist; wenn nicht, folgen Sie zuerst dem WSL-Installations-Tutorial

## Workflow-Überblick

- **VS Code** läuft unter Windows und bietet die visuelle Editor-Oberfläche
- **WSL-Erweiterung** verbindet VS Code mit Ubuntu, sodass Sie Linux-Tools ausführen können
- **Integriertes Terminal** führt Claude Code innerhalb von WSL aus
- Ihre Dateien bleiben in Windows (Dokumente-Ordner) – WSL greift über `/mnt/c/` darauf zu
- Bearbeiten Sie Dateien im Editor, chatten Sie mit Claude Code im Terminal – das Beste aus beiden Welten

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 10. Dezember 2025.
