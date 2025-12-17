[Accueil](./)

# Premiers Pas avec le Contrôle de Version

Vous travaillez sur un projet et effectuez des modifications qui brisent tout. Vous ne vous souvenez plus de ce que vous avez changé, et vous souhaitez revenir au moment où tout fonctionnait. Le contrôle de version est comme des points de sauvegarde dans un jeu vidéo—chaque fois que vous « committez » votre travail, vous créez un point de restauration auquel vous pouvez toujours revenir. [GitHub](https://github.com) stocke vos points de sauvegarde dans le cloud, de sorte que votre code soit sauvegardé en toute sécurité et accessible depuis n'importe quel ordinateur.

## Concepts Clés

- **Git** - Logiciel de contrôle de version qui suit les modifications apportées à vos fichiers sur votre ordinateur
- **GitHub** - Site web qui stocke votre code dans le cloud, comme Google Drive pour le code
- **GitHub Desktop** - Application qui facilite l'utilisation de Git avec des boutons au lieu de commandes
- **Repository (repo)** - Un dossier de projet qui suit toutes vos modifications

## Ce Dont Vous Aurez Besoin

- Ordinateur Windows, macOS ou Linux
- Connexion Internet
- Adresse e-mail pour créer un compte GitHub
- 15 à 20 minutes

## Étape 1 : Créer un Compte GitHub

- Ouvrez votre navigateur web
- Allez sur [github.com](https://github.com)
- Cliquez sur **Sign up**
- Saisissez votre adresse e-mail, créez un mot de passe et choisissez un nom d'utilisateur
- Complétez les étapes de vérification

## Étape 2 : Télécharger GitHub Desktop

- Allez sur [desktop.github.com](https://desktop.github.com)
- Cliquez sur le bouton **Download**
- Ouvrez le fichier téléchargé pour l'installer

**Sur Windows :**
- Double-cliquez sur le fichier d'installation
- GitHub Desktop s'installe et s'ouvre automatiquement

**Sur Mac :**
- Ouvrez le fichier `.zip` téléchargé
- Faites glisser **GitHub Desktop** dans votre dossier Applications
- Ouvrez GitHub Desktop depuis Applications

## Étape 3 : Se Connecter à GitHub Desktop

- Ouvrez GitHub Desktop
- Cliquez sur **Sign in to GitHub.com**
- Votre navigateur s'ouvre—cliquez sur **Authorize desktop**
- Revenez à GitHub Desktop
- Cliquez sur **Finish** pour terminer la configuration

## Étape 4 : Créer Votre Premier Repository

- Dans GitHub Desktop, cliquez sur **Create a New Repository on your Hard Drive**
- Remplissez le formulaire :
  - **Name :** `my-first-project` (ou tout nom qui vous plaît)
  - **Description :** `Learning version control` (optionnel)
  - **Local Path :** Choisissez l'endroit où l'enregistrer (le dossier Documents convient parfaitement)
  - Cochez **Initialize this repository with a README**
- Cliquez sur **Create Repository**

## Étape 5 : Ouvrir le Dossier de Votre Projet

- Dans GitHub Desktop, cliquez sur **Repository** dans la barre de menu
- Sélectionnez **Show in Finder** (Mac) ou **Show in Explorer** (Windows)
- Vous verrez un dossier portant le nom de votre projet
- À l'intérieur se trouve un fichier appelé `README.md`

## Étape 6 : Effectuer Votre Première Modification

- Ouvrez `README.md` dans n'importe quel éditeur de texte (Notepad, TextEdit ou VS Code)
- Remplacez le contenu par :
  ```
  # My First Project

  I'm learning version control with GitHub Desktop.

  ## What I'm Building

  This is a practice project to learn how to:
  - Track changes to my code
  - Create save points (commits)
  - Back up my work to GitHub
  ```
- Cliquez sur **File** → **Save**

## Étape 7 : Créer Votre Premier Commit (Point de Sauvegarde)

- Revenez à GitHub Desktop
- Vous verrez vos modifications surlignées sur le côté droit (vert = ajouté, rouge = supprimé)
- En bas à gauche, saisissez un message de commit : `Updated README with project description`
- Cliquez sur le bouton bleu **Commit to main**

## Étape 8 : Push vers GitHub (Sauvegarder dans le Cloud)

- Cliquez sur le bouton bleu **Publish repository** en haut
- Conservez le nom tel quel
- Décochez « Keep this code private » si vous voulez que d'autres le voient (optionnel)
- Cliquez sur **Publish Repository**

Votre code est maintenant sauvegardé en ligne à l'adresse : `https://github.com/YOUR-USERNAME/my-first-project`

## Prochaines Étapes

- Modifiez à nouveau votre fichier README et committez les modifications
- Créez un nouveau fichier dans le dossier de votre projet et committez-le
- Explorez l'onglet **History** pour voir comment votre projet évolue au fil du temps

## Dépannage

- **Impossible de se connecter à GitHub** - Vérifiez votre connexion Internet. Essayez d'abord de vous connecter sur github.com pour vérifier que vos identifiants fonctionnent.
- **Les modifications n'apparaissent pas dans GitHub Desktop** - Assurez-vous d'avoir enregistré vos fichiers. Cliquez sur **Repository** → **Refresh** ou redémarrez GitHub Desktop.
- **Le push échoue avec une erreur « rejected »** - Quelqu'un d'autre a poussé des modifications. Cliquez d'abord sur **Fetch origin**, puis réessayez de pousser.

## Aperçu du Flux de Travail

- Effectuez des modifications dans les fichiers de votre projet
- Examinez les modifications dans GitHub Desktop (vert = ajouté, rouge = supprimé)
- Rédigez un message de commit descriptif et cliquez sur **Commit to main**
- Cliquez sur **Push origin** pour sauvegarder sur GitHub
- Répétez

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
