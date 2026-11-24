# 第99轮质量抽检报告（spotcheck-round99）——damp-proofing / 防潮 的 nv=false 升级复核

- 抽检人：spotcheck-r99（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论；本会话为委派子代理，命中 `using-superpowers` 的 SUBAGENT-STOP，以任务说明书执行；`verification-before-completion` 全程遵循——本文所有“通过/合格”判断均附本轮实跑输出）。
- 抽检对象（1 条）：`damp-proofing`（防潮）——`entries/batch-02-c.json` 第206–236行（id 206；definition 213；time_or_place 214；overview 215；related 216–218；sources 219–223；needs_verification 224；pending 225；原理 227；典型手法 228；实例 229；常见错误 230；一图 231；待核实 232；SVG 235）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round99.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。抓取、词扫描、相似度、git 核对均在内存态 `python - <<'PY'` 直跑，未落盘临时文件。
- 本轮变更实读：`tools/apply_review_round99.py`（新增，未提交；51行）。其 `main()` 对 `damp-proofing` 做的改动为：
  - `sources` 追加 `db-damp-proofing`（→ 3 源：wp-building-material / wp-sunken-courtyard / db-damp-proofing）。
  - `definition`：「防潮是对墙体与地面施加的湿度控制构造措施，用以阻止上升潮、渗透潮等水分侵入。」
  - `sections.原理`：「以防水薄膜、表面涂层等阻隔层切断水分由地面或墙面渗入的路径，防止地下或近地空间受潮。」
  - `sections.实例`：「名称：地下空间防潮构造（类型性，不指定具体项目）；以防水薄膜与表面涂层阻断上升潮与渗透潮。此处仅列说明，不复制图像。」
  - `needs_verification`：`true`→`false`；`sections.待核实`：「暂无已知待核实项。」；`pending_notes`：`""`。
  - 新增 `sources.json` 记录 `db-damp-proofing`（url `https://www.designingbuildings.co.uk/wiki/Damp_proofing`，`verified=true`，`link_ok=true`，note「访问于 2026-11-24，实抓 HTTP 200；防潮指对墙与地面施加的湿度控制，防上升潮/渗透潮（薄膜、表面涂层等）」）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-damp-proofing = https://www.designingbuildings.co.uk/wiki/Damp_proofing` → `web_fetch` **HTTP 200**（重定向至 `Damp_proofing_buildings`，正文完整取回）。
  - `wp-building-material = https://en.wikipedia.org/wiki/Building_material` → `web_fetch` TypeError（fetch failed）→ Python urllib（浏览器 UA）**HTTP 200，raw≈381,579 bytes**，并完成词频/上下文扫描（见第一节）。后续复抓因网络对该站间歇超时（WinError 10060）；首次成功抓取已捕获唯一相关原句，证据充分。
  - `wp-sunken-courtyard = https://en.wikipedia.org/wiki/Sunken_courtyard` → Python urllib **HTTP 200，raw≈70,503 bytes**，完成词扫描（见第二节）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.11s`（EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）
- `git status --short`：仅 `M coverage.json / M data/sources.json / M entries/batch-02-c.json / M site/entries/damp-proofing.html / M site/index.html / M site/sources.html` 与 `?? tools/apply_review_round99.py`——均为本条第99轮修复方（applier＋gen_site）自身产物；抽检方仅读取，未据以修改。

## 一、★ 概念「对墙体与地面施加湿度控制、阻止上升潮/渗透潮」双平台核对（实抓引句）

- `db-damp-proofing`（Designing Buildings 建筑百科，CIOB/IHBC/CIAT 背书；HTTP200，正文实抓）：
  - `The term 'damp proofing' refers to types of moisture control that are applied to walls and floors to prevent damp from setting in or spreading in a building.`（**湿度控制施加于墙体与地面✓**）
  - `The most common causes of persistent damp in buildings are: Condensation (surface or interstitial). Rising damp. Penetrating damp.`（**上升潮 Rising damp / 渗透潮 Penetrating damp✓**；冷凝 Condensation✓）
  - `damp-proof course ... a barrier, usually formed by a membrane built into the walls ... 150 mm above ground level, to prevent damp rising through the walls.`（**薄膜 barrier 阻上升潮✓**）
  - `damp-proof membrane (DPM). Typically, a DPM is a polyethylene sheet laid under a concrete slab to prevent the concrete from transmitting moisture through capillary action.`（**防水薄膜/毛细作用✓**）
  - `Surface coating: Waterproof surface materials can be used internally or externally, such as render or waterproof plaster.`（**表面涂层✓**）
  - 其他：integral damp proofing、cavity wall、pressure grouting、colourless water-repellent treatments（构造手法佐证）。
- `wp-building-material`（Wikipedia `Building material`，HTTP200，raw≈381,579）：
  - 唯一相关原句：`There are a wide variety of damp proofing and waterproofing membranes used for roofing, basement waterproofing, and geomembranes.`（**防水/防潮薄膜 + 地下室（basement）防水✓**）
  - 词频实测：`damp`=3（仅上句实质性；另两处为 "Wet-laid, or damp, walls…" 的“潮湿黏土墙”无关用法、以及导航条 "Damp Proofing"）；`waterproof`=2（均在该句）；`basement`=1（该句）；`moisture`=3（均无关：植物颗粒 moisture buffering、吸湿调节、木材 moisture-related problems）。**不含** rising damp / penetrating damp / surface coating / 明确的“墙体地面湿度控制”表述。
- `wp-sunken-courtyard`（Wikipedia `Sunken courtyard`，HTTP200，raw≈70,503）：词频实测 `damp`=0、`waterproof`=0、`membrane`=0、`basement`=0、`moisture`=0、`proof`=0——**零覆盖防潮概念**（见第二节）。

| 概念要素 | wp-building-material（Wikipedia） | db-damp-proofing（Designing Buildings） | 判定 |
| --- | --- | --- | --- |
| 施加于墙体与地面的湿度控制 | 部分/隐含：`basement waterproofing`（地下墙体楼板语境） | ✓ 逐字：`moisture control ... applied to walls and floors` | db 直证；wp 隐含（地下/地下室） |
| 上升潮 Rising damp | ✗ 未出现 | ✓ `Rising damp`；`prevent damp rising through the walls` | **db 单源** |
| 渗透潮 Penetrating damp | ✗ 未出现 | ✓ `Penetrating damp` | **db 单源** |
| 防水薄膜 membrane | ✓ `damp proofing and waterproofing membranes ... basement waterproofing` | ✓ `damp-proof course ... membrane`；`damp-proof membrane (DPM)` | **双平台双源✓** |
| 表面涂层 surface coating | ✗ 未出现 | ✓ `Surface coating: Waterproof surface materials ... render or waterproof plaster` | **db 单源** |
| 地下/近地（basement）防水 | ✓ `basement waterproofing` | ✓ `walls and floors` / rising damp 语境 | **双平台双源✓** |
| 阻隔层切断渗入路径（barrier） | 隐含（waterproofing membranes） | ✓ 逐字：`a barrier ... to prevent damp rising`；`prevent ... transmitting moisture through capillary action` | 双源（wp 隐含＋db 直证） |

**判定：** definition「防潮是对墙体与地面施加的湿度控制构造措施，用以阻止上升潮、渗透潮等水分侵入」与 原理「以防水薄膜、表面涂层等阻隔层切断水分由地面或墙面渗入的路径，防止地下或近地空间受潮」——其**核心机制「以防水薄膜/阻隔层控制墙体地面湿度、防地下（basement）/近地受潮」由 Wikipedia（wp-building-material）＋ Designing Buildings（db-damp-proofing）两独立平台共同直证（wp 提供 membrane+basement 骨架，db 提供完整机理与术语）**，非编造、非超源。**须如实说明（不改变合格判定，但为关键透明项）：两平台为“互补式”共同支撑——`上升潮/渗透潮`、`表面涂层`、以及“墙体地面”逐字表述仅由 `db-damp-proofing` 单源承载，`wp-building-material` 并不独立复述这些具体术语；唯一真正“逐元素互证”的是 `薄膜 membrane` 与 `地下 basement` 两个要素。**

## 二、★ wp-sunken-courtyard 是否支撑防潮 + 两源独立性判定

- **wp-sunken-courtyard 不支持防潮（实测 0 命中）**：词扫描 `damp/waterproof/membrane/basement/moisture/proof` 全为 0。该源原为“下沉空间”主题的泛化条目，只提供「下沉空间」语境（本条 theme=下沉空间），**对防潮定义/原理/实例零支撑**。故本条**对防潮概念起作用的双平台实为 `wp-building-material` ＋ `db-damp-proofing`**（与任务书预判一致）。
- **两独立平台判定：成立 ✓**。`wp-building-material` 出版方为 **Wikipedia**（`type=权威百科`），`db-damp-proofing` 出版方为 **Designing Buildings**（`type=学术著作`；CIOB/IHBC/CIAT 机构背书的建筑行业百科）。二者为**不同组织、不同编辑体系、不同平台**，无派生/同源关系，构成两独立平台。
- 透明提示（Minor，不否决）：`wp-sunken-courtyard` 对防潮零覆盖，作为“来源”仅起主题语境作用；若日后统一收紧“来源须对核心概念有实质支撑”的口径，此源属可替换项（可换成权威 “Rising damp / Damp (structural)” 类专条以获得更强的逐元素互证）。当前不构成事实缺陷（双平台由 wp-building-material＋db 满足）。

## 三、★ 实例「类型性」核对与编造检查

- `实例`＝「名称：地下空间防潮构造（**类型性，不指定具体项目**）；以防水薄膜与表面涂层阻断上升潮与渗透潮。此处仅列说明，不复制图像。」
- **类型性合理**：以「地下空间防潮构造」这一**构造类别**作例，不绑定任何具体建筑；其内容「防水薄膜与表面涂层阻断上升潮与渗透潮」与 `db-damp-proofing` 的 `damp-proof membrane / surface coating / rising damp / penetrating damp` **逐项有源一致**。
- **无编造**：实例**未给出**任何具体项目名/地点/设计者/年份/数值，故不存在可编造的具体事实；「不复制图像」自述一致。
- 结论：实例**类型性、有源、不编造**，符合任务要求。

## 四、★ nv=false 是否落地 + 形式四处一致

| 核对项 | damp-proofing | 说明 |
| --- | --- | --- |
| `needs_verification`（entry） | `false` | 落地✓ |
| `pending_notes` | `""` | 空✓ |
| `sections.待核实` | 「暂无已知待核实项。」 | ✓ |
| `coverage.json` 该记录 | `status: 已写`、`source_count: 3`、`needs_verification_count: 0`、`last_updated: 2026-11-24` | ✓ |
| `time_or_place`="20世纪、全球（参见来源）。" | 无「待核实」字样 | ✓ |

四字段（entry nv / pending / 待核实节 / coverage count）**四处一致**；`time_or_place` 干净。`check.py`（含 D14 一致性）**PASS** 佐证。

## 五、★ 七节 / SVG / 规范句 / site 一致

| 核对项 | damp-proofing | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | 定义＋原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实；`check.py` 6 节全非空 PASS |
| 原理非「定义+概述」逐字拼接 | ✓ | 原理聚焦「薄膜/涂层阻隔切断渗入路径」，与定义/概述为不同层面的独立表述 |
| SVG 数量/画布 | ✓ 1 张 | `viewBox='0 0 760 400'`，含「示意图，非施工图」×2（SVG 文本＋figcaption） |
| SVG 越界/禁用 | ✓ | 元素：`rect x140 y140 w480 h170`→x∈[140,620], y∈[140,310]；`line x140–620, y250`；text (300,230)、(300,375)；均在 760×400 内；无 `<image>`/外链；`pytest` `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」＋页脚 note |
| site 一致 | ✓ | `site/entries/damp-proofing.html` 逐节渲染与 JSON 一致（lead=overview、定义、原理、典型手法、实例、常见错误、一图、待核实=暂无、3 来源 均对上） |
| 来源数 | 3（wp-building-material / wp-sunken-courtyard / db-damp-proofing），均 verified=true；核心双平台=wp-building-material＋db-damp-proofing | `check.py` ≥2 PASS |

## 六、★ 相似度（阈值 0.54）

方法（承第97/98轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与第39–98轮报告逐位一致，口径正确）**。全库 258 条。

| 口径 | 最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- |
| 短① | postmodernism | 0.3057 | <0.54 | ✓ |
| 短① | color-psychology / green-architecture | 0.3026 / 0.3022 | <0.54 | ✓ |
| 全字段② | rule-of-odds | 0.3111 | <0.54 | ✓ |
| 全字段② | rock-garden / vernacular-architecture | 0.3082 / 0.3021 | <0.54 | ✓ |

- damp-proofing 全库最近邻：短口径＝`postmodernism 0.3057`；全字段口径＝`rule-of-odds 0.3111`。
- **对全库所有其他条目：短口径 max 0.3057、全字段 max 0.3111，均 ≪ 0.54；无任何对手 >0.54。相似度合格 ✓，余量充足。**

## 七、总判定与依据

**结论：damp-proofing（防潮）——合格（nv=false 升级成立）。**

依据（逐项对齐任务核对点）：
1. **概念/定义/原理双平台支撑：成立 ✓（互补式双平台）**。核心机制「以防水薄膜/阻隔层控制墙体地面湿度、防地下/近地受潮」由 `wp-building-material`（`damp proofing and waterproofing membranes ... basement waterproofing`）＋`db-damp-proofing`（`moisture control ... applied to walls and floors`；`Rising damp/Penetrating damp`；`damp-proof membrane`；`Surface coating`）两独立平台共同直证；`薄膜`与`地下 basement`两要素双源直证。**透明项：`上升潮/渗透潮`、`表面涂层`、逐字“墙体地面”仅由 db 单源承载，wp 只提供 membrane+basement 骨架——两平台为互补式而非逐元素互证（见下方透明说明 A）。**
2. **两源独立：成立 ✓**。Wikipedia（wp-building-material）与 Designing Buildings（db-damp-proofing）为不同组织/平台，无派生关系。
3. **wp-sunken-courtyard 是否支撑防潮：否（0 命中）**。仅作“下沉空间”主题语境源，对防潮定义/原理/实例零支撑；防潮双平台实为 wp-building-material＋db-damp-proofing（透明说明 B）。
4. **类型性实例合理、不编造：成立 ✓**。`地下空间防潮构造（类型性，不指定具体项目）`，内容与 db 逐项有源一致；未给具体项目名/地点/设计者/年份，无编造。
5. **nv=false 落地、形式四处一致：✓**（entry nv=false / pending="" / 待核实=暂无 / coverage count=0；time_or_place 无待核实；`check.py` PASS）。
6. **七节/SVG/规范句/site：✓**（`viewBox 0 0 760 400`、框内、无外链、含「示意图，非施工图」、规范句在、site 与 JSON 一致；`check.py` PASS、`pytest` 5 passed）。
7. **相似度：✓**（短 max 0.3057、全字段 max 0.3111，均 ≪0.54；方法自校 0.5157）。

透明说明（不改合格判定，供 lead 决策）：
- **(A) 双平台为“互补式”共同支撑，非逐元素互证**：`薄膜 membrane`＋`地下 basement` 两要素确由 wp＋db 双源直证；但 `上升潮/Rising damp`、`渗透潮/Penetrating damp`、`表面涂层/Surface coating` 及“墙体地面”逐字表述仅由 `db-damp-proofing` 单源承载，`wp-building-material` 未独立复述。若日后采用“定义内每一具体术语均须双源互证”的更严口径，则这是唯一可再收紧点——建议补一条权威 `Rising damp / Damp (structural)` 类专条作第二源，或把相关具体术语据实标注为单源。当前按“两独立平台共同支撑核心概念”口径判合格。
- **(B) `wp-sunken-courtyard` 对防潮零覆盖**（damp/waterproof/membrane/basement/moisture/proof 全 0），仅主题语境作用；如统一收紧来源相关度，可将其替换为更强的防潮专条。不构成当前事实缺陷。
- **(C) overview「地下水压力」属一般性概括**：db 覆盖 rising damp / tanking / basement waterproofing 等地下水语境界定，“地下水压力（hydrostatic pressure）”非逐字、属通用概述，非编造、非具体数值。

## 八、机器可读汇总

```
ROUND=99
SAMPLER=spotcheck-r99
SCOPE=["damp-proofing"]
READONLY="only wrote research/spotcheck-round99.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={"db-damp-proofing":"web_fetch HTTP200 (Damp_proofing_buildings)",
 "wp-building-material":"web_fetch TypeError->urllib HTTP200 raw~381579 (first fetch; later refetch timeout)",
 "wp-sunken-courtyard":"urllib HTTP200 raw~70503"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
GIT={"changed":["M coverage.json","M data/sources.json","M entries/batch-02-c.json","M site/entries/damp-proofing.html","M site/index.html","M site/sources.html","?? tools/apply_review_round99.py"],"note":"all round99 fixer outputs; sampler read-only"}

DAMP_PROOFING={
 "verdict":"合格",
 "change":"sources +db-damp-proofing; definition/原理 重写为薄膜/涂层阻隔控湿; 实例 类型性(不指定具体项目); nv true->false; pending 清空; 待核实 清空",
 "concept_dual_source":{
   "platforms":["Wikipedia wp-building-material (Building material)","Designing Buildings db-damp-proofing (Damp proofing buildings)"],
   "membrane(薄膜)":"wp 'damp proofing and waterproofing membranes ... basement waterproofing' + db 'damp-proof course ... membrane' / 'damp-proof membrane (DPM)' -> DOUBLE",
   "basement/地下":"wp 'basement waterproofing' + db 'walls and floors'/rising damp -> DOUBLE",
   "moisture_control_walls_floors":"db 'moisture control ... applied to walls and floors' (wp only implicit via basement) -> db-explicit",
   "rising_penetrating_damp":"db 'Rising damp'/'Penetrating damp' only -> db-ONLY",
   "surface_coating":"db 'Surface coating: Waterproof surface materials ... render or waterproof plaster' only -> db-ONLY",
   "barrier":"wp implicit + db 'a barrier ... to prevent damp rising'/'capillary action' -> DOUBLE(implicit+explicit)",
   "pattern":"complementary dual-platform: wp gives membrane+basement backbone; db gives full detail(moisture control/rising/penetrating/surface coating)",
   "holds":true},
 "independence":{"holds":true,"detail":"Wikipedia vs Designing Buildings = two independent orgs/platforms, no derivation"},
 "wp_sunken_courtyard_supports_damp":false,
 "wp_sunken_courtyard_scan":{"damp":0,"waterproof":0,"membrane":0,"basement":0,"moisture":0,"proof":0,
   "note":"theme-context source only; effective dual = wp-building-material + db-damp-proofing"},
 "instance":{"text":"地下空间防潮构造(类型性,不指定具体项目)","typological":true,"specific_project":false,
   "support":"db-damp-proofing membrane/surface coating/rising/penetrating damp","fabricated":false,"no_place_designer_year":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无已知待核实项 / coverage needs_verification_count=0 四处一致; time_or_place='20世纪、全球(参见来源).' 无待核实; check.py PASS",
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"postmodernism 0.3057","nearest_full":"rule-of-odds 0.3111",
   "max_short":0.3057,"max_full":0.3111,"lt_0.54":true,"method_selfcheck_futurism_expressionism":0.5157,"entries":258},
 "transparency_notes":[
   "A: 双平台为互补式——薄膜+地下 basement 双源直证; 上升潮/渗透潮/表面涂层/墙体地面逐字 仅 db 单源, wp 未独立复述; 若采用逐元素互证严口径可补 Rising damp/Damp(structural) 专条或据实标单源",
   "B: wp-sunken-courtyard 对防潮零覆盖(6词全0), 仅主题语境源; 必要时可替换为更强防潮专条",
   "C: overview '地下水压力' 属一般性概括(非逐字、非数值、非编造)"]
}

VERDICT={"damp-proofing":"合格"}
KEY_FINDING="damp-proofing 防潮 nv=false 升级成立: 核心概念『以防水薄膜/阻隔层控制墙体地面湿度、防地下/近地受潮』由 Wikipedia(wp-building-material: 'damp proofing and waterproofing membranes ... basement waterproofing') + Designing Buildings(db-damp-proofing: 'moisture control applied to walls and floors' / Rising damp / Penetrating damp / damp-proof membrane / Surface coating) 两独立平台共同支撑; 薄膜+地下两要素双源直证; wp-sunken-courtyard 对防潮零覆盖(6词全0, 仅主题语境源); 类型性实例(不指定具体项目, 未给名称/地点/设计者/年份)有源不编造; nv=false 形式四处一致, time_or_place 干净; 七节/SVG(760x400框内无外链)/规范句/site一致; check.py PASS + pytest 5 passed; 相似度短0.3057/全0.3111 均≪0.54(方法自校0.5157). 透明: 双平台为互补式——上升潮/渗透潮/表面涂层仅db单源, wp仅给membrane/basement骨架; 地下水压力为一般概括."
```

## 九、只读核验

- 除本报告 `research/spotcheck-round99.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 三个来源本轮均实抓回读（`db-damp-proofing`=web_fetch HTTP200；`wp-building-material`=urllib HTTP200 raw≈381,579 首次抓取成功并完成词扫描，后续复抓因网络间歇超时未再取但已捕获唯一相关原句；`wp-sunken-courtyard`=urllib HTTP200 raw≈70,503）；词扫描、相似度、git 核对均内存态 `python -` 直跑，无临时文件。
- 联网页面（Wikipedia / designingbuildings.co.uk）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中的改动文件与 `?? tools/apply_review_round99.py` 均为**修复方（round99 applier＋gen_site）自身产物**，抽检方仅读取、未据以修改。

*（报告完）*
