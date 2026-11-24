"""第89轮：plaza(城市广场) 概念双源(wp-town-square+pps) + 类型性实例，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "plaza":
                e["definition"] = "广场是城市中向公众开放的开敞公共空间，供聚会、庆典与日常活动使用。"
                e["overview"] = "广场多为建筑围合的开敞场地，承载庆典、社交与休憩；作为公共空间类型，不归于单一设计者。"
                e["sections"]["实例"] = "名称：城市中心广场（类型性，公共空间类型不归于单一设计者）；地点：不指定具体项目。以建筑围合的开敞铺装场地供聚会、庆典与休憩。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round89 applied")


if __name__ == "__main__":
    main()
