Theme 1 — What don’t we know yet about AI, and what should
we find out first?
This chapter helps an owner find the one AI gap that blocks a decision now.
[Team name] · [Cohort] · v0.6 · SME: persona — a fictional 40-person Dutch firm that designs and builds machines · Sources last
appraised: 5 Oct 2026

The question, for this kind of SME
We are a 40-person firm that designs and builds machines in SOLIDWORKS, with PDM, ERP and spreadsheets. We
record our own machine hours. Which AI use do we test first, and how will we know it worked?

The translation
•  What firms like ours do. AI use at Dutch firms with 10–50 people rose to 27% in 2025, mostly for marketing and
admin (CBS, 2025). Owners use Copilot or ChatGPT for quotes and keep a human in charge (Midpoint Brabant,
2025; van der Meer, 2025).

•  What they lack. "Lack of experience" is the top barrier (73%) (CBS, 2025). 83% of SME manufacturers in Brabant

do not know where AI fits in production (FME, 2026).

The firm says it needs
More experience (CBS, 2025)

Legal clarity (CBS, 2025)

(Not named)

The evidence shows it needs
A way to judge output: AI fails where users do not
expect it (Dell'Acqua et al., 2023)
One duty already applies: AI literacy, since
February 2025 (European Union, 2024)
Usable data: often "not in order" (Vankan et al.,
2025); poor data makes models worse (OECD,
2025a)

Difference
Experience alone does not show where
AI fails
The law is a reason to act, not to wait

The biggest difference: surveys do not
ask about data (Eurostat, 2025)

The gap that matters most now
We do not know if our own data is good enough to test one AI use, so we cannot tell whether AI is right or pays
off. Without a baseline, a payback rule such as "one year at most" (Midpoint Brabant, 2025) cannot be applied.

Illustrative use case (CRISP-DM, first steps)
1. Business understanding: write one goal and a payback limit (Linssen et al., 2025). 2. Data understanding: check
whether recorded hours link to a part or drawing in ERP and PDM. Theme 2 runs all six phases.

Recommended tooling
An Excel export from ERP and PDM, with Copilot or ChatGPT for formulas (van der Meer, 2025): a few days. A short in-
house AI literacy session (European Union, 2024): a few hours.

Responsible AI & trust
•  Your data. 52% of firms worry about data fed into AI (OECD, 2025b). Limit who may upload confidential files (van

der Meer, 2025).

•  Rules. Staff who use AI need AI literacy (European Union, 2024). Ask your adviser whether booked hours count as

personal data under the GDPR.

•  People. An expert accepts or rejects every AI suggestion (van der Meer, 2025). Name an owner and a back-up: a

tool fell into disuse when its builder left (van Ginkel, 2025).

First five steps for an owner
1.  Name one decision and goal, with a payback limit (Linssen et al., 2025; Midpoint Brabant, 2025).
2.  Measure your baseline: compare quoted and actual hours on 20–30 recent jobs.
3.  Check your data: can recorded hours be linked to parts in ERP or PDM? (FME, 2026; Vankan et al., 2025)
4.  Appoint an owner and a back-up, and train AI users (European Union, 2024).
5.  Ask your ERP and SOLIDWORKS suppliers what AI is coming (Midpoint Brabant, 2025). Then find out first: is our

data good enough to test AI cost estimation? (Theme 2)

AIBS handbook · Page 1

Theme 2 — What do firms like ours use AI for, and what pays
off?
This chapter helps an owner test one AI use and tell whether it pays off.
[Team name] · [Cohort] · v0.4 · SME: persona — a fictional 40-person Dutch firm that designs and builds machines · Sources last
appraised: 5 Oct 2026

The question, for this kind of SME
Theme 1 found that we do not know if our data is good enough to test AI. Which AI use should we test first, and how
will we know it works?

The translation
AI use
Chat assistant for reports and Excel

Cost estimation for quotes

AI-made drawings in SOLIDWORKS
Models on own data (custom GPTs,
CAM)

Payoff evidence
Measured: 2.8% of work hours saved on average
(Humlum & Vestergaard, 2025)
About 23.5% error with little data (Manuguerra et
al., 2023); about 10% with 13,684 drawings (Arıkan
et al., 2025)
No figures; output needs cleanup (Keglovits, 2025)
Expected, not yet reached (van der Meer, 2025)

Data needed
Text, documents

Drawings, material, batch size,
actual hours (Jacobs, 2025)

3D models, templates
Own history, manuals

Only office assistants have measured gains, and they are small (Humlum & Vestergaard, 2025). We chose cost
estimation for quotes: it runs on the data Theme 1 questions, own drawings and recorded hours (Jacobs, 2025), so
testing it also tests the data gap. Start with in-house parts, not whole machines.

Illustrative use case: AI cost estimation (CRISP-DM)
Phase
1. Business

What you do
Set a goal, pass level and payback limit (Linssen et al.,
2025; Midpoint Brabant, 2025).
List models, drawings, quotes and hours.
One table: past parts, quoted and actual hours.
Trial a commercial platform first.

2. Data
3. Preparation
4. Modelling

5. Evaluation

Compare AI, human quote and actual cost.

6. Deployment

AI drafts; the estimator decides (van der Meer, 2025).

Data reality
Build a baseline from past jobs.

Data use is weak at 80% of firms (FME, 2026).
Poor data makes models worse (OECD, 2025a).
Gives a market average, not your costs (Jacobs,
2025).
AI can be wrong on unusual parts (Dell'Acqua et
al., 2023).
Without an owner, it falls into disuse (van
Ginkel, 2025).

Pass level, set in advance: error no worse than your human quote (about 23.5% with little data (Manuguerra et al.,
2023)), less time per quote, payback within one year (Midpoint Brabant, 2025).

Recommended tooling
Excel baseline: days. Quoting platform trial, such as The Quotation Factory (Brouwers, 2024): weeks. Own model with
a knowledge centre (Linssen et al., 2025): months.

Responsible AI & trust
•  Your data. Test on your own parts. Check client contracts before uploading their drawings.
•  Reliability. Accuracy is tested only on other parts (Arıkan et al., 2025; Manuguerra et al., 2023). Your own test in

phase 5 is the real check.

•  People. A named person approves every quote. Benefits rise 10–40% when employers encourage use (Humlum &

Vestergaard, 2025).

First five steps for an owner
1.  Write the pass level down before you start (Manuguerra et al., 2023; Midpoint Brabant, 2025).
2.  Build a test set of 20–30 past in-house parts with quoted and actual hours and cost (Jacobs, 2025).
3.  Check contracts, then trial one quoting platform on that set (Brouwers, 2024).
4.  Compare AI, human quote and actual cost with your estimator (Dell'Acqua et al., 2023).
5.  Decide: stop, use, or build your own model with a knowledge centre (Linssen et al., 2025).

AIBS handbook · Page 2

Sources for Theme 1 and Theme 2
APA 7. Sources marked (translated from Dutch) are quoted in our English translation.
Arıkan, A. B., Özönder, Ş., Koçyiğit, M. T., Altun, H. O., Küçükkartal, H. K., Arslanoğlu, M., Çağırankaya, F., & Ayvaz, B. (2025).

Machine learning-based manufacturing cost prediction from 2D engineering drawings via geometric features [Preprint]. arXiv.
https://arxiv.org/abs/2508.12440v1

Brouwers, B. (2024, March 15). The Quotation Factory pakt tweeledig probleem aan voor metaalindustrie: betere offertes met

minder personeel [The Quotation Factory tackles a two-sided problem for the metal industry: Better quotes with fewer staff].
IO+. https://ioplus.nl/archive/nl/the-quotation-factory-pakt-tweeledig-probleem-aan-voor-metaalindustrie-betere-offertes-
met-minder-personeel/ (translated from Dutch)

CBS (Statistics Netherlands). (2025, December 12). Bedrijven gebruiken AI vaakst voor marketing of verkoop [Companies use AI

most often for marketing or sales]. https://www.cbs.nl/nl-nl/nieuws/2025/50/bedrijven-gebruiken-ai-vaakst-voor-marketing-
of-verkoop (translated from Dutch)

Dell'Acqua, F., McFowland, E., III, Mollick, E., Lifshitz-Assaf, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R.
(2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker
productivity and quality (Working Paper No. 24-013). Harvard Business School. https://ssrn.com/abstract=4573321

European Union. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 4: AI literacy. EU Artificial Intelligence Act.

https://artificialintelligenceact.eu/article/4/

Eurostat. (2025). Use of artificial intelligence in enterprises. Statistics Explained. Retrieved October 5, 2026, from

https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Use_of_artificial_intelligence_in_enterprises

FME. (2026, April 14). Onderzoek: mkb-maakindustrie zet digitaliseringsstappen, maar productiviteitswinst blijft achter [Research:

SME manufacturing is taking steps in digitalisation, but productivity gains are lagging behind].
https://www.fme.nl/nieuws/onderzoek-mkb-maakindustrie-zet-digitaliseringsstappen-maar-productiviteitswinst-blijft
(translated from Dutch)

Humlum, A., & Vestergaard, E. (2025). Large language models, small labor market effects (Working Paper No. 2025-56). Becker

Friedman Institute, University of Chicago. https://bfi.uchicago.edu/working-paper/large-language-models-small-labor-market-
effects/

Jacobs, T. (2025, October 13). Automated production cost prediction using AI. Sirris.

https://www.sirris.be/en/inspiration/automated-production-cost-prediction-using-ai

Keglovits, N. (2025, November 13). SOLIDWORKS 2026: Enhanced visuals, smarter part design, and auto-generate drawings. Hawk

Ridge Systems. https://hawkridgesys.com/blog/upgrading-solidworks-2026-new-features

Linssen, J., Tunuguntla, D., & Ahmed, F. (2025). Zijn we er al? Te nemen stappen voor de toepassing van AI in de maakindustrie [Are
we there yet? Steps to take to apply AI in manufacturing]. Fraunhofer Innovation Platform at the University of Twente.
https://fip.utwente.nl/wp-content/uploads/2025/07/IN15_TECHINNO_Are-we-there-yet_Saxion_NL.pdf (translated from
Dutch)

Manuguerra, L., Mandolini, M., Germani, M., & Sartini, M. (2023). Machine learning for parametric cost estimation of axisymmetric

components. Proceedings of the Design Society, 3. https://doi.org/10.1017/pds.2023.249

Midpoint Brabant. (2025, November 25). Wat betekent AI voor Janus Metaal, Chromalloy en andere maakbedrijven? [What does AI

mean for Janus Metaal, Chromalloy and other manufacturing companies?]. https://midpointbrabant.nl/succesverhalen/wat-
betekent-ai-voor-janus-metaal-chromalloy-en-andere-maakbedrijven/ (translated from Dutch)

OECD. (2025a). AI adoption by small and medium-sized enterprises [Discussion paper for the 2025 G7 Presidency of Canada]. OECD

Publishing. https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/ai-adoption-by-small-and-medium-
sized-enterprises_9c48eae6/426399c1-en.pdf

OECD. (2025b). Generative AI and the SME workforce: New survey evidence. OECD Publishing. https://doi.org/10.1787/2d08b99d-

en

van der Meer, T. (2025, February 25). Kunstmatige intelligentie in de praktijk in het metaalbedrijf [Artificial intelligence in practice
at metal companies]. Metaal Magazine. https://www.metaalmagazine.nl/nieuws/kunstmatige-intelligentie-in-de-praktijk-in-
het-metaalbedrijf/103593/ (translated from Dutch)

van Ginkel, J. (2025, February 27). AI: een lappendeken van succesverhalen en teleurstellingen [AI: A patchwork of success stories
and disappointments]. Link Magazine. https://linkmagazine.nl/ai-een-lappendeken-van-succesverhalen-en-teleurstellingen/
(translated from Dutch)

Vankan, A., Verhagen, P., Brouwers, L., Boiten, M., de Moor, G., & van der Vorst, T. (2025). Onderzoek AI-gebruik in het mkb:
Ambitie of aarzeling? [Research on AI use in SMEs: Ambition or hesitation?] (Publication No. 2025.035-2531). Dialogic,
commissioned by the Ministry of Economic Affairs. https://open.overheid.nl/documenten/30ab7be6-a0ea-4e4f-bf86-
91157c56ccc8/file (translated from Dutch)

AIBS handbook · Page 3

