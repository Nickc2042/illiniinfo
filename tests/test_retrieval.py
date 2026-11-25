import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from illiniinfo.retrieval import buildIndexes, search

class TestRetrieval(unittest.TestCase):

    def setUp(self):
        # small collection

        docs = [
            {
                "document_id": "UIUC-CS-001",
                "title": "CS Course Catalog",
                "heading": "CS 225",
                "text": "CS 225 covers data structures and algorithms.",
                "source_url": "https://catalog.illinois.edu/courses-of-instruction/cs/",
                "catalog_year": "2026-2027"
            },
            {
                "document_id": "UIUC-CS-002",
                "title": "CS Course Catalog",
                "heading": "CS 411",
                "text": "CS 411 introduces database systems.",
                "source_url": "https://catalog.illinois.edu/courses-of-instruction/cs/",
                "catalog_year": "2026-2027"
            },
        ]

        buildIndexes(docs) # build indexes pre seraching to be used in next test

    def test_TFIDF_Search(self):
        results = search("database systems", method="tfidf")
        self.assertEqual(results[0]["heading"],"CS 411")
        self.assertEqual(results[0]["catalog_year"],"2026-2027")

    def test_BM25_Search(self):
        results = search("database systems", method="bm25")
        self.assertEqual(results[0]["heading"],"CS 411")

    def testInvalid(self):
        with self.assertRaises(ValueError):
            search("database systems", method="stupidAlgoPlaceholder")

    def testBlankQuery(self):
        self.assertEqual(search(" "),[])

if __name__ == "__main__":
    unittest.main()