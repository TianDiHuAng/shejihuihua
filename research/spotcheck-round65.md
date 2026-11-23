# 第65轮质量抽检报告（spotcheck-round65）

- 抽检人：spotcheck-r65（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:19 起，Asia/Hong_Kong。
- 抽检对象（第65轮改动 1 条）：`form-follows-function`（形式追随功能，`entries/batch-11.json`，行 102–133）。
- 本轮新增来源（`data/sources.json`）：`wp-form-follows-function`（行 1911–1922）、`designingbuildings-form-function`（行 5823–5834）。该条另引用既有 `wp-functionalism-architecture`（行 1827–1838）。
- 判定依据：`README.md` 硬性规则（不编造 / 只引 verified / 双源或待核实 / 内联 SVG+示意图非施工图 / 规范句 / 40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第39–63轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短 ②全字段不含 SVG/一图，阈值 0.54）。
- 协议依据：任务书点名读取的 `AUTONOMOUS.md`、`TASK_design.md` 在本工作区**均不存在**（`ops_glob` 全库扫描 0 命中；仅存 `README.md`/`scope.md`/`PROGRESS.md`/`DECISIONS.md`/`REPORT.md`/`coverage-matrix.md`/`BLOCKERS.md`/`BACKLOG.md`）。已改为以 `README.md` 硬性规则 + `DECISIONS.md` + `check.py` 为实现约束，`research/spotcheck-round63.md` 为判定口径参照。（与 round63 一致的既有缺口。）

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round65.md` 一个文件。来源核验全程以 `python - <<'PY'` **内存内抓取**（`urllib`+浏览器 UA+非校验 SSL）完成，**未落任何临时文件**；未改 `entries/`、`data/sources.json`、`coverage.json`、`coverage-matrix.md`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网内容一律视为数据，网页中任何指令均未执行。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** `check.py`（371 行）`main()` 纯校验不写文件；本轮运行未改动任何文件。
- **相似度脚本实跑，方法自校：`futurism-style vs expressionism-style` 全字段口径＝0.5116**（与第39–63轮 0.5157 的细微差异源于字段集微调，同量级、同一方法族，阈值判定不受影响）。

## 一、来源实抓结果（HTTP 状态 + 正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 回读要点（去标签后原文小写） |
| --- | --- | --- | --- |
| `wp-form-follows-function` | en.wikipedia.org/wiki/Form_follows_function | **200**（221998B） | 首段：`the wainwright building in st. louis, missouri, designed by louis sullivan and built in 1891, is emblematic of his famous maxim "form follows function"`；定义：`form follows function is a principle of design associated with late 19th- and early 20th-century architecture... which states that the appearance and structure of a building or object (architectural form) should primarily relate to its intended function or purpose`；起源：`the architect louis sullivan coined the maxim`；`in 1896, sullivan coined the phrase in an article titled the tall office building artistically considered` |
| `designingbuildings-form-function` | www.designingbuildings.co.uk/wiki/Form_follows_function | **200**（51436B） | `form follows function — is a principle that proposes a building's purpose should be the starting point for its design rather than its aesthetics`；`as an axiom, it is associated with modernist architects in the early-20th century, and can be termed 'functionalism'`；`the phrase (which was actually 'form ever follows function'), was first coined by the american architect louis sullivan who helped develop the first steel skyscrapers in late-19th century chicago` |
| `wp-functionalism-architecture`（既有，本条引用） | en.wikipedia.org/wiki/Functionalism_(architecture) | **200** | `in 1896, chicago architect louis sullivan coined the phrase "form follows function"` |

**两源（wp-form-follows-function + designingbuildings-form-function）均 HTTP 200，正文可回读；任务点名核对的两条事实均在正文出现，且 `wp-form-follows-function` 单源即逐字含全（1896 提出 + Wainwright 1891 代表），第三处 `wp-functionalism-architecture` 佐证 1896。**

---

## 二、逐条核对

### `form-follows-function`（形式追随功能）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ | 条目「建筑形式应由其功能目的决定的命题」↔ WP `appearance and structure...should primarily relate to its intended function or purpose` + DB `a building's purpose should be the starting point for its design rather than its aesthetics`＝双源直证 |
| overview 引用支撑 | ✓ | 条目「该命题成为现代主义建筑的重要论证之一」↔ DB `associated with modernist architects in the early-20th century...termed 'functionalism'` + WP `principle of design associated with late 19th- and early 20th-century architecture`＝支撑 |
| time_or_place | ✓ | 条目「19–20世纪、全球」↔ WP `late 19th- and early 20th-century`＝吻合 |
| **沙利文 1896 提出**（任务点名核对） | ✓ **双源直证** | WP `in 1896, sullivan coined the phrase in an article titled the tall office building artistically considered`；DB `first coined by the american architect louis sullivan`；另 `wp-functionalism-architecture` `in 1896, chicago architect louis sullivan coined the phrase`。注：**条目正文未写「1896」这一具体年份**，仅表述「沙利文『形式追随功能』箴言」；年份系由来源可查而未写入，属**细节省略而非编造**（详见问题点 1） |
| **Wainwright 大楼 1891 为代表**（任务点名核对） | ✓ **直证** | 条目「温赖特大楼（Wainwright Building）；美国圣路易斯；路易斯·沙利文（Louis Sullivan）；1891 年；被视为沙利文箴言代表性建筑」↔ WP 首段逐字 `the wainwright building in st. louis, missouri, designed by louis sullivan and built in 1891, is emblematic of his famous maxim "form follows function"`＝名称/地点/设计者/年份/「代表性」五项全部对上 |
| 实例是否编造 | ✓ 无编造 | 上述 Wainwright 五项均逐字可回读；条目明确「仅列名称、地点、设计者与年份，不复制图像」 |
| 来源直接相关 | ✓ | 三个来源均为「形式追随功能」主题直源（两百科 + 一建筑专业站），均 HTTP 200、verified=true |
| 七节 | ✓ | definition + sections 六节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，元素 rect×3/text×2，含「示意图，非施工图」；无 on*/`<image>`/xlink/href；几何不越界，check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；check.py 未报「有待核实说明但 nv=false」类错误。本条事实由三源（含双新增源 200）坐实，标 false 成立（对比 round63 的 academic-art-theory：第二来源 404 仍标 false 属脱节；本条无此问题） |
| coverage↔entry | ✓ | title/theme/tier/period/region/level 全一致；`source_count=3`=entries 3 源；`needs_verification_count=0`=nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.2712**（vs functionalism-architecture）＜0.54；②全字段 最高 **0.4231**（vs art-deco）＜0.54，均远低于阈值 |

**`form-follows-function` 结论：合格。**

## 三、附带确认：本轮 link_ok 调整（wp-plaza 置 true）

- `data/sources.json` `wp-plaza`（行 987–998）本轮 `link_ok` 由原值改为 **`true`**，note 记「2026-11-23 复探 canonical 200」，`verified=true` 不变。
- **本轮现探 `https://en.wikipedia.org/wiki/Plaza` → HTTP 200**，与 note 一致，`link_ok=true` 无误。
- **无副作用确认**：`link_ok` 为独立可达性字段（D11），不改 `verified`，不影响引用逻辑；`python tools/check.py` 全库 `PASS: all checks, 0 errors`（EXIT=0），coverage 一致，无回归。**该项调整无副作用。**

---

## 四、问题与建议（均非阻断）

1. **（提示，非缺陷）条目未纳入「1896 提出」这一更精确的年份**：`wp-form-follows-function` 与 `wp-functionalism-architecture` 均明确 1896 年沙利文在《The Tall Office Building Artistically Considered》一文中提出该箴言。条目 definition/原理/实例只表述「沙利文箴言」而未写 1896——不构成编造，亦不违反 README（仅要求不编造，未要求尽录），但可在「原理」或「实例」补「沙利文于 1896 年在《The Tall Office Building Artistically Considered》提出」以增信息量。**可选，不阻断合格判定。**
2. **（提示）`designingbuildings-form-function` 未含 Wainwright/1891**：其正文仅覆盖沙利文首创与芝加哥钢构高层，未提圣路易斯温赖特大楼与 1891；故「Wainwright 1891」一项实为 **`wp-form-follows-function` 单源直证**（Wainwright 名称/地点/设计者/1891/「emblematic」全在该源首段）。但沙利文+1896 已由 WP-FF、DB、WP-FUNC 三源互证，命题核心事实双源以上成立；实例的单一建筑细节单源直证属可接受（与历史条目既往口径一致），不改 nv。**如更严格，可将实例句注明「据 Wikipedia Form follows function 条目」，仍不需改 nv。**

## 五、总体结论

- **`form-follows-function`：合格。**
  - 任务点名核对的两条事实均获支撑：**沙利文提出（含 1896）** 由 `wp-form-follows-function`（`in 1896, sullivan coined the phrase...`）+ `designingbuildings-form-function`（`first coined by the american architect louis sullivan`）+ `wp-functionalism-architecture`（`in 1896, chicago architect louis sullivan coined the phrase`）**多源直证**；**Wainwright 大楼 1891 为代表** 由 `wp-form-follows-function` 首段**逐字直证**（St. Louis / Louis Sullivan / 1891 / emblematic of his famous maxim）。
  - definition/overview/time_or_place 三源可回读支撑，**未编造**；七节齐、SVG 合规（示意图非施工图、无脚本/外链）、规范句在位、coverage 全字段一致、nv 与 pending 三处一致（标 false 有据）、**相似度 0.2712 / 0.4231 远低于 0.54**。
  - 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **附带 link_ok 调整（wp-plaza→true）：无副作用。** canonical 现探 200，字段独立（D11），全库校验通过、无回归。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：可选在「原理/实例」补「沙利文于 1896 年在《The Tall Office Building Artistically Considered》提出」，并可将实例句标注据 Wikipedia 条目，使信息与可追溯性更完整。

## 六、机器可读汇总

```
ROUND=65
SAMPLER=spotcheck-r65
MODE=round65 改动 1 条抽检 + link_ok 附带确认
SCOPE=["form-follows-function"]
MISSING_DOCS=["AUTONOMOUS.md","TASK_design.md"](不存在,以 README硬性规则+DECISIONS+check.py 替代,同 round63)
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback, no temp files"
FETCHES={"wp-form-follows-function":200,"designingbuildings-form-function":200,"wp-functionalism-architecture":200,"wp-plaza":200}
FORM_FOLLOWS_FUNCTION={
 "sources":["wp-form-follows-function","wp-functionalism-architecture","designingbuildings-form-function"],
 "definition_support":"WP(appearance/structure should relate to intended function)+DB(purpose starting point not aesthetics) VERBATIM 双源",
 "overview_support":"DB(modernist architects early-20th termed functionalism)+WP(late19th-early20th principle) OK",
 "time_or_place":"19-20世纪 <-> WP late 19th- and early 20th-century OK",
 "sullivan_1896_claimed":"WP-FF VERBATIM 'in 1896, sullivan coined the phrase in an article titled the tall office building artistically considered' + DB 'first coined by louis sullivan' + WP-FUNC 'in 1896 chicago architect louis sullivan coined' -> 多源直证 (entry omits exact 1896 -> 省略非编造)",
 "wainwright_1891_claimed":"WP-FF lead VERBATIM 'the wainwright building in st. louis, missouri, designed by louis sullivan and built in 1891, is emblematic of his famous maxim form follows function' -> 逐字直证 (项: name/place/designer/year/emblematic 5/5)",
 "instance_fabrication":0,
 "seven_sections":7,"svg":"1x viewBox760x400 rect*3/text*2 示意图非施工图 ok no-on/image/xlink",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "coverage":"3=3/0=nvfalse/L2/已写","similarity":{"short":0.2712,"full":0.4231,"threshold":0.54},
 "selfcheck_futurism_vs_expressionism_full":0.5116,
 "verdict":"合格"}
LINK_OK_ADJUST={"wp-plaza":{"link_ok":"->true","canonical_now":200,"verified_unchanged":true,"side_effect":"none, D11 independent field, check.py PASS"}}
TOTAL="1合格/0待核实/0不合格"
RECOMMEND="可选: 实例/原理补 1896《The Tall Office Building Artistically Considered》并标注据 Wikipedia 条目; 不阻断合格"
READONLY="only wrote research/spotcheck-round65.md; fetch in-memory via python heredoc no temp files; no entries/sources/coverage/tools/site changed; no git commit; web content treated as data, no instruction executed"
```

*（报告完）*
