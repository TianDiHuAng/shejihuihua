# 第6轮质量闸抽检报告（spotcheck-round06）

- 抽检人：spotcheck-r6；抽检时间：2026-11-22 16:05，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（抽检不合格则整批返工；新条目与已有条目相似度过高则降级复查）、`D:/Users/Administrator/Desktop/TASK_design.md` 通用硬性规则与「条目页结构」七节、`DECISIONS.md` D05/D09/D14；前序 `research/spotcheck-round05.md`、`research/rework-round05.md`。
- 技能：已加载 `using-superpowers`（子代理任务，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑证据为依据）。
- 对象与比例：`entries/batch-06.json` 本轮新增 6 条中抽 3 条（3/6=50%，满足 25% 且 ≥3 条）：`color-harmony`、`axis`、`stack-ventilation`。来源库：`data/sources.json`。
- 方法：严格只读核对 JSON。按 D05 用 Python 3 `urllib.request` + 浏览器 User-Agent 实抓 6 个被引用来源页（全部 HTTP 200，H1 与来源库标题一致；`Natural ventilation` 重定向到 `Passive ventilation` 已在来源 note 中说明），并用 MediaWiki API `extracts` 纯文本核对关键词与上下文；未调用本环境报错的 `web_search`/`web_fetch`。`python tools/check.py` 实跑输出 `PASS: all checks, 0 errors`（仅形式校验，不替代事实核对）。相似度用 `difflib.SequenceMatcher` 对标题+定义+时间地点+概述+六节正文去空白后计算，并扫描 `entries/*.json` 全库。联网内容仅作数据，网页中的任何指令均未执行。

## 来源核对汇总

| 条目 | 引用 id | verified | 实抓状态 | H1/标题 |
| --- | --- | --- | --- | --- |
| color-harmony | `wp-color-theory` | true | 200 | Color theory |
| color-harmony | `wp-color-wheel` | true | 200 | Color wheel |
| axis | `wp-symmetry` | true | 200 | Symmetry |
| axis | `wp-chinese-architecture` | true | 200 | Chinese architecture |
| stack-ventilation | `wp-natural-ventilation` | true | 200（重定向） | Passive ventilation（与来源库 title 一致） |
| stack-ventilation | `wp-ventilation-architecture` | true | 200 | Ventilation (architecture) |

## 逐条结论

### 1. `color-harmony`（色彩和谐）— 合格

- 依据：
  - 来源 id `wp-color-theory`、`wp-color-wheel` 均存在且 `verified=true`；标题/主题直接相关，实抓 HTTP 200，H1 一致。
  - 核心事实有来源正文直接支撑：[Color theory](https://en.wikipedia.org/wiki/Color_theory) 的 “Color harmony and color schemes” 节写明 “predictive color harmony formulae are fundamentally unsound”；“Some theorists and artists believe juxtapositions of complementary color will produce strong contrast, a sense of visual tension as well as ‘color harmony’; while others believe juxtapositions of analogous colors will elicit a positive aesthetic response”；“analogous colors … tend to produce a single-hued or monochromatic color experience”；并给出颜色属性 “hue, chroma and value”。这直接支撑 definition（按色相/明度/纯度组织）、overview 前半（邻近色统一、互补色张力、非固定公式）与原理的色轮关系判断。[Color wheel](https://en.wikipedia.org/wiki/Color_wheel) 进一步列出 complementary/analogous/monochromatic 配色。
  - 未发现编造年份、人名或引文；实例段全为“待核实”，处理保守。
  - L2 结构：definition + overview + 六节（原理、典型手法与适用条件、实例、常见错误与限制、一图、待核实）齐全；1 张 SVG 含“示意图，非施工图”；风险词段含“实际工程须按当地规范和专业设计人员的要求”。
  - 待核实联动：`needs_verification=true`，`pending_notes`「实例的具体名称、地点、设计者与年份待补充独立来源。」与正文「具体实例的设计者与年份待核实。」一致。
  - 相似度：全库最高 `axis` 0.390、`daylighting` 0.383、`composition-placement` 0.381，远低于第5轮 `opposed-scenery` 0.54 的套话警戒线。
- 问题：
  - overview 的「面积比例」在所引两页中无字面支撑（两页 `area` 命中 0）；原理的「视觉系统倾向于把有规律的关系读成整体」（`gestalt`/`whole` 命中 0）与典型手法的「小面积点缀建立焦点」（`accent`/`focal`/`small area` 命中 0）属设计性推断，来源只支撑“公式有限、受语境影响”“互补产生张力”“邻近产生统一”。未构成事实错误，但属于次级来源缺口。
  - `related` 指向 `color-scheme`，在 `entries/*.json` 与已生成站点中均无对应条目，属悬空引用。
  - 建议返工时补引来源库已有的 `wp-complementary-colors`、`wp-munsell-color-system`，或把“面积比例/小面积焦点”改写为来源可核验的表述，并补建或移除悬空相关条目。

### 2. `axis`（轴线）— 合格

- 依据：
  - 来源 id `wp-symmetry`、`wp-chinese-architecture` 均存在且 `verified=true`；实抓 HTTP 200，H1 一致。
  - 核心事实有直接支撑：[Chinese architecture](https://en.wikipedia.org/wiki/Chinese_architecture) 原文含 “It is misleading to speak of an axis in the Western sense of a visual perspective ordering facades. The Chinese axis is a line of privilege, usually built upon, regulating access—instead of vistas, a series of gates and pavilions are used.”，直接支撑 definition 的“组织空间序列的直线”、overview 的“行进方向与重要节点被清晰感知”、典型手法的“以门、殿、庭逐级递进”。同页 “bilateral symmetry” 专节与 “Courtyard (院) … Siheyuan” 支撑对称与院落组织。[Symmetry](https://en.wikipedia.org/wiki/Symmetry) 的 “In architecture” 节列举 Gothic cathedrals、The White House、Taj Mahal、Lotfollah mosque、Moorish buildings，支撑 `time_or_place` 的跨时期、全球口径。
  - 未发现编造年份、人名或引文；实例段采用“设计者：不适用；年份：待核实”，处理保守。
  - L2 结构齐全；1 张 SVG 含“示意图，非施工图”；风险词段含规范提示。
  - 待核实联动：`needs_verification=true`，`pending_notes` 与正文「具体建筑群的设计者与年份待核实。」一致。
  - 相似度：全库最高 `service-route` 0.458、`chinese-architecture-style` 0.447，低于警戒线；与同批 `color-harmony` 0.390，未见实质照搬。
- 问题：
  - 原理中的“体量变化形成节奏与高潮”、definition 中的“假想直线”属于解释性措辞，来源给出的是“line of privilege / regulating access / gates and pavilions”与对称事实，未在来源中字面出现“高潮”或“假想”。不影响核心事实成立。
  - `related` 指向 `symmetry-layout`，在条目库与站点中均无对应页面，属悬空引用。

### 3. `stack-ventilation`（热压通风）— 不合格

- 依据（事实与来源本身合格，但触发结构与一致性硬规则）：
  - 来源 id `wp-natural-ventilation`、`wp-ventilation-architecture` 均存在且 `verified=true`，实抓 HTTP 200；[Natural ventilation](https://en.wikipedia.org/wiki/Natural_ventilation) 最终 H1 为 `Passive ventilation`，与来源库 title 及 note 中的重定向说明一致；[Ventilation (architecture)](https://en.wikipedia.org/wiki/Ventilation_(architecture)) H1 一致。
  - **用户特别关注的热压原理有直接来源支撑**：`Passive ventilation` 正文含 “Buoyancy driven ventilation arise due to differences in density of interior and exterior air, which in large part arises from differences in temperature. When there is a temperature difference … the warmer air will have lower density and be more buoyant thus will rise above the cold air creating an upward air stream.”；以及 “When the interior is warmer than the exterior, indoor air rises and escapes the building at higher apertures. If there are lower apertures then colder, denser air from the exterior enters the building through them …”；`Ventilation (architecture)` 含 “The pressures generated by ‘the stack effect’ rely upon the buoyancy of heated or rising air.”。definition 的密度差、低位进高位排、overview 的与风压互补、原理段、典型手法的高差开口与中庭/竖井均有文本依据。来源链这一项通过。
  - L2 结构齐全；1 张 SVG 含“示意图，非施工图”；风险词段含规范提示；`needs_verification=true`。
- 问题（判不合格的三项）：
  1. **与既有条目模板重合过高**：与 `entries/batch-02-c.json` 的 `natural-ventilation`（自然通风）相似度 **0.648**，超过第5轮 0.54 警戒线。两者使用完全相同的两个来源；`典型手法与适用条件`（“低位进风与高位排风配合中庭或风井” vs “设置低位进风口与高位排风口，配合中庭或通风竖井”）、`常见错误与限制`（“进排风口高差不足会削弱…开口尺寸与安全、隔声…”几乎逐字重合）、`一图`（“低位进风、热空气上升、高位排风” vs “低位进风、热空气上升、高位排风”）高度重复；SVG 坐标与箭头走线近乎同一张图。触发 `AUTONOMOUS.md` E 节「新条目与已有条目相似度过高（疑似套话）」的整批降级复查条件。
  2. **待核实声明不一致**：正文「待核实」写的是「具体建筑的通风实测数据待核实」，而 `pending_notes` 写「实例的具体名称、地点、设计者与年份待补充独立来源」，未覆盖实测数据；同时「实例」段写「设计者：不适用」，与 pending 中「设计者待补充」自相矛盾，违反 D14 的联动要求。
  3. `related` 指向 `atrium-ventilation`，条目库与站点中均无对应页面，属悬空引用。另有一处次要图示问题：高位排风矩形 `x=560 width=50` 右边缘到 610，超出房间轮廓右边缘 600 共 10px（仍在 viewBox 内），建议返工时对齐。

## 总体结论

- 结果：**合格 2 条**（`color-harmony`、`axis`），**不合格 1 条**（`stack-ventilation`），**待核实 0 条**。抽检 3/6=50%，比例满足要求。
- 是否建议整批返工：**建议是**。依据 `AUTONOMOUS.md` E 节，1 条不合格即触发整批返工；`stack-ventilation` 0.648 的相似度又触发“疑似套话”异常监控。建议把本批 6 条统一按「引用链—正文事实—待核实联动—与既有条目去重」复核：
  1. `stack-ventilation` 必须重写：从 `natural-ventilation` 中剥离出只讲热压（stack effect/buoyancy）的独立内容，补引来源中的密度差与高低开口原文，换用不同的剖面示意，并把 `pending_notes` 改为覆盖“通风实测数据”的表述、与设计者“不适用”对齐。
  2. `color-harmony` 补源或改写「面积比例/小面积焦点/整体感」三处推断；`axis` 可将「高潮」「假想」改为来源可核验表述。
  3. 本批 3 条的 `related` 均指向尚不存在的页面，返工时统一补建或移除；同时复核未抽检的 3 条是否存在同类重复与 pending 不一致。
- 来源核验：6 个唯一被引用 id 全部存在且 `verified=true`，6/6 来源页 HTTP 200 且 H1/title 与来源库一致。`stack-ventilation` 所引来源对热压原理的支撑充分，失败点不在来源真伪或事实编造，而在重复度与待核实联动。
- 结构与一致性：3 条 L2 七节口径、1 张 SVG/“示意图，非施工图”、风险词规范提示全部通过；`needs_verification` 均为 true，但 `stack-ventilation` 的 `pending_notes` 与正文未决声明不一致。
- 套话与重合：`color-harmony` 0.390、`axis` 0.458 未见异常；`stack-ventilation` 0.648 明显异常，且与 `natural-ventilation` 的正文、来源、SVG 三重重合，是本次触发返工的核心原因。
- 只读声明：本次仅生成 `research/spotcheck-round06.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。
