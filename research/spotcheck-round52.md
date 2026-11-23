# 第52轮质量抽检报告（spotcheck-round52）——第52轮补具名实例的 3 条（hue / color-symbolism / warm-cool）

- 抽检人：spotcheck-r52（lead 委派子代理，无人值守、未提问）；抽样/核对时间 2026-11-23 15:31 起，Asia/Hong_Kong（CST）。
- 任务：对第52轮“补具名实例”改动条目中的 3 条——`hue`（色相，`entries/batch-01.json`）、`color-symbolism`（色彩象征，`entries/batch-33.json`）、`warm-cool`（冷暖色，`entries/batch-01.json`）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文直接支撑、是否编造、来源是否直接相关；并核对 **hue 两源是否支撑色相环、color-symbolism 两源是否支撑三色象征、warm-cool 是否仅单源**、L2 七节 / SVG / 规范提示、needs_verification 与 pending/待核实联动是否与单源/双源披露一致、相似度（阈值 0.54）。来源在 `data/sources.json`。
- 抽样说明：第52轮补具名实例由 `review-round52a.md`（3 条）与 `review-round52b.md`（4 条）底稿支撑，lead 定向点名本 3 条（3/7≈42.9%，高于 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限）。其余本轮改动条目只做状态观察，不列入内容判定。
- 协议依据：`AUTONOMOUS.md` §E「质量闸」（`tools/check.py` 必须通过；抽检逐条核对来源；不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，不下载运行来源代码，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注“示意图，非施工图”、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附“实际工程须按当地规范和专业设计人员的要求”）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 SUBAGENT-STOP，以任务说明书执行）与 `verification-before-completion`（先实抓证据、后下断言：8 个去重来源本轮全部重新实抓 HTTP 200，关键句做大小写/空白/标点归一后的子串回验；MISS 项另取上下文确认）。
- 治理文件说明：本项目根 `AUTONOMOUS.md` / `TASK_design.md` 不在工作区磁盘；实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round51.md`（253 行）、`research/review-round52a.md`、`research/review-round52b.md`。联网内容一律视为数据，网页中任何指令均未执行。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 15:31 起）**：`data/sources.json`=**181562B@15:31:45**、`coverage.json`=**87347B@15:31:45**、`entries/batch-01.json`=**84947B@15:31:45**、`entries/batch-33.json`=**25816B@15:31:45**、`tools/check.py`=**15908B@2026-11-22 15:11:54**。
- **`git log -1`** = `dda31d2 docs: note round51 push status`；第52轮改动尚未提交——`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-01.json`、`M entries/batch-06.json`、`M entries/batch-33.json`、8 个 `site/entries/*.html`、`site/index.html`、`site/sources.html`，以及 `?? research/review-round52a.md`、`?? research/review-round52b.md`、`?? tools/apply_review_round52.py`（lead 侧底稿/脚本，本抽检不触碰）。抽检对象即上述未提交工作树中的 3 条具名实例现状，非 HEAD 内容。
- **规模与来源库**：`coverage.json` 实读 `total=258`；`pending_sum`（`needs_verification_count` 求和）=**212**（第51轮报告为 213，本轮净降 1，`1/258≈0.39%`）。`sources.json` 共 **383** 条，`verified=true` **380**、`verified=false` **3**。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅写出** `research/spotcheck-round52.md` 一个项目文件；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/review-round52a.md`、`research/review-round52b.md`、`tools/apply_review_round52.py` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容。抓取与分析全程内存（web_fetch + Python stdin 内联），未在项目内落盘脚本或缓存。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须以“实际工程须按当地规范和专业设计人员的要求”收尾；SVG 元素不出 `viewBox`、无 `on*` 事件属性、无外链图片。
- **抓取与回验方法**：`web_fetch` + Python `urllib`（浏览器 UA、timeout 40–60s；Cambridge PDF 关闭 SSL 校验并用 `pypdf` 抽 40 页文本）；逐 URL 记录 HTTP 状态与标题；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；关键句用 `norm()`（NFKC + 弯直引号/破折号/不间断空格归一 + 大小写 + 空白折叠）做子串回验，未命中项再取上下文人工判读。**8 个去重来源本轮全部实抓 HTTP 200**。
- **三级判定定义（沿用第51轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一直接相关来源实质支撑，但某关键事实（核心概念/实例四要素/年份/具体内容映射）实质单源，或第二源对具体表述零覆盖/只作旁证；或 pending 联动与来源实况不一致——属来源深度或披露缺陷，非编造。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入），归一为去空白+小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–51轮报告逐位一致，口径正确。
- **相似度是独立维度**：超线触发 §E「相似度过高（疑似套话）→整批降级」，与“不合格（内容无源）→整批返工”是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

3 条共引用 **8 个去重来源 id（11 处引用：hue 4、color-symbolism 4、warm-cool 3）**，全部存在、全部 `verified=true`、全部 `year=null`（D06 允许）、实抓 8/8 HTTP 200。

| 条目 | 来源 id | 机构 / type | 实抓标题或端点（本轮 HTTP 200） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| hue | `wp-hue` | Wikipedia / 权威百科 | `Hue - Wikipedia` | true / true | **相关（直接·定义）**：`hue is one of the properties`、`angular position ... color wheel`、`saturation / lightness` |
| hue | `wp-color-theory` | Wikipedia / 权威百科 | `Color theory - Wikipedia` | true / true | **相关（直接·定义/手法）**：`value (lightness), chroma (saturation), and hue`；类比/互补配色 |
| hue | `royalsociety-colour-wheel` | Royal Society / 官方机构 | `Colour wheel \| Royal Society` | true / null | **相关（直接·强·实例）**：`first colour wheel`、`Opticks (1704)`、`seven spectral colours into a circle of unequal segments` |
| hue | `mollon-colour-science` | University of Cambridge / 学术著作 | `The Origins of Modern Color Science`（PDF，40 页） | true / null | **相关（直接·强·实例+色相环）**：`seven principal colors of the spectrum`、`Newton's color circle, introduced in his Opticks of 1704`、`same hue but will vary in saturation` |
| color-symbolism | `wp-color-theory` | Wikipedia / 权威百科 | `Color theory - Wikipedia` | true / true | **相关（直接·定义/overview）**：`colors carry significant cultural symbolism`、`culture-bound and may also vary across different contexts` |
| color-symbolism | `wp-theory-of-colours` | Wikipedia / 权威百科 | `Theory of Colours - Wikipedia` | true / true | **相关（直接·定义旁证）**：`allegorical, symbolic, mystic use of colour`；歌德颜色—品质对应 |
| color-symbolism | `libretexts-romanticism` | LibreTexts / 学术著作 | `11.2: Romanticism (1780-1850) - Humanities LibreTexts` | true / null | **相关（直接·强·三色象征）**：`blue, white, and red colors symbolize liberty, equality, and fraternity`；德拉克洛瓦全画策略性用色 |
| color-symbolism | `centv-liberty` | CETV / 学术著作 | `博物馆之夜-【云逛卢浮宫】《自由引导人民》_CETV` | true / null | **相关（直接·实例/一般象征）**：`蓝、白、红三色旗是法国国旗，是1789年法国大革命的象征`；作品成为“象征为自由而奋斗的标志”；**未逐字给出“自由、平等、博爱”三元映射，亦无 RF 129** |
| warm-cool | `wp-color-theory` | Wikipedia / 权威百科 | `Color theory - Wikipedia` | true / true | **相关（直接·强·概念/原理/overview）**：`Warm vs. cool colors` 专节；`warm colors ... advance ... cool colors tend to recede`；arouse/calm |
| warm-cool | `wp-theory-of-colours` | Wikipedia / 权威百科 | `Theory of Colours - Wikipedia` | true / true | **部分相关（概念旁证）**：`yellow ... warm`、`blue ... shadows`、`allegorical, symbolic`；全文 `cool`=0、`warm`=1 |
| warm-cool | `ng-temeraire` | National Gallery / 官方机构 | `Joseph Mallord William Turner \| The Fighting Temeraire \| NG524 \| National Gallery, London` | true / null | **相关（直接·强·实例单源）**：`Joseph Mallord William Turner, 'The Fighting Temeraire', 1839`、`whites, oranges, yellows, and browns giving way to hazy blues, purples, and pinks` |

> 8 源全部 `verified=true`，无假 id；`link_ok=null` 仅表示三态未标（非死链）。**关键相关性结论**：hue 的皇家学会 + Mollon 两源直证牛顿色环；color-symbolism 的 LibreTexts 直证三色三元映射，CETV 直证作品/三色旗的一般象征但未直证三元映射；warm-cool 的具名作品与暖→冷色列仅 `ng-temeraire` 一源直证。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 hue（色相，第52轮改动）——**合格（附需注意项）**

- 条目现状（实读 `entries/batch-01.json` 842–874 行）：`definition`＝“色彩借以区分种类的属性。”；`time_or_place`＝“跨时期、全球（参见来源）。”；`overview`＝“色相是色彩循环秩序的基础，与明度、纯度共同描述颜色。”；`实例`＝“名称：牛顿色环图（Newton's colour wheel）；地点：英国伦敦（皇家学会藏品与研究）；设计者：艾萨克·牛顿（Isaac Newton）；年份：1704 年前后（《光学》时期）。以圆周排布七种光谱色表示色相。…”
- **definition 双源直证**：`wp-hue` 命中 `hue is one of the properties (called color appearance parameters) of a color` 与 `angular position ... on a color wheel`；`wp-color-theory` 命中 `Munsell's 1905 color system represents colors using three color-making attributes, value (lightness), chroma (saturation), and hue`。→ “区分种类的属性 / 与明度、纯度共同描述颜色”双源互证，非编造。
- **time_or_place「跨时期、全球」**：色彩属性的通识范围，无具体年代/地点断言需直证，可接受。
- **overview 支撑**：`wp-hue` 明记色相可由色轮上的角位置表示、其余外观参数为 `saturation / lightness`；`wp-color-theory` 明记 hue/chroma/value 三属性；Mollon PDF 明记 `will all exhibit the same hue but will vary in saturation`。→ “循环秩序 + 与明度纯度共同描述”获三源支撑。
- **原理/典型手法支撑**：`royalsociety-colour-wheel` 的 `Newton set the seven spectral colours into a circle of unequal segments` 与 Mollon 的 `On the circumference of a circle ... each of the seven principal colors of the spectrum` 直证“色轮上按光谱顺序排列”；`wp-color-theory` 的 `analogous colors ... single-hued or monochromatic` 与 `juxtapositions of complementary color will produce strong contrast` 支撑“邻近色协调 / 对比色焦点”。
- **hue 两源是否支撑色相环——是，双源强直证**：
  - Royal Society：「`which included the first colour wheel`」「`Newton set the seven spectral colours into a circle of unequal segments, based on the pattern of musical scale, and created a geometric model which underpins all subsequent theory on colour harmony`」。
  - Mollon PDF：「`On the circumference of a circle (Figure 1.2) he represents each of the seven principal colors of the spectrum.`」「`Figure 1.2 Newton's color circle, introduced in his Opticks of 1704.`」「`Colors that lie on a line connecting the center with a point on the circumference will all exhibit the same hue but will vary in saturation.`」。
  - → 名称、设计者、年份、七色圆周排布与“色相作为可环绕排列维度”均由两独立机构直证，贴合度高。
- **实例四要素核对**：名称（Royal Society `first colour wheel` + Mollon `Newton's color circle`）✓双源；设计者（Newton，两源一致）✓双源；年份（两源均直书 1704，条目写“1704 年前后”）✓双源但措辞更保守；地点“英国伦敦（皇家学会藏品与研究）”为机构/出版语境推断——两源正文未直书出版地 London，Royal Society 页面以机构身份与目录链接提供语境，**属需注意项而非编造**（建议改“英国皇家学会《光学》图版（1704）”或补目录页入 sources）。
- **无编造**：核心定义、色相环、作者、年代、七色圆周均由来源正文直证；不复制图像。
- **内容判定：合格**。需注意两项（地点推断、年份“前后”可收紧为 1704）均非关键事实断裂，不影响判定。

### 3.2 color-symbolism（色彩象征，第52轮改动）——**待核实**

- 条目现状（实读 `entries/batch-33.json` 336–366 行）：`definition`＝“色彩象征指特定色彩在文化中被赋予的联想与含义。”；`time_or_place`＝“跨时期、全球（参见来源）。”；`overview`＝“同一色彩在不同文化中含义不同，需结合语境理解。”；`实例`＝“名称：《自由引导人民》（Liberty Leading the People）；地点：法国巴黎卢浮宫（RF 129）；设计者：欧仁·德拉克洛瓦（Eugène Delacroix）；年份：1830 年。画中蓝白红三色旗象征自由、平等、博爱。…”
- **definition / overview 双源直证**：`wp-color-theory` 命中 `A major underpinning of traditional color theory is that colors carry significant cultural symbolism ... connotative color associations and color symbolism tends to be culture-bound and may also vary across different contexts and circumstances`；`wp-theory-of-colours` 明记歌德色轮的 `allegorical, symbolic, mystic use of colour` 与红/橙/黄/绿/蓝/紫的品质对应。→ 定义与“因文化/语境而异”双源支撑，非编造。
- **来源直接相关**：四源均相关；LibreTexts 与 CETV 是具名实例的直接来源，两篇 Wikipedia 是概念来源。无假源、无死链。
- **color-symbolism 两源是否支撑三色象征——部分支撑，精确映射实质单源**：
  - **LibreTexts（直接·强）**：「`The flag's blue, white, and red colors symbolize liberty, equality, and fraternity, the ideals of the French Revolution.`」＋「`Delacroix used these colors strategically throughout the composition to direct the viewer's attention upward from the crowd to Liberty and the waving flag.`」→ **逐字直证“蓝白红＝自由、平等、博爱”三元映射**，并直证全画策略性用色。
  - **CETV（直接·一般）**：「`蓝、白、红三色旗是法国国旗，是1789年法国大革命的象征，后又成为法兰西帝国的象征。`」＋「`如今已成为象征为自由而奋斗的标志。`」→ 直证三色旗承载政治象征、作品为自由奋斗象征，**但未逐字给出“自由、平等、博爱”三元对应**。
  - → 两源共同支撑“三色旗在此画中承载象征”；但条目所写精确三元映射只有 LibreTexts 一源直证，第二源只作一般象征旁证。按 `TASK_design.md` 关键事实双源规则，属待核实级来源深度缺陷。
- **实例四要素核对**：名称/作者/年份/馆藏地由 LibreTexts 图注 `Eugène Delacroix, Liberty Leading the People (July 28, 1830), September - December 1830, oil on canvas, 260 x 325 cm (Musée du Louvre, Paris)` 与 CETV“1830 年七月革命 / 云逛卢浮宫 / 德拉克洛瓦”双源支撑；**但“RF 129”在两条引用源正文中均为 0 命中**（来自 `review-round52b.md` 的补充卢浮宫官方页，该页未进入本条 `sources`），属“引用源未支撑的具体馆藏号”。
- **无编造**：作品、作者、1830、卢浮宫、三色象征均为真实且获来源支撑；问题是三元映射单源直证与 RF 129 未在引用源中出现，属来源/披露缺陷，不判无源编造。
- **内容判定：待核实**（精确三色象征单源 + RF 129 无引用源支撑 + nv 已清零与来源实况不一致）。

### 3.3 warm-cool（冷暖色，第52轮改动）——**待核实（单源已如实披露）**

- 条目现状（实读 `entries/batch-01.json` 1012–1041 行）：`definition`＝“色彩给人的冷暖心理感受与倾向。”；`time_or_place`＝“跨时期、全球（参见来源）。；”`overview`＝“冷暖关系常用于组织空间前后层次与画面情绪。”；`实例`＝“名称：《被拖去解体的战舰无畏号》（The Fighting Temeraire）；地点：英国伦敦国家美术馆（NG524）；设计者：J.M.W. 透纳（J. M. W. Turner）；年份：1839 年。夕阳下由暖色白橙黄褐渐入冷色蓝紫粉。…”
- **definition / 原理 / overview 来源支撑**：`wp-color-theory` 的 `Warm vs. cool colors` 专节直证「`The distinction between "warm" and "cool" colors has been important since at least the late 18th century`、`warm colors ... advance or appear more active in a painting, while cool colors tend to recede`、`warm colors ... arouse or stimulate the viewer, while cool colors calm and relax`」；`wp-theory-of-colours` 提供歌德“黄色偏暖、蓝色与阴影相关”的感知旁证（全文 `cool`=0、`warm`=1，属部分相关）。→ 核心定义、空间前后与情绪组织获直接相关来源支撑；“红橙偏暖 / 蓝青偏冷”的具体色列主要由 `wp-color-theory` 一源直证，另一百科仅作旁证。
- **warm-cool 是否仅单源——是（指具名实例与暖→冷色列）**：
  - `ng-temeraire` 官方页是**唯一**直证作品四要素与色列的来源：标题含 `The Fighting Temeraire | NG524 | National Gallery, London`；目录行 `Joseph Mallord William Turner, 'The Fighting Temeraire', 1839`；正文「`The whole scene is bathed in colour as the sun sets – whites, oranges, yellows, and browns giving way to hazy blues, purples, and pinks.`」。
  - `wp-color-theory` / `wp-theory-of-colours` 支撑冷暖概念，但**均未提及该作品或该色列**；`review-round52a.md` 曾评估 Webexhibits《Color and Art》只作暖色概念旁证、非同作品，落地也未进入本条 sources。
  - → 条目 `pending_notes`「暖→冷色列由馆方单源直证，待补第二独立机构来源。」与来源实况**完全一致**。
- **无编造**：作品名称、作者、年份、NG524 与暖→冷色列均由国家美术馆官方页正文直证；无假 id、无死链。
- **内容判定：待核实**（关键实例事实单源；披露本身合格，不触发披露失真返工）。补第二独立机构源前，`needs_verification=true` 应维持。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：8 个去重来源 id 全部存在、全部 `verified=true`；`year=null`（在线动态页/无年份字段，D06 允许）；`link_ok`：3 源 true、5 源 null（三态未标，非死链）。无 `verified=false` 引用、无假 id。
- **可达性（本轮实抓）**：8/8 全部 HTTP 200。Royal Society 与 LibreTexts/CETV 经 `web_fetch` 与 Python 双通道确认；Cambridge PDF 经 Python + `pypdf` 抽 40 页确认；Wikipedia 三页与 National Gallery 官方页经 Python 正文抽取确认。
- **相关性结论**：
  - `hue`：4 源均直接相关；皇家学会 + Mollon 双源直证色相环，两个百科直证定义与三属性框架。
  - `color-symbolism`：4 源均相关；LibreTexts 直证三元映射，CETV 直证作品/一般象征但未直证三元映射；两百科直证概念。
  - `warm-cool`：`wp-color-theory` 直接强相关、`wp-theory-of-colours` 部分相关、`ng-temeraire` 直接强相关但仅此一源支撑作品与色列。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hue | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| color-symbolism | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| warm-cool | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含“示意图，非施工图”、无 `on*`、无 `<image>`/外链；「常见错误与限制」均以“实际工程须按当地规范和专业设计人员的要求”收尾；`check.py` PASS。**机械项三条全部通过。**

- **SVG 质量观察（形态贴合主题，但缺“设计意图/尺寸关系”标注——次要、系统性）**：
  - `hue`：横向色相序列框 + “色相序列”标注——贴合色相顺序；缺意图/尺寸关系显式标注。
  - `color-symbolism`：三圆关系图 + “示意图，非施工图”——只画关系，无“蓝/白/红”“自由/平等/博爱”或文化语境文字标注，主题贴合度低于另两条。
  - `warm-cool`：暖色区/冷色区两矩形并置——贴合冷暖分区；缺“前移/后退”等意图标注。
  - **判定**：机械项全过；唯一不足为缺 TASK_design 第6条“图中标注设计意图或尺寸关系”——`check.py` 查不出该语义项，属次要/可提升，建议全站统一补强（延续第44–51轮方向）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实（本轮重点）

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对）；`source_count` 与来源数组长度一致（4=4、4=4、3=3）；`needs_verification_count`：hue=0、color-symbolism=0、warm-cool=1；`related`：hue=`["value"]` 存在，color-symbolism 与 warm-cool 为空数组（无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| hue | false（本轮清零） | "" | “暂无已知待核实项。” | **结构一致 ✓、内容基本恰当 ✓**：核心定义与色相环双源直证、实例四要素除地点语境外均双源；清零合理。需注意地点推断/年份措辞，建议局部修正或补目录源。 |
| color-symbolism | **false（本轮清零）** | "" | “暂无已知待核实项。” | **结构同向但内容失真 ✗**：精确三元映射单源直证、RF 129 未由引用源支撑；原待核实事项并未真正消除。应恢复 `needs_verification=true` 并据实写 pending/待核实，或补齐双源与馆藏号来源后再清零。 |
| warm-cool | true（保持） | “暖→冷色列由馆方单源直证，待补第二独立机构来源。” | 同左（逐字一致） | **结构一致 ✓、内容准确 ✓**：作品与暖→冷色列确为 NG 官方单源直证；nv 保持 true 与单源披露一致。 |

> **异常监控（§E）**：全库 `pending_sum` 由第51轮 213 降至本轮 **212**（-1，0.39%）。净降幅远低于“明显低于历史平均”的整批降级关注线；但 `color-symbolism` 这一条清零属个例误清——补了具名实例 ≠ 精确象征映射与馆藏号已获双源。建议定向回退该条 nv，而非整批处理。

## 七、任务 5：相似度（difflib 去空白+小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| hue | **0.4646** vs value | <0.54 ✓ | **0.4165** vs value | <0.54 ✓ |
| color-symbolism | **0.4390** vs material-color | <0.54 ✓ | **0.3916** vs hue | <0.54 ✓ |
| warm-cool | **0.4082** vs value | <0.54 ✓ | **0.3892** vs color-contrast | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。`hue` 短文本 0.4646 为三者最高（vs value，同属色彩理论近邻，正常）。

### 7.2 第52轮批内 3 条两两（全字段② / 短文本①）

- hue vs color-symbolism：全字段 **0.3851**、短文本 0.3621。
- hue vs warm-cool：全字段 **0.3427**、短文本 0.3810。
- color-symbolism vs warm-cool：全字段 **0.3758**、短文本 0.3304。
- → 批内两两均远低于 0.54，无套话/模板姊妹风险。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–51轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **hue（色相）** | definition/overview **wp-hue + wp-color-theory + Mollon 直证**；色相环由 **Royal Society + Mollon 双源强直证**（七谱色圆周、1704、Newton）；实例作者/年份/七色排列双源；地点“英国伦敦”为机构语境推断、年份“1704 年前后”较原文更保守；无编造 | 4/4 true；4 源直接相关；**4/4 200** | 七节齐、规范句✓；1 SVG 含“示意图，非施工图”、形态贴合，缺意图/尺寸标注（次要） | 全部一致；nv=false↔pending 空↔“暂无” 结构内容均恰当（附地点/措辞修正建议） | 全库 ✓（0.4646/0.4165）；批内 ✓ | **合格** |
| **color-symbolism（色彩象征）** | definition/overview 两百科双源直证；实例名称/作者/1830/卢浮宫双源；**“自由、平等、博爱”三元映射仅 LibreTexts 直证，CETV 只证一般政治象征**；**RF 129 未由本条引用源支撑**（来自未列入 sources 的卢浮宫官方页）；无编造 | 4/4 true；4 源相关；**4/4 200**；CETV 对三元映射仅一般旁证 | 七节齐、规范句✓；1 SVG 合规但缺色彩/文化文字标注、缺意图/尺寸标注（次要） | 元数据一致；但 **nv 由 true 错误清零**、pending 空、待核实“暂无”——**联动内容失真** | 全库 ✓（0.4390/0.3916）；批内 ✓ | **待核实** |
| **warm-cool（冷暖色）** | definition/原理/overview 由 `wp-color-theory` 强直证、`wp-theory-of-colours` 部分旁证；实例四要素与“暖白橙黄褐→冷蓝紫粉”色列 **NG 官方单源直证**；两百科不支撑该作品；无编造 | 3/3 true；`wp-color-theory` 直接、`wp-theory-of-colours` 部分、`ng-temeraire` 直接但单源；**3/3 200** | 七节齐、规范句✓；1 SVG 含“暖色区/冷色区”、形态贴合，缺意图/尺寸标注（次要） | 全部一致；nv=true↔pending↔待核实 三处同文且内容准确，单源披露恰当 | 全库 ✓（0.4082/0.3892）；批内 ✓ | **待核实** |

### 问题清单

- **① color-symbolism 三元映射实质单源（重点·判待核实主因）**：LibreTexts 逐字直证 `blue, white, and red colors symbolize liberty, equality, and fraternity`；CETV 只写三色旗为法国国旗/法国大革命与法兰西帝国象征、作品为自由奋斗象征，未逐字给出“自由、平等、博爱”。建议改写为“三色旗象征法国大革命理想（LibreTexts 逐项记为自由、平等、博爱；CETV 记为法国大革命/法兰西帝国象征）”，或补第二独立机构源直证三元映射。
- **② color-symbolism RF 129 无引用源正文支撑（重点）**：`libretexts-romanticism` 与 `centv-liberty` 对 `RF 129` 均 0 命中；该号来自 `review-round52b.md` 的补充卢浮宫官方页，但未进入本条 `sources`。建议把卢浮宫官方藏品页登记入 sources 并 `verified=true`，或从实例中删去该编号。
- **③ color-symbolism pending 联动失真（重点·须回退）**：`needs_verification` 由 true 清零为 false、pending 空、待核实“暂无”。但问题①②使原待核实事项并未消除；应恢复 `needs_verification=true` 并据实写 pending/待核实，或在补齐三元映射双源与馆藏号来源后再清零。
- **④ warm-cool 实例与色列单源（重点·披露恰当）**：NG 官方页单源直证《无畏号》四要素与暖→冷色列，两百科只证概念。当前 nv=true/pending 同文准确；补第二独立机构源前保持待核实，不建议清零。
- **⑤ hue 地点与年份措辞（轻微）**：“英国伦敦（皇家学会藏品与研究）”未由两源正文直书 London；两源均直书 1704，实例写“1704 年前后”较保守。建议改为“英国皇家学会《光学》图版（1704）”或补目录页入 sources，并把年份收紧为 1704。
- **⑥ 三图“设计意图/尺寸关系”标注缺失（系统性·次要）**：SVG 机械项与主题贴合均过，`color-symbolism` 图甚至未标色彩/象征文字；建议全站统一补强（延续第44–51轮方向）。
- **⑦ 来源 title 元数据简写（轻微）**：新增 8 源 title 多为简写记名（如 `Mollon: Colour Science — Cambridge PDF`、`卢浮宫名画《自由引导人民》 — CETV`），建议存实抓全名。

## 九、总体结论与建议

- **抽样结果**：第52轮补具名实例条目中抽检 3 条——`hue`、`color-symbolism`、`warm-cool`。**内容维度：1 合格（hue）＋2 待核实（color-symbolism、warm-cool）＋0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：8 个引用来源全部存在、`verified=true`、实抓 8/8 HTTP 200。hue 两源强直证牛顿色环；color-symbolism 的两源中 LibreTexts 直证三元映射、CETV 只作一般象征旁证，且 RF 129 未入引用源；warm-cool 的具名作品与暖→冷色列仅 NG 一源直证。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 唯一性与主题贴合通过、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：hue 清零恰当（附轻微措辞项）；warm-cool 保持 true 且披露准确；**color-symbolism nv 清零属个例误清**——把“补了具名实例”误当作“精确象征映射与馆藏号已获双源”。全库 pending_sum 213→212（-1，0.39%），非整批异常，但该个例须定向回退。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4646、全字段最高 0.4165）；方法自校 0.5157 与第39–51轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（1 合格 + 2 待核实），0 编造/假 id/死链。两条待核实均为来源深度/披露缺陷，非无源硬伤。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——pending_sum 净降 0.39%，非“明显低于历史平均”；但 color-symbolism 单条 nv 误清须修正。
  4. **结论：本轮 1 条合格、2 条待核实，不触发整批返工/降级。** 第52轮“补具名实例 + 补源”对 hue 成效显著（双源直证色相环、pending 可正当清零）；color-symbolism 是“补了实例但精确映射/馆藏号未补齐”；warm-cool 是“单源已如实披露”，两者均须定向修复。
- **返工/修复建议（定向、非整批）**：
  1. **（优先·问题①②③）`color-symbolism`**：恢复 `needs_verification=true` 并据实写 `pending_notes`/「待核实」；补一独立机构源直证“蓝白红＝自由、平等、博爱”三元映射，或把实例改写为“三色旗象征法国大革命理想（两源措辞分别标注）”；把卢浮宫官方藏品页登记入 sources 以支撑 `RF 129`，或删去该编号。修复齐备后再清零 nv。
  2. **（问题④）`warm-cool`**：保持 nv=true 与现有 pending；补第二独立机构源直证《无畏号》四要素与暖→冷色列后再清零。现有披露无需返工。
  3. **（问题⑤）`hue`**：保持合格；建议把“英国伦敦（皇家学会藏品与研究）”改为“英国皇家学会《光学》图版（1704）”或补目录源，年份收紧为 1704；nv=false 维持。
  4. **（问题⑥，系统性）**：三图（及全站）补「设计意图或尺寸关系」文字标注，尤其给 `color-symbolism` 图补色彩—象征对应文字。
  5. **（问题⑦）**：新增来源 title 存实抓全名。

### 机器可读汇总

```
ROUND=52
SAMPLER=spotcheck-r52
MODE=第52轮补具名实例条目中lead定向抽3条（hue / color-symbolism / warm-cool）
SCOPE=["hue","color-symbolism","warm-cool"]
FILES={"hue":"entries/batch-01.json","color-symbolism":"entries/batch-33.json","warm-cool":"entries/batch-01.json"}
GIT_HEAD="dda31d2"; ROUND52_COMMITTED=false; GIT_STATUS="round52 changes UNCOMMITTED as found (M coverage/data/sources/entries/batch-01/06/33 + site/*; ?? review-round52a/52b.md, apply_review_round52.py - lead notes, untouched)"
STATE={"sources.json":"181562B@2026-11-23 15:31:45","coverage.json":"87347B@15:31:45","batch-01.json":"84947B@15:31:45","batch-33.json":"25816B@15:31:45","check.py":"15908B@2026-11-22 15:11:54","total":258,"pending_sum":212,"sources_total":383,"sources_verified_true":380,"sources_verified_false":3}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/7 (42.9%, lead 定向抽检)"
FETCH_METHOD="web_fetch + urllib+ChromeUA + pypdf(Mollon 40p); 8/8 HTTP200; norm(quotes/dashes/nbsp/case/space) substring verify; analysis in-memory; no files written except this report"
SOURCES={"count_distinct":8,"count_refs":11,"all_exist":true,"all_verified_true":true,"all_reachable_200":"8/8",
 "hue":{"wp-hue":true,"wp-color-theory":true,"royalsociety-colour-wheel":true,"mollon-colour-science":true},
 "color-symbolism":{"wp-color-theory":true,"wp-theory-of-colours":true,"libretexts-romanticism":true,"centv-liberty":true},
 "warm-cool":{"wp-color-theory":true,"wp-theory-of-colours":true,"ng-temeraire":true},
 "relevance":{"hue":"4源直接相关；RS+Mollon双源直证色相环","color-symbolism":"LibreTexts直证三元映射；CETV仅一般象征旁证；RF129未入引用源","warm-cool":"wp-color-theory强相关；wp-theory-of-colours部分相关；ng-temeraire单源直证作品+色列"}}
BODY_SUPPORT={
 "hue":"definition/overview wp-hue+wp-color-theory+Mollon; 色相环 RS('first colour wheel'/'seven spectral colours into a circle of unequal segments')+Mollon('circumference...seven principal colors'/'Newton's color circle...Opticks of 1704'/'same hue but vary in saturation') 双源; 实例四要素除地点语境外双源; VERDICT=合格 (需注意: 地点London未正文直书; 1704年前后较原文保守)",
 "color-symbolism":"definition/overview 两百科双源; 实例四要素 LibreTexts+CETV 双源, 但'自由平等博爱'仅LibreTexts直证('blue, white, and red colors symbolize liberty, equality, and fraternity'), CETV只证一般政治象征; RF129 两引用源0命中(来自未入sources的Louvre官方页); VERDICT=待核实 (精确映射单源+馆藏号无引用源+NV误清)",
 "warm-cool":"definition/原理/overview wp-color-theory强直证('advance/recede','arouse/calm'); 实例四要素+暖白橙黄褐→冷蓝紫粉仅 ng-temeraire 单源('whites, oranges, yellows, and browns giving way to hazy blues, purples, and pinks'); 两百科不支撑该作品; VERDICT=待核实 (单源已如实披露, 保持nv=true)"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3, 无出界, 无on*/无外链图, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3"}
SVG_NOTE={"hue":"横向色相序列框+色相序列标注, topical","color-symbolism":"三圆关系图, 缺色彩/象征文字标注","warm-cool":"暖色区/冷色区并置, topical","verdict":"机械项全过; 三条均缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x3","source_count":"hue=4, color-symbolism=4, warm-cool=3","nvc":"hue=0, color-symbolism=0, warm-cool=1","needs_verification":"hue=true->false(恰当, 附轻微措辞项); color-symbolism=true->false(误清,须回退); warm-cool=true(保持, 披露准确)","related":"hue=[value]; color-symbolism=[]; warm-cool=[] 无悬空","pending_consistency":"hue结构内容一致; warm-cool单源披露准确; color-symbolism清零失真"}
SIMILARITY={
 "hue":{"vs_all_short":0.4646,"short_entry":"value","vs_all_full":0.4165,"full_entry":"value","verdict":"PASS<0.54"},
 "color-symbolism":{"vs_all_short":0.4390,"short_entry":"material-color","vs_all_full":0.3916,"full_entry":"hue","verdict":"PASS<0.54"},
 "warm-cool":{"vs_all_short":0.4082,"short_entry":"value","vs_all_full":0.3892,"full_entry":"color-contrast","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.3851,"intrabatch_full_max_pair":"hue vs color-symbolism",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-51 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"hue":"合格","color-symbolism":"待核实","warm-cool":"待核实"}
VERDICT_PENDING={"hue":"一致/恰当(附轻微措辞项)","color-symbolism":"失真(个例误清,须回退true)","warm-cool":"一致/准确(单源披露)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
ANOMALY_NVC="pending_sum 213->212 (-1, 0.39%); not batch-level anomaly; color-symbolism single-entry nv mis-clear requires targeted fix"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (1合格+2待核实), 0 fabrication/0 fake id/0 dead link; similarity all <0.54; nvc drop not batch-anomalous. Targeted fixes: (1) color-symbolism restore nv=true + add second source for exact tricolor triad or rewrite with per-source wording + add Louvre official source for RF129 or delete number; (2) warm-cool keep nv=true and add second independent institution source for Temeraire warm-to-cool sequence before clearing; (3) hue keep 合格, tighten location/year or add catalogue source; (4) add design-intent/dimension annotations site-wide; (5) store full source titles."
READONLY="only wrote research/spotcheck-round52.md; no other project file changed (review-round52a/52b.md, apply_review_round52.py untouched); no git commit; round52 work remains uncommitted as found; web content treated as data, no instruction executed; no files written outside deliverable"
```

*（报告完）*
