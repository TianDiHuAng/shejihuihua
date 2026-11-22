# 第35轮质量闸抽检报告（spotcheck-round35）——叠石 / 下沉花园 / 材料色彩（第35轮新增 12 条中抽 3 条）

- 抽检人：spotcheck-r35（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 00:08 起，核对完成约 2026-11-23 00:25，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 10%、至少 3 条逐条核对来源；**不合格则整批返工**，下一轮抽检比例提高到 25%；异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载不运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 verified=true 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根**无同名文件**（已 `ops_glob` 确认）；实际位于 `D:/Users/Administrator/Desktop/`（与第 12–34 轮一致），已按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）；`DECISIONS.md` 在仓库根（21 行）。本轮抽检比例 3/12＝**25%**，与 `METRICS.json` round34 `spotcheck_policy_next_round="25%"` 一致。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong）**：`data/sources.json`=120373B@23:47:23（git 未改，与 HEAD 一致）、`entries/batch-35.json`=23133B@00:08:00、`coverage.json`=83245B@00:07:52、`tools/add_round35.py`=11296B@00:07:45。`git log -1` = `c1ced74 feat: round34 twelve style-history entries`。`git status --porcelain` 显示 ` M coverage.json`、`?? entries/batch-35.json`、`?? tools/add_round35.py`——**即第35轮改动尚未提交**，工作树含本轮未入库改动，属本轮执行中的正常中间态（本轮抽检未改动上述任何文件）。
- **条目规模**：`entries/*.json` 共 **23 文件 / 185 条**（第34轮末 173 条，第35轮 `batch-35` 新增 12 条 → 185；与 `coverage.json` 中 `status=已写` 的 185 条一致；coverage 总口径 246 = 已写 185 + 未开始 61，级别 185 全 L2 + 61 未开始 L1；无重复 id）。`pending_total`（`needs_verification_count` 求和）＝**159**（＝round34 的 147 + 本轮新增 12 条各 1）。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round35.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取全程在 Python 进程内存中进行、**未落盘任何临时文件**（脚本经 stdin 传入 Python，无临时文件）；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。
- **抽检口径与样本**：任务指定第35轮新增 12 条中抽 **3 条**：`rockery`（叠石）、`sunken-garden`（下沉花园）、`material-color`（材料色彩），均在 `entries/batch-35.json`；12 条全为 L2。引用来源为 `wp-chinese-garden`、`wp-garden-design`、`wp-sunken-courtyard`、`wp-color-theory`、`wp-building-material`（见 `data/sources.json`，去重共 5 个来源 id）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（本轮均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书）。先试 `en.wikipedia.org` canonical，本轮仍**超时/失败**（与历史 10060 一致，`web_fetch` 亦返回 `fetch failed`），改 **owiki 同源镜像** `https://owiki.org/wiki/<Title>` 核对标题与正文（DECISIONS D05 允许）。本轮 **3 条共 5 个引用来源 id 全部实抓 HTTP 200**（均经 owiki 镜像），无死链。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）；①短文本＝title+definition+time_or_place+overview；②全字段-不含 SVG 原始标记（definition+time_or_place+overview + 六节正文，`一图`段计入、`svg` 标记不计入）。全库 **185 条**（`entries/*.json` 全部已写条目）逐条扫描，警戒线 **0.54**（与第27–34轮一致的内容层口径②）。
- **“两源互证”判定口径**：`TASK_design.md` 硬性规则要求“关键事实至少两个独立来源互相印证，否则标待核实”。本轮按“两源并集须覆盖 definition/time/overview 全部要点，且定义主干/核心论断至少获两源之一共同支撑”执行；若第二源与本条主题毫无内容交集（泛论伞源）或对本条任一具体论断均不构成印证，则该条核心事实实为**单源**或**无源**，按硬性规则判「待核实／不合格」。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。3 条共引用 **5 个来源 id（去重 5），全部存在、全部 verified=true**：

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| rockery | `wp-chinese-garden` | ✅ / true | Chinese garden / Wikipedia | 权威百科 | true | **直接**（假山石/太湖石/叠石成峰峦、选石标准） |
| rockery | `wp-garden-design` | ✅ / true | Garden design / Wikipedia | 权威百科 | true | 相关（明文 “A rock garden, also known as rockery…”） |
| sunken-garden | `wp-sunken-courtyard` | ✅ / true | Sunken courtyard / Wikipedia | 权威百科 | true | **直接（但正文为单句存根，见 §3.2）** |
| sunken-garden | `wp-garden-design` | ✅ / true | Garden design / Wikipedia | 权威百科 | true | **泛论伞源**（全文 `sunken`=0、`retaining`=0，无下沉内容） |
| material-color | `wp-color-theory` | ✅ / true | Color theory / Wikipedia | 权威百科 | true | 相关（光影响色彩、呈色与材料性质） |
| material-color | `wp-building-material` | ✅ / true | Building material / Wikipedia | 权威百科 | true | **泛论伞源**（全文 `color`/`colour`=0，无“材料色彩”内容） |

> 关键事实：三条 `sources` 数组长度与 `coverage.source_count` 一致（各 2=2）。5 源均 `year=null`（在线百科条目，D06 允许）、`link_ok=true`、`verified=true`。**无死链、无假 id、无 verified=false 被引用。**但 5 源中 `wp-sunken-courtyard` 为**单句存根**、`wp-garden-design`（对 sunken-garden）与 `wp-building-material`（对 material-color）为**泛论伞源**，详见 §三、§四。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 rockery（叠石）——**合格（Minor）**
- **wp-chinese-garden**（owiki 镜像 HTTP200 76820B，h1「Chinese garden」，正文 56741 字符）：
  - “A typical Chinese garden is enclosed by walls and includes one or more ponds, **rock works**, trees and flowers…”（假山石/叠石直证）
  - “twelve tall **limestone rocks** were added to the garden, **symbolizing mountains**. The most famous was a picturesque rock called the **Auspicious Cloud-Capped Peak**…”（**石叠成山、峰**直证）
  - “Liang Ji built an immense landscape garden with **artificial mountains, ravines** and forests”（**峦、壑**直证）
  - “rock was elevated to the status of an art object, **judged by its form, substance, color, and texture, as well as by its softness, transparency**, and other factors”（**选石/赏石标准**直证，对应“瘦、透、漏、皱”的改写）
  - “Bo Juyi wrote a catalog of the famous rocks of Lake Tai, called **Taihu Shiji**. These rocks, of **limestone sculpted by erosion**, became the most highly prized for gardens.”（**选石、太湖石、皱/蚀**直证）
  - “Rocks were solid but **water could wear away rock**. The **deeply eroded rocks** from Lake Tai used in the classical garden illustrated this principle.”（**结合水、蚀孔**佐证）
- **wp-garden-design**（owiki 镜像 HTTP200 45621B，h1「Garden design」）：
  - “A **rock garden, also known as rockery** or alpine garden, is a type of garden that **features extensive use of rocks and stones**, along with plants…”（**rockery＝叠石概念**的第二源佐证）
- **逐项结论**：
  - definition“以假山石堆叠模拟自然山峦”——“symbolizing mountains”“artificial mountains”**直接支撑**。
  - time_or_place“古代、中国”——Chinese garden 全篇讲中国古代园林（含 4th century BC、汉/唐/宋/明/清），**可接受**。
  - overview“以石形与堆法营造峰、峦、洞、壑”——**峰**(peak/Auspicious Cloud-Capped Peak)＋**峦**(mountains)＋**壑**(ravines)＋**洞**(deeply eroded/蚀孔) **均有支撑**。
  - 原理“依石的瘦、透、漏、皱选石”——源文“judged by its form, substance, color, and texture, as well as by its softness, transparency”为其**接近改写**（非逐字），不构成编造。
- **实例核对**：`实例`＝“名称：园林假山（**类型性描述**）；地点与设计者不适用。看石形与堆法如何造出峰壑。”**未点名具体作品、人名或年份 → 无编造风险**；`needs_verification=true`、`pending_notes` 与「待核实」三者逐字一致（均“具体实例待补充”）。
- **判定：合格**。附带 **Minor**：①“瘦、透、漏、皱”为对源文“form/substance/color/texture/softness/transparency”的改写（非逐字，属领域通识归纳，无编造）；②`rockery` 的 SVG 为极简示意（rect＋circle＋path），与「一图」解说“石峰与洞壑的堆叠”**仅部分对应**（只画了一个圆形石与一条曲线，未表现峰林/洞壑层叠）——属图—文部分脱节，非来源/编造缺陷。

### 3.2 sunken-garden（下沉花园）——**不合格（来源支撑失败）**
- **wp-sunken-courtyard**（owiki 镜像 HTTP200 10004B，h1「Sunken courtyard」）——**关键问题：正文为单句存根**：
  - 全文可提取正文仅一句：“In architecture and landscape architecture, a **sunken courtyard**, sometimes called a **sunken plaza**, is a **courtyard below ground level**.”（`textlen`≈1807 字符，其中绝大部分是 OWIKI 站点导航噪声）
  - 关键词实计：`sunken`=4（含导航）、`courtyard`=4、`below`=1、`ground`=1；**`drainage`=0、`retaining`=0、`moisture`=0、`plant`=0**。
- **wp-garden-design**（owiki 镜像 HTTP200 45621B）：
  - 关键词实计：**`sunken`=0、`retaining`=0、`damp`=0、`moisture`=0、`humidity`=0**；`drainage`=1（仅泛述“easier maintenance and drainage”指某类花园），**无任何下沉花园专属内容**。
- **逐项结论（对照所引来源）**：
  - definition“把绿化放到低于街道的地坪上，用高差围出一方安静绿岛”——仅“低于地坪”近似支撑（源 “below ground level”；“街道/安静绿岛/高差围合”为改写，Minor）。
  - time_or_place“20世纪、全球”——**无来源支撑**；且下沉庭院/下沉广场（含地坑院等）历史远早于 20 世纪，标“20世纪”缺乏依据、存疑。
  - overview“植物与水面调节温湿，挡土与排水是必须做好的构造”——**零支撑**（`plant`/`moisture`/`retaining` 两源合计均 = 0；`drainage` 仅 1 处泛述）。
  - 原理“下沉形成内聚空间，植物与水面调节温湿，挡土与排水是关键构造”——**零支撑**。
  - 典型手法“台阶/坡道连接地面，结合挡土墙、种植与排水组织”——**零支撑**（`retaining`=0，无台阶/坡道论述）。
  - 常见错误“排水与防潮不当会积水返潮”——**零支撑**（`damp`/`moisture`=0）。
  - 实例“城市下沉花园（**类型性描述**）；地点与设计者不适用。看高差、绿化与排水的组合。”——**类型性、无具名/年份 → 不编造** ✓。
- **判定：不合格（来源支撑失败）**。核心问题：所引“核心来源”`wp-sunken-courtyard` 在可达镜像中**只是单句词典式存根**，第二源为**无下沉内容的泛论花园设计**；本条除“低于地坪”外，overview／time_or_place／原理／典型手法／常见错误**全部无正文支撑**，属“正文超出所引来源、近乎凭通识硬写”，违反“每条事实有来源”“关键事实两源互证”硬性规则。**非编造人名/年份/引文**，属来源支撑与可核验性缺陷。另：`needs_verification`↔`pending`↔「待核实」虽**逐字一致**，但「待核实」只写“具体实例待补充”，**未披露“overview/原理/典型手法无源、主源为存根”这一真实缺口**。

### 3.3 material-color（材料色彩）——**待核实**
- **wp-color-theory**（owiki 镜像 HTTP200 36521B，h1「Color theory」，正文 23447 字符）：
  - “the appearance of a given colorant is **inherent to its chemical and physical properties**”（**“固有色”**近似支撑）
  - “color is **not intrinsic to objects**, but rather arises from the way an object reflects or absorbs different wavelengths”（色彩非物体固有；与“固有色”表述略有张力，但对“呈色依赖材料物理性质”有支撑）
  - “The **influence of light on color** was investigated…”（**光照影响色彩**直证）
  - 关键词实计：**`texture`=0、`material`=0、`surface`=0、`glossy`=0、`matte`=0、`rough`=0**。
- **wp-building-material**（owiki 镜像 HTTP200 45622B，h1「Building material」，正文 27788 字符）：
  - 导句“Building material is material used for construction. Many naturally occurring substances, such as clay, rocks, sand, wood…”；关键词实计：**`color`=0、`colour`=0、`texture`=0、`aesthetic`=0、`appearance`=0、`surface`=1**。**该文通论建筑材料，通篇不涉“颜色”，对本条“材料色彩”零具体支撑（泛论伞源）。**
- **逐项结论（对照所引来源）**：
  - definition“材料本身的固有色及其对空间氛围的影响”——“固有色”部分可由 `wp-color-theory` “inherent to its chemical and physical properties” 近似支撑；“对空间氛围的影响”**无支撑**。
  - time_or_place“跨时期、全球”——泛述，可接受。
  - overview“材料色与涂层色不同，受纹理与光照影响”——“**受光照影响**”✓（color theory）；“**纹理**”✗（两源 `texture`=0）；“**材料色与涂层色不同**”✗。**部分支撑**。
  - 原理“固有颜色与表面纹理共同决定其呈现色，粗糙面色彩更沉、光面更亮”——核心机制（纹理/粗糙面/光面）**两源均零命中**（`texture`/`rough`/`glossy`/`matte`=0）→ **无支撑**。
  - 典型手法“依空间基调选材色，以材质本色减少涂装、控制色差”——**无支撑**。
  - 实例“清水混凝土的灰色基调（**类型性描述**）；地点与设计者不适用。看材质本色如何定调。”——**类型性、无具名/年份 → 不编造** ✓。
- **判定：待核实**。定义主干（固有色≈材料性质）与 overview 的“光照影响”有主源支撑，**无编造**；但两源均为**泛论伞源**（color theory 通论色彩科学、building material 通论材料且不含“color”），未对“材料固有色/纹理—光泽机理/材料色≠涂层色”等具体论断构成互证，**核心机理实为无源**。建议补一条真正讨论“材料本色/表面质感与色彩”的权威来源（材料学/设计类），或把该缺口写入「待核实」并同步 `pending_notes`。附带 **Minor~Medium**：`material-color` 的 SVG 为两矩形（实心/空心各一），与解说“不同材料的固有色与质感”**仅示意两格**，未表现多种材质与质感差异，图文贴合度弱。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified**：5 个来源 id **全部存在、全部 verified=true**（见 §二表），`year=null`（D06 允许）、`link_ok=true`。
- **相关性**：
  - `wp-chinese-garden`（假山石/叠石/峰峦/选石）——**与 rockery 直接相关**，覆盖其全部要点；`wp-garden-design` 明文“rockery”定义——**相关**，构成第二源。→ rockery 两源均相关、互证成立。
  - `wp-sunken-courtyard`（标题直接，但正文仅“courtyard below ground level”一句）——主题标题相关但**无实体内容**；`wp-garden-design`（`sunken`=0、`retaining`=0）——**与 sunken-garden 非直接相关，属泛论伞源**。→ sunken-garden **无有效内容源**。
  - `wp-color-theory`（光/呈色/色彩感知）——与“色彩”相关但对“材料固有色”仅部分；`wp-building-material`（`color`=0）——**与“材料色彩”非直接相关，属泛论伞源**。→ material-color 两源均为半覆盖/伞源。
- **可达性（本轮实抓，全部 HTTP 200，经 owiki 同源镜像）**：`wp-chinese-garden`（76820B）/ `wp-garden-design`（45621B）/ `wp-sunken-courtyard`（10004B，正文存根）/ `wp-color-theory`（36521B）/ `wp-building-material`（45622B）。**5 个来源 id 全部可达，无死链。**（`en.wikipedia.org` 直连本轮超时、`web_fetch` fetch failed，均按 D05 走 owiki 镜像。）

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含“示意图，非施工图” | SVG 元素出界 | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rockery | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| sunken-garden | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |
| material-color | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 无出界 | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含“示意图，非施工图”；逐元素（rect/circle/line/polyline/polygon/text 坐标，programmatic 核验）**无出界**；「常见错误与限制」段均以规范提示收尾。**机械项三条全部通过。**
>
> **图示去同质化（相较第34轮显著改善）**：程序化比对，batch-35 **全 12 条 SVG 字符串两两互异（distinct=12/12），批内无逐字重复、全库亦无逐字重复**——第34轮“12 条仅 3 套模版、art-deco≡international-style 逐字同图”的问题**本轮已不复现**。但三者（及全批）均为**极简几何示意**（rect/circle/line/polyline），与各自解说的贴合度仍偏弱（见 §3.1/§3.3 的 Minors；sunken-garden 的 line+polyline 剖面亦未画排水/挡土构造），属后续**贴合度**整改项，非机械项判负。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**；`source_count` 与来源数组长度**一致**（各 2=2）；`needs_verification_count`：各 1/true；`related` 均为空数组（无悬空引用）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| rockery | true | 「叠石」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓ |
| sunken-garden | true | 「下沉花园」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓（但未覆盖“正文无源/主源存根”缺口） |
| material-color | true | 「材料色彩」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | （同左，逐字相同） | **完全一致** ✓（但未覆盖“纹理—光泽机理无源/伞源”缺口） |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 三条全部 True）。
> **注意**：三条的「待核实」都只声明“具体实例待补充”。对 `sunken-garden`（overview/原理/典型手法无源、主源为单句存根）与 `material-color`（纹理—光泽机理无源、第二源伞源）而言，**真实存在的来源支撑缺口未被写入待核实**——属“联动一致但内容不完整”，已分别在 §3.2 判不合格、§3.3 判待核实。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54；全库 185 条；口径②=全字段-不含 SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| rockery | **0.3725** vs cunfa | <0.54 ✓ | **0.4582** vs added-scenery | <0.54 ✓ |
| sunken-garden | **0.3611** vs semi-sunken-space | <0.54 ✓ | **0.4362** vs international-style | <0.54 ✓ |
| material-color | **0.4228** vs color-symbolism | <0.54 ✓ | **0.4686** vs structural-material | <0.54 ✓ |

> **三条两档全部 <0.54，无套话越线。** 最近邻多落在**同批 sibling 条目或近邻主题**（rockery→added-scenery、material-color→structural-material、sunken-garden→semi-sunken-space/international-style），反映本批条目仍偏高模板化（句式骨架高度相似：`definition=“X是…的…”`、`实例=“名称：…（类型性描述）；地点与设计者不适用。看…。”`、`待核实=“「X」的具体实例…待补充独立来源。”`），但**尚未越线**。
>
> **补充：batch-35 批内 12 条两两相似度**（口径②全字段）最高为 **added-scenery vs side-scenery＝0.4916**（short 0.4000），次高 material-color vs structural-material＝0.4686、added-scenery vs suppressed-scenery＝0.4631 等，均在 0.54 以下；即整批 new-entry 之间**无套话越线**，不触发 AUTONOMOUS §E“相似度过高→整批降级”。但 0.4916 亦近阈，与句架模板化一致，需关注。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **rockery（叠石）** | definition✓（symbolizing mountains/artificial mountains）；time✓（中国古代园林）；overview✓（峰 peak＋峦 mountains＋壑 ravines＋洞 eroded 石）；原理✓（选石=form/substance/texture/softness/transparency 改写）；实例＝类型性描述无具名/年份→不编造 | 2/2 true；两源均相关（chinese-garden 主证、garden-design 明文 rockery 佐证） | 七节齐、SVG✓（12条互异、极简几何但无重复）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致 | 0.373 / 0.458 | **合格**（Minor：瘦透漏皱为改写；SVG 与解说部分脱节） |
| **sunken-garden（下沉花园）** | definition 仅“低于地坪”近似支撑；**time_or_place“20世纪”无支撑且存疑**；**overview/原理/典型手法/常见错误 全部零支撑**（plant/moisture/retaining/damp=0）；实例＝类型性无具名/年份→不编造；**主源 wp-sunken-courtyard 为单句存根** | 2/2 true；wp-garden-design 非直接相关（伞源），wp-sunken-courtyard 标题相关但无实体内容 | 七节齐、SVG✓（无重复）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致（但未覆盖正文无源缺口） | 0.361 / 0.436 | **不合格**（来源支撑失败；非编造，属正文超出存根/伞源） |
| **material-color（材料色彩）** | definition“固有色”近似支撑、“空间氛围”无支撑；time 泛述可接受；overview 仅“光照”支撑、“纹理/材料色≠涂层色”无支撑；**原理“纹理—粗糙/光面”机理无支撑**；实例＝类型性无具名/年份→不编造 | 2/2 true；wp-color-theory 部分相关、**wp-building-material 泛论伞源（color=0）** | 七节齐、SVG✓（无重复、仅两格示意图文弱）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致（但未覆盖机理无源缺口） | 0.423 / 0.469 | **待核实**（两源伞源、核心机理无源；非编造，建议补真源或扩写待核实） |

- **内容与来源维度**：**1 合格 + 1 待核实 + 1 不合格 + 0 编造**。definition/time/overview 的支撑情况：rockery 全部有直接支撑；sunken-garden overview/time 及多节**无支撑**；material-color overview 部分、原理机理**无支撑**。三条实例均为**类型性描述**、无具名作品/作者/年份；**硬性“编造年份/人名/引文/出处”0 条、假 id 0 条、死链 0 条**。实质缺口在**来源支撑**：`wp-sunken-courtyard` 为单句存根、`wp-garden-design`/`wp-building-material` 为泛论伞源，故 sunken-garden 判不合格、material-color 判待核实。
- **结构与元数据维度**：三条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”且无出界、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 三条**逐字一致**；`check.py` PASS 0 errors。**图示去同质化较第34轮显著改善（12/12 互异，无逐字重复）**，但为极简几何示意，贴合度仍偏弱（需整改，非机械项判负）。
- **相似度维度**：三条两档全部 <0.54（短文本最大 0.4228、全字段最大 0.4686），批内两两最高 0.4916，亦 <0.54，**无套话异常**（但接近阈值，模板化偏高需关注）。

## 九、总体结论与是否建议整批返工

- **抽样结果**：3 条中 **1 条合格（rockery）+ 1 条待核实（material-color）+ 1 条不合格（sunken-garden）**；**内容/来源维度：0 编造、0 假 id、0 死链**。
- **来源层面**：5 个引用来源 id 全部存在、verified=true、均可达（owiki 200）；但 `wp-sunken-courtyard`（对 sunken-garden）为**单句存根**、`wp-garden-design`（对 sunken-garden）与 `wp-building-material`（对 material-color）为**泛论伞源**——这是本轮的核心实质缺陷：**sunken-garden 除“低于地坪”外全书无来源支撑 → 不合格**；**material-color 核心机理无源 → 待核实**。
- **结构/治理层面**：七节/SVG/规范提示机械项全过、元数据与 pending 联动三条**逐字一致**、`check.py` PASS 0 errors；**图示去同质化较第34轮显著改善（12/12 互异）**。
- **相似度层面**：三条两档全部 <0.54（最高全字段 0.4686），批内两两最高 0.4916，**无套话越线**（异常监控未触发，但接近阈值）。
- **是否建议整批返工**：**建议整批返工（整批降级为草稿并复查来源）**。依据：
  1. 按 `AUTONOMOUS.md` §E / `TASK_design.md` 批次复检的硬规则，**抽检出现 1 条不合格（sunken-garden 来源支撑失败）即触发“整批返工”**；本轮不合格 ≠ 编造，而是“正文大面积超出所引（存根/伞源）来源”，仍属来源核对不合格。
  2. **缺陷具有系统性风险、非孤立**：本批 12 条共用有限来源，`wp-sunken-courtyard`（存根）被 **3 条**下沉空间条目（sunken-garden、semi-sunken-space、sunken-atrium）引用；`wp-garden-design`（泛论花园设计，对下沉无内容）被 **8 条**引用；`wp-building-material`（不含 color）被 **2 条**材料条目引用。故“弱来源/伞源 + 正文超出来源”的病根很可能同样存在于未抽到的其余 9 条（尤其下沉空间 3 条、材料 2 条）。
- **必须的定向整改（与整批返工并行的最小修复）**：
  1. **sunken-garden（判不合格，必须重写来源与正文）**：现主源 `wp-sunken-courtyard` 为单句存根、第二源为无下沉内容的泛论花园设计。须补**真正含下沉庭院/下沉广场的排水、挡土、防潮、剖面构造**的权威来源（专业机构/建筑百科/规范解读类），据以重写 overview/原理/典型手法/常见错误；否则删除无源表述并把缺口写入「待核实」+`pending_notes`。`time_or_place` 的“20世纪”须据源更正（下沉庭院历史远早于 20 世纪）。
  2. **material-color（判待核实）**：`wp-building-material` 通篇不含“color”，`wp-color-theory` 不含“texture/材质”。须补一条讨论**材料本色与表面质感/色彩**的权威来源，或把“纹理—光泽机理、材料色≠涂层色”无源之实写入「待核实」并同步 `pending_notes`。
  3. **下沉空间 3 条 + 材料 2 条整批复核**：semi-sunken-space、sunken-atrium 同引存根 `wp-sunken-courtyard`；structural-material 同引 `wp-building-material`（不含 color）；需按同上标准复核来源是否支撑正文。
  4. **待核实披露口径统一（D14 精神）**：本批 12 条「待核实」目前一律只写“具体实例待补充”，无法反映真实的来源支撑缺口；建议对确有“伞源/无源”缺口的条目，把缺口如实写入「待核实」并同步 `pending_notes`，避免“联动一致但内容不完整”。
  5. **图示贴合度（Minor~Medium）**：12 条 SVG 已互异（去同质化达标），但仍为极简几何，需逐条贴合解说重绘（如 rockery 画峰林洞壑、sunken-garden 画排水/挡土剖面、material-color 画多种材质质感对比）。
- **流程记录**：本轮抽检 3/12＝25%（与 METRICS round34 `spotcheck_policy_next_round=25%` 一致）；结果 **1 合格 + 1 待核实 + 1 不合格、0 编造、0 假 id、0 死链、无套话越线**；**因出现 1 条不合格，按 §E 建议下一轮抽检比例维持/提高并对 batch-35 整批复核来源**。建议下轮对 batch-35 其余 9 条逐条做“来源正文是否支撑 definition/time/overview/实例”的定向复核，重点核查存根/伞源（`wp-sunken-courtyard`、`wp-garden-design`、`wp-building-material`、`wp-color-theory`、`wp-architecture`）在所列条目上的支撑力。

---

### 机器可读汇总

```
ROUND=35
SAMPLER=spotcheck-r35
SCOPE=["rockery","sunken-garden","material-color"]
FILES={"rockery":"entries/batch-35.json","sunken-garden":"entries/batch-35.json","material-color":"entries/batch-35.json"}
STATE={"sources.json":"120373B@23:47:23 (git-unmodified)","batch-35.json":"23133B@00:08:00","coverage.json":"83245B@00:07:52","add_round35.py":"11296B@00:07:45","total_written_entries":185,"scope_total":246,"written":185,"not_started":61,"files":23,"pending_total":159}
GIT_HEAD="c1ced74 feat: round34 twelve style-history entries"; GIT_STATUS="dirty: M coverage.json; ?? entries/batch-35.json; ?? tools/add_round35.py (round35 not yet committed)"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="3/12 = 25% (matches METRICS round34 spotcheck_policy_next_round=25%)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia TIMEOUT (web_fetch fetch failed) -> owiki.org mirror HTTP200; 5/5 distinct sources HTTP200; no temp files written"
FETCH={
 "wp-chinese-garden":"OWIKI 200 76820B h1 Chinese garden; 'rock works'; 'twelve tall limestone rocks ... symbolizing mountains'; 'Auspicious Cloud-Capped Peak'; 'artificial mountains, ravines'; 'judged by its form, substance, color, and texture, as well as by its softness, transparency'; 'Taihu Shiji ... limestone sculpted by erosion ... most highly prized'; 'deeply eroded rocks from Lake Tai'",
 "wp-garden-design":"OWIKI 200 45621B h1 Garden design; 'A rock garden, also known as rockery or alpine garden ... extensive use of rocks and stones'; KEY COUNTS: sunken=0, retaining=0, damp=0, moisture=0, humidity=0, drainage=1 (generic) -> no sunken content (UMBRELLA for sunken-garden)",
 "wp-sunken-courtyard":"OWIKI 200 10004B h1 Sunken courtyard; BODY IS A ONE-SENTENCE STUB: 'In architecture and landscape architecture, a sunken courtyard, sometimes called a sunken plaza, is a courtyard below ground level.' textlen~1807 (mostly nav). COUNTS: drainage=0, retaining=0, moisture=0, plant=0, below=1, ground=1 -> supports ONLY 'below ground level'",
 "wp-color-theory":"OWIKI 200 36521B h1 Color theory; 'appearance of a given colorant is inherent to its chemical and physical properties'; 'color is not intrinsic to objects, but rather arises from the way an object reflects or absorbs'; 'influence of light on color'; COUNTS: texture=0, material=0, surface=0, glossy=0, matte=0, rough=0",
 "wp-building-material":"OWIKI 200 45622B h1 Building material; 'Building material is material used for construction ... clay, rocks, sand, wood'; COUNTS: color=0, colour=0, texture=0, aesthetic=0, appearance=0, surface=1 -> NO color content (UMBRELLA for material-color)"
}
SOURCES={"count_distinct":5,"all_exist":true,"all_verified_true":true,"all_urls_reachable_200":"yes (owiki mirror)","relevance_defects":["wp-sunken-courtyard is a one-sentence stub (no body content)", "wp-garden-design is a generic umbrella with zero sunken content for sunken-garden", "wp-building-material is a generic umbrella with zero color content for material-color"]}
BODY_SUPPORT={
 "rockery":"definition/overview/原理/实例 supported by wp-chinese-garden (symbolizing mountains, peaks, ravines, eroded Taihu limestone, form/substance/texture/softness/transparency) + wp-garden-design ('rockery'); instance=type-description honest; VERDICT=合格 (Minor: 瘦透漏皱 paraphrase; SVG partial)",
 "sunken-garden":"definition only weakly ('below ground level'); time_or_place '20世纪' UNSUPPORTED (& doubtful); overview/原理/典型手法/常见错误 ZERO support (plant/moisture/retaining/damp=0 in both sources); primary source is a one-sentence stub; instance=type-description honest; NOT fabrication; VERDICT=不合格 (source-support failure)",
 "material-color":"definition '固有色' partial (inherent to chemical/physical properties), '空间氛围' unsupported; overview '光照' supported but '纹理/材料色≠涂层色' unsupported; 原理 texture/rough/glossy mechanism ZERO support in both sources; 2nd source wp-building-material has color=0; instance=type-description honest; NOT fabrication; VERDICT=待核实"
}
L2_CHECK={"seven_sections":"definition+6/6 x3, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, no overflow (programmatic)","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_dedup":"batch-35 12/12 SVG strings distinct (no verbatim duplicates intra-batch or vs library) -> round34 3-template issue NOT reproduced (improved); but all are minimal geometric diagrams, fit-to-caption weak"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x3","source_count":"2=2 x3","nvc":"1/true x3","needs_verification/pending_notes/待核实":"逐字一致 x3 (sunken-garden & material-color 待核实未覆盖真实来源缺口)","related":"[] (no dangling)"}
SIMILARITY={
 "rockery":{"short":0.3725,"vs_short":"cunfa","full_no_svg":0.4582,"vs_full":"added-scenery","verdict":"PASS<0.54"},
 "sunken-garden":{"short":0.3611,"vs_short":"semi-sunken-space","full_no_svg":0.4362,"vs_full":"international-style","verdict":"PASS<0.54"},
 "material-color":{"short":0.4228,"vs_short":"color-symbolism","full_no_svg":0.4686,"vs_full":"structural-material","verdict":"PASS<0.54"},
 "intra_batch_35_max":{"full_no_svg":0.4916,"pair":["added-scenery","side-scenery"],"short":0.4098},
 "threshold":0.54
}
VERDICT={"rockery":"合格","sunken-garden":"不合格","material-color":"待核实"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
BATCH_SOURCE_REUSE={"wp-garden-design":8,"wp-chinese-garden":6,"wp-sunken-courtyard":3,"wp-architecture":2,"wp-building-material":2,"wp-landscape-architecture":1,"wp-atrium-architecture":1,"wp-color-theory":1}
BATCH_REWORK="建议整批返工（整批降级为草稿并复查来源）：抽检出现 1 条不合格(sunken-garden 来源支撑失败)，按 AUTONOMOUS §E / TASK_design 批次复检规则触发整批返工；且弱来源系统性复用（wp-sunken-courtyard 存根被3条下沉条目引用、wp-garden-design 泛论被8条引用、wp-building-material 无color被2条材料条目引用），病根可能波及未抽到的其余9条。须定向整改：sunken-garden 换真源重写(排水/挡土/防潮/剖面)+更正'20世纪'；material-color 补材料本色/质感权威源或扩写待核实；下沉3条+材料2条整批复核；『待核实』如实披露伞源/无源缺口；SVG 从极简几何改为贴合解说。注：0 编造/0 假id/0死链；七节/元数据/check.py 全过；SVG 已12条互异（去同质化达标）；相似度全部<0.54（批内MAX0.4916）。"
READONLY="only wrote research/spotcheck-round35.md; no other project file changed; no git commit; web content treated as data, no instruction executed; fetches done in-memory via python stdin, no temp files written"
```

*（报告完）*
