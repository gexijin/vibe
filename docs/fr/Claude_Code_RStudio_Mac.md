[Accueil](../fr/)

# Utiliser Claude Code avec RStudio sur Mac

Vous disposez de RStudio sur Mac pour exécuter du code R et de Claude Code pour l'assistance de codage assistée par IA. Ce tutoriel vous montre comment utiliser les deux outils ensemble sur les mêmes fichiers de projet. Vous allez créer un projet R, écrire du code manuellement, puis utiliser Claude Code depuis le Terminal pour l'améliorer avec des visualisations et des analyses, tout en gardant RStudio ouvert pour exécuter et tester votre code.

## Concepts Clés

- **Terminal** - L'interface en ligne de commande de Mac où Claude Code s'exécute
- **Fichiers partagés** - RStudio et Claude Code travaillent sur les mêmes fichiers dans votre dossier Documents
- **Flux de travail hybride** - RStudio exécute le code ; Claude Code l'écrit et l'améliore

## Ce Dont Vous Aurez Besoin

- Avoir complété le guide [Installer Claude Code sur Mac](./Install_Claude_Code_MacOS)
- RStudio installé sur Mac
- 20-30 minutes

## Étape 1 : Ouvrir RStudio sur Mac

- Cliquez sur **Launchpad** dans votre Dock (l'icône en grille de points)
- Tapez `RStudio` dans la zone de recherche
- Cliquez sur **RStudio** pour l'ouvrir
- La fenêtre RStudio s'ouvre avec plusieurs panneaux

## Étape 2 : Créer un Nouveau Projet R

- Dans RStudio, cliquez sur **File** dans le menu supérieur
- Cliquez sur **New Project...**
- Sélectionnez **New Directory**
- Sélectionnez **New Project**
- Pour **Directory name**, tapez : `test_claude`
- Cliquez sur **Browse** à côté de "Create project as subdirectory of:"
- Naviguez jusqu'à votre dossier **Documents**
- Cliquez sur **Open**
- Cliquez sur **Create Project**
- RStudio crée le projet et bascule dessus

## Étape 3 : Créer un Nouveau Script R

- Dans RStudio, cliquez sur **File > New File > R Script**
- Un nouveau script vide s'ouvre dans le panneau supérieur gauche
- Cliquez sur **File > Save** (ou appuyez sur **Command (⌘) + S**)
- Nommez le fichier : `iris.R`
- Cliquez sur **Save**

## Étape 4 : Écrire le Code Initial Manuellement

Tapez ce code dans votre fichier `iris.R` :

```r
data(iris)
str(iris)
summary(iris)
```

- Cliquez sur **File > Save** pour enregistrer vos modifications (ou appuyez sur **Command (⌘) + S**)
- Pour exécuter le code : surlignez toutes les lignes, puis cliquez sur le bouton **Run** (en haut à droite du panneau de script)
- Vous devriez voir le résultat dans le panneau Console montrant la structure et les statistiques du jeu de données

## Étape 5 : Ouvrir le Terminal

- Ouvrez **Finder** et cliquez sur **Applications** dans la barre latérale gauche
- Ouvrez le dossier **Utilities**
- Double-cliquez sur **Terminal**
- La fenêtre Terminal s'ouvre

## Étape 6 : Naviguer vers Votre Dossier de Projet

- Dans le Terminal, tapez cette commande :
  ```
  cd ~/Documents/test_claude
  ```
- Vérifiez que vous êtes au bon emplacement en tapant :
  ```
  ls
  ```
- Vous devriez voir `iris.R` et `test_claude.Rproj` listés

**Astuce :** Si vous n'êtes pas sûr du chemin exact, vous pouvez glisser-déposer le dossier depuis Finder dans le Terminal et le chemin complet apparaîtra automatiquement !

## Étape 7 : Lancer Claude Code

- Dans le Terminal, tapez :
  ```
  claude
  ```
- Claude Code démarre et affiche un message de bienvenue
- Vous devrez peut-être vous authentifier si c'est votre première session
- Vous êtes maintenant prêt à utiliser l'assistance IA pour votre projet R

## Étape 8 : Demander à Claude un Graphique de Dispersion

Si Claude Code est lent ou ne répond pas, attendez simplement qu'il s'initialise. Ensuite, tapez cette demande :

```
Ajoute du code à iris.R pour créer un graphique de dispersion de la longueur vs. largeur des sépales, coloré par espèce. Utilise ggplot2.
```
- Claude Code va lire votre fichier `iris.R` et ajouter le code de visualisation
- Lorsqu'on vous le demande, donnez à Claude la permission de modifier le fichier iris.R en sélectionnant l'option appropriée
- Attendez que Claude termine (vous verrez un message de confirmation)


## Étape 9 : Exécuter le Nouveau Code dans RStudio

- Revenez à RStudio (cliquez sur la fenêtre RStudio ou appuyez sur **Command (⌘) + Tab**)
- Vous verrez peut-être une invite indiquant que le fichier a changé - cliquez sur **Yes** pour recharger
- Si aucune invite n'apparaît, cliquez sur **File > Reopen with Encoding > UTF-8**
- Surlignez tout le code et cliquez sur **Run**
- Un graphique de dispersion apparaît dans le panneau **Plots** (en bas à droite)
- Si vous obtenez une erreur concernant ggplot2, installez-le en tapant `install.packages("ggplot2")` dans le panneau Console

## Étape 10 : Affiner le Graphique de Dispersion

- Revenez au Terminal (appuyez sur **Command (⌘) + Tab** ou cliquez sur la fenêtre Terminal)
- Tapez cette demande :
  ```
  Supprime le titre. Change le type de marqueur par espèce. Passe au thème classique.
  ```

## Étape 11 : Voir le Graphique Affiné

- Revenez à RStudio
- Rechargez le fichier si demandé
- Surlignez le code mis à jour et cliquez sur **Run**
- Le graphique devrait maintenant s'afficher sans titre, avec différentes formes de marqueurs pour chaque espèce, et utilisant le thème classique


## Étape 12 : Demander à Claude un Graphique PCA

- Revenez au Terminal
- Tapez cette demande :
  ```
  Ajoute du code pour effectuer une ACP sur les variables numériques et tracer les échantillons en utilisant les deux premières composantes principales.
  ```

## Étape 13 : Exécuter l'Analyse PCA

- Revenez à RStudio
- Rechargez le fichier si demandé
- Surlignez tout le code et cliquez sur **Run**
- Un graphique PCA apparaît montrant les échantillons projetés sur PC1 et PC2, colorés par espèce

## Étape 14 : Demander à Claude de Réviser et Commenter

- Revenez au Terminal
- Tapez cette demande :
  ```
  Révise le script entier pour vérifier qu'il est correct. Ajoute des commentaires si nécessaire.
  ```
- Claude va réviser le code et ajouter des commentaires complets

## Étape 15 : Demander à Claude de Créer un Document R Markdown

- Revenez au Terminal
- Tapez cette demande :
  ```
  Crée un nouveau fichier R Markdown pour cette analyse. Enregistre-le sous iris_report.Rmd
  ```
- Claude vous demandera la permission de créer ce fichier
- Claude créera un nouveau fichier `.Rmd` dans votre dossier de projet


## Étape 16 : Compiler le Fichier R Markdown

- Revenez à RStudio
- Cliquez sur **File > Open File...**
- Sélectionnez `iris_report.Rmd` et cliquez sur **Open**
- Cliquez sur le bouton **Knit** (avec une icône de pelote de laine) en haut du panneau de script
- RStudio va générer un rapport HTML
- Le rapport s'ouvre dans une nouvelle fenêtre montrant votre analyse complète avec du texte narratif
- Le fichier HTML est enregistré dans votre dossier de projet

## Dépannage

- **RStudio n'affiche pas les modifications du fichier** - Cliquez sur **File > Reopen with Encoding > UTF-8** pour recharger manuellement le fichier, ou fermez et rouvrez le fichier.
- **"claude: command not found"** - Assurez-vous d'avoir complété le [guide d'installation](./Install_Claude_Code_MacOS). Essayez d'ouvrir une nouvelle fenêtre Terminal, ou fermez Terminal complètement (**Command (⌘) + Q**) et rouvrez-le.
- **Les graphiques n'apparaissent pas** - Assurez-vous que ggplot2 est installé. Exécutez `install.packages("ggplot2")` dans la Console RStudio si nécessaire.
- **"No such file or directory"** - Vérifiez que vous avez tapé le chemin correctement à l'Étape 6. Essayez d'utiliser l'astuce glisser-déposer : glissez le dossier test_claude depuis Finder dans le Terminal après avoir tapé `cd ` (avec un espace).
- **Claude Code est lent lors de la première demande** - Attendez 30-60 secondes pour que Claude s'initialise. Les demandes suivantes seront plus rapides.

## Raccourcis Clavier Mac

Raccourcis utiles pour basculer entre les applications :
- **Command (⌘) + Tab** - Basculer rapidement entre les applications ouvertes
- **Command (⌘) + `** (accent grave) - Basculer entre les fenêtres de la même application
- **Command (⌘) + Space** - Ouvrir la recherche Spotlight (pour ouvrir des applications)
- **Command (⌘) + Q** - Quitter complètement une application

## Prochaines Étapes

- Essayez de demander à Claude d'ajouter des tests statistiques (tests t, ANOVA) à votre analyse
- Demandez à Claude d'obtenir une **version Python** de ce code et de préparer un document Quarto
- Demandez à Claude de créer des fonctions pour les tâches répétitives dans vos scripts R
- Utilisez Claude pour déboguer les messages d'erreur lorsque votre code R ne s'exécute pas
- Explorez la possibilité de demander à Claude d'optimiser du code R lent pour de meilleures performances

## Résumé du Flux de Travail

Cette configuration hybride combine le meilleur des deux mondes :

- **RStudio (Mac)** - Console R interactive, visualisation immédiate des graphiques, interface graphique familière pour exécuter le code
- **Claude Code (Terminal)** - Génération de code assistée par IA, révision et amélioration
- **Fichiers partagés** - Les deux outils travaillent sur les mêmes fichiers dans votre dossier Documents
- **Raffinement itératif** - Commencez avec du code manuel, améliorez-le avec Claude, testez dans RStudio, puis affinez davantage
- **Documentation** - Claude peut générer des rapports et des commentaires complets pour votre analyse

Le flux de travail est simple : écrivez ou modifiez du code avec Claude dans le Terminal, puis testez-le et exécutez-le immédiatement dans RStudio. Aucune copie de fichiers ou synchronisation manuelle nécessaire—les deux applications accèdent aux mêmes fichiers de manière transparente sur votre Mac.

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2024.
