# Project plan

Status: proposed plan; implementation has not started. Dates are intentionally unset.

## Milestones

| Order | Milestone | Tentative lead | Completion condition |
| --- | --- | --- | --- |
| 1 | Scope agreed | Nick + team | Exact degree program, catalog year(s), source boundaries, and evaluation rules are documented |
| 2 | Corpus ready | Nick | Curated sources and passages can be reproduced; source context is preserved |
| 3 | Retrieval ready | Kayetan | TF-IDF and BM25 rank the same passage collection through a common result format |
| 4 | Interface ready | Yoyo | Streamlit accepts questions and displays ranked passages, official links, and year context |
| 5 | Evaluation complete | All | Approximately 25–30 questions are judged; both systems have comparable metrics and a support review |
| 6 | Submission ready | All | Setup instructions work from a clean checkout; report, demo, and submission links are complete |

## Planned workflow

The future system will curate official sources, clean their text, create passages, build TF-IDF and BM25 indexes, rank passages for a student question, and display those passages with citations. The interface should present retrieved evidence; generating an answer is optional.

## Scope boundaries

Core: undergraduate Computer Science degree requirements, related course information, selected Academic Catalog pages, and relevant public policy sections.

Deferred: broad university coverage, Course Explorer integration, personalized degree audits, and generated summaries. Optional work begins only after the core workflow and evaluation function.

## Data agreement to establish later

Before implementation, agree on stable document and passage IDs, source URL, title, heading path, passage text, catalog year, and retrieval date. Do not silently combine requirements from different catalog years. Keep an unknown year explicit.

## Evaluation agreement to establish before scoring

- Prepare approximately 25–30 representative questions with IDs and explicit program/year context where needed. The templates are empty.
- Use the same corpus, passage boundaries, queries, and judgment rules for both rankers. Record preprocessing, parameters, corpus version, and deterministic tie handling with each run.
- Manually label passages as relevant (1) or nonrelevant (0). Unjudged passages are not automatically nonrelevant. Judge at least both systems' top-five results and every result needed to determine the reported reciprocal rank.
- For each question, Precision@5 = relevant passages in the top five / 5. If fewer than five are returned, absent slots contribute zero. Average per-question values for the overall score.
- For each question, reciprocal rank = 1 / rank of the first relevant passage, or 0 if none is found in the evaluated ranking. MRR is the average reciprocal rank over questions. If the ranking is truncated at depth k, label the result MRR@k and state k.
- Separately review whether displayed passages actually support the requested information and match its catalog-year context. Keep that check distinct from topical relevance.
- Agree on how to handle duplicates, multiple valid passages, ambiguous questions, and questions outside the corpus. Report the resulting limits.
- If tuning, keep development questions separate from the final evaluation questions and freeze the final protocol before comparing scores.

These are proposed measurement rules, not evaluation results.
