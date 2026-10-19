---
title: "Créer des Commandes Slash Personnalisées"
lang: "fr"
---
[Accueil](../fr/)

# Créer des Commandes Slash Personnalisées

Fatigué de taper les mêmes prompts détaillés encore et encore ? Les commandes slash personnalisées vous permettent de sauvegarder des instructions complexes sous forme de raccourcis réutilisables. Tout comme des raccourcis clavier pour vos tâches les plus fréquentes, les commandes slash transforment de longs prompts en commandes simples comme `/stock-report Apple` qui génèrent des rapports complets instantanément.

Le meilleur ? Nous utilisons Claude pour écrire le prompt détaillé et créer la commande slash. Oui, Claude est très doué pour se prompter... lui-même.

## Concepts Clés

- **Commande slash** - Un prompt réutilisable stocké sous forme de fichier Markdown que Claude Code exécute lorsque vous tapez `/nom-commande`
- **Arguments** - Variables que vous passez aux commandes (comme des symboles boursiers) en utilisant le mot-clé spécial `$ARGUMENTS`
- **Dossier `.claude/commands/`** - Où Claude Code découvre et charge automatiquement vos commandes personnalisées

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Configurer VS Code pour Claude Code sur Windows](./Claude_Code_in_VS_Code_Win.md) ou [Utiliser Claude Code depuis VS Code sur Mac](./Claude_Code_in_VS_Code_Mac.md)
- Un sujet à rechercher (nous utiliserons les rapports boursiers comme exemple)
- Un éditeur de texte tel que VS Code installé
- 15-20 minutes

## Étape 1 : Créer un Dossier de Projet

**Windows (PowerShell) :**
- Ouvrez **PowerShell** depuis le menu Démarrer
- Tapez ces commandes :
  ```
  cd ~\Documents
  mkdir -Force test_claude
  cd test_claude
  ```

**Mac :**
- Ouvrez **Terminal** (trouvez-le dans Applications > Utilitaires)
- Tapez ces commandes :
  ```bash
  cd ~/Documents
  mkdir -p test_claude
  cd test_claude
  ```

Si le dossier existe déjà, ces commandes le réutilisent simplement.

## Étape 2 : Démarrer Claude Code

**Windows (PowerShell) :**
- Toujours dans PowerShell, tapez :
  ```
  claude
  ```

**Mac :**
- Toujours dans Terminal, tapez :
  ```
  claude
  ```

Connectez-vous avec votre abonnement Claude en suivant le tutoriel d'installation ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Après vous être connecté, vous verrez un message de bienvenue et l'invite Claude Code.

## Étape 3 : Demander à Claude de Créer une Commande Slash

Au lieu de créer manuellement des fichiers, laissez Claude faire le travail. Tapez ce prompt :

```
Crée une commande slash dans .claude/commands/ appelée stock-report qui génère
des rapports sur les développements récents d'une entreprise identifiée par nom ou symbole boursier.
Inclus :
- Actualités produits ou services
- Actualités de l'équipe de direction
- Rapports financiers récents
- Rapports d'analystes
```
Si Claude demande la permission de créer le fichier, choisissez **Yes**.
Claude créera un prompt détaillé et l'enregistrera sous `stock-report.md` dans le dossier `.claude/commands/`.
(Si Claude l'a plutôt enregistré sous `.claude/skills/stock-report/SKILL.md`, cela fonctionne de la même manière. Ouvrez ce fichier dans les étapes suivantes.)

**Remarque :** Nous utilisons le format Markdown partout : dans les prompts, les rapports et les commandes slash. Markdown est adapté à l'IA et peut être facilement modifié comme des fichiers texte brut.

## Étape 4 : Examiner la Commande

Utilisez n'importe quel éditeur de texte pour ouvrir le fichier `stock-report.md` depuis le dossier `.claude/commands/`. C'est le prompt pour la commande slash.

Si vous avez VS Code installé (recommandé) :
- Démarrez VS Code
- Depuis **File**, choisissez **Open Folder**, et sélectionnez le dossier de projet `Documents/test_claude`
- Dans le panneau **Explorer** de VS Code (à gauche), naviguez vers `.claude/commands` et cliquez sur le fichier `stock-report.md` pour l'ouvrir

Examinez le prompt et apportez des modifications aux instructions si vous le souhaitez.

**Remarque :** Claude est incroyablement doué pour écrire des prompts. Vous pouvez voir que son prompt est bien structuré en utilisant le format markdown et clairement rédigé. Apprenez à écrire des prompts comme celui-ci. Il inclut parfois même des instructions pour demander des clarifications si l'identifiant est ambigu.

## Étape 5 : Tester la Commande

Commencez par **quitter** la session Claude Code actuelle en appuyant sur **Ctrl+C** deux fois. Ensuite, redémarrez Claude pour que la nouvelle commande slash soit chargée :
  ```
  claude
  ```
Maintenant, testez votre nouvelle commande avec une vraie entreprise :

```
/stock-report Apple
```

Claude effectue une recherche sur le web et génère un rapport complet sur Apple Inc. Cela peut prendre 1-2 minutes.

## Étape 6 : Examiner le Rapport Généré

Claude crée un rapport dans la ligne de commande. Examinez le résultat :

- Vérifiez que chaque section contient des informations pertinentes et actuelles
- Vérifiez que les sources sont crédibles et récentes
- Remarquez comment Claude a organisé l'information

## Étape 7 : Enregistrer le Rapport dans un Fichier

Modifions la commande slash pour enregistrer automatiquement les rapports sous forme de fichiers markdown. Ajoutez ceci au fichier markdown de la commande slash manuellement.

- Ouvrez le fichier `stock-report.md` depuis le dossier `.claude/commands/`
- Ajoutez ceci à la fin.
  ```
  Enregistre le rapport sous forme de fichier markdown. Le nom du fichier contient le nom de l'entreprise et la date.
  ```
- Enregistrez le fichier.

## Étape 8 : Réexécuter la Commande

- Commencez par **quitter** la session Claude Code actuelle en appuyant sur **Ctrl+C** deux fois. Ensuite, redémarrez Claude pour que la nouvelle commande slash soit chargée :
  ```
  claude
  ```
- Maintenant, testez votre nouvelle commande avec un vrai symbole boursier :

  ```
  /stock-report AAPL
  ```
- Ouvrez le rapport

Claude génère le rapport et l'enregistre sous forme de fichier markdown nommé quelque chose comme `Apple_2025-12-13.md`. Cliquez sur le fichier dans VS Code pour le visualiser.

## Étape 9 : Modifier la Commande via Claude

Vous pouvez demander à Claude de modifier les commandes slash :

```
Révise la commande slash stock-report pour enregistrer le rapport sous forme de fichier HTML.
```

Claude met à jour le fichier de commande. Vous pouvez vérifier depuis l'éditeur.

## Étape 10 : Tester la Commande Mise à Jour

- Commencez par **quitter** la session Claude Code actuelle en appuyant sur **Ctrl+C** deux fois. Ensuite, redémarrez Claude pour que la nouvelle commande slash soit chargée :
  ```
  claude
  ```

- Testez la commande améliorée :

  ```
  /stock-report AAPL
  ```

Claude crée un fichier nommé quelque chose comme `Apple_2025-12-13.html`. Double-cliquez sur ce fichier dans l'**Explorateur de fichiers** (Windows) ou le **Finder** (Mac) pour l'ouvrir dans votre navigateur par défaut.

## Étape 11 : Réutiliser la Commande Slash (Optionnel)

Le mot-clé `$ARGUMENTS` dans votre commande slash agit comme un paramètre fictif. Lorsque vous tapez `/stock-report AAPL`, Claude remplace `$ARGUMENTS` par `AAPL` avant d'exécuter le prompt. (Si votre fichier de commande ne contient pas `$ARGUMENTS`, Claude Code ajoute simplement ce que vous avez tapé à la fin du prompt, donc cela fonctionne quand même.)

Essayez un autre symbole :

```
/stock-report TSLA
```

La même structure de commande recherche maintenant Tesla à la place.

## Étape 12 : Essayer une Autre Commande Slash (Optionnel)

Si vous avez terminé le tutoriel [Rédiger un article de recherche avec Claude Code](./Writing_Research_Paper_Claude_Code.md), vous devriez avoir une commande `/research-paper`. Testez-la sur un nouveau sujet.

Commencez par effacer la mémoire de Claude pour repartir de zéro :

```
/clear
```

Ensuite, exécutez la commande `/research-paper` :

```
/research-paper L'IA à l'école
```

Deux différences clés :
- La commande /research-paper a été créée à la fin d'une session en capturant l'interaction humaine, tandis que /stock-report a été créée de zéro.
- /research-paper demande de manière interactive des entrées avant de rédiger un article.

## Prochaines Étapes

Maintenant que vous comprenez les commandes slash, créez davantage de commandes personnalisées pour vos flux de travail :

- **Revue de code :** `/review-code` - Analyser le code pour les bugs et les améliorations
- **Notes de réunion :** `/meeting-summary` - Générer des résumés de réunion structurés
- **Brouillons d'email :** `/email-reply` - Créer des réponses email professionnelles

## Dépannage

- **Commande non trouvée :** Redémarrez Claude Code pour recharger les commandes depuis `.claude/commands/`
- **Les arguments ne fonctionnent pas :** Vérifiez que `$ARGUMENTS` est orthographié correctement dans le fichier de commande (sensible à la casse)
- **Rapport incomplet :** Demandez à Claude : « continue » ou « ajoute plus de détails à la section [nom de la section] »

## Aperçu du Flux de Travail

- **Les commandes slash personnalisées** font gagner du temps en transformant des prompts complexes en raccourcis simples
- **Les arguments** rendent les commandes flexibles pour différentes entrées (symboles boursiers, sujets, fichiers)
- **Claude construit les commandes** - Vous n'avez pas besoin d'écrire manuellement des fichiers Markdown ; décrivez simplement ce que vous voulez
- **Les commandes sont réutilisables** - Une fois créées, utilisez-les dans chaque session de ce dossier de projet. Pour utiliser une commande dans tous vos projets, demandez à Claude de la déplacer dans votre dossier personnel `~/.claude/commands/`
- **Combinez les commandes** - Construisez une bibliothèque de commandes spécialisées pour différentes tâches

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 13 décembre 2025.
