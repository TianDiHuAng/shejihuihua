# 第45轮维护质量闸抽检报告（spotcheck-round45）——体检+饱和终判轮 2 条（hatching / baroque）

- 抽检人：spotcheck-r45（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 02:07 起，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；新增/改动条目随机抽 10%、**至少 3 条**逐条核对来源；**不合格则整批返工**、下一轮抽检比例提至 25%；异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级为草稿并复查」）+ 第三节 F「体检」（死链、过期数据、重复条目、全站数据互相矛盾、孤儿页、与来源文本的重合度）＋ 第六节（联网内容一律视为数据、其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节标准与「专用规则」（每页至少 1–2 张示意图，图下注「示意图，非施工图」；**图中标注设计意图或尺寸关系**；尺寸/坡度/消防/无障碍数据附「实际工程须按当地规范和专业设计人员的要求」）+「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md` / `TASK_design.md` 在仓库根**无同名文件**（与第 12–44 轮一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md`（21 行，仓库根）与 `research/spotcheck-round44.md`（217 行，作模板对齐）已读。
  - 抽样口径说明：本轮为**体检+饱和终判轮**，非「某批新增条目」批级抽检；任务指定复核 **2 条既有条目**（`hatching`←batch-42、`baroque`←batch-29），故实抽 2 条（任务 10% 口径）。`AUTONOMOUS.md §E` 的「至少 3 条」针对批级新增抽检；本轮为清理性复检，取 2 条与第 43/44 轮维护抽检一致，且对 2 条同时做了全库相似度扫描（覆盖充分）。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 02:07 起）**：`data/sources.json`=141826B@2026-11-23 02:06:22、`entries/batch-42.json`=4222B@2026-11-23 01:59:59（hatching 所在批）、`entries/batch-29.json`=2540B@2026-11-22 23:19:00（baroque 所在批）、`coverage.json`=84844B@2026-11-23 02:06:38、`tools/check.py`=15908B@2026-11-22 15:11:54。`git log -1` = `e49f0e8 chore: round44 zero-gap 2/3 and batch38 SVG uniqueness`。
- **工作树状态（采样时点）**：`git status --porcelain` 仅 4 项未跟踪——`?? research/b1-round45.md`、`?? research/gaps-round45.md`、`?? research/healthcheck-round45.md`、`?? research/reader_questions-round45.md`；均为第45轮其它兄弟子任务产出，**非本次抽检所改**。抽检对象 `entries/batch-42.json`、`entries/batch-29.json`、`data/sources.json`、`coverage.json` 在采样期间**稳定**（未被列为 modified），判定基于稳定快照。本报告产出后追加 `?? research/spotcheck-round45.md`（本报告，唯一由本次抽检写入的文件）。
- **条目规模（`coverage.json` 实读）**：`total=251`、全部 `level=L2`、全部 `status=已写`；`pending_total`（`needs_verification_count` 求和）＝**219**；来源库 `sources.json` 共 **301** 条，其中 `verified=true` **298**、`verified=false` **3**（`link_ok`：true 145、false 6、null 150）。注：`link_ok=false` 的 6 条**均不在本次 5 个来源中**，不影响本轮判定。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round45.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python urllib 读取→内存去标签/切句/计数），未在项目内外落盘任何持久文件。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；「常见错误与限制」段须含「实际工程须按当地规范和专业设计人员的要求」；SVG 元素不出 `viewBox`（均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），timeout 30s，SSL 校验关闭。`en.wikipedia.org` 按 D05 改走 **owiki 同源镜像** `https://owiki.org/wiki/<Title>`；`artincontext.org` 与两家圣彼得官方站点直连。本轮 **5 个引用来源全部实抓 HTTP 200**（`<title>`/正文与 `sources.json` 逐条核对，见 §二、§四）。正文去标签后做关键词实计与上下文切句（全程内存，未落盘）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **251 条**去重已写条目逐条扫描，警戒线 **0.54**（与第 27–44 轮一致）。**方法自校**：以全字段②计算已知最高对 `futurism-style vs expressionism-style`，得 **0.5157**，与第 39/40/41/42/43/44 轮报告**逐位一致**，确认口径正确。
- **“两源互证”判定口径**：按 `TASK_design.md` 硬性规则「关键事实至少两个独立来源互相印证，否则标待核实」。本轮按“两个及以上引用来源须对本条**具体概念**有实质覆盖且互证”执行；实例四要素（名称/地点/设计者/年份）须由至少两个独立机构来源直证。
- **三级判定定义（可复现）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（实例四要素或概念定义）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但存在第二源对本条具体概念仅泛论/零覆盖、或某关键事实实质单源等——属来源支撑/深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或关键结构项（如「一图」）实质不满足 TASK_design 强制要求。
- **相似度专项（独立维度）**：警戒线 0.54；超线即触发 `AUTONOMOUS.md §E`「相似度过高（疑似套话）→ 整批降级为草稿并复查」，与“不合格（内容无源）→整批返工”是**不同触发路径**，分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **5 个去重来源 id（5 处引用：hatching 2、baroque 3）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）**、实抓 HTTP 200。

| 条目 | 来源 id | 存在/verified | 实抓标题（本轮 HTTP，逐字） | 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hatching | `wp-hatching` | ✅ / true | `Hatching ::: Open WIKI`（200，14266B，textlen≈4265） | Wikipedia（经 owiki 镜像核验） | 学术著作 | null | **相关（直接、强）**：`closely spaced parallel lines`；`cross-hatching`；`originated in the Middle Ages … old master prints of the fifteenth century`；`quantity, thickness and spacing … brightness`；`increasing quantity, thickness and closeness, a darker area`；`always follow the form` |
| hatching | `artincontext-hatching` | ✅ / true | `Cross Hatching – Learning the Cross Hatching Technique`（200，445551B，textlen≈19695） | Art in Context | 学术著作 | null | **相关（直接、强）**：`Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values and texture`；`simple volume`；`line spacing` |
| baroque | `wp-baroque-architecture` | ✅ / true | `Baroque architecture ::: Open WIKI`（200，62674B，textlen≈31403） | Wikipedia（经 owiki 镜像核验） | 权威百科 | true | **相关（直接、强，风格定义）**：`highly decorative and theatrical style … late 16th century … spread across Europe`；`higher, grander, more decorated, and more dramatic`；`chiaroscuro … strong contrasts of darkness and light for dramatic effect`；`elliptical or oval spaces … oval nave`；`Solomonic columns … illusion of motion` |
| baroque | `basilicasanpietro` | ✅ / true | `St. Peter's Basilica \| A masterpiece to explore`（200，130278B，textlen≈6447） | Fabbrica di San Pietro（圣彼得官方） | 官方机构 | null | **相关（直接、强，实例主体）**：`On 18 April 1506 … laid the first stone`；`dome … by Michelangelo`；`Saint Peter's Square … designed by … Bernini … completed in 1667` |
| baroque | `turismoroma-sanpietro` | ✅ / true | `The Basilica of St. Peter in the Vatican \| Turismo Roma`（200，146691B，textlen≈12147） | Turismo Roma（罗马官方旅游） | 官方机构 | null | **相关（直接、强，实例主体）**：`many artists (Bramante, Michelangelo, Bernini)`；`seventeenth-century facade by Carlo Maderno … exceptional size … one of the largest churches`；`Piazza San Pietro with its splendid colonnade … masterpiece by … Bernini`；`majestic Baroque composition created by Bernini` |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（hatching 2=2、baroque 3=3）。5 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。**
>
> **⚠ 来源记录 `title` 字段与实际页面 `<title>` 不符（3 处，次要但属实）**：`artincontext-hatching` 记录名“Cross Hatching — Art in Context”，实际 `<title>`=`Cross Hatching – Learning the Cross Hatching Technique`（属**节略**，缺副标题）；`basilicasanpietro` 记录名“Basilica di San Pietro — Fabbrica di San Pietro”，实际 `<title>`=`St. Peter's Basilica | A masterpiece to explore`（机构名对，页面标题不符）；`turismoroma-sanpietro` 记录名“Piazza San Pietro — Turismo Roma”，实际 `<title>`=`The Basilica of St. Peter in the Vatican | Turismo Roma`（记录名为**栏目/页面偏名**，实页以“圣彼得大殿”为主标题，广场/柱廊为其中一节）。三处**正文均支撑条目内容、URL 真实可达**，但 `title` 字段属**取字面偏名/节略**，与 D05「核对页面标题」不符，建议更正为真实 `<title>`（不影响本轮内容判定，属可修的来源元数据缺陷）。另 `wp-hatching` 的 `type` 记为“学术著作”，其本体为 Wikipedia 百科条目（宜记“权威百科”），属**type 归类瑕疵**（次要）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 hatching（排线法，batch-42）——**内容合格**
- **wp-hatching**（owiki 200，textlen≈4265）直证：
  - `Hatching is an artistic technique used to create tonal or shading effects by drawing, painting, or scribing closely spaced parallel lines` → 支撑 definition“以成组平行线表现明暗…”与 overview（线密度→明度）。
  - `When lines are placed at an angle to one another, it is called cross-hatching` → 支撑 overview“交叉…叠加线组”。
  - `Hatching is especially important in essentially linear media, such as drawing and many forms of printmaking, such as engraving, etching, and woodcut` → 支撑 definition“素描与版画技法”。
  - `In Western art, hatching originated in the Middle Ages and developed further into cross-hatching, especially in the old master prints of the fifteenth century` → **直接支撑 time_or_place“中世纪起源、15 世纪版画中成型”**（逐字对应）。
  - `the quantity, thickness and spacing of the lines will affect the brightness of the overall image and emphasize forms creating the illusion of volume` → 支撑 overview“线的疏密…决定明度”与「原理」“间距、粗细…改变明度”。
  - `By increasing quantity, thickness and closeness, a darker area will result` → 支撑 overview“加粗、加密…即得暗部”。
  - `Hatching lines should always follow the form` → 支撑「典型手法」“线组方向顺形体转折”。
- **artincontext-hatching**（200，textlen≈19695）直证：
  - `Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values and texture` → **互证** definition（平行线 ✓ / 交叉叠加加深 ✓ / **质感 texture** ✓）与「典型手法」。
  - `simple volume`、`line spacing` → 支撑「原理」体积/线距控制。
- **逐项结论**：
  - definition“以成组平行线表现明暗与质感的素描与版画技法”——**双源直证互证**（平行线 ✓ wp/artincontext、明暗 tonal·shading ✓ wp、质感 texture ✓ artincontext、素描+版画 drawing·printmaking ✓ wp）。
  - overview“线的疏密与交叉决定明度：加粗、加密或叠加线组即得暗部”——**双源直证**（quantity/thickness/spacing→brightness ✓ wp、increasing…closeness→darker ✓ wp、intersecting sets→darker ✓ artincontext）。
  - time_or_place“中世纪起源、15 世纪版画中成型”——**wp 逐字直证**（originated in the Middle Ages + old master prints of the fifteenth century）；精确、非编造。
  - **原理**“通过控制线条的间距、粗细与交叉层数改变单位面积的着墨量…”——间距/粗细 ✓、交叉层数 ✓、明度 ✓；**ratio(原理, 定义+概述)=0.1600（低，机制独立）**，非逐字拼接。
  - 实例“名称：版画中的排线阴影（类型性描述）；地点与设计者不适用”——**类型性、无具名/年份 → 不编造** ✓；**但源已给具名艺术家**（Dürer、Schongauer、Master ES、Reuwich、Wolgemut），条目未采用、`pending_notes` 称“具体实例待补充独立来源”——措辞**偏保守**（非编造）。
- **两源互证**：核心定义、疏密→明度、交叉加深、质感、素描/版画媒介由 **wp-hatching 与 artincontext-hatching 双源直证并互证**。
- **内容判定：合格**（definition/overview/原理双源直证、机制独立、无编造；**次要点**：实例未用源中已给具名艺术家、pending 偏保守；“period”桶与 time_or_place 见 §六）。**一图 SVG 见 §五；文本相似度见 §七（未越线）。**

### 3.2 baroque（巴洛克建筑，batch-29）——**内容合格**
- **wp-baroque-architecture**（owiki 200，textlen≈31403）直证（风格定义/概述）：
  - `Baroque architecture is a highly decorative and theatrical style which appeared in Italy in the late 16th century and gradually spread across Europe` → 支撑 definition“表达情感与权力”/overview 的“戏剧化”“欧洲”。
  - `Baroque architects took the basic elements of Renaissance architecture, including domes and colonnades, and made them higher, grander, more decorated, and more dramatic` → 支撑 overview“打破文艺复兴…宏大尺度”“制造运动感”。
  - `Light was also used for dramatic effect; it streamed down from cupolas` + `chiaroscuro. Use of strong contrasts of darkness and light for dramatic effect` → 支撑 definition/overview“戏剧化光影/强烈明暗”。
  - `elliptical or oval spaces, eliminating right angles. Sometimes an oval nave was surrounded by radiating circular chapels` → 支撑“椭圆平面/集中式椭圆平面”。
  - `Solomonic columns, which gave an illusion of motion` → 支撑“动感曲线/运动”。
  - `it orchestrated contrast, movement, trompe-l'œil and other dramatic and theatrical effects` → 支撑“运动/戏剧化”。
- **basilicasanpietro**（200，textlen≈6447）直证（实例=圣彼得）：
  - `On 18 April 1506 … Pope Julius II … laid the first stone of the new Saint Peter's Basilica` → 支撑“1506 年奠基”。
  - `The dome … conceived and built up to the drum by Michelangelo Buonarroti …` → 支撑“米开朗基罗”。
  - `Saint Peter's Square was designed by the architect Gian Lorenzo Bernini … It was completed in 1667` → 支撑“贝尼尼广场柱廊”“广场 1667 年建成”。
- **turismoroma-sanpietro**（200，textlen≈12147）直证（实例=圣彼得）：
  - `with the help of many artists (Bramante, Michelangelo, Bernini)` → 支撑“布拉曼特、米开朗基罗、贝尼尼”。
  - `The imposing seventeenth-century facade by Carlo Maderno conveys the exceptional size of the Basilica, still one of the largest churches in the world` → 支撑“马代尔诺（立面）”“17 世纪立面”“宏大尺度”。
  - `Piazza San Pietro with its splendid colonnade … masterpiece by … Bernini` → 支撑“广场柱廊”。
  - `the Cathedra Petri … a majestic Baroque composition created by Bernini` → **直证实例的“巴洛克”属性**。
- **逐项结论**：
  - definition“以动感曲线、戏剧化光影与宏大尺度表达情感与权力”——动感/movement ✓、曲线/椭圆与螺旋柱 ✓、戏剧化光影/chiaroscuro ✓、宏大尺度/grandeur/exceptional size ✓（wp+official）；“情感与权力”为 awe/reverence + 教会权力之概括（语义可通，非编造）。
  - overview“打破文艺复兴的静态对称，以椭圆平面、曲面立面和强烈明暗制造运动感”——对文艺复兴的超越 ✓（wp）、椭圆平面 ✓、强烈明暗 ✓、运动感 ✓。
  - time_or_place“文艺复兴至19世纪、欧洲”——欧洲 ✓（spread across Europe）、“late 16th century”✓；**“至19世纪”为 scope 时段归类口径（巴洛克/新巴洛克延续至19世纪），非两源逐字**（Minor，非具体年份编造；与第30轮判定一致）。
  - **原理**“以曲线、起伏立面与集中式椭圆平面制造运动与张力，并借强烈明暗与装饰强调中心”——曲线/椭圆 ✓、明暗 ✓、装饰/强调中心 ✓；**ratio(原理, 定义+概述)=0.2718（中低，机制独立）**。
  - **实例四要素**：名称＝圣彼得大教堂及广场 St. Peter's Basilica ✓（三源）；地点＝梵蒂冈/罗马 ✓（官方两源 Vatican/Rome）；设计者＝布拉曼特、米开朗基罗、马代尔诺（立面）、贝尼尼（广场柱廊）✓（turismoroma `Bramante, Michelangelo, Bernini`+`seventeenth-century facade by Carlo Maderno`；basilica `dome … Michelangelo`+`Square … Bernini`）；年份＝1506 奠基、17 世纪立面、广场 1667 建成 ✓（basilica `18 April 1506 … first stone`+`completed in 1667`；turismoroma `seventeenth-century facade`）。**两官方来源机构独立互证，无编造。**
- **来源支撑强度说明（诚实标注）**：本条**风格定义/概述**主要由 `wp-baroque-architecture`（权威百科）直证；两家圣彼得官方源主要**直证实例细节并坐实“巴洛克”属性**（turismoroma `majestic Baroque composition`）。即：**实例为多源互证；风格特征的定义性表述以单一权威百科为主**——属“以权威百科定义 + 官方源锚定实例”的稳健结构，不构成编造，但严格意义下风格定义本身为**单一定义源**（Minor，建议后续补一条独立风格综述源以强化定义的两源互证）。
- **内容判定：合格**（definition/overview 有权威百科直证、实例四要素多源互证、无编造、原理独立；**次要点**：风格定义为单一权威百科源、time“至19世纪”为分类口径、实例与 pending 措辞见 §六）。**一图 SVG 见 §五；文本相似度见 §七（未越线）。**

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：5 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）。`link_ok`：`wp-baroque-architecture`=true，其余 4=null（三态，非死链、非假源）。**5 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：`wp-hatching`（owiki 200）/`artincontext-hatching`（200）/`wp-baroque-architecture`（owiki 200）/`basilicasanpietro`（200）/`turismoroma-sanpietro`（200）——**5/5 全部 HTTP 200，无死链**（体检 F 之“死链”对本次 5 源为 0）。
- **相关性**：5 源**均直接主体源、实质支撑**（2 百科/专题 + 2 圣彼得官方）；**无第42轮 `designingbuildings-proxemics` 式“直接但极薄/对具体概念零覆盖”缺陷**。唯一**元数据瑕疵**：3 处 `title` 字段与实际 `<title>` 不符（见 §二警示，正文支撑不受影响）。
- **词项覆盖细节**：hatching 的“质感/texture”有 artincontext 直证、“版画”有 wp 直证（engraving/etching/woodcut）；baroque 的“曲线/椭圆/明暗/宏大尺度”均有 wp 直证（oval spaces/chiaroscuro/grandeur），“动感曲线”以“Solomonic columns…illusion of motion + oval spaces”表达——**语义可通、非缺源、非编造**。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | 含“示意图，非施工图” | viewBox | 风险/规范句 | 原理=def+概述拼接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hatching | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | 否（ratio 0.1600） |
| baroque | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | 否（ratio 0.2718） |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含“示意图，非施工图”；「常见错误与限制」段均以规范提示收尾（`实际工程须按当地规范和专业设计人员的要求`）；`check.py` 含 SVG 出界检查，本轮 PASS（两图元素坐标全部在 760×400 内）。**机械项两条全部通过。**

### SVG 质量观察（形态贴合主题，但缺“设计意图/尺寸关系”显式标注——次要、系统性）
- **hatching**：`<line>×7`（左 `<g stroke=accent>` 4 条平行斜线 + 右 `<g stroke=muted>` 3 条平行横线），两组异向＝“平行线 vs 交叉方向”示意，**贴合“平行线与交叉线的密度差异”主题、且非随机占位**（对比第41轮 batch-38 的随机自交多边形）；但两组线**间距相同、未表现“疏密渐变”**，且图内**仅有标题与“示意图，非施工图”，缺 TASK_design 第6条要求的“设计意图或尺寸关系”标注**（次要缺陷）。
- **baroque**：`<ellipse rx=200 ry=70>`（圆形/椭圆广场）+ `<path M200 230 Q380 60 560 230>`（曲面/起伏立面）+ `<line>`（中轴），**贴合“曲线立面与圆形广场”主题、非随机占位**；但为抽象概括，**未标注设计意图或尺寸关系**（次要缺陷）。
- **判定**：两条「一图」**机械项（1 张 + viewBox + “示意图，非施工图” + 不出界）全过**，且**图形形态与主题相关**（区别于 batch-38 完全无关的随机多边形模板）；**唯一不足为“缺图中设计意图/尺寸关系标注”**——`check.py` 只查出界与注记，查不出该语义项，属**次要/可提升**，不构成本轮“不合格”。建议全站做一次 SVG 标注补强（与第44轮对 batch-38 的“重绘+标注”整改方向一致）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatches=NONE）：hatching（排线法（Hatching）/理论/重要/文艺复兴至19世纪/欧洲/L2）、baroque（巴洛克建筑/风格/重要/文艺复兴至19世纪/欧洲/L2）；`source_count` 与来源数组长度一致（2=2、3=3）；`needs_verification_count`：各 1；`related`：hatching=`[]`（无悬空）、baroque=`['renaissance-style','rococo']`（两者均存在，无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| hatching | true | 「排线法（Hatching）」的具体实例（作品、作者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（源已给 Dürer/Schongauer 等，措辞偏保守） |
| baroque | true | 圣彼得大教堂为多建筑师跨时段作品，单一设计者与部分年代不写死。 | 该建筑为多建筑师跨时段作品，单一设计者与部分年代不写死；其余细节待核实。 | **语义一致、非逐字**（待核实节多“其余细节待核实”一句；`check.py` 仅要求非空，不校验逐字，故 PASS） |

> 结构化标志与两处文本：hatching **逐字一致**；baroque **语义一致但非逐字**（与第30轮判定一致，属 Minor）。**注意（D14 精神）**：hatching「待核实」称“具体实例待补充”，而所引 wp 源已含具名艺术家（Dürer、Schongauer、Master ES、Reuwich、Wolgemut），措辞**偏保守、略失准**（非编造、非缺源）；baroque「待核实」称“部分年代不写死”，但实例已写 1506 奠基、17 世纪立面、1667 广场——**措辞与实例所给年份略相抵**（保守但不够自洽，Minor）。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 251 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| hatching | **0.3871** vs stippling | <0.54 ✓ | **0.4581** vs stippling | <0.54 ✓ |
| baroque | **0.4321** vs rococo | <0.54 ✓ | **0.3827** vs rococo | <0.54 ✓ |

> 对**既有 250 条**（排除自身）逐条扫描，两条两档均 **<0.54**（短文本最大 0.4321、全字段最大 0.4581）——**各自与既有库文本区分在阈值内**。hatching 最近邻为同批 `stippling`（0.3871/0.4581，均 <0.54）；baroque 最近邻为风格近亲 `rococo`（0.4321/0.3827，均 <0.54，同属时代/装饰风格近义，属正常语义邻近，未越线）。

### 7.2 batch-42 去模板化核验（hatching vs stippling——第43轮曾越线，本轮已修复）
| 对 | ①短文本 | ②全字段 |
| --- | --- | --- |
| hatching vs stippling（本轮复算） | **0.3871** | **0.4581** |
| （第43轮历史值，作对照） | 0.5668（>0.54 ✗） | 0.5448（>0.54 ✗） |

> **第43轮曾报 batch-42 两条互为模板姊妹、双档越线（0.5668/0.5448）。** 其后提交 `b829329 chore: round43 zero-gap 1/3, de-template hatching/stippling` 已改写两条 `time_or_place`（hatching 现为“中世纪起源、15 世纪版画中成型”，stippling 现为“1510 年前后起源于意大利”）并重写 definition/overview/原理。**本轮复算 0.3871/0.4581，已降至 0.54 以下 → 去模板化生效、越线问题已闭环。**

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–44轮报告**逐位一致**，口径正确。

> **文本相似度判定：两条对既有库均 PASS（均 <0.54）；batch-42 批内复算亦已 <0.54（第43轮越线已修复）。无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 文本相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **hatching（排线法）** | definition **双源直证互证**（parallel lines ✓、tonal·shading ✓、texture ✓、drawing·printmaking ✓）；overview **双源直证**（quantity/thickness/spacing→brightness、closeness→darker、intersecting sets→darker）；time_or_place **wp 逐字直证**（Middle Ages + 15 世纪老大师版画）；实例类型性无具名（不编造，源已给 Dürer 等，pending 偏保守）；原理独立（ratio 0.1600） | 2/2 true；wp+artincontext 均直接强源；**2 源 200 可达**；`artincontext` title 节略（次要） | 七节齐、规范句✓；1 SVG 含“示意图，非施工图”、形态贴合（平行/交叉线），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 **逐字一致**（pending 偏保守） | 既有库 ✓（0.3871/0.4581）；vs stippling ✓（0.3871/0.4581，已去模板化） | **合格**（内容/来源/结构/相似度全过；次要：SVG 标注、pending 偏保守、来源 title 节略） |
| **baroque（巴洛克建筑）** | definition 权威百科**直证**（theatrical/chiaroscuro/grandeur/oval）；overview 直证（超文艺复兴/椭圆/明暗/运动）；**实例四要素三源直证**（圣彼得/梵蒂冈-罗马/布拉曼特·米开朗基罗·马代尔诺·贝尼尼/1506 奠基·广场 1667）；原理独立（0.2718）；time“至19世纪”分类口径（Minor） | 3/3 true；wp+basilica+turismoroma 均直接强源；**3 源 200 可达**；`basilica`/`turismoroma` title 与实页不符（次要） | 七节齐、规范句✓；1 SVG 含“示意图，非施工图”、形态贴合（椭圆广场+曲线立面），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 **语义一致（非逐字，Minor）** | 既有库 ✓（0.4321/0.3827） | **合格**（内容/来源/结构/相似度全过；次要：SVG 标注、pending 非逐字、来源 title 不符、定义单一定义源） |

- **内容与来源维度**：**2 合格＋0 待核实（内容无源）＋0 不合格＋0 编造**。definition/time/overview 均获所引来源直证；baroque 实例四要素由三源直证、hatching 双源直证；**硬性“编造具体年份/人名/引文/出处”0 条、假 id 0 条、死链 0 条**。
- **结构与元数据维度**：两条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”、风险/规范句齐备、元素不出界；元数据逐项一致；`needs_verification↔pending↔待核实`（hatching 逐字一致 / baroque 语义一致）；`check.py` PASS 0 errors；两条 `原理` 均非 def+概述拼接。
- **SVG 维度**：两条「一图」机械项全过、图形与主题相关（非 batch-38 式随机模板）；**唯一不足为缺“设计意图/尺寸关系”图中标注**（次要、系统性，建议补强）。
- **文本相似度维度**：两条对既有库与（batch-42 批内）均 **<0.54（PASS）**；第43轮 batch-42 越线经去模板化已修复。方法自校 0.5157 一致。

## 九、总体结论与建议

- **抽样结果**：抽检对象为体检轮指定的 2 条——`hatching`（batch-42，第42轮新增、第43轮已去模板化）与 `baroque`（batch-29，第29轮新增），抽样=2 条（任务 10% 口径；`check.py` 已全库 PASS）。**内容维度：2 合格＋0 待核实（无源）＋0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：5 个引用来源 id 全部存在、verified=true、**实抓 5/5 HTTP 200 可达**、均直接实质支撑；**无第42轮式“直接但极薄/零覆盖”来源缺陷**。唯 3 处来源 `title` 字段与实际页面标题不符（可修的元数据缺陷）。
- **结构/治理层面**：七节/规范提示机械项两条全过、元数据逐项一致、`needs_verification↔pending↔待核实` 一致（baroque 语义一致）、`check.py` PASS 0 errors、原理均非拼接。
- **相似度层面**：两条对既有库与（batch-42 批内）均 <0.54（PASS）；**第43轮 batch-42 的越线（0.5668/0.5448）已由去模板化提交修复（本轮复算 0.3871/0.4581）**。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——无“不合格”内容条目（2 合格），无编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级为草稿并复查」路径：不成立**——两条均 <0.54，且 batch-42 历史越线已修复。
  3. **结论：本轮抽检 2 条全部合格，无整批返工/降级触发。** 项目体检关键项（check.py PASS、5/5 来源可达、无死链、相似度达标、元数据/pending 一致）无阻断问题。
- **定向润色建议（可选，非返工，逐条 1–2 处文字即可）**：
  - **来源 title 更正（应做）**：`artincontext-hatching`→“Cross Hatching – Learning the Cross Hatching Technique”；`basilicasanpietro`→“St. Peter's Basilica”；`turismoroma-sanpietro`→“The Basilica of St. Peter in the Vatican”（正文与 URL 均真，仅改 `title` 字段）；`wp-hatching` 的 `type` 宜由“学术著作”改“权威百科”。
  - **SVG 标注补强（宜做，系统性）**：为 hatching（标注“平行线/交叉线，疏→密→暗”）与 baroque（标注“椭圆广场/曲线立面/中轴”）补“设计意图或尺寸关系”文字标注，落实 TASK_design 第6条；建议对全站 SVG 统一做一次标注补强，与第44轮 batch-38 重绘整改方向一致。
  - **pending 措辞对齐（宜做）**：baroque `pending_notes` 与「待核实」逐字对齐；baroque「待核实」的“部分年代不写死”宜与实例已给年份调和（如“多建筑师跨时段，具体分期归属以各源表述为准”）；hatching 可用源中已给的 Dürer/Schongauer 等作具名实例，并据实更新「待核实」为“具体代表作品年代待补”。
  - **baroque 定义补强（可选）**：可再引一条独立风格综述源，使“风格特征定义”也达成严格两源互证（现为单一权威百科 + 官方源锚定实例）。
- **流程记录**：本轮抽检 2 条＝**内容 2 合格、0 编造、0 假 id、0 死链、七节/规范/元数据一致、check.py PASS、相似度全 <0.54（batch-42 越线已修复）**；**唯一系统性问题为「一图」缺“设计意图/尺寸关系”标注（次要，非不合格）→ 建议全站 SVG 标注补强**；不触发 §E 返工/降级。

---

### 机器可读汇总

```
ROUND=45
SAMPLER=spotcheck-r45
MODE=体检+饱和终判轮（维护抽检，2条：hatching←batch-42 / baroque←batch-29）
SCOPE=["hatching","baroque"]
FILES={"hatching":"entries/batch-42.json","baroque":"entries/batch-29.json"}
STATE={"sources.json":"141826B@2026-11-23 02:06:22","batch-42.json":"4222B@2026-11-23 01:59:59","batch-29.json":"2540B@2026-11-22 23:19:00","coverage.json":"84844B@2026-11-23 02:06:38","check.py":"15908B@2026-11-22 15:11:54","total":251,"written":251,"all_level":"L2","pending_total":219,"sources_total":301,"sources_verified_true":298,"sources_verified_false":3,"link_ok_true":145,"link_ok_false":6,"link_ok_null":150}
GIT_HEAD="e49f0e8 chore: round44 zero-gap 2/3 and batch38 SVG uniqueness"; GIT_STATUS="4 untracked round45 research files (b1/gaps/healthcheck/reader_questions-round45.md) from sibling subtasks, NOT this spotcheck; target files batch-42.json/batch-29.json/sources.json/coverage.json stable; only file this spotcheck wrote = research/spotcheck-round45.md"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2 条 (task 10%; 体检轮指定复检 2 条既有条目)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia -> owiki.org mirror; artincontext + 2 official San Pietro direct; 5/5 HTTP200; analysis in-memory, no temp file"
SOURCES={"count_distinct":5,"count_refs":5,"all_exist":true,"all_verified_true":true,"all_reachable_200":"5/5","link_ok":{"wp-hatching":null,"artincontext-hatching":null,"wp-baroque-architecture":true,"basilicasanpietro":null,"turismoroma-sanpietro":null},
 "title_mismatch":["artincontext-hatching: stored 'Cross Hatching — Art in Context' vs actual '<title>=Cross Hatching – Learning the Cross Hatching Technique' (abbreviated)","basilicasanpietro: stored 'Basilica di San Pietro — Fabbrica di San Pietro' vs actual '<title>=St. Peter's Basilica | A masterpiece to explore'","turismoroma-sanpietro: stored 'Piazza San Pietro — Turismo Roma' vs actual '<title>=The Basilica of St. Peter in the Vatican | Turismo Roma'"],
 "type_note":"wp-hatching type='学术著作' (Wikipedia; should be 权威百科)"}
BODY_SUPPORT={
 "hatching":"definition DIRECT dual-source (wp 'closely spaced parallel lines','tonal/shading','drawing and many forms of printmaking'; artincontext 'Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values and texture'); overview DIRECT (wp 'quantity, thickness and spacing...brightness','increasing quantity, thickness and closeness, a darker area'); time_or_place wp VERBATIM ('originated in the Middle Ages' + 'old master prints of the fifteenth century'); 原理 ratio(原理,def+overview)=0.1600 independent; instance type-description (source names Durer/Schongauer etc) -> pending conservative; VERDICT=合格",
 "baroque":"definition DIRECT from wp authoritative (theatrical/chiaroscuro/dramatic light/higher-grander-more dramatic/oval spaces/Solomonic columns motion); overview DIRECT wp (transcend Renaissance, oval, light, movement); instance 4-elements THREE-SOURCE (basilica '18 April 1506 first stone'+'completed in 1667'; turismoroma 'Bramante, Michelangelo, Bernini'+'seventeenth-century facade by Carlo Maderno'+'Piazza San Pietro...colonnade...Bernini'+'majestic Baroque composition'); 原理 ratio=0.2718 independent; time '至19世纪' classification (Minor); NOTE style-definition primarily single authoritative source (wp), official sources anchor instance; VERDICT=合格"}
L2_CHECK={"seven_sections":"definition+6/6 x2, no missing/extra","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2, no overflow, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","原理_concat":{"hatching":0.1600,"baroque":0.2718}}
SVG_NOTE={"verdict":"机械项全过 + 形态与主题相关（非 batch-38 随机模板）；缺'设计意图/尺寸关系'图中标注（次要/系统性）","hatching":"<line>x7 (4 parallel diagonal accent + 3 parallel horizontal muted) = parallel vs cross-direction, topical; no density gradient; no intent/dimension annotation","baroque":"<ellipse>+<path Q curve>+<line axis> = circular plaza + curved facade; topical; no intent/dimension annotation"}
METADATA={"title/theme/tier/period/region/level":"ALL OK x2 (mismatches NONE)","source_count":"2=2 / 3=3","nvc":"1 x2","needs_verification":"true x2","related":"hatching [] / baroque ['renaissance-style','rococo'] (no dangling)","pending_consistency":{"hatching":"逐字一致","baroque":"语义一致非逐字（Minor）"}}
SIMILARITY={
 "hatching":{"vs_existing_short":0.3871,"vs_existing_short_entry":"stippling","vs_existing_full":0.4581,"vs_existing_full_entry":"stippling","verdict":"PASS<0.54"},
 "baroque":{"vs_existing_short":0.4321,"vs_existing_short_entry":"rococo","vs_existing_full":0.3827,"vs_existing_full_entry":"rococo","verdict":"PASS<0.54"},
 "batch42_pairwise":{"hatching_vs_stippling_short":0.3871,"hatching_vs_stippling_full":0.4581,"round43_historical":"0.5668/0.5448 (>0.54, FIXED by commit b829329 de-template)","verdict":"PASS<0.54 now"},
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-44 exactly -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"hatching":"合格","baroque":"合格"}
VERDICT_SVG={"hatching":"机械项通过/形态贴合，缺意图·尺寸标注(次要)","baroque":"机械项通过/形态贴合，缺意图·尺寸标注(次要)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
BATCH_ACTION="No rollback/downgrade triggered: content path clear (2 合格, 0 fabrication/0 fake id/0 dead link); similarity path clear (all <0.54; batch-42 round43 0.5668/0.5448 fixed -> 0.3871/0.4581). Optional polish only: correct 3 source title fields (artincontext/basilica/turismoroma) + wp-hatching type; site-wide SVG '设计意图或尺寸关系' annotation pass (esp. hatching/baroque); align baroque pending_notes<->待核实 verbatim & reconcile '部分年代不写死' with listed years; optional extra independent source for baroque style definition."
READONLY="only wrote research/spotcheck-round45.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (no persistent temp file)"
```

*（报告完）*
