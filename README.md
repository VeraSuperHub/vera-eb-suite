# NIW Skill Suite

**Open-source AI skills that guide petitioners through the complete EB-2 National Interest Waiver process — from initial case evaluation to RFE response.**

Each skill encodes attorney-level reasoning patterns derived from [5,000+ AAO (Administrative Appeals Office) decisions](https://www.uscis.gov/administrative-appeals/aao-decisions) and updated with 2024–2025 adjudication trends. Built for [Claude](https://claude.ai).

> **Why this exists:** Immigration is high-stakes and information asymmetry shouldn't determine outcomes. A seasoned NIW attorney makes dozens of judgment calls during petition preparation — most follow discoverable patterns. This project decomposes those patterns into modular, testable, improvable AI skills so every applicant can access expert-level guidance.

---

## The Pipeline

```
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  1. EVALUATE │────▶│ 2. ENDEAVOR  │────▶│  3. PILLAR   │
  │  Go/no-go    │     │  Endeavor    │     │  ×3 runs     │
  │  assessment  │     │  statement   │     │  (one per    │
  │              │     │  + 3 pillar  │     │   pillar)    │
  └──────────────┘     │  seeds       │     └──────┬───────┘
                       └──────────────┘            │
                                                   ▼
  ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
  │ 7. RFE      │     │ 6. PL       │◀────│ 5. ASSEMBLE  │
  │ RESPONSE    │     │ REVIEW      │     │  Full .docx  │
  │ (if needed) │     │ Adversarial │     │  petition    │
  └─────────────┘     │ QA gate     │     └──────┬───────┘
                      └─────────────┘            │
                            ▲              ┌─────┴────────┐
                            └──────────────│ 4. RECOMMEND │
                                           │  Reference   │
                                           │  letters     │
                                           └──────────────┘
```

---

## Skills

| # | Skill | What It Does | Lines |
|---|-------|-------------|-------|
| 1 | [`vera-niw-evaluate`](skills/vera-niw-evaluate/) | Evaluates the petitioner's profile, selects the optimal pathway, identifies strengths and gaps, and produces a go/no-go recommendation with a confidence score | 571 |
| 2 | [`vera-niw-endeavor`](skills/vera-niw-endeavor/) | Drafts the national importance endeavor statement — the single paragraph USCIS reads first — using field-specific framing patterns | 368 |
| 3 | [`vera-niw-pillar`](skills/vera-niw-pillar/) | Writes the three-pillar petition letter covering Prong 1 (substantial merit + national importance), Prong 2 (well-positioned), and Prong 3 (balance of equities). Run once per pillar. | 452 |
| 4 | [`vera-niw-recommendation`](skills/vera-niw-recommendation/) | Generates recommendation letters with writer-specific voice calibration, ensuring each letter covers different evidence angles without redundancy | 535 |
| 5 | [`vera-niw-assemble`](skills/vera-niw-assemble/) | Assembles the final petition package — petition letter, exhibit list, and supporting documents — as an attorney-quality .docx with cross-reference verification | 334 |
| 6 | [`vera-niw-pl-review`](skills/vera-niw-pl-review/) | Adversarial pre-filing review simulating a USCIS officer — 10 denial-pattern checks (A–J) mapped to real AAO denial grounds | 644 |
| 7 | [`vera-niw-rfe-response`](skills/vera-niw-rfe-response/) | Generates point-by-point RFE responses that quote each USCIS finding verbatim and rebut with evidence, updated metrics, and new exhibits | 499 |

**Total: 3,403 lines of encoded expert reasoning across 7 skills.**

---

## Quick Start

### Requirements
- A [Claude Pro](https://claude.ai/upgrade) subscription (for Projects with custom instructions)

### Installation

**Requirements:**
- [Claude Pro, Max, Team, or Enterprise](https://claude.ai/upgrade) subscription
- Code execution enabled (Settings → Capabilities)

**Step 1 — Download the skill**

Download the ZIP file for the skill you want from this repo (each skill folder is a standalone package).

**Step 2 — Upload to Claude**

1. Go to [Settings → Capabilities](https://claude.ai/settings/capabilities)
2. Scroll to the **Skills** section
3. Click **"Upload skill"**
4. Upload the skill's ZIP file
5. Toggle the skill **on**

That's it. Claude will automatically invoke the skill when your request matches its description — no manual activation needed. You'll see the skill appear in Claude's chain of thought as it works.

**Install one skill at a time.** Each skill is a separate ZIP upload. For the full pipeline, install all 7.

### Recommended Workflow

Start with **Evaluate** to get your go/no-go assessment. If the verdict is QUALIFIED or LIKELY_QUALIFIED, proceed through the pipeline in order:

```
Evaluate → Endeavor → Pillar (×3) → Recommendation (×N) → Assemble → PL Review
```

Each skill's output is designed as input for the next skill in the pipeline. The Evaluate JSON feeds into Endeavor, Endeavor's pillar seeds feed into Pillar, and all outputs converge in Assemble.

---

## Usage Examples

**Evaluate — Am I qualified?**
```
I'm a senior data scientist at a Fortune 500 company with 5 years of experience.
I have 3 publications (12 citations total), 2 patents pending, and my fraud
detection system processes 2M+ transactions daily. Evaluate my NIW case.
```

**Endeavor — Define the proposed endeavor:**
```
I just completed NIW_Evaluate and got LIKELY_QUALIFIED. Here's my JSON output:
[paste evaluate output]
Help me draft my proposed endeavor.
```

**Pillar — Write petition content:**
```
Here's my endeavor statement and three pillar definitions from NIW_Endeavor:
[paste endeavor output]
Write the petition content for Pillar 1.
```

**PL Review — Adversarial quality check:**
```
Review my completed petition letter as a USCIS officer. Find every weakness
that would trigger an RFE.
[paste petition letter]
```

**RFE Response — Fight back:**
```
I received this RFE on my NIW petition. Here's the RFE notice and my
original petition letter. Generate a point-by-point response.
[paste RFE notice]
[paste original petition]
```

---

## How It Works

Each skill encodes expert judgment as a structured decision process:

```
Expert Knowledge (5,000+ AAO decisions)
    ↓
Decompose into decision rules & rubrics
    ↓
Encode as structured AI instructions (SKILL.md)
    ↓
Add reference materials (rubrics, schemas, examples)
    ↓
Validate against test cases (evals/)
```

The key insight: an experienced NIW attorney doesn't use magic — they apply discoverable patterns built from hundreds of cases. Those patterns can be decomposed, encoded, validated, and improved by the community.

Read more: [How Skills Work](docs/how-skills-work.md)

---

## Repo Structure

```
niw-skill-suite/
├── README.md
├── LICENSE
├── DISCLAIMER.md
├── docs/
│   └── how-skills-work.md
└── skills/
    ├── vera-niw-evaluate/          ← Step 1: Go/no-go assessment
    │   ├── SKILL.md                   571 lines
    │   ├── README.md
    │   ├── schema/output_schema.json
    │   ├── rubric/field_alignment.md
    │   ├── examples/                  3 example outputs
    │   └── evals/evals.json
    ├── vera-niw-endeavor/          ← Step 2: Endeavor statement
    │   ├── SKILL.md                   368 lines
    │   ├── README.md
    │   ├── references/                2 reference docs
    │   └── evals/evals.json
    ├── vera-niw-pillar/            ← Step 3: Petition content (×3)
    │   ├── SKILL.md                   452 lines
    │   ├── README.md
    │   ├── schema/output_schema.json
    │   └── evals/evals.json
    ├── vera-niw-recommendation/    ← Step 4: Reference letters
    │   ├── SKILL.md                   535 lines
    │   ├── README.md
    │   └── evals/evals.json
    ├── vera-niw-assemble/          ← Step 5: Final .docx assembly
    │   ├── SKILL.md                   334 lines
    │   ├── README.md
    │   ├── references/                2 reference docs
    │   └── evals/evals.json
    ├── vera-niw-pl-review/         ← Step 6: Adversarial review
    │   ├── SKILL.md                   644 lines
    │   ├── README.md
    │   ├── references/                4 reference docs
    │   └── evals/evals.json
    └── vera-niw-rfe-response/      ← Step 7: RFE rebuttal
        ├── SKILL.md                   499 lines
        ├── README.md
        ├── reference/rebuttal-patterns.md
        └── evals/evals.json
```

---

## FAQ

**Is this legal advice?**
No. See [DISCLAIMER.md](DISCLAIMER.md). These tools provide informational guidance only. Always consult a qualified immigration attorney for your specific case.

**Do I need to be technical?**
No. If you can use Claude, you can use these skills. Copy, paste, follow the prompts.

**Will this guarantee my NIW approval?**
No tool or attorney can guarantee approval. These skills help you identify weaknesses and build a stronger petition before filing.

**How is this different from ChatGPT prompts for NIW?**
Generic prompts produce generic output. Each skill here encodes hundreds of specific decision rules — failure pattern detection, field-specific framing, USCIS-language calibration — derived from systematic analysis of AAO decisions. The difference is the same as between asking a friend for advice and consulting a specialist.

**Can I use this with GPT-4 or other models?**
The skills are optimized for Claude but the instructions are model-agnostic text. They may work with other capable models, though output quality may vary.

**Can I contribute?**
Yes. See [Contributing](#contributing) below.

---

## Contributing

Contributions welcome. Especially valuable:

- **Bug reports** — Skill produced incorrect or misleading guidance? Open an issue.
- **Test cases** — Real RFE patterns or edge cases for `evals/`. Anonymize all personal information.
- **Reference materials** — New AAO decisions, policy updates, or adjudication trend data.
- **Skill improvements** — Better rubrics, additional failure patterns, improved prompts.

---

## Disclaimer

These tools are for **informational and educational purposes only**. They do not constitute legal advice and do not create an attorney-client relationship. See [DISCLAIMER.md](DISCLAIMER.md) for full terms.

---

## License

MIT License. See [LICENSE](LICENSE).

