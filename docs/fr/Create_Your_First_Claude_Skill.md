---
title: "Créez Votre Première Compétence Claude"
lang: "fr"
---
[Accueil](./)

# Créez Votre Première Compétence Claude

Vous avez tapé manuellement `/stock-report AAPL` pour générer des rapports. Et si Claude pouvait décider automatiquement de créer un rapport boursier en fonction de votre conversation ? C'est le pouvoir des Compétences (Skills)—comme passer d'une boîte de vitesses manuelle à une transmission automatique qui passe les vitesses quand il le faut.

## Concepts Clés

- **Compétence (Skill)** - Une capacité invoquée par le modèle stockée dans `.claude/skills/` que Claude active automatiquement en fonction du contexte
- **Invoquée par le modèle (model-invoked)** - Claude décide quand utiliser la Compétence en lisant sa description, sans que vous tapiez une commande
- **Toujours une commande slash** - Vous pouvez aussi exécuter n'importe quelle Compétence vous-même en tapant `/nom-de-la-competence` (par exemple `/stock-report AAPL`). Si une Compétence et une commande slash portent le même nom, c'est la Compétence qui est utilisée
- **SKILL.md** - Le fichier principal contenant le frontmatter YAML (métadonnées) et les instructions pour Claude

## Ce Dont Vous Aurez Besoin

- Tutoriel [Créer des Commandes Slash Personnalisées](./Reuse_Prompts_via_Slash_Commands.md) terminé
- La commande slash `stock-report` de ce tutoriel
- VS Code installé
- 10-15 minutes

## Étape 1 : Accédez au Dossier du Projet

**Windows (PowerShell) :**
- Ouvrez **PowerShell** depuis le menu Démarrer
- Tapez :
  ```
  cd ~\Documents\test_claude
  ```

  Si le dossier n'existe pas, créez-le d'abord :
  ```
  mkdir ~\Documents\test_claude
  cd ~\Documents\test_claude
  ```

**Mac :**
- Ouvrez **Terminal** (Applications > Utilitaires)
- Tapez :
  ```bash
  cd ~/Documents/test_claude
  ```

  Si le dossier n'existe pas, créez-le d'abord :
  ```bash
  mkdir -p ~/Documents/test_claude
  cd ~/Documents/test_claude
  ```

## Étape 2 : Démarrez Claude Code

Tapez :
```
claude
```

Connectez-vous avec votre abonnement Claude en suivant le tutoriel d'installation ([Windows](Install_CLAUDE_Code_Win.md) | [Mac](Install_Claude_Code_MacOS.md)). Après vous être connecté, vous verrez un message de bienvenue et l'invite Claude Code.

## Étape 3 : Laissez Claude Modifier les Fichiers Sans Demander

Regardez la ligne d'état juste sous l'invite Claude Code :

- Si elle indique **auto mode on** ou **accept edits on**, tout est prêt
- Si elle indique **manual mode on**, appuyez sur **Shift+Tab** jusqu'à ce qu'elle indique **accept edits on**

Cela permet à Claude de créer et de modifier des fichiers sans demander la permission à chaque fois.

## Étape 4 : Demandez à Claude de Convertir la Commande Slash

Tapez ce prompt :
```
Convertis ma commande slash stock-report en une Compétence.
La Compétence devrait s'activer automatiquement quand je pose des questions sur des entreprises ou des actions.
```

Claude analyse votre commande slash existante et la convertit en Compétence dans `.claude/skills/stock-report/`.

**Ce qui se passe :** Claude crée une nouvelle structure de dossier avec `SKILL.md` contenant le frontmatter YAML qui indique à Claude quand utiliser automatiquement cette Compétence.

## Étape 5 : Examinez la Structure de la Compétence

Ouvrez VS Code et visualisez le projet :
- Cliquez sur **File > Open Folder**
- Sélectionnez `Documents/test_claude`
- Dans le panneau **Explorer** de VS Code (à gauche), accédez à `.claude/skills/stock-report/`
- Cliquez sur `SKILL.md` pour l'ouvrir

Remarquez la structure :
```yaml
---
name: stock-report
description: Generates reports on companies... Use when users ask about stocks, companies, or ticker symbols.
---

[Rest of the instructions]
```

Le champ `description` est la clé—il indique à Claude exactement quand activer cette Compétence automatiquement.

## Étape 6 : Testez la Compétence (Sans Taper de Commande)

Assurez-vous d'abord que Claude Code a chargé la nouvelle Compétence. Tapez :
```
/reload-skills
```
Claude Code indique combien de Compétences sont disponibles. Maintenant, au lieu de taper `/stock-report AAPL`, posez simplement une question naturelle :
```
Que se passe-t-il avec Apple ces derniers temps ?
```

**La différence clé :** Vous n'avez pas tapé de commande. Claude lit votre question, reconnaît que vous posez une question sur une entreprise, vérifie les descriptions des Compétences et décide automatiquement d'utiliser la Compétence stock-report.

Observez Claude travailler—il devrait générer le même rapport complet que vous avez vu auparavant.

## Étape 7 : Comparez les Deux Approches

**Commande Slash (Manuelle) :**
```
/stock-report AAPL
```
- Vous dites explicitement à Claude quoi faire
- Identique à chaque fois
- Bon pour les tâches répétitives et prévisibles

**Compétence (Automatique) :**
```
Parle-moi des récents développements de Tesla
```
ou
```
Je pense à investir dans Microsoft
```
ou
```
Que fait NVIDIA en ce moment ?
```
- Claude décide d'utiliser ou non la Compétence
- Conversation plus naturelle
- Bon pour les flux de travail complexes que Claude gère pour vous

## Étape 8 : Testez les Cas Limites

Essayez des questions qui NE devraient PAS déclencher la Compétence de rapport boursier :
```
Comment installer Python ?
```

Claude répond normalement sans invoquer la Compétence.

Maintenant essayez une question qui DEVRAIT la déclencher :
```
Compare Google et Meta
```

Claude devrait utiliser la Compétence deux fois—une fois pour Google, une fois pour Meta.

## Étape 9 : Modifiez la Description de la Compétence (Optionnel)

Rendons la Compétence plus sélective. Demandez à Claude :
```
Mets à jour la Compétence stock-report pour qu'elle ne s'active que quand je mentionne explicitement
« analyser » ou « rapport » avec un nom d'entreprise.
```

Claude met à jour le champ `description` dans `SKILL.md`. Tapez `/reload-skills` pour que Claude Code prenne en compte la modification, puis testez la différence :
```
Que fait Apple ?
```
(Pourrait ne pas déclencher la Compétence maintenant)

```
Analyse Apple
```
(Devrait déclencher la Compétence)

## Prochaines Étapes

Maintenant que vous comprenez les Compétences, créez-en d'autres pour vos flux de travail :

- **Compétence de recherche** - S'active automatiquement lorsque vous posez des questions nécessitant une recherche web
- **Compétence de revue de code** - S'active lorsque vous mentionnez des bugs, des anomalies ou des problèmes de code
- **Compétence de notes de réunion** - S'active lorsque vous collez des transcriptions de réunions ou mentionnez des résumés

Le principe : Définissez quand Claude devrait automatiquement aider, pas seulement des raccourcis que vous déclenchez manuellement.

## Dépannage

- **La Compétence ne s'active pas :** Vérifiez le champ `description` dans `SKILL.md`—il doit inclure des mots déclencheurs liés à votre question
- **La Compétence s'active trop souvent :** Précisez davantage dans la description quand l'utiliser
- **Impossible de trouver le dossier de la Compétence :** Les Compétences sont dans `.claude/skills/` (dossier caché : l'Explorateur de VS Code l'affiche ; sinon, dans l'**Explorateur de fichiers** de Windows, activez **Affichage > Afficher > Éléments masqués** ; dans le **Finder** sur Mac, appuyez sur **Cmd+Maj+.** pour l'afficher)
- **Les modifications de SKILL.md ne fonctionnent pas :** Les Compétences se rechargent généralement automatiquement lorsqu'elles sont modifiées. Si le dossier `.claude/skills/` a été créé pendant cette session, tapez `/reload-skills` (ou redémarrez Claude Code). Si cela ne fonctionne toujours pas, vérifiez le formatage YAML

## Aperçu du Flux de Travail

- **Les commandes slash** sont des raccourcis que vous tapez manuellement (comme des signets)
- **Les Compétences** sont des capacités que Claude découvre et utilise automatiquement (comme un assistant qui connaît vos préférences)
- **Les descriptions de Compétences** agissent comme des instructions indiquant à Claude : « Utilise-moi quand l'utilisateur dit X »
- **Les deux peuvent coexister** - Utilisez les commandes slash pour les tâches rapides et répétitives ; utilisez les Compétences pour les flux de travail complexes
- **Les Compétences passent mieux à l'échelle** - Vous n'avez pas besoin de mémoriser les noms de commandes ; Claude décide en fonction du contexte

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 13 décembre 2025.
