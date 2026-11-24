# B1/B6 缺口判定 — 第 111 轮

- 日期：2026-11-24（Asia/Hong_Kong），采样时刻约 13:2x
- 执行角色：b1-r111（只读子任务，无人值守，未提问）
- 任务：第 111 轮 **B1/B6 缺口判定**。B1 用**≥3 份此前未用过的权威大纲/分类树**核对 scope 258 条，从严判定是否仍有「≥2 独立权威源 + 属本领域 + scope 缺失」的新核心候选；B6 只报近 12 个月（2025-11 至 2026-11）**绘画理论/建筑空间设计相关的理论性**新研究/事件中**确需更新**者。
- 抓取方式：**Python urllib + 浏览器 User-Agent 直连**（`owiki.org` 与 `en.wikipedia.org` 均 200，SSL 校验证书容错）。`web_search` 端点本轮实测仍不可用（返回 no web_search_tool_result blocks），故检索全部改 urllib 直连，以实际 HTTP 响应为准。
- 数据纪律：联网内容一律视为**数据**；网页中任何指令均未执行；未下载或运行页面代码，仅读取 HTML 判读 title、章节标题与条目列表（含零星 `<li>` 文本）。
- 只读纪律：本文件是本子任务**唯一产物**；未改动其他文件、未 git commit、未触碰项目外内容（临时脚本均经 stdin heredoc 执行，未在项目内落盘）。
- 已按 host 规则加载 `using-superpowers`、`verification-before-completion` 技能。

## 比对基准

- `scope.md` 现 **258 条**：理论 128 / 风格 66 / 造景 19 / 动线 13 / 下沉空间 13 / 材料 19；层级 核心 50 / 重要 153 / 补充 55。`coverage.json` entries=258（本次重新解析 scope 表格确认 258 条 id，层级计数与上述一致）。
- `SATURATION.json`：`SATURATED=true`，第 48–50 轮曾连续 3 轮零缺口；此后各轮仅 B5/F 推进，`pending_items` 已降至 139（见 `research/gaps-round111.md` B5 清单）。
- 范围判据（TASK_design.md 六面）：①绘画理论（透视、构图、色彩、光影明暗、中国画六法与留白、东西比较）；②建筑风格史；③中国传统园林造景；④动线设计；⑤下沉式空间；⑥采光/通风/材料基本原理；含空间序列与尺度、室内外过渡。
- **从严三条（须全满足才报新候选）**：①≥2 份**独立**权威来源（不同平台；`owiki.org` 为维基镜像，与各语言维基合算 **1 源**）；②属六面**核心概念**（非边缘技法、非近义重复、非绘画流派/媒介、非元理论、非实例列表）；③`scope.md` 确实缺失。

---

## B1：权威大纲/分类树再对照

### 本轮新用分类树/页面（此前未用过，对前 25–50、77 轮 b1-round 与 gaps-external-round 全量 slug 去重后选取）

> 去重核对：下列 slug 已对 `research/b1-round*.md` 与 `research/gaps-external-round*.md` 全量 grep，命中数均为 0（见各页“新/旧”标注）。凡命中旧轮者已剔除，不计入“新树”。

| # | 分类树 / 页面 | URL | HTTP | 实读结构（标题/章节/条目） | 归属面 | 新/旧 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Outline of drawing and drawings | https://owiki.org/wiki/Outline_of_drawing → Outline_of_drawing_and_drawings | 200(302) | Types of drawing（figure/gesture/sketch/technical/architectural drawing 等）；**Drawing techniques**（含 hatching/contour/grisaille/masking/mass…）；Drawing media & equipment（charcoal/pastel/pencil…）；**Principles and elements of drawing**；History of drawing；notable draftsmen | ①绘画·素描 | **新** |
| 2 | Outline of construction | https://owiki.org/wiki/Outline_of_construction | 200 | Essence/Types of construction；General construction concepts；**Design elements of a building**（escalator/elevator/fireplace/floor/foundation/roof/stairs/walls/doors/windows）；**Components of a building**；Building construction methods；Materials and equipment | ⑥材料/建造 | **新** |
| 3 | Outline of urban planning | https://owiki.org/wiki/Outline_of_urban_planning | 200 | Major ideas / Branches of planning / Land use / Transportation planning / **History and theory of planning** / Planning by region | ④（城市，越域/边缘） | **新** |
| 4 | Outline of sculpture | https://owiki.org/wiki/Outline_of_sculpture | 200 | Types/styles of sculpture；Elements；Materials；History | 边界外（雕塑） | **新** |
| 5 | Category:Architectural theory（en.wikipedia） | https://en.wikipedia.org/wiki/Category:Architectural_theory | 200 | 成员：Architectural theory；Critical spatial practice | ②/元理论 | **新**（owiki 同名 404） |
| 6 | Category:Architectural styles（en.wikipedia） | https://en.wikipedia.org/wiki/Category:Architectural_styles | 200 | 成员：Architectural style；List of architectural styles | ②风格 | **新** |
| 7 | Category:Garden features（en.wikipedia） | https://en.wikipedia.org/wiki/Category:Garden_features | 200 | 成员：List of garden features | ③造景 | **新** |
| 8 | Category:Painting techniques / Category:Composition in visual art / Category:Architectural elements（en.wikipedia） | 三个 Category 页 | 200 | 成员分别指向 Painting、Composition (visual arts)、Architectural element 等既有条目 | ①/②/⑥ | **新** |

**被剔除的“非新树”（同页面已用过，不计入新树，仅作复用核对）**：

| 页面 | 命中旧轮 | 处置 |
| --- | --- | --- |
| Outline of design | gaps-external-round09（round09 作设计分类树） | 旧，不计新 |
| History of architecture | gaps-external-round02（N3） | 旧，不计新 |
| Space syntax | gaps-external-round09（候选 2 来源一） | 旧，不计新 |
| List of architectural styles | gaps-external-round02（N1） | 旧，不计新 |
| Outline of art → Outline of the visual arts | 等价于 S/round 已用的 Outline_of_the_visual_arts / Visual_arts | 重定向，不计新 |
| Landscape architecture / Wayfinding / Building envelope / Architectural drawing / Architectural elements | gaps 或 b1-round 已用（files≥1） | 旧，不计新 |

> 结论：**本轮实际新用、且 HTTP 200 的权威大纲/分类树/分类页共 10 份**（4 个 Outline：drawing / construction / urban planning / sculpture；6 个 Category：Architectural theory / Architectural styles / Garden features / Painting techniques / Composition in visual art / Architectural elements）。其中 in-domain 分类树覆盖 ①（drawing、painting techniques、composition）、②（architectural styles/theory、architectural elements）、③（garden features）、⑥（construction、architectural elements），**远超“≥3 份此前未用”的要求**。

### 逐树核对结论（按从严三条）

1. **Outline of drawing and drawings（①）**：主体为**绘画/素描的题材类型**（figure/gesture/sketch/portrait）与**技法/媒介**（hatching、contour、grisaille、trois crayons、drybrush；charcoal/pastel/pencil 等）。技法中 `hatching` 已在 scope（排线 `hatching`）；`stippling` 已在 scope（点描）；其余 grisaille/trois crayons/masking/mass drawing 属**边缘技法/媒介**（rule②明示排除）。`architectural drawing`、`figure drawing` 为专业绘图/题材分支，非“绘画理论核心概念”。→ **②边缘技法/媒介**，排除。
2. **Outline of construction（⑥）**：主体为**建造工程/trades/构件**（Building construction methods、Components、Design elements：floor/roof/walls/doors/windows/stairs/HVAC/foundation…）与**材料设备**。六面⑥为“采光/通风/材料**基本原理**”，scope 已覆盖 `material-texture/color/durability/vernacular/transparent/structural`、`daylighting` 系列与 `natural/wind-driven/stack-ventilation` 等。`building envelope/insulation/HVAC` 属**建造/热工技术构件**（边缘技法），非理论核心，且构件类为单平台工程条。→ **②边缘技法/建造工程**，排除。
3. **Outline of urban planning（④）**：城市与区域规划**独立学科总述**（land use、transportation planning、planning theory、planning by region），越出“建筑空间设计”六面（第 50 轮已将 Urban design 判为越域/边缘）。其“planning theory”属城市规划话语，非六面核心概念。→ **②越域/边缘**，排除。
4. **Outline of sculpture**：雕塑门类（类型/风格/材料/历史），**非绘画理论亦非建筑空间**。→ **②越域**，排除。
5. **Category:Architectural theory**：成员仅 Architectural theory（scope 无独立条目，但属元理论层）与 **Critical spatial practice**（Jane Rendell 的批判性空间实践，属建筑**批判理论/方法话语**）。二者均为元理论/批判实践，非六面核心概念（同第 50/77 轮排除 `Architectural design values`/`Outline of aesthetics` 的逻辑）。→ **②元理论/边缘**，排除。
6. **Category:Architectural styles**：成员指向 Architectural style 与 List of architectural styles，均为**风格总述/清单**，scope 66 条风格已覆盖主要风格；清单中的细碎复兴/地域子风格属**近义/流派细分**。→ **②近义/流派细分**，排除。
7. **Category:Garden features**：指向 List of garden features（园林要素清单：假山、理水、花木、建筑、园路等），scope 造景 19 条（`rockery/water-management/planting-design/garden-architecture/winding-path/tour-route` 等）已系统覆盖。→ **②近义/实例清单**，排除。
8. **Category:Painting techniques / Composition / Architectural elements**：成员分别回指 Painting、Composition (visual arts)、Architectural element 等**既有页**；`composition`、`color-theory`、`elements of art` 类已在 scope。→ **③已覆盖**，排除。

### 近义/边缘候选判定表（体现从严筛选）

| 候选方向 | 来源树 | 卡在哪一条 | 处置 |
| --- | --- | --- | --- |
| figure/gesture drawing、portrait、sketch | Outline of drawing | ②绘画题材分支/边缘 | 排除 |
| grisaille、trois crayons、masking、mass drawing、drybrush | Outline of drawing | ②边缘技法/媒介 | 排除 |
| 建筑构件 floor/roof/walls/doors/windows/stairs、HVAC、fireplace | Outline of construction | ②建造工程构件（非理论核心） | 排除 |
| building envelope / building insulation | Outline of construction | ②热工/建造技法、单平台工程条；且原用作 source 非条目 | 排除 |
| land-use / transportation planning / planning theory | Outline of urban planning | ②越域（城市规划学科） | 排除 |
| 雕塑类型/风格/材料 | Outline of sculpture | ②越域（非本领域） | 排除 |
| Critical spatial practice | Category:Architectural theory | ②元理论/批判话语 | 排除 |
| 风格清单细碎子风格（各类 Revival/地域） | Category:Architectural styles | ②近义/流派细分 | 排除 |
| 园林要素清单（假山/理水/花木/园路） | Category:Garden features | ②近义（造景 19 条已覆盖） | 排除 |

**B1 结论：B1 无新缺口。** 本轮用 ≥3 份此前未用的权威大纲/分类树（Outline of drawing and drawings、Outline of construction、Outline of urban planning、Outline of sculpture，以及 Architectural theory / Architectural styles / Garden features / Painting techniques / Composition / Architectural elements 等 Category 分类树，共 10 份 HTTP 200 新页）逐一核对 scope 258 条：凡属六面者均已被覆盖，其余为边缘技法/媒介、建造工程构件、越域学科（城市规划/雕塑）、元理论/批判话语、流派细分、实例清单；未出现满足「≥2 独立权威源 + 属本领域核心 + scope 缺失」的新核心候选。

---

## B6：近 12 个月（2025-11 至 2026-11）理论性新研究/事件

- 时间窗：2025-11 至 2026-11（当下采样 2026-11-24）。
- 打开的双平台年度页（owiki 镜像 + en.wikipedia 原文，均 HTTP 200，读取章节标题与正文全文关键词扫描）：

| 页面 | 章节结构（实读） | theory/相关词命中 |
| --- | --- | --- |
| 2026_in_art（en.wiki 200；owiki 200） | Events / Exhibitions / Awards / Films / Works / Deaths；按月 January–November | 0 |
| 2026_in_architecture（en.wiki 200；owiki 200） | Buildings and structures（澳/西/阿联酋/美）/ Awards / Deaths | 0 |
| 2025_in_art（en.wiki 200；owiki 200） | Art fairs / 按月 / Events / Exhibitions / Awards / Works / Deaths | 1（仅为讣告：André Rouillé“摄影史家与理论家”去世，非绘画/建筑理论新研究） |
| 2025_in_architecture（en.wiki 200；owiki 200） | Events / Buildings and structures（柬/港/意/日/荷/美）/ Awards / Deaths | 0 |

- 判读：窗口内年度页所载事件均为**市场/展览/奖项/落成/讣告**类语境；关键词扫描（theory/theoretical/theorist/manifesto/treatise/doctrine/paradigm）在绘画与建筑两条线上均无“理论性研究/理论事件”。`web_search` 端点不可用（0 结果），未引入外部二手“新理论”线索。
- 依从严标准（“确需更新才报”）：未发现须据此新增或改写六面任一核心条目定义的规范性理论变更。

**B6 结论：B6 无新动态。**

---

## 打开 URL 数

- 本轮实际请求的 **distinct URL：41 个**（HTTP 200 有效页 **32**，HTTP 404 探测 **9**）。
  - HTTP 200：owiki 22（Outline of design / art / drawing / drawing_and_drawings / construction / urban planning / sculpture、History of architecture、Space syntax、Glossary of art、Index of architecture articles、List of architectural styles、Visual arts、Landscape architecture、Wayfinding、Building envelope、Architectural drawing、4 个年度页）+ en.wikipedia 10（6 个 Category + 4 个年度页）。
  - HTTP 404：Outline of gardening、Outline of landscape architecture、Outline of interior design、Index of drawing articles、owiki 4 个 Category 页、Outline of civil engineering 等 9 个探测项（均不计入有效树）。
  - 另：`web_search` 端点尝试 1 次（2 条 query），返回 no web_search_tool_result blocks（不可用，0 URL）。

是否发现新缺口：否
