# SPEC_CODEX v8.2

<!-- rev. v8.0 (changements majeurs et exhaustifs) : section Capacites dediee S3a (anti-boucle) ; S3a/S3b invariants/courant + description physique + resume de backstory ; regle de promotion ; test de saillance ; decouplage des versions (pointeur souple) ; frontiere univers/partie (instance jouee -> CODEX+Parties ; entite -> BIBLE/WIKI si lore). Le 7.x etait un stress-test ; le 8.0 acte ces invariants. -->
<!-- rev. v8.1 : ASCII total (S-notation, fin de l'exemption signe-section/cadratin) ; metadonnee taille au build (le signal d'archivage devient une lecture, plus une estimation) ; livrable 3 renomme Memoire_{Univers}_<n> (destine au joueur, hors repo, hors budget, aucun cf.) ; index Refroidi PERMANENT dans ANNEXE_CHRONO (substitut du Sommaire pour Parties/ entre deux BIBLE BUILDs) ; audit 1 rescope aux sources en contexte ; arbitrage promotion vs unicite ; purge des interdits inertes (S6) ; CORE porte a 8 000 (S3a n'est plus un pointeur) ; retrait du vestige 'V2+ sous Instructions RP' ; collision T<n> resolue (Tour n en CHRONO). -->
<!-- rev. v8.2 (chantier archi) : ANNEXE_CHRONO porte (1) l'ETAT D'ARC courant (jalon courant + prochain jalon) avec renvoi fiche_arc: cf. WIKI Fiches_Arc/<Prota>/<page>.md ; (2) le FIL DES ARCS - suite ordonnee des arcs traverses (memoire longue / anti-amnesie : en jeu on ne lit ni la grosse BIBLE ni les roadmaps, donc ce fil + Parties/Archives sont le substitut de memoire). La fiche d'arc est une mini-bible autosuffisante, document de jeu permanent (buildee au WIKI BUILD, fetchee une fois a l'ouverture, tronquee a la frontiere) : le CODEX y renvoie, il ne la regenere pas. Le renvoi roadmap: est marque (build) : source de creation des fiches, JAMAIS fetche en narration (futur de la saga -> risque de prefiguration). Aligne sur Instructions RP v8.2 (S4 : fiche d'arc a l'ouverture, plus de fetch roadmap en jeu, fetch live sur trou objectif seulement) et SPEC_BIBLE_LORE_WIKI v8.2 (gabarit Fiche d'arc avec arc precedent/suivant, Sommaire sans roadmaps, note ANTI-AMNESIE). -->

Ce fichier definit la forme, les regles de construction et le gabarit du `CODEX_NARRATIF_vX.md`.
Il sert de reference unique en mode CODEX BUILD.
Le modele doit produire un CODEX factuel, compact, autosuffisant, sans narration.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_CODEX_v8_2.md`.
Consultation : fetchee au premier CODEX BUILD (V1 sous Instructions Wiki ; V2+ dans le projet CODEX BUILD dedie, ou elle est normalement jointe en fichier de projet). Pour les builds suivants dans le meme thread, la version en contexte fait foi. Elle porte le process que le CODEX V(N-1) ne contient pas.

---

## 1. Regles generales
- Le CODEX remplace integralement la version precedente.
- Un fait = un seul emplacement canonique.
- Le CODEX ne cree aucun fait nouveau.
- Il reformule, regroupe et compresse uniquement des informations presentes dans le thread, les fichiers joints et l'eventuel CODEX precedent.
- Si une information est absente, floue ou contradictoire : `[INCERTAIN]`.
- Le CODEX est redige en ASCII STRICT, sans aucune exemption : diacritiques retires, signe section U+00A7 remplace par S (sections S1..S7, S3a, S3b), tiret cadratin U+2014 par -, guillemets et apostrophes typographiques par leurs equivalents droits. Verification : grep -nP '[^\x00-\x7F]' vide sur le fichier genere.
- Raison : tout caractere non-ASCII est corruptible au transfert mobile, et le signe section portait le routage structurel (S3a, renvois internes) : c'etait le caractere le plus couteux a perdre. Translitteration fixe, jamais suppression brute (le caractere accentue disparait au transfert ; l'ASCII survit).
  - Allemand : u-trema -> u ; o-trema -> oe ; a-trema -> ae ; eszett -> ss (ex. Ubung, schoen, Maedchen, Strasse).
  - Francais : accents retires dans les fichiers ; reaccentues en narration (cf. instructions).
  - Japonais / coreen : romanisation ASCII (Hepburn sans macron ; romanisation revisee). Kanji et hangul jamais ecrits : romanisation + glose du sens si mot porteur, pas un nom propre.
- Ingestion : un nom fetche en forme accentuee est converti en ASCII a l'ecriture, jamais reinjecte accentue dans un fichier ni la narration. Pour interroger le canon, requeter la forme d'origine accentuee (meilleur rappel).
- Le CODEX est un fichier unique structure en CORE + 7 ANNEXES balisees. Ce n'est PAS une collection de fichiers separes (mais le BUILD produit aussi, a cote, la memoire refroidie et la Memoire narrative - cf. 4ter).
- VERSIONNAGE DES TAMPONS : les OOC actifs (S5) et interdits accumules (S6) sont tamponnes par version de CODEX `[V<n>]`, jamais par date. V<n> = la version du CODEX sous laquelle l'entree a ete posee. Le champ "date reelle de derniere mise a jour" des metadonnees garde une date calendaire (tracabilite du build), mais aucune entree interne n'est datee.
- DECOUPLAGE DES VERSIONS : aucune epingle de version croisee entre fichiers (ni CODEX<->BIBLE, ni fiches<->CODEX). Seule trace de version externe autorisee : un reperage advisory `dernier sync BIBLE: B<x>` dans les metadonnees (S1) du CODEX, NON bloquant - simple canari signalant un CODEX builde sur une BIBLE ancienne. Pas de mention de version dans `bible_lore`. Les tampons internes restent `[V<n>]`.

## 2. Principe redactionnel
- Dense > exhaustif.
- Ligne telegraphique > phrase pleine.
- Renvoi court autorise : `cf. [ANNEXE_X]`, `cf. BIBLE SBX`, `cf. WIKI <dossier>/<page>.md`, `cf. PARTIES <dossier>/<page>.md`.
- Pas de redites entre sections.
- Pas d'adjectifs decoratifs.
- Pas d'exemples illustratifs.
- Pas de justifications.
- Pas de prose hors ANNEXE_STYLE.
- MEMOIRE CHAUDE DE SESSION + ANCRES STABLES DU PROTAGONISTE. Le CODEX porte l'etat actuel du RP, les PNJ en scene, les decisions OOC, les divergences fraiches non formalisees ET le ledger de capacites stables du protagoniste (section dediee S3). Le CODEX doit rester AUTO-SUFFISANT : il fonctionne meme sans BIBLE ni WIKI.
- UNIVERSALITE : la BIBLE et le WIKI sont OPTIONNELS. S'ils existent, le lore statique volumineux (backstory, roadmaps, power-scaling, fiches PNJ) y vit et le CODEX y renvoie. S'ils n'existent pas, ce qui est indispensable a la continuite (dont les capacites du PJ) vit dans le CODEX. L'offload est conditionnel, jamais une obligation.
- Si une BIBLE_LORE est presente : renvoyer a `cf. BIBLE SBX` ou `cf. WIKI <dossier>/<page>.md` pour tout fait deja couvert - mais UNIQUEMENT si la cible contient reellement le detail (anti-boucle : un renvoi ne pointe jamais vers un autre renvoi).
- Si un fait issu du RP est formalise dans Parties/ : renvoyer a `cf. PARTIES <dossier>/<page>.md`.

## 3. Budget

### Plafond
- Plafond dur : CODEX <= 35 000 caracteres.
- Contrainte globale : CODEX + BIBLE_LORE <= 100 000 caracteres (seuil RAG des fichiers de projet). Garantie par construction : 35 000 (CODEX) + 55 000 (BIBLE) = 90 000, marge 10 000.
- Verification au build : `wc -m` (caracteres, locale UTF-8) sur le fichier genere.
- Depassement : signaler, proposer des compressions par gain decroissant (caracteres recuperes + ce qu'on perd), le joueur tranche. Compresser, jamais supprimer l'information utile sans validation.

### Repartition

Sections stables (plafonds fixes) :
- CORE (S1, S2, S3 complet [S3a invariants + S3b courant], S4, S5, S6, S7) : max 8 000 caracteres. (Le 'S3 pointeur' de v8.0 etait un fossile v7 : S3a porte le detail complet des capacites depuis v8.0, le budget l'acte.)
- ANNEXE_STYLE : max 2 000 caracteres.
- ANNEXE_LORE (buffer divergences fraiches) : max 1 000 caracteres.
- Total stable : max 11 000 caracteres.

Sections cumulatives (solde = 24 000 caracteres) :
- ANNEXE_PNJ + ANNEXE_CHRONO + ANNEXE_INVENTAIRE + ANNEXE_TCHEKHOV + ANNEXE_SAVOIRS.
- Repartition libre entre elles selon les besoins du RP.

### Signal d'archivage
- La taille mesuree au build (wc -m) est ECRITE dans la metadonnee `taille au build` (S1). En narration, le signal est une LECTURE de cette metadonnee, jamais une estimation du modele.
- Le CODEX etant statique pendant un thread, le signal s'evalue UNE FOIS, a l'ouverture : si taille au build >= 80% du plafond (28 000 car) -> `[ARCHIVAGE SUGGERE - CODEX a X% du plafond. Compresser CHRONO et/ou archiver dans Parties/.]`
- Le joueur decide. Le MJ ne force pas.

## 4. Regle d'unicite des faits
Chaque fait n'apparait qu'une seule fois dans tout le systeme. Emplacement canonique :

### Dans le CODEX
- Etat courant du protagoniste (position, blessures, ressources du moment) -> CORE S3b (etat courant)
- Capacites stables + description physique + resume de backstory du protagoniste -> CORE S3a (chaud, ancre)
- Reprise et etat courant -> CORE S4
- OOC ecrasant le canon -> CORE S5
- Interdits accumules -> CORE S6
- Sources web -> CORE S7
- Voix, statut, derniere action des PNJ en scene -> ANNEXE_PNJ
- Divergences fraiches non encore formalisees -> ANNEXE_LORE
- Evenements de la session courante, arcs -> ANNEXE_CHRONO
- Objets en jeu -> ANNEXE_INVENTAIRE
- Etat des fils Tchekhov (statut + derniere interaction) -> ANNEXE_TCHEKHOV
- Style -> ANNEXE_STYLE
- Qui sait quoi maintenant -> ANNEXE_SAVOIRS

### Hors du CODEX
- Backstory COMPLETE du protagoniste -> Parties/Suivi/<Nom>_Fiche.md (froid, fetch a la demande). Le CODEX S3a en porte le RESUME chaud. L'INSTANCE jouee (etat, capacites, description) vit dans le CODEX S3, pas dans la BIBLE/WIKI. Mais l'ENTITE, si elle existe hors de la partie (canon ou OC promu au lore), peut y etre decrite neutrement - cf. regle de placement (SPEC_BIBLE). Renvois `cf.` a sens unique, jamais de boucle.
- Definitions des fils Tchekhov (condition, consequence) -> BIBLE SB8 ou WIKI
- Lore canon dans le perimetre du focus -> BIBLE / WIKI
- Divergences lore etablies et formalisees -> BIBLE SB1/SB3 ou WIKI
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
- Silence revele par erreur joueur -> integration CORE S3 etat ou ANNEXE_PNJ voix.
- Evenement clos sans consequence -> compression ANNEXE_CHRONO archive.
- Divergence lore formalisee dans la BIBLE lors d'un BIBLE BUILD -> suppression de l'ANNEXE_LORE, renvoi `cf. BIBLE`.
- TEST DE SAILLANCE (critere de CONSERVATION, pas seulement de rejet) : un fait reste dans le CODEX seulement s'il (a) affecte l'etat courant du protagoniste, (b) est un Tchekhov vivant ou armable, (c) est une divergence fraiche non formalisee, (d) porte la continuite du prochain battement, ou (e) est une capacite stable du protagoniste. Sinon : couleur narrative -> Memoire_{Univers}_<n> (livrable 3, archive joueur) ; detail clos sans portee -> coupe. La couleur ne se perd pas, elle descend dans la Memoire ; elle n'encombre pas le CODEX.
- PROMOTION : toute capacite ou tout fait DURABLE demontre en jeu et absent du calque stable -> promu dans la section Capacites du CODEX (S3a) ; si une BIBLE/WIKI sert de calque lore au RP, monter aussi via BIBLE/WIKI BUILD et pointer dessus. Jamais laisser une capacite durable en memoire transitoire re-derivable a chaque thread. Cette regle prime sur la doctrine "memoire chaude".
- ARBITRAGE UNICITE (cas de la promotion double) : S3a garde TOUJOURS le detail chaud des capacites du protagoniste - exception ASSUMEE a la regle d'unicite (section 4). La page BIBLE/WIKI decrit l'ENTITE (lore neutre, si elle existe) ; S3a decrit l'INSTANCE et ne se compresse JAMAIS en simple renvoi : sinon la capacite redevient a un fetch de distance et la re-derivation que S3a existe pour tuer ressuscite.

## 4ter. Sortie de build RP (TROIS LIVRABLES OBLIGATOIRES)
Tout CODEX BUILD de fin de thread RP produit SYSTEMATIQUEMENT trois fichiers. Aucun n'est conditionnel.

1. CODEX_NARRATIF_vN.md - la memoire CHAUDE. Ecrase la version precedente. Etat courant, PNJ en scene, divergences fraiches, Tchekhov (etat), CHRONO de session. Autosuffisant sur la continuite (ou on en est, ou on va), renvoie a BIBLE/WIKI/Parties pour le lore et le passe.

2. La memoire REFROIDIE - fichiers .md dans Parties/ pour ce qui sort durablement de scene a l'arc a venir (PNJ qui disparaissent, factions dissoutes, lieux quittes, arcs clos). Exemple type : une faction ou un groupe de PNJ qui sort durablement de scene. Indexes dans le CODEX via pointeur `cf. PARTIES <dossier>/<page>.md`. Un fichier par entite ou groupe coherent qui refroidit ; on ECRASE si l'entite refroidit davantage, on n'empile pas. Si rien ne refroidit a ce build, produire une note explicite "memoire refroidie : rien a sortir ce thread" (le livrable existe, meme vide). Les pointeurs `cf. PARTIES` des pages refroidies sont PERMANENTS : ils survivent au test de saillance et aux builds suivants, regroupes dans l'index Refroidi (ANNEXE_CHRONO, cf. gabarit). Cet index est le substitut du Sommaire pour Parties/ entre deux BIBLE BUILDs (le Sommaire, page WIKI, n'est mis a jour qu'au BIBLE BUILD) : le test de fetch des Instructions RP croise Sommaire OU index Refroidi.

3. Memoire_{Univers}_<n> - l'archive NARRATIVE du thread, destinee au JOUEUR (topo, relecture, alimentation d'une autre IA). Recit condense des battements joues (un fichier FIGE par thread, jamais reecrit). Nommage : `Memoire_{Univers}_<n>.md`, empile (n = numero de thread). Ce fichier n'est PAS uploade sur le repo, n'est JAMAIS fetche par le MJ, et echappe au budget de page Parties. Aucun pointeur `cf.` ne le designe depuis le CODEX (anti-boucle : un cf. mene a un emplacement consultable).

Procedure de triage (alimente les livrables 2 et 3) :
a. Identifier les faits, PNJ, arcs et CHRONO qui ne sont plus pertinents pour l'arc a venir -> memoire refroidie (livrable 2).
b. Condenser les battements du thread -> Memoire_{Univers}_<n> (livrable 3).
c. Consulter la roadmap de l'arc a venir pour orienter le CODEX (livrable 1) vers la suite.

Convention de nommage Parties/ :
- Archive narrative joueur : `Memoire_{Univers}_<n>.md` (FIGEE, empilee, HORS repo - reste chez le joueur).
- Memoire refroidie thematique : `Suivi/<sujet>.md` ou sous-dossier dedie (ECRASEE quand le sujet refroidit davantage).
- Fiche protagoniste : HORS PERIMETRE du CODEX build. L'etat chaud (capacites, description, etat) vit dans le CODEX CORE S3. La backstory FROIDE vit en `Suivi/<Nom>_Fiche.md`, creee au V1 et maintenue via BIBLE BUILD - le CODEX build ne la produit ni ne la touche.

## 5. Architecture modulaire

### Sections obligatoires (lues a chaque tour de narration)
- `[CORE - LECTURE OBLIGATOIRE]`
- `[ANNEXE_STYLE - LECTURE OBLIGATOIRE]`

### Sections conditionnelles (lues selon la scene)
- `[ANNEXE_PNJ - si PNJ en scene ou convoque]`
- `[ANNEXE_LORE - buffer divergences fraiches, vide = sain]`
- `[ANNEXE_CHRONO - si continuite temporelle]`
- `[ANNEXE_INVENTAIRE - si objet en jeu]`
- `[ANNEXE_TCHEKHOV - si fil narratif touche ou plantable]`
- `[ANNEXE_SAVOIRS - si secret, revelation ou asymetrie]`

### Compression chronologique progressive (ANNEXE_CHRONO)
- Thread courant : une ligne par battement (Tour n).
- Thread N-1 : une ligne par scene majeure.
- Threads anterieurs : une ligne par arc resolu.
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
1. Chaque fait n'apparait qu'une fois dans les sources EN CONTEXTE (CODEX, BIBLE, narration brute, instructions). Pour WIKI/Parties (pages non chargees) : spot-check via Sommaire / index Refroidi sur les seuls faits SUSPECTS de doublon - aucune pretention a verifier exhaustivement des pages absentes du contexte.
2. Le plafond 35 000 car est respecte (11 000 stable / 24 000 cumulatif), taille mesuree au wc -m et REPORTEE dans la metadonnee `taille au build` ; grep -nP '[^\x00-\x7F]' revient vide.
3. Les sections ne se repetent pas.
4. Le texte reste exploitable sans thread externe.
5. Tout doute est marque `[INCERTAIN]`.
6. Chaque PNJ actif a un champ voix defini ou `voix: [INCERTAIN]`.
7. Le protagoniste a une nature corporelle explicite et une regle de perception par PNJ dans S3.
8. Les regles de filtrage S4bis et S4ter ont ete appliquees.
9. Aucun fait couvert par la BIBLE, le WIKI, Parties/ ou les instructions n'a ete duplique.
10. ANNEXE_SAVOIRS coherente avec ANNEXE_PNJ et CORE S4.
11. ANNEXE_LORE ne contient que des divergences fraiches (< 1000 chars). Si elle deborde, formaliser dans la BIBLE via BIBLE BUILD.
12. Aucun pointeur circulaire : chaque `cf.` mene a un emplacement qui CONTIENT le fait, jamais a un autre renvoi (verif specifique : S3a Capacites ne renvoie a BIBLE/WIKI que si la cible porte le detail).
13. Capacites stables du protagoniste ancrees en S3a ; aucune capacite durable laissee uniquement en etat transitoire (S3b) ou en memoire eparse. Test de saillance (4bis) applique : la couleur narrative est descendue dans la Memoire, pas conservee dans le CODEX.

---

# GABARIT DE SORTIE

# CODEX_NARRATIF_v<N>

## [CORE - LECTURE OBLIGATOIRE]

### S1 Metadonnees
- titre: <titre de la campagne>
- univers: <nom / type>
- regime: canonique | divergence | hybride
- protagoniste: <nom>
- date in-world de reprise: <date>
- date reelle de derniere mise a jour: <AAAA-MM-JJ>
  note: les tampons OOC (S5) et interdits (S6) utilisent [V<n>], pas la date.
- codex_version: V<N>
- plafond: 35 000 car.
- taille au build: <wc -m> car. (<X>% du plafond)
- bible_lore: <nom du fichier BIBLE_LORE si presente, sinon "aucune"> (sans numero de version)
- dernier sync BIBLE: <B<x> si BIBLE presente, advisory non bloquant ; sinon "n/a">
- wiki_base: <URL racine du WIKI GitHub si present, sinon "aucun">
- parties_base: <URL racine de Parties/<Univers>/Partie<n>/ si present, sinon "aucun">

### S2 Premisse
- <ligne 1>
- <ligne 2>
- <ligne 3>
- <ligne 4>
- <ligne 5>

### S3 Protagoniste
Source vivante de l'INSTANCE jouee : ICI (CODEX) + Parties/Suivi pour la backstory froide. L'instance ne vit pas dans la BIBLE/WIKI ; mais l'ENTITE, si elle est du lore (canon ou OC promu), y est decrite a part - cf. SPEC_BIBLE. Capacites ANCREES en S3a (jamais re-derivees).

**S3a Invariants (chaud, stables, changent rarement)**
- Nom / alias :
- Nature corporelle : <corps propre | conscience hote | possession | symbiote | autre>
- Perception par PNJ : <qui percoit, comment, limites>
- Description physique : <apparence stable : silhouette, traits, signes distinctifs. PAS l'etat du moment (-> S3b)>
- Capacites stables : <pouvoirs durables, ANCRE canonique. Detail complet ici. Toute capacite durable demontree en jeu est promue ici - cf. 4bis>
- Resume de backstory : <quelques lignes denses, contexte suffisant pour narrer. Backstory complete = Parties/Suivi (froid, fetch a la demande)>
- Valeurs inviolables : <rappel compact>
- Tics / voix : <rappel compact>

**S3b Etat courant (chaud, transitoire, churn par thread)**
- Etat physique actuel : <blessures, fatigue, marques du moment>
- Etat emotionnel actuel : <en 1 ligne>
- Ressources du moment : <objets ponctuels, allies presents, munitions, mana disponible>
- Contraintes actives : <sceaux, maledictions, limitations temporaires>

### S4 Reprise et etat courant
- Lieu :
- Sous-lieu :
- Dernier [REPERE] :
- PNJ presents physiquement :
- Savoir du protagoniste :
- Savoir cache :
- Tension dominante :
- Rapport de force :
- Dernier echange - joueur : <citation exacte> / PNJ : <citation exacte>
- Etat-cle minimal :
- Prochaine bascule amorcee :

### S5 OOC actifs
- `[V<n>] - <enonce ecrasant le CODEX ou le canon> | sections impactees`  (V<n> = version du CODEX sous laquelle le thread a ete joue ; remplace l'ancien tampon date)

### S6 Interdits accumules
Pieges identifies en session, non reintroduits dans les CODEX suivants. Purge au build, avec validation joueur, des interdits INERTES (piege devenu impossible a reproduire : PNJ definitivement mort, arc clos sans heritier).
- `[V<n>] - <interdit 1>`

### S7 #SITES_REF
| Source | URL | Usage |
|---|---|---|
| <nom> | <url> | <quand consulter> |

---

## [ANNEXE_PNJ - si PNJ en scene ou convoque]

Ne stocker que ce qui diverge du canon ou est specifique au RP.
Pour le canon non modifie, renvoyer a BIBLE, WIKI ou Parties/.

Champ voix obligatoire pour chaque PNJ actif :
- `voix: muet par defaut`
- `voix: sobre, monosyllabique`
- `voix: lyrique, archaique`
- `voix: <description situee>`
- `voix: [INCERTAIN] - ordre OOC requis avant dialogue`

### Actifs
- <PNJ> - <role> | <statut> | <voix> | <relation au protagoniste> | <derniere action> | <inviolable>

### Secondaires
- <PNJ> - <role> | <voix> | <relation> | <inviolable>

### Absents / morts
- <nom>, <nom>, <nom>

---

## [ANNEXE_LORE - buffer divergences fraiches]

Divergences du RP apparues en session, pas encore formalisees dans la BIBLE ou le WIKI.
Max 1 000 caracteres. Si debordement : declencher BIBLE BUILD pour formaliser.
Vide = sain.

- <divergence 1>
- <divergence 2>

---

## [ANNEXE_CHRONO - si continuite temporelle]

`Date reelle | Date in-world | Compteur | Evenement condense`

### Thread courant (une ligne par battement)
- <date> | <date IW> | Tour 1 | <evenement>
- <date> | <date IW> | Tour 2 | <evenement>

### Thread N-1 (une ligne par scene majeure)
- <scene majeure>

### Threads anterieurs (une ligne par arc resolu)
- <arc resolu>

### Fil des arcs (memoire longue - anti-amnesie)
La suite ORDONNEE des arcs traverses dans ce RP, du premier joue jusqu'a l'arc courant, puis l'arc suivant prevu. C'est ICI que vit la memoire du chemin parcouru : en jeu on ne lit ni la grosse BIBLE ni les roadmaps, donc ce fil est le substitut de memoire pour la coherence de fond (cf. SPEC_BIBLE_LORE_WIKI, note ANTI-AMNESIE). Une ligne par arc, dans l'ordre de jeu.
`<#> - <Arc> : <issue / etat 1 ligne> (detail clos : cf. PARTIES Archives/<page>.md si archive)`
- 1 - <Arc1> : <issue>
- 2 - <Arc2> : <issue>
- ... -> arc courant (cf. section Arcs ci-dessous) -> arc suivant prevu : <Arc suivant>

### Arcs (etat courant)
`Arc - enjeu | jalon courant | prochain jalon | statut | fiche_arc: cf. WIKI Fiches_Arc/<Prota>/<page>.md | (build) roadmap: cf. WIKI Roadmap/<Prota>/<page>.md`
- <arc> - <enjeu> | <jalon> | <prochain> | <ouvert/suspendu/clos> | fiche_arc: cf. WIKI Fiches_Arc/<Prota>/<page>.md | (build) roadmap: cf. WIKI Roadmap/<Prota>/<page>.md
- L'etat d'arc (jalon courant / prochain jalon) est tenu A JOUR ici au fil du thread ; la fiche d'arc, elle, est figee a l'ouverture (cf. SPEC_BIBLE_LORE_WIKI, gabarit Fiche d'arc). Le renvoi fiche_arc: pointe la page fetchee une fois a l'ouverture. Le renvoi roadmap: est marque (build) : il ne sert qu'a (re)construire une fiche d'arc en mode Wiki, JAMAIS au fetch en narration (la roadmap porte le futur de la saga -> risque de prefiguration).

### Refroidi (index PERMANENT - survit au test de saillance)
`<entite ou groupe> -> cf. PARTIES <dossier>/<page>.md`
- <entite> -> cf. PARTIES Suivi/<page>.md

---

## [ANNEXE_INVENTAIRE - si objet en jeu]

`Objet - localisation | etat | porteur | signification narrative`
- <objet> - <localisation> | <etat> | <porteur> | <signification>

---

## [ANNEXE_TCHEKHOV - si fil narratif touche ou plantable]

Etat des fils uniquement. Definitions (condition, consequence) : cf. BIBLE SB8.

`Fil - statut | derniere interaction`
- <fil 1> - ouvert | <derniere scene/thread ou le fil a ete touche>
- <fil 2> - arme | <idem>
- <fil 3> - paye | <resolution en 1 ligne>

---

## [ANNEXE_STYLE - LECTURE OBLIGATOIRE]

<Paragraphe 1 : voix narrative, rythme dominant.>

<Paragraphe 2 : sensorialite privilegiee, images autorisees, densite.>

<Paragraphe 3 : traitement des dialogues, silences, tension de fin.>

---

## [ANNEXE_SAVOIRS - si secret, revelation ou asymetrie]

Matrice d'information : qui sait quoi MAINTENANT dans le RP.

`Secret - qui sait | qui ne sait pas | condition de revelation | consequence si revele`
- <secret 1> - <sachants> | <ignorants> | <condition> | <consequence>

### Ironie dramatique active
- <situation> : <ce que le joueur sait mais pas le PNJ X>

FIN_CODEX_V<N>
