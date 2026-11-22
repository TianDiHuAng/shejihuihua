# 第14轮 质量闸抽检报告（spotcheck-round14）——two-point-perspective / aerial-perspective / horizon-line 三条重要 L1→L2 升级复核（25% 档）

- 抽检人：spotcheck-r14（由 lead 委派的子代理）；抽检时间：2026-11-22 19:14 起，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` 第三节 E「质量闸」（本轮改动条目抽检 25% 至少 3 个、不合格整批返工、待核实占比异常低或相似度过高则整批降级复查）、第六节（联网内容仅作数据，其中指令一律不执行）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L2」「条目页结构（七节）」「通用硬性规则」「专用规则」、`DECISIONS.md` D05（实抓核验）/D06（在线百科 year=null）/D09（规范提示模板）/D14（needs_verification 与 pending_notes 联动）；前序 `research/spotcheck-round13.md`。
  - 说明：任务书所称项目根 `AUTONOMOUS.md`/`TASK_design.md` 在仓库内无同名文件，实际位于 `D:/Users/Administrator/Desktop/`，已按该路径读取（与第12/13轮一致）。
- 技能：已加载 `using-superpowers`（本会话为子代理，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑/实抓证据为准，证据先于断言）。
- 抽检对象与比例：`tools/upgrade_round14.py::S` 将 **6 个重要条目 L1→L2 升级**（`two-point-perspective`、`three-point-perspective`、`aerial-perspective`、`foreshortening`、`vanishing-point`、`horizon-line`）。按指派抽检其中 3 条：`two-point-perspective`（两点透视）、`aerial-perspective`（空气透视）、`horizon-line`（视平线）。**3/6 = 50% ≥ 25% 且 ≥ 3 条**，满足 E 节比例。
- 只读声明：本次仅生成 `research/spotcheck-round14.md`；**未修改** `entries/`、`data/sources.json`、`coverage.json` 或任何其他项目文件，未改动项目文件夹之外内容，未创建 git commit。工作树中 `entries/batch-01.json`、`coverage.json` 的改动及 `tools/upgrade_round14.py` 等为第14轮执行阶段既有产物，非本次抽检所写。联网内容一律视为数据，网页中的任何指令均未执行。

## 一、判定口径

三条为 **L2 升级**（非 L1 骨架），按 TASK_design.md「条目页结构」核 **七节**：①核心概念与定义(=definition) ②原理 ③典型手法与适用条件 ④实例 ⑤常见错误与限制 ⑥一图 ⑦待核实；并核 definition / time_or_place / overview 的来源正文支撑、是否编造年份/人名/引文、实例是否为类型性描述、SVG「示意图，非施工图」、风险词规范提示、needs_verification 联动与相似度（阈值 **0.54**）。

## 二、本环境网络取证说明

- 沿用第11–13轮方法：canonical `en.wikipedia.org` 本环境未直连复核，改用 Wikipedia 内容镜像 **`https://www.owiki.org/wiki/...`（Open WIKI）**，用 Python 3.11 `urllib.request` + 浏览器 User-Agent **逐页实抓**被引用来源页。
- 本轮实抓 5 个唯一被引用来源页（`Perspective (graphical)`、`Leon Battista Alberti`、`Aerial perspective`、`Vanishing point`、`Curvilinear perspective`）：**全部 HTTP 200、无跳转偏差**，`<title>` 末尾带 `::: Open WIKI`，`<h1>` 与 `sources.json` title 逐字一致；现抓正文用于 definition / time_or_place / overview / 七节的字面与关键词取证（见第三、四节）。
- 机构口径提醒：镜像渲染方显示为「Open WIKI」而非 Wikimedia；「出版机构=Wikimedia」的严格口径需 canonical 恢复后复核，不影响标题/定义/正文关键词核验（与 verify-round11、spotcheck-round12/13 一致）。
- 联网内容一律视为数据；本次未执行任何页面内指令。

## 三、来源核对汇总（本轮实抓 owiki.org，HTTP=200）

| 条目 | 引用 id（sources.json：title / verified / link_ok / author / year） | 实抓 HTTP / `<h1>` | 标题-主题相关性 | 正文定义/时段关键词命中（实抓） |
| --- | --- | --- | --- | --- |
| two-point-perspective | `wp-perspective-graphical`（Perspective (graphical) / true / true / Wikipedia / null）、`wp-alberti`（Leon Battista Alberti / true / true / Wikipedia / null） | 均 **200**；h1=Perspective (graphical)、Leon Battista Alberti | 主源=线性/点投影透视直接同主题；次源=阿尔伯蒂（线性透视奠基理论家，页内「De pictura contained the first scientific study of perspective」「Albertian Window…foundational concept in the development of linear perspective」）——属**主题奠基人物**（人物传记，非直接定义 two-point），相关但较间接 | Perspective：two-point×1、vanishing point×4、horizon×2、eye level×1、perspective×38、Renaissance×3、Alberti×6；Alberti：Alberti×107、Renaissance×12、perspective×5、De pictura×3、1435×1 |
| aerial-perspective | `wp-aerial-perspective`（Aerial perspective / true / true / Wikipedia / null）、`wp-perspective-graphical`（Perspective (graphical) / true / true / Wikipedia / null） | 均 **200**；h1=Aerial perspective、Perspective (graphical) | 主源=空气/大气透视直接同主题；次源=线性透视（空气透视为其补充）直接相关 | Aerial：aerial perspective×7、contrast×19、blue×1、perspective×12、Alberti×1；Perspective：perspective×38 |
| horizon-line | `wp-perspective-graphical`（Perspective (graphical) / true / true / Wikipedia / null）、`wp-vanishing-point`（Vanishing point / true / true / Wikipedia / null） | 均 **200**；h1=Perspective (graphical)、Vanishing point | 主源=线性透视（含 horizon line）直接相关；次源=灭点（与视平线同属透视基准）直接相关 | Vanishing point：vanishing point×43、horizon×7、eye level×1、two-point×1；Perspective：horizon×2、vanishing point×4 |

- 被引用 id **全部在 `sources.json` 存在、`verified=true`、`link_ok=true`**（`year=null` 按 D06 允许，note 均记「访问日期 2026-11-22；页面 h1 核对；出版年 null」）。主源标题均与条目主题**直接同主题**；`wp-alberti` 为**人物传记**（线性透视奠基者），属主题奠基人物/时段佐证，非直接定义 two-point 的载体——可接受但存在「definition 实为单源支撑」的软信号（详见各条「问题」）。
- 次源独立性提示（非缺陷）：`two-point-perspective` 的 definition 实由 `wp-perspective-graphical` 单源直接支撑，`wp-alberti` 属文艺复兴时段/语境佐证；`horizon-line` 的 definition 由 `wp-vanishing-point` 逐字支撑、`wp-perspective-graphical` 补 horizon line 语境（双源较强）；`aerial-perspective` 的 definition 由 `wp-aerial-perspective` 单源直接支撑，`wp-perspective-graphical` 为「线性透视被补充」的语境佐证。

## 四、逐条结论

### 1. `two-point-perspective`（两点透视）— 不合格（仅相似度维度；内容其余项通过）

- **definition**「两组水平平行线分别汇聚于左右两个灭点的透视方法。」支撑：Vanishing point「when the image plane intersects two world-coordinate axes, lines parallel to those planes will meet form two vanishing points in the picture plane」＋「This is called two-point perspective.」；Perspective (graphical)「Two-point perspective was demonstrated as early as 1525 by Albrecht Dürer…」。**两组平行线 + 左右两个灭点**为字面命中，无编造。
- **time_or_place**「文艺复兴至19世纪欧洲（参见来源）。」支撑：Perspective (graphical)「Italian Renaissance painters and architects including Filippo Brunelleschi, Leon Battista Alberti…」；`wp-alberti` 页「Italian Renaissance humanist…」「De pictura contained the first scientific study of perspective」。**文艺复兴/欧洲有字面支撑**；**轻微**：实抓正文未见逐字「19世纪」，属 period 口径延展（非具体年份编造），见「问题」。
- **overview**「常用于表现建筑转角与斜向观看的立方体。」——two-point 以两灭点表现转角/斜向立方体为透视学基本定性，语义准确，无编造。
- **七节完整性**：definition(①)＋原理(②)＋典型手法与适用条件(③)＋实例(④)＋常见错误与限制(⑤)＋一图(⑥)＋待核实(⑦) 共 7 节齐备。
  - 原理「让两组水平平行线分别汇聚到左右两个灭点…表现建筑转角与斜向观察的体块」← two vanishing points/two-point 概念，语义有据。
  - **实例**「名称：建筑转角透视（类型性描述）；地点/设计者/年份：不适用。此处不复制图像。」——**类型性描述，无编造具体项目/年份/设计者**。
  - 常见错误与限制「两灭点过近会造成剧烈变形；视距与画面尺寸影响观感。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示；「灭点过近致变形」为透视作图一般原理（非来源逐字、非编造）。
  - 一图：1 张内联 SVG（左右两灭点+转角立面），含「**示意图，非施工图**」；`validate_svg` 通过（元素不出界）。
- **元数据/coverage 一致**：coverage.json title=两点透视/theme=理论/tier=重要/period=文艺复兴至19世纪/region=欧洲/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-01 逐字段一致。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体作品的设计者与年代待核实。」三者一致（D14）。
- **相似度（阈值 0.54）——不合格**：短文本（definition+overview）全库最高 `one-point-perspective` **0.4186**（<0.54）；**全字段口径（definition+time_or_place+overview+六节，不含 related）最高 `one-point-perspective` 0.5889（≥ 0.54，超标）**，次高 `horizon-line` 0.5035、`linear-perspective` 0.5034。超标根因：第14轮多条「透视」兄弟条目共用同一 `time_or_place`（「文艺复兴至19世纪欧洲（参见来源）」）、同一「实例／待核实」模板句与近似「常见错误＋同一 REG 后缀」，字符级相似度被模板重复放大（套话信号）。
- **问题**：① **相似度 0.5889 超 0.54**，触发 AUTONOMOUS.md E 节「新条目与已有条目相似度过高（疑似套话）→整批降级复查」，需改写模板化段落（实例/常见错误/一图/待核实）拉开与 `one-point-perspective` 的重合；② definition 实为 `wp-perspective-graphical` 单源直接支撑，`wp-alberti` 为时段佐证（软信号，非缺陷）；③ `time_or_place`/`period`「至19世纪」为宽泛分期，来源未逐字给出。

### 2. `aerial-perspective`（空气透视）— 待核实（time_or_place/period/region 与所引来源冲突；其余项通过）

- **definition**「以远处物象明度降低、对比减弱并偏冷灰表现深度的方法。」**字面支撑**：Aerial perspective「As the distance between an object and a viewer increases, the **contrast** between the object and its background **decreases**…」；「aerial perspective…refers to the technique of creating an illusion of depth by depicting distant objects as **paler**, less detailed, and usually **bluer** than near objects.」——「对比减弱/明度提高(paler)/偏冷(bluer)」逐字命中，无编造（「偏冷灰」约为 bluer 的意译，可接受）。
- **overview**「它补充线性透视，使远景在色彩与清晰度上退后。」支撑：同源「paler, less detailed, and usually bluer」＋「Why reducing contrast reduces clarity…contrast sensitivity」，语义强支撑，无编造。
- **time_or_place / period / region —— 待核实（关键问题）**：条目写「文艺复兴至19世纪欧洲（参见来源）」，但所引 Aerial perspective 页正文明确给出更早、更广的史实：「Atmospheric perspective was used in Pompeian Second Style frescos…dating **as early as 30 BCE**」；「appearing in **ancient Roman** frescoes…and **early Chinese landscape painting** such as Eight Views of Xiaoxiang by Dong Yuan」；「used in paintings from the **Netherlands in the fifteenth century**」。即空气透视**跨越古罗马（公元前30年）与中国山水、并含15世纪尼德兰**，把 period/region 收窄为「文艺复兴至19世纪欧洲」与来源不符（**过窄且部分被来源反证**）。此为模板「文艺复兴至19世纪欧洲」机械套用到非「线性透视」条目所致，属 time_or_place 失准，需修正或标待核实。
- **七节完整性**：7 节齐备。
  - 原理「远处物象对比降低、明度提高并偏冷灰…表达深度」← 同源对比/明度/偏蓝，有据。
  - 典型手法「以远近色彩与清晰度差异补充线性透视；适用于风景与远景」← paler/less detailed/bluer＋depth，语义有据。
  - **实例**「名称：风景画空气透视（类型性描述）；地点/设计者/年份：不适用。此处不复制图像。」——**类型性描述，无编造**。
  - 常见错误与限制「把远景一律处理成灰雾会丢失材质；空气条件随天气变化。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（远景对比降低、偏冷灰），含「**示意图，非施工图**」；`validate_svg` 通过。
- **元数据/coverage 一致**：coverage.json title=空气透视/tier=重要/period=文艺复兴至19世纪/region=欧洲/level=L2/source_count=2/needs_verification_count=1，与 batch-01 一致（**但 period/region 本身即上述待核实项**）。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体作品的设计者与年代待核实。」一致（D14）。注意：pending_notes 只覆盖「实例名称/设计者/年代」，**未覆盖** time_or_place/period/region 的失准项，故该处应补记或升格待核实说明。
- **相似度（阈值 0.54）**：短文本最高 `contrast-principle` **0.2526**；全字段最高 `chiaroscuro` **0.4890**，均 < 0.54，**不超标**。
- **问题**：① **time_or_place/period/region「文艺复兴至19世纪欧洲」与所引来源冲突**（来源含古罗马公元前30年、中国山水、15世纪尼德兰），需改为跨时期/跨地域或据实标注，属 check-1 的 time_or_place 支撑不足；② pending_notes 未覆盖该时段/地区疑点；③ definition 由 `wp-aerial-perspective` 单源直接支撑（`wp-perspective-graphical` 仅语境佐证）。

### 3. `horizon-line`（视平线）— 合格

- **definition**「与观察者眼睛等高、在画面中表现为水平的基准线。」**逐字级支撑**：Vanishing point「The **horizon line** is a theoretical line that represents the **eye level of the observer**.」；Perspective (graphical)「All objects will recede to points in the distance, usually along the **horizon line**」。三要素（眼高/水平/基准线）字面命中，无编造。
- **time_or_place**「文艺复兴至19世纪欧洲（参见来源）。」支撑：Perspective (graphical)「Italian Renaissance painters and architects including Filippo Brunelleschi…」＋ Masaccio「placing the vanishing point at the viewer's eye level in his Holy Trinity」。文艺复兴/欧洲有字面支撑；**轻微**：实抓未见逐字「19世纪」，属 period 口径延展。
- **overview**「视平线统一管理各组平行线，决定画面中人物与建筑的相对高度。」支撑：Vanishing point「If the object is below the horizon line, its lines angle up to the horizon line」＋「eye level of the observer」——线条相对视平线的收束与视高对应，语义准确，无编造。
- **七节完整性**：7 节齐备。
  - 原理「与观察者眼睛等高…水平基准线，统一管理各组平行线」← 同源逐字，有据。
  - 典型手法「先定视平线再定人物与建筑高度关系；适用于场景构图」← eye level/horizon 语境，语义有据。
  - **实例**「名称：场景视平线控制（类型性描述）；地点/设计者/年份：不适用。此处不复制图像。」——**类型性描述，无编造**。
  - 常见错误与限制「视平线位置与视高不一致会造成比例错乱；画面尺寸影响观感。**实际工程须按当地规范和专业设计人员的要求**」——含 D09 规范提示。
  - 一图：1 张内联 SVG（视平线与上下物象），含「**示意图，非施工图**」；`validate_svg` 通过。
- **元数据/coverage 一致**：coverage.json title=视平线/tier=重要/period=文艺复兴至19世纪/region=欧洲/level=L2/source_count=2/needs_verification_count=1，与 batch-01 一致。
- **needs_verification 联动**：true ↔ pending_notes「实例的具体名称、设计者与年代待补充独立来源。」↔ 正文待核实「具体作品的设计者与年代待核实。」一致（D14）。
- **相似度（阈值 0.54）**：短文本最高 `vanishing-point` **0.2653**；**全字段（不含 related）最高 `one-point-perspective` 0.5201（< 0.54，但逼近阈值的软信号）**，其次为 `linear-perspective`、`two-point-perspective` 同级别。全字段 0.5201 < 0.54，**不超标但需监控**。
- **问题**：无实质内容问题（未编造年份/人名/引文）。软信号：① 全字段相似度 0.5201 逼近 0.54，源于同批透视条目模板重合，建议一并改写实例/常见错误措辞；② `time_or_place`/`period`「至19世纪」为宽泛分期，来源未逐字给出。

## 五、结构 / 元数据合规核对（三条共性）

1. **L2 七节完整**：三条均含 definition（=①核心概念与定义）+ 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 六节，合计七节；`tools/check.py` 实跑 **`PASS: all checks, 0 errors`（EXIT=0）** 佐证 `原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实` 六字段非空（check.py L283-286）。
2. **1 张内联 SVG 且含「示意图，非施工图」**：三条各 1 张 `svg`（满足 TASK_design「每页至少 1 到 2 张」下限），逐条字符串「示意图，非施工图」命中；`check.py::validate_svg` 校验 viewBox、非白名单元素、坐标/r/宽高在 viewBox±20% 裕度内（check.py L135-189），0 errors。
3. **风险词段落含规范提示**：三条「常见错误与限制」均含 `REGULATION_NOTE = "实际工程须按当地规范和专业设计人员的要求"`（D09；check.py L19/L291 校验通过）。
4. **needs_verification / pending_notes / 正文待核实 / coverage.nvc 联动一致**：三条 needs_verification=true、pending_notes 非空、正文含「待核实」、coverage.needs_verification_count=1，`check.py`（L266-269、L287-289、L317）通过（0 errors）。**注**：`aerial-perspective` 的时段/地区疑点未被 pending_notes 覆盖，属补充项。
5. **coverage 一致**：三条 title/theme/tier/period/region/level/source_count/needs_verification_count 与 `coverage.json` 逐字段一致（程序化比对 OK，coverage.json L45-55/L84-94/L123-133）。
6. **来源真伪**：被引 4 个唯一 id（`wp-perspective-graphical`、`wp-alberti`、`wp-aerial-perspective`、`wp-vanishing-point`）均存在、verified=true、link_ok=true；本轮 5 页（含 `wp-curvilinear-perspective`）全部 HTTP 200 实抓、`<h1>` 逐字一致。
7. **编造核查**：三条 definition / time_or_place / overview / 七节均**未见具体年份、人名或引文**；实例均为「类型性描述」且 year/设计者填「不适用」，从源头规避 L2 编造风险。（`aerial-perspective` 的问题非编造，而是时段/地区与来源不符。）

## 六、相似度与批次级异常监控

- **相似度算法校准**：为与第13轮可比，本轮「全字段口径」= definition+time_or_place+overview+六节拼接（**不含 related**）。校准验证：`figure-ground` 全字段最高 = 0.4760、`complementary-colors` = 0.5177，与第13轮报告值**逐位一致**；`one-point-perspective` 因本轮 `two-point-perspective` 升级为 L2 后文本变长，其全字段最高由第13轮的 0.4862 升至 0.6080（对照对象 `two-point-perspective`），属正常联动，非算法漂移。
- **本轮三条抽检相似度**（全字段 / 短文本）：`two-point-perspective` **0.5889≥0.54（超标）**/0.4186；`aerial-perspective` 0.4890/0.2526（正常）；`horizon-line` 0.5201/0.2653（接近阈值，软信号）。
- **整批六条（第14轮升级集）全字段最高相似度**：`two-point-perspective` **0.5889（vs one-point，超标）**、`vanishing-point` **0.5361（vs linear-perspective，超标）**、`horizon-line` 0.5201、`three-point-perspective` 0.5010、`aerial-perspective` 0.4890、`foreshortening` 0.4769。**2/6 超 0.54、1/6 逼近**——系六条「透视」条目共用同一 `time_or_place`（「文艺复兴至19世纪欧洲（参见来源）」）、同一「实例」模板句、同一「待核实」句与近似「常见错误＋同一 REG 后缀」所致。**触发 E 节「相似度过高（疑似套话）→整批降级复查」。**
- **待核实占比（E 节监控）**：`upgrade_round14.py` 统一将 6 条升级条目置 `needs_verification=true`（100%），方向与「占比异常低（疑似硬写）」相反，**不触发该监控**；三条的 needs_verification 均对应「实例具体名称/设计者/年代待补独立来源」这一真实未决项，属合理标注。
- **升级范围核实**：`tools/upgrade_round14.py::S` 的 6 条键 = `two-point-perspective/three-point-perspective/aerial-perspective/foreshortening/vanishing-point/horizon-line`，与提示「6 条重要 L1→L2」一致；三条抽检对象确在本轮升级集内，**抽检有效**。
- **结构性核验**：`tools/check.py` 实跑 **PASS: all checks, 0 errors（EXIT=0）**，七节键约束、SVG、规范提示、needs_verification/coverage 联动均通过；`check.py` 内置了「单源且未标待核实」校验（L264），三条均为 2 源，通过。

## 七、总体结论与返工建议

- 逐条：**不合格 1 条**（`two-point-perspective`，仅相似度 0.5889≥0.54 维度）；**待核实 1 条**（`aerial-perspective`，time_or_place/period/region 与来源冲突）；**合格 1 条**（`horizon-line`，含 0.5201 软信号）。
- 三条的 definition / overview 与七节均可由本轮实抓来源正文的字面或强语义文本支撑，**未发现编造年份、人名或引文**；实例均为「类型性描述」，无编造的具体项目/年份。结构上七节齐备、各 1 张 SVG 含「示意图，非施工图」、常见错误与限制含 D09 规范提示、needs_verification/pending_notes/正文待核实/coverage.nvc 联动一致，`check.py` 0 errors。问题集中于 **①相似度（two-point 超标，vanishing-point 亦超标）** 与 **②aerial 的时段/地区失准**。
- **是否建议整批返工：建议整批返工（范围限于第14轮 6 条升级条目，且限于相似度去模板化 + aerial 时段/地区修正），不建议全站返工。** 依据 AUTONOMOUS.md E 节：本轮抽检出现 **1 条不合格（相似度）** 且**同批 `vanishing-point` 0.5361 亦超 0.54**，命中「不合格则整批返工」与「相似度过高则整批降级复查」两条触发条件；但三条内容来源核验扎实、无编造，返工应聚焦而非推倒重写。
- **具体返工项**：
  1. **相似度去模板化**：改写第14轮 6 条的「实例 / 常见错误与限制 / 一图 / 待核实」模板化措辞（现均为高度一致句式＋同一 REG 后缀），并对 `two-point-perspective`、`vanishing-point` 优先处理，使全字段相似度降至 <0.54。
  2. **`aerial-perspective` 时段/地区修正**：将 `time_or_place`/`period`/`region` 由「文艺复兴至19世纪欧洲」改为据实的跨时期/跨地域表述（来源含古罗马公元前30年、中国山水、15世纪尼德兰），或将其降为「待核实」并在 pending_notes 补记该疑点。
  3. **`two-point-perspective` 次源说明**：definition 实为 `wp-perspective-graphical` 单源直接支撑，`wp-alberti` 为时段佐证——升级 L3 或严格双源时补一篇直接界定 two-point 的一般性权威来源。
  4. **period 口径**：三条 `period=文艺复兴至19世纪` 的「至19世纪」为宽泛分期、实抓未逐字给出，可改注「文艺复兴起源」以更贴来源（轻微）。
  5. 收尾时同步更新 REPORT.md / PROGRESS.md / METRICS.json 至第14轮（非本抽检缺陷）。
- **局限**：canonical `en.wikipedia.org` 本环境未直连复核，本轮以 Wikipedia 内容镜像 `owiki.org` 实抓 + 关键词/句级取证；「出版机构=Wikimedia」严格口径待 canonical 恢复后复核。对 L2 的 definition/overview/七节/时段核验已充分。

---

### 机器可读汇总

```
ROUND=14
UPGRADED_ENTRIES=["two-point-perspective","three-point-perspective","aerial-perspective","foreshortening","vanishing-point","horizon-line"]
SPOTCHECKED=["two-point-perspective","aerial-perspective","horizon-line"]
VERDICT={"two-point-perspective":"不合格(相似度)","aerial-perspective":"待核实(time_or_place与来源冲突)","horizon-line":"合格"}
FAILED=["two-point-perspective"]                 # 不合格：相似度 0.5889 >= 0.54
CONTENT_PENDING=["aerial-perspective"]           # 待核实：period/region 过窄且被来源反证
SOURCES_CHECKED=["wp-perspective-graphical","wp-alberti","wp-aerial-perspective","wp-vanishing-point","wp-curvilinear-perspective"]
SOURCES_ALL_VERIFIED=true
HTTP_ALL_200=true
FABRICATION_FOUND=false        # 未见编造年份/人名/引文；实例均为类型性描述（aerial 问题为时段/地区失准，非编造）
SVG_OK=true ; REGNOTE_OK=true ; SEVEN_SECTIONS_OK=true ; NV_LINKAGE_OK=true ; COVERAGE_MATCH=true
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SIMILARITY_MAX_SHORT={"two-point-perspective":0.4186,"aerial-perspective":0.2526,"horizon-line":0.2653}   # all < 0.54
SIMILARITY_MAX_FULL={"two-point-perspective":0.5889,"aerial-perspective":0.4890,"horizon-line":0.5201}    # two-point >=0.54 FAIL; horizon close-but-ok
SIMILARITY_MAX_FULL_BATCH6={"two-point-perspective":0.5889,"vanishing-point":0.5361,"horizon-line":0.5201,"three-point-perspective":0.5010,"aerial-perspective":0.4890,"foreshortening":0.4769}  # 2/6 >=0.54
REWORK_RECOMMENDATION=true     # 限第14轮6条：相似度去模板化 + aerial时段/地区修正；非全站返工
```
