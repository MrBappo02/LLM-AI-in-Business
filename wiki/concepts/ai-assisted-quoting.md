---
type: concept
confidence: 0.75
last_confirmed: 2026-10-12
source_count: 2
---

# AI-assisted quoting

Using AI in the quotation process of a manufacturing SME, either to estimate production cost from drawings and history or to extract the specification from customer requests for quotes (RFQs). In both forms the price decision stays with a human estimator.

## What the sources say

- Reported cost-estimation error is about 23.5% with little data and about 10% with 13,684 drawings (relayed from Manuguerra et al., 2023 and Arıkan et al., 2025). [[2026-10-05-aibs-handbook-themes-1-2]]
- Cost estimation needs drawings, material, batch size and actual hours. Commercial platforms give a market average, not your own costs, and AI can be wrong on unusual parts. [[2026-10-05-aibs-handbook-themes-1-2]]
- It is a good first AI test because it runs on the very data whose quality is in doubt, so testing it also tests the data gap. Start with in-house parts, not whole machines. [[2026-10-05-aibs-handbook-themes-1-2]]
- Tooling by effort: an Excel baseline (days), a quoting-platform trial such as The Quotation Factory (weeks), an own model with a knowledge centre (months). [[2026-10-05-aibs-handbook-themes-1-2]]
- RFQ drafting variant: a business-tier assistant fills a fixed field list (material, dimensions, tolerances, quantity, delivery date), and the existing costing sheet still sets the price. The goal is less reading for the estimator. [[2026-09-24-aibs-handbook-trust-ai-safety]]
- AI can confidently misread a tolerance, so every output is a draft that the estimator approves. Ten random drafts are rechecked each month. [[2026-09-24-aibs-handbook-trust-ai-safety]]
- Check client contracts and NDAs before uploading customer drawings. [[2026-10-05-aibs-handbook-themes-1-2]] [[2026-09-24-aibs-handbook-trust-ai-safety]]

Confidence note: both sources are chapters of the same course handbook, so 0.75 is the ceiling.

## Related

- [[ai-pilot-evaluation]]
- [[ai-data-readiness]]
- [[human-oversight-of-ai]]
