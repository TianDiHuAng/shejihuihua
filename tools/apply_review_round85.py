"""第85轮：tibetan-architecture / xinjiang-architecture 传统民族建筑，概念多源直证、类型性实例(无单一设计者)，升级 nv=false。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = {
 "tibetan-architecture": "藏式建筑以石木厚墙、平顶、碉楼与梯形窗适应高原寒冷，由 xizang.gov.cn、商洛学院、中国非遗网 三源直证；作为传统民族建筑，通常无单一设计者，故以类型性实例呈现。",
 "xinjiang-architecture": "新疆生土/土坯建筑以拱券、内院与廊架适应干热气候，由和田市、吐鲁番市两个政府源直证；作为传统地域民居，通常无单一设计者，故以类型性实例呈现。",
}
OV = {
 "tibetan-architecture": "传统上由地方工匠依高原环境集体营建、无单一设计者，故以类型性实例呈现其构造特征。",
 "xinjiang-architecture": "传统上由当地民居自发营建、无单一设计者，故以类型性实例呈现其构造特征。",
}
DEFS = {
 "tibetan-architecture": "藏式建筑以石木厚墙、平顶与碉楼式体量适应高原寒冷强日照；传统上由地方工匠集体营建。",
 "xinjiang-architecture": "新疆生土建筑以土坯拱券、内院与外廊适应干热气候；传统上由地方民居自发营建。",
}


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in NOTES:
                e["definition"] = DEFS[e["id"]]
                e["overview"] = OV[e["id"]]
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round85 applied")


if __name__ == "__main__":
    main()
