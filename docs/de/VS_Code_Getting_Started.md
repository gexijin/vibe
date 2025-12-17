[Startseite](./)

# Erste Schritte mit VS Code

Sie möchten Code schreiben, aber Notepad oder TextEdit fühlt sich einschränkend an. Sie brauchen etwas, das Ihnen hilft, schneller zu programmieren – mit Syntax-Hervorhebung, Autovervollständigung und integrierten Tools. **VS Code ist wie ein intelligentes Notizbuch für Code** – es versteht, was Sie schreiben, und hilft Ihnen dabei. [Visual Studio Code](https://code.visualstudio.com) ist kostenlos, läuft auf jedem Betriebssystem und wird von Millionen von Entwicklern verwendet.

## Wichtige Konzepte

- **Editor** - Der Hauptbereich, in dem Sie Code schreiben
- **Explorer** - Die Seitenleiste, die Ihre Dateien und Ordner anzeigt
- **Erweiterungen** - Add-ons, die VS Code neue Funktionen geben
- **Integriertes Terminal** - Eine Befehlszeile, die in VS Code eingebaut ist

## Was Sie benötigen

- Windows-, macOS- oder Linux-Computer
- Internetverbindung
- ~500 MB Festplattenspeicher
- 20-25 Minuten

## Schritt 1: VS Code herunterladen und installieren

- Gehen Sie zu [code.visualstudio.com](https://code.visualstudio.com)
- Klicken Sie auf die Schaltfläche **Download** (es erkennt Ihr Betriebssystem)
- Führen Sie das Installationsprogramm aus:
   - **Windows:** Doppelklicken Sie auf die `.exe`, klicken Sie durch die Eingabeaufforderungen auf **Weiter**
   - **Mac:** Öffnen Sie die `.dmg`, ziehen Sie VS Code in **Programme**
   - **Linux:** Folgen Sie den Anweisungen für Ihren Paketmanager
- Starten Sie VS Code

Sie sehen einen Willkommen-Tab mit Optionen für den Einstieg.

## Schritt 2: Die Oberfläche erkunden

VS Code hat fünf Hauptbereiche:

- **Aktivitätsleiste** (linker Rand) - Symbole für Explorer, Suche, Git, Erweiterungen usw.
- **Seitenleiste** - Zeigt Inhalt für die ausgewählte Aktivität (Dateien, Suchergebnisse)
- **Editor** (Mitte) - Wo Sie Code schreiben
- **Panel** (unten) - Terminal, Probleme, Ausgabe
- **Statusleiste** (unterer Rand) - Informationen über Ihre Datei und Ihr Projekt

Klicken Sie auf das **Explorer**-Symbol (oben in der Aktivitätsleiste), um den Dateibrowser zu sehen.

## Schritt 3: Einen Ordner öffnen und erkunden

- Klicken Sie auf **Datei** → **Ordner öffnen**
- Navigieren Sie zu einem beliebigen vorhandenen Ordner auf Ihrem Computer (z.B. Dokumente)
- Klicken Sie auf **Öffnen** (oder **Ordner auswählen**)
- Wenn Sie gefragt werden „Vertrauen Sie den Autoren?", klicken Sie auf **Ja, ich vertraue den Autoren**

Die Explorer-Seitenleiste zeigt nun die Dateien Ihres Ordners:

- Klicken Sie auf einen Ordner, um ihn zu erweitern
- Klicken Sie auf eine beliebige Datei, um sie im Editor zu öffnen
- Klicken Sie auf das **Suchen**-Symbol in der Aktivitätsleiste (Lupe), um über alle Dateien zu suchen

## Schritt 4: Eine Markdown-Datei erstellen

- Klicken Sie im Explorer auf das **Neue Datei**-Symbol (Seite mit +)
- Nennen Sie sie `README.md`
- Fügen Sie diesen Inhalt hinzu:

```
# Mein Projekt

Dies ist ein **Demo-Projekt** zum Erlernen von VS Code.

## Funktionen
- Einfach zu bearbeiten
- Markdown-Formatierung
- Live-Vorschau

## Nächste Schritte
1. Mehr Inhalt hinzufügen
2. Andere Dateitypen ausprobieren
3. Erweiterungen erkunden
```
- Klicken Sie auf **Datei** → **Speichern** zum Speichern

Markdown ist ein einfaches Textformat, das Symbole wie `#` für Überschriften, `**` für Fettschrift und `-` für Listen verwendet. Es wird häufig für Dokumentation und die Kommunikation mit LLMs wie ChatGPT und Claude verwendet.

## Schritt 5: Markdown-Vorschau-Erweiterung installieren

- Klicken Sie auf das **Erweiterungen**-Symbol in der Aktivitätsleiste (das Quadrate-Symbol)
- Geben Sie `Markdown Preview Enhanced` in das Suchfeld ein
- Finden Sie **Markdown Preview Enhanced** in den Ergebnissen
- Klicken Sie auf **Installieren**

## Schritt 6: Ihre Markdown-Datei in der Vorschau anzeigen

- Öffnen Sie `README.md`, falls noch nicht geöffnet
- Klicken Sie mit der rechten Maustaste im Editor und wählen Sie **Markdown Preview Enhanced: Open Preview to the Side**

Ein Vorschau-Panel öffnet sich und zeigt Ihr formatiertes Markdown – bearbeiten Sie links, sehen Sie Änderungen rechts in Echtzeit!

## Schritt 7: Das integrierte Terminal verwenden

- Klicken Sie auf **Terminal** → **Neues Terminal**
- Probieren Sie diese Befehle aus:

**Dateien auflisten:**
```
ls
```
(In der Windows-Eingabeaufforderung verwenden Sie `dir`)

**Arbeitsverzeichnis ausgeben:**
```
pwd
```
(In der Windows-Eingabeaufforderung verwenden Sie `cd`)

**Einen neuen Ordner erstellen:**
```
mkdir notes
```

Prüfen Sie den Explorer – der `notes`-Ordner erscheint! Das Terminal läuft in Ihrem Projektordner, sodass Befehle Ihr Projekt direkt beeinflussen.

## Schritt 8: KI-Agenten in VS Code verwenden (Optional)

VS Code enthält [GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat), einen KI-Assistenten, der Code erklären, schreiben und debuggen kann.

- Öffnen Sie die Datei `README.md` (oder eine andere Datei in Ihrem Projekt)
- Klicken Sie in der Titelleiste auf **Chat** → **Chat öffnen** (oder drücken Sie `Strg+Alt+I` unter Windows/Linux, `Ctrl+Cmd+I` auf Mac)
- Wenn Sie dazu aufgefordert werden, melden Sie sich mit Ihrem **GitHub-Konto** an (ein kostenloser Plan ist verfügbar)
- Geben Sie im Chat-Panel ein: „Erkläre diese Datei"
- Drücken Sie **Eingabe**

GitHub Copilot analysiert Ihre Datei und erklärt, was sie tut. Sie können es bitten, neuen Code zu schreiben, Fehler zu beheben oder Fragen zu beantworten wie „Wie füge ich weitere Funktionen hinzu?"

**Tipp:** Für [Inline-Bearbeitung](https://code.visualstudio.com/docs/copilot/copilot-chat) markieren Sie Code in einer beliebigen Datei und drücken Sie `Strg+I` (Windows/Linux) oder `Cmd+I` (Mac), um Copilot zu bitten, nur diesen Abschnitt zu ändern, zu reparieren oder zu erklären.

## So öffnen Sie Ihr Projekt erneut

- Öffnen Sie VS Code aus dem Startmenü (Windows), Spotlight (Mac) oder Programme (Linux)
- Klicken Sie auf **Datei** → **Zuletzt geöffnet** → wählen Sie Ihren Ordner
- Oder klicken Sie auf **Datei** → **Ordner öffnen** und navigieren Sie dorthin

## Fehlerbehebung

- **Vorschau wird nicht angezeigt:** Stellen Sie sicher, dass die Markdown Preview Enhanced-Erweiterung installiert ist und Sie eine `.md`-Datei geöffnet haben
- **Terminal zeigt falsches Verzeichnis:** Klicken Sie auf das Papierkorb-Symbol im Terminal-Panel, dann klicken Sie auf **Terminal** → **Neues Terminal**
- **Chat-Menü nicht sichtbar:** GitHub Copilot Chat muss möglicherweise installiert werden – klicken Sie auf das **Erweiterungen**-Symbol, suchen Sie nach „GitHub Copilot Chat" und installieren Sie es
- **Erweiterungen funktionieren nicht:** Klicken Sie auf **Ansicht** → **Befehlspalette**, geben Sie „reload window" ein und wählen Sie **Developer: Reload Window**

## Der komplette Workflow

1. Ordner in VS Code öffnen
2. Dateien erstellen/bearbeiten
3. Erweiterungen für die Vorschau verwenden
4. Terminal für Befehle verwenden
5. KI verwenden, um Code zu verstehen und zu verbessern
6. Speichern und wiederholen

## Nächste Schritte

- **Andere Dateitypen ausprobieren:** Erstellen Sie `.html`-, `.css`-, `.js`- oder `.py`-Dateien und sehen Sie VS Codes Syntax-Hervorhebung
- **KI-Funktionen erkunden:** Bitten Sie KI, Code zu schreiben, Fehler zu beheben oder Verbesserungen für Ihre Projekte vorzuschlagen
- **Weitere Erweiterungen installieren:** Probieren Sie „Prettier" für Auto-Formatierung oder „GitLens" für Git-Funktionen
- **Tastenkürzel lernen:** Klicken Sie auf **Hilfe** → **Tastenkombinationsreferenz**, um Ihren Workflow zu beschleunigen

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
