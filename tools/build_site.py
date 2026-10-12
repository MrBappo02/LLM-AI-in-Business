#!/usr/bin/env python3
"""Build a static website from the source pages in wiki/sources/.

    python3 tools/build_site.py      # writes site/index.html and site/sources/<slug>.html

Re-run after every ingest. The script wipes site/ and regenerates it; never edit site/ by hand.
Links between source pages are clickable; links to concept and entity pages show as plain labels.
Standard library only, Python 3.9 or later. No JavaScript, so the pages open straight from disk.
"""
import html
import re
import shutil
import sys
from pathlib import Path

from lint import LINK, parse

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SITE = ROOT / "site"

CSS = """
:root {
  --bg: #f7f6f2; --panel: #ffffff; --text: #1f2328; --muted: #5d636b; --border: #dedcd5;
  --accent: #1f5f8b; --accent-soft: #e3eef6; --tag: #efece4; --quote: #f1efe8;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #15171a; --panel: #1d2024; --text: #e6e6e3; --muted: #9aa0a6; --border: #33373d;
    --accent: #7fb6dd; --accent-soft: #22303b; --tag: #2a2d31; --quote: #23262a;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.6 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
a { color: var(--accent); }
header.top { position: sticky; top: 0; z-index: 1; display: flex; align-items: center; gap: 16px;
  padding: 10px 24px; background: var(--panel); border-bottom: 1px solid var(--border); }
header.top .brand { font-weight: 700; color: var(--text); text-decoration: none; margin-right: auto; }
.btn { display: inline-block; padding: 7px 14px; border: 1px solid var(--border); border-radius: 8px;
  background: var(--panel); color: var(--text); text-decoration: none; font-size: 14px; }
.btn:hover { border-color: var(--accent); color: var(--accent); }
.btn.primary { background: var(--accent); border-color: var(--accent); color: var(--panel); }
.layout { display: grid; grid-template-columns: 280px minmax(0, 1fr); gap: 32px;
  max-width: 1200px; margin: 0 auto; padding: 24px; }
nav.side h2 { font-size: 13px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted);
  margin: 0 0 10px; }
nav.side a { display: block; margin-bottom: 6px; padding: 8px 10px; border: 1px solid var(--border);
  border-radius: 8px; background: var(--panel); color: var(--text); text-decoration: none; font-size: 14px;
  line-height: 1.35; }
nav.side a small { display: block; color: var(--muted); font-size: 12px; }
nav.side a:hover { border-color: var(--accent); }
nav.side a.current { background: var(--accent-soft); border-color: var(--accent); }
main { min-width: 0; background: var(--panel); border: 1px solid var(--border); border-radius: 12px;
  padding: 28px 36px; }
main h1 { margin-top: 0; line-height: 1.25; }
main h2 { margin-top: 32px; padding-bottom: 4px; border-bottom: 1px solid var(--border); }
blockquote { margin: 12px 0; padding: 10px 16px; background: var(--quote);
  border-left: 4px solid var(--accent); border-radius: 4px; }
blockquote p { margin: 0; }
code { background: var(--tag); padding: 1px 5px; border-radius: 4px; font-size: 90%; }
.tag { background: var(--tag); padding: 1px 7px; border-radius: 10px; font-size: 90%; white-space: nowrap; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 14px; }
th, td { text-align: left; vertical-align: top; padding: 6px 10px; border-bottom: 1px solid var(--border); }
table.meta th { width: 130px; color: var(--muted); font-weight: 600; }
.pager { display: flex; justify-content: space-between; gap: 12px; margin-top: 40px;
  padding-top: 20px; border-top: 1px solid var(--border); }
.pager .btn { max-width: 48%; }
.stats { display: flex; gap: 12px; flex-wrap: wrap; margin: 20px 0; }
.stat { flex: 1 1 140px; padding: 14px 16px; border: 1px solid var(--border); border-radius: 10px; }
.stat b { display: block; font-size: 28px; line-height: 1.1; }
.stat span { color: var(--muted); font-size: 14px; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; }
.card { display: flex; flex-direction: column; padding: 16px; border: 1px solid var(--border);
  border-radius: 10px; color: var(--text); text-decoration: none; }
.card:hover { border-color: var(--accent); }
.card .kind { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--accent); }
.card h3 { margin: 4px 0 6px; font-size: 17px; line-height: 1.3; }
.card .meta { color: var(--muted); font-size: 13px; }
.card p { font-size: 14px; margin: 8px 0 12px; flex: 1; }
.card .btn { align-self: flex-start; }
@media (max-width: 800px) {
  .layout { grid-template-columns: 1fr; padding: 16px; gap: 16px; }
  nav.side { order: 2; }
  main { padding: 20px 18px; }
  header.top { padding: 10px 16px; }
}
"""


def clean(value):
    """A frontmatter value for display: ["A", "B"] becomes A, B."""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = ", ".join(v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip())
    return value


def inline(text, sources, prefix):
    """Escape a line of markdown and render its inline formatting."""
    codes = []

    def keep_code(m):
        codes.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)

    def wikilink(m):
        target = m.group(1).strip().split("/")[-1]
        label = m.group(0)[2:-2].split("|")[-1].strip() if "|" in m.group(0) else target
        if target in sources:
            return f'<a href="{prefix}sources/{target}.html">{html.escape(sources[target]["title"])}</a>'
        return f'<span class="tag">{label}</span>'

    text = LINK.sub(wikilink, text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def markdown(body, sources, prefix):
    """Render the markdown the wiki uses: headings, nested lists, quotes, tables, paragraphs."""
    out, para, depth = [], [], 0
    lines = body.strip("\n").splitlines()

    def flush():
        nonlocal depth
        if para:
            out.append(f"<p>{inline(' '.join(para), sources, prefix)}</p>")
            para.clear()
        while depth:
            out.append("</li></ul>")
            depth -= 1

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        item = re.match(r"^(\s*)[-*] (.*)$", line)
        if not stripped:
            if para:
                flush()
        elif re.match(r"^#{1,4} ", stripped):
            flush()
            level = len(stripped) - len(stripped.lstrip("#"))
            out.append(f"<h{level}>{inline(stripped[level:].strip(), sources, prefix)}</h{level}>")
        elif item:
            if para:
                out.append(f"<p>{inline(' '.join(para), sources, prefix)}</p>")
                para.clear()
            level = len(item.group(1).expandtabs(2)) // 2 + 1
            if level > depth:
                while depth < level:
                    out.append("<ul><li>")
                    depth += 1
            else:
                while depth > level:
                    out.append("</li></ul>")
                    depth -= 1
                out.append("</li><li>")
            out.append(inline(item.group(2), sources, prefix))
        elif depth and line.startswith("  "):
            out.append(" " + inline(stripped, sources, prefix))
        elif stripped.startswith(">"):
            # Each > line under ## Quotes is a separate quotation (see quotations() in lint.py).
            flush()
            quote = stripped[1:].strip()
            if quote:
                out.append(f"<blockquote><p>{inline(quote, sources, prefix)}</p></blockquote>")
        elif stripped.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head, *rest = rows
            out.append("<table><tr>" + "".join(f"<th>{inline(c, sources, prefix)}</th>" for c in head)
                       + "</tr>" + "".join("<tr>" + "".join(f"<td>{inline(c, sources, prefix)}</td>"
                                                            for c in r) + "</tr>" for r in rest) + "</table>")
            continue
        else:
            if depth:
                flush()
            para.append(stripped)
        i += 1
    flush()
    return "\n".join(out)


def page(title, content, sources, current=None, prefix=""):
    """Wrap content in the shared layout: top bar, source navigation, main column."""
    links = "\n".join(
        f'<a href="{prefix}sources/{slug}.html"{" class=\"current\"" if slug == current else ""}>'
        f'{html.escape(s["title"])}<small>{html.escape(s["kind"])} · {s["date_published"]}</small></a>'
        for slug, s in sources.items())
    home_class = "btn primary" if current is None else "btn"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
<header class="top">
  <a class="brand" href="{prefix}index.html">LLM Wiki — AI in Business</a>
  <a class="{home_class}" href="{prefix}index.html">Home</a>
</header>
<div class="layout">
<nav class="side">
<h2>Sources ({len(sources)})</h2>
{links}
</nav>
<main>
{content}
</main>
</div>
</body>
</html>
"""


def source_page(slug, s, sources, prev_slug, next_slug):
    url = s.get("url", "")
    url_html = f'<a href="{html.escape(url)}">{html.escape(url)}</a>' if url.startswith("http") \
        else html.escape(url)
    rows = [("Kind", html.escape(s["kind"])), ("Author", html.escape(clean(s.get("author", "")))),
            ("Publisher", html.escape(s.get("publisher", ""))), ("URL", url_html),
            ("Published", s["date_published"]), ("Ingested", s.get("date_ingested", "")),
            ("Added by", html.escape(s.get("added_by", ""))), ("Length", html.escape(s.get("length", "")))]
    meta = "<table class=\"meta\">" + "".join(
        f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows if v) + "</table>"
    body = re.sub(r"^\s*# .*\n", "", s["body"].lstrip("\n"), count=1)

    def button(target, label):
        if not target:
            return "<span></span>"
        return f'<a class="btn" href="{target}.html">{label}</a>'

    pager = (f'<div class="pager">{button(prev_slug, "← " + html.escape(sources[prev_slug]["title"]) if prev_slug else "")}'
             f'{button(next_slug, html.escape(sources[next_slug]["title"]) + " →" if next_slug else "")}</div>')
    content = f"<h1>{html.escape(s['title'])}</h1>\n{meta}\n{markdown(body, sources, '../')}\n{pager}"
    return page(s["title"], content, sources, current=slug, prefix="../")


def home_page(sources, counts):
    stats = "".join(f'<div class="stat"><b>{n}</b><span>{label}</span></div>' for label, n in counts)
    cards = []
    for slug, s in sources.items():
        tldr = re.search(r"## TL;DR\s*\n+\s*- (.+)", s["body"])
        summary = inline(tldr.group(1), {}, "") if tldr else ""
        summary = re.sub(r"<[^>]+>", "", summary)
        cards.append(f"""<a class="card" href="sources/{slug}.html">
<span class="kind">{html.escape(s['kind'])}</span>
<h3>{html.escape(s['title'])}</h3>
<span class="meta">{html.escape(s.get('publisher', ''))} · {s['date_published']}</span>
<p>{summary}</p>
<span class="btn">Read source page →</span>
</a>""")
    content = f"""<h1>LLM Wiki — AI in Business</h1>
<p>This wiki collects sources on <strong>how small and medium-sized firms can use AI</strong>, with a
focus on Dutch mechanical engineering and product design companies: AI assistants inside CAD and
automation software, generative design, AI-assisted quoting, data readiness, data protection,
human oversight, regulation and the geopolitics of who owns the AI a firm depends on.</p>
<p>It follows the LLM Wiki pattern: the team collects sources, and an AI assistant reads each one
once and compiles it into linked pages — one page per source, one per organisation that matters,
one per concept. Questions are answered from those pages rather than from the raw files.</p>
<p>This site shows the <strong>source pages</strong>. Each one says what a source <em>claims</em>,
not what is true: a TL;DR, the key claims with where they came from, verbatim quotes, and caveats
such as who paid for it or what was not read. Grey labels like <span class="tag">generative-design</span>
name the concept and entity pages in the wiki that the source feeds.</p>
<div class="stats">{stats}</div>
<h2>Sources, newest first</h2>
<div class="cards">
{chr(10).join(cards)}
</div>"""
    return page("LLM Wiki — AI in Business", content, sources)


def main():
    sources = {}
    for path in (WIKI / "sources").glob("*.md"):
        meta, body = parse(path)
        if not meta or meta.get("type") != "source":
            continue
        meta["body"] = body
        meta.setdefault("kind", "other")
        meta.setdefault("date_published", "")
        meta.setdefault("title", path.stem)
        sources[path.stem] = meta
    sources = dict(sorted(sources.items(), key=lambda kv: kv[1]["date_published"], reverse=True))

    def count(folder):
        return sum(1 for p in (WIKI / folder).glob("*.md"))

    counts = [("sources", len(sources)), ("concepts", count("concepts")),
              ("entities", count("entities")), ("syntheses", count("syntheses"))]

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "sources").mkdir(parents=True)
    (SITE / "style.css").write_text(CSS.lstrip(), encoding="utf-8")
    (SITE / "index.html").write_text(home_page(sources, counts), encoding="utf-8")
    slugs = list(sources)
    for n, slug in enumerate(slugs):
        prev_slug = slugs[n - 1] if n > 0 else None
        next_slug = slugs[n + 1] if n + 1 < len(slugs) else None
        (SITE / "sources" / f"{slug}.html").write_text(
            source_page(slug, sources[slug], sources, prev_slug, next_slug), encoding="utf-8")
    print(f"Built {len(slugs) + 1} pages in {SITE.relative_to(ROOT)}/ (home + {len(slugs)} sources).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
