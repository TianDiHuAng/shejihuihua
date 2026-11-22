# 第39轮质量闸抽检报告（spotcheck-round39）——非洲建筑 / 拉美殖民建筑 / 架空层（batch-38 中抽 3 条）

- 抽检人：spotcheck-r39（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 00:57 起，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；新增/改动条目随机抽 10%、**至少 3 条**逐条核对来源；**不合格则整批返工**，下一轮抽检比例提高到 25%；异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 `verified=true` 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根**无同名文件**（与第 12–38 轮一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md` 在仓库根（21 行，已读）。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 00:59）**：`data/sources.json`=126910B@00:56:46、`entries/batch-38.json`=47258B@00:56:46、`coverage.json`=83078B@00:56:46、`tools/check.py`=15908B@2026-11-22 15:11:54。`git log -1` = `633bd70 feat: round38 all 246 scope entries written and L2 (unwritten=0)`（batch-38 已提交）。
- **工作树状态**：`git status --porcelain` 仅 3 项——`?? research/gaps-round39.md`、`?? research/healthcheck-round39.md`、`?? research/reader_questions-round39.md`（第39轮其它子任务产出，**非本次抽检所改**）；`entries/`、`data/`、`coverage.json` 无改动（已入库）。
- **条目规模（`coverage.json` 实读）**：`total=246`、全部 `level=L2`、全部 `status=已写`；`pending_total`（`needs_verification_count` 求和）＝**220**（与第38轮末一致，说明本轮抽检未改动任何条目数据）。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round39.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python urllib 读取→内存计数），未在项目内外落盘任何临时文件。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。
- **抽检口径与样本**：任务指定从 `entries/batch-38.json` 抽 **3 条**：`african-architecture`（非洲建筑）、`latin-american-colonial`（拉美殖民建筑）、`raised-floor`（架空层）；均为 L2。抽检比例 3/25＝**12%**（≥10% 下限）。共引用 **4 个去重来源 id（3 条 6 处引用）**：`wp-architectural-style`、`wp-vernacular-architecture`、`wp-history-of-architecture`、`wp-architecture`（见 §二）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（本轮 3 条均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept`/`Accept-Language` 齐备，`ssl` 不校验证书）。先试 `en.wikipedia.org` canonical 历史上超时，改 **owiki 同源镜像** `https://owiki.org/wiki/<Title>` 核对标题与正文（DECISIONS D05 允许）。本轮 **4 个引用来源全部实抓 HTTP 200**，h1 与 `sources.json` 标题逐条核对一致（见 §二）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG 原始标记（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **246 条**去重已写条目逐条扫描，警戒线 **0.54**（与第27–38轮一致）。
- **“两源互证”判定口径**：`TASK_design.md` 硬性规则要求“关键事实至少两个独立来源互相印证，否则标待核实”。本轮按“两源并集须覆盖 definition/time/overview 全部要点，且定义主干/核心论断至少获两源之一直接支撑；若第二源为本条**泛论伞源、零覆盖不互证**（如 `wp-architectural-style` 对非洲 africa=0、对拉美 latin america=0；`wp-architecture` 对架空层 pilotis=0），则相关具体论断实为**单源**，据硬性规则影响判定”执行。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **4 个去重来源 id（6 处引用）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）、全部 link_ok=true、全部 owiki 实抓 HTTP 200**。

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| african-architecture | `wp-architectural-style` | ✅ / true | Architectural style / Wikipedia | 权威百科 | true | **泛论伞源、零覆盖不互证**（`africa=0、african=0、earth=0、thatch=0、rammed earth=0、vernacular=0、climate=0、ethnic=0`，全文不提非洲建筑） |
| african-architecture | `wp-vernacular-architecture` | ✅ / true | Vernacular architecture / Wikipedia | 权威百科 | true | **直接支撑主体**（`africa=2、african=2、rammed earth=1、thatch=4、earth=6、climate=10、ethnic=2、mud brick=3、adobe=2、indigenous=3、local material=1`；**但 `weav=0`（编织无源）**） |
| latin-american-colonial | `wp-architectural-style` | ✅ / true | Architectural style / Wikipedia | 权威百科 | true | **泛论伞源、仅概念层**（`baroque=1、colonial=2` 泛论“风格经殖民传播/文艺复兴转巴洛克”；**`latin america=0、ornament=0、facade=0、indigenous=0`** 不涉拉美具体） |
| latin-american-colonial | `wp-history-of-architecture` | ✅ / true | History of architecture / Wikipedia | 权威百科 | true | **直接主题源、强支撑**（`baroque=30、latin america=1`“Europe, **Latin America** and beyond 1580–1800”、`colonial=2`含“Lima(秘鲁)”、`ornament=17、facade=3、façade=6、indigenous=2`；**但 `heavy/massive` 命中均无关语境→“厚重”无直证**） |
| raised-floor | `wp-architecture`（**泛论唯一相关≈零覆盖**） | ✅ / true | Architecture / Wikipedia | 权威百科 | true | **主题零覆盖**（`pilotis=0、parking=0、stilt=0、ground floor=0`；`raised=1` 实为 Ruskin 引句“edifices raised by men”无关；`ventilation` 仅“heating, ventilation and cooling”环境泛列；`le corbusier=2` 仅名言，不含 pilotis/五点） |
| raised-floor | `wp-vernacular-architecture` | ✅ / true | Vernacular architecture / Wikipedia | 权威百科 | true | **异类邻近、非本概念**（`stilt=2`“Stilt house – a raised house found in monsoonal regions… prone to flooding”＝防洪整屋抬高民居；`parking=0、pilotis=0`、`ground floor=1` 指“Alpine barn 住于底层之上”，与“底层架空作公共/停车”不同；`ventilat=6` 泛指气候通风） |

> 关键事实：三条 `sources` 数组长度与 `coverage.source_count` 一致（各 2=2）。4 源均 `year=null`（在线百科，D06 允许）、`verified=true`、`link_ok=true`。**无死链、无假 id、无 verified=false 被引用。** 但 `wp-architectural-style`（对 african / latin）为**泛论伞源、对本条零/近零主题覆盖不互证**；`wp-architecture`（对 raised-floor）为**主题零覆盖的泛论来源**——详见 §三、§四。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 african-architecture（非洲建筑）——**待核实**
- **wp-vernacular-architecture**（owiki HTTP200 43083B，h1「Vernacular architecture」，textlen≈26773）：
  - 直证：`Rammed earth often used in foundations`（夯土）；`Thatch – dry vegetation used as roofing material`（茅草屋面）；`Climate One of the most significant influences on vernacular architecture is the macro climate of the area in which the building is constructed`（气候）；`Northern African vernacular often has very high thermal mass and small windows to keep the occupants cool`（非洲气候适应）；`the family units of several East African ethnic communities live in family compounds… separate single-roomed dwellings`（族群→形态多样）。
  - 关键词实计：`africa=2、african=2、rammed earth=1、thatch=4、earth=6、climate=10、ethnic=2、mud brick=3、adobe=2、indigenous=3、local material=1`；**`weav=0`（另 `woven=0、wattle=0、wicker=0、mat=0、basket=0、plait=0、braid=0`，仅 `reed=1`）——"编织"作为建材零直证**。
- **wp-architectural-style**（owiki HTTP200 21723B，h1「Architectural style」，textlen≈10185）：
  - 纯“建筑风格概念”泛论伞源，对本条关键词实计 **`africa=0、african=0、earth=0、thatch=0、rammed earth=0、vernacular=0、climate=0、ethnic=0`**——**全文不提非洲建筑，对本条零覆盖、零印证**。
- **逐项结论（对照所引来源）**：
  - definition“以**夯土、茅草、编织**等本地材料塑出多样形态”——夯土✓（rammed earth）、茅草✓（thatch）、本地材料✓（local material/vernacular）；**“编织”✗（weav=0 全套编织词皆 0，无源）**；“多样形态”有 vernacular=58 泛支撑 + 各区差异描述。
  - overview“形态随**气候、族群**与材料而千差万别”——气候✓（climate=10）、族群✓（ethnic=2）、材料✓；“千差万别”≥ 多区/多型描述，方向支撑成立。
  - 原理“就地取材，用土、草、木的构造回应当地气候与生活方式”——土/草/木✓、气候✓、“就地取材”契合 vernacular 概念；**非 definition+overview 逐字拼接**（本条原理为改写，较优）。
  - 典型手法“以夯土、茅草与**编织**等本地材料建造”——夯土✓、茅草✓；**“编织”✗（第二次出现仍无源）**。
  - 常见错误“直接移植会破坏地域性”——**通识补充**（源未逐字，方向不冲突，Minor）。
- **两源互证**：核心（夯土/茅草/本地材料/气候/族群/多样）由 `wp-vernacular-architecture` **强直证**；但第二源 `wp-architectural-style` 为**泛论伞源、africa=0 零覆盖、不互证**——核心实质为**单源**；且“编织”多出无源。
- **实例核对**：`实例`＝“名称：夯土与茅草的聚落屋（**类型性描述**）；地点与设计者不适用。看土墙与草顶。”**类型性、无具名/年份 → 不编造** ✓。
- **判定：待核实**。核心问题：**第二源 `wp-architectural-style` 泛论伞源、零覆盖不互证（africa=0）；主源 `wp-vernacular` 对夯土/茅草/气候/族群有实质支撑，但“编织”反复出现而全无直证（weav/wattle/wicker/woven 全=0）**。属来源支撑缺陷（单源实质 + 一处无源 facet），**非编造人名/年份/引文**，故判**待核实**。

### 3.2 latin-american-colonial（拉美殖民建筑）——**待核实**
- **wp-history-of-architecture**（owiki HTTP200 128112B，h1「History of architecture」，textlen≈86543）：
  - 直证：`Dominating more than two centuries of art and architecture in Europe, **Latin America** and beyond from circa 1580 to circa 1800`（拉美＋巴洛克年代跨度）；`…spreading the two styles into the Americas and **colonial** Africa and Asia, to places such as **Lima**, Mozambique, Goa…`（殖民传播、利马＝秘鲁拉美）；`ornament=17、facade=3、façade=6`（繁复装饰、立面）；`indigenous=2`（本土）；`baroque=30、rococo=16`。
  - 但：`heavy=1`（指 Romanesque“heavy barrel vaults”）、`massive=5`（史前/亚述等）**均无关语境——“厚重”无直证**。
- **wp-architectural-style**（owiki HTTP200 21723B，h1「Architectural style」）：
  - 泛论伞源，仅概念层：`baroque=1`“transitioned from Renaissance to Baroque”、`colonial=2`“An architectural style may also spread through colonialism… Spanish missions in California… Spanish Colonial Revival”；**`latin america=0、ornament=0、facade=0、indigenous=0`——不涉拉美具体，不互证本条具体论断**。
- **逐项结论（对照所引来源）**：
  - definition“混合欧洲**巴洛克**与**本地工艺**”——巴洛克✓（history baroque=30；style baroque=1 概念印证）；本地工艺/本土✓（history indigenous=2）；拉美/殖民语境✓（history Latin America=1 + colonial/Lima）。**主干由 `wp-history` 单源较强支撑**。
  - overview“以**厚重立面**与**繁复装饰**体现殖民与本土交融”——繁复装饰✓（ornament=17）、立面✓（facade/façade=3/6）、殖民＋本土✓；**“厚重”✗（heavy/massive 命中皆无关，无直证）**。
  - 原理（＝definition+overview **逐字拼接**，程序判定 `原理==definition+overview==True`）——同缺口，**未提供独立机制/感受解释**（L2「原理」深度不达标）。
  - 典型手法“以**巴洛克立面**结合本地材料与装饰工艺”——巴洛克✓、立面✓、装饰✓、本地✓；方向可支撑。
  - 常见错误“装饰堆砌会失整体”——**通识补充**（源未逐字，方向不冲突，Minor）。
- **两源互证**：核心“巴洛克＋拉美＋殖民＋装饰/立面/本土”由 `wp-history-of-architecture` **单源较强支撑**；第二源 `wp-architectural-style` 仅概念层泛论、**`latin america=0` 不涉拉美具体、不互证**；且“厚重”无直证。
- **实例核对**：`实例`＝“名称：拉美殖民建筑的典型场景（**类型性描述**）；地点与设计者不适用。”**类型性、无具名/年份 → 不编造** ✓。
- **时期核对**：`time_or_place`“文艺复兴至19世纪、美洲”——拉美（西/葡）殖民建筑约 16—19 世纪，**与史实大致相合**（Minor：起点“文艺复兴”略笼统但非硬性矛盾）。
- **判定：待核实**。核心问题：**主源 `wp-history` 对巴洛克/拉美/殖民/装饰/本土有实质支撑，但第二源 `wp-architectural-style` 为泛论伞源（latin america=0）不互证具体；“厚重”无直证；原理＝定义+概述逐字拼接**。属来源支撑缺陷（具体论断实质单源 + 一处无源 + 结构拼接），**非编造人名/年份/引文**，故判**待核实**。

### 3.3 raised-floor（架空层）——**不合格**
- **wp-architecture（泛论来源）**（owiki HTTP200 52067B，h1「Architecture」，textlen≈31377）：
  - 关键词实计：**`pilotis=0、parking=0、stilt=0、ground floor=0`**；`raised=1` 实为 Ruskin 引句“the edifices **raised** by men… that the sight of them”**与“底层架空”无关**；`ventilation` 仅“heating, **ventilation** and cooling, water use…”的**环境清单泛列**；`le corbusier=2` 仅为“stone, wood, concrete…that is Architecture”名言，**不含 pilotis/新建筑五点**。→ **对本条零覆盖**。
- **wp-vernacular-architecture**（owiki HTTP200 43083B，h1「Vernacular architecture」）：
  - `stilt=2`：“dwellings on **stilts**… frequent flooding or rainy monsoon seasons”、“**Stilt house** – a **raised house** found in monsoonal regions… prone to flooding”——**防洪/防潮的整屋抬高民居**（房屋整体架空于地面/水面之上），与“建筑**底层**架空、**留作公共或停车**等用途的楼层”（现代城市架空层/pilotis 开放底层）**属不同 typology**。
  - `ground floor=1`：“Alpine 'barn' houses – dwellings built on the storey **above the ground floor**, which housed cattle”——指“居室置于底层之上”，亦非“开放底层”。
  - `parking=0、pilotis=0`；`ventilat=6` 泛指气候通风；`public` 命中为 Rudofsky/主流语境，非“开放公共底层”。
- **逐项结论（对照所引来源）**：
  - definition“**建筑底层架空、留作公共或停车等用途**的楼层”——“底层架空（pilotis/open ground floor）”**无源**（pilotis=0、ground floor=0）；“**公共**用途”**无源**；“**停车**”**无源**（parking=0）。两源均不支撑本条定义主干。
  - overview“**释放地面、改善通风**并**容纳公共活动**”——“改善通风”仅 `ventilat` 泛支撑（非架空层专属）；“释放地面/容纳公共活动/停车”**无源**。
  - 原理（＝definition+overview **逐字拼接**，程序判定 `True`）——同缺口，且为拼接。
  - 典型手法“底层以**柱架空**，留出**通道、绿化或停车**”——“柱架空（pilotis）”**无源**（pilotis=0）；通道/绿化/停车**无源**。
  - 常见错误“私密与安全需管理”——**通识补充**（源未逐字，Minor）。
- **两源互证**：**两源均不支撑“底层架空作公共/停车”这一本条定义主干**——`wp-architecture` 主题零覆盖（pilotis/parking/ground floor 全=0，唯一 raised 命中无关）；`wp-vernacular` 仅“防洪抬高整屋（stilt house）”这一**异类邻近概念**，且 parking=0。**核心概念实质无源、且非“两源互证”**。
- **实例核对**：`实例`＝“名称：架空层的典型场景（**类型性描述**）；地点与设计者不适用。”**类型性、无具名/年份 → 不编造** ✓（但整条内容无来源支撑）。
- **判定：不合格**。核心问题：**两个引用来源均不支撑“建筑底层架空、留作公共或停车等用途”的定义主干与“释放地面、容纳公共活动”的机理**（`wp-architecture` pilotis/parking/ground floor 全=0、raised 命中为 Ruskin 无关句；`wp-vernacular` 仅防洪 stilt house、parking=0），**实质无源**，并**违反“关键事实至少两源互证”**；原理＝定义+概述拼接。**非编造具体人名/年份/引文**，但按诚实性与两源硬规则，本条属“核心概念无源”，判**不合格**（与第38轮 `acoustic-environment` 同类：唯一相关来源对本主题零覆盖）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：4 个去重来源 id **全部存在、全部 verified=true、全部 link_ok=true**（见 §二表），`year=null`（D06 允许）。
- **可达性（本轮实抓，owiki 镜像）**：`wp-architectural-style`（200 21723B h1=Architectural style）/ `wp-vernacular-architecture`（200 43083B h1=Vernacular architecture）/ `wp-history-of-architecture`（200 128112B h1=History of architecture）/ `wp-architecture`（200 52067B h1=Architecture）。**4 个来源 id 全部可达，无死链。**（`en.wikipedia.org` 直连按 D05 改走 owiki 镜像。）
- **相关性缺陷**：
  - `wp-architectural-style`（对 **african-architecture**）——**泛论伞源、零覆盖不互证**：`africa=0、african=0、earth=0、thatch=0、rammed earth=0、vernacular=0、climate=0、ethnic=0`。
  - `wp-architectural-style`（对 **latin-american-colonial**）——**泛论伞源、仅概念层**：`baroque=1、colonial=2`，但 `latin america=0、ornament=0、facade=0、indigenous=0`（不涉拉美具体，不互证）。
  - `wp-vernacular-architecture`（对 **african-architecture**）——**直接主体源、强支撑**（rammed earth/thatch/climate/africa/ethnic；但 `weav=0` 编织无源）。
  - `wp-history-of-architecture`（对 **latin-american-colonial**）——**直接主题源、强支撑**（baroque/latin america/colonial(Lima)/ornament/facade/indigenous；但 heavy/massive 无关→“厚重”无直证）。
  - `wp-architecture`（对 **raised-floor**）——**主题零覆盖的泛论来源**：pilotis/parking/stilt/ground floor=0，raised 命中为 Ruskin 无关句。
  - `wp-vernacular-architecture`（对 **raised-floor**）——**异类邻近**：仅防洪 stilt house（整屋抬高），parking=0，与“底层架空作公共/停车”不同 typology。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含“示意图，非施工图” | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| african-architecture | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| latin-american-colonial | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |
| raised-floor | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含“示意图，非施工图”；「常见错误与限制」段均以规范提示收尾；`check.py` 含 SVG 出界检查，本轮 PASS。**机械项三条全部通过。**
>
> **⚠ 批次级系统缺陷（与第37/38轮同类，仍未消除；本条抽检实证）：**
> 1. **SVG 图示模板化、图文脱节（实读原始 SVG 标记核对）**：
>    - `african-architecture`：SVG 仅 `<path d='M 130 300 Q 300 130 590 280'>`（一条弧线）＋一条基线 ＋ 两个 `text`（标题＋“示意图，非施工图”）；`一图` 解说“夯土墙体与茅草顶”，图上**未画任何墙体/草顶**。
>    - `latin-american-colonial` 与 `raised-floor`：两者 SVG **几何几近相同**——`<rect x='120' y='13x' width='520' height='15x'>` ＋ 一条竖向虚线 `<line x1='380' y1='120' x2='380' y2='300' stroke-dasharray='8 6'>` ＋ 两个 `text`；`一图` 解说分别为“拉美殖民建筑的要点”“架空层的要点”，图上**均无内容**且两条**互相雷同**。
>    - 即 3 条全为“一个基本形＋一条线”的**无内容占位图**，与各自 `一图` 解说**系统性脱节**（第34轮“3 套模板”、第36轮“3/12”、第37轮“2/24”、第38轮“3/25”问题在本 3 条上延续）。
> 2. **「原理」节＝ definition+overview 逐字拼接：本 3 条中 2 条命中**（`latin-american-colonial`、`raised-floor`，程序判定 `原理==definition+overview==True`）；`african-architecture` 为改写（`False`，较优）。拼接条**未提供独立机制/感受解释**，违反 L2「原理：为什么这样设计」深度要求。
> 3. **「实例」3/3 全为同一占位模板**：“名称：…（类型性描述）；地点与设计者不适用。”——满足“类型性、不编造”，但**零差异化**，实例节信息量近零（与第37/38轮同模板一致）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **三条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（`field_diffs` 均为空）：african-architecture（风格/补充/跨时期/全球/L2）；latin-american-colonial（风格/补充/文艺复兴至19世纪/美洲/L2）；raised-floor（理论/补充/20世纪/全球/L2）；`source_count` 与来源数组长度**一致**（各 2=2）；`needs_verification_count`：各 1/true；`related` 均为空数组（无悬空引用）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| african-architecture | true | 「非洲建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（但未披露“第二源伞源、编织无源”缺口） |
| latin-american-colonial | true | 「拉美殖民建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（未披露“第二源伞源、厚重无源、原理拼接”缺口） |
| raised-floor | true | 「架空层」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（**未披露“两源均不支撑核心概念、整条实质无源”这一致命缺口**） |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 三条全部 True）。
> **注意（D14 精神）**：三条「待核实」均只声明“具体实例待补充”。对 raised-floor（两源零/异类覆盖、整条核心无源）、african-architecture（伞源＋编织无源）、latin-american-colonial（伞源＋厚重无源＋原理拼接）而言，**真实存在的来源支撑缺口未被写入待核实**——属“联动一致但内容不完整/失真”，已分别在 §3.1/§3.2/§3.3 判定。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54；全库 246 条；口径②=全字段-不含 SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| african-architecture | **0.3750** vs religious-architecture | <0.54 ✓ | **0.4969** vs vernacular-architecture | <0.54 ✓（近阈） |
| latin-american-colonial | **0.4341** vs revival-gothic | <0.54 ✓ | **0.5021** vs islamic-architecture | <0.54 ✓（近阈） |
| raised-floor | **0.3759** vs sunken-atrium | <0.54 ✓ | **0.4895** vs high-tech | <0.54 ✓ |

> **三条两档全部 <0.54，无文本套话越线。** 最近邻多为同域/同类 sibling（african→vernacular-architecture、latin→islamic-architecture/revival-gothic、raised→high-tech/sunken-atrium）；近阈者（latin 0.5021、african 0.4969）反映批次高度模板化的句式骨架。
>
> **补充：本条 3 条两两相似度（口径②全字段）**：african vs latin＝0.4098、african vs raised＝0.4322、latin vs raised＝0.4649，均 <0.54。**batch-38 批内 25 条两两相似度最高仍为 futurism-style vs expressionism-style＝0.5157**（与第38轮 0.5109 同量级，近阈），结合 §五“SVG 占位/雷同、实例 3/3 同模板、原理拼接 2/3”，本批**文本层未越线，结构/图示层持续同质化**。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **african-architecture（非洲建筑）** | definition“夯土/茅草/本地材料”由 wp-vernacular 强直证；“**编织**”无源（weav/wattle/wicker/woven 全=0）；overview“气候/族群/材料”✓（climate=10/ethnic=2）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-architectural-style 泛论伞源（africa=0 零覆盖不互证）、wp-vernacular 直接主体源** | 七节齐、SVG✓（弧线+基线占位，未画土墙/草顶）、风险✓；原理=改写（非拼接） | 全部一致；nv=true/pending/待核实 逐字一致（未披露编织无源/伞源） | 0.3750 / 0.4969 | **待核实**（第二源伞源零覆盖+“编织”无源；主源核心有据；非编造） |
| **latin-american-colonial（拉美殖民建筑）** | definition“巴洛克/拉美/殖民/本地工艺”由 wp-history 强直证（baroque=30、latin america=1、colonial/Lima、indigenous=2）；“**厚重**”无直证（heavy/massive 无关）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-history 直接主题源强支撑，wp-architectural-style 泛论伞源（latin america=0、仅概念层不互证）** | 七节齐、SVG✓（矩形+虚线占位且与 raised 雷同，未画立面）、风险✓；原理=定义+概述逐字拼接 | 全部一致；nv=true/pending/待核实 逐字一致（未披露厚重无源/伞源/拼接） | 0.4341 / 0.5021 | **待核实**（第二源伞源不互证+“厚重”无源+原理拼接；主源核心较强；非编造） |
| **raised-floor（架空层）** | definition“底层架空、留作公共或停车”**无源**（pilotis/parking/ground floor 全=0）；overview“释放地面/容纳公共活动”**无源**；wp-vernacular 仅防洪 stilt house（异类）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-architecture 主题零覆盖（pilotis/parking/stilt/ground floor=0，raised 命中无关）、wp-vernacular 仅防洪抬高整屋（parking=0）** | 七节齐、SVG✓（矩形+虚线占位且与 latin 雷同，未画架空层剖面）、风险✓；原理=定义+概述逐字拼接 | 全部一致；nv=true/pending/待核实 逐字一致（**未披露整条核心无源致命缺口**） | 0.3759 / 0.4895 | **不合格**（两源均不支撑“底层架空作公共/停车”核心，实质无源＋违反两源互证） |

- **内容与来源维度**：**0 合格＋2 待核实（african-architecture、latin-american-colonial）＋1 不合格（raised-floor）＋0 编造**。definition/time/overview 支撑：african 主源强支撑但“编织”无源、第二源伞源；latin 主源强支撑但“厚重”无源、第二源伞源且原理拼接；raised 两源均不支撑核心、实质无源。三条实例均为**类型性描述**、无具名作品/作者/年份；**硬性“编造具体年份/人名/引文/出处”0 条、假 id 0 条、死链 0 条**。实质缺口在**来源支撑**（`wp-architectural-style` 对非洲/拉美泛论伞源零/近零覆盖不互证、`wp-architecture` 对架空层零覆盖）与 **african“编织”无源**、**latin“厚重”无源**、**raised 核心无源**。
- **结构与元数据维度**：三条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 三条**逐字一致**；`check.py` PASS 0 errors。**但 SVG 全为“基本形＋线”占位（latin 与 raised 几何雷同）、实例 3/3 同模板、原理=定义+概述拼接 2/3——属批次级实质缺陷（机械项因“含示意图/不出界”而误过）。**
- **相似度维度**：三条两档全部 <0.54（短文本最大 0.4341、全字段最大 0.5021），两两最高 0.4649，批内 25 条两两最高 0.5157，**文本未越线但显著近阈**，与图示占位/雷同共同反映较高模板化。

## 九、总体结论与是否建议整批返工

- **抽样结果**：3 条中 **0 合格＋2 待核实（african-architecture、latin-american-colonial）＋1 不合格（raised-floor）**；**内容/来源维度：0 编造、0 假 id、0 死链**。
- **来源层面**：4 个引用来源 id 全部存在、verified=true、均可达（owiki 200）；但 `wp-architectural-style`（对 african、latin）**泛论伞源、零/近零主题覆盖（africa=0 / latin america=0）不互证**、`wp-architecture`（对 raised-floor）**主题零覆盖（pilotis/parking/ground floor=0）**；`raised-floor` **两源均不支撑核心概念→整条实质无源 → 不合格**；`african-architecture` “编织”无源＋第二源伞源 → **待核实**；`latin-american-colonial` “厚重”无源＋第二源伞源＋原理拼接 → **待核实**。
- **结构/治理层面**：七节/SVG/规范提示机械项全过、元数据与 pending 联动三条**逐字一致**、`check.py` PASS 0 errors；**但图示占位化（latin/raised SVG 雷同）、实例 3/3 同模板、原理=定义+概述拼接 2/3——本批“形式达标、内容模板化”特征继续存在**。
- **相似度层面**：三条两档全部 <0.54（最高全字段 0.5021 近阈），两两最高 0.4649，批内 25 条两两最高 0.5157（近阈），**文本无套话越线但结构层仍高度模板化**。
- **是否建议整批返工（结论）**：
  1. **§E 硬触发已成立**：本轮出现 **1 条不合格（raised-floor）**——`AUTONOMOUS.md` §三 E / `TASK_design.md`「不合格则整批返工」硬规则**被触发**，**故明确建议 `batch-38` 整批返工**。raised-floor 的问题不仅是“单源”，而是**两个引用来源均不支撑“建筑底层架空、留作公共或停车等用途”的定义主干（pilotis/parking/ground floor 全=0；wp-vernacular 仅防洪 stilt house 异类）**，属可直接判定不合格的实质缺陷；与第38轮 `acoustic-environment`（同样用 `wp-architecture` 泛论零覆盖）**同型复发**，印证第38轮“警惕 `wp-architecture` 泛论零覆盖风险”的判断。
  2. **第38轮整批返工建议尚未执行**：`git log -1`＝`633bd70 feat: round38 all 246 scope entries written and L2`——batch-38 已按原样提交（未返工），本轮独立抽 3 条仍得“1 不合格＋2 待核实”，**进一步支持第38轮整批返工结论继续有效**。
  3. **批次级系统缺陷（独立于上述不合格，亦支持整批处理）**：
     - **图示模板化/雷同（首要）**：3/3 为“基本形＋一线”无内容占位图，`latin-american-colonial` 与 `raised-floor` 的 SVG **几何近乎完全相同**，与各自 `一图` 解说系统性脱节；系第34–38轮同型问题的延续。
     - **「原理」= definition+overview 逐字拼接 2/3**（latin、raised）、**「实例」3/3 同占位模板**：L2 内容深度不达标，属批量“骨架填充”。
  4. **定向返工/最小修复建议**：
     - **raised-floor（判不合格）**：**整条重写**——补一条真正讨论“底层架空/pilotis/开放底层（新建筑五点、Le Corbusier pilotis、城市架空层/公共开放底层）”的权威来源，据以重写定义/典型手法/原理；当前 `wp-architecture`（泛论）与 `wp-vernacular`（防洪 stilt house）均不足以支撑，且需**至少第二个独立来源互证**。
     - **african-architecture（判待核实）**：删去泛论伞源 `wp-architectural-style`（africa=0）或改配一条真正讨论“African architecture / 非洲地域建筑”的权威来源；对“编织”补源或从 definition/典型手法删去；实现“夯土/茅草/气候/族群”两源互证。
     - **latin-american-colonial（判待核实）**：以“Spanish/Portuguese colonial architecture（拉美殖民建筑）”主题源替换伞源 `wp-architectural-style`，支撑“厚重立面/繁复装饰/拉美＋本土交融”实现两源互证；补“厚重”来源或删去；将「原理」改写为独立机制解释而非定义+概述拼接。
     - **整批图示**：**全部 `batch-38` SVG 重绘为逐条贴合本条目解说的差异化示意图**（至少先重绘本报告 3 条：非洲夯土墙/茅草顶剖面、拉美殖民巴洛克立面、架空层（pilotis）开放底层剖面），杜绝“基本形＋线”占位图与 latin/raised 雷同图。
  5. **D14 披露口径统一**：本批「待核实」一律只写“具体实例待补充”，未反映真实来源缺口（raised 两源不支撑核心、african 编织无源、latin 厚重无源/伞源/拼接）；建议对确有“伞源/零覆盖/无源/拼接”的条目，把缺口如实写入「待核实」并同步 `pending_notes`。
- **流程记录**：本轮抽检 3/25＝12%（≥10% 下限）。结果 **0 合格＋2 待核实＋1 不合格、0 编造、0 假 id、0 死链、文本无套话越线**；**因 1 条不合格（raised-floor：两源均不支撑“底层架空作公共/停车”核心、整条实质无源）触发“不合格即整批返工”硬规则，加之第38轮同一整批返工建议尚未执行、批次级图示占位/雷同与原理/实例模板化仍在，明确建议 `batch-38` 整批返工、图示全面重绘，并对 raised-floor/african-architecture/latin-american-colonial 定向补源与纠错**。下轮建议对 `batch-38` 其余条目（尤其所有以 `wp-architectural-style`／`wp-architecture` 泛论源为唯一或主用来源者、以及多 theme=风格 的补充条目）按“来源正文是否支撑 definition/time/overview/实例”定向复核，并对全部 25 条 SVG 是否逐个贴合解说进行图示复核。

---

### 机器可读汇总

```
ROUND=39
SAMPLER=spotcheck-r39
SCOPE=["african-architecture","latin-american-colonial","raised-floor"]
FILES={"african-architecture":"entries/batch-38.json","latin-american-colonial":"entries/batch-38.json","raised-floor":"entries/batch-38.json"}
STATE={"sources.json":"126910B@2026-11-23 00:56:46","batch-38.json":"47258B@2026-11-23 00:56:46","coverage.json":"83078B@2026-11-23 00:56:46","total":246,"written":246,"not_started":0,"all_level":"L2","pending_total":220,"batch38_count":25}
GIT_HEAD="633bd70 feat: round38 all 246 scope entries written and L2 (unwritten=0)"; GIT_STATUS="clean except 3 untracked round39 research files (gaps/healthcheck/reader_questions-round39.md), pre-existing, not modified by this spotcheck"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/25 = 12% (>=10% floor)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia TIMEOUT -> owiki.org mirror HTTP200 (4/4 pages); analysis in-memory, no temp files"
FETCH={
 "wp-architectural-style":"OWIKI 200 21723B h1=Architectural style textlen~10185; africa=0,african=0,earth=0,thatch=0,rammed earth=0,vernacular=0,climate=0,ethnic=0 (for african) AND latin america=0,ornament=0,facade=0,indigenous=0,baroque=1,colonial=2 (for latin) -> GENERIC umbrella; ZERO Africa coverage, only concept-level for Latin America (not co-verifying)",
 "wp-vernacular-architecture":"OWIKI 200 43083B h1=Vernacular architecture textlen~26773; africa=2,african=2,rammed earth=1,thatch=4,earth=6,climate=10,ethnic=2,mud brick=3,adobe=2,indigenous=3,local material=1; weav=0,woven=0,wattle=0,wicker=0,mat=0,basket=0,plait=0,braid=0 (for african -> DIRECT strong but 编织 zero) ; stilt=2('Stilt house-raised house... prone to flooding'),ground floor=1(Alpine barn above ground floor),parking=0,pilotis=0 (for raised -> adjacent DIFFERENT typology)",
 "wp-history-of-architecture":"OWIKI 200 128112B h1=History of architecture textlen~86543; baroque=30,latin america=1('Europe, Latin America...1580-1800'),colonial=2(incl Lima),ornament=17,facade=3,façade=6,indigenous=2,rococo=16; heavy=1(Romanesque),massive=5(prehistoric/Assyrian) -> DIRECT strong for latin but '厚重' NOT supported",
 "wp-architecture":"OWIKI 200 52067B h1=Architecture textlen~31377; pilotis=0,parking=0,stilt=0,ground floor=0; raised=1=Ruskin 'edifices raised by men'(unrelated); ventilation='heating, ventilation and cooling'(generic); le corbusier=2(quote only) -> ZERO coverage of 架空层/pilotis for raised-floor"
}
SOURCES={"count_distinct":4,"count_refs":6,"all_exist":true,"all_verified_true":true,"all_urls_reachable_200":"yes (4 owiki)","relevance_defects":["wp-architectural-style generic umbrella ZERO Africa coverage (africa=0) for african-architecture","wp-architectural-style generic umbrella concept-only for latin-american-colonial (latin america=0)","wp-architecture ZERO 架空层/pilotis coverage for raised-floor (pilotis/parking/stilt/ground floor=0)","wp-vernacular-architecture stilt-house is flood-elevated dwelling, different typology from 底层架空作公共/停车"]}
BODY_SUPPORT={
 "african-architecture":"夯土(rammed earth)/茅草(thatch)/本地材料/local material supported by wp-vernacular; climate=10,ethnic=2 support overview; BUT 编织(weaving) UNSUPPORTED (weav=0,wattle=0,wicker=0,woven=0,mat=0,basket=0); wp-architectural-style umbrella ZERO (africa=0); 原理 rephrased (not concat); instance=type-description honest; NOT fabrication; VERDICT=待核实",
 "latin-american-colonial":"baroque(30)/latin america(1,Lima)/colonial/ornament(17)/facade/indigenous(2) supported by wp-history; BUT 厚重 UNSUPPORTED (heavy/massive hits unrelated); wp-architectural-style umbrella concept-only (latin america=0,ornament=0,facade=0); 原理==definition+overview verbatim concat; instance=type-description honest; NOT fabrication; VERDICT=待核实",
 "raised-floor":"definition '底层架空/公共/停车' UNSUPPORTED (pilotis=0,parking=0,ground floor=0 in wp-architecture [raised=Ruskin unrelated]; wp-vernacular only flood stilt house parking=0); overview '释放地面/容纳公共活动' UNSUPPORTED; 原理==definition+overview verbatim concat; instance=type-description honest; NOT fabricated name/year; VERDICT=不合格"
}
L2_CHECK={"seven_sections":"definition+6/6 x3, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","batch_template_defects":"3/3 placeholder SVG (african=Q-curve+baseline; latin & raised = near-identical rect+dashed-line); figure-caption disconnect; latin vs raised SVGs nearly identical; 原理==definition+overview concat 2/3 (latin,raised); 实例 template 3/3"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x3 (field_diffs=[] vs coverage.json)","source_count":"2=2 x3","nvc":"1/true x3","needs_verification/pending_notes/待核实":"verbatim-identical x3 (african/latin/raised 待核实 NOT disclosing real gaps)","related":"[] (no dangling)"}
SIMILARITY={
 "african-architecture":{"short":0.3750,"vs_short":"religious-architecture","full_no_svg":0.4969,"vs_full":"vernacular-architecture","verdict":"PASS<0.54"},
 "latin-american-colonial":{"short":0.4341,"vs_short":"revival-gothic","full_no_svg":0.5021,"vs_full":"islamic-architecture","verdict":"PASS<0.54 (near threshold)"},
 "raised-floor":{"short":0.3759,"vs_short":"sunken-atrium","full_no_svg":0.4895,"vs_full":"high-tech","verdict":"PASS<0.54"},
 "pairwise_targets":{"african_vs_latin":0.4098,"african_vs_raised":0.4322,"latin_vs_raised":0.4649},
 "intra_batch_38_max":{"full_no_svg":0.5157,"pair":["futurism-style","expressionism-style"]},
 "threshold":0.54
}
VERDICT={"african-architecture":"待核实","latin-american-colonial":"待核实","raised-floor":"不合格"}
VERDICT_SEVERITY={"african-architecture":"待核实(第二源伞源零覆盖africa=0 + 编织无源weav=0; 主源wp-vernacular对夯土/茅草/气候/族群强支撑; 非编造)","latin-american-colonial":"待核实(第二源伞源不互证latin america=0 + 厚重无源 + 原理拼接; 主源wp-history对baroque/latin america/colonial/ornament强支撑; 非编造)","raised-floor":"不合格(两源均不支撑'底层架空作公共/停车'核心: wp-architecture pilotis/parking/ground floor=0, wp-vernacular仅防洪stilt house; 实质无源, 违反两源互证; 原理拼接)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
BATCH_REWORK="YES - §E hard trigger fired: 1 不合格 (raised-floor: BOTH sources do not support core definition '建筑底层架空、留作公共或停车等用途' — wp-architecture pilotis/parking/stilt/ground floor=0 (raised=Ruskin unrelated), wp-vernacular only flood-elevated stilt house parking=0; violates two-source rule). Additionally: round38 whole-batch rework recommendation NOT executed (git HEAD 633bd70 committed batch-38 as-is); batch-level defects persist: 3/3 placeholder/duplicate SVGs (latin & raised near-identical), 原理==definition+overview concat 2/3, 实例 template 3/3. Recommend WHOLE-BATCH rework: redraw all SVGs; targeted: rewrite raised-floor with real pilotis/架空 source(s)+2nd source; fix african-architecture (replace umbrella wp-architectural-style, source or drop 编织); fix latin-american-colonial (replace umbrella source, source 厚重, de-concat 原理). 0 fabrication/0 false id/0 dead link; mechanical seven-section/metadata/check.py all pass; text similarity all<0.54 (targets max 0.5021, intra max 0.5157)."
READONLY="only wrote research/spotcheck-round39.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (no temp files written anywhere)"
```

*（报告完）*
