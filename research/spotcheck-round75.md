# 第75轮 质量抽检报告（spotcheck-round75）

- 抽检人：spotcheck-r75（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 抽检对象：`complementary-colors`（互补色）、`color-contrast`（色彩对比），均在 `entries/batch-01.json`（`grep '"complementary-colors"' / '"color-contrast"'` 定位：行 957 / 行 993）。
- 本轮改动（据 `tools/apply_review_round75.py` 实读 + 当前文件实读）：两条均**升级为已验证**——实例改为具名作品梵高《夜间咖啡馆》（The Night Café，1888，耶鲁大学美术馆），新增两源 `wp-night-cafe`（Wikipedia）+ `vgm-colours`（Van Gogh Museum），`needs_verification` 置 **false**，`sections.待核实` 改「暂无已知待核实项。」`pending_notes` 清空。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round75.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时脚本 `research/_r75_*.py` 用后已 `rm -f`（`ls research/_r75*` → No such file，无残留）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**（check.py 仅校验结构/格式；史实双源与"作品是否红绿互补"由本报告独立实抓正文核验补足。）

## 一、核心命题核对：两源是否都就该作品述"红绿互补/对比"

结论先行：**两源都就该作品（《夜间咖啡馆》）述"红绿对比"，但都没有把该作品的"红绿"逐字定性为"互补/complementary"。**这是本轮的关键缺口。

| 来源 | 实抓 HTTP | 就《夜间咖啡馆》述红绿？ | 是否用"互补/complementary"定性**该作品**？ | 关键原文（本轮现抓回读） |
| --- | --- | --- | --- | --- |
| Wikipedia `wp-night-cafe` | 200（197,907 B） | **是**，强支撑 | **否**——全文 `complementary` **0 次** | ①「In **wildly contrasting**, vivid colours, the **ceiling is green, the upper walls red**」②梵高书信自述：「I have tried to express the terrible **passions of humanity by means of red and green**」③「the **clash and contrast of the most alien reds and greens**」 |
| Van Gogh Museum `vgm-colours` | 200（177,078 B） | **是**，明确点名该作品 | **否（对具体作品）**——`complementary` 全局 3 次全在通用色论段，距 Night Café 段落 >400 字符（位置 3672/4737/4990 vs 作品段 10121/10172） | ①《Night Café》段：「Vincent van Gogh, The Night Café, 1888. Yale University Art Gallery… he chose **clashing reds, greens, and yellows** – of oil lamp light and gas light, of **harmony and discord**」②通用色论段（非该作品）：「**complementary colours – red and green**, yellow and purple, blue and orange – reinforce each other」「complementary colours – positioned directly opposite each other – provide maximum colour contrast」 |

- **Wikipedia 只证"红绿强烈对比/冲突"，从不使用"互补"一词**；**VGM 只在通用理论里说"红+绿是互补色"，而具体到《夜间咖啡馆》它只写"clashing reds, greens…（harmony and discord）"即"冲突/不和谐"，未把该幅的"红绿"称为"互补"。**
- 因此"该作品使用了红绿**互补色**"这一合题，是**用 VGM 通用色论 ＋ 两源对该作红绿对比的描述**桥接推得，**无任一源就"该作品"逐字给出"红绿互补"断言**。缺口属**措辞桥接**，非虚构：红绿对比、绿顶红墙、1888、耶鲁、梵高，两源均**实打实**支撑。

## 二、definition / 实例 是否由两源正文支撑

| 条目 | definition（端内） | 是否有源支撑 | 结论 |
| --- | --- | --- | --- |
| `complementary-colors` | 「色轮上相对、并置时形成强烈对比的色彩。」 | **VGM 通用段直证**：「complementary colours – positioned directly opposite each other – provide maximum colour contrast」；旧源 `wp-complementary-colors`/`wp-color-wheel` 亦在列 | ✓ 定义有据（主要由 VGM 单源直证，Wikipedia Night Café 页不含该定义） |
| `color-contrast` | 「色彩之间在明度、色相、冷暖或纯度上的差异。」 | 旧源 `wp-color-theory`/`wp-complementary-colors` 支撑；实例由 Wikipedia「wildly contrasting」「clash and contrast」+VGM「colour contrast」支撑 | ✓ 定义有据 |

实例四要素（两条共用，均为 Night Café）：

| 要素 | 端内声明 | Wikipedia 实抓 | VGM 实抓 | 结论 |
| --- | --- | --- | --- | --- |
| 名称 | 《夜间咖啡馆》The Night Café | `The Night Café (French: Le Café de nuit)` | `Vincent van Gogh, The Night Café, 1888` | ✓ 双源确证 |
| 地点 | 美国纽黑文耶鲁大学美术馆 | `Location Yale University Art Gallery, New Haven` | `Yale University Art Gallery` | ✓ 双源确证 |
| 设计者 | 文森特·梵高 | `Dutch artist Vincent van Gogh` | `Vincent van Gogh` | ✓ 双源确证 |
| 年份 | 1888 年 | `created… in September 1888` / `1888 paintings` | `1888` | ✓ 双源确证 |

- **无编造**：四要素全部落在真实、可核的作品与人物；未见纽约/错位地点、未见凭空捏造。
- 两条实例的措辞细节：
  - `complementary-colors` 实例：「梵高在书信中明言以**红绿这对互补色**表达激情」——"以红绿表达激情（passions…by means of red and green）"**Wikipedia 书信原文直证 ✓**；但"**互补色**"三字系从 VGM 通用色论外推（该作品页未直证"互补"）。
  - `color-contrast` 实例：「以"最相异的红与绿"冲突并置制造色彩对比」——**Wikipedia「most alien reds and greens」「clash and contrast」直证 ✓**，此条表述与源最贴合。

## 三、两源独立性

- `wp-night-cafe` = **Wikipedia**（权威百科，社区编辑）；`vgm-colours` = **Van Gogh Museum 官方机构**（阿姆斯特丹梵高博物馆）。**二者编辑主体、机构性质、内容生成流程完全独立，非镜像/转引关系**（VGM 页面独立撰文，未标注引自 Wikipedia；Wikipedia 为该作独立词条）。
- **独立性成立 ✓**。此处不存在同源转发或同一数据库重复计数的问题。

## 四、needs_verification=false 是否有据

| 条目 | nv | 判定 |
| --- | --- | --- |
| `complementary-colors` | false | **基本有据但偏激进**：实例四要素与"红绿对比/梵高书信言红绿表达激情"确由双源直证，nv=false 对该层面成立；**但"该作品用红绿互补色"的"互补"定性仅由 VGM 通用色论桥接**，严格说该"合题"仍属推得而非逐字佐证。降为 false 在"实例四要素"上站得住，在"互补＝红绿"合题上略宽（详见问题①）。 |
| `color-contrast` | false | **有据**：该条实例即"红绿冲突对比"，Wikipedia「most alien reds and greens」「clash and contrast」+VGM「clashing reds, greens… harmony and discord」「colour contrast」双源直证，nv=false 合理。 |

- 与 D10/D14 的张力：D10 要求"关键事实双源或标待核实"；D14 要求"出现待核实时 nv=true"。本轮两条把原 nv（true）改 false，**对"实例四要素 + 红绿对比"层面升级为 false 是合理的（确双源）**；仅 `complementary-colors` 的"互补"合题存在措辞桥接，属可收窄项，非阻断。

## 五、结构/格式核对项（两条均查）

| 核对项 | `complementary-colors` | `color-contrast` | 依据 |
| --- | --- | --- | --- |
| 七节齐 | ✓（definition + 六节＝7） | ✓（＝7） | sections keys 6 + definition；check.py 0 报错 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；无 `on*`/`<image>`/`xlink`/`href`/`<script>` | ✓ 同左 | 脚本扫描 bad=[] |
| 规范句 | ✓「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 | ✓ 同左 | 文件实读 |
| sources 可引性 | ✓ 6 源，`wp-night-cafe`/`vgm-colours` 均 `verified=true`、`link_ok=true`（本轮实抓 200） | ✓ 6 源，同上 | sources.json 行 5932–5953 |
| 相似度（阈值0.54） | ✓ 短 0.1928（vs hue）／全 0.4804（vs color-contrast），均 <0.54 | ✓ 短 0.3043（vs contrast-principle）／全 0.4838（vs complementary-colors），均 <0.54 | `difflib.SequenceMatcher` 实算，norm=去空白小写 |

> 注：`color-contrast` 全字段最高 0.4838 是对 `complementary-colors` 的比值，二者为相邻同主题条目、共享 Night Café 实例与两源，故相似度偏高但**仍 <0.54**，判 PASS。

## 六、问题清单

1. **【重要·非阻断】"该作品红绿互补"缺逐字佐证**：两源都写《夜间咖啡馆》"红绿对比/冲突"（Wikipedia：wildly contrasting ceiling green/walls red + "most alien reds and greens" + 书信"passions…by means of red and green"；VGM："clashing reds, greens…harmony and discord"），**但没有任何一源就该作品逐字说"红绿互补/complementary"**——Wikipedia 全文 `complementary` 0 次；VGM 的 `complementary（red and green）` 仅在通用色论段、距作品段 >400 字符。`complementary-colors` 的"以红绿这对互补色"因此是把 VGM 通用色论外推到该作品。**建议**：实例措辞收窄为「以红绿冲突对比表达激情（梵高书信：red and green）；红与绿在色彩理论上为互补色」，或在待核实保留一句"该作'红绿互补'系由通用色论＋两源红绿对比描述桥接"，避免读者误以为两源对该作明言"互补"。
2. **【观察·非阻断】`complementary-colors` 的 nv=false 略激进**：实例四要素双源确证、红绿对比双源确证，但"互补"合题如上（问题①）为桥接。若从严，可将 nv 保留 true 并在待核实写明桥接缺口；若整条语义按"红绿（在色论上互补）对比"理解，则 false 可接受。**属口径取舍，非编造。**
3. **【观察·非阻断】定义支撑偏单源**：`complementary-colors` 的定义"色轮相对、并置强烈对比"在本轮两新源中**实际主要由 VGM 通用段直证**，Wikipedia Night Café 页不含该定义；另有旧源 `wp-complementary-colors`/`wp-color-wheel` 支撑，故定义不悬空，但新源层面"Wikipedia 亦证定义"并不成立。
4. **【观察·非阻断】两条高度共享实例与来源**：`complementary-colors` 与 `color-contrast` 现用同一实例（Night Café）、同一对来源，相似度全字段达 0.48（<0.54 但偏高）。可考虑 `color-contrast` 另择一更能体现"明度/冷暖对比"的实例，以拉开区分度。

> 未发现越权升级造假（人名/作品/地点/年份均真实、双源）、未发现 nv 被改成 false 却无任何来源支撑的凭空断言——缺口是"互补"定性对该作品的措辞桥接，属可收窄的准确性问题，非虚构。

## 七、总体结论

**`color-contrast`：合格（放行）** — 实例《夜间咖啡馆》四要素（名称/耶鲁-纽黑文/梵高/1888）Wikipedia 与 Van Gogh Museum 双源直证；"红绿冲突对比"两源直述（Wikipedia「most alien reds and greens / clash and contrast」+ VGM「clashing reds, greens…harmony and discord」）；定义有旧源＋theory 源支撑；nv=false 有据；七节齐、SVG 合规、规范句在位、相似度 0.3043/0.4838 <0.54。

**`complementary-colors`：待核实（可放行，附带收窄建议）** — 实例四要素与"红绿对比"双源确证、无编造、定义有据、结构全合规；**唯一缺口：无任一源就该作品逐字述"红绿互补/complementary"**（Wikipedia 0 次；VGM 的 complementary 仅通用段、未落到该作），"以红绿这对互补色"系 VGM 通用色论＋两源红绿对比描述的桥接，nv=false 在"互补"合题上略宽。**建议按问题①收窄实例措辞或补一句桥接说明后即可判合格；不构成虚构、不阻断放行语义本身。**

- **本轮 2 条：`color-contrast` 合格；`complementary-colors` 待核实（合格边缘，1 项建议改）。合计：1 合格、1 待核实、0 不合格（1 不合格项不成立，均非编造）。**

## 八、机器可读汇总

```
ROUND=75
SAMPLER=spotcheck-r75
SCOPE=["complementary-colors","color-contrast"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round74.md","entries/batch-01.json","data/sources.json","tools/apply_review_round75.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; temp research/_r75_*.py deleted after (ls _r75* none)"
FETCHES={"wp-night-cafe":200,"vgm-colours":200}
IMPLS="Van Gogh, The Night Café, 1888, Yale University Art Gallery (New Haven)"
INSTANCE_4ELEMENTS={"title":true,"location":true,"artist":true,"year":true,"dual_source":true}
RED_GREEN_ON_THIS_WORK={"wikipedia":"yes (wildly contrasting ceiling green/walls red; most alien reds and greens; letter: passions by means of red and green)","vgm":"yes (clashing reds, greens, and yellows; harmony and discord)"}
COMPLEMENTARY_LABEL_ON_THIS_WORK={"wikipedia":"NO (word 'complementary' count=0)","vgm":"NO for the work (complementary only in general colour-theory section, >400 chars away; Night Café text uses 'clashing/harmony-and-discord', not 'complementary')","gap":"neither source literally calls Night Café red-green 'complementary' about that work; synthesis bridges VGM general theory + both sources' red-green contrast"}
INDEPENDENCE={"wikipedia":"encyclopedia","vgm":"Van Gogh Museum official","independent":true,"mirror_or_reprint":false}
FABRICATION=false
NV_BASIS={"color-contrast":"solid (instance + red-green contrast dual-sourced)","complementary-colors":"mostly solid for 4 elements + red-green contrast; 'complementary' label for the work is bridged -> nv=false slightly generous"}
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 示意图非施工图 no on*/image/xlink/href/script","reg_sentence":true,"sources_verified_all":true}
SIMILARITY={"complementary-colors":{"short":0.1928,"short_vs":"hue","full":0.4804,"full_vs":"color-contrast"},"color-contrast":{"short":0.3043,"short_vs":"contrast-principle","full":0.4838,"full_vs":"complementary-colors"},"threshold":0.54,"pass":true}
ISSUES=["Q1 important: neither source literally says Night Café red-green is 'complementary' (WP 0 hits; VGM complementary only in general section) -> complementary-colors instance 'red-green complementary pair' is a bridge; non-fabricated","Q2 obs: complementary-colors nv=false slightly generous on the complementarity claim","Q3 obs: definition support leans on VGM general section; WP Night Café page lacks the definition","Q4 obs: both entries share same instance+sources; full similarity 0.48 (<0.54 but high)"]
VERDICT_color_contrast="合格"
VERDICT_complementary_colors="待核实（合格边缘，1建议改）"
TOTAL="1合格/1待核实/0不合格"
READONLY="only wrote research/spotcheck-round75.md; fetched html in-memory, temp research/_r75_*.py deleted(confirmed no residue); no entries/sources/coverage/tools/site changed; no git commit; web treated as data, no instructions executed"
```

*（报告完）*
