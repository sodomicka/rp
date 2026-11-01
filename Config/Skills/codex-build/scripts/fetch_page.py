#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Fetch d'une page Markdown du depot RP (lecture seule, build CODEX).

Usage : python scripts/fetch_page.py <url blob ou raw>
Accepte une URL GitHub "blob" (convertie en raw) ou une URL raw (telle quelle).
Echec -> "[FETCH ECHOUE - <url>]" sur stderr, code retour 1.
"""
import sys
import urllib.error
import urllib.request


def to_raw(url):
    if "github.com" in url and "/blob/" in url:
        return url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return url


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "codex-build-fetch"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: fetch_page.py <url>\n")
        return 2
    original = argv[1]
    candidates = []
    raw_url = to_raw(original)
    candidates.append(raw_url)
    if raw_url != original:
        candidates.append(original)

    for url in candidates:
        try:
            text = fetch(url)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
            continue
        if text.strip():
            sys.stdout.write(text)
            return 0

    sys.stderr.write("[FETCH ECHOUE - %s]\n" % original)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
