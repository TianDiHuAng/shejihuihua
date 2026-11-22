"""第40轮：修 batch-38 四条目 + 新增 proxemics 条目。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"
NEW = [
    ("xizang-tibetan-arch", "西藏传统建筑 — 西藏自治区人民政府", "https://www.xizang.gov.cn/xwzx_406/bmkx/202604/t20260401_532425.html", "西藏自治区人民政府", "官方机构", "石木混合结构、平顶、厚石墙小窗保温、收分墙抗震"),
    ("slxy-tibetan-arch", "藏式民居建筑 — 商洛学院", "https://jjc.slxy.edu.cn/info/1992/2454.htm", "商洛学院", "学术著作", "土石木碉楼、方形平顶、梯形小窗"),
    ("ihchina-tibetan", "藏族民居建筑技艺 — 中国非物质文化遗产网", "https://www.ihchina.cn/project_details/14699/", "中国非物质文化遗产网", "官方机构", "平顶、石木交错墙体、阶梯形"),
    ("leach-rock-garden", "Rock Garden — Leach Botanical Garden", "https://www.leachgarden.org/interpretive-signage/rock-garden", "Leach Botanical Garden", "官方机构", "岩石园土壤排水良好、贫瘠、岩生或荒漠植物"),
    ("vt-rock-garden", "Rock gardens and drought-tolerant landscapes — Virginia Tech", "https://news.vt.edu/articles/2024/09/ext-looking-for-a-landscape-design-that-withstands-drought-and-poor-soil.html", "Virginia Cooperative Extension", "学术著作", "岩石园模拟高山环境、需良好排水、耐旱耐贫瘠"),
    ("suzhou-ylj-time", "苏州园林的四季造景 — 苏州市园林和绿化管理局", "https://ylj.suzhou.gov.cn/szsylj/ylys/201903/ff62110521b940d294df634f18559b32.shtml", "苏州市园林和绿化管理局", "官方机构", "利用花木季节性构成四季不同景色、雾晨月夜"),
    ("ctnews-time", "四时风景不同 — 中国旅游新闻网", "https://www.ctnews.com.cn/xczm/content/2024-05/28/content_160715.html", "中国旅游报", "官方机构", "黄昏新月暮霭、雨打芭蕉、落雪等时序意境"),
    ("hts-xinjiang", "维吾尔族民居建筑技艺 — 和田市人民政府", "https://www.hts.gov.cn/lvyouguanguang/minzufengqing/1/content_465.html", "和田市人民政府", "官方机构", "黄粘土方形平顶、厚土墙拱顶、庭院与外廊"),
    ("tlf-xinjiang", "吐鲁番生土建筑 — 吐鲁番市人民政府", "https://www.tlf.gov.cn/tlfs/c106441/200910/64a7d5dc80b0412681082dd6a60187e6.shtml", "吐鲁番市人民政府", "官方机构", "土坯砌墙、拱形屋顶、外廊、葡萄架地下室避暑"),
    ("wp-proxemics", "Proxemics", "https://en.wikipedia.org/wiki/Proxemics", "Wikipedia", "学术著作", "近距学：人际距离与空间组织（经镜像核验）"),
    ("designingbuildings-proxemics", "Proxemics — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Proxemics", "Designing Buildings", "学术著作", "近距学在建成环境中的定义与应用"),
]
SVG_PROX = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='380' cy='200' r='40' fill='var(--accent-soft)' stroke='var(--accent)'/><circle cx='380' cy='200' r='90' fill='none' stroke='var(--muted)'/><circle cx='380' cy='200' r='150' fill='none' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>近距学：亲密—社交—公共距离</text><text x='300' y='385' fill='var(--muted)'>示意图，非施工图</text></svg>"


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({
            "id": sid, "title": title, "author": author, "type": typ,
            "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
            "note": f"访问于 2026-11-23，由核验子任务实抓 HTTP 200 并核对正文；{note}",
        })
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    p = ROOT / "entries" / "batch-38.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    for e in doc["entries"]:
        k = e["id"]
        if k == "tibetan-architecture":
            e["sources"] = ["xizang-tibetan-arch", "slxy-tibetan-arch", "ihchina-tibetan"]
            e["sections"]["原理"] = "高原寒冷多风，建筑以石木厚墙蓄热保温、以平顶兼作晾晒，碉楼式体量与收分墙增强稳定；成排梯形小窗减少散热并抗震。"
            e["sections"]["典型手法与适用条件"] = "以石木厚墙、方形平顶、碉楼体量与梯形窗组织，依山就势。"
            e["sections"]["待核实"] = "「藏式建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「藏式建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
        elif k == "rock-garden":
            e["sources"] = ["wp-garden-design", "leach-rock-garden", "vt-rock-garden"]
            e["sections"]["原理"] = "岩石园用沙砾与石块构成排水良好的贫瘠基质，模拟高山或干旱岩生环境，选耐旱耐瘠的岩生植物。"
            e["sections"]["典型手法与适用条件"] = "以粗砾排水层、置石与岩生植物配置，避免积水与肥力过高。"
            e["sections"]["待核实"] = "「岩石园」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「岩石园」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
        elif k == "time-scenery":
            e["sources"] = ["wp-chinese-garden", "suzhou-ylj-time", "ctnews-time"]
            e["sections"]["原理"] = "园林借花木季相与晨昏、雨雪、月夜等天时变化，使同一景在不同时间呈现不同意境。"
            e["sections"]["典型手法与适用条件"] = "按季选配花木并设观景点题名，捕捉雾晨、月夜、雨雪与四季变化。"
            e["sections"]["待核实"] = "「时序造景」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「时序造景」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
        elif k == "xinjiang-architecture":
            e["sources"] = ["hts-xinjiang", "tlf-xinjiang"]
            e["sections"]["原理"] = "干热气候下以土坯厚墙与拱形屋顶隔热蓄冷，内院、外廊与葡萄架、地下室提供荫凉与避暑。"
            e["sections"]["典型手法与适用条件"] = "以土坯拱券、内院、外廊（阿衣旺）与葡萄架组织。"
            e["sections"]["待核实"] = "「新疆建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
            e["pending_notes"] = "「新疆建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。"
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")

    # proxemics 新条目
    meta = {r["id"]: r for r in json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]}
    if "proxemics" in meta:
        m = meta["proxemics"]
        pe = {
            "id": "proxemics", "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": "近距学（Proxemics）研究人如何用距离与空间安排来调节社交互动。",
            "time_or_place": "20世纪、全球（参见来源）。",
            "overview": "它区分亲密、个人、社交与公共等距离，并把这一尺度用于室内与城市空间布局。",
            "related": ["human-scale", "spatial-perception"],
            "sections": {
                "原理": "人际互动有惯用的距离带：过近引起紧张、过远显得疏离，空间设计据此安排座位、通道与房间尺度。",
                "典型手法与适用条件": "按互动类型设定桌椅间距、通道宽度与半私密边界；适用于办公、餐饮与公共空间。",
                "实例": "名称：按社交距离布置的候车厅座椅（类型性描述）；地点与设计者不适用。",
                "常见错误与限制": "忽视文化差异与个体偏好会误判；具体尺寸须按规范与人群校核。" + REG,
                "一图": "见下方示意：亲密—社交—公共的距离带。",
                "待核实": "「近距学」的具体实例（名称、地点、设计者、年代）待补充独立来源。",
            },
            "svg": [SVG_PROX],
            "sources": ["wp-proxemics", "designingbuildings-proxemics"],
            "needs_verification": True,
            "pending_notes": "「近距学」的具体实例（名称、地点、设计者、年代）待补充独立来源。",
        }
        out = ROOT / "entries" / "batch-40.json"
        payload = {"unit_id": "batch-40", "title": "第40轮新增条目", "entries": [pe]}
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round40 applied")


if __name__ == "__main__":
    main()
