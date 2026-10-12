---
type: source
kind: video
title: "SOLIDWORKS AI Just Got Better - Here's What's New in FD03"
author: ["SOLIDWORKS"]
publisher: "SOLIDWORKS (YouTube)"
url: "https://www.youtube.com/watch?v=-REu7THDEzI"
date_published: 2026-07-28
date_ingested: 2026-10-12
added_by: "Nasjaat"
raw: "../../raw/videos/solidworks-ai-just-got-better-here-s-what-s-new.md"
length: "4:02, 597 words (full human-made transcript read)"
---

# SOLIDWORKS AI Just Got Better - Here's What's New in FD03

## TL;DR

- A SOLIDWORKS product video presenting the AI features in release **R2026x FD03** of its CAD software. It is billed as the first in a series of AI-focused updates.
- The AI moves from a list of separate prompt-invoked "skills" to **one conversational interface** that infers intent, picks the skill, and can chain several skills in one conversation. A prompt library lists what is available.
- **Natural-language macro creation**: describe a task and the AI writes a VBA macro, which can be run or refined through chat.
- A **selection assistant** for selecting many items by description, plus **large-assembly** help: simplifying heavy geometry (e.g. modelled threads) across an assembly and generating lightweight representations (SpeedPaks).
- **B-Rep to parametric conversion**: imported geometry such as STEP files turned into editable parametric parts, for reverse engineering and iterating on existing CAD.

## Key claims

- Designers and engineers want to know how AI can actually improve CAD workflows, so SOLIDWORKS plans a steady stream of AI updates over the next several releases. This is the first. [0:01]
- AI was first introduced as individual skills invoked with specific prompts. FD03 replaces them with a unified interface: a natural conversation in which the AI understands intent and activates the right skill. Several skills can be used in one conversation to move through a complex workflow without changing menus. A new prompt library acts as a roadmap of AI capabilities. [0:01–1:01]
- Macro creation no longer needs coding expertise. Describing a task in natural language makes the integrated AI generate a VBA macro and open it in the editor, e.g. to automate file exports or custom properties. The code can be run immediately or refined through chat. [1:01]
- A selection assistant lets users isolate parts across sketches and drawings with natural language instead of clicking dozens of items. The video claims this reduces mistakes and saves time. [1:01–2:01]
- Large assemblies: users can now act on an earlier performance-analysis feature. The AI identifies high-triangle-count culprits such as modelled threads and simplifies them across the whole assembly in one step. AI-guided SpeedPak generation creates lightweight representations of top-level or sub-assemblies to reduce lag, without opening and inspecting each component. [2:01]
- One of the most requested AI-in-CAD use cases, converting B-Rep geometry (e.g. STEP files) into fully editable parametric parts, is now supported. It is pitched for reverse engineering and for iterating on existing CAD. [3:01]

## Quotes

> generates a VBA macro and opens it directly in your editor
> use multiple skills in a single conversation to
> transform B-Rep geometry like step files into fully editable parametric parts

## Caveats

- **Vendor marketing.** SOLIDWORKS presents its own release on its own channel, and the description links to purchase, quote and demo pages. No figures, no customer cases and no limitations are given. Accuracy of the generated macros, selections and conversions is not discussed. The claim of "reducing mistakes and saving time" is asserted, not measured.
- **Feature announcement, not evidence of use.** The video shows what the product is said to do, not whether firms use it or what it delivers. The video calls itself an "AI preview".
- **Short.** About four minutes. Read in full.
- The presenter is introduced only by the first name Noah and named once, so no entity page. The captions spell the release FDO3 once where the title says FD03.
- **Acquisition note.** `tools/fetch_youtube.py` failed twice with HTTP 429 because its `en.*` caption pattern also requests many auto-translated tracks. The raw file was produced with the tool's own code, restricted to the human `en` track, so the format is unchanged.
- No text addressed to an AI was found.

## Links

- [[solidworks]]
- [[ai-assistants-in-cad]]

Not linked on purpose: the claim about chaining skills in one conversation is a product feature, not evidence for the task-chaining concept.
