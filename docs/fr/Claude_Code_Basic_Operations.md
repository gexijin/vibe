[Accueil](./)

# Claude Code : Opérations de Base

Apprendre à coder avec l'assistance de l'IA peut sembler intimidant au début. Pensez à Claude Code comme un collègue compétent assis à côté de vous — vous décrivez ce que vous voulez en français simple, et il vous aide à y parvenir. Ce tutoriel vous enseigne les opérations essentielles que vous utiliserez quotidiennement, du démarrage de conversations à la gestion de votre espace de travail.

## Concepts Clés

- **Workspace** - Si vous démarrez Claude Code depuis un dossier, celui-ci devient l'espace de travail de la session.
- **REPL (Read-Eval-Print Loop)** - Une session interactive où vous tapez des commandes, Claude répond, et la conversation continue jusqu'à ce que vous quittiez
- **Context** - La quantité de code et d'historique de conversation que Claude se souvient ; comme une mémoire de travail qui se remplit au fil du temps
- **Slash Commands** - Raccourcis intégrés commençant par `/` qui effectuent des actions spécifiques comme effacer l'historique ou afficher l'aide

## Ce Dont Vous Aurez Besoin

- Claude Code installé depuis le tutoriel [Windows](Install_CLAUDE_Code_Win.md) ou [Mac](Install_Claude_Code_MacOS.md)
- WSL installé si vous utilisez Windows
- Familiarité de base avec l'utilisation d'un terminal ou d'une invite de commande
- 15-20 minutes

## Étape 1 : Ouvrez Votre Terminal

- **Windows** : Appuyez sur la touche Windows, tapez `Ubuntu`, et appuyez sur Entrée pour ouvrir le terminal WSL
- **Mac** : Appuyez sur `Cmd+Espace`, tapez `Terminal`, et appuyez sur Entrée

Une fenêtre de texte s'ouvrira où vous pourrez taper des commandes.

## Étape 2 : Obtenez les Fichiers du Projet de Démonstration

Nous utiliserons un véritable projet de science des données pour explorer les fonctionnalités de Claude Code. Vous pouvez soit le cloner avec Git, soit le télécharger directement.

**Option A : Cloner avec Git (si vous avez Git installé) :**

```
git clone https://github.com/gexijin/data_projects
cd data_projects
```

**Option B : Télécharger sans Git :**

- Visitez [https://github.com/gexijin/data_projects](https://github.com/gexijin/data_projects) dans votre navigateur web
- Cliquez sur le bouton vert **Code** près du coin supérieur droit
- Cliquez sur **Download ZIP**
- Extrayez le fichier ZIP dans un dossier appelé **data_projects** dans le dossier Téléchargements.
- Dans votre terminal, naviguez vers le dossier extrait :
  - **Windows** : `cd /mnt/c/Users/VotreNom/Downloads/data_projects`
  - **Mac/Linux** : `cd ~/Downloads/data_projects`

Remplacez `VotreNom` par votre nom d'utilisateur réel et ajustez le chemin si vous l'avez extrait ailleurs. Pour les utilisateurs Windows, vos fichiers Windows sont accessibles depuis /mnt/c dans le système Linux.

## Étape 3 : Démarrez Claude Code depuis le Dossier

Dans votre terminal (assurez-vous d'être dans le dossier data_projects), tapez :

```bash
claude
```

Connectez-vous avec votre abonnement Claude en suivant le [tutoriel d'installation](Install_CLAUDE_Code_Win.md). Après vous être connecté, vous verrez un message de bienvenue et l'invite Claude Code.

Après vous être connecté avec succès, vous verrez un message de bienvenue et l'invite Claude Code.


## Étape 4 : Posez des Questions sur Votre Projet

Claude Code lit automatiquement vos fichiers lorsque nécessaire. Essayez ces questions pour comprendre votre projet :

**Demandez la structure du dossier :**

```
Quelle est la structure du dossier de ce projet ?
```

**Demandez les technologies :**

```
Quelles technologies et bibliothèques ce projet utilise-t-il ?
```

**Demandez les changements récents :**

```
Quel a été le dernier changement apporté à ce projet ?
```

Claude vérifiera l'historique Git (si disponible) et vous informera des commits récents.

Vous pouvez demander à Claude n'importe quoi sur votre code en langage naturel. Il lit les fichiers selon les besoins pour répondre à vos questions.

## Étape 5 : Slash Commands Essentielles

Tapez `/` et appuyez sur Entrée pour voir toutes les commandes disponibles. Voici les plus importantes :

**Voir toutes les commandes :**

```
/
```

Cela affiche un menu de toutes les slash commands. Utilisez les touches fléchées pour parcourir, appuyez sur Entrée pour sélectionner, ou appuyez sur Échap pour annuler.

**Obtenir de l'aide :**

```
/help
```
Affiche la documentation sur l'utilisation de Claude Code.



**Vérifier l'utilisation du contexte :**
Il est important de gérer le contexte, la « mémoire de travail » de Claude.

```
/context
```

**Effacer l'historique de conversation :**

Lorsque le contexte se remplit, démarrez une nouvelle conversation avec `/clear`.
```
/clear
```
Efface la conversation actuelle et recommence à zéro. Utilisez ceci lorsque vous voulez changer de sujet ou lorsque votre conversation devient trop longue. Il est essentiel de gérer le contexte.


**Quitter Claude Code :**

```
/exit
```

Termine votre session et retourne à votre invite de terminal normale. Vous pouvez également appuyer sur **Ctrl + C** deux fois.

## Étape 6 : Raccourcis Clavier

Ces raccourcis rendent le travail avec Claude Code plus rapide :

- **Shift+Tab** - Basculer entre le mode plan, édition ou normal - Planifiez d'abord pour les tâches complexes
- **Alt+Entrée** (Windows/Linux) ou **Option+Return** (Mac) - Ajouter une nouvelle ligne dans votre message sans l'envoyer
- **Ctrl+C** - Annuler l'opération actuelle ou la réponse de Claude
- **Ctrl+D** - Approuver les modifications de fichiers lorsque Claude demande la permission
- **Échap** - Fermer les menus ou annuler la saisie actuelle

## Étape 7 : Toujours Créer un Fichier CLAUDE.md

Le fichier CLAUDE.md est le manuel d'instructions de votre projet pour Claude. Il persiste entre les sessions, donc Claude se souvient du contexte important de votre projet.

**Créez le fichier :**

```
/init
```

Claude créera le fichier avec un résumé de votre projet. Ce fichier reste à la racine de votre projet et Claude le lit automatiquement chaque fois que vous démarrez une nouvelle session.

Vous pouvez modifier CLAUDE.md dans le dossier du projet à tout moment pour ajouter des instructions spécifiques au projet, des conventions de codage ou un contexte important tel que le but des fichiers, etc.

## Étape 8 : Référencer des Fichiers ou des Lignes de Code

Vous pouvez utiliser `@` pour référencer un fichier spécifique :

```
Expliquez le code dans @Visualization/Matplotlib/Nested_Pie_Chart.ipynb
```

Claude lira le notebook et expliquera ce qu'il fait, comment il fonctionne et ce que le code accomplit. Cela amène effectivement le fichier dans le contexte.

Si vous travaillez avec Claude Code depuis VS Code et avez l'extension Claude Code installée, vous pouvez ajouter le fichier au contexte simplement en l'ouvrant. Vous verrez dans le coin inférieur droit de la fenêtre de commande qui affiche `In Nested_Pie_Chart.ipynb`. Alors Claude sait que vous parlez de ce fichier.

De plus, vous pouvez sélectionner quelques lignes de code et Claude affichera **3 lines selected**. Vous pouvez demander à Claude d'apporter des modifications rapides à ces lignes ou poser des questions. Par conséquent, je recommande vivement d'utiliser Claude Code depuis VS Code.


## Étape 9 : Effectuez des Actions avec les Commandes Linux

Claude peut effectuer des actions en exécutant des commandes Linux sous de nombreuses formes.

- Installer des logiciels
  ```
  Installez la bibliothèque pandas
  ```

- Démarrer le contrôle de version
  ```
  Commencez à suivre les changements en utilisant Git. Mon nom est James Bond et mon email est bond@earth.com
  ```
- Valider les changements
  ```
  Validez ces changements.
  ```
- Trouver et télécharger des données
  ```
  Téléchargez le jeu de données wine quality depuis UCI. Mettez-le dans un nouveau dossier appelé wine.
  ```

- Exécuter du code
  ```
  Réécrivez le code du graphique en camembert imbriqué comme un script Python ordinaire.
  Exécutez-le et enregistrez le nouveau code et les graphiques dans le même dossier.
  ```

Nous pouvons poser cette question vague parce que nous venons de lui demander d'expliquer le code. Beaucoup de choses se produisent après cela. Claude installe des logiciels, résout des erreurs, résout des problèmes d'environnements - tout seul.



Vous avez essentiellement un expert en commandes bash Linux à votre disposition. Tant que vous gérez les permissions et approuvez les actions, vous pouvez être très productif.

## Prochaines Étapes

Maintenant que vous connaissez les bases, essayez ceci par vous-même :

- Demandez à Claude d'expliquer un algorithme d'apprentissage automatique dans l'un des dossiers du projet
- Demandez des modifications à un notebook existant (comme changer les couleurs des graphiques ou ajouter de nouvelles fonctionnalités)
- Créez un nouveau script Python qui utilise des données du projet
- Demandez à Claude de comparer deux approches différentes dans le code

## Dépannage

- **Erreur "Command not found"** - Claude Code n'est pas installé ou n'est pas dans votre PATH. Exécutez `npm install -g @anthropic-ai/claude-code` pour l'installer.
- **Claude donne des informations obsolètes** - Effacez le contexte avec `/clear` et redemandez. Les longues conversations peuvent remplir la mémoire de Claude.
- **Les modifications de fichiers ne fonctionnent pas** - Assurez-vous d'avoir les permissions d'écriture dans votre dossier de projet. Claude demandera l'approbation avant de modifier les fichiers — appuyez sur Ctrl+D pour approuver.
- **Le contexte se remplit rapidement** - Utilisez `/context` pour vérifier l'utilisation. Lorsqu'il est presque plein, utilisez `/clear` pour démarrer une conversation fraîche avec une ardoise propre.

## Aperçu du Flux de Travail

Travailler avec Claude Code suit ce schéma :

- Démarrez Claude dans votre dossier de projet avec `claude`
- Posez des questions en langage naturel
- Claude lit les fichiers selon les besoins et répond
- Demandez des modifications de code — Claude demande la permission avant de modifier les fichiers
- Utilisez `/clear` lorsque vous changez de sujet ou que le contexte est plein
- Utilisez `/exit` lorsque vous avez terminé

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 14 décembre 2025.
