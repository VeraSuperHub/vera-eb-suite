# vera-niw-entrepreneur

**Evaluates and guides entrepreneur/founder NIW petitions using the USCIS Policy Manual's entrepreneur-specific framework.**

Part of the [NIW Skill Suite](../README.md) — Entrepreneur pathway (routes into the standard pipeline at Step 2).

## What It Does

Screens entrepreneur cases against USCIS's explicit entrepreneur evidentiary framework (Jan 2025 update), identifies common traps, evaluates 9 evidence categories, and produces an endeavor statement + pillar recommendations that feed into the standard pipeline.

## Position in Pipeline

```
vera-niw-evaluate (Pathway D detected)
    → vera-niw-entrepreneur (you are here)
        → vera-niw-endeavor → vera-niw-pillar (×3) → ...
```

## Invocation

```
I'm a startup founder looking to apply for NIW. My company does [X].
Evaluate my entrepreneur NIW case.
```

Or triggered automatically when `vera-niw-evaluate` detects an entrepreneur pathway.

## Evidence Categories

| # | Category | Required? |
|---|---|---|
| 2.1 | Ownership & Central Role | **Yes** — case cannot proceed without this |
| 2.2 | Background Credentials | No |
| 2.3 | Investment & Financial Evidence | No |
| 2.4 | Incubator/Accelerator Participation | No |
| 2.5 | Intellectual Property | No |
| 2.6 | Awards & Government Support | No |
| 2.7 | Published Materials & Recognition | No |
| 2.8 | Impact Metrics | No |
| 2.9 | Third-Party Validation Letters | No |

## Entrepreneur-Specific Failure Modes

| Trap | What Fails | What Passes |
|---|---|---|
| 1 | Opening a consulting firm in a shortage occupation | Building a specific technology platform addressing a national problem |
| 2 | Industry-level statistics ("car dealerships contribute $X") | Specific endeavor with quantified scope |
| 3 | General "my company will create 50 jobs" | Technology-driven economic value with jobs as one benefit |
| 4 | Benefits limited to specific employers | Systemic problem addressed across the industry |
| 5 | Startup without detailed national impact explanation | Detailed national problem, specific solution, quantified impact |

## Key Context

- USCIS Policy Manual (Jan 2025): "Not every entrepreneur qualifies for national interest waiver."
- STEM entrepreneurs maintain ~90% approval rates
- Non-STEM entrepreneurs face 40-60% denial rates
- Success is not required — but evidence of serious pursuit is

## Output

1. **Evidence Assessment** — scored checklist across all 9 categories
2. **Endeavor Statement** — petition-ready, pattern-checked
3. **Three Pillar Recommendations** — adapted for entrepreneur context
4. **Evidence Gap Analysis** — what's missing and how to obtain it
5. **Recommended Next Steps** — routes to standard pipeline

## Files

```
vera-niw-entrepreneur/
├── SKILL.md                           300 lines
├── README.md
└── evals/evals.json                   4 test cases
```

## Evals

4 test cases covering:
1. Strong STEM entrepreneur (biotech, VC, patents, SBIR) → QUALIFIED
2. IT consulting trap (shortage occupation) → Trap 1/3/4 triggered
3. PhD in wrong occupation (restaurant) → EB-2 gate failure
4. Startup without detailed impact → Trap 2/5 triggered
