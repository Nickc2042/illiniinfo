# Project backlog

Source research has started. This backlog outlines the remaining work. Responsibilities are tentative until the team confirms them.

We will post combined progress updates on textdata.org with the #progress tag as work develops.

## 1. Confirm scope and shared data fields

Tentative lead: Nick.
Review: everyone.

Our proposed starting scope is Grainger Computer Science BS and the 2026-2027 catalog.

We need to confirm the program, catalog edition, source boundaries, passage fields, search-result fields, evaluation rules, and milestone dates.

Done when we record these decisions in docs/decisions.md.

## 2. Review and finalize the source inventory

Tentative lead: Nick.
Depends on: 1 for final approval.

Initial research is recorded in:

- data/nick_source_manifest.csv
- data/nick_section_inventory.csv

We need to confirm which sources and sections belong in the first collection. We will keep pending, optional, and excluded sources clearly labeled.

Done when the team approves the initial source list and verifies the relevant links, program context, and catalog editions.

## 3. Collect text and prepare passages

Tentative collection lead: Nick.
Tentative preprocessing lead: Kayetan.
Depends on: 2.

We will collect verified text and source details in a shared dataset.

We will preserve headings, tables, footnotes, course options, and exceptions during processing. Each passage will retain its passage ID, source ID, URL, heading context, catalog year, and collection date.

Done when we have a documented collection and processing workflow, consistent passages, and checks for empty content and duplicate sources.

## 4. Implement TF-IDF and BM25 retrieval

Tentative lead: Kayetan.
Depends on: 3.
Result-format planning starts after: 1.

We will compare TF-IDF and BM25 using the same passage collection and questions.

Both systems will return a shared result format containing passage text, ranking information, and source details.

Done when both rankers work and we document preprocessing settings, ranking parameters, corpus version, and tie handling.

## 5. Build the Streamlit search interface

Tentative lead: Yoyo.
Interface planning starts after: 1.
Retrieval integration depends on: 4.

The interface will accept student questions and display ranked passages with titles, headings, official links, and catalog-year context.

Done when search results display correctly and the interface handles empty input, no results, and retrieval errors.

## 6. Evaluate both ranking systems

Lead: everyone.
Question design starts after: 1.
Ranking evaluation depends on: 4.
Display review depends on: 5.

We will prepare approximately 25-30 representative questions and manually judge passage relevance.

We will compare Precision@5 and MRR, check whether displayed passages support the requested information, and summarize common errors.

Done when we document the questions, judgments, results, corpus versions, and evaluation settings. We will keep tuning separate from the final evaluation questions.

## 7. Prepare the final documentation and submission

Lead: everyone.
Coordinator: Nick.
Depends on: 6 for final results.

We will update the README with setup and reproduction instructions, measured results, and project limitations.

Each member will contribute documentation and presentation material for their work.

Done when the documentation is complete, the presentation is available, and the GitHub and MediaSpace submission links are filled in.
