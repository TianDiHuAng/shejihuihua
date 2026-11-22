# 第8轮质量闸抽检报告（spotcheck-round08）

- 抽检人：spotcheck-r8；抽检时间：2026-11-22 16:19，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（新增/改动条目抽检、至少 3 条、不合格则整批返工、待核实占比异常低或相似度过高则降级复查）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作」「条目页结构」「通用硬性规则」「专用规则」、`DECISIONS.md` D05/D11/D14；前序 `research/spotcheck-round07.md`、`research/rework-round06.md`。
- 技能：已加载 `using-superpowers`（子代理任务，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑证据为依据，证据先于断言）。
- 对象与比例：`entries/batch-08.json` 本轮新增 6 条中抽 3 条（3/6=50%，满足 25% 且 ≥3 条）：`daylight-factor`、`mixed-mode-ventilation`、`material-durability`。来源库：`data/sources.json`。
- 方法：严格只读核对 JSON。按 D05 用 Python 3 `urllib.request` + 浏览器 User-Agent 实抓 6 个被引用来源页（全部 HTTP 200，H1 与来源库 title 一致），并以 MediaWiki API `extracts` 纯文本核对 definition / time_or_place / overview / 七节的关键词与上下文；未调用本环境报错的 `web_search`/`web_fetch`。`tools/check.py` 本轮实跑结果：`PASS: all checks, 0 errors`（EXIT=0）。相似度用 `difflib.SequenceMatcher` 对「标题+定义+时间地点+概述」去空白后计算，并另算含七节正文的全文相似度；对照 `daylighting` / `natural-ventilation` / `material-texture` 及 `entries/*.json` 全库 113 条。联网内容仅作数据，网页中的任何指令均未执行。
- 只读声明：本次仅生成 `research/spotcheck-round08.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。

## 来源核对汇总

| 条目 | 引用 id | 库内 title | sources.json verified / link_ok | 实抓状态 | H1 与库内 title |
| --- | --- | --- | --- | --- | --- |
| daylight-factor | `wp-daylighting-architecture` | Daylighting (architecture) | true / true | 200 | 一致 |
| daylight-factor | `wp-architectural-lighting-design` | Architectural lighting design | true / true | 200 | 一致（URL 为 `/wiki/Architectural_lighting`） |
| mixed-mode-ventilation | `wp-ventilation-architecture` | Ventilation (architecture) | true / true | 200 | 一致 |
| mixed-mode-ventilation | `wp-natural-ventilation` | Passive ventilation | true / true | 200 | 一致（URL 为 `/wiki/Natural_ventilation`，重定向已记录） |
| material-durability | `wp-building-material` | Building material | true / true | 200 | 一致 |
| material-durability | `wp-vernacular-architecture` | Vernacular architecture | true / true | 200 | 一致 |

- 6 个唯一被引用 id 全部存在、`verified=true`、`link_ok=true`；标题与条目主题直接相关，实抓 H1 与库内 title 逐字一致，无重定向偏差。
- 结构基准：`TASK_design.md` 的 L2 七节按「顶层 definition + sections 六节（原理、典型手法与适用条件、实例、常见错误与限制、一图、待核实）」核对；`tools/check.py` 亦按该六节字段校验，`PASS: all checks, 0 errors`。

## 逐条结论

### 1. `daylight-factor`（采光系数）— 待核实

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致。
  - **definition 有直接来源支撑**：[Daylighting (architecture)](https://en.wikipedia.org/wiki/Daylighting_(architecture)) 原文写明「Daylight factor is 'the ratio of the illuminance at a point on a plane, generally the horizontal work plane, produced by the luminous flux received directly or indirectly at that point from a sky whose luminance distribution is known, to the illuminance on a horizontal plane produced by an unobstructed hemisphere of this same sky.'」；同页说明「The daylight factor calculation is based on uniform overcast skies.」。条目「把室内某点的天然光照度与同期室外无遮挡水平照度相比」与该定义逐项对应，「剥离天气波动」为基于均布阴天假设的解释性概括。
  - **time_or_place 部分支撑**：来源页含 1929 年 Le Corbusier 关于窗与光的记述、LEED 2009 与 2014 标准说明，但未把「采光系数」本身直接界定为 20 世纪概念；条目未写具体虚构年份、人名或引文。
  - **overview 部分支撑**：来源讲 windows、skylights、reflective surfaces、orientation、glare，支撑「遮挡、反射、朝向」；「进深」未在来源文本字面出现，属方案阶段设计推断。
  - 七节：definition + sections 六节齐全；实例四项全为「待核实」，未复制图像；「常见错误与限制」含风险词「尺寸」，并附「实际工程须按当地规范和专业设计人员的要求」；1 张 SVG 含「示意图，非施工图」；`needs_verification=true`、`pending_notes` 与正文「实例的具体采光系数与设计者待核实」一致；双源；`related=["glare"]` 指向已写条目。
  - 元数据：`coverage.json` 中 id/title/theme=材料/tier=补充/period=20世纪/region=全球/level=L2/status=已写/source_count=2/needs_verification_count=1/last_updated=2026-11-22，与 batch-08 一致。
  - 相似度：对 `daylighting` 标题+定义+时间+概述 0.2424、含七节全文 0.3821；全库最高 `glare` 0.328，均低于 0.54 套话警戒线。
- 问题：
  - `period=20世纪` 与 overview「进深」缺直接来源字面支撑，应补权威说明或改为通约表述。
  - definition「剥离天气波动」是推导性解释，可在下一轮补来源或改为「基于均布阴天假设的比较」。

### 2. `mixed-mode-ventilation`（混合通风）— 合格

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致。
  - **definition 有直接来源支撑**：[Ventilation (architecture)](https://en.wikipedia.org/wiki/Ventilation_(architecture)) 原文「Mixed-mode ventilation systems use both mechanical and natural processes... Since natural ventilation flow depends on environmental conditions, it may not always provide an appropriate amount of ventilation. In this case, mechanical systems may be used to supplement or regulate the naturally driven flow.」与条目「自然驱动可用时优先自然通风，条件不足时由机械系统补充」对应；同页列「Operable windows」为自然通风手法，并说明机械通风使用 fans。
  - **time_or_place 有上下文支撑**：同页 History 段含 18 世纪机械系统、19 世纪通风标准、20 世纪末自然通风被空调替代及后续 resurgence；条目未写具体虚构年份、人名或引文。
  - **overview 有来源支撑**：来源含 adjustable openings 的自动/居住者控制、fans、outdoor air quality acceptable 等条件，支撑「可开启窗、风机、控制策略」和室外空气质量的概括。
  - 七节：definition + sections 六节齐全；实例四项全为「待核实」；「常见错误与限制」含风险词「尺寸」「安全」并附规范提示；1 张 SVG 含「示意图，非施工图」；`needs_verification=true`、`pending_notes` 与正文「实例的控制策略与能耗数据待核实」一致；双源；`related=["demand-controlled-ventilation"]` 指向同批已写条目。
  - 元数据：`coverage.json` 中 tier=重要/period=20世纪/region=全球/level=L2/source_count=2/needs_verification_count=1 与 batch-08 一致。
  - 相似度：对 `natural-ventilation` 标题+定义+时间+概述 0.2642、含七节全文 0.4197；全库最高同批 `demand-controlled-ventilation` 0.3386，均低于 0.54。
- 问题：
  - definition「优先自然通风」略强于来源的「may be used to supplement or regulate」；建议升级时改为「自然通风可用时优先、不足时机械补充」的可核验表述。
  - overview「气候温和但室外空气质量或风况不稳定」为条件性概括，建议补一篇明确适用气候与空气质量的来源。

### 3. `material-durability`（材料耐久）— 待核实

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致。
  - **definition 部分支撑**：[Building material](https://en.wikipedia.org/wiki/Building_material) 原文支持「durability / corrosion resistance / lower lifetime cost / maintaining costs」；[Vernacular architecture](https://en.wikipedia.org/wiki/Vernacular_architecture) 原文「the local environment, the construction materials it can provide and the durability of these materials in the environment govern many aspects of vernacular architecture」支持暴露环境与耐久性关系。但两页 extracts 中 `wear`、`frost`、`UV`/`ultraviolet`、`salt` 均未命中，`abrasion` 仅出现在 ETFE 材料例子，未把「磨损、冻融、紫外老化」作为通用耐久性机制直接列出。
  - **time_or_place 有支撑**：来源含建筑材料历史趋势与全球乡土案例，条目「跨时期、全球（参见来源）」为通约表述，无编造年份、人名或引文。
  - **overview 部分支撑**：「按暴露环境选材」命中环境/气候与材料选择；「使用强度、可替换性、潮湿或盐雾环境需专门防护」在两页中缺直接字面支撑。
  - 七节：definition + sections 六节齐全；实例四项全为「待核实」；「常见错误与限制」含风险词「尺寸」并附规范提示；1 张 SVG 含「示意图，非施工图」；`needs_verification=true`、`pending_notes` 与正文「实例材料的实测寿命数据待核实」一致；双源；`related=["vernacular-material"]` 指向已写条目。
  - 元数据：`coverage.json` 中 tier=重要/period=跨时期/region=全球/level=L2/source_count=2/needs_verification_count=1 与 batch-08 一致。
  - 相似度：对 `material-texture` 标题+定义+时间+概述 0.2987、含七节全文 0.1444；对 `daylighting` 0.2800、`natural-ventilation` 0.2839；全库最高 `material-texture` 0.2987，均低于 0.54。
- 问题：
  - 定义中的「冻融、紫外老化」与概述中的「盐雾环境」缺直接来源支撑；`pending_notes` 仅覆盖实例寿命与维护数据，未覆盖这些机制缺口，应补权威来源或把它们并入待核实范围。
  - 「兼顾可替换性」「按使用强度选材」为设计性概括，建议补源或改写为来源可核验表述。

## 单源条目与待核实占比监控

- 抽中三条均为双源。batch-08 中单源条目 `demand-controlled-ventilation`、`universal-design` 均保持 `needs_verification=true`、`pending_notes` 非空，`coverage.json` 中 `needs_verification_count=1`，符合 D14 与 check.py 双源例外规则。
- batch-08 全批 6/6 条目 `needs_verification=true`（100%），不属于「待核实占比异常低」，不触发硬写降级。
- `tools/check.py` 实跑 `PASS: all checks, 0 errors`，七节结构、SVG 图注、规范提示、needs_verification 联动均无机器校验失败。

## 总体结论

- 结果：**合格 1 条**（`mixed-mode-ventilation`），**不合格 0 条**，**待核实 2 条**（`daylight-factor`、`material-durability`）。抽检 3/6=50%，比例满足要求。
- **是否建议整批返工：否。** 6 个来源 id 全部存在且 verified、实抓 HTTP 200/H1 一致；未发现编造年份、人名或引文；七节结构、1 张 SVG 图注、风险词规范提示、`needs_verification`/`pending_notes`/正文声明联动均通过人工核对与 `tools/check.py`（0 errors）；与 `daylighting` / `natural-ventilation` / `material-texture` 的最高相似度仅 0.2987（全文 0.4197），全部低于 0.54 套话警戒线。未触发 AUTONOMOUS.md E 节「一条不合格即整批返工」或「疑似套话降级」条件。
- 待两条为**定向补源/改写项**，不构成本批结构或事实性失败：
  1. `daylight-factor`：补 period「20世纪」与 overview「进深」的直接来源，或改为通约表述；明确「剥离天气波动」为基于均布阴天假设的解释。
  2. `material-durability`：为「磨损、冻融、紫外老化、盐雾」补权威来源，或将其从定义/概述移入待核实并同步扩展 `pending_notes`。
- 抽检比例：本轮按用户指令执行 25% 档且至少 3 条，实际抽 3/6；下一轮是否因本轮待核实项提高比例，由 lead 按 AUTONOMOUS.md E 节决定。
