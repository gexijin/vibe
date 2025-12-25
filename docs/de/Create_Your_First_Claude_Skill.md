[Startseite](./)

# Ihren ersten Claude Skill erstellen

Sie haben manuell `/stock-report AAPL` eingegeben, um Berichte zu generieren. Was wäre, wenn Claude automatisch entscheiden könnte, wann es einen Aktienbericht erstellen soll, basierend auf Ihrer Konversation? Das ist die Kraft von Skills – wie ein Upgrade von manuellem Schalten zu einem Automatikgetriebe, das bei Bedarf schaltet.

## Wichtige Konzepte

- **Skill** - Eine modell-aufgerufene Fähigkeit, die in `.claude/skills/` gespeichert ist und die Claude automatisch basierend auf dem Kontext aktiviert
- **Modell-aufgerufen** - Claude entscheidet, wann der Skill verwendet werden soll, indem es seine Beschreibung liest, ohne dass Sie einen Befehl eingeben
- **SKILL.md** - Die Hauptdatei, die YAML-Frontmatter (Metadaten) und Anweisungen für Claude enthält

## Was Sie benötigen

- Abgeschlossenes Tutorial [Benutzerdefinierte Slash-Befehle erstellen](./Reuse_Prompts_via_Slash_Commands.md)
- Der `stock-report` Slash-Befehl aus diesem Tutorial
- VS Code installiert
- 10-15 Minuten

## Schritt 1: Zum Projektordner navigieren

**Windows (WSL):**
- Öffnen Sie **Ubuntu** aus dem Startmenü
- Geben Sie ein:
  ```bash
  cd /mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude
  ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren Windows-Benutzernamen

  Wenn der Ordner nicht existiert, erstellen Sie ihn zuerst:
  ```bash
  mkdir -p /mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude
  cd /mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude
  ```

**Mac:**
- Öffnen Sie **Terminal** (Programme > Dienstprogramme)
- Geben Sie ein:
  ```bash
  cd ~/Documents/test_claude
  ```

  Wenn der Ordner nicht existiert, erstellen Sie ihn zuerst:
  ```bash
  mkdir -p ~/Documents/test_claude
  cd ~/Documents/test_claude
  ```

## Schritt 2: Claude Code starten

Geben Sie ein:
```
claude
```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im Installations-Tutorial beschrieben ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Nach der Anmeldung sehen Sie eine Willkommensnachricht und die Claude Code-Eingabeaufforderung.

## Schritt 3: Auto-Genehmigung für Bearbeitungen aktivieren

Drücken Sie `Strg+E` (Windows/Linux) oder `Cmd+E` (Mac), um den Auto-Genehmigungsmodus für Bearbeitungen zu aktivieren.

Dies ermöglicht Claude, Dateien zu erstellen und zu ändern, ohne jedes Mal um Erlaubnis zu fragen.

## Schritt 4: Claude bitten, den Slash-Befehl zu konvertieren

Geben Sie diesen Prompt ein:
```
Konvertiere meinen stock-report Slash-Befehl in einen Skill namens generate-stock-reports.
Der Skill soll sich automatisch aktivieren, wenn ich nach Unternehmen oder Aktien frage.
```

Claude analysiert Ihren bestehenden Slash-Befehl und konvertiert ihn in einen Skill in `.claude/skills/stock-report/`.

**Was passiert:** Claude erstellt eine neue Ordnerstruktur mit `SKILL.md`, die YAML-Frontmatter enthält, das Claude sagt, wann dieser Skill automatisch verwendet werden soll.

## Schritt 5: Die Skill-Struktur überprüfen

Öffnen Sie VS Code und sehen Sie sich das Projekt an:
- Klicken Sie auf **File > Open Folder**
- Wählen Sie `Documents/test_claude`
- Navigieren Sie im Datei-Explorer zu `.claude/skills/stock-report/`
- Klicken Sie auf `SKILL.md`, um sie zu öffnen

Beachten Sie die Struktur:
```yaml
---
name: stock-report
description: Generates reports on companies... Use when users ask about stocks, companies, or ticker symbols.
---

[Rest der Anweisungen]
```

Das `description`-Feld ist der Schlüssel – es sagt Claude genau, wann dieser Skill automatisch aktiviert werden soll.

## Schritt 6: Den Skill testen (ohne einen Befehl einzugeben)

Anstatt `/stock-report AAPL` einzugeben, stellen Sie einfach eine natürliche Frage:
```
Was macht Apple in letzter Zeit?
```

**Der wichtige Unterschied:** Sie haben keinen Befehl eingegeben. Claude liest Ihre Frage, erkennt, dass Sie nach einem Unternehmen fragen, prüft die Skill-Beschreibungen und entscheidet automatisch, den stock-report Skill zu verwenden.

Beobachten Sie Claude bei der Arbeit – es sollte denselben umfassenden Bericht generieren, den Sie zuvor gesehen haben.

## Schritt 7: Die beiden Ansätze vergleichen

**Slash-Befehl (Manuell):**
```
/stock-report AAPL
```
- Sie sagen Claude explizit, was es tun soll
- Jedes Mal gleich
- Gut für wiederholte, vorhersehbare Aufgaben

**Skill (Automatisch):**
```
Erzähle mir über Teslas neueste Entwicklungen
```
oder
```
Ich denke darüber nach, in Microsoft zu investieren
```
oder
```
Was macht NVIDIA so?
```
- Claude entscheidet, ob der Skill verwendet werden soll
- Natürlichere Konversation
- Gut für komplexe Workflows, die Claude für Sie verwaltet

## Schritt 8: Grenzfälle testen

Versuchen Sie Fragen, die den Aktienberichts-Skill NICHT auslösen sollten:
```
Wie installiere ich Python?
```

Claude antwortet normal, ohne den Skill aufzurufen.

Versuchen Sie jetzt eine Frage, die ihn auslösen SOLLTE:
```
Vergleiche Google und Meta
```

Claude sollte den Skill zweimal verwenden – einmal für Google, einmal für Meta.

## Schritt 9: Die Skill-Beschreibung ändern (Optional)

Lassen Sie uns den Skill selektiver machen. Bitten Sie Claude:
```
Aktualisiere den stock-report Skill so, dass er sich nur aktiviert, wenn ich explizit
"analysiere" oder "Bericht" zusammen mit einem Unternehmensnamen erwähne.
```

Claude aktualisiert das `description`-Feld in `SKILL.md`. Testen Sie den Unterschied:
```
Was macht Apple so?
```
(Löst den Skill jetzt möglicherweise nicht aus)

```
Analysiere Apple
```
(Sollte den Skill auslösen)

## Nächste Schritte

Jetzt, da Sie Skills verstehen, erstellen Sie mehr für Ihre Workflows:

- **Recherche-Skill** - Aktiviert sich automatisch, wenn Sie Fragen stellen, die Webrecherche erfordern
- **Code-Review-Skill** - Aktiviert sich, wenn Sie Bugs, Probleme oder Code-Probleme erwähnen
- **Meeting-Notizen-Skill** - Aktiviert sich, wenn Sie Meeting-Transkripte einfügen oder Zusammenfassungen erwähnen

Das Muster: Definieren Sie, wann Claude automatisch helfen soll, nicht nur Shortcuts, die Sie manuell auslösen.

## Fehlerbehebung

- **Skill aktiviert sich nicht:** Überprüfen Sie das `description`-Feld in `SKILL.md` – es muss Auslösewörter enthalten, die mit Ihrer Frage zusammenhängen
- **Skill aktiviert sich zu oft:** Machen Sie die Beschreibung spezifischer darüber, wann er verwendet werden soll
- **Skill-Ordner nicht gefunden:** Skills befinden sich in `.claude/skills/` (versteckter Ordner – aktivieren Sie „Versteckte Dateien anzeigen" in Ihrem Datei-Explorer)
- **Änderungen an SKILL.md funktionieren nicht:** Skills werden automatisch geladen, wenn sie geändert werden – kein Neustart nötig. Wenn es immer noch nicht funktioniert, überprüfen Sie die YAML-Formatierung

## Workflow-Überblick

- **Slash-Befehle** sind Shortcuts, die Sie manuell eingeben (wie Lesezeichen)
- **Skills** sind Fähigkeiten, die Claude entdeckt und automatisch verwendet (wie ein Assistent, der Ihre Präferenzen kennt)
- **Skill-Beschreibungen** fungieren als Anweisungen, die Claude sagen: „Verwende mich, wenn der Benutzer X sagt"
- **Beide können koexistieren** - Verwenden Sie Slash-Befehle für schnelle, repetitive Aufgaben; verwenden Sie Skills für komplexe Workflows
- **Skills skalieren besser** - Sie müssen sich keine Befehlsnamen merken; Claude entscheidet basierend auf dem Kontext

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 13. Dezember 2025.
