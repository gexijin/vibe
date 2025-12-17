[Startseite](./)

# Python-Programmierung in VS Code über Docker-Container

Haben Sie schon einmal versucht, Ihren Python-Code mit einem Kollegen zu teilen, nur um dann Stunden mit dem Debuggen von „aber es funktioniert auf meinem Rechner"-Problemen zu verbringen? Docker-Container sind wie Frachtcontainer für Code – sie verpacken Ihre Python-Umgebung, Bibliotheken und Abhängigkeiten in eine versiegelte Box, die überall gleich funktioniert. Außerdem erhalten Sie Zugang zu Zehntausenden von vorgefertigten Images auf [Docker Hub](https://hub.docker.com/), wo Softwareentwickler fertige Umgebungen veröffentlichen und Ihnen den Schmerz manueller Softwareinstallation ersparen. Dieses Tutorial zeigt Ihnen, wie Sie Python in einer isolierten, reproduzierbaren Umgebung mit VS Code und Docker Desktop ausführen.

## Wichtige Konzepte

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Anwendung, die Container auf Ihrem Computer ausführt und isolierte Umgebungen verwaltet
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code-Funktion, die es Ihnen ermöglicht, innerhalb eines Docker-Containers mit voller IDE-Unterstützung zu programmieren
- **Container-Isolation** - Ihr Code läuft in einer separaten Linux-Umgebung, die nur Ihren Projektordner sieht, nicht Ihren gesamten Computer
- **[Python Official Images](https://hub.docker.com/_/python)** - Vorgefertigte Docker-Images mit Python und wichtigen Tools vorinstalliert

## Was Sie benötigen

- Abgeschlossenes Tutorial [Python-Programmierung in VS Code](./Python_Coding_VS_Code_Guide)
- 20-25 Minuten

## Schritt 1: Docker Desktop installieren

- Besuchen Sie die [Docker Desktop Download-Seite](https://www.docker.com/products/docker-desktop/)
- Klicken Sie auf **Download for Windows** (oder Mac/Linux je nach System)
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
- Erstellen Sie darin einen Unterordner namens `.devcontainer`
- Erstellen Sie darin einen Unterordner namens `python`
- Ihre Struktur sollte so aussehen: `python-docker-demo/.devcontainer/` und `python-docker-demo/python/`

## Schritt 4: Die Dockerfile erstellen

- Klicken Sie in VS Code auf **File > Open Folder**
- Navigieren Sie zum Ordner `python-docker-demo`, den Sie gerade erstellt haben
- Klicken Sie auf **Select Folder**
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
    pandas matplotlib seaborn streamlit jupyter

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

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
# Einfache Datenanalyse mit dem Iris-Datensatz
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Lade den Iris-Datensatz
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Zeige die ersten Zeilen an
print(df.head())

# Zusammenfassende Statistiken
print("\nZusammenfassende Statistiken:")
print(df.describe())

# Erstelle Histogramme
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Kelchblattlänge')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Kelchblattbreite')
plt.xlabel('Messung (cm)')
plt.ylabel('Häufigkeit')
plt.title('Iris Kelchblatt-Messungen')
plt.legend()
plt.show()
```

- Klicken Sie auf **File > Save**

## Schritt 7: Eine Streamlit-Web-App erstellen

- Erstellen Sie im `python`-Ordner eine neue Datei namens `app.py`
- Fügen Sie folgenden Inhalt ein:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geysir-Daten")

# Schieberegler für die Anzahl der Bins
bins = st.slider("Anzahl der Bins:", min_value=5, max_value=50, value=30)

# Generiere Beispieldaten (simuliert Old Faithful Ausbruchsdauern)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Erstelle Histogramm
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Ausbruchsdauer (Minuten)')
ax.set_ylabel('Häufigkeit')
ax.set_title(f'Histogramm mit {bins} Bins')

st.pyplot(fig)
```

- Klicken Sie auf **File > Save**

## Schritt 8: Im Container erneut öffnen

- Klicken Sie auf das grüne Symbol in der unteren linken Ecke von VS Code
- Wählen Sie **Reopen in Container** aus dem Menü
- VS Code baut den Container (dies dauert beim ersten Mal 5-10 Minuten)
- Sie sehen eine Fortschrittsanzeige mit den Build-Schritten
- Nach Abschluss zeigt das grüne Symbol **Dev Container: Python in Docker** an

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
ls
```

Sie sehen die Ordner, die Sie erstellt haben: `.devcontainer/`, `python/`, usw.

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
- Wählen Sie die erste Zeile: `import pandas as pd`
- Drücken Sie `Shift+Enter`, um sie in einem interaktiven Python-Terminal auszuführen
- Ein Python-Terminal öffnet sich unten
- Fahren Sie fort, jede Zeile oder jeden Block einzeln mit `Shift+Enter` auszuführen
- Wenn Sie `print(df.head())` ausführen, sehen Sie die ersten 5 Zeilen im Terminal
- Wenn Sie `print(df.describe())` ausführen, sehen Sie statistische Zusammenfassungen
- Wenn Sie den Histogramm-Code ausführen, öffnet sich ein Plot-Fenster mit der Visualisierung

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
- Finden Sie Zeile 6: `st.title("Old Faithful Geysir-Daten")`
- Ändern Sie sie zu:

```python
st.title("Meine erste Python-Docker-App")
```

- Klicken Sie auf **File > Save**
- Kehren Sie zu Ihrem Browser zurück
- Klicken Sie auf **Always rerun** in der oberen rechten Ecke
- Der Titel zeigt jetzt Ihren benutzerdefinierten Text

## Schritt 13: Die Dockerfile verstehen (Optional)

Lassen Sie uns untersuchen, wie die Dockerfile Ihre Umgebung konfiguriert.

- Navigieren Sie im VS Code Explorer zu `.devcontainer/Dockerfile`
- Klicken Sie zum Öffnen der Datei
- Sie sehen die vollständige Konfiguration

**Wichtige Teile:**

- `FROM python:3.12-slim` - Offizielles Python 3.12 Basis-Image (leichtgewichtiges Debian-basiertes)
- `RUN apt-get install` - Linux-Systembibliotheken zum Erstellen von Python-Paketen
- `RUN pip install --no-cache-dir ...` - Installiert Python-Pakete permanent
- `RUN curl... && apt-get install -y nodejs` - Installiert Node.js, das für die Ausführung von Claude Code erforderlich ist
- `RUN npm install -g @anthropic-ai/claude-code` - Installiert Claude Code global für KI-Unterstützung
- `EXPOSE 8501` - Öffnet Port 8501 für Streamlit-Apps

**Andere Python-Images, die Sie verwenden können:**

- `python:3.12` - Vollständiges Python-Image mit mehr Tools (größere Dateigröße)
- `python:3.12-slim` - Leichtgewichtiges Image mit Python und pip (das verwenden wir)
- `python:3.12-alpine` - Minimales Alpine Linux-basiertes Image (kleinste Dateigröße)
- `jupyter/datascience-notebook` - Vorkonfiguriertes Jupyter mit Data-Science-Bibliotheken

Nach der Änderung des Basis-Images müssen Sie den Container neu erstellen, um die Änderungen anzuwenden.

## Schritt 14: Python-Pakete im Docker-Image installieren (Optional)

Pakete, die über pip im Terminal installiert werden (`pip install paket`), sind temporär und verschwinden, wenn Sie den Container neu erstellen. Um Pakete permanent zu machen, fügen Sie sie zur Dockerfile hinzu.

- Navigieren Sie im VS Code Explorer zu `.devcontainer/Dockerfile`
- Klicken Sie zum Öffnen der Datei
- Finden Sie Zeile 9: `RUN pip install --no-cache-dir ...`
- Fügen Sie `scikit-learn` zur Liste hinzu:

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- Klicken Sie auf **File > Save**
- Klicken Sie auf das grüne Symbol in der unteren linken Ecke
- Wählen Sie **Rebuild Container** aus dem Menü
- VS Code erstellt den Container mit Ihrem neuen Paket neu (dies dauert 2-5 Minuten)
- Um zu überprüfen, öffnen Sie ein Python-Terminal und geben Sie ein:

```python
import sklearn
print(sklearn.__version__)
```

Wenn die Version ohne Fehler angezeigt wird, ist das Paket dauerhaft installiert.

## Nächste Schritte

- **Erstellen Sie ein neues Python-Skript** - Erstellen Sie eine neue `.py`-Datei im `python/`-Ordner, schreiben Sie Datenanalyse-Code mit eingebauten Datensätzen oder laden Sie Ihre eigenen CSV-Dateien
- **Installieren Sie Python-Pakete** - Fügen Sie Pakete hinzu, die Sie benötigen, indem Sie die Dockerfile (Zeile 9) bearbeiten und den Container neu erstellen
- **Erkunden Sie Data Science** - Probieren Sie Datenmanipulation mit pandas und Visualisierung mit matplotlib oder seaborn
- **Erstellen Sie Web-Apps** - Erstellen Sie interaktive Dashboards mit Streamlit oder Flask

## Fehlerbehebung

- **Docker Desktop läuft nicht** - Öffnen Sie Docker Desktop und warten Sie auf den grünen Statusanzeiger, bevor Sie den Container erneut öffnen
- **Container-Build schlägt fehl** - Überprüfen Sie Ihre Internetverbindung; der erste Build lädt Images und Pakete herunter. Klicken Sie auf **Rebuild Container**, um es erneut zu versuchen
- **Port 8501 bereits in Verwendung** - Stoppen Sie andere Apps, die diesen Port verwenden, oder ändern Sie den Port in der Dockerfile und `devcontainer.json`

## Workflow-Überblick

Diese Einrichtung gibt Ihnen eine professionelle Python-Entwicklungsumgebung:

- **VS Code** bietet den Code-Editor mit Syntax-Hervorhebung, IntelliSense und Debugging
- **Docker-Container** führt eine isolierte Linux-Umgebung mit Python und allen Abhängigkeiten aus
- **Python official image** (`python:3.12-slim`) enthält Python, pip und wichtige Tools
- **Dev Container config** (`.devcontainer/`) installiert automatisch VS Code-Erweiterungen für Python-Debugging und Sprachunterstützung
- **Port-Weiterleitung** ermöglicht Ihnen den Zugriff auf Web-Apps (Streamlit, Flask), die innerhalb des Containers laufen, von Ihrem Browser aus

## Täglicher Workflow

Sobald alles eingerichtet ist, hier Ihre tägliche Routine:

1. **Docker Desktop starten** - Öffnen Sie die App und warten Sie auf den grünen Statusanzeiger (Docker muss laufen)
2. **VS Code öffnen** - Starten Sie VS Code und öffnen Sie Ihren Projektordner
3. **Im Container erneut öffnen** - Falls nicht bereits im Container, klicken Sie auf das grüne Symbol (unten links) und wählen Sie **Reopen in Container**
4. **Code schreiben und ausführen** - Bearbeiten Sie `.py`-Dateien, führen Sie sie Zeile für Zeile mit `Shift+Enter` aus, oder führen Sie Apps mit `streamlit run app.py` aus
5. **Ihre Arbeit speichern** - Ihre Code-Dateien (`.py`, `.ipynb`) werden auf Ihrem Computer gespeichert und bleiben über Sitzungen hinweg erhalten
6. **Committen und pushen** - Verwenden Sie GitHub Desktop, um Ihre Änderungen zu committen und in das Repository zu pushen

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
