# Changelog

All notable changes to the Vera EB Suite (EB-1 + EB-2 NIW skills) will be documented in this file.

## [2.1.0] - 2026-05-16

### Added
- Strategic Navigation 2026 references for both NIW and EB-1 skill families, distilled from the `Strategic Navigation of EB2 NIW and EB1A Immigration Trends` notebook and constrained to filing-facing use through USCIS/legal source discipline.
- Codex installation guidance for extracting `.skill` archives into local `SKILL.md` folders.

### Changed
- Updated NIW and EB-1 skills to emphasize officer-friendly evidence navigation, document-dump prevention, NIW ripple-effect chains, EB-1 final-merits synthesis, independent recognition, and RFE response triage.
- Rebuilt all `.skill` archives as self-contained packages with shared references and family docs included inside each skill folder.
- Updated public docs from Claude-only framing to Claude Code and Codex-compatible skill usage.

### Fixed
- Corrected several stale relative-reference paths in source and packaged skill files.

## [2.0.0] - 2026-03-08

### Added
- **vera-niw-entrepreneur** — New skill for entrepreneur/founder NIW petitions using USCIS Policy Manual's entrepreneur-specific framework (Jan 2025 update)
- **GoogleScholar tool** — Python scraper (`scholar.py`) + Colab notebook for extracting citation metrics, publication lists, h-index, and co-author networks
- EB-1A standard misapplication detection (Pattern J) across evaluate, pillar, pl-review, and rfe-response
- Implementation vs. Innovation pattern (Pattern I) as standalone denial ground
- U.S. operational presence / letters of interest evidence category (Ingredient 7 in endeavor)
- Recommendation letter authenticity checklist (font consistency, no regulatory parroting)
- Government Agency Letter type (Type G) in vera-niw-recommendation
- Jan 2025 USCIS Policy Manual updates: occupation-level EB-2 gate, experience-specialty match
- FY 2024 public adjudication trend context (NIW approval-rate background 79.99% → 43.31%) used as conservative framing for evidence-readiness summaries; not used for approval-probability prediction
- Standalone deployable prompt for vera-niw-pl-review (works with any LLM API)
- 31 eval test cases across all 8 skills

### Changed
- All skills updated to v2.0 with March 2026 adjudication trend data
- Evidence scoring calibrated to post-2024 approval rate environment
- Publication due diligence framework expanded to 5-step audit (D-1 through D-5)
- Prong 3 elevated from formality to standalone RFE trigger
- Recommendation letter independence standards tightened

## [1.0.0] - Initial Release

### Added
- Core 7-skill pipeline: evaluate → endeavor → pillar → recommendation → assemble → pl-review → rfe-response
- Dhanasar framework implementation across all skills
- Field alignment rubric (3-tier system)
- 10 denial pattern checks (A–J) in pl-review
- 8 rebuttal patterns (R1–R8) in rfe-response
- Output schemas for evaluate and pillar
- Example outputs for evaluate (strong / workable / thin / very-thin evidence-readiness summaries)
