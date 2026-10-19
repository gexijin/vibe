---
title: "Claude Code für Python in VS Code auf dem Mac verwenden"
lang: "de"
---
[Startseite](./)

# Claude Code für Python in VS Code auf dem Mac verwenden

Sie haben Python in VS Code eingerichtet und können Code manuell schreiben. Jetzt möchten Sie, dass KI Ihnen hilft, Ihren Python-Code zu schreiben, zu verbessern und zu debuggen, während Sie sich auf die Analyse konzentrieren. Stellen Sie sich Claude Code als Programmierpartner vor, der in VS Code lebt – Sie beschreiben, was Sie möchten, und er schreibt oder verbessert den Code, während Sie im selben Fenster bleiben.

## Wichtige Konzepte

- **[Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - VS Code-Erweiterung, die den Claude KI-Assistenten direkt in Ihren Editor bringt, mit Inline-Code-Bearbeitungen
- **Chat-Panel** - Seitenpanel in VS Code, in dem Sie mit Claude über Ihren Code kommunizieren
- **Inline-Bearbeitungen** - Claudes vorgeschlagene Codeänderungen erscheinen direkt in Ihren Dateien mit Diffs, die Sie akzeptieren oder ablehnen können

## Was Sie benötigen

- Abgeschlossenes Tutorial [Python in VS Code](./Python_Coding_VS_Code_Guide) - Python sollte in VS Code funktionieren
- Abgeschlossenes Tutorial [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS) - Claude Code CLI sollte installiert sein
- Ein kostenpflichtiger Claude-Plan (z. B. Pro oder Max) oder ein Anthropic-Console-Konto – der kostenlose Plan enthält Claude Code nicht
- 20-30 Minuten

## Schritt 1: VS Code öffnen und Python-Projekt erstellen

- Öffnen Sie **Visual Studio Code**
- Klicken Sie in der Menüleiste auf **File**, dann auf **Open Folder**
- Navigieren Sie zu Ihrem **Dokumente**-Ordner
- Klicken Sie unten im Dialog auf **Neuer Ordner**
- Nennen Sie den Ordner `claude_python_test`
- Klicken Sie auf **Öffnen** (englisch: **Open**), um den neuen Ordner zu öffnen
- Wenn Sie gefragt werden „Do you trust the authors?“, klicken Sie auf **Yes, I trust the authors**

## Schritt 2: Claude Code Extension installieren und anmelden

- Klicken Sie auf das **Extensions**-Symbol in der linken Seitenleiste (Symbol mit vier Quadraten)
- Geben Sie im Suchfeld `Claude Code` ein
- Finden Sie **Claude Code for VS Code** von Anthropic und klicken Sie auf **Install**
- Klicken Sie nach der Installation unten rechts im VS Code-Fenster (in der Statusleiste) auf **✻ Claude Code**, um das Claude-Panel zu öffnen
- Beim ersten Mal erscheint ein Anmeldebildschirm: Klicken Sie auf **Sign in**, bestätigen Sie den Zugriff in Ihrem Browser und kehren Sie dann zu VS Code zurück
- Für detaillierte Authentifizierungsschritte siehe die Anleitung [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS) (Schritt 3)
- Nach der Anmeldung sehen Sie im Panel eine Checkliste **Learn Claude Code** und unten ein Eingabefeld

## Schritt 3: Erstes Python-Skript manuell erstellen

- Klicken Sie in der Menüleiste auf **File > New File...**
- Wählen Sie in der Liste, die oben im Fenster erscheint, **Python File**
- Speichern Sie die Datei durch Klicken auf **File > Save**, nennen Sie sie `iris_analysis.py`
- Geben Sie diesen Code ein:

```python
from sklearn import datasets
import pandas as pd

# Load iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

# Display structure
iris_df.info()
print("\nSummary statistics:")
print(iris_df.describe())
```

- Speichern Sie die Datei durch Klicken auf **File > Save**
- Erstellen Sie eine virtuelle Umgebung wie in Schritt 5 von [Python-Programmierung in VS Code](./Python_Coding_VS_Code_Guide): Klicken Sie auf **View > Command Palette**, geben Sie `Python: Create Environment` ein, wählen Sie **Venv** und dann Ihre Python-Version
- Warten Sie, bis der Ordner `.venv` im Explorer erscheint
- Öffnen Sie ein Terminal: Klicken Sie in der Menüleiste auf **View**, dann auf **Terminal**. Am Anfang der Eingabezeile sollte `(.venv)` stehen
- Installieren Sie die Pakete, die dieses Skript benötigt:
  ```
  pip install scikit-learn pandas
  ```
- Führen Sie im Terminal aus: `python iris_analysis.py`
- Sie sollten die Datensatzstruktur und zusammenfassende Statistiken im Terminal sehen

## Schritt 4: Claude bitten, ein Streudiagramm hinzuzufügen

- Öffnen Sie das Claude-Panel (Spark-Symbol oben rechts in der geöffneten Datei oder **✻ Claude Code** unten rechts)
- Geben Sie im Chat-Feld unten ein:

```
Füge Code zu iris_analysis.py hinzu, um ein Streudiagramm der Kelchblattlänge gegen die Kelchblattbreite zu erstellen, nach Art eingefärbt. Verwende seaborn.
```

- Drücken Sie Enter zum Senden
- Claude liest Ihre Datei und bearbeitet sie – der neue Code erscheint in `iris_analysis.py`
- Wenn Claude ein Diff zeigt und um Erlaubnis fragt, nehmen Sie die Änderung an
- Der seaborn/matplotlib-Code erscheint in Ihrer Datei
- Installieren Sie die Diagramm-Pakete, die Claudes Code verwendet (sie wurden in Schritt 3 nicht installiert). Führen Sie im Terminal (mit `(.venv)` am Anfang der Zeile) aus:
  ```
  pip install seaborn matplotlib
  ```

## Schritt 5: Den aktualisierten Code ausführen

- Führen Sie im Terminal aus: `python iris_analysis.py`
- Ein Streudiagramm-Fenster erscheint
- Sie sollten Punkte sehen, die nach Art gefärbt sind (setosa, versicolor, virginica)
- Schließen Sie das Plot-Fenster, um fortzufahren

## Schritt 6: Claude bitten, das Diagramm zu verfeinern

- Geben Sie im Claude-Chat-Panel ein:

```
Entferne den Titel. Verwende für jede Art eine andere Markerform. Wechsle zum whitegrid-Stil.
```

- Drücken Sie Enter
- Claude aktualisiert den Code
- Nehmen Sie die Änderung an, falls Sie gefragt werden
- Führen Sie den aktualisierten Code erneut aus: `python iris_analysis.py` im Terminal
- Das Diagramm zeigt jetzt verschiedene Markerformen pro Art, keinen Titel und whitegrid-Stil
- Schließen Sie das Plot-Fenster, um fortzufahren

## Schritt 7: Claude um PCA-Analyse bitten

- Geben Sie im Claude-Chat-Panel ein:

```
Füge Code hinzu, um eine PCA auf den numerischen Variablen durchzuführen und die Proben mit den ersten beiden Hauptkomponenten zu plotten.
```

- Drücken Sie Enter
- Claude fügt PCA-Code zu Ihrem Skript hinzu
- Nehmen Sie die Änderung an, falls Sie gefragt werden
- Führen Sie den Code aus: `python iris_analysis.py` im Terminal
- Ein PCA-Plot erscheint, der Proben auf PC1 und PC2 projiziert zeigt, gefärbt nach Art (wenn sich zuerst das Streudiagramm-Fenster aus Schritt 6 öffnet, schließen Sie es – danach erscheint der PCA-Plot)
- Schließen Sie das Plot-Fenster, wenn Sie fertig sind

## Schritt 8: Claude um Überprüfung und Kommentare bitten

- Geben Sie im Claude-Chat-Panel ein:

```
Überprüfe das gesamte Skript auf Korrektheit. Füge Kommentare hinzu, wenn nötig.
```

- Drücken Sie Enter
- Claude überprüft den Code und fügt Kommentare hinzu, die jeden Abschnitt erklären
- Nehmen Sie die Änderung an, falls Sie gefragt werden
- Ihr Skript hat jetzt klare Kommentare, die das Laden der Daten, die Visualisierung und die PCA-Analyse erklären

## Nächste Schritte

- Bitten Sie Claude, ein Jupyter-Notebook zu erstellen: „Konvertiere dies in ein Jupyter-Notebook“
- Verwenden Sie Claude, um Fehler zu debuggen: „Dieser Code gibt Fehler X, kannst du ihn beheben?“
- Fordern Sie statistische Tests an: „Füge einen t-Test hinzu, der die Kelchblattlänge zwischen setosa und versicolor vergleicht“
- Bitten Sie Claude, Code zu optimieren: „Mache diesen Code effizienter mit numpy-Vektorisierung“
- Holen Sie Hilfe bei unbekannten Funktionen: „Erkläre, was pandas.groupby macht“

## Fehlerbehebung

- **Claude-Erweiterung wird nicht angezeigt** - Starten Sie VS Code nach der Installation neu. Klicken Sie auf **View > Extensions**, um zu überprüfen, ob sie installiert ist.
- **Fehler „Cannot read Python file“** - Stellen Sie sicher, dass Sie die Datei mit der Erweiterung `.py` gespeichert haben. Claude benötigt gespeicherte Dateien, um sie zu lesen.
- **Authentifizierung fehlgeschlagen** - Überprüfen Sie, ob Ihr kostenpflichtiger Claude-Plan oder Ihr Anthropic-Console-Konto aktiv ist. Siehe [Claude Code auf dem Mac installieren](./Install_Claude_Code_MacOS) für Fehlerbehebung bei der Authentifizierung.
- **Fehler „Paket nicht gefunden“** oder **`command not found: python`** - Stellen Sie sicher, dass das Terminal `(.venv)` anzeigt (falls nicht, schließen Sie es und öffnen Sie mit **View > Terminal** ein neues), und installieren Sie dann die erforderlichen Pakete: `pip install seaborn matplotlib scikit-learn pandas`. Warten Sie, bis die Installation abgeschlossen ist, bevor Sie den Code ausführen.
- **Codeänderungen werden nicht übernommen** - Wenn Claude um Erlaubnis gefragt hat, stellen Sie sicher, dass Sie die Änderung angenommen haben. Wenn es nicht funktioniert, versuchen Sie, Claudes vorgeschlagenen Code manuell zu kopieren.
- **Plot wird nicht angezeigt** - Stellen Sie sicher, dass ein Bildschirm verfügbar ist. Auf manchen Systemen müssen Sie möglicherweise `plt.show()` am Ende hinzufügen oder `%matplotlib inline` in Jupyter verwenden.

## Workflow-Zusammenfassung

- **Claude Code Extension** bietet einen KI-Assistenten direkt in VS Code mit Chat-Panel und Inline-Diffs
- **Iterative Verfeinerung** - Beginnen Sie mit einfachem Code, bitten Sie Claude um Verbesserungen, testen Sie sofort, dann verfeinern Sie weiter
- **Kontextbewusstsein** - Claude liest Ihre Python-Dateien und versteht Ihre Projektstruktur
- **Inline-Bearbeitung** - Vorgeschlagene Änderungen erscheinen als Diffs in Ihren tatsächlichen Dateien, nicht als separate Chat-Antworten
- **Im Flow bleiben** - Kein Wechseln zwischen Browser und Editor – alles passiert in VS Code

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 11. Dezember 2025.
