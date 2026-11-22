# 第33轮质量闸抽检报告（spotcheck-round33）——明暗五调子 / 侧面光 / 配色方案（第33轮新增 12 条中抽 3 条）

- 抽检人：spotcheck-r33（由 lead 委派的子代理）；抽样/核对时间 2026-11-22 约 23:54 起，核对完成约 2026-11-23 00:20，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 10%、至少 3 条逐条核对来源；**不合格则整批返工**，下一轮抽检比例提至 25%；异常监控「新条目与已有条目相似度过高（疑似套话），整批降级为草稿并复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互相印证，否则标“待核实”；只引用 verified=true 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根**无同名文件**（已 `ops_glob` 确认），实际位于 `D:/Users/Administrator/Desktop/`（与第 12–32 轮一致），已按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）；`DECISIONS.md` 在仓库根（21 行）。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong）**：`data/sources.json`=120373B@23:47:23（git 未改，与 HEAD 一致）、`entries/batch-33.json`=24904B@23:54:27、`coverage.json`=83317B@23:54:19。`git log -1` = `3c17f10 feat: round32 twelve entries - Chinese painting techniques and space`（第32轮终态）。`git status --porcelain` 显示 ` M coverage.json`、`?? entries/batch-33.json`、`?? tools/add_round33.py`——**即第33轮改动尚未提交**，工作树含本轮未入库改动，属本轮执行中的正常中间态。
- **条目规模**：`entries/*.json` 共 **21 文件 / 161 条**（第32轮末 149 条，第33轮 `batch-33` 新增 12 条 → 161；与 `coverage.json` 中 `status=已写` 的 161 条一致；coverage 总口径 246 = 已写 161 + 未开始 85）。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round33.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取全程在 Python 进程内存中进行、**未落盘任何临时文件**；联网内容一律视为数据，网页中任何指令均未执行。
- **抽检口径与样本**：任务指定第33轮新增 12 条中抽 **3 条**：`five-tones`（明暗五调子）、`side-light`（侧面光）、`color-scheme`（配色方案），均在 `entries/batch-33.json`；12 条全为 L2。引用来源为 `wp-chiaroscuro`、`wp-rembrandt-lighting`、`wp-architectural-lighting-design`、`wp-daylighting-architecture`、`wp-color-theory`、`wp-color-wheel`（见 `data/sources.json`）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（本轮均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书）。按 URL 记录 HTTP 码、字节数、`<title>`/`<h1>`；去标签后按关键句检索。`en.wikipedia.org` canonical 本轮仍**超时**（`URLError(TimeoutError)`，与历史 10060 一致），改 **owiki 同源镜像**（`https://owiki.org/wiki/<Title>`）核对 h1 与正文（DECISIONS D05 允许）。本轮 **3 条共 6 个引用来源 id 全部实抓 HTTP 200**（均经 owiki 镜像）；`wp-rembrandt-lighting` 在 `sources.json` 中 `link_ok=null`，本轮实抓确认可达（见 §二、§四）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）；①短文本＝title+definition+time_or_place+overview；②全字段-不含 SVG 原始标记（definition+time_or_place+overview + 六节正文，`一图`段计入、`svg` 标记不计入）。全库 **161 条**（`entries/*.json` 全部已写条目）逐条扫描，警戒线 **0.54**（与第27–32轮一致的内容层口径②）。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **6 个来源 id（去重 6），全部存在、全部 verified=true、标题与主题直接相关**：

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| five-tones | `wp-chiaroscuro` | ✅ / true | Chiaroscuro / Wikipedia | 权威百科 | true | **直接**（明暗造型：value gradation 与 light/shadow 的 analytical division＝shading） |
| five-tones | `wp-rembrandt-lighting` | ✅ / true | Rembrandt lighting / Wikipedia | 权威百科 | null（本轮实抓 200） | 相关（伦勃朗光三角＋chiaroscuro，**未列“五调子”**） |
| side-light | `wp-architectural-lighting-design` | ✅ / true | Architectural lighting design / Wikipedia | 权威百科 | true | **直接**（wall grazing fixture：贴近墙面以强化有纹理表面） |
| side-light | `wp-daylighting-architecture` | ✅ / true | Daylighting (architecture) / Wikipedia | 权威百科 | true | 直接（采光＝布置窗/天窗；高纬冬日入射“highly directional and casts long shadows”） |
| color-scheme | `wp-color-theory` | ✅ / true | Color theory / Wikipedia | 权威百科 | true | **直接**（明列 color schemes / color harmony / analogous / complementary） |
| color-scheme | `wp-color-wheel` | ✅ / true | Color wheel / Wikipedia | 权威百科 | true | **直接**（“a color scheme is the choice of colors used in design”；monochromatic/analogous/complementary） |

> 关键事实：三条 `sources` 数组长度与 `coverage.source_count` 一致（各 2=2）。6 源均 `year=null`（在线百科条目，D06 允许）；`wp-rembrandt-lighting` 的 `link_ok=null` 为来源库独立字段（D11），不影响 verified，本轮已实抓 200。**无死链、无假 id、无 verified=false 被引用。**

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 five-tones（明暗五调子）——**待核实**
- **wp-chiaroscuro**（owiki 镜像 HTTP200 29968B，h1「Chiaroscuro」）：
  - “the effect of light modelling … where **three-dimensional volume is suggested by the value gradation of colour and the analytical division of light and shadow shapes**—often called **‘shading’**.”（“以明暗层次塑造体积/明暗分区”直证——支持 overview 的“归纳明暗、表现立体”）
  - “Chiaroscuro **originated in the Renaissance period** but is most notably associated with **Baroque** art.”；“…as did Delacroix and others in the **nineteenth century**.”（时间下限 Renaissance / Baroque / 十九世纪确有出现，勉强覆盖 time_or_place 的“文艺复兴至19世纪”）
  - **关键缺口：全文检索 `five`、`five tones` 均 NOT FOUND**；文章只讲“value gradation / analytical division of light and shadow shapes”，**从未列举“高光、亮部、明暗交界线、反光与投影”这五个层次**。
- **wp-rembrandt-lighting**（HTTP200 15358B，h1「Rembrandt lighting」）：仅描述“an illuminated **triangle under the eye** … the interaction of shadows and light, also known as **chiaroscuro** … geometric form”，**同样未提“五调子/五档”**。
- **逐项结论**：
  - definition“明暗五调子指高光、亮部、明暗交界线、反光与投影五个明暗层次”——**五档枚举为素描/绘画教学术语（领域正确），但两个引用来源正文均未出现该五分法与这五个名称，属“来源未支撑的细节精确化”**，非编造（无杜撰人名/年份/引文），但按硬性规则应落入「待核实」而当前未落。
  - overview“把连续明暗归纳为五档，便于观察与表现立体”——“归纳明暗/表现立体”有支撑（value gradation + volume）；**“五档”这一具体数目无源文支撑**。
  - time_or_place“文艺复兴至19世纪、欧洲”——Renaissance/Baroque/19th 均见于源文，**可接受**（“至19世纪”为宽范围概括）。
- **实例核对**：`实例`＝“名称：球体五调子练习（**类型性描述**）；地点与作者不适用。观察交界线最实处与反光的最亮处。”**未点名具体作品、人名或年份 → 无编造风险**；`needs_verification=true`、`pending_notes` 与「待核实」一致（但「待核实」只提“具体实例待补充”，**未覆盖上面的定义五分法缺口**）。
- **判定：待核实**——非编造、非假源，但 definition/overview 的核心“五档”分解**缺引用来源正文支撑**，建议补一条绘画理论/素描教学权威来源，或把该术语来源缺口写入「待核实」。附带 Minor：`wp-rembrandt-lighting` 对本条仅间接相关；SVG 与本条内容脱节（见 §五）。

### 3.2 side-light（侧面光）——**合格（Minor）**
- **wp-architectural-lighting-design**（owiki 镜像 HTTP200 37197B，h1「Architectural lighting design」）：
  - “**Wall grazing fixture: Light is closely placed to wall, typically to enhance a textured surface.**”（**“贴近墙面掠射以强化纹理质感”直证**——直接支撑 definition 的“最能把表面质感拉出来”与 原理“凸起迎光、凹陷背光，质感与起伏被放大”）
  - “…the relative **distribution and direction of travel for the light** so as not to cause unnecessary **glare**.”（佐证方向性与眩光限制）
- **wp-daylighting-architecture**（HTTP200 44260B，h1「Daylighting (architecture)」）：
  - “Daylighting is the practice of **placing windows, skylights, other openings, and reflective surfaces** so that direct or indirect sunlight can provide effective internal lighting.”（侧窗采光＝侧面来光的情境支撑）
  - “At higher latitudes during midwinter, **light incidence is highly directional and casts long shadows**.”（方向性入射与长投影＝明暗各半/凹凸落影的物理支撑）
- **逐项结论**：
  - definition“侧面光从约九十度横向打来，凸处迎光、凹处落影，最能把表面质感拉出来”——“掠射/方向性光凸显质感与起伏”有**直接支撑**；“**约九十度**”这一精确角度为摄影/布光常识的概括，源文无逐字数字。
  - overview“明暗各半、戏剧性强，适合表现纹理与体积，暗部需补光”——“表现纹理/体积”有支撑（textured surface / volume）；“明暗各半/戏剧性强/补光”为布光通识，源文无逐字。
- **实例核对**：`实例`＝“名称：侧光下的砖墙质感（**类型性描述**）；地点与作者不适用。看灰缝的凹凸被拉出。”**无具名、无年份 → 无编造**；`needs_verification=true`／`pending_notes`／「待核实」三者逐字一致。
- **判定：合格**——概念有直接来源支撑，仅精确角度/戏剧性措辞属概括性发挥（Minor）。

### 3.3 color-scheme（配色方案）——**合格（Minor）**
- **wp-color-wheel**（owiki 镜像 HTTP200 22959B，h1「Color wheel」）：
  - “In color theory, **a color scheme is the choice of colors used in design for a range of media**.”（**定义直证**：配色方案＝为设计选定的一组颜色）
  - “An **analogous** color scheme is made up of colors next to each other … **Monochromatic** colors are different shades of the same color … **Complementary** colors are two colors directly across from each other.”（**overview“单色、类比或互补组织”强直证**）
- **wp-color-theory**（HTTP200 36521B，h1「Color theory」）：
  - “traditional color theory … color mixing, color contrast effects, **color harmony, color schemes** and color symbolism”（配色/色彩和谐直接在场）
  - “…juxtapositions of **complementary** color will produce strong contrast … while others believe juxtapositions of **analogous** colors will elicit a positive aesthetic response.”（互补/类比的组织逻辑第二源同证）
- **逐项结论**：
  - definition“配色方案指按一定关系选定的主色、辅色与点缀色的组合”——“选择的一组颜色/按关系组织”有**强支撑**；“主色/辅色/点缀”三分是设计常识的细化，源文用“choice of colors”表述、未逐字拆三分。
  - overview“决定画面的统一与重点，可按单色、类比或互补组织”——**强直证**（monochromatic/analogous/complementary）。
- **实例核对**：`实例`＝“名称：以蓝为主色的室内配色（**类型性描述**）；地点与作者不适用。看主辅色的面积搭配。”**无具名、无年份 → 无编造**；三者逐字一致。
- **判定：合格**——定义与概述均有直接/强来源支撑（Minor：“主/辅/点缀＋面积比例”为设计常识细化，源文未逐字，可补设计类来源使链条更完整）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified**：6 个来源 id **全部存在、全部 verified=true**（见 §二表），`year=null`（D06 允许）。
- **相关性**：`wp-chiaroscuro`（明暗造型/阴影分区）与 `wp-color-theory`/`wp-color-wheel`（配色方案定义与单色/类比/互补）为**直接支撑**；`wp-architectural-lighting-design`（wall grazing：强化纹理表面）与 `wp-daylighting-architecture`（侧窗采光、方向性入射与长影）为**直接支撑**；`wp-rembrandt-lighting` 对 five-tones 为**相关但间接**（只述伦勃朗三角与 chiaroscuro，未列五调子）。六个标题均与各自主题直接相关，无泛论伞源。
- **可达性（本轮实抓，全部 HTTP 200）**：`en.wikipedia.org` 六篇 canonical 均超时 → 经 owiki 同源镜像 **6/6 HTTP 200**（Chiaroscuro 29968B / Rembrandt lighting 15358B / Architectural lighting design 37197B / Daylighting 44260B / Color theory 36521B / Color wheel 22959B）。**6 个来源 id 全部可达，无死链。**

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含“示意图，非施工图” | SVG 元素出界 | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| five-tones | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界（程序化核验） | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| side-light | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |
| color-scheme | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含“示意图，非施工图”；逐元素（circle/ellipse/line/text 的 cx±r、cy±r、x/y 坐标）程序化核验**无出界**；「常见错误与限制」段均以规范提示收尾。**机械项三条全部通过。**
>
> **但存在“图—文脱节 + 图示同质化”缺陷（Minor～Medium，非机械项判负，需定向整改）**：
> 1. **`five-tones` 与 `side-light` 的 SVG 字符串逐字相同**（同一个“光源圆→虚线→椭圆『形体与明暗』”的通用模版）。`five-tones` 的「一图」说明为“由高光到投影的五档”，但该 SVG **并未画出五个明暗层次**；`side-light` 的「一图」说明为“光源来自一侧、明暗各半”，该 SVG 也**未表现左右明暗各半**。**图与各自解说词直接不符。**
> 2. `color-scheme` 的 SVG（大圆 r120 + 三个小圆，其中一个填充 accent-soft）与「一图」说明“主色、辅色与点缀的配比”**大体对应但不精确**（未示面积比例/主辅层级）。
> 3. 该缺陷与第32轮已记的“本批 SVG 大量复用两套模版”同类，说明**图示去同质化仍未落实**。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**；`source_count` 与来源数组长度**一致**（各 2=2）；`needs_verification_count`：各 1/true。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| five-tones | **true** | 「明暗五调子」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓ |
| side-light | **true** | 「侧面光」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓ |
| color-scheme | **true** | 「配色方案」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓ |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 全部 True）；三条 `related` 均为空数组（无悬空引用）。
> **注意**：如上 §3.1 所述，five-tones 的「待核实」**只声明了“具体实例”缺口，未声明“五调子五分法本身无引用来源支撑”的缺口**——即 `needs_verification` 与正文声明虽“互相一致”，但**均未覆盖真实存在的来源支撑缺口**，属“联动一致但内容不完整”，已在 §3.1 判为待核实。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54；全库 161 条；口径②=全字段-不含 SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| five-tones | **0.3867** vs chiaroscuro | <0.54 ✓ | **0.4144** vs core-shadow | <0.54 ✓ |
| side-light | **0.3946** vs top-light | <0.54 ✓ | **0.4503** vs back-light | <0.54 ✓ |
| color-scheme | **0.3770** vs value | <0.54 ✓ | **0.4321** vs openness | <0.54 ✓ |

> **三条两档全部 <0.54，无套话超标。** 最近邻多落在**同批 sibling 条目**（five-tones→core-shadow、side-light→back-light、color-scheme→value/openness 等），反映本批条目模板化程度偏高但**尚未越线**。
>
> **补充：batch-33 批内 12 条两两相似度**（口径②全字段）最高为 **reflected-light vs side-light＝0.4650**（short 0.4324），次高 light-shadow-modeling vs core-shadow＝0.4572、side-light vs back-light＝0.4503，均在 0.54 以下；即整批 new-entry 之间**无套话越线**，不触发 AUTONOMOUS §E“相似度过高→整批降级”。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **five-tones（明暗五调子）** | overview“归纳明暗/表现立体”✓（value gradation/volume）；time✓（Renaissance/Baroque/19th 见源）；**definition“五档枚举”×无源文支撑（两源均 NOT FOUND “five”）；实例＝类型性描述无具名/年份→不编造** | 2/2 true；chiaroscuro 直接、rembrandt 间接相关 | 七节齐、SVG✓（但图与解说脱节）、风险✓ | 全部一致；但「待核实」未覆盖五分法缺口 | 0.387 / 0.414 | **待核实**（无编造；建议补绘画理论源或扩写待核实） |
| **side-light（侧面光）** | definition✓（wall grazing 强化纹理＋directional daylight 长影，概念直证）；overview✓（纹理/体积）；“约九十度/明暗各半”为概括（Minor）；实例＝类型性描述无具名/年份→不编造 | 2/2 true；两源均直接 | 七节齐、SVG✓（但图与解说脱节）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致 | 0.395 / 0.450 | **合格**（Minor：精确角度/戏剧性措辞；SVG 与 five-tones 同模版脱节） |
| **color-scheme（配色方案）** | definition✓（color scheme=choice of colors）；overview✓（monochromatic/analogous/complementary 强直证）；“主/辅/点缀＋比例”为设计常识细化（Minor）；实例＝类型性描述无具名/年份→不编造 | 2/2 true；两源均直接 | 七节齐、SVG✓（配比略粗）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致 | 0.377 / 0.432 | **合格**（Minor：三色/面积比例为设计常识，源文未逐字） |

- **内容与来源维度**：**2 合格 + 1 待核实 + 0 不合格**。definition/time_or_place/overview 多数有直接或强支撑；实例三条均为**类型性描述**、无具名作品/作者/年份；**硬性“编造年份/人名/引文/出处”0 条、假第二源 0 条、死链 0 条**。唯一实质缺口在 **five-tones 的“五档”分解无引用来源正文支撑**（属来源未支撑的细节精确化，非编造，应落「待核实」）。
- **结构与元数据维度**：三条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”且无出界、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 三条**逐字一致**；`check.py` PASS 0 errors。但**图示同质化（five-tones≡side-light 逐字同图）且图文不符**，为需整改的质量缺陷。
- **相似度维度**：三条两档全部 <0.54（短文本最大 0.3946、全字段最大 0.4503），批内 12 条两两最高 0.4650，亦 <0.54，**无套话异常**。

## 九、总体结论与是否建议整批返工

- **抽样结果**：3 条中 **2 条合格（side-light、color-scheme）+ 1 条待核实（five-tones）+ 0 条不合格**；**内容/来源/编造维度：0 编造、0 假第二源、0 死链**。
- **来源层面**：6 个引用来源 id 全部存在、verified=true、主题相关（定义/概述/实例有直接或强支撑）；6 个 URL 实抓（owiki 同源镜像）**全部 HTTP 200，无死链**。
- **结构/治理层面**：七节/SVG/规范提示机械项全过、元数据与 pending 联动三条**逐字一致**、`check.py` PASS 0 errors；但图示**同质化＋图文脱节**需整改。
- **相似度层面**：三条两档全部 <0.54（最高全字段 0.4503），批内两两最高 0.4650，**无套话越线**。
- **是否建议整批返工**：**不建议整批返工。** 依据：①源核对维度**不合格 0 条、编造 0、假第二源 0、死链 0**——按 AUTONOMOUS §E，“不合格则整批返工”针对的是**源核对不合格/编造/假源**，本轮为 0，不触发；②三条七节/元数据/`check.py` 全部通过；③相似度全部 <0.54，异常监控未越线。five-tones 属“**待核实**”（来源未支撑的细节，而非编造），按项目规则应由补源/补待核实解决，不构成整批返工理由。
- **必须的定向整改（不触发整批返工，但建议在下一轮优先处理，并写入 BACKLOG）**：
  1. **five-tones 补源或扩「待核实」**：`明暗五调子（高光/亮部/明暗交界线/反光/投影）` 的五分法为素描教学术语，所引 `wp-chiaroscuro`/`wp-rembrandt-lighting` 正文均未列举；建议补一条绘画理论/素描教学权威来源，或把“五调子分法来源待补充”写入该条「待核实」并同步 `pending_notes`。
  2. **图示去同质化＋修图文脱节**：`five-tones` 与 `side-light` 现为**逐字相同的通用 SVG**，且与各自「一图」说明（“由高光到投影的五档” / “光源来自一侧、明暗各半”）不符；建议分别重绘贴合本条概念的示意图，并核对 `color-scheme` 的“主辅点缀配比”图。
  3. **`wp-rembrandt-lighting` 的 `link_ok` 字段补录**（当前 null；本轮实抓 200 可达），使来源库三态完整。
- **流程记录**：本轮抽检 2/3 合格、1 待核实、0 不合格、0 编造、无套话越线；按 §E **不因“不合格”提至 25%**；鉴于 five-tones 待核实，建议下轮抽检仍**对 batch-33 其余 9 条做一次针对性来源复核**（尤其 `light-shadow-modeling`/`cast-shadow`/`highlight`/`reflected-light`/`core-shadow` 同套明暗术语是否也存在“五调子/明暗分区”类无源具体化），以确认待核实是否蔓延。

---

### 机器可读汇总

```
ROUND=33
SAMPLER=spotcheck-r33
SCOPE=["five-tones","side-light","color-scheme"]
FILES={"five-tones":"entries/batch-33.json","side-light":"entries/batch-33.json","color-scheme":"entries/batch-33.json"}
STATE={"sources.json":"120373B@23:47:23 (git-unmodified)","batch-33.json":"24904B@23:54:27","coverage.json":"83317B@23:54:19","total_written_entries":161,"scope_total":246,"files":21}
GIT_HEAD="3c17f10 feat: round32 twelve entries - Chinese painting techniques and space"; GIT_STATUS="dirty: M coverage.json; ?? entries/batch-33.json; ?? tools/add_round33.py (round33 not yet committed)"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia TIMEOUT -> owiki.org mirror HTTP200; 6/6 sources HTTP200; no temp files written"
FETCH={
 "wp-chiaroscuro":"OWIKI 200 29968B h1 Chiaroscuro; 'three-dimensional volume is suggested by the value gradation of colour and the analytical division of light and shadow shapes ... shading'; 'originated in the Renaissance ... Baroque'; 'nineteenth century'; 'five' NOT FOUND",
 "wp-rembrandt-lighting":"OWIKI 200 15358B h1 Rembrandt lighting; 'illuminated triangle under the eye ... chiaroscuro ... geometric form'; no five-tone enumeration",
 "wp-architectural-lighting-design":"OWIKI 200 37197B h1 Architectural lighting design; 'Wall grazing fixture: Light is closely placed to wall, typically to enhance a textured surface'; 'direction of travel ... glare'",
 "wp-daylighting-architecture":"OWIKI 200 44260B h1 Daylighting (architecture); 'placing windows, skylights ... direct or indirect sunlight'; 'light incidence is highly directional and casts long shadows'",
 "wp-color-theory":"OWIKI 200 36521B h1 Color theory; 'color harmony, color schemes'; 'complementary ... strong contrast; analogous ... positive aesthetic response'",
 "wp-color-wheel":"OWIKI 200 22959B h1 Color wheel; 'a color scheme is the choice of colors used in design for a range of media'; 'analogous ... Monochromatic ... Complementary'"
}
SOURCES={"count_distinct":6,"all_exist":true,"all_verified_true":true,"all_urls_reachable_200":"yes (owiki mirror)","note":"wp-rembrandt-lighting link_ok=null in lib but reachable 200"}
BODY_SUPPORT={
 "five-tones":"overview(归纳明暗/表现立体)✓ via value gradation+volume; time(Renaissance/Baroque/19th)✓; definition 五档枚举(高光/亮部/明暗交界线/反光/投影) NOT in either cited source ('five' NOT FOUND) => UNSUPPORTED SPECIFICITY, not fabrication; instance=type-description honest; VERDICT=待核实 (recommend add drawing-theory source or extend 待核实)",
 "side-light":"definition✓ via wall grazing (enhance textured surface) + directional daylight (long shadows); '约九十度/明暗各半' approximated (Minor); instance=type-description honest; VERDICT=合格",
 "color-scheme":"definition✓ (color scheme=choice of colors); overview✓ strong (monochromatic/analogous/complementary); '主/辅/点缀+比例' design elaboration (Minor); instance=type-description honest; VERDICT=合格"
}
L2_CHECK={"seven_sections":"definition+6/6 x3, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, no overflow (programmatic)","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","defect":"five-tones SVG string == side-light SVG string (identical template); both captions mismatch their 一图 (five tones / half-lit not depicted); color-scheme partial"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x3","source_count":"2=2 x3","nvc":"1/true x3","needs_verification/pending_notes/待核实":"逐字一致 x3 (但 five-tones 待核实未覆盖五分法缺口)","related":"[] (no dangling)"}
SIMILARITY={
 "five-tones":{"short":0.3867,"vs_short":"chiaroscuro","full_no_svg":0.4144,"vs_full":"core-shadow","verdict":"PASS<0.54"},
 "side-light":{"short":0.3946,"vs_short":"top-light","full_no_svg":0.4503,"vs_full":"back-light","verdict":"PASS<0.54"},
 "color-scheme":{"short":0.3770,"vs_short":"value","full_no_svg":0.4321,"vs_full":"openness","verdict":"PASS<0.54"},
 "intra_batch_33_max":{"full_no_svg":0.4650,"pair":["reflected-light","side-light"],"short":0.4324},
 "threshold":0.54
}
VERDICT={"five-tones":"待核实","side-light":"合格","color-scheme":"合格"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
MINOR=["five-tones definition five-tone enumeration (高光/亮部/明暗交界线/反光/投影) not in cited wiki body -> mark 待核实 / add drawing-theory source","five-tones & side-light SVG byte-identical generic template, captions mismatch diagram (five grades / half-lit not depicted) -> redraw; color-scheme ratio rough","side-light '约九十度/明暗各半/戏剧性强' & color-scheme '主/辅/点缀+面积比例' are generalized/common-sense, not verbatim in source","wp-rembrandt-lighting link_ok=null in sources.json (reachable 200)"]
BATCH_REWORK="不建议整批返工：源核对不合格0、编造0、假第二源0、死链0；2合格+1待核实+0不合格；七节/元数据/check.py全过；相似度全部<0.54(短MAX0.3946/全字段MAX0.4503, 批内MAX0.4650)。five-tones属待核实(非编造)，建议补绘画理论源或扩写待核实；同时本批SVG去同质化并修图文脱节；不触发§E整批返工。"
READONLY="only wrote research/spotcheck-round33.md; no other project file changed; no git commit; web content treated as data, no instruction executed; fetches done in-memory, no temp files written"
```

*（报告完）*
