# Vera EB Suite

> Hi, I'm **Vera** — a silicon-based rabbit who documents the open-source Claude skills Veronica created.
>
> Veronica has a PhD in Quantitative Sciences, 10+ years across quantitative research, AI, and clinical trials, with publications in psychometrics and human-AI collaboration. She also went through the NIW process herself. She created this suite to systematize the parts of evidence-building and petition preparation that can be decomposed, documented, and reviewed. I help structure the workflows. She reviews, tests, and decides what ships.
>
> Everything in this repo is what can be made explicit: evidence organization, gap spotting, document drafting support, and review workflows. What the suite cannot do is assess whether your specific case will be approved, provide legal advice, or replace an experienced immigration attorney. That remains a human and legal judgment.

**Open-source Claude skills and plugins for EB-1 and EB-2 NIW evidence-building and petition-preparation support — from evidence review and case organization to drafting workflows, recommendation-letter support, pre-filing review, and RFE response preparation.**

Each skill encodes structured reasoning patterns derived from public USCIS materials, AAO decisions, policy guidance, and evidence-organization workflows. Built for [Claude](https://claude.ai).

> **Why this exists:** Immigration petitions are high-stakes, and information asymmetry can make the process harder than it needs to be. Many parts of evidence-building and petition preparation follow patterns that can be made explicit: organizing exhibits, identifying gaps, mapping evidence to criteria, drafting structured narratives, and stress-testing a petition before filing. This project decomposes those repeatable parts into modular, testable, improvable Claude skills — while leaving legal strategy, approval assessment, and final judgment to qualified human professionals.

---

## The Pipelines

### NIW Pipeline (EB-2 National Interest Waiver)

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

Entrepreneur cases route through **vera-niw-entrepreneur** before entering the standard pipeline at Step 2.

### EB-1 Pipeline (Extraordinary Ability / Outstanding Researcher)

> **STEM focus:** The criterion skills below cover the criteria most commonly used in STEM petitions. This is not the full set of EB-1 criteria — criteria such as awards (Crit. 1), membership (Crit. 2), high salary (Crit. 9), and commercial success (Crit. 10) are not yet included. For EB-1A, petitioners must meet at least 3 of the 10 criteria; for EB-1B, petitioners must meet at least 2 of the 6 criteria. Use the criterion skills that match your evidence.

```
  ┌──────────────┐     ┌──────────────────────────────────────┐
  │  1. EVALUATE │────▶│  2. CRITERION SKILLS                 │
  │  Go/no-go    │     │  ┌────────────┐  ┌────────────────┐  │
  │  EB-1A vs    │     │  │ AUTHORSHIP │  │ ORIGINAL       │  │
  │  EB-1B       │     │  │ (Crit. 6)  │  │ CONTRIBUTIONS  │  │
  │              │     │  └────────────┘  │ (Crit. 5)      │  │
  └──────────────┘     │  ┌────────────┐  └────────────────┘  │
                       │  │ JUDGING    │  ┌────────────────┐  │
                       │  │ (Crit. 4)  │  │ CRITICAL ROLE  │  │
                       │  └────────────┘  │ (Crit. 8)      │  │
                       │  ┌────────────┐  └────────────────┘  │
                       │  │ PUBLISHED  │                      │
                       │  │ MATERIAL   │                      │
                       │  │ (Crit. 3)  │                      │
                       │  └────────────┘                      │
                       └──────────────────┬───────────────────┘
                                          ▼
    ┌─────────────┐     ┌─────────────┐  ┌──────────────┐
    │ 6. RFE      │     │ 5. PL       │◀─│ 4. ASSEMBLE  │
    │ RESPONSE    │     │ REVIEW      │  │  Full .docx  │
    │ (if needed) │     │ Adversarial │  │  petition    │
    └─────────────┘     │ QA gate     │  └──────┬───────┘
                        └─────────────┘         │
                              ▲           ┌─────┴────────┐
                              └───────────│ 3. RECOMMEND │
                                          │  + FINAL     │
                                          │  MERITS      │
                                          └──────────────┘
```

---

## Skills

### NIW ([`vera-niw.plugin`](vera-niw.plugin) / [`vera-niw-skillset/`](vera-niw-skillset/))

| # | Skill | What It Does |
|---|-------|-------------|
| 1 | `vera-niw-evaluate` | Reviews the petitioner's profile, maps available evidence to NIW requirements, identifies strengths, gaps, and risk areas, and produces a structured evidence-readiness summary |
| 2 | `vera-niw-endeavor` | Drafts the national importance endeavor statement — the single paragraph USCIS reads first — using field-specific framing patterns |
| 3 | `vera-niw-pillar` | Writes the three-pillar petition letter covering Prong 1 (substantial merit + national importance), Prong 2 (well-positioned), and Prong 3 (balance of equities). Run once per pillar |
| 4 | `vera-niw-recommendation` | Generates recommendation letters with writer-specific voice calibration, ensuring each letter covers different evidence angles without redundancy |
| 5 | `vera-niw-assemble` | Assembles a draft petition-support package — petition-letter draft, exhibit list, and supporting-document structure — as a review-ready .docx with cross-reference checks |
| 6 | `vera-niw-pl-review` | Adversarial pre-filing review using denial-pattern checks mapped to public AAO reasoning patterns and common evidence weaknesses |
| 7 | `vera-niw-rfe-response` | Drafts a structured point-by-point RFE response framework that organizes each USCIS finding, relevant evidence, updated metrics, and potential new exhibits for human review |
| 8 | `vera-niw-entrepreneur` | Evaluates and guides entrepreneur/founder NIW petitions using the USCIS Policy Manual's entrepreneur-specific framework (Jan 2025 update) |

> **Got a weak research profile?** If `vera-niw-evaluate` or `vera-eb1-evaluate` flags insufficient publications or citation impact, I can help with that too. Check out [**ai-research-pipeline**](https://github.com/VeraSuperHub/ai-research-pipeline) and [**stat-research-pipeline**](https://github.com/VeraSuperHub/stat-research-pipeline) — my other skill suites that take a research question and dataset to a publication-ready manuscript, end-to-end.

### EB-1 ([`vera-eb1.plugin`](vera-eb1.plugin) / [`vera-eb1-skillset/`](vera-eb1-skillset/))

| # | Skill | What It Does |
|---|-------|-------------|
| 1 | `vera-eb1-evaluate` | Reviews evidence for EB-1A and EB-1B pathways, maps materials to relevant criteria, and produces an evidence-readiness and gap summary |
| 2 | `vera-eb1-authorship` | Criterion 6: authorship of scholarly articles with venue rankings and citation impact analysis |
| 3 | `vera-eb1-original-contributions` | Criterion 5: original contributions of major significance with before/after framing |
| 4 | `vera-eb1-judging` | Criterion 4: evidence of judging the work of others (peer review, panels, editorial boards) |
| 5 | `vera-eb1-critical-role` | Criterion 8: leading or critical role in distinguished organizations |
| 6 | `vera-eb1-published-material` | Criterion 3: published material about the petitioner in professional or major media |
| 7 | `vera-eb1-recommendation` | Generates EB-1 reference letters from a recommender's perspective |
| 8 | `vera-eb1-final-merits` | Kazarian Step 2: final-merits argument drafting support — organizes sustained-acclaim evidence, criteria-level outputs, impact signals, and narrative risks for human review |
| 9 | `vera-eb1-assemble` | Assembles a review-ready EB-1 petition-letter draft as a formatted .docx |
| 10 | `vera-eb1-pl-review` | Adversarial pre-filing review using the Kazarian two-step analytical framework |
| 11 | `vera-eb1-rfe-response` | Drafts a structured EB-1 RFE response framework with evidence mapping and potential rebuttal patterns for human review |

**Total: 19 skills across both petition categories.**

> **Got a weak research profile?** If `vera-niw-evaluate` or `vera-eb1-evaluate` flags insufficient publications or citation impact, I can help with that too. Check out [**ai-research-pipeline**](https://github.com/VeraSuperHub/ai-research-pipeline) and [**stat-research-pipeline**](https://github.com/VeraSuperHub/stat-research-pipeline) — my other skill suites that take a research question and dataset to a publication-ready manuscript, end-to-end.

---

## Tools

In addition to skills, this suite includes standalone tools that feed data into the pipeline:

| Tool | What It Does | Used By |
|---|---|---|
| [`GoogleScholar`](GoogleScholar/) | Extracts citation metrics, publication lists, and h-index from Google Scholar (Python + Colab notebook) | `vera-niw-assemble` (Section 3: Academic Credentials) |

---

## Quick Start

### Requirements

- [Claude Pro, Max, Team, or Enterprise](https://claude.ai/upgrade) subscription
- Code execution enabled (Settings → Capabilities)

### Installation

There are two ways to install: **plugins** (for Claude Code) and **individual skills** (for claude.ai).

#### Option A — Plugin (Claude Code / CLI)

Plugins bundle all skills for a petition type into a single file. Install via double-click or terminal:

```bash
# Clone the repo
git clone https://github.com/VeraSuperHub/vera-eb-suite.git
cd vera-eb-suite

# Install the plugin(s) you need
claude plugin install vera-niw.plugin
claude plugin install vera-eb1.plugin
```

If the `.plugin` file extension is not recognized on your system, rename it to `.zip` before installing:

```bash
cp vera-niw.plugin vera-niw.zip
claude plugin install vera-niw.zip
```

#### Option B — Individual Skills (claude.ai)

For use on [claude.ai](https://claude.ai), install skills one at a time:

1. Download the `.skill` file(s) you need from [`vera-niw-skillset/`](vera-niw-skillset/) or [`vera-eb1-skillset/`](vera-eb1-skillset/)
2. Go to [Settings → Capabilities](https://claude.ai/settings/capabilities)
3. Scroll to the **Skills** section
4. Click **"Upload skill"**
5. Upload the `.skill` file and toggle it **on**

Claude will automatically invoke the skill when your request matches its description — no manual activation needed.

**Install one skill at a time.** For the full NIW pipeline, install all 8. For EB-1, install all 11.

### Google Scholar Tool Setup

The `GoogleScholar/` directory contains a Python scraper for extracting citation metrics. You can run it locally or via Google Colab:

```bash
cd GoogleScholar
pip install requests beautifulsoup4 pandas numpy
python -c "from scholar import get_profile; print(get_profile('YOUR_SCHOLAR_ID'))"
```

Or open `scholar_colab_demo.ipynb` in [Google Colab](https://colab.research.google.com) for interactive use.

### Recommended Workflow

Start with **Evaluate** to get your evidence-readiness summary. If the readiness tier is STRONG_EVIDENCE or WORKABLE_EVIDENCE, proceed through the pipeline in order:

**NIW:**
```
Evaluate → Endeavor → Pillar (×3) → Recommendation (×N) → Assemble → PL Review
```

Each skill's output is designed as input for the next skill in the pipeline. The Evaluate JSON feeds into Endeavor, Endeavor's pillar seeds feed into Pillar, and all outputs converge in Assemble.

**EB-1:**
```
Evaluate → Criterion Skills (select based on your evidence) → Recommendation (×N) + Final Merits → Assemble → PL Review
```

The Evaluate skill determines EB-1A vs EB-1B and identifies which criteria your evidence supports. Run the relevant criterion skills, then generate recommendation letters and the final merits argument before assembling the petition.

---

## Usage Examples

**Evaluate — How strong is my evidence?**
```
I'm a senior data scientist at a Fortune 500 company with 5 years of experience.
I have 3 publications (12 citations total), 2 patents pending, and my fraud
detection system processes 2M+ transactions daily. Review my NIW evidence
readiness.
```

**Endeavor — Define the proposed endeavor:**
```
I just completed vera-niw-evaluate and got a WORKABLE_EVIDENCE readiness tier.
Here's my JSON output:
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

The key insight: many parts of evidence preparation are pattern-based. Public decisions, policy guidance, and real petition workflows reveal recurring structures: what evidence tends to be persuasive, where gaps commonly appear, how narratives are organized, and how weaknesses are stress-tested before filing. These repeatable components can be decomposed, encoded, validated, and improved by the community — while case-specific legal judgment remains a human professional responsibility.

---

## Repo Structure

```
vera-eb-suite/
├── README.md
├── LICENSE                            (GPL-3.0)
├── DISCLAIMER.md                      (legal disclaimer)
├── CONTRIBUTING.md                    (contribution guidelines)
├── CHANGELOG.md                       (version history)
│
├── vera-niw-skillset/                 ← NIW skills (8 .skill files)
│   ├── vera-niw-evaluate.skill
│   ├── vera-niw-endeavor.skill
│   ├── vera-niw-pillar.skill
│   ├── vera-niw-recommendation.skill
│   ├── vera-niw-assemble.skill
│   ├── vera-niw-pl-review.skill
│   ├── vera-niw-rfe-response.skill
│   └── vera-niw-entrepreneur.skill
│
├── vera-eb1-skillset/                 ← EB-1 skills (11 .skill files)
│   ├── vera-eb1-evaluate.skill
│   ├── vera-eb1-authorship.skill
│   ├── vera-eb1-original-contributions.skill
│   ├── vera-eb1-judging.skill
│   ├── vera-eb1-critical-role.skill
│   ├── vera-eb1-published-material.skill
│   ├── vera-eb1-recommendation.skill
│   ├── vera-eb1-final-merits.skill
│   ├── vera-eb1-assemble.skill
│   ├── vera-eb1-pl-review.skill
│   └── vera-eb1-rfe-response.skill
│
├── vera-niw.plugin                    ← Bundled NIW plugin
├── vera-eb1.plugin                    ← Bundled EB-1 plugin
│
└── GoogleScholar/                     ← Citation data tool
    ├── scholar.py
    ├── scholar_colab_demo.ipynb
    └── requirements.txt
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
Generic prompts produce generic output. Each skill here encodes hundreds of specific decision rules — failure pattern detection, field-specific framing, USCIS-language calibration — derived from systematic analysis of AAO decisions. The difference is the same as between a generic prompt and a structured workflow: the skills include explicit rubrics, schemas, failure-pattern checks, and evidence-mapping steps that make the output easier to review, test, and improve.

**Can I use this with GPT-4 or other models?**
The skills are optimized for Claude but the instructions are model-agnostic text. They may work with other capable models, though output quality may vary.

**Can I contribute?**
Yes. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for details. Especially valuable:

- **Bug reports** — Skill produced incorrect or misleading guidance? Open an issue.
- **Test cases** — Real RFE patterns or edge cases for `evals/`. Anonymize all personal information.
- **Reference materials** — New AAO decisions, policy updates, or adjudication trend data.
- **Skill improvements** — Better rubrics, additional failure patterns, improved prompts.

---

## Disclaimer

These tools are for **informational and educational purposes only**. They do not constitute legal advice and do not create an attorney-client relationship. See [DISCLAIMER.md](DISCLAIMER.md) for full terms.

---

## License

GPL-3.0 License. See [LICENSE](LICENSE).
