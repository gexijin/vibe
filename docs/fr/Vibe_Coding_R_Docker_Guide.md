---
title: "Vibe Coding en R avec Claude Code et Docker"
lang: "fr"
---
[Accueil](../fr/)

# Vibe Coding en R avec Claude Code et Docker

Le vibe coding, c'est comme avoir une conversation avec votre ordinateur : vous décrivez le résultat souhaité, Claude Code le construit, vous testez et affinez. Ce n'est pas de la magie ; c'est une nouvelle façon de travailler où vous guidez la vision et l'IA s'occupe de l'implémentation. Ce tutoriel vous montre comment créer un véritable tableau de bord de statistiques NBA en utilisant uniquement des requêtes en langage naturel.

## Concepts Clés

- **[Claude Code](https://code.claude.com/)** - Assistant de codage IA qui écrit, débogue et refactorise du code en fonction de vos requêtes en langage naturel
- **[hoopR](https://hoopr.sportsdataverse.org/)** - Package R qui fournit un accès facile aux statistiques des joueurs NBA et aux données des matchs
- **Raffinement itératif** - Le modèle de base du vibe coding : décrire → tester → affiner → committer les versions fonctionnelles

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Codage R dans VS Code via un conteneur Docker](./R_Coding_Docker_Guide)
- Avoir terminé [Utiliser GitHub Desktop avec Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- Docker Desktop installé et démarré
- 25 à 30 minutes

## Étape 1 : Créer un Nouveau Dépôt GitHub

- Ouvrez GitHub Desktop
- Cliquez sur **File > New Repository**
- Remplissez les détails :
  - **Name :** `nba-dashboard`
  - **Description :** `NBA stats dashboard built with vibe coding`
  - **Local Path :** Choisissez un emplacement (par exemple, Documents ou dossier de travail)
  - Cochez **Initialize this repository with a README**
- Cliquez sur **Create Repository**
- Cliquez sur **Publish repository** en haut
- Décochez **Keep this code private** si vous voulez qu'il soit public (optionnel)
- Cliquez sur **Publish Repository**

Vous disposez maintenant d'un dépôt Git local et d'une sauvegarde sur GitHub.

## Étape 2 : Copier la Configuration Docker

- Allez sur https://github.com/gexijin/vibe
  - **Remarque pour les Mac Apple Silicon :** Cette configuration est conçue pour les processeurs Intel/AMD. Docker Desktop l'exécute par émulation : cela fonctionne, mais la première construction et R lui-même sont plus lents.
- Cliquez sur **Code**, puis sur **Download ZIP**
- Ouvrez l'**Explorateur de fichiers** (Windows) ou le **Finder** (Mac) et allez dans votre dossier **Téléchargements**
- Décompressez le fichier : sur Windows, faites un clic droit dessus et choisissez **Extraire tout** ; sur Mac, double-cliquez dessus
- Ouvrez le dossier décompressé `vibe-main`. Sur Windows, il peut contenir un autre dossier portant le même nom ; ouvrez celui-ci
- Trouvez le dossier `.devcontainer`
  - Sur Mac, le Finder masque les dossiers dont le nom commence par un point. Appuyez sur **Cmd+Shift+.** (point) pour les afficher
- Copiez l'intégralité du dossier (il contient `Dockerfile` et `devcontainer.json`)
- Naviguez vers votre nouveau dossier `nba-dashboard`
- Collez le dossier `.devcontainer` à cet endroit

Votre dossier `nba-dashboard` devrait maintenant contenir :
- `.devcontainer/` (dossier que vous venez de copier)
- `README.md` (créé par GitHub Desktop)
- `.git/` (dossier masqué pour le contrôle de version)

## Étape 3 : Ouvrir le Projet dans un Conteneur

- Démarrez l'application **Docker Desktop** depuis Windows ou Mac. Laissez-la s'exécuter en arrière-plan
- Ouvrez VS Code
- Cliquez sur **File > Open Folder**
- Naviguez vers le dossier `nba-dashboard`
- Cliquez sur **Select Folder** (Windows) ou **Open** (Mac)
- Une notification apparaît en bas à droite : **Folder contains a Dev Container configuration file**
- Cliquez sur **Reopen in Container**
- Si vous ne voyez pas la notification, cliquez sur l'icône **><** dans le coin inférieur gauche et sélectionnez **Reopen in Container**
- VS Code construit le conteneur Docker (prend 5 à 10 minutes la première fois)
- Observez la notification de progression montrant les étapes de construction
- Une fois terminé, l'icône **><** dans le coin inférieur gauche affiche **Dev Container: R in Docker (AMD64)**

## Étape 4 : Démarrer Claude Code

- Dans VS Code, cliquez sur **Terminal > New Terminal**
- Vous êtes maintenant à l'intérieur du conteneur Docker
- Tapez cette commande pour démarrer Claude Code :

```bash
claude
```

- Une fenêtre de navigateur s'ouvre pour l'authentification
- Cliquez sur **Continue with Google** ou **Continue with Email**
- Connectez-vous avec votre compte Claude. Claude Code nécessite un abonnement Claude payant (comme Pro ou Max) ou un compte Anthropic Console ; l'offre gratuite ne l'inclut pas
- Si le navigateur affiche un code au lieu d'indiquer que c'est terminé, copiez le code, revenez au terminal VS Code et collez-le à l'invite `Paste code here if prompted`, puis appuyez sur Entrée
- Si aucune fenêtre de navigateur ne s'ouvre, appuyez sur `c` pour copier le lien de connexion et collez-le dans votre navigateur
- Après la réussite de l'authentification, revenez au terminal VS Code
- Si on vous demande si vous faites confiance aux fichiers de ce dossier, choisissez **Yes**
- Vous verrez le message de bienvenue de Claude

Claude Code est maintenant en cours d'exécution et prêt pour vos requêtes.

## Étape 5 : Premier Vibe - Obtenir les Données NBA

Maintenant, le plaisir commence. Au lieu de consulter la documentation, décrivez simplement ce que vous voulez.

- Dans le terminal Claude Code, tapez :

```
Installe le package hoopR et charge les statistiques des joueurs NBA pour la saison la plus récente qui a des données. Montre-moi les 10 meilleurs joueurs par points totaux marqués. Affiche-le sous forme de tableau bien présenté.
```

- Appuyez sur Entrée
- Observez Claude :
  - Installer le package hoopR
  - Écrire du code R pour charger les données
  - Créer un script pour afficher les meilleurs marqueurs
  - Exécuter le code
- Examinez la sortie montrant les noms des joueurs, les équipes et les points

Vous venez d'utiliser le vibe coding ! Pas de recherche dans la documentation, pas d'essais et d'erreurs : simplement décrire et tester.

**Sauvegardez votre progression :** Demandez à Claude de faire un commit avec Git, ou faites-le vous-même depuis GitHub Desktop :
```
Fais un commit de ces modifications avec Git.
```

## Étape 6 : Deuxième Vibe - Explorer les Données

Avant de créer un tableau de bord, prenez le temps de comprendre de quelles données vous disposez.

- Dans le terminal Claude Code, tapez :

```
Montre-moi quelles colonnes sont disponibles dans ces données NBA. Ensuite crée un résumé montrant : le nombre de joueurs, le nombre d'équipes, la moyenne de points par joueur, et qui a le plus de passes décisives et de rebonds.
```

- Appuyez sur Entrée
- Claude explore l'ensemble de données et vous montre des statistiques intéressantes
- Regardez la sortie pour voir les colonnes disponibles, comme le nom du joueur, l'équipe, les points, les passes décisives et les rebonds

Cette exploration vous aide à décider quoi mettre dans votre tableau de bord.

**Sauvegardez votre progression :** Demandez à Claude de faire un commit, ou utilisez GitHub Desktop.

## Étape 7 : Troisième Vibe - Créer une Application Shiny de Base

Il est temps de construire le tableau de bord interactif.

- Dans le terminal Claude Code, tapez :

```
Crée une application Shiny dans un fichier appelé app.R qui affiche un tableau interactif des statistiques des joueurs NBA. Inclus des colonnes pour le nom du joueur, l'équipe, les points, les passes décisives et les rebonds. Ajoute un curseur pour filtrer les joueurs par points minimum marqués (de 0 à 1000). Rends-la propre et professionnelle.
```

- Appuyez sur Entrée
- Claude crée `app.R` avec une application Shiny complète
- Attendez que Claude ait fini d'écrire le fichier

## Étape 8 : Exécuter l'Application Shiny

Testez votre tableau de bord pour voir s'il fonctionne.

- Dans l'**Explorer** de VS Code (barre latérale gauche), cliquez sur `app.R` pour l'ouvrir
- Regardez en haut à droite de l'éditeur
- Trouvez le bouton **▶** avec une flèche déroulante
- Cliquez sur la liste déroulante et sélectionnez **Run Shiny App**
- L'application démarre et le tableau de bord s'ouvre dans un onglet d'aperçu à l'intérieur de VS Code (pour utiliser votre navigateur habituel, ouvrez l'onglet **Ports** en bas et cliquez sur l'icône en forme de globe à côté du port)
- Essayez de déplacer le curseur de points : le tableau se filtre en temps réel
- Faites défiler les données des joueurs
- Faites un commit si l'application fonctionne

Si quelque chose ne fonctionne pas, copiez les messages d'erreur et collez-les dans Claude pour qu'il corrige le problème.

## Étape 9 : Quatrième Vibe - Ajouter une Visualisation

Les tableaux sont utiles, mais les visualisations racontent de meilleures histoires.

- De retour dans le terminal Claude Code, tapez :

```
Ajoute un graphique à barres sous le tableau montrant les 15 meilleurs joueurs par points. Utilise différentes couleurs pour chaque joueur. Ajoute aussi un nuage de points montrant la relation entre les points et les passes décisives pour tous les joueurs filtrés.
```

- Appuyez sur Entrée
- Claude met à jour `app.R` avec le code de visualisation
- Cliquez à nouveau sur **Run Shiny App** pour recharger l'application
- Si l'aperçu ne change pas, cliquez sur la flèche de rechargement en haut de l'onglet d'aperçu (ou actualisez votre navigateur)
- Vous voyez maintenant un graphique à barres coloré et un nuage de points
- Déplacez le curseur : toutes les visualisations se mettent à jour ensemble

C'est le vibe coding en action : décrire la fonctionnalité, la tester, itérer.

## Étape 10 : Cinquième Vibe - Ajouter un Filtre par Équipe

Rendez le tableau de bord plus interactif avec la sélection d'équipe.

- Dans le terminal Claude Code, tapez :

```
Ajoute un menu déroulant pour filtrer les joueurs par équipe. Mets-le en haut. Quand je sélectionne une équipe, montre seulement les joueurs de cette équipe. Inclus une option « Toutes les équipes » pour afficher tout le monde.
```

- Appuyez sur Entrée
- Claude ajoute le filtre d'équipe
- Cliquez sur la flèche de rechargement en haut de l'onglet d'aperçu (ou actualisez votre navigateur)
- Testez le menu déroulant : sélectionnez différentes équipes comme Lakers, Warriors, Celtics
- Observez le tableau et les graphiques se mettre à jour pour chaque équipe

Vous construisez un tableau de bord professionnel en ayant une conversation.

## Étape 11 : Réviser et Committer

Avant de faire le commit, examinez ce que Claude a construit.

- Dans l'**Explorer** de VS Code, cliquez sur `app.R` pour l'ouvrir
- Parcourez le code : remarquez la disposition de l'interface utilisateur, la logique du serveur et le code des graphiques
- Vous n'avez pas besoin de comprendre chaque ligne, mais faites-vous une idée de la structure
- Ouvrez GitHub Desktop
- Vous verrez `app.R` listé (comme nouveau fichier, ou comme modifié si vous l'avez déjà commité lors d'une étape précédente)
- Le panneau de droite montre le code ajouté en vert
- Dans le champ **Summary** en bas à gauche, tapez :

```
Create NBA dashboard with team filter and visualizations
```

- Cliquez sur le bouton bleu de commit en bas (son libellé ressemble à **Commit 1 file to main**)
- Cliquez sur **Push origin** pour sauvegarder sur GitHub

Vous avez enregistré votre première version fonctionnelle !

## Étape 12 : Itérer et Améliorer

Le vibe coding brille lorsque vous itérez. Essayez d'ajouter des fonctionnalités en les décrivant :

**Exemples de requêtes à Claude :**

- « Ajoute une zone de recherche de joueur pour que je puisse taper le nom d'un joueur et arriver directement sur sa ligne »
- « Affiche les logos des équipes à côté des noms d'équipes dans le menu déroulant »
- « Ajoute un graphique linéaire montrant la tendance des points par match pour l'équipe sélectionnée »
- « Rends le tableau triable en cliquant sur les en-têtes de colonnes »
- « Ajoute des infobulles au nuage de points montrant les noms des joueurs quand je survole »

Après chaque fonctionnalité réussie :
- Testez-la dans le navigateur
- Si elle fonctionne, faites un commit avec GitHub Desktop
- Si elle ne fonctionne pas, décrivez l'erreur à Claude et demandez-lui de la corriger
- Une fois l'erreur corrigée, committez la version fonctionnelle


**Principes clés :**

- **Décrivez les résultats, pas l'implémentation** - Dites « montre les meilleurs marqueurs » et non « utilise arrange() et head() »
- **Itérez rapidement** - Tester → affiner → tester → affiner
- **Committez les versions fonctionnelles** - Enregistrez chaque succès avant d'essayer de nouvelles fonctionnalités
- **Acceptez les échecs** - Si le code de Claude ne fonctionne pas, décrivez simplement l'erreur et demandez-lui de la corriger
- **Gardez le contrôle** - Vous décidez des fonctionnalités, des priorités et du moment où c'est suffisant

À chaque fois, suivez le modèle : décrire → tester → itérer → committer.

## Prochaines Étapes

- **Appliquez à votre domaine** - Utilisez le vibe coding pour vos propres données (recherche, affaires, loisirs)
- **Essayez d'autres packages** - Demandez à Claude d'utiliser `nflfastR` pour le football américain ou `worldfootballR` pour le football
- **Apprenez en demandant** - Quand Claude écrit du code, demandez « explique ce que fait cette fonction » pour apprendre R
- **Partagez votre tableau de bord** - Déployez sur [shinyapps.io](https://www.shinyapps.io/) (demandez à Claude comment faire)
- **Lisez sur le vibe coding** - Visitez [le guide d'IBM](https://www.ibm.com/think/topics/vibe-coding) pour en savoir plus sur ce style de codage

## Dépannage

- **L'installation de hoopR échoue** - Vérifiez votre connexion Internet ; le package télécharge des données depuis le web. Essayez d'exécuter `install.packages("hoopR")` dans un terminal R pour voir les messages d'erreur détaillés.
- **L'application Shiny ne démarre pas** - Vérifiez que l'extension Shiny est installée (recherchez "Posit.shiny" dans le panneau Extensions de VS Code). Recherchez les messages d'erreur dans le terminal et collez-les dans Claude.
- **Aucune donnée ne s'affiche** - Le package hoopR récupère des données en direct ; si la saison NBA n'a pas commencé, il peut y avoir des données limitées. Demandez à Claude d'utiliser des données d'exemple ou une saison précédente.
- **Claude fait des erreurs** - Normal ! Copiez le message d'erreur, collez-le à Claude et dites « corrige cette erreur ». Le vibe coding inclut l'itération et le débogage.
- **Impossible de pousser vers GitHub** - Assurez-vous que vous êtes connecté à GitHub Desktop et que vous avez publié le dépôt (Étape 1). Vérifiez votre connexion Internet.

## Vue d'Ensemble du Flux de Travail

Ce tutoriel a combiné plusieurs technologies en un seul flux de travail :

- **GitHub Desktop** - Contrôle de version avec interface visuelle (créer des dépôts, committer, pousser)
- **Conteneur Docker** - Environnement R isolé avec toutes les dépendances pré-installées
- **VS Code** - Éditeur de code qui se connecte au conteneur Docker
- **Claude Code** - Assistant IA qui écrit du code R et Shiny à partir de vos descriptions
- **Package hoopR** - Source de données NBA avec API simple
- **Framework Shiny** - Applications web interactives en R

La magie n'est pas un outil unique : c'est la façon dont le vibe coding vous permet de décrire ce que vous voulez et d'itérer rapidement. Vous êtes passé d'un projet vide à un tableau de bord sportif fonctionnel en moins de 30 minutes sans écrire manuellement une seule ligne de code.

## Flux de Travail Quotidien

Après cette configuration initiale, votre routine quotidienne de vibe coding devient :

1. **Démarrez Docker Desktop** - Lancez l'application, attendez que l'indicateur passe au vert
2. **Ouvrez VS Code** - Ouvrez votre projet, rouvrez dans le conteneur si nécessaire
3. **Démarrez Claude Code** - Tapez `claude` dans le terminal
4. **Décrivez votre objectif** - « Ajoute une fonctionnalité qui... » ou « Corrige le bug où... »
5. **Testez les modifications** - Exécutez votre application, vérifiez si elle fonctionne
6. **Itérez ou committez** - Si elle ne fonctionne pas, décrivez la correction ; si elle fonctionne, faites un commit avec GitHub Desktop
7. **Poussez régulièrement** - Cliquez sur **Push origin** pour sauvegarder sur GitHub

Plus vous pratiquez, mieux vous savez décrire ce que vous voulez. Le vibe coding est une compétence : vous apprenez quels types de descriptions fonctionnent le mieux et comment diviser de grandes idées en morceaux testables.

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 7 décembre 2025.
