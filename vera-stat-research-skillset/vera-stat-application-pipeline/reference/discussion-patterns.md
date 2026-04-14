# Discussion Section Patterns

Patterns for generating the Discussion section. The discussion is always generated NEW (not from analysis skill output) because it requires synthesis across all tracks and literature.

## Structure: 6-Paragraph Pattern

### Paragraph 1: Key Findings Summary

**Purpose**: Restate main results in plain language without statistics.

**Pattern**:
```
Our analysis of [N] [subjects/observations] revealed that [main finding 1].
[Main finding 2, if applicable]. These findings were consistent across
[multiple analytical approaches / regression, tree-based, and {alternative} methods],
strengthening confidence in the observed [associations/patterns/effects].
```

**Rules**:
- No p-values or test statistics in this paragraph
- Use "associated with" not "caused"
- Reference the research question explicitly
- Mention cross-method convergence if applicable

### Paragraphs 2-3: Comparison with Prior Work

**Purpose**: Situate findings within existing literature.

**Pattern for agreement**:
```
Our finding that [X] is consistent with [Author (Year)], who reported [similar finding]
in a [study description]. Similarly, [Author (Year)] found [related result] using
[their methods], suggesting [broader pattern].
```

**Pattern for disagreement**:
```
In contrast to [Author (Year)], who found [different result], our analysis suggests
[our finding]. This discrepancy may reflect [difference in population / methods /
time period / sample size / measurement approach].
```

**Pattern for extension**:
```
While [Author (Year)] demonstrated [their finding] using [their method], our
multi-method approach extends this by revealing [new insight from QR/trees/etc.].
Specifically, [quantile regression / tree-based analysis] showed [pattern not
visible in standard regression], suggesting [interpretation].
```

**Rules**:
- Compare with at least 3 prior studies from literature_review.md
- Always explain WHY results might differ (don't just state disagreement)
- Highlight what our multi-method approach adds beyond prior single-method studies
- Draw from `output/literature_review.md` for citations and prior findings

### Paragraph 4: Methodological Strengths

**Purpose**: Articulate the value of the analytical approach.

**Pattern**:
```
A strength of this analysis is the multi-method approach. [Regression method]
provided [specific insight — direction, magnitude, significance of predictors].
[Alternative method, e.g., quantile regression] revealed [what it uniquely showed —
e.g., that effects varied across the outcome distribution]. [Tree-based methods]
identified [nonlinear patterns / interactions / importance rankings] that complement
the parametric results. The convergence of [key finding] across all methods
strengthens confidence that this [association/pattern] is robust to analytical choices.
```

**Rules**:
- Name each method family and its unique contribution
- Reference the unified importance table if applicable
- Use "complement" and "converge" language — methods are lenses, not competitors
- If a method disagreed with others, frame it as revealing complexity, not contradiction

### Paragraph 5: Limitations

**Purpose**: Honest accounting of study weaknesses.

**Minimum 3 limitations**. Select from these categories:

| Category | Example Limitation |
|----------|-------------------|
| Sample | "The sample size of N={X} may limit power to detect small effects, particularly in subgroup analyses" |
| Design | "The cross-sectional design precludes causal inference; associations observed may not reflect causal relationships" |
| Measurement | "Self-reported [variable] may be subject to recall bias or social desirability" |
| Missing data | "Missing data ({X}% overall) were handled by [complete case / imputation], which assumes [MCAR / MAR]" |
| Confounding | "Unmeasured confounders such as [plausible confounder] may account for some of the observed association" |
| Generalizability | "These findings may not generalize to [other population] given the [sample characteristics]" |
| Exploratory | "Tree-based results should be interpreted as exploratory given the sample size; predictive validity was not assessed" |
| Multiple comparisons | "Multiple comparisons across [N] tests increase the risk of false positives; results should be interpreted in the context of the overall pattern" |

**Rules**:
- Be specific — "sample size of 245" not "small sample size"
- State the implication of each limitation — how could it affect conclusions?
- Do NOT propose solutions (that goes in Future Directions)
- If tree-based methods were used on small N, always include the exploratory caveat

### Paragraph 6: Implications & Future Directions

**Purpose**: What the findings mean and what comes next.

**Pattern**:
```
These findings have [practical/clinical/policy] implications. [Specific implication 1 —
what should practitioners/policymakers do with this information]. [Specific implication 2
if applicable].

Future research should [direction 1 — e.g., replicate with larger/different sample].
Additionally, [direction 2 — e.g., longitudinal design to assess causality].
[Direction 3 — e.g., investigate the nonlinear pattern identified by tree-based methods
using targeted study designs].
```

**Rules**:
- At least 1 practical implication
- At least 2 future directions
- Future directions should address the limitations identified above
- If tree-based methods found interesting patterns, suggest confirmatory follow-up
- End on a constructive note (what can be done), not a cautionary one

---

## Tone Rules

| Do | Don't |
|----|-------|
| "was associated with" | "caused", "led to", "resulted in" |
| "suggests" | "proves", "demonstrates conclusively" |
| "may indicate" | "clearly shows" |
| "exploratory analysis revealed" | "machine learning predicted" (unless N is large and validated) |
| "consistent with prior work" | "confirms the theory" |
| "these findings" | "our groundbreaking/novel/innovative results" |
| Name the specific method | "advanced statistical techniques" |
| "not statistically significant" | "no effect", "no relationship" |

## Cross-Method Synthesis Phrasing

Use these patterns in Paragraphs 1 and 4 to describe cross-method convergence:

- "The [association/pattern] was evident across all analytical approaches, from [parametric regression] to [tree-based methods], suggesting robustness to model specification."
- "While [regression] quantified the magnitude of the association (β = X, 95% CI: [Y, Z]), [tree-based methods] confirmed [predictor] as the most important variable, and [quantile regression] showed the effect was [strongest at the lower/upper tail]."
- "The agreement between [method 1] and [method 2] on [finding] strengthens the evidence, while [method 3] uniquely revealed [additional insight]."
