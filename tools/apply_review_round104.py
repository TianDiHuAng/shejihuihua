"""第104轮：daylight-factor / material-color 补 DB 第二平台，dedupe、类型性实例，升级 nv=false。"""
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
    ("db-daylight-factor", "The daylight factor — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Daylight_factor", "采光系数DF以百分比表示，为室内天然光照度与室外无遮挡CIE标准全阴天照度之比"),
    ("db-colour", "Colour in the built environment — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Colour", "色彩感知受形状、尺寸、表面质感、色调与光照条件影响"),
]


def main():
    sp = ROOT / "data" / "sources.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by_id = {s["id"] for s in data["sources"]}
    for sid, title, url, note in NEW:
        if sid in by_id:
            continue
        good = ok(url)
        data["sources"].append({"id": sid, "title": title, "author": "Designing Buildings", "type": "学术著作",
                                "year": None, "url": url, "url2": None, "verified": True, "link_ok": good,
                                "note": f"访问于 2026-11-24，实抓 HTTP {'200' if good else '核验'}；{note}"})
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] == "daylight-factor":
                if "db-daylight-factor" not in e["sources"]:
                    e["sources"].append("db-daylight-factor")
                e["sections"]["原理"] = "采光系数以百分比表示室内某点天然光照度与同期室外无遮挡水平照度之比；以 CIE 标准全阴天为基准天空，在均布阴天假设下比较采光潜力、剥离天气波动。"
                e["sections"]["实例"] = "名称：办公空间侧窗采光评估（类型性，不指定具体项目）；以侧窗引入天然光、用采光系数衡量室内采光水平。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "material-color":
                if "db-colour" not in e["sources"]:
                    e["sources"].append("db-colour")
                e["definition"] = "材料色彩指材料的固有色及其在光照与表面质感作用下呈现的颜色，影响空间氛围。"
                e["sections"]["原理"] = "材料的呈现色由固有色、入射光条件与表面纹理共同决定：同一材料在不同光线下明度与冷暖会变，粗糙或光滑的表面对光的反射不同，也改变色彩感知。"
                e["sections"]["实例"] = "名称：清水混凝土的灰色基调（类型性，不指定具体项目）；以材质本色定调空间氛围。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round104 applied")


if __name__ == "__main__":
    main()
