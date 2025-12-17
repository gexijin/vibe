[Accueil](../fr/)

# Premiers Pas avec VS Code

Vous souhaitez écrire du code, mais Notepad ou TextEdit vous semblent limités. Vous avez besoin d'un outil qui vous aide à coder plus rapidement - avec la coloration syntaxique, l'autocomplétion et des outils intégrés. **VS Code est comme un cahier intelligent pour le code** - il comprend ce que vous écrivez et vous aide tout au long du processus. [Visual Studio Code](https://code.visualstudio.com) est gratuit, fonctionne sur tous les systèmes d'exploitation et est utilisé par des millions de développeurs.

## Concepts Clés

- **Éditeur** - La zone principale où vous écrivez du code
- **Explorateur** - La barre latérale qui affiche vos fichiers et dossiers
- **Extensions** - Des modules complémentaires qui ajoutent de nouvelles fonctionnalités à VS Code
- **Terminal Intégré** - Une ligne de commande intégrée dans VS Code

## Ce Dont Vous Aurez Besoin

- Un ordinateur Windows, macOS ou Linux
- Une connexion Internet
- Environ 500 Mo d'espace disque
- 20 à 25 minutes

## Étape 1 : Télécharger et Installer VS Code

- Allez sur [code.visualstudio.com](https://code.visualstudio.com)
- Cliquez sur le bouton **Download** (il détecte automatiquement votre système d'exploitation)
- Exécutez le programme d'installation :
   - **Windows :** Double-cliquez sur le fichier `.exe`, cliquez sur **Next** à chaque invite
   - **Mac :** Ouvrez le fichier `.dmg`, faites glisser VS Code vers **Applications**
   - **Linux :** Suivez les instructions pour votre gestionnaire de paquets
- Lancez VS Code

Vous verrez un onglet de bienvenue avec des options pour commencer.

## Étape 2 : Découvrir l'Interface

VS Code comporte cinq zones principales :

- **Barre d'Activités** (bord gauche) - Icônes pour l'Explorateur, la Recherche, Git, les Extensions, etc.
- **Barre Latérale** - Affiche le contenu de l'activité sélectionnée (fichiers, résultats de recherche)
- **Éditeur** (centre) - L'endroit où vous écrivez du code
- **Panneau** (en bas) - Terminal, Problèmes, Sortie
- **Barre d'État** (bord inférieur) - Informations sur votre fichier et votre projet

Cliquez sur l'icône **Explorer** (en haut de la Barre d'Activités) pour voir le navigateur de fichiers.

## Étape 3 : Ouvrir un Dossier et Explorer

- Cliquez sur **File** → **Open Folder**
- Naviguez vers n'importe quel dossier existant sur votre ordinateur (par exemple, Documents)
- Cliquez sur **Open** (ou **Select Folder**)
- Si on vous demande « Do you trust the authors? », cliquez sur **Yes, I trust the authors**

La barre latérale Explorateur affiche maintenant les fichiers de votre dossier :

- Cliquez sur un dossier pour le développer
- Cliquez sur n'importe quel fichier pour l'ouvrir dans l'éditeur
- Cliquez sur l'icône **Search** dans la Barre d'Activités (loupe) pour rechercher dans tous les fichiers

## Étape 4 : Créer un Fichier Markdown

- Dans l'Explorateur, cliquez sur l'icône **New File** (page avec +)
- Nommez-le `README.md`
- Ajoutez ce contenu :

```
# My Project

This is a **demo project** for learning VS Code.

## Features
- Easy to edit
- Markdown formatting
- Live preview

## Next Steps
1. Add more content
2. Try other file types
3. Explore extensions
```
- Cliquez sur **File** → **Save** pour enregistrer

Markdown est un format de texte simple qui utilise des symboles comme `#` pour les titres, `**` pour le gras et `-` pour les listes. Il est largement utilisé pour la documentation et pour communiquer avec les LLM comme ChatGPT et Claude.

## Étape 5 : Installer l'Extension Markdown Preview

- Cliquez sur l'icône **Extensions** dans la Barre d'Activités (l'icône avec des carrés)
- Tapez `Markdown Preview Enhanced` dans la zone de recherche
- Trouvez **Markdown Preview Enhanced** dans les résultats
- Cliquez sur **Install**

## Étape 6 : Prévisualiser Votre Fichier Markdown

- Ouvrez `README.md` s'il n'est pas déjà ouvert
- Faites un clic droit dans l'éditeur et sélectionnez **Markdown Preview Enhanced: Open Preview to the Side**

Un panneau de prévisualisation s'ouvre affichant votre Markdown formaté - éditez à gauche, voyez les changements à droite en temps réel !

## Étape 7 : Utiliser le Terminal Intégré

- Cliquez sur **Terminal** → **New Terminal**
- Essayez ces commandes :

**Lister les fichiers :**
```
ls
```
(Sur Windows Command Prompt, utilisez `dir`)

**Afficher le répertoire de travail actuel :**
```
pwd
```
(Sur Windows Command Prompt, utilisez `cd`)

**Créer un nouveau dossier :**
```
mkdir notes
```

Vérifiez l'Explorateur - le dossier `notes` apparaît ! Le terminal s'exécute dans votre dossier de projet, donc les commandes affectent directement votre projet.

## Étape 8 : Utiliser les Agents IA dans VS Code (Optionnel)

VS Code inclut [GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat), un assistant IA qui peut expliquer, écrire et déboguer du code.

- Ouvrez le fichier `README.md` (ou tout autre fichier de votre projet)
- Cliquez sur **Chat** → **Open Chat** dans la barre de titre (ou appuyez sur `Ctrl+Alt+I` sur Windows/Linux, `Ctrl+Cmd+I` sur Mac)
- Si on vous le demande, connectez-vous avec votre **compte GitHub** (un forfait gratuit est disponible)
- Dans le panneau de discussion qui s'ouvre, tapez : « Explain this file »
- Appuyez sur **Enter**

GitHub Copilot analysera votre fichier et expliquera ce qu'il fait. Vous pouvez lui demander d'écrire du nouveau code, de corriger des bugs ou de répondre à des questions comme « How do I add more features? »

**Astuce :** Pour [l'édition en ligne](https://code.visualstudio.com/docs/copilot/copilot-chat), surlignez du code dans n'importe quel fichier et appuyez sur `Ctrl+I` (Windows/Linux) ou `Cmd+I` (Mac) pour demander à Copilot de modifier, corriger ou expliquer uniquement cette section.

## Comment Rouvrir Votre Projet

- Ouvrez VS Code depuis le menu Démarrer (Windows), Spotlight (Mac) ou Applications (Linux)
- Cliquez sur **File** → **Open Recent** → sélectionnez votre dossier
- Ou cliquez sur **File** → **Open Folder** et naviguez vers celui-ci

## Dépannage

- **La prévisualisation ne s'affiche pas :** Assurez-vous que l'extension Markdown Preview Enhanced est installée et que vous avez un fichier `.md` ouvert
- **Le terminal affiche le mauvais répertoire :** Cliquez sur l'icône de corbeille dans le panneau du terminal, puis cliquez sur **Terminal** → **New Terminal**
- **Le menu Chat n'est pas visible :** GitHub Copilot Chat doit peut-être être installé - cliquez sur l'icône **Extensions**, recherchez « GitHub Copilot Chat » et installez-le
- **Les extensions ne fonctionnent pas :** Cliquez sur **View** → **Command Palette**, tapez « reload window » et sélectionnez **Developer: Reload Window**

## Le Workflow Complet

1. Ouvrez un dossier dans VS Code
2. Créez/éditez des fichiers
3. Utilisez des extensions pour prévisualiser
4. Utilisez le terminal pour les commandes
5. Utilisez l'IA pour comprendre et améliorer le code
6. Enregistrez et répétez

## Prochaines Étapes

- **Essayez d'autres types de fichiers :** Créez des fichiers `.html`, `.css`, `.js` ou `.py` et découvrez la coloration syntaxique de VS Code
- **Explorez les fonctionnalités IA :** Demandez à l'IA d'écrire du code, de corriger des bugs ou de suggérer des améliorations pour vos projets
- **Installez plus d'extensions :** Essayez « Prettier » pour le formatage automatique ou « GitLens » pour les fonctionnalités Git
- **Apprenez les raccourcis :** Cliquez sur **Help** → **Keyboard Shortcuts Reference** pour accélérer votre workflow

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 7 décembre 2025.
