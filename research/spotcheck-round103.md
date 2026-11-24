# 第103轮质量抽检报告（spotcheck-round103）——wind-driven-ventilation / transparent-material / safety-guarding 的 nv=false 升级复核

- 抽检人：spotcheck-r103（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言，证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有「合格/通过」判断均附本轮实跑/实抓输出。
- 抽检对象（3 条，类型性实例、升级 nv=false）：
  - `wind-driven-ventilation`（风压通风）——entry 对象在 `entries/batch-36.json`；sources〔wp-natural-ventilation / wp-ventilation-architecture / db-ventilation〕；coverage row L→`wind-driven-ventilation`（title 风压通风，source_count 3，nv_count 0，level L2，last_updated 2026-11-24）。
  - `transparent-material`（透明与半透明材料）——entry 对象在 `entries/batch-08.json`；sources〔wp-building-material / wp-architectural-lighting-design / db-glass〕；coverage row（title 透明与半透明材料，source_count 3，nv_count 0，level L2）。
  - `safety-guarding`（安全防护）——entry 对象在 `entries/batch-02-c.json`；sources〔wp-universal-design / wp-exit-sign / db-guardrail〕；coverage row（title 安全防护，source_count 3，nv_count 0，level L2）。
- 本轮变更实读：`tools/apply_review_round103.py`（新增，未提交，76 行）。其 `main()` 对三条所做改动（逐字段比对 JSON 确认）：
  - 新增 3 个 DB 源：`db-ventilation`（Ventilation — Designing Buildings，url …/wiki/Ventilation）、`db-glass`（Glass for buildings — Designing Buildings，url …/wiki/Glass）、`db-guardrail`（Guardrail — Designing Buildings，url …/wiki/Guardrail）；author Designing Buildings、type 学术著作、year null、verified=true、link_ok=true。
  - `wind-driven-ventilation`：sources 追加 `db-ventilation`；`sections.实例`→「名称：对流通风的房间（类型性，不指定具体项目）；迎风面进风、背风面出风形成穿堂风。此处仅列说明，不复制图像。」；needs_verification true→false；`待核实`→「暂无已知待核实项。」；pending 清空。
  - `transparent-material`：sources 追加 `db-glass`；`sections.原理` 改写为「光线与视线穿过玻璃等透明材料时可传达通透与联系；半透明材料只传光而模糊影像，从而以不同程度削弱空间边界的视觉重量。」；`sections.实例`→「名称：建筑玻璃隔断（类型性，不指定具体项目）；透明玻璃分隔空间而保持视线连通。此处仅列说明，不复制图像。」；nv true→false；待核实清空。
  - `safety-guarding`：sources 追加 `db-guardrail`；`sections.原理` 改写为「以护栏等实体屏障在临空、下沉与高差处阻止跌落，配合照明与出口标识使人能预见边缘与疏散方向，减少跌坠与死角风险。」；`sections.实例`→「名称：临空处防护栏杆（类型性，不指定具体项目）；在边缘设置护栏阻挡跌落。此处仅列说明，不复制图像。」；`常见错误与限制` 改为「栏杆高度、照度等具体数值须按当地规范与专业设计校核，本条不写死数值。」；nv true→false；待核实清空。
  - 备注：`apply_review_round103.py` 写出的 safety-guarding `常见错误与限制` 不含规范句尾句；而**实读当前条目**该节为「…本条不写死数值；实际工程须按当地规范和专业设计人员的要求。」（已带规范句与句号）——说明其后另有补写（或 gen 流程），下文一律以**实读当前 JSON**为准。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round103.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。抓取、词扫描、相似度、去重、结构、site 一致性、git 核对均内存态 `python - <<'PY'` / 工具直跑，未落盘临时文件（除本报告）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-ventilation = https://www.designingbuildings.co.uk/wiki/Ventilation` → `web_fetch` **HTTP 200**，H1=`Ventilation`（无重定向）。
  - `db-glass = https://www.designingbuildings.co.uk/wiki/Glass` → `web_fetch` **HTTP 200**，**重定向到 `/wiki/Glass_for_buildings`**，H1=`Glass for buildings`。
  - `db-guardrail = https://www.designingbuildings.co.uk/wiki/Guardrail` → `web_fetch` **HTTP 200**，H1=`Guardrail`（无重定向）。
  - 六个 Wikipedia 源（本环境 en.wikipedia 直连承前阻断，改用同文镜像 `owiki.org` 实抓，全部 **HTTP 200**，H1 逐一核对）：`wp-natural-ventilation`→`/wiki/Passive_ventilation` H1=`Passive ventilation`；`wp-ventilation-architecture`→`/wiki/Ventilation_(architecture)` H1=`Ventilation (architecture)`；`wp-building-material`→`/wiki/Building_material` H1=`Building material`；`wp-architectural-lighting-design`→`/wiki/Architectural_lighting_design` H1=`Architectural lighting design`；`wp-universal-design`→`/wiki/Universal_design` H1=`Universal design`；`wp-exit-sign`→`/wiki/Exit_sign` H1=`Exit sign`。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.11s`（PYTEST_EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）
- `git status --short`：`M coverage.json / M data/sources.json / M entries/batch-02-c.json / M entries/batch-08.json / M entries/batch-36.json / M site/entries/safety-guarding.html / M site/entries/transparent-material.html / M site/entries/wind-driven-ventilation.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round103.py`——前十项与本轮 `apply_review_round103.py`＋gen_site 自身产物一致；`??` 为修复方脚本。抽检方仅读取，未据以修改。

## 一、★ wind-driven-ventilation（风压通风）逐项核对

### 1.1 概念「依靠室外风在迎风面与背风面形成压差驱动的自然通风」双平台核对（实抓引句）

- `db-ventilation`（Designing Buildings「Ventilation」页；HTTP200，H1=Ventilation）：
  - `Natural ventilation is driven by 'natural' pressure differences from one part of the building to another. Natural ventilation can be wind driven, or buoyancy driven.`（**自然通风由压差驱动；自然通风可风压驱动或热压驱动 ✓✓✓，与本条概念直证；含 wind driven 字样**）
- `wp-natural-ventilation`（Wikipedia `Passive ventilation`；owiki HTTP200）：
  - `There are two types of natural ventilation occurring in buildings: wind driven ventilation and buoyancy-driven ventilation. Wind driven ventilation arises from the different pressures created by wind around a building or structure, and openings being formed on the perimeter which then permit flow through the building.`（**风压通风由风在建筑周围产生的不同压力＋周边开口促成穿流 ✓✓✓，直证「迎/背风面压差驱动」**）
  - `Wind driven ventilation depends on wind behavior, on the interactions with the building envelope and on openings or other air exchange devices such as inlets or windcatchers.`（**风压通风取决于风、围护结构与开口 ✓**）
- `wp-ventilation-architecture`（Wikipedia `Ventilation (architecture)`；owiki HTTP200）：
  - `Natural ventilation ... relies entirely on passive physical phenomena, such as wind pressure, or the stack effect.`（**自然通风依赖风压或热压 ✓✓**）
  - `Wind-driven ventilation relies upon the force of the prevailing wind to pull and push air through the enclosed space as well as through breaches in the building's envelope.`（**风压通风靠主导风的推/拉驱动气流 ✓✓，「pull and push」暗含正/负压两侧**）
  - `three types of natural ventilation occurring in buildings: wind-driven ventilation, pressure-driven flows, and stack ventilation.`（**风压通风为独立类型 ✓**）

| 概念要素 | db-ventilation（Designing Buildings） | wp-natural-ventilation | wp-ventilation-architecture | 判定 |
| --- | --- | --- | --- | --- |
| 风压驱动（wind driven） | ✓ `can be wind driven, or buoyancy driven` | ✓ `wind driven ventilation arises from the different pressures created by wind` | ✓ `such as wind pressure` / `Wind-driven ventilation relies upon the force of the prevailing wind` | **三平台直证✓✓✓** |
| 由建筑周围压差驱动 | ✓ `driven by 'natural' pressure differences` | ✓ `different pressures created by wind around a building` | ✓ `wind pressure` | **三平台✓** |
| 开口/进排风口促成穿流 | △ 未展开 | ✓ `openings being formed on the perimeter which then permit flow through the building` | ✓ `pull and push air through the enclosed space` | **双平台✓（WP强＋WP）** |
| 迎风正压/背风负压（原理） | — | △ `different pressures ... permit flow`（蕴含） | △ `pull and push`（蕴含） | **解释性引申（见 T5），非逐字** |

**判定（1.1）：** definition「风压通风指依靠室外风在建筑迎风面与背风面形成压差驱动的自然通风」与 原理「风吹到建筑，迎风面正压、背风面负压，空气由进风口流向排风口」之核心「风压驱动、由建筑周围（迎/背风面）压差驱动的自然通风、开口促成穿流」由 **Designing Buildings（db-ventilation：`can be wind driven` / `driven by natural pressure differences`）＋ Wikipedia（wp-natural-ventilation：`wind driven ventilation arises from the different pressures created by wind around a building`；wp-ventilation：`wind pressure` / `pull and push air`）两独立平台逐要素直证**，**成立、非编造、双平台强支撑**。「迎风面正压、背风面负压」为标准流体力学通识表述，由「different pressures…permit flow」「pull and push」蕴含，属合理概括（见 T5），非编造。

### 1.2 类型性实例

- `实例`＝「名称：对流通风的房间（**类型性，不指定具体项目**）；迎风面进风、背风面出风形成穿堂风。此处仅列说明，不复制图像。」
- **类型性合理**：「对流通风的房间」为现象类别，不绑定具体项目；内容与 wp-natural-ventilation `openings ... permit flow through the building` / wp-ventilation `pull and push air` 及「穿堂风（cross ventilation）」一致。**未给具体项目名/地点/设计者/年份/数值**，无编造。

### 1.3 nv=false 形式四处一致

| 核对项 | wind-driven-ventilation |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py`（含 D14 一致性）PASS 佐证。

## 二、★ transparent-material（透明与半透明材料）逐项核对

### 2.1 概念「透明传光透视 / 半透明传光但模糊影像 / 改变空间边界视觉重量」双平台核对（实抓引句）

- `db-glass`（Designing Buildings「Glass for buildings」页；HTTP200，经 /wiki/Glass 重定向，H1=Glass for buildings）：
  - `Visual transparency and reflectance can be altered with the addition of admixtures to the initial batch mix. Glass can be transparent, translucent, tinted, reflective, stained, opaque, and so on.`（**明列 transparent / translucent；视觉透明性可调 ✓✓，直证「透明/半透明」「视觉透明性」**）
- `wp-building-material`（Wikipedia `Building material`；owiki HTTP200）「Glass」节：
  - `Glass panes provided humans with the ability to both let light into rooms while at the same time keeping inclement weather outside.`（**玻璃让光进入房间＝传递光 ✓✓**）
  - `Glass 'curtain walls' can be used to cover the entire facade of a building, or it can be used to span over a wide roof structure in a 'space frame'.`（**幕墙＋大跨屋顶采光＝overview「采光顶面/幕墙」✓**）
- `wp-architectural-lighting-design`（Wikipedia `Architectural lighting design`；owiki HTTP200）：
  - `The more transparent the lighting fixture is, the higher efficacy.`（**透明→透光效率高，透明度与传光关联 ✓**）
  - `daylight ... can be used in a space through windows, openings of the interior, skylights, and reflective surfaces.`（**采光透光途径 ✓**）

| 概念要素 | db-glass（Designing Buildings） | wp-building-material | wp-architectural-lighting-design | 判定 |
| --- | --- | --- | --- | --- |
| 透明材料（可透视/传光） | ✓ `Glass can be transparent` / `Visual transparency` | ✓ `let light into rooms` | ✓ `transparent ... higher efficacy` | **三平台✓** |
| 半透明材料（translucent） | ✓ `translucent`（仅列类别） | ✗ | △ 链接 `transparency and translucency` | **DB列名✓（释义见 T1）** |
| 传递光 | ✓ `Visual transparency` | ✓ `let light into rooms` | ✓ `higher efficacy` | **双平台✓** |
| 「模糊影像」「改变空间边界视觉重量」 | ✗ 未展开 | ✗ | △ `visual interest`（弱） | **解释性引申（见 T1），非逐字** |

**判定（2.1）：** definition「透明材料让视线穿透并传递光，半透明材料传递光但模糊影像；两者改变空间边界的视觉重量」与 原理「光线与视线穿过玻璃等透明材料时可传达通透与联系；半透明材料只传光而模糊影像，从而以不同程度削弱空间边界的视觉重量」之核心「透明/半透明、传递光、视觉透明性」由 **Designing Buildings（db-glass：`Glass can be transparent, translucent ... Visual transparency`）＋ Wikipedia（wp-building-material：`let light into rooms`；wp-architectural-lighting-design：`transparent ... higher efficacy`）两独立平台直证**，**成立、非编造、双平台支撑**。其中「半透明＝传光但模糊影像」为 translucent 的通用定义性释义、「改变/削弱空间边界的视觉重量」为建筑视觉的解释性概括，db-glass 只列 `translucent` 未逐字展开（见 T1），属合理补充、非编造。

### 2.2 类型性实例

- `实例`＝「名称：建筑玻璃隔断（**类型性，不指定具体项目**）；透明玻璃分隔空间而保持视线连通。此处仅列说明，不复制图像。」
- **类型性合理**：「建筑玻璃隔断」为现象类别，不绑定具体项目；内容与 db-glass `transparent` / `Visual transparency` 及 wp-building-material 玻璃采光一致。**未给具体项目名/地点/设计者/年份/数值**，无编造。

### 2.3 nv=false 形式四处一致

| 核对项 | transparent-material |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「20世纪、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py` PASS 佐证。

## 三、★ safety-guarding（安全防护）逐项核对（含 db-guardrail 防跌 / 照明·出口标识归属 / 无源成分专查）

### 3.1 概念「护栏防跌 + 照明 + 清晰出口标识」三源核对（实抓引句）

- `db-guardrail`（Designing Buildings「Guardrail」页；HTTP200，H1=Guardrail）：
  - `A guardrail is a longitudinal barrier that prevents people from falling or straying into a dangerous or restricted zone.`（**护栏为纵向屏障，防止人跌落/越界 ✓✓✓ ——直接支撑「防跌」核心**）
  - `Guardrails can be found in locations such as: On a balcony. ... On the edge of a ramp. ... On a landing. ... Along a hiking trail to prevent falls.`（**临空/挑台/坡道/平台＝「临空、下沉与高差处阻止跌落」✓✓**）
  - `Guardrails typically have ergonomic dimensions, with the top rail around 107cms (+/- 8cms) above ground level.`（**给出具体高度 107cm；正因如此，条目在限制节声明「不写死数值、须按当地规范校核」，与 D09 一致 ✓**）
- `wp-exit-sign`（Wikipedia `Exit sign`；owiki HTTP200）：
  - `An exit sign is a pictogram or short text in a public facility marking the location of the closest emergency exit to be used in an emergency that necessitates rapid evacuation.`（**出口标识指示最近紧急出口、疏散 ✓✓✓，直证「出口标识」「疏散方向」**）
  - `Most fire, building, health, and safety codes require exit signs that are always lit.` / `the sign is often permanently illuminated` / `Modern exit signs are often combined with other safety devices, such as emergency floodlighting for supplementary area illumination.`（**标识常亮/永久点亮/应急泛光照明——支撑「出口标识的照明」部分 ✓，但非泛义场地照明，见 3.2**）
- `wp-universal-design`（Wikipedia `Universal design`；owiki HTTP200）：
  - （Communication 例）`Bright and appropriate lighting, particularly task lighting`；`Clear lines of sight to reduce dependence on sound`；`Signs with light-on-dark visual contrast`（**明亮适宜照明/清晰视线/高对比标识＝支撑「照明」「预见边缘」✓✓**）
  - `In the late 1990s, any element which could make the use of the environment inconvenient for people with disabilities was considered a barrier, for example, poor public street lighting.`（**照明不足视为环境障碍＝照明属安全/可达要素 ✓**）

### 3.2 ★特别判断：db-guardrail 是否支撑「防跌」；「照明/出口标识」是否由 wp-exit-sign 支撑、有无无源成分

- **db-guardrail 是否支撑「防跌」——是，逐字直证、足够。** 依据：`A guardrail is a longitudinal barrier that prevents people from falling or straying into a dangerous or restricted zone.` 明确 `prevents people from falling`（防止人跌落），并枚举 balcony / edge of ramp / landing / hiking trail `to prevent falls` 等临空高差场景；正是「护栏在临空、下沉与高差处阻止跌落」的直述来源。**评级：足够（adequate）。**
- **「出口标识」是否由 wp-exit-sign 支撑——是，逐字直证。** `marking the location of the closest emergency exit to be used in an emergency that necessitates rapid evacuation` 直接覆盖「清晰的出口标识」「疏散方向」。
- **「照明」是否由 wp-exit-sign 支撑——部分，不足以单独支撑泛义「照明」；但整体**无**无源成分。** 精确归属：
  1. `wp-exit-sign` 能支撑的是**出口标识本体的照明**（`exit signs that are always lit` / `permanently illuminated` / `emergency floodlighting for supplementary area illumination`），即「标识被点亮/应急泛光」，**不覆盖**「照亮边缘、台阶的场地/通道照明」（definition 中「让人能预见边缘」的照明）。
  2. 泛义「照明」的直证来自 **`wp-universal-design`**：`Bright and appropriate lighting, particularly task lighting`，及 `poor public street lighting` 被列为环境障碍——照明被明确作为可达性/可辨识要素。
  3. 故「照明」这一成分**有源**（主证 wp-universal-design；wp-exit-sign 覆盖标识照明部分），**不存在无源/编造成分**。仅「照明」的归属应记于 wp-universal-design 而非 wp-exit-sign（这不是缺陷，是三源各司其职；见 T4）。
- **「预见边缘」「减少死角」**：`预见边缘` 由 `Clear lines of sight`＋`Bright and appropriate lighting`（wp-universal-design）合理支撑；`减少死角/盲区` 为对「clear lines of sight」的解释性概括（见 T4），非逐字，非编造。

| 概念要素 | db-guardrail（DB） | wp-exit-sign（WP） | wp-universal-design（WP） | 判定 |
| --- | --- | --- | --- | --- |
| 护栏防跌（临空/高差阻止跌落） | ✓✓ `barrier that prevents people from falling`；balcony/ramp/landing`to prevent falls` | — | — | **DB直证✓✓（含 DB 非维基）** |
| 出口标识（指向最近出口/疏散） | — | ✓✓ `marking the location of the closest emergency exit ... rapid evacuation` | △ `Signs with light-on-dark visual contrast` | **WP直证✓✓** |
| 照明（场地/通道照明、预见边缘） | — | △ 仅标识照明/应急泛光 | ✓ `Bright and appropriate lighting`；`poor public street lighting` | **WP（univ-design）直证✓（非 wp-exit-sign，见 T4）** |
| 减少跌坠/死角（安全防护总效） | ✓ prevents falling | ✓ rapid evacuation | △ `Clear lines of sight` | **双平台✓（死角为解释性）** |

**判定（3.1–3.2）：** definition「安全防护以护栏、照明与清晰的出口标识降低高差跌坠与死角风险，让人能预见边缘与疏散方向」与 原理「以护栏等实体屏障在临空、下沉与高差处阻止跌落，配合照明与出口标识使人能预见边缘与疏散方向，减少跌坠与死角风险」之核心——**护栏防跌（db-guardrail 逐字）、出口标识（wp-exit-sign 逐字）、照明（wp-universal-design 逐字）**——由 **Designing Buildings（db-guardrail）＋ Wikipedia（wp-exit-sign / wp-universal-design）两独立平台逐要素直证**，**成立、非编造、双平台强支撑；无无源成分**。「照明」归属应为 wp-universal-design（wp-exit-sign 仅覆盖标识照明/应急泛光），「预见边缘/减少死角」为解释性概括（T4），均属合理，非缺陷。

### 3.3 类型性实例

- `实例`＝「名称：临空处防护栏杆（**类型性，不指定具体项目**）；在边缘设置护栏阻挡跌落。此处仅列说明，不复制图像。」
- **类型性合理**：「临空处防护栏杆」为构件类别，不绑定具体项目；内容与 db-guardrail `prevents people from falling` / balcony/edge/landing 一致。**未给具体项目名/地点/设计者/年份/数值**，无编造。

### 3.4 规范 caveat 已移入限制节（核对）

- `sections.常见错误与限制`＝「栏杆高度、照度等具体数值须按当地规范与专业设计校核，本条不写死数值；实际工程须按当地规范和专业设计人员的要求。」——**具体数值（栏杆高度、照度）的规范 caveat 已置于限制节，且明确「不写死数值」，与 db-guardrail 给出的 107cm 等数值形成「引用源有数值、条目作一般性说明」的正确处理（D09）✓**；规范句在、句末带「。」✓。

### 3.5 nv=false 形式四处一致

| 核对项 | safety-guarding |
| --- | --- |
| `needs_verification`（entry） | `false` ✓ |
| `pending_notes` | `""` ✓ |
| `sections.待核实` | 「暂无已知待核实项。」✓ |
| `coverage.json` 记录 | `status 已写`、`source_count 3`、`needs_verification_count 0`、`last_updated 2026-11-24`、`level L2` ✓ |
| `time_or_place` | 「20世纪、全球（参见来源）。」无「待核实」✓ |

四处一致；`check.py` PASS 佐证。

## 四、形式核对汇总（三条）

| 核对项 | wind-driven-ventilation | transparent-material | safety-guarding |
| --- | --- | --- | --- |
| 七节（定义＋原理/典型手法/实例/常见错误/一图/待核实） | ✓ 6 节全非空 | ✓ 6 节全非空 | ✓ 6 节全非空 |
| SVG 数量 / 画布 | ✓ 1 张，`viewBox='0 0 760 400'` | ✓ 1 张，`viewBox='0 0 760 400'` | ✓ 1 张，`viewBox='0 0 760 400'` |
| SVG 越界 / 外链 | ✓ 元素均在框内（x 40–560,y 40–375）；无 `<image>/<script>/href=/url(`/xlink | ✓ 元素均在框内（x 100–430,y 90–370）；无外链 | ✓ 元素均在框内（x 80–680,y 140–375）；无外链 |
| SVG 注记 | ✓ 含「示意图，非施工图」 | ✓ 含「示意图，非施工图」 | ✓ 含「示意图，非施工图」 |
| 规范句（常见错误收尾） | ✓ 含「实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」，见 T3**） | ✓ 含且（**句末缺「。」，见 T3**） | ✓ 含且**句末带「。」** |
| site 与 JSON 一致 | ✓ `site/entries/wind-driven-ventilation.html` 各节标题、示意图、规范句、Designing Buildings「Ventilation」均与 JSON 一致（实读 L） | ✓ 一致，含 Designing Buildings「Glass for buildings」 | ✓ 一致，含 Designing Buildings「Guardrail」 |
| 来源数 / 双平台 | 3（wp-natural-ventilation + wp-ventilation-architecture + db-ventilation）；平台=Wikipedia×2＋Designing Buildings(DB) | 3（wp-building-material + wp-architectural-lighting-design + db-glass）；平台=Wikipedia×2＋DB | 3（wp-universal-design + wp-exit-sign + db-guardrail）；平台=Wikipedia×2＋DB |
| 新 DB 源 verified/link_ok / 引用 | ✓ verified=true、link_ok=true、各被 1 条引用 | ✓ verified=true、link_ok=true | ✓ verified=true、link_ok=true |

`check.py`：**PASS: all checks, 0 errors（EXIT=0）**；`pytest tests/test_svg_bounds.py`：**5 passed（EXIT=0）**。（三条 site HTML 实读：节标题/示意图/规范句/Designing Buildings 对应标题均在。）

## 五、★ 相似度（阈值 0.54）与 def≠原理

方法（承第97–102轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与历轮逐位一致，口径正确）**。全库 258 条。

| 条目 | 口径 | 最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- | --- |
| wind-driven-ventilation | 短① | stack-ventilation | 0.3977 | <0.54 | ✓ |
| wind-driven-ventilation | 全② | skylight | 0.3806 | <0.54 | ✓ |
| transparent-material | 短① | brutalism | 0.2921 | <0.54 | ✓ |
| transparent-material | 全② | wind-driven-ventilation | 0.3188 | <0.54 | ✓ |
| safety-guarding | 短① | drainage | 0.3380 | <0.54 | ✓ |
| safety-guarding | 全② | damp-proofing | 0.3481 | <0.54 | ✓ |

- **指定对比**（本轮实算）：`wind-driven-ventilation × natural-ventilation` 短 0.3824 / 全 0.2685；`wind-driven-ventilation × stack-ventilation` 短 0.3977 / 全 0.3350；`safety-guarding × exit-sign` 短 0.3067 / 全 0.3120；`transparent-material × material-color` 短 0.2911 / 全 0.2120——**均 <0.54 ✓**。
- 三条全库最近邻最大：wind 短 0.3977、全 0.3806；transparent 短 0.2921、全 0.3188；safety 短 0.3380、全 0.3481——**均 ≪0.54，余量充足，无任何对手 >0.54。相似度合格 ✓**。
- **def≠原理（去重）**：
  - wind-driven-ventilation `definition×原理` = **0.3871**（低重叠、两层次可分：定义「是什么」vs 原理「正/负压如何驱动气流」，去重良好）✓。
  - transparent-material `definition×原理` = **0.5253**（中等重叠：共用「透明材料…传递光/半透明材料…模糊影像/削弱·改变空间边界的视觉重量」；不同处原理增「传达通透与联系」「以不同程度」；**非逐字、非 1.0，去重成立**；重叠偏高见 T2）✓。
  - safety-guarding `definition×原理` = **0.4694**（中等重叠、两层次可分，原理细化「临空/下沉/高差」「实体屏障」）✓。

## 六、总判定与依据

**结论：**
- **`wind-driven-ventilation`（风压通风）——合格。** 概念「风压驱动、由建筑周围（迎/背风面）压差驱动的自然通风、开口促成穿流」由三源（db-ventilation＋wp-natural-ventilation＋wp-ventilation-architecture）逐要素直证；类型性实例合理、nv=false 四处一致、七节/SVG/规范句/site 一致、相似度全通过、def≠原理 0.3871 去重良好。
- **`transparent-material`（透明与半透明材料）——合格（附透明项 T1/T2/T3：半透明=传光但模糊影像、视觉重量为解释性释义；def×原理 0.5253 中等重叠；规范句句末缺句号）。** 概念「透明/半透明、传递光、视觉透明性」由 db-glass（`Glass can be transparent, translucent ... Visual transparency`）＋ wp-building-material（`let light into rooms`）＋ wp-architectural-lighting-design 两平台直证；类型性实例合理、nv=false 四处一致、结构/相似度全通过。
- **`safety-guarding`（安全防护）——合格（附透明项 T4：「照明」主证来自 wp-universal-design、wp-exit-sign 仅覆盖标识照明/应急泛光；「预见边缘/减少死角」为解释性；无无源成分）。** 概念「护栏防跌＋出口标识＋照明」由 db-guardrail（`barrier that prevents people from falling`，逐字支撑防跌）＋ wp-exit-sign（`marking the location of the closest emergency exit ... rapid evacuation`）＋ wp-universal-design（`Bright and appropriate lighting`）两独立平台逐要素直证；规范 caveat 已入限制节、类型性实例合理、nv=false 四处一致、结构/相似度全通过。

依据（逐项对齐任务核对点）：
1. **definition/原理 双平台支撑（含 DB 非维基）**：
   - wind：`风压驱动/压差驱动` 由 db-ventilation（`can be wind driven` / `driven by natural pressure differences`）＋ wp-natural-ventilation（`wind driven ventilation arises from the different pressures created by wind around a building`）＋ wp-ventilation（`wind pressure` / `pull and push air`）**双平台（DB＋WP）直证✓**。
   - transparent：`透明/半透明、传递光、视觉透明性` 由 db-glass（`transparent, translucent ... Visual transparency`）＋ wp-building-material（`let light into rooms`）＋ wp-arch-lighting（`transparent ... higher efficacy`）**双平台直证✓**。
   - safety：`防跌` db-guardrail（`prevents people from falling`）＋`出口标识` wp-exit-sign（`closest emergency exit ... rapid evacuation`）＋`照明` wp-universal-design（`Bright and appropriate lighting`）；**DB＋WP 双平台✓**。
2. **是否编造**：三条均无虚假具体事实；wind「迎风正压/背风负压」、transparent「模糊影像/视觉重量」、safety「预见边缘/死角」为通识性/解释性概括（T1/T4/T5），非编造。
3. **类型性实例合理**：wind「对流通风的房间」、transparent「建筑玻璃隔断」、safety「临空处防护栏杆」均标「类型性，不指定具体项目」、无地点/设计者/年份/数值，内容与 DB 有源一致 ✓。
4. **nv=false 落地+形式四处一致**：三条 entry nv=false / pending="" / 待核实=暂无 / coverage needs_verification_count=0；time_or_place 无「待核实」；`check.py` PASS ✓。
5. **七节/SVG/规范句/site**：三条均 6 节全非空、SVG 1 张 `760×400` 框内无外链含「示意图，非施工图」、规范句在（wind/transparent 句末缺句号 T3，safety 带句号）、site 与 JSON 一致；`check.py` PASS、`pytest` 5 passed ✓。
6. **相似度**：wind 短 max 0.3977 / 全 0.3806；transparent 短 0.2921 / 全 0.3188；safety 短 0.3380 / 全 0.3481；指定对比均 <0.54；方法自校 0.5157 ✓。
7. **来源**：三条各 3 源、DB 与 Wikipedia 两独立平台；新增 db-ventilation / db-glass / db-guardrail verified=true、link_ok=true、各被 1 条引用 ✓。

透明说明（不改合格判定，供 lead 决策）：
- **(T1) transparent-material「半透明=传光但模糊影像」「改变/削弱空间边界的视觉重量」为通识定义/建筑视觉的解释性概括**：db-glass 仅列 `transparent, translucent ...` 未逐字展开 translucent 的「传光不传像」；属合理概括、非编造。可与 `wp-building-material let light into rooms` 及 `wp-arch-lighting` 视觉段互参。
- **(T2) transparent-material def×原理 = 0.5253**：中等偏高重叠（共用「透明材料…传递光/半透明材料…模糊影像/削弱空间边界的视觉重量」），但非逐字、非 1.0，两层次（是什么 vs 机理「传达通透与联系」）基本可分，去重成立；如需更彻底可让原理更侧重「透射/漫射的光学机理」。
- **(T3) wind / transparent 两条「常见错误与限制」规范句句末缺「。」**（`…专业设计人员的要求`，与 r101/r102 T3 同型）；safety 该节句末有「。」。纯格式小疵，`check.py` 未拦（`REGULATION_NOTE` 只匹配子串）。
- **(T4) safety-guarding「照明」归属与解释性成分**：definition 泛义「照明」的直证来自 `wp-universal-design`（`Bright and appropriate lighting` / `poor public street lighting` 为障碍），而 `wp-exit-sign` 仅覆盖「标识常亮/永久点亮/应急泛光照明」；故「照明」有源但不宜说由 wp-exit-sign 单独支撑；「预见边缘/减少死角」由 `Clear lines of sight` 合理引申。**均为归属/解释性说明，不构成无源或编造**。
- **(T5) wind-driven「迎风面正压、背风面负压」**：为标准流体力学通识，由 wp-natural-ventilation `different pressures … permit flow` 与 wp-ventilation `pull and push air` 蕴含，非逐字引用，非编造。
- **(T6) 命名/重定向口径**：`db-glass` url 记 `/wiki/Glass`，实抓重定向至 `/wiki/Glass_for_buildings`（H1=`Glass for buildings`），link_ok 语义不受影响；`wp-architectural-lighting-design` title「Architectural lighting design」而 url=`…/wiki/Architectural_lighting`（重定向到 Architectural_lighting_design，H1 与本轮一致）；`wp-natural-ventilation` title「Passive ventilation」而 url=`…/Natural_ventilation`（owiki H1=`Passive ventilation`）——均同名异名/重定向，承前轮一致，非本条新问题。entry title「透明与半透明材料」与任务「透明材料」为命名口径差异，非错误。

## 七、机器可读汇总

```
ROUND=103
SAMPLER=spotcheck-r103
SCOPE=["wind-driven-ventilation","transparent-material","safety-guarding"]
READONLY="only wrote research/spotcheck-round103.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-ventilation":"web_fetch HTTP200 H1=Ventilation (no redirect)",
 "db-glass":"web_fetch HTTP200 redirect /wiki/Glass->/wiki/Glass_for_buildings H1='Glass for buildings'",
 "db-guardrail":"web_fetch HTTP200 H1=Guardrail (no redirect)",
 "wp-natural-ventilation":"owiki.org HTTP200 H1='Passive ventilation'",
 "wp-ventilation-architecture":"owiki.org HTTP200 H1='Ventilation (architecture)'",
 "wp-building-material":"owiki.org HTTP200 H1='Building material'",
 "wp-architectural-lighting-design":"owiki.org HTTP200 H1='Architectural lighting design'",
 "wp-universal-design":"owiki.org HTTP200 H1='Universal design'",
 "wp-exit-sign":"owiki.org HTTP200 H1='Exit sign'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
GIT={"changed":["M coverage.json","M data/sources.json","M entries/batch-02-c.json","M entries/batch-08.json","M entries/batch-36.json","M site/entries/safety-guarding.html","M site/entries/transparent-material.html","M site/entries/wind-driven-ventilation.html","M site/index.html","M site/sources.html","?? tools/apply_review_round103.py"],"note":"fixer outputs; sampler read-only"}

WIND_DRIVEN={
 "verdict":"合格",
 "change":"sources +db-ventilation; 实例->typological; 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-ventilation (Ventilation)","Wikipedia wp-natural-ventilation (Passive ventilation)","Wikipedia wp-ventilation-architecture (Ventilation (architecture))"],
   "wind_driven":"db 'can be wind driven, or buoyancy driven' + wp-natvent 'wind driven ventilation arises from the different pressures created by wind around a building' + wp-vent 'Wind-driven ventilation relies upon the force of the prevailing wind' -> TRIPLE direct",
   "pressure_difference":"db 'driven by natural pressure differences' + wp-natvent 'different pressures created by wind around a building' + wp-vent 'wind pressure' -> TRIPLE",
   "openings_flow":"wp-natvent 'openings ... permit flow through the building' + wp-vent 'pull and push air through the enclosed space' -> DOUBLE",
   "holds":true},
 "special_judgment_has_db_nonwiki":"db-ventilation supplies explicit 'wind driven' + 'natural pressure differences' -> ADEQUATE non-wiki platform",
 "fabrication":"none (迎风正压/背风负压为标准流体力学概括, implied by 'different pressures...permit flow'/'pull and push')",
 "instance":{"text":"对流通风的房间(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.3871,"distinct":true},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"stack-ventilation 0.3977","nearest_full":"skylight 0.3806","vs_natural_ventilation_short":0.3824,"vs_natural_ventilation_full":0.2685,"max_short":0.3977,"max_full":0.3806,"lt_0.54":true},
 "transparency":["T3 常见错误句末缺句号","T5 迎风正压/背风负压为通识引申","T6 db-glass/wp重定向口径"]
}

TRANSPARENT_MATERIAL={
 "verdict":"合格(附透明项T1/T2/T3)",
 "change":"sources +db-glass; 原理改写(与def去重); 实例->typological; 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-glass (Glass for buildings)","Wikipedia wp-building-material (Building material)","Wikipedia wp-architectural-lighting-design (Architectural lighting design)"],
   "transparent_translucent":"db 'Glass can be transparent, translucent ... Visual transparency' + wp-bm 'let light into rooms' + wp-arch 'transparent ... higher efficacy' -> TRIPLE",
   "light_transmission":"db 'Visual transparency' + wp-bm 'let light into rooms' -> DOUBLE",
   "translucent_blur_visual_weight":"interpretive gloss (db only lists 'translucent'); see T1",
   "holds":true},
 "fabrication":"none (半透明=传光但模糊影像为translucent通用释义, 视觉重量为解释性, 非编造)",
 "instance":{"text":"建筑玻璃隔断(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.5253,"distinct_below_1":true,"note":"中等偏高重叠,非逐字非1.0,去重成立"},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"brutalism 0.2921","nearest_full":"wind-driven-ventilation 0.3188","vs_material_color_short":0.2911,"vs_material_color_full":0.2120,"max_short":0.2921,"max_full":0.3188,"lt_0.54":true},
 "transparency":["T1 半透明=传光但模糊影像/视觉重量为解释性","T2 def×原理0.5253中等偏高","T3 常见错误句末缺句号","T6 title透明与半透明vs透明材料"]
}

SAFETY_GUARDING={
 "verdict":"合格(附透明项T4)",
 "change":"sources +db-guardrail; 原理改写; 实例->typological; 常见错误含规范caveat(实际读含规范句+句号); 待核实清空; nv true->false; pending cleared",
 "concept_dual_source":{
   "platforms":["Designing Buildings db-guardrail (Guardrail)","Wikipedia wp-exit-sign (Exit sign)","Wikipedia wp-universal-design (Universal design)"],
   "fall_prevention":"db-guardrail 'A guardrail is a longitudinal barrier that prevents people from falling or straying into a dangerous or restricted zone' + balcony/ramp/landing 'to prevent falls' -> DB direct (ADEQUATE, verbatim)",
   "exit_signage":"wp-exit-sign 'marking the location of the closest emergency exit to be used in an emergency that necessitates rapid evacuation' -> WP direct",
   "lighting":"wp-universal-design 'Bright and appropriate lighting, particularly task lighting' + 'poor public street lighting' as barrier -> WP direct; wp-exit-sign only covers sign illumination/emergency floodlighting",
   "foresee_edge_deadcorner":"wp-universal-design 'Clear lines of sight' -> interpretive gloss",
   "holds":true},
 "special_judgment":{
   "db_guardrail_supports_fall":"YES verbatim 'prevents people from falling'; adequate",
   "exit_sign_supports_exit_signage":"YES verbatim",
   "lighting_attribution":"general lighting from wp-universal-design NOT wp-exit-sign; wp-exit-sign covers only sign lighting/emergency floodlighting; NO unsourced component"},
 "fabrication":"none (预见边缘/减少死角为解释性; 照明有源)",
 "instance":{"text":"临空处防护栏杆(类型性,不指定具体项目)","typological":true,"specific_project":false,"no_place_designer_year_number":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无 / coverage source_count=3 nv_count=0 four-place consistent; time_or_place clean; check.py PASS",
 "def_vs_principle":{"ratio":0.4694,"distinct":true},
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"reg_period":true,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"drainage 0.3380","nearest_full":"damp-proofing 0.3481","vs_exit_sign_short":0.3067,"vs_exit_sign_full":0.3120,"max_short":0.3380,"max_full":0.3481,"lt_0.54":true},
 "transparency":["T4 照明主证属wp-universal-design(非wp-exit-sign泛义);预见边缘/死角为解释性;无无源成分","T6 重定向口径"]
}

METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258}
VERDICT={"wind-driven-ventilation":"合格","transparent-material":"合格(附透明项T1/T2/T3)","safety-guarding":"合格(附透明项T4)"}
KEY_FINDING="三条 nv=false 升级均成立、均合格。wind-driven-ventilation 风压通风: 概念『风压驱动/建筑周围压差驱动自然通风/开口穿流』由 db-ventilation('can be wind driven, or buoyancy driven'/'driven by natural pressure differences') + wp-natural-ventilation('wind driven ventilation arises from the different pressures created by wind around a building, and openings ... permit flow') + wp-ventilation('wind pressure'/'pull and push air') 双平台直证; def×原理0.3871; 相似度短0.3977/全0.3806<0.54。transparent-material 透明与半透明材料: 概念『透明/半透明/传递光/视觉透明性』由 db-glass('Glass can be transparent, translucent ... Visual transparency') + wp-building-material('let light into rooms') + wp-architectural-lighting-design 双平台直证; def×原理0.5253(已与def去重,非1.0); 相似度短0.2921/全0.3188<0.54。safety-guarding 安全防护: 特别核查——db-guardrail 逐字支撑防跌('A guardrail is a longitudinal barrier that prevents people from falling'), 足够;出口标识由 wp-exit-sign 逐字支撑('marking the location of the closest emergency exit ... rapid evacuation');照明由 wp-universal-design 直证('Bright and appropriate lighting'/'poor public street lighting'为障碍), wp-exit-sign 仅覆盖标识照明/应急泛光, 故照明有源但归属univ-design非exit-sign, 无无源成分;规范caveat(栏杆高度/照度数值)已移入限制节; def×原理0.4694; 相似度短0.3380/全0.3481<0.54。三条均: 类型性实例(不指定具体项目)合理不编造; nv=false四处一致; 七节/SVG(760x400框内无外链含示意图非施工图)/site一致; check.py PASS+pytest 5 passed; 相似度全<0.54(方法自校0.5157). 透明项: T1/T2(transparent释义与def重叠), T3(wind/transparent常见错误句末缺句号), T4(safety照明归属与解释性), T5(wind正负压通识引申), T6(重定向/命名口径). 均不改变合格判定。"
```

## 八、只读核验

- 除本报告 `research/spotcheck-round103.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 六个 Wikipedia 源本轮均经 `owiki.org` 同文镜像 HTTP200 抓回（en.wikipedia 本环境承前阻断，H1 逐一核对一致）；三个 DB 源经 `web_fetch` 直抓 HTTP200（db-ventilation H1=Ventilation；db-glass 经 /wiki/Glass→/wiki/Glass_for_buildings H1=Glass for buildings；db-guardrail H1=Guardrail）。
- 词扫描、相似度、去重、结构、SVG 越界/外链、site 一致性、git 核对均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中的改动文件与 `?? tools/apply_review_round103.py` 均为**他方（round103 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
