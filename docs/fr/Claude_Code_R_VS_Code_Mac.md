[Accueil](../fr/)

# Utiliser Claude Code pour R dans VS Code sur Mac

Vous avez configuré R dans VS Code et pouvez écrire du code manuellement. Maintenant, vous souhaitez que l'IA vous aide à écrire, améliorer et déboguer votre code R pendant que vous vous concentrez sur l'analyse. Considérez Claude Code comme un partenaire de codage qui vit à l'intérieur de VS Code - vous décrivez ce que vous voulez, et il écrit ou améliore le code pendant que vous restez dans la même fenêtre.

## Concepts Clés

- **[Extension Claude Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - Extension VS Code qui intègre l'assistant IA Claude directement dans votre éditeur avec des modifications de code en ligne
- **Panneau de Discussion** - Panneau latéral dans VS Code où vous conversez avec Claude à propos de votre code
- **Modifications en Ligne** - Les suggestions de modifications de code de Claude apparaissent directement dans vos fichiers avec des diffs que vous pouvez accepter ou rejeter

## Ce Dont Vous Aurez Besoin

- Tutoriel [R dans VS Code](./R_Coding_VS_Code_Guide) terminé - R doit fonctionner dans VS Code
- Tutoriel [Installation de Claude Code sur Mac](./Install_Claude_Code_MacOS) terminé - L'interface CLI Claude Code doit être installée
- Abonnement Claude Pro/Max ou clé API Anthropic
- 20-30 minutes

## Étape 1 : Ouvrir VS Code et Créer un Projet R

- Ouvrez **Visual Studio Code**
- Cliquez sur **File** dans la barre de menu, puis sur **Open Folder**
- Naviguez vers votre dossier **Documents**
- Cliquez sur **New Folder** en bas de la boîte de dialogue
- Nommez le dossier `claude_r_test`
- Cliquez sur **Open** pour ouvrir le nouveau dossier
- Si on vous demande "Do you trust the authors?", cliquez sur **Yes, I trust the authors**

## Étape 2 : Installer et Se Connecter à l'Extension Claude Code

- Cliquez sur l'icône **Extensions** dans la barre latérale gauche (icône à quatre carrés)
- Dans la zone de recherche, tapez `Claude Code`
- Trouvez **Claude Code** par Anthropic et cliquez sur **Install**
- Après l'installation, une icône Claude (étincelle) apparaît dans la barre latérale gauche
- Cliquez sur l'icône Claude pour ouvrir le panneau de discussion
- Cliquez sur **Sign in to Claude Code** dans le panneau de discussion
- Choisissez votre méthode d'authentification :
  - **Utilisateurs Claude Pro/Max** : Cliquez sur **Sign in with Claude.ai**, autorisez dans le navigateur, et copiez le code dans VS Code
  - **Utilisateurs avec clé API** : Cliquez sur **Use API Key** et collez votre clé API Anthropic
- Pour des étapes d'authentification détaillées, consultez le guide [Installation de Claude Code sur Mac](./Install_Claude_Code_MacOS) (Étape 5)
- Une fois connecté, vous verrez "Ready to help" dans le panneau de discussion

## Étape 3 : Créer un Script R Initial Manuellement

- Cliquez sur **File > New File** dans la barre de menu
- Cliquez sur **Select a language** et tapez `R`, puis sélectionnez **R**
- Enregistrez le fichier en cliquant sur **File > Save**, nommez-le `iris_analysis.R`
- Tapez ce code :

```r
data(iris)
str(iris)
summary(iris)
```

- Enregistrez le fichier en cliquant sur **File > Save**
- Ouvrez le terminal R : cliquez sur **View** dans la barre de menu, puis sur **Command Palette**, tapez `R: Create R Terminal`, appuyez sur Entrée
- Sélectionnez le code et appuyez sur `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (Mac) pour l'exécuter
- Vous devriez voir la structure du jeu de données et les statistiques récapitulatives dans le terminal

## Étape 4 : Demander à Claude d'Ajouter un Graphique de Dispersion

- Cliquez sur l'icône **Claude** dans la barre latérale gauche pour ouvrir le panneau de discussion
- Dans la zone de discussion en bas, tapez :

```
Add code to iris_analysis.R to create a scatter plot of sepal length vs. width, colored by species. Use ggplot2.
```

- Appuyez sur Entrée pour envoyer
- Claude lit votre fichier et propose des modifications - vous verrez un diff montrant le nouveau code à ajouter
- Cliquez sur **Accept** pour appliquer les modifications
- Le code ggplot2 apparaît dans votre fichier
- Si vous n'avez pas ggplot2 installé, exécutez `install.packages("ggplot2")` dans le terminal R

## Étape 5 : Exécuter le Code Mis à Jour

- Sélectionnez tout le code dans `iris_analysis.R`
- Appuyez sur `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (Mac)
- Un graphique de dispersion apparaît dans une fenêtre graphique séparée
- Vous devriez voir des points colorés par espèce (setosa, versicolor, virginica)

## Étape 6 : Demander à Claude d'Affiner le Graphique

- Dans le panneau de discussion Claude, tapez :

```
Remove title. Change marker type by species. Change to the classic theme.
```

- Appuyez sur Entrée
- Claude affiche les modifications de code mises à jour
- Cliquez sur **Accept**
- Exécutez à nouveau le code mis à jour : sélectionnez tout et appuyez sur `Ctrl+Enter` / `Cmd+Enter`
- Le graphique s'affiche maintenant avec différentes formes de marqueurs par espèce, sans titre, et avec le thème classique

## Étape 7 : Demander à Claude une Analyse en Composantes Principales

- Dans le panneau de discussion Claude, tapez :

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- Appuyez sur Entrée
- Claude ajoute du code PCA à votre script
- Cliquez sur **Accept**
- Exécutez tout le code : sélectionnez tout et appuyez sur `Ctrl+Enter` / `Cmd+Enter`
- Un graphique PCA apparaît montrant les échantillons projetés sur PC1 et PC2, colorés par espèce

## Étape 8 : Demander à Claude de Réviser et Commenter

- Dans le panneau de discussion Claude, tapez :

```
Review the entire script for correctness. Add comments when necessary.
```

- Appuyez sur Entrée
- Claude révise le code et suggère des commentaires expliquant chaque section
- Cliquez sur **Accept**
- Votre script contient maintenant des commentaires clairs expliquant le chargement des données, la visualisation et l'analyse PCA

## Prochaines Étapes

- Demandez à Claude de créer un rapport R Markdown : "Create an R Markdown file for this analysis"
- Utilisez Claude pour déboguer les erreurs : "This code gives Error X, can you fix it?"
- Demandez des tests statistiques : "Add a t-test comparing sepal length between setosa and versicolor"
- Demandez à Claude d'optimiser le code : "Make this loop faster using vectorization"
- Obtenez de l'aide avec des fonctions inconnues : "Explain what dplyr::mutate does"

## Dépannage

- **L'extension Claude ne s'affiche pas** - Redémarrez VS Code après l'installation. Cliquez sur **View > Extensions** pour vérifier qu'elle est installée.
- **Erreur "Cannot read R file"** - Assurez-vous d'avoir enregistré le fichier avec l'extension `.R`. Claude a besoin de fichiers enregistrés pour les lire.
- **Échec de l'authentification** - Vérifiez que votre abonnement Claude Pro/Max est actif ou que votre clé API est valide. Consultez [Installation de Claude Code sur Mac](./Install_Claude_Code_MacOS) pour le dépannage de l'authentification.
- **ggplot2 introuvable** - Installez-le dans le terminal R : `install.packages("ggplot2")`. Attendez la fin de l'installation avant d'exécuter le code.
- **Les modifications de code ne s'appliquent pas** - Assurez-vous de cliquer sur **Accept** sur le diff. Si cela ne fonctionne pas, essayez de copier manuellement le code suggéré par Claude.

## Résumé du Flux de Travail

- **Extension Claude Code** fournit un assistant IA directement dans VS Code avec un panneau de discussion et des diffs en ligne
- **Raffinement itératif** - Commencez avec du code de base, demandez à Claude d'améliorer, testez immédiatement, puis affinez davantage
- **Conscience du contexte** - Claude lit vos fichiers R et comprend la structure de votre projet
- **Édition en ligne** - Les modifications proposées apparaissent sous forme de diffs dans vos fichiers réels, pas dans des réponses de discussion séparées
- **Restez dans le flux** - Pas besoin de basculer entre le navigateur et l'éditeur - tout se passe dans VS Code

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025.
