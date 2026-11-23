"""Adapt ranked results for the interface and supply its fixed preview."""

import re
from collections.abc import Iterable, Mapping
from importlib import import_module
from itertools import islice
from urllib.parse import urlsplit


def load_search():
    """Return the proposed retrieval entry point, or None while it is absent."""
    module_name = "illiniinfo.retrieval"
    try:
        module = import_module(module_name)
    except ModuleNotFoundError as exc:
        if exc.name == module_name:
            return None
        raise
    search = getattr(module, "search", None)
    if not callable(search):
        raise RuntimeError(f"{module_name} must export a callable search function.")
    return search


def _official_source_url(value: str) -> bool:
    if "\\" in value or any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in value):
        return False
    try:
        parts = urlsplit(value)
        hostname = parts.hostname or ""
        # Accessing port also validates an explicit port number.
        _ = parts.port
    except ValueError:
        return False
    return (
        parts.scheme in {"http", "https"}
        and parts.username is None
        and re.fullmatch(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)*illinois\.edu\.?", hostname)
        is not None
    )


def normalize_results(rows: Iterable[Mapping], top_k: int) -> list[dict[str, str]]:
    """Keep the first top_k passage records in the retriever's order."""
    if not isinstance(top_k, int) or isinstance(top_k, bool) or top_k < 1:
        raise ValueError("top_k must be a positive integer.")
    if isinstance(rows, (str, bytes, Mapping)) or not isinstance(rows, Iterable):
        raise ValueError("Search must return an iterable of passage records.")

    results = []
    for rank, row in enumerate(islice(rows, top_k), start=1):
        if not isinstance(row, Mapping):
            raise ValueError(f"Result {rank} must be a passage record.")
        result = {}
        for field in ("passage_id", "title", "text", "source_url"):
            value = row.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Result {rank} needs a nonempty {field}.")
            result[field] = value if field == "text" else value.strip()
        if not _official_source_url(result["source_url"]):
            raise ValueError(f"Result {rank} needs an HTTP(S) source_url on illinois.edu.")

        for field in ("heading", "catalog_year", "document_id", "degree_program", "collection_date"):
            value = row.get(field)
            if value is None:
                continue
            if not isinstance(value, str):
                raise ValueError(f"Result {rank} needs a string for {field}.")
            if value.strip():
                result[field] = value.strip()
        result.setdefault("heading", "")
        if result.get("catalog_year", "unknown").casefold() == "unknown":
            result["catalog_year"] = "Unknown"
        results.append(result)
    return results


PREVIEW_QUERY = "Where can I look up CS 225 and the Computer Science BS technical core?"


def preview_results() -> list[dict[str, str]]:
    """Return two illustrative records based on Nick's source and section inventories."""
    return [
        {
            "passage_id": "preview-cs-225",
            "document_id": "UIUC-CS-002",
            "title": "CS - Computer Science",
            "heading": "CS 225",
            "text": "Open the CS course catalog and look for the CS 225 entry to read its course description.",
            "source_url": "https://catalog.illinois.edu/courses-of-instruction/cs/",
            "catalog_year": "2026–2027 (provisional)",
        },
        {
            "passage_id": "preview-cs-technical-core",
            "document_id": "UIUC-CSBS-001",
            "degree_program": "Grainger Computer Science BS",
            "title": "Computer Science, BS",
            "heading": "Computer Science Technical Core",
            "text": "Open the Computer Science, BS degree page and look for the Computer Science Technical Core section.",
            "source_url": "https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs/",
            "catalog_year": "Unknown",
        },
    ]
