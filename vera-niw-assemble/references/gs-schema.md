# Google Scholar Data Schema

*Status: PLACEHOLDER — update field names when Jupyter notebook is provided.*

This file defines the expected structure of the two GS output files from the
Python notebook. When the notebook arrives, update the field names below to
match actual output. The skill logic does not change — only the field mapping.

---

## File 1: JSON Summary (gs_summary.json)

Expected top-level fields:

```json
{
  "scholar_id": "string — Google Scholar user ID",
  "name": "string — petitioner name as shown on Scholar",
  "total_citations": 0,
  "citations_last_5_years": 0,
  "h_index": 0,
  "h_index_last_5_years": 0,
  "i10_index": 0,
  "i10_index_last_5_years": 0,
  "papers": [
    {
      "title": "string",
      "venue": "string — journal or conference name",
      "year": 0,
      "citation_count": 0,
      "is_first_authored": true,
      "co_authors": ["name1", "name2"],
      "scholar_url": "string",
      "indexed_in": ["Scopus", "ISI", "PubMed"]
    }
  ],
  "notable_citers": [
    {
      "citing_paper_title": "string",
      "citing_author": "string",
      "citing_institution": "string",
      "is_government": false,
      "is_industry": false,
      "citation_year": 0
    }
  ]
}
```

**Placeholder field names — update when notebook arrives.**
If the notebook uses different names (e.g., `citations_total` instead of
`total_citations`), update the names in this file. The SKILL.md references
these names for parsing — change here, skill behavior updates automatically.

---

## File 2: CSV Papers Table (gs_papers.csv)

Expected columns:

| Column | Type | Notes |
|---|---|---|
| `title` | string | Full paper title |
| `venue` | string | Journal or conference name |
| `year` | integer | Publication year |
| `citation_count` | integer | Total citations |
| `is_first_authored` | boolean | True if petitioner is first author |
| `indexed` | string | Comma-separated index names |

**Sort order:** The notebook may sort by citation count descending already.
If not, NIW_Assemble will sort before building the publications table.

---

## Integration Notes

**When the notebook arrives:**
1. Run the notebook on the petitioner's Google Scholar profile
2. Save outputs as `gs_summary.json` and `gs_papers.csv`
3. Provide both files to NIW_Assemble along with the other upstream outputs
4. If field names differ from above: update this file, not SKILL.md

**What NIW_Assemble does with GS data:**
- `total_citations`, `h_index`, `i10_index` → credentials block opening paragraph
- `papers` array → publications table (Section 3), sorted by citation_count
- `is_first_authored` → "First author" label in publications table Role column
- `indexed_in` → Pattern D check — unverified journals flagged
- `notable_citers` where `is_government=true` → flagged as Prong 2 evidence

**What NIW_Assemble does NOT do with GS data:**
- Does not verify citation counts independently
- Does not access Google Scholar directly — all data comes from the notebook
- Does not flag self-citations (notebook should handle this upstream)

---

## Pattern D Journal Check

For each paper in `papers`, if `indexed_in` is empty or contains only
unrecognized values, add this note in the credentials section:

```
[NOTE: "[journal name]" — indexing status unconfirmed by GS notebook.
Verify against ISI Web of Science, Scopus, or PubMed before filing.
USCIS may scrutinize publications not indexed in recognized databases.]
```

Do not silently include unverified journals in the credentials section.
