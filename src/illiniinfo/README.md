# Search interface

Start the [Streamlit app from the repository root](../../README.md#running-the-project). Until a retriever is installed, it shows a fixed example question about CS 225 and the CS technical core. The two example cards link to sources in Nick’s inventory. The course example uses the provisional catalog edition from the inventory. The degree example shows how a missing year appears. Their text and positions are illustrative.

## Connecting the rankers

The proposed entry point is `search(query, *, method, top_k)` in `src/illiniinfo/retrieval.py`. The UI passes a trimmed question, a method of `"tfidf"` or `"bm25"`, and a maximum result count (five by default). Return an iterable of dictionaries in the ranker’s order. An empty iterable means the search found no passages. If the retrieval implementation uses different names or a different signature, adapt the call in `interface_backend.py`. Either ranker can keep its own internal representation.

| Result field | What the interface uses |
| --- | --- |
| `passage_id` | Stable ID for identifying a passage during evaluation |
| `title` | Source document title |
| `text` | Complete passage, including line breaks, footnotes, and exceptions |
| `source_url` | Official Illinois HTTP or HTTPS URL, with a section anchor when available |
| `heading` | Section or course heading, if available |
| `catalog_year` | Edition attached to the passage. Missing or blank values display as “Unknown.” |
| `document_id`, `degree_program`, `collection_date` | Optional source details, shown when supplied |

The first four fields require nonempty strings. Optional fields may be omitted or set to `None`. An example record follows.

```python
{
    "passage_id": "example-cs-225",
    "title": "CS - Computer Science",
    "heading": "CS 225",
    "text": "Illustrative passage text.",
    "source_url": "https://catalog.illinois.edu/courses-of-instruction/cs/",
    "catalog_year": None,
    "document_id": "UIUC-CS-002",
}
```

Once both indexes and the real passages are available, run the same question with each ranker. Compare the displayed order and IDs with each ranker’s output, open a citation, and check the displayed heading, passage, and catalog edition against that source.
