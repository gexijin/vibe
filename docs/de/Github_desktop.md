[Startseite](./)

# Erste Schritte mit Versionskontrolle

Sie arbeiten an einem Projekt und nehmen Änderungen vor, die alles kaputtmachen. Sie können sich nicht erinnern, was Sie geändert haben, und wünschen sich, Sie könnten zum funktionierenden Stand zurückkehren. Versionskontrolle ist wie Speicherpunkte in einem Videospiel – jedes Mal, wenn Sie Ihre Arbeit „committen", erstellen Sie einen Wiederherstellungspunkt, zu dem Sie immer zurückkehren können. [GitHub](https://github.com) speichert Ihre Speicherpunkte in der Cloud, sodass Ihr Code sicher gesichert und von jedem Computer aus zugänglich ist.

## Wichtige Konzepte

- **Git** - Versionskontrollsoftware, die Änderungen an Ihren Dateien auf Ihrem Computer verfolgt
- **GitHub** - Website, die Ihren Code in der Cloud speichert, wie Google Drive für Code
- **GitHub Desktop** - App, die Git mit Schaltflächen statt Befehlen einfach zu bedienen macht
- **Repository (Repo)** - Ein Projektordner, der alle Ihre Änderungen verfolgt

## Was Sie benötigen

- Windows-, macOS- oder Linux-Computer
- Internetverbindung
- E-Mail-Adresse für GitHub-Konto
- 15-20 Minuten

## Schritt 1: Ein GitHub-Konto erstellen

- Öffnen Sie Ihren Webbrowser
- Gehen Sie zu [github.com](https://github.com)
- Klicken Sie auf **Sign up**
- Geben Sie Ihre E-Mail ein, erstellen Sie ein Passwort und wählen Sie einen Benutzernamen
- Schließen Sie die Verifizierungsschritte ab

## Schritt 2: GitHub Desktop herunterladen

- Gehen Sie zu [desktop.github.com](https://desktop.github.com)
- Klicken Sie auf die **Download**-Schaltfläche
- Öffnen Sie die heruntergeladene Datei zur Installation

**Unter Windows:**
- Doppelklicken Sie auf die Installationsdatei
- GitHub Desktop installiert sich und öffnet sich automatisch

**Auf dem Mac:**
- Öffnen Sie die heruntergeladene `.zip`-Datei
- Ziehen Sie **GitHub Desktop** in Ihren Programme-Ordner
- Öffnen Sie GitHub Desktop aus Programme

## Schritt 3: Bei GitHub Desktop anmelden

- Öffnen Sie GitHub Desktop
- Klicken Sie auf **Sign in to GitHub.com**
- Ihr Browser öffnet sich – klicken Sie auf **Authorize desktop**
- Kehren Sie zu GitHub Desktop zurück
- Klicken Sie auf **Finish**, um die Einrichtung abzuschließen

## Schritt 4: Ihr erstes Repository erstellen

- Klicken Sie in GitHub Desktop auf **Create a New Repository on your Hard Drive**
- Füllen Sie das Formular aus:
  - **Name:** `mein-erstes-projekt` (oder einen beliebigen Namen)
  - **Description:** `Versionskontrolle lernen` (optional)
  - **Local Path:** Wählen Sie, wo es gespeichert werden soll (Dokumente-Ordner ist in Ordnung)
  - Aktivieren Sie **Initialize this repository with a README**
- Klicken Sie auf **Create Repository**

## Schritt 5: Ihren Projektordner öffnen

- Klicken Sie in GitHub Desktop in der Menüleiste auf **Repository**
- Wählen Sie **Im Finder anzeigen** (Mac) oder **Im Explorer anzeigen** (Windows)
- Sie sehen einen Ordner mit Ihrem Projektnamen
- Darin ist eine Datei namens `README.md`

## Schritt 6: Ihre erste Änderung vornehmen

- Öffnen Sie `README.md` in einem beliebigen Texteditor (Notepad, TextEdit oder VS Code)
- Ersetzen Sie den Inhalt mit:
  ```
  # Mein erstes Projekt

  Ich lerne Versionskontrolle mit GitHub Desktop.

  ## Was ich baue

  Dies ist ein Übungsprojekt, um zu lernen, wie man:
  - Änderungen an meinem Code verfolgt
  - Speicherpunkte (Commits) erstellt
  - Meine Arbeit auf GitHub sichert
  ```
- Klicken Sie auf **Datei** → **Speichern**

## Schritt 7: Ihren ersten Commit erstellen (Speicherpunkt)

- Kehren Sie zu GitHub Desktop zurück
- Sie sehen Ihre Änderungen auf der rechten Seite hervorgehoben (grün = hinzugefügt, rot = entfernt)
- Geben Sie unten links eine Commit-Nachricht ein: `README mit Projektbeschreibung aktualisiert`
- Klicken Sie auf die blaue Schaltfläche **Commit to main**

## Schritt 8: Auf GitHub pushen (In die Cloud sichern)

- Klicken Sie auf die blaue Schaltfläche **Publish repository** oben
- Behalten Sie den Namen bei
- Deaktivieren Sie „Keep this code private", wenn Sie möchten, dass andere es sehen können (optional)
- Klicken Sie auf **Publish Repository**

Ihr Code ist jetzt online gesichert unter: `https://github.com/IHR-BENUTZERNAME/mein-erstes-projekt`

## Nächste Schritte

- Bearbeiten Sie Ihre README-Datei erneut und committen Sie die Änderungen
- Erstellen Sie eine neue Datei in Ihrem Projektordner und committen Sie sie
- Erkunden Sie den **History**-Tab, um zu sehen, wie sich Ihr Projekt im Laufe der Zeit entwickelt

## Fehlerbehebung

- **Kann mich nicht bei GitHub anmelden** - Überprüfen Sie Ihre Internetverbindung. Versuchen Sie, sich zuerst auf github.com anzumelden, um zu verifizieren, dass Ihre Anmeldedaten funktionieren.
- **Änderungen erscheinen nicht in GitHub Desktop** - Stellen Sie sicher, dass Sie Ihre Dateien gespeichert haben. Klicken Sie auf **Repository** → **Aktualisieren** oder starten Sie GitHub Desktop neu.
- **Push schlägt fehl mit „rejected"-Fehler** - Jemand anderes hat Änderungen gepusht. Klicken Sie zuerst auf **Fetch origin**, dann versuchen Sie erneut zu pushen.

## Workflow-Überblick

- Nehmen Sie Änderungen an Ihren Projektdateien vor
- Überprüfen Sie Änderungen in GitHub Desktop (grün = hinzugefügt, rot = entfernt)
- Schreiben Sie eine beschreibende Commit-Nachricht und klicken Sie auf **Commit to main**
- Klicken Sie auf **Push origin**, um auf GitHub zu sichern
- Wiederholen

---

Erstellt von [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) am 7. Dezember 2025.
