import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from illiniinfo.preprocessing import cleanText, splitPassages, preProcessDoc

class TestPreprocessing(unittest.TestCase):

    def test_clean_text(self):
        text = "  CS   225\tcovers data structures.  "
        self.assertEqual(cleanText(text), "CS 225 covers data structures.")

    def test_split_passages(self):
        text = "CS 225 covers data structures and algorithms."
        passages = splitPassages(text, maxWords=4)

        self.assertEqual(len(passages), 2)
        self.assertEqual(" ".join(passages), text)

    def test_document_metadata(self):
        doc = {
            "document_id": "UIUC-CS-002",
            "title": "CS Course Catalog",
            "heading": "CS 225",
            "text": "CS 225 covers data structures and algorithms.",
            "source_url": "https://catalog.illinois.edu/courses-of-instruction/cs/",
            "catalog_year": "2026-2027"
        }

        passages = preProcessDoc(doc)

        self.assertEqual(passages[0]["passage_id"], "UIUC-CS-002-p001")
        self.assertEqual(passages[0]["heading"], "CS 225")
        self.assertEqual(passages[0]["catalog_year"], "2026-2027")
        self.assertEqual(passages[0]["source_url"], doc["source_url"])


if __name__ == "__main__":
    unittest.main()