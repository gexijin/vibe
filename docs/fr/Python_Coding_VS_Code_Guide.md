[Accueil](./)

# Programmation Python dans VS Code

Vous souhaitez écrire du code Python mais vous n'êtes pas sûr de l'éditeur à utiliser, ou vous recherchez quelque chose de plus léger que PyCharm. Considérez VS Code comme un couteau suisse : il gère Python, R, JavaScript et de nombreux autres langages dans un seul éditeur léger. Ce tutoriel vous montre comment configurer Python dans VS Code avec des fonctionnalités intelligentes telles que la complétion de code, le débogage interactif et même des applications web.

## Concepts Clés

- **[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - Extension VS Code de Microsoft qui fournit la coloration syntaxique, le débogage, l'exécution de code et la prise en charge des notebooks Jupyter
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - Serveur de langage qui active IntelliSense rapide, la vérification de type et les imports automatiques pour Python
- **[Virtual Environment](https://docs.python.org/3/library/venv.html)** - Environnement Python isolé pour gérer les packages spécifiques au projet sans affecter le Python système
- **[Streamlit](https://streamlit.io/)** - Bibliothèque Python pour créer des applications web interactives avec de simples scripts Python

## Ce Dont Vous Aurez Besoin

- Avoir terminé [VS Code Basics](./VS_Code_Getting_Started)
- Connexion Internet pour télécharger Python et les packages
- 15 à 20 minutes

## Étape 1 : Installez Python

Vous avez besoin de Python 3.8 ou supérieur pour une meilleure compatibilité avec les packages modernes.

- **Windows** :
  - Téléchargez la dernière version de Python depuis [python.org](https://www.python.org/downloads/)
  - Exécutez le programme d'installation
  - **Cochez la case « Add python.exe to PATH »** avant de cliquer sur Install Now
  - Notez l'emplacement d'installation (généralement `C:\Users\YourName\AppData\Local\Programs\Python\Python312`)

- **macOS** :
  - Téléchargez depuis [python.org](https://www.python.org/downloads/) et exécutez le programme d'installation
  - Ou utilisez Homebrew : ouvrez Terminal et tapez `brew install python`
  - Chemin Homebrew : `/opt/homebrew/bin/python3` (Apple Silicon) ou `/usr/local/bin/python3` (Intel)

- **Linux** :
  - Python est généralement préinstallé. Vérifiez la version avec `python3 --version`
  - Si nécessaire, installez via le gestionnaire de packages : `sudo apt install python3 python3-pip python3-venv` (Ubuntu/Debian)

Vérifiez l'installation en ouvrant un terminal et en tapant `python3 --version` ou `python --version`.

## Étape 2 : Installez les Extensions Python dans VS Code

- Ouvrez VS Code
- Cliquez sur l'icône **Extensions** dans la barre latérale gauche (ou cliquez sur **View > Extensions**)
- Recherchez `ms-python.python` et cliquez sur **Install** sur l'extension Python de Microsoft
- Pylance devrait s'installer automatiquement avec l'extension Python. Sinon, recherchez `ms-python.vscode-pylance` et installez-la

L'extension Python inclut la prise en charge du débogage, d'IntelliSense, du formatage de code et des notebooks Jupyter.

## Étape 3 : Créez Votre Projet Python

- Créez un nouveau dossier sur votre ordinateur (par exemple, `my-python-project`)
- Dans VS Code, cliquez sur **File > Open Folder** et sélectionnez votre nouveau dossier
- Cliquez sur **File > New File** dans le menu supérieur
- Enregistrez le fichier sous `analysis.py` en cliquant sur **File > Save**

## Étape 4 : Sélectionnez l'Interpréteur Python

VS Code doit savoir quelle installation Python utiliser.

- Cliquez sur **View** dans la barre de menu, puis sur **Command Palette**
- Tapez `Python: Select Interpreter` et sélectionnez-le
- Choisissez la version Python que vous avez installée (par exemple, `Python 3.12.x` ou similaire)
- L'interpréteur sélectionné apparaît dans le coin inférieur droit de VS Code

Si vous ne voyez pas votre installation Python, cliquez sur **Enter interpreter path** et naviguez vers l'emplacement où Python est installé.

## Étape 5 : Créez un Environnement Virtuel

Les environnements virtuels gardent les dépendances de votre projet isolées.

- Cliquez sur **View** dans la barre de menu, puis sur **Command Palette**
- Tapez `Python: Create Environment` et sélectionnez-le
- Choisissez **Venv** (environnement virtuel intégré)
- Sélectionnez votre interpréteur Python dans la liste
- Attendez que VS Code crée l'environnement (vous verrez apparaître un dossier `.venv`)
- VS Code activera automatiquement cet environnement pour votre projet

Vous verrez `(.venv)` dans votre invite de terminal lorsque l'environnement est actif.

## Étape 6 : Installez les Packages Requis

- Ouvrez un nouveau terminal dans VS Code en cliquant sur **View > Terminal**
- Le terminal devrait afficher `(.venv)` indiquant que votre environnement virtuel est actif
- Installez les packages en tapant ces commandes :

```bash
pip install pandas matplotlib streamlit
```

- Attendez que l'installation se termine (peut prendre 1 à 2 minutes)

Si `(.venv)` n'apparaît pas, l'environnement n'est pas actif. Cliquez sur **View > Command Palette**, exécutez `Python: Select Interpreter`, puis choisissez l'interpréteur avec `('.venv': venv)` à côté.

## Étape 7 : Écrivez Votre Premier Script Python

Tapez ce code dans `analysis.py` :

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# View the first few rows
print(iris.head())

# Generate summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- Enregistrez le fichier en cliquant sur **File > Save**

## Étape 8 : Exécutez du Code Python de Manière Interactive

- Avec `analysis.py` ouvert, cliquez sur le bouton **▶ Run Python File** dans le coin supérieur droit
- Ou faites un clic droit dans l'éditeur et sélectionnez **Run Python File in Terminal**
- Regardez la sortie apparaître dans le panneau de terminal
- Une fenêtre d'histogramme apparaîtra montrant votre graphique
- Vous pouvez également sélectionner des lignes spécifiques et appuyer sur `Shift+Enter` pour exécuter uniquement ces lignes dans une session Python interactive

## Étape 9 : Créez une Application Streamlit Simple

- Créez un nouveau fichier : **File > New File**
- Enregistrez-le sous `app.py`
- Tapez ce code :

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# Sidebar slider
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# Load data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Create histogram
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# Display in Streamlit
st.pyplot(fig)
```

- Enregistrez le fichier
- Ouvrez le terminal et exécutez :

```bash
streamlit run app.py
```

- L'application s'ouvre dans votre navigateur (généralement à `http://localhost:8501`)
- Déplacez le curseur dans la barre latérale et regardez l'histogramme se mettre à jour instantanément
- Appuyez sur `Ctrl+C` dans le terminal pour arrêter l'application

## Étape 10 : Utilisez la Complétion de Code et IntelliSense

- Dans `analysis.py`, commencez à taper `iris.` sur une nouvelle ligne
- Un menu déroulant apparaît avec toutes les méthodes et attributs disponibles
- Tapez `iris.gr` et regardez-le suggérer `groupby()`
- Passez votre souris sur `pd.read_csv` dans votre code existant
- Une fenêtre contextuelle affiche la signature de la fonction, les paramètres et la documentation
- Essayez de taper `import ` et regardez VS Code suggérer des noms de packages
- Lorsque vous tapez un appel de fonction, IntelliSense affiche des indications sur les paramètres

## Étape 11 : Essayez le Débogage

- Dans `analysis.py`, cliquez à gauche du numéro de ligne 8 (la ligne `print(iris.head())`) pour définir un point d'arrêt (un point rouge apparaît)
- Cliquez sur **Run** dans la barre de menu, puis sur **Start Debugging**
- Sélectionnez **Python File** lorsque vous y êtes invité
- L'exécution du code s'arrête au point d'arrêt
- Utilisez la barre d'outils de débogage pour parcourir le code, inspecter les variables et voir la pile d'appels
- Cliquez sur **Run > Continue** pour reprendre l'exécution

## Prochaines Étapes

- Explorez [pandas](https://pandas.pydata.org/) pour la manipulation et l'analyse de données
- Apprenez les [notebooks Jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) dans VS Code pour la science des données interactive
- Essayez [Flask](https://flask.palletsprojects.com/) ou [FastAPI](https://fastapi.tiangolo.com/) pour créer des API web
- Installez [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) pour le formatage automatique du code
- Utilisez [pytest](https://docs.pytest.org/) pour écrire et exécuter des tests

## Dépannage

- **« Python is not recognized » dans le terminal** : Python n'est pas dans votre PATH système. Sur Windows, réinstallez Python et cochez « Add python.exe to PATH ». Sur Mac/Linux, utilisez `python3` au lieu de `python`. Redémarrez VS Code après la correction.

- **Aucun interpréteur trouvé** : Cliquez sur le sélecteur d'interpréteur dans le coin inférieur droit de VS Code, ou cliquez sur **View > Command Palette** et exécutez `Python: Select Interpreter`. Si votre installation Python n'apparaît pas, sélectionnez **Enter interpreter path** et naviguez vers votre exécutable Python.

- **L'environnement virtuel ne s'active pas** : VS Code devrait l'activer automatiquement lorsque vous ouvrez un terminal. Sinon, activez-le manuellement : Windows : `.venv\Scripts\activate`, Mac/Linux : `source .venv/bin/activate`. Vérifiez en voyant `(.venv)` dans votre invite de terminal.

- **IntelliSense ne fonctionne pas** : Assurez-vous que Pylance est installé et activé. Vérifiez que le coin inférieur droit affiche votre interpréteur sélectionné. Attendez 10 à 20 secondes après l'ouverture d'un fichier pour que Pylance s'initialise. Redémarrez VS Code si les problèmes persistent.

- **pip install échoue** : Assurez-vous que votre environnement virtuel est activé (recherchez `(.venv)` dans le terminal). Sur Linux, vous devrez peut-être installer d'abord `python3-venv`. Sur Windows, vérifiez que l'antivirus ne bloque pas pip.

- **L'application Streamlit ne s'exécute pas** : Assurez-vous que streamlit est installé dans votre environnement virtuel (`pip list | grep streamlit`). Vérifiez le terminal pour les messages d'erreur. Assurez-vous qu'aucune autre application n'utilise le port 8501.

## Résumé du Flux de Travail

VS Code fournit un environnement moderne et léger pour le développement Python avec ces avantages :

- **Environnement unifié** : Codez en Python, R, JavaScript et plus dans un seul éditeur
- **IntelliSense puissant** : Complétions intelligentes, vérification de type et imports automatiques via Pylance
- **Débogage intégré** : Définissez des points d'arrêt, inspectez les variables et parcourez le code
- **Prise en charge de Jupyter** : Exécutez des notebooks directement dans VS Code sans applications séparées
- **Contrôle de version** : Intégration Git intégrée pour suivre les modifications
- **Écosystème d'extensions** : Des milliers d'extensions pour les tests, le formatage, le linting et plus encore

---

Created by [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) on December 7, 2025.
