# 第106轮质量抽检（spotcheck-round106）——vestibule / eclecticism 双平台支撑与 DB 页「是否真直接支撑」核查

- 抽检人：spotcheck-r106（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象（均宣称升级 nv=false、类型性实例，实读当前 JSON 为准）：
  1. `vestibule`（门厅）——entry 在 `entries/batch-27.json`；sources = `wp-vestibule-architecture`（Wiki）+ `db-vestibule`（DB）；coverage：status 已写 / source_count 2 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
  2. `eclecticism`（折衷主义建筑）——entry 在 `entries/batch-34.json`；sources = `wp-architectural-style`（Wiki）+ `wp-history-of-architecture`（Wiki）+ `db-eclecticism`（DB）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24。
- 任务点名两条要特别判断的 DB 非维基源：`db-vestibule`（URL `/wiki/Vestibule` 实为 Lobby 页）、`db-eclecticism`——是否**真直接支撑**对应概念（非泛述）。结论见各节 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round106.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词比对、相似度、去重、结构、SVG 越界、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-27.json / M entries/batch-34.json / M site/entries/eclecticism.html / M site/entries/vestibule.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round106.py`——**均为 round106 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-vestibule`（记 url `…/wiki/Vestibule`）→ `web_fetch` **实际重定向到 `https://www.designingbuildings.co.uk/wiki/Lobby`，HTTP 200，H1=`Lobby`**（Last edited 24 Oct 2025）。**即 DB 的「Vestibule」并非独立页，重定向到「Lobby」页。**
  - `db-eclecticism`（记 url `…/wiki/Eclecticism`）→ `web_fetch` **实际重定向到 `https://www.designingbuildings.co.uk/wiki/Eclecticism_in_architecture`，HTTP 200，H1=`Eclecticism in architecture`**（Last edited 15 Jun 2022）。
  - `wp-vestibule-architecture`（记 `en.wikipedia.org/wiki/Vestibule_(architecture)`）→ en.wikipedia 直连 **fetch failed**（本环境同 D05 限制）；经镜像 `https://owiki.org/wiki/Vestibule_(architecture)` **HTTP 200**，H1=`Vestibule (architecture)`，逐句核对。
  - `wp-architectural-style`（记 `…/Architectural_style`）→ en 直连 fetch failed；经镜像 `https://owiki.org/wiki/Architectural_style` **HTTP 200**，H1=`Architectural style`。
  - `wp-history-of-architecture`（记 `…/History_of_architecture`）→ en 直连 fetch failed；经镜像 `https://owiki.org/wiki/History_of_architecture` **HTTP 200**，H1=`History of architecture`（含 `### Revivalism and Eclecticism` 专节；该节正文被镜像在「New Classical archit…」处截断，下方透明说明）。
  - （canonical url 在 sources.json 记的是 en.wikipedia；本轮因直连失败改用 owiki.org 镜像抓正文，H1 与条目一致，属抓取环境限制，非数据缺陷。）
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`19 passed in 0.36s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径② = 0.5157（与 r104b/r105 逐位一致，方法正确）。全库 258 条，无重复 id。**

---

## 一、`vestibule`（门厅）

### 1.1 当前 entry 实读（`entries/batch-27.json` L6–36）
- `definition`＝「门厅是进入较大空间前的小型过渡房间，用作等候、缓冲内外环境并组织出入人流。」
- `原理`＝「作为“内外之间”的过渡房间，门厅提供受控的等候与缓冲，并承担进入的人流组织、安全与过渡照明。」
- `overview`＝「门厅位于室内与街道之间，可挡风、减少热损失，并为来访者提供安全的过渡与等候空间。」
- `实例`＝「名称：公共建筑门厅（类型性，不指定具体项目）；位于主入口附近，作为进入前的过渡与等候空间。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「门厅过小会造成拥堵、过大则浪费能耗；疏散与无障碍宽度须按当地规范校核。实际工程须按当地规范和专业设计人员的要求。」
- sources = wp-vestibule-architecture / db-vestibule；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=跨时期、全球（参见来源）。`

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①进入较大空间前的小型过渡房间；②等候；③缓冲内外环境（挡风/减热损）；④组织出入人流；⑤安全；⑥过渡照明。

**wp-vestibule-architecture（Wikipedia；owiki HTTP200，H1=`Vestibule (architecture)`）——①强、②③⑤强、④部分：**
- `A vestibule is a small room leading into a larger space such as a lobby, entrance hall, or passage, for the purpose of waiting, withholding the larger space from view, reducing heat loss, providing storage space for outdoor clothing, etc.`（**①小房间通向较大空间 ✓✓；②waiting ✓；③reducing heat loss / withholding larger space from view ✓**）
- `In modern usage, the term vestibule refers to a small room or antechamber between a building's entrance and main hall … It is the space one occupies once passing the door, but not yet in the main interior of the building.`（**① ✓✓ 门与主厅之间的过渡小空间**）
- `designed to elicit a sense of grandeur by contrasting the vestibule's small space with the following greater one`（**①small vs greater ✓**）
- `A purely utilitarian use of vestibules in modern buildings is to create an airlock entry … reduce air infiltration`；`increasing comfort near entrance doors`（**③缓冲 ✓✓**）
- Greek：`served as a barrier to the outside world, and also added security to discourage unwanted entrance`（**⑤安全 ✓**）；Roman：`two rooms, which usually served as waiting rooms or a porters' lodge where visitors could get directions or information`（**②等候 ✓；④信息/导引 ✓**）
- church：`to deaden the noise from outside`（**③缓冲 ✓**）
- **WP 未直书「过渡照明（transitional lighting）」⑥；④「组织出入人流」以「通向/穿过」隐含而非显式 access/circulation。**

**db-vestibule（Designing Buildings；`/wiki/Vestibule`→重定向 `/wiki/Lobby`，HTTP200，H1=`Lobby`）——②③④⑤⑥强、①部分：**
- `A lobby is a space from which one or more other rooms or corridors can be accessed, typically found near the main entrance to a building. It may be used for access, circulation, or as a waiting area…`（**④access+circulation=组织出入 ✓✓；②waiting area ✓；近主入口 ✓**）
- `A lobby may be referred to as a vestibule, anteroom or foyer.`（**DB 自身把 lobby 与 vestibule 列为同义——确立该页即 DB 的 vestibule 源 ✓**）
- Approved Document M：`an entrance lobby may be used to: Limit air infiltration. / Maintain comfort by controlling drafts. / Increase security. / Provide transitional lighting.`（**③缓冲（limit air infiltration / control drafts / comfort）✓✓；⑤安全（security）✓；⑥过渡照明（transitional lighting）✓✓（与原文 原理「过渡照明」逐字对应）**）
- **DB 未直书①「small room leading into a larger space / 小型、进入较大空间前」——其定义取向是「可从其进入若干房间的 hub」，与 vestibule 的「小前室」形式特征侧重点不同；①的形式定义仅 WP 直证。**

| 概念要素 | wp-vestibule | db-vestibule（DB，Lobby 页） | 判定 |
| --- | --- | --- | --- |
| ①小型过渡房间/进入较大空间前 | ✓✓ small room leading into larger space | △ 近主入口、entrance lobby，但定义是 hub「可从其进入房间之处」 | WP 强、DB 部分 |
| ②等候 | ✓ waiting（for the purpose of waiting / waiting rooms） | ✓ waiting area | **双平台 ✓✓** |
| ③缓冲内外环境（挡风/减热损） | ✓✓ reducing heat loss / airlock reduce infiltration / comfort | ✓✓ limit air infiltration / control drafts / comfort | **双平台 ✓✓** |
| ④组织出入人流 | △ 隐含（通向/穿过） | ✓✓ access, circulation | DB 强 |
| ⑤安全 | ✓ security（Greek barrier） | ✓ increase security | **双平台 ✓✓** |
| ⑥过渡照明 | ✗ | ✓✓ Provide transitional lighting | DB 直证 |

**判定（1.2）：** definition/原理的骨干——②等候、③缓冲、⑤安全、④组织出入、⑥过渡照明——**由 DB 非维基源 `db-vestibule`（Lobby 页）与 Wikipedia（`wp-vestibule-architecture`）双平台逐要素直证 ✓✓**；唯 ①「小型/进入较大空间前」的**形式特征仅 WP 直证**（DB 页把 vestibule 作为 lobby 同义处理，定义偏 hub）。总体两平台支撑成立、互补（WP 给形式定义，DB 给入口门厅的缓冲/等候/出入/过渡照明/安全功能）。

### 1.3 ★特别判断：db-vestibule（实为 Lobby 页）是否真直接支撑「门厅」对应概念（非泛述）
**结论：是，属直接功能支撑（非泛述）；但「小型/进入较大空间前」的形式定义仅由 WP 提供。**
- **它是 DB 的 vestibule 源，而非不相干的通类页**：`/wiki/Vestibule` **重定向到** `/wiki/Lobby`，且 Lobby 页正文 `A lobby may be referred to as a vestibule, anteroom or foyer` **明确把 vestibule 列为该页同义词**——与 r105 的 `db-window`（一个「Window」大类通页、与「侧窗采光」是不同对象）情形**根本不同**。
- **对 entry 的「原理」逐要素直证**：`waiting area`→等候；`access, circulation`→组织出入；`Limit air infiltration / controlling drafts / maintain comfort`→缓冲；`Increase security`→安全；`Provide transitional lighting`→**过渡照明（逐字对应）**。这不是泛述，而是与 entry 原理条款一一对应的功能描述。
- **残留缺口（透明 T）**：该页主对象/定义是 **lobby（一个「可从其进入若干房间」的枢纽），并非「进入较大空间前的小型前室」**；`小型` 与 `进入较大空间前` 的**形式定义只落在 WP**。因此若 lead 采用「定义的形式特征也须 DB 逐句直证」的最严口径，本条 DB 侧可视为对①的部分；但按「概念骨干（等候/缓冲/组织出入/安全/过渡照明）双平台直证」口径，db-vestibule **足以作第二直接源**。
- **与 r105 db-window 的对照结论**：db-window 只支撑「窗=开洞引入光」且完全不含侧窗方向/进深概念→判待核实；db-vestibule 则显式同义并逐条命中原 entry 原理→**判直接支撑**。二者不可等同。

### 1.4 是否编造
- definition/原理各要素均有实源逐句可溯源（WP 形式定义 + DB 功能条款），**非编造 ✓**；overview（挡风/减热损/安全过渡）在 WP（reducing heat loss、security）可溯源。唯 `小型/进入较大空间前` 细项依赖 WP 单平台——属**第二源深度细节**而非编造。

### 1.5 类型性实例合理性
- 「公共建筑门厅（类型性，不指定具体项目）；位于主入口附近，作为进入前的过渡与等候空间」——合理：公共建筑入口设门厅作过渡/等候，是标准类型级例证；未虚构具体项目/地点/年代。✓

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ |
| entry.pending_notes | "" | ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 2 / L2 / 2026-11-24） | ✓ |
| time_or_place | 「跨时期、全球（参见来源）。」无「待核实」 | ✓ |
- **形式四处一致 ✓，check.py PASS；内容前提（双平台支撑，骨干逐要素直证）已满足，nv=false 成立（唯①形式细节为 WP 单平台的 T 说明）。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | 实读 `SECS=6` 且各节非空（最短节 9 字）+ definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素（rect 80–260/150–290、260–500/170–270、500–680/150–290；text 300,130 / 300,375）均落框内，**OOB=NONE** | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(`（external_ref=False） | ✓ |
| SVG 注记 | 含「示意图，非施工图」（含 figcaption「图 1：示意图，非施工图」） | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求。」**句末有「。」**（entry 与 site 均带） | ✓ |
| site 与 JSON 一致 | `site/entries/vestibule.html`：title=门厅、lead=overview、核心定义/原理/实例/常见错误与 JSON 逐句一致（实读 L4/L9/L10/L12/L14/L15） | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| vestibule | 短① | corridor-space | 0.3243 | ✓ <0.54 |
| vestibule | 全② | wind-driven-ventilation | 0.3467 | ✓ <0.54 |
| def×原理（去重） | — | — | 0.3614 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54，无对手越阈 ✓**；方法自校 0.5157 ✓。

### 1.9 条目1 结论
**`vestibule`（门厅）——合格（附 T 透明说明）。**
- 依据：definition/原理骨干（等候/缓冲/组织出入/安全/过渡照明）由 **DB 非维基源 `db-vestibule`（Lobby 页，`/wiki/Vestibule` 重定向至此，正文明确 `a lobby may be referred to as a vestibule`，并以 access/circulation、waiting area、limit air infiltration/control drafts/comfort、increase security、provide transitional lighting 逐条命中 entry 原理）与 `wp-vestibule-architecture`（small room leading into a larger space、for the purpose of waiting、reducing heat loss、security 等）双平台逐要素直证**——`db-vestibule` **足以作第二直接源，属直接功能支撑非泛述**（★特别判断为「是」）。非编造（WP 形式定义逐句可溯，DB 功能条款逐条对应）；类型性实例合理；nv=false 四处形式一致且内容前提成立；七节/SVG（OOB=NONE、无外链、含注记）/规范句（句末带「。」）/site 均过；相似度短 0.3243 全 0.3467、def×原理 0.3614 均 <0.54；check.py PASS、pytest 19 passed；方法自校 0.5157。
- **T 透明说明（不阻断合格）**：`db-vestibule` 实为 DB 的 **Lobby** 页（Vestibule 重定向至此），其自身定义取向是「可从其进入若干房间的入口枢纽」，而「小型/进入较大空间前」的**形式定义只由 WP 直证**。若 lead 要求「定义的形式特征亦须 DB 逐句直证」，可考虑补一条 DB 直接定义「vestibule = small room leading into a larger space」之页（占位 `DB_VESTIBULE_FORMAL_SRC`）或在来源注记注明「形式定义依据 Vestibule (architecture)（Wikipedia），功能条目依据 Lobby（Designing Buildings）」；否则本条按「骨干双平台直证」即判合格。

---

## 二、`eclecticism`（折衷主义建筑）

### 2.1 当前 entry 实读（`entries/batch-34.json` L353–383）
- `definition`＝「折衷主义是在同一设计中混用多种历史风格语汇的取向。」
- `原理`＝「折衷主义不拘单一风格，按功能、造价与表现意图，从古典、哥特、文艺复兴等语汇中择取元素并置，靠比例与构图求统一。」
- `overview`＝「它不专守某一体式，按需要挑选古典、哥特或文艺复兴元素拼合。」
- `实例`＝「名称：折衷主义公共建筑（类型性，不指定具体项目）；在同一立面中并置古典、哥特、文艺复兴等母题。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「混搭失当会杂乱；需统一比例与秩序。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-architectural-style / wp-history-of-architecture / db-eclecticism；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=文艺复兴至19世纪、全球（参见来源）。`、`period=文艺复兴至19世纪`

### 2.2 definition/原理 两平台核对（实抓引句）
概念拆解：①同一设计中混用多种历史风格；②不拘单一风格；③择取元素并置；④靠比例/构图求统一（原理）；⑤类型性实例并置古典/哥特/文艺复兴母题。

**db-eclecticism（Designing Buildings；`/wiki/Eclecticism`→重定向 `/wiki/Eclecticism_in_architecture`，HTTP200，H1=`Eclecticism in architecture`）——①②③强：**
- `Eclecticism is an architectural style that flourished in the 19th and 20th-centuries. It refers to any design that incorporates elements of traditional motifs and styles, decorative aesthetics and ornaments, structural features, and so on, that originated from other cultures or architectural periods.`（**①同一设计混用源自其他文化/历史时期的传统母题与风格 ✓✓；②不拘单一 ✓；③择取元素并置 ✓✓**）
- `the main driving force behind eclecticism was the harnessing of historic styles to create something original and new, rather than simply to revive older styles.`（**③把历史风格为我所用、合成新物 ✓**）
- 罗列复兴风格：`Classical revival / Colonial revival / Exotic revival / Gothic revival / Italian renaissance revival / Spanish colonial revival / Tudor revival`（**多种历史风格 ✓**）

**wp-history-of-architecture（Wikipedia；owiki HTTP200，H1=`History of architecture`）——①③在 19 世纪脉络下支撑（专节，正文截断）：**
- 专节标题 `### Revivalism and Eclecticism`；首句 `The 19th century was dominated by a wide variety of stylistic revivals, variations, and interpretations. Revivalism in architecture is the use of visual styles that consciously echo the style of a previous architectural era.`（**把 Eclecticism 置于 19 世纪「多样风格复兴/变化」脉络，支撑①③背景 ✓；该节后续正文被镜像截断于「New Classical archit…」，未能取得更细句，见透明说明**）

**wp-architectural-style（Wikipedia；owiki HTTP200，H1=`Architectural style`）——③弱/泛：**
- `In the middle of the 19th century, multiple aesthetic and social factors forced architects to design the new buildings using a selection of styles patterned after the historical ones, and style definition became a practical matter.`（**「择取仿历史范式的一组风格」⇒ ③弱支撑 ✓；但该文为「风格」通论，未专述 eclecticism 定义**）
- `After an architectural style has gone out of fashion, revivals and re-interpretation may occur … classicism … revived … as neoclassicism.`（复兴/再诠释背景 ✓）

| 概念要素 | db-eclecticism（DB） | wp-history-of-architecture | wp-architectural-style | 判定 |
| --- | --- | --- | --- | --- |
| ①同一设计混用多种历史风格 | ✓✓ any design that incorporates elements of traditional motifs/styles…from other cultures or architectural periods | △ 专节标题「Revivalism and Eclecticism」+ 19世纪多样复兴（脉络支撑） | ✗ | **DB 强 + WP 专题脉络 ✓** |
| ②不拘单一风格 | ✓ | △ | ✗ | DB 强 |
| ③择取元素并置 | ✓✓ harnessing historic styles to create new；列七种复兴 | △ 复兴脉络 | △「a selection of styles patterned after the historical ones」 | **DB 强 + WP 泛 ✓** |
| ④靠比例/构图求统一 | ✗（原理推演，见 2.4） | ✗ | ✗ | 设计通则推理（非编造、非直引） |

**判定（2.2）：** 核心概念①③「同一设计中混用多种历史风格」**由 DB 非维基源 `db-eclecticism` 强直证 ✓✓**（`any design that incorporates elements of traditional motifs and styles … that originated from other cultures or architectural periods`），并以 `wp-history-of-architecture` 的 `### Revivalism and Eclecticism` 专节（19 世纪多样复兴脉络）与 `wp-architectural-style`（`a selection of styles patterned after the historical ones`）作 Wikipedia 平台支撑。两平台支撑成立（DB 强直 + WP 脉络/泛述）。唯原理④「靠比例与构图求统一」为**设计通则推演**，DB/WP 均无逐字句（详见 2.4）。

### 2.3 ★特别判断：db-eclecticism 是否真直接支撑「混用多种历史风格」概念（非泛述）
**结论：是，强直接支撑（非泛述）。**
- db-eclecticism 的定义句即**逐字命中概念**：`any design that incorporates elements of traditional motifs and styles, decorative aesthetics and ornaments, structural features … that originated from other cultures or architectural periods`——正是「同一设计中混用多种历史风格」；补充句 `harnessing of historic styles to create something original and new` 进一步点明「组合历史风格」的取向；并列出七种复兴风格佐证「多种历史风格」。**这不是泛述，而是对概念的直接定义**，且与「不限某一体式」的 entry 定义/概述完全吻合。
- 注：该源同时明确其时代为 **19th and 20th-centuries**（与 entry `period=文艺复兴至19世纪` 不符，见 2.4/2.6 的 Minor）。

### 2.4 是否编造
- definition/原理②③（不拘单一、择取元素并置、历史风格混用）**有实源**（db-eclecticism 逐句可溯），非编造 ✓。
- **原理④「靠比例与构图求统一」**：DB/WP 均无逐字表述，属建筑设计构图通则的合理推演（与「常见错误与限制：需统一比例与秩序」自洽），**非事实编造**，但为**无直引的推理句**——列入 T 说明。
- **period 元数据待修正**：entry `period=文艺复兴至19世纪`、`time_or_place=文艺复兴至19世纪`，而 `db-eclecticism` 明书 `flourished in the 19th and 20th-centuries`，且 `sources.json` 该源自身 note 亦写「折衷主义：19–20世纪并采多种历史风格的建筑取向」。**entry 的「文艺复兴（起）→19世纪（止）」与来源「19–20世纪」两端均不一致**（文艺复兴只是被择取的一种风格语汇，非折衷主义作为风格/运动的起始年代）。此为**元数据事实性小疵（Minor）**，非 definition/原理编造，但建议修正为「19世纪（延续至20世纪）」或「19–20世纪」。

### 2.5 类型性实例合理性
- 「折衷主义公共建筑（类型性，不指定具体项目）；在同一立面中并置古典、哥特、文艺复兴等母题」——合理：折衷主义 = 同一立面并置多种历史母题，标准类型级例证；未虚构具体项目/地点/年代。✓

### 2.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | ✓ 形式 |
| entry.pending_notes | "" | ✓ 形式 |
| sections.待核实 | 「暂无已知待核实项。」 | ✓ 形式 |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | ✓ 形式 |
| time_or_place | 「文艺复兴至19世纪、全球（参见来源）。」无「待核实」 | △ 形式齐，但 period 与 DB/sources note 的 19–20 世纪不符（Minor，见 2.4） |
- **形式四处一致 ✓，check.py PASS；内容前提（定义/原理 DB+WP 支撑）成立，nv=false 成立；唯 `period/time_or_place` 的「文艺复兴至19世纪」与来源 19–20 世纪不一致，应更正（Minor，不改变定义/原理的支撑结论）。**

### 2.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节 | 实读 `SECS=6` 且各节非空（最短节 9 字）+ definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | 逐元素（rect 140–620/120–300；line x 260/380/500 与 140–620、y 120–300；text 250,350 / 40,40）均落框内，**OOB=NONE** | ✓ |
| SVG 外链 | 无 `<image>/<script>/xlink/href=/url(`（external_ref=False） | ✓ |
| SVG 注记 | 含「示意图，非施工图」 | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**句末缺「。」**（entry L369 与 site L15 均缺；site 页脚 note 处带「。」）——同 r101–r105 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/eclecticism.html`：lead=overview、核心定义/常见错误与 JSON 逐句一致（实读 L9/L10/L15） | ✓ |

### 2.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| eclecticism | 短① | neoclassical | 0.3896 | ✓ <0.54 |
| eclecticism | 全② | wind-driven-ventilation | 0.3550 | ✓ <0.54 |
| def×原理（去重） | — | — | 0.2750 | ✓ 已去重、两层次可分 |
- 全库最大：短 0.4960、全 0.5256（同上）——**均 <0.54 ✓**；方法自校 0.5157 ✓。def×原理 0.2750 印证「原理已与 def 去重」。

### 2.9 条目2 结论
**`eclecticism`（折衷主义建筑）——合格（附两处 T 说明，其一建议修正 period）。**
- 依据：核心概念「同一设计中混用多种历史风格」**由 DB 非维基源 `db-eclecticism` 强直证**（`any design that incorporates elements of traditional motifs and styles … that originated from other cultures or architectural periods`；`harnessing of historic styles to create something original and new`；列七种复兴风格），并以 `wp-history-of-architecture` 的 `### Revivalism and Eclecticism` 专节与 `wp-architectural-style`（`a selection of styles patterned after the historical ones`）作 Wikipedia 平台支撑——`db-eclecticism` **真直接支撑该概念（非泛述）**，★特别判断为「是」。非编造（关键句可溯源）；类型性实例合理；nv=false 形式齐备且内容前提成立；七节/SVG（OOB=NONE、无外链、含注记）/site 一致；相似度短 0.3896 全 0.3550、def×原理 0.2750 均 <0.54；check.py PASS、pytest 19 passed；方法自校 0.5157。
- **T1（Minor，建议修正）**：`period`/`time_or_place`「文艺复兴至19世纪」与 `db-eclecticism`「19th and 20th-centuries」及 `sources.json` 该源 note「19–20世纪」两端不符；建议改为「19世纪（延续至20世纪）」/「19–20世纪」（「文艺复兴」是被择取的风格语汇，不是折衷主义的起始年代）。
- **T2（Minor）**：`常见错误与限制`规范句句末缺「。」（与 r101–r105 同型小疵）；`原理`「靠比例与构图求统一」为设计通则推演、无逐字源（合理、非编造）。

---

## 三、机器可读汇总

```
ROUND=106
SAMPLER=spotcheck-r106
SCOPE=["vestibule","eclecticism"]
READONLY="only wrote research/spotcheck-round106.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-vestibule":"/wiki/Vestibule -> REDIRECT /wiki/Lobby HTTP200 H1='Lobby' (Last edited 24 Oct 2025)",
 "db-eclecticism":"/wiki/Eclecticism -> REDIRECT /wiki/Eclecticism_in_architecture HTTP200 H1='Eclecticism in architecture' (Last edited 15 Jun 2022)",
 "wp-vestibule-architecture":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='Vestibule (architecture)'",
 "wp-architectural-style":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='Architectural style'",
 "wp-history-of-architecture":"en.wikipedia fetch FAILED; owiki.org HTTP200 H1='History of architecture' (has ### Revivalism and Eclecticism section; body truncated at mirror)"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"19 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}

VESTIBULE={
 "verdict":"合格(附T: db-vestibule 实为 Lobby 页, '小型/进入较大空间前'形式定义仅WP; 骨干等候/缓冲/组织出入/安全/过渡照明 DB+WP逐要素直证)",
 "definition":"门厅是进入较大空间前的小型过渡房间，用作等候、缓冲内外环境并组织出入人流。",
 "principle":"作为“内外之间”的过渡房间，门厅提供受控的等候与缓冲，并承担进入的人流组织、安全与过渡照明。",
 "sources":["wp-vestibule-architecture","db-vestibule"],
 "concept_dual_source":{
   "small_room_before_larger":"wp-vestibule 'a small room leading into a larger space ... for the purpose of waiting ... reducing heat loss' / 'small room or antechamber between entrance and main hall' -> WP STRONG; db-vestibule(lobby) only entrance-lobby/ hub framing -> DB PARTIAL",
   "waiting":"wp 'for the purpose of waiting'/'waiting rooms' + db 'waiting area' -> DOUBLE OK",
   "buffer_draft_heatloss":"wp 'reducing heat loss'/'airlock reduce air infiltration'/'comfort' + db 'Limit air infiltration'/'controlling drafts'/'maintain comfort' -> DOUBLE OK",
   "organize_access_circulation":"db 'access, circulation' + wp implicit (leading into/passing door) -> DB STRONG",
   "security":"wp Greek 'added security' + db 'Increase security' -> DOUBLE OK",
   "transitional_lighting":"db 'Provide transitional lighting' (exact) ; wp none -> DB ONLY",
   "db_nonwiki_supports_concept":true,
   "holds_two_platform_for_concept":true},
 "db_vestibule_is_lobby_page":true,
 "db_vestibule_direct_vs_generic":"DIRECT functional support: /wiki/Vestibule redirects to /wiki/Lobby; page states 'a lobby may be referred to as a vestibule'; enumerates waiting area/access/circulation/limit air infiltration/control drafts/security/provide transitional lighting matching entry 原理 element-by-element. Only 'small room before larger space' formal defn is WP-only. NOT analogous to r105 db-window (which was a different generic concept).",
 "fabrication":"no; core supported by wp-vestibule (formal) + db-vestibule (functions); 'small/larger space' precise wording WP-only (second-source depth detail, not fabrication)",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); check.py PASS",
 "nv_false_grounded":true,
 "structure":{"seven_sections":true,"secs":6,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":true,"site_consistent":true,"sources":2},
 "similarity":{"threshold":0.54,"nearest_short":"corridor-space 0.3243","nearest_full":"wind-driven-ventilation 0.3467","def_vs_principle":0.3614,"lt_0.54":true},
 "transparency":["db-vestibule is the DB 'Lobby' page (Vestibule redirects here); 'small room leading into a larger space' formal defn is WP-only; functional essence (waiting/buffer/access-circulation/security/transitional lighting) DB-direct. Non-blocking; optional strengthen with DB_VESTIBULE_FORMAL_SRC."],
 "fix_suggestion":"optional: add a DB page explicitly defining vestibule as small room leading into a larger space (DB_VESTIBULE_FORMAL_SRC) or annotate source note that formal defn follows Vestibule (architecture) WP while functions follow Lobby DB. Not blocking -> 合格."
}

ECLECTICISM={
 "verdict":"合格(附T1 period 元数据与DB 19-20世纪不符建议修正; T2 规范句句末缺句号/原理④无直引)",
 "definition":"折衷主义是在同一设计中混用多种历史风格语汇的取向。",
 "principle":"折衷主义不拘单一风格，按功能、造价与表现意图，从古典、哥特、文艺复兴等语汇中择取元素并置，靠比例与构图求统一。",
 "sources":["wp-architectural-style","wp-history-of-architecture","db-eclecticism"],
 "concept_dual_source":{
   "mix_multiple_historical_styles_in_one_design":"db-eclecticism 'any design that incorporates elements of traditional motifs and styles ... that originated from other cultures or architectural periods' + 'harnessing of historic styles to create something original and new' + 7 revival styles -> DB STRONG; wp-history 'Revivalism and Eclecticism' section / 19th c stylistic revivals -> WP topical; wp-arch-style 'a selection of styles patterned after the historical ones' -> WP generic",
   "not_bound_to_single_style":"db 'rather than simply to revive older styles'/'focus on one particular style' contrasted -> DB; wp topical",
   "proportion_composition_unity":"NO direct quote in db/wp -> design-principle inference (non-fabricated, T)",
   "db_nonwiki_supports_concept":true,
   "holds_two_platform_for_concept":true},
 "db_eclecticism_direct_vs_generic":"DIRECT strong: '/wiki/Eclecticism' -> '/wiki/Eclecticism_in_architecture'; definition explicitly 'any design that incorporates elements of traditional motifs and styles ... that originated from other cultures or architectural periods' = mixing multiple historical styles; NOT generic.",
 "period_discrepancy":"entry period/time_or_place '文艺复兴至19世纪' vs db-eclecticism 'flourished in the 19th and 20th-centuries' and sources.json note '19–20世纪' -> MISMATCH (Minor, recommend 19世纪/19–20世纪). Renaissance is a style vocabulary source, not the period start.",
 "fabrication":"definition/principle core sourced (db-eclecticism) -> no; principle clause 4 'proportion/composition unity' is inference (non-fabricated); period metadata inaccurate (Minor)",
 "type_instance_ok":true,
 "nv_false_form":"four-place consistent form; check.py PASS; period mismatch noted",
 "nv_false_grounded":true,
 "structure":{"seven_sections":true,"secs":6,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"neoclassical 0.3896","nearest_full":"wind-driven-ventilation 0.3550","def_vs_principle":0.2750,"lt_0.54":true},
 "transparency":["T1 period '文艺复兴至19世纪' contradicts db-eclecticism '19th-20th c' + sources note '19–20世纪' -> correct to 19世纪/19–20世纪 (Minor, recommended fix)","T2 规范句 body 句末缺「。」; 原理④ 'proportion/composition unity' is design inference without direct quote (non-fabricated)"],
 "fix_suggestion":"recommended: change period/time_or_place to 19世纪（延续至20世纪）/19–20世纪; add trailing '。' to 常见错误与限制 规范句."
}

VERDICT={"vestibule":"合格(db-vestibule 为DB Lobby页/Vestibule重定向于此, 显式 a lobby may be referred to as a vestibule, 并以 waiting/access-circulation/limit air infiltration/control drafts/security/provide transitional lighting 逐条命中entry原理 -> 直接功能支撑非泛述; 骨干DB+WP双平台; 唯'小型/进入较大空间前'形式定义WP-only=T说明)","eclecticism":"合格(db-eclecticism 强直证'any design that incorporates elements of traditional motifs and styles...from other cultures or architectural periods'=混用多种历史风格, 非泛述; WP history-of-architecture 'Revivalism and Eclecticism' 专节+arch-style 'selection of styles patterned after historical ones' 脉络; 附T1 period文艺复兴至19世纪 vs DB 19-20世纪不符建议修正, T2规范句句末缺句号/原理④无直引)"}
KEY_FINDING="两条均为类型性实例、nv=false。★特别判断: (1) db-vestibule 实为DB Lobby页(/wiki/Vestibule 301-> /wiki/Lobby), 但页内显式 'a lobby may be referred to as a vestibule, anteroom or foyer', 且入口门厅功能限定 'Limit air infiltration / Maintain comfort by controlling drafts / Increase security / Provide transitional lighting' 与 access/circulation/waiting area 逐条对应 entry 原理(等候/缓冲/组织出入/安全/过渡照明) -> 真直接功能支撑, 非泛述; 与 r105 db-window(不同通类对象、缺侧窗概念)根本不同; 残留仅'小型/进入较大空间前'形式定义由 wp-vestibule 'a small room leading into a larger space...reducing heat loss' 单平台直证 -> 判合格附T。(2) db-eclecticism(/wiki/Eclecticism 301-> Eclecticism_in_architecture)定义句'any design that incorporates elements of traditional motifs and styles...that originated from other cultures or architectural periods'+'harnessing of historic styles to create something original and new' 强直证'同一设计混用多种历史风格', 非泛述 -> 判合格; 唯 entry period '文艺复兴至19世纪' 与 DB '19th and 20th-centuries'及sources note '19–20世纪'不符(Minor建议改19世纪/19–20世纪); 规范句句末缺句号(T小疵)。两库最大相似度 短0.496/全0.5256<0.54; def×原理 vestibule 0.3614/eclecticism 0.2750 已去重; 均七节/SVG(OOB=NONE,无外链,含示意图注记)/site一致; check.py PASS + pytest 19 passed; 方法自校0.5157。"
```

## 四、只读核验
- 除本报告 `research/spotcheck-round106.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：`db-vestibule`、`db-eclecticism` 经 `web_fetch` 直抓 HTTP200，但**均发生重定向**（`/wiki/Vestibule`→`/wiki/Lobby` H1=`Lobby`；`/wiki/Eclecticism`→`/wiki/Eclecticism_in_architecture` H1=`Eclecticism in architecture`）——此为 DB 站内重定向，非抓取失败；`wp-vestibule-architecture`、`wp-architectural-style`、`wp-history-of-architecture` 因 en.wikipedia 直连 fetch failed，经 owiki.org 镜像 HTTP200 抓回，H1 逐一核对一致（属本环境抓取限制，非数据缺陷）。
- 词比对、关键词扫描、相似度、去重、结构、SVG 逐元素越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内评论/推荐等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（19 passed）。
- `git status` 中的改动文件（coverage/sources/batch-27/batch-34/site 三页/`?? tools/apply_review_round106.py`）均为**他方（round106 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
