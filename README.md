# IlliniInfo

**University Information Assistant for Students**

A CS 410 information retrieval project at the University of Illinois Urbana-Champaign.

## Status

Source research and planning are in progress. The repository includes source and section inventories, source-review documentation, and evaluation templates.

Text collection, passage preparation, retrieval, interface development, and evaluation are planned next steps.

## Goal

Help UIUC students find relevant passages about undergraduate Computer Science degree requirements and related course information, with official source links and catalog-year context.

Our prototype will compare TF-IDF and BM25 over a small collection of public Academic Catalog pages and selected university policy sections. A Streamlit interface will display ranked passages and citations.

Initial source research focuses on Grainger Computer Science BS and the 2026-2027 catalog. The team still needs to confirm this scope.

## Core scope

- Select relevant official public sources.
- Collect text and source details in a shared dataset.
- Divide the text into passages while preserving headings, URLs, catalog years, and relevant exceptions.
- Implement and compare TF-IDF and BM25 using the same passages.
- Display ranked passages with citations through Streamlit.
- Evaluate approximately 25-30 representative questions using manual relevance judgments, Precision@5, and mean reciprocal rank.
- Check whether displayed passages support the requested information.

Broader degree coverage, Course Explorer integration, and generated summaries are optional extensions after the core workflow functions.

## Team

| Member | Tentative responsibility |
| --- | --- |
| Nick Chaudhari | Coordination, source collection, and organization |
| Kayetan Jarzabek | Preprocessing, indexing, and retrieval |
| Yoyo Lin | Interface development and integration |
| All members | Evaluation, testing, documentation, and presentation |

Responsibilities remain tentative until the team confirms them.

## Start here

1. Read the [proposal](docs/proposal.md).
2. Review the [source inventory](data/nick_source_manifest.csv), [section inventory](data/nick_section_inventory.csv), and [source review](docs/nick_source_review.md).
3. Review the [project plan](docs/project-plan.md), [backlog](docs/backlog.md), and [open decisions](docs/decisions.md).
4. Use the [contribution workflow](CONTRIBUTING.md) for future changes.
5. Refer to the [setup guide](docs/setup.md) for repository and team setup instructions.

## Repository layout

| Path | Purpose |
| --- | --- |
| `docs/` | Proposal, source review, project plans, decisions, and report template |
| `data/` | Source and section inventories, plus collection guidance |
| `src/illiniinfo/` | Reserved for application code |
| `evaluation/` | Question, judgment, and results templates |
| `tests/` | Reserved for tests |
| `reports/` | Reserved for experiment reports and presentation links |

## Running the project

There is no run command yet. Python 3.12 is the proposed development baseline.

We will add dependencies, installation steps, and run instructions with the first implementation.

## Submission links

- Code and documentation: https://github.com/Nickc2042/illiniinfo
- Presentation: Pending. We will add the Illinois MediaSpace link when available.

## Project context

IlliniInfo is a student research project. Search results will retain official source links and applicable catalog-year information.

The team has not selected a software license.
