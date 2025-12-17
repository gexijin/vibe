[Accueil](../fr/)

# Utiliser GitHub Desktop avec Claude Code

Vous codez avec l'assistance de l'IA. Elle apporte des modifications à vos fichiers. Parfois les modifications fonctionnent parfaitement. Parfois non. **Le contrôle de version est comme un bouton d'annulation pour l'ensemble de votre projet.** Chaque fois que vous enregistrez un instantané (appelé un "commit"), vous créez un point de restauration. Vous pouvez toujours revenir en arrière.

Lorsque vous combinez [GitHub Desktop](https://desktop.github.com) avec [Claude Code](https://claude.com/claude-code), vous obtenez un développement à la vitesse de l'IA avec un contrôle de version professionnel.

## Concepts Clés

**Git** suit chaque modification de vos fichiers sur votre ordinateur.

**GitHub** stocke votre code dans le cloud comme sauvegarde.

**GitHub Desktop** rend Git visuel - vous cliquez sur des boutons au lieu de taper des commandes.

**Claude Code** est un assistant de codage IA qui écrit du code, corrige des bugs et crée des commits pour vous.

## Ce Que Vous Allez Faire

Créer une application de minuteur simple avec Claude Code et suivre toutes les modifications avec GitHub Desktop :
- Créer un projet et une application de minuteur
- Tester et corriger les erreurs
- Committer et pousser les modifications
- Supprimer les mauvaises modifications et réessayer
- Laisser Claude automatiser les commits

## Ce Dont Vous Aurez Besoin

- Avoir terminé [Installer Claude Code sur Windows](./Install_CLAUDE_Code_Win) ou [Installer Claude Code sur Mac](./Install_Claude_Code_MacOS)
- Avoir terminé [Premiers Pas avec le Contrôle de Version](./Github_desktop)
- 20 minutes

## Étape 1 : Créer Votre Projet

- Ouvrez **GitHub Desktop**
- Cliquez sur **File** → **New Repository**
- Remplissez :
  - **Name :** `test_claude`
  - **Description :** `A timer app built with Claude Code`
  - **Local Path :** dossier Documents
  - **Cochez** "Initialize this repository with a README"
- Cliquez sur **Create Repository**
- Cliquez sur **Publish repository** en haut
- Cliquez sur **Publish Repository**

Vous avez maintenant un projet local et une sauvegarde cloud sur GitHub.

## Étape 2 : Demander à Claude de Créer l'Application de Minuteur

- Ouvrez votre **terminal**
- Naviguez vers votre projet :
  ```
  cd ~/Documents/test_claude
  ```
- Démarrez Claude Code :
  ```
  claude
  ```
- Tapez cette requête :
  ```
  Create a simple countdown timer app in a single file called timer.html.
  It should have:
  - An input field to set minutes
  - Start and Stop buttons
  - Display showing time remaining in MM:SS format
  - When timer reaches zero, display 'Time's up!'
  Keep it simple with inline CSS and JavaScript.
  ```

Claude crée le fichier `timer.html` (prend 10-30 secondes).

## Étape 3 : Tester le Minuteur

- Dans GitHub Desktop, cliquez sur **Repository** → **Show in Finder/Explorer**
- **Double-cliquez** sur `timer.html` pour l'ouvrir dans votre navigateur
- Essayez le minuteur :
  - Tapez `1` dans le champ de saisie
  - Cliquez sur **Start**
  - Observez le compte à rebours

**Si cela fonctionne :** Passez à l'Étape 5.
**Si quelque chose est cassé :** Continuez à l'Étape 4.

## Étape 4 : Corriger les Erreurs (Si Nécessaire)

- Ouvrez la console du navigateur (clic droit sur la page → **Inspect** → onglet **Console**)
- Copiez tous les messages d'erreur en rouge
- Retournez à Claude Code dans votre terminal
- Collez l'erreur :
  ```
  I'm seeing this error: [paste error]. Can you fix it?
  ```
- Actualisez le navigateur (cliquez sur le bouton de rechargement ou clic droit → **Reload**) et testez à nouveau

## Étape 5 : Examiner les Modifications

- Passez à **GitHub Desktop**
- **Panneau de gauche :** Affiche les fichiers modifiés (`timer.html`)
- **Panneau de droite :** Affiche le code (vert = ajouté)
- Lisez attentivement pour comprendre ce que Claude a créé

Examinez toujours le code généré par l'IA avant de committer.

## Étape 6 : Committer Manuellement

- En bas à gauche, dans le champ **Summary**, tapez :
  ```
  Create initial timer app with start/stop functionality
  ```
- Cliquez sur **Commit to main**

Vous avez créé un point de sauvegarde !

**Bons messages :** "Create initial timer app", "Fix start button"
**Mauvais messages :** "changes", "update", "asdf"

## Étape 7 : Pousser vers GitHub

- Cliquez sur le bouton **Push origin** en haut
- Vérifiez : **Repository** → **View on GitHub** pour voir votre code en ligne

Votre code est maintenant sauvegardé dans le cloud.

## Étape 8 : Ajouter une Notification Sonore

- Dans le terminal Claude Code :
  ```
  Add a sound notification when the timer reaches zero. Use the browser's
  built-in beep sound or create a simple audio alert.
  ```
- Testez : Actualisez le navigateur, réglez le minuteur sur 0.1 minutes, cliquez sur Start

**Pour ce tutoriel :** Faites semblant que le son ne fonctionne pas bien. Ne committez pas encore !

## Étape 9 : Supprimer les Mauvaises Modifications

  Parfois l'IA nous met sur la mauvaise voie et nous devons recommencer depuis notre dernier commit (point de sauvegarde).

- Ouvrez **GitHub Desktop**
- Cliquez sur le menu **Branch** → **Discard All Changes**
- Cliquez sur **Discard Changes** pour confirmer
- Actualisez le navigateur - le minuteur fonctionne sans le son !

Vous venez de jeter le code défectueux et de revenir à votre dernier point de sauvegarde.

## Étape 10 : Recommencer depuis le Début

- Dans Claude Code :
  ```
  Add a sound notification when the timer reaches zero. This time, use an HTML5
  audio element with a simple beep sound generated by the Web Audio API. Make
  sure it handles browser autoplay restrictions gracefully.
  ```
- Testez immédiatement (actualisez le navigateur, réglez sur 0.1 minutes, Start)

**Si cela fonctionne :** Continuez à l'Étape 11.
**Sinon :** Collez l'erreur à Claude ou réessayez.

## Étape 11 : Laisser Claude Committer et Pousser

- Dans Claude Code :
  ```
  commit and push my changes
  ```

Claude va vérifier les modifications, écrire un message de commit, committer et pousser (10-20 secondes).

**Quand utiliser :**
- Commits manuels : Lorsque vous apprenez ou voulez le contrôle
- Commits Claude : Lorsque vous travaillez rapidement et voulez de bons messages

## Étape 12 : Demander à Claude de Résumer les Modifications

- Dans Claude Code :
  ```
  what files have I changed?
  ```

Claude explique vos modifications en langage simple.

**Essayez :** `explain what the audio code does` ou `show me the last 5 commits`

## Étape 13 : Voir l'Historique

- Dans **GitHub Desktop**, cliquez sur l'onglet **History**

Vous verrez :
- Commit initial (README)
- Create initial timer app
- Add improved sound notification

Remarquez que la première tentative de son ratée n'est pas là - vous l'avez supprimée ! Seul le code fonctionnel a été inclus dans vos commits.

## Défis
- Son personnalisé : Téléchargez un .mp3 gratuit depuis [freesound.org](https://freesound.org), placez-le dans votre dossier de projet, demandez à Claude de l'utiliser
- Minuteurs multiples : `Allow users to create and run multiple timers simultaneously`
- Barre de progression : `Add a progress bar that visually shows how much time remains`

**Rappelez-vous :** Testez après chaque fonctionnalité, committez après chaque succès, supprimez les échecs.

**Consultez votre projet sur GitHub.com :** Cliquez sur **Repository** → **View on GitHub** dans GitHub Desktop pour voir votre historique complet des commits et votre code en ligne.

## Dépannage

**"Authentication failed" :** GitHub Desktop → File/Preferences → Accounts → Déconnectez-vous et reconnectez-vous

**Claude dit "not a git repository" :** Assurez-vous d'être dans le bon dossier (`cd ~/Documents/test_claude`)

**Le minuteur ne fonctionne pas :** Ouvrez la console du navigateur (clic droit → **Inspect** → **Console**), copiez les erreurs, collez-les à Claude

**Besoin d'aide ?** [Documentation GitHub Desktop](https://docs.github.com/en/desktop) • [Documentation Claude Code](https://docs.anthropic.com/en/docs/claude-code)

## Le Flux de Travail Complet

- Demandez à Claude de faire des modifications
- Testez dans le navigateur
- Si cela fonctionne → Examinez et committez
- Si cela échoue → Supprimez et réessayez
- Poussez vers GitHub
- Répétez

Commits manuels quand vous voulez le contrôle. Commits Claude quand vous voulez la rapidité. Supprimez sans crainte - ne committez que le code fonctionnel !

## Prochaines Étapes

Essayez d'ajouter des fonctionnalités à votre minuteur :

**Gains rapides :**
- Boutons préréglés pour 5, 10, 15 minutes : `Add three preset buttons: "5 min", "10 min", and "15 min"`
- Bouton pause : `Add a Pause/Resume button that toggles the timer state`
- Meilleur style : `Improve the visual design with a modern color scheme`

Créé par [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/) le 7 décembre 2025.
