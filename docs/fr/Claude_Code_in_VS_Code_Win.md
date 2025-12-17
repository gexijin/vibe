[Accueil](./)

# Configurer VS Code pour Claude Code sur WSL

Vous avez installé WSL et Claude Code sur votre machine Windows - vous souhaitez maintenant un éditeur visuel pour travailler avec votre code. VS Code établit le lien entre Windows et votre environnement Linux, vous permettant d'éditer des fichiers visuellement tout en exécutant Claude Code dans le terminal intégré. Considérez VS Code comme une fenêtre ouverte sur votre monde Linux.

## Concepts Clés

- **VS Code** - Un éditeur de code gratuit de Microsoft qui s'exécute sur Windows mais peut se connecter à WSL
- **Extension WSL** - Connecte VS Code à votre environnement Linux afin que vous puissiez exécuter des outils Linux comme Claude Code
- **Terminal Intégré** - Un panneau de terminal à l'intérieur de VS Code qui s'exécute dans votre environnement WSL (Linux)
- **/mnt/c/** - Comment WSL accède à vos fichiers Windows (par exemple, `/mnt/c/Users/...` = `C:\Users\...`)

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Installer Claude Code sur Windows](./Install_CLAUDE_Code_Win)
- Avoir terminé [Les Bases de VS Code](./VS_Code_Getting_Started)
- 10-15 minutes

## Étape 1 : Créer un Dossier de Projet

- Ouvrez **l'Explorateur de fichiers** (cliquez sur l'icône de dossier dans votre barre des tâches)
- Naviguez vers **Documents**
- Faites un clic droit dans l'espace vide, sélectionnez **Nouveau > Dossier**
- Nommez le dossier `test_claude`

## Étape 2 : Démarrer VS Code

- Cliquez sur le **bouton Démarrer de Windows** (coin inférieur gauche de votre écran)
- Tapez `Visual Studio Code` ou `VS Code` dans la zone de recherche
- Cliquez sur **Visual Studio Code** lorsqu'il apparaît dans les résultats de recherche
- VS Code s'ouvre avec un onglet de bienvenue - vous pouvez fermer cet onglet


## Étape 3 : Installer l'Extension WSL

- Dans VS Code, cliquez sur l'icône **Extensions** dans la barre latérale gauche (elle ressemble à quatre carrés)
- Tapez `WSL` dans la zone de recherche
- Trouvez **WSL** par Microsoft (ce devrait être le premier résultat)
- Cliquez sur le bouton bleu **Install**
- Attendez que l'installation soit terminée (quelques secondes)

## Étape 4 : Connecter VS Code à WSL

- Regardez le coin inférieur gauche de VS Code - vous verrez une icône bleue ou verte
- Cliquez sur cette icône pour ouvrir le menu de connexion à distance
- Sélectionnez **Connect to WSL** dans le menu
- VS Code va se recharger et se connecter à votre installation Ubuntu
- Le coin inférieur gauche devrait maintenant afficher **WSL: Ubuntu**

La première fois que vous vous connectez, VS Code installe un petit serveur dans WSL. Cela prend environ 30 secondes.

## Étape 5 : Ouvrir le Dossier dans VS Code

- Dans VS Code (toujours connecté à WSL), cliquez sur **File** dans la barre de menus, puis **Open Folder**
- Un menu déroulant **Open Folder** apparaît en haut au centre.
- Trouvez votre dossier en tapant :
  ```
  /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Remplacez `YOUR_USERNAME` par votre nom d'utilisateur Windows (par exemple, `John.Smith`)
- Cliquez sur **OK**. VS Code se recharge avec votre dossier `test_claude`
- Si l'on vous demande « Do you trust the authors? », cliquez sur **Yes, I trust the authors**


## Étape 6 : Démarrer Claude Code

- Après le rechargement de VS Code, ouvrez un nouveau terminal : cliquez sur **Terminal** dans la barre de menus, puis **New Terminal**
- Dans le panneau du terminal, tapez :
  ```
  claude
  ```
- Claude Code démarre - vous verrez l'interface familière de Claude Code
- Vous êtes maintenant prêt à utiliser Claude Code tout en éditant des fichiers dans VS Code

## Étape 7 : Tester le Flux de Travail

- Dans Claude Code, tapez :
```
Write a short article explaining why LLMs like to use Markdown format. Save it as article.md
```
- Claude Code crée le fichier - vous verrez `article.md` apparaître dans le panneau Explorateur à gauche
- Cliquez sur `article.md` dans l'Explorateur pour le visualiser dans l'éditeur
- Pour prévisualiser l'article formaté : faites un clic droit sur l'onglet `article.md` et sélectionnez **Open Preview**
- Vous verrez le Markdown rendu avec des titres, des puces et une mise en forme appropriés

## Réouvrir Claude dans VS Code Ultérieurement

Après avoir fermé VS Code, voici comment revenir à vos projets WSL :

- **Option A :** Ouvrez VS Code, cliquez sur le coin inférieur gauche, sélectionnez **Connect to WSL**, puis **File > Open Recent**. Sélectionnez `/mnt/c/Users/YOUR_USERNAME/Documents/test_claude [WSL: Ubuntu]`
- **Option B :** Ouvrez l'application Ubuntu depuis Windows, naviguez vers votre projet dans le terminal, et tapez `code .`

VS Code se souvient de vos dossiers récents, donc l'Option A avec Open Recent est généralement la plus rapide.

## Prochaines Étapes

- Demandez à Claude Code d'expliquer une base de code existante : « Explain what this project does »
- Demandez à Claude Code de vous aider à écrire de nouvelles fonctionnalités : « Add a function that calculates the average of a list »
- Utilisez Claude Code pour corriger des bugs : « This code gives an error, can you fix it? »
- Essayez l'extension VS Code de Claude Code pour une interface visuelle avec des diffs en ligne (recherchez « Claude Code » dans Extensions)
- Pour gérer des fichiers plus volumineux plus efficacement, créez un dossier dans le système de fichiers WSL (`/home/user/`). Depuis Windows, recherchez l'icône Linux en bas de la barre latérale dans l'Explorateur de fichiers. Ou saisissez `\\wsl.localhost\` dans la barre d'adresse.

## Dépannage

- **« WSL: Ubuntu » ne s'affiche pas dans le coin inférieur gauche** - Assurez-vous que WSL est correctement installé ; essayez d'abord d'ouvrir le terminal Ubuntu pour vérifier qu'il fonctionne
- **Le terminal affiche PowerShell au lieu de Linux** - Cliquez sur la flèche déroulante à côté du **+** dans le panneau du terminal et sélectionnez **Ubuntu (WSL)**
- **Commande `claude` introuvable** - Exécutez `claude --version` pour vérifier si Claude Code est installé ; sinon, suivez d'abord le tutoriel d'installation WSL

## Aperçu du Flux de Travail

- **VS Code** s'exécute sur Windows et fournit l'interface d'éditeur visuel
- **L'Extension WSL** connecte VS Code à Ubuntu afin que vous puissiez exécuter des outils Linux
- **Le Terminal Intégré** exécute Claude Code à l'intérieur de WSL
- Vos fichiers restent dans Windows (dossier Documents) - WSL y accède via `/mnt/c/`
- Éditez les fichiers dans l'éditeur, discutez avec Claude Code dans le terminal - le meilleur des deux mondes

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 10 décembre 2025.
