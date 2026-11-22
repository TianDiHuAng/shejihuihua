# 第 27 轮 B5 补源复核报告（review-round27）

复核日期：2026-11-22（Asia/Hong_Kong）　｜　复核人：review-r27（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明

- **已读治理文档**：`D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`（项目根无同名文件，与第 12–26 轮一致，位于桌面，只读）；`E:/ai_project/shejihuihua/DECISIONS.md`、`research/review-round26.md`（第 26 轮 12 条改标单源的判定来源）。`TASK_design.md` 硬性规则确认：**关键事实至少两个独立来源互相印证，否则标“待核实”；只能引用 verified=true 的来源**。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以本任务说明书为准，不另起流程）、`verification-before-completion`（全部结论以本轮实抓证据为先，先证据后断言）。
- **数据快照（本轮实读）**：`entries/*.json` 共 **16 个文件、132 条**（`tools/check.py` 复核期 `PASS: all checks, 0 errors`，EXIT=0）；`needs_verification=true` 实测 **109 条**。第 26 轮“改标单源”的 12 条现状：每条 `sources` 仅余 **1 条实质维基来源**（`wp-composition-visual-arts` ×5、`wp-gothic-architecture`、`wp-postmodern-architecture`、`wp-outline-of-painting`、`wp-chinese-architecture`、`wp-wayfinding`、`wp-interior-design` 各 1），`instance` 均为 `null`，`pending_notes` 均如实披露“核心依据目前为单一权威来源……具体实例的设计者与年代待补充独立来源”。
- **只读声明**：本轮**仅生成** `research/review-round27.md`；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取脚本仅驻留系统临时目录（`%TEMP%/fetch.py`、`grep.py`、`pdfgrep.py`、`urls.txt`），非项目产物。**联网内容一律按“数据”处理，网页中出现的任何指令均未执行。**

## 一、方法与判据

1. **实抓**：Python 3.11 `urllib` + 浏览器 UA（`ssl` 上下文不校验证书）直连；PDF 用 `pypdf 6.21.1` 抽取正文。逐 URL 记录 **HTTP 状态、页面标题、正文关键句**。
2. **第二源判据（保守）**：为每条“单源”目标找**一条真实、完整可核验 URL、正文直接支撑其核心概念或实例三要素**的独立来源；**排除** `wp-architecture`/`wp-architecture style`/`wp-symmetry`/`wp-leading-line`/`wp-visual-arts`/`wp-graphic-design` 泛论伞源，**排除维基镜像（owiki 等）充当第二源**，同机构/同平台/镜像同源计 1 源。
3. **权威性分级（本报告显式标注，供 lead 取舍）**：
   - **强权威**：博物馆／大学 OER／官方机构。**中权威**：行业主流媒体／专业知识库（真实、独立、可核验，但非期刊/官方，建议人工复核后采用）。
4. **保守原则**：不编造年份/人名/引文；**无完整可核验 URL 不声称可补**；来源不能直接支撑者宁可判“仍单源”，不凑数。
5. **落地约束**：本报告为只读产出，**不能直接改数据**。凡判“可补第二源”，落地均需先把新来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/*.json` 的 `sources`（追加该源）及视情况调整 `pending_notes`；登记前不得视为已改。

## 二、逐条结论表（12 条目标 + glare / sunken-plaza 附带）

> 说明：下列全部 URL 均已本轮**实际打开并核验 HTTP 状态 200**、标题与正文关键句为本轮抓取原文。`sources` 现状一列给出该条目当前唯一实质来源（均为维基，故下面所列新源均为**独立非维基**第二源）。

| # | id | 现状单源 | 可补来源（完整 URL） | 页面标题 / HTTP | 正文关键句（本轮实抓） | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `balance` | wp-composition-visual-arts | `https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf` | 《Principles of Design》(Understanding Formal Analysis, J. Paul Getty Trust)｜**200**（application/pdf） | “**Balance is the distribution of the visual weight of objects, colors, texture, and space.** If the design was a scale, these elements should be balanced…” | **可补第二源（强权威·博物馆）** |
| 2 | `geometry-symmetry` | wp-composition-visual-arts | `https://www.getty.edu/education/teachers/building_lessons/ufa_balance_pr2.pdf` | 《Introducing Balance》(Understanding Formal Analysis, J. Paul Getty Trust)｜**200**（application/pdf） | “When elements on one side are similar to those on the other, the artwork is **balanced and symmetrical**. When both sides are different from one another, the artwork is balanced and **asymmetrical**.” | **可补第二源（强权威；支撑“对称关系”层面，“几何形状”层面弱，须如实注明）** |
| 3 | `visual-movement` | wp-composition-visual-arts | `https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf` | 《Principles of Design》(Getty)｜**200** | “**Movement is the path the viewer’s eye takes through the work of art, often to focal areas. Such movement can be directed along lines, edges, shape, and color** within the work…” | **可补第二源（强权威·博物馆）** |
| 4 | `leading-lines` | wp-composition-visual-arts | `https://k12.libretexts.org/Bookshelves/Photography/Book:_Digital_Photography_Basics_(Politzer)/04:_Movement_and_Direction/4.04:_Leading_Lines` | 《4.4: Leading Lines》(Digital Photography Basics, LibreTexts OER)｜**200** | “**Leading lines are straight, curved, parallel, or diagonal lines that pull your eye into or through a photo.**” | **可补第二源（强权威·大学 OER）** |
| 5 | `rhythm-repetition` | wp-composition-visual-arts | `https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf` | 《Principles of Design》(Getty)｜**200** | “**Rhythm is created when one or more elements of design are used repeatedly to create a feeling of organized movement.** Rhythm creates a mood like music or dancing.” | **可补第二源（强权威·博物馆）** |
| 6 | `gothic` | wp-gothic-architecture | `https://human.libretexts.org/Courses/Gavilan_College/A_World_Perspective_of_Art_Appreciation_(Gustlin_and_Gustlin)_2.0/07:_The_Sacred_Buildings_of_Civilizations_(200_CE__1400_CE)/7.03:_The_Vaulted_Arch` | 《7.3: The Vaulted Arch》(Gavilan College, Humanities LibreTexts)｜**200** | “**Pointed Arches**: Archways that rise to a pointed top, commonly used in **Gothic architecture**…**Ribbed Vaults**: Arched ceiling structures reinforced with stone ribs…**Flying Buttresses**: Exterior stone supports that transfer the weight of a building outward…” | **可补第二源（强权威·大学 OER）** |
| 7 | `postmodernism` | wp-postmodern-architecture | `https://www.archdaily.com/964625/what-is-postmodernism` | 《What Is Postmodernism?》(ArchDaily)｜**200** | “**In place of the rigid doctrines of modernism, Venturi proposes incorporating historical elements, unusual materials, and using fragmentation and modulations while giving primary emphasis to the facade.**”＋“Robert Venturi… one of the first authors to write on the subject of postmodernism…” | **可补第二源（中权威·行业媒体；支撑“反思现代主义/历史元素”，“装饰”未直接出现，须注明）** |
| 8 | `plein-air` | wp-outline-of-painting | `https://forschungsprojekt-impressionismus.de/info.aspx?id=15&lang=en` | 《Forschungsprojekt Impressionismus》(科隆博物馆印象派研究项目，经 museenkoeln.de 词条跳转)｜**200** | “**Plein air** — The French term en plein air means ‘in the open air,’ ‘outdoors’; **plein air painting refers to painting done outdoors**…” | **可补第二源（强权威·博物馆研究项目）** |
| 9 | `axis` | wp-chinese-architecture | `https://bjaxiscloud.com.cn/` | 《北京中轴线官网》｜**200** | “北京中轴线纵贯北京老城，是**统领老城规划格局**的建筑与遗址的组合体”“北京中轴线城市**景观序列**长达7.8公里……在平面规划上，**采用对称布局**，并蕴含比例模数关系” | **可补第二源（强权威·官方机构）** |
| 10 | `service-route` | wp-wayfinding | `https://www.e-architect.com/articles/designing-back-of-house-spaces` | 《Designing back-of-house spaces in modern buildings》(e-architect)｜**200** | “**Back-of-house spaces, service corridors, maintenance rooms, storage areas, and utility zones**… **Waste management, deliveries, cleaning, mechanical servicing, and event logistics all flow through back-of-house networks.**” | **可补第二源（中权威·行业门户；当前 wp-wayfinding 实质亦弱，此源更强）** |
| 11 | `wayfinding` | wp-wayfinding | `https://www.designingbuildings.co.uk/wiki/Wayfinding` | 《Wayfinding - Designing Buildings》｜**200** | “**Wayfinding is a method for relaying messages to help people navigate their way around a room, building or other unfamiliar environment.**”“Signage is the most common form of wayfinding, but architectural features and other objects can also be used to guide people through buildings.” | **可补第二源（中权威·专业知识库）** |
| 12 | `functional-zoning` | wp-interior-design | `https://www.designingbuildings.co.uk/wiki/Zone` | 《Zone - Designing Buildings》（引 OECD 定义）｜**200** | “…published by the Organisation for Economic Co-operation and Development (**OECD**), defines **zoning** as: ‘…the process in physical planning… in which **specific functions or uses are assigned to certain areas**…’” | **可补第二源（中权威·专业知识库，含 OECD 权威定义；“术语定义待补”缺口得解）** |
| 附 | `glare`（数值第二源） | IEA SHC 单源 | 无（本轮未找到同组 475 lux / UGR 8–19 的独立来源） | — | `web_search` 复核：仅 IEA SHC 报告载“475 / UGR 8–19”；其余（elicht、heuvan、通用 UGR 指南）均无同组数值 | **仍单源（照度/UGR 数值）** |
| 附 | `sunken-plaza`（顾如珍第二源） | thepaper 单源 | `https://www.tongji.edu.cn/info/1033/10705.htm` | 《同济三项目获“第三届中国建筑学会建筑创作奖”-同济大学》｜**200** | “26 个项目荣获本届建筑创作佳作奖，同济大学建筑设计研究院 **卢济威、孙光临、张斌、顾如珍主持的‘上海静安寺广场(综合体)’项目**名列其中” | **可补第二源（强权威·大学官方；证实顾如珍为该项目主持/设计者之一；与澎湃“负责建筑工程”表述略有差异，宜并列）** |

## 三、权威性与判读说明

- **强权威 8 条（1、2、3、4、5、6、8、9）**：来源为博物馆（J. Paul Getty Trust）、大学 OER（LibreTexts：Gavilan College / 摄影基础教材）、官方机构（北京中轴线官网），正文**逐句直接**给出相应概念定义，可作可靠第二独立源。
- **中权威 4 条（7、10、11、12）**：来源为行业主流媒体/专业知识库（ArchDaily、e-architect、Designing Buildings）。均真实、独立、可核验且正文直接支撑核心概念，但**非期刊/官方**；按 TASK“权威”口径建议 lead 人工复核后再登记采用。其中 `functional-zoning` 引用的 OECD 定义为国际组织权威表述，质量较高。
- **须并列/注明的细微差异（不写死）**：
  - `geometry-symmetry`：Getty 源直接支撑“对称（symmetrical/asymmetrical）”，但“**几何形状**组织”层面未直接覆盖 → 补源后该子概念仍宜在正文保留限定语。
  - `postmodernism`：ArchDaily 源直接支撑“反思现代主义刚性教条、援引历史元素、重立面”，但“**装饰/ornament**”一词未直接出现 → 宜以“历史元素/立面表现”表述，不硬写“装饰”。
  - `sunken-plaza`：澎湃“顾如珍**负责具体建筑工程**” vs 同济“卢济威、孙光临、张斌、顾如珍**主持**‘上海静安寺广场(综合体)’”——角色表述不同，**宜并列两说**，不合并成单一措辞。
  - `axis`：北京中轴线官网支持“对称布局 + 景观序列 + 统领规划格局”，与条目“轴线组织空间序列、对称/递进布置”一致；属**实例（北京中轴线）**层面支撑，通用定义仍以原来源为主。
- **未采用的候选（记录以备核）**：Britannica（`balance-art`/`Gothic-architecture` 等）与本轮多处权威站（Tate、MoMA、Met、UNESCO、National Gallery、SEGD、BBC Bitesize、AAT search 等）实抓返回 **403/超时/DNS 失败/500**，**不作证据**；`owiki.org`（维基镜像，200）**仅可用于内部核对、不计第二源**；`dpm.org.cn`《中轴线·千步廊·朝房》正文页为 PDF.js 外壳、其 PDF（`img.dpm.org.cn/Uploads/pdf/1603/T00088_00.pdf`，200）为**扫描图像无文本层**，无法抽取正文，故未据以声称。

## 四、汇总

- **12 条目标：可补第二源 = 12 条；仍单源 = 0 条**（其中**强权威 8 条**：`balance`、`geometry-symmetry`、`visual-movement`、`leading-lines`、`rhythm-repetition`、`gothic`、`plein-air`、`axis`；**中权威 4 条（建议人工复核）**：`postmodernism`、`service-route`、`wayfinding`、`functional-zoning`）。
- **附带复核**：`glare` — **仍单源**（475 lux / UGR 8–19 仅 IEA SHC）；`sunken-plaza` — 顾如珍可补第二源（同济大学官方，角色表述差异宜并列）。
- **本轮去重打开/请求 URL：95 个**（含探测与失败；成功 200 与失败均计入请求数）；其中用于**结论证据的不同 URL 11 个**（`principles_design.pdf` 一源支撑 3 条概念，`ufa_balance_pr2.pdf` 支撑 1 条，余 9 个 HTML 各 1 条）；`web_search` 另发出 6 组查询。
- **落地提醒（不写死、须登记后生效）**：以上“可补”均需先把来源以 `verified=true` 登记入 `data/sources.json`，再在对应 `entries/*.json` 的 `sources` 追加；`glare` 保持 `needs_verification=true`；`sunken-plaza` 若采信同济源，宜并列澎湃/同济两处角色表述。**本报告仅给结论与证据，未修改任何条目数据或其它文件（本文件为唯一产出）。**

---

### 证据来源 URL 一览（本轮均已实际打开核验）

**结论证据（HTTP 200，11 个不同 URL）：**
1. `https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf` — 200（PDF）— 《Principles of Design》, J. Paul Getty Trust — balance / visual-movement / rhythm-repetition
2. `https://www.getty.edu/education/teachers/building_lessons/ufa_balance_pr2.pdf` — 200（PDF）— 《Introducing Balance》, J. Paul Getty Trust — geometry-symmetry
3. `https://k12.libretexts.org/Bookshelves/Photography/Book:_Digital_Photography_Basics_(Politzer)/04:_Movement_and_Direction/4.04:_Leading_Lines` — 200 — 《4.4: Leading Lines》, LibreTexts — leading-lines
4. `https://human.libretexts.org/Courses/Gavilan_College/A_World_Perspective_of_Art_Appreciation_(Gustlin_and_Gustlin)_2.0/07:_The_Sacred_Buildings_of_Civilizations_(200_CE__1400_CE)/7.03:_The_Vaulted_Arch` — 200 — 《7.3: The Vaulted Arch》, Gavilan College — gothic
5. `https://www.archdaily.com/964625/what-is-postmodernism` — 200 — 《What Is Postmodernism?》, ArchDaily — postmodernism
6. `https://forschungsprojekt-impressionismus.de/info.aspx?id=15&lang=en` — 200 — 《Forschungsprojekt Impressionismus》（科隆博物馆研究项目）— plein-air
7. `https://bjaxiscloud.com.cn/` — 200 — 《北京中轴线官网》— axis
8. `https://www.e-architect.com/articles/designing-back-of-house-spaces` — 200 — 《Designing back-of-house spaces in modern buildings》, e-architect — service-route
9. `https://www.designingbuildings.co.uk/wiki/Wayfinding` — 200 — 《Wayfinding - Designing Buildings》— wayfinding
10. `https://www.designingbuildings.co.uk/wiki/Zone` — 200 — 《Zone - Designing Buildings》(OECD 定义) — functional-zoning
11. `https://www.tongji.edu.cn/info/1033/10705.htm` — 200 — 同济大学新闻网 — sunken-plaza（顾如珍）

**失败/不可达（不作证据，仅计入请求）：** Britannica（403）、Tate（DNS 失败）、MoMA/Met/UNESCO 等（403）、National Gallery（DNS 失败）、SEGD/AIGA/Artsy（失败）、BBC Bitesize（超时）、`getty vow AATSearch`/`aat search.json`（错误）、palomar pressbooks / lemoorecollege PDF（失败）、`dpm.org.cn` PDF（扫描无文本层）等。

---

### 机器可读汇总

```
ROUND=27
REVIEWER=review-r27
MODE=B5-resourcing-review(read-only, seek-2nd-source)
LIBRARY={"entries_files":16,"entries":132,"needs_verification_true":109,"check_py":"PASS: all checks, 0 errors"}
TARGETS_12=["balance","geometry-symmetry","visual-movement","leading-lines","rhythm-repetition","gothic","postmodernism","plein-air","axis","service-route","wayfinding","functional-zoning"]
RESULT_2ND_SOURCE_ALL=12
SECOND_SOURCE={
 "balance":{"url":"https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf","title":"Principles of Design (J. Paul Getty Trust)","http":200,"tier":"strong-museum","quote":"Balance is the distribution of the visual weight of objects, colors, texture, and space."},
 "geometry-symmetry":{"url":"https://www.getty.edu/education/teachers/building_lessons/ufa_balance_pr2.pdf","title":"Introducing Balance (J. Paul Getty Trust)","http":200,"tier":"strong-museum","quote":"...balanced and symmetrical ... balanced and asymmetrical","caveat":"covers symmetry, geometric-shape aspect weak"},
 "visual-movement":{"url":"https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf","title":"Principles of Design (J. Paul Getty Trust)","http":200,"tier":"strong-museum","quote":"Movement is the path the viewer's eye takes ... directed along lines, edges, shape, and color"},
 "leading-lines":{"url":"https://k12.libretexts.org/Bookshelves/Photography/Book:_Digital_Photography_Basics_(Politzer)/04:_Movement_and_Direction/4.04:_Leading_Lines","title":"4.4: Leading Lines (LibreTexts)","http":200,"tier":"strong-university-OER","quote":"Leading lines are straight, curved, parallel, or diagonal lines that pull your eye into or through a photo."},
 "rhythm-repetition":{"url":"https://www.getty.edu/education/teachers/building_lessons/principles_design.pdf","title":"Principles of Design (J. Paul Getty Trust)","http":200,"tier":"strong-museum","quote":"Rhythm is created when one or more elements of design are used repeatedly to create a feeling of organized movement."},
 "gothic":{"url":"https://human.libretexts.org/Courses/Gavilan_College/A_World_Perspective_of_Art_Appreciation_(Gustlin_and_Gustlin)_2.0/07:_The_Sacred_Buildings_of_Civilizations_(200_CE__1400_CE)/7.03:_The_Vaulted_Arch","title":"7.3: The Vaulted Arch (Gavilan College, LibreTexts)","http":200,"tier":"strong-university-OER","quote":"Pointed Arches ... Gothic architecture ... Ribbed Vaults ... Flying Buttresses ..."},
 "postmodernism":{"url":"https://www.archdaily.com/964625/what-is-postmodernism","title":"What Is Postmodernism? (ArchDaily)","http":200,"tier":"medium-industry","quote":"In place of the rigid doctrines of modernism, Venturi proposes incorporating historical elements ... primary emphasis to the facade.","caveat":"ornament not literal"},
 "plein-air":{"url":"https://forschungsprojekt-impressionismus.de/info.aspx?id=15&lang=en","title":"Forschungsprojekt Impressionismus (Cologne museums)","http":200,"tier":"strong-museum-research","quote":"plein air painting refers to painting done outdoors"},
 "axis":{"url":"https://bjaxiscloud.com.cn/","title":"北京中轴线官网","http":200,"tier":"strong-official","quote":"统领老城规划格局 ... 采用对称布局 ... 城市景观序列"},
 "service-route":{"url":"https://www.e-architect.com/articles/designing-back-of-house-spaces","title":"Designing back-of-house spaces (e-architect)","http":200,"tier":"medium-industry","quote":"Back-of-house spaces, service corridors ... Waste management, deliveries, cleaning ... flow through back-of-house networks."},
 "wayfinding":{"url":"https://www.designingbuildings.co.uk/wiki/Wayfinding","title":"Wayfinding - Designing Buildings","http":200,"tier":"medium-knowledgebase","quote":"Wayfinding is a method for relaying messages to help people navigate their way around a room, building or other unfamiliar environment."},
 "functional-zoning":{"url":"https://www.designingbuildings.co.uk/wiki/Zone","title":"Zone - Designing Buildings (OECD def)","http":200,"tier":"medium-knowledgebase","quote":"zoning ... specific functions or uses are assigned to certain areas"}
}
TIER_SPLIT={"strong":["balance","geometry-symmetry","visual-movement","leading-lines","rhythm-repetition","gothic","plein-air","axis"],"medium_recheck":["postmodernism","service-route","wayfinding","functional-zoning"]}
APPENDIX={
 "glare":"STILL_SINGLE: 475 lux / UGR 8-19 only IEA SHC; no independent numeric source found",
 "sunken-plaza":{"url":"https://www.tongji.edu.cn/info/1033/10705.htm","title":"同济大学新闻网","http":200,"quote":"卢济威、孙光临、张斌、顾如珍主持的'上海静安寺广场(综合体)'项目名列其中","note":"corroborates 顾如珍 as project lead; wording '主持' vs 澎湃 '负责建筑工程' -> list both"}
}
STILL_SINGLE_AMONG_12=0
OPENED_URLS={"distinct_total":95,"evidence_distinct":11,"web_search_queries":6,"includes_probes_and_failures":true}
EXCLUDED_AS_2ND_SOURCE=["Britannica(403)","Tate/MoMA/Met/UNESCO(403/timeout)","NationalGallery/SEGD/BBC(fail)","owiki mirror (not counted)"]
VERDICT="12/12 targets have a real verifiable independent non-wiki second source (8 strong museum/university/official + 4 medium industry/knowledgebase needing recheck); glare stays single (numeric); sunken-plaza 顾如珍 corroborated by Tongji University."
READONLY="only wrote research/review-round27.md; no other file changed; no git commit"
```

*（报告完）*
