---
title: "Rédiger un article de recherche avec Claude Code"
lang: "fr"
---
[Accueil](./)

# Rédiger un article de recherche avec Claude Code

Rédigez des articles de recherche en utilisant Claude Code comme assistant pour la recherche, le brainstorming, la planification, la rédaction et l'édition. Ensuite, automatisez ce processus en créant un modèle de commande slash. Consultez un [exemple d'article](./example_paper.md) créé avec ce workflow.

## Concepts clés

- **Workflow** - Recherche → Brainstorming → Recherche ciblée → Plan → Brouillon → Révision manuelle → Polissage avec l'IA → Ajout du résumé → Amélioration du titre → Vérification des références → Relecture avec l'IA
- **Assistant IA** - L'humain prend les décisions clés tandis que l'IA effectue le travail fastidieux
- **Claude Code** - Système d'IA agentique qui effectue des recherches sur le web, organise la recherche et rédige du contenu à travers de simples requêtes
- **Commande slash** - Un prompt personnalisé et détaillé qui peut être réutilisé dans Claude Code

## Ce dont vous aurez besoin

- Avoir terminé [Claude Code dans VS Code sur Windows](./Claude_Code_in_VS_Code_Win.md) ou [Claude Code dans VS Code sur Mac](./Claude_Code_in_VS_Code_Mac.md)
- 30 à 40 minutes

## Étape 1 : Créer un dossier de projet

Créez un dossier pour votre article de recherche :

- Ouvrez l'**Explorateur de fichiers** (Windows) ou le **Finder** (Mac)
- Naviguez vers **Documents**
- Créez un nouveau dossier appelé `test_claude`

Tout ce qui concerne ce projet se passe dans ce dossier.

## Étape 2 : Démarrer VS Code
Pour Windows :
- Cliquez sur le **bouton Démarrer de Windows** (coin inférieur gauche de votre écran)
- Tapez `Visual Studio Code` ou `VS Code` dans la zone de recherche
- Cliquez sur **Visual Studio Code** lorsqu'il apparaît dans les résultats de recherche
- VS Code s'ouvre avec un onglet de bienvenue - vous pouvez fermer cet onglet

Pour Mac :
- Ouvrez le **Finder** et allez dans **Applications**
- Trouvez **Visual Studio Code** et double-cliquez dessus
- Si vous voyez un avertissement « Visual Studio Code est une application téléchargée depuis Internet », cliquez sur **Ouvrir**
- VS Code s'ouvre avec un onglet de bienvenue - vous pouvez fermer cet onglet

## Étape 3 : Ouvrir le dossier dans VS Code
Pour Windows :
- Cliquez sur **File** dans la barre de menu, puis sur **Open Folder**
- Naviguez vers le dossier `test_claude` dans **Documents** et sélectionnez-le
- Cliquez sur **Select Folder**. VS Code se recharge avec votre dossier `test_claude`
- Si on vous demande « Do you trust the authors? », cliquez sur **Yes, I trust the authors**

Pour Mac :
- Dans VS Code, cliquez sur **File** dans la barre de menu, puis sur **Open Folder**
- Naviguez jusqu'au dossier `test_claude` et sélectionnez-le
- Cliquez sur **Open**
- Si on vous demande « Do you trust the authors? », cliquez sur **Yes, I trust the authors**

## Étape 4 : Démarrer Claude Code

- Ouvrez un terminal : cliquez sur **Terminal** dans le menu principal de VS Code, puis sur **New Terminal**
- Dans le panneau du terminal, tapez :
  ```
  claude
  ```

Connectez-vous avec votre abonnement Claude en suivant le tutoriel d'installation ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Après vous être connecté, vous verrez un message de bienvenue et l'invite Claude Code.

## Étape 5 : Recherche initiale

Demandez à Claude de rechercher votre sujet. Copiez et collez ce prompt dans Claude Code, en remplaçant le sujet par le vôtre :

```
J'écris un article de recherche d'environ 1 000 mots sur l'adoption de l'IA en milieu de travail.
Recherche des données récentes (des deux dernières années) sur :
- Les gains de productivité grâce aux outils d'IA
- Les préoccupations et statistiques sur le déplacement d'emplois
- Des études de cas réelles d'entreprises

Exigences :
- Priorise les recherches évaluées par les pairs et les rapports d'industrie crédibles
- Évite les anecdotes et les articles d'opinion
- Liste chaque source avec un résumé de 1-3 phrases
- Regroupe les sources par sujet

Enregistre sous general_research.md
```

Claude effectue des recherches sur le web et organise les résultats dans un fichier appelé `general_research.md`. Cela peut prendre une minute ou deux. Une fois terminé, demandez un résumé :

```
Donne-moi un bref résumé.
```

Examinez le résumé de Claude pour obtenir un aperçu rapide du paysage de la recherche.

## Étape 6 : Lire les sources
Lisez le document de recherche et cliquez sur les sources originales pour vérifier les informations :

1. Cliquez sur `general_research.md` dans le panneau **Explorer** sur la gauche
2. Prévisualisez le document formaté : cliquez avec le bouton droit sur l'onglet `general_research.md` et sélectionnez **Open Preview**
3. Cliquez sur les liens des sources pour lire les articles et études originaux

## Étape 7 : Brainstorming de votre angle

Demandez à Claude de vous aider à faire un brainstorming :

```
En fonction de cette recherche, suggère 3-4 angles que je pourrais prendre pour cet article.
```

Examinez les angles et choisissez celui qui vous intéresse le plus.

## Étape 8 : Recherche ciblée

Maintenant que vous avez votre angle, demandez à Claude une recherche ciblée :

```
Je veux me concentrer sur [l'angle choisi]. Recherche des données plus spécifiques
et des exemples qui soutiennent cette perspective. Enregistre sous focused_research.md
```

Claude trouve des informations ciblées.

## Étape 9 : Créer votre plan

Demandez à Claude de créer un plan basé sur votre angle choisi :

```
Donne-moi 3 options pour un bref plan de mon article basé sur la recherche
ciblée et mon angle choisi. Utilise des puces pour le flux narratif.
Enregistre sous outlines.md
```

Examinez les plans dans `outlines.md` et demandez à Claude de l'ajuster si nécessaire (par exemple, « Fais en sorte que la section 2 se concentre davantage sur les études de cas » ou « Ajoute une section sur les limites »).

## Étape 10 : Rédiger l'article

Sélectionnez votre plan et demandez à Claude de rédiger le brouillon complet :

```
J'aime le plan n°2 [l'option choisie].

Rédige un article de recherche d'environ 1 000 mots basé sur le plan et la recherche.

Structure :
- Introduction : Accroche, contexte, énoncé de thèse
- Corps : 2-3 sections avec arguments, statistiques et exemples
- Conclusion : Résumé et implications

Style :
- Phrases claires et concises (15-20 mots en moyenne)
- Voix active, ton analytique
- Statistiques intégrées à la prose (pas de listes à puces)
- Transitions fluides entre les paragraphes

Citations :
- Utilise des références numérotées [1], [2], etc. après les affirmations
- Inclus 5-15 références
- Ajoute une section Références à la fin

Enregistre sous paper.md
```

Claude rédige le brouillon.

## Étape 11 : Réviser manuellement

Ouvrez `paper.md` dans votre éditeur de texte. Lisez attentivement et apportez vos propres révisions :
- Ajoutez votre voix personnelle et vos idées
- Ajustez les arguments pour qu'ils correspondent à votre réflexion
- Corrigez toute formulation maladroite
- Assurez-vous que les citations sont exactes

Enregistrez vos modifications dans l'éditeur.

## Étape 12 : Polir avec l'IA

Demandez à Claude d'améliorer des sections spécifiques :

```
Rends l'introduction plus engageante avec une accroche captivante.
```

## Étape 13 : Ajouter un résumé

Demandez à Claude d'ajouter une courte synthèse au début :

```
Ajoute un résumé au début de l'article. Écris 2-3 phrases courtes
qui résument l'article.
```

Claude ajoutera le résumé. Examinez et modifiez pour vous assurer qu'il capture avec précision l'essence de votre article.

## Étape 14 : Améliorer le titre

Demandez à Claude de vous donner quelques options pour le titre :

```
Donne-moi quelques options pour le titre. Rends-le plus attrayant.
```

Sélectionnez un titre. Ajoutez votre propre touche :

```
J'aime l'option n°2 [votre choix]. Modifie le fichier.
```

## Étape 15 : Vérifier les références (optionnel)
Demandez à Claude de vérifier que vos citations sont cohérentes et complètes :
```
Vérifie toutes les références dans mon article :
- Vérifie que chaque numéro de citation [1], [2], etc. a une référence correspondante
- Vérifie que chaque référence de la liste est réellement citée dans l'article
- Vérifie que les noms d'auteurs et les titres sont cohérents
- Vérifie que les données et exemples cités apparaissent dans la source
```

Remarque : Claude ne peut vérifier que les sources accessibles publiquement. Pour les articles payants, vérifiez manuellement que vos citations correspondent à ce que vous avez lu.

## Étape 16 : Relire avec l'IA

Demandez à Claude de faire une relecture finale :

```
Fais une relecture finale de l'article :
- Corrige toutes les erreurs d'orthographe et de grammaire
- Assure un formatage cohérent tout au long
- Vérifie le flux et les transitions
```

Examinez les modifications de Claude.

**Exporter vers Word :** Dans VS Code, cliquez avec le bouton droit sur l'onglet `paper.md` et sélectionnez **Open Preview**. Cliquez à l'intérieur du volet de prévisualisation, puis cliquez sur **Edit > Select All** et **Edit > Copy**. Collez dans Microsoft Word—le formatage sera conservé.

## Étape 17 : Créer une commande slash pour de futurs articles

Enregistrez ce workflow comme une commande slash réutilisable pour votre prochain article de recherche :

```
Crée une commande slash appelée /research-paper qui me guide à travers
tout ce workflow. Enregistre-la pour que je puisse l'utiliser pour de futurs articles de recherche sur divers sujets.
```

Claude créera une commande slash personnalisée, généralement dans votre dossier `.claude/commands/` (ou `.claude/skills/research-paper/`). C'est un fichier Markdown contenant un prompt. Avant de l'utiliser pour la première fois, tapez `/reload-skills` (ou quittez Claude Code et relancez-le) pour que la nouvelle commande soit chargée. Ensuite, vous pouvez démarrer votre prochain article de recherche en tapant simplement `/research-paper [votre sujet]` !

## Étape 18 : Obtenir des commentaires

Les LLM n'ont pas de mémoire. Pour chaque réponse, nous devons envoyer toutes nos conversations précédentes de la session de chat pour le contexte. À mesure que l'interaction s'allonge, nous devons être conscients de la longueur du contexte. Si la suite n'a pas de rapport avec ce qui précède, ou si nous pouvons repartir d'un contexte plus propre, mieux vaut recommencer à zéro.

Effacez la mémoire de Claude pour obtenir des commentaires sur votre article. Tapez :

```
/clear
```

Cela supprime tout l'historique de conversation, donc Claude lira votre article avec un regard neuf. Maintenant, demandez des commentaires :

```
Lis paper.md et donne-moi des commentaires honnêtes.
```

Claude critiquera votre article sans être influencé par le fait de l'avoir écrit. Apportez les révisions finales en fonction des commentaires.


## Le workflow complet

1. **Créer un dossier** - Configurez votre dossier de projet dans Documents
2. **Ouvrir dans VS Code** - Ouvrez le dossier dans VS Code
3. **Démarrer Claude Code** - Lancez Claude Code depuis le terminal
4. **Rechercher** - Claude recherche des informations générales sur votre sujet
5. **Lire les sources** - Examinez la recherche dans votre éditeur de texte
6. **Brainstorming** - Choisissez votre angle/perspective
7. **Recherche ciblée** - Claude trouve des données ciblées pour votre angle choisi
8. **Planifier** - Claude crée des options de plan basées sur votre perspective
9. **Rédiger** - Claude rédige l'article complet avec références
10. **Réviser manuellement** - Vous ajoutez votre voix et apportez des modifications
11. **Polir avec l'IA** - Claude améliore des sections spécifiques
12. **Ajouter un résumé** - Claude rédige une synthèse
13. **Améliorer le titre** - Claude suggère des options de titre, vous personnalisez
14. **Vérifier les références** - (Optionnel) Claude vérifie toutes les citations
15. **Relire avec l'IA** - Claude corrige les erreurs et améliore le flux
16. **Créer une commande slash** - Enregistrez le workflow pour de futurs articles
17. **Obtenir un avis neuf** - Effacez la mémoire pour une critique impartiale

## Prochaines étapes

Maintenant que vous avez la commande slash `/research-paper`, essayez d'écrire plus d'articles :

- **Technologie :** `/research-paper "Impact des réseaux sociaux sur la santé mentale des adolescents"`
- **Affaires :** `/research-paper "Productivité du télétravail"`
- **Science :** `/research-paper "Éthique de l'édition génique CRISPR"`
- **Format :** Demandez à Claude : `Donne-moi l'article au format LaTeX`

La commande slash vous guidera automatiquement à travers tout le workflow ! N'oubliez pas d'effacer la mémoire lorsque vous changez de sujet.

## Dépannage

- **Les résultats de recherche de Claude semblent obsolètes :** Demandez une période précise, par exemple « recherche des données des deux dernières années sur [sujet] »
- **Le brouillon est trop long/court :** Dites à Claude : « Fais en sorte que ce soit environ 1 000 mots »
- **Impossible de trouver les fichiers :** Dans le terminal, tapez `ls` pour lister tous les fichiers du dossier actuel

## Ce que vous pouvez demander à Claude

- « Recherche des statistiques plus récentes sur [sujet] » - Trouver des données plus récentes
- « Résume les arguments clés de cet article » - Obtenir un aperçu
- « Rends la conclusion plus persuasive » - Améliorer des sections spécifiques
- « Cite toutes les sources au format APA » - Formater les références

Claude gère la recherche et la rédaction par langage naturel—aucune commande à mémoriser !

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 9 décembre 2025.
