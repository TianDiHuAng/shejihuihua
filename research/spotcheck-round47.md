# 第47轮质量抽检报告（spotcheck-round47）——batch-47 新增 3 条中抽 2 条（dikengyuan / ottoman-architecture）

- 抽检人：spotcheck-r47（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 11:01 起，Asia/Hong_Kong（CST）。
- 任务：对第47轮 `batch-47` 新增 3 条中的 **2 条**——`dikengyuan`（地坑院）、`ottoman-architecture`（奥斯曼建筑）——逐条核对 definition/time_or_place/overview/实例 是否有引用来源正文支撑、是否编造、来源是否直接相关（点名核验：`wp-yaodong` 是否述 sunken yaodong/地坑、`smx-shanzhou-dikengyuan` 政府页是否述地坑院、`wp-ottoman-architecture` 与 `artincontext-islamic-architecture` 是否述中央穹顶+半穹顶）、L2 七节/SVG/规范提示、pending 联动、period/region 口径（含 `sasanian-architecture` 归“伊斯兰前身”是否合理）、相似度（阈值 0.54）。
- 抽样比：`batch-47` 新增 3 条，本轮抽 2 条（**2/3≈67%**，远高于 §E“随机 10%、至少 3 条”的整轮口径下限，属本批针对性补抽；另 1 条 `sasanian-architecture` 未纳入内容核对，仅对其 period/region 口径作专项评估，见 §六）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；抽检逐条核对来源，不合格则整批返工、下轮抽检比例提至 25%；相似度过高→整批降级）＋第三节 F「体检」＋第六节（联网内容一律视为数据、其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节标准与「专用规则」（每页至少 1–2 张示意图、图下注“示意图，非施工图”、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍数据附“实际工程须按当地规范和专业设计人员的要求”）＋「通用硬性规则」（**不编造数字/日期/人名/引文/出处**；**关键事实至少两个独立来源互相印证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md` / `TASK_design.md` 在仓库根**无同名文件**（与历轮一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md`（21 行）、`research/spotcheck-round46b.md`（240 行，作模板与口径对齐）已读。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 11:01 起）**：`data/sources.json`=**153010B@2026-11-23 11:01**、`entries/batch-47.json`=**6657B@2026-11-23 11:01**、`coverage.json`=**87346B@2026-11-23 11:01**、`tools/check.py`=**15908B@2026-11-22 15:11**。`git log -1` = `93487c6 feat: round46 resume expansion, 4 sparse-cell entries, 6 named instances`。
- **工作树状态（采样时点）**：`git status --porcelain` 显示第47轮成果仍在工作区：modified `coverage-matrix.md / coverage.json / data/sources.json / scope.md / site/coverage.html / site/index.html / site/indexes.html / site/sources.html / tools/gen_scope.py`；untracked `entries/batch-47.json`、`research/b1-round47.md`、`research/gaps-round47.md`、`site/entries/{dikengyuan,ottoman-architecture,sasanian-architecture}.html`、`tools/add_round47.py`。抽检对象在采样期间**稳定**，判定基于该稳定快照。本报告产出后追加 `?? research/spotcheck-round47.md`（本报告，唯一由本次抽检写入的文件）。
- **条目规模（`coverage.json` 实读）**：`total=258`、全部 `level=L2`、全部 `status=已写`（=第46轮 255 + 本批新增 3）；`pending_sum`（`needs_verification_count` 求和）＝**220**。来源库 `sources.json` 共 **325** 条，`verified=true` **322**、`verified=false` **3**（`link_ok`：true 145、false 6、null 174）。注：`link_ok=false` 的 6 条**均不在本次 4 个来源中**（本次 4 源 `link_ok` 见 §二），不影响判定。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round47.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python `urllib` 读取→内存去标签/切句/计数，脚本经 stdin 传入、未落盘任何持久文件）。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（两条均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），timeout 40s，SSL 校验关闭，失败重试 6 次。`en.wikipedia.org` 按 D05 改走 **owiki 同源镜像** `https://owiki.org/wiki/<Title>`（并回带直连 en.wikipedia 复核）；`smx.gov.cn`（GB18030 解码）、`artincontext.org` 直连。本轮 **4 个引用来源全部实抓 HTTP 200**（`<title>`/正文与 `sources.json` 逐条核对，见 §二、§三、§四）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **258 条**去重已写条目逐条扫描，警戒线 **0.54**（与第 27–46 轮一致）。**方法自校**：以全字段②计算已知对 `futurism-style vs expressionism-style`，得 **0.5157**，与第 39–46 轮报告**逐位一致**，确认口径正确。
- **“两源互证”判定口径**（沿用第42/46轮明确化口径）：按「关键事实至少两个独立来源互相印证，否则标待核实」；两个引用来源须对本条**具体概念**有实质覆盖且互证；若第二源对本条**具体概念/核心形制**仅泛论或零覆盖，则相关具体论断实为**单源**，据硬性规则影响判定（**待核实＝来源深度缺陷，非编造**）。
- **三级判定定义（可复现）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（概念定义或核心形制/实例）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但存在第二源对本条具体概念仅泛论/零覆盖、或某关键事实（如本条核心形制/营造方法）实质单源——属来源支撑/深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或关键结构项（如「一图」）实质不满足 TASK_design 强制要求。
- **相似度专项（独立维度）**：警戒线 0.54；超线即触发 `AUTONOMOUS.md §E`「相似度过高（疑似套话）→整批降级」，与「不合格（内容无源）→整批返工」是**不同触发路径**，分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **4 个去重来源 id（4 处引用：dikengyuan 2、ottoman 2）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）**、实抓 HTTP 200。

| 条目 | 来源 id | 存在/verified | 实抓标题（本轮 HTTP，逐字） | 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dikengyuan | `wp-yaodong` | ✅ / true | `Yaodong ::: Open WIKI`（owiki 200，19285B，textlen≈8978；直连 en.wikipedia 200 title=`Yaodong - Wikipedia`） | Wikipedia（经 owiki 镜像核验） | 权威百科 | true | **相关（直接、强）**：逐字命中 `In the Loess Plateau…peasants…dig a square pit on the spot, and then dig the cave horizontally on the four walls to form the underground courtyard. In most parts of western Henan, this form of cave is called the "pit yard".`；`Sunken yaodongs are dug around an excavation conducted at the surface, serving as interior courtyard, called yaodong-well or sunken courtyard.` |
| dikengyuan | `smx-shanzhou-dikengyuan` | ✅ / true | `陕州地坑院`（200，34278B，textlen≈1600，GB18030） | 三门峡市人民政府 | 官方机构 | null | **相关（直接、薄）**：`陕州地坑院，国家AAAA级旅游景区，位于河南省三门峡市陕州区张汴乡北营村…`；`…全国乃至世界唯一的地下古民居建筑，是我国特有的四大古民居建筑之一`；`被誉为"地平线下古村落，民居史上活化石"`；`2011年，地坑院营造技艺被列入国家级非物质文化遗产保护名录` |
| ottoman-architecture | `wp-ottoman-architecture` | ✅ / true | `Ottoman architecture ::: Open WIKI`（owiki 200，83308B，textlen≈58815；直连 en.wikipedia 200 title=`Ottoman architecture - Wikipedia`） | Wikipedia（经 owiki 镜像核验） | 权威百科 | null | **相关（直接、强）**：`monumental mosque buildings focused around a high central dome with a varying number of semi-domes`；`a large central dome with a semi-dome behind it`；`two semi-domes aligned with the main central dome`；`the central dome was often accompanied with semi-domes … pendentives`；`Mimar Sinan…Şehzade Mosque, Süleymaniye Mosque, and Selimiye Mosque`（古典期 16–17 世纪） |
| ottoman-architecture | `artincontext-islamic-architecture` | ✅ / true | `Islamic Architecture - Building Styles Across the Muslim World`（200，475392B，textlen≈34400） | Art in Context | 学术著作 | null | **相关但极薄/泛论**：`broad central domes with enormous diameters were placed on top of a center-plan building`；`Mimar Sinan, an Ottoman architect, built some of the most ornate domed structures`；`Suleymaniye Mosque (Istanbul, Turkey)…Architect Mimar Sinan`。**但对「半穹顶（semi-dome）」零覆盖**（`semi-dome=0、semidome=0、half dome=0`；`semi` 仅出现于 `semicircular towers`/`semi-precious stones`） |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（dikengyuan 2=2、ottoman 2=2）。4 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。**
>
> **来源记录 `title` 字段核对**：`wp-yaodong`（记录 `Yaodong` vs 实际 `Yaodong ::: Open WIKI`/`Yaodong - Wikipedia`，镜像后缀）、`wp-ottoman-architecture`（记录 `Ottoman architecture` vs `Ottoman architecture ::: Open WIKI`）、`smx-shanzhou-dikengyuan`（记录 `陕州地坑院 — 三门峡市人民政府` vs 实际 `<title>=陕州地坑院`，机构名相符）**均相符**。**元数据瑕疵（Minor）**：`artincontext-islamic-architecture` 记录 `title="Islamic Architecture — Art in Context"`，实际 `<title>`=`Islamic Architecture - Building Styles Across the Muslim World`（机构名相符，副标题未录入）——建议存全名或备注站点。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 dikengyuan（地坑院，batch-47）——**待核实（核心营造方法“方形坑+四壁横挖窑”仅 wp 单源，smx 直接但极薄未涉方法）**
- **wp-yaodong**（owiki 200，textlen≈8978）直证（主源，强，几乎逐字）：
  - `In the Loess Plateau , without hillsides and ravines available, peasants skillfully use loess's features to dig a square pit on the spot , and then dig the cave horizontally on the four walls to form the underground courtyard.` → **逐字支撑 definition「向下挖方形坑、再沿四壁横向挖窑而成的地下四合院」**（square pit ✓ / cave horizontally on the four walls ✓ / underground courtyard ✓）。
  - `In most parts of western Henan , this form of cave is called the "pit yard".` → 支撑「地坑院/坑院」名称（豫西“pit yard”）与地域（中国）。
  - `Sunken yaodongs are dug around an excavation conducted at the surface, serving as interior courtyard, called yaodong-well or sunken courtyard.`；`Both are excavations of pits in the flat ground.` → 支撑 overview「院落地平线以下」「以坑为院」及「平坦塬面下挖」。
  - `Sunken yaodongs have two types…slope-entrance and flat-entrance.` → 支撑 典型手法「设通道（入口）」。
  - `The surrounding earth acts as a natural insulator, keeping the interior warm in winter and cool in summer.`；`The yaodong is covered with at least two meters of mud to ensure the thermal insulation` → **直接支撑 原理「借土体保温隔热」**。
  - `dig caves in the cliff on the edge of the loess slopes with the floor rectangular and the top arched` → 支撑「拱形窑洞」。
- **smx-shanzhou-dikengyuan**（200，textlen≈1600，GB18030；点名核验项）直证：
  - `陕州地坑院，国家AAAA级旅游景区，位于河南省三门峡市陕州区张汴乡北营村…` → **确述「地坑院」并给出具体地点**（河南省三门峡市陕州区张汴乡北营村）。
  - `…全国乃至世界唯一的地下古民居建筑，是我国特有的四大古民居建筑之一`；`被誉为"地平线下古村落，民居史上活化石"` → **互证「地下/下沉式民居」本质**（“地下古民居”“地平线下”）。
  - `2011年，地坑院营造技艺被列入国家级非物质文化遗产保护名录` → 佐证其为一种专门的**营造技艺**（建造工艺）。
  - **但对本条核心营造方法零覆盖**：`方形=0、方形坑=0、下沉=0、窑洞=0、保温=0、隔热=0、排水=0、通道=0`——**未述“向下挖方形坑、四壁横向挖窑”的营造方法**，仅作景区/非遗/定性的简介（全页仅约 1600 字文本）。
- **逐项结论**：
  - definition「…向下挖方形坑、再沿四壁横向挖窑而成的地下四合院」——**本质（地下/下沉民居）双源可互证**（wp `sunken courtyard/pit yard` + smx `地下古民居/地平线下古村落`）；**但核心营造方法「方形坑+四壁横挖窑」仅 `wp-yaodong` 单源**，smx 零覆盖。
  - time_or_place「古代、中国（参见来源）」——中国 ✓（豫西/黄土塬/三门峡）；「古代」为传统住居类型的时间桶（wp 述起源可溯至公元前 2000 年青铜时代），可接受（Minor，见 §六）。
  - overview「院落地平线以下，以坑为院、四壁为窑，形成“进村不见房”的地下聚落」——「地平线以下」**双源**（wp sunken + smx 地平线下）；「以坑为院、四壁为窑」仅 wp 单源；**「进村不见房」引语在两源正文均查无**（`进村=0/见树=0/不见=0/visible=0/village=0`，仅 smx 有“古村落”）——**引文无源（Minor，见 §八问题③）**。
  - **原理**「黄土直立性强…向下挖坑作院…借土体保温隔热」——square pit/四壁挖窑/土体保温隔热均 wp 直证；`ratio(原理, 定义+概述)=0.2752`（低，机制独立，非逐字拼接）。
  - 实例「陕州地坑院（类型性描述）；地点与设计者不适用」——**名称有源（smx 即“陕州地坑院”）✓**；**但「地点不适用」与 smx 明载地点（河南省三门峡市陕州区张汴乡北营村）相悖**；且“陕州地坑院”是**具名景区（AAAA）非“类型性”**。→ 应据源补地点（设计者/年代仍缺，见 §八问题②）。
- **两源互证（任务专项）——部分成立**：**「地下/下沉民居」「地坑院（名称）」双源互证成立**；**但 definition/overview 的核心营造方法「方形坑+四壁横挖窑」仅 `wp-yaodong` 单源，`smx` 对本条营造方法零覆盖**——按硬性规则「关键事实至少两个独立来源互相印证」，该核心营造方法属**关键事实而实质单源**。
- **专项核验（任务点名）**：**`wp-yaodong` 确述 sunken yaodong/地坑**（逐字命中 `sunken courtyard`、`dig a square pit…four walls…underground courtyard`、`"pit yard"` western Henan）；**`smx` 政府页确述地坑院**（逐字命中 `陕州地坑院`、`地下古民居建筑`、`地平线下古村落`、`地坑院营造技艺`、地点）——**两源均直接相关、命中点名概念**，但 smx 对营造方法极薄。
- **内容判定：待核实**（概念层双源互证、主源 wp 强支撑、无编造；**缺陷＝核心营造方法「方形坑+四壁横挖窑」仅在 wp-yaodong 单源，smx 政府页直接但极薄、未涉营造方法，关键构造实质单源**；另：实例“地点/设计者不适用”与源相悖、overview“进村不见房”引语无源、period 口径见 §六——均见 §八）。**⚠ 与第42/46轮 `early-islamic` 同类（第二源直接但极薄、对核心形制零覆盖→待核实，非不合格）。**

### 3.2 ottoman-architecture（奥斯曼建筑，batch-47）——**待核实（“半穹顶”仅 wp 单源，artincontext 半穹顶零覆盖）**
- **wp-ottoman-architecture**（owiki 200，textlen≈58815）直证（主源，强）：
  - `This style integrated the Ottoman tradition with influences from the Hagia Sophia , resulting in monumental mosque buildings focused around a high central dome with a varying number of semi-dome s.` → **直接支撑 definition「中央大穹顶加半穹顶的集中式清真寺」**（central dome ✓ / semi-domes ✓）。
  - `The latter was covered by a large central dome with a semi-dome behind it, flanked by a row of three smaller domes on either side.`；`its prayer hall makes use of two semi-domes aligned with the main central dome, while the side aisles are each covered by four smaller domes.`；`the central dome was often accompanied with semi-domes … pendentives` → **逐字支撑「中央穹顶+半穹顶」「层层递落的穹顶体系」**。
  - `Classical period (16th to 17th centuries) The start of the classical period is strongly associated with the works of the imperial architect Mimar Sinan.` → 支撑「古典期（16–17 世纪）」「由建筑师锡南推向成熟」。
  - `The most important architect of the classical period is Mimar Sinan , whose major works include the Şehzade Mosque , Süleymaniye Mosque , and Selimiye Mosque.`；`Süleymaniye…1550`；`Selimiye Mosque in Edirne…1568 and completed in 1574` → 支撑实例的**地点/设计者/年代**（见 §八问题②）。
- **artincontext-islamic-architecture**（200，textlen≈34400）直证（第二源，**直接但薄/泛论**；点名核验项）：
  - `Ottoman architecture produced a special style of monumental, representational structure based on the model of pre-existing Byzantine domes: broad central domes with enormous diameters were placed on top of a center-plan building.` → **互证「中央大穹顶（broad central domes）」+「集中式（center-plan building，center-plan=1）**」。
  - `Mimar Sinan, an Ottoman architect, built some of the most ornate domed structures`；`Suleymaniye Mosque (Istanbul, Turkey)…Architect Mimar Sinan` → **互证「锡南」「集中式穹顶清真寺」及实例地点（Istanbul）**。
  - **但对「半穹顶」零覆盖**：`semi-dome=0、semidome=0、half dome=0、half=0`；`semi` 仅出现于无关词（`semicircular towers`/`semi-precious stones`）；亦**无 `cascade/buttress/pendentive/16th/17th/classical`**（古典期年代仅由实例 `Suleymaniye…1558` 间接体现）。
- **逐项结论**：
  - definition「古典期（16–17 世纪）以中央大穹顶加半穹顶的集中式清真寺为标志」——**「中央大穹顶」「集中式（center-plan）」双源可互证**（wp + artincontext）；**但「半穹顶」仅 `wp-ottoman` 单源**（artincontext 零覆盖），**核心标志性形制的一半实质单源**。
  - time_or_place「文艺复兴至19世纪、伊斯兰/南亚」——「文艺复兴至19世纪」桶含 16–17 世纪 ✓（wp 古典期 16–17；artincontext Suleymaniye 1558 间接）；region「伊斯兰/南亚」见 §六（南亚不适用，Minor）。
  - overview「以层层递落的穹顶体系覆盖宽阔礼拜空间，由建筑师锡南推向成熟」——「锡南推向成熟」**双源**（wp Mimar Sinan + artincontext Mimar Sinan）；「层层递落的穹顶体系」＝半穹顶链，**仅 wp 单源**（wp `cascade of domes`/semi-domes；artincontext 无 cascade/semi）。
  - **原理**「以中央大穹顶统摄、四周半穹顶与拱券传递推力，形成开阔而集中的礼拜空间」——中央穹顶/半穹顶/推力/集中空间均主要出 wp（半穹顶单源）；`ratio(原理, 定义+概述)=0.3009`（低，机制独立，非逐字拼接）。
  - 实例「古典奥斯曼集中式清真寺（类型性描述）；地点与设计者不适用」——**具体实例（Şehzade/Süleymaniye/Selimiye，锡南，伊斯坦布尔/埃迪尔内，1543–1574）在两源中均可查**（wp 全有、artincontext Suleymaniye 1558）；**「地点与设计者不适用」与源直接相悖**（见 §八问题②）。
- **两源互证（任务专项）——部分成立**：**「中央大穹顶」「集中式」「锡南」双源互证成立**；**但 definition/overview 的「半穹顶」「层层递落穹顶体系」关键形制仅 wp 单源，`artincontext-islamic-architecture` 对「半穹顶」零覆盖/泛论**。按硬性规则——**“半穹顶”属关键标志性事实而实质单源**。
- **专项核验（任务点名）**：**`wp-ottoman-architecture` 确述中央穹顶+半穹顶**（central dome 13 处、semi-dome 13 处，逐字命中）；**`artincontext-islamic-architecture` 述中央穹顶/集中式/Sinan，但“不述半穹顶”**（semi-dome=0）——即任务点名项**部分不通过（第二源缺半穹顶）**。
- **内容判定：待核实**（definition 概念层“中央穹顶+集中式”双源、主源 wp 强支撑、无编造；**缺陷＝第二源 `artincontext` 对「半穹顶」及“层层递落穹顶体系”零覆盖，“半穹顶”关键标志形制实质单源**；另：实例“地点/设计者不适用”与源相悖、region 口径见 §六——均见 §八）。**⚠ 与第46轮 `early-islamic`（artincontext 对形制零覆盖→待核实）完全同类。**

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：4 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）；`link_ok`：wp-yaodong=true，其余三源=null（三态未标，非死链、非假源）。**4 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：`wp-yaodong`（owiki 200 / en.wikipedia 200）/`smx-shanzhou-dikengyuan`（200）/`wp-ottoman-architecture`（owiki 200 / en.wikipedia 200）/`artincontext-islamic-architecture`（200）——**4/4 全部 HTTP 200，无死链**（体检 F 之“死链”对本次 4 源为 0）。
- **相关性 / 点名核验结论**：
  - **`wp-yaodong` 确述 sunken yaodong/地坑**（`sunken courtyard`、`square pit…four walls…underground courtyard`、`"pit yard"` 豫西）——**正面通过**，且与 definition 逐字对应。
  - **`smx` 政府页确述地坑院**（`陕州地坑院`、`地下古民居建筑`、`地平线下古村落`、`地坑院营造技艺`、地点）——**域内命中**，但**对营造方法零覆盖**（约 1600 字简介，无方形/下沉/窑洞/保温/排水/通道）——属**“直接但极薄”**。
  - **`wp-ottoman-architecture` 确述中央穹顶+半穹顶**——**正面通过**（central dome 13 / semi-dome 13）。
  - **`artincontext-islamic-architecture` 述中央穹顶/集中式/Sinan，但不述半穹顶**（semi-dome=0）——**点名项部分不通过**；属**“直接但极薄/对核心形制零覆盖”**（第42/46轮同类缺陷）。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | 含「示意图，非施工图」 | viewBox / 元素出界 | 风险/规范句 | 原理=def+概述拼接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dikengyuan | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400；x∈[0,680]、y∈[40,380]，**不出界** | ✓ | 否（ratio 0.2752） |
| ottoman-architecture | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400；x∈[0,580]、y∈[40,380]，**不出界** | ✓ | 否（ratio 0.3009） |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含「示意图，非施工图」、无 `on*` 事件属性（程序断言 `onattr=False`）；「常见错误与限制」段均以规范提示收尾（`实际工程须按当地规范和专业设计人员的要求`）；`check.py` 含 SVG 出界检查，本轮 PASS（两图元素坐标全部在 760×400 内）。**机械项两条全部通过。**

### SVG 质量观察（形态贴合主题，但缺「设计意图/尺寸关系」显式标注——次要、系统性）
- **dikengyuan**：`<line y1=180 …>`（地平线）+ `<rect x=240 y=180 w=280 h=140>`（下沉坑院外框）+ 两个内嵌 `<rect>`（270/430,210，＝四壁窑洞）+ 基线，**贴合「下沉坑院 + 四壁窑洞剖面」主题、非随机占位**；但**图中仅标题 + 「示意图，非施工图」，缺 TASK_design 第6条要求的「设计意图或尺寸关系」文字标注**（次要缺陷）。
- **ottoman-architecture**：四条 `Q` 曲线（顶点 380,120 向两侧 300/460 与 220/540 展开＝中央穹顶 + 左右半穹顶）+ 基线，**贴合「中央穹顶 + 半穹顶体系」主题、非随机占位**；同样**未标注「中央穹顶/半穹顶」等设计意图或尺寸关系**（次要缺陷）。
- **唯一性核验（防模板复刻）**：两条 SVG 字符串（518B/589B）在**全库 258 条中各自唯一**（`dup in others=[]`，无整串重复）；与 batch-47 另 1 条（sasanian）互为不同字符串。
- **判定**：两条「一图」**机械项（1 张 + viewBox + 「示意图，非施工图」 + 不出界 + 无事件属性 + 唯一性）全过**，图形与主题相关；**唯一不足为「缺图中设计意图/尺寸关系标注」**——`check.py` 只查出界与注记，查不出该语义项，属**次要/可提升**，不构成本轮「不合格」。建议全站做一次 SVG 标注补强（与第44/45/46 轮方向一致）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实（含 period/region 分类口径）

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatches=NONE）：dikengyuan（地坑院（下沉式窑院）/下沉空间/补充/古代/中国/L2）、ottoman-architecture（奥斯曼建筑/风格/重要/文艺复兴至19世纪/伊斯兰/南亚/L2）；`source_count` 与来源数组长度一致（2=2、2=2）；`needs_verification_count`：各 1；`related`：两条均 `[]`（无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| dikengyuan | true | 「地坑院（下沉式窑院）」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（**但未披露“核心营造方法仅 wp 单源、smx 对方法零覆盖”的真实缺口；且 smx 已给地点，措辞偏保守**，见 §八问题②④） |
| ottoman-architecture | true | 「奥斯曼建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（**但未披露“半穹顶单源、artincontext 零覆盖”的真实缺口；且两源已给具名实例及地点/设计者**，见 §八问题②④） |

> 结构化标志与两处文本：两条 `pending_notes` 与「待核实」节**逐字一致**（结构联动通过）。**注意（D14 精神）**：两条的「待核实」均仅声明“具体实例待补充”，**对真实存在的来源支撑缺口（dikengyuan：核心营造方法单源；ottoman：半穹顶单源）未写入**——属“联动一致但内容不完整/失真”。

### period/region 与分类口径（项目时期桶：古代 / 中世纪 / 文艺复兴至19世纪 / 20世纪 / 当代 / 跨时期）
- **dikengyuan：period=古代、region=中国** ——地坑院为黄土塬传统住居，wp 述其起源可溯至公元前 2000 年青铜时代；作为**传统住居类型**归“古代”可接受（**Minor**：其为仍在使用/2011 年列入非遗的“活态”遗产，严格亦可论“跨时期”，但作传统营造类型用“古代”无误）；`region=中国` ✓（豫西/黄土塬/三门峡）。
- **ottoman-architecture：period=文艺复兴至19世纪、region=伊斯兰/南亚** ——`period` ✓（16–17 世纪古典期落在“文艺复兴至19世纪”桶）；**`region=伊斯兰/南亚` 存在口径瑕疵（Minor）**：奥斯曼核心区在安纳托利亚/巴尔干/黎凡特（伊斯坦布尔、埃迪尔内），“伊斯兰”部分成立，但**“南亚”不适用于本条**（此为伊斯兰建筑群合桶标签，同 `islamic-architecture` 亦用之）——建议在口径说明/`DECISIONS.md` 记录合桶惯例，或细化 region。
- **sasanian-architecture（未抽内容，专项评估 period/region）：period=古代、region=伊斯兰/南亚** ——
  1. `period=古代` ✓：萨珊 224–651 CE 属古典上古晚期，归“古代”合理。
  2. **`region=伊斯兰/南亚` 是否合理（任务点名）**：萨珊为**前伊斯兰的波斯（伊朗）王朝**，既非“伊斯兰”（宗教/文化上属前身），亦非“南亚”（地理上属西亚/伊朗）。其 `time_or_place` 已**明示**“古代、伊斯兰/南亚（**前伊斯兰波斯，iwan 源头**；参见来源）”，即**以“伊斯兰建筑前身/源头”身份并入该合桶**——**作为内容定位（iwan/穹顶被伊斯兰建筑吸收的源头）是合理且有明文注明的**；但**作为 `region` 标签本身不精确**（既非伊斯兰亦非南亚）。→ 结论：**“归伊斯兰前身”合理（前提是该合桶惯例在 `DECISIONS.md`/口径说明中明文记录）；若不记录则 `region` 标签应视为不精确的 Minor 瑕疵**。建议将“伊斯兰建筑及其前身（含前伊斯兰波斯）”合桶惯例写入 `DECISIONS.md`。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| dikengyuan | **0.3077** vs yaodong | <0.54 ✓ | **0.4468** vs yaodong | <0.54 ✓ |
| ottoman-architecture | **0.3469** vs mughal-architecture | <0.54 ✓ | **0.4385** vs islamic-architecture | <0.54 ✓ |

> 对**既有 257 条**（排除自身）逐条扫描，两条两档均 **<0.54**（短文本最大 0.3469、全字段最大 0.4468）——**各自与既有库文本区分在阈值内**。
> - dikengyuan 最近邻：短文本 `yaodong`(0.3077)/`eaves-space`(0.2993)/`side-scenery`(0.2692)；全字段 `yaodong`(0.4468)/`hakka-style`(0.4138)/`eaves-space`(0.4081)（dikengyuan 本为 yaodong 的下沉类型，父概念近邻正常；仍 <0.54）。
> - ottoman 最近邻：短文本 `mughal-architecture`(0.3469)/`islamic-architecture`(0.3392)/`sasanian-architecture`(0.3383)；全字段 `islamic-architecture`(0.4385)/`sasanian-architecture`(0.4359)（同域，正常；仍 <0.54）。
> **均未越线。**

### 7.2 batch-47 批内去模板化核验（3 条两两）
| 对 | ①短文本 | ②全字段 |
| --- | --- | --- |
| dikengyuan vs sasanian-architecture | 0.1579 | 0.3657 |
| dikengyuan vs ottoman-architecture | 0.1393 | 0.3627 |
| sasanian-architecture vs ottoman-architecture | 0.3383 | **0.4286** |

> batch-47 三条**两两均远低于 0.54**（批内全字段最大 **0.4286**，sasanian↔ottoman）——**无第43轮 batch-42 式双条互为模板姊妹、无套话风险**。

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–46轮报告**逐位一致**，口径正确。

> **文本相似度判定：两条对既有库与批内均 PASS（均 <0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 文本相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **dikengyuan（地坑院）** | 概念层（地下/下沉民居）**双源互证**（wp sunken courtyard/pit yard + smx 地下古民居/地平线下古村落）；**但核心营造方法「方形坑+四壁横挖窑」仅 wp-yaodong 单源，smx 零覆盖**；验证点 **wp 确述 sunken yaodong/地坑、smx 确述地坑院**（smx 薄）；实例名称有源（陕州地坑院）但“地点/设计者不适用”与 smx 地点相悖；原理独立（0.2752）；**Minor：“进村不见房”引语无源、“排水”无源、period 古代可接受** | 2/2 true；wp 直接强源、smx 直接但极薄；**2 源 200 可达** | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、形态贴合（地平线+坑院框+两侧窑），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 逐字一致（**未披露方法单源缺口**） | 既有库 ✓（0.3077/0.4468）；批内 ✓ | **待核实**（核心营造方法实质单源）；须修：补第二营造源或据实降级表述★、实例补地点、修“进村不见房”引语；次要：pending/SVG 标注 |
| **ottoman-architecture（奥斯曼建筑）** | definition 概念层双源（中央穹顶 ✓✓、集中式/center-plan ✓✓、锡南 ✓✓），**但「半穹顶」「层层递落穹顶体系」仅 wp 单源（artincontext semi-dome=0）**；overview 同（半穹顶链单源）；验证点 **wp 确述中央穹顶+半穹顶、artincontext 述中央穹顶/集中式/Sinan 但不述半穹顶**；实例具名例（Şehzade/Süleymaniye/Selimiye·锡南·伊斯坦布尔/埃迪尔内·1543–1574）两源可查，“地点/设计者不适用”相悖；原理独立（0.3009）；**Major：「半穹顶」关键标志形制实质单源** | 2/2 true；wp 直接强源；**artincontext 直接但极薄、对半穹顶零覆盖**；**2 源 200 可达** | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、形态贴合（中央穹顶+半穹顶曲线），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 逐字一致（**未披露半穹顶单源缺口**） | 既有库 ✓（0.3469/0.4385）；批内 ✓（max 0.4286） | **待核实**（“半穹顶”实质单源）；须修：补述半穹顶的第二源或据实降级表述★、实例补地点/设计者/年代；次要：region 南亚、pending/SVG 标注 |

### 问题清单（逐条）
- **★① ottoman-architecture「半穹顶」关键标志形制实质单源（本轮判定核心，任务点名）**：definition 将“中央大穹顶**加半穹顶**”并列为标志，overview 亦称“层层递落的穹顶体系”；但 **semi-dome 仅 `wp-ottoman` 单源（13 处），`artincontext-islamic-architecture` 半穹顶零覆盖（0）**，仅述 central dome/center-plan/Sinan。→ 按硬性规则「关键事实至少两源互证」，本条目**判“待核实”**；建议**补一份述及奥斯曼半穹顶体系（semi-dome/cascade of domes）的第二来源**，或将“半穹顶/层层递落”降为“据 wp 单源”并在 pending 披露。
- **★② dikengyuan 核心营造方法实质单源（判定核心）**：definition/原理的核心方法「向下挖方形坑、再沿四壁横向挖窑」逐字见 `wp-yaodong`，但 `smx` 政府页（约 1600 字景区简介）**对方形/下沉/窑洞/营造方法零覆盖**，仅述“地下古民居/地平线下/非遗营造技艺/地点”。→ 按硬性规则本条目**判“待核实”**；建议**补一份述及地坑院营造法（方形天井+四壁窑洞）的第二来源**或在正文/pending 明确“营造方法据 wp 单源”。
- **③ dikengyuan 实例与引语问题**：`实例` 写“陕州地坑院（类型性描述）；**地点与设计者不适用**”，但 ① 陕州地坑院为**具名 AAAA 景区**非“类型性”；② `smx` 明载地点“**河南省三门峡市陕州区张汴乡北营村**”——“地点不适用”与源相悖。另 `overview` 引语“**进村不见房**”在两源正文**均查无**（属无源引文），`典型手法/常见错误` 的“**排水**”两源亦无。→ 据源补地点、将“进村不见房”改为源内实词或删除、“排水”改为一般性说明。（Minor）
- **④ ottoman-architecture 实例要素不全/表述失准**：`实例` 写“古典奥斯曼集中式清真寺（类型性描述）；**地点与设计者不适用**”，但两源明载具名实例——`wp`：Şehzade（1543）/Süleymaniye（1550, İstanbul）/Selimiye（Edirne,1568–74），设计者 **Mimar Sinan（锡南）**；`artincontext`：Suleymaniye Mosque（Istanbul）、Mimar Sinan、1558。→ 据源补“地点（伊斯坦布尔/埃迪尔内）、设计者（锡南）、年代”，并调 pending。（Minor，同 round46 问题③）
- **⑤ 两条 pending 未披露真实缺口（D14 精神）**：两 `pending_notes`/`待核实` 仅称“具体实例待补充”，**均未写入真实来源缺口（dikengyuan 营造方法单源；ottoman 半穹顶单源）**。→ 据实补充。（Minor）
- **⑥ period/region 口径**：`ottoman` region=伊斯兰/**南亚**（南亚不适用于安纳托利亚/巴尔干）；`sasanian` region=伊斯兰/**南亚**（前伊斯兰波斯，既非伊斯兰亦非南亚，仅作“iwan 源头/前身”合桶，`time_or_place` 已注明）；`dikengyuan` period=古代（传统住居类型可接受，活态遗产亦可论跨时期）。→ 建议将“伊斯兰建筑及其前身/南亚”**合桶惯例写入 `DECISIONS.md`**，或按实细化 region；`sasanian 归伊斯兰前身`本身合理（有明文注明），但需口径记录。（Minor）
- **⑦ SVG“设计意图/尺寸关系”标注缺失（两条例、系统性）**：两图机械项与主题贴合均过，但仅标题 + 「示意图，非施工图」，缺 TASK_design 第6条「图中标注设计意图或尺寸关系」。→ 建议全站统一补强（延续第44/45/46 轮）。（Minor、系统性）
- **⑧ 来源元数据瑕疵（轻微）**：`artincontext-islamic-architecture` 记录 `title="Islamic Architecture — Art in Context"`，实际 `<title>`=`Islamic Architecture - Building Styles Across the Muslim World`（机构名相符，副标题未录入）→ 建议存全名或备注站点。（Minor）

## 九、总体结论与建议

- **抽样结果**：本轮抽 `batch-47` 新增 3 条中的 **2 条**——`dikengyuan`、`ottoman-architecture`（2/3≈67%）。**内容维度：0 合格 ＋ 2 待核实 ＋ 0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：4 个引用来源 id **全部存在、verified=true、实抓 4/4 HTTP 200 可达**。**两项任务点名核验**：`wp-yaodong` **确述 sunken yaodong/地坑**（正面）、`smx` **确述地坑院**（域内命中但极薄、未涉营造方法）；`wp-ottoman` **确述中央穹顶+半穹顶**（正面）、`artincontext` **述中央穹顶/集中式/Sinan 但不述半穹顶**（semi-dome=0，点名项部分不通过）。唯 1 处 `title` 元数据瑕疵（artincontext 副标题未录入，Minor）。
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 唯一性与形态贴合通过、元数据逐项一致、`needs_verification↔pending↔待核实` **逐字一致**、`check.py` PASS 0 errors、原理均非拼接（0.2752/0.3009）。
- **相似度层面**：两条对既有库与批内均 <0.54（PASS）；批内最大 0.4286，无套话；方法自校 0.5157 与第39–46 轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——无“不合格”内容条目（0 合格 + 2 待核实），无编造/假 id/死链（待核实属来源深度缺陷，非不合格）。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——两条对既有库与批内均 <0.54。
  3. **结论：本轮 2 条不触发整批返工/降级**；但**两条均判“待核实”（关键形制/营造方法实质单源）**，须**定向修复**。两处“半穹顶/营造方法单源”与“实例地点/设计者不适用却与源相悖”是**同一类系统性来源深度/实例要素缺陷**，建议按下列优先级处理。
- **返工/修复建议（按优先级）**：
  1. **（应做，问题①★）**：为 `ottoman-architecture` 补一份**真正述及奥斯曼半穹顶/层层递落穹顶体系（semi-dome / cascade of domes）的第二来源**以实现“半穹顶”双源互证；否则在正文/pending 明确“半穹顶据 wp 单源，待第二源核”。
  2. **（应做，问题②★）**：为 `dikengyuan` 补一份**真正述及地坑院营造法（方形天井+四壁窑洞）的第二来源**；否则将营造方法表述降为“据 wp-yaodong 单源”并在 pending 披露。
  3. **（应做，问题③④）**：`dikengyuan` 实例据源补地点（河南省三门峡市陕州区张汴乡北营村）、将“进村不见房”改为源内实词/删除、“排水”改一般性说明；`ottoman` 实例据源补地点（伊斯坦布尔/埃迪尔内）、设计者（锡南）、年代（Şehzade 1543/Süleymaniye 1550/Selimiye 1568–74）。
  4. **（应做，问题⑤）**：两条 `pending_notes`/`待核实` 据实补充“核心形制/营造方法单源”的真实缺口（D14 精神）。
  5. **（宜做，问题⑥）**：将“伊斯兰建筑及其前身（含前伊斯兰波斯）/南亚”**合桶惯例写入 `DECISIONS.md`**，或按实细化 `ottoman`/`sasanian` 的 region（南亚不适用）；`sasanian 归伊斯兰前身`合理但需口径记录。
  6. **（宜做，问题⑦，系统性）**：为两图补「设计意图或尺寸关系」文字标注，并全站统一补强（延续第44/45/46 轮）。
  7. **（宜做，问题⑧）**：`artincontext-islamic-architecture` 的 `title` 存全名或备注站点。
- **流程记录**：本轮抽检 2 条＝**内容 0 合格、2 待核实（均为关键形制/营造方法实质单源）、0 不合格、0 编造、0 假 id、0 死链、七节/规范/元数据/pending 结构联动一致、check.py PASS、相似度全 <0.54**；**主要遗留：ottoman「半穹顶」单源、dikengyuan「营造方法」单源（须补第二源或据实降级披露）＋两条实例“地点/设计者不适用”与源相悖（须补）＋period/region 合桶口径（sasanian/ottoman 南亚须记录）＋「一图」缺设计意图/尺寸标注（系统性，宜修）**；**不触发 §E 整批返工/降级**。

---

### 机器可读汇总

```
ROUND=47
SAMPLER=spotcheck-r47
MODE=针对性补抽（batch-47 新增3条中抽2条：dikengyuan / ottoman-architecture；另 sasanian 仅作 period/region 专项评估）
SCOPE=["dikengyuan","ottoman-architecture"]
FILES={"dikengyuan":"entries/batch-47.json","ottoman-architecture":"entries/batch-47.json"}
STATE={"sources.json":"153010B@2026-11-23 11:01","batch-47.json":"6657B@2026-11-23 11:01","coverage.json":"87346B@2026-11-23 11:01","check.py":"15908B@2026-11-22 15:11","total":258,"all_level":"L2","pending_sum":220,"sources_total":325,"sources_verified_true":322,"sources_verified_false":3,"link_ok_true":145,"link_ok_false":6,"link_ok_null":174}
GIT_HEAD="93487c6 feat: round46 resume expansion, 4 sparse-cell entries, 6 named instances"; GIT_STATUS="round47 WIP in worktree; targets stable; only file this spotcheck wrote = research/spotcheck-round47.md"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2/3 (batch-47 新增3条抽2条, 67%)"
FETCH_METHOD="urllib+ChromeUA(retry6); en.wikipedia -> owiki mirror + direct recheck; smx GB18030; artincontext direct; 4/4 HTTP200; analysis in-memory (stdin script, no temp file)"
SOURCES={"count_distinct":4,"count_refs":4,"all_exist":true,"all_verified_true":true,"all_reachable_200":"4/4","link_ok":{"wp-yaodong":true,"smx-shanzhou-dikengyuan":null,"wp-ottoman-architecture":null,"artincontext-islamic-architecture":null},
 "title_note":"artincontext-islamic-architecture record title='Islamic Architecture — Art in Context' vs actual <title>='Islamic Architecture - Building Styles Across the Muslim World' (org matches; subtitle missing) -> minor",
 "point_checks":{"wp-yaodong":"CONFIRMED sunken yaodong/地坑: 'dig a square pit on the spot, and then dig the cave horizontally on the four walls to form the underground courtyard' + 'sunken courtyard' + '\"pit yard\"' western Henan","smx-shanzhou-dikengyuan":"CONFIRMED 地坑院: '陕州地坑院'/'地下古民居建筑'/'地平线下古村落'/'地坑院营造技艺'非遗 + location 河南省三门峡市陕州区张汴乡北营村; BUT 方形/下沉/窑洞/保温/排水/通道=0 -> thin, no construction method","wp-ottoman-architecture":"CONFIRMED central dome AND semi-domes (central dome=13, semi-dome=13); Sinan; classical 16-17c","artincontext-islamic-architecture":"CONFIRMED central dome('broad central domes...center-plan building')+Sinan+Suleymaniye; BUT semi-dome=0/semidome=0/half dome=0 -> ZERO coverage of 半穹顶"}}
BODY_SUPPORT={
 "dikengyuan":"definition core-nature dual-source (wp sunken courtyard/pit yard + smx 地下古民居/地平线下古村落); BUT core construction method '方形坑+四壁横挖窑' single-source(wp only; smx 0); overview '进村不见房' quote NOT in either source; 原理 ratio=0.2752 independent; instance name 陕州地坑院 sourced but '地点/设计者不适用' contradicts smx location; VERDICT=待核实 (core construction method de-facto single-source, non-fabrication)",
 "ottoman-architecture":"definition concept-level dual-source (central dome ✓✓; centralized/center-plan ✓✓; Sinan ✓✓) BUT '半穹顶'+'层层递落穹顶体系' single-source(wp only; artincontext semi-dome=0); 原理 ratio=0.3009 independent; instance named Şehzade/Süleymaniye/Selimiye·Sinan·Istanbul/Edirne·1543-1574 but '地点/设计者不适用' contradicts sources; VERDICT=待核实 (半穹顶 headline form de-facto single-source, non-fabrication)"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2, x<=680/580 y<=380 no overflow, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","原理_concat":{"dikengyuan":0.2752,"ottoman-architecture":0.3009}}
SVG_NOTE={"uniqueness":"both SVG strings (518B/589B) unique across 258 library; distinct from sasanian","dikengyuan":"line(horizon)+rect(pit courtyard)+2 rect(caves on walls) topical; no intent/dimension annotation","ottoman-architecture":"4 Q-curves(central dome + 4 semi-domes)+baseline topical; no intent/dimension annotation","verdict":"机械项+唯一性全过; 缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x2","source_count":"2=2 / 2=2","nvc":"1 x2","needs_verification":"true x2","related":"[] x2 (no dangling)","pending_consistency":"逐字一致 x2","period_region_note":"dikengyuan 古代/中国 OK(traditional type; live heritage could argue 跨时期); ottoman 文艺复兴至19世纪/伊斯兰·南亚 = region '南亚' 不适用(Minor); sasanian 古代/伊斯兰·南亚 = 前伊斯兰波斯归'伊斯兰前身'合理(有明文注明)但 region 标签不精确, 须在 DECISIONS 记录合桶惯例"}
SIMILARITY={
 "dikengyuan":{"vs_existing_short":0.3077,"vs_existing_short_entry":"yaodong","vs_existing_full":0.4468,"vs_existing_full_entry":"yaodong","verdict":"PASS<0.54"},
 "ottoman-architecture":{"vs_existing_short":0.3469,"vs_existing_short_entry":"mughal-architecture","vs_existing_full":0.4385,"vs_existing_full_entry":"islamic-architecture","verdict":"PASS<0.54"},
 "batch47_pairwise_full_max":0.4286,"batch47_pairwise_full_max_pair":"sasanian-architecture vs ottoman-architecture",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-46 exactly -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"dikengyuan":"待核实(核心营造方法实质单源; 须补第二营造源或据实降级 + 实例补地点 + 修'进村不见房'引语)","ottoman-architecture":"待核实(半穹顶实质单源; 须补述半穹顶第二源或据实降级 + 实例补地点/设计者/年代)"}
VERDICT_SVG={"dikengyuan":"机械项+唯一性通过/形态贴合, 缺意图·尺寸标注(次要)","ottoman-architecture":"机械项+唯一性通过/形态贴合, 缺意图·尺寸标注(次要)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
BATCH_ACTION="No rollback/downgrade: no 不合格 (0 合格 + 2 待核实), 0 fabrication/0 fake id/0 dead link; similarity all <0.54. Required fixes: (1) ottoman add true 2nd source for semi-dome/cascade of domes or mark single-source in pending; (2) dikengyuan add true 2nd source for construction method(方形坑+四壁) or mark single-source; (3) both instances fill location/designer/year (陕州·三门峡张汴乡北营村; Suleymaniye/Selimiye·Sinan·Istanbul/Edirne); (4) dikengyuan remove/fix unsourced quote '进村不见房' + '排水'; (5) pending disclose real gaps; (6) document 伊斯兰/南亚 + 前伊斯兰波斯 合桶惯例 in DECISIONS; (7) site-wide SVG 设计意图/尺寸关系 annotation; (8) artincontext title full name."
READONLY="only wrote research/spotcheck-round47.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (stdin script, no persistent temp file)"
```

*（报告完）*
