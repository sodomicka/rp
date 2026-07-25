# Sommaire - Elden Ring

- version : W9

Carte de navigation du WIKI EldenRing et de Parties/EldenRing/.
Perimetre : ELDEN RING, SHADOW OF THE ERDTREE, ELDEN RING NIGHTREIGN.
Terminologie du lore : ANGLAISE (Erdtree, Grace, Tarnished, Shattering). Les noms de dossiers et
les descriptions de service restent en francais, par coherence avec le reste du depot.
Etat : PASSE 0. Corpus constitue, architecture posee, page pilote livree.

## OBJECTIF DU WIKI

Le systeme dans les grandes lignes, sans trou INVISIBLE.

Precision necessaire : le lore d'Elden Ring comporte des trous IRREDUCTIBLES, que les sources ne
comblent nulle part. "Sans trou" ne peut donc pas signifier "toute question a une reponse" - ce
serait de l'invention, que la doctrine du projet interdit. Cela signifie : aucune zone d'ombre
n'est laissee tacite. Chaque trou est repere, borne, et accompagne de ce qui le contraint.

## GRANULARITE

Deux niveaux, et deux seulement (revision du 2026-07-24, decision du worldbuilder) :

1. CORPUS - le texte du jeu brut, non redige, dans `_Corpus/`. Il tient le role de catalogue
   exhaustif : il est deja complet, deja decoupe, et il ne peut pas contredire le jeu puisqu'il
   EST le jeu. Recherche via `_Concordance/`.
2. FICHE REDIGEE - reservee a ce que le corpus ne peut pas faire : synthetiser des fragments
   disperses, arbitrer des contradictions, et cartographier les trous.

Il n'y a PAS de troisieme niveau. La branche `Catalogues/` prevue au premier build a ete
SUPPRIMEE : recopier les descriptions d'objets dans des pages redigees dupliquait le corpus en
moins fidele, avec un risque de desynchronisation entre deux copies du meme texte.

Test avant de creer une page : si son contenu se reduit a recopier le corpus, elle ne doit pas
exister.

## BUDGET DES PAGES

Decision du worldbuilder (2026-07-24), exception au plafond de 8000 caracteres de la SPEC :
- 10 000 caracteres pour une page livree par le MJ ;
- 15 000 caracteres apres integration des modifications du worldbuilder ;
- 15 000 caracteres pour Systemes/Destined_Death.md, page pilote, seuil releve par decision du
  worldbuilder (2026-07-25) en raison de sa densite de trous.
Depassement de ces seuils : signaler et proposer des compressions par gain decroissant, ne
jamais compresser sans validation. Peu de pages sont censees approcher ces plafonds.

## REGISTRE DES TROUS

Toute page redigee porte une section finale `## Trous et contraintes de comblement`.
Chaque entree comporte quatre lignes :
- la question ouverte ;
- DIT : ce que le corpus enonce, avec localisation ;
- NON DIT : ce que le corpus n'aborde pas ;
- CONTRAINTES : ce qu'un comblement futur ne pourrait pas contredire.

La quatrieme ligne est la raison d'etre du dispositif. Elle constitue le cahier des charges de
toute invention ulterieure : elle dit ou sont les murs de la piece, sans dire comment la
meubler. Un index transversal des trous ouverts sera agrege une fois la carte structurelle
complete.

## NARRATION VISUELLE

Elden Ring raconte autant par le design que par le texte : architectures, palettes, motifs,
iconographie. Le corpus n'en capte RIEN. Sans registre dedie, cette part de la narration serait
absente du wiki - non parce qu'elle est incertaine, mais parce que l'outil de collecte est
aveugle.

`_Observations_Visuelles.md` est le pendant du corpus pour cette source. Il est alimente par le
WORLDBUILDER : le MJ ne voit pas le jeu, il ne peut ni produire ni verifier une observation, il
peut seulement la croiser avec le corpus.

Balise `[VISUEL]` : fait de design observable, verifiable par quiconque regarde l'ecran. C'est
du contenu du JEU, donc du meme rang que le texte - a distinguer de `[HORS-JEU]` (trailer,
artbook) et `[CANON LOCAL]` (theorie promue par decision), cf. _Implications.md Q8.

Regle de stratification, jamais fusionnee : le FAIT visuel porte `[VISUEL]`, la LECTURE qu'on
en tire porte `[INTERPRETATION]`. Chaque observation declare en outre si le corpus la corrobore,
l'ignore ou la contredit.

## REGIME D'INDEXATION - exception documentee a la SPEC_BIBLE_LORE_WIKI v8.2

La SPEC prevoit un Sommaire qui liste UNE ENTREE PAR PAGE. Le corpus Elden Ring compte 3538
entrees de texte de jeu, 436 lieux nommes et 254 PNJ nommes : un index plat de tout le perimetre
depasserait la taille utilisable d'un fichier fetche en entier a chaque ouverture de thread.

Decision du worldbuilder (2026-07-24) : la SPEC reste en v8.2, sans modification de Config/.
Elden Ring documente ici son exception. Indexation a trois etages :

1. Sommaire.md (ce fichier) - taille FIXE. Liste les BRANCHES, et nomme individuellement les
   seules pages redigees, qui restent peu nombreuses par construction.
2. <Branche>/_Index.md - sous-sommaire de branche, porte les versions W<N> de ses pages.
3. _Concordance/ - filet de recherche vers le corpus : nom exact d'un item -> fichier qui le
   contient. Retrouver un item coute UN fetch.

Ecart assume avec la regle anti-boucle de la SPEC (S1) : un renvoi du Sommaire mene ici a un
autre index, pas directement au fait. L'anti-boucle reste en vigueur pour les renvois de
CONTENU ; elle n'est levee que pour les renvois de NAVIGATION, sur ces trois etages.

## REGLE NIGHTREIGN

Decision du worldbuilder (2026-07-24) : continuite SEPAREE, avec pont balise.
- La branche Nightreign/ est autonome : Nightfarers, Nightlords, Limveld, mecaniques propres.
- Un fait Nightreign qui eclaire le lore ELDEN RING remonte dans la fiche ER concernee, marque
  `[SOURCE NIGHTREIGN]` et accompagne de son niveau de certitude. Tracable, donc revocable.
- Le sens inverse est INTERDIT : le lore ER ne comble pas les trous de Nightreign par defaut.

## NIVEAUX DE CERTITUDE

Doctrine graduee. Un fait sans balise est ETABLI, c'est-a-dire enonce dans le texte du jeu et
localise dans le corpus. Sinon : `[IMPLICITE]`, `[INTERPRETATION]`, `[INCERTAIN]`,
`[DIVERGENCE RP]`, plus `[SOURCE NIGHTREIGN]`, `[VISUEL]` et `[COUPE]` propres a cet univers.

`[COUPE]` : contenu present dans les fichiers du jeu mais RETIRE de la version finale. Le dump
est un dump de fichiers, pas de contenu joue : il contient des PNJ coupes que rien ne distingue
du contenu actif. Ce contenu est CONSERVE et EXPLOITABLE (decision du worldbuilder,
2026-07-25) : ce n'est pas un fait du monde joue, mais c'est une source officielle de
FromSoftware, donc du materiau de lore legitime - au-dessus d'une theorie de fans, en dessous du
contenu joue. Un trou comble par cette voie garde la balise, donc reste revocable. Le MJ ne peut
pas detecter ces cas seul ; ils sont signales par le worldbuilder. Cas connu : Guilbert.
Detail : cf. _Corpus/_Attributions_Validees.md.

Regle de citation : toute affirmation d'une page redigee doit etre retrouvable dans le corpus a
l'emplacement indique. Une citation est reproduite a la casse et a la lettre.

## WIKI

### (racine)
Description : pages de travail et index.
- _Implications.md (W5) - journal de travail du build (jamais fetche en narration)
- _Questions_Worldbuilder.md (W2) - 136 questions remontees par le build autonome, aucune
  tranchee. A lire avant de reprendre le chantier.
- _Observations_Visuelles.md (W1) - registre de la narration visuelle, alimente par le
  worldbuilder. 2 observations consignees.
- _Relecture_Croisee.md (W1) - collisions inter-pages relevees a la cloture de la carte
  structurelle.
- _Observations_Visuelles.md (W1) - registre de la narration visuelle, alimente par le
  worldbuilder. 2 observations consignees.

### _Corpus/
Description : SOURCE PRIMAIRE. Texte integral du jeu, nettoye ASCII, non redige. Tient le role
de catalogue exhaustif. JAMAIS fetche en narration.
- _Index_Corpus.md (W1) - inventaire des 37 fichiers de corpus
- 41 fichiers de corpus - detail : cf. _Index_Corpus.md
- _Table_Locuteurs.md (W1) - table identifiant / personnage, etablie par auto-identification
  dans le texte. 53 entrees. Limite : dit qu'un bloc CONTIENT une identification, pas que
  toutes ses repliques sont du meme locuteur.
- _Attributions_Validees.md (W1) - decisions d'attribution prises avec le worldbuilder. FONT
  AUTORITE sur les pages. Porte l'alerte CONTENU COUPE.
- NR_Names_01.md et NR_Names_02.md (W1) - ELDEN RING NIGHTREIGN, NOMS SEULS, aucun lore.
  EXCLUS du perimetre des pages Elden Ring et de tout comptage d'occurrences.

### _Concordance/
Description : filet de recherche nom d'item -> fichier de corpus qui le contient.
- _Index_Concordance.md (W1) - gabarit et regle de decoupage. Aucune concordance buildee.

### Cosmologie/
Description : structure du monde et instances qui le gouvernent.
- _Index.md (W2) - sous-sommaire de branche
- Erdtree.md (W1) - nature, forme primordiale (Crucible), racines et Greattree, cycle des ames,
  Minor Erdtrees, Erdtree Burial, etat apres le Shattering. 4 trous documentes.
- Elden_Ring_et_Elden_Beast.md (W1) - l'anneau, ses runes, les Great Runes comme fragments,
  l'anneau d'ancrage, le Shattering subi par l'objet, l'Elden Beast. 5 trous.
- Greater_Will_et_les_Fingers.md (W1) - le Greater Will, Two et Three Fingers, Finger Readers
  et Maidens, Metyr, la transmission des messages et sa rupture. 5 trous.
- Outer_Gods.md (W1) - le terme et ses emplois, Formless Mother, le dieu scelle de la rot, le
  fell god du feu, statut non tranche du Greater Will et de la Frenzied Flame. 5 trous.
- Lands_Between_et_Land_of_Shadow.md (W1) - geographie cosmologique, Sea of Fog, realm of
  shadow, Scadutree, ce qui existe hors des Lands Between. 5 trous.

### Systemes/
Description : regles du monde et mecaniques de pouvoir. Coeur de la carte structurelle.
- _Index.md (W2) - sous-sommaire de branche
- Destined_Death.md (W1) - PAGE PILOTE. Rune of Death, confinement par Maliketh, Night of the
  Black Knives, cursemark, Deathroot, Those Who Live in Death, Gloam-Eyed Queen.
  Porte 6 trous documentes, dont le TROU 1 partiellement resolu par Golden_Order.md.
- Golden_Order.md (W1) - acte fondateur, regression et causality, Elden Ring comme racine,
  exclusions, fundamentalism et defections. 4 trous documentes.
- Grace.md (W1) - siege oculaire, guidance, Tarnished et graceless, sites of grace, rapport aux
  Two Fingers. 4 trous documentes.
- Crucible.md (W1) - forme primordiale de l'Erdtree, les Aspects, les Crucible Knights, statut
  dans le Golden Order, rapport aux Omen. 5 trous.
- Runes_et_Great_Runes.md (W1) - economie des runes, Golden Runes, Great Runes des
  shardbearers, Mending Runes, Divine Towers, restauration de l'anneau. 5 trous.
- Those_Who_Live_in_Death.md (W1) - nature, Deathroot, Deathbirds et ghostflame, les chasseurs,
  Fia et les Deathbed Companions, les Duskborn. 5 trous.
- Empyreans_et_succession_divine.md (W1) - qui peut devenir dieu, designation par les Fingers,
  shadowbound beasts, vaisseaux, consorts. 5 trous.
- Sorceries.md (W1) - glintstone et Academy, conspectus, Carian, gravitationnelle, cristal,
  nuit, primeval current. 5 trous.
- Incantations.md (W1) - ecoles et sceaux sacres, Erdtree, fundamentalist, dragon communion,
  flamme, sang, godslayer, bestial. 5 trous.
- Frenzied_Flame.md (W1) - Three Fingers, Lord of Frenzied Flame, contamination, Shabriri,
  Midra, doctrine du One Great. 5 trous.
- Scarlet_Rot.md (W1) - nature, Aeonia, Malenia Goddess of Rot, dieu scelle, Kindred of Rot,
  aiguilles d'or non allie. 5 trous.

### Factions/
Description : groupes, lignees et institutions.
- _Index.md (W3) - sous-sommaire de branche
- Golden_Lineage.md (W1) - Marika, Godfrey, Radagon, les demi-dieux et les filiations
  reellement attestees, les deux ages. 5 trous.
- Carian_et_Raya_Lucaria.md (W1) - maison royale Carian et Academie, Rennala et Radagon, la
  rupture, la guerre contre le clerge, la lune. 5 trous.
- Black_Knives_et_Numen.md (W1) - les assassines, Alecto et Tiche, le rite des lames, la fuite,
  ce que le corpus dit et tait du commanditaire. 5 trous.
- Omen_et_Hornsent.md (W1) - cornes et Crucible, la persecution, le sous-sol de Leyndell,
  Morgott et Mohg, les hornsent du Land of Shadow. 5 trous.
- Ancient_Dragons_et_Dragon_Cult.md (W1) - Placidusax, Fortissax, la dragon communion, Farum
  Azula, la guerre contre l'Erdtree. 5 trous.
- Nox_Eternal_Cities_et_Albinaurics.md (W1) - Nokron et Nokstella, la haute trahison, le Lord
  of Night attendu, les Silver Tears, les Albinaurics. 5 trous.

### Chronologie/
Description : trame temporelle du lore. Le referentiel de datation reste A ARBITRER : le corpus
ne fournit quasiment aucune date absolue.
- _Index.md (W2) - sous-sommaire de branche
- Chronologie_Generale.md (W1) - ordre RELATIF des evenements etabli a partir des seuls
  marqueurs textuels, sept designations d'epoque relevees. 5 trous.
- Night_of_the_Black_Knives.md (W1) - deroulement atteste, acteurs nommes, double mort,
  cursemark, ce que le corpus declare volontairement cache. 5 trous.
- Shattering.md (W1) - la brisure et la guerre, les shardbearers, l'exil et le rappel des
  Tarnished, l'etat du monde apres. 5 trous.

### Personnages/
Description : fiches individuelles. Creees A LA DEMANDE, quand un arc convoque l'entite
(doctrine ORDRE DE CONSTRUCTION, boucle serree de Passe 2). Les figures structurelles - Marika,
Radagon, Ranni, Godwyn, Maliketh, Miquella, Malenia - sont couvertes par la carte structurelle
avant d'avoir leur fiche propre.
- _Index.md (W1) - sous-sommaire de branche. Aucune page buildee.

### Lieux/
Description : fiches individuelles de lieux. Memes regles que Personnages/ : a la demande.
- _Index.md (W1) - sous-sommaire de branche. Aucune page buildee.

### Artefacts/
Description : objets a role narratif propre. Un objet n'a de fiche que s'il joue un ROLE dans
une histoire, pas parce qu'il porte du lore - sinon il vit dans le corpus.
- _Index.md (W1) - sous-sommaire de branche. Aucune page buildee.

### Nightreign/
Description : couche ELDEN RING NIGHTREIGN, continuite separee. Corpus NON CONSTITUE.
- _Index.md (W1) - sous-sommaire de branche. Aucune page buildee.

### Roadmap/<Prota>/
Description : itineraires par arc, par perspective de prota. SOURCES DE BUILD uniquement, lues
par listing de dossier, jamais fetchees en narration (SPEC v8.2). Passe 2 - aucune page.

### Fiches_Arc/<Prota>/
Description : fiches de narration par arc, mini-bible autosuffisante tronquee a la frontiere de
l'arc. Chargees une fois a l'ouverture de thread. Passe 3 - aucune page.

## PARTIES (Partie1)

Vide - s'ouvre au CODEX V1 : Suivi/ (fiches des personnages affectes par la narration),
Archives/ (chronologie archivee, arcs clos), Decisions/ (bifurcations prises dans ce RP).

---

FIN_WIKI_SOMMAIRE
