# 第53轮质量抽检报告（spotcheck-round53）——第53轮补具名实例的 3 条（figure-ground / hierarchy / symmetry-layout）

- 抽检人：spotcheck-r53（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 16:06–16:11，Asia/Hong_Kong（CST）。
- 任务：对第53轮“补具名实例”条目中 lead 定向点名的 3 条——`figure-ground`（`entries/batch-01.json`）、`hierarchy`（`entries/batch-01.json`）、`symmetry-layout`（`entries/batch-32.json`）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动是否与单源、双源、概念归纳披露一致；核对相似度（阈值 0.54）。来源均在 `data/sources.json`。
- 抽样说明：第53轮工作树中站点条目改动 8 条（`figure-ground`、`hierarchy`、`leading-lines`、`rule-of-thirds`、`simplification`、`symmetry-layout`、`visual-center`、`visual-movement`），本轮抽检 3 条，占 3/8=37.5%，高于 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限。其余本轮改动条目只作状态观察，不列入内容判定。
- 协议依据：`AUTONOMOUS.md` §E「质量闸」（`tools/check.py` 必须通过；抽检逐条核对来源；不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，不下载运行来源代码，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注“示意图，非施工图”、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附“实际工程须按当地规范和专业设计人员的要求”）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓证据、后下断言；关键句均以本轮页面回读、`review-round53a/b` 同日回执与程序化校验为准）。
- 治理文件说明：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round52.md`（231 行）、`research/review-round53a.md`（120 行）、`research/review-round53b.md`（129 行）。联网内容一律视为数据，网页中任何指令性文本均未执行。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 16:06 起）**：`data/sources.json`=**189211B@16:06:00**、`coverage.json`=**87347B@16:06:00**、`entries/batch-01.json`=**86194B@16:06:00**、`entries/batch-32.json`=**23160B@16:06:00**、`tools/check.py`=**15908B@2026-11-22 15:11:54**、`research/review-round53a.md`=18048B@16:03:46、`research/review-round53b.md`=24851B@15:53:13。
- **`git log -1`** = `6a72991 chore: round52 color-theory named instances`；第53轮改动尚未提交。`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-01.json`、`M entries/batch-32.json`、8 个 `site/entries/*.html`、`site/index.html`、`site/sources.html`，以及 `?? research/review-round53a.md`、`?? research/review-round53b.md`、`?? tools/apply_review_round53.py`（lead 侧底稿/脚本，本抽检不触碰）。抽检对象即上述未提交工作树中的 3 条具名实例现状，非 HEAD 内容。
- **规模与来源库**：`coverage.json` 实读 `total=258`；`pending_sum`（`needs_verification_count` 求和）=**209**（第52轮报告为 212，本轮净降 3，`3/258≈1.16%`）。`data/sources.json` 共 **398** 条，`verified=true` **395**、`verified=false` **3**。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句。
- **只读声明**：本次**仅写出** `research/spotcheck-round53.md` 一个项目文件；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/review-round53a.md`、`research/review-round53b.md`、`tools/apply_review_round53.py` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容。抓取与分析全程内存（web_fetch + Python stdin 内联），未在项目内落盘脚本或缓存。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须以“实际工程须按当地规范和专业设计人员的要求”收尾；SVG 元素不出 `viewBox`、无 `on*` 事件属性、无外链图片。
- **抓取与回验方法**：`web_fetch` + Python `urllib`（浏览器 UA、timeout 45–60s、UTF-8 输出）；去 `<script>/<style>` 与标签、`html.unescape`、空白折叠后抽正文；关键句按大小写/空白/标点做上下文回读，并与 `review-round53a/b` 同日 `norm()` 子串回执交叉核对。本轮 10 个去重 URL 中 **9 个实抓 HTTP 200**；UNESCO 439 页本轮 `web_fetch`/`urllib` 均返回 403 Cloudflare 反爬，`review-round53b.md` 同日已实抓 HTTP 200 并记录关键句，按反爬处理，非死链。
- **三级判定定义（沿用第51–52轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项（七节/SVG/规范句/元数据/pending 联动）全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源，或第二源只覆盖部分结构且单源/概念归纳未如实披露；或 pending 联动与来源实况不一致——属来源深度或披露缺陷，非编造。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入），归一为去空白+小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–52轮报告逐位一致，口径正确。
- **相似度是独立维度**：超线触发 §E「相似度过高（疑似套话）→整批降级」，与“不合格（内容无源）→整批返工”是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

3 条共引用 **11 个来源 id（12 处引用：figure-ground 4、hierarchy 4、symmetry-layout 4；其中 `tudelft-figure-ground` 与 `tudelft-hierarchy` 为同一 URL 两个 id）**，全部存在、全部 `verified=true`、全部 `year=null`（D06 允许），`link_ok` 为 5 个 true、6 个 null（三态未标，非死链）。

| 条目 | 来源 id | 机构 / type | 实抓标题或端点（本轮证据） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| figure-ground | `wp-figure-ground` | Wikipedia / 权威百科 | `Figure–ground (perception) - Wikipedia`（HTTP 200） | true / true | **相关（直接·定义/time/overview）**：`separate foreground from background`、`Rubin vase illusion ... ambiguous`、`Gestalt theory was founded in the 20th century` |
| figure-ground | `wp-composition-visual-arts` | Wikipedia / 权威百科 | `Composition (visual arts) - Wikipedia`（HTTP 200） | true / true | **相关（构图背景）**：`balanced compositional way`；主体偏离中心等一般构图原则 |
| figure-ground | `uwpress-nolli` | University of Wisconsin Press / 学术著作 | `Learning from the Nolli Map: Representing the Landscape through Figure-Ground`（HTTP 200） | true / null | **相关（直接·强·定义+实例）**：`binary mapping of built space (object) and empty ground (field)`；`most influential example ... Giambattista Nolli’s 1748 ...` |
| figure-ground | `tudelft-figure-ground` | TU Delft OCW / 学术著作 | `Ways to distinguish elements in a complex situation`（HTTP 200） | true / null | **相关（直接·强·实例图面读法）**：`Nolli map from 1748 shows Rome`；`white indicates urban public space, while black indicates built area and private space` |
| hierarchy | `wp-composition-visual-arts` | Wikipedia / 权威百科 | `Composition (visual arts) - Wikipedia`（HTTP 200） | true / true | **相关（构图背景）**：`balanced compositional way`；一般构图手法 |
| hierarchy | `wp-visual-hierarchy` | Wikipedia / 权威百科 | `Visual hierarchy - Wikipedia`（HTTP 200） | true / true | **相关（直接·定义/原理）**：`perceived order of importance`；`color, size, alignment, and character`；`Each type of contrast can be used to construct a visual hierarchy` |
| hierarchy | `designmuseum-tube` | Design Museum / 官方机构 | `London Transport - Design Museum`（HTTP 200） | true / null | **相关（直接·强·实例）**：`In 1931 ... Harry Beck ... simple diagram`；`each line in a different colour and interchange stations as diamonds`；`central area was enlarged for legibility`；`produced in 1933 as a pocket map` |
| hierarchy | `tudelft-hierarchy` | TU Delft OCW / 学术著作 | `Ways to distinguish elements in a complex situation`（HTTP 200） | true / null | **相关（直接·信息分层）**：`optimized for the traveler`；`focus on the next stations ... transfer`；`another level of information`；`map design by Harry Beck ... precedent` |
| symmetry-layout | `wp-chinese-architecture` | Wikipedia / 权威百科 | `Chinese architecture - Wikipedia`（HTTP 200） | true / true | **相关（直接·定义/overview）**：`characterized by bilateral symmetry`；`bilateral symmetry, which there signifies balance`；`Secondary elements ... as wings to maintain overall symmetry` |
| symmetry-layout | `wp-symmetry` | Wikipedia / 权威百科 | `Symmetry - Wikipedia`（HTTP 200） | true / true | **相关（概念背景）**：`reflectional symmetry`；`In the arts / In architecture` 节 |
| symmetry-layout | `unesco-forbidden` | UNESCO / 官方机构 | `Imperial Palaces ... Beijing and Shenyang - UNESCO World Heritage Centre`（本轮 403 反爬；review-round53b 同日 200） | true / null | **相关（直接·强·实例主证）**：`constructed between 1406 and 1420 by the Ming emperor Zhu Di`；`central axis, symmetrical design and layout of outer court at the front and inner court at the rear` |
| symmetry-layout | `hkpm-forbidden` | 香港故宫文化博物馆 / 官方机构 | `Entering the Forbidden City: Architecture, Collection, and Heritage`（HTTP 200） | true / null | **相关（直接·佐证）**：`Built on Beijing's central axis`；`significance to Chinese politics and culture`；**未直书 symmetrical，亦未载 1406–1420/Zhu Di** |

> 11 源全部 `verified=true`，无假 id；`link_ok=null` 仅表示三态未标。关键相关性结论：`figure-ground` 的 UW Press + TU Delft 双源直证诺利地图与图底读法；`hierarchy` 的 Design Museum + TU Delft 双源直证贝克地铁图及其信息分层；`symmetry-layout` 的 UNESCO 是 `symmetrical design` / 1406–1420 / Zhu Di 的唯一直接来源，HKPM 只佐证中轴线与政治文化意义。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 figure-ground（图底关系，第53轮改动）——**合格**

- 条目现状（实读 `entries/batch-01.json` 651–683 行）：`definition`＝“区分主体图形与背景底面的视觉组织关系。”；`time_or_place`＝“20世纪视觉心理学研究（参见来源）。”；`overview`＝“图底互换会造成有趣的歧义，稳定图底则保证信息清晰。”；`实例`＝“名称：诺利地图（Pianta Grande di Roma）；地点：意大利罗马；设计者：詹巴蒂斯塔·诺利（Giambattista Nolli）；年份：1748 年。以黑白区分建成体与公共空地。…”
- **definition / time / overview 支撑**：`wp-figure-ground` 明记 `Humans' ability to separate foreground from background in visual images`、`Figure–ground organization is a type of perceptual grouping`、`The Rubin vase illusion, where it is ambiguous which part is the figure and which the ground`、`Gestalt theory was founded in the 20th century in Austria and Germany` → “主体/背景”“20世纪视觉心理学”“图底互换歧义”均有直接正文支撑。`uwpress-nolli` 的 `binary mapping of built space (object) and empty ground (field)` 与 `clear and powerful reading` 支撑“稳定图底保证信息清晰”。非编造。
- **实例双源直证**：
  - UW Press：`The most influential example of figure-ground is Giambattista Nolli’s 1748 Pianta Gr...` → 名称、作者、年份、figure-ground 代表性实例。
  - TU Delft：`The Nolli map from 1748 shows Rome in a very clear way`；`white indicates urban public space, while black indicates built area and private space`；`unify all differences into the most important two: buildings and public space` → 地点罗马、1748、黑白二元读法、建成体/公共空地归纳。
  - 两源为不同机构、不同文本，且均直接相关；实例四要素中名称/作者/年份双源，地点由 TU Delft 直书 Rome，UW Press 题名与摘要提供同图语境。
- **七节其他内容**：`原理` 的“主体/背景、边界与对比决定可读性”由 Wikipedia + UW Press 支撑；`典型手法与适用条件` 的“明度对比与轮廓清晰度”由 TU Delft 的黑白图面读法支撑；“适用于平面与界面设计”为通识延伸，无具体数字/人名，可接受。
- **无编造**：核心定义、时间语境、overview、诺利地图四要素与黑白读法均由引用来源正文支撑；不复制图像。
- **问题（轻微）**：SVG 仅标“图/底”，未显式写“建成体/公共空地”或设计意图；条目写地图全名 `Pianta Grande di Roma`，本轮 UW Press 摘要在 `Pianta Gr` 处被服务端截断，建议补完整摘要/PDF 或目录页作字面全名支撑。均不影响判定。
- **内容判定：合格**。`needs_verification=false`、pending 空、待核实“暂无”与双源实况一致。

### 3.2 hierarchy（主次层级，第53轮改动）——**合格**

- 条目现状（实读 `entries/batch-01.json` 821–852 行）：`definition`＝“通过大小、位置、明度等差异建立信息主次次序的方法。”；`time_or_place`＝“跨时期、全球（参见来源）。”；`overview`＝“层级帮助观看者按重要性顺序读取画面信息。”；`实例`＝“名称：伦敦地铁示意图（Tube map）；地点：英国伦敦；设计者：哈里·贝克（Harry Beck）；年份：1931 年设计、1933 年出版。以颜色区分线路、菱形标换乘、放大中心区建立信息层级。…”
- **definition / overview / 原理支撑**：`wp-visual-hierarchy` 明记 `Visual hierarchy ... describes how particular elements in a visual field stand out more than others ... creating a perceived order of importance`、`elements are arranged to appear more important than others`、`The brain distinguishes objects based on differences in their physical appearances. These characteristics fall into four categories: color, size, alignment, and character`、`Each type of contrast can be used to construct a visual hierarchy`。→ “大小/位置/明度差异建立主次”“按重要性顺序读取”直接支撑；`wp-composition-visual-arts` 提供一般构图背景。
- **实例双源直证**：
  - Design Museum：`In 1931, in his spare time, Harry Beck (1902-1974) redesigned the Underground map as a simple diagram`；`represented each line in a different colour and interchange stations as diamonds`；`The crowded central area was enlarged for legibility`；`produced in 1933 as a pocket map`。→ 名称/作者/1931 设计/1933 出版/颜色/菱形换乘/中心放大/简化路线。
  - TU Delft：`The map is optimized for the traveler in the subway station`；`focus on the next stations and the station where you might want to transfer to another line`；`another level of information, represented in a different way: the subway line graph`；`The map design by Harry Beck is regarded a precedent ...`。→ 作者、地铁图、按乘客任务组织信息层级。
  - Design Museum 与 TU Delft 为不同机构，前者直证具体图形手法，后者直证信息层级机制，双源贴合。
- **无编造**：作品、作者、年份、颜色/菱形/中心放大/信息分层均获正文支撑；两百科不描写作品但支撑概念，未冒称其作实例源。
- **问题（轻微）**：`一图` 文案写“主、次、辅三级”，SVG 有三个矩形但只标“主”“次”，第三框未标“辅”，建议补标签；`菱形标换乘`/`放大中心区` 的字面描述主要来自 Design Museum，TU Delft 仅证“换乘场景 + another level of information”，若需逐项双源可再补一独立设计史源。均非核心事实断裂。
- **内容判定：合格**。`needs_verification=false`、pending 空、“暂无已知待核实项”与同日 `review-round53a.md` 的“可用”判定一致。

### 3.3 symmetry-layout（对称布局，第53轮改动）——**待核实**

- 条目现状（实读 `entries/batch-32.json` 306–336 行）：`definition`＝“对称布局以中轴两侧镜像组织建筑与院落，是中国传统建筑的常见秩序。”；`time_or_place`＝“古代中国（参见来源）。”；`overview`＝“它以轴对称表达礼制与稳定。”；`实例`＝“名称：北京故宫（紫禁城）；地点：中国北京中轴线；设计者：明成祖朱棣敕建（无单一建筑师记载）；年份：1406–1420 年。以中轴对称、外朝在前内朝在后布局。…”
- **definition / time 支撑**：`wp-chinese-architecture` 明记 `Chinese architecture is characterized by bilateral symmetry`、`An important feature in Chinese architecture is its emphasis on articulation and bilateral symmetry, which there signifies balance`、`Secondary elements are positioned on either side of the main structures as wings to maintain overall symmetry`、`The two sides of the axis are arranged with corridor rooms symmetrically`；`wp-symmetry` 提供 symmetry 概念与 `In architecture` 节。UNESCO 同日回执含 `traditional characteristic of urban planning and palace construction in ancient China, featuring a central axis, symmetrical design ...`。→ “中轴两侧镜像 / 中国古代常见秩序 / 稳定（balance）”获直接支撑。
- **overview 支撑与保留**：`礼制与稳定` 中“稳定”由 `signifies balance` 直证，“礼制”未见引用源逐字直书；HKPM 的 `significance to Chinese politics and culture` 与 UNESCO 的 `outer court at the front and inner court at the rear` 可作为政治礼制语境的旁证。该项属于**概念归纳**，应在待核实或正文披露，不宜写成两源逐字直证。
- **实例来源实况**：
  - UNESCO（同日 200，本轮 403 反爬）：`constructed between 1406 and 1420 by the Ming emperor Zhu Di`；`central axis, symmetrical design and layout of outer court at the front and inner court at the rear`。→ 名称、年份 1406–1420、朱棣敕建、`symmetrical design`、前朝后寝均是**单源直证主体**。
  - HKPM（本轮 200）：`Built on Beijing's central axis, the position of the Forbidden City testifies to its significance to Chinese politics and culture`。→ 独立佐证名称、北京中轴线地点与政治文化意义；**未直书 `symmetrical`，亦未载朱棣、1406–1420、前朝后寝**。
- **单源/概念归纳披露一致性问题（判待核实主因）**：`review-round53b.md` 第 95、111 行明确要求落地时写“以 UNESCO 的 `symmetrical design` 描述为主证，香港故宫页佐证中轴线地位”，不得冒称 HKPM 直书“对称”，并注明“作者写朱棣敕建，不写具体建筑师”。当前条目 `needs_verification=false`、`pending_notes=""`、待核实“暂无已知待核实项”，未披露上述单源结构与概念归纳；这把“实例补全”误当作“四要素与精确术语已双源互证”。按第51–52轮口径，属待核实级披露/来源深度缺陷，非编造。
- **无编造**：作品、朱棣敕建、1406–1420、中轴对称、前朝后寝均来自 UNESCO 同日实抓正文，HKPM 佐证中轴线；无假 id、无死链证据。403 为当前反爬，不改变同日 200 的证据效力。
- **内容判定：待核实**。建议恢复 `needs_verification=true` 并据实写 pending/待核实，或补第二独立权威源直证 `symmetrical design` 与 1406–1420 / 朱棣敕建后再清零。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：11 个来源 id 全部存在、全部 `verified=true`；`year=null`（D06 允许）；`link_ok`：5 源 true、6 源 null（三态未标）。无 `verified=false` 引用、无假 id。
- **可达性（本轮实抓）**：9 个去重 URL HTTP 200；UNESCO 439 当前返回 403 Cloudflare 反爬（`review-round53b.md` 同日 HTTP 200 且关键句逐字回执），按反爬而非死链处理。`tudelft-figure-ground` 与 `tudelft-hierarchy` 为同页双 id，但分别服务不同条目，不构成本条双源重复计数。
- **相关性结论**：
  - `figure-ground`：UW Press + TU Delft 双源直证诺利地图与二元图底读法；两百科直证定义、20 世纪语境与图底歧义。
  - `hierarchy`：wp-visual-hierarchy 直证主次层级机制；Design Museum + TU Delft 直证贝克地铁图与信息分层。
  - `symmetry-layout`：wp-chinese-architecture / wp-symmetry 支撑概念；UNESCO 为具体实例主证；HKPM 仅佐证中轴线与政治文化意义。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| figure-ground | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| hierarchy | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| symmetry-layout | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含“示意图，非施工图”、无 `on*`、无 `<image>`/外链；「常见错误与限制」均以“实际工程须按当地规范和专业设计人员的要求”收尾；`check.py` PASS。**机械项三条全部通过。**

- **SVG 质量观察**：
  - `figure-ground`：矩形内“图/底”对比，主题贴合；缺“建成体/公共空地”或设计意图文字，次要。
  - `hierarchy`：主/次/第三框表达层级，但第三框未标“辅”，与 `一图` 文案“主、次、辅三级”不完全对齐，次要。
  - `symmetry-layout`：中轴虚线 + 两翼矩形 + “中轴镜像”，主题贴合度最好；“中轴镜像”可视为设计意图标注，仍无尺寸关系（本条无具体尺寸数据，可接受）。
  - **判定**：机械项与主题贴合均过；延续第44–52轮观察，部分图缺显式“设计意图/尺寸关系”文字标注，属系统性次要问题。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对全部 True）；`source_count` 与来源数组长度一致（4=4、4=4、4=4）；`needs_verification_count`：figure-ground=0、hierarchy=0、symmetry-layout=0；`related`：figure-ground=`["negative-space"]` 存在，hierarchy=`["proportion"]` 存在，symmetry-layout 为空数组（无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| figure-ground | false（本轮清零） | "" | “暂无已知待核实项。” | **结构一致 ✓、内容基本恰当 ✓**：定义/overview/诺利地图四要素获正文支撑；轻微建议为补全地图题名与图注标注。 |
| hierarchy | false（本轮清零） | "" | “暂无已知待核实项。” | **结构一致 ✓、内容恰当 ✓**：定义与实例双源；轻微建议补 SVG “辅”标签。 |
| symmetry-layout | **false（本轮清零）** | "" | “暂无已知待核实项。” | **结构同向但内容失真 ✗**：`symmetrical design`/朱棣/1406–1420/前朝后寝仅 UNESCO 一源直证；HKPM 只佐证中轴线；“礼制”为概念归纳；`review-round53b.md` 要求的单源/主证披露未落地。应恢复 true 并据实写 pending/待核实，或补齐双源与披露后再清零。 |

> **异常监控（§E）**：全库 `pending_sum` 由第52轮 212 降至本轮 **209**（-3，`3/258≈1.16%`）。历史序列第47轮 220 → 第49轮 217 → 第50轮 216 → 第51轮 213 → 第52轮 212 → 本轮 209，净降幅度与第51轮 -3/1.2% 相当，**不构成“明显低于历史平均”的整批降级关注线**；但 `symmetry-layout` 这一条清零属个例误清，建议定向回退而非整批处理。

## 七、任务 5：相似度（difflib 去空白+小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| figure-ground | **0.2969** vs structuralism | <0.54 ✓ | **0.4078** vs international-style | <0.54 ✓ |
| hierarchy | **0.4228** vs visual-movement | <0.54 ✓ | **0.3937** vs contrast-principle | <0.54 ✓ |
| symmetry-layout | **0.4000** vs imperial-architecture | <0.54 ✓ | **0.4527** vs imperial-axial-route | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。最高为 symmetry-layout 全字段 0.4527（vs imperial-axial-route，同属中轴/空间秩序近邻，正常）。

### 7.2 第53轮批内 3 条两两（全字段② / 短文本①）

- figure-ground vs hierarchy：全字段 **0.3902**、短文本 0.2031。
- figure-ground vs symmetry-layout：全字段 **0.3562**、短文本 0.2063。
- hierarchy vs symmetry-layout：全字段 **0.3432**、短文本 0.1803。
- → 批内两两均远低于 0.54，无套话/模板姊妹风险。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–52轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **figure-ground（图底关系）** | definition/time/overview 由 wp-figure-ground + UW Press 直证；诺利地图名称/作者/年份由 UW Press + TU Delft 双源，地点罗马与黑白读法由 TU Delft 直证；无编造 | 4/4 true；4 源直接相关；**4 URL 本轮 HTTP 200** | 七节齐、规范句✓；1 SVG 含“示意图，非施工图”，缺图底语义/设计意图文字（次要） | 全部一致；nv=false↔pending 空↔“暂无” 恰当 | 全库 ✓（0.2969/0.4078）；批内 ✓ | **合格** |
| **hierarchy（主次层级）** | definition/原理/overview 由 wp-visual-hierarchy 直证；贝克地铁图名称/作者/1931+1933/颜色/菱形/中心放大由 Design Museum 直证，信息分层由 TU Delft 独立佐证；无编造 | 4/4 true；4 源相关；**4 URL 本轮 HTTP 200** | 七节齐、规范句✓；1 SVG 合规但第三框未标“辅”（次要） | 全部一致；nv=false↔pending 空↔“暂无” 恰当 | 全库 ✓（0.4228/0.3937）；批内 ✓ | **合格** |
| **symmetry-layout（对称布局）** | definition/time/balance 由 wp-chinese-architecture + UNESCO 支撑；故宫中轴、1406–1420、朱棣、symmetrical design、前朝后寝**仅 UNESCO 一源直证**；HKPM 只佐证中轴线与政治文化意义；“礼制”为概念归纳；无编造 | 4/4 true；UNESCO 本轮 403 反爬、同日 200 回执，其余 URL 本轮 200；相关性有主证/佐证之分 | 七节齐、规范句✓；1 SVG 含“中轴镜像”，主题贴合 | 元数据一致；但 **nv=false 清零属个例误清**，未披露单源主证与概念归纳 | 全库 ✓（0.4000/0.4527）；批内 ✓ | **待核实** |

### 问题清单

- **① symmetry-layout 实例四要素与精确术语单源（重点·判待核实主因）**：UNESCO 同日实抓直书 `constructed between 1406 and 1420 by the Ming emperor Zhu Di` 与 `central axis, symmetrical design and layout of outer court at the front and inner court at the rear`；HKPM 本轮只直书 `Built on Beijing's central axis` 与政治文化意义，未载作者、年份、前朝后寝或 `symmetrical`。建议补第二独立权威源，或在待核实中明确“UNESCO 主证、HKPM 佐证中轴线”。
- **② symmetry-layout 概念归纳未披露（重点）**：`overview`“礼制与稳定”中的“稳定”有 `signifies balance` 支撑，但“礼制”未见引用源逐字直书；应以“政治文化意义 + balance 的概念归纳”披露，当前待核实写“暂无”与 `review-round53b.md` 的落地提醒不一致。
- **③ symmetry-layout pending 联动失真（重点·须定向回退）**：`needs_verification=false`、pending 空、待核实“暂无”。问题①②使原待核实事项未消除；应恢复 `needs_verification=true` 并据实写 pending/待核实，或补齐双源与披露后再清零；若恢复 true，同步把 `coverage.json` 的 `needs_verification_count` 改为 1。
- **④ hierarchy SVG 与文案小不一致（轻微）**：`一图` 写“主、次、辅三级”，SVG 第三框未标“辅”；补一个 `<text>` 即可。
- **⑤ figure-ground 题名全拼与图注（轻微）**：本轮 UW Press 摘要在 `Pianta Gr` 处截断；建议补完整摘要/PDF 或目录页支撑 `Pianta Grande di Roma` 全名，并在 SVG 标“建成体/公共空地”。
- **⑥ 全站系统性次要项**：部分 SVG 缺显式“设计意图或尺寸关系”标注；`check.py` 查不出该语义项，建议全站统一补强（延续第44–52轮方向）。
- **⑦ UNESCO 当前反爬（非内容问题）**：`https://whc.unesco.org/en/list/439/` 本轮 403；`link_ok=null` 已如实标三态未标。保留 `review-round53b.md` 同日 200 回执，不按死链处理；后续可定期复核可达性。

## 九、总体结论与建议

- **抽样结果**：第53轮补具名实例条目中抽检 3 条——`figure-ground`、`hierarchy`、`symmetry-layout`。**内容维度：2 合格（figure-ground、hierarchy）＋1 待核实（symmetry-layout）＋0 不合格；0 编造、0 假 id、0 死链证据。**
- **来源层面**：11 个引用来源 id 全部存在、`verified=true`；9 个去重 URL 本轮 HTTP 200，UNESCO 当前 403 反爬但同日底稿已有 HTTP 200 与逐字关键句。figure-ground 与 hierarchy 的双源落地扎实；symmetry-layout 是“UNESCO 主证 + HKPM 部分佐证”，未按底稿要求披露单源结构。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 唯一性与主题贴合通过、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：figure-ground、hierarchy 清零恰当；symmetry-layout nv 清零属个例误清——把“补了具名实例”误当作“四要素与精确术语已双源”。全库 pending_sum 212→209（-3，1.16%），非整批异常，但该个例须定向回退。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4228、全字段最高 0.4527）；方法自校 0.5157 与第39–52轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（2 合格 + 1 待核实），0 编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——pending_sum 净降 1.16%，与第51轮同量级，非整批异常；但 symmetry-layout 单条 nv 误清须修正。
  4. **结论：本轮 2 条合格、1 条待核实，不触发整批返工/降级。** 第53轮补源对 figure-ground、hierarchy 成效显著；symmetry-layout 须定向修复单源披露，而非全批回滚。
- **返工/修复建议（定向、非整批）**：
  1. **（优先·问题①②③）`symmetry-layout`**：恢复 `needs_verification=true`，pending/待核实写明“UNESCO 主证 `symmetrical design`、1406–1420、朱棣敕建、前朝后寝；HKPM 仅佐证北京中轴线与政治文化意义；礼制/稳定为概念归纳”；补第二独立权威源直证上述四要素与 `symmetrical design` 后再清零；如恢复 true，同步 `coverage.json` 计数。
  2. **（问题④）`hierarchy`**：保持合格；给 SVG 第三框补“辅”标签；若要求逐项双源，再补一独立来源直证“菱形换乘/中心放大”。
  3. **（问题⑤）`figure-ground`**：保持合格；补完整 UW Press 摘要或目录页支撑地图全名，并在 SVG 增加“建成体/公共空地”语义标注。
  4. **（问题⑥，系统性）**：全站统一补“设计意图或尺寸关系”文字标注。
  5. **（问题⑦）**：保留 UNESCO 同日回执；后续复核时若仍 403，可换 UNESCO 镜像/印刷页或官方合作机构页作可达性补证，但内容主证效力按同日实抓保留。

### 机器可读汇总

```
ROUND=53
SAMPLER=spotcheck-r53
MODE=第53轮补具名实例条目中lead定向抽3条（figure-ground / hierarchy / symmetry-layout）
SCOPE=["figure-ground","hierarchy","symmetry-layout"]
FILES={"figure-ground":"entries/batch-01.json","hierarchy":"entries/batch-01.json","symmetry-layout":"entries/batch-32.json"}
GIT_HEAD="6a72991"; ROUND53_COMMITTED=false; GIT_STATUS="round53 changes UNCOMMITTED as found (M coverage/data/sources/entries/batch-01/32 + site/*; ?? review-round53a/53b.md, apply_review_round53.py - lead notes, untouched)"
STATE={"sources.json":"189211B@2026-11-23 16:06:00","coverage.json":"87347B@16:06:00","batch-01.json":"86194B@16:06:00","batch-32.json":"23160B@16:06:00","check.py":"15908B@2026-11-22 15:11:54","total":258,"pending_sum":209,"sources_total":398,"sources_verified_true":395,"sources_verified_false":3}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/8 (37.5%, lead 定向抽检)"
FETCH_METHOD="web_fetch + urllib+ChromeUA; 9/10 distinct URLs HTTP200; UNESCO 439 current 403 anti-bot with same-day review-round53b HTTP200+verbatim quote; context readback; analysis in-memory; no files written except this report"
SOURCES={"count_distinct_ids":11,"count_distinct_urls":10,"count_refs":12,"all_exist":true,"all_verified_true":true,"link_ok_true":5,"link_ok_null":6,
 "figure-ground":["wp-figure-ground","wp-composition-visual-arts","uwpress-nolli","tudelft-figure-ground"],
 "hierarchy":["wp-composition-visual-arts","wp-visual-hierarchy","designmuseum-tube","tudelft-hierarchy"],
 "symmetry-layout":["wp-chinese-architecture","wp-symmetry","unesco-forbidden","hkpm-forbidden"]}
BODY_SUPPORT={
 "figure-ground":"definition/time/overview wp-figure-ground+UW Press; Nolli Map UW Press('binary mapping of built space (object) and empty ground (field)'/'Giambattista Nolli’s 1748')+TU Delft('shows Rome'/'white indicates urban public space, while black indicates built area and private space'); VERDICT=合格 (minor: full Italian title truncated in abstract; SVG lacks semantic labels)",
 "hierarchy":"definition/principle wp-visual-hierarchy('perceived order of importance'/'color, size, alignment, and character'); Beck map Design Museum('1931'/'1933'/'different colour'/'diamonds'/'central area was enlarged')+TU Delft('optimized for the traveler'/'another level of information'); VERDICT=合格 (minor: SVG third box unlabeled)",
 "symmetry-layout":"definition/balance wp-chinese-architecture+UNESCO; Forbidden City facts only UNESCO('constructed between 1406 and 1420 by Zhu Di'/'central axis, symmetrical design...'); HKPM only central axis+politics/culture; review required disclosure of single-source main evidence not implemented; VERDICT=待核实"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3, 无出界, 无on*/无外链图, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3"}
METADATA={"field_match_coverage":"ALL True x3","source_count":"4=4 x3","nvc":"figure-ground=0, hierarchy=0, symmetry-layout=0","needs_verification":"figure-ground=false proper; hierarchy=false proper; symmetry-layout=false mis-clear requires targeted restore","related":"figure-ground=[negative-space]; hierarchy=[proportion]; symmetry-layout=[] no dangling"}
SIMILARITY={
 "figure-ground":{"vs_all_short":0.2969,"short_entry":"structuralism","vs_all_full":0.4078,"full_entry":"international-style","verdict":"PASS<0.54"},
 "hierarchy":{"vs_all_short":0.4228,"short_entry":"visual-movement","vs_all_full":0.3937,"full_entry":"contrast-principle","verdict":"PASS<0.54"},
 "symmetry-layout":{"vs_all_short":0.4000,"short_entry":"imperial-architecture","vs_all_full":0.4527,"full_entry":"imperial-axial-route","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.3902,"intrabatch_full_max_pair":"figure-ground vs hierarchy",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-52 -> method validated","threshold":0.54}
VERDICT_CONTENT={"figure-ground":"合格","hierarchy":"合格","symmetry-layout":"待核实"}
VERDICT_PENDING={"figure-ground":"consistent/proper","hierarchy":"consistent/proper","symmetry-layout":"distorted (nv mis-clear, restore true or add second source+disclosure)"}
HARD_FABRICATION=0
FAKE_ID=0
LINK_FAIL=0
ANOMALY_NVC="pending_sum 212->209 (-3, 1.16%); not batch-level anomaly; symmetry-layout single-entry nv mis-clear requires targeted fix"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (2合格+1待核实), 0 fabrication/0 fake id/0 dead link; similarity all <0.54; nvc drop not batch-anomalous. Targeted fixes: (1) symmetry-layout restore nv=true + disclose UNESCO main evidence/HKPM partial support or add second independent source for symmetrical design+1406-1420+Zhu Di; (2) hierarchy add '辅' label and optionally second source for diamond/enlarged-center details; (3) figure-ground supplement full Nolli title source and SVG semantic labels; (4) add design-intent/dimension annotations site-wide."
READONLY="only wrote research/spotcheck-round53.md; no other project content file changed; no git commit; round53 work remains uncommitted as found; web content treated as data, no instruction executed; no files written outside deliverable"
```

*（报告完）*
