#!/usr/bin/env python3
"""Health check for the wiki. Reports; never edits.

    python3 tools/lint.py            # errors and warnings
    python3 tools/lint.py --quiet    # errors only

Exit 0 when there are no errors, 1 when there are. Warnings never fail the run.
Standard library only, Python 3.9 or later.

Errors (must be fixed):
  frontmatter    a page without frontmatter, or without the fields its type needs
  confidence     confidence missing, not a number, or outside 0.0-0.95
  broken-link    a [[wikilink]] to a page that does not exist
  not-in-index   a page that wiki/index.md does not list
  raw-missing    a source page whose raw: file does not exist
  quote          a quotation that does not appear word for word in the raw sources
  raw-changed    a committed file in raw/ that has been edited or deleted

Warnings (worth a look):
  orphan         a page no other page links to
  source-count   source_count differs from the number of source pages linking in
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
CATALOGUES = {"index", "log"}

REQUIRED = {
    "source": ["kind", "title", "url", "date_published", "date_ingested", "added_by", "raw", "length"],
    "entity": ["kind", "confidence", "last_confirmed", "source_count"],
    "concept": ["confidence", "last_confirmed", "source_count"],
    "synthesis": ["question", "date", "source_count"],
}
FOLDER = {"source": "sources", "entity": "entities", "concept": "concepts", "synthesis": "syntheses"}

LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
QUOTE = re.compile(r"[\"“]([^\"“”\n]{20,}?)[\"”]")
MIN_QUOTE_WORDS = 5


def parse(path):
    """Return (frontmatter dict, body). Top-level scalar keys only; enough for this schema."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    meta = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*(?:#.*)?$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip("\"'")
    return meta, text[end + 4:]


def normalise(text):
    text = text.lower().replace("’", "'").replace("‘", "'")
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def strip_code(body):
    return re.sub(r"```.*?```|`[^`\n]*`", "", body, flags=re.S)


def quotations(body):
    """Verbatim claims on a page: text in quotation marks, and blockquote lines under ## Quotes."""
    body = strip_code(body)
    found = [m.group(1) for m in QUOTE.finditer(body)]
    in_quotes = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_quotes = line.strip().lower() == "## quotes"
        elif in_quotes and line.startswith(">"):
            found.append(re.sub(r"\s+—\s+.*$|\(\s*[\d:]+\s*\)\s*$", "", line.lstrip("> ").strip()))
    # An ellipsis or an [editorial insertion] splits a quote into parts that must each be found.
    parts = []
    for q in found:
        for part in re.split(r"\.\.\.|…|\[[^\]]*\]", q):
            if len(normalise(part).split()) >= MIN_QUOTE_WORDS:
                parts.append(part.strip())
    return parts


def raw_changes():
    try:
        out = subprocess.run(["git", "status", "--porcelain", "--", "raw"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return []
    return [line[3:] for line in out.splitlines() if line[:2].strip() in {"M", "D", "MM", "AM", "R"} and not line.startswith("??")]


def main():
    quiet = "--quiet" in sys.argv
    errors, warnings = [], []
    pages = {p.stem: p for p in WIKI.rglob("*.md")}
    meta, bodies = {}, {}
    for slug, path in pages.items():
        meta[slug], bodies[slug] = parse(path)

    raw_text = {}
    for path in RAW.rglob("*.md"):
        raw_text[path.resolve()] = normalise(path.read_text(encoding="utf-8", errors="ignore"))
    all_raw = " ".join(raw_text.values())

    index_links = set(LINK.findall(bodies.get("index", "")))
    inbound = {slug: set() for slug in pages}

    for slug, path in sorted(pages.items()):
        rel = path.relative_to(ROOT)
        body = bodies[slug]
        for target in LINK.findall(strip_code(body)):
            target = target.strip().split("/")[-1]
            if target not in pages:
                errors.append(f"broken-link   {rel}: [[{target}]] does not exist")
            elif target != slug and slug not in CATALOGUES:
                inbound[target].add(slug)
        if slug in CATALOGUES:
            continue

        fm = meta[slug]
        if fm is None:
            errors.append(f"frontmatter   {rel}: no frontmatter block")
            continue
        kind = fm.get("type", "")
        if kind not in REQUIRED:
            errors.append(f"frontmatter   {rel}: type is '{kind}', expected one of {', '.join(REQUIRED)}")
            continue
        if path.parent.name != FOLDER[kind]:
            errors.append(f"frontmatter   {rel}: type {kind} belongs in wiki/{FOLDER[kind]}/")
        for field in REQUIRED[kind]:
            if not fm.get(field) or fm.get(field) in {"[]", "''"}:
                errors.append(f"frontmatter   {rel}: '{field}' is missing or empty")
        if kind in {"entity", "concept"} and fm.get("confidence"):
            try:
                c = float(fm["confidence"])
                if not 0.0 < c <= 0.95:
                    errors.append(f"confidence    {rel}: {c} is outside 0.0-0.95")
            except ValueError:
                errors.append(f"confidence    {rel}: '{fm['confidence']}' is not a number")
        if slug not in index_links:
            errors.append(f"not-in-index  {rel}: add it to wiki/index.md")

        raw_file = None
        if kind == "source" and fm.get("raw"):
            raw_file = (path.parent / fm["raw"]).resolve()
            if not raw_file.exists():
                errors.append(f"raw-missing   {rel}: raw: {fm['raw']} does not exist")
                raw_file = None
        haystack = raw_text.get(raw_file, "") if raw_file else all_raw
        for q in quotations(body):
            if normalise(q) not in haystack:
                where = fm["raw"] if raw_file else "any file in raw/"
                errors.append(f"quote         {rel}: not found in {where}: \"{q[:70]}{'…' if len(q) > 70 else ''}\"")

    for slug, path in sorted(pages.items()):
        if slug in CATALOGUES or meta[slug] is None:
            continue
        rel = path.relative_to(ROOT)
        if not inbound[slug]:
            warnings.append(f"orphan        {rel}: no other page links here")
        kind = meta[slug].get("type")
        if kind in {"entity", "concept"} and meta[slug].get("source_count", "").isdigit():
            actual = sum(1 for s in inbound[slug] if (meta.get(s) or {}).get("type") == "source")
            stated = int(meta[slug]["source_count"])
            if actual != stated:
                warnings.append(f"source-count  {rel}: says {stated}, {actual} source page(s) link here")

    for f in raw_changes():
        errors.append(f"raw-changed   {f}: raw files are never edited; restore it with git checkout -- {f}")

    counts = {k: sum(1 for m in meta.values() if m and m.get("type") == k) for k in REQUIRED}
    plural = {"source": "sources", "entity": "entities", "concept": "concepts", "synthesis": "syntheses"}
    summary = ", ".join(f"{n} {k if n == 1 else plural[k]}" for k, n in counts.items())
    for line in errors:
        print("ERROR  " + line)
    if not quiet:
        for line in warnings:
            print("warn   " + line)
    print(f"\n{summary}. {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
