[Accueil](./)

# Utiliser Claude Code pour Python dans VS Code sur Mac

Vous avez configuré Python dans VS Code et pouvez écrire du code manuellement. Maintenant, vous souhaitez que l'IA vous aide à écrire, améliorer et déboguer votre code Python pendant que vous vous concentrez sur l'analyse. Considérez Claude Code comme un partenaire de codage qui vit à l'intérieur de VS Code - vous décrivez ce que vous voulez, et il écrit ou améliore le code pendant que vous restez dans la même fenêtre.

## Concepts Clés

- **[Extension Claude Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)** - Extension VS Code qui intègre l'assistant IA Claude directement dans votre éditeur avec des modifications de code en ligne
- **Panneau de Chat** - Panneau latéral dans VS Code où vous conversez avec Claude à propos de votre code
- **Modifications en Ligne** - Les modifications de code suggérées par Claude apparaissent directement dans vos fichiers avec des différences que vous pouvez accepter ou rejeter

## Ce Dont Vous Aurez Besoin

- Terminé le tutoriel [Python dans VS Code](./Python_Coding_VS_Code_Guide) - Python doit fonctionner dans VS Code
- Terminé le tutoriel [Installation de Claude Code sur Mac](./Install_Claude_Code_MacOS) - Claude Code CLI doit être installé
- Abonnement Claude Pro/Max ou clé API Anthropic
- 20-30 minutes

## Étape 1 : Ouvrir VS Code et Créer un Projet Python

- Ouvrez **Visual Studio Code**
- Cliquez sur **File** dans la barre de menu, puis sur **Open Folder**
- Naviguez vers votre dossier **Documents**
- Cliquez sur **New Folder** en bas de la boîte de dialogue
- Nommez le dossier `claude_python_test`
- Cliquez sur **Open** pour ouvrir le nouveau dossier
- Si on vous demande "Do you trust the authors?", cliquez sur **Yes, I trust the authors**

## Étape 2 : Installer et Se Connecter à l'Extension Claude Code

- Cliquez sur l'icône **Extensions** dans la barre latérale gauche (icône de quatre carrés)
- Dans la zone de recherche, tapez `Claude Code`
- Trouvez **Claude Code** par Anthropic et cliquez sur **Install**
- Après l'installation, une icône Claude (étincelle) apparaît dans la barre latérale gauche
- Cliquez sur l'icône Claude pour ouvrir le panneau de chat
- Cliquez sur **Sign in to Claude Code** dans le panneau de chat
- Choisissez votre méthode d'authentification :
  - **Utilisateurs Claude Pro/Max** : Cliquez sur **Sign in with Claude.ai**, autorisez dans le navigateur, et copiez le code dans VS Code
  - **Utilisateurs de clé API** : Cliquez sur **Use API Key** et collez votre clé API Anthropic
- Pour les étapes d'authentification détaillées, consultez le guide [Installation de Claude Code sur Mac](./Install_Claude_Code_MacOS) (Étape 5)
- Une fois connecté, vous verrez "Ready to help" dans le panneau de chat

## Étape 3 : Créer un Script Python Initial Manuellement

- Cliquez sur **File > New File** dans la barre de menu
- Cliquez sur **Select a language** et tapez `Python`, puis sélectionnez **Python**
- Enregistrez le fichier en cliquant sur **File > Save**, nommez-le `iris_analysis.py`
- Tapez ce code :

```python
from sklearn import datasets
import pandas as pd

# Load iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

# Display structure
print(iris_df.info())
print("\nSummary statistics:")
print(iris_df.describe())
```

- Enregistrez le fichier en cliquant sur **File > Save**
- Ouvrez le terminal Python : cliquez sur **View** dans la barre de menu, puis sur **Terminal**
- Dans le terminal, exécutez : `python iris_analysis.py`
- Vous devriez voir la structure du jeu de données et les statistiques récapitulatives dans le terminal

## Étape 4 : Demander à Claude d'Ajouter un Graphique de Dispersion

- Cliquez sur l'icône **Claude** dans la barre latérale gauche pour ouvrir le panneau de chat
- Dans la zone de chat en bas, tapez :

```
Add code to iris_analysis.py to create a scatter plot of sepal length vs. width, colored by species. Use seaborn.
```

- Appuyez sur Entrée pour envoyer
- Claude lit votre fichier et propose des modifications - vous verrez une différence montrant le nouveau code à ajouter
- Cliquez sur **Accept** pour appliquer les modifications
- Le code seaborn/matplotlib apparaît dans votre fichier
- Si vous n'avez pas les packages requis, exécutez dans le terminal :
  ```
  pip install seaborn matplotlib scikit-learn pandas
  ```

## Étape 5 : Exécuter le Code Mis à Jour

- Dans le terminal, exécutez : `python iris_analysis.py`
- Une fenêtre de graphique de dispersion apparaît
- Vous devriez voir des points colorés par espèce (setosa, versicolor, virginica)
- Fermez la fenêtre du graphique pour continuer

## Étape 6 : Demander à Claude d'Affiner le Graphique

- Dans le panneau de chat Claude, tapez :

```
Remove title. Change marker type by species. Change to the whitegrid style.
```

- Appuyez sur Entrée
- Claude montre les modifications de code mises à jour
- Cliquez sur **Accept**
- Exécutez à nouveau le code mis à jour : `python iris_analysis.py` dans le terminal
- Le graphique s'affiche maintenant avec différentes formes de marqueurs par espèce, sans titre, et dans le style whitegrid
- Fermez la fenêtre du graphique pour continuer

## Étape 7 : Demander à Claude une Analyse PCA

- Dans le panneau de chat Claude, tapez :

```
Add code to perform PCA on the numeric variables and plot the samples using the first two principal components.
```

- Appuyez sur Entrée
- Claude ajoute du code PCA à votre script
- Cliquez sur **Accept**
- Exécutez le code : `python iris_analysis.py` dans le terminal
- Un graphique PCA apparaît montrant les échantillons projetés sur PC1 et PC2, colorés par espèce
- Fermez la fenêtre du graphique lorsque vous avez terminé

## Étape 8 : Demander à Claude de Réviser et Commenter

- Dans le panneau de chat Claude, tapez :

```
Review the entire script for correctness. Add comments when necessary.
```

- Appuyez sur Entrée
- Claude révise le code et suggère des commentaires expliquant chaque section
- Cliquez sur **Accept**
- Votre script contient maintenant des commentaires clairs expliquant le chargement des données, la visualisation et l'analyse PCA

## Prochaines Étapes

- Demandez à Claude de créer un notebook Jupyter : "Convert this to a Jupyter notebook"
- Utilisez Claude pour déboguer les erreurs : "This code gives Error X, can you fix it?"
- Demandez des tests statistiques : "Add a t-test comparing sepal length between setosa and versicolor"
- Demandez à Claude d'optimiser le code : "Make this code more efficient using numpy vectorization"
- Obtenez de l'aide sur les fonctions inconnues : "Explain what pandas.groupby does"

## Dépannage

- **L'extension Claude ne s'affiche pas** - Redémarrez VS Code après l'installation. Cliquez sur **View > Extensions** pour vérifier qu'elle est installée.
- **Erreur "Cannot read Python file"** - Assurez-vous d'avoir enregistré le fichier avec l'extension `.py`. Claude a besoin de fichiers enregistrés pour les lire.
- **L'authentification a échoué** - Vérifiez que votre abonnement Claude Pro/Max est actif ou que votre clé API est valide. Consultez [Installation de Claude Code sur Mac](./Install_Claude_Code_MacOS) pour le dépannage de l'authentification.
- **Erreurs de package introuvable** - Installez les packages requis dans le terminal : `pip install seaborn matplotlib scikit-learn pandas`. Attendez que l'installation soit terminée avant d'exécuter le code.
- **Les modifications de code ne s'appliquent pas** - Assurez-vous de cliquer sur **Accept** sur la différence. Si cela ne fonctionne pas, essayez de copier manuellement le code suggéré par Claude.
- **Le graphique ne s'affiche pas** - Assurez-vous d'avoir un affichage. Sur certains systèmes, vous devrez peut-être ajouter `plt.show()` à la fin ou utiliser `%matplotlib inline` dans Jupyter.

## Résumé du Flux de Travail

- **Extension Claude Code** fournit un assistant IA directement dans VS Code avec un panneau de chat et des différences en ligne
- **Raffinement itératif** - Commencez avec du code de base, demandez à Claude d'améliorer, testez immédiatement, puis affinez davantage
- **Conscience du contexte** - Claude lit vos fichiers Python et comprend la structure de votre projet
- **Édition en ligne** - Les modifications proposées apparaissent sous forme de différences dans vos fichiers réels, pas dans des réponses de chat séparées
- **Restez dans le flux** - Pas de basculement entre le navigateur et l'éditeur - tout se passe dans VS Code

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025.
