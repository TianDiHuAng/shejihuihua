"""第38轮：写剩余 25 条补充条目，L2。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = "实际工程须按当地规范和专业设计人员的要求"

D = {
"split-primary": ("分离原色调色指以冷暖两套原色分别调色以扩大色域的做法。", "跨时期、全球（参见来源）。", "它用两组原色互补混色，减少色彩发灰。", "以暖红/冷红、暖蓝/冷蓝等成对原色分别调色。", "混色过多仍会发灰；需控比例。", ["wp-color-theory", "wp-primary-color"]),
"time-scenery": ("时序造景指借晨昏、晴雨、雪月等时间与气象变化成景。", "古代、中国（参见来源）。", "同一景物因时序不同而意境各异。", "设观景点并题名，捕捉雨雪晨昏的景致。", "依赖天时，非四季皆有。", ["wp-chinese-garden", "wp-garden-design"]),
"rock-garden": ("岩石园指以岩石与高山植物为主体的园林形式。", "跨时期、全球（参见来源）。", "它模拟高山岩生环境，展示耐旱植物。", "以堆石与排水良好的基质配置高山植物。", "排水不良会烂根；需专业配植。", ["wp-garden-design", "wp-landscape-design"]),
"earth-sheltered": ("覆土建筑指部分或全部覆土、以土体保温隔热的建筑。", "20世纪、全球（参见来源）。", "它以土壤蓄热使室内温度平稳、并融入地形。", "屋面或侧墙覆土，结合防水与采光井。", "防水失效会渗漏；构造须专业。", ["wp-architecture", "wp-sunken-courtyard"]),
"romanticism-style": ("浪漫主义建筑以情感、如画与异域风格为特征。", "文艺复兴至19世纪、欧洲（参见来源）。", "它追求如画轮廓与历史联想，反对新古典的理性。", "以哥特、东方等异域语汇与不规则体量营造如画感。", "拼贴失当会杂乱。", ["wp-architectural-style", "wp-history-of-architecture"]),
"futurism-style": ("未来主义建筑以速度、动态与新技术崇拜为特征。", "20世纪、欧洲（参见来源）。", "它以流线与动势表达对机器时代的向往。", "用斜面、动势线条与新材料的想象性表达。", "多为构想，落地困难。", ["wp-architectural-style", "wp-modern-architecture"]),
"expressionism-style": ("表现主义建筑以扭曲体量、雕塑感与情绪表达为特征。", "20世纪、欧洲（参见来源）。", "它以非几何的有机形体传递强烈情感。", "以扭曲、流塑的体量与砖砌细部表达情绪。", "形式自由带来结构与造价挑战。", ["wp-architectural-style", "wp-modern-architecture"]),
"structuralism": ("结构主义建筑以可生长、可组合的结构单元组织空间。", "20世纪、欧洲（参见来源）。", "它以模数单元与网格形成可扩展的秩序。", "以重复单元与网格按规则组合成整体。", "过度统一会单调。", ["wp-architectural-style", "wp-modern-architecture"]),
"korean-architecture": ("韩国建筑以木构、院落与自然融合的传统为特征。", "跨时期、东亚（参见来源）。", "它强调与地形相和的院落与温突采暖。", "以木构、院落与地面采暖组织居住空间。", "忽略气候与维护会失当。", ["wp-korean-architecture", "wp-architectural-style"]),
"southeast-asian-architecture": ("东南亚建筑以高脚屋、深檐与大出挑适应湿热气候为特征。", "跨时期、东亚（参见来源）。", "它以架空与通风应对潮湿与洪水。", "以高脚、深檐、通透墙体组织通风防潮。", "忽视湿热会导致霉变。", ["wp-architectural-style", "wp-vernacular-architecture"]),
"african-architecture": ("非洲建筑以土构、茅草与地域材料多样形态为特征。", "跨时期、全球（参见来源）。", "它就地取材、形态随气候与族群而异。", "以夯土、茅草与编织等本地材料建造。", "直接移植会破坏地域性。", ["wp-architectural-style", "wp-vernacular-architecture"]),
"latin-american-colonial": ("拉美殖民建筑混合欧洲巴洛克与本地工艺为特征。", "文艺复兴至19世纪、美洲（参见来源）。", "它以厚重立面与繁复装饰体现殖民与本土交融。", "以巴洛克立面结合本地材料与装饰工艺。", "装饰堆砌会失整体。", ["wp-architectural-style", "wp-history-of-architecture"]),
"brazilian-modernism": ("巴西现代主义以曲线体量、混凝土与地域气候回应为特征。", "20世纪、美洲（参见来源）。", "它用自由曲线与遮阳构件塑造热带现代性。", "以曲线混凝土、遮阳板与开放平面组织。", "忽视遮阳会过热。", ["wp-modern-architecture", "wp-architectural-style"]),
"mexican-modernism": ("墨西哥现代主义以壁画性、地域材料与纪念性体量为特征。", "20世纪、美洲（参见来源）。", "它把现代结构与本土艺术结合。", "以混凝土体量结合壁画与地域色彩。", "形式与功能脱节会失当。", ["wp-modern-architecture", "wp-architectural-style"]),
"shanxi-style": ("晋派建筑以厚重砖墙、窄院与防御性聚落为特征。", "古代、中国（参见来源）。", "它适应北方寒冷与商贾聚居，院落狭长高墙。", "以窄长院落、高墙与砖雕组织聚落。", "采光与排水需按规范。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"lingnan-style": ("岭南建筑以通风防潮、骑楼与轻巧装饰为特征。", "古代、中国（参见来源）。", "它以通透布局与遮阳应对湿热多雨。", "以天井、趟门、骑楼与灰塑组织通风防潮。", "防潮通风不当会霉变。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"hokkien-style": ("闽南建筑以红砖、燕尾脊与石雕为特征。", "古代、中国（参见来源）。", "它色彩鲜明、屋脊翘起，装饰繁丽。", "以红砖白石、燕尾脊与石雕木雕装饰。", "装饰过度会失结构逻辑。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"hakka-style": ("客家建筑以围屋、土楼等防御性集合住宅为特征。", "古代、中国（参见来源）。", "它以厚墙、单一入口与内院聚居防卫。", "以夯土厚墙、内向院落与单一门楼组织。", "尺度失当会阴暗潮湿。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"gan-style": ("赣派建筑以马头墙、天井与木构为特征。", "古代、中国（参见来源）。", "它以天井采光排水、马头墙防火。", "以天井、马头墙与木构架组织村落。", "防火与排水须按规范。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"yaodong": ("窑洞是黄土高原上依土崖挖筑的拱形生土居所。", "古代、中国（参见来源）。", "它利用黄土保温、冬暖夏凉。", "依崖挖拱、以土体保温并设炕采光。", "防水与结构失当有坍塌风险。", ["wp-yaodong", "wp-chinese-architecture"]),
"tibetan-architecture": ("藏式建筑以石木厚墙、平顶与碉楼为特征。", "古代、中国（参见来源）。", "它适应高原寒冷与强日照。", "以石砌厚墙、平顶与梯形窗组织。", "采光保温须专门处理。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"xinjiang-architecture": ("新疆建筑以土坯、拱券与庭院为特征。", "古代、中国（参见来源）。", "它适应干热气候、以厚墙与内院遮阳。", "以土坯拱券、内院与廊架组织。", "抗震与排水须按规范。", ["wp-chinese-architecture", "wp-vernacular-architecture"]),
"urban-planning-style": ("城市规划指对城市用地、交通与公共空间的整体安排。", "跨时期、全球（参见来源）。", "它协调功能分区、路网与开放空间。", "以分区、路网与公共空间系统组织城市。", "规划失当会拥堵或割裂。", ["wp-architectural-style", "wp-urban-design"]),
"raised-floor": ("架空层指建筑底层架空、留作公共或停车等用途的楼层。", "20世纪、全球（参见来源）。", "它释放地面、改善通风并容纳公共活动。", "底层以柱架空，留出通道、绿化或停车。", "私密与安全需管理。", ["wp-architecture", "wp-vernacular-architecture"]),
"acoustic-environment": ("声环境指空间中的声音条件，含隔声、吸声与混响。", "20世纪、全球（参见来源）。", "它影响听闻清晰度与舒适。", "以隔声构造、吸声材料与体形控制混响。", "忽视声学会有回声或噪声干扰。", ["wp-architecture"]),
}

SVGS = [
"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><rect x='120' y='130' width='{w}' height='140' fill='none' stroke='var(--accent)'/><line x1='110' y1='290' x2='650' y2='290' stroke='var(--ink)' stroke-width='2'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><circle cx='{cx}' cy='200' r='{r}' fill='var(--accent-soft)' stroke='var(--accent)'/><line x1='80' y1='200' x2='{cx2}' y2='200' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 400'><polygon points='{p1},{p2} {p3},120 {p4},{p2}' fill='none' stroke='var(--accent)'/><rect x='{p5}' y='250' width='120' height='60' fill='none' stroke='var(--muted)'/><text x='40' y='40' fill='var(--ink)'>{t}</text><text x='300' y='375' fill='var(--muted)'>示意图，非施工图</text></svg>",
]

cov = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))["entries"]
META = {r["id"]: r for r in cov}


def main():
    rows = []
    for i, (eid, (defn, tp, ov, method, limit, srcs)) in enumerate(D.items()):
        m = META[eid]
        tpl = SVGS[i % 3]
        if i % 3 == 0:
            svg = tpl.format(w=280 + (i * 4) % 160, t=m["title"])
        elif i % 3 == 1:
            svg = tpl.format(cx=300 + (i * 7) % 120, r=60 + (i * 3) % 40, cx2=250 + (i * 2) % 80, t=m["title"])
        else:
            svg = tpl.format(p1=180 + (i * 3) % 60, p2=300, p3=380, p4=560 - (i * 4) % 80, p5=320 + (i * 2) % 60, t=m["title"])
        rows.append({
            "id": eid, "title": m["title"], "level": "L2", "tier": m["tier"],
            "theme": m["theme"], "period": m["period"], "region": m["region"],
            "definition": defn, "time_or_place": tp, "overview": ov, "related": [],
            "sections": {"原理": defn + ov, "典型手法与适用条件": method,
                         "实例": "名称：%s的典型场景（类型性描述）；地点与设计者不适用。" % m["title"],
                         "常见错误与限制": limit + REG,
                         "一图": "见下方示意：%s的要点。" % m["title"],
                         "待核实": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"]},
            "svg": [svg], "sources": srcs, "needs_verification": True,
            "pending_notes": "「%s」的具体实例（名称、地点、设计者、年代）待补充独立来源。" % m["title"],
        })
    out = ROOT / "entries" / "batch-38.json"
    out.write_text(json.dumps({"unit_id": "batch-38", "title": "第38轮剩余补充条目", "entries": rows},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print("batch-38 written", len(rows))


if __name__ == "__main__":
    main()
