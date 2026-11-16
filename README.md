# IlliniInfo

**University Information Assistant for Students**  
A CS 410 information retrieval project at the University of Illinois Urbana-Champaign.

## Status

Foundation and planning only. No documents have been collected, no retrieval system has been implemented, and no evaluation has been run. This repository is not a working application yet.

## Goal

Help UIUC students find relevant passages about undergraduate Computer Science degree requirements and related course information, with links to official sources and catalog-year context.

The core prototype will compare TF-IDF and BM25 ranking over a small, curated collection of public Academic Catalog pages and selected university policy sections. A Streamlit interface will display ranked passages and citations. Generated answers are an optional extension.

## Core scope

- Curate a small collection of relevant official public pages.
- Clean the documents and divide them into passages while retaining headings, URLs, and catalog-year metadata.
- Implement and compare TF-IDF and BM25 over the same passages.
- Display ranked passages with citations through Streamlit.
- Evaluate approximately 25–30 representative questions using manual relevance judgments, Precision@5, and mean reciprocal rank; separately check whether passages support the requested information.

Broader degree coverage, Course Explorer integration, and generated summaries are optional extensions after the core workflow functions.

## Team

| Member | Tentative responsibility |
| --- | --- |
| Nick Chaudhari | Coordinator; collection and preprocessing |
| Kayetan Jarzabek | Indexing and retrieval |
| Yoyo Lin | Interface development |
| All members | Evaluation, testing, and documentation |

## Start here

1. Read the [proposal](docs/proposal.md).
2. Follow the [GitHub setup guide](docs/setup.md) to finish repository and team setup.
3. Review the [project plan](docs/project-plan.md), [backlog](docs/backlog.md), and [open decisions](docs/decisions.md).
4. Use the [contribution workflow](CONTRIBUTING.md) for future work.

## Repository layout

| Path | Purpose |
| --- | --- |
| `docs/` | Proposal, setup, project plan, backlog, decisions, progress report |
| `src/illiniinfo/` | Reserved for future application code |
| `data/` | Source inventory template and future data guidance |
| `evaluation/` | Empty question, judgment, and results templates |
| `tests/` | Reserved for future tests |
| `reports/` | Reserved for experiment reports and presentation links |
| `.github/` | Issue and pull request templates |

## Running the project

There is no run command yet. Python 3.12 is the proposed development baseline; dependencies and installation commands will be added with the first implementation.

## Submission links

- Code and documentation: pending repository creation; replace this line with the final repository URL.
- Presentation: pending; add the final Illinois MediaSpace URL when available.

## Project context

This is a student project, not an official university advising service. Official sources and their applicable catalog years should remain visible with every result. A software license has not yet been selected by the team.
