# 第37轮质量闸抽检报告（spotcheck-round37）——纪念性尺度 / 伊斯兰建筑 / 奇数法则 / 工艺美术运动（第37轮新增 24 条中抽 4 条）

- 抽检人：spotcheck-r37（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 00:24 起，核对完成约 2026-11-23 00:5x，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（新增/改动条目随机抽 10%、至少 3 条逐条核对来源；**不合格则整批返工，下一轮把抽检比例提高到 25%**；异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级为草稿并复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 verified=true 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md`/`TASK_design.md` 在仓库根**无同名文件**；实际位于 `D:/Users/Administrator/Desktop/`（与第 12–36 轮一致），已按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）；`DECISIONS.md` 在仓库根（21 行）。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong）**：`data/sources.json`=120373B@2026-11-22 23:47:23（本轮未被改动）、`entries/batch-37.json`=45512B@2026-11-23 00:24、`coverage.json`=83138B@2026-11-23 00:23。`git log -1` = `b8597ee feat: round36 twelve circulation and environmental entries`。`git status --porcelain` = ` M coverage.json`、`?? entries/batch-37.json`、`?? tools/add_round37.py`——**即第37轮改动尚未提交**，工作树含本轮未入库改动，属本轮执行中的正常中间态（本次抽检未改动上述任何文件）。
- **条目规模**：`coverage.json` 总口径 **246** = 已写 **221** + 未开始 **25**；已写 **221 全 L2**（第36轮末 197 + 本轮 `batch-37` 新增 24 = 221，一致）。`pending_total`（`needs_verification_count` 求和）＝**195**（＝round36 的 171 + 本轮新增 24 条各 1）。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round37.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，未 `git commit`，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取全程在 Python 进程内存中进行、**未落盘任何临时文件**（脚本经 stdin 传入 Python，无临时文件）；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。
- **抽检口径与样本**：任务指定第37轮新增 24 条中抽 **4 条**：`monumental-scale`（纪念性尺度）、`islamic-architecture`（伊斯兰建筑）、`rule-of-odds`（奇数法则）、`arts-crafts`（工艺美术运动），均在 `entries/batch-37.json`；24 条全为 L2。本轮抽检比例 4/24≈**17%**（≥10% 下限）。引用来源共 **7 个去重 id**：`wp-proportion-architecture`、`wp-architecture`、`wp-islamic-architecture`、`wp-architectural-style`、`wp-composition-visual-arts`、`wp-rule-of-thirds`、`wp-history-of-architecture`（见 `data/sources.json`）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（本轮均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`，`Accept/Accept-Language` 齐备，`ssl` 不校验证书）。先试 `en.wikipedia.org` canonical，本轮**超时/失败**（与历史一致），改 **owiki 同源镜像** `https://owiki.org/wiki/<Title>` 核对标题与正文（DECISIONS D05 允许）。本轮 **4 条共 7 个引用来源全部实抓 HTTP 200**，无死链；h1 与 sources.json 标题逐条核对一致。
- **相似度口径**：`difflib.SequenceMatcher`（去空白）；①短文本＝title+definition+time_or_place+overview；②全字段-不含 SVG 原始标记（definition+time_or_place+overview + 六节正文，`一图`段计入、`svg` 标记不计入）。全库 **221 条**已写条目逐条扫描，警戒线 **0.54**（与第27–36轮一致的内容层口径②）。
- **“两源互证”判定口径**：`TASK_design.md` 硬性规则要求“关键事实至少两个独立来源互相印证，否则标待核实”。本轮按“两源并集须覆盖 definition/time/overview 全部要点，且定义主干/核心论断至少获两源之一直接支撑”执行；若第二源与本条主题毫无内容交集（泛论伞源/错配同类概念）或对本条任一具体论断均不构成印证，则相关具体论断实为**单源**或**无源**，据硬性规则影响判定。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。4 条共引用 **7 个去重来源 id（4×2=8 引用，去重 7），全部存在、全部 verified=true、全部 year=null（D06 允许）、全部 link_ok=true**。

| 条目 | sources（现状） | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| monumental-scale | `wp-proportion-architecture` | ✅ / true | Proportion (architecture) / Wikipedia | 权威百科 | true | **不相关**（讲数学比例/模数/Vitruvius；`monumental=0、scale=0、large=0、tall=0`，无“纪念性/崇高/权威/人在其中显小”内容） |
| monumental-scale | `wp-architecture` | ✅ / true | Architecture / Wikipedia | 权威百科 | true | **泛论伞源，仅一句沾边**（全文 `monumental`=1：“resorted to monumentality…to symbolically represent the political power of the ruler or the state”；`sublime=0、awe=0、authority=0、small=0`） |
| islamic-architecture | `wp-islamic-architecture` | ✅ / true | Islamic architecture / Wikipedia | 权威百科 | true | **直接**（dome=111、arch=274、courtyard=27、geometric=12、calligraphy=6、iwan=12、muqarnas=10，覆盖定义/概述/典型手法全部要点） |
| islamic-architecture | `wp-architectural-style` | ✅ / true | Architectural style / Wikipedia | 权威百科 | true | **泛论伞源**（讲“风格=建筑分类”，Islam/Crafts 均无；仅作背景，不涉本条具体论断） |
| rule-of-odds | `wp-composition-visual-arts` | ✅ / true | Composition (visual arts) / Wikipedia | 权威百科 | true | **直接**（明列“Rule of odds”专段：“an odd number of subjects in an image is more interesting than an even number”） |
| rule-of-odds | `wp-rule-of-thirds` | ✅ / true | Rule of thirds / Wikipedia | 权威百科 | true | **错配/不互证**（讲另一构图法则三分法；`odd=0、rule of odds=0`，对“奇数法则”零覆盖） |
| arts-crafts | `wp-architectural-style` | ✅ / true | Architectural style / Wikipedia | 权威百科 | true | **完全不相关**（全文 `Crafts=0、Morris=0、reform=0、medieval=0`，根本不提工艺美术运动） |
| arts-crafts | `wp-history-of-architecture` | ✅ / true | History of architecture / Wikipedia | 权威百科 | true | **泛论伞源，仅一次名称带过**（`Arts and Crafts`=1，且仅作 Art Nouveau 的影响来源列举，未述运动任何主张） |

> 关键事实：四条 `sources` 数组长度与 `coverage.source_count` 一致（各 2=2）。7 源均 `year=null`（在线百科，D06 允许）、`verified=true`、`link_ok=true`。**无死链、无假 id、无 verified=false 被引用。** 但 `wp-proportion-architecture`（对 monumental-scale）**不相关**、`wp-architecture`/`wp-architectural-style`/`wp-history-of-architecture` 为**泛论伞源**、`wp-rule-of-thirds`（对 rule-of-odds）为**错配同类概念**，详见 §三、§四。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 monumental-scale（纪念性尺度）——**待核实**
- **wp-proportion-architecture**（owiki HTTP200 18446B，h1「Proportion (architecture)」，textlen≈7916）：
  - 定义句：“Proportion is a central principle of architectural theory and an important connection between **mathematics and art**. It is the visual effect of the relationship of the various objects and spaces that make up a structure to one another and to the whole.”
  - 主题为**数学比例/模数（module）/Vitruvius/Alberti/Palladio**；关键词实计：**`monumental=0、scale=0、large=0、tall=0`**；`small`=2（均指八边形/三角形“smaller squares/triangles”的几何细分，非“人在其中显小”）；`grand`=2、`height`=6（教堂立面比例语境）。
  - 结论：**与本条主题不相关**，对“纪念性尺度/崇高/权威/人在其中显小”**零支撑**。
- **wp-architecture**（owiki HTTP200 52067B，h1「Architecture」，textlen≈31380）：
  - 唯一沾边句：“In many ancient civilizations…many ancient cultures **resorted to monumentality in their architecture to symbolically represent the political power of the ruler or the state itself.**”（`monumental`=1、`power`=3）
  - 关键词：**`sublime=0、awe=0、authority=0、human scale=0、small=0`**；`scale`=2 均为景观/城市设计“varying scales of design”语境，非纪念性人-构筑物尺度对比。
- **逐项结论（对照所引来源）**：
  - definition“以超大尺度营造崇高与权威感”——仅 `wp-architecture` 一句“monumentality…represent the political power”**部分支撑“权威感/political power”**；**“崇高（sublime）”✗（=0）、第二源全不相关** → 核心定义仅**单句、单源弱支撑**。
  - overview“放大构件与体量，使人在其中显得渺小”——**无源**（`small=0、human scale=0、sublime=0、awe=0`，两源均无“人显渺小”表述）。
  - 原理（＝definition+overview 逐字拼接）——同 definition/overview 缺口。
  - 典型手法“超常层高、巨柱与宽阔台阶”——**无直证**（proportion 源 `column`=2 讲古典柱式模数而非“巨柱”；architecture 源无层高/台阶内容）。
  - 常见错误“尺度失衡会压抑或空洞”——**无源**（属领域通识）。
- **实例核对**：`实例`＝“名称：纪念性大厅的超尺度柱廊（**类型性描述**）；地点与设计者不适用。人在其下显得渺小。”**类型性、无具名/年份 → 不编造** ✓（但“人在其下显得渺小”同 overview 无源点）。
- **判定：待核实**。核心问题：**第二源 `wp-proportion-architecture` 主题（数学比例）与本条无关、零命中；唯一主源 `wp-architecture` 仅一句“monumentality…political power”弱支撑“权威感”**，而“崇高”“使人在其中显得渺小”“巨柱/层高/宽阔台阶”“压抑/空洞”等均无源。属来源支撑缺陷（单句单源＋多节无源），**非编造人名/年份/引文**。

### 3.2 islamic-architecture（伊斯兰建筑）——**合格（Minor）**
- **wp-islamic-architecture**（owiki HTTP200 132973B，h1「Islamic architecture」，textlen≈95348）：
  - “Islamic architecture comprises the architectural **styles of buildings associated with Islam**. It encompasses both secular and religious styles from the early history of Islam to the present day.”
  - “Later it developed distinct characteristics…in the decoration of surfaces with Islamic **calligraphy, arabesques, and geometric motifs**. New architectural elements like **minarets, muqarnas, and multifoil arches** were invented.”（**几何装饰/书法/穆克纳斯**直证）
  - “**An iwan** is a hall that is walled on three sides and open on one side.”（**伊万**直证）；“the development of **muqarnas** from squinches”（穆克纳斯）
  - 关键词：`dome`=111、`arch`=274、`courtyard`=27、`geometric`=12、`calligraphy`=6、`iwan`=12、`muqarnas`=10、`medieval`=3、`7th century`=6。
- **wp-architectural-style**（owiki HTTP200 21723B，h1「Architectural style」，textlen≈10188）：
  - “An architectural style is a **classification of buildings** based on a set of characteristics…”——**泛论“风格概念”伞源**，`Crafts`=0、Islam 无专述，对本条仅作背景。
- **逐项结论**：
  - definition“以穹顶、拱廊、庭院与几何装饰为特征”——`dome/arch/courtyard/geometric` **直接、充分支撑**。
  - overview“用几何、书法与庭院组织宗教与世俗空间”——`geometric/calligraphy/courtyard`＋“secular and religious styles”**直接支撑**。
  - 原理/典型手法“伊万、穹顶、穆克纳斯与庭院”——`iwan（明确定义）/dome/muqarnas/courtyard` **直接支撑**。
  - time_or_place“中世纪、伊斯兰/南亚”——主源“early history of Islam to present”“7th century”＋`medieval`=3，**“中世纪”可接受**（早伊斯兰属中世纪；为概略化表述，Minor）。
  - 常见错误“装饰套用会失结构逻辑”——**通识性补充**（源未逐字，方向不冲突，Minor）。
- **两源互证**：核心概念由**直接主题源 `wp-islamic-architecture` 直证且极为充分**；`wp-architectural-style` 为泛论伞源仅作背景，未构成具体互证——但主源本身即本条主题权威源，核心内容不依赖伞源。
- **实例核对**：`实例`＝“名称：伊斯兰建筑的典型场景（类型性描述）；地点与设计者不适用。”**类型性、无具名/年份 → 不编造** ✓。
- **判定：合格（Minor）**。主源直接、强支撑定义/概述/典型手法；**Minor：第二源 `wp-architectural-style` 泛论伞源不作互证；“中世纪”为概略化时期标签；“装饰套用失结构逻辑”为通识补充**。非编造。

### 3.3 rule-of-odds（奇数法则）——**合格（Minor~Medium）**
- **wp-composition-visual-arts**（owiki HTTP200 25240B，h1「Composition (visual arts)」，textlen≈14845）：
  - 专段直证：“**Rule of odds** — The ‘rule of odds’ suggests that **an odd number of subjects in an image is more interesting than an even number.** Thus if you have more than one subject in your picture, the suggestion is to choose an arrangement…”（`rule of odds`=3、`odd`=4）
  - 相关句：“**Related to the rule of odds** is the observation that **triangles are an aesthetically pleasing implied shape** within an image.”
- **wp-rule-of-thirds**（owiki HTTP200 17102B，h1「Rule of thirds」，textlen≈7655）：
  - 全篇讲**三分法**（`rule of thirds`=10），关键词 **`odd`=0、`rule of odds`=0**——对“奇数法则”**零覆盖**，属**另一构图法则**，非互证来源。
- **逐项结论**：
  - definition“画面中主体数量取奇数更易形成生动均衡的构图经验”——`wp-composition-visual-arts` **直接、精确支撑**（“odd number…more interesting than an even number”）。
  - overview“奇数群体有中心与两侧，视觉更自然”——“more interesting / choose an arrangement…triangle implied shape”**方向支撑**，“中心与两侧”为合理推演（Minor）。
  - 典型手法“以三或五个主体组织，避免僵硬对称双数”——“odd vs even、triangles(≈3)”**支撑**。
  - 常见错误“机械套用会牵强”——**通识补充**（Minor）。
  - **两源互证**：核心概念仅由 `wp-composition-visual-arts` **单源直证**；`wp-rule-of-thirds` 讲的是**另一条法则（三分法）**，对本条不构成任何印证——**关键概念实为单源**，第二源**错配**（比第36轮 `wp-exit-sign` 的“窄口径伞源”更弱：连 facet 都不重叠）。
- **实例核对**：`实例`＝“名称：奇数法则的典型场景（类型性描述）；地点与设计者不适用。”**类型性、无具名/年份 → 不编造** ✓。
- **判定：合格（Minor~Medium）**。定义主干由**直接主题源 `wp-composition-visual-arts` 精确直证**（该源明列“rule of odds”专段），故核心不虚；**但第二源 `wp-rule-of-thirds` 系另一构图法则、零覆盖、不互证，关键概念实为单源**——若对“关键事实两源互证”从严执行，本条应记待核实。**非编造。**

### 3.4 arts-crafts（工艺美术运动）——**不合格**
- **wp-architectural-style**（owiki HTTP200 21723B，h1「Architectural style」，textlen≈10188）：
  - “An architectural style is a **classification of buildings** based on a set of characteristics and features…”——**纯泛论“建筑风格是什么”的伞源**。
  - 关键词实计：**`Crafts=0、Morris=0、reform=0、medieval=0`**——**全文根本不出现“工艺美术运动（Arts and Crafts）”，对运动零覆盖、零支撑**。
- **wp-history-of-architecture**（owiki HTTP200 128112B，h1「History of architecture」，textlen≈86546）：
  - 唯一提及（`Arts and Crafts`=1、`Crafts`=2）：“…the style was not completely new, since **Art Nouveau artists drew on a huge range of influences, particularly Beaux-Arts architecture, the Arts and Crafts movement, aestheticism and Japanese art.**”——仅作为 **Art Nouveau 的影响来源名称带过**，**未描述该运动任何主张**。
  - `Morris`=0、`reform`=2（与运动主张无关）、`handicraft`=1（指印度河流域文明“urban planning…and handicraft”）、`industrial`=2（泛讲工业革命/国际式，不涉该运动的“反工业”立场）；`19th century`=16、`20th century`=4——该运动在本文处于**19世纪语境**。
- **逐项结论（对照所引来源）**：
  - definition“回归手工艺、反对工业粗制、强调材料与工艺的诚实”——**无源**：`wp-architectural-style` 完全不提该运动；`wp-history-of-architecture` 仅名称带过，**未述“回归手工艺/反工业/材料工艺诚实”任何一条**。
  - overview“重视手作与装饰的整体性，影响后续设计”——仅“影响后续（Art Nouveau）”**一丝沾边**（作为影响来源被列举），“手作与装饰整体性”**无源**。
  - 原理（＝definition+overview 逐字拼接）——同定义/概述缺口。
  - 典型手法“手工、自然纹样与真实材料”——**无源**（两源均无“自然纹样/真实材料/手工”对本运动的描述）。
  - time_or_place“20世纪、欧洲”——**与所引来源矛盾/不符**：`wp-history-of-architecture` 将该运动置于**19世纪语境**描述（“popular during the 19th century…Art Nouveau…drew on…the Arts and Crafts movement”），而**工艺美术运动史实为 19 世纪后期运动（约 1860s–1910s，维多利亚时代反工业化）**，标“20世纪”为**时期误标**。
- **实例核对**：`实例`＝“名称：工艺美术运动的典型场景（类型性描述）；地点与设计者不适用。”**类型性、无具名/年份 → 不编造** ✓（但整条定义/原理/典型手法均无源）。
- **判定：不合格**。核心问题：**两源均为泛论伞源且互不印证**——`wp-architectural-style` 全文不含“Arts and Crafts”（对运动零覆盖），`wp-history-of-architecture` 仅一次作为 Art Nouveau 影响来源名称带过、**未支撑运动任何主张**；故 definition/原理/典型手法**实质无源**，且 **period“20世纪”与所引来源的19世纪语境矛盾、与史实不符（时期误标）**。**非编造具体人名/年份/引文**，但按 TASK_design「关键事实至少两源互证，否则待核实」及诚实性硬规则，本条同时存在“无源＋时期错误”，判**不合格**。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：7 个去重来源 id **全部存在、全部 verified=true、全部 link_ok=true**（见 §二表），`year=null`（D06 允许）。
- **可达性（本轮实抓）**：`wp-proportion-architecture`（owiki 200 18446B）/ `wp-architecture`（owiki 200 52067B）/ `wp-islamic-architecture`（owiki 200 132973B）/ `wp-architectural-style`（owiki 200 21723B）/ `wp-composition-visual-arts`（owiki 200 25240B）/ `wp-rule-of-thirds`（owiki 200 17102B）/ `wp-history-of-architecture`（owiki 200 128112B）。**7 个来源 id 全部可达，无死链。**（`en.wikipedia.org` 直连本轮超时，按 D05 走 owiki 镜像。）
- **相关性缺陷**：
  - `wp-proportion-architecture`（对 monumental-scale）——**不相关**：讲数学比例/模数，`monumental=0、scale=0、large=0`，对“纪念性/崇高/人在其中显小”零覆盖。
  - `wp-architecture`（对 monumental-scale）——**泛论伞源**：仅一句“monumentality…political power”，`sublime/awe/authority/small=0`。
  - `wp-islamic-architecture`（对 islamic-architecture）——**直接主题源，强支撑**。
  - `wp-architectural-style`（对 islamic-architecture / arts-crafts）——**泛论“风格概念”伞源**；对 arts-crafts 全文不含该运动（Crafts=0），对 islamic 仅背景。
  - `wp-composition-visual-arts`（对 rule-of-odds）——**直接主题源，含“rule of odds”专段**。
  - `wp-rule-of-thirds`（对 rule-of-odds）——**错配同类概念**：讲三分法，`odd=0/rule of odds=0`，零覆盖、不互证。
  - `wp-history-of-architecture`（对 arts-crafts）——**泛论伞源，仅一次名称带过**（作为 Art Nouveau 影响来源），未述运动主张。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | 缺节/多节 | SVG 数 | 含“示意图，非施工图” | viewBox | 风险/规范句 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| monumental-scale | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓“实际工程须按当地规范和专业设计人员的要求” |
| islamic-architecture | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |
| rule-of-odds | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |
| arts-crafts | L2 | ✓ | 6/6 | 无 | 1 | ✓ | 0 0 760 400 | ✓ |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、viewBox 均 `0 0 760 400`、均含“示意图，非施工图”；「常见错误与限制」段均以规范提示收尾（`check.py` 含 SVG 出界检查，本轮 PASS）。**机械项四条全部通过。**
>
> **⚠ 批次级系统缺陷（本轮首要质量问题，较第36轮进一步恶化）：**
> 1. **SVG 同质化达到极点：`batch-37` 全 24 条、去文字后仅 2 种互异几何模板（distinct geometry = 2/24）**——
>    - 模板 A（`<rect x=120 y=120 width=520 height=180>`＋一条竖中线 `<line>`）：被 **12 条**共用 = `east-west-color-compare / intimate-scale / node-path / eaves-space / interface-permeability / sustainable-design / constructivism / minimalism-architecture / vernacular-architecture / islamic-architecture / imperial-architecture / rule-of-odds`；
>    - 模板 B（一圆 `<circle r=110>`＋左右各一条水平 `<line>`）：被 **12 条**共用 = `monumental-scale / boundary / corridor-space / opening-interface / view-corridor / arts-crafts / high-tech / critical-regionalism / japanese-architecture / indian-architecture / religious-architecture / tints-shades`；
>    - 即 24 条全部是“空白矩形＋一条线”或“空白圆＋两条线”的**无内容占位图**，`text` 仅两句（标题＋“示意图，非施工图”）。例如 `monumental-scale` 的“超高柱廊与人的尺度对比”、`rule-of-odds` 的“奇数群体”、`islamic-architecture` 的“穹顶/拱廊/庭院”**在图上完全没有任何表现**——`一图` 解说文字与图形**系统性图文脱节**。这**直接违背** `TASK_design.md`“一图：用 SVG 自己绘制平面示意、剖面示意或动线与视线分析图，图中标注设计意图或尺寸关系”的实质要求。第34轮“3 套模板”、第36轮“3/12 套模板”问题在本轮**恶化为 2/24**。
> 2. **「原理」节近乎等于 definition+overview 逐字拼接（23/24 条命中）**：如 `monumental-scale` 原理 =“纪念性尺度指以超大尺度营造崇高与权威感的空间处理。它放大构件与体量，使人在其中显得渺小。”＝definition＋overview 原文拼接，**未提供任何独立机制/感受解释**（违反 L2「原理：为什么这样设计」的深度要求）。
> 3. **「实例」24/24 全为同一占位模板**：“名称：…的典型场景（类型性描述）；地点与设计者不适用。”——虽满足“类型性、不编造”，但**24 条零差异化、无任何具体元素描述**，实例节信息量为零。
> 综合：本批在**机械项（七节/示意图/规范句/元数据）全过**的表象下，**内容与图示高度模板化、近乎空壳**，属 §E“疑似套话→整批降级复查”的**典型形态**。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **四条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（monumental-scale：理论/重要/跨时期/全球/L2；islamic-architecture：风格/重要/中世纪/伊斯兰·南亚/L2；rule-of-odds：理论/补充/跨时期/全球/L2；arts-crafts：风格/重要/20世纪/欧洲/L2）；`source_count` 与来源数组长度**一致**（各 2=2）；`needs_verification_count`：各 1/true；`related` 均为空数组（无悬空引用）。
- **全批程序化核对（24 条）**：`needs_verification==true` 24/24；`pending_notes == sections.待核实` **逐字一致 24/24**；`coverage` 的 `source_count/needs_verification_count` 一致 24/24；`title/theme/tier/level/period/region` 一致 24/24。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| monumental-scale | true | 「纪念性尺度」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（但未披露“崇高/显小无源、第二源不相关”缺口） |
| islamic-architecture | true | 「伊斯兰建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓ |
| rule-of-odds | true | 「奇数法则」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（未披露“第二源错配不互证、实为单源”缺口） |
| arts-crafts | true | 「工艺美术运动」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **完全一致** ✓（未披露“两源伞源无支撑、20世纪时期误标”缺口） |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 四条全部 True；全批 24/24）。
> **注意（D14 精神）**：四条「待核实」均只声明“具体实例待补充”。对 monumental-scale（崇高/显小无源、第二源不相关）、rule-of-odds（第二源错配、实为单源）、arts-crafts（两源伞源无支撑、时期误标）而言，**真实存在的来源支撑缺口/时期错误未被写入待核实**——属“联动一致但内容不完整/失真”，已分别在 §3.1/§3.3/§3.4 判定。

## 七、任务 5：与既有条目相似度（difflib，阈值 0.54；全库 221 条；口径②=全字段-不含 SVG，`一图`计入）

| 条目 | ①短文本(标题+定义+时间+概述) | 判 | ②全字段-不含SVG | 判 |
| --- | --- | --- | --- | --- |
| monumental-scale | **0.4500** vs intimate-scale | <0.54 ✓ | **0.4928** vs intimate-scale | <0.54 ✓（近阈） |
| islamic-architecture | **0.4444** vs indian-architecture | <0.54 ✓ | **0.5057** vs high-tech | <0.54 ✓（近阈） |
| rule-of-odds | **0.4651** vs rule-of-thirds | <0.54 ✓ | **0.4879** vs view-corridor | <0.54 ✓ |
| arts-crafts | **0.4203** vs art-nouveau | <0.54 ✓ | **0.4817** vs high-tech | <0.54 ✓ |

> **四条两档全部 <0.54，无文本套话越线。** 最近邻多落在**同批 sibling 条目**（monumental-scale→intimate-scale、islamic→indian/high-tech、rule-of-odds→view-corridor/corridor-space、arts-crafts→high-tech/critical-regionalism），与同批高度模板化的句式骨架一致。
>
> **补充：batch-37 批内 24 条两两相似度**（口径②全字段）最高为 **high-tech vs critical-regionalism＝0.5160**（short 最高 imperial-architecture vs religious-architecture＝0.4630），**均 <0.54 但明显近阈**——结合 §五“24 条仅 2 套 SVG 几何、原理=定义+概述拼接 23/24、实例 24/24 同模板”，本批**图文模板化程度极高**：文本层未越线，**结构/图示层已实质同质化**，需重点处置。

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **monumental-scale（纪念性尺度）** | definition 仅 wp-architecture 一句“monumentality…political power”**单源弱支撑“权威感”**；“崇高”✗、overview“使人在其中显得渺小”✗、典型手法“巨柱/层高/台阶”✗、常见错误✗ 均无源；实例类型性无具名/年份→不编造 | 2/2 true；**wp-proportion-architecture 主题不相关（monumental/scale=0）、wp-architecture 泛论仅一句** | 七节齐、SVG✓（形式达标；但用模板 B 占位图，未画柱廊-人尺度对比）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致（未覆盖真实缺口） | 0.4500 / 0.4928 | **待核实**（第二源不相关、核心仅单句单源、多节无源；非编造） |
| **islamic-architecture（伊斯兰建筑）** | definition✓（dome/arch/courtyard/geometric）、overview✓（geometry/calligraphy/courtyard）、原理/典型手法✓（iwan/dome/muqarnas/courtyard）、time中世纪可接受；实例类型性无具名/年份→不编造 | 2/2 true；**主源 wp-islamic-architecture 直接强支撑**，wp-architectural-style 泛论伞源仅背景 | 七节齐、SVG✓（模板 A 占位图，未画穹顶/拱廊 Medium）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致 | 0.4444 / 0.5057 | **合格**（Minor：第二源伞源、中世纪概略、图示占位） |
| **rule-of-odds（奇数法则）** | definition✓（“odd number…more interesting than even”专段直证）、overview✓、典型手法✓；第二源 wp-rule-of-thirds 零覆盖不互证（实为单源）；实例类型性无具名/年份→不编造 | 2/2 true；**wp-composition-visual-arts 直接精确支撑**，wp-rule-of-thirds 错配同类概念 | 七节齐、SVG✓（模板 A 占位图，未画奇数群体 Medium）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致（未披露单源缺口） | 0.4651 / 0.4879 | **合格（Minor~Medium）**（第二源错配/实为单源） |
| **arts-crafts（工艺美术运动）** | definition/原理/典型手法**实质无源**（wp-architectural-style 全文不含该运动 Crafts=0；wp-history 仅1次名称带过、未述任何主张）；**period“20世纪”与所引来源19世纪语境矛盾、与史实不符（时期误标）**；实例类型性无具名/年份→不编造 | 2/2 true；**两源均泛论伞源、互不印证** | 七节齐、SVG✓（模板 B 占位图，完全未画运动特征）、风险✓ | 全部一致；nv=true/pending/待核实 逐字一致（未披露无源/时期误标） | 0.4203 / 0.4817 | **不合格**（两源伞源无支撑＋时期误标20世纪） |

- **内容与来源维度**：**2 合格（islamic-architecture、rule-of-odds）＋1 待核实（monumental-scale）＋1 不合格（arts-crafts）＋0 编造**。definition/time/overview 的支撑情况：islamic 主源直证充分；rule-of-odds 主源直证（但第二源错配、实为单源）；monumental-scale 第二源不相关、主源仅一句弱支撑“权威感”，“崇高/显小”无源；arts-crafts 两源均伞源无支撑且时期误标。四条实例均为**类型性描述**、无具名作品/作者/年份；**硬性“编造具体年份/人名/引文/出处”0 条、假 id 0 条、死链 0 条**。实质缺口在**来源支撑**（`wp-proportion-architecture` 不相关、`wp-architectural-style`/`wp-history-of-architecture` 泛论伞源、`wp-rule-of-thirds` 错配）与 **arts-crafts 时期误标**。
- **结构与元数据维度**：四条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 四条**逐字一致**；`check.py` PASS 0 errors。**但 SVG 24 条仅 2 套占位几何、原理=定义+概述拼接 23/24、实例 24/24 同模板——属批次级实质缺陷（形式机械项因“含示意图/不出界”而误过）。**
- **相似度维度**：四条两档全部 <0.54（短文本最大 0.4651、全字段最大 0.5057），批内两两最高 0.5160，**文本未越线但显著近阈**，与图示 2/24 模板共同反映极高模板化。

## 九、总体结论与是否建议整批返工

- **抽样结果**：4 条中 **2 条合格（islamic-architecture、rule-of-odds）＋1 条待核实（monumental-scale）＋1 条不合格（arts-crafts）**；**内容/来源维度：0 编造、0 假 id、0 死链**。
- **来源层面**：7 个引用来源 id 全部存在、verified=true、均可达（owiki 200）；但 `wp-proportion-architecture`（对 monumental-scale）**主题不相关**、`wp-architectural-style`/`wp-history-of-architecture`（对 arts-crafts）**泛论伞源且互不印证**、`wp-rule-of-thirds`（对 rule-of-odds）**错配同类概念**；`arts-crafts` 两源均伞源无支撑＋ **period“20世纪”与所引来源19世纪语境矛盾/史实不符** → **不合格**；`monumental-scale` 第二源不相关＋主源仅单句弱支撑 → **待核实**。
- **结构/治理层面**：七节/SVG/规范提示机械项全过、元数据与 pending 联动四条**逐字一致**、`check.py` PASS 0 errors；**但图示同质化较第36轮进一步恶化：`batch-37` 24 条仅 2 套占位 SVG 几何、图片与解说系统性脱节、原理=定义+概述逐字拼接 23/24、实例 24/24 同模板**——本批“形式达标、内容空壳”特征明显。
- **相似度层面**：四条两档全部 <0.54（最高全字段 0.5057 近阈），批内两两最高 0.5160（近阈），**文本无套话越线但结构层高度模板化**。
- **是否建议整批返工（结论）**：
  1. **§E 硬触发已成立**：本轮出现 **1 条不合格（arts-crafts）**——`TASK_design.md` / `AUTONOMOUS.md`「不合格则整批返工」硬规则**被触发**，**故明确建议 `batch-37` 整批返工**。arts-crafts 的问题不仅是“单源/待核实”，而是**两引用源均泛论伞源、对运动零实质支撑（`wp-architectural-style` 全文不含该运动），且 period“20世纪”与所引来源的19世纪语境及史实矛盾（时期误标）**——属可直接判定不合格的实质缺陷。
  2. **批次级系统缺陷（独立于上述不合格，亦支持整批处理）**：
     - **图示同质化至 2/24 套占位模板（首要）**：24 条全为“空白矩形一线/空白圆两线”无内容占位图，与各自 `一图` 解说**系统性脱节**，违背 TASK_design“用SVG绘制并标注设计意图”的实质要求；系第34轮“3套模板”、第36轮“3/12套模板”问题的**持续恶化（2/24）**，叠加批内文本相似度 0.5160 近阈，符合 §E“疑似套话→整批降级复查”的**精神与实体**。
     - **「原理」= definition+overview 逐字拼接（23/24）**、**「实例」24/24 同占位模板**：L2 内容深度不达标，属批量“骨架填充”而非真实 L2 写作。
  3. **定向返工/最小修复建议**：
     - **arts-crafts（判不合格）**：**整条重写**——补一条真正讨论“工艺美术运动（Arts and Crafts movement）”的权威来源（如 Art and Crafts 专条/William Morris 相关权威条目），据以重写定义/典型手法并落实“回归手工艺、反工业、材料与工艺诚实”的具体主张；**并把 period 由“20世纪”更正为“19世纪（19世纪后期）”，与来源及史实一致**。当前两伞源不可保留作互证。
     - **monumental-scale（判待核实）**：删去不相关源 `wp-proportion-architecture` 或改配一条讨论“纪念性/monumentality、崇高（sublime）、人-建筑尺度对比”的权威来源；对“使人在其中显得渺小/崇高”等待核实表述补源，否则从正文删除并如实写入「待核实」＋`pending_notes`。
     - **rule-of-odds（判合格 Minor~Medium）**：删去错配源 `wp-rule-of-thirds`，改配第二条讨论“rule of odds / 构图平衡”的来源以实现“两源互证”；否则在 `pending_notes`/「待核实」如实标注“关键概念实为单源、第二源错配”。
     - **islamic-architecture（判合格 Minor）**：保留；可将泛论源 `wp-architectural-style` 替换为一条更贴近“伊斯兰建筑”的第二主题源（可选），并把 `一图` 重绘为真实穹顶/拱廊/庭院平面示意。
     - **整批图示**：**全部 24 条 SVG 重绘为逐条贴合本条目解说的差异化示意图**（至少先重绘本报告 4 条：柱廊-人尺度对比、伊斯兰穹顶/拱廊/庭院平面、奇数群体构图、工艺美术运动纹样/材料示意），杜绝“空白矩形/圆＋线”占位图。
  4. **D14 披露口径统一**：本批 24 条「待核实」一律只写“具体实例待补充”，未反映真实来源缺口（arts-crafts 无源/时期误标、monumental-scale 第二源不相关、rule-of-odds 单源）；建议对确有“伞源/错配/无源/时期错误”的条目，把缺口如实写入「待核实」并同步 `pending_notes`。
- **流程记录**：本轮抽检 4/24≈17%（≥10% 下限）。结果 **2 合格 + 1 待核实 + 1 不合格、0 编造、0 假 id、0 死链、文本无套话越线**；**因 1 条不合格（arts-crafts：两伞源无支撑＋20世纪时期误标）触发“不合格即整批返工”硬规则，且存在批次级图示同质化恶化（2/24 套占位模板）与原理/实例模板化，明确建议 `batch-37` 整批返工、图示全面重绘、对 arts-crafts/monumental-scale/rule-of-odds 定向补源与纠错**。若按 §E“疑似套话→整批降级为草稿”执行，亦应整批降级复查。下轮建议对 `batch-37` 其余 20 条按“来源正文是否支撑 definition/time/overview/实例”定向复核，重点核查 `wp-architectural-style`、`wp-history-of-architecture`、`wp-architecture`、`wp-proportion-architecture` 等泛论伞源在各条上的支撑力与相似度近阈风险。

---

### 机器可读汇总

```
ROUND=37
SAMPLER=spotcheck-r37
SCOPE=["monumental-scale","islamic-architecture","rule-of-odds","arts-crafts"]
FILES={"monumental-scale":"entries/batch-37.json","islamic-architecture":"entries/batch-37.json","rule-of-odds":"entries/batch-37.json","arts-crafts":"entries/batch-37.json"}
STATE={"sources.json":"120373B@2026-11-22 23:47:23 (unchanged this round)","batch-37.json":"45512B@2026-11-23 00:24","coverage.json":"83138B@2026-11-23 00:23","total_written_entries":221,"scope_total":246,"written":221,"not_started":25,"pending_total":195,"batch37_count":24}
GIT_HEAD="b8597ee feat: round36 twelve circulation and environmental entries"; GIT_STATUS="dirty: M coverage.json; ?? entries/batch-37.json; ?? tools/add_round37.py (round37 not yet committed)"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="4/24 = ~17% (>=10% floor)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia TIMEOUT -> owiki.org mirror HTTP200 (7/7 wiki pages reachable); no temp files written"
FETCH={
 "wp-proportion-architecture":"OWIKI 200 18446B h1=Proportion (architecture) textlen~7916; 'Proportion is a central principle of architectural theory...mathematics and art'; COUNTS: monumental=0,scale=0,large=0,tall=0,small=2(geometry),grand=2,height=6 -> IRRELEVANT to monumental-scale",
 "wp-architecture":"OWIKI 200 52067B h1=Architecture textlen~31380; 'many ancient cultures resorted to monumentality...to symbolically represent the political power of the ruler or the state'; monumental=1,power=3,sublime=0,awe=0,authority=0,small=0 -> single umbrella sentence only",
 "wp-islamic-architecture":"OWIKI 200 132973B h1=Islamic architecture textlen~95348; dome=111,arch=274,courtyard=27,geometric=12,calligraphy=6,iwan=12(iwan defined),muqarnas=10,medieval=3,7th century=6 -> DIRECT strong support",
 "wp-architectural-style":"OWIKI 200 21723B h1=Architectural style textlen~10188; 'An architectural style is a classification of buildings...'; Crafts=0,Morris=0,reform=0,medieval=0 -> GENERIC umbrella; does NOT mention Arts and Crafts",
 "wp-composition-visual-arts":"OWIKI 200 25240B h1=Composition (visual arts) textlen~14845; 'Rule of odds: an odd number of subjects in an image is more interesting than an even number'; rule of odds=3,odd=4 -> DIRECT exact support for rule-of-odds",
 "wp-rule-of-thirds":"OWIKI 200 17102B h1=Rule of thirds textlen~7655; rule of thirds=10,odd=0,rule of odds=0 -> MISMATCH (different rule), no coverage",
 "wp-history-of-architecture":"OWIKI 200 128112B h1=History of architecture textlen~86546; Arts and Crafts=1 ONLY as Art Nouveau influence ('...Art Nouveau artists drew on...the Arts and Crafts movement...'); Crafts=2,Morris=0,handicraft=1(Indus),industrial=2(general); 19th century=16,20th century=4 -> GENERIC umbrella, passing name-drop only"
}
SOURCES={"count_distinct":7,"all_exist":true,"all_verified_true":true,"all_urls_reachable_200":"yes (7 owiki)","relevance_defects":["wp-proportion-architecture IRRELEVANT to monumental-scale (monumental/scale=0)","wp-architecture single umbrella sentence for monumental-scale (political power only; sublime/awe/small=0)","wp-architectural-style generic umbrella, does NOT mention Arts and Crafts (Crafts=0) for arts-crafts","wp-history-of-architecture only 1 passing name-drop of Arts and Crafts, no tenets -> arts-crafts","wp-rule-of-thirds MISMATCH (rule of thirds, odd=0) for rule-of-odds","wp-architectural-style generic umbrella (background only) for islamic-architecture"]}
BODY_SUPPORT={
 "monumental-scale":"definition core only single-sentence/single-source weak support ('monumentality...political power'); 'sublime/awe/使显渺小' UNSUPPORTED (sublime=0,awe=0,small=0); 2nd source IRRELEVANT; 典型手法(巨柱/层高/台阶) & 常见错误 no source; instance=type-description honest; NOT fabrication; VERDICT=待核实",
 "islamic-architecture":"definition/overview/原理/典型手法 all DIRECTLY supported by wp-islamic-architecture (dome/arch/courtyard/geometric/calligraphy/iwan/muqarnas); time 中世纪 acceptable; 2nd source generic umbrella background only; instance=type-description honest; VERDICT=合格 (Minor)",
 "rule-of-odds":"definition DIRECTLY & exactly supported by wp-composition-visual-arts ('rule of odds' dedicated paragraph); 2nd source wp-rule-of-thirds is a DIFFERENT rule (odd=0) not co-verifying -> concept effectively single-source; instance=type-description honest; VERDICT=合格 (Minor~Medium)",
 "arts-crafts":"definition/原理/典型手法 ESSENTIALLY UNSUPPORTED: wp-architectural-style does NOT mention Arts and Crafts at all (Crafts=0); wp-history-of-architecture 1 passing name-drop as Art Nouveau influence, describes NO tenet; period '20世纪' CONTRADICTS source's 19th-century context & historical fact (Arts and Crafts is late-19th-century); instance=type-description honest; NOT fabricated year/name/quote; VERDICT=不合格"
}
L2_CHECK={"seven_sections":"definition+6/6 x4, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, no overflow (check.py PASS)","risk_note":"实际工程须按当地规范和专业设计人员的要求 x4","batch_template_defects":"24 entries ONLY 2 distinct SVG geometries (templateA rect+line x12; templateB circle+2lines x12) - content-free placeholder figures, systematic figure-caption disconnect; 原理==definition+overview verbatim concat 23/24; 实例 template 24/24; 一图 NOT drawn per TASK_design"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x4 (vs coverage.json)","source_count":"2=2 x4 (batch 24/24)","nvc":"1/true x4","needs_verification/pending_notes/待核实":"verbatim-identical x4 (batch 24/24; arts-crafts/monumental/rule-of-odds 待核实 NOT disclosing real gaps)","related":"[] (no dangling)"}
SIMILARITY={
 "monumental-scale":{"short":0.4500,"vs_short":"intimate-scale","full_no_svg":0.4928,"vs_full":"intimate-scale","verdict":"PASS<0.54 (near threshold)"},
 "islamic-architecture":{"short":0.4444,"vs_short":"indian-architecture","full_no_svg":0.5057,"vs_full":"high-tech","verdict":"PASS<0.54 (near threshold)"},
 "rule-of-odds":{"short":0.4651,"vs_short":"rule-of-thirds","full_no_svg":0.4879,"vs_full":"view-corridor","verdict":"PASS<0.54"},
 "arts-crafts":{"short":0.4203,"vs_short":"art-nouveau","full_no_svg":0.4817,"vs_full":"high-tech","verdict":"PASS<0.54"},
 "intra_batch_37_max":{"full_no_svg":0.5160,"pair":["high-tech","critical-regionalism"],"short":0.4630},
 "threshold":0.54
}
VERDICT={"monumental-scale":"待核实","islamic-architecture":"合格","rule-of-odds":"合格","arts-crafts":"不合格"}
VERDICT_SEVERITY={"monumental-scale":"待核实(第二源不相关+核心仅单句单源+多节无源)","islamic-architecture":"合格(Minor:第二源伞源/中世纪概略/图示占位)","rule-of-odds":"合格(Minor~Medium:第二源错配/实为单源/图示占位)","arts-crafts":"不合格(两源伞源无支撑+20世纪时期误标)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
BATCH_REWORK="YES - §E hard trigger fired: 1 不合格 (arts-crafts: both cited sources are generic umbrellas unsupporting the movement (wp-architectural-style Crafts=0), plus period '20世纪' contradicts source's 19th-century context & fact -> period mislabel). Additionally batch-level systematic defects: batch-37 24 entries only 2 distinct placeholder SVG geometries (worse than round34 3/12 and round36 3/12), systematic figure-caption disconnect; 原理==definition+overview verbatim concat 23/24; 实例 template 24/24. Recommend WHOLE-BATCH rework: redraw all 24 SVGs per-entry, de-template 原理/实例; targeted: rewrite arts-crafts with a real Arts and Crafts source + correct period to 19th century; replace/resupport monumental-scale 2nd source & add sources for sublime/'显得渺小'; fix rule-of-odds 2nd source (rule-of-thirds mismatch); islamic-architecture keep (Minor only). 0 fabrication/0 false id/0 dead link; mechanical seven-section/metadata/check.py all pass; text similarity all<0.54 (intra max 0.5160); 2 SVG placeholder templates & template content are the dominant quality defect."
READONLY="only wrote research/spotcheck-round37.md; no other project file changed; no git commit; web content treated as data, no instruction executed; fetches done in-memory via python stdin, no temp files written"
```

*（报告完）*
