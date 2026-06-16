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
"""
from __future__ import annotations
import sys, json, time
from pathlib import Path
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
# A spread of GDPR articles biased toward naturally-short, self-contained ones
# (definitions, consent, the data-subject rights, breach notice, transfers).
GDPR_ARTICLES = [4, 5, 6, 7, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 25, 30,
                 32, 33, 34, 44, 77]


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


def fetch_wikinews(target_titles: int = 600) -> None:
    out = RAW / "wikinews"
    out.mkdir(parents=True, exist_ok=True)
    # 1) collect a stable list of mainspace, non-redirect article titles
    titles: list[str] = []
    apcontinue = None
    page_i = 0
    while len(titles) < target_titles and page_i < 8:
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
            time.sleep(0.5)
        else:
            break
    titles = titles[:target_titles]
    (out / "title_list.json").write_text(json.dumps(titles, indent=1), encoding="utf-8")
    # 2) MediaWiki forces exlimit=1 for WHOLE-article plaintext extracts, so we
    #    must fetch one title per request. We only need ~15 in-band articles, so
    #    fetch the first `n_fetch` titles individually (deterministic order).
    n_fetch = min(200, len(titles))
    for idx in range(n_fetch):
        title = titles[idx]
        dest = out / f"article_{idx:04d}.json"
        if dest.exists():
            continue
        params = {
            "action": "query", "format": "json", "titles": title,
            "prop": "extracts|info|revisions",
            "explaintext": "1", "exsectionformat": "plain",
            "inprop": "url", "rvprop": "ids|timestamp",
        }
        r = _get(WN_API, params=params)
        dest.write_text(r.text, encoding="utf-8")
        if idx % 25 == 0:
            logger.info(f"Wikinews article {idx}/{n_fetch}: {title!r}")
        time.sleep(0.25)


# --------------------------------------------------------------------------- eCFR
# US regulatory companion. Pull section XML for a few parts rich in short,
# self-contained sections (definitions / requirements). date pinned for repro.
ECFR_DATE = "2024-12-31"
ECFR_TARGETS = [
    # (title, part) -- FTC privacy/telemarketing & consumer rules, short sections
    (16, 312),   # COPPA - Children's Online Privacy Protection Rule
    (16, 314),   # Standards for Safeguarding Customer Information
    (12, 1016),  # Privacy of Consumer Financial Information (Reg P)
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
            r = _get(url, params={"part": str(part)}, timeout=90)
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
