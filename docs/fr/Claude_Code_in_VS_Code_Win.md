---
title: "Configurer VS Code pour Claude Code sur Windows"
lang: "fr"
---
[Accueil](./)

# Configurer VS Code pour Claude Code sur Windows

Vous avez installé Claude Code sur votre machine Windows - vous souhaitez maintenant un éditeur visuel pour travailler avec votre code. VS Code vous permet d'éditer des fichiers visuellement tout en exécutant Claude Code dans le terminal intégré, côte à côte dans la même fenêtre.

## Concepts Clés

- **VS Code** - Un éditeur de code gratuit de Microsoft avec un terminal intégré
- **Terminal Intégré** - Un panneau de terminal PowerShell à l'intérieur de VS Code, pour que vous n'ayez pas à changer de fenêtre pour exécuter Claude Code
- **Dossier de travail** - Le dossier que vous ouvrez dans VS Code ; Claude Code lit et modifie les fichiers qu'il contient

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Installer Claude Code sur Windows](./Install_CLAUDE_Code_Win)
- Avoir terminé [Les Bases de VS Code](./VS_Code_Getting_Started)
- 10-15 minutes

## Étape 1 : Créer un Dossier de Projet

- Ouvrez **l'Explorateur de fichiers** (cliquez sur l'icône de dossier dans votre barre des tâches)
- Naviguez vers **Documents**
- Faites un clic droit dans l'espace vide, sélectionnez **Nouveau > Dossier**
- Nommez le dossier `test_claude`

## Étape 2 : Démarrer VS Code

- Cliquez sur le **bouton Démarrer de Windows** (coin inférieur gauche de votre écran)
- Tapez `Visual Studio Code` ou `VS Code` dans la zone de recherche
- Cliquez sur **Visual Studio Code** lorsqu'il apparaît dans les résultats de recherche
- VS Code s'ouvre avec un onglet de bienvenue - vous pouvez fermer cet onglet


## Étape 3 : Ouvrir le Dossier dans VS Code

- Dans VS Code, cliquez sur **File** dans la barre de menus, puis **Open Folder**
- Naviguez vers **Documents**, sélectionnez le dossier `test_claude`
- Cliquez sur **Select Folder**. VS Code se recharge avec votre dossier `test_claude`
- Si l'on vous demande « Do you trust the authors? », cliquez sur **Yes, I trust the authors**


## Étape 4 : Démarrer Claude Code

- Après le rechargement de VS Code, ouvrez un nouveau terminal : cliquez sur **Terminal** dans la barre de menus, puis **New Terminal**
- Dans le panneau du terminal, tapez :
  ```
  claude
  ```

Connectez-vous avec votre abonnement Claude en suivant le [tutoriel d'installation](Install_CLAUDE_Code_Win.md). Après vous être connecté, vous verrez un message de bienvenue et l'invite Claude Code.

## Étape 5 : Tester le Flux de Travail

- Dans Claude Code, tapez :
```
Écris un court article expliquant pourquoi les LLM aiment utiliser le format Markdown. Enregistre-le sous article.md
```
- Claude Code crée le fichier - vous verrez `article.md` apparaître dans le panneau Explorateur à gauche
- Cliquez sur `article.md` dans l'Explorateur pour le visualiser dans l'éditeur
- Pour prévisualiser l'article formaté : faites un clic droit sur l'onglet `article.md` et sélectionnez **Open Preview**
- Vous verrez le Markdown rendu avec des titres, des puces et une mise en forme appropriés

## Réouvrir Claude dans VS Code Ultérieurement

Après avoir fermé VS Code, voici comment revenir à votre projet :

- **Option A :** Ouvrez VS Code, cliquez sur **File > Open Recent**, et sélectionnez `test_claude`
- **Option B :** Ouvrez **l'Explorateur de fichiers**, faites un clic droit sur le dossier `test_claude`, et sélectionnez **Open with Code**

## Prochaines Étapes

- Demandez à Claude Code d'expliquer une base de code existante : « Explique ce que fait ce projet »
- Demandez à Claude Code de vous aider à écrire de nouvelles fonctionnalités : « Ajoute une fonction qui calcule la moyenne d'une liste »
- Utilisez Claude Code pour corriger des bugs : « Ce code donne une erreur, peux-tu le corriger ? »
- Essayez l'extension VS Code de Claude Code pour une interface visuelle avec des diffs en ligne (recherchez « Claude Code » dans Extensions)

## Dépannage

- **Commande `claude` introuvable** - Exécutez `claude --version` dans le terminal de VS Code pour vérifier si Claude Code est installé ; sinon, suivez d'abord le [tutoriel d'installation](Install_CLAUDE_Code_Win.md)
- **Vous utilisez WSL ?** - Si vous avez suivi le parcours optionnel WSL/Ubuntu, installez l'extension **WSL** depuis la barre latérale Extensions, cliquez sur l'icône bleue/verte dans le coin inférieur gauche, et sélectionnez **Connect to WSL** avant d'ouvrir votre dossier de projet (accessible à `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude`)

## Aperçu du Flux de Travail

- **VS Code** s'exécute sur Windows et fournit l'interface d'éditeur visuel
- **Le Terminal Intégré** exécute Claude Code directement dans VS Code
- Éditez les fichiers dans l'éditeur, discutez avec Claude Code dans le terminal - le meilleur des deux mondes

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 10 décembre 2025.
