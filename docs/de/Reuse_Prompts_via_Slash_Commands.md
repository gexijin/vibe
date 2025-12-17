[Startseite](./)

# Benutzerdefinierte Slash-Befehle erstellen

Sind Sie es leid, immer wieder dieselben detaillierten Prompts einzugeben? Benutzerdefinierte Slash-Befehle ermöglichen es Ihnen, komplexe Anweisungen als wiederverwendbare Shortcuts zu speichern. Wie das Erstellen von Tastaturkürzeln für Ihre häufigsten Aufgaben verwandeln Slash-Befehle lange Prompts in einfache Befehle wie `/stock-report Apple`, die sofort umfassende Berichte generieren.

Das Beste daran? Wir verwenden Claude, um den detaillierten Prompt zu schreiben und den Skill zu erstellen. Ja, Claude ist sehr gut darin, sich...selbst zu prompten.

## Wichtige Konzepte

- **Slash-Befehl** - Ein wiederverwendbarer Prompt, der als Markdown-Datei gespeichert ist und den Claude Code ausführt, wenn Sie `/befehl-name` eingeben
- **Argumente** - Variablen, die Sie an Befehle übergeben (wie Aktienticker), mit dem speziellen Schlüsselwort `$ARGUMENTS`
- **`.claude/commands/`-Ordner** - Wo Claude Code Ihre benutzerdefinierten Befehle automatisch entdeckt und lädt

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code in VS Code unter Windows](./Claude_Code_in_VS_Code_Win.md) oder [Claude Code in VS Code auf dem Mac](./Claude_Code_in_VS_Code_Mac.md)
- Ein Thema zur Recherche (wir verwenden Aktienberichte als Beispiel)
- Ein Texteditor wie VS Code installiert
- 15-20 Minuten

## Schritt 1: Einen Projektordner erstellen

**Windows (WSL):**
- Öffnen Sie **Ubuntu** aus dem Startmenü
- Geben Sie diese Befehle ein:
  ```bash
  cd /mnt/c/Users/IHR_BENUTZERNAME/Documents
  mkdir test_claude
  cd test_claude
   ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren Windows-Benutzernamen

**Mac:**
- Öffnen Sie **Terminal** (finden Sie es unter Programme > Dienstprogramme)
- Geben Sie diese Befehle ein:
  ```bash
  cd ~/Documents
  mkdir test_claude
  cd test_claude
  ```

## Schritt 2: Claude Code starten

**Windows (WSL):**
- Noch im Ubuntu-Terminal, geben Sie ein:
  ```
  claude
  ```

**Mac:**
- Noch im Terminal, geben Sie ein:
  ```
  claude
  ```

Claude Code startet und zeigt eine Willkommensnachricht an.

## Schritt 3: Claude bitten, einen Slash-Befehl zu erstellen

Anstatt Dateien manuell zu erstellen, lassen Sie Claude die Arbeit machen. Geben Sie diesen Prompt ein:

```
Erstelle einen Slash-Befehl namens stock-report, der Berichte über die jüngsten Entwicklungen eines Unternehmens generiert, das über Name oder Ticker-Symbol identifiziert wird.
Beinhalte:
- Produkt- oder Serviceneuigkeiten
- Neuigkeiten zum Managementteam
- Aktuelle Finanzberichte
- Analystenberichte
```
Wenn Sie gefragt werden, erteilen Sie Claude die Erlaubnis, die Datei zu erstellen.
Claude erstellt einen detaillierten Prompt und speichert ihn als `stock-report.md` im `.claude/commands/`-Ordner.

**Hinweis:** Wir verwenden durchgehend das Markdown-Format: in Prompts, Berichten und Slash-Befehlen. Markdown ist KI-freundlich und kann leicht als einfache Textdateien bearbeitet werden.

## Schritt 4: Den Befehl überprüfen

Verwenden Sie einen beliebigen Texteditor, um die Datei `stock-report.md` aus dem `.claude/commands/`-Ordner zu öffnen. Das ist der Prompt für den Slash-Befehl.

Wenn Sie VS Code installiert haben (empfohlen):
- Starten Sie VS Code
- Wählen Sie unter **File** die Option **Open folder** und wählen Sie den Projektordner `Documents/test_claude`
- Navigieren Sie im Datei-Explorer zu `.claude/commands` und klicken Sie auf die Datei `stock-report.md`, um sie zu öffnen

Überprüfen Sie den Prompt und nehmen Sie bei Bedarf Änderungen an den Anweisungen vor.

**Hinweis:** Claude ist unglaublich gut darin, Prompts zu schreiben. Sie können sehen, dass sein Prompt im Markdown-Format gut strukturiert und klar geschrieben ist. Lernen Sie, Prompts so zu schreiben. Manchmal enthält er sogar Anweisungen, bei Unklarheiten nachzufragen.

## Schritt 5: Den Befehl testen

**Beenden** Sie zuerst die aktuelle Claude Code-Sitzung, indem Sie zweimal **Strg+C** drücken. Starten Sie dann Claude neu, damit der neue Slash-Befehl geladen wird:
  ```
  claude
  ```
Testen Sie jetzt Ihren neuen Befehl mit einem echten Aktienticker:

```
/stock-report Apple
```

Claude durchsucht das Web und generiert einen umfassenden Bericht über Apple Inc. Dies kann 1-2 Minuten dauern.

## Schritt 6: Den generierten Bericht überprüfen

Claude erstellt einen Bericht in der Kommandozeile. Überprüfen Sie die Ausgabe:

- Prüfen Sie, ob jeder Abschnitt relevante, aktuelle Informationen enthält
- Verifizieren Sie, dass die Quellen glaubwürdig und aktuell sind
- Beachten Sie, wie Claude die Informationen organisiert hat

## Schritt 7: Bericht in Datei speichern

Lassen Sie uns den Slash-Befehl so modifizieren, dass Berichte automatisch als Markdown-Dateien gespeichert werden. Fügen Sie dies manuell zur Slash-Befehl-Markdown-Datei hinzu.

- Öffnen Sie die Datei `stock-report.md` aus dem `.claude/commands/`-Ordner
- Fügen Sie dies am Ende hinzu.
  ```
  Speichere den Bericht als Markdown-Datei. Der Dateiname enthält Firmenname und Datum.
  ```
- Speichern Sie die Datei.

## Schritt 8: Befehl erneut ausführen

- **Beenden** Sie zuerst die aktuelle Claude Code-Sitzung, indem Sie zweimal **Strg+C** drücken. Starten Sie dann Claude neu, damit der neue Slash-Befehl geladen wird:
  ```
  claude
  ```
- Testen Sie jetzt Ihren neuen Befehl mit einem echten Aktienticker:

  ```
  /stock-report AAPL
  ```
- Öffnen Sie den Bericht

Claude generiert den Bericht und speichert ihn als Markdown-Datei mit einem Namen wie `Apple_2025-12-13.md`. Klicken Sie auf die Datei in VS Code, um sie anzuzeigen.

## Schritt 9: Den Befehl über Claude ändern

Sie können Claude bitten, die Slash-Befehle zu bearbeiten:

```
Überarbeite den stock-report Slash-Befehl, um den Bericht als HTML-Datei zu speichern.
```

Claude aktualisiert die Befehlsdatei. Sie können dies im Editor überprüfen.

## Schritt 10: Den aktualisierten Befehl testen

- **Beenden** Sie zuerst die aktuelle Claude Code-Sitzung, indem Sie zweimal **Strg+C** drücken. Starten Sie dann Claude neu, damit der neue Slash-Befehl geladen wird:
  ```
  claude
  ```

- Testen Sie den erweiterten Befehl:

  ```
  /stock-report AAPL
  ```

Claude erstellt eine Datei mit einem Namen wie `Apple_2025-12-13.html`. Klicken Sie auf diese Datei im Datei-Explorer unter Windows oder Mac, um sie in Ihrem Standardbrowser zu öffnen.

## Schritt 11: Slash-Befehl wiederverwenden (Optional)

Das Schlüsselwort `$ARGUMENTS` in Ihrem Slash-Befehl fungiert als Platzhalter. Wenn Sie `/stock-report AAPL` eingeben, ersetzt Claude `$ARGUMENTS` durch `AAPL`, bevor der Prompt ausgeführt wird.

Versuchen Sie einen anderen Ticker:

```
/stock-report TSLA
```

Dieselbe Befehlsstruktur recherchiert jetzt Tesla stattdessen.

## Schritt 12: Einen anderen Slash-Befehl ausprobieren (Optional)

Wenn Sie das Tutorial [Eine Forschungsarbeit schreiben](./Writing_Research_Paper_Claude_Code.md) abgeschlossen haben, sollten Sie einen `/research-paper`-Befehl haben. Testen Sie ihn mit einem neuen Thema.

Löschen Sie zuerst Claudes Gedächtnis, um frisch zu beginnen:

```
/clear
```

Führen Sie dann den Research-Paper-Befehl aus:

```
/research-paper AI in schools
```

Zwei Hauptunterschiede:
- /research-paper wurde am Ende einer Sitzung erstellt, indem menschliche Interaktion erfasst wurde, während /stock-report von Grund auf neu erstellt wurde.
- /research-paper fragt interaktiv nach Eingaben, bevor es eine Arbeit entwirft.

## Nächste Schritte

Jetzt, da Sie Slash-Befehle verstehen, erstellen Sie mehr benutzerdefinierte Befehle für Ihre Workflows:

- **Code-Review:** `/review-code` - Code auf Fehler und Verbesserungen analysieren
- **Meeting-Notizen:** `/meeting-summary` - Strukturierte Meeting-Zusammenfassungen generieren
- **E-Mail-Entwürfe:** `/email-reply` - Professionelle E-Mail-Antworten erstellen

## Fehlerbehebung

- **Befehl nicht gefunden:** Starten Sie Claude Code neu, um Befehle aus `.claude/commands/` neu zu laden
- **Argumente funktionieren nicht:** Prüfen Sie, ob `$ARGUMENTS` in der Befehlsdatei korrekt geschrieben ist (Groß-/Kleinschreibung beachten)
- **Bericht unvollständig:** Bitten Sie Claude fortzufahren oder "füge mehr Details zum [Abschnittsname]-Abschnitt hinzu"

## Workflow-Überblick

- **Benutzerdefinierte Slash-Befehle** sparen Zeit, indem sie komplexe Prompts in einfache Shortcuts verwandeln
- **Argumente** machen Befehle flexibel für verschiedene Eingaben (Aktienticker, Themen, Dateien)
- **Claude erstellt Befehle** - Sie müssen keine Markdown-Dateien manuell schreiben; beschreiben Sie einfach, was Sie wollen
- **Befehle sind wiederverwendbar** - Einmal erstellt, verwenden Sie sie in verschiedenen Projekten und Sitzungen
- **Befehle kombinieren** - Bauen Sie eine Bibliothek spezialisierter Befehle für verschiedene Aufgaben auf

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 13. Dezember 2025.
