# 第25轮体检抽检报告（spotcheck-round25）——perspective / gothic / wayfinding / drainage 逐条来源正文支撑·来源完整性·结构联动·全库体检复检

- 抽检人：spotcheck-r25（由 lead 委派的子代理）；抽检时间：2026-11-22 约 21:29 起，Asia/Hong_Kong（会话时间取样；核对完成时点约 22:00）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 F「体检（每 5 轮做一次）」+ 第三节 E「质量闸」+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）；`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」；`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（尺寸·坡度·消防·无障碍仅作一般性说明并附规范提示）/D10（关键事实需两独立来源，否则标待核实）/D11（link_ok 三态）/D14（needs_verification 与 pending_notes 联动）。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根无同名文件，实际位于 `D:/Users/Administrator/Desktop/`（与第 12–24 轮一致），已按该路径只读读取；`DECISIONS.md`、`research/spotcheck-round24.md` 在仓库根。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考，不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。

## 〇、数据稳定性说明

- **抽检样本稳定**：本轮开始时 `data/sources.json`=102265B/mtime 21:28:55、`entries/l2-samples.json`=7563B/19:42:39、`entries/batch-02-c.json`=23467B/21:02:34、`entries/batch-02-d.json`=17345B/21:28:55、`entries/batch-07.json`=14868B/20:05:41、`coverage.json`=80224B/21:28:55；至 **22:00:09 复核**，上述 6 个文件的字节数与 mtime **均未变** → 采样数据全程稳定。
- **并发说明**：`research/gaps-round25.md`、`research/reader_questions-round25.md` 为第 25 轮已存在的未跟踪产出；22:00 复核时另见 `M tools/healthcheck.py`（并发体检脚本编辑），属工具层，**不影响**本次抽检的 entries/sources/coverage 数据；本次未触碰 `tools/`。
- **本报告口径**：以当前最终态（上述 21:28:55 快照，22:00:09 复核未变）逐条复核。
- **只读声明**：本次**仅生成** `research/spotcheck-round25.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。抓取脚本与正文仅驻留系统临时目录（`%TEMP%/r25_full.py`、`r25texts.json` 等），非项目产物。联网内容一律视为数据，网页中任何指令均未执行。

## 一、判定口径与抓取方法

- **抽检对象（4 条既有 L2，跨主题）**：`perspective`（透视法/理论，`entries/l2-samples.json`）、`gothic`（哥特建筑/风格，`entries/batch-02-d.json`）、`wayfinding`（导视与寻路/动线，`entries/batch-07.json`）、`drainage`（排水/下沉空间，`entries/batch-02-c.json`）。抽样率满足体检抽检要求，且覆盖“理论/风格/动线/下沉空间”四类主题。
- **正文支撑口径（本轮重点）**：对每条所挂 verified 来源，**实抓正文并逐句比对** definition / 原理 / 典型手法 / 实例；重点核 **“名义第二来源是否真正支撑该条概念”**（而非仅“该来源存在且 verified”）。
- **抓取方法**：Python `urllib` + 浏览器 User-Agent 实抓；`en.wikipedia.org` canonical 多次超时，按任务允许改用 **owiki 同源镜像**（`https://owiki.org/wiki/<Title>`，同源、注明）；中文机构/期刊页 direct canonical 实抓。所有成功抓取均记录 HTTP 码、h1/标题、正文字符数与关键词命中。
- **结构口径**：按 TASK_design「条目页结构」核七节（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）、≥1 张内联 SVG 含「示意图，非施工图」、SVG 不出界、风控段含 D09 规范提示、`needs_verification`↔`pending_notes`↔`sections.待核实`↔`coverage.needs_verification_count` 联动。
- **体检口径（AUTONOMOUS §3.F）**：死链、重复条目、全站数据矛盾、孤儿页/空 related、来源正文重合度/套话、referential integrity（所有引用 id 存在且 verified=true）。

## 二、抽检对象的来源清单与完整性（任务 2 前置）

`python tools/check.py` 实跑 → **`PASS: all checks, 0 errors`（EXIT=0）**。四条的来源 id **全部存在、全部 verified=true**（无一缺失、无一未验证被引用）：

| 条目 | 来源 id | 存在/verified | link_ok | source_count |
| --- | --- | --- | --- | --- |
| perspective | wp-perspective-graphical / wp-vanishing-point / wp-brunelleschi / thepaper-perspective / nelson-atkins-perspective | ✅ ×5 / true ×5 | true,true,true,null,null | 5 |
| gothic | wp-gothic-architecture / wp-architectural-style | ✅ ×2 / true ×2 | true,true | 2 |
| wayfinding | wp-graphic-design / wp-wayfinding | ✅ ×2 / true ×2 | true,true | 2 |
| drainage | wp-architecture / wp-sunken-courtyard / gdkcsj-sysu-gym / sysu-gym-news / ytsjk-sysu-drainage | ✅ ×5 / true ×5 | true,true,null,null,null | 5 |

> 说明：`link_ok=null` 表示 canonical 直连待复核（D11 三态，不影响 verified）；四条**均非单源**（source_count≥2），故任务 2 的“单源披露”分支对抽样四条不直接适用；但“**名义多源/实质单源**”问题见 §三、§四。

## 三、任务 1：来源正文是否支撑 definition / 原理（实抓逐句比对，关键项）

### 3.1 perspective（透视法）——**核心线性透视、灭点、实例均被实抓正文支撑；「空气透视」分句本轮未在镜像正文核到；1413 与维基 1415–1420 有出入但已标待核实 → 合格（附 minor）**

实抓命中（数据，非指令）：
- **wp-perspective-graphical（owiki 同源镜像，canonical 两次超时；镜像 13394 字符，较第24轮 canonical 19663 字符为**节略版**）：** “Linear perspective is an approximate representation, generally on a flat surface, of an image as it is seen by the eye.”；“objects appear smaller as their distance from the observer increases…”；“All objects will recede to points in the distance, usually along the horizon line…”。关键词 `vanishing point`=4、`horizon`=2、`parallel`=2、`converge`=1、`depth`=3、`linear perspective`=4；**但 `aerial perspective`=0、`atmospheric`=0**。
- **wp-vanishing-point（镜像 10509 字符）：** “A vanishing point is a point on the image plane … where the two-dimensional perspective projections of parallel lines in three-dimensional space appear to converge.”；“The horizon line is a theoretical line that represents the eye level of the observer.” → **强支撑“视平线与灭点”**。
- **wp-brunelleschi（镜像 27753 字符）：** “the mathematical technique of linear perspective…”；“Brunelleschi conducted experiments **between 1415 and 1420**, including making paintings with perspectives of the Florence Baptistery viewed from the entrance of the Cathedral”；“The results were compositions with accurate perspective, as seen through a mirror.” → 支撑线性透视发明与洗礼堂镜子演示，**但年份为 1415–1420**。
- **thepaper-perspective（canonical HTTP200，5516 字符）：** `透视`=38、`布鲁内莱斯基`=20、`洗礼堂`=5、`1413`=1、`镜子`=4、`线性透视`=3；正文含“布鲁内莱斯基……创作了两块演示板……一幅……是洗礼堂”“钻了一个小孔……观察一面镜子，镜子中反映出洗礼堂的图像” → **强支撑实例与约 1413 说法**。
- **nelson-atkins-perspective（canonical HTTP200，6493 字符）：** “In the early 1400s, the Italian architect Filippo Brunelleschi (1377–1446) reintroduced … linear perspective.”；“With the help of mirrors, he sketched the Baptistery in perfect perspective.”；“the vanishing point, or point of convergence…” → 支撑 early 1400s、洗礼堂镜子、灭点、spatial depth。

逐项比对：
- definition「线性透视以视平线与灭点组织画面空间」→ **强支撑**（wp-vanishing-point + wp-perspective-graphical）。
- definition「空气透视以明度和色彩衰减补充深度线索」→ **本轮未核到直接支撑**：唯一覆盖“透视”总论的 wp-perspective-graphical 本轮仅得**镜像节略版**，正文 `aerial/atmospheric`=0；其余 4 源亦 0；第24轮 canonical（19663 字符）疑含该节但**本轮 canonical 超时未能直证**。→ 需以 canonical 复核（或改挂 airial/atmospheric perspective 专条）。
- 原理「平行深远线条向远处汇聚，用灭点、视平线与尺度递减表达深度」→ **强支撑**（多源逐句）。
- 实例「佛罗伦萨洗礼堂透视演示；布鲁内莱斯基；约 1413 年（约数）」→ 名称/地点/设计者 **有支撑**；年份“约 1413”来自 thepaper（1 处）+ nelson“early 1400s”，而 **wp-brunelleschi 记 1415–1420** —— 存在源间出入，**条目已置 needs_verification=true 并在待核实/pending 明写“约 1413 年（约数），原始文献年代仍存争议”**，属如实披露。

> **判定：合格（附 minor）**。线性透视、视平线/灭点、原理、实例（名/地/人）均由实抓正文具体支撑。minor：(1)「空气透视…」分句本轮仅得镜像、未核到直接支撑，建议以 canonical 或空气透视专条复核补证；(2)“约 1413”仅 thepaper 单点、与维基 1415–1420 有出入，虽已标待核实，但“学界通行定为约 1413”表述略强，宜弱化为“一说约 1413”。

### 3.2 gothic（哥特建筑）——**定义与原理被 wp-gothic-architecture 正文完全支撑；第二来源 wp-architectural-style 为泛论“建筑风格”总条、对哥特具体定义零支撑 → 名义双源实为单源，且 pending 为模板套话未披露 → 需改进（轻）**

实抓命中：
- **wp-gothic-architecture（owiki 同源镜像，89393 字符）：** “**The defining design element of Gothic architecture is the pointed arch.**”；“The use of the pointed arch in turn led to the development of the **pointed rib vault and flying buttresses**, combined with elaborate tracery and stained glass windows.”；“Gothic architecture is an architectural style that was prevalent in Europe from the late 12th to the 16th century…”。关键词 `pointed arch`=30、`rib vault`=30、`flying buttress`=19、`stained glass`=14 → **对 definition（尖拱/肋拱/飞扶壁）与原理（尖拱→肋拱+飞扶壁→大窗采光）逐句支撑**。
- **wp-architectural-style（owiki 同源镜像，10172 字符）：** `gothic`=2，且均为“建筑风格”概念举例（“……‘Romanesque’ and ‘Gothic’ were initially coined to describe architectural styles……”“……from the Gothic rib vault to modern metal…”）；`pointed arch`=0、`flying buttress`=0 → **对哥特具体定义/原理零实质支撑**，属**泛论总条**。

逐项比对：
- definition「以尖拱、肋拱与飞扶壁为特征的欧洲中世纪建筑风格」→ **完全支撑**（wp-gothic-architecture 逐句）。
- 原理「尖拱、肋拱与飞扶壁把荷载集中到柱墩，墙体可大面积开窗」→ **强支撑**（“……technical improvements in vaults and buttresses that allowed much greater height and larger windows”“transmission of light through stained glass windows”）。
- 第二来源 wp-architectural-style → **无效第二来源**（与哥特无关），导致**核心实为单源**。
- 待核实联动：`pending_notes`=“实例的具体名称、设计者与年代待补充独立来源。”为**全库通用模板**（见 §四/§七），`sections.待核实`=“具体教堂的设计者与年代待核实。”——**二者仅涉实例/年代，均未披露“第二来源无效、核心实为单源”**。
- 内容厚度：definition/overview/原理均一句，属“骨架式 L2”（见 §七 系统性问题）。

> **判定：需改进（轻）**。核心概念与原理由真实哥特专条完全支撑（**非**硬性不合格）；问题在于：(1) 第二来源 `wp-architectural-style` 为泛论总条、对哥特零支撑 → 关键事实名义双源实单源，未满足 D10；(2) `pending_notes`/待核实为模板套话，未如实披露单源/弱源；(3) 内容偏薄。**返工方向**：第二来源改挂真正论述哥特建筑或尖拱/肋拱/飞扶壁结构的权威页（或补一条）；`pending_notes` 改为“核心依据单一哥特专条；第二独立来源待补”；可择机加厚原理与实例。

### 3.3 wayfinding（导视与寻路）——**定义与原理被 wp-wayfinding 正文支撑；第二来源 wp-graphic-design 仅把 wayfinding 列为实践领域之一、对定义/原理支撑极弱 → 名义双源实为单源；内容最薄（原理≈定义）→ 需改进（轻）**

实抓命中：
- **wp-wayfinding（owiki 同源镜像，10364 字符）：** “**Wayfinding encompasses all of the ways in which people orient themselves in physical space and navigate from place to place.**”；“Wayfinding also refers to the set of architectural or design elements that aid orientation.”；“The basic process of wayfinding involves four stages: Orientation is the attempt to determine one's location…”。关键词 `wayfinding`=41、`signage`=7、`sign`=23、`orientation`=2 → **强支撑 definition 与原理**。
- **wp-graphic-design（owiki 同源镜像，26637 字符）：** `wayfinding`=1，仅“……practice areas for environmental graphic designers are **wayfinding**, placemaking, branded environments…”；`navigation`=0、`map`=0 → **仅说明“导视是环境图形设计的实践领域之一”，对 wayfinding 定义/原理零实质支撑**，属泛论总条。

逐项比对：
- definition「人在物理空间中借助标识、地图与视觉线索定向和导航的过程与设计」→ **强支撑**（wp-wayfinding 首句几乎逐字）。
- 原理「寻路是人在空间中依靠标识、地图与空间线索确定方位并抵达目标的过程」→ **支撑**，但**与 definition 高度重复**（同一句改写），L2“原理”节信息增量近零。
- 第二来源 wp-graphic-design → **对概念支撑极弱**（仅实践领域列举），核心实为单源。
- 待核实联动：`pending_notes` 为同一模板“实例的具体名称、设计者与年代待补充独立来源。”；待核实=“所引导视系统的设计者与年代待核实。”——**均只涉实例/年代，未披露单源/弱源**。
- 内容厚度：definition/overview/原理/典型手法各一句，属“骨架式 L2”中最薄一档。

> **判定：需改进（轻）**。definition/原理由 wp-wayfinding 支撑（非硬性不合格）；问题：(1) 第二来源 wp-graphic-design 仅列举实践领域、对定义/原理零支撑 → 名义双源实单源，未满足 D10；(2) 原理与定义重复、内容明显偏薄（近骨架）；(3) pending 为模板套话。**返工方向**：第二来源改挂真正论述 wayfinding/环境图形/寻路认知的权威页；原理改写成与定义互补的机制说明（如 Lynch《The Image of the City》认知地图、四阶段模型）；pending 写明单源。

### 3.4 drainage（排水）——**原理/典型手法被 ytsjk 专业论文强支撑、实例由 3 源互证且面积矛盾已如实标注；两条维基源（wp-architecture / wp-sunken-courtyard）对排水零命中属装饰性 → 合格（附 minor：清理装饰源、概念实为单源 ytsjk 建议补第二专业源）**

实抓命中：
- **ytsjk-sysu-drainage（canonical HTTP200，5244 字符，《给水排水》胡雪利）：** `排水`=47、`集水`=9、`重现期`=13、`下沉`=11、`雨水`=46、`压力流`=5；正文含“在……天沟内……设置 500mm(宽)×500mm(深)集水坑”“屋面排水系统重现期采用 50 年”“对于下沉式空间……需要靠提升进行压力流排水” → **对 definition/原理/典型手法（找坡、集水点、重现期、下沉空间压力流提升）强支撑**。
- **gdkcsj-sysu-gym（canonical HTTP200，1581 字符）：** 设计单位“北京市建筑设计研究院股份有限公司”、设计起止“2014.04-2015.02”、项目面积“25293㎡”、所在“珠海市”、“利用原有地形中 2 米深的水塘做了下沉式处理”→ **支撑实例（设计者/年份/地点/下沉手法）**；`排水`=0。
- **sysu-gym-news（canonical HTTP200，978 字符，南都 2014-11-25）：** “屋顶绿地版体育馆”“总建筑面积约 18000 平方米”→ 支撑实例背景；与 gdkcsj/ytsjk 的 25293㎡ **存在面积出入**（条目 pending 已写“建筑面积记载不一”）。
- **wp-architecture（镜像 31364 字符）：** `drainage`=0、`drain`=0、`slope`=0、`runoff`=0、`stormwater`=1（仅景观专业范围列举） → **对排水零实质支撑**（泛论建筑总条）。
- **wp-sunken-courtyard（镜像 1789 字符，stub）：** 仅“a courtyard below ground level”；`drainage`=0、`water`=0 → **对排水零支撑**。

逐项比对：
- definition「引导雨水离开低处空间与铺装的组织方式」→ **由 ytsjk 支撑**（下沉空间雨水提升、集水沟、重现期）。
- 原理/典型手法「坡度、沟槽与集水点把雨水迅速引离低洼；设找坡、明沟/暗管与雨水口；下沉空间尤需组织」→ **强支撑**（ytsjk 逐项）。
- 实例「中山大学珠海校区体育馆；中国珠海；北京市建筑设计研究院股份有限公司；2014–2015 设计、2017 投用」→ **3 源互证**（gdkcsj 设计单位/年份/地点；sysu/ytsjk 佐证）；面积 18000 vs 25293 已如实标注矛盾。
- 第二/附加来源：`wp-architecture`、`wp-sunken-courtyard` 对排水 **零命中**，属**装饰性维基源**；概念实质由**单一专业源 ytsjk** 支撑（但该源为真实、具体的给排水工程论文，质量高）。
- 待核实联动：`pending_notes`=“雨水排放工程参数待补充专业来源；建筑面积记载不一。”；待核实节同义 → **与正文矛盾点一致**（面积不一确有其事），比 gothic/wayfinding 的模板套话**更如实**；但未点明“概念实由 ytsjk 单源支撑”。

> **判定：合格（附 minor）**。原理/典型手法由真实给排水论文强支撑，实例多源互证且矛盾如实标注，是本轮四条中**来源最扎实**的一条。minor：(1) `wp-architecture`、`wp-sunken-courtyard` 对排水零支撑，属装饰性来源，建议删除或替换为真正论述排水/下沉空间防排水的来源；(2) 概念实质为单源（ytsjk），建议补第二独立专业源并在待核实注明；(3) 面积出入已标注，宜在正文或来源页注明口径。

## 四、任务 2：来源存在性 / verified / 单源披露（单源专项）

- **抽样四条**：来源 id 全部存在、全部 verified=true、无缺失；source_count 分别为 5/2/2/5，**均非单源**。
- **全库单源条目（source_count<2）共 5 条**，逐一核对单源披露（任务 2 重点）：

| 单源条目 | 唯一来源 | needs_verification | pending/待核实是否明说“单源” | 结论 |
| --- | --- | --- | --- | --- |
| rule-of-space | wp-composition-visual-arts | true | ✅“本条核心依据单一权威来源（构图条目 Rule of space 专节）；第二独立来源及实例设计者、年代待补充。” | 合规（第24轮返工后已如实声明单源） |
| diagonal-composition | wp-composition-visual-arts | true | ✅“……单一权威来源；……第二独立来源及实例待补充。” | 合规 |
| s-curve-composition | wp-composition-visual-arts | true | ✅“S 曲线术语与构图原理有单一权威来源支撑；……第二独立来源及实例待补充。” | 合规 |
| triangular-composition | wp-composition-visual-arts | true | ✅“……有单一权威来源支撑；……第二独立来源及实例待补充。” | 合规 |
| **screened-scenery** | wp-chinese-garden | true | ❌ 仅“苏州园林障景具体实例的设计者与年份待补充独立来源。”/待核实“具体实例的设计者与年份待核实。”——**未明说本条核心为单源** | **需改进（单源披露不完整）** |

> 结论：5 条单源中 **4 条合规**（正是第24轮被指“第二来源无效/消歧义”的 4 条构图条目，本轮已改为单源并如实声明——属**维护改善的正面证据**）；**`screened-scenery` 单源披露不完整**（仅述实例/年代，未声明核心单源），建议按同类模板补一句“本条核心依据单一权威来源 wp-chinese-garden”。

## 五、任务 3：七节结构 / SVG / 规范提示 / 待核实联动（实测）

| 检查项 | perspective | gothic | wayfinding | drainage |
| --- | --- | --- | --- | --- |
| 七节齐备（definition + 6 节，无缺无多） | ✅ | ✅ | ✅ | ✅ |
| 1 张内联 SVG，viewBox（0 0 760 400） | ✅ | ✅ | ✅ | ✅ |
| SVG 元素不出界（数值核对） | ✅ x∈[20,700] y∈[20,350] | ✅ x∈[100,660] y∈[140,370] | ✅ x∈[80,495] y∈[80,370] | ✅ x∈[80,680] y∈[110,375] |
| SVG 图注含「示意图，非施工图」 | ✅ | ✅ | ✅ | ✅ |
| 常见错误与限制含 D09 规范提示 | ✅ | ✅ | ✅ | ✅ |
| 正文无编造人名/引文 | ✅ | ✅ | ✅ | ✅ |
| 无编造年份（实例年份来源可查） | ✅（约1413 已标争议） | ✅（不适用） | ✅（不适用） | ✅（2014–2015/2017 有据） |
| needs_verification ↔ pending_notes ↔ 待核实 ↔ coverage.nvc | ✅ T/非空/有/1 | ✅ T/非空/有/1 | ✅ T/非空/有/1 | ✅ T/非空/有/1 |
| theme/tier/period/region 与 coverage 一致 | ✅ 理论/核心/文艺复兴至19世纪/欧洲 | ✅ 风格/核心/中世纪/欧洲 | ✅ 动线/重要/跨时期/全球 | ✅ 下沉空间/核心/跨时期/全球 |
| source_count 与 sources 一致 | ✅ 5 | ✅ 2 | ✅ 2 | ✅ 5 |
| **definition/原理 有实抓来源正文支撑** | ✅ 线性透视强支撑；空气透视分句待核 | ✅ 定义/原理强支撑；第二源无效 | ✅ 定义/原理支撑；第二源极弱 | ✅ 原理强支撑（ytsjk）；两条维基装饰 |

> 四条结构维度**全部通过**：七节完整、各 1 张 SVG 含图注且不出界、D09 提示在位、`needs_verification↔pending↔待核实↔nvc` 形式一致、theme/tier/period/region 与 coverage 对齐、`check.py` PASS 0 errors。**但“形式一致”≠“待核实声明如实覆盖实际缺口”**：gothic、wayfinding 的 pending/待核实与全库另一批条目**逐字相同**（模板套话，见 §七），未披露“第二来源无效/核心单源”。

## 六、逐条验收结论

| 条目 | 来源/正文支撑 | 结构·SVG·规范 | 待核实联动 | 结论 |
| --- | --- | --- | --- | --- |
| **perspective（透视法）** | 线性透视/视平线/灭点/原理/实例（名地人）均强支撑；「空气透视」分句本轮仅镜像未核到；1413↔1415–1420 出入已标待核实 | 全过 | 一致（待核实覆盖年份争议） | **合格（minor：补空气透视直接来源；1413 表述宜弱化）** |
| **gothic（哥特建筑）** | 定义/原理由 wp-gothic-architecture 强支撑；第二源 wp-architectural-style 泛论无关→核心实单源；内容薄 | 全过 | 形式一致但为模板套话、未披露单源 | **需改进（轻：换实质第二源/待核实写明单源/加厚）** |
| **wayfinding（导视与寻路）** | 定义/原理由 wp-wayfinding 支撑；第二源 wp-graphic-design 仅列举实践领域→实单源；原理≈定义、最薄 | 全过 | 形式一致但为模板套话、未披露单源 | **需改进（轻：换实质第二源/原理去重加厚/待核实写明单源）** |
| **drainage（排水）** | 原理/典型手法由 ytsjk 专业论文强支撑；实例 3 源互证、面积矛盾如实标注；两条维基源装饰性 | 全过 | 一致（面积不一如实对应） | **合格（minor：清理装饰性维基源；概念实单源 ytsjk 建议补第二专业源）** |

- **合格 2 条**：`perspective`、`drainage`（核心主张有实质来源支撑，问题为可随批修正的 minor）。
- **需改进 2 条（轻，非硬性不合格）**：`gothic`、`wayfinding`（核心概念有真实专条支撑，但第二来源为泛论总条致名义双源实单源，且待核实为模板套话未披露；内容偏薄）。
- **无硬性不合格**（无核心概念零支撑、无术语错配、无编造）。

## 七、全库体检建议（AUTONOMOUS §3.F，系统性缺陷）

实跑 `tools/check.py` **PASS 0 errors**；全库 **126 条全部 L2**（`LEVELS={'L2':126}`）；**无重复 id**；**所有条目引用的来源 id 全部存在且 verified=true（无缺失、无未验证被引用）**。但体检暴露以下**系统性/结构性**问题：

1. **【最突出·模板化 pending_notes】63/126 条（50%）的 `pending_notes` 是同一句**“实例的具体名称、设计者与年代待补充独立来源。”；全库仅 40 种不同 pending 文本。即“待核实”普遍只写“实例/年代待补”，**不反映真实缺口（如第二来源无效、核心单源、应用主张无源）**。gothic、wayfinding 即此模板实例；这使 `needs_verification` 联动“形式一致而实质失真”（D10/D14）。**建议**：按条目真实缺口重写 pending（单源写明单源、弱源写明弱源、无源应用写明无源），并作为体检批的优先项。
2. **【最突出·名义多源实单源】一批条目把“泛论总条”当作第二来源，实为单源**。全库中“1 实质源 + 1 泛论伞源”结构共 **13 条**，另有伞源被大量挂靠：`wp-architecture`×10、`wp-architectural-style`×5、`wp-symmetry`×4、`wp-leading-line`×2、`wp-graphic-design`×1、`wp-visual-arts`×2。实抓已证：wp-architecture 对 drainage 零命中、wp-architectural-style 对 gothic 零命中、wp-graphic-design 对 wayfinding 仅列举实践领域、wp-symmetry 对构图表（第24轮已证）零相关。受影响条目（示例）：gothic、postmodernism、wayfinding、service-route、universal-design、functional-zoning、balance、geometry-symmetry、rhythm-repetition、axis、visual-movement、leading-lines、plein-air 等。**建议**：对“实质+伞源”结构条目逐条判定伞源是否支撑；不支撑的删除或替换为真正论述该子概念的来源，并在 pending 如实降级为单源。
3. **【规模性·骨架式 L2 / 实例占位】120/126 条为“骨架式 L2”**（definition<45 字、overview<60 字、六节合计<420 字，判定阈值见机器汇总）；**71/126 条“实例”为“类型性描述”占位**（无具体案例），仅 39 条有具体实例（perspective、drainage 属有具体实例的少数）。全库虽已“全部 L2”，但**相当一部分是“形式达 L2、深度未达 L2”**。**建议**：下一阶段以“去骨架化”为维护主线——优先给核心/重要条目的定义与原理补机制说明、把类型性实例替换/补充为具体可查实例（名/地/设计者/年份），并保持双源。
4. **【死链】6 个来源 `link_ok=false`，其中仅 1 个仍被引用**：`wp-plaza`（被 `pedestrian-flow` 引用；note 记“URL 重定向，现标题 Town square，已按实际 h1 核对”）→ 建议把 `wp-plaza` 的 url 更新为 `Town_square`（或改挂现标题）并将 link_ok 复为 true；其余 `wp-art-nouveau / wp-indian-architecture / wp-japanese-architecture / wp-means-of-egress / wp-underground-space` 当前**无条目引用**（其中后两者 verified=false），可保留隔离或清理，不影响在库条目。
5. **【规范提示】2 条 L2 的「常见错误与限制」缺 D09 规范提示**：`east-west-perspective-compare`、`sustainable-architecture`。经看其正文，二者内容**未涉及尺寸/坡度/消防/无障碍数据**，故缺提示或属合理省略；建议在 TASK 规则下明确“无相关数据时可省”，或统一补一句以防审查误判。
6. **【孤儿/导航】10 条 `related` 为空**（如 wayfinding `related: []`），非严格“无入链孤儿页”，但相关条目缺失削弱站内导航与“悬空引用/相关条目”体检项；建议补齐相关条目。
7. **【数据一致性（已妥善处理的正例）】drainage 实例建筑面积 18000㎡（南都）vs 25293㎡（gdkcsj/ytsjk）**存差异，条目 pending 已如实写“建筑面积记载不一” → 处理得当，建议全库继续沿用“矛盾并列+待核实标注”，并复核是否还有其他跨页数据矛盾（本轮抽样未见）。
8. **【来源正文重合度/套话】** 四条的正文均为高度压缩的改写短句，未见大段搬用或近似改写来源结构；但“原理≈定义”“定义/概述一句化”在骨架式条文中普遍，属**模板化措辞**风险源（与第②③条同源），建议随“去骨架化”一并治理。

## 八、总体结论

- **抽样 4 条结果：2 合格（perspective、drainage）+ 2 需改进（gothic、wayfinding，轻）+ 0 硬性不合格。**
- **来源层面**：四条来源 id 全部存在、verified=true；中文专业/机构源（thepaper、nelson-atkins、gdkcsj、sysu、ytsjk）canonical 均 HTTP200 实抓核对；英文维基 canonical 多次超时，改用**owiki 同源镜像**（已注明同源），镜像为节略版，`perspective` 的“空气透视”分句因此本轮未核到、标注待 canonical 复核。
- **结构性系统缺陷（须记入维护台账）**：(1) **模板化 pending 63/126**；(2) **泛论伞源致名义多源实单源，涉及约 13 条“实质+伞源”结构**；(3) **骨架式 L2 120/126、实例占位 71/126**；(4) 单源披露 1 条 `screened-scenery` 不完整；(5) 死链在库引用 1 处（`pedestrian-flow→wp-plaza`）。以上均**非硬性不合格**（核心概念普遍有真实来源），但直接决定“L2 质量”与“待核实口径真实性”。
- **是否整批返工**：**不建议整批降级重写**（核心概念均有真实来源支撑、结构/规范/联动形式全过、check.py PASS）。**建议体检后按“专项维护”处理**：①批量重写模板 pending（按真实缺口）；②逐条判定并替换伞源（wp-architecture/architectural-style/symmetry/leading-line/graphic-design 等）；③对核心/重要条目启动“去骨架化/补具体实例”；④修正 screened-scenery 单源披露与 wp-plaza 死链；⑤复核 airial/空气透视直接来源。上述专项宜分批 commit、每批抽检复验。

---

### 机器可读汇总

```
ROUND=25
SAMPLER=spotcheck-r25
MODE=healthcheck(体检轮)
SCOPE=["perspective","gothic","wayfinding","drainage"]   # 4 条既有 L2，跨主题：理论/风格/动线/下沉空间
FILES={"perspective":"entries/l2-samples.json","gothic":"entries/batch-02-d.json","wayfinding":"entries/batch-07.json","drainage":"entries/batch-02-c.json"}
LIBRARY_SIZE=126 ; LEVELS={'L2':126} ; DUP_IDS=0
STATE_STABLE={"snapshot":"sources 102265B@21:28:55; l2-samples 7563B@19:42:39; batch-02-c 23467B@21:02:34; batch-02-d 17345B@21:28:55; batch-07 14868B@20:05:41; coverage 80224B@21:28:55","recheck":"22:00:09 all unchanged","concurrency":"M tools/healthcheck.py (tool only, no data change) + untracked gaps/reader_questions-round25"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SOURCES_EXIST_VERIFIED_ALL=true
FETCH_METHOD="urllib + Chrome UA; en.wiki canonical TIMEOUT -> owiki.org same-source mirror (noted); zh/institutional canonical HTTP200"
FETCH={
 "wp-perspective-graphical":"OWIKI mirror 13394c h1 ok; vanishing point=4 horizon=2 depth=3 linear perspective=4; AERIAL=0 ATMOSPHERIC=0(clause unconfirmed)",
 "wp-vanishing-point":"OWIKI mirror 10509c; 'vanish point ... parallel lines appear to converge'; horizon line; one-point perspective",
 "wp-brunelleschi":"OWIKI mirror 27753c; linear perspective; experiments 1415-1420; Baptistery from cathedral entrance; mirror",
 "thepaper-perspective":"CANONICAL 200 5516c; 透视38 布鲁内莱斯基20 洗礼堂5 1413=1 镜子4 线性透视3",
 "nelson-atkins-perspective":"CANONICAL 200 6493c; early 1400s Brunelleschi(1377-1446) linear perspective; Baptistery mirrors; vanishing point",
 "wp-gothic-architecture":"OWIKI mirror 89393c; 'defining design element = pointed arch'; pointed arch->rib vault+flying buttress; late12-16c Europe",
 "wp-architectural-style":"OWIKI mirror 10172c; gothic=2(only generic example) pointed arch=0 flying buttress=0 -> IRRELEVANT to gothic specifics",
 "wp-graphic-design":"OWIKI mirror 26637c; wayfinding=1(practice area list) navigation=0 map=0 -> generic",
 "wp-wayfinding":"OWIKI mirror 10364c; 'orient themselves in physical space and navigate from place to place'; aid orientation; 4 stages",
 "wp-architecture":"OWIKI mirror 31364c; drainage0 drain0 slope0 runoff0 stormwater1 -> IRRELEVANT to drainage",
 "wp-sunken-courtyard":"OWIKI mirror 1789c stub; 'courtyard below ground level'; drainage0 water0",
 "gdkcsj-sysu-gym":"CANONICAL 200 1581c; 设计单位=北京市建筑设计研究院股份有限公司; 设计2014.04-2015.02; 面积25293㎡; 珠海; 2米水塘下沉处理",
 "sysu-gym-news":"CANONICAL 200 978c; 南都2014-11-25; 屋顶绿地版; 约18000㎡",
 "ytsjk-sysu-drainage":"CANONICAL 200 5244c; 排水47 集水9 重现期13 下沉11 雨水46 压力流5; 500x500集水坑; 重现期50年; 下沉压力流提升"
}
BODY_SUPPORT={
 "perspective":"STRONG for linear-perspective/horizon/vanish-point/principle/instance(name/place/person); '空气透视' clause UNCONFIRMED this round (mirror lacks aerial/atmospheric; canonical timeout); 1413 vs wiki 1415-1420 discrepancy flagged needs_verification",
 "gothic":"STRONG by wp-gothic-architecture (definition+principle verbatim); 2nd source wp-architectural-style generic/irrelevant -> effectively single-source",
 "wayfinding":"SUPPORTED by wp-wayfinding (definition+principle); 2nd source wp-graphic-design only lists practice area -> effectively single-source; principle≈definition, thinnest",
 "drainage":"STRONG by ytsjk (principle/technique: slope, sump 500x500, 50yr, sunken pressure-flow); instance 3-source (gdkcsj+sysu+ytsjk) with area discrepancy 18000 vs 25293 flagged; wp-architecture/wp-sunken-courtyard decorative(hollow)"
}
SOURCES_STRUCT={"perspective":5,"gothic":2,"wayfinding":2,"drainage":5}  # all exist & verified=true
SINGLE_SOURCE_ENTRIES=["rule-of-space","diagonal-composition","s-curve-composition","triangular-composition","screened-scenery"]
SINGLE_SOURCE_DISCLOSURE={"rule-of-space":"OK declares single-source","diagonal-composition":"OK","s-curve-composition":"OK","triangular-composition":"OK","screened-scenery":"INCOMPLETE (only instance/year, not core single-source)"}
SEVEN_SECTIONS_OK=true_each ; SVG_COUNT=1_each ; SVG_IN_BOUNDS=true_each ; SVG_CAPTION_OK=true_each ; REGNOTE_OK=true_each
NEEDS_V={perspective:T/1, gothic:T/1, wayfinding:T/1, drainage:T/1}
PENDING_TEMPLATEIZED=true  # gothic & wayfinding both = "实例的具体名称、设计者与年代待补充独立来源。"
VERDICT={"perspective":"合格(minor:空气透视分句待canonical核;1413与wiki1415-1420出入已标待核实)","gothic":"需改进(轻:核心定义/原理强支撑,但第二源wp-architectural-style泛论无关->实单源;pending模板未披露;内容薄)","wayfinding":"需改进(轻:定义/原理支撑,但第二源wp-graphic-design仅列举实践->实单源;原理≈定义最薄;pending模板)","drainage":"合格(minor:原理由ytsjk强支撑,实例3源互证面积矛盾如实;两条维基源装饰性应清;概念实单源)"}
LIBRARY_HEALTH={
 "referential_integrity":"OK all referenced ids exist & verified=true; missing=0; used-unverified=0",
 "dup_ids":0,
 "templateized_pending_notes":"63/126 exact same sentence (50%); 40 unique across 126",
 "nominal_multisource_effective_single":{"count_1substantive+1umbrella":13,
   "umbrella_usage":{"wp-architecture":10,"wp-architectural-style":5,"wp-symmetry":4,"wp-leading-line":2,"wp-graphic-design":1,"wp-visual-arts":2},
   "examples":["gothic","postmodernism","wayfinding","service-route","universal-design","functional-zoning","balance","geometry-symmetry","rhythm-repetition","axis","visual-movement","leading-lines","plein-air"]},
 "skeleton_L2":"120/126 (def<45 & overview<60 & sections<420 chars)",
 "placeholder_instance":"71/126 '类型性描述'; only 39 with concrete instance",
 "deadlink_in_use":{"pedestrian-flow":["wp-plaza(redirect Town_square)"]},
 "deadlink_unreferenced":["wp-art-nouveau","wp-indian-architecture","wp-japanese-architecture","wp-means-of-egress","wp-underground-space"],
 "L2_missing_D09_note":["east-west-perspective-compare","sustainable-architecture"],
 "empty_related_count":10,
 "data_conflict":"drainage area 18000 vs 25293 (flagged in pending = good practice)"
}
OVERALL="2合格(perspective,drainage)+2需改进(轻:gothic,wayfinding)+0硬性不合格;四条来源全存在且verified;中文源canonical 200,英文维基canonical超时改owiki同源镜像(节略);系统性缺陷=模板化pending 63/126+泛论伞源致名义多源实单源(约13条)+骨架式L2 120/126+实例占位71/126+单源披露screened-scenery不完整+死链1处"
BATCH_REWORK="不建议整批降级重写;建议专项维护:①按真实缺口批量重写pending;②逐条判定替换泛论伞源;③核心/重要条目去骨架化+补具体实例;④修screened-scenery单源披露+wp-plaza死链;⑤复核空气透视直接来源。分批commit+抽检复验"
```

*（报告完）*
