"""
scholar.py — Python port of the R `scholar` package (jkeirstead/scholar).

Provides functions to extract citation data from Google Scholar, compare
multiple scholars, predict future h-index values, and analyse co-author
networks.

Requirements:
    pip install requests beautifulsoup4 pandas numpy

Optional (for co-author network plotting):
    pip install networkx matplotlib

Usage:
    from scholar import get_profile, get_publications, get_citation_history, ...

    profile = get_profile("B7vSqZsAAAAJ")
    pubs = get_publications("B7vSqZsAAAAJ")
"""

from __future__ import annotations

import re
import time
import warnings
from typing import Optional
from functools import lru_cache

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_SCHOLAR_SITE = "https://scholar.google.com"
_SESSION: Optional[requests.Session] = None


def set_scholar_mirror(mirror: str) -> None:
    """Set a Google Scholar mirror URL."""
    global _SCHOLAR_SITE
    _SCHOLAR_SITE = mirror.rstrip("/")


def _get_session() -> requests.Session:
    """Return a shared requests session (cookie persistence)."""
    global _SESSION
    if _SESSION is None:
        _SESSION = requests.Session()
        _SESSION.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
            }
        )
    return _SESSION


# ---------------------------------------------------------------------------
# Low-level helpers  (mirrors R: utils.R)
# ---------------------------------------------------------------------------


def tidy_id(scholar_id: str) -> str:
    """Ensure a single, clean scholar ID."""
    if isinstance(scholar_id, (list, tuple)):
        if len(scholar_id) != 1:
            warnings.warn(
                f"Only one ID at a time; using first: {scholar_id[0]}"
            )
        scholar_id = scholar_id[0]
    # Strip common trailing fragments
    return scholar_id.split("&")[0].strip()


def get_scholar_resp(
    url: str, attempts_left: int = 5, delay: float = 1.0
) -> requests.Response:
    """GET a Google Scholar page with retries and rate-limit detection."""
    assert attempts_left > 0, "No attempts remaining"

    session = _get_session()
    resp = session.get(url, timeout=30)

    if resp.status_code == 200:
        return resp
    if resp.status_code == 429:
        raise RuntimeError(
            "HTTP 429 — Google is rate-limiting you. "
            "Wait a few minutes before retrying."
        )
    if attempts_left == 1:
        raise ConnectionError(
            f"Cannot connect to Google Scholar (HTTP {resp.status_code}). "
            "Is the ID correct?"
        )
    time.sleep(delay)
    return get_scholar_resp(url, attempts_left - 1, delay)


def _parse_html(url: str) -> BeautifulSoup:
    """Fetch URL and return a BeautifulSoup tree."""
    resp = get_scholar_resp(url)
    return BeautifulSoup(resp.text, "html.parser")


def _grab_id(url: str) -> Optional[str]:
    """Extract the scholar ID from a URL."""
    m = re.search(r"user=([A-Za-z0-9_-]+)", url or "")
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Profile  (mirrors R: get_profile, get_scholar_id)
# ---------------------------------------------------------------------------


def get_profile(scholar_id: str) -> dict:
    """
    Get profile information for a Google Scholar researcher.

    Returns a dict with: id, name, affiliation, total_cites, h_index,
    i10_index, fields, homepage, coauthors, available, not_available.
    """
    scholar_id = tidy_id(scholar_id)
    url = f"{_SCHOLAR_SITE}/citations?hl=en&user={scholar_id}"
    page = _parse_html(url)

    # Name
    name_el = page.select_one("#gsc_prf_in")
    name = name_el.text.strip() if name_el else ""

    # Affiliation
    bio_divs = page.select("div.gsc_prf_il")
    affiliation = bio_divs[0].text.strip() if bio_divs else ""

    # Research interests
    fields = [a.text.strip() for a in page.select("a.gsc_prf_inta")]

    # Homepage
    hp_el = page.select_one("#gsc_prf_ivh a")
    homepage = hp_el["href"] if hp_el else ""

    # Citation table
    stats = page.select("#gsc_rsb_st tr")
    total_cites = h_index = i10_index = 0
    for row in stats:
        cells = row.select("td")
        if len(cells) >= 2:
            label = cells[0].text.strip().lower()
            val = cells[1].text.strip()
            if "citations" in label:
                total_cites = int(val) if val.isdigit() else 0
            elif "h-index" in label:
                h_index = int(val) if val.isdigit() else 0
            elif "i10-index" in label:
                i10_index = int(val) if val.isdigit() else 0

    # Coauthors (listed on profile, up to 20)
    coauthors = []
    for a_tag in page.select("a[tabindex='-1']"):
        href = a_tag.get("href", "")
        coauthor_name = a_tag.text.strip()
        if coauthor_name and "Sort by" not in coauthor_name:
            coauthors.append(
                {"name": coauthor_name, "url": href, "id": _grab_id(href)}
            )

    # Availability metrics
    available = not_available = None
    avail_el = page.select_one("div.gsc_rsb_m_a")
    if avail_el:
        m = re.match(r"(\d+)", avail_el.text)
        available = int(m.group(1)) if m else None
    navail_el = page.select_one("div.gsc_rsb_m_na")
    if navail_el:
        m = re.match(r"(\d+)", navail_el.text)
        not_available = int(m.group(1)) if m else None

    return {
        "id": scholar_id,
        "name": name,
        "affiliation": affiliation,
        "total_cites": total_cites,
        "h_index": h_index,
        "i10_index": i10_index,
        "fields": fields,
        "homepage": homepage,
        "coauthors": coauthors,
        "available": available,
        "not_available": not_available,
    }


def get_scholar_id(
    last_name: str = "",
    first_name: str = "",
    affiliation: Optional[str] = None,
) -> Optional[str]:
    """
    Search for a Google Scholar ID by name (and optional affiliation).

    Returns the scholar ID string, or None if not found.
    """
    if not (first_name or last_name):
        raise ValueError("At least one of first_name / last_name is required.")

    query = f"{first_name}+{last_name}".strip("+")
    url = (
        f"{_SCHOLAR_SITE}/citations?view_op=search_authors"
        f"&mauthors={query}&hl=en&oi=ao"
    )
    resp = get_scholar_resp(url)
    ids = list(set(re.findall(r"user=([A-Za-z0-9_-]+)", resp.text)))

    if not ids:
        warnings.warn("No Scholar ID found.")
        return None

    if len(ids) == 1:
        return ids[0]

    # Multiple matches — use affiliation to disambiguate
    if affiliation is None:
        warnings.warn(
            f"Found {len(ids)} candidates; returning first: {ids[0]}"
        )
        return ids[0]

    for sid in ids:
        try:
            prof = get_profile(sid)
            if affiliation.lower() in prof["affiliation"].lower():
                return sid
        except Exception:
            continue

    warnings.warn("No researcher found at the indicated affiliation.")
    return None


# ---------------------------------------------------------------------------
# Publications  (mirrors R: publications.r)
# ---------------------------------------------------------------------------


def get_publications(
    scholar_id: str,
    cstart: int = 0,
    cstop: int = float("inf"),
    pagesize: int = 100,
    sortby: str = "citation",
) -> pd.DataFrame:
    """
    Get all publications for a scholar.

    Returns a DataFrame with columns: title, author, journal, number,
    cites, year, cid, pubid.
    """
    scholar_id = tidy_id(scholar_id)
    if pagesize > 100:
        warnings.warn("pagesize exceeds 100; capping at 100.")
        pagesize = 100

    assert sortby in ("citation", "year"), "sortby must be 'citation' or 'year'"

    sort_param = "&sortby=pubdate" if sortby == "year" else ""
    url = (
        f"{_SCHOLAR_SITE}/citations?hl=en&user={scholar_id}"
        f"&cstart={cstart}&pagesize={pagesize}{sort_param}"
    )
    page = _parse_html(url)
    rows = page.select("tr.gsc_a_tr")

    records = []
    for row in rows:
        # Title & pubid
        title_el = row.select_one(".gsc_a_at")
        title = title_el.text.strip() if title_el else ""
        pubid = ""
        if title_el and title_el.get("href"):
            m = re.search(r":(.+)$", title_el["href"])
            pubid = m.group(1) if m else ""

        # Citation count & cid
        cite_el = row.select_one(".gsc_a_ac")
        cites = 0
        cid = ""
        if cite_el:
            cites_text = cite_el.text.strip()
            cites = int(cites_text) if cites_text.isdigit() else 0
            href = cite_el.get("href", "")
            m = re.search(r"cites=(\d+)", href)
            cid = m.group(1) if m else ""

        # Year
        year_el = row.select_one(".gsc_a_y span")
        year_text = year_el.text.strip() if year_el else ""
        year = int(year_text) if year_text.isdigit() else None

        # Author & journal/details (two grey lines)
        grey = row.select("td .gs_gray")
        author = grey[0].text.strip() if len(grey) > 0 else ""
        details = grey[1].text.strip() if len(grey) > 1 else ""

        # Parse journal vs number from details
        first_digit = re.search(r"[\[\(]?\d", details)
        if first_digit:
            pos = first_digit.start()
            journal = details[:pos].strip().rstrip(",")
            number = (
                details[pos:].strip().rstrip(",").rstrip()
            )
            # Remove trailing year portion like ", 2019"
            number = re.sub(r",?\s*\d{4}\s*$", "", number).strip().rstrip(",")
        else:
            journal = details.rstrip(",").strip()
            number = ""

        records.append(
            {
                "title": title,
                "author": author,
                "journal": journal,
                "number": number,
                "cites": cites,
                "year": year,
                "cid": cid,
                "pubid": pubid,
            }
        )

    df = pd.DataFrame(records)

    # Paginate if needed
    if len(df) == pagesize and cstart + pagesize < cstop:
        more = get_publications(
            scholar_id,
            cstart=cstart + pagesize,
            cstop=cstop,
            pagesize=pagesize,
            sortby=sortby,
        )
        df = pd.concat([df, more], ignore_index=True)

    return df


def get_article_cite_history(
    scholar_id: str, article_pubid: str
) -> pd.DataFrame:
    """
    Get yearly citation history for a single article.

    Returns DataFrame with columns: year, cites, pubid.
    """
    scholar_id = tidy_id(scholar_id)
    url = (
        f"{_SCHOLAR_SITE}/citations?view_op=view_citation&hl=en"
        f"&citation_for_view={scholar_id}:{article_pubid}"
    )
    page = _parse_html(url)

    years, vals = [], []
    for a_tag in page.select(".gsc_oci_g_a"):
        href = a_tag.get("href", "")
        m = re.search(r"as_ylo=(\d{4})", href)
        if m:
            years.append(int(m.group(1)))
    for span in page.select(".gsc_oci_g_al"):
        vals.append(int(span.text.strip()))

    if not years:
        return pd.DataFrame(columns=["year", "cites", "pubid"])

    # Fill gaps
    full_years = list(range(min(years), max(years) + 1))
    cite_map = dict(zip(years, vals))
    df = pd.DataFrame(
        {
            "year": full_years,
            "cites": [cite_map.get(y, 0) for y in full_years],
            "pubid": article_pubid,
        }
    )
    return df


def get_num_articles(scholar_id: str) -> int:
    """Return the number of publications for a scholar."""
    return len(get_publications(scholar_id))


def get_oldest_article(scholar_id: str) -> Optional[int]:
    """Return the year of the oldest publication."""
    pubs = get_publications(scholar_id)
    years = pubs["year"].dropna()
    return int(years.min()) if len(years) > 0 else None


def get_num_distinct_journals(scholar_id: str) -> int:
    """Return the number of distinct journals a scholar has published in."""
    pubs = get_publications(scholar_id)
    return pubs["journal"].nunique()


def get_num_top_journals(
    scholar_id: str,
    journals: Optional[list[str]] = None,
) -> int:
    """
    Return number of publications in top journals.

    Default journal list follows Acuna et al. (Nature, Science,
    Nature Neuroscience, PNAS, Neuron).
    """
    if journals is None:
        journals = [
            "Nature",
            "Science",
            "Nature Neuroscience",
            "Proceedings of the National Academy of Sciences",
            "Neuron",
        ]
    pubs = get_publications(scholar_id)
    return int(pubs["journal"].isin(journals).sum())


# ---------------------------------------------------------------------------
# Publication details  (mirrors R: get_publication_*)
# ---------------------------------------------------------------------------


def _get_publication_page(scholar_id: str, pub_id: str) -> BeautifulSoup:
    """Fetch the detail page for a single publication."""
    scholar_id = tidy_id(scholar_id)
    url = (
        f"{_SCHOLAR_SITE}/citations?view_op=view_citation&hl=en"
        f"&user={scholar_id}&citation_for_view={scholar_id}:{pub_id}"
    )
    return _parse_html(url)


def get_publication_abstract(scholar_id: str, pub_id: str) -> str:
    """Return the abstract text for a publication."""
    page = _get_publication_page(scholar_id, pub_id)
    el = page.select_one("div.gsh_csp")
    return el.text.strip() if el else ""


def get_publication_url(scholar_id: str, pub_id: str) -> str:
    """Return the URL to the full publication."""
    page = _get_publication_page(scholar_id, pub_id)
    el = page.select_one("a.gsc_oci_title_link")
    return el["href"] if el else ""


def get_publication_date(scholar_id: str, pub_id: str) -> str:
    """Return the publication date string."""
    page = _get_publication_page(scholar_id, pub_id)
    fields = page.select("div.gsc_oci_field")
    values = page.select("div.gsc_oci_value")
    for f, v in zip(fields, values):
        if "publication date" in f.text.strip().lower():
            return v.text.strip()
    return ""


def get_publication_data_extended(scholar_id: str, pub_id: str) -> dict:
    """Return all metadata fields for a publication as a dict."""
    page = _get_publication_page(scholar_id, pub_id)
    fields = page.select("div.gsc_oci_field")
    values = page.select("div.gsc_oci_value")
    return {f.text.strip(): v.text.strip() for f, v in zip(fields, values)}


def get_article_scholar_url(scholar_id: str, pubid: str) -> str:
    """Return the Google Scholar URL for an article's detail page."""
    scholar_id = tidy_id(scholar_id)
    return (
        f"{_SCHOLAR_SITE}/citations?view_op=view_citation&hl=en"
        f"&user={scholar_id}&citation_for_view={scholar_id}:{pubid}"
    )


def get_complete_authors(
    scholar_id: str,
    pubid: str | list[str],
    delay: float = 0.4,
    initials: bool = True,
) -> str | list[str]:
    """
    Get the complete author list for one or more publications.

    Parameters
    ----------
    scholar_id : str
    pubid : str or list of str
    delay : float — average delay between requests (jittered ± 0.5s)
    initials : bool — abbreviate first/middle names

    Returns
    -------
    str or list of str
    """
    scholar_id = tidy_id(scholar_id)

    def _fetch_one(pid: str) -> str:
        url = (
            f"{_SCHOLAR_SITE}/citations?view_op=view_citation"
            f"&citation_for_view={scholar_id}:{pid}"
        )
        page = _parse_html(url)
        el = page.select_one(".gsc_oci_value")
        return el.text.strip() if el else ""

    def _to_initials(author_str: str) -> str:
        authors = [a.strip() for a in author_str.split(",")]
        formatted = []
        for author in authors:
            parts = author.split()
            if not parts:
                continue
            last = parts[-1]
            firsts = "".join(p[0] for p in parts[:-1] if p)
            formatted.append(f"{firsts} {last}".strip())
        return ", ".join(formatted)

    single = isinstance(pubid, str)
    pubids = [pubid] if single else list(pubid)

    if len(pubids) > 50:
        raise ValueError(
            "Requesting >50 publications risks Google blocking your IP."
        )

    results = []
    for i, pid in enumerate(pubids):
        if i > 0:
            jitter = max(0, delay + (np.random.random() - 0.5))
            time.sleep(jitter)
        text = _fetch_one(pid)
        results.append(_to_initials(text) if initials else text)

    return results[0] if single else results


# ---------------------------------------------------------------------------
# Citation history  (mirrors R: get_citation_history)
# ---------------------------------------------------------------------------


def get_citation_history(scholar_id: str) -> pd.DataFrame:
    """
    Get annual citation counts for a scholar (past ~12 years).

    Returns DataFrame with columns: year, cites.
    """
    scholar_id = tidy_id(scholar_id)
    url = (
        f"{_SCHOLAR_SITE}/citations?hl=en&user={scholar_id}"
        f"&pagesize=100&view_op=list_works"
    )
    page = _parse_html(url)

    years = [
        int(s.text) for s in page.select("span.gsc_g_t") if s.text.isdigit()
    ]
    vals = [
        int(s.text) for s in page.select("span.gsc_g_al") if s.text.isdigit()
    ]

    if len(years) > len(vals):
        # Some years have zero citations — use z-index to map
        style_tags = page.select("a.gsc_g_a")
        allvals = [0] * len(years)
        for tag in style_tags:
            style = tag.get("style", "")
            m = re.search(r"z-index:(\d+)", style)
            if m:
                z = int(m.group(1))
                al = tag.select_one(".gsc_g_al")
                if al and z <= len(allvals):
                    allvals[z - 1] = int(al.text)
        vals = list(reversed(allvals))

    # Truncate to same length
    n = min(len(years), len(vals))
    return pd.DataFrame({"year": years[:n], "cites": vals[:n]})


# ---------------------------------------------------------------------------
# Comparing scholars  (mirrors R: compare.r)
# ---------------------------------------------------------------------------


def compare_scholars(
    ids: list[str], pagesize: int = 100
) -> pd.DataFrame:
    """
    Compare citation records of multiple scholars.

    Returns DataFrame with: id, name, year, cites, total (cumulative).
    """
    frames = []
    names_map = {}
    for sid in ids:
        sid = tidy_id(sid)
        pubs = get_publications(sid, pagesize=pagesize)
        yearly = (
            pubs.dropna(subset=["year"])
            .groupby("year")["cites"]
            .sum()
            .reset_index()
        )
        yearly["id"] = sid
        yearly = yearly.sort_values("year")
        yearly["total"] = yearly["cites"].cumsum()
        frames.append(yearly)
        names_map[sid] = get_profile(sid)["name"]

    df = pd.concat(frames, ignore_index=True)
    df["name"] = df["id"].map(names_map)
    return df[["id", "name", "year", "cites", "total"]]


def compare_scholar_careers(
    ids: list[str], career: bool = True
) -> pd.DataFrame:
    """
    Compare citation careers of multiple scholars.

    If career=True, adds a career_year column relative to first citation year.
    Returns DataFrame with: id, name, year, cites, (career_year).
    """
    frames = []
    names_map = {}
    for sid in ids:
        sid = tidy_id(sid)
        hist = get_citation_history(sid)
        hist["id"] = sid
        if career and len(hist) > 0:
            hist["career_year"] = hist["year"] - hist["year"].min()
        frames.append(hist)
        names_map[sid] = get_profile(sid)["name"]

    df = pd.concat(frames, ignore_index=True)
    df["name"] = df["id"].map(names_map)
    cols = ["id", "name", "year", "cites"]
    if career:
        cols.append("career_year")
    return df[cols]


# ---------------------------------------------------------------------------
# Author position  (mirrors R: author_position)
# ---------------------------------------------------------------------------


def author_position(
    author_lists: list[str] | pd.Series, author_name: str
) -> pd.DataFrame:
    """
    Find the position of an author in each publication's author list.

    Parameters
    ----------
    author_lists : list of str — e.g. from get_publications()['author']
    author_name : str — the author to search for (matches on last name)

    Returns
    -------
    DataFrame with: authors, position (1-indexed), n_authors,
    position_normalized (0=first, 1=last, NaN if unknown).
    """
    last_name = author_name.strip().split()[-1].lower()

    records = []
    for authors_str in author_lists:
        parts = [a.strip() for a in str(authors_str).split(",")]
        lastnames = [p.split()[-1].lower() if p.split() else "" for p in parts]
        n = len(parts)
        has_ellipsis = any("..." in p for p in parts)

        matches = [
            i for i, ln in enumerate(lastnames) if last_name in ln
        ]
        if len(matches) == 1:
            pos = matches[0] + 1  # 1-indexed
            if has_ellipsis:
                norm = None
            elif n == 1:
                norm = 1.0
            else:
                norm = (pos - 1) / (n - 1)
            actual_n = None if has_ellipsis else n
        else:
            pos = None
            norm = None
            actual_n = None if has_ellipsis else n

        records.append(
            {
                "authors": authors_str,
                "position": pos,
                "n_authors": actual_n,
                "position_normalized": norm,
            }
        )

    return pd.DataFrame(records)


# ---------------------------------------------------------------------------
# Predict h-index  (mirrors R: predict.r)
# ---------------------------------------------------------------------------


def predict_h_index(
    scholar_id: str,
    journals: Optional[list[str]] = None,
) -> pd.DataFrame:
    """
    Predict future h-index using Acuna et al. (Nature 489, 201-202, 2012).

    Calibrated on neuroscience data — use with caution for other fields.

    Returns DataFrame with: years_ahead (0-10), h_index.
    """
    scholar_id = tidy_id(scholar_id)

    n = get_num_articles(scholar_id)
    prof = get_profile(scholar_id)
    h = prof["h_index"]
    import datetime

    current_year = datetime.datetime.now().year
    oldest = get_oldest_article(scholar_id)
    y = current_year - oldest if oldest else 0
    j = get_num_distinct_journals(scholar_id)
    q = get_num_top_journals(scholar_id, journals) if journals else get_num_top_journals(scholar_id)

    # Regression coefficients from Acuna et al.
    coefs = np.array(
        [
            [0.760, 0.373, 0.967, -0.069, 0.018, 0.033],
            [1.413, 0.781, 0.936, -0.132, 0.018, 0.064],
            [2.227, 1.105, 0.903, -0.193, 0.027, 0.096],
            [3.196, 1.386, 0.871, -0.274, 0.039, 0.145],
            [3.997, 1.578, 0.858, -0.345, 0.063, 0.198],
            [4.752, 1.671, 0.817, -0.377, 0.117, 0.282],
            [5.741, 1.761, 0.761, -0.420, 0.170, 0.394],
            [6.531, 1.796, 0.669, -0.420, 0.252, 0.508],
            [7.482, 1.653, 0.561, -0.415, 0.383, 0.629],
            [8.734, 1.326, 0.478, -0.411, 0.522, 0.823],
        ]
    )

    x = np.array([1.0, np.sqrt(n), h, y, j, q])
    h_pred = coefs @ x
    h_vals = np.concatenate([[h], h_pred])

    if any(np.diff(h_vals) < 0):
        warnings.warn(
            "Decreasing h-values predicted. "
            "Model calibrated on neuroscientists — results may not apply."
        )
    if any(h_vals < 0):
        warnings.warn("Negative h-values predicted. See above warning.")

    return pd.DataFrame(
        {"years_ahead": list(range(11)), "h_index": h_vals}
    )


# ---------------------------------------------------------------------------
# Co-authors & network  (mirrors R: coauthors.R)
# ---------------------------------------------------------------------------


def _list_coauthors(
    scholar_id: str, n_coauthors: int = 5
) -> pd.DataFrame:
    """List coauthors shown on a scholar's profile page."""
    scholar_id = tidy_id(scholar_id)
    if not scholar_id or scholar_id == "nan":
        return pd.DataFrame(
            columns=["author", "author_url", "coauthors", "coauthors_url"]
        )

    url = f"{_SCHOLAR_SITE}/citations?hl=en&user={scholar_id}"
    page = _parse_html(url)

    author_el = page.select_one("#gsc_prf_in")
    author_name = author_el.text.strip() if author_el else ""

    ca_links = page.select("a[tabindex='-1']")
    records = []
    for i, a_tag in enumerate(ca_links[:n_coauthors]):
        ca_name = a_tag.text.strip()
        ca_href = a_tag.get("href", "")
        if "Sort by" in ca_name:
            continue
        records.append(
            {
                "author": author_name,
                "author_url": url,
                "coauthors": ca_name,
                "coauthors_url": f"{_SCHOLAR_SITE}{ca_href}"
                if ca_href.startswith("/")
                else ca_href,
            }
        )

    return pd.DataFrame(records) if records else pd.DataFrame(
        columns=["author", "author_url", "coauthors", "coauthors_url"]
    )


def get_coauthors(
    scholar_id: str, n_coauthors: int = 5, n_deep: int = 1
) -> pd.DataFrame:
    """
    Get a network of co-authors.

    Parameters
    ----------
    scholar_id : str
    n_coauthors : int — how many coauthors to fetch per level
    n_deep : int — depth of network exploration (1 recommended)

    Returns
    -------
    DataFrame with columns: author, coauthors.
    """
    base = _list_coauthors(scholar_id, n_coauthors)
    if base.empty:
        return pd.DataFrame(columns=["author", "coauthors"])

    all_frames = [base]

    current_urls = base["coauthors_url"].tolist()
    for depth in range(n_deep):
        next_frames = []
        for ca_url in current_urls:
            ca_id = _grab_id(ca_url)
            if ca_id:
                try:
                    time.sleep(0.5)  # rate limit
                    sub = _list_coauthors(ca_id, n_coauthors)
                    next_frames.append(sub)
                except Exception:
                    continue
        if not next_frames:
            break
        depth_df = pd.concat(next_frames, ignore_index=True)
        all_frames.append(depth_df)
        current_urls = depth_df["coauthors_url"].tolist()

    result = pd.concat(all_frames, ignore_index=True)
    result = result[~result["coauthors"].str.contains("Sort by", na=False)]
    result["author"] = result["author"].str.title()
    result["coauthors"] = result["coauthors"].str.title()
    return result[["author", "coauthors"]].reset_index(drop=True)


def plot_coauthors(
    network: pd.DataFrame, size_labels: int = 10, figsize: tuple = (12, 8)
):
    """
    Plot a co-author network graph.

    Requires: pip install networkx matplotlib
    """
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.from_pandas_edgelist(network, "author", "coauthors")
    closeness = nx.closeness_centrality(G)

    pos = nx.spring_layout(G, k=2, seed=42)
    sizes = [closeness.get(n, 0.1) * 3000 for n in G.nodes()]

    fig, ax = plt.subplots(figsize=figsize)
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_size=sizes, alpha=0.5, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=size_labels, ax=ax)

    author_name = network["author"].iloc[0] if len(network) > 0 else "Unknown"
    ax.set_title(f"Co-authorship Network of {author_name}", fontsize=16)
    ax.axis("off")
    plt.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Journal ranking / impact factor stubs
# ---------------------------------------------------------------------------
# The R package ships bundled datasets (impactfactor, journalrankings)
# stored in sysdata.rda. We provide lookup via web search instead.


def get_impactfactor(journals: list[str]) -> pd.DataFrame:
    """
    Stub: The R package uses a bundled dataset for impact factor lookup.
    This Python version returns a placeholder DataFrame.

    For real data, consider using the `pybliometrics` or `scholarly` packages,
    or load the Scimago/JCR data yourself.
    """
    warnings.warn(
        "Impact factor data not bundled. Returning empty results. "
        "Consider loading Scimago/JCR data manually."
    )
    return pd.DataFrame({"journal": journals, "impact_factor": [None] * len(journals)})


def get_journalrank(journals: list[str]) -> pd.DataFrame:
    """
    Stub: The R package uses a bundled dataset for journal ranking lookup.
    See get_impactfactor() note.
    """
    warnings.warn(
        "Journal ranking data not bundled. Returning empty results. "
        "Consider loading Scimago/JCR data manually."
    )
    return pd.DataFrame({"journal": journals, "rank": [None] * len(journals)})


# ---------------------------------------------------------------------------
# Convenience: print summary
# ---------------------------------------------------------------------------


def scholar_summary(scholar_id: str) -> str:
    """Print a formatted summary of a scholar's profile."""
    prof = get_profile(scholar_id)
    lines = [
        f"Name:        {prof['name']}",
        f"Affiliation: {prof['affiliation']}",
        f"Scholar ID:  {prof['id']}",
        f"Total cites: {prof['total_cites']}",
        f"h-index:     {prof['h_index']}",
        f"i10-index:   {prof['i10_index']}",
        f"Fields:      {', '.join(prof['fields'])}",
        f"Homepage:    {prof['homepage']}",
        f"Coauthors:   {len(prof['coauthors'])}",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Module-level exports for convenient import
# ---------------------------------------------------------------------------
__all__ = [
    # Config
    "set_scholar_mirror",
    "tidy_id",
    "get_scholar_resp",
    # Profile
    "get_profile",
    "get_scholar_id",
    # Publications
    "get_publications",
    "get_article_cite_history",
    "get_num_articles",
    "get_oldest_article",
    "get_num_distinct_journals",
    "get_num_top_journals",
    # Publication details
    "get_publication_abstract",
    "get_publication_url",
    "get_publication_date",
    "get_publication_data_extended",
    "get_article_scholar_url",
    "get_complete_authors",
    # Citation history
    "get_citation_history",
    # Comparison
    "compare_scholars",
    "compare_scholar_careers",
    # Author analysis
    "author_position",
    # Prediction
    "predict_h_index",
    # Coauthors
    "get_coauthors",
    "plot_coauthors",
    # Journal metrics (stubs)
    "get_impactfactor",
    "get_journalrank",
    # Convenience
    "scholar_summary",
]
