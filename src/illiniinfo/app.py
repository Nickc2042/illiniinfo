"""Streamlit entry point for IlliniInfo passage search."""

import logging
import re
import sys
from pathlib import Path

import streamlit as st

# Streamlit adds the script's directory to sys.path. Add src so the
# interface and its sibling retrieval module share the same package name.
SRC = str(Path(__file__).resolve().parents[1])
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from illiniinfo.interface_backend import (
    PREVIEW_QUERY,
    load_search,
    normalize_results,
    preview_results,
)


LOGGER = logging.getLogger(__name__)
METHODS = {"TF-IDF": "tfidf", "BM25": "bm25"}
RESULT_KEY = "illiniinfo_last_search"


def label(text):
    """Keep source and query text literal inside Streamlit Markdown labels."""
    return re.sub(r"([\\`*_{}\[\]()<>#+.!|~$])", r"\\\1", text)


def render_passage(position, passage):
    title = passage["title"]
    with st.container(border=True):
        heading = passage.get("heading") or title
        st.subheader(f"{position}. {label(heading)}", anchor=False)
        context = [f"Catalog year: {label(passage['catalog_year'])}"]
        if passage.get("degree_program"):
            context.append(label(passage["degree_program"]))
        st.caption(" · ".join(context))
        st.text(passage["text"])
        st.link_button(f"Open source · {label(title)}", passage["source_url"])
        identifiers = [f"Passage: {label(passage['passage_id'])}"]
        if passage.get("document_id"):
            identifiers.append(f"Document: {label(passage['document_id'])}")
        if passage.get("collection_date"):
            identifiers.append(f"Collected: {label(passage['collection_date'])}")
        st.caption(" · ".join(identifiers))


def main():
    st.set_page_config(page_title="IlliniInfo | Catalog search", layout="centered")
    st.title("IlliniInfo")
    st.write("Search UIUC undergraduate Computer Science requirements and course information.")
    try:
        search = load_search()
    except Exception as exc:
        LOGGER.error("Retrieval setup failed (%s)", type(exc).__name__)
        st.session_state.pop(RESULT_KEY, None)
        st.error("Search could not start. Check that the retrieval module and its dependencies are installed.")
        return

    preview = search is None
    if preview:
        st.session_state.pop(RESULT_KEY, None)
        st.info(
            "Interface preview. Live search will be available when the retrieval system is connected. "
            "The example text and order below illustrate how results will appear."
        )

    examples = preview_results() if preview else []
    # Preview controls can update the sample immediately. Live search runs
    # only when the student submits the form.
    with (st.container(border=True) if preview else st.form("passage_search")):
        question = st.text_input(
            "Your question",
            value=PREVIEW_QUERY if preview else "",
            placeholder="For example, what are the prerequisites for CS 225?",
            disabled=preview,
            key="example_question" if preview else "search_question",
        )
        method_col, depth_col = st.columns([2, 1])
        method = method_col.radio(
            "Ranking method", list(METHODS), index=None if preview else 0,
            horizontal=True, disabled=preview,
        )
        if preview:
            top_k = depth_col.selectbox("Maximum passages", range(1, len(examples) + 1), index=len(examples) - 1)
            st.button("Search", type="primary", disabled=True)
        else:
            top_k = depth_col.selectbox("Maximum passages", range(1, 11), index=4)
            submitted = st.form_submit_button("Search", type="primary")

    if preview:
        st.header("Example passages", anchor=False)
        for position, passage in enumerate(examples[:top_k], start=1):
            render_passage(position, passage)
        return

    if submitted:
        st.session_state.pop(RESULT_KEY, None)
        query = question.strip()
        if not query:
            st.warning("Enter a question to search.")
            return
        try:
            with st.spinner("Searching passages…"):
                rows = search(query, method=METHODS[method], top_k=top_k)
                passages = normalize_results(rows, top_k)
        except Exception as exc:
            LOGGER.error("Passage search failed (%s)", type(exc).__name__)
            st.error("The search could not return passages. Try again or check the retrieval index.")
            return
        st.session_state[RESULT_KEY] = (query, method, passages)

    result = st.session_state.get(RESULT_KEY)
    if result is None:
        return
    query, method, passages = result
    st.header("Ranked passages", anchor=False)
    count = len(passages)
    noun = "passage" if count == 1 else "passages"
    st.caption(f"{method} · {count} {noun} for “{label(query)}”")
    if not passages:
        st.info("No passages found. Try a course number or a more specific requirement.")
        return
    for position, passage in enumerate(passages, start=1):
        render_passage(position, passage)


if __name__ == "__main__":
    main()
