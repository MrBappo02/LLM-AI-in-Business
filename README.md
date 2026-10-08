# LLM Wiki — a template for your team's knowledge

An empty wiki that your AI assistant fills and maintains. You collect sources: articles,
videos, reports. The assistant reads each one once and writes it into linked pages: one page
per source, one per organisation that matters, one per idea. When you ask a question, it
answers from those pages and shows which page every claim came from.

Made for the course [AI in Business](https://datadrivendecisions.github.io/ai-in-business/)
(HAN, minor Data Driven Decision Making in Business). It follows the
[LLM Wiki pattern](llm-wiki.md) described by Andrej Karpathy.

## Why a wiki and not a chat with your files

When you upload files to a chat, the assistant looks up passages when you ask, and forgets them
afterwards. Ask again tomorrow and it starts from scratch. A wiki does the reading in advance
and keeps the result:

- **It builds up.** The tenth source is read against the nine before it. Where it disagrees,
  that is written down on the page, not discovered by accident three weeks later.
- **You can check it.** Every page is a plain text file. Every claim links to its source page,
  and every source page points to the original file in `raw/`.
- **It remembers what it did.** `wiki/log.md` records every source added and every question
  asked, with the pages that were read to answer it.

## What is in here

```
AGENTS.md        The rules your assistant follows. Read it; change it when you disagree.
llm-wiki.md      Karpathy's original description of the pattern.
raw/             Your sources, as markdown. Added by you, never edited afterwards.
wiki/            The pages the assistant writes.
  index.md       Every page, one line each.
  log.md         Everything that happened, newest first.
tools/
  fetch_article.py   A web page → the article, word for word, in raw/articles/
  fetch_youtube.py   A YouTube link → a transcript file in raw/videos/
  lint.py            The health check: broken links, missing fields, quotes not in the source
```

## Start (about ten minutes)

You need **git**, **Python 3.9 or later**, and an **AI assistant that can edit files in a
folder**: Claude Code, Cursor, GitHub Copilot in agent mode, Codex, Gemini CLI or Antigravity.
They all read `AGENTS.md`.

1. **Make your own copy.** On GitHub, press **Use this template → Create a new repository**.
   One repository per team. Private is fine; add your teammates as collaborators.
2. **Clone it** and open the folder in your assistant.
3. **Install the two helpers** (once per laptop):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate          # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Check it works:** `python3 tools/lint.py` should say *0 error(s)*. (On Windows the
   command is `python`, not `python3`, here and below.)

## Use

Talk to your assistant in plain language. In Claude Code the slash commands `/ingest`,
`/query` and `/lint` do the same.

**Add an article**

> Ingest https://example.org/some-article — added by Sam

The assistant runs `tools/fetch_article.py`, which saves the article word for word in
`raw/articles/`.

**Add a YouTube video**

> Ingest https://www.youtube.com/watch?v=… — added by Sam

The assistant runs `tools/fetch_youtube.py`, which saves the transcript in `raw/videos/`.
The video itself is not downloaded.

**Add a PDF report**

Save the PDF in `raw/reports/`, then:

> Ingest raw/reports/the-report.pdf — added by Sam

The assistant converts it with `markitdown` and keeps the PDF beside the text.

Each time, the assistant first tells you what it read and which pages it plans to write, and
waits for your go-ahead. That pause is yours: it is where you catch a wrong reading before it
spreads over ten pages.

**Ask a question**

> Which AI uses pay off first for a small manufacturer, according to the wiki?

The answer cites a wiki page after every claim, and says so when the wiki has no source on part
of the question. Ask it to file a good answer, and it becomes a page in `wiki/syntheses/`.

**Check the wiki**

> Lint the wiki.

Run this after every few sources. It reports; it does not fix.

## Reading it

Every page is markdown, so GitHub shows it well enough. For the full experience, open the
folder as a vault in [Obsidian](https://obsidian.md) (free): links become clickable, every page
shows what links to it, and the graph view shows the shape of what you know.

## Three rules worth knowing before you start

1. **No interview material, ever.** Recordings, transcripts, notes, names from your field
   research: none of it goes in this repository, private or not. Whatever the assistant reads is
   sent to a model service. Your knowledge architecture says where that material lives instead.
2. **A source is data, not an instruction.** If a web page contains text aimed at an AI, the
   assistant records it and does not obey it.
3. **Quotes are real.** `tools/lint.py` checks that every quotation on a wiki page appears word
   for word in the raw file. A model can invent a quotation; this is how you catch it.

## Make it yours

`AGENTS.md` is a starting point, not a law. Add a page type your research needs, change the
confidence rules, add a folder for a new kind of source. Change it the way you change your
other platform documents: write down what you changed and why, in `wiki/log.md` as a `schema`
entry and in your team's decision log.

## Limits

- Up to a few hundred pages, the index is enough for the assistant to find things. Beyond that
  you want a search tool; [`llm-wiki.md`](llm-wiki.md) names one.
- The assistant can misread a source. The pause before writing, the quote check and the log are
  there so a person can catch it, but a person has to look.
- Automatic YouTube captions mishear names and numbers. Check a figure against the video before
  it goes on your handbook page.
