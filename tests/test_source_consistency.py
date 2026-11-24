"""check.py 新增来源规则的单元测试：verified+link_ok=false 矛盾、重复 URL 未披露。"""
import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import check


class TestSourceConsistencyRules(unittest.TestCase):
    def make_root(self, sources):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        (root / "data").mkdir()
        (root / "data" / "sources.json").write_text(
            json.dumps({"sources": sources}, ensure_ascii=False), encoding="utf-8")
        self.addCleanup(tmp.cleanup)
        return root

    def base_src(self, sid, url, note="核验说明"):
        return {"id": sid, "title": "T", "author": "A", "type": "百科", "url": url,
                "verified": True, "note": note, "link_ok": True}

    def test_verified_with_dead_link_is_error(self):
        s = self.base_src("s1", "https://example.org/a")
        s["link_ok"] = False
        errors, _ = check.validate_sources(self.make_root([s]))
        self.assertTrue(any("link_ok=false" in e for e in errors), errors)

    def test_duplicate_url_without_disclosure_is_error(self):
        a = self.base_src("a1", "https://example.org/a")
        b = self.base_src("b1", "https://example.org/a")
        errors, _ = check.validate_sources(self.make_root([a, b]))
        self.assertTrue(any("重复 URL" in e for e in errors), errors)

    def test_duplicate_url_with_disclosure_passes(self):
        a = self.base_src("a1", "https://example.org/a", "核验说明 [B4] 同页另一登记")
        b = self.base_src("b1", "https://example.org/a", "核验说明 [B4] 同页另一登记")
        errors, _ = check.validate_sources(self.make_root([a, b]))
        self.assertFalse(any("重复 URL" in e for e in errors), errors)

    def test_different_query_not_duplicate(self):
        a = self.base_src("a1", "https://example.org/a?id=1")
        b = self.base_src("b1", "https://example.org/a?id=2")
        errors, _ = check.validate_sources(self.make_root([a, b]))
        self.assertFalse(any("重复 URL" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
