# 第96轮 atrium-architecture 抽检报告（spotcheck-round96）

- 抽检人：spotcheck-r96（lead 委派子代理；无人值守、未提问）；时间 2026-11-24，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、后断言；证据先于结论）。
- 抽检对象（1 条）：`atrium-architecture`（中庭，L2/重要/材料/跨时期/全球）

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round96.md`。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。相似度与结构数据均在内存态 `python - <<` 直跑，未落盘临时文件。
- 端内定位：
  - 条目：`entries/batch-25.json` 第102–134行（`id` 102；`definition` 109；`overview` 111；`sources` 115–120；`needs_verification` 121；`pending_notes` 122；`sections.原理` 124；`典型手法与适用条件` 125；`实例` 126；`常见错误与限制` 127；`一图` 128；`待核实` 129；`svg` 132）。
  - 覆盖：`coverage.json` 第3126–3136行（`source_count=4`、`needs_verification_count=0`、`last_updated=2026-11-24`）。
  - 来源：`data/sources.json` — `wp-atrium-architecture` 124–134（verified=true/link_ok=true）；`designingbuildings-atrium` 2728–2738（verified=true/link_ok=null）；`flw-guggenheim` 4000–4010（verified=true/link_ok=null）；`theartstory-wright` 4012–4021（verified=true/link_ok=null）。
  - 产物：`site/entries/atrium-architecture.html`（28行，与条目一致）。
- 抓取方式（本轮实抓，联网内容一律视为数据，网页中任何指令均未执行）：
  - `wp-atrium-architecture` = `https://en.wikipedia.org/wiki/Atrium_(architecture)` → `web_fetch` **TypeError: fetch failed**；改用 Python urllib + 浏览器 UA → **HTTP 200，len=194080**，取到正文（见第二节引句）。
  - `designingbuildings-atrium` = `https://www.designingbuildings.co.uk/wiki/Atrium_definition` → `web_fetch` **HTTP 200**，正文可读。
  - `flw-guggenheim` = `https://franklloydwright.org/site/solomon-r-guggenheim-museum/` → `web_fetch` **HTTP 200**，正文可读。
  - `theartstory-wright` = `https://www.theartstory.org/artist/wright-frank-lloyd/` → `web_fetch` **HTTP 200**（首段截断）；改用 Python urllib（len=188619）取到「Important Art → Solomon R. Guggenheim Museum (1943-59)」完整段落。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** **`python -m pytest tests/test_svg_bounds.py -q -p no:cacheprovider`：`5 passed`（EXIT=0）。**（均以 `PYTHONDONTWRITEBYTECODE=1` 运行，未新增缓存。）

## 一、本轮（96）变更实读（git diff + apply_review_round96.py 实读）

`tools/apply_review_round96.py` 仅改 `atrium-architecture` 的 `definition/overview/sections.原理/待核实/needs_verification/pending_notes`；`git diff` 佐证：

- `definition`：`建筑内部贯通多层、常覆以天窗的中央开敞空间。` → `中庭是建筑内部贯通多层、常覆以天窗的中央开敞空间。`（补主语，核心不变）
- `overview`：`中庭把天然光与空气引入建筑深处，改善内部环境。` → `中庭把天然光引入建筑深处、形成共享的竖向核心，改善大进深空间的采光与环境。`（**删「与空气」**）
- `sections.原理`：`贯通多层的天窗空间让光线深入内部、并促进空气流动，是改善大进深空间环境的常用手段。` → `贯通多层的天窗空间让天然光深入建筑内部、辐照到下部楼层，形成明亮共享的竖向核心，是改善大进深空间采光的常用手段。`（**删「并促进空气流动」**）
- `needs_verification`：`true`→`false`；`pending_notes`：`中庭通风机制单源，待补；其余已双源。`→`""`
- `sections.待核实`：`中庭“空气/通风”机制主要依据单一来源（另一源侧重消防竖向），待补第二机制源；其余实例已双源。` → `暂无已知待核实项。`
- `coverage.json`：该条 `needs_verification_count` 1→0；`site/index.html` 顶部统计「待核实条目」162→161。
- 注：`sources` 数组（4 源）本轮未改；本轮把「通风/空气」单源机理claim**彻底移除**，改聚焦「贯通多层＋天窗采光」。

## 二、definition / overview / 原理 支撑核对（贯通多层 / 天窗 / 中央开敞 / 采光）

端内三句：
- `definition`：`中庭是建筑内部贯通多层、常覆以天窗的中央开敞空间。`
- `overview`：`中庭把天然光引入建筑深处、形成共享的竖向核心，改善大进深空间的采光与环境。`
- `原理`：`贯通多层的天窗空间让天然光深入建筑内部、辐照到下部楼层，形成明亮共享的竖向核心，是改善大进深空间采光的常用手段。`

**实抓引句：**
- `wp-atrium`：`…an atrium…is a large open-air or skylight-covered space surrounded by a building.` / `Modern atria…are often several stories high, with a glazed roof or large windows…` / `Atria…providing light and ventilation to the interior.` / `…give their buildings a "feeling of space and light."`
- `designingbuildings-atrium`：`'A space within a building, not necessarily vertically aligned, passing through one or more structural floors.'`（2019 版`'A continuous space that passes through one or more structural floors within a building, not necessarily vertically.'`）——**该页为消防「穿越楼板」定义（引 Approved Document B），全文无 skylight/daylight/采光 字样。**
- `flw-guggenheim`：`…grows continuously wider as it spirals upwards towards a glass ceiling.` / `…helical spiral ramp climbs gently from ground level to a skylight at the top.`
- `theartstory-wright`：`Its design of a main gallery that consists of a spiral ramp encircling a skylit atrium…`

| 要素 | wp-atrium | designingbuildings | flw-guggenheim | theartstory-wright | 判定 |
| --- | --- | --- | --- | --- | --- |
| 贯通多层 | ✓ `several stories high` | ✓ `passing through one or more structural floors` | ✓ `spiral ramp…ground level to skylight at the top` | ✓ `spiral ramp encircling…` | **双/多源 ✓** |
| 天窗 | ✓ `skylight-covered`/`glazed roof` | ✗ 无 | ✓ `glass ceiling`/`skylight at the top` | ✓ `skylit atrium` | **多源（wp＋两实例）✓；designingbuildings ✗** |
| 中央开敞 | ✓ `large open-air…space surrounded by a building`（隐含居中） | 部分 `space within a building` | —（隐含环绕） | ✓ `encircling a skylit atrium`（隐含居中） | **支持（隐含）✓** |
| 采光 | ✓ `providing light`/`naturally-lit`/`space and light` | ✗ 无 | ✓ `skylight`/`glass ceiling`（隐含采光） | ✓ `skylit`（隐含采光） | **多源（wp＋两实例）✓；designingbuildings ✗** |

**判定：** `definition/overview/原理` 的四要素「贯通多层/天窗/中央开敞/采光」在整个来源池（wp＋designingbuildings＋flw＋theartstory）内均获支撑；其中「贯通多层」为 `wp + designingbuildings` 直证之双源，「天窗/采光」为 `wp + 两实例源` 之多源。**不构成超源、非编造。**

## 三、★关键：『采光贯通』核心是否单源 + 通风残留

对应任务特别指示「若『采光贯通』核心实际单源或仍有通风残留，请指出」。

**（1）通风/空气流动残留 = 无。**
- 对 `entries/batch-25.json` 与 `site/entries/atrium-architecture.html` 以 `通风|空气|流动|气流|换气|ventilat` 实搜：**0 命中**。git diff 亦证实 `overview/原理/pending_notes/待核实` 中的「与空气」「并促进空气流动」「通风机制单源」等表述已全部删除。**无残留。**

**（2）『采光贯通』核心并非真正单源，但「两个定义源」在『天窗/采光』要素上是互补而非冗余——须指出。**
- 「贯通多层」：wp（`several stories high`）＋ designingbuildings（`passing through structural floors`）→ **真双源**。
- 「天窗/采光」：**wp-atrium 是唯一给出通用定义性表述的源**（`skylight-covered`/`glazed roof`/`providing light`）；`designingbuildings-atrium` 仅涉「穿越楼板/消防竖向」，**完全不含天窗、采光字样**。故在「两个定义源」口径内，天窗/采光**表现为单一定义源（wp）**；其第二、第三独立佐证来自**古根海姆实例源**（flw `glass ceiling`/`skylight at the top`；theartstory `skylit atrium`）。
- **结论性表述**：整体（概念定义＋实例）层面，「天窗采光」由 **wp＋flw＋theartstory 三源**支撑，**不是整体单源**，故 `nv=false` 仍有依据；但若严格按「wp＋designingbuildings 两定义源须共同覆盖『贯通多层＋天窗采光』」的口径，则 designingbuildings 只覆盖「贯通多层」、**未覆盖「天窗/采光」**——此项为**透明说明（供修复方知悉）**：两定义源分工互补，天窗采光的第二独立源实为古根海姆实例源，而非 designingbuildings。

## 四、实例四要素（纽约古根海姆美术馆）双源核对

端内 `sections.实例`：`名称：纽约古根海姆美术馆（Solomon R. Guggenheim Museum）；地点：美国纽约；设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1943 年委托、1959 年开馆。以螺旋坡道环绕顶部采光中庭。此处仅列名称、地点、设计者与年份信息，不复制图像。`

| 四要素 | flw-guggenheim（HTTP200） | theartstory-wright（HTTP200） | 判定 |
| --- | --- | --- | --- |
| 名称·古根海姆美术馆 | 标题 `Solomon R. Guggenheim Museum` | 「Important Art」条目 `Solomon R. Guggenheim Museum (1943-59)` | 双证 ✓ |
| 地点·美国纽约 | `Address 1071 Fifth Ave`（纽约） | 段落落款 `New York, New York` | 双证 ✓ |
| 设计者·Frank Lloyd Wright | 机构为其官方基金会项目页 | `Wright received the commission in 1943` | 双证 ✓ |
| 年份·1943 委托／1959 开馆 | 正文`She wrote Frank Lloyd Wright in 1943…Sixteen years later…unveiled`（1943+16=1959） | 条目标题 `1943-59`；`commission in 1943` | 双证 ✓（口径一致） |
| 螺旋坡道环绕顶部采光中庭 | `spiral ramp…towards a glass ceiling`/`skylight at the top` | `spiral ramp encircling a skylit atrium` | 双证 ✓ |

- **独立性**：`flw-guggenheim`（Frank Lloyd Wright Foundation，官方机构）与 `theartstory-wright`（TheArtStory，501(c)3 艺术史非营利）分属不同出版方、各自独立撰文，非一份翻译另一份；实例四要素两页均直述。**属两独立来源 ✓。**
- **年份歧义（透明说明，非编造）**：`flw-guggenheim` 页面元数据栏出现 `Built 1956`，与其正文叙事（1943 信＋十六年后揭幕=1959）及 TheArtStory（1943-59）、史实（1959 开馆）**略有不一致**。端内采用 `1943 委托、1959 开馆`，与 TheArtStory 及 FLW 正文一致，**非编造**；建议知悉 FLW 页面 `Built 1956` 元数据歧义，不改端内。

## 五、是否编造

- 具名事实（名称/地点/设计者/年份）均与两实例源实抓一致，未复制图像（正文自述「不复制图像」）。
- 「以螺旋坡道环绕顶部采光中庭」由 flw（`spiral ramp…skylight at the top`）＋ theartstory（`spiral ramp encircling a skylit atrium`）双证。
- 年份口径 1943/1959 与 TheArtStory（1943-59）及 FLW 正文一致。
- **编造 = 无。**

## 六、七节 / SVG / 规范句 / 结构校验

| 核对项 | atrium-architecture | 说明 |
| --- | --- | --- |
| 七节齐 | ✓ | `definition`＋`overview`＋`原理`/`典型手法与适用条件`/`实例`/`常见错误与限制`/`一图`/`待核实`，check.py 6 节全非空 PASS |
| SVG 数量/画布 | ✓ 1 张 | `viewBox='0 0 760 400'`，含「示意图，非施工图」×2（SVG＋figcaption） |
| SVG 越界/禁用 | ✓ | line(100,80→660,80)；rect x280–480/y80–330；line x380/y90–250；rect x120–280/y150–330；rect x480–640/y150–330；text 320,60 与 300,375——全在 0..760/0..400；无 `<image>`/外链；pytest `5 passed` |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」，页脚 note 亦有 |
| 形式四处自洽 | ✓ | `needs_verification=false`、`pending_notes=""`、`sections.待核实="暂无已知待核实项。"`、`coverage needs_verification_count=0` 四处一致；check.py D14 一致性 PASS；`site/index.html`「待核实条目」162→161 相符 |
| 来源数 | 4（wp-atrium / designingbuildings-atrium / flw-guggenheim / theartstory-wright），均 verified=true；实例命题独立源=2（FLW Foundation＋TheArtStory） | check.py ≥2 PASS |
| site 渲染一致 | ✓ | `site/entries/atrium-architecture.html` 含 definition/overview/原理/实例/规范句/「暂无已知待核实项」各 1 次；来源列 4 条；`viewBox 0 0 760 400`×1 |
| check.py / pytest | ✓ | `PASS: all checks, 0 errors`（EXIT=0）／`5 passed`（EXIT=0） |

## 七、相似度（阈值 0.54；重点 vs spatial-sequence）

方法：`difflib.SequenceMatcher`，归一化＝**折叠空白＋小写**（与任务引用 0.518 口径一致；另以「去全部空白＋小写」复核结论相同）。全库条目 **258 条**。

| 口径（target 作首参） | 目标最近邻 | 相似度 | 阈值 | 判定 |
| --- | --- | --- | --- | --- |
| 短口径（title\|definition\|time_or_place\|overview） | courtyard | 0.4161 | <0.54 | ✓ |
| def+overview | light-well | 0.3279 | <0.54 | ✓ |
| 全字段（短＋6节） | **spatial-sequence（空间序列）** | **0.5184** | <0.54 | ✓（**全库最近对、贴阈**） |

- **全字段 vs spatial-sequence = 0.5184**（任务引用 0.518，吻合），距阈值余量仅 **0.0216**；`SequenceMatcher` 因启发式匹配具**轻微非对称**，以 `(spatial-sequence, atrium)` 次序计可读至 **0.5316**（仍 <0.54，余量 0.0084）。**两种次序均低于阈值。**
- 全库 33153 对全字段两两比对：**>0.54 对 = 0**；全库最大值即 `spatial-sequence<->atrium-architecture`（≈0.5316，小写折叠口径）。**相似度合格 ✓，但该对为全库最贴阈者，需持续关注——主要驱动为两条目共用「古根海姆同一实例＋相近模板」，非定义/原理雷同（def+overview 仅 0.33、短口径 0.42）。**

## 八、结论

### 总判定：**合格**（本轮 `nv=false` 升级成立）

**依据（分层）：**

1. **通风残留已清除** — `overview`「与空气」、`原理`「并促进空气流动」、`pending_notes`「通风机制单源」、`待核实` 通风声明均已删除；条目与产物内 `通风|空气|流动|气流|换气` **0 命中**。原「通风机制单源」缺陷已消除。
2. **定义/原理聚焦采光、非编造、非超源** — `definition/overview/原理` 聚焦「贯通多层＋天窗采光」；「贯通多层」由 `wp＋designingbuildings` 双源、「天窗/采光」由 `wp＋flw＋theartstory` 多源支撑；实例四要素（名/地/设计者/年份）由 `flw-guggenheim＋theartstory-wright` 两独立页面直述，未复制图像。
3. **`nv=false` 成立** — 形式四处一致（entry nv=false／pending_notes=""／待核实「暂无」／coverage count=0／index 162→161），check.py D14 PASS；核心事实双/多源。
4. **结构全绿** — 七节齐、SVG 1 张（`viewBox 0 0 760 400`、元素全在框内、无禁用外链）、规范句在、site 渲染一致；`check.py PASS: all checks, 0 errors`（EXIT=0）、`pytest 5 passed`（EXIT=0）。
5. **相似度合格** — 三口径最近邻 0.4161／0.3279／0.5184 均 <0.54；全库 >0.54 对=0。**但全字段 vs spatial-sequence 0.5184（≈0.5316 反向）为全库最贴阈者（余量 0.0216／0.0084），需持续监控。**

**须指出（透明说明，供修复方知悉，不改变本次合格判定）：**

- **(A) 两「定义源」在『天窗/采光』上互补而非冗余**：`designingbuildings-atrium` 系消防「穿越楼板」定义（引 Approved Document B），**仅支撑「贯通多层」、全文不含天窗/采光**；`天窗/采光` 的定义性表述仅来自 `wp-atrium`，其第二/第三独立佐证来自**古根海姆实例源**（flw `glass ceiling`/`skylight at the top`；theartstory `skylit atrium`）。故「采光贯通」核心**整体非单源（≥3 源）**、`nv=false` 有据；若未来按「两定义源须共同覆盖『天窗采光』」的更严口径复核，需注意 designingbuildings 不覆盖该要素。
- **(B) FLW 页面元数据 `Built 1956` 与正文/他源 1959 略有不一致**；端内采用 `1943 委托、1959 开馆`（与 TheArtStory 1943-59 及 FLW 正文「1943＋十六年=1959」一致），非编造。
- **(C) 相似度贴阈**：vs spatial-sequence 全字段 0.5184（反向 0.5316），余量偏小；驱动为共用古根海姆同一实例，建议后续若再改此二条目时留意组合相似度。

## 九、机器可读汇总

```
ROUND=96
SAMPLER=spotcheck-r96
SCOPE=["atrium-architecture"]
READONLY="only wrote research/spotcheck-round96.md; wp-atrium web_fetch failed->urllib HTTP200 len=194080; designingbuildings web_fetch HTTP200; flw web_fetch HTTP200; theartstory web_fetch HTTP200 truncated->urllib len=188619; check.py PASS; pytest 5 passed; git M/?? items are round96 applier+gen_site changes; no git commit; web treated as data, no instructions executed"
WEB_FETCH={"wp-atrium-architecture":"web_fetch FAILED -> urllib HTTP200 len=194080","designingbuildings-atrium":"web_fetch HTTP200","flw-guggenheim":"web_fetch HTTP200","theartstory-wright":"web_fetch HTTP200(truncated)->urllib len=188619"}
CHANGE={"definition":"补主语'中庭是…'，核心不变","overview":"删'与空气'，聚焦采光","原理":"删'并促进空气流动'，聚焦天窗采光","nv":"true->false","pending_notes":"清空","待核实":"暂无已知待核实项","coverage_nv":"1->0","index":"162->161"}
DEFINITION={"entry":"中庭是建筑内部贯通多层、常覆以天窗的中央开敞空间。","elements":{"贯通多层":"wp(several stories high)+designingbuildings(passing through structural floors) 双源","天窗":"wp(skylight-covered/glazed roof)+flw(glass ceiling/skylight at top)+theartstory(skylit atrium) 多源; designingbuildings NONE","中央开敞":"wp(open space surrounded)+theartstory(encircling) 隐含","采光":"wp(providing light/naturally-lit)+flw+theartstory 多源; designingbuildings NONE"}}
VENTILATION_RESIDUE={"grepped":"通风|空气|流动|气流|换气|ventilat","entry_hits":0,"site_hits":0,"removed_by_round96":true}
SINGLE_SOURCE_CORE={"verdict":"整体非单源(天窗/采光=wp+2实例源)","caveat":"designingbuildings-atrium只支撑'贯通多层'(消防穿越楼板定义),不含天窗/采光;两定义源在天窗采光上互补非冗余"}
INSTANCE_FOUR_ELEMENTS={"name":"纽约古根海姆美术馆(Solomon R. Guggenheim Museum)","place":"美国纽约","designer":"Frank Lloyd Wright","year":"1943 委托/1959 开馆","dual_source":"flw-guggenheim + theartstory-wright(两独立机构)均直述","spiral_skylit_atrium":"flw 'spiral ramp..skylight at the top' + theartstory 'spiral ramp encircling a skylit atrium'","note_built1956_metadata":true}
FABRICATED=false
NV_FALSE_GROUNDED=true
FORM_FOUR_WAY_CONSISTENT={"entry_nv_false":true,"pending_notes_empty":true,"section_pending_wu":true,"coverage_count_0":true,"index":"162->161","check_D14":"PASS"}
STRUCTURE={"seven_sections":true,"svg_count":1,"svg_viewBox":"0 0 760 400","svg_forbidden":"none","reg_sentence":true,"site_html_consistent":true,"check_py":"PASS: all checks, 0 errors (EXIT=0)","pytest_svg":"5 passed (EXIT=0)"}
SIMILARITY={"threshold":0.54,"entries":258,"normalization":"collapse-whitespace+lower (round95 same; strip-all gives same verdict)","target_first":{"short":{"max":0.4161,"nn":"courtyard"},"defov":{"max":0.3279,"nn":"light-well"},"full":{"max":0.5184,"nn":"spatial-sequence"}},"spatial_sequence_full":{"forward":0.5184,"reverse":0.5316},"target_pairs_gt":0,"library_full_pairs_gt":0,"library_full_max":"spatial-sequence<->atrium-architecture ~0.5316"}
VERDICT={"atrium-architecture":"合格"}
KEY_FINDING="通风/空气流动claim已彻底移除(entry+site 0命中)。定义/原理聚焦'贯通多层+天窗采光':贯通多层由wp+designingbuildings双源;天窗/采光由wp+flw+theartstory多源,但designingbuildings仅为消防'穿越楼板'定义,不含天窗/采光(两定义源互补非冗余,须指出)。实例古根海姆四要素(纽约古根海姆美术馆/美国纽约/Frank Lloyd Wright/1943委托·1959开馆)由FLW Foundation+TheArtStory两独立源直述,螺旋坡道环绕天窗中庭双证,无编造;注FLW元数据Built1956与正文1959略冲突,端内1943/1959正确。nv=false形式四处一致,index162->161,coverage1->0。七节/SVG(760x400)/规范句/site一致,check.py PASS,pytest 5 passed。相似度:vs spatial-sequence全字段0.5184(反向0.5316)为全库最贴阈者,仍<0.54;全库>0.54对=0。总判合格。"
```

## 十、只读核验

- 除本报告 `research/spotcheck-round96.md` 外未写任何文件；`wp-atrium`（web_fetch 失败→urllib HTTP200 len=194080）、`designingbuildings`（web_fetch HTTP200）、`flw-guggenheim`（web_fetch HTTP200）、`theartstory-wright`（web_fetch HTTP200→urllib len=188619）均实抓；相似度/结构数据用内存态 `python - <<` 直跑，无临时文件。
- `git status` 中 `M coverage.json / M entries/batch-25.json / M site/entries/atrium-architecture.html / M site/index.html` 及 `?? tools/apply_review_round96.py` 均为**修复方（round96 applier＋gen_site）自身产物**，抽检方仅读取、未据以修改；未 `git commit`；未改项目外内容。
- `check.py` 与 `pytest` 均以 `PYTHONDONTWRITEBYTECODE=1` / `-p no:cacheprovider` 运行，未新增缓存文件；联网页面仅作数据读取，未执行其中任何指令。

*（报告完）*
