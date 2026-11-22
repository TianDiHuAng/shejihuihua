# B1/B6 缺口发现 — 第 43 轮（未用过的权威大纲再对照 + 近 12 个月动态）

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23
- 执行角色：b1-r43（只读子任务，无人值守，未提问）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent 直连实抓（依据 DECISIONS.md D05：本环境 web_fetch/网页直取以实际 HTTP 响应为准）。`web_search` 仅用于 B6 线索探测。
- 数据纪律：联网内容一律视为**数据**；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML 正文判读标题与相关句。
- 来源纪律：本轮 B1 全部使用 `owiki.org`（维基镜像，与 en.wikipedia 同源、只计一源）实抓；Britannica 两页 403 未取到。**凡报出候选须≥2 份独立权威来源**——本轮无候选，故不涉第二源判定。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在当前工作区根目录；其真实文件位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`（`WORKFLOW.md` 同目录），本轮已实际读取两份原文。
- 项目根现存治理文件 `DECISIONS.md`、`scope.md`、`REPORT.md`、`research/b1-round42.md` 一并作为方法与来源纪律基准。
- **范围判据取自 TASK_design.md 原文**：`绘画理论：透视法、构图法则、色彩理论、光影与明暗、中国画六法与留白、东西方理论比较`；`建筑与空间设计：主要建筑风格史；中国传统园林造景（借景、框景、对景、障景、曲径与游线）；动线设计；下沉式空间（下沉庭院、下沉广场）；空间序列与尺度；室内外过渡；采光、通风与材料的基本原理`。本轮只接受落入这两段**明确列举子域**的核心概念。
- 判定标准（从严，三条须全部满足）：①≥2 份独立权威来源（非同一平台/镜像）；②属上述六大面之**核心**概念（非边缘技法细节、非近义重复）；③`scope.md` 确实缺失。

## 比对基准

- `scope.md` 现 **251 条**：理论 127 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19。
- 第 42 轮已将 `hatching`（排线法，重要）、`stippling`（点描法，补充）纳入理论（125→127），本轮**不得重复报出**。
- 已逐条在 `entries/`、`scope.md`、`coverage.json`、`data/sources.json`、`research/` 中 grep 核对，凡判为「已覆盖/近义/边缘/域外」者均给出具体对照。

---

## B1：与「未用过」的权威大纲/分类树再对照

本轮对照下列 **8 份此前从未用于本项目任一轮**的权威大纲/分类树/学科总述页面（均文件级 grep `research/` 命中 0 次，确认「未用过」；实抓状态如下）。「≥3 份未用过」要求已远超满足。

| # | 大纲/分类树（未用） | URL | HTTP | 覆盖方向 |
| --- | --- | --- | --- | --- |
| 1 | List of garden types（园林类型分类树） | https://owiki.org/wiki/List_of_garden_types | 200 | 造景 / 园林类型分类 |
| 2 | Garden（园林总述，含 Types / Design 节） | https://owiki.org/wiki/Garden | 200 | 园林类型与设计要素 |
| 3 | List of building materials（建筑材料分类） | https://owiki.org/wiki/List_of_building_materials | 200 | 材料 |
| 4 | Light in painting（绘画中的光，学科总述） | https://owiki.org/wiki/Light_in_painting | 200 | 绘画理论 / 光影与明暗 |
| 5 | Art movement（艺术流派） | https://owiki.org/wiki/Art_movement | 200 | 风格（绘画流派，用于越域核对） |
| 6 | Space (architecture)（建筑空间） | https://owiki.org/wiki/Space_(architecture) | 200 | 空间设计基本原理 |
| 7 | Earth sheltering（覆土/掩土建筑总述） | https://owiki.org/wiki/Earth_sheltering | 200 | 下沉空间 / 材料 / 通风 |
| 8 | Architectural geometry（建筑几何） | https://owiki.org/wiki/Architectural_geometry | 200 | 空间设计 / 几何 |

> 覆盖说明：绘画理论（Light in painting）、建筑风格（Art movement，越域核对用）、园林造景（List of garden types、Garden）、材料（List of building materials）、空间设计基本原理（Space (architecture)、Architectural geometry）、下沉空间（Earth sheltering）六大面均有一份或多份未用大纲实抓对照。Britannica 的 `architecture`、`garden-and-landscape-design` 两页尝试作独立第二权威源，均 403（见失败表），故 B1 对照以 owiki 实抓为准。

### 逐份大纲提取与「未纳入」理由

**#1 List of garden types（200）** — 提取 60+ 园林类型：按国别（Chinese / Dutch / English / French / Indian / Mughal / Italian / Japanese / Korean / Persian / Spanish / US 等）、按历史帝国、按宗教、按功能（bog / cactus / rose / water / herb / kitchen / roof / rock / zen …）。
- 未纳入理由：本页为**园林风格史 / 园艺功能类型**分类树，不属 TASK 明确列举的「中国传统园林造景（借景、框景、对景、障景、曲径与游线）」**核心造景手法**；`French formal garden`、`English landscape garden`、`Persian garden`、`Mughal garden`、`Italian Renaissance garden`、`knot garden`、`bosquet` 等均属欧洲/伊斯兰园林风格，**越出「中国传统园林造景」面**（风格面又限「建筑风格史」）。其中 `Cantonese garden`（粤）、`Sichuanese garden`（川）为中国园林**地域子类型**，与已收录 `chinese-architecture-style`、`garden-architecture` 属**近义/边缘**，非新增核心手法；`zen garden / Japanese dry garden` 为日本园林，越出中国造景面。`water garden`、`herb garden`、`rose garden` 等为园艺功能类型，非理论核心。→ **不构成核心缺口**。

**#2 Garden（200）** — `Types` 节与 #1 同表；`Design` 节列出造园要素：hard landscape（path/rockery/wall/water feature/decking）、planting、drainage、lights、buildings。
- 未纳入理由：这些设计要素均已在本 scope 落位——`garden-architecture`（园林建筑）、`rockery`（叠石）、`water-management`（理水）、`planting-design`（植物配置）、`hardscape-softscape`（硬/软质景观）、`drainage`（排水）、`lighting-design`（照明设计）。逐一为**近义/已覆盖**，无新概念。→ **不构成核心缺口**。

**#3 List of building materials（200）** — 提取建筑材料大类：cold-rolled steel framing、concrete、hempcrete、masonry（brick / stone / adobe / rammed earth / concrete block / terra cotta）、wood/timber（heavy timber / glulam / plywood / OSB）、glass、plastics、thermal/moisture protection 等。
- 未纳入理由：本 scope「材料」主题为**原理级**（`material-texture` 材料质感、`material-color`、`material-durability`、`vernacular-material` 乡土材料[含 adobe/rammed earth]、`transparent-material` 透明材料[玻璃]、`structural-material` 结构材料[钢/混凝土/木]）。上列均为**产品/材料品类级**，与 `structural-material`、`vernacular-material`、`transparent-material` **近义**，属边缘细节，非核心概念。→ **不构成核心缺口**。

**#4 Light in painting（200）** — `Techniques` 节：媒介（pencil / charcoal / oil / pastel / watercolor / acrylic）＋笔法（hatching、soft shading、impasto、glazes、chiaroscuro）；`Genres` 节：interior / still life / landscape / figure；正文提及 chiaroscuro、sfumato、tenebrism、luminism。
- 未纳入理由：`chiaroscuro`（核心）、`sfumato`、`tenebrism`、`hatching`、`stippling` **均已收录**（后两者第 42 轮已纳入）；`luminism` 属绘画**流派/风格**（风格面限建筑）越域；媒介（oil/watercolor/pastel/acrylic/tempera）与题材门类（interior/still-life/landscape/figure）**不属「光影与明暗」等绘画理论六子域**；`impasto`（厚涂）、`glaze`（罩染）、`soft shading`（柔和明暗过渡）属**边缘笔法细节**。→ **不构成核心缺口**（仅边缘技法）。

**#5 Art movement（200）** — 19–21 世纪绘画流派（Impressionism / Cubism / Fauvism / Abstract Expressionism …）。
- 未纳入理由：TASK「风格」明确限**「主要建筑风格史」**，绘画流派**越域**；且本 scope 风格面已有 62 条建筑风格。→ **不构成缺口**（与 round02/41/42 既有排除口径一致）。

**#6 Space (architecture)（200）** — 正文为短条目：space 是建筑设计要素之一，「carving space out of space…using geometry, colours, shapes」。
- 未纳入理由：已被 `space-definition`（建筑空间定义，核心）、`spatial-organization`（空间组织方式，核心）、`geometry-symmetry`（几何与对称）覆盖，属**近义**；且该页为极短 stub、单一来源。→ **不构成核心缺口**。

**#7 Earth sheltering（200）** — `Types`：bermed / in-hill / underground；`Design and construction`：waterproofing、insulation、excavation、drainage；被动系统：earth tube ventilation、passive annual heat storage、annualized geo solar。
- 未纳入理由：类型（bermed/in-hill/underground）与已收录 `earth-sheltered`（覆土建筑）、`semi-sunken-space`（半下沉）、`sunken-*` **近义/已覆盖**；防水防潮排水安全（`damp-proofing`/`drainage`/`safety-guarding`）已收；`earth tube ventilation`（地道风/土壤-空气换热）、`PAHS`、`annualized geo solar` 属**边缘可持续技法**（自然通风的细分被动子技术），非「通风基本原理」**核心概念**。→ **不构成核心缺口**（仅边缘技法）。

**#8 Architectural geometry（200）** — 研究领域：applied geometry + architecture；differential geometry / topology / fractal geometry / cellular automata；developable surfaces、discretisation、generative design、digital fabrication。
- 未纳入理由：属**数字几何研究领域 / 加工与生成设计**，与已收录 `parametric-architecture`（参数化建筑）、`geometry-symmetry` **近义**；属边缘方法学，非空间设计**基本原理**核心概念。→ **不构成核心缺口**。

### 候选概念逐条「未纳入」汇总表

| 候选（来自本轮大纲） | 归属面 | 未纳入理由 |
| --- | --- | --- |
| French/English/Persian/Mughal/Italian garden、knot garden、bosquet | 造景 | 园林**风格史/欧洲规整园**，越出「中国传统园林造景」面（风格限建筑） |
| Cantonese / Sichuanese garden | 造景 | 中国园林**地域子类型**，近义/边缘于 `chinese-architecture-style`、`garden-architecture` |
| Zen / Japanese dry garden | 造景 | **日本园林**，越出中国造景面 |
| water/herb/rose/bog garden 等 | 造景 | **园艺功能类型**，非理论核心 |
| Garden design 要素（path/rockery/water/planting/drainage/light） | 造景 | 已被 garden-architecture / rockery / water-management / planting-design / hardscape-softscape / drainage / lighting-design **覆盖** |
| concrete / steel / timber / brick / stone / glass / adobe / rammed earth | 材料 | **产品品类级**，近义 structural-material / vernacular-material / transparent-material |
| earth tube ventilation / PAHS / annualized geo solar | 材料/通风 | **边缘可持续被动技法**，非通风核心原理 |
| bermed / in-hill / underground earth shelter | 下沉空间 | 近义/已覆盖 earth-sheltered、semi-sunken-space、sunken-* |
| impasto / glaze / soft shading | 光影与明暗 | **边缘笔法细节** |
| luminism | 风格(绘画) | 绘画流派/风格，**越域**（风格限建筑） |
| interior/still-life/landscape/figure genres；oil/watercolor 等媒介 | 绘画理论 | **题材门类/媒介**，非六子域 |
| Impressionism/Cubism 等 art movements | 风格 | 绘画流派，**越域**（限建筑风格史） |
| Space (architecture)「carving space out of space」 | 空间原理 | 近义/已覆盖 space-definition、spatial-organization；stub 单源 |
| developable surfaces / discretisation / generative design | 空间原理 | 数字几何研究领域，近义 parametric-architecture、geometry-symmetry |

### B1 结论

**不构成新的核心缺口。** 本轮以 **8 份此前从未使用**的权威大纲/分类树（List of garden types、Garden、List of building materials、Light in painting、Art movement、Space (architecture)、Earth sheltering、Architectural geometry，均 owiki 实抓 HTTP 200）逐页对照 251 条。所提取的候选概念全部落入以下任一情形：**（a）越出六大面**（园林风格史、绘画流派、绘画媒介/题材）、**（b）近义已收录**（材料品类↔结构/乡土/透明材料；覆土类型↔earth-sheltered；space-stub↔space-definition）、或 **（c）边缘技法细节**（impasto/glaze/soft shading、earth tube/PAHS、建筑几何研究主题）。无一条同时满足「≥2 独立权威源 + 六大面核心概念 + scope 缺失」的严格判据。故 B1 计 **0 条新核心缺口**。

---

## B6：近 12 个月（2025-11 至 2026-11）与绘画理论/建筑空间设计直接相关的理论性新研究/事件

结构化来源页面（均 owiki 实抓 HTTP 200）：
- https://owiki.org/wiki/2025_in_architecture —《2025 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_architecture —《2026 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2025_in_art —《2025 in art ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_art —《2026 in art ::: Open WIKI》200
- 补充线索：`web_search` 2 组查询（2025–2026 建筑/绘画理论新著与进展），返回 10 条结果（见下方清单，仅作线索，未逐一抓取正文）。

保守原则：仅保留能核对到日期/来源、且能明确说明对本项目具体条目产生「新增或更新」**理论性**影响者。窗口内实际事项性质如下（均**非**理论进展）：
- 2025-11-03：罗马中世纪 Torre dei Conti 修缮中局部坍塌（1 死）；2025-03-16 Valkenburg Wilhelminatoren 坍塌；2025-01-07 南加州山火毁建筑——**建成遗产维护/事故**，与具体理论/原理条目无对应（历轮同口径排除）。
- 2025-10-19：卢浮宫 Galerie d'Apollon 法国王冠珠宝被盗；2025-09-25 Bristol 博物馆 600+ 文物被盗；2025-03「Rembrandt 海景画被盗」经证实为拍片摆拍——**文物/安防事件**，非理论。
- 2025-11-18：Klimt《Portrait of Elisabeth Lederer》以 2.384 亿美元成交；2025 Frida Kahlo、Fabergé 等拍卖纪录——**市场/拍卖事件**，非理论。
- 奖项：2025 Pritzker 刘家琨、2025 AIA 金质奖 Deborah Berke、2025 Stirling 奖 Appleby Blue Almshouse——**奖项事件**，不改变任何理论条目定义。
- 2025_in_art 其余为艺博会档期（Art Basel / Frieze / TEFAF 等）与展览；2025_in_architecture 其余为建筑开馆与讣告；2026_in_architecture / 2026_in_art 页面极稀疏（各约 0.3–0.5KB，仅少量列项与讣告）。页面尾部「Books/Films/Programming Languages/TV Series/Video Games」为 owiki 镜像每页注入的**站点样板**，非词条正文，不计入。
- `web_search` 新著线索（均 2025–2026 出版，属**当代理论思潮/专著**，非六大面核心概念的定义性变更）：Sick Architecture（MIT Press, 2025，[brooklynrail 评介](https://brooklynrail.org/2026/10/architecture/sick-architecture-and-we-the-bacteria-notes-toward-biotic-architecture)）、Architecture Is Climate（2025，[GTAS](https://gtas-braunschweig.de/interacting/detail/architecture-is-climate-3)）、Architecture in the Age of Mediatizing Technologies（Routledge，[链接](https://www.routledge.com/Architecture-in-the-Age-of-Mediatizing-Technologies/Lee/p/book/9781032060590)）、Medieval Courtyard Design（Routledge，[链接](http://www.routledge.com/9781040662564)）等。上述为**话语/专著层面**，未提出需据以新增或改写本 scope 任一核心条目（透视/构图/色彩/光影/中国画/建筑风格史/园林造景/动线/下沉/材料/空间原理）的**规范性理论变更**；且多为单一出版方、非双源核心概念。

### B6 结论

**B6 未发现需要更新条目的理论性新研究/事件。** 近 12 个月内可核验事项均为奖项、讣告、建筑开馆、拍卖、盗窃、事故与当代理论专著/思潮；无一构成对「绘画理论 / 建筑空间设计」**核心条目**的理论性新增或更新。已载于 `research/gaps-external-round02.md` 的 3 条实例/语境候选（Guggenheim Abu Dhabi 预计 2026-12 开馆、Lucas Museum 2026-09-22 开馆、Pritzker 2025 刘家琨）维持不变，本轮无需据此改动 scope 或条目。

---

## 本轮实际打开的 URL 与 HTTP 状态

### 对照用大纲/分类树（owiki 镜像，均未在往轮使用；文件级 grep research/ 命中 0）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/List_of_garden_types | List of garden types ::: Open WIKI | 200 |
| https://owiki.org/wiki/Garden | Garden ::: Open WIKI | 200 |
| https://owiki.org/wiki/List_of_building_materials | List of building materials ::: Open WIKI | 200 |
| https://owiki.org/wiki/Light_in_painting | Light in painting ::: Open WIKI | 200 |
| https://owiki.org/wiki/Art_movement | Art movement ::: Open WIKI | 200 |
| https://owiki.org/wiki/Space_(architecture) | Space (architecture) ::: Open WIKI | 200 |
| https://owiki.org/wiki/Earth_sheltering | Earth shelter ::: Open WIKI | 200 |
| https://owiki.org/wiki/Architectural_geometry | Architectural geometry ::: Open WIKI | 200 |

### B6 来源
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/2025_in_architecture | 2025 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_architecture | 2026 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2025_in_art | 2025 in art ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_art | 2026 in art ::: Open WIKI | 200 |

### 失败/不可用（作独立第二权威源探索，审计用）
| URL | 结果 | 备注 |
| --- | --- | --- |
| https://www.britannica.com/art/architecture | HTTP 403 | 独立权威源取不到，改用 owiki 实抓对照 |
| https://www.britannica.com/art/garden-and-landscape-design | HTTP 403 | 同上 |

### web_search 线索（B6；返回摘要，未逐一抓正文，不计入「打开 URL」）
- https://brooklynrail.org/2026/10/architecture/sick-architecture-and-we-the-bacteria-notes-toward-biotic-architecture
- https://gtas-braunschweig.de/interacting/detail/architecture-is-climate-3
- https://www.routledge.com/Architecture-in-the-Age-of-Mediatizing-Technologies/Lee/p/book/9781032060590
- http://www.routledge.com/9781040662564
- 另含 MDPI / Nature / OUP 等单篇论文或书讯 6 条（均为专著/论文层面，非核心概念变更）

### 打开 URL 计数
- 本轮实际发起 HTTP 请求 **23 次**（含同页重复抓取以提取不同章节）；**去重后 14 个不同 URL**；其中 HTTP 200 **12 个**，HTTP 403 **2 个**（britannica 两页）。
- 作为 B1 对照来源的核心大纲页 **8 个**（均 200）；B6 结构化年报页 **4 个**（均 200）；失败 2 个（403）。
- `web_search` 另发起查询 2 组（返回 10 条线索，非 HTTP 正文抓取）。

---

## 机器可读汇总

```
ROUND=43
SCOPE_TOTAL=251   # 理论127/风格62/造景19/动线12/下沉12/材料19
B1_OUTLINES_UNUSED=8   #[List_of_garden_types,Garden,List_of_building_materials,Light_in_painting,Art_movement,Space_(architecture),Earth_sheltering,Architectural_geometry]
B1_ALL_UNUSED_CONFIRMED=true   # research/ grep 命中 0
B1_CANDIDATES=[]   # 无满足「≥2独立源+六大面核心+scope缺失」者
B1_REJECTED=[
 "garden-style-history(French/English/Persian/Mughal/Italian/knot/bosquet: 越出中国园林造景面)",
 "cantonese-sichuanese-garden(中国园林地域子类型: 近义/边缘)",
 "zen-japanese-dry-garden(日本园林: 越域)",
 "garden-functional-types(water/herb/rose/bog: 园艺功能类型, 非理论核心)",
 "garden-design-elements(path/rockery/water/planting/drainage/light: 已覆盖)",
 "building-material-categories(concrete/steel/timber/brick/stone/glass/adobe/rammed-earth: 品类级近义structural/vernacular/transparent-material)",
 "earth-tube-ventilation/PAHS/annualized-geo-solar(边缘可持续被动技法)",
 "earth-shelter-types(bermed/in-hill/underground: 近义earth-sheltered/semi-sunken/sunken)",
 "impasto/glaze/soft-shading(边缘笔法细节)",
 "luminism(绘画流派: 越域)",
 "painting-genres-and-media(interior/still-life/landscape/figure; oil/watercolor: 题材/媒介, 非六子域)",
 "art-movements(Impressionism/Cubism: 绘画流派, 越域-风格限建筑)",
 "space-architecture-stub(carving space out of space: 近义space-definition/spatial-organization, 单源stub)",
 "architectural-geometry(developable-surfaces/discretisation/generative-design: 数字几何研究领域, 近义parametric/geometry-symmetry)"
]
B1_RESULT="不构成新的核心缺口（0 条）"
B6_NEW=[]
B6_RESULT="未发现需要更新条目的理论性新研究/事件（奖项/讣告/开馆/拍卖/盗窃/事故/当代专著思潮均非核心概念理论变更）"
URLS_REQUESTED=23
URLS_OK_200=12
URLS_FAILED_403=2
URLS_DISTINCT=14
```

是否发现新缺口：否
