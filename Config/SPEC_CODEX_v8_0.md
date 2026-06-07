# SPEC_CODEX v8.0

<!-- rev. v8.0 (changements majeurs et exhaustifs) : section Capacites dediee §3a (anti-boucle) ; §3a/§3b invariants/courant + description physique + resume de backstory ; regle de promotion ; test de saillance ; decouplage des versions (pointeur souple) ; frontiere univers/partie (instance jouee -> CODEX+Parties ; entite -> BIBLE/WIKI si lore). Le 7.x etait un stress-test ; le 8.0 acte ces invariants. -->

Ce fichier definit la forme, les regles de construction et le gabarit du `CODEX_NARRATIF_vX.md`.
Il sert de reference unique en mode CODEX BUILD.
Le modele doit produire un CODEX factuel, compact, autosuffisant, sans narration.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_CODEX_v8_0.md`.
Consultation : fetchee au premier CODEX BUILD d'un thread (V1 sous Instructions Wiki, V2+ sous Instructions RP). Pour les builds suivants dans le meme thread, la version fetchee reste en contexte. Elle porte le process que le CODEX V(N-1) ne contient pas.

---

## 1. Regles generales
- Le CODEX remplace integralement la version precedente.
- Un fait = un seul emplacement canonique.
- Le CODEX ne cree aucun fait nouveau.
- Il reformule, regroupe et compresse uniquement des informations presentes dans le thread, les fichiers joints et l'eventuel CODEX precedent.
- Si une information est absente, floue ou contradictoire : `[INCERTAIN]`.
- Le CODEX est redige SANS ACCENT (diacritiques retires des lettres ; symboles § et — conserves).
- Diacritiques : translitteration ASCII fixe, jamais suppression brute (le caractere accentue disparait au transfert mobile ; l'ASCII survit).
  - Allemand : u-trema -> u ; o-trema -> oe ; a-trema -> ae ; eszett -> ss (ex. Ubung, schoen, Maedchen, Strasse).
  - Francais : accents retires dans les fichiers ; reaccentues en narration (cf. instructions).
  - Japonais / coreen : romanisation ASCII (Hepburn sans macron ; romanisation revisee). Kanji et hangul jamais ecrits : romanisation + glose du sens si mot porteur, pas un nom propre.
- Ingestion : un nom fetche en forme accentuee est converti en ASCII a l'ecriture, jamais reinjecte accentue dans un fichier ni la narration. Pour interroger le canon, requeter la forme d'origine accentuee (meilleur rappel).
- Le CODEX est un fichier unique structure en CORE + 7 ANNEXES balisees. Ce n'est PAS une collection de fichiers separes (mais le BUILD produit aussi, a cote, la memoire refroidie et le Tn — cf. 4ter).
- VERSIONNAGE DES TAMPONS : les OOC actifs (§5) et interdits accumules (§6) sont tamponnes par version de CODEX `[V<n>]`, jamais par date. V<n> = la version du CODEX sous laquelle l'entree a ete posee. Le champ "date reelle de derniere mise a jour" des metadonnees garde une date calendaire (tracabilite du build), mais aucune entree interne n'est datee.
- DECOUPLAGE DES VERSIONS : aucune epingle de version croisee entre fichiers (ni CODEX<->BIBLE, ni fiches<->CODEX). Seule trace de version externe autorisee : un reperage advisory `dernier sync BIBLE: B<x>` dans les metadonnees (§1) du CODEX, NON bloquant - simple canari signalant un CODEX builde sur une BIBLE ancienne. Pas de mention de version dans `bible_lore`. Les tampons internes restent `[V<n>]`.

## 2. Principe redactionnel
- Dense > exhaustif.
- Ligne telegraphique > phrase pleine.
- Renvoi court autorise : `cf. [ANNEXE_X]`, `cf. BIBLE §BX`, `cf. WIKI <dossier>/<page>.md`, `cf. PARTIES <dossier>/<page>.md`.
- Pas de redites entre sections.
- Pas d'adjectifs decoratifs.
- Pas d'exemples illustratifs.
- Pas de justifications.
- Pas de prose hors ANNEXE_STYLE.
- MEMOIRE CHAUDE DE SESSION + ANCRES STABLES DU PROTAGONISTE. Le CODEX porte l'etat actuel du RP, les PNJ en scene, les decisions OOC, les divergences fraiches non formalisees ET le ledger de capacites stables du protagoniste (section dediee §3). Le CODEX doit rester AUTO-SUFFISANT : il fonctionne meme sans BIBLE ni WIKI.
- UNIVERSALITE : la BIBLE et le WIKI sont OPTIONNELS. S'ils existent, le lore statique volumineux (backstory, roadmaps, power-scaling, fiches PNJ) y vit et le CODEX y renvoie. S'ils n'existent pas, ce qui est indispensable a la continuite (dont les capacites du PJ) vit dans le CODEX. L'offload est conditionnel, jamais une obligation.
- Si une BIBLE_LORE est presente : renvoyer a `cf. BIBLE §BX` ou `cf. WIKI <dossier>/<page>.md` pour tout fait deja couvert - mais UNIQUEMENT si la cible contient reellement le detail (anti-boucle : un renvoi ne pointe jamais vers un autre renvoi).
- Si un fait issu du RP est formalise dans Parties/ : renvoyer a `cf. PARTIES <dossier>/<page>.md`.

## 3. Budget

### Plafond
- Plafond dur : CODEX <= 35 000 caracteres.
- Contrainte globale : CODEX + BIBLE_LORE <= 100 000 caracteres (seuil RAG des fichiers de projet). Garantie par construction : 35 000 (CODEX) + 55 000 (BIBLE) = 90 000, marge 10 000.
- Verification au build : `wc -m` (caracteres, locale UTF-8) sur le fichier genere.
- Depassement : signaler, proposer des compressions par gain decroissant (caracteres recuperes + ce qu'on perd), le joueur tranche. Compresser, jamais supprimer l'information utile sans validation.

### Repartition

Sections stables (plafonds fixes) :
- CORE (§1, §2, §3 pointeur, §4, §5, §6, §7) : max 7 000 caracteres.
- ANNEXE_STYLE : max 2 000 caracteres.
- ANNEXE_LORE (buffer divergences fraiches) : max 1 000 caracteres.
- Total stable : max 10 000 caracteres.

Sections cumulatives (solde = 25 000 caracteres) :
- ANNEXE_PNJ + ANNEXE_CHRONO + ANNEXE_INVENTAIRE + ANNEXE_TCHEKHOV + ANNEXE_SAVOIRS.
- Repartition libre entre elles selon les besoins du RP.

### Signal d'archivage
- Quand le CODEX depasse 80% du plafond (28 000 caracteres) : le MJ signale en OOC `[ARCHIVAGE SUGGERE — CODEX a X% du plafond. Compresser CHRONO et/ou archiver dans Parties/.]`
- Le joueur decide. Le MJ ne force pas.

## 4. Regle d'unicite des faits
Chaque fait n'apparait qu'une seule fois dans tout le systeme. Emplacement canonique :

### Dans le CODEX
- Etat courant du protagoniste (position, blessures, ressources du moment) -> CORE §3b (etat courant)
- Capacites stables + description physique + resume de backstory du protagoniste -> CORE §3a (chaud, ancre)
- Reprise et etat courant -> CORE §4
- OOC ecrasant le canon -> CORE §5
- Interdits accumules -> CORE §6
- Sources web -> CORE §7
- Voix, statut, derniere action des PNJ en scene -> ANNEXE_PNJ
- Divergences fraiches non encore formalisees -> ANNEXE_LORE
- Evenements de la session courante, arcs -> ANNEXE_CHRONO
- Objets en jeu -> ANNEXE_INVENTAIRE
- Etat des fils Tchekhov (statut + derniere interaction) -> ANNEXE_TCHEKHOV
- Style -> ANNEXE_STYLE
- Qui sait quoi maintenant -> ANNEXE_SAVOIRS

### Hors du CODEX
- Backstory COMPLETE du protagoniste -> Parties/Suivi/<Nom>_Fiche.md (froid, fetch a la demande). Le CODEX §3a en porte le RESUME chaud. L'INSTANCE jouee (etat, capacites, description) vit dans le CODEX §3, pas dans la BIBLE/WIKI. Mais l'ENTITE, si elle existe hors de la partie (canon ou OC promu au lore), peut y etre decrite neutrement - cf. regle de placement (SPEC_BIBLE). Renvois `cf.` a sens unique, jamais de boucle.
- Definitions des fils Tchekhov (condition, consequence) -> BIBLE §B8 ou WIKI
- Lore canon dans le perimetre du focus -> BIBLE / WIKI
- Divergences lore etablies et formalisees -> BIBLE §B1/§B3 ou WIKI
- Power-scaling -> WIKI
- Roadmaps -> WIKI ({Univers}/Roadmap/<Prota>/)
- Fiches personnages -> WIKI
- Arcs joues, CHRONO archivee -> Parties/
- Decisions et bifurcations prises -> Parties/ (Decisions/)
- Regles d'Or, hierarchie des sources, interdits generiques -> Instructions RP/Wiki (lues a chaque tour, jamais dupliquees dans le CODEX)

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
- TEST DE SAILLANCE (critere de CONSERVATION, pas seulement de rejet) : un fait reste dans le CODEX seulement s'il (a) affecte l'etat courant du protagoniste, (b) est un Tchekhov vivant ou armable, (c) est une divergence fraiche non formalisee, (d) porte la continuite du prochain battement, ou (e) est une capacite stable du protagoniste. Sinon : couleur narrative -> Tn (livrable 3, archive joueur) ; detail clos sans portee -> coupe. La couleur ne se perd pas, elle descend dans Tn ; elle n'encombre pas le CODEX.
- PROMOTION : toute capacite ou tout fait DURABLE demontre en jeu et absent du calque stable -> promu dans la section Capacites du CODEX (§3a) ; si une BIBLE/WIKI sert de calque lore au RP, monter aussi via BIBLE/WIKI BUILD et pointer dessus. Jamais laisser une capacite durable en memoire transitoire re-derivable a chaque thread. Cette regle prime sur la doctrine "memoire chaude".

## 4ter. Sortie de build RP (TROIS LIVRABLES OBLIGATOIRES)
Tout CODEX BUILD de fin de thread RP produit SYSTEMATIQUEMENT trois fichiers. Aucun n'est conditionnel.

1. CODEX_NARRATIF_vN.md — la memoire CHAUDE. Ecrase la version precedente. Etat courant, PNJ en scene, divergences fraiches, Tchekhov (etat), CHRONO de session. Autosuffisant sur la continuite (ou on en est, ou on va), renvoie a BIBLE/WIKI/Parties pour le lore et le passe.

2. La memoire REFROIDIE — fichiers .md dans Parties/ pour ce qui sort durablement de scene a l'arc a venir (PNJ qui disparaissent, factions dissoutes, lieux quittes, arcs clos). Exemple type : une faction ou un groupe de PNJ qui sort durablement de scene. Indexes dans le CODEX via pointeur `cf. PARTIES <dossier>/<page>.md`. Un fichier par entite ou groupe coherent qui refroidit ; on ECRASE si l'entite refroidit davantage, on n'empile pas. Si rien ne refroidit a ce build, produire une note explicite "memoire refroidie : rien a sortir ce thread" (le livrable existe, meme vide).

3. Tn — l'archive NARRATIVE du thread, destinee surtout au joueur. Recit condense des battements joues (un fichier FIGE par thread, jamais reecrit). Nommage : `T<n>_<arc>.md` dans Parties/<Univers>/Partie<p>/Suivi/. Empile (T1, T2, T3...). Indexe dans le CODEX ANNEXE_CHRONO via `cf. PARTIES Suivi/T<n>_<arc>.md`.

Procedure de triage (alimente les livrables 2 et 3) :
a. Identifier les faits, PNJ, arcs et CHRONO qui ne sont plus pertinents pour l'arc a venir -> memoire refroidie (livrable 2).
b. Condenser les battements du thread -> Tn (livrable 3).
c. Consulter la roadmap de l'arc a venir pour orienter le CODEX (livrable 1) vers la suite.

Convention de nommage Parties/ :
- Archives de thread : `Suivi/T<n>_<arc>.md` (FIGEES, empilees).
- Memoire refroidie thematique : `Suivi/<sujet>.md` ou sous-dossier dedie (ECRASEE quand le sujet refroidit davantage).
- Fiche protagoniste : HORS PERIMETRE du CODEX build. L'etat chaud (capacites, description, etat) vit dans le CODEX CORE §3. La backstory FROIDE vit en `Suivi/<Nom>_Fiche.md`, creee au V1 et maintenue via BIBLE BUILD - le CODEX build ne la produit ni ne la touche.

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
- Aucune recopie de canon, de BIBLE, de WIKI ou d'instruction non modifie par le RP.

## 7. Audit de compression
Avant de livrer le CODEX, verifier silencieusement :
1. Chaque fait n'apparait qu'une fois dans tout le systeme (CODEX + BIBLE + WIKI + Parties + instructions).
2. Le plafond 35 000 car est respecte, repartition stable/cumulatif respectee.
3. Les sections ne se repetent pas.
4. Le texte reste exploitable sans thread externe.
5. Tout doute est marque `[INCERTAIN]`.
6. Chaque PNJ actif a un champ voix defini ou `voix: [INCERTAIN]`.
7. Le protagoniste a une nature corporelle explicite et une regle de perception par PNJ dans §3.
8. Les regles de filtrage §4bis et §4ter ont ete appliquees.
9. Aucun fait couvert par la BIBLE, le WIKI, Parties/ ou les instructions n'a ete duplique.
10. ANNEXE_SAVOIRS coherente avec ANNEXE_PNJ et CORE §4.
11. ANNEXE_LORE ne contient que des divergences fraiches (< 1000 chars). Si elle deborde, formaliser dans la BIBLE via BIBLE BUILD.
12. Aucun pointeur circulaire : chaque `cf.` mene a un emplacement qui CONTIENT le fait, jamais a un autre renvoi (verif specifique : §3a Capacites ne renvoie a BIBLE/WIKI que si la cible porte le detail).
13. Capacites stables du protagoniste ancrees en §3a ; aucune capacite durable laissee uniquement en etat transitoire (§3b) ou en memoire eparse. Test de saillance (4bis) applique : la couleur narrative est descendue en Tn, pas conservee dans le CODEX.

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
  note: les tampons OOC (§5) et interdits (§6) utilisent [V<n>], pas la date.
- codex_version: V<N>
- plafond: 35 000 car.
- bible_lore: <nom du fichier BIBLE_LORE si presente, sinon "aucune"> (sans numero de version)
- dernier sync BIBLE: <B<x> si BIBLE presente, advisory non bloquant ; sinon "n/a">
- wiki_base: <URL racine du WIKI GitHub si present, sinon "aucun">
- parties_base: <URL racine de Parties/<Univers>/Partie<n>/ si present, sinon "aucun">

### §2 Premisse
- <ligne 1>
- <ligne 2>
- <ligne 3>
- <ligne 4>
- <ligne 5>

### §3 Protagoniste
Source vivante de l'INSTANCE jouee : ICI (CODEX) + Parties/Suivi pour la backstory froide. L'instance ne vit pas dans la BIBLE/WIKI ; mais l'ENTITE, si elle est du lore (canon ou OC promu), y est decrite a part - cf. SPEC_BIBLE. Capacites ANCREES en §3a (jamais re-derivees).

**§3a Invariants (chaud, stables, changent rarement)**
- Nom / alias :
- Nature corporelle : <corps propre | conscience hote | possession | symbiote | autre>
- Perception par PNJ : <qui percoit, comment, limites>
- Description physique : <apparence stable : silhouette, traits, signes distinctifs. PAS l'etat du moment (-> §3b)>
- Capacites stables : <pouvoirs durables, ANCRE canonique. Detail complet ici. Toute capacite durable demontree en jeu est promue ici - cf. 4bis>
- Resume de backstory : <quelques lignes denses, contexte suffisant pour narrer. Backstory complete = Parties/Suivi (froid, fetch a la demande)>
- Valeurs inviolables : <rappel compact>
- Tics / voix : <rappel compact>

**§3b Etat courant (chaud, transitoire, churn par thread)**
- Etat physique actuel : <blessures, fatigue, marques du moment>
- Etat emotionnel actuel : <en 1 ligne>
- Ressources du moment : <objets ponctuels, allies presents, munitions, mana disponible>
- Contraintes actives : <sceaux, maledictions, limitations temporaires>

### §4 Reprise et etat courant
- Lieu :
- Sous-lieu :
- Dernier [REPERE] :
- PNJ presents physiquement :
- Savoir du protagoniste :
- Savoir cache :
- Tension dominante :
- Rapport de force :
- Dernier echange — joueur : <citation exacte> / PNJ : <citation exacte>
- Etat-cle minimal :
- Prochaine bascule amorcee :

### §5 OOC actifs
- `[V<n>] — <enonce ecrasant le CODEX ou le canon> | sections impactees`  (V<n> = version du CODEX sous laquelle le thread a ete joue ; remplace l'ancien tampon date)

### §6 Interdits accumules
Pieges identifies en session, non reintroduits dans les CODEX suivants.
- `[V<n>] — <interdit 1>`

### §7 #SITES_REF
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
`Arc — enjeu | jalon courant | prochain jalon | statut | roadmap: cf. WIKI Roadmap/<Prota>/<page>.md`
- <arc> — <enjeu> | <jalon> | <prochain> | <ouvert/suspendu/clos> | roadmap: cf. WIKI Roadmap/<Prota>/<page>.md

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

FIN_CODEX_V<N>
