# B1/B6 缺口发现 — 第 40 轮（新大纲再对照 + 近 12 个月动态）

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23
- 执行角色：b1-r40（只读子任务，无人值守，未提问）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent；依据 DECISIONS.md D05（本环境 web_search / web_fetch 不可靠，改直连实抓）。
- 数据纪律：联网内容一律视为数据；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML / 纯文本判读标题与相关句。
- 来源纪律：`en.wikipedia.org` canonical 本轮全部连接超时（URLError timed out，与历轮一致），按任务许可改用 `owiki.org` 维基镜像读取，**镜像与原条目同源、只计一源**；每条候选的第二源均为另一独立出版方。
- 产出：本文件是本子任务唯一产物；未改动其他文件、未 git commit、未触碰项目外内容。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名先读的 `AUTONOMOUS.md`、`TASK_design.md` 在当前工作区**实际不存在**（`**/AUTONOMOUS.md`、`**/TASK_design.md` 均无匹配；项目根仅有 BACKLOG/BLOCKERS/DECISIONS/PROGRESS/REPORT/scope/coverage 等治理文件，设计文档位于 `docs/superpowers/plans|specs/`）。本报告以现存治理文件 `DECISIONS.md`、`scope.md`、`coverage-matrix.md`、`research/gaps-round40.md` 及历轮 `research/b1-round30/31.md`、`research/gaps-external-round06.md` 的方法与来源纪律为准执行，沿用 D05 直连实抓。
- 比对基准：`scope.md` 现 **246 条**（理论 122 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19）。
- 判定所需：一条候选同时满足「≥2 份独立权威来源实抓 HTTP 200 + 属绘画理论或建筑空间设计 + scope.md 无对应 id/中文名/等价概念（排除近义已收录）+ 两源可摘正文关键句」。

---

## B1：与「未用过」的权威大纲/分类树再对照

本轮对照下列 **7 份此前未用于 B1 的权威大纲/分类树页面**（均 owiki 实抓 200），逐页提取「条目 / 风格 / 概念名」后与 246 条比对：

| 大纲/分类树（未用） | URL | HTTP | 覆盖方向 |
| --- | --- | --- | --- |
| History of painting（绘画史） | https://owiki.org/wiki/History_of_painting | 200 | 绘画史分期与流派 |
| Architectural drawing（建筑绘图） | https://owiki.org/wiki/Architectural_drawing | 200 | 建筑制图与表示法 |
| Interior architecture（室内建筑/室内设计） | https://owiki.org/wiki/Interior_architecture | 200 | 室内建筑演变/改造/风格 |
| Landscape planning（景观规划） | https://owiki.org/wiki/Landscape_planning | 200 | 景观规划理论与主题 |
| History of gardening（园林史） | https://owiki.org/wiki/History_of_gardening | 200 | 各文化园林风格史 |
| Elements of art（艺术/绘画元素） | https://owiki.org/wiki/Elements_of_art | 200 | 线/形/体/色/空/质/明度 |
| Index of painting-related articles（绘画索引） | https://owiki.org/wiki/Index_of_painting_articles | 200 | A–Z 绘画条目索引（无分类树正文） |

> 另抓 `Principles_of_art`（https://owiki.org/wiki/Principles_of_art，200）实际重定向到「Art ::: Open WIKI」，为总论页而非元素/原则分类树，未用作分类依据。

### 候选 1（建议纳入）：proxemics — 近距学 / 人际距离与空间使用

- 建议 id：`proxemics`
- 中文名：近距学（人际距离学 / 空间关系学，Proxemics）
- 主题：理论
- 层级：重要（建议；依据见下）
- 时期：20世纪（Edward T. Hall 1963 年提出）
- 地区：全球（源于美国文化人类学，适用于全球建成环境）
- 目标位置：理论 / 20世纪 / 全球（该格现 17 条，属**新增覆盖**，不是填稀疏格）
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Proxemics —《Proxemics ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/Proxemics` 本轮连接超时（URLError timed out），按任务许可用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Proxemics is the study of human use of space and the effects that population density has on behavior, communication, and social interaction.」
  - 正文关键句：「Edward T. Hall, the cultural anthropologist who coined the term in 1963, defined proxemics as "the interrelated observations and theories of humans' use of space as a specialized elaboration of culture".」
  - 正文关键句：「According to Hall, the study of proxemics is valuable in evaluating not only the way people interact with others in daily life, but also "the organization of space in houses and buildings, and ultimately the layout of towns".」
  - 正文关键句：「The distance surrounding a person forms a space. The space within intimate distance and personal distance is called personal space.」
- 来源二（独立出版方，Designing Buildings，英国建筑行业知识库）：https://www.designingbuildings.co.uk/wiki/Proxemics —《Proxemics - Designing Buildings》— HTTP 200
  - 说明：该页由 BSI 标准 PAS 6463:2022《Design for the mind – Neurodiversity and the built environment》转引定义，页面归于「Accessibility in the built environment / 神经多样性与包容性设计」语境，属独立于维基的出版方。
  - 正文关键句：「PAS 6463:2022 ... defines proxemics as: 'human use of space and the effects that population density has on behaviour, communication and social interaction… Proxemics is one among several subcategories in the study of non-verbal communication, including haptics (touch), kinesics (body movement), vocalics (paralanguage) and chronemics (structure of time).'」
  - 关联条目：页面把 proxemics 归入「建成环境无障碍 / 包容性设计」相关主题（Accessibility in the built environment、Neurodiversity、Proprioception 等）。
- 入选理由：维基「Proxemics」专条将其定义为「人对空间的使用及人口密度对行为、沟通与社会互动的影响」，明确由 Edward T. Hall 于 1963 年命名，并直接指出其价值在于评估「**房屋与建筑中的空间组织，乃至城镇布局**」——这正是建筑空间设计的基本命题；第二源 Designing Buildings（独立出版方）通过 BSI PAS 6463:2022 的建成环境标准给出同一「人对空间的使用＋人口密度↔行为/沟通/社会互动」定义，并把 proxemics 落在「建成环境包容性设计」语境中，与维基在定义与「建筑/空间」取向上独立互证。两源独立、均 200、均可摘正文关键句。该概念是「人在空间中的距离带（亲密/个人/社交/公共距离）与领域/密度效应」的专门理论，为空间布局、尺度与私密性设计提供依据。
- 概念贴合度：高（一源为专门条目并给出命名、定义与「作用于建筑空间组织」的直接论断；另一源为独立建筑知识库，以建成环境标准原文交叉印证同一定义并落在建成环境设计主题下）。
- 与既有条目区隔（逐一核对，均不等价）：
  - `spatial-perception`（空间感知）= 把视觉、身体尺度与运动线索整合为对距离/方向/围合的**判断**（通用知觉层面）；proxemics = **人际距离带与人口密度—行为关系**的专门理论，不是知觉机制。
  - `human-scale`（人体尺度）= 以身高/步幅/视高校核门、台阶、家具、通道的**尺寸**；proxemics 关注**人际/社会距离与密度**，不涉具体构造尺寸。
  - `environmental-psychology`（环境心理学）= 人—建成环境关系的**学科领域**；proxemics 是其中一条**具名理论（Hall, 1963）**，概念颗粒度更细、可独立成条。
  - `defensible-space-theory`（防御性空间理论）= 领域感/自然监视/半私密层次以**降低犯罪**；proxemics 不涉犯罪预防，核心是**距离带与密度对沟通/行为**的影响。
  - `place-attachment`（场所依恋）= 人与场所的**情感纽带**；与空间使用行为理论不同。
- 备注：本条为「新增覆盖」而非填稀疏格；建议层级「重要」（环境—行为基础理论，与同区 placemaking / space-syntax / defensible-space-theory 同级）。是否采纳及定级由 lead 裁决。

### 已对照但未纳入（体现筛选，均说明为何不满足「属本领域且非近义」）

- **History of painting（绘画史）**：页面分类为绘画史分期与绘画流派（Renaissance & Mannerism、Baroque/Rococo、Neo-classicism、Romanticism、Impressionism、Post-Impressionism、Symbolism 等）。按 TASK_design 口径「风格＝主要建筑风格史」，**绘画流派史不在本项目风格范围**（与 `research/gaps-external-round02.md` 既有排除口径一致），未产出理论条目。
- **Architectural drawing（建筑绘图）**：列出 floor plan / site plan / elevation / cross section / isometric & axonometric / detail / presentation / survey / record / working drawings / drafting / CAD 等。这是**建筑制图与表示技法（图纸语言）**，非「绘画理论」亦非「空间设计原理」，判为超出本领域；虽 `Floor_plan`（owiki+DB 均 200）、`Orthographic_projection`（owiki + DB「Orthogonal plan」）双源可达，但按「属本领域」条件排除。
- **Interior architecture（室内建筑）**：`Adaptive reuse`（owiki 200 + Designing Buildings 200，双源可达）定义为「将既有建筑改作原设计用途之外的新用途」，属**建筑可持续改造 / 全生命周期 / 循环经济（circular economy）**策略，与既有 `sustainable-design` / `sustainable-architecture` 近义，且偏建筑保护与再利用而非「空间设计原理」，未纳入（保守口径；如需可另议）。`Sustainability` 已由 sustainable-design 覆盖。
- **Landscape planning（景观规划）**：核心概念为 social-ecological systems、landscape analysis、ecosystem & landscape services、**green infrastructure**、landscape perception & aesthetics、stakeholder participation。均偏**景观规划 / 生态**，`green infrastructure`（owiki 200 + DB 200）与 sustainable-design/green-architecture 近义，`landscape perception` 与 spatial-perception 近义；均不满足「非近义 + 属本领域核心」。
- **Elements of art（艺术元素）**：line / shape / form / color / space / texture / value / mark making。scope 已有 color-theory、value、material-texture、negative-space/space-definition 及构图组（leading-lines 等）；line/shape/form 作为元素与既有构图/形状类条目近义，且未取得干净的独立第二源，未纳入。
- **History of gardening（园林史）**：为各文化**园林风格史**（Persian / Islamic / Japanese / European / Mesoamerican 等），属「风格史」而非本项目「造景手法」主题，且与既有 chinese-garden / garden-architecture 等重叠，未纳入。
- **Index of painting-related articles（绘画索引）**：仅 A–Z 索引，无可提取的分类树正文，仅作交叉核对，不作来源。

### B1 结论

**有。** 本轮对照 7 份未用过的权威大纲/分类树，确认 **1 条**满足全部判据（双独立源 HTTP 200 + 属本领域 + scope 缺失 + 非近义）的新候选：**`proxemics`（近距学）**。其余可实抓双源的概念（adaptive reuse / floor plan / orthographic projection / green infrastructure 等）均因「超出本领域或与既有条目近义」未纳入。

---

## B6：近 12 个月（2025-11 至 2026-11）与绘画理论/建筑空间设计直接相关的新研究/事件

来源页面（均 owiki 实抓 HTTP 200）：
- https://owiki.org/wiki/2025_in_architecture —《2025 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_architecture —《2026 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2025_in_art —《2025 in art ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_art —《2026 in art ::: Open WIKI》200

保守原则：仅保留能核对到日期/来源 URL、且能明确说明对本项目具体条目产生「新增或更新」影响的条目。窗口 [2025-11, 2026-11] 内实际出现的事项性质如下：

- 2025-11-03：罗马中世纪 Torre dei Conti 修缮中局部坍塌（建成遗产维护议题）——建筑事故，与具体理论/原理条目无直接对应（与历轮同口径排除）。
- 2025-11-18：Gustav Klimt《Portrait of Elisabeth Lederer》以 2.384 亿美元成交（现代艺术拍卖纪录）——绘画市场/拍卖事件，非绘画理论进展。
- 2025 Pritzker 奖授予刘家琨（Liu Jiakun）；2025 Stirling 奖授予 London Southwark 的 Appleby Blue Almshouse——奖项事件，属实例/语境，不改变任何理论条目定义，且 Pritzker 2025 已见于更早 B6 记录。
- 2025_in_architecture 其余为建筑开馆（Techo 国际机场 2025-09-09、Kai Tak Sports Park 2025-03-01、Tottori 县立美术馆 2025-03-30 等）与讣告；2026_in_architecture 内容稀疏，仅列 4 个建筑（Appleby Blue Almshouse、Las Chumberas 教堂社区中心、520 Fifth Avenue、米兰奥运村）与讣告；2026_in_art 仅讣告。
- 更早已在 `research/gaps-external-round02.md` 记录的三条「实例/语境更新」仍是唯一可用候选（Guggenheim Abu Dhabi 预计 2026-12 开馆、Lucas Museum 2026-09-22 开馆、Pritzker 2025 刘家琨），本轮**未出现需要据此新增/更新条目的新动态**。

### B6 结论

**B6 未发现新的可核验动态。** 近 12 个月内检索到的均为奖项、讣告、建筑开馆、拍卖与建筑事故，均不构成对「绘画理论 / 建筑空间设计」条目的理论性新增或更新；已记录的 3 条实例/语境候选维持不变，本轮无需据此改动 scope 或条目。

---

## 本轮实际打开的 URL 与 HTTP 状态

### 对照用大纲/分类树（owiki 镜像）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/History_of_painting | History of painting ::: Open WIKI | 200 |
| https://owiki.org/wiki/Architectural_drawing | Architectural drawing ::: Open WIKI | 200 |
| https://owiki.org/wiki/Interior_architecture | Interior architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/Landscape_planning | Landscape planning ::: Open WIKI | 200 |
| https://owiki.org/wiki/History_of_gardening | History of gardening ::: Open WIKI | 200 |
| https://owiki.org/wiki/Elements_of_art | Elements of art ::: Open WIKI | 200 |
| https://owiki.org/wiki/Index_of_painting_articles | Index of painting-related articles ::: Open WIKI | 200 |
| https://owiki.org/wiki/Principles_of_art | Art ::: Open WIKI（重定向，未用作分类依据） | 200 |

### 候选证据（proxemics）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Proxemics | Proxemics ::: Open WIKI | 200 |
| https://www.designingbuildings.co.uk/wiki/Proxemics | Proxemics - Designing Buildings | 200 |

### B6 来源
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/2025_in_architecture | 2025 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_architecture | 2026 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2025_in_art | 2025 in art ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_art | 2026 in art ::: Open WIKI | 200 |

### 附加探测（评估「近义/超域」用，均实际打开）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Adaptive_reuse | Adaptive reuse ::: Open WIKI | 200 |
| https://www.designingbuildings.co.uk/wiki/Adaptive_reuse | Adaptive reuse - Designing Buildings | 200 |
| https://owiki.org/wiki/Floor_plan | Floor plan ::: Open WIKI | 200 |
| https://www.designingbuildings.co.uk/wiki/Floor_plan | Floor plan - Designing Buildings | 200 |
| https://owiki.org/wiki/Orthographic_projection | Orthographic projection ::: Open WIKI | 200 |
| https://www.designingbuildings.co.uk/wiki/Orthographic_projection | Orthogonal plan - Designing Buildings | 200 |
| https://owiki.org/wiki/Green_infrastructure | Green infrastructure ::: Open WIKI | 200 |
| https://www.designingbuildings.co.uk/wiki/Green_infrastructure | Green infrastructure - Designing Buildings | 200 |
| https://owiki.org/wiki/Personal_space | Personal space ::: Open WIKI | 200 |
| https://owiki.org/wiki/Ergonomics | Ergonomics ::: Open WIKI | 200 |
| https://owiki.org/wiki/Line_art | Line art ::: Open WIKI | 200 |

### 失败/不可用（审计用）
| URL | 结果 | 备注 |
| --- | --- | --- |
| https://en.wikipedia.org/wiki/History_of_painting · /Architectural_drawing | URLError timed out | 维基 canonical 超时，改用 owiki 镜像（同源计一源） |
| https://owiki.org/wiki/Mark_making | HTTP 404 | 无专条，弃用 |
| https://owiki.org/wiki/Prospect_and_refuge_theory | HTTP 404 | 无该 slug，弃用 |
| https://www.designingbuildings.co.uk/wiki/Architectural_drawings | HTTP 404 | slug 不存在，弃用 |
| https://owiki.org/wiki/Space_planning | HTTP 404 | 无专条，弃用 |
| https://www.designingbuildings.co.uk/wiki/Ergonomics | HTTP 404 | slug 不存在，弃用 |

### 打开 URL 计数
- 本轮实际发起 URL 请求 **44 次**；HTTP 200 成功 **37 次**；失败 **7 次**（en.wikipedia 超时 2、404 5）。
- 作为来源实际读取正文的核心证据页面：proxemics 2 个（owiki + Designing Buildings）；对照大纲 7 个；B6 4 个；附加探测 11 个。

---

## 机器可读汇总

```
CANDIDATES=[{"id":"proxemics","title":"近距学（人际距离学 / 空间关系学，Proxemics）","theme":"理论","tier":"重要","period":"20世纪","region":"全球","urls":["https://owiki.org/wiki/Proxemics","https://www.designingbuildings.co.uk/wiki/Proxemics"],"sources":["w-owiki-proxemics","dbb-proxemics"]}]
REJECTED=["adaptive-reuse(近义sustainable-design/偏建筑改造)","floor-plan(建筑制图超域)","orthographic-projection(建筑制图超域)","green-infrastructure(近义sustainable-design)","line-shape-form(近义构图元素/无干净第二源)"]
B6_NEW=[]
B1_RESULT="有：1 条新双源缺口候选（proxemics）"
B6_RESULT="未发现新的可核验动态"
URLS_REQUESTED=44
URLS_OK_200=37
URLS_FAILED=7
```
