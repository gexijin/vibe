[Startseite](./)

# Claude Code unter Windows installieren

Claude Code ist ein KI-Assistent, der in Ihrem Terminal lebt und Ihnen beim Schreiben, Debuggen und Verstehen von Code hilft. Mit dieser Anleitung läuft Claude Code in wenigen Minuten nativ unter Windows. WSL2 wird am Ende als optionale, fortgeschrittenere Einrichtung vorgestellt.

## Wichtige Konzepte

- **PowerShell** - Das integrierte Befehlszeilentool von Windows, das hier zum Installieren und Ausführen von Claude Code verwendet wird
- **Git for Windows** - Ein kostenloser Download, der **Git Bash** hinzufügt, die Shell, die Claude Code zum Ausführen von Befehlen verwendet
- **WSL (Windows Subsystem for Linux)** - Eine optionale Windows-Funktion, die ein echtes Linux-System neben Windows ausführt; wird in der fortgeschrittenen Einrichtung am Ende verwendet

## Was Sie benötigen

- Einen Windows 10- oder Windows 11-Computer
- Ein Claude Pro/Max-Abonnement oder einen API-Schlüssel
- 5 - 10 Minuten

## Schritt 1: Git for Windows installieren (optional, empfohlen)

Git for Windows ist **empfohlen, aber optional**. Es fügt **Git Bash** hinzu, die Shell, die Claude Code zum Ausführen von Befehlen verwendet. Wenn Sie ihn überspringen, greift Claude Code stattdessen auf PowerShell zurück – Sie können also direkt zu Schritt 2 wechseln und Git bei Bedarf später installieren.

- Gehen Sie zu [git-scm.com/download/win](https://git-scm.com/download/win)
- Der Download sollte automatisch starten – öffnen Sie das Installationsprogramm, wenn er fertig ist
- Klicken Sie sich mit **Next** durch das Installationsprogramm und übernehmen Sie die Standardoptionen
- Klicken Sie auf **Install** und dann auf **Finish**

Das war's – Claude Code erkennt Git Bash beim Start automatisch.

## Schritt 2: Claude Code installieren

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

## Schritt 3: Mit Ihrem Anthropic-Konto verbinden

### Option A. Ihr Claude Pro- oder Max-Abonnement verwenden

- Geben Sie im PowerShell-Fenster ein:
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

Die folgenden API-basierten Optionen laufen ebenfalls in **PowerShell** und nutzen den Befehl `setx`, der eine Einstellung dauerhaft speichert. **Schließen Sie PowerShell nach einem `setx` und öffnen Sie es erneut**, damit die Änderung wirksam wird, und starten Sie dann `claude`.

### Option B. Anthropic-API-Schlüssel verwenden

Wenn Sie einen Anthropic-API-Schlüssel anstelle eines Claude-Abonnements haben:

- Holen Sie sich Ihren API-Schlüssel von der [Anthropic Console](https://console.anthropic.com/)
- Geben Sie in PowerShell ein:
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
   Ersetzen Sie `your-api-key-here` durch Ihren tatsächlichen API-Schlüssel
- Schließen Sie PowerShell und öffnen Sie es erneut, damit die Änderung wirksam wird
- Starten Sie Claude Code:
   ```
   claude
   ```

### Option C. OpenRouter API verwenden (kostenlos starten!)

OpenRouter ist ein einheitliches API-Gateway, das über einen einzigen API-Schlüssel Zugang zu über 500 großen Sprachmodellen bietet. Das kann eine günstige Möglichkeit sein, Claude Code zu nutzen: Sie zahlen nur für die Nutzung und wählen aus Modellen verschiedener Preisklassen.

- Registrieren Sie sich auf [openrouter.ai](https://openrouter.ai) und melden Sie sich an
- Klicken Sie auf **Get API key** und kopieren Sie den Schlüssel an einen sicheren Ort
- Setzen Sie in PowerShell die erforderlichen Umgebungsvariablen:
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- Schließen Sie PowerShell und öffnen Sie es erneut, dann starten Sie Claude Code:
   ```
   claude
   ```
- Überprüfen Sie die Verbindung durch Eingabe von `/status` in Claude Code

**Hinweise:**
- Ersetzen Sie `your-openrouter-api-key` durch Ihren tatsächlichen OpenRouter API-Schlüssel
- `ANTHROPIC_API_KEY` muss explizit auf leer gesetzt werden
- Um andere Modelle zu verwenden, müssen diese **Tool-Nutzungsfähigkeiten** unterstützen. Sie können Modelle überschreiben mit:
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- Durchsuchen Sie verfügbare Modelle unter [openrouter.ai/models](https://openrouter.ai/models)
- Die kostenlose Stufe bietet 50 API-Anfragen pro Tag
- Weitere Details finden Sie im [offiziellen OpenRouter-Leitfaden](https://openrouter.ai/docs/guides/claude-code-integration)

### Option D. Anthropic API über Azure Foundry verwenden

Fügen Sie in PowerShell diesen Code ein, um die Umgebungsvariablen zu definieren:
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**Hinweis:** Ersetzen Sie `xxxx-eastus2` durch Ihren Foundry-Ressourcennamen (verwenden Sie nicht die gesamte Basis-URL). Ersetzen Sie `your_api_key` durch Ihren vollständigen API-Schlüssel aus Ihrem Azure-Portal.

Schließen Sie dann PowerShell, öffnen Sie es erneut und starten Sie Claude Code:
```
claude
```

Sie sollten nun Claude Code mit Azure-bereitgestellten Claude-Modellen verwenden können.

## Schritt 4: Claude Code testen

Sie sind fertig! Geben Sie `claude` in PowerShell ein und stellen Sie eine allgemeine Frage wie „Erkläre Quantencomputing".

## Schritt 5: Auf Ihre Projekte zugreifen

- Wenn Sie einen Projektordner haben, wechseln Sie in PowerShell dorthin:
   ```
   cd ~/Documents/test_claude
   ```
- Starten Sie dann Claude:
   ```
   claude
   ```
- Bitten Sie Claude zu Beginn, Ihnen die Codebasis zu erklären.
- Sie können Claude bitten, Änderungen vorzunehmen.
- Testen Sie Ihren Code in Ihrer bevorzugten IDE.

**Hinweis:** Claude arbeitet innerhalb eines Projektordners und speichert dort seine Einstellungen. Das ist sein Arbeitsbereich.

## Schritt 6: (Optional) WSL2 für die vollständige Linux-Erfahrung installieren

Für die meisten Nutzer reicht die native Einrichtung oben völlig aus. Claude Code läuft unter Linux jedoch besser. WSL2 führt ein echtes Linux-System innerhalb von Windows aus und bietet **Bash Tool Sandboxing** (eine Sicherheitsfunktion) sowie eine bessere Kompatibilität mit Linux-Toolchains. Die Einrichtung dauert länger und erfordert einen Neustart – tun Sie dies also nur, wenn Sie die vollständige Linux-Erfahrung möchten.

### a) Virtualisierung prüfen und WSL installieren

**Prüfen Sie zunächst, ob die Virtualisierung aktiviert ist:**

- **Klicken Sie mit der rechten Maustaste** auf die Taskleiste (die Leiste am unteren Bildschirmrand)
- Klicken Sie im Menü auf **Task-Manager**
- Wenn sich der Task-Manager in einem kleinen Fenster öffnet, klicken Sie unten auf **Mehr Details**
- Klicken Sie oben auf die Registerkarte **Leistung**
- Klicken Sie in der linken Seitenleiste auf **CPU**
- Suchen Sie die Zeile **Virtualisierung:** und prüfen Sie, ob dort **Aktiviert** steht

**Wenn dort „Deaktiviert" steht:** Sie müssen die Virtualisierung im BIOS Ihres Computers aktivieren:
- Starten Sie Ihren Computer neu
- Drücken Sie während des Starts die BIOS-Taste (normalerweise **F2**, **F10**, **Entf** oder **Esc**, je nach Computerhersteller)
- Suchen Sie nach Einstellungen zu „Virtualization Technology", „Intel VT-x", „AMD-V" oder „SVM Mode"
- Aktivieren Sie diese Einstellungen
- Speichern und verlassen Sie das BIOS (normalerweise **F10**)

**Jetzt WSL installieren:**

- Klicken Sie auf die **Windows-Starttaste** und geben Sie `PowerShell` ein
- **Klicken Sie mit der rechten Maustaste** auf **Windows PowerShell** und klicken Sie auf **Als Administrator ausführen**
- Klicken Sie auf **Ja**, wenn gefragt wird „Möchten Sie zulassen, dass diese App Änderungen an Ihrem Gerät vornimmt?"
- Geben Sie im PowerShell-Fenster ein:
   ```
   wsl --install
   ```
- Möglicherweise sehen Sie Meldungen wie „Installing: Windows Subsystem for Linux" und „Installing: Ubuntu"
- Wenn die Installation abgeschlossen ist, starten Sie Ihren Computer neu

**Hinweis:** `wsl --install` erfordert Windows 10 Version 2004 oder höher oder Windows 11. Wenn der Befehl nicht erkannt wird, ist Ihre Windows-Version möglicherweise zu alt.

### b) Ubuntu einrichten

Nach dem Neustart sollte innerhalb von 2-5 Minuten automatisch ein Terminalfenster mit „Ubuntu" im Titel erscheinen. Falls nicht, klicken Sie auf die **Windows-Starttaste**, geben Sie `Ubuntu` ein und klicken Sie auf die **Ubuntu**-App (orangefarbenes Kreissymbol).

- Warten Sie auf die Meldung: `Enter new UNIX username:`
- Geben Sie einen Benutzernamen ein (nur Kleinbuchstaben und Zahlen, keine Leerzeichen) – zum Beispiel `john`
- Sie sehen: `New password:`
- Geben Sie ein einfaches Passwort ein (Sie sehen die Zeichen beim Tippen nicht – das ist normal)
- Geben Sie dasselbe Passwort erneut ein, wenn Sie dazu aufgefordert werden

**Wichtig:** Merken Sie sich diesen Benutzernamen und das Passwort – Sie werden sie später brauchen.

### c) Claude Code in WSL installieren

- Geben Sie im Ubuntu-Terminal ein:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Überprüfen Sie durch Eingabe von:
   ```
   claude --version
   ```
- Verbinden Sie Ihr Konto, indem Sie `claude` im Ubuntu-Terminal eingeben und der Browser-Anmeldung folgen (wie in Schritt 3, Option A). Wenn Sie stattdessen einen API-Schlüssel verwenden, setzen Sie ihn mit `export ANTHROPIC_API_KEY="your-api-key-here"` (WSL verwendet Linux-Befehle, kein `setx`)
- Um einen Windows-Projektordner aus WSL zu öffnen:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Ersetzen Sie `Username` durch Ihren tatsächlichen Windows-Benutzernamen.

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
- Prüfen Sie im Task-Manager, ob die Virtualisierung aktiviert ist (siehe den optionalen WSL-Abschnitt oben)
- Wenn sie deaktiviert ist, aktivieren Sie sie im BIOS Ihres Computers
- Nach dem Aktivieren der Virtualisierung starten Sie Ihren Computer neu und versuchen Sie `wsl --install` erneut

### „wsl --install" funktioniert nicht
- Stellen Sie sicher, dass Sie PowerShell als Administrator ausführen
- Stellen Sie sicher, dass Sie Windows 10 Version 2004+ oder Windows 11 haben
- Führen Sie zuerst `wsl --update` aus, dann `wsl --install` erneut

### Ubuntu-Fenster öffnet sich nach dem Neustart nicht
- Klicken Sie auf die **Windows-Starttaste**, geben Sie `Ubuntu` ein und klicken Sie auf die **Ubuntu**-App, um sie manuell zu starten

## Benötigen Sie Hilfe?

- Für WSL-Probleme: [Microsoft WSL-Dokumentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Für Claude Code-Probleme: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2025. Aktualisiert Juni 2026.
