# Working together

## Workflow

1. Choose a task and agree on its acceptance criteria.
2. Update your local `main`, then create a short branch such as `docs/scope` or `feature/tfidf`.
3. Make one focused change and verify the behavior relevant to it.
4. Open a pull request explaining what changed, why, and how it was checked.
5. Have another teammate review it, then merge and delete the task branch.

Keep `main` usable as the project develops. Record important scope or evaluation decisions in `docs/decisions.md`.

## What belongs in Git

Commit code, documentation, small source metadata tables, evaluation questions, judgments, and compact reproducibility records. Keep downloaded page snapshots, generated passages, indexes, environments, credentials, and machine-specific files out of Git by default. Document how to reproduce generated data when collection is implemented.

Do not commit student identifiers or private university content. The planned corpus uses public official sources only.

## Team handoffs

Before connecting collection, retrieval, and the interface, agree on the passage fields, query input, and ranked-result fields. Preserve the source URL, heading context, and applicable catalog year through each stage. Record the agreed contract in documentation when implementation begins.

## Checks

Documentation changes: check links and accuracy. Later code changes: run the relevant tests and record the command and result in the pull request. Do not claim an unrun check passed. No automated checks or tests are installed in this foundation.
