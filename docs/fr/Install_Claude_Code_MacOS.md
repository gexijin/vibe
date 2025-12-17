[Accueil](../fr/)

# Installer Claude Code sur Mac

Claude Code est un assistant IA qui fonctionne dans votre Terminal et vous aide à écrire, déboguer et comprendre du code. Considérez-le comme un partenaire de codage compétent disponible chaque fois que vous avez besoin d'aide. Que vous soyez débutant complet ou développeur expérimenté, Claude Code peut accélérer votre flux de travail et vous aider à apprendre.

Ce guide vous accompagne à travers l'installation étape par étape, avec des instructions détaillées pour les débutants.

## Vue d'ensemble

- Téléchargez et installez Node.js
- Installez Claude Code en utilisant npm
- Configurez votre clé API
- Commencez à utiliser Claude Code

## Concepts clés

- **Terminal** : Une application Mac intégrée où vous tapez des commandes au lieu de cliquer sur des boutons. C'est ainsi que vous interagirez avec Claude Code.
- **Node.js** : Un logiciel dont Claude Code a besoin pour fonctionner. Considérez-le comme le moteur qui alimente Claude Code.
- **Claude Code** : Un assistant de codage IA que vous exécutez dans Terminal. Il peut répondre à des questions, écrire du code et vous aider à comprendre les projets existants.

## Ce dont vous aurez besoin

- Un ordinateur Mac (macOS 10.15 Catalina ou plus récent recommandé)
- Connexion Internet
- Accès administrateur sur votre ordinateur
- Abonnement Claude Pro/Max ou clé API
- 15 à 20 minutes

## Étape 1 : Télécharger Node.js

Claude Code nécessite Node.js version 18 ou supérieure.

**Tout d'abord, vérifiez si Node.js est déjà installé :**

- Cliquez sur l'icône **Launchpad** dans votre Dock (l'icône avec des carrés colorés)
- Tapez `Terminal` dans la zone de recherche en haut
- Cliquez sur **Terminal** (une icône carrée noire)
- Dans Terminal, tapez :
   ```
   node --version
   ```
- Regardez les résultats :
   - **Si vous voyez un numéro de version comme `v18.x.x` ou supérieur** : Node.js est déjà installé ! Passez à l'Étape 4.
   - **Si vous voyez "command not found"** : Continuez avec l'installation ci-dessous.

**Pour télécharger Node.js :**

- Ouvrez votre navigateur Web (Safari, Chrome, Firefox, etc.)
- Allez sur ce site Web :
   ```
   https://nodejs.org/
   ```
- Cliquez sur le bouton vert qui dit **Obtenir Node.js** (ou **Get Node.js** en anglais)
- Cliquez sur le bouton vert qui dit **macOS Installer (.pkg)** au milieu de l'écran
- Un fichier sera téléchargé dans votre dossier Téléchargements (prend généralement 30 à 60 secondes)
   - Le fichier sera nommé quelque chose comme `node-v24.x.x.pkg`

## Étape 2 : Installer Node.js

- Ouvrez **Finder** (cliquez sur l'icône du visage souriant bleu dans votre Dock)
- Cliquez sur **Téléchargements** dans la barre latérale gauche
- Trouvez le fichier que vous venez de télécharger (ressemble à `node-v24.x.x.pkg`)
- Double-cliquez sur le fichier pour l'ouvrir
- Une fenêtre d'installation apparaîtra - cliquez sur **Continuer**
- Cliquez à nouveau sur **Continuer** sur l'écran de licence
- Cliquez sur **Accepter** pour accepter la licence
- Cliquez sur **Installer**
- On vous demandera votre mot de passe Mac (celui que vous utilisez pour vous connecter)
- Tapez votre mot de passe et cliquez sur **Installer le logiciel**
- Attendez que l'installation se termine (1 à 2 minutes)
- Cliquez sur **Fermer** lorsque vous voyez "L'installation a réussi"
- Vous pouvez déplacer l'installateur vers la Corbeille si demandé

## Étape 3 : Vérifier l'installation de Node.js

- Cliquez sur l'icône **Launchpad** dans votre Dock (l'icône avec des carrés colorés)
- Tapez `Terminal` dans la zone de recherche en haut
- Cliquez sur **Terminal** (une icône carrée noire)
- Une fenêtre Terminal s'ouvrira
- Dans Terminal, tapez :
   ```
   node --version
   ```
- Vous devriez voir quelque chose comme `v24.x.x` (les chiffres exacts peuvent varier)
- Si vous voyez un numéro de version, parfait ! Node.js est installé correctement

**Si vous voyez "command not found" :**
- Fermez Terminal complètement (cliquez sur **Terminal** dans la barre de menus, puis **Quitter Terminal**)
- Ouvrez Terminal à nouveau
- Essayez la commande à nouveau

**Astuce :** Gardez Terminal ouvert pour les prochaines étapes.

## Étape 4 : Installer Claude Code

- Dans Terminal, tapez :
   ```
   npm install -g @anthropic-ai/claude-code
   ```
- Attendez que Claude Code s'installe (2 à 5 minutes)
- Si vous voyez une erreur "permission denied", essayez avec `sudo` :
   ```
   sudo npm install -g @anthropic-ai/claude-code
   ```
   Ensuite, saisissez votre mot de passe Mac lorsque demandé (vous ne le verrez pas pendant que vous tapez)
- Vous pouvez voir des avertissements en texte jaune ou rouge - c'est généralement normal
- Lorsque l'installation est terminée, vérifiez en tapant :
   ```
   claude --version
   ```
- Vous devriez voir le numéro de version de Claude Code

## Étape 5 : Connecter à votre compte Anthropic

### Option A. Utilisez votre abonnement Claude Pro ou Max

- Dans Terminal, tapez :
   ```
   claude
   ```
- Claude essaie d'ouvrir un navigateur. S'il ne s'ouvre pas automatiquement, copiez l'URL affichée dans Terminal et collez-la dans votre navigateur.
- Connectez-vous à votre compte Claude.ai (cela peut se produire automatiquement)
- Cliquez sur **Autoriser** (ou **Authorize**)
- Cliquez sur **Copier le Code** (ou **Copy Code**) lorsqu'un long code apparaît
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

### Option C. Utilisez l'API Anthropic via Azure Foundry

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

## Étape 6 : Commencer à utiliser Claude Code

Vous êtes prêt ! Voici comment utiliser Claude Code :

- Dans Terminal, tapez :
   ```
   claude
   ```
- Il vous pose quelques questions avant d'être prêt à discuter
- Pour voir si cela fonctionne, posez une question générale telle que "Expliquez l'informatique quantique."

## Étape 7 : Naviguer vers votre projet

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

## Prochaines étapes
- [VS Code Getting Started](./VS_Code_Getting_Started.md) - Apprenez à utiliser VS Code, un éditeur de code populaire
- [Claude Code in VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - Exécutez Claude Code dans VS Code
- [Writing a Research Paper with Claude Code](./Writing_Research_Paper_Claude_Code.md) - Utilisez Claude Code pour la rédaction académique

## Comment ouvrir Terminal à nouveau

Après avoir fermé Terminal, voici comment l'ouvrir à nouveau :

- Cliquez sur l'icône **Launchpad** dans votre Dock (l'icône avec des carrés colorés)
- Tapez `Terminal` dans la zone de recherche en haut
- Cliquez sur **Terminal**
- Une fenêtre Terminal s'ouvrira

## Dépannage

### L'installateur Node.js ne s'ouvre pas
- Assurez-vous d'avoir téléchargé le fichier `.pkg` depuis nodejs.org
- Essayez de faire un clic droit sur le fichier et sélectionnez **Ouvrir** au lieu de double-cliquer
- Allez dans **Réglages Système** > **Confidentialité et Sécurité** et cliquez sur **Ouvrir quand même**

### "node: command not found" après l'installation
- Fermez Terminal complètement (cliquez sur **Terminal** dans la barre de menus, puis **Quitter Terminal**)
- Ouvrez Terminal à nouveau
- Essayez `node --version` à nouveau
- Si cela ne fonctionne toujours pas, redémarrez votre Mac et réessayez

### L'installation npm échoue avec des erreurs de permission
- Ajoutez `sudo` avant la commande npm :
  ```
  sudo npm install -g @anthropic-ai/claude-code
  ```
- Saisissez votre mot de passe Mac lorsque demandé (vous ne le verrez pas pendant que vous tapez)

### Commandes Claude Code introuvables
- Assurez-vous que l'installation npm s'est terminée avec succès
- Essayez de fermer et de rouvrir Terminal
- Vérifiez si Claude Code est installé : `npm list -g @anthropic/claude-code`
- Essayez de réinstaller : `npm install -g @anthropic-ai/claude-code`

### Erreurs "Cannot find module"
- Assurez-vous que Node.js est correctement installé : `node --version`
- Essayez de réinstaller Claude Code : `npm uninstall -g @anthropic/claude-code` puis `npm install -g @anthropic-ai/claude-code`

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

- Pour le téléchargement de Node.js : [Node.js Official Website](https://nodejs.org/)
- Pour les problèmes Node.js : [Node.js Documentation](https://nodejs.org/docs/)
- Pour les problèmes npm : [npm Documentation](https://docs.npmjs.com/)
- Pour les problèmes Claude Code : [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

*Dernière mise à jour : Décembre 2025*
