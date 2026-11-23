# Interface tests

Install the [interface dependencies](../README.md#running-the-project) and run the following command from the repository root.

```bash
python -m unittest discover -s tests
```

The tests run the Streamlit app with its preview and with a test retriever. They exercise the query controls, result ordering, citations, missing catalog years, and empty or failed searches. Evaluating ranking quality requires the team’s passage collection and relevance judgments.
