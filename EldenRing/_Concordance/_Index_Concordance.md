# Index - Concordance

- version : W1
- branche : _Concordance/
- role : filet de recherche. Repond a "dans quelle page du wiki se trouve tel item ?" en un fetch.
- etat : PASSE 0, aucune concordance buildee (elle suit les catalogues).

## Principe

Le Sommaire ne liste pas les items un par un : ils vivent dans des pages de Catalogues/. La
concordance est la table qui rattache un NOM EXACT a la page qui le porte. Elle se construit
apres les catalogues, jamais avant : une concordance qui pointe vers une page inexistante est
pire qu'absente.

## Decoupage prevu

Alphabetique, un fichier par tranche, plafond 8000 caracteres par fichier :
`Concordance_A_C.md`, `Concordance_D_F.md`, ... Les tranches sont ajustees pour equilibrer les
tailles, pas fixees a l'avance.

## Gabarit d'entree

`| <Nom exact en anglais> | <type> | <page qui le contient> |`

## Regles

- Le nom est celui du jeu, en anglais, orthographe exacte du corpus. Aucune normalisation.
- Un item ne peut apparaitre que dans UNE page de catalogue. Si un item merite une fiche propre
  (role narratif), il vit dans Artefacts/ et la concordance y renvoie.
- La concordance ne porte AUCUN fait de lore. C'est un aiguillage, rien d'autre.

---

FIN_WIKI__CONCORDANCE_INDEX
