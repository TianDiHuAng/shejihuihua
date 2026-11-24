# 第105轮质量抽检（spotcheck-round105）——side-window-daylight / lighting-design 双平台支撑与数值核查

- 抽检人：spotcheck-r105（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象（均声明升级 nv=false、类型性实例，实读当前 JSON 为准）：
  1. `side-window-daylight`（侧窗采光）——entry 在 `entries/batch-36.json`；sources = `wp-daylighting-architecture`（Wiki）+ `wp-architectural-lighting-design`（Wiki）+ `db-window`（DB）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
  2. `lighting-design`（照明设计）——entry 在 `entries/batch-07.json`；sources = `wp-interior-design`（Wiki）+ `wp-architectural-lighting-design`（Wiki）+ `db-artificial-lighting`（DB）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。

> 说明：任务描述把条目1写为「wp-daylighting-architecture/wp-arch-lighting」，条目2写为「wp-interior-design/wp-arch-lighting」；实读当前 entry，两者第二 Wiki 源均为 `wp-architectural-lighting-design`（title「Architectural lighting design」，url …/Architectural_lighting），无「wp-arch-lighting」此 id。下文一律以实读 JSON 的 source id 为准。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round105.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词比对、相似度、去重、结构、SVG 越界、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-07.json / M entries/batch-36.json / M site/entries/lighting-design.html / M site/entries/side-window-daylight.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round105.py`——**均为 round105 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-window = https://www.designingbuildings.co.uk/wiki/Window` → `web_fetch` **HTTP 200**，H1=`Window`（Last edited 07 Aug 2024）。
  - `db-artificial-lighting = https://www.designingbuildings.co.uk/wiki/Artificial_lighting` → `web_fetch` **HTTP 200**，H1=`Artificial lighting`（Last edited 01 Jul 2021）。
  - `wp-daylighting-architecture = https://en.wikipedia.org/wiki/Daylighting_(architecture)` → en.wikipedia 直连 **fetch failed**（本环境同 D05 限制）；经镜像 `https://owiki.org/wiki/Daylighting_(architecture)` **HTTP 200**，H1=`Daylighting (architecture)`，逐句核对一致。
  - `wp-architectural-lighting-design = https://en.wikipedia.org/wiki/Architectural_lighting` → en 直连 **fetch failed**；经镜像 `https://owiki.org/wiki/Architectural_lighting` → 重定向至 `/wiki/Architectural_lighting_design` **HTTP 200**，H1=`Architectural lighting design`。
  - `wp-interior-design = https://en.wikipedia.org/wiki/Interior_design` → en 直连 **fetch failed**；经镜像 `https://owiki.org/wiki/Interior_design` **HTTP 200**，H1=`Interior design`。
  - （canonical url 在 sources.json 记的是 en.wikipedia；本轮因直连失败改用 owiki.org 镜像抓取正文，H1 与条目一致，属抓取环境限制，非数据缺陷。sources.json 的 `verified/link_ok=true` 为先前记录。）
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.22s`（PYTEST_EXIT=0）**（PYTHONPATH=项目根、PYTHONDONTWRITEBYTECODE=1，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径② = 0.5157（与 r104b 逐位一致，方法正确）。全库 258 条，无重复 id。**

## 一、`side-window-daylight`（侧窗采光）

### 1.1 当前 entry 实读
- `definition`＝「侧窗采光从外墙侧面开洞进光，窗边亮、越往里越暗，光线带明显方向。」
- `原理`＝「光从外墙竖向窗洞侧面进入，靠窗处亮、随进深逐渐衰减、光线方向明显；布窗宜与房间进深和窗地比配合。」
- `overview`＝「它是最常见的开窗方式，靠窗布置工作位更有利，进深大处则需辅助照明。」
- `实例`＝「名称：教室侧窗采光（类型性，不指定具体项目）；光线由侧面窗洞射入、向室内深处逐渐衰减。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「进深过大处采光不足；需按规范核算。实际工程须按当地规范和专业设计人员的要求」
- sources = wp-daylighting-architecture / wp-architectural-lighting-design / db-window；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①外墙侧面开窗进光；②靠窗亮、越往里越暗（随进深衰减）；③光线方向明显。

**wp-daylighting-architecture（Wikipedia；owiki HTTP200，H1=Daylighting (architecture)）——强支撑：**
- `Windows are the most common way to admit daylight into a space. Their vertical orientation means that they selectively admit sunlight and diffuse daylight at different times of the day and year.`（**窗为最常见引入天然光方式；竖向窗=侧窗 ✓①**）
- `Equatorial-side windows receive at least some direct sunlight on any sunny day of the year, so they are effective at daylighting areas of the house adjacent to the windows.`（**窗附近/相邻区域被有效照亮＝靠窗亮 ✓②前半**）
- `light incidence is highly directional and casts long shadows`（**光线方向性强 ✓③**）
- 侧窗深部衰减的间接直证：`reflecting the collected daylight deeper inside ... light shelves`、`The light shelf ... reflects sunlight upward to illuminate the ceiling ... reduce deep shadows, reducing the need for general illumination`、`admit diffuse daylight that evenly illuminates a space`（**需靠 light shelf/反射面把光「引向更深处」「减少深阴影」——反证不采取措施时越往里越暗 ✓②**）

**wp-architectural-lighting-design（Wikipedia；H1=Architectural lighting design）——弱/泛：**
- `The architectural makeup of a space impacts the day lighting. It can be used in a space through windows, openings of the interior, skylights, and reflective surfaces.`（**仅泛述「经窗/开口/天窗/反射面引入天然光」，未及侧窗方向性/进深衰减**）

**db-window（Designing Buildings；web_fetch HTTP200，H1=Window）——仅泛述窗户：**
- `Windows are openings fitted with glass to admit light and allow people to see out. They are often openable to allow ventilation.`（**窗=开洞引入光＝「开洞引入天然光」✓（极泛）**）
- 其余篇幅为：Elements of a window（light/frame/lintel/jamb/sill/mullion/transom…）、Materials、Opening type（fixed light / sash / casement / tilt&turn / pivot / bi-fold / louvre…）、Number of panes，及「Other types」罗列 `Sidelight - Positioned beside a door or main window`、`Bay window - ... project in front of the external wall line`、`Clerestory - ... allow natural light in`。
- **关键：全文为「窗户」通类条目（类型/材料/构件），未出现「侧窗采光」作为采光策略的论述，未提「窗边亮/越往里越暗/光线方向明显」等②③特征。**

| 概念要素 | wp-daylighting | wp-arch-lighting | db-window（DB） | 判定 |
| --- | --- | --- | --- | --- |
| ①外墙侧面开窗进光 | ✓✓ vertical windows / equatorial-side windows | ✓（泛：through windows） | △ 仅「窗=开洞引入光」，无「侧面策略」 | WP 强，DB 泛 |
| ②靠窗亮、越往里越暗 | ✓✓ effective at areas adjacent to windows；light shelf 反证深部衰减 | ✗ | ✗ | 仅 WP |
| ③光线方向明显 | ✓✓ highly directional … casts long shadows | ✗ | ✗ | 仅 WP |

**判定（1.2）：** 核心概念②③（侧窗方向性、进深衰减）**仅由 Wikipedia 平台（wp-daylighting-architecture）强支撑**；另一 Wikipedia 源泛化；**DB 非维基源 db-window 只支撑「开洞引入天然光」这一最泛要素，不支撑「外墙侧面/靠窗亮/越往里暗/方向明显」**。即 `db-window` 属**过泛的「窗户」通类条目**，并非「侧窗采光」的直接论述页。

### 1.3 ★特别判断：db-window 是否足以支撑「侧窗采光」（而非仅泛述窗户）
**结论：不足。** 实抓 db-window 全文（H1=Window）为窗户构件的通类词条：定义句仅 `openings fitted with glass to admit light`；正文围绕构件（frame/mullion/jamb…）、材料、开启方式（sash/casement/…）、玻璃层数展开；「Other types」里 `Sidelight`指「门/主窗旁侧窄窗」、`Clerestory`「高处成带采光窗」、`Bay window`「凸出外墙面」——**都不是「侧窗采光」策略（侧面开窗→靠窗亮→越深越暗→方向明显）**。故 db-window 只等值于「窗=墙上/屋顶开洞引入天然光（含 bay 等）」（即 sources.json 自身 note 所写），**不能作为「侧窗采光」的第二直接源**。→ 触发任务判据「若某条 DB 页过泛/不足以作第二直接源，请判待核实」。**本条判待核实。**

（旁证：库内另有 `db-daylight-factor`（The daylight factor，采光测量）、`db-skylight`、`db-light-well` 等 DB 页，但均非「侧窗采光」方向性论述；未借以补强本条，仅说明现有 DB 池缺「侧窗/侧光采光」直接页。）

### 1.4 是否编造
- definition/原理 之②③等具体特征**有实源**（wp-daylighting-architecture 逐句可溯源），**非编造** ✓。overview/实例均属常识性类型描述、无虚构事实。唯 sourcing 深度不足（DB 只到「开洞引入光」），属**第二源偏弱**而非造假。

### 1.5 类型性实例合理性
- 「教室侧窗采光（类型性，不指定具体项目）」——合理：教室侧墙开窗、侧向进光、随进深衰减，为标准类型级例证；未虚构具体项目/地点/年代。✓

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ 形式 |
| entry.pending_notes | "" | ✓ 形式 |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ 形式 |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | ✓ 形式 |
| time_or_place | 「跨时期、全球（参见来源）。」无「待核实」 | ✓ 形式 |
- **形式四处一致 ✓，check.py PASS；但内容前提（DB 第二直接源不足）未满足，nv=false 严格意义上不成立。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 6 节全非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素解析（line/rect/circle/text 坐标）均落框内，OUT_OF_BOUNDS=NONE | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(` | ✓ |
| SVG 注记 | 含「示意图，非施工图」 | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（同 r101–r104 T 小疵；check.py 只匹配子串不拦） | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/side-window-daylight.html` 的 title/definition/overview/规范句与 JSON 逐句一致（实读） | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| side-window-daylight | 短① | skylight | 0.3567 | ✓ <0.54 |
| side-window-daylight | 全② | skylight | 0.3970 | ✓ <0.54 |
| def×原理（去重） | — | — | 0.4000 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54，无对手越阈 ✓**；方法自校 0.5157 ✓。

### 1.9 条目1 结论
**`side-window-daylight`（侧窗采光）——待核实。**
- 依据：definition/原理核心（②靠窗亮越往里暗、③方向明显）**仅 Wikipedia 平台（wp-daylighting-architecture）强支撑**；`db-window` 为「窗户」通类词条，**只能支撑「开洞引入天然光」这一极泛要素，不足以作为「侧窗采光」的第二直接源**——符合任务「DB 页过泛/不足以作第二直接源→待核实」判据。
- 非编造（WP 逐句可溯源）；类型性实例合理；nv=false 形式四处一致但**内容前提不满足**；七节/SVG/规范句/site 均过（规范句句末缺「。」为 T 小疵）；相似度与 def 去重均 <0.54；check.py PASS、pytest 5 passed。
- 供 lead 决策的最小修正建议：将 `db-window` 换/补为「直接论述侧窗/侧向采光（方向性、进深衰减）」的非维基来源——如 Designing Buildings 的采光/侧光专页（`db-daylighting`/`db-side-lighting` 之类，需实抓核实存在且含侧光论述），或其他权威采光设计指南（占位 `DB_DAYLIGHT_PAGE` / `AUTHORITATIVE_DAYLIGHT_SRC`）；若暂无可核的第二直接源，应在 `待核实`/`pending_notes` 明示「侧窗方向性/进深衰减特征目前仅 Wikipedia 单平台直证」，并将 nv 置 true。

## 二、`lighting-design`（照明设计）

### 2.1 当前 entry 实读
- `definition`＝「组织天然光与人工光以支持视觉、健康和空间氛围的设计。」
- `原理`＝「白天优先引入天然光、夜间或采光不足处由人工照明补足，按视觉任务与空间氛围分层布光，兼顾能效与舒适。」
- `overview`＝「照明设计把采光、任务照明和情绪氛围作为整体考虑。」
- `实例`＝「名称：博物馆分层照明（类型性，不指定具体项目）；以天然光与人工光分层配合，突出展品并保护展品。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「只堆亮度会眩光与过热；色温混用会破坏氛围，参数须按规范校核。实际工程须按当地规范和专业设计人员的要求」
- sources = wp-interior-design / wp-architectural-lighting-design / db-artificial-lighting；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`

### 2.2 definition/原理 两平台核对（实抓引句）
概念拆解：①组织天然光+人工光；②支持视觉；③支持健康；④支持空间氛围；（原理另含：夜间/不足处人工补足、分层布光、能效、舒适）。

**db-artificial-lighting（Designing Buildings；web_fetch HTTP200，H1=Artificial lighting）——强支撑「人工光设计」与「天然+人工」：**
- `Lighting (or illumination) describes the way an area is made known to the human eye through either natural or artificial light.`（**照明=天然光或人工光 ✓①（天然+人工同框）**）
- `Buildings are often designed to optimise the capture of natural daylight.`（**天然采光设计 ✓①**）
- `Artificial light is generally easily manipulated to achieve the required lighting outcome. The light can be increased or decreased, directed, focused and coloured. This allows lighting to create a range of effects according to the requirements of a space.`（**人工光可操控以营造适配空间的多种效果 ✓④空间氛围**）
- 三分法：`Ambient lighting`（`comfortable level of brightness ... see reasonably well and navigate safely`→②视觉+舒适）、`Task lighting`（`reading, studying and way-finding ... where ambient light levels are insufficient`→②视觉）、`Accent lighting`（`imparts drama and character ... draw the viewer's attention`→④氛围）。
- `The type of artificial light source chosen will depend on ... the quality and type of light required for the space, and the energy consumption of the light fitting.`（**能效 ✓**）

**wp-architectural-lighting-design（Wikipedia；H1=Architectural lighting design）——强支撑（含「健康」）：**
- `It can include manipulation and design of both daylight and electric light or both, to serve human needs.`（**天然光+电光并设计 ✓①**）
- `The objective ... is to balance the art and the science of lighting to create mood, visual interest and enhance the experience of a space or place`（**氛围/体验 ✓④**）
- `The visual aspects ... aesthetics and the narrative of the space and the non-visual aspects are those concerned with human health and well-being.`（**健康与福祉 ✓③直证**）
- `The basic aim of lighting within the built environment is to enable occupants to see clearly and without discomfort.`（**视觉 ✓②**）
- Day lighting 节：`There are psychological and physical health benefits that come from using daylight in a space ... ease seasonal affective disorder ... vitamin D ... regulating circadian rhythms`（**健康 ✓③直证**）
- Electric lighting 节：`allow the user of the space to see at various times in the day, but especially at night or in winter season, when daylight is no longer a possible or sufficient source of light`（**夜间/不足处人工补足 ✓原理**）
- `Lighting layers include: task layer, focal layer, ambient layer, decorative layer, and daylight layer.`（**分层布光 ✓原理**）

**wp-interior-design（Wikipedia；H1=Interior design）——支撑：**
- `By adding natural and artificial lighting a designer can enhance the features in space and make it more pleasing. Lighting can enhance the aesthetic appeal of a place, setting the mood for the room.`（**天然+人工 ✓①；氛围 ✓④**）
- `... office you want ... overhead lighting, task/desk lighting and natural lighting. Making sure there is enough lighting in a workspace is important so the person using the place does not strain their eyesight.`（**视觉 ✓②；分层 ✓原理**）

| 概念要素 | db-artificial-lighting（DB） | wp-arch-lighting | wp-interior-design | 判定 |
| --- | --- | --- | --- | --- |
| ①组织天然光+人工光 | ✓✓ either natural or artificial light；optimise natural daylight；人工光详述 | ✓✓ daylight and electric light | ✓ natural and artificial lighting | **双平台强证（DB+WP）✓✓** |
| ②支持视觉 | ✓✓ see reasonably well；task lighting | ✓✓ see clearly without discomfort | ✓ not strain eyesight | **双平台（DB+WP）✓✓** |
| ③支持健康 | △ comfortable/navigate safely（+站内 related「Health and wellbeing…」） | ✓✓ human health and well-being；daylight health benefits | ✗ | WP 强、DB 间接 |
| ④支持空间氛围 | ✓✓ effects per space；accent drama/character | ✓✓ mood, visual interest, experience | ✓ setting the mood | **双平台（DB+WP）✓✓** |
| 原理：夜间/不足处人工补足 | ✓ night/winter when daylight insufficient | ✓✓ 同上 | — | 双平台 ✓ |
| 原理：分层布光 | ✓ ambient/task/accent | ✓✓ lighting layers | ✓ overhead/task/natural | 双平台 ✓ |
| 原理：能效 | ✓ energy consumption | ✓ energy consumed | — | 双平台 ✓ |
| 原理：舒适 | ✓ comfortable brightness | ✓ without discomfort | — | 双平台 ✓ |

**判定（2.2）：** 定义/原理的骨干——「组织天然光+人工光、支持视觉、空间氛围」以及原理四项（人工补足/分层/能效/舒适）——**由 DB 非维基源（db-artificial-lighting）与 Wikipedia 平台（wp-architectural-lighting-design / wp-interior-design）双平台逐要素直证，强成立、非编造 ✓✓**。唯「健康」一项**以 Wikipedia（wp-architectural-lighting-design）为主证，db-artificial-lighting 正文仅以「comfortable/navigate safely」相邻表达+站内「Health and wellbeing impacts of natural and artificial lighting」相关主题间接呼应**（见 2.3 透明说明）。

### 2.3 ★特别判断：db-artificial-lighting 是否足以支撑「人工光设计」且与 wp 天然光共同覆盖「天然+人工」
**结论：足以，覆盖成立。**
- 「人工光设计」：db-artificial-lighting 正文明确「artificial light ... easily manipulated ... increased/decreased/directed/focused/coloured ... create a range of effects according to requirements of a space」，并给出 ambient/task/accent 三类与光源/能效——**是对「人工光设计」的直接、充分论述 ✓✓**。
- 「天然+人工」共同覆盖：db-artificial-lighting 开篇即 `through either natural or artificial light`，且 `optimise the capture of natural daylight`；与之配合的 Wikipedia 侧（wp-architectural-lighting-design `both daylight and electric light`、wp-interior-design `natural and artificial lighting`）**完整覆盖「天然+人工」两侧 ✓✓**。db 与 wp 分工互补、无重叠凑数。
- 透明说明（T）：definition 中「健康」主要靠 Wikipedia 强证；db-artificial-lighting 正文仅 comfort/safety 相邻 + 站内相关主题链接，**未在正文直书 health**。若 lead 要求「逐要素均为 DB+WP 双直证」，可考虑为「健康」补一处 DB 明述（如 DB「Health and wellbeing impacts of natural and artificial lighting」页正文），否则建议在来源注记注明「健康一项主要依据 Architectural lighting design（Wikipedia）」。**此项不阻断合格判定**，因（a）原理全四项均双平台直证；（b）定义骨干「组织天然+人工、视觉、氛围」双平台直证；（c）「健康」非编造（WP 明述）。

### 2.4 是否编造
- definition/原理 各要素均有实源逐句可溯源，**非编造 ✓**。db-artificial-lighting 的 note「人工照明：以灯具提供照度，与天然光配合」与正文（`artificial light ... emanates from electric lamps`；`through either natural or artificial light`）**一致、无误引 ✓**。无无源主张残留。

### 2.5 类型性实例合理性
- 「博物馆分层照明（类型性，不指定具体项目）；以天然光与人工光分层配合，突出展品并保护展品」——合理：博物馆=天然光+人工光分层（基础/重点照明）、突出展品并控光保护展品，契合「分层布光/天然+人工」原理；未虚构具体项目/年代。✓

### 2.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ 形式 |
| entry.pending_notes | "" | ✓ 形式 |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ 形式 |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | ✓ 形式 |
| time_or_place | 「跨时期、全球（参见来源）。」无「待核实」 | ✓ 形式 |
- **形式四处一致 ✓；内容前提（双平台支撑）已满足（除「健康」主要为 WP 主证的 T 说明外），nv=false 成立。**

### 2.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 6 节全非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素解析（rect 120–640/110–320、circle 200,150 r16、polygon 160–240/166–300、rect 420,240+160×40、text 300,90 / 300,370）均落框内，OUT_OF_BOUNDS=NONE | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(` | ✓ |
| SVG 注记 | 含「示意图，非施工图」 | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（同 r101–r104 T 小疵） | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/lighting-design.html` 的 title/definition/overview/规范句与 JSON 逐句一致（实读） | ✓ |

### 2.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| lighting-design | 短① | daylighting | 0.4603 | ✓ <0.54 |
| lighting-design | 全② | skylight | 0.3835 | ✓ <0.54 |
| def×原理（去重） | — | — | 0.3200 | ✓ 已去重、两层次可分 |
- 全库最大：短 0.4960、全 0.5256（同上）——**均 <0.54 ✓**；方法自校 0.5157 ✓。def×原理 0.3200 印证「原理已与 def 去重」。

### 2.9 条目2 结论
**`lighting-design`（照明设计）——合格。**
- 依据：definition/原理骨干（组织天然光+人工光、视觉、空间氛围 + 原理四项）由 **DB 非维基源 db-artificial-lighting 与 Wikipedia（wp-architectural-lighting-design/wp-interior-design）双平台逐要素直证**；`db-artificial-lighting` **足以支撑「人工光设计」并与 WP 天然光共同覆盖「天然+人工」**（特别判断为「是」）；非编造；类型性实例合理；nv=false 形式齐备且内容前提成立；七节/SVG/规范句/site 均过（规范句句末缺「。」为 T 小疵）；相似度 all<0.54、def×原理 0.3200 已去重；check.py PASS、pytest 5 passed。
- T 透明说明：「健康」一项以 wp-architectural-lighting-design 强证为主，db-artificial-lighting 正文仅 comfort/safety 相邻表达+站内相关主题；不影响合格，但建议来源注记注明或补一处 DB 明述「健康/福祉」以完全对齐逐要素双直证口径。

## 三、机器可读汇总

```
ROUND=105
SAMPLER=spotcheck-r105
SCOPE=["side-window-daylight","lighting-design"]
READONLY="only wrote research/spotcheck-round105.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-window":"web_fetch HTTP200 H1='Window' (Last edited 07 Aug 2024)",
 "db-artificial-lighting":"web_fetch HTTP200 H1='Artificial lighting' (Last edited 01 Jul 2021)",
 "wp-daylighting-architecture":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='Daylighting (architecture)'",
 "wp-architectural-lighting-design":"en.wikipedia fetch FAILED; owiki.org /Architectural_lighting -> /Architectural_lighting_design HTTP200 H1='Architectural lighting design'",
 "wp-interior-design":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='Interior design'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}

SIDE_WINDOW_DAYLIGHT={
 "verdict":"待核实",
 "definition":"侧窗采光从外墙侧面开洞进光，窗边亮、越往里越暗，光线带明显方向。",
 "principle":"光从外墙竖向窗洞侧面进入，靠窗处亮、随进深逐渐衰减、光线方向明显；布窗宜与房间进深和窗地比配合。",
 "sources":["wp-daylighting-architecture","wp-architectural-lighting-design","db-window"],
 "concept_dual_source":{
   "external_side_window":"wp-daylighting 'Windows ... vertical orientation ... admit sunlight and diffuse daylight' / 'equatorial-side windows ... effective at daylighting areas ... adjacent to the windows' -> WP strong; db-window generic 'openings ... admit light' only",
   "bright_by_window_darker_with_depth":"wp-daylighting 'effective at areas adjacent to the windows' + light shelf 'reflect ... deeper inside'/'reduce deep shadows' (implicit) -> WP only",
   "directional_light":"wp-daylighting 'light incidence is highly directional and casts long shadows' -> WP only",
   "db_nonwiki_supports_full_concept":false,
   "holds_two_platform_for_specific_concept":false},
 "db_window_insufficient_reason":"db-window is a generic 'Window' article (elements/materials/opening types); only supports 'window opening admits natural light', NOT side-placement/depth/directionality -> over-generic, cannot be 2nd direct source",
 "fabrication":"core supported by wp-daylighting (not fabricated); db second-source depth insufficient (weak sourcing, not fabrication)",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); check.py PASS",
 "nv_false_grounded":false,
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"skylight 0.3567","nearest_full":"skylight 0.3970","def_vs_principle":0.4000,"lt_0.54":true},
 "transparency":["DB 第二直接源不足（db-window 过泛）——待核实触发项","规范句句末缺「。」（T 小疵）"],
 "fix_suggestion":"replace/supplement db-window with a non-wiki page directly covering side-window/side-daylighting (DB_DAYLIGHT_PAGE / AUTHORITATIVE_DAYLIGHT_SRC); else record 待核实 note and set nv=true"
}

LIGHTING_DESIGN={
 "verdict":"合格",
 "definition":"组织天然光与人工光以支持视觉、健康和空间氛围的设计。",
 "principle":"白天优先引入天然光、夜间或采光不足处由人工照明补足，按视觉任务与空间氛围分层布光，兼顾能效与舒适。",
 "sources":["wp-interior-design","wp-architectural-lighting-design","db-artificial-lighting"],
 "concept_dual_source":{
   "natural_plus_artificial":"db 'through either natural or artificial light'/'optimise natural daylight' + wp 'both daylight and electric light'/'natural and artificial lighting' -> DOUBLE(DB+WP) OK",
   "visual":"db 'see reasonably well'/task lighting + wp 'see clearly without discomfort'/'not strain eyesight' -> DOUBLE(DB+WP) OK",
   "ambiance":"db 'create effects according to requirements of a space'/accent 'drama and character' + wp 'mood, visual interest'/'setting the mood' -> DOUBLE(DB+WP) OK",
   "health":"wp-arch-lighting 'human health and well-being' + daylight 'health benefits (SAD, vitamin D, circadian)' strong; db-artificial-lighting body only comfort/safety + related-topic link -> WP-primary, DB-adjacent",
   "principle_4_dual":"artificial-fill-at-night/insufficient + layering + energy + comfort all DB+WP",
   "holds_two_platform_for_concept":true},
 "db_artificial_lighting_sufficient_for_artificial_design":true,
 "db_plus_wp_covers_natural_and_artificial":true,
 "fabrication":"no; all elements sourced; db note accurate",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent; check.py PASS",
 "nv_false_grounded":true,
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"daylighting 0.4603","nearest_full":"skylight 0.3835","def_vs_principle":0.3200,"lt_0.54":true},
 "transparency":["健康 element WP-primary (db only comfort/safety + related link) — non-blocking T note","规范句句末缺「。」（T 小疵）"]
}

GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}
VERDICT={"side-window-daylight":"待核实(DB 第二直接源不足: db-window 过泛, 仅支撑开洞引入天然光, 不支撑侧窗方向性/进深衰减)","lighting-design":"合格(db-artificial-lighting 足够支撑人工光设计并与 wp 天然光共同覆盖天然+人工; 健康项 WP 主证)"}
KEY_FINDING="条1 side-window-daylight: wp-daylighting-architecture 逐句直证侧窗(vertical windows)、靠窗亮(adjacent to windows)、方向(highly directional)、进深衰减(light shelf deeper inside/reduce deep shadows)，但 db-window 为窗户通类词条(构件/材料/开启方式)，仅支撑『窗=开洞引入天然光』，不支撑侧窗方向性/进深衰减——DB 非维基第二直接源不足，判待核实(非编造、实例合理、nv形式四处一致、七节/SVG/规范句在(句末缺句号)/site一致、相似度短0.3567全0.3970<0.54、def×原理0.40)。条2 lighting-design: db-artificial-lighting 直证人工光设计('through either natural or artificial light'/'manipulated ... effects according to requirements of a space'/ambient-task-accent/energy) 并与 wp-architectural-lighting-design('both daylight and electric light'/'mood, visual interest'/'human health and well-being') 及 wp-interior-design('natural and artificial lighting'/'setting the mood') 双平台逐要素覆盖天然+人工/视觉/氛围+原理四项；健康以 WP 强证为主(db 仅 comfort/safety+站内related)——足够、非编造、实例合理、nv形式齐备且成立、七节/SVG/规范句(句末缺句号)/site过、相似度短0.4603全0.3835<0.54、def×原理0.32已去重；判合格。check.py PASS + pytest 5 passed；方法自校 0.5157；全库最大 短0.496/全0.5256<0.54。"
```

## 四、只读核验
- 除本报告 `research/spotcheck-round105.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：db-window、db-artificial-lighting 经 `web_fetch` 直抓 HTTP200（H1 分别为 Window / Artificial lighting）；wp-daylighting-architecture、wp-architectural-lighting-design、wp-interior-design 因 en.wikipedia 直连 fetch failed，经 owiki.org 镜像 HTTP200 抓回，H1 逐一核对一致（属本环境抓取限制，非数据缺陷）。
- 词比对、关键词扫描、相似度、去重、结构、SVG 越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内评论/推荐等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（pytest 用 Anaconda 解释器 + PYTHONPATH=项目根）。
- `git status` 中的改动文件与 `?? tools/apply_review_round105.py` 均为**他方（round105 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
