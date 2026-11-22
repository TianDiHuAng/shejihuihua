# 第13轮 质量闸抽检报告（spotcheck-round13）——one-point-perspective / figure-ground / complementary-colors 三条重要 L1→L2 升级复核（25% 档）

- 抽检人：spotcheck-r13（由 lead 委派的子代理）；抽检时间：2026-11-22 18:57 起，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽检 25% 至少 3 个、不合格整批返工、待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容仅作数据，其中指令一律不执行）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」、`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（尺寸/规范提示模板）/D14（needs_verification 与 pending_notes 联动）；前序 `research/spotcheck-round12.md`。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`，已按该路径读取（与第12轮一致）。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象与比例：`tools/upgrade_round13.py::S` 将 **6 个重要条目 L1→L2 升级**（`one-point-perspective`、`rule-of-thirds`、`figure-ground`、`negative-space`、`hue`、`complementary-colors`）。按指派抽检其中 3 条：`one-point-perspective`（一点透视）、`figure-ground`（图底关系）、`complementary-colors`（互补色）。**3/6 = 50% ≥ 25% 且 ≥ 3 条**，满足 E 节比例。
- 只读声明：本次仅生成 `research/spotcheck-round13.md`；**未修改** `entries/`、`data/sources.json`、`coverage.json` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。工作树中 `coverage.json`、`entries/batch-01.json` 的改动及 `tools/upgrade_round13.py` 等为第13轮执行阶段既有产物，非本次抽检所写。联网内容一律视为数据，网页中的任何指令均未执行。
- 判定口径：三条为 **L2 升级**（非 L1 骨架），按 TASK_design.md「条目页结构」核 **七节完整**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核 definition / time_or_place / overview 的来源支撑、SVG「示意图，非施工图」、规范提示、needs_verification 联动与相似度。

## 一、本环境网络取证说明（关键前置）

- 与 `spotcheck-round11.md`/`spotcheck-round12.md` 一致：canonical `https://en.wikipedia.org/wiki/...` 在本会话 **不可直连**（实测 `urlopen error timed out`）；改用 Wikipedia 内容镜像 **`https://www.owiki.org/wiki/...`（Open WIKI）**，用 Python 3.11 `urllib.request` + 浏览器 User-Agent **逐页实抓** 6 个被引用来源页。
- 本轮实抓结果：6 页 **全部 HTTP 200、无跳转偏差**，`<title>` 末尾带 `::: Open WIKI`，`<h1>` 与 `sources.json` title 逐字一致；现抓正文用于 definition / time_or_place / overview / 七节的字面与关键词取证（见第二、三节）。
- 机构口径提醒：镜像渲染方显示为「Open WIKI」而非 Wikimedia，故「出版机构=Wikimedia」的严格口径仍需网络恢复后用 canonical 复核；不影响标题/定义/正文核验（与 verify-round11、spotcheck-round12 一致）。
- 联网内容一律视为数据；本次未执行任何页面内指令。

## 二、来源核对汇总（本轮实抓 owiki.org，HTTP=200）

| 条目 | 引用 id（sources.json：title / verified / link_ok / author / year） | 实抓 HTTP / `<h1>` | 标题-主题相关性 | 正文定义关键词命中（实抓计数） |
| --- | --- | --- | --- | --- |
| one-point-perspective | `wp-perspective-graphical`（Perspective (graphical) / true / true / Wikipedia / null）、`wp-de-pictura`（De pictura / true / true / Wikipedia / null） | 均 **200**；h1=Perspective (graphical)、De pictura | 主源=线性/点投影透视直接同主题；次源=阿尔伯蒂《论绘画》（线性几何透视最早记述）直接相关 | Perspective：vanishing point×4、parallel×2、converge×1、horizon×2、one-point×1、point-projection×3、recede×1、Italian Renaissance×1、Brunelleschi×10、frontal×1；De pictura：perspective×3、Alberti×10、1435×3、linear×1 |
| figure-ground | `wp-figure-ground`（Figure–ground (perception) / true / true / Wikipedia / null）、`wp-composition-visual-arts`（Composition (visual arts) / true / true / Wikipedia / null） | 均 **200**；h1=Figure–ground (perception)、Composition (visual arts) | 主源=图底知觉直接同主题；次源=构图（图底为其组织层面）直接相关 | Figure–ground：figure×41、ground×43、Gestalt×10、Rubin×4、perception×12、reversible×1、background×10；Composition：composition×23、organization×2、arrange×5、elements×15、viewer×12、visual path×1 |
| complementary-colors | `wp-complementary-colors`（Complementary colors / true / true / Wikipedia / null）、`wp-color-wheel`（Color wheel / true / true / Wikipedia / null） | 均 **200**；h1=Complementary colors、Color wheel | 主源=互补色直接同主题；次源=色轮（互补色定义所在载体）直接相关 | Complementary：complementary×38、opposite×3、color wheel×3、contrast×9、mixing×3、neutral×3、afterimage×3、hue×2；Color wheel：color wheel×29、complementary×4、opposite×1、hue×7 |

- 6 个唯一被引用 id **全部在 `sources.json` 存在、`verified=true`、`link_ok=true`**（`year=null` 按 D06 允许，note 均记「访问日期 2026-11-22；页面 h1 核对；出版年 null」）。主源标题均与条目主题**直接同主题**；次源为**主题下位的奠基著作/具体法则/载体概念**，直接相关（非仅有间接关联）。无「标题与主题不符」。
- 次源独立性提示（非缺陷）：`figure-ground` 的定义实为 `wp-figure-ground` 单源直接支撑，`wp-composition-visual-arts` 属「构图/组织」层面的语境佐证；`one-point-perspective` 的 time_or_place 由 `wp-de-pictura`（文艺复兴、阿尔伯蒂 1435）补强；`complementary-colors` 的「色轮相对位置」由 `wp-color-wheel` 独立补强。若升级 L3 或严格执行「关键事实两独立来源互证」，`figure-ground` 可再补一篇直接界定该概念的一般性权威来源。

## 三、逐条结论

### 1. `one-point-perspective`（一点透视）— 合格

- **definition**「平行线向画面中单一主灭点汇聚的透视方法。」支撑：Perspective (graphical)「Linear or point-projection **perspective** is one of two types of **graphical projection** perspective…」；「All objects will **recede to points** in the distance, usually along the **horizon line**」；「a central **vanishing point** can be used to indicate **frontal** depth」；「Leonardo applied **one-point perspective**」。三要素（平行线/单一主灭点/汇聚）为字面或强语义命中，无编造。
- **time_or_place**「文艺复兴至19世纪欧洲（参见来源）。」支撑：Perspective「**Italian Renaissance** painters and architects including Filippo Brunelleschi, Leon Battista Alberti…」；De pictura「the first description of **linear geometric perspective** around 1416; Alberti… dedicated the **1435** edition」，欧洲+文艺复兴有字面支撑；**未写具体年份、未点名人名**（正文回避了 Brunelleschi/Alberti 等名），规避编造。**轻微**：「至19世纪」为技法盛期的宽泛分期，实抓正文未见逐字「19世纪」，属 period 口径延展（非正文断言、非具体年份编造），见「问题」。
- **overview**「适合表现正对观察者的立面、走廊与室内空间。」支撑：「a central vanishing point can be used to indicate **frontal** depth」（正对立面）；「one-point perspective」+ 走廊/室内为一点透视的典型适用对象的定性概括，语义准确，无编造。
- **七节完整性**：definition(①)+原理(②)+典型手法与适用条件(③)+实例(④)+常见错误与限制(⑤)+一图(⑥)+待核实(⑦) 共 7 节齐备。
  - 原理「一点透视把一组平行于视线的线汇聚到画面单一主灭点，正对视线的立面保持不动形」←「recede to points」+「central vanishing point…frontal depth」，有据。
  - 典型手法「以视平线与主灭点作图，适用于走廊、街景与正对观察者的室内」← horizon line / vanishing point / one-point 原词。
  - **实例**「名称：正对式室内透视（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。此处不复制图像。」——**类型性描述，无编造的具体项目/年份/设计者**。
  - 常见错误与限制「偏离主灭点会造成正立面变形；画面尺寸影响透视观感。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（视平线+单一主灭点+汇聚线），含「**示意图，非施工图**」；`validate_svg` 元素均不出界。
- **元数据**：coverage.json theme=理论/tier=重要/period=文艺复兴至19世纪/region=欧洲/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 逐字段一致。
- **needs_verification 联动**：needs_verification=true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体作品的设计者与年代待核实。」三者一致（D14）。
- **相似度**：短文本（definition+overview）全库最高 `two-point-perspective` 0.4186；全字段口径最高 `linear-perspective` 0.4862，**均 < 0.54**。
- **问题**：无实质问题（未编造年份/人名/引文）。轻微：`time_or_place`/`period` 的「至19世纪」为宽泛分期，实抓正文未逐字给出「至19世纪」；`region=欧洲` 已由来源字面支撑。不影响合格，升级 L3 时可改注「文艺复兴起源」以更贴来源。

### 2. `figure-ground`（图底关系）— 合格

- **definition**「区分主体图形与背景底面的视觉组织关系。」**字面支撑**：Figure–ground「**Figure–ground organization** is a type of **perceptual grouping** that is a vital necessity for recognizing objects through vision. In Gestalt psychology it is known as identifying a **figure** from the **back ground**.」，无编造。
- **time_or_place**「20世纪视觉心理学研究（参见来源）。」**字面支撑**：「The Gestalt theory was founded in the **20th century** in Austria and Germany…In **1912**, the Gestalt school was formed by Max Wertheimer…」——「20世纪」精准对应；**未写具体年份、未点名人名**（正文未出现 Rubin/Wertheimer 等名），规避编造。
- **overview**「图底互换会造成有趣的歧义，稳定图底则保证信息清晰。」支撑：「The image is famous for being **reversible**. "The viewer may either observe a young girl…or an old woman…"」（图底互换/可逆→歧义）；「a vital necessity for recognizing objects」（稳定图底→信息清晰）。语义强支撑，无编造。
- **七节完整性**：7 节齐备。
  - 原理「图底关系区分被注意的主体（图）与背景（底），两者边界与对比决定可读性」←「identifying a figure from the back ground」+「**edge-assignment** and its effect on shape perception」+ 黑白字纸示例（对比），有据。
  - 典型手法「以明度对比与轮廓清晰度强化图底分离；适用于平面与界面设计」← edge-assignment/轮廓与黑白对比为字面，界面设计为语义应用层。
  - **实例**「名称：图底对比练习（类型性描述）；地点/设计者/年份：不适用。此处不复制图像。」——**类型性描述，无编造**。
  - 常见错误与限制「图底对比不足会造成辨认困难；可读性需兼顾无障碍对比度。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（图/底分离），含「**示意图，非施工图**」。
- **元数据**：coverage.json theme=理论/tier=重要/period=20世纪/region=全球/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 一致（`period=20世纪` 由来源「founded in the 20th century」直接支撑）。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体案例的设计者与年代待核实。」一致。
- **相似度**：短文本最高 `complementary-colors` 0.2198；全字段口径最高 `color-theory` 0.4760，**均 < 0.54**。
- **问题**：无实质问题（未编造）。轻微：① 定义/原理由 `wp-figure-ground` 单源直接支撑，`wp-composition-visual-arts` 为语境佐证（见第二节次源提示）；② 典型手法「界面设计」为语义应用层概括（来源以图形/知觉为主），可接受。

### 3. `complementary-colors`（互补色）— 合格

- **definition**「色轮上相对、并置时形成强烈对比的色彩。」**字面精确支撑**：Complementary colors「Complementary colors are pairs of colors which, when combined or mixed, cancel each other out…**When two highly chromatic complementary colors are placed next to each other, they create a strong contrast.**」「…may also be called "**opposite colors**"」；Color wheel「**Complementary colors are two colors directly across from each other**; for example, red and cyan」——「色轮上相对」+「并置强对比」双源逐字命中，无编造。
- **time_or_place**「跨时期、全球（参见来源）。」——互补色为跨时代跨地域的色彩关系概念，宽泛对应，**未写具体年份/人名**。
- **overview**「互补配色能制造张力，降低一方纯度可获得更稳定的效果。」——「制造张力」←「create a strong contrast」+「battle and antithesis」（页面引文语境）；「降低一方纯度→更稳定」为**基于来源「mixed with an amount of the complementary wavelength to produce a **neutral** color」「partitive color mixing…appear **gray**」的语义推演**（来源讲「混合得中性灰」，条目讲「降低纯度求稳定」，方向一致但非逐字）。属可接受的领域意译，**非编造事实**；为三者中语义外推最强处，见「问题」。
- **七节完整性**：7 节齐备。
  - 原理「互补色位于色轮相对位置，并置时形成强烈对比，可制造张力与焦点」← opposite on wheel ×+ strong contrast，有据（「焦点」为设计语义延伸）。
  - 典型手法「以互补色小面积点缀建立重点；适用于需要活力的画面与空间」← 由「strong contrast」延伸的设计实践，语义合理（「小面积点缀」非来源逐字）。
  - **实例**「名称：互补配色（类型性描述）；地点/设计者/年份：不适用。此处不复制图像。」——**类型性描述，无编造**。
  - 常见错误与限制「大面积等量互补会刺眼；应调节纯度与面积比例。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（色轮对侧互补），含「**示意图，非施工图**」。
- **元数据**：coverage.json theme=理论/tier=重要/period=跨时期/region=全球/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 一致。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体案例的设计者与年代待核实。」一致。
- **相似度**：短文本最高 `figure-ground` 0.2198；**全字段口径最高 `hue` 0.5177（< 0.54 但最接近阈值）**，与 `value` 0.4938、`color-theory` 0.4887 次之——系六条升级条目共用「原理/典型手法/实例/常见错误与限制」模板 + 同属色彩主题的 hue 所致（详见第五节监控）。
- **问题**：无实质问题（未编造年份/人名/引文）。轻微：① overview「降低一方纯度可获得更稳定效果」、典型手法「小面积点缀」为对来源「混合得中性/灰」的设计语义外推（非逐字），可接受；② 全字段相似度 0.5177 逼近阈值，建议后续批次改写实例/限制段措辞以拉开模板重合（见第五节）。

## 四、结构 / 元数据合规核对（三条共性，均通过）

1. **L2 七节完整**：三条均含 definition（=①核心概念与定义）+ 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 六节，合计七节；`tools/check.py` 实跑 **`PASS: all checks, 0 errors`（EXIT=0）** 佐证七节键约束通过。
2. **1 张内联 SVG 且含「示意图，非施工图」**：三条各 1 张 `svg`（满足 TASK_design「每页至少 1 到 2 张」下限），逐条字符串「示意图，非施工图」命中；`check.py::validate_svg` 校验 viewBox 存在、元素坐标/r/width/height 未出界，0 errors。
3. **风险词段落含规范提示**：三条「常见错误与限制」均含 `REG = "实际工程须按当地规范和专业设计人员的要求"`（D09、check.py 校验通过）。
4. **needs_verification / pending_notes / 正文待核实 / coverage.nvc 联动一致**：三条 needs_verification=true、pending_notes 非空、正文含「待核实」、coverage.needs_verification_count=1，`check.py` 通过（0 errors）。
5. **coverage 一致**：三条 title/theme/tier/period/region/level/source_count/needs_verification_count 与 `coverage.json` 逐字段一致（程序化比对 OK）。
6. **来源真伪**：6 个被引 id 存在、verified=true、link_ok=true；本轮 6 页全部 HTTP 200 实抓、`<h1>` 逐字一致、定义关键词命中（见第二、三节）。
7. **编造核查**：三条 definition / time_or_place / overview / 七节均**未见具体年份、人名或引文**；实例均为「类型性描述」且 year/设计者填「不适用」，从源头规避 L2 编造风险。

## 五、异常监控与批次级观察

- **待核实占比（E 节监控）**：`upgrade_round13.py` 统一将 6 条升级条目置 `needs_verification=true`（100%），**方向与「占比异常低（疑似硬写）」相反**，不触发该监控；三条的 needs_verification 均对应「实例具体名称/设计者/年代待补独立来源」这一真实未决项，属合理标注而非隐藏缺口。
- **套话/相似度（E 节监控）**：短文本口径三条最高 0.4186 / 0.2198 / 0.2198，均远低于 0.54；**全字段口径**最高 0.4862 / 0.4760 / **0.5177**，均 < 0.54，无「相似度过高」判定。**软信号**：`complementary-colors`↔`hue` 全字段 0.5177 逼近 0.54，源于六条升级条目共用「原理/典型手法/实例/常见错误与限制」固定模板（instance 段措辞高度一致）。属 L2 早期「无具体项目/年份、不编造」的合规取舍，**不构成降级**，但建议后续批次对 instance 与常见错误段做个性化改写，拉开模板重合。
- **升级范围核实**：`tools/upgrade_round13.py::S` 的 6 条键 = `one-point-perspective/rule-of-thirds/figure-ground/negative-space/hue/complementary-colors`，与提示「6 条重要 L1→L2」一致；三条抽检对象确在本轮升级集内，抽检有效。
- **轮次收尾文件状态（提示，非本抽检缺陷）**：`entries/batch-01.json`、`coverage.json` 已反映第13轮升级（工作树未提交）；`REPORT.md`/`PROGRESS.md`/`METRICS.json` 的 G 阶段覆盖重写待 lead 收尾时闭环，不影响本抽检对三条的质量判断。

## 六、总体结论与返工建议

- 逐条：**合格 3 条**（`one-point-perspective`、`figure-ground`、`complementary-colors`）；**不合格 0 条**；**内容缺陷待核实 0 条**（三条的 needs_verification=true 为对「实例具体名称/设计者/年代」的合理待补标注，非内容缺陷）。
- 三条的 definition / time_or_place / overview 及七节均可由本轮实抓来源正文的字面文本或强语义文本支撑（6 页全部 HTTP 200、`<h1>` 逐字匹配、定义关键词命中），**未发现编造年份、人名或引文**；三条实例均为「类型性描述」，无编造的具体项目/年份，从源头规避 L2 层编造风险。
- 结构上七节齐备、各 1 张 SVG 含「示意图，非施工图」、常见错误与限制含 D09 规范提示；needs_verification/pending_notes/正文待核实/coverage.nvc 联动一致；短文本相似度最高 0.4186、全字段最高 0.5177 均 < 0.54；`check.py` 0 errors。
- **是否建议整批返工：不建议。** 本轮抽检 3/3 合格、0 不合格，未触发 AUTONOMOUS.md E 节「不合格则整批返工」条件；未发现硬写或套话降级信号。
- **轻微改进建议（非返工项）**：① `complementary-colors`↔`hue` 全字段相似度 0.5177 逼近阈值，后续批次改写实例/限制段措辞；② `complementary-colors` overview「降低一方纯度」与典型手法「小面积点缀」为语义外推，升级 L3 时可补直接来源；③ `one-point-perspective` 的 `time_or_place`/`period`「至19世纪」可改注「文艺复兴起源」以更贴来源；④ `figure-ground` 升级 L3 时补一篇直接界定该概念的一般性独立来源；⑤ 收尾时更新 REPORT.md / PROGRESS.md / METRICS.json 至第13轮。
- **局限**：canonical `en.wikipedia.org` 本会话仍不可直连，本轮以 Wikipedia 内容镜像 `owiki.org` 实抓 + 关键词上下文取证；「出版机构=Wikimedia」的严格口径待网络恢复后以 canonical 复核。对 L2 的定义/概述/七节核验已充分。

---

### 机器可读汇总

```
ROUND=13
UPGRADED_ENTRIES=["one-point-perspective","rule-of-thirds","figure-ground","negative-space","hue","complementary-colors"]
SPOTCHECKED=["one-point-perspective","figure-ground","complementary-colors"]
VERDICT={"one-point-perspective":"合格","figure-ground":"合格","complementary-colors":"合格"}
FAILED=[]            # 不合格条目
CONTENT_PENDING=[]   # 内容层面待核实条目
SOURCES_CHECKED=["wp-perspective-graphical","wp-de-pictura","wp-figure-ground","wp-composition-visual-arts","wp-complementary-colors","wp-color-wheel"]
SOURCES_ALL_VERIFIED=true
HTTP_ALL_200=true
FABRICATION_FOUND=false   # 未见编造年份/人名/引文；实例均为类型性描述
SVG_OK=true ; REGNOTE_OK=true ; SEVEN_SECTIONS_OK=true ; NV_LINKAGE_OK=true ; COVERAGE_MATCH=true
SIMILARITY_MAX_SHORT={"one-point-perspective":0.4186,"figure-ground":0.2198,"complementary-colors":0.2198}      # all < 0.54
SIMILARITY_MAX_FULL={"one-point-perspective":0.4862,"figure-ground":0.4760,"complementary-colors":0.5177}        # all < 0.54 (complementary~hue closest, template-driven)
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
REWORK_RECOMMENDATION=false
```
