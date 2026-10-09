---
title: "Claude Code: Grundlegende Operationen"
lang: "de"
---
[Startseite](./)

# Claude Code: Grundlegende Operationen

Das Programmieren mit KI-Unterstützung zu lernen kann anfangs überwältigend wirken. Stellen Sie sich Claude Code als einen erfahrenen Kollegen vor, der neben Ihnen sitzt – Sie beschreiben auf Deutsch, was Sie möchten, und er hilft Ihnen dabei, es zu erreichen. Dieses Tutorial vermittelt Ihnen die wesentlichen Operationen, die Sie täglich nutzen werden, vom Starten von Gesprächen bis zur Verwaltung Ihres Arbeitsbereichs.

## Wichtige Konzepte

- **Arbeitsbereich** - Der Ordner, aus dem Sie Claude Code starten; Claude liest und bearbeitet in dieser Sitzung die Dateien darin
- **REPL (Read-Eval-Print Loop)** - Eine interaktive Sitzung, in der Sie Befehle eingeben, Claude antwortet und das Gespräch fortgesetzt wird, bis Sie es beenden
- **Kontext** - Die Menge an Code und Gesprächsverlauf, die Claude sich merkt; wie Arbeitsspeicher, der sich mit der Zeit füllt
- **Slash-Befehle** - Eingebaute Abkürzungen, die mit `/` beginnen und bestimmte Aktionen ausführen, wie das Löschen des Verlaufs oder das Anzeigen von Hilfe

## Was Sie benötigen

- Claude Code installiert aus dem [Windows](Install_CLAUDE_Code_Win.md)- oder [Mac](Install_Claude_Code_MacOS.md)-Tutorial
- Grundlegende Vertrautheit mit der Verwendung eines Terminals oder einer Eingabeaufforderung
- 15-20 Minuten

## Schritt 1: Ihr Terminal öffnen

- **Windows**: Drücken Sie die Windows-Taste, geben Sie `PowerShell` ein und drücken Sie Enter, um PowerShell zu öffnen
- **Mac**: Drücken Sie `Cmd+Leertaste`, geben Sie `Terminal` ein und drücken Sie Enter

**Hinweis:** Wenn Sie im Windows-Installations-Tutorial statt der nativen Installation den optionalen WSL/Ubuntu-Weg eingerichtet haben, öffnen Sie stattdessen die App **Ubuntu** und verwenden Sie in den folgenden Schritten Linux-Pfade (z. B. `/mnt/c/Users/IhrName/...`).

Ein Textfenster öffnet sich, in dem Sie Befehle eingeben können.

## Schritt 2: Die Demo-Projekt-Dateien holen

Wir verwenden ein echtes Data-Science-Projekt, um die Funktionen von Claude Code zu erkunden. Sie können es entweder mit Git klonen oder direkt herunterladen.

**Option A: Mit Git klonen (wenn Sie Git installiert haben):**

```
git clone https://github.com/gexijin/data_projects
cd data_projects
```

**Option B: Ohne Git herunterladen:**

- Besuchen Sie [https://github.com/gexijin/data_projects](https://github.com/gexijin/data_projects) in Ihrem Webbrowser
- Klicken Sie auf die grüne **Code**-Schaltfläche oben rechts
- Klicken Sie auf **Download ZIP**
- Entpacken Sie die ZIP-Datei in Ihren Downloads-Ordner. GitHub nennt den entpackten Ordner **data_projects-main** – benennen Sie ihn in **data_projects** um, damit er zum Rest dieses Tutorials passt.
- Navigieren Sie in Ihrem Terminal zum entpackten Ordner:
  ```
  cd ~/Downloads/data_projects
  ```

Passen Sie den Pfad an, falls Sie es woanders entpackt haben.

## Schritt 3: Claude Code aus dem Ordner starten

In Ihrem Terminal (stellen Sie sicher, dass Sie sich im Ordner data_projects befinden), geben Sie ein:

```bash
claude
```

Melden Sie sich mit Ihrem Claude-Abonnement an, wie im Installations-Tutorial beschrieben ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Nach der Anmeldung sehen Sie eine Willkommensnachricht und die Claude Code-Eingabeaufforderung.

## Schritt 4: Fragen zu Ihrem Projekt stellen

Claude Code liest Ihre Dateien automatisch, wenn es nötig ist. Probieren Sie diese Fragen aus, um Ihr Projekt zu verstehen:

**Nach der Ordnerstruktur fragen:**

```
Was ist die Ordnerstruktur dieses Projekts?
```

**Nach Technologien fragen:**

```
Welche Technologien und Bibliotheken verwendet dieses Projekt?
```

**Nach den letzten Änderungen fragen:**

```
Was war die letzte Änderung an diesem Projekt?
```

Claude prüft den Git-Verlauf (falls vorhanden) und informiert Sie über die letzten Commits.

Sie können Claude alles über Ihren Code in natürlicher Sprache fragen. Es liest Dateien nach Bedarf, um Ihre Fragen zu beantworten.

## Schritt 5: Wichtige Slash-Befehle

Geben Sie `/` ein und drücken Sie Enter, um alle verfügbaren Befehle zu sehen. Hier sind die wichtigsten:

**Alle Befehle anzeigen:**

```
/
```

Dies zeigt ein Menü aller Slash-Befehle an. Verwenden Sie die Pfeiltasten zum Durchsuchen, drücken Sie Enter zum Auswählen oder Esc zum Abbrechen.

**Hilfe erhalten:**

```
/help
```
Zeigt Dokumentation zur Verwendung von Claude Code an.



**Kontextverbrauch prüfen:**
Es ist wichtig, den Kontext zu verwalten, Claudes „Arbeitsspeicher".

```
/context
```

**Gesprächsverlauf löschen:**

Wenn der Kontext voll wird, starten Sie ein neues Gespräch mit `/clear`.
```
/clear
```
Löscht das aktuelle Gespräch und beginnt von vorne. Verwenden Sie dies, wenn Sie das Thema wechseln möchten oder wenn Ihr Gespräch zu lang wird. Es ist wichtig, den Kontext zu verwalten.


**Claude Code beenden:**

```
/exit
```

Beendet Ihre Sitzung und kehrt zu Ihrer normalen Terminal-Eingabeaufforderung zurück. Sie können auch zweimal **Strg + C** drücken.

## Schritt 6: Änderungen genehmigen und Tastenkombinationen nutzen

Wenn Claude eine Datei bearbeiten oder einen Befehl ausführen möchte, zeigt es ein kleines Menü mit Optionen wie **Yes** und **No**. Markieren Sie Ihre Wahl mit den Pfeiltasten und drücken Sie **Enter**.

Einige Tastenkombinationen machen das Arbeiten mit Claude Code außerdem schneller:

- **Umschalt+Tab** - Zwischen den Modi wechseln (Manual, Accept Edits, Plan) - Der Plan-Modus ist nützlich, um eine komplexe Aufgabe zu prüfen, bevor Claude etwas ändert
- **Strg+C** - Brechen Sie die aktuelle Operation oder Claudes Antwort ab
- **Esc** - Claude mitten in der Antwort stoppen oder ein Menü schließen
- **`\` und dann Enter** (oder **Strg+J**) - Fügen Sie eine neue Zeile in Ihre Nachricht ein, ohne sie zu senden

## Schritt 7: Immer eine CLAUDE.md-Datei erstellen

Die CLAUDE.md-Datei ist das Handbuch Ihres Projekts für Claude. Sie bleibt über Sitzungen hinweg erhalten, sodass Claude sich wichtigen Kontext über Ihr Projekt merkt.

**Die Datei erstellen:**

```
/init
```

Claude erstellt die Datei mit einer Zusammenfassung Ihres Projekts. Diese Datei bleibt in Ihrem Projektstammverzeichnis und Claude liest sie automatisch bei jedem Start einer neuen Sitzung.

Sie können CLAUDE.md im Projektordner jederzeit bearbeiten, um projektspezifische Anweisungen, Codierkonventionen oder wichtigen Kontext wie den Zweck von Dateien usw. hinzuzufügen.

## Schritt 8: Auf Dateien oder Codezeilen verweisen

Sie können `@` verwenden, um auf eine bestimmte Datei zu verweisen:

```
Erkläre den Code in @Visualization/Matplotlib/Nested_Pie_Chart.ipynb
```

Claude liest das Notebook und erklärt, was es tut, wie es funktioniert und was der Code erreicht. Dies bringt die Datei effektiv in den Kontext.

Wenn Sie mit Claude Code aus VS Code arbeiten und die Claude Code-Erweiterung installiert haben, können Sie die Datei zum Kontext hinzufügen, indem Sie sie einfach öffnen. Sie sehen unten rechts im Befehlsfenster `In Nested_Pie_Chart.ipynb`. Dann weiß Claude, dass Sie über diese Datei sprechen.

Außerdem können Sie einige Codezeilen auswählen und Claude zeigt **3 lines selected** an. Sie können Claude bitten, schnelle Änderungen an diesen Zeilen vorzunehmen oder Fragen zu stellen. Daher empfehle ich dringend, Claude Code aus VS Code zu verwenden.


## Schritt 9: Aktionen mit Linux-Befehlen ausführen

Claude kann Aktionen ausführen, indem es Linux-Befehle in vielen Formen ausführt.

- Software installieren
  ```
  Installiere die pandas-Bibliothek
  ```

- Versionskontrolle starten
  ```
  Starte die Versionskontrolle mit Git. Mein Name ist James Bond und meine E-Mail ist bond@earth.com
  ```
- Änderungen committen
  ```
  Committe diese Änderungen.
  ```
- Daten finden und herunterladen
  ```
  Lade den Weindatenqualitätsdatensatz von UCI herunter. Lege ihn in einen neuen Ordner namens wine.
  ```

- Code ausführen
  ```
  Schreibe den Code für das verschachtelte Kreisdiagramm als reguläres Python-Skript um.
  Führe es aus und speichere den neuen Code und die Diagramme im selben Ordner.
  ```

Claude installiert Software, behebt Fehler und verwaltet Umgebungen – alles von selbst.



Sie haben im Wesentlichen einen Experten für Linux-Bash-Befehle zur Verfügung. Solange Sie Berechtigungen verwalten und Aktionen genehmigen, können Sie sehr produktiv sein.

## Nächste Schritte

Jetzt, da Sie die Grundlagen kennen, probieren Sie diese selbst aus:

- Bitten Sie Claude, einen Machine-Learning-Algorithmus in einem der Projektordner zu erklären
- Fordern Sie Änderungen an einem bestehenden Notebook an (wie das Ändern von Diagrammfarben oder das Hinzufügen neuer Funktionen)
- Erstellen Sie ein neues Python-Skript, das Daten aus dem Projekt verwendet
- Bitten Sie Claude, zwei verschiedene Ansätze in der Codebasis zu vergleichen

## Fehlerbehebung

- **„Command not found"-Fehler** - Claude Code ist nicht installiert oder nicht in Ihrem PATH. Folgen Sie erneut dem Installations-Tutorial für [Windows](Install_CLAUDE_Code_Win.md) oder [Mac](Install_Claude_Code_MacOS.md), oder führen Sie das Installationsprogramm direkt erneut aus: `irm https://claude.ai/install.ps1 | iex` (Windows PowerShell) oder `curl -fsSL https://claude.ai/install.sh | bash` (Mac/WSL).
- **Claude gibt veraltete Informationen** - Löschen Sie den Kontext mit `/clear` und fragen Sie erneut. Lange Gespräche können Claudes Speicher füllen.
- **Dateiänderungen funktionieren nicht** - Stellen Sie sicher, dass Sie Schreibrechte in Ihrem Projektordner haben. Claude fragt um Erlaubnis, bevor es Dateien ändert – wählen Sie im angezeigten Menü **Yes** aus.
- **Kontext füllt sich schnell** - Verwenden Sie `/context`, um die Nutzung zu überprüfen. Wenn er fast voll ist, verwenden Sie `/clear`, um ein neues Gespräch mit einer sauberen Ausgangslage zu beginnen.

## Workflow-Überblick

Das Arbeiten mit Claude Code folgt diesem Muster:

- Starten Sie Claude in Ihrem Projektordner mit `claude`
- Stellen Sie Fragen in natürlicher Sprache
- Claude liest Dateien nach Bedarf und antwortet
- Fordern Sie Codeänderungen an – Claude fragt um Erlaubnis, bevor es Dateien ändert
- Verwenden Sie `/clear`, wenn Sie das Thema wechseln oder der Kontext voll wird
- Verwenden Sie `/exit`, wenn Sie fertig sind

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 14. Dezember 2025.
