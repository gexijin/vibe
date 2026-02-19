[Startseite](./)

# Claude Code auf dem Mac installieren

Claude Code ist ein KI-Assistent, der in Ihrem Terminal lebt und Ihnen hilft, Code zu schreiben, zu debuggen und zu verstehen. Stellen Sie es sich als einen erfahrenen Programmierpartner vor, der jederzeit verfügbar ist, wenn Sie Hilfe benötigen. Ob Sie kompletter Anfänger oder erfahrener Entwickler sind – Claude Code kann Ihren Workflow beschleunigen und Ihnen beim Lernen helfen.

Diese Anleitung führt Sie Schritt für Schritt durch die Installation, mit detaillierten Anweisungen für Einsteiger.

## Überblick

- Terminal öffnen
- Claude Code installieren
- Ihre API-Verbindung konfigurieren
- Mit Claude Code beginnen

## Wichtige Konzepte

- **Terminal**: Eine integrierte Mac-App, in der Sie Befehle eingeben statt auf Schaltflächen zu klicken. So interagieren Sie mit Claude Code.
- **Claude Code**: Ein KI-Programmierassistent, den Sie im Terminal ausführen. Er kann Fragen beantworten, Code schreiben und Ihnen helfen, bestehende Projekte zu verstehen.

## Was Sie benötigen

- Einen Mac-Computer (macOS 13.0 Ventura oder neuer)
- Internetverbindung
- Administratorzugang auf Ihrem Computer
- Claude Pro/Max-Abonnement oder API-Schlüssel
- 5 - 10 Minuten

## Schritt 1: Terminal öffnen

- Klicken Sie auf das **Launchpad**-Symbol in Ihrem Dock (das Symbol mit den bunten Quadraten)
- Geben Sie `Terminal` in das Suchfeld oben ein
- Klicken Sie auf **Terminal** (ein schwarzes quadratisches Symbol)
- Ein Terminal-Fenster öffnet sich mit einem blinkenden Cursor

**Tipp:** Lassen Sie Terminal für die nächsten Schritte geöffnet.

## Schritt 2: Claude Code installieren

Kopieren Sie im Terminal den folgenden Befehl, fügen Sie ihn ein und drücken Sie **Return**:
```
curl -fsSL https://claude.ai/install.sh | bash
```

- Warten Sie, bis Claude Code installiert ist (1-2 Minuten)
- Möglicherweise sehen Sie einige Fortschrittsmeldungen – das ist normal
- Wenn die Installation abgeschlossen ist, schließen Sie Terminal und öffnen Sie es erneut. Überprüfen Sie dann durch Eingabe von:
   ```
   claude --version
   ```
- Sie sollten die Versionsnummer von Claude Code sehen

**Alternative: Installation mit Homebrew**

Wenn Sie Homebrew verwenden, können Sie Claude Code damit installieren:
```
brew install --cask claude-code
```

**Tipp:** Führen Sie `claude doctor` nach der Installation aus, um zu prüfen, ob alles korrekt eingerichtet ist.

## Schritt 3: Mit Ihrem Anthropic-Konto verbinden

### Option A. Ihr Claude Pro- oder Max-Abonnement verwenden

- Geben Sie im Terminal ein:
   ```
   claude
   ```
- Claude versucht, einen Browser zu öffnen. Wenn er sich nicht automatisch öffnet, kopieren Sie die im Terminal angezeigte URL und fügen Sie sie in Ihren Browser ein.
- Melden Sie sich bei Ihrem Claude.ai-Konto an (dies kann automatisch geschehen)
- Klicken Sie auf **Authorize**
- Klicken Sie auf **Copy Code**, wenn ein langer Code erscheint
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

### Option C. OpenRouter API verwenden (kostenlos starten!)

OpenRouter ist ein einheitliches API-Gateway, das Zugang zu über 500 großen Sprachmodellen über einen einzigen API-Schlüssel bietet. Dies kann eine wirtschaftliche Möglichkeit sein, Claude Code zu nutzen, da Sie nur für die Nutzung bezahlen und aus Modellen verschiedener Preisklassen wählen können.

- Registrieren Sie sich auf [openrouter.ai](https://openrouter.ai) und melden Sie sich an
- Klicken Sie auf **Get API key** und kopieren Sie den Schlüssel an einen sicheren Ort
- Setzen Sie die erforderlichen Umgebungsvariablen, bevor Sie Claude Code starten:
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- Starten Sie Claude Code:
   ```
   claude
   ```
- Überprüfen Sie die Verbindung, indem Sie `/status` in Claude Code eingeben

**Hinweise:**
- Ersetzen Sie `your-openrouter-api-key` durch Ihren tatsächlichen OpenRouter-API-Schlüssel
- `ANTHROPIC_API_KEY` muss explizit auf leer gesetzt werden
- Um alternative Modelle zu verwenden, müssen diese **Tool-Nutzungsfähigkeiten** unterstützen. Sie können Modelle überschreiben mit:
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Durchsuchen Sie verfügbare Modelle auf [openrouter.ai/models](https://openrouter.ai/models)
- Das kostenlose Kontingent gibt Ihnen 50 API-Anfragen pro Tag
- Weitere Details finden Sie im [offiziellen OpenRouter-Leitfaden](https://openrouter.ai/docs/guides/claude-code-integration)


### Option D. Anthropic API über Azure Foundry verwenden

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

## Schritt 4: Claude Code testen

Sie sind fertig! So verwenden Sie Claude Code:

- Geben Sie im Terminal ein:
   ```
   claude
   ```
- Es stellt Ihnen einige Fragen, bevor es bereit ist zum Chatten
- Um zu testen, ob es funktioniert, stellen Sie eine allgemeine Frage wie „Erkläre mir Quantencomputing."

## Schritt 5: Zu Ihrem Projekt navigieren

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

## Schritt 6: Claude Code aktualisieren

Claude Code, das über den nativen Installer installiert wurde, aktualisiert sich automatisch im Hintergrund. Sie können ein Update auch manuell auslösen:

- Geben Sie im Terminal ein:
   ```
   sudo claude
   ```
- Claude Code prüft auf Updates und installiert die neueste Version

**Hinweis:** Homebrew-Installationen aktualisieren sich nicht automatisch. Führen Sie regelmäßig `brew upgrade claude-code` aus, um die neueste Version zu erhalten.

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

### Erster Schritt: Claude Doctor ausführen
Wenn etwas nicht funktioniert, führen Sie zuerst diesen Befehl aus:
```
claude doctor
```
Er überprüft Ihre Installation und meldet eventuelle Probleme.

### Installationsskript schlägt fehl
- Stellen Sie sicher, dass Sie macOS 13.0 oder neuer verwenden
- Versuchen Sie die Homebrew-Alternative: `brew install --cask claude-code`
- Überprüfen Sie Ihre Internetverbindung und versuchen Sie es erneut

### Claude Code-Befehle werden nicht gefunden
- Schließen Sie Terminal vollständig (klicken Sie auf **Terminal** in der Menüleiste, dann auf **Terminal beenden**)
- Öffnen Sie Terminal erneut
- Versuchen Sie `claude --version`, um zu prüfen, ob es installiert ist
- Versuchen Sie, den Installationsbefehl erneut auszuführen: `curl -fsSL https://claude.ai/install.sh | bash`

### Authentifizierung schlägt fehl
- Stellen Sie sicher, dass Sie ein aktives Claude Pro/Max-Abonnement oder einen gültigen API-Schlüssel haben
- Versuchen Sie, `claude` erneut auszuführen und den Anmeldevorgang abzuschließen
- Überprüfen Sie, ob Ihr Browser die richtige Autorisierungsseite geöffnet hat

## Tipps für Mac-Benutzer

### Projektpfade finden
Um den Pfad zu einem Ordner zu finden:
- Öffnen Sie den Finder
- Navigieren Sie zu Ihrem Projektordner
- Ziehen Sie den Ordner per Drag & Drop ins Terminal – der vollständige Pfad erscheint!

### Verschiedene Terminal-Apps verwenden
Sie können auch andere Terminal-Apps verwenden wie:
- iTerm2 (beliebte Alternative mit mehr Funktionen)
- Warp (modernes Terminal mit KI-Funktionen)
- Hyper (plattformübergreifendes Terminal)

Claude Code funktioniert mit allen!

## Benötigen Sie Hilfe?

- Für Claude Code-Probleme: [Claude Code GitHub](https://github.com/anthropics/claude-code)
- Für die offizielle Einrichtungsdokumentation: [Claude Code Setup-Anleitung](https://code.claude.com/docs/en/setup)

---

*Zuletzt aktualisiert: Februar 2026*
