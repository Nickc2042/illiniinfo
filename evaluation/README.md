# Evaluation area

These CSV files contain headers only. No questions, judgments, or results have been produced.

| File | Intended use |
| --- | --- |
| `questions.csv` | Approximately 25–30 representative questions; program/year context; future development/evaluation split |
| `judgments.csv` | Manual passage relevance and separate evidence-support judgments |
| `results.csv` | One row per system/run with aggregate scores and reproducibility references |

## Conventions to confirm

- `query_id` and `passage_id` must match the IDs used by retrieval runs.
- In `questions.csv`, `split` can be `dev` or `eval`; do not tune on final evaluation questions. Specify the covered degree program and year when relevant.
- In `judgments.csv`, use `relevance` values 0 or 1. A missing judgment is unjudged, not 0. `supports_requested_information` can be `yes`, `partial`, or `no`; leave it blank until reviewed. `judge` is an agreed team label.
- In `results.csv`, `p_at_5` and `mrr` are aggregate means between 0 and 1; `query_count` is the number of scored questions. State a numeric `ranking_depth` if truncated, otherwise `full`. Identify the metric as MRR@k when truncated.
- Record `corpus_version`, `code_commit`, and `settings_path` with each run. The settings file should document ranker parameters, preprocessing, tie handling, and the query/judgment versions. These do not exist yet.
- Keep future machine-readable rankings and settings in `runs/` (ignored by Git by default). Commit only compact reviewed summaries, and record how full runs can be reproduced or located.

See [the project plan](../docs/project-plan.md) for the proposed formulas and judging protocol. Agree on the protocol before generating scores.
