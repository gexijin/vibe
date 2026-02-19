[Accueil](./)

# Installer Claude Code sur Windows

Claude Code est un assistant IA qui vit dans votre terminal et vous aide à écrire, déboguer et comprendre du code. Ce guide vous accompagne dans la configuration complète : une installation native rapide via PowerShell, puis WSL2 pour l'expérience complète sous Linux.

## Concepts Clés

- **WSL (Windows Subsystem for Linux)** - Une fonctionnalité Windows qui exécute un véritable système Linux parallèlement à Windows
- **Ubuntu** - Une distribution Linux populaire et conviviale pour les débutants que vous pouvez installer via WSL
- **PowerShell** - L'outil de ligne de commande intégré de Windows, utilisé ici pour installer Claude Code et WSL

## Ce Dont Vous Aurez Besoin

- Un ordinateur Windows 10 (version 2004 ou supérieure) ou Windows 11
- Un accès administrateur sur votre ordinateur
- Un abonnement Claude Pro/Max ou une clé API via Azure Foundry
- 10 à 15 minutes

## Étape 1 : Installer Claude Code en Natif sur Windows (fonctionne mais non recommandé)

- Cliquez sur le **bouton Démarrer de Windows**
- Tapez `PowerShell` et cliquez sur **Windows PowerShell**
- Dans la fenêtre PowerShell, tapez :
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Attendez que l'installation se termine
- Fermez et rouvrez PowerShell, puis vérifiez en tapant :
   ```
   claude --version
   ```
- Vous devriez voir le numéro de version de Claude Code

> **Remarque :** L'installation native sur Windows présente certaines limitations :
> - Pas de sandboxing pour l'outil Bash (une fonctionnalité de sécurité disponible uniquement sous WSL2/macOS)
> - Certains outils et flux de travail fonctionnent mieux dans un environnement Linux
>
> Continuez avec les étapes ci-dessous pour installer WSL2 et bénéficier de l'expérience complète.

## Étape 2 : Vérifier la Virtualisation et Installer WSL

**Tout d'abord, vérifiez si la virtualisation est activée :**

- **Faites un clic droit** sur la barre des tâches (la barre en bas de votre écran)
- Cliquez sur **Gestionnaire des tâches** dans le menu
- Si le Gestionnaire des tâches s'ouvre dans une petite fenêtre, cliquez sur **Plus de détails** en bas
- Cliquez sur l'onglet **Performance** en haut
- Cliquez sur **Processeur** dans la barre latérale gauche
- Regardez la section en bas à droite de la fenêtre
- Trouvez la ligne qui indique **Virtualisation :** et vérifiez si elle indique **Activée**

**Si elle indique "Activée" :** Parfait ! Continuez ci-dessous.

**Si elle indique "Désactivée" :** Vous devez activer la virtualisation dans les paramètres BIOS de votre ordinateur :
- Redémarrez votre ordinateur
- Au démarrage, appuyez sur la touche BIOS (généralement **F2**, **F10**, **Suppr** ou **Échap** - cela dépend du fabricant de votre ordinateur)
- Recherchez les paramètres liés à "Virtualization Technology", "Intel VT-x", "AMD-V" ou "SVM Mode"
- Activez ces paramètres
- Enregistrez et quittez le BIOS (généralement **F10**)
- Votre ordinateur redémarrera normalement

**Maintenant, installez WSL :**

- Cliquez sur le **bouton Démarrer de Windows**
- Tapez `PowerShell` dans la zone de recherche
- **Faites un clic droit** sur **Windows PowerShell** et cliquez sur **Exécuter en tant qu'administrateur**
- Cliquez sur **Oui** lorsque l'on vous demande « Voulez-vous autoriser cette application à apporter des modifications à votre appareil ? »

**Vérifiez si WSL et Ubuntu sont déjà installés :**

- Dans la fenêtre PowerShell, tapez :
   ```
   wsl --list --verbose
   ```
- **Si vous voyez "Ubuntu" listé :** WSL est déjà installé ! Passez à l'Étape 3.
- **Si vous voyez un message d'erreur :** Continuez avec l'installation ci-dessous.

**Pour installer WSL et Ubuntu :**

- Dans la fenêtre PowerShell, tapez :
   ```
   wsl --install
   ```
- Vous pourriez voir des messages comme "Installing: Windows Subsystem for Linux" et "Installing: Ubuntu"
- Lorsque l'installation est terminée, redémarrez votre ordinateur :
   - Cliquez sur le **bouton Démarrer de Windows** → **icône Alimentation** → **Redémarrer**
- Votre ordinateur va redémarrer — cela prend environ 1 à 2 minutes

**Remarque :** Si vous obtenez une erreur indiquant que la commande n'est pas reconnue, votre version de Windows est peut-être trop ancienne. Assurez-vous d'avoir Windows 10 version 2004 ou supérieure, ou Windows 11.

## Étape 3 : Configurer Ubuntu

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

**Important :** Retenez ce nom d'utilisateur et ce mot de passe — vous en aurez besoin plus tard.

## Étape 4 : Installer Claude Code dans WSL

- Dans le terminal Ubuntu, tapez :
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Attendez que Claude Code s'installe
- Lorsque l'installation est terminée, vérifiez en tapant :
   ```
   claude --version
   ```
- Vous devriez voir le numéro de version de Claude Code

## Étape 5 : Se Connecter à Votre Compte Anthropic

### Option A. Utiliser votre abonnement Claude Pro ou Max

- Dans le terminal Ubuntu, tapez :
   ```
   claude
   ```
- Claude essaie d'ouvrir un navigateur. S'il ne peut pas s'ouvrir automatiquement, maintenez **Ctrl** enfoncé et cliquez sur l'URL longue pour l'ouvrir dans un navigateur. Alternativement, copiez l'URL et collez-la dans un navigateur externe.
- Connectez-vous à votre compte Claude.ai (cela peut se produire automatiquement si vous utilisez Chrome)
- Cliquez sur **Authorize**
- Cliquez sur **Copy Code** lorsqu'un long code apparaît
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

### Option C. Utiliser l'API OpenRouter (commencez gratuitement !)

OpenRouter est une passerelle API unifiée qui donne accès à plus de 500 grands modèles de langage via une seule clé API. C'est une façon économique d'utiliser Claude Code, car vous ne payez que pour l'utilisation et pouvez choisir parmi des modèles de différentes gammes de prix.

- Inscrivez-vous sur [openrouter.ai](https://openrouter.ai) et connectez-vous
- Cliquez sur **Get API key** et copiez la clé dans un endroit sûr
- Définissez les variables d'environnement requises avant de démarrer Claude Code :
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- Démarrez Claude Code :
   ```
   claude
   ```
- Vérifiez la connexion en tapant `/status` dans Claude Code

**Remarques :**
- Remplacez `your-openrouter-api-key` par votre véritable clé API OpenRouter
- `ANTHROPIC_API_KEY` doit être explicitement défini comme vide
- Pour utiliser des modèles alternatifs, ils doivent prendre en charge les **capacités d'utilisation d'outils**. Vous pouvez remplacer les modèles avec :
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Parcourez les modèles disponibles sur [openrouter.ai/models](https://openrouter.ai/models)
- Le niveau gratuit vous donne 50 requêtes API par jour
- Consultez le [guide officiel OpenRouter](https://openrouter.ai/docs/guides/claude-code-integration) pour plus de détails

### Option D. Utiliser l'API Anthropic via Azure Foundry

Avant de démarrer Claude Code, dans le terminal Ubuntu, collez ce code pour définir les variables d'environnement :
```
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure resource name
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**Remarque :** Remplacez `xxxx-eastus2` par le nom de votre Ressource Foundry (n'utilisez pas l'URL de base complète). Remplacez `your_api_key` par votre clé API complète depuis votre portail Azure.

Ensuite, démarrez Claude Code :
```
claude
```

Vous devriez maintenant pouvoir utiliser Claude Code avec les modèles Claude déployés sur Azure.

## Étape 6 : Tester Claude Code

Vous êtes prêt ! Tapez `claude` dans le terminal Ubuntu et posez une question générale comme "Explain quantum computing."

## Étape 7 : Accéder à Vos Projets

**Windows natif (PowerShell) :**
- Si vous avez un dossier de projet, naviguez vers celui-ci :
   ```
   cd ~/Documents/test_claude
   ```
- Puis démarrez Claude :
   ```
   claude
   ```

**WSL (Ubuntu) :**
- Si vous avez un dossier Windows appelé `test_claude`, vous pouvez y accéder :
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Remplacez `Username` par votre nom d'utilisateur Windows réel.
- Puis démarrez Claude :
   ```
   claude
   ```

- Commencez par demander à Claude de vous expliquer la base de code.
- Vous pouvez demander à Claude d'apporter des modifications.
- Testez votre code dans votre IDE préféré.

**Remarque :** Claude fonctionne dans un dossier de projet. Il enregistre les paramètres dans ce dossier. C'est l'espace de travail de Claude.

## Étape 8 : Mettre à Jour Claude Code

Claude Code se met à jour automatiquement, mais vous pouvez le mettre à jour manuellement à tout moment :

**WSL (Ubuntu) :**
```
sudo claude update
```

**Windows natif (PowerShell — exécuter en tant qu'administrateur) :**
```
claude update
```

## Prochaines Étapes

- **Configurer VS Code :** Suivez le guide [VS Code Getting Started](VS_Code_Getting_Started), puis connectez-le à Claude Code avec [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win)
- **Apprendre les bases de Git :** Ajoutez le contrôle de version à vos projets avec [Claude Code Git on Windows](Claude_Code_Git_Windows)
- **Essayer un projet :** Parcourez [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) pour voir Claude Code en action

## Dépannage

### Première étape : Exécuter Claude Doctor

Si quelque chose ne fonctionne pas, essayez d'abord cette commande :
```
claude doctor
```
Cet outil de diagnostic intégré vérifie votre installation et signale les problèmes courants.

### Commande claude introuvable (Windows natif)

- Fermez et rouvrez PowerShell
- Essayez d'exécuter à nouveau la commande d'installation :
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- Assurez-vous que votre PATH inclut le répertoire d'installation de Claude

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
Cette erreur signifie que la virtualisation n'est pas activée :
- Retournez à l'Étape 2 et vérifiez dans le Gestionnaire des tâches si la virtualisation est activée
- Si elle est désactivée, vous devez l'activer dans le BIOS de votre ordinateur (voir l'Étape 2 pour les instructions)
- Après avoir activé la virtualisation, redémarrez votre ordinateur et essayez `wsl --install` à nouveau

### "wsl --install" ne fonctionne pas
- Assurez-vous que vous exécutez PowerShell en tant qu'administrateur
- Assurez-vous d'avoir Windows 10 version 2004+ ou Windows 11
- Essayez d'exécuter : `wsl --update` d'abord, puis essayez `wsl --install` à nouveau

### La fenêtre Ubuntu ne s'ouvre pas après le redémarrage
- Cliquez sur le bouton Démarrer de Windows
- Tapez `Ubuntu`
- Cliquez sur l'application Ubuntu pour la lancer manuellement

### Comment ouvrir le terminal Ubuntu après l'avoir fermé
- Cliquez sur le **bouton Démarrer de Windows**, tapez `Ubuntu`, et cliquez sur l'application **Ubuntu** (icône de cercle orange)

### Commandes Claude Code introuvables (WSL)
- Assurez-vous que l'installation s'est terminée avec succès
- Essayez de fermer et de rouvrir le terminal Ubuntu
- Essayez d'exécuter à nouveau la commande d'installation : `curl -fsSL https://claude.ai/install.sh | bash`

## Besoin d'Aide ?

- Pour les problèmes WSL : [Documentation WSL de Microsoft](https://docs.microsoft.com/en-us/windows/wsl/)
- Pour les problèmes Claude Code : [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025. Mis à jour en février 2026.
