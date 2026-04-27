# Contributing to NIW Skill Suite

Thanks for your interest in improving NIW petition guidance for everyone.

## How to Contribute

### Bug Reports

If a skill produced incorrect or misleading guidance, open an issue with:

1. Which skill was involved
2. The type of input you provided (anonymize all personal information)
3. What the skill produced
4. What you expected instead
5. Why the output is incorrect (cite AAO decisions or USCIS policy if possible)

### Test Cases

Adding eval test cases is one of the most valuable contributions. Each skill has an `evals/evals.json` file. Good test cases:

- Cover edge cases not already tested
- Include real RFE patterns (anonymized)
- Test failure mode detection (not just happy paths)
- Include expected evidence-readiness summaries / assessments with reasoning

**Critical: Anonymize all personal information.** Change names, institutions, specific dates, and any identifying details. The test case should preserve the pattern, not the person.

### Reference Materials

- New AAO decisions that establish or modify adjudication patterns
- USCIS Policy Manual updates
- Adjudication trend data (approval rates, RFE patterns)
- Field-specific framing examples

### Skill Improvements

- Better rubrics or scoring criteria
- Additional denial/failure patterns
- Improved prompt engineering for more reliable output
- Bug fixes in decision logic

## Skill Architecture

Each skill follows this structure:

```
vera-niw-{name}/
├── SKILL.md          # The skill instructions (this IS the skill)
├── README.md         # Documentation for humans
├── evals/
│   └── evals.json    # Test cases
├── schema/           # (optional) JSON output schemas
├── rubric/           # (optional) Scoring rubrics
├── references/       # (optional) Reference documents loaded by SKILL.md
└── examples/         # (optional) Example outputs
```

The `SKILL.md` file is what Claude executes. Everything else supports it.

## Guidelines

- **Keep skills standalone.** Each skill folder should work independently when uploaded as a ZIP to Claude. Don't create cross-skill dependencies on shared files.
- **Be conservative.** Immigration is high-stakes. When in doubt, flag a weakness rather than miss it. A false positive costs the petitioner time; a false negative costs them their case.
- **Cite sources.** Reference specific AAO decisions, USCIS Policy Manual sections, or adjudication data when adding new patterns or rules.
- **Test your changes.** Run the skill against the existing eval cases and add new ones for your changes.
- **Don't break the pipeline.** Skills consume each other's output. If you change an output format, check downstream skills.

## Pull Request Process

1. Fork the repo
2. Create a branch for your change
3. Make your changes
4. Run eval test cases if applicable
5. Submit a PR with a clear description of what changed and why

## Legal

By contributing, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE).

Do not include any content that constitutes legal advice. All contributions must be consistent with the project's [DISCLAIMER.md](DISCLAIMER.md).
