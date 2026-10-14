# BIBLE_LORE_LOP - Lies of P

- version : B10
- univers : Lies of P (Neowiz / Round8 Studio, 2023) + DLC Overture
- source canon : transcript vidéo "complete story of Lies of P" (base game + DLC)
- régime canonique : canon principal interprété (narrateur vidéo). Tout fait absent = [INCERTAIN].
- régime RP/OC : depuis B4, la couche RP (OC, divergences assumées) est tissée INLINE dans les SB, balisée [DIVERGENCE RP], par-dessus le socle canon. Le canon pur reste la base ; la divergence se greffe, jamais ne la masque.
- date réelle de dernière mise à jour : 2026-10-13
- note B6 : (1) retrait de l'apparat coquilles transcript ; suppression de _Table_Noms_Canon.md ; SB9.5 ne renvoie plus à la table. (2) francisation des noms anglais selon la loc FR officielle, propagée à tout le wiki + roadmaps (noms propres et noms de fichiers inchangés).
- note B7 : intégration du duo Claudia Volfe (la Renarde Rousse) / Lucio Volfe (le Chat Noir) en SB7. Personnages canon (Red Fox / Black Cat) désormais dotés d'une fiche commune dédiée (Personnages/Claudia_et_Lucio.md) ; le détail (filiation Volfe légitime/bâtard, double-jeu Bâtards/Balayeurs, règle du coeur pur pour le Fruit d'Or, trajectoire jusqu'en 1851) vit dans la fiche.
- note B8 : BIBLE BUILD de clôture des forages 5.1 et 5.2 (dettes I14 soldées). (1) SB3, SB4 : Workshop Union -> Parlement des Artisans (SB4 uniformisé avec SB3) ; Venigni Works -> Fabrique Artisanale Venigni. (2) SB0 mis aux normes S8 : raw_base et parties_raw_base stockés, fetch en raw par défaut, inventaire des pages rattachées. (3) SB5 : [DIVERGENCE RP] entrée de P à l'Hôtel Krat sans mensonge (Humanity System). (4) Coquilles (SB2, SB6). (5) Francisation VF (décision worldbuilder) : RÔDEURS (VO : Stalkers), BÂTARDS (VO : Bastards), BALAYEURS (VO : Sweepers) en SB4. (6) Réaccentuation de tout LOP/ : fin de la règle ASCII (décision worldbuilder) ; en-tête et SB9.5 mis à jour. (7) Francisation VF lot 2 : glossaire validé par le worldbuilder (lots A, B, C), la VO gardée en glose à la première mention.
- note B9 : BIBLE BUILD de clôture du forage 5.3 (Le Roi des Pantins). (1) SB0 : 36 pages Personnages (+ Pinocchio_chrono_A, satellite de P). (2) SB1.7 : [DIVERGENCE RP] Magnus hors du Grand Covenant, comme les Pantins de l'Arc (propagé depuis Magnus.md). (3) SB5 : visage de Carlo, signature et mémoire musculaire de Léa sur P ; règle du coeur pur pour le Fruit d'Or. (4) SB7 : fin de Romeo réécrite (suicide, 1852) ; plus d'Arlecchino en 1852.
- note B10 : BIBLE BUILD de clôture du forage 5.4 (La Vérité de Geppetto). (1) SB0 : 37 pages Personnages (+ Hugo) ; budgets de fiche (SPEC v8.9) : Markiona inscrite en pivot (plafond 30k), aux côtés des protagonistes P et Magnus. (2) SB5 : [DIVERGENCE RP] téléportation des Stargazers réservée à P. (3) SB7 : Alidoro / Parrot, renvoi vers Hugo.

> Cette BIBLE est la couche de fondation (Passe 0) de la couche canon LOP. Elle pose le socle partagé
> par toutes les fiches noyau (Passe 1). Un fait = un seul emplacement canonique ; les fiches renvoient
> ici plutôt que de redupliquer. Français accentué ; noms de fichiers et de dossiers en ASCII.

## SB0 - Identité de l'univers

- Titre : Lies of P. Soulslike (2023), Neowiz / Round8 Studio. DLC : Overture (événements antérieurs au base game).
- Source littéraire : "Les Aventures de Pinocchio" (Carlo Collodi, 1883), Toscane, Italie. Adaptation libre.
- Cadre esthétique : Belle Époque (1871-1914), âge d'or de la civilisation européenne.
- Lieu central : la cité fictive de Krat, ancienne ville côtière pauvre devenue métropole prospère grâce à l'Ergo, puis ravagée par deux fléaux simultanés : la Frénésie des Pantins (pantins devenus hostiles) et la Maladie de Pétrification (maladie pétrifiante).
- Protagoniste : Pinocchio (P), pantin à Ego éveillé, créé par Geppetto.
- Budgets de fiche (SPEC v8.9) : plafond propre de 30k pour les protagonistes, Pinocchio et Magnus [DIVERGENCE RP], et pour le pivot désigné par le worldbuilder, Markiona [DIVERGENCE RP]. Toute autre page : 12k.
- Thème central : l'humanité acquise par le mensonge et le libre arbitre ; la frontière entre pantin et humain.

### Routage WIKI / Parties (accès GitHub, cf. S8 de l'INSTRUCTION)
- wiki_base : https://github.com/sodomicka/rp/blob/main/LOP/
- raw_base : https://raw.githubusercontent.com/sodomicka/rp/main/LOP/
  (racine du WIKI. On fetche en raw, on cite en blob. URL d'une page = base + dossier + fichier. Ex. : raw_base + "Personnages/Markiona.md".)
- sommaire : https://github.com/sodomicka/rp/blob/main/LOP/Sommaire.md
  (carte de navigation du WIKI et des Parties ; point d'entrée pour localiser toute page.)
- parties_base : [INCERTAIN - aucun RP en cours. Forme attendue au lancement : https://github.com/sodomicka/rp/blob/main/Parties/LOP/Partie<n>/ ; valeur à fixer quand une Partie<n> est ouverte.]
- parties_raw_base : [INCERTAIN - idem. Forme attendue : https://raw.githubusercontent.com/sodomicka/rp/main/Parties/LOP/Partie<n>/]
- Filet de fetch : raw par défaut (markdown brut, sans parsing). Secours : page blob + parser (S8, méthode 4) si le raw revient vide ou inaccessible.
- pages wiki rattachées :
  - Personnages - fiches noyau des personnages, canon et OC (Magnus), et satellites de Magnus, Markiona et Pinocchio (chrono, relations) (37 pages)
  - Creatures - boss et créatures notables, fiche groupée (1 page)
  - Lieux - Krat et ses lieux, dont Aurus [DIVERGENCE RP] (12 pages)
  - Factions - Alchimistes, Rôdeurs, Confrérie des Lapins Noirs, Parlement des Artisans (4 pages)
  - Systemes - Ergo, Grand Covenant, Pétrification, Frénésie, Oreilles (VO : Listeners), etc. (11 pages)
  - Objets - objets et reliques, fiche groupée (1 page)
  - Roadmap/Magnus/ - roadmaps par ère, non indexées au Sommaire : sources de build, jamais fetchées en narration

## SB1 - Vérités fondatrices du monde

1. L'ERGO est l'essence de la vie humaine, l'âme (ou sa manifestation) qui quitte le corps à la mort. Normalement il ascende ; piégé dans le minéral Crowd, il se cristallise. C'est à la fois la source d'énergie, la monnaie et la matière première des pantins de Krat.
2. Le CROWD est un minéral inorganique découvert ~600 ans avant le jeu dans un gouffre (la Relique de Trismegistus) sous Krat. Il absorbe et emprisonne l'Ergo. La Relique est une immense mine d'Ergo ; l'Hôtel Krat est bâti au-dessus.
3. Les PANTINS (puppets) sont alimentés par l'Ergo et liés au code GRAND COVENANT. Ils développent un EGO (conscience) au contact prolongé de l'Ergo. Cet éveil de l'Ego est le coeur de l'intrigue.
   - [DIVERGENCE RP] Exception unique à l'éveil-par-contact : un Ego peut naître INNÉ et VIERGE, sans contact prolongé, si le pantin est animé par un Ergo d'une pureté extrême JAMAIS habité par un ego auparavant (l'intensité de l'Ergo remplace la durée du contact). Magnus (OC) est le seul cas connu dans tout le monde. À NE PAS confondre avec un Ergo contenant déjà un ego (ex. l'Ergo de Carlo dans P, ou le cristal de Camille) : celui-là porte une identité, donc un ego emprunté, pas vierge. cf. Personnages/Magnus.md, SB8, Systemes/Genies_et_Chef_D_Oeuvres.md.
4. La MALADIE DE PÉTRIFICATION (VO : Petrification Disease) provient des spores d'Ergo manipulées par les Alchimistes. Les faux "remèdes" l'aggravent : les malades deviennent des CARCASSES.
5. Les OREILLES (écouteurs) sont des humains capables de communiquer avec l'Ergo (l'essence humaine piégée) et de manipuler le temps. Sophia Monad est l'Oreille du jeu ; sa mort/mutation alimente la boucle temporelle du gameplay (rewind à chaque mort de P).
6. LE BRAS DE DIEU (VO : Arm of God) est une relique ancienne ; réveiller le "dieu" (le Star/ange tombé) via cette relique est le but suprême des Alchimistes.
7. MENSONGE = humanité. Le Grand Covenant interdit aux pantins de mentir et de tuer des humains. Pinocchio en est exempté : mentir le rend progressivement humain.
   - [DIVERGENCE RP] Magnus n'y obéit pas non plus, comme tous les Pantins de l'Arc de Markiona. Ni lui ni P ne savent rien de la Loi Zéro avant que Venigni décode le message de Romeo (1852). cf. Personnages/Magnus.md.

## SB2 - Théologie alchimique (le Star et l'Ange à une Aile)

- Croyance : un "star" / ange descendit sur Terre sous forme humaine, voulant offrir l'immortalité après avoir entendu les voeux des humains. Le don fut décevant ; le dieu fut déchiré.
- Hypothèse : ce dieu vint peut-être sous forme de météorite de Crowd = la toute première source d'Ergo.
- Réveiller ce dieu via le Bras de Dieu = objectif premier des Alchimistes. Motto de l'Ordre : "wake up, evolve, ascend" (s'éveiller, évoluer, ascender).
- Symbole : l'OUROBOROS (serpent se mordant la queue) = cycle d'éternité, naissance-vie-mort, fin = nouveau commencement.
- La Cathédrale St Frangelico fut fondée, selon la légende, quand St Frangelico rencontra l'Ange à une Aile. Andreas, en mutant, se proclame lui-même l'Ange à une Aile.

## SB3 - Histoire de Krat (du général au particulier)

- Passé lointain : Krat = ville côtière pauvre, dirigée par des ANCIENNES LIGNÉES (caretakers privilégiés, possessions transmises par générations).
- ~600 ans avant le jeu : effondrement du sol -> découverte du cluster inorganique, de corps, et du Crowd. Le puits est nommé Relique de Trismegistus.
- Arrivée des Alchimistes (fondés par Valentinus Monad) : d'abord à Village Clair-de-Lune, puis contrôle de la Relique. Krat passe du charbon à l'Ergo ; les mines de charbon ferment et deviennent le Marais Aride.
- Geppetto (Parlement des Artisans) + famille Venigni (Fabrique Artisanale Venigni) produisent en masse les pantins. Ergo = énergie + monnaie. Krat devient un hub d'innovation. Pouvoir des anciennes lignées décline face aux Alchimistes et au Parlement des Artisans.
- La Grande Exposition devait montrer au monde le futur de l'automation et l'Ergo. Elle n'aura jamais lieu (annulée à cause de la maladie ; voir DLC).
- Chute : mort de Camille (épouse de Geppetto) ; éveil de l'Ego des pantins ; expériences alchimiques sur l'Ergo -> Maladie de Pétrification ; schisme Simon/Valentinus ; Bataille de la Tour des Artisans ; Frénésie des Pantins déclenchée par Geppetto via Romeo. Krat s'effondre.

## SB4 - Factions

- ALCHIMISTES (VO : Alchemists ; l'Ordre) : mystiques, médecins et scientifiques, quête de la vie éternelle. Fondateur Valentinus Monad. Basés à l'Abbaye de l'Arche, Allée des Alchimistes (terre étrangère, île = lieu le + efficace au monde pour les ondes d'Ergo). Scission : Simon Manus prend le contrôle, excommunie/élimine les loyaux à Valentinus.
- PARLEMENT DES ARTISANS (VO : Workshop Union) : techniciens horlogers, menés par Geppetto, alliés à la famille Venigni et à sa Fabrique Artisanale Venigni (VO : Venigni Works). Fabriquent les pantins. NB : Geppetto pratique l'alchimie par méthode/nécessité mais n'est PAS membre de l'Ordre (cf. Giuseppe_Geppetto.md).
- RÔDEURS (VO : Stalkers) : protecteurs/chasseurs de Krat, deux factions :
  - BÂTARDS (VO : Bastards ; nobles familles, motto "honor or nothing", menés par Lumacchio, gardes des Alchimistes).
  - BALAYEURS (VO : Sweepers ; issus des ruelles, motto "we always repay what is owed", menés par Véronique, installaient les Stargazers).
  Décimés à la Bataille de la Tour des Artisans ; survivants devenus fous, criminels ou alliés des Alchimistes.
- CONFRÉRIE DES LAPINS NOIRS (VO : Black Rabbit Brotherhood) : gang de rôdeurs survivants ; extorsion/protection ; voleurs de corps pour les Alchimistes (extraction d'Ergo). Probablement issu du système de "choix de voie" de la Maison de Charité Monad.
- MONAD FAMILY : famille riche et influente ; fonde la Maison de Charité Monad (éducation des enfants pauvres selon 3 voies : rôdeur, alchimiste, technicienne des artisans (VO : workshop technician)).

## SB5 - Systèmes et mécaniques

- ERGO : voir SB1. Sa qualité se dégrade à cause des expériences alchimiques -> défauts dans les pantins.
- GRAND COVENANT : code gravé dans les pantins. Premier Commandement : tout pantin obéit aux ordres de son créateur. LOI ZÉRO : "le nom du créateur est Geppetto" (exécutée par Geppetto pour déclencher la Frénésie).
- ORGANE-P (VO : P-Organ) : organe-coeur de pantin conçu par Geppetto, stocke et amplifie l'Ergo. Implanté avec succès dans Pinocchio (échec dans le Pantin sans Nom).
- MÉTHODE DU DIABLE : procédé de Geppetto pour transformer un corps humain (mourant ou mort) en pantin en préservant l'Ergo. Preuve canon : Romeo (humain -> Roi des Pantins). cf. Giuseppe_Geppetto.md, Personnages/Romeo.md. [DIVERGENCE RP] Appliquée à Pinocchio : un châssis de pantin de guerre recouvert de chair humaine d'emprunt (la peau de Léa Florence Monad), animé par l'Ergo de Carlo, avec un bras gauche mécanique (Bras Légion) servant de leurre ostensible. P est ainsi indiscernable d'un humain : il a le visage de Carlo, mais la peau garde la signature de Léa (yeux bleus, taches de rousseur) et sa mémoire musculaire, si bien que P se bat comme elle. cf. Pinocchio.md, Lea_Florence_Monad.md, Systemes/Genies_et_Chef_D_Oeuvres.md.
- SYSTÈME D'HUMANITÉ (VO : Humanity System) : mentir, écouter de la musique, choix moraux -> humanité croissante de P (coeur qui bat, chaleur, cheveux qui poussent et grisonnent = éveil de l'Ego de Carlo). Conditionne la fin.
  - [DIVERGENCE RP] P entre à l'Hôtel Krat SANS mentir (Magnus négocie l'entrée, Markiona humaine les accompagne) : son éveil ne s'ouvre pas par le mensonge mais aussi par d'autres vecteurs, d'abord le modèle familial du duo Magnus / Markiona. Le mensonge reste un vecteur. cf. Personnages/Pinocchio.md.
- STARGAZERS : invention des rôdeurs ; téléportation, absorption des spores d'Ergo (zones sûres temporaires), indicateur de la boucle temporelle (cadrans de l'Hôtel Krat). Stargazer doré (VO : golden Stargazer) = voyage temporel (DLC).
  - [DIVERGENCE RP] La téléportation est réservée à P (décision worldbuilder ; sinon, pas d'Overture) : Magnus et Markiona vont à pied ou en tram. cf. Systemes/Stargazers.md, Lieux/Krat.md (Géographie du RP).
- MALADIE DE PÉTRIFICATION : voir SB1. Écailles, perte de la voix/vue, mutation en Carcasse.
- OREILLES / ARBRE À FRUITS D'OR (VO : Gold Coin Tree) : les Oreilles peuvent être transformées en Arbre à Fruits d'Or (arbre dont les fruits, Fruit d'Or, contrôlent l'Ergo). Selon Sophia : "les larmes tristes de ceux devenus arbres".
  - [DIVERGENCE RP] Règle du coeur pur : tout le monde peut approcher l'arbre, mais seuls P et Magnus peuvent cueillir ; les autres s'y brûlent. Les Alchimistes n'ont jamais eu de vrai fruit, seulement un ersatz. Giangio tire du fruit le remède d'Antonia (canon). cf. Systemes/Gold_Coin_Tree.md.

## SB6 - Chronologie canon (repères datables ou ordonnables)

- T-600 ans : découverte du Crowd et de la Relique de Trismegistus.
- Arrivée des Alchimistes ; transformation de Krat (du charbon à l'Ergo).
- Production de masse des pantins (Geppetto + Venigni) ; âge d'or de Krat.
- ~30 ans avant le jeu : Andreas nommé prêtre de St Frangelico.
- Mort de Camille ; éveil de l'Ego de Camil (le pantin-servante portant l'Ergo de Camille) ; début des expériences sur les Oreilles et de l'intérêt alchimique pour l'immortalité.
- Mort de Carlo (Maladie de Pétrification à la Maison de Charité) ; début du plan de résurrection de Geppetto.
- Schisme Simon/Valentinus ; prime sur Léa Florence ; excommunication de Valentinus ; assaut de Simon (mort de Valentinus et Isabelle ; Sophia capturée).
- DLC Overture : voyage temporel de P (avant l'annulation de la Grande Exposition). Mort de Véronique, du Surveillant aux Deux Visages, de Lumacchio, du Gardien Tourmenté, d'Arlecchino ; mort de Léa (par le Pantin sans Nom) ; capture de Romeo par Geppetto. NB : P est rappelé au présent AVANT l'arrivée de Geppetto au Domaine de la Rose ; il n'assiste pas aux morts de Romeo et Léa (cf. Pinocchio.md).
- Bataille de la Tour des Artisans : effondrement (shards de Crowd) ; décimation des rôdeurs.
- Romeo transformé en pantin ; Loi Zéro ; Frénésie des Pantins ; Romeo devient Roi des Pantins et se rebelle.
- Base game : réveil de P à la Gare Centrale (VO : Krat Central Station) ; trame principale jusqu'aux fins.
- Post-crédits : Paracelsus dans le train ; teaser Dorothy (sequel).

## SB7 - Personnages-pivots (renvois)

- Pinocchio (P) : protagoniste. cf. Personnages/Pinocchio.md
- Giuseppe Geppetto : créateur, antagoniste caché (Loi Zéro, Frénésie). cf. Personnages/Giuseppe_Geppetto.md
- Simon Manus : antagoniste principal (ascension divine). cf. Personnages/Simon_Manus.md
- Sophia Monad : Oreille, "Fée bleue". cf. Personnages/Sophia_Monad.md
- Romeo : Roi des Pantins, ami de Carlo. [DIVERGENCE RP] Ami de Magnus (Ère 2). À l'Opéra (1852), Magnus le reconnaît et l'étreint ; Romeo reconnaît Léa dans la chair de P et se donne la mort. cf. Personnages/Romeo.md
- Carlo / Camille : fils et épouse de Geppetto, moteurs de l'intrigue. cf. Personnages/Carlo.md, Camille.md
- Valentinus / Léa Florence Monad : fondateur de l'Ordre / Rôdeuse Légendaire. cf. fiches dédiées.
- Arlecchino : pantin meurtrier (DLC), détruit en 1850 au Domaine de la Rose. [DIVERGENCE RP] Plus d'Arlecchino en 1852 : le "Roi des Énigmes" et ses cabines du base game sont caducs (décision worldbuilder). cf. Personnages/Arlecchino.md
- Markiona / Lumacchio / Véronique : pivots DLC. cf. fiches dédiées.
- Philip Paracelsus (= Giangio) : alchimiste caché, fil du sequel. cf. Personnages/Philip_Paracelsus.md
- Alidoro / Parrot : le Traqueur (VO : Tracker) / faux Alidoro. [DIVERGENCE RP] Alidoro, ami de Magnus, qui démasque Parrot à la voix (1852) et apprend l'imposture à Hugo, futur Traqueur. cf. Personnages/Alidoro_et_Parrot.md, Hugo.md
- Claudia Volfe (la Renarde Rousse) / Lucio Volfe (le Chat Noir) : demi-fratrie de rôdeurs (le Renard et le Chat de Collodi) ; bases canon + [DIVERGENCE RP] (double-jeu Bâtards/Balayeurs, règle du coeur pur pour le Fruit d'Or). cf. Personnages/Claudia_et_Lucio.md
- [DIVERGENCE RP] Magnus (OC) : pantin parfait de Markiona, Ego inné et vierge (né d'un Ergo pur). cf. Personnages/Magnus.md
- [DIVERGENCE RP] Miroir créateur/créature (Geppetto/P vs Markiona/Magnus ; le deuil comme moteur). cf. Systemes/Genies_et_Chef_D_Oeuvres.md

## SB8 - Échelles de puissance (tiers indicatifs, source-only)

> Indicatif et dérivé de la difficulté/narration de la source ; non chiffré par le jeu. [INTERPRÉTATION].
- Sommet (entités divines/uniques) : Simon Manus (Dieu Éveillé), Bras de Dieu / le Star, Gardien Tourmenté (ancien).
- Très haut (boss majeurs) : Laxasia la Complète, Pantin sans Nom, Arlecchino, Roi des Pantins (Romeo), Markiona.
- Haut : Léa Florence Monad (Rôdeuse Légendaire), boss-pantins de Romeo (Maître du Défilé, Veilleur Désarticulé, Fuoco), Champion Victor, Monstre Vert du Marais.
- Intermédiaire : Confrérie des Lapins Noirs (older brother), Marcheur d'Illusions, Surveillant aux Deux Visages, Prédateur Tyrannique, Véronique, Lumacchio (mute).
- Protagoniste : Pinocchio, monte en puissance via l'Ergo accumulé et l'Organe-P ; renforcé par Sophia.
- [DIVERGENCE RP] Protagoniste (OC) : Magnus, au niveau de Pinocchio. cf. Personnages/Magnus.md, Personnages/Markiona.md.

## SB9 - Règles d'or de la couche canon LOP

1. Cette BIBLE et les fiches font loi ; priment sur le canon externe du jeu en cas de conflit avec la source.
2. Un fait = un seul emplacement canonique. Les fiches renvoient ici (cf. SB<N>) plutôt que de redupliquer.
3. DEVOIR D'EXTRACTION : tout fait présent dans la source DOIT être extrait. [INCERTAIN] = vraiment absent de la source, jamais un prétexte pour ne pas chercher.
4. Doute réel -> [INCERTAIN] ; interprétation du narrateur -> [INTERPRÉTATION] ; théorie explicite du narrateur -> [THÉORIE] ; divergence ou ajout RP/OC assumé -> [DIVERGENCE RP].
5. Français accentué dans les .md (fin de la règle ASCII, décision worldbuilder) ; noms de fichiers et de dossiers en ASCII. Noms canon selon cette BIBLE et les fiches.

---

FIN_BIBLE_B10
