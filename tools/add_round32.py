"""第32轮：写 12 条未写条目（中国画技法组 + 对称布局/开敞），直接 L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

# id: (definition, time_or_place, overview, method, limit, sources)
DATA = {
"bone-method": ("骨法用笔指以有骨力的笔线塑造形体的用笔要求，是六法之一。", "古代中国（参见来源）。", "它强调线条的力度与结构，而非描摹表面。", "以中锋、提按与顿挫控制笔线粗细与力度，使形体有骨架。", "笔线软弱会使形体松散；用笔需与物象结构相符。", ["wp-six-principles-chinese-painting", "wp-chinese-painting"]),
"likeness-form": ("应物象形指按对象本来的形貌去描绘，是六法之一。", "古代中国（参见来源）。", "它要求形似，但需服从整体气韵。", "观察对象的比例与结构后落笔，先取大势再定细节。", "只求形似而失神会呆板；过分变形则失真。", ["wp-six-principles-chinese-painting", "wp-chinese-painting"]),
"color-according-type": ("随类赋彩指按物象类别施以相应色彩，是六法之一。", "古代中国（参见来源）。", "它不求条件色写实，而按类别与意象设色。", "按物象类别确定主色，以平涂与渲染表现色块。", "设色过艳会压过笔墨；色彩需与意境协调。", ["wp-six-principles-chinese-painting", "wp-chinese-painting"]),
"transmission-copy": ("传移模写指通过临摹前人名作学习技法，是六法之一。", "古代中国（参见来源）。", "它把临摹作为传承与习画的路径。", "对临、背临与摹写结合，先得其形再求其神。", "一味复制会失去创造；临摹须理解而非描抄。", ["wp-six-principles-chinese-painting", "wp-chinese-painting"]),
"ink-wash": ("水墨是以水墨浓淡表现物象的中国画形式。", "古代中国（参见来源）。", "它舍弃多彩，以墨分五色表现层次与气韵。", "以水的多少调出焦、浓、重、淡、清等墨阶，层层积染。", "墨色过死会板滞；水分失控会洇散失形。", ["wp-ink-wash-painting", "wp-chinese-painting"]),
"cunfa": ("皴法是山水画中表现山石纹理与体积的笔法体系。", "古代中国（参见来源）。", "不同皴法对应不同地质与质感。", "以披麻、斧劈等笔法依山石结构层叠皴擦。", "皴法套用不当会与山形脱节；需随对象变化。", ["wp-chinese-painting", "wp-ink-wash-painting"]),
"gongbi": ("工笔是以精细勾勒与层层设色为特征的中国画法。", "古代中国（参见来源）。", "它工整细腻，常用于人物、花鸟。", "先勾线定形，再以淡彩多次罩染，层层积色。", "过度描摹会僵硬；线色需协调统一。", ["wp-chinese-painting", "wp-ink-wash-painting"]),
"xieyi": ("写意是以简练笔墨抒写意趣的中国画法。", "古代中国（参见来源）。", "它重神韵与笔势，不拘形似细节。", "以阔笔泼墨、一次成形，重气势与虚实。", "笔墨失控会潦草；写意亦需结构支撑。", ["wp-chinese-painting", "wp-ink-wash-painting"]),
"xu-shi": ("虚实指画面中实景与空白、浓淡之间的相生关系。", "古代中国（参见来源）。", "它以虚衬实，使画面有呼吸与想象空间。", "以留白、淡墨与云雾处理虚处，实处以浓墨刻画。", "虚实失衡会壅塞或空洞；需与意境配合。", ["wp-chinese-painting", "wp-chinese-garden"]),
"landscape-painting": ("山水画以自然山川为题材，是中国画的主要门类。", "古代中国（参见来源）。", "它借山川寄托情怀，讲究可游可居的意境。", "以高远、深远、平远经营空间，配合皴法与水法。", "空间层次不清会平铺；须与笔墨气韵统一。", ["wp-chinese-painting", "wp-ink-wash-painting"]),
"symmetry-layout": ("对称布局以中轴两侧镜像组织建筑与院落，是中国传统建筑的常见秩序。", "古代中国（参见来源）。", "它以轴对称表达礼制与稳定。", "沿中轴布置主要建筑，两翼对称配置次要空间。", "地形不平时硬做对称代价高；需与功能协调。", ["wp-chinese-architecture", "wp-symmetry"]),
"openness": ("开敞指空间界面通透、与外部连续的处理方式。", "跨时期、全球（参见来源）。", "开敞使室内外视线与活动连成一体。", "以大面积开窗、柱廊与院落弱化边界。", "过度开敞会带来眩光与能耗；需兼顾私密与气候。", ["wp-architecture", "wp-courtyard"]),
}

SVG = {
"cn-ink": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 140 300 Q 260 120 420 220 T 640 140' fill='none' stroke='var(--accent)' stroke-width='4'/><path d='M 160 320 Q 300 220 460 300' fill='none' stroke='var(--muted)'/><text x='250' y='90' fill='var(--ink)'>笔墨层次与气脉</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"cn-layer": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='150' width='160' height='120' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='320' y='150' width='160' height='120' fill='none' stroke='var(--muted)'/><rect x='520' y='150' width='120' height='120' fill='none' stroke='var(--muted)'/><text x='250' y='120' fill='var(--ink)'>主次与虚实布局</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"axis-sym": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='380' y1='60' x2='380' y2='340' stroke='var(--accent)' stroke-dasharray='8 6'/><rect x='240' y='150' width='120' height='150' fill='var(--accent-soft)' stroke='var(--accent)'/><rect x='400' y='150' width='120' height='150' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='330' y='110' fill='var(--ink)'>中轴镜像</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"openness": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='120' width='200' height='180' fill='none' stroke='var(--accent)'/><line x1='340' y1='140' x2='600' y2='140' stroke='var(--muted)' stroke-dasharray='6 5'/><line x1='340' y1='280' x2='600' y2='280' stroke='var(--muted)' stroke-dasharray='6 5'/><text x='360' y='110' fill='var(--ink)'>界面向外开敞</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
}
CHOOSE = {
"bone-method": "cn-ink", "likeness-form": "cn-layer", "color-according-type": "cn-layer",
"transmission-copy": "cn-layer", "ink-wash": "cn-ink", "cunfa": "cn-ink",
"gongbi": "cn-ink", "xieyi": "cn-ink", "xu-shi": "cn-layer",
"landscape-painting": "cn-ink", "symmetry-layout": "axis-sym", "openness": "openness",
}

coverage = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in coverage}


def main():
    rows = []
    for eid, (definition, tp, ov, method, limit, srcs) in DATA.items():
        m = META[eid]
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": definition, "time_or_place": tp, "overview": ov,
            "related": [],
            "sections": {
                "原理": definition + ov,
                "典型手法与适用条件": method,
                "实例": "名称：%s的典型应用（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。" % m["title"],
                "常见错误与限制": limit + REG,
                "一图": "见下方示意图，仅表达关系。",
                "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
            },
            "svg": [SVG[CHOOSE[eid]]],
            "sources": srcs,
            "needs_verification": True,
            "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-32.json"
    out.write_text(json.dumps({"unit_id": "batch-32", "title": "第32轮中国画与空间条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-32 written", len(rows))


if __name__ == "__main__":
    main()
