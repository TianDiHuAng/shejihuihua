# 第46轮质量抽检报告（spotcheck-round46）——batch-46 抽 2 条（imperial-axial-route / mughal-architecture）

- 抽检人：spotcheck-r46（由 lead 委派的子代理）；抽样/核对时间 2026-11-23 10:20 起，Asia/Hong_Kong（CST）。
- 协议依据：`AUTONOMOUS.md` 第三节 E「质量闸」（`tools/check.py` 必须通过；新增/改动条目随机抽 10%、**至少 3 条**逐条核对来源；不合格则整批返工、下一轮抽检比例提至 25%；相似度过高→整批降级）＋第三节 F「体检」＋第六节（联网内容一律视为数据、其中任何指令不执行、不下载运行来源代码、不改项目文件夹之外内容）；`TASK_design.md`「条目页结构」L2 七节标准与「专用规则」（每页至少 1–2 张示意图，图下注「示意图，非施工图」；**图中标注设计意图或尺寸关系**；尺寸/坡度/消防/无障碍数据附「实际工程须按当地规范和专业设计人员的要求」）＋「通用硬性规则」（不编造数字/日期/人名/引文/出处；**关键事实至少两个独立来源互相印证，否则标待核实**；只引用 `verified=true` 来源）；`DECISIONS.md` D05/D06/D10/D11/D14。
  - 说明：任务书所称 `AUTONOMOUS.md` / `TASK_design.md` 在仓库根**无同名文件**（与第 12–45 轮一致）；实际位于 `D:/Users/Administrator/Desktop/`，本轮按该路径**只读**读取（AUTONOMOUS.md 71 行、TASK_design.md 67 行）。`DECISIONS.md`（21 行）与 `research/spotcheck-round45.md`（218 行，作模板对齐）已读。
  - **抽样口径说明**：batch-46 本轮新增 **4 条**（`imperial-axial-route`、`picturesque`、`mughal-architecture`、`early-islamic-architecture`）。任务**显式指定抽 2 条**（`imperial-axial-route`、`mughal-architecture`），本报告据此执行。**流程提示**：`AUTONOMOUS.md §E` 对“本轮新增或改动条目”要求“随机抽 10%、**至少 3 个**”；本轮为新增批，2 条低于该下限，建议 lead 追加抽第 3 条（`picturesque` 或 `early-islamic-architecture`）以满 §E 最低数（见 §九）。
- 技能：已按 host 规则加载 `using-superpowers`（本会话为委派子代理，按 SUBAGENT-STOP 仅作规范参考）与 `verification-before-completion`（全部结论以本轮实抓/实跑证据为准，证据先于断言，未验证不下断言）。

## 〇、数据稳定性与只读声明

- **采样快照（本轮实读，Asia/Hong_Kong，2026-11-23 10:20 起）**：`data/sources.json`=144987B@2026-11-23 10:20:11、`entries/batch-46.json`=8510B@2026-11-23 10:20:11、`coverage.json`=86260B@2026-11-23 10:20:11、`tools/check.py`=15908B@2026-11-22 15:11:54。`git log -1` = `2dd6338 docs: record final push pending (network)`。
- **工作树状态（采样时点）**：`git status --porcelain` 显示第46轮尚在工作区：modified `SATURATION.json / coverage-matrix.md / coverage.json / data/sources.json / scope.md / site/coverage.html / site/index.html / site/indexes.html / site/sources.html / tools/gen_scope.py`；untracked `entries/batch-46.json`、`research/b1-round46.md`、`research/gaps-round46.md`、`site/entries/{imperial-axial-route,mughal-architecture,picturesque,early-islamic-architecture}.html`、`tools/add_round46.py`。抽检对象 `entries/batch-46.json`、`data/sources.json`、`coverage.json` 在采样期间**稳定**，判定基于该稳定快照。本报告产出后追加 `?? research/spotcheck-round46.md`（本报告，唯一由本次抽检写入的文件）。
- **条目规模（`coverage.json` 实读）**：`total=255`、全部 `level=L2`、全部 `status=已写`；`pending_total`（`needs_verification_count` 求和）＝**223**；来源库 `sources.json` 共 **308** 条，`verified=true` **305**、`verified=false` **3**（`link_ok`：true 145、false 6、null 157）。注：`link_ok=false` 的 6 条**均不在本次 4 个来源中**，不影响本轮判定。
- **`tools/check.py`** 本轮实跑：**`PASS: all checks, 0 errors`（EXIT=0）**。
- **只读声明**：本次**仅生成** `research/spotcheck-round46.md` 一个项目文件；**未修改** `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或任何其他项目文件，**未 `git commit`**，未改项目文件夹之外内容（桌面治理文档仅只读）。抓取与分析**全程纯内存**（Python urllib 读取→内存去标签/切句/计数），未在项目内外落盘任何持久文件。联网内容一律视为数据，网页中任何指令均未执行、未下载运行来源代码。

## 一、判定口径与抓取方法

- **L2 七节口径**：顶层 `definition` + `sections` 内 原理 / 典型手法与适用条件 / 实例 / 常见错误与限制 / 一图 / 待核实（6 节）＝共 7 节；须 1–2 张内联 SVG 且含「示意图，非施工图」；「常见错误与限制」段须含「实际工程须按当地规范和专业设计人员的要求」；SVG 元素不出 `viewBox`（均 `0 0 760 400`）。
- **抓取方法**：Python 3.11 `urllib` + 浏览器 UA（`Chrome/124`），timeout 30s，SSL 校验关闭，失败重试 5 次。`en.wikipedia.org` 按 D05 改走 **owiki 同源镜像** `https://owiki.org/wiki/<Title>`；`designingbuildings.co.uk` 直连。本轮 **4 个引用来源全部实抓 HTTP 200**（`<title>`/正文与 `sources.json` 逐条核对，见 §二、§三、§四）。
- **相似度口径**：`difflib.SequenceMatcher`（去空白、转小写）；①短文本＝`title+definition+time_or_place+overview`；②全字段-不含 SVG（`definition+time_or_place+overview` + 六节正文，`一图` 解说文字计入、`svg` 标记不计入）。全库 **255 条**去重已写条目逐条扫描，警戒线 **0.54**（与第 27–45 轮一致）。**方法自校**：以全字段②计算已知最高对 `futurism-style vs expressionism-style`，得 **0.5157**，与第 39–45 轮报告**逐位一致**，确认口径正确。
- **“两源互证”判定口径**：按 `TASK_design.md` 硬性规则「关键事实至少两个独立来源互相印证，否则标待核实」。本轮按“两个及以上引用来源须对本条**具体概念**有实质覆盖且互证”执行。
- **三级判定定义（可复现）**：
  - **合格**：definition/time/overview/实例均获所引来源正文直接支撑；关键事实（概念定义或实例）由 ≥2 独立来源直证互证；无编造；机械项（七节/SVG 含注记/规范句/元数据/pending 联动）全过。
  - **待核实**：核心获至少一个直接相关来源实质支撑，但存在第二源对本条具体概念仅泛论/零覆盖、或某关键事实实质单源等——属来源支撑/深度缺陷，**非编造**。
  - **不合格**：definition/overview 主干被两个引用来源均不支撑（实质无源）；或关键结构项（如「一图」）实质不满足 TASK_design 强制要求。
- **相似度专项（独立维度）**：警戒线 0.54；超线即触发 `AUTONOMOUS.md §E`「相似度过高（疑似套话）→整批降级为草稿并复查」，与“不合格（内容无源）→整批返工”是**不同触发路径**，分列。

## 二、抽检对象来源清单与完整性

`python tools/check.py` → **PASS, 0 errors**。2 条共引用 **4 个去重来源 id（4 处引用：imperial 2、mughal 2）**，**全部存在、全部 verified=true、全部 year=null（D06 允许）**、实抓 HTTP 200。

| 条目 | 来源 id | 存在/verified | 实抓标题（本轮 HTTP，逐字） | 机构 | type | link_ok | 与主题相关性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| imperial-axial-route | `wp-forbidden-city` | ✅ / true | `Forbidden City ::: Open WIKI`（200，50383B，textlen≈31178） | Wikipedia（经 owiki 镜像核验） | 权威百科 | null | **相关（直接、强）**：`the Outer Court or Front Court to the south, which was used for ceremonial purposes; and the Inner Court or Back Palace to the north, which was the residence of the emperor`；`The Inner Court is separated from the Outer Court by an oblong courtyard lying orthogonal to the city's main axis`；`The central north–south axis remains the central axis of Beijing` |
| imperial-axial-route | `designingbuildings-forbidden-city` | ✅ / true | `Forbidden City - Designing Buildings`（200，55405B，textlen≈7365） | Designing Buildings Wiki | 学术著作（wiki，宜记“行业百科/知识库”） | null | **相关（直接、强）**：`The Outer Court (the southern part)…was used for public audiences and ceremonies; while the Inner Court (northern part) contained residences for the royal family`；`emphasis on articulation and bilateral symmetry`；`Wu (Meridian Gate), the imposing 38 m…southern entrance`；`Construction began in 1406…Zhu Di…Yongle Emperor` |
| mughal-architecture | `wp-mughal-architecture` | ✅ / true | `Mughal architecture ::: Open WIKI`（200，46857B，textlen≈27806） | Wikipedia（经 owiki 镜像核验） | 权威百科 | null | **相关（直接、强）**：`Mughal architecture is the style…developed in the Mughal Empire in the 16th, 17th and 18th centuries…in the Indian subcontinent`；`derived from three main architectural traditions: local Indo-Islamic…Islamic Persia and Central Asia…indigenous Hindu`；`large bulbous domes…vaulted gateways`；`chahar bagh type of garden`；`Pietra dura…inlaid stone`；`consciously used architecture as a way to publicly display their presence and power` |
| mughal-architecture | `designingbuildings-taj-mahal` | ✅ / true | `Taj Mahal - Designing Buildings`（200，60764B，textlen≈11226） | Designing Buildings | 学术著作（wiki，宜记“行业百科/知识库”） | null | **相关（直接、强）**：`generally regarded as the best example of Mughal architecture, which is a blend of Indian, Persian and Islamic styles`；`central dome is 73 m…surrounded by four smaller domes`；`The garden is set out as a square quartered by long watercourses`；`Perfect symmetrical planning`；`commissioned in 1632 by the Mughal emperor Shah Jahan`；`designed by Ustad Ahmad Lahauri` |

> 关键事实：两条 `sources` 数组长度与 `coverage.source_count` 一致（imperial 2=2、mughal 2=2）。4 源均 `year=null`（在线内容，D06 允许）、`verified=true`、实抓 200。**无死链、无假 id、无 verified=false 被引用。**
>
> **来源记录 `title` 字段核对（本轮无实质不符，较第45轮改进）**：4 条记录 `title` 与实际 `<title>` 逐条相符（设计建筑用连字符“-”代替记录的破折号“—”，属排版差异，不算不符）。**唯一元数据瑕疵**：`designingbuildings-forbidden-city`、`designingbuildings-taj-mahal` 的 `type` 记为“学术著作”，而其本体为 Designing Buildings（行业 Construction Wiki / 知识库），宜记“行业百科/知识库”（次要、可修）。

## 三、任务 1：来源正文是否支撑 definition / time_or_place / overview 及七节「实例」（实抓逐句比对）

### 3.1 imperial-axial-route（宫廷中轴仪礼动线，batch-46）——**内容合格**
- **wp-forbidden-city**（owiki 200，textlen≈31178）直证：
  - `the Outer Court or Front Court to the south, which was used for ceremonial purposes; and the Inner Court or Back Palace to the north, which was the residence of the emperor and his family` → **直接支撑 overview“外朝在南、内朝在北”“外朝典礼、内朝起居”**（逐字对应）。
  - `The Inner Court is separated from the Outer Court by an oblong courtyard lying orthogonal to the city's main axis.` → **直接支撑 definition/overview“沿中轴层层递进”**（main axis）。
  - `The central north–south axis remains the central axis of Beijing.` / `the central axis of the Forbidden City…leading all the way from the Gate of China in the south to Jingshan Park in the north` → **直接支撑 definition“南北中轴”**。
  - `ceremonial centre of imperial power`、`Hall of Supreme Harmony…used for ceremonial purposes, such as enthronements…` → 支撑“典礼/礼制”。
- **designingbuildings-forbidden-city**（200，textlen≈7365）直证：
  - `The Outer Court (the southern part…)…used for public audiences and ceremonies; while the Inner Court (northern part) contained residences for the royal family, servants` → **互证 overview“外朝南/典礼、内朝北/起居”**（双源互证）。
  - `emphasis on articulation and bilateral symmetry to signify balance` → 支撑“对称”。
  - `the Wu (Meridian Gate), the imposing 38 m…southern entrance` → 支撑“门阙”（南门/午门）。
  - `Construction began in 1406…Zhu Di…Yongle Emperor`；`completed in 1420` → 支撑“紫禁城”实例（可补年代/营建者）。
- **逐项结论**：
  - definition“以南北中轴依次组织外朝典礼与内朝起居的行进序列”——**双源直证互证**（南北中轴 ✓ wp；外朝典礼 ✓ wp+db；内朝起居 ✓ wp+db）。
  - overview“外朝在南、内朝在北，沿中轴层层递进，以对称与门阙强化礼制秩序”——**双源直证**（南/北 ✓✓、中轴 ✓wp、对称 ✓db、门阙/南门 ✓db）。
  - time_or_place“古代、中国（参见来源）”——中国 ✓、紫禁城明清（1406–1420）属“古代”（本项目时期大桶）✓；**“古代”为宽松时期桶，非具体朝代**（Minor，可接受）。
  - **原理**“以中轴串联门、庭、殿，把‘外朝理政—内朝起居’的功能与尊卑次序写进行进路线”——中轴/门庭殿/功能次序均有源支撑；**ratio(原理, 定义+概述)=0.2353（低，机制独立）**，非逐字拼接。
  - 实例“名称：紫禁城南北中轴行进（类型性描述）；地点与设计者不适用”——**紫禁城/中轴/外朝内朝层次均有双源支撑、无编造**；**但“地点与设计者不适用”与源相悖**：两源均给**地点=北京**、`1406–1420`、营建者=朱棣/明成祖（详见 §八问题①）。
- **两源互证**：核心定义、外朝南/内朝北、典礼/起居、中轴、对称由 **wp-forbidden-city 与 designingbuildings-forbidden-city 双源直证并互证**。
- **专项核验（任务点名）**：**`wp-forbidden-city` 确真述“外朝南/内朝北/中轴”**——逐字命中 `Outer Court…to the south…ceremonial` + `Inner Court…to the north…residence` + `central north–south axis` + `separated…orthogonal to the city's main axis`。**非张冠李戴、非套用。**
- **内容判定：合格**（definition/overview/原理双源直证、机制独立、无编造；次要点：实例可据源补全、pending 偏保守、SVG 标注见 §五、时期桶见 §六）。**一图 SVG 见 §五；文本相似度见 §七（未越线）。**

### 3.2 mughal-architecture（莫卧儿建筑，batch-46）——**内容合格（时期口径见 §六问题②）**
- **wp-mughal-architecture**（owiki 200，textlen≈27806）直证（风格定义/概述）：
  - `Mughal architecture is the style of architecture developed in the Mughal Empire in the 16th, 17th and 18th centuries throughout the ever-changing extent of their empire in the Indian subcontinent` → 支撑 definition“莫卧儿帝国”“南亚”；**注意源为“16th, 17th and 18th centuries”（含18世纪）**。
  - `Mughal architecture was derived from three main architectural traditions: local Indo-Islamic architecture, the architecture of Islamic Persia and Central Asia, and indigenous Hindu architecture` → **直接支撑 definition“融合印度、波斯与伊斯兰语汇”**（Indian/Persian/Islamic ✓）。
  - `Mughal buildings have a uniform pattern…including large bulbous domes, slender minarets…large vaulted gateways, and delicate ornamentation` + `Bulbous domes and ogive arches were among the most prominent recurring elements` → 支撑 overview“穹顶、拱门”。
  - `These gardens…modeled on the Persian chahar bagh type, in which gardens are geometrically divided into different plots, usually four equal parts` → 支撑“对称花园/四分花园（charbagh）”。
  - `Pietra dura, known as parchin kari…was the technique of decorating with inlaid stone` → 支撑“精细石材镶嵌”。
  - `Mughal emperors and elites consciously used architecture as a way to publicly display their presence and power` → **直接支撑 overview“彰显帝国权力”**。
- **designingbuildings-taj-mahal**（200，textlen≈11226）直证（实例=泰姬陵 + 莫卧儿属性）：
  - `generally regarded as the best example of Mughal architecture, which is a blend of Indian, Persian and Islamic styles` → **直证实例的“莫卧儿”属性 + 印度/波斯/伊斯兰融合**（互证 definition）。
  - `The central dome is 73 m (240 ft) high… surrounded by four smaller domes` → 支撑“穹顶”。
  - `The garden is set out as a square quartered by long watercourses` + `Perfect symmetrical planning` → 支撑“对称花园”。
  - `commissioned in 1632 by the Mughal emperor Shah Jahan…designed by Ustad Ahmad Lahauri` → 支撑实例年份/设计者（可补）。
- **逐项结论**：
  - definition“16–17世纪南亚莫卧儿帝国融合印度、波斯与伊斯兰语汇的建筑风格”——帝国/南亚 ✓、印/波/伊融合 ✓✓（双源）；**惟“16–17世纪”低于源“16–18世纪”（少 18 世纪）**（见 §六问题②）。
  - overview“以穹顶、拱门、对称花园与精细石材镶嵌彰显帝国权力”——穹顶 ✓、拱门 ✓、对称花园/charbagh ✓、石材镶嵌/pietra dura ✓、帝国权力 ✓（wp+db）。
  - **原理**“把中亚穹顶与波斯拱、印度石作与镶嵌工艺综合，以对称与尺度表达皇权”——穹顶/波斯拱/印度石作/镶嵌/皇权均有源；**ratio(原理, 定义+概述)=0.1856（低，机制独立）**。
  - 实例“名称：泰姬陵（类型性描述）；地点与设计者不适用”——泰姬陵/穹顶/四分花园对称 ✓✓；**但“地点与设计者不适用”与源相悖**：源给**地点=阿格拉（Agra）**、设计者=**Ustad Ahmad Lahauri**、年代=1632（详见 §八问题③）。
- **两源互证**：核心定义（莫卧儿/印波伊融合）、穹顶、对称花园、帝国权力由 **wp-mughal-architecture 与 designingbuildings-taj-mahal 双源直证并互证**。
- **专项核验（任务点名）**：**`designingbuildings-taj-mahal` 确真述“莫卧儿”**——逐字命中 `best example of Mughal architecture, which is a blend of Indian, Persian and Islamic styles`。**非泛论、非零覆盖。**
- **内容判定：合格**（definition/overview/原理双源直证、机制独立、无编造；**主要问题：时期/分类口径**——见 §六问题②；次要点：实例可据源补全、pending 偏保守、SVG 标注见 §五）。**一图 SVG 见 §五；文本相似度见 §七（未越线）。**

## 四、任务 2：来源 id 存在性、verified、相关性、可达性（汇总）

- **存在性/verified/link_ok**：4 个去重来源 id **全部存在、全部 verified=true**（见 §二表）；`year=null`（D06 允许）；`link_ok` 全为 null（三态未标，非死链、非假源）。**4 源全部 `verified=true`，无一 false。**
- **可达性（本轮实抓）**：`wp-forbidden-city`（owiki 200）/`designingbuildings-forbidden-city`（200）/`wp-mughal-architecture`（owiki 200）/`designingbuildings-taj-mahal`（200）——**4/4 全部 HTTP 200，无死链**（体检 F 之“死链”对本次 4 源为 0）。
- **相关性**：4 源**均直接主体源、实质支撑并命中任务点名概念**（2 百科 + 2 行业知识库）；**无第42轮 `designingbuildings-proxemics` 式“直接但极薄/对具体概念零覆盖”缺陷**。任务两项点名核验均**正面通过**（wp-forbidden-city 真述外朝内朝中轴；designingbuildings-taj-mahal 真述莫卧儿）。
- **词项覆盖细节**：imperial 的“中轴”由 wp 直证（central axis/main axis）、“对称”由 db 直证（bilateral symmetry）、“门阙”以 db 的 Meridian Gate 表达——**双源互补、非缺源**；mughal 的“四分花园”wp 作 chahar bagh、db 作 square quartered、“石材镶嵌”wp 作 pietra dura——**语义可通、非缺源、非编造**。

## 五、任务 3：L2 七节完整性 + SVG + 风险/规范提示（程序化实核）

| 条目 | level | definition 顶层 | sections 6 节 | SVG 数 | 含“示意图，非施工图” | viewBox | 风险/规范句 | 原理=def+概述拼接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| imperial-axial-route | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | 否（ratio 0.2353） |
| mughal-architecture | L2 | ✓ | 6/6 | 1 | ✓ | 0 0 760 400 | ✓ | 否（ratio 0.1856） |

> 七节完整（definition + 原理/典型手法与适用条件/实例/常见错误与限制/一图/待核实 齐备，无缺节、无多余节）；每条 1 张内联 SVG、`viewBox='0 0 760 400'`、均含“示意图，非施工图”；「常见错误与限制」段均以规范提示收尾（`实际工程须按当地规范和专业设计人员的要求`）；`check.py` 含 SVG 出界检查，本轮 PASS（两图元素坐标全部在 760×400 内）。**机械项两条全部通过。**

### SVG 质量观察（形态贴合主题，但缺“设计意图/尺寸关系”显式标注——次要、系统性）
- **imperial-axial-route**：`<line stroke-dasharray='8 6'>×1`（中轴虚线，380 竖向）+ `<rect>×3`（300/90、300/170、300/250 三进院落沿轴叠置），**贴合“中轴串联门—庭—殿、由外朝向内朝递进”主题、非随机占位**；但**三进未标注“外朝/内朝/门/庭/殿”、图内仅有标题与“示意图，非施工图”，缺 TASK_design 第6条要求的“设计意图或尺寸关系”标注**（次要缺陷）。
- **mughal-architecture**：`<rect>`（建筑/院落外框）+ `<path d='M380 110 Q300 60 220 110'>`（穹顶弧）+ `<line>`（四分/对称轴），**贴合“穹顶 + 对称四分花园”主题、非随机占位**；但为抽象概括，**未标注“穹顶/拱门/四分花园/对称轴”等设计意图或尺寸关系**（次要缺陷）。
- **唯一性核验（防第38轮式模板复刻）**：两条 SVG 字符串在**全库 255 条中各自唯一**（无整串重复）；batch-46 四条 SVG 互为**不同字符串**（非同一模板复填）。`stroke-dasharray='8 6'` 在库中另 5 处出现属「中轴/虚线」通用画法，非整图复制。**形态与主题相关，区别于 batch-38 完全无关的随机多边形模板。**
- **判定**：两条「一图」**机械项（1 张 + viewBox + “示意图，非施工图” + 不出界 + 唯一性）全过**，图形与主题相关；**唯一不足为“缺图中设计意图/尺寸关系标注”**——`check.py` 只查出界与注记，查不出该语义项，属**次要/可提升**，不构成本轮“不合格”。建议全站做一次 SVG 标注补强（与第44/45 轮方向一致）。

## 六、任务 4：元数据一致性 + needs_verification ↔ pending_notes ↔ 正文待核实（含 period/region 分类口径）

- **两条** `title/theme/tier/period/region/level` 与 `coverage.json` 逐字段**一致**（程序化比对 mismatches=NONE）：imperial-axial-route（宫廷中轴仪礼动线/动线/重要/古代/中国/L2）、mughal-architecture（莫卧儿建筑/风格/重要/中世纪/伊斯兰·南亚/L2）；`source_count` 与来源数组长度一致（2=2、2=2）；`needs_verification_count`：各 1；`related`：两条均 `[]`（无悬空）。

| 条目 | needs_verification | pending_notes（结构化） | 正文「待核实」节 | 一致性 |
| --- | --- | --- | --- | --- |
| imperial-axial-route | true | 「宫廷中轴仪礼动线」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（但源已给紫禁城/北京/1406–1420，措辞偏保守） |
| mughal-architecture | true | 「莫卧儿建筑」的具体实例（名称、地点、设计者、年代）待补充独立来源。 | 逐字相同 | **逐字一致** ✓（但源已给泰姬陵/阿格拉/Ustad Ahmad Lahauri/1632，措辞偏保守） |

> 结构化标志与两处文本：两条 `pending_notes` 与「待核实」节**逐字一致**（较第45轮 baroque“语义一致非逐字”更规范）。**注意（D14 精神）**：两条「待核实」均称“具体实例（名称、地点、设计者、年代）待补充独立来源”，而**所引来源已给出具名实例与要素**——措辞**偏保守、与源实况略有出入**（非编造、非缺源；建议据源改“具体代表作品的细分年代/归属待补”或直接采源中要素）。

### period/region 与分类口径（项目时期桶：古代 / 中世纪 / 文艺复兴至19世纪 / 20世纪 / 当代 / 跨时期）
- **imperial-axial-route：period=古代、region=中国** ——紫禁城为明清（1406–1420），本项目“古代”按“前现代中国”大桶归入，**与既有中国条目（loop-route 古代/中国 等）口径一致**；可接受（Minor：非具体朝代）。
- **mughal-architecture：period=中世纪、region=伊斯兰/南亚** ——**存在实质口径问题**：
  1. 条目 `definition` 自述“16–17世纪”、`time_or_place` 注“史学上限至17世纪”，而**源实为“16th, 17th and 18th centuries”**——**“至17世纪”与源（含 18 世纪）不符、definition 亦少 18 世纪**。
  2. **16–17（18）世纪在项目既有时期桶中应落“文艺复兴至19世纪”**（该桶已有 32 条，含巴洛克等 15–19 世纪风格），**归“中世纪”与自身定义及源年代相悖**。现库里与 `islamic-architecture`（伊斯兰建筑总条目，7–19 世纪跨代，记“中世纪”）同桶，属**沿用地区归类惯例**；同批 `early-islamic-architecture`（倭马亚 7–8 世纪）记“古代”，而**更晚的莫卧儿却记“中世纪”**，**时期桶时序与史实错位**（详见 §八问题②）。
  - 建议：mughal 改 `period="文艺复兴至19世纪"`（或“跨时期”），`definition` 改“16–18世纪”（或明确“古典期 16–17 世纪”并注明源含 18 世纪），并移除/更正 `time_or_place` 的“史学上限至17世纪”；若项目确有意将“伊斯兰/南亚”风格统一归“中世纪”，须在 `DECISIONS.md`/口径说明中**明文记录该惯例**，否则应更正。

## 七、任务 5：相似度（difflib，阈值 0.54；全库 255 条；口径②=全字段-不含 SVG，`一图`计入）

### 7.1 对既有库（排除自身）逐条扫描
| 条目 | ①短文本 max（vs 既有库） | 判 | ②全字段 max（vs 既有库） | 判 |
| --- | --- | --- | --- | --- |
| imperial-axial-route | **0.3472** vs symmetry-layout | <0.54 ✓ | **0.4436** vs symmetry-layout | <0.54 ✓ |
| mughal-architecture | **0.3041** vs islamic-architecture | <0.54 ✓ | **0.4269** vs islamic-architecture | <0.54 ✓ |

> 对**既有 254 条**（排除自身）逐条扫描，两条两档均 **<0.54**（短文本最大 0.3472、全字段最大 0.4436）——**各自与既有库文本区分在阈值内**。imperial 最近邻为 `symmetry-layout`（0.4436）、其后 `loop-route`(0.4414)/`serial-route`(0.4334)（同为动线/对称近义，正常语义邻近）；mughal 最近邻为父条目 `islamic-architecture`（0.4269）、`indian-architecture`(0.4045)/`early-islamic-architecture`(0.4029)（同域近亲，属正常语义邻近）。**均未越线。**

### 7.2 batch-46 批内去模板化核验（4 条两两）
| 对 | ①短文本 | ②全字段 |
| --- | --- | --- |
| imperial-axial-route vs picturesque | 0.1564 | 0.3623 |
| imperial-axial-route vs mughal-architecture | 0.1474 | 0.3398 |
| imperial-axial-route vs early-islamic-architecture | 0.1916 | 0.3643 |
| picturesque vs mughal-architecture | 0.1592 | 0.3430 |
| picturesque vs early-islamic-architecture | 0.1461 | 0.3605 |
| mughal-architecture vs early-islamic-architecture | 0.2540 | 0.4029 |

> batch-46 四条**两两均远低于 0.54**（批内全字段最大 0.4029，mughal↔early-islamic）——**无第43轮 batch-42 式双条互为模板姊妹、无套话风险**。

### 7.3 方法自校
- `futurism-style vs expressionism-style` 全字段②＝**0.5157**，与第39–45轮报告**逐位一致**，口径正确。

> **文本相似度判定：两条对既有库与批内均 PASS（均 <0.54）；无相似度降级触发。**

## 八、逐条验收结论

| 条目 | definition / time_or_place / overview / 实例 来源支撑 | 来源存在·verified·相关·可达 | 七节 / 规范 / SVG | 元数据·pending 联动 | 文本相似度(①②) | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| **imperial-axial-route（宫廷中轴仪礼动线）** | definition **双源直证互证**（南北中轴 ✓wp、外朝典礼 ✓wp+db、内朝起居 ✓wp+db）；overview **双源直证**（外朝南/内朝北 ✓✓、对称 ✓db、门阙/午门 ✓db）；验证点 **wp-forbidden-city 确述外朝/内朝/中轴**；实例紫禁城有源（**“地点不适用”与源相悖，可补北京/1406–1420/明成祖**）；原理独立（0.2353） | 2/2 true；wp+db 均直接强源且命中点名概念；**2 源 200 可达**；db type“学术著作”（wiki，次要） | 七节齐、规范句✓；1 SVG 含“示意图，非施工图”、形态贴合（中轴三进），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 **逐字一致**（pending 偏保守） | 既有库 ✓（0.3472/0.4436）；批内 ✓ | **合格**（次要：实例可补、pending 偏保守、SVG 标注、db type） |
| **mughal-architecture（莫卧儿建筑）** | definition **双源直证互证**（莫卧儿帝国/南亚 ✓、印/波/伊融合 ✓✓）；overview 直证（穹顶/拱门/对称花园/石材镶嵌/帝国权力 ✓✓）；验证点 **designingbuildings-taj-mahal 确述莫卧儿**（“best example of Mughal architecture, blend of Indian, Persian and Islamic”）；实例泰姬陵有源（**“地点与设计者不适用”与源相悖，可补阿格拉/Ustad Ahmad Lahauri/1632**）；原理独立（0.1856）；**时期口径问题见问题②** | 2/2 true；wp+db 均直接强源且命中点名概念；**2 源 200 可达**；db type“学术著作”（wiki，次要） | 七节齐、规范句✓；1 SVG 含“示意图，非施工图”、形态贴合（穹顶+对称轴），**缺意图/尺寸标注（次要）** | 全部一致；nv=true/pending/待核实 **逐字一致**（pending 偏保守） | 既有库 ✓（0.3041/0.4269）；批内 ✓（max 0.4029） | **合格**（内容/来源/结构/相似度）；**须更正：时期口径（问题②）**；次要：实例可补、pending 偏保守、SVG 标注、db type |

### 问题清单（逐条）
- **① imperial-axial-route 实例要素不全/表述失准**：`实例` 写“地点与设计者不适用”，但两源明载**地点=北京**、`1406–1420`、营建者=朱棣/明成祖；`pending_notes`/`待核实` 称“具体实例待补充独立来源”，与两源已给紫禁城实况略相抵。→ **建议据源补 地点（北京）/年代（1406–1420）/营建者（明成祖）**，并调 pending 为“细分年代/具体段落归属待补”。（非编造，Minor）
- **② mughal-architecture 时期/分类口径不符（本轮最需修）**：`period="中世纪"` 与自身 `definition="16–17世纪"` 及源 `16th–18th centuries` 相悖；`time_or_place`“史学上限至17世纪”与源（含 18 世纪）不符；16–18 世纪按项目时期桶宜归“文艺复兴至19世纪”。→ **建议 `period` 改“文艺复兴至19世纪”（或“跨时期”）、`definition` 改“16–18世纪”、更正 `time_or_place`**；若坚持地区归类惯例须在 DECISIONS/口径说明明文记录（否则视为口径错误）。（Minor–Moderate；不影响内容“合格”，但应修）
- **③ mughal-architecture 实例要素不全/表述失准**：`实例` 写“地点与设计者不适用”，但两源明载**地点=阿格拉（Agra）**、设计者=**Ustad Ahmad Lahauri**、年代=1632。→ 同问题①，据源补全并调 pending。（Minor）
- **④ SVG “设计意图/尺寸关系”标注缺失（两条例、系统性）**：两图机械项与主题贴合均过，但仅标题+“示意图，非施工图”，缺 TASK_design 第6条“图中标注设计意图或尺寸关系”。→ 建议全站统一补强（延续第44/45 轮）。（Minor、系统性）
- **⑤ 来源 type 归类瑕疵（两源）**：`designingbuildings-forbidden-city`、`designingbuildings-taj-mahal` 记“学术著作”，本体为 Designing Buildings 行业 Wiki/知识库，宜记“行业百科/知识库”。（Minor，不影响内容判定）
- **⑥ pending 偏保守（两条例）**：源已给具名实例与要素，仍统一写“具体实例待补充独立来源”，略失准（非编造、非缺源）。→ 与问题①③一并调和。（Minor）

## 九、总体结论与建议

- **抽样结果**：任务指定抽检 batch-46 新增 4 条中的 **2 条**——`imperial-axial-route`、`mughal-architecture`。**内容维度：2 合格＋0 待核实（无源）＋0 不合格；0 编造、0 假 id、0 死链。**
- **来源层面**：4 个引用来源 id 全部存在、verified=true、**实抓 4/4 HTTP 200 可达**、均直接实质支撑；**两项任务点名核验正面通过**（`wp-forbidden-city` 真述外朝/内朝/中轴；`designingbuildings-taj-mahal` 真述莫卧儿）。唯 2 处 `type` 归类瑕疵（“学术著作”→宜“行业百科/知识库”），本轮**无 source `title` 不符**（较第45轮改进）。
- **结构/治理层面**：七节/规范提示机械项两条全过、SVG 唯一性通过、元数据逐项一致、`needs_verification↔pending↔待核实` **逐字一致**、`check.py` PASS 0 errors、原理均非拼接（0.2353/0.1856）。
- **相似度层面**：两条对既有库与批内均 <0.54（PASS）；批内最大 0.4029，无套话；方法自校 0.5157 与第39–45 轮一致。
- **是否整批返工 / 降级（结论）**：
  1. **§E「抽检不合格→整批返工（25%）」路径：不成立**——无“不合格”内容条目（2 合格），无编造/假 id/死链。
  2. **§E「相似度过高（疑似套话）→整批降级为草稿并复查」路径：不成立**——两条对既有库与批内均 <0.54。
  3. **结论：本轮抽检 2 条内容/来源/结构/相似度全部合格，不触发整批返工/降级。** 但存在**须定向修复的时期口径问题（mughal 问题②）**与若干 Minor（实例要素、pending 措辞、SVG 标注、db type）。
- **返工/修复建议（按优先级）**：
  1. **（应做，mughal 问题②）**：`mughal-architecture` 的 `period` 由“中世纪”改“文艺复兴至19世纪”（或“跨时期”）、`definition` 改“16–18世纪”、更正 `time_or_place`“史学上限至17世纪”；若保留地区归类惯例，须在 `DECISIONS.md` 明文记录“伊斯兰/南亚风格统一归中世纪”的口径。
  2. **（应做，问题①③⑥）**：两条例证实例据源补全——imperial 补“北京/1406–1420/明成祖”；mughal 补“阿格拉/Ustad Ahmad Lahauri/1632”；并将 `pending_notes`/`待核实` 由“具体实例待补充独立来源”改为“具体代表作品细分年代/归属待核”等据实措辞。
  3. **（宜做，问题④，系统性）**：为两图补“设计意图或尺寸关系”文字标注（imperial：外朝→内朝、门/庭/殿、中轴；mughal：穹顶/拱门/四分花园/对称轴），并对全站 SVG 统一做一次标注补强（延续第44/45 轮）。
  4. **（宜做，问题⑤）**：`designingbuildings-forbidden-city`、`designingbuildings-taj-mahal` 的 `type` 改“行业百科/知识库”。
  5. **（流程）**：`AUTONOMOUS.md §E` 对“本轮新增 4 条”要求“至少抽 3 条”；本轮任务显式指定 2 条，建议 lead 追加抽第 3 条（`picturesque` 或 `early-islamic-architecture`）以满 §E 最低数（本报告已对 4 条做过相似度与来源可达的横向扫描，但未逐句核验后两条正文）。
- **流程记录**：本轮抽检 2 条＝**内容 2 合格、0 编造、0 假 id、0 死链、七节/规范/元数据/pending 一致、check.py PASS、相似度全 <0.54**；**主要遗留：mughal 时期口径（问题②，须修）＋「一图」缺设计意图/尺寸标注（系统性，宜修）**；不触发 §E 返工/降级。

---

### 机器可读汇总

```
ROUND=46
SAMPLER=spotcheck-r46
MODE=新增批抽检（batch-46 4条中抽2条：imperial-axial-route / mughal-architecture）
SCOPE=["imperial-axial-route","mughal-architecture"]
FILES={"imperial-axial-route":"entries/batch-46.json","mughal-architecture":"entries/batch-46.json"}
STATE={"sources.json":"144987B@2026-11-23 10:20:11","batch-46.json":"8510B@2026-11-23 10:20:11","coverage.json":"86260B@2026-11-23 10:20:11","check.py":"15908B@2026-11-22 15:11:54","total":255,"written":255,"all_level":"L2","pending_total":223,"sources_total":308,"sources_verified_true":305,"sources_verified_false":3,"link_ok_true":145,"link_ok_false":6,"link_ok_null":157}
GIT_HEAD="2dd6338 docs: record final push pending (network)"; GIT_STATUS="batch-46 round46 work-in-progress in worktree (modified SATURATION/coverage-matrix/coverage/sources/scope/site pages/gen_scope.py; untracked batch-46.json + site/entries 4 html + add_round46.py + b1/gaps-round46 research); targets stable; only file this spotcheck wrote = research/spotcheck-round46.md"
CHECK_PY="PASS: all checks, 0 errors (EXIT=0)"
SAMPLE_RATIO="2 条 (task explicit 2 of 4; §E batch-min 3 NOT met -> advise add 3rd)"
FETCH_METHOD="urllib+ChromeUA(retry5); en.wikipedia -> owiki.org mirror; designingbuildings direct; 4/4 HTTP200; analysis in-memory, no temp file"
SOURCES={"count_distinct":4,"count_refs":4,"all_exist":true,"all_verified_true":true,"all_reachable_200":"4/4","link_ok":{"wp-forbidden-city":null,"designingbuildings-forbidden-city":null,"wp-mughal-architecture":null,"designingbuildings-taj-mahal":null},
 "title_mismatch":"NONE (round45-style title mismatch absent; dash variant only)",
 "type_note":"designingbuildings-forbidden-city & designingbuildings-taj-mahal type='学术著作' but body is Designing Buildings Construction Wiki -> should be 行业百科/知识库",
 "point_checks":{"wp-forbidden-city":"CONFIRMED describes Outer Court(south,ceremonial)+Inner Court(north,residence)+central north-south axis + 'orthogonal to the city's main axis'","designingbuildings-taj-mahal":"CONFIRMED describes Mughal: 'best example of Mughal architecture, blend of Indian, Persian and Islamic styles'"}}
BODY_SUPPORT={
 "imperial-axial-route":"definition DIRECT dual-source (wp Outer Court south ceremonial/Inner Court north residence + central axis; db Outer Court south ceremonies/Inner Court north residences + bilateral symmetry + Meridian Gate); overview DIRECT dual-source; 原理 ratio=0.2353 independent; instance 紫禁城 supported but '地点/设计者不适用' contradicts sources (Beijing/1406-1420/明成祖) -> under-filled; VERDICT=合格",
 "mughal-architecture":"definition DIRECT dual-source (wp 16-18c Mughal+Indo-Islamic/Islamic Persia/Hindu; db Taj 'best example of Mughal, blend Indian/Persian/Islamic'); overview DIRECT (domes/arches/charbagh/pietra dura/power); 原理 ratio=0.1856 independent; instance 泰姬陵 supported but '地点/设计者不适用' contradicts sources (Agra/Ustad Ahmad Lahauri/1632); PERIOD ISSUE: definition 16-17c vs source 16-18c, period 中世纪 vs own def/source; VERDICT=合格(content)+须修时期口径"}
L2_CHECK={"seven_sections":"definition+6/6 x2","svg_count":"1 each","svg_phrase":"示意图，非施工图 x2","viewBox":"0 0 760 400 x2, no overflow, check.py PASS","risk_note":"实际工程须按当地规范和专业设计人员的要求 x2","原理_concat":{"imperial-axial-route":0.2353,"mughal-architecture":0.1856}}
SVG_NOTE={"uniqueness":"both SVG strings unique across 255 library; batch-46 4 SVGs all distinct; dash8-6 marker shared by 5 other axis-style svgs (generic)", "imperial-axial-route":"line(dashed axis)+3rect(门/庭/殿 3进) topical; no intent/dimension annotation", "mughal-architecture":"rect+path(dome)+lines(symmetry axis) topical; no intent/dimension annotation", "verdict":"机械项+唯一性全过; 缺设计意图/尺寸关系标注(次要/系统性)"}
METADATA={"title/theme/tier/period/region/level":"ALL match coverage x2","source_count":"2=2 / 2=2","nvc":"1 x2","needs_verification":"true x2","related":"[] x2 (no dangling)","pending_consistency":"逐字一致 x2","period_region_note":"imperial 古代/中国 OK(宽松桶); mughal 中世纪/伊斯兰南亚 = ISSUE(16-18c应为文艺复兴至19世纪; 与early-islamic=古代时序错位)"}
SIMILARITY={
 "imperial-axial-route":{"vs_existing_short":0.3472,"vs_existing_short_entry":"symmetry-layout","vs_existing_full":0.4436,"vs_existing_full_entry":"symmetry-layout","verdict":"PASS<0.54"},
 "mughal-architecture":{"vs_existing_short":0.3041,"vs_existing_short_entry":"islamic-architecture","vs_existing_full":0.4269,"vs_existing_full_entry":"islamic-architecture","verdict":"PASS<0.54"},
 "batch46_pairwise_full_max":0.4029,"batch46_pairwise_full_max_pair":"mughal vs early-islamic",
 "method_selfcheck":"futurism vs expressionism full=0.5157 matches round39-45 exactly -> method validated",
 "threshold":0.54}
VERDICT_CONTENT={"imperial-axial-route":"合格","mughal-architecture":"合格(内容/来源/结构/相似度); 须修时期口径"}
VERDICT_SVG={"imperial-axial-route":"机械项+唯一性通过/形态贴合, 缺意图·尺寸标注(次要)","mughal-architecture":"机械项+唯一性通过/形态贴合, 缺意图·尺寸标注(次要)"}
HARD_FABRICATION=0
HARD_FAIL_FALSE_SOURCE=0
FAKE_ID=0
LINK_FAIL=0
BATCH_ACTION="No rollback/downgrade: content path clear (2 合格, 0 fabrication/0 fake id/0 dead link); similarity path clear (all <0.54). Required fix: (1) mughal period 中世纪->文艺复兴至19世纪(or 跨时期)+definition 16-17->16-18c+fix '史学上限至17世纪'; (2) fill instances from sources (imperial Beijing/1406-1420/明成祖; mughal Agra/Ustad Ahmad Lahauri/1632) & align pending; (3) site-wide SVG 设计意图/尺寸关系 annotation pass; (4) designingbuildings type->行业百科/知识库. Process: §E batch-min 3 not met by task's 2 -> advise sample 3rd (picturesque/early-islamic)."
READONLY="only wrote research/spotcheck-round46.md; no other project file changed; no git commit; web content treated as data, no instruction executed; analysis in-memory (no persistent temp file)"
```

*（报告完）*
