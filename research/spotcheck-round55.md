# 第55轮质量抽检报告（spotcheck-round55）——第55轮补具名实例的 3 条（sunken-atrium / earth-sheltered / rockery）

- 抽检人：spotcheck-r55（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 16:56–17:09，Asia/Hong_Kong（CST）。
- 任务：对第55轮「补具名实例」条目中 lead 定向点名的 3 条——`sunken-atrium`（`entries/batch-35.json` 286–316 行）、`earth-sheltered`（`entries/batch-38.json` 98–128 行）、`rockery`（`entries/batch-35.json` 96–126 行）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动；核对相似度（阈值 0.54）。来源均在 `data/sources.json`。
- 抽样说明：第55轮工作树改动含 8 条补具名实例条目（`review-round55a.md` 4 条：sunken-garden / sunken-atrium / semi-sunken-space / earth-sheltered；`review-round55b.md` 4 条：rockery / planting-design / seasonal-scenery / visitor-route），本轮抽检 3 条，占 3/8=37.5%，高于 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限。其余本轮改动条目只作状态观察，不列入内容判定。
- 协议依据：`AUTONOMOUS.md` §E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，不下载运行来源代码，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14/D16。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓证据、后下断言；关键句均以本轮 web_fetch / urllib / curl 实抓回读为准）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 16:56 起）**：`data/sources.json`=**205599B**、`coverage.json`=87347B（258 条）、`entries/batch-35.json`=23685B、`entries/batch-38.json`=64106B、`tools/check.py`=15908B。
- **`git log -1`** = `66c001d docs: note round54 push status`；第55轮改动尚未提交。`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-35.json`、`M entries/batch-36.json`、`M entries/batch-38.json`、8 个 `site/entries/*.html`、`site/index.html`、`site/sources.html`，以及 `?? research/healthcheck-round55.md`、`?? research/review-round55a.md`、`?? research/review-round55b.md`、`?? tools/apply_review_round55.py`（lead 侧底稿/脚本，本抽检不触碰）。抽检对象即上述未提交工作树中的 3 条现状，非 HEAD 内容。
- **规模与来源库**：`coverage.json` 实读 `total=258`；`pending_sum`（`needs_verification_count` 求和）=**195**（第54轮报告为 203，本轮净降 8，`195/258≈75.6%` 为存量待核实占比，非「异常低」）。`data/sources.json` 共 **430** 条，`verified=true` **427**、`verified=false` **3**。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（`open(...,'w')`/`write_text`/`.write(`/`shutil`/`unlink`/`os.remove` 均 0 命中）。
- **只读声明**：本次**仅写出** `research/spotcheck-round55.md` 一个项目文件；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/review-round55a.md`、`research/review-round55b.md`、`tools/apply_review_round55.py` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容（抓取全程内存，临时文件即用即删）。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`PROGRESS.md`、`research/spotcheck-round54.md`（231 行）、`research/healthcheck-round55.md`（10 行）、`research/review-round55a.md`（140 行）、`research/review-round55b.md`（115 行）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾；SVG 元素不出 `viewBox`、无 `on*` 事件属性、无外链图片。
- **抓取与回验方法**：`web_fetch` 本轮对 Louvre / PCF / Moesgaard / Henning / Wikipedia 多页成功（HTTP 200，返回全文可见关键句）；部分站点受跳转/反爬影响（UNESCO 813 本轮 403、苏州市园林局页 web_fetch 重定向失败），改用 `urllib`/`curl` + 浏览器 UA 直连；关键句按大小写/空白归一（`norm()`/`lower()`）做上下文回读，并与 `review-round55a/b.md` 同日逐字回执交叉核对。10/11 个去重 URL 本轮实抓 HTTP 200；UNESCO 本轮 403 反爬，按反爬/连接异常而非死链处理（`review-round55b.md` 同日 200 回执）。
- **三级判定定义（沿用第51–54轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项（七节/SVG/规范句/元数据/pending 联动）全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源/无源，或第二源只覆盖部分结构且单源/概念归纳未如实披露；或 pending 联动与来源实况不一致——属来源深度或披露缺陷，非编造。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，按 `sections` 原始插入顺序、`一图` 解说文字计入、`svg` 标记不计入），归一为去空白+小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–54轮报告逐位一致，口径正确。
- **相似度是独立维度**：超线触发 §E「整批降级」，与「不合格（内容无源）→整批返工」是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

3 条共引用 **11 个来源 id（12 处引用：每条目 4；`wp-sunken-courtyard` 被 sunken-atrium / earth-sheltered 共用）**，全部存在、全部 `verified=true`、`year=null`（D06 允许）、无 `link_ok=false`（新登记 6 源均 `link_ok=null` 三态未标，非死链）。

| 条目 | 来源 id | 机构 / type | 实抓标题或端点（本轮证据） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| sunken-atrium | `louvre-pyramid-symbol` | Musée du Louvre / 官方机构 | `A pyramid for a symbol - Cour Napoléon & Pyramid`（HTTP 200） | true / null | **相关（直接·强·实例主证）**：`central underground lobby affording direct access to the museum's three wings`；`the most transparent, light and luminous structure possible`；`inaugurated on 29 March 1989`；`Chinese-American architect Ieoh Ming Pei` |
| sunken-atrium | `pcf-grand-louvre` | PCF Architects / 建筑师事务所 | `Grand Louvre Modernization - PCF Architects`（HTTP 200） | true / null | **相关（直接·强·实例佐证）**：`Hall Napoleon with underground links to museum wings`；`areas within and below the existing museum`；`direct access to galleries in each of the museum's three wings` |
| sunken-atrium | `wp-atrium-architecture` | Wikipedia / 权威百科 | `Atrium (architecture) - Wikipedia`（HTTP 200） | true / — | **相关（概念背景）**：`skylight` / `central` / `light` 命中，支撑「中庭天窗采光」通识 |
| sunken-atrium | `wp-sunken-courtyard` | Wikipedia / 权威百科 | `Sunken courtyard - Wikipedia`（HTTP 200） | true / — | **相关（概念背景）**：`sunken courtyard` / `below ground level` 命中 |
| earth-sheltered | `moesgaard-building` | Moesgaard Museum / 官方机构 | `Building and landscape - Moesgaard`（HTTP 200） | true / null | **相关（直接·强·实例主证）**：`opened in 2014`；`designed by Henning Larsen Architects`；`staggered levels ... inspired by archaeological excavations`；馆址 Højbjerg |
| earth-sheltered | `henning-moesgaard` | Henning Larsen Architects / 官方机构 | `Moesgaard \| Henning Larsen`（HTTP 200） | true / null | **相关（直接·强·实例佐证）**：`Aarhus, Denmark`；`2009 - 2014`；`Nestled into the rolling landscape of southern Aarhus`；`sloping roof, landscaped with grass and moss`；`allow natural light into the exhibition spaces below` |
| earth-sheltered | `wp-architecture` | Wikipedia / 权威百科 | `Architecture - Wikipedia`（HTTP 200） | true / — | **弱相关（概念背景·不支撑热工定义）**：全页无 `thermal mass`/`earth shelter`；`insulat` 唯一命中在「斯瓦希里海岸陶瓦屋顶隔热」无关语境 |
| earth-sheltered | `wp-sunken-courtyard` | Wikipedia / 权威百科 | 同上（HTTP 200） | true / — | **弱相关（概念背景）**：`sunken courtyard` / `below ground level`；与覆土热工无直接对应 |
| rockery | `suzhou-lion-grove` | 苏州市园林和绿化管理局 / 官方机构 | `狮子林 - 苏州市园林局`（curl HTTP 200，43887B） | true / null | **相关（直接·强·实例主证）**：`狮子林位于江苏省苏州市城区东北角的园林路23号`；`国内尚存最大的古代假山群`；`以"适、漏、瘦、皱"的太湖石堆叠的假山，玲珑俊秀，洞壑盘旋`；`元至正二年(1342)，弟子们买地置屋为天如禅师建禅林` |
| rockery | `unesco-suzhou` | UNESCO World Heritage Centre / 官方机构 | `Classical Gardens of Suzhou - UNESCO`（本轮 403 反爬；review-round55b 同日 200） | true / null | **相关（直接·实例佐证）**：`the Lion Grove Garden` 列入苏州九处代表；`rock formations` 构成园林 |
| rockery | `wp-chinese-garden` | Wikipedia / 权威百科 | `Chinese garden - Wikipedia`（HTTP 200） | true / — | **相关（概念背景）**：`artificial mountains and rock gardens`；`taihu` 太湖石 |
| rockery | `wp-garden-design` | Wikipedia / 权威百科 | `Garden design - Wikipedia`（HTTP 200） | true / — | **相关（概念背景）**：`rock garden, also known as rockery or alpine garden` |

> 11 源全部 `verified=true`、无假 id；`link_ok=null` 仅表示三态未标。关键相关性结论：`sunken-atrium`、`rockery` 的实例四要素均获双源直证；`earth-sheltered` 的实例四要素双源直证，但其 definition/overview 的「土体保温隔热/土壤蓄热使室内温度平稳」在所引四源正文中均无支撑（见 3.2）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 sunken-atrium（地下中庭，第55轮改动）——**合格**

- 条目现状（实读 `entries/batch-35.json` 286–316 行）：`definition`＝「地下中庭贯通地下若干层，靠天窗或下沉庭院把光送到最深处。」；`time_or_place`＝「20世纪、全球（参见来源）。」；`overview`＝「它同时承担采光、交通与公共活动，是地下空间的组织核心。」；`实例`＝「名称：卢浮宫金字塔与拿破仑大厅（Pyramide / Hall Napoléon）；地点：法国巴黎卢浮宫拿破仑庭院；设计者：贝聿铭（I. M. Pei）；年份：1989 年 3 月 29 日启用。中央地下大厅直通博物馆三翼。……」
- **definition / time / overview 支撑**：Louvre 官方明记 `central underground lobby affording direct access to the museum's three wings`、`the most transparent, light and luminous structure possible`、小金字塔 `bring light into the entrances of the museum's three wings`、`transform visitor circulation inside the Louvre`、`ticket office, auditorium, cafés, bookshops – even a shopping centre` → 「贯通地下多层」「天窗采光」「交通与公共活动」「组织核心」均有直接正文支撑；PCF `areas within and below the existing museum`、`Hall Napoleon with underground links to museum wings` 独立佐证「地下多层 + 三翼连通」。`wp-atrium-architecture`（skylight/central/light）与 `wp-sunken-courtyard`（sunken courtyard/below ground level）作概念背景。非编造。
- **实例双源直证**：
  - Louvre 官方（本轮 HTTP 200）：`Chinese-American architect Ieoh Ming Pei`（设计者）、`inaugurated on 29 March 1989`（年份）、`Cour Napoléon`（地点）、`Pyramid` + `central underground lobby`（名称/空间类型）→ 名称、地点、设计者、年份四项逐字直证。
  - PCF Architects（本轮 HTTP 200）：同一 Grand Louvre 项目，`Hall Napoleon with underground links to museum wings`、`A centrally located glass pyramid ... direct access to galleries in each of the museum's three wings` → 从设计方项目档案独立佐证同一实例的名称/地点/地下连通结构。
  - 两源为不同机构（博物馆官方 + 建筑师事务所官方），均直接相关；年份 1989-03-29 由 Louvre 官方直书（PCF 项目档案同项目佐证，未以另一口径改年），符合底稿 `review-round55a.md` §2.2 分工，不构成实质单源缺陷。条目写「中央地下大厅直通博物馆三翼」与 Louvre 原文一致，未夸大为「独立新建馆」（底稿保留标注已遵守）。
- **七节其他内容**：`原理`「中庭贯通地下多层并通过天窗或下沉庭院引入天然光」由 Louvre + PCF 支撑；`典型手法与适用条件`「围绕中庭布置交通与公共功能」由 Louvre `visitor circulation`/`auditorium`/`shopping centre` 支撑。
- **无编造**：核心定义、time 语境、overview、卢浮宫实例四要素与年份均由引用来源正文支撑；不复制图像。
- **问题（轻微）**：① `time_or_place`「20世纪、全球」为一般分类，实例本身为 1989 年巴黎，来源未逐字给「20世纪」口径，属通识概括、无具体数字人名，可接受；② 本条与 `visitor-route` 共用卢浮宫金字塔实例（全字段相似度 0.4478，见第七节），属同实例跨条目复用，非套话，建议两条目侧重点保持区分（本条重「地下中庭采光/交通」，visitor-route 重「参观动线组织」）；③ 两源 `link_ok=null` 三态未标，已如实标。
- **内容判定：合格**。`needs_verification=false`、pending 空、待核实「暂无已知待核实项。」与双源实况一致。

### 3.2 earth-sheltered（覆土建筑，第55轮改动）——**待核实**

- 条目现状（实读 `entries/batch-38.json` 98–128 行）：`definition`＝「覆土建筑指部分或全部覆土、以土体保温隔热的建筑。」；`time_or_place`＝「20世纪、全球（参见来源）。」；`overview`＝「它以土壤蓄热使室内温度平稳、并融入地形。」；`原理`＝「覆土建筑指部分或全部覆土、以土体保温隔热的建筑。它以土壤蓄热使室内温度平稳、并融入地形。」（**系 definition + overview 逐字重复**）；`实例`＝「名称：莫斯高博物馆（Moesgaard Museum）；地点：丹麦奥胡斯南部；设计者：亨宁·拉森建筑事务所（Henning Larsen Architects）；年份：2014 年开馆（2009–2014 设计施工）。坡地覆土、草皮屋顶、自然光进入地下展厅。……」
- **实例双源直证（扎实）**：
  - Moesgaard 官方（本轮 HTTP 200）：`When our exhibition building opened in 2014`、`The building was designed by Henning Larsen Architects`、`staggered levels ... inspired by archaeological excavations`、馆址 `Moesgård Allé 15, DK-8270 Højbjerg` → 名称、设计者、年份直证；Højbjerg 属奥胡斯南部。
  - Henning Larsen 官方（本轮 HTTP 200）：`Aarhus, Denmark`、`2009 - 2014`、`Nestled into the rolling landscape of southern Aarhus`、`publicly accessible sloping roof, landscaped with grass and moss`、`light well apertures that form terraces and allow natural light into the exhibition spaces below` → 地点（奥胡斯南部）、年份（2009–2014）、「坡地覆土、草皮屋顶、自然光进入地下展厅」逐字直证。
  - 两源为不同机构（业主/博物馆官方 + 设计方事务所官方），四要素双源直证；底稿 `review-round55a.md` §2.3「坡地覆土/半掩覆型、非全地下住宅」的诚实标注已落地。实例层面无编造。
- **definition / overview 热工主张无来源正文支撑（判待核实主因）**：definition 的核心谓语「以土体保温隔热」与 overview 的「土壤蓄热使室内温度平稳」是全条的定义性机制主张。本轮对四源正文逐词回验：`wp-architecture` 全页无 `thermal mass`/`earth shelter`，唯一 `insulat` 命中在「斯瓦希里海岸陶瓦屋顶隔热」无关语境；`wp-sunken-courtyard` 的 `thermal`/`insulat`/`temperature`/`earth` 全部 MISS；`moesgaard-building` 的 `thermal`/`insulat`/`temperature`/`energy`/`mass` 全部 MISS；`henning-moesgaard` 的 `thermal`/`insulat`/`temperature` 全部 MISS（`energy`/`climate`/`mass` 命中均在无关 JSON 元数据或「building mass」非热工语境）。即**四源无一正文支撑该热工机制**。该主张是具体物理机制描述（非「和谐/理性」式纯概念归纳），且两条 Wikipedia 概念源本身与覆土建筑并不直接对应。按「关键事实至少两个独立来源互证，否则标待核实」与第54轮 constructivism「红色几何」同类口径，判待核实（属来源深度/披露缺陷，非编造——无假 id、无死链、实例本身有源）。
- **七节「原理」逐字重复（次要·套话）**：`原理` 仅复制 definition + overview，未提供独立的机制 Explanation，属第54轮起持续关注的「套话/模板」质量问题，`check.py` 查不出该语义项。建议在补源或改写定义时一并重写「原理」。
- **needs_verification 联动失真（重点·须定向处理）**：`needs_verification=false`、pending 空、待核实「暂无已知待核实项。」。实例四要素扎实，实例层面清零恰当；但 definition/overview 的热工主张无源且未在待核实字段披露，属披露缺陷。按第54轮 constructivism 同类口径，判待核实级披露问题。
- **其他（轻微）**：① `time_or_place`「20世纪」与实例源 2009–2014（21世纪）不完全对应，属一般分类口径；② `wp-architecture`/`wp-sunken-courtyard` 两条概念源与本条覆土热工定义关联弱，建议注明为概念背景或替换为直接相关的覆土建筑热工权威源；③ SVG 含 `<ellipse cx=327 cy=269 rx=37 ry=333>`，`ry=333` 使椭圆纵向约 -64~602 超出 `viewBox 0 0 760 400`，但 `check.py` 仅校验 cx/cy/r 不校验 rx/ry，属脚本盲区下的潜在出界（示意装饰元素，次要）。
- **内容判定：待核实**。建议：补一独立权威源直证覆土建筑的热工机制（土壤蓄热/保温隔热），或将 definition/overview/原理 改写为有源表述（如「覆土建筑指部分或全部覆土、草皮屋顶嵌入地形、展厅位于其下并由采光井补光」），并据此改写「原理」；若无法补齐则恢复 `needs_verification=true` 并据实写 pending/待核实，同步 `coverage.json` 计数。

### 3.3 rockery（叠石，第55轮改动）——**合格**

- 条目现状（实读 `entries/batch-35.json` 96–126 行）：`definition`＝「叠石是以假山石堆叠模拟自然山峦的造园手法。」；`time_or_place`＝「古代、中国（参见来源）。」；`overview`＝「叠石以石形与堆法营造峰、峦、洞、壑。」；`原理`＝「依石的瘦、透、漏、皱选石，按山势堆叠，模拟自然山岳的起伏与洞穴。」；`实例`＝「名称：苏州狮子林湖石假山群；地点：中国江苏苏州园林路；设计者：天如禅师及弟子（无单一设计师）；年份：元至正二年（1342 年）。」
- **definition / time / overview 支撑**：`wp-garden-design` 明记 `rock garden, also known as rockery or alpine garden`、`extensive use of rocks and stones`；`wp-chinese-garden` 含 `artificial mountains and rock gardens`、`taihu` 太湖石 → 「以假山石堆叠模拟自然山峦」直接支撑。苏州市园林局 `以"适、漏、瘦、皱"的太湖石堆叠的假山，玲珑俊秀，洞壑盘旋`、`石峰和石笋` → 「石形堆法营造峰/洞/壑」与「瘦、透、漏、皱选石」直接支撑（来源作「适、漏、瘦、皱」，条目用通行的「瘦、透、漏、皱」，属同组太湖石品评标准的通行表述，无编造数字/人名）。非编造。
- **实例双源直证**：
  - 苏州市园林和绿化管理局（本轮 curl HTTP 200，43887B）：`狮子林位于江苏省苏州市城区东北角的园林路23号`（地点）、`国内尚存最大的古代假山群`/`假山王国`（名称/类型）、`元至正二年(1342)，弟子们买地置屋为天如禅师建禅林`（年份 + 营造主体）→ 名称、地点、年份直证，设计者以「天如禅师及弟子（无单一设计师）」如实标注营造主体，符合底稿 `review-round55b.md` §2.1「只写营造主体、不编造个人名」要求。
  - UNESCO 世界遗产中心（本轮 403 反爬，`review-round55b.md` 同日 200 逐字回执）：`the Lion Grove Garden` 列入苏州九处代表、`rock formations` 构成园林 → 独立佐证狮子林为苏州古典园林代表且以叠石/岩峰构景。
  - 两源为不同机构（园林主管机关 + UNESCO），均直接相关；年份 1342 由园林主管机关直书（该园主管机关为其沿革的强权威一手来源，UNESCO 覆盖园林代表身份而非年份），符合第54轮 renaissance-style「年份主要由强权威官方源直书、第二源覆盖实例结构」的既有判定，不构成实质单源缺陷。
- **七节其他内容**：`典型手法与适用条件`「选石、立意、堆叠，结合植物与水」与苏州市园林局 `经过叠石名家的精妙构思`、`石缝间长着古树和松柏` 相容；无具体数字/人名编造。
- **无编造**：核心定义、overview、狮子林实例四要素均由引用来源正文支撑；设计者缺载按「无单一设计师」处理，未凑数。
- **问题（轻微）**：① 年份 1342 主要由苏州市园林局单源直书（UNESCO 未给年份），底稿已明确分工且园林主管机关为一手强权威，不影响判定；② UNESCO 本轮 403 反爬，保留同日 200 回执，`link_ok=null` 已标；③ 概念源 `wp-chinese-garden`/`wp-garden-design` 为百科，按项目既定口径作背景（实例以官方源为证），可接受；④ 原理「瘦、透、漏、皱」与来源「适、漏、瘦、皱」字面略有出入，属同一品石标准的通行表述，无实质错误。
- **内容判定：合格**。`needs_verification=false`、pending 空、待核实「暂无已知待核实项。」与双源实况一致（设计者处理已在实例正文如实标注，非隐瞒）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：11 个来源 id 全部存在、`verified=true`；`year=null`（D06 允许）；新登记 6 源 `link_ok=null`（三态未标）；无 `link_ok=false`（healthcheck-round55 列出的 6 条 false 源均不在本批）。无假 id。
- **可达性（本轮实抓）**：10/11 去重 URL 本轮 HTTP 200（Louvre、PCF、Moesgaard、Henning、苏州市园林局经 curl、wp-atrium-architecture、wp-sunken-courtyard、wp-architecture、wp-chinese-garden、wp-garden-design）；UNESCO 813 本轮 403 反爬，`review-round55b.md` 同日 200 且关键句逐字回执，按反爬而非死链处理。`web_fetch` 对部分站点受前端跳转影响（苏州市园林局页），按 D05 改 urllib/curl，不影响证据效力。
- **相关性结论**：
  - `sunken-atrium`：Louvre + PCF 双源直证卢浮宫地下大厅实例四要素与采光/三翼；两 Wikipedia 作概念背景。
  - `earth-sheltered`：Moesgaard + Henning 双源直证实实例四要素与地形嵌入；**但两条 Wikipedia 概念源与「土体保温隔热」定义不直接对应，definition/overview 热工主张四源均无支撑**。
  - `rockery`：苏州市园林局 + UNESCO 双源直证狮子林湖石假山实例；两 Wikipedia 作叠石概念背景。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sunken-atrium | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| earth-sheltered | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| rockery | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械项三条全部通过。**

- **SVG 质量观察**：
  - `sunken-atrium` / `rockery`：复用简洁剖面/石景轮廓模板，标「地下中庭」「叠石」，主题贴合；无具体尺寸标注（本批无尺寸数据，可接受）。
  - `earth-sheltered`：坡地草皮 + 采光井意象，标「覆土建筑」，主题贴合；但 `<ellipse ry=333>` 潜在纵向出界（见 3.2 轻微项），且延续第44–54轮观察——图示缺显式「设计意图/尺寸关系」文字标注，`check.py` 查不出该语义项，属系统性次要问题。
  - **判定**：机械项与主题贴合均过；建议全站统一补「设计意图或尺寸关系」标注（延续第44–54轮方向）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对全部 True）；`source_count` 与来源数组长度一致（4=4、4=4、4=4）；`needs_verification_count`：三条均=0。
- `git diff` 显示本轮共 **8 条** `needs_verification_count` 由 1→0，对应 8 条补具名实例条目批量清零，`pending_sum` 由 203→195（-8，3.94%）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| sunken-atrium | false（本轮清零） | "" | 「暂无已知待核实项。」 | **结构一致 ✓、内容恰当 ✓**：定义/overview/卢浮宫四要素双源支撑。 |
| earth-sheltered | **false（本轮清零）** | "" | 「暂无已知待核实项。」 | **结构同向但内容失真 ✗**：实例四要素双源扎实，但 definition/overview 热工主张四源无支撑、原理逐字重复，未披露。应补源/改写后再清零，或恢复 true 并据实写 pending/待核实。 |
| rockery | false（本轮清零） | "" | 「暂无已知待核实项。」 | **结构一致 ✓、内容基本恰当 ✓**：定义/overview/狮子林四要素双源；年份强权威官方源直书；轻微建议注明年份单源与 UNESCO 反爬回执。 |

> **异常监控（§E）**：全库 `pending_sum` 由第54轮 203 降至本轮 **195**（-8，3.94%）。存量待核实占比 195/258≈75.6%，处历史高位，**不触发「待核实占比异常低（疑似硬写）」降级**；降幅来自本轮一次性补 8 条具名实例后的批量清零，属本轮工作直接结果；但 `earth-sheltered` 在 definition/overview 仍有热工主张无源的情况下清零，属个例误清，建议定向回退而非整批处理。

## 七、任务 5：相似度（difflib 去空白+小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| sunken-atrium | **0.3676** vs atrium-ventilation | <0.54 ✓ | **0.4478** vs visitor-route | <0.54 ✓ |
| earth-sheltered | **0.4286** vs organic-architecture | <0.54 ✓ | **0.3930** vs minimalism-architecture | <0.54 ✓ |
| rockery | **0.3725** vs cunfa | <0.54 ✓ | **0.4246** vs seasonal-scenery | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。最高为 sunken-atrium 全字段 0.4478（vs visitor-route，同用卢浮宫金字塔实例，正常近邻，非套话）。

### 7.2 第55轮批内 3 条两两（全字段② / 短文本①）

- sunken-atrium vs earth-sheltered：全字段 **0.3625**、短文本 0.2963。
- sunken-atrium vs rockery：全字段 **0.3428**、短文本 0.1587。
- earth-sheltered vs rockery：全字段 **0.3507**、短文本 0.1913。
- → 批内两两均远低于 0.54，无套话/模板姊妹风险。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–54轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **sunken-atrium（地下中庭）** | definition/overview 由 Louvre + PCF 直证；卢浮宫四要素 Louvre 官方直书、PCF 佐证；无编造 | 4/4 true；实例源直接相关且本轮 200；概念源背景 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」 | 全部一致；nv=false↔pending 空↔「暂无」恰当 | 全库 ✓（0.3676/0.4478）；批内 ✓ | **合格** |
| **earth-sheltered（覆土建筑）** | 实例四要素由 Moesgaard + Henning 双源直证；**但 definition「土体保温隔热」/overview「土壤蓄热使室内温度平稳」四源正文均无支撑，原理逐字重复 definition+overview** | 4/4 true；实例源直接相关且本轮 200；两条 Wikipedia 概念源与热工定义不直接对应 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」，但 `<ellipse ry=333>` 潜在出界（次要） | 元数据一致；**nv=false 清零属个例误清**，热工主张无源未披露 | 全库 ✓（0.4286/0.3930）；批内 ✓ | **待核实** |
| **rockery（叠石）** | definition/overview 由 wp-garden-design/wp-chinese-garden + 苏州市园林局直证；狮子林名称/地点/1342 由苏州市园林局直证、UNESCO 佐证，设计者「无单一设计师」如实标注；无编造 | 4/4 true；实例源直接相关（园林局本轮 200、UNESCO 403 反爬+同日 200 回执）；概念源背景 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」 | 全部一致；nv=false↔pending 空↔「暂无」基本恰当；轻微建议注明年份单源+反爬回执 | 全库 ✓（0.3725/0.4246）；批内 ✓ | **合格** |

### 问题清单

- **① earth-sheltered definition/overview 热工主张无来源正文支撑（重点·判待核实主因）**：`wp-architecture` 无 thermal mass/earth shelter（唯一 insulat 命中在无关的斯瓦希里海岸屋顶语境），`wp-sunken-courtyard`/`moesgaard-building`/`henning-moesgaard` 的 thermal/insulat/temperature 全 MISS。建议补一独立权威源直证覆土建筑土壤蓄热/保温机制，或改写为有源表述；无法补齐则恢复 `needs_verification=true`。
- **② earth-sheltered 原理逐字重复 definition+overview（次要·套话）**：`原理` 未提供独立机制说明，建议在补源/改写定义时一并重写。
- **③ earth-sheltered pending 联动失真（重点·须定向回退）**：`needs_verification=false`、pending 空、待核实「暂无」；问题①②使 definition/overview 层面仍有未披露的无源主张。应补源/改写后再清零，或恢复 true 并据实写 pending/待核实，若恢复 true 同步 `coverage.json` 计数。
- **④ earth-sheltered SVG 潜在出界（次要·脚本盲区）**：`<ellipse cx=327 cy=269 rx=37 ry=333>` 纵向约 -64~602 超 `viewBox 0 0 760 400`；`check.py` 不校验 rx/ry，建议手工收小 ry 或改绘。
- **⑤ earth-sheltered 概念源关联弱（轻微）**：`wp-architecture`/`wp-sunken-courtyard` 与覆土热工定义不直接对应，建议注明概念背景或替换为直接相关的覆土热工权威源；`time_or_place`「20世纪」与实例 2009–2014 不完全对应。
- **⑥ sunken-atrium 同实例跨条目复用（轻微）**：与 `visitor-route` 共用卢浮宫金字塔（全字段 0.4478），建议保持两条目侧重点区分；年份单源由 Louvre 官方直书（底稿分工已明确），`link_ok=null` 已标。
- **⑦ rockery 年份单源与反爬回执（轻微）**：1342 由苏州市园林局直书（强权威一手源），UNESCO 覆盖园林代表身份；保留 UNESCO 同日 200 回执，`link_ok=null` 已标。
- **⑧ 全站系统性次要项**：部分 SVG 缺显式「设计意图/尺寸关系」标注，`check.py` 查不出该语义项，建议全站统一补强（延续第44–54轮方向）。

## 九、总体结论与建议

- **抽样结果**：第55轮补具名实例条目中抽检 3 条——`sunken-atrium`、`earth-sheltered`、`rockery`。**内容维度：2 合格（sunken-atrium、rockery）＋1 待核实（earth-sheltered）＋0 不合格；实例层面 0 编造、0 假 id、0 死链证据。**
- **来源层面**：11 个引用来源 id 全部存在、`verified=true`；10/11 去重 URL 本轮 HTTP 200，UNESCO 403 反爬但同日底稿有 200 与逐字关键句。三条的实例四要素均获双源直证；`sunken-atrium`、`rockery` 的定义/overview 获官方源直接支撑，`earth-sheltered` 的定义/overview 热工主张是唯一实质无源点。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 唯一性与 theme 贴合基本通过（earth-sheltered 有一处潜在出界）、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：sunken-atrium、rockery 清零恰当；earth-sheltered nv 清零属个例误清——definition/overview 热工主张无源未披露。全库 pending_sum 203→195（-8，3.94%），存量占比 75.6% 处高位，不触发「占比异常低」降级。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4286、全字段最高 0.4478）；方法自校 0.5157 与第39–54轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（2 合格 + 1 待核实），0 实例编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——存量待核实占比 75.6% 处高位，降幅来自本轮批量补实例，非整批硬写；但 earth-sheltered 单条 nv 误清须修正。
  4. **结论：本轮 2 条合格、1 条待核实，不触发整批返工/降级。** 第55轮补源对 sunken-atrium、rockery 成效显著；earth-sheltered 须定向修复 definition/overview 无源热工主张与联动，而非全批回滚。
- **返工/修复建议（定向、非整批）**：
  1. **（优先·问题①③）`earth-sheltered`**：补一独立权威源直证覆土建筑「土壤蓄热/保温隔热」机制，或把 definition/overview 改写为有源表述（如「部分或全部覆土、草皮屋顶嵌入地形、展厅位于其下并由采光井补光」）；若无法补齐则恢复 `needs_verification=true` 并据实写 pending/待核实，同步 `coverage.json` 计数。
  2. **（问题②）`earth-sheltered` 原理**：随定义改写重写「原理」，消除 definition+overview 逐字重复。
  3. **（问题④）`earth-sheltered` SVG**：收小 `<ellipse ry=333>` 或改绘，消除潜在纵向出界。
  4. **（问题⑤）`earth-sheltered` 概念源**：注明两条 Wikipedia 为概念背景，或替换为直接相关的覆土热工权威源。
  5. **（问题⑥）`sunken-atrium`**：保持合格；建议与 `visitor-route` 明确侧重区分，来源 note 补记年份单源由 Louvre 官方直书。
  6. **（问题⑦）`rockery`**：保持合格；来源 note 补记 1342 由园林主管机关单源直书与 UNESCO 同日 200 回执。
  7. **（问题⑧，系统性）**：全站统一补「设计意图或尺寸关系」文字标注。

### 机器可读汇总

```
ROUND=55
SAMPLER=spotcheck-r55
MODE=第55轮补具名实例条目中lead定向抽3条（sunken-atrium / earth-sheltered / rockery）
SCOPE=["sunken-atrium","earth-sheltered","rockery"]
FILES={"sunken-atrium":"entries/batch-35.json","earth-sheltered":"entries/batch-38.json","rockery":"entries/batch-35.json"}
GIT_HEAD="66c001d"; ROUND55_COMMITTED=false; GIT_STATUS="round55 changes UNCOMMITTED as found (M coverage/data/sources/entries/batch-35/36/38 + site/*; ?? healthcheck-round55.md, review-round55a/55b.md, apply_review_round55.py - lead notes, untouched)"
STATE={"sources.json":"205599B","coverage.json":"total=258","batch-35.json":"23685B","batch-38.json":"64106B","pending_sum":195,"sources_total":430,"sources_verified_true":427,"sources_verified_false":3}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements (grep 0 hits)"
SAMPLE_RATIO="3/8 (37.5%, lead 定向抽检)"
FETCH_METHOD="web_fetch succeeded for Louvre/PCF/Moesgaard/Henning/Wikipedia; suzhou-gov via curl 200(43887B); UNESCO 403 anti-bot with same-day review-round55b HTTP200 verbatim quotes; 10/11 distinct URLs HTTP200 this round; norm()/lower() readback; in-memory; only this report written"
SOURCES={"count_distinct_ids":11,"count_distinct_urls":11,"count_refs":12,"all_exist":true,"all_verified_true":true,"link_ok_false":0,"link_ok_null_new":6}
BODY_SUPPORT={
 "sunken-atrium":"definition/overview Louvre('central underground lobby ... three wings'/'most transparent, light and luminous'/'visitor circulation')+PCF('areas within and below the existing museum'/'underground links to museum wings'); Louvre Pyramid/Hall Napoleon four facts Louvre official('Ieoh Ming Pei'/'inaugurated on 29 March 1989'/'Cour Napoléon')+PCF(project archive); VERDICT=合格 (minor: time 20C general, shared Louvre instance with visitor-route)",
 "earth-sheltered":"instance Moesgaard Museum four facts Moesgaard official('opened in 2014'/'designed by Henning Larsen Architects'/Højbjerg)+Henning Larsen('Aarhus, Denmark'/'2009 - 2014'/'southern Aarhus'/'grass and moss'/'natural light into exhibition spaces below'); BUT definition '土体保温隔热' & overview '土壤蓄热使室内温度平稳' UNSUPPORTED in all 4 cited sources (wp-architecture insulat hit=Swahili coast; others thermal/temperature MISS), 原理 verbatim duplicates definition+overview; VERDICT=待核实",
 "rockery":"definition/overview wp-garden-design('rock garden, also known as rockery')+wp-chinese-garden('artificial mountains and rock gardens'/'taihu')+suzhou gov('太湖石堆叠的假山...洞壑盘旋'); Lion Grove name/place/1342 suzhou gov('园林路23号'/'国内尚存最大的古代假山群'/'元至正二年(1342)...天如禅师')+UNESCO 813('the Lion Grove Garden'/'rock formations'), designer '无单一设计师' per brief; VERDICT=合格 (minor: year mainly single-source suzhou gov; UNESCO 403 anti-bot same-day 200)"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3, 无on*/无外链图, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_issue":"earth-sheltered ellipse ry=333 potential vertical overflow (check.py checks cx/cy/r only, not rx/ry - script blind spot)"}
METADATA={"field_match_coverage":"ALL True x3","source_count":"4=4 x3","nvc":"all 0; git diff coverage: 8 entries 1->0, pending_sum 203->195 (-8, 3.94%), stock pending ratio 195/258=75.6% (high, not anomalous-low)","needs_verification":"sunken=false proper; rockery=false proper; earth-sheltered=false mis-clear requires targeted fix","related":"no dangling in sampled"}
SIMILARITY={
 "sunken-atrium":{"vs_all_short":0.3676,"short_entry":"atrium-ventilation","vs_all_full":0.4478,"full_entry":"visitor-route","verdict":"PASS<0.54"},
 "earth-sheltered":{"vs_all_short":0.4286,"short_entry":"organic-architecture","vs_all_full":0.3930,"full_entry":"minimalism-architecture","verdict":"PASS<0.54"},
 "rockery":{"vs_all_short":0.3725,"short_entry":"cunfa","vs_all_full":0.4246,"full_entry":"seasonal-scenery","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.3625,"intrabatch_full_max_pair":"sunken-atrium vs earth-sheltered",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-54 -> method validated (raw dict order)",
 "threshold":0.54}
VERDICT_CONTENT={"sunken-atrium":"合格","earth-sheltered":"待核实","rockery":"合格"}
VERDICT_PENDING={"sunken-atrium":"consistent/proper","earth-sheltered":"distorted (nv mis-clear; definition/overview thermal claim unsourced, rewrite with source or restore true)","rockery":"consistent/proper (minor: year single-source + UNESCO anti-bot quote)"}
HARD_FABRICATION_INSTANCE=0
UNSOURCED_CLAIM=1
FAKE_ID=0
LINK_FAIL=0
ANOMALY_NVC="pending_sum 203->195 (-8, 3.94%); stock ratio 75.6% high -> no anomalous-low downgrade; batch of 8 named-instance clears this round; earth-sheltered single-entry nv mis-clear requires targeted fix"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (2合格+1待核实), 0 instance fabrication/0 fake id/0 dead link; similarity all <0.54; pending stock high. Targeted fixes: (1) earth-sheltered source or rewrite thermal definition/overview + restore nv=true if unfixed; (2) rewrite verbatim 原理; (3) fix ellipse ry=333 overflow; (4) mark 2 Wikipedia as background; (5) sunken-atrium differentiate from visitor-route; (6) rockery note year single-source + UNESCO 200 quote; (7) add design-intent/dimension annotations site-wide."
READONLY="only wrote research/spotcheck-round55.md; no other project content file changed; no git commit; round55 work remains uncommitted as found; web content treated as data, no instruction executed; temp fetch file removed; no files written outside deliverable"
```

*（报告完）*
