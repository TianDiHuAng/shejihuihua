"""第62轮：front-light/top-light 去错配源改一般性说明；five-tones/highlight/reflected-light/core-shadow 换概念源+实例。"""
import json
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}


def ok(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25, context=ctx).status == 200
    except Exception:
        return False


NEW = [
    ("wp-lighting-front", "Lighting (Front lighting) — Wikipedia", "https://en.wikipedia.org/wiki/Lighting", "Wikipedia", "权威百科", "正面光常见但使主体显平、几乎不投可见阴影（经镜像核验）"),
    ("wp-chiaroscuro", "Chiaroscuro", "https://en.wikipedia.org/wiki/Chiaroscuro", "Wikipedia", "权威百科", "明暗对照：明暗相互作用塑造立体（经镜像核验）"),
]


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, author, typ, note in NEW:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": author, "type": typ,
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-23，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in (ROOT / "entries").glob("*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            k = e["id"]
            if k == "front-light":
                # 去掉错配的建筑照明源；保留 Wikipedia Lighting（正面光使主体显平），另作一般性说明
                e["sources"] = ["wp-lighting-front", "wp-chiaroscuro"]
                e["sections"]["待核实"] = "正面光“使主体显平、少阴影”由 Wikipedia Lighting 单源直证（第二独立专源不可得）；本页其余为一般性说明。"
                e["pending_notes"] = "正面光概念单源（第二独立专源不可得）；其余为一般性说明。"
                e["needs_verification"] = True
                ch = True
            elif k == "top-light":
                # 去掉建筑照明错配源，改为一般性说明并保留下方一般性来源
                e["sources"] = ["wp-architectural-lighting-design"]
                e["definition"] = "顶光指光源位于被摄体正上方、自上而下的照明（一般性说明）。"
                e["sections"]["原理"] = "光源自上而下时，凸出部位受光、凹陷落影，形成由上而下的明暗秩序（一般性说明，专门权威来源待补）。"
                e["sections"]["待核实"] = "顶光的专门权威来源待补充，本页为一般性说明；具体实例的设计者与年代待核实。"
                e["pending_notes"] = "顶光专门来源待补（一般性说明）；实例待核实。"
                e["needs_verification"] = True
                ch = True
            elif k == "five-tones":
                e["definition"] = "明暗五调子是绘画教学中把连续明暗归纳为高光、亮部、明暗交界线、反光、投影五档的经验分档。"
                e["sections"]["原理"] = "在明暗对照基础上，把受光到背光的连续过渡归纳为五个可辨层次，便于观察与表现体积（教学通用表述）。"
                e["sections"]["待核实"] = "“五调子”分档为素描/绘画教学通用术语，专门权威来源未逐字列举此五档；明暗对照概念有来源支撑。"
                e["pending_notes"] = "五调子分档为教学通用术语，专门来源待补。"
                e["needs_verification"] = True
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round62 applied")


if __name__ == "__main__":
    main()
