---
type: source
kind: other
title: "Who owns your AI – and what happens to you if that changes?"
author: ["Unknown (no team named)"]
publisher: "AIBS handbook (course handbook draft)"
url: "none — local PDF, raw/reports/Handbook_page_Geopolitics_v2.pdf"
date_published: 2026-10-12
date_ingested: 2026-10-12
added_by: "Nasjaat"
raw: "../../raw/reports/Handbook_page_Geopolitics_v2.md"
length: "1 page (read in full), including references"
---

# AIBS handbook — Who owns your AI, and what happens to you if that changes?

## TL;DR

- A handbook chapter on geopolitics and vendor models, for Dutch mechanical engineering or product design firms with 20–75 staff (SolidWorks, Inventor, Siemens NX).
- The question it asks is not which AI is best but who controls the AI the firm starts to depend on, and what happens to its designs, costs and continuity if that changes.
- The US, China and the EU each want to own the AI stack (chips, computing, models, software), and each says so in official plans. Most AI tools an SME uses are likely US-owned, so US policy can change their price, availability or terms.
- All three blocs back open models. The chapter calls this the SME's main lever.
- Advice: list each tool's owner, home country and data location; classify files; check contracts for exit terms; define a plan B per tool; look for GenAI4EU pilots.

## Key claims

Claims about national strategies are relayed from the cited policy documents.

- **United States:** AI is framed as a race for global dominance. The US wants to export its full AI technology stack to allies, expects allies to follow US export controls, and may otherwise use secondary tariffs (citing The White House, 2025, *America's AI Action Plan*). (2. The translation)
- **China:** the 15th Five-Year Plan targets breakthroughs in integrated circuits, machine tools, basic and industrial software and AI chips, to build an independent, controllable hardware-software ecosystem. Its AI+ initiative applies AI across the industrial life cycle, including design. Chinese machine builders will therefore compete with AI-supported design on a separate technology stack. (2. The translation)
- **European Union:** open-source software is central to EU technological independence, to reduce lock-in to non-EU vendors (citing European Commission, 2026). GenAI4EU invests about €700 million in made-in-Europe generative AI for sectors including manufacturing and robotics, yet only 13.5% of EU companies use AI (citing European Commission, n.d.). (2. The translation)
- **The common thread:** all three blocs back open models. Even the US plan says open-weight models let businesses avoid dependence on a closed model provider and keep sensitive data in-house. (2. The translation)
- **Use case (fictional 40-person machine builder):** AI to speed up concept design. Classify CAD files as public, internal or confidential. Test a closed cloud tool against an open local model, and evaluate time saved, quality, where data goes, and what happens if the vendor changes price or terms. Deploy cloud AI for non-sensitive work and the local model for NDA projects. (3. Illustrative use case)
- **Tooling:** (a) closed cloud AI inside current software (low effort, highest dependency); (b) European GenAI4EU-backed solutions (low–medium effort, EU-based); (c) an open-weight model on your own PC (medium effort, one-off hardware, data stays in-house). (4. Recommended tooling)
- **Responsible AI:** know who owns each tool and where files go, and never upload NDA designs unchecked. Treat AI designs as proposals that a qualified engineer approves. Keep a manual fallback for every AI step, and train staff rather than replace their judgement. (5. Responsible AI & trust)
- **First five steps:** inventory tools (owner, home country, data location); classify files and decide what never goes into closed cloud AI; check contracts for data use, price changes and exit terms; a plan B per tool; GenAI4EU pilots. (6. First five steps)

## Quotes

> being dependent on a closed model provider — The White House (2025), as quoted in the chapter
> Keep a manual fallback for every AI step

## Caveats

- **Student handbook draft, not primary evidence.** No team, cohort, version or date appears on the page. `date_published` is the date the file was received (2026-10-12). The newest reference is dated 21 Aug 2026, so the chapter was written after that.
- **Policy documents as relayed.** The US and Chinese positions come from short quotes of official plans; the chapter does not analyse them. The Chinese plan is read in a translation (Euclera, hosted by WKO).
- **Citation inconsistencies:**
  - The text cites People's Republic of China, 2026, but the reference list gives Euclera, T. b. (n.d.).
  - GenAI4EU is cited as n.d. in the text but dated 21 Aug 2026 in the list.
  - The White House reference has no title.
  - The European Commission is listed as Commission, E.
- **Different populations.** The 13.5% figure covers all EU companies. It is not comparable with the Dutch 10–50-employee figure in [[2026-10-05-aibs-handbook-themes-1-2]].
- **Same course as the other handbook chapters** ([[2026-10-05-aibs-handbook-themes-1-2]], [[2026-09-24-aibs-handbook-trust-ai-safety]]).
- **An earlier upload of this file was blank.** This conversion is from the re-uploaded copy.
- No protected material, and no text addressed to an AI.

## Links

- [[geopolitics-of-ai]]
- [[ai-vendor-dependency]]
- [[genai4eu]]
- [[ai-data-protection]]
- [[human-oversight-of-ai]]
- [[human-ai-handoff-costs]]
- [[ai-pilot-evaluation]]
- [[sme-ai-adoption-barriers]]

Cited but without pages: The White House (*America's AI Action Plan*, 2025), European Commission (EU Open Source Strategy; GenAI4EU page), China's 15th Five-Year Plan (Euclera translation via WKO). The chapter uses CRISP-DM as its template.
