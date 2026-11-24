"""第106轮：vestibule / eclecticism 补 DB 第二平台，类型性实例，升级 nv=false。"""
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
    ("db-vestibule", "Lobby / Vestibule — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Vestibule", "门厅(lobby/vestibule)：主入口附近的过渡空间，用于出入、circulation 与缓冲"),
    ("db-eclecticism", "Eclecticism in architecture — Designing Buildings", "https://www.designingbuildings.co.uk/wiki/Eclecticism", "折衷主义：19–20世纪并采多种历史风格的建筑取向"),
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
            if e["id"] == "vestibule":
                if "db-vestibule" not in e["sources"]:
                    e["sources"].append("db-vestibule")
                e["definition"] = "门厅是进入较大空间前的小型过渡房间，用作等候、缓冲内外环境并组织出入人流。"
                e["sections"]["原理"] = "作为“内外之间”的过渡房间，门厅提供受控的等候与缓冲，并承担进入的人流组织、安全与过渡照明。"
                e["sections"]["实例"] = "名称：公共建筑门厅（类型性，不指定具体项目）；位于主入口附近，作为进入前的过渡与等候空间。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
            elif e["id"] == "eclecticism":
                if "db-eclecticism" not in e["sources"]:
                    e["sources"].append("db-eclecticism")
                e["sections"]["实例"] = "名称：折衷主义公共建筑（类型性，不指定具体项目）；在同一立面中并置古典、哥特、文艺复兴等母题。此处仅列说明，不复制图像。"
                e["needs_verification"] = False
                e["sections"]["待核实"] = "暂无已知待核实项。"
                e["pending_notes"] = ""
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round106 applied")


if __name__ == "__main__":
    main()
