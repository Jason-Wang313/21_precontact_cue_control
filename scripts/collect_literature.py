from __future__ import annotations

import json
import math
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)
RAW_PATH = DOCS / "literature_openalex_raw.jsonl"
STATUS_PATH = DOCS / "literature_collection_status.json"

TARGET = 1250
PER_PAGE = 200

QUERIES: list[tuple[str, str]] = [
    ("robotic manipulation tactile sensing grasp", "tactile manipulation"),
    ("robotic grasping tactile feedback slip detection", "tactile grasping"),
    ("pre-touch sensing robotic manipulation proximity", "pretouch proximity"),
    ("precontact sensing robot hand grasping", "precontact grasping"),
    ("proximity sensor robotic gripper manipulation", "proximity sensing"),
    ("vision tactile robotic manipulation grasping", "visuotactile manipulation"),
    ("contact-rich manipulation robot control", "contact-rich control"),
    ("hybrid force position control robotic manipulation", "hybrid force control"),
    ("tactile servoing robotic manipulation", "tactile servoing"),
    ("reactive grasping tactile robot hand", "reactive grasping"),
    ("in-hand manipulation tactile robot dexterous", "dexterous in-hand"),
    ("robotic grasp planning force closure tactile", "grasp planning"),
    ("haptic exploration robot object recognition tactile", "haptic exploration"),
    ("active perception robotic grasping manipulation", "active perception"),
    ("multimodal tactile visual robot manipulation", "multimodal manipulation"),
    ("robot hand slip control tactile manipulation", "slip control"),
    ("robot manipulation compliance friction estimation tactile", "friction compliance"),
    ("deformable object manipulation robot tactile", "deformable manipulation"),
    ("robotic manipulation contact uncertainty grasp strategy", "uncertain contact"),
    ("event based tactile sensing robot manipulation", "event tactile"),
    ("gel tactile sensor robotic manipulation grasp", "gel tactile"),
    ("force tactile sensors robot grasp stability", "grasp stability"),
    ("robot learning manipulation tactile feedback", "learning tactile"),
    ("adaptive grasp strategy robot manipulation", "adaptive grasp"),
    ("sim-to-real robotic manipulation tactile grasp", "sim-to-real tactile"),
    ("robotic manipulation physical reasoning contact", "physical reasoning"),
    ("robot foundation model manipulation contact tactile", "foundation manipulation"),
    ("pregrasp perception robotic grasp strategy", "pregrasp perception"),
    ("noncontact tactile proximity robotic manipulation", "noncontact cue"),
    ("robotic hand preshaping grasp selection tactile", "preshape grasp"),
    ("grasp failure prediction tactile vision robot", "failure prediction"),
    ("contact mode estimation robotic manipulation", "contact mode"),
    ("impedance control robot manipulation contact", "impedance control"),
    ("model predictive control robotic manipulation contact", "contact MPC"),
    ("robot manipulation affordance grasp tactile", "affordance grasp"),
    ("robotic bin picking tactile grasping", "bin picking"),
]

KEYWORDS = {
    "robot": 3.0,
    "robotic": 3.0,
    "manipulation": 3.0,
    "grasp": 3.0,
    "grasping": 3.0,
    "tactile": 3.5,
    "haptic": 2.5,
    "touch": 2.5,
    "contact": 2.5,
    "precontact": 6.0,
    "pre-contact": 6.0,
    "pretouch": 6.0,
    "pre-touch": 6.0,
    "proximity": 4.5,
    "noncontact": 4.0,
    "sensor": 1.4,
    "sensing": 1.8,
    "slip": 2.5,
    "force": 1.6,
    "strategy": 2.0,
    "control": 1.4,
    "reactive": 2.0,
    "servo": 1.6,
    "dexterous": 2.0,
    "in-hand": 2.0,
    "compliance": 1.4,
    "friction": 1.4,
    "hybrid": 1.2,
    "multimodal": 1.4,
}


def write_status(stage: str, **extra: Any) -> None:
    payload = {"stage": stage, "time": time.strftime("%Y-%m-%d %H:%M:%S"), **extra}
    STATUS_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def decode_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positions: list[tuple[int, str]] = []
    for word, locs in index.items():
        if isinstance(locs, list):
            for loc in locs:
                if isinstance(loc, int):
                    positions.append((loc, word))
    if not positions:
        return ""
    positions.sort()
    return " ".join(word for _, word in positions)


def api_json(url: str, params: dict[str, Any], retries: int = 3) -> dict[str, Any] | None:
    params = {k: v for k, v in params.items() if v is not None}
    full = url + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        full,
        headers={
            "User-Agent": "paper21-precontact-cue-control/1.0 (mailto:anonymous@example.com)",
            "Accept": "application/json",
        },
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read()
            return json.loads(data.decode("utf-8", errors="replace"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            write_status("api_retry", url=url, params=params, attempt=attempt + 1, error=str(exc))
            time.sleep(1.5 * (attempt + 1))
    return None


def concept_list(work: dict[str, Any]) -> str:
    concepts = work.get("concepts") or []
    names: list[str] = []
    for concept in concepts[:8]:
        if isinstance(concept, dict) and concept.get("display_name"):
            names.append(clean_text(concept["display_name"]))
    keywords = work.get("keywords") or []
    for keyword in keywords[:8]:
        if isinstance(keyword, dict) and keyword.get("display_name"):
            names.append(clean_text(keyword["display_name"]))
    return "; ".join(dict.fromkeys(names))


def venue_name(work: dict[str, Any]) -> str:
    primary = work.get("primary_location") or {}
    source = primary.get("source") if isinstance(primary, dict) else None
    if isinstance(source, dict) and source.get("display_name"):
        return clean_text(source["display_name"])
    host = work.get("host_venue") or {}
    if isinstance(host, dict) and host.get("display_name"):
        return clean_text(host["display_name"])
    return ""


def author_names(work: dict[str, Any]) -> str:
    authorships = work.get("authorships") or []
    names: list[str] = []
    for authorship in authorships[:8]:
        author = authorship.get("author") if isinstance(authorship, dict) else None
        if isinstance(author, dict) and author.get("display_name"):
            names.append(clean_text(author["display_name"]))
    if len(authorships) > 8:
        names.append("et al.")
    return "; ".join(names)


def relevance_score(title: str, abstract: str, concepts: str, cited_by: int, year: int | None) -> float:
    text = f"{title} {abstract} {concepts}".lower()
    score = 0.0
    for term, weight in KEYWORDS.items():
        if term in text:
            score += weight
    if "robot" in text and ("grasp" in text or "manipulation" in text):
        score += 7.0
    if "tactile" in text and ("grasp" in text or "manipulation" in text):
        score += 6.0
    if ("precontact" in text or "pre-contact" in text or "pretouch" in text or "pre-touch" in text or "proximity" in text) and "robot" in text:
        score += 8.0
    if "contact" in text and "control" in text:
        score += 3.0
    score += min(8.0, math.log1p(max(cited_by, 0)))
    if year and year >= 2015:
        score += 1.5
    if year and year >= 2021:
        score += 1.0
    return score


def parse_openalex_work(work: dict[str, Any], query: str, bucket: str) -> dict[str, Any] | None:
    title = clean_text(work.get("display_name") or work.get("title"))
    if len(title) < 5:
        return None
    abstract = clean_text(decode_abstract(work.get("abstract_inverted_index")))
    year = work.get("publication_year")
    try:
        year_int = int(year) if year else None
    except (TypeError, ValueError):
        year_int = None
    cited_by = work.get("cited_by_count") or 0
    try:
        cited_by_int = int(cited_by)
    except (TypeError, ValueError):
        cited_by_int = 0
    concepts = concept_list(work)
    score = relevance_score(title, abstract, concepts, cited_by_int, year_int)
    doi = clean_text(work.get("doi")).replace("https://doi.org/", "")
    url = clean_text(work.get("id"))
    primary = work.get("primary_location") or {}
    landing = ""
    if isinstance(primary, dict):
        landing = clean_text(primary.get("landing_page_url") or primary.get("pdf_url"))
    return {
        "source": "OpenAlex",
        "source_id": clean_text(work.get("id")),
        "doi": doi,
        "title": title,
        "year": year_int or "",
        "venue": venue_name(work),
        "authors": author_names(work),
        "cited_by_count": cited_by_int,
        "abstract": abstract,
        "concepts": concepts,
        "query": query,
        "query_bucket": bucket,
        "url": landing or url,
        "relevance_score": round(score, 3),
    }


def parse_crossref_item(item: dict[str, Any], query: str, bucket: str) -> dict[str, Any] | None:
    title_items = item.get("title") or []
    title = clean_text(title_items[0] if title_items else "")
    if len(title) < 5:
        return None
    abstract = clean_text(re.sub("<[^>]+>", " ", item.get("abstract") or ""))
    issued = item.get("issued", {}).get("date-parts", [[None]])
    year = issued[0][0] if issued and issued[0] else None
    try:
        year_int = int(year) if year else None
    except (TypeError, ValueError):
        year_int = None
    authors = []
    for author in (item.get("author") or [])[:8]:
        given = clean_text(author.get("given"))
        family = clean_text(author.get("family"))
        name = clean_text(f"{given} {family}")
        if name:
            authors.append(name)
    if len(item.get("author") or []) > 8:
        authors.append("et al.")
    venue_items = item.get("container-title") or []
    venue = clean_text(venue_items[0] if venue_items else "")
    cited_by = int(item.get("is-referenced-by-count") or 0)
    concepts = clean_text(item.get("subject") or "")
    score = relevance_score(title, abstract, concepts, cited_by, year_int)
    doi = clean_text(item.get("DOI"))
    return {
        "source": "Crossref",
        "source_id": "https://doi.org/" + doi if doi else clean_text(item.get("URL")),
        "doi": doi,
        "title": title,
        "year": year_int or "",
        "venue": venue,
        "authors": "; ".join(authors),
        "cited_by_count": cited_by,
        "abstract": abstract,
        "concepts": concepts,
        "query": query,
        "query_bucket": bucket,
        "url": clean_text(item.get("URL")),
        "relevance_score": round(score, 3),
    }


def dedupe_key(row: dict[str, Any]) -> str:
    doi = clean_text(row.get("doi")).lower()
    if doi:
        return "doi:" + doi
    title = clean_text(row.get("title")).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title).strip()
    year = clean_text(row.get("year"))
    return f"title:{title}:{year}"


def collect_openalex() -> dict[str, dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    for qi, (query, bucket) in enumerate(QUERIES, start=1):
        cursor = "*"
        for page in range(2):
            write_status("openalex_fetch", query_index=qi, query=query, page=page + 1, unique=len(seen))
            data = api_json(
                "https://api.openalex.org/works",
                {
                    "search": query,
                    "per-page": PER_PAGE,
                    "cursor": cursor,
                    "filter": "from_publication_date:1970-01-01,to_publication_date:2026-06-11",
                    "mailto": "anonymous@example.com",
                },
            )
            if not data:
                break
            for work in data.get("results") or []:
                if not isinstance(work, dict):
                    continue
                row = parse_openalex_work(work, query, bucket)
                if not row:
                    continue
                key = dedupe_key(row)
                old = seen.get(key)
                if old is None or row["relevance_score"] > old["relevance_score"]:
                    seen[key] = row
            cursor = (data.get("meta") or {}).get("next_cursor")
            if not cursor:
                break
            if len(seen) >= TARGET and page == 0:
                break
            time.sleep(0.15)
        if len(seen) >= TARGET + 300:
            break
    return seen


def collect_crossref(seen: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    if len(seen) >= TARGET:
        return seen
    for qi, (query, bucket) in enumerate(QUERIES, start=1):
        write_status("crossref_fetch", query_index=qi, query=query, unique=len(seen))
        data = api_json(
            "https://api.crossref.org/works",
            {
                "query": query,
                "rows": 100,
                "select": "DOI,title,container-title,issued,author,abstract,is-referenced-by-count,URL,subject",
                "mailto": "anonymous@example.com",
            },
        )
        if not data:
            continue
        items = ((data.get("message") or {}).get("items") or [])
        for item in items:
            if not isinstance(item, dict):
                continue
            row = parse_crossref_item(item, query, bucket)
            if not row:
                continue
            key = dedupe_key(row)
            old = seen.get(key)
            if old is None or row["relevance_score"] > old["relevance_score"]:
                seen[key] = row
        if len(seen) >= TARGET:
            break
        time.sleep(0.2)
    return seen


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    write_status("start", target=TARGET, query_count=len(QUERIES))
    seen = collect_openalex()
    seen = collect_crossref(seen)
    rows = sorted(seen.values(), key=lambda r: (float(r.get("relevance_score") or 0), int(r.get("cited_by_count") or 0)), reverse=True)
    with RAW_PATH.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    write_status("done", unique=len(rows), raw_path=str(RAW_PATH), target_met=len(rows) >= 1000)
    print(json.dumps({"unique": len(rows), "raw_path": str(RAW_PATH), "target_met": len(rows) >= 1000}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        write_status("fatal_caught", error=repr(exc))
        print(json.dumps({"error": repr(exc), "raw_path": str(RAW_PATH)}, indent=2))
        raise SystemExit(0)
