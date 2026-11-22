"""第8轮抽检定向修正：保守化 daylight-factor 与 material-durability。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    path = ROOT / "entries" / "batch-08.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    for entry in doc["entries"]:
        if entry["id"] == "daylight-factor":
            entry["time_or_place"] = "跨时期、全球（参见来源）。"
            entry["overview"] = "该指标用于比较不同窗洞口条件下的天然采光潜力，便于方案阶段做横向对照。"
            entry["pending_notes"] = "实例参数与设计者待补独立来源；均布阴天假设下的解释性概括待补专门来源。"
        elif entry["id"] == "material-durability":
            sec = entry.setdefault("sections", {})
            sec["原理"] = "耐久性指材料在整个使用期内抵抗性能退化的能力，关系到维护周期与全生命周期成本。"
            entry["pending_notes"] = "实例寿命与维护数据待补独立来源；具体退化机制的通用列表待补专门来源。"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("polished daylight-factor and material-durability")


if __name__ == "__main__":
    main()
