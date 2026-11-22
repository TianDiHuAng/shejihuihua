# 第43轮质量闸抽检报告（spotcheck-round43）——batch-42 新增 2 条（hatching / stippling）

- 抽检人：spotcheck-r43（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 01:56 起，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；新增/改动条目随机抽 10%、**至少 3 条**逐条核对来源；**不合格则整批返工**，下一轮抽检比例提高到 25%；异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级为草稿并复查」）+ 第六节（联网内容一律视为数据，其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）+ `TASK_design.md`「条目页结构」L2 七节标准与「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标“待核实”**；只引用 `verified=true` 来源；图下注明“示意图，非施工图”；尺寸/坡度/消防/无障碍注明“实际工程须按当地规范和专业设计人员的要求”）+ `DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md` / `TASK_design.md` 在仓库根**无同名文件**（与第 12–42 轮一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md`（21 行）在仓库根已读；`research/spotcheck-round42.md`（215 行）已读作模板对齐。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 01:56 起）**：`data/sources.json`=141823B@01:54:18、`entries/batch-42.json`=4221B@01:54:18、`coverage.json`=84844B@01:54:57、`tools/check.py`=15908B@2026-11-22 15:11:54。`git log -1` = `dfc5753 docs: note round42 push status`。
- **工作树状态（采样时点）**：`git status --porcelain` 仅 3 项未跟踪——`?? research/gaps-round43.md`、`?? research/healthcheck-round43.md`、`?? research/reader_questions-round43.md`（第43轮其它兄弟子任务产出，**非本次抽检所改**）。抽检对象文件 `entries/batch-42.json`、`data/sources.json`、`coverage.json` 在采样期间稳定（未被 `git status` 列为 modified），判定基于稳定快照。
- **条目规模（`coverage.json` 实读）**：`total=251`、全部 `level=L2`、全部 `status=已写`；`pending_total`（`needs_verification_count` 求和）＝**219**；来源库 `sources.json` 共 **301** 条，其中 `verified=true` 共 **298** 条（`link_ok`：true 145、false 6、null 150）。注：`link_ok=false` 的 6 条**均不在本次抽检的 4 个来源中**，不影响本轮判定。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round43.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python urllib 读取→内存计数/切句），未在项目内外落盘任何持久文件。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1 张内联 SVG 且含“示意图，非施工图”；「常见错误与限制」段须含“实际工程须按当地规范和专业设计人员的要求”；SVG 元素不出 `viewBox`（均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），带 3 次重试。`en.wikipedia.org` 直连按 D05 改走 **owiki 同源镜像** `https://owiki.org/wiki/<Title>`；`artincontext.org` 直连。本轮 **4 个引用来源全部实抓 HTTP 200**（h1/标题与 `sources.json` 逐条核对，见 §二、§四）。正文去标签后做关键词实计与上下文切句（全程内存）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **251 条**去重已写条目逐条扫描，警戒线 **0.54**（与第27–42轮一致）。**方法自校**：以全字段②计算 batch-38 已知最高对 `futurism-style vs expressionism-style`，得 **0.5157**，与第39/40/41/42轮报告**逐位一致**，确认口径正确。
- **“两源互证”判定口径**：按 `TASK_design.md` 硬性规则“关键事实至少两个独立来源互相印证，否则标待核实”。本轮按“两个引用来源须对本条**具体概念**有实质覆盖且互证”执行。
- **本报告三级判定定义（明确、可复现）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；两源（或以上）均直接相关且关键事实获（至少近似）互证；无编造；机械项全过。
  - **待核实**：核心获**至少一个直接相关来源**实质支撑，但存在下列之一：(a) 第二源对本条具体概念仅泛论/零覆盖、关键事实实质单源；(b) 某一具体标志性词项无源；(c)「原理」＝定义+概述逐字拼接。→ 属来源支撑/深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被**两个引用来源均不支撑（实质无源）**，实质性违反两源互证。
- **相似度专项（独立维度）**：警戒线 0.54。超线即触发 `AUTONOMOUS.md §E`「新条目与已有条目相似度过高（疑似套话）→ 整批降级为草稿并复查」；该异常属**风格/去重缺陷**，与“不合格（内容无源）→整批返工”是**不同触发路径**，本报告分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **4 个去重来源 id（4 处引用：hatching 2、stippling 2）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）**、实抓 HTTP 200（标题核对一致）；`link_ok` 4 个均为 **null**（三态，非死链）。**无死链、无假 id、无 verified=false 被引用。**

| 条目 | 来源 id | 存在/verified | 标题 / 机构 | type | link_ok | 与主题相关性（实抓正文） |
| --- | --- | --- | --- | --- | --- | --- |
| hatching | `wp-hatching` | ✅ / true | Hatching / Wikipedia（owiki 200, 14266B, h1=Hatching, textlen≈4269） | 学术著作 | null | **直接主体源、强支撑**：`Hatching is an artistic technique used to create tonal or shading effects by drawing, painting, or scribing closely spaced parallel lines`；`When lines are placed at an angle to one another, it is called cross-hatching`；`Hatching is especially important in essentially linear media, such as drawing and many forms of printmaking, such as engraving, etching, and woodcut`；`the quantity, thickness and spacing of the lines will affect the brightness … the illusion of volume`；`By increasing quantity, thickness and closeness, a darker area will result`；`Hatching lines should always follow the form`。`hatching=13, cross-hatch=2, cross=4, shading=2, engraving=3, etching=1, lines=9` |
| hatching | `artincontext-hatching` | ✅ / true | Cross Hatching – Learning the Cross Hatching Technique / Art in Context（200, 445551B, textlen≈19631） | 学术著作 | null | **直接主体源、强支撑**：`Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values and texture`；`Using your pencils, start with a light layer of cross-hatching to establish the shadow areas`；`Practice five values, curved strokes, and line spacing`。`hatching=67, cross=73, shading=15, etching=3, lines=42` |
| stippling | `wp-stippling` | ✅ / true | Stippling / Wikipedia（owiki 200, 13116B, h1=Stippling, textlen≈3572） | 学术著作 | null | **直接主体源、强支撑**：`Stippling is the creation of a pattern simulating varying degrees of solidity or shading by using small dots`；`the denser the dots, the darker the apparent shade—or lighter, if the pigment is lighter than the surface`；`similar to—but distinct from—pointillism, which uses dots of different colours to simulate blended colours`；`In printmaking, stipple engraving is a technique using flicks of the burin to build up the image in short lines or dots`。`stippling=6, dot=6, dots=5, engraving=2` |
| stippling | `artincontext-stippling` | ✅ / true | Stippling Art – Creating Designs and Patterns With Small Dots / Art in Context（200, 381041B, textlen≈24029） | 学术著作 | null | **直接主体源、强支撑**：`stippling art is a drawing technique that creates images and shapes on paper by making small dots close together`；`When the dots are further apart, it creates highlights, or when closer together, it creates shadows`；`This will form contours of a particular shape and give the image realism and depth`；`The stippling process was first invented by an Italian engraver and painter Giulio Campagnola in 1510`；`The stippling technique is also used in scientific illustrations … in biology and archeology`。`stippling=99, dot=55, dots=49, shading=17, gradient=3` |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（hatching 2=2、stippling 2=2）。4 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。** 4 源均直接相关、强支撑（无第42轮 `designingbuildings-proxemics` 式“直接但极薄/零覆盖”缺陷）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 hatching（排线法）——**内容合格**
- **wp-hatching**（owiki HTTP200, textlen≈4269）直证：
  - `Hatching is an artistic technique used to create tonal or shading effects by drawing, painting, or scribing closely spaced parallel lines` → 支撑 definition“以密集的平行线表现明暗”。
  - `When lines are placed at an angle to one another, it is called cross-hatching` + `By increasing quantity, thickness and closeness, a darker area will result` → 支撑 definition“交叉排线叠加多组线以加深色调”与 overview“越密越暗”。
  - `the quantity, thickness and spacing of the lines will affect the brightness … emphasize forms creating the illusion of volume` → 支撑 overview“越疏越亮/塑造体积”与「原理」“疏密决定明度…塑造体积”。
  - `especially important in essentially linear media, such as drawing and many forms of printmaking, such as engraving, etching, and woodcut` → 支撑「原理」“版画、素描…的常用手段”。
  - `Hatching lines should always follow the form` → 支撑「典型手法」“按形体走向安排线组方向”。
- **artincontext-hatching**（HTTP200, textlen≈19631）直证：
  - `Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values and texture` → 支撑 definition（互证：平行线+交叉叠加加深+**质感 texture**）与 overview“交叉排线可层层加深”。
  - `start with a light layer of cross-hatching to establish the shadow areas` + `line spacing` → 支撑「典型手法」“以平行线铺底、交叉线加深”。
- **逐项结论**：
  - definition“以密集的平行线表现明暗与质感，交叉排线叠加多组线以加深色调”——**两源直证互证**（closely spaced parallel lines ✓ / tonal·shading ✓ / cross-hatching intersecting sets build darker values & texture ✓）。
  - overview“线条越密越暗、越疏越亮，交叉排线可层层加深”——**两源直证**（increasing quantity·thickness·closeness→darker ✓ / spacing→brightness ✓ / intersecting sets build darker ✓）。
  - time_or_place“文艺复兴至19世纪、欧洲”——欧洲（Western art）✓；**“文艺复兴起”近似成立**（wp：`old master prints of the fifteenth century`＝15世纪文艺复兴早期；但 wp 原文 `originated in the Middle Ages`，起点实更早）；**“至19世纪”上界无正文支撑（次要瑕疵，非具体日期编造）**。
  - **原理**“线条的疏密与交叉层数决定局部明度，是版画、素描与铜版画塑造体积的常用手段”——疏密/交叉→明度✓、版画/素描/engraving·etching✓、volume✓；**非 def+overview 拼接（实算 ratio(原理, def+概述)=0.1346）**。唯一细节：**“铜版画”略具体**——wp 列举 `engraving, etching, woodcut`，铜版画属 engraving/etching 凹版，属合理外推（次要）。
  - 实例“名称：铜版画的排线明暗（类型性描述）；地点与设计者不适用”——**类型性、无具名/年份 → 不编造** ✓；**但所引来源已含具名实例**（wp：`Albrecht Dürer`、`Martin Schongauer`、`Master ES`、`Erhard Reuwich` 等），条目未采用、`pending_notes` 称“作品、作者、年代待补充独立来源”——**作者/作品其实已由已核验来源给出**，措辞偏保守（非编造）。
- **两源互证**：核心定义、交叉叠加、疏密→明度、版画媒介由 **wp-hatching 与 artincontext-hatching 双源强直证并互证**。
- **内容判定：合格**（definition/overview/原理双源直证、机制独立、无编造；**次要瑕疵**：period“至19世纪”无源、“铜版画”略具体、实例未用已给具名艺术家且 pending 偏保守）。**相似度另见 §七（越线）。**

### 3.2 stippling（点描法）——**内容合格**
- **wp-stippling**（owiki HTTP200, textlen≈3572）直证：
  - `Stippling is the creation of a pattern simulating varying degrees of solidity or shading by using small dots` → 支撑 definition“以细点的疏密表现明暗”。
  - `the denser the dots, the darker the apparent shade—or lighter, if the pigment is lighter than the surface` → 支撑 overview“点越密越暗、越疏越亮”与「原理」“单位面积点数决定局部明度”。
  - `similar to—but distinct from—pointillism, which uses dots of different colours` → stippling 与 pointillism **明确区分**（未混淆）。
  - `In printmaking, stipple engraving … build up the image in short lines or dots` → 支撑版画语境（「原理」）。
- **artincontext-stippling**（HTTP200, textlen≈24029）直证：
  - `stippling art is a drawing technique that creates images and shapes on paper by making small dots close together` → 支撑 definition（互证）。
  - `When the dots are further apart, it creates highlights, or when closer together, it creates shadows` → 支撑 overview（互证）。
  - `This will form contours of a particular shape and give the image realism and depth` → 支撑 definition“形体”。
  - `The stippling process was first invented by an Italian engraver and painter Giulio Campagnola in 1510` + `smoother transition of shading and tone` → 支撑 time“文艺复兴”（1510）与「原理」“模拟连续调子/渐变”。
  - `The stippling technique is also used in scientific illustrations … in biology and archeology` → 支撑「实例」“点描的生物插画”（有据的类型性描述）。
- **逐项结论**：
  - definition“以细点的疏密表现明暗与形体的绘制技法”——**两源直证互证**（small dots shading ✓ / drawing technique·shapes ✓ / contours of shape ✓）。
  - overview“点越密越暗、越疏越亮，靠点的聚集塑造渐变”——**两源直证**（denser dots darker ✓ / apart highlights · closer shadows ✓ / smoother transition of shading and tone 渐变 ✓）。
  - time_or_place“文艺复兴至19世纪、欧洲”——**“文艺复兴起”成立且强**（artincontext：`invented … Giulio Campagnola in 1510`，意大利/欧洲）；欧洲✓；**“至19世纪”上界无正文支撑（次要瑕疵，非具体日期编造）**。
  - **原理**“单位面积内点的数量决定局部明度，靠点阵密度模拟连续调子”——密度→明度✓、连续调子（varying degrees of solidity or shading / smoother transition of tone）✓；**非 def+overview 拼接（实算 ratio(原理, def+概述)=0.1687）**。
  - 典型手法“以细密点阵逐层加密表现暗部，靠疏密过渡表现亮部”——artincontext：`dots further apart → highlights, closer → shadows`、四技法 dotting/dashing/tracing/hatching、按压力使点大小变化 → **支撑**。
  - 实例“名称：点描的生物插画（类型性描述）；地点与设计者不适用”——**类型性、无具名/年份 → 不编造** ✓；且“科学/生物插画”**有据**（artincontext：scientific illustrations / biology）；**来源另含具名艺术家**（Campagnola 1510、Isaac Beckett），条目未采用、`pending_notes` 偏保守（非编造）。
- **两源互证**：核心定义、疏密→明暗、渐变、形体由 **wp-stippling 与 artincontext-stippling 双源强直证并互证**；与 pointillism 明确区分（wp）。
- **内容判定：合格**（definition/overview/原理双源直证、机制独立、与 pointillism 区分、无编造；**次要瑕疵**：period“至19世纪”无源、实例未用已给具名艺术家且 pending 偏保守）。**相似度另见 §七（越线）。**

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：4 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）。`link_ok` 4 个均=null（三态，非死链、非假源）。**4 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：`wp-hatching`（owiki 200, 14266B, h1=Hatching）/ `artincontext-hatching`（200, 445551B, h1=Cross Hatching – Learning the Cross Hatching Technique）/ `wp-stippling`（owiki 200, 13116B, h1=Stippling）/ `artincontext-stippling`（200, 381041B, h1=Stippling Art – Creating Designs and Patterns With Small Dots）。**4/4 全部 HTTP 200，无死链。**（en.wikipedia 按 D05 改走 owiki 镜像，正文完整。）
- **相关性**：4 源**均直接主体源、强支撑**（wp 为百科专条、artincontext 为专题教程），**无 round42 `designingbuildings-proxemics` 式“直接但极薄/对具体概念零覆盖”缺陷**。唯一细节：`wp-hatching` 的 `density=0`（未用“density”一词），但以 `increasing quantity, thickness and closeness → darker` 表达同一“疏密→明度”概念，**语义等价，非缺源**；`wp-stippling`/两条 artincontext 均有直接“denser/closer→darker、apart→lighter”表述。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | 含“示意图，非施工图” | viewBox | 风险/规范句 | 原理=def+概述拼接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hatching | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | **否**（独立机制；ratio 0.1346） |
| stippling | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | **否**（独立机制；ratio 0.1687） |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含“示意图，非施工图”；「常见错误与限制」段均以规范提示收尾；`check.py` 含 SVG 出界检查，本轮 PASS。**机械项两条全部通过。**
>
> **SVG 质量观察**：
> - `hatching`：`<line>×7`（左 group 4 条平行斜线＋右 group 3 条平行横线，两组异向＝平行线/交叉线示意），**贴合“平行线与交叉线叠加”尚可**（形态抽象，未表现疏密渐变）。
> - `stippling`：`<circle>×2` 且 `stroke-dasharray='2 10'/'1 14'`（用虚线圆环示意“点”），**贴合“点的疏密形成明暗”偏弱**——两个虚线圆环并非点阵密度渐变，表达力有限（仍属非纯占位，机械项通过）。
> - 两条 SVG 基本形不同（直线组 vs 虚圆环），无跨条目几何模板复用迹象（对比第41轮 batch-38 的 >0.95 雷同，本批形态可区分）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatches=NONE）：hatching（排线法（Hatching）/理论/重要/文艺复兴至19世纪/欧洲/L2）、stippling（点描法（Stippling）/理论/补充/文艺复兴至19世纪/欧洲/L2）；`source_count` 与来源数组长度一致（2=2、2=2）；`needs_verification_count`：各 1；`related`：两条均为 `[]` 空数组（无悬空引用）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| hatching | true | 「排线法（Hatching）」的具体实例（作品、作者、年代）待补充独立来源。 | 逐字相同 | **结构逐字一致** ✓（但内容上作者/作品已由已核验源给出，措辞偏保守） |
| stippling | true | 「点描法（Stippling）」的具体实例（作品、作者、年代）待补充独立来源。 | 逐字相同 | **结构逐字一致** ✓（Campagnola/Beckett 具名实例已由源给出，措辞偏保守） |

> 结构化标志与两处文本**逐字一致**（程序化 `pending_notes == sections.待核实` 两条全部 True）。**注意（D14 精神）**：两条「待核实」仅声明“具体实例待补充”，而所引来源实际上已含具名艺术家/作品（Dürer / Schongauer / Campagnola / Beckett），措辞**偏保守、略失准**（非编造、非缺源）。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 251 条；口径②=全字段-不含 SVG，`一图`计入）

**这是本轮唯一实质性缺陷，也是核心结论。**

### 7.1 对既有库（排除同批姊妹）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| hatching | **0.3980** vs sfumato | <0.54 ✓ | **0.4194** vs sfumato | <0.54 ✓ |
| stippling | **0.4211** vs sfumato | <0.54 ✓ | **0.4494** vs sfumato | <0.54 ✓ |

> 对**既有 249 条**（排除同批另一方）逐条扫描，两条两档均 **<0.54**（短文本最大 0.4211、全字段最大 0.4494）——**各自与既有库区分良好**。

### 7.2 同批两条（hatching vs stippling）——**双双越线**
| 对 | ①短文本 | ②全字段 |
| --- | --- | --- |
| **hatching vs stippling** | **0.5668（>0.54 ✗）** | **0.5448（>0.54 ✗）** |

> **两条 batch-42 新增条目互为模板姊妹，①短文本 0.5668、②全字段 0.5448，双双越过 0.54 警戒线。** 结构性成因（可复现）：两 `time_or_place` **逐字相同**（均为“文艺复兴至19世纪、欧洲（参见来源）。”）；definition 同构（“X指以…的疏密表现明暗与…”）；overview 同构（“X越密越暗、越疏越亮…”）；原理/典型手法同为“疏密→明度/逐层加密”。**属典型的批内套话模板**。
> **与既有目标条目区分（任务专项）**：hatching vs `light-shadow-modeling`＝短 0.324/全 0.3471、vs `cunfa`＝短 0.1892/全 0.33；stippling vs `light-shadow-modeling`＝短 0.3452/全 0.3728、vs `cunfa`＝短 0.2482/全 0.3591——**均 <0.54 且概念可区分**（光影塑形＝受光/背光明暗梯度塑体积；皴法＝中国山水笔触表现山石纹理；排线/点描＝以平行线/细点密度表现明暗的具体技法，媒介与手法不同）。**问题不在“与既有库套话”，而在“两条新条目彼此套话”。**

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39/40/41/42轮报告**逐位一致**，口径正确。

> **相似度判定：两条对既有库均 PASS；但两条彼此 0.5668/0.5448 双越 0.54 → 触发 `AUTONOMOUS.md §E` 异常监控「新条目与已有条目相似度过高（疑似套话）→ 整批降级为草稿并复查」。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关 | L2 七节/SVG/风险 | 元数据·联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **hatching（排线法）** | definition/overview/原理 **双源直证互证**（closely spaced parallel lines / cross-hatching intersecting sets build darker values & texture / increasing closeness→darker / spacing→brightness / volume / engraving·etching）；period 文艺复兴近似成立（15世纪老大师），**“至19世纪”无源（次要）**；“铜版画”略具体（次要）；实例类型性无具名（不编造，源已给 Dürer/Schongauer 等） | 2/2 true；**wp + artincontext 均直接主体源、强互证** | 七节齐、SVG✓（7 线组，贴合尚可）、风险✓；原理非拼接 | 全部一致；nv=true/pending/待核实 逐字一致（pending 偏保守） | 既有库 ✓（0.398/0.419）；**同批 vs stippling 0.5668/0.5448 越线 ✗** | **内容合格；相似度越线→需去模板化返工** |
| **stippling（点描法）** | definition/overview/原理 **双源直证互证**（small dots shading / shapes·contours / denser dots darker·apart lighter / smoother transition of tone / scientific illustration / 与 pointillism 明确区分）；period 文艺复兴成立（1510 Campagnola），**“至19世纪”无源（次要）**；实例类型性无具名（不编造，源已给 Campagnola/Beckett） | 2/2 true；**wp + artincontext 均直接主体源、强互证** | 七节齐、SVG✓（2 虚圆环，贴合偏弱）、风险✓；原理非拼接 | 全部一致；nv=true/pending/待核实 逐字一致（pending 偏保守） | 既有库 ✓（0.4211/0.4494）；**同批 vs hatching 0.5668/0.5448 越线 ✗** | **内容合格；相似度越线→需去模板化返工** |

- **内容与来源维度**：**2 合格＋0 待核实＋0 不合格＋0 编造**。definition/time/overview/原理均**双源强直证并互证**（本轮来源质量优于第42轮 proxemics 的单源缺口）；实例均为**类型性描述**、无具名作品/作者/年份；**硬性“编造具体年份/人名/引文/出处”0 条、假 id 0 条、死链 0 条**。唯一内容次要点：两条 period“至19世纪”上界无源、实例未采用源中已给具名艺术家（pending 偏保守）、hatching“铜版画”略具体。
- **结构与元数据维度**：两条 L2 七节齐、各 1 张 SVG 含“示意图，非施工图”、风险/规范句齐备；元数据逐项一致；`needs_verification↔pending↔待核实` 两条**逐字一致**；`check.py` PASS 0 errors；两条 `原理` 均非 def+overview 拼接。
- **相似度维度（决定性缺陷）**：对既有库两条均 PASS（≤0.4494）；**但两条彼此 0.5668（短）/0.5448（全）双越 0.54**——批内套话模板，触发 §E「整批降级为草稿并复查」。

## 九、总体结论与返工建议

- **抽样结果**：抽检对象为 batch-42 全 2 条新增（hatching、stippling），抽样=100%（`§E` “至少 3 条”本轮因该批仅 2 条新增，实抽 2 条并**额外对同批与既有库全量做相似度扫描**，覆盖充分）。**内容维度：2 合格＋0 待核实＋0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：4 个引用来源 id 全部存在、verified=true、**实抓 4/4 HTTP 200 可达**、均直接主体源强支撑；**无第42轮式“直接但极薄/零覆盖”来源缺陷**。
- **结构/治理层面**：七节/SVG/规范提示机械项两条全过、元数据与 pending 联动两条**逐字一致**、`check.py` PASS 0 errors、原理均非拼接；SVG 基本形可区分（直线组 vs 虚圆环）。
- **相似度层面（关键）**：对既有库两条均 <0.54（PASS）；**但两条彼此 ①0.5668 / ②0.5448 双越 0.54 警戒线 → 批内套话模板**。方法自校 0.5157 一致，口径正确。
- **是否建议整批返工 / 降级（结论）**：
  1. **§E“抽检不合格→整批返工（25%）”路径：不成立**——无“不合格”内容条目（2 合格），且无编造/假 id/死链。
  2. **§E“相似度过高（疑似套话）→整批降级为草稿并复查”路径：成立**——batch-42 两条互为模板姊妹、双档越线。**建议：将 batch-42 全 2 条降级为草稿并复查，做去模板化改写后重抽。**
  3. **定向返工/最小修复建议（batch-42）**：
     - **去模板化**：改写两条各自的 `time_or_place`（现两者逐字相同“文艺复兴至19世纪、欧洲（参见来源）。”，应分别据源细化：hatching 可写“中世纪起源、15 世纪老大师版画成型、欧洲”；stippling 可写“1510 年意大利起源、欧洲”）、`definition` 与 `overview` 句式（避免“X越密越暗、越疏越亮”同构照搬），并区分「原理」表述，使 pairwise 降至 <0.54。
     - **period 收窄**：两条“至19世纪”上界无源 → 收窄为“文艺复兴（及此前/中世纪起源，视条目）”或补 19 世纪来源后再保留。
     - **实例据实**：hatching 可用已核验源具名（Dürer / Schongauer / Master ES）、stippling 用（Campagnola 1510 / Isaac Beckett）替换通用类型描述，并据实更新「待核实」（改为“仅具体年代/某作品待补”）。
     - **hatching「原理」“铜版画”**：改为已源支撑的“版画（engraving / etching / woodcut）”或补铜版画来源。
  4. **流程说明**：本轮 batch-42 仅 2 条新增，已全抽（100%）+ 全库相似度扫描；**因相似度越线，batch-42 需“降级草稿并复查（去模板化重写）”，复查通过后即可纳入正常 10% 抽检节奏**（无需按“不合格”上调至 25%，因非内容无源缺陷）。

- **流程记录**：本轮抽检 2 条（batch-42 全 2）＝**内容 2 合格、0 编造、0 假 id、0 死链、机械项全过、元数据/pending 逐字一致、原理非拼接**；**唯一实质缺陷为两条彼此相似度双越 0.54（批内套话模板）→ §E 整批降级为草稿并复查，去模板化改写后重抽。**

---

### 机器可读汇总

```
ROUND=43
SAMPLER=spotcheck-r43
SCOPE=["hatching","stippling"]
FILES={"hatching":"entries/batch-42.json","stippling":"entries/batch-42.json"}
STATE={"sources.json":"141823B@2026-11-23 01:54:18","batch-42.json":"4221B@2026-11-23 01:54:18","coverage.json":"84844B@2026-11-23 01:54:57","check.py":"15908B@2026-11-22 15:11:54","total":251,"written":251,"all_level":"L2","pending_total":219,"sources_total":301,"sources_verified_true":298,"link_ok_true":145,"link_ok_false":6,"link_ok_null":150}
GIT_HEAD="dfc5753 docs: note round42 push status"; GIT_STATUS="3 untracked round43 research files (gaps/healthcheck/reader_questions-round43.md) from sibling subtasks, NOT this spotcheck; target files batch-42.json/sources.json/coverage.json stable; only file this spotcheck wrote = research/spotcheck-round43.md"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2/2 (=100%: batch-42 has only 2 new entries; plus full-library similarity scan)"
FETCH_METHOD="urllib+ChromeUA; en.wikipedia -> owiki.org mirror; artincontext direct; 4/4 HTTP200; analysis in-memory, no temp file"
SOURCES={"count_distinct":4,"count_refs":4,"all_exist":true,"all_verified_true":true,"all_reachable_200":"4/4","link_ok":{"wp-hatching":null,"artincontext-hatching":null,"wp-stippling":null,"artincontext-stippling":null},"relevance_defects":[]}
BODY_SUPPORT={
 "hatching":"definition DIRECT by BOTH (wp 'create tonal or shading effects by ... closely spaced parallel lines','cross-hatching'=lines at angle,'By increasing quantity,thickness and closeness, a darker area will result','quantity,thickness and spacing ... brightness ... illusion of volume','engraving,etching,woodcut','Hatching lines should always follow the form'; artincontext 'Hatching uses parallel lines; cross-hatching adds intersecting sets to build darker values and texture'); 原理 not concat(ratio 0.1346); MINOR: period upper '至19世纪' unsourced (wp: originated Middle Ages / 15th-c old masters), '铜版画' slight specificity, instance type-description though source names Dürer/Schongauer; VERDICT=合格(content)",
 "stippling":"definition DIRECT by BOTH (wp 'creating a pattern simulating varying degrees of solidity or shading by using small dots','the denser the dots, the darker the apparent shade—or lighter','distinct from pointillism'; artincontext 'drawing technique ... small dots close together','dots further apart highlights, closer shadows','contours of a particular shape','invented ... Campagnola in 1510','smoother transition of shading and tone','scientific illustrations biology'); 原理 not concat(ratio 0.1687); MINOR: period upper '至19世纪' unsourced (1510 supports Renaissance start), instance type-description though source names Campagnola/Beckett; VERDICT=合格(content)"
}
L2_CHECK={"seven_sections":"definition+6/6 x2, no missing/extra","svg":"1 each, all 示意图非施工图, viewBox 0 0 760 400, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","原理_concat":"none (0.1346/0.1687)","svg_shapes":{"hatching":"line x7 (two groups: 4 slanted + 3 horizontal; fair fit)","stippling":"circle x2 dashed (stroke-dasharray; weak fit for dot-density)"},"svg_distinct":true}
METADATA={"title/theme/tier/period/region/level":"ALL OK x2 (mismatches NONE)","source_count":"2=2/2=2","nvc":"1 x2","needs_verification/pending_notes/待核实":"verbatim-identical x2 (pending slightly conservative: named artists exist in sources)","related":"[] x2 (no dangling)"}
SIMILARITY={
 "hatching":{"vs_existing_short":0.3980,"vs_existing_short_entry":"sfumato","vs_existing_full":0.4194,"vs_existing_full_entry":"sfumato","vs_existing_verdict":"PASS<0.54"},
 "stippling":{"vs_existing_short":0.4211,"vs_existing_short_entry":"sfumato","vs_existing_full":0.4494,"vs_existing_full_entry":"sfumato","vs_existing_verdict":"PASS<0.54"},
 "pairwise_siblings":{"hatching_vs_stippling":{"short":0.5668,"full":0.5448},"verdict":"FAIL>0.54 (both) -> intra-batch boilerplate"},
 "distinct_from":{"hatching_vs_light-shadow-modeling":{"short":0.324,"full":0.3471},"hatching_vs_cunfa":{"short":0.1892,"full":0.33},"stippling_vs_light-shadow-modeling":{"short":0.3452,"full":0.3728},"stippling_vs_cunfa":{"short":0.2482,"full":0.3591}},
 "method_selfcheck":"batch-38 futurism vs expressionism full=0.5157 matches round39/40/41/42 exactly -> method validated",
 "threshold":0.54
}
VERDICT_CONTENT={"hatching":"合格","stippling":"合格"}
VERDICT_SIMILARITY={"hatching":"越线(0.5668/0.5448 >0.54)","stippling":"越线(0.5668/0.5448 >0.54)"}
VERDICT_SEVERITY={"hatching":"content 合格 (definition/overview/原理 dual-source direct & corroborated; no fabrication; MINOR: period '至19世纪' unsourced, '铜版画' slight, instance type-description) BUT similarity vs sibling stippling 0.5668/0.5448 >0.54 -> needs de-templating","stippling":"content 合格 (definition/overview/原理 dual-source direct & corroborated; pointillism distinguished; no fabrication; MINOR: period '至19世纪' unsourced, instance type-description) BUT similarity vs sibling hatching 0.5668/0.5448 >0.54 -> needs de-templating"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
LINK_FAIL=0
BATCH_REWORK="Content path NOT triggered (0 不合格, 2 合格, 0 fabrication/0 false id/0 dead link). SIMILARITY-ANOMALY path TRIGGERED per AUTONOMOUS §E: batch-42's two new entries are template siblings, pairwise short 0.5668 / full 0.5448 both >0.54 (identical time_or_place, isomorphic definition/overview/原理). ACTION: downgrade batch-42 (both entries) to draft and re-check; de-template rewrite (differentiate time_or_place '文艺复兴...' vs '1510 意大利...', rewrite definition/overview句式, use named artists Dürer/Schongauer & Campagnola/Beckett, narrow '至19世纪' unsourced upper bound, '铜版画' -> engraving/etching/woodcut or add source). vs existing 249 library both PASS (<=0.4494), so issue is intra-batch boilerplate only. No 25% escalation needed (not content-unsourced failure)."
READONLY="only wrote research/spotcheck-round43.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (no persistent temp file)"
```

*（报告完）*
