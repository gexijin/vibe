[Startseite](./)

# Python-Programmierung in VS Code

Sie möchten Python-Code schreiben, sind sich aber nicht sicher, welchen Editor Sie verwenden sollen, oder Sie suchen nach etwas Leichterem als PyCharm. Stellen Sie sich VS Code als ein Schweizer Taschenmesser vor – es handhabt Python, R, JavaScript und viele andere Sprachen in einem leichtgewichtigen Editor. Dieses Tutorial zeigt Ihnen, wie Sie Python in VS Code mit intelligenten Funktionen wie Codevervollständigung, interaktivem Debugging und sogar Web-Apps einrichten.

## Wichtige Konzepte

- **[Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - VS Code-Erweiterung von Microsoft, die Syntax-Hervorhebung, Debugging, Codeausführung und Jupyter-Notebook-Unterstützung bietet
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - Sprachserver, der schnelle IntelliSense, Typprüfung und Auto-Imports für Python ermöglicht
- **[Virtuelle Umgebung](https://docs.python.org/3/library/venv.html)** - Isolierte Python-Umgebung zur Verwaltung projektspezifischer Pakete ohne Beeinträchtigung des System-Python
- **[Streamlit](https://streamlit.io/)** - Python-Bibliothek zur Erstellung interaktiver Web-Apps mit einfachen Python-Skripten

## Was Sie benötigen

- Abgeschlossenes Tutorial [VS Code Grundlagen](./VS_Code_Getting_Started)
- Internetverbindung zum Herunterladen von Python und Paketen
- 15-20 Minuten

## Schritt 1: Python installieren

Sie benötigen Python 3.8 oder höher für die beste Kompatibilität mit modernen Paketen.

- **Windows**:
  - Laden Sie das neueste Python von [python.org](https://www.python.org/downloads/) herunter
  - Führen Sie das Installationsprogramm aus
  - **Aktivieren Sie das Kontrollkästchen „Add python.exe to PATH"** bevor Sie auf Install Now klicken
  - Notieren Sie den Installationsort (typischerweise `C:\Users\IhrName\AppData\Local\Programs\Python\Python312`)

- **macOS**:
  - Laden Sie von [python.org](https://www.python.org/downloads/) herunter und führen Sie das Installationsprogramm aus
  - Oder verwenden Sie Homebrew: Öffnen Sie Terminal und geben Sie `brew install python` ein
  - Homebrew-Pfad: `/opt/homebrew/bin/python3` (Apple Silicon) oder `/usr/local/bin/python3` (Intel)

- **Linux**:
  - Python ist normalerweise vorinstalliert. Überprüfen Sie die Version mit `python3 --version`
  - Falls nötig, installieren Sie über den Paketmanager: `sudo apt install python3 python3-pip python3-venv` (Ubuntu/Debian)

Überprüfen Sie die Installation, indem Sie ein Terminal öffnen und `python3 --version` oder `python --version` eingeben.

## Schritt 2: Python-Erweiterungen in VS Code installieren

- Öffnen Sie VS Code
- Klicken Sie auf das **Extensions**-Symbol in der linken Seitenleiste (oder klicken Sie auf **View > Extensions**)
- Suchen Sie nach `ms-python.python` und klicken Sie auf **Install** bei der Python-Erweiterung von Microsoft
- Pylance sollte automatisch mit der Python-Erweiterung installiert werden. Falls nicht, suchen Sie nach `ms-python.vscode-pylance` und installieren Sie es

Die Python-Erweiterung enthält Unterstützung für Debugging, IntelliSense, Code-Formatierung und Jupyter-Notebooks.

## Schritt 3: Ihr Python-Projekt erstellen

- Erstellen Sie einen neuen Ordner auf Ihrem Computer (z.B. `mein-python-projekt`)
- Klicken Sie in VS Code auf **File > Open Folder** und wählen Sie Ihren neuen Ordner
- Klicken Sie im oberen Menü auf **File > New File**
- Speichern Sie die Datei als `analysis.py` durch Klicken auf **File > Save**

## Schritt 4: Python-Interpreter auswählen

VS Code muss wissen, welche Python-Installation verwendet werden soll.

- Klicken Sie in der Menüleiste auf **View**, dann auf **Command Palette**
- Geben Sie `Python: Select Interpreter` ein und wählen Sie es aus
- Wählen Sie die Python-Version, die Sie installiert haben (z.B. `Python 3.12.x` oder ähnlich)
- Der ausgewählte Interpreter erscheint in der unteren rechten Ecke von VS Code

Wenn Sie Ihre Python-Installation nicht sehen, klicken Sie auf **Enter interpreter path** und navigieren Sie dorthin, wo Python installiert ist.

## Schritt 5: Eine virtuelle Umgebung erstellen

Virtuelle Umgebungen halten Ihre Projektabhängigkeiten isoliert.

- Klicken Sie in der Menüleiste auf **View**, dann auf **Command Palette**
- Geben Sie `Python: Create Environment` ein und wählen Sie es aus
- Wählen Sie **Venv** (eingebaute virtuelle Umgebung)
- Wählen Sie Ihren Python-Interpreter aus der Liste
- Warten Sie, bis VS Code die Umgebung erstellt hat (Sie sehen einen `.venv`-Ordner erscheinen)
- VS Code aktiviert diese Umgebung automatisch für Ihr Projekt

Sie sehen `(.venv)` in Ihrer Terminal-Eingabeaufforderung, wenn die Umgebung aktiv ist.

## Schritt 6: Erforderliche Pakete installieren

- Öffnen Sie ein neues Terminal in VS Code durch Klicken auf **View > Terminal**
- Das Terminal sollte `(.venv)` anzeigen, was darauf hinweist, dass Ihre virtuelle Umgebung aktiv ist
- Installieren Sie Pakete durch Eingabe dieser Befehle:

```bash
pip install pandas matplotlib streamlit
```

- Warten Sie, bis die Installation abgeschlossen ist (kann 1-2 Minuten dauern)

Wenn `(.venv)` nicht erscheint, ist die Umgebung nicht aktiv. Klicken Sie auf **View > Command Palette**, führen Sie `Python: Select Interpreter` aus und wählen Sie dann den Interpreter mit `('.venv': venv)` daneben.

## Schritt 7: Ihr erstes Python-Skript schreiben

Geben Sie diesen Code in `analysis.py` ein:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Iris-Datensatz laden
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Erste Zeilen anzeigen
print(iris.head())

# Zusammenfassende Statistiken generieren
print("\nSummary Statistics:")
print(iris.describe())

# Histogramm erstellen
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- Speichern Sie die Datei durch Klicken auf **File > Save**

## Schritt 8: Python-Code interaktiv ausführen

- Mit geöffneter `analysis.py` klicken Sie auf die Schaltfläche **▶ Run Python File** in der oberen rechten Ecke
- Oder klicken Sie mit der rechten Maustaste im Editor und wählen Sie **Run Python File in Terminal**
- Beobachten Sie die Ausgabe im Terminal-Panel
- Ein Histogramm-Fenster öffnet sich und zeigt Ihren Plot
- Sie können auch bestimmte Zeilen auswählen und `Shift+Enter` drücken, um nur diese Zeilen in einer interaktiven Python-Sitzung auszuführen

## Schritt 9: Eine einfache Streamlit-App erstellen

- Erstellen Sie eine neue Datei: **File > New File**
- Speichern Sie sie als `app.py`
- Geben Sie diesen Code ein:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# Seitenleisten-Schieberegler
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# Daten laden
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Histogramm erstellen
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# In Streamlit anzeigen
st.pyplot(fig)
```

- Speichern Sie die Datei
- Öffnen Sie das Terminal und führen Sie aus:

```bash
streamlit run app.py
```

- Die App öffnet sich in Ihrem Browser (normalerweise unter `http://localhost:8501`)
- Bewegen Sie den Schieberegler in der Seitenleiste und beobachten Sie, wie sich das Histogramm sofort aktualisiert
- Drücken Sie `Strg+C` im Terminal, um die App zu stoppen

## Schritt 10: Codevervollständigung und IntelliSense verwenden

- In `analysis.py` beginnen Sie auf einer neuen Zeile `iris.` zu tippen
- Ein Dropdown erscheint mit allen verfügbaren Methoden und Attributen
- Geben Sie `iris.gr` ein und beobachten Sie, wie es `groupby()` vorschlägt
- Bewegen Sie Ihre Maus über `pd.read_csv` in Ihrem bestehenden Code
- Ein Popup zeigt Funktionssignatur, Parameter und Dokumentation
- Versuchen Sie `import ` zu tippen und beobachten Sie, wie VS Code Paketnamen vorschlägt
- Wenn Sie einen Funktionsaufruf eingeben, zeigt IntelliSense Parameter-Hinweise an

## Schritt 11: Debugging ausprobieren

- In `analysis.py` klicken Sie links neben Zeilennummer 8 (die Zeile `print(iris.head())`), um einen Breakpoint zu setzen (roter Punkt erscheint)
- Klicken Sie in der Menüleiste auf **Run**, dann auf **Start Debugging**
- Wählen Sie **Python File**, wenn Sie dazu aufgefordert werden
- Die Codeausführung pausiert am Breakpoint
- Verwenden Sie die Debug-Symbolleiste, um durch den Code zu schreiten, Variablen zu inspizieren und den Aufrufstapel zu sehen
- Klicken Sie auf **Run > Continue**, um die Ausführung fortzusetzen

## Nächste Schritte

- Erkunden Sie [pandas](https://pandas.pydata.org/) für Datenmanipulation und -analyse
- Lernen Sie [Jupyter-Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) in VS Code für interaktive Data Science
- Probieren Sie [Flask](https://flask.palletsprojects.com/) oder [FastAPI](https://fastapi.tiangolo.com/) zum Erstellen von Web-APIs
- Installieren Sie [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) für automatische Code-Formatierung
- Verwenden Sie [pytest](https://docs.pytest.org/) zum Schreiben und Ausführen von Tests

## Fehlerbehebung

- **„Python is not recognized" im Terminal**: Python ist nicht in Ihrem System-PATH. Unter Windows installieren Sie Python neu und aktivieren Sie „Add python.exe to PATH". Unter Mac/Linux verwenden Sie `python3` statt `python`. Starten Sie VS Code nach der Korrektur neu.

- **Kein Interpreter gefunden**: Klicken Sie auf den Interpreter-Selektor in der unteren rechten Ecke von VS Code, oder klicken Sie auf **View > Command Palette** und führen Sie `Python: Select Interpreter` aus. Wenn Ihre Python-Installation nicht erscheint, wählen Sie **Enter interpreter path** und navigieren Sie zu Ihrer Python-Ausführungsdatei.

- **Virtuelle Umgebung wird nicht aktiviert**: VS Code sollte sie automatisch aktivieren, wenn Sie ein Terminal öffnen. Falls nicht, aktivieren Sie manuell: Windows: `.venv\Scripts\activate`, Mac/Linux: `source .venv/bin/activate`. Überprüfen Sie durch `(.venv)` in Ihrer Terminal-Eingabeaufforderung.

- **IntelliSense funktioniert nicht**: Stellen Sie sicher, dass Pylance installiert und aktiviert ist. Überprüfen Sie, ob in der unteren rechten Ecke Ihr ausgewählter Interpreter angezeigt wird. Warten Sie 10-20 Sekunden nach dem Öffnen einer Datei, bis Pylance initialisiert ist. Starten Sie VS Code neu, wenn Probleme bestehen bleiben.

- **pip install schlägt fehl**: Stellen Sie sicher, dass Ihre virtuelle Umgebung aktiviert ist (suchen Sie nach `(.venv)` im Terminal). Unter Linux müssen Sie möglicherweise zuerst `python3-venv` installieren. Unter Windows überprüfen Sie, ob kein Antivirenprogramm pip blockiert.

- **Streamlit-App wird nicht ausgeführt**: Stellen Sie sicher, dass streamlit in Ihrer virtuellen Umgebung installiert ist (`pip list | grep streamlit`). Überprüfen Sie das Terminal auf Fehlermeldungen. Stellen Sie sicher, dass keine andere App Port 8501 verwendet.

## Workflow-Zusammenfassung

VS Code bietet eine moderne, leichtgewichtige Umgebung für Python-Entwicklung mit diesen Vorteilen:

- **Vereinheitlichte Umgebung**: Programmieren Sie Python, R, JavaScript und mehr in einem Editor
- **Leistungsstarke IntelliSense**: Intelligente Vervollständigungen, Typprüfung und Auto-Imports über Pylance
- **Integriertes Debugging**: Setzen Sie Breakpoints, inspizieren Sie Variablen und schreiten Sie durch Code
- **Jupyter-Unterstützung**: Führen Sie Notebooks direkt in VS Code ohne separate Anwendungen aus
- **Versionskontrolle**: Eingebaute Git-Integration zum Verfolgen von Änderungen
- **Erweiterungs-Ökosystem**: Tausende Erweiterungen für Tests, Formatierung, Linting und mehr

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
