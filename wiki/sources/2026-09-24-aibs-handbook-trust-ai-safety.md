---
type: source
kind: other
title: "Can I trust AI with my data, its answers and my people?"
author: ["Team 5"]
publisher: "AIBS handbook (course handbook draft)"
url: "none — local PDF, raw/reports/handbook-trust-ai-safety-v2.pdf"
date_published: 2026-09-24
date_ingested: 2026-10-12
added_by: "Nasjaat"
raw: "../../raw/reports/handbook-trust-ai-safety-v2.md"
length: "2 pages (read in full), including references"
---

# AIBS handbook — Can I trust AI with my data, its answers and my people?

## TL;DR

- A handbook chapter by Team 5 (v0.2) for a fictional family-owned 30-person Dutch CNC shop. Its most valuable data is customer drawings (often under NDA), price calculations and staff records.
- **Data:** free chatbots are the main risk. Business plans with a signed data processing agreement don't train on your data by default, and a local open model (LM Studio, Ollama) keeps everything in-house.
- **Answers:** an autonomy ladder (advise → draft for approval → act within fixed limits) where every new use starts at the bottom. Avoid excessive agency.
- **People:** hidden AI use is already common (78% of AI users bring their own tools), and bans alone fail. Offer one approved tool and a rule, and train staff (a legal duty since 2 Feb 2025).
- Use case: AI fills a field list from RFQs, the costing sheet still sets the price, and the estimator approves every draft. It is tested on 50 past RFQs against a pass level set first.

## Key claims

Figures are relayed from the chapter's cited sources.

**1. My data (The translation)**
- Anything typed into a cloud AI tool goes to the provider's servers. The Dutch data protection authority (AP) warns that data entered in free versions may be stored and used for training, and it received more chatbot-related breach reports in 2025 than in 2024 (citing Accountant.nl, 2025).
- Business plans come with a contract and by default don't train on your data (citing OpenAI, Microsoft, Anthropic, Mistral AI). Copilot keeps EU prompts in the EU. Always sign the data processing agreement.
- LM Studio or Ollama can run an open model on one PC with 16 GB memory and a graphics card (citing SitePoint, 2026). Nothing leaves the building, but the models are weaker and need upkeep.

**2. Its answers (The translation)**
- Every new use starts at the bottom of a ladder: advise (a person decides) → draft for approval (a named person checks and sends) → act within fixed limits (only low-risk, reversible tasks).
- Avoid excessive agency: give AI only the tools and rights the task needs, and let a person approve high-impact actions (citing OWASP Gen AI Security Project, 2025). Never leave decisions that seriously affect a person to AI alone (citing GDPR, Art. 22).

**3. My people (The translation)**
- 78% of AI users bring their own tools to work (citing Microsoft & LinkedIn, 2024). Bans alone fail because employers can't watch everyone (citing Accountant.nl, 2025).
- Offer one approved tool, a clear rule on what may go in, and block free chatbots. Staff AI training has been a legal duty since 2 Feb 2025 (citing EU AI Act Art. 4).

**Use case (CRISP-DM table)**
- Business: the estimator loses mornings reading RFQs. The goal is less reading, with prices staying with the estimator.
- Data, honestly assessed: past quotes are spread over Excel and ERP with inconsistent material names, some drawings are scans, and many fall under NDA.
- Preparation: 50 past RFQs, with unneeded personal data removed and one fixed field list (material, dimensions, tolerances, quantity, delivery date).
- Modelling: no custom model. A business-tier assistant fills the fields, and the existing costing sheet sets the price.
- Evaluation: compare the AI's fields with the estimator's on the 50 RFQs, count errors per field (watch tolerances), and set the pass level first.
- Deployment: draft for approval only. The estimator checks every draft, and 10 random drafts are rechecked each month.

**Tooling and responsible AI**
- Tools in order of effort: a business-plan chat assistant (low), Microsoft 365 Copilot (low–medium; check file access first), Power Automate or Zapier with an AI step (medium), a local model (medium–high). (Recommended tooling)
- Reliability: trust the tool only as far as the 50-RFQ test shows, since AI can confidently misread a tolerance. Every output is a draft. (Responsible AI & trust)
- GDPR: keep personal data out of prompts, list each AI tool in the processing register, and report leaks to the AP within 72 hours. (Responsible AI & trust)
- AI takes over the reading, not the judgement. Let staff say which AI they use without blame. (Responsible AI & trust)
- First five steps: ask the team which tools they use (no blame), choose one business-tier tool and sign its DPA, write a one-page AI rule, run a one-hour AI literacy session and keep a record of it, and test the quote use case on 50 past RFQs. (First five steps)

## Quotes

> AI takes over the reading, not the judgement
> Nothing leaves the building, but the models are weaker and need upkeep
> Bans alone fail, because employers can't watch everyone

## Caveats

- **Student handbook draft (v0.2), not primary evidence.** Every claim is relayed from a cited source that is not in this wiki. Vendor privacy pages (OpenAI, Microsoft, Anthropic, Mistral AI) are the evidence for the business-plan claims, so those claims are as the vendors describe their own products.
- **Fictional persona** (stated as not a real firm).
- **Date.** `date_published` is the last appraised date in the header (24 Sept 2026; the header reads ast appraised, a typo).
- **Reference mismatch.** The OWASP reference is titled LLM06:2025 Excessive Agency, but its URL points to `llm06-sensitive-information-disclosure`.
- The CBS (2025) reference is listed but not cited in the text.
- **Same course as the other handbook chapters** ([[2026-10-05-aibs-handbook-themes-1-2]], [[2026-10-12-aibs-handbook-geopolitics]]), so they are not independent of one another.
- No protected material, and no text addressed to an AI.

## Links

- [[ai-data-protection]]
- [[human-oversight-of-ai]]
- [[human-ai-handoff-costs]]
- [[shadow-ai]]
- [[ai-literacy-obligation]]
- [[ai-assisted-quoting]]
- [[ai-pilot-evaluation]]
- [[ai-data-readiness]]
- [[ai-vendor-dependency]]

Cited but without pages: Accountant.nl / Autoriteit Persoonsgegevens (AP), OpenAI, Microsoft, Anthropic, Mistral AI, Microsoft & LinkedIn Work Trend Index, OWASP Gen AI Security Project, SitePoint, GDPR (Art. 22, 30, 33, 35). The chapter uses CRISP-DM as its template.
