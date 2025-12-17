[Accueil](../fr/)

# Codage R dans VS Code via un conteneur Docker

Avez-vous déjà essayé de partager votre code R avec un collègue, pour ensuite passer des heures à déboguer des problèmes du type "mais ça fonctionne sur ma machine" ? Les conteneurs Docker sont comme des conteneurs maritimes pour le code : ils emballent votre environnement R, vos bibliothèques et vos dépendances dans une boîte scellée qui fonctionne de la même manière partout. De plus, vous avez accès à des dizaines de milliers d'images pré-construites sur [Docker Hub](https://hub.docker.com/), où les développeurs de logiciels publient des environnements prêts à l'emploi, vous évitant ainsi la corvée de l'installation manuelle de logiciels. Ce tutoriel vous montre comment exécuter R dans un environnement isolé et reproductible en utilisant VS Code et Docker Desktop.

## Concepts Clés

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Application qui exécute des conteneurs sur votre ordinateur, gérant des environnements isolés
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - Fonctionnalité de VS Code qui vous permet de coder à l'intérieur d'un conteneur Docker avec un support complet de l'IDE
- **Isolation de conteneur** - Votre code s'exécute dans un environnement Linux séparé qui ne voit que votre dossier de projet, et non votre ordinateur entier
- **[Rocker](https://rocker-project.org/)** - Images Docker pré-construites spécialement conçues pour le développement R

## Ce Dont Vous Aurez Besoin

- Avoir terminé [R Coding in VS Code](./R_Coding_VS_Code_Guide)
- Avoir terminé [GitHub Desktop Basics](./Github_desktop)
- 20-25 minutes

## Étape 1 : Installez Docker Desktop

- Visitez la [page de téléchargement de Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Cliquez sur **Download for Windows** (ou Mac/Linux selon votre système)
- Exécutez le programme d'installation et suivez l'assistant d'installation
- Lorsque vous y êtes invité, activez WSL 2 (utilisateurs Windows) ou acceptez les paramètres par défaut
- Après l'installation, lancez Docker Desktop
- Attendez que le moteur Docker démarre (vous verrez un indicateur de statut vert en bas à gauche)

## Étape 2 : Installez l'extension Dev Containers

- Ouvrez VS Code
- Cliquez sur l'icône **Extensions** dans la barre latérale gauche (ou cliquez sur **View > Extensions**)
- Tapez `dev containers` dans la zone de recherche
- Trouvez **Dev Containers** par Microsoft
- Cliquez sur **Install**

## Étape 3 : Clonez le projet Vibe avec GitHub Desktop

- Ouvrez GitHub Desktop
- Cliquez sur **File > Clone repository**
- Cliquez sur l'onglet **URL**
- Dans le champ **Repository URL**, collez : `https://github.com/gexijin/vibe`
- Choisissez où enregistrer le projet (le champ **Local Path**)
- Cliquez sur **Clone**
- GitHub Desktop téléchargera le projet à l'emplacement que vous avez choisi

## Étape 4 : Ouvrez le projet dans VS Code

- Dans VS Code, cliquez sur **File > Open Folder**
- Naviguez jusqu'au dossier `vibe` que vous venez de cloner
- Cliquez sur **Select Folder**
- Vous verrez les fichiers du projet dans la barre latérale Explorer

## Étape 5 : Rouvrez dans le conteneur

- Recherchez une notification en bas à droite : **Folder contains a Dev Container configuration file**
- Cliquez sur **Reopen in Container**
- Si vous ne voyez pas la notification, cliquez sur l'icône verte dans le coin inférieur gauche
- Sélectionnez **Reopen in Container** dans le menu
- VS Code construira le conteneur (cela prend 5-10 minutes la première fois)
- Vous verrez une notification de progression affichant les étapes de construction
- Lorsque terminé, l'icône verte affichera **Dev Container: R in Docker**

**Remarque :** Le conteneur inclut automatiquement l'extension R et le package languageserver. Le Dockerfile et le devcontainer.json gèrent cela pour vous.

## Étape 6 : Comprenez l'environnement du conteneur

Vous codez maintenant à l'intérieur d'un conteneur Linux. Explorons ce que cela signifie.

- Cliquez sur **Terminal > New Terminal** pour ouvrir un terminal à l'intérieur du conteneur
- Vérifiez votre emplacement actuel :

```bash
pwd
```

Vous verrez `/workspaces/vibe` - c'est votre dossier de projet à l'intérieur du conteneur.

- Listez les fichiers :

```bash
ls
```

Vous verrez les mêmes fichiers du projet : `R/`, `.devcontainer/`, `README.md`, etc.

- Essayez de remonter d'un répertoire :

```bash
cd ..
ls
```

Vous ne verrez que `vibe/` - le conteneur est isolé. Vous ne pouvez pas accéder aux autres dossiers de votre ordinateur, au Bureau ou aux Documents. Cette isolation garantit que votre environnement R est propre et reproductible.

- Revenez au dossier du projet :

```bash
cd vibe
```

## Étape 7 : Exécutez du code R ligne par ligne

Le conteneur a R pré-installé avec des packages communs. Exécutons un script d'analyse de données simple.

- Dans l'Explorer de VS Code, naviguez jusqu'à `R/iris_analysis.R`
- Cliquez pour ouvrir le fichier
- Vous verrez du code R qui analyse le jeu de données iris
- Sélectionnez la première ligne : `data(iris)`
- Appuyez sur `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (Mac) pour l'exécuter
- Si vous n'avez pas de terminal R ouvert, la première fois en crée un, la deuxième fois exécute le code
- Continuez à exécuter chaque ligne une à la fois
- Lorsque vous exécutez `head(iris)`, vous verrez les 6 premières lignes dans le terminal
- Lorsque vous exécutez `summary(iris)`, vous verrez des résumés statistiques
- Lorsque vous exécutez les commandes `hist()`, des graphiques d'histogrammes s'ouvriront dans des fenêtres séparées
- Vous pouvez également sélectionner plusieurs lignes et les exécuter ensemble avec `Ctrl+Enter` ou `Cmd+Enter`

## Étape 8 : Exécutez l'application

Le projet inclut une application Shiny de démonstration qui crée un histogramme interactif.

- Dans l'Explorer de VS Code, naviguez jusqu'à `R/app.R`
- Cliquez pour ouvrir le fichier
- Vous verrez le code d'une application web Shiny
- Regardez en haut à droite de la fenêtre de l'éditeur pour un bouton **▶**
- Cliquez sur la flèche déroulante à côté et sélectionnez **Run Shiny App**
- L'application démarrera et VS Code transférera automatiquement le port 3838
- Une notification apparaît : **Open in Browser**
- Cliquez sur **Open in Browser**
- L'application Shiny s'ouvre dans votre navigateur web
- Déplacez le curseur pour changer les barres de l'histogramme - le graphique se met à jour en temps réel

## Étape 9 : Effectuez une modification simple

Modifions l'application pour voir comment fonctionne le développement.

- Laissez l'application en cours d'exécution
- Dans VS Code, modifiez `R/app.R`
- Trouvez la ligne 16 : `titlePanel("Old Faithful Geyser Data")`
- Changez-la en :

```r
titlePanel("My First R Docker App")
```

- Enregistrez le fichier (**File > Save**)
- L'extension Shiny rechargera automatiquement l'application
- Actualisez votre navigateur (ou il peut s'actualiser automatiquement)
- Le titre affiche maintenant votre texte personnalisé

## Étape 10 : Comprendre le Dockerfile (Optionnel)

- Dans l'Explorer de VS Code, naviguez jusqu'à `.devcontainer/Dockerfile`
- Cliquez pour ouvrir le fichier
- Vous verrez la configuration complète :

```dockerfile
# choose a Dockerhub base image
FROM rocker/shiny-verse:latest

# 1. System deps commonly needed by R packages
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# 2. R packages for VS Code integration: language server + debugger
RUN R -q -e 'install.packages(c("rstudioapi", "languageserver"), repos="https://cloud.r-project.org")'

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Shiny server port
EXPOSE 3838
```

**Parties clés :**

- `FROM rocker/shiny-verse:latest` - Image de base avec R, Shiny et tidyverse pré-installés
- `RUN apt-get install` - Bibliothèques système Linux pour les packages R
- `RUN R -q -e 'install.packages(...)'` - Installe les packages R de manière permanente
- `RUN curl... && apt-get install -y nodejs` - Installe Node.js, requis pour exécuter Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Installe Claude Code globalement pour l'assistance IA
- `EXPOSE 3838` - Ouvre le port 3838 pour les applications Shiny

**Autres images Rocker que vous pouvez utiliser :**

- `rocker/r-ver:4.5.3` - Juste R (version spécifique)
- `rocker/rstudio:latest` - R avec RStudio Server
- `rocker/tidyverse:latest` - R avec les packages tidyverse
- `rocker/shiny-verse:latest` - R avec Shiny et tidyverse (ce que nous utilisons)

Après avoir modifié l'image de base, reconstruisez le conteneur pour appliquer les modifications.

## Étape 11 : Installez des packages R dans l'image Docker (Optionnel)

Les packages installés via la console R (`install.packages()`) sont temporaires et disparaissent lorsque vous reconstruisez le conteneur. Pour rendre les packages permanents, ajoutez-les au Dockerfile.

- Dans l'Explorer de VS Code, naviguez jusqu'à `.devcontainer/Dockerfile`
- Cliquez pour ouvrir le fichier
- Ajoutez une nouvelle ligne sous les autres lignes 'install.packages' pour installer le package `data.table` :
```dockerfile
RUN R -q -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
```

- Enregistrez le fichier (**File > Save**)
- Cliquez sur l'icône verte dans le coin inférieur gauche
- Sélectionnez **Rebuild Container** dans le menu
- VS Code reconstruira le conteneur avec votre nouveau package (cela prend 2-5 minutes)
- Pour vérifier, ouvrez un terminal R et tapez :

```r
library(data.table)
```

S'il se charge sans erreurs, le package est installé de manière permanente.

## Prochaines Étapes

- **Créez un nouveau script R** - Créez un nouveau fichier `.R` dans le dossier `R/`, écrivez du code d'analyse de données en utilisant des jeux de données intégrés comme `mtcars` ou `iris`
- **Installez des packages R** - Ajoutez les packages dont vous avez besoin en modifiant le Dockerfile et en reconstruisant le conteneur
- **Explorez tidyverse** - Essayez la manipulation de données avec `dplyr` et la visualisation avec `ggplot2` en utilisant des exemples de jeux de données

## Dépannage

- **Docker Desktop ne fonctionne pas** - Ouvrez Docker Desktop et attendez l'indicateur de statut vert avant de rouvrir le conteneur
- **La construction du conteneur échoue** - Vérifiez votre connexion Internet ; la première construction télécharge environ 2 Go. Cliquez sur **Rebuild Container** pour réessayer
- **Le port 3838 est déjà utilisé** - Arrêtez les autres applications utilisant ce port, ou changez le port dans `.devcontainer/devcontainer.json`

## Aperçu du flux de travail

Cette configuration vous offre un environnement de développement R professionnel :

- **VS Code** fournit l'éditeur de code avec la coloration syntaxique et IntelliSense
- **Le conteneur Docker** exécute un environnement Linux isolé avec R et toutes les dépendances
- **L'image Rocker** (`rocker/shiny-verse`) inclut R, Shiny, tidyverse et des outils de développement
- **La configuration Dev Container** (`.devcontainer/`) installe automatiquement les extensions VS Code pour le débogage R et le support du langage
- **Le transfert de port** vous permet d'accéder à l'application Shiny s'exécutant à l'intérieur du conteneur depuis votre navigateur

## Flux de travail quotidien

Une fois que tout est configuré, voici votre routine quotidienne :

1. **Démarrez Docker Desktop** - Ouvrez l'application et attendez l'indicateur de statut vert (Docker doit être en cours d'exécution)
2. **Ouvrez VS Code** - Lancez VS Code et ouvrez votre dossier de projet
3. **Rouvrez dans le conteneur** - Si vous n'êtes pas déjà dans le conteneur, cliquez sur l'icône verte (en bas à gauche) et sélectionnez **Reopen in Container**
4. **Écrivez et exécutez du code** - Modifiez les fichiers `.R`, exécutez ligne par ligne avec `Ctrl+Enter`/`Cmd+Enter`, ou exécutez des applications Shiny avec le bouton **▶ Run Shiny App**
5. **Enregistrez votre travail** - Vos fichiers de code (`.R`, `.Rmd`) sont enregistrés sur votre ordinateur et persistent d'une session à l'autre
6. **Committez et poussez** - Utilisez GitHub Desktop pour committer vos modifications et pousser vers le dépôt

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 7 décembre 2025.
