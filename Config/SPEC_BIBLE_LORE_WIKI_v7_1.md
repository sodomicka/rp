# SPEC_BIBLE_LORE_WIKI v7.1

Ce fichier definit la forme, les regles de construction et le gabarit du systeme BIBLE_LORE + WIKI + Parties :
- `BIBLE_LORE_{UNIVERS}.md` — index de routage + lore condense, fichier de projet lu en integralite par le MJ.
- WIKI GitHub (`{Univers}/`) — pages .md du monde, consultees par fetch a la demande. Cout zero en contexte tant que non fetchees.
- Parties GitHub (`Parties/{Univers}/Partie<n>/`) — memoire froide du RP, arcs joues, tracking PNJ, CHRONO archivee. Consultees par fetch a la demande. Chaque `<n>` correspond a un RP distinct dans le meme univers.

Le modele doit produire des documents factuels, structures, sans narration, sans interpretation non balisee.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_BIBLE_LORE_WIKI_v7_1.md`.
Consultation : fetchee au premier BIBLE BUILD. Entre deux builds, la BIBLE elle-meme sert de reference — ses sections vides conservent le gabarit de cette spec pour que le MJ n'ait plus a la refetcher.

---

## 1. Role et position hierarchique

La BIBLE_LORE est le point d'entree du systeme de reference lore. Elle contient :
1. Le lore condense de l'univers (§B0-§B8), lisible seul, autosuffisant pour les faits essentiels.
2. Les definitions des fils Tchekhov du RP (§B8), migrees depuis le CODEX.
3. L'index de routage (§B9) vers les pages WIKI et Parties/ pour le detail.

Le WIKI (`{Univers}/`) contient le monde : fiches personnages, chronologie detaillee, roadmaps, power-scaling, lore approfondi.

Les Parties (`Parties/{Univers}/Partie<n>/`) contiennent la memoire froide d'un RP donne : arcs joues, CHRONO archivee, fiches de suivi des PNJ affectes par la narration, fiche protagoniste, decisions et bifurcations prises. Chaque Partie<n> est un RP autonome dans le meme univers.

Hierarchie :
`OOC joueur > CODEX > BIBLE_LORE > WIKI > Canon externe > #SITES_REF > improvisation`

La BIBLE_LORE prime sur le canon externe. Le WIKI prime sur le canon externe mais est ecrase par la BIBLE_LORE en cas de conflit. Le CODEX ne duplique ni la BIBLE ni le WIKI — il ne stocke que l'etat courant et les divergences fraiches.

## 2. Quand utiliser le systeme

Le systeme BIBLE_LORE + WIKI est utilise des que l'univers necessite un socle de lore fiable que le MJ ne peut pas reconstituer de memoire. Le joueur decide en setup si une BIBLE est necessaire.
- Si oui : BIBLE + WIKI portent le lore canon et les divergences etablies. Le CODEX ne stocke que la memoire chaude de session.
- Si non (codex pur) : le MJ se fie a ses connaissances + fetch. Le CODEX porte les divergences et les faits canon critiques.

## 3. Architecture a quatre couches

```
CODEX (vivant, memoire chaude de session)
  |-> BIBLE_LORE (index + lore condense, fichier de projet, lue en entier)
  |     |-> WIKI GitHub {Univers}/ (pages .md du monde, fetch a la demande)
  |     |     |-> {Univers}/Roadmap/ (itineraires par arc, communs a tous les RP)
  |-> Parties/{Univers}/Partie<n>/ (memoire froide d'un RP donne, fetch a la demande)
        |-> Suivi/ (fiches PNJ affectes, protagoniste)
        |-> Archives/ (CHRONO archivee, arcs clos)
        |-> Decisions/ (bifurcations prises dans ce RP)
```

Le CODEX ANNEXE_CHRONO > Arcs pointe vers la page Roadmap concernee via `roadmap: cf. WIKI Roadmap/<page>.md`. La roadmap est commune a tous les RP de l'univers ; les decisions specifiques a un RP sont tracees dans `Parties/{Univers}/Partie<n>/Decisions/`.

### Flux de resolution d'un fait lore
1. CODEX (divergence fraiche du RP ?) -> si oui, utiliser.
2. BIBLE_LORE §B0-§B8 (fait condense ?) -> si oui, utiliser.
3. BIBLE_LORE §B9 -> Sommaire.md (deja en contexte depuis le fetch initial) : identifier la page, puis fetch de la page.
4. Fetch / #SITES_REF (canon externe) -> si hors perimetre BIBLE + WIKI.
5. Invention prudente -> coherente avec les echelons superieurs.

---

## 4. BIBLE_LORE — Principes redactionnels

- Dense > exhaustif. Ligne telegraphique > phrase pleine.
- FOCUS : la bible ne couvre que le PERIMETRE NARRATIF defini par le joueur.
- Pas de narration, pas de prose, pas de metaphores.
- Pas d'adjectifs decoratifs ni de jugements de valeur.
- Phrases > 25 mots interdites.
- Redaction SANS ACCENT (diacritiques retires des lettres ; symboles § et — conserves), meme regle que le CODEX :
  - Allemand : u-trema -> u ; o-trema -> oe ; a-trema -> ae ; eszett -> ss (Ubel, Groesse, Solitaer).
  - Francais : accents retires dans les fichiers ; reaccentues en narration.
  - Japonais / coreen : romanisation ASCII ; kanji et hangul jamais ecrits (romanisation + glose si mot porteur).
- Ingestion : nom fetche en forme accentuee converti en ASCII a l'ecriture, jamais reinjecte accentue. Pour interroger le canon, requeter la forme d'origine accentuee.
- Aucune theorie de fans. Aucune speculation non balisee.

### Niveaux de certitude
Chaque fait porte implicitement le niveau "etabli" sauf balisage contraire :
- `[IMPLICITE]` — fortement implique par le canon mais jamais enonce explicitement.
- `[INTERPRETATION]` — lecture coherente mais debattue ou ambigue. Le joueur tranche en OOC si le RP touche ce point.
- `[INCERTAIN]` — information contradictoire ou insuffisante dans les sources.
- `[DIVERGENCE RP]` — divergence du RP par rapport au canon, formalisee et validee par le joueur.

## 5. BIBLE_LORE — Budget

Plafond dur : 55 000 caracteres.
Contrainte globale : CODEX + BIBLE_LORE <= 100 000 caracteres (seuil RAG des fichiers de projet). Garantie par construction : 55 000 (BIBLE) + 35 000 (CODEX) = 90 000, marge 10 000.
Verification au build : `wc -m` (caracteres, locale UTF-8) sur le fichier genere. Depassement : signaler, proposer des compressions par gain decroissant (caracteres recuperes + ce qu'on perd), le worldbuilder tranche. Compresser, jamais supprimer l'information utile sans validation.

Repartition indicative (guide, pas plafonds rigides par section) :

| Bloc | Fourchette | Role |
|---|---|---|
| §B0 | 1-2k | Metadonnees, wiki_base, parties_base |
| §B1-§B4 | 5-12k | Cosmogonie, lexique, chronologie condensee, factions |
| §B5 | 8-20k | Personnages (syntheses, croissance principale) |
| §B6-§B7 | 2-5k | Lieux, artefacts |
| §B8 | 2-5k | Mysteres ouverts + definitions Tchekhov |
| §B9 | <1k | Pointeur vers {Univers}/Sommaire.md (index detaille hors BIBLE, taille fixe) |
| Journal | 1-3k | — |

Principe directeur : §B1-§B8 contiennent assez pour que le MJ ne soit pas perdu sans fetcher. Le detail vit sur le WIKI et dans Parties/. Si une section (§B2, §B6, §B7) n'apporte pas de contexte ambiant indispensable, elle peut etre allegee et vivre principalement sur le WIKI.

## 6. BIBLE_LORE — Architecture des sections

Fichier unique, lu en integralite par le MJ a chaque tour.
Chaque section a un identifiant stable (`§B0`, `§B1`...).

### BIBLE auto-portante
Les sections pas encore remplies conservent le gabarit de la SPEC (lignes de structure, champs, format). Ainsi le MJ sait quoi remplir au prochain build sans refetcher la SPEC. La BIBLE livree n'a jamais de section vide sans structure.

### Sections (ordre fixe, toutes optionnelles sauf §B0, §B1, §B9)

#### §B0 Metadonnees [OBLIGATOIRE]
- univers :
- focus narratif : <perimetre couvert>
- scope : <petit | moyen | grand>
- sources primaires : <liste>
- date de build : <AAAA-MM-JJ>
- bible_version : B<N>
- wiki_base : <URL racine du WIKI GitHub>
  Format : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
  Toutes les URLs WIKI de §B9 se construisent par concatenation : wiki_base + chemin relatif.
- parties_base : <URL racine de Parties/ GitHub pour le RP en cours>
  Format : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
  Toutes les URLs Parties de §B9 se construisent par concatenation : parties_base + chemin relatif.
- pages wiki rattachees :
  - <Dossier> — <description courte> (<N> pages)

#### §B1 Cosmogonie et regles du monde [OBLIGATOIRE]
Comment le monde fonctionne dans le perimetre du focus.
Inclut les divergences RP formalisees (balisees `[DIVERGENCE RP]`).
- <regle 1>
- <regle 2>

#### §B2 Lexique
`Terme — definition (1 ligne max)`

#### §B3 Chronologie
`Date/Ere | Evenement | Consequence`

Detail des etapes par arc : cf. {Univers}/Roadmap/ (fetch obligatoire en debut de thread pour l'arc en cours).

Notes de cadrage chronologique en fin de §B3 sous `### Notes`.

#### §B4 Factions et groupes
`Faction — nature | objectif | allies | ennemis | statut dans le focus`

#### §B5 Personnages
Personnages canon pertinents au focus + personnages RP.

Contenu AUTORISE :
- identite, role, affiliation, capacites, relations, sort connu ;
- traits comportementaux observables dans les sources ;
- motivations explicitement enoncees ou fortement impliquees ;
- rapport avec le protagoniste (synthese).

Contenu INTERDIT :
- voix (registre, tics verbaux, ton) — ANNEXE_PNJ du CODEX ;
- etat actuel dans le RP — CODEX §4 ;
- interpretation psychologique non fondee.

La frontiere : la BIBLE dit QUI ils sont et CE QU'ILS ONT FAIT. Le CODEX dit COMMENT ils parlent et OU ils en sont.

Format :
`Nom — role | capacites-cle | relations | sort connu | certitude`
Si fiche WIKI ou Parties/ detaillee : `detail: cf. WIKI <page>.md` ou `detail: cf. PARTIES <page>.md`.

#### §B6 Lieux
`Lieu — nature | rattachement | fonction narrative | etat connu`

#### §B7 Artefacts et objets
Objets narrativement significatifs (pas l'inventaire du RP — cf. CODEX ANNEXE_INVENTAIRE).
`Objet — nature | origine | pouvoir/fonction | localisation connue | certitude`

#### §B8 Mysteres ouverts et fils Tchekhov
Deux sous-sections :

##### Mysteres
Questions non resolues, pertinentes au focus. Le MJ doit savoir ce qui est volontairement flou.
`Mystere — hypotheses principales | statut (ouvert / resolu-dans-RP / hors-perimetre)`

##### Tchekhov
Definitions des fils narratifs plantes dans le RP. L'ETAT de chaque fil (ouvert/arme/paye) est dans le CODEX ANNEXE_TCHEKHOV. La BIBLE porte les definitions stables.
`Fil — plante en | condition de detonation | consequence attendue`

#### §B9 Index — routage [OBLIGATOIRE si WIKI present]
§B9 ne contient PAS l'index detaille page-par-page. Cet index vit dans `{Univers}/Sommaire.md` (page WIKI fetchee au debut de chaque thread, cf. section 10), pour que §B9 reste de taille fixe et ne croisse plus avec le nombre de pages.

Contenu de §B9 :
- `Index detaille page-par-page : cf. WIKI {Univers}/Sommaire.md`

Regles de §B9 :
- L'inventaire des dossiers (avec compte de pages) est deja dans §B0 `pages wiki rattachees` — il sert de filet de securite si Sommaire.md tombe (listing direct via la methode dossier de ACCES GITHUB).
- §B1-§B8 portent le resume ambiant : le MJ sait CE QUI EXISTE sans fetch. Sommaire.md dit OU est le detail. La page cible porte le detail.
- Sommaire.md est fetche au debut de chaque thread RP (carte de navigation centrale) et reste en contexte. Fetche tot pour rester saillant (eviter le lost-in-the-middle). Voir section 10.
- Chaque page reste une unite autonome, fetchee en entier. L'URL se construit : `wiki_base` ou `parties_base` (§B0) + `<Dossier>/<Page>.md`.

---

## 7. WIKI — Specification des pages

### Nature
Les pages WIKI sont des fichiers .md heberges sur un depot GitHub public. Chaque page est une unite de consultation autonome, fetchee en entier.

Types de pages possibles :
- Sommaire (index detaille de toutes les pages WIKI et Parties — voir gabarit ci-dessous).
- Chronologie detaillee par ere.
- Fiches personnages approfondies.
- Descriptions de lieux.
- Roadmaps (itineraires par arc, communs a tous les RP de l'univers).
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
2. Ligne de metadonnees minimale (univers, dossier, version).
3. Contenu structure en sections si pertinent.
4. Pas de contenu narratif (sauf pages transcript = verbatim).

### Gabarit Roadmap

Les roadmaps vivent dans `{Univers}/Roadmap/`. Elles decrivent les itineraires possibles par arc, independamment d'un RP specifique. Les decisions prises dans un RP donne sont tracees dans `Parties/{Univers}/Partie<n>/Decisions/`.

```
# Roadmap_<Arc>

- statut : <en cours | a venir | clos>
- version : W<N>

## Conditions de depart
- <prerequis narratif 1>
- <prerequis narratif 2>

## Etapes
| # | Etape | Lieu | PNJ impliques | Tchekhov lies | Condition d'avancement |
|---|---|---|---|---|---|
| 1 | <jalon> | <lieu> | <noms> | <fils> | <declencheur> |

## Bifurcations
- Apres etape <N> : si <condition A> -> <consequence>. Si <condition B> -> <consequence>.

## Conditions de cloture
- <condition de fin d'arc>
- <consequence sur l'univers>

---
FIN_WIKI_ROADMAP_<ARC>
```

### Gabarit Sommaire

`{Univers}/Sommaire.md` porte l'index detaille que §B9 ne porte plus : une entree par page, groupee par dossier. C'est la carte de navigation du WIKI et de Parties/. Fetchee au debut de chaque thread RP. Mise a jour via BIBLE BUILD a chaque ajout de page.

```
# Sommaire — {Univers}

- univers : <univers>
- version : W<N>
- bible rattachee : BIBLE_LORE_{UNIVERS} B<N>

## WIKI

### <Dossier>/
Description : <contenu du dossier en 1 ligne>
- <Page>.md — <description courte du contenu>

### Roadmap/
Description : itineraires par arc, communs a tous les RP de l'univers.
- Roadmap_<Arc>.md — <description courte>

## PARTIES (Partie<n>)

### Suivi/
Description : fiches de suivi des personnages affectes par la narration.
- <Page>.md — <description courte>

### Archives/
Description : chronologie archivee, arcs clos.
- <Page>.md — <description courte>

### Decisions/
Description : bifurcations prises dans ce RP par rapport aux roadmaps.
- Decisions_<Arc>.md — <description courte>

---
FIN_WIKI_SOMMAIRE
```

### Maintenance
Pages WIKI mises a jour via BIBLE BUILD. Statiques entre deux builds.

---

## 8. Parties — Specification

### Nature
Les pages Parties/ sont des fichiers .md heberges sur le meme depot GitHub, dans `Parties/{Univers}/Partie<n>/`. Elles constituent la memoire froide d'un RP donne. Chaque `Partie<n>` est un RP autonome dans le meme univers, ce qui permet de jouer plusieurs RP en parallele avec des bifurcations differentes.

### Structure
```
Parties/{Univers}/
  Partie1/
    Suivi/
      <Protagoniste>_Fiche.md — fiche complete du protagoniste (identite, capacites, backstory)
      <PNJ>_Suivi.md — tracking des PNJ affectes par la narration
    Archives/
      CHRONO_<arc>.md — chronologie archivee d'un arc clos
    Decisions/
      Decisions_<arc>.md — bifurcations prises dans ce RP par rapport a la roadmap
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
- roadmap : cf. WIKI Roadmap/<page>.md

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
- Roadmap de l'arc en cours : fetch obligatoire en debut de thread RP depuis `{Univers}/Roadmap/`.
- Fiches Suivi/ : fetch a la demande quand un PNJ suivi entre en scene.
- Archives/ : fetch exceptionnel (flashback, verification).
- Decisions/ : fetch a la demande pour verifier les choix anterieurs.

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
Au premier BIBLE BUILD (aucune BIBLE existante), le MJ fetche `https://github.com/sodomicka/rp/blob/main/Config/SPEC_BIBLE_LORE_WIKI_v7_1.md`. Si la SPEC n'est pas encore sur le depot (tout premier build, rien n'existe), le joueur la fournit en fichier joint ou dans le chat pour ce premier thread. Apres ce premier build, la SPEC est uploadee dans Config/ et tout passe en fetch.

Pour les builds suivants, la BIBLE elle-meme sert de reference (gabarit integre dans les sections vides). Le fetch de la SPEC n'est necessaire que si le MJ a besoin de verifier une regle de construction.

### Processus — Phase 1 : Genese de la bibliotheque
Si construction collaborative :
1. Inventorier les sources disponibles.
2. Proposer une architecture de WIKI adaptee au RP.
3. Le joueur valide, ajuste ou complete.
4. Pour chaque fait ambigu, le MJ pose la question — le joueur tranche.
5. Construire les pages une par une ou par lot thematique, validation par dossier.
6. La BIBLE_LORE est construite en dernier — elle condense le WIKI et genere §B9.

### Processus — Phase 2 : Construction directe
Si sources completes et plan clair :
1. Lire toutes les sources.
2. Construire les pages WIKI selon le plan.
3. Construire la BIBLE_LORE avec §B9 indexe.
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
  Roadmap/
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
- Theories de fans — sauf validation OOC explicite comme canon local.
- Contenu genere par IA non verifie.
- Novelisations ou adaptations non canoniques.

### Fetch pendant le build
Si le joueur fournit des URL : fetcher et extraire.
Si le joueur fournit des fichiers : lire et extraire.
Le MJ ne fetche PAS de sources supplementaires de sa propre initiative. Trou critique -> `[INCERTAIN]` + suggestion de source en OOC.

---

## 10. Utilisation en narration

### Chargement par tour
1. BIBLE_LORE en entier (§B0-§B9) — obligatoire, c'est l'index.
2. Si la scene necessite un detail non couvert par §B0-§B8 : consulter §B9, identifier la page, construire l'URL, fetch.
3. Chaque page est fetchee en entier — unite autonome.
4. Maximum : 2-3 consultations WIKI/Parties par tour de narration (hors fetch initial de Roadmap).

### Fetch initial de thread
Au debut de chaque thread RP, avant toute narration :
1. Identifier l'arc en cours via CODEX ANNEXE_CHRONO > Arcs.
2. Fetch de {Univers}/Sommaire.md (`wiki_base` + `Sommaire.md`) — carte de navigation, reste en contexte tout le thread. Fetche tot pour rester saillant.
3. Fetch de la page Roadmap de l'arc (`wiki_base` + `Roadmap/<page>.md`) — reste en contexte tout le thread.
4. Si le CODEX §3 renvoie a une fiche dans Parties/ : fetch optionnel de la fiche protagoniste.
5. Narration.

### Gestion des echecs de fetch
- Si fetch echoue (404, timeout, contenu inattendu) : ne JAMAIS improviser silencieusement.
- Signaler en OOC : `[FETCH ECHOUE — <page> — invention prudente ou correction URL requise.]`

### Ce que la BIBLE, le WIKI et Parties/ ne font PAS
- Pas de voix PNJ (ANNEXE_PNJ du CODEX).
- Pas d'etat actuel du RP (CODEX §4).
- Pas de mise a jour pendant le RP. Statiques entre deux builds.

---

## 11. Mise a jour

La BIBLE_LORE, le WIKI et Parties/ sont statiques pendant le RP — pas de mise a jour a chaque CODEX BUILD.
Le joueur peut demander un BIBLE BUILD entre deux sessions pour :
- ajouter des sources ou des pages ;
- formaliser des divergences fraiches (CODEX ANNEXE_LORE -> BIBLE §B1/§B3 ou WIKI) ;
- archiver la CHRONO dans Parties/ ;
- mettre a jour les fiches Suivi/ ;
- enregistrer les decisions dans Decisions/ ;
- corriger des erreurs ;
- reorganiser la structure.

Lors d'un rebuild, le numero de version de la BIBLE incremente (B1 -> B2 -> ...).
Les pages WIKI/Parties modifiees sont re-livrees ; les autres restent intactes.
Le joueur uploade les fichiers mis a jour sur le depot GitHub.

---

## 12. Depot GitHub — Convention

### Structure du depot
```
sodomicka/rp/
  Config/
    SPEC_CODEX_v7_1.md
    SPEC_BIBLE_LORE_WIKI_v7_1.md
  <Univers>/
    <Dossier_thematique>/
      <Page>.md
    Roadmap/
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

# GABARIT DE SORTIE — BIBLE_LORE

# BIBLE_LORE_{UNIVERS}

## Table des matieres
- §B0 Metadonnees
- §B1 Cosmogonie et regles du monde
- §B2 Lexique
- §B3 Chronologie
- §B4 Factions et groupes
- §B5 Personnages
- §B6 Lieux
- §B7 Artefacts et objets
- §B8 Mysteres ouverts et Tchekhov
- §B9 Index du WIKI et des Parties

## §B0 Metadonnees
- univers :
- focus narratif :
- scope : <petit | moyen | grand>
- sources primaires :
- date de build : <AAAA-MM-JJ>
- bible_version : B<N>
- wiki_base : `https://github.com/sodomicka/rp/blob/main/<Univers>/`
- parties_base : `https://github.com/sodomicka/rp/blob/main/Parties/<Univers>/Partie<n>/`
- pages wiki rattachees :
  - <Dossier> — <description courte> (<N> pages)

## §B1 Cosmogonie et regles du monde
- <regle 1>
- <regle 2>

## §B2 Lexique
`Terme — definition (1 ligne max)`

## §B3 Chronologie
| Date/Ere | Evenement | Consequence |
|---|---|---|
| <date> | <evenement> | <consequence> |

Detail des etapes par arc : cf. {Univers}/Roadmap/ (fetch obligatoire en debut de thread pour l'arc en cours).

### Notes
- <note de cadrage>

## §B4 Factions et groupes
`Faction — nature | objectif | allies | ennemis | statut dans le focus`

## §B5 Personnages
`Nom — role | capacites-cle | relations | sort connu | certitude`
Si fiche WIKI ou Parties/ detaillee : `detail: cf. WIKI <page>.md` ou `detail: cf. PARTIES <page>.md`.

## §B6 Lieux
`Lieu — nature | rattachement | fonction narrative | etat connu`

## §B7 Artefacts et objets
`Objet — nature | origine | pouvoir/fonction | localisation connue | certitude`

## §B8 Mysteres ouverts et Tchekhov

### Mysteres
`Mystere — hypotheses principales | statut (ouvert / resolu-dans-RP / hors-perimetre)`

### Tchekhov
`Fil — plante en | condition de detonation | consequence attendue`

## §B9 Index — routage

Index detaille page-par-page : cf. WIKI {Univers}/Sommaire.md
(Inventaire des dossiers : cf. §B0 pages wiki rattachees.)

---

## Journal de version
- B1 — <AAAA-MM-JJ> — creation, WIKI <N> dossiers / <M> pages, budget BIBLE <X> car.
- B<N> — <AAAA-MM-JJ> — <motif>.

FIN_BIBLE_B<N>

---

# GABARIT DE SORTIE — PAGE WIKI / PARTIES

# <Titre de la page>

- univers : <univers>
- dossier : <dossier thematique>
- sources : <sources utilisees>
- version : W<N>
- bible rattachee : BIBLE_LORE_{UNIVERS} B<N>

## <Section 1>
<contenu structure>

## <Section 2>
<contenu structure>

---

FIN_WIKI_{DOSSIER}_{PAGE}
