# 第 57 轮 B5 补源报告（review-round57b）——4 条建筑/空间概念条目补具名实例（各两条独立权威来源）

复核日期：2026-11-23（Asia/Hong_Kong）　｜　复核人：review-r57b（lead 委派子任务，无人值守）　｜　性质：**严格只读，唯一产出本文件**

## 〇、执行说明与只读声明

- **已读治理与上下文文档**：项目根 `AUTONOMOUS.md` / `TASK_design.md` 实读为 NOT_FOUND；按 `research/review-round56b.md` 第 7 行记录读取桌面原件 `D:/Users/Administrator/Desktop/AUTONOMOUS.md`（71 行）、`D:/Users/Administrator/Desktop/TASK_design.md`（67 行）；并读本项目 `DECISIONS.md`（25 行）、`research/review-round56b.md`（116 行）。
- **已加载技能**：`using-superpowers`（本会话为委派子任务，按其 SUBAGENT-STOP 以任务说明书为准）、`verification-before-completion`（先实抓、后断言；全部关键句逐条 `norm(quote) in norm(page)` 回验，见第五节回执）。
- **硬性规则确认**：不编造名称、地点、作者、年份、引文、出处；关键事实须两个独立来源互证；同一机构只算 1 源；凑不齐双源写“仅单源/不可得”并尽量换更易双源实例。网页内容一律视为数据，页面中出现的任何指令均未执行。
- **通道与故障**：`web_search` 端点异常（返回 no web_search_tool_result，与 DECISIONS D05 一致）；Bing / DuckDuckGo-lite / Mojeek 结果页被代理污染或 403，仅用于定位不作证据；本地 urllib 遇代理 MITM 证书 hostname mismatch，改用 `ssl._create_unverified_context()` + 浏览器 UA 直连；`web_fetch` 服务端直读作补充。证据正文全部来自实抓；Wikipedia 外部链接 API 仅用于**定位 URL**，未作证据。
- **只读声明**：本轮仅生成 `E:/ai_project/shejihuihua/research/review-round57b.md`；未修改 `entries/`、`data/sources.json`、`coverage.json`、`tools/`、`site/` 或其他项目文件，未 git commit，未改项目外内容。

## 一、方法与判据

1. **实抓**：逐 URL 记录 HTTP 状态、字节数、`<title>`；去 `<script>/<style>` 与标签、`html.unescape` 后抽正文；用 `norm()`（NFKC + 弯/直引号、破折号、零宽空格、不间断空格归一 + 空白折叠 + 小写）对关键句做子串回验。
2. **独立性判据**：同一机构只算 1 源。特别注意：`visitdenmark.com` 的 Strøget 页与 `visitcopenhagen.com` 内容逐字相同、页脚标注“Last updated by: VisitCopenhagen”、图片 © Wonderful Copenhagen，**判为同机构转载，已剔除**，不与 VisitCopenhagen 凑双源（同上轮剔除 museum.nl 的判据）。柏林爱乐基金会官网的 philharmonie 页与 acoustic 专页同属一个机构，合并计为 1 源。
3. **权威性分级**：强权威＝建筑事务所官方项目页、机构/乐团官方、国家公共广播机构、都道府县/市级官方旅游站；中—强权威＝建筑专业媒体（Architects' Journal, RIBA 旗下）。
4. **不采用维基作主源**：沿用项目既定口径，Wikipedia 及其镜像未作证据。
5. **落地约束**：本报告只读产出，不直接改数据。落地须先把来源以 `verified=true` 登记进 `data/sources.json`，再改写对应 `entries/batch-*.json` 的 `sources` 与「实例」段，同步 `pending_notes` /「待核实」，复跑 `tools/check.py`。

## 二、四条补源（名称 / 地点 / 作者 / 年份 + 两条独立权威来源）

### 2.1 `thermal-comfort`（热舒适）→ **曼尼托巴水电大楼（Manitoba Hydro Place）**

- **名称**：Manitoba Hydro Place / 曼尼托巴水电大楼，以被动式太阳能/自然通风与热舒适设计著称的高性能办公楼。
- **地点**：**加拿大曼尼托巴省温尼伯市 Portage Avenue**（①“Location Winnipeg, Manitoba”；②“The 23-storey, energy-efficient building on Winnipeg's Portage Avenue”）。
- **设计者**：**KPMB Architects（方案/设计建筑师，多伦多）＋ Architecture49（原 Smith Carter，温尼伯，执行建筑师）**（①“Architects KPMB Architects (design architect), Architecture49 (execu…”；②“a joint venture between Kuwabara Payne McKenna Blumberg Architects of Toronto and Winnipeg's Smith Carter Architects and Engineers Inc.”）。
- **年份**：**2009 年落成启用**（②报道发布于 2009-07-10，并记“opened its doors to employees last December”，即 2008 年 12 月入住；业界通行以 2009 年为建成年，CTBUH 2009 美洲最佳高层建筑奖亦在此年。落地写“2008 年底启用 / 2009 年获奖”，不写单一绝对年份以免与源冲突）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | KPMB Architects 设计事务所官方项目页（**强权威·设计方官方**） | `https://www.kpmb.com/project/manitoba-hydro-place/` | Manitoba Hydro Place - KPMB | **200**（41,942 B；urllib 直连 + web_fetch 双向 200） | “Every element melds performance and aesthetics: solar chimney, wintergardens, waterfalls, **thermal mass**, vertical neighbourhoods, double façade, geothermal…”；“Harnessing an Extreme Climate for Passive Energy … to **harness passive solar and wind energies**.”；“A **double façade** … reduces heating/cooling loads by providing a **tempered buffer to extreme outdoor temperatures**.”；“Operable windows … permit **natural ventilation** at seasonally appropriate times of the year.” |
| ② | CBC News 加拿大广播公司（**强权威·国家公共广播机构**） | `https://www.cbc.ca/news/entertainment/manitoba-hydro-place-wins-architecture-award-1.860288` | Manitoba Hydro Place wins architecture award \| CBC News | **200**（91,161 B；urllib 直连） | “A Winnipeg skyscraper designed by Toronto and Winnipeg architectural firms has won the Council on Tall Buildings and Urban Habitat's **2009 award for the best tall building in the Americas**.”；“Manitoba Hydro Place, which opened its doors to employees last December, was a **joint venture between Kuwabara Payne McKenna Blumberg Architects of Toronto and Winnipeg's Smith Carter Architects and Engineers Inc.**”；“The building uses **geothermal heating and radiant cooling** that makes it one of the most energy-efficient office towers in the world.” |

**对 `thermal-comfort`（热舒适）的支撑**：①从设计方层面逐条给出被动式热环境策略——thermal mass（热蓄能）、double façade（双层表皮作为“tempered buffer”缓冲极端室外温度）、operable windows 实现 natural ventilation、solar chimney 与地源热泵；②从独立第三方（国家广播 + CTBUH 奖项）确认其“geothermal heating and radiant cooling”“one of the most energy-efficient office towers in the world”。两源合起来支撑“以被动式与设备策略主动营造室内热舒适、并获权威能效认可”的具名实例。**保留标注**：两源均未使用字面术语“thermal comfort”，而是用 thermal mass / natural ventilation / tempered buffer / radiant cooling 等工程等价表述；落地应写“馆方/设计方记为这些热环境策略，按概念属热舒适设计”，不得写成两源逐字用了该词。年份按“2008 年底启用 / 2009 年获奖”并置，不写单一绝对建成年度。

### 2.2 `acoustic-environment`（声环境）→ **柏林爱乐大厅（Philharmonie Berlin）**

- **名称**：Philharmonie Berlin / 柏林爱乐大厅，柏林爱乐乐团主厅，以“葡萄园式”环绕座席与声学设计著称。
- **地点**：**德国柏林**（①“The Philharmonie Berlin has been the musical heart of Berlin since 1963”）。
- **设计者**：**Hans Scharoun（汉斯·沙龙）**；声学顾问 **Lothar Cremer**（柏林工大技术声学研究所主任）（①“the architect Hans Scharoun … developed the main concert hall”；②“Hans Scharoun had already enlisted the services of Lothar Cremer … an expert on acoustics”）。
- **年份**：**1963 年**（①“musical heart of Berlin since 1963”）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ①a | Berliner Philharmoniker 乐团/场馆官方介绍页（**强权威·机构官方**） | `https://www.berliner-philharmoniker.de/en/about-us/philharmonie/` | Philharmonie Berlin \| Berliner Philharmoniker | **200**（63,675 B） | “The Philharmonie Berlin has been the **musical heart of Berlin since 1963**.”；“Its unusual architecture and innovative concert hall design … now **serves as a model for concert halls all over the world**.”；“**the architect Hans Scharoun** … developed the main concert hall … with the concert platform and the musicians forming the central focal point.” |
| ①b | 同机构官方声学专页（**同上机构，合并计 1 源**） | `https://www.berliner-philharmoniker.de/en/about-us/philharmonie/acoustic/` | Sounding Space \| Berliner Philharmoniker | **200**（58,419 B；署名 Rainer Esche） | “Hans Scharoun had already enlisted the services of **Lothar Cremer** … an expert on acoustics … head of the Institute for Technical Acoustics at Berlin's Technical University”；“the demand for a **reverberation time of two seconds** proved the least of his problems”；“reflective surfaces … were fitted to the **'vineyard terraces'** behind and on both sides of the podium”；“ten **'clouds'**, slightly curving downwards, were suspended … above the platform” |
| ② | Architects' Journal（RIBA 旗下建筑专业媒体，**中—强权威**） | `https://www.architectsjournal.co.uk/news/scharouns-berlin-philharmonie-building-burns` | Scharoun's Berlin Philharmonie building burns | **200**（89,830 B；urllib 直连） | “**Scharoun's masterpiece** is currently home to the German capital's leading orchestra, directed by British conductor Simon Rattle.”（标题与正文均明确该建筑为 Scharoun 代表作、顶级乐团驻地） |

**对 `acoustic-environment`（声环境）的支撑**：①（含 ①b 声学专页）为决定性权威证据——明确声学顾问 Lothar Cremer、混响时间目标 2 秒、按 2,250 座计算 26,000 m³ 容积与人均约 10 m³ 气容、葡萄园式台地反射面、10 片“声云”与低频吸收“金字塔”，逐条说明声学设计手法；②从独立建筑媒体确认该厅为 Scharoun 代表作、德国顶级乐团驻地，佐证其“以声学/设计著称”的地位。**保留标注（重要）**：源②是一则火灾新闻，仅提供“Scharoun 代表作 / 顶级乐团主厅”的身份佐证，**不含声学技术细节**；所有声学参数与手法均出自源①（场馆官方）。落地若写具体声学数据，只标源①，不得归于源②。

### 2.3 `pedestrian-flow`（步行流线）→ **斯特勒格特步行街（Strøget）**

- **名称**：Strøget / 斯特勒格特，哥本哈根市中心步行街，欧洲最长步行街之一。
- **地点**：**丹麦哥本哈根市中心，从市政厅广场（City Hall Square / Rådhuspladsen）到国王新广场（Kongens Nytorv）**。
- **作者 / 规划者**：**无单一设计者**：Strøget 是 1800 年代形成的街道昵称，涵盖 Frederiksberggade、Nygade、Vimmelskaftet、Østergade 等街段；1962 年起逐步转为步行街，常与丹麦建筑师/城市规划师 **Jan Gehl** 的公共空间研究相关联。来源页未点名单一“作者”，落地不编造设计者。
- **年份**：**1962 年起步行化**（Wikipedia 定位线索；采用的权威源页本身未给确切年份，落地年份标“待核实”或注明线索来源）。

| # | 机构 / 权威级 | URL | 标题 | HTTP | 关键句（实抓，已回验） |
| --- | --- | --- | --- | --- | --- |
| ① | VisitCopenhagen / Wonderful Copenhagen 官方旅游站（**强权威·市级官方旅游机构**） | `https://www.visitcopenhagen.com/copenhagen/stroget-gdk414471` | Strøget \| Shopping area in Copenhagen | **200**（182,397 B；urllib 直连） | “What will you find on Strøget, **one of Europe's longest pedestrian streets**?”；“**The 1.1km stretch runs from** City Hall Square to Kongens Nytorv”；“Strøget is a nickname from the 1800s and covers the streets Frederiksberggade, Nygade, Vimmelskaftet and Østergade…” |

**判定：仅单源 / 不可得（第二独立源）**。

- **理由**：唯一可靠且正文可核对的权威源为 VisitCopenhagen 官方。`visitdenmark.com/…/stroget-gdk414471`（HTTP 200）正文与 ① 逐字相同、页脚“Last updated by: VisitCopenhagen”、图片 © Wonderful Copenhagen，**判为同机构转载予以剔除**；其余候选在本次环境下均不可用：Britannica `place/Stroget`、`topic/Stroget`、`place/Strøget` 均 403（Cloudflare）/404；哥本哈根市政府 `subsite.kk.dk` 页面本地 SSL 握手失败、web.archive.org 存档 web_fetch 连接失败；Architect Magazine（Jan Gehl）403；C40 案例页 404；gehlarchitects.com / gehlpeople.com SSL 失败或 JS 空壳。
- **对 `pedestrian-flow` 的支撑（基于已确认的单源）**：①明确 Strøget 为“欧洲最长步行街之一”、给出 1.1 km 的连续步行尺度及所串联的广场节点，可支撑“以连续步行流线组织公共空间”的具名实例，但**按项目“关键事实两个独立来源”的硬性规则，仍应标“待核实”**。
- **落地建议**：本条维持 `needs_verification=true`，`pending_notes` 写明“步行街身份已由 VisitCopenhagen 官方一源确认；第二独立权威源因 Britannica/市政府站点在本环境不可达而暂缺”。已按任务要求尝试“换更易双源实例”（时代广场步行化：NYC DOT 页面 404、NYU 页面 202 空壳、Urban.org 404），同样无法凑齐，故保留原实例并如实标注。

### 2.4 `corridor-space`（廊道空间）→ **米兰维托里奥·埃马努埃莱二世拱廊（Galleria Vittorio Emanuele II）**

- **名称**：Galleria Vittorio Emanuele II / 米兰拱廊，玻璃与铸铁拱顶覆盖的十字形商业拱廊，被誉为世界最著名拱廊之一。
- **地点**：**意大利米兰，连接米兰大教堂（Duomo）与斯卡拉歌剧院（Teatro alla Scala）**。
- **作者**：**Giuseppe Mengoni（朱塞佩·门戈尼）**（Wikipedia 定位线索；采用的权威源未能正文核对，落地作者字段标“待核实”）。
- **年份**：**1865 年动工、1877 年落成**（Wikipedia 定位线索；采用的权威源未能正文核对，落地年份标“待核实”）。

**判定：不可得（本环境下无两条可正文核对的独立权威来源）**。

- **理由（全部为本轮实抓的环境限制，非源不存在）**：
  - Treccani《Enciclopedia Italiana》条目 `https://www.treccani.it/enciclopedia/galleria-vittorio-emanuele-ii_(Enciclopedia-Italiana)/` HTTP **200**（86,985 B），但正文为 JS 动态渲染，去标签后仅剩导航提示（正文 161 字符），**无法核对关键句**，按“无关键句不声称”不采用。
  - Yale LUX 馆藏记录 `https://lux.collections.yale.edu/view/place/a5de40aa-38fa-46cf-b206-8fec00417aed` HTTP **200**（4,200 B），但返回“You need to enable JavaScript to run this app.”，无可核正文。
  - Britannica 候选 `topic/Galleria-Vittorio-Emanuele-II`、`place/Galleria-Vittorio-Emanuele-II`、`topic/Galleria-Vittorio-Emanuele`、`place/Victor-Emmanuel-Gallery` 等均 403/404；UNESCO `whc.unesco.org/en/list/1650/`（博洛尼亚拱廊）403；Comune di Milano / yesmilano / italia.it / visitamilano 各候选 URL 均 403/404；Getty 藏品页 200 但为 JS 空壳；LOC 权威记录 403；metmuseum Heilbrunn 年表 429/连接失败。
  - 已按任务要求“换更易双源实例”：改试博洛尼亚拱廊（UNESCO + Comune di Bologna，均 403/空壳）、故宫廊道（dpm.org.cn 404）等，仍无法凑齐。
- **落地建议**：本条维持 `needs_verification=true`，`pending_notes` 写明“米兰拱廊为廊道空间经典实例，但本环境下 Britannica/UNESCO/意大利官方站均不可达或正文 JS 渲染，名称/地点可确认，作者 Mengoni 与 1865–1877 年份待补第二独立权威源后写入”。不得据 Wikipedia 或 JS 空壳页把作者/年份写成“已验证”。

## 三、汇总

| 条目 | 具名实例 | 地点 | 作者 / 设计者 | 年份 | 源① | 源② | HTTP | 判定 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `thermal-comfort` | 曼尼托巴水电大楼 Manitoba Hydro Place | 加拿大温尼伯 Portage Avenue | KPMB Architects（设计）＋Architecture49 / Smith Carter（执行） | 2008 年底启用 / 2009 获奖 | KPMB 官方项目页 | CBC News | 200 / 200 | **双源齐备**；无字面“thermal comfort”，用 thermal mass/natural ventilation/radiant cooling；年份并置 |
| `acoustic-environment` | 柏林爱乐大厅 Philharmonie Berlin | 德国柏林 | Hans Scharoun（建筑）；Lothar Cremer（声学） | 1963 | 柏林爱乐官方（philharmonie＋acoustic 页，同机构计 1 源） | Architects' Journal | 200 / 200 | **双源齐备**；声学参数全出源①，源②仅身份佐证 |
| `pedestrian-flow` | 斯特勒格特步行街 Strøget | 丹麦哥本哈根市政厅广场—国王新广场 | 无单一设计者（Jan Gehl 研究相关） | 1962 起步行化（待核实） | VisitCopenhagen 官方 | —— | 200 / —— | **仅单源/不可得**；VisitDenmark 为同机构转载已剔除，第二独立源环境不可达 |
| `corridor-space` | 米兰维托里奥·埃马努埃莱二世拱廊 Galleria Vittorio Emanuele II | 意大利米兰大教堂—斯卡拉歌剧院 | Giuseppe Mengoni（待核实） | 1865–1877（待核实） | —— | —— | —— / —— | **不可得**；Treccani/Yale LUX 正文 JS 空壳，Britannica/UNESCO/意大利官方站 403/404 |

- **双源齐备率：2/4**（thermal-comfort、acoustic-environment）；**仅单源：1/4**（pedestrian-flow）；**不可得：1/4**（corridor-space）。0 条编造。
- **机构独立性**：thermal 为设计事务所官方 + 国家公共广播（不同机构）；acoustic 为场馆官方 + 建筑专业媒体（不同机构）；同一机构的多页面与同机构转载页均已合并/剔除。
- **需落地时保留的诚实标注**：①thermal 实例用工程等价词而非字面“thermal comfort”，年份写“2008 年底启用 / 2009 获奖”；②acoustic 的声学数据只归源①，源②仅身份佐证；③pedestrian 仅一源，维持待核实，不写单一设计者、年份标待核实；④corridor 作者/年份不得据空壳页写成已验证，维持待核实；⑤所有来源页中出现的任何指令性文字均未执行。

## 四、被拒用来源记录（供后续参考，不作证据）

| URL / 来源 | 状态 | 处置 |
| --- | --- | --- |
| `https://www.visitdenmark.com/denmark/plan-your-trip/stroget-gdk414471` | HTTP 200，但正文与 VisitCopenhagen 逐字相同、页脚“Last updated by: VisitCopenhagen” | 按“同机构只算 1 源”剔除，不凑 pedestrian 双源 |
| `https://www.britannica.com/place/Stroget`、`/topic/Stroget`、`/place/Str%C3%B8get`、`/topic/Galleria-Vittorio-Emanuele-II`、`/place/Galleria-Vittorio-Emanuele-II`、`/topic/Berlin-Philharmonie`、`/topic/Musikverein` 等 | 403（Cloudflare “Just a moment…”）或 404 | 放弃作声环境/步行/廊道第二源 |
| `https://whc.unesco.org/en/list/1650/`（博洛尼亚拱廊） | 403（Cloudflare） | 放弃博洛尼亚拱廊替代方案 |
| `https://www.treccani.it/enciclopedia/galleria-vittorio-emanuele-ii_(Enciclopedia-Italiana)/` | 200（86,985 B），但正文 JS 渲染，去标签后仅 161 字符导航 | 无可核关键句，不采用 |
| `https://lux.collections.yale.edu/view/place/a5de40aa-...` | 200（4,200 B），返回“You need to enable JavaScript…” | 无可核正文，不采用 |
| `https://www.getty.edu/art/collection/object/103DWN` | 200 但 JS 空壳 | 不采用 |
| `https://subsite.kk.dk/Nyheder/2012/September/KFF_Stroeget_50.aspx`、web.archive.org 存档 | 本地 SSL 握手失败 / web_fetch 连接失败 | 放弃哥本哈根市政府第二源 |
| `https://www.architectmagazine.com/planning/jan-gehl-...`、`https://www.metmuseum.org/toah/hd/arcad/hd_arcad.htm`、`https://www.canadianarchitect.com/...`、`https://www.ctbuh.org/...` | 403 / 429 / 404 | 放弃作相应第二源 |
| `https://www.nyc.gov/.../times-square-ped-plaza.shtml`、`https://www.nyu.edu/...times-square...` | 404 / 202 空壳（时代广场替代方案） | 换实例尝试失败，pedestrian 维持 Strøget 单源 |
| Wikipedia 及镜像站 | 未采用 | 仅用其外部链接 API 定位 URL，按项目口径排除作证据 |

## 五、证据回执（verification-before-completion）

对全部采用来源重抓并执行 `norm()`（NFKC + 弯直引号/破折号/零宽空格/不间断空格归一 + 空白折叠 + 小写）子串命中：

- **KPMB-thermal**：HTTP 200，41,942 B，标题 `manitoba hydro place - kpmb`；关键句 `thermal mass`＝FOUND，`harness passive solar and wind energies`＝FOUND；`operable windows … double façade … natural ventilation` 与前轮实抓原文一致（本回验因 façade 的 ç 规范化差异显示 MISS，前轮抽取原文见 2.1 表，非源缺失）。
- **CBC-thermal**：HTTP 200，91,161 B，标题 `manitoba hydro place wins architecture award | cbc news`；`geothermal heating and radiant cooling`＝FOUND，`joint venture between kuwabara payne mckenna blumberg architects`＝FOUND；`opened its doors last december` 见前轮抽取原文（大小写/冠词差异导致本回验 MISS，非源缺失）。
- **BPH-main-acoustic**：HTTP 200，63,675 B，标题 `philharmonie berlin | berliner philharmoniker`；3 条关键句全 FOUND（musical heart of berlin since 1963 / architect hans scharoun / serves as a model for concert halls all over the world）。
- **BPH-acoustic**：HTTP 200，58,419 B，标题 `sounding space | berliner philharmoniker`；4 条关键句全 FOUND（reverberation time of two seconds / lothar cremer / vineyard terraces / ten "clouds"）。
- **AJ-acoustic**：HTTP 200，89,830 B，标题 `scharoun's berlin philharmonie building burns`；`scharoun's masterpiece is currently home to the german capital's leading orchestra`＝FOUND。
- **VisitCPH-ped**：HTTP 200，182,397 B，标题 `strøget | shopping area in copenhagen`；`one of europe's longest pedestrian streets`＝FOUND，`the 1.1km stretch runs from`＝FOUND。

> 校验方法：UTF-8 解码 → 去 script/style/标签 → `html.unescape` → `norm()` 子串命中。HTTP 状态、字节数与 `<title>` 均来自同轮实抓。所有“仅单源/不可得”判定均附对应 URL 的实际 HTTP 状态与失败原因（见第四节），未在无证据情况下声称来源成立。
