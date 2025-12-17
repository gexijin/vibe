[Accueil](./)

# Exécuter R dans VS Code

Vous souhaitez écrire du code R mais RStudio vous semble lourd ou vous préférez la flexibilité de VS Code. Considérez VS Code comme un couteau suisse - il peut gérer R, Python et de nombreux autres langages dans un seul éditeur léger. Ce tutoriel vous montre comment configurer R dans VS Code avec des fonctionnalités intelligentes comme la complétion de code, les graphiques interactifs et même les applications Shiny.

## Concepts Clés

- **[languageserver](https://github.com/REditorSupport/languageserver)** - Package R qui permet la complétion de code, la vérification de syntaxe et la documentation au survol dans VS Code
- **[R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)** - Extension VS Code qui connecte votre éditeur à R et fournit la coloration syntaxique, l'exécution de code et le débogage
- **[Shiny Extension](https://marketplace.visualstudio.com/items?itemName=Posit.shiny)** - Extension VS Code pour créer et exécuter des applications web Shiny interactives avec rechargement automatique

## Ce Dont Vous Aurez Besoin

- Avoir terminé [VS Code Basics](./VS_Code_Getting_Started)
- Connexion Internet pour télécharger R et les packages
- 10 à 15 minutes

## Étape 1 : Installer ou Mettre à Jour R

Vous avez besoin de R version 4.0 ou supérieure pour une meilleure compatibilité.

- **Windows** :
  - Téléchargez la dernière version de R depuis [CRAN Windows](https://cran.r-project.org/bin/windows/base/) et exécutez l'installateur
  - Pendant l'installation, **notez le chemin d'installation** (par exemple : `C:\Program Files\R\R-4.5.3`)
  - Si vous avez une ancienne version, désinstallez-la d'abord via Paramètres > Applications

- **macOS** :
  - Téléchargez depuis [CRAN macOS](https://cran.r-project.org/bin/macosx/) et exécutez l'installateur .pkg
  - Notez si vous utilisez Intel (`/Library/Frameworks/R.framework/Resources/bin/R`) ou Apple Silicon avec Homebrew (`/opt/homebrew/bin/R`)
  - Lors de la mise à jour, la nouvelle version remplacera l'ancienne

- **Linux** :
  - Utilisez votre gestionnaire de packages (par exemple, `sudo apt install r-base` sur Ubuntu)
  - Ou suivez les instructions [CRAN Linux](https://cran.r-project.org/bin/linux/)

Vous configurerez VS Code pour trouver R à l'Étape 3, donc ne vous inquiétez pas si `R --version` ne fonctionne pas encore dans votre terminal.

## Étape 2 : Installer les Extensions R dans VS Code

- Ouvrez VS Code
- Cliquez sur l'icône **Extensions** dans la barre latérale gauche
- Recherchez `REditorSupport.r` et cliquez sur **Install** sur l'extension R par REditorSupport
- Recherchez `Posit.shiny` et cliquez sur **Install** sur l'extension Shiny par Posit

## Étape 3 : Trouver le Chemin d'Installation de R

Avant de configurer VS Code, vous devez savoir où R est installé sur votre système.

### Pour les Utilisateurs Windows

1. Ouvrez l'**Explorateur de Fichiers**
2. Naviguez vers `C:\Program Files\R\`
3. Vous verrez un dossier comme `R-4.5.3` (votre numéro de version peut différer)
4. Ouvrez ce dossier → Ouvrez le dossier `bin`
5. Vous verrez `R.exe` là
6. Le chemin complet est : `C:\Program Files\R\R-4.5.3\bin\R.exe`

**Notez ou retenez votre numéro de version** (par exemple, `R-4.5.3`) - vous en aurez besoin à l'Étape 4.

### Pour les Utilisateurs macOS

Votre installation de R se trouve généralement dans l'un de ces emplacements :

- **Installation standard (Intel ou Apple Silicon)** : `/Library/Frameworks/R.framework/Resources/bin/R`
- **Homebrew sur Apple Silicon** : `/opt/homebrew/bin/R`
- **Homebrew sur Intel** : `/usr/local/bin/R`

Pour vérifier quel chemin vous avez, ouvrez le **Terminal** et tapez :
```bash
which R
```

Cela vous montrera le chemin exact de votre installation de R.

### Pour les Utilisateurs Linux

R est généralement installé à : `/usr/bin/R`

Vérifiez en ouvrant un terminal et en tapant :
```bash
which R
```

## Étape 4 : Configurer VS Code pour Trouver R

- Dans VS Code, cliquez sur l'**icône d'engrenage** dans le coin inférieur gauche
- Sélectionnez **Settings** dans le menu
- Dans la barre de recherche en haut, tapez `r.rpath.windows` (Windows), `r.rpath.mac` (macOS), ou `r.rpath.linux` (Linux)
- Vous devriez voir le paramètre apparaître. Cliquez sur **Edit in settings.json** sous le paramètre
- Le fichier settings.json s'ouvrira
- Ajoutez la configuration appropriée pour votre plateforme à l'intérieur des accolades `{}`

**Pour Windows**, ajoutez cette ligne (remplacez `R-4.5.3` par votre version de l'Étape 3) :

```json
"r.rpath.windows": "C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe",
```

**Pourquoi deux barres obliques inverses (`\\`) ?** Dans les fichiers JSON, la barre oblique inverse `\` est un caractère spécial (appelé caractère d'échappement). Pour représenter une seule barre oblique inverse dans le chemin de fichier réel, vous devez taper deux barres obliques inverses `\\`. Donc `C:\Program Files` devient `C:\\Program Files` dans settings.json.

**Pour macOS**, ajoutez l'une de ces lignes :

```json
"r.rpath.mac": "/Library/Frameworks/R.framework/Resources/bin/R",
```

Ou si vous avez installé R via Homebrew sur Apple Silicon :

```json
"r.rpath.mac": "/opt/homebrew/bin/R",
```

**Pour Linux**, ajoutez :

```json
"r.rpath.linux": "/usr/bin/R",
```

- Enregistrez le fichier en cliquant sur **File > Save**
- **Redémarrez VS Code** complètement pour que les modifications prennent effet

## Étape 5 : Installer les Packages R Requis

- Dans VS Code, cliquez sur **View** dans le menu supérieur, puis sélectionnez **Command Palette**
- Tapez `R: Create R Terminal` et sélectionnez-le
- Une console R apparaîtra dans le panneau terminal en bas
  - Vous devriez voir R démarrer avec les informations de version
  - Si vous obtenez une erreur, vérifiez à nouveau votre configuration settings.json à l'Étape 4 et redémarrez VS Code
- Installez les packages en tapant ces commandes une par une :

```r
install.packages("languageserver")
install.packages("shiny")
```

- Attendez que l'installation se termine (peut prendre quelques minutes)
- Tapez `q()` et appuyez sur Entrée pour quitter R
- Tapez `n` lorsqu'on vous demande d'enregistrer l'espace de travail

Simplement taper `R` dans un terminal normal ne fonctionnera pas à moins que R ne soit dans votre PATH système. L'extension R utilise votre paramètre `r.rpath` pour trouver R.

## Étape 6 : Créer Votre Projet R

- Créez un nouveau dossier sur votre ordinateur (par exemple, `my-r-project`)
- Dans VS Code, cliquez sur **File > Open Folder** et sélectionnez votre nouveau dossier
- Cliquez sur **File > New File** dans le menu supérieur
- Enregistrez le fichier sous `analysis.R` en cliquant sur **File > Save**

## Étape 7 : Écrire Votre Premier Script R

- Tapez ce code dans `analysis.R` :

```r
# Load the iris dataset
data(iris)

# View the first few rows
head(iris)

# Generate summary statistics
summary(iris)

hist(iris$Sepal.Length)
```

- Enregistrez le fichier en cliquant sur **File > Save**

## Étape 8 : Exécuter du Code R de Manière Interactive

- Avec `analysis.R` ouvert, sélectionnez une ligne de code et appuyez sur `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (Mac) pour l'exécuter
- Si vous n'avez pas de terminal ouvert, le premier `Ctrl+Enter` / `Cmd+Enter` ouvre un terminal R. Le second exécute le code.
- Observez la sortie apparaître dans le terminal et le graphique s'ouvrira dans une fenêtre séparée
- Vous pouvez également sélectionner toutes les lignes et les exécuter de la même manière.

## Étape 9 : Créer une Application Shiny Simple

- Créez un nouveau fichier dans votre dossier de projet : **File > New File**
- Enregistrez-le sous `app.R`
- Tapez ce code :

```r
library(shiny)

ui <- fluidPage(
  titlePanel("Interactive Histogram"),

  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 5,
                  max = 50,
                  value = 30)
    ),

    mainPanel(
      plotOutput("histogram")
    )
  )
)

server <- function(input, output) {
  output$histogram <- renderPlot({
    x <- faithful$waiting
    bins <- seq(min(x), max(x), length.out = input$bins + 1)

    hist(x, breaks = bins, col = "steelblue", border = "white",
         xlab = "Waiting time (minutes)",
         main = "Distribution of Waiting Times")
  })
}

shinyApp(ui = ui, server = server)
```

- Enregistrez le fichier
- Remarquez le bouton **▶** qui apparaît en haut à droite de l'éditeur
- Cliquez sur le menu déroulant pour sélectionner **Run Shiny App**
- L'application s'ouvre dans un navigateur ou un panneau VS Code
- Déplacez le curseur et observez l'histogramme se mettre à jour instantanément

## Étape 10 : Utiliser la Complétion de Code et l'Aide au Survol

- Dans `analysis.R`, commencez à taper `mea` sur une nouvelle ligne
- Un menu déroulant apparaît avec des suggestions - sélectionnez `mean()` en appuyant sur Entrée
- Survolez avec votre souris le mot `mean` dans votre code existant
- Une fenêtre contextuelle affiche la documentation de la fonction et des exemples d'utilisation
- Essayez de survoler `lm`, `summary`, ou `plot` pour voir leur documentation
- Tapez `data$` et regardez VS Code suggérer les noms de colonnes (`x` et `y`)

## Étape 11 : Essayer Plus de Fonctionnalités

- **Intégration Markdown** : Créez un fichier R Markdown (`.Rmd`) pour mélanger code, sortie et texte
- **Formatage de code** : Faites un clic droit dans votre script R et sélectionnez **Format Document** pour formater automatiquement le code
- **Débogage** : Définissez des points d'arrêt en cliquant à gauche des numéros de ligne, puis exécutez le code en mode débogage
- **Intégration Git** : Utilisez les fonctionnalités Git intégrées de VS Code pour contrôler la version de vos projets R

## Prochaines Étapes

- Créez une application Shiny multi-fichiers avec des fichiers séparés `ui.R` et `server.R`
- Explorez [ggplot2](https://ggplot2.tidyverse.org/) pour la visualisation avancée de données
- Essayez les packages [tidyverse](https://www.tidyverse.org/) (`dplyr`, `tidyr`) pour la manipulation de données
- Apprenez R Markdown ou [Quarto](https://quarto.org/) pour créer des rapports avec du code R intégré
- Installez l'[extension R Debugger](https://marketplace.visualstudio.com/items?itemName=RDebugger.r-debugger) pour un débogage avancé

## Dépannage

- **« R is not recognized » dans le terminal VS Code** : VS Code ne peut pas trouver R. Vérifiez votre settings.json (Étape 4) - vérifiez que le chemin R est correct et pointe vers `R.exe` (Windows) ou le binaire R (Mac/Linux). Exemples de chemins :
  - Windows : `C:\\Program Files\\R\\R-4.5.3\\bin\\R.exe` (ajustez le numéro de version)
  - macOS Intel : `/Library/Frameworks/R.framework/Resources/bin/R`
  - macOS Homebrew : `/opt/homebrew/bin/R`
  - Linux : `/usr/bin/R`
  Après correction, redémarrez VS Code complètement.

- **Incompatibilité de version R dans les paramètres** : Si vous avez mis à jour R mais que VS Code utilise toujours l'ancienne version, mettez à jour le numéro de version dans votre configuration `r.rpath` de settings.json pour correspondre à la nouvelle installation de R (voir Étape 3 pour trouver votre chemin d'installation actuel).

- **La complétion de code ne fonctionne pas** : Assurez-vous que languageserver s'est installé avec succès (Étape 5). Redémarrez VS Code après l'installation. Attendez 10 à 20 secondes après l'ouverture d'un fichier R pour que le serveur de langage s'initialise. Vérifiez le panneau Output (View > Output > R Language Server) pour les erreurs.

- **Les graphiques n'apparaissent pas** : Les graphiques s'ouvriront dans des fenêtres séparées en utilisant le périphérique graphique par défaut de R. Assurez-vous d'avoir un gestionnaire de fenêtres disponible. Sur certains systèmes, vous devrez peut-être installer X11 (macOS) ou vous assurer que le support graphique est activé.

- **L'application Shiny ne s'exécute pas** : Assurez-vous que l'extension Shiny est installée (Étape 2), que le package shiny est installé (Étape 5), et que votre fichier est nommé `app.R`. Vérifiez le terminal pour les messages d'erreur. Le bouton Run n'apparaît que lorsque VS Code reconnaît le fichier comme une application Shiny.

## Résumé du Flux de Travail

VS Code fournit une alternative moderne et légère à RStudio avec ces avantages clés :

- **Environnement unifié** : Codez en R, Python, JavaScript et plus dans un seul éditeur
- **Personnalisable** : Installez uniquement les extensions dont vous avez besoin pour une configuration légère
- **Terminal intégré** : Exécutez R, Git et des commandes shell côte à côte
- **Développement Shiny** : Lancement d'application en un clic avec rechargement automatique fait gagner du temps
- **Contrôle de version** : Intégration Git intégrée sans outils externes

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 7 décembre 2025.
