import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from illiniinfo.indexing import TF_IDF_Index
class TestTFIDFIndex(unittest.TestCase):

    def test_search(self):
        passages = ["CS 225 covers data structures and algorithms", "CS 374 covers algorithms and computation", "CS 411 introduces database systems"]
        index = TF_IDF_Index(passages) # build TF IDF index
        results = index.search("database systems",top_k=2) # search for a topic related to databases specifically
        
        self.assertEqual(results[0][0], 2) # expecting the database passage to rank first at index 2


if __name__ == "__main__":
    unittest.main()
