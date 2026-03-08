# vera-niw-pl-review

**Adversarial pre-filing review that simulates a USCIS officer to find every weakness before filing.**

Part of the [NIW Skill Suite](../README.md) — Step 6 in the pipeline.

## What It Does

Reviews petition letters (PL), reference letters (RL), and attorney briefs against 10 real AAO denial patterns, producing a structured risk assessment with actionable rewrite guidance.

This is the quality gate before filing. Run this on the output of `vera-niw-assemble` and on every recommendation letter from `vera-niw-recommendation`.

## Position in Pipeline

```
vera-niw-assemble → vera-niw-pl-review (you are here)
vera-niw-recommendation → vera-niw-pl-review (letter check)
```

## Invocation

```
Review my completed petition letter as a USCIS officer. Find every weakness
that would trigger an RFE.
[paste or upload petition letter]
```

## Denial Patterns Checked

| Pattern | Name | What It Catches |
|---|---|---|
| 0 | EB-2 Gate | Occupation doesn't require advanced degree |
| A | Occupation ≠ Endeavor | Describes a job, not a bounded undertaking |
| B | Vagueness | Could apply to any competent professional |
| C | National vs. Field Importance | Argues field significance, not specific impact |
| D | Publication Due Diligence | 5-step audit: venue tier, trajectory, authorship, citation quality, industry exception |
| E | Prong 2 Failures | No business plan, no third-party interest, no independence |
| F | Recommendation Letter Failures | Non-independent, no before/after framing, generic superlatives |
| G | Prong 3 Balance Failures | No PERM impracticality argument, no urgency |
| H | Evidence Organization | Missing exhibits, technical compliance issues |
| I | Implementation vs. Innovation | Applying existing methods vs. creating new ones (2024-2025 trend) |
| J | EB-1A Misapplication | Officer using wrong legal standard (2024-2025 trend) |

## Output Structure

1. **USCIS Officer Review** — finding-by-finding in officer voice, per-prong assessments
2. **Publication Due Diligence** — 5-step audit with per-paper table
3. **Overall RFE Risk** — HIGH / MEDIUM / LOW with priority-ordered critical gaps
4. **Rewrite Guidance** — concrete example rewrites for each critical gap

## Standalone Deployable Version

The `references/vera-niw-pl-review-deployable.md` file contains a self-contained version of this review that can be used as a system prompt with any LLM API (Claude, GPT-4, Gemini, etc.) without the Skills platform.

## Key Rules

- Conservative by default — calibrated to FY 2024 approval rates (43.31%)
- Assertions without exhibits are not evidence
- Recommendation letter independence is binary — no soft calls
- Publication trajectory gates everything else for academic cases
- Does not invent problems — genuinely strong sections are acknowledged

## Files

```
vera-niw-pl-review/
├── SKILL.md                           670 lines
├── README.md
├── references/
│   ├── pub-diligence.md               5-step publication audit framework
│   ├── field-alignment.md             3-tier field classification rubric
│   ├── eb2-eligibility.md             Jan 2025 EB-2 policy gate
│   └── vera-niw-pl-review-deployable.md  standalone prompt version
└── evals/evals.json                   4 test cases
```

## Evals

4 test cases covering:
1. Vague endeavor with occupation framing → Pattern A flag
2. Weak recommendation letter → Pattern F flag (non-independence, missing before/after)
3. Strong petition → LOW/MEDIUM risk acknowledgment
4. RFE response petition → Named endeavor recognition
