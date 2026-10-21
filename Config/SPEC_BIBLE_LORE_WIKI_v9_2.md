# SPEC_BIBLE_LORE_WIKI v9.2

Ce fichier définit la forme, les règles de construction et le gabarit du système BIBLE_LORE + WIKI + Parties :
- `BIBLE_LORE_{UNIVERS}.md` - index de routage + lore condensé. Vit sur le dépôt, à la racine de `{Univers}/`. Lue EN ENTIER à l'ouverture de chaque thread de build (worldbuilding), avec le Sommaire et le journal d'implications. Pas lue en jeu : en narration, la roadmap en cours et les fiches de l'étape prennent le relais (cf. §10).
- WIKI GitHub (`{Univers}/`) - pages .md du monde, consultées par fetch à la demande. Coût zéro en contexte tant que non fetchées.
- Parties GitHub (`Parties/{Univers}/Partie<n>/`) - mémoire froide du RP, arcs joués, tracking PNJ, CHRONO archivée, indexée par le Sommaire de jeu. Consultées par fetch à la demande. Chaque `<n>` correspond à un RP distinct dans le même univers.

Le modèle doit produire des documents factuels, structurés, sans narration, sans interprétation non balisée.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_BIBLE_LORE_WIKI_v9_2.md`.

---

## 1. Rôle et position hiérarchique

La BIBLE_LORE est le point d'entrée du système de référence lore. Elle contient :
1. Le lore condensé de l'univers (SB0-SB8), lisible seul, autosuffisant pour les faits essentiels.
2. Les définitions des fils Tchekhov du RP (SB8), migrées depuis le CODEX.
3. L'index de routage (SB9) vers le Sommaire du WIKI pour le détail.

Le WIKI (`{Univers}/`) contient le monde : fiches personnages, chronologie détaillée, roadmaps, power-scaling, lore approfondi.

Les Parties (`Parties/{Univers}/Partie<n>/`) contiennent la mémoire froide d'un RP donné : arcs joués, CHRONO archivée, fiches de suivi des PNJ affectés par la narration, fiche protagoniste, décisions et bifurcations prises. Chaque Partie<n> est un RP autonome dans le même univers.

Hiérarchie - ÉCHELLE DE RÉFÉRENCE DU SYSTÈME, déclinée par mode :
`OOC joueur > CODEX > { BIBLE_LORE, WIKI } > Canon externe > #SITES_REF > improvisation`
- En NARRATION : échelle complète (Instructions RP §1). `#SITES_REF` est la liste de sources du CODEX §7 : elle sert à VÉRIFIER le canon externe, jamais à l'écraser.
- En WORLDBUILDING : `décision du worldbuilder` remplace `OOC joueur`, et le barreau CODEX est absent - il n'existe pas encore (Instructions Wiki §2).
Les trois énoncés décrivent la MÊME échelle. Toute divergence entre eux est un bug, pas une nuance de mode.

BIBLE et WIKI au même échelon, arbitrés par SCOPE : sur le détail spécialisé d'un sujet qui a une fiche, la FICHE prime (la BIBLE résume, la fiche détaille) ; sur le structurel/transversal (cosmogonie, règles du monde, index de routage), la BIBLE prime. Contradiction FRANCHE (au-delà d'un simple écart de granularité) = l'une est périmée -> signaler au joueur, ne pas trancher seul. Les deux priment sur le canon externe. Le CODEX ne duplique ni la BIBLE ni le WIKI - il stocke l'état courant, les capacités / description physique / résumé de backstory du protagoniste, et les divergences fraîches. L'INSTANCE jouée du protagoniste (état, run courant) vit en CODEX + Parties, pas dans la BIBLE/WIKI. Mais son ENTITÉ, si elle existe indépendamment de la partie (personnage canon, ou OC promu au lore), est décrite neutrement comme toute entité - cf. règle de placement (§7). Anti-boucle : un renvoi `cf.` mène toujours à un emplacement qui CONTIENT le fait, jamais à un autre renvoi.

## 2. Quand utiliser le système

Le système BIBLE_LORE + WIKI est utilisé dès que l'univers nécessite un socle de lore fiable que le MJ ne peut pas reconstituer de mémoire. Le joueur décide en setup si une BIBLE est nécessaire.
- Si oui : BIBLE + WIKI portent le lore canon et les divergences établies. Le CODEX ne stocke que la mémoire chaude de session.
- Si non (codex pur) : le MJ se fie à ses connaissances + fetch. Le CODEX porte les divergences et les faits canon critiques.

## 3. Architecture à quatre couches

```
CODEX (vivant, mémoire chaude de session)
  |-> BIBLE_LORE (index + lore condensé, sur le dépôt, lue en entier à l'ouverture de chaque thread de build ; pas lue en jeu)
  |     |-> WIKI GitHub {Univers}/ (pages .md du monde, fetch à la demande ; index : Sommaire.md)
  |     |     |-> {Univers}/Roadmap/<Prota>/ (itinéraires par arc, par perspective de prota ; la roadmap en cours est un document de jeu)
  |-> Parties/{Univers}/Partie<n>/ (mémoire froide d'un RP donné, fetch à la demande ; index : Sommaire_Jeu.md)
        |-> Suivi/ (fiches PNJ affectés, protagoniste, mémoire refroidie)
        |-> Archives/ (CHRONO archivée, arcs clos)
        |-> Decisions/ (bifurcations prises dans ce RP)
```

Le CODEX ANNEXE_CHRONO pointe vers la roadmap COURANTE et son étape via `roadmap: cf. WIKI Roadmap/<Prota>/<page>.md | etape: <n>`, et tient le FIL LONG des arcs traversés (suite ordonnée des arcs déjà joués -> arc courant) : c'est lui qui porte la mémoire du chemin parcouru en jeu. Les décisions spécifiques à un RP sont tracées dans `Parties/{Univers}/Partie<n>/Decisions/`, et le passé joué archivé dans `Parties/{Univers}/Partie<n>/Archives/`.

### Roadmap et CODEX : deux rôles distincts
- ROADMAP (`Roadmap/<Prota>/`) : l'ITINÉRAIRE de l'arc - jalons dans l'ordre, casting, lieux, échelle temporelle, conditions de sortie (requis + interdits), verrous, roadmap suivante. Grain : le JALON (ce qui arrive, qui est là, où, quand ; matière dictée télégraphique). Le détail de scène n'y a pas sa place : il se met en scène EN JEU, à partir du jalon et des fiches. La roadmap EN COURS est un document de jeu : fetchée à l'ouverture du thread, elle fait foi sur la trame de l'étape. Elle porte aussi du futur : c'est un CADRAGE MJ, jamais un texte à annoncer en prose (Instructions RP §5).
- CODEX (ANNEXE_CHRONO) : l'ÉTAT D'ARC vivant ET LE FIL LONG - roadmap et étape courantes, jalon courant, statut, PLUS la suite ordonnée des arcs déjà traversés. C'est le CODEX qui tient où on en est ET d'où l'on vient ; la roadmap dit où l'on va. Le détail archivé du passé joué vit dans Parties/, indexé au Sommaire de jeu.

> ANTI-AMNÉSIE. En jeu on ne consulte pas la BIBLE. La mémoire de l'histoire repose sur deux sources, par horizon : (a) MÉMOIRE LONGUE / cohérence du chemin -> CODEX ANNEXE_CHRONO (fil ordonné des arcs traversés) + pages Parties/ indexées au Sommaire de jeu (fetch à la demande) ; (b) ÉTAPE COURANTE -> la roadmap en cours + les fiches de l'étape. La roadmap décrit le FUTUR PRÉVU, pas le PASSÉ VÉCU : ce n'est pas un substitut de mémoire.

### Flux de résolution d'un fait lore
1. CODEX (divergence fraîche du RP ?) -> si oui, utiliser.
2. Roadmap en cours et fiches déjà en contexte -> si oui, utiliser.
3. Sommaire.md (WIKI) ou Sommaire_Jeu.md (Parties/), déjà en contexte : identifier la page, puis fetch de la page.
4. Fetch / #SITES_REF (canon externe) -> si hors périmètre BIBLE + WIKI.
5. Invention prudente -> cohérente avec les échelons supérieurs.

---

## 4. BIBLE_LORE - Principes rédactionnels

### But : le monde en notices

La BIBLE dit qu'un fait EXISTE, ce qu'il est en une phrase, et à quoi il s'articule. Jamais comment il se déroule en détail : ça, c'est la fiche. Test d'admission d'une ligne de BIBLE : "sans elle, le MJ risque-t-il d'écrire une contradiction sans savoir qu'il faut fetcher ?" Non -> la ligne vit en fiche, pas en BIBLE.

Répartition des rôles, à ne plus perdre de vue :
- BIBLE = radar de FAITS. Elle couvre le monde par fait, pour que le MJ détecte quand fetcher. Les collisions de lore arrivent par fait, pas par page.
- Sommaire = index de PAGES. Il couvre le WIKI par page, pour dire où c'est écrit. Fetché en début de chaque thread de jeu : y déporter des résumés d'entités taxerait le document le plus lu du système.
- Fiches = DÉTAIL. Déroulés, texture, exhaustif.

Règles dérivées :
- Entrée d'entité (SB4 à SB7) plafonnée à 3-4 lignes dès qu'une fiche WIKI existe : notice + renvoi. Sans fiche, l'entrée peut être plus riche - la BIBLE est alors le domicile du fait.
- État de chantier INTERDIT en BIBLE (captures de session, questions de build en cours) : domicile _Implications / _Chantier_*.
- Décroissance obligatoire : à chaque BIBLE BUILD, tout fil résolu ou Tchekhov détoné se compresse en une ligne de statut + renvoi (le déroulé vit en roadmap/chrono). Une BIBLE qui ne fait que croître est une BIBLE qui dérive.


- Dense > exhaustif. Ligne télégraphique > phrase pleine.
- FOCUS : la bible ne couvre que le PÉRIMÈTRE NARRATIF défini par le joueur.
- Pas de narration, pas de prose, pas de métaphores.
- Pas d'adjectifs décoratifs ni de jugements de valeur.
- Phrases > 25 mots interdites.
- Ingestion : pour interroger le canon, requêter la forme d'origine du nom (accentuée si elle l'est : meilleur rappel).
- Aucune théorie de fans. Aucune spéculation non balisée.

### Niveaux de certitude
Chaque fait porte implicitement le niveau "établi" sauf balisage contraire :
- `[IMPLICITE]` - fortement impliqué par le canon mais jamais énoncé explicitement.
- `[INTERPRETATION]` - lecture cohérente mais débattue ou ambiguë. Le joueur tranche en OOC si le RP touche ce point.
- `[INCERTAIN]` - information contradictoire ou insuffisante dans les sources.
- `[DIVERGENCE RP]` - divergence du RP par rapport au canon, formalisée et validée par le joueur.

## 5. BIBLE_LORE - Budget

Plafond dur : 55 000 caractères.
Cible indicative : 35 000 à 40 000 caractères. Le plafond dur reste la limite de sécurité ; la cible est le régime de croisière d'une BIBLE en notices. Un build qui livre au-delà de la cible justifie l'écart (univers à très large cast, etc.).
Pas de contrainte de cohabitation CODEX + BIBLE : la BIBLE n'est pas lue en jeu, donc BIBLE et CODEX ne sont jamais en contexte ensemble. La BIBLE garde son plafond propre de 55 000 caractères : lue en entier à chaque ouverture de thread de build, elle se paie en contexte à chaque thread.
Le seuil de bascule retrieval (RAG) des fichiers de projet (SPEC_CODEX §3) ne concerne plus la phase build : BIBLE, SPEC et pages se fetchent, aucune ne se charge comme fichier de projet.
Vérification au build : `wc -m` (caractères, locale UTF-8) sur le fichier généré. Dépassement : signaler, proposer des compressions par gain décroissant (caractères récupérés + ce qu'on perd), le worldbuilder tranche. Compresser, jamais supprimer l'information utile sans validation.

Répartition indicative (guide, pas plafonds rigides par section) :

| Bloc | Fourchette | Rôle |
|---|---|---|
| SB0 | 1-2k | Métadonnées, wiki_base, parties_base |
| SB1-SB4 | 5-12k | Cosmogonie, lexique, chronologie condensée, factions |
| SB5 | 8-20k | Personnages (synthèses, croissance principale) |
| SB6-SB7 | 2-5k | Lieux, artefacts |
| SB8 | 2-5k | Mystères ouverts + définitions Tchekhov |
| SB9 | <1k | Pointeur vers {Univers}/Sommaire.md (index détaillé hors BIBLE, taille fixe) |

Principe directeur : SB1-SB8 contiennent assez pour que le MJ ne soit pas perdu sans fetcher. Le détail vit sur le WIKI et dans Parties/. Si une section (SB2, SB6, SB7) n'apporte pas de contexte ambiant indispensable, elle peut être allégée et vivre principalement sur le WIKI.

## 6. BIBLE_LORE - Architecture des sections

Fichier unique, lu en intégralité par le MJ à chaque tour DE BUILD (phase worldbuilding). JAMAIS chargé en narration (cf. §5 et §10).
Chaque section a un identifiant stable (`SB0`, `SB1`...).

### BIBLE auto-portante
Les sections pas encore remplies conservent le gabarit de la SPEC (lignes de structure, champs, format). Ainsi le MJ sait quoi remplir au prochain build sans refetcher la SPEC. La BIBLE livrée n'a jamais de section vide sans structure.

### Sections (ordre fixe, toutes optionnelles sauf SB0, SB1, SB9)

#### SB0 Métadonnées [OBLIGATOIRE]
- univers :
- sources primaires : <liste>
- bible_version : B<N>
- wiki_base : <URL racine du WIKI GitHub, forme blob - lecture humaine>
  Format : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
- raw_base : <URL racine du WIKI, forme raw - FETCH PAR DÉFAUT>
  Format : `https://raw.githubusercontent.com/sodomicka/rp/main/<Univers>/`
- parties_base : <URL racine de Parties/ GitHub pour le RP en cours, forme blob>
  Format : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
- parties_raw_base : <idem, forme raw - FETCH PAR DÉFAUT>
  Format : `https://raw.githubusercontent.com/sodomicka/rp/main/Parties/<Univers>/Partie<n>/`

  Les deux formes sont STOCKÉES, pas dérivées à la volée : le fetch par défaut se fait sur raw (markdown brut, aucun parsing), et une dérivation refaite à chaque appel est une occasion d'erreur pour zéro gain. Toutes les URLs se construisent par concaténation : base + chemin relatif. La forme blob reste utile pour un lien lisible et pour la méthode de secours (cf. §12).
- pages wiki rattachées :
  - <Dossier> - <description courte> (<N> pages)

#### SB1 Cosmogonie et règles du monde [OBLIGATOIRE]
Comment le monde fonctionne dans le périmètre du focus.
Inclut les divergences RP formalisées (balisées `[DIVERGENCE RP]`).
- <règle 1>
- <règle 2>

#### SB2 Lexique
`Terme - définition (1 ligne max)`

#### SB3 Chronologie
`Date/Ère | Événement | Conséquence`

Détail des étapes par arc : cf. {Univers}/Roadmap/<Prota>/.
En jeu : la roadmap en cours et son étape (désignées par le CODEX ANNEXE_CHRONO) cadrent l'arc ; le fil long des arcs traversés vient du CODEX ANNEXE_CHRONO.

Notes de cadrage chronologique en fin de SB3 sous `### Notes`.

#### SB4 Factions et groupes
`Faction - nature | objectif | alliés | ennemis | statut dans le focus`

#### SB5 Personnages
Personnages décrits NEUTREMENT : ce qui existe indépendamment d'une partie. Canon, ET OC promus au lore (un OC peut être prota dans une partie et entité de monde dans une autre - ex. un démon originel qui enrichit la théologie). La distinction n'est pas "OC vs canon" mais "existe sans cette partie ?".
- L'INSTANCE jouée d'un prota (état, run courant) ne figure PAS ici : elle vit en CODEX §3. Mais l'ENTITÉ, si elle existe hors de la partie, est décrite ici comme toute autre.
- Une RELATION à un prota va en perspective ou en neutre selon que le prota est un véhicule d'instance ou une entité de lore - décision worldbuilder, cf. règle de placement (§7).

Contenu AUTORISÉ :
- identité, rôle, affiliation, capacités, relations, sort connu ;
- traits comportementaux observables dans les sources ;
- motivations explicitement énoncées ou fortement impliquées ;
- rapport à une autre entité de lore (synthèse) ; un rapport à un prota-instance va en perspective, cf. §7.

Contenu INTERDIT :
- voix (registre, tics verbaux, ton) - ANNEXE_PNJ du CODEX ;
- état actuel dans le RP - CODEX §4 ;
- interprétation psychologique non fondée.

La frontière : la BIBLE dit QUI ils sont et CE QU'ILS ONT FAIT. Le CODEX dit COMMENT ils parlent et OÙ ils en sont.

Format :
`Nom - rôle | capacités-clé | relations | sort connu | certitude`
Si fiche WIKI détaillée : `detail: cf. WIKI <page>.md`. La BIBLE indexe le monde (= WIKI) ; Parties/ (archive d'une partie) s'atteint via le Sommaire, jamais par renvoi BIBLE.

#### SB6 Lieux
`Lieu - nature | rattachement | fonction narrative | état connu`

#### SB7 Artefacts et objets
Objets narrativement significatifs (pas l'inventaire du RP - cf. CODEX ANNEXE_INVENTAIRE).
`Objet - nature | origine | pouvoir/fonction | localisation connue | certitude`

#### SB8 Mystères ouverts et fils Tchekhov

Règle : SB8 porte, par mystère ou fil, la DÉFINITION et le STATUT (ouvert / armé / détoné / résolu) + renvoi. Les déroulés de détonation, conséquences jouées et captures d'état vivent en roadmap, chrono ou _Chantier_* - jamais ici. Un fil détoné ou résolu se compresse en une ligne au build suivant (décroissance, cf. §4).
Deux sous-sections :

##### Mystères
Questions non résolues, pertinentes au focus. Le MJ doit savoir ce qui est volontairement flou.
`Mystère - hypothèses principales | statut (ouvert / résolu-dans-RP / hors-périmètre)`

##### Tchekhov
Définitions des fils narratifs plantés dans le RP. L'ÉTAT de chaque fil (ouvert/armé/payé) est dans le CODEX ANNEXE_TCHEKHOV. La BIBLE porte les définitions stables.
`Fil - planté en | condition de détonation | conséquence attendue`

#### SB9 Index - routage [OBLIGATOIRE si WIKI présent]
SB9 ne contient PAS l'index détaillé page-par-page. Cet index vit dans `{Univers}/Sommaire.md` (page WIKI fetchée au début de chaque thread, cf. Instructions RP §4) ; celui de Parties/ vit dans `Sommaire_Jeu.md` de chaque partie, pour que SB9 reste de taille fixe et ne croisse plus avec le nombre de pages.

Contenu de SB9 :
- `Index détaillé page-par-page : cf. WIKI {Univers}/Sommaire.md`

Règles de SB9 :
- L'inventaire des dossiers (avec compte de pages) est déjà dans SB0 `pages wiki rattachées` - il sert de filet de sécurité si Sommaire.md tombe (listing direct via la méthode dossier de ACCÈS GITHUB).
- SB1-SB8 portent le résumé ambiant : le MJ sait CE QUI EXISTE sans fetch. Sommaire.md dit OÙ est le détail. La page cible porte le détail.
- Sommaire.md est fetché au début de chaque thread RP (carte de navigation centrale) et reste en contexte. Fetché tôt pour rester saillant (éviter le lost-in-the-middle). Règles d'usage : Instructions RP §4.
- Chaque page reste une unité autonome, fetchée en entier. L'URL se construit : `raw_base` ou `parties_raw_base` (SB0) + `<Dossier>/<Page>.md`.

---

## 7. WIKI - Spécification des pages

### Placement d'une fiche (règle générale, tous univers)
Pas de liste de catégories en dur : la structure s'organise par PRÉCÉDENT.
1. Consulter le Sommaire. Si le TYPE de fiche existe déjà -> s'aligner sur le dossier existant (précédent). Sinon -> appliquer les règles génériques de cette SPEC (granularité, nommage, neutre vs perspective) et créer le dossier.
2. Contenu qui existe INDÉPENDAMMENT de toute partie -> branche neutre `<Type>/`, décrit en lui-même. Un OC promu au lore en fait partie : son histoire ET ses relations sont du lore neutre.
3. Dès qu'une fiche MENTIONNE un prota, ou contient un élément potentiellement spécifique à une partie -> l'IA DEMANDE : lore neutre, ou sous-branche perspective `<Type>/<Prota>/` ? Le worldbuilder seul tranche, parce que la réponse dépend de son intention (l'OC est-il destiné au lore, ou véhicule d'instance ?). Jamais d'automatisme : le même OC peut être prota ici et entité-monde ailleurs.
4. Build pour un nouveau prota : pour chaque fiche pertinente, trois issues - RIEN À FAIRE / AJOUTER une sous-branche `<Type>/<Prota>/` / CRÉER en sous-branche. Ne jamais modifier la branche neutre ni les autres sous-branches sans validation.

Exemples d'arborescence : `Personnages/Macht/` (Macht neutre) ; `Personnages/<Prota>/` (perspective : relations à ce prota) ; `Roadmap/<Prota>/` (itinéraire vu par ce prota). Le neutre est l'intrant réutilisable, la sous-branche `<Prota>/` est ce qu'on ajoute par perspective - zéro retouche du neutre quand on ajoute un prota.

### Nature
Les pages WIKI sont des fichiers .md hébergés sur un dépôt GitHub public. Chaque page est une unité de consultation autonome, fetchée en entier.

Types de pages possibles :
- Sommaire (index détaillé de toutes les pages WIKI - voir gabarit ci-dessous).
- Fiches personnages approfondies (neutres `<Type>/` ou perspective `<Type>/<Prota>/`).
- Descriptions de lieux.
- Roadmaps (itinéraires par arc, par PERSPECTIVE de prota : `Roadmap/<Prota>/`).
- Power-scaling.
- Systèmes de magie/combat détaillés.
- Tout découpage thématique pertinent au RP.

### Principes rédactionnels
- Même registre que la BIBLE : factuel, sans narration.
- Niveaux de certitude identiques : établi / [IMPLICITE] / [INTERPRETATION] / [INCERTAIN] / [DIVERGENCE RP].

### Budget par page
- Plancher : 2 000 caractères (vérification : wc -m). En dessous : fusionner avec une page voisine.
- PAS DE PLAFOND de page : une page ne se scinde que sur DÉCISION du worldbuilder (lisibilité, ère close), jamais pour tenir un budget ; rien ne se compresse pour tenir un budget.
- Seule exception : roadmaps jusqu'à 15 000 caractères, 22 000 pour une roadmap passée en immersion (modes d'étape et tranches de vie, cf. Instructions Wiki §4, passe d'immersion). Document de jeu fetché seul et en entier : y renvoyer le MJ vers d'autres pages coûte plus que les caractères gagnés. Au-delà de 15 000 : signaler, proposer des coupes par gain décroissant, le worldbuilder tranche.

### Pages satellites d'entité

Quand le worldbuilder décide de scinder une fiche d'entité (lisibilité, ère close), elle se scinde en pages satellites nommées par volet :
- `<Entite>_chrono_<N>.md` : trajectoire datée par ère (précédent : Nisha_chrono_A/B).
- `<Entite>_inventaire.md` : objets, arsenal, possessions récurrentes.
- `<Entite>_relations_<N>.md` : réseau relationnel (règles propres : Satellite relations, ci-dessous).
La fiche mère garde le NOYAU (identité, mécanique, psychologie) et renvoie vers ses satellites. Sous le plancher de 2 000, un satellite refusionne dans la fiche mère.
Un satellite suit sa fiche mère : une fiche de groupe (précédent : Claudia_et_Lucio) a des satellites de groupe ; deux fiches distinctes ne partagent jamais un satellite.

### Satellite relations

OPTIONNEL. Tous les personnages n'y ont pas droit. Le worldbuilder le décide, le MJ peut le proposer, dans deux cas :
- la fiche mère devient difficile à lire ;
- les relations portent assez de texture pour mériter leur page (adresses qui changent selon l'interlocuteur, régimes avant/après une bascule, rituels), même sans saturation.
Sans satellite, les relations restent dans la fiche mère, avec les mêmes rubriques, adresses comprises.

DÉCOUPE. Une page par cercle quand le volume l'exige (précédent : Nisha_relations_proches, _famille, _boulot, _eleves_tokyo).

GROUPABLE. Une entrée peut viser un GROUPE (faction, cercle, fratrie) au lieu d'un individu, quand ses membres partagent la même relation à l'entité. Les membres qui font exception sont nommés dans l'entrée de groupe, avec leur usage propre. Un membre dont la relation va au-delà de l'exception garde sa propre entrée ; l'entrée de groupe le nomme sans redire son détail.

ADRESSES. Rubrique obligatoire de chaque entrée, individuelle ou de groupe : qui appelle qui comment, dans les deux sens ; tutoiement ou vouvoiement ; surnoms et leurs conditions (en privé, devant témoins, depuis telle date) ; exceptions nominatives. La liste est EXHAUSTIVE : une adresse qui n'y figure pas ne s'emploie pas, prénom compris. Un satellite peut poser la convention inverse en tête (" les appellatifs listés s'ajoutent aux prénoms, toujours disponibles " : précédent Nisha).

RÈGLES GÉNÉRALES. Une habitude d'adresse ou de comportement qui vaut pour tous les interlocuteurs (précédent : Nisha appelle toute femme " ma belle ") s'écrit une fois, en tête du satellite (ou de la première page d'une série), jamais entrée par entrée.

Frontière fiche/relations : la fiche mère garde la MÉCANIQUE d'une relation (domination, symbiose, pool partagé - tout ce qui touche au système de pouvoir) ; la page relations porte la TEXTURE (surnoms et adresses réciproques, rituels et habitudes, dynamique, ce que l'autre sait de l'entité, évolution datée télégraphique). Cross-renvois obligatoires dans les deux sens.

Gabarit page relations :
```
# <Entité> - Relations (<cercle>)

- version : W<N>

<Une ligne : satellite de quelle fiche, pages sœurs, où vit la mécanique.>

## Règles générales (si besoin)
- <habitude d'adresse ou de comportement valable pour tous les interlocuteurs>

## <Autre entité>
- Statut : <une ligne>
- Surnoms / adresses : <dans les deux sens ; tu/vous ; surnoms et conditions ; ce qui ne s'emploie pas>
- Rituels / habitudes : <...>
- Dynamique : <...>
- Ce que <l'autre> sait : <accès au secret, angles morts>
- Évolution datée : <télégraphique, par date>

## <Groupe> (entrée de groupe)
- Statut : <la relation commune aux membres>
- Surnoms / adresses : <usage du groupe> ; exceptions : <membres nommés, leur usage>
- Dynamique : <...>
```
Exemple de FORMAT (illustratif, NE PAS inscrire tel quel) :
```
## Les Rôdeurs (entrée de groupe)
- Surnoms / adresses : pour eux, Magnus et Markiona sont le Loup Noir et la Louve Blanche, jamais leurs vrais noms ; exceptions : Alidoro, Roméo et Léa emploient les vrais noms.
```

### Structure interne d'une page
Pas de gabarit imposé sauf pour les Roadmaps (cf. gabarit ci-dessous). Obligations :
1. Titre clair en H1, correspondant au nom de la page.
2. Métadonnée unique : version (W<N>). Aucune autre métadonnée (pas d'univers, dossier, sources, bible rattachée : l'indexation va de la BIBLE vers la page via le Sommaire, jamais l'inverse).
3. Contenu structuré en sections si pertinent.
4. Pas de contenu narratif (sauf pages transcript = verbatim).

### Trajectoire datée (gabarit fiche d'entité)
Troisième strate de toute fiche perso/lieu/objet. Décrit le DEVENIR DATÉ de l'entité APRÈS le point de départ. N'existe que dans la fiche pleine ({Univers}/). En jeu, l'état d'une entité à l'ouverture d'une étape se lit dans cette strate, à la date de l'étape ; ce qui est daté après n'est su de personne et ne se joue pas.
Règles :
- Forme télégraphique, une ligne par événement. Pas de prose ; le détail narratif vit dans la roadmap.
- ALIMENTATION À CHAUD : une entrée est ajoutée UNIQUEMENT après avoir roadmappé l'arc qui la produit. Jamais d'anticipation.
- CANON PAR DÉFAUT, neutre, réutilisable entre parties (comme les roadmaps).
- OVERRIDE PAR PARTIES/ : quand une partie diverge, le delta va en Parties/{Univers}/Partie<n>/ et SURCLASSE cette strate pour la partie concernée (routage §7 inchangé).
- CONSOLIDATION : les pointeurs datés jadis en Notes de frontière (mort canon, éveil, départ...) migrent ici sous forme datée ; Notes de frontière ne garde que les renvois non datés et les hors-périmètre.
- PLAFOND : par défaut 30 entrées max par fiche. Dérivation : une ligne télégraphique fait ~120 car., 30 lignes ~3 600 car., soit une strate qui reste lisible d'un coup d'œil. Le worldbuilder ajuste par univers ; il ne laisse PAS le champ vide - un placeholder non rempli dans une SPEC est une règle morte, et les Instructions Wiki interdisent explicitement de laisser un [A definir] pour esquiver une question. Au-delà du plafond : compresser ou déporter en roadmap ; dépassement signalé, jamais compressé seul.
Gabarit :
```
## Trajectoire datée
| Date/ère | Événement | Delta d'état |
|---|---|---|
| <date> | <événement télégraphique> | <ce qui change : grade, doigts, sort débloqué, statut, relation> |
```
Exemple de FORMAT (illustratif, NE PAS inscrire tel quel) :
```
| 2006 | Affrontement de Toji, éveil | passe à 23 doigts ; débloque Rouge, Violet, Extension de Territoire |
```

### Gabarit Roadmap

Les roadmaps vivent dans `{Univers}/Roadmap/<Prota>/`, une par arc, par perspective de prota. Les décisions prises dans un RP donné sont tracées dans `Parties/{Univers}/Partie<n>/Decisions/`.

DOCUMENT DE JEU. La roadmap en cours est fetchée à l'ouverture de chaque thread de jeu (Instructions RP §4) et reste en contexte tout le thread, avec les fiches de son casting. Elle doit donc porter tout ce que le MJ doit savoir pour mener l'arc sans vue d'ensemble de la saga : où on va, qui est là, ce qui est requis, ce qui est interdit.

GRAIN. Le jalon : ce qui arrive, qui est là, où, quand. Le détail de scène (mise en scène, répliques, gestes) ne s'écrit pas : il se joue en jeu, à partir du jalon et des fiches. Test : un détail qui ne déplace pas le jalon n'a pas sa place en roadmap.

```
# Roadmap <N> - <Titre>

- version : W<N>
- statut : <à venir | en cours | clos> ; <JOUABLE | NON JOUABLE (narrée)>
- prota / POV : <...>
- échelle temporelle : <durée réelle in-world, ex. ~190 ans, ~3 jours, une journée>
- borne d'entrée : <situation de départ>
- borne de sortie : <situation qui clôt l'arc> -> <roadmap suivante>
- roadmap précédente : cf. WIKI Roadmap/<Prota>/<page>.md (ou "aucune - premier arc")
- roadmap suivante : cf. WIKI Roadmap/<Prota>/<page>.md (ou "aucune - fin" ; embranchement : une ligne par sortie, annotée de sa condition)

## Intention
<1 à 3 lignes : ce que l'arc doit faire ressentir ou établir>

## Itinéraire (jalons)
1. <jalon> [JOUÉE | AU CHOIX, date] : ce qui arrive, qui, où, quand
2. <jalon>
...
Bloc couvrant un long laps à rendre en vignettes : marquer `[SNAPSHOTS - <durée chiffrée>]`.
Modes d'étape (posés à la passe d'immersion) : `[JOUÉE]` = rythme classique ; `[AU CHOIX]` = rapide ou classique au choix du joueur (Instructions RP §3, modes d'étape).

## Tranches de vie
- <scène de quotidien sans date, une ligne> (optionnel ; posé à la passe d'immersion)

## Casting convoqué
- <Nom> - <rôle dans l'arc> - cf. <Type>/<page>   (ou "non fiche" + description d'une ligne)

## Lieux et objets
- <Lieu ou objet> - <fonction dans l'arc> - cf. <Type>/<page>   (ou "non fiche" + description d'une ligne)

## Conditions de sortie
### Requis
- <action que le joueur doit avoir accomplie pour que l'arc se close>
### Interdits
- <action que le protagoniste ne peut pas accomplir> - <ce qu'elle casserait : arc ou fait ultérieur concerné>

## Verrous
- Jalon <n> : <choix du joueur dont la saga dépend>. Paliers :
  1. <palier le plus doux>
  2. Refus maintenu : <palier suivant>
  ...
  n-1. Avertissement du MJ : la suite n'est pas scénarisée et mène à l'avortement du RP.
  n. Entêtement maintenu : le MJ déclare la fin du RP et ne narre plus dans ce thread ; rejouer = nouveau thread, CODEX d'entrée réutilisé sans modification.

## Bifurcations
- Embranchement, après jalon <n> : si <condition A> -> <conséquence, roadmap suivante A>. Si <condition B> -> <conséquence, roadmap suivante B>.

## Notes de frontière
- <ce qui appartient à l'arc suivant, nommé sans être déroulé>

---
FIN_WIKI_ROADMAP_<PROTA>_<N>
```

ÉCHELLE TEMPORELLE : obligatoire et chiffrée. Elle dit au MJ à quelle vitesse le temps s'écoule sur l'arc, pour qu'il cale l'écoulement par défaut sur l'arc et non sur son envie de scènes (Instructions RP §3). Un bloc `[SNAPSHOTS]` porte sa propre durée : elle borne l'ellipse. Compresser n'est PAS supprimer : le joueur doit sentir le temps passer.

CONDITIONS DE SORTIE. Le MJ en jeu n'a pas la vue d'ensemble de la saga : la roadmap la lui donne sous forme de règles.
- REQUIS : ce que le joueur doit avoir fait pour que l'arc se close. Tant qu'un requis manque, la borne de sortie n'est pas atteinte.
- INTERDITS : ce que le protagoniste ne peut pas faire, parce que ça casserait cet arc OU un arc ultérieur (interdits INTER-ROADMAPS : tuer un personnage dont la saga a besoin plus tard, révéler un secret avant son heure...). Le bon sens n'a pas besoin d'être écrit ; ce qui dépend de la vue d'ensemble, si. Chaque interdit nomme ce qu'il protège, pour que le MJ en mesure le poids.
- En jeu, un requis refusé ou un interdit tenté se tient par les paliers d'un verrou : le MJ force la main du plus doux au plus dur, jamais en annonçant la raison en prose.

BIFURCATIONS, deux usages.
- EMBRANCHEMENT : le récit se sépare en deux chemins (tuer ou épargner un personnage central...). Coûteux : chaque branche exige ses propres suites et une roadmap suivante par sortie.
- JALON VERROUILLÉ : un choix du joueur dont la saga dépend. Pas de seconde branche : le MJ force la main par paliers, du plus doux au plus dur, en jeu (un PNJ insiste, un autre vient en renfort, le groupe fait pression, une autorité tranche) ou en méta quand aucun PNJ ne peut le porter (rappel du MJ hors fiction). Si le refus tient, le MJ avertit que la suite n'est pas scénarisée, puis déclare la fin du RP en dernier recours.
- À chaque roadmap, le MJ de build repère les choix du joueur dont la saga dépend et propose un verrou pour chacun, et les interdits inter-roadmaps que les arcs suivants imposent.

### Gabarit Sommaire

`{Univers}/Sommaire.md` porte l'index détaillé du WIKI que SB9 ne porte plus : une entrée par page, groupée par dossier. Fetché au début de chaque thread RP. Mis à jour via BIBLE BUILD à chaque ajout de page. Parties/ a son propre index : le Sommaire de jeu (§8).

```
# Sommaire - {Univers}

- version : W<N>

## WIKI

> Chaque entrée porte la version `(W<N>)` de la page : inventaire de versions. Un écart entre ce W<N> et celui écrit dans la page elle-même signale une copie périmée (canari, non bloquant).
>
> QUI LIT LE CANARI. Deux lecteurs, deux moments :
> - EN NARRATION, à chaque page fetchée : le MJ compare le `W<N>` de la page au `W<N>` de son entrée au Sommaire. Écart -> `[VERSION DECALEE - <page> : Sommaire W<x>, page W<y>]` en OOC bref, NON BLOQUANT. Arbitrage : la PAGE fait foi (c'est le fichier réel ; le Sommaire n'est qu'un index). Cf. Instructions RP §4.2ter.
> - AU BIBLE BUILD : toute page relivrée incrémente son `W<N>` et son entrée au Sommaire est mise à jour DANS LE MÊME BUILD. C'est ici que se solde un `[VERSION DECALEE]` remonté en jeu.

### <Dossier>/
Description : <contenu du dossier en 1 ligne>
- <Page>.md (W<N>) - <description courte du contenu>

### Roadmap/<Prota>/
Description : itinéraires par arc, dans l'ordre de la saga. La roadmap en cours est fetchée à l'ouverture de chaque thread de jeu (désignée par le CODEX).
- <Roadmap>.md (W<N>) - <arc, bornes, échelle temporelle>

> NON INDEXÉS. Le garde-cap (`Roadmap/<Prota>/00_Garde_Cap.md`) : source de build, jamais fetché en narration. `Parties/<Partie>/Memoires/` : archives narratives interdites en jeu (sauf ordre OOC explicite), consultées au BUILD seulement par listing direct du dossier. Indexer un dossier le fait paraître fetchable en narration.

---
FIN_WIKI_SOMMAIRE
```

### Maintenance
Pages WIKI mises à jour via BIBLE BUILD. Statiques entre deux builds.

---

## 8. Parties - Spécification

### Nature
Les pages Parties/ sont des fichiers .md hébergés sur le même dépôt GitHub, dans `Parties/{Univers}/Partie<n>/`. Elles constituent la mémoire froide d'un RP donné. Chaque `Partie<n>` est un RP autonome dans le même univers, ce qui permet de jouer plusieurs RP en parallèle avec des bifurcations différentes.

### Structure
```
Parties/{Univers}/
  Partie1/
    Sommaire_Jeu.md - index de la mémoire de la partie (gabarit ci-dessous). Écrit par le CODEX V1 puis tenu à jour par chaque CODEX BUILD. Fetché à l'ouverture de chaque thread de jeu.
    Suivi/
      <Protagoniste>_Fiche.md - backstory COMPLÈTE + identité du protagoniste (froid, fetch à la demande). PAS les capacités ni l'état : ils vivent dans le CODEX §3 (capacités ancrées en §3a). Le CODEX §3a porte le résumé chaud de cette backstory.
      <PNJ>_Suivi.md - tracking des PNJ affectés par la narration
    Archives/
      CHRONO_<arc>.md - chronologie archivée d'un arc clos
    Decisions/
      Decisions_<arc>.md - bifurcations prises dans ce RP par rapport à la roadmap
    Memoires/
      Memoire_{Univers}_<n>.md - archive NARRATIVE figée d'un thread (livrable 3 du CODEX BUILD).
        NON indexée au Sommaire (même doctrine que Roadmap/ : un dossier indexé paraît fetchable en jeu).
        INTERDITE en narration sauf ordre OOC explicite. Fetchable AU BUILD pour recalibrer
        ANNEXE_STYLE uniquement - elle rend du TON, jamais des faits. Hors budget de page.
        Accès par listing direct du dossier (cf. §12). Cf. SPEC_CODEX 4ter, livrable 3.
  Partie2/
    Suivi/
    Archives/
    Decisions/
```

### Gabarit Sommaire de jeu

Le MJ doit savoir OÙ piocher sans tout fouiller : chaque entrée liste les SUJETS que la page couvre (personnages, lieux, objets, fils, période). Un sujet qui n'y figure pas n'est pas dans la page.

```
# Sommaire de jeu - {Univers} Partie<n>

- version : W<N>

> Index de la mémoire froide de la partie. Écrit par le CODEX BUILD, fetché à l'ouverture de chaque thread de jeu, reste en contexte. Route un trou objectif vers la page qui le porte. `Memoires/` n'est pas indexé (interdit en jeu).

### Suivi/
- <Page>.md (W<N>) - <contenu en une ligne> | sujets : <personnages, lieux, objets, fils, période>

### Archives/
- <Page>.md (W<N>) - <arc clos, période> | sujets : <...>

### Decisions/
- Decisions_<Arc>.md (W<N>) - <bifurcations de l'arc> | sujets : <...>

---
FIN_PARTIES_SOMMAIRE_JEU
```

### Gabarit Decisions

Les pages Decisions/ tracent les choix spécifiques à un RP par rapport à la roadmap commune. Elles permettent de comparer les parties entre elles.

```
# Decisions_<Arc>

- partie : <n>
- version : W<N>
- roadmap : cf. WIKI Roadmap/<Prota>/<page>.md

## Bifurcations prises
| Étape roadmap | Choix canonique | Choix de cette partie | Conséquence |
|---|---|---|---|
| <#> | <branche par défaut> | <ce que le joueur a fait> | <impact> |

---
FIN_PARTIES_DECISIONS_<ARC>
```

### Règles
- Les fiches Suivi/ sont mises à jour entre les sessions via CODEX BUILD (mémoire refroidie) ou BIBLE BUILD. Toute page Parties/ créée ou relivrée est reportée au Sommaire de jeu dans le même build.
- Les Archives/ sont en écriture seule : une fois archivée, une CHRONO n'est plus modifiée (sauf correction d'erreur).
- Budget par page : même contrainte que le WIKI (plancher de 2 000 caractères, pas de plafond). EXCEPTION : `Memoires/` (archive narrative, hors plancher).

### Fetch
- Règles, déclencheurs et budgets : cf. Instructions RP §4 (ouverture de thread, déclencheur objectif, TTL). Non dupliqués ici. Le routage passe par le Sommaire de jeu.
- Seules nuances propres à Parties/ : Archives/ en fetch exceptionnel (flashback, vérification) ; Decisions/ à la demande pour vérifier un choix antérieur ; `Memoires/` JAMAIS en narration (sauf ordre OOC explicite) - réservé au CODEX BUILD, usage unique : recalibrage d'ANNEXE_STYLE.

---

## 9. Règles de build (BIBLE BUILD)

### Déclenchement
Le joueur demande un BIBLE BUILD explicitement (`#BIBLE_BUILD`) ou implicitement (toute demande de création, mise à jour ou modification de la BIBLE et/ou du WIKI). Pour une modification ponctuelle (corriger un fait, ajouter une ligne), le MJ fournit les blocs à remplacer sans rebuild complet.

Le joueur fournit :
1. L'univers cible.
2. Le focus narratif (ère, arc, faction, région).
3. Les sources : fichiers joints et/ou URL à fetcher.
4. La liste des dossiers/pages souhaitées (ou "à déterminer ensemble").

### Fetch de la SPEC
Au premier BIBLE BUILD (aucune BIBLE existante), le MJ LISTE d'abord `Config/` pour relever le numéro de version courant (Instructions Wiki §8 : clone sans blobs par défaut, listing github.com/tree en secours), PUIS fetche la SPEC correspondante.
Ne JAMAIS recopier un numéro de version figé depuis un document (SPEC, instructions, BIBLE) : c'est le mécanisme de la spec fantôme - un build fait sur une révision périmée dont personne ne s'aperçoit. Si la SPEC n'est pas encore sur le dépôt (tout premier build, rien n'existe), le joueur la fournit en fichier joint ou dans le chat pour ce premier thread. Après ce premier build, le MJ écrit la SPEC dans Config/ (Instructions Wiki §8bis) et tout passe en fetch.

Pour les builds suivants, la BIBLE elle-même sert de référence (gabarit intégré dans les sections vides). Le fetch de la SPEC n'est nécessaire que si le MJ a besoin de vérifier une règle de construction.

### Processus - Phase 1 : Genèse de la bibliothèque
Si construction collaborative :
1. Inventorier les sources disponibles.
2. Proposer une architecture de WIKI adaptée au RP.
3. Le joueur valide, ajuste ou complète.
4. Pour chaque fait ambigu, le MJ pose la question - le joueur tranche.
5. Construire les pages une par une ou par lot thématique, validation par dossier.
6. La BIBLE_LORE est construite en dernier - elle condense le WIKI et génère SB9.

### Processus - Phase 2 : Construction directe
Si sources complètes et plan clair :
1. Lire toutes les sources.
2. Construire les pages WIKI selon le plan.
3. Construire la BIBLE_LORE avec SB9 indexé.
4. Livrer tous les fichiers.

### Sortie du build
- BIBLE_LORE : un fichier .md, à la racine de `{Univers}/` sur le dépôt. Les sections pas encore remplies conservent le gabarit (structure, champs, format) pour les builds futurs.
- Pages WIKI : fichiers .md individuels par dossier, écrits sur le dépôt par le MJ (Instructions Wiki §8bis).
- Pages Parties/ : fichiers .md si nécessaire, écrits de la même façon dans Parties/{Univers}/Partie<n>/.
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

### Sources autorisées
- Transcripts in-game, guides/wikis officiels.
- Bases de données communautaires de haute qualité (en extrayant les FAITS, pas les interprétations).
- Notes du joueur.
- Exports de threads précédents.

### Sources interdites
- Théories de fans - sauf validation OOC explicite comme canon local.
- Contenu généré par IA non vérifié.
- Novélisations ou adaptations non canoniques.

### Fetch pendant le build
Si le joueur fournit des URL : fetcher et extraire.
Si le joueur fournit des fichiers : lire et extraire.
Le MJ ne fetche PAS de sources supplémentaires de sa propre initiative. Trou critique -> `[INCERTAIN]` + suggestion de source en OOC.

---

## 10. Utilisation en narration

Les règles d'usage en narration (déclencheur objectif de fetch, TTL, séquence d'ouverture de thread, gestion des échecs de fetch et backstop anti-invention) vivent dans les Instructions RP (§4) et ne sont PAS dupliquées ici : une règle de narration écrite dans une SPEC que la narration ne charge jamais est du texte mort qui désynchronise en silence.

Seuls invariants côté SPEC :
- Chaque page WIKI/Parties est une unité autonome, fetchée en entier.
- La BIBLE_LORE est le document DE LA PHASE BUILD : lue en entier à l'ouverture de chaque thread de worldbuilding, elle sert d'index permanent. En jeu elle n'est PAS lue : la roadmap en cours et les fiches de l'étape portent le lore utile ; la BIBLE ne se récupère qu'en dernier recours, sur trou objectif qu'aucune page ne couvre (cf. Instructions RP §1, §2.1).

### Ce que la BIBLE, le WIKI et Parties/ ne font PAS
- Pas de voix PNJ (ANNEXE_PNJ du CODEX).
- Pas d'état actuel du RP (CODEX §4).
- Pas de mise à jour pendant le RP. Statiques entre deux builds.

---

## 11. Mise à jour

La BIBLE_LORE, le WIKI et Parties/ sont statiques pendant le RP - pas de mise à jour à chaque CODEX BUILD.
Le joueur peut demander un BIBLE BUILD entre deux sessions pour :
- ajouter des sources ou des pages ;
- formaliser des divergences fraîches (CODEX ANNEXE_LORE -> BIBLE SB1/SB3 ou WIKI) ;
- archiver la CHRONO dans Parties/ ;
- mettre à jour les fiches Suivi/ ;
- enregistrer les décisions dans Decisions/ ;
- corriger des erreurs ;
- réorganiser la structure.

Lors d'un rebuild, le numéro de version de la BIBLE incrémente (B1 -> B2 -> ...). L'historique des changements vit dans git (log + diff), pas dans un journal interne au fichier.
Les pages WIKI/Parties modifiées sont re-livrées ; les autres restent intactes.
Le MJ écrit les fichiers mis à jour sur le dépôt (Instructions Wiki §8bis).

---

## 12. Dépôt GitHub - Convention

### Structure du dépôt
```
sodomicka/rp/
  Config/
    SPEC_CODEX_v8_10.md
    SPEC_BIBLE_LORE_WIKI_v9_2.md
    (numéros indicatifs : vérifier le listing réel de Config/ avant tout fetch)
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
- Une SPEC modifiée change de numéro (nom de fichier + titre) : sinon deux fichiers différents revendiquent le même numéro, c'est le mécanisme même de la spec fantôme.
- Chaque SPEC a sa propre numérotation : SPEC_BIBLE_LORE_WIKI et SPEC_CODEX évoluent séparément.
- L'historique des changements vit dans git (log + diff), jamais dans le fichier : ni commentaire de révision, ni ligne Revision, ni étiquette de version sur une règle (SPEC et instructions).

### URL de consultation
FETCH (défaut) - forme raw, markdown brut, sans parsing :
- Page WIKI : `raw_base` + `<Dossier>/<Page>.md`
- Page Parties/ : `parties_raw_base` + `<Dossier>/<Page>.md`
- SPEC : `https://raw.githubusercontent.com/sodomicka/rp/main/Config/<fichier>.md`

LIEN LISIBLE / SECOURS - forme blob (parsing requis, cf. Instructions RP §4 méthode 2) :
- Page WIKI : `wiki_base` + `<Dossier>/<Page>.md`
- Page Parties/ : `parties_base` + `<Dossier>/<Page>.md`
- SPEC : `https://github.com/sodomicka/rp/blob/main/Config/<fichier>.md`

Règle : on FETCHE en raw, on CITE en blob. Une URL blob passée à un fetcheur oblige à parser du HTML pour rien.

### Visibilité
Le dépôt doit être PUBLIC pour que fetch fonctionne sans token.

---

# GABARIT DE SORTIE - BIBLE_LORE

# BIBLE_LORE_{UNIVERS}

## Table des matières
- SB0 Métadonnées
- SB1 Cosmogonie et règles du monde
- SB2 Lexique
- SB3 Chronologie
- SB4 Factions et groupes
- SB5 Personnages
- SB6 Lieux
- SB7 Artefacts et objets
- SB8 Mystères ouverts et Tchekhov
- SB9 Index - routage

## SB0 Métadonnées
- univers :
- sources primaires :
- bible_version : B<N>
- wiki_base : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
- raw_base : `https://raw.githubusercontent.com/sodomicka/rp/main/<Univers>/`
- parties_base : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
- parties_raw_base : `https://raw.githubusercontent.com/sodomicka/rp/main/Parties/<Univers>/Partie<n>/`
- pages wiki rattachées :
  - <Dossier> - <description courte> (<N> pages)

## SB1 Cosmogonie et règles du monde
- <règle 1>
- <règle 2>

## SB2 Lexique
`Terme - définition (1 ligne max)`

## SB3 Chronologie
| Date/Ère | Événement | Conséquence |
|---|---|---|
| <date> | <événement> | <conséquence> |

Détail des étapes par arc : cf. {Univers}/Roadmap/<Prota>/.
En jeu : la roadmap en cours et son étape (désignées par le CODEX ANNEXE_CHRONO) cadrent l'arc ; le fil long des arcs traversés vient du CODEX ANNEXE_CHRONO.

### Notes
- <note de cadrage>

## SB4 Factions et groupes
`Faction - nature | objectif | alliés | ennemis | statut dans le focus`

## SB5 Personnages
`Nom - rôle | capacités-clé | relations | sort connu | certitude`
Si fiche WIKI détaillée : `detail: cf. WIKI <page>.md`. La BIBLE indexe le monde (= WIKI) ; Parties/ (archive d'une partie) s'atteint via le Sommaire, jamais par renvoi BIBLE.

## SB6 Lieux
`Lieu - nature | rattachement | fonction narrative | état connu`

## SB7 Artefacts et objets
`Objet - nature | origine | pouvoir/fonction | localisation connue | certitude`

## SB8 Mystères ouverts et Tchekhov

### Mystères
`Mystère - hypothèses principales | statut (ouvert / résolu-dans-RP / hors-périmètre)`

### Tchekhov
`Fil - planté en | condition de détonation | conséquence attendue`

## SB9 Index - routage

Index détaillé page-par-page : cf. WIKI {Univers}/Sommaire.md
(Inventaire des dossiers : cf. SB0 pages wiki rattachées.)

---

FIN_BIBLE_B<N>

---

# GABARIT DE SORTIE - PAGE WIKI / PARTIES

# <Titre de la page>

- version : W<N>

## <Section 1>
<contenu structuré>

## <Section 2>
<contenu structuré>

---

FIN_WIKI_{DOSSIER}_{PAGE}
