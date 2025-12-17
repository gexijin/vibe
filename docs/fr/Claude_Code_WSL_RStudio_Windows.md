[Accueil](../fr/)

# Utiliser Claude Code depuis WSL avec RStudio sur Windows

Vous disposez de RStudio sur Windows pour exécuter du code R et de Claude Code dans WSL pour une assistance au codage pilotée par l'IA. Ce tutoriel vous montre comment utiliser ces deux outils ensemble sur les mêmes fichiers de projet. Vous allez créer un projet R dans Windows, écrire du code manuellement, puis utiliser Claude Code depuis le terminal Ubuntu pour l'améliorer avec des visualisations et des analyses—tout en gardant RStudio ouvert pour exécuter et tester votre code.

## Concepts Clés

- **WSL (Windows Subsystem for Linux)** - Exécute Ubuntu Linux à l'intérieur de Windows, où Claude Code est installé
- **Traduction des chemins de fichiers** - Les chemins Windows comme `C:\Users\VotreNom\Documents` deviennent `/mnt/c/Users/VotreNom/Documents` dans WSL
- **Flux de travail hybride** - RStudio (Windows) exécute le code ; Claude Code (WSL) l'écrit et l'améliore

## Ce Dont Vous Aurez Besoin

- Avoir terminé le guide [Installer Claude Code sur Windows](./Install_CLAUDE_Code_Win)
- RStudio installé sur Windows
- 20 à 30 minutes

## Étape 1 : Ouvrir RStudio sur Windows

- Cliquez sur le **bouton Démarrer de Windows**
- Tapez `RStudio` dans la zone de recherche
- Cliquez sur **RStudio** pour l'ouvrir
- La fenêtre RStudio s'ouvre avec plusieurs panneaux

## Étape 2 : Créer un Nouveau Projet R

- Dans RStudio, cliquez sur **File** dans le menu du haut
- Cliquez sur **New Project...**
- Sélectionnez **New Directory**
- Sélectionnez **New Project**
- Pour **Directory name**, tapez : `test_claude`
- Cliquez sur **Browse** à côté de "Create project as subdirectory of:"
- Naviguez vers votre dossier **Documents**
- Cliquez sur **Select Folder**
- Cliquez sur **Create Project**
- RStudio crée le projet et bascule vers celui-ci

## Étape 3 : Créer un Nouveau Script R

- Dans RStudio, cliquez sur **File > New File > R Script**
- Un nouveau script vide s'ouvre dans le panneau en haut à gauche
- Cliquez sur **File > Save** (ou l'icône d'enregistrement)
- Nommez le fichier : `iris.R`
- Cliquez sur **Save**

## Étape 4 : Écrire le Code Initial Manuellement

Tapez ce code dans votre fichier `iris.R` :

```r
data(iris)
str(iris)
summary(iris)
```

- Cliquez sur **File > Save** pour enregistrer vos modifications
- Pour exécuter le code : sélectionnez toutes les lignes, puis cliquez sur le bouton **Run** (en haut à droite du panneau de script)
- Vous devriez voir une sortie dans le panneau Console affichant la structure du jeu de données et les statistiques

## Étape 5 : Ouvrir le Terminal Ubuntu

- Cliquez sur le **bouton Démarrer de Windows**
- Tapez `Ubuntu` dans la zone de recherche
- Cliquez sur **Ubuntu** (icône circulaire orange)
- Le terminal Ubuntu s'ouvre

## Étape 6 : Naviguer vers Votre Dossier de Projet

- Dans le terminal Ubuntu, tapez cette commande (remplacez `VotreNomUtilisateur` par votre véritable nom d'utilisateur Windows) :
  ```
  cd /mnt/c/Users/VotreNomUtilisateur/Documents/test_claude
  ```
- Pour trouver votre nom d'utilisateur, vous pouvez taper : `ls /mnt/c/Users/` et chercher le nom de votre dossier
- Vérifiez que vous êtes au bon endroit en tapant :
  ```
  ls
  ```
- Vous devriez voir `iris.R` et `test_claude.Rproj` listés

## Étape 7 : Lancer Claude Code

- Dans le terminal Ubuntu, tapez :
  ```
  claude
  ```
- Claude Code démarre et affiche un message de bienvenue
- Vous devrez peut-être vous reconnecter - consultez le guide [Installer Claude Code sur Windows](./Install_CLAUDE_Code_Win) pour les étapes d'authentification
- Vous êtes maintenant prêt à utiliser l'assistance IA pour votre projet R

## Étape 8 : Demander à Claude un Nuage de Points

Si Claude Code est lent ou ne répond pas, attendez simplement qu'il s'initialise. Ensuite, tapez cette requête :

```
Add code to iris.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```
- Claude Code va lire votre fichier `iris.R` et ajouter le code de visualisation
- Lorsqu'on vous le demande, donnez à Claude la permission de modifier le fichier iris.R en sélectionnant l'option appropriée
- Attendez que Claude ait terminé (vous verrez un message de confirmation)


## Étape 9 : Exécuter le Nouveau Code dans RStudio

- Revenez à RStudio (cliquez sur la fenêtre RStudio)
- Vous pourriez voir un message indiquant que le fichier a changé - cliquez sur **Yes** pour recharger
- Si aucun message n'apparaît, cliquez sur **File > Reopen with Encoding > UTF-8**
- Sélectionnez tout le code et cliquez sur **Run**
- Un nuage de points apparaît dans le panneau **Plots** (en bas à droite)
- Si vous obtenez une erreur concernant ggplot2, installez-le en tapant `install.packages("ggplot2")` dans le panneau Console

## Étape 10 : Affiner le Nuage de Points

- Revenez au terminal Ubuntu
- Tapez cette requête :
  ```
  Remove title. Change marker type by species. Change to the classic theme.
  ```

## Étape 11 : Voir le Graphique Affiné

- Revenez à RStudio
- Rechargez le fichier si demandé
- Sélectionnez le code mis à jour et cliquez sur **Run**
- Le graphique devrait maintenant s'afficher sans titre, avec différentes formes de marqueurs pour chaque espèce, et en utilisant le thème classique


## Étape 12 : Demander à Claude un Graphique PCA

- Revenez au terminal Ubuntu
- Tapez cette requête :
  ```
  Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
  ```

## Étape 13 : Exécuter l'Analyse PCA

- Revenez à RStudio
- Rechargez le fichier si demandé
- Sélectionnez tout le code et cliquez sur **Run**
- Un graphique PCA apparaît montrant les échantillons projetés sur PC1 et PC2, colorés par espèce

## Étape 14 : Demander à Claude de Réviser et Commenter

- Revenez au terminal Ubuntu
- Tapez cette requête :
  ```
  Review the entire script for correctness. Add comments when necessary.
  ```
- Claude va réviser le code et ajouter des commentaires complets

## Étape 15 : Demander à Claude de Créer un Fichier R Markdown

- Revenez au terminal Ubuntu
- Tapez cette requête :
  ```
  Create a new R Markdown file for this analysis. Save as iris_report.Rmd
  ```
- Claude vous demandera la permission de créer ce fichier.
- Claude va créer un nouveau fichier `.Rmd` dans votre dossier de projet


## Étape 16 : Compiler le Fichier R Markdown

- Revenez à RStudio
- Cliquez sur **File > Open File...**
- Sélectionnez `iris_report.Rmd` et cliquez sur **Open**
- Cliquez sur le bouton **Knit** (avec une icône de pelote de laine) en haut du panneau de script
- RStudio va générer un rapport HTML
- Le rapport s'ouvre dans une nouvelle fenêtre montrant votre analyse complète avec du texte narratif
- Le fichier HTML est enregistré dans votre dossier de projet

## Dépannage

- **"Permission denied" lors de l'accès aux fichiers Windows depuis WSL** - Assurez-vous d'utiliser `/mnt/c/` et non `C:/`. Vérifiez que votre nom d'utilisateur est correct dans le chemin.
- **RStudio n'affiche pas les modifications de fichier** - Cliquez sur **File > Reopen with Encoding > UTF-8** pour recharger manuellement le fichier.
- **"claude: command not found"** - Assurez-vous d'avoir terminé le guide d'installation. Essayez d'ouvrir une nouvelle fenêtre de terminal Ubuntu.
- **Les graphiques n'apparaissent pas** - Assurez-vous que ggplot2 est installé. Exécutez `install.packages("ggplot2")` dans la Console RStudio si nécessaire.
- **Erreur : "cannot change working directory"** - Votre chemin Windows contient des espaces. À l'Étape 6, encadrez le chemin avec des guillemets : `cd "/mnt/c/Users/Votre Nom/Documents/test_claude"`
- **Claude Code est lent à la première requête** - Attendez 30 à 60 secondes pour que Claude s'initialise. Les requêtes suivantes seront plus rapides.

## Prochaines Étapes

- Essayez de demander à Claude d'ajouter des tests statistiques (t-tests, ANOVA) à votre analyse
- Demandez à Claude d'obtenir une **version Python** de ce code et de préparer un document Quarto
- Demandez à Claude de créer des fonctions pour les tâches répétitives dans vos scripts R
- Utilisez Claude pour déboguer les messages d'erreur lorsque votre code R ne s'exécute pas
- Explorez en demandant à Claude d'optimiser du code R lent pour de meilleures performances

## Résumé du Flux de Travail

Cette configuration hybride combine le meilleur des deux mondes :

- **RStudio (Windows)** - Console R interactive, visualisation immédiate des graphiques, interface graphique familière pour exécuter le code
- **Claude Code (WSL)** - Génération, révision et amélioration du code alimentées par l'IA
- **Fichiers partagés** - Les deux outils travaillent sur les mêmes fichiers via le point de montage `/mnt/c/` de WSL
- **Raffinement itératif** - Commencez avec du code manuel, améliorez avec Claude, testez dans RStudio, puis affinez davantage
- **Documentation** - Claude peut générer des rapports complets et des commentaires pour votre analyse

Le flux de travail est simple : écrivez ou modifiez du code avec Claude dans le terminal Ubuntu, puis testez-le et exécutez-le immédiatement dans RStudio. Aucune copie de fichier ni synchronisation manuelle nécessaire—WSL et Windows partagent les mêmes fichiers de manière transparente.

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025.
