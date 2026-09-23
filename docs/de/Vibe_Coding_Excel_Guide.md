---
title: "Vibe Coding eines Budget-Trackers in Excel mit Claude Code"
lang: "de"
---
[Startseite](./)

# Vibe Coding eines Budget-Trackers in Excel mit Claude Code

Vibe Coding ist wie ein Gespräch mit Ihrem Computer – Sie beschreiben das Ergebnis, Claude Code baut es, Sie testen und verfeinern. Es ist keine Magie; es ist eine neue Art zu arbeiten, bei der Sie die Vision vorgeben und die KI die Tabellen-Mechanik übernimmt: Formeln, Formatierung und Diagramme. Dieses Tutorial führt Sie Schritt für Schritt durch den Aufbau eines echten Budget-Trackers mit mehreren Tabellenblättern – nur mit Anfragen in natürlicher Sprache.

## Wichtige Konzepte

- **[Claude Code](https://code.claude.com/)** - KI-Programmierassistent, der Dateien basierend auf Ihren natürlichsprachlichen Anfragen schreibt, bearbeitet und korrigiert
- **Arbeitsmappe mit mehreren Tabellenblättern** - Eine einzelne `.xlsx`-Datei mit mehreren Tabs (Einnahmen, Ausgaben, Übersicht), die sich über Formeln aufeinander beziehen
- **Iterative Verfeinerung** - Das zentrale Vibe-Coding-Muster: beschreiben → testen → verfeinern → funktionierende Versionen committen

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code mit Excel in VS Code verwenden](./Excel_Coding_VS_Code_Guide)
- Abgeschlossenes Tutorial [GitHub Desktop mit Claude Code verwenden](./GitHub_Desktop_Claude_Code_Workflow)
- 25-30 Minuten

## Schritt 1: Neues GitHub-Repository erstellen

- Öffnen Sie GitHub Desktop
- Klicken Sie auf **File > New Repository**
- Füllen Sie die Details aus:
  - **Name:** `budget-dashboard`
  - **Description:** `Persönlicher Budget-Tracker, erstellt mit Vibe Coding`
  - **Local Path:** Wählen Sie einen Speicherort (z.B. Dokumente oder Arbeitsordner)
  - Aktivieren Sie **Initialize this repository with a README**
- Klicken Sie auf **Create Repository**
- Klicken Sie oben auf **Publish repository**
- Deaktivieren Sie **Keep this code private**, wenn Sie es öffentlich machen möchten (optional)
- Klicken Sie auf **Publish Repository**

Sie haben jetzt ein lokales Git-Repository und ein Backup auf GitHub.

## Schritt 2: Das Projekt in VS Code öffnen

- Öffnen Sie VS Code
- Klicken Sie auf **File > Open Folder**
- Wählen Sie Ihren `budget-dashboard`-Ordner aus
- Klicken Sie auf **Ordner auswählen** (Windows) oder **Öffnen** (Mac)
- Falls noch nicht geschehen, installieren Sie die Erweiterung **Spreadsheet Viewer** von MESCIUS (früher **Excel Viewer** von GrapeCity), damit Sie Tabellen ansehen können, ohne VS Code zu verlassen. Suchen Sie im Extensions-Bereich nach ihrer ID, `GrapeCity.gc-excelviewer`, um die richtige zu finden

## Schritt 3: Claude Code starten

- Klicken Sie auf **Terminal > New Terminal**
- Geben Sie diesen Befehl ein, um Claude Code zu starten:

```bash
claude
```

- Melden Sie sich an, falls Sie dazu aufgefordert werden, und warten Sie dann auf die Willkommensnachricht von Claude

Claude Code läuft jetzt und ist bereit für Ihre Anfragen.

## Schritt 4: Erster Vibe - Die Blätter Einnahmen und Ausgaben erstellen

Anstatt eine Tabelle Zelle für Zelle aufzubauen, beschreiben Sie einfach, was Sie möchten.

- Geben Sie im Claude Code-Terminal ein:

```
Erstelle eine Tabelle namens budget.xlsx mit zwei Tabellenblättern: „Einnahmen" und „Ausgaben". Einnahmen soll die Spalten Quelle, Monat und Betrag haben, mit 3 Beispiel-Einnahmequellen über 2 Monate. Ausgaben soll die Spalten Kategorie, Monat und Betrag haben, mit 6 Beispielkategorien (wie Miete, Lebensmittel, Transport, Nebenkosten, Freizeit, Sparen) über dieselben 2 Monate. Füge unten auf jedem Blatt eine Zeile „Summe" mit SUM-Formeln hinzu.
```

- Drücken Sie Enter
- Beobachten Sie, wie Claude ein Python-Skript schreibt und ausführt, das die Arbeitsmappe erstellt, und sie anschließend neu berechnet, damit die Summen echte Zahlen anzeigen
- Öffnen Sie `budget.xlsx` im Spreadsheet Viewer-Tab und klicken Sie sich durch beide Blätter

**Speichern Sie Ihren Fortschritt:** Bitten Sie Claude, mit Git zu committen, oder machen Sie dies selbst in GitHub Desktop:
```
Committe diese Änderungen.
```

## Schritt 5: Zweiter Vibe - Ein Blatt Übersicht hinzufügen

Bevor Sie Diagramme erstellen, verknüpfen Sie die beiden Blätter miteinander.

- Geben Sie im Claude Code-Terminal ein:

```
Füge budget.xlsx ein drittes Tabellenblatt namens „Übersicht" hinzu. Es soll Gesamteinnahmen, Gesamtausgaben und Nettoersparnis (Einnahmen minus Ausgaben) anzeigen, jeweils berechnet mit Formeln, die sich auf die Blätter Einnahmen und Ausgaben beziehen – keine fest eingetragenen Zahlen.
```

- Drücken Sie Enter
- Claude aktualisiert die Arbeitsmappe und berechnet sie neu
- Öffnen Sie den Tab **Übersicht** und klicken Sie auf die Zelle Nettoersparnis, um zu prüfen, ob es sich um eine Formel handelt, die sich auf die anderen Blätter bezieht

**Speichern Sie Ihren Fortschritt:** Bitten Sie Claude, zu committen, oder verwenden Sie GitHub Desktop.

## Schritt 6: Dritter Vibe - Diagramme hinzufügen

Zahlen sind nützlich, aber Diagramme erzählen die Geschichte auf einen Blick.

- Geben Sie im Claude Code-Terminal ein:

```
Füge dem Blatt Ausgaben ein Kreisdiagramm hinzu, das den Gesamtanteil jeder Kategorie an den Ausgaben zeigt. Füge dem Blatt Übersicht ein Balkendiagramm hinzu, das Gesamteinnahmen und Gesamtausgaben für jeden Monat vergleicht.
```

- Drücken Sie Enter
- Claude fügt beide Diagramme hinzu und berechnet die Datei neu
- Öffnen Sie `budget.xlsx` im Spreadsheet Viewer erneut (oder aktualisieren Sie den Tab) und prüfen Sie beide Blätter auf die neuen Diagramme

## Schritt 7: Vierter Vibe - Kategorien über dem Budget hervorheben

Machen Sie Probleme auf einen Blick sichtbar, anstatt in den Zahlen danach zu suchen.

- Geben Sie im Claude Code-Terminal ein:

```
Füge auf dem Blatt Ausgaben eine bedingte Formatierung hinzu, sodass jede Ausgabe über $500 in einem einzelnen Monat rot hervorgehoben wird und alles unter $100 grün hervorgehoben wird.
```

- Drücken Sie Enter
- Öffnen Sie die Datei erneut und prüfen Sie das Blatt Ausgaben – die Zellen sollten jetzt je nach Wert eingefärbt sein

Wenn etwas nicht richtig aussieht, kopieren Sie, was Sie sehen, und beschreiben Sie es Claude, damit es das Problem behebt.

## Schritt 8: Fünfter Vibe - Eine Dropdown-Liste für Kategorien hinzufügen

Machen Sie das Blatt leichter erweiterbar, ohne dass sich Tippfehler einschleichen.

- Geben Sie im Claude Code-Terminal ein:

```
Füge der Spalte Kategorie im Blatt Ausgaben eine Datenüberprüfung hinzu, sodass sie nur Werte aus einer Dropdown-Liste der vorhandenen Kategorien sowie „Sonstiges" akzeptiert. Füge unten zwei leere Zeilen für neue Einträge hinzu.
```

- Drücken Sie Enter
- Öffnen Sie die Datei, klicken Sie in eine der leeren Zellen der Spalte Kategorie und prüfen Sie, ob ein Dropdown-Pfeil mit Ihrer Kategorienliste erscheint

## Schritt 9: Überprüfen und Committen

Überprüfen Sie vor dem Committen, was Claude erstellt hat.

- Klicken Sie sich im Spreadsheet Viewer durch alle drei Blätter – Einnahmen, Ausgaben, Übersicht
- Sie müssen nicht jede Formel verstehen, aber bekommen Sie ein Gefühl für die Struktur
- Öffnen Sie GitHub Desktop
- Sie sehen `budget.xlsx` als geänderte Datei aufgelistet
- Geben Sie im **Summary**-Feld unten links ein:

```
Diagramme, bedingte Formatierung und Kategorie-Dropdown zum Budget-Tracker hinzufügen
```

- Klicken Sie auf **Commit to main**
- Klicken Sie auf **Push origin**, um auf GitHub zu sichern

Sie haben eine vollständig funktionierende Version Ihres Budget-Trackers gespeichert!

## Schritt 10: Iterieren und Verbessern

Vibe Coding glänzt beim Iterieren. Versuchen Sie, Funktionen hinzuzufügen, indem Sie sie beschreiben:

**Beispielanfragen an Claude:**

- "Füge dem Blatt Übersicht eine Zeile Sparziel hinzu, die den Fortschritt in Richtung eines Sparziels von $500/Monat zeigt"
- "Füge ein viertes Tabellenblatt hinzu, das einen Vergleich zum Vorjahr zeigt, sobald ich Daten für mehr Monate hinzufüge"
- "Ändere die Farben des Kreisdiagramms in ein Blau-Grau-Farbschema"
- "Füge zu jeder Formel eine Notiz mit einer Erklärung hinzu, damit ich lernen kann, was sie bewirken"
- "Erstelle eine zweite Arbeitsmappe namens household_budget.xlsx für eine vierköpfige Familie mit mehr Kategorien"

Nach jeder erfolgreichen Funktion:
- Öffnen Sie die Datei und prüfen Sie sie im Spreadsheet Viewer
- Wenn es funktioniert, committen Sie mit GitHub Desktop
- Wenn etwas falsch aussieht, beschreiben Sie es Claude und bitten Sie um Korrektur
- Wenn behoben, committen Sie die funktionierende Version

**Schlüsselprinzipien:**

- **Beschreiben Sie Ergebnisse, nicht die Umsetzung** - Sagen Sie „hebe Ausgaben über $500 hervor", nicht „verwende bedingte Formatierung mit einer CellIsRule"
- **Iterieren Sie schnell** - Testen → verfeinern → testen → verfeinern
- **Committen Sie funktionierende Versionen** - Speichern Sie jeden Erfolg, bevor Sie neue Funktionen ausprobieren
- **Akzeptieren Sie Fehlschläge** - Wenn eine Formel oder ein Diagramm nicht richtig herauskommt, beschreiben Sie einfach das Problem und bitten Sie Claude, es zu beheben
- **Behalten Sie die Kontrolle** - Sie entscheiden, was der Tracker anzeigen soll und wann er gut genug ist

Jedes Mal folgen Sie dem Muster: beschreiben → Datei prüfen → iterieren → committen.

## Nächste Schritte

- **Wenden Sie es auf Ihre eigenen Finanzen an** - Bitten Sie Claude, den Tracker mit Ihren echten Einnahme- und Ausgabenkategorien neu aufzubauen
- **Importieren Sie echte Daten** - Legen Sie einen Kontoauszug als CSV in Ihren Projektordner und bitten Sie Claude, ihn in den Tracker einzuarbeiten
- **Lernen Sie durch Fragen** - Wenn Claude eine Formel schreibt, fragen Sie „erkläre, was diese Formel macht", um Excel zu lernen
- **Teilen Sie Ihren Tracker** - Pushen Sie die fertige Datei auf GitHub, damit Sie (oder Familienmitglieder) jederzeit die neueste Version abrufen können
- **Lesen Sie über Vibe Coding** - Besuchen Sie [IBMs Leitfaden](https://www.ibm.com/think/topics/vibe-coding), um mehr über diesen Programmierstil zu erfahren

## Fehlerbehebung

- **Eine Formelzelle ist leer oder zeigt `None`** - Die Datei muss nach Änderungen neu berechnet werden. Bitten Sie Claude: „Berechne budget.xlsx neu und bestätige, dass es keine Formelfehler gibt."
- **Diagramm aktualisiert sich nach dem Ändern der Daten nicht** - Öffnen Sie den Tab in VS Code erneut (schließen Sie ihn und klicken Sie wieder auf die Datei), um den Spreadsheet Viewer zur Aktualisierung zu zwingen.
- **Claude macht Fehler** - Normal! Beschreiben Sie, was falsch aussieht, und bitten Sie Claude, es zu beheben. Vibe Coding beinhaltet Iteration und Debugging.
- **Kann nicht auf GitHub pushen** - Stellen Sie sicher, dass Sie in GitHub Desktop angemeldet sind und das Repository veröffentlicht haben (Schritt 1). Überprüfen Sie Ihre Internetverbindung.
- **Dropdown-Liste erscheint nicht** - Die Datenüberprüfung wird nur in echten Tabellenprogrammen (Excel, LibreOffice, Google Sheets) angezeigt, nicht immer in einfachen Vorschau-Programmen. Öffnen Sie die Datei in Excel oder LibreOffice Calc, um sie zu testen.

## Workflow-Überblick

Dieses Tutorial kombinierte mehrere Tools in einem Workflow:

- **GitHub Desktop** - Versionskontrolle mit visueller Oberfläche (Repos erstellen, committen, pushen)
- **VS Code** - Editor mit der Spreadsheet Viewer-Erweiterung für schnelle Vorschauen
- **Claude Code** - KI-Assistent, der aus Ihren Beschreibungen echte `.xlsx`-Dateien erstellt und bearbeitet
- **openpyxl (im Hintergrund)** - Die Engine, mit der Claude Formeln, Formatierung und Diagramme in die Datei schreibt

Die Magie liegt nicht in einem einzelnen Tool – sondern darin, dass Sie mit Vibe Coding beschreiben können, was Sie möchten, und schnell iterieren. Sie sind von einem leeren Ordner zu einem funktionierenden Budget-Tracker voller Diagramme gekommen, ohne eine einzige Formel von Hand zu schreiben.

## Täglicher Workflow

Nach dieser anfänglichen Einrichtung sieht Ihre tägliche Vibe-Coding-Routine so aus:

1. **Öffnen Sie VS Code** - Öffnen Sie Ihren Projektordner
2. **Starten Sie Claude Code** - Geben Sie `claude` im Terminal ein
3. **Beschreiben Sie Ihr Ziel** - „Füge eine Funktion hinzu, die..." oder „Korrigiere die Zeile, in der..."
4. **Prüfen Sie die Datei** - Öffnen Sie sie im Spreadsheet Viewer oder in Excel/LibreOffice
5. **Iterieren oder committen** - Wenn etwas nicht stimmt, beschreiben Sie die Korrektur; wenn es funktioniert, committen Sie mit GitHub Desktop
6. **Pushen Sie regelmäßig** - Klicken Sie auf **Push origin**, um auf GitHub zu sichern

Je mehr Sie üben, desto besser können Sie beschreiben, was Sie möchten. Vibe Coding ist eine Fähigkeit – Sie lernen, welche Beschreibungen am besten funktionieren und wie Sie große Tabellen-Ideen in testbare Teile zerlegen.

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 21. September 2026.
