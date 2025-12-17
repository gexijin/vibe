[Accueil](../fr/)

# Créer un Claude Skill pour la Recherche Médicale

Rester informé de la recherche médicale implique de parcourir des articles scientifiques denses remplis de jargon. Un Claude Skill, c'est comme avoir un assistant de recherche qui lit des centaines d'articles et les explique en langage clair - au lieu de passer des heures à chercher sur PubMed et à décoder un langage technique, vous posez une simple question et obtenez un résumé clair basé sur les dernières avancées scientifiques.

Dans ce tutoriel, vous allez créer un Claude Skill qui recherche la littérature médicale évaluée par les pairs. Nous créons d'abord un script Python pour interroger PubMed. La meilleure partie ? Vous pouvez demander à Claude de faire tout le travail ! Il dispose d'un Skill qui crée des Skills !

## Concepts Clés

- **Claude Skill** - Un outil spécialisé qui étend les capacités de Claude Code avec des instructions personnalisées, du code et de la documentation stockés dans `.claude/skills/`
- **PubMed** - Base de données gratuite de plus de 35 millions d'articles de recherche biomédicale maintenue par la Bibliothèque Nationale de Médecine des États-Unis
- **Biopython** - Bibliothèque Python qui fournit des outils pour interroger la base de données PubMed de manière programmatique
- **Auto-edit mode** - Fonctionnalité activée avec Shift+Tab qui permet à Claude d'effectuer plusieurs modifications de fichiers sans demander la permission à chaque fois

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Claude Code dans VS Code sur Windows](./Claude_Code_in_VS_Code_Win.md) ou [Claude Code dans VS Code sur Mac](./Claude_Code_in_VS_Code_Mac.md)
- Connexion Internet pour les recherches PubMed
- 15-20 minutes

## Étape 1 : Naviguer vers le Dossier du Projet

Si vous avez terminé le [tutoriel sur les slash commands](./Reuse_Prompts_via_Slash_Commands.md), le dossier `test_claude` existe déjà. Ces commandes fonctionnent dans tous les cas.

**Windows (WSL) :**
- Ouvrez **Ubuntu** depuis le menu Démarrer
- Tapez ces commandes :
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir -p test_claude
  cd test_claude
  ```
  Remplacez `YOUR_USERNAME` par votre nom d'utilisateur Windows

**Mac :**
- Ouvrez **Terminal** (trouvez-le dans Applications > Utilitaires)
- Tapez ces commandes :
  ```bash
  cd ~/Documents
  mkdir -p test_claude
  cd test_claude
  ```

Le flag `-p` crée le dossier s'il n'existe pas, ou ne fait simplement rien s'il existe déjà.

## Étape 2 : Démarrer Claude Code

Tapez cette commande :
```bash
claude
```

Claude Code démarre et affiche un message de bienvenue.

## Étape 3 : Activer le Mode Auto-Edit

Appuyez sur **Shift+Tab** pour activer le mode auto-edit. Vous verrez un message de confirmation.

Le mode auto-edit permet à Claude de créer et modifier plusieurs fichiers sans demander la permission à chaque fois. Ceci est essentiel pour construire des skills qui impliquent la création de nombreux fichiers.

## Étape 4 : Créer le Script de Recherche PubMed

Copiez et collez ce prompt :

```
Écris un script Python appelé pubmed_search.py qui :
- Prend une requête de recherche comme argument de ligne de commande
- Récupère jusqu'à 10 articles récents
- Renvoie le PMID, le titre, les auteurs, le journal, l'année, un aperçu du résumé et l'URL
```
Claude crée le script. Il installe le package Biopython requis, qui inclut un module entrez pour interagir avec PubMed. Passez en revue la sortie pour voir la structure du script.

## Étape 5 : Tester le Script

Demandez à Claude de le tester :

```
Teste le script avec la requête "immunotherapy breast cancer"
```

Claude exécute le script et affiche 10 articles récents sur l'immunothérapie pour le cancer du sein. Vous verrez les titres, les auteurs, les résumés et les liens PubMed.

**Remarque :** La recherche trouve des milliers d'articles mais ne récupère que les 10 plus récents pour une revue rapide.

## Étape 6 : Créer le Skill de Recherche Médicale

Maintenant, nous allons tout regrouper dans un skill réutilisable. Copiez et collez :

```
Crée un Claude Skill appelé "medical-research" qui :
- Prend en charge une question médicale
- Conçoit des requêtes pour récupérer des résumés PubMed
- Crée des résumés en langage clair accessibles aux non-scientifiques
- Inclut le script pubmed_search.py dans le dossier du skill
```

Claude crée la structure complète du skill :
- `.claude/skills/medical-research/pubmed_search.py` - Le script de recherche
- `.claude/skills/medical-research/SKILL.md` - Instructions pour Claude sur comment utiliser le skill
- `.claude/skills/medical-research/README.md` - Documentation utilisateur
- `.claude/skills/medical-research/EXAMPLES.md` - Exemples de sorties

Cela prend 2-3 minutes car Claude écrit une documentation complète.

## Étape 7 : Tester le Skill

Posez une question de recherche en langage naturel :

```
Est-ce que je peux perdre du poids avec le régime cétogène ?
```

Claude automatiquement :
- Reconnaît ceci comme une question de recherche médicale
- Active le skill medical-research
- Recherche des articles pertinents sur PubMed
- Analyse les découvertes
- Explique la recherche en langage clair couvrant l'efficacité, les mécanismes et les considérations

La réponse inclut des sections comme "Comment Ça Marche", "Résultats de Recherche", "Considérations Importantes" et "Conclusion".

## Étape 8 : Tester une Autre Question

Essayez un autre sujet de recherche :

```
Est-ce que les vaccins causent l'autisme ?
```

La réponse explique le consensus scientifique, l'origine du mythe et les conséquences dans le monde réel.

## Étape 9 : Explorer les Fichiers du Skill (Optionnel)

Ouvrez VS Code pour voir la structure du skill :

**Windows :**
- Ouvrez l'**Explorateur de Fichiers**, naviguez vers `C:\Users\YOUR_USERNAME\Documents\test_claude`
- Faites un clic droit sur le dossier et sélectionnez **Ouvrir avec Code**

**Mac :**
- Ouvrez le **Finder**, naviguez vers `Documents/test_claude`
- Faites un clic droit sur le dossier et sélectionnez **Ouvrir avec Visual Studio Code**
- Ou tapez simplement ``` code . ``` depuis Terminal

Dans VS Code :
- Développez `.claude/skills/medical-research/` dans l'explorateur de fichiers
- Ouvrez `SKILL.md` pour voir les instructions détaillées pour Claude
- Ouvrez `README.md` pour voir la documentation utilisateur
- Ouvrez `pubmed_search.py` pour voir le code Python

**Remarque :** Le skill est complètement autonome - tout le code et la documentation vivent dans un seul dossier.

## Étape 10 : Installer des Skills depuis le Répertoire d'Anthropic

Anthropic maintient un répertoire de skills pré-construits que vous pouvez installer et utiliser instantanément.

- Pour installer un skill depuis le répertoire, demandez simplement à Claude :

  ```
  Installe le skill document depuis le répertoire d'Anthropic
  ```
- Essayez ce skill :
  ```
  Crée une présentation PowerPoint sur les Claude Skills.
  ```


Le **document skill** vous aide à lire et écrire des fichiers en PDF, Word, PowerPoint et Excel. Claude clonera le skill dans votre dossier `.claude/skills/`.

**Autres skills disponibles depuis le répertoire d'Anthropic :**
- Parcourez le catalogue complet sur [github.com/anthropics/claude-skills](https://github.com/anthropics/skills)
- Demandez à Claude « Quels skills sont disponibles dans le répertoire d'Anthropic ? » pour voir la liste actuelle

## Prochaines Étapes

- **PDF :** Copiez quelques fichiers PDF dans un sous-dossier de ce dossier de projet et demandez des résumés.
- **Autres skills publics :** Essayez les skills disponibles depuis Anthropic.
- **Partager des skills :** Les skills sont simplement des dossiers zippés !
- **Créer d'autres skills :** Tout ce qui vous intéresse. Par exemple, vous pouvez mettre vos propres fichiers de données dans un dossier de skill.

## Dépannage

- **Biopython non installé :** Claude installera automatiquement Biopython lors de la création du script. Si vous voyez des erreurs d'importation lors du test, demandez à Claude d'installer Biopython manuellement avec `pip install biopython`
- **Script non trouvé :** Vérifiez que le mode auto-edit a été activé (Shift+Tab) - Claude a besoin de la permission pour créer des fichiers
- **Le skill ne s'active pas :** Le skill devrait fonctionner immédiatement après sa création - essayez de poser la question à nouveau ou vérifiez que SKILL.md a le bon `name: medical-research` dans l'en-tête

## Aperçu du Workflow

- **Claude Skills** sont plus puissants que les slash commands - ils combinent code, documentation et instructions personnalisées
- **Auto-edit mode** (Shift+Tab) simplifie la création en évitant les demandes de permission répétées
- **Packaging autonome** - Les scripts vivent à l'intérieur des dossiers de skills, les rendant portables et partageables
- **Activation automatique** - Les skills se déclenchent en fonction des modèles de questions (les questions de recherche activent medical-research)
- **Interface en langage naturel** - Posez des questions naturelles sans connaître les détails techniques

## Skills vs Slash Commands

| Fonctionnalité | Skills | Slash Commands |
|---------|--------|----------------|
| **Ce qu'il contient** | Prompts, code, données et documentation | Prompts uniquement |
| **Activation** | Automatiquement chargé lorsque pertinent | Déclenché manuellement avec `/command` |
| **Cas d'utilisation** | Workflows complexes nécessitant l'exécution de code | Modèles de prompts rapides et workflows |
| **Emplacement du fichier** | `.claude/skills/skill-name/` | `.claude/commands/` |
| **Structure** | Plusieurs fichiers (SKILL.md, README.md, fichiers de code) | Un seul fichier `.md` par commande |

**Point Clé :** Les Slash Commands injectent simplement des prompts depuis l'interface utilisateur. C'est utile, mais limité.

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 13 décembre 2025.
