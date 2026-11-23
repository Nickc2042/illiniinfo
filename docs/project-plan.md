# Project plan

Source research has started. This plan outlines the remaining work. Responsibilities and milestone dates still need team confirmation.

## Milestones

| Order | Milestone | Tentative lead | Completion condition |
| --- | --- | --- | --- |
| 1 | Scope agreed | Nick + team | Program, catalog edition, source boundaries, data fields, and evaluation rules are documented |
| 2 | Corpus ready | Nick + Kayetan | Shared source text and processed passages are reproducible and retain source context |
| 3 | Retrieval ready | Kayetan | TF-IDF and BM25 rank the same passages through a shared result format |
| 4 | Interface ready | Yoyo | Streamlit displays ranked passages with official links, headings, and catalog-year context |
| 5 | Evaluation complete | Everyone | Approximately 25-30 questions have relevance judgments, ranking metrics, and a passage-support review |
| 6 | Submission ready | Everyone | Setup instructions, documentation, presentation, and submission links are complete |

Nick will focus on source collection and organization. Kayetan will handle preprocessing, indexing, and retrieval. Yoyo will handle interface development and integration.

## Planned workflow

We will select official sources and collect verified text in a shared dataset.

We will clean the text, create passages, and build TF-IDF and BM25 indexes over the same collection.

The interface will accept student questions and display ranked passages with citations. Generated answers are an optional extension.

## Scope

Our core scope covers undergraduate Computer Science degree requirements, related course information, selected Academic Catalog pages, and relevant public university policies.

Initial source research focuses on Grainger Computer Science BS and the 2026-2027 catalog. The team still needs to confirm this choice.

We will defer broader degree coverage, Course Explorer integration, personalized degree audits, and generated summaries until the core workflow and evaluation function.

## Shared data format

Before connecting the components, we will agree on:

- Document ID
- Passage ID
- Source URL
- Document title
- Heading context
- Passage text
- Catalog year
- Collection date

We will preserve relevant tables, footnotes, course alternatives, and exceptions.

We will keep different degree programs and catalog editions separate. Unknown years will stay explicitly labeled as unknown.

## Evaluation plan

We will prepare approximately 25-30 representative questions with IDs and program/year context where needed.

Both rankers will use the same corpus, passages, questions, and judgment rules. We will record preprocessing settings, ranking parameters, corpus versions, and tie handling.

### Relevance judgments

We will label passages as relevant (1) or nonrelevant (0). Missing judgments will stay unjudged.

We will judge both systems’ top-five results and enough additional results to establish the first relevant passage within the reported ranking depth.

### Precision@5

For each question:

Precision@5 = number of relevant passages in the top five / 5

If fewer than five passages return, missing positions contribute zero. We will average the per-question scores.

### Mean reciprocal rank

For each question:

Reciprocal rank = 1 / rank of the first relevant passage

The score is zero if no relevant passage appears within the evaluated ranking depth.

MRR is the average reciprocal rank across questions. If we limit evaluation to depth k, we will report MRR@k and state k.

### Passage support

We will separately check whether displayed passages support the requested information and match the question’s program and catalog-year context.

### Evaluation controls

Before scoring, we will agree on how to handle duplicate results, multiple relevant passages, ambiguous questions, and questions outside the collection.

We will keep tuning questions separate from the final evaluation set and finalize the protocol before comparing results.

These rules describe planned evaluation. We have not reported measured results.

## Progress updates and submission

We will combine team updates into a progress report on textdata.org using the #progress tag.

Each member will contribute documentation and presentation material for their work. We will add measured results, limitations, reproduction instructions, and final submission links as the project develops.
