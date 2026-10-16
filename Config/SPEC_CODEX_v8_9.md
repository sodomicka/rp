# SPEC_CODEX v8.9

Ce fichier définit la forme, les règles de construction et le gabarit du `CODEX_NARRATIF.md`. Le CODEX vit sur le dépôt sous ce nom FIXE, `Parties/{Univers}/Partie<n>/CODEX_NARRATIF.md`, écrase à chaque build : la version porte dans le titre (`# CODEX_NARRATIF_v<N>`) et la balise `FIN_CODEX_V<N>`, l'historique vit dans git. Une seule version sur le dépôt, jamais de copie versionnée à côté.
Il sert de référence unique en mode CODEX BUILD.
Le modèle doit produire un CODEX factuel, compact, autosuffisant, sans narration.

Emplacement : `https://github.com/sodomicka/rp/blob/main/Config/SPEC_CODEX_v8_9.md`.
Consultation : lue EN ENTIER sur le dépôt (raw) à chaque build, avant toute autre action. Aucune copie embarquée ne fait foi : une SPEC trouvée ailleurs (skill, fichiers de projet) se confronte à celle du dépôt, qui tranche. Seule exception : une SPEC fournie en conversation fait foi pour CE build, signalée en une ligne. Vérifier le numéro de version courant par le listing de `Config/`. Elle porte le process que le CODEX V(N-1) ne contient pas.

---

## 1. Règles générales
- Le CODEX remplace intégralement la version précédente.
- Un fait = un seul emplacement canonique.
- Le CODEX ne crée aucun fait nouveau.
- Il reformule, regroupe et compresse uniquement des informations présentes dans le thread de jeu, les fichiers joints et l'éventuel CODEX précédent.
- THREAD DE JEU = ENTRÉE DE BUILD. Une partie vit dans un seul projet. Le build se fait dans un thread dédié du même projet et LIT lui-même la narration brute dans le thread de jeu (lecture de thread, messages complets, du plus ancien au plus récent) : rien n'est exporté ni collé. Thread de jeu à digérer : celui que nomme le joueur ; à défaut, le thread de jeu du projet le plus récent après le `thread source` du CODEX V(N-1). Doute -> demander. Hors projet seulement : narration brute fournie dans le thread de build.
- Si une information est absente, floue ou contradictoire : `[INCERTAIN]`.
- Ingestion : pour interroger le canon, requêter la forme d'origine du nom (accentuée si elle l'est : meilleur rappel).
- Le CODEX est un fichier unique structuré en CORE + 7 ANNEXES balisées. Ce n'est PAS une collection de fichiers séparés (mais le BUILD produit aussi, à côté, la mémoire refroidie, le Sommaire de jeu et la Mémoire narrative - cf. 4ter).
- VERSIONNAGE DES TAMPONS : les OOC actifs (§5) et interdits accumulés (§6) sont tamponnés par version de CODEX `[V<n>]`, jamais par date. V<n> = la version du CODEX sous laquelle l'entrée a été posée. Le champ "date réelle de dernière mise à jour" des métadonnées garde une date calendaire (traçabilité du build), mais aucune entrée interne n'est datée.
- DÉCOUPLAGE DES VERSIONS : aucune épingle de version croisée entre fichiers (ni CODEX<->BIBLE, ni fiches<->CODEX). Seule trace de version externe autorisée : un repérage advisory `dernier sync BIBLE: B<x>` dans les métadonnées (§1) du CODEX, NON bloquant - simple canari signalant un CODEX buildé sur une BIBLE ancienne. Pas de mention de version dans `bible_lore`. Les tampons internes restent `[V<n>]`. Même logique pour la SPEC : la métadonnée `spec au build` (§1) trace version et source de la spec utilisée - advisory, canari anti spec fantôme (un build fait sur une spec périmée se voit au premier coup d'œil).

## 2. Principe rédactionnel
- Dense > exhaustif.
- Ligne télégraphique > phrase pleine.
- Renvoi court autorisé : `cf. [ANNEXE_X]`, `cf. BIBLE SBX`, `cf. WIKI <dossier>/<page>.md`, `cf. PARTIES <dossier>/<page>.md`.
- Pas de redites entre sections.
- RENVOI SEC : un fait pivot (mécanisme de capacité, limite révélée, événement charnière) vit à UN emplacement canonique ; toute autre section qui en a besoin POINTE (`cf. S3a`, `cf. [ANNEXE_X]`) sans re-paraphraser. Tolérance : le nom du fait + son effet en 3-5 mots + le renvoi ; jamais le mécanisme redécrit. Un même mécanisme rédigé en toutes lettres dans 2+ sections = défaut d'audit (point 3).
- GRADIENT DE FRAÎCHEUR : la granularité d'un fait dépend de son ÂGE, pas de sa section. Le CODEX vN sert à narrer le thread N : détail fin réservé à l'état courant et au thread N-1 (continuité) ; tout fait date de N-2 ou avant descend en RÉSUMÉ, dans TOUTES les sections (PNJ, SAVOIRS, INVENTAIRE - la compression progressive n'est plus l'exclusivité de la CHRONO). Deux exceptions : (a) fils Tchekhov vivants/armés : état précis conservé quel que soit l'âge (un fil planté en N-5 peut payer demain) ; (b) ancres durables par personnage et par lieu : voix, traits saillants, relation - la fiche d'identité compacte, jamais l'historique des faits et gestes.
- Pas d'adjectifs décoratifs.
- Pas d'exemples illustratifs.
- Pas de justifications.
- Pas de prose hors ANNEXE_STYLE.
- MÉMOIRE CHAUDE DE SESSION + ANCRES STABLES DU PROTAGONISTE. Le CODEX porte l'état actuel du RP, les PNJ en scène, les décisions OOC, les divergences fraîches non formalisées ET le ledger de capacités stables du protagoniste (section dédiée §3). Le CODEX doit rester AUTO-SUFFISANT : il fonctionne même sans BIBLE ni WIKI.
- UNIVERSALITÉ : la BIBLE et le WIKI sont OPTIONNELS. S'ils existent, le lore statique volumineux (backstory, roadmaps, power-scaling, fiches PNJ) y vit et le CODEX y renvoie. S'ils n'existent pas, ce qui est indispensable à la continuité (dont les capacités du PJ) vit dans le CODEX. L'offload est conditionnel, jamais une obligation.
- Si une BIBLE_LORE est présente : renvoyer à `cf. BIBLE SBX` ou `cf. WIKI <dossier>/<page>.md` pour tout fait déjà couvert - mais UNIQUEMENT si la cible contient réellement le détail (anti-boucle : un renvoi ne pointe jamais vers un autre renvoi).
- Si un fait issu du RP est formalisé dans Parties/ : renvoyer à `cf. PARTIES <dossier>/<page>.md`.

## 3. Budget

### Plafond (barème croissant linéaire)
- Plafond dur du build N : `plafond(N) = min(30 000 + 3 000 x (N - 1), 90 000)` caractères.
- Barème : V1 (fin de worldbuilding) = 30 000 ; +3 000 par génération ; terminal 90 000 atteint à V21 (V20 = 87 000). Absolu et calculable depuis le seul numéro de version : aucune dépendance à la taille mesurée du V(N-1), un build qui déraille ne contamine pas les suivants.
- Raison du barème : un plafond fixe élevé est un mur lointain sans pression locale - le CODEX gonfle de build en build sans jamais le toucher, et le gras s'installe en redites. Le barème met un plafond PROCHE à chaque génération : la croissance se mérite (la saga accumule légitimement arcs et PNJ), la redite se paie comptant.
- Raison du terminal 90 000 : le CODEX est lu EN ENTIER à l'ouverture de chaque thread de jeu et reste en contexte tout le thread, en face de la roadmap en cours, des deux Sommaires et des fiches de l'étape. 90 000 laisse la place à ce socle et à la narration. CODEX et BIBLE ne sont jamais en contexte ensemble : la BIBLE n'est pas lue en jeu.
- Vérification au build : calculer plafond(N), puis `wc -m` (caractères, locale UTF-8) sur le fichier généré, UNE fois en fin de build. Les deux valeurs sont reportées en §1.

### Répartition
Sections stables (plafonds fixes, INVARIANTS quel que soit N - lues à chaque tour) :
- CORE (§1, §2, §3 complet [§3a invariants + §3b courant], §4, §5, §6, §7) : max 8 000 caractères.
- ANNEXE_STYLE : max 2 000 caractères.
- ANNEXE_LORE (buffer divergences fraîches) : max 1 000 caractères.
- Total stable : max 11 000 caractères. Le stable ne suit JAMAIS le barème : le CORE est relu à chaque tour, un CORE qui grossit avec la saga = lost-in-the-middle garanti. Toute la pente vit dans le cumulatif.

Sections cumulatives (solde variable) :
- `cumulatif(N) = plafond(N) - 11 000`. Exemples : V1 = 19 000 ; V5 = 31 000 ; V10 = 46 000 ; V21+ = 79 000.
- ANNEXE_PNJ + ANNEXE_CHRONO + ANNEXE_INVENTAIRE + ANNEXE_TCHEKHOV + ANNEXE_SAVOIRS.
- Répartition libre entre elles selon les besoins du RP.

Total CODEX (stable + cumulatif) : max plafond(N).

### Budgets-cibles par section (écrire À LA CIBLE, pas écrire-puis-couper)
Cibles fixes pour CORE et stable (plafonds durs) ; enveloppe globale pour le cumulatif (libre par construction). Les cibles visent ~5% sous chaque plafond : on rédige directement dedans, on ne déborde pas pour raboter ensuite.

| Section | Cible (car.) | Plafond |
|---|---|---|
| §1 Métadonnées | ~650 | (CORE) |
| §2 Prémisse | ~550 | (CORE) |
| §3a Invariants | ~3000 | (CORE) |
| §3b État courant | ~450 | (CORE) |
| §4 Reprise | ~1400 | (CORE) |
| §5 OOC actifs | ~550 | (CORE) |
| §6 Interdits | ~650 | (CORE) |
| §7 #SITES_REF | ~300 | (CORE) |
| CORE total | ~7550 | 8000 (dur) |
| ANNEXE_STYLE | ~1800 | 2000 (dur) |
| ANNEXE_LORE | viser le vide | 1000 (dur) |
| Cumulatif (PNJ/CHRONO/INVENTAIRE/TCHEKHOV/SAVOIRS) | enveloppe cumulatif(N), viser ~5% sous | cumulatif(N) (dur) |

Les cibles sont indicatives et calées sur la DENSITÉ attendue, pas sur le plafond : un plafond plus haut n'autorise pas un CORE plus gras (le CORE est relu à chaque tour - lost-in-the-middle). Un RP particulier peut déplacer quelques centaines de caractères entre sections CORE tant que CORE total reste <= 7600.

### Ordre et méthode de rédaction
- Rédiger par POIDS DÉCROISSANT : les sections les plus lourdes d'abord (typiquement §3a et §4 dans CORE ; ANNEXE_CHRONO et ANNEXE_PNJ dans le cumulatif), chacune directement à sa cible.
- Écrire À LA CIBLE des le premier jet, viser ~5% sous le plafond de section. Ne pas rédiger confortablement pour couper après.
- UNE seule mesure `wc -m` en fin de build (sur le fichier complet), pas une mesure par section ni par retouche.

### Dépassement
Deux régimes distincts, ne pas les confondre :
- Dépassement d'une CIBLE de section (interne) : le modèle tranche SEUL. UNE passe décisive (coupe franche, viser -10% sous la cible pour reprendre de la marge), puis UNE seule re-mesure. JAMAIS de micro-coupes successives re-mesurées à chaque fois : le grignotage = un appel outil par coupe, la latence explose pour finir à quelques caractères de la limite. Pas de validation joueur requise.
- Dépassement du PLAFOND DUR total (plafond(N)) à la livraison : SIGNALER, proposer des compressions par gain décroissant (caractères récupérés + ce qu'on perd), le JOUEUR tranche. Compresser, jamais supprimer l'information utile sans validation.

### Signal d'archivage (déclencheurs absolus)
- La taille mesurée au build (`wc -m`) est ÉCRITE dans la métadonnée `taille au build` (§1). En narration, le signal est une LECTURE de cette métadonnée, évaluée UNE FOIS à l'ouverture, jamais une estimation du modèle.
- DÉCOUPLÉ du % de plafond (plafond(N) est un barème de croissance, pas le seuil RAG ; un pourcentage du plafond ne signale rien d'utile). Deux déclencheurs ABSOLUS :
  - ANNEXE_CHRONO > 15 000 car -> `[ARCHIVAGE SUGGERE - archiver les threads anciens dans Parties/, ne garder que les arcs resolus en une ligne.]` (Coût de relecture par tour : la CHRONO est de fait relue souvent.)
  - Taille totale > 64 000 car -> `[ARCHIVAGE SUGGERE - CODEX volumineux. Compresser CHRONO et/ou archiver dans Parties/.]` (Garde-fou fichier, sous la marge RAG. Sous le barème, atteignable à partir de V13 seulement : avant, plafond(N) mord d'abord.)
- Le joueur décide. Le MJ ne force pas.

## 4. Règle d'unicité des faits
Chaque fait n'apparaît qu'une seule fois dans tout le système. Emplacement canonique :

### Dans le CODEX
- État courant du protagoniste (position, blessures, ressources du moment) -> CORE §3b (état courant)
- Capacités stables + description physique + résumé de backstory du protagoniste -> CORE §3a (chaud, ancre)
- Reprise et état courant -> CORE §4
- OOC écrasant le canon -> CORE §5
- Interdits accumulés -> CORE §6
- Sources web -> CORE §7
- Voix, statut, dernière action des PNJ en scène -> ANNEXE_PNJ
- Divergences fraîches non encore formalisées -> ANNEXE_LORE
- Événements de la session courante, arcs -> ANNEXE_CHRONO
- Objets en jeu -> ANNEXE_INVENTAIRE
- État des fils Tchekhov (statut + dernière interaction) -> ANNEXE_TCHEKHOV
- Style -> ANNEXE_STYLE
- Qui sait quoi maintenant -> ANNEXE_SAVOIRS

### Hors du CODEX
- Backstory COMPLÈTE du protagoniste -> Parties/Suivi/<Nom>_Fiche.md (froid, fetch à la demande). Le CODEX §3a en porte le RÉSUMÉ chaud. L'INSTANCE jouée (état, capacités, description) vit dans le CODEX §3, pas dans la BIBLE/WIKI. Mais l'ENTITÉ, si elle existe hors de la partie (canon ou OC promu au lore), peut y être décrite neutrement - cf. règle de placement (SPEC_BIBLE). Renvois `cf.` à sens unique, jamais de boucle.
- Définitions des fils Tchekhov (condition, conséquence) -> BIBLE SB8 ou WIKI
- Lore canon dans le périmètre du focus -> BIBLE / WIKI
- Divergences lore établies et formalisées -> BIBLE SB1/SB3 ou WIKI
- Power-scaling -> WIKI
- Roadmaps -> WIKI ({Univers}/Roadmap/<Prota>/)
- Fiches personnages -> WIKI
- Arcs joués, CHRONO archivée -> Parties/ (indexés au Sommaire de jeu)
- Décisions et bifurcations prises -> Parties/ (Decisions/)
- Règles d'Or, hiérarchie des sources, interdits génériques -> Instructions RP/Wiki (lues à chaque tour, jamais dupliquées dans le CODEX)

## 4bis. Filtrage au build
- Doublon avec canon accessible via #SITES_REF et non modifié par le RP -> rejet. Si le fetch échoue au moment du build, conserver le fait avec `[FETCH INDISPONIBLE]`.
- Fait déjà présent dans BIBLE, WIKI ou Parties/ -> rejet (renvoyer via `cf.`).
- Doublon interne inter-sections -> rejet.
- Erreur corrigée en scène sans trou CODEX -> rejet.
- OOC émotionnel sans contenu factuel -> rejet.
- Ligne dérivée d'un invariant déjà écrit -> rejet.
- Silence révélé par erreur joueur -> intégration CORE §3 état ou ANNEXE_PNJ voix.
- Événement clos sans conséquence -> compression ANNEXE_CHRONO archive.
- Divergence lore formalisée dans la BIBLE lors d'un BIBLE BUILD -> suppression de l'ANNEXE_LORE, renvoi `cf. BIBLE`.
- TEST DE SAILLANCE (critère de CONSERVATION, pas seulement de rejet) : un fait reste dans le CODEX seulement s'il (a) affecte l'état courant du protagoniste, (b) est un Tchekhov vivant ou armable, (c) est une divergence fraîche non formalisée, (d) porte la continuité du prochain battement, ou (e) est une capacité stable du protagoniste. Sinon : couleur narrative -> Memoire_{Univers}_<n> (livrable 3) ; détail clos sans portee -> coupe. La couleur ne se perd pas, elle descend dans la Mémoire ; elle n'encombre pas le CODEX. La Mémoire est sur le dépôt et relisible AU BUILD (jamais en jeu) : la descente n'est plus un aller simple, mais elle ne rend que du TON, jamais des faits (cf. 4ter, livrable 3).
- PROMOTION : toute capacité ou tout fait DURABLE démontré en jeu et absent du calque stable -> promu dans la section Capacités du CODEX (§3a) ; si une BIBLE/WIKI sert de calque lore au RP, monter aussi via BIBLE/WIKI BUILD et pointer dessus. Jamais laisser une capacité durable en mémoire transitoire re-dérivable à chaque thread. Cette règle prime sur la doctrine "mémoire chaude".
- ARBITRAGE UNICITÉ (cas de la promotion double) : §3a garde TOUJOURS le détail chaud des capacités du protagoniste - exception ASSUMÉE à la règle d'unicité (section 4). La page BIBLE/WIKI décrit l'ENTITÉ (lore neutre, si elle existe) ; §3a décrit l'INSTANCE et ne se compresse JAMAIS en simple renvoi : sinon la capacité redevient à un fetch de distance et la re-dérivation que §3a existe pour tuer ressuscite.
- PORTE DE SORTIE TCHEKHOV : l'ANNEXE_TCHEKHOV ne liste que les fils VIVANTS (planté / ouvert / actif / armé). Un fil qui se clôt (payé, consumé, clos, inerte) : au build de clôture, sa résolution tient en UNE ligne CHRONO (ou rien, si un événement CHRONO la porte déjà) ; au build suivant, il est SUPPRIMÉ de l'annexe. Un fil paye n'a rien à faire dans la mémoire chaude.
- LES CAPACITÉS NE SONT JAMAIS DES FILS : mécanisme, état et limites d'une capacité vivent en §3a, point. Aucune entrée Tchekhov ne doublonne §3a sous un chapeau de fil narratif. Un fil ne touche une capacité que si un enjeu narratif DISTINCT du mécanisme est en suspens (ex. : qui découvrira l'existence de X), et par renvoi sec.
- §3a DESCRIPTIF, JAMAIS NARRATIF : une capacité s'écrit règle + limites (ce qu'elle fait, ce qu'elle ne fait pas, contre quoi elle échoue). Zéro exploit, zéro historique ("a fait reculer X", "a entamé Y" -> CHRONO ou Mémoire narrative). L'invariant DÉCRIT, la CHRONO raconte.

### Fetch conditionnel au build (vitesse)
- Ne fetcher une page du repo (Sommaire, Sommaire de jeu, roadmap, page WIKI/Parties) QUE si une décision de build en DÉPEND : résolution d'un renvoi `cf.`, débusquage d'un doublon SUSPECT (pas une vérification exhaustive de pages absentes du contexte).
- Par défaut : NE PAS fetcher. Le doute léger ne justifie pas un aller-retour réseau : marquer `[INCERTAIN]` coûte moins cher qu'un fetch et laisse le joueur trancher.
- Pas de sur-vérification : une page se consulte au plus une fois, en LECTURE SEULE. Exception obligatoire : la roadmap en cours, pour fixer l'étape courante (cf. 4ter, triage c).

## 4ter. Sortie de build RP (TROIS LIVRABLES OBLIGATOIRES)
Tout CODEX BUILD de fin de thread RP produit trois sorties. Les trois EXISTENT toujours ; c'est leur FORME qui s'allège quand il n'y a rien à produire.

1. CODEX_NARRATIF.md (`Parties/{Univers}/Partie<n>/`) - la mémoire CHAUDE. Écrase la version précédente. État courant, PNJ en scène, divergences fraîches, Tchekhov (état), CHRONO de session. Autosuffisant sur la continuité (où on en est, où on va), renvoie à BIBLE/WIKI/Parties pour le lore et le passé.

2. La mémoire REFROIDIE - fichiers .md dans Parties/ pour ce qui sort durablement de scène à l'arc à venir (PNJ qui disparaissent, factions dissoutes, lieux quittés, arcs clos). Exemple type : une faction ou un groupe de PNJ qui sort durablement de scène. Un fichier par entité ou groupe cohérent qui refroidit ; on ÉCRASE si l'entité refroidit davantage, on n'empilé pas. SI RIEN NE REFROIDIT à ce build : NE PAS créer de fichier - une seule ligne dans la présentation de build suffit ("refroidi : rien à sortir ce thread"). Pas de livrable .md vide à structurer.

   SOMMAIRE DE JEU (`Parties/{Univers}/Partie<n>/Sommaire_Jeu.md`, gabarit : SPEC_BIBLE_LORE_WIKI §8). C'est l'INDEX de toute la mémoire froide de la partie : une entrée par page Parties/ (Suivi, Archives, Décisions), avec les SUJETS qu'elle couvre (personnages, lieux, objets, fils, période), pour que le MJ sache où piocher sans tout fouiller. Le build l'ÉCRIT LUI-MÊME, dans le même build que les pages qu'il crée ou écrase : toute page créée, relivrée ou dont les sujets changent y est reportée, version comprise. Fetché à l'ouverture de chaque thread de jeu. Le Sommaire du WIKI n'indexe pas Parties/ : le build n'y touche pas. Memoires/ n'y figure jamais.

3. Memoire_{Univers}_<n> - l'archive NARRATIVE du thread : récit condensé des battements joués, destinée au JOUEUR (topo, relecture, alimentation d'une autre IA) ET au BUILD (recalibrage de style, cf. ci-dessous). Un fichier FIGÉ par thread, jamais réécrit. Nommage : `Memoire_{Univers}_<n>.md`, empilé (n = numéro de thread).

   EMPLACEMENT : `Parties/{Univers}/Partie<n>/Memoires/`. Écrit sur le dépôt par le MJ (Instructions Wiki §8bis, valable aussi au CODEX BUILD), comme les autres pages Parties/. Échappe au budget de page Parties (500-2000 tokens) : c'est une archive narrative, pas une fiche.

   NON INDEXÉE AU SOMMAIRE - même doctrine que `Roadmap/<Prota>/` : un dossier indexé paraît fetchable en narration. On y accède par listing direct du dossier au build (cf. ACCÈS GITHUB, méthode dossier).

   INTERDITE EN NARRATION. Le MJ ne la fetche JAMAIS de sa propre initiative. Raisons : (a) elle est cumulative et non bornée - un thread de plus, un fichier de plus ; (b) c'est de la prose longue, exactement ce qui noie un contexte (lost-in-the-middle) ; (c) elle réinjecterait en pleine narration ce que le test de saillance vient d'évacuer. Seule exception : un ordre OOC EXPLICITE du joueur, qui prime par hiérarchie. La continuité en jeu passe par le CODEX ; le détail des scènes closes par les pages indexées au Sommaire de jeu.

   FETCHABLE AU BUILD, conditionnel et pour UN usage nommé : RECALIBRER ANNEXE_STYLE (cf. gabarit ANNEXE_STYLE). Ne JAMAIS s'en servir pour réinjecter des faits dans le CODEX - un fait évacué par le test de saillance a été évacué, le repêcher annule la règle. La Mémoire fournit du TON, pas du fait.

   Aucun pointeur `cf.` ne la désigne depuis le CODEX : le CODEX est lu en narration, où la Mémoire est interdite - un `cf.` y menant serait une invitation à enfreindre la règle.

Procédure de triage (alimente les livrables 2 et 3) :
a. Identifier les faits, PNJ, arcs et CHRONO qui ne sont plus pertinents pour l'arc à venir -> mémoire refroidie (livrable 2).
b. Condenser les battements du thread -> Memoire_{Univers}_<n> (livrable 3).
c. FIXER L'ÉTAPE COURANTE (obligatoire à chaque build) : consulter la roadmap en cours et reporter dans ANNEXE_CHRONO > Arcs la roadmap, l'étape et le jalon où reprendra le prochain thread. C'est elle que le thread suivant fetchera.
c2. POSER LE `thread source` (§1, obligatoire à chaque build) : le thread de jeu digéré. Le thread de jeu suivant y lira la fin de la dernière scène pour reprendre en continuité directe.
d. Reporter au Sommaire de jeu toute page Parties/ créée ou écrasée (livrable 2).

Convention de nommage Parties/ :
- Archive narrative : `Memoires/Memoire_{Univers}_<n>.md` (FIGÉE, empilée, sur le dépôt, NON indexée au Sommaire, hors budget de page).
- Mémoire refroidie thématique : `Suivi/<sujet>.md` ou sous-dossier dédié (ÉCRASÉE quand le sujet refroidit davantage).
- Fiche protagoniste : HORS PÉRIMÈTRE du CODEX build. L'état chaud (capacités, description, état) vit dans le CODEX CORE §3. La backstory FROIDE vit en `Suivi/<Nom>_Fiche.md`, créée au V1 et maintenue via BIBLE BUILD - le CODEX build ne la produit ni ne la touche.

## 5. Architecture modulaire

### Sections obligatoires (lues à chaque tour de narration)
- `[CORE - LECTURE OBLIGATOIRE]`
- `[ANNEXE_STYLE - LECTURE OBLIGATOIRE]`

### Sections conditionnelles (lues selon la scène)
- `[ANNEXE_PNJ - si PNJ en scène ou convoqué]`
- `[ANNEXE_LORE - buffer divergences fraiches, vide = sain]`
- `[ANNEXE_CHRONO - si continuite temporelle]`
- `[ANNEXE_INVENTAIRE - si objet en jeu]`
- `[ANNEXE_TCHEKHOV - si fil narratif touche ou plantable]`
- `[ANNEXE_SAVOIRS - si secret, revelation ou asymetrie]`

### Compression chronologique progressive (ANNEXE_CHRONO)
Déclinaison CHRONO du GRADIENT DE FRAÎCHEUR (cf. §2), qui s'applique désormais à TOUTES les sections.
- Thread courant : une ligne par battement (Tour n).
- Thread N-1 : une ligne par scène majeure.
- Threads antérieurs : une ligne par arc résolu.
- Arcs clos sans conséquence ouverte : fusion en ligne narrative unique.
- Quand ANNEXE_CHRONO dépasse 15 000 caractères : archiver les threads anciens dans Parties/, ne garder que les arcs résolus en une ligne (cf. signal d'archivage, section 3).

## 6. Interdictions de forme
- Aucun paragraphe explicatif hors ANNEXE_STYLE.
- Aucune narration.
- Aucune métaphore.
- Aucun micro-geste.
- Aucun dialogue.
- Aucune liste imbriquée au-delà d'un niveau.
- Phrases > 20 mots interdites hors ANNEXE_STYLE.
- Aucune recopie inter-sections.
- Aucune recopie de canon, de BIBLE, de WIKI ou d'instruction non modifié par le RP.

## 7. Audit de compression
Checklist RAPIDE intégrée à la passe de rédaction (pas une étape cérémonielle séparée). Avant de livrer le CODEX, vérifier :
1. Chaque fait n'apparaît qu'une fois dans les sources EN CONTEXTE (CODEX, BIBLE, narration brute, instructions). Pour WIKI/Parties (pages non chargées) : spot-check via Sommaire / Sommaire de jeu sur les seuls faits SUSPECTS de doublon - aucune prétention à vérifier exhaustivement des pages absentes du contexte, aucun fetch sauf si une décision en dépend (cf. 4bis, fetch conditionnel).
2. Le plafond du build est respecte : plafond(N) = min(30 000 + 3 000 x (N-1), 90 000), soit 11 000 stable + cumulatif(N), taille mesurée au `wc -m` (UNE fois) et REPORTÉE dans la métadonnée `taille au build`.
3. Les sections ne se répètent pas : RENVOI SEC appliqué (cf. §2), aucun mécanisme rédigé en toutes lettres dans 2+ sections.
4. Le texte reste exploitable sans thread externe.
5. Tout doute est marque `[INCERTAIN]`.
6. Chaque PNJ actif a un champ voix défini ou `voix: [INCERTAIN]`.
7. Le protagoniste a une nature corporelle explicite en §3a. La règle de perception par PNJ est OBLIGATOIRE seulement si la nature corporelle l'exige (conscience hôte, possession, symbiote, dissimulation, non-humain à perception variable) ; corps propre perçu normalement -> `perception: standard`, le point est satisfait.
8. Les règles de filtrage §4bis et §4ter ont été appliquées.
9. Aucun fait couvert par la BIBLE, le WIKI, Parties/ ou les instructions n'a été dupliqué.
10. ANNEXE_SAVOIRS cohérente avec ANNEXE_PNJ et CORE §4.
11. ANNEXE_LORE ne contient que des divergences fraîches (< 1000 chars). Si elle déborde, formaliser dans la BIBLE via BIBLE BUILD.
12. Aucun pointeur circulaire : chaque `cf.` mène à un emplacement qui CONTIENT le fait, jamais à un autre renvoi (vérif spécifique : §3a Capacités ne renvoie à BIBLE/WIKI que si la cible porte le détail).
13. Capacités stables du protagoniste ancrées en §3a ; aucune capacité durable laissée uniquement en état transitoire (§3b) ou en mémoire éparse. Test de saillance (4bis) appliqué : la couleur narrative est descendue dans la Mémoire, pas conservée dans le CODEX.
14. ANNEXE_TCHEKHOV : fils vivants uniquement ; les fils clos/payés/consumés du build précédent ont été supprimés ; aucune capacité déguisée en fil (cf. 4bis).
15. Gradient de fraîcheur appliqué (cf. §2) : aucun détail fin date de N-2 ou avant hors exceptions (Tchekhov vivants, ancres durables) ; §3a descriptif, zéro exploit.

---

# GABARIT DE SORTIE

# CODEX_NARRATIF_v<N>

## [CORE - LECTURE OBLIGATOIRE]

### §1 Métadonnées
- titre: <titre de la campagne>
- univers: <nom / type>
- régime: canonique | divergence | hybride
- protagoniste: <nom>
- date in-world de reprise: <date>
- date réelle de dernière mise à jour: <AAAA-MM-JJ>
  note: les tampons OOC (§5) et interdits (§6) utilisent [V<n>], pas la date.
- codex_version: V<N>
- plafond: <plafond(N)> car. (barème : min(30 000 + 3 000 x (N-1), 90 000))
- taille au build: <wc -m> car. (<X>% du plafond(N))
- thread source: <titre du thread de jeu digéré par ce build> | <id de son message racine, lisible par lecture de thread> ("aucun" pour le V1 ou hors projet)
- spec au build: SPEC_CODEX v8.9 (source: GitHub | fournie en conversation)
- bible_lore: <nom du fichier BIBLE_LORE si présente, sinon "aucune"> (sans numéro de version)
- dernier sync BIBLE: <B<x> si BIBLE présente, advisory non bloquant ; sinon "n/a">
- wiki_base: <URL racine du WIKI GitHub si présent, sinon "aucun">
- parties_base: <URL racine de Parties/<Univers>/Partie<n>/ si présent, sinon "aucun">

### §2 Prémisse
- <ligne 1>
- <ligne 2>
- <ligne 3>
- <ligne 4>
- <ligne 5>

### §3 Protagoniste
Source vivante de l'INSTANCE jouée : ICI (CODEX) + Parties/Suivi pour la backstory froide. L'instance ne vit pas dans la BIBLE/WIKI ; mais l'ENTITÉ, si elle est du lore (canon ou OC promu), y est décrite à part - cf. SPEC_BIBLE. Capacités ANCRÉES en §3a (jamais re-dérivées).

**§3a Invariants (chaud, stables, changent rarement)**
- Nom / alias :
- Nature corporelle : <corps propre | conscience hôte | possession | symbiote | autre>
- Perception par PNJ : <qui perçoit, comment, limites>
- Description physique : <apparence stable : silhouette, traits, signes distinctifs. PAS l'état du moment (-> §3b)>
- Capacités stables : <pouvoirs durables, ANCRE canonique. Détail complet ici. Règle + limites, ZÉRO exploit ni historique (cf. 4bis). Toute capacité durable démontrée en jeu est promue ici - cf. 4bis>
- Résumé de backstory : <quelques lignes denses, contexte suffisant pour narrer. Backstory complète = Parties/Suivi (froid, fetch à la demande)>
- Valeurs inviolables : <rappel compact>
- Tics / voix : <rappel compact>

**§3b État courant (chaud, transitoire, churn par thread)**
- État physique actuel : <blessures, fatigue, marques du moment>
- État émotionnel actuel : <en 1 ligne>
- Ressources du moment : <objets ponctuels, alliés présents, munitions, mana disponible>
- Contraintes actives : <sceaux, malédictions, limitations temporaires>

### §4 Reprise et état courant
- Lieu :
- Sous-lieu :
- Dernier [REPERE] :
- PNJ présents physiquement :
- Savoir du protagoniste :
- Savoir caché :
- Tension dominante :
- Rapport de force :
- Dernier échange - joueur : <dernière réplique, verbatim> / PNJ : <idem>
- État-clé minimal :
- Prochaine bascule amorcée :

### §5 OOC actifs
- `[V<n>] - <énoncé écrasant le CODEX ou le canon> | sections impactées`  (V<n> = version du CODEX sous laquelle le thread a été joué)

### §6 Interdits accumulés
Pièges identifiés en session, non réintroduits dans les CODEX suivants. Purge au build, avec validation joueur, des interdits INERTES (piège devenu impossible à reproduire : PNJ définitivement mort, arc clos sans héritier).
- `[V<n>] - <interdit 1>`

### §7 #SITES_REF
| Source | URL | Usage |
|---|---|---|
| <nom> | <url> | <quand consulter> |

---

## [ANNEXE_PNJ - si PNJ en scène ou convoqué]

Ne stocker que ce qui diverge du canon ou est spécifique au RP.
Pour le canon non modifié, renvoyer à BIBLE, WIKI ou Parties/.

Champ voix obligatoire pour chaque PNJ actif :
- `voix: muet par défaut`
- `voix: sobre, monosyllabique`
- `voix: lyrique, archaique`
- `voix: <description situee>`
- `voix: [INCERTAIN] - ordre OOC requis avant dialogue`

### Actifs
- <PNJ> - <rôle> | <statut> | <voix> | <relation au protagoniste> | <dernière action> | <inviolable>

### Secondaires
- <PNJ> - <rôle> | <voix> | <relation> | <inviolable>

### Absents / morts
- <nom>, <nom>, <nom>

---

## [ANNEXE_LORE - buffer divergences fraiches]

Divergences du RP apparues en session, pas encore formalisées dans la BIBLE ou le WIKI.
Max 1 000 caractères. Si débordement : déclencher BIBLE BUILD pour formaliser.
Vide = sain.

- <divergence 1>
- <divergence 2>

---

## [ANNEXE_CHRONO - si continuite temporelle]

`Date réelle | Date in-world | Compteur | Événement condensé`

### Thread courant (une ligne par battement)
- <date> | <date IW> | Tour 1 | <événement>
- <date> | <date IW> | Tour 2 | <événement>

### Thread N-1 (une ligne par scène majeure)
- <scène majeure>

### Threads antérieurs (une ligne par arc résolu)
- <arc résolu>

### Fil des arcs (mémoire longue - anti-amnésie)
La suite ORDONNÉE des arcs traversés dans ce RP, du premier joué jusqu'à l'arc courant, puis l'arc suivant prévu. C'est ICI que vit la mémoire du chemin parcouru : en jeu on ne lit pas la BIBLE et la roadmap ne porte que l'arc en cours, donc ce fil est le substitut de mémoire pour la cohérence de fond (cf. SPEC_BIBLE_LORE_WIKI, note ANTI-AMNÉSIE). Une ligne par arc, dans l'ordre de jeu.
`<#> - <Arc> : <issue / état 1 ligne> (détail clos : cf. PARTIES Archives/<page>.md si archive)`
- 1 - <Arc1> : <issue>
- 2 - <Arc2> : <issue>
- ... -> arc courant (cf. section Arcs ci-dessous) -> arc suivant prévu : <Arc suivant>

### Arcs (état courant)
`Arc - enjeu | roadmap: cf. WIKI Roadmap/<Prota>/<page>.md | etape: <n> | jalon courant | statut`
- <arc> - <enjeu> | roadmap: cf. WIKI Roadmap/<Prota>/<page>.md | etape: <n> | <jalon> | <ouvert/suspendu/clos>
- Fixé à chaque build (4ter, triage c). Le thread de jeu suivant fetche CETTE roadmap à l'ouverture et reprend à CETTE étape.

### Mémoire froide
Index de Parties/ : cf. PARTIES Sommaire_Jeu.md (tenu par le build, fetché à l'ouverture).

---

## [ANNEXE_INVENTAIRE - si objet en jeu]

`Objet - localisation | état | porteur | signification narrative`
- <objet> - <localisation> | <état> | <porteur> | <signification>

---

## [ANNEXE_TCHEKHOV - si fil narratif touche ou plantable]

État des fils VIVANTS uniquement (planté / ouvert / actif / armé). Définitions (condition, conséquence) : cf. BIBLE SB8.
Fil clos/payé/consumé : une ligne CHRONO au build de clôture, supprimé de cette annexe au build suivant (cf. 4bis). Les capacités ne sont jamais des fils : elles vivent en §3a (cf. 4bis).

`Fil - statut | dernière interaction`
- <fil 1> - ouvert | <dernière scène/thread où le fil a été touché>
- <fil 2> - armé | <idem>

---

## [ANNEXE_STYLE - LECTURE OBLIGATOIRE]

RECALIBRATION AU BUILD - cette annexe ne se recopie pas d'une version à l'autre par défaut. À chaque build, la confronter au texte RÉELLEMENT écrit :
- Source gratuite, toujours en contexte : la NARRATION BRUTE du thread courant (entrée de build). Comparer ce que l'annexe PRESCRIT à ce qui a été PRODUIT ; écart durable -> l'annexe a dérivé ou la voix a évolué, trancher et réécrire le paragraphe concerné.
- Source conditionnelle : `Parties/{Univers}/Partie<n>/Memoires/Memoire_{Univers}_<n-k>.md` (threads antérieurs), à fetcher SEULEMENT si une dérive de voix est suspectée sur la durée ou si le joueur la signale. Sans cela, on ne remonte pas : la narration brute du thread courant suffit.
- Une annexe recopiée à l'identique sur cinq builds sans confrontation est un fossile, pas une consigne.

<Paragraphe 1 : voix narrative, rythme dominant.>

<Paragraphe 2 : sensorialité privilégiée, images autorisées, densité.>

<Paragraphe 3 : traitement des dialogues, silences, tension de fin.>

---

## [ANNEXE_SAVOIRS - si secret, revelation ou asymetrie]

Matrice d'information : qui sait quoi MAINTENANT dans le RP.

`Secret - qui sait | qui ne sait pas | condition de révélation | conséquence si révélé`
- <secret 1> - <sachants> | <ignorants> | <condition> | <conséquence>

### Ironie dramatique active
- <situation> : <ce que le joueur sait mais pas le PNJ X>

FIN_CODEX_V<N>
