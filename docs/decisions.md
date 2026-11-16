# Decisions and open questions

## Established by the proposal

| Topic | Direction |
| --- | --- |
| Project | IlliniInfo: University Information Assistant for Students |
| Initial focus | Undergraduate CS requirements and related course information |
| Sources | Curated public Academic Catalog pages and selected university policy sections |
| Ranking | Compare TF-IDF and BM25 |
| Interface | Streamlit; ranked passages and citations |
| Evaluation | Approximately 25–30 questions, manual relevance, Precision@5, MRR, passage-support review |
| Extensions | Broader degrees, Course Explorer, generated summaries after the core workflow |
| Coordinator | Nick Chaudhari |

## Resolve before implementation

| Decision | Current status | Owner |
| --- | --- | --- |
| Exact undergraduate CS degree program covered | Open; do not assume CS, CS + X, and Math & CS share requirements | All |
| Catalog year(s) and handling of unknown years | Open | All |
| Initial source list and corpus size | Open; keep the collection small | Nick + team |
| Passage boundaries and common data/result fields | Open | Nick + Kayetan + Yoyo |
| Relevance, evidence support, duplicate, and MRR-depth rules | Proposed in project-plan.md; team review pending | All |
| Python version | Proposed: 3.12; not yet confirmed | All |
| Dependencies and versions | Deferred to implementation | All |
| Course deadlines and milestone dates | Open | Nick |
| Repository visibility and instructor access for submission | Proposed: private initially; submission access pending | Nick |
| Kayetan and Yoyo's GitHub usernames | Not provided; invitations not sent | Nick |
| Software license | Not selected | All |

## Decision log template

Copy this for each new decision:

```text
Date:
Decision:
Reason:
Agreed by:
Affected files or milestone:
```
