[Startseite](./)

# Claude Code auf dem Mac installieren

Claude Code ist ein KI-Assistent, der in Ihrem Terminal lebt und Ihnen hilft, Code zu schreiben, zu debuggen und zu verstehen. Stellen Sie es sich als einen erfahrenen Programmierpartner vor, der jederzeit verfügbar ist, wenn Sie Hilfe benötigen. Ob Sie kompletter Anfänger oder erfahrener Entwickler sind – Claude Code kann Ihren Workflow beschleunigen und Ihnen beim Lernen helfen.

Diese Anleitung führt Sie Schritt für Schritt durch die Installation, mit detaillierten Anweisungen für Einsteiger.

## Überblick

- Node.js herunterladen und installieren
- Claude Code mit npm installieren
- Ihren API-Schlüssel konfigurieren
- Mit Claude Code beginnen

## Wichtige Konzepte

- **Terminal**: Eine integrierte Mac-App, in der Sie Befehle eingeben statt auf Schaltflächen zu klicken. So interagieren Sie mit Claude Code.
- **Node.js**: Software, die Claude Code zum Laufen benötigt. Betrachten Sie es als den Motor, der Claude Code antreibt.
- **Claude Code**: Ein KI-Programmierassistent, den Sie im Terminal ausführen. Er kann Fragen beantworten, Code schreiben und Ihnen helfen, bestehende Projekte zu verstehen.

## Was Sie benötigen

- Einen Mac-Computer (macOS 10.15 Catalina oder neuer empfohlen)
- Internetverbindung
- Administratorzugang auf Ihrem Computer
- Claude Pro/Max-Abonnement oder API-Schlüssel
- 15 - 20 Minuten

## Schritt 1: Node.js herunterladen

Claude Code erfordert Node.js Version 18 oder höher.

**Prüfen Sie zunächst, ob Node.js bereits installiert ist:**

- Klicken Sie auf das **Launchpad**-Symbol in Ihrem Dock (das Symbol mit den bunten Quadraten)
- Geben Sie `Terminal` in das Suchfeld oben ein
- Klicken Sie auf **Terminal** (ein schwarzes quadratisches Symbol)
- Geben Sie im Terminal ein:
   ```
   node --version
   ```
- Schauen Sie sich das Ergebnis an:
   - **Wenn Sie eine Versionsnummer wie `v18.x.x` oder höher sehen**: Node.js ist bereits installiert! Springen Sie zu Schritt 4.
   - **Wenn Sie „command not found" sehen**: Fahren Sie mit der Installation unten fort.

**Um Node.js herunterzuladen:**

- Öffnen Sie Ihren Webbrowser (Safari, Chrome, Firefox usw.)
- Gehen Sie zu dieser Website:
   ```
   https://nodejs.org/
   ```
- Klicken Sie auf die grüne Schaltfläche **Get Node.js**
- Klicken Sie auf die grüne Schaltfläche **macOS Installer (.pkg)** in der Mitte des Bildschirms
- Eine Datei wird in Ihren Downloads-Ordner heruntergeladen (dauert normalerweise 30-60 Sekunden)
   - Die Datei heißt etwa `node-v24.x.x.pkg`

## Schritt 2: Node.js installieren

- Öffnen Sie den **Finder** (klicken Sie auf das blaue lächelnde Gesicht-Symbol in Ihrem Dock)
- Klicken Sie auf **Downloads** in der linken Seitenleiste
- Suchen Sie die gerade heruntergeladene Datei (sieht aus wie `node-v24.x.x.pkg`)
- Doppelklicken Sie auf die Datei, um sie zu öffnen
- Ein Installationsfenster erscheint - klicken Sie auf **Fortfahren**
- Klicken Sie erneut auf **Fortfahren** beim Lizenz-Bildschirm
- Klicken Sie auf **Akzeptieren**, um die Lizenz anzunehmen
- Klicken Sie auf **Installieren**
- Sie werden nach Ihrem Mac-Passwort gefragt (das, mit dem Sie sich anmelden)
- Geben Sie Ihr Passwort ein und klicken Sie auf **Software installieren**
- Warten Sie, bis die Installation abgeschlossen ist (1-2 Minuten)
- Klicken Sie auf **Schließen**, wenn Sie „Die Installation war erfolgreich" sehen
- Sie können das Installationsprogramm in den Papierkorb verschieben, wenn Sie gefragt werden

## Schritt 3: Node.js-Installation überprüfen

- Klicken Sie auf das **Launchpad**-Symbol in Ihrem Dock (das Symbol mit den bunten Quadraten)
- Geben Sie `Terminal` in das Suchfeld oben ein
- Klicken Sie auf **Terminal** (ein schwarzes quadratisches Symbol)
- Ein Terminal-Fenster öffnet sich
- Geben Sie im Terminal ein:
   ```
   node --version
   ```
- Sie sollten etwas wie `v24.x.x` sehen (die genauen Zahlen können variieren)
- Wenn Sie eine Versionsnummer sehen, großartig! Node.js ist korrekt installiert

**Wenn Sie „command not found" sehen:**
- Schließen Sie Terminal vollständig (klicken Sie auf **Terminal** in der Menüleiste, dann auf **Terminal beenden**)
- Öffnen Sie Terminal erneut
- Versuchen Sie den Befehl noch einmal

**Tipp:** Lassen Sie Terminal für die nächsten Schritte geöffnet.

## Schritt 4: Claude Code installieren

- Geben Sie im Terminal ein:
   ```
   npm install -g @anthropic-ai/claude-code
   ```
- Warten Sie, bis Claude Code installiert ist (2-5 Minuten)
- Wenn Sie einen „permission denied"-Fehler sehen, versuchen Sie es mit `sudo`:
   ```
   sudo npm install -g @anthropic-ai/claude-code
   ```
   Geben Sie dann Ihr Mac-Passwort ein, wenn Sie dazu aufgefordert werden (Sie sehen es nicht beim Tippen)
- Sie sehen möglicherweise einige Warnungen in gelbem oder rotem Text - das ist normalerweise normal
- Wenn die Installation abgeschlossen ist, überprüfen Sie durch Eingabe von:
   ```
   claude --version
   ```
- Sie sollten die Versionsnummer von Claude Code sehen

## Schritt 5: Mit Ihrem Anthropic-Konto verbinden

### Option A. Ihr Claude Pro- oder Max-Abonnement verwenden

- Geben Sie im Terminal ein:
   ```
   claude
   ```
- Claude versucht, einen Browser zu öffnen. Wenn er sich nicht automatisch öffnet, kopieren Sie die im Terminal angezeigte URL und fügen Sie sie in Ihren Browser ein.
- Melden Sie sich bei Ihrem Claude.ai-Konto an (dies kann automatisch geschehen)
- Klicken Sie auf **Autorisieren**
- Klicken Sie auf **Code kopieren**, wenn ein langer Code erscheint
- Gehen Sie zurück zum Terminal-Fenster
- Zum Einfügen im Terminal: Klicken Sie auf **Bearbeiten** in der Menüleiste, dann auf **Einfügen**
- Sie sollten eine Erfolgsmeldung sehen
- Folgen Sie den Anweisungen, um die Einrichtung abzuschließen

### Option B. Anthropic-API-Schlüssel verwenden

Wenn Sie einen Anthropic-API-Schlüssel anstelle eines Claude-Abonnements haben:

- Holen Sie sich zunächst Ihren API-Schlüssel von der [Anthropic Console](https://console.anthropic.com/)
- Geben Sie im Terminal ein:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Ersetzen Sie `your-api-key-here` durch Ihren tatsächlichen API-Schlüssel
- Um dies dauerhaft zu machen (damit Sie es nicht jedes Mal einstellen müssen), fügen Sie es zu Ihrem Shell-Profil hinzu:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```
   Ersetzen Sie `your-api-key-here` durch Ihren tatsächlichen API-Schlüssel
- Schließen Sie Terminal und öffnen Sie es erneut, damit die Änderungen wirksam werden

**Hinweis:** Wenn Sie einen älteren Mac mit bash anstelle von zsh verwenden, ersetzen Sie `~/.zshrc` durch `~/.bash_profile` im obigen Befehl.

### Option C. Anthropic API über Azure Foundry verwenden

Diese Option ist für Organisationen gedacht, die Azure-gehostete Claude-Modelle verwenden. Fügen Sie im Terminal-Fenster diesen Code ein, um Umgebungsvariablen zu definieren (vor dem Starten von Claude):
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Hinweis:** Ersetzen Sie `xxxx-eastus2` durch Ihren Foundry-Ressourcennamen (verwenden Sie nicht die gesamte Basis-URL). Ersetzen Sie `your_api_key` durch Ihren vollständigen API-Schlüssel aus Ihrem Azure-Portal.

## Schritt 6: Mit Claude Code beginnen

Sie sind fertig! So verwenden Sie Claude Code:

- Geben Sie im Terminal ein:
   ```
   claude
   ```
- Es stellt Ihnen einige Fragen, bevor es bereit ist zum Chatten
- Um zu testen, ob es funktioniert, stellen Sie eine allgemeine Frage wie „Erkläre mir Quantencomputing."

## Schritt 7: Zu Ihrem Projekt navigieren

- Wenn Sie ein Projekt in Ihren Mac-Ordnern haben, können Sie dorthin navigieren:
   ```
   cd ~/Documents/test_claude
   ```
   Ersetzen Sie `test_claude` durch Ihren tatsächlichen Projektordnernamen

- Starten Sie dann Claude:
   ```
   claude
   ```
- Beginnen Sie damit, Claude zu bitten, Ihnen die Codebasis zu erklären.
- Sie können Claude bitten, Änderungen vorzunehmen.
- Testen Sie Ihren Code in Ihrer bevorzugten IDE.

**Hinweis:** Claude arbeitet innerhalb eines Projektordners. Es definiert Schreibrechte im Ordner und speichert Einstellungen in diesem Ordner. Es ist Claudes Arbeitsbereich.

## Nächste Schritte
- [VS Code Erste Schritte](./VS_Code_Getting_Started.md) - Lernen Sie VS Code kennen, einen beliebten Code-Editor
- [Claude Code in VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - Führen Sie Claude Code innerhalb von VS Code aus
- [Eine Forschungsarbeit mit Claude Code schreiben](./Writing_Research_Paper_Claude_Code.md) - Verwenden Sie Claude Code für akademisches Schreiben

## Terminal erneut öffnen

Nach dem Schließen von Terminal können Sie es so wieder öffnen:

- Klicken Sie auf das **Launchpad**-Symbol in Ihrem Dock (das Symbol mit den bunten Quadraten)
- Geben Sie `Terminal` in das Suchfeld oben ein
- Klicken Sie auf **Terminal**
- Ein Terminal-Fenster öffnet sich

## Fehlerbehebung

### Node.js-Installer lässt sich nicht öffnen
- Stellen Sie sicher, dass Sie die `.pkg`-Datei von nodejs.org heruntergeladen haben
- Versuchen Sie, mit der rechten Maustaste auf die Datei zu klicken und **Öffnen** auszuwählen, anstatt doppelt zu klicken
- Gehen Sie zu **Systemeinstellungen** > **Datenschutz & Sicherheit** und klicken Sie auf **Trotzdem öffnen**

### „node: command not found" nach der Installation
- Schließen Sie Terminal vollständig (klicken Sie auf **Terminal** in der Menüleiste, dann auf **Terminal beenden**)
- Öffnen Sie Terminal erneut
- Versuchen Sie `node --version` erneut
- Wenn es immer noch nicht funktioniert, starten Sie Ihren Mac neu und versuchen Sie es noch einmal

### npm-Installation schlägt mit Berechtigungsfehlern fehl
- Fügen Sie `sudo` vor dem npm-Befehl hinzu:
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
- Geben Sie Ihr Mac-Passwort ein, wenn Sie dazu aufgefordert werden (Sie sehen es nicht beim Tippen)

### Claude Code-Befehle werden nicht gefunden
- Stellen Sie sicher, dass die npm-Installation erfolgreich abgeschlossen wurde
- Versuchen Sie, Terminal zu schließen und erneut zu öffnen
- Prüfen Sie, ob Claude Code installiert ist: `npm list -g @anthropic/claude-code`
- Versuchen Sie es erneut zu installieren: `npm install -g @anthropic-ai/claude-code`

### „Cannot find module"-Fehler
- Stellen Sie sicher, dass Node.js richtig installiert ist: `node --version`
- Versuchen Sie, Claude Code neu zu installieren: `npm uninstall -g @anthropic/claude-code` dann `npm install -g @anthropic-ai/claude-code`

## Tipps für Mac-Benutzer

### Projektpfade finden
Um den Pfad zu einem Ordner zu finden:
- Öffnen Sie den Finder
- Navigieren Sie zu Ihrem Projektordner
- Ziehen Sie den Ordner per Drag & Drop ins Terminal - der vollständige Pfad erscheint!

### Verschiedene Terminal-Apps verwenden
Sie können auch andere Terminal-Apps verwenden wie:
- iTerm2 (beliebte Alternative mit mehr Funktionen)
- Warp (modernes Terminal mit KI-Funktionen)
- Hyper (plattformübergreifendes Terminal)

Claude Code funktioniert mit allen!

## Benötigen Sie Hilfe?

- Für Node.js-Download: [Node.js Offizielle Website](https://nodejs.org/)
- Für Node.js-Probleme: [Node.js Dokumentation](https://nodejs.org/docs/)
- Für npm-Probleme: [npm Dokumentation](https://docs.npmjs.com/)
- Für Claude Code-Probleme: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

*Zuletzt aktualisiert: Dezember 2025*
