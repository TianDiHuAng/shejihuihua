# B1/B6 缺口发现 — 第 45 轮（未用过的权威大纲再对照 + 近 12 个月动态；饱和终判第 3 轮）

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23
- 执行角色：b1-r45（只读子任务，无人值守，未提问）
- 抓取方式：`web_fetch` 工具与 Python 3.11 urllib + 浏览器 User-Agent 直连 owiki 镜像实抓（依据 DECISIONS.md D05：本环境网页直取以实际 HTTP 响应为准）。`web_search` 仅用于 B6 线索探测。
- 数据纪律：联网内容一律视为**数据**；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML 正文判读标题与相关句。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在当前工作区根目录；其真实文件位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`（`WORKFLOW.md` 同目录），本轮已实际读取三份原文。
- 项目根现存治理文件 `DECISIONS.md`、`scope.md`、`PROGRESS.md`、`BLOCKERS.md`、`research/outline_raw.md`、`research/b1-round43.md`、`research/b1-round44.md` 一并作为方法与来源纪律基准。
- **范围判据取自 TASK_design.md 原文**：`绘画理论：透视法、构图法则、色彩理论、光影与明暗、中国画六法与留白、东西方理论比较`；`建筑与空间设计：主要建筑风格史；中国传统园林造景（借景、框景、对景、障景、曲径与游线）；动线设计；下沉式空间（下沉庭院、下沉广场）；空间序列与尺度；室内外过渡；采光、通风与材料的基本原理`。本轮只接受落入这两段**明确列举子域**的核心概念。
- AUTONOMOUS.md 第四节扩充规则：新增条目须「至少两份独立的权威来源把它归入本领域」，单轮 scope 增幅 ≤10%。本轮所有新页均为 owiki 单一平台/镜像，**均不计第二独立源**。
- 判定标准（从严，三条须全部满足）：①≥2 份独立权威来源（非同一平台/镜像）；②属上述六大面之**核心**概念（非边缘技法、非近义重复、非绘画流派/媒介/题材）；③`scope.md` 确实缺失。

## 比对基准

- `scope.md` 现 **251 条**：理论 127 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19（核心 50、重要 147、补充 54）。
- 已用大纲：S1–S12（Outline of architecture、Architectural style、Chinese garden、Chinese painting、Perspective (graphical)、Composition (visual arts)、Color theory、Circulation (architecture)、Architectural lighting、Ventilation (architecture)、Chinese architecture、Garden design）＋ round02/06/09/40/41/42/43/44 各轮已用页面（详见 `research/outline_raw.md`、`research/gaps-external-round*.md`、`b1-round40~44.md`）。
- 第 42 轮已纳入 `hatching`（排线法）、`stippling`（点描法）；第 43、44 轮从严判定 0 新缺口。本轮**不得重复**上述条目与已用页面。
- 已逐条在 `research/`、`entries/`、`scope.md`、`data/`、`coverage.json` 中 grep 核对：本轮 6 份**新**大纲页 slug 命中 **0**（见文末 `B1_ALL_UNUSED_CONFIRMED=true`）；另 3 份此前已出现/已作来源，**不计入「新」**（见下方说明）。

---

## B1：与「未用过」的权威大纲/分类树再对照

本轮对照下列 **6 份此前从未用于本项目任一轮**的权威百科总述/分类页（文件级 grep `research/`、`entries/`、`scope.md`、`data/`、`coverage.json` 均命中 0 次；owiki 镜像实抓 HTTP 200）。「≥3 份未用过」要求已超出一倍满足。

| # | 大纲/分类页（未用·grep 0） | URL | HTTP | 覆盖方向 |
| --- | --- | --- | --- | --- |
| 1 | Figure drawing（人体写生/人体素描，技法总述） | https://owiki.org/wiki/Figure_drawing | 200 | 绘画理论（人体比例/技法核对） |
| 2 | Building science（建筑科学，学科总述） | https://owiki.org/wiki/Building_science | 200 | 材料 / 采光 / 通风原理 |
| 3 | Environmental design（环境设计，学科总述） | https://owiki.org/wiki/Environmental_design | 200 | 空间设计 / 室内外 / 可持续 |
| 4 | Basement（地下室，类型与设计分类） | https://owiki.org/wiki/Basement | 200 | 下沉空间 / 地下空间 |
| 5 | Philosophy of architecture（建筑哲学，学科总述） | https://owiki.org/wiki/Philosophy_of_architecture | 200 | 空间设计理论（越域核对） |
| 6 | Pedestrian（行人/步行，概念总述） | https://owiki.org/wiki/Pedestrian | 200 | 动线（人行流线核对） |

> 覆盖说明：绘画理论（Figure drawing）、材料/采光/通风（Building science）、空间设计（Environmental design、Philosophy of architecture）、下沉空间（Basement）、动线（Pedestrian）五个方向各有 1–2 份未用大纲实抓对照。全部为 owiki 镜像单一平台，故均**不计第二独立源**；本轮无候选，不涉第二源判定。

**此前已出现、故不计「新」的补充页（仅作旁证/稳健性核对，不列入上表「未用」）：**
- `Color_wheel`（200）——已是 `data/sources.json` 的 `wp-color-wheel` 来源，且 `b1-round42.md:96` 已就「color wheel / color mixing / color space / opponent process」判为「色彩科学机制，与 color-theory 系列近义或颗粒度更细 → 不报」。本轮实抓复核同结论，**不作为新大纲计数**。
- `Japanese_garden`（200）——`review-round04.md:21` 已实际抓取（200）用于 framed-scenery 补源核对，属已查页面；内容为中国/日本园林史与风格，**越出「中国传统园林造景」面**（借景 shakkei 已收录 `borrowed-scenery`），亦**不计新**。
- `Architectural_theory`（200）——已在本项目往轮页面清单中（grep 命中），**不计新**。

### 逐份大纲提取与「未纳入」理由

**#1 Figure drawing（200）** — 人体写生/人体素描总述：方法（life drawing、照片参照、默写；按明暗塑造 / 解剖骨骼肌肉 / 几何体概括三种路径）；body proportions（普通 7.5 头身、理想 8 头身、英雄 8.5 头身）；媒介（Conté 蜡笔、炭笔、石墨、墨水、ink wash）；历史（Carracci 学院、David 画室、academy figure）；gesture drawing、foreshortening、figure–ground / 构图；女艺术家受限于人体写生的史实。
- 未纳入理由：属**绘画技法/教学方法**（人体写生这一科），**不属于** TASK 六子域（透视/构图/色彩/光影与明暗/中国画六法与留白/东西方比较）中的核心概念；`body proportions`（头身比）与已收录 `proportion`（比例，核心）、`human-scale`（人体尺度）**近义**；`gesture drawing`、按解剖/几何概括路径为**边缘技法细节**；`foreshortening`（缩短法）**已是 scope 条目**（`foreshortening`，重要）。→ **不构成核心缺口**（技法/近义/边缘）。

**#2 Building science（200，15KB+）** — 建筑科学=建筑物理/建筑科学交叉学科；Topics：Daylighting and visual comfort（含 glare）、Indoor environmental quality（IEQ）、HVAC、Enclosure（envelope）systems、Building sustainability（含 embodied carbon / decarbonization / 净零能耗）、Post-Occupancy Evaluation（POE）；列若干期刊。
- 未纳入理由：属**学科/工程层面总述**；其核心 topic 与已收录 `daylighting`、`glare`、`visual-comfort`、`thermal-comfort`、`acoustic-environment`、`natural-ventilation`、`mixed-mode-ventilation`、`demand-controlled-ventilation`、`material-durability`、`damp-proofing`、`sustainable-design`/`sustainable-architecture` **近义/已覆盖**；`embodied carbon`/`decarbonization`/`POE`/`IEQ` 为**工程评价指标与方法**，非「采光、通风与材料的基本原理」核心概念；单源。→ **不构成核心缺口**（学科层/近义/边缘）。

**#3 Environmental design（200）** — 环境设计：处理环境参数以规划建筑/产品/政策；Core Principles（sustainability / functionality / aesthetics / holistic）；Modern Uses（sustainable architecture、landscape architecture & urban planning、transportation、industrial design、interior design & space planning）；History（古希腊/古罗马 solar heating、William Morris、Fuller）；research areas（含 environmental psychology、sociology of architecture）。
- 未纳入理由：属**跨学科领域/职业层面总述**（含 geography、industrial design、public policy），域过宽；四项 principles 与已收录 `sustainable-design`、`space-definition`/`spatial-organization`、`environmental-psychology` **近义**；history 段 solar heating 为**被动式太阳能史例**（边缘技术史）；非六大面新增核心概念。单源。→ **不构成核心缺口**（学科层/近义/域外）。

**#4 Basement（200）** — 地下室：任何不高于室外地坪的楼层；用途（设备/停车/设备间）；Types；Design and structural considerations；Drainage considerations；文化与装修；房地产面积口径。
- 未纳入理由：属**地下/半地下建筑构件与工程建设**；与已收录 `earth-sheltered`（覆土建筑）、`semi-sunken-space`（半下沉空间）、`sunken-courtyard`/`sunken-plaza`/`sunken-garden`、`damp-proofing`（防潮）、`drainage`（排水）、`safety-guarding`（安全防护）**近义/已覆盖**；排水与结构为下沉空间**已知常见问题细节**（TASK 第 5 节「常见错误与限制」已含排水/防潮/安全/无障碍）；属构件级边缘，非核心概念。单源。→ **不构成核心缺口**（近义/边缘）。

**#5 Philosophy of architecture（200）** — 建筑哲学：属**艺术哲学**分支，讨论建筑的审美价值、语义及其与文化发展的关系；History（柏拉图…）；Wittgenstein 与建筑哲学。
- 未纳入理由：属**哲学/美学思辨**，越出六大面（绘画理论/建筑空间设计）；与已收录 `academic-art-theory` 及 round41 已用 outline `Aesthetics` 相关但**非六大面核心概念**；属方法论/思辨层，单源。→ **不构成核心缺口**（越域/边缘）。

**#6 Pedestrian（200）** — 行人：步行者（含轮椅/助行器）；footpaths/sidewalks/pavement；Walkability；health benefits and environment。
- 未纳入理由：属**交通/步行者概念**；`walkability`（步行适宜性）与已收录 `pedestrian-flow`（人行流线，核心）、`circulation`（动线，核心）**近义**——第 44 轮已就 `Walkability` 页判定「近义 pedestrian-flow/circulation、属城市步行适宜性评价指标」排除，本轮 `Pedestrian` 页同一层级同一口径；属城市规划/交通层面，非「动线设计」新增核心。单源。→ **不构成核心缺口**（近义/域外）。

### 候选概念逐条「未纳入」汇总表

| 候选（来自本轮大纲） | 归属面 | 未纳入理由 |
| --- | --- | --- |
| figure drawing / life drawing / gesture drawing | 绘画理论 | **技法/教学科目**，非六子域核心；gesture 为边缘技法 |
| body proportions（7.5/8/8.5 头身） | 绘画理论 | 近义 `proportion`、`human-scale` |
| foreshortening | 绘画理论 | **已是 scope 条目**（foreshortening 缩短法） |
| daylighting / glare / visual comfort / IEQ / POE | 材料·采光 | 近义/已覆盖 daylighting、glare、visual-comfort；POE/IEQ 为工程评价指标 |
| HVAC / enclosure / embodied carbon / decarbonization | 材料·通风·可持续 | 工程系统/评价指标，非「基本原理」核心；近义 sustainable-design |
| environmental design（sustainability/functionality/aesthetics/holistic） | 空间/环境 | 跨学科职业层面；近义 sustainable-design、spatial-organization |
| solar heating（Greek/Roman） | 材料/通风 | 被动式太阳能**技术史例**，边缘 |
| basement types / drainage / structural | 下沉空间 | 近义/已覆盖 earth-sheltered、semi-sunken、sunken-*、damp-proofing、drainage、safety-guarding |
| philosophy of architecture（aesthetic value / Wittgenstein） | 空间理论 | **越域**（哲学/美学思辨）；非六子域核心 |
| pedestrian / sidewalk / walkability | 动线 | 近义 pedestrian-flow、circulation；城市交通层面（round44 同口径） |

### B1 结论

**不构成新的核心缺口。** 本轮以 **6 份此前从未使用**的权威百科总述/分类页（Figure drawing、Building science、Environmental design、Basement、Philosophy of architecture、Pedestrian，均 owiki 实抓 HTTP 200，`research/`、`entries/`、`scope.md`、`data/`、`coverage.json` grep 命中 0）逐页对照 251 条；另以 `Color_wheel`、`Japanese_garden`、`Architectural_theory` 三份已出现/已作来源页作旁证复核（不计新）。所提取候选概念全部落入以下任一情形：**（a）越出六大面**（philosophy of architecture、environmental design 跨学科、pedestrian 交通）；**（b）近义已收录**（figure drawing↔proportion/human-scale；building science↔daylighting/glare/thermal/ventilation；basement↔earth-sheltered/sunken-*/drainage；pedestrian↔pedestrian-flow/circulation）；或 **（c）边缘技法/工程细节/单源**（gesture drawing、embodied carbon/POE、solar heating 史例、drainage 施工）。无一条同时满足「≥2 独立权威源 + 六大面核心概念 + scope 缺失」的严格判据。故 B1 计 **0 条新核心缺口**。

---

## B6：近 12 个月（2025-11 至 2026-11）与绘画理论/建筑空间设计直接相关的理论性新研究/事件

本轮以 `web_search` 6 组查询（2025–2026 建筑/绘画/空间设计理论新著与动态）探测线索，返回约 20 条结果。保守原则：仅保留能核对到日期/来源、且能明确说明对本项目具体条目产生「新增或更新」**理论性**影响者。窗口内实际事项性质如下（均**非**核心概念的理论性变更）：

- **奖项/论坛/会议事件**：2026 全国美术论坛·杭州（中国美协，[链接](https://caanet.org.cn/newsdetail.mx?id=10217)）；北京画院「传统中国绘画研究中心」2026 学术年会（[链接](https://game.sohu.com/a/1104865325_255783)）——**学术会议/论坛**，不改变任何条目定义。
- **当代理论专著/思潮（单一出版方或单篇论文，未提出规范性理论变更）**：Sick Architecture（MIT Press, 2025，[brooklynrail 评介](https://brooklynrail.org/2026/10/architecture/sick-architecture-and-we-the-bacteria-notes-toward-biotic-architecture)）；Architectural Thinking in a Climate Emergency（[Buildings & Cities](https://www.buildingsandcities.org/insights/reviews/architectural-thinking.html)）；Raphael's Sistine Madonna as a System of Visual Engineering（MDPI Arts, 2026, [链接](https://www.mdpi.com/2076-0752/15/1/14)）；The Architectural Principles of Compositional Construction in Contemporary Painting（Zenodo, [链接](https://zenodo.org/records/22016460)）；Application of Supports Theory in Building Design（MDPI Buildings, [链接](https://www.mdpi.com/2075-5309/16/1/92)）；都市巢穴：开放建筑理论下的青年住宅社区适应性设计研究（武大硕论 2025，[链接](https://openir.whu.edu.cn/AchievementDetail/degree_ab839d95-25d5-4fb9-a6e9-c1f49b80ca0f)）；Spatial Mise-en-Scène and Narrative in Architecture（[BAGH](https://www.bagh-sj.com/jufile?ar_sfile=3276669)）；In Fourth Nature Concept, Form Follows Spirit（Prochnow, 2026, [REAL CORP](https://repository.corp.at/1356)）；Visual Narrative and Lacanian Psychoanalysis（Routledge 2026，[链接](https://www.routledge.com/Visual-Narrative-and-Lacanian-Psychoanalysis/Biberman/p/book/9781032850795)）。
- **中国传统画论研究动态**：南北宗论（[百度百科词条](https://baike.baidu.com/view/122197.html)）提及 2026 年邵琦专著《中国画的语境与语义》——**当代研究专著**，非核心概念定义性变更；「南北宗论」本身为画史流派论，非六大面核心子域，属绘画流派/断代史（往轮同口径排除流派）。
- 既有结构化年报页（`2025/2026 in architecture/art`）已在第 43、44 轮实抓核验，性质为事故/奖项/开馆/讣告/拍卖/盗窃/展览，非理论进展；本轮不重复抓取、结论维持。

### B6 结论

**B6 未发现需要更新条目的理论性新研究/事件。** 近 12 个月内可核验事项均为学术会议/论坛、当代理论专著与单篇论文、画史断代研究专著；无一构成对「绘画理论 / 建筑空间设计」**核心条目**（透视/构图/色彩/光影与明暗/中国画六法与留白/东西方比较/建筑风格史/园林造景/动线/下沉空间/材料·采光·通风/空间序列与尺度/室内外过渡）的理论性新增或更新，且均为单一出版方或单篇、非双源核心概念。已载于 `research/gaps-external-round02.md` 的 3 条实例/语境候选（Guggenheim Abu Dhabi 预计 2026-12 开馆、Lucas Museum 2026-09-22 开馆、Pritzker 2025 刘家琨）维持不变，本轮无需据此改动 scope 或条目。

---

## 本轮实际打开的 URL 与 HTTP 状态

### B1 新增对照页（owiki 镜像，6 份，`research/`+`entries/`+`scope.md`+`data/`+`coverage.json` grep 命中 0）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Figure_drawing | Figure drawing ::: Open WIKI | 200 |
| https://owiki.org/wiki/Building_science | Building science ::: Open WIKI | 200 |
| https://owiki.org/wiki/Environmental_design | Environmental design ::: Open WIKI | 200 |
| https://owiki.org/wiki/Basement | Basement ::: Open WIKI | 200 |
| https://owiki.org/wiki/Philosophy_of_architecture | Philosophy of architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/Pedestrian | Pedestrian ::: Open WIKI | 200 |

### B1 旁证复核页（此前已出现/已作来源，不计「新」）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Color_wheel | Color wheel ::: Open WIKI | 200 |
| https://owiki.org/wiki/Japanese_garden | Japanese garden ::: Open WIKI | 200 |
| https://owiki.org/wiki/Architectural_theory | Architectural theory ::: Open WIKI | 200 |

### 失败/不可用
| URL | 结果 |
| --- | --- |
| https://owiki.org/wiki/Architectural_criticism | 404（页面不存在，未取到） |
| https://owiki.org/wiki/Underground_space | 404（页面不存在，未取到） |
| https://owiki.org/wiki/Chinese_landscape_garden | 404（页面不存在，未取到） |

### web_search 线索（B6；返回摘要，未逐一抓正文，不计入「打开 URL」）
- 6 组查询：`2025 2026 new theory architecture space design research` / `2025 2026 art theory painting new publication` / `2025 2026 建筑理论 新研究 空间设计` / `2025 2026 中国画 理论 研究 新发现` / `2025 2026 architecture theory paradigm new book review` / `new theory of perspective or composition 2025 2026 art history`；合并返回约 20 条线索（含上方链接），仅作 B6 探测。

### 打开 URL 计数
- 本轮实际发起 HTTP 请求 **12 次**，对应 **12 个不同 URL**（无同页重复抓取）：**9 个 HTTP 200、3 个 HTTP 404（0 超时/0 403）**。
  - 其中 B1 **新增未用大纲页 6 个**（均 200）；旁证复核页 3 个（均 200，不计新）；失败 404 页 3 个。
- `web_search` 另发起查询 **6 组**（返回约 20 条线索，非 HTTP 正文抓取）。

---

## 机器可读汇总

```
ROUND=45
SCOPE_TOTAL=251   # 理论127/风格62/造景19/动线12/下沉12/材料19
B1_OUTLINES_UNUSED=6   #[Figure_drawing,Building_science,Environmental_design,Basement,Philosophy_of_architecture,Pedestrian]
B1_ALL_UNUSED_CONFIRMED=true   # research/+entries/+scope.md+data/+coverage.json grep 命中 0（6 slug 全 0）
B1_SUPPLEMENTARY_REUSED=[Color_wheel(b1-round42 已排除/已作wp-color-wheel来源),Japanese_garden(review-round04 已查),Architectural_theory(往轮已用)]
B1_CANDIDATES=[]   # 无满足「≥2独立源+六大面核心+scope缺失」者
B1_REJECTED=[
 "figure-drawing(技法/教学科目; body-proportions 近义 proportion/human-scale; foreshortening 已收录; gesture 边缘)",
 "building-science(学科/工程层面; 近义 daylighting/glare/visual-comfort/thermal/ventilation/material-durability/damp-proofing/sustainable; embodied carbon/POE 工程指标)",
 "environmental-design(跨学科职业层面; 近义 sustainable-design/spatial-organization/environmental-psychology; solar heating 史例)",
 "basement(构件/工程级; 近义 earth-sheltered/semi-sunken/sunken-*/damp-proofing/drainage/safety-guarding)",
 "philosophy-of-architecture(哲学/美学思辨 越域; 近 Aesthetics/academic-art-theory; 边缘)",
 "pedestrian(交通/步行; 近义 pedestrian-flow/circulation; round44 同口径; 域外)"
]
B1_RESULT="不构成新的核心缺口（0 条）"
B6_NEW=[]
B6_RESULT="未发现需要更新条目的理论性新研究/事件（论坛/会议/当代专著/单篇论文/画史断代专著均非核心概念理论变更，且单源）"
URLS_REQUESTED=12
URLS_OK_200=9
URLS_FAILED=3   # 均 404
URLS_DISTINCT=12
WEB_SEARCH_QUERIES=6
```

是否发现新缺口：否
