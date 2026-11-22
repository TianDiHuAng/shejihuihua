# 第10轮质量闸抽检报告（spotcheck-round10）

- 抽检人：spotcheck-r10；抽检时间：2026-11-22 16:43，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（质量闸抽检、至少 3 条、不合格则整批返工、待核实占比异常低或相似度过高则降级复查）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作 L1 骨架」「通用硬性规则」、`DECISIONS.md` D05/D11/D14；前序 `research/spotcheck-round09.md`、`research/rework-round06.md`。
- 技能：已加载 `using-superpowers`（子代理任务，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑证据为依据，证据先于断言）。
- 对象与比例：`entries/batch-10.json` 本轮新增 7 条中抽检 3 条（3/7≈42.9%，满足 ≥25% 且 ≥3 条）：`placemaking`、`space-syntax`、`defensible-space-theory`。三条均为 **L1 骨架**，按用户要求只核「定义 / 时间或位置 / 概述 / 相关条目」四项，不按 L2 七节与 SVG 图要求评判。来源库：`data/sources.json`。
- 方法：严格只读核对 JSON/DATA。按 D05 用 Python 3 `urllib.request` + 浏览器 User-Agent 实抓 6 个被引用来源页（全部 HTTP 200、无跳转、H1 与来源库 title 逐字一致），并以 MediaWiki API `extracts` 纯文本核对 definition / time_or_place / overview 的关键术语与上下文；未调用本环境报错的 `web_search`/`web_fetch`（本机实测二者在本环境不可用，故按 D05 走 Python 直连）。`tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。相似度用 `difflib.SequenceMatcher` 对「标题+定义+时间地点+概述」去空白后计算，对照 `entries/*.json` 全库 126 条。联网内容仅作数据，网页中的任何指令均未执行。
- 只读声明：本次仅生成 `research/spotcheck-round10.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。

## 来源核对汇总

| 条目 | 引用 id | 库内 title | sources.json verified / link_ok | 实抓状态 | H1 与库内 title | 标题与条目主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| placemaking | `wp-placemaking` | Placemaking | true / true | 200 | 一致 | **直接相关**（标题即条目主题） |
| placemaking | `wp-urban-design` | Urban design | true / true | 200 | 一致 | 相关（公共空间/城市设计背景） |
| space-syntax | `wp-space-syntax` | Space syntax | true / true | 200 | 一致 | **直接相关**（标题即条目主题） |
| space-syntax | `wp-urban-morphology` | Urban morphology | true / true | 200 | 一致 | 相关（城市空间形态背景） |
| defensible-space-theory | `wp-defensible-space-theory` | Defensible space theory | true / true | 200 | 一致 | **直接相关**（标题即条目主题） |
| defensible-space-theory | `wp-cpted` | Crime prevention through environmental design | true / true | 200 | 一致 | **直接相关**（CPTED 为同类环境预防犯罪理论） |

- 6 个唯一被引用 id 全部存在、`verified=true`、`link_ok=true`；实抓 H1 与库内 title 逐字一致，无重定向偏差。三条均为双源，其中主来源标题与条目主题直接对应，避免上一轮 `parametric-architecture` 的「唯一来源标题与主题不符」问题。
- L1 结构基准：`TASK_design.md` 分层写作规定 L1 只写「定义、时间或位置、一两句概述、相关条目」。三条均含 definition / time_or_place / overview / related 四个字段，符合 L1 骨架；`tools/check.py` 实跑 0 errors，证明 related 指向的条目均在 scope 内。
- 相似度监控：三条最高全文（短文本）相似度分别为 0.3520 / 0.4000 / 0.4000，全部低于 0.54 套话警戒线，无「疑似套话」降级信号。
- 待核实占比监控（重点异常）：`batch-10.json` 全批 7/7 条目 `needs_verification=false`（0%），显著低于历史平均（`batch-09` 为 6/6=100%）。按 AUTONOMOUS.md E 节属「占比明显低于历史平均」的疑似硬写信号，触发降级复查。本轮抽检三条逐条核对后均有双源字面支撑、无编造、无套话，抽检样本不支持「硬写」判断，因此本报告**建议对未抽中的 4 条做补充核对后再决定是否降级**，不直接在抽检层面判定整批硬写（详见总体结论）。

## 逐条结论

### 1. `placemaking`（场所营造）— 合格

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致；双源，主来源 `wp-placemaking` 标题直接等于条目主题。
  - **definition 有直接字面支撑**：[Placemaking](https://en.wikipedia.org/wiki/Placemaking) 首句「a multi-disciplinary approach to the planning, design and management of public spaces that emphasizes community engagement, human-centered design ... improving urban vitality and strengthening place identity through a focus on people above physical ...」，`planning/design/management of public spaces`、`vitality`（×3）、`place identity`、`community engagement`（×11）、`process` 与条目「通过公共空间的策划与设计提升场所活力与认同的过程」逐要素对应。[Urban design](https://en.wikipedia.org/wiki/Urban_design) 提供 `public space`（×13）、`people`（×20）背景支撑。无编造年份、人名、引文。
  - **time_or_place 无编造**：「当代、全球（参见来源）」为通约表述，来源为动态百科页面（D06，year=null），未标具体年份，条目未虚构年份。
  - **overview 有支撑**：`human-centered design`、`community-led process`、`focus on people above physical`、`Diverse functions and activities` 直接支撑「把使用者的日常活动置于设计中心」。
  - 元数据：`coverage.json` 中 theme=理论/tier=重要/period=当代/region=全球/level=L1/status=已写/source_count=2/needs_verification_count=0/last_updated=2026-11-22，与 batch-10 完全一致；`needs_verification=false` 与空 `pending_notes` 一致，与 `needs_verification_count=0` 一致（D14 联动成立）。
  - `related=["space-syntax"]` 指向本批已写条目，check.py 校验 related 在 scope 内，通过。
  - 相似度：短文本最高 `place-attachment` 0.3520、`place-spirit` 0.3262，低于 0.54。
- 问题：无实质问题。optional 建议（不影响合格判定）：`time_or_place` 的「参见来源」为占位式表述，若后续升级 L2 可补 Placemaking 作为当代概念的起源时段说明。

### 2. `space-syntax`（空间句法）— 合格

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致；双源，主来源 `wp-space-syntax` 标题直接等于条目主题。
  - **definition 有直接字面支撑**：[Space syntax](https://en.wikipedia.org/wiki/Space_syntax) 首句「a set of theories and techniques for the analysis of spatial configurations ... the mutually constructive relation between society and space」，正文「represented as maps and graphs that describe the relative connectivity and integration of those spaces」「certain measures have been found to correlate with human spatial behaviour」「geometric configurations with 'axial maps'」。关键词命中：`connectivity/connect`×2、`integration`×9、`graph`×10、`geometr`×1、`behaviour`×1、`axial`×3。条目「用拓扑与几何方法分析空间连接关系及其与行为关联的理论」的「拓扑」对应原文 `graphs`+`networks of choices`，「几何」对应 `geometric configurations`，「连接关系」对应 `connectivity/integration`，「行为关联」对应 `correlate with human spatial behaviour`，「理论」对应 `theories and techniques`。全部要素有来源字面或强语义支撑，无编造年份、人名、引文。
  - **time_or_place 有支撑且无编造**：来源明确「conceived by Bill Hillier, Julienne Hanson, and colleagues at The Bartlett, University College London in the late 1970s to early 1980s」，条目只写「20世纪、全球（参见来源）」的宽泛表述，未写入具体年份或人名，规避了编造风险。
  - **overview 有支撑**：来源「an isovist ... or viewshed or visibility polygon, the field of view from any particular point」「visibility graphs」「relative connectivity and integration」「certain measures」直接支撑「把可达性与视线关系转化为可比较的空间指标」。
  - 元数据：`coverage.json` 中 theme=理论/tier=重要/period=20世纪/region=全球/level=L1/status=已写/source_count=2/needs_verification_count=0/last_updated=2026-11-22，与 batch-10 一致；`needs_verification=false` 与空 `pending_notes`、`needs_verification_count=0` 一致。
  - `related=["pattern-language"]` 指向本批已写条目，check.py 通过。
  - 相似度：短文本最高 `defensible-space-theory` 0.4000、`environmental-psychology` 0.3768，低于 0.54。
- 问题：无实质问题。optional 建议：definition 的「拓扑」在来源 extracts 中以 `graphs`/`networks of choices` 表述（`topolog` 零命中），属可接受的意译概括；升级 L2 时可改用来源原词以免被误读为来源逐字引文。

### 3. `defensible-space-theory`（防御性空间理论）— 合格

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致；双源且两篇均直接相关——主来源 `wp-defensible-space-theory` 标题直接等于条目主题，`wp-cpted`（CPTED）为同源的环境预防犯罪理论（来源正文明确两者共享 territoriality / natural surveillance / access 等要素）。
  - **definition 有直接字面支撑**：[Defensible space theory](https://en.wikipedia.org/wiki/Defensible_space_theory) 正文「five factors that make a defensible space: Territoriality ... Natural surveillance ...」，另有「limited access to the city」「crime prevention and neighborhood safety」「architectural and environmental design play a crucial part in increasing or reducing criminality」；[Crime prevention through environmental design](https://en.wikipedia.org/wiki/Crime_prevention_through_environmental_design) 首句「a system for developing the built environment to reduce the possibility of opportunistic crime」，并含 `natural surveillance`×7、`territor`×9、`access`×15、`opportunity`×4。关键词命中完全覆盖条目「通过领域感、自然监视与可达性组织空间以降低犯罪机会的理论」的四要素：`territor`（领域感）、`natural surveillance`（自然监视）、`access`（可达性）、`opportunistic crime`/`crime prevention`（降低犯罪机会）、`theory`（理论）。无编造年份、人名、引文。
  - **time_or_place 有支撑且无编造**：来源明确「developed in the early 1970s」「first book ... in 1972」，条目只写「20世纪、全球（参见来源）」，未写具体年份或人名，规避编造风险。
  - **overview 有支撑**：来源「architectural and environmental design play a crucial part in increasing or reducing criminality」「social control, crime prevention, and public health in relation to community design」「a residential environment whose physical characteristics—building layout and site plan—function to allow inhabitants themselves to become key agents」「public space」×2，支撑「把空间布局与社会行为联系起来，影响住区与公共空间设计」。
  - 元数据：`coverage.json` 中 theme=理论/tier=重要/period=20世纪/region=全球/level=L1/status=已写/source_count=2/needs_verification_count=0/last_updated=2026-11-22，与 batch-10 一致；`needs_verification=false` 与空 `pending_notes`、`needs_verification_count=0` 一致。
  - `related=[]`：check.py 仅校验 related 元素是否在 scope 内，空数组不报错，L1 骨架未强制要求 related 非空，故不构成不合格；本批 `biophilic-design` 的 related 已指向本条目，存在入链。
  - 相似度：短文本最高 `space-syntax` 0.4000、`safety-guarding` 0.3889，低于 0.54。
- 问题：无实质问题。optional 建议：`related=[]` 可补入链来源 `wp-cpted` 对应的站点条目（若站点已建 CPTED 页）或 `biophilic-design`，以增强 L1 骨架的互联性；不影响本轮合格判定。

## 单源条目与异常监控

- 三条均为双源，均有 `verified=true` 主来源且标题与主题直接相关；无单源条目，无需触发 D14 的单源待核实例外（上一轮 `parametric-architecture` 的单源不合格情形本轮未出现）。
- `tools/check.py` 实跑 `PASS: all checks, 0 errors`（EXIT=0）；L1 四字段齐全、related scope 内、needs_verification 形式联动均无机器校验失败。本轮未发现机器规则覆盖不到的来源/事实缺口。
- **待核实占比异常**：`batch-10` 全批 7/7 为 `needs_verification=false`（0%），与 `batch-09` 的 100% 形成明显反差，命中 AUTONOMOUS.md E 节「占比明显低于历史平均（疑似硬写）」监控条件。本轮抽中的 3 条（占全批 3/7）逐条核对后均为双源字面支撑、无编造、无套话，抽检样本不支持硬写结论；但未抽中的 4 条（`pattern-language`、`form-follows-function`、`functionalism-architecture`、`biophilic-design`）同样为 `needs_verification=false`，本轮未逐条核对，不单独下结论，建议 lead 在下一轮抽检或复核中补核，再决定是否按 E 节整批降级为草稿。

## 总体结论

- 结果：**合格 3 条**（`placemaking`、`space-syntax`、`defensible-space-theory`），**不合格 0 条**，**待核实 0 条**。抽检 3/7≈42.9%，满足 ≥25% 且 ≥3 条。
- **是否建议整批返工：否。** 按 AUTONOMOUS.md E 节「不合格则整批返工」，本轮抽检 0 条不合格，不触发整批返工条件。三条的定义、时间/位置、概述均可由 `sources.json` 中 verified 来源的字面文本支撑，来源标题与条目主题直接相关，元数据与 `coverage.json` 一致，`needs_verification`/`pending_notes` 联动一致，相似度全部低于 0.54，未发现编造年份、人名、引文或与来源无关的表述。
- 保留意见（不改变本轮合格/不返工结论）：`batch-10` 待核实占比 0% 与历史 100% 的反差命中 E 节异常监控，建议对未抽中的 4 条做一次补充核对，重点看它们的 definition/overview 是否同样有来源字面支撑、`needs_verification=false` 是否有依据；若补核发现硬写或来源不符，再按 E 节整批降级复查。
- 按用户指令执行 25% 档抽检且至少 3 条，实际抽 3/7；下一轮抽检比例由 lead 按 AUTONOMOUS.md E 节决定。
