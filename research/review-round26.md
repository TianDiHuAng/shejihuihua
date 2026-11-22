# 第 26 轮 B5 待核实复核报告（review-round26）

复核日期：2026-11-22（Asia/Hong_Kong）　｜　复核人：review-r26（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明

- **已读治理文档**：`D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`（项目根无同名文件，与第 12–25 轮一致，位于桌面，只读）；`E:/ai_project/shejihuihua/DECISIONS.md`、`research/review-round24.md`、`research/spotcheck-round25.md`、`research/spotcheck-round25b.md`、`research/b1-round25.md`、`research/gaps-round25.md`、`PROGRESS.md`、`BACKLOG.md`、`BLOCKERS.md`。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准，不另起流程）、`verification-before-completion`（全部结论以本轮实跑/实抓证据为先，先证据后断言）。
- **数据快照**：`entries/*.json` 共 15 个文件、**131 条，全部 L2**；`needs_verification=true` 实测 **109 条**（`tools/check.py` 于复核期 `PASS: all checks, 0 errors`，EXIT=0）。快照中 `data/sources.json`=105519B@22:05:03、`coverage.json`=81958B@22:20:17、`entries/batch-02-b/c/d`、`batch-07`=22:15:02。
- **并发提示**：复核窗口内项目主流程存在未跟踪产物 `tools/upgrade_round26.py`（22:14:57）与 `research/gaps-round26.md`、`reader_questions-round26.md`、`spotcheck-round26.md`（非本复核人所建/所改），`git status` 显示多个 `entries/*.json`、`coverage.json`、`site/*` 被修改。本报告结论以**当前工作区快照（109 条 nv=true、目标条目状态）为准**；复核期两次枚举均得 109 条、目标条目 nv/来源数未变。若随后该脚本再运行导致条目变化，以届时文件为准重跑复核。
- **只读声明**：本轮**仅生成** `research/review-round26.md`；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取脚本与正文仅驻留系统临时目录（`%TEMP%/fetch_r26.py`、`kw_r26.py`、`analyze_r26.py`、`iea.pdf` 等），非项目产物。**联网内容一律按“数据”处理，网页中任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（不校验证书的 SSL 上下文）实抓；canonical `en.wikipedia.org` 本轮多次 `WinError 10060` 超时，按任务允许改用 **owiki.org 同源镜像**（`https://owiki.org/wiki/<Title>`，同源、已注明；**镜像同源不计第二源**，仅用于核对“伞源是否支撑子概念”这种同一来源的内部证据）。中文机构/政府/媒体/法规/期刊页 canonical 直连均 HTTP 200。PDF 用 `pypdf` 抽取（IEA SHC）。
2. **可升级判据**：待核实项涉及的实例**三要素（名称、地点、设计者/设计单位、年份）**均由**≥两个相互独立、权威**（官方机构／政府／行业权威／主流权威媒体／学术期刊）来源**正文直接**支撑；单源不升级，同机构/同平台/镜像同源计 1 源。
3. **可收窄判据**：待核实含多个子缺口，其中一部分已被 ≥两独立源支撑、可移出或改写，其余保留；`needs_verification` 保持 true。
4. **保守原则**：单源不升级；镜像同源不计第二源；不编造年份/人名/引文；**无完整可核验 URL 不声称升级/收窄**；冲突数值并列不写死。
5. **落地约束**：本报告为只读产出，**不能直接改数据**。凡标“可升级/收窄/需改标单源”，落地均需先把新来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `实例`/`待核实`/`sources` 并调整 `needs_verification`；登记前不得视为已改。

## 二、13 条“1 实质源 + 1 泛论伞源”逐条判定（本轮系统性重点）

> 结构定义：`source_count==2` 且其中恰 1 条为伞源（`wp-architecture`/`wp-architectural-style`/`wp-symmetry`/`wp-leading-line`/`wp-graphic-design`/`wp-visual-arts`）。全库精确命中 **13 条**（12 条 nv=true + `universal-design` nv=false），与第 25 轮体检“13 条”口径一致。
>
> **伞源实测（owiki 同源镜像，HTTP 200，均为“同一来源”内部核查，不作第二源）**：
> - `wp-architectural-style`（Architectural style）：`gothic`=2（仅“……‘Romanesque’ and ‘Gothic’ were initially coined to describe architectural styles……”与“from the Gothic rib vault to modern…”泛论举例）、`pointed arch`=0、`flying buttress`=0、`stained glass`=0 → **对哥特子概念零实质支撑**。
> - `wp-graphic-design`（Graphic design）：`wayfinding`=1（仅“practice areas for environmental graphic designers are wayfinding…”列举）、`navigation`=0 → **仅列实践领域，对定义/原理零支撑**。
> - `wp-symmetry`（Symmetry）：`axis`=2（“screw axis”数学轴、“vertical axis … like that present in the human face”对称反射轴）、`balance`=4（“harmonious and beautiful proportion and balance”“asymmetrical balance of social interactions”）→ **数学/知觉泛论，非建筑轴线、非构图视觉重量均衡**。
> - `wp-leading-line`（Leading line→重定向 Leading_lines）：owiki body 为**榜单/导航桩页**（len≈2696，无构图技法正文；“leading line”=2 均为标题导航）→ **无实质正文，第二源失效**。
> - `wp-visual-arts`（Visual arts）：`plein air`=0、`en plein air`=0、`landscape painting`=0（`impressionism`=4 为通史泛论）→ **对外光写生零支撑**。
> - `wp-architecture`（Architecture）：`service`=1（“offering or rendering professional services”＝建筑师执业服务）、`zoning`=1（“building codes and zoning laws”＝规划法规分区）、`circulation`=0、`wayfinding`=0、`drainage`=0 → **对“后勤服务动线”“功能分区”术语零实质支撑**。
>
> 结论：**6 条伞源对相应子概念均“零命中/仅泛论列举”**，系统性判断成立——“1 实质 + 1 伞源”结构实为**名义双源、实质单源（或双弱）**，违反 TASK“关键事实至少两个独立来源印证”与 D10。

| # | id | 伞源 | 实质源（实测支撑） | 伞源实测 | 结论 |
| --- | --- | --- | --- | --- | --- |
| 1 | `balance` | wp-symmetry | Composition (visual arts)：`balance`=3 | Symmetry 泛论（社会/数学均衡），非构图视觉重量 | **需改标单源+待核实**（删/换 wp-symmetry，实质＝Composition） |
| 2 | `geometry-symmetry` | wp-symmetry | Composition：`symmetry`=1（薄） | Symmetry 为数学泛论，非几何构图法 | **需改标单源+待核实**（并宜换更强构图源） |
| 3 | `visual-movement` | wp-leading-line | Composition：`movement`=8 | Leading_lines 为桩页，零技法正文 | **需改标单源+待核实** |
| 4 | `leading-lines` | wp-leading-line | Composition：`leading line`=0（镜像节略，待 canonical 复核） | 同桩页 | **需改标单源+换实质源+待核实**（Composition 对引导线支撑弱） |
| 5 | `rhythm-repetition` | wp-symmetry | Composition：`rhythm`=0（镜像节略） | 同数学泛论 | **需改标单源+换实质源+待核实**（rhythm 支撑弱） |
| 6 | `gothic` | wp-architectural-style | Gothic architecture：`pointed arch`=29/`flying buttress`=18/`rib vault`=30/`stained glass`=14 | 恰 0/0/1/0，仅泛论举例 | **需改标单源+待核实**（删/换伞源；实质强） |
| 7 | `postmodernism` | wp-architectural-style | Postmodern architecture：`ornament`=18/`Venturi`=23/`irony`=3 | 仅 `postmodern`=1 泛论 | **需改标单源+待核实**（实质强） |
| 8 | `plein-air` | wp-visual-arts | Outline of painting：`plein air`=1（薄） | `plein air`=0 | **需改标单源+换实质源+待核实**（实质源仅一次提及） |
| 9 | `axis` | wp-symmetry | Chinese architecture：`axis`=4/`symmetry`=6/`courtyard`=12 | axis=数学/反射轴，非建筑轴线 | **需改标单源+待核实**（实质强） |
| 10 | `service-route` | wp-architecture | Wayfinding：`service`=2（泛）、`logistics`=0、`back of house`=0 | service=执业服务，非后勤动线 | **需换实质源+待核实**（实质源也不能支撑“后勤服务动线”核心概念） |
| 11 | `wayfinding` | wp-graphic-design | Wayfinding：`navigate`=3/`signage`=7/`orientation`=2（定义原句支撑） | wayfinding=1 实践领域列举 | **需改标单源+待核实**（删/换伞源；实质强） |
| 12 | `functional-zoning` | wp-architecture | Interior design：`zoning`=0、`functional`=5（部分）、`space planning`=2 | zoning=规划法规分区 | **需改标单源+换源+待核实**（术语定义双源均弱；pending 已如实披露） |
| 13 | `universal-design`（nv=false） | wp-architecture | Universal design：定义/概述强 | Architecture 泛论，零支撑 | **结构注记**：已非待核实；建议清理装饰性伞源 wp-architecture，保留 wp-universal-design |

> 落地建议（统一）：上述 12 条 nv=true 条目应把 `pending_notes` 由“模板句(实例三要素待补)”改写为**如实单源披露**（如“核心依据单一权威来源《X》专条，第二独立来源待补；实例设计者/年代待补”）；伞源不支撑者删除或替换为真正论述该子概念的权威页；`needs_verification` 保持 true。其中 4、5、8、10、12 实质源本身偏弱，应优先“换实质源”。

## 三、抽样详核（gothic / wayfinding / drainage / spatial-organization / modernism / 动线类）

> 以下逐条给出实抓证据（完整 URL + 标题 + HTTP + 正文关键句），并据 §一判据下结论。

### 3.1 `gothic`（核心/风格）——**需改标单源（删/换伞源）；保持待核实**
- 条目：`definition`＝“以尖拱、肋拱与飞扶壁为特征的欧洲中世纪建筑风格”；`sources`＝`wp-gothic-architecture`＋`wp-architectural-style`；`pending_notes`＝“「哥特建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。”
- 实抓：`wp-gothic-architecture`（`https://owiki.org/wiki/Gothic_architecture`，200，len≈91956）“The defining design element of Gothic architecture is the **pointed arch**”；`pointed arch`=29、`rib vault`=30、`flying buttress`=18、`stained glass`=14 → **定义/原理强支撑（单一实质源）**。`wp-architectural-style`（`https://owiki.org/wiki/Architectural_style`，200）`pointed arch`=0、`flying buttress`=0、`gothic`=2 仅泛论举例 → **第二源无效**。
- **结论：需改标“单源+待核实”**（实质＝wp-gothic-architecture 强；wp-architectural-style 零支撑应删/换）；实例三要素仍缺 → **保持 nv=true**。（与第 25 轮 spotcheck 结论一致。）

### 3.2 `wayfinding`（重要/动线）——**需改标单源（删/换伞源）；保持待核实**
- 条目：定义＝“人在物理空间中借助标识、地图与视觉线索定向和导航的过程与设计”；`sources`＝`wp-graphic-design`＋`wp-wayfinding`。
- 实抓：`wp-wayfinding`（`https://owiki.org/wiki/Wayfinding`，200，len≈11472）“Wayfinding encompasses all of the ways in which people orient themselves in physical space and navigate from place to place”；`navigate`=3/`signage`=7/`orientation`=2 → **定义/原理强支撑（单一实质源）**。`wp-graphic-design`（`https://owiki.org/wiki/Graphic_design`，200）`wayfinding`=1（仅实践领域列举）、`navigation`=0 → **第二源极弱**。
- **结论：需改标“单源+待核实”**；实例三要素缺 → **保持 nv=true**。

### 3.3 `drainage`（核心/下沉空间）——**可收窄（保留 nv=true）**
- 条目：定义＝“引导雨水离开低处空间与铺装的组织方式”；`sources`（5）＝`wp-architecture`、`wp-sunken-courtyard`、`gdkcsj-sysu-gym`、`sysu-gym-news`、`ytsjk-sysu-drainage`；`pending_notes`＝“雨水排放工程参数待补充专业来源；建筑面积记载不一。”
- 实抓：
  - `ytsjk-sysu-drainage`（`https://www.ytsjk.cn/Book/S-7-5738`，200，len≈5324，《给水排水》胡雪利）：“在……天沟内……设置 **500mm(宽)×500mm(深) 集水坑**”；“屋面排水系统**重现期采用 50 年**”；“对于下沉式空间……需要靠**提升进行压力流排水**”；`排水`=47/`集水`=9/`重现期`=13/`下沉`=11/`压力流`=5 → **工程参数与原理已被这一专业源正文强支撑**。
  - `gdkcsj-sysu-gym`（`https://www.gdkcsj.com/m/caseInfo.aspx?id=1487`，200，len≈1583）：“设计单位：**北京市建筑设计研究院股份有限公司**；设计起止时间：**2014.04-2015.02**；项目面积：**25293㎡**；项目所在地区：**广东省珠海市**；整体总建筑面积 25293 平方米” → **实例（名称/地点/设计者/年份）单一权威源**。
  - `sysu-gym-news`（`https://www.sysu.edu.cn/news/info/2171/587221.htm`，200，len≈1560）：“建设**总建筑面积约 18000 平方米**的体育馆”“2017 年投入使用” → 与 25293㎡ **面积冲突**（来源互证名称/地点，但不给设计者）。
  - `wp-architecture`（`https://owiki.org/wiki/Architecture`，200）`drainage`=0；`wp-sunken-courtyard`（200，stub）`drainage`=0 → **两条维基源对排水零支撑（装饰性）**。
- **结论：可收窄**——(a)“工程参数（集水坑 500×500、重现期 50 年、压力流提升）”**已由 ytsjk 专业源正文直接支撑**，可从待核实移出（现 pending 该子项已属陈旧）；(b) **仍保留待核实**：实例设计者（北京院）与 2014–2015 设计年仅 `gdkcsj` **单源**，建筑面积 18000/25293 记载不一须并列；(c) 建议删除/替换 `wp-architecture`、`wp-sunken-courtyard` 两条零命中装饰源。因“设计者/年份”未达两独立源，**不整条升级，保持 nv=true**。

### 3.4 `spatial-organization`（核心/理论）——**保持（已升级，复核维持）**
- 现状：`needs_verification=false`、`pending_notes` 空；`实例`已为“萨伏伊别墅 Villa Savoye（法国普瓦西 Poissy；勒·柯布西耶与皮埃尔·让纳雷；1928–1931）……以坡道与连续流线组织‘建筑漫步’的串联式空间”；`sources`＝`wp-architecture`、`wp-architectural-theory`、`fondationlc-villa-savoye`、`villasavoye-promenade`。
- 实抓复核两官方源仍 200：`https://www.fondationlecorbusier.fr/en/work-architecture/achievements-villa-savoye-and-gardeners-lodge-poissy-france-1928-1931/`（200，标题“Le Corbusier and Pierre Jeanneret : the Villa Savoye - 1928-1931”，含 Poissy/1928-1931）、`https://www.villa-savoye.fr/en/discover/an-architectural-promenade`（200，标题“An architectural promenade | Villa Savoye”，正文“the double circulation… the continuity of the space… a ramp connects them”）。
- **结论：保持**——第 24 轮“可升级（Villa Savoye）”已落地且两独立官方源三要素（名称/地点/设计者/年份）与“建筑漫步/连续式空间组织”概念正文支撑，本轮复核维持。**提醒**：条目仍挂 `wp-architecture`（泛论伞源），建议清理，不影响 nv=false 结论。

### 3.5 `modernism`（核心/风格）——**保持（非伞源；实例三要素缺）**
- 条目：`sources`＝`wp-modern-architecture`＋`wp-le-corbusier`（均特定条目，**非伞源**）；`实例`＝“现代主义住宅与公共建筑（类型性描述）”；`pending_notes`＝“具体实例（名称、地点、设计者、年代）待补充独立来源。”
- 实抓：`wp-modern-architecture`（`https://owiki.org/wiki/Modern_architecture`，200）`modern architecture`=22/`function`=13/`le corbusier`=30；`wp-le-corbusier`（`https://owiki.org/wiki/Le_Corbusier`，200）`Le Corbusier`=201/`Villa Savoye`=10/`1887`=2/`1965`=5 → **定义/原理有特定条目支撑，非伞源问题**；但两源亦均为维基百科（非独立双源给同一具名实例三要素）。
- **结论：保持 nv=true**——定义可用，但“具名实例三要素 + 两独立权威源”未成，不升级。（若后续以萨伏伊/图根哈特等具名实例配“官方+权威媒体”双源，可仿 spatial-organization 升级；本轮不作为。）

### 3.6 动线“traffic 类”抽样：`service-route` / `pedestrian-flow` / `functional-zoning` / `circulation`
- `service-route`（重要/动线）：`sources`＝`wp-wayfinding`＋`wp-architecture`。实抓 wp-wayfinding（200）`service`=2（泛）、`logistics`=0、`back of house`=0；wp-architecture（200）`service`=1（“professional services”＝执业服务）。→ **双源均不支撑“后勤/清洁/配送非公众动线”核心概念**，属“实质源也弱”。**结论：需换实质源 + 保持 nv=true**。
- `pedestrian-flow`（核心/动线）：`sources`＝`wp-wayfinding`＋`wp-urban-design`（wp-urban-design 为泛论城市设计总条，非伞源清单内但同属泛论）。`pending`＝实例三要素待补。→ **保持 nv=true**（第二源泛论、实例三要素缺）。
- `functional-zoning`（重要/理论）：见 §二表 #12。`pending` 已如实写“Architecture 与 Interior design 未直接给出‘功能分区’术语定义；核心概念与实例数据均待补独立来源”。→ **需改标/换源 + 保持 nv=true**（披露已诚实）。
- `circulation`（核心/动线）：`needs_verification=false`，实例＝所罗门·R·古根海姆美术馆（美国纽约；赖特；1956–1959；连续螺旋坡道）；`sources`含 `nyc-lpc-guggenheim`＋`guggenheim-visitor-guide` 两独立官方（纽约市地标保护委员会 / 古根海姆访客指南）→ **保持（已升级）**；`wp-architecture`/`wp-wayfinding` 为泛论点缀，可清理。

## 四、可升级 / 收窄 / 保持 线索复核

### 4.1 `green-architecture`（核心/风格）——**可升级（候选；须先登记 3 个新来源、改写实例、面积并列）**
- 现状：`needs_verification=true`；`pending_notes`＝“设计者与 2018 设计年代仍单源，待补充；评价数据已多源。”；`实例`仍为占位“被动式节能公共建筑（类型性描述）”；`sources`（4）＝`wp-green-building`、`wp-sustainable-architecture`、`changzhou-gxzj`、`xinhua-js-green`（**注意：设计者所依据的 NJTech 源并未挂在条目 sources 内**）。

| # | 来源完整 URL | 标题 / 机构 | HTTP | 正文关键句 |
| --- | --- | --- | --- | --- |
| 1 | `http://www.jszb.com.cn/JSZB/YW_info/ZhongBiaoGS/ViewGSDetail.aspx?RowID=1077182&categoryNum=012` | 常州国展资产高新智汇中心新建项目的中标公告 — **江苏省建设工程招标网（政府招标平台）** | 200 | “项目名称：常州国展资产高新智汇中心新建项目；项目类型：**设计**；**中标单位名称：南京工业大学建筑设计研究院**；项目经理：李毅；**中标时间：2018年10月25日**；**工程地点：常州市新北区**；建筑面积 18897.00 平方米；标段含勘察/设计/采购/施工 EPC” |
| 2 | `https://ngsj.njtech.edu.cn/info/1064/1954.htm` | 常州国展资产高新智汇中心 — **南京工业大学建筑设计研究院有限公司（设计单位自站）** | 200 | “项目地点：江苏省常州市新北区；建筑面积：19291 平方米；**设计时间：2018 年**；三星级绿色建筑设计标识（2021）、2022 年度江苏绿色建筑创新示范工程一等奖…” |
| 3 | `http://mp.weixin.qq.com/s?__biz=MzY4OTA2NjgwNQ==&mid=2247518460&idx=1&sn=090755503f8cb70408f3933abfbe47e5&chksm=f2309e11748c74e8e969a804f1223e7cc96872cb0980eb96975d414df0848434f4a132f8bcfa` | 2022 年度江苏绿色建筑创新示范工程｜常州国展资产高新智汇中心 — **江苏省绿色建筑协会 / 绿色宜居生态保护（奖项主办方）** | 200 | “**建设单位：常州国展资产经营有限公司；设计单位：南京工业大学建筑设计研究院**；咨询单位：江苏超柏建设科技有限公司；建筑面积：18594㎡；绿建标识：三星级…（一等奖项目）” |
| 4 | `https://www.changzhou.gov.cn/gi_news/828161639281792` | 常州市美丽宜居城市建设综合试点实施方案 — **常州市人民政府** | 200 | “…推进…**常州国展资产高新智汇中心新建项目**…等绿色建筑实践…”（点名项目属绿色建筑实践；无设计者/年份） |
| 5 | `https://js.news.cn/20250407/5442dcc356fc4d69b0c26cf04381435d/c.html` | 一座新城背后的“绿色脉动”… — **新华网江苏频道** | 200 | “**绿色建筑三星项目高新智汇中心**…”（未带全名，疑同一项目并列注明） |

- **结论：可升级（候选）**——实例**三要素**（名称＝常州国展资产高新智汇中心；地点＝常州市新北区；设计者＝南京工业大学建筑设计研究院；年份＝2018 年设计/中标）由 **政府招标平台 jszb（#1，独立权威，一次同时给出设计者+2018+地点+名称）＋ 设计单位自站 NJTech（#2）＋ 奖项主办方公众号（#3）≥2 个相互独立权威源**正文直接支撑。
  - **落地步骤**：先把 #1、#2、#3 登记入 `data/sources.json`（verified=true），把 `实例` 由“类型性描述”改写为“常州国展资产高新智汇中心（江苏省常州市新北区；南京工业大学建筑设计研究院设计；2018 年）”，并置 `needs_verification=false`。
  - **冲突并列（不写死）**：建筑面积四源不一——NJTech 19291㎡、jszb 18897㎡、公众号 18594㎡（新华网/政府未给面积）→ 正文宜并列注明“各源记载不一（≈1.86–1.93 万㎡）”，不写死单值。
  - **注**：评价数据（三星级、2022 江苏绿色建筑创新示范工程一等奖）已多源（NJTech＋公众号＋新华网），可一并写实。

### 4.2 `glare`（重要/材料）——**保持（数值仍单源）**
- 现状：`sources`（5）＝`wp-daylighting-architecture`、`wp-architectural-lighting-design`、`iea-pbc-xining`、`elicht-pbc-xining`、`heuvan-pbc-xining`；`pending`＝“照度与 UGR 数值仅单一来源，待补充独立来源；面积记载不一。”
- 实抓：`https://iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf`（200，application/pdf，1.84MB，pypdf 抽取 10700 字）含“**475**”（照明功率密度/照度表多处）、“Xining Central Sub-branch of the People’s Bank of China”，且“Unified glare rating URG … R 19 19 - 25 **M 8 19 - 18**”→ **UGR 8–19 与 475 lux 均由该 IEA SHC 单一来源正文承载**。另抓 `https://www.elicht.com/view/101733.html`（200）`475`=0/`UGR`=0/面积“1万”；`http://www.heuvan.com/news_details.aspx?id=54`（200）`475`=0/`UGR`=0/面积“1.75”；`web_search` 未获同组 475 lux／UGR 8–19 的第二来源。
- **结论：保持 nv=true**——照度/UGR 仍单源（IEA），面积 1万/1.75万/≈1.8万并列；建议下轮取住建/科研或同行评议论文载同组数值方可移出。**提醒**：条目 source id 的 URL 误作 `https://ww.iea-shc.org/...`（少一个 w），应更正为 `https://iea-shc.org/...`。

### 4.3 `sunken-plaza`（核心/下沉空间）——**保持（顾如珍仍单源）**
- 现状：`sources`（4）＝`thepaper-jingan`、`jfdaily-jingan`、`wp-sunken-courtyard`、`people-sh-jingan`；`pending`＝“顾如珍负责建筑工程为单源，待补充独立来源；其他实例的设计者与年代待核实。”
- 实抓：`https://m.thepaper.cn/newsDetail_forward_2786200`（200，len≈7476）`顾如珍`=3，原句“卢济威的夫人——**同济设计院副总建筑师顾如珍负责了具体的建筑工程**”“顾如珍亲自负责推敲包括高差、细部材料在内的各种细节”→ **单源确证**。`https://www.jfdaily.com/wx/detail.do?id=1010081`（200）`顾如珍`=0；`https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html`（200）`顾如珍`=0、`1999`=2（仅证 1999-09-15 建成）。
- **结论：保持 nv=true**——`卢济威主持城市设计`、`1999 年落成` 多源可证，但 **“顾如珍负责建筑工程”仍仅澎湃可读单源**；期刊候选页（`it.alljournals.cn`→`aipub` 验证码壳）不可读，按“无完整可核验 URL 不升级/收窄”**不据此改动**。

## 五、其余 nv=true 条目（保持，95 条）

> 以下 95 条本轮未取得成对独立权威源正文直接支撑其**具名实例三要素**（或为单源已如实披露、或为多源但缺具名实例），按保守原则**保持 `needs_verification=true`**。其中结构需注意者已标注。

**A. 已如实披露单源（保持，模板正确）**：`rule-of-space`、`diagonal-composition`、`s-curve-composition`、`triangular-composition`、`screened-scenery`。

**B. 多源但缺具名实例三要素（保持）**：`courtyard`、`borrowed-scenery`、`framed-scenery`、`opposed-scenery`、`winding-path`、`natural-ventilation`、`leaked-scenery`、`vitruvian-triad`（+装伞源 wp-visual-arts，可清）、`chinese-architecture-style`（蒯祥单源+装伞源 wp-architectural-style，可清）、`perspective`、`sunken-courtyard`、`exit-sign`（另见第 25b 轮：time_or_place“20 世纪”无据，宜按 D14 如实披露）、`evacuation-route`。

**C. 普通“实例三要素待补”占位（保持）**：`linear-perspective`、`scattered-perspective`、`composition`、`proportion`、`color-theory`、`value`、`one-point-perspective`、`two-point-perspective`、`three-point-perspective`、`aerial-perspective`、`foreshortening`、`vanishing-point`、`horizon-line`、`rule-of-thirds`、`simplification`、`figure-ground`、`negative-space`、`visual-center`、`contrast-principle`、`hierarchy`、`hue`、`saturation`、`primary-colors`、`complementary-colors`、`color-contrast`、`warm-cool`、`curvilinear-perspective`、`golden-ratio`、`framing-composition`、`chiaroscuro`、`qi-yun`、`liubai`、`yijing`、`east-west-perspective-compare`、`east-west-space-compare`、`spatial-sequence`、`transition-space`、`interior-exterior-transition`、`damp-proofing`、`safety-guarding`、`material-texture`、`renaissance-style`、`mannerism`、`beaux-arts`、`light-well`、`vernacular-material`、`color-harmony`、`composition-placement`、`stack-ventilation`、`thermal-comfort`、`gestalt-organization-laws`、`color-psychology`、`environmental-psychology`、`hardscape-softscape`、`lighting-design`、`place-attachment`、`daylight-factor`、`mixed-mode-ventilation`、`material-durability`、`transparent-material`、`gray-space`、`enclosure`、`placemaking`、`space-syntax`、`pattern-language`、`form-follows-function`、`functionalism-architecture`、`biophilic-design`、`defensible-space-theory`、`rembrandt`、`tenebrism`、`plaza`、`atrium-architecture`。

> 说明：`exit-sign` 与 `plaza` 的 `time_or_place`/俗称问题（第 25b 轮已指出）仍属“形式一致、实质未披露”，建议随模板 pending 专项一并治理；本轮只读不落地。

## 六、汇总

- **nv=true 总数：109 条** ＝ 可升级 1 ＋ 可收窄 1 ＋ 需改标单源/换伞源 12 ＋ 保持 95（合计 109，经脚本核对相等）。
  - **可升级（建议整条置 nv=false）：1 条** — `green-architecture`（jszb 政府招标平台＋NJTech＋奖项主办方公众号 ≥2 独立源支撑实例三要素；须登记来源、改写实例、面积 18594/18897/19291 并列）。**均须先登记 `sources.json` 方可生效。**
  - **可收窄（保持 nv=true）：1 条** — `drainage`（工程参数已被 ytsjk 专业源支撑，可移出；设计者/2014–2015 设计年仍 gdkcsj 单源、面积 18000/25293 冲突保留；清装饰源 wp-architecture/wp-sunken-courtyard）。
  - **需改标“单源+待核实”/换伞源（保持 nv=true）：12 条** — `balance`、`geometry-symmetry`、`visual-movement`、`leading-lines`、`rhythm-repetition`、`gothic`、`postmodernism`、`plein-air`、`axis`、`service-route`、`wayfinding`、`functional-zoning`（其中 leading-lines/rhythm/plein-air/service-route/functional-zoning 实质源亦偏弱，须换实质源）。
  - **保持（nv=true）：95 条** — 见 §五（A 5＋B 13＋C 77；均缺成对独立源支撑的具名实例三要素，或单/弱源，或已有数据冲突待并列）。
  - **结构注记（nv=false，不计入 109）**：`universal-design` 仍挂装饰性伞源 `wp-architecture`，建议清理。
- **已升级复核维持**：`spatial-organization`（Villa Savoye，两官方源 200）、`circulation`（古根海姆，两官方源）——nv=false 复核有效。
- **保持单源结论**：`glare`（475 lux / UGR 8–19 仍仅 IEA）、`sunken-plaza`（顾如珍仍仅澎湃）。
- **本轮去重打开 URL：34 个**（成功 32 ＋ canonical 超时失败 2）；其中 owiki 同源镜像 15 个（**镜像同源不计第二源**）、机构/政府/媒体/法规/期刊 17 个；另 `web_search` 3 条 query。
- **数据/冲突提示（不写死）**：green-architecture 面积 18594/18897/19291 并列；drainage 面积 18000/25293 并列、概念实质单源 ytsjk；glare 面积 1万/1.75万/≈1.8万并列、数值单源；`iea-pbc-xining` URL 误作 `ww.iea-shc.org` 应更正。

### 本报告实际打开/请求的 URL 一览

**owiki 同源镜像（HTTP 200；同源，不计第二源，仅作伞源内部核查/实质源核对）：**
1. `https://owiki.org/wiki/Architectural_style` — 200 — Architectural style
2. `https://owiki.org/wiki/Graphic_design` — 200 — Graphic design
3. `https://owiki.org/wiki/Symmetry` — 200 — Symmetry
4. `https://owiki.org/wiki/Leading_line`（→`/wiki/Leading_lines`）— 200 — Leading lines（桩页，无技法正文）
5. `https://owiki.org/wiki/Visual_arts` — 200 — Visual arts
6. `https://owiki.org/wiki/Architecture` — 200 — Architecture
7. `https://owiki.org/wiki/Composition_(visual_arts)` — 200 — Composition (visual arts)
8. `https://owiki.org/wiki/Gothic_architecture` — 200 — Gothic architecture
9. `https://owiki.org/wiki/Postmodern_architecture` — 200 — Postmodern architecture
10. `https://owiki.org/wiki/Chinese_architecture` — 200 — Chinese architecture
11. `https://owiki.org/wiki/Outline_of_painting` — 200 — Outline of painting
12. `https://owiki.org/wiki/Wayfinding` — 200 — Wayfinding
13. `https://owiki.org/wiki/Interior_design` — 200 — Interior design
14. `https://owiki.org/wiki/Modern_architecture` — 200 — Modern architecture
15. `https://owiki.org/wiki/Le_Corbusier` — 200 — Le Corbusier

**机构 / 政府 / 媒体 / 法规 / 期刊（canonical，HTTP 200）：**
16. `http://www.jszb.com.cn/JSZB/YW_info/ZhongBiaoGS/ViewGSDetail.aspx?RowID=1077182&categoryNum=012` — 200 — 常州国展资产高新智汇中心新建项目的中标公告（江苏省建设工程招标网）
17. `https://ngsj.njtech.edu.cn/info/1064/1954.htm` — 200 — 常州国展资产高新智汇中心（南京工业大学建筑设计研究院）
18. `https://ngsj.njtech.edu.cn/info/1013/1007.htm` — 200 — 我院中标常州国展资产高新智汇中心工程总承包项目（2018-10-25）
19. `https://www.changzhou.gov.cn/gi_news/828161639281792` — 200 — 常州市美丽宜居城市建设综合试点实施方案（常州市人民政府）
20. `https://js.news.cn/20250407/5442dcc356fc4d69b0c26cf04381435d/c.html` — 200 — 解码常州高铁新城 ESG 路径（新华网江苏）
21. `http://mp.weixin.qq.com/s?__biz=MzY4OTA2NjgwNQ==&mid=2247518460&idx=1&sn=090755503f8cb70408f3933abfbe47e5&chksm=f2309e11748c74e8e969a804f1223e7cc96872cb0980eb96975d414df0848434f4a132f8bcfa` — 200 — 2022 年度江苏绿色建筑创新示范工程｜常州国展资产高新智汇中心（江苏省绿色建筑协会）
22. `https://www.ytsjk.cn/Book/S-7-5738` — 200 — 中山大学体育馆排水及管线综合设计分析（《给水排水》胡雪利）
23. `https://www.gdkcsj.com/m/caseInfo.aspx?id=1487` — 200 — 中山大学珠海校区体育馆（广东省工程勘察设计行业协会）
24. `https://www.sysu.edu.cn/news/info/2171/587221.htm` — 200 — 中山大学珠海校区体育馆（中山大学新闻网，2014-11-25，约 18000㎡）
25. `https://iea-shc.org/Data/Sites/1/publications/CN-Peoples-Bank-of-China.pdf` — 200（application/pdf，1.84MB，pypdf）— Retrofit of office lighting, People’s Bank of China Xining（IEA SHC）
26. `https://m.thepaper.cn/newsDetail_forward_2786200` — 200 — “魔都”新生：同济大学与静安寺广场和南京路步行街的修建（澎湃新闻·私家历史）
27. `https://www.jfdaily.com/wx/detail.do?id=1010081` — 200 — 卢济威教授：中国现代城市设计创始者之一…（解放日报·上观）
28. `https://sh.people.com.cn/BIG5/n2/2024/0319/c134768-40780072.html` — 200 — 上海静安寺广场焕新启用（人民网上海）
29. `https://www.fondationlecorbusier.fr/en/work-architecture/achievements-villa-savoye-and-gardeners-lodge-poissy-france-1928-1931/` — 200 — Le Corbusier and Pierre Jeanneret: the Villa Savoye - 1928-1931（Fondation Le Corbusier）
30. `https://www.villa-savoye.fr/en/discover/an-architectural-promenade` — 200 — An architectural promenade | Villa Savoye（CMN）
31. `https://www.elicht.com/view/101733.html` — 200 — 中国人民银行西宁中心支行照明改造（云知光；475/UGR=0，面积“1万”）
32. `http://www.heuvan.com/news_details.aspx?id=54` — 200 — 中国人民银行西宁中心支行照明案例（恒亦明；475/UGR=0，面积“1.75万”）

**失败 / 不可达（2 个，不计证据）：**
- `https://en.wikipedia.org/wiki/Architectural_style` — 超时（`WinError 10060`）
- `https://en.wikipedia.org/wiki/Composition_(visual_arts)` — 超时（`WinError 10060`）

> 另：`web_search` 3 条 query（green 设计者第二源 / 西宁 475·UGR / 静安寺顾如珍）。canonical 维基超时，英文维基正文一律以 owiki 同源镜像核对（已注明，镜像同源不计第二源）。**保守原则声明**：单源不升级；镜像同源不计第二源；同机构/同平台转载计 1 源；不可读摘要页不据以升级/收窄；无完整可核验 URL 不声称升级；冲突数值并列。**本报告仅给结论与证据，未修改任何条目数据或其它文件（本文件为唯一产出）。**

---

### 机器可读汇总

```
ROUND=26
REVIEWER=review-r26
MODE=B5-pending-review(read-only)
LIBRARY={"entries_files":15,"entries":131,"levels":{"L2":131},"needs_verification_true":109,"needs_verification_false":22}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SNAPSHOT={"sources.json":"105519B@22:05:03","coverage.json":"81958B@22:20:17","batch-02-b/c/d,batch-07":"22:15:02","concurrency":"untracked tools/upgrade_round26.py + gaps/reader_questions/spotcheck-round26.md (not mine)"}
UMBRELLA_SOURCES=["wp-architecture","wp-architectural-style","wp-symmetry","wp-leading-line","wp-graphic-design","wp-visual-arts"]
UMBRELLA13=["balance","geometry-symmetry","visual-movement","leading-lines","rhythm-repetition","gothic","postmodernism","plein-air","axis","service-route","wayfinding","universal-design(nv=false)","functional-zoning"]
UMBRELLA_ZERO_HIT={"wp-architectural-style":"gothic generic only (pointed arch=0/flying buttress=0)","wp-graphic-design":"wayfinding=1 practice list (navigation=0)","wp-symmetry":"axis=screw/reflection, balance=social/math (not arch/composition)","wp-leading-line":"stub/listing page, no technique text","wp-visual-arts":"plein air=0","wp-architecture":"service=professional services, zoning=building code, circulation/wayfinding/drainage=0"}
CLASSIFICATION={"upgrade":["green-architecture"],"narrow":["drainage"],"relabel_single_or_swap_umbrella":["balance","geometry-symmetry","visual-movement","leading-lines","rhythm-repetition","gothic","postmodernism","plein-air","axis","service-route","wayfinding","functional-zoning"],"keep":95,"sum_109":true}
UPGRADE_EVIDENCE_green_architecture={"instance":"常州国展资产高新智汇中心 / 常州市新北区 / 南京工业大学建筑设计研究院 / 2018","independent_sources":["jszb.com.cn 中标公告(gov) 200 [designer+2018+place+name]","ngsj.njtech.edu.cn/info/1064/1954.htm 200 [designer+2018]","mp.weixin 江苏省绿色建筑协会 200 [designer+name+place]"],"area_conflict":"19291 vs 18897 vs 18594 (not fixed)","action":"register sources -> rewrite instance -> nv=false"}
NARROW_EVIDENCE_drainage={"params_sourced_by":"ytsjk.cn 200 [集水坑500x500/重现期50年/压力流]","instance_single_source":"gdkcsj.com 200 [北京院/2014.04-2015.02/25293]","area_conflict":"18000(sysu) vs 25293(gdkcsj)","decorative_sources":["wp-architecture","wp-sunken-courtyard (drainage=0)"],"action":"move params out; keep designer/year single + area conflict; keep nv=true"}
HOLD_SINGLE_SOURCE={"glare":"475 lux & UGR 8-19 only IEA PDF (elicht/heuvan 475=0/UGR=0); area 1万/1.75万/1.8万","sunken-plaza":"顾如珍 负责建筑工程 only thepaper (jfdaily/people 顾如珍=0); 1999 multi"}
ALREADY_UPGRADED_OK={"spatial-organization":"Villa Savoye, 2 official 200","circulation":"Guggenheim, 2 official"}
OPENED_URLS={"dedup_total":34,"success":32,"owiki_mirror":15,"institutional":17,"canonical_timeout":2,"web_search_queries":3}
VERDICT="109 nv=true = upgrade1(green-architecture) + narrow1(drainage) + relabel_umbrella12 + keep95; 6 umbrella sources zero-hit confirmed; glare/sunken-plaza stay single; spatial-organization/circulation maintain upgraded"
READONLY="only wrote research/review-round26.md; no other file changed; no git commit"
```

*（报告完）*
