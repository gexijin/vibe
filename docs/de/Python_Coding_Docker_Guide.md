---
title: "Python-Programmierung in VS Code über Docker-Container"
lang: "de"
---
[Startseite](./)

# Python-Programmierung in VS Code über Docker-Container

Haben Sie schon einmal versucht, Ihren Python-Code mit einem Kollegen zu teilen, nur um dann Stunden mit dem Debuggen von „aber auf meinem Rechner läuft es doch“-Problemen zu verbringen? Docker-Container sind wie Frachtcontainer für Code – sie verpacken Ihre Python-Umgebung, Bibliotheken und Abhängigkeiten in eine versiegelte Box, die überall gleich funktioniert. Außerdem erhalten Sie Zugang zu Zehntausenden von vorgefertigten Images auf [Docker Hub](https://hub.docker.com/), wo Softwareentwickler fertige Umgebungen veröffentlichen und Ihnen den Schmerz manueller Softwareinstallation ersparen. Dieses Tutorial zeigt Ihnen, wie Sie Python in einer isolierten, reproduzierbaren Umgebung mit VS Code und Docker Desktop ausführen.

## Wichtige Konzepte

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Anwendung, die Container auf Ihrem Computer ausführt und isolierte Umgebungen verwaltet
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code-Funktion, die es Ihnen ermöglicht, innerhalb eines Docker-Containers mit voller IDE-Unterstützung zu programmieren
- **Container-Isolation** - Ihr Code läuft in einer separaten Linux-Umgebung, die nur Ihren Projektordner sieht, nicht Ihren gesamten Computer
- **[Offizielle Python-Images](https://hub.docker.com/_/python)** - Vorgefertigte Docker-Images mit Python und wichtigen Tools vorinstalliert

## Was Sie benötigen

- Abgeschlossenes Tutorial [Python-Programmierung in VS Code](./Python_Coding_VS_Code_Guide)
- 20-25 Minuten

## Schritt 1: Docker Desktop installieren

- Besuchen Sie die [Docker Desktop Download-Seite](https://www.docker.com/products/docker-desktop/)
- Klicken Sie auf **Download Docker Desktop** und wählen Sie Ihr System (Windows, oder Mac - Apple Silicon für Macs mit M1/M2/M3/M4, oder Mac - Intel Chip für ältere Macs)
- Führen Sie das Installationsprogramm aus und folgen Sie dem Assistenten
- Wenn Sie dazu aufgefordert werden, aktivieren Sie WSL 2 (Windows-Benutzer) oder akzeptieren Sie die Standardeinstellungen
- Starten Sie Docker Desktop nach der Installation
- Warten Sie, bis die Docker-Engine gestartet ist (Sie sehen einen grünen Statusanzeiger unten links)

## Schritt 2: Dev Containers-Erweiterung installieren

- Öffnen Sie VS Code
- Klicken Sie auf das **Extensions**-Symbol in der linken Seitenleiste (oder klicken Sie auf **View > Extensions**)
- Geben Sie `dev containers` in das Suchfeld ein
- Finden Sie **Dev Containers** von Microsoft
- Klicken Sie auf **Install**

## Schritt 3: Python-Projektordner erstellen

- Erstellen Sie einen neuen Ordner auf Ihrem Computer namens `python-docker-demo`
- Klicken Sie in VS Code auf **File > Open Folder**
- Navigieren Sie zum Ordner `python-docker-demo`, den Sie gerade erstellt haben
- Klicken Sie auf **Ordner auswählen** (Windows) oder **Öffnen** (Mac) – bei englischer Anzeige heißen die Schaltflächen **Select Folder** bzw. **Open**
- Bewegen Sie in der Explorer-Seitenleiste die Maus über die Überschrift **PYTHON-DOCKER-DEMO**, klicken Sie auf das Symbol **New Folder** und nennen Sie den Ordner `.devcontainer`
- Klicken Sie in der Explorer-Seitenleiste auf eine leere Stelle unterhalb von `.devcontainer`, sodass nichts markiert ist, klicken Sie dann erneut auf das Symbol **New Folder** und nennen Sie den Ordner `python`
- Ihre Struktur sollte so aussehen: `python-docker-demo/.devcontainer/` und `python-docker-demo/python/`

Wir erstellen diese Ordner in VS Code, weil der Finder auf dem Mac keinen Ordnernamen erlaubt, der mit einem Punkt (`.`) beginnt.

## Schritt 4: Die Dockerfile erstellen

- Klicken Sie in der Explorer-Seitenleiste mit der rechten Maustaste auf den `.devcontainer`-Ordner
- Klicken Sie auf **New File**
- Nennen Sie sie `Dockerfile`
- Fügen Sie folgenden Inhalt ein:

```dockerfile
# Choose the official Python slim image
FROM python:3.12-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Install Python packages for data science and web apps
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally (newer npm blocks its setup script unless allowed)
RUN npm config set allow-scripts=@anthropic-ai/claude-code --location=global \
    && npm install -g @anthropic-ai/claude-code

# 5. Expose Streamlit port
EXPOSE 8501
```

- Klicken Sie auf **File > Save**

## Schritt 5: Die Dev Container-Konfiguration erstellen

- Erstellen Sie im `.devcontainer`-Ordner eine neue Datei namens `devcontainer.json`
- Fügen Sie folgenden Inhalt ein:

```json
{
  "name": "Python in Docker",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy"
      ]
    }
  },
  "forwardPorts": [8501],
  "postCreateCommand": "python3 --version"
}
```

- Klicken Sie auf **File > Save**

## Schritt 6: Ein Python-Datenanalyse-Skript erstellen

- Erstellen Sie im `python`-Ordner eine neue Datei namens `iris_analysis.py`
- Fügen Sie folgenden Inhalt ein:

```python
# Simple data analysis using the iris dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Sepal Length')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Sepal Width')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Iris Sepal Measurements')
plt.legend()
plt.savefig('iris_histogram.png')
```

- Klicken Sie auf **File > Save**

## Schritt 7: Eine Streamlit-Web-App erstellen

- Erstellen Sie im `python`-Ordner eine neue Datei namens `app.py`
- Fügen Sie folgenden Inhalt ein:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geyser Data")

# Slider for number of bins
bins = st.slider("Number of bins:", min_value=5, max_value=50, value=30)

# Generate sample data (simulating Old Faithful eruption durations)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Create histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Eruption Duration (minutes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram with {bins} bins')

st.pyplot(fig)
```

- Klicken Sie auf **File > Save**

## Schritt 8: Im Container erneut öffnen

- Klicken Sie auf das Symbol **><** in der unteren linken Ecke von VS Code
- Wählen Sie **Reopen in Container** aus dem Menü
- VS Code baut den Container (dies dauert beim ersten Mal 5-10 Minuten)
- Sie sehen eine Fortschrittsanzeige mit den Build-Schritten
- Nach Abschluss steht in der unteren linken Ecke **Dev Container: Python in Docker**

## Schritt 9: Die Container-Umgebung verstehen

Jetzt programmieren Sie innerhalb eines Linux-Containers. Lassen Sie uns erkunden, was das bedeutet.

- Klicken Sie auf **Terminal > New Terminal**, um ein Terminal innerhalb des Containers zu öffnen
- Überprüfen Sie Ihren aktuellen Standort:

```bash
pwd
```

Sie sehen `/workspaces/python-docker-demo` – das ist Ihr Projektordner innerhalb des Containers.

- Listen Sie die Dateien auf:

```bash
ls -a
```

Sie sehen die Ordner, die Sie erstellt haben: `.devcontainer/`, `python/`, usw. (`-a` zeigt auch Ordner an, deren Name mit einem Punkt beginnt)

- Versuchen Sie, ein Verzeichnis nach oben zu gehen:

```bash
cd ..
ls
```

Sie sehen nur `python-docker-demo/` – der Container ist isoliert. Sie können nicht auf die anderen Ordner, den Desktop oder die Dokumente Ihres Computers zugreifen. Diese Isolation stellt sicher, dass Ihre Python-Umgebung sauber und reproduzierbar ist.

- Kehren Sie zum Projektordner zurück:

```bash
cd python-docker-demo
```

## Schritt 10: Python-Code Zeile für Zeile ausführen

Der Container hat Python mit Data-Science-Paketen vorinstalliert. Führen wir das Analyseskript aus.

- Navigieren Sie im VS Code Explorer zu `python/iris_analysis.py`
- Klicken Sie zum Öffnen der Datei
- Klicken Sie in Zeile 2, `import pandas as pd` (Zeile 1 ist nur ein Kommentar)
- Drücken Sie `Shift+Enter`, um sie in einem interaktiven Python-Terminal auszuführen
- Ein Python-Terminal öffnet sich unten
- Fahren Sie fort, jede Zeile oder jeden Block einzeln mit `Shift+Enter` auszuführen
- Wenn Sie `print(df.head())` ausführen, sehen Sie die ersten 5 Zeilen im Terminal
- Wenn Sie `print(df.describe())` ausführen, sehen Sie statistische Zusammenfassungen
- Wenn Sie den Histogramm-Code ausführen, wird das Diagramm als `iris_histogram.png` in Ihrem Projektordner gespeichert (der Container hat keinen Bildschirm, daher können Diagramme nicht in einem Fenster geöffnet werden) – klicken Sie in der Explorer-Seitenleiste auf die Datei, um sie anzusehen

## Schritt 11: Die Streamlit-App ausführen

Das Projekt enthält eine Demo-Streamlit-App, die ein interaktives Histogramm erstellt.

- Navigieren Sie im VS Code Explorer zu `python/app.py`
- Klicken Sie zum Öffnen der Datei
- Öffnen Sie ein neues Terminal (**Terminal > New Terminal**)
- Führen Sie die App aus:

```bash
cd python
streamlit run app.py
```

- Die App startet und zeigt eine URL an: `http://localhost:8501`
- Eine Benachrichtigung erscheint: **Open in Browser**
- Klicken Sie auf **Open in Browser**
- Die Streamlit-App öffnet sich in Ihrem Webbrowser
- Bewegen Sie den Schieberegler, um die Histogramm-Bins zu ändern – das Diagramm aktualisiert sich in Echtzeit

## Schritt 12: Eine einfache Änderung vornehmen

Lassen Sie uns die App modifizieren, um zu sehen, wie Entwicklung funktioniert.

- Lassen Sie die App laufen
- Bearbeiten Sie in VS Code `python/app.py`
- Finden Sie Zeile 5: `st.title("Old Faithful Geyser Data")`
- Ändern Sie sie zu:

```python
st.title("My First Python Docker App")
```

- Klicken Sie auf **File > Save**
- Kehren Sie zu Ihrem Browser zurück
- Klicken Sie auf **Always rerun** in der oberen rechten Ecke
- Der Titel zeigt jetzt Ihren benutzerdefinierten Text

## Schritt 13: Die Dockerfile verstehen (Optional)

- Navigieren Sie im VS Code Explorer zu `.devcontainer/Dockerfile`
- Klicken Sie zum Öffnen der Datei
- Sie sehen die vollständige Konfiguration

**Wichtige Teile:**

- `FROM python:3.12-slim` - Offizielles Python 3.12 Basis-Image (schlankes, Debian-basiertes Image)
- `RUN apt-get install` - Linux-Systembibliotheken zum Erstellen von Python-Paketen
- `RUN pip install --no-cache-dir ...` - Installiert Python-Pakete permanent
- `RUN curl... && apt-get install -y nodejs` - Installiert Node.js und npm, mit denen die nächste Zeile Claude Code installiert
- `RUN npm config set allow-scripts=... && npm install -g @anthropic-ai/claude-code` - Installiert Claude Code global für KI-Unterstützung (der erste Teil lässt Claude Code seine Einrichtung abschließen, die neuere npm-Versionen sonst blockieren)
- `EXPOSE 8501` - Öffnet Port 8501 für Streamlit-Apps

**Andere Python-Images, die Sie verwenden können:**

- `python:3.12` - Vollständiges Python-Image mit mehr Tools (größere Dateigröße)
- `python:3.12-slim` - Leichtgewichtiges Image mit Python und pip (das verwenden wir)
- `python:3.12-alpine` - Minimales Alpine Linux-basiertes Image (kleinste Dateigröße)
- `quay.io/jupyter/datascience-notebook` - Vorkonfiguriertes Jupyter mit Data-Science-Bibliotheken

Nach der Änderung des Basis-Images müssen Sie den Container neu erstellen, um die Änderungen anzuwenden. Hinweis: Mit dieser Dockerfile funktionieren nur Debian-basierte Images wie `python:3.12` und `python:3.12-slim`; Alpine- und Jupyter-Images brauchen eine andere Dockerfile.

## Schritt 14: Python-Pakete im Docker-Image installieren (Optional)

Pakete, die über pip im Terminal installiert werden (`pip install package`), sind temporär und verschwinden, wenn Sie den Container neu erstellen. Um Pakete permanent zu machen, fügen Sie sie zur Dockerfile hinzu.

- Navigieren Sie im VS Code Explorer zu `.devcontainer/Dockerfile`
- Klicken Sie zum Öffnen der Datei
- Finden Sie Zeile 10: `RUN pip install --no-cache-dir ...`
- Fügen Sie `plotly` zur Liste hinzu:

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn plotly
```

- Klicken Sie auf **File > Save**
- Klicken Sie auf das Symbol **><** in der unteren linken Ecke
- Wählen Sie **Rebuild Container** aus dem Menü
- VS Code erstellt den Container mit Ihrem neuen Paket neu (dies dauert 2-5 Minuten)
- Um es zu überprüfen, öffnen Sie ein Terminal (**Terminal > New Terminal**) und führen Sie aus:

```bash
python -c "import plotly; print(plotly.__version__)"
```

Wenn die Version ohne Fehler angezeigt wird, ist das Paket dauerhaft installiert.

## Nächste Schritte

- **Erstellen Sie ein neues Python-Skript** - Erstellen Sie eine neue `.py`-Datei im `python/`-Ordner, schreiben Sie Datenanalyse-Code mit eingebauten Datensätzen oder laden Sie Ihre eigenen CSV-Dateien
- **Installieren Sie Python-Pakete** - Fügen Sie Pakete hinzu, die Sie benötigen, indem Sie die Dockerfile (Zeile 10) bearbeiten und den Container neu erstellen
- **Erkunden Sie Data Science** - Probieren Sie Datenmanipulation mit pandas und Visualisierung mit matplotlib oder seaborn
- **Erstellen Sie Web-Apps** - Erstellen Sie interaktive Dashboards mit Streamlit oder Flask

## Fehlerbehebung

- **Docker Desktop läuft nicht** - Öffnen Sie Docker Desktop und warten Sie auf den grünen Statusanzeiger, bevor Sie den Container erneut öffnen
- **Container-Build schlägt fehl** - Überprüfen Sie Ihre Internetverbindung; der erste Build lädt Images und Pakete herunter. Klicken Sie auf **Rebuild Container**, um es erneut zu versuchen
- **Port 8501 bereits in Verwendung** - Stoppen Sie andere Apps, die diesen Port verwenden, oder wählen Sie einen anderen Port (zum Beispiel 8502): Ändern Sie ihn in der Dockerfile und in `devcontainer.json`, erstellen Sie den Container neu und starten Sie die App dann mit `streamlit run app.py --server.port 8502`

## Workflow-Überblick

Diese Einrichtung gibt Ihnen eine professionelle Python-Entwicklungsumgebung:

- **VS Code** bietet den Code-Editor mit Syntax-Hervorhebung, IntelliSense und Debugging
- **Docker-Container** führt eine isolierte Linux-Umgebung mit Python und allen Abhängigkeiten aus
- **Offizielles Python-Image** (`python:3.12-slim`) enthält Python, pip und wichtige Tools
- **Dev-Container-Konfiguration** (`.devcontainer/`) installiert automatisch VS Code-Erweiterungen für Python-Debugging und Sprachunterstützung
- **Port-Weiterleitung** ermöglicht Ihnen den Zugriff auf Web-Apps (Streamlit, Flask), die innerhalb des Containers laufen, von Ihrem Browser aus

## Täglicher Workflow

Sobald alles eingerichtet ist, hier Ihre tägliche Routine:

1. **Docker Desktop starten** - Öffnen Sie die App und warten Sie auf den grünen Statusanzeiger (Docker muss laufen)
2. **VS Code öffnen** - Starten Sie VS Code und öffnen Sie Ihren Projektordner
3. **Im Container erneut öffnen** - Falls nicht bereits im Container, klicken Sie auf das Symbol **><** in der unteren linken Ecke und wählen Sie **Reopen in Container**
4. **Code schreiben und ausführen** - Bearbeiten Sie `.py`-Dateien, führen Sie sie Zeile für Zeile mit `Shift+Enter` aus, oder führen Sie Apps mit `streamlit run app.py` aus
5. **Ihre Arbeit speichern** - Ihre Code-Dateien (`.py`, `.ipynb`) werden auf Ihrem Computer gespeichert und bleiben über Sitzungen hinweg erhalten
6. **Committen und pushen** - Wenn Ihr Projekt ein GitHub-Repository ist (siehe [GitHub Desktop mit Claude Code verwenden](./GitHub_Desktop_Claude_Code_Workflow)), committen und pushen Sie Ihre Änderungen mit GitHub Desktop

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
