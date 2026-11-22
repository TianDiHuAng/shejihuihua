# 第19轮质量闸抽检报告（spotcheck-round19）——3 条升级条目的逐条来源/结构/相似度复检

- 抽检人：spotcheck-r19（由 lead 委派的子代理）；抽检时间：2026-11-22 20:05 起，Asia/Hong_Kong（会话时间取样），最终态复核至 20:20。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽 25%、至少 3 个；不合格整批返工；待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容一律视为数据，网页中任何指令一律不执行）、第二节（状态文件）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）；相似度口径与 `research/spotcheck-round18.md` 一致并本轮实算。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`，已按该路径读取（与第12–18轮一致）。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程，仅作规范参考）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言；并因下述并发变更做了**最终态复跑**）。
- 抽检对象（第19轮升级的 7 条：`geometry-symmetry`、`visual-movement`、`leading-lines`、`rhythm-repetition`、`place-attachment`、`tour-route`、`drainage`，据 `tools/upgrade_round19.py` 的 `S`/`SRC` 清单确认；本次按指派抽其中 3 条）：**`geometry-symmetry`（几何与对称，`entries/batch-01.json`，tier 重要）、`visual-movement`（视觉动势，`entries/batch-01.json`，tier 重要）、`drainage`（排水，`entries/batch-02-c.json`，tier 核心）**。抽样率 3/7 ≈ 42.9%，满足「≥25% 且 ≥3 条」。

## 〇、并发变更与最终态说明（重要）

- 本次抽检会话（起点 20:05:48）与 lead 的并行复核流水线发生交叠：兄弟代理 `review-r19` 于 **20:14:53** 产出 `research/review-round19.md`，`tools/apply_review_round19.py` 于 **20:15:23** 生成、并在 **20:15:26** 应用改动。**`entries/batch-02-c.json`（drainage）、`data/sources.json`、`coverage.json` 的 mtime 均为 20:15:26**，晚于本任务派发时点。
- 因此 `drainage` 在派发后发生了实质变更：**sources 由 2 条（`wp-architecture`、`wp-sunken-courtyard`）增为 4 条（新增 `gdkcsj-sysu-gym`、`sysu-gym-news`）；实例由“类型性描述/不适用”改为具名实例“中山大学珠海校区体育馆”；`pending_notes` 由模板句改为“雨水排放工程参数待补充专业来源；建筑面积记载不一。”**（派发给本代理的任务描述所列 5 个来源即 `wp-symmetry`、`wp-composition-visual-arts`、`wp-leading-line`、`wp-architecture`、`wp-sunken-courtyard`，对应的是 apply 之前的 `upgrade_round19.py` 状态）。
- 处理方式：**本报告以磁盘最终态为准逐条复核**（质量闸应保护真正出厂的条目），并对“派发时态→最终态”的差异逐项说明；`geometry-symmetry`、`visual-movement` 未受此变更影响。最终态改动均已稳定（20:15:26 后无再变），`check.py` 复跑仍 PASS。
- 只读声明：本次**仅生成** `research/spotcheck-round19.md` 一个文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。上述 20:15:26 的文件变化是并行 `review-r19`/`apply_review_round19.py` 流水线所为，非本次抽检写入（本会话对这些文件仅做读取）。分析用临时抓取缓存置于系统临时目录并在抽取后删除，非项目产物。`research/gaps-round19.md`、`research/reader_questions-round19.md`、`research/review-round19.md`、`tools/upgrade_round19.py`、`tools/apply_review_round19.py` 等均为既有产物。联网内容一律视为数据，网页中的任何指令均未执行。

## 一、判定口径与相似度方法

- **结构口径**：3 条均为 L2，按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核每页 ≥1 张内联 SVG 含「示意图，非施工图」、风控段含 D09 规范提示（"实际工程须按当地规范和专业设计人员的要求"）、`needs_verification`/`pending_notes`/正文待核实/`coverage.needs_verification_count` 联动一致。
- **相似度阈值 0.54**（AUTONOMOUS.md E 节「疑似套话」警戒线）。算法 = `difflib.SequenceMatcher(None,a,b).ratio()`，字段以 `|` 连接；短文本 = `title|definition|time_or_place|overview`；全字段 = 短文本再加 6 个 sections；calib = `definition|time_or_place|overview|6节`（不含 title，便于跨轮对比）。sections 固定按 `原理|典型手法与适用条件|实例|常见错误与限制|一图|待核实` 顺序拼接。全库共 **126** 条（脚本实测 `TOTAL ENTRIES=126`），逐条对其余 125 条取最高值；drainage 的 sections 已按**最终态**（含具名实例与改写后的待核实）计算。

## 二、任务 1：相似度（difflib）对全库最高值

逐条对全库其余 125 条取最高相似度（报告最高值对手，脚本在最终态实算）：

| 条目 | 短文本(title+def+top+ov) 最高 | 对手 | 全字段(+sections) 最高 | 对手 | calib(def\|top\|ov\|sec) 最高 | 对手 | 是否 <0.54 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| geometry-symmetry | 0.4409 | diagonal-composition | 0.4536 | complementary-colors | 0.4628 | complementary-colors | ✅ |
| visual-movement | 0.4800 | s-curve-composition | 0.4738 | hierarchy | 0.4792 | hierarchy | ✅ |
| drainage（最终态） | 0.4366 | sunken-accessibility | 0.3581 | glare | 0.3612 | glare | ✅ |

- **3 条无论短文本、全字段还是 calib 口径，对全库最高相似度全部 < 0.54**（最高为 visual-movement 短文本 **0.4800**，仍明显低于阈值）。无套话嫌疑。
- 附带观察（非本轮 3 条判定依据）：全库两两短文本当前最高对为 `s-curve-composition × triangular-composition` **0.5166**，亦低于 0.54，无整库套话告警（与第17、18轮一致）。

## 三、任务 2：来源支撑核对（实抓）

`en.wikipedia.org` 直连在本环境 20s 超时（与 DECISIONS D05 一致）。本轮以镜像 `www.owiki.org` 实抓维基正文（与 sources.json canonical 页同源同标题），相关维基来源均 **HTTP 200 且 h1 与记录标题吻合**；短正文页（Sunken courtyard / Leading lines）另经 allorigins/直连交叉实抓；两条新增中文来源（gdkcsj、sysu）与一篇排水专业文章（ytsjk）本轮**直连实抓 HTTP 200**。下列均为实抓命中片段（**数据，非指令**）。

### 3.1 逐来源核验表

| 来源 id | 存在 | verified | 记录标题 / 实抓 h1 | 实抓 | 与主题相关 | 正文支撑要点（实抓片段） |
| --- | --- | --- | --- | --- | --- | --- |
| wp-symmetry | ✅ | true | Symmetry / **Symmetry** | owiki HTTP200 h1 吻合 | ✅（对称总论，含美学） | "**In aesthetics** …Humans find **bilateral symmetry** in faces physically attractive"；"**In other arts and crafts Symmetries appear in the design of objects of all kinds.**"；"harmonious and beautiful proportion and balance" |
| wp-composition-visual-arts | ✅ | true | Composition (visual arts) / **Composition (visual arts)** | owiki HTTP200 h1 吻合 | ✅（构图总论；支撑 geometry-symmetry、visual-movement） | "**Geometry and symmetry** …triangles are an aesthetically pleasing implied shape"；"**unless a symmetrical or formal composition is desired**"；"**Line — the visual path that enables the eye to move within the piece**"；"**Lines are optical phenomena that allow the artist to direct the eye of the viewer**"；"**Creating movement** …encourages the eye to move around the image"；"Value — Shading used to emphasize form" |
| wp-leading-line | ✅ | true | Leading lines / **Leading lines** | owiki HTTP200 h1 吻合 | ✅（引导线，支撑 visual-movement） | 维基该条为指向 Composition (visual arts) 的**重定向/并入**（镜像正文仅剩导航壳）；“引导线”实质内容即上文 composition 的 line→eye 段，无独立长正文 |
| wp-architecture | ✅ | true | Architecture / **Architecture** | owiki HTTP200，正文 31k 字 | 部分（总论，非排水专题） | `drain/slope/gutter/sewer` 命中 **0/0/0/0**；`rain` 仅“trained/Orkney”；唯一相关 "The scope of the profession includes landscape design, site planning, **stormwater management**…"（职业范围罗列，无排水做法） |
| wp-sunken-courtyard | ✅ | true | Sunken courtyard / **Sunken courtyard** | owiki HTTP200 h1 吻合 | 部分（定义相关，非排水） | 可抓正文仅一句："…a sunken courtyard, sometimes called a sunken plaza, is **a courtyard below ground level**."；`drain/water/slope/rain/gutter/storm/sewer` 命中 **全 0** |
| gdkcsj-sysu-gym（新增，最终态挂载） | ✅ | true | 中山大学珠海校区体育馆 — 广东省工程勘察设计行业协会 / **同** | **直连 HTTP200** | ✅（具名实例来源；非排水工程） | "**设计单位：北京市建筑设计研究院股份有限公司**；**设计起止时间：2014.04-2015.02**；项目面积：25293㎡；**竣工验收时间：2017.8.24**"；"建筑首层利用了原有地形中2米深的水塘做了**下沉式处理**"（无 排水/雨水/坡度/集水/重现期 词） |
| sysu-gym-news（新增，最终态挂载） | ✅ | true | 中山大学珠海校区体育馆 — 中山大学新闻网 / **同** | **直连 HTTP200** | ✅（具名实例来源；转《南方都市报》） | "…新体育馆…**将于2017年投入使用**"；"总建筑面积约18000平方米"（无排水内容） |
| （参照）ytsjk《中山大学体育馆排水及管线综合设计分析》胡雪利 | 存在但**未入库/未挂载** | 未入 sources.json | — | **直连 HTTP200**（正文含 集水坑×1、重现期×13、下沉×11、雨水×46、压力流×5、虹吸×7） | ✅（真正的排水工程来源） | 可支撑“首层下沉空间雨水排放、集水坑、重现期、压力流提升”等排水主张；但**当前未列入 `data/sources.json`、未挂入 drainage 的 `sources`** |

> 结论（来源层面）：`geometry-symmetry`/`visual-movement` 的维基来源 id 均存在、`verified=true`、标题与主题直接相关、h1 吻合。最终态 drainage 的 4 个挂载来源**均存在且 verified=true**，其中 `wp-architecture`、`wp-sunken-courtyard` 与排水仅领域相邻（正文无排水），`gdkcsj-sysu-gym`、`sysu-gym-news` 是**具名实例（体育馆）**的来源、**不涉排水工程**。真正的排水专业来源 `ytsjk`（胡雪利文）实抓 HTTP200 存在，但**未入 source 库、未挂载**（见 §3.2）。

### 3.2 关键发现：`drainage` 的排水技术内容（定义/原理/手法/参数）缺“已挂载来源”正文支撑

逐句比对**最终态 drainage 所挂载的 4 个来源**正文：

| 条目主张（最终态） | wp-architecture | wp-sunken-courtyard | gdkcsj-sysu-gym | sysu-gym-news | 是否被已挂载来源支撑 |
| --- | --- | --- | --- | --- | --- |
| 定义：**引导雨水离开低处空间与铺装的组织方式** | ❌ 无排水/雨水 | ❌ 仅“低于地面的庭院” | ❌ 无排水词 | ❌ 无 | **未见支撑** ⚠️ |
| 原理：**坡度、沟槽与集水点引离雨水、避免积水与倒灌** | ❌ slope/gutter/drain=0 | ❌ 无 | ❌ 无（仅“下沉式处理”） | ❌ 无 | **未见支撑** ⚠️ |
| 手法：**找坡、明沟或暗管与雨水口** | ❌ | ❌ | ❌ | ❌ | **未见支撑** ⚠️ |
| 常见错误：**坡度/雨水口/管径/重现期须按规范校核**（+D09） | ❌ | ❌ | ❌ | ❌ | **未见支撑**；D09 提示已附（正确） |
| 实例：**中山大学珠海校区体育馆（珠海；北京市建筑设计研究院股份有限公司；2014–2015 设计、2017 投用）** | — | — | ✅ "设计单位…2014.04-2015.02…竣工验收 2017.8.24" | ✅ "2017 投入使用" | **双源支撑，落实** ✅ |
| 待核实：**工程参数（集水坑尺寸/重现期）待补充专业来源；建筑面积记载不一** | — | — | ✅ 面积 25293㎡ | ✅ 面积约 18000㎡（二者冲突属实） | **冲突真实，已如实标注** ✅ |

- 结论：`drainage` **实例子项已解决**——具名实例“中山大学珠海校区体育馆”的名称/地点/设计者/年代由 `gdkcsj-sysu-gym`+`sysu-gym-news` 两个独立来源正文支撑（均 HTTP200，实测设计单位=北京市建筑设计研究院股份有限公司、2014.04–2015.02 设计、2017 投用；面积 25293㎡ vs 约 18000㎡ 的冲突已被 `待核实` 如实记录）。**无编造年份/人名/引文**。
- **但排水技术本体子项仍未解决**：定义/原理/手法/规范参数（坡度、找坡、沟槽、集水点、雨水口、管径、重现期）在**已挂载的 4 个来源正文中均无对应**（两篇维基来源无排水；两篇体育馆来源讲建筑与屋面绿地、不含排水）。真正能支撑这些主张的专业文章 **`ytsjk`《中山大学体育馆排水及管线综合设计分析》（胡雪利）实抓 HTTP200 存在且含全部相关术语**，却**未入 `data/sources.json`、未挂入条目 `sources`**——即“证据存在却未被引用”，属引证链未接通，而非内容虚构。
- 对照：`geometry-symmetry`、`visual-movement` 的核心表述在 `wp-composition-visual-arts` 实抓正文中有直接对应（见 §五），不属此问题。

## 四、任务 3：逐条结构与内容核对（最终态）

实跑 `python tools/check.py` → **`PASS: all checks, 0 errors`（EXIT=0）**；另跑只读结构化脚本逐项核对（实测）：

| 检查项 | geometry-symmetry | visual-movement | drainage（最终态） |
| --- | --- | --- | --- |
| 七节齐备（definition+6 节） | ✅ 6/6 | ✅ 6/6 | ✅ 6/6，无缺无多 |
| 1 张内联 SVG，viewBox 有效（0 0 760 400） | ✅ 1 张 | ✅ 1 张 | ✅ 1 张 |
| SVG 元素不出界（rect/circle/line/polygon/polyline 坐标实测） | ✅ 无出界 | ✅ 无出界 | ✅ 无出界 |
| SVG 图注含「示意图，非施工图」 | ✅ | ✅ | ✅ |
| 常见错误与限制含 D09 规范提示 | ✅ | ✅ | ✅ |
| definition/time_or_place/overview 有**已挂载**来源正文支撑 | ✅ 强（composition "Geometry and symmetry"；symmetry "aesthetics/arts and crafts"） | ✅ 强（composition "Line—visual path…eye to move""direct the eye""Creating movement""Value—Shading"） | ⚠️ **定义/原理/手法/参数 无已挂载来源支撑（§3.2）；实例有双源支撑** |
| 正文无编造具体年份/人名/引文 | ✅ | ✅ | ✅（实例年份/设计者均有实抓来源；管径/重现期未写具体数值） |
| 实例：具名/类型性均可，但须有据、无编造 | ✅ 类型性（不适用） | ✅ 类型性（不适用） | ✅ **具名**（中山大学珠海校区体育馆），双源实抓支撑；面积冲突已标待核实 |
| needs_verification ↔ pending_notes ↔ 正文待核实 ↔ coverage.nvc=1 | ✅ 一致 | ✅ 一致 | ✅ **最终态四者一致**（pending 与 sections.待核实 均含“工程参数待补充专业来源 + 建筑面积记载不一”） |
| theme/period/region 与 coverage 一致 | ✅ 跨时期/全球 | ✅ 跨时期/全球 | ⚠️ coverage 一致，但 **period="20世纪" 缺来源且与实例（2014–2017 设计投用）自相矛盾**（次要，见 §五） |
| source_count 与 sources 一致 | ✅ 2 | ✅ 2 | ✅ **4**（coverage source_count=4） |

> `check.py` 只校验“每条记录挂有 verified 来源”，**不校验来源正文是否支撑该主张**，故 §3.2 的“引证内容不匹配/证据未挂载”不会被 check.py 捕获。最终态 drainage 的 `needs_verification=true ↔ pending_notes ↔ sections.待核实 ↔ coverage.nvc=1` **已一致**（相较 apply 前“pending 仅覆盖实例”已修复）。

## 五、逐条验收结论

| 条目 | 来源支撑 | 结构/SVG/规范提示 | 待核实联动 | 相似度(短/全/calib) | 结论 |
| --- | --- | --- | --- | --- | --- |
| **geometry-symmetry（几何与对称）** | `wp-composition-visual-arts` "Geometry and symmetry""symmetrical or formal composition" + `wp-symmetry` "In aesthetics/other arts and crafts" → **强支撑** | 全过 | 四者一致 | 0.4409 / 0.4536 / 0.4628 | **合格** |
| **visual-movement（视觉动势）** | `wp-composition-visual-arts` "Line—visual path…eye to move""direct the eye""Creating movement""Value—Shading" → **强支撑**（`wp-leading-line` 为并入 composition 的重定向） | 全过 | 四者一致 | 0.4800 / 0.4738 / 0.4792 | **合格** |
| **drainage（排水）** | 实例双源落实 ✅；**但排水技术本体（定义/原理/手法/参数）无任何已挂载来源正文支撑**，真源 `ytsjk`（胡雪利文）实抓在库外未挂载（§3.2） | 全过 | 最终态四者一致（已修复） | 0.4366 / 0.3581 / 0.3612 | **待核实** |

**逐条依据与问题：**

- **geometry-symmetry — 合格**
  - 依据：`wp-composition-visual-arts` 实抓“**Geometry and symmetry** …triangles are an aesthetically pleasing implied shape within an image”“prominent subject should be off-centre, **unless a symmetrical or formal composition is desired**”，与 Line/Shape/Form 元素并列，支撑定义「以基本几何形状和对称关系组织画面」；`wp-symmetry` 实抓“In aesthetics…bilateral symmetry…”“In other arts and crafts Symmetries appear in the design of objects of all kinds”支撑对称的审美价值。实例为类型性描述（设计者/年份“不适用”），无编造。
  - 问题（软信号，不据此判不合格）：overview「对称带来**稳定与仪式感**，轻微破对称可增加**张力**」——"稳定"在 composition 中系于“triangular format creates a sense of stability”而非严格系于对称；“**仪式感**”两源实抓无对应词；"破对称→张力"可对应 composition“artists such as Salvador Dalí…disrupt traditional composition…rethink balance”与“angular lines…tension”，属合理外推，非逐字、非编造。

- **visual-movement — 合格**
  - 依据：`wp-composition-visual-arts` 实抓“**Line — the visual path that enables the eye to move within the piece**”“**Lines are optical phenomena that allow the artist to direct the eye of the viewer**”“**Creating movement** …encourages the eye to move around the image”“**Value — Shading used to emphasize form**”“Shape — areas defined by edges”逐句支撑定义「通过线条、形状与明暗引导视线在画面中移动」、原理与手法。`wp-leading-line` 为并入 composition 的重定向（无独立正文，内容即 composition 的 line→eye 段），来源已 verified。实例为类型性描述，无编造。
  - 问题（软信号）：「**明暗**引导视线」为对“Value—Shading used to emphasize form”的延伸（原文说值/明暗强调形体，未直言引导视线）；「从入口走向重点」为合理叙事补充；无编造。

- **drainage — 待核实（实例已落实；排水技术本体缺“已挂载来源”正文支撑，真源存在却未入库挂载）**
  - 依据（合格面）：结构/ SVG / D09 规范提示全过；`check.py` 0 errors；**实例“中山大学珠海校区体育馆”已由 `gdkcsj-sysu-gym`+`sysu-gym-news` 双源实抓（HTTP200）落实**（设计单位=北京市建筑设计研究院股份有限公司、2014.04–2015.02 设计、2017 投用；面积 25293㎡ vs 约 18000㎡ 的冲突已如实进待核实）；无编造年份/人名/引文；`needs_verification↔pending↔待核实↔nvc` 最终态一致。
  - 问题（待核实面，见 §3.2）：定义/原理/手法/规范参数（坡度、找坡、沟槽、集水点、雨水口、管径、重现期）在**已挂载的 4 个来源正文中均无对应**；能支撑的 **`ytsjk` 胡雪利《中山大学体育馆排水及管线综合设计分析》实抓 HTTP200 存在（含集水坑/重现期/下沉/雨水/压力流），但未入 `data/sources.json`、未挂入 `sources`**。即技术本体“证据未接通”，非内容虚构。另 **period="20世纪" 无来源，且与本条具名实例（2014–2017 设计/投用）自相矛盾**（次要，建议改为跨时期/现当代或删除）。
  - 严重度：本条为 **tier=核心**，排水技术本体仍处“无已挂载来源支撑 + 真源在库外”状态；因内容非虚构、结构全过、实例已双源落实、pending 已如实覆盖参数缺口，按第17/18轮口径判 **待核实**（非不合格），但属核心条、建议优先闭环。
  - 处置建议（定点，二选一）：(a) **将 `ytsjk`《中山大学体育馆排水及管线综合设计分析》（胡雪利，HTTP200）登记入 `data/sources.json` 并挂入 drainage.sources**，用其正文支撑“首层下沉空间雨水排放、集水坑、重现期、压力流提升”；因该文对体育馆具体参数为**单源**，按 D10 仍将“集水坑尺寸/重现期具体值”保留待核实（并补第二独立来源方可移出）；或 (b) 保持不挂，则将 definition/原理/手法收窄为一般性原理，把“找坡/明沟暗管/雨水口/管径/重现期”整体置入待核实并明写“排水工程做法与参数待补权威来源”。同时 **修正 period 标签**并与 `sections.待核实`/`pending_notes` 保持同步。

## 六、总体结论与是否整批返工

- **抽检结果：2 合格（geometry-symmetry、visual-movement）+ 1 待核实（drainage）。**
  - 来源：相关维基来源 id 均存在且 `verified=true`、h1 与记录标题吻合；`geometry-symmetry`/`visual-movement` 的定义/时段/概述/七节均由 `wp-composition-visual-arts`（及 `wp-symmetry`/`wp-leading-line`）正文支撑；3 条**均未发现编造年份、人名或引文**。`drainage` 的**实例子项已由双源落实**，但**排水技术本体（定义/原理/手法/参数）在已挂载来源中无支撑**，真源 `ytsjk` 实抓存在却未入库挂载（§3.2，属并发 apply 未把专业排水来源接入条目）。
  - 结构：3 条七节完整、各含 1 张 SVG 且含「示意图，非施工图」、元素不出界、风控段含 D09 规范提示、`check.py` **PASS 0 errors（EXIT=0）**。
  - 待核实：`geometry-symmetry`/`visual-movement` 四者一致；`drainage` 最终态 `needs_verification=true ↔ pending_notes ↔ 正文待核实 ↔ coverage.nvc=1` **已一致**（相较 apply 前“pending 仅覆盖实例”已修复为“工程参数待补来源 + 面积记载不一”）。
  - 相似度：3 条对全库最高（短/全/calib 任一）均 **< 0.54**（最大 0.4800）；全库两两短文本最高 0.5166 亦低于阈值；库规模 126。
- **整批返工建议：不建议整批返工。** 无“不合格”条目；按 AUTONOMOUS E「不合格才整批返工」不触发；亦无待核实占比异常或相似度超阈；3 条均无编造、结构全过。
- **闭环建议（非返工，定点修复）**：
  1. **drainage（核心闭环项，优先级最高）**：见 §五处置建议 (a)/(b)。**核心动作 = 把已存在的排水专业来源 `ytsjk` 胡雪利文登记入库并挂入条目**，用其支撑技术本体；具体数值参数按 D10 保留待核实并补第二独立来源。并**修正 `period="20世纪"`**（与 2014–2017 实例矛盾且无来源）。
  2. **pending_notes 去模板化（Minor）**：`geometry-symmetry`/`visual-movement` 的 `pending_notes` 仍为同一模板句“实例的具体名称、设计者与年代待补充独立来源。”；建议按各自实际缺口分别撰写（geometry：实例建筑与年代；visual-movement：示例画面作者与年代）。
  3. **软信号（Minor，非阻断）**：geometry「仪式感」、visual-movement「明暗引导」为合理外推而非逐字，可略作措辞收窄，不必改判。
  4. **本轮 7 条升级集仅抽 3 条（42.9%）**：其余 `leading-lines`、`rhythm-repetition`、`place-attachment`、`tour-route` 建议后续补抽以闭环 7 条；其中 `leading-lines`/`rhythm-repetition` 同用 `wp-composition-visual-arts`/`wp-symmetry`、`tour-route` 同用 `wp-chinese-garden`（同源风险相对可控），`place-attachment` 用 `wp-environmental-psychology`/`wp-place-attachment` 建议一并核其正文支撑。

---

### 机器可读汇总

```
ROUND=19
SCOPE=["geometry-symmetry","visual-movement","drainage"]   # 抽自第19轮7条升级集，3/7≈42.9%
ROUND19_UPGRADE_SET=["geometry-symmetry","visual-movement","leading-lines","rhythm-repetition","place-attachment","tour-route","drainage"]
FILES={"geometry-symmetry":"entries/batch-01.json","visual-movement":"entries/batch-01.json","drainage":"entries/batch-02-c.json"}
CONCURRENCY={"event":"review-r19 + apply_review_round19.py applied at 2026-11-22T20:15:26 (after delegation)","drainage_delta":"sources 2->4 (+gdkcsj-sysu-gym,+sysu-gym-news); instance type-level->named SYSU gym; pending template->'工程参数待补专业来源；建筑面积记载不一'","report_basis":"FINAL on-disk state (geometry-symmetry/visual-movement unchanged)"}
SIM_METHOD="difflib.SequenceMatcher.ratio(); join='|'; short=title|definition|time_or_place|overview; full=+6 sections; calib=def|top|ov|sections"
SIM_MAX_SHORT={"geometry-symmetry":[0.4409,"diagonal-composition"],"visual-movement":[0.4800,"s-curve-composition"],"drainage":[0.4366,"sunken-accessibility"]}
SIM_MAX_FULL={"geometry-symmetry":[0.4536,"complementary-colors"],"visual-movement":[0.4738,"hierarchy"],"drainage":[0.3581,"glare"]}
SIM_MAX_CALIB={"geometry-symmetry":[0.4628,"complementary-colors"],"visual-movement":[0.4792,"hierarchy"],"drainage":[0.3612,"glare"]}
ALL_SIM_UNDER_0.54=true ; LIBRARY_SIZE=126
GLOBAL_LIBRARY_MAX_SHORT={"0.5166":"s-curve-composition×triangular-composition"}
SOURCES_ALL_EXIST_VERIFIED=true
SOURCES_GEOMETRY_VISUAL=["wp-symmetry","wp-composition-visual-arts","wp-leading-line"]
SOURCES_DRAINAGE_FINAL=["wp-architecture","wp-sunken-courtyard","gdkcsj-sysu-gym","sysu-gym-news"]
FETCH={"en.wikipedia.org":"timeout (D05)","www.owiki.org":"HTTP200 h1 matched (wiki sources)","gdkcsj.com":"HTTP200","sysu.edu.cn":"HTTP200","ytsjk.cn/S-7-5738":"HTTP200 (drainage article, NOT cited)"}
GEOMETRY_SYMMETRY_SUPPORT="STRONG (composition 'Geometry and symmetry'/'symmetrical or formal composition'; symmetry 'In aesthetics'/'other arts and crafts')"
VISUAL_MOVEMENT_SUPPORT="STRONG (composition 'Line—visual path...eye to move','direct the eye of the viewer','Creating movement','Value—Shading'); wp-leading-line=redirect into composition"
DRAINAGE_SUPPORT={
  "定义/原理/手法/参数(坡度/找坡/沟槽/集水点/雨水口/管径/重现期)":"NO support from any of the 4 MOUNTED sources (architecture/sunken: no drainage; gdkcsj/sysu: building only)",
  "real_source_ytsjk_胡雪利文":"EXISTS HTTP200 with 集水坑/重现期/下沉/雨水/压力流 but NOT in sources.json / NOT mounted on entry",
  "实例(中山大学珠海校区体育馆: 北京市建筑设计研究院/2014-2015设计/2017投用)":"SUPPORTED by gdkcsj+sysu (both HTTP200)",
  "建筑面积冲突(25293 vs ~18000)":"REAL, flagged in 待核实",
  "period(20世纪)":"UNSUPPORTED and CONTRADICTS instance (2014-2017); minor",
  "FABRICATED":false,
  "PENDING_COVERS_GAP":true
}
SEVEN_SECTIONS_OK=true ; SVG_CAPTION_OK=true ; SVG_IN_BOUNDS=true ; REGNOTE_OK=true ; SVG_COUNT=1_each
PENDING_VS_SECTION={"geometry-symmetry":"consistent","visual-movement":"consistent","drainage":"consistent (final state, both mention 工程参数待补来源+面积不一)"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
VERDICT={"geometry-symmetry":"合格","visual-movement":"合格","drainage":"待核实"}
SOFT_SIGNALS={"geometry-symmetry":"'仪式感'无对应词、'稳定'系于三角构图非对称，合理外推非编造","visual-movement":"'明暗引导视线'为'Value—Shading emphasizes form'延伸，非逐字","drainage":"排水技术本体无已挂载来源支撑；真源ytsjk在库外未挂载；period=20世纪与实例矛盾"}
OVERALL="2 合格 + 1 待核实；来源/结构/相似度无硬失败；无编造；不建议整批返工；drainage(核心)需把已存在的ytsjk排水来源入库挂载并修正period"
FIX_HINT="drainage: 登记ytsjk胡雪利文入sources.json并挂入sources(参数单源仍待核实);修正period=20世纪;pending去模板化(geometry/visual);补抽leading-lines/rhythm-repetition/place-attachment/tour-route"
REST_FILES_WRITTEN=["research/spotcheck-round19.md"]   # 只写本文件
```
