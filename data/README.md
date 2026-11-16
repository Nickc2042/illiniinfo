# Data area

No sources have been selected or downloaded yet. `source_manifest.csv` is a header-only inventory template.

## Inventory fields

| Field | Purpose |
| --- | --- |
| document_id | Stable ID for a source document |
| title | Official page title |
| source_url | Official public URL |
| catalog_year | Applicable year, or explicit `unknown`; do not infer it from retrieval date |
| retrieved_at | Actual collection timestamp in ISO 8601 format; leave blank until fetched |
| inclusion_reason | Why this source belongs in the agreed scope |
| notes | Program, relevant sections, or collection notes |

Future downloaded pages belong in `raw/`, cleaned documents in `processed/`, passages in `passages/`, and indexes in `indexes/`. These generated directories are ignored by Git. Add the collection and reproduction instructions when implemented.

Use official public pages only. Preserve URL, headings, and year context when creating passages. Keep selected inventory metadata small enough to review in Git.
