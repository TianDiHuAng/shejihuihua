# 第104轮 material-color 复审（spotcheck-round104b）——修正后双平台支撑 / 无源主张彻底移除核查

- 复审人：spotcheck-r104b（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：已加载 `using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言，证据先于结论）。`using-superpowers` 命中 SUBAGENT-STOP，按任务说明书直接执行；`verification-before-completion` 全程遵循——本文所有判断均附本轮实抓/实跑/实读输出。
- 复审对象：`material-color`（材料色彩）——entry 在 `entries/batch-35.json`（unit_id=batch-35，第 12 条之一）；sources〔wp-color-theory / wp-building-material / db-colour〕；coverage row（title 材料色彩，status 已写，source_count 3，needs_verification_count 0，level L2，last_updated 2026-11-24）。
- 本轮修正声称：(a) 更正 `db-colour` 的 note 为准确表述；(b) 将 `definition`/`原理` 改为「材料固有色 + 入射光条件决定呈现色」，删除「表面质感/纹理影响色彩」无源主张；实例仍类型性；nv=false。**下文一律以实读当前 JSON 为准。**

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round104b.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`site/`、`tools/`，未 `git commit`，未改项目外内容。抓取、词比对、相似度、去重、结构、SVG 越界、site 一致性均内存态 `python - <<'PY'` / 工具直跑，未落盘临时文件（除本报告）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码）：
  - `db-colour = https://www.designingbuildings.co.uk/wiki/Colour` → `web_fetch` **HTTP 200**，**重定向到 `/wiki/Colour_in_the_built_environment`**，H1=`Colour in the built environment`。
  - `wp-color-theory = https://owiki.org/wiki/Color_theory` → `web_fetch` **HTTP 200**，H1=`Color theory`。
  - `wp-building-material = https://owiki.org/wiki/Building_material` → `web_fetch` **HTTP 200**，H1=`Building material`。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（CHECK_EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed in 0.13s`（PYTEST_EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）
- `git status --short`：`M coverage.json / M data/sources.json / M entries/batch-08.json / M entries/batch-35.json / M site/entries/daylight-factor.html / M site/entries/material-color.html / M site/index.html / M site/sources.html / ?? research/spotcheck-round104.md / ?? research/spotcheck-round104b.md / ?? tools/apply_review_round104.py`——前八项为修复方产物；`??` 为本抽检报告与修复脚本。抽检方仅读取，未据以修改。

## 一、definition / 原理「固有色 + 入射光条件决定呈现色」双平台核对（实抓引句）

当前 entry 实读（`entries/batch-35.json`，id=material-color）：
- `definition`＝「材料色彩指材料的**固有色**及其在**光照条件**下呈现的颜色，影响空间氛围。」
- `sections.原理`＝「材料的呈现色由**固有色**与**入射光条件**决定：同一材料在不同光源与光线下明度与冷暖会变，故色彩需结合照明条件来评估。」
- 关键：`definition` / `原理` **均已不含「表面质感/纹理/表面」字样**（逐字段关键词扫描：definition hits=[]、原理 hits=[]）。

实抓引句（逐字核对）：
- `db-colour`（Designing Buildings「Colour in the built environment」；HTTP200，经 /wiki/Colour 重定向，H1=Colour in the built environment）：
  - `Light (a form of electromagnetic radiation) of a certain wavelength must be emitted, transmitted or reflected by an object. The wavelength will determine whether that colour is green, red or blue or a combination of these`（**物体反射/透射的波长决定颜色＝固有色/材质反射决定呈现色 ✓✓**）
  - `Colour can only be perceived due to the presence of light and most light sources produce different light wave combinations.`（**色彩只能在光存在下被感知；不同光源产生不同光波组合＝光照条件影响色彩感知 ✓✓✓，逐字直证**）
- `wp-color-theory`（Wikipedia `Color theory`；owiki HTTP200）：
  - `color is not intrinsic to objects, but rather arises from the way an object reflects or absorbs different wavelengths.`（**颜色源自物体反射/吸收不同波长＝固有色决定呈现色 ✓✓**）
  - `The influence of light on color was investigated and revealed further by al-Kindi and Ibn al-Haytham.`（**光对颜色的影响 ✓✓**）
  - `the prevailing context which includes setting and ambient lighting`（**环境照明属影响色彩感知的情境因素 ✓**）
- `wp-building-material`（Wikipedia `Building material`；owiki HTTP200，「Glass」节）：
  - `Additives are often included the mixture used to produce glass with shades of colors or various characteristics.`（**添加剂使玻璃呈不同色相＝材料固有色 ✓（弱）**）

| 概念要素 | db-colour（DB） | wp-color-theory | wp-building-material | 判定 |
| --- | --- | --- | --- | --- |
| 固有色 / 材质反射决定呈现色 | ✓✓ `wavelength … reflected by an object … determine … colour` | ✓✓ `arises from the way an object reflects or absorbs different wavelengths` | ✓ `Additives … produce glass with shades of colors`（弱） | **双平台直证（DB＋WP）✓✓** |
| 光照条件影响呈现色 | ✓✓ `Colour can only be perceived due to the presence of light … different light wave combinations` | ✓✓ `influence of light on color`；`ambient lighting` | ✗ | **双平台直证（DB＋WP）✓✓** |

**判定（一）：** definition/原理 中「固有色」与「光照条件（不同光源不同光波）决定呈现色」之核心——**双独立平台（Designing Buildings db-colour ＋ Wikipedia wp-color-theory，wp-building-material 弱佐）逐要素直证，成立、非编造、双平台强支撑 ✓✓。** 修正 (b) 对 definition/原理 的目标达成。

## 二、★特别判断：「表面质感/纹理影响色彩」无源主张是否已彻底移除（本轮核心）

逐字段关键词扫描（`质感` / `纹理` / `表面`）实读结果：

| 字段 | 命中 | 原文 | 判定 |
| --- | --- | --- | --- |
| definition | 无 | 材料色彩指材料的固有色及其在光照条件下呈现的颜色，影响空间氛围。 | ✓ 已移除 |
| 原理 | 无 | 材料的呈现色由固有色与入射光条件决定：… | ✓ 已移除 |
| **overview** | **`纹理`** | **材料色与涂层色不同，受纹理与光照影响。** | ✗ **无源主张残留** |
| 一图 | `质感` | 见下方示意：不同材料的固有色与质感。 | △ 提及「质感」（描述性、较弱） |
| 典型手法/实例/常见错误/待核实 | 无 | — | ✓ |

- **definition / 原理 已彻底移除「表面质感/表面纹理影响色彩」——是。**
- **但全条目并未「彻底移除」：`overview` 字段仍写「材料色与涂层色不同，受纹理与光照影响」，其语义正是「材料色受纹理影响」这一无源主张，逐字残留。** 该字段在 site 页面以 lead 段落呈现（`site/entries/material-color.html`：`<p class="lead">材料色与涂层色不同，受纹理与光照影响。</p>`，已实读一致）。
- **该残留是否有所引源支撑？无。**
  - `db-colour`：全文唯一出现 `surface texture` 的句子是定义句 `Everything that an individual perceives visually that is not to do with their perception of shape, size, surface texture, tone and motion of objects can be termed 'colour'.`——把 shape/size/surface texture/tone/motion 作为与 colour **相区分（并列排除）**的感知维度，**不支撑「纹理影响色彩」，反而把二者区分**。
  - `wp-color-theory`：仅述「颜色源自反射/吸收不同波长」与「光/环境照明影响颜色」，**未涉及表面粗糙度/光泽（纹理）如何改变色彩感知**。
  - `wp-building-material`：未涉及。
  - ⇒ `overview`「受纹理…影响」在全部三源中**无支撑（无源）**。

**结论（二）：** 「表面质感/纹理影响色彩」无源主张**在 definition/原理 已消除，但在 overview（及一图注「质感」）仍残留，未「彻底移除」**。这是本轮唯一阻断项：内容层面仍有未溯源成分，且该成分与 db-colour 原文区分句语义相冲突。

## 三、修正 (a) 复核：db-colour 的 note 是否为准确表述

实读 `data/sources.json` 中 db-colour：
- `note`＝「访问于 2026-11-24，实抓 HTTP 200；**色彩需有光方能被感知，不同光源产生不同光波组合（色彩为区别于形状/尺寸/表面质感等之外的感知）**」
- 逐句比对原文：
  - 「色彩需有光方能被感知」↔ `Colour can only be perceived due to the presence of light` ✓
  - 「不同光源产生不同光波组合」↔ `most light sources produce different light wave combinations` ✓
  - 「（色彩为区别于形状/尺寸/表面质感等之外的感知）」↔ `not to do with their perception of shape, size, surface texture, tone and motion … can be termed 'colour'` ✓
- **判定：note 已为准确表述，上一轮「把区分句反向转写成『色彩感知受…表面质感…影响』」的误引已纠正 ✓（修正 (a) 达成）。** 值得注意：源注本身已不再宣称「纹理影响色彩」，恰与 `overview` 仍写「受纹理…影响」形成背离——条目正文超出（且违背）了它自己的源注。

## 四、是否编造

- definition/原理 核心（固有色 + 入射光条件）**有源、非编造** ✓。
- db-colour note **准确、无误引** ✓。
- 残留 `overview`「受纹理与光照影响」：属**未溯源的解释性/通识性延伸**（物理光学上「粗糙/光滑表面反射不同」可解释），非「凭空虚构事实」，但确为**无源主张**且与 db-colour 区分句相冲突——按本项目「主张须可溯源」口径，不能挂靠任一所引源。

## 五、nv=false 是否成立

| 核对项 | material-color | 判定 |
| --- | --- | --- |
| `needs_verification`（entry） | `false` | ✓ 形式 |
| `pending_notes` | `""` | ✓ 形式 |
| `sections.待核实` | 「暂无已知待核实项。」 | ✓ 形式 |
| `coverage.json` 记录 | status 已写、source_count 3、needs_verification_count 0、last_updated 2026-11-24、level L2 | ✓ 形式 |
| `time_or_place` | 「跨时期、全球（参见来源）。」无「待核实」 | ✓ 形式 |

- **形式四处一致 ✓；`check.py` PASS。**
- **内容前提：definition/原理 已达标，但 `overview` 残留无源「纹理影响色彩」→ 内容前提未完全满足，nv=false 严格意义上仍不成立**（该无源成分应当删除或补源，方能落 nv=false）。

## 六、七节 / SVG / 规范句 / site

| 核对项 | material-color | 判定 |
| --- | --- | --- |
| 七节（定义＋原理/典型手法/实例/常见错误/一图/待核实） | 6 节全非空 + definition，共七节 | ✓ |
| SVG 数量 / 画布 | 1 张，`viewBox='0 0 760 400'` | ✓ |
| SVG 越界 | 元素均在框内（rect x140–360/400–620, y130–270；text 300,375 与 40,40） | ✓ |
| SVG 外链 | 无 `<image>/<script>/href=/xlink/url(` | ✓ |
| SVG 注记 | 含「示意图，非施工图」 | ✓ |
| 规范句（常见错误收尾） | 含「实际工程须按当地规范和专业设计人员的要求」，**句末缺「。」** | ✓（T 小疵） |
| site 与 JSON 一致 | 标题/definition/原理/overview/实例/一图/规范句/SVG 均一致（实读）；**含 overview「受纹理与光照影响」** | ✓（一致，亦复现残留） |
| 来源数 / 双平台 | 3（wp-color-theory + wp-building-material + db-colour）；平台=Wikipedia×2＋Designing Buildings(DB) | ✓ |

## 七、相似度（阈值 0.54）与 def≠原理

方法（承前轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（逐位一致，口径正确）**。全库 258 条。

| 条目 | 口径 | 最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- | --- |
| material-color | 短① | structural-material | 0.4000 | <0.54 | ✓ |
| material-color | 全② | wind-driven-ventilation | 0.3757 | <0.54 | ✓ |

- 指定对比（本轮实算）：`material-color × transparent-material` 短 0.2892 / 全 0.3293；`material-color × material-texture` 短 0.3511 / 全 0.2714；`material-color × color-symbolism` 短 0.3969 / 全 0.2496——**均 <0.54 ✓**。
- 全库最大：短 0.496、全 0.5256——**均 <0.54，无任何对手越阈 ✓**。
- **def≠原理（去重）：material-color `definition×原理` = 0.2791（低重叠、两层次可分，去重良好）✓。**

## 八、总判定与依据

**结论：`material-color`（材料色彩）——不合格（残留无源主张未彻底移除）。**

依据（逐项对齐任务核对点）：
1. **definition/原理「固有色 + 光照影响呈现色」双平台支撑——成立 ✓✓。** 固有色：db-colour `wavelength … reflected by an object … determine … colour`＋wp-color-theory `arises from the way an object reflects or absorbs different wavelengths`（＋wp-building-material「添加剂呈色」弱佐）；光照：db-colour `Colour can only be perceived due to the presence of light … different light wave combinations`＋wp-color-theory `influence of light on color` / `ambient lighting`。**DB＋WP 双独立平台逐要素直证。**
2. **「表面质感/纹理影响色彩」无源主张是否已彻底移除——否 ✗（本轮核心缺陷）。** definition/原理 已清除，但 `overview` 仍写「材料色与涂层色不同，**受纹理与光照影响**」（site lead 段落复现），一图注亦提「质感」；该「纹理影响色彩」在 db-colour / wp-color-theory / wp-building-material 三源中**均无支撑**（db-colour 唯一 `surface texture` 句为「色彩=排除形状/尺寸/表面质感/色调/运动的感知」的区分句，语义相反）。故**未彻底移除**。
3. **是否编造——核心不编造 ✓；db-colour note 已更正为准确表述、无误引 ✓。** 唯 `overview` 残留「纹理影响」属无源延伸（非虚构事实，但仍无源、且与 db-colour 区分句冲突）。
4. **nv=false——形式四处一致 ✓，但内容前提因 overview 残留而无源 → 严格不成立 ✗。**
5. **七节/SVG/规范句/site——七节全非空 ✓、SVG 1 张 760×400 框内无外链含「示意图，非施工图」✓、规范句在（句末缺「。」小疵）✓、site 与 JSON 一致 ✓。** `check.py` PASS、`pytest` 5 passed。
6. **相似度——短 0.4000 / 全 0.3757，指定对比与全库最大均 <0.54 ✓；def≠原理 0.2791 去重良好 ✓；方法自校 0.5157 ✓。**

透明说明（供 lead 决策）：
- **(T1，阻断项) overview 残留无源「纹理影响色彩」**：最小修正——将 `overview`「材料色与涂层色不同，受纹理与光照影响。」改为「材料色与涂层色不同，**受固有色与光照条件影响**。」（并建议一图注「不同材料的固有色与质感」→「不同材料的固有色与光照效果」）。修正后全条目即无「纹理/表面质感影响色彩」字样，definition/原理/overview 一致双平台可溯源，可转 **合格**。此项在 definition/原理 已达标，缺陷仅在 overview（及一图注）这一处残留。
- **(T2，小疵) 常见错误与限制 规范句句末缺「。」**（`…专业设计人员的要求`，与 r101/r102/r103/r104 T3 同型）；`check.py` 未拦（`REGULATION_NOTE` 只匹配子串）。
- **(T3) 命名/重定向口径**：`db-colour` url 记 `/wiki/Colour`，实抓重定向至 `/wiki/Colour_in_the_built_environment`（H1=`Colour in the built environment`）——link_ok 语义不受影响，承前轮同型，非本轮新问题。

## 九、机器可读汇总

```
ROUND=104b
SAMPLER=spotcheck-r104b
SCOPE=["material-color"]
READONLY="only wrote research/spotcheck-round104b.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={
 "db-colour":"web_fetch HTTP200 redirect /wiki/Colour->/wiki/Colour_in_the_built_environment H1='Colour in the built environment'",
 "wp-color-theory":"owiki.org HTTP200 H1='Color theory'",
 "wp-building-material":"owiki.org HTTP200 H1='Building material'"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}

MATERIAL_COLOR={
 "verdict":"不合格(残留无源主张未彻底移除: overview '受纹理与光照影响')",
 "definition":"材料色彩指材料的固有色及其在光照条件下呈现的颜色，影响空间氛围。",
 "principle":"材料的呈现色由固有色与入射光条件决定：同一材料在不同光源与光线下明度与冷暖会变，故色彩需结合照明条件来评估。",
 "concept_dual_source":{
   "inherent_colour_material_reflection":"db 'wavelength ... reflected by an object ... determine ... colour' + wp-ct 'arises from the way an object reflects or absorbs different wavelengths' + wp-bm 'Additives ... glass with shades of colors'(weak) -> DOUBLE(DB+WP) OK",
   "light_affects_presented_colour":"db 'Colour can only be perceived due to the presence of light ... different light wave combinations' + wp-ct 'influence of light on color'/'ambient lighting' -> DOUBLE(DB+WP) OK",
   "holds":true},
 "unsourced_claim_removed_completely":{
   "definition":"REMOVED (no 质感/纹理/表面)",
   "principle":"REMOVED (no 质感/纹理/表面)",
   "overview":"NOT REMOVED -> '材料色与涂层色不同，受纹理与光照影响。' still present (site lead paragraph)",
   "一图":"mentions 质感 ('不同材料的固有色与质感', weaker/descriptive)",
   "residual_supported_by_any_source":false,
   "holds":false},
 "db_colour_note_fixed":true,
 "db_colour_note":"访问于 2026-11-24，实抓 HTTP 200；色彩需有光方能被感知，不同光源产生不同光波组合（色彩为区别于形状/尺寸/表面质感等之外的感知）",
 "fabrication":"core not fabricated; db-colour note accurate/no misquote; overview '纹理影响' is unsourced extension (not fabricated fact but unsourced, conflicts with db-colour distinction clause)",
 "nv_false_form":"four-place consistent (nv=false/pending=''/待核实=暂无/coverage nv_count=0/time_or_place clean); check.py PASS",
 "nv_false_grounded":false,
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"caption":"示意图，非施工图","reg_sentence":true,"reg_period":false,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"nearest_short":"structural-material 0.4000","nearest_full":"wind-driven-ventilation 0.3757","vs_transparent_material_short":0.2892,"vs_transparent_material_full":0.3293,"vs_material_texture_short":0.3511,"vs_material_texture_full":0.2714,"vs_color_symbolism_short":0.3969,"vs_color_symbolism_full":0.2496,"max_short":0.4000,"max_full":0.3757,"global_max_short":0.496,"global_max_full":0.5256,"lt_0.54":true},
 "def_vs_principle":{"ratio":0.2791,"distinct":true},
 "transparency":["T1 overview 残留无源 '受纹理与光照影响'（阻断项）","T2 常见错误句末缺句号","T3 重定向口径"]}
METHOD_SELFCHECK={"futurism_x_expressionism_full":0.5157,"entries":258}
VERDICT={"material-color":"不合格(残留无源主张未彻底移除: overview '受纹理与光照影响'; definition/原理已清除且双平台支撑成立, db-colour note 已更正)"}
KEY_FINDING="material-color 复审第104轮修正：definition/原理『固有色+入射光条件决定呈现色』已由 db-colour('Light of a certain wavelength must be emitted, transmitted or reflected by an object. The wavelength will determine whether that colour is green, red or blue' / 'Colour can only be perceived due to the presence of light and most light sources produce different light wave combinations') + wp-color-theory('color ... arises from the way an object reflects or absorbs different wavelengths' / 'influence of light on color' / 'ambient lighting') + wp-building-material('Additives ... produce glass with shades of colors' 弱) 双平台逐要素直证; db-colour note 已更正为准确表述（'色彩需有光方能被感知，不同光源产生不同光波组合（色彩为区别于形状/尺寸/表面质感等之外的感知）'），上一轮误引已纠正，definition/原理 已彻底删除『表面质感/纹理影响色彩』。★但全条目未彻底移除：overview 仍写『材料色与涂层色不同，受纹理与光照影响。』（site lead 段落复现），一图注亦提『质感』——该『纹理影响色彩』在三源均无支撑（db-colour 唯一 surface texture 句为『色彩=排除形状/尺寸/表面质感/色调/运动的感知』区分句，语义相反）。故内容前提未完全满足，nv=false 严格不成立。形式项全过：七节/SVG(760x400框内无外链含示意图非施工图)/site一致/规范句在(句末缺句号)；相似度短0.4000/全0.3757<0.54，def×原理0.2791，方法自校0.5157；check.py PASS+pytest 5 passed。最小修正：overview 改『受固有色与光照条件影响』(一图注改『固有色与光照效果』)后可转合格。"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round104b.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- db-colour 经 `web_fetch` 直抓 HTTP 200（/wiki/Colour→/wiki/Colour_in_the_built_environment，H1=Colour in the built environment）；wp-color-theory、wp-building-material 经 `owiki.org` HTTP200 抓回（H1 逐一核对一致）。
- 词比对、关键词扫描、相似度、去重、结构、SVG 越界/外链、site 一致性均内存态 `python - <<'PY'` 直跑，无临时文件。
- 联网页面（designingbuildings.co.uk / owiki.org）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中的改动文件与 `?? tools/apply_review_round104.py` 均为**他方（round104 修复方）产物**，抽检方仅读取、未据以修改。

*（报告完）*
