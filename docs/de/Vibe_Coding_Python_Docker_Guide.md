[Startseite](./)

# Vibe Coding in Python mit Claude Code und Docker

Sie haben Python-Code geschrieben, indem Sie jede Zeile selbst getippt haben. Aber was wäre, wenn Sie beschreiben könnten, was Sie wollen, in einfachem Deutsch, und der Code erscheint? Vibe Coding ist wie ein Gespräch mit Ihrem Computer – Sie beschreiben das Ergebnis, Claude Code baut es, Sie testen und verfeinern. Es ist keine Magie; es ist eine neue Art zu arbeiten, bei der Sie die Vision leiten und KI die Umsetzung übernimmt. Dieses Tutorial zeigt Ihnen, wie Sie den klassischen Iris-Blumendatensatz analysieren, indem Sie nur natürlichsprachliche Anfragen verwenden.

## Wichtige Konzepte

- **[Vibe Coding](https://www.ibm.com/think/topics/vibe-coding)** - Programmieren durch Beschreiben dessen, was Sie wollen, in natürlicher Sprache, dann Iterieren basierend auf Ergebnissen, anstatt Code Zeile für Zeile zu schreiben
- **[Claude Code](https://code.claude.com/)** - KI-Programmierassistent, der Code basierend auf Ihren natürlichsprachlichen Anfragen schreibt, debuggt und überarbeitet
- **[Iris-Datensatz](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)** - Klassischer Datensatz mit Messungen von 150 Iris-Blumen aus drei Arten
- **Iterative Verfeinerung** - Das zentrale Vibe-Coding-Muster: beschreiben → testen → verfeinern → funktionierende Versionen committen

## Was Sie benötigen

- Abgeschlossenes Tutorial [Python-Programmierung in VS Code über Docker](./Python_Coding_Docker_Guide)
- Abgeschlossenes Tutorial [GitHub Desktop mit Claude Code verwenden](./GitHub_Desktop_Claude_Code_Workflow)
- 20-25 Minuten

## Schritt 1: Neues GitHub-Repository erstellen

- Öffnen Sie GitHub Desktop
- Klicken Sie auf **File > New Repository**
- Füllen Sie die Details aus:
  - **Name:** `iris-analysis`
  - **Description:** `Iris data analysis built with vibe coding`
  - **Local Path:** Wählen Sie einen Speicherort (z.B. Dokumente oder Arbeitsordner)
  - Aktivieren Sie **Initialize this repository with a README**
- Klicken Sie auf **Create Repository**
- Klicken Sie oben auf **Publish repository**
- Deaktivieren Sie **Keep this code private**, wenn Sie es öffentlich machen möchten (optional)
- Klicken Sie auf **Publish Repository**

Sie haben jetzt ein lokales Git-Repository und ein Backup auf GitHub.

## Schritt 2: Docker-Konfiguration kopieren

Sie benötigen den `.devcontainer`-Ordner aus dem Vibe-Projekt, um Ihre Docker-Umgebung einzurichten.

- Öffnen Sie den Datei-Explorer (Windows) oder Finder (Mac)
- Navigieren Sie zu Ihrem Vibe-Projektordner (z.B. `Documents/vibe`)
- Finden Sie den `.devcontainer`-Ordner
- Kopieren Sie den gesamten Ordner (er enthält `Dockerfile` und `devcontainer.json`)
- Navigieren Sie zu Ihrem neuen `iris-analysis`-Ordner
- Fügen Sie den `.devcontainer`-Ordner dort ein

Ihr `iris-analysis`-Ordner sollte jetzt enthalten:
- `.devcontainer/` (Ordner, den Sie gerade kopiert haben)
- `README.md` (von GitHub Desktop erstellt)
- `.git/` (versteckter Ordner für Versionskontrolle)

## Schritt 3: Projekt im Container öffnen

- Öffnen Sie VS Code
- Klicken Sie auf **File > Open Folder**
- Navigieren Sie zum `iris-analysis`-Ordner
- Klicken Sie auf **Ordner auswählen**
- Eine Benachrichtigung erscheint unten rechts: **Folder contains a Dev Container configuration file**
- Klicken Sie auf **Reopen in Container**
- Wenn Sie die Benachrichtigung nicht sehen, klicken Sie auf das grüne Symbol in der unteren linken Ecke und wählen Sie **Reopen in Container**
- VS Code baut den Docker-Container (dauert beim ersten Mal 3-5 Minuten)
- Beobachten Sie die Fortschrittsanzeige mit den Build-Schritten
- Nach Abschluss zeigt das grüne Symbol **Dev Container: Python in Docker** an

## Schritt 4: Claude Code starten

- Klicken Sie in VS Code auf **Terminal > New Terminal**
- Sie sind jetzt innerhalb des Docker-Containers
- Geben Sie diesen Befehl ein, um Claude Code zu starten:

```bash
claude
```

- Ein Browserfenster öffnet sich zur Authentifizierung
- Klicken Sie auf **Continue with Google** oder **Continue with Email**
- Melden Sie sich mit Ihrem Claude-Konto an (oder erstellen Sie eines)
- Nach erfolgreicher Authentifizierung kehren Sie zum VS Code-Terminal zurück
- Sie sehen Claudes Willkommensnachricht

Claude Code läuft jetzt und ist bereit für Ihre Anfragen.

## Schritt 5: Erster Vibe - Daten laden

Jetzt beginnt der Spaß. Anstatt Dokumentation nachzuschlagen, beschreiben Sie einfach, was Sie wollen.

- Geben Sie im Claude Code-Terminal ein:

```
Lade den Iris-Datensatz aus scikit-learn. Konvertiere ihn in einen Pandas-DataFrame mit korrekten Spaltennamen. Füge die Artnamen als Spalte hinzu (nicht nur Zahlen). Zeige mir die ersten 10 Zeilen. Speichere den Code in einer Datei namens iris_exploration.py
```

- Drücken Sie Enter
- Beobachten Sie Claude:
  - Python-Code zum Laden der Daten schreiben
  - Ein Skript mit korrekten Imports erstellen
  - Den Code ausführen, um Ihnen die Ergebnisse zu zeigen
- Überprüfen Sie die Ausgabe mit Blumenmessungen und Artnamen

Sie haben gerade Vibe Coding verwendet! Kein Durchsuchen von Dokumentation, kein Trial-and-Error – einfach beschreiben und testen.

Bitten Sie Claude, mit Git zu committen. Oder machen Sie dies selbst in GitHub Desktop.
```
Committe diese Änderungen.
```
## Schritt 6: Zweiter Vibe - Zusammenfassende Statistiken

Bevor Sie Visualisierungen erstellen, verstehen Sie, was die Daten enthalten.

- Geben Sie im Claude Code-Terminal ein:

```
Zeige mir zusammenfassende Statistiken für die Iris-Daten, gruppiert nach Arten. Ich möchte den Mittelwert, das Minimum und das Maximum für jede Messung (Kelchblattlänge, Kelchblattbreite, Blütenblattlänge, Blütenblattbreite) für jede der drei Arten sehen. Füge dies zu iris_exploration.py hinzu
```

- Drücken Sie Enter
- Claude aktualisiert das Skript und zeigt Statistiken
- Beachten Sie, wie verschiedene Arten unterschiedliche Messbereiche haben
- Setosa hat viel kleinere Blütenblätter als Virginica

Diese Exploration hilft Ihnen, Muster in den Daten zu verstehen.

Bitten Sie Claude, mit Git zu committen. Oder machen Sie dies selbst in GitHub Desktop.

## Schritt 7: Dritter Vibe - Ein Histogramm erstellen

Zeit, die Daten zu visualisieren.

- Geben Sie im Claude Code-Terminal ein:

```
Erstelle ein Histogramm, das die Verteilung der Blütenblattlängen für alle Blumen zeigt. Verwende 20 Bins. Füge einen Titel und Achsenbeschriftungen hinzu. Speichere das Diagramm als petal_length_histogram.png. Füge diesen Code zu iris_exploration.py hinzu
```

- Drücken Sie Enter
- Claude erstellt den Visualisierungscode
- Eine PNG-Datei erscheint in Ihrem Projektordner
- Öffnen Sie `petal_length_histogram.png`, um das Diagramm zu sehen
- Beachten Sie die zwei Spitzen – dies zeigt, dass die Arten unterschiedliche Blütenblattlängen haben

## Schritt 8: Vierter Vibe - Streudiagramm

Streudiagramme zeigen Beziehungen zwischen zwei Variablen.

- Geben Sie im Claude Code-Terminal ein:

```
Erstelle ein Streudiagramm mit Blütenblattlänge auf der x-Achse und Blütenblattbreite auf der y-Achse. Färbe jeden Punkt nach Art mit verschiedenen Farben ein. Füge eine Legende hinzu, die zeigt, welche Farbe welche Art ist. Speichere als petal_scatter.png. Füge dies zu iris_exploration.py hinzu
```

- Drücken Sie Enter
- Claude erstellt das Streudiagramm
- Öffnen Sie `petal_scatter.png`, um das Ergebnis zu sehen
- Beachten Sie, wie die drei Arten deutliche Cluster bilden
- Setosa (kleine Blütenblätter) ist klar von den anderen getrennt

Das ist Vibe Coding in Aktion: Visualisierung beschreiben, testen, iterieren.

## Schritt 9: Fünfter Vibe - Box-Plot

Box-Plots sind großartig zum Vergleichen von Verteilungen über Gruppen hinweg.

- Geben Sie im Claude Code-Terminal ein:

```
Erstelle einen Box-Plot, der die Blütenblattlängen der drei Arten vergleicht. Setze die Arten auf die x-Achse und die Blütenblattlänge auf die y-Achse. Verwende verschiedene Farben für jede Art. Füge einen Titel hinzu. Speichere als species_boxplot.png. Füge dies zu iris_exploration.py hinzu
```

- Drücken Sie Enter
- Claude fügt den Box-Plot-Code hinzu
- Öffnen Sie `species_boxplot.png`, um den Vergleich zu sehen
- Die Boxen zeigen den Median und die Quartile für jede Art
- Sie können deutlich sehen, dass Virginica die längsten Blütenblätter hat

## Schritt 10: Überprüfen und Committen

Überprüfen Sie vor dem Committen, was Claude erstellt hat.

- Klicken Sie im VS Code Explorer auf `iris_exploration.py`, um es zu öffnen
- Überfliegen Sie den Code – beachten Sie die Imports, das Laden der Daten und die Plotting-Abschnitte
- Sie müssen nicht jede Zeile verstehen, aber bekommen Sie ein Gefühl für die Struktur
- Prüfen Sie, dass alle PNG-Dateien erstellt wurden: `petal_length_histogram.png`, `petal_scatter.png`, `species_boxplot.png`
- Öffnen Sie GitHub Desktop
- Sie sehen alle neuen Dateien aufgelistet (das Python-Skript und die PNG-Bilder)
- Geben Sie im **Summary**-Feld unten links ein:

```
Iris-Datenanalyse mit Histogrammen, Streudiagrammen und Box-Plots
```

- Klicken Sie auf **Commit to main**
- Klicken Sie auf **Push origin**, um auf GitHub zu sichern

Sie haben Ihre erste funktionierende Analyse gespeichert!

## Schritt 11: Iterieren und Verbessern

Vibe Coding glänzt beim Iterieren. Versuchen Sie, Funktionen hinzuzufügen, indem Sie sie beschreiben:

**Beispielanfragen an Claude:**

- "Füge eine Korrelationsmatrix-Heatmap hinzu, die Beziehungen zwischen allen vier Messungen zeigt"
- "Erstelle einen Violin-Plot, der die Kelchblattbreite über die Arten hinweg vergleicht"
- "Berechne und zeige den Korrelationskoeffizienten zwischen Blütenblattlänge und -breite"
- "Füge statistische Testergebnisse hinzu, die Arten vergleichen (ANOVA oder t-Test)"
- "Erstelle einen Pair-Plot, der alle Variablenbeziehungen nach Arten gefärbt zeigt"

Nach jedem erfolgreichen Feature:
- Testen Sie es, indem Sie das Skript ausführen
- Wenn es funktioniert, committen Sie mit GitHub Desktop
- Wenn es nicht funktioniert, sagen Sie Claude den Fehler und bitten Sie um Korrektur
- Wenn behoben, committen Sie die funktionierende Version


**Schlüsselprinzipien:**

- **Beschreiben Sie Ergebnisse, nicht Implementierung** - Sagen Sie "zeige Korrelations-Heatmap", nicht "verwende seaborn.heatmap() mit df.corr()"
- **Iterieren Sie schnell** - Testen → verfeinern → testen → verfeinern
- **Committen Sie funktionierende Versionen** - Speichern Sie jeden Erfolg, bevor Sie neue Funktionen versuchen
- **Akzeptieren Sie Fehlschläge** - Wenn Claudes Code nicht funktioniert, beschreiben Sie einfach den Fehler und bitten Sie um Korrektur
- **Behalten Sie die Kontrolle** - Sie entscheiden über Funktionen, Prioritäten und wann es gut genug ist

Jedes Mal folgen Sie dem Muster: beschreiben → testen → iterieren → committen.

## Nächste Schritte

- **Versuchen Sie andere Datensätze** - Bitten Sie Claude, den Wine-Datensatz, Digits-Datensatz zu verwenden oder eine CSV-Datei zu laden
- **Erkunden Sie weitere Visualisierungen** - Probieren Sie Heatmaps, Pair-Plots oder Violin-Plots
- **Lernen Sie durch Fragen** - Wenn Claude Code schreibt, fragen Sie "erkläre, was diese Zeile macht", um Python zu lernen
- **Wenden Sie es auf Ihre eigenen Daten an** - Verwenden Sie Vibe Coding, um Ihre Forschungs- oder Arbeitsdaten zu analysieren
- **Lesen Sie über Vibe Coding** - Besuchen Sie [IBMs Leitfaden](https://www.ibm.com/think/topics/vibe-coding), um mehr über diesen Programmierstil zu erfahren

## Fehlerbehebung

- **Plot wird nicht angezeigt** - Der Code speichert Plots als PNG-Dateien. Schauen Sie in Ihrem Projektordner und öffnen Sie die Bilddatei direkt in VS Code.
- **Import-Fehler** - Der Docker-Container sollte pandas, matplotlib und scikit-learn vorinstalliert haben. Wenn nicht, bitten Sie Claude, sie mit pip zu installieren.
- **Claude macht Fehler** - Normal! Kopieren Sie die Fehlermeldung, fügen Sie sie bei Claude ein und sagen Sie "behebe diesen Fehler." Vibe Coding beinhaltet Iteration und Debugging.
- **Kann nicht auf GitHub pushen** - Stellen Sie sicher, dass Sie in GitHub Desktop angemeldet sind und das Repository veröffentlicht haben (Schritt 1). Überprüfen Sie Ihre Internetverbindung.
- **Container startet nicht** - Stellen Sie sicher, dass Docker Desktop läuft (grüner Statusanzeiger). Versuchen Sie, auf das grüne Symbol in VS Code zu klicken und **Rebuild Container** zu wählen.

## Workflow-Überblick

Dieses Tutorial kombinierte mehrere Technologien in einem Workflow:

- **GitHub Desktop** - Versionskontrolle mit visueller Oberfläche (Repos erstellen, committen, pushen)
- **Docker-Container** - Isolierte Python-Umgebung mit allen vorinstallierten Abhängigkeiten
- **VS Code** - Code-Editor, der sich mit dem Docker-Container verbindet
- **Claude Code** - KI-Assistent, der Python-Code aus Ihren Beschreibungen schreibt
- **scikit-learn** - Stellt den Iris-Datensatz und Machine-Learning-Tools bereit
- **pandas** - Datenmanipulation und -analyse
- **matplotlib** - Erstellen von Visualisierungen

Die Magie liegt nicht in einem einzelnen Tool – es ist, wie Vibe Coding Sie beschreiben lässt, was Sie wollen, und schnell iterieren. Sie sind von einem leeren Projekt zu einer vollständigen Datenanalyse mit mehreren Visualisierungen in 20 Minuten gekommen, ohne eine einzige Zeile Code manuell zu schreiben.


---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2025.
