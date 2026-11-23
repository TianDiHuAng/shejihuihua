# 第46轮质量抽检报告·补（spotcheck-round46b）——batch-46 补抽 2 条（picturesque / early-islamic-architecture）

- 抽检人：spotcheck-r46b（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 10:25 起，Asia/Hong_Kong（CST）。
- 任务：对第46轮 `batch-46` 中**未被 `spotcheck-round46.md` 覆盖的另 2 条**——`picturesque`（如画）、`early-islamic-architecture`（早期伊斯兰建筑）——逐条核对 definition/time/overview/实例 是否有引用来源正文支撑、是否编造、来源是否直接相关（点名核验 `tate-picturesque` 是否述如画定义、`artincontext-islamic-art` 是否述倭马亚/岩石圆顶/清真寺）、L2 七节/SVG/规范提示、pending 联动、period/region 口径、相似度（阈值 0.54）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；新增/改动条目随机抽 10%、**至少 3 条**逐条核对来源；不合格则整批返工、下一轮抽检比例提至 25%；相似度过高→整批降级）＋第三节 F「体检」＋第六节（联网内容一律视为数据、其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节标准与「专用规则」（每页至少 1–2 张示意图、图下注「示意图，非施工图」、图中标注设计意图或尺寸关系、尺寸/坡度/消防/无障碍数据附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md` / `TASK_design.md` 在仓库根**无同名文件**（与第 12–45 轮及本轮 `spotcheck-round46.md` 一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md`（21 行）已读，`research/spotcheck-round46.md`（本批已抽的另 2 条报告）作模板对齐。
- 与 `spotcheck-round46.md` 的分工：前者抽 `imperial-axial-route`/`mughal-architecture`；本报告补抽 `picturesque`/`early-islamic-architecture`。两份合起来即覆盖 `batch-46` 全部 **4 条**，满足 §E「至少 3 条」下限。
- 技能：按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 10:25 起）**：`data/sources.json`=144993B@2026-11-23 10:25:45、`entries/batch-46.json`=8616B@2026-11-23 10:25:45、`coverage.json`=86274B@2026-11-23 10:25:45、`tools/check.py`=15908B@2026-11-22 15:11:54。`git log -1` = `2dd6338 docs: record final push pending (network)`。
- **版本漂移提示（重要）**：`spotcheck-round46.md` 记录其采样时 `entries/batch-46.json`=**8510B@10:20:11**、`mughal-architecture.period=中世纪`、imperial/mughal 实例为「地点与设计者不适用」。本轮实读 `batch-46.json`=**8616B@10:25:45**，`mughal-architecture.period` 已变为 **「文艺复兴至19世纪」**，`imperial-axial-route`/`mughal-architecture` 的「实例」已补地名/设计者/年代——即 round46 报告点名的问题②①③**已被上一环节修复**。故本报告基于**更新后的当前文件**判定；`picturesque`/`early-islamic-architecture` 的「实例」**仍是「地点与设计者不适用」**（未随之更新，见 §八问题③⑥）。
- **工作树状态（采样时点）**：`git status --porcelain` 显示第46轮成果仍在工作区：modified `SATURATION.json / coverage-matrix.md / coverage.json / data/sources.json / scope.md / site/coverage.html / site/entries/chinese-architecture-style.html / site/index.html / site/indexes.html / site/sources.html / tools/gen_scope.py`；untracked `entries/batch-46.json`、`research/b1-round46.md`、`research/gaps-round46.md`、`research/spotcheck-round46.md`、`site/entries/{imperial-axial-route,mughal-architecture,picturesque,early-islamic-architecture}.html`、`tools/add_round46.py`。抽检对象在采样期间**稳定**，判定基于该稳定快照。本报告产出后追加 `?? research/spotcheck-round46b.md`（本报告，唯一由本次抽检写入的文件）。
- **条目规模（`coverage.json` 实读）**：`total=255`、全部 `level=L2`、全部 `status=已写`；`pending_total`（`needs_verification_count` 求和）＝**223**；来源库 `sources.json` 共 **308** 条，`verified=true` **305**、`verified=false` **3**（`link_ok`：true 145、false 6、null 157）。注：`link_ok=false` 的 6 条**均不在本次 4 个来源中**（本轮 4 源 `link_ok` 全为 null），不影响判定。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round46b.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python urllib 读取→内存去标签/切句/计数），未在项目内外落盘任何持久文件。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；「常见错误与限制」段须含「实际工程须按当地规范和专业设计人员的要求」；SVG 元素不出 `viewBox`（两条均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），timeout 30–40s，SSL 校验关闭，失败重试 5–6 次。`en.wikipedia.org` 按 D05 改走 **owiki 同源镜像** `https://owiki.org/wiki/<Title>`；`tate.org.uk`、`artincontext.org` 直连。本轮 **4 个引用来源全部实抓 HTTP 200**（`<title>`/正文与 `sources.json` 逐条核对，见 §二、§三、§四）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **255 条**去重已写条目逐条扫描，警戒线 **0.54**（与第 27–46 轮一致）。**方法自校**：以全字段②计算已知最高对 `futurism-style vs expressionism-style`，得 **0.5157**，与第 39–45 轮及本轮 spotcheck-round46 报告**逐位一致**，确认口径正确。
- **“两源互证”判定口径**（沿用第42轮明确化口径）：按「关键事实至少两个独立来源互相印证，否则标待核实」；两个引用来源须对本条**具体概念**有实质覆盖且互证；若第二源对本条**具体概念**（如早期伊斯兰清真寺形制/方形平面/柱廊）**零覆盖或仅复述通用定义/泛论**，则相关具体论断实为**单源**，据硬性规则影响判定。
- **三级判定定义（可复现）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（概念定义或实例）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但存在第二源对本条具体概念仅泛论/零覆盖、或某关键事实实质单源、或「原理」＝定义+概述逐字拼接等——属来源支撑/深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或关键结构项（如「一图」）实质不满足 TASK_design 强制要求。
- **相似度专项（独立维度）**：警戒线 0.54；超线即触发 `AUTONOMOUS.md §E`「相似度过高（疑似套话）→整批降级为草稿并复查」，与「不合格（内容无源）→整批返工」是**不同触发路径**，分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **4 个去重来源 id（4 处引用：picturesque 2、early-islamic 2）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）**、实抓 HTTP 200。

| 条目 | 来源 id | 存在/verified | 实抓标题（本轮 HTTP，逐字） | 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| picturesque | `wp-picturesque` | ✅ / true | `Picturesque ::: Open WIKI`（200，32137B，textlen≈18933） | Wikipedia（经 owiki 镜像核验） | 权威百科 | null | **相关（直接、强）**：`Picturesque is an aesthetic ideal introduced into English cultural debate in 1782 by William Gilpin…`；`"the term 'picturesque' needs to be understood in relationship to…the beautiful and the sublime"`；`Picturesque arose as a mediator between these opposed ideals of beauty and the sublime`；Hussey：`the characteristics of the picturesque were 'roughness and sudden variation joined to irregularity of form, colour, lighting, and even sound'`；`This new image disregarded the principles of symmetry and perfect proportions while focusing more on 'accidental irregularity'`；`The irregular, anti-classical ruins became sought-after sights.` |
| picturesque | `tate-picturesque` | ✅ / true | `Picturesque \| Tate`（200，77800B，textlen≈2562） | Tate | 官方机构 | null | **相关（直接、强）**：`The word picturesque refers to an ideal type of landscape that has an artistic appeal, in that it is beautiful but also with some elements of wildness`；`At one extreme was the sublime…at the other the beautiful…In between came the picturesque, views seen as being artistic but containing elements of wildness or irregularity.`；`The theory of the picturesque was developed by writers William Gilpin…and Uvedale Price…` |
| early-islamic-architecture | `wp-umayyad-architecture` | ✅ / true | `Umayyad architecture ::: Open WIKI`（200，36984B，textlen≈21129） | Wikipedia（经 owiki 镜像核验） | 权威百科 | null | **相关（直接、强）**：`Umayyad architecture developed in the Umayyad Caliphate between 661 and 750, primarily in its heartlands in historical Syria.`；`The sanctuary of the Dome of the Rock…in Jerusalem, is the oldest surviving major Islamic building.`；`Both had hypostyle designs, with roofs supported by elaborately designed columns.`；`Wasit…included a square Friday mosque with a hypostyle roof.`；`evolved from square prayer enclosures`；`The prayer hall has three aisles parallel to the qibla wall`；`Abd al-Malik ibn Marwan who also built the Dome of Rock`；`the building of the Great Mosque of Damascus`（Al-Walid I） |
| early-islamic-architecture | `artincontext-islamic-art` | ✅ / true | `Islamic Art - A Deep Dive into the Gilded World of Islamic Art`（200，485730B，textlen≈37k） | Art in Context | 学术著作 | null | **相关但极薄/泛论**：`The Umayyad Dynasty ruled from around 661 to 750 CE`；`the shrine in Jerusalem called the Dome of the Rock (c. 7th century CE) and the Al-Aqsa Mosque (completed in 705 CE)`；`Architects also utilized the Byzantine-style dome in building layouts.`；`One such feature is the Sahn, which is the large courtyard…important part of the Mosque's prayer hall`。**但对「倭马亚清真寺形制/方形平面/柱廊(hypostyle)」零覆盖（hypostyle=0、colonnade=0、建筑义 square=0）** |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（picturesque 2=2、early-islamic 2=2）。4 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。**
>
> **来源记录 `title` 字段核对**：`wp-picturesque`（记录 `Picturesque` vs 实际 `Picturesque ::: Open WIKI`，镜像后缀）、`tate-picturesque`（记录 `Picturesque — Tate` vs 实际 `Picturesque | Tate`，破折号/竖线排版差异）、`wp-umayyad-architecture`（记录 `Umayyad architecture` vs `Umayyad architecture ::: Open WIKI`）**均相符**。**唯一元数据瑕疵**：`artincontext-islamic-art` 记录 `title="Islamic Art — Art in Context"`，实际 `<title>`=`Islamic Art - A Deep Dive into the Gilded World of Islamic Art`（机构名 Art in Context 相符，仅副标题未录入）——次要，建议记录全名或备注「Art in Context 站点」。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 picturesque（如画，batch-46）——**内容合格**
- **wp-picturesque**（owiki 200，textlen≈18933）直证：
  - `Picturesque is an aesthetic ideal introduced into English cultural debate in 1782 by William Gilpin…` → 支撑 definition「风景**审美**趣味」+ overview 时代/英国背景。
  - Gilpin：`picturesque [is] "a term expressive of that peculiar kind of beauty, which is agreeable in a picture"` → **直接支撑 definition「入画效果」**（像画一样的美）。
  - `the term "picturesque" needs to be understood in relationship to…the beautiful and the sublime`；`Picturesque arose as a mediator between these opposed ideals of beauty and the sublime` → **直接支撑 overview「介于优美与崇高之间」**（逐字对应 mediator between beauty and the sublime）。
  - Hussey：`roughness and sudden variation joined to irregularity of form…`；`disregarded the principles of symmetry…focusing more on "accidental irregularity"` → **支撑 definition「不规则、变化」**。
  - `The irregular, anti-classical ruins became sought-after sights.` → **支撑 overview「废墟」**。
  - `Picturesque-hunters tried to "capture" wild scenes`、`designed landscapes should be composed like landscape paintings with a foreground, a middle ground and a background`、`picturesque garden scenes / picturesque style in landscape gardening…create foregrounds, middlegrounds, and backgrounds` → **支撑「野趣」「入画构图」「如画式风景园林」实例类型**。
- **tate-picturesque**（200，textlen≈2562）直证（点名核验项）：
  - `The word picturesque refers to an ideal type of landscape that has an artistic appeal, in that it is beautiful but also with some elements of wildness` → **直接、逐字支撑 definition「风景审美趣味（ideal type of landscape / artistic appeal）」「野趣（wildness）」**，并支撑「入画（artistic appeal）」。
  - `At one extreme was the sublime…at the other the beautiful…In between came the picturesque, views seen as being artistic but containing elements of wildness or irregularity.` → **互证 overview「介于优美与崇高之间」「不规则（irregularity）」**（与 wp 双源直证）。
  - `The theory of the picturesque was developed by writers William Gilpin (Observations on the River Wye 1770) and Uvedale Price…` → 支撑「审美理论」属性。
- **逐项结论**：
  - definition「追求不规则、野趣与入画效果的风景审美趣味」——**双源直证互证**（不规则 ✓wp+✓tate；野趣 wild/wildness ✓wp+✓tate；入画 picture-like/artistic appeal ✓wp+✓tate；风景审美 aesthetic ideal of landscape ✓wp+✓tate）。
  - time_or_place「跨时期、欧洲（参见来源）」——欧洲 ✓（Gilpin/Observations on the River Wye/English cultural debate；Tate 述英国理论）；「跨时期」为美学-conceptual 大桶（本体起于 18 世纪、影响延续），可接受（Minor：本义主要属 18–19 世纪，见 §六）。
  - overview「介于优美与崇高之间，偏爱起伏地形、树木掩映与废墟」——**核心「介于优美与崇高之间」双源直证**（wp mediator + tate in-between）；「废墟」✓wp；**但「起伏地形」「树木掩映」两处为宽松转述**：wp 有「planting trees / grounds / foreground-middleground-background / frame the view」，未见「起伏/undulating terrain」或「树木掩映/screened by trees」的字面（见 §八问题②，Minor）。
  - **原理**「把『像画一样』作为评判风景的标准，以不对称、变化与野趣唤起情感」——picture-like ✓、不对称 ✓（disregarded symmetry）、变化 ✓（sudden variation）、野趣 ✓；**ratio(原理, 定义+概述)=0.1649（低，机制独立）**，非逐字拼接。
  - 实例「如画式风景园林（类型性描述）；地点与设计者不适用」——「如画式风景园林」**类型有源支撑**（picturesque garden scenes / landscape gardening），作为**类型性实例合理、无编造**；`pending_notes` 拟补具名例，诚实（见 §八问题⑥，Minor：pending 偏保守，wp 未给单一具名园林）。
- **两源互证**：definition 与 overview 核心（不规则/野趣/入画、介于优美与崇高之间）由 **wp-picturesque 与 tate-picturesque 双源直证并互证**。
- **专项核验（任务点名）**：**`tate-picturesque` 确真述如画定义**——逐字命中 `The word picturesque refers to an ideal type of landscape that has an artistic appeal…beautiful but also with some elements of wildness` + `In between came the picturesque…wildness or irregularity`。**非张冠李戴、非套用。**
- **内容判定：合格**（definition/overview核心双源直证、机制独立、无编造；次要：overview「起伏地形/树木掩映」为宽松转述、period「跨时期」偏宽、pending 偏保守、SVG 标注见 §五）。**一图 SVG 见 §五；文本相似度见 §七（未越线）。**

### 3.2 early-islamic-architecture（早期伊斯兰建筑，batch-46）——**待核实（第二源对具体形制泛论/零覆盖，方形平面+柱廊实质单源）**
- **wp-umayyad-architecture**（owiki 200，textlen≈21129）直证（主源，强）：
  - `Umayyad architecture developed in the Umayyad Caliphate between 661 and 750, primarily in its heartlands in historical Syria.` → 支撑 definition「倭马亚时期」。
  - `The sanctuary of the Dome of the Rock…in Jerusalem, is the oldest surviving major Islamic building.`；`The most important examples…including the Dome of the Rock, the Great Mosque of Damascus…` → 支撑「圣所/清真寺」「实例=岩石圆顶/倭马亚清真寺」。
  - `Both had hypostyle designs, with roofs supported by elaborately designed columns.`；`Wasit…included a square Friday mosque with a hypostyle roof.`；`evolved from square prayer enclosures` → **直接支撑 definition/overview「方形平面、柱廊（hypostyle/多柱式）」**。
  - `The prayer hall has three aisles parallel to the qibla wall, a common arrangement in Umayyad mosques in Syria.` → **支撑原理「朝向（qibla）」**。
  - `Wooden domes were constructed for Al-Aqsa Mosque and the Dome of the Rock`；`Abd al-Malik…built the Dome of Rock`；`the building of the Great Mosque of Damascus`（Al-Walid I） → 支撑「穹顶」及实例的**地点/主事者**（见 §八问题③）。
- **artincontext-islamic-art**（200，textlen≈37k）直证（第二源，**直接但薄/泛论**；点名核验项）：
  - `The Umayyad Dynasty ruled from around 661 to 750 CE` → **互证「倭马亚时期（661–750）」**（与 wp 双源）。
  - `the shrine in Jerusalem called the Dome of the Rock (c. 7th century CE) and the Al-Aqsa Mosque (completed in 705 CE)` → **互证「岩石圆顶（圣所）」「清真寺」**（点名项命中）。
  - `Architects also utilized the Byzantine-style dome in building layouts.`；`One such feature is the Sahn…important part of the Mosque's prayer hall` → 泛撑「穹顶」「庭院/祈祷厅」。
  - **但对本条具体形制零覆盖**：`hypostyle=0、colonnade=0、建筑义 square=0`（square 仅出现在 Kufic 书法描述）——**无「方形平面」、无「柱廊」、无对倭马亚清真寺形制的实质描述**；且未把「岩石圆顶/清真寺」明确归为倭马亚所建（Umayyad 仅 2 处，均朝代年表语）。
- **逐项结论**：
  - definition「倭马亚时期形成的清真寺与圣所形制：方形平面、柱廊与穹顶」——**「倭马亚时期」「清真寺/圣所」「穹顶」双源可互证**；**但「方形平面」「柱廊」仅 wp-umayyad-architecture 单源**（artincontext 零覆盖），**核心形制的一半实质单源**。
  - overview「以方形礼拜殿与柱廊容纳信众，以穹顶标示神圣中心」——「穹顶」双源；**「方形礼拜殿」「柱廊」仅 wp 单源**；「标示神圣中心」为释义性整合（Dome of the Rock 为圣所）。
  - **原理**「以宽大的柱廊礼拜殿满足集体礼拜，以穹顶与朝向（qibla）确立神圣方位」——柱廊/礼拜殿/qibla/穹顶均有源（柱廊仍主要出 wp）；**ratio(原理, 定义+概述)=0.2708（低，机制独立）**，非逐字拼接。
  - 实例「岩石圆顶与倭马亚清真寺（类型性描述）；地点与设计者不适用」——**岩石圆顶双源、倭马亚清真寺（大马士革大清真寺）出 wp**；**但「地点与设计者不适用」与源相悖**：wp 明载 **地点=耶路撒冷（岩石圆顶）/大马士革（大清真寺）**、**主事者=阿卜杜勒·马利克（岩石圆顶）/瓦利德一世（大马士革大清真寺）**（见 §八问题③，Minor）。
- **两源互证（任务专项）——部分成立**：**「倭马亚时期」「清真寺/圣所」「穹顶」「岩石圆顶」双源互证成立**；**但 definition/overview 的「方形平面」「柱廊（hypostyle）」关键形制仅 wp 单源，`artincontext-islamic-art` 对本条具体形制零覆盖/泛论**。按硬性规则「关键事实至少两个独立来源互相印证」——**方形平面+柱廊属关键事实而实质单源**。
- **专项核验（任务点名）**：**`artincontext-islamic-art` 确述倭马亚/岩石圆顶/清真寺**（逐字命中 Umayyad Dynasty 661–750、Dome of the Rock 圣所、清真寺/祈祷厅），**但仅泛论、未涉倭马亚清真寺形制（方形/柱廊）**——属「直接相关但极薄」，而非零相关。
- **内容判定：待核实**（definition 概念层双源互证、主源 wp 强支撑、无编造；**缺陷＝第二源 `artincontext-islamic-art` 对「方形平面/柱廊」及倭马亚清真寺形制零覆盖，关键形制实质单源**；另：实例「地点/设计者不适用」与源相悖、period 口径见 §六、pending 未披露该缺口——均见 §八）。**⚠ 与第42轮 `proxemics` 同类（第二源直接但极薄、对具体概念零覆盖→待核实，非不合格）。**

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：4 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）；`link_ok` 全为 null（三态未标，非死链、非假源）。**4 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：`wp-picturesque`（owiki 200）/`tate-picturesque`（200）/`wp-umayyad-architecture`（owiki 200）/`artincontext-islamic-art`（200）——**4/4 全部 HTTP 200，无死链**（体检 F 之“死链”对本次 4 源为 0）。
- **相关性**：
  - picturesque 两源（wp 百科 + Tate 官方机构）**均直接主体源、强互证**，点名核验（tate 述如画定义）**正面通过**。
  - early-islamic 的 **wp-umayyad-architecture 直接强源、命中全部形制**；**`artincontext-islamic-art` 直接但极薄**——对本条具体概念（方形平面/柱廊/倭马亚清真寺形制）**零覆盖**，仅泛论朝代年表与岩石圆顶/清真寺。属**第42轮 `designingbuildings-proxemics` 式“直接但极薄/对具体概念零覆盖”缺陷**（本轮为「待核实」，非不合格）。
- **词项覆盖细节**：early-islamic 的「方形」由 wp 直证（`square Friday mosque`/`square prayer enclosures`）、「柱廊」由 wp 直证（`hypostyle…columns`）、「qibla」由 wp 直证（`qibla wall`）；**artincontext 对三者 0 命中**——**单源、非双源互证**。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | 含「示意图，非施工图」 | viewBox | 风险/规范句 | 原理=def+概述拼接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| picturesque | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | 否（ratio 0.1649） |
| early-islamic-architecture | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | 否（ratio 0.2708） |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含「示意图，非施工图」、无 `on*` 事件属性；「常见错误与限制」段均以规范提示收尾（`实际工程须按当地规范和专业设计人员的要求`）；`check.py` 含 SVG 出界检查，本轮 PASS（两图元素坐标全部在 760×400 内）。**机械项两条全部通过。**

### SVG 质量观察（形态贴合主题，但缺「设计意图/尺寸关系」显式标注——次要、系统性）
- **picturesque**：`<path d='M120 320 Q260 150 420 260 T660 180' stroke-width='3'>`（不规则曲线＝地形/路径的曲折）+ `<circle cx=420 cy=260 r=26 fill='accent-soft'>`（点景/掩映元素），**贴合「如画的不规则与掩映、入画构图」主题、非随机占位**；但**图中仅标题 + 「示意图，非施工图」，缺 TASK_design 第6条要求的「设计意图或尺寸关系」文字标注**（次要缺陷）。
- **early-islamic-architecture**：`<rect x=140 y=150 w=480 h=160>`（方形平面/礼拜殿外框）+ `<circle cx=380 cy=150 r=56>`（穹顶）+ `<line x1=180 y1=230 x2=580 y2=230>`（柱廊/中轴），**贴合「方形平面 + 柱廊 + 穹顶」主题、非随机占位**；同样**未标注「方形平面/柱廊/穹顶」等设计意图或尺寸关系**（次要缺陷）。
- **唯一性核验（防模板复刻）**：两条 SVG 字符串在**全库 255 条中各自唯一**（无整串重复）；与 batch-46 另 2 条（imperial/mughal）互为**不同字符串**。
- **判定**：两条「一图」**机械项（1 张 + viewBox + 「示意图，非施工图」 + 不出界 + 无事件属性 + 唯一性）全过**，图形与主题相关；**唯一不足为「缺图中设计意图/尺寸关系标注」**——`check.py` 只查出界与注记，查不出该语义项，属**次要/可提升**，不构成本轮「不合格」。建议全站做一次 SVG 标注补强（与第44/45/46 轮方向一致）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实（含 period/region 分类口径）

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatches=NONE）：picturesque（如画（Picturesque 美学）/理论/重要/跨时期/欧洲/L2）、early-islamic-architecture（早期伊斯兰建筑/风格/重要/古代/伊斯兰·南亚/L2）；`source_count` 与来源数组长度一致（2=2、2=2）；`needs_verification_count`：各 1；`related`：两条均 `[]`（无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| picturesque | true | 「如画（Picturesque 美学）」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（但实例为理论类型，wp 未给单一具名园林，措辞尚可） |
| early-islamic-architecture | true | 「早期伊斯兰建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（**但未披露「第二源对形制零覆盖、方形平面/柱廊单源」的真实缺口**；且源已给岩石圆顶/大马士革大清真寺及地点、主事者，措辞偏保守，见 §八问题③⑤） |

> 结构化标志与两处文本：两条 `pending_notes` 与「待核实」节**逐字一致**（结构联动通过）。**注意（D14 精神）**：`early-islamic-architecture` 的「待核实」仅声明“具体实例待补充”，**对真实存在的来源支撑缺口（`artincontext` 对形制零覆盖、方形平面/柱廊单源）未写入**——属“联动一致但内容不完整/失真”；`picturesque` 的「待核实」对理论类型尚可，但 wp 未给单一具名园林。

### period/region 与分类口径（项目时期桶：古代 / 中世纪 / 文艺复兴至19世纪 / 20世纪 / 当代 / 跨时期）
- **picturesque：period=跨时期、region=欧洲** ——如画为 18 世纪英国/欧洲风景美学，`region=欧洲` ✓（可细化“英国/欧洲”，Minor）；`period=跨时期` 为美学-conceptual 大桶（影响延续多期），**可接受**（Minor：本体主要属 18–19 世纪，按严格桶亦可入“文艺复兴至19世纪”，但作为跨期审美概念用“跨时期”无误）。
- **early-islamic-architecture：period=古代、region=伊斯兰/南亚** ——**存在实质口径问题（本轮最需修，同类 round46 mughal 问题②）**：
  1. 条目 `definition`/`time_or_place` 自述「倭马亚时期」，两源均载 **661–750 CE**（7–8 世纪，属**中世纪早期**）。项目内 **`islamic-architecture`（伊斯兰建筑总条目，含倭马亚）记“中世纪”、`byzantine`（东罗马，同期）记“中世纪”、`gothic`/`romanesque` 记“中世纪”**；**唯独作为伊斯兰建筑早段的 `early-islamic-architecture` 记“古代”**——**与其父条目 `islamic-architecture`（中世纪）及史实时序错位**（更早的 7–8 世纪反而记更古的桶）。
  2. `region=伊斯兰/南亚`：倭马亚核心区在叙利亚/黎凡特（大马士革、耶路撒冷），「伊斯兰」部分成立；「南亚」不适用于本条，但该 region 为合桶标签（同 `islamic-architecture` 亦用此标签），可接受（Minor）。
  - 建议：`period` 由「古代」改 **「中世纪」**（与 `islamic-architecture`、`byzantine` 同桶一致，符合 661–750 为早期中世纪），并同步 `time_or_place`；若项目有意将“伊斯兰/南亚风格”统一另立口径，须在 `DECISIONS.md`/口径说明中**明文记录该惯例**，否则应更正。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 255 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| picturesque | **0.2647** vs trompe-loeil | <0.54 ✓ | **0.4139** vs rockery | <0.54 ✓ |
| early-islamic-architecture | **0.3919** vs islamic-architecture | <0.54 ✓ | **0.4544** vs islamic-architecture | <0.54 ✓ |

> 对**既有 254 条**（排除自身）逐条扫描，两条两档均 **<0.54**（短文本最大 0.3919、全字段最大 0.4544）——**各自与既有库文本区分在阈值内**。
> - picturesque 最近邻：短文本 `trompe-loeil`(0.2647)/`urban-planning-style`(0.2632)/`s-curve-composition`(0.2614)；全字段 `rockery`(0.4139)/`radial-route`(0.4097)/`planting-design`(0.4096)（园林/构图近义，正常语义邻近）。
> - early-islamic 最近邻：`islamic-architecture`(短 0.3919 / 全 0.4544，父条目、正常同域)、`indian-architecture`(短 0.3889 / 全 0.4339)、全字段次高 `eaves-space`(0.4477)（模板性通用短语导致，仍 <0.54）。
> **均未越线。**

### 7.2 batch-46 批内去模板化核验（4 条两两，基于**当前更新后文件**）
| 对 | ①短文本 | ②全字段 |
| --- | --- | --- |
| imperial-axial-route vs picturesque | 0.1564 | 0.2295 |
| imperial-axial-route vs mughal-architecture | 0.1954 | 0.3252 |
| imperial-axial-route vs early-islamic-architecture | 0.1916 | 0.2375 |
| picturesque vs mughal-architecture | 0.1730 | 0.2285 |
| picturesque vs early-islamic-architecture | 0.1461 | **0.3605** |
| mughal-architecture vs early-islamic-architecture | 0.2775 | 0.2496 |

> batch-46 四条**两两均远低于 0.54**（批内全字段最大 **0.3605**，picturesque↔early-islamic；涉及本报告两对的最大值即此）——**无第43轮 batch-42 式双条互为模板姊妹、无套话风险**。（注：本表数值基于更新后文件；与 `spotcheck-round46.md` 旧快照的个别数值差异，源于 `batch-46.json` 8510B→8616B 的版本漂移，非口径错误。）

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–45轮及本轮 spotcheck-round46 报告**逐位一致**，口径正确。

> **文本相似度判定：两条对既有库与批内均 PASS（均 <0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 文本相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **picturesque（如画）** | definition **双源直证互证**（不规则 ✓wp+✓tate、野趣 ✓wp+✓tate、入画/artistic appeal ✓wp+✓tate）；overview **核心双源直证**（介于优美与崇高之间 ✓wp+✓tate、废墟 ✓wp）；验证点 **tate 确述如画定义**；实例为类型性、有源、无编造；原理独立（0.1649）；**Minor：「起伏地形/树木掩映」为宽松转述、period 跨时期偏宽** | 2/2 true；wp+Tate 均直接强源且命中点名概念；**2 源 200 可达** | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、形态贴合（不规则曲线+点景），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 逐字一致 | 既有库 ✓（0.2647/0.4139）；批内 ✓ | **合格**（次要：overview 宽松转述、period 偏宽、SVG 标注） |
| **early-islamic-architecture（早期伊斯兰建筑）** | definition 概念层双源（倭马亚时期 ✓✓、清真寺/圣所 ✓✓、穹顶 ✓✓），**但「方形平面」「柱廊」仅 wp 单源（artincontext 零覆盖）**；overview 同（方形礼拜殿/柱廊单源）；验证点 **artincontext 确述倭马亚/岩石圆顶/清真寺**（但仅泛论、未涉形制）；实例岩石圆顶双源、倭马亚清真寺出 wp（**「地点/设计者不适用」与源相悖，可补耶路撒冷/大马士革·阿卜杜勒·马利克/瓦利德一世**）；原理独立（0.2708）；**period 古代口径问题见 §六/问题①** | 2/2 true；wp 直接强源；**artincontext 直接但极薄、对形制零覆盖**；**2 源 200 可达** | 七节齐、规范句✓；1 SVG 含「示意图，非施工图」、形态贴合（方框+穹顶+柱廊线），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 逐字一致（**未披露形制单源缺口**） | 既有库 ✓（0.3919/0.4544，<0.54）；批内 ✓（max 0.3605） | **待核实**（关键形制实质单源）；**须修：period 古代→中世纪；实例补地点/主事者**；次要：pending/SVG 标注 |

### 问题清单（逐条）
- **① early-islamic-architecture 的 period 口径不符（本轮最需修，同 round46 mughal 问题②）**：`period="古代"` 与自身 `definition="倭马亚时期"`（两源均 661–750 CE，7–8 世纪早期中世纪）及父条目 `islamic-architecture=中世纪`、`byzantine=中世纪` 相悖。→ **建议 `period` 改「中世纪」并同步 `time_or_place`**；若要沿用地区归类惯例须在 `DECISIONS.md` 明文记录。（Minor–Moderate；不影响“待核实”判定，但应修）
- **② picturesque overview 两处宽松转述**：`overview` 写「偏爱**起伏地形、树木掩映**与废墟」，源只直证「wild/irregular/ruins/landscape/garden/planting/foreground-middleground-background」，未见「起伏地形（undulating terrain）」「树木掩映（screened by trees）」字面。→ 建议改为源内实词（不规则、野趣、废墟、入画构图）或据源补证。（Minor）
- **③ early-islamic-architecture 实例要素不全/表述失准**：`实例` 写「地点与设计者不适用」，但 wp 明载**地点=耶路撒冷（岩石圆顶）/大马士革（大清真寺）**、**主事者=阿卜杜勒·马利克/瓦利德一世**。→ 据源补地点与主事者（年份可留待补），并调 pending。（Minor，同 round46 问题①③）
- **④ early-islamic-architecture 关键形制实质单源（判定核心）**：`方形平面`（wp：square Friday mosque / square prayer enclosures）、`柱廊`（wp：hypostyle…columns）仅 `wp-umayyad-architecture` 单源；`artincontext-islamic-art` 对二者及倭马亚清真寺形制**零覆盖**（hypostyle=0、colonnade=0、建筑义 square=0）。→ 按硬性规则「关键事实至少两源互证」，本条目**判“待核实”**；建议补一份真正述及倭马亚清真寺形制（hypostyle/方形平面/柱廊）的第二来源，或将形制描述降为“据 wp 单源”，并在 pending 披露。（核心）
- **⑤ early-islamic-architecture pending 未披露真实缺口**：`pending_notes`/`待核实` 仅称“具体实例待补充”，**未写入“第二源对形制零覆盖、方形平面/柱廊单源”的真实来源缺口**。→ 建议据实补充。（Minor，D14 精神）
- **⑥ picturesque pending 偏保守（轻微）**：理论类条目，「如画式风景园林」为类型性实例合理，wp 未给单一具名园林；pending 称“具体实例待补充”尚可，维持即可（如能补具名如画园林更好）。（Minor）
- **⑦ SVG“设计意图/尺寸关系”标注缺失（两条例、系统性）**：两图机械项与主题贴合均过，但仅标题 + 「示意图，非施工图」，缺 TASK_design 第6条「图中标注设计意图或尺寸关系」。→ 建议全站统一补强（延续第44/45/46 轮）。（Minor、系统性）
- **⑧ 来源元数据瑕疵（轻微）**：`artincontext-islamic-art` 记录 `title="Islamic Art — Art in Context"`，实际 `<title>`=`Islamic Art - A Deep Dive into the Gilded World of Islamic Art`（机构名相符，副标题未录入）→ 建议存全名或备注「Art in Context 站点」。（Minor）

## 九、总体结论与建议

- **抽样结果**：本报告补抽 batch-46 的 **2 条**——`picturesque`、`early-islamic-architecture`（与 `spotcheck-round46.md` 的 `imperial-axial-route`/`mughal-architecture` 合并即覆盖 batch-46 全 4 条，满足 §E「至少 3 条」）。**内容维度：1 合格（picturesque）＋1 待核实（early-islamic-architecture）＋0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：4 个引用来源 id 全部存在、verified=true、**实抓 4/4 HTTP 200 可达**。**两项任务点名核验**：`tate-picturesque` **确述如画定义**（正面通过）；`artincontext-islamic-art` **确述倭马亚/岩石圆顶/清真寺**（域内命中，但**对倭马亚清真寺形制零覆盖、泛论**）。picturesque 双源强互证；early-islamic 主源 wp 强、第二源直接但极薄。唯 1 处 `title` 元数据瑕疵（artincontext 副标题未录入，Minor）。
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 唯一性与形态贴合通过、元数据逐项一致、`needs_verification↔pending↔待核实` **逐字一致**、`check.py` PASS 0 errors、原理均非拼接（0.1649/0.2708）。
- **相似度层面**：两条对既有库与批内均 <0.54（PASS）；批内最大 0.3605，无套话；方法自校 0.5157 与第39–45 轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——无“不合格”内容条目（1 合格 + 1 待核实），无编造/假 id/死链（待核实属来源深度缺陷，非不合格）。
  2. **§E「相似度过高（疑似套话）→整批降级为草稿并复查」路径：不成立**——两条对既有库与批内均 <0.54。
  3. **结论：本轮 2 条不触发整批返工/降级**；`picturesque` 内容合格，`early-islamic-architecture` 判“待核实”（须补第二形制源或据实降级表述）。但存在**须定向修复的口径问题（early-islamic period 古代→中世纪，问题①）**与若干 Minor（形制单源披露、实例要素、overview 转述、pending、SVG 标注、title 元数据）。
- **返工/修复建议（按优先级）**：
  1. **（应做，问题①）**：`early-islamic-architecture` 的 `period` 由「古代」改「中世纪」（与 `islamic-architecture`/`byzantine` 一致、符合 661–750 早期中世纪），同步 `time_or_place`；若保留地区惯例须在 `DECISIONS.md` 明文记录。
  2. **（应做，问题④）**：为 `early-islamic-architecture` 补一份**真正述及倭马亚清真寺形制（方形平面/柱廊/hypostyle）的第二来源**以实现关键事实双源互证；否则在正文与 pending 明确标注「形制据 wp 单源，待第二源核」（当前已 needs_verification=true，但 pending 需据实披露）。
  3. **（应做，问题③⑤）**：`early-islamic-architecture` 实例据源补「地点（耶路撒冷/大马士革）、主事者（阿卜杜勒·马利克/瓦利德一世）」，并将 pending 由“具体实例待补充”改为据实措辞（含形制单源说明）。
  4. **（宜做，问题②⑥）**：`picturesque` overview 将「起伏地形/树木掩映」改为源内实词（不规则/野趣/废墟/入画构图）或据源补证；实例 pending 酌情补具名如画园林。
  5. **（宜做，问题⑦，系统性）**：为两图补「设计意图或尺寸关系」文字标注（picturesque：不规则曲线=地形/路径、点景=掩映；early-islamic：方框=方形平面、圆=穹顶、横线=柱廊），并全站统一补强（延续第44/45/46 轮）。
  6. **（宜做，问题⑧）**：`artincontext-islamic-art` 的 `title` 存全名或备注站点。
- **流程记录**：本轮抽检 2 条＝**内容 1 合格（picturesque）、1 待核实（early-islamic，形制单源）、0 不合格、0 编造、0 假 id、0 死链、七节/规范/元数据/pending 结构联动一致、check.py PASS、相似度全 <0.54**；**主要遗留：early-islamic period 口径（古代→中世纪，须修）＋关键形制单源（须第二源或据实披露）＋「一图」缺设计意图/尺寸标注（系统性，宜修）**；不触发 §E 返工/降级。**（注：本报告基于 `batch-46.json` 8616B@10:25:45 更新后快照；round46 报告点名的 mughal period 与 imperial/mughal 实例问题已在此之前修复。）**

---

### 机器可读汇总

```
ROUND=46
SAMPLER=spotcheck-r46b
MODE=补抽（batch-46 4条中另2条：picturesque / early-islamic-architecture；与 round46 的 imperial/mughal 合覆盖全4条）
SCOPE=["picturesque","early-islamic-architecture"]
FILES={"picturesque":"entries/batch-46.json","early-islamic-architecture":"entries/batch-46.json"}
STATE={"sources.json":"144993B@2026-11-23 10:25:45","batch-46.json":"8616B@2026-11-23 10:25:45","coverage.json":"86274B@2026-11-23 10:25:45","check.py":"15908B@2026-11-22 15:11:54","total":255,"written":255,"all_level":"L2","pending_total":223,"sources_total":308,"sources_verified_true":305,"sources_verified_false":3,"link_ok_true":145,"link_ok_false":6,"link_ok_null":157}
VERSION_DRIFT="batch-46.json 8510B@10:20:11 -> 8616B@10:25:45; mughal period 中世纪->文艺复兴至19世纪; imperial/mughal instances filled; picturesque/early-islamic instances still '地点与设计者不适用'"
GIT_HEAD="2dd6338 docs: record final push pending (network)"; GIT_STATUS="round46 WIP in worktree; targets stable; only file this spotcheck wrote = research/spotcheck-round46b.md"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2 条 (batch-46 4条中另2条); 合并 round46 覆盖 4/4 >= 3 (§E min met by pair)"
FETCH_METHOD="urllib+ChromeUA(retry5-6); en.wikipedia -> owiki.org mirror; tate/artincontext direct; 4/4 HTTP200; analysis in-memory, no temp file"
SOURCES={"count_distinct":4,"count_refs":4,"all_exist":true,"all_verified_true":true,"all_reachable_200":"4/4","link_ok":{"wp-picturesque":null,"tate-picturesque":null,"wp-umayyad-architecture":null,"artincontext-islamic-art":null},
 "title_note":"artincontext-islamic-art record title='Islamic Art — Art in Context' vs actual <title>='Islamic Art - A Deep Dive into the Gilded World of Islamic Art' (org matches; subtitle missing) -> minor",
 "point_checks":{"tate-picturesque":"CONFIRMED describes picturesque: 'ideal type of landscape that has an artistic appeal...beautiful but also with some elements of wildness' + 'In between came the picturesque...wildness or irregularity'","artincontext-islamic-art":"CONFIRMED mentions Umayyad('ruled 661 to 750 CE')+Dome of the Rock('shrine in Jerusalem')+mosques+'Byzantine-style dome'; BUT hypostyle=0/colonnade=0/architectural-square=0 -> thin/general, zero coverage of Umayyad mosque form"}}
BODY_SUPPORT={
 "picturesque":"definition DIRECT dual-source (wp: aesthetic ideal/Gilpin/picture-like/irregularity/ruins; tate: ideal landscape/artistic appeal/beautiful+wildness/between sublime&beautiful); overview core DIRECT dual-source (between beautiful&sublime + ruins); 原理 ratio=0.1649 independent; instance type-level supported; MINOR overview '起伏地形/树木掩映' loose paraphrase; VERDICT=合格",
 "early-islamic-architecture":"definition concept-level dual-source (Umayyad 661-750 ✓✓; mosque/sanctuary ✓✓; dome ✓✓) BUT '方形平面'+'柱廊(hypostyle)' single-source(wp only; artincontext 0); overview same; 原理 ratio=0.2708 independent; instance Dome of the Rock dual + Umayyad Mosque wp but '地点/设计者不适用' contradicts sources (Jerusalem/Damascus, Abd al-Malik/Al-Walid I); PERIOD ISSUE 古代 should be 中世纪; VERDICT=待核实 (key form facts de-facto single-source, non-fabrication)"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2, no overflow, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","原理_concat":{"picturesque":0.1649,"early-islamic-architecture":0.2708}}
SVG_NOTE={"uniqueness":"both SVG strings unique across 255 library; distinct from other batch-46 svgs","picturesque":"path(irregular curve)+circle(spot/element) topical; no intent/dimension annotation","early-islamic-architecture":"rect(square plan)+circle(dome)+line(colonnade/axis) topical; no intent/dimension annotation","verdict":"机械项+唯一性全过; 缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x2","source_count":"2=2 / 2=2","nvc":"1 x2","needs_verification":"true x2","related":"[] x2 (no dangling)","pending_consistency":"逐字一致 x2","period_region_note":"picturesque 跨时期/欧洲 OK(可细化英国); early-islamic 古代/伊斯兰南亚 = ISSUE(661-750 应为中世纪, 与 islamic-architecture=中世纪/byzantine=中世纪 矛盾; 见问题①)"}
SIMILARITY={
 "picturesque":{"vs_existing_short":0.2647,"vs_existing_short_entry":"trompe-loeil","vs_existing_full":0.4139,"vs_existing_full_entry":"rockery","verdict":"PASS<0.54"},
 "early-islamic-architecture":{"vs_existing_short":0.3919,"vs_existing_short_entry":"islamic-architecture","vs_existing_full":0.4544,"vs_existing_full_entry":"islamic-architecture","verdict":"PASS<0.54"},
 "batch46_pairwise_full_max":0.3605,"batch46_pairwise_full_max_pair":"picturesque vs early-islamic",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-46 exactly -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"picturesque":"合格","early-islamic-architecture":"待核实(关键形制实质单源); 须修 period 古代->中世纪 + 实例补地点/主事者"}
VERDICT_SVG={"picturesque":"机械项+唯一性通过/形态贴合, 缺意图·尺寸标注(次要)","early-islamic-architecture":"机械项+唯一性通过/形态贴合, 缺意图·尺寸标注(次要)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
BATCH_ACTION="No rollback/downgrade: no 不合格 (1 合格 + 1 待核实), 0 fabrication/0 fake id/0 dead link; similarity all <0.54. Required fix: (1) early-islamic period 古代->中世纪; (2) add true 2nd source for Umayyad mosque form (square/colonnade/hypostyle) or mark single-source in pending; (3) early-islamic instance fill location(Jerusalem/Damascus)+patron(Abd al-Malik/Al-Walid I); (4) picturesque trim overview unsupported adjectives; (5) site-wide SVG 设计意图/尺寸关系 annotation; (6) artincontext title full name."
READONLY="only wrote research/spotcheck-round46b.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (no persistent temp file)"
```

*（报告完）*
