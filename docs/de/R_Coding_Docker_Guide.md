---
title: "R-Programmierung in VS Code über Docker-Container"
lang: "de"
---
[Startseite](./)

# R-Programmierung in VS Code über Docker-Container

Haben Sie schon einmal versucht, Ihren R-Code mit einem Kollegen zu teilen, nur um dann Stunden mit dem Debuggen von „aber es funktioniert auf meinem Rechner"-Problemen zu verbringen? Docker-Container sind wie Frachtcontainer für Code – sie verpacken Ihre R-Umgebung, Bibliotheken und Abhängigkeiten in eine versiegelte Box, die überall gleich funktioniert. Außerdem erhalten Sie Zugang zu Zehntausenden von vorgefertigten Images auf [Docker Hub](https://hub.docker.com/), wo Softwareentwickler fertige Umgebungen veröffentlichen und Ihnen den Schmerz manueller Softwareinstallation ersparen. Dieses Tutorial zeigt Ihnen, wie Sie R in einer isolierten, reproduzierbaren Umgebung mit VS Code und Docker Desktop ausführen.

## Wichtige Konzepte

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Anwendung, die Container auf Ihrem Computer ausführt und isolierte Umgebungen verwaltet
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code-Funktion, die es Ihnen ermöglicht, innerhalb eines Docker-Containers mit voller IDE-Unterstützung zu programmieren
- **Container-Isolation** - Ihr Code läuft in einer separaten Linux-Umgebung, die nur Ihren Projektordner sieht, nicht Ihren gesamten Computer
- **[Rocker](https://rocker-project.org/)** - Vorgefertigte Docker-Images, die speziell für R-Entwicklung entwickelt wurden

## Was Sie benötigen

- Abgeschlossenes Tutorial [R-Programmierung in VS Code](./R_Coding_VS_Code_Guide)
- Abgeschlossenes Tutorial [GitHub Desktop Grundlagen](./Github_desktop)
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

## Schritt 3: Das Vibe-Projekt mit GitHub Desktop klonen

- Öffnen Sie GitHub Desktop
- Klicken Sie auf **File > Clone repository**
- Klicken Sie auf den **URL**-Tab
- Fügen Sie im Feld **Repository URL** ein: `https://github.com/gexijin/vibe`
- Wählen Sie, wo das Projekt gespeichert werden soll (das Feld **Local Path**)
- Klicken Sie auf **Clone**
- GitHub Desktop lädt das Projekt an Ihren gewählten Ort herunter

## Schritt 4: Projekt in VS Code öffnen

- Klicken Sie in VS Code auf **File > Open Folder**
- Navigieren Sie zum Ordner `vibe`, den Sie gerade geklont haben
- Klicken Sie auf **Ordner auswählen** (englisch: **Select Folder**)
- Sie sehen die Projektdateien in der Explorer-Seitenleiste

## Schritt 5: Im Container erneut öffnen

- Suchen Sie nach einer Benachrichtigung unten rechts: **Folder contains a Dev Container configuration file**
- Klicken Sie auf **Reopen in Container**
- Wenn Sie die Benachrichtigung nicht sehen, klicken Sie auf das grüne Symbol in der unteren linken Ecke
- Wählen Sie **Reopen in Container** aus dem Menü
- VS Code baut den Container (dies dauert beim ersten Mal 5-10 Minuten)
- Sie sehen eine Fortschrittsanzeige mit den Build-Schritten
- Nach Abschluss zeigt das grüne Symbol **Dev Container: R in Docker (AMD64)** an

**Hinweis:** Der Container enthält automatisch die R-Erweiterung und das languageserver-Paket. Die Dockerfile und devcontainer.json erledigen das für Sie.

## Schritt 6: Die Container-Umgebung verstehen

Jetzt programmieren Sie innerhalb eines Linux-Containers. Lassen Sie uns erkunden, was das bedeutet.

- Klicken Sie auf **Terminal > New Terminal**, um ein Terminal innerhalb des Containers zu öffnen
- Überprüfen Sie Ihren aktuellen Standort:

```bash
pwd
```

Sie sehen `/workspaces/vibe` – das ist Ihr Projektordner innerhalb des Containers.

- Listen Sie die Dateien auf:

```bash
ls
```

Sie sehen dieselben Dateien aus dem Projekt: `R/`, `.devcontainer/`, `README.md`, usw.

- Versuchen Sie, ein Verzeichnis nach oben zu gehen:

```bash
cd ..
ls
```

Sie sehen nur `vibe/` – der Container ist isoliert. Sie können nicht auf die anderen Ordner, den Desktop oder die Dokumente Ihres Computers zugreifen. Diese Isolation stellt sicher, dass Ihre R-Umgebung sauber und reproduzierbar ist.

- Kehren Sie zum Projektordner zurück:

```bash
cd vibe
```

## Schritt 7: R-Code Zeile für Zeile ausführen

Der Container hat R mit gängigen Paketen vorinstalliert. Führen wir ein einfaches Datenanalyse-Skript aus.

- Navigieren Sie im VS Code Explorer zu `R/iris_analysis.R`
- Klicken Sie zum Öffnen der Datei
- Sie sehen R-Code, der den Iris-Datensatz analysiert
- Wählen Sie die erste Zeile: `data(iris)`
- Drücken Sie `Strg+Enter` (Windows/Linux) oder `Cmd+Enter` (Mac), um sie auszuführen
- Wenn Sie kein R-Terminal offen haben, erstellt das erste Mal eines, das zweite Mal führt den Code aus
- Fahren Sie fort, jede Zeile einzeln auszuführen
- Wenn Sie `head(iris)` ausführen, sehen Sie die ersten 6 Zeilen im Terminal
- Wenn Sie `summary(iris)` ausführen, sehen Sie statistische Zusammenfassungen
- Wenn Sie die `hist()`-Befehle ausführen, öffnen sich Histogramm-Plots in separaten Fenstern
- Sie können auch mehrere Zeilen auswählen und sie zusammen mit `Strg+Enter` oder `Cmd+Enter` ausführen

## Schritt 8: Die App ausführen

Das Projekt enthält eine Demo-Shiny-App, die ein interaktives Histogramm erstellt.

- Navigieren Sie im VS Code Explorer zu `R/app.R`
- Klicken Sie zum Öffnen der Datei
- Sie sehen Code für eine Shiny-Webanwendung
- Schauen Sie oben rechts im Editor-Fenster nach einer **▶**-Schaltfläche
- Klicken Sie auf den Dropdown-Pfeil daneben und wählen Sie **Run Shiny App**
- Die App startet und VS Code leitet Port 3838 automatisch weiter
- Eine Benachrichtigung erscheint: **Open in Browser**
- Klicken Sie auf **Open in Browser**
- Die Shiny-App öffnet sich in Ihrem Webbrowser
- Bewegen Sie den Schieberegler, um die Histogramm-Bins zu ändern – das Diagramm aktualisiert sich in Echtzeit

## Schritt 9: Eine einfache Änderung vornehmen

Lassen Sie uns die App modifizieren, um zu sehen, wie Entwicklung funktioniert.

- Lassen Sie die App laufen
- Bearbeiten Sie in VS Code `R/app.R`
- Finden Sie Zeile 16: `titlePanel("Old Faithful Geyser Data")`
- Ändern Sie sie zu:

```r
titlePanel("My First R Docker App")
```

- Speichern Sie die Datei (**File > Save**)
- Die Shiny-Erweiterung lädt die App automatisch neu
- Aktualisieren Sie Ihren Browser (oder er aktualisiert sich möglicherweise automatisch)
- Der Titel zeigt jetzt Ihren benutzerdefinierten Text

## Schritt 10: Das Dockerfile verstehen (Optional)

- Navigieren Sie im VS Code Explorer zu `.devcontainer/Dockerfile`
- Klicken Sie zum Öffnen der Datei
- Sie sehen die vollständige Konfiguration:

```dockerfile
# choose a Dockerhub base image with R, Shiny Server, and tidyverse packages
FROM rocker/shiny-verse:latest

# 1. System deps commonly needed by R packages
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# 2. R packages for VS Code integration: language server + debugger
RUN R -q -e 'install.packages(c("rstudioapi", "languageserver"), repos="https://cloud.r-project.org")'

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Give shiny passwordless sudo for updating Claude Code from VS Code
RUN echo 'shiny ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    rm -rf /var/lib/apt/lists/*

# Expose Shiny server port
EXPOSE 3838
```

**Wichtige Teile:**

- `FROM rocker/shiny-verse:latest` - Basis-Image mit vorinstalliertem R, Shiny und tidyverse
- `RUN apt-get install` - Linux-Systembibliotheken für R-Pakete
- `RUN R -q -e 'install.packages(...)'` - Installiert R-Pakete permanent
- `RUN curl... && apt-get install -y nodejs` - Installiert Node.js, erforderlich für Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Installiert Claude Code global für KI-Unterstützung
- `RUN echo 'shiny ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers` - Erlaubt dem Benutzer im Container, `sudo claude update` ohne Passwortabfrage auszuführen
- `EXPOSE 3838` - Öffnet Port 3838 für Shiny-Apps

**Andere Rocker-Images, die Sie verwenden können:**

- `rocker/r-ver:4.5.3` - Nur R (spezifische Version)
- `rocker/rstudio:latest` - R mit RStudio Server
- `rocker/tidyverse:latest` - R mit tidyverse-Paketen
- `rocker/shiny-verse:latest` - R mit Shiny und tidyverse (das verwenden wir)

Nach Änderung des Basis-Images müssen Sie den Container neu erstellen, um die Änderungen anzuwenden.

## Schritt 11: R-Pakete im Docker-Image installieren (Optional)

Über die R-Konsole installierte Pakete (`install.packages()`) sind temporär und verschwinden, wenn Sie den Container neu erstellen. Um Pakete permanent zu machen, fügen Sie sie der Dockerfile hinzu.

- Navigieren Sie im VS Code Explorer zu `.devcontainer/Dockerfile`
- Klicken Sie zum Öffnen der Datei
- Fügen Sie eine neue Zeile unterhalb der anderen 'install.packages'-Zeilen hinzu, um das `data.table`-Paket zu installieren:
```dockerfile
RUN R -q -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
```

- Speichern Sie die Datei (**File > Save**)
- Klicken Sie auf das grüne Symbol in der unteren linken Ecke
- Wählen Sie **Rebuild Container** aus dem Menü
- VS Code erstellt den Container mit Ihrem neuen Paket neu (dies dauert 2-5 Minuten)
- Um zu überprüfen, öffnen Sie ein R-Terminal und geben Sie ein:

```r
library(data.table)
```

Wenn es ohne Fehler geladen wird, ist das Paket permanent installiert.

## Nächste Schritte

- **Erstellen Sie ein neues R-Skript** - Erstellen Sie eine neue `.R`-Datei im `R/`-Ordner, schreiben Sie Datenanalyse-Code mit eingebauten Datensätzen wie `mtcars` oder `iris`
- **Installieren Sie R-Pakete** - Fügen Sie Pakete hinzu, die Sie benötigen, indem Sie die Dockerfile bearbeiten und den Container neu erstellen
- **Erkunden Sie tidyverse** - Probieren Sie Datenmanipulation mit `dplyr` und Visualisierung mit `ggplot2` mit Beispieldatensätzen

## Fehlerbehebung

- **Docker Desktop läuft nicht** - Öffnen Sie Docker Desktop und warten Sie auf den grünen Statusanzeiger, bevor Sie den Container erneut öffnen
- **Container-Build schlägt fehl** - Überprüfen Sie Ihre Internetverbindung; der erste Build lädt ~2GB herunter. Klicken Sie auf **Rebuild Container**, um es erneut zu versuchen
- **Port 3838 bereits in Verwendung** - Stoppen Sie andere Apps, die diesen Port verwenden, oder ändern Sie den Port in `.devcontainer/devcontainer.json`

## Workflow-Überblick

Diese Einrichtung gibt Ihnen eine professionelle R-Entwicklungsumgebung:

- **VS Code** bietet den Code-Editor mit Syntax-Hervorhebung und IntelliSense
- **Docker-Container** führt eine isolierte Linux-Umgebung mit R und allen Abhängigkeiten aus
- **Rocker image** (`rocker/shiny-verse`) enthält R, Shiny, tidyverse und Entwicklertools
- **Dev Container config** (`.devcontainer/`) installiert automatisch VS Code-Erweiterungen für R-Debugging und Sprachunterstützung
- **Port-Weiterleitung** ermöglicht Ihnen den Zugriff auf die Shiny-App, die innerhalb des Containers läuft, von Ihrem Browser aus

## Täglicher Workflow

Sobald alles eingerichtet ist, hier Ihre tägliche Routine:

1. **Docker Desktop starten** - Öffnen Sie die App und warten Sie auf den grünen Statusanzeiger (Docker muss laufen)
2. **VS Code öffnen** - Starten Sie VS Code und öffnen Sie Ihren Projektordner
3. **Im Container erneut öffnen** - Falls nicht bereits im Container, klicken Sie auf das grüne Symbol (unten links) und wählen Sie **Reopen in Container**
4. **Code schreiben und ausführen** - Bearbeiten Sie `.R`-Dateien, führen Sie sie Zeile für Zeile mit `Strg+Enter`/`Cmd+Enter` aus, oder führen Sie Shiny-Apps mit der Schaltfläche **▶ Run Shiny App** aus
5. **Ihre Arbeit speichern** - Ihre Code-Dateien (`.R`, `.Rmd`) werden auf Ihrem Computer gespeichert und bleiben über Sitzungen hinweg erhalten
6. **Committen und pushen** - Verwenden Sie GitHub Desktop, um Ihre Änderungen zu committen und in das Repository zu pushen

## Was ist Docker Desktop?

Docker Desktop ist eine Anwendung, die die Nutzung von Docker auf Ihrem Computer erleichtert. Sie stellt die Hintergrunddienste bereit, die Docker benötigt, und bietet ein Fenster, in dem Sie Ihre Container, Images, Speicher und andere Docker-Ressourcen sehen und verwalten können.

Sie können sich Docker Desktop als Steuerzentrale für Ihre Container vorstellen. Wenn Sie Docker Desktop öffnen, startet es die Docker-Engine. Die Docker-Engine ist der Teil von Docker, der Container tatsächlich erstellt und ausführt. Normalerweise müssen Sie nicht direkt mit der Engine arbeiten, da Docker Desktop sie für Sie verwaltet.

### Was macht Docker Desktop?

Docker Desktop übernimmt mehrere wichtige Aufgaben:

- **Führt die Docker-Engine aus** - Die Engine erstellt und betreibt die Container, in denen Ihre Software läuft.
- **Lädt Images herunter** - Ein Image ist ein fertiges Startpaket, zum Beispiel ein Linux-System mit R und gängigen R-Paketen. In diesem Tutorial verwendet das Projekt ein Image aus dem Rocker-Projekt.
- **Erstellt Container** - Docker verwendet das Dockerfile und die Dev-Container-Einstellungen dieses Projekts, um einen Container zu erstellen, der für die R-Entwicklung vorbereitet ist.
- **Startet und stoppt Container** - Sie können den Container bei Bedarf öffnen, pausieren, neu starten oder stoppen.
- **Verbindet Container mit Ihren Dateien** - Ihr Projektordner ist im Container verfügbar, sodass Sie Dateien in VS Code bearbeiten können, während der Code im Container läuft.
- **Verbindet Container mit Ihrem Browser** - Wenn die Shiny-App Port 3838 verwendet, sorgen Docker Desktop und VS Code gemeinsam dafür, dass die App in Ihrem Webbrowser erreichbar ist.

### Wie Docker Desktop in dieses Tutorial passt

Drei Teile arbeiten zusammen:

1. **Docker Desktop** führt die Docker-Engine auf Ihrem Computer aus.
2. **VS Code** ist der Editor, in dem Sie R-Code schreiben und ausführen.
3. **Der Dev Container** stellt eine vorbereitete Linux-Umgebung bereit, die R, R-Pakete und die in diesem Projekt verwendeten Werkzeuge enthält.

Wenn Sie **Reopen in Container** wählen, bittet VS Code Docker Desktop, den Container des Projekts zu erstellen oder zu starten. Die Anwendung läuft weiterhin auf Ihrem Computer, aber die R-Umgebung befindet sich im Container. So bleiben R-Version, Pakete und Systemwerkzeuge vom Rest Ihres Computers getrennt.

Docker Desktop ersetzt weder VS Code noch R noch Ihren Webbrowser. Es stellt die Umgebung bereit, in der der Container läuft. In VS Code arbeiten Sie, R ist die Sprache, die Sie verwenden, und im Browser sehen Sie sich die Shiny-App an.

### Warum Docker Desktop verwenden?

Wenn Sie R und alle benötigten Pakete direkt auf Ihrem Computer installieren, kann es manchmal zu Versionskonflikten kommen. Ein Projekt braucht vielleicht eine andere Paketversion als ein anderes Projekt. Docker Desktop hilft, solche Konflikte zu vermeiden, indem es jedem Projekt eine eigene, kontrollierte Umgebung gibt.

Wenn zum Beispiel eine Kommilitonin oder ein Kommilitone dieselben Projektdateien und Docker-Einstellungen verwendet, kann Docker eine Umgebung erstellen, die Ihrer sehr ähnlich ist. Dadurch ist es weniger wahrscheinlich, dass Sie einen Fehler sehen, der nur durch unterschiedliche Softwareversionen entsteht. Ihr R-Code und Ihre Projektdateien bleiben auf Ihrem Computer, während die Werkzeuge, die zum Ausführen benötigt werden, im Container organisiert sind.

Docker Desktop muss geöffnet sein und laufen, bevor Sie dieses Projekt in einem Container erstellen oder erneut öffnen. Wenn Docker Desktop geschlossen ist, kann VS Code den Container nicht starten, und Sie sehen möglicherweise eine Fehlermeldung, dass Docker nicht läuft.

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
