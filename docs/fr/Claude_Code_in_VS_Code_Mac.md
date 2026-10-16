---
title: "Utiliser Claude Code depuis VS Code sur Mac"
lang: "fr"
---
[Accueil](./)

# Utiliser Claude Code depuis VS Code sur Mac

Vous avez installé Claude Code sur votre Mac - maintenant vous souhaitez un éditeur visuel pour travailler avec votre code. VS Code vous permet d'éditer des fichiers visuellement tout en exécutant Claude Code dans le terminal intégré. C'est comme avoir votre éditeur de code et votre assistant IA côte à côte dans une seule fenêtre.

## Concepts Clés

- **VS Code** - Un éditeur de code gratuit de Microsoft qui fonctionne sur Mac
- **Terminal Intégré** - Un panneau de terminal à l'intérieur de VS Code où vous exécutez Claude Code
- **Panneau Explorateur** - Le navigateur de fichiers sur le côté gauche de VS Code

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Installer Claude Code sur Mac](./Install_Claude_Code_MacOS)
- Avoir terminé [Notions de Base de VS Code](./VS_Code_Getting_Started)
- 10-15 minutes

## Étape 1 : Démarrer VS Code

- Ouvrez **Finder** et allez dans **Applications**
- Trouvez **Visual Studio Code** et double-cliquez dessus
- Si vous voyez un avertissement "Visual Studio Code est une application téléchargée depuis Internet", cliquez sur **Ouvrir**
- VS Code s'ouvre avec un onglet de bienvenue - vous pouvez fermer cet onglet

**Astuce :** Faites un clic droit sur VS Code dans le Dock et sélectionnez **Options > Garder dans le Dock** pour un accès facile ultérieurement.

## Étape 2 : Créer un Dossier de Projet

- Ouvrez **Finder**
- Cliquez sur **Documents** dans la barre latérale gauche
- Cliquez sur **Fichier** dans la barre de menu, puis **Nouveau dossier**
- Nommez le dossier `test_claude`

## Étape 3 : Ouvrir le Dossier dans VS Code

- Dans VS Code, cliquez sur **File** dans la barre de menu, puis **Open Folder**
- Naviguez vers **Documents** et sélectionnez le dossier `test_claude` que vous avez créé
- Cliquez sur **Open**
- Si on vous demande "Do you trust the authors of the files in this folder?", cliquez sur **Yes, I trust the authors**

Vous devriez maintenant voir `TEST_CLAUDE` dans le panneau **Explorer** sur le côté gauche.

## Étape 4 : Démarrer Claude Code et se Connecter

- Ouvrez un nouveau terminal : cliquez sur **Terminal** dans la barre de menu, puis **New Terminal**
- Un panneau de terminal apparaît en bas de VS Code
- Dans le terminal, tapez :
  ```
  claude
  ```
- Si Claude Code vous demande de vous connecter, suivez les étapes de connexion du [tutoriel d'installation](./Install_Claude_Code_MacOS). Claude Code nécessite un abonnement Claude payant (comme Pro ou Max) ou un compte Anthropic Console — l'offre gratuite ne l'inclut pas.
- Vous verrez un message de bienvenue et l'invite Claude Code
- Vous pouvez maintenant utiliser Claude Code tout en modifiant des fichiers dans VS Code

**Remarque :** Vous n'avez besoin de vous connecter qu'une seule fois — les sessions suivantes affichent directement le message de bienvenue.

## Étape 5 : Tester le Flux de Travail

- Dans Claude Code, tapez :
```
Écris un court article expliquant pourquoi les LLM aiment utiliser le format Markdown. Enregistre-le sous article.md
```
- Claude Code crée le fichier - vous verrez `article.md` apparaître dans le panneau **Explorer** sur la gauche
- Cliquez sur `article.md` dans l'Explorateur pour le visualiser dans l'éditeur
- Pour prévisualiser l'article formaté : faites un clic droit sur l'onglet `article.md` et sélectionnez **Open Preview**
- Vous verrez le Markdown rendu avec les titres, puces et mise en forme appropriés

## Rouvrir Claude dans VS Code Plus Tard

Après avoir fermé VS Code, voici comment revenir à votre projet :

- **Option A :** Ouvrez VS Code, cliquez sur **File > Open Recent**, et sélectionnez `test_claude`
- **Option B :** Ouvrez Terminal, naviguez vers votre projet avec `cd ~/Documents/test_claude`, et tapez `code .`

VS Code mémorise vos dossiers récents, donc l'Option A avec Open Recent est généralement la plus rapide.

## Prochaines Étapes

- Demandez à Claude Code d'expliquer une base de code existante : « Explique ce que fait ce projet »
- Demandez à Claude Code de vous aider à écrire de nouvelles fonctionnalités : « Ajoute une fonction qui calcule la moyenne d'une liste »
- Utilisez Claude Code pour corriger des bugs : « Ce code donne une erreur, peux-tu le corriger ? »
- Essayez l'extension Claude Code pour un panneau de discussion visuel qui affiche les modifications directement dans le code. Lancer `claude` dans le terminal de VS Code l'installe généralement pour vous (sinon, recherchez "Claude Code" dans Extensions). Ouvrez n'importe quel fichier, puis cliquez sur l'icône Spark en haut à droite de l'éditeur

## Dépannage

- **Le terminal affiche "zsh" mais Claude Code ne démarre pas** - Assurez-vous que Claude Code est correctement installé ; exécutez `claude --version` pour vérifier
- **Commande "code" introuvable dans Terminal** - Dans VS Code, cliquez sur **View** dans la barre de menu, puis **Command Palette**, tapez "shell command", et sélectionnez **Shell Command: Install 'code' command in PATH**
- **VS Code ne s'ouvre pas car il provient d'un développeur non identifié** - Allez dans **Réglages Système > Confidentialité et sécurité** et cliquez sur **Ouvrir quand même**

## Aperçu du Flux de Travail

- **VS Code** fournit l'interface d'éditeur visuel
- **Terminal Intégré** exécute Claude Code à l'intérieur de VS Code
- Vos fichiers restent dans votre dossier Documents (ou où vous choisissez)
- Éditez des fichiers dans l'éditeur, discutez avec Claude Code dans le terminal - le meilleur des deux mondes

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 10 décembre 2025.
