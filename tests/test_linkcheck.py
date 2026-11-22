"""linkcheck.py 三态分类测试。"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))


class LinkCheckTest(unittest.TestCase):
    def test_classify_status(self):
        import linkcheck
        self.assertIs(linkcheck.classify(200), True)
        self.assertIs(linkcheck.classify(301), True)
        self.assertEqual(linkcheck.classify(403), "blocked")
        self.assertEqual(linkcheck.classify(429), "blocked")
        self.assertIs(linkcheck.classify(404), False)
        self.assertIs(linkcheck.classify(None), None)


if __name__ == "__main__":
    unittest.main()
