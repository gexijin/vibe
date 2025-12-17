[Startseite](./)

# R in VS Code ausführen

Sie möchten R-Code schreiben, aber RStudio fühlt sich schwerfällig an oder Sie bevorzugen die Flexibilität von VS Code. Stellen Sie sich VS Code als ein Schweizer Taschenmesser vor – es kann R, Python und viele andere Sprachen in einem leichtgewichtigen Editor handhaben. Dieses Tutorial zeigt Ihnen, wie Sie R in VS Code mit intelligenten Funktionen wie Codevervollständigung, interaktiven Plots und sogar Shiny-Apps einrichten.

## Wichtige Konzepte

- **[languageserver](https://github.com/REditorSupport/languageserver)** - R-Paket, das Codevervollständigung, Syntaxprüfung und Hover-Dokumentation in VS Code ermöglicht
- **[R-Erweiterung](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - VS Code-Erweiterung, die Ihren Editor mit R verbindet und Syntax-Hervorhebung, Codeausführung und Debugging bietet
- **[Shiny-Erweiterung](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - VS Code-Erweiterung zum Erstellen und Ausführen interaktiver Shiny-Web-Apps mit Auto-Reload

## Was Sie benötigen

- Abgeschlossenes Tutorial [VS Code Grundlagen](./VS_Code_Getting_Started)
- Internetverbindung zum Herunterladen von R und Paketen
- 10-15 Minuten

## Schritt 1: R installieren oder aktualisieren

Sie benötigen R Version 4.0 oder höher für die beste Kompatibilität.

- **Windows**:
  - Laden Sie das neueste R von [CRAN Windows](https://cran.r-project.org/bin/windows/base/) herunter und führen Sie das Installationsprogramm aus
  - Während der Installation **notieren Sie den Installationspfad** (zum Beispiel: `C:\Program Files\R\R-4.5.3`)
  - Wenn Sie eine alte Version haben, deinstallieren Sie sie zuerst über Einstellungen > Apps

- **macOS**:
  - Laden Sie von [CRAN macOS](https://cran.r-project.org/bin/macosx/) herunter und führen Sie das .pkg-Installationsprogramm aus
  - Beachten Sie, ob Sie Intel (`/Library/Frameworks/R.framework/Resources/bin/R`) oder Apple Silicon mit Homebrew (`/opt/homebrew/bin/R`) verwenden
  - Beim Aktualisieren ersetzt die neue Version die alte

- **Linux**:
  - Verwenden Sie Ihren Paketmanager (z.B. `sudo apt install r-base` unter Ubuntu)
  - Oder folgen Sie den [CRAN Linux](https://cran.r-project.org/bin/linux/) Anweisungen

Sie konfigurieren VS Code in Schritt 3 so, dass es R findet, also machen Sie sich keine Sorgen, wenn `R --version` in Ihrem Terminal noch nicht funktioniert.

## Schritt 2: R-Erweiterungen in VS Code installieren

- Öffnen Sie VS Code
- Klicken Sie auf das **Extensions**-Symbol in der linken Seitenleiste
- Suchen Sie nach `REditorSupport.r` und klicken Sie auf **Install** bei der R-Erweiterung von REditorSupport
- Suchen Sie nach `Posit.shiny` und klicken Sie auf **Install** bei der Shiny-Erweiterung von Posit

## Schritt 3: Ihren R-Installationspfad finden

Bevor Sie VS Code konfigurieren, müssen Sie wissen, wo R auf Ihrem System installiert ist.

### Für Windows-Benutzer

1. Öffnen Sie den **Datei-Explorer**
2. Navigieren Sie zu `C:\Program Files\R\`
3. Sie sehen einen Ordner wie `R-4.5.3` (Ihre Versionsnummer kann abweichen)
4. Öffnen Sie diesen Ordner → Öffnen Sie den `bin`-Ordner
5. Sie sehen dort `R.exe`
6. Der vollständige Pfad ist: `C:\Program Files\R\R-4.5.3\bin\R.exe`

**Schreiben Sie sich Ihre Versionsnummer auf oder merken Sie sie sich** (z.B. `R-4.5.3`) – Sie brauchen sie in Schritt 4.

### Für macOS-Benutzer

Ihre R-Installation befindet sich typischerweise an einem dieser Orte:

- **Standard-Installation (Intel oder Apple Silicon)**: `/Library/Frameworks/R.framework/Resources/bin/R`
- **Homebrew auf Apple Silicon**: `/opt/homebrew/bin/R`
- **Homebrew auf Intel**: `/usr/local/bin/R`

Um zu überprüfen, welchen Pfad Sie haben, öffnen Sie **Terminal** und geben Sie ein:
```bash
which R
```

Dies zeigt Ihnen den genauen Pfad zu Ihrer R-Installation.

### Für Linux-Benutzer

R ist typischerweise installiert unter: `/usr/bin/R`

Überprüfen Sie durch Öffnen eines Terminals und Eingeben von:
```bash
which R
```

## Schritt 4: VS Code konfigurieren, um R zu finden

- Klicken Sie in VS Code auf das **Zahnrad-Symbol** in der unteren linken Ecke
- Wählen Sie **Settings** aus dem Menü
- In der Suchleiste oben geben Sie `r.rpath.windows` (Windows), `r.rpath.mac` (macOS) oder `r.rpath.linux` (Linux) ein
- Sie sollten die Einstellung erscheinen sehen. Klicken Sie auf **Edit in settings.json** unter der Einstellung
- Die Datei settings.json öffnet sich
- Fügen Sie die entsprechende Konfiguration für Ihre Plattform innerhalb der geschweiften Klammern `{}` hinzu

**Für Windows**, fügen Sie diese Zeile hinzu (ersetzen Sie `R-4.5.3` durch Ihre Version aus Schritt 3):

```json
"r.rpath.windows": "C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe",
```

**Warum zwei Backslashes (`\\`)?** In JSON-Dateien ist der Backslash `\` ein Sonderzeichen (genannt Escape-Zeichen). Um einen einzelnen Backslash im tatsächlichen Dateipfad darzustellen, müssen Sie zwei Backslashes `\\` eingeben. Also wird `C:\Program Files` zu `C:\\Program Files` in settings.json.

**Für macOS**, fügen Sie eine dieser Zeilen hinzu:

```json
"r.rpath.mac": "/Library/Frameworks/R.framework/Resources/bin/R",
```

Oder wenn Sie R über Homebrew auf Apple Silicon installiert haben:

```json
"r.rpath.mac": "/opt/homebrew/bin/R",
```

**Für Linux**, fügen Sie hinzu:

```json
"r.rpath.linux": "/usr/bin/R",
```

- Speichern Sie die Datei durch Klicken auf **File > Save**
- **Starten Sie VS Code vollständig neu**, damit die Änderungen wirksam werden

## Schritt 5: Erforderliche R-Pakete installieren

- Klicken Sie in VS Code im oberen Menü auf **View**, dann wählen Sie **Command Palette**
- Geben Sie `R: Create R Terminal` ein und wählen Sie es aus
- Eine R-Konsole erscheint im Terminal-Panel unten
  - Sie sollten sehen, wie R mit Versionsinformationen startet
  - Wenn Sie einen Fehler erhalten, überprüfen Sie Ihre settings.json-Konfiguration in Schritt 4 und starten Sie VS Code neu
- Installieren Sie Pakete durch Eingabe dieser Befehle einzeln:

```r
install.packages("languageserver")
install.packages("shiny")
```

- Warten Sie, bis die Installation abgeschlossen ist (kann einige Minuten dauern)
- Geben Sie `q()` ein und drücken Sie Enter, um R zu beenden
- Geben Sie `n` ein, wenn Sie nach dem Speichern des Arbeitsbereichs gefragt werden

Das einfache Eingeben von `R` in einem normalen Terminal funktioniert nicht, es sei denn, R ist in Ihrem System-PATH. Die R-Erweiterung verwendet Ihre `r.rpath`-Einstellung, um R zu finden.

## Schritt 6: Ihr R-Projekt erstellen

- Erstellen Sie einen neuen Ordner auf Ihrem Computer (z.B. `mein-r-projekt`)
- Klicken Sie in VS Code auf **File > Open Folder** und wählen Sie Ihren neuen Ordner
- Klicken Sie im oberen Menü auf **File > New File**
- Speichern Sie die Datei als `analysis.R` durch Klicken auf **File > Save**

## Schritt 7: Ihr erstes R-Skript schreiben

- Geben Sie diesen Code in `analysis.R` ein:

```r
# Iris-Datensatz laden
data(iris)

# Erste Zeilen anzeigen
head(iris)

# Zusammenfassende Statistiken generieren
summary(iris)

hist(iris$Sepal.Length)
```

- Speichern Sie die Datei durch Klicken auf **File > Save**

## Schritt 8: R-Code interaktiv ausführen

- Mit geöffneter `analysis.R` wählen Sie eine Codezeile aus und drücken Sie `Strg+Enter` (Windows/Linux) oder `Cmd+Enter` (Mac), um sie auszuführen
- Wenn Sie kein Terminal offen haben, öffnet das erste `Strg+Enter` / `Cmd+Enter` ein R-Terminal. Das zweite führt den Code aus.
- Beobachten Sie die Ausgabe im Terminal und der Plot öffnet sich in einem separaten Fenster
- Sie können auch alle Zeilen auswählen und sie auf die gleiche Weise ausführen.

## Schritt 9: Eine einfache Shiny-App erstellen

- Erstellen Sie eine neue Datei in Ihrem Projektordner: **File > New File**
- Speichern Sie sie als `app.R`
- Geben Sie diesen Code ein:

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Interaktives Histogramm"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Anzahl der Bins:",
                  min = 5,
                  max = 50,
                  value = 30)
    ),

    mainPanel(
      plotOutput("histogram")
    )
  )
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    x <- faithful$waiting
    bins <- seq(min(x), max(x), length.out = input$bins + 1)

    hist(x, breaks = bins, col = "steelblue", border = "white",
         xlab = "Wartezeit (Minuten)",
         main = "Verteilung der Wartezeiten")
  })
}

shinyApp(ui = ui, server = server)
```

- Speichern Sie die Datei
- Beachten Sie die **▶**-Schaltfläche, die oben rechts im Editor erscheint
- Klicken Sie auf das Dropdown, um **Run Shiny App** auszuwählen
- Die App öffnet sich in einem Browser oder VS Code-Panel
- Bewegen Sie den Schieberegler und beobachten Sie, wie sich das Histogramm sofort aktualisiert

## Schritt 10: Codevervollständigung und Hover-Hilfe verwenden

- In `analysis.R` beginnen Sie auf einer neuen Zeile `mea` zu tippen
- Ein Dropdown erscheint mit Vorschlägen – wählen Sie `mean()` durch Drücken von Enter
- Bewegen Sie Ihre Maus über das Wort `mean` in Ihrem bestehenden Code
- Ein Popup zeigt die Funktionsdokumentation und Anwendungsbeispiele
- Versuchen Sie, über `lm`, `summary` oder `plot` zu hovern, um deren Dokumentation zu sehen
- Geben Sie `data$` ein und beobachten Sie, wie VS Code Spaltennamen (`x` und `y`) vorschlägt

## Schritt 11: Weitere Funktionen ausprobieren

- **Markdown-Integration**: Erstellen Sie eine R-Markdown-Datei (`.Rmd`), um Code, Ausgabe und Text zu mischen
- **Code-Formatierung**: Klicken Sie mit der rechten Maustaste in Ihr R-Skript und wählen Sie **Format Document**, um Code automatisch zu formatieren
- **Debugging**: Setzen Sie Breakpoints durch Klicken links neben Zeilennummern, dann führen Sie Code im Debug-Modus aus
- **Git-Integration**: Verwenden Sie VS Codes eingebaute Git-Funktionen, um Ihre R-Projekte zu versionieren

## Nächste Schritte

- Erstellen Sie eine Multi-Datei-Shiny-App mit separaten `ui.R`- und `server.R`-Dateien
- Erkunden Sie [ggplot2](https://ggplot2.tidyverse.org/) für fortgeschrittene Datenvisualisierung
- Probieren Sie die [tidyverse](https://www.tidyverse.org/)-Pakete (`dplyr`, `tidyr`) für Datenmanipulation
- Lernen Sie R Markdown oder [Quarto](https://quarto.org/) zum Erstellen von Berichten mit eingebettetem R-Code
- Installieren Sie die [R Debugger-Erweiterung](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) für fortgeschrittenes Debugging

## Fehlerbehebung

- **„R is not recognized" im VS Code-Terminal**: VS Code kann R nicht finden. Überprüfen Sie Ihre settings.json (Schritt 4) – verifizieren Sie, dass der R-Pfad korrekt ist und auf `R.exe` (Windows) oder die R-Binärdatei (Mac/Linux) zeigt. Beispielpfade:
  - Windows: `C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe` (Versionsnummer anpassen)
  - macOS Intel: `/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew: `/opt/homebrew/bin/R`
  - Linux: `/usr/bin/R`
  Starten Sie VS Code nach der Korrektur vollständig neu.

- **R-Versionsunterschied in den Einstellungen**: Wenn Sie R aktualisiert haben, aber VS Code noch die alte Version verwendet, aktualisieren Sie die Versionsnummer in Ihrer settings.json `r.rpath`-Konfiguration, um der neuen R-Installation zu entsprechen (siehe Schritt 3, um Ihren aktuellen Installationspfad zu finden).

- **Codevervollständigung funktioniert nicht**: Stellen Sie sicher, dass languageserver erfolgreich installiert wurde (Schritt 5). Starten Sie VS Code nach der Installation neu. Warten Sie 10-20 Sekunden nach dem Öffnen einer R-Datei, bis der Sprachserver initialisiert ist. Überprüfen Sie das Output-Panel (View > Output > R Language Server) auf Fehler.

- **Plots erscheinen nicht**: Plots öffnen sich in separaten Fenstern mit R's Standard-Grafikgerät. Stellen Sie sicher, dass Sie einen Fenstermanager verfügbar haben. Auf manchen Systemen müssen Sie möglicherweise X11 (macOS) installieren oder sicherstellen, dass Grafikunterstützung aktiviert ist.

- **Shiny-App wird nicht ausgeführt**: Stellen Sie sicher, dass die Shiny-Erweiterung installiert ist (Schritt 2), das shiny-Paket installiert ist (Schritt 5) und Ihre Datei `app.R` heißt. Überprüfen Sie das Terminal auf Fehlermeldungen. Die Run-Schaltfläche erscheint nur, wenn VS Code die Datei als Shiny-App erkennt.

## Workflow-Zusammenfassung

VS Code bietet eine moderne, leichtgewichtige Alternative zu RStudio mit diesen wichtigen Vorteilen:

- **Vereinheitlichte Umgebung**: Programmieren Sie R, Python, JavaScript und mehr in einem Editor
- **Anpassbar**: Installieren Sie nur die Erweiterungen, die Sie für ein schlankes Setup brauchen
- **Integriertes Terminal**: Führen Sie R, Git und Shell-Befehle nebeneinander aus
- **Shiny-Entwicklung**: App-Start mit einem Klick mit Auto-Reload spart Zeit
- **Versionskontrolle**: Eingebaute Git-Integration ohne externe Tools

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
