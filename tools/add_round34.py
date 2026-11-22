"""第34轮：写 12 条风格史条目（罗马/罗曼/洛可可/新古典/新艺术/装饰艺术/国际风格/有机/风格派/哥特复兴/文艺复兴复兴/折衷主义），L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

D = {
"ancient-roman": dict(defn="古罗马建筑以拱券、穹顶与混凝土技术著称，并继承发展希腊柱式。", tp="古代、欧洲（参见来源）。", ov="罗马人用拱与穹顶覆盖大跨度空间，把希腊柱式转为装饰性立面语言。",
 prin="拱券把受力转为压力、混凝土使大跨与厚墙可行，因而能建浴场、万神殿式的穹顶空间。", method="以半圆拱、交叉拱与穹顶组织空间，柱式用于立面划分。",
 inst="名称：万神殿式穹顶建筑（类型性描述）；地点与设计者不适用。看穹顶与拱券如何形成大跨。", cap="见下方示意：拱券与穹顶的受力关系。", limit="忽视拱的侧推力会开裂；材料与抗震须按规范。", srcs=["wp-roman-architecture", "wp-classical-architecture"]),
"romanesque": dict(defn="罗曼式建筑以厚重墙体、半圆拱、小窗与墩柱为特征。", tp="中世纪、欧洲（参见来源）。", ov="它承重墙厚、开窗少，内部幽暗稳重，是哥特之前的过渡风格。",
 prin="以厚墙与墩柱承重并用半圆拱与筒拱，墙体承受大推力，故开窗受限、空间沉厚。", method="以半圆拱廊、筒拱与厚墩墙组织，小窗采光。",
 inst="名称：罗曼式教堂（类型性描述）；地点与设计者不适用。看厚墙与半圆拱廊。", cap="见下方示意：厚墙与半圆拱。", limit="采光不足与墙体开裂是常见问题；需按规范加固。", srcs=["wp-romanesque-architecture", "wp-architectural-style"]),
"rococo": dict(defn="洛可可建筑与装饰以轻盈曲线、柔和色彩和繁细装饰为特征。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="它比巴洛克更轻巧私密，多用于室内与府邸沙龙。",
 prin="以不对称的卷草曲线、浅色与金饰营造轻盈私密的室内氛围。", method="用灰泥卷草、镜面与浅色墙面装饰室内。",
 inst="名称：洛可可府邸沙龙（类型性描述）；地点与设计者不适用。看曲线与浅色如何显轻盈。", cap="见下方示意：曲线装饰与浅色调。", limit="装饰过密会繁琐；维护成本高。", srcs=["wp-rococo", "wp-architectural-style"]),
"neoclassical": dict(defn="新古典主义建筑回归古希腊罗马的秩序、对称与柱式。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="它反对洛可可的繁饰，以简洁几何与古典母题重建理性。",
 prin="以古典柱式、三角山花与对称体量表达理性与秩序，装饰克制。", method="按古典范式组织立面与平面，减少装饰。",
 inst="名称：新古典主义公共建筑（类型性描述）；地点与设计者不适用。看山花与柱式的秩序。", cap="见下方示意：三角山花与柱廊。", limit="照搬古典易僵化；需结合功能与结构。", srcs=["wp-neoclassical-architecture", "wp-architectural-style"]),
"art-nouveau": dict(defn="新艺术运动以自然曲线、铁艺与整体艺术设计为特征。", tp="20世纪、欧洲（参见来源）。", ov="它反对历史复古，从植物曲线与工艺中寻找新形式。",
 prin="以流动的植物曲线与铁艺把结构、装饰与室内统一为整体艺术。", method="用铁艺曲线、彩玻璃与整体室内设计。",
 inst="名称：新艺术风格住宅入口（类型性描述）；地点与设计者不适用。看铁艺曲线如何统摄装饰。", cap="见下方示意：植物曲线与铁艺。", limit="曲线装饰成本高、难维护；需与结构协调。", srcs=["wp-art-nouveau", "wp-architectural-style"]),
"art-deco": dict(defn="装饰艺术以几何化装饰、金属光泽与流线造型为特征。", tp="20世纪、全球（参见来源）。", ov="它把现代几何与奢华材料结合，流行于两次大战之间。",
 prin="以重复的几何母题、阶梯状体量与金属饰面表达现代性的华丽。", method="用几何图案、金属线条与流线体量装饰立面与室内。",
 inst="名称：装饰艺术风格电影院门厅（类型性描述）；地点与设计者不适用。看几何母题与金属线条。", cap="见下方示意：几何母题与阶梯体量。", limit="奢华饰面维护成本高；易过时。", srcs=["wp-art-deco", "wp-architectural-style"]),
"international-style": dict(defn="国际风格以体积而非体量、规则立面与少装饰为特征，是现代主义的国际化表达。", tp="20世纪、全球（参见来源）。", ov="它强调标准化与轻盈感，弱化地方装饰。",
 prin="以框架结构释放墙体、以规则网格与通透玻璃表达现代性。", method="用规则柱网、玻璃幕墙与自由平面组织。",
 inst="名称：国际风格办公楼（类型性描述）；地点与设计者不适用。看规则网格与玻璃立面。", cap="见下方示意：规则网格与通透立面。", limit="忽视气候会能耗高；需结合遮阳。", srcs=["wp-international-style", "wp-modern-architecture"]),
"organic-architecture": dict(defn="有机建筑主张建筑与自然、地形和使用者生活有机融合。", tp="20世纪、全球（参见来源）。", ov="它以内外连续、就地取材与流动空间回应场所。",
 prin="强调建筑像生物般与场地共生，空间流动、材料真实、形式顺应环境。", method="用流动平面、自然材料与融入地形的体量。",
 inst="名称：有机建筑住宅（类型性描述）；地点与设计者不适用。看室内如何向景观延展。", cap="见下方示意：体量与地形融合。", limit="形式自由带来造价与施工难题；需专业协同。", srcs=["wp-frank-lloyd-wright", "wp-modern-architecture"]),
"de-stijl": dict(nl="", defn="风格派以直线、矩形与原色块的抽象秩序为特征。", tp="20世纪、欧洲（参见来源）。", ov="它追求普遍秩序，把艺术简化为水平垂直与原色。",
 prin="以水平/垂直线与红黄蓝原色加黑白灰，追求普遍而理性的抽象秩序。", method="用网格、原色块与非对称平衡组织平面与立面。",
 inst="名称：风格派式室内与绘画（类型性描述）；地点与设计者不适用。看原色块与网格的关系。", cap="见下方示意：网格与原色块。", limit="严格抽象易冷硬；功能适配需调整。", srcs=["wp-de-stijl", "wp-architectural-style"]),
"revival-gothic": dict(defn="哥特复兴以重新采用中世纪哥特形式为特征。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="它借哥特尖拱与装饰表达浪漫与宗教感。",
 prin="以尖拱、飞扶壁与花窗等哥特语汇唤起历史与浪漫联想。", method="按哥特母题设计教堂与校园建筑。",
 inst="名称：哥特复兴教堂（类型性描述）；地点与设计者不适用。看尖拱与花窗的复现。", cap="见下方示意：尖拱与花窗。", limit="形式复古而结构未必匹配；需现代加固。", srcs=["wp-gothic-architecture", "wp-architectural-style"]),
"revival-renaissance": dict(defn="文艺复兴复兴以重拾文艺复兴的对称、柱式与穹顶为特征。", tp="文艺复兴至19世纪、欧洲（参见来源）。", ov="它在19世纪以文艺复兴语汇塑造庄重的公共建筑。",
 prin="以对称、圆拱、穹顶与水平檐口重建文艺复兴式的均衡与纪念性。", method="用对称体量、圆拱窗与穹顶组织公共建筑。",
 inst="名称：文艺复兴复兴式市政厅（类型性描述）；地点与设计者不适用。看对称与穹顶。", cap="见下方示意：对称体量与穹顶。", limit="语汇堆叠易失当；需功能匹配。", srcs=["wp-renaissance-architecture", "wp-architectural-style"]),
"eclecticism": dict(defn="折衷主义指在同一建筑中混合多种历史风格的做法。", tp="文艺复兴至19世纪、全球（参见来源）。", ov="它按需要选取不同风格语汇，常见于19世纪公共建筑。",
 prin="不固守单一风格，而按功能与表现需要混合古典、哥特等语汇。", method="在立面与室内选取不同历史母题组合。",
 inst="名称：折衷主义公共建筑（类型性描述）；地点与设计者不适用。看不同母题如何并置。", cap="见下方示意：多种风格母题并置。", limit="混搭失当会杂乱；需统一比例与秩序。", srcs=["wp-architectural-style", "wp-history-of-architecture"]),
}

SVG_A = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><line x1='120' y1='300' x2='640' y2='300' stroke='var(--ink)' stroke-width='3'/><line x1='200' y1='300' x2='200' y2='150' stroke='var(--accent)' stroke-width='14'/><line x1='330' y1='300' x2='330' y2='150' stroke='var(--accent)' stroke-width='14'/><line x1='460' y1='300' x2='460' y2='150' stroke='var(--accent)' stroke-width='14'/><polygon points='160,150 330,70 500,150' fill='var(--accent-soft)' stroke='var(--accent)'/><text x='250' y='350' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_B = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><path d='M 220 300 L 220 180 Q 380 40 540 180 L 540 300' fill='none' stroke='var(--accent)' stroke-width='4'/><line x1='160' y1='300' x2='600' y2='300' stroke='var(--ink)' stroke-width='3'/><text x='250' y='350' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG_C = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='140' y='120' width='480' height='180' fill='none' stroke='var(--accent)'/><line x1='260' y1='120' x2='260' y2='300' stroke='var(--muted)'/><line x1='380' y1='120' x2='380' y2='300' stroke='var(--muted)'/><line x1='500' y1='120' x2='500' y2='300' stroke='var(--muted)'/><line x1='140' y1='200' x2='620' y2='200' stroke='var(--muted)'/><text x='250' y='350' fill='var(--muted)'>示意图，非施工图</text></svg>"
SVG = {k: SVG_A for k in D}
for k in ["romanesque", "revival-gothic", "organic-architecture"]:
    SVG[k] = SVG_B
for k in ["international-style", "de-stijl", "eclecticism", "art-deco", "minimalism-architecture"]:
    if k in SVG:
        SVG[k] = SVG_C

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    rows = []
    for eid, f in D.items():
        m = META[eid]
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": f["defn"], "time_or_place": f["tp"], "overview": f["ov"],
            "related": [],
            "sections": {
                "原理": f["prin"], "典型手法与适用条件": f["method"],
                "实例": f["inst"], "常见错误与限制": f["limit"] + REG,
                "一图": f["cap"],
                "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
            },
            "svg": [SVG.get(eid, SVG_A)],
            "sources": f["srcs"],
            "needs_verification": True,
            "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-34.json"
    out.write_text(json.dumps({"unit_id": "batch-34", "title": "第34轮风格史条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-34 written", len(rows))


if __name__ == "__main__":
    main()
