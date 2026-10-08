#!/usr/bin/env python3
"""Save a web article, word for word, into raw/articles/<slug>.md.

    python3 tools/fetch_article.py https://example.org/some-article
    python3 tools/fetch_article.py URL -o raw/articles/my-name.md

Needs markitdown (pip install -r requirements.txt). The text is saved as the page gives it,
not summarised, so a quotation on a wiki page can be checked against it. Menus above the
article's title are dropped; everything from the title down is kept.
"""
import argparse
import json
import re
import sys
import unicodedata
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; llm-wiki-template)"


class Meta(HTMLParser):
    """Collect <meta> tags and the <title>."""

    def __init__(self):
        super().__init__()
        self.meta, self.title, self._in_title = {}, "", False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta":
            key = (a.get("property") or a.get("name") or "").lower()
            if key and a.get("content") and key not in self.meta:
                self.meta[key] = a["content"].strip()
        elif tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def slugify(text, max_words=10):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words[:max_words]) or "article"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url")
    parser.add_argument("-o", "--output", help="output path (default: raw/articles/<slug>.md)")
    args = parser.parse_args()

    try:
        from markitdown import MarkItDown
    except ImportError:
        sys.exit("markitdown is not installed. Run: pip install -r requirements.txt")

    try:
        req = urllib.request.Request(args.url, headers={"User-Agent": UA})
        html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")
    except Exception as err:  # noqa: BLE001 - any network failure means the same thing here
        sys.exit(f"Could not fetch the page: {err}. Save it as markdown by hand instead (see AGENTS.md).")
    meta = Meta()
    meta.feed(html)
    m = meta.meta

    text = MarkItDown().convert(args.url).text_content
    title = m.get("og:title") or meta.title.strip() or args.url
    # Drop navigation above the article: keep from the first H1 onwards.
    h1 = re.search(r"^# .+$", text, flags=re.M)
    if h1:
        text = text[h1.start():]
        title = h1.group(0)[2:].strip()
    published = (m.get("article:published_time") or m.get("date") or m.get("dc.date") or "")[:10]
    author = m.get("author") or m.get("article:author") or ""

    out = Path(args.output) if args.output else ROOT / "raw" / "articles" / f"{slugify(title)}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        sys.exit(f"{out} already exists. Raw files are never overwritten by accident; remove it first if you mean to replace it.")

    front = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"url: {json.dumps(args.url)}",
        f"author: {json.dumps(author, ensure_ascii=False)}   # from the page's metadata; check it",
        f"site: {json.dumps(m.get('og:site_name', ''), ensure_ascii=False)}",
        f"date_published: {published}",
        f"retrieved: {date.today().isoformat()}",
        "---",
        "",
    ]
    out.write_text("\n".join(front) + text.strip() + "\n", encoding="utf-8")
    shown = out.relative_to(ROOT) if out.is_relative_to(ROOT) else out
    print(f"Wrote {shown}  ({len(text.split())} words). Check that the end of the article is there.")


if __name__ == "__main__":
    main()
