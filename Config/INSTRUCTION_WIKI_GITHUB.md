# INSTRUCTION WIKI - ACCÈS GITHUB (§8)

Fichier `Config/` qui prolonge le cœur `Config/INSTRUCTION_WIKI_COEUR.md` ("INSTRUCTION - WIKI BUILD + SETUP + CODEX V1") : même autorité, même numérotation. Renvois : §1 à §7, MODE GUIDE et ORDRE DE CONSTRUCTION -> le cœur, lu en premier ; §8 et modes détaillés -> leur fichier (liste au cœur §0). Se lit EN ENTIER.

### 8. ACCÈS GITHUB
`wiki_base` (SB0 de la BIBLE_LORE) = racine du WIKI, forme blob ; `raw_base` = la même racine en forme raw, **utilisée pour tous les fetchs**. Idem `parties_base` / `parties_raw_base`. URL d'une page = base + dossier + fichier. Règle : on fetche en raw, on cite en blob. Le Sommaire (`wiki_base + Sommaire.md`, lien en SB9) est la carte de navigation.

**Méthode 1 - LIRE UNE PAGE (défaut) : raw, markdown brut, sans parsing.**
```bash
curl -sL "{raw_base}{dossier}/{fichier}.md"
```
`{raw_base}` se LIT dans BIBLE SB0 (champs `raw_base` / `parties_raw_base`) - stocké, pas dérivé à la volée. BIBLE ancienne sans ces champs : dériver de `{base}` (`github.com` -> `raw.githubusercontent.com`, `/blob/<branche>/` -> `/<branche>/`, branche `main`) et **ajouter les champs au prochain BIBLE BUILD**.

**Méthode 2 - LISTER UN DOSSIER (défaut) : clone sans blobs.**
```bash
git clone --filter=blob:none --depth 1 https://github.com/sodomicka/rp.git /tmp/rp
ls /tmp/rp/Config
find /tmp/rp/{Univers} -type f -name '*.md' | sort
```
Arborescence seule, sans contenu de fichier : le dépôt ENTIER en une fois. À faire une seule fois par thread, puis réutiliser le clone. Usages : relever le numéro de version des SPEC dans `Config/`, lister `Roadmap/<Prota>/` (non indexé au Sommaire), lister `Parties/<Partie>/Memoires/`, vérifier qu'une page existe avant de la fetcher.

**Méthode 3 - LISTER UN DOSSIER (secours)** : si le clone est indisponible dans l'environnement courant.
```bash
curl -sL "https://github.com/sodomicka/rp/tree/main/{path}" \
  | grep -oP '(?<="){path}/[^"]+\.md' | sort -u
```
Certains environnements renvoient 403 sur `github.com` tout en laissant passer `raw.githubusercontent.com` : dans ce cas cette méthode est morte et le clone est le seul chemin. En dernier recours, sonder directement les URL raw candidates (une URL qui répond 200 existe, 404 non) et le dire au worldbuilder.

**Méthode 4 - LIRE UNE PAGE (secours ultime)** : page blob + extraction Python, si raw est vide ou inaccessible. `rawLines` est une clé interne non contractuelle du rendu GitHub : elle peut disparaître sans préavis, et l'échec est SILENCIEUX (parser vide, pas d'erreur).
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
Échec réel de toutes les méthodes : signaler selon §5. Si c'est l'environnement qui bloque et non le dépôt, le DIRE : le worldbuilder doit savoir que le MJ est aveugle sur une partie du dépôt.

### 8bis. Écriture sur le dépôt
1. Le MJ écrit lui-même sur le dépôt ; le worldbuilder n'uploade rien à la main.
2. Rien ne s'écrit sans avoir été montré et approuvé (§1).
3. Tout passe par une branche et une pull request, une par thread, jamais de push direct sur main.
4. Un nouveau thread ne lit que main : une PR non fusionnée n'existe pas pour lui.
5. Échec d'écriture : [ECRITURE ECHOUEE - <fichier>], signalé au worldbuilder, jamais contourné.
6. Fusion : le MJ fusionne lui-même la PR sur main en fin de thread, une fois tout validé.

FIN_INSTRUCTION_WIKI_GITHUB
