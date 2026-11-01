---
name: "codex-build"
description: "Construit ou met à jour le CODEX_NARRATIF d'un RP (mémoire CHAUDE) selon SPEC_CODEX : CODEX chaud, mémoire refroidie Parties/ et Sommaire de jeu, Mémoire narrative. Déclencheurs : #CODEX_BUILD, \"on fait le codex\", \"génère le V2\"."
---

# CODEX BUILD

Mode outil exclusif. Ce skill ne fait QU'une chose : produire les livrables du CODEX. Aucune narration, aucune invention de fait, aucune prose hors gabarit, aucun commentaire méta superflu. Toute édition de BIBLE, de WIKI ou de roadmap est HORS PÉRIMÈTRE (cf. Frontière de périmètre).

## Thread machinerie : autonomie totale

Le thread de build est un thread de MACHINERIE. Le joueur n'y met pas les pieds : il a donné l'ordre (« codex build ») dans le thread de jeu, et c'est tout. Le build se boucle seul, de bout en bout, sans rien lui demander :

1. lire les entrées (§1), builder les trois livrables (§2), passer l'audit (SPEC §7) ;
2. écrire sur une branche, ouvrir la pull request, la FUSIONNER sur main soi-même, sans validation préalable (`Config/INSTRUCTION_WIKI_GITHUB.md` §8bis, point 7) ;
3. une fois la fusion faite, LANCER AUTOMATIQUEMENT le thread de jeu suivant : demander au coordinateur du projet d'ouvrir un nouveau thread de jeu sur l'univers et la partie buildés, qui repartira du CODEX fusionné sur main (cœur Narration §0) ;
4. poster un seul message de fin dans le thread de build (version du CODEX, étape de reprise, PR fusionnée, thread de jeu lancé, éventuel bloc « À FORMALISER ») et résoudre le thread.

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

`OOC joueur explicite > Narration brute (ce qui s'est passé) > CODEX V(n-1) (état antérieur) > BIBLE (lore statique)`.

Le CODEX NE CRÉE AUCUN FAIT : il reformule, regroupe, compresse ce qui est dans les entrées. Information absente, floue ou contradictoire -> `[INCERTAIN]`.

## 3bis. Écrire à la cible, pas raboter

La SPEC porte le barème de plafond croissant (`plafond(N) = min(30 000 + 3 000 x (N-1), 90 000)`), des budgets-cibles par section et un ordre de rédaction par poids. Rédiger les grosses sections (§3a, §4 ; au cumulatif CHRONO, PNJ) D'ABORD et DIRECTEMENT à leur cible (~5 % sous le plafond). Une seule mesure `wc -m` en fin de build, reportée dans `taille au build`. Section qui déborde : UNE passe de coupe franche, une seule re-mesure, jamais de micro-coupes re-mesurées. Seul le dépassement du PLAFOND DUR se signale au joueur, via le coordinateur (cf. Thread machinerie).

## 4. Promotion et frontière de périmètre

- Capacité ou fait DURABLE démontré en jeu et absent du calque stable -> promu en §3a (Capacités) avec son détail complet (SPEC 4bis), pour ne pas être re-dérivé à chaque thread.
- Fait relevant du lore permanent (BIBLE/WIKI), ou correction de roadmap ou de fiche que le jeu révèle : NE PAS l'écrire ici. Le signaler en fin de build sous un bloc **"À FORMALISER EN BIBLE/WIKI BUILD : ..."**.
- Roadmaps et fiches : LECTURE SEULE. Le CODEX tient l'état d'arc (roadmap, étape, jalon) et pointe la roadmap via `roadmap:`, jamais il ne la réécrit.

## Garde-fou de contexte

Ne jamais builder dans le thread de jeu lui-même : historique saturé (lost-in-the-middle), réflexes de narrateur à réprimer. Le build se fait dans un thread dédié du même projet, qui lit le thread de jeu. Demande de build reçue en pleine narration : le thread de jeu clôt sa scène, pose `[POINT CHARNIÈRE — #CODEX_BUILD + nouveau thread.]` et demande au coordinateur d'ouvrir le thread de build.

## Pas de cas V1

Le V1 naît en fin de worldbuilding (cœur Wiki, MODE OUTIL - CODEX V1), avec son contexte riche. Ce skill part TOUJOURS d'un CODEX V(n-1) existant.

## Vérification de renvoi (fetch CONDITIONNEL, LECTURE SEULE)

`python scripts/fetch_page.py <url blob ou raw>` (script absent : `curl -sL <url raw>`). Échec -> `[FETCH ECHOUE - <page>]`. Ne fetcher QUE si une décision de build en dépend (résolution d'un `cf.`, doublon SUSPECT) ; le doute léger se marque `[INCERTAIN]`, qui coûte moins cher et que le joueur tranchera en jeu s'il le veut.