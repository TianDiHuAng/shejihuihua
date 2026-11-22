"""第27轮：补齐 vestibule（门厅）L2 条目，回答 B4 读者问题。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
SVG = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='80' y='150' width='180' height='140' fill='none' stroke='var(--muted)'/><rect x='260' y='170' width='240' height='100' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='500' y='150' width='180' height='140' fill='none' stroke='var(--muted)'/><text x='300' y='130' fill='var(--ink)'>门厅：内外之间的缓冲</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>"

entry = {
    "id": "vestibule", "title": "门厅", "level": "L2", "tier": "重要",
    "theme": "理论", "period": "跨时期", "region": "全球",
    "definition": "门厅是进入较大空间前的小型过渡房间，缓冲室内外并承接换乘与等候。",
    "time_or_place": "跨时期、全球（参见来源）。",
    "overview": "门厅位于室内与街道之间，可挡风、减少热损失，并作为安检、礼仪与人流组织的过渡节点。",
    "related": ["transition-space"],
    "sections": {
        "原理": "作为“内外之间”的缓冲室，门厅减小开门时的冷风与热量流失，并把来访者从外部状态过渡到内部秩序。",
        "典型手法与适用条件": "以门厅组织换鞋、安检、等候与人流分流；适用于住宅入口、公共建筑与办公大堂。",
        "实例": "名称：公共建筑门厅（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "门厅过小会造成拥堵、过大则浪费能耗；疏散与无障碍宽度须按规范校核。" + REG,
        "一图": "见下方示意：门厅作为内外缓冲。",
        "待核实": "具体建筑门厅的设计者与年代待核实。",
    },
    "svg": [SVG],
    "sources": ["wp-vestibule-architecture", "wp-loggia"],
    "needs_verification": True,
    "pending_notes": "「门厅」的具体实例（名称、地点、设计者、年代）待补充独立来源。",
}


def main():
    out = ROOT / "entries" / "batch-27.json"
    data = {"unit_id": "batch-27", "title": "第27轮补齐条目", "entries": [entry]}
    if out.exists():
        data = json.loads(out.read_text(encoding="utf-8"))
        if not any(e["id"] == "vestibule" for e in data["entries"]):
            data["entries"].append(entry)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("vestibule written")


if __name__ == "__main__":
    main()
