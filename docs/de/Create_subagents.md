[Startseite](./)

# Einen Subagenten in Claude Code erstellen

Sie möchten Investitionsmöglichkeiten vergleichen, aber die Recherche mehrerer Unternehmen und deren Bewertung dauert Stunden. Stellen Sie sich einen Subagenten wie die Einstellung eines Finanzanalysten vor, der genau weiß, wie er Ihre Recherche-Tools verwendet – Sie geben ihm Firmennamen, und er sammelt Berichte, bewertet jedes Unternehmen über wichtige Kennzahlen hinweg und empfiehlt die beste Investition. Sobald Sie lernen, Subagenten zu erstellen, können Sie jeden repetitiven mehrstufigen Workflow in Ihrer Arbeit automatisieren. Dieses Tutorial zeigt Ihnen, wie Sie diesen Analysten bauen.

## Wichtige Konzepte

- **Subagent** - Ein spezialisierter KI-Arbeiter mit eigenem Ziel, System-Prompt und Tools, der Aufgaben autonom erledigt
- **Skill** - Eine wiederverwendbare Fähigkeit (wie das Generieren von Aktienberichten), die Subagenten aufrufen können, um ihre Ziele zu erreichen
- **System-Prompt** - Anweisungen, die definieren, was der Subagent tut, wie er Unternehmen bewertet und welches Format er zurückgibt
- **Separation of Concerns** - Skills sammeln Daten; Subagenten verwenden diese Daten, um Entscheidungen zu treffen

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code in VS Code unter Windows](./Claude_Code_in_VS_Code_Win.md) oder [Claude Code in VS Code auf dem Mac](./Claude_Code_in_VS_Code_Mac.md)
- Der Aktienberichts-Skill bereits installiert (in `.claude/skills/generate-stock-reports/`)
- VS Code oder einen anderen Texteditor
- 20-25 Minuten

## Schritt 1: Einen Projektordner erstellen und Claude Code starten

**Windows (WSL):**
- Öffnen Sie **Ubuntu** aus dem Startmenü
- Geben Sie diese Befehle ein:
  ```bash
  cd /mnt/c/Users/IHR_BENUTZERNAME/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren Windows-Benutzernamen
- Starten Sie Claude Code:
  ```
  claude
  ```

**Mac:**
- Öffnen Sie **Terminal** (finden Sie es unter Programme > Dienstprogramme)
- Geben Sie diese Befehle ein:
  ```bash
  cd ~/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
- Starten Sie Claude Code:
  ```
  claude
  ```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im Installations-Tutorial beschrieben ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Nach der Anmeldung sehen Sie eine Willkommensnachricht und die Claude Code-Eingabeaufforderung.

## Schritt 2: Überprüfen, ob der Aktienberichts-Skill existiert

Bevor Sie Ihren Subagenten bauen, bestätigen Sie, dass der Skill verfügbar ist. Geben Sie ein:

```
Liste alle verfügbaren Skills auf
```

Sie sollten `generate-stock-reports` in der Ausgabe sehen. Dieser Skill recherchiert Unternehmen und generiert Berichte über Produktneuigkeiten, Management-Updates, finanzielle Leistung und Analystenmeinungen.

Wenn Sie ihn nicht sehen, sollten die Skill-Dateien in `.claude/skills/generate-stock-reports/` (Projektebene) sein.

## Schritt 3: Die Subagent vs Skill-Architektur verstehen

So arbeiten Subagenten und Skills zusammen:

| Komponente | Zweck | Beispiel |
|-----------|---------|---------|
| **Skill** | Sammelt Rohdaten über ein Unternehmen | „Generiere Bericht für Apple: Produkte, Finanzen, Management, Analysten" |
| **Subagent** | Verwendet Skill-Daten, um ein Ziel zu erreichen | „Hole Berichte für Apple und Microsoft, bewerte beide, empfehle in welches investiert werden soll" |

**Wichtiger Unterschied:**
- **Skill = Tool**, das Recherche durchführt
- **Subagent = Entscheidungsträger**, der das Tool verwendet und Logik anwendet

Ihr Stock-Picker-Subagent wird:
1. Den Aktienberichts-Skill für jedes Unternehmen aufrufen (2+ mal)
2. Unternehmen über Kategorien hinweg bewerten (Finanzen, Wachstum, Management, Stimmung)
3. Punktzahlen vergleichen und die beste Investition empfehlen

## Schritt 4: Den Stock Picker Subagenten erstellen

Geben Sie diesen Befehl ein:

```
/agents
```

Sie sehen die Claude Code Agenten-Oberfläche, die bestehende Subagenten (falls vorhanden) und Optionen zum **Erstellen**, **Bearbeiten** oder **Löschen** von Subagenten zeigt.

Erstellen Sie jetzt Ihren Subagenten:
- Wählen Sie **Create new subagent**
- Wählen Sie **Project**
- Wählen Sie **Generate with Claude (recommended)**
- Fügen Sie Folgendes als Anweisungen ein:
  ```
  Erstelle eine Markdown-Datei für einen neuen Subagenten namens stock-picker:
  - Er nimmt zwei oder mehr Aktien entgegen
  - Verwendet den generate-stock-reports Skill zur Recherche
  - Scorecards werden basierend auf den gesammelten Datenkategorien erstellt
  - Eine abschließende Empfehlung wird gegeben.
  ```
- Drücken Sie **Enter** auf **[Continue]**, um **All tools** zu verwenden
- Wählen Sie **Sonnet** als Modell
- Drücken Sie **Enter**, um zufällig eine Farbe auszuwählen

## Schritt 5: Überprüfen, was Sie gebaut haben (Reflexions-Checkpoint)

Um die Datei in VS Code zu öffnen, klicken Sie auf **File > Open File...** und navigieren Sie zu `.claude/agents/stock-picker.md`.

Oder Sie können Claude bitten:
```
Zeige mir die stock-picker Subagenten-Datei.
```
Claude zeigt die Subagenten-Datei an, die sich unter `.claude/agents/stock-picker.md` befindet. Sie sehen:

Es gibt ein **YAML-Frontmatter** oben:
```
---
name: stock-picker
description: Compares multiple companies for investment decisions...
skills: generate-stock-reports
---
```

Dieses Frontmatter (der Abschnitt zwischen den `---`-Markierungen) sagt Claude Code, wann dieser Subagent aktiviert werden soll und welche Skills er verwenden kann.

Es gibt einen **System-Prompt** unter dem Frontmatter mit Ihrer Bewertungsmethodik.

**Bestätigen Sie diese Schlüsselelemente:**
- Subagent hat Zugriff auf den `generate-stock-reports` Skill
- System-Prompt erklärt die Bewertungsaufschlüsselung
- Ziel des Subagenten ist klar: Unternehmen vergleichen und eines empfehlen

Sie können die Datei direkt bearbeiten oder Claude bitten, sie zu aktualisieren.

## Schritt 6: Den Subagenten testen

Testen Sie jetzt Ihren Subagenten mit einem echten Vergleich. Geben Sie ein:

```
Was ist die bessere Investition: Apple oder Google?
```

Der Subagent aktiviert sich automatisch basierend auf Ihrer Beschreibung.

## Schritt 7: Den Subagenten bei der Arbeit beobachten

Während der Subagent läuft, sehen Sie ihn:
1. **Den Skill zweimal aufrufen** - Den generate-stock-reports Skill einmal für Apple aufrufen, dann für Google
2. **Daten sammeln** - Jeder Skill-Aufruf durchsucht das Web und generiert einen Unternehmensbericht
3. **Unternehmen bewerten** - Wendet die 40/30/20/10-Gewichtung über Kategorien an
4. **Ausgabe generieren** - Erstellt Vergleichstabelle und Empfehlung

Dies kann 2-3 Minuten dauern, da Webrecherche involviert ist.

## Schritt 8: Die Ausgabe überprüfen

Der Subagent gibt eine detaillierte Analyse zurück, die Folgendes enthält:
- **Einzelne Unternehmensberichte** - Produktupdates, Finanzkennzahlen, Managementänderungen, Analystenstimmung für jede Aktie
- **Vergleichs-Scorecard** - Numerische Bewertungen über Kategorien hinweg (Finanzielle Gesundheit, Wachstumspotenzial, Managementqualität, Marktstimmung)
- **Endgültige Empfehlung** - In welche Aktie investiert werden soll und warum

Der Subagent zeigt dies möglicherweise im Terminal an oder generiert eine Markdown-Datei mit dem vollständigen Bericht. Sie können die Subagenten-Datei bearbeiten, um Bewertungsgewichte oder das Ausgabeformat anzupassen.

## Nächste Schritte

Jetzt, da Sie einen funktionierenden Stock-Picker-Subagenten haben, versuchen Sie diese Erweiterungen:

- **3+ Aktien vergleichen**: „Vergleiche AAPL, MSFT und GOOGL", um zu sehen, wie der Subagent mehr Optionen handhabt
- **Bewertungsgewichte anpassen**: Bearbeiten Sie die Subagenten-Datei, um die 40/30/20/10-Aufschlüsselung zu ändern (z.B. machen Sie Wachstum zu 40%, wenn Sie Wachstumsaktien bevorzugen)
- **Andere Subagenten erstellen**: Bauen Sie einen „code-reviewer" Subagenten, „bug-hunter" Subagenten oder „document-writer" Subagenten für verschiedene Aufgaben

## Fehlerbehebung

- **Subagent aktiviert sich nicht**: Stellen Sie sicher, dass Ihre Anfrage das Vergleichen von Unternehmen oder Investitionsentscheidungen erwähnt. Versuchen Sie: „Verwende den stock-picker Subagenten zum Vergleich..."
- **Skill nicht gefunden**: Überprüfen Sie, ob `.claude/skills/generate-stock-reports/SKILL.md` existiert. Starten Sie Claude Code neu, wenn Sie ihn gerade hinzugefügt haben.
- **Unvollständige Bewertungen**: Bitten Sie den Subagenten, „weiterzumachen" oder „die Bewertungen für jede Kategorie detaillierter zu erklären"
- **Fehler beim Erstellen des Subagenten**: Überprüfen Sie, ob der `.claude/agents/`-Ordner existiert. Claude Code sollte ihn automatisch erstellen.

## Workflow-Überblick

- **Subagenten automatisieren mehrstufige Workflows** - Sie orchestrieren Skills, wenden Logik an und liefern Entscheidungen
- **Skills sind wiederverwendbare Tools** - Ein Skill kann von mehreren Subagenten für verschiedene Ziele verwendet werden
- **System-Prompts definieren Verhalten** - Klare Anweisungen und Bewertungskriterien machen Subagenten zuverlässig
- **Subagenten behalten Fokus** - Jeder Subagent hat einen einzigen, klaren Zweck (Aktienauswahl, Code-Review, usw.)
- **Komposition skaliert** - Bauen Sie eine Bibliothek von Skills und Subagenten, die zusammenarbeiten

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 14. Dezember 2025.
