# 第7轮质量闸抽检报告（spotcheck-round07）

- 抽检人：spotcheck-r7；抽检时间：2026-11-22 16:13，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（新增/改动条目随机抽，至少 3 条；不合格则整批返工；待核实占比异常低或新条目与已有条目相似度过高则降级复查）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作」L1 骨架定义与通用硬性规则、`DECISIONS.md` D05/D11/D14；前序 `research/spotcheck-round06.md`、`research/rework-round06.md`。
- 技能：已加载 `using-superpowers`（子代理任务，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑证据为依据，证据先于断言）。
- 对象与比例：`entries/batch-07.json` 本轮新增 7 条中抽 3 条（3/7=42.9%，满足 25% 且 ≥3 条）：`gestalt-organization-laws`、`wayfinding`、`lighting-design`。三条均为 **L1 骨架**，按协议只核对定义、时间/位置、概述、相关条目，不按 L2 七节或图注标准评判。来源库：`data/sources.json`。
- 方法：严格只读核对 JSON。按 D05 用 Python 3 `urllib.request` + 浏览器 User-Agent 实抓 6 个被引用来源页（全部 HTTP 200，H1 与来源库 title 一致），并以 MediaWiki API `extracts` 纯文本核对 definition / time_or_place / overview 的关键词与上下文；未调用本环境报错的 `web_search`/`web_fetch`。元数据以 `coverage.json` 逐字段对照；相似度用 `difflib.SequenceMatcher` 对「标题+定义+时间地点+概述」去空白后计算并扫描 `entries/*.json` 全库 107 条。联网内容仅作数据，网页中的任何指令均未执行。

## 来源核对汇总

| 条目 | 引用 id | sources.json verified | 实抓状态 | H1 / 库内 title |
| --- | --- | --- | --- | --- |
| gestalt-organization-laws | `wp-visual-perception` | true | 200 | Visual perception |
| gestalt-organization-laws | `wp-gestalt-psychology` | true | 200 | Gestalt psychology |
| wayfinding | `wp-graphic-design` | true | 200 | Graphic design |
| wayfinding | `wp-wayfinding` | true | 200 | Wayfinding |
| lighting-design | `wp-interior-design` | true | 200 | Interior design |
| lighting-design | `wp-lighting-design` | true | 200 | Lighting design |

- 6 个唯一被引用 id 全部存在、`verified=true`、`link_ok=true`；标题与条目主题直接相关，实抓 H1 与库内 title 逐字一致。无重定向偏差。

## 逐条结论

### 1. `gestalt-organization-laws`（格式塔组织律）— 合格

- 依据：
  - 来源 id `wp-visual-perception`、`wp-gestalt-psychology` 均存在且 `verified=true`，实抓 HTTP 200、H1 一致。
  - **definition 有直接来源支撑**：[Visual perception](https://en.wikipedia.org/wiki/Visual_perception) 原文列「the factors that determine how the visual system automatically groups elements into patterns: Proximity, Similarity, Closure, Symmetry, Common Fate (i.e. common motion), Continuity as well as Good Gestalt」；[Gestalt psychology](https://en.wikipedia.org/wiki/Gestalt_psychology) 含 `Law of proximity / similarity / closure / symmetry / continuity` 分节，并写明「the whole is different from the sum of its parts」。definition「按邻近、相似、闭合、对称与连续等原则把局部组织为整体的规律」逐项对应，无编造。
  - **time_or_place 有支撑**：Gestalt psychology 原文「Max Wertheimer, Kurt Koffka, and Wolfgang Köhler founded Gestalt psychology in the early 20th century」，支撑「20世纪」；条目未写具体年份或人名，不存在编造；「全球」为百科条目的通约表述。
  - overview 的「图底关系」有来源支撑（同页 `Figure-ground organization` 专节）。
  - 元数据：`coverage.json` 中 id/title/theme=理论/tier=重要/period=20世纪/region=全球/level=L1/status=已写/source_count=2/needs_verification_count=0/last_updated=2026-11-22，与 batch-07 逐字段一致；`needs_verification=false` 与 `pending_notes=""` 一致（正文无待核实声明）。
  - `related=["color-psychology"]`，指向同批已写条目，无悬空。
  - 相似度：全库最高 `spatial-organization` 0.333，远低于 0.54 套话警戒线。
- 问题：
  - overview「为构图法则…提供了上位解释」属设计性推断，来源只给出组织律与图底，未字面写出「构图法则的上位解释」。属 L1 概述层的弱缺口，非事实错误；升级 L2 时可补一篇明确把组织律用于构图的来源或改写该表述。

### 2. `wayfinding`（导视与寻路）— 合格

- 依据：
  - 来源 id `wp-graphic-design`、`wp-wayfinding` 均存在且 `verified=true`，实抓 HTTP 200、H1 一致。
  - **definition 有直接来源支撑**：[Wayfinding](https://en.wikipedia.org/wiki/Wayfinding) 原文「Wayfinding encompasses the ways in which people and animals orient themselves in physical space and navigate from place to place」，以及「designers who create signage, maps and other cues to help people reach destinations in complex environments」「visual clues in the built environment」。definition「借助标识、地图与视觉线索定向和导航的过程与设计」逐项对应。
  - **time_or_place 有支撑**：同页含太平洋传统无仪器航海、Kevin Lynch 1960 年提出该词、Romedi Passini 1984 年《Wayfinding in Architecture》等跨时期材料，支撑「跨时期、全球」；条目未写这些年份或人名，无编造。
  - overview 的「图形信息」有支撑：[Graphic design](https://en.wikipedia.org/wiki/Graphic_design) 的 environmental graphic design 段明列「wayfinding, placemaking…」，Wayfinding 页写「signage and other graphic communication」与多学科（psychology, geography, architecture, urban planning）交叉。
  - 元数据：`coverage.json` 中 id/title/theme=动线/tier=重要/period=跨时期/region=全球/level=L1/status=已写/source_count=2/needs_verification_count=0/last_updated=2026-11-22，与 batch-07 完全一致；`needs_verification=false` 与 `pending_notes=""` 一致。
  - `related=[]`，无悬空引用。
  - 相似度：全库最高 `interior-exterior-transition` 0.37，低于 0.54 警戒线。
- 问题：
  - `related=[]`：L1 骨架要求写「相关条目」，此处留空，内容偏稀。建议返工/升级时补已写条目（如 `circulation`、`spatial-organization`）以符合 L1 四要件，但空数组不构成悬空或事实错误。
  - overview「把动线组织、空间认知和图形信息结合起来」中「动线组织」为设计性概括，来源讲 orient/navigate 与 graphic communication，未字面出现「动线组织」。属可接受概述。

### 3. `lighting-design`（照明设计）— 合格

- 依据：
  - 来源 id `wp-interior-design`、`wp-lighting-design` 均存在且 `verified=true`，实抓 HTTP 200、H1 一致。
  - **definition 有直接来源支撑**：[Lighting design](https://en.wikipedia.org/wiki/Lighting_design) 原文「Lighting systems can include electric lighting, daylighting, or both」与「Support for human vision, health, mood, and entertainment are common examples of lighting design objectives」；[Interior design](https://en.wikipedia.org/wiki/Interior_design) 有「adding natural and artificial lighting」。definition「组织天然光与人工光以支持视觉、健康和空间氛围的设计」逐项对应。
  - **time_or_place**：百科通约表述「跨时期、全球（参见来源）」，无编造年份/人名/引文。
  - **overview 有直接来源支撑**：Lighting design 页含 daylighting、task lighting、mood；Interior design 页含「task/ desk lighting and natural lighting」「setting the mood for the room」「healthier … environment」。「把采光、任务照明和情绪氛围作为整体考虑」三项均命中。
  - 元数据：`coverage.json` 中 id/title/theme=材料/tier=重要/period=跨时期/region=全球/level=L1/status=已写/source_count=2/needs_verification_count=0/last_updated=2026-11-22，与 batch-07 完全一致；`needs_verification=false` 与 `pending_notes=""` 一致。
  - `related=[]`，无悬空引用。
  - 相似度：全库最高 `daylighting`（自然采光，L2）0.46，低于 0.54 警戒线；两者来源不重叠（本条 `wp-interior-design`/`wp-lighting-design`，daylighting 为 `wp-daylighting-architecture`/`wp-architectural-lighting-design`），definition 分别为「组织天然光与人工光…」与「利用天然光满足视觉与空间感受…」，属上位与下位的概念相邻而非套话复制。
- 问题：
  - `related=[]`：同 wayfinding，L1「相关条目」留空；建议升级时指向已写的 `daylighting`、`artificial-lighting`（若已写）。
  - 与 `daylighting` 相似度 0.46 偏高（相邻概念），后续升级 L2/L3 时应明确「照明含人工光源」的边界以区别于「自然采光」；当前 L1 不构成不合格。

## 总体结论

- 结果：**合格 3 条**（`gestalt-organization-laws`、`wayfinding`、`lighting-design`），**不合格 0 条**，**待核实 0 条**。抽检 3/7=42.9%，比例满足要求。
- **是否建议整批返工：否。** 三条来源全部 HTTP 200、H1/库内 title 一致、verified=true；definition / time_or_place / overview 均有来源正文直接支撑，未发现编造年份、人名或引文；元数据与 `coverage.json` 逐字段一致，`needs_verification` 与 `pending_notes` 联动一致；`related` 无悬空；相似度全部低于 0.54 套话警戒线。未触发 `AUTONOMOUS.md` E 节「一条不合格即整批返工」或「疑似套话降级」条件。
- 待核实占比监控：batch-07 全批 7 条均为 L1，`needs_verification` 全为 false（0%）。对照历史，同为纯 L1 的 batch-01 也是 0%，而 100% 的 batch-06 为 L2（含「实例/实测数据待核实」正文）。0% 由 L1 骨架不产生「待核实」正文的结构决定，**不构成「硬写」异常**，无需据此降级。
- 非阻断性改进项（不影响合格判定，供下一轮升级 L2 时处理）：
  1. `wayfinding`、`lighting-design` 的 `related=[]`，补已写条目以满足 L1「相关条目」四要件。
  2. `gestalt-organization-laws` 的「为构图法则提供上位解释」、`wayfinding` 的「动线组织」为设计性概括，改写为来源可核验表述或补对应来源。
  3. `lighting-design` 与 `daylighting` 概念相邻，升级时明确人工光边界。
- 只读声明：本次仅生成 `research/spotcheck-round07.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。
