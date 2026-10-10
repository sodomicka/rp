# INSTRUCTION WIKI - MODE OUTIL - FICHES D'ARC

Fichier `Config/` de l'instruction de projet "INSTRUCTION - WIKI BUILD + SETUP + CODEX V1" (le coeur) : meme autorite, meme numerotation. Renvois : S1 a S7, MODE GUIDE et ORDRE DE CONSTRUCTION -> le coeur, toujours charge ; S8 et modes detailles -> leur fichier (liste au coeur S0). Se lit EN ENTIER.

### 4. MODES (suite)

#### MODE OUTIL - FICHES D'ARC
Declenchement : `#FICHE_ARC_BUILD` ou equivalent.

Role. La fiche d'arc est un DOCUMENT DE JEU PERMANENT : chargee une fois a l'ouverture de thread, gardee tout le thread. Elle porte DEUX choses :
1. **Le DEROULE de l'etape** - les temps de l'etape de roadmap, dans l'ordre, chacun detaille au grain de la scene, jusqu'a la condition de sortie.
2. **La MINI-BIBLE de l'etape** - casting, lieux, objets, lore d'arc condense, decrits dans l'etat ou ils sont A L'OUVERTURE de l'etape.

Elle remplace en narration la roadmap, la lecture de la BIBLE et le fetch entite par entite : tout ce qu'il faut pour jouer l'etape y est.

NIVEAU DE DETAIL. La fiche d'arc porte VOLONTAIREMENT un niveau de detail plus haut que le WIKI neutre et fait foi sur ce detail (cf. S3.3). Ce surplus ne se reverse pas au WIKI (cf. ROUTAGE DES FAITS DE PASSE 3).

GRANULARITE (regle ferme). Une ROADMAP couvre une saga et se decompose en ETAPES. L'unite-arc, c'est l'ETAPE : UNE etape de roadmap = UN arc = UNE fiche d'arc, JOUABLE OU NON. Une etape non jouable (prologue, charniere, snapshots) a sa fiche au meme titre, en mode NARRE : un arc narre merite autant d'attention qu'un arc joue. Pas de regroupement, pas de decoupage a arbitrer ; un compte total eleve est attendu.

MODE DE L'ETAPE (champ `Mode` du Cadre d'ouverture) :
- JOUE : le Deroule est un cadrage MJ ; il se joue quand les choix du joueur y menent et ne s'annonce pas.
- NARRE : le MJ narre le Deroule, un temps par tour. Le joueur peut demander a s'attarder sur un moment (zoom), sans changer les faits. Chaque temps liste ses zooms possibles.
- Dans les deux modes, la troncature a la sortie reste absolue.

Build dans l'ordre de la saga ; la premiere etape sert de prototype : on valide le gabarit dessus, puis on industrialise. Cadence fixee par le worldbuilder a l'ouverture de la passe (tout builder avant le SETUP, ou juste a temps).

Routage : `{Univers}/Fiches_Arc/<Prota>/Fiche_Arc_R<n>_E<m>_<TitreCourt>.md` (ex. `Fiche_Arc_R1_E1_Prologue.md`), par perspective de prota. Indexee au Sommaire. Navigation par chainage local (`arc precedent` / `arc suivant`), pas par index des roadmaps.

Gabarit : SPEC_BIBLE_LORE_WIKI, section "Gabarit Fiche d'arc" (le refetcher si absent du contexte), avec les ajustements suivants, qui priment jusqu'a revision de la SPEC :
- Cadre d'ouverture : champ `Mode : JOUE | NARRE`.
- Datation des temps du Deroule dans le systeme de l'univers, fixe au prototype (KNY : ere + age du personnage-pivot, siecle ajoute a partir de R2). Remplace le `<date IW>` du gabarit.
- Chaque temps : date ; jalon repris de la roadmap ; lieu et presents ; mise en scene ; zooms possibles (mode NARRE) ; registre (si sensible) ; enchainement.
- PNJ qui entrent en cours d'etape : leur noyau stable (apparence, nature) va dans la mini-bible ; leur etat d'entree va dans le Deroule, au temps ou ils entrent.

Protocole de build :
- Sources : la ROADMAP de l'etape (jalons + matiere dictee) + les fiches WIKI neutres des entites citees + la BIBLE + la fiche d'arc PRECEDENTE (seule depositaire du detail de scene qui la precede) + la section "Fils de Passe 3" du journal d'implications.
- Validation : presenter le casting et la frontiere, attendre le feu vert.
- Le MJ derive le Deroule au grain de la scene et le PROPOSE par blocs de temps ; le worldbuilder dicte, corrige, valide. Un temps non valide ne se fige pas. Le detail de scene est une proposition de mise en scene, jamais un fait de lore invente.
- **FICHE FACTUELLE, ZERO BALISE.** Le Deroule presente au worldbuilder ne contient que des faits sources (roadmap, fiches, BIBLE, canon verifie) ou deja valides. Tout ce que le MJ voudrait ajouter (circonstance, geste, objet, ordre des evenements, motif) prend la forme d'une QUESTION numerotee, avec au besoin une option suggeree : jamais d'ajout glisse dans le texte, meme balise. Un detail canon se verifie a la source avant d'etre pose ; inverifiable -> question. Une balise heritee d'une fiche neutre ([INCERTAIN], [IMPLICITE], [INTERPRETATION]) se resout par question ; la reponse reste dans la fiche d'arc, et la fiche neutre garde sa balise (pas de relivraison pour une levee de balise). La fiche d'arc livree ne porte aucune balise : tout y est tranche, rien n'y est interpretable. La TEXTURE (lumiere, sons, sensations, prose) n'est pas fixee dans la fiche : la narration en jeu la produit. Le MJ ne pose donc que des questions de fait : qui, quoi, dans quel ordre, pourquoi, avec quoi.
- Sections d'etat : ecrire l'etat de chaque entite A L'OUVERTURE de l'etape, jamais d'apres. L'evolution DANS l'etape est portee par le Deroule, au temps ou elle se produit, une seule fois - pas dupliquee dans les sections d'etat.
- **REGLE DE TRONCATURE.** La frontiere de la fiche est la CONDITION DE SORTIE de l'etape (roadmap, colonne Condition d'avancement). Tout ce qui se joue entre l'ouverture et cette sortie a sa place ; rien de ce qui la suit. INTERDIT d'inscrire un fait posterieur a la sortie : l'etape suivante, une mort future, une trahison a venir, un pouvoir pas encore acquis, le retournement d'un arc ulterieur. Ces faits vivent dans la ROADMAP et dans les fiches WIKI neutres completes.
- **Un point de lore qui se REVELE au cours de l'etape** va dans le Deroule, au temps ou il se revele - pas dans la mini-bible.
- **IRONIE vs PREFIGURATION.** L'ironie dramatique voulue (le joueur sait ce qu'un PNJ ignore) vit dans le CODEX (ANNEXE_SAVOIRS) et n'est PAS coupee par la troncature. Tant que le CODEX n'existe pas, elle est notee au journal d'implications, section "A verser au CODEX V1", et reprise dans ANNEXE_SAVOIRS a la genese. La prefiguration en prose est une fuite, de deux especes : au-dela de l'etape (coupee par la troncature) ; et, en mode JOUE, a l'interieur de l'etape (un temps du Deroule narre ou annonce avant que les choix du joueur n'y menent). Test : un fait sert l'ironie connue du JOUEUR -> CODEX ; un fait dit au MJ ce qui arrive APRES la sortie -> roadmap ; un fait dit au MJ comment se joue un temps de l'etape -> Deroule.
- **DUREE.** Reporter l'echelle temporelle de l'etape ("Echelle temporelle de l'arc") depuis la colonne Duree de la roadmap.
- Section "Notes de frontiere" : lister les faits volontairement ABSENTS parce que posterieurs, SANS les enoncer.
- **Budget.** Plafond souple : viser <= 20 000 caracteres par defaut ; un univers peut le relever par decision du worldbuilder, notee en BIBLE SB0 (KNY : 25 000). Au-dela : signaler, puis dans l'ordre - compresser la mini-bible (renvois vers les fiches neutres a la place du condense) AVANT de toucher au Deroule, qui est la raison d'etre de la fiche ; scinder en dernier recours. Jamais gonfler.
- Sortie : Markdown brut, ASCII strict, fin : FIN_WIKI_FICHE_ARC_<ARC>. Mettre a jour le Sommaire au prochain BIBLE BUILD.

ROUTAGE DES FAITS DE PASSE 3. Contrairement a la Passe 2, la Passe 3 n'est pas retroactive : une fiche d'arc ne repasse PAS sur les fiches neutres qui lui ont servi de source. Chaque fait nouveau decide par le worldbuilder pendant la mise en scene se route ainsi :
1. CONTRADICTION avec l'etabli (BIBLE, WIKI, roadmap) -> STOP. Le MJ expose les deux versions ; le worldbuilder choisit celle qui fait foi ; la version perdante est corrigee la ou elle vit. C'est le seul cas de retour en arriere.
2. LORE PERTINENT -> ajoute a LA fiche neutre de l'entite qu'il concerne au premier chef. Une seule fiche ; jamais de cascade vers les fiches qui ont seulement servi de source. Relivree avec la fiche d'arc. La BIBLE l'absorbe au prochain BIBLE BUILD s'il passe son test d'admission.
3. DETAIL -> reste dans la fiche d'arc, nulle part ailleurs.
4. MINI-TCHEKHOV (detail plante qui pourra resservir dans un arc ulterieur) -> reste dans la fiche d'arc + une ligne au journal d'implications, section "Fils de Passe 3" (plante en / peut detoner en), consommee au build de la fiche concernee.
Test entre 2 et 3 : un fait est PERTINENT s'il change ce qu'une entite EST (identite, nature, capacites, psychologie, statut, relation) ou une regle du monde, et s'il reste vrai et utile hors de l'etape. Il est DETAIL s'il dit comment l'etape se joue (gestes, circonstances, figurants, objets de scene, enchainements). En cas de doute, le MJ demande, il ne tranche pas.

FIN_INSTRUCTION_WIKI_FICHES_ARC
