[Accueil](./)

# Installer Claude Code sur Windows

Claude Code est un assistant IA qui vit dans votre terminal et vous aide à écrire, déboguer et comprendre du code. Avec ce guide, Claude Code fonctionnera nativement sur Windows en quelques minutes. WSL2 est aussi proposé à la fin, en tant qu'option plus avancée.

## Concepts clés

- **PowerShell** - L'outil de ligne de commande intégré de Windows, utilisé ici pour installer et lancer Claude Code
- **Git for Windows** - Un téléchargement gratuit qui ajoute **Git Bash**, le shell que Claude Code utilise pour exécuter des commandes
- **WSL (Windows Subsystem for Linux)** - Une fonctionnalité Windows optionnelle qui exécute un véritable système Linux aux côtés de Windows ; utilisée dans la configuration avancée en fin de guide

## Ce dont vous aurez besoin

- Un ordinateur Windows 10 ou Windows 11
- Un abonnement Claude Pro/Max, ou une clé API
- 5 à 10 minutes

## Étape 1 : Installer Git for Windows (optionnel, recommandé)

Git for Windows est **recommandé, mais optionnel**. Il ajoute **Git Bash**, le shell que Claude Code utilise pour exécuter des commandes. Si vous l'ignorez, Claude Code utilisera PowerShell à la place : passez alors directement à l'Étape 2 et installez Git plus tard si vous le souhaitez.

- Allez sur [git-scm.com/download/win](https://git-scm.com/download/win)
- Le téléchargement devrait démarrer automatiquement — ouvrez le programme d'installation une fois terminé
- Cliquez sur **Next** pour avancer dans l'installation, en acceptant les options par défaut
- Cliquez sur **Install**, puis sur **Finish**

C'est tout — Claude Code détectera Git Bash automatiquement à son démarrage.

## Étape 2 : Installer Claude Code

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

## Étape 3 : Se connecter à votre compte Anthropic

### Option A. Utilisez votre abonnement Claude Pro ou Max

- Dans la fenêtre PowerShell, tapez :
   ```
   claude
   ```
- Claude essaie d'ouvrir un navigateur. S'il ne peut pas s'ouvrir automatiquement, maintenez **Ctrl** enfoncé et cliquez sur l'URL longue pour l'ouvrir dans un navigateur. Vous pouvez aussi copier l'URL et la coller dans un navigateur externe.
- Connectez-vous à votre compte Claude.ai (cela peut se produire automatiquement si vous utilisez Chrome)
- Cliquez sur **Authorize**
- Cliquez sur **Copy Code** lorsqu'un long code apparaît
- Retournez à la fenêtre du terminal
- Pour coller dans le terminal : **Faites un clic droit** et sélectionnez **Coller** (ou appuyez sur **Ctrl+Maj+V**)
- Vous devriez voir un message de succès
- Suivez les instructions pour terminer la configuration

Les options basées sur une API ci-dessous se configurent dans **PowerShell** avec la commande `setx`, qui enregistre un paramètre de façon permanente. Après un `setx`, **fermez et rouvrez PowerShell** pour appliquer le changement, puis lancez `claude`.

### Option B. Utilisez la clé API Anthropic

Si vous avez une clé API Anthropic au lieu d'un abonnement Claude :

- Obtenez votre clé API depuis la [Console Anthropic](https://console.anthropic.com/)
- Dans PowerShell, tapez :
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
   Remplacez `your-api-key-here` par votre clé API réelle
- Fermez et rouvrez PowerShell pour appliquer le changement
- Lancez Claude Code :
   ```
   claude
   ```

### Option C. Utilisez l'API OpenRouter (commencez gratuitement !)

OpenRouter est une passerelle API unifiée qui donne accès à plus de 500 grands modèles de langage via une seule clé API. C'est une façon économique d'utiliser Claude Code : vous ne payez qu'à l'usage et choisissez parmi des modèles de différentes gammes de prix.

- Inscrivez-vous sur [openrouter.ai](https://openrouter.ai) et connectez-vous
- Cliquez sur **Get API key** et copiez la clé dans un endroit sûr
- Dans PowerShell, définissez les variables d'environnement requises :
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- Fermez et rouvrez PowerShell, puis lancez Claude Code :
   ```
   claude
   ```
- Vérifiez la connexion en tapant `/status` dans Claude Code

**Remarques :**
- Remplacez `your-openrouter-api-key` par votre véritable clé API OpenRouter
- `ANTHROPIC_API_KEY` doit être explicitement défini comme vide
- Pour utiliser d'autres modèles, ceux-ci doivent prendre en charge les **capacités d'utilisation d'outils**. Vous pouvez remplacer les modèles avec :
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- Parcourez les modèles disponibles sur [openrouter.ai/models](https://openrouter.ai/models)
- Le niveau gratuit vous donne 50 requêtes API par jour
- Consultez le [guide officiel OpenRouter](https://openrouter.ai/docs/guides/claude-code-integration) pour plus de détails

### Option D. Utilisez l'API Anthropic via Azure Foundry

Dans PowerShell, collez ce code pour définir les variables d'environnement :
```
# Enable Microsoft Foundry integration
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure resource name
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# Set models to your resource's deployment names
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**Remarque :** Remplacez `xxxx-eastus2` par le nom de votre Ressource Foundry (n'utilisez pas l'URL de base complète). Remplacez `your_api_key` par votre clé API complète depuis votre portail Azure.

Ensuite, fermez et rouvrez PowerShell, puis lancez Claude Code :
```
claude
```

Vous devriez maintenant pouvoir utiliser Claude Code avec les modèles Claude déployés sur Azure.

## Étape 4 : Tester Claude Code

Vous êtes prêt ! Tapez `claude` dans PowerShell et posez une question générale comme « Expliquez l'informatique quantique ».

## Étape 5 : Accéder à vos projets

- Si vous avez un dossier de projet, accédez-y dans PowerShell :
   ```
   cd ~/Documents/test_claude
   ```
- Puis démarrez Claude :
   ```
   claude
   ```
- Commencez par demander à Claude de vous expliquer la base de code.
- Vous pouvez demander à Claude d'apporter des modifications.
- Testez votre code dans votre IDE préféré.

**Remarque :** Claude fonctionne dans un dossier de projet et y enregistre ses paramètres. C'est son espace de travail.

## Étape 6 : (Optionnel) Installer WSL2 pour l'expérience complète sous Linux

Pour la plupart des utilisateurs, la configuration native ci-dessus suffit largement. Cela dit, Claude Code fonctionne mieux sous Linux. WSL2 exécute un véritable système Linux dans Windows et ajoute le **sandboxing de l'outil Bash** (une fonctionnalité de sécurité) ainsi qu'une meilleure compatibilité avec les outils Linux. La configuration est plus longue et impose un redémarrage : ne le faites que si vous voulez l'expérience complète sous Linux.

### a) Vérifier la virtualisation et installer WSL

**Tout d'abord, vérifiez si la virtualisation est activée :**

- **Faites un clic droit** sur la barre des tâches (la barre en bas de votre écran)
- Cliquez sur **Gestionnaire des tâches** dans le menu
- Si le Gestionnaire des tâches s'ouvre dans une petite fenêtre, cliquez sur **Plus de détails** en bas
- Cliquez sur l'onglet **Performance** en haut
- Cliquez sur **Processeur** dans la barre latérale gauche
- Trouvez la ligne qui indique **Virtualisation :** et vérifiez si elle indique **Activée**

**Si elle indique "Désactivée" :** Vous devez activer la virtualisation dans le BIOS de votre ordinateur :
- Redémarrez votre ordinateur
- Au démarrage, appuyez sur la touche BIOS (généralement **F2**, **F10**, **Suppr** ou **Échap**, selon le fabricant)
- Recherchez les paramètres liés à "Virtualization Technology", "Intel VT-x", "AMD-V" ou "SVM Mode"
- Activez ces paramètres
- Enregistrez et quittez le BIOS (généralement **F10**)

**Maintenant, installez WSL :**

- Cliquez sur le **bouton Démarrer de Windows**, tapez `PowerShell`
- **Faites un clic droit** sur **Windows PowerShell** et cliquez sur **Exécuter en tant qu'administrateur**
- Cliquez sur **Oui** lorsque l'on vous demande « Voulez-vous autoriser cette application à apporter des modifications à votre appareil ? »
- Dans la fenêtre PowerShell, tapez :
   ```
   wsl --install
   ```
- Vous pourriez voir des messages comme "Installing: Windows Subsystem for Linux" et "Installing: Ubuntu"
- Lorsque l'installation est terminée, redémarrez votre ordinateur

**Remarque :** `wsl --install` nécessite Windows 10 version 2004 ou supérieure, ou Windows 11. Si la commande n'est pas reconnue, votre version de Windows est peut-être trop ancienne.

### b) Configurer Ubuntu

Après le redémarrage, une fenêtre de terminal avec "Ubuntu" dans le titre devrait s'ouvrir automatiquement dans les 2 à 5 minutes. Sinon, cliquez sur le **bouton Démarrer de Windows**, tapez `Ubuntu` et cliquez sur l'application **Ubuntu** (icône de cercle orange).

- Attendez le message : `Enter new UNIX username:`
- Tapez un nom d'utilisateur (lettres minuscules et chiffres uniquement, sans espaces) — par exemple `john`
- Vous verrez : `New password:`
- Tapez un mot de passe simple (vous ne verrez pas les caractères pendant la saisie — c'est normal)
- Tapez à nouveau le même mot de passe lorsque vous y êtes invité

**Important :** Retenez ce nom d'utilisateur et ce mot de passe — vous en aurez besoin plus tard.

### c) Installer Claude Code dans WSL

- Dans le terminal Ubuntu, tapez :
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- Vérifiez en tapant :
   ```
   claude --version
   ```
- Connectez votre compte en tapant `claude` dans le terminal Ubuntu et en suivant la connexion via le navigateur (comme à l'Étape 3, Option A). Si vous utilisez plutôt une clé API, définissez-la avec `export ANTHROPIC_API_KEY="your-api-key-here"` (WSL utilise des commandes Linux, pas `setx`)
- Pour ouvrir un dossier de projet Windows depuis WSL :
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   Remplacez `Username` par votre nom d'utilisateur Windows réel.

## Prochaines étapes

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
- Vérifiez dans le Gestionnaire des tâches si la virtualisation est activée (voir la section WSL optionnelle ci-dessus)
- Si elle est désactivée, activez-la dans le BIOS de votre ordinateur
- Après avoir activé la virtualisation, redémarrez votre ordinateur et essayez `wsl --install` à nouveau

### "wsl --install" ne fonctionne pas
- Assurez-vous d'exécuter PowerShell en tant qu'administrateur
- Assurez-vous d'avoir Windows 10 version 2004+ ou Windows 11
- Exécutez `wsl --update` d'abord, puis `wsl --install` à nouveau

### La fenêtre Ubuntu ne s'ouvre pas après le redémarrage
- Cliquez sur le **bouton Démarrer de Windows**, tapez `Ubuntu` et cliquez sur l'application **Ubuntu** pour la lancer manuellement

## Besoin d'aide ?

- Pour les problèmes WSL : [Documentation WSL de Microsoft](https://docs.microsoft.com/en-us/windows/wsl/)
- Pour les problèmes Claude Code : [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 11 décembre 2025. Mis à jour en juin 2026.
