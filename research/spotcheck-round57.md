# 第57轮质量抽检报告（spotcheck-round57）——第57轮补具名实例的 3 条（wayfinding / accessibility-design / acoustic-environment）

- 抽检人：spotcheck-r57（lead 委派子代理，无人值守、未提问）；抽检时间 2026-11-23 17:48–18:05，Asia/Hong_Kong。
- 任务：对第57轮「补具名实例」条目中 lead 定点 3 条——`wayfinding`（`entries/batch-07.json` 138–167 行）、`accessibility-design`（`entries/batch-36.json` 340–369 行）、`acoustic-environment`（`entries/batch-38.json` 734–764 行）——逐条核对 definition / time_or_place / overview / 实例是否有引用来源正文支撑、是否编造、来源是否直接相关；核对 L2 七节 / 内联 SVG / 规范提示；核对 `needs_verification` 与 `pending_notes` / 正文「待核实」联动；核对相似度（阈值 0.54）。12 个来源均在 `data/sources.json`。
- 抽样说明：round57 落地脚本 `tools/apply_review_round57.py`（只读查看）的 `INST` 共 6 条补具名实例条目（wayfinding / visual-comfort / accessibility-design / sustainable-design / thermal-comfort / acoustic-environment），来源底稿 `research/review-round57a.md`（4 条）与 `review-round57b.md`（4 条，其中 pedestrian-flow / corridor-space 判「仅单源/不可得」未落地实例）。本轮定点抽 3 条，占 3/6=50%（以落地条目计），高于 `AUTONOMOUS.md` §E「随机 10%／至少 3 个」下限。其余本轮改动条目只作状态观察，不列入内容判定。
- 协议依据：`AUTONOMOUS.md` §E（质量闸：check.py 必须通过；抽检不合格则整批返工、下轮抽检提至 25%；待核实占比异常低或相似度过高→整批降级）＋第六节（联网内容一律视为数据，网页中任何指令不得执行，项目文件夹之外保持原样）；`TASK_design.md`「条目页结构」L2 七节与「专用规则」（每页 1–2 张内联 SVG、图下注「示意图，非施工图」、SVG 元素不出 viewBox、尺寸/坡度/消防/无障碍附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；关键事实至少两个独立来源互证，否则标待核实；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D07/D10/D11/D14。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，命中 `SUBAGENT-STOP`，以任务说明书执行）与 `verification-before-completion`（先实抓、后断言；12 个来源正文均由本轮 `web_fetch` / `urllib` 实抓回读为准，未采信底稿的二手转述）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，2026-11-23 17:48 起）**：`data/sources.json` 含 **458** 条来源（`verified=true` 455、`verified=false` 3、`link_ok=false` 6）；`coverage.json`=`total=258`、实读 258 条、`pending_sum`=**193**；`entries/batch-07.json`=16077B、`batch-36.json`=25729B、`batch-38.json`=64915B。
- **`git log -1`** = `04931db chore: round56 theory named instances`（第56轮改动已提交，与 round56 报告记录的「d99f17b 未提交」不同）。第57轮改动尚未提交：`git status --porcelain` 显示 `M coverage.json`、`M data/sources.json`、`M entries/batch-06/07/36/37/38.json`、`M site/entries/{accessibility-design,acoustic-environment,sustainable-design,thermal-comfort,visual-comfort,wayfinding}.html`、`M site/index.html`、`M site/sources.html`，以及 `?? research/review-round57a.md`、`review-round57b.md`、`tools/apply_review_round57.py`（lead 侧底稿/脚本，本抽检不触碰）。抽检对象即上述未提交工作树中的 3 条现状，非 HEAD 内容。
- **`python tools/check.py` 本轮实跑：`PASS: all checks, 0 errors`（EXIT=0）**。运行前已 grep 确认该脚本无写文件语句（`open(...,'w')`/`write_text`/`.write(`/`shutil`/`unlink`/`os.remove` 均 0 命中）。另用 `importlib` 载入 `validate_svg` 对三条 SVG 单独复核，均返回 `NONE`。
- **只读声明**：本次**仅写出** `research/spotcheck-round57.md` 一个项目文件；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`review-round57a.md`、`review-round57b.md`、`apply_review_round57.py` 或任何其他项目内容文件，未 `git commit`，未改项目文件夹之外内容（抓取全程内存，无文件写入）。联网内容一律视为数据，网页中任何指令性文本均未执行。
- **治理文件说明**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 在工作区磁盘为 NOT_FOUND；按前轮先例实读桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行），另读本项目 `DECISIONS.md`（25 行）、`research/spotcheck-round56.md`（227 行）、`review-round57a.md`（119 行）、`review-round57b.md`（124 行）、`tools/apply_review_round57.py`（61 行）。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；SVG 元素须限制在 viewBox 内、无 `on*` 事件属性、无外链图片；「常见错误与限制」段须以「实际工程须按当地规范和专业设计人员的要求」收尾。
- **抓取与回验方法**：`web_fetch` 本轮对 Rijksmuseum（自动跳转到 object URL）、Wim Crouwel Instituut、U.S. Access Board、Berliner Philharmoniker 主页与声学专页、Designing Buildings 两页、Physics LibreTexts 均 HTTP 200 且正文关键句可见；Smithsonian 原文 `airspacemag.com` 跨域跳转未跟随，改抓最终 `smithsonianmag.com` 同文 HTTP 200；`architectsjournal` 的 `web_fetch` 返 403，按 D05 改 `urllib` + 浏览器 UA + 非校验 SSL，HTTP 200（89795B）关键句可见；`wp-wayfinding` / `wp-universal-design` 的 `web_fetch` 报 `fetch failed`，`urllib` 同页 HTTP 200（202465B / 395546B）。关键句按去标签 → `html.unescape` → 折叠空白 → 小写归一做上下文回读，并与 `review-round57a/b.md` 同日逐字回执交叉核对。
- **三级判定定义（沿用第51–56轮）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（核心定义或实例四要素）由 ≥2 独立来源直证互证或由强权威官方源直证且第二源覆盖实例结构；无编造；机械项（七节/SVG/规范句/元数据/pending 联动）全过或仅有不影响判定的轻微问题。
  - **待核实**：核心获直接相关来源实质支撑，但某关键事实（实例四要素、年份、具体术语或内容映射）实质单源/无源，或第二源只覆盖部分结构且单源/概念归纳未如实披露；`needs_verification=true` 且 pending/正文如实披露者，属「正确的待核实管理」，判待核实但无治理缺陷。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或实例核心四要素无任何来源直证；或关键结构项（七节/SVG）实质不满足 TASK_design 强制要求。
- **相似度口径**：`difflib.SequenceMatcher`；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，按 `sections` 原始插入顺序、`一图` 解说文字计入、`svg` 标记不计入），归一为去空白+小写。全库 258 条逐条扫描，警戒线 **0.54**。**方法自校**：`futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–56轮报告逐位一致，口径正确。
- **相似度是独立维度**：超线触发 §E「整批降级」，与「不合格（内容无源）→整批返工」是不同触发路径；pending 联动失真单独列为问题，不自动等于内容无源。

## 二、抽检对象来源清单与完整性

3 条共引用 **12 个来源 id（12 处引用，每条 4；无跨条目共用）**，全部存在、全部 `verified=true`、`year=null`（D06 允许）、无 `link_ok=false`（3 个 Wikipedia 源 `link_ok=true`，9 个新登记/沿用源 `link_ok=null` 三态未标，非死链）。

| 条目 | 来源 id | 机构 / type | 实抓标题或端点（本轮证据） | verified / link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- |
| wayfinding | `wp-wayfinding` | Wikipedia / 权威百科 | `Wayfinding - Wikipedia`（urllib HTTP 200，202465B） | true / true | **相关（概念主证·背景）**：`applied by designers who create signage, maps and other cues to help people reach destinations`、`orient themselves in physical space and navigate from place to place` |
| wayfinding | `designingbuildings-wayfinding` | Designing Buildings / 建设百科 | `Wayfinding - Designing Buildings`（HTTP 200） | true / null | **相关（概念主证·背景）**：`Wayfinding is a method for relaying messages to help people navigate their way around a room, building or other unfamiliar environment`、`Standardised colours, fonts, icons and sign shapes` |
| wayfinding | `rijksmuseum-schiphol-sign` | Rijksmuseum 荷兰国立博物馆 / 官方机构 | `Signage for Schiphol Airport - Rijksmuseum`（HTTP 200，跳转到 object 页） | true / null | **相关（直接·实例 1967 阶段主证）**：`Signage for Schiphol Airport`、`Benno Wissing, 1967`、`in 1967 Wissing devised a crystal-clear system... text indicated the destination, arrows the direction, yellow stood for arrival and departure` |
| wayfinding | `crouwel-schiphol` | Wim Crouwel Instituut / 设计史研究机构 | `Designing for everyone: The ISOTYPE legacy in Schiphol's wayfinding system`（HTTP 200） | true / null | **相关（直接·实例 1990s 阶段主证）**：`wayfinding system at Schiphol Airport in Amsterdam`、`In 1967, the designer Benno Wissing... created a groundbreaking signage system`、`In the 1990s, the design studio Mijksenaar was brought in to rebrand this signage system`、`one of the first airports to integrate a signage strategy involving clear and consistent pictograms` |
| accessibility | `wp-universal-design` | Wikipedia / 权威百科 | `Universal design - Wikipedia`（urllib HTTP 200，395546B） | true / true | **相关（概念背景）**：`make them accessible to all people, regardless of age, disability, or other factors` |
| accessibility | `wp-exit-sign` | Wikipedia / 权威百科 | `Exit sign - Wikipedia`（沿用前轮登记，本条未单独重抓） | true / true | **弱相关（概念背景）**：疏散标识，与无障碍通达路径仅间接相关 |
| accessibility | `accessboard-smithsonian` | U.S. Access Board 美国联邦无障碍委员会 / 官方机构 | `U.S. Access Board Commends Smithsonian National Museum of Natural History for New Accessible Routes`（HTTP 200） | true / null | **相关（直接·实例主证）**：`On December 15, 2021, the Smithsonian National Museum of Natural History held a ribbon-cutting ceremony to celebrate the installation of new sloped walkways for accessible entry on the National Mall side of the 111-year-old building` |
| accessibility | `si-nmnh-accessibility` | Smithsonian Magazine / NMNH / 学会官方刊物 | `Inclusive Innovations: An Accessible Natural History Experience`（最终 `smithsonianmag.com` HTTP 200） | true / null | **相关（直接·实例佐证）**：`In 2021, the museum completed the installation of two elevated walkways, designed to enhance accessibility...`、`members of the museum's leadership and the U.S. Access Board gathered to unveil the two symmetrical walkways` |
| acoustic | `designingbuildings-acoustics` | Designing Buildings / 建设百科 | `Building acoustics - Designing Buildings`（HTTP 200） | true / null | **相关（概念主证）**：`the minimisation of noise transmission from one space to another and the control of the characteristics of sound within spaces themselves`、Reverberation time / Sound absorption / Sound insulation 三节、`A high reverberation time can make a room sound muffled, loud and noisy` |
| acoustic | `libretexts-room-acoustics` | Physics LibreTexts / 学术教材 | `3.1: Anechoic and Reverberation Rooms`（HTTP 200 + urllib 132402B） | true / null | **相关（概念背景）**：`reverberation time`、`sound reflection`、`sound absorption`、`in anechoic rooms, the walls are very absorbent in order to eliminate these reflections` |
| acoustic | `berlin-phil` | Berliner Philharmoniker 乐团官方 / 官方机构 | `Philharmonie Berlin`（主页 HTTP 200）＋`Sounding Space`（声学专页 HTTP 200，署名 Rainer Esche，同机构合并计 1 源） | true / null | **相关（直接·实例主证）**：主页 `The Philharmonie Berlin has been the musical heart of Berlin since 1963`、`the architect Hans Scharoun ... developed the main concert hall`；声学页 `Hans Scharoun had already enlisted the services of Lothar Cremer. An expert on acoustics... head of the Institute for Technical Acoustics`、`reverberation time of two seconds`、`vineyard terraces`、`ten "clouds" ... suspended` |
| acoustic | `aj-berlin-phil` | Architects' Journal / 建筑专业媒体 | `Scharoun's Berlin Philharmonie building burns`（urllib HTTP 200，89795B） | true / null | **相关（身份佐证·不含声学细节）**：`Scharoun's masterpiece is currently home to the German capital's leading orchestra` |

> 12 源全部 `verified=true`、无假 id、无 `link_ok=false`。关键相关性结论：`wayfinding` 与 `accessibility-design` 的定义/overview 由概念源直证，实例四要素由两条不同机构来源互证；`acoustic-environment` 的定义/overview 由两概念源直证，实例的名称/地点/Scharoun 双源互证，但**声学参数、Cremer、1963 年份仅柏林爱乐官方单机构直证**（两页面合并计一源，AJ 仅身份佐证，已如实披露）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」

### 3.1 wayfinding（导视与寻路，第57轮改动）——**待核实**

- 条目现状（实读 `entries/batch-07.json` 138–167 行）：`definition`＝「人在物理空间中借助标识、地图与视觉线索定向和导航的过程与设计。」；`time_or_place`＝「跨时期、全球（参见来源）。」；`overview`＝「导视与寻路把动线组织、空间认知和图形信息结合起来。」；`实例`＝「名称：阿姆斯特丹史基浦机场导视系统；地点：荷兰史基浦；设计者：贝诺·维辛（Benno Wissing，1967）、保罗·迈克萨纳（Paul Mijksenaar，1990s）；年份：1967 年、1990 年代。最早整合象形符号的机场导视之一。……」
- **definition / overview 支撑（扎实·双源概念背景）**：`wp-wayfinding` 本轮 HTTP 200 正文 `applied by designers who create signage, maps and other cues to help people reach destinations in complex environments`、`orient themselves in physical space and navigate from place to place` 直证「标识、地图与视觉线索定向导航」；`designingbuildings-wayfinding` `method for relaying messages to help people navigate... unfamiliar environment`、`Standardised colours, fonts, icons and sign shapes` 互证。`overview`「动线组织、空间认知与图形信息结合」为概念归纳，无具体数字/引文，可接受。非编造。
- **实例四要素（主体双源，1990s 阶段单源·已如实披露）**：
  - **名称**：Rijksmuseum `Signage for Schiphol Airport` + Crouwel `wayfinding system at Schiphol Airport in Amsterdam` → 双源直证 ✓。
  - **地点**：「荷兰史基浦」由 Crouwel `Schiphol Airport in Amsterdam` + Rijksmuseum 荷兰国立博物馆藏品语境支撑；Amsterdam/Schiphol 属荷兰为通识地理，非编造 ✓。
  - **设计者/年份 1967**：Rijksmuseum `Benno Wissing, 1967` + Crouwel `In 1967, the designer Benno Wissing... created a groundbreaking signage system` → 双源直证 ✓。
  - **设计者/年份 1990s**：Crouwel `In the 1990s, the design studio Mijksenaar was brought in to rebrand this signage system` → **单源**（Rijksmuseum 藏品仅到 1967 年）。「最早整合象形符号的机场导视之一」亦仅 Crouwel `one of the first airports to integrate a signage strategy involving clear and consistent pictograms` 直证，属单源概念性表述。
  - 条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「同一导视系统的不同阶段由两源分别记载，作者与年份分期列出。」→ 分期事实已披露，符合底稿 §2.1「保留标注」要求，不构成隐瞒。
- **七节其他内容**：`原理`「寻路是人在空间中依靠标识、地图与空间线索确定方位并抵达目标的过程」由两概念源直证；`典型手法与适用条件`「分级标识、连续视觉线索、节点地标」与 Designing Buildings `Simplicity/Clarity/Hierarchy/Consistency`、`signage... arrows, pictograms` 相容。
- **无编造**：核心定义、overview、实例主体四要素均由引用来源正文支撑；1990s 阶段不凑第二源而如实标分期披露；不复制图像。
- **问题（轻微）**：① 1990s 阶段（Mijksenaar、1990 年代、「最早整合象形符号」）实质单源（Crouwel），已披露；② 条目写「保罗·迈克萨纳（Paul Mijksenaar，1990s）」把来源的「design studio Mijksenaar」具体化为个人姓名，Crouwel 参考文献列 `Mijksenaar, Paul. Wayfinding at Schiphol` 可支撑个人关联，但建议改为「Mijksenaar 设计事务所（1990s 改造）」更贴原文；③ 「待核实」文本是「分期记载」的说明性披露而非真正未决项，语义上更像清单注记而非待核实问题——如接受 1990s 单源来自强权威研究机构且主体四要素双源，可评估清零；④ 9 个新登记源中本条 3 个 `link_ok=null` 已如实标。
- **内容判定：待核实（正确的待核实管理）**。`needs_verification=true` ↔ pending ↔ 正文「待核实」三者一致且披露诚实；无治理缺陷。

### 3.2 accessibility-design（无障碍设计，第57轮改动）——**合格**

- 条目现状（实读 `entries/batch-36.json` 340–369 行）：`definition`＝「无障碍设计指使不同行动能力者都能安全、便利地使用环境的设计。」；`time_or_place`＝「20世纪、全球（参见来源）。」；`overview`＝「它以坡道、扶手、标识与尺度保障平等使用。」；`实例`＝「名称：史密森尼国家自然历史博物馆无障碍坡道；地点：美国华盛顿国家广场；设计者：史密森尼学会（实施）、美国无障碍委员会（表彰）；年份：2021 年。新增坡道改善入口可达性。……」
- **definition / time / overview 支撑**：`wp-universal-design` 本轮 HTTP 200 正文 `accessible to all people, regardless of age, disability, or other factors` 直证「不同行动能力者都能使用环境」；`wp-exit-sign` 作疏散标识背景（与本条核心关联弱）。`overview` 的「坡道、扶手、标识与尺度」由 Access Board `new sloped walkways`、`bronze handrails`、`eight feet wide` 及 Smithsonian `eight-foot-wide design`、`bronze handrail` 直证。非编造。
- **实例双源直证（扎实·本轮清零有据）**：
  - **名称**：Access Board `new sloped walkways` at Smithsonian NMNH + Smithsonian `two elevated walkways` → 双源 ✓。
  - **地点**：「美国华盛顿国家广场」由两源 `National Mall side` + Smithsonian `111-year-old building`/NMNH 语境直证 ✓（National Mall 位于华盛顿为通识地理）。
  - **责任方**：两源一致——Access Board 标题 `U.S. Access Board Commends...`、正文 `On behalf of the U.S. Access Board, Training Coordinator Bill Botten attended the ceremony`；Smithsonian `members of the museum's leadership and the U.S. Access Board gathered to unveil the two symmetrical walkways`。条目以「史密森尼学会（实施）、美国无障碍委员会（表彰）」写机构责任方，**未编造个人建筑师**（来源确无单一署名建筑师），口径诚实 ✓。
  - **年份**：Access Board `On December 15, 2021` + Smithsonian `In 2021, the museum completed the installation` → 双源直证 ✓。
  - 两源为不同机构（联邦 Access Board + 史密森学会官方刊物），四要素双源互证；底稿 §2.3 的「sloped/elevated walkways 指同一改造、作者写机构责任方」诚实标注已落地。
- **七节其他内容**：`原理`「消除高差、连续扶手与清晰指引」由两源坡道/扶手/landings 直证；`典型手法与适用条件`「无障碍坡道、扶手、触觉标识、通行宽度」与 Access Board `eight feet wide... two-way pedestrian traffic` 相容。
- **无编造**：核心定义、overview、实例四要素均由引用来源正文支撑；不复制图像。
- **问题（轻微）**：① `definition` 主要靠 `wp-universal-design`（通用设计）支撑，「无障碍设计」与「通用设计」概念相邻但非完全同一，属可接受的概念背景，建议注明；② `wp-exit-sign` 与本条核心关联弱，建议注明为背景或替换；③ `period=20世纪` 而具名实例为 2021 年（概念起源于 20 世纪即可，不与实例年份矛盾）；④ 2 个新登记源 `link_ok=null` 已标。
- **内容判定：合格**。`needs_verification=false`、pending 空、待核实「暂无已知待核实项。」与双源实况一致；本轮 true→false 清零有据，非硬写。

### 3.3 acoustic-environment（声环境，第57轮改动）——**待核实**

- 条目现状（实读 `entries/batch-38.json` 734–764 行）：`definition`＝「声环境指空间中的声音条件，包括隔声、吸声与混响。」；`time_or_place`＝「20世纪、全球（参见来源）。」；`overview`＝「混响过长、隔声不足或噪声干扰都会削弱听闻清晰度与舒适。」；`实例`＝「名称：柏林爱乐大厅（Philharmonie Berlin）；地点：德国柏林；设计者：汉斯·沙隆（Hans Scharoun，建筑）、洛塔尔·克雷默（Lothar Cremer，声学）；年份：1963 年。葡萄园式座席与顶部声学反射板，混响时间约 2 秒。……」
- **definition / overview 支撑（扎实·双概念源）**：`designingbuildings-acoustics` 本轮 HTTP 200 正文 `the minimisation of noise transmission from one space to another and the control of the characteristics of sound within spaces themselves` + Reverberation time / Sound absorption / Sound insulation 三节直证「隔声、吸声与混响」；`libretexts-room-acoustics` `reverberation time`、`sound absorption`、`reflect... eliminate these reflections` 互证。`overview`「混响过长、隔声不足或噪声干扰削弱清晰度舒适」由 `A high reverberation time can make a room sound muffled, loud and noisy`、`intelligibility`、`noise nuisance... negative effects on health, wellbeing and general quality of life` 直证。非编造。
- **实例四要素（身份双源，声学细节单机构·已如实披露）**：
  - **名称/地点**：Berliner Philharmoniker 主页 `The Philharmonie Berlin has been the musical heart of Berlin since 1963` + AJ `Scharoun's Berlin Philharmonie`、`German capital's leading orchestra` → 双源 ✓。
  - **设计者 Scharoun（建筑）**：BPH 主页 `the architect Hans Scharoun ... developed the main concert hall` + AJ `Scharoun's masterpiece` → 双源 ✓。
  - **设计者 Cremer（声学）/年份 1963/声学参数**：Cremer 仅 BPH 声学专页 `Hans Scharoun had already enlisted the services of Lothar Cremer. An expert on acoustics... head of the Institute for Technical Acoustics`；1963 仅 BPH 主页 `since 1963`（AJ 为 2018 火灾新闻，无 1963）；「葡萄园式座席与顶部声学反射板、混响约 2 秒」仅 BPH 声学页 `vineyard terraces`、`ten "clouds" ... suspended`、`reverberation time of two seconds`。BPH 主页与声学页为同一机构，合并计 1 源 → 上述均为**单机构直证**。
  - 条目 `needs_verification=true`、`pending_notes` 与正文「待核实」同为「声学参数仅柏林爱乐官方单机构直证（两个页面合并计一源），AJ 仅作身份佐证。」→ 单机构事实与 AJ 角色已如实披露，与底稿 §2.2「声学数据只归源①，源②仅身份佐证」一致，不构成隐瞒。
- **七节其他内容**：`原理`「硬表面反射形成混响、吸声缩短混响、隔声阻断传播」由两概念源直证；`典型手法与适用条件`「隔声墙体/楼板、吸声材料、按用途设定混响时间」与 Designing Buildings 三节相容。
- **无编造**：核心定义、overview、实例身份要素均由引用来源正文支撑；声学参数不凑第二源而如实标单机构；不复制图像。
- **问题**：
  - ① **（判待核实主因·已如实披露）** Cremer、1963、声学参数仅 BPH 官方单机构直证；AJ 仅身份佐证。如需升级为合格，须补一独立机构来源直证声学顾问/混响目标/落成年份。
  - ② **（SVG 缺陷·重要·非本轮引入）**：本条 SVG 有元素越出 `viewBox='0 0 760 400'`——`<ellipse cx=263 cy=161 rx=103 ry=361>` 实际 y 范围 [-200, 522]、`<rect x=604 y=248 width=34 height=312>` 实际 y 至 560，均超出 0–400 会被裁剪，违反 TASK_design「SVG 元素限制在 viewBox 内」。本轮 `git diff` 显示该 SVG **未改动**（svg 行变更数 0），属存量缺陷；`check.py` 的 `validate_svg` 不校验 `rx/ry`、也不校验 `x+width`/`y+height` 的包容性，故 PASS 掩盖了此缺陷。建议修复图形并增强 check.py 几何校验。
  - ③ 4 个来源 `link_ok=null` 已如实标；AJ 的 `web_fetch` 403 但 urllib 200，按反爬/连接异常处理、非死链。
- **内容判定：待核实（正确的待核实管理）**。`needs_verification=true` ↔ pending ↔ 正文「待核实」三者一致且披露诚实；内容层面无治理缺陷，SVG 缺陷为机械项存量问题（修复建议见第九节）。

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：12 个来源 id 全部存在、`verified=true`、`year=null`（D06 允许）；3 个 Wikipedia 源 `link_ok=true`，9 个新登记/沿用源 `link_ok=null`（三态未标），无 `link_ok=false`。无假 id。
- **可达性（本轮实抓）**：12/12 URL 本轮取得正文。9 个 `web_fetch` 直读 200；Smithsonian 经最终域名 200；`architectsjournal`、`wp-wayfinding`、`wp-universal-design` 经 `urllib` 200；`libretexts` 两通道均 200。`link_ok=null` 未标 true 属三态保守，不影响证据效力。
- **相关性结论**：
  - `wayfinding`：两概念源支撑定义/overview；Rijksmuseum + Crouwel 直证史基浦实例（1967 阶段双源、1990s 阶段单源）。
  - `accessibility-design`：`wp-universal-design` 支撑核心定义，`wp-exit-sign` 为背景；Access Board + Smithsonian 双源直证 NMNH 2021 坡道四要素。
  - `acoustic-environment`：两概念源支撑定义/overview；BPH + AJ 双源直证实例身份，声学参数/年份/Cremer 仅 BPH 单机构（已披露）。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | viewBox | 含「示意图，非施工图」 | on* 事件 / 外链图 | 规范句收尾 | validate_svg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wayfinding | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE |
| accessibility-design | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE |
| acoustic-environment | L2 | ✓ | 6/6 | 1 | `0 0 760 400` | ✓ | 无 / 无 | ✓ | NONE（但有越界几何，见 3.3②） |

> 七节完整（定义 + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实，无缺节无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、含「示意图，非施工图」、无 `on*`、无 `<image>`/外链；「常见错误与限制」均以「实际工程须按当地规范和专业设计人员的要求」收尾；`check.py` PASS。**机械项三条形式层面全部通过**；acoustic-environment 的 SVG 存在实际越界几何（存量、check.py 盲区）。
>
> `git diff` 确认三条 SVG **均未在 round57 改动**（变更行数 0），本轮仅改 `sections.实例`、`sources`、`needs_verification`、`pending_notes`、`sections.待核实`。
>
> **SVG 质量观察**：wayfinding（路径—节点—指示牌）与 accessibility-design（坡道—连续扶手）主题贴合；acoustic-environment 图形冗杂且越界。延续第44–56轮观察——三条均缺显式「设计意图/尺寸关系」文字标注，`check.py` 查不出该语义项，属系统性次要问题。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实

- 三条 `title/tier/theme/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对全部 OK，无 MISMATCH）；`source_count` 与来源数组长度一致（4=4、4=4、4=4）。`needs_verification_count`：wayfinding=1、accessibility=0、acoustic=1，与条目 `needs_verification` 逐条对应。
- `git diff coverage.json` 显示本轮 6 条补实例条目 `source_count` 2→4，其中 `accessibility-design` 的 `needs_verification_count` 1→0（唯一清零）。`pending_sum` 第56轮 194 → 本轮 **193**（-1），净变化与该条清零一致。存量待核实占比 193/258≈74.8%，处历史高位。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 联动一致性 |
| --- | --- | --- | --- | --- |
| wayfinding | true（保持） | 「同一导视系统的不同阶段由两源分别记载，作者与年份分期列出。」 | 同 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：1990s 单源分期事实已披露，保持待核实正确（注记文本语义偏说明性，见 3.1 问题③）。 |
| accessibility-design | **false（本轮清零）** | "" | 「暂无已知待核实项。」 | **结构一致 ✓、内容恰当 ✓**：四要素双源直证，清零恰当。 |
| acoustic-environment | true（保持） | 「声学参数仅柏林爱乐官方单机构直证（两个页面合并计一源），AJ 仅作身份佐证。」 | 同 pending 逐字一致 | **结构一致 ✓、内容恰当 ✓**：单机构事实与 AJ 角色如实披露，保持待核实正确。 |

> **异常监控（§E）**：全库 `pending_sum` 由第56轮 194 降至本轮 **193**（-1，0.52%）。存量待核实占比 193/258≈74.8%，处历史高位，**不触发「待核实占比异常低（疑似硬写）」降级**；本轮唯一清零 `accessibility-design` 经抽检确认四要素双源扎实，属有据清零，非硬写。

## 七、任务 5：相似度（difflib 去空白+小写，阈值 0.54；全库 258 条；口径②=全字段-不含 SVG）

### 7.1 对既有库（排除自身）逐条扫描

| 条目 | ①短文本 max（vs 全库除自身） | 判 | ②全字段 max（vs 全库除自身） | 判 |
| --- | --- | --- | --- | --- |
| wayfinding | **0.3704** vs interior-exterior-transition | <0.54 ✓ | **0.3291** vs circulation | <0.54 ✓ |
| accessibility-design | **0.4671** vs sunken-accessibility | <0.54 ✓ | **0.3961** vs sunken-accessibility | <0.54 ✓ |
| acoustic-environment | **0.3529** vs environmental-psychology | <0.54 ✓ | **0.3550** vs minimalism-architecture | <0.54 ✓ |

> 三条两档均 **<0.54**，未越线。最高为 accessibility-design 短文本 0.4671（vs sunken-accessibility，两条同含「无障碍」定义句式与「保障平等使用」措辞，属正常近邻；全字段仅 0.3961，内容分化明显）。

### 7.2 第57轮批内 3 条两两（全字段② / 短文本①）

- wayfinding vs accessibility-design：全字段 **0.2583**、短文本 0.2517。
- wayfinding vs acoustic-environment：全字段 **0.2530**、短文本 0.2535。
- accessibility-design vs acoustic-environment：全字段 **0.2887**、短文本 0.3066。
- → 批内两两均远低于 0.54，无套话/模板姊妹风险。

### 7.3 方法自校

- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–56轮报告逐位一致，口径正确。

> **文本相似度判定：三条对全库与批内均 PASS（<0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **wayfinding（导视与寻路）** | definition/overview 由两概念源直证；实例主体四要素双源（1967 Wissing），1990s Mijksenaar 阶段单源且已披露；无编造 | 4/4 true；12/12 本轮可达；实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界 | 全部一致；nv=true↔pending↔「待核实」披露诚实 | 全库 ✓（0.3704/0.3291）；批内 ✓ | **待核实** |
| **accessibility-design（无障碍设计）** | definition/overview 由 wp-universal-design 直证；NMNH 坡道四要素由 Access Board + Smithsonian 双源直证；无编造 | 4/4 true；实例源本轮 200 且直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、无越界 | 全部一致；nv=false 清零恰当 | 全库 ✓（0.4671/0.3961）；批内 ✓ | **合格** |
| **acoustic-environment（声环境）** | definition/overview 由两概念源直证；实例身份（名称/地点/Scharoun）双源，Cremer/1963/声学参数仅 BPH 单机构且已披露；无编造 | 4/4 true；AJ 经 urllib 200；实例源直接相关 | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」，但**元素越出 viewBox（存量缺陷）** | 元数据一致；nv=true 方向正确、披露诚实 | 全库 ✓（0.3529/0.3550）；批内 ✓ | **待核实** |

### 问题清单

- **① wayfinding 1990s 阶段单源（判待核实主因·已如实披露）**：Mijksenaar、1990 年代、「最早整合象形符号」仅 Crouwel 一源直证，Rijksmuseum 藏品止于 1967。已标 `needs_verification=true` 且披露分期，属「正确的待核实管理」，无治理缺陷；如需升级为合格，须补一独立机构来源直证 1990s 改造。
- **② wayfinding「Paul Mijksenaar」个人化措辞（轻微）**：来源写「design studio Mijksenaar」，建议改为「Mijksenaar 设计事务所（1990s 改造）」更贴原文（Crouwel 参考文献列 Paul Mijksenaar 作个人关联，非硬伤）。
- **③ wayfinding「待核实」文本语义（轻微）**：现为「分期记载」说明而非真正未决项；可在接受 1990s 单源来自强权威研究机构的前提下评估清零，或改写为明确点出单源项。
- **④ acoustic-environment 声学参数单机构（判待核实主因·已如实披露）**：Cremer、1963、混响 2 秒、葡萄园式反射板仅 BPH 官方单机构（主页+声学页合并计一源）直证，AJ 仅身份佐证。已披露，属「正确的待核实管理」；升级需补独立机构声学来源。
- **⑤ acoustic-environment SVG 越界（重要·存量·非本轮引入）**：`ellipse ry=361`（y 至 522）、`rect y=248 height=312`（y 至 560）越出 viewBox 0–400，会被裁剪；`check.py` 不校验 `rx/ry` 与 `x+width`/`y+height` 包容性，PASS 掩盖缺陷。建议修复图形并增强 check.py 几何校验。
- **⑥ 概念源弱相关（轻微）**：`wp-exit-sign`（accessibility）、`wp-universal-design` 与「无障碍设计」的边界、`libretexts`/`designingbuildings-acoustics` 的定位，建议注明为概念背景或替换更直接来源。
- **⑦ accessibility-design period 与实例年份（轻微）**：`period=20世纪` 而实例为 2021 年；概念起源于 20 世纪即可，不构成矛盾。
- **⑧ 全站系统性次要项**：三条 SVG 均缺显式「设计意图/尺寸关系」标注，`check.py` 查不出该语义项，建议全站统一补强（延续第44–56轮方向）。
- **⑨ 三态与可达性（轻微）**：9 个来源 `link_ok=null` 已标；AJ `web_fetch` 403 / Wikipedia `web_fetch` 失败均经 urllib 200，按连接异常处理、非死链。

## 九、总体结论与建议

- **抽样结果**：第57轮补具名实例条目中定点抽检 3 条——`wayfinding`、`accessibility-design`、`acoustic-environment`。**内容维度：1 合格（accessibility-design）＋2 待核实（wayfinding、acoustic-environment）＋0 不合格；实例层面 0 编造、0 假 id、0 死链证据。**
- **来源层面**：12 个引用来源 id 全部存在、`verified=true`、本轮全部取得正文（AJ / 两 Wikipedia 经 urllib）。`accessibility-design` 的实例四要素双源扎实；`wayfinding` 实例主体双源、1990s 阶段单源（已披露）；`acoustic-environment` 实例身份双源、声学参数/年份/Cremer 单机构（已披露）。
- **结构/治理层面**：七节/规范提示机械项三条全过、SVG 唯一性与 theme 贴合通过（acoustic SVG 存量越界另列）、元数据逐项一致、`check.py` PASS 0 errors。**pending 联动**：三条结构一致；`accessibility-design` 清零恰当；`wayfinding`、`acoustic-environment` 保持 true 且披露诚实。全库 pending_sum 194→193（-1），存量占比 74.8% 处高位，不触发「占比异常低」降级。
- **相似度层面**：三条对全库与批内均 <0.54（短文本最高 0.4671、全字段最高 0.3961）；方法自校 0.5157 与第39–56轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——0 不合格（1 合格 + 2 待核实），0 实例编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级」路径：不成立**——三条对全库与批内均 <0.54。
  3. **§E「待核实占比异常低（疑似硬写）→整批降级」路径：不成立**——存量待核实占比 74.8% 处高位，本轮唯一清零有双源直证支撑，非整批硬写。
  4. **结论：本轮 1 条合格、2 条待核实，不触发整批返工/降级。** 两条待核实均为「来源深度/披露缺陷」而非编造，且 `needs_verification` 联动方向正确、披露诚实。
- **返工/修复建议（定向、非整批）**：
  1. **（问题⑤，优先）`acoustic-environment` SVG**：修正 `ellipse rx/ry`、`rect height` 越界，使全部元素落在 viewBox 0–400 内；同时在 `tools/check.py::validate_svg` 增加 `rx/ry` 与 `x+width`/`y+height` 包容性校验，消除「PASS 掩盖越界」盲点。
  2. **（问题④）`acoustic-environment`**：保持待核实；补一独立机构来源直证 Cremer / 1963 / 混响目标以升级为合格，否则维持现状（当前披露已诚实，无需回滚）。
  3. **（问题①②③）`wayfinding`**：保持待核实或补 1990s 改造的第二独立源后升级；建议把「保罗·迈克萨纳」改为「Mijksenaar 设计事务所（1990s 改造）」；把「待核实」注记改写为明确点出单源项，或评估清零。
  4. **（问题⑥⑦）概念源与字段**：把 `wp-exit-sign`、通用设计/声学概念源注明为背景或替换；无须因 period 与实例年份差异改动。
  5. **（问题⑧，系统性）**：全站统一补「设计意图或尺寸关系」SVG 标注。

### 机器可读汇总

```
ROUND=57
SAMPLER=spotcheck-r57
MODE=第57轮补具名实例条目中lead定点抽3条（wayfinding / accessibility-design / acoustic-environment）
SCOPE=["wayfinding","accessibility-design","acoustic-environment"]
FILES={"wayfinding":"entries/batch-07.json","accessibility-design":"entries/batch-36.json","acoustic-environment":"entries/batch-38.json"}
GIT_HEAD="04931db chore: round56 theory named instances"; ROUND57_COMMITTED=false; GIT_STATUS="round57 changes UNCOMMITTED as found (M coverage/data/sources/entries/batch-06/07/36/37/38 + site/*; ?? review-round57a.md, review-round57b.md, apply_review_round57.py - lead notes, untouched)"
STATE={"sources.json":"458 sources, verified_true=455, verified_false=3, link_ok_false=6","coverage.json":"total=258","batch-07.json":"16077B","batch-36.json":"25729B","batch-38.json":"64915B","pending_sum":193}
CHECK_PY="PASS: all checks, 0 errors (EXIT=0); no file-write statements; validate_svg on 3 svgs = NONE (but acoustic SVG has unreported out-of-viewBox geometry)"
SAMPLE_RATIO="3/6 (50%, lead 定点抽检; 6 landed named-instance entries per apply_review_round57.py)"
FETCH_METHOD="web_fetch 200 for Rijksmuseum(redirect)/Crouwel/AccessBoard/BPH-main/BPH-acoustic/DB-wayfinding/DB-acoustics/LibreTexts; Smithsonian final smithsonianmag.com 200; urllib 200 for AJ(web_fetch 403),wp-wayfinding,wp-universal-design; quote readback via de-tag+unescape+fold; in-memory; only this report written"
SOURCES={"count_distinct_ids":12,"count_refs":12,"all_exist":true,"all_verified_true":true,"link_ok_false":0,"link_ok_true_wikipedia":3,"link_ok_null":9}
BODY_SUPPORT={
 "wayfinding":"definition/overview two concept sources (wp-wayfinding 'signage, maps and other cues to help people reach destinations'; DB 'method for relaying messages... navigate'); instance Schiphol name+1967 Wissing dual (Rijksmuseum 'Benno Wissing, 1967' + Crouwel 'In 1967, the designer Benno Wissing'); 1990s Mijksenaar + pictogram-first single (Crouwel only); VERDICT=待核实 (1990s phase single-source honestly disclosed, nv=true proper); minor: personal 'Paul Mijksenaar' vs source 'design studio Mijksenaar'",
 "accessibility-design":"definition wp-universal-design('accessible to all people regardless of age/disability'); NMNH 2021 sloped walkways four facts dual (Access Board 'On December 15, 2021... new sloped walkways... National Mall side' + Smithsonian 'In 2021... two elevated walkways' + 'Access Board gathered to unveil'); institutional responsibility not fabricated architect; VERDICT=合格 (dual-source, nv cleared true->0 evidenced)",
 "acoustic-environment":"definition/overview two concept sources (DB Building acoustics + LibreTexts); instance name/place/Scharoun dual (BPH main 'since 1963'/'architect Hans Scharoun' + AJ 'Scharoun's masterpiece'); Cremer/1963/reverb-2s/vineyard single-institution BPH acoustic+main merged (AJ identity only); VERDICT=待核实 (single-institution acoustic facts honestly disclosed, nv=true proper); SVG out-of-viewBox geometry (ellipse ry=361 y[-200,522], rect y248+h312->560) pre-existing, check.py blind spot"}
L2_CHECK={"seven_sections":"definition+6/6 x3","svg_count":"1 each","svg_phrase":"示意图，非施工图 x3","viewBox":"0 0 760 400 x3; 无on*/无外链图","risk_note":"实际工程须按当地规范和专业设计人员的要求 x3","svg_changed_this_round":0,"svg_issue":"acoustic SVG elements exceed viewBox (pre-existing, check.py misses rx/ry and x+w/y+h); no design-intent/dimension annotation site-wide (systemic minor)"}
METADATA={"field_match_coverage":"ALL OK x3","source_count":"4=4 x3","nvc":"wayfinding=1, accessibility=0, acoustic=1; coverage diff: 6 entries source_count 2->4, accessibility nvc 1->0; pending_sum 194->193 (-1, 0.52%), stock ratio 193/258=74.8% (high, not anomalous-low)","needs_verification":"wayfinding=true proper; accessibility=false proper evidenced clear; acoustic=true proper"}
SIMILARITY={
 "wayfinding":{"vs_all_short":0.3704,"short_entry":"interior-exterior-transition","vs_all_full":0.3291,"full_entry":"circulation","verdict":"PASS<0.54"},
 "accessibility-design":{"vs_all_short":0.4671,"short_entry":"sunken-accessibility","vs_all_full":0.3961,"full_entry":"sunken-accessibility","verdict":"PASS<0.54"},
 "acoustic-environment":{"vs_all_short":0.3529,"short_entry":"environmental-psychology","vs_all_full":0.3550,"full_entry":"minimalism-architecture","verdict":"PASS<0.54"},
 "intrabatch_full_max":0.2887,"intrabatch_full_max_pair":"accessibility-design vs acoustic-environment",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-56 -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"wayfinding":"待核实","accessibility-design":"合格","acoustic-environment":"待核实"}
VERDICT_PENDING={"wayfinding":"proper (nv=true, 1990s single-source disclosed; note text is descriptive)","accessibility-design":"proper (dual-source, nv=false cleared)","acoustic-environment":"proper (nv=true, single-institution acoustic facts disclosed)"}
HARD_FABRICATION_INSTANCE=0
UNSOURCED_CLAIM=0
FAKE_ID=0
LINK_FAIL=0
SVG_OUT_OF_VIEWBOX=1
ANOMALY_NVC="pending_sum 194->193 (-1, 0.52%); stock ratio 74.8% high -> no anomalous-low downgrade; 1 evidenced clear"
BATCH_ACTION="No rollback/downgrade: 0 不合格 (1合格+2待核实), 0 instance fabrication/0 fake id/0 dead link; similarity all <0.54; pending stock high. Targeted fixes: (1) fix acoustic SVG out-of-viewBox geometry + strengthen check.py geometric validation; (2) acoustic keep 待核实 or add independent acoustic source; (3) wayfinding reword 'Paul Mijksenaar' to design studio, mark single-source 1990s phase explicitly or consider clearing; (4) mark weak concept sources as background."
READONLY="only wrote research/spotcheck-round57.md; no other project content file changed; no git commit; round57 work remains uncommitted as found; web content treated as data, no instruction executed; in-memory fetch, no files written outside deliverable"
```

*（报告完）*
