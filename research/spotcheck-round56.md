# 第56轮质量抽检报告（spotcheck-round56）——第56轮补具名实例的 3 条（gestalt-organization-laws / environmental-psychology / intimate-scale）

- 抽检人：spotcheck-r56（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 17:22–17:35，Asia/Hong_Kong。
- 任务：对第56轮「补具名实例」条目中 lead 定点的 3 条——`gestalt-organization-laws`（`entries/batch-07.json` 6–38 行）、`environmental-psychology`（`entries/batch-07.json` 74–106 行）、`intimate-scale`（`entries/batch-37.json` 70–100 行）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动；核对相似度（阈值 0.54）。来源均在 `data/sources.json`。
- 抽样说明：第56轮工作树改动含 8 条补具名实例条目（`review-round56a.md` 4 条：gestalt-organization-laws / color-psychology / environmental-psychology / east-west-color-compare；`review-round56b.md` 4 条：monumental-scale / intimate-scale / tints-shades / split-primary），本轮抽检 lead 定点 3 条，占 3/8=37.5%，高于 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限。其余本轮改动条目只作状态观察，不列入内容判定。
- 协议依据：`AUTONOMOUS.md` §E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14/D16。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓、后断言；关键句均按本轮 web_fetch / urllib 实抓正文回读为准）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 17:22 起）**：`data/sources.json` 含 **446** 条来源（`verified=true` 443、`verified=false` 3、`link_ok=false` 6）；`coverage.json`=`total=258`、实读 258 条、`pending_sum`=**194**；`entries/batch-07.json`=15827B、`entries/batch-37.json`=46935B。
- **`git log -1`** = `d99f17b docs: note round55 push status`；第56轮改动尚未提交。`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-07.json`、`M batch-37.json`、`M batch-38.json`、9 个 `site/entries/*.html`、`site/index.html`、`site/sources.html`，以及 `?? research/review-round56a.md`、`?? review-round56b.md`、`?? tools/apply_review_round56.py`（lead 侧底稿/脚本，本抽检不触碰）。抽检对象即上述未提交工作树中的 3 条现状，非 HEAD 内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（`open(...,'w')`/`write_text`/`.write(`/`shutil`/`unlink`/`os.remove` 均 0 命中）。
- **只读声明**：本次**仅写出** `research/spotcheck-round56.md` 一个项目文件；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`review-round56a.md`、`review-round56b.md`、`tools/apply_review_round56.py` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容（抓取全程内存，临时文件即用即删）。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round55.md`（230 行）、`research/review-round56a.md`（98 行）、`research/review-round56b.md`（116 行）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾；SVG 元素不出 `viewBox`、无 `on*` 事件属性、无外链图片。
- **抓取与回验方法**：`web_fetch` 本轮对 PPS、MAS、Britannica（格式塔）、表千家 Tai-an、Another Kyoto 妙喜庵多页成功（HTTP 200，全文可见关键句）；Niels Bohr Archive 页 `web_fetch` 报 `fetch failed`，按 D05 改 `urllib` + 浏览器 UA 直连，HTTP 200（2315B），全文可见关键句；6 个 Wikipedia 概念源 `urllib` 直连全部 HTTP 200。关键句按大小写/空白/标点归一（`html.unescape` → 去标签 → 折叠空白）做上下文回读，并与 `review-round56a/b.md` 同日逐字回执交叉核对。
- **三级判定定义（沿用第51–55轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项（七节/SVG/规范句/元数据/pending 联动）全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源/无源，或第二源只覆盖部分结构且单源/概念归纳未如实披露；或 overview 含具体体验/机制主张无来源正文支撑——属来源深度或披露缺陷，非编造。`needs_verification=true` 且 pending/正文如实披露者，属「正确的待核实管理」，判待核实但无治理缺陷。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，按 `sections` 原始插入顺序、`一图` 解说文字计入、`svg` 标记不计入），归一为去空白+小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–55轮报告逐位一致，口径正确。
- **相似度是独立维度**：超线触发 §E「整批降级」，与「不合格（内容无源）→整批返工」是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

3 条共引用 **12 个来源 id（12 处引用，每条 4；无跨条目共用）**，全部存在、全部 `verified=true`、`year=null`（D06 允许）、无 `link_ok=false`（本轮新登记 6 源 `link_ok=null` 三态未标，非死链；6 个 Wikipedia 源 `link_ok=true`）。

| 条目 | 来源 id | 机构 / type | 实抓标题或端点（本轮证据） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| gestalt | `wp-visual-perception` | Wikipedia / 权威百科 | `Visual perception - Wikipedia`（HTTP 200，529717B） | true / true | **相关（概念背景）**：`grouping`×2、`proximity`、`similarity`×3、`closure`、`gestalt`×11 |
| gestalt | `wp-gestalt-psychology` | Wikipedia / 权威百科 | `Gestalt psychology - Wikipedia`（HTTP 200，453961B） | true / true | **相关（概念背景）**：`proximity`×10、`similarity`×12、`closure`×12、`figure-ground`×6、`whole`×19 |
| gestalt | `nba-rubin-vase` | Niels Bohr Archive / 学术档案机构 | `NBA: seminars :Thursday 12 February 2015`（urllib HTTP 200，2315B） | true / null | **相关（直接·实例唯一源）**：`Rubins vase is probably one of the best known figures in psychology`、`Edgar Rubin (18861951)`、`Synsoplevede Figurer ... from 1915`、`figure-ground problem`、`University of Copenhagen`、`Blegdamsvej 17, Copenhagen` |
| gestalt | `britannica-gestalt` | Britannica / 权威百科署名条目 | `Perception - Primary Tendencies, Organization`（HTTP 200） | true / null | **相关（直接·概念主证·非鲁宾专页）**：`Gestalt principles of perceptual organization`、`proximity`/`similarity`/`closure`/`symmetry`/`continuity`、`Patterns take precedence over elements`、`The whole is more than the sum of its parts`、`created by the perceptual system` |
| environmental | `wp-landscape-architecture` | Wikipedia / 权威百科 | `Landscape architecture - Wikipedia`（HTTP 200，505575B） | true / true | **弱相关（概念背景）**：`natural`×10、`built`×2、`environment`×58 |
| environmental | `wp-environmental-psychology` | Wikipedia / 权威百科 | `Environmental psychology - Wikipedia`（HTTP 200，487734B） | true / true | **相关（概念主证）**：`natural`×17、`built environment`×7、`behavior`×65、`well-being`×8、`place`×51 |
| environmental | `pps-whyte-plazas` | Project for Public Spaces / 公共空间机构 | `What Holly Whyte's "Social Life" Film Can Teach Us Today`（HTTP 200） | true / null | **相关（直接·实例主证）**：`Seagram Building Plaza, one of 12 plazas William H. Whyte observed for the Street Life Project study, circa 1970s`、`People tend to sit where there are places to sit`、`originally produced the 16mm film in 1980` |
| environmental | `mas-whyte-plazas` | Municipal Art Society of New York / 城市公共空间机构 | `The Social Life of Small Urban Spaces – MAS`（HTTP 200） | true / null | **相关（直接·实例佐证）**：`William H. "Holly" Whyte's 1980 film`、`breakthrough 1980 Street Life Project study of New York's plazas`、`observing – and recording – the actual behavior of city dwellers` |
| intimate | `wp-proportion-architecture` | Wikipedia / 权威百科 | `Proportion (architecture) - Wikipedia`（HTTP 200，162464B） | true / true | **相关（概念背景）**：`human scale`、`proportion`×37、`body`×13 |
| intimate | `wp-architecture` | Wikipedia / 权威百科 | `Architecture - Wikipedia`（HTTP 200，623722B） | true / true | **弱相关（概念背景）**：`human`×14、`scale`×4 |
| intimate | `omotesenke-taian` | 表千家不審菴 / 茶道流派官方 | `Tai-an`（HTTP 200，1951B） | true / null | **相关（直接·实例主证）**：`The one tea house remaining that is certainly Rikyu's. A national treasure.`、`located in Myoki-an in Kyoto prefecture's Oyamazaki-cho`、`a two mat room`、`nijiriguchi (crawl-through entrance)`、`It is said that it was built in Tensho 10 (1582)` |
| intimate | `kyoto-taian` | Another Kyoto 京都府官方旅游站 | `妙喜庵（待庵） \| 旅遊景點 \| Another Kyoto`（HTTP 200，55916B） | true / null | **相关（直接·实例佐证）**：`千利休唯一現存的茶室`、`天正10年（1582年）`、`大小為2帖榻榻米，打破了當時4帖半的概念`、`第一個設立了「躙口」`、`京都府乙訓郡大山崎町大山崎龍光56` |

> 12 源全部 `verified=true`、无假 id、无 `link_ok=false`。关键相关性结论：`environmental-psychology`、`intimate-scale` 的实例四要素均获双源直证；`gestalt-organization-laws` 的 definition/overview 获 Britannica + 两 Wikipedia 多源支撑，但**实例四要素仅 Niels Bohr Archive 一源直证**，Britannica 已如实标注为概念背景源、非该图专页。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 gestalt-organization-laws（格式塔组织律，第56轮改动）——**待核实**

- 条目现状（实读 `entries/batch-07.json` 6–38 行）：`definition`＝「视觉系统按邻近、相似、闭合、对称与连续等原则把局部组织为整体的规律。」；`time_or_place`＝「20世纪、全球（参见来源）。」；`overview`＝「格式塔组织律为构图法则与图底关系提供了上位解释。」；`实例`＝「名称：鲁宾花瓶（Rubin's vase）；地点：丹麦哥本哈根；设计者：埃德加·鲁宾（Edgar Rubin）；年份：1915 年。图与底可互换……」
- **definition / overview 支撑（扎实·多源）**：Britannica 本轮 HTTP 200 正文逐字给出 `Gestalt principles of perceptual organization`、`proximity`、`similarity`、`closure`、`symmetry`、`continuity`、`good continuation`，并以 `Patterns take precedence over elements and have properties that are not inherent in the elements themselves`、`The whole is more than the sum of its parts`、`such emerging patterns ... are created by the perceptual system; that is, by the perceiver himself` 直证「整体先于局部被感知／视觉系统组织」；两 Wikipedia 概念源 `grouping/proximity/similarity/closure` 与 `figure-ground` 命中互证。`overview` 的「上位解释」由 Britannica 组织原则总论支撑，「图底关系」由 Britannica figure-ground 语境与 NBA `figure-ground problem` 支撑。非编造。
- **实例四要素（实质单源·已如实披露）**：
  - Niels Bohr Archive（本轮 urllib HTTP 200，2315B）：`Rubins vase is probably one of the best known figures in psychology`（名称；页面纯文本层撇号丢失，标题作 `Rubin's vase and early psychology in Denmark`）、`Edgar Rubin (18861951)`（设计者，连字符在纯文本层丢失）、`from 1915`（年份）、`Blegdamsvej 17, Copenhagen` + `Rubin was educated at the University of Copenhagen`（地点：讲座页地点 + 鲁宾哥本哈根大学学术语境）→ 名称、设计者、年份、地点四项均由同一机构直证。
  - Britannica 格式塔页**不含鲁宾花瓶的作者/年份**（底稿 §1 与本轮回验一致），只作概念背景；两 Wikipedia 为概念源，非该图专页。故实例四要素**实质单源**。
  - 该条 `needs_verification=true`、`pending_notes` 与正文「待核实」均写明「鲁宾花瓶由 Niels Bohr Archive 单源直证；Britannica 为格式塔组织原则概念背景源，非该图专页」→ 单源事实已如实披露，符合底稿 §1 诚实标注落地要求，不构成隐瞒。
- **七节其他内容**：`原理`「视觉会把邻近、相似、连续、闭合的元素自动归组，整体先于局部被感知」由 Britannica 直证（与 earth-sheltered 的逐字重复不同，本条提供了独立机制表述）；`典型手法与适用条件`「用间距、相似形与连续线引导分组」由 Britannica proximity/similarity/good continuation 支撑。
- **无编造**：核心定义、overview、鲁宾花瓶四要素均由引用来源正文支撑；设计者/年份不凑第二源而如实标单源；不复制图像。
- **问题（轻微）**：① 实例四要素实质单源（NBA），但已披露，按 constructivism 同类口径判待核实；② `time_or_place`「20世纪」为通识分类，Britannica 未逐字给该口径，无具体数字人名，可接受；③ 4 个新登记源 `link_ok=null` 三态未标，已如实标。
- **内容判定：待核实（正确的待核实管理）**。`needs_verification=true` ↔ pending ↔ 正文「待核实」三者一致且披露诚实；无治理缺陷。

### 3.2 environmental-psychology（环境心理学，第56轮改动）——**合格**

- 条目现状（实读 `entries/batch-07.json` 74–106 行）：`definition`＝「研究自然与建成环境如何影响人的体验与行为的领域。」；`time_or_place`＝「20世纪、全球（参见来源）。」；`overview`＝「该领域把空间感知、场所情感与使用行为纳入统一框架。」；`实例`＝「名称：西格拉姆大厦广场／Whyte 街头生活项目；地点：美国纽约；设计者：威廉·H·怀特（William H. Whyte）；年份：1970 年代观察、1980 年发布。通过实地观察研究人在城市广场的行为。……」
- **definition / time / overview 支撑**：`wp-environmental-psychology` 本轮 HTTP 200 正文 `natural`×17、`built environment`×7、`behavior`×65、`well-being`×8、`place`×51 → 「自然与建成环境」「体验与行为」直接支撑；`wp-landscape-architecture`（natural/built/environment）作背景。`overview` 的「空间感知／场所情感／使用行为统一框架」由 place、behavior、well-being 命中组合支撑（属概念归纳，无具体数字/引文，可接受）。非编造。
- **实例双源直证**：
  - PPS（本轮 HTTP 200）：`A photo still from the Social Life film featuring the Seagram Building Plaza, one of 12 plazas William H. Whyte observed for the Street Life Project study, circa 1970s`（名称、研究者、1970s）、`People tend to sit where there are places to sit`、`originally produced the 16mm film in 1980`（发布年份）→ 名称、地点（纽约广场语境）、人物、年份逐字直证。
  - MAS（本轮 HTTP 200）：`William H. "Holly" Whyte's 1980 film`、`his breakthrough 1980 Street Life Project study of New York's plazas`、`Whyte and his team's dedication to observing – and recording – the actual behavior of city dwellers`、`insights into the ways city dwellers interact with the urban environment` → 从机构史与影片/研究报告角度独立佐证同一实例的年份、研究者、实地观察方法。
  - 两源为不同法人机构（PPS + MAS，曾合作修复影片但独立计源，符合底稿 §3 判定），四要素双源互证；底稿 §3 诚实标注已落地（广场名来自 PPS，项目年份由 MAS 覆盖）。
- **七节其他内容**：`原理`「研究人如何感知、使用并回应自然与建成环境，关注私密性、领域感与压力恢复」由 `wp-environmental-psychology`（behavior/place/well-being）支撑；`典型手法与适用条件`「空间层次、可控制感与自然元素」与 PPS「sittable space／可坐面积」观察结论相容。
- **无编造**：核心定义、overview、西格拉姆广场／Whyte 项目四要素均由引用来源正文支撑；不复制图像。
- **问题（轻微）**：① 实例字段用「设计者：威廉·H·怀特」，但 Whyte 实为研究者／项目主持者而非广场的建筑师（西格拉姆大厦建筑师为 Mies van der Rohe）——条目未声称 Whyte 设计了建筑，列其为「街头生活项目」研究者可接受，建议把字段措辞改为「研究者／项目主持」以免误导；② `wp-landscape-architecture` 与本条核心关联弱，建议注明为概念背景；③ 2 个新登记源 `link_ok=null` 已标。
- **内容判定：合格**。`needs_verification=false`、pending 空、待核实「暂无已知待核实项。」与双源实况一致。

### 3.3 intimate-scale（亲切尺度，第56轮改动）——**待核实**

- 条目现状（实读 `entries/batch-37.json` 70–100 行）：`definition`＝「亲切尺度指以接近人体与日常活动的尺寸营造亲近感。」；`time_or_place`＝「跨时期、全球（参见来源）。」；`overview`＝「它以小尺度细部与柔和光线让人放松。」；`原理`＝「亲切尺度指以接近人体与日常活动的尺寸营造亲近感。它以小尺度细部与柔和光线让人放松。」（**系 definition + overview 逐字重复**）；`实例`＝「名称：待庵茶室；地点：日本京都府大山崎町妙喜庵内；设计者：相传为千利休；年份：天正 10 年（1582 年）。二帖榻榻米、设躙口，尺度极小。……」
- **实例双源直证（扎实）**：
  - 表千家不審菴（本轮 HTTP 200，1951B）：`The one tea house remaining that is certainly Rikyu's. A national treasure.`（设计者）、`located in Myoki-an in Kyoto prefecture's Oyamazaki-cho`（地点）、`a two mat room`（二帖）、`nijiriguchi (crawl-through entrance)`（躙口）、It is said that it was built in `Tensho 10 (1582)`（年份，保留语气）→ 名称、地点、设计者、年份直证。
  - Another Kyoto 京都府官方旅游站（本轮 HTTP 200，55916B）：`妙喜庵內保存千利休唯一現存的茶室，是被指定為國寶的「待庵（たいあん）」之一`、`天正10年（1582年）`、`大小為2帖榻榻米，打破了當時4帖半的概念`、`第一個設立了「躙口」，縮小客人進出用的門`、`京都府乙訓郡大山崎町大山崎龍光56` → 地点、设计者、年份、二帖、躙口逐字直证。
  - 两源为不同机构（茶道流派官方 + 都道府县官方旅游站），四要素双源直证；条目「相传为千利休」保守表述与底稿 §2.2 保留语气一致（表千家对作者用 `certainly`、对年份用 `It is said`，条目统一写「相传」偏保守但非错误）。实例层面无编造。
- **definition / overview 支撑（概念背景 + 部分无源）**：`wp-proportion-architecture`（`human scale`、`body`×13、`proportion`×37）与 `wp-architecture`（`human`×14、`scale`×4）作「接近人体尺寸」的概念背景；实例两源直证「二帖榻榻米、躙口缩小」支撑「小尺度细部」。但 `overview` 的「**柔和光线让人放松**」在所引四源正文中均无直接支撑——属体验性通识归纳，非具体物理机制/数字（与第55轮 earth-sheltered「土壤蓄热」具体机制主张有别，严重度较低），但在 L2 标准下属 overview 中未获正文支撑的主张。
- **七节「原理」逐字重复（次要·套话）**：`原理` 仅复制 definition + overview，未提供独立机制说明，属第54轮起持续关注的「套话/模板」质量问题，`check.py` 查不出该语义项。
- **needs_verification 联动（方向正确·披露不完整）**：`needs_verification=true`、pending 与正文「待核实」均写「设计者与年份为『相传』（表千家官方用 It is said），待补确证来源」→ 实例层面的相传语气已披露，nv=true 方向正确；但 overview「柔和光线让人放松」无源未在 pending/待核实中披露，披露不完整。
- **其他（轻微）**：① `time_or_place`「跨时期」为通识分类，无具体数字；② `wp-architecture` 与本条关联弱，建议注明为概念背景；③ 2 个新登记源 `link_ok=null` 已标。
- **内容判定：待核实**。建议：把 overview 改写为有源表述（如「以二帖小间、躙口等贴近人体的极小尺度营造内敛亲近感」）或补一权威源直证「柔和光线让人放松」，并据此重写「原理」；若保留现表述，则在 pending/待核实补披露该无源主张。nv=true 已置，联动方向无需回退。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：12 个来源 id 全部存在、`verified=true`；`year=null`（D06 允许）；6 个新登记源 `link_ok=null`（三态未标），6 个 Wikipedia 源 `link_ok=true`；无 `link_ok=false`。无假 id。
- **可达性（本轮实抓）**：12/12 URL 本轮取得正文（11 个 web_fetch 200 + Niels Bohr Archive 经 urllib 200；6 个 Wikipedia 经 urllib 200）；Niels Bohr 页 `web_fetch` 报 `fetch failed`（服务端抓取异常），按连接异常而非死链处理，urllib 同页 200 且关键句逐字可见。`link_ok=null` 未标 true 属三态保守，不影响证据效力。
- **相关性结论**：
  - `gestalt-organization-laws`：Britannica + 两 Wikipedia 支撑组织律概念；Niels Bohr Archive 直证鲁宾花瓶四要素（单源，已披露）。
  - `environmental-psychology`：PPS + MAS 双源直证西格拉姆广场／Whyte 项目四要素；`wp-environmental-psychology` 支撑核心定义，`wp-landscape-architecture` 为背景。
  - `intimate-scale`：表千家 + Another Kyoto 双源直证待庵四要素；两 Wikipedia 作「人体尺度」概念背景；overview「柔和光线让人放松」四源无支撑。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gestalt-organization-laws | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| environmental-psychology | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |
| intimate-scale | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械项三条全部通过。**

- **SVG 质量观察**：
  - `gestalt-organization-laws`：三圆成组 + 一圆异组，标「邻近即成组」，主题贴合；无具体尺寸标注（本批无尺寸数据，可接受）。
  - `environmental-psychology`：人—环境互动示意，标「人」「环境」，主题贴合；无具体尺寸标注，可接受。
  - `intimate-scale`：低层高剖面轮廓，标「亲切尺度」，主题贴合。
  - **判定**：机械项与主题贴合均过；延续第44–55轮观察——三条图示均缺显式「设计意图/尺寸关系」文字标注，`check.py` 查不出该语义项，属系统性次要问题。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对全部 True，无 MISMATCH）；`source_count` 与来源数组长度一致（4=4、4=4、4=4）。`needs_verification_count`：gestalt=1、environmental=0、intimate=1，与条目 `needs_verification` 逐条对应。
- `git diff` 显示本轮 8 条补具名实例条目中，`environmental-psychology` 与 `east-west-color-compare` 两条 `needs_verification` 由 true→false，`pending_sum` 第55轮 195 → 本轮 **194**（-1，净变化含其他条目调整）。存量待核实占比 194/258≈75.2%，处历史高位。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| gestalt-organization-laws | true（保持） | 「鲁宾花瓶由 Niels Bohr Archive 单源直证；Britannica 为概念背景源，非该图专页。」 | 同 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：单源事实如实披露，保持待核实正确。 |
| environmental-psychology | **false（本轮清零）** | "" | 「暂无已知待核实项。」 | **结构一致 ✓、内容恰当 ✓**：四要素双源直证，清零恰当。 |
| intimate-scale | true（保持） | 「设计者与年份为『相传』（表千家官方用 It is said），待补确证来源。」 | 同 pending 逐字一致 | **结构一致 ✓、内容部分恰当**：实例相传语气已披露；overview「柔和光线让人放松」无源未披露。 |

> **异常监控（§E）**：全库 `pending_sum` 由第55轮 195 降至本轮 **194**（-1，0.51%）。存量待核实占比 194/258≈75.2%，处历史高位，**不触发「待核实占比异常低（疑似硬写）」降级**；本轮两条清零均有双源直证支撑（`environmental-psychology` 本轮抽检确认 PPS+MAS 双源扎实），属有据清零，非硬写。

## 七、任务 5：相似度（difflib 去空白+小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| gestalt-organization-laws | **0.3333** vs spatial-organization | <0.54 ✓ | **0.3348** vs international-style | <0.54 ✓ |
| environmental-psychology | **0.4783** vs color-psychology | <0.54 ✓ | **0.4033** vs art-deco | <0.54 ✓ |
| intimate-scale | **0.4500** vs monumental-scale | <0.54 ✓ | **0.3703** vs monumental-scale | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。最高为 environmental-psychology 短文本 0.4783（vs color-psychology，两条同为「理论」主题、同为「研究…的领域」定义句式，属正常近邻，非套话；全字段仅 0.4033，内容分化明显）。

### 7.2 第56轮批内 3 条两两（全字段② / 短文本①）

- gestalt-organization-laws vs environmental-psychology：全字段 **0.2970**、短文本 0.2740。
- gestalt-organization-laws vs intimate-scale：全字段 **0.2771**、短文本 0.2353。
- environmental-psychology vs intimate-scale：全字段 **0.2665**、短文本 0.2381。
- → 批内两两均远低于 0.54，无套话/模板姊妹风险。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–55轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **gestalt-organization-laws（格式塔组织律）** | definition/overview 由 Britannica + 两 Wikipedia 多源直证；鲁宾花瓶四要素由 Niels Bohr Archive 单源直证且已如实披露；无编造 | 4/4 true；12/12 本轮可达（NBA 经 urllib）；概念源背景、实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」 | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.3333/0.3348）；批内 ✓ | **待核实** |
| **environmental-psychology（环境心理学）** | definition/overview 由 wp-environmental-psychology 直证；西格拉姆／Whyte 四要素由 PPS + MAS 双源直证；无编造 | 4/4 true；实例源本轮 200 且直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」 | 全部一致；nv=false 清零恰当 | 全库 ✓（0.4783/0.4033）；批内 ✓ | **合格** |
| **intimate-scale（亲切尺度）** | 待庵四要素由表千家 + Another Kyoto 双源直证；definition 概念背景支撑；**overview「柔和光线让人放松」四源无支撑、原理逐字重复 definition+overview** | 4/4 true；实例源本轮 200 且直接相关；两 Wikipedia 为背景 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」 | 元数据一致；nv=true 方向正确，但 overview 无源未披露 | 全库 ✓（0.4500/0.3703）；批内 ✓ | **待核实** |

### 问题清单

- **① gestalt 实例四要素实质单源（判待核实主因·已如实披露）**：鲁宾花瓶名称/作者/年份/地点仅 Niels Bohr Archive 直证，Britannica 明确非该图专页、两 Wikipedia 非实例源。已标 `needs_verification=true` 且 pending/正文如实披露，属「正确的待核实管理」，无治理缺陷；如需升级为合格，须补一独立机构来源直证鲁宾花瓶作者/年份。
- **② intimate-scale overview「柔和光线让人放松」无来源正文支撑（判待核实主因）**：表千家、Another Kyoto、两 Wikipedia 均无该表述。建议改写为有源表述（如「以二帖小间、躙口等贴近人体的极小尺度营造内敛亲近感」），或补权威源直证，并在 pending/待核实披露。
- **③ intimate-scale 原理逐字重复 definition+overview（次要·套话）**：随问题②一并重写，消除重复。
- **④ environmental-psychology 实例「设计者：威廉·H·怀特」措辞（轻微）**：Whyte 为研究者/项目主持，非广场建筑师；建议改字段为「研究者／项目主持」以免误导（不影响判定）。
- **⑤ environmental / intimate 概念源关联弱（轻微）**：`wp-landscape-architecture`、`wp-architecture` 与本条核心关联弱，建议注明概念背景或替换。
- **⑥ 全站系统性次要项**：三条 SVG 均缺显式「设计意图/尺寸关系」标注，`check.py` 查不出该语义项，建议全站统一补强（延续第44–55轮方向）。
- **⑦ 三态与可达性（轻微）**：6 个新登记源 `link_ok=null` 已标；Niels Bohr 页 `web_fetch` 失败但 urllib 200，按连接异常处理、非死链。

## 九、总体结论与建议

- **抽样结果**：第56轮补具名实例条目中抽检 3 条——`gestalt-organization-laws`、`environmental-psychology`、`intimate-scale`。**内容维度：1 合格（environmental-psychology）＋2 待核实（gestalt-organization-laws、intimate-scale）＋0 不合格；实例层面 0 编造、0 假 id、0 死链证据。**
- **来源层面**：12 个引用来源 id 全部存在、`verified=true`、本轮全部取得正文（Niels Bohr 经 urllib）。`environmental-psychology`、`intimate-scale` 的实例四要素均获双源直证；`gestalt-organization-laws` 的 definition/overview 获 Britannica + 两 Wikipedia 多源支撑，唯实例四要素实质单源（已如实披露）；`intimate-scale` 的 overview 含一处无源体验主张。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 唯一性与 theme 贴合通过、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：三条结构一致；`environmental-psychology` 清零恰当；`gestalt-organization-laws` 保持 true 且披露诚实；`intimate-scale` 保持 true 方向正确但 overview 无源未披露。全库 pending_sum 195→194（-1），存量占比 75.2% 处高位，不触发「占比异常低」降级。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4783、全字段最高 0.4033）；方法自校 0.5157 与第39–55轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（1 合格 + 2 待核实），0 实例编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——存量待核实占比 75.2% 处高位，本轮两条有据清零，非整批硬写。
  4. **结论：本轮 1 条合格、2 条待核实，不触发整批返工/降级。** 两条待核实均为「来源深度/披露缺陷」而非编造：`gestalt-organization-laws` 已是「正确的待核实管理」，`intimate-scale` 需补 overview 披露/有源改写。
- **返工/修复建议（定向、非整批）**：
  1. **（问题②，优先）`intimate-scale`**：将 overview「柔和光线让人放松」改写为有源表述或补权威源直证，据此重写逐字重复的「原理」；保留 `needs_verification=true`，在 pending/待核实补披露该主张（若改写后全部有源且实例双源，可评估清零）。
  2. **（问题①）`gestalt-organization-laws`**：保持待核实；可补一独立机构来源直证鲁宾花瓶作者/年份以升级为合格，否则维持现状（当前披露已诚实，无需回滚）。
  3. **（问题④）`environmental-psychology`**：保持合格；建议把实例「设计者」字段改为「研究者：William H. Whyte」，避免与广场建筑师混淆。
  4. **（问题⑤）**：把 `wp-landscape-architecture`/`wp-architecture` 注明为概念背景，或替换为直接相关来源。
  5. **（问题⑥，系统性）**：全站统一补「设计意图或尺寸关系」SVG 标注。

### 机器可读汇总

```
ROUND=56
SAMPLER=spotcheck-r56
MODE=第56轮补具名实例条目中lead定点抽3条（gestalt-organization-laws / environmental-psychology / intimate-scale）
SCOPE=["gestalt-organization-laws","environmental-psychology","intimate-scale"]
FILES={"gestalt-organization-laws":"entries/batch-07.json","environmental-psychology":"entries/batch-07.json","intimate-scale":"entries/batch-37.json"}
GIT_HEAD="d99f17b"; ROUND56_COMMITTED=false; GIT_STATUS="round56 changes UNCOMMITTED as found (M coverage/data/sources/entries/batch-07/37/38 + site/*; ?? review-round56a.md, review-round56b.md, apply_review_round56.py - lead notes, untouched)"
STATE={"sources.json":"446 sources, verified_true=443, verified_false=3, link_ok_false=6","coverage.json":"total=258","batch-07.json":"15827B","batch-37.json":"46935B","pending_sum":194,"sources_total":446}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements (grep 0 hits)"
SAMPLE_RATIO="3/8 (37.5%, lead 定向抽检)"
FETCH_METHOD="web_fetch 200 for PPS/MAS/Britannica-gestalt/Omotesenke/Another-Kyoto; nba-old.nbi.dk web_fetch 'fetch failed' -> urllib 200 (2315B) full text; 6 Wikipedia via urllib 200; quote readback via html.unescape+de-tag+fold; in-memory; only this report written"
SOURCES={"count_distinct_ids":12,"count_distinct_urls":12,"count_refs":12,"all_exist":true,"all_verified_true":true,"link_ok_false":0,"link_ok_null_new":6,"link_ok_true_wikipedia":6}
BODY_SUPPORT={
 "gestalt-organization-laws":"definition/overview Britannica('Gestalt principles of perceptual organization'/'proximity similarity closure symmetry continuity'/'Patterns take precedence over elements'/'whole more than sum of parts')+2 Wikipedia(grouping/figure-ground); Rubin vase four facts NBA single source('Rubins vase...best known figures'/'Edgar Rubin (18861951)'/'from 1915'/'Blegdamsvej 17, Copenhagen'+'University of Copenhagen'); Britannica NOT vase-specific; VERDICT=待核实 (instance four facts single-source but honestly disclosed, nv=true proper)",
 "environmental-psychology":"definition wp-environmental-psychology('natural'17/'built environment'7/'behavior'65/'place'51); Seagram Plaza/Whyte four facts PPS('Seagram Building Plaza, one of 12 plazas William H. Whyte observed...circa 1970s'/'film in 1980')+MAS('William H Holly Whyte's 1980 film'/'1980 Street Life Project study of New York's plazas'); VERDICT=合格 (minor: 'designer' should read researcher)",
 "intimate-scale":"Taian four facts Omotesenke('certainly Rikyu's'/'Myoki-an in Kyoto prefecture's Oyamazaki-cho'/'two mat room'/'nijiriguchi'/'Tensho 10 (1582)')+Another Kyoto('千利休唯一現存的茶室'/'天正10年（1582年）'/'2帖榻榻米'/'躙口'/'大山崎町大山崎龍光56'); BUT overview '柔和光线让人放松' UNSUPPORTED in all 4 cited sources, 原理 verbatim duplicates definition+overview; VERDICT=待核实"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3, 无on*/无外链图, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_issue":"no explicit design-intent/dimension annotation site-wide (systemic minor)"}
METADATA={"field_match_coverage":"ALL True x3","source_count":"4=4 x3","nvc":"gestalt=1, environmental=0, intimate=1; git diff: 2 entries true->0 (environmental, east-west-color-compare), pending_sum 195->194 (-1, 0.51%), stock ratio 194/258=75.2% (high, not anomalous-low)","needs_verification":"gestalt=true proper (single-source disclosed); environmental=false proper (dual-source); intimate=true proper direction but overview unsourced not disclosed"}
SIMILARITY={
 "gestalt-organization-laws":{"vs_all_short":0.3333,"short_entry":"spatial-organization","vs_all_full":0.3348,"full_entry":"international-style","verdict":"PASS<0.54"},
 "environmental-psychology":{"vs_all_short":0.4783,"short_entry":"color-psychology","vs_all_full":0.4033,"full_entry":"art-deco","verdict":"PASS<0.54"},
 "intimate-scale":{"vs_all_short":0.4500,"short_entry":"monumental-scale","vs_all_full":0.3703,"full_entry":"monumental-scale","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.2970,"intrabatch_full_max_pair":"gestalt vs environmental",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-55 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"gestalt-organization-laws":"待核实","environmental-psychology":"合格","intimate-scale":"待核实"}
VERDICT_PENDING={"gestalt-organization-laws":"proper (nv=true, single-source honestly disclosed)","environmental-psychology":"proper (dual-source, nv=false cleared)","intimate-scale":"direction proper (nv=true) but overview unsourced not disclosed"}
HARD_FABRICATION_INSTANCE=0
UNSOURCED_CLAIM=1
FAKE_ID=0
LINK_FAIL=0
ANOMALY_NVC="pending_sum 195->194 (-1, 0.51%); stock ratio 75.2% high -> no anomalous-low downgrade; 2 evidenced clears this round"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (1合格+2待核实), 0 instance fabrication/0 fake id/0 dead link; similarity all <0.54; pending stock high. Targeted fixes: (1) intimate-scale rewrite/disclose unsourced '柔和光线' overview + verbatim 原理; (2) gestalt keep 待核实 or add independent source for Rubin vase author/year; (3) environmental change instance 'designer' to 'researcher'; (4) mark weak Wikipedia concept sources as background; (5) add design-intent/dimension annotations site-wide."
READONLY="only wrote research/spotcheck-round56.md; no other project content file changed; no git commit; round56 work remains uncommitted as found; web content treated as data, no instruction executed; temp fetch in-memory, no files written outside deliverable"
```

*（报告完）*
