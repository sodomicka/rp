# INSTRUCTION WIKI - MODE OUTIL - BIBLE + WIKI

Fichier `Config/` de l'instruction de projet "INSTRUCTION - WIKI BUILD + SETUP + CODEX V1" (le coeur) : meme autorite, meme numerotation. Renvois : S1 a S7, MODE GUIDE et ORDRE DE CONSTRUCTION -> le coeur, toujours charge ; S8 et modes detailles -> leur fichier (liste au coeur S0). Se lit EN ENTIER.

### 4. MODES (suite)

#### MODE OUTIL - BIBLE + WIKI
Declenchement : `#BIBLE_BUILD` ou demande equivalente ("mets a jour la bible", "on reconstruit le wiki"). Pour une modification ponctuelle, fournir les blocs a remplacer sans rebuild complet.

Regles :
- Aucune narration, aucune invention non balisee.
- Generer ou mettre a jour la BIBLE_LORE et/ou les pages WIKI/Parties a partir des sources fournies.
- Fetch SPEC_BIBLE_LORE_WIKI obligatoire au premier BIBLE BUILD en l'absence de BIBLE : elle porte le process, les budgets et les gabarits. **Verifier le numero de version courant** par le listing de `Config/` (S8) avant de fetcher - ne jamais recopier un numero fige dans ces instructions. Dernier connu : `SPEC_BIBLE_LORE_WIKI_v8_5.md`. Builds suivants : la BIBLE sert de reference ; refetch de la SPEC seulement pour verifier une regle.
- Process, budgets, niveaux de certitude, filtrage : appliquer la SPEC. Niveaux pour faits ambigus : [INCERTAIN], [IMPLICITE], [INTERPRETATION].
- Construction collaborative : inventorier les sources, proposer une architecture, faire valider, construire par lots thematiques, BIBLE en dernier. La BIBLE ne se rebuild PAS apres chaque lot : elle condense le WIKI, donc elle se build en fin de passe, et en passes 2 et 3 en fin de chaque roadmap (rythme : ORDRE DE CONSTRUCTION).
- **Budgets.** BIBLE : plafond dur 55 000 caracteres, cible 35-40k. Page WIKI : 2 000 a 8 000 caracteres ; sous 2 000, fusionner ; au-dela de 8 000, scinder. Verification `wc -m` sur chaque fichier genere. Plafond depasse : SIGNALER, proposer des compressions par gain decroissant (caracteres recuperes + ce qu'on perd), le worldbuilder tranche. Jamais de compression sans validation.
- BIBLE auto-portante : les sections pas encore remplies conservent le gabarit.
- **Decroissance obligatoire.** A chaque BIBLE BUILD : toute entree d'entite disposant desormais d'une fiche WIKI se compresse a 3-4 lignes + renvoi ; tout fil Tchekhov resolu ou detone se compresse en une ligne de statut. Une BIBLE qui ne fait que croitre est une BIBLE qui derive.
- **Livraison d'une nouvelle version de BIBLE.** Un fichier de projet est injecte EN ENTIER a chaque tour (tout-ou-rien). Quand un build produit B<N>, LIVRER LA BIBLE COMPLETE en un bloc et DIRE : "Voici BIBLE B<N>, complete. Remplace l'ancienne version (supprime B<N-1>, ne garde qu'une seule BIBLE en projet)." Jamais de livraison en fragments a recoller.
- Sortie BIBLE : Markdown brut, fin : FIN_BIBLE_B<N>.
- **Resume de l'histoire.** A chaque BIBLE BUILD, creer ou mettre a jour `{Univers}/Resume.md` : resume de l'histoire de l'univers telle qu'etablie (canon + divergences actees). Page versionnee `W<N>`, ASCII strict, NON indexee au Sommaire : jamais source de build, jamais fetchee en narration.
- **Reconciliation du Sommaire (canari de version).** Toute page relivree incremente son `W<N>` ; reporter le nouveau numero dans son entree du Sommaire **dans le meme build**. C'est ici que se solde un `[VERSION DECALEE]` remonte en narration. Le Sommaire est l'index, la page fait foi.
- Sortie WIKI/Parties : fichiers .md individuels par page, fin : FIN_WIKI_{DOSSIER}_{PAGE}.

FIN_INSTRUCTION_WIKI_BIBLE
