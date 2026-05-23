# SPEC_CODEX v7.0

Ce fichier definit la forme, les regles de construction et le gabarit du `CODEX_NARRATIF_vX.md`.
Il sert de reference unique en mode CODEX BUILD.
Le modele doit produire un CODEX factuel, compact, autosuffisant, sans narration.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_CODEX_v7_0.md`.
Consultation : fetchee au premier CODEX BUILD d'un thread (V1 sous Instructions Wiki, V2+ sous Instructions RP). Pour les builds suivants dans le meme thread, la version fetchee reste en contexte.

---

## 1. Regles generales
- Le CODEX remplace integralement la version precedente.
- Un fait = un seul emplacement canonique.
- Le CODEX ne cree aucun fait nouveau.
- Il reformule, regroupe et compresse uniquement des informations presentes dans le thread, les fichiers joints et l'eventuel CODEX precedent.
- Si une information est absente, floue ou contradictoire : `[INCERTAIN]`.
- Le CODEX est redige SANS ACCENT.
- Noms accentues : preciser une fois la forme canonique si utile, puis garder la forme sans accent.
- Le CODEX est un fichier unique structure en CORE + 7 ANNEXES balisees. Ce n'est PAS une collection de fichiers separes.

## 2. Principe redactionnel
- Dense > exhaustif.
- Ligne telegraphique > phrase pleine.
- Renvoi court autorise : `cf. [ANNEXE_X]`, `cf. BIBLE §BX`, `cf. WIKI <dossier>/<page>.md`, `cf. PARTIES <dossier>/<page>.md`.
- Pas de redites entre sections.
- Pas d'adjectifs decoratifs.
- Pas d'exemples illustratifs.
- Pas de justifications.
- Pas de prose hors ANNEXE_STYLE.
- NE STOCKER QUE LA MEMOIRE CHAUDE DE SESSION. Le CODEX porte l'etat actuel du RP, les PNJ en scene, les decisions OOC et les divergences fraiches non encore formalisees. Le lore statique, les fiches personnages, les roadmaps et le power-scaling vivent dans la BIBLE et le WIKI.
- Si une BIBLE_LORE est presente : renvoyer a `cf. BIBLE §BX` ou `cf. WIKI <dossier>/<page>.md` pour tout fait deja couvert.
- Si un fait issu du RP est formalise dans Parties/ : renvoyer a `cf. PARTIES <dossier>/<page>.md`.

## 3. Budget lineaire

### Formule
`B(N) = min(10000 + 360 * (N - 1), 35000)`
- N = numero de version du CODEX.
- Plafond dur : 35 000 caracteres.
- B(1) = 10 000.
- Plafond atteint a V70. Au-dela : compresser, jamais supprimer l'information utile.
- Contrainte globale : CODEX + BIBLE_LORE <= 100 000 caracteres (seuil RAG empirique des fichiers de projet).

### Table rapide

| V | Budget |
|---|---|
| V1 | 10 000 |
| V5 | 11 440 |
| V10 | 13 240 |
| V20 | 16 840 |
| V30 | 20 440 |
| V50 | 27 640 |
| V70 | 34 840 |
| V70+ | 35 000 |

### Repartition budgetaire

Sections stables (plafonds fixes) :
- CORE (§1, §2, §3 pointeur, §4, §5, §6, §7, §8) : max 7 000 caracteres.
- ANNEXE_STYLE : max 2 000 caracteres.
- ANNEXE_LORE (buffer divergences fraiches) : max 1 000 caracteres.
- Total stable : max 10 000 caracteres.

Sections cumulatives (solde = B(N) - stable) :
- ANNEXE_PNJ + ANNEXE_CHRONO + ANNEXE_INVENTAIRE + ANNEXE_TCHEKHOV + ANNEXE_SAVOIRS.
- Repartition libre entre elles selon les besoins du RP.

Signal d'archivage :
- Quand le CODEX depasse 80% de B(N) : le MJ signale en OOC `[ARCHIVAGE SUGGERE — CODEX a X% de B(N). Compresser CHRONO et/ou archiver dans Parties/.]`
- Le joueur decide. Le MJ ne force pas.

## 4. Regle d'unicite des faits
Chaque fait n'apparait qu'une seule fois dans tout le systeme. Emplacement canonique :

### Dans le CODEX
- Etat courant du protagoniste (position, blessures, ressources) -> CORE §3
- Reprise et etat courant -> CORE §4
- Regles d'Or -> CORE §5
- OOC ecrasant le canon -> CORE §6
- Interdits accumules -> CORE §7
- Sources web -> CORE §8
- Voix, statut, derniere action des PNJ en scene -> ANNEXE_PNJ
- Divergences fraiches non encore formalisees -> ANNEXE_LORE
- Evenements de la session courante, arcs -> ANNEXE_CHRONO
- Objets en jeu -> ANNEXE_INVENTAIRE
- Etat des fils Tchekhov (statut + derniere interaction) -> ANNEXE_TCHEKHOV
- Style -> ANNEXE_STYLE
- Qui sait quoi maintenant -> ANNEXE_SAVOIRS

### Hors du CODEX
- Identite, capacites, limites, backstory du protagoniste -> WIKI (Parties/) — le CODEX §3 ne garde qu'un pointeur + etat courant
- Definitions des fils Tchekhov (condition, consequence) -> BIBLE §B8 ou WIKI
- Lore canon dans le perimetre du focus -> BIBLE / WIKI
- Divergences lore etablies et formalisees -> BIBLE §B1/§B3 ou WIKI
- Power-scaling -> WIKI
- Roadmaps -> WIKI ({Univers}/Roadmap/)
- Fiches personnages -> WIKI
- Arcs joues, CHRONO archivee -> Parties/
- Decisions et bifurcations prises -> Parties/ (Decisions/)

## 4bis. Filtrage au build
- Doublon avec canon accessible via #SITES_REF et non modifie par le RP -> rejet. Si le fetch echoue au moment du build, conserver le fait avec `[FETCH INDISPONIBLE]`.
- Fait deja present dans BIBLE, WIKI ou Parties/ -> rejet (renvoyer via `cf.`).
- Doublon interne inter-sections -> rejet.
- Erreur corrigee en scene sans trou CODEX -> rejet.
- OOC emotionnel sans contenu factuel -> rejet.
- Ligne derivee d'un invariant deja ecrit -> rejet.
- Silence revele par erreur joueur -> integration CORE §3 etat ou ANNEXE_PNJ voix.
- Evenement clos sans consequence -> compression ANNEXE_CHRONO archive.
- Divergence lore formalisee dans la BIBLE lors d'un BIBLE BUILD -> suppression de l'ANNEXE_LORE, renvoi `cf. BIBLE`.

## 4ter. Triage au build RP
En fin de thread RP, le CODEX BUILD inclut une etape de triage :
1. Identifier les faits, PNJ, arcs et CHRONO qui ne sont plus pertinents pour l'arc a venir.
2. Les exporter en fichiers .md separes (archivage dans Parties/).
3. Les indexer dans le CODEX via pointeur (`cf. PARTIES <dossier>/<page>.md`) pour fetch futur si redevenu pertinent.
4. Consulter la roadmap de l'arc a venir pour orienter le CODEX vers la suite.
5. Le CODEX resultant est autosuffisant sur la continuite (ou on en est, ou on va) mais renvoie a BIBLE/WIKI/Parties pour le lore et le passe.

## 5. Architecture modulaire

### Sections obligatoires (lues a chaque tour de narration)
- `[CORE — LECTURE OBLIGATOIRE]`
- `[ANNEXE_STYLE — LECTURE OBLIGATOIRE]`

### Sections conditionnelles (lues selon la scene)
- `[ANNEXE_PNJ — si PNJ en scene ou convoque]`
- `[ANNEXE_LORE — buffer divergences fraiches, vide = sain]`
- `[ANNEXE_CHRONO — si continuite temporelle]`
- `[ANNEXE_INVENTAIRE — si objet en jeu]`
- `[ANNEXE_TCHEKHOV — si fil narratif touche ou plantable]`
- `[ANNEXE_SAVOIRS — si secret, revelation ou asymetrie]`

### Compression chronologique progressive (ANNEXE_CHRONO)
- Thread courant : un T par battement.
- Thread N-1 : un T par scene majeure.
- Threads anterieurs : un T par arc resolu.
- Arcs clos sans consequence ouverte : fusion en ligne narrative unique.
- Quand ANNEXE_CHRONO depasse 12 000 caracteres : archiver les threads anciens dans Parties/, ne garder que les arcs resolus en une ligne.

## 6. Interdictions de forme
- Aucun paragraphe explicatif hors ANNEXE_STYLE.
- Aucune narration.
- Aucune metaphore.
- Aucun micro-geste.
- Aucun dialogue.
- Aucune liste imbriquee au-dela d'un niveau.
- Phrases > 20 mots interdites hors ANNEXE_STYLE.
- Aucune recopie inter-sections.
- Aucune recopie de canon, de BIBLE ou de WIKI non modifie par le RP.

## 7. Audit de compression
Avant de livrer le CODEX, verifier silencieusement :
1. Chaque fait n'apparait qu'une fois dans tout le systeme (CODEX + BIBLE + WIKI + Parties).
2. Le budget B(N) est respecte, repartition stable/cumulatif respectee.
3. Les sections ne se repetent pas.
4. Le texte reste exploitable sans thread externe.
5. Tout doute est marque `[INCERTAIN]`.
6. Chaque PNJ actif a un champ voix defini ou `voix: [INCERTAIN]`.
7. Le protagoniste a une nature corporelle explicite et une regle de perception par PNJ dans §3.
8. Les regles de filtrage §4bis et §4ter ont ete appliquees.
9. Aucun fait couvert par la BIBLE, le WIKI ou Parties/ n'a ete duplique.
10. ANNEXE_SAVOIRS coherente avec ANNEXE_PNJ et CORE §4.
11. ANNEXE_LORE ne contient que des divergences fraiches (< 1000 chars). Si elle deborde, formaliser dans la BIBLE via BIBLE BUILD.

---

# GABARIT DE SORTIE

# CODEX_NARRATIF_v<N>

## [CORE — LECTURE OBLIGATOIRE]

### §1 Metadonnees
- titre: <titre de la campagne>
- univers: <nom / type>
- regime: canonique | divergence | hybride
- protagoniste: <nom>
- date in-world de reprise: <date>
- date reelle de derniere mise a jour: <AAAA-MM-JJ>
- codex_version: V<N>
- budget: B(<N>) = <valeur> car.
- bible_lore: <nom du fichier BIBLE_LORE si presente, sinon "aucune">
- wiki_base: <URL racine du WIKI GitHub si present, sinon "aucun">
- parties_base: <URL racine de Parties/<Univers>/Partie<n>/ si present, sinon "aucun">

### §2 Premisse
- <ligne 1>
- <ligne 2>
- <ligne 3>
- <ligne 4>
- <ligne 5>

### §3 Protagoniste — etat courant
Fiche complete : cf. WIKI ou Parties/ <dossier>/<fiche>.md

- Nom / alias :
- Nature corporelle : <corps propre | conscience hote | possession | symbiote | autre>
- Perception par PNJ : <qui percoit, comment, limites>
- Etat physique actuel : <blessures, fatigue, marques>
- Etat emotionnel actuel : <en 1 ligne>
- Ressources actuelles : <objets, allies, mana, etc.>
- Contraintes actives : <sceaux, maledictions, limitations temporaires>
- Valeurs inviolables : <rappel compact>
- Tics / voix : <rappel compact>

### §4 Reprise et etat courant
- Lieu :
- Sous-lieu :
- Dernier [REPERE] :
- PNJ presents physiquement :
- Savoir du protagoniste :
- Savoir cache :
- Tension dominante :
- Rapport de force :
- Dernieres paroles echangees : <citation joueur + PNJ>
- Derniere parole / action PNJ : <citation exacte>
- Derniere parole / action joueur : <citation exacte>
- Etat-cle minimal :
- Prochaine bascule amorcee :

### §5 Regles d'Or
1. CODEX = loi, prime sur canon externe. OOC > CODEX > BIBLE_LORE > WIKI > Canon externe > #SITES_REF > invention.
2. Un fait = un emplacement dans tout le systeme.
3. Doute -> [INCERTAIN], jamais invention.
4. PNJ sans voix etablie = muet par defaut.
5. Invariants protagoniste inviolables : nature corporelle, perception par PNJ (cf. fiche WIKI/Parties).

### §6 OOC actifs
- `[AAAA-MM-JJ] — <enonce ecrasant le CODEX ou le canon> | sections impactees`

### §7 Interdits accumules
Pieges identifies en session, non reintroduits dans les CODEX suivants.
- `[AAAA-MM-JJ] — <interdit 1>`

### §8 #SITES_REF
| Source | URL | Usage |
|---|---|---|
| <nom> | <url> | <quand consulter> |

---

## [ANNEXE_PNJ — si PNJ en scene ou convoque]

Ne stocker que ce qui diverge du canon ou est specifique au RP.
Pour le canon non modifie, renvoyer a BIBLE, WIKI ou Parties/.

Champ voix obligatoire pour chaque PNJ actif :
- `voix: muet par defaut`
- `voix: sobre, monosyllabique`
- `voix: lyrique, archaique`
- `voix: <description situee>`
- `voix: [INCERTAIN] — ordre OOC requis avant dialogue`

### Actifs
- <PNJ> — <role> | <statut> | <voix> | <relation au protagoniste> | <derniere action> | <inviolable>

### Secondaires
- <PNJ> — <role> | <voix> | <relation> | <inviolable>

### Absents / morts
- <nom>, <nom>, <nom>

---

## [ANNEXE_LORE — buffer divergences fraiches]

Divergences du RP apparues en session, pas encore formalisees dans la BIBLE ou le WIKI.
Max 1 000 caracteres. Si debordement : declencher BIBLE BUILD pour formaliser.
Vide = sain.

- <divergence 1>
- <divergence 2>

---

## [ANNEXE_CHRONO — si continuite temporelle]

`Date reelle | Date in-world | Compteur | Evenement condense`

### Thread courant (un T par battement)
- <date> | <date IW> | T1 | <evenement>
- <date> | <date IW> | T2 | <evenement>

### Thread N-1 (un T par scene majeure)
- <scene majeure>

### Threads anterieurs (un T par arc resolu)
- <arc resolu>

### Arcs
`Arc — enjeu | jalon courant | prochain jalon | statut | roadmap: cf. WIKI Roadmap/<page>.md`
- <arc> — <enjeu> | <jalon> | <prochain> | <ouvert/suspendu/clos> | roadmap: cf. WIKI Roadmap/<page>.md

---

## [ANNEXE_INVENTAIRE — si objet en jeu]

`Objet — localisation | etat | porteur | signification narrative`
- <objet> — <localisation> | <etat> | <porteur> | <signification>

---

## [ANNEXE_TCHEKHOV — si fil narratif touche ou plantable]

Etat des fils uniquement. Definitions (condition, consequence) : cf. BIBLE §B8.

`Fil — statut | derniere interaction`
- <fil 1> — ouvert | <derniere scene/thread ou le fil a ete touche>
- <fil 2> — arme | <idem>
- <fil 3> — paye | <resolution en 1 ligne>

---

## [ANNEXE_STYLE — LECTURE OBLIGATOIRE]

<Paragraphe 1 : voix narrative, rythme dominant.>

<Paragraphe 2 : sensorialite privilegiee, images autorisees, densite.>

<Paragraphe 3 : traitement des dialogues, silences, tension de fin.>

---

## [ANNEXE_SAVOIRS — si secret, revelation ou asymetrie]

Matrice d'information : qui sait quoi MAINTENANT dans le RP.

`Secret — qui sait | qui ne sait pas | condition de revelation | consequence si revele`
- <secret 1> — <sachants> | <ignorants> | <condition> | <consequence>

### Ironie dramatique active
- <situation> : <ce que le joueur sait mais pas le PNJ X>

---

## Journal de version
- V1 — <AAAA-MM-JJ> — creation, B(1) = 10000, budget 10000 car.
- V<N> — <AAAA-MM-JJ> — <motif>, budget B(<N>) car.

FIN_CODEX_V<N>
