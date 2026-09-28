---
title: "Vibe Coding d'un Suivi de Budget dans Excel avec Claude Code"
lang: "fr"
---
[Accueil](./)

# Vibe Coding d'un Suivi de Budget dans Excel avec Claude Code

Le vibe coding ressemble à une conversation avec votre ordinateur : vous décrivez le résultat souhaité, Claude Code le construit, vous testez et affinez. Ce n'est pas de la magie ; c'est une nouvelle façon de travailler où vous guidez la vision et l'IA gère la mécanique du tableur : formules, mise en forme et graphiques. Ce tutoriel vous guide dans la création d'un vrai suivi de budget à plusieurs feuilles en utilisant uniquement des requêtes en langage naturel.

## Concepts Clés

- **[Claude Code](https://code.claude.com/)** - Assistant de codage IA qui écrit, modifie et corrige des fichiers en fonction de vos demandes en langage naturel
- **Classeur à plusieurs feuilles** - Un seul fichier `.xlsx` contenant plusieurs onglets (Revenus, Dépenses, Synthèse) qui se référencent les uns les autres à l'aide de formules
- **Raffinement itératif** - Le modèle central du vibe coding : décrire → tester → affiner → valider les versions fonctionnelles

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Use Claude Code with Excel in VS Code](./Excel_Coding_VS_Code_Guide)
- Avoir terminé [Use GitHub Desktop with Claude Code](./GitHub_Desktop_Claude_Code_Workflow)
- 25-30 minutes

## Étape 1 : Créer un Nouveau Dépôt GitHub

- Ouvrez GitHub Desktop
- Cliquez sur **File > New Repository**
- Remplissez les détails :
  - **Name :** `budget-dashboard`
  - **Description :** `Suivi de budget personnel créé avec le vibe coding`
  - **Local Path :** Choisissez un emplacement (par exemple, Documents ou dossier de travail)
  - Cochez **Initialize this repository with a README**
- Cliquez sur **Create Repository**
- Cliquez sur **Publish repository** en haut
- Décochez **Keep this code private** si vous voulez qu'il soit public (optionnel)
- Cliquez sur **Publish Repository**

Vous disposez maintenant d'un dépôt Git local et d'une sauvegarde sur GitHub.

## Étape 2 : Ouvrir le Projet dans VS Code

- Ouvrez VS Code
- Cliquez sur **File > Open Folder**
- Sélectionnez votre dossier `budget-dashboard`
- Cliquez sur **Select Folder** (Windows) ou **Open** (Mac)
- Si ce n'est pas déjà fait, installez l'extension **Spreadsheet Viewer** par MESCIUS (anciennement **Excel Viewer** par GrapeCity) pour pouvoir afficher les feuilles de calcul sans quitter VS Code. Recherchez son identifiant, `GrapeCity.gc-excelviewer`, dans le panneau Extensions pour trouver la bonne

## Étape 3 : Démarrer Claude Code

- Cliquez sur **Terminal > New Terminal**
- Tapez cette commande pour démarrer Claude Code :

```bash
claude
```

- Connectez-vous si on vous le demande, puis attendez le message de bienvenue de Claude

Claude Code est maintenant en cours d'exécution et prêt à recevoir vos demandes.

## Étape 4 : Premier Vibe - Construire les Feuilles Revenus et Dépenses

Au lieu de construire une feuille de calcul cellule par cellule, décrivez simplement ce que vous voulez.

- Dans le terminal Claude Code, tapez :

```
Crée une feuille de calcul appelée budget.xlsx avec deux feuilles : « Revenus » et « Dépenses ». Revenus doit avoir les colonnes Source, Mois et Montant, avec 3 exemples de sources de revenus sur 2 mois. Dépenses doit avoir les colonnes Catégorie, Mois et Montant, avec 6 exemples de catégories (comme Loyer, Courses, Transport, Charges, Loisirs, Épargne) sur les mêmes 2 mois. Ajoute une ligne Total en bas de chaque feuille à l'aide de formules SUM.
```

- Appuyez sur Entrée
- Regardez Claude écrire et exécuter un script Python qui construit le classeur, puis le recalcule pour que les totaux affichent de vrais nombres
- Ouvrez `budget.xlsx` dans l'onglet Spreadsheet Viewer et parcourez les deux feuilles

**Enregistrez votre progression :** Demandez à Claude de valider en utilisant Git, ou faites-le vous-même depuis GitHub Desktop :
```
Valide ces modifications.
```

## Étape 5 : Deuxième Vibe - Ajouter une Feuille de Synthèse

Avant de créer des graphiques, reliez les deux feuilles entre elles.

- Dans le terminal Claude Code, tapez :

```
Ajoute une troisième feuille appelée « Synthèse » à budget.xlsx. Elle doit afficher le Total des revenus, le Total des dépenses et l'Épargne nette (Revenus moins Dépenses), chacun calculé avec des formules qui font référence aux feuilles Revenus et Dépenses - pas avec des nombres saisis en dur.
```

- Appuyez sur Entrée
- Claude met à jour le classeur et le recalcule
- Ouvrez l'onglet **Synthèse** et cliquez sur la cellule Épargne nette pour vérifier qu'il s'agit d'une formule faisant référence aux autres feuilles

**Enregistrez votre progression :** Demandez à Claude de valider, ou utilisez GitHub Desktop.

## Étape 6 : Troisième Vibe - Ajouter des Graphiques

Les nombres sont utiles, mais les graphiques racontent l'histoire en un coup d'œil.

- Dans le terminal Claude Code, tapez :

```
Ajoute à la feuille Dépenses un graphique en secteurs montrant la part totale de chaque catégorie dans les dépenses. Ajoute à la feuille Synthèse un graphique en barres comparant le Total des revenus et le Total des dépenses pour chaque mois.
```

- Appuyez sur Entrée
- Claude ajoute les deux graphiques et recalcule le fichier
- Rouvrez `budget.xlsx` dans Spreadsheet Viewer (ou actualisez l'onglet) et vérifiez que les nouveaux graphiques apparaissent dans les deux feuilles

## Étape 7 : Quatrième Vibe - Mettre en Évidence les Catégories Hors Budget

Rendez les problèmes visibles en un coup d'œil au lieu de les chercher parmi les nombres.

- Dans le terminal Claude Code, tapez :

```
Dans la feuille Dépenses, ajoute une mise en forme conditionnelle pour que toute dépense supérieure à $500 sur un seul mois soit surlignée en rouge, et toute dépense inférieure à $100 soit surlignée en vert.
```

- Appuyez sur Entrée
- Rouvrez le fichier et vérifiez la feuille Dépenses : les cellules devraient maintenant être colorées en fonction de leur valeur

Si quelque chose ne semble pas correct, notez ce que vous voyez et décrivez-le à Claude pour qu'il le corrige.

## Étape 8 : Cinquième Vibe - Ajouter une Liste Déroulante de Catégories

Rendez la feuille plus facile à compléter sans fautes de frappe.

- Dans le terminal Claude Code, tapez :

```
Ajoute une validation des données à la colonne Catégorie de la feuille Dépenses pour qu'elle n'accepte que les valeurs d'une liste déroulante contenant les catégories existantes, plus « Autre ». Ajoute deux lignes vides en bas, prêtes pour de nouvelles saisies.
```

- Appuyez sur Entrée
- Ouvrez le fichier, cliquez dans l'une des cellules Catégorie vides et vérifiez qu'une flèche de liste déroulante apparaît avec votre liste de catégories

## Étape 9 : Réviser et Valider

Avant de valider, examinez ce que Claude a construit.

- Dans Spreadsheet Viewer, parcourez les trois feuilles : Revenus, Dépenses, Synthèse
- Vous n'avez pas besoin de comprendre chaque formule, mais ayez une idée de la structure
- Ouvrez GitHub Desktop
- Vous verrez `budget.xlsx` listé comme fichier modifié
- Dans le champ **Summary** en bas à gauche, tapez :

```
Ajout de graphiques, d'une mise en forme conditionnelle et d'une liste déroulante de catégories au suivi de budget
```

- Cliquez sur **Commit to main**
- Cliquez sur **Push origin** pour sauvegarder sur GitHub

Vous avez enregistré une version complète et fonctionnelle de votre suivi de budget !

## Étape 10 : Itérer et Améliorer

Le vibe coding brille lorsque vous itérez. Essayez d'ajouter des fonctionnalités en les décrivant :

**Exemples de demandes à Claude :**

- « Ajoute une ligne Objectif d'épargne à la feuille Synthèse montrant la progression vers un objectif d'épargne de $500/mois »
- « Ajoute une quatrième feuille qui affiche une comparaison d'une année sur l'autre quand j'aurai ajouté plus de mois de données »
- « Change les couleurs du graphique en secteurs pour un thème bleu et gris »
- « Ajoute une note expliquant chaque formule pour que je puisse apprendre ce qu'elles font »
- « Crée un deuxième classeur appelé household_budget.xlsx pour une famille de quatre personnes avec plus de catégories »

Après chaque fonctionnalité réussie :
- Ouvrez le fichier et vérifiez-le dans Spreadsheet Viewer
- Si cela fonctionne, validez avec GitHub Desktop
- Si quelque chose semble incorrect, décrivez-le à Claude et demandez-lui de le corriger
- Une fois corrigée, validez la version fonctionnelle

**Principes clés :**

- **Décrivez les résultats, pas l'implémentation** - Dites « surligne les dépenses supérieures à $500 » et non « utilise une mise en forme conditionnelle avec une CellIsRule »
- **Itérez rapidement** - Tester → affiner → tester → affiner
- **Validez les versions fonctionnelles** - Enregistrez chaque succès avant d'essayer de nouvelles fonctionnalités
- **Acceptez les échecs** - Si une formule ou un graphique ne sort pas correctement, décrivez simplement le problème et demandez à Claude de le corriger
- **Restez aux commandes** - Vous décidez de ce que le suivi doit afficher et du moment où il est suffisamment bon

À chaque fois, suivez le modèle : décrire → vérifier le fichier → itérer → valider.

## Prochaines Étapes

- **Appliquez-le à vos propres finances** - Demandez à Claude de reconstruire le suivi autour de vos vraies catégories de revenus et de dépenses
- **Importez de vraies données** - Déposez un relevé bancaire au format CSV dans votre dossier de projet et demandez à Claude de l'intégrer au suivi
- **Apprenez en posant des questions** - Quand Claude écrit une formule, demandez « explique ce que fait cette formule » pour apprendre Excel
- **Partagez votre suivi** - Poussez le fichier terminé sur GitHub pour que vous (ou les membres de votre famille) puissiez récupérer la dernière version
- **Lisez sur le vibe coding** - Visitez [le guide d'IBM](https://www.ibm.com/think/topics/vibe-coding) pour en savoir plus sur ce style de codage

## Dépannage

- **Une cellule de formule est vide ou affiche `None`** - Le fichier doit être recalculé après les modifications. Demandez à Claude : « Recalcule budget.xlsx et vérifie qu'il n'y a aucune erreur de formule. »
- **Le graphique ne se met pas à jour après la modification des données** - Rouvrez l'onglet dans VS Code (fermez-le et cliquez à nouveau sur le fichier) pour forcer Spreadsheet Viewer à s'actualiser.
- **Claude fait une erreur** - Normal ! Décrivez ce qui ne semble pas correct et demandez à Claude de le corriger. Le vibe coding inclut l'itération et le débogage.
- **Impossible de pousser vers GitHub** - Assurez-vous que vous êtes connecté à GitHub Desktop et que vous avez publié le dépôt (Étape 1). Vérifiez votre connexion Internet.
- **La liste déroulante n'apparaît pas** - La validation des données ne s'affiche que dans de vrais logiciels de tableur (Excel, LibreOffice, Google Sheets), et pas toujours dans les visionneuses légères. Ouvrez le fichier dans Excel ou LibreOffice Calc pour la tester.

## Aperçu du Flux de Travail

Ce tutoriel a combiné plusieurs outils en un seul flux de travail :

- **GitHub Desktop** - Contrôle de version avec interface visuelle (créer des dépôts, valider, pousser)
- **VS Code** - Éditeur avec l'extension Spreadsheet Viewer pour des aperçus rapides
- **Claude Code** - Assistant IA qui construit et modifie de vrais fichiers `.xlsx` à partir de vos descriptions
- **openpyxl (en coulisses)** - Le moteur que Claude utilise pour écrire les formules, la mise en forme et les graphiques dans le fichier

La magie n'est pas un seul outil : c'est la façon dont le vibe coding vous permet de décrire ce que vous voulez et d'itérer rapidement. Vous êtes passé d'un dossier vide à un suivi de budget fonctionnel et rempli de graphiques sans écrire une seule formule à la main.

## Flux de Travail Quotidien

Après cette configuration initiale, votre routine quotidienne de vibe coding devient :

1. **Ouvrez VS Code** - Ouvrez votre dossier de projet
2. **Démarrez Claude Code** - Tapez `claude` dans le terminal
3. **Décrivez votre objectif** - « Ajoute une fonctionnalité qui... » ou « Corrige la ligne où... »
4. **Vérifiez le fichier** - Ouvrez-le dans Spreadsheet Viewer ou dans Excel/LibreOffice
5. **Itérez ou validez** - Si quelque chose ne va pas, décrivez la correction ; si cela fonctionne, validez avec GitHub Desktop
6. **Poussez régulièrement** - Cliquez sur **Push origin** pour sauvegarder sur GitHub

Plus vous pratiquez, mieux vous savez décrire ce que vous voulez. Le vibe coding est une compétence : vous apprenez quels types de descriptions fonctionnent le mieux et comment découper de grandes idées de tableur en éléments testables.

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 21 septembre 2026.
