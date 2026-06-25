# SPEC_BIBLE_LORE_WIKI v8.2

Ce fichier definit la forme, les regles de construction et le gabarit du systeme BIBLE_LORE + WIKI + Parties :
- `BIBLE_LORE_{UNIVERS}.md` - index de routage + lore condense, fichier de projet lu en integralite par le MJ.
- WIKI GitHub (`{Univers}/`) - pages .md du monde, consultees par fetch a la demande. Cout zero en contexte tant que non fetchees.
- Parties GitHub (`Parties/{Univers}/Partie<n>/`) - memoire froide du RP, arcs joues, tracking PNJ, CHRONO archivee. Consultees par fetch a la demande. Chaque `<n>` correspond a un RP distinct dans le meme univers.

Le modele doit produire des documents factuels, structures, sans narration, sans interpretation non balisee.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_BIBLE_LORE_WIKI_v8_2.md`.

---

## 1. Role et position hierarchique

La BIBLE_LORE est le point d'entree du systeme de reference lore. Elle contient :
1. Le lore condense de l'univers (SB0-SB8), lisible seul, autosuffisant pour les faits essentiels.
2. Les definitions des fils Tchekhov du RP (SB8), migrees depuis le CODEX.
3. L'index de routage (SB9) vers les pages WIKI et Parties/ pour le detail.

Le WIKI (`{Univers}/`) contient le monde : fiches personnages, chronologie detaillee, roadmaps, power-scaling, lore approfondi.

Les Parties (`Parties/{Univers}/Partie<n>/`) contiennent la memoire froide d'un RP donne : arcs joues, CHRONO archivee, fiches de suivi des PNJ affectes par la narration, fiche protagoniste, decisions et bifurcations prises. Chaque Partie<n> est un RP autonome dans le meme univers.

Hierarchie :
`OOC joueur > CODEX > { BIBLE_LORE, WIKI } > Canon externe > #SITES_REF > improvisation`

BIBLE et WIKI au meme echelon, arbitres par SCOPE : sur le detail specialise d'un sujet qui a une fiche, la FICHE prime (la BIBLE resume, la fiche detaille) ; sur le structurel/transversal (cosmogonie, regles du monde, index de routage), la BIBLE prime. Contradiction FRANCHE (au-dela d'un simple ecart de granularite) = l'une est perimee -> signaler au joueur, ne pas trancher seul. Les deux priment sur le canon externe. Le CODEX ne duplique ni la BIBLE ni le WIKI - il stocke l'etat courant, les capacites / description physique / resume de backstory du protagoniste, et les divergences fraiches. L'INSTANCE jouee du protagoniste (etat, run courant) vit en CODEX + Parties, pas dans la BIBLE/WIKI. Mais son ENTITE, si elle existe independamment de la partie (personnage canon, ou OC promu au lore), est decrite neutrement comme toute entite - cf. regle de placement (S7). Anti-boucle : un renvoi `cf.` mene toujours a un emplacement qui CONTIENT le fait, jamais a un autre renvoi.

## 2. Quand utiliser le systeme

Le systeme BIBLE_LORE + WIKI est utilise des que l'univers necessite un socle de lore fiable que le MJ ne peut pas reconstituer de memoire. Le joueur decide en setup si une BIBLE est necessaire.
- Si oui : BIBLE + WIKI portent le lore canon et les divergences etablies. Le CODEX ne stocke que la memoire chaude de session.
- Si non (codex pur) : le MJ se fie a ses connaissances + fetch. Le CODEX porte les divergences et les faits canon critiques.

## 3. Architecture a quatre couches

```
CODEX (vivant, memoire chaude de session)
  |-> BIBLE_LORE (index + lore condense, fichier de projet, lue en entier)
  |     |-> WIKI GitHub {Univers}/ (pages .md du monde, fetch a la demande)
  |     |     |-> {Univers}/Roadmap/<Prota>/ (itineraires par arc, par perspective de prota)
  |     |     |-> {Univers}/Fiches_Arc/<Prota>/ (fiches de narration par arc : casting tronque a la frontiere de l'arc, chargees une fois a l'ouverture de thread)
  |-> Parties/{Univers}/Partie<n>/ (memoire froide d'un RP donne, fetch a la demande)
        |-> Suivi/ (fiches PNJ affectes, protagoniste)
        |-> Archives/ (CHRONO archivee, arcs clos)
        |-> Decisions/ (bifurcations prises dans ce RP)
```

Le CODEX ANNEXE_CHRONO pointe vers la fiche d'arc COURANTE via `fiche_arc: cf. WIKI Fiches_Arc/<Prota>/<page>.md`, et tient le FIL LONG des arcs traverses (suite ordonnee des arcs deja joues -> arc courant -> arc suivant prevu) : c'est lui, pas la roadmap, qui porte la memoire du chemin parcouru en jeu. Le renvoi `roadmap: cf. WIKI Roadmap/<Prota>/<page>.md` ne sert qu'au BUILD (creer la fiche d'arc) et n'est PAS fetche en narration. La fiche d'arc et la roadmap sont par perspective de prota ; les decisions specifiques a un RP sont tracees dans `Parties/{Univers}/Partie<n>/Decisions/`, et le passe joue archive dans `Parties/{Univers}/Partie<n>/Archives/`.

### Roadmap, fiche d'arc, CODEX : trois roles distincts
- ROADMAP (`Roadmap/<Prota>/`) : l'ITINERAIRE de toute la saga - les jalons jouables dans l'ordre, conditions d'avancement, bifurcations, futur compris. SOURCE DE BUILD UNIQUEMENT : matiere premiere des fiches d'arc (une etape = une fiche), lue en mode Wiki en listant le dossier. NON indexee au Sommaire, JAMAIS fetchee en narration (le MJ qui lirait le futur de la saga prefigurerait en prose). Reste au repo comme reference de construction.
- FICHE D'ARC (`Fiches_Arc/<Prota>/`) : la MINI-BIBLE AUTOSUFFISANTE de l'etape - casting + lieux + objets + lore d'arc condense, tout decrit dans l'etat ou il est A L'OUVERTURE de l'arc, rien d'apres. Document de jeu permanent : charge une fois a l'ouverture de thread, reste tout le thread ; remplace en jeu le fetch entite-par-entite ET la lecture de la grosse BIBLE. Maillon de navigation : porte `arc precedent` / `arc suivant` (chainage local de proche en proche, sans index global). La troncature a la frontiere empeche le MJ de prefigurer le futur en prose.
- CODEX (ANNEXE_CHRONO) : l'ETAT D'ARC vivant ET LE FIL LONG - jalon courant, prochain jalon, statut, PLUS la suite ordonnee des arcs deja traverses (memoire du chemin parcouru). Reinjecte en tete chaque tour (immunite lost-in-the-middle). C'est le CODEX - pas la roadmap (futur prevu, hors jeu), pas la fiche d'arc (qui ignore le passe) - qui tient ou on en est ET d'ou l'on vient. Le detail archive du passe joue (scenes closes) vit dans Parties/Archives, fetchable a la demande.

> ANTI-AMNESIE (v8.2). En jeu on ne consulte ni la grosse BIBLE ni les roadmaps. La memoire de l'histoire ne repose donc PAS sur ces deux sources mais sur deux autres, par horizon : (a) MEMOIRE LONGUE / coherence du chemin -> CODEX ANNEXE_CHRONO (fil ordonne des arcs traverses) + Parties/Archives (detail des scenes closes, fetch a la demande) ; (b) ARC COURANT -> la fiche d'arc chargee. La roadmap decrit le FUTUR PREVU, pas le PASSE VECU : ce n'est pas un substitut de memoire. Si un fait de fond profond manque vraiment et n'est ni en CODEX, ni en fiche, ni en Archives -> fetch cible Parties/Archives ou, en dernier recours hors jeu, la BIBLE complete.

### Flux de resolution d'un fait lore
1. CODEX (divergence fraiche du RP ?) -> si oui, utiliser.
2. BIBLE_LORE SB0-SB8 (fait condense ?) -> si oui, utiliser.
3. BIBLE_LORE SB9 -> Sommaire.md (deja en contexte depuis le fetch initial) : identifier la page, puis fetch de la page.
4. Fetch / #SITES_REF (canon externe) -> si hors perimetre BIBLE + WIKI.
5. Invention prudente -> coherente avec les echelons superieurs.

---

## 4. BIBLE_LORE - Principes redactionnels

- Dense > exhaustif. Ligne telegraphique > phrase pleine.
- FOCUS : la bible ne couvre que le PERIMETRE NARRATIF defini par le joueur.
- Pas de narration, pas de prose, pas de metaphores.
- Pas d'adjectifs decoratifs ni de jugements de valeur.
- Phrases > 25 mots interdites.
- Redaction ASCII STRICTE (diacritiques retires des lettres ET tout caractere non-ASCII converti), meme regle que le CODEX et que l'INSTRUCTION S3.4 :
  - Symboles : signe section U+00A7 -> "S" (donc SB0..SB9) ; tiret cadratin U+2014 -> "-" ; guillemets U+00AB / U+00BB -> guillemet droit " ; fleche U+2192 -> -> ; apostrophe courbe U+2019 -> apostrophe droite '.
  - Allemand : u-trema -> u ; o-trema -> oe ; a-trema -> ae ; eszett -> ss (ex. Ubung, schoen, Maedchen, Strasse).
  - Francais : accents retires dans les fichiers ; reaccentues en narration.
  - Japonais / coreen : romanisation ASCII ; kanji et hangul jamais ecrits (romanisation + glose si mot porteur).
  - Verification avant chaque sortie : grep -nP '[^\x00-\x7F]' sur le fichier genere doit revenir vide. Regle de portee : tout fichier .md du systeme est en ASCII strict (BIBLE_LORE, pages WIKI, fichiers Parties/, SPEC, et le CODEX - cf. SPEC_CODEX, qui n'exempte plus le signe section ni le cadratin) ; les instructions de projet (.txt) restent accentuees pour la lisibilite humaine.
- Ingestion : nom fetche en forme accentuee converti en ASCII a l'ecriture, jamais reinjecte accentue. Pour interroger le canon, requeter la forme d'origine accentuee.
- Aucune theorie de fans. Aucune speculation non balisee.

### Niveaux de certitude
Chaque fait porte implicitement le niveau "etabli" sauf balisage contraire :
- `[IMPLICITE]` - fortement implique par le canon mais jamais enonce explicitement.
- `[INTERPRETATION]` - lecture coherente mais debattue ou ambigue. Le joueur tranche en OOC si le RP touche ce point.
- `[INCERTAIN]` - information contradictoire ou insuffisante dans les sources.
- `[DIVERGENCE RP]` - divergence du RP par rapport au canon, formalisee et validee par le joueur.

## 5. BIBLE_LORE - Budget

Plafond dur : 55 000 caracteres.
Plus de contrainte de cohabitation CODEX + BIBLE (v8.2) : le CODEX V1 se build a la fin des instructions Wiki, une fois la BIBLE retiree des fichiers de projet (bascule jeu, tout-ou-rien). BIBLE et CODEX ne sont jamais charges simultanement ; l'ancien plafond commun (<= 100 000, seuil RAG) est retire. La BIBLE garde son plafond propre de 55 000 caracteres pour la phase build.
Verification au build : `wc -m` (caracteres, locale UTF-8) sur le fichier genere. Depassement : signaler, proposer des compressions par gain decroissant (caracteres recuperes + ce qu'on perd), le worldbuilder tranche. Compresser, jamais supprimer l'information utile sans validation.

Repartition indicative (guide, pas plafonds rigides par section) :

| Bloc | Fourchette | Role |
|---|---|---|
| SB0 | 1-2k | Metadonnees, wiki_base, parties_base |
| SB1-SB4 | 5-12k | Cosmogonie, lexique, chronologie condensee, factions |
| SB5 | 8-20k | Personnages (syntheses, croissance principale) |
| SB6-SB7 | 2-5k | Lieux, artefacts |
| SB8 | 2-5k | Mysteres ouverts + definitions Tchekhov |
| SB9 | <1k | Pointeur vers {Univers}/Sommaire.md (index detaille hors BIBLE, taille fixe) |

Principe directeur : SB1-SB8 contiennent assez pour que le MJ ne soit pas perdu sans fetcher. Le detail vit sur le WIKI et dans Parties/. Si une section (SB2, SB6, SB7) n'apporte pas de contexte ambiant indispensable, elle peut etre allegee et vivre principalement sur le WIKI.

## 6. BIBLE_LORE - Architecture des sections

Fichier unique, lu en integralite par le MJ a chaque tour.
Chaque section a un identifiant stable (`SB0`, `SB1`...).

### BIBLE auto-portante
Les sections pas encore remplies conservent le gabarit de la SPEC (lignes de structure, champs, format). Ainsi le MJ sait quoi remplir au prochain build sans refetcher la SPEC. La BIBLE livree n'a jamais de section vide sans structure.

### Sections (ordre fixe, toutes optionnelles sauf SB0, SB1, SB9)

#### SB0 Metadonnees [OBLIGATOIRE]
- univers :
- sources primaires : <liste>
- bible_version : B<N>
- wiki_base : <URL racine du WIKI GitHub>
  Format : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
  Toutes les URLs WIKI de SB9 se construisent par concatenation : wiki_base + chemin relatif.
- parties_base : <URL racine de Parties/ GitHub pour le RP en cours>
  Format : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
  Toutes les URLs Parties de SB9 se construisent par concatenation : parties_base + chemin relatif.
- pages wiki rattachees :
  - <Dossier> - <description courte> (<N> pages)

#### SB1 Cosmogonie et regles du monde [OBLIGATOIRE]
Comment le monde fonctionne dans le perimetre du focus.
Inclut les divergences RP formalisees (balisees `[DIVERGENCE RP]`).
- <regle 1>
- <regle 2>

#### SB2 Lexique
`Terme - definition (1 ligne max)`

#### SB3 Chronologie
`Date/Ere | Evenement | Consequence`

Detail des etapes par arc : cf. {Univers}/Roadmap/<Prota>/ (fetch obligatoire en debut de thread pour l'arc en cours).

Notes de cadrage chronologique en fin de SB3 sous `### Notes`.

#### SB4 Factions et groupes
`Faction - nature | objectif | allies | ennemis | statut dans le focus`

#### SB5 Personnages
Personnages decrits NEUTREMENT : ce qui existe independamment d'une partie. Canon, ET OC promus au lore (un OC peut etre prota dans une partie et entite de monde dans une autre - ex. un demon originel qui enrichit la theologie). La distinction n'est pas "OC vs canon" mais "existe sans cette partie ?".
- L'INSTANCE jouee d'un prota (etat, run courant) ne figure PAS ici : elle vit en CODEX S3. Mais l'ENTITE, si elle existe hors de la partie, est decrite ici comme toute autre.
- Une RELATION a un prota va en perspective ou en neutre selon que le prota est un vehicule d'instance ou une entite de lore - decision worldbuilder, cf. regle de placement (S7).

Contenu AUTORISE :
- identite, role, affiliation, capacites, relations, sort connu ;
- traits comportementaux observables dans les sources ;
- motivations explicitement enoncees ou fortement impliquees ;
- rapport a une autre entite de lore (synthese) ; un rapport a un prota-instance va en perspective, cf. S7.

Contenu INTERDIT :
- voix (registre, tics verbaux, ton) - ANNEXE_PNJ du CODEX ;
- etat actuel dans le RP - CODEX S4 ;
- interpretation psychologique non fondee.

La frontiere : la BIBLE dit QUI ils sont et CE QU'ILS ONT FAIT. Le CODEX dit COMMENT ils parlent et OU ils en sont.

Format :
`Nom - role | capacites-cle | relations | sort connu | certitude`
Si fiche WIKI detaillee : `detail: cf. WIKI <page>.md`. La BIBLE indexe le monde (= WIKI) ; Parties/ (archive d'une partie) s'atteint via le Sommaire, jamais par renvoi BIBLE.

#### SB6 Lieux
`Lieu - nature | rattachement | fonction narrative | etat connu`

#### SB7 Artefacts et objets
Objets narrativement significatifs (pas l'inventaire du RP - cf. CODEX ANNEXE_INVENTAIRE).
`Objet - nature | origine | pouvoir/fonction | localisation connue | certitude`

#### SB8 Mysteres ouverts et fils Tchekhov
Deux sous-sections :

##### Mysteres
Questions non resolues, pertinentes au focus. Le MJ doit savoir ce qui est volontairement flou.
`Mystere - hypotheses principales | statut (ouvert / resolu-dans-RP / hors-perimetre)`

##### Tchekhov
Definitions des fils narratifs plantes dans le RP. L'ETAT de chaque fil (ouvert/arme/paye) est dans le CODEX ANNEXE_TCHEKHOV. La BIBLE porte les definitions stables.
`Fil - plante en | condition de detonation | consequence attendue`

#### SB9 Index - routage [OBLIGATOIRE si WIKI present]
SB9 ne contient PAS l'index detaille page-par-page. Cet index vit dans `{Univers}/Sommaire.md` (page WIKI fetchee au debut de chaque thread, cf. Instructions RP S4), pour que SB9 reste de taille fixe et ne croisse plus avec le nombre de pages.

Contenu de SB9 :
- `Index detaille page-par-page : cf. WIKI {Univers}/Sommaire.md`

Regles de SB9 :
- L'inventaire des dossiers (avec compte de pages) est deja dans SB0 `pages wiki rattachees` - il sert de filet de securite si Sommaire.md tombe (listing direct via la methode dossier de ACCES GITHUB).
- SB1-SB8 portent le resume ambiant : le MJ sait CE QUI EXISTE sans fetch. Sommaire.md dit OU est le detail. La page cible porte le detail.
- Sommaire.md est fetche au debut de chaque thread RP (carte de navigation centrale) et reste en contexte. Fetche tot pour rester saillant (eviter le lost-in-the-middle). Regles d'usage : Instructions RP S4.
- Chaque page reste une unite autonome, fetchee en entier. L'URL se construit : `wiki_base` ou `parties_base` (SB0) + `<Dossier>/<Page>.md`.

---

## 7. WIKI - Specification des pages

### Placement d'une fiche (regle generale, tous univers)
Pas de liste de categories en dur : la structure s'organise par PRECEDENT.
1. Consulter le Sommaire. Si le TYPE de fiche existe deja -> s'aligner sur le dossier existant (precedent). Sinon -> appliquer les regles generiques de cette SPEC (granularite, nommage, neutre vs perspective) et creer le dossier.
2. Contenu qui existe INDEPENDAMMENT de toute partie -> branche neutre `<Type>/`, decrit en lui-meme. Un OC promu au lore en fait partie : son histoire ET ses relations sont du lore neutre.
3. Des qu'une fiche MENTIONNE un prota, ou contient un element potentiellement specifique a une partie -> l'IA DEMANDE : lore neutre, ou sous-branche perspective `<Type>/<Prota>/` ? Le worldbuilder seul tranche, parce que la reponse depend de son intention (l'OC est-il destine au lore, ou vehicule d'instance ?). Jamais d'automatisme : le meme OC peut etre prota ici et entite-monde ailleurs.
4. Build pour un nouveau prota : pour chaque fiche pertinente, trois issues - RIEN A FAIRE / AJOUTER une sous-branche `<Type>/<Prota>/` / CREER en sous-branche. Ne jamais modifier la branche neutre ni les autres sous-branches sans validation.

Exemples d'arborescence : `Personnages/Macht/` (Macht neutre) ; `Personnages/<Prota>/` (perspective : relations a ce prota) ; `Roadmap/<Prota>/` (itineraire vu par ce prota). Le neutre est l'intrant reutilisable, la sous-branche `<Prota>/` est ce qu'on ajoute par perspective - zero retouche du neutre quand on ajoute un prota.

### Nature
Les pages WIKI sont des fichiers .md heberges sur un depot GitHub public. Chaque page est une unite de consultation autonome, fetchee en entier.

Types de pages possibles :
- Sommaire (index detaille de toutes les pages WIKI et Parties - voir gabarit ci-dessous).
- Fiches personnages approfondies (neutres `<Type>/` ou perspective `<Type>/<Prota>/`).
- Descriptions de lieux.
- Roadmaps (itineraires par arc, par PERSPECTIVE de prota : `Roadmap/<Prota>/`).
- Fiches d'arc (casting d'un arc tronque a sa frontiere, par PERSPECTIVE de prota : `Fiches_Arc/<Prota>/` - voir gabarit ci-dessous).
- Power-scaling.
- Systemes de magie/combat detailles.
- Tout decoupage thematique pertinent au RP.

### Principes redactionnels
- Meme registre que la BIBLE : factuel, sans accent, sans narration.
- Niveaux de certitude identiques : etabli / [IMPLICITE] / [INTERPRETATION] / [INCERTAIN] / [DIVERGENCE RP].

### Budget par page
- Fourchette : 500 a 2000 tokens (~2000 a 8000 caracteres).
- En dessous de 500 tokens : fusionner avec une page voisine.
- Au-dela de 2000 tokens : scinder en sous-pages.
- Exception : pages transcript jusqu'a 4000 tokens.

### Structure interne d'une page
Pas de gabarit impose sauf pour les Roadmaps (cf. gabarit ci-dessous). Obligations :
1. Titre clair en H1, correspondant au nom de la page.
2. Metadonnee unique : version (W<N>). Aucune autre metadonnee (pas d'univers, dossier, sources, bible rattachee : l'indexation va de la BIBLE vers la page via le Sommaire, jamais l'inverse).
3. Contenu structure en sections si pertinent.
4. Pas de contenu narratif (sauf pages transcript = verbatim).

### Trajectoire datee (gabarit fiche d'entite)
Troisieme strate de toute fiche perso/lieu/objet. Decrit le DEVENIR DATE de l'entite APRES le point de depart. N'existe que dans la fiche pleine ({Univers}/). INTERDITE dans la fiche d'arc.
Regles :
- Forme telegraphique, une ligne par evenement. Pas de prose ; le detail narratif vit dans la roadmap.
- ALIMENTATION A CHAUD : une entree est ajoutee UNIQUEMENT apres avoir roadmappe l'arc qui la produit. Jamais d'anticipation.
- CANON PAR DEFAUT, neutre, reutilisable entre parties (comme roadmaps et fiches d'arc).
- OVERRIDE PAR PARTIES/ : quand une partie diverge, le delta va en Parties/{Univers}/Partie<n>/ et SURCLASSE cette strate pour la partie concernee (routage S7 inchange).
- CONSOLIDATION : les pointeurs dates jadis en Notes de frontiere (mort canon, eveil, depart...) migrent ici sous forme datee ; Notes de frontiere ne garde que les renvois non dates et les hors-perimetre.
- PLAFOND : <N> entrees max par fiche [A FIXER PAR LE WORLDBUILDER] ; au-dela, compresser ou deporter en roadmap, depassement signale jamais compresse seul.
Gabarit :
```
## Trajectoire datee
| Date/ere | Evenement | Delta d'etat |
|---|---|---|
| <date> | <evenement telegraphique> | <ce qui change : grade, doigts, sort debloque, statut, relation> |
```
Exemple de FORMAT (illustratif, NE PAS inscrire tel quel) :
```
| 2006 | Affrontement de Toji, eveil | passe a 23 doigts ; debloque Rouge, Violet, Extension de Territoire |
```

### Gabarit Roadmap

Les roadmaps vivent dans `{Univers}/Roadmap/<Prota>/`. Elles decrivent les itineraires par arc, par perspective de prota. Les decisions prises dans un RP donne sont tracees dans `Parties/{Univers}/Partie<n>/Decisions/`.

```
# Roadmap_<Arc>

- statut : <en cours | a venir | clos>
- version : W<N>

## Conditions de depart
- <prerequis narratif 1>
- <prerequis narratif 2>

## Etapes
| # | Etape | Lieu | PNJ impliques | Tchekhov lies | Duree | Condition d'avancement |
|---|---|---|---|---|---|---|
| 1 | <jalon> | <lieu> | <noms> | <fils> | <echelle temporelle reelle du bloc, ex. ~190 ans, ~3 jours, instantane> | <declencheur> |

Colonne DUREE (correctif ellipse v8.2) : chaque bloc jouable porte son echelle temporelle REELLE in-world ("~190 ans", "~3 jours", "une saison"). Elle dit au MJ a quelle vitesse le temps s'ecoule SUR CE BLOC, pour qu'il cale l'ecoulement par defaut sur l'arc et non sur son envie de scenes. Sans duree chiffree, le MJ condense des siecles en jours (bug constate). Regle d'ecoulement cote narration : Instructions RP S3 (ellipse par defaut bornee).

Bloc couvrant un long laps (annees/decennies) a rendre en vignettes : marquer la section `[SNAPSHOTS]`. Le MJ compresse alors en vignettes evocatrices au lieu de jouer chaque etape - compresser n'est PAS supprimer, le joueur doit sentir le temps passer (cf. Instructions RP, sequence de roadmap). Un bloc `[SNAPSHOTS]` porte d'autant plus une duree chiffree : c'est elle qui borne l'ampleur de l'ellipse.

## Bifurcations
- Apres etape <N> : si <condition A> -> <consequence>. Si <condition B> -> <consequence>.

## Conditions de cloture
- <condition de fin d'arc>
- <consequence sur l'univers>

---
FIN_WIKI_ROADMAP_<ARC>
```

### Gabarit Fiche d'arc

Les fiches d'arc vivent dans `{Univers}/Fiches_Arc/<Prota>/`, par perspective de prota, comme les roadmaps. C'est un DOCUMENT DE JEU PERMANENT : le MJ la charge une fois a l'ouverture de thread (cf. Instructions RP S4) et elle reste en contexte tout le thread, contrairement aux fiches d'entites fetchees a la demande.

GRANULARITE (regle ferme). Une ROADMAP couvre une saga / un gros bloc d'itineraire et se decompose en ETAPES. L'unite-arc, c'est l'ETAPE : UNE etape de roadmap = UN arc = UNE fiche d'arc. Pas de regroupement d'etapes, pas de decoupage a arbitrer - le decoupage est deja porte par la segmentation de la roadmap. Une roadmap de N etapes produit donc N fiches d'arc (le compte total peut etre eleve, c'est attendu et voulu).

Principe directeur : la roadmap dit OU on va (jalons de toute la saga, futur compris) ; la fiche d'arc est une MINI-BIBLE AUTOSUFFISANTE de l'etape - elle reunit TOUT ce qu'il faut pour jouer cette etape sans rouvrir la grosse BIBLE (source de confusion en jeu) : le casting en scene AU DEPART de l'etape, plus le lore d'arc condense (les points de BIBLE / fiches strictement pertinents pour cette etape, reformules court). Elle remplace a la fois le fetch entite-par-entite ET la lecture de la BIBLE en narration. MAIS elle reste tronquee a la frontiere de l'etape (cf. regle de troncature).

REGLE DE TRONCATURE (le coeur de la fiche). Chaque entite est decrite dans l'etat ou elle se trouve A L'OUVERTURE de l'arc - jamais d'apres :
- Etat, relations, position, savoir : tels qu'ils sont au premier battement jouable de l'arc.
- INTERDIT : ce qu'une entite devient, apprend, subit ou revele PLUS TARD dans l'arc ; sa mort future ; une trahison a venir ; un pouvoir pas encore acquis. Ces faits vivent dans la ROADMAP (cadrage MJ hors prose) et dans les fiches WIKI neutres completes (fetch a la demande si besoin de build), pas dans la fiche d'arc chargee en permanence.
- Un fait posterieur qui DOIT cadrer le MJ sans fuiter en prose va en roadmap, pas en fiche d'arc. La fiche d'arc est ce que le MJ peut avoir en tete en permanence SANS risquer de prefigurer.

IRONIE STRUCTURELLE vs PREFIGURATION SPECIFIQUE (distinction a ne pas confondre) :
- L'IRONIE DRAMATIQUE voulue par le worldbuilder (le joueur sait une chose qu'un PNJ ignore) est un MOTEUR de RP. Elle vit dans le CODEX (ANNEXE_SAVOIRS > Ironie dramatique active) et reste. La fiche d'arc tronquee ne la tue pas : elle empeche seulement le MJ d'en savoir trop sur la suite et de le laisser filtrer en prose.
- La PREFIGURATION SPECIFIQUE en prose ("ce qu'il ne comprendra que des siecles plus tard", un evenement futur annonce dans le recit) est une FUITE. C'est elle que la troncature coupe.
- Test : un fait sert l'ironie connue du JOUEUR (CODEX) -> garder cote CODEX. Un fait dit au MJ ce qui arrivera PLUS TARD dans l'arc -> roadmap, hors fiche d'arc.

Budget : la fiche d'arc est l'EXCEPTION au plafond des pages WIKI. Comme c'est le SEUL document de lore charge a l'ouverture (la BIBLE n'est plus lue en jeu), elle a le droit d'etre lourde : aussi courte que possible, aussi longue que necessaire pour etre autosuffisante sur l'etape. Pas de plafond serre type 500-2000 tokens. Reste oriente "ce qu'il faut pour jouer l'etape" : on rapatrie le lore PERTINENT, condense (pas d'extraits integraux de la BIBLE), jamais du remplissage. Si une etape est vraiment massive, scinder (ex. `Fiches_Arc/<Prota>/<Arc>_partie1.md`).

```
# Fiche_Arc_<Arc>

- version : W<N>
- roadmap liee : cf. WIKI Roadmap/<Prota>/Roadmap_<Arc>.md
- frontiere : etat decrit = OUVERTURE de l'arc. Rien d'ulterieur (cf. SPEC regle de troncature).
- arc precedent : cf. WIKI Fiches_Arc/<Prota>/Fiche_Arc_<ArcPrecedent>.md   (ou "aucun - premier arc")
- arc suivant : cf. WIKI Fiches_Arc/<Prota>/Fiche_Arc_<ArcSuivant>.md   (ou "aucun - fin ouverte / dernier arc")

> CHAINAGE LOCAL (v8.2). Les champs `arc precedent` / `arc suivant` font de chaque fiche un maillon : la navigation entre arcs se fait DE PROCHE EN PROCHE par ces pointeurs, sans repasser par un index global des roadmaps (les roadmaps ne sont plus indexees au Sommaire en jeu - cf. note Roadmap du Sommaire). BIFURCATION : si l'arc debouche sur plusieurs suites (ex. branche canon vs branche divergente), lister UN pointeur `arc suivant` par sortie, chacun annote de sa condition (ex. "si <condition A> -> Fiche_Arc_<X>.md ; si <condition B> -> Fiche_Arc_<Y>.md"). FIN OUVERTE : `arc suivant : aucun`. La MEMOIRE du chemin deja parcouru ne vit PAS ici (la fiche ignore le passe joue) : elle vit dans le CODEX ANNEXE_CHRONO (fil long des arcs traverses) et dans Parties/Archives - cf. section 3, trois roles.

## Cadre d'ouverture
- Lieu(x) de depart : <ou commence l'arc>
- Situation initiale : <etat du monde au premier battement, sans rien annoncer de la suite>
- Echelle temporelle de l'arc : <duree totale, ex. ~190 ans - cale l'ecoulement par defaut, cf. roadmap colonne Duree>

## Lore d'arc condense (mini-bible)
Le lore strictement necessaire pour jouer cette etape sans rouvrir la grosse BIBLE. Condense, reformule court (pas d'extraits integraux). Borne a l'ouverture de l'etape : un point de lore qui ne se REVELE qu'au cours de l'etape n'a pas sa place ici (cf. troncature).
- Contexte de l'etape : <ce qui s'est passe avant, l'enjeu de cette etape, ce qui amene les personnages la - vu depuis l'ouverture>
- Lore pertinent : <regles du monde, systemes, faits d'univers que le MJ doit avoir en tete pour CETTE etape - condense des sections BIBLE / fiches concernees, reformule>
- Enjeux et fils chauds : <Tchekhov actifs a l'ouverture (etat initial seul), savoirs / ironies en jeu - sans annoncer leur aboutissement>

## PNJ presents ou evoques a l'ouverture
Pour chaque PNJ : etat A L'OUVERTURE uniquement.
- <PNJ> - role a l'ouverture | relation au prota a l'ouverture | savoir a l'ouverture | fiche neutre : cf. WIKI <Type>/<page>.md

## Lieux de l'arc
- <Lieu> - etat/fonction a l'ouverture | fiche : cf. WIKI <Type>/<page>.md

## Objets presents ou evoques
- <Objet> - etat/localisation a l'ouverture | fiche : cf. WIKI <Type>/<page>.md

## Notes de frontiere
- <rappel explicite des faits volontairement ABSENTS de cette fiche parce que posterieurs a l'ouverture - sans les enoncer : "l'evolution de X au cours de l'arc -> roadmap", pas le contenu de l'evolution>

---
FIN_WIKI_FICHE_ARC_<ARC>
```

### Gabarit Sommaire

`{Univers}/Sommaire.md` porte l'index detaille que SB9 ne porte plus : une entree par page, groupee par dossier. C'est la carte de navigation du WIKI et de Parties/. Fetchee au debut de chaque thread RP. Mise a jour via BIBLE BUILD a chaque ajout de page.

```
# Sommaire - {Univers}

- version : W<N>

## WIKI

> Chaque entree porte la version `(W<N>)` de la page : inventaire de versions. Un ecart entre ce W<N> et celui ecrit dans la page elle-meme signale une copie perimee (canari, non bloquant).

### <Dossier>/
Description : <contenu du dossier en 1 ligne>
- <Page>.md (W<N>) - <description courte du contenu>

### Fiches_Arc/<Prota>/
Description : fiches de narration par arc (mini-bible autosuffisante tronquee a la frontiere de l'arc), par PERSPECTIVE de prota. Chargees une fois a l'ouverture de thread. Navigation entre arcs par chainage local (champs `arc precedent` / `arc suivant` de chaque fiche), pas par un index des roadmaps.
- Fiche_Arc_<Arc>.md (W<N>) - <description courte>

> ROADMAPS NON INDEXEES EN JEU (v8.2). Le dossier `Roadmap/<Prota>/` n'est PLUS liste au Sommaire. Les roadmaps restent physiquement au repo - ce sont des SOURCES DE BUILD (matiere premiere des fiches d'arc), lues en mode Wiki en listant directement le dossier `Roadmap/<Prota>/` (cf. ACCES GITHUB), jamais via le Sommaire. En jeu (RP), le MJ ne fetch jamais de roadmap : il navigue d'arc en arc par les fiches, et tient le fil long via le CODEX ANNEXE_CHRONO. Indexer les roadmaps au Sommaire les ferait croire fetchables en narration et alourdirait l'index sans usage de jeu - on les en sort donc volontairement.

## PARTIES (Partie<n>)

### Suivi/
Description : fiches de suivi des personnages affectes par la narration.
- <Page>.md (W<N>) - <description courte>

### Archives/
Description : chronologie archivee, arcs clos.
- <Page>.md (W<N>) - <description courte>

### Decisions/
Description : bifurcations prises dans ce RP par rapport aux roadmaps.
- Decisions_<Arc>.md (W<N>) - <description courte>

---
FIN_WIKI_SOMMAIRE
```

### Maintenance
Pages WIKI mises a jour via BIBLE BUILD. Statiques entre deux builds.
Cas particulier du Sommaire : les pages Parties/ creees par un CODEX BUILD (memoire refroidie) n'y apparaissent qu'au prochain BIBLE BUILD. Entre-temps, l'index Refroidi du CODEX (ANNEXE_CHRONO) fait foi - le test de fetch des Instructions RP croise Sommaire OU index Refroidi.

---

## 8. Parties - Specification

### Nature
Les pages Parties/ sont des fichiers .md heberges sur le meme depot GitHub, dans `Parties/{Univers}/Partie<n>/`. Elles constituent la memoire froide d'un RP donne. Chaque `Partie<n>` est un RP autonome dans le meme univers, ce qui permet de jouer plusieurs RP en parallele avec des bifurcations differentes.

### Structure
```
Parties/{Univers}/
  Partie1/
    Suivi/
      <Protagoniste>_Fiche.md - backstory COMPLETE + identite du protagoniste (froid, fetch a la demande). PAS les capacites ni l'etat : ils vivent dans le CODEX S3 (capacites ancrees en S3a). Le CODEX S3a porte le resume chaud de cette backstory.
      <PNJ>_Suivi.md - tracking des PNJ affectes par la narration
    Archives/
      CHRONO_<arc>.md - chronologie archivee d'un arc clos
    Decisions/
      Decisions_<arc>.md - bifurcations prises dans ce RP par rapport a la roadmap
  Partie2/
    Suivi/
    Archives/
    Decisions/
```

### Gabarit Decisions

Les pages Decisions/ tracent les choix specifiques a un RP par rapport a la roadmap commune. Elles permettent de comparer les parties entre elles.

```
# Decisions_<Arc>

- partie : <n>
- version : W<N>
- roadmap : cf. WIKI Roadmap/<Prota>/<page>.md

## Bifurcations prises
| Etape roadmap | Choix canonique | Choix de cette partie | Consequence |
|---|---|---|---|
| <#> | <branche par defaut> | <ce que le joueur a fait> | <impact> |

---
FIN_PARTIES_DECISIONS_<ARC>
```

### Regles
- Les fiches Suivi/ sont mises a jour entre les sessions via BIBLE BUILD ou manuellement par le joueur.
- Les Archives/ sont en ecriture seule : une fois archivee, une CHRONO n'est plus modifiee (sauf correction d'erreur).
- Budget par page : meme contrainte que le WIKI (500-2000 tokens).

### Fetch
- Regles, declencheurs et budgets : cf. Instructions RP S4 (ouverture de thread, declencheur objectif, TTL). Non dupliques ici.
- Seules nuances propres a Parties/ : Archives/ en fetch exceptionnel (flashback, verification) ; Decisions/ a la demande pour verifier un choix anterieur.

---

## 9. Regles de build (BIBLE BUILD)

### Declenchement
Le joueur demande un BIBLE BUILD explicitement (`#BIBLE_BUILD`) ou implicitement (toute demande de creation, mise a jour ou modification de la BIBLE et/ou du WIKI). Pour une modification ponctuelle (corriger un fait, ajouter une ligne), le MJ fournit les blocs a remplacer sans rebuild complet.

Le joueur fournit :
1. L'univers cible.
2. Le focus narratif (ere, arc, faction, region).
3. Les sources : fichiers joints et/ou URL a fetcher.
4. La liste des dossiers/pages souhaitees (ou "a determiner ensemble").

### Fetch de la SPEC
Au premier BIBLE BUILD (aucune BIBLE existante), le MJ fetche `https://github.com/sodomicka/rp/blob/main/Config/SPEC_BIBLE_LORE_WIKI_v8_2.md`. Si la SPEC n'est pas encore sur le depot (tout premier build, rien n'existe), le joueur la fournit en fichier joint ou dans le chat pour ce premier thread. Apres ce premier build, la SPEC est uploadee dans Config/ et tout passe en fetch.

Pour les builds suivants, la BIBLE elle-meme sert de reference (gabarit integre dans les sections vides). Le fetch de la SPEC n'est necessaire que si le MJ a besoin de verifier une regle de construction.

### Processus - Phase 1 : Genese de la bibliotheque
Si construction collaborative :
1. Inventorier les sources disponibles.
2. Proposer une architecture de WIKI adaptee au RP.
3. Le joueur valide, ajuste ou complete.
4. Pour chaque fait ambigu, le MJ pose la question - le joueur tranche.
5. Construire les pages une par une ou par lot thematique, validation par dossier.
6. La BIBLE_LORE est construite en dernier - elle condense le WIKI et genere SB9.

### Processus - Phase 2 : Construction directe
Si sources completes et plan clair :
1. Lire toutes les sources.
2. Construire les pages WIKI selon le plan.
3. Construire la BIBLE_LORE avec SB9 indexe.
4. Livrer tous les fichiers.

### Sortie du build
- BIBLE_LORE : un fichier .md, fichier de projet. Les sections pas encore remplies conservent le gabarit (structure, champs, format) pour les builds futurs.
- Pages WIKI : fichiers .md individuels par dossier, a uploader sur le depot GitHub par le joueur.
- Pages Parties/ : fichiers .md si necessaire, a uploader dans Parties/{Univers}/Partie<n>/.
- Structure de sortie :
```
BIBLE_LORE_{UNIVERS}.md
{Univers}/
  <Dossier>/
    <Page>.md
  Roadmap/<Prota>/
    <Page>.md
  Fiches_Arc/<Prota>/
    <Page>.md
Parties/{Univers}/
  Partie<n>/
    Suivi/
      <Page>.md
    Archives/
      <Page>.md
    Decisions/
      <Page>.md
```

### Sources autorisees
- Transcripts in-game, guides/wikis officiels.
- Bases de donnees communautaires de haute qualite (en extrayant les FAITS, pas les interpretations).
- Notes du joueur.
- Exports de threads precedents.

### Sources interdites
- Theories de fans - sauf validation OOC explicite comme canon local.
- Contenu genere par IA non verifie.
- Novelisations ou adaptations non canoniques.

### Fetch pendant le build
Si le joueur fournit des URL : fetcher et extraire.
Si le joueur fournit des fichiers : lire et extraire.
Le MJ ne fetche PAS de sources supplementaires de sa propre initiative. Trou critique -> `[INCERTAIN]` + suggestion de source en OOC.

---

## 10. Utilisation en narration

Les regles d'usage en narration (declencheur objectif de fetch, TTL, budgets par tour, sequence d'ouverture de thread, gestion des echecs de fetch et backstop anti-invention) vivent dans les Instructions RP (S4) et ne sont PAS dupliquees ici : une regle de narration ecrite dans une SPEC que la narration ne charge jamais est du texte mort qui desynchronise en silence.

Seuls invariants cote SPEC :
- Chaque page WIKI/Parties est une unite autonome, fetchee en entier.
- La BIBLE_LORE est un fichier de projet : integralement en contexte, elle sert d'index permanent.

### Ce que la BIBLE, le WIKI et Parties/ ne font PAS
- Pas de voix PNJ (ANNEXE_PNJ du CODEX).
- Pas d'etat actuel du RP (CODEX S4).
- Pas de mise a jour pendant le RP. Statiques entre deux builds.

---

## 11. Mise a jour

La BIBLE_LORE, le WIKI et Parties/ sont statiques pendant le RP - pas de mise a jour a chaque CODEX BUILD.
Le joueur peut demander un BIBLE BUILD entre deux sessions pour :
- ajouter des sources ou des pages ;
- formaliser des divergences fraiches (CODEX ANNEXE_LORE -> BIBLE SB1/SB3 ou WIKI) ;
- archiver la CHRONO dans Parties/ ;
- mettre a jour les fiches Suivi/ ;
- enregistrer les decisions dans Decisions/ ;
- corriger des erreurs ;
- reorganiser la structure.

Lors d'un rebuild, le numero de version de la BIBLE incremente (B1 -> B2 -> ...). L'historique des changements vit dans git (log + diff), pas dans un journal interne au fichier.
Les pages WIKI/Parties modifiees sont re-livrees ; les autres restent intactes.
Le joueur uploade les fichiers mis a jour sur le depot GitHub.

---

## 12. Depot GitHub - Convention

### Structure du depot
```
sodomicka/rp/
  Config/
    SPEC_CODEX_v8_2.md
    SPEC_BIBLE_LORE_WIKI_v8_2.md
  <Univers>/
    <Dossier_thematique>/
      <Page>.md
    Roadmap/<Prota>/
      <Page>.md
    Fiches_Arc/<Prota>/
      <Page>.md
  Parties/<Univers>/
    Partie<n>/
      Suivi/
        <Page>.md
      Archives/
        <Page>.md
      Decisions/
        <Page>.md
```

### Convention de nommage
- Dossiers : PascalCase ou Snake_Case, descriptifs.
- Pages : Snake_Case, descriptives.
- Pas d'accents dans les noms de fichiers et dossiers.
- Pas d'espaces (underscores).

### URL de consultation
Toute page WIKI est accessible a : `wiki_base` + `<Dossier>/<Page>.md`.
Toute page Parties/ est accessible a : `parties_base` + `<Dossier>/<Page>.md`.
Toute SPEC est accessible a : `https://github.com/sodomicka/rp/blob/main/Config/<fichier>.md`.

### Visibilite
Le depot doit etre PUBLIC pour que fetch fonctionne sans token.

---

# GABARIT DE SORTIE - BIBLE_LORE

# BIBLE_LORE_{UNIVERS}

## Table des matieres
- SB0 Metadonnees
- SB1 Cosmogonie et regles du monde
- SB2 Lexique
- SB3 Chronologie
- SB4 Factions et groupes
- SB5 Personnages
- SB6 Lieux
- SB7 Artefacts et objets
- SB8 Mysteres ouverts et Tchekhov
- SB9 Index - routage

## SB0 Metadonnees
- univers :
- sources primaires :
- bible_version : B<N>
- wiki_base : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
- parties_base : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
- pages wiki rattachees :
  - <Dossier> - <description courte> (<N> pages)

## SB1 Cosmogonie et regles du monde
- <regle 1>
- <regle 2>

## SB2 Lexique
`Terme - definition (1 ligne max)`

## SB3 Chronologie
| Date/Ere | Evenement | Consequence |
|---|---|---|
| <date> | <evenement> | <consequence> |

Detail des etapes par arc : cf. {Univers}/Roadmap/<Prota>/ (fetch obligatoire en debut de thread pour l'arc en cours).

### Notes
- <note de cadrage>

## SB4 Factions et groupes
`Faction - nature | objectif | allies | ennemis | statut dans le focus`

## SB5 Personnages
`Nom - role | capacites-cle | relations | sort connu | certitude`
Si fiche WIKI detaillee : `detail: cf. WIKI <page>.md`. La BIBLE indexe le monde (= WIKI) ; Parties/ (archive d'une partie) s'atteint via le Sommaire, jamais par renvoi BIBLE.

## SB6 Lieux
`Lieu - nature | rattachement | fonction narrative | etat connu`

## SB7 Artefacts et objets
`Objet - nature | origine | pouvoir/fonction | localisation connue | certitude`

## SB8 Mysteres ouverts et Tchekhov

### Mysteres
`Mystere - hypotheses principales | statut (ouvert / resolu-dans-RP / hors-perimetre)`

### Tchekhov
`Fil - plante en | condition de detonation | consequence attendue`

## SB9 Index - routage

Index detaille page-par-page : cf. WIKI {Univers}/Sommaire.md
(Inventaire des dossiers : cf. SB0 pages wiki rattachees.)

---

FIN_BIBLE_B<N>

---

# GABARIT DE SORTIE - PAGE WIKI / PARTIES

# <Titre de la page>

- version : W<N>

## <Section 1>
<contenu structure>

## <Section 2>
<contenu structure>

---

FIN_WIKI_{DOSSIER}_{PAGE}
