[Accueil](./)

# Installer Claude Code sur Mac

Claude Code est un assistant IA qui vit dans votre Terminal et vous aide à écrire, déboguer et comprendre du code. Voyez-le comme un partenaire de programmation compétent, disponible dès que vous en avez besoin. Que vous soyez débutant complet ou développeur expérimenté, Claude Code peut accélérer votre flux de travail et faciliter votre apprentissage.

Ce guide vous accompagne pas à pas dans l'installation, avec des instructions détaillées pour les débutants.

## Vue d'ensemble

- Ouvrez Terminal
- Installez Claude Code
- Configurez votre connexion API
- Commencez à utiliser Claude Code

## Concepts clés

- **Terminal** : Une application Mac intégrée où vous tapez des commandes au lieu de cliquer sur des boutons. C'est ainsi que vous interagirez avec Claude Code.
- **Claude Code** : Un assistant de codage IA que vous exécutez dans Terminal. Il peut répondre à des questions, écrire du code et vous aider à comprendre les projets existants.

## Ce dont vous aurez besoin

- Un ordinateur Mac (macOS 13.0 Ventura ou plus récent)
- Connexion Internet
- Accès administrateur sur votre ordinateur
- Abonnement Claude Pro/Max ou clé API
- 5 à 10 minutes

## Étape 1 : Ouvrir Terminal

- Cliquez sur l'icône **Launchpad** dans votre Dock (l'icône avec des carrés colorés)
- Tapez `Terminal` dans la zone de recherche en haut
- Cliquez sur **Terminal** (une icône carrée noire)
- Une fenêtre Terminal s'ouvrira avec un curseur clignotant

**Astuce :** Gardez Terminal ouvert pour les prochaines étapes.

## Étape 2 : Installer Claude Code

Dans Terminal, copiez et collez cette commande, puis appuyez sur **Retour** :
```
curl -fsSL https://claude.ai/install.sh | bash
```

- Attendez que Claude Code s'installe (1 à 2 minutes)
- Vous pouvez voir des messages de progression - c'est normal
- Lorsque l'installation est terminée, fermez et rouvrez Terminal, puis vérifiez en tapant :
   ```
   claude --version
   ```
- Vous devriez voir le numéro de version de Claude Code

**Alternative : Installer avec Homebrew**

Si vous utilisez Homebrew, vous pouvez installer Claude Code avec :
```
brew install --cask claude-code
```

**Astuce :** Exécutez `claude doctor` après l'installation pour vérifier que tout est correctement configuré.

## Étape 3 : Connecter à votre compte Anthropic

### Option A. Utilisez votre abonnement Claude Pro ou Max

- Dans Terminal, tapez :
   ```
   claude
   ```
- Claude essaie d'ouvrir un navigateur. S'il ne s'ouvre pas automatiquement, copiez l'URL affichée dans Terminal et collez-la dans votre navigateur.
- Connectez-vous à votre compte Claude.ai (cela peut se produire automatiquement)
- Cliquez sur **Authorize**
- Cliquez sur **Copy Code** lorsqu'un long code apparaît
- Retournez à la fenêtre Terminal
- Pour coller dans Terminal : Cliquez sur **Édition** dans la barre de menus, puis cliquez sur **Coller**
- Vous devriez voir un message de succès
- Suivez les instructions pour terminer la configuration

### Option B. Utilisez la clé API Anthropic

Si vous avez une clé API Anthropic au lieu d'un abonnement Claude :

- Tout d'abord, obtenez votre clé API depuis la [Anthropic Console](https://console.anthropic.com/)
- Dans Terminal, tapez :
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   Remplacez `your-api-key-here` par votre clé API réelle
- Pour rendre cela permanent (afin de ne pas avoir à le définir à chaque fois), ajoutez-le à votre profil shell :
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```
   Remplacez `your-api-key-here` par votre clé API réelle
- Fermez et rouvrez Terminal pour que les modifications prennent effet

**Remarque :** Si vous utilisez un Mac plus ancien avec bash au lieu de zsh, remplacez `~/.zshrc` par `~/.bash_profile` dans la commande ci-dessus.

### Option C. Utilisez l'API OpenRouter (commencez gratuitement !)

OpenRouter est une passerelle API unifiée qui donne accès à plus de 500 grands modèles de langage via une seule clé API. Cela peut être un moyen économique d'utiliser Claude Code, car vous ne payez que pour l'utilisation et pouvez choisir parmi des modèles à différents niveaux de prix.

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
- Remplacez `your-openrouter-api-key` par votre clé API OpenRouter réelle
- `ANTHROPIC_API_KEY` doit être explicitement défini sur vide
- Pour utiliser des modèles alternatifs, ils doivent prendre en charge les **capacités d'utilisation d'outils**. Vous pouvez remplacer les modèles avec :
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- Parcourez les modèles disponibles sur [openrouter.ai/models](https://openrouter.ai/models)
- Le niveau gratuit vous donne 50 requêtes API par jour
- Consultez le [guide officiel OpenRouter](https://openrouter.ai/docs/guides/claude-code-integration) pour plus de détails


### Option D. Utilisez l'API Anthropic via Azure Foundry

Cette option est destinée aux organisations utilisant des modèles Claude hébergés sur Azure. Dans la fenêtre Terminal, collez ce code pour définir les variables d'environnement (avant de démarrer Claude) :
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

**Remarque :** Remplacez `xxxx-eastus2` par le nom de votre Foundry Resource (n'utilisez pas l'URL de base complète). Remplacez `your_api_key` par votre clé API complète depuis votre portail Azure.

## Étape 4 : Tester Claude Code

Vous êtes prêt ! Voici comment utiliser Claude Code :

- Dans Terminal, tapez :
   ```
   claude
   ```
- Il vous pose quelques questions avant d'être prêt à discuter
- Pour voir si cela fonctionne, posez une question générale telle que "Expliquez l'informatique quantique."

## Étape 5 : Naviguer vers votre projet

- Si vous avez un projet dans vos dossiers Mac, vous pouvez y naviguer :
   ```
   cd ~/Documents/test_claude
   ```
   Remplacez `test_claude` par le nom réel de votre dossier de projet

- Ensuite, démarrez Claude :
   ```
   claude
   ```
- Commencez par demander à Claude de vous expliquer le code source.
- Vous pouvez demander à Claude d'effectuer des modifications.
- Testez votre code dans votre IDE préféré.

**Remarque :** Claude fonctionne à l'intérieur d'un dossier de projet. Il définit les permissions d'écriture dans le dossier et enregistre les paramètres dans ce dossier. C'est l'espace de travail de Claude.

## Étape 6 : Mettre à jour Claude Code

Claude Code installé via l'installateur natif se met à jour automatiquement en arrière-plan. Vous pouvez également déclencher manuellement une mise à jour :

- Dans Terminal, tapez :
   ```
   sudo claude
   ```
- Claude Code vérifiera les mises à jour et installera la dernière version

**Remarque :** Les installations via Homebrew ne se mettent pas à jour automatiquement. Exécutez `brew upgrade claude-code` périodiquement pour obtenir la dernière version.

## Prochaines étapes
- [Premiers pas avec VS Code](./VS_Code_Getting_Started.md) - Apprenez à utiliser VS Code, un éditeur de code populaire
- [Claude Code dans VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - Exécutez Claude Code dans VS Code
- [Rédiger un article de recherche avec Claude Code](./Writing_Research_Paper_Claude_Code.md) - Utilisez Claude Code pour la rédaction académique

## Comment ouvrir Terminal à nouveau

Après avoir fermé Terminal, voici comment l'ouvrir à nouveau :

- Cliquez sur l'icône **Launchpad** dans votre Dock (l'icône avec des carrés colorés)
- Tapez `Terminal` dans la zone de recherche en haut
- Cliquez sur **Terminal**
- Une fenêtre Terminal s'ouvrira

## Dépannage

### Première étape : Exécutez Claude Doctor
Si quelque chose ne fonctionne pas, exécutez d'abord cette commande :
```
claude doctor
```
Elle vérifie votre installation et signale tout problème.

### Le script d'installation échoue
- Assurez-vous d'avoir macOS 13.0 ou plus récent
- Essayez l'alternative Homebrew : `brew install --cask claude-code`
- Vérifiez votre connexion Internet et réessayez

### Commandes Claude Code introuvables
- Fermez Terminal complètement (cliquez sur **Terminal** dans la barre de menus, puis **Quitter Terminal**)
- Ouvrez Terminal à nouveau
- Essayez `claude --version` pour vérifier si Claude Code est installé
- Essayez d'exécuter à nouveau la commande d'installation : `curl -fsSL https://claude.ai/install.sh | bash`

### L'authentification échoue
- Assurez-vous d'avoir un abonnement Claude Pro/Max actif ou une clé API valide
- Essayez d'exécuter `claude` à nouveau et complétez le processus de connexion
- Vérifiez que votre navigateur a ouvert la bonne page d'autorisation

## Conseils pour les utilisateurs Mac

### Trouver les chemins de projet
Pour trouver le chemin vers un dossier :
- Ouvrez Finder
- Naviguez vers votre dossier de projet
- Glissez et déposez le dossier dans Terminal - le chemin complet apparaîtra !

### Utiliser différentes applications Terminal
Vous pouvez également utiliser d'autres applications de terminal telles que :
- iTerm2 (alternative populaire avec plus de fonctionnalités)
- Warp (terminal moderne avec des fonctionnalités IA)
- Hyper (terminal multiplateforme)

Claude Code fonctionne avec tous !

## Besoin d'aide ?

- Pour les problèmes Claude Code : [Claude Code GitHub](https://github.com/anthropics/claude-code)
- Pour la documentation officielle : [Guide de configuration de Claude Code](https://code.claude.com/docs/en/setup)

---

*Dernière mise à jour : Février 2026*
