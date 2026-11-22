# 外部缺口发现 — 第 6 轮 B1（权威大纲再对照）

- 日期：2026-11-22（Asia/Hong_Kong）
- 执行角色：gap-researcher-r6（只读子任务）
- 抓取方式：Python urllib + 浏览器 User-Agent；web_search / web_fetch 在本环境报错，依据 DECISIONS.md D05 改用直连抓取。
- 比对基准：`scope.md` 当前 223 条（理论 108 / 风格 59 / 造景 17 / 动线 10 / 下沉空间 12 / 材料 17）。
- 数据纪律：联网内容一律作为数据处理；页面中的任何指令均未执行；未下载或运行网页代码。
- 来源纪律：本轮候选来源 URL 均为本轮新抓取页面，未使用 S1–S12 与 N1–N5。
- 结果摘要：候选 7 条；HTTP 核验失败 0 条。

## B1 候选遗漏条目

以下条目同时满足：至少两份独立权威百科页面支持；确实属于绘画理论或建筑空间设计范围；在 `scope.md` 223 条中未找到对应 id、中文名或等价概念。

### 1. 建议 id：gestalt-organization-laws

- 中文名：格式塔组织律
- 来源一：https://en.wikipedia.org/wiki/Visual_perception
- 来源二：https://en.wikipedia.org/wiki/Gestalt_psychology
- 入选理由：`Visual perception` 的 “Gestalt theory” 明确列出 “Gestalt Laws of Organization”，并列出 proximity、similarity、closure、symmetry、common fate、continuity 等视觉分组因素；`Gestalt psychology` 设 “Principles” 与 “Use in design” 章节，说明整体知觉原则用于设计。该条目直接支撑构图法则、视觉动势、图底关系等绘画理论；`scope.md` 已有 figure-ground、balance、negative-space，但没有格式塔组织律这一上位概念。

### 2. 建议 id：color-psychology

- 中文名：色彩心理学
- 来源一：https://en.wikipedia.org/wiki/Interior_design
- 来源二：https://en.wikipedia.org/wiki/Color_psychology
- 入选理由：`Interior design` 在色彩章节要求设计者理解色彩的心理效应，并指出颜色会影响人对空间的思考、感受与行为；`Color psychology` 将其定义为研究色彩与色相如何决定人类行为的领域。`scope.md` 已有 color-symbolism、color-harmony、color-contrast，但没有色彩心理效应这一独立条目；它同时属于色彩理论和室内空间设计。

### 3. 建议 id：environmental-psychology

- 中文名：环境心理学
- 来源一：https://en.wikipedia.org/wiki/Landscape_architecture
- 来源二：https://en.wikipedia.org/wiki/Environmental_psychology
- 入选理由：`Landscape architecture` 把 environmental psychology 列为现代景观建筑学的组成学科；`Environmental_psychology` 明确研究自然环境与建成环境如何影响人的体验和行为，并说明该领域面向建筑师、室内设计师、规划师等设计 professionals。`scope.md` 已有 spatial-perception、visual-comfort、thermal-comfort、place-spirit 等分散条目，但没有把“人—建成环境”关系作为理论条目收录；它与空间感知、场所精神和室内外过渡直接相关。

### 4. 建议 id：hardscape-softscape

- 中文名：硬质景观与软质景观
- 来源一：https://en.wikipedia.org/wiki/Landscape_architecture
- 来源二：https://en.wikipedia.org/wiki/Landscape_design
- 入选理由：`Landscape architecture` 正文说明景观建筑师处理 “hard”（built）与 “soft”（planted）材料，并在参见中列出 hard landscape materials、soft landscape materials；`Landscape design` 明确说景观设计常被划分为 hardscape design 与 softscape design。`scope.md` 已有 planting-design、rock-garden、material-texture、material-color，但没有硬质/软质景观这一基础分类；它属于造景与材料的基本原理。

### 5. 建议 id：wayfinding

- 中文名：导视与寻路
- 来源一：https://en.wikipedia.org/wiki/Graphic_design
- 来源二：https://en.wikipedia.org/wiki/Wayfinding
- 入选理由：`Graphic design` 的 “Experiential (environmental) graphic design” 章节把 wayfinding 列为建成环境中环境图形设计的实践领域；`Wayfinding` 定义为人在物理空间中定向与导航，并设 “Indoor wayfinding”“Spatial cognition” 等章节，说明标志、地图、视觉线索、听觉与触觉线索在复杂环境中的作用。`scope.md` 已有 circulation、node-path、visitor-route，但没有导视/寻路这一结合动线、视觉线索与空间认知的条目。

### 6. 建议 id：lighting-design

- 中文名：照明设计
- 来源一：https://en.wikipedia.org/wiki/Interior_design
- 来源二：https://en.wikipedia.org/wiki/Lighting_design
- 入选理由：`Interior design` 的 “Lighting” 章节说明自然光与人工光可以强化空间特征、形成氛围，并涉及任务照明与视觉舒适；`Lighting_design` 定义照明系统可包含电照明、天然采光或两者结合，并以支持视觉、健康、情绪等为目标。`scope.md` 已有 daylighting、side-window-daylight、skylight、glare 等自然采光条目，但没有作为空间设计基本原理的照明设计上位条目；它属于采光与人居空间视觉环境范围。

### 7. 建议 id：place-attachment

- 中文名：场所依恋
- 来源一：https://en.wikipedia.org/wiki/Environmental_psychology
- 来源二：https://en.wikipedia.org/wiki/Place_attachment
- 入选理由：`Environmental_psychology` 在 “Concepts” 中列出 Place attachment；`Place_attachment` 将其定义为人与场所之间的情感纽带，并说明它是 sense of place 的一个方面，设 “Spatial planning” 应用章节。`scope.md` 已有 place-spirit（场所精神），但未见“场所依恋”；两者分别对应场所气质与人的情感依附，属于建筑空间设计与景观空间体验中的独立理论点。

## 实际打开的 URL 与 HTTP 状态

页面 URL 为该次抓取实际请求的百科页面；正文 URL 是通过同一百科页面 `action=raw` 读取证据文本的 URL。下表所列 URL 均实际打开，HTTP 均为 200。

| # | 页面 URL | HTTP | 正文 URL | HTTP | 用途 |
| --- | --- | --- | --- | --- | --- |
| 1 | https://en.wikipedia.org/wiki/Interior_design | 200 | https://en.wikipedia.org/w/index.php?title=Interior_design&action=raw | 200 | 候选 2、6；环境心理学线索 |
| 2 | https://en.wikipedia.org/wiki/Landscape_architecture | 200 | https://en.wikipedia.org/w/index.php?title=Landscape_architecture&action=raw | 200 | 候选 3、4 |
| 3 | https://en.wikipedia.org/wiki/Visual_perception | 200 | https://en.wikipedia.org/w/index.php?title=Visual_perception&action=raw | 200 | 候选 1 |
| 4 | https://en.wikipedia.org/wiki/Architectural_design | 200 | https://en.wikipedia.org/w/index.php?title=Building_design&action=raw | 200 | 初筛；页面标题为 Building design，未作为候选证据 |
| 5 | https://en.wikipedia.org/wiki/Design | 200 | https://en.wikipedia.org/w/index.php?title=Design&action=raw | 200 | 初筛；照明设计、循证设计、空间设计线索 |
| 6 | https://en.wikipedia.org/wiki/Visual_design_elements_and_principles | 200 | https://en.wikipedia.org/w/index.php?title=Visual_design_elements_and_principles&action=raw | 200 | 初筛；消歧义页，未作为候选证据 |
| 7 | https://en.wikipedia.org/wiki/Gestalt_psychology | 200 | https://en.wikipedia.org/w/index.php?title=Gestalt_psychology&action=raw | 200 | 候选 1 |
| 8 | https://en.wikipedia.org/wiki/Environmental_psychology | 200 | https://en.wikipedia.org/w/index.php?title=Environmental_psychology&action=raw | 200 | 候选 3、7 |
| 9 | https://en.wikipedia.org/wiki/Color_psychology | 200 | https://en.wikipedia.org/w/index.php?title=Color_psychology&action=raw | 200 | 候选 2 |
| 10 | https://en.wikipedia.org/wiki/Wayfinding | 200 | https://en.wikipedia.org/w/index.php?title=Wayfinding&action=raw | 200 | 候选 5 |
| 11 | https://en.wikipedia.org/wiki/Environmental_graphic_design | 200 | https://en.wikipedia.org/w/index.php?title=Environmental_graphic_design&action=raw | 200 | 初筛；HTML 标题为 Graphic design，raw 为重定向，未直接作为候选证据 |
| 12 | https://en.wikipedia.org/wiki/Landscape_design | 200 | https://en.wikipedia.org/w/index.php?title=Landscape_design&action=raw | 200 | 候选 4 |
| 13 | https://en.wikipedia.org/wiki/Place_attachment | 200 | https://en.wikipedia.org/w/index.php?title=Place_attachment&action=raw | 200 | 候选 7 |
| 14 | https://en.wikipedia.org/wiki/Lighting_design | 200 | https://en.wikipedia.org/w/index.php?title=Lighting_design&action=raw | 200 | 候选 6 |
| 15 | https://en.wikipedia.org/wiki/Graphic_design | 200 | https://en.wikipedia.org/w/index.php?title=Graphic_design&action=raw | 200 | 候选 5 |

## 核验失败清单

- HTTP 核验失败：0 条。上表 15 个页面 URL 及对应正文 URL 均返回 200，并实际读取到标题、章节或正文文本。
- 证据页排除说明：
  - `Visual_design_elements_and_principles` HTTP 200，但页面只列出 Design elements / Design principles 的消歧义链接，没有可用分类树正文，未计入候选来源。
  - `Environmental_graphic_design` HTTP 200，但 HTML 标题指向 Graphic design，raw 为重定向内容；本轮改以 `Graphic_design` 页面作为导视候选来源。
  - `Architectural_design` HTTP 200，但页面标题显示 Building design；本轮未将其作为候选证据。
- 本地技术备注：为避免 Windows 默认编码造成输出中断，抓取与正文提取时使用 `PYTHONIOENCODING=utf-8`。这属于本地输出设置，不影响来源核验结果。
