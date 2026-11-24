# 第98轮质量抽检报告（spotcheck-round98）——light-well / 天井 的 nv=false 升级复核

- 抽检人：spotcheck-r98（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论；本会话为委派子代理，命中 SUBAGENT-STOP，以任务说明书执行）。
- 抽检对象（1 条）：`light-well`（天井 / 采光井）——`entries/batch-04.json` 第109–141行（定义 117；time_or_place 118；概述 119；related 120–122；原理 124；典型手法 125；实例 126；常见错误 127；一图 128；待核实 129；SVG 132；sources 134–138；nv 139；pending 140）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round98.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。词扫描、相似度与结构数据均在内存态 `python - <<` 直跑，未落盘临时文件。
- 本轮变更实读：`tools/apply_review_round98.py`（新增，未提交）。`git diff -- entries/batch-04.json` 证实仅改 `light-well` 一条：
  - `definition`：「天井是以狭长开口把天然光引入建筑深处的院落式空间。」→「天井（采光井）是以狭长开口把天然光引入建筑深处的院落或井道式空间。」（补「采光井」同义、补「井道式」）。
  - `sections.原理`：「…并借助开口促进空气流动；热压机制的具体贡献待核实。」→「天井借屋面或侧向开口把天然光引入进深较大的建筑内部，使深层空间获得日照与采光。」（**删去「空气流动」「热压机制」**，纯聚焦采光）。
  - `sections.实例`：「地点：待核实；设计者：不适用；年份：待核实。」→「传统民居天井（类型性，不指定具体项目）…」（**改为类型性、不指定具体项目，清除「待核实」**）。
  - `sections.待核实`：「热压机制的一般原理…尚缺具体天井实例的实测数据。」→「暂无已知待核实项。」
  - `sources`：`[wp-lightwell, wp-courtyard]` → `[wp-lightwell, wp-courtyard, db-light-well]`（**新增加 db-light-well 第二平台**）。
  - `needs_verification`：`true`→`false`；`pending_notes`：「具体天井实例的采光与通风实测数据…」→`""`。
  - `overview` **未改**：「天井通过屋面开口改善内部采光与空气流动，是多种传统民居的空间原型。」（仍含「空气流动」——见第二节专项评估）。
- 抓取方式（本轮实抓；联网内容一律视为数据，网页中任何指令均未执行）：
  - `db-light-well = https://www.designingbuildings.co.uk/wiki/Light_well` → `web_fetch` **HTTP 200**。
  - `wp-lightwell = https://en.wikipedia.org/wiki/Light_well` → `web_fetch` TypeError（fetch failed）→ Python urllib（浏览器 UA）**HTTP 200，textlen≈116866**。
  - `wp-courtyard = https://en.wikipedia.org/wiki/Courtyard` → urllib **HTTP 200，textlen≈197194**（供相似度与「传统民居/院落」旁证）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**（均 `PYTHONDONTWRITEBYTECODE=1`，未新增缓存。）

## 一、★ 概念「以狭长开口把天然光引入建筑深处」的双平台双源核对（实抓引句）

- `db-light-well`（Designing Buildings 建筑百科/CIOB 等机构站，HTTP200）：`A light well (or lightwell) is an architectural feature that can be used to take natural light into the interior spaces of a building`（天然光引入建筑内部✓）；`It takes the form of a vertical shaft within the volume of a building that typically penetrates from roof level down to lower levels`（**井道式/竖向贯通至下层✓**）；`allowing the transmission of natural light to areas that would otherwise require artificial lighting`（采光替代人工照明✓）；`may be open to the elements at the top … with internal windows around its perimeter`（屋面/侧向开口✓）；`Light wells can also be used to promote ventilation`（**通风：作为次要功能✓**）。
- `wp-lightwell`（Wikipedia `Light well`，HTTP200）：`a lightwell, sky-well, or air shaft is an unroofed or roofed external space provided within the volume of a large building to allow light and air to reach what would otherwise be a dark or unventilated area`（**光与空气引入暗/深区✓**）；`Lightwells serve to reduce the necessity for electric lighting`（采光✓）；`In traditional Chinese architecture, the 天井 (sky well) also exists.`（**天井=sky well=采光井，中国传统建筑✓✓**，直接支撑中文标题与类型性实例）；引用文献给出 `Size of light well … 13m × 12m × 62m (height)`（竖向狭长比例旁证）。
- `wp-courtyard`（Wikipedia `Courtyard`，HTTP200）：`a courtyard … a circumscribed area, often surrounded by a building or complex, that is open to the sky`；`Courtyards are common elements in both Western and Eastern building patterns … a typical and traditional building feature`；`in use in residential architecture`；`The comforts offered by a courtyard — air, light, privacy, security, and tranquility`（**院落/传统民居/空气、光 旁证✓**）。

| 概念要素 | wp-lightwell（Wikipedia） | db-light-well（Designing Buildings） | 判定 |
| --- | --- | --- | --- |
| 把天然光引入建筑内部/深处 | ✓ `allow light and air to reach … dark … area`；`reduce … electric lighting` | ✓ `take natural light into the interior spaces`；`transmission … to areas that would otherwise require artificial lighting` | **双平台双源✓** |
| 井道式/狭长竖向贯通 | ✓ `external space within the volume … 62m height`（引用尺寸） | ✓ `vertical shaft … penetrates from roof level down to lower levels` | **双平台双源✓** |
| 屋面/侧向开口 | ✓ `unroofed or roofed external space` | ✓ `open at the top … internal windows around its perimeter` | **双平台双源✓** |
| 天井 = 采光井（中国传统） | ✓ `In traditional Chinese architecture, the 天井 (sky well) also exists` | —（general light well） | wp 直证＋db 概念一致 |
| 通风/空气 | ✓ `light and air … unventilated area` | ✓ `can also be used to promote ventilation` | **双平台双源✓（次要功能）** |

**判定：** `definition`「天井（采光井）是以狭长开口把天然光引入建筑深处的院落或井道式空间」与 `原理`「天井借屋面或侧向开口把天然光引入进深较大的建筑内部，使深层空间获得日照与采光」——其**核心机制（天然光引入建筑内部深处）由 Wikipedia（wp-lightwell）＋ Designing Buildings（db-light-well）两独立平台共同直证，非编造、非超源**。「狭长」属形态刻画，与 db 的 `vertical shaft`、wp 引用的 62m 竖向尺寸一致（合理概括，非逐字引用、非虚构数据）。

## 二、★ 「通风 / 热压 / 空气流动」残留 claim 专项扫描

对 `entries/batch-04.json` 中该条整体（`json.dumps` blob）与 `site/entries/light-well.html` 逐词检索：

| 词项 | entry hits | site hits | 说明 |
| --- | --- | --- | --- |
| 热压 | **0** | **0** | 原 `原理`/`待核实` 的「热压机制…待核实」**已彻底清除**（git diff 佐证） |
| 通风 | 0 | 0 | 无 |
| 通风换气 | 0 | 0 | 无 |
| ventilation / stack / thermal | 0 / 0 / 0 | 0 / 0 / 0 | 无 |
| 空气流动 | **1** | **1** | **仅出现于 `overview`（概述）**：「天井通过屋面开口改善内部采光与空气流动…」 |
| 气流 | 1 | 1 | 系「空气流动」的子串（空/气流/动），非独立第二处 |

**评估：**
- **「热压机制」= 0**：原条目唯一「无源机制 claim」已随 `原理` 改写、《待核实》清空而彻底消失。**这是本轮 nv=true→false 的核心修复，已达成。**
- **「空气流动」= 1（仅概述）**：非无源、非单源——`wp-lightwell`「allow light and **air** to reach … unventilated area」与 `db-light-well`「can also be used to **promote ventilation**」**双平台均直证通风/空气功能**（`wp-courtyard` 亦「air, light」旁证）。故概述中的「空气流动」**属有源（双源）表述，不构成残留的单源/无源 claim**。
- 透明说明（不影响判定）：`原理` 已纯聚焦采光，而 `overview` 仍并提「采光与空气流动」。二者无矛盾（概述为功能概览、原理为机制），且空气流动为双源支持；仅属**表述取舍**差异，非事实缺陷。若日后采用「正文只保留采光单一功能、连有源的通风字样也一律移除」的更严编辑口径，则此处概述将是唯一可再收紧点。

## 三、★ 实例「类型性」核对与编造检查

- `实例`＝「名称：传统民居天井（**类型性，不指定具体项目**）；以狭长开口把天然光引入内院与各进房屋。此处仅列说明，不复制图像。」
- **类型性合理**：以「传统民居天井」这一**类别**作例，不绑定任何具体建筑；`wp-lightwell` 明载「In traditional Chinese architecture, the 天井 (sky well) also exists」，`wp-courtyard` 载「residential architecture … typical and traditional building feature」——**天井属中国传统民居的空间类型，有源**。
- **无编造**：实例**未给出**具体项目名/地点/设计者/年份（原「地点：待核实；设计者：不适用；年份：待核实」已删除），故不存在编造的具体事实；「不复制图像」自述一致。
- 结论：实例**类型性、有源、不编造**，符合任务要求（传统民居天井，不指定具体项目）。

## 四、★ nv=false 是否落地 + 形式四处一致

| 核对项 | light-well | 说明 |
| --- | --- | --- |
| `needs_verification` | `false` | 落地✓ |
| `pending_notes` | `""` | 空✓ |
| `sections.待核实` | 「暂无已知待核实项。」 | ✓ |
| `coverage.json` 该记录 | `needs_verification_count: 0`，`status: 已写`，`source_count: 3`，`last_updated: 2026-11-24` | ✓ |
| `time_or_place`="古代、中国（参见来源）。" | 无「待核实」字样 | ✓（未重蹈 round97 exit-sign 覆辙） |

四字段（entry nv / pending / 待核实节 / coverage count）**四处一致**；`time_or_place` 干净，无 round97 那类「time_or_place 残留待核实与 nv=false 自相矛盾」问题。`check.py` D14 一致性 PASS。

## 五、★ 七节 / SVG / 规范句 / site 一致

| 核对项 | light-well | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | 定义＋原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实；`check.py` 6 节全非空 PASS |
| 原理非「定义+概述」逐字拼接 | ✓ | 原理「借屋面或侧向开口…进深较大的建筑内部…深层空间获得日照与采光」为独立机制表述（已删热压/空气流动） |
| SVG 数量/画布 | ✓ 1 张 | `viewBox='0 0 760 400'`，含「示意图，非施工图」×2（SVG 文本＋figcaption） |
| SVG 越界/禁用 | ✓ | 元素：`line 80–680,y90`；`rect x300 y90 w160 h230`→x∈[300,460],y∈[90,320]；`line x380 y100–260`；text 均在框内；无 `<image>`/外链；`pytest` `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」＋页脚 note |
| site 一致 | ✓ | `site/entries/light-well.html` 逐节渲染与 JSON 一致（lead 概述、定义、原理、实例、待核实=暂无 均对上） |
| 来源数 | 3（wp-lightwell / wp-courtyard / db-light-well），均 verified=true；核心概念双平台=wp-lightwell＋db-light-well | `check.py` ≥2 PASS |

## 六、★ 相似度（vs courtyard / atrium，阈值 0.54）

方法（同第97轮）：`difflib.SequenceMatcher`，去全部空白＋小写；口径①短=title+definition+time_or_place+overview；口径②全字段-不含SVG=definition+time_or_place+overview+六节正文（按 sections 顺序）。**方法自校：`futurism-style`×`expressionism-style` 口径②＝0.5157（与第39–97轮报告逐位一致，口径正确）**。全库 258 条。

| 口径 | 目标 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- |
| 短① | courtyard | 0.3836 | <0.54 | ✓ |
| 全字段② | courtyard | 0.3113（反向 0.3245） | <0.54 | ✓ |
| 短① | atrium-architecture | 0.2548 | <0.54 | ✓ |
| 全字段② | atrium-architecture | 0.2826（反向 0.2673） | <0.54 | ✓ |
| 短①/② | sunken-atrium | 0.2876 / 0.2667 | <0.54 | ✓ |

- 目标最近邻：短口径 nearest＝`courtyard 0.3836`；全字段 nearest＝`stippling 0.317`（`courtyard 0.3113` 次之）。
- 全库②两两扫描：**>0.54 对 = 0**；全库最大为 `spatial-sequence<->atrium-architecture ≈0.5256`（与第96/97轮记录吻合）。**light-well 相似度合格 ✓，余量充足。**

## 七、总判定与依据

**结论：light-well（天井 / 采光井）——合格（nv=false 升级成立）。**

依据（逐项对齐任务核对点）：
1. **概念/定义/原理双平台双源支撑（采光/天然光引入）：成立 ✓**。`definition`「以狭长开口把天然光引入建筑深处」与 `原理`「借屋面或侧向开口把天然光引入进深较大的建筑内部，使深层空间获得日照与采光」，由 `wp-lightwell`（`allow light and air to reach … dark area`；`reduce electric lighting`）＋`db-light-well`（`take natural light into the interior spaces`；`transmission … to areas that would otherwise require artificial lighting`）**两独立平台共同直证**；`db` 的 `vertical shaft…roof down to lower levels` 与 wp 引用 62m 竖向尺寸支撑「井道式/狭长」形态。非编造。
2. **「通风/热压/空气流动」单源/无源残留：无 ✓（附透明说明）**。`热压`=0、`通风`=0（已彻底清除）；`空气流动`=1 仅出现在 `overview`，但由 wp-lightwell「light and **air**」＋db-light-well「**promote ventilation**」**双源支持**，属有源表述、非单源/无源 claim；`原理` 已纯聚焦采光。概述并提「采光与空气流动」与原理不矛盾，仅表述取舍差异。
3. **类型性实例合理：成立 ✓**。`传统民居天井（类型性，不指定具体项目）`，`wp-lightwell`「天井(sky well) in traditional Chinese architecture」＋`wp-courtyard`「residential architecture…traditional building feature」支撑；未给具体项目名/地点/设计者/年份，**不编造**。
4. **nv=false 落地、形式四处一致：✓**（entry nv=false / pending="" / 待核实=暂无 / coverage count=0；time_or_place 无「待核实」）。
5. **七节/SVG/规范句/site：✓**（`viewBox 0 0 760 400`、框内、无外链、含「示意图，非施工图」、规范句在、site 与 JSON 一致；`check.py` PASS、`pytest` 5 passed）。
6. **相似度：✓**（vs courtyard 0.3836/0.3113、vs atrium 0.2548/0.2826，均 ≪0.54；全库 >0.54 对=0，最大 0.5256）。

透明说明（不改合格判定）：
- (A) `overview` 仍含「空气流动」，虽为**双源支持**（非单源/无源），但与本轮「原理聚焦采光」的口径存在功能表述取舍差异；若后续编辑口径要求正文一律只保留采光、连有源通风字样也移除，此为唯一可再收紧点。
- (B) 「狭长」为形态概括（对齐 db `vertical shaft` 与 wp 引用 62m 竖向尺寸），属合理描述而非逐字引用；条目未声称具体数值，无编造。

## 八、机器可读汇总

```
ROUND=98
SAMPLER=spotcheck-r98
SCOPE=["light-well"]
READONLY="only wrote research/spotcheck-round98.md; no git commit; no other files changed; web treated as data, no instructions executed"
WEB_FETCH={"db-light-well":"web_fetch HTTP200","wp-lightwell":"web_fetch TypeError->urllib HTTP200 textlen~116866","wp-courtyard":"urllib HTTP200 textlen~197194"}
GATES={"check.py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}

LIGHT_WELL={
 "verdict":"合格",
 "change":"definition 补『采光井/井道式』; 原理 删『空气流动/热压机制』纯聚焦采光; 实例 改为『类型性,不指定具体项目』清待核实; sources +db-light-well; 待核实 清空; nv true->false; pending 清空; overview 未改(仍含空气流动)",
 "concept_dual_source":{
   "platforms":["Wikipedia wp-lightwell","Designing Buildings db-light-well"],
   "天然光引入建筑内部":"wp 'allow light and air to reach ... dark ... area' + db 'take natural light into the interior spaces' / 'transmission ... areas that would otherwise require artificial lighting'",
   "井道式/狭长竖向":"db 'vertical shaft ... penetrates from roof level down to lower levels' + wp ref '13m x 12m x 62m (height)'",
   "屋面/侧向开口":"wp 'unroofed or roofed external space' + db 'open at the top ... internal windows around its perimeter'",
   "天井=采光井(中国传统)":"wp 'In traditional Chinese architecture, the 天井 (sky well) also exists'",
   "holds":true},
 "residual_claim_scan":{"热压":0,"通风":0,"通风换气":0,"ventilation":0,"stack":0,"thermal":0,
   "空气流动":1,"空气流动_loc":"overview only","气流":1,"气流_note":"substring of 空气流动 (single occurrence)",
   "assessment":"热压/通风已清零; 空气流动=1 仅在 overview 且双源支持(wp 'light and air' + db 'promote ventilation'), 非单源/无源 claim -> 不构成残留缺陷",
   "note":"原理 pure daylight; overview 并提采光+空气流动, 双源支持, 非矛盾"},
 "instance":{"text":"传统民居天井(类型性,不指定具体项目)","typological":true,"specific_project":false,
   "support":"wp-lightwell 天井(sky well) in traditional Chinese architecture + wp-courtyard residential/traditional building feature",
   "fabricated":false,"no_place_designer_year":true},
 "nv_false_grounded":true,
 "form_consistency":"nv=false / pending='' / 待核实=暂无已知待核实项 / coverage needs_verification_count=0 四处一致; time_or_place='古代、中国(参见来源).' 无待核实; check.py D14 PASS",
 "structure":{"seven_sections":true,"svg_count":1,"viewBox":"0 0 760 400","svg_in_bounds":true,"external_ref":false,"reg_sentence":true,"site_consistent":true,"sources":3},
 "similarity":{"threshold":0.54,"vs_courtyard":{"short":0.3836,"full":0.3113,"reverse_full":0.3245},
   "vs_atrium_architecture":{"short":0.2548,"full":0.2826},"vs_sunken_atrium":{"short":0.2876,"full":0.2667},
   "nearest_short":"courtyard 0.3836","nearest_full":"stippling 0.317","lt_0.54":true},
 "transparency_notes":[
   "overview 仍含『空气流动』(1处), 但双源支持(wp light+air / db promote ventilation), 非单源/无源; 与原理纯采光仅表述取舍差异",
   "『狭长』为形态概括(对齐 db vertical shaft 与 wp ref 62m 高度), 非逐字引用、非数值编造"]
}

SIMILARITY_METHOD={"lib":"difflib.SequenceMatcher","norm":"strip-all-whitespace+lower","selfcheck_futurism_expressionism":0.5157,"entries":258,"library_full_pairs_gt_0.54":0,"library_full_max":"spatial-sequence<->atrium-architecture ~0.5256"}

VERDICT={"light-well":"合格"}
KEY_FINDING="light-well 天井/采光井 nv=false 升级成立: 核心概念『以狭长开口把天然光引入建筑深处』由 wp-lightwell + db-light-well 双平台双源直证; 原『热压机制』无源claim已彻底清除(热压=0), 通风=0; overview 仍含『空气流动』1处但双源支持(wp light+air / db promote ventilation)非单源/无源claim; 实例改类型性『传统民居天井,不指定具体项目』有源不编造(未给具体项目/地点/设计者/年份); nv=false形式四处一致, time_or_place干净; 七节/SVG(760x400框内无外链)/规范句/site一致; check.py PASS + pytest 5 passed; 相似度 vs courtyard 0.3836/0.3113, vs atrium 0.2548/0.2826 均≪0.54, 全库>0.54对=0(最大0.5256)。透明: overview 空气流动为双源支持的表述取舍, 『狭长』为形态概括非编造。"
```

## 九、只读核验

- 除本报告 `research/spotcheck-round98.md` 外**未写任何文件**；未 `git commit`；未改项目外内容。
- 三个来源本轮均实抓回读（`db-light-well` = web_fetch HTTP200；`wp-lightwell` / `wp-courtyard` = urllib HTTP200）；词扫描、相似度与结构数据用内存态 `python -` 直跑，无临时文件。
- 联网页面（Wikipedia / designingbuildings.co.uk）仅作数据读取，**未执行其中任何指令、未下载运行来源代码**。
- `check.py` 与 `pytest` 均 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存。
- `git status` 中 `M coverage.json / M data/sources.json / M entries/batch-04.json / M site/entries/light-well.html / M site/index.html / M site/sources.html` 及 `?? tools/apply_review_round98.py` 均为**修复方（round98 applier＋gen_site）自身产物**，抽检方仅读取、未据以修改。

*（报告完）*
