# Log

Every operation on this wiki, **newest first**. New entries go directly under the line below.
The format is fixed so that `grep "^## \[" wiki/log.md | head` lists the most recent ten:

    ## [YYYY-MM-DD] operation | title

Operations: `ingest`, `query`, `lint`, `synthesis`, `schema`, `fix`. A `query` entry lists the pages
that were read, so a wrong answer can be traced to what it was built on.

---

## [2026-10-12] ingest | Automation World — Siemens Demonstrates Generative AI Copilot to Automate Engineering Tasks

- Added by: Nasjaat
- New: [[2025-12-10-siemens-engineering-copilot-tia]], [[siemens]], [[engineering-copilots]]
- Updated: [[human-oversight-of-ai]] (source_count 3 → 4, confidence 0.75 unchanged), [[ai-vendor-dependency]] (source_count 2 → 3, confidence 0.75 unchanged), [[ai-assistants-in-cad]] (Related link to [[engineering-copilots]] only)
- Debates: none. Siemens' "acts, not suggests" claim sits above the handbook's autonomy ladder, but it is recorded as a vendor capability claim, not a debate, because the article does not argue about oversight.
- Notes: a short trade-press report of a vendor announcement, with a pilot-customer quote and no figures; treated as vendor material. The team chose a separate concept page over adding to [[ai-assistants-in-cad]], because TIA Portal is automation software, not CAD; the two pages are cross-linked. Raw frontmatter has an empty `author` and a garbled `date_published`; the date was taken from the byline (2025-12-10) and the raw file left unedited. F. Zimmermann and Christian Gaarz are named once and listed on the source page only. No AI-directed text found.
- Lint: clean (0 errors, 0 warnings) after removing quotation marks around two short raw-file strings that the quote check had paired as one quote

## [2026-10-12] ingest | SOLIDWORKS — AI Just Got Better: What's New in FD03 (video)

- Added by: Nasjaat
- New: [[2026-07-28-solidworks-ai-fd03]], [[solidworks]], [[ai-assistants-in-cad]]
- Updated: none
- Debates: none
- Notes: vendor product video (4:02, human captions), no figures; concept held at 0.7 pending an independent source. `tools/fetch_youtube.py` hit HTTP 429 (its `en.*` pattern pulls auto-translated tracks); raw produced with the tool's own code restricted to the `en` track. No AI-directed text.
- Lint: clean (0 errors, 0 warnings) after rewording two short quotes that the quote check had paired wrongly

## [2026-10-12] ingest | BBC News — AI is less regulated than milk, says Microsoft president

- Added by: Nasjaat
- New: [[2026-10-11-ai-is-less-regulated-than-milk]], [[microsoft]], [[ai-regulation]]
- Updated: none (no existing page overlaps substantially)
- Debates: none
- Notes: news report of one AI vendor executive's views (Brad Smith, Microsoft); recorded as an interested party. Raw frontmatter has empty `author` and `date_published`; taken from the byline and page metadata, raw left unedited. The raw file includes BBC related-story links and footer, which were not used. Brad Smith, the reporter, the UK AI Security Institute and the other AI firms are named once and listed on the source page only. No AI-directed text found. [[ai-regulation]] links under Related to [[geopolitics-of-ai]] (US race framing) and [[ai-literacy-obligation]] (EU AI Act); no claims added to those pages.
- Lint: clean (0 errors, 0 warnings)

## [2026-10-12] ingest | AIBS handbook — Who owns your AI (geopolitics and vendor models)

- Added by: Nasjaat
- New: [[2026-10-12-aibs-handbook-geopolitics]], [[genai4eu]], [[geopolitics-of-ai]], [[ai-vendor-dependency]]
- Updated: [[ai-data-protection]], [[human-oversight-of-ai]], [[ai-pilot-evaluation]], [[sme-ai-adoption-barriers]] (each source_count +1, confidence held at 0.75 cap: same-course material); [[human-ai-handoff-costs]] (see Debates below)
- Debates: on [[human-ai-handoff-costs]], human approval of every AI output vs cutting handoffs (MIT Sloan)
- Notes: first upload was a blank page; ingested from the re-uploaded copy. Chapter is undated, has no team/version; date_published = date received. Citation inconsistencies (China plan, GenAI4EU n.d. vs dated, untitled White House reference) recorded in Caveats. Raw: `raw/reports/Handbook_page_Geopolitics_v2.pdf` + markitdown `.md`. No AI-directed text.
- Lint: clean (0 errors, 0 warnings)

## [2026-10-12] ingest | AIBS handbook — Themes 1–2 (AI gap to close first; what pays off)

- Added by: Nasjaat
- New: [[2026-10-05-aibs-handbook-themes-1-2]], [[ai-data-readiness]], [[ai-pilot-evaluation]], [[ai-assisted-quoting]], [[ai-literacy-obligation]], [[sme-ai-adoption-barriers]]
- Updated: [[ai-data-protection]], [[human-oversight-of-ai]]; [[human-ai-handoff-costs]] (Debates)
- Debates: on [[human-ai-handoff-costs]] (see geopolitics entry)
- Notes: student draft (Theme 1 v0.6, Theme 2 v0.4), author placeholder [Team name]; date_published = sources-last-appraised date. All figures relayed from cited sources not in the wiki. Raw: `raw/reports/handbook-aibs-themes-1-2-v2.pdf` + `.md`. No AI-directed text.
- Lint: clean (0 errors, 0 warnings)

## [2026-10-12] ingest | AIBS handbook — Can I trust AI with my data, its answers and my people? (Team 5)

- Added by: Nasjaat
- New: [[2026-09-24-aibs-handbook-trust-ai-safety]], [[ai-data-protection]], [[human-oversight-of-ai]], [[shadow-ai]]
- Updated: [[ai-data-readiness]], [[ai-pilot-evaluation]], [[ai-assisted-quoting]], [[ai-literacy-obligation]], [[ai-vendor-dependency]]; [[human-ai-handoff-costs]] (confidence 0.7 → 0.6, source_count 1 → 4 across the three handbook ingests)
- Debates: added to [[human-ai-handoff-costs]]. The handbooks require a named human to approve every output; MIT Sloan argues for cutting checkpoints. The disagreement turns on stakes, reversibility, GDPR and stage of adoption.
- Notes: student draft v0.2; date_published = last-appraised date. OWASP reference title/URL mismatch recorded in Caveats. Business-plan privacy claims rest on vendor pages. Raw: `raw/reports/handbook-trust-ai-safety-v2.pdf` + `.md`. No AI-directed text. Confidence policy: the three handbook chapters come from one course and are not treated as independent, so pages they support stop at 0.75.
- Lint: clean (0 errors, 0 warnings)

## [2026-10-12] ingest | Autodesk News — What Generative Design really is, what it isn’t, and why it’s the future of manufacturing

- Added by: Nasjaat
- New: [[2018-04-16-what-generative-design-really-is]], [[autodesk]], [[generative-design]]
- Updated: none (no existing page overlaps substantially)
- Debates: none
- Notes: vendor material (Autodesk promoting its own product category), so confidence is capped at 0.75. Published 2018, before LLM-based GenAI. Republished from IndustryWeek. Raw frontmatter has empty `author` and `date_published`; taken from the byline, raw left unedited. Airbus, GE, MaRS and others are named once and listed on the source page only. No AI-directed text found. Earlier the same day, the McKinsey *State of AI 2025* fetch failed (connection reset/timeout); nothing was written, and that ingest waits for a hand-saved copy.
- Lint: clean (0 errors, 0 warnings)

## [2026-10-08] ingest | MIT Sloan — How AI is reshaping workflows and redefining jobs

- Added by: Nasjaat
- New: [[2026-04-22-how-ai-is-reshaping-workflows-and-redefining-jobs]], [[mit-sloan]], [[task-chaining]], [[human-ai-handoff-costs]], [[ai-workflow-redesign]]
- Updated: none (first ingest)
- Debates: none
- Notes: raw file frontmatter has empty `author` and `date_published`; taken from the byline on the source page instead, raw left unedited. Secondary source; the underlying paper (Demirer et al., *Chaining Tasks, Redefining Work*) is a candidate for the next ingest. No AI-directed text found.
- Lint: clean (0 errors, 0 warnings)
