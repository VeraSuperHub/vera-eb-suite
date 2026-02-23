# vera-niw-recommendation

**Version:** 1.1.0
**Part of:** NIW Petition Skill System
**One letter per recommender. Run once per letter needed.**

## Position in Pipeline

```
vera-niw-pillar ×3 (Section 6 generates recommender profiles)
        ↓
[vera-niw-recommendation ×3-4]
        ↓
vera-niw-pl-review (Pattern F check before sending to recommender)
        ↓
vera-niw-assemble → .docx
```

**Pipeline shortcut:** If you've run vera-niw-pillar, paste the Section 6
recommender profile block as `PILLAR_RECOMMENDER_GUIDANCE` input — the skill
will pre-populate contributions and key claims from it automatically.

## Three Letter Types

| Type | When to Use | Core Message |
|---|---|---|
| **A — Methodology** | Recommender is in the same technical/methodological field | "This is a genuine theoretical breakthrough" |
| **B — Domain Application** | Recommender is a practitioner who applied the work | "This solved a real problem in my domain" |
| **C — Hybrid** | One recommender covers both dimensions | Methodology innovation + real-world impact |

## Recommended Portfolio Per NIW Petition
- 1× Type A — validates technical originality (same-field academic)
- 1-2× Type B — validates real-world impact (clinician, executive, regulator)
- 1× advisor letter — validates petitioner's role (clearly labeled as affiliated)
- 1× senior practitioner — validates national-scale relevance

## Required Inputs
- Proposed endeavor
- Target pillar (title + description)
- Recommender: name, title, institution, background, credentials
- Independence: how they are independent + exactly how they discovered the work
- Letter type: A / B / C
- Contributions: 2-4 with before/after framing (Type A) or problem/application/outcome/numbers (Type B)
- Federal/national hook

## What Makes a Strong Letter
1. Independence stated explicitly in paragraph 1
2. Specific discovery story (read the paper, requested code, attended seminar)
3. Before/after framing ("Prior to Dr. X's work...")
4. Named method/model acronyms + named journals with rankings
5. Concrete numbers (patients, surgeries, jobs, dollar amounts)
6. Named federal policy connection
7. "As the original developer of X" framing if applicable (most powerful)
8. Strong closing: "strongest recommendation" / "irreplaceable figure"

## Files
```
niw-recommendation/
├── SKILL.md       Full instructions + writing rules for all three types
├── README.md      This file
└── evals/
    └── evals.json 4 test cases (Type A, B, C, incomplete input)
```
