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
  Erstelle eine einfache Countdown-Timer-App in einer einzelnen Datei namens timer.html.
  Sie sollte haben:
  - Ein Eingabefeld zum Einstellen der Minuten
  - Start- und Stopp-Schaltflächen
  - Eine Anzeige mit der verbleibenden Zeit im MM:SS-Format
  - Wenn der Timer Null erreicht, zeige 'Zeit abgelaufen!'
  Halte es einfach mit Inline-CSS und JavaScript.
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
  Ich sehe diesen Fehler: [Fehler einfügen]. Kannst du ihn beheben?
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
  Erstelle erste Timer-App mit Start/Stopp-Funktionalität
  ```
- Klicken Sie auf **Commit to main**

Sie haben einen Speicherpunkt erstellt!

**Gute Commit-Nachrichten:** „Erstelle erste Timer-App", „Behebe Start-Schaltfläche"
**Schlechte Commit-Nachrichten:** „Änderungen", „Update", „asdf"

## Schritt 7: Auf GitHub pushen

- Klicken Sie oben auf die Schaltfläche **Push origin**
- Überprüfen Sie: **Repository** → **View on GitHub**, um Ihren Code online zu sehen

Ihr Code ist jetzt in der Cloud gesichert.

## Schritt 8: Tonbenachrichtigung hinzufügen

- Im Claude Code-Terminal:
  ```
  Füge eine Tonbenachrichtigung hinzu, wenn der Timer Null erreicht. Verwende den
  eingebauten Browser-Signalton oder erstelle einen einfachen Audio-Alarm.
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
  Füge eine Tonbenachrichtigung hinzu, wenn der Timer Null erreicht. Verwende diesmal ein HTML5-
  Audioelement mit einem einfachen Signalton, der über die Web Audio API erzeugt wird. Stelle
  sicher, dass Browser-Autoplay-Einschränkungen elegant behandelt werden.
  ```
- Sofort testen (Browser aktualisieren, 0.1 Minuten setzen, Start)

**Wenn es funktioniert:** Weiter zu Schritt 11.
**Wenn nicht:** Fehler zu Claude einfügen oder erneut versuchen.

## Schritt 11: Claude committen und pushen lassen

- In Claude Code:
  ```
  Committe und pushe meine Änderungen
  ```

Claude überprüft Änderungen, schreibt eine Commit-Nachricht, committet und pusht (10-20 Sekunden).

**Wann verwenden:**
- Manuelle Commits: Beim Lernen oder wenn Sie Kontrolle wollen
- Claude-Commits: Beim schnellen Arbeiten und wenn Sie gute Nachrichten wollen

## Schritt 12: Claude bitten, Änderungen zusammenzufassen

- In Claude Code:
  ```
  Welche Dateien habe ich geändert?
  ```

Claude erklärt Ihre Änderungen in einfacher Sprache.

**Probieren Sie:** `Erkläre, was der Audio-Code macht` oder `Zeige mir die letzten 5 Commits`

## Schritt 13: Verlauf ansehen

- Klicken Sie in **GitHub Desktop** auf den Tab **History**

Sie sehen:
- Initial commit (README)
- Create initial timer app
- Add improved sound notification

Beachten Sie, dass der erste fehlgeschlagene Tonversuch nicht da ist – Sie haben ihn verworfen! Nur funktionierender Code hat es in Ihre Commits geschafft.

## Herausforderungen
- Benutzerdefinierter Ton: Laden Sie eine kostenlose .mp3 von [freesound.org](https://freesound.org) herunter, legen Sie sie in Ihren Projektordner, bitten Sie Claude, sie zu verwenden
- Mehrere Timer: `Ermögliche Benutzern, mehrere Timer gleichzeitig zu erstellen und auszuführen`
- Fortschrittsbalken: `Füge einen Fortschrittsbalken hinzu, der visuell zeigt, wie viel Zeit verbleibt`

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
- Preset-Schaltflächen für 5, 10, 15 Minuten: `Füge drei Preset-Schaltflächen hinzu: "5 min", "10 min" und "15 min"`
- Pause-Schaltfläche: `Füge eine Pause/Fortsetzen-Schaltfläche hinzu, die den Timer-Status umschaltet`
- Besseres Styling: `Verbessere das visuelle Design mit einem modernen Farbschema`

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
