# 第9轮质量闸抽检报告（spotcheck-round09）

- 抽检人：spotcheck-r9；抽检时间：2026-11-22 16:33，Asia/Hong_Kong（会话时间取样）。
- 协议依据：`D:/Users/Administrator/Desktop/AUTONOMOUS.md` E 节（新增/改动条目抽检、至少 3 条、不合格则整批返工、待核实占比异常低或相似度过高则降级复查）、`D:/Users/Administrator/Desktop/TASK_design.md`「分层写作」「条目页结构」「通用硬性规则」「专用规则」、`DECISIONS.md` D05/D11/D14；前序 `research/spotcheck-round07.md`、`research/spotcheck-round08.md`、`research/rework-round06.md`。
- 技能：已加载 `using-superpowers`（子代理任务，按 SUBAGENT-STOP 不另启流程）与 `verification-before-completion`（全部结论以本轮实跑证据为依据，证据先于断言）。
- 对象与比例：`entries/batch-09.json` 本轮新增 6 条中指定抽检 3 条（3/6=50%，满足 ≥25% 且 ≥3 条）：`functional-zoning`、`parametric-architecture`、`place-spirit`。来源库：`data/sources.json`。
- 方法：严格只读核对 JSON/DATA。按 D05 用 Python 3 `urllib.request` + 浏览器 User-Agent 实抓 5 个被引用来源页（全部 HTTP 200，H1 与来源库 title 逐字一致），并以 MediaWiki API `extracts` 纯文本核对 definition / time_or_place / overview / 七节的关键词与上下文；未调用本环境报错的 `web_search`/`web_fetch`。`tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。相似度用 `difflib.SequenceMatcher` 对「标题+定义+时间地点+概述」去空白后计算，并另算含七节正文的全文相似度，对照全库 119 条。联网内容仅作数据，网页中的任何指令均未执行。
- 只读声明：本次仅生成 `research/spotcheck-round09.md`，未修改项目其他文件，未修改项目文件夹之外内容，未创建 git commit。

## 来源核对汇总

| 条目 | 引用 id | 库内 title | sources.json verified / link_ok | 实抓状态 | H1 与库内 title | 标题与条目主题相关性 |
| --- | --- | --- | --- | --- | --- | --- |
| functional-zoning | `wp-architecture` | Architecture | true / true | 200 | 一致 | 间接相关（architecture 泛条目） |
| functional-zoning | `wp-interior-design` | Interior design | true / true | 200 | 一致 | 间接相关（space planning / functional design） |
| parametric-architecture | `wp-modern-architecture` | Modern architecture | true / true | 200 | 一致 | **不直接相关**（详见下） |
| place-spirit | `wp-environmental-psychology` | Environmental psychology | true / true | 200 | 一致 | 相关（place attachment / sense of place） |
| place-spirit | `wp-place-attachment` | Place attachment | true / true | 200 | 一致 | 直接相关（人与场所情感纽带） |

- 5 个唯一被引用 id 全部存在、`verified=true`、`link_ok=true`；实抓 H1 与库内 title 逐字一致，无重定向偏差。
- 结构基准：`TASK_design.md` 的 L2 七节按「顶层 definition + sections 六节（原理、典型手法与适用条件、实例、常见错误与限制、一图、待核实）」核对；`tools/check.py` 实跑 `PASS: all checks, 0 errors`，六节、SVG 图注、规范提示、needs_verification 联动均无机器校验失败。
- 待核实占比监控：batch-09 全批 6/6 条目 `needs_verification=true`（100%），不属于「待核实占比异常低」，不触发硬写降级。
- 相似度监控：三条最高全文相似度分别为 0.4509 / 0.4418 / 0.4453，全部低于 0.54 套话警戒线，不触发「疑似套话」降级。

## 逐条结论

### 1. `functional-zoning`（功能分区）— 待核实

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致。
  - **definition 仅间接支撑**：[Architecture](https://en.wikipedia.org/wiki/Architecture) 中的 `zoning` 仅出现 1 次且为「building codes and zoning laws」（法定用地分区），并非「把相近活动归并为连续区域」的功能分区定义；[Interior design](https://en.wikipedia.org/wiki/Interior_design) 含 `space planning`（×2）、`programming`（×11）、`functional design`、`effective use of space, user well-being`。可支撑「空间规划/功能设计」这一宽泛背景，但两页 extracts 中 `functional zoning`、`back of house`、`adjacency`、`workflow` 均未命中，definition 的精确表述无直接来源。
  - **time_or_place 无编造**：「跨时期、全球」为通约表述，无具体年份、人名、引文。
  - **overview 部分支撑**：`public buildings` 在 Interior design 页出现，但「公共、服务、后勤三类区域」的三分法在两页均无字面依据，属设计惯例性概括。
  - 七节：definition + sections 六节齐全；实例四项为「类型性实例（不指定具体项目）」，未虚构具体项目、设计者或年份，写法诚实；「常见错误与限制」含风险词「尺寸」并附「实际工程须按当地规范和专业设计人员的要求」；1 张 SVG 含「示意图，非施工图」；`needs_verification=true`、`pending_notes`「实例的功能分区数据与设计者待补独立来源」与正文「待核实」声明一致；双源；`related=["spatial-organization"]` 指向已写条目（L1）。
  - 元数据：`coverage.json` 中 tier=重要/period=跨时期/region=全球/level=L2/source_count=2/needs_verification_count=1/status=已写/last_updated=2026-11-22，与 batch-09 一致。
  - 相似度：短文本最高 `spatial-perception` 0.3436、全文最高 `enclosure` 0.4509；全库最高 0.4509，低于 0.54。
- 问题：
  - definition「把相近活动归并为连续区域，减少交叉干扰」与 overview「公共、服务、后勤三类区域」缺直接来源字面支撑，需在下一轮补一篇明确讲 functional zoning / space planning zoning 的权威来源，或改写为来源可核验的通约表述。
  - `pending_notes` 只覆盖「实例数据与设计者」，未覆盖上述定义/概述层面的来源缺口，建议同步扩展待核实范围。

### 2. `parametric-architecture`（参数化建筑）— 不合格

- 依据：
  - 来源 id 存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致；单源条目，`needs_verification=true` 已确认，`pending_notes` 非空，`coverage.json` 中 `needs_verification_count=1`，符合 D14 与 check.py 双源例外规则。
  - **核心定义无来源支撑（不合格主因）**：唯一来源 [Modern architecture](https://en.wikipedia.org/wiki/Modern_architecture) 的 extracts（75327 字符）中 `parametric`、`parametricism`、`algorithm`、`computational`、`digital`、`computer`、`Zaha Hadid`、`Gehry`、`Libeskind`、`21st century`、`blob`、`form-generated` 全部 0 命中，仅有 `postmodern`（×3）与 `organic`（×3，指 Wright 的 Usonian）。该页覆盖 19 世纪至 20 世纪现代主义/后现代，**不含参数化设计**。条目 definition「把几何关系写成可变参数，使形状随条件变化而生成连续族」、overview「以算法驱动表皮或结构布局」在该来源中零可核验依据。
  - **来源标题与条目主题不直接相关**：`Modern architecture`（现代建筑）≠ `参数化建筑`；参数化设计通常归为 20 世纪末至今的 Parametricism / 数字生成设计，与该来源条目主题不构成直接支撑关系，违反用户核对项 2「来源标题与条目主题直接相关」。
  - **time_or_place 与来源时期冲突**：条目写「当代、全球」，唯一来源为 Modern architecture（历史时期条目），`period` 与来源性质不一致，且来源未给「当代」依据。
  - **待核实声明与缺口不匹配**：`pending_notes`「仅一份直接来源；参数化实例的设计者与年代待补独立来源」只声明实例数据缺口，未声明核心定义/概述/时期本身无来源支撑；正文「待核实」节同样只写实例设计者与年代，正文与元数据虽形式一致（D14 通过），但**未如实反映最关键的事实性缺口**。
  - 未发现编造的具体年份、人名或引文（写「类型性实例」规避了虚构具体项目，这一点诚实）；七节齐全，1 张 SVG 含「示意图，非施工图」，风险词「尺寸」附规范提示；`related=["green-architecture"]` 指向已写条目（L1）；相似度短文本最高 0.2805、全文最高 0.4418，低于 0.54。
- 问题：
  - （Critical）核心定义、概述、时期缺可核验来源，且唯一来源标题与主题不直接相关——不满足「每条事实有来源且来源 verified」与「关键事实至少两个独立来源或标待核实」。
  - （Important）`period=当代` 与来源「Modern architecture」冲突，需改为来源可支撑的表述或补当代参数化设计的权威来源。
  - （Important）`pending_notes` 与正文「待核实」未覆盖核心定义/概述的来源缺口，需如实补充。

### 3. `place-spirit`（场所精神）— 待核实

- 依据：
  - 来源 id 均存在且 verified/link_ok 为 true，实抓 HTTP 200、H1 一致。
  - **definition 部分支撑**：[Place attachment](https://en.wikipedia.org/wiki/Place_attachment) 原文「Place attachment is the emotional bond between person and place」「sense of place」「Memories combine sensations and perceptions...」「places derive religious, historical, or other cultural meanings」「desires to preserve ecological or architectural characteristics of a place」支撑「历史、记忆、独特气质、认同」；[Environmental psychology](https://en.wikipedia.org/wiki/Environmental_psychology) 含 `place attachment`（×6）、`sense of place`（×2）、`place identity`（×8）、`Place identity` 专节。但两页 `genius loci`、`spirit of place` 均为 0 命中，「场所精神」这一具体概念未被来源直接界定；`materials` 在 Place attachment 页 0 命中，`historic` 仅出现 1 次且非「场所精神由材料构成」的表述。
  - **time_or_place 部分支撑**：「20世纪」与场所依恋理论的兴起时期大致相符，但 `region=欧洲` 在两页无直接字面依据（理论代表多为 Proshansky 等，来源未强调欧洲），属待核实。
  - **overview 部分支撑**：「保留场所记忆」命中记忆/特征保存；「运用地域材料与尺度」的 `materials`/`scale` 缺直接字面依据（Environmental psychology 的 `scale` 指量表，`materials` 指学习资料，均非设计尺度/地域材料）；`landscape`（×6/×7）、`urban` 支撑「更新与景观设计」的大背景。
  - 七节：definition + sections 六节齐全；实例四项为「类型性实例（不指定具体项目）」，未虚构具体项目、设计者或年份，写法诚实；「常见错误与限制」含风险词「安全」并附「实际工程须按当地规范和专业设计人员的要求」；1 张 SVG 含「示意图，非施工图」；`needs_verification=true`、`pending_notes`「具体场所的设计者与实测数据待补独立来源」与正文「待核实」声明一致；双源；`related=["spatial-perception"]` 指向同批已写条目（L2）。
  - 元数据：`coverage.json` 中 tier=重要/period=20世纪/region=欧洲/level=L2/source_count=2/needs_verification_count=1/status=已写，与 batch-09 一致。
  - 相似度：短文本最高 `bauhaus` 0.3099、全文最高 `enclosure` 0.4453；全库最高 0.4453，低于 0.54。
- 问题：
  - definition 中「材料」与「场所精神」具体概念、time_or_place 的「欧洲」、overview 的「地域材料与尺度」缺直接来源支撑；未编造年份、人名或引文，但建议补一篇界定 genius loci / sense of place 的权威来源，或把这些表述并入待核实并扩展 `pending_notes`。
  - `pending_notes` 仅覆盖「设计者与实测数据」，未覆盖上述概念与地域来源缺口。

## 单源条目与待核实占比监控

- 抽中三条中 `parametric-architecture` 为单源，已确认 `needs_verification=true`、`pending_notes` 非空、`coverage.json` 中 `needs_verification_count=1`，形式合规；但如前述，单源本身内容不支撑核心事实，构成本轮唯一「不合格」。
- batch-09 全批 6/6 条目 `needs_verification=true`（100%），不属于「待核实占比异常低」，不触发硬写降级。
- `tools/check.py` 实跑 `PASS: all checks, 0 errors`；三条的七节结构、1 张 SVG 图注、风险词规范提示、needs_verification 形式联动均无机器校验失败——说明本轮「不合格」是机器规则覆盖不到的来源相关性/事实支撑缺口，需人工抽检发现。

## 总体结论

- 结果：**合格 0 条**，**不合格 1 条**（`parametric-architecture`），**待核实 2 条**（`functional-zoning`、`place-spirit`）。抽检 3/6=50%，满足 ≥25% 且 ≥3 条。
- **是否建议整批返工：是。** 按 `AUTONOMOUS.md` E 节「抽检……不合格则整批返工」（前序 `research/rework-round06.md` 亦为 1 条不合格触发整批返工），本轮 `parametric-architecture` 判为不合格，已触发整批返工条件。返工重点：
  1. `parametric-architecture`（Critical）：补一篇真正覆盖参数化设计/Parametricism 的 verified 权威来源（用 Python urllib + UA 核对 H1 后写入 `sources.json`），据此重写 definition / overview / `period=当代`；若短期无法补源，则把核心定义/概述/时期明确并入 `pending_notes` 与正文「待核实」，并把 `period` 改为与唯一来源一致的表述。
  2. `functional-zoning`、`place-spirit`（定向补源/改写项）：为「公共/服务/后勤三分法」「材料」「场所精神/genius loci」「欧洲」等补权威来源或改为来源可核验的通约表述，并同步扩展 `pending_notes`。
  3. 未抽中的 `gray-space`、`spatial-perception`、`enclosure` 随整批返工做一次同类来源相关性自查（本轮未逐条核对，不单独下结论）。
- 未触发「相似度过高疑似套话」（最高 0.4509 < 0.54）与「待核实占比异常低」（100%）两项降级条件；除 `parametric-architecture` 的来源/事实支撑缺口外，未发现编造年份、人名或引文，七节结构、SVG 图注、风险词规范提示、`needs_verification`/`pending_notes`/正文声明的形式联动均通过。
- 按用户指令执行 25% 档抽检且至少 3 条，实际抽 3/6；下一轮抽检比例由 lead 按 `AUTONOMOUS.md` E 节决定。
