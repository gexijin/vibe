[Accueil](./)

# Vibe Coding en Python avec Claude Code et Docker

Vous avez écrit du code Python en tapant chaque ligne vous-même. Mais que se passerait-il si vous pouviez décrire ce que vous voulez en français et regarder le code apparaître ? Le vibe coding ressemble à une conversation avec votre ordinateur : vous décrivez le résultat souhaité, Claude Code le construit, vous testez et affinez. Ce n'est pas de la magie ; c'est une nouvelle façon de travailler où vous guidez la vision et l'IA gère l'implémentation. Ce tutoriel vous montre comment analyser le jeu de données classique des fleurs d'iris en utilisant uniquement des requêtes en langage naturel.

## Concepts Clés

- **[Vibe Coding](https://www.ibm.com/think/topics/vibe-coding)** - Programmer en décrivant ce que vous voulez en langage naturel, puis itérer en fonction des résultats plutôt que d'écrire le code ligne par ligne
- **[Claude Code](https://code.claude.com/)** - Assistant de codage IA qui écrit, débogue et refactorise le code en fonction de vos demandes en langage naturel
- **[Jeu de données Iris](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)** - Jeu de données classique contenant les mesures de 150 fleurs d'iris de trois espèces
- **Raffinement itératif** - Le modèle central du vibe coding : décrire → tester → affiner → valider les versions fonctionnelles

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Python Coding in VS Code via Docker](./Python_Coding_Docker_Guide)
- Avoir terminé [Using GitHub Desktop with Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 20-25 minutes

## Étape 1 : Créer un Nouveau Dépôt GitHub

- Ouvrez GitHub Desktop
- Cliquez sur **File > New Repository**
- Remplissez les détails :
  - **Name :** `iris-analysis`
  - **Description :** `Iris data analysis built with vibe coding`
  - **Local Path :** Choisissez un emplacement (par exemple, Documents ou dossier de travail)
  - Cochez **Initialize this repository with a README**
- Cliquez sur **Create Repository**
- Cliquez sur **Publish repository** en haut
- Décochez **Keep this code private** si vous voulez qu'il soit public (optionnel)
- Cliquez sur **Publish Repository**

Vous disposez maintenant d'un dépôt Git local et d'une sauvegarde sur GitHub.

## Étape 2 : Copier la Configuration Docker

Vous avez besoin du dossier `.devcontainer` du projet vibe pour configurer votre environnement Docker.

- Ouvrez l'Explorateur de fichiers (Windows) ou Finder (Mac)
- Naviguez vers votre dossier de projet vibe (par exemple, `Documents/vibe`)
- Trouvez le dossier `.devcontainer`
- Copiez l'intégralité du dossier (il contient `Dockerfile` et `devcontainer.json`)
- Naviguez vers votre nouveau dossier `iris-analysis`
- Collez le dossier `.devcontainer` à cet endroit

Votre dossier `iris-analysis` devrait maintenant contenir :
- `.devcontainer/` (dossier que vous venez de copier)
- `README.md` (créé par GitHub Desktop)
- `.git/` (dossier caché pour le contrôle de version)

## Étape 3 : Ouvrir le Projet dans le Conteneur

- Ouvrez VS Code
- Cliquez sur **File > Open Folder**
- Naviguez vers le dossier `iris-analysis`
- Cliquez sur **Select Folder**
- Une notification apparaît en bas à droite : **Folder contains a Dev Container configuration file**
- Cliquez sur **Reopen in Container**
- Si vous ne voyez pas la notification, cliquez sur l'icône verte dans le coin inférieur gauche et sélectionnez **Reopen in Container**
- VS Code construit le conteneur Docker (prend 3 à 5 minutes la première fois)
- Observez la notification de progression montrant les étapes de construction
- Une fois terminé, l'icône verte affiche **Dev Container: Python in Docker**

## Étape 4 : Démarrer Claude Code

- Dans VS Code, cliquez sur **Terminal > New Terminal**
- Vous êtes maintenant à l'intérieur du conteneur Docker
- Tapez cette commande pour démarrer Claude Code :

```bash
claude
```

- Une fenêtre de navigateur s'ouvre pour l'authentification
- Cliquez sur **Continue with Google** ou **Continue with Email**
- Connectez-vous avec votre compte Claude (ou créez-en un)
- Après la réussite de l'authentification, retournez au terminal VS Code
- Vous verrez le message de bienvenue de Claude

Claude Code est maintenant en cours d'exécution et prêt pour vos demandes.

## Étape 5 : Premier Vibe - Charger les Données

Maintenant, le plaisir commence. Au lieu de consulter la documentation, décrivez simplement ce que vous voulez.

- Dans le terminal Claude Code, tapez :

```
Charge le jeu de données iris depuis scikit-learn. Convertis-le en dataframe pandas avec des noms de colonnes appropriés. Ajoute les noms des espèces comme colonne (pas juste des nombres). Montre-moi les 10 premières lignes. Enregistre le code dans un fichier appelé iris_exploration.py
```

- Appuyez sur Entrée
- Observez Claude :
  - Écrire du code Python pour charger les données
  - Créer un script avec les imports appropriés
  - Exécuter le code pour vous montrer les résultats
- Examinez la sortie affichant les mesures des fleurs et les noms d'espèces

Vous venez d'utiliser le vibe coding ! Pas de recherche dans la documentation, pas d'essais et d'erreurs : décrivez et testez simplement.

Demandez à Claude de valider en utilisant Git. Ou faites-le vous-même depuis GitHub Desktop.
```
Valide ces modifications.
```
## Étape 6 : Deuxième Vibe - Statistiques Récapitulatives

Avant de créer des visualisations, comprenez ce que contiennent les données.

- Dans le terminal Claude Code, tapez :

```
Montre-moi les statistiques récapitulatives pour les données iris regroupées par espèce. Je veux voir la moyenne, le min et le max pour chaque mesure (longueur sépale, largeur sépale, longueur pétale, largeur pétale) pour chacune des trois espèces. Ajoute ceci à iris_exploration.py
```

- Appuyez sur Entrée
- Claude met à jour le script et affiche les statistiques
- Remarquez comment différentes espèces ont des plages de mesures différentes
- Setosa a des pétales beaucoup plus petits que Virginica

Cette exploration vous aide à comprendre les motifs dans les données.

Demandez à Claude de valider en utilisant Git. Ou faites-le vous-même depuis GitHub Desktop.

## Étape 7 : Troisième Vibe - Créer un Histogramme

Il est temps de visualiser les données.

- Dans le terminal Claude Code, tapez :

```
Crée un histogramme montrant la distribution des longueurs de pétales pour toutes les fleurs. Utilise 20 intervalles. Ajoute un titre et des étiquettes d'axes. Enregistre le graphique sous petal_length_histogram.png. Ajoute ce code à iris_exploration.py
```

- Appuyez sur Entrée
- Claude crée le code de visualisation
- Un fichier PNG apparaît dans votre dossier de projet
- Ouvrez `petal_length_histogram.png` pour voir le graphique
- Remarquez les deux pics : cela montre que les espèces ont des longueurs de pétales différentes

## Étape 8 : Quatrième Vibe - Nuage de Points

Les nuages de points montrent les relations entre deux variables.

- Dans le terminal Claude Code, tapez :

```
Crée un nuage de points avec la longueur des pétales sur l'axe x et la largeur des pétales sur l'axe y. Colore chaque point par espèce en utilisant différentes couleurs. Ajoute une légende montrant quelle couleur correspond à quelle espèce. Enregistre sous petal_scatter.png. Ajoute ceci à iris_exploration.py
```

- Appuyez sur Entrée
- Claude crée le nuage de points
- Ouvrez `petal_scatter.png` pour voir le résultat
- Remarquez comment les trois espèces forment des groupes distincts
- Setosa (petits pétales) est clairement séparée des autres

C'est le vibe coding en action : décrivez la visualisation, testez-la, itérez.

## Étape 9 : Cinquième Vibe - Diagramme en Boîte

Les diagrammes en boîte sont excellents pour comparer les distributions entre groupes.

- Dans le terminal Claude Code, tapez :

```
Crée un diagramme en boîte comparant les longueurs de pétales des trois espèces. Mets les espèces sur l'axe x et la longueur des pétales sur l'axe y. Utilise différentes couleurs pour chaque espèce. Ajoute un titre. Enregistre sous species_boxplot.png. Ajoute ceci à iris_exploration.py
```

- Appuyez sur Entrée
- Claude ajoute le code du diagramme en boîte
- Ouvrez `species_boxplot.png` pour voir la comparaison
- Les boîtes montrent la médiane et les quartiles pour chaque espèce
- Vous pouvez clairement voir que Virginica a les pétales les plus longs

## Étape 10 : Réviser et Valider

Avant de valider, examinez ce que Claude a construit.

- Dans l'Explorateur VS Code, cliquez sur `iris_exploration.py` pour l'ouvrir
- Parcourez le code : remarquez les imports, le chargement des données et les sections de traçage
- Vous n'avez pas besoin de comprendre chaque ligne, mais ayez une idée de la structure
- Vérifiez que tous les fichiers PNG ont été créés : `petal_length_histogram.png`, `petal_scatter.png`, `species_boxplot.png`
- Ouvrez GitHub Desktop
- Vous verrez tous les nouveaux fichiers listés (le script Python et les images PNG)
- Dans le champ **Summary** en bas à gauche, tapez :

```
Iris data analysis with histograms, scatter plots, and box plots
```

- Cliquez sur **Commit to main**
- Cliquez sur **Push origin** pour sauvegarder sur GitHub

Vous avez enregistré votre première analyse fonctionnelle !

## Étape 11 : Itérer et Améliorer

Le vibe coding brille lorsque vous itérez. Essayez d'ajouter des fonctionnalités en les décrivant :

**Exemples de demandes à Claude :**

- « Ajoute une carte thermique de matrice de corrélation montrant les relations entre les quatre mesures »
- « Crée un violin plot comparant la largeur des sépales entre les espèces »
- « Calcule et affiche le coefficient de corrélation entre la longueur et la largeur des pétales »
- « Ajoute les résultats de tests statistiques comparant les espèces (ANOVA ou test t) »
- « Crée un pair plot montrant toutes les relations entre variables colorées par espèce »

Après chaque fonctionnalité réussie :
- Testez-la en exécutant le script
- Si cela fonctionne, validez avec GitHub Desktop
- Si cela casse, dites à Claude l'erreur et demandez de la corriger
- Une fois corrigée, validez la version fonctionnelle


**Principes clés :**

- **Décrivez les résultats, pas l'implémentation** - Dites « montre une carte thermique de corrélation » et non « utilise seaborn.heatmap() avec df.corr() »
- **Itérez rapidement** - Tester → affiner → tester → affiner
- **Validez les versions fonctionnelles** - Enregistrez chaque succès avant d'essayer de nouvelles fonctionnalités
- **Acceptez les échecs** - Si le code de Claude ne fonctionne pas, décrivez simplement l'erreur et demandez de la corriger
- **Restez aux commandes** - Vous décidez des fonctionnalités, des priorités et quand c'est suffisamment bon

À chaque fois, suivez le modèle : décrire → tester → itérer → valider.

## Prochaines Étapes

- **Essayez différents jeux de données** - Demandez à Claude d'utiliser le jeu de données wine, digits ou de charger un fichier CSV
- **Explorez plus de visualisations** - Essayez les heatmaps, les pair plots ou les violin plots
- **Apprenez en posant des questions** - Quand Claude écrit du code, demandez « explique ce que fait cette ligne » pour apprendre Python
- **Appliquez à vos propres données** - Utilisez le vibe coding pour analyser vos données de recherche ou de travail
- **Lisez sur le vibe coding** - Visitez [le guide d'IBM](https://www.ibm.com/think/topics/vibe-coding) pour en savoir plus sur ce style de codage

## Dépannage

- **Le graphique ne s'affiche pas** - Le code enregistre les graphiques sous forme de fichiers PNG. Regardez dans votre dossier de projet et ouvrez directement le fichier image dans VS Code.
- **Erreurs d'importation** - Le conteneur Docker devrait avoir pandas, matplotlib et scikit-learn pré-installés. Si ce n'est pas le cas, demandez à Claude de les installer avec pip.
- **Claude fait des erreurs** - Normal ! Copiez le message d'erreur, collez-le à Claude et dites « corrige cette erreur ». Le vibe coding inclut l'itération et le débogage.
- **Impossible de pousser vers GitHub** - Assurez-vous que vous êtes connecté à GitHub Desktop et que vous avez publié le dépôt (Étape 1). Vérifiez votre connexion Internet.
- **Le conteneur ne démarre pas** - Assurez-vous que Docker Desktop est en cours d'exécution (indicateur d'état vert). Essayez de cliquer sur l'icône verte dans VS Code et de sélectionner **Rebuild Container**.

## Aperçu du Flux de Travail

Ce tutoriel a combiné plusieurs technologies dans un seul flux de travail :

- **GitHub Desktop** - Contrôle de version avec interface visuelle (créer des dépôts, valider, pousser)
- **Conteneur Docker** - Environnement Python isolé avec toutes les dépendances pré-installées
- **VS Code** - Éditeur de code qui se connecte au conteneur Docker
- **Claude Code** - Assistant IA qui écrit du code Python à partir de vos descriptions
- **scikit-learn** - Fournit le jeu de données Iris et les outils d'apprentissage automatique
- **pandas** - Manipulation et analyse de données
- **matplotlib** - Création de visualisations

La magie n'est pas un seul outil : c'est la façon dont le vibe coding vous permet de décrire ce que vous voulez et d'itérer rapidement. Vous êtes passé d'un projet vide à une analyse de données complète avec plusieurs visualisations en 20 minutes sans écrire une seule ligne de code manuellement.


---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025.
