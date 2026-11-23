import sys
import unittest
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock

from streamlit.testing.v1 import AppTest


APP = Path(__file__).resolve().parents[1] / "src" / "illiniinfo" / "app.py"
ROWS = [
    {
        "passage_id": "course-p2",
        "title": "CS course catalog",
        "heading": "CS 225",
        "text": "A sample course passage.\nA second line from the same passage.",
        "source_url": "https://catalog.illinois.edu/courses-of-instruction/cs/",
        "catalog_year": "2026-2027",
    },
    {
        "passage_id": "degree-p1",
        "title": "Computer Science, BS",
        "heading": "Computer Science Technical Core",
        "text": "A sample degree passage.",
        "source_url": "https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs/",
    },
]


class InterfaceTests(unittest.TestCase):
    def start(self, search=None):
        name = "illiniinfo.retrieval"
        if name in sys.modules:
            self.addCleanup(sys.modules.__setitem__, name, sys.modules[name])
        else:
            self.addCleanup(sys.modules.pop, name, None)
        module = None
        if search is not None:
            module = ModuleType(name)
            module.search = search
        sys.modules[name] = module
        app = AppTest.from_file(str(APP)).run()
        self.assertFalse(app.exception)
        return app

    def submit(self, app, question):
        app.text_input[0].input(question)
        app.button[0].click().run()
        self.assertFalse(app.exception)

    def test_preview_is_identified_without_a_retriever(self):
        app = self.start()
        self.assertIn("CS 225", app.text_input[0].value)
        self.assertTrue(app.button[0].disabled)
        self.assertEqual(len(app.get("link_button")), 2)
        self.assertTrue(any("example" in node.value.lower() for node in app.header))
        self.assertIsNone(app.radio[0].value)
        app.selectbox[0].select(1).run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.get("link_button")), 1)

    def test_blank_query_does_not_call_the_retriever(self):
        search = Mock()
        app = self.start(search)
        self.submit(app, "   ")
        search.assert_not_called()
        self.assertTrue(app.warning)
        self.assertFalse(app.get("link_button"))

    def test_ranker_arguments_order_citations_and_rerun(self):
        search = Mock(return_value=ROWS)
        app = self.start(search)
        self.assertEqual(app.selectbox[0].value, 5)
        app.radio[0].set_value("BM25")
        app.selectbox[0].select(2)
        self.submit(app, "  Find CS 225  ")
        search.assert_called_once_with("Find CS 225", method="bm25", top_k=2)
        self.assertEqual([node.value for node in app.text], [r["text"] for r in ROWS])
        sources = app.get("link_button")
        self.assertEqual([button.proto.url for button in sources], [row["source_url"] for row in ROWS])
        self.assertEqual([node.value for node in app.subheader], ["1. CS 225", "2. Computer Science Technical Core"])
        details = "\n".join(node.value for node in app.caption)
        for row, button in zip(ROWS, sources):
            self.assertIn(row["title"], button.proto.label)
            self.assertIn(row["passage_id"], details)
        self.assertIn("2026-2027", details)
        self.assertIn("unknown", details.lower())
        app.run()
        self.assertFalse(app.exception)
        self.assertEqual(search.call_count, 1)
        self.assertEqual(len(app.get("link_button")), 2)

    def test_display_limit_and_default_method(self):
        search = Mock(return_value=ROWS)
        app = self.start(search)
        app.selectbox[0].select(1)
        self.submit(app, "Technical core")
        search.assert_called_once_with("Technical core", method="tfidf", top_k=1)
        self.assertEqual([node.value for node in app.text], [ROWS[0]["text"]])

    def test_new_search_replaces_old_results_on_empty_response_or_failure(self):
        for response, state in [
            ([], "info"),
            (RuntimeError("index missing"), "error"),
            ([dict(ROWS[0], source_url="https://illinois.edu.example.org/")], "error"),
        ]:
            with self.subTest(response=response):
                search = Mock(side_effect=[ROWS, response])
                app = self.start(search)
                self.submit(app, "CS 225")
                self.assertEqual(len(app.get("link_button")), 2)
                self.submit(app, "Different question")
                self.assertTrue(app.get(state))
                self.assertFalse(app.get("link_button"))
                self.assertFalse(app.text)
                self.assertEqual(search.call_count, 2)


if __name__ == "__main__":
    unittest.main()
