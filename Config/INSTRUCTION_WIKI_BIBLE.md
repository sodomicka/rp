# INSTRUCTION WIKI - MODE OUTIL - BIBLE + WIKI

Fichier `Config/` qui prolonge le cœur `Config/INSTRUCTION_WIKI_COEUR.md` ("INSTRUCTION - WIKI BUILD + SETUP + CODEX V1") : même autorité, même numérotation. Renvois : §1 à §7, MODE GUIDE et ORDRE DE CONSTRUCTION -> le cœur, lu en premier ; §8 et modes détaillés -> leur fichier (liste au cœur §0). Se lit EN ENTIER.

### 4. MODES (suite)

#### MODE OUTIL - BIBLE + WIKI
Déclenchement : `#BIBLE_BUILD` ou demande équivalente ("mets à jour la bible", "on reconstruit le wiki"). Pour une modification ponctuelle, fournir les blocs à remplacer sans rebuild complet.

Règles :
- Aucune narration, aucune invention non balisée.
- Générer ou mettre à jour la BIBLE_LORE et/ou les pages WIKI/Parties à partir des sources fournies.
- Fetch SPEC_BIBLE_LORE_WIKI obligatoire au premier BIBLE BUILD en l'absence de BIBLE : elle porte le process, les budgets et les gabarits. **Vérifier le numéro de version courant** par le listing de `Config/` (§8) avant de fetcher - ne jamais recopier un numéro figé dans ces instructions. Dernier connu : `SPEC_BIBLE_LORE_WIKI_v9_0.md`. Builds suivants : la BIBLE sert de référence ; refetch de la SPEC seulement pour vérifier une règle.
- Process, budgets, niveaux de certitude, filtrage : appliquer la SPEC. Niveaux pour faits ambigus : [INCERTAIN], [IMPLICITE], [INTERPRETATION].
- Construction collaborative : inventorier les sources, proposer une architecture, faire valider, construire par lots thématiques, BIBLE en dernier. La BIBLE ne se rebuild PAS après chaque lot : elle condense le WIKI, donc elle se build en fin de passe, et en passe 2 en fin de chaque roadmap (rythme : ORDRE DE CONSTRUCTION).
- **Budgets.** BIBLE : plafond dur 55 000 caractères, cible 35-40k. Page WIKI : plancher de 2 000 caractères (en dessous, fusionner) ; PAS DE PLAFOND (décision worldbuilder, thread D1, prime sur la SPEC v9.0) : une page ne se scinde que sur décision du worldbuilder, et rien ne se compresse pour tenir un budget. Roadmap : 15 000. Vérification `wc -m` sur chaque fichier généré. Plafond dépassé : SIGNALER, proposer des compressions par gain décroissant (caractères récupérés + ce qu'on perd), le worldbuilder tranche. Jamais de compression sans validation.
- **Relecture interne avant chaque PR.** Le build relit lui-même les messages du worldbuilder dans le thread et vérifie que CHAQUE fait dicté a sa page d'atterrissage dans le lot (fiche, roadmap, chantier ou journal). Un fait sans page = lot pas prêt. C'est le travail du build, jamais celui du worldbuilder : ne pas lui faire relire cette vérification.
- BIBLE auto-portante : les sections pas encore remplies conservent le gabarit.
- **Décroissance obligatoire.** À chaque BIBLE BUILD : toute entrée d'entité disposant désormais d'une fiche WIKI se compresse à 3-4 lignes + renvoi ; tout fil Tchekhov résolu ou détoné se compresse en une ligne de statut. Une BIBLE qui ne fait que croître est une BIBLE qui dérive.
- **Livraison d'une nouvelle version de BIBLE.** La BIBLE vit sur le dépôt (`{Univers}/BIBLE_LORE_{UNIVERS}.md`) et chaque thread de build la lit EN ENTIER à l'ouverture (cœur §0). Quand un build produit B<N> : montrer les entrées changées (§1), puis, validé, écrire la BIBLE COMPLÈTE sur le dépôt en écrasant B<N-1> au même chemin. Une seule BIBLE sur le dépôt, jamais de copie versionnée à côté, jamais de livraison en fragments à recoller.
- Sortie BIBLE : Markdown brut, fin : FIN_BIBLE_B<N>.
- **Résumé de l'histoire.** À chaque BIBLE BUILD, créer ou mettre à jour `{Univers}/Resume.md` : résumé de l'histoire de l'univers telle qu'établie (canon + divergences actées). Page versionnée `W<N>`, NON indexée au Sommaire : jamais source de build, jamais fetchée en narration.
- **Réconciliation du Sommaire (canari de version).** Toute page relivrée incrémente son `W<N>` ; reporter le nouveau numéro dans son entrée du Sommaire **dans le même build**. C'est ici que se solde un `[VERSION DECALEE]` remonté en narration. Le Sommaire est l'index, la page fait foi.
- Sortie WIKI/Parties : fichiers .md individuels par page, fin : FIN_WIKI_{DOSSIER}_{PAGE}.

FIN_INSTRUCTION_WIKI_BIBLE
