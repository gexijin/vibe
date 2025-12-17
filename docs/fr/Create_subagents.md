[Accueil](../fr/)

# Créer un Sous-Agent dans Claude Code

Vous souhaitez comparer des opportunités d'investissement, mais faire des recherches sur plusieurs entreprises et les évaluer prend des heures. Imaginez un sous-agent comme l'embauche d'un analyste financier qui sait exactement comment utiliser vos outils de recherche : vous lui donnez des noms d'entreprises, et il rassemble des rapports, évalue chaque entreprise selon des critères clés et recommande le meilleur investissement. Une fois que vous aurez appris à créer des sous-agents, vous pourrez automatiser n'importe quel flux de travail répétitif en plusieurs étapes dans votre travail. Ce tutoriel vous montre comment construire cet analyste.

## Concepts Clés

- **Sous-Agent** - Un travailleur IA spécialisé avec son propre objectif, son prompt système et ses outils qui accomplit des tâches de manière autonome
- **Skill** - Une capacité réutilisable (comme générer des rapports boursiers) que les sous-agents peuvent invoquer pour accomplir leurs objectifs
- **Prompt Système** - Instructions qui définissent ce que fait le sous-agent, comment il évalue les entreprises et quel format il renvoie
- **Séparation des Préoccupations** - Les skills collectent les données ; les sous-agents utilisent ces données pour prendre des décisions

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Claude Code dans VS Code sur Windows](./Claude_Code_in_VS_Code_Win.md) ou [Claude Code dans VS Code sur Mac](./Claude_Code_in_VS_Code_Mac.md)
- Le skill de rapport boursier déjà installé (dans `.claude/skills/generate-stock-reports/`)
- VS Code ou un autre éditeur de texte
- 20-25 minutes

## Étape 1 : Créer un Dossier de Projet et Démarrer Claude Code

**Windows (WSL) :**
- Ouvrez **Ubuntu** depuis le menu Démarrer
- Tapez ces commandes :
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
  Remplacez `YOUR_USERNAME` par votre nom d'utilisateur Windows
- Démarrez Claude Code :
  ```
  claude
  ```

**Mac :**
- Ouvrez **Terminal** (trouvez-le dans Applications > Utilitaires)
- Tapez ces commandes :
  ```bash
  cd ~/Documents
  mkdir stock_picker_test
  cd stock_picker_test
  ```
- Démarrez Claude Code :
  ```
  claude
  ```

Claude Code démarre et affiche un message de bienvenue.

## Étape 2 : Vérifier que le Skill de Rapport Boursier Existe

Avant de construire votre sous-agent, confirmez que le skill est disponible. Tapez :

```
List all available skills
```

Vous devriez voir `generate-stock-reports` dans la sortie. Ce skill fait des recherches sur les entreprises et génère des rapports couvrant les actualités produits, les mises à jour de la direction, les performances financières et les perspectives des analystes.

Si vous ne le voyez pas, les fichiers du skill devraient se trouver dans `.claude/skills/generate-stock-reports/` (niveau projet).

## Étape 3 : Comprendre l'Architecture Sous-Agent vs Skill

Voici comment les sous-agents et les skills fonctionnent ensemble :

| Composant | Objectif | Exemple |
|-----------|---------|---------|
| **Skill** | Collecte des données brutes sur une entreprise | "Générer un rapport pour Apple : produits, finances, direction, analystes" |
| **Sous-Agent** | Utilise les données du skill pour accomplir un objectif | "Obtenir des rapports pour Apple et Microsoft, évaluer les deux, recommander dans lequel investir" |

**Différence clé :**
- **Skill = outil** qui fait des recherches
- **Sous-Agent = décideur** qui utilise l'outil et applique la logique

Votre sous-agent de sélection d'actions va :
1. Invoquer le skill de rapport boursier pour chaque entreprise (2+ fois)
2. Évaluer les entreprises selon plusieurs catégories (finances, croissance, direction, sentiment)
3. Comparer les scores et recommander le meilleur investissement

## Étape 4 : Créer le Sous-Agent de Sélection d'Actions

Tapez cette commande :

```
/agents
```

Vous verrez l'interface des agents de Claude Code montrant les sous-agents existants (le cas échéant) et les options pour **Create**, **Edit** ou **Delete** des sous-agents.

Maintenant créez votre sous-agent :
- Sélectionnez **Create new subagent**
- Sélectionnez **Project**
- Sélectionnez **Generate with Claude (recommended)**
- Collez ce qui suit pour les instructions :
  ```
  Create a markdown file for a new subagent called stock-picker:
  - It takes two or more stocks
  - Uses the generate-stock-reports skill to do research
  - Score cards are created based on the categories of data collected
  - A final recommendation is given.
  ```
- Appuyez sur **Enter** sur **[Continue]** pour utiliser **All tools**
- Sélectionnez **Sonnet** pour le modèle
- Appuyez sur **Enter** pour choisir une couleur aléatoirement

## Étape 5 : Examiner ce que Vous Avez Construit (Point de Réflexion)

Pour ouvrir le fichier dans VS Code, cliquez sur **File > Open File...** et naviguez vers `.claude/agents/stock-picker.md`.

Ou vous pouvez demander à Claude :
```
Show me the stock-picker subagent file.
```
Claude affichera le fichier du sous-agent situé dans `.claude/agents/stock-picker.md`. Vous verrez :

Il y a un **frontmatter YAML** en haut :
```
---
name: stock-picker
description: Compares multiple companies for investment decisions...
skills: generate-stock-reports
---
```

Ce frontmatter (la section entre les marqueurs `---`) indique à Claude Code quand activer ce sous-agent et quels skills il peut utiliser.

Il y a un **prompt système** sous le frontmatter avec votre méthodologie d'évaluation.

**Confirmez ces éléments clés :**
- Le sous-agent a accès au skill `generate-stock-reports`
- Le prompt système explique la répartition des scores
- L'objectif du sous-agent est clair : comparer les entreprises et en recommander une

Vous pouvez modifier le fichier directement ou demander à Claude de le mettre à jour.

## Étape 6 : Tester le Sous-Agent

Maintenant testez votre sous-agent avec une vraie comparaison. Tapez :

```
Which is a better investment: Apple or Google?
```

Le sous-agent s'activera automatiquement en fonction de votre description.

## Étape 7 : Observer le Sous-Agent Travailler

Pendant que le sous-agent s'exécute, vous le verrez :
1. **Invoquer le skill deux fois** - Appeler le skill generate-stock-reports une fois pour Apple, puis pour Google
2. **Collecter des données** - Chaque appel du skill recherche sur le web et génère un rapport d'entreprise
3. **Évaluer les entreprises** - Applique la pondération 40/30/20/10 sur les catégories
4. **Générer la sortie** - Crée un tableau de comparaison et une recommandation

Cela peut prendre 2-3 minutes car la recherche web est impliquée.

## Étape 8 : Examiner la Sortie

Le sous-agent renvoie une analyse détaillée incluant :
- **Rapports individuels des entreprises** - Mises à jour produits, métriques financières, changements de direction, sentiment des analystes pour chaque action
- **Tableau de comparaison** - Scores numériques selon les catégories (Santé Financière, Potentiel de Croissance, Qualité de la Direction, Sentiment du Marché)
- **Recommandation finale** - Dans quelle action investir et pourquoi

Le sous-agent peut afficher cela dans le terminal ou générer un fichier markdown avec le rapport complet. Vous pouvez modifier le fichier du sous-agent pour personnaliser les pondérations des scores ou le format de sortie.

## Prochaines Étapes

Maintenant que vous avez un sous-agent de sélection d'actions fonctionnel, essayez ces extensions :

- **Comparer 3+ actions** : "Compare AAPL, MSFT, and GOOGL" pour voir comment le sous-agent gère plus d'options
- **Ajuster les pondérations** : Modifiez le fichier du sous-agent pour changer la répartition 40/30/20/10 (par exemple, mettez la croissance à 40% si vous préférez les actions de croissance)
- **Créer d'autres sous-agents** : Construisez un sous-agent "code-reviewer", "bug-hunter" ou "document-writer" pour différentes tâches

## Dépannage

- **Le sous-agent ne s'active pas** : Assurez-vous que votre demande mentionne la comparaison d'entreprises ou les décisions d'investissement. Essayez : "Use the stock-picker subagent to compare..."
- **Skill non trouvé** : Vérifiez que `.claude/skills/generate-stock-reports/SKILL.md` existe. Redémarrez Claude Code si vous venez de l'ajouter.
- **Scores incomplets** : Demandez au sous-agent de "continue" ou "explain the scores for each category in more detail"
- **Erreur lors de la création du sous-agent** : Vérifiez que le dossier `.claude/agents/` existe. Claude Code devrait le créer automatiquement.

## Vue d'Ensemble du Flux de Travail

- **Les sous-agents automatisent les flux de travail en plusieurs étapes** - Ils orchestrent les skills, appliquent la logique et fournissent des décisions
- **Les skills sont des outils réutilisables** - Un skill peut être utilisé par plusieurs sous-agents pour différents objectifs
- **Les prompts système définissent le comportement** - Des instructions claires et des critères d'évaluation rendent les sous-agents fiables
- **Les sous-agents maintiennent leur focus** - Chaque sous-agent a un objectif unique et clair (sélection d'actions, revue de code, etc.)
- **La composition permet l'évolutivité** - Construisez une bibliothèque de skills et de sous-agents qui fonctionnent ensemble

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 14 décembre 2025.
