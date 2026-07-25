# Corpus - table des locuteurs, etablie par auto-identification

- version : W1
- nature : SOURCE DERIVEE. Table identifiant / personnage, construite UNIQUEMENT a partir des
  repliques ou le locuteur se nomme lui-meme. Aucune inference, aucun souvenir de jeu.
- usage : lever l'anonymat des citations de dialogue. Jamais fetche en narration.

## Pourquoi cette table

Le dump indexe les dialogues par identifiant de locuteur sans fournir de table vers les noms.
Les pages du wiki citaient donc des repliques anonymes, et plusieurs ont conclu a tort qu'un
bloc etait 'sans locuteur identifiable'. C'etait faux : de nombreux blocs contiennent leur
propre auto-identification, sous la forme 'I am X' ou 'My name is X'.

## Limite a respecter absolument

Cette table dit qu'un bloc CONTIENT une auto-identification, PAS que toutes ses repliques sont
du meme locuteur. Un bloc regroupe plusieurs sections, qui peuvent porter des voix distinctes.
Exemple avere : le bloc 0205 porte en section 80 'I am Melina' et en sections 40, 41 et 60 une
voix qui s'adresse a un 'young seedling' et parle de son propre reve d'Ordre - ce n'est
manifestement pas la meme locutrice.

Regle d'usage : une attribution est ETABLIE si la replique citee est dans la MEME SECTION que
l'auto-identification. Sinon elle est [IMPLICITE] et doit etre balisee, ou confirmee par une
source hors-texte (cinematique) sous balise [HORS-JEU].

## Table (53 auto-identifications)

| Bloc | Personnage | Replique probante | Sections |
|---|---|---|---|
| 0202 | Malenia | [20260500] I am Malenia. | 12 |
| 0205 | Melina | [20580200] I am Melina. | 5 |
| 1001 | Melina | [100120050] I am Melina, and I have an accord with this person. | 29 |
| 2039 | Malenia | [203900010] I am Malenia. Blade of Miquella. | 5 |
| Finger Reader Enia [1020] | Enia | [102001010] You've done well. I am Enia, the Finger Reader. | 16 |
| 2168 | Ranni's | [216808020] Fine. I am Ranni's shadow and it's for her that I fight. | 14 |
| 2208 | Iron Fist | [220803010] I am Iron Fist Alexander! | 6 |
| Alexander, Warrior Jar [2200] | Alexander | [220002010] I am Alexander, also known as the Iron Fist. And as you can see, I'm stuck her | 50 |
| Asimi, Silver Tear [2180] | Asimi | [218002010] I am Asimi. My true form is that of a silver tear. | 17 |
| Old Albus [2190] | Albus | [219002040] I am Albus. An Albinauric, as you can see. | 4 |
| War Counselor Iji [2240] | Iji | [224010010] I am Iji. A blacksmith who once served the Carian royals... | 29 |
| 2241 | Iji | [224100030] Again, I am Iji. | 8 |
| 3030 | Guilbert | [303002020] I am Guilbert. A Redeemer of vengeance. In all its forms. | 11 |
| 3072 | Pidia | [307200030] I am Pidia. Servant to the Carian royal family. | 7 |
| Latenna the Albinauric [2280] | Latenna | [228010040] Let's try again. I'm Latenna. An Albinauric, the same as Old Albus. | 16 |
| Preceptor Seluvis [3070] | Seluvis | [307001020] I am Seluvis, preceptor in the sorcerous arts. | 37 |
| Tanith, Volcano Manor Proprietress [3000] | Tanith | [300001010] I am Tanith, the proprietress of this house. | 35 |
| 3128 | Jerren | [312804020] I am Jerren, bringer of your death. Do not forget. | 6 |
| Edgar the Revenger [3110] | Edgar | [311001010] I'm Edgar, warden of this castle as ordained by Lord Godrick himself. | 8 |
| Irina of Morne [3100] | Irina | [310001020] My name is Irina. I've escaped from Castle Morne, to the south. | 31 |
| Irina of Morne [3100] | Hyetta | [310010010] My name is Hyetta, and I'm journeying in search of the distant light. | 31 |
| Patches [3090] | Patches | [309007010] I'm Patches. Patches the Untethered. | 30 |
| Rya the Scout [3130] | Rya | [313010030] I am Rya, in the service of Lady Tanith of the Volcano Manor. | 41 |
| Sorceress Sellen [3160] | Sellen | [316001010] I am Sellen, a sorcerer, quite plainly. | 33 |
| Witch-Hunter Jerren [3120] | Jerren | [312001040] I am Jerren. Foolish old warrior, and witness. | 25 |
| 3218 | Kenneth Haight | [321802010] I am Kenneth Haight, and I have seen quite enough! | 5 |
| Fia, Deathbed Companion [3220] | Fia | [322001010] I am Fia. | 26 |
| Roderika, Spirit Tuner [3200] | Roderika | [320030010] My name is Roderika. I should have told you sooner. | 32 |
| Shabriri [3180] | Yura | [318010020] I am Yura. Hunter of Bloody Fingers. | 33 |
| Miriel, Pastor of Vows [3300] | Miriel | [330001020] I am Miriel, steward of this sacred chamber. | 19 |
| Nepheli Loux, Warrior [3340] | Nepheli Loux | [334002030] I am Nepheli Loux. Tarnished and warrior, like you. | 24 |
| Sir Gideon Ofnir, the All-Knowing [3240] | Gideon Ofnir | [324020020] I am known as Gideon Ofnir. | 49 |
| Sorcerer Rogier [3250] | Tarnished | [325002030] I'm Tarnished, like you. | 31 |
| Sorcerer Thops [3330] | Thops | [333002020] My name is Thops. | 18 |
| Merchant Kale [8000] | Kale | [800001040] I am Kale. Purveyor of fine goods. | 37 |
| Millicent [3480] | Millicent | [348021040] My name is Millicent. I pray fate permits us meet again. | 28 |
| Sage Gowry [3490] | Gowry | [349001010] I am Gowry. A great sage, in my day, anyway. | 30 |
| Scribe Corhyn [3510] | Corhyn | [351001010] Welcome to the Roundtable Hold. I'm Corhyn, a man of the cloth. | 39 |
| 0210 | Radahn | [21040000] I am Radahn. | 7 |
| 10903 | Jolan | [1090300050] I am Jolan. The Night is yours now to wield. | 6 |
| 10904 | Jolan | [1090450030] I am Jolan. Loyal to Count Ymir. | 2 |
| 11601 | Ansbach | [1160100010] I am Ansbach. Formerly in service to Lord Mohg. | 1 |
| 11606 | Ansbach | [1160650010] I am Ansbach. Formerly in service to Lord Mohg. | 4 |
| 11633 | Ansbach | [1163300000] I am Ansbach of the Pureblood Knights. | 1 |
| 11701 | Freyja | [1170100020] I am Freyja. I once fought alongside General Radahn. | 4 |
| 11702 | Freyja | [1170210020] I am Freyja. I once fought alongside General Radahn. | 2 |
| 11704 | Freyja | [1170410020] I am Freyja. I once fought alongside General Radahn. | 4 |
| 11801 | Leda | [1180100010] I am Leda. And like you, I was guided by faith along his honourable path. | 1 |
| 11803 | Leda | [1180350010] I am Leda. I missed my chance to speak with you last time, | 5 |
| 11804 | Leda | [1180420010] I am Leda. I missed my chance to speak with you last time, | 6 |
| 11901 | Thiollier | [1190100040] My name is Thiollier. | 1 |
| 11904 | Thiollier | [1190450040] My name is Thiollier. | 4 |
| 12001 | Ymir | [1200100010] I am Ymir. Welcome, to Manus Metyr. | 1 |

## Cas remarquables

- Bloc `Shabriri [3180]` : le bloc porte le nom de Shabriri, mais la replique [318010020] dit
  "I am Yura. Hunter of Bloody Fingers." Deux identites dans un meme bloc de dialogue.
- Bloc `0205` : contient l'auto-identification de Melina ET la promesse [20500300]
  "Destined Death." adressee au Lord of Frenzied Flame.
- Bloc `2168` : le locuteur se dit "Ranni's shadow", sans donner de nom propre.
- Bloc `Irina of Morne [3100]` : contient DEUX auto-identifications distinctes, Irina et Hyetta.

---

FIN_WIKI__CORPUS_TABLE_LOCUTEURS
