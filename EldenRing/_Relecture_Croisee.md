# Relecture croisee - Elden Ring

- version : W1
- nature : audit de cloture de la carte structurelle. Document de TRAVAIL et de DECISION.
  Il POINTE les collisions, il n'en corrige aucune. Jamais fetche en narration.
- perimetre audite : les 25 pages redigees de la carte structurelle (Cosmologie 5, Systemes 11,
  Factions 6, Chronologie 3), plus Sommaire.md, les quatre `_Index.md` de branche peuplees et
  `_Observations_Visuelles.md`.
- arbitre : `_Corpus/` (fichiers NR_* exclus, continuite separee par D1).
- etat : 33 collisions retenues, AUCUNE tranchee. Toutes attendent une decision du worldbuilder.

## Ce qu'est une relecture croisee de cloture, et pourquoi elle existe

Le wiki se construit par lots. Chaque page est ecrite en integrant a chaud ce que les pages deja
livrees imposent, et c'est ce qui garantit la coherence LOCALE : au moment ou une page part, elle
est juste au regard de ce qui existe. Mais cette discipline a un angle mort structurel, et il est
irreductible : une page ecrite au lot 1 ne peut pas savoir ce que le lot 3 va etablir. Quand
Destined_Death.md, page pilote, raconte la Night of the Black Knives, la page d'evenement qui lui
disputera l'autorite n'existe pas encore. Quand Erdtree.md ecrit "le corpus n'en dit rien
d'autre" sur l'ere anterieure a l'arbre, la page qui alignera six attestations de cette meme ere
n'est pas buildee. Aucune faute de methode n'a ete commise : c'est l'ordre de construction qui
produit mecaniquement ces ecarts.

La relecture croisee est la passe qui ferme cet angle mort. Elle relit l'ensemble comme un seul
document et cherche ce qu'aucune page ne pouvait voir depuis sa propre place : deux pages qui
affirment le contraire l'une de l'autre, deux pages qui balisent differemment le meme fait, une
page qui declare non dit ce qu'une autre cite, un renvoi qui pointe vers rien, deux registres de
trous ouverts sur une seule et meme question. Elle existe parce que le cout de ces ecarts n'est
pas cosmetique : en jeu, le MJ ne lit pas le wiki en entier, il fetche UNE page. Selon la page
ouverte, il refusera de nommer un personnage que l'autre nomme, ou improvisera dans un trou que
l'autre a deja comble. Une contradiction inter-pages est un generateur silencieux d'invention.

Trois regles gouvernent ce document. Il ne tranche rien : le corpus peut donner tort a une page,
cela ne dit pas encore ce que le monde doit devenir - c'est la decision du worldbuilder. Il ne
corrige rien : les corrections partiront au prochain BIBLE BUILD, apres arbitrage. Il verifie
tout ce qu'il avance : chaque collision retenue a ete controlee ligne a ligne dans `_Corpus/`, et
les collisions les plus graves l'ont ete deux fois, une collision BLOQUANTE fausse coutant plus
cher qu'une collision mineure ratee.

## Methode

Quatre relectures independantes, chacune avec sa lentille, sur les 25 pages lues integralement :

1. CONTRADICTIONS CHRONOLOGIQUES ET CAUSALES - ordre des evenements, ancrages, chaines de cause.
2. CONTRADICTIONS SUR LES ENTITES - roles, filiations, titres, statuts ; un nom traite comme une
   entite ici et comme deux la.
3. INCOHERENCES DE BALISAGE - un fait ETABLI sur une page et balise sur une autre ; un fait pose
   comme etabli alors que la SOURCE porte elle-meme une reserve ; un fait declare NON DIT alors
   qu'il est cite ailleurs.
4. RENVOIS ET DOUBLONS - renvois morts, tags [A BUILDER] sur pages livrees, faits traites en
   detail par deux pages, deux autorites concurrentes, doublons de trous.

Les quatre rapports ont produit 41 signalements, ramenes ici a 33 entrees. Cinq collisions
avaient ete vues par deux ou trois lentilles sous des angles differents et sont regroupees en une
seule entree : la rune de l'anneau (C2), le second demi-dieu (C1), "first Elden Lord" (C8), la
Gloam-Eyed Queen (C10), le siege oculaire de la grace (C23). Deux defauts du Sommaire releves
separement sont fusionnes en C33. Les quatre collisions classees BLOQUANTES ont ete reverifiees au
corpus avant redaction ; les quatre sont confirmees, aucune n'a ete degradee.

## Comment lire une entree

- PAGES : les fiches en collision. Le nombre de pages touchees fixe l'ordre a gravite egale.
- COLLISION : ce que chaque page dit, en clair.
- CORPUS : ce que le texte du jeu porte, localise. C'est l'arbitre de FAIT, pas l'arbitre de
  DECISION - il dit qui a mal lu, il ne dit pas ce qu'il faut ecrire.
- ARBITRAGE : une question FERMEE, tranchable sans relire le wiki, suivie de la consequence de
  chaque branche.

Echelle de gravite : BLOQUANTE = un MJ recevra deux reponses incompatibles selon la page fetchee,
sur un fait qui engage le jeu. GENANTE = incoherence reelle qui deforme un trou ou une autorite,
sans casser le monde. MINEURE = harmonisation de redaction, aucun enjeu de lore.

---

# COLLISIONS BLOQUANTES (4)

### C1 - Le corpus nomme-t-il le second demi-dieu mort la Nuit des Black Knives ?

- PAGES : Factions/Black_Knives_et_Numen.md, Chronologie/Night_of_the_Black_Knives.md,
  Systemes/Destined_Death.md, Systemes/Those_Who_Live_in_Death.md (4 pages, vue par 3 lentilles).
- COLLISION : Black_Knives TROU 4 demande "Qui est le second demigod mort cette nuit-la ?" et
  pose en NON DIT que "le corpus ne nomme jamais le second mort, et ne dit jamais explicitement
  que Ranni a tue sa chair CETTE nuit-la". Les trois autres pages citent la phrase qui nomme les
  deux morts, et Destined_Death en tire une affirmation ferme : "La symetrie est exacte et
  enoncee : Ranni perd la chair, Godwyn perd l'ame."
- CORPUS : `_Corpus/ER_Goods_02.md`, entree Cursemark of Death [8191], quatre phrases. La
  quatrieme, ligne 1723 : "Ranni was the first of the demigods whose flesh perished, while the
  Prince of Death perished in soul alone." Black_Knives cite les phrases 2 et 3 et s'arrete une
  phrase avant celle qui repond a sa propre question. La moitie de son NON DIT est fausse. L'autre
  moitie est exacte : le mot "night" ne figure pas dans l'entree, la simultaneite est enoncee mais
  le rattachement a cette nuit precise passe par Godwyn.
- ARBITRAGE : le TROU 4 de Black_Knives doit-il etre REECRIT en "la chair de Ranni a-t-elle peri
  cette nuit-la ?" - seule part reellement non dite - et sa citation completee de la quatrieme
  phrase ? OUI : le second mort cesse d'etre un trou, le TROU 3 de Night_of_the_Black_Knives
  (laquelle des deux morts etait visee) reste valide, et un MJ ne peut plus placer un tiers.
  NON : il faut alors expliquer pourquoi trois pages nomment Ranni et une l'interdit.
- Sous-question a trancher dans le meme geste, car le corpus ne la ferme pas : le suicide rituel
  de Ranni est-il un ACTE DU COMPLOT du meme soir, ou un acte separe et posterieur ?

### C2 - Destined Death etait-elle une rune de l'Elden Ring, ou du Golden Order seul ?

- PAGES : Systemes/Destined_Death.md, Systemes/Golden_Order.md,
  Cosmologie/Elden_Ring_et_Elden_Beast.md (3 pages, vue par 2 lentilles).
- COLLISION : Destined_Death ouvre par une phrase NON BALISEE, donc ETABLIE au sens du bandeau de
  la page : "C'est l'une des runes constitutives de l'Elden Ring", et durcit en TROU 1 contrainte
  (d) : "le verbe 'plucked' suppose que la rune faisait PARTIE de ce dont on l'a retiree, donc
  l'Elden Ring la contenait". Golden_Order TROU 3 contrainte (b) en fait une contrainte opposable.
  Elden_Ring_et_Elden_Beast TROU 4 demonte l'inference : "le corpus dit Golden Order, non Elden
  Ring", et son NON DIT ajoute que la LISTE des runes de l'anneau n'est nulle part donnee.
- CORPUS : source unique, `_Corpus/ER_Talk_01.md` ligne 1957 : "[102030040] The forbidden shadow,
  plucked from the Golden Order upon its creation...". Golden Order, jamais Elden Ring. Controle
  exhaustif : les 17 occurrences de "Rune of Death" du corpus ne la rattachent JAMAIS a l'anneau.
  Deux pages posent donc comme texte du jeu une proposition que le jeu ne contient pas.
- ENJEU : causal, pas cosmetique. Si la rune n'a jamais appartenu a l'anneau, reparer l'Elden Ring
  ne restitue pas la mort, et la Mending Rune of the Death-Prince AJOUTE un principe a l'Ordre au
  lieu d'en restaurer un.
- ARBITRAGE : Destined Death etait-elle contenue dans l'ELDEN RING, ou dans le GOLDEN ORDER seul ?
  ELDEN RING : c'est une decision de worldbuilding, a baliser comme telle, et le TROU 4
  d'Elden_Ring_et_Elden_Beast doit etre reecrit. GOLDEN ORDER SEUL : la phrase d'ouverture de
  Destined_Death passe en [INTERPRETATION] et la contrainte (b) de Golden_Order TROU 3 tombe.

### C3 - Le corpus nomme-t-il le pere de Ranni ?

- PAGES : Factions/Carian_et_Raya_Lucaria.md, Factions/Golden_Lineage.md,
  Systemes/Empyreans_et_succession_divine.md (3 pages).
- COLLISION : Carian TROU 1 ("Ranni est-elle fille de Radagon ?") pose en NON DIT que "le corpus
  ne nomme JAMAIS le pere de Ranni, ni ne la designe comme soeur de Radahn ou de Rykard", et en
  tire la contrainte (a) : "son statut doit venir d'ailleurs que de sa mere". Golden_Lineage range
  la meme filiation parmi les FILIATIONS EXPLICITEMENT ATTESTEES ; Empyreans cite la meme replique.
- CORPUS : `_Corpus/ER_Talk_06.md`, lignes 830 a 832, Rogier : "[325030030] Lunar Princess Ranni.
  One of the children born to King Consort Radagon and his first wife, Renalla." puis
  "[325030040] Demigod and sister to General Radahn and Praetor Rykard." Les DEUX negations de
  Carian sont fausses. Le TROU 1 de Carian est un FAUX TROU et sa contrainte (a) s'effondre.
  Origine probable de l'erreur : la page cite [324027030] "Lunar Princess Ranni, daughter to
  Rennala", replique de Gideon, incomplete, sans remonter a celle de Rogier.
- ARBITRAGE : supprime-t-on le TROU 1 de Carian au profit d'un renvoi vers Golden_Lineage, ou le
  REFORMULE-t-on sur ce qui reste reellement non dit ? SUPPRESSION : la filiation devient un fait
  simple, une autorite unique. REFORMULATION : les deux vrais trous disponibles sont "Ranni est-
  elle nee avant ou apres l'union Radagon-Marika ?" et "pourquoi elle seule des enfants de Rennala
  est-elle Empyrean, quand Radahn et Rykard ne le sont pas ?".

### C4 - Les guerres liurniennes sont-elles des batailles du Shattering ?

- PAGES : Chronologie/Chronologie_Generale.md, Factions/Carian_et_Raya_Lucaria.md,
  Chronologie/Shattering.md (3 pages).
- COLLISION : Chronologie_Generale TROU 5, intitule "L'ordre des batailles du Shattering", range
  "The First Liurnian War" [61023] et "The Second Liurnian War" [61021] parmi les "batailles
  ordinales dans un meme theatre", aux cotes des deux Defenses de Leyndell, et demande comment
  situer Aeonia et Volcano Manor "par rapport aux guerres de Liurnia". Carian fait des memes
  guerres les campagnes de Radagon ANTERIEURES a son mariage avec Rennala ; Shattering TROU 4 note
  que le texte ne rattache PAS ces marqueurs a la Shattering.
- CORPUS : `_Corpus/ER_Events.md` ligne 78 : "The First Liurnian War / Radagon's glory burns red
  as his hair" ; lignes 73 a 75 : "The Second Liurnian War / No victory for the golden, nor for
  the moon / No prize but atonement; the birth of a vow" - le voeu, donc le mariage a la Church of
  Vows. Erreur de fond confirmee : la serie [61010]-[61050] n'est PAS une liste de batailles du
  Shattering mais un corpus de steles couvrant toute l'histoire. On y trouve, verifie sur place,
  [61011] Godfrey a la fin de sa campagne et [61030] "The Routing of the Ancient Dragons" avec
  Godwyn vivant. Les memes batailles ne peuvent pas etre a la fois anterieures au mariage de
  Radagon et des episodes de la guerre fratricide qui suit le bris de l'anneau.
- ARBITRAGE : reduit-on le TROU 5 de Chronologie_Generale aux seuls theatres attestes du
  Shattering - Leyndell, Aeonia, Volcano Manor - en deplacant les guerres liurniennes dans le bloc
  anterieur ? OUI : la chronologie redevient coherente et Carian fait autorite sur ces deux
  guerres. NON : il faut assumer une divergence explicite avec le corpus et la baliser.

---

# COLLISIONS GENANTES (24)

### C5 - Quel balisage pour l'attribution d'un locuteur ?

- PAGES : Systemes/Destined_Death.md, Factions/Carian_et_Raya_Lucaria.md contre
  Chronologie/Night_of_the_Black_Knives.md, Factions/Golden_Lineage.md,
  Systemes/Frenzied_Flame.md, Scarlet_Rot.md, Sorceries.md, Those_Who_Live_in_Death.md,
  Incantations.md, Factions/Omen_et_Hornsent.md (10 pages).
- COLLISION : dix pages tiennent l'attribution d'une replique pour ETABLIE quand le locuteur se
  nomme dans son propre bloc (Rogier, Fia, Ranni, Godfrey, Hyetta, Gowry, Millicent, Sellen, D,
  Corhyn, Miriel, Thops, Iji). Deux pages appliquent [INCERTAIN] aux MEMES conditions :
  Destined_Death TROU 5 declare que "les attributions de cette page sont deduites du CONTENU des
  repliques", Carian balise [INCERTAIN] l'attribution de [20250400] a Ranni.
- CORPUS : le camp ETABLI a raison. `ER_Talk_01.md` [106110010] "Indeed, I am the witch Ranni."
  ouvre le bloc 10611 qui porte l'aveu du vol ; [106120060] commence par "I am the witch Ranni. I
  stole Death long ago" ; [20250400] est litteralement "Upon my name as Ranni the". Ce sont des
  auto-nominations, pas des deductions. Destined_Death se sous-estime et met [INCERTAIN] sur
  l'aveu le plus load-bearing du wiki - Ranni revendiquant le vol de la Rune of Death - pendant
  que la page d'evenement le tient pour acquis.
- ARBITRAGE : adopte-t-on la regle unique "auto-nomination dans le bloc = ETABLI ; deduction par
  le seul contenu = [INCERTAIN]" ? OUI : Destined_Death TROU 5 et le [INCERTAIN] de Carian se
  repassent a cette aune, et le vrai perimetre du [INCERTAIN] se reduit au bloc 2040
  (Margit/Morgott), deja correctement identifie par Omen_et_Hornsent TROU 5. NON : il faut dire
  quelle autre regle s'applique, les dix pages etant a realigner dans l'autre sens.

### C6 - Que faire des tags [A BUILDER] portes sur des pages livrees ?

- PAGES : Systemes/Destined_Death.md, Cosmologie/Erdtree.md, Systemes/Golden_Order.md,
  Systemes/Grace.md, Cosmologie/Greater_Will_et_les_Fingers.md, Cosmologie/Outer_Gods.md,
  Factions/Nox_Eternal_Cities_et_Albinaurics.md (7 pages).
- COLLISION : sept pages renvoient vers des pages EXISTANTES en les marquant [A BUILDER].
  Verifie sur disque : Destined_Death ligne 189 "Those Who Live in Death, Golden Order : pages de
  systeme [A BUILDER]" - les deux existent, et le TROU 1 de la MEME page ecrit "RESOLU EN PARTIE
  le 2026-07-25 par le build de Systemes/Golden_Order.md" ; Erdtree renvoie "Systemes/Crucible.md,
  Systemes/Golden_Order.md, Systemes/Grace.md [A BUILDER]" et repete le tag en corps de page sur
  Crucible.md ; Golden_Order marque Erdtree.md et Elden_Ring_et_Elden_Beast.md ; Grace marque
  Greater_Will_et_les_Fingers.md et Golden_Lineage.md ; Greater_Will et Outer_Gods rangent
  Frenzied_Flame.md et Scarlet_Rot.md dans leur bloc [A BUILDER] ; Nox y range Golden_Order.md.
  Les neuf pages visees existent.
- ENJEU : operationnel et immediat. En jeu, un MJ qui lit [A BUILDER] conclut que la page n'existe
  pas, ne la fetche pas, et retombe sur le trou ou sur l'invention alors que l'autorite existe.
- ARBITRAGE : deux questions, tranchables ensemble. (1) Purge-t-on tous les [A BUILDER] portant
  sur des pages livrees au prochain BIBLE BUILD ? (2) La convention "tag en fin de liste separee
  par des virgules" est structurellement ambigue - porte-t-elle sur le dernier item ou sur toute
  la liste ? Adopte-t-on un tag PAR ITEM ? Note : `_Questions_Worldbuilder.md` porte deja la
  question sous une autre forme (point 5), sans reponse.

### C7 - Les _Index de branche portent-ils les versions, ou renvoient-ils au Sommaire ?

- PAGES : Sommaire.md, Cosmologie/_Index.md, Systemes/_Index.md, Factions/_Index.md,
  Chronologie/_Index.md (5 pages).
- COLLISION : le Sommaire pose une indexation a trois etages et delegue formellement l'etage 2 :
  "<Branche>/_Index.md - sous-sommaire de branche, PORTE LES VERSIONS W<N> DE SES PAGES". Les
  quatre _Index concernes ne les portent pas et renvoient au Sommaire : "Liste detaillee et a
  jour : cf. Sommaire.md". Verifie : Factions/_Index.md annonce "etat : lot 3 integre (6 pages)"
  puis liste "(aucune)" trois lignes plus bas ; Chronologie/_Index.md fait de meme avec 3 pages ;
  Cosmologie/_Index.md ne liste qu'Erdtree.md sur 5 ; Systemes/_Index.md n'en liste que 3 sur 11.
- ENJEU : boucle de navigation fermee, Sommaire -> _Index -> Sommaire, sans jamais atteindre
  l'information. L'exception de navigation admise par le Sommaire autorise une descente vers un
  autre index, pas un aller-retour.
- ARBITRAGE : peuple-t-on les _Index de branche, ou supprime-t-on l'etage 2 de la doctrine du
  Sommaire ? PEUPLER : c'est ce que projette `_Implications.md` T6, qui prevoit de deporter la
  liste des pages vers eux quand le Sommaire deviendra trop gros. SUPPRIMER : le Sommaire reste
  seul index, les _Index se reduisent a un en-tete de branche. Dans les deux cas, corriger la
  contradiction interne "lot integre (N pages)" / "(aucune)" de Factions et Chronologie.

### C8 - "First Elden Lord" : premier absolu, ou premier de l'ere de l'Erdtree ?

- PAGES : Factions/Golden_Lineage.md, Factions/Ancient_Dragons_et_Dragon_Cult.md,
  Systemes/Crucible.md, Chronologie/Chronologie_Generale.md (4 pages, vue par 2 lentilles).
- COLLISION : trois pages posent "Godfrey, First Elden Lord" sans reserve. Ancient_Dragons TROU 1
  contrainte (c) pose, egalement sans reserve et comme contrainte dure de comblement : "le titre
  d'Elden Lord existait deja avant l'Erdtree". Chronologie_Generale cite les DEUX dans deux
  sections voisines sans relever la tension.
- CORPUS : les deux enonces existent, la collision est imputable a la source. 29 occurrences de
  "first Elden Lord" pour Godfrey, sans reserve ; une seule pour Placidusax, hedgee par la source
  ("is said to have been Elden Lord in the age before the Erdtree", `ER_Goods_01.md` l.1472). Le
  datum qui les reconcilie n'est cite par AUCUNE des 25 pages : `ER_Talk_06.md` ligne 1602, Miriel
  sur Radagon, "[330050060] Taking the title...of second Elden Lord." L'ordinal est donc interne a
  l'ere de l'Erdtree, ce qui absout Godfrey sans effacer Placidusax.
- ARBITRAGE : "first Elden Lord" vaut-il A L'INTERIEUR de l'ere de l'Erdtree, ou au sens ABSOLU ?
  INTERIEUR : Placidusax releve d'une institution homonyme et anterieure, les deux enonces
  coexistent, et la ligne "second Elden Lord" de Miriel doit etre inscrite dans une page.
  ABSOLU : le titre de Placidusax devient une tradition rapportee que l'Ordre ne reconnait pas -
  le hedge de la source l'autorise - et Ancient_Dragons TROU 1 contrainte (c) doit tomber.

### C9 - Radagon et Marika : une entite sous deux noms, ou deux personnes ?

- PAGES : Factions/Golden_Lineage.md contre Systemes/Empyreans_et_succession_divine.md,
  Cosmologie/Elden_Ring_et_Elden_Beast.md, Factions/Carian_et_Raya_Lucaria.md (4 pages).
- COLLISION : Golden_Lineage porte SEULE l'hypothese d'identite, correctement balisee : "'To
  think, that Radagon was Marika herself.' - Corhyn donne cela comme une deduction, pas comme un
  constat. [INCERTAIN]". Elle ne la propage ni ne la renvoie nulle part. Les trois autres pages
  raisonnent sur DEUX personnes distinctes sans jamais mentionner l'hypothese : Empyreans tire une
  regle structurelle de leur dualite ("Thou'rt yet to become me. Thou'rt yet to become a god.",
  adresse a Radagon) ; Elden_Ring pose deux agents d'un meme geste ("Queen Marika shattered the
  Elden Ring and Radagon attempted to repair it") ; Carian narre un depart et un remariage entre
  personnes distinctes.
- CORPUS : aucune des deux lectures n'est fausse. La seule source d'identite est Corhyn, deduction
  d'un PNJ ; partout ailleurs le corpus les nomme separement. Ce qui manque est le BALISAGE
  CROISE : une seule page sur quatre sait que la question existe.
- ARBITRAGE : l'identite Radagon = Marika est-elle RETENUE, ou laissee en suspens ? RETENUE : il
  faut reecrire la lecture d'Empyreans sur [100102020] - "Thou'rt yet to become me" devient Marika
  s'adressant a elle-meme - et annoter Elden_Ring TROU 3, ou Marika's Hammer devient une seule
  personne qui brise puis repare. EN SUSPENS : Empyreans, Elden_Ring et Carian doivent porter un
  renvoi vers Golden_Lineage declarant qu'elles raisonnent sous l'hypothese de deux personnes.

### C10 - Gloam-Eyed Queen et Dusk-Eyed Queen : une figure ou deux ?

- PAGES : Systemes/Destined_Death.md, Systemes/Incantations.md (2 pages, vue par 3 lentilles).
- COLLISION : Destined_Death TROU 6 declare "trois phrases dans tout le corpus" et conclut : "Le
  corpus ne dit RIEN de sa fin. Une Empyrean qui commandait la mort des dieux disparait du texte
  sans un mot", puis renvoie a des sources hors-texte pour combler. Le nom Dusk-Eyed Queen n'y
  figure nulle part. Incantations TROU 2 produit une QUATRIEME phrase, qui narre une defaite.
- CORPUS : `_Corpus/ER_Weapons_01.md` ligne 465, Godslayer's Greatsword : "Sacred sword of the
  Dusk-Eyed Queen who controlled the Godskin Apostles before her defeat at the hands of Maliketh."
  La defaite des Apostles par Maliketh est par ailleurs attestee quatre fois (`ER_Armor_01.md`,
  set Godskin Apostle) - et Destined_Death la cite elle-meme deux paragraphes plus haut sans
  jamais rapprocher les deux enonces. Le corpus n'identifie PAS les deux reines : les deux lectures
  restent ouvertes.
- ARBITRAGE : Gloam-Eyed Queen et Dusk-Eyed Queen sont-elles UNE figure ou DEUX ? UNE : le TROU 6
  de Destined_Death est faux sur son decompte et sur sa conclusion ; il perd son pathos et devient
  un trou sur le SORT POSTERIEUR a la defaite, pas sur le silence total. DEUX : Destined_Death doit
  porter une note de perimetre disant que la Dusk-Eyed Queen est une autre figure, sinon le lecteur
  croit le corpus muet la ou il parle. Dans les deux cas les deux trous doivent etre chaines : ils
  n'en font qu'un.

### C11 - La Gloam-Eyed Queen est-elle anterieure a la fondation du Golden Order ?

- PAGES : Systemes/Empyreans_et_succession_divine.md, Systemes/Destined_Death.md,
  Systemes/Golden_Order.md (3 pages).
- COLLISION : Empyreans pose sans reserve que la designation par les Fingers "fait CANDIDAT et non
  dieu, et son objet nomme est la succession de Marika", puis liste la Gloam-Eyed Queen parmi les
  Empyreans - donc, par cette regle, posterieure a la divinite de Marika. Destined_Death TROU 6
  contrainte (a) dit l'inverse : "candidate legitime a la divinite AU MEME TITRE QUE MARIKA", donc
  concurrente ; contrainte (c) : "le sceau de Maliketh vient APRES son regne". Golden_Order ferme
  la chaine : le confinement de Destined Death est "CONCOMITANT de sa creation".
- CORPUS : la chaine est nette. `ER_Armor_01.md` l.1213 "after their defeat by Maliketh, the Black
  Blade, the source of their power was sealed away" ; `ER_Goods_02.md` l.493 "when Maliketh sealed
  Destined Death, the true power of the black flame was lost" ; `ER_Goods_02.md` l.1657 "The Golden
  Order was created by confining Destined Death". La Gloam-Eyed Queen tombe donc AVANT la fondation
  de l'Ordre : elle ne peut pas etre candidate a succeder a une Marika dont l'Ordre n'existe pas
  encore. Empyreans generalise une replique de Ranni en regle universelle.
- ARBITRAGE : "chosen by the Fingers" designe-t-il une candidature a la DIVINITE EN GENERAL, ou
  specifiquement a la SUCCESSION DE MARIKA ? EN GENERAL : lecture de Destined_Death, compatible
  avec la chronologie, et la regle d'Empyreans doit etre elargie. SUCCESSION DE MARIKA : lecture
  d'Empyreans, incompatible - il faut alors sortir la Gloam-Eyed Queen de la liste ou dater
  autrement le sceau de Maliketh.

### C12 - Qui detient l'autorite sur la Nuit des Black Knives ?

- PAGES : Systemes/Destined_Death.md, Chronologie/Night_of_the_Black_Knives.md,
  Factions/Black_Knives_et_Numen.md (3 pages).
- COLLISION : trois autorites sur un meme evenement. Night_of_the_Black_Knives declare le partage
  des son chapeau ("Page d'EVENEMENT ; la rune volee est traitee par Systemes/Destined_Death.md"),
  partage que Destined_Death n'honore pas : elle porte une section complete "Le vol : Night of the
  Black Knives" et une section "La double mort et la cursemark", et ses Renvois ne nomment NI la
  page d'evenement NI la page de faction. Trois registres de trous se recouvrent partiellement
  (Destined_Death TROU 2, Black_Knives TROU 2, Night_of_the_Black_Knives TROU 1), pour un seul
  renvoi croise sur les six possibles.
- CAUSE PROBABLE : Destined_Death est la page pilote, ecrite avant l'existence des deux autres, et
  n'a pas ete relue apres leur livraison.
- ARBITRAGE : adopte-t-on le partage a trois - la RUNE a Destined_Death, l'EVENEMENT a
  Chronologie, le GROUPE a Factions - declare dans les trois chapeaux, avec le trou du
  COMMANDITAIRE porte par la seule page d'evenement ? OUI : une question, une page, cinq renvois a
  poser. NON : il faut dire quelle page absorbe les autres.

### C13 - L'ere anterieure a l'Erdtree est-elle documentee ?

- PAGES : Cosmologie/Erdtree.md, Chronologie/Chronologie_Generale.md,
  Factions/Ancient_Dragons_et_Dragon_Cult.md (3 pages).
- COLLISION : Erdtree ecrit "Une seule phrase, mais elle est categorique [...] Le corpus n'en dit
  rien d'autre", et son TROU 3 pose en NON DIT "sa duree, ses habitants, son ordre, la maniere dont
  elle s'est achevee". Chronologie_Generale consacre une section entiere au bloc anterieur et y
  aligne quatre attestations distinctes ; Ancient_Dragons TROU 4 contrainte (b) en tire "les
  dragons anciens y 'ruled' : un ordre politique, pas une faune".
- CORPUS : Chronologie_Generale a raison, massivement. Six enonces distincts, verifies :
  `ER_Goods_02.md`:324 ghostflame ; `ER_Goods_02.md`:861 les premieres armes des betes ;
  `ER_Goods_03.md`:57 les civilisations englouties ; `ER_Goods_04.md`:398 la fleur funeraire
  "before the Erdtree grew" ; `ER_Weapons_02.md`:248 et `SOTE_Talismans.md`:99 et 107 "The ancient
  dragons, who ruled in the prehistoric era before the Erdtree" ; `ER_Goods_01.md`:1472 Placidusax.
- ENJEU : le TROU 3 d'Erdtree invite le worldbuilder a inventer "ses habitants" et "son ordre"
  alors que les deux sont partiellement etablis ailleurs. Toute reponse donnee dans ce cadre risque
  de contredire l'empire des dragons anciens.
- ARBITRAGE : reduit-on le TROU 3 d'Erdtree a ce qui reste reellement non dit - la DUREE de l'ere
  et la MANIERE dont elle s'est achevee - en renvoyant habitants et ordre a Chronologie_Generale et
  Ancient_Dragons ? OUI : le trou se ferme aux trois quarts. NON : il faut expliquer pourquoi une
  page cosmologique ignore six attestations.

### C14 - Le Crucible est-il date par le corpus ?

- PAGES : Chronologie/Chronologie_Generale.md, Systemes/Crucible.md,
  Cosmologie/Lands_Between_et_Land_of_Shadow.md (3 pages).
- COLLISION : Chronologie_Generale TROU 4 pose en NON DIT que "le crucible n'est jamais date :
  'primordial' qualifie une FORME de l'Erdtree, pas une epoque", et le laisse flotter dans le
  corps de page. Crucible cite une datation explicite, et Lands_Between TROU 3 contrainte (a) s'en
  sert comme d'un jalon.
- CORPUS : `_Corpus/SOTE_Goods_01.md` lignes 994 et 1003 : "In an age long past, before this land
  was enshrouded in shadow, the vitality of the Crucible flourished." C'est bien une EPOQUE.
  Nuance a preserver : cette datation situe le Crucible par rapport a l'enshrouding du realm of
  shadow, PAS par rapport a l'Erdtree. Chronologie_Generale a raison sur l'absence de repere
  Crucible/Erdtree, tort sur "jamais date".
- ARBITRAGE : reformule-t-on le TROU 4 en distinguant les deux reperes - le Crucible EST date
  relativement a l'ombre, il ne l'est PAS relativement a l'Erdtree ? OUI : la contrainte de
  Lands_Between tient, et le trou se reduit au seul rapport Crucible/Erdtree. NON : il faut
  expliquer pourquoi une datation explicite ne compte pas.

### C15 - La croisade de Messmer a-t-elle un ancrage chronologique ?

- PAGES : Chronologie/Chronologie_Generale.md, Factions/Carian_et_Raya_Lucaria.md,
  Systemes/Sorceries.md (3 pages).
- COLLISION : Chronologie_Generale TROU 3 pose en NON DIT qu'"aucun texte releve ne relie la
  croisade a Godfrey, a la guerre contre les Geants, a la Nuit des Black Knives ou au Shattering",
  et en contrainte (c) que "le corpus ne l'inscrit dans aucune des epoques nommees : un placement
  ne peut pas s'en reclamer". Carian TROU 5 et Sorceries fournissent pourtant un ancrage par
  Rellana.
- CORPUS : l'ancrage existe. `SOTE_Goods_01.md` l.883 "In her childhood, she and her elder sister
  Rennala met these moons" ; `SOTE_Armor.md` l.866 "Rennala [...] gave her younger sister, who
  renounced her lineage to chase after Messmer, a gift of lustrous black hair" ; `SOTE_Goods_01.md`
  l.592 "Rellana disavowed her birthright and chose to stand at Messmer's side". La croisade tombe
  donc dans la fourchette qui va de la jeunesse de Rennala a l'arrivee de Radagon en Liurnie - soit
  dans les epoques nommees, ce que la contrainte (c) interdit de revendiquer.
- ARBITRAGE : integre-t-on l'ancrage Rellana au TROU 3, en absorbant la tension avec le "Long ago"
  par la longevite des Carians et des demi-dieux ? OUI : la croisade devient contemporaine de la
  generation de Rennala et la contrainte (c) tombe. NON : l'ancrage est juge insuffisant, et les
  deux pages doivent le dire explicitement plutot que l'une l'ignorer.

### C16 - Marika est-elle l'auteur du bris de l'Elden Ring ?

- PAGES : Factions/Black_Knives_et_Numen.md, Cosmologie/Elden_Ring_et_Elden_Beast.md,
  Chronologie/Shattering.md (3 pages).
- COLLISION : Black_Knives TROU 5 pose en DIT, donc en registre des faits acquis, que "leurs
  terres ont produit le marteau avec lequel Marika brisa l'Elden Ring", et cite Marika's Hammer
  sans balise. Les deux pages dont c'est le sujet gardent la question OUVERTE : Elden_Ring TROU 3
  ("Qui a brise l'anneau, et pourquoi ?") avec contrainte (d) sur l'agent anonyme des cinematiques,
  Shattering TROU 1 avec "Sur l'AUTEUR de la brisure, le corpus se contredit".
- CORPUS : les deux enonces existent. `ER_Weapons_01.md`, Marika's Hammer, nomme Marika sans
  reserve ; `ER_Talk_01.md` [13000300], [13000310] et [16500700] posent explicitement l'ignorance
  ("The Elden Ring was broken, but by whom? And why?"). La page qui n'en fait pas son sujet est la
  seule a fermer la question, en passant.
- ARBITRAGE : "Marika a brise l'anneau" est-il ACTE comme decision, ou la question reste-t-elle
  OUVERTE ? ACTE : Elden_Ring TROU 3 et Shattering TROU 1 se ferment ensemble. OUVERTE : la ligne
  DIT de Black_Knives TROU 5 doit se replier sur ce que le corpus garantit - "le marteau capable de
  briser l'Elden Ring vient des terres des Numen" - formulation deja employee par la contrainte (b)
  de la meme entree.

### C17 - L'origine des Numen hors des Lands Between est-elle etablie ou rapportee ?

- PAGES : Factions/Black_Knives_et_Numen.md, Cosmologie/Lands_Between_et_Land_of_Shadow.md,
  Systemes/Empyreans_et_succession_divine.md (3 pages).
- COLLISION : deux pages balisent [INCERTAIN] en citant la reserve de la source. La page
  PROPRIETAIRE du sujet cite la phrase nue, sans balise - alors qu'elle balise scrupuleusement la
  rumeur voisine ("rumored to be Numen" -> [INCERTAIN]) - et pose en DIT de son TROU 5 "origine
  hors des Lands Between ; meme souche que Marika", avec une contrainte opposable.
- CORPUS : `ER_Goods_01.md` ligne 1373 : "The Numen are said to have come from outside the Lands
  Between, and are in fact of the same stock as Queen Marika herself." La reserve "are said to"
  couvre TOUTE la phrase, donc aussi l'ascendance de Marika - pilier du TROU 2 d'Empyreans
  ("Marika a-t-elle ete Empyrean ?") et du TROU 3 d'Elden_Ring.
- ARBITRAGE : la filiation Marika/Numen est-elle promue en DECISION du worldbuilder, ou reste-t-
  elle [INCERTAIN] ? DECISION : les trois pages retirent le hedge et le fait devient opposable.
  [INCERTAIN] : Black_Knives se realigne sur le balisage des deux autres. C'est le pire cas de
  figure en l'etat, la page qui laisse tomber la reserve etant celle qu'on consultera.

### C18 - Combien y a-t-il de lunes, et qui en repond ?

- PAGES : Systemes/Sorceries.md, Factions/Carian_et_Raya_Lucaria.md,
  Factions/Nox_Eternal_Cities_et_Albinaurics.md (3 pages).
- COLLISION : Sorceries TROU 3 et Carian TROU 4 posent la meme question avec des preuves
  DIFFERENTES et incompletes chacune. Les trois premieres citations sont communes (Rennala's Full
  Moon, Ranni's Dark Moon, Rellana's Twin Moons) ; Sorceries seule porte Freezing Mist ("The snowy
  crone taught the young Ranni to fear the dark moon") ; Carian seule porte une quatrieme lune,
  "Said to be a fragment of the black moon that once hung above the Eternal City" (Memory Stone).
  Nox traite un troisieme fois le meme objet ("Nokstella eut un astre, the lost black moon").
- CORPUS : toutes les citations verifiees (`ER_Goods_01.md`:1958, 1966, 2011 ; `ER_Goods_03.md`:
  1836 ; `SOTE_Goods_01.md`:883). Le probleme n'est pas la divergence mais l'incompletude
  symetrique : qui consulte Sorceries ignore la lune noire de la cite eternelle, qui consulte
  Carian ignore qu'on a appris a Ranni a craindre la lune noire.
- ARBITRAGE : quelle page est PROPRIETAIRE de la question des lunes - Sorceries (les lunes comme
  objet de sorcellerie) ou Carian (les lunes comme patrimoine de la maison) ? La page retenue
  absorbe les cinq citations, y compris la lune de Nokstella ; les deux autres passent en renvoi
  de contenu, sur le modele deja applique entre Sorceries TROU 5 et Incantations TROU 3.

### C19 - Trois renvois visuels annoncent des observations qui n'existent pas

- PAGES : Cosmologie/Elden_Ring_et_Elden_Beast.md, Systemes/Runes_et_Great_Runes.md,
  Factions/Carian_et_Raya_Lucaria.md, contre _Observations_Visuelles.md (3 pages + le registre).
- COLLISION : trois pages renvoient au registre visuel comme s'il portait le fait. Elden_Ring :
  "Apparence et affrontement : cf. _Observations_Visuelles.md" et, en Renvois, "(forme de l'anneau,
  apparence de l'Elden Beast)". Runes : "Aspect d'une rune : voir _Observations_Visuelles.md.
  [VISUEL]". Carian TROU 4 : "RENVOI : _Observations_Visuelles.md (apparence des lunes)". Verifie :
  le fichier ne porte que OBS-001 (Fire Monks / Blackflame Monks) et OBS-002 (motif digital du
  Godslayer's Seal et de Metyr). Rien sur l'anneau, l'Elden Beast, l'aspect d'une rune ni les lunes.
- PREUVE QUE LA FAUTE EST EVITABLE : trois autres pages emploient la forme qui DECLARE le vide.
  Lands_Between TROU 5 : "RENVOI : _Observations_Visuelles.md, non renseigne." Crucible : "rien
  d'enregistre sur le Crucible". Omen_et_Hornsent : "rien d'enregistre (cornes, silhouette)".
- ARBITRAGE : impose-t-on la forme qui declare - un renvoi visuel non renseigne doit dire qu'il ne
  l'est pas ? OUI : trois renvois a reecrire, et le MJ cesse de croire que le fait existe. NON : il
  faut alimenter le registre sur ces quatre objets, ce que seul le worldbuilder peut faire (le MJ
  ne voit pas le jeu, cf. D12).

### C20 - Le Crucible est-il une entite distincte de l'Erdtree ?

- PAGES : Cosmologie/Erdtree.md, Systemes/Crucible.md (2 pages).
- COLLISION : lectures opposees des DEUX MEMES citations. Erdtree : "L'Erdtree n'est donc pas une
  origine : il est un ETAT ULTERIEUR d'autre chose. Le Crucible le precede et lui SURVIT sous forme
  de puissance residuelle." Crucible : "Le Crucible n'est donc pas une entite distincte de
  l'Erdtree : c'est l'Erdtree a un ETAT ANTERIEUR", durci en TROU 2 contrainte (a) : "c'est un
  CHANGEMENT D'ETAT d'une meme chose, pas un remplacement par une autre".
- CORPUS : ne tranche pas. `ER_Armor_01.md` l.1241 "Not unlike the crucible, the Erdtree in its
  primordial form" et l.1297 "the crucible of life, the primordial form of the Erdtree". Mais les
  consequences divergent et sont deja engagees : Crucible documente un Crucible ACTIF au present
  (influence sur les betes du realm of shadow, pouvoirs d'Andreas, doctrine hornsent, quete de
  Devonia pour "the Crucible's origin", "mother of Crucibles"), ce qui suppose une entite propre ;
  et "le Crucible lui survit" est logiquement incompatible avec "un etat anterieur de la meme
  chose".
- ARBITRAGE : le Crucible est-il le MEME ETRE a deux etats, ou un SUBSTRAT VITAL DISTINCT dont
  l'Erdtree est une mise en forme ? MEME ETRE : Erdtree doit retirer "lui survit", et le Crucible
  actif au present devient une remanence. SUBSTRAT DISTINCT : Crucible TROU 2 contrainte (a) tombe.
  La reponse conditionne le TROU 4 du Crucible (l'origine cherchable par Devonia) et le TROU 1 de
  l'Erdtree.

### C21 - Le siege du Dragonlord est-il a Farum Azula ?

- PAGES : Chronologie/Chronologie_Generale.md, Factions/Ancient_Dragons_et_Dragon_Cult.md
  (2 pages). Note : une lentille sur quatre a ecarte ce point en jugeant qu'il est flague des deux
  cotes ; les autres l'ont retenu, le NON DIT d'Ancient_Dragons portant sur l'existence meme du
  chainage, pas sur sa force.
- COLLISION : Chronologie_Generale TROU 4 fonde sur ce chainage - et sur lui seul - le
  rattachement de Farum Azula au bloc anterieur a l'Erdtree, puisque Placidusax y est dit "Elden
  Lord in the age before the Erdtree". Ancient_Dragons TROU 4 pose en NON DIT que "le corpus
  n'ecrit JAMAIS que le siege du Dragonlord se trouve a Farum Azula".
- CORPUS : le chainage est textuel. Deux entrees d'`ER_Goods_01.md` partagent mot pour mot la meme
  formule : l.1472 (Remembrance of the Dragonlord) "The Dragonlord whose seat lies at the heart of
  the storm beyond time" et l.1272 (Miquella's Needle) "the heart of the storm beyond time said to
  be found in Faram Azula". La reserve "said to be" est portee par la source. Ancient_Dragons
  ignore la seconde entree, que Frenzied_Flame cite pourtant integralement.
- ARBITRAGE : le chainage "heart of the storm beyond time" est-il SUFFISANT pour situer le siege
  du Dragonlord a Farum Azula ? OUI : le NON DIT d'Ancient_Dragons se rectifie, [IMPLICITE] est le
  bon balisage. NON : Chronologie_Generale perd son seul argument pour dater Farum Azula, et le
  bloc pre-Erdtree se reduit a trois elements.

### C22 - L'Elden Ring est-il la source nommee de la grace ?

- PAGES : Cosmologie/Elden_Ring_et_Elden_Beast.md, Systemes/Grace.md (2 pages).
- COLLISION : Elden_Ring cite comme etabli "Anchor of all lands, giver of grace, wellspring of all
  joy" et resume : "Attributs recurrents : racine de l'Ordre, ancre des terres, source de la
  grace". Grace TROU 1 pose en NON DIT "l'instance qui donne et reprend. Le corpus emploie
  systematiquement des tournures passives ou impersonnelles, sans JAMAIS nommer d'agent". La
  replique n'est citee nulle part dans Grace.md.
- CORPUS : un donneur est nomme. `ER_Talk_01.md` ligne 1793 : "[102001060] 'Anchor of all lands,
  giver of grace, wellspring of all joy.'" - invocation des Fingers relayee par Enia. Le "jamais"
  de Grace.md est faux tel qu'il est ecrit.
- ARBITRAGE : le TROU 1 de Grace scinde-t-il ses deux questions - qui est la SOURCE cosmologique
  de la grace (l'anneau, atteste) et qui la RETIRE a un individu (Godfrey "was robbed of his
  grace", agent jamais nomme) ? OUI : le trou survit, reduit a la seconde. NON : il tombe.
- Consequence causale examinee par aucune page, a trancher avant le jeu : si la grace depend de
  l'anneau, le bris devrait l'affecter - or l'anneau brise "yet guides thy kin" ([12000400]) et la
  grace continue de guider.

### C23 - La grace siege-t-elle dans les yeux, au present ?

- PAGES : Systemes/Grace.md, Systemes/Runes_et_Great_Runes.md (2 pages, vue par 2 lentilles).
- COLLISION : Grace pose en tete de sa section "Nature et siege", sans balise, au present et sans
  restriction : "La grace habite les etres, et elle siege dans les YEUX", puis batit dessus une
  contrainte de comblement (TROU 4 (b)). Runes_et_Great_Runes : "Une seule entree la localise dans
  l'oeil, et au passe."
- CORPUS : Runes a raison sur les deux points. La formule commune aux sept Golden/Numen/Hero's/
  Lord's Runes est "Grace that dwells WITHIN THE INHABITANTS of the Lands Between" (`ER_Goods_01.md`
  lignes 1337 a 1385) - jamais les yeux. La seule entree oculaire est Lands Between Rune [2990],
  ligne 1530 : "Grace SAID TO HAVE ONCE dwelled in the eyes of the inhabitants" - hapax, modalise
  et revolu. Grace convertit une reserve de source au passe en fait etabli au present, et en tire
  une contrainte opposable.
- ARBITRAGE : la grace est-elle visible dans les yeux AU PRESENT du RP ? OUI : c'est une decision
  de worldbuilding, a baliser comme telle. NON : Grace.md se realigne sur "la grace habite les
  habitants" et renvoie le siege oculaire a un [INCERTAIN] date au passe.
- Consequence directe en jeu : un MJ decrivant un habitant vivant des Lands Between saura-t-il ou
  non lui mettre de l'or dans les yeux ?

### C24 - Le Greater Will est-il blessable ?

- PAGES : Factions/Nox_Eternal_Cities_et_Albinaurics.md, Cosmologie/Greater_Will_et_les_Fingers.md
  (2 pages).
- COLLISION : Greater_Will balise "sous la meme reserve de source [...] [INCERTAIN]" et pose en
  TROU 1 contrainte (b) : "il est DIT blessable [...] mais la source hedge". Nox cite la meme ligne
  sans balise et pose en DIT de son TROU 3 : "il peut nuire au Greater Will et a ses vassaux".
- CORPUS : `ER_Goods_02.md` ligne 1536 : "Cannot be wielded by those without a fate, but is said
  to be able to harm the Greater Will and its vassals." La reserve est dans la source.
- ENJEU : "le Greater Will est atteignable par une arme" est la premisse de tout scenario de
  rebellion contre lui. Le RP se joue differemment selon que c'est un fait du monde ou une
  reputation d'objet a Nokron.
- ARBITRAGE : le Fingerslayer Blade peut-il EFFECTIVEMENT blesser le Greater Will, ou est-ce une
  reputation ? EFFECTIVEMENT : decision du worldbuilder, les deux pages retirent le hedge.
  REPUTATION : Nox s'aligne sur [INCERTAIN].

### C25 - Le lien Misbegotten / Crucible est-il un fait ou une croyance ?

- PAGES : Factions/Omen_et_Hornsent.md, Systemes/Crucible.md (2 pages).
- COLLISION : les deux pages posent la MEME question (le Crucible explique-t-il les cornes ?) et
  se renvoient explicitement l'une a l'autre, mais avec des socles OPPOSES. Omen_et_Hornsent TROU 1
  contrainte (b) : "les Misbegotten SONT rattaches au Crucible" - la majuscule en fait une
  contrainte opposable. Crucible : "[INCERTAIN] : 'are held to be' marque une croyance rapportee",
  repris en TROU 1 contrainte (a).
- CORPUS : `ER_Goods_04.md` ligne 770 : "The misbegotten are held to be a punishment for making
  contact with the Crucible" - croyance in-world, pas fait.
- ARBITRAGE : le lien Misbegotten/Crucible est-il un FAIT DU MONDE ou une OPINION des Lands
  Between ? FAIT : Crucible retire son [INCERTAIN]. OPINION : Omen_et_Hornsent retire sa contrainte
  (b) - et le meme mecanisme de jugement culturel qui structure deja l'opposition devolution /
  evolutionary gifts entre Lands Between et hornsent s'applique une fois de plus. Une seule reponse
  pour les deux TROU 1.

### C26 - Astrologues et sorciers : un trou, deux registres

- PAGES : Systemes/Sorceries.md, Factions/Carian_et_Raya_Lucaria.md (2 pages).
- COLLISION : Sorceries TROU 1 ("Astrologues et sorciers : qui descend de qui ?") et Carian TROU 2
  ("Les astrologues precedent-ils les sorciers, ou en descendent-ils ?") sont la meme question,
  avec les memes trois citations, sans aucun renvoi croise, et avec des CONTRAINTES partiellement
  disjointes : Sorceries insiste sur le baton d'astrologue deja catalyseur a glintstone, Carian sur
  le fait que "les Carians se savent du cote astrologue". Deux cahiers des charges concurrents pour
  une meme invention future.
- CORPUS : les trois entrees existent, la contradiction est imputable a la source.
  `ER_Weapons_01.md`:207 "Astrologers, who preceded the sorcerers" ; `ER_Armor_02.md`:614 et 621
  "Glintstone sorcerers are the descendants of astrologers" ; `ER_Armor_01.md`:1509 et suivantes
  "are said to be heirs of the glintstone sorcerers".
- ARBITRAGE : Sorceries.md est-elle designee PAGE PROPRIETAIRE de ce trou, Carian passant en
  renvoi de contenu ? OUI : un seul cahier des charges, les deux jeux de contraintes fusionnes dans
  Sorceries. NON : il faut dire ce qui justifie deux registres pour une question.

### C27 - Crucible.md renvoie a trois pages qui n'existent pas

- PAGES : Systemes/Crucible.md, Factions/Omen_et_Hornsent.md (2 pages).
- COLLISION : Crucible renvoie a "Factions/Crucible_Knights.md, Factions/Hornsent.md,
  Systemes/Omen.md [A BUILDER] - cf. TROU 1". Ces trois noms n'existent pas et ne figurent dans
  AUCUNE des 25 pages listees par `_Implications.md` : ce ne sont pas des pages a builder, ce sont
  des noms fantomes. La page reelle existe et couvre les deux peuples : Factions/Omen_et_Hornsent.md,
  dont le TROU 1 porte le renvoi RETOUR, lui correct ("cf. Systemes/Crucible.md, TROU 1").
- ARBITRAGE : remplace-t-on les trois noms fantomes par Factions/Omen_et_Hornsent.md ? OUI : le
  renvoi aller existe enfin. Verifier dans le meme geste qu'on ne cree pas de boucle renvoi-vers-
  renvoi : Crucible TROU 1 doit GARDER son contenu propre, pas se reduire a pointer vers l'autre
  page.

### C28 - Une seule Great Rune est-elle l'anneau d'ancrage ?

- PAGES : Systemes/Golden_Order.md, Cosmologie/Elden_Ring_et_Elden_Beast.md,
  Systemes/Runes_et_Great_Runes.md (3 pages).
- COLLISION : Golden_Order ecrit "L'une occupe une position singuliere" et reprend le fait comme
  acquis dans le DIT de son TROU 3 ("l'une est l'anneau d'ancrage en son centre"), sans reserve et
  sans renvoi. Elden_Ring TROU 2 documente exactement l'inverse ("Deux Great Runes se disent
  l'anneau d'ancrage"), et Runes TROU 3 confirme que cela "interdit de lire ces descriptions comme
  un inventaire coherent".
- CORPUS : deux entrees, deux articles definis. `ER_Goods_01.md` ligne 192 (Godrick) "This Great
  Rune is known as the anchor ring, found in the center of the Elden Ring" ; ligne 210 (Morgott)
  "This Great Rune is the anchor ring that houses the base". Golden_Order ferme silencieusement,
  par selection de citation, une contradiction que deux autres pages documentent.
- ARBITRAGE : corrige-t-on Golden_Order en lui faisant citer les deux entrees et renvoyer a
  Elden_Ring TROU 2 ? OUI : la page proprietaire de la structure interne de l'anneau reste la page
  Cosmologie, et Golden_Order cesse de trancher en passant. NON : il faut dire laquelle des deux
  Great Runes est l'anneau d'ancrage, ce que le corpus ne permet pas sans decision.

---

# COLLISIONS MINEURES (5)

### C29 - Deux pages localisent une citation dans le mauvais fichier de corpus

- PAGES : Systemes/Destined_Death.md, Systemes/Golden_Order.md contre
  Systemes/Empyreans_et_succession_divine.md (3 pages).
- COLLISION : Destined_Death et Golden_Order citent "Marika's sole need of her shadow was a vessel
  to lock away Destined Death. Even then, she betrayed him." en la localisant dans
  `_Corpus/SOTE_Goods_01.md`, sans nom d'entree. Empyreans la localise dans Remembrance of the
  Black Blade, entree qu'elle situe elle-meme dans `_Corpus/ER_Goods_01.md`.
- CORPUS : Empyreans a raison. La phrase est a `_Corpus/ER_Goods_01.md` ligne 1452, entree
  Remembrance of the Black Blade [2956] ; elle n'apparait nulle part dans SOTE_Goods_01.md. Deux
  pages sur trois renvoient donc a un fichier qui ne contient pas la citation, et sur l'enonce le
  plus structurant du rapport Marika / Maliketh - celui qui fonde le TROU 4 de Destined_Death.
- ARBITRAGE : etend-on `verif_citations.py` au controle du FICHIER cite, et pas seulement a
  l'existence litterale de la citation quelque part dans `_Corpus/` ? C'est exactement le type
  d'erreur que l'outil ne peut pas voir en l'etat (cf. `_Implications.md`, section Outil de
  verification). Correction de localisation dans les deux pages, sans enjeu de lore.

### C30 - L'aiguille d'or non alliee : trois balisages pour une phrase

- PAGES : Cosmologie/Outer_Gods.md, Systemes/Scarlet_Rot.md, Systemes/Frenzied_Flame.md (3 pages).
- COLLISION : Scarlet_Rot balise ("L'effet est enonce sous reserve PAR LA SOURCE [...]
  [INCERTAIN]") ; Frenzied_Flame TROU 4 (a) semi-hedge ("est dit capable de retarder la rot", sans
  balise) ; Outer_Gods TROU 2 (b) affirme a l'indicatif que l'aiguille "agit [...] contre 'the
  incurable rotting sickness'".
- CORPUS : `ER_Goods_03.md` lignes 770 et 778 : "it is thought capable of forestalling the
  incurable rotting sickness" - reserve de source. La contrainte d'Outer_Gods survit par un autre
  chemin (Hefty Rot Pot, "Rot is one of the divine elements of the outer gods", non modalise) :
  l'enjeu de lore est faible.
- ARBITRAGE : retient-on le balisage de Scarlet_Rot, page proprietaire du sujet, pour les trois
  pages, en refondant la contrainte d'Outer_Gods sur Hefty Rot Pot plutot que sur l'aiguille ?

### C31 - Les Two Fingers maitrisent-ils la grace ?

- PAGES : Systemes/Grace.md, Cosmologie/Greater_Will_et_les_Fingers.md (2 pages).
- COLLISION : Grace TROU 2 pose en NON DIT que "le corpus les met toujours en voisinage, jamais en
  equation", et ne retient que deux lignes de voisinage institutionnel. Greater_Will cite une ligne
  qui repond DIRECTEMENT a la question, avec sa reserve : "They are the purported masters of the
  grace that guides your kind" [INCERTAIN].
- CORPUS : attribution correcte. `ER_Talk_03.md` ligne 1548, replique [301021030], bloc 3010 dont
  le locuteur se nomme en [301012010] "Me. Varre." La formule "jamais en equation" reste
  techniquement defendable - maitrise n'est pas identite - mais elle laisse croire que le corpus
  est muet la ou il porte un enonce hedge.
- ARBITRAGE : integre-t-on la ligne de Varre au DIT du TROU 2 de Grace, avec sa DOUBLE reserve
  ("purported" est du texte source, et Varre est une source hostile) ? Si oui, un rapport de
  MAITRISE suffit-il a FERMER le trou, ou seulement a le CONTRAINDRE ?

### C32 - L'ordre entre le bris de l'anneau et la saisie des eclats

- PAGES : Cosmologie/Elden_Ring_et_Elden_Beast.md, Chronologie/Shattering.md (2 pages).
- COLLISION : Elden_Ring pose "Le bris PRECEDE la guerre" et en fait une contrainte dure (TROU 3
  (c) : "le bris precede la guerre et la saisie des shards"). Shattering TROU 2 laisse en NON DIT
  "l'ordre entre la brisure et la revendication des eclats".
- CORPUS : ferme trivialement la question. `ER_Talk_01.md` ligne 156 : "[14000500] Soon, Marika's
  offspring, demigods all, claimed the shards of the Elden Ring" - on ne peut pas revendiquer des
  eclats avant qu'il y en ait. La contrainte (b) de Shattering l'admet d'ailleurs a demi-mot ("les
  eclats existent avant la guerre").
- ARBITRAGE : retire-t-on ce membre du NON DIT du TROU 2 de Shattering ? Aucun enjeu de monde,
  simple harmonisation de redaction.

### C33 - Le Sommaire : entree fantome, entree en double, quatre versions en retard

- PAGES : Sommaire.md (1 page, trois defauts distincts).
- COLLISION : (a) le Sommaire indexe `_Relecture_Croisee.md (W1)` au meme titre que les autres,
  donc comme livree - le present document la produit, l'entree devient exacte a sa livraison ;
  (b) l'entree `_Observations_Visuelles.md (W1)` figure DEUX FOIS a l'identique, lignes 123 et 127 ;
  (c) quatre entrees sont en retard sur les pages : Elden_Ring_et_Elden_Beast.md indexee (W1) pour
  une page en W2, Greater_Will_et_les_Fingers.md (W1) pour W2, Cosmologie/_Index.md (W2) pour W3,
  Systemes/_Index.md (W2) pour W6. Les 21 autres entrees sont a jour.
- ENJEU : le canari de version est le mecanisme qui doit permettre de detecter un [VERSION
  DECALEE] en narration. S'il derive silencieusement, il ne detecte plus rien. Une entree fantome,
  elle, coute un fetch en echec et un [FETCH ECHOUE] a signaler en pleine narration.
- ARBITRAGE : aucun. Trois corrections mecaniques a passer au prochain BIBLE BUILD, sans decision
  de fond. La regle est deja ecrite : "Toute page relivree incremente son W<N> ; reporter le nouveau
  numero dans son entree du Sommaire dans le meme build."

---

# FAUX POSITIFS ECARTES

Consignes pour qu'ils ne soient pas re-souleves a la prochaine passe. Chacun a ete verifie au
corpus et rejete.

- Blocs de repliques Ranni [106030xxx] contre [106200xxx] : `ER_Talk_01.md` porte reellement DEUX
  blocs quasi identiques, le second inserant la replique de Blaidd et decalant les IDs d'un cran.
  Destined_Death, Empyreans et Night_of_the_Black_Knives ont toutes raison. Ce n'est pas une erreur
  de citation.
- "grave of civilizations that flourished before the Erdtree" attribue a Map: Ainsel River par
  Chronologie_Generale et a Map: Siofra River par Nox : `ER_Goods_03.md` porte la phrase sur les
  DEUX cartes.
- Statut du Greater Will parmi les outer gods : Outer_Gods, Greater_Will et Frenzied_Flame disent
  toutes trois que le corpus ne l'appelle jamais outer god. Convergence, pas collision.
- Godwyn = Prince of Death : equation portee a l'identique par cinq pages, corpus confirme ("the
  Prince of Death, he who used to be called Godwyn", `ER_Talismans.md`, Prince of Death's Pustule).
- Margit / Morgott : seule Omen_et_Hornsent ouvre la question, aucune page ne pose l'inverse. C'est
  le vrai perimetre du [INCERTAIN] d'attribution de locuteur (bloc 2040), cf. C5.
- Corruption des Two Fingers imputee au Shattering (Shattering.md) contre l'interdiction posee par
  Greater_Will TROU 2 (c) : les deux enonces ne portent pas sur le meme objet (corruption contre
  silence), et Shattering balise deja la replique de Varre comme croyance de locuteur.
- Avertissement de methode de Chronologie_Generale ("aucune datation chiffree d'un evenement
  passe") : verifie, le corpus ne porte que "an age ago", "so many moons ago", et les chiffres
  tournes vers l'avenir.
- Doctrine du One Great attribuee a Hyetta par Frenzied_Flame : correct et source ([310010010] "My
  name is Hyetta") ; les autres pages disent seulement "une maiden". Difference de granularite.
- Variation "trace / residue / true vestiges" des Golden Runes : signalee par Grace.md dans la
  phrase meme ou elle dit "a l'identique". Trop faible pour etre remonte.
- Rellana soeur cadette de Rennala : verifie, "her elder sister Rennala" (`SOTE_Goods_01.md`:883).
- Ordovis, chevalier du Crucible sous Godfrey ET "old hero of the Shattering" : ecart reel mais
  isole dans Crucible.md TROU 3, qu'aucune autre page ne contredit. A verser au registre des trous
  de la page, pas a la relecture croisee.

---

# RECAPITULATIF DES ARBITRAGES

| # | Question fermee | Gravite | Pages |
|---|---|---|---|
| C1 | Reecrire Black_Knives TROU 4 en "la chair de Ranni a-t-elle peri cette nuit-la ?" | BLOQUANTE | 4 |
| C2 | Destined Death : contenue dans l'Elden Ring, ou dans le Golden Order seul ? | BLOQUANTE | 3 |
| C3 | Supprimer le TROU 1 de Carian, ou le reformuler sur ce qui reste non dit ? | BLOQUANTE | 3 |
| C4 | Les guerres liurniennes sortent-elles du TROU 5 (batailles du Shattering) ? | BLOQUANTE | 3 |
| C5 | Regle unique : auto-nomination = ETABLI, deduction par contenu = [INCERTAIN] ? | GENANTE | 10 |
| C6 | Purger les [A BUILDER] sur pages livrees, et taguer par item ? | GENANTE | 7 |
| C7 | Peupler les _Index de branche, ou supprimer l'etage 2 ? | GENANTE | 5 |
| C8 | "First Elden Lord" : interne a l'ere de l'Erdtree, ou absolu ? | GENANTE | 4 |
| C9 | Identite Radagon = Marika retenue, ou laissee en suspens ? | GENANTE | 4 |
| C10 | Gloam-Eyed et Dusk-Eyed : une figure ou deux ? | GENANTE | 2 |
| C11 | "Chosen by the Fingers" : divinite en general, ou succession de Marika ? | GENANTE | 3 |
| C12 | Partage a trois de la Nuit des Black Knives (rune / evenement / groupe) ? | GENANTE | 3 |
| C13 | Reduire Erdtree TROU 3 a la duree et a la fin de l'ere ? | GENANTE | 3 |
| C14 | Le Crucible est date par rapport a l'ombre, non a l'Erdtree ? | GENANTE | 3 |
| C15 | Integrer l'ancrage Rellana au TROU 3 de la croisade de Messmer ? | GENANTE | 3 |
| C16 | "Marika a brise l'anneau" : acte, ou question ouverte ? | GENANTE | 3 |
| C17 | Origine Numen / souche de Marika : decision, ou [INCERTAIN] ? | GENANTE | 3 |
| C18 | Page proprietaire des lunes : Sorceries ou Carian ? | GENANTE | 3 |
| C19 | Imposer la forme "renvoi visuel non renseigne" ? | GENANTE | 3 |
| C20 | Crucible : meme etre a deux etats, ou substrat distinct ? | GENANTE | 2 |
| C21 | Le chainage "heart of the storm beyond time" suffit-il pour Farum Azula ? | GENANTE | 2 |
| C22 | Scinder Grace TROU 1 en source cosmologique / agent du retrait ? | GENANTE | 2 |
| C23 | La grace est-elle visible dans les yeux au present du RP ? | GENANTE | 2 |
| C24 | Le Fingerslayer Blade blesse-t-il effectivement le Greater Will ? | GENANTE | 2 |
| C25 | Misbegotten / Crucible : fait du monde ou opinion des Lands Between ? | GENANTE | 2 |
| C26 | Sorceries proprietaire du trou astrologues / sorciers ? | GENANTE | 2 |
| C27 | Remplacer les trois renvois fantomes de Crucible par Omen_et_Hornsent ? | GENANTE | 2 |
| C28 | Golden_Order cite-t-elle les deux anneaux d'ancrage et renvoie-t-elle ? | GENANTE | 3 |
| C29 | Etendre verif_citations.py au controle du fichier cite ? | MINEURE | 3 |
| C30 | Aligner les trois pages sur le balisage de Scarlet_Rot pour l'aiguille ? | MINEURE | 3 |
| C31 | Integrer la ligne de Varre au TROU 2 de Grace ; ferme-t-elle le trou ? | MINEURE | 2 |
| C32 | Retirer l'ordre bris / eclats du NON DIT de Shattering TROU 2 ? | MINEURE | 2 |
| C33 | Corrections mecaniques du Sommaire (fantome, doublon, 4 versions) | MINEURE | 1 |

Total : 33 entrees, 4 BLOQUANTES, 24 GENANTES, 5 MINEURES. Aucune tranchee.

Pages les plus exposees, par nombre de collisions : Systemes/Destined_Death.md (9),
Chronologie/Chronologie_Generale.md (6), Factions/Carian_et_Raya_Lucaria.md (6),
Cosmologie/Elden_Ring_et_Elden_Beast.md (6), Systemes/Grace.md (5). Que la page PILOTE soit la
plus exposee est attendu et non imputable a sa redaction : ecrite en premier, elle a raisonne sur
un wiki vide, et huit lots l'ont depuis contournee sans qu'elle soit relue.

---

FIN_WIKI__RELECTURE_CROISEE
