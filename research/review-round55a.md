# 第 55 轮 B5 补源报告（review-round55a）——4 条“下沉空间”条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r55a（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读边界

- **已读上下文**：项目根 `AUTONOMOUS.md`、`TASK_design.md` 实读为 NOT_FOUND；按既有先例读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）与 `D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；项目 `DECISIONS.md`（25 行）、`research/review-round54b.md`（143 行）已读。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言：HTTP、标题、关键句逐条回验，见第五节）。
- **对象现状**：`entries/batch-35.json` 中 `sunken-garden`、`sunken-atrium`、`semi-sunken-space` 仍写“类型性描述/具体实例待补充独立来源”；`entries/batch-38.json` 中 `earth-sheltered` 仍写“具体实例（名称、地点、设计者、年代）待补充独立来源”。本报告仅为补源底稿，**未改条目数据**。
- **证据口径**：不编造名称、地点、设计者、年份、引文、出处；每条用两个不同机构的页面，同机构只算 1 源；搜索结果页只用于定位，不作证据；正文关键句均来自机构页面直接抓取并做 `norm()` 子串回验。联网内容一律按数据处理，网页中出现的任何指令均未执行。
- **通道说明**：部分站点的 `web_fetch` 受前端跳转/反爬影响，改用 `urllib` 浏览器 UA 直连页面；最终表中 HTTP 均为实际响应码。Britannica 等站点的反爬页未作证据。
- **只读声明**：本轮**仅生成** `research/review-round55a.md` 一个文件；未改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/`、`research/` 其他文件，未 `git commit`，未改项目文件夹之外内容。开工前 `git status --porcelain` 已有 `?? research/healthcheck-round55.md`（非本轮产物，未触碰）。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、原始 `<title>`、响应体；去 `<script>/<style>` 与标签后 `html.unescape`，再用 `norm()`（NFKC + 弯/直引号、破折号、零宽空格、不间断空格归一 + 空白折叠 + 小写）做关键句子串回验，`FOUND` 才写入正文。
2. **独立性**：两个来源必须来自不同机构/站点主体；建筑师事务所与其项目业主/博物馆可互证，但同一站点不同页面只算 1 源。
3. **权威性**：优先机构官方页（花园官方、博物馆官方、建筑师事务所官方）；补充权威行业组织/建筑媒体项目库（Communities in Bloom、ArchDaily）。
4. **空间类型支撑**：来源必须明确写出“下沉花园 / 地下大厅 / 覆土、草坡与地下展厅 / 开挖至地下室标高的下沉庭院”等可定位空间事实；仅有泛泛介绍不采用。
5. **落地约束**：本报告只读产出。落地时须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与 `sections.实例`，同步清理 `待核实`/`pending_notes`，复跑 `tools/check.py`；登记前不得视为已改。

## 二、四条复核（每条：名称 / 地点 / 设计者 / 年份 + 两条独立权威来源）

### 2.1 `sunken-garden`（下沉花园）→ **布查特花园下沉花园（The Sunken Garden, The Butchart Gardens）**

- **名称**：布查特花园下沉花园 / The Sunken Garden, The Butchart Gardens
- **地点**：**加拿大不列颠哥伦比亚省布伦特伍德湾、温哥华岛 Tod Inlet**（① “Vancouver Island … Tod Inlet”；② “located in Brentwood Bay, British Columbia”）
- **设计者 / 营造主体**：**Jennie Butchart**（① 园方直书 “Jennie envisioned a grand garden in its place … the quarry blossomed into today’s Sunken Garden”；② 不单列设计者，只作独立地点/年份/园名互证。诚实标注：落地写“Jennie Butchart 将废弃采石坑改造为下沉花园”，不把 Robert Butchart 写成唯一设计者。）
- **年份**：**1904（园区建立）；1912（园方年表中采石坑花园化节点）**（② “Established in 1904”；① “1904 Where it all began” / “1912 A passion project”。不写“下沉花园 1904 完工”，因为两源均未给出完工年。）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） | 对本空间类型的支撑 |
| --- | --- | --- | --- | --- | --- | --- |
| ① | The Butchart Gardens 官方园史（**强权威·花园官方机构**） | `https://butchartgardens.com/our-story/` | Our Story - The Butchart Gardens | **200** | “Coming from Ontario, husband and wife, Robert and Jennie Butchart moved to Vancouver Island to build a cement plant on a rich limestone deposit at Tod Inlet.”；“1912 A passion project As cement production exhausted the limestone deposits, Jennie envisioned a grand garden in its place and began transferring top soil by horse and cart. Little by little, the quarry blossomed into today’s Sunken Garden.” | 直接说明“采石坑→下沉花园”的生成机制、地点与营造主体，是下沉花园由低洼/开采遗迹转为绿化空间的实例证据。 |
| ② | Communities in Bloom 加拿大全国园艺展示页（**中—强权威·全国性园艺组织**） | `https://www.communitiesinbloom.ca/the-butchart-gardens-british-columbia-2026-national-special-attractions/` | The Butchart Gardens, British Columbia - 2026 National Special Attractions - Communities in Bloom | **200** | “Established in 1904, The Butchart Gardens is a world-famous horticultural attraction located in Brentwood Bay, British Columbia.”；“…including the iconic Sunken Garden, Rose Garden, Japanese Garden, Italian garden, and Mediterranean Garden.”；“As a National Historic Site of Canada…” | 独立确认年份、地点、该园确有 iconic Sunken Garden 及其加拿大国家历史遗址身份，补足非园方视角的双源互证。 |

**四要素对位**：名称＝Butchart Gardens 的 Sunken Garden（①②同名）；地点＝Brentwood Bay / Vancouver Island Tod Inlet（①详细地点、②省级地点）；设计者＝Jennie Butchart（①直书，②不单列，已标注）；年份＝1904 园区建立（②直书；①年表同记）、1912 采石坑改造节点（①直书）。

**独立性说明**：园方机构与加拿大 Communities in Bloom 全国组织是不同机构，非镜像页面，关键句均由各自页面直出，可作独立双源。

**保留标注**：设计者由园方一手园史单独命名，第二源仅互证园名/地点/年份；落地时如需“设计者双源逐字互证”，应另补第三源，但本条已满足任务要求的“具名实例 + 两条独立权威来源”。

### 2.2 `sunken-atrium`（地下中庭）→ **卢浮宫金字塔与拿破仑大厅地下大厅（Louvre Pyramid / Hall Napoléon underground lobby）**

- **名称**：卢浮宫金字塔及拿破仑大厅地下大厅 / Louvre Pyramid, Hall Napoléon underground lobby
- **地点**：**法国巴黎卢浮宫 Cour Napoléon**（① “Cour Napoléon”；② “Site 9 hectares, including areas within and below the existing museum”）
- **设计者**：**Ieoh Ming Pei / I. M. Pei（贝聿铭）**（① 直书 “Chinese-American architect Ieoh Ming Pei”；②为建筑师事务所 PCF 项目页，项目署名主体一致。）
- **年份**：**1989（金字塔 1989-03-29 落成启用）**（① “inaugurated on 29 March 1989”；②列该项目为 Grand Louvre Modernization，未以另一口径改年。）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） | 对本空间类型的支撑 |
| --- | --- | --- | --- | --- | --- | --- |
| ① | Musée du Louvre 官方建筑史页（**强权威·博物馆官方机构**） | `https://www.louvre.fr/en/explore/the-palace/a-pyramid-for-a-symbol` | A pyramid for a symbol - Cour Napoléon & Pyramid | **200** | “What a bold undertaking indeed on the part of the Chinese-American architect Ieoh Ming Pei, to transform the very heart of the palace.”；“Pei came up with the idea of a central underground lobby affording direct access to the museum’s three wings, which would transform visitor circulation inside the Louvre.”；“whilst creating the most transparent, light and luminous structure possible.”；“the Pyramid was inaugurated on 29 March 1989.” | 直接给出“central underground lobby + 三翼直达 + 透明采光结构 + 金字塔天窗/入口”，正是地下中庭借上部玻璃采光并把人流组织到多翼的实例。 |
| ② | PCF Architects（原 I. M. Pei 事务所）项目页（**强权威·建筑师事务所官方**） | `https://pcfarchitects.com/projects/grand-louvre-modernization/` | Grand Louvre Modernization - PCF Architects | **200** | “Public plaza, Hall Napoleon with underground links to museum wings, auditorium, restaurants, museum shop, boutiques, workshops”；“Site 9 hectares, including areas within and below the existing museum” | 从设计方项目档案独立确认 Hall Napoleon 的地下联络功能，以及工程范围包含既有博物馆上下空间，支撑“地下中庭/地下大厅连通多层多翼”的类型判断。 |

**四要素对位**：名称＝Louvre Pyramid / Hall Napoléon underground lobby（①②同一 Grand Louvre 项目）；地点＝巴黎卢浮宫 Cour Napoléon（①直书，②以现有博物馆上下范围对应）；设计者＝I. M. Pei（①直书，②为 Pei 事务所项目页）；年份＝1989（①直书落成日）。

**独立性说明**：博物馆官方与建筑师事务所官方为不同机构，分别以策展/建筑史叙述和项目档案叙述互证，可作独立双源。

**保留标注**：①称为 “central underground lobby”，②称 “Hall Napoleon with underground links”；落地时写“地下中庭/地下大厅（central underground lobby）”，避免把它误写成普通地上中庭。天窗采光以玻璃金字塔与官方 “transparent, light and luminous” 叙述支持，不虚构具体采光系数或尺寸。

### 2.3 `earth-sheltered`（覆土建筑）→ **莫斯高博物馆（Moesgaard Museum）**

- **名称**：莫斯高博物馆 / Moesgaard Museum
- **地点**：**丹麦奥胡斯南部（Aarhus, Denmark）**（①馆址 Moesgård Allé 15, DK-8270 Højbjerg；② “Aarhus, Denmark”）
- **设计者**：**Henning Larsen Architects**（① “The building was designed by Henning Larsen Architects”；②即事务所官方项目页。）
- **年份**：**2014 开馆；项目 2009–2014**（① “opened in 2014”；② “2009 - 2014”）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） | 对本空间类型的支撑 |
| --- | --- | --- | --- | --- | --- | --- |
| ① | Moesgaard Museum 官方建筑页（**强权威·博物馆官方机构**） | `https://moesgaardmuseum.dk/en/visit-us/building-and-landscape` | Building and landscape - Moesgaard | **200** | “When our exhibition building opened in 2014, Denmark gained a new cultural-historical landmark. The building was designed by Henning Larsen Architects …”；“With its staggered levels, the building is inspired by archaeological excavations which gradually uncover the layers of history.” | 官方确认开馆年、设计者，并明确建筑以错层体量模拟考古挖掘层级，支持“结合地形、部分掩覆”的覆土空间策略。 |
| ② | Henning Larsen 建筑师事务所项目页（**强权威·建筑师事务所官方**） | `https://henninglarsen.com/projects/moesgaard` | Moesgaard \| Henning Larsen | **200** | “Aarhus, Denmark”；“2009 - 2014”；“Nestled into the rolling landscape of southern Aarhus …”；“Its publicly accessible sloping roof, landscaped with grass and moss …”；“light well apertures that form terraces and allow natural light into the exhibition spaces below.” | 直接给出覆土建筑关键证据：嵌入起伏地形、草与苔藓覆盖的可上人坡屋顶、采光井把自然光送入下方展厅。 |

**四要素对位**：名称＝Moesgaard Museum（①②同一项目）；地点＝Aarhus / Højbjerg（②城市、①馆址）；设计者＝Henning Larsen Architects（①直书，②为事务所项目页）；年份＝2014 开馆、2009–2014 项目期（两源口径互补）。

**独立性说明**：业主/博物馆官方与设计方事务所官方是不同机构；一个讲公共建筑与开放屋顶，一个讲地形嵌入与草坡采光井，互证且非同一文本来源。

**保留标注**：该例是**坡地覆土/半掩覆型**覆土建筑，不是全地下住宅；落地宜写“覆土建筑的代表性公共建筑：草坡屋顶嵌入地形、展厅位于其下并由采光井补光”，避免写成完全覆土封闭体。

### 2.4 `semi-sunken-space`（半下沉空间）→ **Sunken House（Adjaye Associates）**

- **名称**：Sunken House / 下沉住宅
- **地点**：**英国伦敦 Hackney 的 De Beauvoir Town**（① “London, UK”；② “De Beauvoir town in Hackney”）
- **设计者**：**Adjaye Associates**（① “Design Architect Adjaye Associates”；②标题即 “Sunken House / Adjaye Associates”）
- **年份**：**2007**（① “Status 2007”；② “Completed in 2007 in United Kingdom”）

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（原文，实抓，已回验 FOUND） | 对本空间类型的支撑 |
| --- | --- | --- | --- | --- | --- | --- |
| ① | Adjaye Associates 官方项目页（**强权威·建筑师事务所官方**） | `https://www.adjaye.com/work/sunken-house/` | Sunken House - Adjaye Associates | **200** | “London, UK”；“Status 2007”；“Design Architect Adjaye Associates”；“the Sunken House stands in an excavated courtyard, which is not overlooked by the adjacent buildings, and the main living space is located at this level.”；“The bedrooms are on the first floor, and there is a large studio on the second floor …” | 明确住宅立于开挖庭院中，主要生活层位于下沉标高，上层仍有卧室与工作室，是“半下沉、半地上”的直接实例证据。 |
| ② | ArchDaily 项目库（**中—强权威·国际建筑媒体项目档案**） | `https://www.archdaily.com/213736/sunken-house-adjaye-associates` | Sunken House / Adjaye Associates \| ArchDaily | **200** | “Completed in 2007 in United Kingdom.”；“A three storey house in conservation area of De Beauvoir town in Hackney.”；“The site has been excavated to basement level creating a sunken patio …” | 独立确认年份、地点、三层住宅与“开挖至地下室标高形成下沉庭院”，从项目档案侧互证半下沉空间类型。 |

**四要素对位**：名称＝Sunken House（①②同名）；地点＝London, UK / De Beauvoir Town, Hackney（①国家城市、②街区）；设计者＝Adjaye Associates（①字段、②标题）；年份＝2007（两源一致）。

**独立性说明**：建筑师事务所官方与 ArchDaily 项目库为不同机构，前者给空间剖面与使用分层，后者给建成时间/地点/开挖事实，独立双源成立。

**保留标注**：ArchDaily 的关键句来自页面可见的元数据摘要（正文项目介绍在页面上受 gated-content 限制）；本条已按页面实际可见文本回验，不扩写截断后的内容。落地写“开挖庭院使主生活层下沉，卧室与工作室仍在楼上”，不将该住宅写成全地下建筑。

## 三、汇总

| 条目 | 具名实例 | 地点 | 设计者 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `sunken-garden` | 布查特花园下沉花园 The Sunken Garden | 加拿大 BC 省 Brentwood Bay / Vancouver Island Tod Inlet | Jennie Butchart（园方直书） | 园区 1904；采石坑花园化节点 1912 | Butchart Gardens 官方园史 | Communities in Bloom 全国园艺展示页 | 200 / 200 | **双源可用**；设计者仅园方命名，第二源互证园名/地点/年份 |
| `sunken-atrium` | 卢浮宫金字塔 / Hall Napoléon 地下大厅 | 法国巴黎卢浮宫 Cour Napoléon | I. M. Pei（贝聿铭） | 1989（金字塔落成 3 月 29 日） | Louvre 官方建筑史页 | PCF Architects 项目页 | 200 / 200 | **双源可用**；源①直书 central underground lobby 与采光结构 |
| `earth-sheltered` | 莫斯高博物馆 Moesgaard Museum | 丹麦 Aarhus（Højbjerg） | Henning Larsen Architects | 2014 开馆（项目 2009–2014） | Moesgaard Museum 官方建筑页 | Henning Larsen 项目页 | 200 / 200 | **双源可用**；属坡地覆土/半掩覆型，非全地下 |
| `semi-sunken-space` | Sunken House | 英国伦敦 Hackney / De Beauvoir Town | Adjaye Associates | 2007 | Adjaye Associates 官方项目页 | ArchDaily 项目库 | 200 / 200 | **双源可用**；开挖庭院+上层空间，典型半下沉住宅 |

- **双源齐备率：4/4**；8 个来源均为完整 URL、具名机构、HTTP 200，**0 条写“仅单源/不可得”**。
- **机构独立性**：8 机构互不重复：The Butchart Gardens、Communities in Bloom、Musée du Louvre、PCF Architects、Moesgaard Museum、Henning Larsen、Adjaye Associates、ArchDaily。
- **无维基作证**：Wikipedia/Wikidata/搜索结果页只用于定位线索，未列入证据表。
- **需落地时保留的诚实标注（4 处）**：
  1. `sunken-garden`：设计者 Jennie Butchart 由园方一手园史单独命名；第二源只互证园名/地点/年份。
  2. `sunken-atrium`：源①用 “central underground lobby”，源②用 “Hall Napoleon with underground links”；写“地下中庭/地下大厅”并保留原词，避免误写为地上中庭。
  3. `earth-sheltered`：Moesgaard 是坡地覆土公共建筑，写“草坡屋顶嵌入地形、展厅在其下并由采光井补光”，不写成全地下住宅。
  4. `semi-sunken-space`：ArchDaily 关键句为页面可见元数据摘要，正文有 gated-content；按可见文本引用，不扩写截断部分。
- **未做之事**：本报告未修改任何条目数据或其它项目文件；四条 `sections.实例` 现状仍须由 lead 按第一节“落地约束”另行改写并复跑 `tools/check.py`。

## 四、被拒用/未列来源记录（供后续参考，不作证据）

| URL / 类型 | 状态 | 处置 |
| --- | --- | --- |
| `https://www.britannica.com/place/Butchart-Gardens` | `web_fetch` HTTP 200，但 `urllib` 直连 404/反爬波动 | 未作证据；换用可直接回验的 Communities in Bloom 全国园艺页 |
| `https://www.thecanadianencyclopedia.ca/en/article/butchart-gardens` | HTTP 403（CloudFront） | 弃用 |
| `https://en.wikipedia.org/w/api.php` 查询结果、Google/Bing 结果页 | 仅线索页 | 不作证据 |
| `https://www.louvre.fr/en/explore/the-palace/the-pyramid` | HTTP 404（旧路径） | 改用 sitemap 中的现行页 `a-pyramid-for-a-symbol` |
| `https://www.nga.gov/visit/visit-the-east-building.html` | HTTP 403（Just a moment…） | 未作证据；地下中庭改选 Louvre + PCF 双源 |

## 五、证据回执（verification-before-completion）

逐条 `norm(quote) in norm(page)` 子串回验结果；`FOUND` 才写入正文。

| 来源 | 回验句（缩写） | 结果 |
| --- | --- | --- |
| Butchart Gardens 官方园史 | “Robert and Jennie Butchart moved to Vancouver Island … Tod Inlet” / “Jennie envisioned a grand garden in its place” / “the quarry blossomed into today’s Sunken Garden” | FOUND |
| Communities in Bloom | “Established in 1904” / “located in Brentwood Bay, British Columbia” / “including the iconic Sunken Garden” / “As a National Historic Site of Canada” | FOUND |
| Louvre 官方 | “central underground lobby affording direct access to the museum’s three wings” / “inaugurated on 29 March 1989” / “Chinese-American architect Ieoh Ming Pei” / “most transparent, light and luminous structure possible” | FOUND |
| PCF Architects | “Hall Napoleon with underground links to museum wings” / “including areas within and below the existing museum” | FOUND |
| Moesgaard Museum 官方 | “opened in 2014” / “designed by Henning Larsen Architects” / “staggered levels … inspired by archaeological excavations” | FOUND |
| Henning Larsen 官方 | “Aarhus, Denmark” / “2009 - 2014” / “Nestled into the rolling landscape” / “sloping roof, landscaped with grass and moss” / “allow natural light into the exhibition spaces below” | FOUND |
| Adjaye Associates 官方 | “London, UK” / “Status 2007” / “Design Architect Adjaye Associates” / “stands in an excavated courtyard” / “main living space is located at this level” / “bedrooms are on the first floor” | FOUND |
| ArchDaily | “Completed in 2007 in United Kingdom” / “conservation area of De Beauvoir town in Hackney” / “excavated to basement level creating a sunken patio” | FOUND |

> 校验方法：UTF-8 解码 → 去 script/style 与标签 → `html.unescape` → `norm()`（NFKC + 弯直引号/破折号/零宽空格/不间断空格归一 + 空白折叠 + 小写）→ 子串命中。HTTP 与 `<title>` 来自同一轮实抓；表中 200 均为实际响应码。
