"""第53轮：为 8 个构图/视觉原理条目补具名实例。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("uni-visual-literacy", "Visual Literacy — University of Northern Iowa", "https://uni.edu/fabos/ml/readings/visual_literacy.html", "University of Northern Iowa", "学术著作", "三分法：元素置于交叉点；1938 柏林赛照片示例"),
    ("uwpress-nolli", "Landscape Journal — UW Press", "https://lj.uwpress.org/node/3090", "University of Wisconsin Press", "学术著作", "诺利地图为 figure-ground 最有影响实例：建成体/空地二元"),
    ("tudelft-figure-ground", "Figure-ground — TU Delft OCW", "https://ocw.tudelft.nl/course-readings/ways-distinguish-elements-complex-situation/", "TU Delft", "学术著作", "白=公共空间、黑=建成/私人空间，诺利图归纳建筑与公共空间"),
    ("britishmuseum-greatwave", "葛饰北斋经典藏品 — 大英博物馆", "https://britishmuseum.org.cn/blog/classic-collection-by-katsushika-hokusai", "大英博物馆", "官方机构", "《神奈川冲浪里》巨浪最高点、富士山渺小、几何构图"),
    ("christies-greatwave", "The Great Wave — Christie's", "https://www.christies.com.cn/zh/lot/katsushika-hokusai-1760-1849-kanagawa-oki-nami-ura-6525585/", "Christie's", "官方机构", "《神奈川冲浪里》富士山远景渺小"),
    ("designmuseum-tube", "London Transport — Design Museum", "https://designmuseum.org/london-transport", "Design Museum", "官方机构", "哈里·贝克地铁图：颜色区分、菱形换乘、放大中心区、简化"),
    ("tudelft-hierarchy", "Ways to distinguish elements — TU Delft OCW", "https://ocw.tudelft.nl/course-readings/ways-distinguish-elements-complex-situation/", "TU Delft", "学术著作", "信息层级：按乘客场景关注下一站/换乘站，另一层信息"),
    ("jstage-greatwave", "Golden rectangle in the Great Wave — J-STAGE", "https://www.jstage.jst.go.jp/article/jsgs1967/41/4/41_4_3/_article", "J-STAGE (JSGS)", "学术著作", "《神奈川冲浪里》存在黄金矩形、构成核心"),
    ("conncoll-greatwave", "Hokusai's Great Wave — Connecticut College", "https://diluo.digital.conncoll.edu/Asianart/editors-pick/hokusais-the-great-wave-2/", "Connecticut College", "学术著作", "富士山居中为锚点，浪曲线与斜向"),
    ("hermitage-redharmony", "Harmony in Red — Hermitage", "https://hermitagemuseum.org/digital-collection/28389?lng=en", "Hermitage Museum", "官方机构", "马蒂斯《红色和谐》1908，平面化、装饰性"),
    ("uen-matisse", "Matisse: Harmony in Red — UEN Pressbooks", "https://uen.pressbooks.pub/arth2720/chapter/matisse-harmony-in-red/", "UEN Pressbooks", "学术著作", "《红色和谐》强调画面平面性、压缩空间"),
    ("britannica-schoolathens", "How Raphael used perspective — Britannica", "https://www.britannica.com/biography/How-did-Raphael-use-perspective-to-organize-the-School-of-Athens", "Britannica", "权威百科", "《雅典学院》姿态引导视线至中心，透视汇聚点"),
    ("grinnell-schoolathens", "School of Athens — Grinnell College", "https://www.originsliberaleducation.sites.grinnell.edu/exhibits/show/origins/schoolofathens", "Grinnell College", "学术著作", "《雅典学院》线性透视、构图线框住主体"),
    ("unesco-forbidden", "Imperial Palaces of the Ming — UNESCO", "https://whc.unesco.org/en/list/439/", "UNESCO", "官方机构", "紫禁城中轴、对称布局、外朝前内朝后，1406–1420 朱棣建"),
    ("hkpm-forbidden", "Entering the Forbidden City — HKPM", "https://www.hkpm.org.hk/en/exhibition/entering-the-forbidden-city-architecture-collection-and-heritage", "香港故宫文化博物馆", "官方机构", "紫禁城建于北京中轴上"),
]
INST = {
 "rule-of-thirds": ("名称：柏林奥林匹克体育场敬礼照片；地点：德国柏林；设计者：摄影者不详；年份：1938 年 5 月 14 日。运动员腰线与看台线落在画面水平三分线上。此处仅列名称、地点、作者与年份信息，不复制图像。", ["uni-visual-literacy"], True, "仅单一机构来源（UNI）直证该作品的三分法运用；作品摄影者未署，待补第二独立来源。"),
 "figure-ground": ("名称：诺利地图（Pianta Grande di Roma）；地点：意大利罗马；设计者：詹巴蒂斯塔·诺利（Giambattista Nolli）；年份：1748 年。以黑白区分建成体与公共空地。此处仅列名称、地点、作者与年份信息，不复制图像。", ["uwpress-nolli", "tudelft-figure-ground"], False, ""),
 "visual-center": ("名称：《神奈川冲浪里》；地点：日本神奈川外海（远眺富士山）；设计者：葛饰北斋；年份：约 1831 年。视觉中心落在前景巨浪最高点，而非画面几何中心。此处仅列名称、地点、作者与年份信息，不复制图像。", ["britishmuseum-greatwave", "christies-greatwave"], True, "两源直证巨浪为焦点、富士山渺小，但未逐字使用“视觉中心”；概念为归纳。"),
 "hierarchy": ("名称：伦敦地铁示意图（Tube map）；地点：英国伦敦；设计者：哈里·贝克（Harry Beck）；年份：1931 年设计、1933 年出版。以颜色区分线路、菱形标换乘、放大中心区建立信息层级。此处仅列名称、地点、作者与年份信息，不复制图像。", ["designmuseum-tube", "tudelft-hierarchy"], False, ""),
 "leading-lines": ("名称：《神奈川冲浪里》；地点：日本神奈川外海；设计者：葛饰北斋；年份：约 1830–1832 年（Penn State OER 记 1831）。浪的曲线与斜向构成把视线引向富士山。此处仅列名称、地点、作者与年份信息，不复制图像。", ["jstage-greatwave", "conncoll-greatwave"], True, "两源直证黄金矩形与中央锚点，但未逐字使用“引导线”；概念为归纳。"),
 "simplification": ("名称：《红色和谐》（Harmony in Red）；地点：俄罗斯艾尔米塔什博物馆；设计者：亨利·马蒂斯；年份：1908 年。以平面化色块压缩三维空间。此处仅列名称、地点、作者与年份信息，不复制图像。", ["hermitage-redharmony", "uen-matisse"], False, ""),
 "visual-movement": ("名称：《雅典学院》；地点：梵蒂冈签字厅；设计者：拉斐尔；年份：1509–1511 年。人物姿态引导视线汇聚于中央的柏拉图与亚里士多德。此处仅列名称、地点、作者与年份信息，不复制图像。", ["britannica-schoolathens", "grinnell-schoolathens"], True, "Britannica 该页自述为 AI 生成（官方发布）；Grinnell 的视线句述配对壁画，未误植。"),
 "symmetry-layout": ("名称：北京故宫（紫禁城）；地点：中国北京中轴线；设计者：明成祖朱棣敕建（无单一建筑师记载）；年份：1406–1420 年。以中轴对称、外朝在前内朝在后布局。此处仅列名称、地点、作者与年份信息，不复制图像。", ["unesco-forbidden", "hkpm-forbidden"], False, ""),
}


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": None,
                                "note": f"访问于 2026-11-23，由核验子任务实抓 HTTP 200 并核对正文；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in INST:
                inst, srcs, keep, caveat = INST[e["id"]]
                e["sections"]["实例"] = inst
                for r in srcs:
                    if r not in e["sources"]:
                        e["sources"].append(r)
                if keep:
                    e["needs_verification"] = True
                    e["sections"]["待核实"] = caveat
                    e["pending_notes"] = caveat
                else:
                    e["needs_verification"] = False
                    e["sections"]["待核实"] = "暂无已知待核实项。"
                    e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round53 applied")


if __name__ == "__main__":
    main()
