# vera-niw-assemble

**Stage 5 of the NIW Petition Skill System.** Assembles a complete I-140
petition letter as a `.docx` file from all upstream skill outputs and Google
Scholar data.

---

## Position in Pipeline

```
vera-niw-evaluate  →  vera-niw-endeavor  →  vera-niw-pillar ×3
        ↓                    ↓                      ↓
                    [vera-niw-assemble]
                           ↓
              niw_petition_[LastName].docx
                           ↓
                  vera-niw-pl-review  (final quality gate)
```

---

## What it generates vs. passes through

| Section | Origin |
|---|---|
| I. Introduction | **Generated** from evaluate JSON + endeavor statement |
| II. Proposed Endeavor | **Pass-through** from vera-niw-endeavor |
| III. Academic Credentials | **Generated** from Google Scholar JSON + CSV |
| IV–VI. Pillar 1–3 prose | **Pass-through** from vera-niw-pillar runs |
| VII. Unified Prong 3 | **Synthesized** from 3× per-pillar Prong 3 sections |
| VIII. Conclusion | **Generated** |
| IX. Exhibit Index | **Generated** from (See Exhibit [X]) tags in prose |

---

## Required Inputs

1. `vera-niw-evaluate` output JSON
2. `vera-niw-endeavor` output (endeavor statement + 3 pillar titles)
3. `vera-niw-pillar` prose — run 1, run 2, run 3 (Sections 1–5 from each)
4. Google Scholar JSON (`gs_summary.json`) — from GS notebook
5. Google Scholar CSV (`gs_papers.csv`) — from GS notebook

**GS data not yet available?** Provide everything else and the skill will
assemble with `[GS_DATA_NEEDED]` placeholders in Section III.

---

## Updating for the GS Notebook

When the Google Scholar Jupyter notebook is ready:

1. Run it on the petitioner's Scholar profile
2. Save outputs as `gs_summary.json` and `gs_papers.csv`
3. Check `references/gs-schema.md` — if notebook field names differ from
   the placeholder names, update `gs-schema.md` (not SKILL.md)
4. Provide both files to NIW_Assemble along with the other inputs

---

## Full invocation

> "Use vera-niw-assemble to build my final petition document. Here are my
> inputs: [paste evaluate JSON], [paste endeavor statement + pillar titles],
> [paste pillar 1 prose], [paste pillar 2 prose], [paste pillar 3 prose],
> [paste or upload GS JSON and CSV]."

---

## After Assembly

Run `vera-niw-pl-review` on the assembled petition letter as the final
adversarial quality gate before attorney review or filing. NIW_Assemble
produces a complete document — vera-niw-pl-review checks it for RFE risks.
