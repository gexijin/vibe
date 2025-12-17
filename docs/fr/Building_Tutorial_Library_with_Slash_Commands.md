# Comment Claude Code m'a aidé à créer ces tutoriels

En décembre 2025, je me suis lancé dans la création d'une bibliothèque de tutoriels complète pour Claude Code. Mon objectif : des tutoriels pratiques et ciblés qui guident les débutants complets à travers des tâches réelles, étape par étape. Pas de théorie en masse. Pas de manuels de référence exhaustifs. Juste « faites ceci, puis cela, puis ceci » jusqu'à ce que vous ayez accompli quelque chose de concret.

Ce qui a commencé comme quelques fichiers de documentation a rapidement évolué en une plateforme d'apprentissage multilingue avec plus de 100 documents de tutoriels. Le secret ? Je ne les ai pas tous écrits manuellement. Au lieu de cela, j'ai créé un ensemble de commandes slash personnalisées (essentiellement des invites réutilisables) qui ont transformé Claude Code en une usine de documentation automatisée — une usine qui produit systématiquement des tutoriels dans mon style pratique et progressif.

## Le Défi

Créer des tutoriels prend du temps. Chacun nécessite une recherche des meilleures pratiques actuelles, une rédaction structurée adaptée aux débutants, un formatage cohérent, une validation de l'exactitude technique, une traduction en plusieurs langues, et une maintenance continue à mesure que les outils évoluent. Faire cela manuellement pour plus de 20 tutoriels dans plus de 3 langues prendrait des semaines.

## La Solution : Du Processus Manuel aux Commandes Slash Automatisées

L'intuition clé : **automatiser les flux de travail éprouvés, pas les théoriques**.

Je ne me suis pas assis pour concevoir des commandes slash à partir de zéro. Au lieu de cela, j'ai créé les premiers tutoriels manuellement par le biais d'invites interactives avec Claude, j'ai affiné le processus par itération, puis j'ai demandé à Claude de codifier le processus fonctionnel en une commande slash.

C'est exactement le modèle décrit dans mon [tutoriel sur les articles de recherche](./Writing_Research_Paper_Claude_Code.md) : parcourez le flux de travail manuellement, puis à la dernière étape, demandez à Claude de l'enregistrer en tant que commande réutilisable.

Le résultat a été cinq commandes slash spécialisées qui gèrent l'ensemble du cycle de vie des tutoriels.

### [`/tutorial`](./assets/commands/tutorial.md) - Le Générateur de Tutoriels

Née de la création de plusieurs tutoriels interactifs, cette commande capture le flux de travail éprouvé :

1. **Recherche** : Claude effectue des recherches sur le web pour obtenir des informations actuelles — pas de numéros de version obsolètes ni de méthodes dépréciées
2. **Planification** : Claude présente ce qu'il a appris, recommande une approche et décrit les principales étapes
3. **Itération** : Je révise le plan, je demande à Claude de réviser plusieurs fois jusqu'à satisfaction
4. **Rédaction** : Après approbation, Claude rédige en suivant des règles de formatage strictes :
   - Lien d'accueil en haut
   - Accroche engageante
   - Concepts clés
   - Instructions étape par étape avec des verbes d'action
   - Section de dépannage
   - Date de création
5. **Test** : Je teste moi-même les étapes dans un terminal séparé, je révise si nécessaire
6. **Peaufinage** : Parfois je modifie manuellement, parfois je demande à Claude de le faire

La commande impose une structure cohérente dans tous les tutoriels. Chaque tutoriel semble provenir du même auteur — parce qu'ils ont suivi le même processus systématique. J'ai généré plus de 20 tutoriels couvrant des sujets allant des opérations Git de base aux flux de travail Docker avancés.

### [`/review-tutorial`](./assets/commands/review-tutorial.md) - Le Robot de Contrôle Qualité

Voici quelque chose de remarquable : j'ai simplement demandé à Claude de « créer une commande slash pour examiner les tutoriels ». Aucune spécification détaillée. Claude a généré un flux de travail complet en trois phases avec plus de 30 critères de qualité organisés en catégories :

- **Qualité du Contenu** : titre, accroche, concepts clés, prérequis, flux des étapes, prochaines étapes, dépannage
- **Normes de Formatage** : lien d'accueil, titres d'étapes, puces, gras/backticks, blocs de code, paragraphes
- **Convivialité pour Débutants** : instructions basées sur les menus, différences de plateforme, cibles de clic exactes, pas de jargon
- **Exactitude Technique** : commandes correctes, interface utilisateur actuelle, estimations de temps réalistes
- **Qualité d'Écriture** : grammaire, terminologie cohérente, langage concis

La commande présente les résultats dans un rapport structuré, puis applique les corrections après approbation. Pourquoi était-ce nécessaire ? Deux raisons : Claude ne suit pas toujours strictement les règles de `/tutorial`, et la commande `/tutorial` elle-même a évolué à mesure que je créais plus de tutoriels. La commande de révision me permet de polir par lot les tutoriels antérieurs pour les conformer aux dernières normes.

### [`/translate-chinese`](./assets/commands/translate-chinese.md) et [`/translate-spanish`](./assets/commands/translate-spanish.md) - Le Moteur de Localisation

Les traductions japonaises sont venues en premier — et sans commande slash. J'ai simplement demandé à Claude Code de traduire tous les tutoriels en japonais dans une seule invite. Claude a automatiquement généré 8 sous-agents fonctionnant en parallèle, chacun gérant différents tutoriels simultanément. Les résultats étaient excellents, ce qui m'a donné confiance pour formaliser le processus en commandes slash pour le chinois et l'espagnol.

Encore une fois, j'ai simplement demandé à Claude de « créer une commande slash pour traduire les tutoriels en chinois » — aucune directive spécifique. Claude a généré un flux de travail en six phases avec des règles complètes :

- **Règles de Traduction** : Conserver les blocs de code, les termes techniques (Git, Docker, VS Code), les chemins de fichiers et les URL en anglais ; traduire le texte d'instruction, les titres et les explications
- **Directives Linguistiques** : Règles de ton et de style, traductions techniques courantes (Click = 点击, Install = 安装), conventions d'adresse formelle
- **Exigences de Formatage** : Lien d'accueil localisé, structure préservée, ponctuation correcte (。，！？ pour le chinois, ¿? ¡! pour l'espagnol)
- **Révision de Qualité** : Liste de vérification du flux naturel, terminologie cohérente, utilisation appropriée des caractères

Avec les commandes slash prêtes, j'ai demandé à Claude Code de traduire les 25 tutoriels en utilisant des sous-agents. La traduction complète — 50 nouveaux fichiers dans deux langues — n'a pris que 15 minutes.

Le résultat : 81 fichiers de tutoriels traduits dans les répertoires chinois, espagnol et japonais — tous maintenant une qualité et une structure cohérentes.

### [`/review-translation`](./assets/commands/review-translation.md) - L'Outil de Maintenance des Traductions

Les tutoriels évoluent. Les commandes changent. De nouvelles sections sont ajoutées. Cette commande maintient les traductions synchronisées grâce à un flux de travail en quatre phases :

1. **Lecture des Deux Versions** : Charger l'original anglais et la traduction côte à côte
2. **Comparaison et Mise à Jour** : Identifier les sections manquantes, le contenu obsolète, les commandes ou URL modifiées
3. **Révision de la Qualité** : Vérifier l'exactitude de la traduction, la qualité linguistique, la cohérence du formatage
4. **Rapport et Correction** : Présenter les résultats, obtenir l'approbation, appliquer les mises à jour

La révision de qualité est approfondie — pour le japonais, elle vérifie la formulation naturelle (pas mot à mot), le niveau de politesse approprié (forme です/ます), l'utilisation correcte des particules (は/が, を, に, で), et l'absence de surutilisation de katakana non naturel. Lorsque j'ai mis à jour les tutoriels anglais, j'ai pu rapidement propager les modifications à toutes les traductions tout en maintenant la qualité linguistique.

### Peaufiner les Traductions pour un Flux Naturel

Après avoir synchronisé les traductions avec les originaux anglais, j'ai ajouté une étape finale de peaufinage : éditer chaque document traduit individuellement pour la qualité linguistique, sans comparaison avec l'anglais. Cette étape se concentre uniquement sur la lecture naturelle du texte pour les locuteurs natifs.

L'intuition clé : **utiliser des invites dans la langue cible**. Au lieu de demander à Claude en anglais de « polir ce document japonais », j'ai utilisé ChatGPT pour écrire les invites en japonais, chinois ou espagnol. Cela a produit des résultats nettement meilleurs — Claude semblait penser plus naturellement dans cette langue lorsque les instructions étaient également dans cette langue.

Par exemple, pour peaufiner les documents chinois, j'ai utilisé :
« 修改 @docs/zh/ 目录下的中文文档。中文需要流畅、准确、言简意赅。提示词也要用中文。 Use subagents. » Pour l'espagnol : « Revisa los documentos en @docs/es/. El español debe ser fluido, preciso y conciso. Use subagents. » Pour le japonais : « @docs/ja/ のドキュメントを修正してください。日本語は流暢で正確、簡潔にしてください。Use subagents. »

De meilleurs modèles tels qu'Opus 4.5 semblent également aider. Cette étape de peaufinage a détecté des formulations maladroites qui n'étaient pas techniquement incorrectes mais qui ne semblaient pas naturelles. Combiné avec les sous-agents, j'ai pu peaufiner tous les plus de 25 documents dans chaque langue en une seule opération par lot.

## Passer à l'Échelle avec les Sous-Agents

Pour un travail vraiment parallèle, j'ai utilisé la fonctionnalité de sous-agent de Claude. Lors du peaufinage des traductions japonaises, j'ai lancé plusieurs agents de révision simultanément, traitant 19 fichiers avec des améliorations coordonnées.

La combinaison de commandes slash pour les flux de travail structurés et de sous-agents pour la parallélisation a créé un pipeline de documentation qui s'est étendu bien au-delà de ce que l'effort manuel pourrait réaliser.

## Les Résultats

En moins de deux semaines, j'ai créé plus de 20 tutoriels anglais couvrant des sujets de niveau débutant à intermédiaire, 81 tutoriels traduits dans 3 langues, une qualité constante grâce à des processus de révision automatisés, et une documentation maintenable avec des outils de synchronisation pour les traductions.

Tous les tutoriels suivent la même structure, le même style d'écriture et les mêmes conventions de formatage — parce qu'ils ont été générés par le même processus systématique.

## Leçons Clés

- **Commencez manuellement, puis automatisez.** Faites d'abord la tâche manuellement, affinez le processus, puis demandez à Claude de l'enregistrer en tant que commande.
- **Structurez les commandes comme des flux de travail multiphases.** Dites à Claude comment réfléchir au problème, pas seulement quoi faire.
- **Intégrez le contrôle qualité dans le processus.** Créez une commande de révision en parallèle de votre commande de génération.
- **Rendez les commandes collaboratives, pas autonomes.** Incluez des étapes d'approbation. Claude gère les parties fastidieuses ; vous prenez les décisions stratégiques.
- **Utilisez les sous-agents pour le traitement par lot.** Lors du traitement de nombreux documents, dites explicitement « Use subagents » dans votre invite. Appuyez d'abord sur Shift+Tab pour activer le mode d'acceptation automatique — les sous-agents ne demanderont pas de permissions, rendant le traitement parallèle fluide.

## Conclusion

La construction de cette bibliothèque de tutoriels m'a appris que l'automatisation ne consiste pas à retirer les humains du processus — il s'agit d'amplifier le jugement humain. Je n'ai pas écrit plus de 100 tutoriels manuellement, mais chacun d'entre eux reflète mes normes, ma structure et mon approbation.

Les commandes slash ont transformé Claude Code d'un assistant utile en une usine de documentation qui travaille sous ma direction, maintient mes normes et s'adapte à la taille de projet dont j'ai besoin.

Si vous avez des tâches de documentation répétitives, ne continuez pas à les faire manuellement. Créez la commande slash une fois, puis déployez-la des dizaines ou des centaines de fois.

C'est le pouvoir de l'automatisation systématique.

---

*Vous voulez voir les commandes slash que j'ai créées ? Consultez le [dossier commands](./assets/commands/). La bibliothèque complète de tutoriels est disponible sur le [site de documentation du projet](https://github.com/gexijin/vibe/tree/main/docs).*

---

**P.S.** Cet article de blog a lui-même été rédigé par Claude Code à travers des invites itératives :
1. « Examinez mon historique de commits et écrivez un article de blog sur la façon dont j'ai créé ces tutoriels, en soulignant mon utilisation de commandes slash pour automatiser. »
2. « Reflétez que la commande /tutorial a évolué à partir d'invites interactives manuelles d'abord. »
3. « Soulignez mon style de tutoriel : pratique, ciblé, étape par étape. »
4. « Ajoutez que les traductions japonaises sont venues en premier sans commandes slash, et Claude a utilisé 8 sous-agents en parallèle. »
5. « Ajoutez que Claude a écrit les commandes slash de traduction sans directives spécifiques, et l'utilisation de sous-agents. »
6. « Lien vers les commandes enregistrées dans docs/assets/commands. »
7. « Réécrivez avec moins de puces. »
8. « Lisez réellement les commandes slash et ajoutez des détails. »
9. « Résumez notre interaction. Ajoutez un P.S. sur la façon dont ce blog a été généré. »

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 15 décembre 2025.
