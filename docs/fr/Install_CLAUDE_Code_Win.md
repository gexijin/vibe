[Accueil](./)

# Installer Claude Code sur Windows avec WSL

Claude Code est un assistant de codage IA puissant, mais les utilisateurs Windows font face à un défi : de nombreux outils de développement fonctionnent mieux sur Linux. La solution ? WSL (Windows Subsystem for Linux) vous permet d'exécuter un environnement Linux complet dans Windows, comme si vous aviez deux ordinateurs en un. Ce guide vous accompagne dans la configuration complète pour que vous puissiez commencer à coder avec Claude en environ 20 minutes.

## Concepts Clés

- **WSL (Windows Subsystem for Linux)** - Une fonctionnalité Windows qui exécute un véritable système Linux parallèlement à Windows
- **Ubuntu** - Une distribution Linux populaire et conviviale pour les débutants que nous installerons via WSL
- **PowerShell** - L'outil de ligne de commande intégré de Windows, utilisé ici pour installer WSL
- **Node.js** - Un environnement d'exécution JavaScript dont Claude Code a besoin pour fonctionner
- **Terminal** - Une interface textuelle pour exécuter des commandes (comme la ligne de commande Ubuntu)

## Ce Dont Vous Aurez Besoin

- Un ordinateur Windows 10 (version 2004 ou supérieure) ou Windows 11
- Un accès administrateur sur votre ordinateur
- Un abonnement Claude Pro/Max ou une clé API via Azure Foundry
- 15 à 20 minutes

## Étape 1 : Vérifier si la Virtualisation est Activée

Avant d'installer WSL, vous devez vérifier que la virtualisation est activée sur votre ordinateur. Cela est nécessaire pour que WSL fonctionne.

- **Faites un clic droit** sur la barre des tâches (la barre en bas de votre écran)
- Cliquez sur **Gestionnaire des tâches** dans le menu
- Si le Gestionnaire des tâches s'ouvre dans une petite fenêtre, cliquez sur **Plus de détails** en bas
- Cliquez sur l'onglet **Performance** en haut
- Cliquez sur **Processeur** dans la barre latérale gauche
- Regardez la section en bas à droite de la fenêtre
- Trouvez la ligne qui indique **Virtualisation :** et vérifiez si elle indique **Activée**

**Si elle indique "Activée" :** Parfait ! Passez à l'Étape 2.

**Si elle indique "Désactivée" :** Vous devez activer la virtualisation dans les paramètres BIOS de votre ordinateur :
- Redémarrez votre ordinateur
- Au démarrage, appuyez sur la touche BIOS (généralement **F2**, **F10**, **Suppr** ou **Échap** - cela dépend du fabricant de votre ordinateur)
- Recherchez les paramètres liés à "Virtualization Technology", "Intel VT-x", "AMD-V" ou "SVM Mode"
- Activez ces paramètres
- Enregistrez et quittez le BIOS (généralement **F10**)
- Votre ordinateur redémarrera normalement

## Étape 2 : Ouvrir PowerShell en tant qu'Administrateur

- Cliquez sur le **bouton Démarrer de Windows** (icône Windows dans le coin inférieur gauche)
- Tapez `PowerShell` dans la zone de recherche
- Dans les résultats de recherche, vous verrez **Windows PowerShell**
- **Faites un clic droit** sur **Windows PowerShell**
- Cliquez sur **Exécuter en tant qu'administrateur** dans le menu
- Une fenêtre apparaîtra demandant "Voulez-vous autoriser cette application à apporter des modifications à votre appareil ?"
- Cliquez sur **Oui**

Une fenêtre bleue avec du texte blanc s'ouvrira - c'est PowerShell en cours d'exécution en tant qu'administrateur.

## Étape 3 : Installer WSL

**D'abord, vérifiez si WSL et Ubuntu sont déjà installés :**

- Dans la fenêtre PowerShell, tapez :
   ```
   wsl --list --verbose
   ```
- Regardez les résultats :
   - **Si vous voyez "Ubuntu" listé** avec un STATE "Running" ou "Stopped" : WSL et Ubuntu sont déjà installés ! Passez à l'Étape 4.
   - **Si vous voyez un message d'erreur** ou "Windows Subsystem for Linux has no installed distributions" : Continuez avec l'installation ci-dessous.

**Pour installer WSL et Ubuntu :**

- Dans la fenêtre PowerShell, tapez :
   ```
   wsl --install
   ```
- Vous pourriez voir des messages comme "Installing: Windows Subsystem for Linux" et "Installing: Ubuntu"
- Lorsque vous voyez un message indiquant que l'installation est terminée, vous devez redémarrer votre ordinateur :
   - Cliquez sur le **bouton Démarrer de Windows**
   - Cliquez sur l'**icône Alimentation**
   - Cliquez sur **Redémarrer**
- Votre ordinateur va redémarrer - cela prend environ 1 à 2 minutes

**Pourquoi le redémarrage est nécessaire :** Le redémarrage permet à Windows d'activer les fonctionnalités WSL et Virtual Machine Platform qui viennent d'être installées.

**Remarque :** Si vous obtenez une erreur indiquant que la commande n'est pas reconnue, votre version de Windows est peut-être trop ancienne. Assurez-vous d'avoir Windows 10 version 2004 ou supérieure, ou Windows 11. Exécutez Windows Update pour obtenir la dernière version.

## Étape 4 : Configurer Ubuntu (Première Fois Uniquement)

Après le redémarrage de votre ordinateur, une fenêtre de terminal avec "Ubuntu" dans le titre devrait s'ouvrir automatiquement dans les 2 à 5 minutes.

**Si la fenêtre Ubuntu ne s'est PAS ouverte automatiquement :**
- Cliquez sur le **bouton Démarrer de Windows**
- Tapez `Ubuntu` dans la zone de recherche
- Cliquez sur **Ubuntu** (vous verrez une icône circulaire orange)
- Le terminal Ubuntu s'ouvrira et continuera la configuration

**Maintenant, complétez la configuration initiale :**

- Attendez le message : `Enter new UNIX username:`
- Tapez un nom d'utilisateur (utilisez uniquement des lettres minuscules et des chiffres, sans espaces)
   - Exemple : `john`
- Vous verrez : `New password:`
- Tapez un mot de passe simple (même le même que le nom d'utilisateur `john`)
- Vous ne verrez pas les caractères pendant que vous tapez - c'est normal
- Tapez à nouveau le même mot de passe lorsque vous y êtes invité

**Important :** Retenez ce nom d'utilisateur et ce mot de passe - vous en aurez besoin plus tard.

## Étape 5 : Mettre à Jour Ubuntu

- Dans la fenêtre du terminal Ubuntu, tapez :
   ```
   sudo apt update
   ```
- Tapez votre mot de passe (celui que vous venez de créer) lorsque vous y êtes invité
- Ensuite, tapez :
   ```
   sudo apt upgrade -y
   ```
- Attendez que tous les paquets soient mis à jour (cela peut prendre 5 minutes)

## Étape 6 : Installer Node.js

Claude Code nécessite Node.js version 18 ou supérieure. Suivez ces étapes :

- Dans le terminal Ubuntu, copiez et collez ces commandes :

   D'abord, téléchargez l'installateur nvm :
   ```
   wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh --no-check-certificate
   cat install.sh | bash
   \. "$HOME/.nvm/nvm.sh"
   nvm install 24
   ```
   Cela télécharge d'abord l'installateur nvm, l'installe, puis l'utilise pour installer Node.js v 24.0
- Attendez que Node.js s'installe (2 à 5 minutes)
- Vérifiez l'installation en tapant :
   ```
   node --version
   ```
- Vous devriez voir quelque chose comme `v24.x.x` (les chiffres exacts peuvent varier)

## Étape 7 : Installer Claude Code

- Dans le terminal Ubuntu, tapez :
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Attendez que Claude Code s'installe (2 à 5 minutes)
- Vous pourriez voir des avertissements en texte jaune ou rouge - c'est généralement normal
- Lorsque l'installation est terminée, vérifiez en tapant :
   ```
   claude --version
   ```
- Vous devriez voir le numéro de version de Claude Code

## Étape 8 : Configurer Votre Connexion API Anthropic

### Option A. Utiliser votre abonnement Claude Pro ou Max

- Dans le terminal Ubuntu, tapez :
   ```
   claude
   ```
- Claude essaie d'ouvrir un navigateur. S'il ne peut pas s'ouvrir automatiquement, maintenez **Ctrl** enfoncé et cliquez sur l'URL longue pour l'ouvrir dans un navigateur. Alternativement, copiez l'URL et collez-la dans un navigateur externe.
- Connectez-vous à votre compte Claude.ai (cela peut se produire automatiquement si vous utilisez Chrome)
- Cliquez sur **Autoriser** (ou **Authorize**)
- Cliquez sur **Copier le Code** (ou **Copy Code**) lorsqu'un long code apparaît
- Retournez à la fenêtre du terminal
- Pour coller dans le terminal : **Faites un clic droit** et sélectionnez **Coller** (ou appuyez sur **Ctrl+Maj+V**)
- Vous devriez voir un message de succès
- Suivez les instructions pour terminer la configuration

### Option B. Utiliser une clé API Anthropic

Si vous avez une clé API Anthropic au lieu d'un abonnement Claude :

- D'abord, obtenez votre clé API depuis la [Console Anthropic](https://console.anthropic.com/)
- Dans le terminal Ubuntu, tapez :
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Remplacez `your-api-key-here` par votre clé API réelle
- Pour rendre ceci permanent (afin de ne pas avoir à le définir à chaque fois), ajoutez-le à votre profil shell :
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```
   Remplacez `your-api-key-here` par votre clé API réelle
- Fermez et rouvrez le terminal Ubuntu pour que les modifications prennent effet
- Vous devriez maintenant pouvoir utiliser Claude Code avec votre clé API

### Option C. Utiliser l'API Anthropic via Azure Foundry

Avant de démarrer Claude Code, dans la fenêtre du terminal Ubuntu, collez ce code pour définir les variables d'environnement :
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Remarque :** Remplacez `xxxx-eastus2` par le nom de votre Ressource Foundry (n'utilisez pas l'URL de base complète). Remplacez `your_api_key` par votre clé API complète depuis votre portail Azure.

Ensuite, démarrez Claude Code :
```
claude
```

Vous devriez maintenant pouvoir utiliser Claude Code avec les modèles Claude déployés sur Azure.


## Étape 9 : Tester Claude Code

Vous êtes prêt ! Pour voir si cela fonctionne, posez une question générale comme "Expliquez l'informatique quantique."

## Étape 10 : Accéder à Vos Projets Windows
- Si vous avez un dossier Windows appelé `test_claude` contenant les fichiers d'un projet, vous pouvez y accéder :
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Remplacez `Username` par votre nom d'utilisateur Windows réel.
- Ensuite, démarrez Claude :
   ```
   claude
   ```
- Commencez par demander à Claude de vous expliquer la base de code.
- Vous pouvez demander à Claude d'apporter des modifications.
- Testez votre code dans votre IDE préféré.

**Remarque :** Claude fonctionne dans un dossier de projet. Il enregistre les paramètres dans ce dossier. C'est l'espace de travail de Claude.

## Prochaines Étapes

- **Configurer VS Code :** Suivez le guide [VS Code Getting Started](VS_Code_Getting_Started), puis connectez-le à Claude Code avec [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)
- **Apprendre les bases de Git :** Ajoutez le contrôle de version à vos projets avec [Claude Code Git on Windows](Claude_Code_Git_Windows)
- **Essayer un projet :** Parcourez [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) pour voir Claude Code en action

## Dépannage

### Comment ouvrir le terminal Ubuntu après l'avoir fermé
- Cliquez sur le **bouton Démarrer de Windows**, tapez `Ubuntu`, et cliquez sur l'application **Ubuntu** (icône de cercle orange)

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
Cette erreur signifie que la virtualisation n'est pas activée :
- Retournez à l'Étape 1 et vérifiez dans le Gestionnaire des tâches si la virtualisation est activée
- Si elle est désactivée, vous devez l'activer dans le BIOS de votre ordinateur (voir l'Étape 1 pour les instructions)
- Après avoir activé la virtualisation, redémarrez votre ordinateur et essayez `wsl --install` à nouveau

### "wsl --install" ne fonctionne pas
- Assurez-vous que vous exécutez PowerShell en tant qu'Administrateur
- Assurez-vous d'avoir Windows 10 version 2004+ ou Windows 11
- Essayez d'exécuter : `wsl --update` d'abord, puis essayez `wsl --install` à nouveau

### La fenêtre Ubuntu ne s'ouvre pas après le redémarrage
- Cliquez sur le bouton Démarrer de Windows
- Tapez `Ubuntu`
- Cliquez sur l'application Ubuntu pour la lancer manuellement

### "sudo: apt: command not found"
- Votre WSL n'a peut-être pas été installé correctement
- Dans PowerShell (en tant qu'Admin), tapez : `wsl --unregister Ubuntu`
- Ensuite, exécutez `wsl --install` à nouveau

### L'installation de Node.js échoue
- Assurez-vous d'avoir exécuté `sudo apt update` en premier
- Essayez la commande d'installation à nouveau

### Les commandes Claude Code sont introuvables
- Assurez-vous que l'installation s'est terminée avec succès
- Essayez de fermer et de rouvrir le terminal Ubuntu
- Essayez d'exécuter à nouveau la commande d'installation : `curl -fsSL https://claude.ai/install.sh | bash`

## Besoin d'Aide ?

- Pour les problèmes WSL : [Documentation WSL de Microsoft](https://docs.microsoft.com/en-us/windows/wsl/)
- Pour les problèmes Claude Code : [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025.
