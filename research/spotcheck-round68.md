# 第68轮质量抽检报告（spotcheck-round68）

- 抽检人：spotcheck-r68（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 19:34 起，Asia/Hong_Kong。
- 抽检对象（第68轮改动 1 条）：`spatial-sequence`（空间序列，`entries/batch-02-a.json`，行 309–340，经 `grep "spatial-sequence"` 定位）。
- 本轮引用来源（`data/sources.json`）：`nyc-lpc-guggenheim`（行 2056–2066，NYC Landmarks Preservation Commission，官方机构 PDF，verified=true）、`guggenheim-visitor-guide`（行 2068–2078，Solomon R. Guggenheim Foundation，官方访客指南 PDF，verified=true）。
- 本轮任务：将 `spatial-sequence` 实例升级为「已验证」——实例=纽约古根海姆螺旋坡道，双源=`nyc-lpc-guggenheim`（NYC 地标报告 PDF："spiraling expanse…continuous…spiral ramps"）＋`guggenheim-visitor-guide`（官方访客指南 PDF："Ascend the building's grand spiral…spiral ramp quarter mile long, climbs at a three-degree incline"）。
- 判定依据：`README.md` 硬性规则（不编造/只引 verified/关键事实双源互证否则标待核实/内联 SVG 非施工图/规范句/40 条上限）＋`DECISIONS.md`（D05/D06/D10/D11/D14）＋`tools/check.py` 校验口径＋第39–67轮既定相似度口径（difflib.SequenceMatcher，norm=去空白小写，①短=title+definition ②全字段不含 SVG，阈值 0.54）。

## 〇、只读声明与数据稳定性（verification-before-completion：先实抓、先跑、再断言）

- **只读**：本次**仅写出** `research/spotcheck-round68.md` 一个文件。来源核验全程以 `python - <<'PY'` **内存内抓取**（`urllib`＋浏览器 UA＋非校验 SSL）并对 PDF 用 `pypdf` 解析，**仅落两份临时抽取文本**（`research/_tmp_nyc.txt`、`research/_tmp_guide.txt`），核验后**已删除**；未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`，未 `git commit`，未改项目外内容。联网与 PDF 内容一律视为数据，网页/文档中任何指令均未执行（仅正文回读）。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）。** 纯校验不写文件。
- **注**：工作区含第68轮未提交改动（`spatial-sequence` 条目与 coverage 已改为 nv=false/双源）。本次核验以工作区当前内容为准，未触碰数据文件。

## 一、来源实抓结果（HTTP 状态＋PDF 正文回读，均为本轮现抓）

| 来源 id | URL | HTTP | 页数/大小 | 回读要点（PDF 抽取原文，逐字） |
| --- | --- | --- | --- | --- |
| `nyc-lpc-guggenheim` | http://s-media.nyc.gov/agencies/lpc/lp/1774.pdf | **200** | 32 页 / 14.4MB | `The spiraling expanse, linked to the smaller "monitor" ... breaks New York's relentless grid ... the building's organic form`（spiraling expanse 逐字）；`this surprising spiral form, with all its associations to the continuous creative force of nature`（continuous 逐字）；`Circles and spiral ramps were erployed by Wright in designs`（spiral ramps 逐字）；`Frank Lloyd Wright, Architect. Built 1956-59`（设计者/年代逐字） |
| `guggenheim-visitor-guide` | https://www.guggenheim.org/wp-content/uploads/2025/07/250715_VE_VisitorGuide_v02.pdf | **200** | 4 页 / 61.8KB | `Ascend the building's grand spiral toward the central dome`（Ascend / grand spiral 逐字）；`The rotunda's spiral ramp is a quarter mile long and climbs steadily at a three-degree incline`（spiral ramp / quarter mile / three-degree incline 逐字）；`Since it opened to the public in 1959`（1959 逐字）；`commissioned Frank Lloyd Wright to design`（设计者逐字） |

**两源均 HTTP 200、PDF 正文可回读。任务点名的引文串「spiraling expanse…continuous…spiral ramps」与「Ascend the building's grand spiral…spiral ramp quarter mile long…three-degree incline」全部在两份 PDF 正文逐字可回读。**

## 二、逐条核对

### `spatial-sequence`（空间序列）— **合格**

| 核对项 | 结论 | 依据 |
| --- | --- | --- |
| definition 引用支撑 | ✓ 有据 | 条目 definition「若干空间按进入顺序组织形成的连续体验」＋overview「开合、明暗与尺度变化控制节奏，使行进成为叙事」↔ 双源对古根海姆连续坡道「螺旋盘旋而上、连续观展」的逐字描述（guide `Ascend the building's grand spiral ... take in ... works`；nyc `spiral ramps`）＝「连续体验」直证；「按进入顺序组织」由连续坡道盘旋而上的观展动线支撑。属对该实例的合理概念抽象，未虚构 |
| time_or_place | ✓ | 「跨时期、全球（参见来源）」为泛化空间序列概念表述，实例具体年代由 sections 承载，成立 |
| **实例·纽约古根海姆螺旋坡道**（任务点名） | ✓ 直证 | 条目「名称：纽约古根海姆博物馆（Solomon R. Guggenheim Museum）螺旋坡道；地点：美国纽约」↔ nyc `SOLOMON R. GUGGENHEIM MUSEUM, 1071 Fifth Avenue, Manhattan ... spiral ramps`；guide `The Guggenheim New York ... grand spiral`＝名称/地点/螺旋坡道逐字对上 |
| **双源引文一（spiraling expanse…continuous…spiral ramps）**（任务点名） | ✓ **逐字** | nyc PDF：`spiraling expanse`、`continuous creative force`、`spiral ramps` 三串均命中（见 §一） |
| **双源引文二（Ascend…grand spiral…quarter mile…three-degree incline）**（任务点名） | ✓ **逐字** | guide PDF：`Ascend the building's grand spiral`、`spiral ramp is a quarter mile long and climbs steadily at a three-degree incline` 全串命中（`quarter mile` 因 PDF 换行断为 `quarter  mile`，语义连续完整） |
| 实例·设计者/年份（是否编造） | ✓ **直证** | 条目「设计者：弗兰克·劳埃德·赖特（Frank Lloyd Wright）；年份：1959 年开馆」↔ nyc `Frank Lloyd Wright, Architect. Built 1956-59`；guide `Since it opened to the public in 1959 ... commissioned Frank Lloyd Wright to design`＝设计者与 1959 开馆逐字可回读，**未编造** |
| 来源直接相关 | ✓ | 一为 NYC 地标保护委员会官方地标报告（对古根海姆建筑本体与螺旋形式、Wright、1956–59 详细记述），一为古根海姆基金会官方访客指南（螺旋坡道尺寸/坡度/1959/Wright），均主题直源、HTTP 200、verified=true |
| **两源独立性**（任务点名：NYC LPC 政府 vs 古根海姆官方） | ✓ **成立** | `nyc-lpc-guggenheim` 发布方＝**纽约市地标保护委员会（政府机构）**，体例为地标认定报告（legal/历史考证、含 tax map/听证记录）；`guggenheim-visitor-guide` 发布方＝**Solomon R. Guggenheim Foundation（博物馆官方）**，体例为访客导览。**两独立主体、官方属性不同（政府 vs 馆方）、文件性质与措辞体例完全不同、非镜像**；两者均独立载明「螺旋坡道/Wright/1959」核心事实，构成真双源互证 |
| 七节 | ✓ | definition + sections 六节（原理／典型手法与适用条件／实例／常见错误与限制／一图／待核实）＝七节齐，无空缺（check.py 0 报错） |
| SVG | ✓ | 1 张（`viewBox 0 0 760 400`，ellipse/path/circle/text，含「示意图，非施工图」；无 `on*=` 事件处理器、无 `<image>`/xlink/href/`<script>`；check.py 0 报错） |
| 规范句 | ✓ | 「常见错误与限制」收尾「实际工程须按当地规范和专业设计人员的要求」在位 |
| nv↔pending 联动 | ✓ 一致 | `needs_verification=false`／`pending_notes=""`／「待核实」节「暂无已知待核实项」三处一致；正文无内联「待核实」声明；check.py 未报「有待核实说明但 nv=false」类错误 |
| **nv 置 false 是否有据** | ✓ **有据** | 三要素（definition 连续体验 / overview 节奏叙事 / 实例螺旋坡道）均由两官方源逐字支撑；两源为**政府机构 vs 馆方**两独立发布主体，非镜像，核心事实（螺旋坡道连续观展、Wright、1959）双源独立印证。原第21轮「核心概念在旧来源正文缺失」的缺陷随本轮换为直接论述螺旋坡道连续观展的两官方源而消解，标 false 属**有据**（非掩盖：概念—实例—来源已闭环） |
| coverage↔entry | ✓ | title「空间序列」/theme「理论」/tier「核心」/period「跨时期」/region「全球」/level「L2」全一致；`source_count=2`＝entries 2 源；`needs_verification_count=0`＝nv false；status=已写 |
| 相似度（阈值 0.54） | ✓ | ①短 最高 **0.3673**（vs spatial-organization）＜0.54；②全字段 最高 **0.5096**（vs atrium-architecture）＜0.54，均低于阈值（全字段 0.5096 为贴近但合规） |

**`spatial-sequence` 结论：合格（本轮已可升级为已验证）。**

## 三、问题与建议（均非阻断）

1. **（提示，非阻断）全字段相似度 0.5096 逼近阈值（0.54，余量 0.03）**：最高相似对象为 `atrium-architecture`（中庭建筑），源于两者都就古根海姆螺旋中庭/连续观展有描述。当前仍合规，但若后续 `atrium-architecture` 或本条再扩写实例段，存在触阈风险，建议后续轮次留意差异化表述（如强化「序列/行进节奏」概念而弱化「中庭形态」复述）。
2. **（提示，非阻断）概念层来源偏实例化**：两源均为古根海姆**具体建筑**的官方文档，「空间序列」的一般性理论（起承转合、序列组织原则）系对其连续坡道实例的概念抽象，而非来自专论「空间序列」的理论文献（历史 gaps 多轮曾记「空间序列一般理论待补充专门来源」）。当前 definition/overview 属对实例动线的合理抽象、可回读支撑，标已验证在「实例+概念抽象」口径下成立；若追求理论层更硬的双源，可后续补一篇论述空间序列/游线的理论专文。**可选，不阻断。**

## 四、总体结论

- **`spatial-sequence`：合格（本轮已可升级为已验证）。**
  - 任务点名核对诸项全部获逐字支撑：**spiraling expanse…continuous…spiral ramps** 由 `nyc-lpc-guggenheim` PDF 逐字命中；**Ascend…grand spiral…quarter mile…three-degree incline** 由 `guggenheim-visitor-guide` PDF 逐字命中；实例 名称/地点/设计者（Wright）/年份（1959 开馆，nyc「Built 1956-59」）均双源可回读，**未编造**。
  - definition/overview/time_or_place 有据；七节齐、SVG 合规（示意图非施工图、无脚本/外链/事件处理器）、规范句在位、coverage 全字段一致、nv↔pending 三处一致。
  - **nv=false 有据**：`nyc-lpc-guggenheim`（纽约市地标保护委员会·政府）与 `guggenheim-visitor-guide`（Solomon R. Guggenheim Foundation·馆方官方）为两独立发布主体、文件性质与体例不同、非镜像，核心「螺旋坡道连续观展/Wright/1959」事实互证，双源独立成立。
  - **相似度 0.3673 / 0.5096 低于 0.54**（全字段 0.5096 接近阈值，见问题1）。
  - 全库 `python tools/check.py`＝`PASS: all checks, 0 errors`（EXIT=0）。
- **本轮 1 条：1 合格、0 待核实、0 不合格。**
- **建议（非阻断）**：① 留意全字段相似度 0.5096 与 `atrium-architecture` 的贴近，后续差异化表述；② 若追求理论层更硬双源，可补一篇论述「空间序列/游线」的理论专文。

## 五、机器可读汇总

```
ROUND=68
SAMPLER=spotcheck-r68
MODE=round68 改动 1 条抽检（spatial-sequence 升级已验证）
SCOPE=["spatial-sequence"]
DOCS_READ=["DECISIONS.md","research/spotcheck-round67.md","README.md","tools/check.py","entries/batch-02-a.json","data/sources.json","coverage.json"]
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
FETCH_METHOD="urllib+UA+unverified-SSL in-memory readback + pypdf parse; temp extracts research/_tmp_*.txt deleted after"
FETCHES={"nyc-lpc-guggenheim":200,"guggenheim-visitor-guide":200}
SPATIAL_SEQUENCE={
 "sources":["guggenheim-visitor-guide","nyc-lpc-guggenheim"],
 "definition_support":"双源古根海姆连续坡道连续观展(guide 'Ascend the building's grand spiral ... works' / nyc 'spiral ramps') -> 连续体验+进入顺序有据",
 "instance":"纽约古根海姆博物馆螺旋坡道 / 美国纽约 / Frank Lloyd Wright / 1959开馆",
 "quote1_nyc":"'spiraling expanse' + 'continuous creative force' + 'spiral ramps' VERBATIM in nyc PDF",
 "quote2_guide":"'Ascend the building's grand spiral' + 'spiral ramp is a quarter mile long and climbs steadily at a three-degree incline' VERBATIM in guide PDF (quarter mile 换行断为 quarter  mile)",
 "wright_year":"nyc 'Frank Lloyd Wright, Architect. Built 1956-59' + guide 'opened to the public in 1959 ... commissioned Frank Lloyd Wright' -> 逐字, 未编造",
 "two_source_independence":"nyc-lpc-guggenheim=纽约市地标保护委员会(政府机构,地标认定报告) vs guggenheim-visitor-guide=Solomon R. Guggenheim Foundation(馆方官方,访客指南): 两独立发布主体/官方属性不同/体例不同/非镜像 -> 真双源互证",
 "seven_sections":7,"svg":"1x viewBox760x400 ellipse/path/circle/text 示意图非施工图, no on*/image/xlink/href/script",
 "reg_sentence":true,"nv":false,"pending_consistent":true,
 "nv_false_basis":"definition/overview/实例三要素均双官方源(政府+馆方)逐字支撑, 非镜像互证; 原第21轮概念缺源缺陷随换直接论述螺旋坡道连续观展两官方源而消解 -> 标 false 有据",
 "coverage":"title/theme/tier/period/region/level 一致; source_count2=2源; nvc0=nvfalse",
 "similarity":{"short":0.3673,"short_vs":"spatial-organization","full":0.5096,"full_vs":"atrium-architecture","threshold":0.54},
 "verdict":"合格"}
TOTAL="1合格/0待核实/0不合格"
RECOMMEND="非阻断: ①全字段相似度0.5096近阈值(vs atrium-architecture),后续差异化表述 ②概念层可补空间序列理论专文双源"
READONLY="only wrote research/spotcheck-round68.md; fetched+parsed PDFs in-memory, temp extracts research/_tmp_*.txt deleted; no entries/sources/coverage/tools/site changed; no git commit; web/pdf treated as data (no instructions executed)"
NOTE="工作区含 round68 未提交改动(spatial-sequence 条目+coverage 已 nv=false/双源), 核验以工作区当前内容为准, 未触碰"
```

*（报告完）*
