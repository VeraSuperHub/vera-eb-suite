# Google Scholar Data Schema

*Updated to match `GoogleScholar/scholar.py` output fields.*

This file defines the expected structure of the Google Scholar data files
used by vera-niw-assemble. Field names match the output of `scholar.py`.

---

## Profile Data (`get_profile()` output)

```json
{
  "id": "string — Google Scholar user ID",
  "name": "string — petitioner name as shown on Scholar",
  "affiliation": "string — current affiliation",
  "total_cites": 0,
  "h_index": 0,
  "i10_index": 0,
  "fields": ["string — research interest areas"],
  "homepage": "string — URL",
  "coauthors": [
    {
      "name": "string",
      "url": "string",
      "id": "string — coauthor Scholar ID"
    }
  ]
}
```

---

## Publications Data (`get_publications()` output — DataFrame)

| Column | Type | Notes |
|---|---|---|
| `title` | string | Full paper title |
| `author` | string | Author list as shown on Scholar |
| `journal` | string | Journal or conference name (parsed from details) |
| `number` | string | Volume/issue/page info |
| `cites` | integer | Total citation count |
| `year` | integer or null | Publication year |
| `cid` | string | Citation cluster ID (for linking to citing papers) |
| `pubid` | string | Publication ID (for detail page lookups) |

**Sort order:** Sorted by citation count descending by default (when `sortby="citation"`).
Can also sort by year with `sortby="year"`.

---

## Citation History (`get_citation_history()` output — DataFrame)

| Column | Type | Notes |
|---|---|---|
| `year` | integer | Calendar year |
| `cites` | integer | Citations received that year |

Covers approximately the past 12 years of citation data.

---

## Per-Article Citation History (`get_article_cite_history()` output — DataFrame)

| Column | Type | Notes |
|---|---|---|
| `year` | integer | Calendar year |
| `cites` | integer | Citations received that year |
| `pubid` | string | Publication ID |

---

## Integration with vera-niw-assemble

**How to provide GS data to NIW_Assemble:**

1. Run `scholar.py` functions on the petitioner's Google Scholar profile
2. Save profile as JSON, publications as CSV
3. Provide both to NIW_Assemble along with other upstream outputs

**What NIW_Assemble does with GS data:**
- `total_cites`, `h_index`, `i10_index` → credentials block opening paragraph
- Publications DataFrame → publications table (Section 3), sorted by `cites`
- `author` field → authorship position analysis (first author detection)
- `journal` field → Pattern D venue quality check — unverified journals flagged
- Citation history → trajectory analysis for Prong 2

**What NIW_Assemble does NOT do with GS data:**
- Does not verify citation counts independently
- Does not access Google Scholar directly — all data comes from the scraper
- Does not flag self-citations (handle this upstream if needed)

---

## Pattern D Journal Check

For each paper in publications, if the journal name is not recognized as a
Tier 1 or Tier 2 venue (per the pub-diligence framework), add this note
in the credentials section:

```
[NOTE: "[journal name]" — indexing status unconfirmed.
Verify against ISI Web of Science, Scopus, or PubMed before filing.
USCIS may scrutinize publications not indexed in recognized databases.]
```

Do not silently include unverified journals in the credentials section.

---

## Additional Helper Functions

The `scholar.py` module also provides:

| Function | Returns | Use Case |
|---|---|---|
| `get_publication_abstract(id, pubid)` | string | Extract abstract for exhibit preparation |
| `get_complete_authors(id, pubid)` | string | Full author list (not truncated) |
| `author_position(author_lists, name)` | DataFrame | First/middle/last author analysis |
| `predict_h_index(id)` | DataFrame | 10-year h-index projection (Acuna et al.) |
| `get_coauthors(id)` | DataFrame | Co-author network for independence analysis |
| `compare_scholars(ids)` | DataFrame | Benchmark against peers in field |
