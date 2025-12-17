[Startseite](./)

# Vibe Coding in R mit Claude Code und Docker

Vibe Coding ist wie ein Gespräch mit Ihrem Computer – Sie beschreiben das Ergebnis, Claude Code baut es, Sie testen und verfeinern. Es ist keine Magie; es ist eine neue Art zu arbeiten, bei der Sie die Vision leiten und KI die Umsetzung übernimmt. Dieses Tutorial zeigt Ihnen, wie Sie ein echtes NBA-Statistik-Dashboard erstellen, indem Sie nur natürlichsprachliche Anfragen verwenden.

## Wichtige Konzepte

- **[Claude Code](https://code.claude.com/)** - KI-Programmierassistent, der Code basierend auf Ihren natürlichsprachlichen Anfragen schreibt, debuggt und überarbeitet
- **[hoopR](https://hoopr.sportsdataverse.org/)** - R-Paket, das einfachen Zugriff auf NBA-Spielerstatistiken und Spieldaten bietet
- **Iterative Verfeinerung** - Das zentrale Vibe-Coding-Muster: beschreiben → testen → verfeinern → funktionierende Versionen committen

## Was Sie benötigen

- Abgeschlossenes Tutorial [R-Programmierung in VS Code über Docker](./R_Coding_Docker_Guide)
- Abgeschlossenes Tutorial [GitHub Desktop mit Claude Code verwenden](./GitHub_Desktop_Claude_Code_Workflow)
- Docker Desktop installiert und gestartet
- 25-30 Minuten

## Schritt 1: Neues GitHub-Repository erstellen

- Öffnen Sie GitHub Desktop
- Klicken Sie auf **File > New Repository**
- Füllen Sie die Details aus:
  - **Name:** `nba-dashboard`
  - **Description:** `NBA stats dashboard built with vibe coding`
  - **Local Path:** Wählen Sie einen Speicherort (z.B. Dokumente oder Arbeitsordner)
  - Aktivieren Sie **Initialize this repository with a README**
- Klicken Sie auf **Create Repository**
- Klicken Sie oben auf **Publish repository**
- Deaktivieren Sie **Keep this code private**, wenn Sie es öffentlich machen möchten (optional)
- Klicken Sie auf **Publish Repository**

Sie haben jetzt ein lokales Git-Repository und ein Backup auf GitHub.

## Schritt 2: Docker-Konfiguration kopieren

- Gehen Sie zu https://github.com/gexijin/vibe
  - **Hinweis für ARM64-Benutzer (Apple Silicon Macs):** Verwenden Sie stattdessen https://github.com/gexijin/vibe/tree/ARM64
- Klicken Sie auf **Code** und Download Zip
- Öffnen Sie den Datei-Explorer (Windows) oder Finder (Mac)
- Entpacken Sie die Datei im Download-Ordner
- Navigieren Sie zu Ihrem Vibe-Projektordner (z.B. `Documents/vibe`)
- Finden Sie den `.devcontainer`-Ordner
- Kopieren Sie den gesamten Ordner (er enthält `Dockerfile` und `devcontainer.json`)
- Navigieren Sie zu Ihrem neuen `nba-dashboard`-Ordner
- Fügen Sie den `.devcontainer`-Ordner dort ein

Ihr `nba-dashboard`-Ordner sollte jetzt enthalten:
- `.devcontainer/` (Ordner, den Sie gerade kopiert haben)
- `README.md` (von GitHub Desktop erstellt)
- `.git/` (versteckter Ordner für Versionskontrolle)

## Schritt 3: Projekt im Container öffnen

- Starten Sie die **Docker Desktop**-App unter Windows oder Mac. Lassen Sie sie im Hintergrund laufen
- Öffnen Sie VS Code
- Klicken Sie auf **File > Open Folder**
- Navigieren Sie zum `nba-dashboard`-Ordner
- Klicken Sie auf **Ordner auswählen** (Windows) oder **Öffnen** (Mac)
- Eine Benachrichtigung erscheint unten rechts: **Folder contains a Dev Container configuration file**
- Klicken Sie auf **Reopen in Container**
- Wenn Sie die Benachrichtigung nicht sehen, klicken Sie auf das grüne Symbol in der unteren linken Ecke und wählen Sie **Reopen in Container**
- VS Code baut den Docker-Container (dauert beim ersten Mal 3-5 Minuten)
- Beobachten Sie die Fortschrittsanzeige mit den Build-Schritten
- Nach Abschluss zeigt das grüne Symbol **Dev Container: R in Docker** an

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

## Schritt 5: Erster Vibe - NBA-Daten abrufen

Jetzt beginnt der Spaß. Anstatt Dokumentation nachzuschlagen, beschreiben Sie einfach, was Sie wollen.

- Geben Sie im Claude Code-Terminal ein:

```
Installiere das hoopR-Paket und lade aktuelle NBA-Spielerstatistiken. Zeige mir die Top 10 Spieler nach Gesamtpunkten dieser Saison. Stelle es als schöne Tabelle dar.
```

- Drücken Sie Enter
- Beobachten Sie Claude:
  - Das hoopR-Paket installieren
  - R-Code zum Laden der Daten schreiben
  - Ein Skript erstellen, um die Top-Scorer anzuzeigen
  - Den Code ausführen
- Überprüfen Sie die Ausgabe mit Spielernamen, Teams und Punkten

Sie haben gerade Vibe Coding verwendet! Kein Durchsuchen von Dokumentation, kein Trial-and-Error – einfach beschreiben und testen.

**Speichern Sie Ihren Fortschritt:** Bitten Sie Claude, mit Git zu committen, oder machen Sie dies selbst in GitHub Desktop:
```
Committe diese Änderungen.
```

## Schritt 6: Zweiter Vibe - Daten erkunden

Bevor Sie ein Dashboard bauen, verstehen Sie, welche Daten Sie haben.

- Geben Sie im Claude Code-Terminal ein:

```
Zeige mir welche Spalten in diesen NBA-Daten verfügbar sind. Erstelle dann eine Zusammenfassung mit: Anzahl der Spieler, Anzahl der Teams, durchschnittliche Punkte pro Spieler, und wer die meisten Assists und Rebounds hat.
```

- Drücken Sie Enter
- Claude erkundet den Datensatz und zeigt Ihnen interessante Statistiken
- Schauen Sie sich die Ausgabe an, um verfügbare Spalten wie: player_name, team, points, assists, rebounds, field_goal_percentage, usw. zu sehen

Diese Exploration hilft Ihnen zu entscheiden, was in Ihr Dashboard kommt.

**Speichern Sie Ihren Fortschritt:** Bitten Sie Claude zu committen oder nutzen Sie GitHub Desktop.

## Schritt 7: Dritter Vibe - Einfache Shiny-App erstellen

Zeit, das interaktive Dashboard zu bauen.

- Geben Sie im Claude Code-Terminal ein:

```
Erstelle eine Shiny-App in einer Datei namens app.R, die eine interaktive Tabelle mit NBA-Spielerstatistiken zeigt. Füge Spalten für Spielername, Team, Punkte, Assists und Rebounds hinzu. Füge einen Schieberegler hinzu, um Spieler nach Mindestpunktzahl zu filtern (von 0 bis 1000). Mache es sauber und professionell.
```

- Drücken Sie Enter
- Claude erstellt `app.R` mit einer vollständigen Shiny-Anwendung
- Warten Sie, bis Claude die Datei fertig geschrieben hat

## Schritt 8: Die Shiny-App ausführen

Testen Sie Ihr Dashboard, um zu sehen, ob es funktioniert.

- Schauen Sie oben rechts im VS Code-Editor (wo `app.R` geöffnet ist)
- Finden Sie die **▶**-Schaltfläche mit einem Dropdown-Pfeil
- Klicken Sie auf das Dropdown und wählen Sie **Run Shiny App**
- Die App startet und eine Benachrichtigung erscheint: **Open in Browser**
- Klicken Sie auf **Open in Browser**
- Das NBA-Dashboard öffnet sich in Ihrem Webbrowser
- Versuchen Sie, den Punkte-Schieberegler zu bewegen – die Tabelle filtert in Echtzeit
- Scrollen Sie durch die Spielerdaten
- Committen Sie Änderungen, wenn die App funktioniert

Wenn etwas nicht funktioniert, kopieren Sie alle Fehlermeldungen und fügen Sie sie bei Claude ein, um sie zu beheben.

## Schritt 9: Vierter Vibe - Visualisierung hinzufügen

Tabellen sind nützlich, aber Visualisierungen erzählen bessere Geschichten.

- Zurück im Claude Code-Terminal, geben Sie ein:

```
Füge unterhalb der Tabelle ein Balkendiagramm hinzu, das die Top 15 Spieler nach Punkten zeigt. Verwende verschiedene Farben für jeden Spieler. Füge auch ein Streudiagramm hinzu, das die Beziehung zwischen Punkten und Assists für alle gefilterten Spieler zeigt.
```

- Drücken Sie Enter
- Claude aktualisiert `app.R` mit Visualisierungscode
- Klicken Sie erneut auf **Run Shiny App**, um die App neu zu laden
- Aktualisieren Sie Ihren Browser
- Sie sehen jetzt ein buntes Balkendiagramm und ein Streudiagramm
- Bewegen Sie den Schieberegler – alle Visualisierungen aktualisieren sich zusammen

Das ist Vibe Coding in Aktion: Feature beschreiben, testen, iterieren.

## Schritt 10: Fünfter Vibe - Team-Filter hinzufügen

Machen Sie das Dashboard interaktiver mit Teamauswahl.

- Geben Sie im Claude Code-Terminal ein:

```
Füge ein Dropdown-Menü hinzu, um Spieler nach Team zu filtern. Platziere es oben. Wenn ich ein Team auswähle, zeige nur Spieler aus diesem Team. Füge eine "Alle Teams"-Option hinzu, um alle anzuzeigen.
```

- Drücken Sie Enter
- Claude fügt den Team-Filter hinzu
- Aktualisieren Sie Ihren Browser
- Testen Sie das Dropdown – wählen Sie verschiedene Teams wie Lakers, Warriors, Celtics
- Beobachten Sie, wie Tabelle und Diagramme sich für jedes Team aktualisieren

Sie bauen ein professionelles Dashboard durch ein Gespräch.

## Schritt 11: Überprüfen und Committen

Überprüfen Sie vor dem Committen, was Claude erstellt hat.

- Klicken Sie im VS Code Explorer auf `app.R`, um es zu öffnen
- Überfliegen Sie den Code – beachten Sie das UI-Layout, die Server-Logik und den Plotting-Code
- Sie müssen nicht jede Zeile verstehen, aber bekommen Sie ein Gefühl für die Struktur
- Öffnen Sie GitHub Desktop
- Sie sehen `app.R` als neue Datei aufgelistet
- Das rechte Panel zeigt den gesamten Code in Grün (neue Hinzufügungen)
- Geben Sie im **Summary**-Feld unten links ein:

```
Create NBA dashboard with team filter and visualizations
```

- Klicken Sie auf **Commit to main**
- Klicken Sie auf **Push origin**, um auf GitHub zu sichern

Sie haben Ihre erste funktionierende Version gespeichert!

## Schritt 12: Iterieren und Verbessern

Vibe Coding glänzt beim Iterieren. Versuchen Sie, Funktionen hinzuzufügen, indem Sie sie beschreiben:

**Beispielanfragen an Claude:**

- "Füge ein Suchfeld für Spieler hinzu, damit ich einen Spielernamen eingeben und zu ihm springen kann"
- "Zeige die Team-Logos neben den Teamnamen im Dropdown"
- "Füge ein Liniendiagramm hinzu, das den Punkte-pro-Spiel-Trend für das ausgewählte Team zeigt"
- "Mache das Balkendiagramm sortierbar, indem man auf Spaltenüberschriften klickt"
- "Füge Tooltips zum Streudiagramm hinzu, die Spielernamen zeigen, wenn ich darüber fahre"

Nach jedem erfolgreichen Feature:
- Testen Sie es im Browser
- Wenn es funktioniert, committen Sie mit GitHub Desktop
- Wenn es nicht funktioniert, sagen Sie Claude den Fehler und bitten Sie um Korrektur
- Wenn behoben, committen Sie die funktionierende Version


**Schlüsselprinzipien:**

- **Beschreiben Sie Ergebnisse, nicht Implementierung** - Sagen Sie "zeige die Top-Scorer", nicht "verwende arrange() und head()"
- **Iterieren Sie schnell** - Testen → verfeinern → testen → verfeinern
- **Committen Sie funktionierende Versionen** - Speichern Sie jeden Erfolg, bevor Sie neue Funktionen versuchen
- **Akzeptieren Sie Fehlschläge** - Wenn Claudes Code nicht funktioniert, beschreiben Sie einfach den Fehler und bitten Sie um Korrektur
- **Behalten Sie die Kontrolle** - Sie entscheiden über Funktionen, Prioritäten und wann es gut genug ist

Jedes Mal folgen Sie dem Muster: beschreiben → testen → iterieren → committen.

## Nächste Schritte

- **Wenden Sie es auf Ihren Bereich an** - Verwenden Sie Vibe Coding für Ihre eigenen Daten (Forschung, Geschäft, Hobbys)
- **Versuchen Sie andere Pakete** - Bitten Sie Claude, `nflfastR` für Football oder `worldfootballR` für Fußball zu verwenden
- **Lernen Sie durch Fragen** - Wenn Claude Code schreibt, fragen Sie "erkläre, was diese Funktion macht", um R zu lernen
- **Teilen Sie Ihr Dashboard** - Stellen Sie es auf [shinyapps.io](https://www.shinyapps.io/) bereit (fragen Sie Claude wie)
- **Lesen Sie über Vibe Coding** - Besuchen Sie [IBMs Leitfaden](https://www.ibm.com/think/topics/vibe-coding), um mehr über diesen Programmierstil zu erfahren

## Fehlerbehebung

- **hoopR-Installation schlägt fehl** - Überprüfen Sie Ihre Internetverbindung; das Paket lädt Daten aus dem Web herunter. Versuchen Sie `install.packages("hoopR")` in einem R-Terminal auszuführen, um detaillierte Fehlermeldungen zu sehen.
- **Shiny-App startet nicht** - Überprüfen Sie, ob die Shiny-Erweiterung installiert ist (suchen Sie "Posit.shiny" in VS Code Extensions). Überprüfen Sie das Terminal auf Fehlermeldungen und fügen Sie sie bei Claude ein.
- **Keine Daten angezeigt** - Das hoopR-Paket zieht Live-Daten; wenn die NBA-Saison nicht begonnen hat, gibt es möglicherweise begrenzte Daten. Bitten Sie Claude, Beispieldaten oder eine frühere Saison zu verwenden.
- **Claude macht Fehler** - Normal! Kopieren Sie die Fehlermeldung, fügen Sie sie bei Claude ein und sagen Sie "behebe diesen Fehler". Vibe Coding beinhaltet Iteration und Debugging.
- **Kann nicht auf GitHub pushen** - Stellen Sie sicher, dass Sie in GitHub Desktop angemeldet sind und das Repository veröffentlicht haben (Schritt 1). Überprüfen Sie Ihre Internetverbindung.

## Workflow-Überblick

Dieses Tutorial kombinierte mehrere Technologien in einem Workflow:

- **GitHub Desktop** - Versionskontrolle mit visueller Oberfläche (Repos erstellen, committen, pushen)
- **Docker-Container** - Isolierte R-Umgebung mit allen vorinstallierten Abhängigkeiten
- **VS Code** - Code-Editor, der sich mit dem Docker-Container verbindet
- **Claude Code** - KI-Assistent, der R- und Shiny-Code aus Ihren Beschreibungen schreibt
- **hoopR-Paket** - NBA-Datenquelle mit einfacher API
- **Shiny-Framework** - Interaktive Web-Apps in R

Die Magie liegt nicht in einem einzelnen Tool – es ist, wie Vibe Coding Sie beschreiben lässt, was Sie wollen, und schnell iterieren. Sie sind von einem leeren Projekt zu einem funktionierenden Sport-Dashboard in unter 30 Minuten gekommen, ohne eine einzige Zeile Code manuell zu schreiben.

## Täglicher Workflow

Nach dieser ersten Einrichtung wird Ihre tägliche Vibe-Coding-Routine:

1. **Docker Desktop starten** - Starten Sie die App, warten Sie auf den grünen Status
2. **VS Code öffnen** - Öffnen Sie Ihr Projekt, öffnen Sie im Container neu falls nötig
3. **Claude Code starten** - Geben Sie `claude` im Terminal ein
4. **Beschreiben Sie Ihr Ziel** - "Add a feature that..." oder "Fix the bug where..."
5. **Testen Sie die Änderungen** - Führen Sie Ihre App aus, prüfen Sie ob sie funktioniert
6. **Iterieren oder committen** - Wenn kaputt, beschreiben Sie die Korrektur; wenn funktioniert, committen Sie mit GitHub Desktop
7. **Regelmäßig pushen** - Klicken Sie auf **Push origin**, um auf GitHub zu sichern

Je mehr Sie üben, desto besser werden Sie darin zu beschreiben, was Sie wollen. Vibe Coding ist eine Fähigkeit – Sie lernen, welche Arten von Beschreibungen am besten funktionieren und wie Sie große Ideen in testbare Teile aufteilen.

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
