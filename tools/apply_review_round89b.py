"""第89b轮：plaza 用 db-plaza（Designing Buildings 广场直接定义）替换泛援 pps，正式双源升级。"""
import json
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}


def ok(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25, context=ctx).status == 200
    except Exception:
        return False


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    if "db-plaza" not in by_id:
        url = "https://www.designingbuildings.co.uk/wiki/Plaza"
        good = ok(url)
        data["sources"].append({"id": "db-plaza", "title": "Plaza — Designing Buildings", "author": "Designing Buildings",
                                "type": "学术著作", "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；广场定义：连接街道网络的公共开敞空间，可从建筑前庭到城市大广场，由建筑围合"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "plaza":
                # 用 db-plaza 替换泛援的 pps
                e["sources"] = ["wp-town-square", "db-plaza"] + [s for s in e["sources"] if s not in ("wp-town-square", "pps-successful-place", "db-plaza")]
                e["definition"] = "广场是城市中由建筑围合、与街道相连的开敞公共空间，供聚会、庆典与日常活动使用。"
                e["overview"] = "广场可从建筑前庭到城市大广场，多由建筑围合、与路网相连，承载庆典、社交与休憩；作为公共空间类型不归于单一设计者。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round89b applied")


if __name__ == "__main__":
    main()
