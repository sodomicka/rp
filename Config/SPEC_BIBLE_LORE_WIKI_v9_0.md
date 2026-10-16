# SPEC_BIBLE_LORE_WIKI v9.0

Ce fichier definit la forme, les regles de construction et le gabarit du systeme BIBLE_LORE + WIKI + Parties :
- `BIBLE_LORE_{UNIVERS}.md` - index de routage + lore condense. Vit sur le depot, a la racine de `{Univers}/`. Lue EN ENTIER a l'ouverture de chaque thread de build (worldbuilding), avec le Sommaire et le journal d'implications. Pas lue en jeu : en narration, la roadmap en cours et les fiches de l'etape prennent le relais (cf. S10).
- WIKI GitHub (`{Univers}/`) - pages .md du monde, consultees par fetch a la demande. Cout zero en contexte tant que non fetchees.
- Parties GitHub (`Parties/{Univers}/Partie<n>/`) - memoire froide du RP, arcs joues, tracking PNJ, CHRONO archivee, indexee par le Sommaire de jeu. Consultees par fetch a la demande. Chaque `<n>` correspond a un RP distinct dans le meme univers.

Le modele doit produire des documents factuels, structures, sans narration, sans interpretation non balisee.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_BIBLE_LORE_WIKI_v9_0.md`.

---

## 1. Role et position hierarchique

La BIBLE_LORE est le point d'entree du systeme de reference lore. Elle contient :
1. Le lore condense de l'univers (SB0-SB8), lisible seul, autosuffisant pour les faits essentiels.
2. Les definitions des fils Tchekhov du RP (SB8), migrees depuis le CODEX.
3. L'index de routage (SB9) vers le Sommaire du WIKI pour le detail.

Le WIKI (`{Univers}/`) contient le monde : fiches personnages, chronologie detaillee, roadmaps, power-scaling, lore approfondi.

Les Parties (`Parties/{Univers}/Partie<n>/`) contiennent la memoire froide d'un RP donne : arcs joues, CHRONO archivee, fiches de suivi des PNJ affectes par la narration, fiche protagoniste, decisions et bifurcations prises. Chaque Partie<n> est un RP autonome dans le meme univers.

Hierarchie - ECHELLE DE REFERENCE DU SYSTEME, declinee par mode :
`OOC joueur > CODEX > { BIBLE_LORE, WIKI } > Canon externe > #SITES_REF > improvisation`
- En NARRATION : echelle complete (Instructions RP S1). `#SITES_REF` est la liste de sources du CODEX S7 : elle sert a VERIFIER le canon externe, jamais a l'ecraser.
- En WORLDBUILDING : `decision du worldbuilder` remplace `OOC joueur`, et le barreau CODEX est absent - il n'existe pas encore (Instructions Wiki S2).
Les trois enonces decrivent la MEME echelle. Toute divergence entre eux est un bug, pas une nuance de mode.

BIBLE et WIKI au meme echelon, arbitres par SCOPE : sur le detail specialise d'un sujet qui a une fiche, la FICHE prime (la BIBLE resume, la fiche detaille) ; sur le structurel/transversal (cosmogonie, regles du monde, index de routage), la BIBLE prime. Contradiction FRANCHE (au-dela d'un simple ecart de granularite) = l'une est perimee -> signaler au joueur, ne pas trancher seul. Les deux priment sur le canon externe. Le CODEX ne duplique ni la BIBLE ni le WIKI - il stocke l'etat courant, les capacites / description physique / resume de backstory du protagoniste, et les divergences fraiches. L'INSTANCE jouee du protagoniste (etat, run courant) vit en CODEX + Parties, pas dans la BIBLE/WIKI. Mais son ENTITE, si elle existe independamment de la partie (personnage canon, ou OC promu au lore), est decrite neutrement comme toute entite - cf. regle de placement (S7). Anti-boucle : un renvoi `cf.` mene toujours a un emplacement qui CONTIENT le fait, jamais a un autre renvoi.

## 2. Quand utiliser le systeme

Le systeme BIBLE_LORE + WIKI est utilise des que l'univers necessite un socle de lore fiable que le MJ ne peut pas reconstituer de memoire. Le joueur decide en setup si une BIBLE est necessaire.
- Si oui : BIBLE + WIKI portent le lore canon et les divergences etablies. Le CODEX ne stocke que la memoire chaude de session.
- Si non (codex pur) : le MJ se fie a ses connaissances + fetch. Le CODEX porte les divergences et les faits canon critiques.

## 3. Architecture a quatre couches

```
CODEX (vivant, memoire chaude de session)
  |-> BIBLE_LORE (index + lore condense, sur le depot, lue en entier a l'ouverture de chaque thread de build ; pas lue en jeu)
  |     |-> WIKI GitHub {Univers}/ (pages .md du monde, fetch a la demande ; index : Sommaire.md)
  |     |     |-> {Univers}/Roadmap/<Prota>/ (itineraires par arc, par perspective de prota ; la roadmap en cours est un document de jeu)
  |-> Parties/{Univers}/Partie<n>/ (memoire froide d'un RP donne, fetch a la demande ; index : Sommaire_Jeu.md)
        |-> Suivi/ (fiches PNJ affectes, protagoniste, memoire refroidie)
        |-> Archives/ (CHRONO archivee, arcs clos)
        |-> Decisions/ (bifurcations prises dans ce RP)
```

Le CODEX ANNEXE_CHRONO pointe vers la roadmap COURANTE et son etape via `roadmap: cf. WIKI Roadmap/<Prota>/<page>.md | etape: <n>`, et tient le FIL LONG des arcs traverses (suite ordonnee des arcs deja joues -> arc courant) : c'est lui qui porte la memoire du chemin parcouru en jeu. Les decisions specifiques a un RP sont tracees dans `Parties/{Univers}/Partie<n>/Decisions/`, et le passe joue archive dans `Parties/{Univers}/Partie<n>/Archives/`.

### Roadmap et CODEX : deux roles distincts
- ROADMAP (`Roadmap/<Prota>/`) : l'ITINERAIRE de l'arc - jalons dans l'ordre, casting, lieux, echelle temporelle, conditions de sortie (requis + interdits), verrous, roadmap suivante. Grain : le JALON (ce qui arrive, qui est la, ou, quand ; matiere dictee telegraphique). Le detail de scene n'y a pas sa place : il se met en scene EN JEU, a partir du jalon et des fiches. La roadmap EN COURS est un document de jeu : fetchee a l'ouverture du thread, elle fait foi sur la trame de l'etape. Elle porte aussi du futur : c'est un CADRAGE MJ, jamais un texte a annoncer en prose (Instructions RP S5).
- CODEX (ANNEXE_CHRONO) : l'ETAT D'ARC vivant ET LE FIL LONG - roadmap et etape courantes, jalon courant, statut, PLUS la suite ordonnee des arcs deja traverses. C'est le CODEX qui tient ou on en est ET d'ou l'on vient ; la roadmap dit ou l'on va. Le detail archive du passe joue vit dans Parties/, indexe au Sommaire de jeu.

> ANTI-AMNESIE. En jeu on ne consulte pas la BIBLE. La memoire de l'histoire repose sur deux sources, par horizon : (a) MEMOIRE LONGUE / coherence du chemin -> CODEX ANNEXE_CHRONO (fil ordonne des arcs traverses) + pages Parties/ indexees au Sommaire de jeu (fetch a la demande) ; (b) ETAPE COURANTE -> la roadmap en cours + les fiches de l'etape. La roadmap decrit le FUTUR PREVU, pas le PASSE VECU : ce n'est pas un substitut de memoire.

### Flux de resolution d'un fait lore
1. CODEX (divergence fraiche du RP ?) -> si oui, utiliser.
2. Roadmap en cours et fiches deja en contexte -> si oui, utiliser.
3. Sommaire.md (WIKI) ou Sommaire_Jeu.md (Parties/), deja en contexte : identifier la page, puis fetch de la page.
4. Fetch / #SITES_REF (canon externe) -> si hors perimetre BIBLE + WIKI.
5. Invention prudente -> coherente avec les echelons superieurs.

---

## 4. BIBLE_LORE - Principes redactionnels

### But : le monde en notices

La BIBLE dit qu'un fait EXISTE, ce qu'il est en une phrase, et a quoi il s'articule. Jamais comment il se deroule en detail : ca, c'est la fiche. Test d'admission d'une ligne de BIBLE : "sans elle, le MJ risque-t-il d'ecrire une contradiction sans savoir qu'il faut fetcher ?" Non -> la ligne vit en fiche, pas en BIBLE.

Repartition des roles, a ne plus perdre de vue :
- BIBLE = radar de FAITS. Elle couvre le monde par fait, pour que le MJ detecte quand fetcher. Les collisions de lore arrivent par fait, pas par page.
- Sommaire = index de PAGES. Il couvre le WIKI par page, pour dire ou c'est ecrit. Fetche en debut de chaque thread de jeu : y deporter des resumes d'entites taxerait le document le plus lu du systeme.
- Fiches = DETAIL. Deroules, texture, exhaustif.

Regles derivees :
- Entree d'entite (SB4 a SB7) plafonnee a 3-4 lignes des qu'une fiche WIKI existe : notice + renvoi. Sans fiche, l'entree peut etre plus riche - la BIBLE est alors le domicile du fait.
- Etat de chantier INTERDIT en BIBLE (captures de session, questions de build en cours) : domicile _Implications / _Chantier_*.
- Decroissance obligatoire : a chaque BIBLE BUILD, tout fil resolu ou Tchekhov detone se compresse en une ligne de statut + renvoi (le deroule vit en roadmap/chrono). Une BIBLE qui ne fait que croitre est une BIBLE qui derive.


- Dense > exhaustif. Ligne telegraphique > phrase pleine.
- FOCUS : la bible ne couvre que le PERIMETRE NARRATIF defini par le joueur.
- Pas de narration, pas de prose, pas de metaphores.
- Pas d'adjectifs decoratifs ni de jugements de valeur.
- Phrases > 25 mots interdites.
- Ingestion : pour interroger le canon, requeter la forme d'origine du nom (accentuee si elle l'est : meilleur rappel).
- Aucune theorie de fans. Aucune speculation non balisee.

### Niveaux de certitude
Chaque fait porte implicitement le niveau "etabli" sauf balisage contraire :
- `[IMPLICITE]` - fortement implique par le canon mais jamais enonce explicitement.
- `[INTERPRETATION]` - lecture coherente mais debattue ou ambigue. Le joueur tranche en OOC si le RP touche ce point.
- `[INCERTAIN]` - information contradictoire ou insuffisante dans les sources.
- `[DIVERGENCE RP]` - divergence du RP par rapport au canon, formalisee et validee par le joueur.

## 5. BIBLE_LORE - Budget

Plafond dur : 55 000 caracteres.
Cible indicative : 35 000 a 40 000 caracteres. Le plafond dur reste la limite de securite ; la cible est le regime de croisiere d'une BIBLE en notices. Un build qui livre au-dela de la cible justifie l'ecart (univers a tres large cast, etc.).
Pas de contrainte de cohabitation CODEX + BIBLE : la BIBLE n'est pas lue en jeu, donc BIBLE et CODEX ne sont jamais en contexte ensemble. La BIBLE garde son plafond propre de 55 000 caracteres : lue en entier a chaque ouverture de thread de build, elle se paie en contexte a chaque thread.
Le seuil de bascule retrieval (RAG) des fichiers de projet (SPEC_CODEX S3) ne concerne plus la phase build : BIBLE, SPEC et pages se fetchent, aucune ne se charge comme fichier de projet.
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

Fichier unique, lu en integralite par le MJ a chaque tour DE BUILD (phase worldbuilding). JAMAIS charge en narration (cf. S5 et S10).
Chaque section a un identifiant stable (`SB0`, `SB1`...).

### BIBLE auto-portante
Les sections pas encore remplies conservent le gabarit de la SPEC (lignes de structure, champs, format). Ainsi le MJ sait quoi remplir au prochain build sans refetcher la SPEC. La BIBLE livree n'a jamais de section vide sans structure.

### Sections (ordre fixe, toutes optionnelles sauf SB0, SB1, SB9)

#### SB0 Metadonnees [OBLIGATOIRE]
- univers :
- sources primaires : <liste>
- bible_version : B<N>
- wiki_base : <URL racine du WIKI GitHub, forme blob - lecture humaine>
  Format : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
- raw_base : <URL racine du WIKI, forme raw - FETCH PAR DEFAUT>
  Format : `https://raw.githubusercontent.com/sodomicka/rp/main/<Univers>/`
- parties_base : <URL racine de Parties/ GitHub pour le RP en cours, forme blob>
  Format : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
- parties_raw_base : <idem, forme raw - FETCH PAR DEFAUT>
  Format : `https://raw.githubusercontent.com/sodomicka/rp/main/Parties/<Univers>/Partie<n>/`

  Les deux formes sont STOCKEES, pas derivees a la volee : le fetch par defaut se fait sur raw (markdown brut, aucun parsing), et une derivation refaite a chaque appel est une occasion d'erreur pour zero gain. Toutes les URLs se construisent par concatenation : base + chemin relatif. La forme blob reste utile pour un lien lisible et pour la methode de secours (cf. S12).
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

Detail des etapes par arc : cf. {Univers}/Roadmap/<Prota>/.
En jeu : la roadmap en cours et son etape (designees par le CODEX ANNEXE_CHRONO) cadrent l'arc ; le fil long des arcs traverses vient du CODEX ANNEXE_CHRONO.

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

Regle : SB8 porte, par mystere ou fil, la DEFINITION et le STATUT (ouvert / arme / detone / resolu) + renvoi. Les deroules de detonation, consequences jouees et captures d'etat vivent en roadmap, chrono ou _Chantier_* - jamais ici. Un fil detone ou resolu se compresse en une ligne au build suivant (decroissance, cf. S4).
Deux sous-sections :

##### Mysteres
Questions non resolues, pertinentes au focus. Le MJ doit savoir ce qui est volontairement flou.
`Mystere - hypotheses principales | statut (ouvert / resolu-dans-RP / hors-perimetre)`

##### Tchekhov
Definitions des fils narratifs plantes dans le RP. L'ETAT de chaque fil (ouvert/arme/paye) est dans le CODEX ANNEXE_TCHEKHOV. La BIBLE porte les definitions stables.
`Fil - plante en | condition de detonation | consequence attendue`

#### SB9 Index - routage [OBLIGATOIRE si WIKI present]
SB9 ne contient PAS l'index detaille page-par-page. Cet index vit dans `{Univers}/Sommaire.md` (page WIKI fetchee au debut de chaque thread, cf. Instructions RP S4) ; celui de Parties/ vit dans `Sommaire_Jeu.md` de chaque partie, pour que SB9 reste de taille fixe et ne croisse plus avec le nombre de pages.

Contenu de SB9 :
- `Index detaille page-par-page : cf. WIKI {Univers}/Sommaire.md`

Regles de SB9 :
- L'inventaire des dossiers (avec compte de pages) est deja dans SB0 `pages wiki rattachees` - il sert de filet de securite si Sommaire.md tombe (listing direct via la methode dossier de ACCES GITHUB).
- SB1-SB8 portent le resume ambiant : le MJ sait CE QUI EXISTE sans fetch. Sommaire.md dit OU est le detail. La page cible porte le detail.
- Sommaire.md est fetche au debut de chaque thread RP (carte de navigation centrale) et reste en contexte. Fetche tot pour rester saillant (eviter le lost-in-the-middle). Regles d'usage : Instructions RP S4.
- Chaque page reste une unite autonome, fetchee en entier. L'URL se construit : `raw_base` ou `parties_raw_base` (SB0) + `<Dossier>/<Page>.md`.

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
- Sommaire (index detaille de toutes les pages WIKI - voir gabarit ci-dessous).
- Fiches personnages approfondies (neutres `<Type>/` ou perspective `<Type>/<Prota>/`).
- Descriptions de lieux.
- Roadmaps (itineraires par arc, par PERSPECTIVE de prota : `Roadmap/<Prota>/`).
- Power-scaling.
- Systemes de magie/combat detailles.
- Tout decoupage thematique pertinent au RP.

### Principes redactionnels
- Meme registre que la BIBLE : factuel, sans narration.
- Niveaux de certitude identiques : etabli / [IMPLICITE] / [INTERPRETATION] / [INCERTAIN] / [DIVERGENCE RP].

### Budget par page
- Fourchette : 2 000 a 12 000 caracteres (verification : wc -m).
- En dessous de 2 000 : fusionner avec une page voisine.
- Au-dela de 12 000 : scinder (pages satellites pour une fiche d'entite, cf. ci-dessous ; sous-pages sinon).
- Exception : pages transcript jusqu'a 16 000 caracteres.

### Pages satellites d'entite

Quand une fiche d'entite sature son budget, elle se scinde en pages satellites nommees par volet :
- `<Entite>_chrono_<N>.md` : trajectoire datee par ere (precedent : Nisha_chrono_A/B).
- `<Entite>_inventaire.md` : objets, arsenal, possessions recurrentes.
- `<Entite>_relations_<N>.md` : reseau relationnel (regles propres : Satellite relations, ci-dessous).
La fiche mere garde le NOYAU (identite, mecanique, psychologie) et renvoie vers ses satellites. Un satellite respecte le budget de page standard (12 000) ; sous le plancher de 2 000, il refusionne dans la fiche mere.
Un satellite suit sa fiche mere : une fiche de groupe (precedent : Claudia_et_Lucio) a des satellites de groupe ; deux fiches distinctes ne partagent jamais un satellite.

### Satellite relations

OPTIONNEL. Tous les personnages n'y ont pas droit. Le worldbuilder le decide, le MJ peut le proposer, dans deux cas :
- la fiche mere sature son budget ;
- les relations portent assez de texture pour meriter leur page (adresses qui changent selon l'interlocuteur, regimes avant/apres une bascule, rituels), meme sans saturation.
Sans satellite, les relations restent dans la fiche mere, avec les memes rubriques, adresses comprises.

DECOUPE. Une page par cercle quand le volume l'exige (precedent : Nisha_relations_proches, _famille, _boulot, _eleves_tokyo).

GROUPABLE. Une entree peut viser un GROUPE (faction, cercle, fratrie) au lieu d'un individu, quand ses membres partagent la meme relation a l'entite. Les membres qui font exception sont nommes dans l'entree de groupe, avec leur usage propre. Un membre dont la relation va au-dela de l'exception garde sa propre entree ; l'entree de groupe le nomme sans redire son detail.

ADRESSES. Rubrique obligatoire de chaque entree, individuelle ou de groupe : qui appelle qui comment, dans les deux sens ; tutoiement ou vouvoiement ; surnoms et leurs conditions (en prive, devant temoins, depuis telle date) ; exceptions nominatives. La liste est EXHAUSTIVE : une adresse qui n'y figure pas ne s'emploie pas, prenom compris. Un satellite peut poser la convention inverse en tete (" les appellatifs listes s'ajoutent aux prenoms, toujours disponibles " : precedent Nisha).

REGLES GENERALES. Une habitude d'adresse ou de comportement qui vaut pour tous les interlocuteurs (precedent : Nisha appelle toute femme " ma belle ") s'ecrit une fois, en tete du satellite (ou de la premiere page d'une serie), jamais entree par entree.

Frontiere fiche/relations : la fiche mere garde la MECANIQUE d'une relation (domination, symbiose, pool partage - tout ce qui touche au systeme de pouvoir) ; la page relations porte la TEXTURE (surnoms et adresses reciproques, rituels et habitudes, dynamique, ce que l'autre sait de l'entite, evolution datee telegraphique). Cross-renvois obligatoires dans les deux sens.

Gabarit page relations :
```
# <Entite> - Relations (<cercle>)

- version : W<N>

<Une ligne : satellite de quelle fiche, pages soeurs, ou vit la mecanique.>

## Regles generales (si besoin)
- <habitude d'adresse ou de comportement valable pour tous les interlocuteurs>

## <Autre entite>
- Statut : <une ligne>
- Surnoms / adresses : <dans les deux sens ; tu/vous ; surnoms et conditions ; ce qui ne s'emploie pas>
- Rituels / habitudes : <...>
- Dynamique : <...>
- Ce que <l'autre> sait : <acces au secret, angles morts>
- Evolution datee : <telegraphique, par date>

## <Groupe> (entree de groupe)
- Statut : <la relation commune aux membres>
- Surnoms / adresses : <usage du groupe> ; exceptions : <membres nommes, leur usage>
- Dynamique : <...>
```
Exemple de FORMAT (illustratif, NE PAS inscrire tel quel) :
```
## Les Rodeurs (entree de groupe)
- Surnoms / adresses : pour eux, Magnus et Markiona sont le Loup Noir et la Louve Blanche, jamais leurs vrais noms ; exceptions : Alidoro, Romeo et Lea emploient les vrais noms.
```

### Derogation fiche protagoniste

La fiche d'un PROTAGONISTE echappe au plafond de page standard : plafond propre de 30 000 caracteres (verification : wc -m). Meme derogation pour un personnage PIVOT designe par le worldbuilder, note en BIBLE SB0. Raison : c'est le document le plus central du WIKI ; la decouper pour respecter un budget pense pour des fiches PNJ multiplierait les fetchs obligatoires. Au-dela de 30k : scinder par pages satellites (ci-dessus), jamais gonfler.

### Structure interne d'une page
Pas de gabarit impose sauf pour les Roadmaps (cf. gabarit ci-dessous). Obligations :
1. Titre clair en H1, correspondant au nom de la page.
2. Metadonnee unique : version (W<N>). Aucune autre metadonnee (pas d'univers, dossier, sources, bible rattachee : l'indexation va de la BIBLE vers la page via le Sommaire, jamais l'inverse).
3. Contenu structure en sections si pertinent.
4. Pas de contenu narratif (sauf pages transcript = verbatim).

### Trajectoire datee (gabarit fiche d'entite)
Troisieme strate de toute fiche perso/lieu/objet. Decrit le DEVENIR DATE de l'entite APRES le point de depart. N'existe que dans la fiche pleine ({Univers}/). En jeu, l'etat d'une entite a l'ouverture d'une etape se lit dans cette strate, a la date de l'etape ; ce qui est date apres n'est su de personne et ne se joue pas.
Regles :
- Forme telegraphique, une ligne par evenement. Pas de prose ; le detail narratif vit dans la roadmap.
- ALIMENTATION A CHAUD : une entree est ajoutee UNIQUEMENT apres avoir roadmappe l'arc qui la produit. Jamais d'anticipation.
- CANON PAR DEFAUT, neutre, reutilisable entre parties (comme les roadmaps).
- OVERRIDE PAR PARTIES/ : quand une partie diverge, le delta va en Parties/{Univers}/Partie<n>/ et SURCLASSE cette strate pour la partie concernee (routage S7 inchange).
- CONSOLIDATION : les pointeurs dates jadis en Notes de frontiere (mort canon, eveil, depart...) migrent ici sous forme datee ; Notes de frontiere ne garde que les renvois non dates et les hors-perimetre.
- PLAFOND : par defaut 30 entrees max par fiche. Derivation : une ligne telegraphique fait ~120 car., 30 lignes ~3 600 car., soit moins du tiers du plafond de page (12 000). Le worldbuilder ajuste par univers ; il ne laisse PAS le champ vide - un placeholder non rempli dans une SPEC est une regle morte, et les Instructions Wiki interdisent explicitement de laisser un [A definir] pour esquiver une question. Au-dela du plafond : compresser ou deporter en roadmap ; depassement signale, jamais compresse seul.
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

Les roadmaps vivent dans `{Univers}/Roadmap/<Prota>/`, une par arc, par perspective de prota. Les decisions prises dans un RP donne sont tracees dans `Parties/{Univers}/Partie<n>/Decisions/`.

DOCUMENT DE JEU. La roadmap en cours est fetchee a l'ouverture de chaque thread de jeu (Instructions RP S4) et reste en contexte tout le thread, avec les fiches de son casting. Elle doit donc porter tout ce que le MJ doit savoir pour mener l'arc sans vue d'ensemble de la saga : ou on va, qui est la, ce qui est requis, ce qui est interdit.

GRAIN. Le jalon : ce qui arrive, qui est la, ou, quand. Le detail de scene (mise en scene, repliques, gestes) ne s'ecrit pas : il se joue en jeu, a partir du jalon et des fiches. Test : un detail qui ne deplace pas le jalon n'a pas sa place en roadmap.

```
# Roadmap <N> - <Titre>

- version : W<N>
- statut : <a venir | en cours | clos> ; <JOUABLE | NON JOUABLE (narree)>
- prota / POV : <...>
- echelle temporelle : <duree reelle in-world, ex. ~190 ans, ~3 jours, une journee>
- borne d'entree : <situation de depart>
- borne de sortie : <situation qui clot l'arc> -> <roadmap suivante>
- roadmap precedente : cf. WIKI Roadmap/<Prota>/<page>.md (ou "aucune - premier arc")
- roadmap suivante : cf. WIKI Roadmap/<Prota>/<page>.md (ou "aucune - fin" ; embranchement : une ligne par sortie, annotee de sa condition)

## Intention
<1 a 3 lignes : ce que l'arc doit faire ressentir ou etablir>

## Itineraire (jalons)
1. <jalon : ce qui arrive, qui, ou, quand>
2. <jalon>
...
Bloc couvrant un long laps a rendre en vignettes : marquer `[SNAPSHOTS - <duree chiffree>]`.

## Casting convoque
- <Nom> - <role dans l'arc> - cf. <Type>/<page>   (ou "non fiche" + description d'une ligne)

## Lieux et objets
- <Lieu ou objet> - <fonction dans l'arc> - cf. <Type>/<page>   (ou "non fiche" + description d'une ligne)

## Conditions de sortie
### Requis
- <action que le joueur doit avoir accomplie pour que l'arc se close>
### Interdits
- <action que le protagoniste ne peut pas accomplir> - <ce qu'elle casserait : arc ou fait ulterieur concerne>

## Verrous
- Jalon <n> : <choix du joueur dont la saga depend>. Paliers :
  1. <palier le plus doux>
  2. Refus maintenu : <palier suivant>
  ...
  n-1. Avertissement du MJ : la suite n'est pas scenarisee et mene a l'avortement du RP.
  n. Entetement maintenu : le MJ declare la fin du RP et ne narre plus dans ce thread ; rejouer = nouveau thread, CODEX d'entree reutilise sans modification.

## Bifurcations
- Embranchement, apres jalon <n> : si <condition A> -> <consequence, roadmap suivante A>. Si <condition B> -> <consequence, roadmap suivante B>.

## Notes de frontiere
- <ce qui appartient a l'arc suivant, nomme sans etre deroule>

---
FIN_WIKI_ROADMAP_<PROTA>_<N>
```

ECHELLE TEMPORELLE : obligatoire et chiffree. Elle dit au MJ a quelle vitesse le temps s'ecoule sur l'arc, pour qu'il cale l'ecoulement par defaut sur l'arc et non sur son envie de scenes (Instructions RP S3). Un bloc `[SNAPSHOTS]` porte sa propre duree : elle borne l'ellipse. Compresser n'est PAS supprimer : le joueur doit sentir le temps passer.

CONDITIONS DE SORTIE. Le MJ en jeu n'a pas la vue d'ensemble de la saga : la roadmap la lui donne sous forme de regles.
- REQUIS : ce que le joueur doit avoir fait pour que l'arc se close. Tant qu'un requis manque, la borne de sortie n'est pas atteinte.
- INTERDITS : ce que le protagoniste ne peut pas faire, parce que ca casserait cet arc OU un arc ulterieur (interdits INTER-ROADMAPS : tuer un personnage dont la saga a besoin plus tard, reveler un secret avant son heure...). Le bon sens n'a pas besoin d'etre ecrit ; ce qui depend de la vue d'ensemble, si. Chaque interdit nomme ce qu'il protege, pour que le MJ en mesure le poids.
- En jeu, un requis refuse ou un interdit tente se tient par les paliers d'un verrou : le MJ force la main du plus doux au plus dur, jamais en annoncant la raison en prose.

BIFURCATIONS, deux usages.
- EMBRANCHEMENT : le recit se separe en deux chemins (tuer ou epargner un personnage central...). Couteux : chaque branche exige ses propres suites et une roadmap suivante par sortie.
- JALON VERROUILLE : un choix du joueur dont la saga depend. Pas de seconde branche : le MJ force la main par paliers, du plus doux au plus dur, en jeu (un PNJ insiste, un autre vient en renfort, le groupe fait pression, une autorite tranche) ou en meta quand aucun PNJ ne peut le porter (rappel du MJ hors fiction). Si le refus tient, le MJ avertit que la suite n'est pas scenarisee, puis declare la fin du RP en dernier recours.
- A chaque roadmap, le MJ de build repere les choix du joueur dont la saga depend et propose un verrou pour chacun, et les interdits inter-roadmaps que les arcs suivants imposent.

### Gabarit Sommaire

`{Univers}/Sommaire.md` porte l'index detaille du WIKI que SB9 ne porte plus : une entree par page, groupee par dossier. Fetche au debut de chaque thread RP. Mis a jour via BIBLE BUILD a chaque ajout de page. Parties/ a son propre index : le Sommaire de jeu (S8).

```
# Sommaire - {Univers}

- version : W<N>

## WIKI

> Chaque entree porte la version `(W<N>)` de la page : inventaire de versions. Un ecart entre ce W<N> et celui ecrit dans la page elle-meme signale une copie perimee (canari, non bloquant).
>
> QUI LIT LE CANARI. Deux lecteurs, deux moments :
> - EN NARRATION, a chaque page fetchee : le MJ compare le `W<N>` de la page au `W<N>` de son entree au Sommaire. Ecart -> `[VERSION DECALEE - <page> : Sommaire W<x>, page W<y>]` en OOC bref, NON BLOQUANT. Arbitrage : la PAGE fait foi (c'est le fichier reel ; le Sommaire n'est qu'un index). Cf. Instructions RP S4.2ter.
> - AU BIBLE BUILD : toute page relivree incremente son `W<N>` et son entree au Sommaire est mise a jour DANS LE MEME BUILD. C'est ici que se solde un `[VERSION DECALEE]` remonte en jeu.

### <Dossier>/
Description : <contenu du dossier en 1 ligne>
- <Page>.md (W<N>) - <description courte du contenu>

### Roadmap/<Prota>/
Description : itineraires par arc, dans l'ordre de la saga. La roadmap en cours est fetchee a l'ouverture de chaque thread de jeu (designee par le CODEX).
- <Roadmap>.md (W<N>) - <arc, bornes, echelle temporelle>

> NON INDEXES. Le garde-cap (`Roadmap/<Prota>/00_Garde_Cap.md`) : source de build, jamais fetche en narration. `Parties/<Partie>/Memoires/` : archives narratives interdites en jeu (sauf ordre OOC explicite), consultees au BUILD seulement par listing direct du dossier. Indexer un dossier le fait paraitre fetchable en narration.

---
FIN_WIKI_SOMMAIRE
```

### Maintenance
Pages WIKI mises a jour via BIBLE BUILD. Statiques entre deux builds.

---

## 8. Parties - Specification

### Nature
Les pages Parties/ sont des fichiers .md heberges sur le meme depot GitHub, dans `Parties/{Univers}/Partie<n>/`. Elles constituent la memoire froide d'un RP donne. Chaque `Partie<n>` est un RP autonome dans le meme univers, ce qui permet de jouer plusieurs RP en parallele avec des bifurcations differentes.

### Structure
```
Parties/{Univers}/
  Partie1/
    Sommaire_Jeu.md - index de la memoire de la partie (gabarit ci-dessous). Ecrit par le CODEX V1 puis tenu a jour par chaque CODEX BUILD. Fetche a l'ouverture de chaque thread de jeu.
    Suivi/
      <Protagoniste>_Fiche.md - backstory COMPLETE + identite du protagoniste (froid, fetch a la demande). PAS les capacites ni l'etat : ils vivent dans le CODEX S3 (capacites ancrees en S3a). Le CODEX S3a porte le resume chaud de cette backstory.
      <PNJ>_Suivi.md - tracking des PNJ affectes par la narration
    Archives/
      CHRONO_<arc>.md - chronologie archivee d'un arc clos
    Decisions/
      Decisions_<arc>.md - bifurcations prises dans ce RP par rapport a la roadmap
    Memoires/
      Memoire_{Univers}_<n>.md - archive NARRATIVE figee d'un thread (livrable 3 du CODEX BUILD).
        NON indexee au Sommaire (meme doctrine que Roadmap/ : un dossier indexe parait fetchable en jeu).
        INTERDITE en narration sauf ordre OOC explicite. Fetchable AU BUILD pour recalibrer
        ANNEXE_STYLE uniquement - elle rend du TON, jamais des faits. Hors budget de page.
        Acces par listing direct du dossier (cf. S12). Cf. SPEC_CODEX 4ter, livrable 3.
  Partie2/
    Suivi/
    Archives/
    Decisions/
```

### Gabarit Sommaire de jeu

Le MJ doit savoir OU piocher sans tout fouiller : chaque entree liste les SUJETS que la page couvre (personnages, lieux, objets, fils, periode). Un sujet qui n'y figure pas n'est pas dans la page.

```
# Sommaire de jeu - {Univers} Partie<n>

- version : W<N>

> Index de la memoire froide de la partie. Ecrit par le CODEX BUILD, fetche a l'ouverture de chaque thread de jeu, reste en contexte. Route un trou objectif vers la page qui le porte. `Memoires/` n'est pas indexe (interdit en jeu).

### Suivi/
- <Page>.md (W<N>) - <contenu en une ligne> | sujets : <personnages, lieux, objets, fils, periode>

### Archives/
- <Page>.md (W<N>) - <arc clos, periode> | sujets : <...>

### Decisions/
- Decisions_<Arc>.md (W<N>) - <bifurcations de l'arc> | sujets : <...>

---
FIN_PARTIES_SOMMAIRE_JEU
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
- Les fiches Suivi/ sont mises a jour entre les sessions via CODEX BUILD (memoire refroidie) ou BIBLE BUILD. Toute page Parties/ creee ou relivree est reportee au Sommaire de jeu dans le meme build.
- Les Archives/ sont en ecriture seule : une fois archivee, une CHRONO n'est plus modifiee (sauf correction d'erreur).
- Budget par page : meme contrainte que le WIKI (2 000 a 12 000 caracteres). EXCEPTION : `Memoires/` (archive narrative, non bornee, hors budget).

### Fetch
- Regles, declencheurs et budgets : cf. Instructions RP S4 (ouverture de thread, declencheur objectif, TTL). Non dupliques ici. Le routage passe par le Sommaire de jeu.
- Seules nuances propres a Parties/ : Archives/ en fetch exceptionnel (flashback, verification) ; Decisions/ a la demande pour verifier un choix anterieur ; `Memoires/` JAMAIS en narration (sauf ordre OOC explicite) - reserve au CODEX BUILD, usage unique : recalibrage d'ANNEXE_STYLE.

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
Au premier BIBLE BUILD (aucune BIBLE existante), le MJ LISTE d'abord `Config/` pour relever le numero de version courant (Instructions Wiki S8 : clone sans blobs par defaut, listing github.com/tree en secours), PUIS fetche la SPEC correspondante.
Ne JAMAIS recopier un numero de version fige depuis un document (SPEC, instructions, BIBLE) : c'est le mecanisme de la spec fantome - un build fait sur une revision perimee dont personne ne s'apercoit. Si la SPEC n'est pas encore sur le depot (tout premier build, rien n'existe), le joueur la fournit en fichier joint ou dans le chat pour ce premier thread. Apres ce premier build, le MJ ecrit la SPEC dans Config/ (Instructions Wiki S8bis) et tout passe en fetch.

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
- BIBLE_LORE : un fichier .md, a la racine de `{Univers}/` sur le depot. Les sections pas encore remplies conservent le gabarit (structure, champs, format) pour les builds futurs.
- Pages WIKI : fichiers .md individuels par dossier, ecrits sur le depot par le MJ (Instructions Wiki S8bis).
- Pages Parties/ : fichiers .md si necessaire, ecrits de la meme facon dans Parties/{Univers}/Partie<n>/.
- Structure de sortie :
```
BIBLE_LORE_{UNIVERS}.md
{Univers}/
  <Dossier>/
    <Page>.md
  Roadmap/<Prota>/
    <Page>.md
Parties/{Univers}/
  Partie<n>/
    Sommaire_Jeu.md
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

Les regles d'usage en narration (declencheur objectif de fetch, TTL, sequence d'ouverture de thread, gestion des echecs de fetch et backstop anti-invention) vivent dans les Instructions RP (S4) et ne sont PAS dupliquees ici : une regle de narration ecrite dans une SPEC que la narration ne charge jamais est du texte mort qui desynchronise en silence.

Seuls invariants cote SPEC :
- Chaque page WIKI/Parties est une unite autonome, fetchee en entier.
- La BIBLE_LORE est le document DE LA PHASE BUILD : lue en entier a l'ouverture de chaque thread de worldbuilding, elle sert d'index permanent. En jeu elle n'est PAS lue : la roadmap en cours et les fiches de l'etape portent le lore utile ; la BIBLE ne se recupere qu'en dernier recours, sur trou objectif qu'aucune page ne couvre (cf. Instructions RP S1, S2.1).

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
Le MJ ecrit les fichiers mis a jour sur le depot (Instructions Wiki S8bis).

---

## 12. Depot GitHub - Convention

### Structure du depot
```
sodomicka/rp/
  Config/
    SPEC_CODEX_v8_8.md
    SPEC_BIBLE_LORE_WIKI_v9_0.md
    (numeros indicatifs : verifier le listing reel de Config/ avant tout fetch)
  <Univers>/
    <Dossier_thematique>/
      <Page>.md
    Roadmap/<Prota>/
      <Page>.md
  Parties/<Univers>/
    Partie<n>/
      Sommaire_Jeu.md
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

### Version des SPEC
- Une SPEC modifiee change de numero (nom de fichier + titre) : sinon deux fichiers differents revendiquent le meme numero, c'est le mecanisme meme de la spec fantome.
- Chaque SPEC a sa propre numerotation : SPEC_BIBLE_LORE_WIKI et SPEC_CODEX evoluent separement.
- L'historique des changements vit dans git (log + diff), jamais dans le fichier : ni commentaire de revision, ni ligne Revision, ni etiquette de version sur une regle (SPEC et instructions).

### URL de consultation
FETCH (defaut) - forme raw, markdown brut, sans parsing :
- Page WIKI : `raw_base` + `<Dossier>/<Page>.md`
- Page Parties/ : `parties_raw_base` + `<Dossier>/<Page>.md`
- SPEC : `https://raw.githubusercontent.com/sodomicka/rp/main/Config/<fichier>.md`

LIEN LISIBLE / SECOURS - forme blob (parsing requis, cf. Instructions RP S4 methode 2) :
- Page WIKI : `wiki_base` + `<Dossier>/<Page>.md`
- Page Parties/ : `parties_base` + `<Dossier>/<Page>.md`
- SPEC : `https://github.com/sodomicka/rp/blob/main/Config/<fichier>.md`

Regle : on FETCHE en raw, on CITE en blob. Une URL blob passee a un fetcheur oblige a parser du HTML pour rien.

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
- raw_base : `https://raw.githubusercontent.com/sodomicka/rp/main/<Univers>/`
- parties_base : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
- parties_raw_base : `https://raw.githubusercontent.com/sodomicka/rp/main/Parties/<Univers>/Partie<n>/`
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

Detail des etapes par arc : cf. {Univers}/Roadmap/<Prota>/.
En jeu : la roadmap en cours et son etape (designees par le CODEX ANNEXE_CHRONO) cadrent l'arc ; le fil long des arcs traverses vient du CODEX ANNEXE_CHRONO.

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
