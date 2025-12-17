[Accueil](../fr/)

# Créer des Commandes Slash Personnalisées

Fatigué de taper les mêmes prompts détaillés encore et encore ? Les commandes slash personnalisées vous permettent de sauvegarder des instructions complexes sous forme de raccourcis réutilisables. Comme créer des raccourcis clavier pour vos tâches les plus fréquentes, les commandes slash transforment de longs prompts en commandes simples comme `/stock-report Apple` qui génèrent des rapports complets instantanément.

Le meilleur ? Nous utilisons Claude pour écrire le prompt détaillé et créer la Skill. Oui, Claude est très doué pour se prompter... lui-même.

## Concepts Clés

- **Commande slash** - Un prompt réutilisable stocké sous forme de fichier Markdown que Claude Code exécute lorsque vous tapez `/nom-commande`
- **Arguments** - Variables que vous passez aux commandes (comme des symboles boursiers) en utilisant le mot-clé spécial `$ARGUMENTS`
- **Dossier `.claude/commands/`** - Où Claude Code découvre et charge automatiquement vos commandes personnalisées

## Ce Dont Vous Aurez Besoin

- Avoir complété [Claude Code in VS Code on Windows](./Claude_Code_in_VS_Code_Win.md) ou [Claude Code in VS Code on Mac](./Claude_Code_in_VS_Code_Mac.md)
- Un sujet à rechercher (nous utiliserons les rapports boursiers comme exemple)
- Un éditeur de texte tel que VS Code installé
- 15-20 minutes

## Étape 1 : Créer un Dossier de Projet

**Windows (WSL) :**
- Ouvrez **Ubuntu** depuis le menu Démarrer
- Tapez ces commandes :
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir test_claude
  cd test_claude
   ```
  Remplacez `YOUR_USERNAME` par votre nom d'utilisateur Windows

**Mac :**
- Ouvrez **Terminal** (trouvez-le dans Applications > Utilitaires)
- Tapez ces commandes :
  ```bash
  cd ~/Documents
  mkdir test_claude
  cd test_claude
  ```

## Étape 2 : Démarrer Claude Code

**Windows (WSL) :**
- Toujours dans le terminal Ubuntu, tapez :
  ```
  claude
  ```

**Mac :**
- Toujours dans Terminal, tapez :
  ```
  claude
  ```

Claude Code démarre et affiche un message de bienvenue.

## Étape 3 : Demander à Claude de Créer une Commande Slash

Au lieu de créer manuellement des fichiers, laissez Claude faire le travail. Tapez ce prompt :

```
Create a slash command called stock-report that generates
reports on recent developments of a company identified by name or ticker symbol.
Include:
- Product or service news
- Management team news
- Recent financial reports
- Analyst reports
```
Lorsqu'on vous le demande, accordez à Claude la permission de créer le fichier.
Claude créera un prompt détaillé et l'enregistrera sous `stock-report.md` dans le dossier `.claude/commands/`.

**Remarque :** Nous utilisons le format Markdown partout : dans les prompts, les rapports et les commandes slash. Markdown est adapté à l'IA et peut être facilement modifié comme des fichiers texte brut.

## Étape 4 : Examiner la Commande

Utilisez n'importe quel éditeur de texte pour ouvrir le fichier `stock-report.md` depuis le dossier `.claude/commands/`. C'est le prompt pour la commande slash.

Si vous avez VS Code installé (recommandé) :
- Démarrez VS Code
- Depuis **File**, choisissez **Open folder**, et sélectionnez le dossier de projet `Documents/test_claude`
- Depuis l'explorateur de fichiers, naviguez vers `.claude/commands` et cliquez sur le fichier `stock-report.md` pour l'ouvrir

Examinez le prompt et apportez des modifications aux instructions si vous le souhaitez.

**Remarque :** Claude est incroyablement doué pour écrire des prompts. Vous pouvez voir que son prompt est bien structuré en utilisant le format markdown et clairement rédigé. Apprenez à écrire des prompts comme celui-ci. Il inclut parfois même des instructions pour demander des clarifications si l'identifiant est ambigu.

## Étape 5 : Tester la Commande

Commencez par **quitter** la session Claude Code actuelle en appuyant sur **Ctrl+C** deux fois. Ensuite, redémarrez Claude pour que la nouvelle commande slash soit chargée :
  ```
  claude
  ```
Maintenant, testez votre nouvelle commande avec un vrai symbole boursier :

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
  Save the report as a markdown file. File name has company name and date.
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
Revise the stock-report slash command to save the report as a html file.
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

Claude crée un fichier nommé quelque chose comme `Apple_2025-12-13.html`. Cliquez sur ce fichier depuis File Explorer sur Windows ou Mac pour l'ouvrir dans votre navigateur par défaut.

## Étape 11 : Réutiliser la Commande Slash (Optionnel)

Le mot-clé `$ARGUMENTS` dans votre commande slash agit comme un paramètre fictif. Lorsque vous tapez `/stock-report AAPL`, Claude remplace `$ARGUMENTS` par `AAPL` avant d'exécuter le prompt.

Essayez un autre symbole :

```
/stock-report TSLA
```

La même structure de commande recherche maintenant Tesla à la place.

## Étape 12 : Essayer une Autre Commande Slash (Optionnel)

Si vous avez complété le tutoriel [Writing Research Paper](./Writing_Research_Paper_Claude_Code.md), vous devriez avoir une commande `/research-paper`. Testez-la sur un nouveau sujet.

Commencez par effacer la mémoire de Claude pour repartir de zéro :

```
/clear
```

Ensuite, exécutez la commande research paper :

```
/research-paper AI in schools
```

Deux différences clés :
- /research-paper a été créé à la fin d'une session en capturant l'interaction humaine, tandis que /stock-report est créé à partir de zéro.
- /research-paper demande de manière interactive des entrées avant de rédiger un article.

## Prochaines Étapes

Maintenant que vous comprenez les commandes slash, créez davantage de commandes personnalisées pour vos workflows :

- **Revue de code :** `/review-code` - Analyser le code pour les bugs et les améliorations
- **Notes de réunion :** `/meeting-summary` - Générer des résumés de réunion structurés
- **Brouillons d'email :** `/email-reply` - Créer des réponses email professionnelles

## Dépannage

- **Commande non trouvée :** Redémarrez Claude Code pour recharger les commandes depuis `.claude/commands/`
- **Arguments ne fonctionnent pas :** Vérifiez que `$ARGUMENTS` est orthographié correctement dans le fichier de commande (sensible à la casse)
- **Rapport incomplet :** Demandez à Claude de "continue" ou "add more detail to the [section name] section"

## Aperçu du Workflow

- **Les commandes slash personnalisées** font gagner du temps en transformant des prompts complexes en raccourcis simples
- **Les arguments** rendent les commandes flexibles pour différentes entrées (symboles boursiers, sujets, fichiers)
- **Claude construit les commandes** - Vous n'avez pas besoin d'écrire manuellement des fichiers Markdown ; décrivez simplement ce que vous voulez
- **Les commandes sont réutilisables** - Une fois créées, utilisez-les à travers les projets et les sessions
- **Combinez les commandes** - Construisez une bibliothèque de commandes spécialisées pour différentes tâches

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 13 décembre 2025.
