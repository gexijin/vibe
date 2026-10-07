---
title: "Claude Code avec contrôle de version pour Windows"
lang: "fr"
---
[Accueil](./)

# Claude Code avec contrôle de version pour Windows

Vous travaillez avec l'assistance de l'IA. Elle apporte des modifications à vos fichiers. Parfois les modifications sont brillantes. Parfois elles ne le sont pas. **Le contrôle de version est comme un bouton d'annulation pour l'ensemble de votre projet.** Chaque fois que vous enregistrez un instantané (appelé un "commit"), vous créez un point de restauration auquel vous pouvez toujours revenir. Mieux encore, vous pouvez faire tout cela entièrement sur votre ordinateur et Claude Code le fait pour vous.

## Concepts Clés

- **PowerShell** - L'outil en ligne de commande intégré à Windows, utilisé ici pour exécuter Git et Claude Code
- **Git** - Suit chaque modification de vos fichiers sur votre ordinateur, créant des points de restauration auxquels vous pouvez revenir à tout moment
- **Commit** - Un instantané de votre projet à un moment spécifique avec une description de ce qui a changé
- **Claude Code** - Assistant de codage IA qui écrit du code, corrige des bugs et gère les opérations Git grâce à de simples demandes

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Installer Claude Code sur Windows](./Install_CLAUDE_Code_Win)
- 20 minutes

## Étape 1 : Ouvrez PowerShell

- Cliquez sur le menu **Démarrer**
- Tapez `PowerShell`
- Cliquez sur **Windows PowerShell** pour l'ouvrir

**Remarque :** Si vous avez suivi le parcours optionnel WSL/Ubuntu au lieu de l'installation native, ouvrez plutôt l'application **Ubuntu** — Git et Claude Code y fonctionnent de la même façon, simplement avec des chemins de style Linux (`/mnt/c/Users/...`) au lieu de `~\Documents\...`.

## Étape 2 : Installez Git

- Vérifiez si Git est déjà installé :
  ```
  git --version
  ```
- Si vous voyez un numéro de version comme `git version 2.45.0`, passez à l'Étape 3
- Si vous voyez une erreur, installez Git for Windows :
  - Allez sur [git-scm.com/download/win](https://git-scm.com/download/win)
  - Le téléchargement devrait démarrer automatiquement — ouvrez le programme d'installation une fois terminé
  - Cliquez sur **Next** tout au long de l'installation, en acceptant les options par défaut
  - Cliquez sur **Install**, puis sur **Finish**
  - Fermez et rouvrez PowerShell, puis vérifiez à nouveau avec `git --version`

## Étape 3 : Configurez Git avec Votre Identité

Git a besoin de savoir qui vous êtes pour les messages de commit.

- Définissez votre nom et votre email (peuvent être fictifs)
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

L'utilisation de votre nom et de votre email vous aide à identifier qui a effectué les modifications lorsque plusieurs personnes travaillent sur ceci.

## Étape 4 : Naviguez vers Votre Dossier Documents

- Naviguez vers votre dossier Documents :
  ```
  cd ~\Documents
  ```
- Vérifiez que vous êtes au bon endroit :
  ```
  pwd
  ```

Vous devriez voir un chemin se terminant par `\Documents`.

## Étape 5 : Créez un Dossier de Projet

- Créez un dossier appelé `test_claude` :
  ```
  mkdir test_claude
  ```
- Naviguez dedans :
  ```
  cd test_claude
  ```

C'est ici que votre projet vivra.

## Étape 6 : Démarrez Claude Code

- Démarrez Claude Code :
  ```
  claude
  ```

Connectez-vous avec votre abonnement Claude en suivant le [tutoriel d'installation](Install_CLAUDE_Code_Win.md). Après vous être connecté, vous verrez un message de bienvenue et l'invite Claude Code.

## Étape 7 : Demandez à Claude d'Initialiser Git

- Tapez cette demande :
  ```
  Commence à suivre les modifications
  ```

Claude initialise un dépôt Git dans votre dossier (prend 2-5 secondes). Vous avez maintenant le contrôle de version !

## Étape 8 : Construisez l'Application Minuteur

- Dans Claude Code, tapez :
  ```
  Crée une application de minuteur simple dans un seul fichier appelé timer.html.
  Elle doit avoir :
  - Un champ de saisie pour définir les minutes
  - Des boutons Démarrer et Arrêter
  - Un affichage montrant le temps restant au format MM:SS
  ```

Claude crée `timer.html` (prend 10-30 secondes) avec le code CSS et JavaScript.

## Étape 9 : Testez le Minuteur

- Ouvrez l'Explorateur de Fichiers Windows
- Naviguez vers `Documents\test_claude`
- Double-cliquez sur `timer.html` pour l'ouvrir dans votre navigateur
- Essayez le minuteur :
  - Tapez `1` dans le champ de saisie
  - Cliquez sur **Start**
  - Regardez le compte à rebours

**Si quelque chose ne fonctionne pas :** Dans Claude Code, décrivez l'erreur : « Je vois cette erreur : [décrivez ce qui s'est passé]. Peux-tu la corriger ? »

## Étape 10 : Demandez à Claude de Commit

- Dans Claude Code, tapez :
  ```
  Enregistre ces modifications.
  ```

Claude va :
- Vérifier quels fichiers ont changé
- Écrire un message de commit descriptif
- Créer le commit (prend 5-10 secondes)

Vous avez créé votre premier point de sauvegarde ! Vous pouvez toujours revenir à cette version fonctionnelle.

## Étape 11 : Ajoutez des Boutons Prédéfinis

- Dans Claude Code, tapez :
  ```
  Ajoute deux boutons en haut. Si je clique dessus, cela démarre automatiquement des minuteurs de 1 et 5 minutes.
  ```
- Actualisez votre onglet de navigateur
- Testez : Cliquez sur le bouton **5 min**
- Si cela fonctionne, commitez les modifications :
  ```
  Enregistre ces modifications.
  ```

Nous avons créé un 2ème point de sauvegarde. Cette version a les deux boutons fonctionnels.


## Étape 12 : Ajoutez un Autre Bouton

- Dans Claude Code, tapez :
  ```
  Ajoute un bouton de 15 minutes.
  ```
- Actualisez votre onglet de navigateur
- Testez : Cliquez sur le bouton **15 min**

**Pour ce tutoriel :** Faites semblant que le bouton 15 minutes ne fonctionne pas correctement. Ne commitez pas encore—nous allons pratiquer l'abandon des mauvaises modifications.

## Étape 13 : Abandonnez les Modifications

Parfois le code de l'IA ne fonctionne pas et vous devez recommencer depuis votre dernier point de sauvegarde.

- Dans Claude Code, tapez :
  ```
  Abandonne ces modifications.
  ```
- Claude affiche un menu avec des options comme **Yes** et **No** — utilisez les touches fléchées (ou appuyez sur le numéro à côté de **Yes**) pour le sélectionner, puis appuyez sur **Entrée**
- Actualisez votre navigateur—le bouton 15 minutes disparaît

Claude supprime les nouvelles modifications que nous n'aimons pas. Le minuteur fonctionne à nouveau avec seulement les boutons 1 et 5 minutes !

## Étape 14 : Ajoutez une Notification Sonore

- Dans Claude Code, tapez :
  ```
  Ajoute une notification sonore quand le minuteur atteint zéro.
  ```
- Actualisez le navigateur et testez une fois que Claude a terminé (réglez le minuteur sur 1 minute)
- Si cela fonctionne, commitez les modifications :
  ```
  Enregistre ces modifications.
  ```

## Étape 15 : Ajoutez un Bouton de Rappel

- Dans Claude Code, tapez :
  ```
  Le son doit continuer jusqu'à ce que je clique sur un bouton pour le mettre en pause.
  ```
- Actualisez le navigateur et testez une fois que Claude a terminé (réglez le minuteur sur 1 minute)
- Si cela fonctionne, commitez les modifications :
  ```
  Enregistre ces modifications.
  ```

## Étape 16 : Affichez Votre Historique de Commit

- Dans Claude Code, tapez :
  ```
  Montre-moi mon historique de modifications
  ```

Claude affiche vos commits dans un format lisible. Vous verrez :
- Votre commit initial de l'application minuteur
- Le commit des boutons prédéfinis (1 min et 5 min)
- Le commit de la notification sonore
- Le bouton de rappel.

Remarquez que la tentative du bouton 15 minutes n'est pas là—vous l'avez abandonnée !

## Étape 17 : Examinez le Code

- Dans le navigateur qui affiche l'application, faites un clic droit et sélectionnez **Afficher le code source de la page**
- Vous pouvez voir le code source pour cela.
- Dans Claude Code, demandez
  ```
  Explique ce code. Juste les grandes lignes.
  ```

## Le Flux de Travail Complet

- Demandez à Claude d'apporter des modifications
- Testez
- Si cela fonctionne → Demandez à Claude de commiter
- Si cela échoue → Demandez à Claude de le corriger.
- Impossible de corriger → Abandonnez les modifications et réessayez
- Répétez

Vous pouvez toujours revenir à n'importe quel commit. Abandonnez sans crainte—ne commitez que du code fonctionnel !

## Prochaines Étapes

Essayez d'ajouter d'autres fonctionnalités à votre minuteur :

- **Bouton 15 minutes :** « Ajoute un bouton prédéfini de 15 minutes qui fonctionne » (refaites ce que nous avons abandonné !)
- **Bouton pause :** « Ajoute un bouton Pause/Reprendre qui bascule l'état du minuteur »
- **Meilleur style :** « Améliore le design visuel avec une palette de couleurs moderne et des polices plus grandes »
- **Barre de progression :** « Ajoute une barre de progression visuelle montrant le temps restant »

Rappelez-vous : Testez après chaque fonctionnalité, commitez après chaque succès, abandonnez les échecs.

## Dépannage

- **Erreur "not a git repository" :** Assurez-vous d'être dans le dossier test_claude (`cd ~\Documents\test_claude`)
- **Impossible de trouver timer.html dans Windows :** Le fichier est à `C:\Users\YOUR_USERNAME\Documents\test_claude\timer.html`
- **Commande `git` introuvable :** Fermez et rouvrez PowerShell après avoir installé Git for Windows pour que le PATH soit mis à jour, puis exécutez à nouveau `git --version`
- **Le minuteur ne fonctionne pas :** Ouvrez la console du navigateur (clic droit sur la page, sélectionnez **Inspecter**, cliquez sur l'onglet **Console**), copiez tous les messages d'erreur en rouge, collez-les à Claude

## Ce Que Vous Pouvez Demander à Claude

- « Quels fichiers ai-je modifiés ? » - Voir les modifications non commitées
- « Montre-moi les différences » - Voir exactement quel code a changé
- « Explique ce que fait le code du minuteur » - Comprendre l'implémentation
- « Crée une branche appelée expérience » - Essayer des modifications risquées en toute sécurité
- « Reviens au commit précédent » - Annuler tout depuis le dernier commit

Claude gère toutes les opérations Git en langage naturel—aucune commande à mémoriser !

## Aperçu du Flux de Travail

- **Configuration :** Installez Git une fois, configurez l'identité une fois
- **Développement :** Claude écrit le code, vous testez dans le navigateur
- **Contrôle de Version :** Claude gère toutes les opérations Git via de simples demandes
- **Sécurité :** Abandonnez les mauvaises modifications à tout moment, revenez à n'importe quel commit précédent
- **Local :** Tout reste sur votre ordinateur, aucun compte ni connexion Internet requis

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 8 décembre 2025.
