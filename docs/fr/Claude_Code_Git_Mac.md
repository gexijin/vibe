[Accueil](./)

# Claude Code avec le contrôle de version local pour Mac

Vous codez avec l'assistance de l'IA. Elle apporte des modifications à vos fichiers. Parfois, les modifications fonctionnent parfaitement. Parfois, elles ne fonctionnent pas. **Le contrôle de version est comme un bouton d'annulation pour l'ensemble de votre projet.** Chaque fois que vous enregistrez un instantané (appelé un « commit »), vous créez un point de restauration auquel vous pouvez toujours revenir. Mieux encore, vous pouvez faire tout cela entièrement sur votre ordinateur et Claude Code le fait pour vous.

## Concepts Clés

- **Terminal** - Interface en ligne de commande intégrée à Mac pour exécuter des commandes
- **Git** - Suit chaque modification de vos fichiers sur votre ordinateur, créant des points de restauration auxquels vous pouvez revenir à tout moment
- **Commit** - Un instantané de votre projet à un moment précis avec une description de ce qui a changé
- **Claude Code** - Assistant de codage IA qui écrit du code, corrige les bugs et gère les opérations Git par de simples demandes

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Installing Claude Code on Mac](./Install_Claude_Code_MacOS)
- 30 minutes

## Étape 1 : Ouvrir Terminal

Choisissez l'une de ces méthodes :

- **Spotlight :** Appuyez sur `Command (⌘) + Espace`, tapez `Terminal`, appuyez sur Entrée
- **Finder :** Ouvrez **Applications** > **Utilitaires** > **Terminal**
- **Launchpad :** Cliquez sur **Launchpad** dans le Dock, recherchez `Terminal`

Vous verrez une invite de commande se terminant par `$` ou `%`.

## Étape 2 : Installer Git

Mac a souvent Git préinstallé. Vérifions :

- Tapez cette commande et appuyez sur Entrée :
  ```
  git --version
  ```

**Si vous voyez un numéro de version** (comme `git version 2.39.0`), Git est déjà installé—passez à l'Étape 3.

**Si vous voyez « command not found »** ou une fenêtre contextuelle vous demandant d'installer les outils de développement :
- Cliquez sur **Installer** dans la fenêtre contextuelle, ou exécutez :
  ```
  xcode-select --install
  ```
- Attendez la fin de l'installation (1-5 minutes)
- Vérifiez que Git est installé :
  ```
  git --version
  ```

Vous devriez voir quelque chose comme `git version 2.39.0`.

## Étape 3 : Configurer Git avec Votre Identité

Git a besoin de savoir qui vous êtes pour les messages de commit.

- Définissez votre nom et votre e-mail (peuvent être fictifs) :
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

L'utilisation de votre nom et de votre e-mail vous aide à identifier qui a effectué les modifications lorsque plusieurs personnes travaillent sur ce projet.

## Étape 4 : Accéder à Votre Dossier Documents

- Accédez à votre dossier Documents :
  ```
  cd ~/Documents
  ```
- Vérifiez que vous êtes au bon endroit :
  ```
  pwd
  ```

Vous devriez voir `/Users/VOTRE_NOM_UTILISATEUR/Documents`.

## Étape 5 : Créer le Dossier du Projet

- Créez un dossier appelé `test_claude` :
  ```
  mkdir test_claude
  ```
- Accédez-y :
  ```
  cd test_claude
  ```

C'est là que votre projet va résider.

## Étape 6 : Démarrer Claude Code

- Démarrez Claude Code :
  ```
  claude
  ```

Claude Code se lance et attend votre demande.

## Étape 7 : Demander à Claude d'Initialiser Git

- Tapez cette demande :
  ```
  Start tracking changes
  ```

Claude initialise un dépôt Git dans votre dossier (prend 2-5 secondes). Vous avez maintenant le contrôle de version !

## Étape 8 : Créer l'Application de Minuterie

- Dans Claude Code, tapez :
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  ```

Claude crée `timer.html` (prend 10-30 secondes) avec le code CSS et JavaScript.

## Étape 9 : Tester la Minuterie

- Ouvrez Finder
- Accédez à **Documents** > **test_claude**
- Double-cliquez sur `timer.html` pour l'ouvrir dans votre navigateur
- Essayez la minuterie :
  - Tapez `1` dans le champ de saisie
  - Cliquez sur **Start**
  - Regardez le compte à rebours

**Si quelque chose ne fonctionne pas :** Dans Claude Code, décrivez l'erreur : `I'm seeing this error: [décrivez ce qui s'est passé]. Can you fix it?`

## Étape 10 : Demander à Claude de Faire un Commit

- Dans Claude Code, tapez :
  ```
  Save these changes.
  ```

Claude va :
- Vérifier quels fichiers ont changé
- Rédiger un message de commit descriptif
- Créer le commit (prend 5-10 secondes)

Vous avez créé votre premier point de sauvegarde ! Vous pouvez toujours revenir à cette version fonctionnelle.

## Étape 11 : Ajouter des Boutons Prédéfinis

- Dans Claude Code, tapez :
  ```
  Add two buttons on the top. If I click on them it automatically starts 1- and 5-minute timers.
  ```
- Actualisez votre onglet de navigateur (ou appuyez sur `Command (⌘) + R`)
- Testez : Cliquez sur le bouton **5 min**
- Si cela fonctionne, faites un commit des modifications :
  ```
  Save these changes.
  ```

Nous avons créé un 2e point de sauvegarde. Cette version a les deux boutons qui fonctionnent.

## Étape 12 : Ajouter un Autre Bouton

- Dans Claude Code, tapez :
  ```
  Add a 15-minute button.
  ```
- Actualisez votre onglet de navigateur (appuyez sur `Command (⌘) + R`)
- Testez : Cliquez sur le bouton **15 min**

**Pour ce tutoriel :** Prétendez que le bouton 15 minutes ne fonctionne pas correctement. Ne faites pas encore de commit—nous allons pratiquer l'abandon des mauvaises modifications.

## Étape 13 : Abandonner les Modifications

Parfois, le code de l'IA ne fonctionne pas et vous devez recommencer à partir de votre dernier point de sauvegarde.

- Dans Claude Code, tapez :
  ```
  discard these changes.
  ```
- Claude demandera une confirmation
- Tapez `yes` et appuyez sur Entrée
- Actualisez votre navigateur—le bouton 15 minutes disparaît

Claude rejette les nouvelles modifications que nous n'aimons pas. La minuterie fonctionne à nouveau avec seulement les boutons 1 et 5 minutes !

## Étape 14 : Ajouter une Notification Sonore

- Dans Claude Code, tapez :
  ```
  Add a sound notification when time is up.
  ```
- Actualisez le navigateur et testez après que Claude ait terminé (réglez la minuterie sur 0.1 minutes)
- Si cela fonctionne, faites un commit des modifications :
  ```
  Save these changes.
  ```

## Étape 15 : Ajouter un Bouton de Répétition

- Dans Claude Code, tapez :
  ```
  The sound should continue until I click a button to snooze it.
  ```
- Actualisez le navigateur et testez après que Claude ait terminé (réglez la minuterie sur 0.1 minutes)
- Si cela fonctionne, faites un commit des modifications :
  ```
  Save these changes.
  ```

## Étape 16 : Voir Votre Historique de Commits

- Dans Claude Code, tapez :
  ```
  show my change history
  ```

Claude affiche vos commits dans un format lisible. Vous verrez :
- Votre commit de l'application de minuterie initiale
- Le commit des boutons prédéfinis (1 min et 5 min)
- Le commit de la notification sonore
- Le commit du bouton de répétition

Remarquez que la tentative du bouton 15 minutes n'y est pas—vous l'avez abandonnée !

## Étape 17 : Examiner le Code

- Dans le navigateur qui affiche l'application, faites un clic droit et sélectionnez **Afficher le code source de la page** (ou appuyez sur `Option (⌥) + Command (⌘) + U`)
- Vous pouvez voir le code source de ceci.
- Dans Claude Code, demandez
  ```
  Explain this code. Just big picture.
  ```

## Le Workflow Complet

- Demandez à Claude d'apporter des modifications
- Testez
- Si cela fonctionne → Demandez à Claude de faire un commit
- Si cela échoue → Demandez à Claude de le corriger.
- Impossible à corriger → Abandonnez les modifications et réessayez
- Répétez

Vous pouvez toujours revenir à n'importe quel commit. Abandonnez sans crainte—ne commitez que le code fonctionnel !

## Prochaines Étapes

Essayez d'ajouter plus de fonctionnalités à votre minuterie :

- **Bouton 15 minutes :** `Add a working 15-minute preset button` (refaites ce que nous avons abandonné !)
- **Bouton Pause :** `Add a Pause/Resume button that toggles the timer state`
- **Meilleure mise en page :** `Improve the visual design with a modern color scheme and larger fonts`
- **Barre de progression :** `Add a visual progress bar showing time remaining`

N'oubliez pas : Testez après chaque fonctionnalité, commitez après chaque succès, abandonnez les échecs.

## Dépannage

- **Erreur « not a git repository » :** Assurez-vous d'être dans le dossier test_claude (`cd ~/Documents/test_claude`)
- **Impossible de trouver timer.html dans Finder :** Le fichier se trouve à `/Users/VOTRE_NOM_UTILISATEUR/Documents/test_claude/timer.html`
- **Les commandes Git ne fonctionnent pas :** Assurez-vous d'avoir terminé l'Étape 2 et installé Git
- **La minuterie ne fonctionne pas :** Ouvrez la console du navigateur (clic droit sur la page, sélectionnez **Inspecter**, puis cliquez sur l'onglet **Console**), copiez tous les messages d'erreur en rouge, collez-les dans Claude

## Ce Que Vous Pouvez Demander à Claude

- `what files have I changed?` - Voir les modifications non commitées
- `show me the diff` - Voir exactement quel code a changé
- `explain what the timer code does` - Comprendre l'implémentation
- `create a branch called experiment` - Essayer des modifications risquées en toute sécurité
- `go back to the previous commit` - Annuler tout depuis le dernier commit

Claude gère toutes les opérations Git en langage naturel—aucune commande à mémoriser !

## Aperçu du Workflow

- **Configuration :** Installez Git une fois, configurez l'identité une fois
- **Développement :** Claude écrit le code, vous testez dans le navigateur
- **Contrôle de Version :** Claude gère toutes les opérations Git via de simples demandes
- **Sécurité :** Abandonnez les mauvaises modifications à tout moment, revenez à n'importe quel commit précédent
- **Local :** Tout reste sur votre ordinateur, aucun compte ni connexion Internet requis

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 8 décembre 2025.
