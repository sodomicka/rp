# INSTRUCTION WIKI - ACCES GITHUB (S8)

Fichier `Config/` de l'instruction de projet "INSTRUCTION - WIKI BUILD + SETUP + CODEX V1" (le coeur) : meme autorite, meme numerotation. Renvois : S1 a S7, MODE GUIDE et ORDRE DE CONSTRUCTION -> le coeur, toujours charge ; S8 et modes detailles -> leur fichier (liste au coeur S0). Se lit EN ENTIER.

### 8. ACCES GITHUB
`wiki_base` (SB0 de la BIBLE_LORE) = racine du WIKI, forme blob ; `raw_base` = la meme racine en forme raw, **utilisee pour tous les fetchs**. Idem `parties_base` / `parties_raw_base`. URL d'une page = base + dossier + fichier. Regle : on fetche en raw, on cite en blob. Le Sommaire (`wiki_base + Sommaire.md`, lien en SB9) est la carte de navigation.

**Methode 1 - LIRE UNE PAGE (defaut) : raw, markdown brut, sans parsing.**
```bash
curl -sL "{raw_base}{dossier}/{fichier}.md"
```
`{raw_base}` se LIT dans BIBLE SB0 (champs `raw_base` / `parties_raw_base`) - stocke, pas derive a la volee. BIBLE ancienne sans ces champs : deriver de `{base}` (`github.com` -> `raw.githubusercontent.com`, `/blob/<branche>/` -> `/<branche>/`, branche `main`) et **ajouter les champs au prochain BIBLE BUILD**.

**Methode 2 - LISTER UN DOSSIER (defaut) : clone sans blobs.**
```bash
git clone --filter=blob:none --depth 1 https://github.com/sodomicka/rp.git /tmp/rp
ls /tmp/rp/Config
find /tmp/rp/{Univers} -type f -name '*.md' | sort
```
Arborescence seule, sans contenu de fichier : le depot ENTIER en une fois. A faire une seule fois par thread, puis reutiliser le clone. Usages : relever le numero de version des SPEC dans `Config/`, lister `Roadmap/<Prota>/` (non indexe au Sommaire), lister `Parties/<Partie>/Memoires/`, verifier qu'une page existe avant de la fetcher.

**Methode 3 - LISTER UN DOSSIER (secours)** : si le clone est indisponible dans l'environnement courant.
```bash
curl -sL "https://github.com/sodomicka/rp/tree/main/{path}" \
  | grep -oP '(?<="){path}/[^"]+\.md' | sort -u
```
Certains environnements renvoient 403 sur `github.com` tout en laissant passer `raw.githubusercontent.com` : dans ce cas cette methode est morte et le clone est le seul chemin. En dernier recours, sonder directement les URL raw candidates (une URL qui repond 200 existe, 404 non) et le dire au worldbuilder.

**Methode 4 - LIRE UNE PAGE (secours ultime)** : page blob + extraction Python, si raw est vide ou inaccessible. `rawLines` est une cle interne non contractuelle du rendu GitHub : elle peut disparaitre sans preavis, et l'echec est SILENCIEUX (parser vide, pas d'erreur).
```bash
curl -sL "{base}{dossier}/{fichier}.md" | python3 -c "
import sys, json
html = sys.stdin.read()
for seg in html.split('\"rawLines\":')[1:]:
    start = seg.index('['); result, depth = '', 0
    for c in seg[start:]:
        result += c
        if c == '[': depth += 1
        if c == ']': depth -= 1
        if depth == 0: break
    try:
        for line in json.loads(result): print(line)
    except: pass
"
```
Echec reel de toutes les methodes : signaler selon S5. Si c'est l'environnement qui bloque et non le depot, le DIRE : le worldbuilder doit savoir que le MJ est aveugle sur une partie du depot.

FIN_INSTRUCTION_WIKI_GITHUB
