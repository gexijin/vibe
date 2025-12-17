[Startseite](./)

# Einen Claude Skill für medizinische Forschung erstellen

Mit der medizinischen Forschung Schritt zu halten bedeutet, sich durch dichte wissenschaftliche Arbeiten voller Fachjargon zu kämpfen. Ein Claude Skill ist wie ein Forschungsassistent, der Hunderte von Artikeln liest und sie in einfachem Deutsch erklärt – anstatt Stunden damit zu verbringen, PubMed zu durchsuchen und Fachsprache zu entschlüsseln, stellen Sie eine einfache Frage und erhalten eine klare Zusammenfassung basierend auf der neuesten Wissenschaft.

In diesem Tutorial erstellen Sie einen Claude Skill, der peer-reviewte medizinische Literatur durchsucht. Wir erstellen zuerst ein Python-Skript, das PubMed abfragt. Das Beste daran? Sie können Claude bitten, die ganze Arbeit zu erledigen! Es hat einen Skill, der Skills erstellt!

## Wichtige Konzepte

- **Claude Skill** - Ein spezialisiertes Tool, das die Fähigkeiten von Claude Code mit benutzerdefinierten Anweisungen, Code und Dokumentation erweitert, gespeichert in `.claude/skills/`
- **PubMed** - Kostenlose Datenbank mit 35+ Millionen biomedizinischen Forschungsarbeiten, gepflegt von der US National Library of Medicine
- **Biopython** - Python-Bibliothek, die Tools zur programmgesteuerten Abfrage der PubMed-Datenbank bereitstellt
- **Auto-Edit-Modus** - Funktion, die mit Shift+Tab aktiviert wird und Claude erlaubt, mehrere Dateiänderungen vorzunehmen, ohne jedes Mal um Erlaubnis zu fragen

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code in VS Code unter Windows](./Claude_Code_in_VS_Code_Win.md) oder [Claude Code in VS Code auf dem Mac](./Claude_Code_in_VS_Code_Mac.md)
- Internetverbindung für PubMed-Suchen
- 15-20 Minuten

## Schritt 1: Zum Projektordner navigieren

Wenn Sie das [Slash-Commands-Tutorial](./Reuse_Prompts_via_Slash_Commands.md) abgeschlossen haben, existiert der `test_claude`-Ordner bereits. Diese Befehle funktionieren in beiden Fällen.

**Windows (WSL):**
- Öffnen Sie **Ubuntu** aus dem Startmenü
- Geben Sie diese Befehle ein:
  ```bash
  cd /mnt/c/Users/IHR_BENUTZERNAME/Documents
  mkdir -p test_claude
  cd test_claude
  ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren Windows-Benutzernamen

**Mac:**
- Öffnen Sie **Terminal** (finden Sie es unter Programme > Dienstprogramme)
- Geben Sie diese Befehle ein:
  ```bash
  cd ~/Documents
  mkdir -p test_claude
  cd test_claude
  ```

Das `-p`-Flag erstellt den Ordner, wenn er nicht existiert, oder tut einfach nichts, wenn er bereits existiert.

## Schritt 2: Claude Code starten

Geben Sie diesen Befehl ein:
```bash
claude
```

Claude Code startet und zeigt eine Willkommensnachricht an.

## Schritt 3: Auto-Edit-Modus aktivieren

Drücken Sie **Shift+Tab**, um den Auto-Edit-Modus zu aktivieren. Sie sehen eine Bestätigungsmeldung.

Der Auto-Edit-Modus ermöglicht Claude, mehrere Dateien zu erstellen und zu ändern, ohne jedes Mal um Erlaubnis zu fragen. Dies ist wichtig für das Erstellen von Skills, die das Erstellen vieler Dateien beinhalten.

## Schritt 4: Das PubMed-Suchskript erstellen

Kopieren und fügen Sie diesen Prompt ein:

```
Schreibe ein Python-Skript namens pubmed_search.py, das:
- Eine Suchanfrage als Kommandozeilenargument annimmt
- Bis zu 10 aktuelle Artikel abruft
- PMID, Titel, Autoren, Zeitschrift, Jahr, Abstract-Vorschau und URL zurückgibt
```
Claude erstellt das Skript. Es installiert das erforderliche Biopython-Paket, das ein Entrez-Modul für die Interaktion mit PubMed enthält. Überprüfen Sie die Ausgabe, um die Skriptstruktur zu sehen.

## Schritt 5: Das Skript testen

Bitten Sie Claude, es zu testen:

```
Teste das Skript mit der Anfrage "immunotherapy breast cancer"
```

Claude führt das Skript aus und zeigt 10 aktuelle Arbeiten über Immuntherapie bei Brustkrebs an. Sie sehen Titel, Autoren, Abstracts und PubMed-Links.

**Hinweis:** Die Suche findet Tausende von Artikeln, ruft aber nur die 10 neuesten für eine schnelle Überprüfung ab.

## Schritt 6: Den Medical Research Skill erstellen

Jetzt verpacken wir alles in einen wiederverwendbaren Skill. Kopieren und fügen Sie ein:

```
Erstelle einen Claude Skill namens "medical-research", der:
- Eine medizinische Frage aufnimmt
- Abfragen entwirft, um PubMed-Abstracts abzurufen
- Zusammenfassungen in einfacher Sprache erstellt, die für Nicht-Wissenschaftler zugänglich sind
- Das pubmed_search.py-Skript im Skill-Ordner enthält
```

Claude erstellt die vollständige Skill-Struktur:
- `.claude/skills/medical-research/pubmed_search.py` - Das Suchskript
- `.claude/skills/medical-research/SKILL.md` - Anweisungen für Claude zur Verwendung des Skills
- `.claude/skills/medical-research/README.md` - Benutzerdokumentation
- `.claude/skills/medical-research/EXAMPLES.md` - Beispielausgaben

Dies dauert 2-3 Minuten, während Claude umfassende Dokumentation schreibt.

## Schritt 7: Den Skill testen

Stellen Sie eine Forschungsfrage in einfacher Sprache:

```
Kann ich mit der Keto-Diät abnehmen?
```

Claude wird automatisch:
- Erkennen, dass dies eine medizinische Forschungsfrage ist
- Den medical-research Skill aktivieren
- PubMed nach relevanten Arbeiten durchsuchen
- Die Ergebnisse analysieren
- Die Forschung in einfacher Sprache erklären, die Wirksamkeit, Mechanismen und Überlegungen abdeckt

Die Antwort enthält Abschnitte wie „How It Works", „Research Findings", „Important Considerations" und „The Bottom Line".

## Schritt 8: Eine weitere Frage testen

Versuchen Sie ein anderes Forschungsthema:

```
Verursachen Impfstoffe Autismus?
```

Die Antwort erklärt den wissenschaftlichen Konsens, den Ursprung des Mythos und reale Konsequenzen.

## Schritt 9: Die Skill-Dateien erkunden (Optional)

Öffnen Sie VS Code, um die Skill-Struktur zu sehen:

**Windows:**
- Öffnen Sie den **Datei-Explorer**, navigieren Sie zu `C:\Users\IHR_BENUTZERNAME\Documents\test_claude`
- Klicken Sie mit der rechten Maustaste auf den Ordner und wählen Sie **Mit Code öffnen**

**Mac:**
- Öffnen Sie **Finder**, navigieren Sie zu `Documents/test_claude`
- Klicken Sie mit der rechten Maustaste auf den Ordner und wählen Sie **Mit Visual Studio Code öffnen**
- Oder geben Sie einfach ``` code . ``` im Terminal ein

In VS Code:
- Erweitern Sie `.claude/skills/medical-research/` im Datei-Explorer
- Öffnen Sie `SKILL.md`, um detaillierte Anweisungen für Claude zu sehen
- Öffnen Sie `README.md`, um die Benutzerdokumentation zu sehen
- Öffnen Sie `pubmed_search.py`, um den Python-Code zu sehen

**Hinweis:** Der Skill ist vollständig eigenständig – aller Code und alle Dokumentation befinden sich in einem Ordner.

## Schritt 10: Skills aus Anthropics Repository installieren

Anthropic pflegt ein Repository mit vorgefertigten Skills, die Sie sofort installieren und verwenden können.

- Um einen Skill aus dem Repository zu installieren, bitten Sie Claude einfach:

  ```
  Installiere den document skill aus Anthropics Repository
  ```
- Probieren Sie diesen Skill aus:
  ```
  Erstelle eine PowerPoint-Präsentation über Claude Skills.
  ```


Der **document skill** hilft Ihnen beim Lesen und Schreiben von Dateien in PDF, Word, PowerPoint und Excel. Claude klont den Skill in Ihren `.claude/skills/`-Ordner.

**Andere verfügbare Skills aus Anthropics Repository:**
- Durchsuchen Sie den vollständigen Katalog unter [github.com/anthropics/claude-skills](https://github.com/anthropics/skills)
- Fragen Sie Claude „Welche Skills sind im Anthropic Repository verfügbar?", um die aktuelle Liste zu sehen

## Nächste Schritte

- **PDF:** Kopieren Sie ein paar PDF-Dateien in einen Unterordner in diesem Projektordner und bitten Sie um Zusammenfassungen.
- **Andere öffentliche Skills:** Probieren Sie Skills aus, die von Anthropic verfügbar sind.
- **Skills teilen:** Skills sind einfach gezippte Ordner!
- **Andere Skills erstellen:** Alles, was Sie interessiert. Zum Beispiel können Sie Ihre eigenen Datendateien in einen Skill-Ordner legen.

## Fehlerbehebung

- **Biopython nicht installiert:** Claude installiert Biopython automatisch, wenn es das Skript erstellt. Wenn Sie beim Testen Importfehler sehen, bitten Sie Claude, Biopython manuell mit `pip install biopython` zu installieren
- **Skript nicht gefunden:** Überprüfen Sie, ob der Auto-Edit-Modus aktiviert war (Shift+Tab) – Claude braucht die Erlaubnis, Dateien zu erstellen
- **Skill aktiviert sich nicht:** Der Skill sollte sofort nach der Erstellung funktionieren – versuchen Sie, die Frage erneut zu stellen oder überprüfen Sie, ob SKILL.md den korrekten `name: medical-research` in der Kopfzeile hat

## Workflow-Überblick

- **Claude Skills** sind mächtiger als Slash-Befehle – sie kombinieren Code, Dokumentation und benutzerdefinierte Anweisungen
- **Auto-Edit-Modus** (Shift+Tab) rationalisiert die Erstellung, indem wiederholte Berechtigungsabfragen vermieden werden
- **Eigenständige Verpackung** – Skripte befinden sich innerhalb von Skill-Ordnern, was sie portabel und teilbar macht
- **Automatische Aktivierung** – Skills werden basierend auf Fragemustern ausgelöst (Forschungsfragen aktivieren medical-research)
- **Natürlichsprachliche Schnittstelle** – Stellen Sie natürliche Fragen, ohne die technischen Details zu kennen

## Skills vs Slash-Befehle

| Merkmal | Skills | Slash-Befehle |
|---------|--------|----------------|
| **Was es enthält** | Prompts, Code, Daten und Dokumentation | Nur Prompts |
| **Aktivierung** | Wird automatisch geladen, wenn relevant | Manuell ausgelöst mit `/befehl` |
| **Anwendungsfall** | Komplexe Workflows, die Code-Ausführung erfordern | Schnelle Prompt-Vorlagen und Workflows |
| **Dateispeicherort** | `.claude/skills/skill-name/` | `.claude/commands/` |
| **Struktur** | Mehrere Dateien (SKILL.md, README.md, Code-Dateien) | Einzelne `.md`-Datei pro Befehl |

**Wichtige Erkenntnis:** Slash-Befehle injizieren nur Prompts aus der UI. Das ist nützlich, aber begrenzt.

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 13. Dezember 2025.
