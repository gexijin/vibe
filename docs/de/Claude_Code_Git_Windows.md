[Startseite](./)

# Claude Code mit Versionskontrolle für Windows

Sie arbeiten mit KI-Unterstützung. Sie nimmt Änderungen an Ihren Dateien vor. Manchmal sind die Änderungen brillant. Manchmal nicht. **Versionskontrolle ist wie eine Rückgängig-Taste für Ihr gesamtes Projekt.** Jedes Mal, wenn Sie einen Snapshot speichern (genannt „Commit"), erstellen Sie einen Wiederherstellungspunkt, zu dem Sie immer zurückkehren können. Das Beste daran: Sie können dies komplett auf Ihrem Computer machen und Claude Code erledigt es für Sie.

## Wichtige Konzepte

- **WSL (Windows Subsystem for Linux)** - Führt Linux-Tools wie Git nativ unter Windows aus
- **Git** - Verfolgt jede Änderung an Ihren Dateien auf Ihrem Computer und erstellt Wiederherstellungspunkte, zu denen Sie jederzeit zurückkehren können
- **Commit** - Ein Snapshot Ihres Projekts zu einem bestimmten Zeitpunkt mit einer Beschreibung dessen, was sich geändert hat
- **Claude Code** - KI-Programmierassistent, der Code schreibt, Fehler behebt und Git-Operationen durch einfache Anfragen erledigt

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code unter Windows installieren](./Install_CLAUDE_Code_Win)
- WSL und Ubuntu installiert
- 20 Minuten

## Schritt 1: Ubuntu-Terminal öffnen

- Klicken Sie auf das **Start**-Menü
- Geben Sie `Ubuntu` ein
- Klicken Sie auf **Ubuntu**, um das Terminal zu öffnen

Sie sehen eine Eingabeaufforderung, die mit `$` endet.

## Schritt 2: Git installieren

- Geben Sie diesen Befehl ein und drücken Sie Enter:
  ```
  sudo apt-get install git
  ```
- Wenn Sie dazu aufgefordert werden, geben Sie Ihr Passwort ein und drücken Sie Enter
- Warten Sie, bis die Installation abgeschlossen ist (10-30 Sekunden)
- Überprüfen Sie, ob Git installiert ist:
  ```
  git --version
  ```

Sie sollten etwas wie `git version 2.34.1` sehen.

## Schritt 3: Git mit Ihrer Identität konfigurieren

Git muss wissen, wer Sie sind, für Commit-Nachrichten.

- Legen Sie Ihren Namen und Ihre E-Mail fest (kann fiktiv sein):
  ```
  git config --global user.name "Ihr Name"
  git config --global user.email "ihre.email@beispiel.com"
  ```

Die Verwendung Ihres Namens und Ihrer E-Mail hilft Ihnen zu identifizieren, wer Änderungen vorgenommen hat, wenn mehrere Personen daran arbeiten.

## Schritt 4: Zu einem Windows-Ordner navigieren

WSL kann über `/mnt/c/` auf Ihre Windows-Dateien zugreifen.

- Navigieren Sie zu Ihrem Windows-Benutzerordner:
  ```
  cd /mnt/c/Users/IHR_BENUTZERNAME/Documents
  ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren tatsächlichen Windows-Benutzernamen.
- Überprüfen Sie, ob Sie am richtigen Ort sind:
  ```
  pwd
  ```

Sie sollten `/mnt/c/Users/IHR_BENUTZERNAME/Documents` sehen.

## Schritt 5: Projektordner erstellen

- Erstellen Sie einen Ordner namens `test_claude`:
  ```
  mkdir test_claude
  ```
- Navigieren Sie hinein:
  ```
  cd test_claude
  ```

Hier wird Ihr Projekt leben.

## Schritt 6: Claude Code starten

- Starten Sie Claude Code:
  ```
  claude
  ```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im [Installations-Tutorial](Install_CLAUDE_Code_Win.md) beschrieben. Nach der Anmeldung sehen Sie eine Willkommensnachricht und die Claude Code-Eingabeaufforderung.

## Schritt 7: Claude bitten, Git zu initialisieren

- Geben Sie diese Anfrage ein:
  ```
  Beginne mit der Nachverfolgung von Änderungen
  ```

Claude initialisiert ein Git-Repository in Ihrem Ordner (dauert 2-5 Sekunden). Sie haben jetzt Versionskontrolle!

## Schritt 8: Die Timer-App erstellen

- Geben Sie in Claude Code ein:
  ```
  Erstelle eine einfache Countdown-Timer-App in einer einzelnen Datei namens timer.html.
  Sie sollte haben:
  - Ein Eingabefeld zum Einstellen der Minuten
  - Start- und Stopp-Schaltflächen
  - Eine Anzeige mit der verbleibenden Zeit im MM:SS-Format
  ```

Claude erstellt `timer.html` (dauert 10-30 Sekunden) mit dem CSS- und JavaScript-Code.

## Schritt 9: Den Timer testen

- Öffnen Sie den Windows Datei-Explorer
- Navigieren Sie zu `Dokumente\test_claude`
- Doppelklicken Sie auf `timer.html`, um sie in Ihrem Browser zu öffnen
- Testen Sie den Timer:
  - Geben Sie `1` in das Eingabefeld ein
  - Klicken Sie auf **Start**
  - Beobachten Sie den Countdown

**Wenn etwas nicht funktioniert:** Beschreiben Sie in Claude Code den Fehler: „Ich sehe diesen Fehler: [beschreiben Sie, was passiert ist]. Kannst du das reparieren?"

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
- Aktualisieren Sie Ihren Browser-Tab
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
- Aktualisieren Sie Ihren Browser-Tab
- Testen Sie: Klicken Sie auf die **15 min**-Schaltfläche

**Für dieses Tutorial:** Tun Sie so, als würde die 15-Minuten-Schaltfläche nicht korrekt funktionieren. Committen Sie noch nicht – wir üben das Verwerfen schlechter Änderungen.

## Schritt 13: Änderungen verwerfen

Manchmal funktioniert KI-Code nicht und Sie müssen von Ihrem letzten Speicherpunkt neu beginnen.

- Geben Sie in Claude Code ein:
  ```
  Verwirf diese Änderungen.
  ```
- Claude wird um Bestätigung bitten
- Drücken Sie `1` und dann Enter
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
  Der Ton sollte weiterlaufen, bis ich auf eine Schaltfläche klicke, um ihn stummzuschalten.
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
- Den Preset-Schaltflächen (1-min und 5-min) Commit
- Den Tonbenachrichtigungs-Commit
- Die Schlummer-Schaltfläche.

Beachten Sie, dass der 15-Minuten-Schaltflächen-Versuch nicht da ist – Sie haben ihn verworfen!

## Schritt 17: Den Code untersuchen

- Klicken Sie im Browser, der die App zeigt, mit der rechten Maustaste und wählen Sie **Quelltext anzeigen**
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

- **„not a git repository"-Fehler:** Stellen Sie sicher, dass Sie im test_claude-Ordner sind (`cd /mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude`)
- **timer.html in Windows nicht gefunden:** Die Datei ist unter `C:\Users\IHR_BENUTZERNAME\Documents\test_claude\timer.html`
- **Git fragt nach Passwort:** Sie haben das `sudo`-Passwort falsch eingegeben – versuchen Sie es noch einmal sorgfältig
- **Timer funktioniert nicht:** Öffnen Sie die Browser-Konsole (Rechtsklick auf die Seite, **Untersuchen** auswählen, Tab **Console** klicken), kopieren Sie alle roten Fehlermeldungen und fügen Sie sie Claude ein

## Was Sie Claude fragen können

- `Welche Dateien habe ich geändert?` - Uncommittete Änderungen sehen
- `Zeige mir die Unterschiede` - Genau sehen, welcher Code sich geändert hat
- `Erkläre, was der Timer-Code macht` - Die Implementierung verstehen
- `Erstelle einen Branch namens experiment` - Riskante Änderungen sicher ausprobieren
- `Gehe zurück zum vorherigen Commit` - Alles seit dem letzten Commit rückgängig machen

Claude erledigt alle Git-Operationen durch natürliche Sprache – keine Befehle zum Auswendiglernen!

## Workflow-Überblick

- **Einrichtung:** Git einmal installieren, Identität einmal konfigurieren
- **Entwicklung:** Claude schreibt Code, Sie testen im Browser
- **Versionskontrolle:** Claude erledigt alle Git-Operationen über einfache Anfragen
- **Sicherheit:** Schlechte Änderungen jederzeit verwerfen, zu jedem vorherigen Commit zurückkehren
- **Lokal:** Alles bleibt auf Ihrem Computer, kein Konto oder Internet erforderlich

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 8. Dezember 2025.
