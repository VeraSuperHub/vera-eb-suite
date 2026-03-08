# vera-niw-rfe-response

**Generates point-by-point RFE responses that force officers to write from scratch to justify denial.**

Part of the [NIW Skill Suite](../README.md) — Step 7 in the pipeline (used only when an RFE is received).

## What It Does

Takes the RFE notice, original petition, reference letters, and any new evidence gathered since filing, then produces a structured rebuttal document that quotes each USCIS finding verbatim and rebuts it with evidence.

## Position in Pipeline

```
[RFE Received] + original petition + reference letters
    → vera-niw-rfe-response (you are here)
        → vera-niw-pl-review (quality check on response)
```

## Invocation

```
I received this RFE on my NIW petition. Here's the RFE notice and my
original petition letter. Generate a point-by-point response.
[paste RFE notice]
[paste original petition]
```

## Rebuttal Patterns

| Pattern | Trigger | Strategy |
|---|---|---|
| R1 | Publications too recent | Peer review cycle timelines, pre-publication evidence |
| R2 | No government letters | Cite Dhanasar (not required), federal mandate mapping |
| R3 | No economic effects | Clarify not independent requirement, three evidence lines |
| R4 | Work not adopted | Citation independence analysis, categorize by usage type |
| R5 | Not lead author | Authorship conventions, co-author attribution letters |
| R6 | Low citation count | Growth trajectory, quality over quantity, ESI percentiles |
| R7 | Peer review insufficient | Editorial board attestation |
| R8 | Prong 3 balance | Counterfactual, structural PERM incompatibility, urgency |

## 2025-2026 RFE Trends

- Intensified national importance scrutiny
- Financial self-sufficiency demands for entrepreneurs
- Implementation vs. Innovation as standalone denial ground
- Occupation-level EB-2 gate challenges (Jan 2025)
- EB-1A standard misapplication (correctable with Dhanasar citation)
- Prong 3 as standalone denial trigger

## Output Structure

1. **Header** — case identification
2. **Opening** — Dhanasar framework + updated metrics headline
3. **Section I** — Clarified endeavor (if needed)
4. **Section II** — Prong 1 point-by-point rebuttals + affirmative case
5. **Section III** — Prong 2 rebuttals + progress since filing
6. **Section IV** — Prong 3 balance argument
7. **Section V** — Conclusion + prayer for relief
8. **Appendix** — New exhibits table

## Key Rules

- Never introduce a materially new endeavor (the "new endeavor trap")
- Never argue labor shortage — this undermines Prong 3
- Assertive tone, no hedging ("the record establishes," not "we believe")
- Quote officer findings verbatim before each rebuttal
- Fresh recommendation letters are the most effective RFE rebuttal tool
- Run `vera-niw-pl-review` on the completed response before filing

## Files

```
vera-niw-rfe-response/
├── SKILL.md                           541 lines
├── README.md
├── reference/rebuttal-patterns.md     R1–R8 pattern library
└── evals/evals.json                   6 test cases
```

## Evals

6 test cases covering:
1. Low citations + weak adoption → R4/R6 rebuttals
2. Recent publications + national importance gaps → R1/R2/R3 rebuttals
3. EB-1A misapplication edge case → Dhanasar correction
4. New endeavor trap edge case → Warning against material change
5. Should-not-trigger: new petition (routes to `vera-niw-endeavor`)
6. Should-not-trigger: qualification assessment (routes to `vera-niw-evaluate`)
