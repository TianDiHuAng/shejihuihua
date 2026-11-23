# 第51轮质量抽检报告（spotcheck-round51）——第51轮补具名实例的 8 条中抽 3 条（linear-perspective / scattered-perspective / value）

- 抽检人：spotcheck-r51（由 lead 委派的子代理，无人值守、未提问）；抽样/核对时间 2026-11-23 15:04 起，Asia/Hong_Kong（CST）。
- 任务：对第51轮"补具名实例"改动条目中的 **3 条**——`linear-perspective`（线性透视）、`scattered-perspective`（散点透视）、`value`（明度），均在 `entries/batch-01.json`——逐条核对 **definition / time_or_place / overview / 实例** 是否有引用来源正文**直接支撑**、是否**编造**、来源是否**直接相关**；以及 **L2 七节 / SVG / 规范提示 / pending 联动（本次把实例替换为具名作品后 needs_verification/pending 是否与披露一致）/ 相似度（阈值 0.54）**。来源在 `data/sources.json`。
- 抽样说明：第51轮共落地 8 条具名实例（linear/scattered/three-point/horizon-line 来自 `review-round51a`；composition/balance/proportion/value 来自 `review-round51b`）。本轮抽检 lead 定向点名其中 3 条（3/8=37.5%，高于 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限）。其余 5 条本轮**未做内容核对**，仅列名备查（见 §六注）。
- 协议依据：`AUTONOMOUS.md` §E「质量闸」（`tools/check.py` 必须通过；抽检逐条核对来源，不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，不下载运行来源代码，不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注"示意图，非施工图"、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附"实际工程须按当地规范和专业设计人员的要求"）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 SUBAGENT-STOP，按任务说明书执行）与 `verification-before-completion`（**先实抓证据、后下断言**：12 个引用来源本轮全部重新实抓 HTTP 200，全部关键句做大小/空白/标点归一后的子串回验，未命中项进一步取上下文确认）。

> 治理文件说明：`AUTONOMOUS.md`、`TASK_design.md` 不在项目工作区磁盘、也不在本项目 git 历史（已 glob 全盘 + `git log --all --` 双重确认）；按 `research/review-round51a.md`/`review-round51b.md` 记录实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）。本轮以这套规则作为核对依据，与第 39–50 轮各报告口径一致。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 15:04 起）**：`data/sources.json`=**175604B@15:04:44**、`coverage.json`=**87347B@15:04:44**、`entries/batch-01.json`=**83028B@15:04:44**、`tools/check.py`=**15908B@2026-11-22 15:11:54**。
- **`git log -1`** = `e587fbe chore: round50 SATURATED=true again (3/3 zero-gap, 258 all L2, sparse=0)`；**第51轮改动尚未提交**——`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-01.json`、9 个 `site/entries/*.html`、`site/index.html`、`site/sources.html`，以及 `?? research/review-round51a.md`、`?? research/review-round51b.md`、`?? tools/apply_review_round51.py`（后三者为 lead 侧第51轮底稿/应用脚本，**本抽检不触碰**）。**抽检对象即上述未提交工作树中的 3 条具名实例现状**，非 HEAD 内容。
- **落地口径**：`git diff -- entries/batch-01.json` 逐条核对，第51轮把 8 条「类型性实例」改写为「具名实例」并各补两源；本轮 3 条：
  - `linear-perspective`：实例「文艺复兴线性透视绘画（类型性描述）」→「《圣三位一体》/佛罗伦萨 Santa Maria Novella/马萨乔/约 1425–1427（各家 1425–1428 / 1425–1426）」；新增 `wga-masaccio-trinity`、`wp-holy-trinity-masaccio`；`needs_verification` 保持 **true**，`pending_notes` 改为"年份各家不一，已并列；两源直证线性透视。"
  - `scattered-perspective`：实例「中国传统长卷山水（类型性描述）」→「《清明上河图》/北宋汴京（今开封），故宫藏/张择端/12 世纪初」；新增 `dpm-qingming`、`columbia-handscroll`；`needs_verification` 由 true **翻转为 false**，`pending_notes` 清空为 ""，「待核实」改为"暂无已知待核实项。"
  - `value`：实例「明度块面练习（类型性描述）」→「《夜巡》/阿姆斯特丹国立博物馆 SK-C-5/伦勃朗/1642」；新增 `rijks-nightwatch`、`wga-nightwatch`；`needs_verification` 由 true **翻转为 false**，`pending_notes` 清空为 ""，「待核实」改为"暂无已知待核实项。"
- **条目规模（`coverage.json` 实读）**：`total=258`、全部 `level=L2`、`status=已写`；`pending_sum`（`needs_verification_count` 求和）＝**213**（第50轮报告为 216，本轮因 3 条清零而下降，见 §六异常监控）。来源库 `sources.json` 共 **371** 条，`verified=true` **368**、`verified=false` **3**。
- **`tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round51.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/review-round51a.md`、`research/review-round51b.md`、`tools/apply_review_round51.py` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容。抓取与分析全程内存（Python stdin heredoc，抓取暂存 `/tmp` 临时文件已于写报告前删除，未在项目内落盘）。联网内容一律视为**数据**，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含"示意图，非施工图"；「常见错误与限制」段须以"实际工程须按当地规范和专业设计人员的要求"收尾；SVG 元素不出 `viewBox`、无 `on*` 事件属性、无外链图片。
- **抓取与回验方法**：Python `urllib` + 浏览器 UA（`Chrome/124`），timeout 40s，SSL 校验关闭；逐 URL 记录 HTTP 状态、字节数、`<title>`；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；关键句用 `norm()`（NFKC + 弯直引号/破折号/不间断空格归一 + 大小写 + 空白折叠）做 `norm(quote) in norm(body)` 子串回验，未命中项再取上下文人工判读。**12 个引用来源本轮全部实抓 HTTP 200**（见 §二）。
- **三级判定定义（可复现，沿用第50轮）**：
  - **合格**：definition/time/overview/实例 均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但某**关键事实**（核心概念/实例四要素/年份）实质单源，或第二源对具体概念零覆盖/主题错位；或 pending 联动与来源实况不一致——属来源深度或披露缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入），归一为**去空白+小写**。全库 **258 条**逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第 39–50 轮报告**逐位一致**，确认口径正确。
- **相似度是独立维度**：超线触发 §E「相似度过高（疑似套话）→整批降级」，与"不合格（内容无源）→整批返工"是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **12 个去重来源 id（12 处引用，每条 4 源）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）、实抓 12/12 HTTP 200**。

| 条目 | 来源 id | 机构 / type | 实抓标题（本轮 HTTP 200，逐字） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| linear-perspective | `wp-perspective-graphical` | Wikipedia / 权威百科 | `Perspective (graphical) - Wikipedia`（418722B） | true / true | **相关（直接·强·定义）**：`Linear perspective`、`vanishing point`、`Italian Renaissance` |
| linear-perspective | `wp-vanishing-point` | Wikipedia / 权威百科 | `Vanishing point - Wikipedia`（168934B） | true / true | **相关（直接·强·定义）**：`parallel lines`、`vanishing point` |
| linear-perspective | `wga-masaccio-trinity` | Web Gallery of Art / 学术著作 | `Trinity, fresco in the Santa Maria Novella in Florence`（12086B） | true / null | **相关（直接·强·实例）**：`most famous work of Masaccio`、`barrel vault drawn in perspective`、`between 1425 and 1428`、`Santa Maria Novella, Florence` |
| linear-perspective | `wp-holy-trinity-masaccio` | Wikipedia / 权威百科 | `Holy Trinity (Masaccio) - Wikipedia`（182619B） | true / null | **相关（直接·强·实例）**：`first monumental Renaissance paintings to utilize linear perspective`、`Masaccio created the Holy Trinity between 1425-1426`、`Santa Maria Novella` |
| scattered-perspective | `wp-chinese-painting` | Wikipedia / 权威百科 | `Chinese painting - Wikipedia`（410158B） | true / true | **标题相关但正文零覆盖**：全文 `perspective`=0、`scattered`=0、`viewpoint`=0、`focal`=0；仅 `distance`/`space` 一般论述，**不支撑"视点移动/多视点组合"定义** |
| scattered-perspective | `wp-reverse-perspective` | Wikipedia / 权威百科 | `Reverse perspective - Wikipedia`（106557B） | true / true | **主题错位**：讲拜占庭"反向透视"（物体位于投影点与视平面之间），`Chinese`=0、`China`=0；与"中国画散点透视"非同一概念 |
| scattered-perspective | `dpm-qingming` | 故宫博物院 / 官方机构 | `张择端清明上河图卷 - 故宫博物院`（106475B） | true / null | **相关（直接·强·官方·实例）**：`《清明上河图》卷，北宋，张择端作…`、`汴京（今河南开封）`；**但无"12世纪初"字样**（仅记"北宋"） |
| scattered-perspective | `columbia-handscroll` | Columbia University / 学术著作 | `Song Dynasty China \| Asia for Educators`（17539B） | true / null | **相关（直接·中权威·手法）**：`a handscroll can show the same object from different angles`、`overhead perspective`、`dramatically shifts his angle of vision`；**但 `Zhang Zeduan`=0、`12th`/`century`=0**，`Qingming` 仅见于导航标题 |
| value | `wp-colorfulness` | Wikipedia / 权威百科 | `Colorfulness - Wikipedia`（192956B） | true / true | **相关（直接·定义）**：`lightness`、`brightness`、`luminance`、`grayscale` |
| value | `wp-color-theory` | Wikipedia / 权威百科 | `Color theory - Wikipedia`（285442B） | true / true | **相关（直接·定义）**：`value (lightness)`、`lightness`、`luminance` |
| value | `rijks-nightwatch` | Rijksmuseum / 官方机构 | `The Night Watch Militia Company of District II… - Rijksmuseum`（299117B） | true / null | **相关（直接·强·官方·实例+手法）**：`Rembrandt van Rijn, 1642`、`Object number SK-C-5`、`used the light to focus on particular details` |
| value | `wga-nightwatch` | Web Gallery of Art / 学术著作 | `The Nightwatch by REMBRANDT Harmenszoon van Rijn`（8510B） | true / null | **相关（直接·强·实例+手法）**：`The Nightwatch 1642 Oil on canvas…Rijksmuseum, Amsterdam`、`chiaroscuro as a dramatic device` |

> 12 源 **全部 verified=true**，无假 id、无死链、`link_ok=null` 仅表示三态未标（非死链）。**相关性亮点/雷点**：`linear-perspective`、`value` 四源均直接相关且手法直证；`scattered-perspective` 的 `wp-chinese-painting` 正文对核心定义零覆盖、`wp-reverse-perspective` 主题错位（拜占庭反向透视），真正支撑"多视点"手法的只有 `columbia-handscroll` 一源。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 linear-perspective（线性透视，第51轮改动）——**合格**

- 条目现状（实读 line 6–37）：`definition`＝"以几何投影和灭点组织画面深度的透视体系。"；`time_or_place`＝"文艺复兴时期意大利（参见来源）。"；`overview`＝"它把观察者视点固定，使平行线按规律汇聚，是焦点透视的基础。"；`实例`＝"名称：《圣三位一体》（Holy Trinity）；地点：意大利佛罗伦萨新圣母玛利亚教堂；设计者：马萨乔（Masaccio）；年份：约 1425–1427 年（各家记 1425–1428 / 1425–1426）。以桶形拱券的透视表现纵深。…"
- **definition / 原理双源直证**：`wp-perspective-graphical` 命中 `Linear perspective`、`vanishing point`、`Italian Renaissance`；`wp-vanishing-point` 命中 `parallel lines`、`vanishing point`。→ "几何投影 + 灭点 + 平行线汇聚"由两个 Wikipedia 独立条目互证，非编造。
- **time_or_place「文艺复兴时期意大利」**：`wp-perspective-graphical` 命中 `Italian Renaissance`（透视在意大利文艺复兴发展）；`wp-holy-trinity-masaccio` 命中 `Renaissance`。→ 支撑（宽泛、条目已注"参见来源"）。
- **overview「固定视点/平行线按规律汇聚/焦点透视基础」**：`wp-vanishing-point`（平行线汇聚于灭点）＋ `wp-perspective-graphical`（线性透视基础）支撑。→ 支撑。
- **实例四要素（《圣三位一体》）——四要素均双源直证**：
  - 名称：`wga-masaccio-trinity` 标题 `Trinity, fresco in the Santa Maria Novella in Florence` ＋ `wp-holy-trinity-masaccio` 标题 `Holy Trinity (Masaccio)` → ✓ 双源。
  - 地点（佛罗伦萨 Santa Maria Novella）：`wga` `Santa Maria Novella, Florence` ＋ `wp-holy-trinity` `santa maria novella, in florence` → ✓ 双源。
  - 设计者（马萨乔）：`wga` `the most famous work of Masaccio` ＋ `wp-holy-trinity` `Masaccio created the Holy Trinity between 1425-1426` → ✓ 双源。
  - 年份（约 1425–1427，各家 1425–1428 / 1425–1426）：`wga` `between 1425 and 1428`、`Trinity 1425-28 Fresco` ＋ `wp-holy-trinity` `between 1425-1426` → ✓ 双源并列，已如实披露分歧，无编造。
  - 手法「桶形拱券的透视表现纵深」：`wga` `a barrel vault drawn in perspective…foreshortened…there seems to be a hole in the wall` ＋ `wp-holy-trinity` `one of the first monumental Renaissance paintings to utilize linear perspective` → ✓ **双源直证，贴合度高**。
- **无编造**：名称/地点/作者/年代/桶形拱券透视均经两独立源直证；不复制图像。
- **需注意（Minor，不影响合格）**：折中值"约 1425–1427"是两源区间（1425–1428 / 1425–1426）的折中，**非任一源原文**；虽已在括号内并列两源、非编造，但建议直写"约 1425–1428（Wikipedia 记 1425–1426）"以免误读为另有第三源。`pending_notes`"两源直证线性透视"措辞准确（指两个 wp 定义源），可保留。
- **内容判定：合格**。

### 3.2 scattered-perspective（散点透视，第51轮改动）——**待核实**

- 条目现状（实读 line 40–71）：`definition`＝"中国画中视点移动、多视点组合的空间表现方法。"；`time_or_place`＝"古代中国（参见来源）。"；`overview`＝"它使长卷能够连续展开不同视点下的景物，与焦点透视形成对照。"；`实例`＝"名称：《清明上河图》；地点：北宋汴京（今河南开封），原作藏北京故宫博物院；设计者：张择端；年份：12 世纪初。以手卷移步换景、视角流动体现散点透视。…"
- **definition 核心「视点移动 / 多视点组合」——实质单源，两 wp 源一零覆盖、一错位（关键缺陷）**：
  - `wp-chinese-painting`：实抓全文 `perspective`=0、`scattered`=0、`viewpoint`=0、`focal`=0；`shift` 的上下文是"paradigm shift in representation"（范式转变）、"shift their attention from jiehua"（题材转向），与视点移动无关；`vantage` 出现在"taking advantage of British traders"（利用）。→ **对核心定义零覆盖**。
  - `wp-reverse-perspective`：讲的是 `reverse perspective, also called inverse/inverted/divergent/Byzantine perspective`，`objects…placed between the projective point and the viewing plane`；全文 `Chinese`=0、`China`=0。→ **主题错位**（拜占庭反向透视 ≠ 中国散点透视）。
  - `columbia-handscroll`：`with the use of perspective, the artist can make something seem to come closer and then to recede, a handscroll can show the same object from different angles`、`the beijing scroll often employs an overhead perspective…but occasionally the artist dramatically shifts his angle of vision`。→ **唯一实质支撑**"多视点/视点移动"的来源（大学教学项目，中权威）。
  - → 定义主干"多视点组合"实质仅 `columbia-handscroll` **单源**支撑，命中「第二源对具体概念零覆盖/主题错位 → 待核实」判据。
- **time_or_place「古代中国」**：`dpm-qingming`（北宋）＋ `columbia-handscroll`（Song dynasty）提供背景，宽泛可接受；无独立"古代"断言需直证。
- **overview「长卷连续展开不同视点…与焦点透视形成对照」**：`columbia-handscroll` 支撑"不同角度/视角切换"；"与焦点透视形成对照"属通识比较、无源直书但可接受。
- **实例四要素（《清明上河图》）——官方单源直证 + 年份无源**：
  - 名称 / 朝代 / 地点 / 作者：`dpm-qingming` 官方正文 `《清明上河图》卷，北宋，张择端作…`、`描绘的是…北宋都城汴京（今河南开封）…` → 名称、北宋、张择端、汴京（开封）**官方强源直证**；但**仅此一源**（`columbia-handscroll` 的 `Qingming`=3 仅见于导航/标题 `translations of qingming shanghe tu`，`Zhang Zeduan`=0，对作者零覆盖）。
  - 年份「12 世纪初」——**无任何引用来源正文直接支撑**：`dpm-qingming` 仅记"北宋"（960–1127，跨 10–12 世纪，未直书 12 世纪初）；`columbia-handscroll` `12th`=0、`century`=0、`1100`=0、`twelfth`=0。`review-round51a` 底稿另引 `intro-two-versions.html` 记 "12th-century scroll"，但**该页未落入本条目 sources**。→ 与第50轮 `negative-space` 的 period"20世纪"无源**同类缺陷**。
  - 手法「以手卷移步换景、视角流动体现散点透视」：`columbia-handscroll` 的 `different angles`/`overhead perspective`/`shifts his angle of vision` 支撑"移步换景/视角流动"；但两源均未直书"散点透视"术语（术语定性属通识解读）。
- **无编造**：《清明上河图》、张择端、北宋汴京、故宫藏均为真实且经故宫官方直证；"12世纪初"是无源断言而非捏造的地名/人名/引文；不复制图像。
- **pending 联动（本轮重点·不合格项）**：`needs_verification` 由 true **清零为 false**、`pending_notes` 置空、「待核实」改为"暂无已知待核实项。"。但：
  - 核心定义实质单源（wp 一源零覆盖、一源主题错位）；
  - 实例作者实质单源（仅故宫官方 `dpm-qingming`），年份"12世纪初"无源；
  - 依 `TASK_design` 硬性规则「关键事实至少两个独立来源互证，否则标待核实」与 `DECISIONS.md` D14，此条**应维持 needs_verification=true** 并据实写 pending/待核实。清零 nv 属**把"补了具名实例"误当作"全部待核实已消除"**，与来源实况和披露不一致（披露失真）。
  - → **pending 联动：不合格（结构三处同文，但内容失真）**。这是本条判"待核实"的主要驱动之一。
- **内容判定：待核实**（核心概念实质单源 + 第二源主题错位、实例年份无源、作者单源、且 nv 被错误清零；非编造，属来源深度 + 披露缺陷，不触发整批返工）。

### 3.3 value（明度，第51轮改动）——**合格（附需注意项）**

- 条目现状（实读 line 210–241）：`definition`＝"色彩的明暗程度。"；`time_or_place`＝"跨时期、全球（参见来源）。"；`overview`＝"明度关系决定画面的结构与可读性，先于色相被视觉系统捕捉。"；`实例`＝"名称：《夜巡》（The Night Watch）；地点：荷兰阿姆斯特丹国立博物馆（SK-C-5）；设计者：伦勃朗（Rembrandt van Rijn）；年份：1642 年。以明暗对照与用光聚焦组织明暗层次。…"
- **definition「色彩的明暗程度」双源直证**：`wp-colorfulness` 命中 `lightness`/`brightness`/`luminance`；`wp-color-theory` 命中 `value (lightness)`/`lightness`。→ 双源互证，非编造。
- **time_or_place「跨时期、全球」**：色彩理论的通识属性，宽泛、无具体年代/地点断言需直证，可接受。
- **overview——部分直证、部分通识引申（需注意）**：`wp-colorfulness`/`wp-color-theory` 支撑"明度/明度关系"概念；但"**决定画面的结构与可读性**""**先于色相被视觉系统捕捉**"两句在两源正文中 `structure`、`readability`、`before hue`、`before color`、`first thing`、`more quickly than` **全 MISS**——属通识引申/感知先后宣称，无来源正文直证。因非"关键事实四要素"，判合格项下的需注意；建议弱化为通识表述或补色彩感知来源（比第50轮 negative-space 的"呼吸感"引申更具体，宜处理）。
- **实例四要素（《夜巡》）——四要素均双源直证，手法双源直证**：
  - 名称：`rijks-nightwatch` 标题/正文 `The Night Watch…` ＋ `wga-nightwatch` `The Nightwatch` → ✓ 双源。
  - 地点（阿姆斯特丹国立博物馆 SK-C-5）：`rijks` `Object number SK-C-5` ＋ `wga` `Rijksmuseum, Amsterdam` → ✓ 双源。
  - 设计者（伦勃朗）：`rijks` `Rembrandt van Rijn, 1642` ＋ `wga` `by REMBRANDT Harmenszoon van Rijn` → ✓ 双源。
  - 年份 1642：`rijks` `1642` ＋ `wga` `The Nightwatch 1642` → ✓ 双源。
  - 手法「明暗对照与用光聚焦组织明暗层次」：`rijks` `Rembrandt used the light to focus on particular details, like the captain's gesturing hand and the young girl in the background` ＋ `wga` `his use of chiaroscuro as a dramatic device` → ✓ **双源直证，贴合度是三条中最高**。
- **无编造**：四要素 + 明暗手法全部双源直证；不复制图像。
- **pending 联动（恰当）**：第51轮把原 pending「具体实例的设计者与年代待补充独立来源」彻底解决（四要素双源 + 手法双源），故 `needs_verification` 由 true 清零为 false、`pending_notes` 置空、「待核实」="暂无已知待核实项。" 与来源实况**一致**，清零恰当。唯一遗留是 overview 的通识引申句无源，不构成原 pending（具体实例设计者/年代）的未了项。
- **内容判定：合格**（definition + 实例四要素 + 手法均双源直证；无编造；pending 清零恰当；仅需处理 overview 引申句与次要项）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：12 个去重来源 id **全部存在、全部 verified=true**；`year=null`（在线动态页，D06 允许）；`link_ok`：6 源 true、6 源 null（三态未标，非死链）。**无一 false、无一假 id**。
- **可达性（本轮实抓）**：12/12 全部 HTTP 200（wp-perspective-graphical / wp-vanishing-point / wga-masaccio-trinity / wp-holy-trinity-masaccio / wp-chinese-painting / wp-reverse-perspective / dpm-qingming / columbia-handscroll / wp-colorfulness / wp-color-theory / rijks-nightwatch / wga-nightwatch），无死链。
- **相关性结论**：
  - `linear-perspective`：4 源**均直接相关**——前两源直书线性透视/灭点定义，后两源直指《圣三位一体》四要素与桶形拱券透视。
  - `scattered-perspective`：`dpm-qingming`（官方，直证实例名称/作者/朝代/地点）、`columbia-handscroll`（直证手卷多视点手法）相关；**`wp-chinese-painting` 正文对定义零覆盖、`wp-reverse-perspective` 主题错位**——两源"形式上引用、实质上不支撑核心定义"。
  - `value`：4 源**均直接相关**——前两源直证明度定义，后两源直证《夜巡》四要素与明暗/chiaroscuro 手法。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| linear-perspective | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| scattered-perspective | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| value | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含"示意图，非施工图"、无 `on*`、无 `<image>`/外链；「常见错误与限制」均以"实际工程须按当地规范和专业设计人员的要求"收尾；`check.py` 含 SVG 出界检查、本轮 PASS。**机械项三条全部通过。**

- **SVG 质量观察（形态贴合主题，但缺"设计意图/尺寸关系"标注——次要、系统性）**：
  - `linear-perspective`：视平线 + 单一灭点 + 三条汇聚斜线 + "视平线/灭点"标注——贴合"平行线汇聚于灭点"主题；缺"设计意图/尺寸关系"显式标注。
  - `scattered-perspective`：长幅外框 + 三个视点圆 + 连线 + "视点1/2/3"标注——贴合"多视点并列"主题；同样缺意图/尺寸标注。
  - `value`：四个明度梯度方块 + "明度梯度"标注——贴合"明度梯级"主题；同样缺意图/尺寸标注。
  - **判定**：机械项全过、图形与主题相关；唯一不足为缺 TASK_design 第6条"图中标注设计意图或尺寸关系"——`check.py` 查不出该语义项，属次要/可提升，建议全站统一补强（延续第 44–50 轮方向）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实（本轮重点）

- **三条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对）；`source_count` 与来源数组长度一致（4=4 ×3）；`needs_verification_count`：linear=1、scattered=0、value=0；`related`：linear=`["one-point-perspective"]`、scattered=`["composition"]`、value=`["saturation"]`，**均存在、无悬空**。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| linear-perspective | true（本轮未动） | "年份各家不一，已并列；两源直证线性透视。" | 同左（逐字一致） | **结构一致 ✓、内容准确 ✓**：年份分歧确实存在且已并列；"两源直证"指两 wp 定义源，成立。nv=true 恰当。 |
| scattered-perspective | **true → false（本轮清零）** | 清空为 "" | "暂无已知待核实项。" | **结构同向，但内容失真 ✗**：核心定义实质单源（wp 一源零覆盖、一源主题错位）、实例作者单源、年份"12世纪初"无源——应维持 nv=true。清零与来源实况和披露不一致，命中 §E「待核实占比异常低（疑似硬写）」的关注点（见下）。 |
| value | true → false（本轮清零） | 清空为 "" | "暂无已知待核实项。" | **结构一致 ✓、内容恰当 ✓**：实例四要素 + 明暗手法双源直证，原 pending（具体实例设计者/年代待补源）已彻底解决，清零合理。 |

> **异常监控（§E）**：全库 `pending_sum` 由第50轮 216 降至本轮 **213**（-3，对应第51轮 3 条清零：scattered-perspective、value、horizon-line；linear 等 5 条保留 true）。净降幅 3/258≈1.2%，**总量不构成"明显低于历史平均"的整批异常**；但 `scattered-perspective` 这一条清零属**个例误清**——补了具名实例 ≠ 核心概念与实例年份已获双源。建议定向回退该条 nv，而非整批处理。

## 七、任务 5：相似度（difflib 去空白+小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| linear-perspective | **0.4375** vs vanishing-point | <0.54 ✓ | **0.4223** vs one-point-perspective | <0.54 ✓ |
| scattered-perspective | **0.3652** vs cunfa | <0.54 ✓ | **0.3649** vs leaked-scenery | <0.54 ✓ |
| value | **0.4522** vs color-contrast | <0.54 ✓ | **0.3910** vs level-change | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。`value` 短文本 0.4522 为三者最高（vs color-contrast，同属色彩理论近邻，正常）。

### 7.2 第51轮批内 3 条两两（全字段② / 短文本①）

- linear-perspective vs scattered-perspective：全字段 **0.3063**、短文本 0.3259。
- linear-perspective vs value：全字段 **0.3487**、短文本 0.2333。
- scattered-perspective vs value：全字段 **0.3506**、短文本 0.1709。
- → 批内两两均远低于 0.54，**无套话/模板姊妹风险**。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第 39–50 轮报告**逐位一致**，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **linear-perspective（线性透视）** | definition/原理 **两 wp 源互证**；time 意大利文艺复兴（wp-perspective-graphical）；overview 两源支撑；实例四要素 + 桶形拱券透视 **wga + wp-holy-trinity 双源直证**；无编造；需注意折中年份"1425–1427"非原文（已并列两源） | 4/4 true；4 源直接相关；**4/4 200** | 七节齐、规范句✓；1 SVG 含"示意图，非施工图"、形态贴合，缺意图/尺寸标注（次要） | 全部一致；nv=true↔pending↔待核实 三处同文且内容准确 | 全库 ✓（0.4375/0.4223）；批内 ✓ | **合格** |
| **scattered-perspective（散点透视）** | 核心定义"多视点组合"**实质仅 columbia 单源**（wp-chinese-painting 正文零覆盖、wp-reverse-perspective 拜占庭反向透视主题错位）；实例名称/作者/朝代/地点 **故宫官方单源**直证、年份"12世纪初"**无来源支撑**、作者仅一源；无编造 | 4/4 true；**2 源正文零覆盖/错位**；4/4 200 | 七节齐、规范句✓；1 SVG 合规、形态贴合，缺意图/尺寸标注（次要） | 元数据一致；但 **nv 由 true 错误清零**、pending 空、待核实"暂无"——**联动内容失真** | 全库 ✓（0.3652/0.3649）；批内 ✓ | **待核实** |
| **value（明度）** | definition **两 wp 源互证**；实例四要素 + 明暗/chiaroscuro 手法 **rijks（官方）+ wga 双源直证**；无编造；需注意 overview 两句通识引申无源直证 | 4/4 true；4 源直接相关；**4/4 200** | 七节齐、规范句✓；1 SVG 合规、形态贴合，缺意图/尺寸标注（次要） | 全部一致；nv 清零恰当（原 pending 已由双源彻底解决） | 全库 ✓（0.4522/0.3910）；批内 ✓ | **合格** |

### 问题清单

- **① scattered-perspective 核心定义实质单源 + 两源不相关（重点·判待核实主因）**：`wp-chinese-painting` 正文 `perspective`=0/`scattered`=0/`viewpoint`=0，对"视点移动、多视点组合"零覆盖；`wp-reverse-perspective` 讲拜占庭反向透视、`Chinese`=0，主题错位；真正支撑"多视点"手法的只有 `columbia-handscroll`（大学教学项目，中权威）一源。建议补一独立强源直证"散点透视=中国画多视点/视点移动"概念本身（如故宫/大学学术论文论手卷多视点），否则维持待核实。
- **② scattered-perspective 年份"12世纪初"无来源支撑（重点）**：`dpm-qingming` 仅记"北宋"（960–1127）、`columbia-handscroll` `12th`/`century`=0；review 底稿所引 `intro-two-versions.html`（记 12th-century）未落入 sources。应改注"北宋（960–1127）"或补源直证 12 世纪初，或写"具体年代无定论"。
- **③ scattered-perspective pending 联动失真（重点·须回退）**：`needs_verification` 由 true 清零为 false，但核心概念单源、作者单源、年份无源，原「待核实」事项并未真正消除。应恢复 `needs_verification=true` 并据实写 `pending_notes`/「待核实」（问题①②）；或在补齐双源后再清零。
- **④ value overview 引申句无来源直证（次要）**："明度关系决定画面的结构与可读性""先于色相被视觉系统捕捉"在 `wp-colorfulness`/`wp-color-theory` 正文中 `structure`/`readability`/`before hue` 全 MISS。建议弱化为通识表述或补色彩感知来源；不影响合格判定。
- **⑤ linear-perspective 折中年份（轻微）**："约 1425–1427"为两源区间折中、非任一源原文（虽已并列披露、非编造）。建议直写"约 1425–1428（Wikipedia 记 1425–1426）"。
- **⑥ 三图"设计意图/尺寸关系"标注缺失（系统性·次要）**：SVG 机械项与主题贴合均过，但缺 TASK_design 第6条标注——建议全站统一补强（延续第 44–50 轮）。
- **⑦ 来源 title 元数据瑕疵（轻微）**：新增 8 源 title 多为简写记名（如 `Trinity, Santa Maria Novella — Web Gallery of Art`、`The Night Watch — Rijksmuseum`、`Song Dynasty China: The Handscroll Format — Columbia`），建议存实抓全名。

## 九、总体结论与建议

- **抽样结果**：第51轮 8 条具名实例中抽检 3 条——`linear-perspective`、`scattered-perspective`、`value`。**内容维度：2 合格（linear、value）＋ 1 待核实（scattered）＋ 0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：12 个引用来源 **全部存在、verified=true、实抓 12/12 HTTP 200**。`linear-perspective` 与 `value` 四源均直接相关、实例四要素 + 手法双源直证；`scattered-perspective` 存在**两源正文零覆盖/主题错位**（`wp-chinese-painting`、`wp-reverse-perspective`）与**年份无源**，仅官方 `dpm-qingming`（实例）+ `columbia-handscroll`（手法）实质支撑。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 形态贴合与唯一性通过、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：linear（nv=true）与 value（nv 清零）结构内容均一致且恰当；**scattered 的 nv 清零属个例误清**——把"补了具名实例"误当作"待核实已消除"，与核心概念单源/年份无源的实况不符（问题③）。全库 pending_sum 216→213（-3），净降幅 1.2% 不构成整批异常，但该个例须定向回退。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4522、全字段最高 0.4223）；方法自校 0.5157 与第 39–50 轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——**0 不合格**（2 合格 + 1 待核实），0 编造/假 id/死链。`scattered-perspective` 是**来源深度 + 披露缺陷（待核实）**，非无源/编造，不触发整批返工。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——pending_sum 净降 1.2%，非"明显低于历史平均"；但 scattered 单条 nv 误清须修正。
  4. **结论：本轮 2 条合格、1 条待核实，不触发整批返工/降级。** 第51轮"补具名实例 + 补第二机构源"对 `linear`、`value` 成效显著（双源直证、pending 可正当清零）；`scattered` 仍是**补了实例但未补概念双源**——新增两源一对定义零覆盖、一主题错位，且错误清零了 nv。
- **返工/修复建议（定向、非整批）**：
  1. **（优先·问题①②③）`scattered-perspective`**：恢复 `needs_verification=true` 并据实写 `pending_notes`/「待核实」；补一独立强源直证"散点透视=中国画多视点/视点移动"概念（现有两 wp 源一零覆盖一错位）；年份"12世纪初"补源或改为"北宋（960–1127）"/"具体年代无定论"；作者补第二独立源或明确标注单源。若一时无法补齐，宁可保持待核实，不可清零 nv。
  2. **（问题④）`value`**：overview 两句通识引申弱化表述或补色彩感知来源；实例与核心保持合格、nv=false 维持。
  3. **（问题⑤）`linear-perspective`**：折中年份改写为"约 1425–1428（Wikipedia 记 1425–1426）"；其余保持合格、nv=true 维持。
  4. **（问题⑥，系统性）**：三图（及全站）补「设计意图或尺寸关系」文字标注，延续第 44–50 轮方向。
  5. **（问题⑦）**：新增来源 title 存实抓全名。
- **流程记录**：本轮抽检 3 条＝**内容 2 合格、1 待核实、0 不合格、0 编造、0 假 id、0 死链、七节/规范/元数据机械项全过、check.py PASS、相似度全 <0.54**；**主要遗留：`scattered-perspective` 判待核实（概念实质单源 + 两源不相关 + 年份无源 + nv 误清，须定向修复）；`value` 与 `linear` 合格但各有 1 处措辞/引申需修正；SVG 意图/尺寸标注系统性缺失；少量来源 title 元数据。无可判整批返工的无源/编造硬缺陷，不触发 §E 整批返工/降级。**

### 机器可读汇总

```
ROUND=51
SAMPLER=spotcheck-r51
MODE=第51轮8条具名实例中lead定向抽3条（linear-perspective / scattered-perspective / value）；另 five 未内容核对
SCOPE=["linear-perspective","scattered-perspective","value"]
FILES={"linear-perspective":"entries/batch-01.json","scattered-perspective":"entries/batch-01.json","value":"entries/batch-01.json"}
GIT_HEAD="e587fbe"; ROUND51_COMMITTED=false; GIT_STATUS="round51 changes UNCOMMITTED in working tree (M coverage.json/data/sources.json/entries/batch-01.json + site/*; ?? research/review-round51a.md, review-round51b.md, tools/apply_review_round51.py - lead notes, untouched)"
STATE={"sources.json":"175604B@2026-11-23 15:04:44","coverage.json":"87347B@15:04:44","batch-01.json":"83028B@15:04:44","check.py":"15908B@2026-11-22 15:11:54","total":258,"all_level":"L2","pending_sum":213,"sources_total":371,"sources_verified_true":368,"sources_verified_false":3}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/8 (37.5%, lead 定向抽检)"
FETCH_METHOD="urllib+ChromeUA; 12/12 HTTP200; norm(quotes/dashes/nbsp/case/space) substring verify; MISS items context-checked; analysis in-memory; /tmp fetch cache deleted"
SOURCES={"count_distinct":12,"count_refs":12,"all_exist":true,"all_verified_true":true,"all_reachable_200":"12/12",
 "linear-perspective":{"wp-perspective-graphical":true,"wp-vanishing-point":true,"wga-masaccio-trinity":true,"wp-holy-trinity-masaccio":true},
 "scattered-perspective":{"wp-chinese-painting":true,"wp-reverse-perspective":true,"dpm-qingming":true,"columbia-handscroll":true},
 "value":{"wp-colorfulness":true,"wp-color-theory":true,"rijks-nightwatch":true,"wga-nightwatch":true},
 "relevance":{"linear-perspective":"4源直接相关(2定义+2实例)","scattered-perspective":"wp-chinese-painting正文零覆盖; wp-reverse-perspective拜占庭反向透视主题错位; dpm官方+columbia手法相关","value":"4源直接相关(2定义+2实例+明暗手法)"}}
BODY_SUPPORT={
 "linear-perspective":"definition/原理 几何投影+灭点+平行线汇聚 双wp源; time 意大利文艺复兴(wp-perspective-graphical Italian Renaissance); overview 两wp源; 实例《圣三位一体》四要素+桶形拱券透视 wga('most famous work of Masaccio'/'barrel vault drawn in perspective'/'between 1425 and 1428'/'Santa Maria Novella, Florence')+wp-holy-trinity('first monumental...linear perspective'/'Masaccio created...1425-1426') 双源; 无编造; VERDICT=合格 (需注意: 折中年份1425-1427非任一源原文,已并列)",
 "scattered-perspective":"核心定义'多视点组合'实质单源(columbia 'different angles'/'shifts his angle of vision'), wp-chinese-painting perspective=0零覆盖, wp-reverse-perspective Chinese=0主题错位(拜占庭反向透视); 实例《清明上河图》四要素 官方dpm单源('北宋,张择端作...汴京(今开封)'), 作者columbia=0, 年份'12世纪初'两源均无(仅北宋/0处12th)无源; 手法'视角流动'columbia直证但源未直书散点透视; 无编造; VERDICT=待核实 (来源深度缺陷+NV误清)",
 "value":"definition 色彩明暗程度 双wp源('lightness'/'value (lightness)'); 实例《夜巡》四要素+明暗手法 rijks('Rembrandt van Rijn, 1642'/'SK-C-5'/'used the light to focus')+wga('The Nightwatch 1642'/'chiaroscuro as a dramatic device') 双源直证; overview'决定结构可读性'/'先于色相'两源structure/readability/before hue全MISS(通识引申需注意); 无编造; VERDICT=合格"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3, 无出界, 无on*/无外链图, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3"}
SVG_NOTE={"linear-perspective":"视平线+单灭点+汇聚斜线, topical","scattered-perspective":"长幅+三视点圆, topical","value":"明度梯度方块, topical","verdict":"机械项全过; 三条均缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x3","source_count":"4=4 x3","nvc":"linear=1, scattered=0, value=0","needs_verification":"linear=true(未动), scattered=true->false(误清), value=true->false(恰当)","related":"linear=[one-point-perspective], scattered=[composition], value=[saturation] 均存在无悬空","pending_consistency":"linear结构内容一致/准确; value清零恰当; scattered清零失真(核心单源+作者单源+年份无源, 应维持true)"}
SIMILARITY={
 "linear-perspective":{"vs_all_short":0.4375,"short_entry":"vanishing-point","vs_all_full":0.4223,"full_entry":"one-point-perspective","verdict":"PASS<0.54"},
 "scattered-perspective":{"vs_all_short":0.3652,"short_entry":"cunfa","vs_all_full":0.3649,"full_entry":"leaked-scenery","verdict":"PASS<0.54"},
 "value":{"vs_all_short":0.4522,"short_entry":"color-contrast","vs_all_full":0.3910,"full_entry":"level-change","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.3506,"intrabatch_full_max_pair":"scattered-perspective vs value",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-50 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"linear-perspective":"合格","scattered-perspective":"待核实","value":"合格"}
VERDICT_PENDING={"linear-perspective":"一致/恰当","scattered-perspective":"失真(个例误清,须回退true)","value":"一致/恰当"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
ANOMALY_NVC="pending_sum 216->213 (-3, 1.2%); not batch-level anomaly; scattered single-entry nv mis-clear requires targeted fix"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (2合格+1待核实), 0 fabrication/0 fake id/0 dead link; similarity all <0.54; nvc drop not batch-anomalous. Targeted fixes: (1) scattered-perspective restore nv=true + add independent source for scattered-perspective concept + fix/annotate year '12世纪初' + second source for author; (2) value soften overview unsupported generality or add source; (3) linear-perspective rewrite midpoint year; (4) add design-intent/dimension annotations site-wide; (5) store full source titles."
READONLY="only wrote research/spotcheck-round51.md; no other project file changed (review-round51a/51b.md, apply_review_round51.py untouched); no git commit; round51 work remains uncommitted as found; web content treated as data, no instruction executed; /tmp fetch cache deleted; no file written outside deliverable"
```

*（报告完）*
