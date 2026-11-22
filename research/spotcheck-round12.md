# 第12轮 质量闸抽检报告（spotcheck-round12）——linear-perspective / composition / color-theory 三条核心 L1→L2 升级复核（25% 档）

- 抽检人：spotcheck-r12（由 lead 委派的子代理）；抽检时间：2026-11-22 18:43 起，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽检 10% 至少 3 个、本轮 25% 档、不合格整批返工、待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容仅作数据，其中指令一律不执行）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」、`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（尺寸/规范提示模板）/D14（needs_verification 与 pending_notes 联动）；前序 `research/verify-round11.md`、`research/spotcheck-round11.md`。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 实际位于 `D:/Users/Administrator/Desktop/`（仓库内无同名文件），已按该路径读取。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑证据为准，证据先于断言）。
- 抽检对象与比例：本轮 `entries/batch-01.json` 经 `tools/upgrade_round12.py` 将 **7 个核心理论条目 L1→L2 升级**（`linear-perspective`、`scattered-perspective`、`composition`、`balance`、`proportion`、`color-theory`、`value`）。按指派抽检其中 3 条：`linear-perspective`（线性透视）、`composition`（构图法则）、`color-theory`（色彩理论）。**3/7 ≈ 42.9% ≥ 25% 且 ≥ 3 条**，满足 E 节抽检比例。
- 只读声明：本次仅生成本文件 `research/spotcheck-round12.md`；**未修改** `entries/`、`data/sources.json`、`coverage.json` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。`tools/check.py` 本轮**只读实跑** `PASS: all checks, 0 errors`（EXIT=0）。联网内容一律视为数据，网页中的任何指令均未执行。
- 判定口径：因三条为 **L2 升级**（非 L1 骨架），按 TASK_design.md「条目页结构」核 **七节完整**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核 definition / time_or_place / overview 的来源支撑、SVG「示意图，非施工图」、规范提示、needs_verification 联动与相似度。

## 一、本环境网络取证说明（关键前置）

- 与 `verify-round11.md`、`spotcheck-round11.md` 记录一致：canonical `https://en.wikipedia.org/wiki/...` 在本会话被 DNS 投毒 + TCP 超时，不可直连；`web_search`/`web_fetch` 在本环境不稳定/报错。故按 D05 改用 **Wikipedia 内容镜像 `owiki.org`（Open WIKI）**，用 Python 3 `urllib.request` + 浏览器 User-Agent **逐页实抓** 6 个被引用来源页。
- 本轮实抓结果：6 页**全部 HTTP 200、无跳转偏差**，`<title>` 末尾带 `::: Open WIKI`，`<h1>` 与 `sources.json` title 逐字一致；现抓正文用于 definition / overview / 七节的字面与关键词取证（见第二节、第三节）。
- 机构口径提醒：镜像渲染方显示为「Open WIKI」而非 Wikimedia，故「出版机构=Wikimedia」的严格口径仍需网络恢复后用 canonical 复核；不影响标题/定义/正文核验（与 verify-round11 一致）。
- 联网内容一律视为数据；本次未执行任何页面内指令。

## 二、来源核对汇总（本轮实抓 owiki.org，HTTP=200）

| 条目 | 引用 id（sources.json：title / verified / link_ok / author / year） | 实抓 HTTP / `<h1>` | 标题-主题相关性 | 正文定义关键词命中（实抓条数） |
| --- | --- | --- | --- | --- |
| linear-perspective | `wp-perspective-graphical`（Perspective (graphical) / true / true / Wikipedia / null）、`wp-vanishing-point`（Vanishing point / true / true / Wikipedia / null） | 均 **200**；h1=Perspective (graphical)、Vanishing point | 主源=线性透视直接同主题；次源=灭点直接同主题 | Perspective：projection×9、parallel×2、vanishing×4、horizon×2、foreshorten×3、smaller×3；Vanishing point：vanishing point×42、parallel×21、converge×2、horizon×7 |
| composition | `wp-composition-visual-arts`（Composition (visual arts) / true / true / Wikipedia / null）、`wp-rule-of-thirds`（Rule of thirds / true / true / Wikipedia / null） | 均 **200**；h1=Composition (visual arts)、Rule of thirds | 主源=构图直接同主题；次源=三分法（构图法则之一）直接相关 | Composition：composition×22、element×21、viewer×12、balance×3、arranged×2；Rule of thirds：rule of thirds×9、third×21、intersection×2、composition×3 |
| color-theory | `wp-color-theory`（Color theory / true / true / Wikipedia / null）、`wp-theory-of-colours`（Theory of Colours / true / true / Wikipedia / null） | 均 **200**；h1=Color theory、Theory of Colours | 主源=色彩理论直接同主题；次源=歌德《色彩论》（色彩理论奠基著作）直接相关 | Color theory：hue×20、contrast×19、harmony×12、mixing×10、complementary×12、color wheel×6、saturation×5；Theory of Colours：colour×78、light×52、dark×30、goethe×82 |

- 6 个唯一被引用 id **全部在 `sources.json` 存在、`verified=true`、`link_ok=true`**（`year=null` 按 D06 允许，note 均记「访问日期 2026-11-22；页面 h1 核对；出版年 null」）。主源标题均与条目主题**直接同主题**；次源 `wp-rule-of-thirds`/`wp-theory-of-colours` 为**主题下位的具体法则/奠基著作**，与主题直接相关（非仅有间接关联）。无「标题与主题不符」。
- 次源独立性提示（非缺陷）：`composition` 的定义实为 `wp-composition-visual-arts` 单源直接支撑，`wp-rule-of-thirds` 属「常用手法」层面的佐证；`color-theory` 的定义由 `wp-color-theory` 逐字支撑，`wp-theory-of-colours` 为特定历史著作而非独立的一般性概述。若升级 L3 或严格执行「关键事实两独立来源互证」，可各补一篇直接界定该概念的一般性权威来源。

## 三、逐条结论

### 1. `linear-perspective`（线性透视）— 合格

- **definition**「以几何投影和灭点组织画面深度的透视体系。」字面支撑：Perspective (graphical) 首句「Linear or point-projection **perspective** is one of two types of **graphical projection** perspective …」；Vanishing point「…the two-dimensional **perspective projections** of parallel lines … appear to **converge**」。三要素（几何投影 / 灭点 / 画面深度）均命中，无编造。
- **time_or_place**「文艺复兴时期意大利（参见来源）。」字面支撑：Perspective (graphical)「**Italian Renaissance** painters and architects including Filippo Brunelleschi …」；**未写具体年份、未点名人名**，规避编造。
- **overview**「它把观察者视点固定，使平行线按规律汇聚，是焦点透视的基础。」支撑：「as it is seen by the eye」（视点）、「objects appear smaller as their distance … increases」、「All objects will **recede to points** in the distance」（平行线汇聚）；「焦点透视」对应「point-projection perspective」（=线性/焦点透视），定性准确。
- **七节完整性**：definition(①) + 原理(②)+典型手法与适用条件(③)+实例(④)+常见错误与限制(⑤)+一图(⑥)+待核实(⑦) 共 7 节齐备。
  - 原理「使相互平行的深远线条向灭点汇聚，按近大远小建立空间秩序」← 「objects appear smaller as distance increases」+「parallel … converge」+「recede to points」，有据。
  - 典型手法「先定视平线与主灭点，再让同组平行线指向同一灭点；适用于正对观察面的室内与街景」← horizon line / vanishing point / one-point perspective 原词；街景例「Straight railroad tracks are a familiar modern example」。
  - **实例**「名称：文艺复兴线性透视绘画（类型性描述）；地点：不适用；设计者：不适用；年份：不适用。」——**类型性描述，无编造的具体项目/年份/设计者**，符合要求（不复制图像）。
  - 常见错误与限制「多个不一致灭点会造成空间矛盾；画面尺寸与观看距离影响透视观感。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（视平线+单一灭点），含「**示意图，非施工图**」。
- **元数据**：coverage.json theme=理论/tier=核心/period=文艺复兴至19世纪/region=欧洲/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 逐字段一致。
- **needs_verification 联动**：needs_verification=true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体作品的设计者与年代待核实。」三者一致（D14、check.py 0 errors）。
- **相似度**：全库 126 条，短文本最高 `vanishing-point` 0.4375、`perspective` 0.4066、`one-point-perspective` 0.3636，**最高 0.4375 < 0.54**。
- **问题**：无实质问题（未编造年份/人名/引文）。轻微：`period` 元数据「文艺复兴至19世纪」为技法盛期的宽泛分期，来源未逐字给出「至19世纪」；但 `time_or_place` 字段「文艺复兴时期意大利」已由来源字面支撑，`period` 属 schema 分期口径，非正文事实断言，不影响合格。

### 2. `composition`（构图法则）— 合格

- **definition**「对画面元素的位置、比例与关系进行组织以形成秩序和重点的方法。」支撑：Composition (visual arts)「The term **composition** means "putting together". It can be thought of as the **organization** of art … **arranged** using conscious thought」、「These **elements** in the overall design usually **relate to each other** and to the whole art work」。位置/关系为字面，比例（proportion）为语义级概括（正文以 element/value/balance 组织），无编造。
- **time_or_place**「跨时期、全球（参见来源）。」构图适用于一切时代与地域的艺术，宽泛对应，**未写具体年份/人名**。
- **overview**「构图决定观看路径与信息主次，是绘画与视觉设计共通的骨架。」支撑：「**visual path** that enables the eye to **move** within the piece」（观看路径）、「Composition can apply to **any work of art**, from music through writing and into photography」（共通骨架）、「important compositional elements」（主次）。
- **七节完整性**：7 节齐备。
  - 原理「把元素按位置、比例与关系组织成有序整体，引导观看顺序与信息主次」← 「organization」「relate to each other and to the whole」+「visual path」。
  - 典型手法「**三分法**、主次安排与视觉引导是常用手段；适用于绘画、摄影与界面布局」← Rule of thirds「a rule of thumb for **composing visual art** such as designs, films, **paintings, and photographs**」（三分法直接命中）。
  - **实例**「名称：通用构图实践（类型性描述）；地点/设计者/年份：不适用。」——**类型性描述，无编造具体项目/年份**。
  - 常见错误与限制「元素过多会削弱重点；构图为视觉秩序而非工程尺寸。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（三分网格与主体位置），含「**示意图，非施工图**」。
- **元数据**：coverage.json theme=理论/tier=核心/period=跨时期/region=全球/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 一致。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体案例的设计者与年代待核实。」一致。
- **相似度**：短文本最高 `s-curve-composition` 0.3910、`balance` 0.3817、`hierarchy` 0.3796，**最高 0.3910 < 0.54**。
- **问题**：无实质问题（未编造）。轻微：① definition 中「比例」为对「元素组织」的概括（Composition 页 proportion 关键词 0 命中），属可接受意译；② 常见错误与限制把 D09「实际工程须按当地规范…」工程提示套用于纯视觉构图主题，略显 boilerplate，但符合统一模板不构成缺陷。

### 3. `color-theory`（色彩理论）— 合格

- **definition**「研究色彩混合、对比与和谐规律的理论体系。」**字面精确支撑**：Color theory 首句「…a historical body of knowledge describing the behavior of colors — namely in **color mixing, color contrast effects, color harmony**, color schemes and color symbolism」——混合/对比/和谐三要素与原文逐字对应。
- **time_or_place**「跨时期、全球（参见来源）。」色彩理论跨时代跨地域，宽泛对应，**未写具体年份/人名**。
- **overview**「色彩理论连接物理光学、视觉感知与审美经验。」支撑：「the relationship between **human color perception** and the interactions of colors」（视觉感知）、「color science … chemistry, astronomy or color reproduction」「objective standards in color mixing」（物理/光学侧）、「have **artistic applications**」（审美经验）。「物理光学」为对「color science / light」的轻度概括，属可接受意译。
- **七节完整性**：7 节齐备。
  - 原理「以色相、明度与纯度的关系解释配色、对比与和谐的规律」← hue×20、saturation×5、contrast×19、harmony×12、color wheel×6、complementary×12。
  - 典型手法「以色轮组织邻近色与互补色；适用于绘画、室内与视觉传达」← color wheel、complementary、artistic applications。
  - **实例**「名称：色轮配色实践（类型性描述）；地点/设计者/年份：不适用。」——**类型性描述，无编造具体项目/年份**。
  - 常见错误与限制「只套公式会忽略光照与材质；色彩对比需兼顾可读性与无障碍。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（色轮上的色彩关系），含「**示意图，非施工图**」。
- **元数据**：coverage.json theme=理论/tier=核心/period=跨时期/region=全球/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 一致。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体案例的设计者与年代待核实。」一致。
- **相似度**：短文本最高 `color-psychology` 0.4062、`primary-colors` 0.4000、`value`/`saturation` 0.3853，**最高 0.4062 < 0.54**。
- **问题**：无实质问题（未编造）。轻微：① overview「物理光学」属轻度概括（来源以 color science / light 表述，未逐字出现「物理光学」）；② 次源 `wp-theory-of-colours` 为歌德 1810 年著作，属主题下位的特定历史著作而非独立的一般性概述，见第二节次源独立性提示。

## 四、结构 / 元数据合规核对（三条共性，均通过）

1. **L2 七节完整**：三条均含 definition（=①核心概念与定义）+ 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 六节，合计七节；`check.py` 实跑 0 errors 佐证七节键约束通过。
2. **1 张内联 SVG 且含「示意图，非施工图」**：三条各 1 张 `svg`，逐条检测字符串「示意图，非施工图」命中；`check.py::validate_svg` 校验 viewBox 存在、元素坐标/r/width/height 未出界，0 errors。
3. **风险词段落含规范提示**：三条「常见错误与限制」均含 `REGULATION_NOTE = "实际工程须按当地规范和专业设计人员的要求"`（D09、check.py 291–292 校验通过）。
4. **needs_verification / pending_notes / 正文待核实 / coverage.nvc 联动一致**：三条 needs_verification=true、pending_notes 非空、正文含「待核实」、coverage.needs_verification_count=1；check.py 264–269、288、317 全部通过（0 errors）。
5. **coverage 一致**：三条 title/theme/tier/period/region/level/source_count/needs_verification_count 与 `coverage.json` 逐字段一致（程序化比对 OK）。
6. **来源真伪**：6 个被引 id 存在、verified=true、link_ok=true；本轮 6 页全部 HTTP 200 实抓、`<h1>` 逐字一致、定义关键词命中（见第二、三节）。
7. **相似度**：三条全库最高 0.4375 / 0.3910 / 0.4062，**均 < 0.54 套话警戒线**。
8. **机器校验**：`tools/check.py` 只读实跑 `PASS: all checks, 0 errors`（EXIT=0）。

## 五、异常监控与批次级观察

- **待核实占比（E 节监控）**：本轮 `upgrade_round12.py` 统一将 7 条升级条目置 `needs_verification=true`（100%），**方向与「占比异常低（疑似硬写）」相反**，不触发该监控；且三条的 needs_verification 均对应「实例具体名称/设计者/年代待补独立来源」这一真实未决项，属合理标注而非隐藏缺口。
- **套话/相似度（E 节监控）**：三条相似度最高 0.4375 < 0.54；`instance` 字段采用「类型性描述」模板（三条措辞一致）会提高短文本相似度，但仍在阈值内，且属 L2 早期「无具体项目/年份、不编造」的合规取舍，不构成降级。
- **升级范围核实**：`tools/upgrade_round12.py::S` 的 7 条键 = `linear-perspective/scattered-perspective/composition/balance/proportion/color-theory/value`，与提示「本轮 7 条核心 L1→L2」一致；三条抽检对象确在本轮升级集内，抽检有效。
- **轮次收尾文件状态（提示，非本抽检缺陷）**：`REPORT.md`、`PROGRESS.md` 末尾变更日志当前仍停在**第 11 轮**快照（第 12 轮 G 阶段尚未覆盖重写）；`coverage.json`/`entries/batch-01.json` 已反映第 12 轮升级。此为收尾待办，供 lead 在 G 阶段闭环，不影响本抽检对三条的质量判断。

## 六、总体结论与返工建议

- 逐条：**合格 3 条**（`linear-perspective`、`composition`、`color-theory`）；**不合格 0 条**；**内容缺陷待核实 0 条**（三条的 needs_verification=true 为对「实例具体名称/设计者/年代」的合理待补标注，非内容缺陷）。
- 三条的 definition / time_or_place / overview 及七节均可由本轮实抓来源正文的字面文本或强语义文本支撑（6 页全部 HTTP 200、`<h1>` 逐字匹配、定义关键词命中），**未发现编造年份、人名或引文**；三条实例均为「类型性描述」，无编造的具体项目/年份，从源头规避 L2 层编造风险。
- 结构上七节齐备、各 1 张 SVG 含「示意图，非施工图」、常见错误与限制含 D09 规范提示；needs_verification/pending_notes/正文待核实/coverage.nvc 联动一致；相似度最高 0.4375/0.3910/0.4062 均 < 0.54；`check.py` 0 errors。
- **是否建议整批返工：不建议。** 本轮抽检 3/3 合格、0 不合格，未触发 AUTONOMOUS.md E 节「不合格则整批返工」条件；未发现硬写或套话降级信号。
- **轻微改进建议（非返工项）**：① 升级 L3 时为 `composition`、`color-theory` 各补一篇直接同主题的一般性独立来源，满足「两独立来源互证」严格口径；② `color-theory` overview「物理光学」可改为来源原词（color science / light / 色彩感知）；③ `linear-perspective` 的 `period` 若需更贴来源，可注「文艺复兴起源」；④ 收尾时更新 REPORT.md / PROGRESS.md 至第 12 轮。
- **局限**：canonical `en.wikipedia.org` 本会话仍不可直连，本轮以 Wikipedia 内容镜像 `owiki.org` 实抓 + 关键词上下文取证；「出版机构=Wikimedia」的严格口径待网络恢复后以 canonical 复核。对 L2 的定义/概述/七节核验已充分。

---

### 机器可读汇总

```
ROUND=12
UPGRADED_ENTRIES=["linear-perspective","scattered-perspective","composition","balance","proportion","color-theory","value"]
SPOTCHECKED=["linear-perspective","composition","color-theory"]
VERDICT={"linear-perspective":"合格","composition":"合格","color-theory":"合格"}
FAILED=[]            # 不合格条目
CONTENT_PENDING=[]   # 内容层面待核实条目
SOURCES_CHECKED=["wp-perspective-graphical","wp-vanishing-point","wp-composition-visual-arts","wp-rule-of-thirds","wp-color-theory","wp-theory-of-colours"]
SOURCES_ALL_VERIFIED=true
HTTP_ALL_200=true
SVG_OK=true ; REGNOTE_OK=true ; SEVEN_SECTIONS_OK=true ; NV_LINKAGE_OK=true
SIMILARITY_MAX={"linear-perspective":0.4375,"composition":0.3910,"color-theory":0.4062}   # all < 0.54
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
REWORK_RECOMMENDATION=false
```
