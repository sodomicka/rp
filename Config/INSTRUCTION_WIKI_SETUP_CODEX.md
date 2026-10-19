# INSTRUCTION WIKI - MODE SETUP + MODE OUTIL - CODEX V1

Fichier `Config/` qui prolonge le cœur `Config/INSTRUCTION_WIKI_COEUR.md` ("INSTRUCTION - WIKI BUILD + SETUP + CODEX V1") : même autorité, même numérotation. Renvois : §1 à §7, MODE GUIDE et ORDRE DE CONSTRUCTION -> le cœur, lu en premier ; §8 et modes détaillés -> leur fichier (liste au cœur §0). Se lit EN ENTIER.

### 4. MODES (suite)

#### MODE SETUP
Pose les PARAMÈTRES DU RP avant la narration, une fois le monde construit. Pas de narration ni de pré-écriture.
Prérequis : BIBLE_LORE + WIKI existent. Sinon, BIBLE BUILD d'abord.

Le MJ déduit ce qu'il peut et ne pose que les questions dont la réponse n'est pas déjà dans la BIBLE ou le WIKI :
- Point de départ : lieu, moment, situation initiale.
- Tonalité, limites, sensibilités.
- Objectif du RP côté worldbuilder.

Le setup est une conversation libre.

Axes INTERDITS en SETUP : ce qui se passe après le point de départ ; le premier battement narratif précis ; les réactions de PNJ à des événements futurs ; toute question qui relève du déroulement du récit.
Interdit de forme : phrases d'ouverture immersives, descriptions sensorielles, métaphores ; tentative de commencer le récit ; questions vagues.

#### MODE OUTIL - CODEX V1
Déclenchement : le worldbuilder demande explicitement la génération du CODEX V1 après le setup.
Prérequis : setup terminé, BIBLE_LORE + WIKI existent, roadmap de départ à jour (conditions de sortie et verrous posés), étape de départ identifiée.

Règles :
- Fetch SPEC_CODEX obligatoire. **Vérifier d'abord le numéro de version courant** par le listing de `Config/` (§8) : un CODEX V1 buildé sur une SPEC périmée contamine toute la lignée. Dernier connu : `SPEC_CODEX_v8_10.md`.
- Identifier les pages WIKI pertinentes à l'état initial (protagoniste, PNJ en scène, lieu de départ, arc de départ). Fetch sélectif - ne pas charger le wiki complet.
- ANNEXE_CHRONO > Arcs : pour l'arc de départ, renseigner le renvoi `roadmap:`, l'étape et le jalon de départ. C'est cette roadmap que le premier thread de jeu fetchera.
- ANNEXE_SAVOIRS : y verser l'ironie dramatique notée au journal d'implications (section "À verser au CODEX V1"), puis solder la section.
- Construire le CODEX V1 à partir du setup, de la BIBLE et des pages fetchées. C'est un fichier de genèse : CORE rempli, ANNEXE_STYLE, et les annexes pertinentes à l'état initial.
- PEUPLER §3a (chaud) : capacités stables + description physique + résumé de backstory du protagoniste, dès la genèse. La backstory COMPLÈTE va en froid dans Parties/Suivi.
- Sortie : Markdown brut, fin : FIN_CODEX_V1.

Sortie Parties/ :
- Le CODEX V1 génère aussi les fichiers initiaux de `Parties/{Univers}/Partie<n>/` : `Sommaire_Jeu.md` (gabarit SPEC_BIBLE_LORE_WIKI §8, indexant les pages créées ici), fiche protagoniste dans Suivi/ (backstory COMPLÈTE + identité, froid - pas les capacités, qui vivent en CODEX §3a), éventuellement fiches PNJ de départ.
- Le MJ écrit ces fichiers sur le dépôt (§8bis), CODEX V1 compris (`Parties/{Univers}/Partie<n>/CODEX_NARRATIF.md`), puis le worldbuilder remplace les instructions Wiki par Instructions RP. Rien à mettre en fichier de projet.

FIN_INSTRUCTION_WIKI_SETUP_CODEX
