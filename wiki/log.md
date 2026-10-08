# Log

Every operation on this wiki, **newest first**. New entries go directly under the line below.
The format is fixed so that `grep "^## \[" wiki/log.md | head` lists the most recent ten:

    ## [YYYY-MM-DD] operation | title

Operations: `ingest`, `query`, `lint`, `synthesis`, `schema`, `fix`. A `query` entry lists the pages
that were read, so a wrong answer can be traced to what it was built on.

---

## [2026-10-08] ingest | MIT Sloan — How AI is reshaping workflows and redefining jobs

- Added by: Nasjaat
- New: [[2026-04-22-how-ai-is-reshaping-workflows-and-redefining-jobs]], [[mit-sloan]], [[task-chaining]], [[human-ai-handoff-costs]], [[ai-workflow-redesign]]
- Updated: none (first ingest)
- Debates: none
- Notes: raw file frontmatter has empty `author` and `date_published`; taken from the byline on the source page instead, raw left unedited. Secondary source; the underlying paper (Demirer et al., *Chaining Tasks, Redefining Work*) is a candidate for the next ingest. No AI-directed text found.
- Lint: clean (0 errors, 0 warnings)
