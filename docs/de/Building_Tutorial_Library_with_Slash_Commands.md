[Startseite](./index.html)

# Wie Claude Code mir half, diese Tutorials zu erstellen

Mitte Dezember 2025 verbrachte ich 2 Stunden damit, meiner Forschungsassistentin per Zoom bei der Installation von Claude Code zu helfen. Mir wurde klar, dass jemand wie sie spezifische, praxisnahe Anleitungen braucht, also machte ich mich daran, umfassende Tutorials für Claude Code zu erstellen. Mein Ziel: praxisnahe, fokussierte Tutorials, die komplette Anfänger Schritt für Schritt durch echte Aufgaben führen. Keine Theorieabhandlungen. Keine umfassenden Referenzhandbücher. Einfach nur „tun Sie dies, dann das, dann das", bis Sie etwas Konkretes erreicht haben.

Was als ein paar Dokumentationsdateien begann, entwickelte sich schnell zu einer mehrsprachigen Lernplattform mit über 100 Tutorial-Dokumenten. Das Geheimnis? Ich habe sie nicht alle manuell geschrieben. Stattdessen habe ich eine Reihe von benutzerdefinierten Slash-Befehlen (im Wesentlichen wiederverwendbare Prompts) erstellt, die Claude Code in eine automatisierte Dokumentationsfabrik verwandelten – eine, die konsequent Tutorials in meinem praxisnahen, schrittweisen Stil produziert.

## Die Herausforderung

Das Erstellen von Tutorials ist zeitaufwändig. Jedes einzelne erfordert Recherche nach aktuellen Best Practices, strukturiertes anfängerfreundliches Schreiben, konsistente Formatierung, Validierung der technischen Genauigkeit, Übersetzung in mehrere Sprachen und laufende Wartung, wenn sich Tools weiterentwickeln. Dies manuell für über 20 Tutorials in mehr als 3 Sprachen zu tun, hätte Wochen gedauert.

## Die Lösung: Von manuellem Prozess zu automatisierten Slash-Befehlen

Ich erstellte fünf spezialisierte Slash-Befehle, die den gesamten Tutorial-Lebenszyklus abdeckten.

### [`/tutorial`](./assets/commands/tutorial.md) - Der Tutorial-Generator

Ich erstellte die ersten Tutorials manuell durch interaktives Prompten mit Claude. Verfeinerte den Prozess durch Iteration und bat dann Claude, den funktionierenden Prozess in einen Slash-Befehl zu kodifizieren.

Dies ist genau das Muster, das in meinem [Forschungsarbeit-Tutorial](./Writing_Research_Paper_Claude_Code.md) beschrieben wird: Gehen Sie den Workflow manuell durch, dann bitten Sie im letzten Schritt Claude, ihn als wiederverwendbaren Befehl zu speichern, der den bewährten Workflow erfasst:

1. **Recherche**: Claude durchsucht das Web nach aktuellen Informationen – keine veralteten Versionsnummern oder veralteten Methoden
2. **Planung**: Claude präsentiert, was es gelernt hat, empfiehlt einen Ansatz und skizziert die Hauptschritte
3. **Iteration**: Ich überprüfe den Plan, bitte Claude mehrmals um Überarbeitung, bis ich zufrieden bin
4. **Schreiben**: Nach der Genehmigung schreibt Claude nach strengen Formatierungsregeln:
   - Home-Link oben
   - Ansprechender Hook
   - Wichtige Konzepte
   - Schritt-für-Schritt-Anleitungen mit Aktionsverben
   - Fehlerbehebungsabschnitt
   - Erstellungsdatum
5. **Testen**: Ich teste die Schritte selbst in einem separaten Terminal, überarbeite bei Bedarf
6. **Polieren**: Manchmal bearbeite ich manuell, manchmal bitte ich Claude, es zu tun

Der Befehl erzwingt eine konsistente Struktur über alle Tutorials hinweg. Jedes Tutorial fühlt sich an, als käme es vom selben Autor – weil sie alle demselben systematischen Prozess folgten. Ich habe über 20 Tutorials zu Themen von grundlegenden Git-Operationen bis zu fortgeschrittenen Docker-Workflows generiert.

### [`/review-tutorial`](./assets/commands/review-tutorial.md) - Der Qualitätskontroll-Bot

Bei diesem bat ich Claude einfach, „einen Slash-Befehl zum Überprüfen von Tutorials zu erstellen". Keine detaillierten Spezifikationen. Claude generierte einen umfassenden dreiphasigen Workflow mit über 30 Qualitätskriterien, organisiert in Kategorien:

- **Inhaltsqualität**: Titel, Hook, Schlüsselkonzepte, Voraussetzungen, Schrittfluss, nächste Schritte, Fehlerbehebung
- **Formatierungsstandards**: Home-Link, Schrittüberschriften, Aufzählungspunkte, Fett/Backticks, Codeblöcke, Absätze
- **Anfängerfreundlichkeit**: Menübasierte Anleitungen, Plattformunterschiede, genaue Klickziele, kein Jargon
- **Technische Genauigkeit**: Korrekte Befehle, aktuelle UI, realistische Zeitschätzungen
- **Schreibqualität**: Grammatik, konsistente Terminologie, prägnante Sprache

Der Befehl präsentiert Ergebnisse in einem strukturierten Bericht und wendet dann nach Genehmigung Korrekturen an. Warum war das nötig? Zwei Gründe: Claude befolgt die `/tutorial`-Regeln nicht immer streng, und der `/tutorial`-Befehl selbst entwickelte sich weiter, während ich mehr Tutorials erstellte. Der Review-Befehl ermöglicht es mir, frühere Tutorials stapelweise zu polieren, um den neuesten Standards zu entsprechen.

### [`/translate-chinese`](./assets/commands/translate-chinese.md) & [`/translate-spanish`](./assets/commands/translate-spanish.md) - Die Lokalisierungs-Engine

Die japanischen Übersetzungen kamen zuerst – ohne Slash-Befehl. Ich bat Claude Code einfach, alle Tutorials in einem einzigen Prompt ins Japanische zu übersetzen. Claude erzeugte automatisch 8 Subagenten, die parallel liefen und jeweils verschiedene Tutorials gleichzeitig bearbeiteten.

Für folgende Sprachen bat ich Claude, „einen Slash-Befehl zum Übersetzen von Tutorials ins Chinesische zu erstellen" – keine spezifischen Richtlinien. Claude generierte einen sechsphasigen Workflow mit umfassenden Regeln:

- **Übersetzungsregeln**: Codeblöcke, technische Begriffe (Git, Docker, VS Code), Dateipfade und URLs in Englisch belassen; Anleitungstext, Überschriften und Erklärungen übersetzen
- **Sprachrichtlinien**: Ton- und Stilregeln, gängige technische Übersetzungen (Click = 点击, Install = 安装), formelle Anredekonventionen
- **Formatierungsanforderungen**: Lokalisierter Home-Link, beibehaltene Struktur, korrekte Interpunktion (。，！？ für Chinesisch, ¿? ¡! für Spanisch)
- **Qualitätsüberprüfung**: Checkliste für natürlichen Fluss, konsistente Terminologie, korrekte Zeichenverwendung

Mit den fertigen Slash-Befehlen bat ich Claude Code, alle 25 Tutorials mit Subagenten zu übersetzen. Die gesamte Übersetzung – 50 neue Dateien in zwei Sprachen – dauerte nur 15 Minuten.

Das Ergebnis: 81 übersetzte Tutorial-Dateien in chinesischen, spanischen, französischen, deutschen und japanischen Verzeichnissen – alle mit gleichbleibender Qualität und Struktur.

### [`/review-translation`](./assets/commands/review-translation.md) - Das Übersetzungspflege-Tool

Tutorials entwickeln sich weiter. Befehle ändern sich. Neue Abschnitte werden hinzugefügt. Dieser Befehl hält Übersetzungen durch einen vierphasigen Workflow synchron:

1. **Beide Versionen lesen**: Englisches Original und Übersetzung nebeneinander laden
2. **Vergleichen und Aktualisieren**: Fehlende Abschnitte, veraltete Inhalte, geänderte Befehle oder URLs identifizieren
3. **Qualität überprüfen**: Übersetzungsgenauigkeit, Sprachqualität, Formatierungskonsistenz prüfen
4. **Bericht erstellen und Beheben**: Ergebnisse präsentieren, Genehmigung einholen, Aktualisierungen anwenden

Die Qualitätsüberprüfung ist gründlich – für Japanisch prüft sie natürliche Formulierung (nicht Wort für Wort), angemessenes Höflichkeitsniveau (です/ます-Form), korrekte Partikelverwendung (は/が, を, に, で) und keinen unnatürlichen Katakana-Übergebrauch. Als ich englische Tutorials aktualisierte, konnte ich Änderungen schnell auf alle Übersetzungen übertragen und dabei die Sprachqualität beibehalten.

### Übersetzungen für natürlichen Fluss polieren

Nach dem Synchronisieren der Übersetzungen mit den englischen Originalen fügte ich einen letzten Polierschritt hinzu: jedes übersetzte Dokument einzeln auf Sprachqualität bearbeiten, ohne mit dem Englischen zu vergleichen. Dieser Schritt konzentriert sich ausschließlich darauf, den Text für Muttersprachler natürlich klingen zu lassen.

Ich verwendete Prompts in der Zielsprache. Anstatt Claude auf Englisch zu bitten, „dieses japanische Dokument zu polieren", verwendete ich ChatGPT, um die Prompts auf Japanisch, Chinesisch oder Spanisch zu schreiben. Dies schien bessere Ergebnisse zu liefern – Claude schien in dieser Sprache natürlicher zu denken, wenn die Anweisungen auch in dieser Sprache waren.

Zum Beispiel verwendete ich zum Polieren chinesischer Dokumente:
"修改 @docs/zh/ 目录下的中文文档。中文需要流畅、准确、言简意赅。提示词也要用中文。 Use subagents." Für Spanisch: "Revisa los documentos en @docs/es/. El español debe ser fluido, preciso y conciso. Use subagents." Für Japanisch: "@docs/ja/ のドキュメントを修正してください。日本語は流暢で正確、簡潔にしてください。Use subagents."

Bessere Modelle wie Opus 4.5 scheinen auch zu helfen. Dieser Polierschritt erfasste ungeschickte Formulierungen, die technisch nicht falsch waren, aber nicht natürlich klangen. Kombiniert mit Subagenten konnte ich alle über 25 Dokumente in jeder Sprache in einer einzigen Batch-Operation polieren.

## Skalierung mit Subagenten

Für wirklich parallele Arbeit verwendete ich Claudes Subagenten-Funktion. Beim Polieren japanischer Übersetzungen startete ich mehrere Review-Agenten gleichzeitig, die 19 Dateien mit koordinierten Verbesserungen verarbeiteten.

Die Kombination von Slash-Befehlen für strukturierte Workflows und Subagenten für Parallelisierung schuf eine Dokumentationspipeline, die weit über das hinausging, was manuelle Arbeit erreichen konnte.

## Die Ergebnisse

In weniger als zwei Wochen erstellte ich über 20 englische Tutorials zu Themen vom Anfänger- bis Fortgeschrittenenniveau, 81 übersetzte Tutorials in 3 Sprachen, konsistente Qualität durch automatisierte Review-Prozesse und wartbare Dokumentation mit Synchronisierungstools für Übersetzungen.

Alle Tutorials folgen derselben Struktur, demselben Schreibstil und denselben Formatierungskonventionen – weil sie durch denselben systematischen Prozess generiert wurden.

## Wichtige Lektionen

- **Beginnen Sie manuell, dann automatisieren Sie.** Führen Sie die Aufgabe zuerst manuell aus, verfeinern Sie den Prozess, dann bitten Sie Claude, ihn als Befehl zu speichern.
- **Strukturieren Sie Befehle als mehrphasige Workflows.** Sagen Sie Claude, wie es das Problem durchdenken soll, nicht nur was es tun soll.
- **Bauen Sie Qualitätskontrolle in den Prozess ein.** Erstellen Sie einen Review-Befehl neben Ihrem Generierungsbefehl.
- **Machen Sie Befehle kollaborativ, nicht autonom.** Fügen Sie Genehmigungsschritte ein. Claude erledigt die mühsamen Teile; Sie treffen strategische Entscheidungen.
- **Verwenden Sie Subagenten für Batch-Verarbeitung.** Wenn Sie viele Dokumente verarbeiten, sagen Sie explizit „Use subagents" in Ihrem Prompt. Drücken Sie zuerst Shift+Tab, um den Auto-Accept-Modus zu aktivieren – Subagenten fragen nicht nach Berechtigungen, was parallele Verarbeitung nahtlos macht.

## Fazit

Der Aufbau dieser Tutorial-Bibliothek lehrte mich, dass Automatisierung nicht bedeutet, Menschen aus dem Prozess zu entfernen – es geht darum, menschliches Urteilsvermögen zu verstärken. Ich habe keine 100+ Tutorials manuell geschrieben, aber jedes einzelne spiegelt meine Standards, meine Struktur und meine Genehmigung wider.

Slash-Befehle verwandelten Claude Code von einem hilfreichen Assistenten in eine Dokumentationsfabrik, die auf meine Anweisung arbeitet, meine Standards einhält und auf jede Projektgröße skaliert, die ich brauche.

Wenn Sie repetitive Dokumentationsaufgaben haben, machen Sie sie nicht weiter manuell. Erstellen Sie den Slash-Befehl einmal, dann setzen Sie ihn Dutzende oder Hunderte Male ein.

Das ist die Kraft systematischer Automatisierung.

---

*Möchten Sie die Slash-Befehle sehen, die ich erstellt habe? Schauen Sie sich den [Commands-Ordner](./assets/commands/) an. Die vollständige Tutorial-Bibliothek ist auf der [Projektdokumentationsseite](https://github.com/gexijin/vibe/tree/main/docs) verfügbar.*

---

**P.S.** Dieser Blogbeitrag wurde selbst von Claude Code durch iteratives Prompten erstellt:
1. „Überprüfe meinen Commit-Verlauf und schreibe einen Blogbeitrag darüber, wie ich diese Tutorials erstellt habe, mit Schwerpunkt auf meiner Verwendung von Slash-Befehlen zur Automatisierung."
2. „Reflektiere, dass der /tutorial-Befehl zuerst aus manuellem interaktivem Prompten entstanden ist."
3. „Betone meinen Tutorial-Stil: praxisnah, fokussiert, Schritt für Schritt."
4. „Füge hinzu, dass japanische Übersetzungen zuerst kamen, ohne Slash-Befehle, und dass Claude 8 Subagenten parallel verwendet hat."
5. „Füge hinzu, dass Claude die Übersetzungs-Slash-Befehle ohne spezifische Richtlinien geschrieben hat, und die Verwendung von Subagenten."
6. „Verlinke auf die gespeicherten Befehle in docs/assets/commands."
7. „Schreibe mit weniger Aufzählungspunkten um."
8. „Lies tatsächlich die Slash-Befehle und füge Details hinzu."
9. „Fasse unsere Interaktion zusammen. Füge ein P.S. darüber hinzu, wie dieser Blog generiert wurde."

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 15. Dezember 2025.
