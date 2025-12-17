[Accueil](./)

# Programmation Python dans VS Code via un Conteneur Docker

Avez-vous déjà essayé de partager votre code Python avec un collègue, pour finalement passer des heures à déboguer des problèmes du type « mais ça marche sur ma machine » ? Les conteneurs Docker sont comme des conteneurs d'expédition pour le code : ils emballent votre environnement Python, vos bibliothèques et vos dépendances dans une boîte scellée qui fonctionne de la même manière partout. De plus, vous avez accès à des dizaines de milliers d'images pré-construites sur [Docker Hub](https://hub.docker.com/), où les développeurs de logiciels publient des environnements prêts à l'emploi, vous évitant les difficultés de l'installation manuelle de logiciels. Ce tutoriel vous montre comment exécuter Python dans un environnement isolé et reproductible en utilisant VS Code et Docker Desktop.

## Concepts Clés

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - Application qui exécute des conteneurs sur votre ordinateur, en gérant des environnements isolés
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - Fonctionnalité de VS Code qui vous permet de coder à l'intérieur d'un conteneur Docker avec un support complet de l'IDE
- **Isolation du Conteneur** - Votre code s'exécute dans un environnement Linux séparé qui ne voit que votre dossier de projet, pas votre ordinateur entier
- **[Images Officielles Python](https://hub.docker.com/_/python)** - Images Docker pré-construites avec Python et les outils essentiels pré-installés

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Python Coding in VS Code](./Python_Coding_VS_Code_Guide)
- 20-25 minutes

## Étape 1 : Installez Docker Desktop

- Visitez la [page de téléchargement de Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Cliquez sur **Download for Windows** (ou Mac/Linux selon votre système)
- Exécutez le programme d'installation et suivez l'assistant d'installation
- Lorsqu'on vous le demande, activez WSL 2 (utilisateurs Windows) ou acceptez les paramètres par défaut
- Après l'installation, lancez Docker Desktop
- Attendez que le moteur Docker démarre (vous verrez un indicateur d'état vert en bas à gauche)

## Étape 2 : Installez l'Extension Dev Containers

- Ouvrez VS Code
- Cliquez sur l'icône **Extensions** dans la barre latérale gauche (ou cliquez sur **View > Extensions**)
- Tapez `dev containers` dans la zone de recherche
- Trouvez **Dev Containers** par Microsoft
- Cliquez sur **Install**

## Étape 3 : Créez un Dossier de Projet Python

- Créez un nouveau dossier sur votre ordinateur nommé `python-docker-demo`
- À l'intérieur, créez un sous-dossier nommé `.devcontainer`
- À l'intérieur, créez un sous-dossier nommé `python`
- Votre structure devrait ressembler à : `python-docker-demo/.devcontainer/` et `python-docker-demo/python/`

## Étape 4 : Créez le Dockerfile

- Dans VS Code, cliquez sur **File > Open Folder**
- Naviguez vers le dossier `python-docker-demo` que vous venez de créer
- Cliquez sur **Select Folder**
- Dans la barre latérale Explorer, faites un clic droit sur le dossier `.devcontainer`
- Cliquez sur **New File**
- Nommez-le `Dockerfile`
- Collez le contenu suivant :

```dockerfile
# Choose the official Python slim image
FROM python:3.12-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Install Python packages for data science and web apps
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Streamlit port
EXPOSE 8501
```

- Cliquez sur **File > Save**

## Étape 5 : Créez la Configuration Dev Container

- Dans le dossier `.devcontainer`, créez un nouveau fichier nommé `devcontainer.json`
- Collez le contenu suivant :

```json
{
  "name": "Python in Docker",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy"
      ]
    }
  },
  "forwardPorts": [8501],
  "postCreateCommand": "python3 --version"
}
```

- Cliquez sur **File > Save**

## Étape 6 : Créez un Script d'Analyse de Données Python

- Dans le dossier `python`, créez un nouveau fichier nommé `iris_analysis.py`
- Collez le contenu suivant :

```python
# Simple data analysis using the iris dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Sepal Length')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Sepal Width')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Iris Sepal Measurements')
plt.legend()
plt.show()
```

- Cliquez sur **File > Save**

## Étape 7 : Créez une Application Web Streamlit

- Dans le dossier `python`, créez un nouveau fichier nommé `app.py`
- Collez le contenu suivant :

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geyser Data")

# Slider for number of bins
bins = st.slider("Number of bins:", min_value=5, max_value=50, value=30)

# Generate sample data (simulating Old Faithful eruption durations)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Create histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Eruption Duration (minutes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram with {bins} bins')

st.pyplot(fig)
```

- Cliquez sur **File > Save**

## Étape 8 : Rouvrez dans le Conteneur

- Cliquez sur l'icône verte dans le coin inférieur gauche de VS Code
- Sélectionnez **Reopen in Container** dans le menu
- VS Code va construire le conteneur (cela prend 5-10 minutes la première fois)
- Vous verrez une notification de progression affichant les étapes de construction
- Une fois terminé, l'icône verte affichera **Dev Container: Python in Docker**

## Étape 9 : Comprenez l'Environnement du Conteneur

Maintenant, vous codez à l'intérieur d'un conteneur Linux. Explorons ce que cela signifie.

- Cliquez sur **Terminal > New Terminal** pour ouvrir un terminal à l'intérieur du conteneur
- Vérifiez votre emplacement actuel :

```bash
pwd
```

Vous verrez `/workspaces/python-docker-demo` - c'est votre dossier de projet à l'intérieur du conteneur.

- Listez les fichiers :

```bash
ls
```

Vous verrez les dossiers que vous avez créés : `.devcontainer/`, `python/`, etc.

- Essayez de remonter d'un répertoire :

```bash
cd ..
ls
```

Vous ne verrez que `python-docker-demo/` - le conteneur est isolé. Vous ne pouvez pas accéder aux autres dossiers de votre ordinateur, Bureau ou Documents. Cette isolation garantit que votre environnement Python est propre et reproductible.

- Retournez au dossier du projet :

```bash
cd python-docker-demo
```

## Étape 10 : Exécutez du Code Python Ligne par Ligne

Le conteneur a Python pré-installé avec des packages de science des données. Exécutons le script d'analyse.

- Dans VS Code Explorer, naviguez vers `python/iris_analysis.py`
- Cliquez pour ouvrir le fichier
- Sélectionnez la première ligne : `import pandas as pd`
- Appuyez sur `Shift+Enter` pour l'exécuter dans un terminal Python interactif
- Un terminal Python s'ouvre en bas
- Continuez à exécuter chaque ligne ou bloc un à la fois avec `Shift+Enter`
- Lorsque vous exécutez `print(df.head())`, vous verrez les 5 premières lignes dans le terminal
- Lorsque vous exécutez `print(df.describe())`, vous verrez des résumés statistiques
- Lorsque vous exécutez le code de l'histogramme, une fenêtre de graphique s'ouvrira montrant la visualisation

## Étape 11 : Exécutez l'Application Streamlit

Le projet inclut une application Streamlit de démonstration qui crée un histogramme interactif.

- Dans VS Code Explorer, naviguez vers `python/app.py`
- Cliquez pour ouvrir le fichier
- Ouvrez un nouveau terminal (**Terminal > New Terminal**)
- Exécutez l'application :

```bash
cd python
streamlit run app.py
```

- L'application démarrera et affichera une URL : `http://localhost:8501`
- Une notification apparaît : **Open in Browser**
- Cliquez sur **Open in Browser**
- L'application Streamlit s'ouvre dans votre navigateur web
- Déplacez le curseur pour changer les intervalles de l'histogramme - le graphique se met à jour en temps réel

## Étape 12 : Effectuez un Changement Simple

Modifions l'application pour voir comment fonctionne le développement.

- Gardez l'application en cours d'exécution
- Dans VS Code, éditez `python/app.py`
- Trouvez la ligne 6 : `st.title("Old Faithful Geyser Data")`
- Changez-la en :

```python
st.title("My First Python Docker App")
```

- Cliquez sur **File > Save**
- Retournez à votre navigateur
- Cliquez sur **Always rerun** dans le coin supérieur droit
- Le titre affiche maintenant votre texte personnalisé

## Étape 13 : Comprendre le Dockerfile (Optionnel)

- Dans VS Code Explorer, naviguez vers `.devcontainer/Dockerfile`
- Cliquez pour ouvrir le fichier
- Vous verrez la configuration complète

**Parties clés :**

- `FROM python:3.12-slim` - Image de base officielle Python 3.12 (légère basée sur Debian)
- `RUN apt-get install` - Bibliothèques système Linux pour construire des packages Python
- `RUN pip install --no-cache-dir ...` - Installe de manière permanente les packages Python
- `RUN curl... && apt-get install -y nodejs` - Installe Node.js, requis pour exécuter Claude Code
- `RUN npm install -g @anthropic-ai/claude-code` - Installe Claude Code globalement pour l'assistance IA
- `EXPOSE 8501` - Ouvre le port 8501 pour les applications Streamlit

**Autres images Python que vous pouvez utiliser :**

- `python:3.12` - Image Python complète avec plus d'outils (taille plus grande)
- `python:3.12-slim` - Image légère avec Python et pip (celle que nous utilisons)
- `python:3.12-alpine` - Image minimale basée sur Alpine Linux (taille la plus petite)
- `jupyter/datascience-notebook` - Jupyter pré-configuré avec des bibliothèques de science des données

Après avoir changé l'image de base, reconstruisez le conteneur pour appliquer les modifications.

## Étape 14 : Installez des Packages Python dans l'Image Docker (Optionnel)

Les packages installés via pip dans le terminal (`pip install package`) sont temporaires et disparaissent lorsque vous reconstruisez le conteneur. Pour rendre les packages permanents, ajoutez-les au Dockerfile.

- Dans VS Code Explorer, naviguez vers `.devcontainer/Dockerfile`
- Cliquez pour ouvrir le fichier
- Trouvez la ligne 9 : `RUN pip install --no-cache-dir ...`
- Ajoutez `scikit-learn` à la liste :

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- Cliquez sur **File > Save**
- Cliquez sur l'icône verte dans le coin inférieur gauche
- Sélectionnez **Rebuild Container** dans le menu
- VS Code va reconstruire le conteneur avec votre nouveau package (cela prend 2-5 minutes)
- Pour vérifier, ouvrez un terminal Python et tapez :

```python
import sklearn
print(sklearn.__version__)
```

Si cela affiche la version sans erreurs, le package est installé de manière permanente.

## Prochaines Étapes

- **Créez un nouveau script Python** - Créez un nouveau fichier `.py` dans le dossier `python/`, écrivez du code d'analyse de données en utilisant des ensembles de données intégrés ou chargez vos propres fichiers CSV
- **Installez des packages Python** - Ajoutez les packages dont vous avez besoin en éditant le Dockerfile (ligne 9) et en reconstruisant le conteneur
- **Explorez la science des données** - Essayez la manipulation de données avec pandas et la visualisation avec matplotlib ou seaborn
- **Construisez des applications web** - Créez des tableaux de bord interactifs avec Streamlit ou Flask

## Dépannage

- **Docker Desktop ne fonctionne pas** - Ouvrez Docker Desktop et attendez l'indicateur d'état vert avant de rouvrir le conteneur
- **La construction du conteneur échoue** - Vérifiez votre connexion Internet ; la première construction télécharge des images et des packages. Cliquez sur **Rebuild Container** pour réessayer
- **Le port 8501 est déjà utilisé** - Arrêtez les autres applications utilisant ce port, ou changez le port dans le Dockerfile et `devcontainer.json`

## Vue d'Ensemble du Flux de Travail

Cette configuration vous donne un environnement de développement Python professionnel :

- **VS Code** fournit l'éditeur de code avec la coloration syntaxique, IntelliSense et le débogage
- **Le conteneur Docker** exécute un environnement Linux isolé avec Python et toutes les dépendances
- **L'image officielle Python** (`python:3.12-slim`) inclut Python, pip et les outils essentiels
- **La configuration Dev Container** (`.devcontainer/`) installe automatiquement les extensions VS Code pour le débogage Python et le support du langage
- **Le transfert de port** vous permet d'accéder aux applications web (Streamlit, Flask) s'exécutant à l'intérieur du conteneur depuis votre navigateur

## Flux de Travail Quotidien

Une fois que tout est configuré, voici votre routine quotidienne :

1. **Démarrez Docker Desktop** - Ouvrez l'application et attendez l'indicateur d'état vert (Docker doit être en cours d'exécution)
2. **Ouvrez VS Code** - Lancez VS Code et ouvrez votre dossier de projet
3. **Rouvrez dans le Conteneur** - Si vous n'êtes pas déjà dans le conteneur, cliquez sur l'icône verte (en bas à gauche) et sélectionnez **Reopen in Container**
4. **Écrivez et exécutez du code** - Éditez les fichiers `.py`, exécutez ligne par ligne avec `Shift+Enter`, ou exécutez des applications avec `streamlit run app.py`
5. **Enregistrez votre travail** - Vos fichiers de code (`.py`, `.ipynb`) sont enregistrés sur votre ordinateur et persistent entre les sessions
6. **Validez et poussez** - Utilisez GitHub Desktop pour valider vos modifications et pousser vers le dépôt

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 7 décembre 2025.
