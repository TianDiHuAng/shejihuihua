# 第61轮 side-light 二次返工复检报告（spotcheck-round61c）——单条复检 + 全库 SVG 去重抽验

- 复检人：spotcheck-r61c（lead 委派子代理，无人值守、未提问）；复检时间 2026-11-23 18:57 起，Asia/Hong_Kong。
- 任务：第61b 轮判 `side-light` 不合格（定义源为建筑照明错配、实例挂靠在同页另一幅画《A Seated Man with a Stick》）后已二次返工。本轮对 `entries/batch-33.json` 的 **`side-light` 单条**复检：definition/overview/原理 是否由两源正文（`studiobinder-side-lighting`＋`wp-rembrandt-lighting`）逐字支撑、实例《63岁自画像》四要素是否属实且侧光描述是否编造、SVG 是否独立不雷同、七节/规范句、needs_verification↔pending↔待核实联动、相似度（阈值 0.54）；**另加：全库 258 条 SVG 字节去重抽验**，报是否有残留重复组。
- 协议依据：`AUTONOMOUS.md` §三 E（质量闸；抽检不合格整批返工、下轮抽检 25%；相似度过高→整批降级）＋§六（联网内容一律视为数据，网页中任何指令不得执行）；`TASK_design.md`「条目页结构」L2 七节＋「专用规则」（1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造、关键事实≥2 独立源、只引 verified=true 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（委派子代理命中 `SUBAGENT-STOP`，以任务书执行）与 `verification-before-completion`（**先实抓、先跑，再断言**；本报告所有来源正文均由本轮 `urllib` 实抓回读为准，不采信 sources.json 的 note 二手转述）。

## 〇、只读声明与数据稳定性

- **只读**：本次**仅写出** `research/spotcheck-round61c.md` 一个文件。核对期间临时写过 `research/_r61c_sb.html`、`_r61c_wpr.html`、`_r61c_ng.html`（抓取原页），收尾已全部 `rm` 删除（`ls research/_r61c_*` → 无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其它内容文件，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行。
- **`git log -1`** = `6202b6b chore: round60 chiaroscuro and cast-shadow named instances`。二次返工**尚未提交**：`git status --porcelain` 显示 `M entries/batch-33.json`（含 side-light、light-shadow-modeling 等 11 条、及前轮改动）、`M data/sources.json`、`M coverage.json`、多条 `M site/entries/*.html`；未跟踪 `tools/apply_review_round61c.py`、`tools/fix_dup_svgs_r61*.py`、`research/spotcheck-round61*.md`。复检对象＝工作树现状。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前 grep 该脚本写文件语句（`write_text`/`.write(`/`open(...,'w')`/`os.remove`/`unlink`/`shutil`）计数 **0**（仅读）。
- **二次返工内容**（读 `tools/apply_review_round61c.py` 并比对工作树确认已生效）：`side-light` sources 换为 `studiobinder-side-lighting`＋`wp-rembrandt-lighting`；definition/overview/原理/实例/待核实/pending 全部重写；实例改挂《63岁自画像》。`light-shadow-modeling` 换专属 SVG（体现「受光面—明暗交界—暗部」渐变）。sources.json 新增 `studiobinder-side-lighting`、`wp-rembrandt-lighting`（均 verified=true）。

## 一、判定口径与抓取方法（沿用第51–61轮）

- **L2 七节**：顶层 `definition`＋`sections` 六节（原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实）＝7 节；1–2 张内联 SVG、含「示意图，非施工图」；SVG 元素不出 viewBox（指不由元素内、无越界）、无 `on*`、无外链图；「常见错误与限制」以规范句收尾。
- **抓取**：`urllib`＋浏览器 UA＋非校验 SSL 实抓并回读，去 `<script>/<style>` 与标签→`html.unescape`→`norm()`（去空白＋小写）子串回验。本轮实抓（HTTP 200）：`studiobinder-side-lighting`(336464B)、`wp-rembrandt-lighting`(151129B)、`ng-rembrandt-self63`(128971B)。
- **三级判定**（沿用）：**合格**＝definition/time/overview/实例均获所引来源正文直接支撑，关键事实≥2 独立源直证或强权威官方源直证＋第二源，无编造，机械项全过或有轻微项；**待核实**＝核心获实质支撑，但某关键事实实质单源/无源或为来源未逐字作出的解读，nv=true 且 pending/正文如实披露；**不合格**＝definition/overview 主干被所引来源均不支撑、实例核心四要素无源或挂错对象、或关键结构项（七节/SVG）实质不满足。
- **相似度**：`difflib.SequenceMatcher`；①短文本＝title+definition+time_or_place+overview；②全字段-不含 SVG＝definition+time_or_place+overview＋六节正文（含「一图」解说）。norm＝去全部空白＋小写。全库 258 条扫描，阈值 0.54。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**（与第39–61轮逐位一致，口径正确）。

## 二、side-light definition / overview / 原理 是否由两源正文支撑

- 条目现状（工作树）：definition＝「侧光指光源位于被摄体一侧、从侧面照来的照明。」；overview＝「侧光在一侧受光、另一侧落影，能凸显表面特征与质感，明暗对比强。」；原理＝「光线从侧面掠过表面：迎光面亮、背光侧落影，凸处迎光、凹陷背光，因而放大质感与起伏。」sources＝`studiobinder-side-lighting`、`wp-rembrandt-lighting`。

### 2.1 StudioBinder（实抓逐字直证「从一侧照来 / 凸显质感 / 另一侧落影」）

- 直证句（实抓 `studiobinder.com/blog/what-is-side-lighting/`，norm 回验）：
  - `Side lighting is a lighting technique that directs a light source from one side of a subject.`（光源从主体**一侧**照来）→ 「光源位于被摄体一侧、从侧面照来的照明」**逐字命中** ✓。
  - `...ultimately is defined by exposing only one side of a subject.`（仅一侧受光）✓。
  - `...side lighting also brings out the features and texture in a subject. Since the light is coming from a side angle, the smallest features cast shadows making them more pronounced.`（**凸显特征与质感**、侧角投射阴影）→ 「凸显表面特征与质感」「凸处迎光、凹陷背光、放大质感与起伏」**支撑** ✓。
  - 同页 `down the middle between light and dark`、`add contrast` 等述明暗对比 → 「明暗对比强」支撑 ✓。
- 关键词命中：`side lighting`×37、`side light`×49、`from one side`×1、`one side of`×4、`texture`×1、`shadow`×4。**结论：定义主干「从一侧照来」「质感」「另一侧落影」全部由 StudioBinder 正文逐字／实质支撑。**

### 2.2 Wikipedia Rembrandt lighting（实抓逐字直证「一侧明暗对照」）

- 直证句（实抓 `en.wikipedia.org/wiki/Rembrandt_lighting`，norm 回验）：
  - `One side of the face is lit well from the main light source while the other side of the face uses the interaction of shadows and light, also known as chiaroscuro, to create this geometric form on the face.`（**一侧受光、另一侧以阴影与光—即明暗对照—塑形**）→ 「一侧受光、另一侧落影」「明暗对照塑造结构」**逐字命中** ✓。
  - 同页 `the key light is placed high and to one side at the front`、`illuminated triangle...on the less illuminated side`（一侧高光/另一侧较暗、三角光）→ 强化「一侧受光一侧背光」语义 ✓。
- 关键词：`rembrandt lighting`×23、`one side`×2、`chiaroscuro`×2、`triangle`×4、`shadow`×5。
- **结论：定义/原理的「一侧受光、另一侧落影、明暗对照」由 Rembrandt lighting 百科正文逐字直证。** 两源互补：StudioBinder 提供「从一侧照来＋质感」，Wikipedia 提供「一侧明暗对照」，**双独立权威源逐字直证 definition/overview/原理** ✓。

### 2.3 上一轮「建筑照明错配」缺陷是否消除

- 旧源 `wp-architectural-lighting-design`、`wp-daylighting-architecture` **已从 side-light.sources 移除**（现仅 studiobinder＋wp-rembrandt-lighting 两源）。第61b 的致命缺陷（两定义源为建筑照明/采光、全文无侧光术语）**已消除** ✓。

## 三、实例《63岁自画像》真实性核对

- 条目实例（工作树）：「名称：《63岁自画像》（Self Portrait at the Age of 63）；地点：英国伦敦国家美术馆（NG221）；作者：伦勃朗（Rembrandt）；年份：1669 年。面部一侧受光另一侧沉入阴影，以明暗对照塑造结构。此处仅列名称、地点、作者与年份信息，不复制图像。」
- **NG 官方页实抓逐字核对**（`nationalgallery.org.uk/paintings/rembrandt-self-portrait-at-the-age-of-63`，HTTP 200，128971B）：
  - 名称 `Self Portrait at the Age of 63` ✓；编号 `NG221`×2 ✓；作者 `Rembrandt` ✓；年份 `1669`（`Rembrandt, 'Self Portrait at the Age of 63', 1669`）✓；`National Gallery, London` ✓。**四要素全部由 NG 官方源直证，无编造** ✓。
- **侧光描述核对**：NG 对该自画像正文原文 `...turned a spotlight on his features. The beam bounces off his high forehead and the tip of his nose... By contrast, the dark, shadowy background is thinly painted...` 另述其「experiment with lighting effects / light effects that he used to emphasise his face」「modelling the skin in three dimensions」。→ NG 明述「聚光投向面部、深色阴影背景、以光效强调面部、三维塑造」，但**并未逐字使用「one side lit / other side in shadow / chiaroscuro」描述该自画像**。
- **关键纠错**：NG 全页唯一的 `lit dramatically from one side` 仍指向**同页相关作品《A Seated Man with a Stick》（Follower of Rembrandt）**，**并非**《63岁自画像》——即第61b 指出的「实例挂靠另一幅画」的坑仍在原文里。**但本轮实例描述已不再引用该错误原句**：实例改述为「面部一侧受光另一侧沉入阴影，以明暗对照塑造结构」，是基于「伦勃朗光（Rembrandt lighting）」概念对该自画像面部明暗特征的**解读**，而非照抄《A Seated Man》那句，也非对四要素的编造。
- **结论**：实例四要素**属实无编造**；「面部一侧受光/一侧沉入阴影、以明暗对照」为**据 Rembrandt lighting 特征所作的合理解读**（NG 原文述聚光+阴影背景+三维塑造，方向一致，但未逐字作出侧光/明暗对照判断）。此解读已入 `needs_verification=true`＋pending／待核实如实披露 → 属「待核实（合理推断已披露）」而非「不合格（挂错对象＋编造）」。**第61b 的「实例挂靠另一幅画」致命项实质解除**（不再引用错误原句，四要素直证）。

## 四、L2 七节 + SVG + 规范提示（程序化实核）

| 条目 | def 顶层 | sections 6 节 | SVG 数 | viewBox | 「示意图，非施工图」 | on*/外链图 | 规范句收尾 | SVG 几何越界 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| side-light | ✓ | 6/6（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 1 | `0 0 760 400` | ✓ | 无/无（无 `<image>`、无 xlink、无外链 http） | ✓ 以「实际工程须按当地规范和专业设计人员的要求」收尾 | 无（rect/line/polygon/text 均在 0–760×400 内） |

- **SVG 语义贴合**：side-light SVG＝`rect x=300`（竖立主体）、`line x1=80→x2=290 + polygon 箭头`（自左向右的**侧向光源**）、文字「侧向光源」「示意图，非施工图」。图形为「矩形主体 + 从左侧横向射入的箭头光源」，**表达侧光（光源在一侧、水平掠过）**，与本条「光源来自一侧、明暗各半」的「一图」文字一致 ✓。
- **SVG 唯一性**：全库 258 条按 svg 字符串精确比对，side-light SVG 仅 1 条、与他条**均不相同**（`same_as=[]`）✓。

## 五、needs_verification ↔ pending ↔ 正文待核实 联动 + 元数据一致 + 相似度

- **元数据一致**：`coverage.json` side-light（L2 / 已写 / source_count=2 / needs_verification_count=1）↔ entry（sources 长度=2 / needs_verification=True）逐项匹配 ✓。
- **联动表**：

| 项 | 值 |
| --- | --- |
| needs_verification | **true** |
| pending_notes | 「实例侧光为据伦勃朗光特征的解读；概念已双源。」 |
| 正文「待核实」节 | 「侧光概念由 StudioBinder 与 Wikipedia（伦勃朗光）双源直证；实例《63岁自画像》的伦勃朗式侧光为据其明暗对照特征的解读。」 |
| 联动一致性 | **结构一致且披露准确 ✓**：如实区分「概念双源直证」与「实例侧光为解读」，与本轮实际（定义由两源直证、实例侧光为推断）完全相符；无把错配源当「背景」的误导（旧「Tate 背景」表述已删） |

### 相似度（difflib 去全部空白＋小写，阈值 0.54；全库 258 条）

| 条目 | ①短文本 max | ②全字段-不含SVG max |
| --- | --- | --- |
| side-light | **0.3875 vs back-light** | **0.3726 vs back-light** |

- 批内两两（全字段）：side-light vs back-light 0.3726、side-light vs light-shadow-modeling 0.3426，均远 <0.54 ✓。
- **方法自校**：`futurism vs expressionism` 全字段②＝**0.5157**，与第39–61轮逐位一致，口径正确。
- side-light 对全库与批内均 PASS（<0.54）✓。

## 六、全库 SVG 去重抽验（另加项）

- **方法**：读 `entries/*.json` 全部 258 条，按每条 `svg` 列表逐串精确比对（字符串完全相等），聚成重复组。
- **结果**：**重复组 = 0**。全库 258 条 **无任意两条 SVG 字符串完全相同**。
- **对照第61b 的残留问题**：第61b 发现 `light-shadow-modeling` 的 SVG 与 `cast-shadow`/`highlight`/`reflected-light`/`core-shadow`/`front-light`/`top-light` 共 6 条字节完全相同（通用图复用）；本轮二次返工后复核——`light-shadow-modeling` SVG 与他条 **均不同**（`same_as=[]`），其专属 SVG 绘「受光面—明暗交界—暗部」渐变；上述 6 条各自 SVG 长度分别为 512/319/459/368/443/509，亦**互不相同**。该通用图复用组**已解散** ✓。
- **结论：全库无两条 SVG 完全相同，无残留重复组。**（注：本项仅核「字符串完全相同」的硬重复；语义近似/同构不同字节的软雷同不在本次抽验范围。）

## 七、逐条验收结论

| 条目 | definition/overview/原理 来源支撑 | 实例真实性 | 七节/规范/SVG | nv·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **side-light（侧面光）** | **双源逐字直证**：StudioBinder（`from one side of a subject`/`brings out the features and texture`/`cast shadows`）＋Wikipedia Rembrandt lighting（`One side of the face is lit well... the other side... shadows and light, also known as chiaroscuro`）→「从一侧照来、质感、一侧明暗对照」全部支撑；建筑照明错配两源已移除 | 四要素（NG221/1669/Rembrandt/National Gallery）NG 官方源**直证、无编造**；「一侧受光/一侧沉入阴影」为据伦勃朗光特征的解读（已披露），不再挂靠《A Seated Man with a Stick》错误原句 | 七节齐、规范句✓；1 SVG 唯一、表达侧光、无越界 | nv=True↔pending↔待核实**结构一致且披露准确** | ✓（0.3875/0.3726） | **合格**（第61b 不合格缺陷已实质修复） |

### 问题清单

- **① side-light 定义主干无源（第61b 严重项）→ 已修复**：两建筑照明源移除，换 `studiobinder-side-lighting`（`from one side of a subject`/texture/shadows）＋`wp-rembrandt-lighting`（one side lit / other side chiaroscuro）双源逐字直证。**结论：合格。**
- **② side-light 实例挂靠另一幅画（第61b 严重项）→ 已实质解除**：实例四要素改由 NG《63岁自画像》官方页直证；描述不再引用指向《A Seated Man with a Stick》的 `lit dramatically from one side` 原句。「一侧受光」为据伦勃朗光特征对该自画像面部明暗（NG 述聚光+深阴影背景+三维塑造）的合理推断，已入 nv/pending 如实披露。**结论：合格（实例侧光为已披露解读）。**
- **③ side-light pending 披露误导（第61b 治理项）→ 已修复**：旧「概念有 Tate 背景」删除；pending/待核实改为「概念双源直证、实例为解读」，与实际一致。**结论：合格。**
- **④ light-shadow-modeling 通用图复用（第61b 中等项）→ 已整改**：专属 SVG「受光面—明暗交界—暗部」，全库去重已无与其相同者。**结论：已修复。**
- **⑤ wp-rembrandt-lighting.link_ok=null（维护·轻微）**：本轮实抓 HTTP 200 可达，仅未写入 link_ok=true，建议补记。（不构成内容判定问题）
- **⑥ side-light 实例「一侧明暗对照」为概念推断（轻微·已披露）**：NG 对该自画像未逐字作「one side / chiaroscuro」判断（该措辞仅见于同页《A Seated Man》）；实例表述系据伦勃朗光特征解读，nv=true 已如实标注。可进一步以「据伦勃朗光特征推断」措辞微调更稳妥，但当前披露已充分，不构成不合格。

## 八、总体结论

- **单条复检：`side-light` = 合格。** 第61b 判不合格的两项致命缺陷（定义源建筑照明错配、实例挂靠同页另一幅画）**均已实质修复**：
  1. **定义双源逐字直证**——`StudioBinder`「a light source from one side of a subject / brings out the features and texture / cast shadows」＋`Wikipedia Rembrandt lighting`「One side of the face is lit well... the other side... shadows and light, also known as chiaroscuro」，覆盖「从一侧照来 / 质感 / 一侧明暗对照」全部要点，双独立权威源。
  2. **实例四要素真**——NG 官方页直证 `Self Portrait at the Age of 63 / NG221 / Rembrandt / 1669 / National Gallery, London`，无编造；「一侧受光/一侧沉入阴影」为据伦勃朗光特征对该自画像面部明暗的解读，已在 nv/pending/待核实如实披露，且不再引用指向《A Seated Man with a Stick》的错误原句。
- **结构/治理**：七节齐（definition＋6 节）、1 张内联 SVG 唯一且表达侧光、含「示意图，非施工图」、无 `on*`/无外链/几何无越界、规范句收尾；元数据 coverage↔entry 一致（src=2/nvc=1/nv=True）；`check.py PASS 0 errors`。
- **相似度**：side-light 对全库（短 0.3875 / 全字段 0.3726）与批内（vs back-light 0.3726、vs lsm 0.3426）均 <0.54；方法自校 0.5157 一致。
- **全库 SVG 去重抽验**：258 条，**重复组 = 0，无两条 SVG 完全相同**；第61b 的 light-shadow-modeling 通用图复用组（原 7 条同字节）**已解散**，相关条目 SVG 互不相同。
- **是否整批返工 / 降级**：
  1. §E「抽检不合格→整批返工（25%）」：**本轮 side-light 已合格**（原唯一不合格项消除），本项不再触发的**前提**成立；唯 §E 触发判定应以本轮抽检整体为准，本条本身不再产生新不合格。建议下轮抽检比例可回调（由 25% 起，视整体批次质量再定）。
  2. §E「相似度过高→整批降级」：**不成立**（0.3875/0.3726 <0.54）。
  3. §E「待核实占比异常低→整批降级」：**不成立**（side-light nv=True 且披露准确）。
- **修复/维护建议**：
  1. **（维护）** 补记 `wp-rembrandt-lighting.link_ok=true`（实抓 200 可达）。
  2. **（措辞·可选）** 实例可将「面部一侧受光另一侧沉入阴影，以明暗对照塑造结构」微调为「据伦勃朗光特征，其面部呈现一侧受光/一侧明暗对照的解读」，使推断色彩更醒目（当前 nv/pending 已披露，非阻断）。
  3. **（常规）** 全库软雷同（同构不同字节）建议后续体检，非本次硬重复范围。

### 机器可读汇总

```
ROUND=61c
SAMPLER=spotcheck-r61c
MODE=第61轮 side-light 二次返工复检(单条) + 全库258条SVG字节去重抽验
SCOPE=["side-light"]
FILES={"side-light":"entries/batch-33.json side-light"}
GIT_HEAD="6202b6b chore: round60 chiaroscuro and cast-shadow named instances"; REWORK_COMMITTED=false
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); check.py write-statements grep count=0"
FETCH_METHOD="urllib+UA+unverified-SSL HTTP200 readback: studiobinder-side-lighting(336464B), wp-rembrandt-lighting(151129B), ng-rembrandt-self63(128971B)"
DEFINITION_SUPPORT={
 "studiobinder":"'Side lighting is a lighting technique that directs a light source from one side of a subject' + 'exposing only one side' + 'brings out the features and texture...smallest features cast shadows' + 'down the middle between light and dark' -> supports 从一侧照来/质感/另一侧落影 VERBATIM",
 "wp_rembrandt":"'One side of the face is lit well from the main light source while the other side of the face uses the interaction of shadows and light, also known as chiaroscuro' + 'key light placed high and to one side' -> supports 一侧明暗对照 VERBATIM",
 "two_source_dual_direct":true,
 "old_architectural_sources_removed":true}
INSTANCE={
 "four_facts":"NG221/1669/Rembrandt/National Gallery,London ALL verified verbatim on NG official page (HTTP200)",
 "side_light_claim":"'面部一侧受光另一侧沉入阴影,以明暗对照' is INTERPRETATION from Rembrandt-lighting feature; NG describes spotlight-on-features + dark shadowy background + 3D modelling, does NOT verbatim say one-side/chiaroscuro for THIS portrait; disclosed via nv=true/pending",
 "mis_anchor_to_other_work":"The only 'lit dramatically from one side' on NG page refers to 'A Seated Man with a Stick' (other work) — entry NO LONGER quotes that wrong sentence; four facts are of the Self Portrait itself",
 "fabrication":0}
L2_CHECK={"seven_sections":"definition+6/6","svg_count":1,"svg_phrase":"示意图，非施工图","viewBox":"0 0 760 400; no on*/no external image","risk_note":"实际工程须按当地规范和专业设计人员的要求","svg_out_of_viewbox":0,"svg_semantic":"rect subject + left-to-right arrow = side light, matches 一图"}
SVG_SIDE_LIGHT_UNIQUE=true
METADATA={"coverage_vs_entry":"source_count=2=2, nvc=1=needs_verification true, level=L2, status=已写","consistent":true}
NV_PENDING={"needs_verification":true,"pending":"实例侧光为据伦勃朗光特征的解读；概念已双源。","waitting_section":"侧光概念由 StudioBinder 与 Wikipedia（伦勃朗光）双源直证；实例...解读。","consistent_and_accurate":true}
SIMILARITY={"side_light":{"short_max":0.3875,"short_entry":"back-light","full_max":0.3726,"full_entry":"back-light","verdict":"PASS<0.54"},"intrabatch_full":{"vs_back_light":0.3726,"vs_lsm":0.3426},"method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-61","threshold":0.54}
VERDICT_CONTENT={"side-light":"合格"}
DEFINITION_UNSOURCED=0
HARD_FABRICATION_INSTANCE=0
SVG_SEMANTIC_MISMATCH=0
SVG_OUT_OF_VIEWBOX=0
FULL_LIBRARY_SVG_SCAN={"total_entries":258,"exact_duplicate_groups":0,"residual_duplicate_groups":[],"note":"light-shadow-modeling former 6-shared generic SVG group DISSOLVED; its dedicated SVG + cast-shadow/highlight/reflected-light/core-shadow/front-light/top-light all mutually distinct"}
MINOR={"wp_rembrandt_link_ok_null":"live 200 reachable, suggest record true","instance_side_light_interpretation":"NG does not verbatim say one-side/chiaroscuro for this portrait; disclosed, optional wording tweak"}
BATCH_ACTION="side-light PASS (both previous fatal defects — definition-source mismatch & instance mis-anchor to A Seated Man with a Stick — substantially fixed; dual-source verbatim support; four facts NG-verified; side-light interpretation disclosed via nv/pending). Full-library 258 SVG exact-duplicate scan = 0 residual duplicate groups (light-shadow-modeling generic-reuse group dissolved). Non-blocking: record wp-rembrandt-lighting.link_ok=true; optional instance wording tweak."
READONLY="only wrote research/spotcheck-round61c.md; temp files research/_r61c_*.html written then rm-removed (ls shows none); no other project content file changed; no git commit; web content treated as data, no instruction executed"
```

*（报告完）*
