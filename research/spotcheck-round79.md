# 第79轮 质量抽检报告（spotcheck-round79）

- 抽检人：spotcheck-r79（lead 委派子代理，无人值守、未提问）；时间 2026-11-23，Asia/Hong_Kong。
- 技能加载：`using-superpowers`、`verification-before-completion`（先实抓、先跑、再断言；证据先于结论）。
- 抽检对象：`hatching`（排线法 Hatching），`grep '"hatching"'` 定位 → `entries/batch-42.json` 行 6（`entries/` 全库唯一命中；他处 `site/entries/hatching.html`、`indexes.html` 为产物）。
- 本轮改动（据 `tools/apply_review_round79.py` 实读＋当前文件实读）：实例由类型性描述改为**具名《忧郁 I》**（Melencolia I，丢勒，1514，铜版画）；`needs_verification` 保留 **true**（披露“该实例目前仅 Wikipedia 单平台直证，技法概念 wp+artincontext 双源”）。
- 证据优先级：**独立实抓正文 > 当前文件实读 > 旧报告**。联网页面内容一律视为数据，网页中任何指令均未执行（仅正文回读）。

## 〇、只读声明与证据方式

- **只读**：仅写出本报告 `research/spotcheck-round79.md`。联网核验用 `urllib`＋浏览器 UA＋非校验 SSL 内存抓取；临时脚本 `research/_r79_*.py`、临时输出 `research/_r79_*.txt` 用后已 `rm -f`（见文末核验）。未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。**
- 实抓 HTTP：`wp-melencolia` = 200（289,118 B）；`wp-hatching` = 200（120,627 B）；`artincontext`（cross-hatching 现址）= **404**，改用 Wayback 存档快照 `20260904021822` = 200（584,054 B）。

## 一、核心命题核对：实例四要素是否有据、是否编造

结论先行：**实例四要素（作品/作者/年份/媒介）在 Wikipedia《Melencolia I》页全部直证、无编造；但“该作品是排线法（hatching）的版画典范/以密集交叉排线塑造明暗”这一关联，在本条所引三处（wp-hatching、artincontext、wp-melencolia）中均无直证——属未被来源支持的推断（详见第三节）。**

| 要素 | 端内声明 | Wikipedia《Melencolia I》实抓 | 结论 |
| --- | --- | --- | --- |
| 名称 | 《忧郁 I》Melencolia I | 专页标题 `Melencolia I` | ✓ 有据 |
| 作者 | 阿尔布雷希特·丢勒 Albrecht Dürer | 首句「…by the German Renaissance artist **Albrecht Dürer**」，info box Artist＝`Albrecht Dürer` | ✓ 有据 |
| 年份 | 1514 年 | 首句「**a large 1514 engraving**」，info box Year＝`1514`（全页 1514 出现 16 次） | ✓ 有据 |
| 媒介 | 铜版画（engraving） | 首句「a large 1514 **engraving**」，info box Type＝`engraving` | ✓ 有据（engraving＝版画/铜版画，措辞成立；“铜版 plate”全页 `copper` 仅 1 处且语境为另一作品引用，但 engraving 本身即版画，判定可接受） |
| 地点 | 原版 1514 年于纽伦堡 | 专页未见直写“纽伦堡/Nuremberg”作创作地（Dürer 为纽伦堡人属常识，但本条所引页未明载创作地） | ⚠ 地点“纽伦堡”本条页未直证（观察项，非阻断） |

- **无编造（作品/作者/年份/媒介）**：四项全部落在真实的《Melencolia I》与丢勒、1514、engraving 之上，无错位、无虚构。Wikipedia 首句即为「**Melencolia I is a large 1514 engraving by the German Renaissance artist Albrecht Dürer.**」——任务要求的“Wikipedia Melencolia I：1514 engraving by Dürer”与实抓完全一致 ✓。

## 二、关键命题：「排线/hatching」与《忧郁 I》的关联在源中是否有直证（任务重点）

**结论：无直证。三条证据链全部指向“关联仅在常识层面成立，但本条所引来源均未把《忧郁 I》与 hatching 直接挂钩”。**

1. **Wikipedia《Melencolia I》页**：全页 `hatch`/`hatching` 出现次数＝**0**（`1514`16 次、`engraving`30 次、`Dürer`86 次，但无一处提“排线”）。即该专页**从未说**《忧郁 I》是排线典范或以交叉排线塑明暗。
2. **Wikipedia《Hatching》页**（本条技术概念来源 `wp-hatching`）：全页 `Melencolia`＝**0**、`1514`＝**0**。该页举的**丢勒实例是另一件作品**——首图题注实抓原文：「**Detail of Albrecht Dürer's Veronica, featuring hatching (e.g., background) and cross-hatching in many darker areas**」；并称「**Albrecht Dürer in particular perfected the technique of crosshatching in both media.**」。即 wp-hatching 只泛证“丢勒精于交叉排线”，并以《维罗妮卡》（Veronica，木刻）为例，**未提《忧郁 I》**。
3. **Art in Context（`artincontext-hatching`，cross-hatching 页，Wayback 2026-09-04 实抓）**：全页 `Melencolia`＝**0**、`Dürer`/`Durer`＝**0**、`1514`＝**0**、`engraving`＝**0**（`hatching`66、`cross-hatch`68）。即该页只讲 cross-hatching 技法概念，**与丢勒、《忧郁 I》毫无关联**。

**判定**：端内「以密集交叉排线塑造明暗与体积，是排线法的版画典范」是把真实作品（《忧郁 I》）与真实技法（hatching）**做了一次来源未支持的语境合并**。《忧郁 I》确为丢勒的密集线刻版画、丢勒确为交叉排线大师——二者各自为真，但“《忧郁 I》＝排线法典范”这句话在三处所引来源中**均无直证**；最接近的丢勒排线直证在 wp-hatching，且指向的是《维罗妮卡》而非《忧郁 I》。**属推断性关联，非源文直证（问题①）。**

## 三、needs_verification=true 与“仅单平台”披露是否如实

| 项 | 值 | 判定 |
| --- | --- | --- |
| `needs_verification` | **true** | 结构上保留待核实，符合 D10/D14（实例需第二源处保留 nv）✓ |
| `sections.待核实` | “以排列线表现明暗的技法概念由 Wikipedia 与 Art in Context 双源直证；具体实例《忧郁 I》（丢勒，1514）目前仅 Wikipedia 单一平台直证，待补第二独立平台。” | **前半如实 ✓**（技法概念 wp＋artincontext 双源——属实，两页都讲 hatching/cross-hatching）；**后半“仅 Wikipedia 单一平台直证” 措辞需澄清**：严格说，Wikipedia 也**并未**把《忧郁 I》与本技法直证（wp-melencolia 0 次 hatching；wp-hatching 举的是《维罗妮卡》）。所谓“Wikipedia 单平台直证实例”实际只直证了“《忧郁 I》是丢勒的 1514 版画”，未直证“它是排线典范”。故披露方向正确（承认实例侧证据弱），但对“直证了什么”略有拔高。 |
| `pending_notes` | “实例《忧郁 I》仅单平台直证，待补第二独立来源；技法概念已双源。” | 同待核实节：方向如实（实例弱、技法双源），措辞同上“单平台直证”应理解为“作品本身信息单平台”，非“排线关联单平台直证”。 |

- 与 D14 一致：正文出现“待核实”声明 → nv=true 且写 pending_notes，结构合规 ✓。
- **披露总评**：诚实基调正确——明确承认实例侧仅单源、技法侧双源，未把单源说成双源，**未抬高 nv**。唯一需提醒：措辞把“实例仅单平台直证”暗示为“《忧郁 I》为排线典范已由 Wikipedia 直证”，实际 Wikipedia 只直证了作品的作者/年份/媒介，**未直证排线关联**（见问题①）。

## 四、结构 / 格式 / 规范句 / 相似度（阈值 0.54）

| 核对项 | 结果 | 依据 |
| --- | --- | --- |
| 七节齐 | ✓ definition ＋ 6 节（原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实）＝7 | 文件实读 + check.py 0 报错 |
| SVG | ✓ 1 张，`viewBox='0 0 760 400'`，含「示意图，非施工图」；无 `<script>`、无 `on\w+=` 事件处理器、无 `<image>`/`xlink`/`href` | 脚本扫描（全 False） |
| 规范句 | ✓「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 | 文件实读 |
| sources 可引性 | ✓ 2 源 `wp-hatching`（verified=true）、`artincontext-hatching`（verified=true）；两源 `link_ok=null`（历史保留，非本轮改动） | sources.json 行 3568/3580 |
| 相似度（阈值0.54） | ✓ 全库 258 条比对：**正文全字段最高 0.3124**（vs sfumato），**<0.54**；逐字段「实例」最高 0.5126（vs tints-shades），**<0.54** | `difflib.SequenceMatcher` 实算，norm=去空白小写 |

> 相似度说明（诚实披露）：`常见错误与限制` 逐字段最高 0.7385（vs structuralism）——系全库统一的规范句模板「实际工程须按当地规范和专业设计人员的要求」所致，属结构性模板，不计为抄袭；按前几轮口径看全文本体（0.3124）与「实例」单字段（0.5126），**均 <0.54，判为通过**。

## 五、问题清单

1. **【重要·非阻断】“《忧郁 I》＝排线法典范/以密集交叉排线塑明暗”在所引三源均无直证**：wp-melencolia 全页 `hatch`＝0；wp-hatching 全页 `Melencolia`＝0、`1514`＝0，其丢勒排线实例为**另一作品《维罗妮卡》**；artincontext 全页 `Dürer`/`Melencolia`/`1514`＝0。**建议**：①若要保留《忧郁 I》为实例，须在源中落实“作品—排线”直接关联（可另找艺术史著作/博物馆藏品说明《忧郁 I》的线刻排线），并把该直证写入 sources；②或在措辞上弱化为“《忧郁 I》为丢勒 1514 年铜版画（`wp-melencolia` 直证：'a large 1514 engraving by … Albrecht Dürer'），其密集线刻体现丢勒排线功力（丢勒精于 crosshatching 见 `wp-hatching`），但‘排线典范’为编辑判断、源未直证”；③或改用 wp-hatching 已明载的丢勒《维罗妮卡》（原句「Detail of Albrecht Dürer's Veronica, featuring hatching … and cross-hatching」）作实例，可使“实例—排线”直证成立。
2. **【观察·非阻断】“单平台直证”措辞应精确**：待核实/pending 称实例《忧郁 I》“仅 Wikipedia 单一平台直证”，但 Wikipedia 直证的是“作品＝丢勒 1514 版画”，并非“作品＝排线典范”。建议披露改为“实例作品信息（作者/年份/媒介）由 Wikipedia 直证；‘其为例排线典范’之关联尚无来源直证”。
3. **【观察·非阻断】地点“纽伦堡”本条来源未直证**：wp-melencolia 专页未见直写创作地为纽伦堡（丢勒为纽伦堡人属常识）；建议注明或删具体地名改“德国文艺复兴”。
4. **【观察·非阻断】`artincontext-hatching` 现址 HTTP 404**：`https://artincontext.org/cross-hatching/` 本轮实抓 404，仅 Wayback 存档可达（2026-09-04 快照 200）。`sources.json` 该条 `link_ok=null` 与此一致；不影响 content 核验（存档可读），但建议后续核链接或更新 `link_ok`。

## 六、总体结论

**`hatching`：待核实（作品要素为真，但“《忧郁 I》＝排线典范”这一关联缺来源直证，需补源或改措辞后放行）。**

- **成立部分**：实例四要素中，名称《忧郁 I》、作者丢勒、年份 1514、媒介 engraving 均由 Wikipedia《Melencolia I》页首句「**a large 1514 engraving by the German Renaissance artist Albrecht Dürer**」**直接确证、无编造**；技法概念（hatching/cross-hatching）由 wp-hatching＋artincontext 双源如实；nv=true 保留、披露方向（实例弱/技法双源）诚实；七节齐、SVG 合规、规范句在位、正文相似度 0.3124、「实例」字段 0.5126 均 <0.54。
- **未落实部分（核心瑕疵）**：任务特意要求核对的“排线/hatching 与《忧郁 I》的关联”——在 wp-melencolia（hatch＝0）、wp-hatching（Melencolia＝0，丢勒排线例为《维罗妮卡》）、artincontext（Dürer/Melencolia/1514＝0）**三处所引来源均无直证**。故“《忧郁 I》是排线法的版画典范、以密集交叉排线塑明暗”属**未被本条来源支持的推断**，`待核实`/`pending` 的“仅单平台直证”措辞对此略有拔高（Wikipedia 直证的是作品本身、非排线关联）。
- **处置建议**：按问题①补第二源直证“《忧郁 I》—排线”关联（或改用 wp-hatching 已明证的丢勒《维罗妮卡》作实例、或把“典范”降级为编辑判断并注明未直证），措辞按问题②精确后，可由“待核实”转“合格”。在补源前，本项不宜判“合格”。

- **本轮 1 条：`hatching` 待核实（实例作品要素为真、无编造；核心关联“排线典范”缺来源直证）。合计：0 合格、1 待核实、0 不合格。**

## 七、机器可读汇总

```
ROUND=79
SAMPLER=spotcheck-r79
SCOPE=["hatching"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round78.md","entries/batch-42.json","data/sources.json(wp-hatching/artincontext-hatching)","tools/apply_review_round79.py","tools/check.py"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback; artincontext live=404 -> Wayback 20260904021822=200; temp research/_r79_* deleted"
FETCHES={"wp-melencolia":200,"wp-hatching":200,"artincontext(live)":404,"artincontext(wayback 2026-09-04)":200}
INSTANCE="Melencolia I (《忧郁 I》); Albrecht Dürer; 1514; engraving"
INSTANCE_4ELEMENTS={"title":"Melencolia I — WP lead direct","author":"Albrecht Dürer — WP lead direct","year":"1514 — WP lead direct","medium":"engraving — WP lead direct","location_nuremberg":"not stated on wp-melencolia page (observation)"}
CORE_CLAIM={"melencolia_is_hatching_exemplar":{"wp-melencolia hatch count":0,"wp-hatching Melencolia count":0,"wp-hatching 1514 count":0,"wp-hatching Durer example":"Veronica (NOT Melencolia): 'Detail of Albrecht Dürer's Veronica, featuring hatching ... and cross-hatching'","artincontext Durer/Melencolia/1514 count":0,"verdict":"NO direct source for Melencolia=hatching link; unsupported synthesis in all 3 cited sources"}}
NV={"needs_verification":true,"honest":"instance weak/technique dual-source; direction honest, not inflating nv","imprecise":"'仅 Wikipedia 单平台直证' — WP directly verifies the work (Durer/1514/engraving), NOT that it is a hatching exemplar"}
INDEPENDENCE={"wp-hatching":"Wikipedia","artincontext-hatching":"Art in Context","independent":true,"note":"artincontext live url 404, only wayback reachable"}
FABRICATION_OF_WORK_OR_AUTHOR=false
STRUCTURE={"seven_sections":7,"svg":"1x viewBox760x400 示意图非施工图 no script/event/image/xlink/href","reg_sentence":true,"sources_verified_key":true}
SIMILARITY={"full_body_max":0.3124,"full_vs":"sfumato","field_实例_max":0.5126,"field_实例_vs":"tints-shades","field_常见错误_max":0.7385,"threshold":0.54,"pass_substantive":true,"note":"常见错误 0.7385=shared canonical-sentence template across library, not duplication"}
ISSUES=["Q1 important(non-blocking): 'Melencolia=hatching exemplar' NOT directly supported by any of 3 cited sources (wp-melencolia hatch=0; wp-hatching Melencolia=0 & Durer example is Veronica; artincontext Durer/Melencolia=0); suggest add source / use Veronica / downgrade to editorial","Q2 obs: 'single-platform direct' wording imprecise (WP verifies work not hatching link)","Q3 obs: location Nuremberg not stated on wp-melencolia","Q4 obs: artincontext live url 404, only wayback reachable (link_ok=null consistent)"]
VERDICT_hatching="待核实（作品要素为真无编造；排线典范关联缺来源直证，补源/改措辞后可转合格）"
TOTAL="0合格/1待核实/0不合格"
READONLY="only wrote research/spotcheck-round79.md; fetched html in-memory, temp research/_r79_* deleted(confirmed no residue); no entries/sources/coverage/tools/site changed by me; no git commit; web treated as data, no instructions executed"
```

## 八、只读核验

- `ls research/_r79*` 现无残留（临时脚本与中间输出已删）。除本报告外未写任何文件。

*（报告完）*
