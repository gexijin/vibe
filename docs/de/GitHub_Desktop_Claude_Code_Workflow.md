[Startseite](./)

# GitHub Desktop mit Claude Code verwenden

Sie programmieren mit KI-Unterstützung. Sie nimmt Änderungen an Ihren Dateien vor. Manchmal funktionieren die Änderungen perfekt. Manchmal nicht. **Versionskontrolle ist wie eine Rückgängig-Taste für Ihr gesamtes Projekt.** Jedes Mal, wenn Sie einen Snapshot speichern (genannt „Commit"), erstellen Sie einen Wiederherstellungspunkt. Sie können immer zurückgehen.

Wenn Sie [GitHub Desktop](https://desktop.github.com) mit [Claude Code](https://claude.com/claude-code) kombinieren, erhalten Sie KI-Geschwindigkeit bei der Entwicklung mit professioneller Versionskontrolle.

## Wichtige Konzepte

**Git** verfolgt jede Änderung an Ihren Dateien auf Ihrem Computer.

**GitHub** speichert Ihren Code in der Cloud als Backup.

**GitHub Desktop** macht Git visuell – Sie klicken auf Schaltflächen statt Befehle zu tippen.

**Claude Code** ist ein KI-Programmierassistent, der Code schreibt, Fehler behebt und Commits für Sie erstellt.

## Was Sie tun werden

Erstellen Sie eine einfache Timer-App mit Claude Code und verfolgen Sie alle Änderungen mit GitHub Desktop:
- Projekt und Timer-App erstellen
- Testen und Fehler beheben
- Änderungen committen und pushen
- Schlechte Änderungen verwerfen und erneut versuchen
- Claude Commits automatisieren lassen

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win) oder [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS)
- Abgeschlossenes Tutorial [Erste Schritte mit Versionskontrolle](./Github_desktop)
- 20 Minuten

## Schritt 1: Ihr Projekt erstellen

- Öffnen Sie **GitHub Desktop**
- Klicken Sie auf **File** → **New Repository**
- Füllen Sie aus:
  - **Name:** `test_claude`
  - **Description:** `Eine Timer-App erstellt mit Claude Code`
  - **Local Path:** Dokumente-Ordner
  - **Aktivieren Sie** „Initialize this repository with a README"
- Klicken Sie auf **Create Repository**
- Klicken Sie oben auf **Publish repository**
- Klicken Sie auf **Publish Repository**

Sie haben jetzt ein lokales Projekt und ein Cloud-Backup auf GitHub.

## Schritt 2: Claude bitten, die Timer-App zu erstellen

- Öffnen Sie Ihr **Terminal**
- Navigieren Sie zu Ihrem Projekt:
  ```
  cd ~/Documents/test_claude
  ```
- Starten Sie Claude Code:
  ```
  claude
  ```
- Geben Sie diese Anfrage ein:
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  - When timer reaches zero, display 'Time's up!'
  Keep it simple with inline CSS and JavaScript.
  ```

Claude erstellt die `timer.html`-Datei (dauert 10-30 Sekunden).

## Schritt 3: Den Timer testen

- Klicken Sie in GitHub Desktop auf **Repository** → **Im Finder/Explorer anzeigen**
- **Doppelklicken Sie** auf `timer.html`, um sie in Ihrem Browser zu öffnen
- Testen Sie den Timer:
  - Geben Sie `1` in das Eingabefeld ein
  - Klicken Sie auf **Start**
  - Beobachten Sie den Countdown

**Wenn es funktioniert:** Gehen Sie zu Schritt 5.
**Wenn etwas nicht funktioniert:** Fahren Sie mit Schritt 4 fort.

## Schritt 4: Fehler beheben (falls nötig)

- Öffnen Sie die Browser-Konsole (Rechtsklick auf Seite → **Untersuchen** → Tab **Console**)
- Kopieren Sie alle roten Fehlermeldungen
- Gehen Sie zurück zu Claude Code in Ihrem Terminal
- Fügen Sie den Fehler ein:
  ```
  I'm seeing this error: [Fehler einfügen]. Can you fix it?
  ```
- Aktualisieren Sie den Browser (klicken Sie auf die Neu laden-Schaltfläche oder Rechtsklick → **Neu laden**) und testen Sie erneut

## Schritt 5: Änderungen überprüfen

- Wechseln Sie zu **GitHub Desktop**
- **Linkes Panel:** Zeigt geänderte Dateien (`timer.html`)
- **Rechtes Panel:** Zeigt den Code (grün = hinzugefügt)
- Lesen Sie durch, um zu verstehen, was Claude erstellt hat

Überprüfen Sie immer KI-generierten Code vor dem Committen.

## Schritt 6: Manuell committen

- Geben Sie unten links im **Summary-Feld** ein:
  ```
  Create initial timer app with start/stop functionality
  ```
- Klicken Sie auf **Commit to main**

Sie haben einen Speicherpunkt erstellt!

**Gute Commit-Nachrichten:** „Create initial timer app", „Fix start button"
**Schlechte Commit-Nachrichten:** „changes", „update", „asdf"

## Schritt 7: Auf GitHub pushen

- Klicken Sie oben auf die Schaltfläche **Push origin**
- Überprüfen Sie: **Repository** → **View on GitHub**, um Ihren Code online zu sehen

Ihr Code ist jetzt in der Cloud gesichert.

## Schritt 8: Tonbenachrichtigung hinzufügen

- Im Claude Code-Terminal:
  ```
  Add a sound notification when the timer reaches zero. Use the browser's
  built-in beep sound or create a simple audio alert.
  ```
- Testen Sie: Browser aktualisieren, Timer auf 0.1 Minuten setzen, Start klicken

**Für dieses Tutorial:** Tun Sie so, als würde der Ton nicht gut funktionieren. Committen Sie noch nicht!

## Schritt 9: Schlechte Änderungen verwerfen

Manchmal führt uns KI auf den falschen Weg und wir müssen von unserem letzten Commit (Speicherpunkt) neu beginnen.

- Öffnen Sie **GitHub Desktop**
- Klicken Sie auf **Branch**-Menü → **Discard All Changes**
- Klicken Sie auf **Discard Changes** zur Bestätigung
- Browser aktualisieren – der Timer funktioniert ohne den Ton!

Sie haben gerade fehlerhaften Code verworfen und sind zu Ihrem letzten Speicherpunkt zurückgekehrt.

## Schritt 10: Von vorne neu machen

- In Claude Code:
  ```
  Add a sound notification when the timer reaches zero. This time, use an HTML5
  audio element with a simple beep sound generated by the Web Audio API. Make
  sure it handles browser autoplay restrictions gracefully.
  ```
- Sofort testen (Browser aktualisieren, 0.1 Minuten setzen, Start)

**Wenn es funktioniert:** Weiter zu Schritt 11.
**Wenn nicht:** Fehler zu Claude einfügen oder erneut versuchen.

## Schritt 11: Claude committen und pushen lassen

- In Claude Code:
  ```
  commit and push my changes
  ```

Claude überprüft Änderungen, schreibt eine Commit-Nachricht, committet und pusht (10-20 Sekunden).

**Wann verwenden:**
- Manuelle Commits: Beim Lernen oder wenn Sie Kontrolle wollen
- Claude-Commits: Beim schnellen Arbeiten und wenn Sie gute Nachrichten wollen

## Schritt 12: Claude bitten, Änderungen zusammenzufassen

- In Claude Code:
  ```
  what files have I changed?
  ```

Claude erklärt Ihre Änderungen in einfachem Englisch.

**Probieren Sie:** `explain what the audio code does` oder `show me the last 5 commits`

## Schritt 13: Verlauf ansehen

- Klicken Sie in **GitHub Desktop** auf den Tab **History**

Sie sehen:
- Initial commit (README)
- Create initial timer app
- Add improved sound notification

Beachten Sie, dass der erste fehlgeschlagene Tonversuch nicht da ist – Sie haben ihn verworfen! Nur funktionierender Code hat es in Ihre Commits geschafft.

## Herausforderungen
- Benutzerdefinierter Ton: Laden Sie eine kostenlose .mp3 von [freesound.org](https://freesound.org) herunter, legen Sie sie in Ihren Projektordner, bitten Sie Claude, sie zu verwenden
- Mehrere Timer: `Allow users to create and run multiple timers simultaneously`
- Fortschrittsbalken: `Add a progress bar that visually shows how much time remains`

**Denken Sie daran:** Nach jeder Funktion testen, nach jedem Erfolg committen, Fehlschläge verwerfen.

**Sehen Sie Ihr Projekt auf GitHub.com:** Klicken Sie auf **Repository** → **View on GitHub** in GitHub Desktop, um Ihren vollständigen Commit-Verlauf und Code online zu sehen.

## Fehlerbehebung

**„Authentication failed":** GitHub Desktop → File/Preferences → Accounts → Abmelden und erneut anmelden

**Claude sagt „not a git repository":** Stellen Sie sicher, dass Sie im richtigen Ordner sind (`cd ~/Documents/test_claude`)

**Timer funktioniert nicht:** Browser-Konsole öffnen (Rechtsklick → **Untersuchen** → **Console**), Fehler kopieren, zu Claude einfügen

**Brauchen Sie Hilfe?** [GitHub Desktop docs](https://docs.github.com/en/desktop) • [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)

## Der komplette Workflow

- Claude bitten, Änderungen vorzunehmen
- Im Browser testen
- Wenn es funktioniert → Überprüfen und committen
- Wenn es fehlschlägt → Verwerfen und erneut versuchen
- Auf GitHub pushen
- Wiederholen

Manuelle Commits, wenn Sie Kontrolle wollen. Claude-Commits, wenn Sie Geschwindigkeit wollen. Verwerfen Sie furchtlos – committen Sie nur funktionierenden Code!

## Nächste Schritte

Versuchen Sie, Funktionen zu Ihrem Timer hinzuzufügen:

**Schnelle Erfolge:**
- Preset-Schaltflächen für 5, 10, 15 Minuten: `Add three preset buttons: "5 min", "10 min", and "15 min"`
- Pause-Schaltfläche: `Add a Pause/Resume button that toggles the timer state`
- Besseres Styling: `Improve the visual design with a modern color scheme`

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
