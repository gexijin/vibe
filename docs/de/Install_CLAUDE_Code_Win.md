[Startseite](./)

# Claude Code unter Windows installieren

Claude Code ist ein KI-Assistent, der in Ihrem Terminal lebt und Ihnen beim Schreiben, Debuggen und Verstehen von Code hilft. Diese Anleitung führt Sie durch die komplette Einrichtung: eine schnelle native Installation über PowerShell, dann WSL2 für die vollständige Linux-basierte Erfahrung.

## Wichtige Konzepte

- **WSL (Windows Subsystem for Linux)** - Eine Windows-Funktion, die ein echtes Linux-System neben Windows ausführt
- **Ubuntu** - Eine beliebte, einsteigerfreundliche Linux-Distribution, die Sie über WSL installieren können
- **PowerShell** - Das integrierte Befehlszeilentool von Windows, das hier zur Installation von Claude Code und WSL verwendet wird

## Was Sie benötigen

- Einen Windows 10 (Version 2004 oder höher) oder Windows 11 Computer
- Administratorzugang auf Ihrem Computer
- Claude Pro/Max-Abonnement oder API-Schlüssel über Azure Foundry
- 10 - 15 Minuten

## Schritt 1: Claude Code nativ unter Windows installieren (funktioniert, aber nicht empfohlen)

- Klicken Sie auf die **Windows-Starttaste**
- Geben Sie `PowerShell` ein und klicken Sie auf **Windows PowerShell**
- Geben Sie im PowerShell-Fenster ein:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Warten Sie, bis die Installation abgeschlossen ist
- Schließen Sie PowerShell und öffnen Sie es erneut, dann überprüfen Sie durch Eingabe von:
   ```
   claude --version
   ```
- Sie sollten die Versionsnummer von Claude Code sehen

> **Hinweis:** Die native Windows-Installation hat einige Einschränkungen:
> - Kein Bash Tool Sandboxing (eine Sicherheitsfunktion, die nur in WSL2/macOS verfügbar ist)
> - Einige Tools und Workflows funktionieren in einer Linux-Umgebung besser
>
> Fahren Sie mit den folgenden Schritten fort, um WSL2 für die vollständige Erfahrung zu installieren.

## Schritt 2: Virtualisierung prüfen und WSL installieren

**Prüfen Sie zunächst, ob die Virtualisierung aktiviert ist:**

- **Klicken Sie mit der rechten Maustaste** auf die Taskleiste (die Leiste am unteren Bildschirmrand)
- Klicken Sie im Menü auf **Task-Manager**
- Wenn sich der Task-Manager in einem kleinen Fenster öffnet, klicken Sie unten auf **Mehr Details**
- Klicken Sie oben auf die Registerkarte **Leistung**
- Klicken Sie in der linken Seitenleiste auf **CPU**
- Schauen Sie auf den unteren rechten Bereich des Fensters
- Suchen Sie die Zeile **Virtualisierung:** und prüfen Sie, ob dort **Aktiviert** steht

**Wenn dort „Aktiviert" steht:** Ausgezeichnet! Fahren Sie unten fort.

**Wenn dort „Deaktiviert" steht:** Sie müssen die Virtualisierung in den BIOS-Einstellungen Ihres Computers aktivieren:
- Starten Sie Ihren Computer neu
- Drücken Sie während des Starts die BIOS-Taste (normalerweise **F2**, **F10**, **Entf** oder **Esc** - es hängt von Ihrem Computerhersteller ab)
- Suchen Sie nach Einstellungen zu „Virtualization Technology", „Intel VT-x", „AMD-V" oder „SVM Mode"
- Aktivieren Sie diese Einstellungen
- Speichern und verlassen Sie das BIOS (normalerweise **F10**)
- Ihr Computer startet normal neu

**Jetzt WSL installieren:**

- Klicken Sie auf die **Windows-Starttaste**
- Geben Sie `PowerShell` in das Suchfeld ein
- **Klicken Sie mit der rechten Maustaste** auf **Windows PowerShell** und klicken Sie auf **Als Administrator ausführen**
- Klicken Sie auf **Ja**, wenn gefragt wird „Möchten Sie zulassen, dass diese App Änderungen an Ihrem Gerät vornimmt?"

**Prüfen Sie, ob WSL und Ubuntu bereits installiert sind:**

- Geben Sie im PowerShell-Fenster ein:
   ```
   wsl --list --verbose
   ```
- **Wenn Sie „Ubuntu" aufgelistet sehen:** WSL ist bereits installiert! Fahren Sie mit Schritt 3 fort.
- **Wenn Sie eine Fehlermeldung sehen:** Fahren Sie mit der Installation unten fort.

**Um WSL und Ubuntu zu installieren:**

- Geben Sie im PowerShell-Fenster ein:
   ```
   wsl --install
   ```
- Möglicherweise sehen Sie Meldungen wie „Installing: Windows Subsystem for Linux" und „Installing: Ubuntu"
- Wenn die Installation abgeschlossen ist, starten Sie Ihren Computer neu:
   - Klicken Sie auf die **Windows-Starttaste** → **Ein/Aus-Symbol** → **Neu starten**
- Ihr Computer wird neu gestartet - das dauert etwa 1-2 Minuten

**Hinweis:** Wenn Sie einen Fehler erhalten, dass der Befehl nicht erkannt wird, ist Ihre Windows-Version möglicherweise zu alt. Stellen Sie sicher, dass Sie Windows 10 Version 2004 oder höher oder Windows 11 haben.

## Schritt 3: Ubuntu einrichten

Nach dem Neustart Ihres Computers sollte innerhalb von 2-5 Minuten automatisch ein Terminalfenster mit „Ubuntu" im Titel erscheinen.

**Wenn sich das Ubuntu-Fenster NICHT automatisch geöffnet hat:**
- Klicken Sie auf die **Windows-Starttaste**
- Geben Sie `Ubuntu` in das Suchfeld ein
- Klicken Sie auf **Ubuntu** (Sie sehen ein kreisförmiges orangefarbenes Symbol)
- Das Ubuntu-Terminal öffnet sich und setzt die Einrichtung fort

**Schließen Sie nun die erstmalige Einrichtung ab:**

- Warten Sie auf die Meldung: `Enter new UNIX username:`
- Geben Sie einen Benutzernamen ein (verwenden Sie nur Kleinbuchstaben und Zahlen, keine Leerzeichen)
   - Beispiel: `john`
- Sie sehen: `New password:`
- Geben Sie ein einfaches Passwort ein (sogar dasselbe wie der Benutzername `john`)
- Sie sehen die Zeichen beim Tippen nicht - das ist normal
- Geben Sie dasselbe Passwort erneut ein, wenn Sie dazu aufgefordert werden

**Wichtig:** Merken Sie sich diesen Benutzernamen und das Passwort — Sie werden sie später brauchen.

## Schritt 4: Claude Code in WSL installieren

- Geben Sie im Ubuntu-Terminal ein:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Warten Sie, bis Claude Code installiert ist
- Wenn die Installation abgeschlossen ist, überprüfen Sie durch Eingabe von:
   ```
   claude --version
   ```
- Sie sollten die Versionsnummer von Claude Code sehen

## Schritt 5: Mit Ihrem Anthropic-Konto verbinden

### Option A. Ihr Claude Pro- oder Max-Abonnement verwenden

- Geben Sie im Ubuntu-Terminal ein:
   ```
   claude
   ```
- Claude versucht, einen Browser zu öffnen. Wenn er sich nicht automatisch öffnet, halten Sie **Strg** gedrückt und klicken Sie auf die lange URL, um sie in einem Browser zu öffnen. Alternativ kopieren Sie die URL und fügen Sie sie in einen externen Browser ein.
- Melden Sie sich bei Ihrem Claude.ai-Konto an (dies kann automatisch geschehen, wenn Sie Chrome verwenden)
- Klicken Sie auf **Authorize**
- Klicken Sie auf **Copy Code**, wenn ein langer Code erscheint
- Gehen Sie zurück zum Terminal-Fenster
- Zum Einfügen im Terminal: **Rechtsklick** und **Einfügen** wählen (oder **Strg+Umschalt+V** drücken)
- Sie sollten eine Erfolgsmeldung sehen
- Folgen Sie den Anweisungen, um die Einrichtung abzuschließen

### Option B. Anthropic-API-Schlüssel verwenden

Wenn Sie einen Anthropic-API-Schlüssel anstelle eines Claude-Abonnements haben:

- Holen Sie sich zunächst Ihren API-Schlüssel von der [Anthropic Console](https://console.anthropic.com/)
- Geben Sie im Ubuntu-Terminal ein:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Ersetzen Sie `your-api-key-here` durch Ihren tatsächlichen API-Schlüssel
- Um dies dauerhaft zu machen (damit Sie es nicht jedes Mal einstellen müssen), fügen Sie es zu Ihrem Shell-Profil hinzu:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   Ersetzen Sie `your-api-key-here` durch Ihren tatsächlichen API-Schlüssel
- Schließen Sie das Ubuntu-Terminal und öffnen Sie es erneut, damit die Änderungen wirksam werden
- Sie sollten nun Claude Code mit Ihrem API-Schlüssel verwenden können

### Option C. OpenRouter API verwenden (kostenlos starten!)

OpenRouter ist ein einheitliches API-Gateway, das über einen einzigen API-Schlüssel Zugang zu über 500 großen Sprachmodellen bietet. Dies kann eine wirtschaftliche Möglichkeit sein, Claude Code zu nutzen, da Sie nur für die Nutzung bezahlen und aus Modellen verschiedener Preisklassen wählen können.

- Registrieren Sie sich auf [openrouter.ai](https://openrouter.ai) und melden Sie sich an
- Klicken Sie auf **Get API key** und kopieren Sie den Schlüssel an einen sicheren Ort
- Setzen Sie die erforderlichen Umgebungsvariablen vor dem Start von Claude Code:
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
- Überprüfen Sie die Verbindung durch Eingabe von `/status` in Claude Code

**Hinweise:**
- Ersetzen Sie `your-openrouter-api-key` durch Ihren tatsächlichen OpenRouter API-Schlüssel
- `ANTHROPIC_API_KEY` muss explizit auf leer gesetzt werden
- Um alternative Modelle zu verwenden, müssen diese **Tool-Nutzungsfähigkeiten** unterstützen. Sie können Modelle überschreiben mit:
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Durchsuchen Sie verfügbare Modelle unter [openrouter.ai/models](https://openrouter.ai/models)
- Die kostenlose Stufe bietet 50 API-Anfragen pro Tag
- Weitere Details finden Sie im [offiziellen OpenRouter-Leitfaden](https://openrouter.ai/docs/guides/claude-code-integration)

### Option D. Anthropic API über Azure Foundry verwenden

Fügen Sie vor dem Starten von Claude Code im Ubuntu-Terminal diesen Code ein, um Umgebungsvariablen zu definieren:
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Hinweis:** Ersetzen Sie `xxxx-eastus2` durch Ihren Foundry-Ressourcennamen (verwenden Sie nicht die gesamte Basis-URL). Ersetzen Sie `your_api_key` durch Ihren vollständigen API-Schlüssel aus Ihrem Azure-Portal.

Starten Sie dann Claude Code:
```
claude
```

Sie sollten nun Claude Code mit Azure-bereitgestellten Claude-Modellen verwenden können.

## Schritt 6: Claude Code testen

Sie sind fertig! Geben Sie `claude` im Ubuntu-Terminal ein und stellen Sie eine allgemeine Frage wie „Erkläre Quantencomputing."

## Schritt 7: Auf Ihre Projekte zugreifen

**Natives Windows (PowerShell):**
- Wenn Sie einen Projektordner haben, navigieren Sie dorthin:
   ```
   cd ~/Documents/test_claude
   ```
- Starten Sie dann Claude:
   ```
   claude
   ```

**WSL (Ubuntu):**
- Wenn Sie einen Windows-Ordner namens `test_claude` haben, können Sie darauf zugreifen:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Ersetzen Sie `Username` durch Ihren tatsächlichen Windows-Benutzernamen.
- Starten Sie dann Claude:
   ```
   claude
   ```

- Beginnen Sie damit, Claude zu bitten, Ihnen die Codebasis zu erklären.
- Sie können Claude bitten, Änderungen vorzunehmen.
- Testen Sie Ihren Code in Ihrer bevorzugten IDE.

**Hinweis:** Claude arbeitet innerhalb eines Projektordners. Es speichert Einstellungen in diesem Ordner. Es ist Claudes Arbeitsbereich.

## Schritt 8: Claude Code aktualisieren

Claude Code aktualisiert sich automatisch, aber Sie können jederzeit manuell aktualisieren:

**WSL (Ubuntu):**
```
sudo claude update
```

**Natives Windows (PowerShell — als Administrator ausführen):**
```
claude update
```

## Nächste Schritte

- **VS Code einrichten**: Folgen Sie der Anleitung [VS Code Erste Schritte](VS_Code_Getting_Started), dann verbinden Sie es mit Claude Code mit [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)
- **Git-Grundlagen lernen**: Fügen Sie Versionskontrolle zu Ihren Projekten hinzu mit [Claude Code Git unter Windows](Claude_Code_Git_Windows)
- **Ein Projekt ausprobieren**: Arbeiten Sie durch [Eine Forschungsarbeit mit Claude Code schreiben](Writing_Research_Paper_Claude_Code), um Claude Code in Aktion zu sehen

## Fehlerbehebung

### Erster Schritt: Claude Doctor ausführen

Wenn etwas nicht funktioniert, versuchen Sie zuerst diesen Befehl:
```
claude doctor
```
Dieses integrierte Diagnosetool überprüft Ihre Installation und meldet häufige Probleme.

### Claude-Befehl nicht gefunden (natives Windows)

- Schließen Sie PowerShell und öffnen Sie es erneut
- Versuchen Sie, den Installationsbefehl erneut auszuführen:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Stellen Sie sicher, dass Ihr PATH das Claude-Installationsverzeichnis enthält

### „Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
Dieser Fehler bedeutet, dass die Virtualisierung nicht aktiviert ist:
- Gehen Sie zurück zu Schritt 2 und prüfen Sie im Task-Manager, ob die Virtualisierung aktiviert ist
- Wenn deaktiviert, müssen Sie sie im BIOS Ihres Computers aktivieren (siehe Schritt 2 für Anweisungen)
- Nach dem Aktivieren der Virtualisierung starten Sie Ihren Computer neu und versuchen Sie `wsl --install` erneut

### „wsl --install" funktioniert nicht
- Stellen Sie sicher, dass Sie PowerShell als Administrator ausführen
- Stellen Sie sicher, dass Sie Windows 10 Version 2004+ oder Windows 11 haben
- Versuchen Sie zuerst: `wsl --update`, dann versuchen Sie `wsl --install` erneut

### Ubuntu-Fenster öffnet sich nach dem Neustart nicht
- Klicken Sie auf Windows-Start
- Geben Sie `Ubuntu` ein
- Klicken Sie auf die Ubuntu-App, um sie manuell zu starten

### Ubuntu-Terminal nach dem Schließen wieder öffnen
- Klicken Sie auf die **Windows-Starttaste**, geben Sie `Ubuntu` ein und klicken Sie auf die **Ubuntu**-App (orangefarbenes Kreissymbol)

### Claude Code-Befehle werden nicht gefunden (WSL)
- Stellen Sie sicher, dass die Installation erfolgreich abgeschlossen wurde
- Versuchen Sie, das Ubuntu-Terminal zu schließen und erneut zu öffnen
- Versuchen Sie, den Installationsbefehl erneut auszuführen: `curl -fsSL https://claude.ai/install.sh | bash`

## Benötigen Sie Hilfe?

- Für WSL-Probleme: [Microsoft WSL-Dokumentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Für Claude Code-Probleme: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2025. Aktualisiert Februar 2026.
