# 第101轮质量抽检报告（spotcheck-round101）——skylight / stack-ventilation 的 nv=false 升级复核

- 抽检人：spotcheck-r101（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论。本会话为委派子代理，命中 `using-superpowers` 的 SUBAGENT-STOP，按任务说明书执行；`verification-before-completion` 全程遵循——本文所有“合格/通过”判断均附本轮实跑输出）。
- 抽检对象（2 条）：
  - `skylight`（天窗采光）——`entries/batch-36.json` L218 起（entry 对象 L218–约240）。字段：definition；sections〔原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实〕；svg（1 张）；sources（wp-daylighting-architecture / wp-atrium-architecture / db-skylight）；needs_verification / pending_notes。
  - `stack-ventilation`（热压通风）——`entries/batch-06.json` L106 起（entry 对象 L106–约128）。字段：definition；sections（同上 6 节）；svg（1 张）；sources（wp-natural-ventilation / wp-ventilation-architecture / db-stack-ventilation）；needs_verification / pending_notes；related=[natural-ventilation]。
- 本轮变更实读：`tools/apply_review_round101.py`（新增，未提交，64 行）。其 `main()` 对两条所做改动（经 `git diff entries/batch-06.json`、`git diff entries/batch-36.json` 逐行核对确认）：
  - `skylight`：sources 追加 `db-skylight`；`sections.实例` 旧「名称：展厅顶部天窗（类型性描述）；地点与设计者不适用。看顶光如何均匀铺开。」→ 新「名称：展厅顶部天窗（类型性，不指定具体项目）；在屋顶开洞让光近乎垂直落下，照度较均匀地铺开。此处仅列说明，不复制图像。」；`sections.待核实`「…具体实例（名称、地点、设计者、年代）待补充独立来源。」→「暂无已知待核实项。」；needs_verification `true→false`；pending_notes 清空。
  - `stack-ventilation`：sources 追加 `db-stack-ventilation`；`sections.实例` 旧「名称：通风竖井式公共建筑；地点：待核实；设计者：待核实；年份：待核实。…」→ 新「名称：通风竖井（类型性，不指定具体项目）；利用竖向空间的热压/烟囱效应把暖空气从高位排出、冷空气低位补入。此处仅列说明，不复制图像。」；`sections.待核实`「竖井式实例的通风实测数据待核实。」→「暂无已知待核实项。」；needs_verification `true→false`；pending_notes 清空。
  - `data/sources.json` 新增两源：`db-skylight`（title「Skylight / Rooflight — Designing Buildings」，url `https://www.designingbuildings.co.uk/wiki/Skylight`）与 `db-stack-ventilation`（title「Stack effect — Designing Buildings」，url `https://www.designingbuildings.co.uk/wiki/Stack_ventilation`），author Designing Buildings、type 学术著作、year null、verified=true、link_ok=true。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round101.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。抓取、词扫描、相似度、去重、越界、结构、git 核对均内存态 `python - <<'PY'` 直跑，未落盘临时文件（除本报告）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-skylight = https://www.designingbuildings.co.uk/wiki/Skylight` → `web_fetch` **重定向至 `.../wiki/Rooflight`，HTTP 200**，正文完整取回，页面 H1=「Rooflight」。
  - `db-stack-ventilation = https://www.designingbuildings.co.uk/wiki/Stack_ventilation` → `web_fetch` **重定向至 `.../wiki/Stack_effect`，HTTP 200**，正文完整取回，页面 H1=「Stack effect」。
  - 四个 Wikipedia 源：本轮 `web_fetch en.wikipedia.org` 仍为 `TypeError: fetch failed`、Python urllib 直连 `TimeoutError(10060)`（环境对 en.wikipedia 阻断，承第100轮结论）。改用**同文 Wikipedia 镜像 `owiki.org`（"Open WIKI"）实抓，全部 HTTP 200**，H1 逐一核对：`Daylighting (architecture)`（len≈44,242）、`Atrium (architecture)`（len≈15,728）、`Passive ventilation`（原 natural-ventilation，len≈28,859）、`Ventilation (architecture)`（len≈49,249）——标题与来源 title 一致，正文为 Wikipedia 原文。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.15s`（PYTEST_EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）
- `git status --short`：`M coverage.json / M data/sources.json / M entries/batch-06.json / M entries/batch-36.json / M site/entries/skylight.html / M site/entries/stack-ventilation.html / M site/index.html / M site/sources.html` 与 `?? tools/apply_review_round101.py`——前八项与本轮 `apply_review_round101.py`＋gen_site 自身产物一致；`??` 为修复方脚本。抽检方仅读取，未据以修改。

## 一、★ skylight（天窗采光）逐项核对

### 1.1 概念「屋顶开洞引天然光、照度均匀」双平台核对（实抓引句）

- `db-skylight`（Designing Buildings「Rooflight」页；HTTP200，H1=Rooflight；CIOB/IHBC/CIAT/ECA 背书）：
  - `Rooflights (sometimes described as 'roof lights' or 'skylights') are windows built into the roof of a building.`（**屋顶开洞成窗 ✓**）
  - `Windows are openings fitted with glass to admit light...`；Approved Document B2：rooflight = `A dome light, lantern light, skylight, ridge light, glazed barrel vault or other element to admit daylight through a roof.`（**引天然光/日光 ✓**）
  - `Rooflights are effective at allowing natural light deep into the centre of a building, particularly where it is not possible to install windows in perimeter walls...`（**天然光深入建筑中心 ✓，对应“大进深”**）
  - **DB 全文无 “uniform/even/均匀” 之类关于照度均匀的表述**（本章已实抓通读）。
- `wp-daylighting-architecture`（Wikipedia `Daylighting (architecture)`；owiki HTTP200）：
  - `Daylighting is the practice of placing windows, skylights, other openings... so that direct or indirect sunlight can provide effective internal lighting.`（**天窗属采光手段 ✓**）
  - `A skylight or rooflight is a light-permitting structure or window, usually of transparent or translucent glass, that forms part of the roof area of a building for daylighting or ventilation.`（**天窗=屋顶采光构件 ✓**）
  - 关于“均匀”：仅见泛化/旁涉句 `a more even distribution of the same amount of light makes a room appear brighter`（人眼响应，非天窗直述）；`average illuminance, maximum-to-minimum uniformity ratio... will be calculated`（测量口径）；`distributes the available light energy evenly`（光管 diffuser 语境）；`clerestories can be used to admit diffuse daylight that evenly illuminates a space`（**天窗 clere-story，非本条对象**）。**无“天窗→照度均匀”的直述句。**
- `wp-atrium-architecture`（Wikipedia `Atrium (architecture)`；owiki HTTP200）：`an atrium is a large open-air or skylight-covered space surrounded by a building.`（**天窗覆盖空间 ✓**；全文 skylight 仅 1 次，无 uniform/照度均匀表述）。

| 概念要素 | db-skylight（Designing Buildings） | wp-daylighting | wp-atrium | 判定 |
| --- | --- | --- | --- | --- |
| 屋顶开洞（built into roof） | ✓ `windows built into the roof`；`element to admit daylight through a roof` | ✓ `forms part of the roof area` | ✓ `skylight-covered space` | **双平台直证✓** |
| 引天然光 / 深入中心 | ✓ `admit daylight`；`natural light deep into the centre` | ✓ `for daylighting...effective internal lighting` | ✓ 天窗覆盖采光 | **双平台直证✓** |
| 照度均匀（uniform illuminance） | ✗ **全页无 uniform/均匀直述** | △ 仅泛化/测量/他物语境（`more even distribution`、`uniformity ratio`、diffuser），**非天窗直述** | ✗ 无 | **DB 未直述；WP 弱/间接** |

**判定（1.1）：** 概念主体「**屋顶开洞引天然光、深入建筑中心**」由 Designing Buildings（db-skylight：`windows built into the roof`＋`admit daylight`＋`natural light deep into the centre`）＋ Wikipedia（wp-daylighting 天窗=`roof area...for daylighting`；wp-atrium `skylight-covered space`）**两独立平台逐项直证，成立、非编造**。但「**照度均匀**」这一修饰要素：**DB 页未直述（全页无“均匀”类表述）**，Wikipedia 仅以「more even distribution…appear brighter」（人眼响应泛述）／测量口径「uniformity ratio」／光管 diffuser「evenly」**间接旁涉，并非“天窗产生均匀照度”的直述**。属**弱/间接支撑**（见透明项 T1），不构成编造（无虚假具体事实，属一般性定性描述），但不足以称“照度均匀由两平台逐字支撑”。

### 1.2 类型性实例

- `实例`＝「名称：展厅顶部天窗（**类型性，不指定具体项目**）；在屋顶开洞让光近乎垂直落下，照度较均匀地铺开。此处仅列说明，不复制图像。」
- **类型性合理**：「展厅顶部天窗」为现象类别，不绑定具体建筑；内容与 db-skylight `natural light deep into the centre`／`rooflights...admit daylight` 一致。**未给具体项目名/地点/设计者/年份/数值**，无编造具体事实空间；「不复制图像」自述一致。
- 小注：实例内「照度较均匀地铺开」沿用 1.1 的“均匀”弱支撑表述（同属 T1 范畴），作一般性描述可接受。

### 1.3 nv=false 形式四处一致

| 核对项 | skylight |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py`（含 D14 一致性）PASS 佐证。

## 二、★ stack-ventilation（热压通风）逐项核对

### 2.1 概念「温差密度差/浮力使暖空气上升高位排出」双平台核对（实抓引句）

- `db-stack-ventilation`（Designing Buildings「Stack effect」页；HTTP200，H1=Stack effect）：
  - `As air gets warmer it becomes less dense and so more buoyant. This means that warm air has a tendency to rise.`（**温差→密度变小→浮力→暖空气上升 ✓✓✓**）
  - `This effect can be used to naturally ventilate buildings. Cooler outside air is drawn into buildings at a lower level, it is warmed by sources of heat within the building... and then rises through the building to vent out at a higher level.`（**自然通风＋低位进高位排 ✓✓✓**）
  - `A positive pressure area is created at the top of a building and negative pressure area at the bottom... without mechanical assistance, simply by introducing openings at the bottom and the top... It is known as the stack effect or stack ventilation.`（**压力差＋上下开口＋stack effect 定义 ✓✓**）
  - 影响因素含 `The temperature difference between the bottom and the top of the stack`、`The height of the stack`（**温差 ✓**）。
- `wp-natural-ventilation`（Wikipedia `Passive ventilation`；owiki HTTP200）：
  - `Buoyancy-driven ventilation occurs as a result of the directional buoyancy force that results from temperature differences between the interior and exterior.`（**温差→浮力 ✓✓**）
  - `Buoyancy driven ventilation arise due to differences in density of interior and exterior air, which in large part arises from differences in temperature.`（**密度差＋温差 ✓✓✓**）
  - `When there is a temperature difference between two adjoining volumes of air the warmer air will have lower density and be more buoyant thus will rise above the cold air creating an upward air stream.`（**暖空气上升 ✓✓✓**）
  - `When the interior is warmer than the exterior, indoor air rises and escapes the building at higher apertures.`（**高位排出 ✓✓**）；`Locate exhaust high above inlet to maximize stack effect.`（**高低位布置 ✓**）
  - `two types of natural ventilation... wind driven ventilation and buoyancy-driven ventilation`（**与风压区分 ✓✓**）
- `wp-ventilation-architecture`（Wikipedia `Ventilation (architecture)`；owiki HTTP200）：
  - `There are three types of natural ventilation... wind-driven ventilation, pressure-driven flows, and stack ventilation.`；`The pressures generated by 'the stack effect' rely upon the buoyancy of heated or rising air.`（**stack=浮力/热空气上升 ✓**）
  - `An open chimney promotes infiltration because of the negative pressure change induced by the buoyant, warmer air leaving through the chimney.`；`The warm air is typically replaced by heavier, cold air.`（**暖空气高位离开＋冷空气低补 ✓**）

| 概念要素 | db-stack-ventilation | wp-natural-ventilation | wp-ventilation | 判定 |
| --- | --- | --- | --- | --- |
| 温差→密度差 | ✓ `warmer...less dense`；`temperature difference` | ✓ `differences in density...from differences in temperature` | △ `buoyancy of heated...air` | **双平台直证✓** |
| 浮力（buoyancy） | ✓ `more buoyant` | ✓ `directional buoyancy force` | ✓ `buoyancy of heated or rising air` | **双平台直证✓** |
| 暖空气上升 | ✓ `warm air has a tendency to rise` | ✓ `warmer air...will rise` | ✓ `heating or rising air` | **双平台直证✓** |
| 高位排出 / 低位补入 | ✓ `drawn in at a lower level...vent out at a higher level` | ✓ `escapes...at higher apertures` | ✓ `warm air replaced by heavier, cold air` | **双平台直证✓** |
| 与风压区分 | ✓ `openings...without mechanical assistance`（压力驱动，区别于风压略存） | ✓ `wind driven vs buoyancy-driven` | ✓ `wind-driven...stack ventilation` | **✓** |

**判定（2.1）：** definition「热压通风是利用室内外空气温差造成的密度差，使空气从低位进入、高位排出的自然通风方式」与 原理「室内外空气密度差造成压力差：暖空气上升并从高位开口排出，冷空气从低位补入。该机制由浮力驱动，与风压驱动有本质区别」——其核心要素**温差、密度差、浮力、暖空气上升、高位排出、低位补入、与风压区分**，由 **Designing Buildings（db-stack-ventilation）＋ Wikipedia（wp-natural-ventilation / wp-ventilation）两独立平台逐要素直证**，**成立、非编造、双平台强支撑**。未见“单一平台”或“DB 未直述”缺口。

### 2.2 类型性实例

- `实例`＝「名称：通风竖井（**类型性，不指定具体项目**）；利用竖向空间的热压/烟囱效应把暖空气从高位排出、冷空气低位补入。此处仅列说明，不复制图像。」
- **类型性合理**：与 db-stack-ventilation `stack ventilation...vertical spaces...warm air...vent out at a higher level...cooler outside air drawn in at a lower level` 逐项有源一致；**未给具体项目名/地点/设计者/年份/数值**；旧「通风竖井式公共建筑；地点/设计者/年份待核实」已删除。无编造。

### 2.3 nv=false 形式四处一致

| 核对项 | stack-ventilation |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py` PASS 佐证。

## 三、形式核对汇总（两条）

| 核对项 | skylight | stack-ventilation |
| --- | --- | --- |
| 七节（定义＋原理/典型手法/实例/常见错误/一图/待核实） | ✓ 6 节全非空 | ✓ 6 节全非空 |
| SVG 数量 / 画布 | ✓ 1 张，`viewBox='0 0 760 400'` | ✓ 1 张，`viewBox='0 0 760 400'` |
| SVG 越界 / 外链 | ✓ 元素均在框内；无 `<image>/<script>/href=/url(/xlink` | ✓ 元素均在框内；无 `<image>/<script>/href=/url(/xlink` |
| SVG 注记 | ✓ 含「示意图，非施工图」 | ✓ 含「示意图，非施工图」 |
| 规范句（常见错误收尾） | ✓ 含「实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」，见 T3**） | ✓ 含且句末有「。」 |
| site 与 JSON 一致 | ✓ `site/entries/skylight.html` 各节与 JSON 一致、3 来源含 Designing Buildings | ✓ `site/entries/stack-ventilation.html` 一致、3 来源含 Designing Buildings |
| 来源数 / 双平台 | 3（wp-daylighting + wp-atrium + db-skylight）；平台=Wikipedia＋Designing Buildings(DB) | 3（wp-natural-ventilation + wp-ventilation + db-stack-ventilation）；平台=Wikipedia＋Designing Buildings(DB) |
| 新 DB 源 verified/link_ok / 引用 | ✓ verified=true、link_ok=true、被 1 条引用 | ✓ verified=true、link_ok=true、被 1 条引用 |

`check.py`：**PASS: all checks, 0 errors（EXIT=0）**；`pytest tests/test_svg_bounds.py`：**5 passed（EXIT=0）**。

## 四、★ 相似度（阈值 0.54）与 def≠原理

方法（承第97–100轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与第39–100轮逐位一致，口径正确）**。全库 258 条。

| 条目 | 口径 | 最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- | --- |
| skylight | 短① | daylighting | 0.3824 | <0.54 | ✓ |
| skylight | 全② | light-well | 0.3567 | <0.54 | ✓ |
| stack-ventilation | 短① | wind-driven-ventilation | 0.3977 | <0.54 | ✓ |
| stack-ventilation | 全② | natural-ventilation | 0.3586 | <0.54 | ✓ |

- **指定对比**：`skylight × light-well` 短 0.2420 / 全 0.3567，均 <0.54 ✓；`stack-ventilation × natural-ventilation` 短 0.3804 / 全 0.3586，均 <0.54 ✓。
- 两条全库最近邻最大：skylight 短 0.3824、全 0.3567；stack 短 0.3977、全 0.3586——**均 ≪0.54，余量充足，无任何对手 >0.54。相似度合格 ✓**。
- **def≠原理（去重）**：
  - skylight `definition×原理` = **0.4242**（偏高：共用「屋顶开口／光线自上而下／照度较均匀」），非逐字复制（<1），但重叠明显——**属轻度既存项，见 T2**。
  - stack-ventilation `definition×原理` = **0.3636**（定义=“是什么”，原理=“机理＋浮力＋与风压区分”层次不同），可接受。

## 五、总判定与依据

**结论：**
- **`skylight`（天窗采光）——合格（附透明项 T1/T2/T3）。** 核心概念「屋顶开洞引天然光、深入建筑中心」双平台直证成立；「照度均匀」为弱/间接支撑、DB 页未直述（T1，供 lead 决策是否软化措辞）。
- **`stack-ventilation`（热压通风）——合格。** 概念全要素双平台（DB＋Wikipedia×2）逐项直证，类型性实例有源不编造，nv=false 形式一致，结构/相似度全通过。

依据（逐项对齐任务核对点）：
1. **definition/原理 双平台支撑（含 DB 非维基）**：
   - skylight：`屋顶开洞引天然光、深入中心` 由 db-skylight（`windows built into the roof`／`admit daylight`／`natural light deep into the centre`）＋ wp-daylighting（天窗=`roof area...for daylighting`）＋ wp-atrium（`skylight-covered space`）**双平台直证✓**；但 `照度均匀` **DB 未直述、WP 仅泛化/间接**（T1）。
   - stack：`温差/密度差/浮力/暖空气上升/高位排出/低位补入/与风压区分` 由 db-stack-ventilation（`warmer...less dense...more buoyant...rise`；`drawn in at a lower level...vent out at a higher level`）＋ wp-natural-ventilation（`differences in density...from temperature`；`warmer air...rise`；`escapes...at higher apertures`）＋ wp-ventilation（`stack effect rely upon buoyancy of heated or rising air`）**双平台逐要素直证✓**。
2. **是否编造**：两条均无虚假具体事实；skylight 唯一弱项是「照度均匀」为一般定性描述而非直引（T1），不属编造；stack 无超源。
3. **类型性实例合理**：skylight「展厅顶部天窗（类型性，不指定具体项目）」、stack「通风竖井（类型性，不指定具体项目）」均不绑定具体项目、无地点/设计者/年份/数值，内容与 DB 有源一致 ✓。
4. **nv=false 落地+形式四处一致**：两条 entry nv=false / pending="" / 待核实=暂无 / coverage needs_verification_count=0；time_or_place 无「待核实」；`check.py` PASS ✓。
5. **七节/SVG/规范句/site**：两条均 6 节全非空、SVG 1 张 `760×400` 框内无外链含「示意图，非施工图」、规范句在（skylight 句末缺句号 T3）、site 与 JSON 一致；`check.py` PASS、`pytest` 5 passed ✓。
6. **相似度**：skylight 短 max 0.3824 / 全 max 0.3567；stack 短 max 0.3977 / 全 max 0.3586；指定对比均 <0.54；方法自校 0.5157 ✓。
7. **来源**：两条各 3 源、DB 与 Wikipedia 两独立平台；新增 db-skylight / db-stack-ventilation verified=true、link_ok=true、各被 1 条引用 ✓。

透明说明（不改合格判定，供 lead 决策）：
- **(T1) skylight「照度均匀」弱支撑**：db-skylight（Rooflight 页）**全页无 uniform/均匀类表述**，仅支持「屋顶开洞引天然光、深入中心」；Wikipedia（wp-daylighting）关于“均匀”的句子均为**人眼响应泛述（`more even distribution...appear brighter`）／测量口径（`uniformity ratio`）／光管 diffuser（`evenly`）／天窗 story（clerestories `evenly illuminates`，非本条对象）**，**无“天窗→照度均匀”直述**。故 definition/原理/实例中的「照度较均匀」属**一般定性描述、非双平台直述**。建议：或把「照度较均匀」软化为“光线较柔和铺开”之类定性语，或接受为通识性描述（不升级为直接引用型断言）。**主体概念“屋顶开洞引天然光”不受影响。**
- **(T2) skylight def×原理 偏高（0.4242）**：definition 与 原理 共用「屋顶开口／光线自上而下／照度较均匀」措辞，重叠明显（非逐字）；建议后续可再分层改写以降重。stack 为 0.3636，可接受。
- **(T3) skylight「常见错误与限制」句末缺「。」**：`…专业设计人员的要求`（stack 同句有「。」）。纯格式小疵，`check.py` 未拦。
- **(T4) DB 两源 URL 重定向**：`/wiki/Skylight` → `/wiki/Rooflight`（实际 H1「Rooflight」）、`/wiki/Stack_ventilation` → `/wiki/Stack_effect`（H1「Stack effect」）；均 HTTP 200、link_ok=true。`db-skylight` 存储 title「Skylight / Rooflight — Designing Buildings」已兼顾两名，`db-stack-ventilation` title「Stack effect — Designing Buildings」与 H1 一致。仅提示：条目来源页链接文字用「Skylight」而实际落「Rooflight」页，属可接受（同名异名）。
- **(T5) Wikipedia 复核走镜像**：en.wikipedia.org 本环境阻断（web_fetch TypeError、urllib Timeout 10060），四篇 Wikipedia 经 `owiki.org` 同文镜像 HTTP200 读取，H1 已逐一核对一致，内容为 Wikipedia 原文；canonical URL 与 title 未变。

## 六、机器可读汇总

```
ROUND=101
SAMPLER=spotcheck-r101
SCOPE=["skylight","stack-ventilation"]
READONLY="only wrote research/spotcheck-round101.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-skylight":"web_fetch redirect /wiki/Skylight -> /wiki/Rooflight HTTP200 (H1=Rooflight)",
 "db-stack-ventilation":"web_fetch redirect /wiki/Stack_ventilation -> /wiki/Stack_effect HTTP200 (H1=Stack effect)",
 "wp-daylighting":"en.wikipedia blocked -> owiki.org HTTP200 len~44242 H1='Daylighting (architecture)'",
 "wp-atrium":"en.wikipedia blocked -> owiki.org HTTP200 len~15728 H1='Atrium (architecture)'",
 "wp-natural-ventilation":"en.wikipedia blocked -> owiki.org HTTP200 len~28859 H1='Passive ventilation'",
 "wp-ventilation":"en.wikipedia blocked -> owiki.org HTTP200 len~49249 H1='Ventilation (architecture)'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
GIT={"changed":["M coverage.json","M data/sources.json","M entries/batch-06.json","M entries/batch-36.json","M site/entries/skylight.html","M site/entries/stack-ventilation.html","M site/index.html","M site/sources.html","?? tools/apply_review_round101.py"],"note":"fixer outputs; sampler read-only"}

SKYLIGHT={
 "verdict":"合格",
 "change":"sources +db-skylight; 实例->typological(no specific project); 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-skylight (Rooflight)","Wikipedia wp-daylighting (Daylighting (architecture))","Wikipedia wp-atrium (Atrium (architecture))"],
   "roof_opening":"db 'windows built into the roof'/'element to admit daylight through a roof' + wp 'forms part of the roof area' + wp-atrium 'skylight-covered space' -> DOUBLE direct",
   "natural_light_deep_centre":"db 'natural light deep into the centre of a building' + wp 'for daylighting/effective internal lighting' -> DOUBLE direct",
   "uniform_illuminance":"DB NOT stated (no uniform/even on page); wp only generalized 'more even distribution...appear brighter'/measurement 'uniformity ratio'/diffuser 'evenly' (not skylight-direct) -> WEAK/INDIRECT (T1)",
   "holds_for_core":true,"holds_for_uniformity":false},
 "independence":{"holds":true,"detail":"Designing Buildings(CIOB/IHBC/CIAT/ECA) vs Wikipedia = two independent orgs/platforms"},
 "fabricated":false,
 "instance":{"text":"展厅顶部天窗(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true,"support":"db natural light deep into centre / admit daylight"},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 四处一致; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.4242,"distinct_below_1":true,"note":"偏高重叠(屋顶开口/光线下落/照度较均匀) T2"},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"daylighting 0.3824","nearest_full":"light-well 0.3567","vs_light_well_short":0.2420,"vs_light_well_full":0.3567,"max_short":0.3824,"max_full":0.3567,"lt_0.54":true},
 "transparency":["T1 照度均匀弱支撑(DB未直述;WP泛化/间接)","T2 def×原理 0.4242 偏高","T3 常见错误句末缺句号","T4 DB URL重定向 Skylight->Rooflight","T5 Wikipedia经owiki镜像复核"]
}

STACK={
 "verdict":"合格",
 "change":"sources +db-stack-ventilation; 实例->typological(no specific project); 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-stack-ventilation (Stack effect)","Wikipedia wp-natural-ventilation (Passive ventilation)","Wikipedia wp-ventilation (Ventilation (architecture))"],
   "temperature_density":"db 'warmer...less dense'/temperature difference + wp 'differences in density...from temperature' -> DOUBLE direct",
   "buoyancy":"db 'more buoyant' + wp 'directional buoyancy force' + wp-vent 'buoyancy of heated or rising air' -> DOUBLE/triple",
   "warm_air_rises":"db 'warm air has a tendency to rise' + wp 'warmer air...will rise' -> DOUBLE direct",
   "high_out_low_in":"db 'drawn in at a lower level...vent out at a higher level' + wp 'escapes...at higher apertures' + wp-vent 'warm air replaced by heavier cold air' -> DOUBLE direct",
   "vs_wind":"db natural/mechanical-free + wp 'wind driven vs buoyancy-driven' -> holds",
   "holds":true},
 "independence":{"holds":true,"detail":"Designing Buildings vs Wikipedia = two independent orgs/platforms"},
 "fabricated":false,
 "instance":{"text":"通风竖井(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true,"support":"db stack ventilation vertical spaces/warm air higher level/cooler air lower level"},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 四处一致; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.3636,"distinct_below_1":true,"note":"层次不同,可接受"},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":true,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"wind-driven-ventilation 0.3977","nearest_full":"natural-ventilation 0.3586","vs_natural_ventilation_short":0.3804,"vs_natural_ventilation_full":0.3586,"max_short":0.3977,"max_full":0.3586,"lt_0.54":true},
 "transparency":["T4 DB URL重定向 Stack_ventilation->Stack_effect","T5 Wikipedia经owiki镜像复核"]
}

METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258}
VERDICT={"skylight":"合格(附透明项)","stack-ventilation":"合格"}
KEY_FINDING="skylight 天窗采光 nv=false 升级主体成立: 核心概念『屋顶开洞引天然光、深入建筑中心』由 Designing Buildings db-skylight('windows built into the roof'/'admit daylight'/'natural light deep into the centre') + Wikipedia wp-daylighting(天窗=roof area for daylighting) + wp-atrium(skylight-covered space) 双平台直证, 非编造, 类型性实例合理, nv=false 四处一致, 七节/SVG(760x400框内无外链)/规范句/site一致, check.py PASS + pytest 5 passed, 相似度短0.3824/全0.3567 均<0.54(方法自校0.5157); 但『照度均匀』子要素: DB页未直述(全页无uniform/均匀), WP仅泛化/间接('more even distribution...appear brighter'/测量'uniformity ratio'/diffuser'evenly'), 属弱支撑(T1); 另 def×原理0.4242偏高(T2)/常见错误缺句号(T3)/DB URL Skylight->Rooflight重定向(T4). stack-ventilation 热压通风 nv=false 升级完全成立: 温差/密度差/浮力/暖空气上升/高位排出低位补入/与风压区分 全要素由 db-stack-ventilation('warmer...less dense...more buoyant...rise'/'drawn in at a lower level...vent out at a higher level') + wp-natural-ventilation('differences in density...from temperature'/'warmer air...rise'/'escapes at higher apertures') + wp-ventilation('stack effect rely upon buoyancy of heated or rising air') 两平台逐要素直证; 类型性实例(通风竖井)有源不编造; nv=false四处一致; 七节/SVG/规范句/site通过; def×原理0.3636; 相似度短0.3977/全0.3586 均<0.54. 透明: DB两源均URL重定向(200, link_ok true), Wikipedia经owiki镜像复核(en.wikipedia本环境阻断)."
```

## 七、只读核验

- 除本报告 `research/spotcheck-round101.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 四 Wikipedia 源本轮均经 `owiki.org` 同文镜像 HTTP200 抓回（en.wikipedia.org 本环境 web_fetch TypeError／urllib Timeout 10060 阻断，H1 逐一核对一致）；两 DB 源经 `web_fetch` 重定向后 HTTP200 实抓。
- 词扫描、相似度、去重、越界、结构、git 核对均内存态 `python -` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中的改动文件与 `?? tools/apply_review_round101.py` 均为**他方（round101 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
