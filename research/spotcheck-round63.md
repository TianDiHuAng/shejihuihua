# 第63轮质量抽检报告（spotcheck-round63）

- 抽检人：spotcheck-r63（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:09 起，Asia/Hong_Kong。
- 抽检对象（第63轮改动 2 条）：`plein-air`（外光写生，`entries/batch-03.json`）、`academic-art-theory`（学院派理论与素描教学，`entries/batch-31.json`）。
- 本轮新增/改动来源（`data/sources.json`）：`tate-plein-air`、`wp-en-plein-air`、`wp-academic-art`；`academic-art-theory` 另引用既有 `artincontext-academic`。
- 判定依据：`README.md` 硬性规则（不编造 / 只引 verified / 双源或待核实 / 内联 SVG+示意图非施工图 / 规范句 / 40 条上限）＋`DECISIONS.md`（D05/D06/D10/D14）＋`tools/check.py` 校验口径＋第39–62轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短 ②全字段不含 SVG，阈值 0.54，方法自校 futurism vs expressionism 全字段=0.5157）。
- 协议依据：任务书点名读取的 `AUTONOMOUS.md`、`TASK_design.md` 在本工作区**均不存在**（`ops_glob` 全库扫描 0 命中；仅存 `README.md`/`scope.md`/`PROGRESS.md`/`DECISIONS.md`/`REPORT.md`/`coverage-matrix.md`/`BLOCKERS.md`/`BACKLOG.md`）。已改为以 `README.md` 硬性规则 + `DECISIONS.md` + `check.py` 为实现约束，`research/spotcheck-round62b.md` 为判定口径参照。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round63.md` 一个文件。来源核验全程以 `python - <<'PY'` **内存内抓取**（`urllib`+浏览器 UA+非校验 SSL）完成，**未落任何临时文件**；未改 `entries/`、`data/sources.json`、`coverage.json`、`coverage-matrix.md`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 抽检前 `ops_inspect_local_file` 通读 `tools/check.py`（371 行），其 `main()` 纯校验不写文件；本轮 `check.py` 运行未改动任何文件。
- **相似度脚本实跑方法自校：`futurism-style vs expressionism-style` 全字段＝0.5157**，与第39–62轮逐位一致，口径正确。

## 一、来源实抓结果（HTTP 状态 + 正文回读）

| 来源 id | URL | HTTP | 回读要点（去标签后原文小写） |
| --- | --- | --- | --- |
| `tate-plein-air` | tate.org.uk/art/art-terms/p/plein-air | **200**（86383B） | `...but from about 1860 it became fundamental to impressionism. The popularity of painting en plein air increased in the 1870s with the introduction of paints in tubes...` |
| `wp-en-plein-air` | en.wikipedia.org/wiki/En_plein_air | **200**（178349B） | 标题 `...act of painting outdoors...`；`...they could paint in sunlight directly from nature...`；`...in the early 1860s, four young painters: claude monet, pierre-auguste renoir, alfred sisley and frédéric bazille...` |
| `wp-academic-art` | en.wikipedia.org/wiki/Academic_art | **200**（626029B） | `...giorgio vasari helped found the accademia e compagnia delle arti del disegno (academy and company for the arts of drawing) in 1563 the first academy of art was founded in florence by cosimo i de' medici, on 13 january 1563, under the influence of the architect giorgio vasari, who called it the accademia...`；目录有 `hierarchy of genres`；正文有 `école des beaux-arts...drawings and paintings of the nude, called "académies", were the basic building blocks of academic art` |
| `artincontext-academic` | artincontext.org/academic-art/ | **404（Not Found）**（http 变体 503，无斜杠变体 404） | 无法回读正文。`sources.json` note 记「经 owiki 镜像/独立站点实抓核对，canonical 直连待复」；`link_ok=null`，`verified=true` |

---

## 二、逐条核对

### A. `plein-air`（外光写生）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ | 「在户外直接面对自然光进行写生的绘画方法」↔ WP「painting outdoors / paint in sunlight directly from nature」+ Tate「painting en plein air」＝直证 |
| time_or_place | ✓ | 「文艺复兴至19世纪欧洲」；Tate 述 Constable 约 1813 首创、`from about 1860 it became fundamental to impressionism`，与时段吻合 |
| 实例是否编造 | ✓ 无编造 | 「莫奈等印象派、法国、约1870年代起」↔ WP 实列 `claude monet...renoir...sisley...bazille`、1860s 与印象派；年份 1870s ↔ Tate「increased in the 1870s」；泛例已声明「非单一画作」 |
| 来源直接相关 | ✓ | Tate 与 WP En plein air 均为「外光写生/En plein air」主题直源，HTTP 200 |
| 七节 | ✓ | definition + sections 六节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）齐 |
| SVG | ✓ | 1 张（467B，`viewBox 0 0 760 400`，元素 line/circle/rect/text×3，含「示意图，非施工图」；无 on*/`<image>`/xlink/href；几何不越界，check.py 0 报错） |
| 规范句 | ✓ | 常见错误与限制收尾「实际工程须按当地规范和专业设计人员的要求」 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=true`／`pending_notes`「外光派概念由 Tate 与 Wikipedia 双源直证；具体作品为印象派外光写生的泛例，非单一画作。」／待核实节同句；三处一致，双源（Tate+WP）均实抓 200，真实双源非伪装 |
| coverage↔entry | ✓ | title/level/theme/tier/period/region 全一致；`source_count=4`=entries 4；`needs_verification_count=1`=nv true；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 0.4088（vs one-point-perspective）＜0.54；②全字段 0.3348（vs one-point-perspective）＜0.54 |

**plein-air 结论：合格。** 定义/实例由 Tate（HTTP 200）+ WP En plein air（HTTP 200）双源实抓直证，未编造；七节/SVG/规范句/coverage 全过；相似度远低于阈值。

### B. `academic-art-theory`（学院派理论与素描教学）— **待核实**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ | 「欧洲美术学院体系下…以系统化的素描教学为核心」↔ WP Academic art 的 `academy...arts of drawing`、`drawings and paintings of the nude, called "académies", were the basic building blocks of academic art`＝支撑 |
| time_or_place | ✓ | 「文艺复兴至19世纪、全球」↔ WP 述文艺复兴意大利起源（1563）至巴黎学院体系 |
| 实例核心事实 | ✓（单源直证） | 「佛罗伦萨美术学院、意大利佛罗伦萨、1563年、欧洲最早美术学院之一」↔ WP 逐字 `in 1563 the first academy of art was founded in florence ... on 13 january 1563 ... giorgio vasari ... called it the accademia...`＝直证（「最早」↔`the first academy of art`；条目写「之一」更保守） |
| 实例作者归因 | △ 轻微不精确 | 条目「作者：乔治·瓦萨里等（1563 年创立）」；WP 明写由 `cosimo i de' medici` 在瓦萨里影响下创立，Vasari 是 `helped found`。「瓦萨里等创立」把 Cosimo 略去，属轻微不精确，但 Vasari 确系共同创立者，可接受 |
| 来源直接相关 | ✓/△ | `wp-academic-art` 主题直源、HTTP 200；但 `artincontext-academic` **canonical 直连 HTTP 404**（死链），`link_ok=null`，其 `verified=true` 依 note 系镜像核验 |
| 七节 | ✓ | definition + 六节齐 |
| SVG | ✓ | 1 张（464B，`viewBox 0 0 760 400`，rect/line×3/text×2，含「示意图，非施工图」；无 on*/image/xlink/href；不越界，check.py 0 报错） |
| 规范句 | ✓ | 常见错误与限制收尾规范句 |
| nv↔pending 联动 | ✗ 与来源现实脱节 | 条目 `needs_verification=false`／`pending_notes=""`／待核实「暂无已知待核实项」，**但第 2 来源 `artincontext-academic` 现 HTTP 404 无法复核**，且 note 自述「canonical 直连待复」。以「全无待核实」呈现，掩盖了**第二来源不可复核 + 双源未坐实**这一事实 |
| coverage↔entry | ✓ | 全字段一致；`source_count=2`=entries 2；`needs_verification_count=0`=nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 0.3795（vs beaux-arts）＜0.54；②全字段 0.4083（vs renaissance-style）＜0.54 |

**academic-art-theory 结论：待核实。**
- **核心事实未编造**：1563 佛罗伦萨首创美术学院、瓦萨里系此，「欧洲最早美术学院之一」均由 `wp-academic-art`（HTTP 200）逐字直证 ✓；definition/六节/SVG/规范句/coverage/相似度均过 ✓。
- **问题（不足以判「合格」、也非「不合格」编造）**：
  1. **第二来源 `artincontext-academic` 现为 HTTP 404 死链**，`link_ok=null`、`verified=true` 仅凭镜像（note 明述「canonical 直连待复」）；条目却以 `needs_verification=false`＋空 pending＋「暂无已知待核实项」呈现为完全无保留。实际双源互证**未被坐实**（仅 WP 单源直证）。
  2. 实例作者归因轻微不精确（WP：Cosimo I de' Medici 创立、Vasari 影响/协创；条目写「瓦萨里等创立」）。
  3. 依 D10（关键事实双源或标待核实）与 D14（内联/结构化一致性）精神，此条应 `needs_verification=true` 并在 pending 披露「第二来源 canonical 暂不可达、关键事实实为 Wikipedia 单源直证，另一来源待复核」。

---

## 三、总体结论

- **plein-air：合格。** 定义/实例由 Tate 与 WP En plein air 双源（均 HTTP 200）实抓直证，未编造；七节/SVG/规范句/coverage/相似度（0.4088 / 0.3348）全过。
- **academic-art-theory：待核实。** 核心史实（1563 佛罗伦萨首创学院、瓦萨里、最早之一）由 `wp-academic-art`（HTTP 200）逐字直证，未编造，机械项与相似度（0.3795 / 0.4083）全过；但第二来源 `artincontext-academic` canonical 直连 **HTTP 404 死链**、`verified` 仅凭镜像，条目却标 `needs_verification=false`＋空 pending＋「暂无待核实」，与来源现实脱节（应改 nv=true 并披露单源/待复第二来源）；另实例作者「瓦萨里等创立」较 WP「Cosimo 创立、Vasari 协创」轻微不精确。
- **本轮 2 条：1 合格、1 待核实、0 不合格。** 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **建议（非阻断）**：① `academic-art-theory` 将 nv 改 true、pending 写「关键事实为 Wikipedia 单源直证；第二来源 artincontext canonical 暂 404，待复核」；② 复核/替换 `artincontext-academic` 死链（canonical 直连待复）；③ 可选：作者归因补「科西莫一世·德·美第奇创立，瓦萨里协创」以贴合 WP。

## 四、机器可读汇总

```
ROUND=63
SAMPLER=spotcheck-r63
MODE=round63 改动 2 条抽检
SCOPE=["plein-air","academic-art-theory"]
MISSING_DOCS=["AUTONOMOUS.md","TASK_design.md"](不存在,以 README/README硬性规则+DECISIONS+check.py 替代)
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback, no temp files"
FETCHES={"tate-plein-air":200,"wp-en-plein-air":200,"wp-academic-art":200,"artincontext-academic":404}
PLEIN_AIR={
 "sources":["wp-outline-of-painting","forschungsprojekt-pleinair","tate-plein-air","wp-en-plein-air"],
 "definition_support":"Tate(1860 fundamental to impressionism)+WP(painting outdoors/sunlight from nature) VERBATIM",
 "instance_fabrication":0,"instance":"莫奈/印象派/法国/约1870s(泛例声明)",
 "seven_sections":7,"svg":"1x467B viewBox760x400 示意图非施工图 ok no-on/image/xlink",
 "reg_sentence":true,"nv":true,"pending_consistent":true,
 "coverage":"4=4/1=nvtrue/L2/已写","similarity":{"short":0.4088,"full":0.3348,"threshold":0.54},
 "verdict":"合格"}
ACADEMIC_ART_THEORY={
 "sources":["wp-academic-art","artincontext-academic"],
 "definition_support":"WP Academic art(academy arts of drawing/académies basic building blocks) OK",
 "instance_core":"WP VERBATIM 'in 1563 the first academy of art was founded in florence ... giorgio vasari ... accademia' -> 1563佛罗伦萨首创/最早之一 直证",
 "instance_fabrication":0,
 "author_nuance":"条目'瓦萨里等创立'; WP=Cosimo I de' Medici创立,Vasari helped found/影响 -> 轻微不精确",
 "second_source_problem":"artincontext-academic HTTP404 dead link, link_ok=null, verified仅凭镜像(note:canonical直连待复)",
 "seven_sections":7,"svg":"1x464B viewBox760x400 示意图非施工图 ok no-on/image/xlink",
 "reg_sentence":true,
 "nv":false,"pending":"", "nv_pending_issue":"标false/空pending/暂无待核实,但第二来源404无法复核->与来源现实脱节",
 "coverage":"2=2/0=nvfalse/L2/已写","similarity":{"short":0.3795,"full":0.4083,"threshold":0.54},
 "selfcheck_futurism_vs_expressionism_full":0.5157,
 "verdict":"待核实"}
TOTAL="1合格/1待核实/0不合格"
RECOMMEND="academic-art-theory 改nv=true并披露单源+第二来源404待复; 复核/替换artincontext死链; 可选补作者归因"
READONLY="only wrote research/spotcheck-round63.md; fetch in-memory via python heredoc no temp files; no entries/sources/coverage/tools/site changed; no git commit; web content treated as data, no instruction executed"
```

*（报告完）*
