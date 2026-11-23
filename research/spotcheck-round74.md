# 第74轮 质量抽检报告（spotcheck-round74）

- 抽检人：spotcheck-r74（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 抽检对象：`trompe-loeil`（错视画 Trompe-l'œil），在 `entries/batch-41.json` 第 36 行条目（`grep "trompe-loeil"` 定位）。
- 本轮改动（据 `tools/apply_review_round74.py` 与当前文件实读）：实例从「类型性描述」改为**具名作品** Pozzo《圣依纳爵的荣耀》（Sant'Ignazio，1685–97）；新增 `wga-pozzo` 第二平台佐证作者/年代；保留 `needs_verification=true`（技法具体描述仍单源）。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言）。
- 权威事实源：本轮以**当前文件实读 + 独立实抓**为准（证据优先级：实抓 > 当前文件 > 旧报告）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round74.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时脚本 `research/_r74_verify.py` 用后已 `rm -f`（`ls research/_r74*` 无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**（check.py 只校验结构/格式；史实双源由本报告正文独立核验补足。）

## 一、实例四要素核对（Pozzo / Sant'Ignazio / 1685–97）

| 要素 | 端内声明 | 独立实抓（本轮现抓 HTTP 200 + 正文回读） | 结论 |
| --- | --- | --- | --- |
| 作者 Pozzo | 安德烈亚·波佐（Andrea Pozzo） | **Wikipedia Andrea Pozzo**：「His masterpiece is the nave ceiling of the Church of Sant'Ignazio in Rome」；**WGA**：「POZZO, Andrea Italian painter (1642, Trento - 1709, Vienna)…Paintings in Sant'Ignazio, Rome」 | ✓ 双源确证 |
| 地点 Sant'Ignazio | 意大利罗马圣依纳爵教堂 | Wikipedia：`Sant'Ignazio in Rome`；WGA：`Paintings in Sant'Ignazio, Rome`；Wikipedia Trompe-l'œil：`Sant'Ignazio in Campo Marzio` | ✓ 双源确证 |
| 作品《圣依纳爵的荣耀》 | Apotheosis of St Ignatius（中殿天顶画） | **Wikipedia Trompe-l'œil**：「Andrea Pozzo's **Apotheosis of St Ignatius** on the ceiling of the Roman church of Sant'Ignazio」；Wikipedia Andrea Pozzo：「nave ceiling…quadratura…illusion of three-dimensional space」 | ✓ 确证（且为天顶画/quadratura 错视，与端内「假穹顶在平顶上制造天顶错视」一致） |
| 年份 1685–1697 | 1685–1697 年 | **WGA**：「Paintings in Sant'Ignazio, Rome (**1685-97**)」 → 与"1685–97"字面一致；**但 Wikipedia Andrea Pozzo** 明确天顶画为「painted between **1685–1694**」；同页 1697 指「asked to build…**altars**…in the apse」（祭坛，非天顶画） | ⚠ **部分有据/存轻微口径偏差**（见问题①） |

- **无编造**：四要素均落在真实、可核的作品与人物；实例中不含「纽约/New York」等错位表述（脚本 `fabric` 检查均 False）。**未见越权升级或凭空捏造。**
- 关键否证/差异（本轮独立发现）：**天顶画的完成年，Wikipedia 作 1685–1694，端内与 WGA 作 1685–1697。**「1697」在 Wikipedia 对应的是该教堂**祭坛**工程，而非天顶画本身。端内的「1685–1697」等于把"该教堂波佐壁画/相关作品"的 WGA 笼统区间（1685-97）套用到了"天顶画"这一具体对象上。属**区间口径混用**，非虚构日期（有 WGA 字面支撑），但严格说天顶画结束年应以 1694 更准。

## 二、needs_verification / pending / 待核实 披露一致性（技法单源）

| 核对项 | 实读 | 结论 |
| --- | --- | --- |
| `needs_verification` | `true` | ✓ 保留 |
| `pending_notes` | 「技法具体描述待补第二独立专述；作者/年代已两平台佐证。」 | ✓ 如实（技法仍单源，作者/年代双平台） |
| `sections.待核实` | 「作品作者与年代（Pozzo 1685–97 Sant'Ignazio）由 Wikipedia 与 Web Gallery of Art 两平台佐证；"假穹顶错视"技法的具体描述以 artincontext 等为主，待补第二独立专述。」 | ✓ 与 pending_notes 语义一致，且如实点明技法单源 |
| `coverage.json` 对应 | `source_count=4`、`needs_verification_count=1`、`status=已写`、title/theme/tier/period/region/level 一致 | ✓ 三处联动一致 |

- 结论：**needs_verification=true 的设置与 pending 披露如实、未越权降级**。技法具体描述仍单源（artincontext/designingbuildings 为同一知识点），保留 nv=true 是诚实做法，符合 README 规则 3 与 D10/D14。

## 三、结构/格式核对项

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| 七节齐 | ✓ | `definition` + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝ 7；check.py 0 报错 |
| SVG | ✓ | 1 张，`viewBox '0 0 760 400'`，rect/polygon/text，含「示意图，非施工图」；无 `on*=`、无 `<image>`/xlink/href/`<script>` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位（脚本 `reg_sentence=True`） |
| sources 可引性 | ✓ | `wp-trompe-loeil`/`artincontext-trompe`/`designingbuildings-trompe`/`wga-pozzo` 均 `verified=true`；`wga-pozzo` `link_ok=true`（本轮实抓 200） |
| 相似度（阈值 0.54） | ✓ | ①短最高 **0.2564**（vs picturesque）＜0.54；②全字段最高 **0.3281**（vs foreshortening）＜0.54（`difflib.SequenceMatcher` 实算，norm=去空白小写） |

## 四、来源独立实抓记录（本轮现抓，HTTP + 正文回读）

| 来源 | URL | HTTP | 大小 |
| --- | --- | --- | --- |
| Wikipedia Andrea Pozzo | https://en.wikipedia.org/wiki/Andrea_Pozzo | **200** | 223,990 B |
| Wikipedia Trompe-l'œil | https://en.wikipedia.org/wiki/Trompe-l%27%C5%93il | **200** | 416,462 B |
| WGA Andrea Pozzo | https://www.wga.hu/html_m/p/pozzo/index.html | **200** | 5,210 B |

- `wga-pozzo` 的 `note`（"波佐 1642–1709，罗马 Sant'Ignazio 壁画 1685–97"）与 WGA 页面正文「POZZO, Andrea Italian painter (1642, Trento - 1709, Vienna)…Paintings in Sant'Ignazio, Rome (1685-97)」**逐字吻合**，note 未虚标。

## 五、问题清单

1. **【轻微·非阻断】天顶画年份口径**：端内实例「年份：1685–1697 年」把 WGA 的"该教堂作品 1685-97"套到"天顶画"上；Wikipedia Andrea Pozzo 明确**天顶画 1685–1694**，1697 实指**祭坛**。建议把实例年份改为「1685–1694（天顶画；WGA 作 1685–97 概括该教堂作品）」或类似限定，以消除口径混用。**不构成编造**（有 WGA 字面支撑），但严格准确性可再收窄。
2. **【观察】待核实节措辞**：现写「作品作者与年代（Pozzo 1685–97…）由 Wikipedia 与 Web Gallery of Art 两平台佐证」，其中"年代"的 Wikipedia 侧实为 1685–1694、WGA 侧为 1685–97；两平台**对终点年并不完全一致**，措辞"两平台佐证"对"1697"略宽。可与问题①一并微调。
3. **【观察·非阻断】技法仍单源**：`needs_verification=true` 保留合理，属诚实标注，无越权。

> 未发现越权升级（如把 nv 改 false、把单源技法写死为定论）或编造人名/作品/地点。改动整体朝"具名实例 + 第二平台佐证 + 诚实保留待核实"方向，符合规则。

## 六、总体结论

**`trompe-loeil`：合格（放行）** — 四要素 Pozzo / Sant'Ignazio / 《圣依纳爵的荣耀》/ 1685–(94) 均有 Wikipedia(Andrea Pozzo + Trompe-l'œil) 与 WGA 佐证，非编造；`needs_verification=true` 与 `pending_notes`/`待核实`/`coverage` 三处一致、如实披露技法单源；七节齐、SVG 合规、规范句在位；相似度 0.2564/0.3281 均低于 0.54。

- 唯一需留意：**天顶画终点年 1685–1697 与 Wikipedia 的 1685–1694 存在口径偏差**（1697 实为祭坛），属轻微、可后续收窄，不阻断放行。
- **本轮 1 条：1 合格、0 待核实、0 不合格（附 1 项轻微建议改）。**

## 七、机器可读汇总

```
ROUND=74
SAMPLER=spotcheck-r74
SCOPE=["trompe-loeil"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round72b.md","README.md 硬性规则","tools/check.py","tools/apply_review_round74.py","entries/batch-41.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r74_verify.py deleted after (ls _r74* none)"
FETCHES={"wp-andrea-pozzo":200,"wp-trompe-loeil":200,"wga-pozzo":200}
FOUR_ELEMENTS={"Pozzo":true,"Sant'Ignazio":true,"Apotheosis title":true,"year_1685-97":"partial (1685 side ok; end-year 1697 vs WP 1694 for ceiling; 1697 refers to altars)"}
FABRICATION=false
NV_DISCLOSURE={"needs_verification":true,"pending_notes":"技法具体描述待补第二独立专述；作者/年代已两平台佐证","待核实_consistent":true,"coverage_nvc":1,"coverage_source_count":4}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 rect/polygon/text 示意图非施工图 no on*/image/xlink/href/script","reg_sentence":true,"sources_verified_all":true}
SIMILARITY={"short":0.2564,"short_vs":"picturesque","full":0.3281,"full_vs":"foreshortening","threshold":0.54,"pass":true}
ISSUES=["Q1 minor: instance year 1685-1697 conflates WGA general 1685-97 with ceiling; WP says ceiling 1685-1694, 1697=altars","Q2 obs: 'two-platform corroboration' for 1697 end-year slightly wide","Q3 obs: technique still single-source, nv=true honest"]
VERDICT="合格"
TOTAL="1合格/0待核实/0不合格"
READONLY="only wrote research/spotcheck-round74.md; fetched html in-memory, temp research/_r74_verify.py deleted(confirmed); no entries/sources/coverage/tools/site changed; no git commit; web treated as data, no instructions executed"
```

*（报告完）*
