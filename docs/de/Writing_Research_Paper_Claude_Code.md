[Startseite](./)

# Eine Forschungsarbeit mit Claude Code schreiben

Schreiben Sie Forschungsarbeiten mit Claude Code als Assistent für Recherche, Brainstorming, Planung, Entwurf und Bearbeitung. Automatisieren Sie dann diesen Prozess, indem Sie einen Vorlage-Slash-Befehl erstellen. Sehen Sie ein [Beispielpapier](./example_paper.md), das mit diesem Workflow erstellt wurde.

## Wichtige Konzepte

- **Workflow** - Recherche → Brainstorming → Fokussierte Recherche → Gliederung → Entwurf → Manuell überarbeiten → Mit KI polieren → Abstract hinzufügen → Titel verbessern → Referenzen prüfen → Mit KI korrekturlesen
- **KI-Assistent** - Der Mensch trifft wichtige Entscheidungen, während die KI die mühsame Arbeit erledigt
- **Claude Code** - Agentisches KI-System, das das Web durchsucht, Recherchen organisiert und Inhalte durch einfache Anfragen verfasst
- **Slash-Befehl** - Ein angepasster, detaillierter Prompt, der in Claude Code wiederverwendet werden kann

## Was Sie benötigen

- Abgeschlossenes Tutorial [Claude Code in VS Code unter Windows](./Claude_Code_in_VS_Code_Win) oder [Claude Code in VS Code auf dem Mac](./Claude_Code_in_VS_Code_Mac)
- 30-40 Minuten

## Schritt 1: Einen Projektordner erstellen

Erstellen Sie einen Ordner für Ihre Forschungsarbeit:

- Öffnen Sie den **Datei-Explorer** (Windows) oder **Finder** (Mac)
- Navigieren Sie zu **Dokumente**
- Erstellen Sie einen neuen Ordner namens `test_claude`

Alles über dieses Projekt passiert in diesem Ordner.

## Schritt 2: VS Code starten
Für Windows:
- Klicken Sie auf die **Windows-Starttaste** (unten links auf Ihrem Bildschirm)
- Geben Sie `Visual Studio Code` oder `VS Code` in das Suchfeld ein
- Klicken Sie auf **Visual Studio Code**, wenn es in den Suchergebnissen erscheint
- VS Code öffnet sich mit einem Willkommen-Tab – Sie können diesen Tab schließen
- Schauen Sie in die untere linke Ecke von VS Code – Sie sehen ein blaues oder grünes Symbol
- Klicken Sie auf dieses Symbol, um das Remote-Verbindungsmenü zu öffnen
- Wählen Sie **Connect to WSL** aus dem Menü
- VS Code wird neu geladen und verbindet sich mit Ihrer Ubuntu-Installation
- Die untere linke Ecke sollte jetzt **WSL: Ubuntu** anzeigen

Für Mac:
- Öffnen Sie den **Finder** und gehen Sie zu **Programme**
- Finden Sie **Visual Studio Code** und doppelklicken Sie darauf
- Wenn Sie eine Warnung sehen „Visual Studio Code ist eine aus dem Internet heruntergeladene App", klicken Sie auf **Öffnen**
- VS Code öffnet sich mit einem Willkommen-Tab – Sie können diesen Tab schließen

## Schritt 3: Den Ordner in VS Code öffnen
Für Windows über WSL:
- Klicken Sie in VS Code (noch mit WSL verbunden) in der Menüleiste auf **File**, dann auf **Open Folder**
- Ein **Open Folder**-Dropdown erscheint oben in der Mitte.
- Finden Sie Ihren Ordner durch Eingabe von:
  ```
  /mnt/c/Users/IHR_BENUTZERNAME/Documents/test_claude
  ```
  Ersetzen Sie `IHR_BENUTZERNAME` durch Ihren Windows-Benutzernamen (z.B. `Max.Mustermann`)
- Klicken Sie auf **OK**. VS Code lädt mit Ihrem `test_claude`-Ordner neu


Für Mac:
- Klicken Sie in VS Code in der Menüleiste auf **File**, dann auf **Open Folder**
- Navigieren Sie zum und wählen Sie den `test_claude`-Ordner
- Klicken Sie auf **Öffnen** (Mac) oder **OK** (Windows)
- Wenn Sie gefragt werden „Vertrauen Sie den Autoren?", klicken Sie auf **Ja, ich vertraue den Autoren**

## Schritt 4: Claude Code starten

- Öffnen Sie ein Terminal: Klicken Sie auf **Terminal** im VS Code-Hauptmenü, dann auf **New Terminal**
- Geben Sie im Terminal-Panel ein:
  ```
  claude
  ```
- Claude Code startet und ist bereit, bei Ihrer Forschungsarbeit zu helfen

## Schritt 5: Erste Recherche

Bitten Sie Claude, Ihr Thema zu recherchieren. Kopieren und fügen Sie diesen Prompt in Claude Code ein und ersetzen Sie das Thema durch Ihr eigenes:

```
Ich schreibe eine Forschungsarbeit von etwa 1.000 Wörtern über die Einführung von KI am Arbeitsplatz.
Suche nach aktuellen Daten (2023-2025) zu:
- Produktivitätssteigerungen durch KI-Tools
- Sorgen über Arbeitsplatzverluste und Statistiken
- Praxisbeispiele von Unternehmen

Anforderungen:
- Peer-Review-Forschung und glaubwürdige Branchenberichte bevorzugen
- Anekdoten und Meinungsartikel vermeiden
- Jede Quelle mit einer 1-3-satzigen Zusammenfassung auflisten
- Quellen nach Themen gruppieren

Speichern als general_research.md
```

Claude durchsucht das Web und organisiert die Ergebnisse in einer Datei namens `general_research.md`. Dies kann ein oder zwei Minuten dauern. Wenn fertig, bitten Sie um eine Zusammenfassung:

```
Gib mir eine kurze Zusammenfassung.
```

Überprüfen Sie Claudes Zusammenfassung, um einen schnellen Überblick über die Recherchelandschaft zu erhalten.

## Schritt 6: Die Quellen lesen
Lesen Sie das Recherche-Dokument durch und klicken Sie durch zu den Originalquellen, um die Informationen zu verifizieren:

1. Klicken Sie auf `general_research.md` im Explorer-Panel links
2. Zeigen Sie das formatierte Dokument in der Vorschau an: Rechtsklick auf den Tab `general_research.md` und wählen Sie **Open Preview**
3. Klicken Sie auf die Quellen-Links, um die Originalartikel und -studien zu lesen

## Schritt 7: Ihren Ansatz brainstormen

Bitten Sie Claude beim Brainstorming zu helfen:

```
Basierend auf dieser Recherche, schlage 3-4 Ansätze vor, die ich für diese Arbeit nehmen könnte.
```

Überprüfen Sie die Ansätze und wählen Sie den, der Sie am meisten interessiert.

## Schritt 8: Fokussierte Recherche

Jetzt, da Sie Ihren Ansatz haben, bitten Sie Claude um gezielte Recherche:

```
Ich möchte mich auf [Ihr gewählter Ansatz] konzentrieren. Suche nach spezifischeren Daten
und Beispielen, die diese Perspektive unterstützen. Speichern als focused_research.md
```

Claude findet gezielte Informationen.

## Schritt 9: Ihren Plan erstellen

Bitten Sie Claude, eine Gliederung basierend auf Ihrem gewählten Ansatz zu erstellen:

```
Gib mir 3 Optionen für eine kurze Gliederung meiner Arbeit basierend auf der fokussierten
Recherche und meinem gewählten Ansatz. Verwende Aufzählungspunkte für den narrativen Ablauf.
Speichern als outlines.md
```

Überprüfen Sie die Gliederung und bitten Sie Claude bei Bedarf um Anpassungen (z.B. „Lass Abschnitt 2 mehr auf Fallstudien fokussieren" oder „Füge einen Abschnitt über Einschränkungen hinzu").

## Schritt 10: Die Arbeit entwerfen

Wählen Sie Ihre Gliederung und bitten Sie Claude, den vollständigen Entwurf zu schreiben:

```
Mir gefällt Gliederung Nr. 2 [Ihre gewählte Option].

Schreibe eine Forschungsarbeit von etwa 1.000 Wörtern basierend auf der Gliederung und Recherche.

Struktur:
- Einleitung: Aufhänger, Kontext, These
- Hauptteil: 2-3 Abschnitte mit Argumenten, Statistiken und Beispielen
- Fazit: Zusammenfassung und Implikationen

Stil:
- Klare, prägnante Sätze (durchschnittlich 15-20 Wörter)
- Aktive Stimme, analytischer Ton
- Statistiken in den Fließtext einweben (keine Aufzählungslisten)
- Fließende Übergänge zwischen Absätzen

Zitate:
- Nummerierte Referenzen [1], [2], etc. nach Behauptungen verwenden
- 5-15 Referenzen einbeziehen
- Einen Literaturverzeichnis-Abschnitt am Ende hinzufügen

Speichern als paper.md
```

Claude schreibt den Entwurf.

## Schritt 11: Manuell überarbeiten

Öffnen Sie `paper.md` in Ihrem Texteditor. Lesen Sie sorgfältig durch und nehmen Sie Ihre eigenen Überarbeitungen vor:
- Fügen Sie Ihre persönliche Stimme und Erkenntnisse hinzu
- Passen Sie Argumente an Ihr Denken an
- Korrigieren Sie unbeholfene Formulierungen
- Stellen Sie sicher, dass Zitate korrekt sind

Speichern Sie Ihre Änderungen im Editor.

## Schritt 12: Mit KI polieren

Bitten Sie Claude, bestimmte Abschnitte zu verbessern:

```
Mache die Einleitung ansprechender mit einem überzeugenden Aufhänger.
```

## Schritt 13: Ein Abstract hinzufügen

Bitten Sie Claude, am Anfang eine kurze Zusammenfassung hinzuzufügen:

```
Füge ein Abstract am Anfang der Arbeit hinzu. Schreibe 2-3 kurze Sätze,
die die Arbeit zusammenfassen.
```

Claude fügt das Abstract hinzu. Überprüfen und bearbeiten Sie, um sicherzustellen, dass es das Wesen Ihrer Arbeit korrekt erfasst.

## Schritt 14: Titel verbessern

Bitten Sie Claude, Ihnen einige Optionen für den Titel zu geben:

```
Gib mir einige Optionen für den Titel. Mache ihn ansprechender.
```

Wählen Sie einen Titel. Fügen Sie Ihre eigene Note hinzu:

```
Mir gefällt Option Nr. 2 [Ihre Wahl]. Bearbeite die Datei.
```

## Schritt 15: Referenzen prüfen (Optional)
Bitten Sie Claude zu verifizieren, dass Ihre Zitate konsistent und vollständig sind:
```
Überprüfe alle Referenzen in meiner Arbeit:
- Verifiziere, dass jede Zitatnummer [1], [2], etc. eine passende Referenz hat
- Verifiziere, dass jede Referenz in der Liste tatsächlich in der Arbeit zitiert wird
- Prüfe, dass Autorennamen und Titel konsistent sind
- Verifiziere, dass die zitierten Daten und Beispiele in der Quelle erscheinen
```

Hinweis: Claude kann nur öffentlich zugängliche Quellen verifizieren. Für kostenpflichtige Artikel prüfen Sie manuell, ob Ihre Zitate mit dem übereinstimmen, was Sie gelesen haben.

## Schritt 16: Mit KI korrekturlesen

Bitten Sie Claude um ein abschließendes Korrekturlesen:

```
Führe ein abschließendes Korrekturlesen der Arbeit durch:
- Behebe Rechtschreib- und Grammatikfehler
- Stelle konsistente Formatierung durchgehend sicher
- Prüfe Fluss und Übergänge
```

Überprüfen Sie Claudes Änderungen.

**Export nach Word:** Klicken Sie in VS Code mit der rechten Maustaste auf den Tab `paper.md` und wählen Sie **Open Preview**. Klicken Sie in den Vorschaubereich, dann klicken Sie auf **Edit > Select All** und **Edit > Copy**. Fügen Sie in Microsoft Word ein – die Formatierung bleibt erhalten.

## Schritt 17: Einen Slash-Befehl für zukünftige Arbeiten erstellen

Speichern Sie diesen Workflow als wiederverwendbaren Slash-Befehl für Ihre nächste Forschungsarbeit:

```
Erstelle einen Slash-Befehl namens /research-paper, der mich durch
diesen gesamten Workflow führt. Speichere ihn, damit ich ihn für zukünftige Forschungsarbeiten zu verschiedenen Themen verwenden kann.
```

Claude erstellt einen benutzerdefinierten Slash-Befehl in Ihrem `.claude/commands/`-Ordner. Es ist eine Markdown-Datei mit einem Prompt. Sie können Ihre nächste Forschungsarbeit einfach durch Eingabe von `/research-paper [Ihr Thema]` starten!

## Schritt 18: Feedback einholen

LLMs haben kein Gedächtnis. Für jede Antwort müssen wir alle unsere vorherigen Gespräche in der Chat-Sitzung als Kontext senden. Je länger die Interaktion wird, desto mehr müssen wir uns der Länge des Kontexts bewusst sein. Wenn er nicht relevant ist oder wir einen saubereren Kontext bieten können, profitieren wir von einem Neuanfang.

Löschen Sie Claudes Gedächtnis, um Feedback zu Ihrer Arbeit zu erhalten. Geben Sie ein:

```
/clear
```

Dies entfernt den gesamten Gesprächsverlauf, sodass Claude Ihre Arbeit mit frischen Augen liest. Bitten Sie nun um Feedback:

```
Lies paper.md und gib mir ehrliches Feedback.
```

Claude wird Ihre Arbeit kritisieren, ohne davon beeinflusst zu sein, sie geschrieben zu haben. Nehmen Sie basierend auf dem Feedback letzte Überarbeitungen vor.


## Der komplette Workflow

1. **Ordner erstellen** - Projektordner in Dokumente einrichten
2. **In VS Code öffnen** - Den Ordner in VS Code öffnen
3. **Claude Code starten** - Claude Code vom Terminal aus starten
4. **Recherche** - Claude sucht nach allgemeinen Informationen zu Ihrem Thema
5. **Quellen lesen** - Die Recherche in Ihrem Texteditor überprüfen
6. **Brainstorming** - Ihren Ansatz/Perspektive wählen
7. **Fokussierte Recherche** - Claude findet gezielte Daten für Ihren gewählten Ansatz
8. **Plan** - Claude erstellt Gliederungsoptionen basierend auf Ihrer Perspektive
9. **Entwurf** - Claude schreibt die vollständige Arbeit mit Referenzen
10. **Manuell überarbeiten** - Sie fügen Ihre Stimme hinzu und nehmen Änderungen vor
11. **Mit KI polieren** - Claude verbessert bestimmte Abschnitte
12. **Abstract hinzufügen** - Claude erstellt eine Zusammenfassung
13. **Titel verbessern** - Claude schlägt Titeloptionen vor, Sie passen an
14. **Referenzen prüfen** - (Optional) Claude verifiziert alle Zitate
15. **Mit KI korrekturlesen** - Claude behebt Fehler und verbessert den Fluss
16. **Slash-Befehl erstellen** - Den Workflow für zukünftige Arbeiten speichern
17. **Frisches Feedback einholen** - Gedächtnis für unvoreingenommene Kritik löschen

## Nächste Schritte

Jetzt, da Sie den `/research-paper`-Slash-Befehl haben, versuchen Sie, weitere Arbeiten zu schreiben:

- **Technologie:** `/research-paper "Auswirkungen sozialer Medien auf die psychische Gesundheit von Teenagern"`
- **Wirtschaft:** `/research-paper "Produktivität bei Remote-Arbeit"`
- **Wissenschaft:** `/research-paper "Ethik der CRISPR-Gen-Editierung"`
- **Format:** Bitten Sie Claude `Gib mir die Arbeit im LaTeX-Format`

Der Slash-Befehl führt Sie automatisch durch den gesamten Workflow! Vergessen Sie nicht, den Speicher zu löschen, wenn Sie das Thema wechseln.

## Fehlerbehebung

- **Claude-Suchergebnisse scheinen veraltet:** Geben Sie „Suche nach Daten von 2024-2025 zu [Thema]" an
- **Entwurf ist zu lang/kurz:** Sagen Sie Claude: „Mache dies ungefähr 1.000 Wörter lang"
- **Dateien nicht gefunden:** Geben Sie im Terminal `ls` ein, um alle Dateien im aktuellen Ordner aufzulisten

## Was Sie Claude fragen können

- `suche nach aktuelleren Statistiken zu [Thema]` - Neuere Daten finden
- `fasse die Hauptargumente in dieser Arbeit zusammen` - Überblick erhalten
- `mache das Fazit überzeugender` - Bestimmte Abschnitte verbessern
- `zitiere alle Quellen im APA-Format` - Referenzen formatieren

Claude erledigt Recherche und Schreiben durch natürliche Sprache – keine Befehle zum Auswendiglernen!

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 9. Dezember 2025.
