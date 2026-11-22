"""第10轮：用现有已核验来源把 6 个核心风格/理论 L1 升级为 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

SVG = {
    "chiaroscuro": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='60' y='80' width='640' height='240' fill='none' stroke='var(--line)'/><circle cx='220' cy='200' r='90' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='330' y='140' width='120' height='120' fill='none' stroke='var(--muted)'/><text x='150' y='120' fill='var(--ink)'>受光面</text><text x='470' y='200' fill='var(--ink)'>暗部与投影</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "gothic": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='100' y1='320' x2='660' y2='320' stroke='var(--ink)' stroke-width='3'/><path d='M 200 320 L 200 180 Q 320 60 440 180 L 440 320' fill='none' stroke='var(--accent)' stroke-width='3'/><path d='M 420 320 L 420 180 Q 540 60 660 180 L 660 320' fill='none' stroke='var(--muted)' stroke-width='3'/><text x='250' y='140' fill='var(--ink)'>尖拱</text><text x='510' y='140' fill='var(--ink)'>飞扶壁</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "renaissance-style": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='120' width='520' height='200' fill='none' stroke='var(--accent)' stroke-width='2'/><line x1='380' y1='120' x2='380' y2='320' stroke='var(--muted)'/><rect x='120' y='270' width='520' height='50' fill='var(--accent-soft)' stroke='var(--muted)'/><text x='330' y='100' fill='var(--ink)'>对称与柱式</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "modernism": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='110' width='480' height='210' fill='none' stroke='var(--accent)' stroke-width='2'/><rect x='180' y='150' width='120' height='170' fill='var(--accent-soft)' stroke='var(--muted)'/><rect x='380' y='150' width='200' height='80' fill='none' stroke='var(--muted)'/><text x='200' y='90' fill='var(--ink)'>自由平面与体量</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "bauhaus": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='250' cy='200' r='70' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='360' y='130' width='120' height='140' fill='none' stroke='var(--muted)'/><polygon points='560,270 620,130 680,270' fill='none' stroke='var(--accent)'/><text x='200' y='100' fill='var(--ink)'>基本几何</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
    "postmodernism": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='120' width='480' height='200' fill='none' stroke='var(--line)'/><polygon points='140,120 300,120 260,160 180,160' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='380' y='140' width='100' height='100' fill='none' stroke='var(--muted)'/><text x='300' y='90' fill='var(--ink)'>历史符号与拼贴</text><text x='300' y='370' fill='var(--muted)'>示意图，非施工图</text></svg>",
}

SECTIONS = {
    "chiaroscuro": {
        "原理": "明暗法用光与影的对比塑造体积和空间深度，把视线引向受光区域。",
        "典型手法与适用条件": "以单一光源确定受光面与暗部，用过渡色阶表现转折；适用于强调戏剧性与体积感的画面。",
        "实例": "名称：文艺复兴至巴洛克的明暗法绘画实践（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "暗部过硬会失去透明感；极端对比需要兼顾细节可读性。" + REG,
        "一图": "见下方示意：受光面、暗部与投影的关系。",
        "待核实": "具体作品的设计者与年代待核实。",
    },
    "gothic": {
        "原理": "尖拱、肋拱与飞扶壁把荷载集中到柱墩，墙体因此可以大面积开窗。",
        "典型手法与适用条件": "以尖拱统一不同跨度的拱顶，用飞扶壁把侧推力外传；适用于追求高耸与光线的教堂空间。",
        "实例": "名称：哥特式大教堂（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "只模仿尖拱而忽视结构逻辑会失去整体性；石构尺寸与抗震须按当地规范校核。" + REG,
        "一图": "见下方剖面示意：尖拱与飞扶壁的荷载传递。",
        "待核实": "具体教堂的设计者与年代待核实。",
    },
    "renaissance-style": {
        "原理": "文艺复兴建筑以古典柱式、对称与几何比例表达理性与秩序。",
        "典型手法与适用条件": "以轴线对称组织立面，按柱式确定比例；适用于公共建筑与府邸。",
        "实例": "名称：文艺复兴府邸与教堂（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "脱离结构比例照搬柱式会流于布景；材料尺寸按当地规范校核。" + REG,
        "一图": "见下方立面示意：对称与柱式节奏。",
        "待核实": "具体建筑的设计者与年代待核实。",
    },
    "modernism": {
        "原理": "现代主义以功能、结构与新材料为基础，追求自由平面与简洁形式。",
        "典型手法与适用条件": "用框架结构释放墙体，按功能组织空间；适用于大批量建造与城市住宅。",
        "实例": "名称：现代主义住宅与公共建筑（类型性描述）；地点：全球；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "忽视地域气候会造成不适；结构与保温构造按当地规范校核。" + REG,
        "一图": "见下方体量示意：自由平面与结构框架。",
        "待核实": "具体建筑的设计者与年代待核实。",
    },
    "bauhaus": {
        "原理": "包豪斯把艺术、工艺与工业生产结合，主张形式服从功能与材料逻辑。",
        "典型手法与适用条件": "以基本几何形与标准化构件组织设计；适用于教学、家具与建筑实践。",
        "实例": "名称：包豪斯校舍与设计教育（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "过度标准化可能牺牲地方性与使用差异；构造细节按当地规范校核。" + REG,
        "一图": "见下方示意：基本几何与标准化构件。",
        "待核实": "具体作品的设计者与年代待核实。",
    },
    "postmodernism": {
        "原理": "后现代主义以历史符号、拼贴与戏谑回应现代主义的单一理性。",
        "典型手法与适用条件": "混合历史母题与通俗符号，强调与语境的对话；适用于公共与文化建筑。",
        "实例": "名称：后现代主义公共建筑（类型性描述）；地点：全球；设计者：不适用；年份：不适用。此处不复制图像。",
        "常见错误与限制": "符号堆砌可能流于表面；结构与防火按当地规范校核。" + REG,
        "一图": "见下方示意：历史符号与拼贴。",
        "待核实": "具体建筑的设计者与年代待核实。",
    },
}

SOURCES = {
    "chiaroscuro": ["wp-chiaroscuro", "wp-tenebrism"],
    "gothic": ["wp-gothic-architecture", "wp-architectural-style"],
    "renaissance-style": ["wp-renaissance-architecture", "wp-alberti"],
    "modernism": ["wp-modern-architecture", "wp-le-corbusier"],
    "bauhaus": ["wp-bauhaus", "wp-modern-architecture"],
    "postmodernism": ["wp-postmodern-architecture", "wp-architectural-style"],
}


def main():
    count = 0
    for path in sorted((ROOT / "entries").glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in doc.get("entries", []):
            eid = entry["id"]
            if eid not in SECTIONS:
                continue
            entry["level"] = "L2"
            entry["sections"] = SECTIONS[eid]
            entry["svg"] = [SVG[eid]]
            entry["sources"] = SOURCES[eid]
            entry["needs_verification"] = True
            entry["pending_notes"] = "实例的具体名称、设计者与年代待补充独立来源。"
            count += 1
            changed = True
        if changed:
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"upgraded={count}")


if __name__ == "__main__":
    main()
