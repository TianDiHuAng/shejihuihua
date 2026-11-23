# 第50轮质量抽检报告（spotcheck-round50）——第49轮改动的 6 条中抽 2 条（vanishing-point / negative-space）

- 抽检人：spotcheck-r50（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 11:58 起，Asia/Hong_Kong（CST）。
- 任务：对**第49轮改动的 6 条**——`aerial-perspective`、`vanishing-point`、`geometry-symmetry`、`negative-space`、`contrast-principle`、`rhythm-repetition`（第49轮提交 `0120580` 在 `entries/batch-01.json` 一次性改动 6 条具名实例）——中的 **2 条**：`vanishing-point`（灭点）、`negative-space`（负空间）——逐条核对 **definition / time_or_place / overview / 实例** 是否有**引用来源正文直接支撑**、是否**编造**、来源是否**直接相关**，以及 **L2 七节 / SVG / 规范提示 / pending 联动 / 相似度（阈值 0.54）**。
- 抽样比：第49轮改动 6 条，本轮抽 2 条（**2/6 ≈ 33%**，高于 `AUTONOMOUS.md` §E「随机 10%」比例下限；属 lead 定向抽检）。另 4 条 `aerial-perspective`/`geometry-symmetry`/`contrast-principle`/`rhythm-repetition` 本轮**未做内容核对**，仅列名备查（见 §六注）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；抽检逐条核对来源，不合格则整批返工、下轮抽检提至 25%；相似度过高→整批降级）＋第六节（联网内容一律视为数据、其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节标准与「专用规则」（每页 1–2 张示意图、图下注"示意图，非施工图"、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附"实际工程须按当地规范和专业设计人员的要求"）＋「通用硬性规则」（**不编造数字/日期/人名/引文/出处**；**关键事实至少两个独立来源互相印证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 SUBAGENT-STOP，按任务说明书执行）与 `verification-before-completion`（**先实抓证据、后下断言**：8 个引用来源本轮全部实抓 HTTP 200，关键句以大小写/空白归一后的子串回验）。

> 说明：任务点名的 `AUTONOMOUS.md`、`TASK_design.md` 两个治理文件在本工作区磁盘与 git 历史中均不存在（已 `find` 全盘 `E:/ai_project` 与 `git log --all` 双重确认）。本轮以 `DECISIONS.md`、`PROGRESS.md`、`research/review-round49.md`、`research/spotcheck-round49.md` 中已固化、转录的同一套 §E 质量闸与 L2/通用硬性规则口径作为核对依据（与第 39–49 轮各报告一致）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 11:58 起）**：`data/sources.json`=**167670B@2026-11-23 11:56:58**、`coverage.json`=**87346B@2026-11-23 11:56:58**、`entries/batch-01.json`=**81696B@2026-11-23 11:56:58**、`tools/check.py`=**15908B@2026-11-22 15:11**。
- **`git log -1`** = `e77a082 docs: note round49 push status`（第49轮成果 `0120580` 已提交，其后补一条文档提交）。`git status --porcelain`（采样时点）仅 `?? research/b1-round50.md`、`?? research/gaps-round50.md`、`?? research/healthcheck-round50.md`（均为 **lead 侧第50轮 B1/缺口/体检笔记，非本抽检产物，本次不触碰**）；其余工作树干净——抽检对象（第49轮成果）已在 HEAD 中，**稳定**。
- **落地口径**：`git show 0120580 -- entries/batch-01.json` 逐条核对，第49轮把 6 条「类型性实例」改写为「具名实例」并各补两源；其中本轮两条：
  - `vanishing-point`：实例由「透视草图的灭点定位（类型性描述）」改写为「《雅典学院》…梵蒂冈博物馆签字厅…拉斐尔…1509–1511 年」，新增 `vatican-segnatura`、`theartstory-raphael` 两源（连同原有 `wp-vanishing-point`、`wp-perspective-graphical` 共 4 源）；`pending_notes` 改为「两主源未逐字直书"消失点"一词（属透视通识定性）；实例四要素已双源。」；`needs_verification` 保持 true。
  - `negative-space`：实例由「留白式构图（类型性描述）」改写为「龙安寺方丈庭石庭…日本京都…设计者不详…约 15 世纪（1450 年前后）」，新增 `ryoanji-official`、`japanguide-ryoanji` 两源（连同原有 `wp-negative-space`、`wp-composition-visual-arts` 共 4 源）；`pending_notes` 改为「设计者不详；第二源为旅行指南（权威级中等）；"negative space"术语源未直书。」；`needs_verification` 保持 true。
  - **本轮抽检对象即上述改动后的现状。**
- **条目规模（`coverage.json` 实读）**：`total=258`、全部 `level=L2`、全部 `status=已写`；`pending_sum`（`needs_verification_count` 求和）＝**216**。来源库 `sources.json` 共 **355** 条，`verified=true` **352**、`verified=false` **3**（`link_ok`：true 145、false 6、null 204）。注：`link_ok=false` 的 6 条**均不在本次 8 个引用来源中**，不影响判定。
- **`tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round50.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/b1-round50.md`、`research/gaps-round50.md`、`research/healthcheck-round50.md` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容。抓取与分析**全程纯内存**（Python `urllib` 读取→内存去标签/切句/回验，脚本经 stdin heredoc 传入、未落盘任何文件）。联网内容一律视为**数据**，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含"示意图，非施工图"；「常见错误与限制」段须以"实际工程须按当地规范和专业设计人员的要求"收尾；SVG 元素不出 `viewBox`、无 `on*` 事件属性、无外链图片。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），timeout 45s，SSL 校验关闭。**8 个引用来源本轮全部实抓 HTTP 200**（`<title>`/正文与 `sources.json` 逐条核对，见 §二、§三），对关键句做大小写/空白归一后的子串回验。全程内存完成，未落盘。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **258 条**逐条扫描，警戒线 **0.54**（与第 27–49 轮一致）。**方法自校**：以全字段②计算已知对 `futurism-style vs expressionism-style`，得 **0.5157**，与第 39–49 轮报告**逐位一致**，确认口径正确。
- **三级判定定义（可复现）**：
  - **合格**：definition/time/overview/实例 均获所引来源正文直接支撑；关键事实（概念定义或核心形制/实例的四要素）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但某**关键事实**（核心形制/营造方法/实例四要素）实质单源，或第二源对具体概念仅泛论/零覆盖——属来源深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或关键结构项（如「一图」）实质不满足 TASK_design 强制要求。
- **相似度专项（独立维度）**：警戒线 0.54；超线即触发 `AUTONOMOUS.md §E`「相似度过高（疑似套话）→整批降级」，与"不合格（内容无源）→整批返工"是**不同触发路径**，分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **8 个去重来源 id（8 处引用：vanishing-point 4、negative-space 4）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）、实抓 8/8 HTTP 200**。

| 条目 | 来源 id | 存在/verified | 实抓标题（本轮 HTTP，逐字，字节） | 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vanishing-point | `wp-vanishing-point` | ✅/true | `Vanishing point - Wikipedia`（200，168934B） | Wikipedia | 权威百科 | true | **相关（直接、强）**：`the two-dimensional perspective projections of parallel lines in three-dimensional space appear to converge`；`vanishing point`（55 处）；`one to three vanishing points` |
| vanishing-point | `wp-perspective-graphical` | ✅/true | `Perspective (graphical) - Wikipedia`（200，418722B） | Wikipedia | 权威百科 | true | **相关（直接、强）**：`Vanishing points…`；`All objects will recede to points in the distance, usually along the horizon line`；`Italian Renaissance painters…`；`Renaissance` 专节 |
| vanishing-point | `vatican-segnatura` | ✅/true | `Room of the Segnatura`（200，46490B） | Musei Vaticani（官方） | 官方机构 | null | **相关（直接、强·官方）**：`The Room of the Segnatura contains Raphael's most famous frescoes`；`School of Athens`（画目）；`Vatican`。**但静态正文无年份（JS 渲染，`1509/1511` 均未现）** |
| vanishing-point | `theartstory-raphael` | ✅/true | `Raphael Paintings, Bio, Ideas \| TheArtStory`（200，163680B） | TheArtStory | 学术著作 | null | **相关（直接、强）**：`Fresco - Vatican City 1509-11 The School of Athens This fresco, also in the Stanza della Segnatura`；`three-point perspective`；`diminish`；`Renaissance` |
| negative-space | `wp-negative-space` | ✅/true | `Negative space - Wikipedia`（200，132109B） | Wikipedia | 权威百科 | true | **相关（直接、强·定义）**：`negative space or negative volume is the empty space around and between the subject(s) of an image`；`white space`；`positive space … surrounding space` |
| negative-space | `wp-composition-visual-arts` | ✅/true | `Composition (visual arts) - Wikipedia`（200，180359B） | Wikipedia | 权威百科 | true | **相关（直接）**：`Positive space is the subject of the piece. The empty spaces around, above, and within, is negative space` |
| negative-space | `ryoanji-official` | ✅/true | `大雲山 龍安寺｜Ryoanji`（200，6427B） | Ryōan-ji（官方寺院） | 官方机构 | null | **相关但内容稀薄（零覆盖·仅名称/地址/营业信息）**：正文仅 `Ryoanji`、`13, Ryoanji Goryonoshitacho, Ukyo-ku Kyoto-shi, Kyoto`、开放时间与票价——**无 `rock garden`、无年份、无石组/砂** |
| negative-space | `japanguide-ryoanji` | ✅/true | `Ryoanji Temple - Kyoto Travel`（200，255034B） | Japan Guide（旅行指南） | 学术著作（作者记为机构） | null | **相关（直接、中权威）**：`Ryoanji Temple…is the site of Japan's most famous rock garden`；`the site was converted into a Zen temple in 1450`；`A few stones of Ryoanji's famous rock garden` |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（均 4=4）。8 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。**
> **来源记录 `title` 字段核对（Minor）**：`vatican-segnatura`（记录 `Stanza della Segnatura — Musei Vaticani` vs 实际 `<title>=Room of the Segnatura`，同一页英文标题）、`theartstory-raphael`（记录 `Raphael — TheArtStory` vs 实际 `Raphael Paintings, Bio, Ideas | TheArtStory`）、`ryoanji-official`（记录 `Ryōan-ji — official` vs 实际 `大雲山 龍安寺｜Ryoanji`）、`japanguide-ryoanji`（记录 `Ryōan-ji — Japan Guide` vs 实际 `Ryoanji Temple - Kyoto Travel`）均为**副标题省略式记名**，属元数据 Minor，不影响事实。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 vanishing-point（灭点，第49轮改动）——**合格（definition/overview 双源、实例名称/地点/设计者双源，无编造；年份单源与 pending 措辞为需修正项）**
- 条目现状（实读）：`definition`＝"画面中相互平行的深远线汇聚的假想点。"；`time_or_place`＝"文艺复兴时期（参见来源）。"；`overview`＝"灭点位置决定观看方向与空间稳定性，是透视作图的核心。"；`实例`＝"名称：《雅典学院》（The School of Athens）；地点：梵蒂冈博物馆签字厅；设计者：拉斐尔（Raphael）；年份：1509–1511 年。以透视汇聚表现纵深。…"
- **definition / 原理（"相互平行的深远线汇聚 + 假想点"）双源直证**：
  - `wp-vanishing-point`：`the two-dimensional perspective projections of parallel lines in three-dimensional space appear to converge`（平行纵深线汇聚）＋`vanishing point` 全文 55 处＋`one to three vanishing points`。
  - `wp-perspective-graphical`：`Vanishing points…`＋`All objects will recede to points in the distance, usually along the horizon line`（纵深线收于一点）＋`perspective` 通篇。
  - → **"平行纵深线 + 汇聚于假想点" 由 wp 两独立条目互证，非编造。**
- **time_or_place「文艺复兴时期」**：`wp-perspective-graphical` 设 `Renaissance` 专节，并称 `Italian Renaissance painters and architects…`（透视在意大利文艺复兴发展）。→ 支撑（单一强源即可，条目已注"参见来源"）。
- **overview「灭点决定观看方向/空间稳定，是透视作图核心」**：`wp-perspective-graphical` 关于 vanishing points、horizon、perspective projection 的整节内容支撑；`wp-vanishing-point` 亦证其为透视核心。→ 支撑。
- **实例四要素（《雅典学院》）**：
  - `theartstory-raphael`（独立教育机构）：`Fresco - Vatican City 1509-11 The School of Athens This fresco, also in the Stanza della Segnatura…`＋`three-point perspective`＋`diminish`——**名称/地点(梵蒂冈/签字厅)/年份(1509-11)/透视纵深描写 全要素直证**。
  - `vatican-segnatura`（梵蒂冈博物馆官方）：`School of Athens`＋`Raphael's most famous frescoes`＋`Room of the Segnatura`——**名称/设计者/地点(签字厅)直证；但静态正文无年份**。
  - → 名称、地点、设计者 **官方 + 教育机构 双独立源互证**；**年份 1509–1511 仅 TheArtStory 一源直证**（Vatican 页 JS 渲染，静态抽取无 `1509/1511`；评审底稿所列第二年份源 `wga.hu`（Web Gallery of Art）**并未落入本条目 `sources`**）。
  - **无编造**：《雅典学院》1509–1511、拉斐尔、梵蒂冈签字厅均为真实且经 TheArtStory 直证；图像不复制。
- **专项问题（需修正 / Minor）**：
  - ① **年份单源且 pending 措辞虚报**：`pending_notes`＝"实例四要素已双源"，但落地 4 源中**年份 1509–1511 只有 `theartstory-raphael` 一源**（`vatican-segnatura` 静态无年份），实际是"名称/地点/设计者双源、年份单源"。`pending_notes` 应改为如"名称/地点/设计者双源；年份 1509–1511 据 TheArtStory（Vatican 官方页未标年）"。
  - ② `pending_notes` 首句"两主源未逐字直书'消失点'一词（属透视通识定性）"**与实际不符**：`wp-vanishing-point` 正是以英文 `vanishing point` 直接定义该词（全文 55 处）。该句疑为沿用评审底稿对 Vatican/WGA 的判断而误挂到"两主源"，属措辞/对象错位，建议更正或删除。
  - ③ 落地来源与评审底稿的差异：底稿给出 ①Vatican ②**WGA(wga.hu)** ③TheArtStory，落地换成 ①`vatican-segnatura` ②`wp-vanishing-point` ③`wp-perspective-graphical` ④`theartstory-raphael`，**未纳入 WGA**——本身不构成缺陷（wp 两源对"灭点/透视"更直接），但正是缺了 WGA 使"年份双源"落空（见①）。
- **内容判定：合格**（definition/原理 双源互证；实例名称/地点/设计者官方+教育机构双源；无编造；仅"年份单源 + pending 措辞虚报/错位"两处需修正项）。

### 3.2 negative-space（负空间，第49轮改动）——**待核实（definition/overview 双源成立，但实例四要素实质单源、官方源零覆盖、period"20世纪"无源——来源深度缺陷，非编造）**
- 条目现状（实读）：`definition`＝"主体之外的空白区域参与构图的方法。"；`time_or_place`＝"20世纪（参见来源）；中国画留白传统另见相关条目。"；`overview`＝"负空间塑造主体轮廓并控制画面呼吸感。"；`实例`＝"名称：龙安寺方丈庭石庭（Ryōan-ji rock garden）；地点：日本京都；设计者：不详；年份：约 15 世纪（1450 年前后）。以白砂与置石留白组织"负空间"。…"
- **definition / 原理（"主体之外的空白区域"）双源直证**：
  - `wp-negative-space`：`negative space or negative volume is the empty space around and between the subject(s) of an image`（主体周围/之间的空白空间）＋`white space`＋`positive space … surrounding space … is seen as the negative space`。
  - `wp-composition-visual-arts`：`Positive space is the subject of the piece. The empty spaces around, above, and within, is negative space`。
  - → **"主体之外的空白区域" 由 wp 两独立条目互证，非编造。**
- **overview「塑造主体轮廓 + 控制呼吸感」**：`wp-negative-space` `the space around a subject, not the subject itself, forms…`（塑造主体轮廓）＋ positive/negative space 主次关系——支撑（"呼吸感"为通识引申，可接受）。
- **time_or_place「20世纪」——无引用来源支撑（关键缺陷）**：
  - `wp-negative-space` 全文年份＝`[1016,1984,1993,1999]`，`20th`/`twentieth`/`20th-century` **均 0 处**（仅参考文献含 `21st Century Practice`）。
  - `wp-composition-visual-arts`、`ryoanji-official`、`japanguide-ryoanji` 亦**无** `20th/twentieth/20th century`（japanguide 的 `century` 仅出现在"Century-Old Kiln"广告）。
  - → **4 个引用来源均不直书"20 世纪"**，而 `time_or_place` 以"（参见来源）"声称有据——属**时间口径无源**（条目与 `coverage.period=20世纪` 同值、历史遗留，但本轮改动未纠正、pending 亦未披露）。
- **实例四要素（龙安寺石庭）——实质单源 + 官方页零覆盖**：
  - `japanguide-ryoanji`（旅行指南，中权威）：`is the site of Japan's most famous rock garden`（名称/岩石庭）＋`converted into a Zen temple in 1450`（1450）＋`A few stones of Ryoanji's famous rock garden`（置石）＋`Kyoto`——**名称/地点/年份/石组 唯一实质来源**。
  - `ryoanji-official`（官方寺院）：实抓正文**仅**营业时间、票价、地址 `13, Ryoanji Goryonoshitacho, Ukyo-ku Kyoto-shi, Kyoto`、页脚版权；**无 `rock garden`、无年份、无石组/砂、无 1450**——对"具体概念仅零覆盖"，只证名称"Ryoanji"与所在地京都。
  - **设计者不详**：两源均未署名设计者，与"不详"自洽。
  - **"1450"是寺院改禅寺之年，非石庭造园之年**：Japan Guide 原句为 `the site was converted into a Zen temple in 1450`；评审底稿亦记「石庭具体年代无确切定论」。条目写"约 15 世纪（1450 年前后）"把**寺院改禅寺年**当作**石庭年代**，属口径滑移（非编造地理/人名）。
  - **"以白砂与置石…组织'负空间'"为通识解读**：两园林来源均**未出现 `negative space`**（`negative space` 在 ryoanji/japanguide 中 0 处），"白砂"亦未在 japanguide 明写（仅"stone/rocks"与"Zen sand raking"体验广告）；把龙安寺读作"负空间范例"是艺术史通识解读，非来源直书——`pending_notes` 已披露此点。
  - → **实例四要素中，名称/年份/石组 实质仅 `japanguide`（旅行指南）单源；官方页对详情零覆盖**——命中「第二源对具体概念零覆盖 / 实例四要素实质单源」的**待核实**判据。
- **无编造**：龙安寺在京都、以岩石庭著称、1450 由别墅改禅寺，均为真实且经 Japan Guide 直证；不复制图像、不虚构设计者。
- **专项问题（重点）**：
  - ① **period"20 世纪"无任何引用来源支撑**（见上），且 `pending_notes`/「待核实」**未披露**——应改为据实（如删"20 世纪"或注明"术语通行于 20 世纪艺术批评，所引条目不直书"）。
  - ② **实例实质单源（旅行指南）+ 官方页零覆盖**：`ryoanji-official` 仅有名称/地址/营业信息，`japanguide` 为旅行指南（中权威）；"双源"形式成立但**内容深度单薄**，`pending_notes` 已部分披露（"第二源为旅行指南（权威级中等）"），但未点明"官方页仅名称地址、零覆盖详情"。
  - ③ **年份口径滑移**：1450 为改禅寺年，非石庭成园年；建议写"约 15 世纪（寺院 1450 年改禅寺；石庭具体年代无定论）"。
- **内容判定：待核实**（definition/overview 双源、无编造；但**实例四要素（名称/年份/石组）实质单源+官方源零覆盖**、**period"20 世纪"无源**——属来源深度缺陷，非不合格）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：8 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）；`link_ok`：wp 两源 true，其余六源 null（三态未标，非死链、非假源）。**8 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：wp-vanishing-point(200)/wp-perspective-graphical(200)/vatican-segnatura(200)/theartstory-raphael(200)/wp-negative-space(200)/wp-composition-visual-arts(200)/ryoanji-official(200)/japanguide-ryoanji(200)——**8/8 全部 HTTP 200**，无死链（体检 F 之"死链"对本次 8 源为 0）。
- **相关性结论**：
  - vanishing-point：`wp-vanishing-point`、`wp-perspective-graphical`、`vatican-segnatura`（官方）、`theartstory-raphael` **4 源均直接相关**（前两源直书灭点/透视定义，后两源直指《雅典学院》实例）。
  - negative-space：`wp-negative-space`、`wp-composition-visual-arts` **直接定义源（强）**；`japanguide-ryoanji` 直接命中岩石庭/1450（中权威旅行指南）；`ryoanji-official` **相关但内容稀薄——仅名称/地址/营业信息，对实例详情零覆盖**。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件属性 / 外链图 | 规范句收尾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vanishing-point | L2 | ✓ | 6/6（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| negative-space | L2 | ✓ | 6/6（同上） | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含"示意图，非施工图"、无 `on*` 事件属性、无 `<image>`/外链；「常见错误与限制」段均以"实际工程须按当地规范和专业设计人员的要求"收尾；`check.py` 含 SVG 出界检查，本轮 PASS。**机械项两条全部通过。**

### SVG 质量观察（形态贴合主题，但缺「设计意图/尺寸关系」显式标注——次要、系统性）
- **vanishing-point**：四条斜线（`line` x1=80/690,y1=90/300 收于 470,205）+ 圆点（灭点）+ 文字"所有斜线交于此"——**贴合"平行线汇聚于灭点"主题、非随机占位**；但仅标题 + "示意图，非施工图"，**缺 TASK_design 第6条「图中标注设计意图或尺寸关系」**（次要、系统性）。
- **negative-space**：外框矩形 + 实心圆"主体" + 旁注"负空间"——**贴合"主体与负空间"对比主题、非随机占位**；同样**未标注具体设计意图或尺寸关系**（次要、系统性）。
- **判定**：两条「一图」机械项（1 张 + viewBox + "示意图，非施工图" + 无越界 + 无事件属性/外链）全过，图形与主题相关；**唯一不足为「缺图中设计意图/尺寸关系标注」**——`check.py` 只查出界与注记，查不出该语义项，属**次要/可提升**，不构成本轮"不合格"。建议全站统一补强（延续第 44–49 轮方向）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对）：vanishing-point（灭点/理论/重要/文艺复兴至19世纪/欧洲/L2）、negative-space（负空间/理论/重要/20世纪/全球/L2）；`source_count` 与来源数组长度一致（4=4、4=4）；`needs_verification_count`：各 1；`related`：vanishing-point=`["horizon-line"]`（存在，视平线）、negative-space=`["visual-center"]`（存在，视觉中心），**无悬空**。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| vanishing-point | true | "两主源未逐字直书"消失点"一词（属透视通识定性）；实例四要素已双源。" | 同左（逐字一致） | **结构一致** ✓（nv=true↔pending↔待核实 三处文本相同；但**内容有两处欠准**：首句"两主源未直书消失点"与 wp-vanishing-point 实况不符；末句"实例四要素已双源"与"年份单源"不符，见 §三 3.1） |
| negative-space | true | "设计者不详；第二源为旅行指南（权威级中等）；"negative space"术语源未直书。" | 同左（逐字一致） | **结构一致** ✓（nv=true↔pending↔待核实 三处文本相同；但**未披露** period"20世纪"无源、官方页零覆盖详情，见 §三 3.2） |

> 说明（D14 精神）：两条 nv=true，均置 pending 且「待核实」节非空，**结构联动正确**。差异在**披露完整度**：`negative-space` 未把"period 20 世纪无源""官方页仅名称地址零覆盖""1450 为改禅寺年"写入 pending；`vanishing-point` 的 pending 存在两处与实抓不符的表述。建议据 §三修正措辞后，`negative-space` 的 nv=true 是**恰当**的（判待核实后应保留），`vanishing-point` 若只修 pending 措辞、补年份第二源或注明单源，可维持合格。

### 元数据/批次注
- **type/year**：8 源 `year=null`（在线动态页，D06 允许）；`vatican-segnatura`/`ryoanji-official` 为**官方机构**（强权威）、`theartstory-raphael` 为学术著作（中—强）、`japanguide-ryoanji` 为旅行指南（中权威、作者记为机构）、`wp-*` 为百科（权威）。`ryoanji-official` 虽属官方但**页面为极简营业信息页、内容零覆盖**，权威标签不能弥补内容稀薄。
- **抽样范围注**：第49轮改动 6 条中，本轮仅对 `vanishing-point`、`negative-space` 做内容核对；`aerial-perspective`、`geometry-symmetry`、`contrast-principle`、`rhythm-repetition` **本轮未做内容核对**（不在本次 2 条内，仅列名备查）。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| vanishing-point | **0.4219** vs linear-perspective | <0.54 ✓ | **0.3709** vs one-point-perspective | <0.54 ✓ |
| negative-space | **0.3333** vs rule-of-space | <0.54 ✓ | **0.3618** vs liubai | <0.54 ✓ |

> 对**既有 257 条**（排除自身）逐条扫描，两条两档均 **<0.54**（短文本最大 0.4219、全字段最大 0.3709——分别出现在 vanishing-point 与 one-point-perspective/linear-perspective 之间，同属透视类近邻，正常）。**均未越线。**

### 7.2 第49轮 6 条批内去模板化核验（两两，全字段②）
- 全字段②批内**最大 0.3802**（geometry-symmetry vs rhythm-repetition），短文本①批内**最大 0.4211**（contrast-principle vs rhythm-repetition）——**批内两两均远低于 0.54，无第43轮 batch-42 式双条互为模板姊妹、无套话风险**。
- 本轮两条具体：vanishing-point vs negative-space 全字段 **0.3105**；与其余四条全字段区间 0.2806–0.3360，均在阈值内。

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第 39–49 轮报告**逐位一致**，口径正确。

> **文本相似度判定：两条对既有库与批内均 PASS（均 <0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 文本相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **vanishing-point（灭点）** | definition/原理（平行纵深线汇聚于假想点）**wp-vanishing-point+wp-perspective-graphical 双源互证**；time 文艺复兴（wp-perspective-graphical）；overview 双源；实例名称/地点/设计者 **vatican(官方)+theartstory 双源**、**年份 1509–1511 仅 theartstory 单源**；无编造；**需修正：年份单源、pending "四要素双源" 虚报、pending "两主源未直书消失点" 与实况不符** | 4/4 true；wp 两源+theartstory 直接强源、vatican 官方直接源；**4 源 200 可达** | 七节齐、规范句✓；1 SVG 含"示意图，非施工图"、形态贴合，**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 三处同文，**但 pending 两处内容欠准** | 既有库 ✓（0.4219/0.3709）；批内 ✓ | **合格**（附1项需修正：年份单源+pending 措辞） |
| **negative-space（负空间）** | definition/overview **wp-negative-space+wp-composition 双源**；实例名称/地点/年份 **实质仅 japanguide（旅行指南）单源**、**ryoanji-official 官方页零覆盖（仅名称/地址）**、1450 为改禅寺年非成园年、"负空间"关联为通识解读（源未直书，已披露）；**period"20世纪"无任何引用源支撑且未披露**；无编造 | 4/4 true；wp 两源直接强源、japanguide 中权威直接源、**ryoanji-official 内容稀薄零覆盖**；**4 源 200 可达** | 七节齐、规范句✓；1 SVG 含"示意图，非施工图"、形态贴合，**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 三处同文，**但未披露 period 无源/官方零覆盖** | 既有库 ✓（0.3333/0.3618）；批内 ✓ | **待核实** |

### 问题清单
- **① vanishing-point 年份单源 + pending 虚报（需修正）**：`pending_notes`="实例四要素已双源"，但落地 4 源中年份 1509–1511 仅 `theartstory-raphael` 一源直证（`vatican-segnatura` 静态无年份；评审底稿所列 `wga.hu` 未入源）。应改注"名称/地点/设计者双源；年份据 TheArtStory"。
- **② vanishing-point pending 对象错位（需修正）**：首句"两主源未逐字直书'消失点'"与 `wp-vanishing-point` 实况不符（该页正是以 `vanishing point` 定义该词）。建议更正或删除。
- **③ negative-space period"20 世纪"无源（重点/需修正）**：4 引用源均无 `20th/twentieth`；`time_or_place` 却注"（参见来源）"。应据实修正或注明术语通行年代而非所引条目。
- **④ negative-space 实例实质单源 + 官方页零覆盖（重点·判待核实主因）**：名称/年份/石组 仅 `japanguide`（旅行指南，中权威）直证；`ryoanji-official` 仅名称/地址/营业信息，对详情零覆盖。建议补一独立强源（如博物馆/大学枯山水论文；评审底稿曾试 Met 429、Britannica 404）或换更强实例。
- **⑤ negative-space 年份口径滑移（次要）**：1450 为寺院改禅寺年（`converted into a Zen temple in 1450`），非石庭成园年；建议写"约 15 世纪（寺院 1450 改禅寺；石庭年代无定论）"。
- **⑥ SVG"设计意图/尺寸关系"标注缺失（两条例、系统性·次要）**：两图机械项与主题贴合均过，但缺 TASK_design 第6条"图中标注设计意图或尺寸关系"——建议全站统一补强（延续第 44–49 轮）。
- **⑦ 来源元数据瑕疵（轻微）**：`vatican-segnatura`/`theartstory-raphael`/`ryoanji-official`/`japanguide-ryoanji` 的 `title` 为副标题省略式记名（建议存全名）。

## 九、总体结论与建议

- **抽样结果**：本轮抽第49轮改动 6 条中的 **2 条**——`vanishing-point`、`negative-space`（2/6≈33%，lead 定向抽检）。**内容维度：1 合格（vanishing-point）＋ 1 待核实（negative-space）＋ 0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：8 个引用来源 id **全部存在、verified=true、实抓 8/8 HTTP 200 可达**。`vanishing-point` 的 definition 双源（wp 两条目）、实例名称/地点/设计者双源（Vatican 官方 + TheArtStory）；`negative-space` 的 definition 双源（wp 两条目），但**实例四要素实质单源（Japan Guide 旅行指南）+ 官方页零覆盖**、且 **period"20 世纪"无源**。
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 形态贴合与唯一性通过、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：两条 nv=true 与 `pending_notes`/`待核实` 三处同文、结构一致；但 `vanishing-point` 的 pending 有两处与实抓不符（对象错位+虚报四要素双源），`negative-space` 的 pending 未披露 period 无源/官方零覆盖（内容披露不完整）。
- **相似度层面**：两条对既有库与批内均 <0.54（PASS）；批内最大全字段 0.3802、短文本 0.4211，无套话；方法自校 0.5157 与第 39–49 轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——**0 不合格**（1 合格 + 1 待核实），0 编造/假 id/死链。`negative-space` 为**来源深度缺陷（待核实）**而非无源/编造，不触发整批返工。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——两条对既有库与批内均 <0.54。
  3. **结论：本轮 1 条合格、1 条待核实，不触发整批返工/降级。** 第49轮通过"补具名实例 + 补第二机构源"较第48轮普遍改善；但 `negative-space` 的"双源"在**内容深度上仍偏单薄**（官方页零覆盖、旅行指南为中权威、period 无源），需定向补强或换更强实例。
- **返工/修复建议（定向、非整批）**：
  1. **（优先·问题③④）`negative-space`**：补一独立强源（博物馆/大学枯山水或龙安寺史论文）以支撑"岩石庭+年代"；或按评审底稿备选改取更强"东方留白"实例（如马远《寒江独钓图》，但须先抓双强源方可落证据）。同时把 period"20 世纪"改为据实（删或注明术语通行年代而非所引条目）。
  2. **（优先·问题①）`vanishing-point`**：补 WGA（`wga.hu`，"The School of Athens 1509"）或另一独立年份源使年份双源；否则把 `pending_notes` 改为"名称/地点/设计者双源、年份据 TheArtStory 单源"。
  3. **（问题②）`vanishing-point`**：更正 pending 首句（对象错位，wp-vanishing-point 实以 `vanishing point` 定义）。
  4. **（问题⑤）`negative-space`**：年份写"约 15 世纪（寺院 1450 改禅寺；石庭年代无定论）"。
  5. **（问题⑥，系统性）**：两图补「设计意图或尺寸关系」文字标注，并全站统一补强（延续第 44–49 轮）。
  6. **（问题⑦）**：来源 `title` 存全名。
- **流程记录**：本轮抽检 2 条＝**内容 1 合格、1 待核实、0 不合格、0 编造、0 假 id、0 死链、七节/规范/元数据/pending 结构联动一致、check.py PASS、相似度全 <0.54**；**主要遗留：`negative-space` 判待核实（实例实质单源+官方零覆盖+period 无源，需补强/换例）；`vanishing-point` 合格但年份单源+pending 措辞需修正；SVG 尺寸/意图标注系统性；少量来源 title 元数据。无可判整批返工的无源/编造硬缺陷，不触发 §E 整批返工/降级。**

---

### 机器可读汇总

```
ROUND=50
SAMPLER=spotcheck-r50
MODE=第49轮改动6条中定向抽2条（vanishing-point / negative-space）；另 aerial/geometry-symmetry/contrast/rhythm 未内容核对
SCOPE=["vanishing-point","negative-space"]
FILES={"vanishing-point":"entries/batch-01.json","negative-space":"entries/batch-01.json"}
ROUND49_COMMIT="0120580 feat: round49 six named instances, zero-gap 2/3"
ROUND49_CHANGED=["aerial-perspective","vanishing-point","geometry-symmetry","negative-space","contrast-principle","rhythm-repetition"]
GIT_HEAD="e77a082"; GIT_STATUS="clean except untracked research/b1-round50.md, gaps-round50.md, healthcheck-round50.md (lead notes, untouched); targets stable in HEAD"
STATE={"sources.json":"167670B@2026-11-23 11:56:58","coverage.json":"87346B@2026-11-23 11:56:58","batch-01.json":"81696B@2026-11-23 11:56:58","check.py":"15908B@2026-11-22 15:11","total":258,"all_level":"L2","pending_sum":216,"sources_total":355,"sources_verified_true":352,"sources_verified_false":3,"link_ok_true":145,"link_ok_false":6,"link_ok_null":204}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2/6 (~33%, lead 定向抽检)"
FETCH_METHOD="urllib+ChromeUA; 8/8 HTTP200; phrase substring verify after norm; analysis in-memory (stdin heredoc, no persistent file)"
SOURCES={"count_distinct":8,"count_refs":8,"all_exist":true,"all_verified_true":true,"all_reachable_200":"8/8",
 "vanishing-point":{"wp-vanishing-point":true,"wp-perspective-graphical":true,"vatican-segnatura":null,"theartstory-raphael":null},
 "negative-space":{"wp-negative-space":true,"wp-composition-visual-arts":true,"ryoanji-official":null,"japanguide-ryoanji":null},
 "relevance":{"vanishing-point":"wp两源直接定义; vatican官方+theartstory 直指雅典学院实例; 4源直接",
              "negative-space":"wp两源直接定义; japanguide中权威直接(most famous rock garden/1450); ryoanji-official内容稀薄仅名称地址零覆盖详情"},
 "title_note":"vatican/theartstory/ryoanji/japanguide title 副标题省略 -> minor"}
BODY_SUPPORT={
 "vanishing-point":"definition/原理 平行纵深线汇聚 双源(wp-vanishing-point 'parallel lines...appear to converge' + wp-perspective-graphical 'recede to points...Renaissance'); overview双源; time 文艺复兴(wp-perspective-graphical); 实例 名称/地点/设计者 dual(vatican官方'Room of the Segnatura/Raphael/School of Athens' + theartstory 'Fresco - Vatican City 1509-11 The School of Athens ... Stanza della Segnatura'), 年份1509-1511 仅theartstory单源(vatican静态无年; wga.hu未入源); VERDICT=合格 (需修正: 年份单源; pending'四要素双源'虚报; pending'两主源未直书消失点'与wp实况不符)",
 "negative-space":"definition/原理 主体外空白区域 双源(wp-negative-space 'empty space around and between the subject(s)' + wp-composition 'empty spaces around...is negative space'); overview双源; 实例 名称/地点/年份 实质单源(japanguide 'most famous rock garden'/'converted...1450'), ryoanji-official仅名称/地址零覆盖, 设计者不详(与源一致), 'negative space'关联源未直书(已披露); period'20世纪'无任何引用源支撑(4源0处20th/twentieth)且未披露; 1450为改禅寺年非成园年; VERDICT=待核实 (来源深度缺陷, 非编造)"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2, 无出界, 无on*/无外链图, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2"}
SVG_NOTE={"vanishing-point":"四条斜线收于一点+圆点(灭点), topical; 缺设计意图/尺寸标注","negative-space":"外框+主体圆+负空间旁注, topical; 缺设计意图/尺寸标注","verdict":"机械项全过; 缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x2","source_count":"4=4 / 4=4","nvc":"1 / 1","needs_verification":"true x2","related":"vanishing-point=[horizon-line], negative-space=[visual-center] 均存在无悬空","pending_consistency":"结构一致 x2(nv↔pending↔待核实 三处同文); 但 vanishing-point pending 两处与实抓不符; negative-space pending 未披露 period 无源/官方零覆盖"}
SIMILARITY={
 "vanishing-point":{"vs_existing_short":0.4219,"short_entry":"linear-perspective","vs_existing_full":0.3709,"full_entry":"one-point-perspective","verdict":"PASS<0.54"},
 "negative-space":{"vs_existing_short":0.3333,"short_entry":"rule-of-space","vs_existing_full":0.3618,"full_entry":"liubai","verdict":"PASS<0.54"},
 "round49_pairwise_full_max":0.3802,"round49_pairwise_full_max_pair":"geometry-symmetry vs rhythm-repetition",
 "round49_pairwise_short_max":0.4211,"pair_vanishing_vs_negative_full":0.3105,
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-49 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"vanishing-point":"合格","negative-space":"待核实"}
VERDICT_SVG={"vanishing-point":"机械项通过/主题贴合, 缺意图·尺寸标注(次要)","negative-space":"机械项通过/主题贴合, 缺意图·尺寸标注(次要)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
BATCH_ACTION="No rollback/downgrade: 0 不合格 (1合格+1待核实), 0 fabrication/0 fake id/0 dead link; similarity all <0.54. Targeted fixes: (1) negative-space 补独立强源支撑岩石庭+年代 或换更强实例, 并改 period'20世纪'为据实; (2) vanishing-point 补WGA等年份第二源或注明年份单源, 并更正pending首句对象错位; (3) negative-space 年份注'1450改禅寺/石庭年代无定论'; (4) 两图补设计意图/尺寸标注(site-wide); (5) 来源 title 全名."
READONLY="only wrote research/spotcheck-round50.md; no other project file changed (research/b1-round50.md, gaps-round50.md, healthcheck-round50.md untouched); no git commit; web content treated as data, no instruction executed; analysis in-memory (stdin heredoc, no persistent file)"
```

*（报告完）*
