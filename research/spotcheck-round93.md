# 第93轮 early-islamic-architecture 抽检报告（spotcheck-round93）

- 抽检人：spotcheck-r93（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`early-islamic-architecture`（早期伊斯兰建筑，L2/重要/风格/中世纪/伊斯兰/南亚）
  - 条目：`entries/batch-46.json` 第97–127行（`id` 在第98行；`sources` 第120–124行）。
  - 覆盖：`coverage.json` 第3281–3293行（`source_count=3`、`needs_verification_count=0`、`last_updated=2026-11-24`）。
  - 来源定义：`data/sources.json` — `wp-umayyad-architecture` 第3675–3686行、`artincontext-islamic-art` 第3687–3698行、`artincontext-islamic-architecture` 第3891–3902行；三源均 `verified=true`、`link_ok=null`。
  - 产物：`site/entries/early-islamic-architecture.html`（24行，与条目一致）。
- 本轮（93）变更（据 `tools/apply_review_round93.py` 实读 + `git diff` 实读 + 当前文件实读）：
  - `sources`：`[wp-umayyad-architecture, artincontext-islamic-art]` → `[wp-umayyad-architecture, artincontext-islamic-art, artincontext-islamic-architecture]`（新增第二直接源 artincontext-islamic-architecture）。
  - `needs_verification`：`true`→`false`；`pending_notes`：`方形平面/柱廊形制单源（第二源较薄），待补第二独立来源。`→`""`。
  - `sections.待核实`：`“方形平面＋柱廊”形制主要依据单一权威来源（第二源对形制覆盖较薄），待补；具体年代细节亦待核实。`→`暂无已知待核实项。`
  - `coverage.json`：该条 `source_count` 2→3、`needs_verification_count` 1→0；`site/index.html` 顶部统计「待核实条目」164→163（与本次 nv true→false 一致）。
  - 注：`definition`/`overview`/`sections.实例` 文本本轮**未改**（上一轮已定稿）；本轮只补源并将 nv 置 false。
- 证据优先级：**独立实抓正文 > 当前文件实读 > git diff > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读、取句、比对）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round93.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- 抓取方式（本轮实抓）：
  - `wp-umayyad-architecture` = `https://en.wikipedia.org/wiki/Umayyad_architecture` → `web_fetch` 直连 **FAIL（TypeError: fetch failed）**；改用 Python urllib + 浏览器 UA → **HTTP 200**，`len=670593`，页面标题 `Umayyad architecture - Wikipedia`。
  - `artincontext-islamic-architecture` = `https://artincontext.org/islamic-architecture/` → `web_fetch` **HTTP 200**（正文被截断，仅得标题）＋ Python urllib **HTTP 200**，`len=476808`，标题 `Islamic Architecture - Building Styles Across the Muslim World`。
  - `artincontext-islamic-art` = `https://artincontext.org/islamic-art/` → Python urllib **HTTP 200**，`len=481679`，标题 `Islamic Art - A Deep Dive into the Gilded World of Islamic Art`。
- 关键实抓原句（去标签后回读）：
  - **WP（Umayyad architecture，Wikipedia 200）**：
    - `Wasit in present-day Iraq was the most important of these, and included a square Friday Mosque with a hypostyle roof.`（**方形＋hypostyle 屋顶**，正中命题）
    - `This type of plan, characterized by a covered, qibla-oriented hypostyle prayer hall and a central open sahn (courtyard) enclosed by surrounding riwaqs (arcades), is based on the layout of the early Prophet's Mosque in Medina.`（**类型化：hypostyle 礼拜殿＋中央庭院＋柱廊**）
    - `The three most important imperial mosque projects undertaken during the Umayyad period were the rebuilding of the Prophet's Mosque in Medina, the Al-Aqsa Mosque in Jerusalem, and the construction of the Great Mosque of Damascus, which are some of the most important "Arab-type" or "hypostyle-type" mosques.`（**倭马亚＋hypostyle-type**）
    - `religious structures such as the Dome of the Rock in Jerusalem and the Great Mosque of Damascus, which are considered among the greatest monuments of early Islamic architecture`（**实例：岩石圆顶＋大马士革清真寺**）
  - **Art in Context（Islamic Architecture，200）**：
    - `These cities' principal congregational mosques were designed in the hypostyle style.`（**hypostyle 直证**）
    - `It was a modest courtyard construction made of unbaked brick with a rectangle, almost square floor plan of around 56 by 53 meters.`（**方形平面约 56×53 米**）
    - `The mosque was continuously enlarged over the rest of the 7th and 8th centuries to contain a massive flat-roofed prayer hall with a central courtyard.`（**平顶礼拜殿＋中央庭院**）
    - `The courtyard design with hypostyle halls was used by all Abbasid mosques.`（**庭院＋hypostyle 厅**）
    - `The Great Mosque of Damascus and the Dome of the Rock in Jerusalem are two prominent early Islamic architectural masterpieces completed during the Umayyad period.`（**实例：大马士革清真寺＋岩石圆顶，Umayyad**）
    - 岩石圆顶图注：`Function Shrine`、`Date of Completion 691 CE`。
  - **Art in Context（Islamic Art，200）**：
    - `...the shrine in Jerusalem called the Dome of the Rock (c. 7th century CE) and the Al-Aqsa Mosque (completed in 705 CE)...`（**仅支持岩石圆顶为「shrine」＋阿克萨**）
    - **全篇无 `hypostyle`（0 次）、无 `Great Mosque of Damascus`（0 次）** → 此页对「方形平面＋柱廊」命题覆盖为 0，只能作岩石圆顶「圣所」的补充旁证。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**
- `git status --porcelain`（实读）：`M coverage.json / M entries/batch-46.json / M site/entries/early-islamic-architecture.html / M site/index.html` 及 `?? tools/apply_review_round93.py` 均为**修复方（round93 applier＋gen_site）自身产物**，非本抽检所写；抽检方仅读取。

## 一、复核 definition/实例是否由来源支撑

端内 definition：`早期伊斯兰建筑指倭马亚时期形成的清真寺与圣所形制：方形平面、柱廊与穹顶。`
端内 overview：`以方形礼拜殿与柱廊容纳信众，以穹顶标示神圣中心。`
端内 实例：`岩石圆顶（Dome of the Rock）与大马士革大清真寺（Great Mosque of Damascus）；地点：耶路撒冷、大马士革；设计者：哈里发阿卜杜勒·马利克、瓦利德一世主持；年份：岩石圆顶约 691 年、大马士革清真寺约 705 年。`

| 定义/实例要素 | wp-umayyad（实抓） | artincontext-architecture（实抓） | 判定 |
| --- | --- | --- | --- |
| **方形平面** | `a square Friday Mosque with a hypostyle roof` | `almost square floor plan of around 56 by 53 meters` | **双平台直证 ✓** |
| **柱廊／hypostyle** | `hypostyle roof`、`hypostyle prayer hall … riwaqs (arcades)` | `designed in the hypostyle style`、`hypostyle halls` | **双平台直证 ✓** |
| **穹顶／圣所** | 岩石圆顶列为 early Islamic 名构（Dome of the Rock） | `Function Shrine`（岩石圆顶图注）；Domes 专节 | both 直证（穹顶作相邻要素）|
| **倭马亚时期** | `during the Umayyad period`、`Umayyad architecture` | `During the Umayyad period`、`The Umayyad Era (661–750 CE)` | 双证 ✓ |
| **实例：岩石圆顶＋大马士革大清真寺** | `Dome of the Rock … and the Great Mosque of Damascus … greatest monuments of early Islamic architecture` | `The Great Mosque of Damascus and the Dome of the Rock … two prominent early Islamic architectural masterpieces … Umayyad period` | **双平台直证 ✓** |
| **年份（约691／约705）** | 首段 `Dome of the Rock (688–692)`、`Great Mosque of Damascus (705–715)` | `Date of Completion 691 CE`；大马士革 705 期 | 一致（`约` 前缀合理）✓ |
| **主持者（阿卜杜勒·马利克／瓦利德一世）** | 阿卜杜勒·马利克建岩石圆顶、瓦利德一世建大马士革清真寺 | 岩石圆顶图注另列 Architect `Raja ibn Haywa` | 与 WP 一致（`主持`＝委托者，非杜撰）|

**判定（复核 definition/实例）：** 定义中的「方形平面＋柱廊（hypostyle）」核心形制由 **Wikipedia 与 Art in Context 两个独立平台直接、同时**证成；实例「岩石圆顶＋大马士革大清真寺」亦在**两平台**各自被明确列为倭马亚/early Islamic 代表建筑并给出年代。`穹顶/圣所` 由两页（Dome of the Rock 图注 `Function Shrine`／`shrine in Jerusalem`）支撑。definition/实例**均由来源支撑，无超源**。

## 二、复核「方形平面＋柱廊」是否确由 wp-umayyad + artincontext 双独立平台直证

| 约束 | 证据 | 结论 |
| --- | --- | --- |
| wp-umayyad 直证「方形＋柱廊」 | `a square Friday Mosque with a hypostyle roof`；`hypostyle prayer hall … enclosed by surrounding riwaqs` | **直证 ✓** |
| artincontext-architecture 直证「方形＋柱廊」 | `designed in the hypostyle style`；`almost square floor plan of around 56 by 53 meters`；`flat-roofed prayer hall with a central courtyard` | **直证 ✓** |
| 两源分属不同平台 | Wikipedia（en.wikipedia.org） vs Art in Context（artincontext.org） | **两独立平台 ✓** |
| 二者非复制关系 | 措辞、结构、例证不同（WP 举 Wasit/Samarra；AIC 举 Kufa/Fustat/先知寺 56×53m） | **独立 ✓** |
| 命题与句意吻合 | WP「square…hypostyle」；AIC「hypostyle style…square floor plan…flat-roofed prayer hall…central courtyard」——同一「方形平面＋柱廊（flat-roofed hypostyle）＋中央庭院」模型 | **吻合 ✓** |

**判定：** 「方形平面＋柱廊（hypostyle）」**确由 wp-umayyad（Wikipedia）与 artincontext-islamic-architecture（Art in Context）双独立平台直证**，与上一轮悬置的「第二源对形制覆盖较薄」正相反——本轮新增的 AIC 建筑页对该形制覆盖**充分且直白**，命题成立。

## 三、复核两源是否独立（含「两个 artincontext 页」特别判断）

当前 `sources` 三源 = `wp-umayyad-architecture`（Wikipedia）＋`artincontext-islamic-art`（Art in Context）＋`artincontext-islamic-architecture`（Art in Context）。

| 维度 | wp-umayyad | artincontext-architecture | artincontext-islamic-art | 是否独立 |
| --- | --- | --- | --- | --- |
| 出版方 | Wikipedia | Art in Context | Art in Context | WP 与 AIC **两平台**；两个 AIC 页**同平台** |
| 对「方形＋柱廊」覆盖 | 直证 | **直证（充分）** | **无（0 次 hypostyle / 0 次 Damascus）** | 第二直接源＝AIC 建筑页 |
| 对「岩石圆顶＝圣所」 | 支持 | 支持（Function Shrine） | 支持（shrine in Jerusalem） | 补充旁证 |
| 内容关系 | 独立百科 | 独立内容站 | 同站另一主题（艺术） | WP⊥AIC；两 AIC 页同一出版方 |

**特别判断（关键项）：** 题目提示「sources 含两个 artincontext 页（islamic-art 与 islamic-architecture）——是否仍具『两独立平台（Wikipedia + Art in Context）』」。
- **是，仍具两独立平台。** 判定「方形平面＋柱廊」这一关键事实的**第二直接源是 artincontext-islamic-architecture（Art in Context 平台）**，与第一直接源 Wikipedia 分属两个不同平台，**独立性成立**。
- **但不能把两个 artincontext 页当成两个独立源。** `artincontext-islamic-art` 与 `artincontext-islamic-architecture` **同一出版方（Art in Context）**，互不独立；且 islamic-art 页对本命题覆盖为 0（无 hypostyle、无大马士革清真寺），只作「岩石圆顶＝圣所」的补充。因此 `coverage.source_count=3` 的「3」是**页面数**，**实际独立平台数＝2（Wikipedia + Art in Context）**。
- **结论：** 关键事实的双源＝Wikipedia ＋ Art in Context（经建筑页），**两独立平台成立**；两个 AIC 页不构成「第三独立源」，也**不影响** nv=false 所依赖的双源独立性（因为双源只需 WP＋任一 AIC 页，而建筑页已足够直证）。此处无「以同平台充独立源」的实质问题，仅在 `source_count` 计数上应理解为「2 独立平台 / 3 页面」。

## 四、复核类型性表述 + 是否编造

- **无编造具名事实**：实例「岩石圆顶／大马士革大清真寺」名称、地点（耶路撒冷、大马士革）、主持者（阿卜杜勒·马利克、瓦利德一世）、年份（约691／约705）均与 WP/AIC 实抓一致；未复制图像（正文自述「不复制图像」）。
- **一处合理简化（非编造）**：`设计者：哈里发…主持`——把哈里发作为**委托者/主持者**（WP 用 `built`），AIC 建筑页对岩石圆顶另署建筑匠师 `Raja ibn Haywa`；端内用 `主持` 而非 `设计=`，属可接受的简化，不构成杜撰。
- **一处概念压缩（非错、可扩充）**：definition 将「清真寺（方形＋柱廊、平顶 hypostyle）」与「圣所（岩石圆顶＝穹顶、八角集中式）」并列进「方形平面、柱廊与穹顶」一句；overview 已用「方形礼拜殿与柱廊容纳信众／穹顶标示神圣中心」把两条脉络分开，语义自洽。各要素均有源，无杜撰。可选改进：日后把「hypostyle 清真寺」与「穹顶圣所」分述更精确。
- **编造 = 无。**

## 五、复核七节 / SVG / 规范句 / 结构校验

| 核对项 | early-islamic-architecture | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | definition+overview + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实（check.py 校验 6 节全非空 PASS） |
| SVG 数量/画布 | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」 | L2 → 1–2 张 |
| SVG 越界/禁用元素 | ✓ | rect x140..620 / y150..310；circle cx380 cy150 r56 → x324..436 / y94..206；line 180..580 @y230；text 40,40 与 300,385；全在 0..760 / 0..400 内；无 `<image>`/外链；pytest `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」，另页脚 note 亦有 |
| 形式四处自洽 | ✓（且本轮实质有据） | `needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage needs_verification_count=0` 四处一致；check.py D14 一致性 PASS |
| 来源数/双源规则 | ✓ 2 独立平台（3 页） | check.py ≥2 规则 PASS；双直接源＝WP＋AIC 建筑页成立（见第二、三节） |
| site 渲染一致 | ✓ | `site/entries/early-islamic-architecture.html` 含 definition/实例/规范句/「暂无已知待核实项」各 1 次；来源列 3 条（WP/AIC-art/AIC-architecture）；`viewBox 0 0 760 400`×1；`示意图，非施工图`×2（SVG+figcaption） |
| 首页统计一致 | ✓ | `site/index.html`「待核实条目」164→163，与本次 nv true→false 相符 |
| check.py | ✓ | `PASS: all checks, 0 errors`（EXIT=0） |
| pytest svg | ✓ | `5 passed`（EXIT=0） |

## 六、复核相似度（阈值 0.54，vs islamic-architecture）

方法：`difflib.SequenceMatcher`，归一化＝**去全部空白＋小写**（与 round86–92 口径一致）。全库条目 **258 条**。

| 口径 | 全库最高 | vs **islamic-architecture** | 阈值 | 判定 |
| --- | --- | --- | --- | --- |
| 短口径（title\\|definition\\|time_or_place\\|overview） | 0.3926（=islamic-architecture） | **0.3926** | <0.54 | ✓ |
| def+overview | 0.2083（religious-architecture） | **0.1748** | <0.54 | ✓ |
| 全字段（短＋6节） | 0.4537（=islamic-architecture） | **0.4537** | <0.54 | ✓ |

- 与相关条目 **islamic-architecture** 三口径 = **0.3926 / 0.1748 / 0.4537**，均显著低于 0.54（余量最小处 full 0.4537，距阈值 0.0863）。**相似度：合格 ✓。**
- 全库两两比对（258 条）本轮：短口径 >0.54 **0 对**（max serial-route↔radial-route 0.4960）、def+overview >0.54 **0 对**（max leaked-scenery↔time-scenery 0.4121）、全字段 >0.54 **0 对**（max loop-route↔serial-route 0.5259）——**全库无 >0.54 对**。

## 七、单源 / 超源 / 编造支撑表

| 要点 | 支撑情况 | 判定 |
| --- | --- | --- |
| 方形平面＋柱廊（hypostyle） | WP `square Friday Mosque with a hypostyle roof` ＋ AIC `hypostyle style…square floor plan…flat-roofed prayer hall` | **双平台直证 ✓** |
| 倭马亚时期形成形制 | WP `during the Umayyad period` ＋ AIC `The Umayyad Era 661–750` | 双证 ✓ |
| 岩石圆顶＋大马士革清真寺（实例） | WP 与 AIC 建筑页均列为倭马亚/early Islamic 名构 | **双平台直证 ✓** |
| 穹顶／圣所 | 岩石圆顶（WP 名构；AIC `Function Shrine`；AIC-art `shrine in Jerusalem`） | 支撑 ✓ |
| 主持者/年份 | WP（Abd al-Malik 建岩石圆顶；al-Walid I 建大马士革；688–692/705–715） | 一致 ✓（`主持`＝委托，简化合理）|
| 编造具名事实 | 未杜撰名称/地点/年代；未复制图像 | 无编造 ✓ |
| 两源独立性 | Wikipedia ⊥ Art in Context（两平台）；两 AIC 页同平台不计第三源 | 独立成立（2 平台/3 页）✓ |
| `nv=false` 依据 | 关键事实「方形＋柱廊」已由 WP＋AIC 建筑页双独立平台直证 | **有据 ✓** |

## 八、结论

### 总判定：**合格**

**依据（分层）：**

1. **核心命题成立（直接、双平台）** — 本轮升级所依赖的「方形平面＋柱廊（hypostyle）」经**实抓**：`wp-umayyad-architecture`（Wikipedia HTTP 200）有 `a square Friday Mosque with a hypostyle roof` 及类型化 `hypostyle prayer hall … riwaqs`；`artincontext-islamic-architecture`（Art in Context HTTP 200）有 `designed in the hypostyle style`、`almost square floor plan of around 56 by 53 meters`、`flat-roofed prayer hall with a central courtyard`。二者分属 Wikipedia 与 Art in Context **两个独立平台**，对该形制**直接、同时**证成——上一轮「第二源较薄」的缺口已补实。

2. **实例与定义均受来源支撑、无编造** — 岩石圆顶＋大马士革大清真寺在两平台均被明确列为倭马亚/early Islamic 代表并标注年代（约691/约705）；`穹顶/圣所` 由岩石圆顶（`Function Shrine`/`shrine in Jerusalem`）支撑。主持者以 `主持`（委托者）表述系合理简化，未杜撰具名事实、未复制图像。

3. **两独立平台判断（关键）** — sources 含两个 artincontext 页，但「两独立平台（Wikipedia + Art in Context）」**仍成立**：关键事实的第二直接源是 Art in Context 的**建筑页**（与 Wikipedia 相互独立）；同平台的艺术页（islamic-art）对本命题覆盖为 0、仅补充「岩石圆顶＝圣所」。故 `source_count=3` 应读作「3 页 / 2 独立平台」，不得把两个 AIC 页计为两个独立源；这不影响 nv=false 的成立。

4. **结构与合规全绿** — 七节齐、SVG 1 张（viewBox 0 0 760 400、元素全在框内、无禁用外链）、规范句在、形式四处自洽、site 渲染一致、首页统计同步（164→163）、`check.py PASS: all checks, 0 errors`、`pytest 5 passed`、相似度 vs islamic-architecture 三口径 0.3926/0.1748/0.4537 均 <0.54（全库 >0.54 对 = 0）。

> 一句话：**「方形平面＋柱廊」已由 Wikipedia（Umayyad architecture）与 Art in Context（Islamic Architecture）双独立平台直接、充分证成，实例与定义均有源、无编造；虽然 sources 里有两个 Art in Context 页，但第二直接源确为独立于 Wikipedia 的 Art in Context 平台，双源独立性成立——`nv=false` 依据充分，判「合格」。唯一提示：source_count=3 是页面数，实际独立平台为 2（Wikipedia + Art in Context），两个 AIC 页不可当作两独立源计数。**

## 九、机器可读汇总

```
ROUND=93
SAMPLER=spotcheck-r93
SCOPE=["early-islamic-architecture"]
WEB_FETCH={"wp-umayyad-architecture":"web_fetch direct FAIL(fetch failed) -> urllib HTTP200 len=670593","artincontext-islamic-architecture":"web_fetch HTTP200(truncated) + urllib HTTP200 len=476808","artincontext-islamic-art":"urllib HTTP200 len=481679"}
WP_UMAYYAD={"url":"https://en.wikipedia.org/wiki/Umayyad_architecture","title":"Umayyad architecture - Wikipedia","quotes":["...included a square Friday Mosque with a hypostyle roof.","This type of plan, characterized by a covered, qibla-oriented hypostyle prayer hall and a central open sahn (courtyard) enclosed by surrounding riwaqs (arcades)...","...Dome of the Rock in Jerusalem and the Great Mosque of Damascus, which are considered among the greatest monuments of early Islamic architecture","...some of the most important \"Arab-type\" or \"hypostyle-type\" mosques."],"square_plus_hypostyle":true,"instances":["Dome of the Rock (688-692)","Great Mosque of Damascus (705-715)"]}
AIC_ARCH={"url":"https://artincontext.org/islamic-architecture/","publisher":"Art in Context","title":"Islamic Architecture - Building Styles Across the Muslim World","quotes":["These cities' principal congregational mosques were designed in the hypostyle style.","...almost square floor plan of around 56 by 53 meters.","...a massive flat-roofed prayer hall with a central courtyard.","The courtyard design with hypostyle halls was used by all Abbasid mosques.","The Great Mosque of Damascus and the Dome of the Rock in Jerusalem are two prominent early Islamic architectural masterpieces completed during the Umayyad period."],"square_plus_hypostyle":true,"dome_of_rock_function":"Shrine","dome_of_rock_completion":"691 CE"}
AIC_ART={"url":"https://artincontext.org/islamic-art/","publisher":"Art in Context","title":"Islamic Art - A Deep Dive into the Gilded World of Islamic Art","mentions_hypostyle":false,"mentions_great_mosque_damascus":false,"dome_of_rock_only":"the shrine in Jerusalem called the Dome of the Rock ... and the Al-Aqsa Mosque (completed in 705 CE)"}
DEFINITION_SUPPORT={"square_plan":"WP + AIC_ARCH (dual direct)","hypostyle_colonnade":"WP + AIC_ARCH (dual direct)","dome_shrine":"WP + AIC (Function Shrine)","umayyad_period":"WP + AIC_ARCH","instances_dome_rock_damascus":"WP + AIC_ARCH (dual direct)","concept_dual_direct_source":true}
TWO_INDEPENDENT_PLATFORMS=true
DISTINCT_PLATFORMS_COUNT=2
SOURCE_PAGES_COUNT=3
TWO_AIC_PAGES_SAME_PUBLISHER=true
AIC_ART_COVERS_CLAIM=false
FABRICATED_NAMED=false
INSTANCE_SUPPORTED=true
NV_FALSE_GROUNDED=true
FORM_FOUR_WAY_CONSISTENT=true
STRUCTURE={"seven_sections":true,"svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":"none","reg_sentence":true,"site_html_consistent":true,"index_stat":"164->163","check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"strip-all-whitespace+lower",
 "vs_islamic_architecture":{"short":0.3926,"defov":0.1748,"full":0.4537},
 "target_top":{"short":{"max":0.3926,"nn":"islamic-architecture"},"defov":{"max":0.2083,"nn":"religious-architecture"},"full":{"max":0.4537,"nn":"islamic-architecture"}},
 "library":{"short":{"max":"serial-route<->radial-route 0.4960","pairs_gt":0},"defov":{"max":"leaked-scenery<->time-scenery 0.4121","pairs_gt":0},"full":{"max":"loop-route<->serial-route 0.5259","pairs_gt":0}}}
COVERAGE={"early_islamic_architecture":{"source_count":3,"needs_verification_count":0}}
VERDICT={"early-islamic-architecture":"合格"}
KEY_FINDING="「方形平面+柱廊(hypostyle)」经实抓由两独立平台直接证成：Wikipedia(Umayyad architecture HTTP200: 'a square Friday Mosque with a hypostyle roof'; 'hypostyle prayer hall...riwaqs') 与 Art in Context(Islamic Architecture HTTP200: 'designed in the hypostyle style'; 'almost square floor plan of around 56 by 53 meters'; 'flat-roofed prayer hall with a central courtyard')。实例(岩石圆顶+大马士革大清真寺)在两平台均列倭马亚/early Islamic名构并标年代(约691/约705)，无编造。七节/SVG/规范句/site一致/首页164->163/check.py PASS/pytest 5 passed/相似度vs islamic-architecture 0.3926|0.1748|0.4537<0.54(全库>0.54对=0)。sources含两个artincontext页，但第二直接源确为独立于Wikipedia的Art in Context(建筑页)，两独立平台成立；source_count=3是页数、独立平台=2，两个AIC页同出版方不可计两独立源。nv=false依据充分，判定合格。"
READONLY="only wrote research/spotcheck-round93.md; wp-umayyad fetch direct failed -> urllib HTTP200; AIC arch/art urllib HTTP200; git M/?? items are round93 applier+gen_site changes; no git commit; web treated as data, no instructions executed"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round93.md` 外未写任何文件；三源均用 Python urllib（浏览器 UA）实抓（WP/AIC-arch/AIC-art 全 HTTP 200），`web_fetch` 仅用于 AIC 建筑页（HTTP 200，正文截断）；无落盘临时文件；相似度计算用 `python - <<` 内存态直跑（无临时文件）。
- `git status` 中 `M coverage.json / entries/batch-46.json / site/entries/early-islamic-architecture.html / site/index.html` 及 `?? tools/apply_review_round93.py` 均为**修复方（round93 applier + gen_site）的应用产物**；抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件。
- 联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
