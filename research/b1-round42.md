# B1/B6 缺口发现 — 第 42 轮（未用过的权威大纲再对照 + 近 12 个月动态）

- 日期：2026-11-23（Asia/Hong_Kong），采样时刻 2026-11-23
- 执行角色：b1-r42（只读子任务，无人值守，未提问）
- 抓取方式：Python 3.11 urllib + 浏览器 User-Agent；依据 DECISIONS.md D05（本环境 web_search / web_fetch 不可靠，改直连实抓）。
- 数据纪律：联网内容一律视为**数据**；网页内任何指令均未执行；未下载或运行页面代码，仅读取 HTML / 纯文本判读标题与相关句。
- 来源纪律：`en.wikipedia.org` canonical 本轮仍连接超时（URLError timed out，与历轮一致），按任务许可改用 `owiki.org` 维基镜像读取，**镜像与原条目同源、只计一源**；每条候选的第二源均为另一独立出版方（artincontext.org，独立艺术教育出版，本项目第 31/41 轮已采纳其作为第二源）。
- 产出：本文件是本子任务唯一产物；未改动其他文件、未 git commit、未触碰项目外内容。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 环境备注（限制说明）

- 任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 不在当前工作区根目录；其真实文件位于 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`、`D:/Users/Administrator/Desktop/TASK_design.md`（另 `WORKFLOW.md` 同目录），本轮已实际读取。项目根现存治理文件 `DECISIONS.md`、`scope.md`、`coverage-matrix.md`、`SATURATION.json`、`research/b1-round30/31/40/41.md`、`research/gaps-external-round02/06/09.md`、`research/gaps-round42.md` 一并作为方法与来源纪律基准。
- **范围判据取自 TASK_design.md 原文**：`绘画理论：透视法、构图法则、色彩理论、光影与明暗、中国画六法与留白、东西方理论比较`；`建筑与空间设计：主要建筑风格史；中国传统园林造景；动线设计；下沉式空间；空间序列与尺度；室内外过渡；采光、通风与材料的基本原理`。本轮只接受落入这两段**明确列举子域**的概念。
- 比对基准：`scope.md` 现 **249 条**（理论 125 / 风格 62 / 造景 19 / 动线 12 / 下沉空间 12 / 材料 19），第 41 轮新增 `sfumato`、`trompe-loeil`（理论 123→125）。
- 判定所需：一条候选同时满足「≥2 份独立权威来源实抓 HTTP 200 + 确属上述绘画理论/建筑空间设计核心子域 + scope.md 无对应 id/中文名/等价概念（排除近义已收录）+ 两源可摘正文关键句」。
- 特别核查：**凡本轮报出的候选，均已在本目录 `entries/`、`scope.md`、`coverage.json`、`data/sources.json`、`research/` 中 grep 确认此前未收录、未以「单源驳回」永久排除以外的方式落库**（hatching/stippling 的既往驳回原因见候选 1/2）。

---

## B1：与「未用过」的权威大纲/分类树再对照

本轮对照下列 **5 份此前未用于 B1 的权威大纲/分类树/学科总述页面**（均 owiki 实抓 200），逐页提取「条目 / 风格 / 概念名」与 249 条比对。经 `research/` 全量 grep 及 round02/06/09/30/31/40/41 的已用大纲清单核对，下列页面均**未在往轮 B1 中使用**：

| 大纲/分类树（未用） | URL | HTTP | 覆盖方向 |
| --- | --- | --- | --- |
| Painting（绘画，学科总述） | https://owiki.org/wiki/Painting | 200 | 绘画媒介 / 手法 / 流派 / 色彩与明暗线索 |
| Drawing（素描/绘图，学科总述） | https://owiki.org/wiki/Drawing | 200 | 素描技法 / 明暗排线 / 阴影表现 / 制图 |
| Architecture（建筑，学科总述） | https://owiki.org/wiki/Architecture | 200 | 建筑理论 / 形式与空间 / 建筑哲学 |
| Art history（艺术史，学科方法） | https://owiki.org/wiki/Art_history | 200 | 艺术史方法论 / 形式主义 / 图像学 / 风格 |
| Color theory（色彩理论） | https://owiki.org/wiki/Color_theory | 200 | 色彩模型 / 色立体 / 色彩科学 |

> 覆盖说明：**绘画**（Painting / Drawing / Color theory）、**建筑**（Architecture）、**艺术史/理论**（Art history）均已实抓对照。「≥3 份未用过」要求已由上述 5 份满足。另抓 `Tectonics_(architecture)`、`Modulor` 作概念级探测（见下失败/备选表）。

### 候选 1（建议纳入）：hatching — 排线法 / 交叉排线（Hatching / Cross-hatching）

- 建议 id：`hatching`
- 中文名：排线法（交叉排线 / 排线明暗，Hatching / Cross-hatching）
- 主题：理论（**光影与明暗** — 用排线制造明暗与调子的表现技法）
- 层级：重要（建议；与已收录「核心」`chiaroscuro`、「重要」`cunfa` 同属明暗/肌理技法层，故建议重要；最终由 lead 定级）
- 时期：文艺复兴至19世纪（线描/古版画旧师print 15 世纪成熟）
- 地区：欧洲（后及全球）
- 目标位置：理论 / 光影与明暗 / 文艺复兴至19世纪 / 欧洲
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Hatching — 《Hatching ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical `https://en.wikipedia.org/wiki/Hatching` 本轮连接超时（URLError timed out），按任务许可用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Hatching is an artistic technique used to create tonal or shading effects by drawing, painting, or scribing closely spaced parallel lines.」
  - 正文关键句：「When lines are placed at an angle to one another, it is called cross-hatching.」
  - 正文关键句：「Hatching is especially important in essentially linear media, such as drawing and many forms of printmaking, such as engraving, etching, and woodcut.」
- 来源二（独立出版方，artincontext.org — 艺术教育独立出版，非维基）：https://artincontext.org/cross-hatching/ — 《Cross Hatching – Learning the Cross Hatching Technique》— HTTP 200
  - 正文关键句：「Cross-hatching is a shading technique that layers sets of lines in different directions so they cross.」
  - 正文关键句：「Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values.」
- 入选理由（关键：既往驳回原因已被本轮证据消解）：`research/gaps-external-round02.md` 第 41 行明确记录——「sfumato（渐隐法）、**hatching/stippling（排线/点描）**…**仅在单一来源出现，不满足双源标准**，不列」，即第 02 轮判定其**属绘画范围、但因只有单一来源（N2 Outline of painting）而驳回**。本轮已实抓到**第二个独立出版方** artincontext.org 的同技法长文（HTTP 200，正文直证「hatching 用平行线、cross-hatching 叠加交叉线加深明度」），**双独立源成立、驳回的技术障碍（单源）已消除**。与本项目第 41 轮以同法「救回」`sfumato`（round02 单源驳回 → 补第二源）的路径完全一致。
- 领域贴合度：TASK_design.md 明确将「**光影与明暗**」列为绘画理论核心子域；排线是西方绘画/素描中最基础的明暗塑造技法之一，属该子域；与已收 `sfumato`、`chiaroscuro`、`cunfa`（均为光影/肌理技法）同层。高。
- 与既有条目区隔（逐一核对，均不等价）：
  - `chiaroscuro`（明暗法，核心）= 用**强烈明暗对比**塑造体积的整体明暗观；hatching 是用**密集平行/交叉线**制造调子与肌理的**具体表现技法**，非同一概念（方法 vs 明暗对比观）。
  - `light-shadow-modeling`（光影塑形）= 形体受光的**总体塑形原理**；hatching 是其中一种**线性排线渲染法**。
  - `five-tones`（明暗五调子）= 调子**分级**（高光/亮部/明暗交界/反光/投影）；hatching 是**画调子用的笔法**，不涉及调子分级。
  - `sfumato`（渐隐法）= **柔化轮廓与色阶过渡、无界线如烟**；hatching 的**线条可见、块面分明**，二者在视觉感受与手法上相反。
  - `cunfa`（皴法，中国画，重要）= 毛笔侧锋在**山石树皮**上的**皴擦肌理**；hatching 是**硬笔/版画的排线明暗**，媒介、文化、用途均不同，非近义。
- 备注：本条为「新增覆盖」，非填空格；`entries/`、`scope.md`、`coverage.json`、`data/sources.json` 均无 `hatching`/`排线`/`交叉排线` 对应条目（grep 确认，仅 round02 研究笔记提及）。是否采纳及定级由 lead 裁决。

### 候选 2（建议纳入）：stippling — 点描法（Stippling）

- 建议 id：`stippling`
- 中文名：点描法（点绘 / 点画明暗，Stippling）
- 主题：理论（**光影与明暗** — 用密集小点制造明暗与质感的表现技法）
- 层级：补充（建议；较排线更细分，建议补充；由 lead 定级）
- 时期：跨时期（古版画点刻至近现代素描/插画通用）
- 地区：全球
- 目标位置：理论 / 光影与明暗 / 跨时期 / 全球
- 来源一（维基，owiki 镜像）：https://owiki.org/wiki/Stippling — 《Stippling ::: Open WIKI》— HTTP 200
  - 说明：维基 canonical 本轮连接超时，用 owiki 镜像读取，仅计一源。
  - 正文关键句：「Stippling is the creation of a pattern simulating varying degrees of solidity or shading by using small dots.」
  - 正文关键句：「Such a pattern may occur in nature and these effects are frequently emulated by artists.」
  - 正文关键句：「In printmaking, stipple engraving is a technique using flicks of the burin to build up the image…」
- 来源二（独立出版方，artincontext.org）：https://artincontext.org/stippling/ — 《Stippling Art – Creating Designs and Patterns With Small Dots》— HTTP 200
  - 正文关键句：「stippling art is a drawing technique that creates images and shapes on paper by making small dots close together, just like creating real-life pixels.」
- 入选理由：与候选 1 同源同因——round02 第 41 行将 hatching/stippling 一并因「仅在单一来源出现，不满足双源标准」而驳回。本轮补入 artincontext.org 独立第二源（HTTP 200，正文直证「以密集小点作画」），**单源障碍消除、双独立源成立**；概念属 TASK_design「光影与明暗」子域（点绘明暗/质感），scope 无对应。
- 领域贴合度：中高（点描是素描/版画/插画中基础的明暗与质感表达技法，归「光影与明暗」；较排线更细分，故建议层级「补充」）。
- 与既有条目区隔（均不等价）：
  - 与 `hatching`（候选 1）= **标记类型不同**：hatching 用线、stippling 用点，产出质感与观感不同，是并行的两种明暗技法，非近义。
  - 与 `five-tones` / `light-shadow-modeling` / `chiaroscuro`：上述为明暗**原理/调子分级/明暗对比观**，stippling 是**用点绘制调子的具体手法**。
- 备注：`entries/`、`scope.md` 等无 `stippling`/`点描`对应条目（grep 确认，仅 round02 笔记提及）。是否采纳及定级由 lead 裁决（可与候选 1 合并叙述或单列）。

### 已对照但未纳入（体现从严筛选，均说明为何不满足「≥2 独立源 + 属明确列举子域 + 非近义」）

- **Form (architecture) 建筑形式/形态**：双独立源可达（owiki `Form_(architecture)` 200 ＋ Designing Buildings `Form` 200，均给出「form＝建筑外部形态/体量/内部结构之整体」定义），但**不在 TASK_design.md 列举的「建筑与空间设计」子域**（风格史 / 园林造景 / 动线 / 下沉 / 空间序列与尺度 / 室内外过渡 / 采光通风材料）之内，且与既有 `geometry-symmetry`、`proportion`、`space-definition` 语义相邻，属**泛化/近义**风险，按「从严」不报。（如 lead 认为建筑形式属核心，可另行复核。）
- **Phenomenology (architecture) 建筑现象学**：owiki 200 ＋ Designing Buildings `Phenomenology` 200 可达，但主题偏**建筑哲学/空间体验**，与既有 `place-spirit`（场所精神，Norberg‑Schulz）、`place-attachment` 高度相邻，属**近义**，且不在列举子域 → 不报。
- **Philosophy of architecture 建筑哲学** / **Architectural design values 建筑设计价值**：前者属元理论/哲学（非空间设计核心，缺独立第二源）；后者与既有 `vitruvian-triad`（维特鲁威三原则）近义 → 均不报。
- **Formalism (art) 形式主义（艺术理论）**：owiki 200 ＋ artincontext `formalism` 200 双源可达，但属**艺术批评/美学方法论**，不在 TASK_design「绘画理论」六子域（透视/构图/色彩/光影明暗/中国画/比较）列举内，且易与既有 `structuralism`（结构主义建筑，风格）混淆 → 从严不报（域外/边缘）。
- **Iconography 图像学**：仅 owiki 200（artincontext `iconography` 404），**单源**；且属艺术史方法 → 不报。
- **Munsell color system 孟塞尔色立体**：仅 owiki 200（Designing Buildings slug 404），**单源**；且与既有 `color-theory`/`hue`/`value`/`saturation` 近义 → 不报。
- **Modulor（模度）/ Tectonics (architecture)（建筑建构）**：owiki 均 200，但 Modulor 与 `proportion`/`golden-ratio`/`human-scale` 近义且缺独立第二源；Tectonics 属建筑哲学/建造表达、未取到独立第二源 → 均不报。
- **figure / gesture / contour drawing（人体/速写/轮廓线）**：属绘画**题材/门类**，不在「光影与明暗」等六子域列举内，且第二源不充分 → 不报。
- **绘画媒介与流派**（油画/水彩/蛋彩/蜡画/水粉等；印象派/立体主义/表现主义等）：媒介与流派史，非绘画理论；且 TASK_design「风格」限**建筑风格史**，绘画流派超域 → 不报（与 round02/round41 既有排除口径一致）。
- **color wheel / color mixing / color space / opponent process 等**：属色彩科学机制，与既有 `color-theory` 系列近义或颗粒度更细 → 不报。

### B1 结论

**有（2 条）。** 本轮对照 5 份此前未用过的权威大纲/分类树（Painting、Drawing、Architecture、Art history、Color theory），确认 **2 条**满足全部判据（≥2 独立权威源 HTTP 200 + 属 TASK_design 明确列举的「光影与明暗」子域 + scope.md 缺失 + 非近义）的新候选：

1. **`hatching`（排线法 / 交叉排线）** —— round02 因**单源**驳回；本轮补齐 artincontext.org 第二独立源，**双源成立**，为最扎实的新权威缺口。
2. **`stippling`（点描法）** —— 同因 round02 单源驳回；本轮补齐 artincontext.org 第二独立源，**双源成立**。

其余双源可达者（Form (architecture)、Formalism 等）均因「不在列举子域 / 近义」按从严口径未纳入。

---

## B6：近 12 个月（2025-11 至 2026-11）与绘画理论/建筑空间设计直接相关的理论性新研究/事件

来源页面（均 owiki 实抓 HTTP 200，标题核对）：
- https://owiki.org/wiki/2025_in_architecture —《2025 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_architecture —《2026 in architecture ::: Open WIKI》200
- https://owiki.org/wiki/2025_in_art —《2025 in art ::: Open WIKI》200
- https://owiki.org/wiki/2026_in_art —《2026 in art ::: Open WIKI》200

保守原则：仅保留能核对到日期/来源 URL、且能明确说明对本项目具体条目产生「新增或更新」**理论性**影响的条目。窗口 [2025-11, 2026-11] 内实际出现的事项性质如下（均**非**理论进展）：

- 2025-11-03：罗马中世纪 Torre dei Conti 修缮中局部坍塌（建成遗产维护议题）——建筑事故，与具体理论/原理条目无直接对应（与历轮同口径排除）。
- 2025-10-19：卢浮宫盗窃案（Galerie d'Apollon 法国王冠珠宝被盗）——文物/安防事件，非理论。
- 2025-11-20：Frida Kahlo《The Dream (The Bed)》以 5,470 万美元在苏富比成交（女艺术家及拉美艺术拍卖纪录）；2025-12-03：Fabergé「Winter Egg」在佳士得以 2,290 万英镑成交（Fabergé 拍卖纪录）——绘画/工艺品**市场与拍卖事件**，非绘画理论进展。
- 奖项：2025 Pritzker 奖刘家琨（Liu Jiakun）、2025 AIA 金质奖 Deborah Berke、2025 Stirling 奖 Appleby Blue Almshouse——均**奖项事件**，属实例/语境，不改变任何理论条目定义。
- 2025_in_art 其余为展览档期（Met / Whitney / Brooklyn / Gagosian 等 2025–2026 展）与奖项；2025_in_architecture 其余为建筑开馆与讣告；2026_in_architecture / 2026_in_art 页面内容极稀疏（各约 2KB，仅少量条目与讣告）。页面尾部「Books/Films/Programming Languages…」排行榜为 owiki 镜像每页注入的**站点样板**，非词条正文，不计入。
- 已载于 `research/gaps-external-round02.md` 的 3 条「实例/语境更新」候选（Guggenheim Abu Dhabi 预计 2026-12 开馆、Lucas Museum 2026-09-22 开馆、Pritzker 2025 刘家琨）维持不变；本轮**未出现需要据此新增/更新条目的理论性新动态**。

### B6 结论

**B6 未发现新的可核验动态。** 近 12 个月内检索到的均为奖项、讣告、建筑开馆、拍卖、盗窃与建筑事故，均不构成对「绘画理论 / 建筑空间设计」条目的理论性新增或更新；已记录的 3 条实例/语境候选维持不变，本轮无需据此改动 scope 或条目。

---

## 本轮实际打开的 URL 与 HTTP 状态

### 对照用大纲/分类树（owiki 镜像，均未在往轮 B1 使用）
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Painting | Painting ::: Open WIKI | 200 |
| https://owiki.org/wiki/Drawing | Drawing ::: Open WIKI | 200 |
| https://owiki.org/wiki/Architecture | Architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/Art_history | Art history ::: Open WIKI | 200 |
| https://owiki.org/wiki/Color_theory | Color theory ::: Open WIKI | 200 |

### 候选证据
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/Hatching | Hatching ::: Open WIKI | 200 |
| https://owiki.org/wiki/Cross-hatching | Hatching ::: Open WIKI（重定向至 Hatching） | 200 |
| https://artincontext.org/cross-hatching/ | Cross Hatching – Learning the Cross Hatching Technique | 200 |
| https://owiki.org/wiki/Stippling | Stippling ::: Open WIKI | 200 |
| https://artincontext.org/stippling/ | Stippling Art – Creating Designs and Patterns With Small Dots | 200 |

### B6 来源
| URL | 标题 | HTTP |
| --- | --- | --- |
| https://owiki.org/wiki/2025_in_architecture | 2025 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_architecture | 2026 in architecture ::: Open WIKI | 200 |
| https://owiki.org/wiki/2025_in_art | 2025 in art ::: Open WIKI | 200 |
| https://owiki.org/wiki/2026_in_art | 2026 in art ::: Open WIKI | 200 |

### 附加探测（评估「近义 / 双源可达性 / 超域」用，均实际打开）
| URL | 结果 | 用途 |
| --- | --- | --- |
| https://owiki.org/wiki/Form_(architecture) | 200 | Form 候选，双源可达但域外/近义，弃 |
| https://www.designingbuildings.co.uk/wiki/Form | 200 | Form 第二源（建筑 form 定义） |
| https://owiki.org/wiki/Phenomenology_(architecture) | 200 | 建筑现象学，近义 place-spirit，弃 |
| https://www.designingbuildings.co.uk/wiki/Phenomenology | 200 | 现象学第二源，弃 |
| https://owiki.org/wiki/Formalism_(art) | 200 | 形式主义，域外/方法论，弃 |
| https://artincontext.org/formalism/ | 200 | 形式主义第二源，弃 |
| https://owiki.org/wiki/Iconography | 200 | 图像学，单源，弃 |
| https://owiki.org/wiki/Munsell_color_system | 200 | 孟塞尔色立体，单源/近义，弃 |
| https://owiki.org/wiki/Tectonics_(architecture) | 200 | 建筑建构，缺第二源，弃 |
| https://owiki.org/wiki/Modulor | 200 | 模度，近义 proportion，弃 |
| https://www.designingbuildings.co.uk/wiki/Hatching | 200 | 「标准剖面线样式」=技术制图 hatch，非艺术排线，不作候选第二源 |

### 失败/不可用（审计用，第二源探索）
| URL | 结果 | 备注 |
| --- | --- | --- |
| https://en.wikipedia.org/wiki/Painting | URLError timed out | 维基 canonical 超时，改用 owiki 镜像（同源计一源） |
| https://artincontext.org/hatching/ | HTTP 404 | 无单独 hatching 页，改用其 cross-hatching 页 |
| https://artincontext.org/iconography/ | HTTP 404 | 图像学无对应专页（单源） |
| https://www.designingbuildings.co.uk/wiki/Munsell_colour_system | HTTP 404 | slug 不存在 |
| https://www.designingbuildings.co.uk/wiki/Cross-hatching | HTTP 404 | slug 不存在 |
| https://www.britannica.com/art/formalism-art | HTTP 403 | Britannica 403 |

### 打开 URL 计数
- 本轮实际发起 HTTP 请求 **39 次**；HTTP 200 成功 **33 次**；失败 **6 次**（en.wikipedia 超时 1、artincontext 404 2、DB 404 2、Britannica 403 1）；去重后 **31 个不同 URL**。
- 作为来源实际读取正文的核心证据页：hatching 2 个（owiki Hatching ＋ artincontext Cross-hatching）、stippling 2 个（owiki Stippling ＋ artincontext Stippling）；对照大纲 5 个；B6 4 个；附加探测/失败 18 个（含重复抓取）。

---

## 机器可读汇总

```
CANDIDATES=[
 {"id":"hatching","title":"排线法（交叉排线，Hatching / Cross-hatching）","theme":"理论","subdomain":"光影与明暗","tier":"重要","period":"文艺复兴至19世纪","region":"欧洲","urls":["https://owiki.org/wiki/Hatching","https://artincontext.org/cross-hatching/"],"sources":["w-owiki-hatching","aic-cross-hatching"],"note":"round02 曾以单源驳回，本轮补齐第二独立源 artincontext"},
 {"id":"stippling","title":"点描法（Stippling）","theme":"理论","subdomain":"光影与明暗","tier":"补充","period":"跨时期","region":"全球","urls":["https://owiki.org/wiki/Stippling","https://artincontext.org/stippling/"],"sources":["w-owiki-stippling","aic-stippling"],"note":"round02 曾以单源驳回，本轮补齐第二独立源 artincontext"}
]
REJECTED=["form-architecture(双源可达但不在列举子域/近义geometry-symmetry,proportion,space-definition)",
          "phenomenology-architecture(近义place-spirit/place-attachment)",
          "philosophy-of-architecture(元理论/缺第二源)",
          "architectural-design-values(近义vitruvian-triad)",
          "formalism-art(艺术批评方法论/域外,缺列举子域)",
          "iconography(单源)",
          "munsell-color-system(单源/近义color-theory)",
          "modulor/tectonics(近义/缺第二源)",
          "figure-gesture-contour-drawing(题材门类/非列举子域)",
          "painting-media-and-movements(媒介/流派史,超绘画理论且风格限建筑)",
          "color-wheel-mixing-space-opponent(色彩科学机制/近义)"]
B6_NEW=[]
B1_RESULT="有：2 条新双源缺口候选（hatching、stippling），均为 round02 单源驳回项补第二源后成立"
B6_RESULT="未发现新的可核验动态"
URLS_REQUESTED=39
URLS_OK_200=33
URLS_FAILED=6
URLS_DISTINCT=31
```

是否发现新缺口：是
