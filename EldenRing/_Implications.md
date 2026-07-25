# Journal d'implications - Elden Ring

- version : W6
- nature : bloc-notes de coordination du build. Doutes non tranches, points a reverifier,
  questions en attente. Document de TRAVAIL, jamais fetche en narration.

## Decisions actees (worldbuilder, 2026-07-24)

| # | Sujet | Decision |
|---|---|---|
| D1 | Nightreign | Continuite separee. Pont balise `[SOURCE NIGHTREIGN]` vers les fiches ER. Sens inverse interdit. |
| D2 | Canonicite | Doctrine graduee. Etabli = enonce dans le texte du jeu ; le reste balise. |
| D3 | Sources | Dump de texte du jeu en primaire, wikis communautaires en appoint sur les faits structurels. Le worldbuilder comble les trous restants. |
| D4 | Granularite | Exhaustif au sens "aucune ligne du corpus perdue". Trois niveaux : fiche / catalogue / corpus. |
| D5 | SPEC | Non modifiee. Exception d'indexation documentee en tete du Sommaire EldenRing. |
| D6 | Demarrage | Corpus + architecture complete avant toute redaction de lore. |
| D7 | Granularite (REVISION) | "Granularite totale" DEFAITE. Branche Catalogues/ supprimee : elle dupliquait le corpus. Deux niveaux seulement, corpus et fiche redigee. Objectif reformule : le systeme dans les grandes lignes, sans trou INVISIBLE. |
| D8 | Registre des trous | Section `Trous et contraintes de comblement` adossee a CHAQUE page redigee, en quatre lignes (question / DIT / NON DIT / CONTRAINTES). Index transversal agrege plus tard. |
| D10 | Budget des pages | Plafond porte a 10 000 caracteres pour une page livree par le MJ, 15 000 apres integration des modifications du worldbuilder. Exception documentee au plafond de 8000 de la SPEC. |
| D12 | Narration visuelle | Le design est une source de lore a part entiere, que le corpus textuel ne capte pas. Registre dedie `_Observations_Visuelles.md`, alimente par le WORLDBUILDER (le MJ ne voit pas le jeu). Balise `[VISUEL]` pour le fait de design, `[INTERPRETATION]` pour la lecture qu'on en tire - jamais fusionnees. Chaque observation declare si le corpus la corrobore, l'ignore ou la contredit. |
| D13 | Seuil page pilote | Destined_Death.md passe a 15 000 caracteres. |
| D11 | Ordre des chantiers | ELDEN RING d'abord (base + Shadow of the Erdtree), Nightreign ensuite. Sources hors-texte (datamining, trailers, theories retenues) traitees dans des threads dedies, en passes ulterieures. |
| D9 | Priorite | Carte structurelle d'environ 25 pages. Fiches de personnages et de lieux creees a la demande, quand un arc les convoque. |

## Questions ouvertes

| # | Question | Statut |
|---|---|---|
| Q1 | Perimetre des fiches individuelles Personnages : 254 PNJ nommes, combien meritent une fiche ? | EN ATTENTE |
| Q2 | Perimetre des fiches individuelles Lieux : 436 lieux nommes, meme question. | EN ATTENTE |
| Q3 | Frontiere Artefacts/ vs Catalogues/ : quel critere exact fait qu'un objet merite sa fiche ? | EN ATTENTE |
| Q4 | Chronologie : Elden Ring ne fournit quasiment aucune date absolue. Faut-il poser un axe relatif normalise (ex. "avant/apres Shattering") ou un axe numerote arbitraire ? | EN ATTENTE |
| Q5 | Un protagoniste est-il deja pressenti ? Le Tarnished est un personnage muet ; le RP se fera-t-il avec un OC Tarnished, ou une autre nature d'entite ? | HORS PASSE 0, a poser au SETUP |

## A verifier au moment du build (faits avances en conversation, non encore sources)

| # | Fait | Source a etablir |
|---|---|---|
| V1 | Le Shard que possede Heolstor provient du Shattering. | Corpus Nightreign, non constitue |
| V2 | La Revenant renseigne le sort du corps de Ranni. | Corpus Nightreign, non constitue |
| V3 | Le Guardian renseigne les Stormhawks. | Corpus Nightreign, non constitue |
| V4 | L'Executor renseigne le Crucible. | Corpus Nightreign, non constitue |

Ces quatre points sont des affirmations du worldbuilder, retenues comme axes de travail. Ils
seront sources au moment de builder la branche Nightreign, conformement a la doctrine graduee.

## Carte structurelle - 25 pages [PROPOSE, NON TRANCHE]

Cosmologie (5) : Erdtree | Elden_Ring_et_Elden_Beast | Greater_Will_et_les_Fingers |
Outer_Gods | Lands_Between_et_Land_of_Shadow

Systemes (11) : Grace | Runes_et_Great_Runes | Golden_Order | Destined_Death [FAIT] |
Those_Who_Live_in_Death | Crucible | Empyreans_et_succession_divine | Sorceries |
Incantations | Frenzied_Flame | Scarlet_Rot

Factions (6) : Golden_Lineage | Carian_et_Raya_Lucaria | Black_Knives_et_Numen |
Omen_et_Hornsent | Ancient_Dragons_et_Dragon_Cult | Nox_Eternal_Cities_et_Albinaurics

Chronologie (3) : Chronologie_Generale | Night_of_the_Black_Knives | Shattering

Ordre d'attaque propose : Erdtree, Golden_Order et Grace en premier lot - ils se contraignent
mutuellement, les ecrire ensemble fait remonter les contradictions pendant qu'on a le contexte.

## Outil de verification

`verif_citations.py` (livre hors depot) controle que chaque citation anglaise d'une page existe
LITTERALEMENT dans _Corpus/. Etat au 2026-07-25 : 116 citations verifiees, 0 echec.

L'outil a ete valide par controle inverse : trois erreurs volontairement introduites dans trois
pages ont bien ete detectees. Il avait auparavant un defaut d'appariement des guillemets - un
extrait court comme "Erdtree" decalait toutes les paires suivantes et rendait le controle de la
page inoperant sans le signaler. Corrige. Trois erreurs REELLES ont ete trouvees et corrigees
grace a lui : une troncature de citation dans Erdtree.md, une ellipse non litterale dans
Golden_Order.md, une casse fautive dans Grace.md.

## Etat de la carte structurelle : COMPLETE

25 pages sur 25. Passe 0 achevee : corpus, architecture, carte structurelle, BIBLE B1.

Build autonome du 2026-07-25, en trois lots de sept pages plus une relecture croisee et huit
sections de BIBLE. 59 agents, aucune erreur.

CHIFFRES DU BUILD
- 25 pages redigees, chacune avec 4 a 6 trous documentes et leurs contraintes de comblement.
- 1 179 citations anglaises verifiees LITTERALEMENT contre le corpus par script. Zero echec.
- 166 inventions detectees et corrigees par les auditeurs adversariaux AVANT livraison.
- 136 questions remontees au worldbuilder, aucune tranchee (cf. _Questions_Worldbuilder.md).
- 33 collisions inter-pages relevees a la relecture croisee, dont 4 BLOQUANTES, corrigees
  (cf. _Relecture_Croisee.md).
- BIBLE_LORE_ELDENRING B1 : 54 847 caracteres pour un plafond de 55 000.

CE QUE LE DISPOSITIF A COUTE ET RAPPORTE
Sans l'audit adversarial, 166 affirmations non sourcees seraient entrees au wiki : la redaction
seule, meme cadree par une doctrine explicite, ne suffit pas. Le controle par script ne remplace
pas l'audit et l'audit ne remplace pas le script - le premier attrape les citations inexactes,
le second les affirmations sans citation.

FAILLE CORRIGEE DANS L'OUTIL DE VERIFICATION
verif_citations.py ignorait les extraits de moins de 20 caracteres ; un extrait court decalait
en outre l'appariement de tous les guillemets suivants, rendant le controle d'une page inoperant
SANS le signaler. Seuil abaisse a 10 caracteres, appariement corrige. La correction a
immediatement revele deux citations fautives dans Grace.md, page ecrite a la main.

## Inventaire Nightreign etabli (noms seuls, sans lore)

AVERTISSEMENT DE RIGUEUR : le corpus NR donne des NOMS, pas des ROLES. Il n'etablit pas qu'une
entite est un Nightlord ou un Nightfarer - il donne son nom. Seul "Heolstor the Nightlord"
porte le titre dans son nom meme. Les regroupements ci-dessous sont donc des HYPOTHESES DE
CLASSEMENT [INCERTAIN], a confirmer quand un dump de texte existera.

Entites nommees a motif nocturne (statut de Nightlord NON etabli par le corpus, sauf Heolstor) :
Adel, Baron of Night | Animus, Ascendant Light | Borealis the Freezing Fog | Caligo, Miasma of
Night | Fulghor, Champion of Nightglow | Gladius, Beast of Night | Gnoster, Wisdom of Night |
Libra, Creature of Night | Maris, Fathom of Night | Heolstor the Nightlord.

Noms correspondant aux Nightfarers jouables (statut NON etabli par le corpus) : Wylder |
Guardian | Ironeye | Raider | Recluse | Duchess | Executor | Revenant.
Objets a nom evocateur, sans description disponible : Primordial Nightlord's Rune | Blade of
Night Fragment | The Shape of Night | Trace of Night | Vestige of Night | Power of Night and
Flame. Le premier pourrait correspondre au Shard evoque par le worldbuilder (V1), mais AUCUNE
description n'existe pour l'etablir. Ne pas conclure.

## Alertes de fin de build

| # | Sujet | Etat |
|---|---|---|
| A1 | BIBLE B1 a 54 847 / 55 000 caracteres : 153 de marge. Tout ajout futur exige une compression prealable. Envisager de deporter SB5 Personnages (11 982 car.) vers des fiches WIKI des que la branche Personnages/ sera peuplee. | SIGNALE |
| A2 | Plusieurs pages sont a moins de 50 caracteres de leur plafond de 10 000. Elles ne peuvent plus rien recevoir sans compression. Les auditeurs ont signale les faits qu'ils ont du renoncer a integrer : ils sont listes dans _Questions_Worldbuilder.md. | SIGNALE |
| A3 | Les 25 pages restent en W1 alors que 5 ont ete corrigees apres la relecture croisee. Incrementer sans reporter au Sommaire creerait un [VERSION DECALEE] : a solder au prochain BIBLE BUILD. | SIGNALE |
| A4 | Attribution des locuteurs de dialogue : le dump indexe par identifiant, sans table vers les noms. Les redacteurs ont parfois attribue une replique par voisinage d'identifiant. Decision de DOCTRINE en attente (cf. _Questions_Worldbuilder.md). | EN ATTENTE |
| A5 | Branches Personnages/, Lieux/, Artefacts/ et Nightreign/ vides par decision (D9 : creation a la demande). Le Sommaire les liste avec 0 page : ce n'est pas un oubli. | NORMAL |

## Trous et alertes

| # | Sujet | Etat |
|---|---|---|
| T1 | Corpus Nightreign : LORE NON CONSTITUABLE en l'etat. Les deux pistes ont ete exploitees le 2026-07-25. Le depot Elden-Ring-Nightreign-Save-Editor publie 8 fichiers .fmg.xml en en_US (GoodsName, NpcName, AntiqueName, AttachEffectName, base et dlc01), soit 3 219 entrees non nulles - mais ZERO entree de plus de 160 caracteres : ce sont des NOMS SEULS. Les fichiers porteurs de texte (Caption, Info, TalkMsg) ne sont pas publies. Archive malgre tout en _Corpus/NR_Names_01.md et NR_Names_02.md : cela etablit l'existence et l'orthographe exacte des entites, rien de plus. Consequence : les 4 axes V1-V4 restent NON SOURCES et aucune page de lore Nightreign n'est redigeable. Il faudrait un dump complet type Carian Archive, qui n'existe pas encore publiquement. | BLOQUE - source manquante |
| T2 | `TalkMsg` indexe par ID de locuteur, pas par nom. Table ID -> PNJ manquante. | OUVERT |
| T3 | Aucune geographie dans le corpus (quel lieu dans quelle region, qui se tient ou). | OUVERT, source d'appoint prevue |
| T4 | Decalage de version des SPEC : les instructions de projet citent `SPEC_BIBLE_LORE_WIKI_v8_3` et `SPEC_CODEX_v8_4` ; le depot ne porte que `v8_2` et `SPEC_CODEX_v8_3`. | SIGNALE AU WORLDBUILDER |
| T6 | Le Sommaire devait rester de TAILLE FIXE. Il est passe de 7 580 a 9 850 caracteres en un lot, par ajout de doctrines (narration visuelle, budget) et de 3 entrees de page. La croissance par doctrine est ponctuelle, celle par page ne l'est pas : 21 pages restantes a environ 150 caracteres l'entree ajouteront environ 3 000 caracteres. Projection : environ 13 000 caracteres a la fin de la carte structurelle. Acceptable, mais a surveiller - si le seuil devient genant, deporter la liste des pages vers les _Index de branche et ne garder au Sommaire que les branches. | SIGNALE |
| T5 | Dans cet environnement, `curl` vers `github.com` est bloque (403). Seul `raw.githubusercontent.com` repond. La methode 2 de l'instruction (blob + parser rawLines) est inutilisable ici ; le listing de dossier passe par l'API jsDelivr. | CONTOURNE |

---

FIN_WIKI__IMPLICATIONS
