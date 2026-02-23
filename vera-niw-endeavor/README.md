# vera-niw-endeavor

**Version:** 1.0.0  
**Part of:** NIW Petition Skill System  
**Depends on:** NIW_Evaluate (recommended — optional)  
**Feeds into:** NIW_Pillar (one pillar seed per pillar run)

---

## What This Skill Does

Guides NIW applicants through brainstorming and crystallizing their **proposed
endeavor** — the single most important element of an NIW petition, and the
#1 cause of RFEs when done wrong.

The skill transforms raw expertise into a specific, named, bounded undertaking
that passes USCIS scrutiny under the Dhanasar (2016) framework. It does this
through a structured 4-phase process:

1. **Diagnose** — score any existing draft against USCIS failure patterns
2. **Interview** — extract the 6 required ingredients
3. **Draft** — produce 2 candidate statements (narrow + broad)
4. **Stress-test** — validate against all patterns, then finalize

---

## How to Invoke

**If you have an NIW_Evaluate output (recommended):**
> "I just completed NIW_Evaluate and got [VERDICT]. Here's my JSON:
> [paste output]. Help me draft my proposed endeavor."

**If starting fresh:**
> "Help me brainstorm my NIW proposed endeavor. I'm a [brief background]."

**If you have a draft to review:**
> "Can you review and improve my proposed endeavor draft? [paste draft]"

**Direct triggers:**
- "What should my NIW proposed endeavor be?"
- "My endeavor statement is too vague — help me fix it"
- "I got an RFE saying my endeavor is too broad"
- "Help me define my NIW endeavor"

---

## What You'll Get

- **Endeavor statement** — 3–5 sentences, third person, petition-ready prose
- **Pattern check scorecard** — explicit ✅/⚠️/❌ for USCIS failure patterns A, B, C + substitutability test
- **3 pillar seeds** — title + rationale for each, ready to pass directly into NIW_Pillar

---

## The 6 Ingredients

Every valid NIW endeavor needs all six:

| # | Ingredient | What It Is |
|---|---|---|
| 1 | Named project | A proper-noun identifier for the specific work |
| 2 | National-scale problem | Documented, quantified, sourced to a federal/authoritative report |
| 3 | Named methodology | Specific technique — not "AI" or "machine learning" |
| 4 | Application domain | Tier 1 or 2 per field-alignment.md — technology labels stripped |
| 5 | Measurable national outcome | A number: dollars, population, % improvement, scale |
| 6 | Substitutability answer | Why this petitioner specifically — not any qualified peer |

---

## Files

```
vera-niw-endeavor/
├── SKILL.md                         Full skill instructions (292 lines)
├── README.md                        This file
├── evals/
│   └── evals.json                   4 test cases (Routes A, B, C + Tier 3 reframe)
└── references/
    ├── endeavor-anatomy.md          6 ingredients, annotated examples, rewrite templates
    └── field-alignment.md           Tier 1/2/3 domain table, AI-as-method rule
```

---

## Key Rules

1. **Never draft without all 6 ingredients.** Ask for what's missing.
2. **Technology labels (AI/ML/NLP) are methods, not domains.** Strip them. Ask "applied to what?"
3. **Tier 3 domains don't get endorsed — they get reframed.** Offer alternatives, don't paper over a weak case.
4. **Never fabricate statistics or quotes.** Flag as [STATISTIC NEEDED] and ask.
5. **Named projects outperform unnamed work.** Push for a proper-noun project name.
6. **Scale ≠ national importance.** 200M consumer users is scale. It is not NIW evidence.
