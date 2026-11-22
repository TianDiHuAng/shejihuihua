# 第41轮质量闸抽检报告（spotcheck-round41）——晋派建筑 / 岭南建筑 / 城市规划（batch-38 中抽 3 条）

- 抽检人：spotcheck-r41（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 01:37 起，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；新增/改动条目随机抽 10%、**至少 3 条**逐条核对来源；**不合格则整批返工**，下一轮抽检比例提高到 25%；异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 `verified=true` 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md` / `TASK_design.md` 在仓库根**无同名文件**（与第 12–40 轮一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md`（21 行）、`PROGRESS.md`（90 行）在仓库根已读。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 01:37–01:38）**：`data/sources.json`=138329B@01:36:23、`entries/batch-38.json`=47647B@01:36:23、`coverage.json`=83419B@01:36:23、`tools/check.py`=15908B@2026-11-22 15:11:54。`git log -1` = `6fb274d docs: note round40 push failure`；其上一提交 `9e66770 feat: round40 proxemics added, batch38 sourced rewrites`。
- **工作树状态**：`git status --porcelain` 仅 2 项——`?? research/gaps-round41.md`、`?? research/reader_questions-round41.md`（第41轮其它子任务产出，**非本次抽检所改**）；`entries/`、`data/`、`coverage.json` 无未提交改动。
- **条目规模（`coverage.json` 实读）**：`total=247`、全部 `level=L2`、全部 `status=已写`；`pending_total`（`needs_verification_count` 求和）＝**215**；来源库 `sources.json` 共 **293** 条，其中 `verified=true` 共 **290** 条（`link_ok=true` 145、`link_ok=null` 142）。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round41.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python urllib 读取→内存计数），未在项目内外落盘任何临时文件。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。
- **抽检口径与样本**：任务指定从 `entries/batch-38.json` 抽 **3 条**：`shanxi-style`（晋派建筑）、`lingnan-style`（岭南建筑）、`urban-planning-style`（城市规划）；均为 L2、`tier=补充`、`theme=风格`。共引用 **4 个去重来源 id（3 条 6 处引用）**：`wp-chinese-architecture`、`wp-vernacular-architecture`、`wp-architectural-style`、`wp-urban-design`（见 §二）。抽检比率 3/25＝**12%**（满足“至少 3 条、≥10%”下限；**但 §E 对上一轮（第40轮判 1 条不合格）要求本轮提至 25%，见 §九 流程说明**）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（本轮 3 条均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`）。`en.wikipedia.org` 直连按 D05 改走 **owiki 同源镜像** `https://owiki.org/wiki/<Title>` 核对标题与正文。本轮 **4 个引用来源全部实抓 HTTP 200**，h1 与 `sources.json` 标题逐条核对一致（见 §二、§四）。正文去标签后做关键词实计与上下文抽取（全程内存，不落盘）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **247 条**去重已写条目逐条扫描，警戒线 **0.54**（与第27–40轮一致）。**方法自校**：以全字段②计算 batch-38 批内两两最高，得 **futurism-style vs expressionism-style＝0.5157**，与第39/40轮报告**逐位一致**，确认口径正确。
- **“两源互证”判定口径**：按 `TASK_design.md` 硬性规则“关键事实至少两个独立来源互相印证，否则标待核实”。本轮按“两个引用来源须对本条**具体概念**有实质覆盖且互证；若第二源对本条**零覆盖或仅泛论/邻近、不涉本条具体概念**，则相关具体论断实为**单源**，据硬性规则影响判定”执行。
- **本报告三级判定定义（明确、可复现）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；两源均直接相关且关键事实获（至少近似）互证；无编造；机械项全过。
  - **待核实**：核心获**至少一个直接相关来源**实质支撑，但存在下列之一：(a) 第二源仅泛论/零覆盖、关键事实实质单源；(b) 某一具体词项（如“高墙”“窄院”“砖雕”“骑楼”“趟门”“功能分区”）无源；(c)「原理」＝定义+概述逐字拼接。→ 属来源支撑/深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被**两个引用来源均不支撑（实质无源）**，实质性违反两源互证（同第38/39/40轮 `acoustic-environment`/`raised-floor`/`tibetan-architecture` 型）。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **4 个去重来源 id（6 处引用）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）**、owiki 实抓 HTTP 200（h1 与标题一致）；`link_ok`：3 个 true、`wp-urban-design` 为 **null**（三态，非死链）。

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| shanxi-style | `wp-chinese-architecture` | ✅ / true | Chinese architecture / Wikipedia | 权威百科 | true | **直接主体源、强支撑**（该页有专节「Shanxi architecture」：`Shanxi family compounds are representative of vernacular architecture in North China`、`Merchants and bureaucrats preferred to close off the front with an imposing gate`、`Northern courtyards … keeping out the cold north winds`；`shanxi=7、jin=4、courtyard=12、family compound=1、merchant=1、carving=6、yaodong=2`） |
| shanxi-style | `wp-vernacular-architecture` | ✅ / true | Vernacular architecture / Wikipedia | 权威百科 | true | **主题零覆盖（对山西）**：`shanxi=0、jin=0、merchant=0、brick carving=0`；`courtyard=2`（中东/地中海庭院）、`family compound=1`（东非族compound）、`cave dwelling=1`（意大利 Matera）**均为他域例证，不涉山西** |
| lingnan-style | `wp-chinese-architecture` | ✅ / true | Chinese architecture / Wikipedia | 权威百科 | true | **直接主体源、强支撑**（专节「Lingnan architecture」：`Classical Lingnan architecture is used primarily in Guangdong and the eastern half of Guangxi … adaptive to the subtropical region`；另有「sky well」通风句；`lingnan=2、guangdong=2、courtyard=12、veranda=2、ventilation=1、southern=7`；**但 `qilou=0、arcade=0`——“骑楼/趟门”无源**） |
| lingnan-style | `wp-vernacular-architecture` | ✅ / true | Vernacular architecture / Wikipedia | 权威百科 | true | **主题零覆盖（对岭南）**：`lingnan=0、guangdong=0、qilou=0、arcade=0`；`ventilation=6、hot=3、tropical=1` 为**泛温带通风原理**（`cross ventilation through openings`），不涉岭南具体手法 |
| urban-planning-style | `wp-architectural-style` | ✅ / true | Architectural style / Wikipedia | 权威百科 | true | **主题零覆盖（伞源）**：`urban=0、plan=0、city=0`（仅 `road=2` 与主题无关）；该页纯讲“建筑风格分类”，**完全不涉城市规划**——正是任务提示的 `wp-architectural-style` 伞源 |
| urban-planning-style | `wp-urban-design` | ✅ / true | Urban design / Wikipedia | 权威百科 | **null** | **直接主体源、强支撑**：`urban planning=17、urban design=75、public space=13、transport=6、land use=2、grid=2`；`zoning=0`（“功能分区”无字面源，`functional=2` 为 `functionality/multifunctional` 泛义） |

> 关键事实：三条 `sources` 数组长度与 `coverage.source_count` 一致（各 2=2）。4 源均 `year=null`（在线百科，D06 允许）、`verified=true`。**无死链、无假 id、无 verified=false 被引用。** 但 `wp-vernacular-architecture`（对 shanxi、lingnan）为**他域/泛论零覆盖不互证**、`wp-architectural-style`（对 urban）为**主题零覆盖伞源**——详见 §三、§四。**关键区别（相对第40轮 tibetan）**：shanxi/lingnan 的第一源 `wp-chinese-architecture` 确有**山西/岭南专节**（`shanxi=7`、`lingnan=2`），故两条**核心主体并非无源**，与 tibetan（两源 `tibet=0` 实质无源→不合格）性质不同。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 shanxi-style（晋派建筑）——**待核实**
- **wp-chinese-architecture**（owiki HTTP200 61926B，h1「Chinese architecture」，textlen≈42254）：
  - 直证：`Shanxi family compounds are representative of vernacular architecture in North China`（山西家族院落＝北方民居代表→支撑“山西一带…聚落”）；`Merchants and bureaucrats preferred to close off the front with an imposing gate`（商贾＋临街门楼→支撑“商贾”“门楼体现财力”）；`Northern courtyards are typically open and face south … while keeping out the cold north winds`（院落御寒→支撑“御寒”）；`In the mountainous areas of Shanxi, yaodong is a type of earth shelter`（山西窑洞）。
  - 关键词实计：`shanxi=7、jin=4、merchant=1、courtyard=12、family compound=1、carving=6、yaodong=2、north china=1`；**`brick carving=0、high wall=0、defensive=0`；`narrow=1`（且唯一命中为岭南 “Narrow doors”，非“窄院”）——“高墙”“砖雕”“防卫”无源、“窄院”无源**。
- **wp-vernacular-architecture**（owiki HTTP200 43083B，h1「Vernacular architecture」，textlen≈26771）：
  - **对山西零覆盖**：`shanxi=0、jin=0、merchant=0、brick carving=0`；`courtyard=2`（中东北非/地中海 `courtyard gardens`）、`family compound=1`（东非族 `family compounds`）、`cave dwelling=1`（意大利 `Sassi di Matera`）——**均为他域例证，不涉山西/晋商**，不能互证本条。
- **逐项结论（对照所引来源）**：
  - definition“山西一带高墙窄院、砖雕精细的商贾聚落建筑”——“山西一带/商贾聚落”✓（Shanxi family compounds、merchants）；**“高墙”✗（high wall=0）、“窄院”✗（无源，且源称北方院落“typically open”，语义相左）、“砖雕”✗（brick carving=0，carving 命中皆他域/佛窟）**。
  - overview“为御寒与防卫，院落狭长、外墙高厚”——“御寒”✓（keeping out cold north winds）；**“防卫”✗（defensive=0）、“院落狭长/外墙高厚”✗（无源，且“狭长”与源“typically open”相左）**。
  - time_or_place“古代、中国”——✓（源为山西历代木构与北方民居，方向一致）。
  - **原理**“高墙窄院利于保温与防卫，砖雕与门楼体现财力与礼制”——**为改写（非拼接，程序判定 `原理==definition+overview==False`）**；其中“保温”✓（cold north winds）、“门楼”✓（imposing gate）、“礼制”可由 `All buildings were legally regulated` 间接支撑，但**“防卫”“砖雕”仍无源**。
  - 实例＝“名称：晋商高墙窄院（**类型性描述**）；地点与设计者不适用。两进窄院夹在高厚砖墙之间，门楼砖雕在冬日斜阳里投下细密阴影。”**类型性、无具名作品/作者/年份 → 不编造** ✓；但“两进窄院/高厚砖墙/砖雕”等描述性论断**均无所引来源支撑**。
- **两源互证**：核心（山西商贾聚落）由 `wp-chinese-architecture` **强直证**；但第二源 `wp-vernacular-architecture` **对山西零覆盖（他域例证）**、且“高墙/窄院/砖雕/防卫”具体词项无源、部分与源相左，**关键描述实质单源+具体项无源**。
- **判定：待核实**（非编造；第一源直接相关、核心强支撑；缺陷＝第二源对山西零覆盖不互证 + 高墙/窄院/砖雕/防卫无源）。

### 3.2 lingnan-style（岭南建筑）——**待核实**
- **wp-chinese-architecture**（owiki HTTP200 61926B，h1「Chinese architecture」）：
  - 直证：`Classical Lingnan architecture is used primarily in Guangdong and the eastern half of Guangxi. It is noted for its use of carvings and sculptures for decorations, green brick, balconies, "Cold alleys", "Narrow doors", and many other characteristics adaptive to the subtropical region`（岭南/广东✓、应对亚热带湿热✓、装饰雕刻/绿砖/阳台/冷巷✓）；`"Sky well" … concept of an "open space" surrounded by buildings … these enclosures aid in temperature regulation and in ventilation`（天井＝sky well✓、拔风降温✓）。
  - 关键词实计：`lingnan=2、guangdong=2、courtyard=12、veranda=2、tropical=1、humid=1、ventilation=1、southern=7、hot=1`；**`qilou=0、arcade=0`——英文源不载“骑楼(arcade)”；“趟门”亦无对应（源仅 “Narrow doors”，语义不同）**。
- **wp-vernacular-architecture**（owiki HTTP200 43083B，h1「Vernacular architecture」）：
  - **对岭南零覆盖**：`lingnan=0、guangdong=0、qilou=0、arcade=0`；仅 `ventilation=6、hot=3、tropical=1` 为**泛温带/湿热气候通用原理**（`Buildings in warm climates … allow significant cross ventilation`），不涉岭南骑楼/趟门/天井手法。
- **逐项结论（对照所引来源）**：
  - definition“岭南建筑以骑楼、趟门、天井应对湿热多雨”——“岭南✓、应对湿热多雨✓、天井✓（sky well）、通风降温✓”；**“骑楼✗（qilou/arcade=0）、“趟门✗（无源）”——定义三项特征中两项无源**。
  - overview“它通透轻巧，靠遮阳与通风降温”——通风降温✓（sky well aids ventilation/温度调节）、通透/轻巧大致✓（balconies、亚热带适应性、lighter 材料）；“遮阳”仅可由 balconies/亚热带间接推断，无字面。
  - time_or_place“古代、中国”——✓（Classical Lingnan，广东/广西，方向一致）。
  - **原理**“骑楼遮阳避雨、天井拔风、趟门调节通风，构成湿热气候的空间策略”——**为改写（非拼接，`False`）**；“天井拔风”✓（sky well ventilation），**“骑楼”“趟门”仍无源**。
  - 实例＝“名称：骑楼下的街屋（**类型性描述**）；地点与设计者不适用。二层出挑的骑楼在街道上连成遮阳长廊，天井把湿热空气从屋顶拔走。”**类型性、无具名/年份 → 不编造** ✓；但“骑楼”无源、“天井拔风”有源。
- **两源互证**：核心“岭南应对湿热”由 `wp-chinese-architecture` **强直证**；但“骑楼/趟门”两项标志性手法无源，第二源 `wp-vernacular-architecture` **对岭南零覆盖（仅泛温带通风）**，**关键手法实质单源+两项无源**。
- **判定：待核实**（非编造；第一源直接相关、岭南核心强支撑；缺陷＝骑楼/趟门无源 + 第二源零覆盖不互证）。

### 3.3 urban-planning-style（城市规划）——**待核实**
- **wp-urban-design**（owiki HTTP200 59478B，h1「Urban design」，textlen≈38256，`link_ok=null` 但 verified=true）：
  - 直证：`Urban designers connect … architecture, landscape architecture and urban planning`、`Urban design deals with the larger scale of groups of buildings, infrastructure, streets, and public spaces, entire neighbourhoods and districts, and entire cities`、`design and management of public space`、`grid plan of a city layout`、`land use`、`transportation`——支撑“城市用地(land use)/交通(transport)/公共空间(public space)/路网(grid)/整体安排”。
  - 关键词实计：`urban planning=17、urban design=75、public space=13、transport=6、land use=2、grid=2、functional=2`；**`zoning=0`——“功能分区”无字面源**（`functional=2` 为 `functionality`/`multifunctional` 泛义）。
- **wp-architectural-style**（owiki HTTP200 21723B，h1「Architectural style」，textlen≈10183）：
  - **主题零覆盖（伞源）**：`urban=0、plan=0、city=0`（仅 `road=2` 与城市规划无关）。该页纯讲“建筑风格/样式分类”，**完全不涉城市规划**，正是任务点名的 `wp-architectural-style` 伞源。
- **逐项结论（对照所引来源）**：
  - definition“城市规划指对城市用地、交通与公共空间的整体安排”——“城市用地✓、交通✓、公共空间✓、整体安排✓”，由 `wp-urban-design` **强支撑**。
  - overview“它协调功能分区、路网与开放空间”——“路网✓（grid plan）、开放空间✓（public space）”；**“功能分区✗（zoning=0）无源**。
  - time_or_place“跨时期、全球”——✓（urban design 通史至现代、全球）。
  - **原理**“城市规划指对城市用地、交通与公共空间的整体安排。它协调功能分区、路网与开放空间。”——**＝definition+overview 逐字拼接（程序判定 `原理==definition+overview==True`）**，**无独立机制/感受解释**（L2「原理」深度不足）；且“功能分区”无源。
  - 实例＝“名称：城市规划的典型场景（**类型性描述**）；地点与设计者不适用。”**类型性、无具名/年份 → 不编造** ✓，但信息量近零。
- **两源互证**：核心（用地/交通/公共空间/路网）由 `wp-urban-design` **强直证**；但**第二源 `wp-architectural-style` 对城市规划零覆盖（`urban=0、plan=0、city=0`）**，“功能分区”无源，`原理`拼接——**关键事实实质单源**。
- **判定：待核实**（非编造；第一源强、直接相关；缺陷＝第二源零覆盖伞源不互证 + “功能分区”无源 + 原理=定义+概述逐字拼接）。
- **次要观察（非判定主因）**：本条 `theme=风格`，而“城市规划”实为学科/实践而非“建筑风格”，分类存疑；建议复审其 theme（或归入动线/理论类）。`time_or_place`“跨时期、全球”与 `region=全球` 合理。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：4 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）。`link_ok`：`wp-chinese-architecture`/`wp-vernacular-architecture`/`wp-architectural-style`=true，**`wp-urban-design`=null**（三态，非死链、非假源）。
- **可达性（本轮实抓，owiki 镜像）**：`wp-chinese-architecture`（200 61926B h1=Chinese architecture）/ `wp-vernacular-architecture`（200 43083B h1=Vernacular architecture）/ `wp-architectural-style`（200 21723B h1=Architectural style）/ `wp-urban-design`（200 59478B h1=Urban design）。**4 个来源 id 全部可达，无死链。**（`en.wikipedia.org` 直连按 D05 改走 owiki 镜像；正文完整，非截断。）
- **相关性缺陷**：
  - `wp-vernacular-architecture`（对 **shanxi-style**）——**对他域/零覆盖**：`shanxi=0、jin=0、merchant=0、brick carving=0`，courtyard/family compound/cave dwelling 命中皆中东/非洲/意大利。
  - `wp-vernacular-architecture`（对 **lingnan-style**）——**对岭南零覆盖**：`lingnan=0、guangdong=0、qilou=0、arcade=0`，仅泛温带通风。
  - `wp-architectural-style`（对 **urban-planning-style**）——**主题零覆盖伞源**：`urban=0、plan=0、city=0`。
  - `wp-chinese-architecture`（对 shanxi、lingnan）/ `wp-urban-design`（对 urban）——**直接主体源、强支撑**（唯一缺陷分别为 shanxi“高墙/窄院/砖雕/防卫”无源、lingnan“骑楼/趟门”无源、urban“功能分区”无源）。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含“示意图，非施工图” | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shanxi-style | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| lingnan-style | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |
| urban-planning-style | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含“示意图，非施工图”；「常见错误与限制」段均以规范提示收尾；`check.py` 含 SVG 出界检查，本轮 PASS。**机械项三条全部通过。**
>
> **⚠ 批次级系统缺陷（与第34–40轮同类，仍未消除；本条抽检实证）：**
> 1. **SVG 图示模板化、图文脱节、且与全库多条几何雷同（实读原始 SVG 标记 + 几何相似度核对）**：
>    - `shanxi-style`：SVG 仅 `<polygon points='184,300 380,124 566,300'…/>`（三角形）＋`<rect x='334' y='250' width='120' height='50'…/>`（矩形）＋标题/“示意图，非施工图”两段文字；**未画高墙/窄院/砖雕**。几何相似度：**vs tibetan-architecture=0.963、vs rock-garden=0.956、vs korean-architecture=0.956**（同一“三角＋矩形”模板）。
>    - `lingnan-style`：SVG 仅三个 `<rect>`＋两段文字；**未画骑楼长廊/天井拔风**。几何相似度：**vs earth-sheltered=0.977、vs southeast-asian-architecture=0.977、vs xinjiang-architecture=0.973**。
>    - `urban-planning-style`：SVG 仅一条 `<path>` 曲线＋一条 `<line>` 底线＋文字；**未画路网/功能分区**。几何相似度：**vs romanticism-style=0.981、vs african-architecture=0.968、vs hokkien-style=0.968**。
>    - 即 3 条全为“基本形”的**无内容占位图**，与各自 `一图` 解说**系统性脱节**，且与库内多条**几何近乎相同（模板复用）**；`batch-38` 中仍有 4/25 条为“polygon+rect”同模板。延续第34–40轮同型问题。
> 2. **「原理」节＝ definition+overview 逐字拼接：本 3 条中 1 条命中**（`urban-planning-style`，程序判定 `原理==definition+overview==True`）；`shanxi`、`lingnan` 为改写（`False`）。拼接条**未提供独立机制/感受解释**，违反 L2「原理：为什么这样设计」深度要求。
> 3. **「实例」：3/3 均为“名称：…的典型/类型场景（类型性描述）；地点与设计者不适用”模板**——均满足“类型性、不编造”，但**信息量近零、模板高度同质**，未落到 L2“只写名称、地点、设计者、年份”的具名实例要求（以“待补充”披露）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **三条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（`field_diffs` 均为空）：shanxi（风格/补充/古代/中国/L2）、lingnan（风格/补充/古代/中国/L2）、urban（风格/补充/跨时期/全球/L2）；`source_count` 与来源数组长度**一致**（各 2=2）；`needs_verification_count`：各 1/true；`related` 均为空数组（无悬空引用）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| shanxi-style | true | 「晋派建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（未披露“高墙/窄院/砖雕/防卫无源、第二源零覆盖”缺口） |
| lingnan-style | true | 「岭南建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（未披露“骑楼/趟门无源、第二源零覆盖”缺口） |
| urban-planning-style | true | 「城市规划」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（未披露“第二源零覆盖伞源、功能分区无源、原理拼接”缺口） |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 三条全部 True）。
> **注意（D14 精神）**：三条「待核实」均只声明“具体实例待补充”。对 shanxi（高墙/窄院/砖雕/防卫无源、第二源零覆盖）、lingnan（骑楼/趟门无源、第二源零覆盖）、urban（第二源伞源零覆盖、功能分区无源、原理拼接）而言，**真实存在的来源支撑缺口未被写入待核实**——属“联动一致但内容不完整/失真”，已在 §3 各条判定。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54；全库 247 条；口径②=全字段-不含 SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| shanxi-style | **0.4035** vs imperial-architecture | <0.54 ✓ | **0.4933** vs hakka-style | <0.54 ✓（近阈） |
| lingnan-style | **0.5000** vs xinjiang-architecture | <0.54 ✓（近阈） | **0.4895** vs southeast-asian-architecture | <0.54 ✓ |
| urban-planning-style | **0.3818** vs opening-interface | <0.54 ✓ | **0.4966** vs view-corridor | <0.54 ✓（近阈） |

> **三条两档全部 <0.54，无文本套话越线**。最近邻多为同域/同类 sibling：`shanxi→hakka-style/imperial-architecture`（同为中国地域/传统风格）、`lingnan→xinjiang/southeast-asian-architecture`（地域风格补充）、`urban→view-corridor/opening-interface`（空间组织类）。近阈者（lingnan 短文本 0.5000、urban 全字段 0.4966、shanxi 全字段 0.4933）反映批次高度模板化的句式骨架。
>
> **补充：本条 3 条两两相似度**：shanxi vs lingnan＝短 0.3636/全 0.4506、shanxi vs urban＝0.2241/0.4035、lingnan vs urban＝0.2222/0.4238，均 <0.54。**batch-38 批内 25 条两两相似度最高仍为 futurism-style vs expressionism-style＝0.5157**（与第39/40轮 0.5157 逐位一致，方法自校依据），文本层未越线；但结合 §五“SVG 占位/雷同（几何相似度普遍>0.95）、实例 3/3 同模板、原理拼接 1/3”，**结构/图示层持续严重同质化**。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **shanxi-style（晋派建筑）** | “山西一带/商贾聚落”由 wp-chinese-architecture **强直证**（Shanxi family compounds、merchants、imposing gate、cold north winds 原句）；**“高墙”“窄院”“砖雕”“防卫”无源**（high wall/brick carving/defensive=0；窄院与源“northern courtyards typically open”相左）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-chinese-architecture 直接主体源强支撑（有 Shanxi 专节），wp-vernacular-architecture 对山西零覆盖（他域例证）不互证** | 七节齐、SVG✓（三角+矩形占位且与 tibetan/rock/korean 几何≈0.96 雷同，未画高墙窄院）、风险✓；原理改写（非拼接）但“防卫/砖雕”无源 | 全部一致；nv=true/pending/待核实 逐字一致（未披露无源/第二源零覆盖） | 0.4035 / 0.4933 | **待核实**（第二源零覆盖不互证 + 高墙/窄院/砖雕/防卫无源；主源强；非编造） |
| **lingnan-style（岭南建筑）** | “岭南/应对湿热/天井(sky well)/通风”由 wp-chinese-architecture **强直证**；**“骑楼”“趟门”无源**（qilou/arcade=0，源仅 “Narrow doors/balconies/Cold alleys”）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-chinese-architecture 直接主体源强支撑（有 Lingnan 专节），wp-vernacular-architecture 对岭南零覆盖（仅泛温带通风）不互证** | 七节齐、SVG✓（三矩形占位且与 earth-sheltered/southeast-asian/xinjiang 几何≈0.97 雷同，未画骑楼天井）、风险✓；原理改写（非拼接）但“骑楼/趟门”无源 | 全部一致；nv=true/pending/待核实 逐字一致（未披露无源/第二源零覆盖） | 0.5000 / 0.4895 | **待核实**（第二源零覆盖不互证 + 骑楼/趟门无源；主源强；非编造） |
| **urban-planning-style（城市规划）** | “用地/交通/公共空间/路网/整体安排”由 wp-urban-design **强直证**（land use/transport/public space/grid 原句）；**“功能分区”无源**（zoning=0）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-urban-design 直接主体源强支撑（link_ok=null 但 verified），wp-architectural-style 主题零覆盖伞源（urban/plan/city=0）不互证** | 七节齐、SVG✓（曲线+底线占位且与 romanticism/african/hokkien 几何≈0.97 雷同，未画路网/分区）、风险✓；原理=定义+概述逐字拼接 | 全部一致；nv=true/pending/待核实 逐字一致（未披露伞源/功能分区/拼接） | 0.3818 / 0.4966 | **待核实**（第二源零覆盖伞源不互证 + 功能分区无源 + 原理拼接；主源强；非编造） |

- **内容与来源维度**：**0 合格＋3 待核实＋0 不合格＋0 编造**。definition/time/overview 支撑：shanxi 主源强但“高墙/窄院/砖雕/防卫”无源、第二源他域零覆盖；lingnan 主源强但“骑楼/趟门”无源、第二源零覆盖；urban 主源强但“功能分区”无源、第二源伞源零覆盖、原理拼接。三条实例均为**类型性描述**、无具名作品/作者/年份；**硬性“编造具体年份/人名/引文/出处”0 条、假 id 0 条、死链 0 条**。实质缺口在**来源支撑与深度**（第二源零覆盖/他域/伞源、标志性手法词项无源、1 条原理拼接）。
- **结构与元数据维度**：三条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 三条**逐字一致**；`check.py` PASS 0 errors。**但 SVG 全为“基本形”占位并与全库多条几何≈0.96–0.98 雷同（模板复用）、实例 3/3 同模板、原理拼接 1/3——属批次级实质缺陷（机械项因“含示意图/不出界”而误过）。**
- **相似度维度**：三条两档全部 <0.54（短文本最大 0.5000、全字段最大 0.4966），两两最高 0.4506，批内 25 条两两最高 0.5157，**文本未越线但显著近阈**，与图示占位/雷同共同反映较高模板化。

## 九、总体结论与返工建议

- **抽样结果**：3 条中 **0 合格＋3 待核实（shanxi-style、lingnan-style、urban-planning-style）＋0 不合格**；**内容/来源维度：0 编造、0 假 id、0 死链**。
- **来源层面**：4 个引用来源 id 全部存在、verified=true、均可达（owiki 200）；但 `wp-vernacular-architecture`（对 shanxi、lingnan）**对他域/零覆盖**、`wp-architectural-style`（对 urban）**主题零覆盖伞源**；3 条均存在“标志性/具体词项无源”（shanxi：高墙/窄院/砖雕/防卫；lingnan：骑楼/趟门；urban：功能分区）与“第二源不互证”。**因三条核心主体均有第一直接源强支撑（`wp-chinese-architecture` 有山西/岭南专节、`wp-urban-design` 强覆盖），故均判“待核实”，无一构成“两源均不支撑核心→不合格”**（与第40轮 tibetan 明确区分）。
- **结构/治理层面**：七节/SVG/规范提示机械项全过、元数据与 pending 联动三条**逐字一致**、`check.py` PASS 0 errors；**但图示占位化并与全库多条几何≈0.96–0.98 雷同、实例 3/3 同模板、urban 原理=定义+概述拼接——本批“形式达标、内容模板化”特征继续存在**。
- **相似度层面**：三条两档全部 <0.54（最高短文本 0.5000、最高全字段 0.4966，近阈），两两最高 0.4506，批内 25 条两两最高 0.5157（近阈），**文本无套话越线但结构层仍高度模板化**。
- **是否建议整批返工（结论）**：
  1. **§E 整批返工硬触发本轮未成立**：本轮**无“不合格”条目**（三条均“待核实”），故不因本轮抽检直接触发“不合格即整批返工”。但三条反映的**第二源零覆盖/伞源、标志性词项无源、原理拼接、SVG 模板复用**属 batch-38 持续性系统缺陷，**建议对 batch-38 做定向返工 + 扩大补抽**（见下）。
  2. **定向返工/最小修复建议**：
     - **shanxi-style（待核实）**：保留 `wp-chinese-architecture`（有 Shanxi 专节，直接强源）；**替换第二源** `wp-vernacular-architecture`（对山西零覆盖）→ 用库内 `wp-courtyard`（院落/四合院）或**新增一条山西民居/晋商大院（如 Wikipedia “Shanxi architecture”/晋商大院）来源**实现互证；**删改“高墙/窄院/防卫”等无源且与源相左的表述**（源称北方院落 typically open），或补源；“砖雕”补源或删；SVG 重绘为“高墙窄院长剖面＋门楼”。
     - **lingnan-style（待核实）**：保留 `wp-chinese-architecture`（有 Lingnan 专节）；**替换第二源** `wp-vernacular-architecture`（对岭南零覆盖）→ **新增岭南建筑/骑楼来源**（库内暂无独有源，如 Wikipedia “Lingnan architecture”“Qilou/骑楼”）；**“骑楼/趟门”若无源则从 definition/原理删去或补源**（现仅天井 sky well 有源）；SVG 重绘为“骑楼长廊＋天井拔风剖面”。
     - **urban-planning-style（待核实）**：**替换第二源** `wp-architectural-style`（零覆盖伞源）→ 用库内 `wp-urban-morphology` 或**新增 “Urban planning/城市规划” 来源**；**「功能分区」补 zoning 来源或改为“用地/路网/开放空间”**；**「原理」改写为独立机制解释（非定义+概述拼接）**；SVG 重绘为“路网/功能分区示意图”；**复核 `theme=风格` 是否应为动线/理论类**。
     - **整批图示**：**全部 `batch-38` SVG 重绘为逐条贴合本条目解说的差异化示意图**，杜绝“基本形”占位与跨条目几何复用（本报告 3 条与库内多条相似度>0.95）。
  3. **D14 披露口径统一**：本批「待核实」一律只写“具体实例待补充”，未反映真实来源缺口（高墙/窄院/砖雕/防卫、骑楼/趟门、功能分区无源；第二源零覆盖/伞源；原理拼接）；建议对确有“伞源/零覆盖/无源/拼接”的条目，把缺口如实写入「待核实」并同步 `pending_notes`。
  4. **流程说明（§E 抽检比例）**：第40轮已判 1 条不合格（tibetan-architecture），按 §E「下一轮把抽检比例提高到 25%」，本轮对 batch-38（25 条）应抽 **≈7 条**；而本任务仅抽 **3 条（12%）**，**低于 §E 上调后的比例**。建议：对 batch-38 其余条目——尤其所有以 `wp-architectural-style`/`wp-vernacular-architecture`/`wp-chinese-architecture` 作主/伞源、`theme=风格` 的地域/风格补充条目（如 shanxi/lingnan/hokkien/hakka/gan/xinjiang/korean/southeast-asian 等）——**补抽至 25%** 或整批复查，确认是否同型“第二源零覆盖/伞源 + 标志性词项无源”。
- **流程记录**：本轮抽检 3/25＝12%（达“至少 3 条、≥10%”下限，但低于 §E 上一轮不合格后应提的 25%）。结果 **0 合格＋3 待核实＋0 不合格、0 编造、0 假 id、0 死链、文本无套话越线**；批次级缺陷（SVG 模板复用/占位、实例同模板、urban 原理拼接、第二源零覆盖/伞源、标志性词项无源）继续存在，**建议对上述 3 条定向返工并对 batch-38 补抽至 25%**。

---

### 机器可读汇总

```
ROUND=41
SAMPLER=spotcheck-r41
SCOPE=["shanxi-style","lingnan-style","urban-planning-style"]
FILES={"shanxi-style":"entries/batch-38.json","lingnan-style":"entries/batch-38.json","urban-planning-style":"entries/batch-38.json"}
STATE={"sources.json":"138329B@2026-11-23 01:36:23","batch-38.json":"47647B@2026-11-23 01:36:23","coverage.json":"83419B@2026-11-23 01:36:23","total":247,"written":247,"not_started":0,"all_level":"L2","pending_total":215,"sources_total":293,"sources_verified_true":290,"link_ok_true":145,"link_ok_null":142,"batch38_count":25}
GIT_HEAD="6fb274d docs: note round40 push failure"; GIT_STATUS="clean except 2 untracked round41 research files (gaps/reader_questions-round41.md), pre-existing, not modified by this spotcheck"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/25 = 12% (>=10% & >=3 floor; BUT round40 had 1 不合格 -> §E post-fail ratio should be 25% ~=7, so undersampled)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia -> owiki.org mirror HTTP200 (4/4 pages); analysis in-memory, no temp files; pages complete"
FETCH={
 "wp-chinese-architecture":"OWIKI 200 61926B h1=Chinese architecture textlen~42254; shanxi=7,jin=4,merchant=1,courtyard=12,family compound=1,yaodong=2,carving=6,north china=1; brick carving=0,high wall=0,defensive=0,narrow=1(only Lingnan 'Narrow doors'); lingnan=2,guangdong=2,veranda=2,tropical=1,humid=1,ventilation=1,southern=7; qilou=0,arcade=0; quotes 'Shanxi family compounds are representative of vernacular architecture in North China','Merchants and bureaucrats preferred to close off the front with an imposing gate','Northern courtyards are typically open and face south...keeping out the cold north winds','Classical Lingnan architecture is used primarily in Guangdong...adaptive to the subtropical region','Sky well...aid in temperature regulation and in ventilation'",
 "wp-vernacular-architecture":"OWIKI 200 43083B h1=Vernacular architecture textlen~26771; shanxi=0,jin=0,merchant=0,brick carving=0; courtyard=2(MiddleEast/Med),family compound=1(EastAfrican),cave dwelling=1(Sassi di Matera); lingnan=0,guangdong=0,qilou=0,arcade=0,ventilation=6,hot=3,tropical=1(generic warm-climate cross ventilation) -> ZERO regional coverage for shanxi & lingnan",
 "wp-architectural-style":"OWIKI 200 21723B h1=Architectural style textlen~10183; urban=0,plan=0,city=0,road=2 -> ZERO coverage of urban planning (umbrella source)",
 "wp-urban-design":"OWIKI 200 59478B h1=Urban design textlen~38256; urban planning=17,urban design=75,public space=13,transport=6,land use=2,grid=2,functional=2; zoning=0"
}
SOURCES={"count_distinct":4,"count_refs":6,"all_exist":true,"all_verified_true":true,"link_ok":{"wp-chinese-architecture":true,"wp-vernacular-architecture":true,"wp-architectural-style":true,"wp-urban-design":null},"all_owiki_reachable_200":"yes (4/4)","relevance_defects":["wp-vernacular-architecture ZERO Shanxi coverage (shanxi/jin/merchant=0; courtyard/family compound/cave dwelling are other regions) for shanxi-style","wp-vernacular-architecture ZERO Lingnan coverage (lingnan/guangdong/qilou/arcade=0; only generic warm-climate ventilation) for lingnan-style","wp-architectural-style ZERO urban-planning coverage (urban/plan/city=0) UMBRELLA for urban-planning-style"]}
BODY_SUPPORT={
 "shanxi-style":"definition '山西一带高墙窄院/砖雕精细/商贾聚落' : 山西+商贾聚落 DIRECT by wp-chinese-architecture (Shanxi family compounds, merchants, imposing gate, cold north winds); 高墙/窄院/砖雕/防卫 UNSUPPORTED (high wall/brick carving/defensive=0; 窄院 contradicted by 'northern courtyards typically open'); wp-vernacular ZERO Shanxi; 原理 rephrased (not concat) but 防卫/砖雕 unsourced; instance=type-description honest; NOT fabrication; VERDICT=待核实",
 "lingnan-style":"definition '骑楼/趟门/天井 应对湿热多雨' : 岭南+应对湿热+天井(sky well)+通风 DIRECT by wp-chinese-architecture; 骑楼(qilou)/趟门 UNSUPPORTED (qilou=0/arcade=0, only 'Narrow doors/balconies/Cold alleys'); wp-vernacular ZERO Lingnan (generic warm-climate only); 原理 rephrased (not concat) but 骑楼/趟门 unsourced; instance=type-description honest; NOT fabrication; VERDICT=待核实",
 "urban-planning-style":"definition '用地/交通/公共空间/整体安排' DIRECT by wp-urban-design (land use/transport/public space/grid); overview '功能分区' UNSUPPORTED (zoning=0); wp-architectural-style ZERO coverage UMBRELLA (urban/plan/city=0); 原理==definition+overview VERBATIM concat (True); instance=type-description honest; NOT fabrication; theme=风格 classification questionable (minor); VERDICT=待核实"
}
L2_CHECK={"seven_sections":"definition+6/6 x3, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_template_defect":"3/3 placeholder SVG; geometry near-identical to other entries: shanxi vs tibetan=0.963/rock=0.956/korean=0.956; lingnan vs earth-sheltered=0.977/southeast-asian=0.977/xinjiang=0.973; urban vs romanticism=0.981/african=0.968/hokkien=0.968; batch-38 polygon+rect=4/25","原理_concat":"urban-planning-style only (True); shanxi/lingnan rephrased (False)","实例_template":"3/3 same type-description template, no named instance (disclosed via pending)"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x3 (field_diffs=[])","source_count":"2=2 x3","nvc":"1/true x3","needs_verification/pending_notes/待核实":"verbatim-identical x3 (NOT disclosing real gaps)","related":"[] (no dangling)"}
SIMILARITY={
 "shanxi-style":{"short":0.4035,"vs_short":"imperial-architecture","full_no_svg":0.4933,"vs_full":"hakka-style","verdict":"PASS<0.54 (near)"},
 "lingnan-style":{"short":0.5000,"vs_short":"xinjiang-architecture","full_no_svg":0.4895,"vs_full":"southeast-asian-architecture","verdict":"PASS<0.54 (near short)"},
 "urban-planning-style":{"short":0.3818,"vs_short":"opening-interface","full_no_svg":0.4966,"vs_full":"view-corridor","verdict":"PASS<0.54 (near)"},
 "pairwise_targets":{"shanxi_vs_lingnan":{"short":0.3636,"full":0.4506},"shanxi_vs_urban":{"short":0.2241,"full":0.4035},"lingnan_vs_urban":{"short":0.2222,"full":0.4238}},
 "intra_batch_38_max":{"full_no_svg":0.5157,"pair":["futurism-style","expressionism-style"]},
 "method_selfcheck":"intra-batch-38 max 0.5157 matches round39/40 exactly -> method validated",
 "threshold":0.54
}
VERDICT={"shanxi-style":"待核实","lingnan-style":"待核实","urban-planning-style":"待核实"}
VERDICT_SEVERITY={"shanxi-style":"待核实(第二源 wp-vernacular 对山西零覆盖不互证 + 高墙/窄院/砖雕/防卫无源(high wall/brick carving/defensive=0; 窄院 contradicted); 主源 wp-chinese-architecture 有 Shanxi 专节强支撑; 非编造)","lingnan-style":"待核实(第二源 wp-vernacular 对岭南零覆盖不互证 + 骑楼/趟门无源(qilou/arcade=0); 主源 wp-chinese-architecture 有 Lingnan 专节强支撑 shell+天井; 非编造)","urban-planning-style":"待核实(第二源 wp-architectural-style 主题零覆盖伞源(urban/plan/city=0) + 功能分区无源(zoning=0) + 原理=def+overview 拼接; 主源 wp-urban-design 强支撑; 非编造; theme=风格 分类存疑)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
BATCH_REWORK="NOT hard-triggered this round (0 不合格, all 3=待核实, no 'BOTH sources unsupport core'). However batch-level systemic defects persist across batch-38: (1) 3/3 placeholder SVGs geometrically near-identical to multiple other entries (>0.95); (2) instance 3/3 same template, no named example; (3) urban 原理=def+overview verbatim concat; (4) second sources zero-coverage/umbrella (wp-vernacular-architecture for shanxi&lingnan; wp-architectural-style UMBRELLA for urban); (5) signature terms unsourced (shanxi 高墙/窄院/砖雕/防卫; lingnan 骑楼/趟门; urban 功能分区). Recommend TARGETED rework of these 3 + batch-wide SVG redraw + replace second sources (shanxi: add Shanxi/晋商 source or wp-courtyard; lingnan: add Lingnan/Qilou source, delete unsourced 骑楼/趟门 or source them; urban: swap wp-architectural-style->wp-urban-morphology/Urban planning source, rewrite 原理, source 功能分区, reclassify theme). Process: round40 had 1 不合格 -> §E says sample 25%(~7/25) but this task sampled only 3/25=12% -> recommend补抽至25%. 0 fabrication/0 false id/0 dead link; mechanical seven-section/metadata/check.py all pass; text similarity all<0.54 (short max 0.5000, full max 0.4966, intra-batch max 0.5157)."
READONLY="only wrote research/spotcheck-round41.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (no temp files written anywhere)"
```

*（报告完）*
