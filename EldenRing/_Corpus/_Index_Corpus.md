# Index - Corpus

- version : W1
- branche : _Corpus/
- nature : SOURCE PRIMAIRE. Texte du jeu, nettoye ASCII, aucune redaction, aucune interpretation.
- etat : constitue pour ELDEN RING et SHADOW OF THE ERDTREE. Nightreign NON CONSTITUE.

## Origine des sources

- ELDEN RING : Carian Archive (AsteriskAmpersand), dump engUS.
  https://github.com/AsteriskAmpersand/Carian-Archive
- SHADOW OF THE ERDTREE : Impalers Archive (ividyon), dump engUS.
  https://github.com/ividyon/Impalers-Archive
- Complements .fmg.xml (noms de lieux, noms de PNJ, textes d'evenement) tires des memes depots.

## Regles d'usage

- JAMAIS fetche en narration. Document de build et de verification uniquement.
- Toute citation du wiki doit etre retrouvable ici. Un fait introuvable dans le corpus et non
  couvert par une source d'appoint validee est un trou a signaler, jamais a combler.
- Plafond de decoupage : 70 000 caracteres par fichier.

## Volumetrie

- 37 fichiers, 1501123 caracteres.
- ELDEN RING base : 2590 entrees d'items et dialogues, 436 lieux nommes, 254 PNJ nommes.
- SHADOW OF THE ERDTREE : 948 entrees d'items et dialogues.

## Trous connus du corpus

- `MovieSubtitle.fmg` est vide dans les deux dumps. Les cinematiques sont neanmoins presentes
  dans `TalkMsg` (verifie : le prologue figure en ER_Talk).
- `TalkMsg` indexe les dialogues par ID de locuteur, PAS par nom de PNJ. La table de
  correspondance ID -> PNJ n'est pas fournie par le dump. [INCERTAIN]
- Le corpus ne porte AUCUNE geographie : rien n'indique dans quelle region se trouve un lieu,
  ni ou se tient un PNJ. Source d'appoint necessaire (wikis communautaires, faits structurels
  uniquement, jamais d'interpretation).
- Aucun corpus ELDEN RING NIGHTREIGN a ce jour.

## Fichiers

- ER_Armor_01.md (W1) - ELDEN RING - Armures (1/2) | 260 entrees | 68938 car.
- ER_Armor_02.md (W1) - ELDEN RING - Armures (2/2) | 265 entrees | 61018 car.
- ER_Arts.md (W1) - ELDEN RING - Arts et competences | 181 entrees | 37547 car.
- ER_Events.md (W1) - ELDEN RING - Textes d'evenement | 678 (doublons et %null% retires) entrees | 28978 car.
- ER_Gems.md (W1) - ELDEN RING - Cendres de guerre (gems) | 99 entrees | 31609 car.
- ER_Goods_01.md (W1) - ELDEN RING - Objets, cles, notes, souvenirs (1/4) | 230 entrees | 69168 car.
- ER_Goods_02.md (W1) - ELDEN RING - Objets, cles, notes, souvenirs (2/4) | 228 entrees | 68959 car.
- ER_Goods_03.md (W1) - ELDEN RING - Objets, cles, notes, souvenirs (3/4) | 272 entrees | 68976 car.
- ER_Goods_04.md (W1) - ELDEN RING - Objets, cles, notes, souvenirs (4/4) | 159 entrees | 45938 car.
- ER_Loading.md (W1) - ELDEN RING - Ecrans de chargement | 66 entrees | 14407 car.
- ER_Npcs.md (W1) - ELDEN RING - Noms de PNJ et de boss | 254 (doublons et %null% retires) entrees | 8650 car.
- ER_Places.md (W1) - ELDEN RING - Noms de lieux | 436 (doublons et %null% retires) entrees | 13657 car.
- ER_Talismans.md (W1) - ELDEN RING - Talismans | 118 entrees | 35672 car.
- ER_Talk_01.md (W1) - ELDEN RING - Dialogues et cinematiques (1/8) | 38 entrees | 70285 car.
- ER_Talk_02.md (W1) - ELDEN RING - Dialogues et cinematiques (2/8) | 30 entrees | 68188 car.
- ER_Talk_03.md (W1) - ELDEN RING - Dialogues et cinematiques (3/8) | 28 entrees | 70156 car.
- ER_Talk_04.md (W1) - ELDEN RING - Dialogues et cinematiques (4/8) | 21 entrees | 66020 car.
- ER_Talk_05.md (W1) - ELDEN RING - Dialogues et cinematiques (5/8) | 21 entrees | 59579 car.
- ER_Talk_06.md (W1) - ELDEN RING - Dialogues et cinematiques (6/8) | 26 entrees | 66108 car.
- ER_Talk_07.md (W1) - ELDEN RING - Dialogues et cinematiques (7/8) | 40 entrees | 69633 car.
- ER_Talk_08.md (W1) - ELDEN RING - Dialogues et cinematiques (8/8) | 12 entrees | 28730 car.
- ER_Tutorial.md (W1) - ELDEN RING - Tutoriels | 32 entrees | 9513 car.
- ER_Weapons_01.md (W1) - ELDEN RING - Armes (1/2) | 281 entrees | 68755 car.
- ER_Weapons_02.md (W1) - ELDEN RING - Armes (2/2) | 182 entrees | 39138 car.
- SOTE_Armor.md (W1) - SHADOW OF THE ERDTREE - Armures | 145 entrees | 39452 car.
- SOTE_Arts.md (W1) - SHADOW OF THE ERDTREE - Arts et competences | 79 entrees | 18895 car.
- SOTE_Events.md (W1) - SHADOW OF THE ERDTREE - Textes d'evenement | 167 (doublons et %null% retires) entrees | 8523 car.
- SOTE_Gems.md (W1) - SHADOW OF THE ERDTREE - Cendres de guerre | 25 entrees | 9442 car.
- SOTE_Goods_01.md (W1) - SHADOW OF THE ERDTREE - Objets, cles, notes (1/2) | 224 entrees | 69159 car.
- SOTE_Goods_02.md (W1) - SHADOW OF THE ERDTREE - Objets, cles, notes (2/2) | 80 entrees | 26178 car.
- SOTE_Loading.md (W1) - SHADOW OF THE ERDTREE - Ecrans de chargement | 5 entrees | 1490 car.
- SOTE_Npcs.md (W1) - SHADOW OF THE ERDTREE - Noms de PNJ | 65 (doublons et %null% retires) entrees | 2427 car.
- SOTE_Places.md (W1) - SHADOW OF THE ERDTREE - Noms de lieux | 313 (doublons et %null% retires) entrees | 10202 car.
- SOTE_Talismans.md (W1) - SHADOW OF THE ERDTREE - Talismans | 40 entrees | 13557 car.
- SOTE_Talk_01.md (W1) - SHADOW OF THE ERDTREE - Dialogues (1/2) | 179 entrees | 68459 car.
- SOTE_Talk_02.md (W1) - SHADOW OF THE ERDTREE - Dialogues (2/2) | 62 entrees | 34721 car.
- SOTE_Weapons.md (W1) - SHADOW OF THE ERDTREE - Armes | 107 entrees | 28996 car.

---

FIN_WIKI__CORPUS_INDEX
