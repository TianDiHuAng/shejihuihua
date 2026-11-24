"""第82c轮：差异化 5 条高相似度条目的定义/概述/原理，降低严口径相似度。"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = {
 "gongbi": dict(defn="工笔是先用细线勾定形廓、再以多层薄彩罩染的中国画技法，成品工整精致。",
   ov="它讲究线描的匀净与染色的层次，工序繁而慢，多见于人物与花鸟题材。",
   prin="工笔先以匀细的墨线立骨、定出轮廓，再以淡彩一遍遍罩染积色，靠遍数与色阶渐次求润泽，落笔不能急躁。"),
 "xieyi": dict(defn="写意是以阔笔简墨直取神韵、不拘形似的中国画风。",
   ov="它凭笔势与墨色的干湿浓淡一次成形，留给观者想象余地，常用于花鸟与人物。",
   prin="写意走的是减法：以最少的笔触概括对象神态，借浓淡干湿与留白营造气韵，重神采而非描摹细节。"),
 "revival-gothic": dict(defn="哥特复兴是18–19世纪重新起用中世纪哥特形式的建筑潮流。",
   ov="它用尖拱、飞扶壁与花窗唤起对中世纪的浪漫想象，多见于教堂与校园。",
   prin="哥特复兴把中世纪的尖拱、飞扶壁、花窗与垂直线条重新组合，借历史语汇营造宗教感与浪漫氛围。"),
 "revival-renaissance": dict(defn="文艺复兴复兴是19世纪重新采用文艺复兴对称、柱式与穹顶语汇的做法。",
   ov="它以圆拱、水平檐口与居中穹顶重塑均衡庄重的公共建筑形象。",
   prin="文艺复兴复兴偏爱对称平面、半圆拱窗、壁柱与居中穹顶，以水平檐口收束立面，重建文艺复兴式的均衡与纪念性。"),
 "eclecticism": dict(defn="折衷主义是在同一设计中混用多种历史风格语汇的取向。",
   ov="它不专守某一体式，按需要挑选古典、哥特或文艺复兴元素拼合。",
   prin="折衷主义不拘单一风格，按功能、造价与表现意图，从古典、哥特、文艺复兴等语汇中择取元素并置，靠比例与构图求统一。"),
}


def main():
    for p in ROOT.glob("entries/*.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        ch = False
        for e in doc.get("entries", []):
            if e["id"] in V:
                f = V[e["id"]]
                e["definition"] = f["defn"]
                e["overview"] = f["ov"]
                e["sections"]["原理"] = f["prin"]
                ch = True
        if ch:
            p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print("round82c applied")


if __name__ == "__main__":
    main()
