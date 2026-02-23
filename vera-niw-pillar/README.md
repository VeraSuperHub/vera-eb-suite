# niw-pillar

**Version:** 1.0.0
**Part of:** NIW Petition Skill System
**Depends on:** niw-evaluate (verdict must be QUALIFIED or LIKELY_QUALIFIED)
**Feeds into:** niw-assemble (one output per pillar)

---

## What This Skill Does

Generates a complete, publication-ready NIW petition section for **one pillar**
at a time, covering all three Dhanasar prongs:

- **Prong 1** — Substantial merit and national importance
- **Prong 2** — Petitioner is well-positioned to advance the endeavor
- **Prong 3** — National interest outweighs labor certification requirement

Run this skill once per pillar. A 3-pillar endeavor = 3 runs of this skill.
Combine all outputs in niw-assemble.

---

## How to Invoke

**Full invocation:**
> "Use the niw-pillar skill to write the NIW petition section for Pillar 2
> (Financial Market Integrity) of Dr. Patel's proposed endeavor. Here are
> the pillar details: [paste details]"

**Minimal trigger:**
> "Write NIW Pillar 2 for [applicant]. Pillar: [description]"

---

## Required Inputs

| Input | Required | Notes |
|---|---|---|
| Proposed endeavor statement | Yes | Full text |
| All pillar titles | Yes | So the skill understands context |
| Target pillar | Yes | Number or title |
| Problem description | Yes | Specific, not vague |
| Methodology | Yes | Named technique (e.g., NLP, survival analysis) |
| Past work | Yes | Publications, tools, conference presentations |
| Future plan | Yes | What comes next |
| Statistics | Strongly recommended | Dollar figures, job counts, population percentages |
| Federal connections | Strongly recommended | Named agencies, legislation, dollar amounts |
| Expert endorsements | Strongly recommended | Name, title, institution, quote |

**If statistics or expert names are missing, the skill will ask before writing.**
It will not fabricate numbers or quotes.

---

## Output

- ~1,500–2,500 words of formal legal/academic prose
- Structured with Prong 1 / Prong 2 / Prong 3 headers
- Followed by a JSON metadata block for niw-assemble consumption
- Suitable for direct inclusion in an I-140 NIW petition or RRFE response

---

## Key Quality Rules

Every output must have:
- Specific statistics (no vague scale claims)
- Named methodology (not "advanced methods")
- Named federal agency or legislation
- At least one expert quote with name + institution
- Phased future plan with deliverables
- Third-person prose throughout
- No hedging language

---

## Files

```
niw-pillar/
├── SKILL.md               Full instructions + writing rules
├── README.md              This file
├── schema/
│   └── output_schema.json Output contract for niw-assemble
└── evals/
    └── evals.json         4 test cases covering full/partial/industry inputs
```
