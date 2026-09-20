# _Implications - Cyberpunk

- version : W17
- Document de travail. Non indexe au Sommaire. Jamais fetche en narration.

## Etat du build
- Passe 0 close. Passe 1 en cours.
- Lot IA : LIVRE (5 pages).
- Lot Personnages : LIVRE (2026-09-19). 14 fiches + 2 satellites : Silas_Null (W4), Silas_Null_relations_1 et _2 (W2), Mr_Blue_Eyes, Peralez (W2), Sandra_Dorsett, Bryce_Mosley, Maman_Brigitte (W2), Placide, Wilky_LaGuerre, Kurt_Hansen, T_Bug, Songbird, Solomon_Reed, Rosalind_Myers, V.
- Propagations du lot : Net_et_Blackwall W5, Entites_du_Blackwall W3, J0RMUN94ND W3, Alt_Cunningham W2, Lilith W2, Night_Corp W3, Chrome_et_Cyberpsychose W4, NetWatch W4, Voodoo_Boys W5, Barghest W2, Pacifica_et_Dogtown W2, Chrono_Univers W4, Chrono_2077 W3, Night_City_2077 W3, Sommaire W7.
- Lot Power_Scaling : LIVRE (2026-09-20). 2 pages W1 : Power_Scaling/Scaling_Numerique.md, Power_Scaling/Scaling_Physique.md. Propagations : J0RMUN94ND W4, Alt_Cunningham W3, Lilith W3, Entites_du_Blackwall W4, IA_Mineures W2, Silas_Null W5, Silas_Null_relations_1 W3, Maman_Brigitte W3, Wilky_LaGuerre W2, Mr_Blue_Eyes W2, V W2, Netrunning_2077 W2, Night_Corp W4, Maelstrom W3, FIA_NUSA W2, Chrono_2077 W4, Chrono_Univers W5, Sites_Arasaka W2, Sommaire W8.
- Point de depart fixe (2026-09-20) : ouverture de R0. Propagations WIKI : RESTE, cf. HANDOFF B3 S1.
- A FAIRE : BIBLE B3 + Resume (cloture de Passe 1), dans un THREAD DEDIE (decision worldbuilder 2026-09-20). Tout le necessaire : HANDOFF B3 ci-dessous. Puis Passe 2.

## HANDOFF B3 - thread dedie (consolide 2026-09-20)

Tout est ACTE sauf mention [A VALIDER]. Ordre d'execution recommande : S0, S1, S2, S3, S4.

### S0. Ouverture du thread
- Lire ce journal (W17), puis Sommaire (W8). BIBLE B2 en fichier de projet.
- Verifier sur le depot que le lot Power_Scaling est pousse (Sommaire en W8, Power_Scaling/ present).
- SPEC : v8_5 a reverifier par listing de Config/.
- Budget : 10 consultations WIKI par tour. Tour 1 suggere : Chrono_2077, Sites_Arasaka, Silas_Null, T_Bug, Silas_Null_relations_2, Resume, Night_City_2077 (Rhyne), Net_et_Blackwall (Bartmoss). Tour 2 : fiches SB5 restantes (Peralez, Rosalind_Myers, Songbird, Kurt_Hansen, Solomon_Reed, Placide, Maman_Brigitte, Wilky_LaGuerre, Bryce_Mosley, Sandra_Dorsett, V, Mr_Blue_Eyes, IA/).
- Localiser par grep sur le clone (audit, hors budget) avant d'editer ; lire en entier toute page editee.

### S1. Propagations WIKI du point de depart (AVANT la BIBLE)
Decision : point de depart = ouverture de R0. Appel de T-Bug = premier beat de R1 (sort des fiches noyau). Detail : Decisions actees - lot Power_Scaling, Point de depart.
- Chronologie/Chrono_2077.md (W4 -> W5)
  - S1 : titre -> "Avant le point de depart (ouverture de R0)". Ligne Silas : retirer "T-Bug lui demande de rester en plan B pour le Konpeki" ; age selon la date de R0 [A VALIDER].
  - S1bis : R0 = un contrat de Mr. Hands ; decor de Silas (VDB en solo, genie du hack, symbiose avec Yor, neutre dans les conflits internes aux VDB, proche de Brigitte, Placide et Slider) ; "Point de depart du RP : ouverture de R0". Retirer l'appel de T-Bug de S1bis.
  - S2 : premier beat de R1, T-Bug contacte Silas directement, sans fixer, pour l'avoir en assurance. Ligne Silas : retirer "Point de depart du RP".
- Lieux/Sites_Arasaka.md (W2 -> W3) : S2, retirer "Point de depart du RP".
- Personnages/Silas_Null.md (W5 -> W6)
  - S1 : "Age au point de depart" selon la date de R0 [A VALIDER] ; l'age au T0 (braquage) reste 22 ans.
  - Table d'histoire : retirer la ligne "2077, veille du T0" (appel de T-Bug), en GARDANT le fait "il ignore que Brigitte est derriere le vol de la Relic" (le loger en S12 s'il n'y est pas).
  - Liens : "T-Bug : collegue occasionnelle ; plan B au Konpeki" -> retirer "plan B au Konpeki".
- Personnages/T_Bug.md (W1 -> W2) : S4, retirer "Veille du T0 : elle lui demande de rester en plan B pour le Konpeki. Silas y est en freelance, pas en tant que VDB." (matiere roadmap R1).
- Personnages/Silas_Null_relations_2.md (W2 -> W3), bloc T-Bug : Statut, retirer "Au T0, elle lui demande de rester en plan B..." ; Dynamique, garder "Elle sait qu'il est meilleur qu'elle", la suite ("c'est pour ca qu'elle le veut en plan B") part en matiere roadmap R1 ; Evolution datee, retirer "2077, veille du T0 : plan B du Konpeki".
- Tiennent sans changement : V.md et Sites_Arasaka "Silas a 22 ans" (age au braquage) ; Chrono_Univers intro "a la veille du RP".
- Sommaire (W8 -> W9) : descriptions de Resume ("arrete a l'ouverture de R0") et de T_Bug (retirer "plan B Silas") ; W de toutes les pages relivrees.

### S2. BIBLE B3 (livraison complete, FIN_BIBLE_B3, cible 35-40k, plafond 55k, wc -m)
- SB0
  - Protagoniste : Silas "Zer0" Null (ex-"Zer0_Null").
  - Focus narratif : de R0 (contrat de Mr. Hands, avant le Konpeki) jusqu'au Blackwall. Point de depart : ouverture de R0.
  - Sources : images de Yor, de Silas et de V RECUES (retirer "a venir, Passe 1").
  - Pages rattachees : IA 5 ; Personnages 16 (14 fiches + 2 satellites) ; Power_Scaling 2 ; recompter au listing.
  - Etat du build : Passe 1 close ; suite : Passe 2 (garde-cap pre-roadmap du worldbuilder, puis roadmaps).
- SB1
  - Retirer "Collision sur Songbird, puis sur le mur." (matiere de Passe 2). Garder "Deux modeles d'empire numerique : Yor amalgame, Blue Eyes hierarchise."
- SB2
  - Lexique creole de Silas, depuis Silas_Null.md S10 : dont "manje l", "vale l", "Miray nwa", "tchwip". Handle Zer0.
- SB3 (verifier chaque date, montrer les calculs)
  - 2055 : naissance, lieu [INCERTAIN] (retirer "Pacifica").
  - 2062 : Silas, 7 ans, arrive a Pacifica avec les refugies haitiens.
  - 2069 : premier mort, un netrunner NetWatch, sous Slider ; il garde sa Netdriver (14 ans : du 30/01/2069 au 29/01/2070).
  - 2070 : schisme VDB, juste avant la secession de Hansen ; Silas (15 ans) suit Slider a Dogtown (retirer "annees 2070 [INCERTAIN]").
  - 2075-2077 : Yor devance Alt d'une courte tete (retirer "au calibre d'Alt").
  - 2077 : Konpeki fin avril-debut mai.
  - Notes : retirer "Mois du Konpeki : canon muet" et "Ordre des arcs". Poser : R0 (contrat de Mr. Hands) -> R1 (premier beat : appel de T-Bug ; puis le Konpeki, depuis l'appartement de Coastview) -> ellipse de convalescence de V, Silas traque Lilith ; la suite en garde-cap ; le Blackwall en dernier. Point de depart : ouverture de R0, date [A VALIDER].
- SB4
  - Maelstrom : retirer "arc 2".
  - Barghest : "loi d'enfance de Silas" -> loi du quartier de son adolescence (depuis 2070, 15 ans).
  - Voodoo Boys : Silas en solo, pas sorti ; neutre dans les conflits internes.
- SB5 (decroissance : 3-4 lignes + renvoi pour chaque entite a fiche)
  - A fiche : Silas_Null (+ relations_1, relations_2), J0RMUN94ND, Alt_Cunningham, Lilith, Entites_du_Blackwall (Cynosure, Cerberus, co-batisseurs), IA_Mineures (CN-07, Delamain, Skippy, Brendan), Mr_Blue_Eyes, Peralez, Sandra_Dorsett, Bryce_Mosley, Maman_Brigitte, Placide, Wilky_LaGuerre, Kurt_Hansen, T_Bug, Songbird, Solomon_Reed, Rosalind_Myers, V. Bartmoss : domicile Net_et_Blackwall S2.
  - Silas : Zer0 ; haitien ; VDB en solo, pas "ex-VDB" ; orphelin arrive en 2062 (retirer "gamin sans nom de Dogtown") ; nom donne par Slider ; echelles et fausse modestie (renvoi Power_Scaling).
  - Yor : scaling corrige ; Soulkiller NetWatch ; origine actee (AI_Devourer_V0.94) ; image recue.
  - V : Sandevistan, pas de deck ; meilleure des Valentinos au Sandevistan ; sommet physique en fin 2077.
  - LaGuerre : canon verifie (vivant pendant The Damned ; mort en 2077 dans sa planque de l'Eventide, evoquee dans I've Seen That Face Before ; tueur [INCERTAIN]). Retirer "a reverifier".
  - Rhyne et Holt : aligner sur Night_City_2077 S4 (Rhyne mort, cause [INCERTAIN] ; Holt ex-adjoint, candidat). Detail du cyberpsycho : C2 ouvert.
  - Lilith : "Cible 1" -> cible.
  - Sans fiche, restent en SB5 comme domicile du fait : Jackie, Dex, Johnny, Smasher, famille Arasaka, Takemura, Brick, Royce, Patricia et Dum Dum, Zaria, Regina, Meredith, Rogue, Gary, Mr. Hands, Alex.
- SB6 : relire les mentions de point de depart ; rien d'autre releve.
- SB7 : ajouter le Soulkiller NetWatch (outil de Yor, copie partielle d'engramme, herite du projet AI_Devourer).
- SB8
  - Mysteres : fermer "Origine de J0RMUN94ND" (actee, lot IA) et "Nature exacte de Lilith" (dixieme cercle acte, lot IA).
  - Tchekhov "LaGuerre indic FIA" : aligner sur le canon verifie.
  - Tchekhov "Trahison de T-Bug" : "plante au T0 (plan B)" -> plante au premier beat de R1.
- SB9 : inchange.

### S3. Resume.md (W1 -> W2)
- Intro : "Etat arrete a l'ouverture de R0" (au lieu de la veille du Konpeki).
- S2 : orphelin arrive en 2062 avec les refugies (retirer "gamin sans nom", "entree par LaGuerre") ; Dogtown en 2070, a 15 ans ; nom "Null" donne par Slider ; handle Zer0.
- Cibles de Yor : retirer "dans l'ordre" ; le mur en dernier, garde-manger ferme.
- S4 : titre -> "Etat du monde a l'ouverture de R0" ; retirer "T-Bug demande a Silas de rester en plan B" ; Rhyne mort, cause [INCERTAIN].
- Integrer : Yor devance Alt ; V au Sandevistan.

### S4. Journal
- Proposer au worldbuilder une purge de ce journal : tours soldes compresses en une ligne, seules les sections vivantes gardees en detail. [A VALIDER]
- Puis W18.

## Sources (worldbuilder)
- Image de Yor : RECUE, integree en IA/J0RMUN94ND.md S5.
- Images de Silas (lames mantis, hack) : RECUES 2026-09-19. Description validee (cf. decisions).
- Image de V : RECUE 2026-09-19 (figurine, art promotionnel). Integree en Personnages/V.md S2.

## Environnement technique (2026-09-19)
- SPEC courante : `SPEC_BIBLE_LORE_WIKI_v8_5.md`. SPEC_CODEX : `v8_4.md`. Verifies par listing reel de Config/.
- Rev. v8.5 : la fiche d'arc porte le DEROULE de l'etape ; troncature deplacee de l'OUVERTURE a la SORTIE de l'etape. Les Instructions Wiki ont ete reecrites en consequence (MODE OUTIL - FICHES D'ARC).
- Listing de dossier : `github.com/.../tree/...` peut renvoyer 403 selon l'environnement. Methode de listing remplacee par un clone sans blobs. Cf. Instructions Wiki S8.

## Decisions actees - lot Power_Scaling (2026-09-20)

### Architecture
- Deux pages. Scaling_Numerique : entites sur trois axes (planification, etalon Blue Eyes ; taille, etalon Alt ; puissance brute, etalon Cynosure) et netrunners par paliers de reputation, avec talent et specialite. Scaling_Physique : combat hors hack, Smasher et V (fin 2077) au sommet, plus l'axe emprise physique des entites. Les runners figurent sur les deux : talent en numerique, corps en physique.
- Etat au point de depart ; section Deltas dates vide, alimentee a chaud.
- Sommaire : DEROGATION, plafond porte a 20 000 caracteres. Pas de resserrage.

### Echelle numerique
- Croisements : Alt, planification haute sous Blue Eyes, puissance brute haute sous Cynosure. Blue Eyes, taille sous Alt, puissance brute sous Cynosure. Cynosure, planification basse, taille non mesuree. Lilith basse, petite, petite.
- Blackwall : au-dessus de Yor au point de depart, en taille et en puissance brute ; les autres repas la rendent capable du dessert.
- Bartmoss : hors echelle, puissance dormante non mesuree.
- Yor et Alt : a leur rencontre (avant 2075), Yor nettement depassee, a fui a temps. Puis absorptions dans le vieux Net, puis via Silas. Hierarchie renversee : Alt a peine sous Yor au point de depart. REMPLACE "egale Alt en taille".
- Soulkiller NetWatch : version NetWatch du tueur d'ame, copie PARTIELLE d'un engramme avant de griller un humain (un peu de data). Heritee du projet AI_Devourer, perdue par NetWatch avec lui ; Yor seule la possede. Nom [INCERTAIN].
- Paliers netrunners : Legendes, Blackwall-armes, Elite, Pro, Rue. Slider Elite, Mosley Pro haut, Dorsett Pro, runners corpo Pro a Elite.
- Silas. Connecte : Blackwall-arme. Deconnecte : reputation Elite sous Brigitte et Slider ; il se fait passer pour moins doue que ses mentors, qui se doutent qu'il ment, pas a quel point. Niveau reel : numero 1 de l'Elite. Talent pur : niveau Alt et Bartmoss, specialite percage d'ICE (Bartmoss : conception de daemons).

### Echelle physique
- Paliers : Sommet (Smasher ; V fin 2077) ; reference 2076 (David Martinez) ; Elite (Takemura, Reed, Hansen, MaxTac, Cerberus, Placide, Silas ; Silas pilote par Yor en haut) ; Pro (V au point de depart en haut, Jackie, Alex, vrais cyberpsychos en haut) ; Rue. T-Bug : douee sur le Net seulement.
- Yor pilotant Silas : ignore les limites du corps (dechirures, lesions), le fait bouger comme un predateur, un animal sauvage.
- V : Sandevistan des le depart, pas de deck ; meilleure utilisatrice de Sandevistan des Valentinos avant le Konpeki ; build a la David Martinez, moins accro a la chrome. Hors echelle numerique.
- Emprise physique : Blue Eyes > Yor > Lilith = Cynosure > Alt.

### Ordre des arcs (correction worldbuilder)
- L'ordre des cibles et des arcs inscrit au rappel de cadrage n'avait jamais ete donne par le worldbuilder. RETIRE de 9 pages et du Sommaire ; reste a retirer de la BIBLE et de Resume au B3.
- Fixe : R0 = un contrat de Mr. Hands (intro). R1 = premier beat, T-Bug contacte Silas directement, sans fixer, pour l'avoir en assurance ; puis le Konpeki, que Silas travaille depuis son appartement de Coastview. Puis ellipse de convalescence de V, pendant laquelle Silas traque Lilith.
- La suite : garde-cap pre-roadmap du worldbuilder (grandes lignes, Tchekhov, pre-decoupage en roadmaps). Seul point fixe au-dela : le Blackwall en dernier.
- Lecon de methode : une ligne de cadrage n'entre ici qu'avec sa source (date et parole du worldbuilder). Un ordre, un calendrier ou une orientation d'arc sans source n'est pas acte.

### Point de depart (2026-09-20)
- Point de depart du RP = OUVERTURE DE R0 (et non plus la veille du Konpeki).
- R0 = arc d'introduction : un contrat de Mr. Hands. Il pose le decor de Silas : Voodoo Boy en solo, genie du hack, symbiose avec Yor, neutre dans les conflits internes aux VDB, proche de Brigitte, Placide et Slider.
- Appel de T-Bug (plan B, sans fixer) : PREMIER BEAT DE R1. Choix laisse au MJ par le worldbuilder ("peu importe") ; option propre retenue : l'appel sort des fiches noyau.
- Date de R0 : [INCERTAIN], anterieure au braquage (fin avril-debut mai 2077). Si elle precede le 30/01/2077, Silas a 21 ans au point de depart (2076 - 2055) ; sinon 22 (2077 - 2055). Question posee au worldbuilder. [A VALIDER]

## Decisions actees - lot Personnages (2026-09-19)

### Cadrage
- Fichier de Brigitte : Personnages/Maman_Brigitte.md. Le renvoi Voodoo_Boys S3 vers Personnages/Brigitte.md est a corriger (sous-lot 2, W4).
- Rosalind Myers et Kurt Hansen ajoutes au lot (Hansen dirige Dogtown, ou Silas a grandi).
- Placement : toutes les fiches du lot en Personnages/ neutre. Silas est un OC promu au lore ; ses liens en font partie.
- Gabarit : precedent du lot IA. Trajectoire datee vide a la genese ; le detail canon post-T0 reste en Chrono_2077, dans les pages de faction, ou ci-dessous en matiere roadmap.
- Lexique creole de Silas : section de Silas_Null.md (un satellite passerait sous le plancher SPEC).

### Silas
- Description physique : proposition MJ validee, lue sur les deux images, SAUF "yeux mi-clos" (retire).
- Filaments violets lumineux (mains, poignets, pieds) : DIEGETIQUES, visibles des netrunners avances seulement. Signature visuelle des hacks via Yor.
- Gouts : boissons energisantes (Chromanticore) ; cuisine pimentee et/ou creole.
- Nom : "Silas" est tout ce qui lui reste de parents qu'il n'a jamais connus. "Null" lui a ete donne par Slider (Wilky LaGuerre), pour qui tout le monde merite un nom.
- Enfance : Pacifica avant Hansen, parmi les Voodoo Boys. Placide en "grand frere". Brigitte et Slider : figures d'autorite, puis mentors, chacun a sa maniere. Lien avec Brigitte anterieur au schisme.
- Deck : NetWatch Netdriver, prise sur un netrunner NetWatch qu'il a grille a 14 ans, son premier mort, sous la supervision de Slider. Calcul : 14 ans du 30/01/2069 au 29/01/2070. Modifie depuis ; son matos compte parmi les meilleurs des VDB.
- Chrome nerveuse : Kerenzikov, accelerateur synaptique, nanorelais, tous modifies et boostes. Le deck occupe l'unique slot d'OS : pas de Sandevistan.
- QG : appartement a Coastview, attribue par Brigitte.
- Fixers : Mr. Hands surtout ; aussi Rogue et Regina Jones ; un peu tous les autres. Reputation : fantome dans ses contrats, sans coeur tant que la mission est remplie, sang-froid a toute epreuve.
- Schisme : a suivi Slider sans couper les ponts avec Brigitte ; a refuse de servir de balance a l'un comme a l'autre. DETESTE LES INDICS. Ironie armee : Slider est un indic FIA, Silas l'ignore (Tchekhov "LaGuerre indic FIA" aiguise).
- Formation : par Slider encore voyant, puis aveugle.
- Statut chez les VDB : pas sorti. Parti en solo, liens encore forts, toujours a sa place parmi eux. Remplace "ex-Voodoo Boy".
- A reporter dans Silas_Null.md (acte avant ce lot) : cout de la symbiose - accumulation de chrome de systeme nerveux pour accueillir Yor, reflexes aberrants, humanite decroissante, loin d'Adam Smasher mais meme pente ; sans Yor, cyberpsychose. Mecanique complete : IA/J0RMUN94ND.md S6.
- Creole haitien : parle creole avec les VDB, emploie lui-meme quelques expressions. En fiche : le FAIT (langue, avec qui, depuis quand) + le lexique, ASCII romanise. Registre et tics de voix : CODEX ANNEXE_PNJ. Termes retenus a reporter au SB2 de la BIBLE au B3.
- Page relations : premier jet de texture par le MJ, valide ensuite par le worldbuilder. Casting : Yor, Slider, Brigitte, Placide, T-Bug, Mr. Hands, Rogue (le juge tres fiable), Regina Jones (le trouve tres efficace, surtout en chasse aux cyberpsychos).

### Autres fiches
- Blue Eyes : les autres hommes aux yeux bleus du canon sont des IA asservies. Integre en Personnages/Mr_Blue_Eyes.md S3.
- Bryce Mosley : a capture un fragment de Yor, qui s'est autodetruit. Integre en Personnages/Bryce_Mosley.md S5. Suite : matiere roadmap.
- V : femme ; parcours Gosse des rues, divergence Valentinos (cf. second tour) ; look des arts promotionnels (image fournie).

### Second tour (2026-09-19)
- C-S1 RESOLU : Silas est deja avec la communaute haitienne avant son arrivee a Pacifica (2062, a 7 ans), orphelin parmi d'autres, gere par le clan sous Brigitte et Slider. Lieu de naissance : non fixe ("peu importe") [INCERTAIN]. Remplace "ne a Pacifica".
- C-S2 RESOLU : Silas est HAITIEN, autant que les autres VDB. Remplace "non haitien". L'item "precedent canon de non-Haitiens chez les VDB" devient sans objet.
- C-S3 PARTIEL : le POURQUOI est acte, pas le QUAND. Il suit Slider, plus proche de ses idees (chasse aux corpos plutot que percer le mur). Il le voit devenir aveugle et accepte sa version : une ICE trop bien protegee lui a grille le cortex visuel. Il le suit au schisme sans tourner le dos aux autres VDB, fait des boulots pour eux tant que ce n'est pas contre Slider.
- C-S4 RESOLU : n'a jamais quitte Pacifica. Deux maisons : le QG de Slider (Dogtown) et l'appartement offert par Brigitte (Coastview).
- C-S5 RESOLU : les fragments portent aussi la signature violette, mais vague : plus mythe que certitude. NetWatch S4 et J0RMUN94ND S4/S8 mis a jour ; "aucun pattern identifie" tient.
- C-S6 RESOLU : manie validee (doigts a la tempe pour lancer un hack).
- C-S7 RESOLU : Yor mange l'IA des vrais cyberpsychos que Silas chasse pour Regina ; il les livre brises et plus psychotiques ; Regina recoit des echantillons corrompus.
- C-S8 : lexique propose REFUSE. Methode : le worldbuilder dictera ce qu'il veut en francais, le MJ traduira. Section a ajouter a Silas_Null.md le moment venu ; termes retenus au SB2 au B3.
- C2 (Rhyne) : laisse [INCERTAIN], a trancher plus tard. Night_City_2077 S4, Chrono_2077 S1, Peralez S4 mis a jour.
- C-V1 RESOLU, DIVERGENCE : V a grandi dans le giron des Valentinos, comme Silas chez les VDB. Jackie Welles en grand frere protecteur (miroir de Placide pour Silas) ; Mama Welles et Padre en figures d'autorite.

### Troisieme tour (2026-09-19)
- Budget : DEROGATION pour IA/J0RMUN94ND.md, plafond porte a 12 000 caracteres (au lieu de 8 000). A 7 942 au W3.
- C-S3 RESOLU : schisme et depart de Slider (et de Silas) pour Dogtown en 2070, juste avant la secession de Hansen. Silas n'est pas enferme a Dogtown : c'est la qu'il passe le plus clair de son temps.
- C-S9 RESOLU : le handle devient "Zer0", derive de Null, pour plus d'anonymat. "Zer0_Null" est abandonne.
- Relations : texture du premier jet VALIDEE, avec corrections. Slider l'appelle "Zer0" ou "Null", selon ; Silas l'appelle "Slider" ou "LaGuerre", selon. Silas n'a jamais rencontre Mr. Hands en personne (jusqu'au T0).
- T-Bug et Silas se sont rencontres sur des forums de runners du dark net.
- Lexique creole : le worldbuilder a fixe les registres (colere par paliers, la ou Silas perd le langage poli ; frustration ; excuses ; le mur noir ; l'ordre "Yor, bouffe-le"). Traduction MJ integree en Silas_Null.md S10. "Miray nwa" pour le mur noir (souvenir du worldbuilder : "murai nwa"). Le reste : balise [Creole] en jeu. Termes a reporter au SB2 au B3.

### Quatrieme tour (2026-09-19)
- C-S10 RESOLU : Silas ignore que Brigitte est derriere le vol de la Relic. Il est sur le Konpeki en freelance, pas en tant que VDB. Integre en Silas_Null W3 S4 et Maman_Brigitte W2 S7.
- Lexique : "Yor, vale l." (avale-le) ajoute a "Yor, manje l.".
- Tic culturel "tchwip" (le tchip haitien ; onomatopee, verbe tchwipe/tuipe/kuipe/tchipe ; se fait, ne se dit pas) : registre de la colere, de l'agacement, de la frustration. Mot au lexique (Silas_Null S10) ; frequence et placement a reporter en CODEX ANNEXE_PNJ (Silas) au CODEX V1.
- Johnny Silverhand et Gary le Prophete : pas de fiche prevue. Renvois morts repointes vers leur domicile actuel (Alt_Cunningham S2 -> Sites_Arasaka S3 ; Lilith S3 -> Night_Corp S3). Lot complementaire possible si le worldbuilder le veut.

## Conflits ouverts - attente worldbuilder
- SOLDE (2026-09-20) : point de depart. Tranche : ouverture de R0 ; appel de T-Bug en premier beat de R1. Propagations : HANDOFF B3 S1.
- Date de R0, donc age de Silas au point de depart (21 ou 22 ans). [A VALIDER]

## Propagations a executer apres C-S1 a C-S4 (actees sur le fond, formulation dependante)
- FAIT : Voodoo_Boys (W4-W5), Chrono_Univers (W2-W3), Chrono_2077 W3, Night_City_2077 W3, Peralez W2, Pacifica_et_Dogtown W2 (S8), Barghest W2 (S5).
- RESTE, au B3 : repris integralement dans HANDOFF B3 (S2, S3).
- FAIT : Lieux/Sites_Arasaka.md S2 (W2) : braquage fin avril ou debut mai 2077 ; renvoi vers _Implications retire (document non fetchable en narration).

## Canon verifie (2026-09-19)
- Wilky LaGuerre, alias Slider (fandom) : ex-bras droit de Brigitte. Rupture sur l'ideal : elle veut percer le mur, lui prefere casses corpo et assassinats par le Net et juge le mur trop dangereux. Un casse attire la FIA, qui l'aveugle definitivement puis en fait un indic par chantage. Fuit Pacifica pour Dogtown, y rejoint des VDB deja installes, prend la tete d'un trafic de logiciels illegaux ; la FIA l'y rattrape. Yeux blancs. Planque : Eventide Resort & Spa, Dogtown. Vivant pendant The Damned (V et Reed passent par lui pour joindre Songbird) ; mort en 2077 dans sa planque, evoquee dans I've Seen That Face Before. Tueur [INCERTAIN]. Rapport medical : 39 ans, date du rapport inconnue.
- The Rescue (Sandra Dorsett) : vers avril 2077, avant le braquage. Cf. A reverifier.
- Project Oracle : reference de la puce de Gary decryptee, selon PC Gamer. Integre en Night_Corp W3.

## Matiere roadmap (post-T0, hors fiches noyau)
- R1, premier beat (2026-09-20) : T-Bug contacte Silas directement, sans fixer, pour l'avoir en assurance sur le Konpeki. Il y est en freelance, pas en tant que VDB. Motif, cote T-Bug : elle le sait meilleur qu'elle.
- Mosley : sa prochaine rencontre avec Yor sera sa fin (decision worldbuilder 2026-09-19).
- Detonation de C-S10 : quand V appelle Mr. Hands, Hands lui donne le contact de Silas (decision worldbuilder 2026-09-19).
- Mr. Hands : jamais rencontre en personne avant R1 (formulation du worldbuilder, qui laisse une rencontre possible a partir de R1).
- Blue Eyes, Dream On : appel holo anonyme a V, qui evoque sa Relic ; Blue Eyes sur une terrasse, main a la tempe.
- Blue Eyes, The Killing Moon : fenetre du Tycho Terminal ; quai du monorail, parapluie.
- Blue Eyes, Path of Glory (Johnny et Rogue, ou V seule) : surveille l'assaut d'Arasaka et envoie ses gens voler equipement et donnees ; engage V pour voler un cache de donnees d'un client d'un casino du Crystal Palace ; rencontre a l'Afterlife ; fait couper les capteurs de la station.
- Peralez, Dream On : verite dite -> maire paranoiaque ; mensonge -> maire heureux mais manipule (cf. A3). Elizabeth avait d'abord propose l'enquete I Fought the Law a Judy Alvarez, qui a recommande V.
- Mosley, I Walk the Line : Brigitte et Ti Neptune pieges en stase ; coupe la liaison de V avec Placide pour negocier.
- Blue Eyes : ce que Silas et Yor savent de lui au T0 [INCERTAIN].

## Trous ouverts - lot IA
- Annee exacte de creation de J0RMUN94ND [INCERTAIN]. Pose "annees 2040", projet contemporain du Blackwall (2044). A fixer quand le worldbuilder voudra.
- Ce qu'Alt Cunningham sait de J0RMUN94ND APRES la percee de 2075 [INCERTAIN]. Non tranche. Detonation naturelle : arc Alt et Voodoo Boys (Passe 2).
- Nombre et nature des entites de Cynosure / Songbird [INCERTAIN]. Reste ouvert, SB8.
- Etat en 2077 des Transcendentaux et Fantomes co-batisseurs [INCERTAIN].
- Sort de l'IA extraite de Skippy [INCERTAIN].
- Nature du virus qui a fragmente Delamain [INCERTAIN].
- Lieu exact du signalement de cyberpsycho de Zaria Hughes [INCERTAIN].
- Lien eventuel entre Cerberus et les entites canalisees par Songbird : non etabli.

## Dettes de build a solder
- SOLDEE : notice Blue Eyes de Net_et_Blackwall S6, compressee en renvoi (W5, 7 668 car., sous le plafond). Renvois repointes en Entites_du_Blackwall S6, J0RMUN94ND S7, Night_Corp S4, Chrome_et_Cyberpsychose S2bis.
- Renvois en avant vers Personnages/ : TOUS SOLDES.
- SOLDEE : Sommaire, derogation a 20 000 caracteres (2026-09-20).
- SOLDEE : renvois vers Power_Scaling/, repointes vers les pages livrees (J0RMUN94ND S4, Alt S3, Lilith S4, Entites S3, Silas S7, Netrunning S6).
- BIBLE B3 et Resume : dette consolidee dans HANDOFF B3.

## Extraction transcript video lore (recu 2026-09-18, audio->texte avec erreurs)

Normalisation des noms : Rasaka = Arasaka ; Kengtao = Kang Tao ; Dexter Di Shur = Dexter DeShawn ; compte Peki Plaza = Konpeki Plaza ; Jackie Wells = Welles ; Johnny Silverend = Silverhand ; TU = CHOOH2 ; Luus Rein/Rin = Lucius Rhyne ; wellt/Holt = Weldon Holt ; Perales/Perale = Peralez ; Rash Bartmos = Rache Bartmoss ; Siri = Ciri ; Polyhistore/Polyistor = Polyhistor ; tyomanta/Hiromanta = Tyromanta ; Blue Ice = Blue Eyes ; Nibles = Nibbles.

### A. Faits de jeu (canon, a integrer)
- A1. Konpeki Plaza : pendant la scene du penthouse, Adam Smasher est marque "vous a repere" par les optiques de detection, mais n'agit pas. Fait de jeu ; sens non explique. Cible : Chronologie/Chrono_2077.md, roadmap Konpeki (Passe 2).
- A2. Gary le Prophete (Watson, pres de l'appartement de V) : complotiste ; envoie V voler une puce ; disparait ; son disciple raconte un enlevement par des hommes en costume aux yeux bleus. Puce : "techno-necromanciens", "la nuit vient, la nuit eternelle". Cible : Personnages/Mr_Blue_Eyes.md, Factions/Night_Corp.md. NOTE : la scene de l'echange est aussi la source de la formule du dixieme cercle, integree en IA/Lilith.md S3.
- A3. Affaire Peralez (Dream On) : Jefferson Peralez, candidat maire (l'ancien maire Lucius Rhyne a ete assassine) ; "cambriolage" dont il ne se souvient pas ; societe de securite SSI qui couvre ; piece secrete de surveillance ; base SSI piratee -> le couple est cobaye d'une experience de controle mental. Voix inconnue a V : "Nous savons qui vous etes, ce que vous etes et ce que vous voulez." Fins : verite dite -> Jefferson maire et paranoiaque ; verite tue -> maire heureux mais manipule. Homme en costume aux yeux bleus observe la conversation sur le toit. Cible : Personnages/Peralez.md, Mr_Blue_Eyes.md.
- A4. Sandra Dorsett : sauvee par V au debut ; contenu annexe : Night Corp conditionne et manipule l'esprit de ses employes, voire de personnalites plus importantes, par des IA. Cible : Personnages/Sandra_Dorsett.md, Factions/Night_Corp.md. [IMPLICITE] pour le mot "IA" : a reverifier sur la source (shards Night Corp).
- A5. Lucius Rhyne : assassine ; enquete annexe -> Weldon Holt, son bras droit, implique ; un cyberpsycho aurait servi d'instrument [INCERTAIN sur le detail cyberpsycho]. Cible : Night_City_2077.md (maire), Chrono_2077.md.
- A6. Delamain (Epistrophy) : voitures IA qui deviennent autonomes, personnalites distinctes, refus d'ordres, fuite. INTEGRE en IA/IA_Mineures.md S3.
- A7. Phantom Liberty : Songbird contaminee par des IA hostiles, ca la tue. Son billet pour la Lune vient d'un "intermediaire", corpo banal, costume discret, cheveux noirs, yeux bleus, qui lui a pose des questions auxquelles elle seule pouvait repondre, dont sur le mur noir. Blue Eyes apparait plusieurs fois dans le DLC. Cible : Songbird.md, Mr_Blue_Eyes.md.
- A8. Fin The Sun : Blue Eyes confie a V le casse du Crystal Palace (station spatiale). Cible : Chrono_2077.md.
- A9. Biotechnica : vaccins, medicaments, CHOOH2, SCOP ; nourriture de masse a base d'insectes, fermes proteiniques fermees ; nourriture fraiche = luxe. Experiences de clonage. All Foods (Northside, Maelstrom) affilie a Biotechnica ; produits avec 3,5 % d'ingredients d'origine inconnue. Cible : Factions/ (corpos), Lieux/Watson.md.
- A10. Bartmoss : cadavre dans un congelateur cryogenique, trouve par V en suivant un signal inconnu. Maitre Zen : invisible pour Johnny. INTEGRE en Net_et_Blackwall.md S2.
- A11. FF:06:B5 : statue, moines, cube dore, chapelle de Polyhistor, Tyromanta, ouroboros, borne d'arcade, coordonnees, le Surveillant. Le fil est bien articule autour d'un ouroboros - le lien est reel, mais META. FERME, hors lore du RP. Aucun rattachement a J0RMUN94ND, malgre l'imagerie du serpent. Decision worldbuilder 2026-09-19.
- A12. Animaux quasi disparus ; chats sphynx (Nibbles) ; bakeneko selon Takemura. Texture.
- A13. Chambre 301 : inscriptions "je ne suis pas moi-meme". Texture.

### B. Theories de fans (interdites sauf adoption OOC explicite)
- B1. ADOPTE (2026-09-18) : Blue Eyes = IA sans nom connu ayant ecrase la psyche d'un homme ; identite de l'hote effacee de tous les systemes ; noyau de l'IA dans ce corps hors Net. PRECISION 2026-09-19 : le noyau y est INTEGRALEMENT, il dirige tout depuis ce corps, qui est un cadavre habite.
- B2. ADOPTE par implication de B1 : Night Corp, SSI, Peralez = instruments de l'IA Blue Eyes. Le mot "ruche" n'est pas retenu.
- B3. ADOPTE : vrais cyberpsychos = IA dans des corps de chair. Songbird a Cynosure, Zaria Hughes. Ecrit en Monde/Chrome_et_Cyberpsychose.md S2bis.
- B4. ADOPTE : la Lune est un piege de Blue Eyes pour absorber les entites de Songbird. Ecrit en Factions/FIA_NUSA.md S5.
- B5. ORIENTE OUI, tranche en fin de roadmap (Passe 2).
- B6. INDIFFERENT : reste [INTERPRETATION], rumeur non tranchee (Night_City_2077.md S2).
- B7. ADOPTE : virus declenche a la mort du corps ; conscience survivante hors corps comme Alt, jamais amalgamee. Maitre Zen = Bartmoss. Ecrit en Net_et_Blackwall.md S2.
- B8. MYSTERE FERME : FF:06:B5, cube, ouroboros. Cf. A11.
- B9. HORS PERIMETRE, confirme.

### C. Points du transcript a reverifier avant integration
- C1. SOLDE (2026-09-19) : CN-07 est bien une IA, texte canon du databank Carpe Noctem (fandom). Integre en Personnages/Sandra_Dorsett.md S2.
- C2. Rhyne / Holt : role exact d'un cyberpsycho dans l'attentat.
- C3. Bartmoss : version canon de sa mort (frigo, arret cardiaque, date) vs declenchement du virus.
- C4. SOLDE (2026-09-19) : SSI confirme. Integre en Personnages/Peralez.md S5.

## Decisions actees - lot IA (2026-09-19)
- Origine de J0RMUN94ND : creee par NetWatch comme outil IA chargee d'en neutraliser d'autres ; deployee et scellee du cote vieux Net pour le purger de l'interieur ; rebellion ; projet detruit et abandonne ; changement de strategie et de signature ; meconnaissable par ses createurs ; liberee par Silas en 2075.
- Nom : AI_Devourer_V0.94 a la creation (NetWatch). Auto-renommee J0RMUN94ND une fois libre, leet sur JORMUNGAND (correspondance position par position, O->0 G->9 A->4), le "94" aux septieme et huitieme caracteres inscrivant son versioning d'origine. NetWatch ignore ce nom. "Yor" est le surnom donne par Silas.
- Metaphore du serpent : CONSTRICTION du monde = contention des IA. Pas la devoration (confusion initiale avec le God Devouring Serpent d'Elden Ring, corrigee par le worldbuilder). Elle garde la fonction de contention et change le beneficiaire.
- Avatar : image fournie. Fillette, age apparent 6 ans [INTERPRETATION]. Description en IA/J0RMUN94ND.md S5.
- Cout de la symbiose : l'humanite de Silas. Yor peut prendre le controle du corps. Yor est tres attachee a Silas.
- Alt Cunningham a croise Yor avant 2075 et a failli l'absorber. Precise le 2026-09-20 : Yor nettement depassee, a fui a temps ; hierarchie renversee depuis.
- Lilith : le dixieme cercle = extension de Dante, le cercle des demons numeriques, superstition de Maelstromers dont Lilith profite ; esthetique satanique adoptee ; alias "Queen Lilith" (canon). Elle sait que les IA cherchent a se posseder entre elles pour gagner en puissance de calcul et en data ; elle ignore Yor.
- Reunion Maelstrom / corpos de The Prophet's Song : les corpos sont Arasaka, balise [DIVERGENCE RP] (le canon consulte ne nomme pas les parties et situe la scene a Kabuki).
- Economie de l'appetit : IA mangee = puissance de calcul + experience (data). Engramme mange = data brute, moins interessante ; Yor le recupere plutot que le gacher quand elle grille un humain. CN-07 est une proie. ICE et daemons = menu fretin. IA de service = amuse-bouches. Yor veut tout.
- Braindances : pas des IA. Hors perimetre du lot.
- Blue Eyes : domicile unique en Personnages/Mr_Blue_Eyes.md. Regle de placement derivee : la fiche vit la ou l'entite se joue.

## Decisions actees (rappel de cadrage)
- Prota : Silas "Zer0" Null (handle change le 2026-09-19, ex-"Zer0_Null"), masculin, ne le 30/01/2055, fiche NEUTRE.
- IA : J0RMUN94ND (Yor), agglomerat sous paradigme unique, fiche NEUTRE. Noyau hors Net dans le systeme nerveux de Silas.
- Scaling Yor (corrige 2026-09-20) : ecrase Lilith ; egale Blue Eyes en planification et les entites de Cynosure en puissance brute ; devance Alt d'une courte tete ; sous le Blackwall en taille et puissance brute.
- Convergence des buts : Yor gardienne unique des IA, Silas seul proxy ; Silas martyr consentant.
- Ordre des arcs : RETIRE le 2026-09-20, jamais donne par le worldbuilder. Fixe : R0 -> R1 Konpeki -> ellipse (Silas traque Lilith) ; puis garde-cap ; le Blackwall en dernier. cf. Decisions actees - lot Power_Scaling.
- Blue Eyes absorbe les IA lui aussi : concurrent direct de Yor sur le meme gibier.
- Bartmoss : hors liste de cibles a ce jour ; a trancher en roadmap.
- Trahison de T-Bug par Silas au Konpeki : matiere de roadmap (Passe 2).
- Point de depart : ouverture de R0 (2026-09-20).
- NetWatch : obstacle, pas cible. Le mur = garde-manger ferme, ultime repas de Yor.
- Sources validees : wiki Cyberpunk fandom, Edgerunners, lore Cyberpunk 2020/RED.
- Limites : aucune, sauf sexualite (hors objectifs de Silas et de Yor).

## Regles de forme (worldbuilder, 2026-09-19)
- Creole haitien, tous threads (build et jeu) : regle ecrite en BIBLE SB0 (B2), a reporter dans le CODEX V1, ANNEXE_STYLE, au CODEX BUILD. Pas dans les Instructions RP (decision worldbuilder).

## A reverifier
- SOLDE (2026-09-20) : braquage fin avril ou debut mai 2077, reporte en Lieux/Sites_Arasaka.md S2 (W2). Jour [INCERTAIN].
- Sous-district exact du Konpeki Plaza dans Watson.
- Nom du traite de fin de guerre d'Unification.
- Developpe exact de R.A.B.I.D.S.
- Population de Night City en 2077.
- Date de debut de la relation Alt / Johnny : une source secondaire donnait "2020", probablement une confusion avec le nom du JDR Cyberpunk 2020. Non integree.

---

FIN_WIKI__IMPLICATIONS
