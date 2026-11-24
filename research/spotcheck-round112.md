# 第112轮质量抽检（spotcheck-round112）——`garden-architecture`（园林建筑）双平台（含 DB `Pavilion` 之 Garden pavilion 专节）支撑核查

- 抽检人：spotcheck-r112b（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（现抓、现跑、后断言；证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 抽检对象：`garden-architecture`（园林建筑）——`entries/batch-35.json` L160 起；宣称本轮升级 `nv=false`（needs_verification=false、pending_notes 清空）。sources = `wp-chinese-garden` / `wp-garden-design` / `db-pavilion`（3 条，含 DB 非维基）；coverage：status 已写 / source_count 3 / needs_verification_count 0 / level L2 / last_updated 2026-11-24（已实读）。
- 本轮变更集（`git status --short` 实读：`M coverage.json / M data/sources.json / M entries/batch-35.json / M site/entries/garden-architecture.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round112.py`）——**均为 round112 修复方产物，抽检方仅读取、未据以修改**。对照 `tools/apply_review_round112.py`（实读）确认本轮动作：向 `data/sources.json` 追加 `db-pavilion`，给 `garden-architecture` 追加 `db-pavilion` 源、改写 definition/原理/实例、`needs_verification` true→false、`待核实`→「暂无已知待核实项。」、`pending_notes` 清空。
  - 定义：`园林建筑指园林中的亭、榭、廊等小型建筑。` → `园林建筑指园林中供观景、休憩与点景的亭、榭、廊等小型建筑。`
  - 原理：`亭榭等园林建筑置于景观点上，兼作景点与观景处。` → `亭榭等园林建筑置于景观点上，可开放或半开放、供遮荫休憩，既自成景又供观景，串联游线与视线。`
  - 实例：改为 `名称：临水亭榭（类型性，不指定具体项目）；置于水岸景观点，兼作景点与观景处。此处仅列说明，不复制图像。`
- 任务点名要特别判断的非维基源 `db-pavilion`（`/wiki/Pavilion`）——是否**真含「garden pavilion」专述**（有独立 Garden pavilion 节、原句述「可开放、供 shelter、ornamental/delicate、Chinese parks and gardens 供遮荫休憩」），还是**仅泛述 pavilion**。结论见 1.3 ★。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round112.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词频、相似度、去重、结构、SVG、site 一致性均内存态（`python - <<'PY'` / 工具直读）跑，未落盘临时文件（除本报告）。
- `git status --short` 本轮实读：`M coverage.json / M data/sources.json / M entries/batch-35.json / M site/entries/garden-architecture.html / M site/index.html / M site/sources.html / ?? tools/apply_review_round112.py`——**均为 round112 修复方产物，抽检方仅读取、未据以修改**；抽检方唯一新增为本报告。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `wp-chinese-garden`（`https://en.wikipedia.org/wiki/Chinese_garden`）→ `python urllib`（浏览器 UA、SSL 免检）**实抓 HTTP 200**，`<title>=Chinese garden - Wikipedia`，rawlen=490958，正文 textlen=83282。关键词计数：**pavilion=64 / garden pavilion=1 / shelter=1 / ornamental=2 / delicate=1 / rest=13 / view=59**。
  - `wp-garden-design`（`https://en.wikipedia.org/wiki/Garden_design`）→ **实抓 HTTP 200**，`<title>=Garden design - Wikipedia`，rawlen=320777，textlen=40847。关键词计数：**pavilion=1 / shelter=2 / ornamental=3 / rest=11 / view=6**——`Pavilion` **仅出现在 formal garden 特征名词列表**（Avenue…Orangery…Pavilion…Pergola…Trellis），**无 garden pavilion 专述**，属泛论性第三源。
  - `db-pavilion`（`https://www.designingbuildings.co.uk/wiki/Pavilion`）→ **实抓 HTTP 200**，`<title>=Pavilion - Designing Buildings`（Main author: Heidi Schwartz，页内 `Last edited 30 Dec 2021`），rawlen=56221，textlen=6530。关键词计数：**pavilion=36 / garden pavilion=4 / open sided=1 / shelter=1 / ornamental=1 / delicate=1 / gazebo=3 / rest=2 / view=1**；目录含独立节 **「3 Garden pavilion」**。逐句见 1.2 / 1.3。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests -q -p no:cacheprovider`：`19 passed in 0.67s`（PYTEST_EXIT=0）**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存/未落盘）。
- 相似度方法承前轮：`difflib.SequenceMatcher`，去全部空白（NFKC 归一）+小写；口径①短=title+definition+time_or_place+overview；口径②全=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style × expressionism-style` 口径②=0.5157（与 r108/r109/r110 逐位一致，方法正确）。全库 258 条，无重复 id。**

---

## 一、`garden-architecture`（园林建筑）

### 1.1 当前 entry 实读（`entries/batch-35.json` L160 起）
- `definition`＝「园林建筑指园林中供观景、休憩与点景的亭、榭、廊等小型建筑。」
- `原理`＝「亭榭等园林建筑置于景观点上，可开放或半开放、供遮荫休憩，既自成景又供观景，串联游线与视线。」
- `典型手法与适用条件`＝「依景设亭、临水建榭，控制体量与样式以融于自然。」
- `overview`＝「园林建筑既是景点也是观景点，组织游线与视线。」
- `实例`＝「名称：临水亭榭（类型性，不指定具体项目）；置于水岸景观点，兼作景点与观景处。此处仅列说明，不复制图像。」
- `常见错误与限制`＝「体量过大将压景；需与山水协调。实际工程须按当地规范和专业设计人员的要求」（**句末缺「。」**）
- sources = wp-chinese-garden / wp-garden-design / db-pavilion；`needs_verification=false`、`pending_notes=""`、`待核实=暂无已知待核实项。`、`time_or_place=古代、中国（参见来源）。`、`related=[]`。level L2 / tier 重要 / theme 造景 / period 古代 / region 中国。

### 1.2 definition/原理 两平台核对（实抓引句）
概念拆解：①对象＝**园林中的小型建筑（亭、榭、廊等）**；②功能＝**供观景、休憩（遮荫）与点景**；③形态＝**可开放/半开放**；④作用＝**自成景又供观景、串联游线与视线**。

**wp-chinese-garden（Wikipedia；en 直连 HTTP200，`<title>=Chinese garden`）——①②③④直证：**
- 建筑类型含亭/榭/廊（①）：实抓句「Chinese gardens are filled with architecture; **halls, pavilions, temples, galleries, bridges, kiosks, and towers**, occupying a large part of the space.」；「In addition to these larger halls and pavilions, the garden is filled with **smaller pavilions (also called ting)**…」；「**Galleries (lang) are narrow covered corridors** which connect the buildings…」；「…**lakes and waterside pavilions**…」——亭(ting)/榭(waterside pavilions)/廊(lang/galleries)齐备。
- 休憩、遮荫（②）：「…which are designed for **providing shelter from the sun or rain**, for contemplating a scene, reciting a poem, taking advantage of a breeze, or **simply resting**.」
- 观景、点景（②④）：「The Humble Administrator's Garden… **eighteen pavilions for viewing different features of the garden**…」；「They are sometimes… **stood by themselves at view points of the garden**, by a pond or at the top of a hill.」；「pavilions surround the lake **to see it from different points of view**」；「a special pavilion for viewing them」。
- 可开放/半开放（③）：「This building has **folding or movable walls, for opening up a panoramic view** of the garden.」
- 串联游线与视线（④）：「By moving from structure to structure, visitors can view a series of carefully composed scenes…」；galleries「connect the buildings… help divide the garden into different sections」。
- 结论：该源对「园林亭榭廊等小型建筑 + 观景休憩点景 + 可开放 + 串联游线视线」**均有直证**。

**db-pavilion（Designing Buildings；`/wiki/Pavilion`，HTTP200，`<title>=Pavilion - Designing Buildings`，Last edited 30 Dec 2021）——独立「Garden pavilion」节直证②③、并涉中国园林亭榭：**
- 独立节「**3 Garden pavilion**」逐句：「**A garden or park pavilion may be open sided and used to provide shelter** for exhibitions, restaurants, lectures, sports facilities and so on. In this instance, a pavilion is akin to a bandstand, gazebo, kiosk, poolhouse or summerhouse and **often includes seating**. **Some garden pavilions can be ornamental or delicate structures.**」——直证「可开放（open sided）」「供 shelter（休憩/遮荫/庇护）」「装饰性点景（ornamental/delicate）」。
- 「Pavilions of the world」节涉中国园林亭榭：「…**They are frequently featured in Chinese parks and gardens, where they provide shade and a place to rest.**」——直证「园林亭榭 + 遮荫 + 休憩」。
- 结论：该源既有 **独立「Garden pavilion」专节**（原句支撑开放/shelter/ornamental），又述 **Chinese parks and gardens 供遮荫休憩**——**园林亭榭直证第二平台**。

**wp-garden-design（Wikipedia；HTTP200）——泛论/列表性，无 garden pavilion 专述：**
- `pavilion` 仅 1 次，且出现在 formal garden 特征名词串「…Orangery Parterre **Pavilion** Pergola Reflecting pool Sylvan theater Terrace Topiary Trellis」中，**仅把 Pavilion 列为园林特征之一，无定义/功能专述**。属泛论性第三源（与 r110 `wp-architectural-style` 性质相同）。

| 概念要素 | wp-chinese-garden | db-pavilion（非维基） | wp-garden-design | 判定 |
| --- | --- | --- | --- | --- |
| ① 园林小型建筑（亭/榭/廊） | ✓ halls/pavilions/galleries/kiosks；ting；waterside pavilions；galleries(lang) | ✓ Garden pavilion 节；Chinese parks and gardens | △ 仅列表列 Pavilion | **成立（wp 直证，DB 佐证）** |
| ② 供观景/休憩/点景 | ✓「shelter from sun or rain…simply resting」「pavilions for viewing」「observation/view points」 | ✓「provide shelter…seating」「ornamental or delicate」「shade and a place to rest」 | ✗ | **成立** |
| ③ 可开放/半开放 | ✓「folding or movable walls, for opening up a panoramic view」 | ✓「may be open sided」 | ✗ | **成立** |
| ④ 自成景/供观景、串联游线视线 | ✓「moving from structure to structure…composed scenes」；galleries connect | △（偏 shelter/ornamental，未逐条述游线） | ✗ | **成立（wp 直证，DB 佐证）** |

**判定（1.2）：definition/原理 获「两独立平台」直证。** 两平台＝Wikipedia `Chinese garden`（①②③④直证）与 DB `Pavilion`（②③专节直证、①佐证）。四项概念要素**均至少两平台成立**（②核心观景/shelter、③开放由 wp+DB 双证）。`wp-garden-design` 为泛论/列表性第三源、不专述 garden pavilion，但两平台直证已由前两者满足。

### 1.3 ★特别判断：`db-pavilion` 是否真含 "garden pavilion" 专述（非仅泛述 pavilion）
**结论：是。DB 页确有独立「Garden pavilion」专节，逐句直述「可开放 + 供 shelter + 常含座椅 + ornamental/delicate」，并另述「Chinese parks and gardens 供遮荫与休憩」，非仅泛述 pavilion。**
- **专节存在**：页面目录「1 Introduction / 2 Tent pavilion / **3 Garden pavilion** / 4 Structural pavilions / 5 Pavilions of the world / 6 Related articles」，第 3 节为**独立成节**，非附注一句。
- **专节原句直证**：「**A garden or park pavilion may be open sided and used to provide shelter** for exhibitions, restaurants, lectures, sports facilities and so on. In this instance, a pavilion is akin to a bandstand, gazebo, kiosk, poolhouse or summerhouse and **often includes seating**. **Some garden pavilions can be ornamental or delicate structures.**」
  - 开放＝**may be open sided**（可开放）✓；
  - 功能＝**provide shelter / includes seating**（供休憩/遮荫）✓；
  - 点景＝**ornamental or delicate structures**（装饰/精巧点景）✓。
- **中国园林语境直证**：「Pavilions of the world」节：「…Pavilions…**frequently featured in Chinese parks and gardens, where they provide shade and a place to rest.**」——直接落到「园林（Chinese parks and gardens）+ 亭（pavilion）+ 遮荫 + 休憩」。
- **与「仅泛述 pavilion」区分**：DB 页 `Introduction` 泛述 pavilion 为「lightweight, festive…enclosures such as tent pavilions, garden pavilions and art pavilions」；但第 3 节是**专门讲 garden pavilion**（开放/shelter/ornamental），第 5 节又落到中国园林亭榭。故该源**同时**支撑「园林亭榭是小型建筑、可开放、供休憩」与「装饰性点景」——**正是本条定义/原理所需，非仅一词泛述**。
- **对照 r109/r110 反例**：r109 的 `db-traffic`/`db-pedestrian` 只是术语定义（泛述交通/行人）无流线直证；本页 `db-pavilion` 有**独立 Garden pavilion 节原句 + 中国园林亭榭句**，性质不同，**构成真第二平台直证**。
- **附（源数据极小疵，可忽略）**：sources.json 标题记「Pavilion — Designing Buildings」，实页 `<title>=Pavilion - Designing Buildings`（em-dash vs hyphen 差异），标题实质一致；`note` 所述「园林/公园亭榭：可开放、供遮荫休憩与装饰性点景的建筑」与实页**逐项相符**；`year=null` 符合 D06（动态页面、页内 Last edited 30 Dec 2021）。

### 1.4 是否编造
- definition/原理**均可逐句溯源、非杜撰**：①亭榭廊小型建筑←wp「halls, pavilions…galleries, kiosks」「smaller pavilions (ting)」「Galleries (lang)」「waterside pavilions」/DB「Garden pavilion」「Chinese parks and gardens」；②观景休憩点景←wp「shelter from sun or rain…simply resting」「pavilions for viewing」「view points」/DB「provide shelter…seating」「ornamental or delicate」「shade and a place to rest」；③可开放/半开放←wp「folding or movable walls, for opening up a panoramic view」/DB「may be open sided」；④自成景供观景/串联游线←wp「moving from structure to structure…composed scenes」「galleries connect」。**结论：非编造，可溯源。**
- `常见错误与限制`「体量过大将压景；需与山水协调」属通行造园专业常识性提示（非历史事实主张），后接规范句，按 D09 处理妥当，不构成未证事实。

### 1.5 类型性实例合理性
- 实例为「临水亭榭（类型性，不指定具体项目）；置于水岸景观点，兼作景点与观景处。此处仅列说明，不复制图像。」——**类型性实例合理，不依赖未核的具体项目/设计者/年代，无未核事实风险、无侵权**。✓
- 与本条概念自洽（临水亭榭＝wp「waterside pavilions」「pavilions over the water for viewing」；兼作景点与观景处＝wp「pavilions for viewing … different points of view」）。

### 1.6 nv=false 形式
| 项 | 值 | 判定 |
| --- | --- | --- |
| entry.needs_verification | false | 形式 ✓ |
| entry.pending_notes | "" | 形式 ✓ |
| sections.待核实 | 「暂无已知待核实项。」 | 形式 ✓ |
| coverage.needs_verification_count | 0（status 已写 / source_count 3 / L2 / 2026-11-24） | 形式 ✓ |
| time_or_place | 「古代、中国（参见来源）。」无「待核实」 | 形式 ✓ |
- **形式五处一致 ✓，check.py PASS；且内容前提（两独立平台直证概念，见 1.2/1.3）成立 → nv=false 实质成立。**

### 1.7 七节 / SVG / 规范句 / site
| 核对项 | 值 | 判定 |
| --- | --- | --- |
| 七节（definition+原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实） | sections 6 节齐备且非空 + definition，共七节 | ✓ |
| SVG 数量 / viewBox | 1 张，`0 0 760 400` | ✓ |
| SVG 越界 | check.py `validate_svg` 通过（PASS 0 errors）；逐元素（rect x80 y90 w600 h230→右680 底320；circle cx240 cy200 r34；path M360,260 Q460,160 600,250；text x300 y375；text x40 y40）均落框内（坐标数值 min0/max600、y max375） | ✓ |
| SVG 外链 | 无 `<image>/<script>/<iframe>/href=/url(`（forbidden=[]；除 xmlns 命名空间外无 http） | ✓ |
| SVG 注记 | 含「示意图，非施工图」 | ✓ |
| 规范句 | 「实际工程须按当地规范和专业设计人员的要求」在，**entry 句末缺「。」**（`常见错误与限制` 以「要求」收尾；site 页脚 note 处带「。」）——同 r101–r110 T 小疵 | ✓（T 小疵） |
| site 与 JSON 一致 | `site/entries/garden-architecture.html`：title/definition/overview(lead)/time_or_place/原理/典型手法/实例/常见错误/一图/待核实 逐句 `in html=True`；JSON `<svg>` 串 `in html=True`；源三行（Chinese garden / Garden design / Pavilion — Designing Buildings）一致 | ✓ |
| site/sources.html | `db-pavilion` 行在：`<a href=".../wiki/Pavilion">Pavilion — Designing Buildings</a>` / Designing Buildings / 学术著作 / 动态·未标注 / 已核验 / 可达 / note 与实页相符 | ✓ |

### 1.8 相似度（阈值 0.54）与 def≠原理
| 条目 | 口径 | 最近邻 | 相似度 | 判定 |
| --- | --- | --- | --- | --- |
| garden-architecture | 短① | imperial-architecture | 0.4426 | ✓ <0.54 |
| garden-architecture | 全② | wind-driven-ventilation | 0.3505 | ✓ <0.54 |
| garden-architecture × imperial-architecture（短① Top5） | — | imperial-architecture 0.4426 / religious-architecture 0.3667 / xu-shi 0.3333 / lingnan-style 0.3333 / hokkien-style 0.3307 | 均 <0.54 | ✓ 非重复条目 |
| def×原理（去重） | — | — | 0.2432 | ✓ 两层次可分 |
- 全库最大：短 0.4960（serial-route×radial-route）、全 0.5256（spatial-sequence×atrium-architecture）——**均 <0.54 ✓**；方法自校 0.5157 ✓；258 条无重复 id。**相似度非本条问题。**

### 1.9 条目结论
**`garden-architecture`（园林建筑）——合格（本轮 nv=false 升级成立）。**
- 依据：definition/原理四项要素（①园林小型建筑亭/榭/廊 ②供观景/休憩/点景 ③可开放/半开放 ④自成景供观景、串联游线视线）**获「Wikipedia Chinese garden + DB Pavilion」两独立平台直证**——★特别判断 `db-pavilion`（`/wiki/Pavilion`，HTTP200）**有独立「3 Garden pavilion」专节**，原句「A garden or park pavilion **may be open sided** and used to **provide shelter**…often includes seating. **Some garden pavilions can be ornamental or delicate structures**」直证「开放/shelter/装饰点景」，并「Pavilions of the world」述「frequently featured in **Chinese parks and gardens**, where they provide **shade and a place to rest**」直证园林亭榭；`wp-chinese-garden` 以「halls, pavilions…galleries, kiosks」「smaller pavilions (ting)…shelter from sun or rain…simply resting」「eighteen pavilions for viewing…」「view points」「folding or movable walls, for opening up a panoramic view」「Galleries (lang)…connect the buildings」直证亭/榭/廊、观景/休憩/点景与可开放。**「两平台（含 DB 非维基）支撑」前提成立 → nv=false 实质成立；definition/原理非编造、可逐句溯源。**
- 通过项：类型性实例合理；七节 / SVG（无越界、无外链、含示意图注记）/ site 与 JSON 一致、sources.html 含 db-pavilion；相似度短 0.4426、全 0.3505、def×原理 0.2432 均 <0.54；check.py PASS、pytest 19 passed、方法自校 0.5157；258 条 0 重复 id；全库最大短 0.4960 / 全 0.5256 均 <0.54。
- **T（Minor）**：①`常见错误与限制` 规范句句末缺「。」；②（透明性）`wp-garden-design` 为泛论/列表性第三源（仅把 Pavilion 列为 formal garden 特征之一）、不专述 garden pavilion——本条两平台直证实际由 `wp-chinese-garden` + `db-pavilion` 满足，`wp-garden-design` 属补充性泛源（不影响 nv=false 成立）；③sources.json `db-pavilion` 标题破折号为「—」、实页为「-」（em-dash vs hyphen），实质一致，可忽略；④SVG 为通用示意图模板（矩形+圆+曲线+标注），示意性合格但非专属园林建筑图形（符合“示意图非施工图”口径，非缺陷）。
- **处置建议**：维持 `needs_verification=false`；如追求零瑕疵，可在下一轮统一补 `常见错误与限制` 规范句句末「。」（历史遗留 T 小疵，非本条特有）。

---

## 二、机器可读汇总

```
ROUND=112
SAMPLER=spotcheck-r112b
SCOPE=["garden-architecture"]
READONLY="only wrote research/spotcheck-round112.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "wp-chinese-garden":"en.wikipedia 200 '<title>=Chinese garden - Wikipedia' rawlen=490958 textlen=83282; counts: pavilion=64 garden pavilion=1 shelter=1 ornamental=2 delicate=1 rest=13 view=59; quotes: 'halls, pavilions, temples, galleries, bridges, kiosks, and towers'; 'smaller pavilions (also called ting)... providing shelter from the sun or rain... simply resting'; 'eighteen pavilions for viewing different features of the garden'; 'stood by themselves at view points of the garden'; 'folding or movable walls, for opening up a panoramic view of the garden'; 'Galleries (lang) are narrow covered corridors which connect the buildings'; 'waterside pavilions'",
 "wp-garden-design":"en.wikipedia 200 '<title>=Garden design - Wikipedia' rawlen=320777 textlen=40847; pavilion=1 shelter=2 ornamental=3 rest=11 view=6; Pavilion only in formal-garden feature list (Orangery/Parterre/Pavilion/Pergola/...) -> NOT garden-pavilion-specific, generic third source",
 "db-pavilion":"designingbuildings 200 '<title>=Pavilion - Designing Buildings' Last edited 30 Dec 2021 rawlen=56221 textlen=6530; counts: pavilion=36 garden pavilion=4 open sided=1 shelter=1 ornamental=1 delicate=1 gazebo=3 rest=2 view=1; TOC has '3 Garden pavilion'; GARDEN-PAVILION SECTION QUOTE: 'A garden or park pavilion may be open sided and used to provide shelter for exhibitions, restaurants, lectures, sports facilities and so on. In this instance, a pavilion is akin to a bandstand, gazebo, kiosk, poolhouse or summerhouse and often includes seating. Some garden pavilions can be ornamental or delicate structures.'; 'Pavilions of the world': 'They are frequently featured in Chinese parks and gardens, where they provide shade and a place to rest.'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest":"19 passed (EXIT=0)"}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258,"dup_ids":0}
GLOBAL_MAX={"short":["serial-route","radial-route",0.4960],"full":["spatial-sequence","atrium-architecture",0.5256]}

GARDEN_ARCHITECTURE={
 "verdict":"合格(本轮nv=false升级成立)",
 "definition":"园林建筑指园林中供观景、休憩与点景的亭、榭、廊等小型建筑。",
 "principle":"亭榭等园林建筑置于景观点上，可开放或半开放、供遮荫休憩，既自成景又供观景，串联游线与视线。",
 "sources":["wp-chinese-garden","wp-garden-design","db-pavilion"],
 "concept_dual_source":{
   "garden_small_buildings_ting_xie_lang":"wp 'halls,pavilions...galleries,kiosks' + 'smaller pavilions (ting)' + 'Galleries (lang)' + 'waterside pavilions' / db 'Garden pavilion' section + 'Chinese parks and gardens' -> ESTABLISHED",
   "viewing_rest_scenic":"wp 'shelter from sun or rain...simply resting' + 'pavilions for viewing' + 'view points' / db 'provide shelter...seating' + 'ornamental or delicate' + 'shade and a place to rest' -> ESTABLISHED",
   "open_semi_open":"wp 'folding or movable walls, for opening up a panoramic view' / db 'may be open sided' -> ESTABLISHED",
   "scenic_view_route_sightline":"wp 'moving from structure to structure...composed scenes' + 'galleries connect' -> ESTABLISHED (db supportive)",
   "holds_two_platform_for_concept":true},
 "db_pavilion_garden_specific_vs_generic":"DIRECT (真支撑): DB /wiki/Pavilion has dedicated section '3 Garden pavilion' verbatim 'A garden or park pavilion may be open sided and used to provide shelter...often includes seating. Some garden pavilions can be ornamental or delicate structures.' plus 'Pavilions of the world': 'frequently featured in Chinese parks and gardens, where they provide shade and a place to rest' -> supports garden pavilion (open/shelter/ornamental/Chinese gardens), NOT merely generic pavilion; unlike r109 db-traffic/db-pedestrian generic term defs.",
 "fabrication":"NOT fabricated; definition/principle quote-traceable element-by-element to wp-chinese-garden + db-pavilion",
 "instance":"临水亭榭(类型性,不指定具体项目) -- reasonable type-level instance",
 "type_instance_ok":true,
 "nv_false_form":"five-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); substantive premise (two-platform direct support) TRUE -> nv=false valid",
 "structure":{"seven_sections":true,"sections_with_def":7,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"imperial-architecture 0.4426","nearest_full":"wind-driven-ventilation 0.3505","def_vs_principle":0.2432,"lt_0.54":true},
 "transparency":["T1: 常见错误与限制 规范句句末缺「。」","T2: wp-garden-design 为泛论/列表性第三源(仅列Pavilion为formal garden特征), 两平台直证实由 wp-chinese-garden + db-pavilion 满足","T3: sources.json db-pavilion 标题破折号 — vs 实页 - (实质一致, 可忽略)","T4: SVG为通用示意图模板, 示意性合格非专属图形"]}

VERDICT={"garden-architecture":"合格(nv=false 成立: definition/原理四要素 园林小型建筑亭/榭/廊 / 观景休憩点景 / 可开放半开放 / 自成景供观景串联游线 由 wp-chinese-garden(Chinese garden, Wikipedia) + db-pavilion(Pavilion, Designing Buildings 非维基) 两独立平台直证; ★db-pavilion 有独立'3 Garden pavilion'专节 原句'may be open sided...provide shelter...often includes seating...Some garden pavilions can be ornamental or delicate structures'直证开放/shelter/装饰点景 + 'Pavilions of the world' 'Chinese parks and gardens...shade and a place to rest'直证园林亭榭(非仅泛述pavilion); 非编造可溯源; 类型性实例临水亭榭合理; 七节/SVG无越界无外链含示意图注记/site与JSON一致/sources.html含db-pavilion; 相似度短0.4426全0.3505 def×原理0.2432 均<0.54; check.py PASS/pytest 19 passed/方法自校0.5157/258条0重复/全库最大短0.4960全0.5256<0.54. T小疵: 规范句句末缺句号; wp-garden-design为泛论第三源; db标题破折号差异; SVG通用模板)")
KEY_FINDING="garden-architecture 与 r109 vehicle-flow/pedestrian-flow 关键差异: 后者所加 DB 源(db-traffic/db-pedestrian)仅为相关名词术语定义(泛述交通/行人)无流线组织直证→不合格; 本条所加 db-pavilion 有独立'3 Garden pavilion'专节, 逐句直述'may be open sided...provide shelter...includes seating...ornamental or delicate'且'Pavilions of the world'述'Chinese parks and gardens...shade and a place to rest'(直证园林亭榭, 非仅泛述pavilion), 与 wp-chinese-garden(亭ting/榭waterside pavilions/廊galleries; pavilions for viewing/view points; folding or movable walls for panoramic view; shelter from sun or rain...simply resting)构成两独立平台直证 -> '两平台(含DB非维基)支撑'前提成立, nv=false实质成立, 判合格. 仅规范句句末缺句号等 T 小疵."
```

## 三、只读核验
- 除本报告 `research/spotcheck-round112.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 抓取：`wp-chinese-garden`、`wp-garden-design` 经 `python urllib`（浏览器 UA、SSL 免检）实抓 en.wikipedia HTTP200（rawlen 490958 / 320777，textlen 83282 / 40847），逐标题与关键词计数核对；`db-pavilion`（`/wiki/Pavilion` 200，Last edited 30 Dec 2021）实抓全文逐句核对（含目录「3 Garden pavilion」节与「Pavilions of the world」中国园林句）。
- 词频、相似度、去重（258 条/0 重复）、结构、SVG 逐元素越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（en.wikipedia.org / designingbuildings.co.uk）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**（页面内导航/推荐/评论等均按数据忽略）。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存（19 passed）。
- `git status` 中的改动文件（coverage/sources/batch-35/site 三页/`?? tools/apply_review_round112.py`）均为**他方（round112 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
