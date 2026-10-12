---
type: concept
confidence: 0.7
last_confirmed: 2026-10-12
source_count: 1
---

# AI assistants in CAD

Conversational AI built into CAD software. The user describes a task in natural language and the assistant carries it out inside the design tool, for example writing automation code, selecting geometry or converting files. It assists the designer's existing workflow, unlike [[generative-design]], where the software generates the geometry itself.

## What the sources say

- Interface: one chat that infers what the user wants and calls the right capability, rather than a menu of separate prompt-triggered skills. Several capabilities can be chained in one conversation. [[2026-07-28-solidworks-ai-fd03]]
- Automation without coding: the assistant writes a VBA macro from a plain-language description (e.g. automating file exports or custom properties), which the user runs or refines through chat. It is pitched as making design automation accessible to non-programmers. [[2026-07-28-solidworks-ai-fd03]]
- Repetitive interaction: a selection assistant picks many items across sketches and drawings by description. The vendor claims fewer mistakes and time saved, with no figures. [[2026-07-28-solidworks-ai-fd03]]
- Model performance: the assistant finds heavy geometry (such as modelled threads) across a large assembly, simplifies it in one step, and generates lightweight representations to reduce lag. [[2026-07-28-solidworks-ai-fd03]]
- Legacy and imported geometry: converting B-Rep files (e.g. STEP) into editable parametric parts is called one of the most requested AI-in-CAD use cases, useful for reverse engineering and iterating on existing designs. [[2026-07-28-solidworks-ai-fd03]]

## Caveat on the evidence

The only source so far is a 2026 vendor video (SOLIDWORKS) announcing features. It gives no accuracy figures, time savings or user experience. Confidence stays at 0.7 and cannot rise above 0.75 until an independent source (a user firm's account, a test or a study) reports how these assistants perform.

## Related

- [[solidworks]]
- [[engineering-copilots]] (the same pattern in automation engineering software)
- [[generative-design]]
- [[autodesk]]
