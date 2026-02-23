# NIW_Evaluate

**Version:** 1.0.0
**Part of:** NIW Petition Skill System
**Next skill:** NIW_Endeavor (if QUALIFIED or LIKELY_QUALIFIED)

---

## What This Skill Does

Evaluates whether a user qualifies for a National Interest Waiver (NIW)
self-petition. Produces a structured verdict with strengths, gaps, evidence
scoring, and a recommended action plan.

Always errs conservative. The NIW bar is high and a weak petition costs more
than waiting.

---

## How to Invoke

Simply ask Claude to evaluate your NIW background and provide your information.
You can provide it as free text, a resume/CV upload, or a structured JSON block.

**Minimal invocation:**
> "Evaluate my NIW background: [paste your background info]"

**Full invocation:**
> "Use the NIW_Evaluate skill to assess whether I qualify for a National
> Interest Waiver. Here is my background: [info]"

---

## What to Provide

| Field | Required | Notes |
|---|---|---|
| Name + pronoun | Yes | |
| Highest degree, field, university, year | Yes | |
| Current title + employer | Yes | |
| Years of experience | Yes | |
| Publications (count, breakdown, venues) | If academic | |
| Citation count + h-index | If academic | Google Scholar preferred |
| Peer review count | If academic | |
| Key projects (title, outcome, evidence) | Yes | Be specific about evidence |
| Field / domain | Yes | Be precise — "AI" alone is not sufficient |

---

## Output

Produces a JSON evaluation result (see `schema/output_schema.json`) and a
plain-English summary with:
- **Verdict**: QUALIFIED / LIKELY_QUALIFIED / BORDERLINE / NOT_QUALIFIED
- **Top strengths** (3)
- **Top gaps** (3) with concrete actions to close each
- **Evidence scores** per claim
- **Recommended pillar previews** (if qualified — feeds NIW_Endeavor)

---

## Verdict Definitions

| Verdict | Meaning | Next Step |
|---|---|---|
| QUALIFIED | Strong case, proceed | → NIW_Endeavor |
| LIKELY_QUALIFIED | Good case with addressable gaps | → NIW_Endeavor (note conditions) |
| BORDERLINE | Meaningful gaps; address before filing | Fix gaps first, re-evaluate |
| NOT_QUALIFIED | Does not meet threshold | Gap analysis + timeline to qualify |

---

## Key Rules

1. **AI is a method, not a domain.** "AI for public health" = Tier 1. "AI for marketing" = Tier 3.
2. **Every claim needs evidence.** No evidence = blocking gap.
3. **Objective evidence > subjective evidence.** Both are needed; neither alone is sufficient.
4. **Conservative by default.** When in doubt, lower verdict.

---

## Files

```
NIW_Evaluate/
├── SKILL.md                  Full evaluation instructions + rubric
├── README.md                 This file
├── schema/
│   └── output_schema.json    Formal output contract (consumed by NIW_Endeavor)
├── examples/
│   ├── qualified_output.json     Sample QUALIFIED evaluation
│   ├── borderline_output.json    Sample BORDERLINE evaluation
│   └── not_qualified_output.json Sample NOT_QUALIFIED evaluation
└── evals/
    └── evals.json            6 test cases for skill validation
```
