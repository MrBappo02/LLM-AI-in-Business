---
type: concept
confidence: 0.75
last_confirmed: 2026-10-12
source_count: 3
---

# AI data protection

Controlling which company, customer and personal data goes into AI tools, and where it ends up. For an SME this mostly means choosing the right type of tool (free, business plan or local) and setting a rule for what may be uploaded.

## What the sources say

- Anything typed into a cloud AI tool goes to the provider's servers. Free versions are the main risk: the Dutch data protection authority warns that data entered there may be stored and used for training, and it reports more chatbot-related breach reports in 2025 than in 2024. [[2026-09-24-aibs-handbook-trust-ai-safety]]
- Business plans with a signed data processing agreement do not train on customer data by default (per the vendors' own privacy pages). Microsoft Copilot keeps EU prompts in the EU. [[2026-09-24-aibs-handbook-trust-ai-safety]]
- A local open model (LM Studio, Ollama) on one capable PC keeps all data in-house, but it is weaker and needs upkeep. [[2026-09-24-aibs-handbook-trust-ai-safety]] An open-weight model on your own PC is also the low-dependency option. [[2026-10-12-aibs-handbook-geopolitics]]
- 52% of firms worry about data fed into AI (relayed from OECD, 2025b). Limit who may upload confidential files, and ask an adviser whether booked hours count as personal data under the GDPR. [[2026-10-05-aibs-handbook-themes-1-2]]
- Under the GDPR: keep personal data out of prompts, list each AI tool in the processing register, and report leaks to the authority within 72 hours. [[2026-09-24-aibs-handbook-trust-ai-safety]]
- Classify files as public, internal or confidential, and decide what never goes into closed cloud AI. Never upload NDA designs unchecked; use a local model for NDA projects. [[2026-10-12-aibs-handbook-geopolitics]]

Confidence note: all three sources are chapters of the same course handbook. The business-plan claims rest on vendor documentation. 0.75 is the ceiling.

## Related

- [[shadow-ai]]
- [[ai-vendor-dependency]]
- [[human-oversight-of-ai]]
