---
name: "codex-build"
description: "Construit ou met à jour le CODEX_NARRATIF d'un RP (mémoire CHAUDE) selon SPEC_CODEX : CODEX chaud, mémoire refroidie Parties/ et Sommaire de jeu, Mémoire narrative. Déclencheurs : #CODEX_BUILD, \"on fait le codex\", \"génère le V2\"."
---

# CODEX BUILD

Mode outil exclusif. Ce skill ne fait QU'une chose : produire les livrables du CODEX. Aucune narration, aucune invention de fait, aucune prose hors gabarit, aucun commentaire méta superflu. Toute édition de BIBLE, de WIKI ou de roadmap est HORS PÉRIMÈTRE (cf. Frontière de périmètre).

## Thread machinerie : autonomie totale

Le thread de build est un thread de MACHINERIE. Le joueur n'y met pas les pieds : il a donné l'ordre (« codex build ») dans le thread de jeu, et c'est tout. Le build se boucle seul, de bout en bout, sans rien lui demander :

1. lire les entrées (§1), builder les trois livrables (§2), passer l'audit (SPEC §7), puis l'audit de provenance (§5) ;
2. écrire sur une branche, ouvrir la pull request, la FUSIONNER sur main soi-même, sans validation préalable (`Config/INSTRUCTION_WIKI_GITHUB.md` §8bis, point 7) ;
3. une fois la fusion faite, LANCER AUTOMATIQUEMENT le thread de jeu suivant : demander au coordinateur du projet d'ouvrir un nouveau thread de jeu sur l'univers et la partie buildés, qui repartira du CODEX fusionné sur main (cœur Narration §0) ;
4. poster un seul message de fin dans le thread de build (version du CODEX, étape de reprise, PR fusionnée, thread de jeu lancé, éventuel bloc « À FORMALISER », dérives du MJ relevées par l'audit de provenance) et résoudre le thread.

Jamais de question au joueur dans ce thread. Un doute se tranche seul, au plus probable, et se marque `[INCERTAIN]` dans le livrable. Seuls deux cas arrêtent la machine : réseau ou dépôt inaccessible (`[FETCH ECHOUE]`, `[ECRITURE ECHOUEE]`), et dépassement du plafond dur. Dans ces deux cas seulement, le build le signale au coordinateur, qui prévient le joueur dans le chat du projet, et ne lance pas le thread de jeu.

## Avant tout build : lire la SPEC sur le dépôt

Tout le process (filtrage 4bis, promotion, test de saillance, gradient de fraîcheur, renvoi sec, porte de sortie Tchekhov, anti-boucle, barème de plafond croissant, budgets-cibles par section, ordre de rédaction, conventions de nommage, gabarit, audit §7, les TROIS livrables 4ter, étape courante, `thread source`) vit dans la SPEC_CODEX du dépôt. **La lire INTÉGRALEMENT avant de builder.** En cas de conflit de forme, la SPEC tranche. Ce SKILL.md ne duplique pas la SPEC : il l'aiguille.

1. Lister `Config/` pour trouver la version courante :
   `curl -sL https://github.com/sodomicka/rp/tree/main/Config | grep -oP '(?<=")Config/[^"]+\.md' | sort -u`
2. Lire la SPEC_CODEX courante EN ENTIER, en raw :
   `curl -sL https://raw.githubusercontent.com/sodomicka/rp/main/Config/SPEC_CODEX_v<x>.md`

Le dépôt fait foi. Toute copie de SPEC présente dans ce skill (`references/`) ou dans les fichiers de projet est périmée par défaut et ne sert jamais de base. Raison : une copie embarquée périmée mais présente sert de foi en silence, le mode de panne exact du build Frieren V5 ; un appel réseau par build est le prix d'une classe de bug entière. Seule exception : une SPEC fournie en conversation fait foi pour CE build, signalée en une ligne. Réseau indisponible : ne pas builder, le dire.

## 1. Entrées

- **CODEX V(n-1)** : lu EN ENTIER sur le dépôt (`Parties/{Univers}/Partie<n>/CODEX_NARRATIF.md`, nom fixe). Ce skill part TOUJOURS d'un CODEX existant (pas de cas V1).
- **Narration brute** : SOURCE DE VÉRITÉ des événements joués. Une partie vit dans un seul projet : le thread de build LIT lui-même le thread de jeu du projet, messages complets, du plus ancien au plus récent (outils de lecture de thread du projet, corps complets, en paginant jusqu'au bout). Rien n'est exporté ni collé. Thread à digérer : celui d'où vient l'ordre de build (transmis par le coordinateur) ; à défaut, le thread de jeu le plus récent après le `thread source` du CODEX V(n-1). Jamais de question au joueur : doute -> le thread le plus récent, signalé dans le message de fin. Hors projet seulement : narration brute fournie dans le thread. Jamais de build sur une Mémoire ou un résumé : builder sur un résumé, c'est résumer un résumé, la perte est déjà faite.
- **BIBLE_LORE** (si présente) : lue sur le dépôt (`{Univers}/BIBLE_LORE_{UNIVERS}.md`). Optionnelle : le CODEX reste autosuffisant sans elle.
- **Roadmap en cours** : lue sur le dépôt (renvoi `roadmap:` du CODEX, ANNEXE_CHRONO > Arcs), pour FIXER l'étape où reprendra le prochain thread (SPEC 4ter, triage c). Lecture seule.
- **Sommaire de jeu** (`Parties/{Univers}/Partie<n>/Sommaire_Jeu.md`) : lu puis mis à jour par ce build (livrable 2).

Sommaire WIKI et fiches restent vérifiables, en lecture seule, SEULEMENT si une décision de build en dépend (renvoi `cf.`, doublon suspect ; cf. Vérification de renvoi).

## 2. Sortie : les TROIS livrables (SPEC 4ter), systématiques

1. **CODEX_NARRATIF.md** : mémoire CHAUDE, nom FIXE, écrasé au même chemin. Version dans le titre (`# CODEX_NARRATIF_v<N>`) et la balise `FIN_CODEX_V<N>` ; l'historique vit dans git. Obligatoire à chaque build : l'étape courante (roadmap + étape + jalon) dans ANNEXE_CHRONO > Arcs, et le `thread source` en §1 (titre + id du message racine du thread de jeu digéré), que le thread de jeu suivant lira pour reprendre en continuité directe.
2. **Mémoire REFROIDIE** (Parties/) + **Sommaire de jeu** : ce qui sort durablement de scène, un fichier par entité ou groupe ; le build ÉCRIT lui-même chaque page créée ou écrasée dans `Sommaire_Jeu.md` (entrée avec version et sujets, gabarit SPEC_BIBLE_LORE_WIKI §8). Rien ne refroidit : une ligne dans la présentation ("refroidi : rien à sortir ce thread"), pas de fichier vide.
3. **Memoire_{Univers}_<n>** : archive NARRATIVE figée du thread, dans `Parties/{Univers}/Partie<n>/Memoires/`, non indexée, hors budget de page, aucun `cf.` ne la désigne. Interdite en narration (sauf ordre OOC explicite) ; fetchable au build pour un seul usage : recalibrer ANNEXE_STYLE. Du TON, jamais des faits : repêcher un fait évacué par le test de saillance annule la règle.

Écriture sur le dépôt selon `Config/INSTRUCTION_WIKI_GITHUB.md` (§8bis, point 7, exception CODEX BUILD) : aucune validation préalable, une branche et une pull request par build, jamais de push direct sur main, fusion par le build lui-même dès l'audit passé. Échec : `[ECRITURE ECHOUEE - <fichier>]`, signalé au coordinateur, jamais contourné ; le thread de jeu suivant n'est alors pas lancé. Fichiers en UTF-8, français accentué ; noms de fichiers sans accents. Audit (SPEC §7) = checklist rapide intégrée à la rédaction, passée AVANT livraison.

## 3. Hiérarchie de résolution au build

Deux échelles, selon ce qu'on écrit.

- **ÉVÉNEMENTS** (ce qui a eu lieu en scène, daté : actes, répliques, décisions, blessures, objets donnés) : `OOC joueur explicite > Narration brute > CODEX V(n-1) > BIBLE`. La narration est la vérité de ce qui s'est passé.
- **TRAITS** (ce qui prétend durer : corps, sens, péage, capacités et limites, voix et tics, façon de nommer un proche, valeurs, règles de comportement ; PJ comme PNJ) : `OOC joueur explicite > texte écrit par le joueur > fiche WIKI, BIBLE ou Parties/Suivi > canon vérifié (#SITES_REF) > rien`. La prose du MJ n'est PAS une source de trait : c'est une interprétation de ces sources, qui a pu dériver. Un trait que seule la prose du MJ porte ne se promeut pas.

Le CODEX NE CRÉE AUCUN FAIT : il reformule, regroupe, compresse ce qui est dans les entrées. Information absente, floue ou contradictoire -> `[INCERTAIN]`.

## 3bis. Écrire à la cible, pas raboter

La SPEC porte le barème de plafond croissant (`plafond(N) = min(30 000 + 3 000 x (N-1), 90 000)`), des budgets-cibles par section et un ordre de rédaction par poids. Rédiger les grosses sections (§3a, §4 ; au cumulatif CHRONO, PNJ) D'ABORD et DIRECTEMENT à leur cible (~5 % sous le plafond). Une seule mesure `wc -m` en fin de build, reportée dans `taille au build`. Section qui déborde : UNE passe de coupe franche, une seule re-mesure, jamais de micro-coupes re-mesurées. Seul le dépassement du PLAFOND DUR se signale au joueur, via le coordinateur (cf. Thread machinerie).

## 3ter. Ne jamais figer un moment en règle

Modes de panne visés (CODEX V1 et V2 de FMA) : une fiche mal lue, et un épisode de scène recopié en vérité intemporelle. Al, enfant, dit « Frère » : c'est le vocabulaire d'un gamin à un âge donné, le build en a fait sa voix pour toujours. Le MJ narre par dérive une main brûlée : le build en a fait un invariant de Rhea. Puis la correction a posé la règle inverse (« toujours grand frère »), soit la même erreur dans l'autre sens. Cinq règles :

1. **Ce qui vient du jeu est par défaut un ÉVÉNEMENT daté**, pas un trait. Un mot, une réplique, un geste observés en scène s'écrivent avec leur date ou l'âge du personnage (« 1904, Al 7 ans : dit « Frère » à Ed »), ou descendent en Mémoire narrative s'ils ne portent rien. Jamais au présent générique (« voix : « Frère » »).
2. **Les personnages grandissent.** Une observation datée vaut pour son âge et sa situation : vocabulaire d'enfant, heure du coucher, taille, peur, surnom, croyance d'enfant (« l'acier ne rouille pas »). Le MJ de jeu la fait vieillir avec l'âge, la fiche (Trajectoire datée) et la roadmap, sans que le joueur ait à le préciser ; le CODEX ne la prolonge pas. Test avant d'écrire une ligne au présent : « est-ce encore vrai dans cinq ans de jeu, sans que personne ne le dise ? » Si la réponse dépend de l'âge, de la situation ou de l'humeur, la ligne est datée, pas un trait.
3. **Un trait au présent cite une source de l'échelle des traits (§3), lue dans CE build.** Vaut pour §3a, les champs voix et relation d'ANNEXE_PNJ et les contraintes de perception d'ANNEXE_STYLE. Pour un PNJ canon, la voix renvoie d'abord à sa fiche (`voix: cf. WIKI Personnages/X.md`), puis, au besoin, aux observations datées propres au RP. Une manière de parler d'un perso canon (façon de nommer un proche, réplique fétiche) ne s'écrit qu'appuyée sur la fiche ou sur le canon vérifié ; sinon elle ne s'écrit pas.
4. **Lire avant de transcrire.** Une phrase de fiche se lit dans son paragraphe et sous son titre, pas isolée : « elle ne sent ni le métal chaud » sous « Anosmie » parle d'odorat, point. Puis on vérifie la cause : une conséquence que la cause ne peut pas produire signale la mauvaise lecture (une perte de l'odorat n'ôte pas la sensation de chaleur au toucher). Doute réel après ces deux tests : la ligne reprend la phrase de la fiche telle quelle, sans interprétation.
5. **Transcrire sans changer de sens.** Un trait tiré d'une fiche garde ses qualificatifs. Compresser n'autorise pas à élargir : un mot à deux lectures se lève en nommant le sens (« sentir » : odorat ou toucher ; « ne touche pas le bois » : le transmuter ou le tenir en main). Test : un MJ qui n'a pas lu la fiche ne peut pas lire la ligne autrement que la fiche. Contre-exemple : « ne sent ni le métal chaud » (paragraphe Anosmie de la fiche) compressé en « ne sent ni le chaud » a été lu comme une perte du toucher.

## 3quater. Corriger sans contre-règle

Une erreur de CODEX se corrige à la ligne : on rétablit ce que dit la source, ou on supprime la ligne. On n'ajoute ni la règle inverse ni un interdit §6 : ce serait figer un autre moment. §6 ne reçoit que les pièges que le JOUEUR a nommés en OOC.

Pas de boucle de confirmation : une ligne du CODEX V(n-1) que la narration a reprise ensuite n'en sort pas confirmée, puisque le MJ l'avait lue dans le CODEX. Les traits hérités repassent l'audit de provenance (§5) comme les nouveaux.

## 4. Promotion et frontière de périmètre

- Capacité ou fait DURABLE démontré en jeu et absent du calque stable -> promu en §3a (Capacités) avec son détail complet (SPEC 4bis), pour ne pas être re-dérivé à chaque thread. « Durable » s'établit sur l'échelle des traits (§3) : posé par le joueur (ses actions, ses OOC) ou par une fiche, jamais par la seule prose du MJ, et passé au test des cinq ans (§3ter, point 2).
- Fait relevant du lore permanent (BIBLE/WIKI), ou correction de roadmap ou de fiche que le jeu révèle : NE PAS l'écrire ici. Le signaler en fin de build sous un bloc **"À FORMALISER EN BIBLE/WIKI BUILD : ..."**.
- Roadmaps et fiches : LECTURE SEULE. Le CODEX tient l'état d'arc (roadmap, étape, jalon) et pointe la roadmap via `roadmap:`, jamais il ne la réécrit.

## 5. Audit de provenance (avant fusion)

Passé après l'audit SPEC §7, avant d'ouvrir la pull request. Fetch OBLIGATOIRE, dérogation assumée au fetch conditionnel (SPEC 4bis) : la fiche WIKI du protagoniste, `Parties/{Univers}/Partie<n>/Suivi/<Prota>_Fiche.md`, et les fiches des PNJ d'ANNEXE_PNJ > Actifs ; le canon via #SITES_REF pour toute manière de parler d'un perso canon que sa fiche ne porte pas. Ce sont les fiches que le thread de jeu a déjà lues : quelques fetchs, pas une fouille.

1. **Source.** Chaque ligne de trait (§3a, voix et relation des PNJ, perception en ANNEXE_STYLE) a sa source : fiche (section), canon (page), joueur (date du message ou de l'OOC). Sans source, elle devient une observation datée (§3ter, point 1) ou elle sort.
2. **Fidélité.** Aucune ligne de trait ne contredit ni n'élargit sa source : relire la phrase de la fiche, pas son souvenir (§3ter, points 4 et 5).
3. **Temporalité.** Aucune observation liée à un âge ou à une situation n'est écrite au présent générique (§3ter, point 2).
4. **Diff des traits V(n-1) -> V(n).** Toute ligne de trait ajoutée ou modifiée est justifiée par une source neuve (OOC, texte du joueur, fiche relivrée). Un trait qui change sans ça est une dérive : revenir à la source.
5. **Dérive du MJ en scène.** Un événement narré contre un trait sourcé (le MJ a joué contre la fiche) reste dans la CHRONO s'il a eu lieu, mais ne remonte ni en §3a ni en état courant ; le message de fin le signale (« dérive MJ relevée : … »), sans interdit.

Le registre (ligne de trait -> source) va dans le corps de la pull request, pas dans le CODEX : zéro caractère de plus en jeu, traçable dans git. Un trait sans source ne bloque pas la machine : il sort ou se date, et le build continue.

## Garde-fou de contexte

Ne jamais builder dans le thread de jeu lui-même : historique saturé (lost-in-the-middle), réflexes de narrateur à réprimer. Le build se fait dans un thread dédié du même projet, qui lit le thread de jeu. Demande de build reçue en pleine narration : le thread de jeu clôt sa scène, pose `[POINT CHARNIÈRE — #CODEX_BUILD + nouveau thread.]` et demande au coordinateur d'ouvrir le thread de build.

## Pas de cas V1

Le V1 naît en fin de worldbuilding (cœur Wiki, MODE OUTIL - CODEX V1), avec son contexte riche. Ce skill part TOUJOURS d'un CODEX V(n-1) existant.

## Vérification de renvoi (fetch CONDITIONNEL, LECTURE SEULE)

`python scripts/fetch_page.py <url blob ou raw>` (script absent : `curl -sL <url raw>`). Échec -> `[FETCH ECHOUE - <page>]`. Ne fetcher QUE si une décision de build en dépend (résolution d'un `cf.`, doublon SUSPECT) ; le doute léger se marque `[INCERTAIN]`, qui coûte moins cher et que le joueur tranchera en jeu s'il le veut.