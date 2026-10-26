# Doigts de Sukuna - Power-scaling

- version : W16

## Unite
- Unite de puissance de l'univers = le doigt de Sukuna.
- 20 doigts = Sukuna complet = 100 pourcent.
- 1 doigt = 5 pourcent. Echelle NON lineaire (resonance) : 2 doigts ne valent pas 10 pourcent.

## Statut de l'unite (in-world / meta)
[DIVERGENCE RP]
- Jusqu'en 2018, l'unite est PUREMENT EXTRADIEGETIQUE : personne ne compte en doigts. Aucune mesure de reserve n'est enseignee nulle part ; clans et universites jaugent par GRADE, point.
- ERE C : une fois Yuji recrute, Satoru et Nisha observent son evolution sur trois doigts et EXTRAPOLENT la courbe. L'unite devient alors diegetique - mais d'usage restreint au couple et a la famille. Clans et ecoles conservent le systeme des grades.
- Consequence de MJ : avant 2018, aucun personnage ne peut citer ni meme penser un chiffre en doigts. La table ci-dessous est un outil d'arbitrage hors-fiction, pas un savoir du monde.
- Doctrine des reserves et des grades : cf. BIBLE SB1 et Pedagogie/Energie_Territoires_1eAnnee.md.

## Formule
P(n) = 5 + 95 * ((n - 1) / 19) ^ 2.35   (en pourcent, pour n >= 1)
P(0) = 0 par convention (aucun doigt = aucune puissance de Sukuna).
- Verification : P(1) = 5 ; P(20) = 100.
- Exposant > 1 : courbe convexe. Les premiers doigts pesent peu, la puissance explose vers la fin = effet de resonance.
- Valeurs au-dela de 20 = theoriques (Sukuna n'a que 20 doigts). Servent a scaler ce qui depasse Sukuna complet.

## Table
| Doigts | Puissance (%) |
|---|---|
| 0 | 0 |
| 1 | 5.00 |
| 2 | 5.09 |
| 3 | 5.48 |
| 4 | 6.24 |
| 5 | 7.44 |
| 6 | 9.12 |
| 7 | 11.33 |
| 8 | 14.09 |
| 9 | 17.44 |
| 10 | 21.41 |
| 11 | 26.02 |
| 12 | 31.30 |
| 13 | 37.26 |
| 14 | 43.94 |
| 15 | 51.35 |
| 16 | 59.51 |
| 17 | 68.44 |
| 18 | 78.15 |
| 19 | 88.66 |
| 20 | 100.00 |
| 21 | 112.17 |
| 22 | 125.19 |
| 23 | 139.07 |
| 24 | 153.84 |
| 25 | 169.49 |
| 26 | 186.06 |
| 27 | 203.54 |
| 28 | 221.95 |

## Bareme de grade (double : fleau / exorciste)
Le label de grade sature vite ; au-dela, c'est le nombre de doigts qui discrimine.
| Doigts | Classe fleau | Classe exorciste |
|---|---|---|
| 0 | - | profane |
| 1-2 | 2 | Semi 2 |
| 3-4 | 1 | 2 |
| 5 | 1 | Semi 1 |
| 6 | Special | Semi 1 |
| 7-8 | Special | 1 |
| 9+ | Special | Special |

Note : Grade Special 1 (rang elite des grandes familles, hors universite d'exorcisme - le fourre-tout pour Special et Grade 1 des clans) est un palier administratif, pas une marche de puissance distincte sur cette echelle.

## Repères chiffrés et courbes A2
- Déplacés pour le poids : cf. Power_Scaling/Doigts_de_Sukuna_reperes.md (repères par entité, courbes A2 2005 -> 2008).

## Synergie et symbiose (combinaison de duos)
Deux combattants de concert ne s'additionnent pas betement : leur puissance combinee suit une loi qui amplifie la somme selon deux leviers de RELATION.
- Synergie (syn) : confiance et coordination, commune a TOUS les duos. Fraction capee a 1 (100 %).
- Symbiose (sym) : resonance fusionnelle propre aux JUMEAUX (lien forge des l'enfance). Fraction capee a 1 ; nulle pour les non-jumeaux.

Loi : P_combo = (P1 + P2) x (1 + 0.10 * syn + 0.16 * sym)   [P en %, syn/sym en fraction]

- Bond nul (syn = sym = 0) : P_combo = P1 + P2 (pure somme, aucune resonance).
- Apogee jumeaux (syn = sym = 1) : +26 % sur la somme. Apogee non-jumeaux (syn = 1, sym = 0) : +10 %. Le plafond du systeme (+26 %) est cale sur l'apogee Naoya+Nisha = 24 doigts.
- La somme brute domine : c'est le tonnage qui pese le plus, le bond n'est que l'amplificateur.
- Regle de pouce : un duo de jumeaux l'emporte sur un duo non-jumeau des que sa somme atteint ~87 % de celle de l'adversaire (1.10 / 1.26).
- syn et sym ne sont PAS figes : ils dependent de la relation AU MOMENT du combat, fixes au cas par cas (matchup, enjeu, issue) -> a determiner en roadmap pour chaque duo. Actes :
  - Mei Mei + Ui Ui = syn 100 % (foi aveugle ; Ui Ui faible, mais le bond plein leve Mei Mei de +10 %).
  - Nisha + Geto (epoque quatuor, 2006-2007) = syn 85 % (confiance totale au combat malgre la tension morale ; la synergie mesure la coordination, pas l'accord ideologique ; sym 0, non-jumeaux).

Reperes d'apogee :
| Duo | Type | Sommes (%) | P_combo | Doigts |
|---|---|---|---|---|
| Satoru + Nisha | non-jumeaux (syn 100) | 139.07 + 78.15 | 238.95 % | ~28.9 |
| Maki + Mai (curseur 0/100) | jumelles (syn+sym 100) | 78.15 + 68.44 | 184.70 % | ~25.9 |
| Naoya + Nisha (adulte) | jumeaux (syn+sym 100) | 43.94 + 78.15 | 153.84 % | 24.0 |

Ces combos peuvent franchir le Sukuna brut (> 20 doigts / 100 %) : valeurs theoriques assumees (cf. Table).

Exemple date (2c1 "Deux contre le dieu", Roadmap A2_7, 2007) : Nisha (16 = 59.51 %) + Geto (15 = 51.35 %), syn 85 % -> (110.86) x 1.085 = 120.28 % (~21.6 doigts) < Satoru seul (23 = 139.07 %). Le dieu l'emporte meme a 2 contre 1 ; l'Infini scelle l'ecart. Illustre "la somme brute domine" : aucun bond de synergie ne comble l'abime de Gojo.

## Partage gemellaire (Maki / Mai)
Le pool gemellaire des jumelles d'Ogi se repartit le long d'un curseur a somme constante (les parts des deux totalisent 100 %). Chaque repartition fixe la puissance des deux :

| Repartition | Maki (plafond) | Mai (plafond) |
|---|---|---|
| Maki 50 / Mai 50 | 6 | 1 |
| Maki 40 / Mai 60 | 8 | 8 |
| Maki 25 / Mai 75 | 12 | 12 |
| Maki 0 / Mai 100 | 18 | 17 |

- Pour Maki (Restriction Celeste physique), MOINS d'energie occulte = PLUS de puissance : a 0 % elle atteint le corps de monstre, voie Toji (18). A l'etat de base (50/50) elle est bridee a 6, et plafonnee Grade 4 par blocage politique du clan.
- Pour Mai (sort de Construction), c'est l'inverse : plus d'energie occulte = plus de puissance ; a 100 % elle culmine a 17. A l'etat de base, Mai = 1 doigt (Semi-Grade 2).
- Distinction : le curseur fixe les puissances INDIVIDUELLES ; quand les jumelles combattent EN DUO, c'est la loi synergie/symbiose ci-dessus qui combine ces individuels (symbiose, car jumelles). Apogee duo : cf. Reperes d'apogee.
- [DIVERGENCE RP] Plafond vs exploite. La table ci-dessus donne le PLAFOND fixe par la repartition ; l'EXPLOITE est ce qui sort reellement au combat.
  - Maki (Restriction physique) : exploite = plafond, toujours - c'est du corps, il n'y a pas de sort a maitriser. Tout glissement de curseur se traduit immediatement en puissance.
  - Mai (sort de Construction) : exploite = plafond x maitrise. Tant qu'elle construit mal son sort, elle reste SOUS son plafond. Le curseur lui donne le reservoir ; la maitrise le convertit.
- Trajectoire ere B (Maki / Mai) :
  | Jalon | Repartition | Maki (= exploite) | Mai plafond | Mai exploite |
  |---|---|---|---|---|
  | 2008 (debut B1) | 50/50 | 6 | 1 | 1 |
  | 2011 (pivot B1) | 40/60 | 8 | 8 | 3 |
  | 2015 (B3, lecon Yorozu) | 40/60 | 8 | 8 | 8 |
  | avr 2017 (B3_3, entrée de Maki à Tokyo) | 30/70 | ~11 | ~11 | ~11 |
  | 1 nov 2018 (D1, coup d'État Zenin) | 10/90 | 16 | 15 | 15 |
  Lecture : le curseur glisse en 2011 (50/50 -> 40/60), puis en avril 2017 (40/60 -> 30/70, valeurs interpolées : chacune assume enfin sa voie, le corps pour Maki, la Construction pour Mai). En 2015, c'est la MAITRISE de Mai qui rattrape son plafond (3 -> 8, apres avoir vu Yorozu manier la Construction), pas le curseur. Égalité structurelle jusqu'à 30/70 : les jumelles se valent, d'où leurs égalités aux Amicales 2017 et 2018. Au-delà, Maki prend un doigt d'avance (16 contre 15 à 10/90, 18 contre 17 à l'apogée).
- Mecanique du curseur (declencheurs des bascules, enjeux narratifs) -> roadmap.

## Plafond mondial
Gojo post-Toji (23 doigts / 139 %) n'est depasse, en 1 contre 1, que par trois etres, dans des conditions particulieres :
- Sukuna dans Megumi a 20 doigts sur 20 (receptacle parfait) : 27 sur l'echelle, symbiose parasitique [DIVERGENCE RP] (cf. reperes). Meme classe theorique : Eien dans Nisha, si elle l'avait emporte. Kenjaku dans Suguru (22) reste SOUS ce plafond.
- Yuta dans le corps de Satoru adulte.
- Yuji adulte.
Note : Megumi l'EGALE en 2022 (23, Mahoraga dompte), sans le depasser [DIVERGENCE RP] (cf. reperes).
Note : en DUO, des combinaisons depassent 23 (Maki+Mai, Satoru+Nisha a apogee ; cf. Synergie et symbiose) - mais le plafond mondial vise le 1 contre 1.

## Notes de certitude
- Loi synergie/symbiose : [DIVERGENCE RP], calee sur les apogees fournis par le worldbuilder. Split synergie +10 % / symbiose +16 % ; le total +26 % est impose par l'apogee Naoya+Nisha = 24 doigts. syn/sym par duo fixes au cas par cas en roadmap (actes : Mei Mei+Ui Ui 100 % ; Nisha+Geto 85 % en 2006-2007).
- Partage gemellaire Maki/Mai : [DIVERGENCE RP], table fournie par le worldbuilder ; mecanique du curseur -> roadmap.
- Repères chiffrés et courbes : notes de certitude sur Power_Scaling/Doigts_de_Sukuna_reperes.md.

---

FIN_WIKI_POWER_SCALING_DOIGTS_DE_SUKUNA
