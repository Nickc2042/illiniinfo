# Initial backlog

Planning only. These items have not been created as GitHub issues and are not assignments to begin implementation now. Create them when the team is ready.

## 1. Confirm scope and shared contracts

Tentative lead: Nick; review: all.

Done when the exact undergraduate CS program, catalog year(s), source boundaries, passage/result fields, evaluation rules, and milestone dates are recorded in docs/decisions.md.

## 2. Curate the official-source inventory

Tentative lead: Nick. Depends on 1.

Done when the team has reviewed a small, in-scope list of official public sources with stable IDs, URLs, year context, and inclusion reasons in data/source_manifest.csv. No collection occurs in the foundation stage.

## 3. Build collection and preprocessing

Tentative lead: Nick. Depends on 2.

Done when source snapshots and passages can be reproduced, headings and provenance survive cleaning, year metadata is retained, and malformed or empty content is handled. Agree on passage boundaries before indexing.

## 4. Implement the retrieval comparison

Tentative lead: Kayetan. Depends on 3; interfaces can be planned after 1.

Done when TF-IDF and BM25 use the same passage collection, return a shared result format with source metadata, and document their parameters and tie handling.

## 5. Build the Streamlit search interface

Tentative lead: Yoyo. Depends on the agreed contract in 1 and working retrieval in 4 for integration.

Done when a question produces ranked passages with titles, official links, headings, and catalog-year context; empty input, no results, and failures have clear behavior.

## 6. Evaluate both systems

Tentative lead: all. Define questions/rules after 1; score after 4 and review display support after 5.

Done when approximately 25–30 questions have documented judgments, comparable Precision@5 and MRR results, a passage-support review, and a short error analysis. Record corpus/run versions and avoid tuning on the final evaluation set.

## 7. Prepare the report, presentation, and submission

Tentative lead: all; coordinator: Nick. Depends on 6.

Done when the README supports reproduction, limitations and results are documented, the presentation is available, and the code/documentation and MediaSpace links are filled in.
