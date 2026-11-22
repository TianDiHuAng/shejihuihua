"""check.py 的失败测试：先运行确认 FAIL，再实现校验器。"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))


def write(root, rel, obj):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def svg(caption_ok=True):
    cap = "示意图，非施工图" if caption_ok else "随便一张图"
    return (
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
        "<rect x='10' y='10' width='80' height='80'/>"
        f"<text x='20' y='90'>{cap}</text></svg>"
    )


def base_entry(**overrides):
    entry = {
        "id": "perspective", "title": "透视法", "level": "L2", "tier": "核心",
        "theme": "理论", "period": "跨时期", "region": "全球",
        "definition": "在平面上表现空间深度的方法。",
        "time_or_place": "文艺复兴时期欧洲",
        "overview": "通过灭点与视平线组织画面空间。",
        "related": [],
        "sections": {
            "原理": "视线汇聚产生深度感。",
            "手法": "确定视平线与灭点后连线。",
            "实例": "名称、地点、设计者、年份",
            "常见错误与限制": "灭点混乱；实际工程须按当地规范和专业设计人员的要求。",
        },
        "svg": [svg()],
        "sources": ["src-a", "src-b"],
        "needs_verification": False,
        "pending_notes": "",
    }
    entry.update(overrides)
    return entry


class CheckTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "entries").mkdir()
        write(self.root, "data/sources.json", {"sources": [
            {"id": "src-a", "title": "Perspective (graphical) - Wikipedia", "author": "Wikipedia contributors",
             "type": "权威百科", "year": None, "url": "https://example.org/a", "url2": None,
             "verified": True, "note": "标题与机构已核对，访问于 2026-11-22"},
            {"id": "src-b", "title": "Composition (visual arts) - Wikipedia", "author": "Wikipedia contributors",
             "type": "权威百科", "year": None, "url": "https://example.org/b", "url2": None,
             "verified": True, "note": "标题与机构已核对，访问于 2026-11-22"},
            {"id": "src-c", "title": "未核验页面", "author": "未知", "type": "权威百科",
             "year": None, "url": "https://example.org/c", "url2": None,
             "verified": False, "note": "无法打开"},
        ]})
        (self.root / "scope.md").write_text(
            "| id | 名称 | 层级 | 时期 | 地区 | 来源 |\n"
            "| --- | --- | --- | --- | --- | --- |\n"
            "| perspective | 透视法 | 核心 | 跨时期 | 全球 | S5 |\n",
            encoding="utf-8",
        )
        write(self.root, "coverage.json", {"updated": "2026-11-22", "total": 1, "entries": [
            {"id": "perspective", "title": "透视法", "theme": "理论", "tier": "核心",
             "period": "跨时期", "region": "全球", "level": "L2", "status": "已完成",
             "source_count": 2, "needs_verification_count": 0, "last_updated": "2026-11-22"},
        ]})
        write(self.root, "entries/sample.json", {"unit_id": "sample", "title": "样板", "entries": [base_entry()]})

    def tearDown(self):
        self.tmp.cleanup()

    def run_check(self):
        import check
        return check.validate_all(self.root)

    def test_unverified_source_rejected(self):
        write(self.root, "entries/sample.json", {"unit_id": "sample", "title": "样板",
              "entries": [base_entry(sources=["src-a", "src-c"])]})
        errors = self.run_check()
        self.assertTrue(any("verified" in e for e in errors), errors)

    def test_svg_script_rejected(self):
        bad = svg().replace("<rect", "<script>alert(1)</script><rect")
        write(self.root, "entries/sample.json", {"unit_id": "sample", "title": "样板",
              "entries": [base_entry(svg=[bad])]})
        errors = self.run_check()
        self.assertTrue(any("SVG" in e or "script" in e for e in errors), errors)

    def test_pending_notes_required(self):
        write(self.root, "entries/sample.json", {"unit_id": "sample", "title": "样板",
              "entries": [base_entry(needs_verification=True, pending_notes="")]})
        errors = self.run_check()
        self.assertTrue(any("pending_notes" in e for e in errors), errors)

    def test_scope_coverage_mismatch(self):
        write(self.root, "coverage.json", {"updated": "2026-11-22", "total": 2, "entries": []})
        errors = self.run_check()
        self.assertTrue(any("scope" in e or "coverage" in e for e in errors), errors)

    def test_dual_source_rule(self):
        write(self.root, "entries/sample.json", {"unit_id": "sample", "title": "样板",
              "entries": [base_entry(sources=["src-a"])]})
        errors = self.run_check()
        self.assertTrue(any("双源" in e or "待核实" in e for e in errors), errors)

    def test_l2_requires_svg_caption(self):
        write(self.root, "entries/sample.json", {"unit_id": "sample", "title": "样板",
              "entries": [base_entry(svg=[svg(caption_ok=False)])]})
        errors = self.run_check()
        self.assertTrue(any("示意图，非施工图" in e for e in errors), errors)

    def test_valid_project_passes(self):
        self.assertEqual(self.run_check(), [])


if __name__ == "__main__":
    unittest.main()
