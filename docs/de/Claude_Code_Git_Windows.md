---
title: "Claude Code mit lokaler Versionskontrolle für Windows"
lang: "de"
---
[Startseite](./)

# Claude Code mit lokaler Versionskontrolle für Windows

Sie arbeiten mit KI-Unterstützung. Die KI nimmt Änderungen an Ihren Dateien vor. Manchmal sind die Änderungen brillant. Manchmal nicht. **Versionskontrolle ist wie eine Rückgängig-Taste für Ihr gesamtes Projekt.** Jedes Mal, wenn Sie einen Snapshot speichern (genannt „Commit“), erstellen Sie einen Wiederherstellungspunkt, zu dem Sie immer zurückkehren können. Das Beste daran: Sie können dies komplett auf Ihrem Computer machen und Claude Code erledigt es für Sie.

## Wichtige Konzepte

- **PowerShell** - Das integrierte Befehlszeilen-Tool von Windows, mit dem Sie hier Git und Claude Code ausführen
- **Git** - Verfolgt jede Änderung an Ihren Dateien auf Ihrem Computer und erstellt Wiederherstellungspunkte, zu denen Sie jederzeit zurückkehren können
- **Commit** - Ein Snapshot Ihres Projekts zu einem bestimmten Zeitpunkt mit einer Beschreibung dessen, was sich geändert hat
- **Claude Code** - KI-Programmierassistent, der Code schreibt, Fehler behebt und Git-Operationen durch einfache Anfragen erledigt

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win)
- 20-30 Minuten

## Schritt 1: PowerShell öffnen

- Klicken Sie auf das **Start**-Menü
- Geben Sie `PowerShell` ein
- Klicken Sie auf **Windows PowerShell**, um es zu öffnen

**Hinweis:** Wenn Sie statt der nativen Installation den optionalen WSL/Ubuntu-Weg eingerichtet haben, öffnen Sie stattdessen die App **Ubuntu** – Git und Claude Code funktionieren dort genauso, nur mit Linux-Pfaden (`/mnt/c/Users/...`) statt `~\Documents\...`.

## Schritt 2: Git installieren

- Überprüfen Sie, ob Git bereits installiert ist:
  ```
  git --version
  ```
- Wenn Sie eine Versionsnummer wie `git version 2.45.0` sehen, springen Sie zu Schritt 3
- Wenn Sie eine Fehlermeldung sehen, installieren Sie Git for Windows:
  - Gehen Sie zu [git-scm.com/download/win](https://git-scm.com/download/win)
  - Klicken Sie auf dieser Seite oben auf **Click here to download** und öffnen Sie dann das Installationsprogramm, wenn der Download abgeschlossen ist
  - Klicken Sie sich mit **Next** durch das Installationsprogramm und übernehmen Sie die Standardoptionen
  - Klicken Sie auf **Install** und dann auf **Finish**
  - Schließen und öffnen Sie PowerShell erneut und überprüfen Sie dann noch einmal mit `git --version`

## Schritt 3: Git mit Ihrer Identität konfigurieren

Git muss für Commit-Nachrichten wissen, wer Sie sind.

- Legen Sie Ihren Namen und Ihre E-Mail fest (kann fiktiv sein):
  ```
  git config --global user.name "Ihr Name"
  git config --global user.email "ihre.email@beispiel.com"
  ```

Mit Name und E-Mail können Sie später erkennen, wer welche Änderung vorgenommen hat, wenn mehrere Personen am Projekt arbeiten.

## Schritt 4: Zu Ihrem Dokumente-Ordner navigieren

- Navigieren Sie zu Ihrem Dokumente-Ordner:
  ```
  cd ~\Documents
  ```
- Überprüfen Sie, ob Sie am richtigen Ort sind:
  ```
  pwd
  ```

Sie sollten einen Pfad sehen, der auf `\Documents` endet.

Wenn Sie `Cannot find path` sehen, wird Ihr Dokumente-Ordner wahrscheinlich von OneDrive gesichert. Führen Sie stattdessen `cd ~\OneDrive\Documents` aus. Auf deutschem Windows heißt dieser Ordner meist `OneDrive\Dokumente`; verwenden Sie dann `cd ~\OneDrive\Dokumente`.

## Schritt 5: Projektordner erstellen

- Erstellen Sie einen Ordner namens `test_claude`:
  ```
  mkdir test_claude
  ```
- Navigieren Sie hinein:
  ```
  cd test_claude
  ```

Hier wird Ihr Projekt gespeichert.

## Schritt 6: Claude Code starten

- Starten Sie Claude Code:
  ```
  claude
  ```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im [Installations-Tutorial](Install_CLAUDE_Code_Win.md) beschrieben. Nach der Anmeldung sehen Sie eine Willkommensnachricht und das Eingabefeld von Claude Code.

## Schritt 7: Claude bitten, Git zu initialisieren

- Geben Sie diese Anfrage ein:
  ```
  Beginne mit der Nachverfolgung von Änderungen
  ```

Claude initialisiert ein Git-Repository in Ihrem Ordner (dauert 2-5 Sekunden). Sie haben jetzt Versionskontrolle!

## Schritt 8: Die Timer-App erstellen

- Kopieren Sie in Claude Code diese gesamte Anfrage und fügen Sie sie ein (beim Einfügen bleiben alle Zeilen zusammen; wenn Sie Enter drücken, würde sie zu früh abgeschickt):

  ```
  Erstelle eine einfache Countdown-Timer-App in einer einzelnen Datei namens timer.html.
  Sie soll Folgendes enthalten:
  - Ein Eingabefeld zum Einstellen der Minuten
  - Start- und Stopp-Schaltflächen
  - Eine Anzeige mit der verbleibenden Zeit im MM:SS-Format
  ```

Claude erstellt `timer.html` (dauert 10-30 Sekunden) mit dem CSS- und JavaScript-Code.

## Schritt 9: Den Timer testen

- Öffnen Sie den **Datei-Explorer** (File Explorer) von Windows
- Navigieren Sie zu `Dokumente\test_claude`
- Doppelklicken Sie auf `timer.html`, um sie in Ihrem Browser zu öffnen
- Testen Sie den Timer:
  - Geben Sie `1` in das Eingabefeld ein
  - Klicken Sie auf **Start**
  - Beobachten Sie den Countdown

**Sie sehen `test_claude` nicht?** Wenn OneDrive Ihre Dokumente sichert, zeigt der Datei-Explorer einen anderen Dokumente-Ordner an. Klicken Sie in die Adressleiste des Datei-Explorers, fügen Sie `%USERPROFILE%\Documents\test_claude` ein und drücken Sie **Enter**.

**Wenn etwas nicht funktioniert:** Beschreiben Sie in Claude Code den Fehler: „Ich sehe diesen Fehler: [beschreiben Sie, was passiert ist]. Kannst du das reparieren?“

## Schritt 10: Claude bitten zu committen

- Geben Sie in Claude Code ein:
  ```
  Speichere diese Änderungen.
  ```

Claude wird:
- Prüfen, welche Dateien sich geändert haben
- Eine beschreibende Commit-Nachricht schreiben
- Den Commit erstellen (dauert 5-10 Sekunden)

Sie haben Ihren ersten Speicherpunkt erstellt! Sie können immer zu dieser funktionierenden Version zurückkehren.

## Schritt 11: Preset-Schaltflächen hinzufügen

- Geben Sie in Claude Code ein:
  ```
  Füge zwei Schaltflächen oben hinzu. Wenn ich darauf klicke, starten automatisch 1- und 5-Minuten-Timer.
  ```
- Aktualisieren Sie Ihren Browser-Tab (drücken Sie `F5` oder `Strg + R`)
- Testen Sie: Klicken Sie auf die **5 min**-Schaltfläche
- Wenn es funktioniert, committen Sie die Änderungen:
  ```
  Speichere diese Änderungen.
  ```

Wir haben einen 2. Speicherpunkt erstellt. Diese Version hat die zwei funktionierenden Schaltflächen.


## Schritt 12: Eine weitere Schaltfläche hinzufügen

- Geben Sie in Claude Code ein:
  ```
  Füge eine 15-Minuten-Schaltfläche hinzu.
  ```
- Aktualisieren Sie Ihren Browser-Tab (drücken Sie `F5` oder `Strg + R`)
- Testen Sie: Klicken Sie auf die **15 min**-Schaltfläche

**Für dieses Tutorial:** Tun Sie so, als würde die 15-Minuten-Schaltfläche nicht korrekt funktionieren. Committen Sie noch nicht – wir üben das Verwerfen schlechter Änderungen.

## Schritt 13: Änderungen verwerfen

Manchmal funktioniert KI-Code nicht und Sie müssen von Ihrem letzten Speicherpunkt neu beginnen.

- Geben Sie in Claude Code ein:
  ```
  Verwirf diese Änderungen.
  ```
- Claude bittet Sie meist zuerst um eine Bestätigung. Wenn ein Menü erscheint, wählen Sie **Yes** (mit den Pfeiltasten oder der Zahl daneben) und drücken Sie **Enter**. Wenn Claude in einer Nachricht nachfragt, tippen Sie `ja, verwirf die Änderungen an timer.html` und drücken Sie **Enter**
- Aktualisieren Sie Ihren Browser – die 15-Minuten-Schaltfläche verschwindet

Claude verwirft die neuen Änderungen, die wir nicht mögen. Der Timer funktioniert wieder mit nur den 1- und 5-Minuten-Schaltflächen!

## Schritt 14: Tonbenachrichtigung hinzufügen

- Geben Sie in Claude Code ein:
  ```
  Füge eine Tonbenachrichtigung hinzu, wenn der Timer Null erreicht.
  ```
- Aktualisieren Sie den Browser und testen Sie, nachdem Claude fertig ist (stellen Sie den Timer auf 1 Minute)
- Wenn es funktioniert, committen Sie die Änderungen:
  ```
  Speichere diese Änderungen.
  ```

## Schritt 15: Schlummer-Schaltfläche hinzufügen

- Geben Sie in Claude Code ein:
  ```
  Der Ton soll weiterlaufen, bis ich eine Schaltfläche zum Schlummern drücke.
  ```
- Aktualisieren Sie den Browser und testen Sie, nachdem Claude fertig ist (stellen Sie den Timer auf 1 Minute)
- Wenn es funktioniert, committen Sie die Änderungen:
  ```
  Speichere diese Änderungen.
  ```

## Schritt 16: Ihren Commit-Verlauf ansehen

- Geben Sie in Claude Code ein:
  ```
  Zeige meinen Änderungsverlauf
  ```

Claude zeigt Ihre Commits in einem lesbaren Format an. Sie sehen:
- Ihren ursprünglichen Timer-App-Commit
- Den Commit mit den Preset-Schaltflächen (1 und 5 Minuten)
- Den Tonbenachrichtigungs-Commit
- Den Schlummer-Schaltflächen-Commit

Beachten Sie, dass der 15-Minuten-Schaltflächen-Versuch nicht da ist – Sie haben ihn verworfen!

## Schritt 17: Den Code untersuchen

- Klicken Sie im Browser, der die App zeigt, mit der rechten Maustaste und wählen Sie **Seitenquelltext anzeigen** (View Page Source)
- Sie können den Quellcode dafür sehen.
- Fragen Sie in Claude Code:
  ```
  Erkläre diesen Code. Nur das große Ganze.
  ```

## Der komplette Workflow

- Claude bitten, Änderungen vorzunehmen
- Testen
- Wenn es funktioniert → Claude bitten zu committen
- Wenn es fehlschlägt → Claude bitten, es zu reparieren
- Nicht reparierbar → Änderungen verwerfen und erneut versuchen
- Wiederholen

Sie können immer zu jedem Commit zurückkehren. Verwerfen Sie furchtlos – committen Sie nur funktionierenden Code!

## Nächste Schritte

Versuchen Sie, weitere Funktionen zu Ihrem Timer hinzuzufügen:

- **15-Minuten-Schaltfläche:** `Füge eine funktionierende 15-Minuten-Preset-Schaltfläche hinzu` (wiederholen Sie, was wir verworfen haben!)
- **Pause-Schaltfläche:** `Füge eine Pause/Fortsetzen-Schaltfläche hinzu, die den Timer-Status umschaltet`
- **Besseres Styling:** `Verbessere das visuelle Design mit einem modernen Farbschema und größeren Schriften`
- **Fortschrittsbalken:** `Füge einen visuellen Fortschrittsbalken hinzu, der die verbleibende Zeit anzeigt`

Denken Sie daran: Nach jeder Funktion testen, nach jedem Erfolg committen, Fehlschläge verwerfen.

## Fehlerbehebung

- **„not a git repository“-Fehler:** Stellen Sie sicher, dass Sie im test_claude-Ordner sind (`cd ~\Documents\test_claude` oder, wenn Sie in Schritt 4 den OneDrive-Pfad verwendet haben, `cd ~\OneDrive\Documents\test_claude` – auf deutschem Windows meist `cd ~\OneDrive\Dokumente\test_claude`)
- **timer.html in Windows nicht gefunden:** Die Datei ist unter `C:\Users\IHR_BENUTZERNAME\Documents\test_claude\timer.html` (oder `C:\Users\IHR_BENUTZERNAME\OneDrive\Documents\test_claude\timer.html` – auf deutschem Windows meist `C:\Users\IHR_BENUTZERNAME\OneDrive\Dokumente\test_claude\timer.html` –, wenn Sie in Schritt 4 den OneDrive-Pfad verwendet haben)
- **Befehl `git` nicht gefunden:** Schließen und öffnen Sie PowerShell nach der Installation von Git for Windows erneut, damit der PATH aktualisiert wird, und führen Sie dann noch einmal `git --version` aus
- **Timer funktioniert nicht:** Öffnen Sie die Browser-Konsole (Rechtsklick auf die Seite, **Untersuchen** auswählen, Tab **Konsole** (Console) klicken), kopieren Sie alle roten Fehlermeldungen und fügen Sie sie Claude ein

## Was Sie Claude fragen können

- `Welche Dateien habe ich geändert?` - Noch nicht committete Änderungen sehen
- `Zeige mir die Unterschiede` - Genau sehen, welcher Code sich geändert hat
- `Erkläre, was der Timer-Code macht` - Die Implementierung verstehen
- `Erstelle einen Branch namens experiment` - Riskante Änderungen sicher ausprobieren
- `Mach alles seit meinem letzten Commit rückgängig` - Änderungen verwerfen, die Sie noch nicht gespeichert haben

Claude erledigt alle Git-Operationen durch natürliche Sprache – keine Befehle zum Auswendiglernen!

## Workflow-Überblick

- **Einrichtung:** Git einmal installieren, Identität einmal konfigurieren
- **Entwicklung:** Claude schreibt Code, Sie testen im Browser
- **Versionskontrolle:** Claude erledigt alle Git-Operationen über einfache Anfragen
- **Sicherheit:** Schlechte Änderungen jederzeit verwerfen, zu jedem vorherigen Commit zurückkehren
- **Lokal:** Ihr Git-Verlauf bleibt auf Ihrem Computer – kein GitHub-Konto nötig (Claude Code selbst braucht trotzdem Internet und Ihr Claude-Konto)

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 8. Dezember 2025.
