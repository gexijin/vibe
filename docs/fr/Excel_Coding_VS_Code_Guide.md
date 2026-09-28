---
title: "Utiliser Claude Code avec Excel dans VS Code"
lang: "fr"
---
[Accueil](./)

# Utiliser Claude Code avec Excel dans VS Code

Vous avez besoin d'un tableur - des formules, une mise en forme, peut-être un graphique - mais vous ne voulez pas vous battre avec les menus d'Excel. Considérez Claude Code comme un assistant qui connaît Excel sur le bout des doigts : vous décrivez ce que vous voulez en français, et il construit un vrai fichier `.xlsx` avec des formules qui fonctionnent. Ce tutoriel vous montre comment préparer un dossier de projet dans VS Code et laisser Claude Code créer et modifier des feuilles de calcul Excel pour vous.

## Concepts Clés

- **Compétence xlsx** - Capacité intégrée à Claude Code pour créer et modifier des feuilles de calcul `.xlsx` avec de vraies formules, une mise en forme et des graphiques
- **[Extension Spreadsheet Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)** (anciennement Excel Viewer) - Extension VS Code qui vous permet d'afficher et de modifier des fichiers de tableur sans quitter l'éditeur
- **Formules ou nombres saisis en dur** - Claude Code écrit de vraies formules Excel (comme `=SUM(B2:B9)`) afin que votre feuille se recalcule lorsque vous modifiez les données

## Ce Dont Vous Aurez Besoin

- Avoir terminé [VS Code Basics](./VS_Code_Getting_Started)
- Claude Code installé et fonctionnel (voir [Install Claude Code on Windows](./Install_CLAUDE_Code_Win) ou [Install Claude Code on Mac](./Install_Claude_Code_MacOS))
- Microsoft Excel, LibreOffice Calc ou Google Sheets pour ouvrir le fichier terminé (optionnel - l'extension Spreadsheet Viewer fonctionne sans aucun d'entre eux)
- 15-20 minutes

## Étape 1 : Installer l'Extension Spreadsheet Viewer dans VS Code

- Ouvrez VS Code
- Cliquez sur l'icône **Extensions** dans la barre latérale gauche (ou cliquez sur **View > Extensions**)
- Recherchez `GrapeCity.gc-excelviewer`
- Cliquez sur **Install** sous **Spreadsheet Viewer** par **MESCIUS**

**Remarque :** Cette extension s'appelait auparavant **Excel Viewer** par **GrapeCity**, et d'anciens guides et vidéos utilisent peut-être encore ce nom. Une recherche sur « Excel Viewer » affiche désormais plusieurs autres extensions : recherchez donc par l'identifiant ci-dessus pour obtenir la bonne. L'identifiant commence toujours par `GrapeCity` - c'est normal.

Cela vous permet de cliquer sur n'importe quel fichier `.xlsx` et de le voir affiché comme une feuille de calcul directement dans VS Code, sans avoir à passer à une autre application.

## Étape 2 : Créer Votre Dossier de Projet

- Créez un nouveau dossier sur votre ordinateur (par exemple, `my-excel-project`)
- Dans VS Code, cliquez sur **File > Open Folder** et sélectionnez votre nouveau dossier
- Cliquez sur **Select Folder** (Windows) ou **Open** (Mac)

## Étape 3 : Démarrer Claude Code

- Cliquez sur **Terminal > New Terminal** dans VS Code
- Tapez cette commande et appuyez sur Entrée :

```bash
claude
```

- Si c'est la première fois, une fenêtre de navigateur s'ouvre pour l'authentification - connectez-vous avec votre compte Claude
- Revenez à VS Code dès que vous voyez le message de bienvenue de Claude dans le terminal

## Étape 4 : Créer Votre Première Feuille de Calcul

- Dans le terminal Claude Code, tapez :

```
Crée une feuille de calcul appelée budget.xlsx avec les colonnes Catégorie, Montant mensuel et Remarques. Ajoute 6 exemples de catégories de dépenses comme Loyer, Courses et Charges, avec des montants réalistes. Ajoute une ligne Total en bas qui additionne la colonne Montant mensuel à l'aide d'une formule.
```

- Appuyez sur Entrée
- Regardez Claude écrire un script Python, l'exécuter et produire `budget.xlsx` dans votre dossier de projet
- Claude recalcule aussi le fichier pour que les formules affichent de vrais nombres, et non des cellules vides

## Étape 5 : Afficher le Résultat

- Dans le panneau Explorer de VS Code (à gauche), cliquez sur `budget.xlsx`
- L'extension Spreadsheet Viewer ouvre le fichier sous forme de feuille de calcul
- Si vous voyez à la place du texte et des symboles illisibles, VS Code a ouvert le fichier en texte brut - voir la section Dépannage ci-dessous
- Cliquez sur la cellule **Total** en bas : remarquez qu'il s'agit d'une formule, et non d'un nombre saisi à la main
- Si Excel ou LibreOffice Calc est installé, vous pouvez aussi double-cliquer sur le fichier dans l'Explorateur de fichiers (Windows) ou le Finder (Mac) pour l'ouvrir dans ce logiciel

## Étape 6 : Demander à Claude d'Ajouter un Graphique

- De retour dans le terminal Claude Code, tapez :

```
Ajoute à budget.xlsx un graphique en secteurs montrant la part de chaque catégorie dans le total des dépenses mensuelles.
```

- Appuyez sur Entrée
- Rouvrez `budget.xlsx` dans l'onglet Spreadsheet Viewer (cliquez sur l'icône d'actualisation, ou fermez puis rouvrez le fichier) pour voir le nouveau graphique

## Étape 7 : Modifier les Données et Demander à Claude de Mettre à Jour

- Dans Spreadsheet Viewer, ou dans Excel/LibreOffice si le fichier y est ouvert, modifiez l'un des montants (par exemple, doublez la valeur du Loyer)
- Enregistrez le fichier
- Dans le terminal Claude Code, tapez :

```
J'ai modifié certains nombres dans budget.xlsx. Recalcule les totaux et vérifie que le graphique correspond toujours aux données.
```

- Appuyez sur Entrée
- Claude lit vos modifications, recalcule les formules et confirme que tout concorde

Voici le flux de travail essentiel : décrivez ce que vous voulez, laissez Claude le construire, vérifiez le résultat et demandez des modifications en langage courant.

## Étape 8 : Demander à Claude de Nettoyer des Données Désordonnées

Claude Code est aussi utile pour réparer des feuilles de calcul déjà en désordre.

- Tapez :

```
Crée un fichier messy_sales.csv avec 15 lignes de données de ventes qui comportent quelques problèmes : quelques cellules vides, des formats de date incohérents et une ligne en double. Crée ensuite une version nettoyée appelée sales_clean.xlsx qui corrige ces problèmes, et explique ce que tu as corrigé.
```

- Appuyez sur Entrée
- Lisez le résumé que Claude vous donne de ce qu'il a trouvé et corrigé
- Ouvrez `sales_clean.xlsx` pour vérifier que les données sont correctes

## Prochaines Étapes

- Demandez à Claude de construire une feuille de calcul à partir d'un fichier CSV que vous avez déjà (faites-le d'abord glisser dans votre dossier de projet)
- Essayez des demandes plus avancées : « ajoute une mise en forme conditionnelle pour que toute catégorie au-dessus de $500 passe en rouge »
- Demandez à Claude d'ajouter une deuxième feuille qui résume les données de la première
- Combinez cela avec [Use GitHub Desktop with Claude Code](./GitHub_Desktop_Claude_Code_Workflow) pour enregistrer des versions de vos feuilles de calcul au fur et à mesure
- Passez à [Vibe Coding a Budget Tracker in Excel](./Vibe_Coding_Excel_Guide) pour construire un projet complet à plusieurs feuilles

## Dépannage

- **`budget.xlsx` s'ouvre sous forme de texte et de symboles illisibles (commençant par `PK`)** : VS Code affiche le fichier brut parce qu'aucune visionneuse de tableur ne l'a pris en charge. Le fichier lui-même n'est pas abîmé - un `.xlsx` est un paquet compressé, pas du texte brut. Vérifiez que **Spreadsheet Viewer** par MESCIUS (`GrapeCity.gc-excelviewer`) est installé et activé, puis fermez l'onglet, faites un clic droit sur `budget.xlsx` dans le panneau Explorer, choisissez **Open With...** et sélectionnez **Excel Editor** (l'éditeur de Spreadsheet Viewer pour les fichiers `.xlsx`). Si une autre extension de tableur est également installée, choisissez **Configure default editor for '*.xlsx'...** dans la même liste et sélectionnez **Excel Editor** pour qu'un simple clic sur le fichier l'utilise désormais.
- **Spreadsheet Viewer affiche un aperçu vide ou cassé** : Fermez l'onglet et rouvrez le fichier. Si le problème persiste, ouvrez plutôt le fichier dans Excel, LibreOffice Calc ou Google Sheets - le fichier lui-même est correct, il s'agit simplement d'un problème d'aperçu.
- **Les cellules de formule sont vides au lieu d'afficher un nombre** : Cela signifie généralement que le fichier n'a pas été recalculé après son écriture. Demandez à Claude : « Recalcule budget.xlsx et vérifie qu'il n'y a aucune erreur de formule. »
- **Les modifications de Claude n'apparaissent pas** : Assurez-vous de regarder le même fichier que celui modifié par Claude (vérifiez le nom de fichier qu'il mentionne). Fermez et rouvrez l'onglet dans VS Code pour forcer l'actualisation.
- **« claude is not recognized » dans le terminal** : Claude Code n'est pas installé correctement. Consultez à nouveau le [guide d'installation](./Install_CLAUDE_Code_Win) correspondant à votre système.

## Résumé du Flux de Travail

- **VS Code** - Votre dossier de projet et un endroit pour afficher les feuilles de calcul avec l'extension Spreadsheet Viewer
- **Claude Code** - Écrit et modifie de vrais fichiers `.xlsx` avec des formules qui fonctionnent, à partir de vos demandes en langage courant
- **Excel / LibreOffice / Google Sheets** - Optionnels, pour ouvrir et retoucher à la main les fichiers créés par Claude
- **Itérer** - Décrivez ce que vous voulez, vérifiez le résultat, décrivez la modification suivante

---

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 21 septembre 2026.
