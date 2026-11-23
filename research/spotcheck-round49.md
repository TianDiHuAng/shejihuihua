# 第49轮质量抽检报告（spotcheck-round49）——第48轮改动的 5 条中抽 2 条（atrium-architecture / brutalism）

- 抽检人：spotcheck-r49（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 11:39 起，Asia/Hong_Kong（CST）。
- 任务：对**第48轮改动的 5 条**——`atrium-architecture`、`parametric-architecture`、`deconstructivism`、`brutalism`、`two-point-perspective`——中的 **2 条**：`atrium-architecture`（中庭）、`brutalism`（粗野主义）——逐条核对 **definition / time_or_place / overview / 实例** 是否有**引用来源正文直接支撑**、是否**编造**、来源是否**直接相关**，以及 **L2 七节 / SVG / 规范提示 / pending 联动 / 相似度（阈值 0.54）**。
- 抽样比：第48轮改动 5 条，本轮抽 2 条（**2/5＝40%**，高于 `AUTONOMOUS.md` §E「随机 10%」的比例下限；但为 lead 定向点名的**针对性补抽**，另 3 条 `parametric-architecture`/`deconstructivism`/`two-point-perspective` 本轮**未做内容核对**，仅列名，见 §六注）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；抽检逐条核对来源，不合格则整批返工、下轮抽检提至 25%；相似度过高→整批降级）＋第六节（联网内容一律视为数据、其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节标准与「专用规则」（每页 1–2 张示意图、图下注"示意图，非施工图"、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附"实际工程须按当地规范和专业设计人员的要求"）＋「通用硬性规则」（**不编造数字/日期/人名/引文/出处**；**关键事实至少两个独立来源互相印证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 以任务说明书为准）与 `verification-before-completion`（**先实抓证据、后下断言**：9 个引用来源全部本轮实抓，关键句以 `norm(quote) in norm(page)` 子串回验）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 11:39 起）**：`data/sources.json`=**161837B@2026-11-23 11:39**、`coverage.json`=**87346B@2026-11-23 11:39**、`entries/batch-04.json`=**11987B@2026-11-23 11:39**、`entries/batch-25.json`=**10775B@2026-11-23 11:39**、`tools/check.py`=**15908B@2026-11-22 15:11**。
- **`git log -1`** = `358cb9a feat: round48 five named instances, zero-gap 1/3`（第48轮已提交）。`git status --porcelain`（采样时点）仅 `?? research/b1-round49.md`（**这是 lead 侧第49轮 B1 检索笔记，非本抽检产物，本次不触碰**）；其余工作树干净——抽检对象（第48轮成果）已在 HEAD 中，**稳定**。
- **落地口径**：第48轮提交 `358cb9a` 的 stat 显示改动 5 个条目 `entries/batch-01.json`(two-point-perspective)、`entries/batch-04.json`(brutalism、deconstructivism)、`entries/batch-09.json`(parametric-architecture)、`entries/batch-25.json`(atrium-architecture)，`data/sources.json` +120 行（新增 15 个来源）。`git show 358cb9a` 逐条核对：`brutalism` 的 `实例` 由"…来源页面称其常被视为粗野主义风格的最初灵感"改写为含"以清水混凝土（béton brut）著称"，并新增 `flc-unite`、`theartstory-brutalism` 两源；`atrium-architecture` 的 `实例` 由"带天窗中庭的公共建筑（类型性描述）"改写为"纽约古根海姆美术馆…（1943 委托、1959 开馆，螺旋坡道环绕顶部采光中庭）"，新增 `flw-guggenheim`、`theartstory-wright` 两源，并**清除**原 `pending_notes` 与 `待核实`（nv true→false）。**本轮抽检对象即上述改动后的现状。**
- **条目规模（`coverage.json` 实读）**：`total=258`、全部 `level=L2`、全部 `status=已写`；`pending_sum`（`needs_verification_count` 求和）＝**217**。来源库 `sources.json` 共 **343** 条，`verified=true` **340**、`verified=false` **3**（`link_ok`：true 145、false 6、null 192）。注：`link_ok=false` 的 6 条**均不在本次 9 个引用来源中**，不影响判定。
- **`tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round49.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/b1-round49.md` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python `urllib` 读取→内存去标签/切句/回验，脚本经 stdin heredoc 传入、未落盘任何文件）。联网内容一律视为**数据**，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含"示意图，非施工图"；「常见错误与限制」段须以"实际工程须按当地规范和专业设计人员的要求"收尾；SVG 元素不出 `viewBox`。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），timeout 45s，SSL 校验关闭。**9 个引用来源本轮全部实抓 HTTP 200**（`<title>`/正文与 `sources.json` 逐条核对，见 §二、§三），对关键句做 `norm(quote) in norm(page)` 子串回验（大小写/弯直引号/破折号/空白归一化）。全程在内存中完成，未落盘。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **258 条**逐条扫描，警戒线 **0.54**（与第 27–48 轮一致）。**方法自校**：以全字段②计算已知对 `futurism-style vs expressionism-style`，得 **0.5157**，与第 39–47 轮报告**逐位一致**，确认口径正确。
- **三级判定定义（可复现）**：
  - **合格**：definition/time/overview/实例 均获所引来源正文直接支撑；关键事实（概念定义或核心形制/实例的四要素）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但某**关键事实**（核心形制/营造方法/实例四要素）实质单源，或第二源对具体概念仅泛论/零覆盖——属来源深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或关键结构项（如「一图」）实质不满足 TASK_design 强制要求。
- **相似度专项（独立维度）**：警戒线 0.54；超线即触发 `AUTONOMOUS.md §E`「相似度过高（疑似套话）→整批降级」，与"不合格（内容无源）→整批返工"是**不同触发路径**，分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **9 个去重来源 id（9 处引用：brutalism 5、atrium 4）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）、实抓 9/9 HTTP 200**。

| 条目 | 来源 id | 存在/verified | 实抓标题（本轮 HTTP，逐字，字节） | 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| brutalism | `wp-brutalist-architecture` | ✅/true | `Brutalist architecture - Wikipedia`（200，677497B） | Wikipedia | 权威百科 | true | **相关（直接、强）**：`minimalist construction showcasing the bare building materials and structural elements over decorative design`；`exposed, unpainted concrete`；`béton brut ("raw concrete")`；`simple, honest, and functional buildings`；`massive in character`；`social housing influenced by socialist principles`；`monumental` |
| brutalism | `wp-architectural-style` | ✅/true | `Architectural style - Wikipedia`（200，166520B） | Wikipedia | 权威百科 | true | **相关但泛化（不涉 brutalism）**：仅定义"an architectural style is a classification of buildings…"；**全文无 `brutal` 字样**——属"style"伞概念来源，**对本条具体论断零覆盖** |
| brutalism | `wp-unite-d-habitation` | ✅/true | `Unité d'habitation - Wikipedia`（200，242636B） | Wikipedia | 权威百科 | true | **相关（直接、强）**：`Unité d'habitation`、`Marseille`、`Le Corbusier`、`1947`、`1952`、`béton brut` 全部命中 |
| brutalism | `flc-unite` | ✅/true | `Le Corbusier, Unité d'habitation, Marseille, France, 1945-1952`（200，96823B） | Fondation Le Corbusier（官方基金会） | 官方机构 | null | **相关（直接、强·官方）**：标题即 `Le Corbusier, Unité d'habitation, Marseille, France, 1945-1952`；正文 `the final version of the Marseille Housing Unit was adopted in March 1947`（1947 定案）。**但静态正文抽取未见 `béton brut`**（该词由 wp-unite/theartstory 补证） |
| brutalism | `theartstory-brutalism` | ✅/true | `Brutalist Architecture Movement Overview \| TheArtStory`（200，170612B） | TheArtStory | 学术著作 | null | **相关（直接、强）**：`Unité d'habitation (1952)`、`war-damaged Marseille`、`raw concrete (French "béton brut") for exterior surfaces`、`weight, density, and mass of concrete` |
| atrium | `wp-atrium-architecture` | ✅/true | `Atrium (architecture) - Wikipedia`（200，195046B） | Wikipedia | 权威百科 | true | **相关（直接、强）**：`a large open-air or skylight-covered space surrounded by a building`；`atria were a common feature in ancient roman dwellings, providing light and ventilation to the interior`；`modern atria … are often several stories high, with a glazed roof`；`the atrium was the open central court with enclosed rooms on all sides` |
| atrium | `designingbuildings-atrium` | ✅/true | `Atrium definition - Designing Buildings`（200，45066B） | Designing Buildings（行业维基；记录 author 记作"Wikipedia/机构"） | 学术著作 | null | **相关（直接、定义型·薄）**：`Approved Document B, fire safety … defines an atrium as: 'a space within a building, not necessarily vertically aligned, passing through one or more structural [floors]'`——支持"建筑内贯通多层空间"，但为消防定义，**不涉采光/通风/实例** |
| atrium | `flw-guggenheim` | ✅/true | `Solomon R. Guggenheim Museum - Frank Lloyd Wright Foundation`（200，52892B） | Frank Lloyd Wright Foundation（官方） | 官方机构 | null | **相关（直接、强·官方）**：`She wrote Frank Lloyd Wright in 1943`；`resembles a white ribbon curled into a cylindrical stack … spirals upwards towards a glass ceiling`；`never received a significant commission in New York` |
| atrium | `theartstory-wright` | ✅/true | `Wright Architecture, Bio, Ideas \| TheArtStory`（200，188632B） | TheArtStory | 学术著作 | null | **相关（直接、强）**：`Solomon R. Guggenheim Museum (1943-59)`；`a spiral ramp encircling a skylit atrium`；`the Guggenheim Museum building in New York City` |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（brutalism 5=5、atrium 4=4）。9 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。**
> **来源记录 `title` 字段核对（Minor）**：`flc-unite`（记录 `Unité d'habitation, Marseille — Fondation Le Corbusier` vs 实际 `<title>=Le Corbusier, Unité d'habitation, Marseille, France, 1945-1952`，机构相符但年份未录入）、`theartstory-brutalism`（记录 `Brutalism — TheArtStory` vs 实际 `Brutalist Architecture Movement Overview | TheArtStory`）、`theartstory-wright`（记录 `Frank Lloyd Wright — TheArtStory` vs 实际 `Wright Architecture, Bio, Ideas | TheArtStory`）为**副标题省略式记名**；`designingbuildings-atrium` 的 `author` 记为 `Wikipedia/机构`（实为 Designing Buildings 行业维基，**非 Wikipedia**）——均属存全名/机构更精确的**元数据 Minor**，不影响事实。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 brutalism（粗野主义，第48轮改动）——**合格（definition/overview 双源、实例四要素双独立源、无编造；仅个别 Minor）**
- 条目现状（实读）：`definition`＝"粗野主义以暴露的混凝土结构和大体量表达材料的真实性与社会性。"；`time_or_place`＝"20世纪、全球（参见来源）。"；`overview`＝"适用于公共建筑与纪念性项目；需要以结构清晰、体量组合明确为前提。"；`实例`＝"名称：马赛公寓（Unité d'habitation）；地点：法国马赛；设计者：勒·柯布西耶（Le Corbusier）；年份：1947–1952 年。以清水混凝土（béton brut）著称。…"
- **definition / 原理**（"暴露的混凝土结构 + 大体量 + 材料真实性 + 社会性"）**双源直证**：
  - `wp-brutalist-architecture`：`minimalist construction showcasing the bare building materials and structural elements over decorative design`（暴露材料/结构）＋`exposed, unpainted concrete`（暴露混凝土）＋`béton brut ("raw concrete")`＋`simple, honest, and functional buildings`（材料真实性）＋`massive in character`（大体量）＋`social housing influenced by socialist principles`（社会性）。
  - `theartstory-brutalism`：`raw concrete (French "béton brut") for exterior surfaces, leaving evidence of the construction`（暴露混凝土/材料真实性）＋`weight, density, and mass of concrete, steel, and stone`、`monumental simplicity`（大体量）＋`democratic-socialist visions of community`（社会性）。
  - → **"暴露的混凝土结构/大体量/材料真实性/社会性" 四点均获 wp + theartstory 两独立平台互证**，**非编造**。
- **time_or_place「20世纪、全球」**：`wp-brutalist-architecture` 信息框 `yearsactive: 1950s - early 1980s`、页尾分类 `20th-century architectural styles`；`theartstory-brutalism` `1950s`、`1954` 语境。→ "20世纪" 成立（"全球"为泛域桶，可接受）。
- **overview「公共建筑/纪念性；结构清晰、体量组合明确」**：wp `commonly used in the design of institutional buildings, such as provincial legislatures, public works projects, universities, libraries, courts, and city halls`＋`monumental`；theartstory `public`/`government`/`monumental simplicity`。→ 支撑。
- **实例四要素（马赛公寓）双独立源**：
  - `flc-unite`（Fondation Le Corbusier 官方）：标题 `Le Corbusier, Unité d'habitation, Marseille, France, 1945-1952`；`adopted in March 1947`——覆盖 名称/地点/设计者/年份（1945–1952，1947 定案）。
  - `theartstory-brutalism`（独立教育机构）：`Unité d'habitation (1952)`、`war-damaged Marseille`、`Le Corbusier`——覆盖 名称/年份(1952 落成)/地点/设计者。
  - `wp-unite-d-habitation` 全要素（`Unité d'habitation`/`Marseille`/`Le Corbusier`/`1947`/`1952`/`béton brut`）佐证。
  - → 实例四要素 + `béton brut` 由 **官方基金会 + TheArtStory（两独立机构）** 互证，**非编造**。
- **专项问题（Minor）**：
  - ① `wp-architectural-style` **全文无 `brutal` 字样**，仅定义"an architectural style is a classification of buildings…"——属**泛化/冗余来源**，对本条具体论断零覆盖（brutalism 的具体论断已由其余 4 源支撑，故不构成无源，但该源**不"直接相关"**，建议移除或替换为专述粗野主义之权威源）。
  - ② 实例年份"1947–1952"与官方源标题"**1945-1952**"存在口径差（1945 立项、1947 定案、1952 落成）。**非编造**（与"March 1947 定案 + 1952 落成"自洽），但建议注"项目 1945、1947 定案、1952 落成"。
- **内容判定：合格**（definition/原理 双源互证；实例四要素双独立机构直证；无编造；仅 wp-architectural-style 泛化、年份口径两处 Minor）。

### 3.2 atrium-architecture（中庭，第48轮改动）——**合格（主干定义与实例双源；仅"通风单源披露"与分类两处 Minor）**
- 条目现状（实读）：`definition`＝"建筑内部贯通多层、常覆以天窗的中央开敞空间。"；`time_or_place`＝"跨时期、全球（参见来源）。"；`overview`＝"中庭把天然光与空气引入建筑深处，改善内部环境。"；`实例`＝"名称：纽约古根海姆美术馆（Solomon R. Guggenheim Museum）；地点：美国纽约；设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1943 年委托、1959 年开馆。以螺旋坡道环绕顶部采光中庭。…"
- **definition「贯通多层 + 覆天窗 + 中央开敞空间」双源直证**：
  - `wp-atrium-architecture`：`a large open-air or skylight-covered space surrounded by a building`（覆天窗/围合）＋`modern atria … are often several stories high, with a glazed roof or large windows`（贯通多层 + 天窗顶）＋`the atrium was the open central court with enclosed rooms on all sides`（中央开敞）。
  - `designingbuildings-atrium`（引英国 Approved Document B）：`a space within a building, not necessarily vertically aligned, passing through one or more structural [floors]`（建筑内贯通多层空间）。
  - → 定义四要点由 **Wikipedia + Designing Buildings 两独立平台**互证，**非编造**。
- **time_or_place「跨时期、全球」**：`wp-atrium-architecture` `ancient roman dwellings`（古代罗马）→ `modern atria … late 19th and 20th centuries`（19–20 世纪）——**跨时期**成立；全球为泛域桶，可接受。（历史沿革由 wp 直述；designingbuildings 不涉史）
- **overview「天然光与空气引入建筑深处」**：`wp-atrium-architecture` `providing light and ventilation to the interior`（采光 + 通风）——**采光**由 wp + 实例源（theartstory `skylit atrium`、flw `glass ceiling`）互证；**通风/空气**仅 wp 单源（详见 Minor ①）。
- **实例四要素（古根海姆）双独立源**：
  - `flw-guggenheim`（Frank Lloyd Wright Foundation 官方）：`She wrote Frank Lloyd Wright in 1943`（1943 委托）＋`spirals upwards towards a glass ceiling`（螺旋/玻璃顶采光）＋`New York`。
  - `theartstory-wright`（独立教育机构）：`Solomon R. Guggenheim Museum (1943-59)`（1943–59）＋`a spiral ramp encircling a skylit atrium`（螺旋坡道环采光中庭）＋`New York City`。
  - → 名称/地点/设计者/年份(1943 委托、1959 开馆)/"螺旋坡道环顶部采光中庭" 由 **官方基金会 + TheArtStory（两独立机构）**互证，**非编造**。
- **专项问题（Minor）**：
  - ① **"通风/空气"机制仍实质单源**：`overview` 称"天然光与**空气**引入建筑深处"，但 9 源中仅 `wp-atrium-architecture` 明写 `light and ventilation`；`designingbuildings` 为消防竖向定义（不涉通风），两实例源只证**采光**（`skylit`/`glass ceiling`），**无第二源直证"通风/空气流动"**。第48轮把本条 `needs_verification` 由 true 置 false、清空 `pending_notes`、`待核实`改"暂无已知待核实项"，**未保留原"采光/通风依据偏单一权威来源"披露**——属**诚实性 Minor（漏披露通风单源）**：建议保留一句"通风机制据 wp 单源"或在正文以一般性说明呈现，或将 `overview` 收窄为"天然光（及通风）"并注明来源。
  - ② **分类口径（Minor，历史遗留）**：`theme=材料`，但"中庭"属**空间/采光要素**（更近"下沉空间/采光"维度），非"材料"。条目与 `coverage.json` **一致**（非本轮改动引入），仅分类质量存疑，建议后续复核维度归属。
  - ③ `designingbuildings-atrium` 的 `author` 记 `Wikipedia/机构` 不精确（实为 Designing Buildings 行业维基）——元数据 Minor（见 §二注）。
- **内容判定：合格**（主干 definition 与实例四要素均双独立源直证、无编造；仅"通风单源披露缺失"、theme 分类、author 记名三处 Minor；不构成"不合格"，亦不足以整体改判"待核实"——核心形制与实例已达双源）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：9 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）；`link_ok`：wp 三源 true，其余六源 null（三态未标，非死链、非假源）。**9 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：wp-brutalist(200)/wp-architectural-style(200)/wp-unite-d-habitation(200)/flc-unite(200)/theartstory-brutalism(200)/wp-atrium(200)/designingbuildings-atrium(200)/flw-guggenheim(200)/theartstory-wright(200)——**9/9 全部 HTTP 200**，无死链（体检 F 之"死链"对本次 9 源为 0）。
- **相关性结论**：
  - brutalism：`wp-brutalist-architecture`、`wp-unite-d-habitation`、`flc-unite`（官方）、`theartstory-brutalism` **4 源直接相关**；`wp-architectural-style` **泛化不相关**（不涉 brutalism，Minor①）。
  - atrium：`wp-atrium-architecture`、`designingbuildings-atrium`（定义型）、`flw-guggenheim`（官方）、`theartstory-wright` **4 源均直接相关**（designingbuildings 为消防定义、较薄但直接命中"atrium 定义"）。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | 含「示意图，非施工图」 | viewBox / 元素出界 | 规范句收尾 | on* 事件属性 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| brutalism | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400；矩形/文字 x∈[120,640]、y∈[90,370]，**不出界**；`check.py` PASS | ✓ | 无 |
| atrium-architecture | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400；x∈[100,660]、y∈[60,375]，**不出界**；`check.py` PASS | ✓ | 无 |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含"示意图，非施工图"、无 `on*` 事件属性；「常见错误与限制」段均以"实际工程须按当地规范和专业设计人员的要求"收尾；`check.py` 含 SVG 出界检查，本轮 PASS。**机械项两条全部通过。**

### SVG 质量观察（形态贴合主题，但缺「设计意图/尺寸关系」显式标注——次要、系统性）
- **brutalism**：`<rect>` 外框 + 内嵌体量块（x=180/380）+ 标题"粗野混凝土体量"——**贴合"粗野混凝土体量组合"主题、非随机占位**；但仅标题 + "示意图，非施工图"，**缺 TASK_design 第6条「图中标注设计意图或尺寸关系」**（次要、系统性）。
- **atrium-architecture**：顶部基线（屋面/天窗）+ 中央竖虚线（采光中庭）+ 左右房间块——**贴合"天窗采光中庭"剖面主题、非随机占位**；同样**未标注"天窗/中庭"等设计意图或尺寸关系**（次要、系统性）。
- **判定**：两条「一图」机械项（1 张 + viewBox + "示意图，非施工图" + 不出界 + 无事件属性）全过，图形与主题相关；**唯一不足为「缺图中设计意图/尺寸关系标注」**——`check.py` 只查出界与注记，查不出该语义项，属**次要/可提升**，不构成本轮"不合格"。建议全站统一补强（延续第 44–48 轮方向）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对）：brutalism（粗野主义/风格/重要/20世纪/全球/L2）、atrium-architecture（中庭/材料/重要/跨时期/全球/L2）；`source_count` 与来源数组长度一致（5=5、4=4）；`needs_verification_count`：各 0；`related`：brutalism=`["structuralism"]`、atrium=`["daylighting"]`（无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| brutalism | false | "" | "暂无已知待核实项。" | **一致** ✓（definition/实例均双源，nv=false 可接受） |
| atrium-architecture | false | "" | "暂无已知待核实项。" | **结构一致** ✓（但**第48轮清除了原"采光/通风偏单一"披露，通风仍 wp 单源**，见 §三 3.2 Minor①——属"联动一致但内容欠完整/略乐观"） |

> 说明（D14 精神）：atrium 第48轮把 `needs_verification` 由 true→false 并清空 `pending_notes`/`待核实`。实例四要素确已双源、可支持"实例待核实"关闭；但原 `pending_notes` 另含"**采光/通风依据偏单一权威来源**"一义，其中**通风**仍实质单源（除 wp 外无第二机制源），清除时未保留该点。建议在 `overview`/`原理` 或 `待核实` 中保留一句通风单源披露（Minor）。

### 元数据/批次注
- **type/year**：9 源 `year=null`（在线动态页，D06 允许）；`flc-unite`/`flw-guggenheim` 为**官方机构**（强权威），`theartstory-*` 为学术著作（中—强），`designingbuildings-atrium` 为行业维基（定义型、薄）。
- **抽样范围注**：第48轮改动 5 条中，本轮仅对 `atrium-architecture`、`brutalism` 做内容核对；`parametric-architecture`、`deconstructivism`、`two-point-perspective` **本轮未做内容核对**（不在本次 2 条内，仅列名备查）。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| brutalism | **0.3776** vs constructivism | <0.54 ✓ | **0.4094** vs minimalism-architecture | <0.54 ✓ |
| atrium-architecture | **0.4444** vs courtyard | <0.54 ✓ | **0.4622** vs circulation | <0.54 ✓ |

> 对**既有 257 条**（排除自身）逐条扫描，两条两档均 **<0.54**（短文本最大 0.4444、全字段最大 0.4622）——**各自与既有库文本区分在阈值内**。
> - brutalism 最近邻：短文本 `constructivism`(0.3776)/`critical-regionalism`(0.3521)/`high-tech`(0.3511)；全字段 `minimalism-architecture`(0.4094)/`art-deco`(0.3993)/`beaux-arts`(0.3982)（同属风格史，正常；仍 <0.54）。
> - atrium 最近邻：短文本 `courtyard`(0.4444)/`atrium-ventilation`(0.3740)/`reflected-light`(0.3729)；全字段 `circulation`(0.4622)/`organic-architecture`(0.4473)/`postmodernism`(0.4128)（`atrium` 与 `courtyard`/`circulation` 空间概念近邻正常；全字段 0.4622 相对偏高但仍 <0.54）。
> **均未越线。**

### 7.2 第48轮 5 条批内去模板化核验（两两，全字段②）
| 对 | 短文本 | 全字段 |
| --- | --- | --- |
| atrium-architecture vs parametric-architecture | 0.2571 | 0.3168 |
| atrium-architecture vs deconstructivism | 0.2329 | 0.3651 |
| atrium-architecture vs brutalism | 0.2286 | 0.3413 |
| atrium-architecture vs two-point-perspective | 0.1401 | 0.2743 |
| parametric-architecture vs deconstructivism | 0.1807 | 0.3525 |
| parametric-architecture vs brutalism | 0.2125 | 0.2899 |
| parametric-architecture vs two-point-perspective | 0.1695 | 0.3406 |
| deconstructivism vs brutalism | 0.3133 | 0.3237 |
| deconstructivism vs two-point-perspective | 0.1311 | 0.3598 |
| brutalism vs two-point-perspective | 0.1582 | 0.2850 |

> 第48轮 5 条**两两均远低于 0.54**（批内全字段最大 **0.3651**，atrium↔deconstructivism）——**无第43轮 batch-42 式双条互为模板姊妹、无套话风险**。

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第 39–48 轮报告**逐位一致**，口径正确。

> **文本相似度判定：两条对既有库与批内均 PASS（均 <0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 文本相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **brutalism（粗野主义）** | definition/原理（暴露混凝土/大体量/材料真实性/社会性）**wp+theartstory 双源互证**；overview 公共/纪念性双源；实例四要素 + béton brut **flc-unite(官方)+theartstory 双独立源**；无编造；**Minor：wp-architectural-style 未涉 brutalism（泛化）、年份 1947–1952 vs 官方 1945-1952 口径差** | 5/5 true；wp-brutalist/unite、flc、theartstory 直接强源，wp-architectural-style 泛化；**5 源 200 可达** | 七节齐、规范句✓；1 SVG 含"示意图，非施工图"、形态贴合，**缺意图/尺寸标注（次要）** | 全部一致；nv=false/pending="" /待核实"暂无" 一致 | 既有库 ✓（0.3776/0.4094）；批内 ✓（max 0.3651） | **合格** |
| **atrium-architecture（中庭）** | definition（贯通多层+覆天窗+中央开敞）**wp+designingbuildings 双源**；overview 采光双源（通风 wp 单源）；实例四要素 + 螺旋坡道环采光中庭 **flw-guggenheim(官方)+theartstory 双独立源**；无编造；**Minor：通风单源未披露、theme=材料 分类存疑** | 4/4 true；wp-atrium、flw、theartstory 直接强源，designingbuildings 定义型（薄）；**4 源 200 可达** | 七节齐、规范句✓；1 SVG 含"示意图，非施工图"、形态贴合，**缺意图/尺寸标注（次要）** | 全部一致；nv=false/pending="" /待核实"暂无" 一致（**但清除原"采光/通风偏单一"披露，通风单源漏披露**） | 既有库 ✓（0.4444/0.4622）；批内 ✓（max 0.3651） | **合格** |

### 问题清单（均为 Minor，不阻断）
- **① brutalism 泛化来源**：`wp-architectural-style` 全文无 `brutal` 字样，仅定义"architectural style"，对本条具体论断零覆盖——**非无源（其余 4 源已支撑）**，但建议移除或换为专述粗野主义之权威源。
- **② brutalism 实例年份口径**：条目"1947–1952"vs 官方 `flc-unite` 标题"1945-1952"（1945 立项/1947 定案/1952 落成）。**非编造**，建议在 `实例` 注全"项目 1945、1947 定案、1952 落成"。
- **③ atrium 通风单源漏披露**：`overview`"天然光与**空气**"中"通风/空气"仅 `wp-atrium` 单源（designingbuildings 为消防竖向定义、实例源只证采光）；第48轮清空 `pending_notes`/`待核实` 未保留原"采光/通风偏单一"披露——建议保留一句通风单源披露或补第二机制源。
- **④ atrium theme 分类**：`theme=材料`，中庭属空间/采光要素（更近"下沉空间/采光"维度）。条目与 coverage 一致（历史遗留），建议后续复核维度归属。
- **⑤ SVG"设计意图/尺寸关系"标注缺失（两条例、系统性）**：两图机械项与主题贴合均过，但缺 TASK_design 第6条"图中标注设计意图或尺寸关系"——建议全站统一补强（延续第 44–48 轮）。
- **⑥ 来源元数据瑕疵（轻微）**：`flc-unite`/`theartstory-brutalism`/`theartstory-wright` 的 `title` 为副标题省略式记名（建议存全名）；`designingbuildings-atrium` 的 `author` 记"Wikipedia/机构"（实为 Designing Buildings 行业维基，非 Wikipedia）。

## 九、总体结论与建议

- **抽样结果**：本轮抽第48轮改动 5 条中的 **2 条**——`atrium-architecture`、`brutalism`（2/5＝40%，lead 定向补抽）。**内容维度：2 合格 ＋ 0 待核实 ＋ 0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：9 个引用来源 id **全部存在、verified=true、实抓 9/9 HTTP 200 可达**。两条实例四要素（马赛公寓；纽约古根海姆）均获**官方机构源（Fondation Le Corbusier / Frank Lloyd Wright Foundation）+ 独立教育机构（TheArtStory）双独立源**直证；definition 亦双源（brutalism：wp+theartstory；atrium：wp+designingbuildings）。唯 `wp-architectural-style` 泛化（不涉 brutalism，Minor）。
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 形态贴合与唯一性通过、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：两条 nv=false 与 `pending_notes=""`/`待核实="暂无"` 结构一致；**但 atrium 第48轮清除原通风单源披露，属"一致但欠完整"（Minor③）**。
- **相似度层面**：两条对既有库与批内均 <0.54（PASS）；批内最大 0.3651，无套话；方法自校 0.5157 与第 39–48 轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——**0 不合格**（2 合格），0 编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——两条对既有库与批内均 <0.54。
  3. **结论：本轮 2 条均判「合格」，不触发整批返工/降级。** 与第47轮（2 条均"待核实"、关键形制单源）相比，**第48轮通过"补具名实例 + 补第二独立机构源"实质性改善了来源深度**：两条实例四要素与核心定义均达双独立源，**无编造、无关键形制单源**。
- **返工/修复建议（均为 Minor、非阻断，宜下一轮体检顺手处理）**：
  1. **（宜做，问题①）**：移除/替换 `wp-architectural-style` 泛化来源，或补一份专述粗野主义的权威源。
  2. **（宜做，问题②）**：`brutalism` 实例年份注明"项目 1945、1947 定案、1952 落成"，消解与官方标题"1945-1952"的口径差。
  3. **（宜做，问题③）**：`atrium` 在 `overview`/`原理`/`待核实` 保留一句"通风机制据 wp 单源"披露，或补第二机制源，使 nv=false 完全站得住。
  4. **（宜做，问题④）**：复核 `atrium` 的 `theme=材料` 维度归属（建议归"下沉空间/采光"）。
  5. **（宜做，问题⑤，系统性）**：为两图补「设计意图或尺寸关系」文字标注，并全站统一补强（延续第 44–48 轮）。
  6. **（宜做，问题⑥）**：三个来源 `title` 存全名，`designingbuildings-atrium` 的 `author` 改为"Designing Buildings（行业维基）"。
- **流程记录**：本轮抽检 2 条＝**内容 2 合格、0 待核实、0 不合格、0 编造、0 假 id、0 死链、七节/规范/元数据/pending 结构联动一致、check.py PASS、相似度全 <0.54**；**主要遗留：两条均为 Minor 级打磨（brutalism 泛化源+年份口径；atrium 通风单源未披露+theme 分类；SVG 尺寸/意图标注系统性；少量来源 title 元数据），无内容/结构硬缺陷，不触发 §E 整批返工/降级。**

---

### 机器可读汇总

```
ROUND=49
SAMPLER=spotcheck-r49
MODE=第48轮改动5条中定向抽2条（atrium-architecture / brutalism）；另 parametric/deconstructivism/two-point 未内容核对
SCOPE=["atrium-architecture","brutalism"]
FILES={"brutalism":"entries/batch-04.json","atrium-architecture":"entries/batch-25.json"}
ROUND48_COMMIT="358cb9a feat: round48 five named instances, zero-gap 1/3"
ROUND48_CHANGED=["atrium-architecture","parametric-architecture","deconstructivism","brutalism","two-point-perspective"]
STATE={"sources.json":"161837B@2026-11-23 11:39","coverage.json":"87346B@2026-11-23 11:39","batch-04.json":"11987B@2026-11-23 11:39","batch-25.json":"10775B@2026-11-23 11:39","check.py":"15908B@2026-11-22 15:11","total":258,"all_level":"L2","pending_sum":217,"sources_total":343,"sources_verified_true":340,"sources_verified_false":3,"link_ok_true":145,"link_ok_false":6,"link_ok_null":192}
GIT_HEAD="358cb9a"; GIT_STATUS="clean except untracked research/b1-round49.md (lead's B1 note, untouched); targets stable in HEAD"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2/5 (第48轮改动5条抽2条, 40%; lead 定向补抽)"
FETCH_METHOD="urllib+ChromeUA; 9/9 HTTP200; phrase substring verify norm(quote) in norm(page); analysis in-memory (stdin heredoc, no persistent file)"
SOURCES={"count_distinct":9,"count_refs":9,"all_exist":true,"all_verified_true":true,"all_reachable_200":"9/9",
 "brutalism":{"wp-brutalist-architecture":true,"wp-architectural-style":true,"wp-unite-d-habitation":true,"flc-unite":null,"theartstory-brutalism":null},
 "atrium-architecture":{"wp-atrium-architecture":true,"designingbuildings-atrium":null,"flw-guggenheim":null,"theartstory-wright":null},
 "relevance":{"brutalism":"wp-brutalist/unite+flc(官方)+theartstory 直接强源; wp-architectural-style 泛化(不涉 brutalism)",
              "atrium-architecture":"wp-atrium+flw(官方)+theartstory 直接强源; designingbuildings 定义型(消防,薄)直接"},
 "title_note":"flc-unite / theartstory-brutalism / theartstory-wright title 副标题省略; designingbuildings author='Wikipedia/机构' 不精确 -> minor"}
BODY_SUPPORT={
 "brutalism":"definition/原理 暴露混凝土+大体量+材料真实性+社会性 双源(wp-brutalist+theartstory); 实例四要素+béton brut flc-unite(官方)+theartstory 双独立源; wp-unite 全要素佐证; time 20世纪(wp yearsactive 1950s-early1980s / 20th-century); overview 公共/纪念性双源; VERDICT=合格 (Minor: wp-architectural-style 泛化; 年份 1947-1952 vs 官方 1945-1952)",
 "atrium-architecture":"definition 贯通多层+覆天窗+中央开敞 双源(wp-atrium+designingbuildings ApprovedDocB); 实例四要素+螺旋坡道环采光中庭 flw-guggenheim(官方)+theartstory 双独立源; time 跨时期(Roman->19/20c); overview 采光双源/通风仅 wp 单源; VERDICT=合格 (Minor: 通风单源未披露; theme=材料 分类存疑)"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2, 无出界, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","on_attr":"none"}
SVG_NOTE={"brutalism":"rect外框+体量块(粗野混凝土体量) topical; 缺设计意图/尺寸标注","atrium-architecture":"屋面基线+中央采光中庭竖虚线+两侧房间 topical; 缺设计意图/尺寸标注","verdict":"机械项全过; 缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x2","source_count":"5=5 / 4=4","nvc":"0 x2","needs_verification":"false x2","related":"brutalism=[structuralism], atrium=[daylighting] 无悬空","pending_consistency":"结构一致 x2; 但 atrium 清除原'采光/通风偏单一'披露, 通风仍 wp 单源(Minor)"}
SIMILARITY={
 "brutalism":{"vs_existing_short":0.3776,"short_entry":"constructivism","vs_existing_full":0.4094,"full_entry":"minimalism-architecture","verdict":"PASS<0.54"},
 "atrium-architecture":{"vs_existing_short":0.4444,"short_entry":"courtyard","vs_existing_full":0.4622,"full_entry":"circulation","verdict":"PASS<0.54"},
 "round48_pairwise_full_max":0.3651,"round48_pairwise_full_max_pair":"atrium-architecture vs deconstructivism",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-48 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"brutalism":"合格","atrium-architecture":"合格"}
VERDICT_SVG={"brutalism":"机械项通过/主题贴合, 缺意图·尺寸标注(次要)","atrium-architecture":"机械项通过/主题贴合, 缺意图·尺寸标注(次要)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
BATCH_ACTION="No rollback/downgrade: 0 不合格 (2 合格), 0 fabrication/0 fake id/0 dead link; similarity all <0.54. Optional minor polish: (1) brutalism 移除/替换 wp-architectural-style 泛化源; (2) brutalism 实例注'1945立项/1947定案/1952落成'; (3) atrium 保留通风单源披露或补第二机制源; (4) atrium theme 复核维度; (5) 两图补设计意图/尺寸标注(site-wide); (6) 来源 title 全名 + designingbuildings author 更正."
READONLY="only wrote research/spotcheck-round49.md; no other project file changed (research/b1-round49.md untouched); no git commit; web content treated as data, no instruction executed; analysis in-memory (stdin heredoc, no persistent file)"
```

*（报告完）*
