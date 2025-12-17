[Accueil](./)

# Créez Votre Première Compétence Claude

Vous avez tapé manuellement `/stock-report AAPL` pour générer des rapports. Et si Claude pouvait décider automatiquement de créer un rapport boursier en fonction de votre conversation ? C'est le pouvoir des Compétences (Skills)—comme passer d'une boîte de vitesses manuelle à une transmission automatique qui change les vitesses selon les besoins.

## Concepts Clés

- **Skill** - Une capacité invoquée par le modèle stockée dans `.claude/skills/` que Claude active automatiquement en fonction du contexte
- **Model-invoked** - Claude décide quand utiliser la Compétence en lisant sa description, sans que vous tapiez une commande
- **SKILL.md** - Le fichier principal contenant le frontmatter YAML (métadonnées) et les instructions pour Claude

## Ce Dont Vous Aurez Besoin

- Tutoriel [Create Custom Slash Commands](./Reuse_Prompts_via_Slash_Commands.md) terminé
- La commande slash `stock-report` de ce tutoriel
- VS Code installé
- 10-15 minutes

## Étape 1 : Accédez au Dossier du Projet

**Windows (WSL) :**
- Ouvrez **Ubuntu** depuis le menu Démarrer
- Tapez :
  ```bash
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  ```
  Remplacez `YOUR_USERNAME` par votre nom d'utilisateur Windows

  Si le dossier n'existe pas, créez-le d'abord :
  ```bash
  mkdir -p /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
  cd /mnt/c/Users/YOUR_USERNAME/Documents/test_claude
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

Claude Code démarre et affiche le message de bienvenue.

## Étape 3 : Activez l'Approbation Automatique pour les Modifications

Appuyez sur `Ctrl+E` (Windows/Linux) ou `Cmd+E` (Mac) pour activer le mode d'approbation automatique des modifications.

Cela permet à Claude de créer et de modifier des fichiers sans demander la permission à chaque fois.

## Étape 4 : Demandez à Claude de Convertir la Commande Slash

Tapez cette invite :
```
Convertis ma commande slash stock-report en une Compétence appelée generate-stock-reports.
La Compétence devrait s'activer automatiquement quand je pose des questions sur des entreprises ou des actions.
```

Claude analyse votre commande slash existante et la convertit en Compétence dans `.claude/skills/stock-report/`.

**Ce qui se passe :** Claude crée une nouvelle structure de dossier avec `SKILL.md` contenant le frontmatter YAML qui indique à Claude quand utiliser automatiquement cette Compétence.

## Étape 5 : Examinez la Structure de la Compétence

Ouvrez VS Code et visualisez le projet :
- Cliquez sur **File > Open Folder**
- Sélectionnez `Documents/test_claude`
- Dans l'explorateur de fichiers, accédez à `.claude/skills/stock-report/`
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

Au lieu de taper `/stock-report AAPL`, posez simplement une question naturelle :
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

Claude met à jour le champ `description` dans `SKILL.md`. Testez la différence :
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

- **Research Skill** - S'active automatiquement lorsque vous posez des questions nécessitant une recherche web
- **Code Review Skill** - S'active lorsque vous mentionnez des bugs, des problèmes ou des problèmes de code
- **Meeting Notes Skill** - S'active lorsque vous collez des transcriptions de réunions ou mentionnez des résumés

Le principe : Définissez quand Claude devrait automatiquement aider, pas seulement des raccourcis que vous déclenchez manuellement.

## Dépannage

- **La Compétence ne s'active pas :** Vérifiez le champ `description` dans `SKILL.md`—il doit inclure des mots déclencheurs liés à votre question
- **La Compétence s'active trop souvent :** Rendez la description plus spécifique sur quand l'utiliser
- **Impossible de trouver le dossier de la Compétence :** Les Compétences sont dans `.claude/skills/` (dossier caché—activez « Afficher les fichiers cachés » dans votre explorateur de fichiers)
- **Les modifications de SKILL.md ne fonctionnent pas :** Les Compétences se chargent automatiquement lorsqu'elles sont modifiées—aucun redémarrage nécessaire. Si cela ne fonctionne toujours pas, vérifiez le formatage YAML

## Aperçu du Flux de Travail

- **Les commandes slash** sont des raccourcis que vous tapez manuellement (comme des signets)
- **Les Compétences** sont des capacités que Claude découvre et utilise automatiquement (comme un assistant qui connaît vos préférences)
- **Les descriptions de Compétences** agissent comme des instructions indiquant à Claude : « Utilise-moi quand l'utilisateur dit X »
- **Les deux peuvent coexister** - Utilisez les commandes slash pour les tâches rapides et répétitives ; utilisez les Compétences pour les flux de travail complexes
- **Les Compétences évoluent mieux** - Vous n'avez pas besoin de mémoriser les noms de commandes ; Claude décide en fonction du contexte

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 13 décembre 2025.
