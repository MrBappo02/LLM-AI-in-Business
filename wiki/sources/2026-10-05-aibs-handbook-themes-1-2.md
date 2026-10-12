---
type: source
kind: other
title: "Theme 1 — What don't we know yet about AI, and what should we find out first? / Theme 2 — What do firms like ours use AI for, and what pays off?"
author: ["Unnamed team (placeholder [Team name])"]
publisher: "AIBS handbook (course handbook draft)"
url: "none — local PDF, raw/reports/handbook-aibs-themes-1-2-v2.pdf"
date_published: 2026-10-05
date_ingested: 2026-10-12
added_by: "Nasjaat"
raw: "../../raw/reports/handbook-aibs-themes-1-2-v2.md"
length: "3 pages (read in full): Theme 1, Theme 2, shared reference list"
---

# AIBS handbook — Themes 1 and 2: the AI gap to close first, and what pays off

## TL;DR

- Two handbook chapters for a fictional 40-person Dutch firm that designs and builds machines (SOLIDWORKS, PDM, ERP, spreadsheets, own recorded machine hours).
- Theme 1: owners say they lack experience and legal clarity. The chapter argues the gap that matters most is unasked: whether the firm's own data is good enough to test one AI use. Without a baseline, payback can't be judged.
- Theme 2: only office assistants have measured gains, and they are small. The chapter picks **AI cost estimation for quotes** as the first test, because it runs on the very data Theme 1 doubts.
- The method is CRISP-DM with a pass level set in advance (error no worse than the human quote, less time per quote, payback within one year). AI drafts and a named estimator decides.
- Five first steps per theme: name one decision and its payback limit, measure a baseline on 20–30 jobs, check the data links, appoint an owner and a back-up, and trial one quoting platform.

## Key claims

All figures are relayed from the chapter's cited sources. None was checked against those sources.

**Theme 1 (page 1)**
- AI use at Dutch firms with 10–50 people rose to 27% in 2025, mostly for marketing and admin (citing CBS, 2025). Owners use Copilot or ChatGPT for quotes and keep a human in charge (citing Midpoint Brabant, 2025; van der Meer, 2025). (The translation)
- Lack of experience is the top barrier at 73% (CBS, 2025). 83% of SME manufacturers in Brabant do not know where AI fits in production (FME, 2026). (The translation)
- Said versus needed: firms ask for more experience, but they need a way to judge output, because AI fails where users do not expect it (Dell'Acqua et al., 2023). They ask for legal clarity, but the AI literacy duty already applies from February 2025 (EU AI Act Art. 4), which makes the law a reason to act, not to wait. Usable data is never named, yet it is often not in order (Vankan et al., 2025), and poor data makes models worse (OECD, 2025a). Surveys do not ask about data (Eurostat, 2025). (table)
- The gap that matters most is not knowing whether the firm's own data is good enough to test one AI use. Without a baseline, a payback rule such as one year at most cannot be applied. (The gap that matters most now)
- Tooling: an Excel export from ERP/PDM with Copilot or ChatGPT for formulas (a few days), plus a short in-house AI literacy session (a few hours). (Recommended tooling)
- Responsible AI: 52% of firms worry about data fed into AI (OECD, 2025b), so limit who may upload confidential files. Ask an adviser whether booked hours are personal data under the GDPR. An expert accepts or rejects every AI suggestion. Name an owner and a back-up, because a tool fell into disuse when its builder left (van Ginkel, 2025). (Responsible AI & trust)
- First five steps: one decision and goal with a payback limit; a baseline of quoted vs actual hours on 20–30 recent jobs; check whether hours link to parts in ERP/PDM; an owner and a back-up, and training for AI users; ask ERP and SOLIDWORKS suppliers what AI is coming. (First five steps)

**Theme 2 (page 2)**
- Payoff evidence by use. Chat assistant: 2.8% of work hours saved on average (Humlum & Vestergaard, 2025). Cost estimation: about 23.5% error with little data (Manuguerra et al., 2023), about 10% with 13,684 drawings (Arıkan et al., 2025). AI-made SOLIDWORKS drawings: no figures, and the output needs cleanup (Keglovits, 2025). Models on own data: expected, not yet reached (van der Meer, 2025). (The translation)
- Only office assistants have measured gains, and they are small. Cost estimation was chosen because testing it also tests the data gap. Start with in-house parts, not whole machines. (The translation)
- CRISP-DM walk-through. Data use is weak at 80% of firms (FME, 2026). Commercial platforms give a market average, not your costs (Jacobs, 2025). AI can be wrong on unusual parts (Dell'Acqua et al., 2023). Without an owner the tool falls into disuse. (use-case table)
- Pass level set in advance: error no worse than the human quote, less time per quote, payback within one year. (Pass level)
- Tooling by effort: Excel baseline (days), a quoting platform trial such as The Quotation Factory (weeks), an own model built with a knowledge centre (months). (Recommended tooling)
- Accuracy figures come only from other firms' parts, so the firm's own phase-5 test is the real check. Check client contracts before uploading their drawings. A named person approves every quote. Benefits rise 10–40% when employers encourage use (Humlum & Vestergaard, 2025). (Responsible AI & trust)

## Quotes

> The law is a reason to act, not to wait
> Experience alone does not show where AI fails
> Only office assistants have measured gains, and they are small
> AI drafts; the estimator decides

## Caveats

- **Student handbook draft, not primary evidence.** Theme 1 is v0.6 and Theme 2 is v0.4. The author is an unfilled placeholder ([Team name], [Cohort]). Every figure is relayed from a cited source that is not in this wiki.
- **Translated sources.** Most Dutch sources are quoted in the team's own English translation (stated on page 3).
- **Fictional persona.** The firm is invented, so the use case is illustrative, not a case study.
- **Date.** `date_published` is the Sources last appraised date (5 Oct 2026), not a publication date.
- **Small and uneven evidence base.** The cost-estimation error figures come from two studies on other firms' parts (axisymmetric components; 2D drawings). The 2.8% figure comes from one Danish labour-market study.
- **Same course as the other handbook chapters** ([[2026-09-24-aibs-handbook-trust-ai-safety]], [[2026-10-12-aibs-handbook-geopolitics]]), so they are not independent confirmation of one another.
- No protected material, and no text addressed to an AI.

## Links

- [[ai-data-readiness]]
- [[ai-pilot-evaluation]]
- [[ai-assisted-quoting]]
- [[ai-data-protection]]
- [[human-oversight-of-ai]]
- [[human-ai-handoff-costs]]
- [[ai-literacy-obligation]]
- [[sme-ai-adoption-barriers]]

Cited but without pages: CBS, FME, Midpoint Brabant, Eurostat, OECD, Dell'Acqua et al., Humlum & Vestergaard, Manuguerra et al., Arıkan et al., Jacobs (Sirris), Keglovits (Hawk Ridge Systems), Linssen et al. (Fraunhofer Innovation Platform, University of Twente), Vankan et al. (Dialogic), van der Meer (Metaal Magazine), van Ginkel (Link Magazine), Brouwers (IO+, on The Quotation Factory). The chapter uses CRISP-DM as its template.
