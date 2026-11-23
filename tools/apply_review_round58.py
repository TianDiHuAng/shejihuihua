"""第58轮：为 8 个中国画理论/技法条目补具名实例（16 源）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = [
    ("dpm-luoshenfu", "洛神赋图（宋摹）— 故宫名画记", "https://minghuaji.dpm.org.cn/paint/detail?id=69037b434240e1bbaa99067ca79e94f3", "故宫博物院", "官方机构", "顾恺之《洛神赋图》宋摹，以形写神、传神写照"),
    ("chinaculture-luoshenfu", "Chinese painting — ChinaCulture", "http://en.chinaculture.org/gb/en_artqa/2003-09/24/content_39739.htm", "ChinaCulture", "官方机构", "故宫藏《洛神赋图》，捕捉人物心境"),
    ("britannica-maxia", "Ma-Xia school — Britannica", "https://www.britannica.com/art/Ma-Xia-school", "Britannica", "权威百科", "马夏派边角山水，大面积留白、一隅构图"),
    ("chinaculture-mayuan", "Ma Yuan and Xia Gui — ChinaCulture", "http://en.chinaculture.org/gb/en_artqa/2003-09/24/content_39574.htm", "ChinaCulture", "官方机构", "马远夏圭由全景转为边角聚焦布局"),
    ("britannica-wangwei", "Wang Wei and scholar landscape — Britannica", "https://www.britannica.com/art/How-did-Wang-Wei-influence-the-tradition-of-scholar-landscape-painting", "Britannica", "权威百科", "王维 701–761，文人水墨山水，重个人表达"),
    ("chinaculture-wangwei", "Chinese painting spirit — ChinaCulture", "http://en.chinaculture.org/gb/en_artqa/2003-12/17/content_44510.htm", "ChinaCulture", "官方机构", "表达内在精神，画花不画全朵只取数瓣"),
    ("britannica-wudaozi", "Wu Daoxuan — Britannica", "https://www.britannica.com/biography/Wu-Daoxuan", "Britannica", "权威百科", "吴道子笔法富表现力、粗细变化，无确切实存作品"),
    ("chinaculture-wudaozi", "Wu Daoxuan — ChinaCulture", "http://en.chinaculture.org/gb/en_artqa/2003-09/24/content_39639.htm", "ChinaCulture", "官方机构", "吴道子笔法多变有力，《送子天王图》为代表"),
    ("dpm-xiaoxiang", "潇湘图 — 故宫名画记", "https://minghuaji.dpm.org.cn/paint/detail?id=fmfsfonhaf1fxv4dmh0h97cj5i5q6d3s&topicType=14", "故宫博物院", "官方机构", "（传）董源《潇湘图》山石坡脚用短披麻皴"),
    ("people-xiaoxiang", "董源与披麻皴 — 人民日报海外版", "https://paper.people.com.cn/rmrbhwb/html/2016-06/18/content_1688427.htm", "人民日报海外版", "学术著作", "董源创造重要山水技法披麻皴"),
    ("dpm-furong", "芙蓉锦鸡图 — 故宫博物院", "https://www.dpm.org.cn/collection/paint/230125.html", "故宫博物院", "官方机构", "（传）赵佶《芙蓉锦鸡图》，工致细丽、双钩法"),
    ("people-furong", "宋徽宗工笔花鸟 — 人民网", "https://culture.people.com.cn/n1/2016/1115/c1013-28860469.html", "人民网", "学术著作", "《芙蓉锦鸡图》宋徽宗工笔花鸟代表，绢本双勾重彩"),
    ("npm-poshui", "泼墨仙人 — 国立故宫博物院数位典藏", "https://digitalarchive.npm.gov.tw/opendata/Pub/Detail/14658?dep=P&mode=full", "国立故宫博物院", "官方机构", "梁楷《泼墨仙人图》减笔写意，约48.7×27cm"),
    ("rmzx-poshui", "梁楷泼墨仙人图 — 人民政协网", "https://www.rmzxw.com.cn/c/2016-10-17/1086460.shtml", "人民政协网", "学术著作", "《泼墨仙人图》减笔画代表作、大写意楷模"),
    ("sc-kumu", "苏轼枯木怪石图 — 四川发布", "https://www.scpublic.cn/news/getdetail/id?id=689450", "四川发布", "官方机构", "苏轼《枯木怪石图》水墨纸本手卷"),
    ("sansu-kumu", "苏轼木石图 — 三苏文化大数据库", "http://www.mssswhyjy.cn/sansu/xslw/detail?uid=1000000000000076999", "眉山三苏祠博物馆", "官方机构", "纸本墨笔画，石不作皴、微着墨"),
]
INST = {
 "qi-yun": ("名称：顾恺之《洛神赋图》（现存宋摹本）；地点：北京故宫博物院藏；作者：顾恺之（约 345–406）；年代：东晋（现存宋摹）。以形写神、传神写照。此处仅列名称、地点、作者与年代信息，不复制图像。", ["dpm-luoshenfu", "chinaculture-luoshenfu"], True, "两源直证“以形写神”与代表作，但未逐字使用“气韵生动”；概念归属为解读。"),
 "liubai": ("名称：马远、夏圭“马夏派”边角山水（代表《寒江独钓图》）；地点：中国（南宋画院）；作者：马远、夏圭；年代：约 1175–1210 年。以大面积留白、一隅取景著称。此处仅列名称、地点、作者与年代信息，不复制图像。", ["britannica-maxia", "chinaculture-mayuan"], True, "流派级留白由两源直证；单幅《寒江独钓图》第二独立来源不可得。"),
 "yijing": ("名称：王维文人水墨山水传统（以《辋川图》为代表）；地点：中国唐代；作者：王维（701–761）；年代：唐代。以简淡笔墨表达内在情思。此处仅列名称、地点、作者与年代信息，不复制图像。", ["britannica-wangwei", "chinaculture-wangwei"], True, "Britannica 直证王维与文人山水传统、ChinaCulture 直证重内在精神，但两源未共同点名《辋川图》。"),
 "bone-method": ("名称：吴道子《送子天王图》（传，宋摹；原作不存）；地点：原作已佚、传世为摹本；作者：相传吴道子（约 700–760）；年代：盛唐。笔法粗细转折、富有骨力。此处仅列名称、地点、作者与年代信息，不复制图像。", ["britannica-wudaozi", "chinaculture-wudaozi"], True, "吴道子无确切实存作品；实例为传本/摹本，已如实标注。"),
 "cunfa": ("名称：董源《潇湘图》卷（披麻皴）；地点：北京故宫博物院藏；作者：旧题/传董源（？—962，五代南唐）；年代：五代约 10 世纪。山石坡脚用短披麻皴。此处仅列名称、地点、作者与年代信息，不复制图像。", ["dpm-xiaoxiang", "people-xiaoxiang"], True, "作者为旧题/传董源，并存《河伯娶妇图》异名，无绝对纪年。"),
 "gongbi": ("名称：《芙蓉锦鸡图》轴；地点：北京故宫博物院藏；作者：（传）赵佶／画院画家御题画；年代：北宋 12 世纪初。以双钩重彩、工致细丽著称。此处仅列名称、地点、作者与年代信息，不复制图像。", ["dpm-furong", "people-furong"], True, "作者不可写徽宗亲笔（故宫引徐邦达说为画院御题画），已按传本标注。"),
 "xieyi": ("名称：梁楷《泼墨仙人图》；地点：国立故宫博物院（台北）藏；作者：传梁楷；年代：南宋约 13 世纪初。以减笔泼墨的大写意著称。此处仅列名称、地点、作者与年代信息，不复制图像。", ["npm-poshui", "rmzx-poshui"], True, "尺寸两源略有出入（约 48.7×27cm），真迹归属有争议，已按传本标注。"),
 "ink-wash": ("名称：苏轼《枯木怪石图》（《木石图》）；地点：原作于徐州萧县圣泉寺、现私人藏；作者：苏轼；年代：北宋约 11 世纪。以水墨纸本、笔墨无多见生趣。此处仅列名称、地点、作者与年代信息，不复制图像。", ["sc-kumu", "sansu-kumu"], True, "现为私人藏、真迹存疑，两源部分同源，不表述为逐字双源印证。"),
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
                e["needs_verification"] = keep
                e["sections"]["待核实"] = caveat if keep else "暂无已知待核实项。"
                e["pending_notes"] = caveat if keep else ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round58 applied")


if __name__ == "__main__":
    main()
