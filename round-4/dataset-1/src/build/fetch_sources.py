#!/usr/bin/env python3
"""Fetch & CACHE raw source documents into raw/ (the only network step).

Architecture: this script performs ALL network I/O and writes verbatim raw
responses (HTML / JSON / XML) under raw/. The build_*.py scripts then parse
ONLY from raw/ with no network, so dataset regeneration is deterministic.

Sources:
  - GDPR (regulatory, EU)  : gdpr-info.eu per-article HTML (verbatim official
                             GDPR text; legal source EUR-Lex CELEX:32016R0679).
  - Wikinews (news)        : en.wikinews.org MediaWiki API plaintext extracts
                             (CC BY 2.5).
  - eCFR (regulatory, US)  : ecfr.gov versioner API section XML (US Gov, public
                             domain).
CUAD (legal) is already cached at raw/cuad_data/CUADv1.json (CC BY 4.0).

iter_4 SCALE-UP: this fetch caches a much LARGER candidate pool so the build can
select ~24-32 documents per genre. Only NEW (uncached) files are fetched; the
iter_2 snapshot is reused verbatim. Wikinews article fetching is parallelised
with a small thread pool (each request still pulls ONE title -- MediaWiki forces
exlimit=1 for whole-article plaintext extracts) and a polite UA + retries.
"""
from __future__ import annotations
import sys, json, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from loguru import logger
import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
UA = {"User-Agent": "AII-research-dataset-builder/1.0 (academic; contact subscriptions-ai-claude1@ijs.si)"}

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(ROOT / "logs" / "fetch.log"), rotation="20 MB", level="DEBUG")


@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=2, max=20),
       retry=retry_if_exception_type((requests.RequestException,)))
def _get(url: str, params: dict | None = None, timeout: int = 40) -> requests.Response:
    r = requests.get(url, params=params, headers=UA, timeout=timeout)
    r.raise_for_status()
    return r


# --------------------------------------------------------------------------- GDPR
# A broad spread of GDPR articles (iter_4): definitions (4), principles (5-11),
# the data-subject rights (12-22), controller/processor duties (24-36), breach
# notice (33-34), international transfers (44-49), and remedies/liability
# (77-82). The build filters to the 1150-3550 char band and deepens gold recall.
GDPR_ARTICLES = [4, 5, 6, 7, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                 24, 25, 26, 28, 30, 32, 33, 34, 35, 36,
                 44, 45, 46, 47, 48, 49,
                 77, 78, 79, 82]


def fetch_gdpr() -> None:
    out = RAW / "gdpr"
    out.mkdir(parents=True, exist_ok=True)
    for n in GDPR_ARTICLES:
        dest = out / f"art-{n}.html"
        if dest.exists() and dest.stat().st_size > 2000:
            logger.info(f"GDPR art-{n}: cached")
            continue
        url = f"https://gdpr-info.eu/art-{n}-gdpr/"
        try:
            r = _get(url)
            dest.write_text(r.text, encoding="utf-8")
            logger.info(f"GDPR art-{n}: {len(r.text)} bytes")
            time.sleep(0.6)
        except Exception as e:
            logger.error(f"GDPR art-{n} failed: {e}")


# ----------------------------------------------------------------------- Wikinews
WN_API = "https://en.wikinews.org/w/api.php"


def _fetch_wikinews_article(idx: int, title: str, out: Path) -> str | None:
    """Fetch ONE Wikinews article's whole-article plaintext extract -> cache file.
    Returns the title on a fresh fetch, None if already cached."""
    dest = out / f"article_{idx:04d}.json"
    if dest.exists():
        return None
    params = {
        "action": "query", "format": "json", "titles": title,
        "prop": "extracts|info|revisions",
        "explaintext": "1", "exsectionformat": "plain",
        "inprop": "url", "rvprop": "ids|timestamp",
    }
    r = _get(WN_API, params=params)
    dest.write_text(r.text, encoding="utf-8")
    return title


def fetch_wikinews(target_titles: int = 800, n_fetch: int = 800,
                   workers: int = 6) -> None:
    out = RAW / "wikinews"
    out.mkdir(parents=True, exist_ok=True)
    # 1) collect a stable, deterministic list of mainspace, non-redirect article
    #    titles (alphabetical from "A"). Re-fetched fresh each run for a stable
    #    ordering; the per-title extract files are the cached snapshot.
    titles: list[str] = []
    apcontinue = None
    page_i = 0
    while len(titles) < target_titles and page_i < 12:
        params = {
            "action": "query", "format": "json", "list": "allpages",
            "apnamespace": "0", "aplimit": "500", "apfilterredir": "nonredirects",
            "apfrom": "A",
        }
        if apcontinue:
            params["apcontinue"] = apcontinue
        r = _get(WN_API, params=params)
        j = r.json()
        (out / f"allpages_{page_i}.json").write_text(json.dumps(j), encoding="utf-8")
        batch = [p["title"] for p in j["query"]["allpages"]]
        titles.extend(batch)
        logger.info(f"Wikinews allpages page {page_i}: +{len(batch)} (total {len(titles)})")
        if "continue" in j:
            apcontinue = j["continue"]["apcontinue"]
            page_i += 1
            time.sleep(0.4)
        else:
            break
    titles = titles[:target_titles]
    (out / "title_list.json").write_text(json.dumps(titles, indent=1), encoding="utf-8")

    # 2) fetch whole-article plaintext extracts (ONE title per request -- MediaWiki
    #    forces exlimit=1). Parallelised with a small thread pool over the
    #    UNCACHED indices only; deterministic per-index cache files.
    n_fetch = min(n_fetch, len(titles))
    todo = [(idx, titles[idx]) for idx in range(n_fetch)
            if not (out / f"article_{idx:04d}.json").exists()]
    logger.info(f"Wikinews: {n_fetch} target articles, {len(todo)} to fetch "
                f"({n_fetch - len(todo)} cached)")
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(_fetch_wikinews_article, idx, title, out): (idx, title)
                for idx, title in todo}
        for fut in as_completed(futs):
            idx, title = futs[fut]
            try:
                res = fut.result()
                done += 1
                if done % 50 == 0:
                    logger.info(f"Wikinews fetched {done}/{len(todo)} (last idx {idx})")
            except Exception as e:
                logger.error(f"Wikinews article {idx} ({title!r}) failed: {e}")
    logger.info(f"Wikinews: fetched {done} new articles")


# --------------------------------------------------------------------------- eCFR
# US regulatory companion (iter_4: broadened). Pull section XML for parts rich in
# short, self-contained sections (definitions / requirements). Date pinned for
# reproducibility. NEW parts add telemarketing, HIPAA, Reg S-P, Reg E.
ECFR_DATE = "2024-12-31"
ECFR_TARGETS = [
    # (title, part) -- federal privacy / consumer-protection rules with many
    # short, self-contained sections.
    (16, 312),   # COPPA - Children's Online Privacy Protection Rule
    (16, 314),   # Standards for Safeguarding Customer Information (FTC Safeguards)
    (12, 1016),  # Privacy of Consumer Financial Information (Reg P)
    (16, 310),   # Telemarketing Sales Rule
    (45, 164),   # HIPAA Security and Privacy Rules
    (17, 248),   # Regulation S-P: Privacy of Consumer Financial Information (SEC)
    (12, 1005),  # Electronic Fund Transfers (Regulation E)
]


def fetch_ecfr() -> None:
    out = RAW / "ecfr"
    out.mkdir(parents=True, exist_ok=True)
    for title, part in ECFR_TARGETS:
        dest = out / f"title-{title}-part-{part}.xml"
        if dest.exists() and dest.stat().st_size > 1000:
            logger.info(f"eCFR {title} CFR part {part}: cached")
            continue
        url = f"https://www.ecfr.gov/api/versioner/v1/full/{ECFR_DATE}/title-{title}.xml"
        try:
            r = _get(url, params={"part": str(part)}, timeout=120)
            dest.write_text(r.text, encoding="utf-8")
            logger.info(f"eCFR {title} CFR part {part}: {len(r.text)} bytes")
            time.sleep(0.8)
        except Exception as e:
            logger.error(f"eCFR {title} part {part} failed: {e}")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "gdpr"):
        fetch_gdpr()
    if which in ("all", "wikinews"):
        fetch_wikinews()
    if which in ("all", "ecfr"):
        fetch_ecfr()
    logger.info("fetch_sources done")
