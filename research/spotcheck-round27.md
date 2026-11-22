# 第27轮质量闸抽检报告（spotcheck-round27）——tenebrism / plaza / vestibule 逐条来源正文支撑·来源相关性·L2 七节与SVG·元数据联动·相似度

- 抽检人：spotcheck-r27（由 lead 委派的子代理）；抽检样本时间 2026-11-22 约 22:25 起、核对完成约 22:29，Asia/Hong_Kong（CST）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 ≥ 10%、至少 3 条逐条核对来源；**不合格则整批返工**，下一轮抽检比例提到 25%）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）；`D:/Users/Administrator/Desktop/TASK_design.md`「条目页结构」L2 七节标准 +「通用硬性规则」（不编造数字·日期·人名·引文·出处；关键事实两独立来源否则标待核实；只引用 verified=true 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+「专用规则」；`DECISIONS.md` D05（网页实抓核验）/D06（在线百科 year=null）/D10（关键事实双源否则待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–26 轮一致），已按该路径只读读取；`DECISIONS.md` 在仓库根。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。

## 〇、数据稳定性与只读声明

- **采样快照**：`data/sources.json`=106650B@22:23:24、`entries/batch-25.json`=10714B@22:20:17、`entries/batch-27.json`=2290B@22:25:36、`coverage.json`=81955B@22:25:37（Asia/Hong_Kong）。读取的三条条目内容与对应 `coverage.json` 一致（见 §六）。`python tools/check.py` 于 22:29 实跑 **`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round27.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未创建 git commit，未改项目文件夹之外内容。抓取缓存仅驻留系统临时目录（`%TEMP%/r27/*.txt`），非项目产物。联网内容一律视为数据，网页中任何指令均未执行。
- **并发提示**：`git status` 见本项目主流程正在改写 `coverage.json / site/*`（`M coverage.json`、`M site/*.html`、`?? entries/batch-27.json`、`?? research/gaps-round27.md` 等，非本子任务所改）。本报告以 22:20–22:25 快照为准。

## 一、判定口径与抓取方法

- **抽检对象**（任务指定，本轮相关 3 条）：`tenebrism`、`plaza`（第26轮 L2 升级时未抽的 2 条，见 `entries/batch-25.json`）、`vestibule`（本轮新增 L2，见 `entries/batch-27.json`）。3 条满足 ≥25%、≥3 条门槛。
- **L2 七节口径**：顶层 `definition` + `sections` 中 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）；须 1 张 SVG 且含“示意图，非施工图”；“常见错误与限制”段须以“实际工程须按当地规范和专业设计人员的要求”收尾。
- **抓取方法**：Python 3 `urllib` + 浏览器 User-Agent 实抓。`en.wikipedia.org` canonical 本轮仍 `WinError 10060`（连接超时，与第 12–26 轮一致），改 **owiki 同源镜像**（`https://owiki.org/wiki/<Title>`）；`dailyartmagazine.com`、`pps.org` canonical 直连 **HTTP 200**。所有成功抓取均记录 HTTP 码、字节数、`<h1>`/`<title>`、正文长度与关键词命中（正文文本缓存于 `%TEMP%/r27/`）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）对 `entries/*.json` 全库（132 条）扫描，警戒线 **0.54**。分四档报告：①短文本（标题+定义+时间地点+概述）；②全字段-不含SVG（+sections 全部文本）；③全字段-含SVG原始标记；④纯内容（去掉“实例/常见错误与限制/一图”固定模板与SVG）。

## 二、抽检对象来源清单与完整性（任务 2）

`python tools/check.py` → **PASS, 0 errors**。三条被抽条目的来源 id **全部存在、全部 verified=true**；但**相关性核查发现 `wp-loggia` 与「门厅」主题不相关**（详见 §四与 §三.3）：

| 条目 | 来源 id | 存在/verified | 标题（来源库） | type | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| tenebrism | wp-tenebrism | ✅ / true | Tenebrism | 权威百科 | 直接（暗绘风格专条） |
| tenebrism | dailyart-tenebrism | ✅ / true | Tenebrism 101 — DailyArt Magazine | 学术著作（实为大众艺术杂志） | 直接（暗绘风格专文） |
| plaza | wp-town-square | ✅ / true | Town square (Plaza) | 权威百科 | 直接（城市广场专条） |
| plaza | pps-successful-place | ✅ / true | What Makes a Successful Place? — PPS | 官方机构 | 直接（优秀公共空间四要素） |
| vestibule | wp-vestibule-architecture | ✅ / true | Vestibule (architecture) | 权威百科 | 直接（门厅专条） |
| vestibule | wp-loggia | ✅ / true | Loggia | 权威百科 | **不相关**（敞廊/凉廊，室外开敞廊道，与室内门厅无关） |

> 结论：六条来源 id 全部存在、verified=true。但 `vestibule` 的第二来源 `wp-loggia`（Loggia＝有顶的**室外**开敞廊道/画廊）与「门厅」（入口处**室内**小房间、挡风减热损失）分属相反的空间类型，**标题与主题不直接相关**，且正文对门厅零支撑（互文命中均为 0，见 §三.3、§四）。此为该条**来源相关性硬伤**。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节（实抓逐句比对）

### 3.1 tenebrism（暗绘风格/暗色调主义）——**合格**
- **wp-tenebrism**（canonical 超时 → owiki 镜像 HTTP200 14145B，h1「Tenebrism」，正文 4263c；tenebrism=6/chiaroscuro=2/dark=3/spotlight=1/dramatic=3/Caravaggio=3/17th=2/century=2/contrast=2）：原文 “Tenebrism … is a style of painting using especially pronounced chiaroscuro, where there are **violent contrasts of light and dark, and where darkness becomes a dominating feature of the image**.”；“The technique was developed to add drama to an image through a **spotlight effect**”；“Tenebrism is used only to obtain a **dramatic impact** while chiaroscuro is a broader term”；“applied to other **17th-century** painters”。
- **dailyart-tenebrism**（canonical HTTP200 128696B，h1「Tenebrism 101: All You Need to Know」，正文 10344c；tenebrism=16/Caravaggio=17/chiaroscuro=4/dramatic=3/17th=2/century=3/religious=2）：原文 “The word tenebrism comes from the Italian word **tenebroso which means dark or gloomy**”；“the Baroque movement, which characterizes much of the **European art of the 17th century**, is known for its **dramatic flair**”；“religious art / Religious Painting”。
- 逐项：definition「把背景压到极暗、以强烈聚光突出主体的绘画风格」✓（darkness dominating + spotlight + violent contrasts 逐字）；time_or_place「17世纪、欧洲」✓（17th-century + European art of the 17th century）；overview「明暗法的极端化，营造神秘与戏剧张力」✓（“only to obtain dramatic impact while chiaroscuro is a broader term”＋“add drama”＋“tenebroso=gloomy”）；原理✓；典型手法「大面积深色配集中高光；适用于宗教画与戏剧性题材」✓（violent contrasts + religious + dramatic）。
- **实例**：“名称：暗色调绘画（类型性描述）；地点：欧洲；设计者：不适用；年份：不适用”——**类型性描述，无杜撰具体作品/人名/年份** ✓。
- 未发现编造年份/人名/引文。
- **Minor**：①概述“**神秘**”一词为宽泛引申（源自 tenebroso=dark/gloomy），非源文直述，属可接受的意译；②`dailyart-tenebrism` 的 `type` 记为“学术著作”，实为大众艺术杂志（DailyArt Magazine），`author` 记为“Wikipedia/机构”属模板占位，均为元数据瑕疵，不影响正文支撑。

### 3.2 plaza（广场/城市广场）——**合格**
- **wp-town-square**（canonical `en.wikipedia.org/wiki/Plaza` 超时 WinError10060；owiki `/wiki/Plaza` 仅 1662c **残桩/榜单页**（无正文）；owiki `/wiki/Town_square` HTTP200 28841B，h1「Town square」，正文 13971c → 与来源标题“Town square (Plaza)”一致的正文专条）：原文 “A town square, also called a **plaza** or piazza, is an **open public space** commonly found in the heart of a traditional town or city, and which is **used for community gatherings**.”；“Most squares are **hardscapes** suitable for open markets, concerts, political rallies, and other events that **require firm ground**.”（hit: public=18/open space=3/hard=2/market=8/gather=1/civic=1）
- **pps-successful-place**（canonical HTTP200 41561B，h1「What Makes a Successful Place?」，正文 9781c）：原文 “to be successful, they generally share the following **four qualities: they are accessible; people are engaged in activities there; the space is comfortable and has a good image; and finally, it is a sociable place: one where people meet each other**…”（hit: access=7/activities=8/comfort=6/sociability=2/social=4/community=4/public space=9）
- 逐项：definition「城市中向公众开放、供聚会与活动的硬质开敞空间」✓（open public space + community gatherings + hardscapes/firm ground；双源互补）；time_or_place「跨时期、全球」✓（traditional town or city / around the world）；overview「兼具通行、停留与交往功能，是城市公共生活的重要场所」✓（accessible 通行 + activities 停留活动 + sociable 交往 + community gatherings）；原理✓；典型手法「以可达性、活动、舒适与社交四要素组织」✓✓（pps 原文四要素逐字对应）。
- **实例**：“名称：城市中心广场（类型性描述）；地点/设计者/年份：不适用”——**类型性描述，无杜撰** ✓。
- **Minor（抓取提示，非缺陷）**：`sources.json` 的 url 指向 `en.wikipedia.org/wiki/Plaza`，owiki 镜像 `/wiki/Plaza` 为残桩；正文支撑实际来自同概念的 `/wiki/Town_square` 专条（h1 与来源标题“Town square (Plaza)”一致）。来源真实、正文支撑成立，仅镜像路由需注意。

### 3.3 vestibule（门厅）——**不合格（来源相关性 + 无源表述）**
- **wp-vestibule-architecture**（owiki 镜像 HTTP200 21297B，h1「Vestibule (architecture)」，正文 10213c；vestibule=48/entrance=12/wind=1/heat=1/security=3/waiting=2/lobby=2）：原文 “A vestibule is a **small room leading into a larger space** such as a lobby, entrance hall, or passage, for the purpose of **waiting**, withholding the larger space from view, **reducing heat loss**, providing storage space for outdoor clothing…”；“By creating an **air lock entry, vestibules reduce infiltration losses or gains caused by wind**”；“The vestibule … also **added security** to discourage unwanted entrance…”。→ 强支撑 definition「进入较大空间前的小型过渡房间，缓冲室内外」、overview「挡风、减少热损失」、原理、以及“安检(security)”。
- **wp-loggia（第二来源）——主题不相关**（owiki 镜像 HTTP200 14777B，h1「Loggia」，正文 4621c）：原文 “a **loggia is a covered exterior gallery or corridor**, often on an upper level… The corridor is **open to the elements** because its outer wall is only partial…”。关键词：vestibule=0/anteroom=0/hall=0/transition=0/corridor=2/arcade=3/open=6。**门厅页与 Loggia 页互文命中均为 0**（vestibule 提到 loggia=0；loggia 提到 vestibule=0）。Loggia 为**室外开敞**廊道，与门厅**室内封闭缓冲**的空间类型相反，**不能支撑门厅任何定义/原理/手法**。
- 逐项核查存在的无源表述（以 wp-vestibule 正文为准）：
  - definition「承接**换乘**与等候」：**等待(waiting)✓**，但“**换乘**”（transfer）源文 **transfer=0**，无据；term 疑似“换鞋/换装”笔误（storage of outdoor clothing 仅部分支撑换装）。
  - overview「作为**安检、礼仪与人流组织**的过渡节点」：“安检(security)”✓（security=3），但“**礼仪**”源文 **ceremon/ritual=0**；“**人流组织/分流**”源文 **circulat=0/crowd=0/traffic=0**（flow 仅 1 次）——均**无源**。
  - 典型手法「组织换鞋、安检、**等候与人流分流**」「楼梯连廊」——人流/分流部分同样无源。
- 逐项：definition 主体（小型过渡房间、缓冲室内外、等候、减热损失）✓；time_or_place「跨时期、全球」✓（modern and classical architecture）；overview“挡风减热损失”✓、但“礼仪/人流组织”✗无源；原理✓；典型手法部分✗。
- **实例**：“名称：公共建筑门厅（类型性描述）；地点/设计者/年份：不适用”——**类型性描述，无杜撰** ✓。
- **问题定性（不合格）**：①`wp-loggia` 与“门厅”**标题不直接相关**（违反任务 2 硬标准）、正文零支撑，导致关键事实**并非双源**（实际仅 wp-vestibule 单源有效）；②definition/overview/典型手法含“换乘、礼仪、人流组织/分流”等**无源表述**；③上述实质缺口**未在 `待核实` 节或 `pending_notes` 披露**（二者只写“具体实例的设计者与年代”）。修正方向：以真正相关的第二来源（如建筑词典 entry hall / lobby / airlock / wind-lobby 专条）替换 `wp-loggia`，删/改无源词，并如实披露缺口。

## 四、任务 2：来源 id 存在性、verified、标题相关性

- 六条来源：**全部存在、全部 verified=true**（见 §二表）。
- **相关性**：`wp-tenebrism`、`dailyart-tenebrism`、`wp-town-square`、`pps-successful-place`、`wp-vestibule-architecture` 五条标题与主题**直接相关**；**`wp-loggia` 与「门厅」不相关（不合格）**——Loggia 为室外开敞廊道，与室内门厅分属相反空间类型，且两页互文 0。
- **可达性**：`dailyartmagazine.com`、`pps.org` canonical HTTP200；`wp-tenebrism`、`wp-vestibule-architecture`、`wp-loggia`、`wp-town-square`(→Town_square) 经 owiki 同源镜像 HTTP200 实抓核对 h1；`en.wikipedia.org` canonical 超时（WinError 10060，与历史一致）。
- **`link_ok` 与 `verified` 语义分离（D11）**：`dailyart-tenebrism`/`wp-town-square`/`pps-successful-place` 的 `link_ok=null`（canonical 未直连或镜像路由不同），`wp-tenebrism`/`wp-vestibule-architecture`/`wp-loggia` 为 `true`；`verified` 独立表示标题/机构已核对，不受影响。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节 | SVG 数 | 含“示意图，非施工图” | SVG 元素出界 | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tenebrism | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无（viewBox 0 0 760 400，逐属性核验） | ✓“实际工程须按当地规范和专业设计人员的要求” |
| plaza | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无 | ✓ |
| vestibule | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 全部齐备）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含“示意图，非施工图”；逐属性（cx/cy/x/y/x1..y2/points/width/height/rx/ry/r）核验**无出界**；“常见错误与限制”段均以规范提示收尾。**该项三条全部通过。**

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- `entries/batch-25.json`（tenebrism、plaza）与 `entries/batch-27.json`（vestibule）对 `coverage.json` 逐字段比对：`title/theme/tier/period/region/level` **全部一致**；`source_count`＝来源数组长度（均 2）**一致**；`needs_verification=true` ↔ `coverage.needs_verification_count=1` ↔ `pending_notes` 非空 **形式一致**。

| 条目 | needs_verification | pending_notes（结构化） | 正文 `待核实` 节 | 一致性 |
| --- | --- | --- | --- | --- |
| tenebrism | true | 具体**实例**（名称/地点/设计者/年代）待补充独立来源 | 具体**作品与作者年代**待核实 | **一致**（同指具体例证/年代）✓ |
| plaza | true | 具体**实例**（名称/地点/设计者/年代）待补充独立来源 | 具体**广场的设计者与年代**待核实 | **一致**✓ |
| vestibule | true | 具体**实例**（名称/地点/设计者/年代）待补充独立来源 | 具体**建筑门厅的设计者与年代**待核实 | 形式一致，**但实质缺口未披露**：真正的缺陷（`wp-loggia` 不相关、“换乘/礼仪/人流组织”无源）未写入 pending/待核实 ✗(部分) |

> 结论：`needs_verification` 状态与计数形式三条全部合规（nv=true、nvc=1、pending 非空），title/theme/tier/period/region/level/source_count 逐项一致。但 `vestibule` **形式联动、实质未披露**——其来源相关性硬伤与无源表述未在结构化字段如实表达（D14 实质联动缺口，性质同第 25/26 轮“形式一致、实质未披露”）。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54，全库 132 条）

| 条目 | ①短文本(标题+定义+时间+概述) | ②全字段-不含SVG | ③全字段-含SVG标记 | ④纯内容(去模板句+SVG) |
| --- | --- | --- | --- | --- |
| tenebrism | **0.3836** vs chiaroscuro | **0.4278** vs rembrandt | 0.6372 vs color-contrast ⚠ | 0.3583 vs chiaroscuro |
| plaza | **0.3582** vs atrium-architecture | **0.4453** vs pedestrian-flow | 0.6128 vs hardscape-softscape ⚠ | 0.3136 vs color-theory |
| vestibule | **0.3165** vs saturation | **0.4199** vs transition-space | 0.6166 vs saturation ⚠ | 0.2994 vs transition-space |

- **短文本（①）全部 <0.54**（0.3165–0.3836）；**全字段-不含SVG（②）全部 <0.54**（0.4199–0.4453）；**纯内容（④）全部 <0.54**（0.2994–0.3583）。
- **仅“全字段-含SVG原始标记”（③）三条均 ≥0.54**（0.6128–0.6372）。该越线**由结构模板与 SVG 标记（viewBox/rect/text/var(--…)/统一水印“示意图，非施工图”）驱动，而非实质内容套话**——④去掉模板与 SVG 后仅 0.30–0.36。**不构成“内容套话”降级依据**；但如实记录：若机械以③口径套 0.54，则三条均越线，建议相似度门槛采用②或④（内容层）。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview 来源支撑 | 来源存在·verified·**相关** | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①/②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **tenebrism（暗绘风格）** | 定义✓（darkness dominating+spotlight+violent contrasts）；时间✓（17th c. Europe）；概述✓（extreme chiaroscuro+dramatic+tenebroso）；原理/手法✓ | 2/2 true，均相关（专条+专文，互补非伞源） | 七节齐、SVG✓、风险✓ | 全部一致；nv/pending/待核实一致 ✓ | 0.384/0.428 | **合格**（minor：dailyart type误记学术著作、author 占位） |
| **plaza（广场）** | 定义✓（open public space+community gatherings+hardscapes，双源）；时间✓（跨时期/全球）；概述✓（accessible/activities/comfort/sociable 四要素）；手法✓ | 2/2 true，均相关（Town square 专条 + PPS 四要素） | 七节齐、SVG✓、风险✓ | 全部一致；nv/pending/待核实一致 ✓ | 0.358/0.445 | **合格**（minor：镜像 /wiki/Plaza 为残桩，实际支撑取自 Town_square 专条） |
| **vestibule（门厅）** | 定义主体✓（small room+waiting+reducing heat loss）、挡风减热✓；**“换乘/礼仪/人流组织”无源✗** | **1 直接相关 + 1 不相关（wp-loggia）**；实际单源有效 | 七节齐、SVG✓、风险✓ | 形式一致；**实质缺口未披露** | 0.317/0.420 | **不合格**：第二来源 wp-loggia 主题不相关、零支撑；overview/手法含无源表述；缺口未披露 |

- **合格 2 条**：`tenebrism`、`plaza`。
- **不合格 1 条**：`vestibule`（来源相关性硬伤 + 无源表述）。
- **硬性“编造”0 条**：三条 `实例` 均为“类型性描述 + 地点/设计者/年份 不适用”，未发现编造人名、引文、出处或具体年份。

## 九、总体结论与是否整批返工

- **抽样结果**：3 条中 **2 合格（tenebrism、plaza）+ 1 不合格（vestibule）**；**硬性编造 0 条**（无杜撰人名/引文/具体年份/出处）。
- **来源层面**：六条来源 id 全部存在、verified=true；五条标题直接相关，**`wp-loggia` 与「门厅」不相关（唯一硬伤）**；`dailyartmagazine`/`pps` canonical HTTP200，wikis 经 owiki 同源镜像核对（en.wikipedia canonical 超时 WinError10060，与历史一致）。
- **结构层面**：三条 L2 七节完整、各 1 张 SVG 均含“示意图，非施工图”、元素无出界、风险/规范句齐备；`check.py` **PASS 0 errors**。
- **数据治理**：元数据（title/theme/tier/period/region/level/source_count）逐项一致；`needs_verification↔pending↔nvc` 形式一致，但 `vestibule` 来源硬伤与无源表述未披露（D14 实质联动缺口）。
- **相似度**：①短文本、②全字段-不含SVG、④纯内容**均 <0.54**（0.30–0.45）；**仅③“含SVG原始标记”口径越线 0.61–0.64，成因是结构模板与 SVG 标记，非内容套话**，不构成降级依据，已如实留痕。
- **是否建议整批返工**：**建议按 §E 触发返工，但返工范围限定为 `vestibule` 单条（即 batch-27 本轮新增批次）。** 依据：`vestibule` 触及任务 2「标题与主题直接相关」硬标准（`wp-loggia`＝室外敞廊，与室内门厅不相关、正文零支撑）及无源表述，属**不合格**；AUTONOMOUS §E 明文“不合格则整批返工”，故 batch-27（仅 vestibule 一条）须整批返工修正。`tenebrism`、`plaza`（batch-25 复检条目）已在第27轮抽检中对来源、七节、相似度全部合格，**无需返工**。
  - **定向修正清单（vestibule）**：①以真正相关的第二来源（建筑词典 entry hall / lobby / airlock / wind-lobby / vestibule 专条，verified=true）替换 `wp-loggia`，恢复“关键事实双源”；②删/改 definition“换乘”、overview/典型手法“礼仪、人流组织/分流”等无源表述，改为源文可支撑的“等候、挡风、减少热损失、储存外衣、安全屏障”等；③令 `pending_notes`/`待核实` 如实披露“换装/换乘及礼仪、人流组织为概括、具体实例年代待核”等实质缺口（D14）；④复跑 `check.py` 并复检。
  - **宽松口径备选**：若质量闸采用“核心定义有真实来源、无编造即不判硬不合格”的宽松口径，则 `vestibule` 可降级为“待核实/需修正”，仅需定向修正单条（不整批返工）。但严格按 §E 与任务 2 相关性硬标准，本报告以**不合格**处理并建议返工 `vestibule`。

---

### 机器可读汇总

```
ROUND=27
SAMPLER=spotcheck-r27
SCOPE=["tenebrism","plaza","vestibule"]   # tenebrism/plaza in batch-25 (round26 unsampled), vestibule new L2 in batch-27; 3条
FILES={"tenebrism":"entries/batch-25.json","plaza":"entries/batch-25.json","vestibule":"entries/batch-27.json"}
STATE={"sources.json":"106650B@22:23:24","batch-25.json":"10714B@22:20:17","batch-27.json":"2290B@22:25:36","coverage.json":"81955B@22:25:37"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0) @22:29"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia canonical WinError10060 TIMEOUT -> owiki.org mirror; dailyartmagazine/pps canonical HTTP200"
FETCH={
 "wp-tenebrism":"OWIKI 200 14145B h1='Tenebrism' 4263c; 'darkness becomes a dominating feature'; 'spotlight effect'; 'dramatic impact while chiaroscuro is broader'; '17th-century'",
 "dailyart-tenebrism":"CANONICAL 200 128696B h1='Tenebrism 101: All You Need to Know' 10344c; 'tenebroso=dark or gloomy'; 'European art of the 17th century dramatic flair'; religious=2",
 "wp-town-square":"canonical /wiki/Plaza TIMEOUT; owiki /wiki/Plaza=1662c STUB(no body); owiki /wiki/Town_square 200 28841B h1='Town square' 13971c; 'open public space...used for community gatherings'; 'hardscapes...require firm ground'; public=18/hard=2/market=8",
 "pps-successful-place":"CANONICAL 200 41561B h1='What Makes a Successful Place?' 9781c; 'four qualities: accessible; engaged in activities; comfortable and good image; sociable place where people meet'",
 "wp-vestibule-architecture":"OWIKI 200 21297B h1='Vestibule (architecture)' 10213c; 'small room leading into a larger space...for waiting...reducing heat loss'; 'air lock entry...reduce...wind'; 'added security'",
 "wp-loggia":"OWIKI 200 14777B h1='Loggia' 4621c; 'covered EXTERIOR gallery or corridor...open to the elements'; vestibule=0/anteroom=0/hall=0/transition=0; mutual mention 0/0"
}
BODY_SUPPORT={
 "tenebrism":"STRONG def+time(17c Europe)+overview(extreme chiaroscuro+drama)+原理+手法; 2 relevant src; MINOR dailyart type=学术著作(magazine), author placeholder",
 "plaza":"STRONG def(open public space+community gatherings+hardscapes, 2 src)+time(跨时期/全球)+overview(accessible/activities/comfort/sociable)+手法(PPS four qualities verbatim); support via Town_square article (Plaza mirror stub)",
 "vestibule":"def主体 OK(small room+waiting+reducing heat loss, wind, security) from wp-vestibule; 2nd src wp-loggia TOPICALLY IRRELEVANT(exterior open gallery; 0 support); UNSUPPORTED '换乘'(transfer=0)/'礼仪'(ceremon=0)/'人流组织'(circulat/crowd/traffic=0); gap undisclosed"
}
L2_CHECK={"seven_sections":"6/6 x3 + definition顶层","svg":"1 each, all '示意图，非施工图'","svg_bounds":"no overflow (760x400)","risk_note":"'实际工程须按当地规范和专业设计人员的要求' x3"}
SOURCE_RELEVANCE={"wp-tenebrism":"direct","dailyart-tenebrism":"direct","wp-town-square":"direct","pps-successful-place":"direct","wp-vestibule-architecture":"direct","wp-loggia":"NOT related to vestibule (loggia=exterior open gallery)"}
METADATA_CONSISTENCY={"batch vs coverage title/theme/tier/period/region/level":"ALL OK x3","source_count=2":"OK x3","needs_verification=true & nvc=1 & pending!=''":"formally OK x3; vestibule substantive gap (loggia mismatch + unsupported terms) UNDISCLOSED"}
SIMILARITY={
 "tenebrism":{"short":0.3836,"full_no_svg":0.4278,"full_with_svg":0.6372,"content_only":0.3583},
 "plaza":{"short":0.3582,"full_no_svg":0.4453,"full_with_svg":0.6128,"content_only":0.3136},
 "vestibule":{"short":0.3165,"full_no_svg":0.4199,"full_with_svg":0.6166,"content_only":0.2994},
 "threshold":0.54,
 "verdict":"short & full_no_svg & content_only ALL <0.54; only full_with_svg>=0.54 due to svg-markup+template (structural, not content)"
}
VERDICT={"tenebrism":"合格(minor: dailyart type/author元数据)","plaza":"合格(minor: /wiki/Plaza 镜像残桩，支撑取自Town_square)","vestibule":"不合格(wp-loggia主题不相关+零支撑; '换乘/礼仪/人流组织'无源; 缺口未披露)"}
HARD_FAIL=0
OVERALL="2合格(tenebrism,plaza)+1不合格(vestibule)+0编造; 6来源全存在&verified, 5相关/1不相关(wp-loggia); 七节/SVG/风险全过; check.py PASS; 相似度short&full_no_svg&content_only<0.54,仅含SVG/模板口径越线(结构非内容)"
BATCH_REWORK="建议按§E返工,范围限定vestibule单条(batch-27): 换相关第二来源替换wp-loggia+删/改'换乘/礼仪/人流组织'无源词+如实披露缺口; tenebrism/plaza合格无需返工"
```

*（报告完）*
