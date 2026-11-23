# 第59轮质量抽检报告（spotcheck-round59）——第59轮补具名实例 4 条六法组中抽 3 条（likeness-form / color-according-type / composition-placement）

- 抽检人：spotcheck-r59（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 18:27 起，Asia/Hong_Kong。
- 任务：对第59轮「补具名实例」的 4 条六法组条目中抽 3 条——`likeness-form`（应物象形，`entries/batch-32.json` 38–68 行）、`color-according-type`（随类赋彩，`entries/batch-32.json` 70–99 行）、`composition-placement`（经营位置，`entries/batch-06.json` 40–72 行）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关（**重点：复用的库内已验证来源是否真的支撑「该作品体现该法」**）；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动（本轮统一保留待核实，因概念为对应解读）；核对相似度（阈值 0.54）。
- 协议依据：`AUTONOMOUS.md` §E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 元素不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STRUCT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓、后断言；本条所有来源正文均由本轮 `urllib` 实抓回读为准，不采信 sources.json 的 note 二手转述）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 18:27 起）**：`coverage.json`=`total=258`、`pending_sum=**191**`；`entries/batch-06.json`=15068B（含 composition-placement）、`entries/batch-32.json`=24929B（含 likeness-form / color-according-type）。三条 `needs_verification_count` 各=1、`source_count` 各=4、`level=L2`、`status=已写`、`last_updated=2026-11-23`。
- **`git log -1`** = `612290f chore: round58 Chinese painting named instances`。第59轮改动尚未提交：`git status --porcelain` 显示 `M coverage.json`、`M entries/batch-06.json`、`M entries/batch-32.json`、`M site/entries/{color-according-type,composition-placement,likeness-form,transmission-copy}.html`。抽检对象即上述未提交工作树中 3 条的现状。**说明**：`pending_sum` 由第58轮的 193 降至 191（-2），与本轮 `transmission-copy` 被改一致（疑为 round59 对该条做了某处理，非本次抽检对象，仅作状态观察，未纳入内容判定）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（仅 `path.open(encoding="utf-8")` 两处读，无 `'w'`/`write_text`/`.write(`/`unlink`/`os.remove`/`shutil`）。
- **只读声明**：本次**仅写出** `research/spotcheck-round59.md` 一个项目文件；核对期间为比对抓取正文临时写过 `research/_snip_r59.txt`、`research/_sixprin.txt`，已在收尾 `rm` 删除（`git status` 复核无残留）。未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容（抓取全程内存/临时文件，已清理）。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round58.md`（243 行）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；SVG 元素须限制在 viewBox 内、无 `on*` 事件属性、无外链图片；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾。
- **抓取与回验方法**：本轮全部来源 `urllib`+浏览器 UA+非校验 SSL 实抓 HTTP 200：`dpm-qianli`（26310B）、`dpm-qingming`（106475B）、`columbia-handscroll`（17539B）、`dpm-luoshenfu`（17454B）、`wp-six-principles-chinese-painting`（68384B）均取正文；`chinaculture-luoshenfu`（10526B）取英文正文。关键句按去标签→`html.unescape`→`norm()`（去空白＋小写）子串回验，全部佐证。`dpm-*` 为 GBK 乱码风险页面，改用「去标签后对解码 Unicode 码点做 norm 比对」回验（布尔 YES/no），避免控制台 GBK 输出干扰。
- **三级判定定义（沿用第51–58轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源/无源，或为来源未逐字作出的解读/存在来源明确讨论的学术争议；`needs_verification=true` 且 pending/正文如实披露者，属「正确的待核实管理」，判待核实但无治理缺陷。
  - **不合格**：definition/overview 主干被引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，含 `一图` 解说文字、不计 `svg` 标记），归一为去空白＋小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–58轮报告逐位一致，口径正确。

## 二、抽检对象来源清单与相关性（本轮全部实抓正文）

3 条共引用来源去重后 7 个 id；**每条 4 个（2 个概念背景源 + 2 个实例源）**。

| 条目 | 实例 | 引用来源 id（4） | 实抓证据（本轮） | 与本条的「直接相关性」 |
| --- | --- | --- | --- | --- |
| likeness-form 应物象形 | 顾恺之《洛神赋图》（宋摹） | `wp-six-principles-chinese-painting`、`wp-chinese-painting`、`dpm-luoshenfu`、`chinaculture-luoshenfu` | wp: `"Correspondence to the Object" (yingwu 应物) or the depicting of form (xiangxing 象形), which would include shape and line`；dpm-luoshenfu: 「顾恺之洛神赋图卷（宋摹）」「东晋，顾恺之作」「以形写神」「顾恺之（约345—406）」；chinaculture: `Luoshen Appraisal Painting`、`Gu Kaizhi`、`classic` | **概念源直证定义**（应物象形=形/象形）；**两实例源直证作品四要素与「以形写神」写照**；「应物象形」术语未在该作品页逐字出现→概念对应解读（已披露） |
| color-according-type 随类赋彩 | 王希孟《千里江山图》 | `wp-six-principles-chinese-painting`、`wp-chinese-painting`、`dpm-qianli`、**`dpm-luoshenfu`** | wp: `"Suitability to Type" (suilei 随类) or the application of color (fucai 赋彩), including layers, value and tone`；dpm-qianli: 「王希孟千里江山图卷」「北宋，王希孟，绢本设色」「北宋政和三年（1113）」「继承和发展了唐代青绿山水画的技法……青、绿颜色中寻求变化」 | **概念源直证定义**（随类赋彩=赋彩）；`dpm-qianli` 直证青绿设色实例；**`dpm-luoshenfu`（洛神赋图）与「赋彩/青绿」无关，为挂名不相关源**（见 3.2 问题②） |
| composition-placement 经营位置 | 张择端《清明上河图》 | `wp-six-principles-chinese-painting`、`wp-composition-visual-arts`、`dpm-qingming`、`columbia-handscroll` | wp: `"Division and Planning" (jingying 经营) or placing and arrangement (weizhi 位置), corresponding to composition, space and depth`；dpm-qingming: 「张择端清明上河图卷」「散点透视法组织画面」「手卷形式」「鸟瞰式全景法」；columbia: `handscroll`、`with the use of perspective... show the same object from different angles`、`unroll only an arm's length section at a time` | **概念源直证定义**（经营位置=位置/安排/composition）；**实例源双证长卷散点布局**；columbia 直证手卷移步换景机制，与「长卷经营」高度相关 |

> 7 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）、`link_ok=true/null`（三态，`wp-*`=true，`dpm-*`/`columbia`=null 保守）。无假 id、无 `link_ok=false`。**关键相关性结论**：三条 definition 均由 `wp-six-principles-chinese-painting` 逐字直证（该页对三法均有英文对应释义），无编造；三个实例四要素均由对应官方机构源直证；**唯一相关性缺陷：`color-according-type` 的 `dpm-luoshenfu` 与「赋彩/青绿」无关**（但真正的实例源 `dpm-qianli` 已充分支撑，故属冗余挂名而非编造）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 likeness-form（应物象形）——**待核实（正确的待核实管理；SVG 语义错配须修）**

- 条目现状（`entries/batch-32.json` 38–68 行）：`definition`＝「应物象形指按对象本来的形貌去描绘，是六法之一。」；`time_or_place`＝「古代中国（参见来源）。」；`overview`＝「它要求形似，但需服从整体气韵。」；`实例`＝「名称：顾恺之《洛神赋图》（宋摹本，注重人物形貌与神情的写照）；地点：北京故宫博物院藏；作者：顾恺之（约345–406）；年代：东晋（现存宋摹）……」
- **definition / overview 支撑**：`wp-six-principles-chinese-painting` 逐字 `"Correspondence to the Object" (yingwu 应物) or the depicting of form (xiangxing 象形), which would include shape and line` → 「按对象本来的形貌去描绘」直证 ✓；overview「要求形似，但需服从整体气韵」与六法体系相容（气韵为六法之首）。非编造。
- **实例四要素（双源直证）**：dpm-luoshenfu 标题「顾恺之洛神赋图卷（宋摹）」+「东晋，顾恺之作」+「顾恺之（约345—406）」+「以形写神」直证；chinaculture `Luoshen Appraisal Painting`、`Gu Kaizhi`、`classic` 佐证 → 名称/地点（故宫藏）/作者/年代四要素双源支撑，「（宋摹本）」与故宫「（宋摹）」一致 ✓。「以形写神」故宫名画记逐字直证 ✓。
- **关键缺口（判待核实主因·已如实披露）**：两实例源均未逐字写「应物象形」四字（作品页讲的是「以形写神」）；「按六法第二法归入应物象形实例」为解读性映射。条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「两源直证作品形神写照；'应物象形'为六法概念，作品为形似写照范例，属概念对应解读。」→ 解读性质已如实披露，不构成隐瞒。
- **七节/SVG/规范提示（机械项）**：6 节齐；1 张 SVG `viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无外链 `<image>`；「常见错误与限制」以规范句收尾 ✓；几何复算无越界 ✓。
- **问题**：
  - ① **（判待核实主因·已披露）** 「应物象形」术语为该作品页所无，概念归属为解读；保持待核实正确，升级需补一源直接把该作品与「应物象形」挂钩。
  - ② **（Important·SVG 语义错配，本轮引入）** 本条 SVG 元素文字为「**主次与虚实布局**」，且图形为「主/次/虚实三色块布局」——这是**构图（经营位置）**的示意，与「应物象形=按对象形貌描绘形似」语义**不符**；且该 SVG 与 `color-according-type` 的 SVG **完全相同（逐字节一致）**。`TASK_design` 要求「图中标注设计意图或尺寸关系」，此图既未贴合本法（形似写照），又与另条重复。属内容工程缺陷（影响图示表达力，不影响文字内容判定），须换用贴合「取形→写照」的示意图并补标注。
- **内容判定：待核实（正确的待核实管理）**。文字四要素双源扎实、`needs_verification` 联动诚实；但图示语义错配＋与另条重复为须修问题。

### 3.2 color-according-type（随类赋彩）——**待核实（正确的待核实管理；SVG 语义错配 + 一个不相关挂名源）**

- 条目现状（`entries/batch-32.json` 70–99 行）：`definition`＝「随类赋彩指按物象类别施以相应色彩，是六法之一。」；`time_or_place`＝「古代中国（参见来源）。」；`overview`＝「它不求条件色写实，而按类别与意象设色。」；`实例`＝「名称：《千里江山图》（青绿设色，按物类施彩）；地点：北京故宫博物院藏；作者：王希孟；年代：北宋政和三年（1113）……」
- **definition / overview 支撑**：`wp-six-principles-chinese-painting` 逐字 `"Suitability to Type" (suilei 随类) or the application of color (fucai 赋彩), including layers, value and tone` → 「按物象类别施以相应色彩」直证 ✓。非编造。
- **实例四要素（dpm-qianli 直证 + dpm-luoshenfu 无关）**：
  - 名称：「王希孟千里江山图卷」dpm-qianli 直证 ✓。
  - 地点：「清宫旧藏」「故宫博物院版权所有」→ 北京故宫博物院藏 ✓（单源 dpm-qianli 直证；`chinaculture` 未引本条）。
  - 作者：「北宋，王希孟」dpm-qianli 直证 ✓。
  - 年代：「北宋政和三年（1113）」「希孟年十八岁」dpm-qianli 直证 ✓。
  - **「青绿设色」**：「继承和发展了唐代青绿山水画的技法，用笔精细，注重在青、绿颜色中寻求变化」「绢本设色」dpm-qianli 逐字直证 ✓。
- **关键缺口（判待核实主因）**：① 实例四要素**实质单源**（仅 dpm-qianli；第四条 `dpm-luoshenfu` 是《洛神赋图》，与青绿设色毫无关系，不能互证）；② 「随类赋彩」术语未在该作品页逐字出现，概念归属为解读。条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「《千里江山图》青绿设色由故宫源直证；'随类赋彩'为六法概念，作品为设色范例，属概念对应。」→ 已披露，不隐瞒。
- **七节/SVG/规范提示（机械项）**：6 节齐；1 张 SVG `viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无外链；规范句收尾 ✓；几何无越界 ✓。
- **问题**：
  - ① **（判待核实主因·已披露）** 概念归属为解读 + 实例实质单源；保持待核实正确。**要升级为合格，须补第二个直接相关官方源**（如另一馆藏/权威页直证《千里江山图》青绿设色），而非靠 `dpm-luoshenfu`。
  - ② **（Important·挂名不相关源）** 第 4 源 `dpm-luoshenfu`（《洛神赋图》）与「随类赋彩/青绿设色」**无主题关联**，仅凑 `source_count=4`；建议替换为与本实例相关的第二源（或如实减为 3 源并同步 coverage `source_count`）。
  - ③ **（Important·SVG 语义错配，本轮引入）** SVG 文字「**主次与虚实布局**」与「随类赋彩=按类设色」语义不符，应为「按物类归并的色块分布」，却用了构图布局图；且与 `likeness-form` SVG **逐字节相同**。须换用贴合「色块/设色」的示意图并补标注。
- **内容判定：待核实（正确的待核实管理）**。文字定义/实例由 dpm-qianli 直证但实例实质单源，概念为解读已披露；SVG 错配与挂名源为须修问题。

### 3.3 composition-placement（经营位置）——**待核实（正确的待核实管理；内容四要素双源扎实，图示得体）**

- 条目现状（`entries/batch-06.json` 40–72 行）：`definition`＝「经营位置是中国画六法之一，指画面中各部分的位置安排与主次关系。」；`time_or_place`＝「古代中国（参见来源）。」；`overview`＝「它关注物象在画面中的占位与呼应，与西方构图理论中的布局概念可相互参照。」；`实例`＝「名称：《清明上河图》（长卷经营位置、散点布局）；地点：北京故宫博物院藏；作者：张择端；年代：北宋……」
- **definition / overview 支撑**：`wp-six-principles-chinese-painting` 逐字 `"Division and Planning" (jingying 经营) or placing and arrangement (weizhi 位置), corresponding to composition, space and depth` → 定义「位置安排与主次关系」直证 ✓；overview「与西方构图理论布局概念可相互参照」由 `wp-composition-visual-arts`（构图 visual arts）背景源支撑，相容 ✓。非编造。
- **实例四要素（双源直证）**：
  - 名称：「张择端清明上河图卷」dpm-qingming 直证 ✓。
  - 地点：「故宫博物院」页 + 故宫藏品源语境 → 北京故宫博物院藏 ✓。
  - 作者：「张择端」dpm-qingming 直证 ✓。
  - 年代：「北宋」dpm-qingming 页面北宋语境支撑 ✓。
  - **「长卷经营位置、散点布局」**：dpm-qingming「作者用传统的手卷形式，采取"散点透视法"组织画面」「构图采用鸟瞰式全景法」逐字直证 + columbia「handscroll … unroll only an arm's length section at a time … the viewer determined the pace … show the same object from different angles」双证手卷移步换景机制 ✓。**「此作品体现该法」获两独立源直接支撑**——本条是三例中「复用来源真正支撑'该作品体现该法'」最扎实的。
- **关键缺口（判待核实主因·已披露）**：「经营位置」术语未在该作品页逐字出现，属概念对应解读；dpm-qingming 用「散点透视/手卷形式/鸟瞰全景」而非四字「经营位置」。条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「手卷移步换景与长卷布局由两源直证；'经营位置'为六法概念，属对应解读。」→ 已披露，诚实。
- **七节/SVG/规范提示（机械项）**：6 节齐；1 张 SVG `viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无外链；规范句收尾 ✓；几何无越界 ✓。**SVG 内容得体**：图为「主位（主体大块）/次位与呼应（右侧两分块）+ 主次呼应标注」，贴合「经营位置=主次与占位」，且与另外两条**不重复**（另两条为逐字节相同的通用布局图）。`related=["transmission-copy"]` 合理（同为六法之一，存在对应页）。
- **问题**：
  - ① **（判待核实主因·已披露）** 概念归属为解读，两实例源用「散点透视/手卷」而非「经营位置」四字；保持待核实正确。可接受（内容实质接近合格）。
  - ② （轻微）SVG 未标具体尺寸/比例关系，仅标「主位/次位与呼应」意图；`TASK_design` 要求「标注设计意图或尺寸关系」，已标设计意图，可满足；无越界。
- **内容判定：待核实（正确的待核实管理；内容四要素双源扎实，图示得体，实质接近合格）**。`needs_verification` 联动诚实，无治理缺陷。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：7 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）；`wp-*` 三条 `link_ok=true`，`dpm-qianli`/`dpm-luoshenfu`/`dpm-qingming`/`columbia-handscroll` 四条 `link_ok=null`（三态保守）。无假 id、无 `link_ok=false`。
- **可达性（本轮实抓）**：全部 `urllib` HTTP 200 取得正文（dpm-qianli 26310B、dpm-qingming 106475B、columbia 17539B、dpm-luoshenfu 17454B、wp-six-principles 68384B、chinaculture 10526B）。
- **相关性结论**：
  - `likeness-form`：概念源逐字直证定义；dpm-luoshenfu + chinaculture 双源直证《洛神赋图》四要素与「以形写神」；「应物象形」归属为解读（已披露）。
  - `color-according-type`：概念源逐字直证定义；dpm-qianli 单源直证《千里江山图》青绿设色；**`dpm-luoshenfu` 不相关挂名**（问题②）；「随类赋彩」归属为解读（已披露）。
  - `composition-placement`：概念源逐字直证定义；dpm-qingming + columbia 双源直证《清明上河图》长卷散点布局与手卷机制；「经营位置」归属为解读（已披露）。三例中相关性最扎实。
- **「复用来源是否真的支撑'该作品体现该法'」结论**：
  - composition-placement：**是**（dpm-qingming 散点透视/手卷 + columbia 手卷机制，两源直接支撑长卷经营）。
  - likeness-form：**是**（dpm-luoshenfu「以形写神」+ chinaculture 人物心境，直接支撑形神写照；唯术语未逐字）。
  - color-according-type：**是（靠 dpm-qianli 一源）**，但第二源 `dpm-luoshenfu` **不支撑**「该作品体现该法」，属无效互证。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 | SVG 几何越界 | SVG 语义贴合 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| likeness-form | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | **✗ 错配**（图为「主次与虚实布局」，与应物象形不符） |
| color-according-type | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | **✗ 错配**（应为色块分布，实为构图布局图） |
| composition-placement | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE | ✓ 得体（主位/次位/呼应） |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；三条「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械项三条形式层面全部通过。**
>
> **几何实核（针对第57轮 acoustic 越界缺陷的同类检查）**：按 `x/y/width/height` 与 `cx/cy/rx/ry`、`line` 端点复算三条 SVG 元素包围盒，全部落在 0–760 × 0–400 内，**无越界**。
>
> **SVG 语义/重复问题（本轮新增·Important）**：`likeness-form` 与 `color-according-type` 的 SVG **逐字节完全相同**，且其文字「主次与虚实布局」实际是**构图（经营位置）**的示意——对「应物象形」（取形写照）与「随类赋彩」（按类设色）**语义均不符**。`TASK_design` 要求「图中标注设计意图或尺寸关系」且图中应与本法相称；此为第44–58轮「通用图复用」系统性问题的延续，且本轮从「图重复」升级为「图与主题不符」。`check.py` 不检查该语义项，故 PASS 未暴露。建议为两条换用贴合主题的示意图（likeness-form：取形→写照顺序；color-according-type：按物类归并的色块分布）并补标注。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 `mismatch=NONE`）；`source_count` 与来源数组长度一致（4=4 ×3）；`coverage.needs_verification_count` 三条各=1，与条目 `needs_verification=true` 逐条对应。
- `pending_sum`=**191**（第58轮 193，本轮 -2，与 `transmission-copy` 被改一致；非本次对象）。存量待核实占比 191/258≈74.0%，处历史高位，**不触发「待核实占比异常低（疑似硬写）」降级**。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| likeness-form | true（保持） | 「两源直证作品形神写照；'应物象形'为六法概念，作品为形似写照范例，属概念对应解读。」 | 与 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：解读性质已披露，保持待核实正确。 |
| color-according-type | true（保持） | 「《千里江山图》青绿设色由故宫源直证；'随类赋彩'为六法概念，作品为设色范例，属概念对应。」 | 与 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：解读已披露；但 pending 未点明「实例实质单源/第4源不相关」（见问题②）。 |
| composition-placement | true（保持） | 「手卷移步换景与长卷布局由两源直证；'经营位置'为六法概念，属对应解读。」 | 与 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：双源直证+解读已披露，最扎实。 |

> **异常监控（§E）**：全库 `pending_sum` 191，较第58轮 193 少 2（与该轮 `transmission-copy` 改动对应，非本次抽检对象）；三条对象 `needs_verification` 均为 true，无硬写清零；存量占比 74.0% 高位，不触发「占比异常低」降级。

## 七、任务 5：相似度（difflib 去空白＋小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| likeness-form | **0.4545** vs color-according-type | <0.54 ✓ | **0.4975** vs qi-yun | <0.54 ✓ |
| color-according-type | **0.4545** vs likeness-form | <0.54 ✓ | **0.4528** vs likeness-form | <0.54 ✓ |
| composition-placement | **0.3582** vs xu-shi | <0.54 ✓ | **0.4000** vs color-according-type | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。最高为 likeness-form 全字段 0.4975（vs qi-yun，同为「六法+洛神赋图+概念解读」结构），仍低于阈值 0.0425 裕度。

### 7.2 第59轮批内 3 条两两（全字段② / 短文本①）

- likeness-form vs color-according-type：全字段 **0.4563**、短文本 0.4545。
- likeness-form vs composition-placement：全字段 **0.3878**、短文本 0.2985。
- color-according-type vs composition-placement：全字段 **0.4000**、短文本 0.3043。
- → 批内两两均低于 0.54，无套话/模板姊妹风险（likeness-form 与 color-according-type 因同为「六法+作品+概念解读」对称句式而偏高 0.45，属正常近邻；实例分别为《洛神赋图》与《千里江山图》，内容分化明显）。

### 7.3 方法自校

- `futurism vs expressionism` 全字段②＝**0.5157**，与第39–58轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition/time/overview/实例 来源支撑 | 来源存在·verified·相关·可达 | 七节/规范/SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **likeness-form（应物象形）** | 概念源逐字直证定义；《洛神赋图》四要素双源（故宫名画记+ChinaCulture）直证，「以形写神」逐字；「应物象形」归属为解读且已披露；无编造 | 4/4 存在且 true；本轮 200；实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界；**SVG 语义错配且与 color-according-type 逐字节重复（须修）** | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.4545/0.4975）；批内 ✓ | **待核实** |
| **color-according-type（随类赋彩）** | 概念源逐字直证定义；《千里江山图》四要素+青绿设色由 dpm-qianli 直证；但**实例实质单源**、第4源 `dpm-luoshenfu` 不相关挂名；「随类赋彩」归属为解读已披露；无编造 | 4/4 存在且 true；本轮 200；**1 源不相关** | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界；**SVG 语义错配且与 likeness-form 逐字节重复（须修）** | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.4545/0.4528）；批内 ✓ | **待核实** |
| **composition-placement（经营位置）** | 概念源逐字直证定义；《清明上河图》四要素+长卷散点布局由 dpm-qingming+columbia 双源直证；「经营位置」归属为解读已披露；无编造 | 4/4 存在且 true；本轮 200；**两实例源均直接相关** | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界、语义得体 | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.3582/0.4000）；批内 ✓ | **待核实（内容四要素双源扎实，实质接近合格）** |

### 问题清单

- **① likeness-form 概念归属为解读（判待核实主因·已如实披露，轻微）**：两实例源未逐字用「应物象形」（用「以形写神」），已标 nv=true 并披露；升级需补一源直接挂钩该术语与该作品。
- **② color-according-type 实例实质单源 + 不相关挂名源（Important）**：实例四要素仅 dpm-qianli 单源直证；第 4 源 `dpm-luoshenfu`（洛神赋图）与「赋彩/青绿」无关，属凑 source_count 的挂名源。建议补第二个直接相关来源（或如实减源并同步 coverage `source_count`）。pending 现仅披露「概念解读」，未提示「实例单源/第4源不相关」，建议 pending 同时点明以更诚实。
- **③ likeness-form / color-according-type SVG 语义错配 + 逐字节重复（Important·本轮引入）**：两条 SVG 完全相同，文字「主次与虚实布局」实为构图示意，对「应物象形」（取形写照）与「随类赋彩」（按类设色）**均不符**；`TASK_design` 要求图示与本法相称并标设计意图。须换用各自贴合主题的示意图并补标注。（composition-placement 的 SVG 得体，不在此列。）
- **④ 三例共性·概念归属为解读（判待核实主因·均已披露）**：「应物象形/随类赋彩/经营位置」三术语均非实例作品页逐字所出，属六法概念对应解读，`needs_verification=true` 与 pending/正文一致披露，方向正确。
- **⑤ 概念源背景定位（轻微）**：`wp-six-principles-chinese-painting`（本轮实抓确认对三法均有逐字英文释义，作为定义主证成立）、`wp-chinese-painting` / `wp-composition-visual-arts` 为背景源；`dpm-*`/`columbia` `link_ok=null` 已标保守。

## 九、总体结论与建议

- **抽样结果**：第59轮补具名实例六法组中抽检 3 条——`likeness-form`、`color-according-type`、`composition-placement`。**内容维度：0 合格（3 条均待核实，其中 composition-placement 内容四要素双源扎实、实质接近合格）＋3 待核实＋0 不合格；实例层面 0 编造、0 假 id、0 死链证据。** 三条 definition 均由 `wp-six-principles-chinese-painting` 逐字直证（本轮实抓确认），无编造。
- **来源层面**：7 个来源全部存在、`verified=true`、本轮全部取得正文。三条实例四要素主要由官方机构源直证；**composition-placement 双源真正支撑「该作品体现该法」，最扎实；likeness-form 双源支撑形神写照；color-according-type 仅单源支撑，第 4 源挂名不相关**（问题②）。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 几何无越界、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：三条结构一致、披露诚实；`pending_sum`=191（较第58轮 -2，对应 transmission-copy 改动），存量占比 74.0% 高位，不触发降级。**但 SVG 语义错配＋两条逐字节重复（问题③）为本轮须修的内容工程缺陷，`check.py` 不覆盖故 PASS 未暴露。**
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4545、全字段最高 0.4975）；方法自校 0.5157 与第39–58轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（3 待核实），0 实例编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——存量占比 74.0% 高位，本轮对象无清零。
  4. **结论：本轮 3 条待核实、0 不合格，不触发整批返工/降级。** 三条待核实均为「概念对应解读需披露」而非编造，`needs_verification` 联动方向正确、披露诚实。
- **返工/修复建议（定向、非整批）**：
  1. **（问题③，优先·内容工程）** 为 `likeness-form`（取形→写照顺序图）与 `color-according-type`（按物类归并的色块分布图）分别换用贴合主题、彼此不重复的内联 SVG，并补「设计意图/尺寸关系」标注；建议全站排查同类「构图通用图」复用。
  2. **（问题②，Important·来源）** 为 `color-according-type` 补第二个直接相关官方源（另一馆藏/权威页直证《千里江山图》青绿设色），替换不相关的 `dpm-luoshenfu`；若要保留现结构，可在 `pending_notes` 增述「实例实质单源，第二实例源待补」，使待核实披露更完整。
  3. **（问题①④，可选升级）** 三条内容（定义+实例）已获直证，若 lead 判断「概念对应解读」已充分披露、无需维持 nv，可评估将对应条目 `needs_verification` true→false 清零（须同步 `pending_notes`、正文「待核实」、`coverage.needs_verification_count` 与 `pending_sum`）；否则维持现状（当前披露诚实，无需回滚）。
  4. **（问题⑤，轻微）** 概念背景源在站点来源页注明「背景/定义」定位；`link_ok=null` 维持三态保守即可。

### 机器可读汇总

```
ROUND=59
SAMPLER=spotcheck-r59
MODE=第59轮补具名实例六法组抽3条（likeness-form / color-according-type / composition-placement）
SCOPE=["likeness-form","color-according-type","composition-placement"]
FILES={"likeness-form":"entries/batch-32.json:38-68","color-according-type":"entries/batch-32.json:70-99","composition-placement":"entries/batch-06.json:40-72"}
GIT_HEAD="612290f chore: round58 Chinese painting named instances"; ROUND59_COMMITTED=false; GIT_STATUS="round59 changes UNCOMMITTED as found (M coverage/batch-06/batch-32 + site entries color-according-type,composition-placement,likeness-form,transmission-copy)"
STATE={"coverage.json":"total=258, pending_sum=191 (was 193 in r58; -2 aligns with transmission-copy edit)","nvc_per_entry":1,"src_count_per_entry":4,"level":"L2"}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements; SVG geometry recheck: 0 out-of-viewBox across 3"
SAMPLE_RATIO="3/4 of the round59 六法 named-instance group (>=§E min 3)"
FETCH_METHOD="urllib+UA+unverified-SSL HTTP200 for dpm-qianli(26310B),dpm-qingming(106475B),columbia-handscroll(17539B),dpm-luoshenfu(17454B),wp-six-principles(68384B),chinaculture-luoshenfu(10526B); norm substring readback; all FOUND"
SOURCES={"ids":7,"all_exist":true,"all_verified_true":true,"all_year_null":true,"link_ok_true":["wp-six-principles-chinese-painting","wp-chinese-painting","wp-composition-visual-arts"],"link_ok_null":["dpm-qianli","dpm-luoshenfu","dpm-qingming","columbia-handscroll"],"fake_id":0,"irrelevant_source":["color-according-type->dpm-luoshenfu"]}
BODY_SUPPORT={
 "likeness-form":"definition backed verbatim by wp-six-principles ('Correspondence to the Object (yingwu应物) or depicting of form (xiangxing象形)'); instance Luoshen Fu Tu four facts dual (dpm-luoshenfu '顾恺之洛神赋图卷（宋摹）/东晋顾恺之作/约345-406/以形写神' + chinaculture 'Luoshen Appraisal Painting/Gu Kaizhi/classic'); '应物象形' term not literal on artwork page -> concept interpretation, disclosed; VERDICT=待核实",
 "color-according-type":"definition backed verbatim ('Suitability to Type (suilei随类) or application of color (fucai赋彩)'); instance Qianli Jiangshan Tu four facts single-source (dpm-qianli '王希孟千里江山图卷/北宋绢本设色/政和三年1113/青绿山水技法青绿颜色中变化'); 4th source dpm-luoshenfu IRRELEVANT (洛神赋图, no color relation); '随类赋彩' concept interpretation disclosed; VERDICT=待核实",
 "composition-placement":"definition backed verbatim ('Division and Planning (jingying经营) or placing and arrangement (weizhi位置), composition/space/depth'); instance Qingming Shanghe Tu four facts dual (dpm-qingming '张择端清明上河图卷/散点透视法/手卷/鸟瞰全景' + columbia 'handscroll/perspective same object from different angles/arm's length section'); '经营位置' concept interpretation disclosed; VERDICT=待核实 (content four-fact dual-source, close to 合格)"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3; 无on*/无外链图","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_out_of_viewbox":0,"svg_semantic_issue":"likeness-form == color-according-type SVG byte-identical; text '主次与虚实布局' is composition layout, MISMATCHES 应物象形 and 随类赋彩 semantics; composition-placement SVG valid"}
METADATA={"field_match_coverage":"ALL OK x3 (mismatch=NONE)","source_count":"4=4 x3","nvc":"nvc=1 x3; pending_sum=191 (r58 193, -2 vs transmission-copy); stock ratio 191/258=74.0% high -> no anomalous-low downgrade","needs_verification":"all true; pending==待核实节 verbatim x3"}
SIMILARITY={
 "likeness-form":{"vs_all_short":0.4545,"short_entry":"color-according-type","vs_all_full":0.4975,"full_entry":"qi-yun","verdict":"PASS<0.54"},
 "color-according-type":{"vs_all_short":0.4545,"short_entry":"likeness-form","vs_all_full":0.4528,"full_entry":"likeness-form","verdict":"PASS<0.54"},
 "composition-placement":{"vs_all_short":0.3582,"short_entry":"xu-shi","vs_all_full":0.4000,"full_entry":"color-according-type","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.4563,"intrabatch_full_max_pair":"likeness-form vs color-according-type",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-58 -> method validated","threshold":0.54}
VERDICT_CONTENT={"likeness-form":"待核实","color-according-type":"待核实","composition-placement":"待核实"}
HARD_FABRICATION_INSTANCE=0
UNSOURCED_CLAIM=0
FAKE_ID=0
LINK_FAIL=0
SVG_OUT_OF_VIEWBOX=0
SVG_SEMANTIC_MISMATCH=2
IRRELEVANT_SOURCE_COUNT=1
BATCH_ACTION="No rollback/downgrade: 0 不合格 (3 待核实), 0 instance fabrication/0 fake id/0 dead link; similarity all <0.54; pending stock high (74.0%). Targeted fixes: (1) HIGH: replace likeness-form & color-according-type SVG (currently byte-identical generic '主次与虚实布局' composition图, semantically mismatched) with theme-fitting diagrams + intent/dimension annotation; (2) HIGH: color-according-type replace irrelevant dpm-luoshenfu with a 2nd relevant official source (or drop + sync source_count), and note '实例实质单源' in pending; (3) optional: evaluate nv clear for 3 entries if lead deems concept-interpretation disclosure sufficient (else keep)."
READONLY="only wrote research/spotcheck-round59.md; temp files research/_snip_r59.txt & _sixprin.txt written then rm-removed (git status clean of them); no other project content file changed; no git commit; round59 work remains uncommitted as found; web content treated as data, no instruction executed"
```

*（报告完）*
